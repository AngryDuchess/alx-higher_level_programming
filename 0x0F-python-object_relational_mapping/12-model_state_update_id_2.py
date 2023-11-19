#!/usr/bin/python3
"""
updates an existing new object in the databse
"""
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from sys import argv

    MY_USER, MY_PASS, MY_DB = argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = session.query(State).where(State.id == 2).first()
    state_obj.name = 'New Mexico'
    session.commit()
    session.close()
