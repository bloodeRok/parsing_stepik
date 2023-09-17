import logging
import traceback
from datetime import datetime

import schedule

from core.handlers import GoogleTableHandler


def add_payments_to_google_table():
    try:
        run_time = GoogleTableHandler().put_all_payments_to_google_sheet()
        print("Success")
        print(f"Run time: {run_time}")
        print(f"Current date and time: {datetime.now()}")
    except Exception:
        logging.error(traceback.format_exc())
        print("Something went wrong!")
        exit()


def start():
    schedule.every(30).minutes.do(add_payments_to_google_table)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    start()
