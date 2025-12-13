from transformers import pipeline
from langdetect import detect

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

responses = {
    "en": {
        "positive": "🙂 The sentiment is positive",
        "negative": "☹️ The sentiment is negative",
        "neutral": "😐 The sentiment is neutral"
    },
    "fa": {
        "positive": "🙂 احساس جمله مثبت است",
        "negative": "☹️ احساس جمله منفی است",
        "neutral": "😐 احساس جمله خنثی است"
    }
}

def analyze_sentiment(text):
    lang = detect(text)

    result = sentiment_pipeline(text)[0]
    label = result["label"]

    if "1" in label or "2" in label:
        sentiment = "negative"
    elif "3" in label:
        sentiment = "neutral"
    else:
        sentiment = "positive"

    message = responses.get(lang, responses["en"])[sentiment]
    return f"🌍 Language: {lang}\n{message}"