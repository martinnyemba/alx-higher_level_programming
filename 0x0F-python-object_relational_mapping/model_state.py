#!/usr/bin/python3
"""
Module contains script that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# receive a pre-existing MetaData object for declarative_base()
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class with id and name attributes of each State
    """
    __tablename__ = 'states'
    id = Column("id", Integer, unique=True, nullable=False, primary_key=True)
    name = Column("states_name", String(128), nullable=False)
