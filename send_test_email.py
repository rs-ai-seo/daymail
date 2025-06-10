
import smtplib
from email.mime.text import MIMEText
import os

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
TO_EMAIL = "guy@r-s.co.il"

msg = MIMEText("שלום גיא,\n\nזהו מייל בדיקה ממערכת ה-SEO שלך. אם קיבלת את ההודעה הזו, תכתוב לי כאן: '✔️ הגיע'.\n\nתודה,\nהמערכת שלך")
msg["Subject"] = "בדיקה 1 – האם המייל הזה הגיע?"
msg["From"] = SMTP_USER
msg["To"] = TO_EMAIL

try:
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
    print("✔️ מייל נשלח בהצלחה.")
except Exception as e:
    print("❌ שגיאה בשליחת מייל:", e)
