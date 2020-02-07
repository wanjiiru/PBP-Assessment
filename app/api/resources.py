import csv
import io
from io import StringIO

from flask import request
from flask_restplus import Resource, Namespace
from ..extensions import DB, auth
import json
import traceback
from ..extensions import DB, auth
import re
from werkzeug.datastructures import FileStorage

from ..models import Invoice

ns = Namespace('Sales', description='sales endpoints')

parser = ns.parser()
parser.add_argument('file', location='files',
                    type=FileStorage, required=True)


@ns.route('upload')
class Upload(Resource):
    @ns.expect(parser, validate=True)
    def post(self):
        args = parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        if not uploaded_file:
            return "No file"
        data = []
        stream = StringIO(uploaded_file.stream.read().decode('utf-8'), newline=None)
        reader = csv.reader(stream)
        i = 0
        headers = None
        for row in reader:
            if i == 0:
                i += 1
                headers = row
                continue
            data.append({key: value for key, value in zip(headers, row)})
        print(type(data))
        for x in data:
            name = x['*ContactName']
            invoice_number = x['*InvoiceNumber']
            invoice_date = x['*InvoiceDate']
            due_date = x['*DueDate']
            description = x['*Description']
            quantity = int(x['*Quantity'])
            unit_amount = int((x['unit_amount']))
            print(name)

            invoice_data = Invoice(**{
                "contact_name": name,
                "invoice_number": invoice_number,
                "invoice_date": invoice_date,
                "due_date": due_date,
                "description": description,
                "quantity": quantity,
                "unit_amount": unit_amount,

            })
            DB.session.add(invoice_data)
            DB.session.commit()
