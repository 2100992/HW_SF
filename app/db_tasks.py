import sqlalchemy as sa

metadata = sa.MetaData()

task_db = sa.Table('tasks', metadata,
    sa.Column('uid', sa.Integer, primary_key=True),
    sa.Column('desc', sa.Text),
    sa.Column('is_completed', sa.Boolean)
)