import discord
from discord.ext import commands
import dotenv
import os
import logging


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=None,
            intents=discord.Intents.default(),
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="commands!"
            ),
        )

    async def setup_hook(self) -> None:
        await self.load_extension("cogs.events")
        await self.load_extension("cogs.tasks")
        await self.load_extension("cogs.commands")
        await self.tree.sync()


def main():
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger("discord").setLevel(logging.WARNING)

    bot = Bot()
    dotenv.load_dotenv(dotenv.find_dotenv())
    BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")

    if not BOT_TOKEN:
        raise KeyError(
            "BOT_TOKEN environment variable was not set correctly, create a .env file based on the provided .env.example file!"
        )

    bot.run(BOT_TOKEN, reconnect=True, log_handler=None)


if __name__ == "__main__":
    main()
