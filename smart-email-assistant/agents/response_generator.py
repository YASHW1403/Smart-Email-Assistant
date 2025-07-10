import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"

def extract_name(email_text):
    """
    Extracts name from 'I am Yash', 'I'm Rahul', 'This is Neha'.
    Returns: 'Yash' or None
    """
    match = re.search(r"(i am|i'm|this is)\s+([A-Z][a-z]+)", email_text, re.IGNORECASE)
    return match.group(2).strip().title() if match else None

CATEGORY_INSTRUCTIONS = {
    "HR": "You are an HR assistant. Write a professional response to the user's email.",
    "IT": "You are an IT helpdesk assistant. Write a concise and helpful response to the user's IT issue.",
    "Other": "You are a company assistant. Respond clearly and politely to the user's internal query."
}

def generate_response(email_text, predicted_category):
    if not GROQ_API_KEY:
        raise Exception("Missing GROQ_API_KEY. Add it to your .env file.")

    name = extract_name(email_text)
    greeting = f"Hi {name}," if name else "Hello,"

    instruction = CATEGORY_INSTRUCTIONS.get(predicted_category, CATEGORY_INSTRUCTIONS["Other"])
    prompt = f"{instruction}\n\n{greeting}\n\nEmail:\n{email_text}"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant responding to internal emails. "
                    "Use the sender's name only if it's mentioned. "
                    "You may use professional sign-offs like 'Best regards', but do NOT include placeholder names like [Your Name]."
                )
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.6
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    result = response.json()
    reply_text = result["choices"][0]["message"]["content"].strip()
    reply_text = re.sub(r"\[ ?(Your ?Name|Name) ?\]", "", reply_text, flags=re.IGNORECASE)

    return {
        "response": reply_text.strip()
    }
