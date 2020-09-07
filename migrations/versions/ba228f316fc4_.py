"""empty message

Revision ID: ba228f316fc4
Revises: ff7bf83b6716
Create Date: 2020-06-15 16:25:58.647937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba228f316fc4'
down_revision = 'ff7bf83b6716'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks_list', sa.Column('tasks', app.database.db_types.JsonCustomType.JsonCustomType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks_list', 'tasks')
    # ### end Alembic commands ###