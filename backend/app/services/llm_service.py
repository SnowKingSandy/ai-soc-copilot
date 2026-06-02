import os
import json
import re

from dotenv import load_dotenv
import google.generativeai as genai

from app.services.parser_service import extract_metadata
from app.services.playbook_service import get_playbook
from app.services.risk_service import calculate_risk

from app.agents.threat_detector import detect_threat
from app.agents.mitre_mapper import get_mitre_id

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_log(log_text: str):

    metadata = extract_metadata(log_text)

    threat_type = detect_threat(log_text)

    mitre_id = get_mitre_id(
        threat_type
    )

    playbook = get_playbook(
        threat_type
    )

    risk_score = calculate_risk(
        metadata["failed_attempts"],
        threat_type
    )

    prompt = f"""
You are a Senior SOC Analyst.

Analyze the security event.

SECURITY LOG:
{log_text}

PARSED METADATA:
{json.dumps(metadata, indent=2)}

RULE DETECTION:
{threat_type}

MITRE TECHNIQUE:
{mitre_id}

RISK SCORE:
{risk_score}/100

SECURITY PLAYBOOK:
{json.dumps(playbook, indent=2)}

Instructions:

1. Use the rule detection result.
2. Use the MITRE mapping.
3. Use the provided playbook actions.
4. Determine severity.
5. Determine attack type.
6. Estimate confidence.
7. Write a concise summary.
8. Generate recommendations based on the playbook.

Return ONLY valid JSON.

JSON FORMAT:

{{
    "severity": "",
    "attack_type": "",
    "confidence": 0.0,
    "summary": "",
    "recommendations": []
}}

Rules:
- Return JSON only.
- No markdown.
- No explanations.
- No code fences.
"""

    response = model.generate_content(
        prompt
    )

    raw_text = response.text.strip()

    try:

        # Extract JSON even if Gemini wraps it
        # in ```json ... ```
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

        result["metadata"] = metadata

        result["detected_threat"] = threat_type

        result["mitre_id"] = mitre_id

        result["playbook"] = playbook

        result["risk_score"] = risk_score

        return result

    except Exception as e:

        return {
            "severity": "UNKNOWN",
            "attack_type": threat_type,
            "confidence": 0.0,
            "summary": f"JSON parsing failed: {str(e)}",
            "recommendations": playbook["actions"],
            "metadata": metadata,
            "detected_threat": threat_type,
            "mitre_id": mitre_id,
            "playbook": playbook,
            "risk_score": risk_score,
            "raw_response": raw_text
        }