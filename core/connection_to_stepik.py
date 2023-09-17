from datetime import datetime
from typing import Any

import requests
from requests.auth import HTTPBasicAuth

from core.constants.defaults import (
    STEPIK_CLIENT_ID,
    STEPIK_CLIENT_SECRET, AUTH_DATA
)
import pandas as pd
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
            course_payments: pd.DataFrame
    ) -> [pd.DataFrame, bool]:
        response_json = requests.get(
            COURSE_PAGE_URL.format(course=course, page=page_num),
            headers=self.headers
        ).json()

        page_payments = pd.DataFrame(
            data=response_json.get("course-payments")
        )

        if page_payments.empty:
            return course_payments, False

        page_payments = page_payments[
            page_payments["status"] == "success"
            ]
        page_payments["user_name"] = [
            self.__get_user_name(user_id=user_id)
            for user_id in page_payments["user"]
        ]
        page_payments["course_name"] = [
            self.__get_course_name(course_id=course_id)
            for course_id in page_payments["course"]
        ]
        page_payments["date"] = [
            date_to_rus_format(date=payment_date)
            for payment_date in page_payments["payment_date"]
        ]
        page_payments["promo_code"] = [
            promo if promo else ""
            for promo in page_payments["promo_code"]
        ]

        page_payments = page_payments[[
            "amount",
            "course",
            "course_name",
            "date",
            "promo_code",
            "user",
            "user_name",
            "payment_date",
        ]].rename(
            columns={
                "amount": "Цена",
                "course": "ID курса",
                "course_name": "Имя курса",
                "date": "Дата покупки",
                "promo_code": "Промокод",
                "user": "ID пользователя",
                "user_name": "Имя пользователя",
                "payment_date": "Точная дата и время покупки",
            }
        )

        course_payments = pd.concat(
            [course_payments, page_payments],
            ignore_index=True,
        )

        return course_payments, response_json["meta"]["has_next"]

    def get_payments(self, courses: Any) -> pd.DataFrame:
        """
        TODO -> + docstring
        :param courses:
        :return:
        """

        course_payments = pd.DataFrame()
        for course in courses:
            page_num = 0
            has_next = True
            while has_next:
                page_num += 1
                print(f"course: {course}, page: {page_num}")
                course_payments, has_next = self.__add_payments_from_page(
                    course=course,
                    page_num=page_num,
                    course_payments=course_payments
                )

        return course_payments.sort_values(by=["Точная дата и время покупки"])
