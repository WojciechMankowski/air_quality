from time import sleep
from database.get_id_of_city import get_data_id_sensor_for_city
from air_quality_data import get_data
from data_filtering import data_filtering
from data_save_to_database import data_save


def main():
    city = "Warszawa"
    data_to_save = []
    data_id_sensors = [id_city[city] for id_city in get_data_id_sensor_for_city(city)]
    for id in data_id_sensors:
        data = get_data(id)
        key = data['key']
        values = data['values']
        for item in values:
            filters = data_filtering(item)
            if isinstance(filters, dict):
                data_to_save.append({"sensor_id": id, "key": key, **data_filtering(item)})
    data_save(data_to_save)


if __name__ == '__main__':
    while True:
        main()
        sleep(300)
