"""empty message

Revision ID: 11c8ba986e68
Revises: 32953d1b8596
Create Date: 2022-12-05 08:10:19.446209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11c8ba986e68'
down_revision = '32953d1b8596'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_favorite_question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('favorite_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorite_id'], ['favorite.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favorite_question')
    # ### end Alembic commands ###
