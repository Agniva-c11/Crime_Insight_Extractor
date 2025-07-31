from deep_translator import GoogleTranslator
from langdetect import detect

def translate_to_english(text):
    """Detects the language of the input text and translates it to English if needed."""
    try:
        # Detect the language of the input text
        lang = detect(text)

        # If the language is not English, translate it to English
        if lang != 'en':
            translated = GoogleTranslator(source='auto', target='en').translate(text)
            return translated
        return text
    except Exception as e:
        return f"Translation error: {str(e)}"