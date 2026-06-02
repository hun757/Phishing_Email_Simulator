import os
import tkinter as tk
from tkinter import ttk, messagebox
from dotenv import load_dotenv
import tempfile
import webbrowser

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
    html_body = generate_html_body(scenario, body)

    preview_html = f"""
    <html>
    <head>
        <title>Email Preview</title>
    </head>
    <body>
        <h3>Subject: {subject}</h3>
        <hr>
        {html_body}
    </body>
    </html>
    """

    with tempfile.NamedTemporaryFile(
        mode="w",
        delete=False,
        suffix=".html",
        encoding="utf-8"
    ) as file:
        file.write(preview_html)
        preview_path = file.name

    webbrowser.open(preview_path)


def view_logs():
    logs = read_email_logs()

    if logs is None:
        messagebox.showinfo("Logs", "No log file found.")
        return

    log_window = tk.Toplevel(root)
    log_window.title("Email Logs")
    log_window.geometry("750x500")
    log_window.configure(bg=BG_COLOR)

    text_area = tk.Text(
        log_window,
        wrap="word",
        bg=INPUT_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        font=("Consolas", 10),
        relief="flat"
    )
    text_area.pack(expand=True, fill="both", padx=15, pady=15)

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


#UI Theme

BG_COLOR = "#050807"
CARD_COLOR = "#0b0f0c"
TEXT_COLOR = "#39ff14"
SUB_TEXT_COLOR = "#9ca3af"
BUTTON_COLOR = "#0f3d1e"
BUTTON_HOVER = "#14532d"
INPUT_COLOR = "#020617"
BORDER_COLOR = "#39ff14"


root = tk.Tk()
root.title("Phishing Awareness Email Simulator")
root.geometry("700x760")
root.resizable(True, True)
root.configure(bg=CARD_COLOR)


style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Dark.TCombobox",
    fieldbackground=INPUT_COLOR,
    background=INPUT_COLOR,
    foreground=TEXT_COLOR,
    arrowcolor=TEXT_COLOR,
    bordercolor=BORDER_COLOR,
    lightcolor=BORDER_COLOR,
    darkcolor=BORDER_COLOR,
    selectforeground=TEXT_COLOR,
    insertcolor=TEXT_COLOR,
    relief="solid",
    padding=2
)
style.map(
    "Dark.TCombobox",
    fieldbackground=[
        ("readonly", INPUT_COLOR),
        ("focus", INPUT_COLOR),
        ("active", INPUT_COLOR)
    ],
    foreground=[
        ("readonly", TEXT_COLOR),
        ("focus", TEXT_COLOR),
        ("active", TEXT_COLOR)
    ],
    background=[
        ("readonly", INPUT_COLOR),
        ("focus", INPUT_COLOR),
        ("active", INPUT_COLOR)
    ],
    selectbackground=[
        ("readonly", INPUT_COLOR),
        ("focus", INPUT_COLOR),
        ("active", INPUT_COLOR)
    ],
    selectforeground=[
        ("readonly", TEXT_COLOR),
        ("focus", TEXT_COLOR),
        ("active", TEXT_COLOR)
    ],
    bordercolor=[
        ("readonly", BORDER_COLOR),
        ("focus", BORDER_COLOR),
        ("active", BORDER_COLOR)
    ],
    lightcolor=[
        ("readonly", BORDER_COLOR),
        ("focus", BORDER_COLOR),
        ("active", BORDER_COLOR)
    ],
    darkcolor=[
        ("readonly", BORDER_COLOR),
        ("focus", BORDER_COLOR),
        ("active", BORDER_COLOR)
    ]
)


canvas = tk.Canvas(
    root,
    bg=CARD_COLOR,
    highlightthickness=0,
    bd=0,
    takefocus=0
)
canvas.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(15, 0),
    pady=15
)

style.layout("Cyber.Vertical.TScrollbar",
[
    ('Vertical.Scrollbar.trough',
     {'children':
      [('Vertical.Scrollbar.thumb',
        {'expand': '1', 'sticky': 'nswe'})],
      'sticky': 'ns'})
])

style.configure(
    "Cyber.Vertical.TScrollbar",
    background=BUTTON_COLOR,
    troughcolor=BG_COLOR,
    bordercolor=BORDER_COLOR,
    arrowcolor=TEXT_COLOR,
    darkcolor=BUTTON_COLOR,
    lightcolor=BUTTON_COLOR,
    gripcount=0,
    arrowsize=14,
    width=14
)

style.map(
    "Cyber.Vertical.TScrollbar",
    background=[
        ("active", "#16a34a"),
        ("!active", BUTTON_COLOR)
    ]
)

scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=canvas.yview,
    style="Cyber.Vertical.TScrollbar"
)

scrollbar.pack(
    side="right",
    fill="y",
    padx=(0,5),
    pady=15
)

canvas.configure(yscrollcommand=scrollbar.set)

main_frame = tk.Frame(
    canvas,
    bg=CARD_COLOR,
    padx=20,
    pady=20,
    highlightbackground=BORDER_COLOR,
    highlightcolor=BORDER_COLOR,
    highlightthickness=2,
    bd=0,
    relief="flat",
    takefocus=0
)

