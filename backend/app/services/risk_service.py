def calculate_risk(
    failed_attempts: int,
    threat_type: str
):

    score = 0

    # Failed login weighting
    if failed_attempts >= 50:
        score += 50
    elif failed_attempts >= 20:
        score += 35
    elif failed_attempts >= 10:
        score += 20
    elif failed_attempts > 0:
        score += 10

    # Threat weighting
    threat_scores = {
        "BRUTE_FORCE": 30,
        "PORT_SCAN": 15,
        "MALWARE": 40,
        "RANSOMWARE": 60,
        "SQL_INJECTION": 35
    }

    score += threat_scores.get(
        threat_type,
        10
    )

    return min(score, 100)