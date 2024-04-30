from flask import Blueprint, render_template, url_for
from app.routes.routes_api import routes_api
from app.routes.routes_api import get_aggregate_notifications

routes_html = Blueprint('routes_html', __name__)

# route that serves the HTML page for notifications
@routes_html.route('/notifications.html')
def notifications():
    
    api_url = routes_api.name + '.' + get_aggregate_notifications.__name__

    return render_template('notifications.html', api_url=url_for(api_url))
