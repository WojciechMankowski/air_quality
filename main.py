from time import sleep

from dotenv import load_dotenv
from database.get_id_of_city import get_data_id_sensor
from database.sensor_id_for_cities import *
from database.Databese import AirQualityDatabase
from air_quality_data import get_data
from datetime import datetime
from os import getenv


def create_id(db):
    ids = db.get_id("air_quality")
    if len(ids) != 0:
        return db.get_id("air_quality")[-1][0] + 1
    else:
        return 1


def main():
    # pobranie id dla sensorów
    # iniclazcja bazy danych
    load_dotenv()
    user = getenv("USER")
    password = getenv("PASSWORD")
    host = getenv("HOST")
    db = AirQualityDatabase(user, password, host=host)
    # zapisanie id dla największych miast
    query = 'SELECT cityname, id FROM station'
    _data = db.query(query)
    data = []
    for city in _data:
        query2 = f'SELECT id FROM sensors WHERE stationid = {city[1]}'
        data_sensors = db.query(query2)
        data.append({city[0]: data_sensors[0][0]})
    cities = [
        get_bydgoszcz_sensors(data),
        get_gdansk_sensors(data),
        get_krakow_sensors(data),
        get_lodz_sensors(data),
        get_wroclaw_sensors(data),
        get_poznan_sensors(data),
        get_szczecin_sensors(data),
        get_lublin_sensors(data),
        get_katowice_sensors(data),
        get_warsaw_sensors(data)
    ]
    # pobieranie danych z API
    for city_id in cities:
        for id in city_id:
            hour = datetime.now().hour
            data = get_data(id)
            identifiers = db.get_id("air_quality")
            ids = identifiers[-1][0] + 1
            print(ids in identifiers)
            key = data['key']
            values = data['values'][:hour + 1]
            for item in values:
                print(item)
                db.add_air_quality_data(key, item['date'], item['value'], id)


if __name__ == '__main__':
    while True:
        main()
