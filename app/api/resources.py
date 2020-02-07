from flask_restplus import Resource, Namespace
from ..extensions import DB, auth
import json
import traceback
from ..extensions import DB, auth
import re
from werkzeug.datastructures import FileStorage


ns = Namespace('Sales', description='sales endpoints')

parser=ns.parser()
parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

@ns.route('sales/file')
class Upload(Resource):
    @ns.expect(parser, validate=True)
    def post(self):
        args = parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        print(uploaded_file)
        return {'status': 'success'}, 201



