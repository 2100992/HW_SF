import sys
sys.path.append('.')

from app.db import metadata, vote_results
import sqlalchemy as sa

def creade_db(engine):
    engine = sa.create_engine(engine)
    metadata.create_all(engine)

    with engine.begin() as connection:
        for i, animal in enumerate(['cats', 'dogs', 'parrots'], start = 1):
            statement = vote_results.insert().values(
                id = i,
                name = animal,
                votes = 0
            )
            connection.execute(statement)

def main():
    creade_db('sqlite:///my_db.sqlite')

if __name__ == "__main__":
    main()