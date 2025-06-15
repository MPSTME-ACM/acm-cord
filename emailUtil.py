import smtplib
from email.message import EmailMessage
from config import SMTP_SEVER, SMTP_SERVER_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM

def sendMail(name: str, emailId: str, inviteLink: str, dept: str, role: str):
    with open('email.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('{{name}}', name)\
               .replace('{{email}}', emailId)\
               .replace('{{link}}', inviteLink)\
               .replace('{{department}}', dept)\
               .replace('{{role}}', role)

    msg = EmailMessage()
    msg['Subject'] = f"💙 Welcome to the MUNSoc Family, You have been selected as {role} for {dept}"
    msg['From'] = EMAIL_FROM
    msg['To'] = emailId
    msg.set_content(f"Please join the discord server for MUNSoc 25-26 by using this link: {inviteLink}")
    msg.add_alternative(html, subtype='html')

    with smtplib.SMTP_SSL(SMTP_SEVER, SMTP_SERVER_PORT) as smtp:
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)
