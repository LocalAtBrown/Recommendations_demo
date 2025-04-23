# tests/mocks.py
from app.models.interface import RecommenderModel


class MockModel(RecommenderModel):
    def predict(self, user_id: str, context: dict) -> list:
        return [f"mocked_item_for_{user_id}"]
