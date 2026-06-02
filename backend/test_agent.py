from app.agents.graph import graph

result = graph.invoke(
    {
        "log_text":
        "20 failed login attempts from IP 10.10.10.5",

        "metadata": {
            "source_ip": "10.10.10.5",
            "failed_attempts": 20
        },

        "threat_type": "BRUTE_FORCE",

        "mitre_id": "T1110",

        "playbook": {
            "actions": [
                "Block source IP"
            ]
        },

        "risk_score": 0
    }
)

print(result)