from salesapp.models import DB
from marshmallow import Schema, fields

from salesapp.models.base import BaseModel


class Invoice(BaseModel):
    __tablename__ = 'sales_invoice'
    contact_name = DB.Column(DB.String(400),nullable=False)
    invoice_number = DB.Column(DB.Integer,nullable=False)
    invoice_date = DB.Column(DB.DateTime,nullable=False)
    due_date = DB.Column(DB.DateTime,nullable=False)
    description = DB.Column(DB.String(1000),nullable=False)
    quantity = DB.Column(DB.Integer,nullable=False)
    unit_amount = DB.Column(DB.Integer,nullable=False)
    total_amount=DB.Column(DB.Integer)


class InvoiceSchema(Schema):
    contact_name = fields.Str()
    invoice_number = fields.Integer()
    invoice_date = fields.DateTime()
    due_date = fields.DateTime()
    description = fields.Str()
    quantity = fields.Integer()
    unit_amount = fields.Integer()


invoice_schema = InvoiceSchema()
invoices_schema = InvoiceSchema(many=True)
