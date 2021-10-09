"""CM-791 session id updates

Revision ID: 8c375095efa7
Revises: f67f1970ee20
Create Date: 2021-08-29 15:31:52.957107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8c375095efa7"
down_revision = "f67f1970ee20"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "FK__climate_f__sessi__17036CC0", "climate_feed", type_="foreignkey"
    )
    op.drop_constraint("FK__scores__session___18EBB532", "scores", type_="foreignkey")
    op.drop_constraint("FK__scores__user_uui__30C33EC3", "scores", type_="foreignkey")
    op.drop_constraint("FK__signup__session___19DFD96B", "signup", type_="foreignkey")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(
        "FK__signup__session___19DFD96B",
        "signup",
        "sessions",
        ["session_uuid"],
        ["session_uuid"],
    )
    op.create_foreign_key(
        "FK__scores__user_uui__30C33EC3", "scores", "users", ["user_uuid"], ["uuid"]
    )
    op.create_foreign_key(
        "FK__scores__session___18EBB532",
        "scores",
        "sessions",
        ["session_uuid"],
        ["session_uuid"],
    )
    op.create_foreign_key(
        "FK__climate_f__sessi__17036CC0",
        "climate_feed",
        "sessions",
        ["session_uuid"],
        ["session_uuid"],
    )
    # ### end Alembic commands ###