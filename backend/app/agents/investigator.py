import json
import re
from typing import Dict

from app.services.llm_service import model


def investigate(incident: Dict) -> Dict:
    """Use the Gemini model to generate an investigation report for an incident.

    Returns a dict with timeline, root_cause, attack_chain, recommended_actions.
    """

    prompt = f"""
You are a Senior SOC Investigator. Given the following incident record, produce a concise investigation report.

Incident JSON:
{json.dumps(incident, indent=2)}

Provide the output strictly as JSON with the following keys:
{{
  "timeline": "...",
  "root_cause": "...",
  "attack_chain": "...",
  "recommended_actions": ["action1", "action2"]
}}

Rules:
- Return only JSON. No markdown, no explanation.
- Keep items concise.
"""

    response = model.generate_content(prompt)

    raw_text = response.text.strip()

    try:
        match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if match:
            raw_text = match.group(0)

        result = json.loads(raw_text)

        # Ensure keys exist
        report = {
            "timeline": result.get("timeline", ""),
            "root_cause": result.get("root_cause", ""),
            "attack_chain": result.get("attack_chain", ""),
            "recommended_actions": result.get("recommended_actions", []),
        }

        return report

    except Exception as e:
        return {
            "timeline": "",
            "root_cause": f"LLM parsing failed: {str(e)}",
            "attack_chain": "",
            "recommended_actions": [],
            "raw_response": raw_text,
        }
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