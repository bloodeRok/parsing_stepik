from datetime import datetime

from core.connection_to_stepik import StepikConnect
from core.utils.enums import Courses

stepik_connection = StepikConnect()
payments = {}

start_date = datetime.now()

payments["ds"] = stepik_connection.get_payments(
    courses=Courses.ds.value
)
payments["analytics"] = stepik_connection.get_payments(
    courses=Courses.analytics.value
)


a = 5
