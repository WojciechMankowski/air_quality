import os
from time import sleep
from air_quality_data import get_data
from Databese import AirQualityDatabase
from dotenv import load_dotenv

def main():
    load_dotenv()
    user = os.getenv("USER")
    password =os.getenv('PASSWORD')
    host = os.getenv("HOST")
    db = AirQualityDatabase(user, password, host=host)
    for ids in db.get_data("Sensors"):
        data = get_data(ids[0])
        key = data["key"]
        values = data["values"]

        if isinstance(values, list):
            for item in values:
                data_data = db.get_data('air_quality')
                # print(data_data)
                db.add_air_quality_data(len(data_data)+1, key, item["date"], item["value"], ids[0])
                sleep(15)

if __name__ == '__main__':
    main()