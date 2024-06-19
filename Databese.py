from psycopg2 import connect

class AirQualityDatabase:
    def __init__(self, user, password, host, port="5432", db_name="air_quality"):
        self.db_name = db_name
        self.conn = connect(database=db_name, user=user, password=password, host=host, port=port)
        self.cursor = self.conn.cursor()

    def add_station(self, data):
        self.cursor.execute(
            """
            INSERT INTO station (id, stationName, gegrLat, gegrLon, cityName, communeName, districtName, provinceName, addressStreet)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                data["id"],
                data["stationName"],
                data["gegrLat"],
                data["gegrLon"],
                data["city"]["name"],
                data["city"]["commune"]["communeName"],
                data["city"]["commune"]["districtName"],
                data["city"]["commune"]["provinceName"],
                data.get("addressStreet"),
            ),
        )
        self.conn.commit()

    def add_archival_data(self, name, stationCode, date, value):
        self.cursor.execute(
            """
            SELECT * FROM Archived_data 
            WHERE stationName = %s AND date = %s AND value = %s
            """,
            (name, date, value),
        )
        existing_data = self.cursor.fetchone()
        if not existing_data:
            self.cursor.execute(
                """
                INSERT INTO Archived_data (stationName, stationCode, date, value)
                VALUES (%s, %s, %s, %s)
                """,
                (name, stationCode, date, value),
            )
            self.conn.commit()

    def add_sensor(self, data):
        self.cursor.execute(
            """
            INSERT INTO Sensors (id, stationId, paramName, paramFormula, paramCode, idParam)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                data["id"],
                data["stationId"],
                data["param"]["paramName"],
                data["param"]["paramFormula"],
                data["param"]["paramCode"],
                data["param"]["idParam"],
            ),
        )
        self.conn.commit()

    def get_data(self, name_table):
        self.cursor.execute(f"SELECT * FROM {name_table}")
        return self.cursor.fetchall()

    def get_id(self, name_table):
        self.cursor.execute(f"SELECT Id FROM {name_table}")
        return self.cursor.fetchall()

    def add_air_quality_data(self, id, key, date, value, sensor_id):
        # Sprawdzenie czy dane już istnieją
        self.cursor.execute(
            """
            SELECT 1 FROM air_quality
            WHERE pollutant = %s AND measurement_date = %s AND sensor_id = %s
            """,
            (key, date, sensor_id),
        )

        existing_data = self.cursor.fetchone()

        if existing_data:
            # Dane już istnieją, wykonaj UPDATE
            self.cursor.execute(
                """
                UPDATE air_quality
                SET value = %s
                WHERE pollutant = %s AND measurement_date = %s AND sensor_id = %s
                """,
                (value, key, date, sensor_id),
            )
        else:
            # Dane nie istnieją, wykonaj INSERT
            self.cursor.execute(
                """
                INSERT INTO air_quality (id, pollutant, measurement_date, value, sensor_id)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (id, key, date, value, sensor_id),
            )

        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()



