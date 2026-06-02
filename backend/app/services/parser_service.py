import re


def extract_metadata(log_text: str) -> dict:

    metadata = {
        "source_ip": None,
        "failed_attempts": 0
    }

    if not log_text:
        return metadata

    # Extract IP address
    ip_match = re.search(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        log_text
    )

    if ip_match:
        metadata["source_ip"] = ip_match.group()

    # Extract failed attempts
    failed_patterns = [
        r"(\d+)\s+failed",
        r"(\d+)\s+unsuccessful",
        r"(\d+)\s+login attempts",
        r"(\d+)\s+authentication attempts"
    ]

    for pattern in failed_patterns:

        match = re.search(
            pattern,
            log_text.lower()
        )

        if match:

            metadata["failed_attempts"] = int(
                match.group(1)
            )

            break

    return metadata