"""empty message

Revision ID: 6d85567e6a5e
Revises: 8b1a156f0f67
Create Date: 2020-11-15 16:13:14.992221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d85567e6a5e'
down_revision = '8b1a156f0f67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'hint',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=2000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'hint',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
    # ### end Alembic commands ###
