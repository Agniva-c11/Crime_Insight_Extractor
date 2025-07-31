import streamlit as st
import os
from audio_processing.transcribe import transcribe_audio
from translation.translator import translate_to_english
from utils.clean_text import clean_text
from extraction.classifier import classify_complaint
from extraction.insights import extract_insights
from pydub import AudioSegment

st.title("🚓 Police Call Analytics – Crime Insight Extractor")

# File Uploader
uploaded_file = st.file_uploader("Upload an audio complaint (.wav or .mp3)", type=["wav", "mp3"])

if uploaded_file is not None:
    file_path = f"temp_audio.{uploaded_file.name.split('.')[-1]}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Convert MP3 to WAV if needed
    st.info("Transcribing audio...")
    if file_path.endswith(".mp3"):
        audio = AudioSegment.from_mp3(file_path)
        file_path = "temp_audio.wav"
        audio.export(file_path, format="wav")

    # Transcribe audio to text
    transcription = transcribe_audio(file_path)
    st.subheader("🗣️ Transcribed Text")
    st.write(transcription)

    # Translate transcribed text into english and clean it
    translated = translate_to_english(transcription)
    cleaned = clean_text(translated)
    st.subheader("🌍 Translated & Cleaned Text")
    st.write(cleaned)

    # Classify complaints into categories
    category, confidence = classify_complaint(cleaned)
    st.subheader("🔍 Complaint Category")
    st.json({"category": category, "confidence": round(confidence, 2)})

    # Extract crime related insights
    st.subheader("🧠 Extracted Insights")
    insights = extract_insights(cleaned)
    st.json(insights)

    os.remove(file_path)