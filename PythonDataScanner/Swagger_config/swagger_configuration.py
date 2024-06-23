from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

# URL for accessing Swagger UI
SWAGGER_URL = '/swagger'
# URL where your API definition is located
API_URL = '/static/swagger.json'  # Path to your API definition

# Configuring Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'https://pydatascanner.azurewebsites.net/swagger.json'
# API_URL = 'http://127.0.0.1:8000/swagger.json'
# API_URL = 'http://127.0.0.1:5000/swagger.json'

def configure_swagger():
    swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "STAI Data Scanner" # Setting the application name displayed in Swagger UI
    }
)
    return swaggerui_blueprint


def serve_swagger_json():
    with open('Swagger_config/swagger.json', 'r') as f:
        return jsonify(json.load(f))