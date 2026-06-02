from typing import TypedDict


class IncidentState(TypedDict):

    log_text: str

    metadata: dict

    threat_type: str

    mitre_id: str

    playbook: dict

    risk_score: int

    report: dict