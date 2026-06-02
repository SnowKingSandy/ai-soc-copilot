from app.knowledge_base.security_playbooks import (
    SECURITY_PLAYBOOKS
)

DEFAULT_PLAYBOOK = {
    "mitre": "UNKNOWN",
    "severity": "MEDIUM",
    "actions": [
        "Investigate the incident",
        "Review system logs",
        "Monitor affected assets",
        "Escalate to the security team if required"
    ]
}


def get_playbook(threat_type: str) -> dict:

    if not threat_type:
        return DEFAULT_PLAYBOOK

    playbook = SECURITY_PLAYBOOKS.get(
        threat_type.upper()
    )

    if playbook is None:

        print(
            f"[PLAYBOOK WARNING] No playbook found for threat type: {threat_type}"
        )

        return DEFAULT_PLAYBOOK

    return playbook