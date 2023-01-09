"""add last few columns to posts table

Revision ID: 971e9e050f4f
Revises: 1572dcbb7193
Create Date: 2023-01-08 16:04:56.005116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "971e9e050f4f"
down_revision = "1572dcbb7193"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="1"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
