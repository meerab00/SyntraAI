
import streamlit as st

# Page config
st.set_page_config(page_title="SyntraAI", page_icon="🤖", layout="wide")

# Title
st.title("🤖 SyntraAI - AI Assistant")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Home", "Chatbot", "Translator", "Voice", "Summarizer", "Calculator"]
)

# HOME
if menu == "Home":
    st.subheader("Welcome to SyntraAI 🚀")
    st.write("Your all-in-one AI Assistant App")

    st.info("Select a feature from sidebar to start")

# CHATBOT
elif menu == "Chatbot":
    st.subheader("💬 AI Chatbot")

    user_input = st.text_input("Ask anything:")

    if st.button("Send"):
        # yahan tum apna chatbot module connect karna
        st.success(f"You asked: {user_input}")
        st.write("AI Answer will come here... (connect chatbot.py)")

# TRANSLATOR

import streamlit as st
from modules.translator import translate_textfrom modules.translator import translate_text

elif menu == "Translator":
    st.subheader("🌍 Translator")

    text = st.text_area("Enter text")
    lang = st.selectbox("Language", ["en", "ur", "fr", "es"])

    if st.button("Translate"):
        if text.strip():
            result = translate_text(text, lang)
            st.success(result)
        else:
            st.warning("Please enter text first")

    lang = st.selectbox("Translate to:", ["English", "Urdu"])

    if st.button("Translate"):
        st.success("Translated text will appear here")

# VOICE
elif menu == "Voice":
    st.subheader("🎤 Voice Assistant")

    st.write("Voice feature will be connected from voice.py")

# SUMMARIZER
elif menu == "Summarizer":
    st.subheader("📝 Text Summarizer")

    text = st.text_area("Enter long text")

    if st.button("Summarize"):
        st.success("Summary will appear here")

# CALCULATOR
elif menu == "Calculator":
    st.subheader("🧮 Smart Calculator")

    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            st.success(num1 + num2)
        elif operation == "Subtract":
            st.success(num1 - num2)
        elif operation == "Multiply":
            st.success(num1 * num2)
        elif operation == "Divide":
            if num2 != 0:
                st.success(num1 / num2)
            else:
                st.error("Cannot divide by zero")
