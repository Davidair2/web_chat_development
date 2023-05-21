"""empty message

Revision ID: 4befd9b27268
Revises: 8bc10dde6140
Create Date: 2023-05-20 22:33:18.414537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4befd9b27268'
down_revision = '8bc10dde6140'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('userinfo', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_userinfo_dob'), ['dob'], unique=False)

    with op.batch_alter_table('user_info', schema=None) as batch_op:
        batch_op.drop_index('ix_user_info_dob')

    op.drop_table('user_info')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=128), nullable=False))
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_column('username')

    op.create_table('user_info',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('dob', sa.DATETIME(), nullable=True),
    sa.Column('country', sa.VARCHAR(length=64), nullable=True),
    sa.Column('city', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_info', schema=None) as batch_op:
        batch_op.create_index('ix_user_info_dob', ['dob'], unique=False)

    with op.batch_alter_table('userinfo', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_userinfo_dob'))

    op.drop_table('userinfo')
    # ### end Alembic commands ###