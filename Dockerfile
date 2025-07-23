FROM python:3.13.2-alpine

WORKDIR /bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
