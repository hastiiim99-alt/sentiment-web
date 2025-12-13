import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from sentiment import analyze_sentiment

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

app = Flask(__name__)

application = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("سلام! پیام بفرست تا احساسش رو بگم 🙂")

async def handle_message(update, context):
    text = update.message.text
    result = analyze_sentiment(text)
    await update.message.reply_text(result)

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route("/")
def home():
    return "Bot is running 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok"