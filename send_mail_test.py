import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))
smtp_user = os.getenv("SMTP_USERNAME")
smtp_pass = os.getenv("SMTP_PASSWORD")
sender = os.getenv("SMTP_FROM")
recipient = os.getenv("SMTP_TO")

msg = EmailMessage()
msg["Subject"] = "ATS-Testmail"
msg["From"] = sender
msg["To"] = recipient
msg.set_content("Hallo! Dies ist ein Test vom ATS-Parser via SMTP.")

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
    print("✅ Mail erfolgreich gesendet.")
except Exception as e:
    print("❌ Fehler beim Senden:", e)

