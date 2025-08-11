"""add foreign key to posts

Revision ID: 9b52b3e2d676
Revises: ff830434d376
Create Date: 2025-08-11 00:11:46.469918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b52b3e2d676'
down_revision = 'ff830434d376'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_posts_users', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass

def downgrade():
    op.drop_constraint('fk_posts_users', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass