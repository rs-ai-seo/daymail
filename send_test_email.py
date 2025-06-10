from flask import Flask
import smtplib
import os
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/send_test_email")
def send_email():
    try:
        SMTP_HOST = os.environ.get("SMTP_HOST")
        SMTP_PORT = int(os.environ.get("SMTP_PORT"))
        SMTP_USER = os.environ.get("SMTP_USER")
        SMTP_PASS = os.environ.get("SMTP_PASS")
        TO_EMAIL = os.environ.get("TO_EMAIL")

        msg = MIMEText("המייל הזה נשלח אוטומטית מהמערכת שלך. אם קיבלת אותו, הכל עובד כראוי.")
        msg["Subject"] = "בדיקת מערכת SEO אוטומטית"
        msg["From"] = SMTP_USER
        msg["To"] = TO_EMAIL

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)

        return "✔️ נשלח מייל בהצלחה!"
    except Exception as e:
        return f"❌ שגיאה בשליחה: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
