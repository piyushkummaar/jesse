"""empty message

Revision ID: eb49b4bad811
Revises: 0f6aecb6ebc6
Create Date: 2020-06-03 11:39:48.484455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb49b4bad811'
down_revision = '0f6aecb6ebc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tasks', app.database.db_types.JsonCustomType.JsonCustomType(), nullable=True),
    sa.Column('next_task_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=254), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('registration_date', sa.Float(), nullable=True),
    sa.Column('terms_and_conditions_checked', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_email_verified', sa.Boolean(), nullable=True),
    sa.Column('email_verification_date', sa.DateTime(), nullable=True),
    sa.Column('current_mentorship_role', sa.Integer(), nullable=True),
    sa.Column('membership_status', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=500), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('occupation', sa.String(length=80), nullable=True),
    sa.Column('organization', sa.String(length=80), nullable=True),
    sa.Column('slack_username', sa.String(length=80), nullable=True),
    sa.Column('social_media_links', sa.String(length=500), nullable=True),
    sa.Column('skills', sa.String(length=500), nullable=True),
    sa.Column('interests', sa.String(length=200), nullable=True),
    sa.Column('resume_url', sa.String(length=200), nullable=True),
    sa.Column('photo_url', sa.String(length=200), nullable=True),
    sa.Column('need_mentoring', sa.Boolean(), nullable=True),
    sa.Column('available_to_mentor', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('mentorship_relations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mentor_id', sa.Integer(), nullable=True),
    sa.Column('mentee_id', sa.Integer(), nullable=True),
    sa.Column('action_user_id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.Float(), nullable=False),
    sa.Column('accept_date', sa.Float(), nullable=True),
    sa.Column('start_date', sa.Float(), nullable=True),
    sa.Column('end_date', sa.Float(), nullable=True),
    sa.Column('state', sa.Enum('PENDING', 'ACCEPTED', 'REJECTED', 'CANCELLED', 'COMPLETED', name='mentorshiprelationstate'), nullable=False),
    sa.Column('notes', sa.String(length=400), nullable=True),
    sa.Column('tasks_list_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mentee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['mentor_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['tasks_list_id'], ['tasks_list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('relation_id', sa.Integer(), nullable=True),
    sa.Column('creation_date', sa.Float(), nullable=False),
    sa.Column('modification_date', sa.Float(), nullable=True),
    sa.Column('comment', sa.String(length=400), nullable=False),
    sa.ForeignKeyConstraint(['relation_id'], ['mentorship_relations.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks_list.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks_comments')
    op.drop_table('mentorship_relations')
    op.drop_table('users')
    op.drop_table('tasks_list')
    # ### end Alembic commands ###
