import sys
sys.path.append('.')

tests_tasks = [
    'Проверить работу задачника',
    'Проверить возможность удаления задачи'
]

from app.db_tasks import metadata, task_db
import sqlalchemy as sa

def creade_db(engine):
    engine = sa.create_engine(engine)
    metadata.create_all(engine)

    with engine.begin() as connection:
        for i, desc in enumerate(tests_tasks, start = 1):
            statement = task_db.insert().values(
                uid = i,
                desc = desc,
                is_completed = False
            )
            connection.execute(statement)

def main():
    creade_db('sqlite:///my_db_tasks.sqlite')

if __name__ == "__main__":
    main()