import pytest
from fastapi.testclient import TestClient

from forests_api.main import app


@pytest.fixture()
def client() -> TestClient:
    yield TestClient(app)
