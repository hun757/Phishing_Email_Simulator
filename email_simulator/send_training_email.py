import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")

receiver_email = EMAIL_ADDRESS

msg = EmailMessage()

msg["Subject"] = "[TRAINING SIMULATION] Security Awareness Test"
msg["From"] = EMAIL_ADDRESS
msg["To"] = receiver_email

msg.set_content("""
SAFE CYBERSECURITY TRAINING EMAIL

This is a phishing-awareness simulation.
No malicious activity is performed.
""")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
    smtp.send_message(msg)

print("[+] Training email sent successfully.")