#!/usr/bin/python3
"""
Module contains script that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=Metadata())

class State(Base):
    """
    Class with id and name attributes of each State
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
