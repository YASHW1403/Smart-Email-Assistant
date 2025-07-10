import os
import json

ESCALATION_LOG = "escalation_log.txt"

def escalate_email(email_text, predicted_category, confidence):
    reason = []
    if confidence < 0.6:
        reason.append("Low confidence")
    if predicted_category == "Other":
        reason.append("Unknown category")

    log_entry = {
        "email_text": email_text,
        "predicted_category": predicted_category,
        "confidence": confidence,
        "status": "escalated",
        "reason": ", ".join(reason)
    }

    with open(ESCALATION_LOG, "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    return {
        "status": "escalated",
        "reason": log_entry["reason"],
        "logged_to": ESCALATION_LOG
    }
