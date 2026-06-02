import os
import tkinter as tk
from tkinter import ttk, messagebox
from dotenv import load_dotenv

from email_templates import generate_training_email, generate_html_body
from email_sender import send_email
from logger import save_email_log, read_email_logs


load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def preview_email():
    scenario = scenario_box.get()

    if not scenario:
        messagebox.showerror("Error", "Please select a training scenario.")
        return

    subject, _ = generate_training_email(scenario)
    body = body_text_box.get("1.0", tk.END).strip()

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


def view_logs():
    logs = read_email_logs()

    if logs is None:
        messagebox.showinfo("Logs", "No log file found.")
        return

    log_window = tk.Toplevel(root)
    log_window.title("Email Logs")
    log_window.geometry("750x500")

    text_area = tk.Text(log_window, wrap="word")
    text_area.pack(expand=True, fill="both")

    text_area.insert("1.0", logs)
    text_area.config(state="disabled")


def load_template_body():
    scenario = scenario_box.get()

    if not scenario:
        return

    subject, body = generate_training_email(scenario)

    body_text_box.delete("1.0", tk.END)
    body_text_box.insert("1.0", body)


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
        subject, _ = generate_training_email(scenario)
        body = body_text_box.get("1.0", tk.END).strip()
        html_body = generate_html_body(scenario, body)

        attachment_path = None

        send_email(
            EMAIL_ADDRESS,
            APP_PASSWORD,
            receiver_email,
            subject,
            body,
            html_body,
            attachment_path
        )

        save_email_log(receiver_email, scenario, "SUCCESS")

        messagebox.showinfo(
            "Success",
            f"Training email sent successfully to:\n{receiver_email}"
        )

    except Exception as e:
        messagebox.showerror("Send Failed", str(e))
        save_email_log(receiver_email, scenario, f"FAILED: {e}")


root = tk.Tk()
root.title("Phishing Awareness Email Simulator")
root.geometry("520x620")
root.resizable(True, True)

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

body_label = tk.Label(root, text="Custom Email Body:")
body_label.pack(pady=(15, 5))

body_text_box = tk.Text(root, width=55, height=8, wrap="word")
body_text_box.pack()

scenario_box.current(0)
load_template_body()
scenario_box.bind("<<ComboboxSelected>>", lambda event: load_template_body())

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

view_logs_button = tk.Button(
    root,
    text="View Logs",
    command=view_logs,
    width=25,
    height=2
)
view_logs_button.pack(pady=5)

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