"""empty message

Revision ID: a016653cffb1
Revises: 6e19aec6e88d
Create Date: 2022-12-04 14:54:31.790543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a016653cffb1'
down_revision = '6e19aec6e88d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_favorite_question', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user_favorite_question', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_favorite_question', type_='foreignkey')
    op.drop_column('user_favorite_question', 'user_id')
    # ### end Alembic commands ###
