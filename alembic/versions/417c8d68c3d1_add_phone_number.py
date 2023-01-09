"""add phone number

Revision ID: 417c8d68c3d1
Revises: 4908038c935e
Create Date: 2023-01-08 16:31:41.099490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "417c8d68c3d1"
down_revision = "4908038c935e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("phone_number", sa.String(length=25), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "phone_number")
    # ### end Alembic commands ###