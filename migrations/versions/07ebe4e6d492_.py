"""empty message

Revision ID: 07ebe4e6d492
Revises: 641277fbea21
Create Date: 2020-05-28 20:13:33.107016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07ebe4e6d492'
down_revision = '641277fbea21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_review')
    op.create_unique_constraint(None, 'product', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='unique')
    op.create_table('product_review',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='product_review_pkey')
    )
    # ### end Alembic commands ###