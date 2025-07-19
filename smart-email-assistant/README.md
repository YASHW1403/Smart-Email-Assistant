# Smart Email Assistant 

Hey, Myself YASH SAMIR WADEKAR, so this is Smart Email Assistant project that I build. The project was to make a tool that can read company internal emails and reply to them automatically using machine learning and LLMs.

## What it does

So basically this assistant does 3 things:

1. Classifies emails into IT, HR or Other using ML (I used RandomForest and tfidf)
2. Replies to email using GenAI from Groq's LLaMA3 model. The replies are polite and clean.
3. Escalates emails if the model is confused or the confidence is low (like < 0.6)

It also logs escalations to a file for manual checking later.

I used a script to randomly mix them into a pandas DataFrame and saved to a CSV. You can check the script in the notebooks/ folder.
i have used scripts to directly generate CSV file for emails with categories rather then downloading CSV File from online.
data_generation.py is the file i used to vcreate emails which are stored in emails.csv

## Tech Stack

- Python
- scikit-learn
- transformers (but via API)
- Streamlit (for the UI)
- Groq API (for GenAI) -  Used for my Earlier project based on ML AI (Multiple Disease management System)
- dotenv for managing secrets - My grow api is saved here

## Folder Structure

```bash
smart-email-assistant/
├── agents/
│   ├── email_classifier.py
│   ├── response_generator.py
│   └── escalation_agent.py
├── models/
│   ├── email_classifier.pkl
│   └── vectorizer.pkl
├── data/
│   └── emails.csv
├── orchestrator.py
├── app.py
├── escalation_log.txt
├── .env
├── requirements.txt
└── README.md

## Folder Structure
There's a text box where you paste the email and when you hit the button it shows:
-> predicted category
-> confidence
-> AI-generated response 
-> or if escalated, the reason and log file name
