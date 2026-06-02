import os
from datetime import datetime

def save_email_log(receiver_email, scenario, status):
    os.makedirs("logs", exist_ok=True)

    log_file = os.path.join("logs", "email_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(
            f"[{timestamp}] Receiver: {receiver_email} | Scenario: {scenario} | Status: {status}\n"
        )


def read_email_logs():
    log_file = os.path.join("logs", "email_log.txt")

    if not os.path.exists(log_file):
        return None

    with open(log_file, "r", encoding="utf-8") as f:
        return f.read()