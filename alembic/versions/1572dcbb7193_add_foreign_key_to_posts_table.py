"""add foreign-key to posts table

Revision ID: 1572dcbb7193
Revises: 9f08a885e0ad
Create Date: 2023-01-08 15:59:27.043884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1572dcbb7193"
down_revision = "9f08a885e0ad"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts", type_="foreignkey")
    op.drop_column("posts", "owner_id")
    pass
