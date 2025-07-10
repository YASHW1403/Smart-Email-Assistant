
from agents.email_classifier import predict_category
from agents.response_generator import generate_response
from agents.escalation_agent import escalate_email

def process_email(email_text):
    print(f"\n📥 Received email: {email_text}")

    # Step 1: Classify
    classification = predict_category(email_text)
    category = classification["predicted_category"]
    confidence = classification["confidence"]

    print(f"🔍 Predicted: {category} (Confidence: {confidence})")

    # Step 2: Check escalation criteria
    needs_escalation = confidence < 0.6 or category == "Other"

    # Step 3: Always generate response for feedback
    response = generate_response(email_text, category)

    result = {
        "email_text": email_text,
        "predicted_category": category,
        "confidence": confidence,
        "response": response["response"]
    }

    if needs_escalation:
        escalation = escalate_email(email_text, category, confidence)
        result["escalation"] = escalation

    return result

# Test
if __name__ == "__main__":
    email = input("📧 Enter email text: ")
    result = process_email(email)

    print("\n📤 Final Output:")
    for k, v in result.items():
        print(f"{k}: {v}")
