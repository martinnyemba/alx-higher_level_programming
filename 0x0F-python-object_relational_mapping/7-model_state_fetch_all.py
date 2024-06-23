#!/usr/bin/python3
"""
This script starts a link class to a table in a database
using SQLAlchemy. It connects to a MySQL database, queries the
State table and prints each state.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # create engine that connects to my sql database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create all tables in the database defined by Base's subclasses
    Base.metadata.create_all(engine)

    # Bind the engine to the session
    # Create a configured "Session" class and Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State table and order by State.id
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")

    # Close the Session
    session.close()
