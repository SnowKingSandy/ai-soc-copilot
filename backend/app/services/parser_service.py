import re


def extract_metadata(log_text: str):

    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    ip_matches = re.findall(
        ip_pattern,
        log_text
    )

    failed_attempts = 0

    match = re.search(
        r"(\d+)\s+failed",
        log_text.lower()
    )

    if match:
        failed_attempts = int(
            match.group(1)
        )

    return {
        "source_ip": ip_matches[0] if ip_matches else None,
        "failed_attempts": failed_attempts
    }