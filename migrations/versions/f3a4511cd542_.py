"""empty message

Revision ID: f3a4511cd542
Revises: 515ce5d41d66
Create Date: 2020-02-07 22:32:41.905519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3a4511cd542'
down_revision = '515ce5d41d66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sales_invoice', 'description',
               existing_type=sa.VARCHAR(length=400),
               type_=sa.String(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sales_invoice', 'description',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=400),
               existing_nullable=True)
    # ### end Alembic commands ###
