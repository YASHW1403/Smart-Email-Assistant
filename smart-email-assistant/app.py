import streamlit as st
from orchestrator import process_email

st.set_page_config(page_title="Smart Email Assistant", layout="centered")

st.title("📬 Smart Email Assistant")
st.markdown("An Intelligent Email Classification and Response System, Integrated with Groq's LLaMA3 API")

with st.form("email_form"):
    email_text = st.text_area("✉️ Enter email content below:", height=150)
    submitted = st.form_submit_button("Process Email")

if submitted:
    if not email_text.strip():
        st.warning("Please enter a valid email.")
    else:
        with st.spinner("Analyzing email..."):
            result = process_email(email_text)

        st.markdown("### 📊 Classification Result")
        st.markdown(f"**Category:** `{result['predicted_category']}`")
        st.markdown(f"**Confidence:** `{result['confidence']}`")

        st.markdown("---")
        st.markdown("### 🤖 Generated Response")
        st.success(result["response"])

        if "escalation" in result:
            st.markdown("---")
            st.markdown("### 🚨 Escalation Triggered")
            st.error(f"**Reason:** {result['escalation']['reason']}")
            st.markdown(f"*Logged to:* `{result['escalation']['logged_to']}`")

