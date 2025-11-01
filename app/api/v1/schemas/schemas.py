from pydantic import BaseModel, Field
from typing import List


class Summary(BaseModel):
    summary: str = Field(
        description="Research summary.",
    )


class Insights(BaseModel):
    text: str = Field(
        "An introductory paragraph",
        description="Introductory text for the insights section.",
    )
    points: List[str] = Field(
        default_factory=list, description="List of key insights or bullet points."
    )


class Questions(BaseModel):
    text: str = Field(
        "An introductory paragraph",
        description="Introductory text for the questions section.",
    )
    points: List[str] = Field(
        default_factory=list,
        description="List of thought-provoking or follow-up questions.",
    )


class ResearchAnalysisResult(BaseModel):
    summary: Summary = Field(
        ..., description="Concise summary of the research content."
    )
    insights: Insights = Field(
        ..., description="Insights section with structured details."
    )
    questions: Questions = Field(
        ..., description="Questions section with reflective or exploratory points."
    )
