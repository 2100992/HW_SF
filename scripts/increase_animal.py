import sys
sys.path.append('.')

import sqlalchemy as sa
from app.db import vote_results

def increase_animal(engine, animal):
    engine = sa.create_engine(engine)
    with engine.begin() as connection:
        select = vote_results.select().where(vote_results.c.name == animal)
        results = connection.execute(select)
        id, _, votes = results.fetchone()

        new_votes = votes + 1
        update = (
            vote_results.update().values(votes=new_votes).where(vote_results.c.id == id)
        )
        connection.execute(update)

def main():
    aminals = ['cats', 'dogs', 'parrots']
    for animal in aminals:
        increase_animal("sqlite:///my_db.sqlite", animal)

if __name__ == "__main__":
    main()
