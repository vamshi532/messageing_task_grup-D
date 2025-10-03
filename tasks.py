# tasks.py
import os
from celery import Celery
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from dotenv import load_dotenv

load_dotenv()

# Celery instance
celery_app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER", "amqp://guest:guest@localhost:5672//")
)

@celery_app.task
def send_email():
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")
    receiver_email = sender_email  # Sending to yourself

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Test Email from Messaging System"
    msg.attach(MIMEText("Hello! This is a test email from Flask + Celery system.", 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

@celery_app.task
def log_time():
    print(f"Logging time: {datetime.now()}")
