from fastapi.testclient import TestClient

from models.forests import ForestsModel


def mock_forest(db_session):
    db_session.add(
        ForestsModel(
            name="Amazon",
            type="conservation",
            thumbnail="https://img.com/1",
            description="A moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America.",
        )
    )
    db_session.commit()


def test_home_returns_200(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_a_forest_with_name_type_thumbnail_and_description(
    client: TestClient, db_session
):
    mock_forest(db_session)
    response = client.get("/")

    response_body = response.json()

    assert len(response_body) == 1

    forest = response_body[0]

    assert forest["name"] == "Amazon"
    assert forest["type"] == "conservation"
    assert forest["thumbnail"] == "https://img.com/1"
    assert (
        forest["description"]
        == "A moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America."
    )
