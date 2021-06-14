from fastapi.testclient import TestClient

from models.forests import ForestsModel


def mock_forest(db_session):
    db_session.add(
        ForestsModel(
            name="Amazon",
            type="conservation",
            thumbnail="https://img.com/1",
            description="A moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America.",
            country="Brazil",
            area=50,
            latitude=-90,
            longitude=-180,
            long_description="Jari Pará, an avoided deforestation project, preserves 50,480 hectares of primarily virgin Amazon forest. The project, which aims to promote forest conservation and reduce potential greenhouse gas emissions (GHG), likewise emphasizes the importance of local economic development. Over the project’s 30-year lifetime, it is expected to sequester nearly 15 million tonnes of carbon emissions. To prevent illegal deforestation, the project has pledged extensive surveillance and monitoring.",
            carbon_stored=100,
            carbon_stored_delta=10,
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


def test_home_returns_additional_forest_details_for_the_details_page(
    client: TestClient, db_session
):
    mock_forest(db_session)
    response = client.get("/")

    response_body = response.json()

    forest = response_body[0]

    assert forest["country"] == "Brazil"
    assert forest["latitude"] == -90
    assert forest["longitude"] == -180

    assert forest["area"] == 50
    assert (
        forest["long_description"]
        == "Jari Pará, an avoided deforestation project, preserves 50,480 hectares of primarily virgin Amazon forest. The project, which aims to promote forest conservation and reduce potential greenhouse gas emissions (GHG), likewise emphasizes the importance of local economic development. Over the project’s 30-year lifetime, it is expected to sequester nearly 15 million tonnes of carbon emissions. To prevent illegal deforestation, the project has pledged extensive surveillance and monitoring."
    )
    assert forest["carbon_stored"] == 100
    assert forest["carbon_stored_delta"] == 10
