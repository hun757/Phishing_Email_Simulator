# Phishing Awareness Email Simulator

A cybersecurity awareness training simulator built with Python and Tkinter.

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

* Python
* Tkinter
* HTML/CSS
* SMTP (Gmail)
* dotenv
* Webbrowser module

---

## Project Structure

```text
project/
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
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Install Requirements

```bash
pip install python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
EMAIL_ADDRESS=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password
```

---

## Running the Application

Start the desktop application:

```bash
python main.py
```

Optional local web server for training pages:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/training_page.html
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
* Attachment selection support
* CSV bulk email campaigns
* SQLite dashboard
* Click tracking analytics
* User management system
* GitHub Pages deployment
* Executable packaging (.exe)

---

## Author

Jeonghun Park

