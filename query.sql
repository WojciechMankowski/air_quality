CREATE TABLE air_quality (
    id SERIAL PRIMARY KEY not null ,
    pollutant VARCHAR(250) not null ,
    measurement_date timestamp not null ,
    value decimal,
    sensors_id integer not null REFERENCES sensors(id)
)