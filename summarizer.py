import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="centered")

st.title("📝 Text Summarizer")
st.caption("Lamba text do — chota summary milega!")

input_text = st.text_area(
    "Apna Text Yahan Likho:",
    placeholder="Paste your long text here...",
    height=250
)

length = st.radio(
    "Summary Kitni Lambi Chahiye?",
    ["Short (2-3 lines)", "Medium (5-6 lines)", "Detailed (10+ lines)"],
    horizontal=True
)

if st.button("Summarize", use_container_width=True):
    if input_text.strip() == "":
        st.warning("Pehle kuch text likho!")
    else:
        with st.spinner("Summarizing..."):
            try:
                client = InferenceClient(
                    provider="novita",
                    api_key=st.secrets["HF_TOKEN"]
                )

                if length == "Short (2-3 lines)":
                    instruction = "Summarize the following text in 2-3 lines only."
                elif length == "Medium (5-6 lines)":
                    instruction = "Summarize the following text in 5-6 lines."
                else:
                    instruction = "Summarize the following text in detail with 10 or more lines."

                response = client.chat.completions.create(
                    model="meta-llama/llama-3.1-8b-instruct",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert text summarizer. Only provide the summary, no extra explanation."
                        },
                        {
                            "role": "user",
                            "content": f"{instruction}\n\nText: {input_text}"
                        }
                    ],
                    max_tokens=1024,
                )

                summary = response.choices[0].message.content
                st.success("Summary Ready! ✅")
                st.text_area("Summary:", value=summary, height=200)

            except Exception as e:
                st.error(f"Error: {str(e)}")
