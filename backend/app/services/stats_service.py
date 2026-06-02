from app.database import SessionLocal
from app.models.incident import Incident


def get_stats():

    db = SessionLocal()

    incidents = db.query(
        Incident
    ).all()

    total = len(incidents)

    high = len(
        [
            i
            for i in incidents
            if i.severity == "HIGH"
        ]
    )

    critical = len(
        [
            i
            for i in incidents
            if i.severity == "CRITICAL"
        ]
    )

    medium = len(
        [
            i
            for i in incidents
            if i.severity == "MEDIUM"
        ]
    )

    low = len(
        [
            i
            for i in incidents
            if i.severity == "LOW"
        ]
    )

    db.close()

    return {
        "total_incidents": total,
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low
    }