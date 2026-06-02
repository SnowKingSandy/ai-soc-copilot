from pydantic import BaseModel


class Metadata(BaseModel):
    source_ip: str | None = None
    failed_attempts: int = 0


class Playbook(BaseModel):
    mitre: str
    severity: str
    actions: list[str]


class IncidentResponse(BaseModel):
    severity: str
    attack_type: str
    detected_threat: str
    mitre_id: str
    confidence: float
    risk_score: int
    summary: str
    recommendations: list[str]
    metadata: Metadata
    playbook: Playbook