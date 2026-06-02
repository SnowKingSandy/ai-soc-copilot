def detect_threat(log_text: str):

    log = log_text.lower()

    if "failed login" in log:
        return "BRUTE_FORCE"

    if "port scan" in log:
        return "PORT_SCAN"

    if "malware" in log:
        return "MALWARE"

    if "ransomware" in log:
        return "RANSOMWARE"

    if "sql injection" in log:
        return "SQL_INJECTION"

    return "UNKNOWN"