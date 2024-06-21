from os import getenv
from typing import List
from dotenv import load_dotenv
from database.Databese import AirQualityDatabase

def data_save(data: List[dict[str, float]]):
    load_dotenv()
    user = getenv("USER")
    password = getenv("PASSWORD")
    host = getenv("HOST")
    db = AirQualityDatabase(user, password, host=host)
    for item in data:
        db.add_air_quality_data(item['key'], item['date'], item['value'], item['sensor_id'])