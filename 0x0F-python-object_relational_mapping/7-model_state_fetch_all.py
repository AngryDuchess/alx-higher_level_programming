#!/usr/bin/python3
"""
lists all state objects from a specified database
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from sys import argv


MY_USER, MY_PASS, MY_DB = argv[1:]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(MY_USER, MY_PASS, MY_DB),
                       pool_pre_ping=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id)
for row in states:
    print("{}: {}".format(row.id, row.name))
session.close()
