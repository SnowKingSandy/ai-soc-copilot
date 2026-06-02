def detect_threat(log_text: str) -> str:

    if not log_text:
        return "UNKNOWN"

    log = log_text.lower()

    # Brute Force / Credential Stuffing
    brute_force_patterns = [
        "failed login",
        "failed authentication",
        "invalid password",
        "authentication failure",
        "login failed",
        "credential stuffing",
        "password spray",
        "password spraying"
    ]

    # Port Scanning / Reconnaissance
    port_scan_patterns = [
        "port scan",
        "nmap scan",
        "reconnaissance",
        "network scan",
        "service scan"
    ]

    # Malware
    malware_patterns = [
        "malware",
        "trojan",
        "virus",
        "worm",
        "spyware",
        "backdoor",
        "malicious file"
    ]

    # Ransomware
    ransomware_patterns = [
        "ransomware",
        "encrypted files",
        "file encryption",
        "ransom demand",
        "crypto locker"
    ]

    # SQL Injection
    sql_injection_patterns = [
        "sql injection",
        "union select",
        "or 1=1",
        "database attack",
        "sql payload"
    ]

    if any(pattern in log for pattern in brute_force_patterns):
        return "BRUTE_FORCE"

    if any(pattern in log for pattern in port_scan_patterns):
        return "PORT_SCAN"

    if any(pattern in log for pattern in malware_patterns):
        return "MALWARE"

    if any(pattern in log for pattern in ransomware_patterns):
        return "RANSOMWARE"

    if any(pattern in log for pattern in sql_injection_patterns):
        return "SQL_INJECTION"

    return "UNKNOWN"