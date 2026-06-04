from pydantic import BaseModel
from typing import List


class InvestigateRequest(BaseModel):
    incident_id: int


class InvestigationResponse(BaseModel):
    timeline: str
    root_cause: str
    attack_chain: str
    recommended_actions: List[str]
