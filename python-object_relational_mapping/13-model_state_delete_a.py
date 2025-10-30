#!/usr/bin/python3
"""Elimina todos los objetos State
con nombre que contenga la letra a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        (
            f"mysql+mysqldb://{sys.argv[1]}:"
            f"{sys.argv[2]}@localhost:3306/"
            f"{sys.argv[3]}"
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    session.commit()

    session.close()
