import sys
sys.path.append('.')

import sqlalchemy as sa
from app.db import vote_results
import json

def list_result(engine):
    engine = sa.create_engine(engine)
    result = {}
    with engine.begin() as connection:
        select = vote_results.select()
        results = connection.execute(select)
        for id, name, votes in results.fetchall():
            result[name] = votes
        result = json.dumps(result)
        return result

def main():
    print(list_result("sqlite:///my_db.sqlite"))

if __name__ == "__main__":
    main()
