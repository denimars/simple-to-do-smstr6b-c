"""empty message

Revision ID: b51bc977fdae
Revises: e6d42d40c634
Create Date: 2018-07-05 11:24:09.549311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b51bc977fdae'
down_revision = 'e6d42d40c634'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anggota',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identitas', sa.Integer(), nullable=False),
    sa.Column('no_anggota', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=30), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('anggota')
    # ### end Alembic commands ###
