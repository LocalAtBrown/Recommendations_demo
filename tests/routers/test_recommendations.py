from tests.fixtures import fixture_client_with_mock_model

fixture_client_with_mock_model  # Ignore this. It's here just to prevent my IDE autoformatter from removing the import.


def test_recommendations(fixture_client_with_mock_model):
    client = fixture_client_with_mock_model
    response = client.post("/recommendations/", json={"user_id": "test_user"})

    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert data["recommendations"] == ["mocked_item_for_test_user"]


# Fill out unit tests as need arises
