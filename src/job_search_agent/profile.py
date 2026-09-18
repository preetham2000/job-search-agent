import json
from pathlib import Path

from .schemas import CandidateProfile

def load_candidate_profile(file_path: str = 'data/profile.json') -> CandidateProfile:
    profile_path = Path(file_path)
    if not profile_path.exists():
        raise FileNotFoundError(f"Candidate profile not found: {profile_path}")

    with profile_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return CandidateProfile.model_validate(data)