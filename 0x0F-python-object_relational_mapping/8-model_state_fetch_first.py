#!/usr/bin/python3
"""
prints the first state object from a specified database
"""
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


MY_USER, MY_PASS, MY_DB = argv[1:]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(MY_USER, MY_PASS, MY_DB),
                       pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).first()
if (states is None):
    print('Nothing')
else:
    print("{}: {}".format(states.id, states.name))
session.close()
