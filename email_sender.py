import os
import smtplib
import mimetypes
from email.message import EmailMessage

def add_attachment(msg, file_path):
    if not file_path:
        return

    if not os.path.exists(file_path):
        raise FileNotFoundError("Attachment file does not exist.")

    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type is None:
        mime_type = "application/octet-stream"

    main_type, sub_type = mime_type.split("/", 1)

    with open(file_path, "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype=main_type,
            subtype=sub_type,
            filename=os.path.basename(file_path)
        )


def send_email(email_address, app_password, receiver_email, subject, plain_body, html_body, attachment_path=None):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = receiver_email

    msg.set_content(plain_body)
    msg.add_alternative(html_body, subtype="html")

    if attachment_path:
        add_attachment(msg, attachment_path)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(email_address, app_password)
        smtp.send_message(msg)