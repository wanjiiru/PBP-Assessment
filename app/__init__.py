from flask import Flask

from app.extensions import DB, API, migrate
from werkzeug.middleware.proxy_fix import ProxyFix

import app.models

from app.config import config


def create_app(environment='development'):

    app = Flask(__name__)
    setup_config(app)
    setup_extensions(app)
    setup_api()

    @app.before_request
    def log_requests():
        from flask import request
        print(f"url: {request.endpoint}, host: {request.host}, request_args: {request.args.to_dict()}")

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,X-Requested-With,accept')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')

        return response

    app.wsgi_app = ProxyFix(app.wsgi_app)
    return app



def setup_extensions(app):
    DB.init_app(app)
    API.init_app(app)
    migrate.init_app(app, db=DB)


def setup_config(app: Flask, testing=False):
    if testing:
        app.config.from_object(config.TestingConfig)
        app.config.from_object(config.ProductionConfig)

#
def setup_api():
    pass
#     from messaging.api.resource import ns
#
#     API.add_namespace(ns, '/')
