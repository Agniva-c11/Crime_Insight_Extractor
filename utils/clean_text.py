import re

def clean_text(text):
    # Replace multiple whitespace characters (tabs, newlines, etc.) with a single space
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing spaces
    return text.strip()