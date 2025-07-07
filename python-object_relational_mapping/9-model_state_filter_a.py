#!/usr/bin/python3
"""Lista estados que contienen la letra 'a'"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    S = State
    states = session.query(S).filter(S.name.like('%a%')).order_by(S.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