canvas_window = canvas.create_window(
    (0, 0),
    window=main_frame,
    anchor="nw"
)

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


def resize_main_frame(event=None):
    canvas_width = canvas.winfo_width()

    canvas.itemconfig(
        canvas_window,
        width=canvas_width-10
    )

    canvas.configure(scrollregion=canvas.bbox("all"))


main_frame.bind("<Configure>", update_scroll_region)
canvas.bind("<Configure>", resize_main_frame)
root.bind("<Configure>", resize_main_frame)



def style_button(button):
    button.configure(
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground=BUTTON_HOVER,
        activeforeground=TEXT_COLOR,
        relief="solid",
        bd=1,
        cursor="hand2",
        font=("Consolas", 10, "bold")
    )


title_label = tk.Label(
    main_frame,
    text="[ PHISHING AWARENESS SIMULATOR ]",
    font=("Consolas", 20, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)
title_label.pack(pady=(5, 10))


description_label = tk.Label(
    main_frame,
    text="> authorised security training environment",
    wraplength=620,
    font=("Consolas", 11),
    bg=CARD_COLOR,
    fg=SUB_TEXT_COLOR
)
description_label.pack(pady=(0, 25))


email_label = tk.Label(
    main_frame,
    text="TARGET EMAIL:",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Consolas", 11, "bold")
)
email_label.pack(pady=(5, 6))


receiver_entry = tk.Entry(
    main_frame,
    width=58,
    bg=INPUT_COLOR,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief="flat",
    font=("Consolas", 11),
    highlightthickness=2,
    highlightbackground=BORDER_COLOR,
    highlightcolor=BORDER_COLOR,
    bd=0
)
receiver_entry.pack(ipady=8, pady=(0, 18))


scenario_label = tk.Label(
    main_frame,
    text="TRAINING MODULE:",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Consolas", 11, "bold")
)
scenario_label.pack(pady=(5, 6))


scenario_box = ttk.Combobox(
    main_frame,
    width=55,
    state="readonly",
    style="Dark.TCombobox",
    values=[
        "Password Reset Training",
        "Invoice Training",
        "Security Alert Training",
        "Delivery Notification Training",
        "HR Policy Update Training"
    ]
)
scenario_box.pack(ipady=5, pady=(0, 18))
root.option_add("*TCombobox*Listbox.background", INPUT_COLOR)
root.option_add("*TCombobox*Listbox.foreground", TEXT_COLOR)
root.option_add("*TCombobox*Listbox.selectBackground", BUTTON_COLOR)
root.option_add("*TCombobox*Listbox.selectForeground", TEXT_COLOR)
root.option_add("*TCombobox*Listbox.font", ("Consolas", 10))

body_label = tk.Label(
    main_frame,
    text="EMAIL PAYLOAD PREVIEW:",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Consolas", 11, "bold")
)
body_label.pack(pady=(5, 6))


body_text_box = tk.Text(
    main_frame,
    width=64,
    height=8,
    wrap="word",
    bg=INPUT_COLOR,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief="flat",
    bd=0,
    font=("Consolas", 11),
    highlightthickness=2,
    highlightbackground=BORDER_COLOR,
    highlightcolor=BORDER_COLOR
)
body_text_box.pack(pady=(0, 18))


scenario_box.current(0)
load_template_body()
def remove_focus(event=None):
    root.focus_set()

scenario_box.bind(
    "<<ComboboxSelected>>",
    lambda event: [load_template_body(), remove_focus()]
)
scenario_box.bind(
    "<FocusIn>",
    lambda e: scenario_box.selection_clear()
)


consent_var = tk.BooleanVar()

consent_check = tk.Checkbutton(
    main_frame,
    text="I confirm this email is for authorised training/testing only.",
    variable=consent_var,
    wraplength=600,
    bg=CARD_COLOR,
    fg=SUB_TEXT_COLOR,
    activebackground=CARD_COLOR,
    activeforeground=TEXT_COLOR,
    selectcolor=INPUT_COLOR,
    font=("Consolas", 10)
)
consent_check.pack(pady=(0, 22))


preview_button = tk.Button(
    main_frame,
    text="[ PREVIEW EMAIL ]",
    command=preview_email,
    width=24,
    height=1
)
preview_button.pack(pady=4, ipady=3)
style_button(preview_button)


view_logs_button = tk.Button(
    main_frame,
    text="[ VIEW LOGS ]",
    command=view_logs,
    width=24,
    height=1
)
view_logs_button.pack(pady=4, ipady=3)
style_button(view_logs_button)


send_button = tk.Button(
    main_frame,
    text="[ SEND TRAINING EMAIL ]",
    command=send_training_email,
    width=24,
    height=1
)
send_button.pack(pady=(8, 5), ipady=3)
style_button(send_button)


footer_label = tk.Label(
    main_frame,
    text="> no credential collection | no impersonation | no malicious payloads",
    bg=CARD_COLOR,
    fg=SUB_TEXT_COLOR,
    font=("Consolas", 9)
)
footer_label.pack(pady=(15, 0))


root.mainloop()