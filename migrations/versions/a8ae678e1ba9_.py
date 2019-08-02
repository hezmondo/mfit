"""empty message

Revision ID: a8ae678e1ba9
Revises: e53415594d4a
Create Date: 2019-01-13 21:20:56.097106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8ae678e1ba9'
down_revision = 'e53415594d4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_fit',
    sa.Column('fitness_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fitness_id'], ['fitness.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_fit')
    # ### end Alembic commands ###
