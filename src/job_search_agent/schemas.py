from typing import Literal
from pydantic import BaseModel, Field

class EmploymentPreferences(BaseModel):
    exclude_staffing_companies: bool = True
    allow_established_consultancies: bool = True
    acceptable_consultancy_examples: list[str] = []
    avoid_layered_subcontracting: bool = True
    avoid_c2c_only_roles: bool = True

class CandidateProfile(BaseModel):
    target_roles: list[str]
    experience_years: float = Field(ge=0)
    education: list[str]
    skills: list[str]
    experience: list[str]
    certifications: list[str] = []
    preferred_locations: list[str] = []
    requires_future_sponsorship: bool = False
    employment_preferences: EmploymentPreferences
    constraints: list[str] = []

class ClassificationResult(BaseModel):
    decision: Literal["APPLY", "REVIEW", "SKIP"]

    fit_score: int = Field(ge=0, le=100, description="Overall job fit score from 0 to 100.")

    role_family: Literal[
        "software_engineering",
        "ai_ml",
        "cloud_devops",
        "other",
    ]

    matched_requirements: list[str]

    missing_requirements: list[str]

    hard_blockers: list[str]

    reasoning: str