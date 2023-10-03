
import smtplib
from email.message import EmailMessage

def send_email_alert(subject, to_email, smtp_server, smtp_port, smtp_user, smtp_pass, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        print("Email alert sent!")
    except Exception as e:
        print(f"Failed to send email alert. Error: {e}")
