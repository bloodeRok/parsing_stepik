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


class GoogleSheet(IntEnum):
    all_index = 0
    ds_index = 1
    analytics_index = 2
    test_all_index = 3
    test_ds_index = 4
    test_analytics_index = 5
