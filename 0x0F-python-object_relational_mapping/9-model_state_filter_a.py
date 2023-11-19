#!/usr/bin/python3
"""
this module finds all states containing the letter a
"""
if __name__ == '__main__':
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv

    MY_USER, MY_PASS, MY_DB = argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(
             State.id)
    for row in states:
        print("{}: {}".format(row.id, row.name))
    session.close()
