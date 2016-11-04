from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, text

Base = declarative_base()

class Sensors(Base):
    __tablename__ = 'sensors'

    sensor_id = Column(Integer, primary_key=True)
    station_name = Column(String(30), nullable=False)
    sensor_data = Column(String(1000), nullable=False)
    event_date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    def __init__(self, station_name, sensor_data, event_date=None):
        self.station_name = station_name
        self.sensor_data = sensor_data
        self.event_date = event_date

    def __repr__(self):
        return '<station_name %r>' % (self.station_name)

class Status(Base):
    __tablename__ = 'status'

    status_id = Column(Integer, primary_key=True)
    station_name = Column(String(30), nullable=False)
    station_status = Column(Integer, nullable=False)
    brew_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    def __init__(self, station_name, station_status, brew_time=None):
        self.station_name = station_name
        self.station_status = station_status
        self.brew_time = brew_time

    def __repr__(self):
        return '<station_name %r, station_status %r, brew_time %r>' % (self.station_name, self.station_status, self.brew_time)


