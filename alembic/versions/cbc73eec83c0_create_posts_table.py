"""create posts table

Revision ID: cbc73eec83c0
Revises: 
Create Date: 2025-08-10 20:18:24.061398

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cbc73eec83c0'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('title', sa.String(length=100), nullable=False)
    )
    pass

def downgrade():
    op.drop_table('posts')
    pass