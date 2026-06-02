SECURITY_PLAYBOOKS = {

    "BRUTE_FORCE": {
        "mitre": "T1110",
        "severity": "HIGH",
        "actions": [
            "Block source IP",
            "Enable MFA",
            "Review account lockout policy",
            "Investigate successful logins"
        ]
    },

    "PORT_SCAN": {
        "mitre": "T1046",
        "severity": "MEDIUM",
        "actions": [
            "Monitor source IP",
            "Review firewall logs",
            "Check exposed services"
        ]
    },

    "MALWARE": {
        "mitre": "T1204",
        "severity": "HIGH",
        "actions": [
            "Isolate affected host",
            "Run malware scan",
            "Collect forensic evidence",
            "Review affected systems"
        ]
    },

    "RANSOMWARE": {
        "mitre": "T1486",
        "severity": "CRITICAL",
        "actions": [
            "Isolate affected host",
            "Disconnect network access",
            "Preserve forensic evidence",
            "Initiate incident response"
        ]
    },

    "SQL_INJECTION": {
        "mitre": "T1190",
        "severity": "HIGH",
        "actions": [
            "Block malicious requests",
            "Review database activity",
            "Check application logs",
            "Patch vulnerable endpoints"
        ]
    }
}