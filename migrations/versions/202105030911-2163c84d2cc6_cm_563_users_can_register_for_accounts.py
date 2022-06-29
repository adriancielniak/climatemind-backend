"""CM-563 Users can register for accounts

Revision ID: 2163c84d2cc6
Revises: ff7f55e704ca
Create Date: 2021-05-03 09:11:53.181295

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = "2163c84d2cc6"
down_revision = "ff7f55e704ca"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("uuid", mssql.UNIQUEIDENTIFIER(), nullable=False))
    op.drop_constraint("fk_scores__user_uuid__users", "scores", type_="foreignkey")
    op.drop_index("ix_users__username", table_name="users")
    op.drop_column("users", "username")
    op.drop_constraint("pk_users", "users", type_="primary")
    op.drop_column("users", "user_uuid")
    sa.PrimaryKeyConstraint("uuid")
    op.create_primary_key("pk_users", "users", ["uuid"])
    op.create_foreign_key(None, "scores", "users", ["user_uuid"], ["uuid"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "user_uuid", mssql.UNIQUEIDENTIFIER(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "username",
            sa.VARCHAR(length=64, collation="SQL_Latin1_General_CP1_CI_AS"),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("users", "uuid")
    op.drop_constraint(None, "scores", type_="foreignkey")
    op.create_foreign_key(
        "FK__scores__user_uui__17F790F9",
        "scores",
        "users",
        ["user_uuid"],
        ["user_uuid"],
    )
    # ### end Alembic commands ###