"""add bookings

Revision ID: 0cb957f20a43
Revises: 18fc2bdadbbc
Create Date: 2024-08-14 20:24:44.774367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0cb957f20a43'
down_revision: Union[str, None] = '18fc2bdadbbc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('date_from', sa.Date(), nullable=False),
    sa.Column('date_to', sa.Date(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('total_cost', sa.Integer(), sa.Computed('(date_to - date_from) * price', ), nullable=True),
    sa.Column('total_days', sa.Integer(), sa.Computed('(date_to - date_from) * price', ), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    # ### end Alembic commands ###