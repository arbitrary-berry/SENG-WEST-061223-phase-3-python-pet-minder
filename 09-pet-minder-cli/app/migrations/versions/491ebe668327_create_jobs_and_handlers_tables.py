"""create jobs and handlers tables

Revision ID: 491ebe668327
Revises: 032892426402
Create Date: 2023-08-04 11:51:41.570531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '491ebe668327'
down_revision = '032892426402'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('handlers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('hourly_rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('request', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('fee', sa.Float(), nullable=True),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.Column('handler_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['handler_id'], ['handlers.id'], ),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobs')
    op.drop_table('handlers')
    # ### end Alembic commands ###
