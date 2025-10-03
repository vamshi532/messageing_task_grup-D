# app.py
from flask import Flask
from tasks import send_email, log_time

flask_app = Flask(__name__)

# Home route
@flask_app.route("/")
def home():
    return "Messaging system is running! Use /send to send email or /log to log time."

# Route to trigger email task
@flask_app.route("/send")
def send():
    send_email.delay()  # run as Celery task
    return "✅ Email task sent to Celery worker!"

# Route to trigger log task
@flask_app.route("/log")
def log():
    log_time.delay()
    return "✅ Log time task sent to Celery worker!"

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=8000)
