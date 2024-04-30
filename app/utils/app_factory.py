import logging
import sys
from flask import Flask
from app.routes.routes_html import routes_html
from app.routes.routes_api import routes_api
from app.routes.routes_swagger import SWAGGER_URL, routes_swagger, routes_swagger_ui
from app.utils.db import db


def create_app(config):
    logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
                    level=config.LOG_LEVEL)

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config)
    
    app.register_blueprint(routes_api, url_prefix='/api')
    app.register_blueprint(routes_html, url_prefix='/')
    app.register_blueprint(routes_swagger, url_prefix='/')
    app.register_blueprint(routes_swagger_ui, url_prefix=SWAGGER_URL)

    # Print the registered routes
    logging.info("Registered routes:")
    for rule in app.url_map.iter_rules():
        logging.info(f"{rule.endpoint}: {', '.join([str(r) for r in rule.methods])} {rule}")

    # Initialize the database
    db.init_app(app)

    logging.info("App created successfully")

    return app

