"""add active realizations to ensemble

Revision ID: abccdeea2826
Revises: 057555237953
Create Date: 2021-10-14 11:30:46.804752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "abccdeea2826"
down_revision = "057555237953"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ensemble",
        sa.Column("active_realizations", sa.ARRAY(sa.Integer()), nullable=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ensemble", "active_realizations")
    # ### end Alembic commands ###