"""empty message

Revision ID: a822ec8f48b6
Revises: 688792d038ee
Create Date: 2018-07-05 11:44:13.442897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a822ec8f48b6'
down_revision = '688792d038ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=50), nullable=False),
    sa.Column('user', sa.String(length=20), nullable=False),
    sa.Column('hash_password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###