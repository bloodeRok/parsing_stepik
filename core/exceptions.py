class NotAcceptable(Exception):
    status_code = 406
    default_detail = "Пользователь ввёл некорректные данные."


class Unauthorized(Exception):
    status_code = 401
    default_detail = "Не удалось авторизоваться."
