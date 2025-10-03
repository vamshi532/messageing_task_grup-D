# app.py
import os
from flask import Flask
from tasks import send_email, log_time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return "Messaging system is running! Use /send to send email or /log to log time."

@app.route("/send")
def send():
    send_email.delay()
    return "✅ Email task sent to Celery worker!"

@app.route("/log")
def log():
    log_time.delay()
    return "✅ Log time task sent to Celery worker!"

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 8000))
    app.run(host="0.0.0.0", port=port)
