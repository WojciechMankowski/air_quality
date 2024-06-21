import os
from typing import List
from database.Databese import AirQualityDatabase
from dotenv import load_dotenv


def get_data_id_sensor() -> List[dict[str, int]]:
    '''Downloading information about the id sensor for each city'''
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")

    db = AirQualityDatabase(user, password, host)
    query = 'SELECT cityname, id FROM station'
    data = db.query(query)
    data_id_sensors = []
    for city in data:
        query2 = f'SELECT id FROM sensors WHERE stationid = {city[1]}'
        data_sensors = db.query(query2)
        data_id_sensors.append({city[0]: data_sensors[0][0]})
    return data_id_sensors
def get_data_id_sensor_for_city(city_name) -> List[dict[str, int]]:
    '''Downloading information about the id sensor for each city'''
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")

    db = AirQualityDatabase(user, password, host)
    query = f"SELECT cityname, id FROM station WHERE cityname = '{city_name}'"
    data = db.query(query)
    data_id_sensors = []
    for city in data:
        query2 = f'SELECT id FROM sensors WHERE stationid = {city[1]}'
        data_sensors = db.query(query2)
        data_id_sensors.append({city[0]: data_sensors[0][0]})
    return data_id_sensors
def get_id_sensor_of_city(data: List[dict[str, int]], city: str) -> List[int]:
    data_id = []
    for item in data:
        for key, value in item.items():
            if key == city:
                data_id.append(value)
    return data_id


if __name__ == '__main__':
    data = get_data_id_sensor_for_city("Gdańsk")





