# PhishLab – Phishing Awareness Email Simulator

## Overview

PhishLab is a Python-based phishing awareness training simulator designed for authorised cybersecurity education and security awareness demonstrations.

This project provides a safe phishing-awareness training environment using custom HTML emails, simulation landing pages, SMTP email delivery, logging features, and a hacker-style dark UI.

---

## Features

* Custom phishing-awareness training scenarios
* HTML email templates
* Browser-based HTML email preview
* SMTP email delivery using Gmail
* Hacker-style dark desktop UI
* Email sending logs
* Modular Python project structure
* Scenario simulation landing pages
* Safe training environment with no credential collection
* Executable (.exe) support using PyInstaller

---

## Training Scenarios

The simulator currently includes multiple awareness scenarios:

* Password Reset Training
* Invoice Training
* Security Alert Training
* Delivery Notification Training
* HR Policy Update Training

Each scenario generates different phishing-awareness style email content for cybersecurity education purposes.

---

## Technologies Used

* Python 3.13
* Tkinter
* HTML/CSS
* SMTP (Gmail)
* python-dotenv
* PyInstaller
* Webbrowser module

---

## Project Structure

```text
Phishing_Email_Simulator/
│
├── main.py
├── email_templates.py
├── email_sender.py
├── logger.py
├── training_page.html
├── logs/
├── .env
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/hun757/Phishing_Email_Simulator.git
cd Phishing_Email_Simulator
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```bash
pip install python-dotenv
pip install pyinstaller
```

---

## Configure Environment Variables

Create a `.env` file:

```env
EMAIL_ADDRESS=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password
```

---

## Running the Application

```bash
python main.py
```

---

## Build Executable

```powershell
pyinstaller --onedir --windowed --name PhishLab main.py
```

Executable output:

```text
dist/PhishLab/
```

Run executable:

```text
PhishLab.exe
```

---

## Safety Notice

This project is designed strictly for authorised cybersecurity awareness training and educational purposes.

The simulator:

* Does not collect credentials
* Does not impersonate real organisations
* Does not deploy malicious payloads
* Does not perform credential harvesting

All simulation pages clearly indicate authorised training after interaction.

---

## Future Improvements

* Scenario-specific phishing landing pages
* Attachment support
* CSV bulk email campaigns
* SQLite dashboard
* Click tracking analytics
* User management system
* GitHub Pages deployment
* Improved HTML templates

---

## Author

Jeonghun Park
Macquarie University – Cybersecurity / IT
