#!/usr/bin/python3
"""
lists all cities objects from a specified database
"""
if __name__ == "__main__":
    from sqlalchemy.orm import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import State, Base
    from model_city import City
    from sys import argv

    MY_USER, MY_PASS, MY_DB = argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (session.query(City, State).filter
              (City.state_id == State.id).order_by(City.id).all())
    for row in cities:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
    session.close()
