"""add content column to posts table

Revision ID: 56e7f2b68dbe
Revises: cbc73eec83c0
Create Date: 2025-08-10 23:59:45.610034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56e7f2b68dbe'
down_revision = 'cbc73eec83c0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
