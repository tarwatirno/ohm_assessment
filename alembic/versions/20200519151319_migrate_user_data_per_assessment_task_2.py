"""Migrate user data per assessment task 2

Revision ID: 420f468207ef
Revises: 00000000
Create Date: 2020-05-19 15:13:19.777386

"""

# revision identifiers, used by Alembic.
revision = '420f468207ef'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column("user",sa.Column("address", sa.String(255)))
    op.add_column("user",sa.Column("zip_code", sa.String(5)))
    op.execute("update user set point_balance=5000 where user_id=1")
    op.execute("update user set address=\"350 Townsend St #424, San Francisco, CA\",zip_code=\"94107\" where user_id=2")
    op.execute("update user set tier=\"Silver\" where user_id=3")



def downgrade():
    pass
