import sqlalchemy as sa

from app.db import vote_results

aminals = ['cats', 'dogs', 'parrots']

def increase_animal(animal):
    engine = sa.create_engine("sqlite:///my_db.sqlite")
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
    for animal in aminals:
        increase_animal(animal)

if __name__ == "__main__":
    main()
