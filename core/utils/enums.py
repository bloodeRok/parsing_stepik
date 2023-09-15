from enum import Enum, IntEnum


class Courses(Enum):
    ds = [
        93963,
        93964,
        93962,
        93965,
        89437,
        89440,
        92038,
        83861,
        90702,
        96896,
        99445,
        100626,
        94351,
        96146,
        98107,
        94350,
        96145,
        98106,
        90686,
        94772,
        98104
    ]
    analytics = [
        115951,
        112072,
        115952,
        115950,
        112076,
        115949,
        115943,
        112077,
        115948
    ]


class Columns(IntEnum):
    amount = 2
    course = 3
    payment_date = 4
    promo_code = 5
    user = 6
    user_name = 7
    course_name = 8
