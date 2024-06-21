from datetime import datetime
def is_data_today(date: str) -> bool:
    today = datetime.now().strftime("%Y-%m-%d")
    return  today == date[:10]