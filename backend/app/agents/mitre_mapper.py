MITRE_MAPPING = {
    "BRUTE_FORCE": "T1110",
    "PORT_SCAN": "T1046",
    "MALWARE": "T1204",
    "RANSOMWARE": "T1486",
    "SQL_INJECTION": "T1190"
}


def get_mitre_id(threat_type: str):

    return MITRE_MAPPING.get(
        threat_type,
        "UNKNOWN"
    )