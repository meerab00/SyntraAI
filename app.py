
import streamlit as st
from modules.translator import translate_text
from modules.summarizer import summarize_text

st.set_page_config(page_title="SyntraAI", page_icon="🤖", layout="wide")

st.title("🤖 SyntraAI - AI Assistant")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Home", "Translator", "Summarizer", "Calculator"]
)

# HOME
if menu == "Home":
    st.subheader("Welcome to SyntraAI 🚀")
    st.write("AI Assistant App (Working Version)")

# TRANSLATOR
elif menu == "Translator":
    st.subheader("🌍 Translator")

    text = st.text_area("Enter text")
    lang = st.selectbox("Select language", ["en", "ur", "fr", "es"])

    if st.button("Translate"):
        if text.strip():
            result = translate_text(text, lang)
            st.success(result)
        else:
            st.warning("Please enter text")

# SUMMARIZER
elif menu == "Summarizer":
    st.subheader("📝 Summarizer")

    text = st.text_area("Enter paragraph")

    if st.button("Summarize"):
        if text.strip():
            result = summarize_text(text)
            st.success(result)
        else:
            st.warning("Please enter text")

# CALCULATOR
elif menu == "Calculator":
    st.subheader("🧮 Calculator")

    num1 = st.number_input("Number 1")
    num2 = st.number_input("Number 2")

    op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if op == "Add":
            st.success(num1 + num2)
        elif op == "Subtract":
            st.success(num1 - num2)
        elif op == "Multiply":
            st.success(num1 * num2)
        elif op == "Divide":
            if num2 != 0:
                st.success(num1 / num2)
            else:
                st.error("Cannot divide by zero")
