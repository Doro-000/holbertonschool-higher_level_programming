#!/usr/bin/python3

"""changes the name of a State object from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    my_session = Session()
    state = my_session.query(State).get(2)
    state.name = 'New Mexico'
    my_session.commit()
    my_session.close()

