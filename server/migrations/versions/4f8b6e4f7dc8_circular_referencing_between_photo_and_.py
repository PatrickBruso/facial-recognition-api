"""circular referencing between photo and face

Revision ID: 4f8b6e4f7dc8
Revises: 96cc9a323b47
Create Date: 2022-04-06 01:48:13.915407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f8b6e4f7dc8'
down_revision = '96cc9a323b47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('thumbnail_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'profile', 'face', ['thumbnail_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'profile', type_='foreignkey')
    op.drop_column('profile', 'thumbnail_id')
    # ### end Alembic commands ###
