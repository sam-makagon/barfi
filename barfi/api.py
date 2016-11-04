import flask.ext.restless

from barfi import app, models, logmsg, EVENT_START, EVENT_STOP
from barfi.database import session, printquery
from barfi.paginate import get_total_pages, get_offset
from barfi.config import ITEMS_PER_PAGE, DEBUG
from barfi import app, models
from barfi.database import session


# update service based on new event
def insert_sensor_reading(data=None, **kw):
  #if DEBUG:
  logmsg("data=%s, kw=%s" % (data, kw)) 

  record = {'station_name': kw['result']['station_name']}
  record['weight_grams'] = kw['result']['weight_grams']
  
  try:
    session.query(models.Sensors).insert(record)
    session.commit()
  except Exception as e:
    logmsg("exception caught inserting sensor record %s" % e)

manager = flask.ext.restless.APIManager(app, session=session)

#service_blueprint = manager.create_api(models.Sensors, methods=['GET', 'POST'])
service_blueprint = manager.create_api(models.Sensors, 
    methods=['GET', 'POST']
)

    # postprocessors={
    #   'POST' : [insert_sensor_reading],
    #   'GET' : [insert_sensor_reading],
    # }