from datetime import datetime, timedelta

import gspread
import pandas as pd
from gspread_dataframe import set_with_dataframe

from connection_to_stepik import StepikConnect
from constants.defaults import GOOGLE_SHEET_CREDENTIALS, GOOGLE_SHEET_ID
from utils.enums import Courses, GoogleSheet

stepik_connection = StepikConnect()


class GoogleTableHandler:
    def __init__(self):
        google_auth = gspread.service_account_from_dict(
            GOOGLE_SHEET_CREDENTIALS
        )
        self.google_table = google_auth.open_by_key(key=GOOGLE_SHEET_ID)

    @staticmethod
    def __get_all_payments_data() -> dict:
        payments = {
            "ds": stepik_connection.get_payments(
                courses=Courses.ds.value
            ),
            "analytics": stepik_connection.get_payments(
                courses=Courses.analytics.value
            )
        }

        return payments

    def put_all_payments_to_google_sheet(self) -> timedelta:

        start_date = datetime.now()

        payments = self.__get_all_payments_data()

        test_all_sheet = self.google_table.get_worksheet(
            index=GoogleSheet.all_index.value
        )
        test_ds_sheet = self.google_table.get_worksheet(
            index=GoogleSheet.ds_index.value
        )
        test_analytics_sheet = self.google_table.get_worksheet(
            index=GoogleSheet.analytics_index.value
        )

        all_payments = pd.concat(
            [payments["ds"], payments["analytics"]],
            ignore_index=True
        ).sort_values(by=["Точная дата и время покупки"])

        set_with_dataframe(test_all_sheet, all_payments)
        set_with_dataframe(test_ds_sheet, payments["ds"])
        set_with_dataframe(test_analytics_sheet, payments["analytics"])

        return datetime.now() - start_date
