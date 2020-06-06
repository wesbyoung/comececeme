"""empty message

Revision ID: f85e43690237
Revises: 6119c880d431
Create Date: 2020-06-06 17:25:59.199772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f85e43690237'
down_revision = '6119c880d431'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('_zip', sa.Integer(), nullable=True))
    op.drop_column('customer', 'zip')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('zip', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('customer', '_zip')
    # ### end Alembic commands ###