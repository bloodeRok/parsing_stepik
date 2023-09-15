from datetime import datetime
from typing import Any

import requests
from requests.auth import HTTPBasicAuth

from core.constants.defaults import (
    STEPIK_CLIENT_ID,
    STEPIK_CLIENT_SECRET, AUTH_DATA
)
from core.constants.urls import AUTH_URL, COURSE_PAGE_URL, USER_URL, COURSE_URL
from core.exceptions import NotAcceptable, Unauthorized
from core.utils.formatters import date_to_rus_format


class StepikConnect:

    def __init__(self):
        """
        Connects to Stepik and authorized.

        :raises NotAcceptable: when URL is unavailable
            or returned not 200 status code.
        :raises Unauthorized: when cannot authorize.
        """

        auth = HTTPBasicAuth(
            STEPIK_CLIENT_ID,
            STEPIK_CLIENT_SECRET
        )

        try:
            response = requests.post(url=AUTH_URL, data=AUTH_DATA, auth=auth)
        except requests.exceptions.RequestException:
            raise NotAcceptable("Stepik URL недоступен.")

        if response.status_code != 200:
            raise NotAcceptable(
                f"Stepik URL вернул статус код: {response.status_code}."
            )

        token = response.json().get('access_token', None)
        if not token:
            raise Unauthorized

        self.token = token
        self.headers = {'Authorization': 'Bearer ' + token}

    @staticmethod
    def __get_user_name(user_id: int) -> str:
        return requests.get(
            url=USER_URL.format(user_id=user_id)
        ).json()["users"][0]["full_name"]

    def __get_course_name(self, course_id: int) -> str:
        return requests.get(
            url=COURSE_URL.format(course_id=course_id),
            headers=self.headers
        ).json()["courses"][0]["title"]

    def __add_payments_from_page(
            self,
            course: int,
            page_num: int,
            payments: list[dict[str, Any]]
    ) -> bool:
        response_json = requests.get(
            COURSE_PAGE_URL.format(course=course, page=page_num),
            headers=self.headers
        ).json()

        all_payments = response_json.get("course-payments")
        if not all_payments:
            return False

        for payment in all_payments:
            if payment["status"] == "success":
                try:
                    amount = int(float(payment["amount"]))
                except TypeError:
                    amount = ""
                payments.append(
                    {
                        "amount": amount,
                        "course": course,
                        "payment_date": date_to_rus_format(
                            date=payment["payment_date"]
                        ),
                        "promo_code": payment["promo_code"],
                        "user": payment["user"],
                        "user_name": self.__get_user_name(
                            user_id=payment["user"]
                        ),
                        "course_name": self.__get_course_name(course_id=course)
                    }
                )
                print(f"course({course}), page({page_num}): {payment}")
        return response_json["meta"]["has_next"]

    def get_payments(self, courses: Any) -> list[dict[str, Any]]:
        """
        TODO -> + docstring
        :param courses:
        :return:
        """

        payments = []
        start_date = datetime.now()
        for course in courses:
            page_num = 0
            has_next = True
            while has_next:
                page_num += 1
                has_next = self.__add_payments_from_page(
                    course=course,
                    page_num=page_num,
                    payments=payments
                )

        return payments
