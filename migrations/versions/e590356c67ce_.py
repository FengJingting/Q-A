"""empty message

Revision ID: e590356c67ce
Revises: d9f405321ba6
Create Date: 2022-11-26 14:09:34.920988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e590356c67ce'
down_revision = 'd9f405321ba6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_favorite_question',
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('favorite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorite.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favorite_question')
    op.drop_table('favorite')
    # ### end Alembic commands ###