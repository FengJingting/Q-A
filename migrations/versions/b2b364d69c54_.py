"""empty message

Revision ID: b2b364d69c54
Revises: c4cd8d2a604a
Create Date: 2022-12-04 15:56:36.818586

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b2b364d69c54'
down_revision = 'c4cd8d2a604a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'iscollect')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('iscollect', mysql.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
