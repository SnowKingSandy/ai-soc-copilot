from app.database import SessionLocal
from app.models.incident import Incident


def save_incident(data):

    db = SessionLocal()

    incident = Incident(
        severity=data["severity"],
        attack_type=data["attack_type"],
        detected_threat=data.get(
            "detected_threat",
            "UNKNOWN"
        ),
        mitre_id=data.get(
            "mitre_id",
            None
        ),
        risk_score=data["risk_score"],
        confidence=data["confidence"],
        source_ip=data["metadata"]["source_ip"],
        failed_attempts=data["metadata"]["failed_attempts"],
        summary=data["summary"]
    )

    db.add(incident)

    db.commit()

    db.refresh(incident)

    db.close()

    return incident


def get_all_incidents():

    db = SessionLocal()

    incidents = db.query(
        Incident
    ).all()

    db.close()

    return incidents

def delete_incident(incident_id):

    db = SessionLocal()

    incident = (
        db.query(Incident)
        .filter(
            Incident.id == incident_id
        )
        .first()
    )

    if incident:
        db.delete(incident)
        db.commit()

    db.close()