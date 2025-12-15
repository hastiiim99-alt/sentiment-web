from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        res = sentiment_pipeline(text)[0]
        stars = int(res["label"][0])

        if stars <= 2:
            result = "منفی 😠"
        elif stars == 3:
            result = "خنثی 😐"
        else:
            result = "مثبت 😊"

    return render_template("index.html", result=result)

if name == "__main__":
    app.run(host="0.0.0.0", port=7860)