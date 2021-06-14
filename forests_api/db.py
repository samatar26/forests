import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from forests_api.env import DATABASE_PASSWORD
from models import Base


def engine():
    url = sqlalchemy.engine.url.URL.create(
        drivername="postgresql+psycopg2",
        username="forests",
        database="forests",
        password=DATABASE_PASSWORD,
        query={
            "host": "{}/{}".format(
                "/cloudsql", "samatar-dev-43f2d25b:europe-west2:forests"
            )
        },
    )
    engine = create_engine(url)
    Base.metadata.bind = engine
    return engine


Session = sessionmaker(bind=engine())
session = scoped_session(Session)
