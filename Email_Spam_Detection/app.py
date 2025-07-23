import streamlit as st
import joblib

# Load model
import os
model = joblib.load(os.path.join(os.path.dirname(__file__), 'spam_model.pkl'))


# Streamlit UI
st.set_page_config(page_title="Spam Email Classifier", layout="centered")
st.title("📧 Spam Email Detection")

input_text = st.text_area("Enter your email text below:", height=200)

if st.button("Check if Spam"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([input_text])[0]
        if prediction == 1:
            st.error("🚫 This email is classified as **SPAM**.")
        else:
            st.success("✅ This email is **NOT SPAM**.")
