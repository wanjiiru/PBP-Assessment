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
        for x in data:
            import datetime
            name = x['*ContactName']
            invoice_number = x['*InvoiceNumber']
            invoice_date = x['*InvoiceDate']
            invoice_date_time_obj = datetime.datetime.strptime(invoice_date.strip('\t\r\n'), '%d/%m/%Y')
            due_date = x['*DueDate']
            due_date_time_obj = datetime.datetime.strptime(due_date.strip('\t\r\n'), '%d/%m/%Y')
            description = x['*Description']
            quantity = int(x['*Quantity'])
            unit_amount = int((x['*UnitAmount']))

            invoice_data = Invoice(**{
                "contact_name": name,
                "invoice_number": invoice_number,
                "invoice_date": invoice_date_time_obj,
                "due_date": due_date_time_obj,
                "description": description,
                "quantity": quantity,
                "unit_amount": unit_amount,

            })
            DB.session.add(invoice_data)
            DB.session.commit()

            return {
                       'status': 'success'
                   }, 201


@ns.route('summary/topfivecustomers')
class Summary(Resource):
    def get(self):
        top_five_customers = []

        top_five = Invoice.query.order_by(Invoice.quantity.desc()).limit(5).all()
        for i in top_five:
            top_five_customers.append({
                'name': i.contact_name,
                'Quantity': i.quantity
            })
        return {
            'status': 'success',
            'Top Five Customers': top_five_customers
        }
