"""empty message

Revision ID: f40d5280512c
Revises: f272ca0f018d
Create Date: 2020-11-21 20:55:13.373260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f40d5280512c'
down_revision = 'f272ca0f018d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_projects', sa.Column('status', sa.Enum('pending', 'active', name='userprojectstatusenum'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_projects', 'status')
    # ### end Alembic commands ###
