FROM python:3.13.2-alpine

WORKDIR /bot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]
