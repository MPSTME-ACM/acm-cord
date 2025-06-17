import csv
import time
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/XXXX/XXXX"
CSV_FILE = "members.csv"
DELAY_SECONDS = 20

def send_webhook_message(content: str):
    payload = {
        "content": content
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 204:
        print(f"Failed to send message: {response.status_code} - {response.text}")
    else:
        print("Message sent:", content)

def main():
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name'].strip()
            dept_id = row['Department Id'].strip()
            email = row['email'].strip()

            if not name or not dept_id or not email:
                print(f"Skipping invalid row: {row}")
                continue

            message = f"!register {dept_id} {email} {name}"
            send_webhook_message(message)
            time.sleep(DELAY_SECONDS)

if __name__ == "__main__":
    main()
