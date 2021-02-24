from flask.helpers import url_for
#from app_constants import AppConstants
#from endpoints import api
from flask import g
import time
from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint

env_config = {
    "development": "env_constants.EnvConstantsDevelopment",
    "testing":     "env_constants.EnvConstantsTesting",
    "production":  "env_constants.EnvConstants",
    "default":     "env_constants.EnvConstants",
}

def init_logger(app):
    from logging import StreamHandler
    from utils.log_formatter import LogFormatter
    import sys

    from flask.logging import default_handler
    app.logger.removeHandler(default_handler)

    handler = StreamHandler(sys.stderr)
    handler.setFormatter(LogFormatter(
        '[%(asctime)s] [%(remoteaddr)s] %(levelname)s in %(module)s:%(url)s : %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config.get('LOG_LEVEL'))

def init_swagger_ui(app):
    swaggerui_blueprint = get_swaggerui_blueprint(
       #Specify your own SWAGGER_URL and API_URL
        #AppConstants.SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        #AppConstants.API_URL,
    )
    app.register_blueprint(swaggerui_blueprint)



def initialize_app():
    from werkzeug.middleware.proxy_fix import ProxyFix
    from flask import Flask
    from os import environ as env
    app_env = env.get('FLASK_ENV', 'default')
    app = Flask(__name__)
    CORS(app)
    app.url_map.strict_slashes = False

    app.config.from_object(env_config.get(app_env))
    app.config["PROPAGATE_EXCEPTIONS"] = False

    init_logger(app)
    #implement your own API and initialize it here
    #api.init_app(app)
    if app.config.get("SWAGGER_UI"): init_swagger_ui(app)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    #for rule in app.url_map.iter_rules(): app.logger.debug(rule)
    return app


app = initialize_app()

@app.before_request
def before_request():
    g.req_start = time.time()

@app.after_request
def after_request(response):
    diff = time.time() - g.req_start
    response.headers.set("Execution-Time", diff)
    return response
