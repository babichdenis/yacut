"""added added_by field

Revision ID: 6c33fb3a32c5
Revises: 8f9b0d5b62bf
Create Date: 2024-05-16 18:46:24.614953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c33fb3a32c5'
down_revision = '8f9b0d5b62bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_map',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original', sa.String(length=256), nullable=False),
    sa.Column('short', sa.String(length=16), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short')
    )
    op.create_index(op.f('ix_url_map_timestamp'), 'url_map', ['timestamp'], unique=False)
    op.drop_index('ix_URLMap_timestamp', table_name='URLMap')
    op.drop_table('URLMap')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URLMap',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('original', sa.VARCHAR(length=256), nullable=False),
    sa.Column('short', sa.VARCHAR(length=16), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short')
    )
    op.create_index('ix_URLMap_timestamp', 'URLMap', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_url_map_timestamp'), table_name='url_map')
    op.drop_table('url_map')
    # ### end Alembic commands ###