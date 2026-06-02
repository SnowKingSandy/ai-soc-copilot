import os
import json
import re

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def reporter_agent(state):

    prompt = f"""
You are a Senior SOC Analyst.

SECURITY LOG:
{state['log_text']}

METADATA:
{json.dumps(state['metadata'], indent=2)}

THREAT TYPE:
{state['threat_type']}

MITRE:
{state['mitre_id']}

RISK SCORE:
{state['risk_score']}

PLAYBOOK:
{json.dumps(state['playbook'], indent=2)}

Generate a security incident report.

Return ONLY valid JSON.

{{
    "severity":"",
    "attack_type":"",
    "confidence":0.0,
    "summary":"",
    "recommendations":[]
}}
"""

    try:

        response = model.generate_content(
            prompt
        )

        raw_text = response.text.strip()

        match = re.search(
            r"\{.*\}",
            raw_text,
            re.DOTALL
        )

        if match:
            raw_text = match.group(0)

        result = json.loads(
            raw_text
        )

        result["metadata"] = state["metadata"]

        result["detected_threat"] = state["threat_type"]

        result["mitre_id"] = state["mitre_id"]

        result["playbook"] = state["playbook"]

        result["risk_score"] = state["risk_score"]

        state["report"] = result

        return state

    except Exception as e:

        print(
            f"[REPORTER ERROR] {str(e)}"
        )

        playbook = state.get(
            "playbook",
            {
                "severity": "MEDIUM",
                "actions": [
                    "Investigate the incident",
                    "Review system logs"
                ]
            }
        )

        state["report"] = {
            "severity": playbook.get(
                "severity",
                "MEDIUM"
            ),
            "attack_type": state["threat_type"],
            "confidence": 0.5,
            "summary": (
                f"Threat detected: "
                f"{state['threat_type']}. "
                f"LLM analysis unavailable."
            ),
            "recommendations": playbook.get(
                "actions",
                []
            ),
            "metadata": state["metadata"],
            "detected_threat": state["threat_type"],
            "mitre_id": state["mitre_id"],
            "playbook": playbook,
            "risk_score": state["risk_score"]
        }

        return state