from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from forests_api.env import DATABASE_URL
from models import Base


def engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.bind = engine
    return engine


Session = sessionmaker(bind=engine())
session = scoped_session(Session)
