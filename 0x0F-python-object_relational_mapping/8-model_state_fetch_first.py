#!/usr/bin/python3
""" Prints first State object in a database."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import State, Base
from sys import argv


def main():
    """ Function not run when imported """
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).order_by(State.id).first()
    if rows:
        print(f"{rows.id}: {rows.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
