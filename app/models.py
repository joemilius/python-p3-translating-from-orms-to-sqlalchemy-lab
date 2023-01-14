#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    # Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
    pass

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    
