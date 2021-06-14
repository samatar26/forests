import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from forests_api.dependencies import get_session
from forests_api.env import DATABASE_URL
from forests_api.main import app

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False)


@pytest.fixture(scope="module")
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture()
def db_session(connection) -> Session:
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()


@pytest.fixture()
def client(
    db_session,
) -> TestClient:
    def _get_session_override():
        yield db_session

    app.dependency_overrides[get_session] = _get_session_override

    yield TestClient(app)
