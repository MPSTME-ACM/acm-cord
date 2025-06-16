import smtplib
from email.message import EmailMessage
from config import SMTP_SEVER, SMTP_SERVER_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, ENABLE_SMTPS

def sendMail(name: str, emailId: str, inviteLink: str, dept: str, role: str):
    with open('mail.html', 'r', encoding='utf-8') as f:
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

    smtp = None
    try:
        if int(ENABLE_SMTPS) == 1:
            smtp = smtplib.SMTP_SSL(SMTP_SEVER, SMTP_SERVER_PORT)
        else:
            smtp = smtplib.SMTP(SMTP_SEVER, SMTP_SERVER_PORT)
            smtp.starttls()
            
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)

    except Exception as e:
        print(e)

    finally:
        if smtp:
            smtp.quit()