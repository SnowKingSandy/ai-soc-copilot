from app.database import SessionLocal
from app.models.incident import Incident
from app.agents.investigator import investigate


def investigate_incident(incident_id: int):
    db = SessionLocal()

    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        db.close()
        return None

    # Convert SQLAlchemy model to dict for the agent
    incident_dict = {
        "id": incident.id,
        "severity": incident.severity,
        "attack_type": incident.attack_type,
        "detected_threat": incident.detected_threat,
        "mitre_id": incident.mitre_id,
        "confidence": incident.confidence,
        "risk_score": incident.risk_score,
        "source_ip": incident.source_ip,
        "failed_attempts": incident.failed_attempts,
        "summary": incident.summary,
    }

    report = investigate(incident_dict)

    db.close()

    return report
