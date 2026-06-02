import os
import smtplib
import tkinter as tk
from tkinter import ttk, messagebox
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv

os.environ["TCL_LIBRARY"] = r"C:\Users\pjhgn\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\pjhgn\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def generate_training_email(scenario):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    templates = {
        "Password Reset Training": {
            "subject": "[TRAINING SIMULATION] Password Reset Awareness Example",
            "body": f"""
SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Password Reset Awareness

This is a simulated phishing-awareness training email.
No real credentials are requested.
No data is collected.

Training purpose:
- Learn how suspicious password reset emails may look
- Practice identifying warning signs

Indicators:
- Urgent language
- Password-related request
- Generic greeting
- Link-based action request

Generated at: {current_time}
"""
        },
        "Invoice Training": {
            "subject": "[TRAINING SIMULATION] Invoice Awareness Example",
            "body": f"""
SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Invoice Awareness

This is a simulated training email.
No attachment is included.
No payment is requested.

Training purpose:
- Learn how fake invoice emails may appear
- Practice checking sender and context

Indicators:
- Unexpected invoice
- Unknown sender
- Pressure to act quickly
- Attachment or payment request

Generated at: {current_time}
"""
        },
        "Security Alert Training": {
            "subject": "[TRAINING SIMULATION] Security Alert Awareness Example",
            "body": f"""
SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Security Alert Awareness

This is a simulated training email.
No login page is included.
No personal information is requested.

Training purpose:
- Learn how fake security alerts may look
- Practice verifying suspicious account warnings

Indicators:
- Fear-based wording
- Account suspension claim
- Login request
- Suspicious link

Generated at: {current_time}
"""
        }
    }

    return templates[scenario]["subject"], templates[scenario]["body"]

def preview_email():
    scenario = scenario_box.get()

    if not scenario:
        messagebox.showerror("Error", "Please select a training scenario.")
        return

    subject, body = generate_training_email(scenario)

    preview_window = tk.Toplevel(root)
    preview_window.title("Email Preview")
    preview_window.geometry("650x500")

    subject_label = tk.Label(
        preview_window,
        text=f"Subject: {subject}",
        font=("Arial", 11, "bold"),
        wraplength=600,
        justify="left"
    )
    subject_label.pack(pady=10, padx=10, anchor="w")

    body_text = tk.Text(preview_window, wrap="word", width=75, height=25)
    body_text.pack(padx=10, pady=10)

    body_text.insert("1.0", body)
    body_text.config(state="disabled")

def send_training_email():
    receiver_email = receiver_entry.get().strip()
    scenario = scenario_box.get()
    consent_checked = consent_var.get()

    if not receiver_email:
        messagebox.showerror("Error", "Please enter receiver email.")
        return

    if "@" not in receiver_email or "." not in receiver_email:
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    if not scenario:
        messagebox.showerror("Error", "Please select a training scenario.")
        return

    if not consent_checked:
        messagebox.showerror(
            "Safety Check",
            "You must confirm this is for authorised training/testing only."
        )
        return

    if not EMAIL_ADDRESS or not APP_PASSWORD:
        messagebox.showerror(
            "Environment Error",
            "EMAIL_ADDRESS or APP_PASSWORD is missing in .env file."
        )
        return

    try:
        subject, body = generate_training_email(scenario)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receiver_email
        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
            smtp.send_message(msg)

        messagebox.showinfo(
            "Success",
            f"Training email sent successfully to:\n{receiver_email}"
        )

    except Exception as e:
        messagebox.showerror("Send Failed", str(e))


root = tk.Tk()
root.title("Phishing Awareness Email Simulator")
root.geometry("520x420")

title_label = tk.Label(
    root,
    text="Phishing Awareness Email Simulator",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)

description_label = tk.Label(
    root,
    text="Safe training email sender for cybersecurity awareness practice.",
    wraplength=450
)
description_label.pack(pady=5)

email_label = tk.Label(root, text="Receiver Email:")
email_label.pack(pady=(20, 5))

receiver_entry = tk.Entry(root, width=50)
receiver_entry.pack()

scenario_label = tk.Label(root, text="Training Scenario:")
scenario_label.pack(pady=(20, 5))

scenario_box = ttk.Combobox(
    root,
    width=47,
    state="readonly",
    values=[
        "Password Reset Training",
        "Invoice Training",
        "Security Alert Training"
    ]
)
scenario_box.pack()
scenario_box.current(0)

consent_var = tk.BooleanVar()

consent_check = tk.Checkbutton(
    root,
    text="I confirm this email is for authorised training/testing only.",
    variable=consent_var,
    wraplength=450
)
consent_check.pack(pady=20)

preview_button = tk.Button(
    root,
    text="Preview Email",
    command=preview_email,
    width=25,
    height=2
)
preview_button.pack(pady=5)

send_button = tk.Button(
    root,
    text="Send Training Email",
    command=send_training_email,
    width=25,
    height=2
)
send_button.pack(pady=10)

footer_label = tk.Label(
    root,
    text="No credential collection, no impersonation, no malicious payloads.",
    fg="gray"
)
footer_label.pack(pady=15)

root.mainloop()