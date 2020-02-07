from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth

DB = SQLAlchemy()
API = Api(title=' App')
migrate = Migrate()
auth = HTTPBasicAuth()
