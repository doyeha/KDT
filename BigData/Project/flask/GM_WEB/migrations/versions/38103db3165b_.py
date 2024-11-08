"""empty message

Revision ID: 38103db3165b
Revises: 
Create Date: 2024-10-25 09:51:07.867328

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '38103db3165b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ap_comment')
    op.drop_table('nf_preds')
    op.drop_table('ap_preds')
    op.drop_table('gg_preds')
    op.drop_table('gold_preds')
    op.drop_table('gold_comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gold_comments',
    sa.Column('Date', sa.DATE(), nullable=False),
    sa.Column('comment', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('Date'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('gold_preds',
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('predicted', mysql.DOUBLE(asdecimal=True), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('gg_preds',
    sa.Column('date', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('predicted', mysql.DOUBLE(asdecimal=True), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ap_preds',
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('predicted', mysql.DOUBLE(asdecimal=True), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('nf_preds',
    sa.Column('date', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('predicted', mysql.DOUBLE(asdecimal=True), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ap_comment',
    sa.Column('Date', sa.DATE(), nullable=False),
    sa.Column('comments', mysql.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('Date'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
