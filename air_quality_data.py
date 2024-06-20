from datetime import datetime
import requests

# URL API
BASE_URL = "https://api.gios.gov.pl/pjp-api/rest/"


def get_stations():
    """Pobiera listę stacji pomiarowych."""
    url = BASE_URL + "station/findAll"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_sensors(station_id):
    """Pobiera listę stanowisk pomiarowych dla danej stacji."""
    url = BASE_URL + f"station/sensors/{station_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_data(sensor_id):
    """Pobiera dane archiwalne dla danego stanowiska pomiarowego."""
    size = datetime.now().hour
    url = BASE_URL + f"data/getData/{sensor_id}?size={size + 2}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_archival_data(sensor_id):
    """Pobiera dane historyczne dla danego stanowiska pomiarowego."""
    days = (datetime.now() - datetime(2024, 6, 1)).days
    url = BASE_URL + f"archivalData/getDataBySensor/{sensor_id}?size=500&dayNumber={1}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()["Lista archiwalnych wyników pomiarów"]


