import re

def extract_insights(text):
    # Simple regex-based location and time detection (placeholder)
    location_pattern = r"(?:in|at|on)\s([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)"
    time_pattern = r"\b(?:today|yesterday|tonight|last night|this morning|\d{1,2} ?(AM|PM)|\d{1,2}:\d{2})\b"

    # Find all matching locations and time
    locations = re.findall(location_pattern, text)
    times = re.findall(time_pattern, text)

    # Clean and structured extracted data
    return {
        "locations": list(set(locations)),
        "time": list(set([" ".join(t) if isinstance(t, tuple) else t for t in times])),
    }