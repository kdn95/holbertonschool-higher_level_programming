#!/usr/bin/python3
"""Print all City objs
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = (session.query(State, City)
            .join(City, State.id == City.state_id).all())
    for row in rows:
        print("{0}: ({1}) {2}"
              .format(row.State.name, row.City.id, row.City.name))
