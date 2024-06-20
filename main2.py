import os
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
from database.Databese import AirQualityDatabase
from air_quality_data import get_data

def initialize_database():
    '''Create instacje obcject database'''
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    return AirQualityDatabase(user, password, host=host)

def process_sensor_data(db):
   '''Get data for one id sensor'''
   for ids in db.get_data("Sensors"):
        data = get_data(ids[0])
        key = data["key"]
        values = data["values"]
        process_values(db, key, values, ids[0])

def add_air_quality_data(db, key, item, sensor_id):
    '''Save data to database'''
    data_data = db.get_data('air_quality')
    db.add_air_quality_data(len(data_data) + 1, key, item["date"], item["value"], sensor_id)

def process_values(db, key, values, sensor_id):
    '''Checking the measurement date if it is today, saves this data to the database'''
    if isinstance(values, list):
        for item in values:
            date_st = item['date'][:10]
            date_now = datetime.today().date()
            date_str = date_now.strftime("%Y-%m-%d")
            is_today = date_str == date_st
            if is_today:
                add_air_quality_data(db, key, item, sensor_id)
                sleep(15)
            break

def main():
    db = initialize_database()
    process_sensor_data(db)

if __name__ == '__main__':
    main()