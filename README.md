# Phishing Email Simulator

A safe cybersecurity learning project built with Python.

This project simulates phishing-awareness training emails using Gmail SMTP and environment variables. The goal is to understand email automation, phishing indicators, and secure secret management in a controlled educational environment.

---

## Features

* Safe phishing-awareness email simulation
* Gmail SMTP integration
* Environment variable protection with `.env`
* Python email automation
* Security-focused project structure

---

## Technologies Used

* Python
* Gmail SMTP
* python-dotenv
* Git & GitHub
* Virtual Environment (`venv`)

---

## Project Structure

```text
phishing-email-simulator/
│
├── email_simulator/
│   └── send_training_email.py
│
├── .env
├── .gitignore
├── README.md
└── .venv/
```

---

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/phishing-email-simulator.git
cd phishing-email-simulator
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

#### Windows PowerShell

```powershell
.\.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install python-dotenv
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
EMAIL_ADDRESS=your_test_email@gmail.com
APP_PASSWORD=your_gmail_app_password
```

---

### 5. Run the Program

```bash
python email_simulator/send_training_email.py
```

---

## Security Notes

This project is designed strictly for educational and defensive cybersecurity purposes.

* No credential harvesting
* No impersonation
* No malicious payloads
* No real phishing attacks

Only safe phishing-awareness training simulations are performed.

---

## Learning Objectives

* Understand SMTP email automation
* Learn secure secret management
* Practice cybersecurity project structure
* Explore phishing awareness concepts
* Improve Python automation skills
