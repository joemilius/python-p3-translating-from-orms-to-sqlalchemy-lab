from sqlalchemy import create_engine

from models import Dog

engine = create_engine('sqlite:///:memory:')

def create_table(base):
    base.metadata.create_all(engine)
    return engine
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    return session
    pass

def new_from_db(session, row):
    return session.query(Dog).filter_by(id = row.id).first()
    pass

def get_all(session):
    return [dog for dog in session.query(Dog)]
    pass

def find_by_name(session, name):
    return session.query(Dog).filter_by(name = name).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).filter_by(id = id).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    return session
    pass