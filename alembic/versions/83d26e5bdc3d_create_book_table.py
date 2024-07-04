"""create_book_table

Revision ID: 83d26e5bdc3d
Revises: 6318f834c001
Create Date: 2024-07-03 10:08:01.432709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83d26e5bdc3d'
down_revision: Union[str, None] = '6318f834c001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("book",sa.Column("id",sa.Integer, primary_key=True),
    sa.Column("title",sa.String(30), nullable=False),
    sa.Column("publication_date",sa.Date, nullable=True),
    sa.Column("genre",sa.String(50)),
    sa.Column("count",sa.Integer,nullable=True),
    sa.Column('author_name', sa.String(30), sa.ForeignKey('author.name'), nullable=True)
    )
    
    op.create_table(
        'member_books',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('member.id'), primary_key=True),
        sa.Column('book_id', sa.Integer, sa.ForeignKey('book.id'), primary_key=True)
    )


def downgrade() -> None:
    op.drop_table('book')
    op.drop_table('member_book')
