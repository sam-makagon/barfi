create schema coffee if not exists;

ALTER ROLE barfi SET search_path TO coffee;

drop table coffee.sensors;
drop table coffee.status;

create table coffee.sensors (
    sensor_id serial PRIMARY KEY
    , station_name text not null
    , sensor_data text null
    , event_date timestamp null default CURRENT_TIMESTAMP
);

create table coffee.status (
    status_id serial PRIMARY KEY
    , station_name text not null
    , station_status int not null
    , brew_time timestamp null
);

GRANT ALL PRIVILEGES ON SCHEMA coffee TO barfi;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA coffee TO  barfi;


GRANT USAGE, SELECT ON SEQUENCE coffee.sensors_sensor_id_seq TO barfi;
GRANT USAGE, SELECT ON SEQUENCE coffee.sensors_sensor_id_seq TO barfi;

GRANT USAGE, SELECT ON SEQUENCE coffee.status_status_id_seq TO barfi;
GRANT USAGE, SELECT ON SEQUENCE coffee.status_status_id_seq TO barfi;



/* 
drop table coffee.stations;
drop table coffee.carafes;
drop table coffee.sensors;


create table coffee.stations (
    station_id serial PRIMARY KEY
    , station_name text not null
);

create table coffee.carafes (
    carafe_id serial PRIMARY KEY
    , station_id integer not null references coffee.stations(station_id)
    , carafe_number int not null default 0
    , carafe_status int null
);

create index carafes_idx1 on coffee.carafes(station_id, carafe_number);

create table coffee.sensors (
    event_id serial PRIMARY KEY
    , station_id integer not null references coffee.stations(station_id)
    , weight_grams int not null
    , weight_date timestamp not null
);

create index sensors_idx1 on coffee.sensors(station_id);

*/


