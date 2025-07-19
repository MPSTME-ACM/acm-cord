import smtplib
from email.message import EmailMessage
import socket  # For timeout
from config import SMTP_SEVER, SMTP_SERVER_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, ENABLE_SMTPS

def sendMail(emailId):
    print("[INFO] Preparing email...")
    
    msg = EmailMessage()
    msg['Subject'] = "💙 Welcome to the ACM Family"
    msg['From'] = EMAIL_FROM
    msg['To'] = emailId
    msg.set_content("Please join the discord server for ACM 25-26.")

    smtp = None
    try:
        # Set global socket timeout to avoid hanging
        socket.setdefaulttimeout(10)

        if int(ENABLE_SMTPS) == 1:
            print(f"[INFO] Connecting using SMTPS to {SMTP_SEVER}:{SMTP_SERVER_PORT}...")
            smtp = smtplib.SMTP_SSL(SMTP_SEVER, SMTP_SERVER_PORT, timeout=10)
        else:
            print(f"[INFO] Connecting using SMTP to {SMTP_SEVER}:{SMTP_SERVER_PORT}...")
            smtp = smtplib.SMTP(SMTP_SEVER, SMTP_SERVER_PORT, timeout=10)
            smtp.set_debuglevel(1)  # Enable SMTP debug output
            print("[INFO] Starting TLS...")
            smtp.starttls()


        smtp.set_debuglevel(1)  # Enable SMTP debug output
        print("[INFO] Logging in...")
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

        print(f"[INFO] Sending email to {emailId}...")
        smtp.send_message(msg)
        print("[SUCCESS] Email sent successfully!")

    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

    finally:
        if smtp:
            print("[INFO] Closing SMTP connection...")
            smtp.quit()

# Example call
sendMail("kartik@jkartik.in")
