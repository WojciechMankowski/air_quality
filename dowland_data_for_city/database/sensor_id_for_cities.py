from typing import List
from dowland_data_for_city.database.get_id_of_city import get_id_sensor_of_city


def get_warsaw_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Warszawa')


def get_krakow_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Kraków')


def get_lodz_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Łódź')


def get_wroclaw_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Wrocław')


def get_poznan_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Poznań')


def get_gdansk_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Gdańsk')


def get_szczecin_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Szczecin')


def get_bydgoszcz_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Bydgoszcz')


def get_lublin_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Lublin')


def get_katowice_sensors(data: List[dict[str, int]]) -> List[int]:
    return get_id_sensor_of_city(data, 'Katowice')