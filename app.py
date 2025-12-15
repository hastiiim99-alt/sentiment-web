from flask import Flask, render_template, request
from transformers import pipeline
from langdetect import detect

app = Flask(__name__)

# مدل سبک چندزبانه
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def get_sentiment_label(text, lang):
    result = sentiment_pipeline(text)[0]
    stars = int(result["label"][0])

    if stars <= 2:
        return "منفی 😠" if lang == "fa" else "Negative 😠"
    elif stars == 3:
        return "خنثی 😐" if lang == "fa" else "Neutral 😐"
    else:
        return "مثبت 😊" if lang == "fa" else "Positive 😊"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        lang = detect(text)  # تشخیص زبان
        result = get_sentiment_label(text, "fa" if lang == "fa" else "en")
    return render_template("index.html", result=result)

if name == "__main__":
    app.run(host="0.0.0.0", port=7860)