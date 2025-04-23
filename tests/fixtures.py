import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.routers.recommendations import get_model
from tests.mocks import MockModel


@pytest.fixture
def fixture_client_with_mock_model():
    app.dependency_overrides[get_model] = lambda: MockModel()
    yield TestClient(app)
    app.dependency_overrides.clear()
