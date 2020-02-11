import csv
from io import StringIO
from flask_restplus import Resource, Namespace
from sqlalchemy import and_

from ..extensions import DB
from werkzeug.datastructures import FileStorage

from ..models import Invoice
from salesapp.extensions import csrf

ns = Namespace('Sales', description='sales endpoints')

parser = ns.parser()
parser.add_argument('file', location='files',
                    type=FileStorage, required=True)


@csrf.exempt
@ns.route('upload')
class Upload(Resource):
    @ns.expect(parser, validate=True, csrf=False)
    def post(self):
        args = parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        if not uploaded_file:
            return "No file provided"
        data = []
        stream = StringIO(uploaded_file.stream.read().decode('utf-8'))
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
            # save to invoice model
            invoice_data = Invoice(**{
                "contact_name": name,
                "invoice_number": invoice_number,
                "invoice_date": invoice_date_time_obj,
                "due_date": due_date_time_obj,
                "description": description,
                "quantity": quantity,
                "unit_amount": unit_amount,
                'total_amount': unit_amount * quantity

            })
            DB.session.add(invoice_data)
            DB.session.commit()

        return {
                   'status': 'success'
               }, 201


@ns.route('summary/topfivecustomers')
class Summary(Resource):
    # Returning the Top Five customers, according to Quantity bought.
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


@ns.route('summary/topfiveperyear')
class SummaryPerYear(Resource):
    def get(self):

        # Returning the Top Five customers according Total amount (quantity *unitAmount) due for a given year
        results_2019 = []
        results_2020 = []
        # get first five in 2019
        twenny_19 = Invoice.query.filter(Invoice.due_date <= '2019-12-31 00:00:00').order_by(
            Invoice.total_amount.desc()).limit(5)
        # get first in 2020
        twenny_20 = Invoice.query.filter(Invoice.due_date <= '2020-12-31 00:00:00').order_by(
            Invoice.total_amount.desc()).limit(5)

        for i in twenny_20:
            results_2020.append({
                'name': i.contact_name,
                'Quantity': i.total_amount

            })

        for x in twenny_19:
            results_2019.append({
                'name': x.contact_name,
                'Quantity': x.total_amount
            })

        return {
            'status': 'success',
            'Top five customers in 2019': results_2019,
            'Top five Customers in 2020': results_2020
        }


trx_parser = ns.parser()
trx_parser.add_argument('date', required=False)


@ns.route('summary/transactions/<string:date>')
class Transactions(Resource):
    def get(datee):
        pass
