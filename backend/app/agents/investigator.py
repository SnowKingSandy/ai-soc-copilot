def investigator_agent(state):
    metadata = state["metadata"]

    findings = []

    if metadata.get(
        "failed_attempts",
        0
    ) >= 20:

        findings.append(
            "High volume authentication failures"
        )

    if metadata.get(
        "source_ip"
    ):

        findings.append(
            f"Source IP: {metadata['source_ip']}"
        )

    state["findings"] = findings

    return state