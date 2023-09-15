def date_to_rus_format(date: str) -> str:
    return "-".join(date.split("T")[0].split("-")[::-1])
