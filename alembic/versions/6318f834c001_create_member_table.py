"""create_member_table

Revision ID: 6318f834c001
Revises: be1203ac8486
Create Date: 2024-07-03 10:05:36.871026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6318f834c001'
down_revision: Union[str, None] = 'be1203ac8486'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("member",sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),     
        sa.Column('password' ,sa.String(700), nullable=False),
        sa.Column('email', sa.String(30), nullable=False, unique=True),
        sa.Column('membership_status', sa.String(10),nullable=True))


def downgrade() -> None:
     op.drop_table('member')
