from is_today import is_data_today
def data_filtering(data: dict[str, str]) -> dict[str, str]:
    is_today = is_data_today(data['date'])
    if is_today:
        return data