from flask import render_template, request

from barfi import app, models, logmsg
from barfi.database import session, printquery
from barfi.paginate import get_total_pages, get_offset
from barfi.config import ITEMS_PER_PAGE, DEBUG

@app.route('/')
@app.route('/barfi/')
def show_services():
  # cur_page = get_page(request)
  # offset = get_offset(cur_page)

  # #base services query
  # services = session.query(models.Service).\
  #             join(models.Status).\
  #             with_entities(models.Service.id, models.Service.name, models.Service.host, models.Service.status,\
  #               models.Service.modify_date, models.Service.start_date, models.Service.user,\
  #               models.Service.stop_date, models.Service.message, models.Service.arguments, models.Status.status_description )
  
  # #apply search
  # if request.args.get('search'):
  #   search_term = '%%%s%%' % request.args.get('search')
  #   services = services.filter( (models.Service.message.like(search_term)) | (models.Service.name.like(search_term)) )

  # #apply sort
  # if request.args.get('sort_by'):
  #   if request.args.get('sort_order') == 'desc':
  #     services = services.order_by(getattr(models.Service, request.args.get('sort_by')).desc())
  #   else:
  #     services = services.order_by(getattr(models.Service, request.args.get('sort_by')).asc())
  # else:
  #   #default sort
  #   services = services.order_by(models.Service.modify_date.desc())


  # #apply offset and limit
  # services = services.offset(offset).limit(ITEMS_PER_PAGE)

  # rowcount = session.query(models.Service.id).count()
  # total_pages = get_total_pages(rowcount)

  # if DEBUG:
  #   logmsg("offset=%s, limit=%s, total_pages=%s, rowcount=%s, ITEMS_PER_PAGE=%s" % (offset, ITEMS_PER_PAGE, total_pages, rowcount, ITEMS_PER_PAGE))
  #   logmsg(printquery(services))

  return render_template('services.html')



