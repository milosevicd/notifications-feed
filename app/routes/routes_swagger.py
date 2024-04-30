from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint, jsonify, current_app as app

# Configure Swagger
SWAGGER_URL = '/swagger'
API_SPEC_URL = '/api_spec'

routes_swagger = Blueprint('routes_swagger', __name__)

@routes_swagger.route(API_SPEC_URL, methods=['GET'])
def api_spec(): 
    swag = swagger(app, prefix='/api')
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Notifications API"
    return jsonify(swag)

routes_swagger_ui = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_SPEC_URL,
    config = {
        'app_name': "Notifications API"
    }
)