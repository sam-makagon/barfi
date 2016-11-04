import flask.ext.restless

from barfi import app, models, logmsg, EVENT_START, EVENT_STOP
from barfi.database import session, printquery, toggle_status
from barfi.paginate import get_total_pages, get_offset
from barfi.config import ITEMS_PER_PAGE, DEBUG
from barfi import app, models

# update service based on new event
def insert_sensor_reading(data=None, **kw):
  #if DEBUG:
  logmsg("data=%s, kw=%s" % (data, kw)) 

  record = {'station_name': 'bunn'}
  record['station_status'] = 1 #kw['result']['sensor_data']
  
  toggle_status()

  # try:
  #   #session.query(models.Service).filter(models.Service.id == kw['result']['parent_id']).update(update)
  #   session.query(models.Status).update(record)
  #   session.commit()
  # except Exception as e:
  #   logmsg("exception caught inserting sensor record %s" % e)

manager = flask.ext.restless.APIManager(app, session=session)

service_blueprint = manager.create_api(models.Status, methods=['GET', 'POST'])
service_blueprint = manager.create_api(models.Sensors, 
    methods=['GET', 'POST'],
    preprocessors={
      'POST' : [insert_sensor_reading],
    }
)

