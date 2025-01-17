"""your message

Revision ID: 864e96738795
Revises: 79a1c3debd03
Create Date: 2023-09-12 07:14:31.283093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '864e96738795'
down_revision = '79a1c3debd03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###
