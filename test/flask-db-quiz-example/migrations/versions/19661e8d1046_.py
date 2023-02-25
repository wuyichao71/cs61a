"""empty message

Revision ID: 19661e8d1046
Revises: 
Create Date: 2023-02-22 19:25:29.950028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19661e8d1046'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player_scores',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('player', sa.String(length=255), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_scores')
    # ### end Alembic commands ###
