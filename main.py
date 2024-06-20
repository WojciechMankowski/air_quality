import os, time
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
from database.Databese import AirQualityDatabase
from air_quality_data import get_data
from concurrent.futures import ThreadPoolExecutor


def initialize_database():
    """Stwórz instancję obiektu bazy danych"""
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    return AirQualityDatabase(user, password, host=host)


def add_air_quality_data(db, key, item, sensor_id):
    """Zapisz dane do bazy danych"""
    db.add_air_quality_data(key, item["date"], item["value"], sensor_id)


def process_values(db, key, values, sensor_id):
    """Sprawdź datę pomiaru i zapisz do bazy danych, jeśli jest dzisiaj"""
    if isinstance(values, list):
        today_str = datetime.today().strftime("%Y-%m-%d")
        for item in values:
            if item['date'][:10] == today_str:
                add_air_quality_data(db, key, item, sensor_id)
                sleep(1)  # zmniejszony czas sleep dla demonstracji


def process_sensor_data(db, ids):
    """Przetwarzaj dane dla pojedynczego sensora"""
    data = get_data(ids[0])
    key = data["key"]
    values = data["values"]
    process_values(db, key, values, ids[0])


def main():
    db = initialize_database()
    sensor_ids = db.get_data("Sensors")
    num_operations = len(sensor_ids)

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(process_sensor_data, db, ids) for ids in sensor_ids]
        for future in futures:
            future.result()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Liczba operacji: {num_operations}")
    print(f"Czas trwania każdej operacji (średnio): {total_time / num_operations:.2f} sekundy")


if __name__ == "__main__":
    main()
