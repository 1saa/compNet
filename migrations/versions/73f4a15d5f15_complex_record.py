"""complex record

Revision ID: 73f4a15d5f15
Revises: ca8525ee9177
Create Date: 2020-04-09 16:54:39.560738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73f4a15d5f15'
down_revision = 'ca8525ee9177'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.add_column(sa.Column('assessment', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('complaint', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('demographics', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('history', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('plan', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('prescriptions', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('results', sa.String(length=140), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'role', ['role_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.drop_column('results')
        batch_op.drop_column('prescriptions')
        batch_op.drop_column('plan')
        batch_op.drop_column('history')
        batch_op.drop_column('demographics')
        batch_op.drop_column('complaint')
        batch_op.drop_column('assessment')

    # ### end Alembic commands ###