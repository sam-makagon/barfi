create schema coffee;

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


    