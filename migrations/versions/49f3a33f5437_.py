"""empty message

Revision ID: 49f3a33f5437
Revises: a3cf002f4da8
Create Date: 2018-06-08 01:37:24.165316

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '49f3a33f5437'
down_revision = 'a3cf002f4da8'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('send_email', sa.Boolean(), nullable=True))
    op.add_column('sessions_version', sa.Column('send_email', sa.Boolean(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sessions_version', 'send_email')
    op.drop_column('sessions', 'send_email')
    # ### end Alembic commands ###