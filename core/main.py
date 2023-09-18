import logging
import traceback
from datetime import datetime

import schedule

from handlers import GoogleTableHandler


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


def get_time():
    print(datetime.now())


def start():
    print("Program started!")
    add_payments_to_google_table()


if __name__ == "__main__":
    start()
