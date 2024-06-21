from datetime import datetime
def is_data_today(date: str) -> bool:
    now = datetime.now()
    today = datetime(now.year, now.month, now.day, now.hour -1, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
    return  today == date