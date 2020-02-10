from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask import Blueprint
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from flask_wtf import CSRFProtect

DB = SQLAlchemy()
API = Api(title=' App')
migrate = Migrate()
auth = HTTPBasicAuth()
csrf = CSRFProtect()


