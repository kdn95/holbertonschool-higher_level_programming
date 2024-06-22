#!/usr/bin/python3
"""
    Contains class definition of state
    and instance base = declarative_base()
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()


class State(base):
    __tablename__ = 'states'
    # Primary key column
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


# Create the engine
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa')

Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create the tables in the database (if they don't already exist)
base.metadata.create_all(engine)
