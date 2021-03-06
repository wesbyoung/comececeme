"""added is_admin column to Account model

Revision ID: a935515e3c1c
Revises: 979a876ec756
Create Date: 2020-09-23 02:29:25.037141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a935515e3c1c'
down_revision = '979a876ec756'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'is_admin')
    # ### end Alembic commands ###
