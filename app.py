import streamlit as st
from model import predict_job
from auth import auth
from db import save_history, get_history
from payments import payment_section

# Page config
st.set_page_config(page_title="AI Scam Detector", page_icon="🛑")

# Auth
user = auth()

if not user:
    st.stop()

# Payment
payment_section()

# UI
st.title("🛑 AI Fake Job Detector")
st.caption(f"Welcome {user} 👋")

# Input
job_text = st.text_area("📄 Enter Job Description")

# Button
if st.button("🔍 Analyze"):

    if job_text.strip() == "":
        st.warning("Enter text first")
    else:
        prediction, confidence, reasons = predict_job(job_text)

        if prediction == 1:
            result = "FAKE"
            st.error(f"🚨 Fake Job (Confidence: {confidence:.2f})")
        else:
            result = "REAL"
            st.success(f"✅ Real Job (Confidence: {confidence:.2f})")

        # Explain AI
        st.subheader("🧠 Reason")
        for word in reasons:
            st.write(f"👉 {word}")

        # Save history
        save_history(user, job_text, result, confidence)

# Show history
st.subheader("📊 Your History")

history = get_history(user)

for row in history:
    st.write(f"📝 {row[1][:50]}...")
    st.write(f"Result: {row[2]} | Confidence: {row[3]:.2f}")
    st.markdown("---")