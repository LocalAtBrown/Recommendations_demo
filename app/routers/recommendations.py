import os
from typing import Dict, Optional

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from ..logger import get_logger, logging
from ..models.interface import LocalModel, MockVertexModel, RecommenderModel


# ---- Model Dependency ----
def get_model() -> RecommenderModel:
    MODEL_BACKEND = os.getenv("MODEL_BACKEND", "local")
    print("running backend")
    print(f"MODEL_BACKEND={MODEL_BACKEND}")
    if MODEL_BACKEND == "vertex":
        model: RecommenderModel = (
            MockVertexModel()
        )  # Replace with real VertexAIPredictor when ready
    else:
        model: RecommenderModel = LocalModel()

    return model


router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# ---- Request/Response Models ----
class RecommendationRequest(BaseModel):
    user_id: str
    context: Optional[Dict] = {}


class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: list


@router.post("/", response_model=RecommendationResponse)
def get_recommendations(
    req: RecommendationRequest,
    logger: logging.Logger = Depends(get_logger),
    model: RecommenderModel = Depends(get_model),
    # This is an issue wherein the model is reloaded each time a http request is made.
    # There are additional options to cache or load the model on startup while still
    # maintaining the Depends functionality.
    # https://chatgpt.com/share/e/6808e692-e120-800f-bd88-51c1ae28f7d8
):
    user_id = req.user_id
    context = req.context or {}

    logger.info(f"Received request for user_id={user_id}, context={context}")
    recommendations = model.predict(user_id, context)
    return {"user_id": user_id, "recommendations": recommendations}
