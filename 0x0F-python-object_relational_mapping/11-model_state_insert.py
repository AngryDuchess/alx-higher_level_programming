#!/usr/bin/python3
"""
adds a new object to our databse
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

    state_obj = State(name='Louisiana')
    session.add(state_obj)
    session.commit()
    print(state_obj.id)
    session.close()
