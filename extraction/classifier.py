from transformers import pipeline

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

# Predefined crime categories for classification
CATEGORIES = ["Robbery", "Assault", "Cybercrime", "Theft", "Harassment"]

# Classifies a complaint into one of the predefined crime categories using zero-shot learning
def classify_complaint(text):
    result = classifier(text, CATEGORIES)
    return result['labels'][0], result['scores'][0]