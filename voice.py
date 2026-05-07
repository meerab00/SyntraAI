import os
import tempfile
import whisper
import gradio as gr
from groq import Groq
from gtts import gTTS

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY not found. Add it in Hugging Face Space Secrets.")

client = Groq(api_key=GROQ_API_KEY)

whisper_model = whisper.load_model("base")

def voice_assistant(audio):
    if audio is None:
        return "Please record audio.", None

    # Step 1: Speech to Text
    result = whisper_model.transcribe(audio)
    user_text = result["text"]

    # Step 2: AI Response
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful AI voice assistant."},
            {"role": "user", "content": user_text}
        ],
        model="llama-3.1-8b-instant"
    )
    response_text = chat_completion.choices[0].message.content

    # Step 3: Text to Speech
    tts = gTTS(response_text)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)

    return response_text, temp_audio.name

with gr.Blocks() as demo:
    gr.Markdown("# 🎙️ Voice-to-Voice AI Assistant")
    gr.Markdown("Whisper + Groq + Google TTS")

    audio_input = gr.Audio(type="filepath", label="🎤 Speak Here")
    text_output = gr.Textbox(label="💬 Assistant Response")
    audio_output = gr.Audio(label="🔊 Voice Response")

    submit_btn = gr.Button("🚀 Generate Response")

    submit_btn.click(
        fn=voice_assistant,
        inputs=audio_input,
        outputs=[text_output, audio_output]
    )

demo.launch()
