from datetime import datetime

def generate_training_email(scenario):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    templates = {
        "Password Reset Training": {
            "subject": "[TRAINING SIMULATION] Password Reset Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Password Reset Awareness

This is a simulated phishing-awareness training email.
No real credentials are requested.
No data is collected.

Generated at: {current_time}
"""
        },
        "Invoice Training": {
            "subject": "[TRAINING SIMULATION] Invoice Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Invoice Awareness

This is a simulated training email.
No attachment is included.
No payment is requested.

Generated at: {current_time}
"""
        },
        "Security Alert Training": {
            "subject": "[TRAINING SIMULATION] Security Alert Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Security Alert Awareness

This is a simulated training email.
No login page is included.
No personal information is requested.

Generated at: {current_time}
"""
        }
    }

    return templates[scenario]["subject"], templates[scenario]["body"]


def generate_html_body(scenario, body):
    html_body = f"""
<html>
<body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
    <div style="max-width: 600px; margin: auto; background-color: white; border-radius: 10px; border: 1px solid #ddd; overflow: hidden;">
        <div style="background-color: #1e3a8a; color: white; padding: 20px; text-align: center;">
            <h2>Cybersecurity Awareness Training</h2>
        </div>

        <div style="padding: 25px;">
            <h3 style="color: #111827;">{scenario}</h3>

            <p>{body.replace(chr(10), "<br>")}</p>

            <div style="text-align:center; margin-top:30px;">
                <a href="https://example.com/training"
                   style="background-color:#2563eb; color:white; padding:12px 20px; text-decoration:none; border-radius:6px; font-weight:bold;">
                   Review Training
                </a>
            </div>

            <p style="margin-top:30px; font-size:12px; color:gray;">
                This email is part of an authorised cybersecurity awareness simulation.
            </p>
        </div>
    </div>
</body>
</html>
"""
    return html_body