#!/usr/bin/python3
"""
prints the state passed as an argument to the script
"""
if __name__ == '__main__':
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    MY_USER, MY_PASS, MY_DB, MY_STATE = argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == MY_STATE).order_by(
            State.id).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
