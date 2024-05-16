"""added added_by field

Revision ID: 8f9b0d5b62bf
Revises: 
Create Date: 2024-05-16 13:52:29.490213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f9b0d5b62bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URLMap',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('original', sa.String(
                        length=256), nullable=False),
                    sa.Column('short', sa.String(length=16), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('short')
                    )
    op.create_index(op.f('ix_URLMap_timestamp'),
                    'URLMap', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_URLMap_timestamp'), table_name='URLMap')
    op.drop_table('URLMap')
    # ### end Alembic commands ###