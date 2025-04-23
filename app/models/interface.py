from typing import Dict, List, Union

import pandas as pd

from ..logger import get_logger, logging

logger: logging.Logger = get_logger()


# ---- Model Interface ----
class RecommenderModel:
    def predict(self, user_id: str, context: Dict):
        raise NotImplementedError


# ---- Local Model Interface ----
class LocalModel(RecommenderModel):
    def __init__(self):
        logger.info("[LocalModel] Loading local model")
        interaction_matrix = pd.read_csv(
            "app/models/models/CF_Mem_engagement_time_cosine_similarity_1745421071.23957/interaction_matrix.csv",
            index_col=0,
            dtype={"user_pseudo_id": str},
        )
        similarity_matrix = pd.read_csv(
            "app/models/models/CF_Mem_engagement_time_cosine_similarity_1745421071.23957/similarity_matrix.csv",
            index_col=0,
            dtype={"user_pseudo_id": str},
        )
        self.model: CollaborativeFilteringMemoryModel = (
            CollaborativeFilteringMemoryModel(
                "engagement_time", "cosine", interaction_matrix, similarity_matrix
            )
        )
        logger.info("[LocalModel] loaded local model")

    def predict(self, user_id: str, context: Dict):
        return self.model.predict(user_id)


# ---- Mock Vertex AI Interface ----
class MockVertexModel(RecommenderModel):
    def predict(self, user_id: str, context: dict):
        logging.info("[MockVertexModel] Pretending to call Vertex AI")
        return ["item_x", "item_y"]


# ---- Model Class Zoo ----


class CollaborativeFilteringMemoryModel:
    """
    This model is (and must remain) a direct copy from
    app/models/notebooks/cf-ga4-dfp-memory.ipynb

    The functionality of this class depends on pandas data frame structure
    developed in the notebook. Should that shift, we may have compatibility issues.

    """

    def __init__(
        self,
        interaction_type: str,
        distance_metric: str,
        # e.g. "cosine", "euclidean", etc.
        interaction_matrix: pd.DataFrame,
        similarity_matrix: pd.DataFrame,
    ):
        self.interaction_type = interaction_type
        self.distance_metric = distance_metric
        self.interaction_matrix = interaction_matrix
        self.similarity_matrix = similarity_matrix

    def predict(
        self, user_id: str, top_n: int = 5
    ) -> List[Dict[str, Union[str, float]]]:
        # Grab all pages viewed by the user
        user_ratings = self.interaction_matrix.loc[user_id]
        # We need to filter user_ratings, b/c interaction_matrix included 0 as a fill value for missing ratings
        rated_items = user_ratings[user_ratings > 0].index.tolist()

        # For each user-interacted page, get the similarity scores of all other pages to that page
        scores = pd.Series(dtype=float)
        for item in rated_items:
            similar_items = self.similarity_matrix[item]
            scores = scores.add(similar_items, fill_value=0)

        # Remove already rated items
        scores = scores.drop(rated_items, errors="ignore")
        top_scores = scores.sort_values(ascending=False).head(top_n)

        # Convert to list of dicts
        return [
            {"page_location": str(page), "similarity": float(similarity)}
            for page, similarity in top_scores.items()
        ]
