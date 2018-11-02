"""empty message

Revision ID: 8a6a57b41c80
Revises: 40fb79ea6606
Create Date: 2018-11-02 19:42:40.320875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a6a57b41c80'
down_revision = '40fb79ea6606'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('participants', sa.Column('address', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('participants', 'address')
    # ### end Alembic commands ###
