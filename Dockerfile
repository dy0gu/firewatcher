FROM gorialis/discord.py:minimal

WORKDIR /app

COPY pyproject.toml .

RUN pip install .

COPY . .

ENTRYPOINT [ "python", "src/bot.py" ]
