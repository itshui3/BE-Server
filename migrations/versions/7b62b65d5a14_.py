"""empty message

Revision ID: 7b62b65d5a14
Revises: 9854a7fe5134
Create Date: 2020-04-30 10:55:40.870920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b62b65d5a14'
down_revision = '9854a7fe5134'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('action', sa.String(length=1024), nullable=True),
    sa.Column('damage', sa.Integer(), nullable=True),
    sa.Column('heal', sa.Integer(), nullable=True),
    sa.Column('armor', sa.Integer(), nullable=True),
    sa.Column('resuseable', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('merchant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('inventory', sa.String(length=1024), nullable=True),
    sa.Column('gold', sa.Integer(), nullable=True),
    sa.Column('HP', sa.Integer(), nullable=True),
    sa.Column('attack', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('npc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('ref', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('items', sa.String(length=1024), nullable=True),
    sa.Column('gold', sa.Integer(), nullable=True),
    sa.Column('HP', sa.Integer(), nullable=True),
    sa.Column('isHostile', sa.Boolean(), nullable=True),
    sa.Column('attack', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('ref')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('floor', sa.String(length=20), nullable=True),
    sa.Column('items', sa.String(length=1024), nullable=True),
    sa.Column('NPCs', sa.String(length=1024), nullable=True),
    sa.Column('mobs', sa.String(length=1024), nullable=True),
    sa.Column('north', sa.String(length=20), nullable=True),
    sa.Column('east', sa.String(length=20), nullable=True),
    sa.Column('south', sa.String(length=20), nullable=True),
    sa.Column('west', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('character_name', sa.String(length=100), nullable=True),
    sa.Column('character_type', sa.String(length=100), nullable=True),
    sa.Column('portrait', sa.String(length=1024), nullable=True),
    sa.Column('HP', sa.Integer(), nullable=True),
    sa.Column('MP', sa.Integer(), nullable=True),
    sa.Column('attack', sa.Integer(), nullable=True),
    sa.Column('gold', sa.Integer(), nullable=True),
    sa.Column('encounter_cd', sa.Integer(), nullable=True),
    sa.Column('current_room', sa.String(length=20), nullable=True),
    sa.Column('items', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('room')
    op.drop_table('npc')
    op.drop_table('merchant')
    op.drop_table('item')
    # ### end Alembic commands ###
