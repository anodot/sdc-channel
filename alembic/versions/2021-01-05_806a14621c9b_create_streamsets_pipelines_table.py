"""create streamsets_pipelines table

Revision ID: 806a14621c9b
Revises: 
Create Date: 2021-01-05 16:56:23.741507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '806a14621c9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'streamsets_pipelines',
        sa.Column('pipeline_id', sa.String, nullable=False, primary_key=True),
        sa.Column('streamsets_id', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('streamsets_pipelines')
