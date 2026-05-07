
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="English to Urdu Translator", page_icon="🌐", layout="centered")

st.markdown("""
<style>
    #MainMenu, footer { visibility: hidden; }
    .stTextArea textarea { font-size: 16px; }
</style>
""", unsafe_allow_html=True)

st.title("🌐 English to Urdu Translator")
st.caption("Type English text — Urdu translation milegi!")

english_text = st.text_area(
    "English Text Likho:",
    placeholder="Type your English text here...",
    height=200
)

if st.button("Translate", use_container_width=True):
    if english_text.strip() == "":
        st.warning("Pehle kuch English text likho!")
    else:
        with st.spinner("Translating..."):
            try:
                client = InferenceClient(
                    provider="novita",
                    api_key=st.secrets["HF_TOKEN"]
                )

                response = client.chat.completions.create(
                    model="meta-llama/llama-3.1-8b-instruct",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert English to Urdu translator. Translate the given English text to Urdu script only. Do not add any explanation, just provide the Urdu translation."
                        },
                        {
                            "role": "user",
                            "content": f"Translate this to Urdu: {english_text}"
                        }
                    ],
                    max_tokens=1024,
                )

                urdu_translation = response.choices[0].message.content

                st.success("Translation Ready! ✅")
                st.text_area(
                    "Urdu Translation:",
                    value=urdu_translation,
                    height=200
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")
