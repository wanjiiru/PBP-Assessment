from .resources import ns
from flask_restplus import Api, apidoc, Resource

from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(blueprint, doc='/docs', ui=False)

api.add_namespace(ns, path='/Sales')

from .resources import Invoice

__all__ = [
    'Invoice'
]
