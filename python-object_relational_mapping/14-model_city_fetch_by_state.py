#!/usr/bin/python3
"""Imprime todos los objetos City"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> "
              "<database name>".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        cities = session.query(City).filter(City.state_id == state.id).\
                 order_by(City.id)
        for city in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
