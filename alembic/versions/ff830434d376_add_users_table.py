"""add users table

Revision ID: ff830434d376
Revises: 56e7f2b68dbe
Create Date: 2025-08-11 00:05:30.979853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff830434d376'
down_revision = '56e7f2b68dbe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
