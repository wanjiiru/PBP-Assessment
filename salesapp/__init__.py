from flask import Flask
from flask_wtf import CsrfProtect

from salesapp.api import resources

from salesapp.extensions import DB, API, migrate
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_simplemde import SimpleMDE
from flask_bootstrap import Bootstrap

from salesapp import config

def create_app():
    app = Flask(__name__, template_folder='templates')
    setup_config(app)
    setup_extensions(app)
    from salesapp import models
    setup_api()
    # set_forms(app)
    from .main import main as bp
    app.register_blueprint(bp)
    simple = SimpleMDE()
    bootstrap = Bootstrap()
    simple.init_app(app)
    bootstrap.init_app(app)
    app.config['SECRET_KEY'] = 'you-will-never-guess'


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


def setup_api():
    from salesapp.api import ns
    API.add_namespace(ns, '/')


def set_forms(app):
    init_app(app)
