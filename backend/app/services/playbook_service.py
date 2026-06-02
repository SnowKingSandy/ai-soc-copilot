from app.knowledge_base.security_playbooks import (
    SECURITY_PLAYBOOKS
)


def get_playbook(threat_type):

    return SECURITY_PLAYBOOKS.get(
        threat_type,
        None
    )