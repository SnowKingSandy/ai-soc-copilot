from app.services.risk_service import (
    calculate_risk
)


def risk_agent(state):
    risk = calculate_risk(
        state["metadata"]["failed_attempts"],
        state["threat_type"]
    )

    state["risk_score"] = risk

    return state