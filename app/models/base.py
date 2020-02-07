from sqlalchemy_utils import generic_repr
from sqlalchemy.sql import func
from app.models import DB


@generic_repr
class BaseModel(DB.Model):
    __abstract__ = True

    id = DB.Column(DB.Integer, primary_key=True)
    created_at = DB.Column(DB.DateTime(timezone=True), server_default=func.now())
    updated_at = DB.Column(DB.DateTime(timezone=True), onupdate=func.now())
