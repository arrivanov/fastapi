"""create post table

Revision ID: 40fb4a026fda
Revises: 
Create Date: 2023-01-08 15:23:32.288538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "40fb4a026fda"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(100), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
