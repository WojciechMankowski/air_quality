import os
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
from Databese import AirQualityDatabase  # Assuming the module and class are imported correctly
from air_quality_data import get_data  # Assuming the module and function are imported correctly


def initialize_database():
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    return AirQualityDatabase(user, password, host=host)


def process_sensor_data(db):
    for ids in db.get_data("Sensors"):
        data = get_data(ids[0])
        key = data["key"]
        values = data["values"]
        process_values(db, key, values, ids[0])


def process_values(db, key, values, sensor_id):
    if isinstance(values, list):
        for item in values:
            date_st = item['date'][:10]
            date_now = datetime.today().date()
            date_str = date_now.strftime("%Y-%m-%d")
            is_today = date_str == date_st
            if is_today:
                add_air_quality_data(db, key, item, sensor_id)
                sleep(15)


def add_air_quality_data(db, key, item, sensor_id):
    data_data = db.get_data('air_quality')
    db.add_air_quality_data(len(data_data) + 1, key, item["date"], item["value"], sensor_id)


def main():
    db = initialize_database()
    process_sensor_data(db)


if __name__ == "__main__":
    main()
