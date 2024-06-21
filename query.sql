CREATE TABLE air_quality (
    id SERIAL PRIMARY KEY not null ,
    pollutant VARCHAR(250) not null ,
    measurement_date timestamp not null ,
    value decimal,
    sensors_id integer not null REFERENCES sensors(id)
)


SELECT
    Station.id,
    Station.stationName,
    Station.gegrLat,
    Station.gegrLon,
    Station.cityName,
    Sensors.id as sensor_id,
    Sensors.paramName,
    Sensors.paramFormula,
    air_quality.id as air_quality_id,
    air_quality.pollutant,
    air_quality.measurement_date,
    air_quality.value
FROM
    air_quality
LEFT JOIN
    Sensors ON air_quality.sensors_id = Sensors.id
LEFT JOIN
    Station ON Sensors.stationId = Station.id;