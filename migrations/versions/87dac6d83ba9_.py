"""empty message

Revision ID: 87dac6d83ba9
Revises: bec135f8999f
Create Date: 2023-02-28 14:42:15.805527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87dac6d83ba9'
down_revision = 'bec135f8999f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz_result', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz_result', schema=None) as batch_op:
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###