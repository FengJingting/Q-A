"""empty message

Revision ID: a3800f778e1a
Revises: b2b364d69c54
Create Date: 2022-12-04 16:25:38.204204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a3800f778e1a'
down_revision = 'b2b364d69c54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_favorite_question', 'question_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('user_favorite_question', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_favorite_question', sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.alter_column('user_favorite_question', 'question_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
