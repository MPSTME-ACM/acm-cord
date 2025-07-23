import requests
from email.message import EmailMessage
from config import DOMAIN, MG_API_KEY, MG_FROM

MAILGUN_API_BASE = f"https://api.mailgun.net/v3/{DOMAIN}"

def sendMail(name: str, emailId: str, inviteLink: str, dept: str, role: str):
    with open('mail.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fill in placeholders
    html = html.replace('{{name}}', name)\
               .replace('{{email}}', emailId)\
               .replace('{{link}}', inviteLink)\
               .replace('{{department}}', dept)\
               .replace('{{role}}', role)

    # Fallback plain text
    plain_text = f"Please join the discord server for ACM 25-26 by using this link: {inviteLink}"

    # Send email via Mailgun API
    try:
        response = requests.post(
            f"{MAILGUN_API_BASE}/messages",
            auth=("api", MG_API_KEY),
            data={
                "from": MG_FROM,
                "to": [emailId],
                "subject": f"💙 Welcome to the ACM Family, You have been selected as {role} for {dept}",
                "text": plain_text,
                "html": html
            }
        )

        if response.status_code != 200:
            print(f"[ERROR] Mailgun API error: {response.status_code} {response.text}")

    except Exception as e:
        print(f"[ERROR] Exception while sending email: {e}")