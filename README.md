# Police Call Analytics - Crime Insight Extractor

This project analyzez police complaint audio calls and extracts structured crime related information. It takes an audio file as input, transcribes it to text, translates it into english (if not in english), cleans the text, classifies the type of crime, and extracts key insights like location and time.

## Features

- Upload audio files (`.wav` or `.mp3`)
- Automatic speech-to-text transcription using Whisper
- Translation to English using Google Translate
- Text cleaning
- Complaint category classification using zero-shot learning
- Location and time extraction via regex

---

## Approach

The application follows these steps:

1. **Transcription**: Uses [Faster Whisper](https://github.com/guillaumekln/faster-whisper) for efficient audio transcription on CPU.
2. **Translation**: Detects the language of the transcription and translates it to English if needed using `deep_translator`.
3. **Text Cleaning**: Removes extra spaces and standardizes formatting using regex.
4. **Classification**: Applies zero-shot classification (Facebook’s `bart-large-mnli`) to categorize the complaint (e.g., Robbery, Assault).
5. **Insight Extraction**: Uses regex patterns to extract time and location references from the cleaned text.

---

## Setup Instruction

### 1. Clone the repository
- git clone https://github.com/Agniva-c11/Crime_Insight_Extractor
- cd Crime_Insight_Extractor

### 2. Create and Activate Virtual Environment
- python3 -m venv venv
- source venv/bin/activate        # For Windows: venv\Scripts\activate

### 3. Install required dependencies
- pip install -r requirements.txt

### 4. Run the app
- streamlit run app.py