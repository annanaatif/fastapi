"""add phone number to users table

Revision ID: 3901bb7e087d
Revises: 47bef2729c24
Create Date: 2025-08-11 00:34:51.279138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3901bb7e087d'
down_revision = '47bef2729c24'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_column('users', 'phone_number')
    pass
