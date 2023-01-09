"""add content column to posts table

Revision ID: ada84a28dc44
Revises: 40fb4a026fda
Create Date: 2023-01-08 15:35:50.372187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ada84a28dc44"
down_revision = "40fb4a026fda"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(255), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
