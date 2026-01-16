from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    preditcted_category: str = Field(
        ..., decription="The predicted insurance premium category",
        example = "High"
    )
    confidence: float = Field(
        ..., description="Model's confidence score for the predicted class (range: 0 to 1)",
        example=0.8432
    )
    class_probabilities: Dict[str, float] = Field(
        ..., description="Probabilities for each insurance premium category",
        example={
            "Low": 0.01,
            "Medium": 0.15,
            "High": 0.84}
    )