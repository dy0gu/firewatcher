FROM gorialis/discord.py

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN --mount=type=secret,id=BOT_TOKEN echo 'BOT_TOKEN="$(cat /run/secrets/token)"' > .env

CMD ["python", "app/bot.py"]
