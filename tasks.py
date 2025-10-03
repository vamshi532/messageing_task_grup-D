# tasks.py
from celery import Celery
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Celery instance
celery_app = Celery("tasks", broker="amqp://guest:guest@localhost:5672//")

@celery_app.task
def send_email():
    sender_email = "vamshinamala0@gmail.com"          # Your personal Gmail
    sender_password = "mnhh mudt obsl hdaq"             # Gmail App Password
    receiver_email = "vamshinamala0@gmail.com"        # Your personal Gmail

    # Email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Test Email from Messaging System"
    body = "Hello Vamshi! This is a test email sent from our Flask + Celery messaging system."
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server and send email
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
