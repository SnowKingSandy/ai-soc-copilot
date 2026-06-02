from app.agents.graph import (
    graph
)

from app.services.parser_service import (
    extract_metadata
)

from app.agents.threat_detector import (
    detect_threat
)

from app.agents.mitre_mapper import (
    get_mitre_id
)

from app.services.playbook_service import (
    get_playbook
)


def analyze_log(log_text):

    metadata = extract_metadata(
        log_text
    )

    threat = detect_threat(
        log_text
    )

    mitre = get_mitre_id(
        threat
    )

    playbook = get_playbook(
        threat
    )

    result = graph.invoke(
        {
            "log_text": log_text,
            "metadata": metadata,
            "threat_type": threat,
            "mitre_id": mitre,
            "playbook": playbook,
            "risk_score": 0
        }
    )

    return result["report"]