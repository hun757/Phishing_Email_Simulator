from datetime import datetime

def generate_training_email(scenario):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    templates = {
        "Password Reset Training": {
            "subject": "[TRAINING SIMULATION] Password Reset Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Password Reset Awareness

This is a simulated phishing-awareness training email.

Warning signs:
- Urgent password reset request
- Generic greeting
- Link-based action

Generated at: {current_time}
"""
        },

        "Invoice Training": {
            "subject": "[TRAINING SIMULATION] Invoice Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Invoice Awareness

This is a simulated invoice awareness email.

Warning signs:
- Unexpected invoice
- Unknown sender
- Pressure to pay quickly

Generated at: {current_time}
"""
        },

        "Security Alert Training": {
            "subject": "[TRAINING SIMULATION] Security Alert Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Security Alert Awareness

This is a simulated security alert email.

Warning signs:
- Fear-based wording
- Account suspension claim
- Suspicious login request

Generated at: {current_time}
"""
        },

        "Delivery Notification Training": {
            "subject": "[TRAINING SIMULATION] Delivery Notification Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: Delivery Notification Awareness

This is a simulated delivery notification email.

Warning signs:
- Unexpected package message
- Tracking link pressure
- Unknown delivery provider

Generated at: {current_time}
"""
        },

        "HR Policy Update Training": {
            "subject": "[TRAINING SIMULATION] HR Policy Update Awareness Example",
            "body": f"""SAFE CYBERSECURITY TRAINING EMAIL

Scenario: HR Policy Update Awareness

This is a simulated HR policy email.

Warning signs:
- Unexpected HR document
- Request to open attachment
- Urgent internal policy update

Generated at: {current_time}
"""
        }
    }

    return templates[scenario]["subject"], templates[scenario]["body"]


def generate_html_body(scenario, body):
    formatted_body = body.replace("\n", "<br>")

    return f"""
<html>
<body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
    <div style="max-width: 650px; margin: auto; background-color: white; border-radius: 12px; border: 1px solid #ddd; overflow: hidden;">

        <div style="background-color: #1e3a8a; color: white; padding: 22px; text-align: center;">
            <h2 style="margin: 0;">Cybersecurity Awareness Training</h2>
            <p style="margin: 8px 0 0 0;">Authorised Simulation Email</p>
        </div>

        <div style="padding: 28px;">
            <h3 style="color: #111827;">{scenario}</h3>

            <p style="line-height: 1.6; color: #374151;">
                {formatted_body}
            </p>

            <div style="text-align:center; margin: 30px 0;">
                <a href="https://example.com/training"
                   style="background-color:#2563eb; color:white; padding:13px 24px; text-decoration:none; border-radius:8px; font-weight:bold;">
                   Review Training Material
                </a>
            </div>

            <div style="background-color:#fef3c7; padding:15px; border-radius:8px; color:#92400e; font-size:14px;">
                Training Reminder: Do not enter real passwords or personal information.
            </div>
        </div>

        <div style="background-color:#f3f4f6; padding:15px; text-align:center; font-size:12px; color:#6b7280;">
            Security Awareness Platform Demo
        </div>

    </div>
</body>
</html>
"""