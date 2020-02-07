from app.models import DB
from marshmallow import Schema, fields

from app.models.base import BaseModel


class SalesInvoice(BaseModel):
    __tablename__ = 'sales_invoice'
    contact_name = DB.Column(DB.String(400))
    invoice_number = DB.Column(DB.Integer)
    due_date = DB.Column(DB.DateTime)
    description = DB.Column(DB.String(400))
    quantity = DB.Column(DB.Integer)
    unit_amount = DB.Column(DB.Integer)
