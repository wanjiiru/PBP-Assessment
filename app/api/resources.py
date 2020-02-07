from flask_restplus import Resource, Namespace
from ..extensions import DB, auth
import json
import traceback
from ..extensions import DB, auth
import re

ns = Namespace('Sales', description='sales endpoints')
