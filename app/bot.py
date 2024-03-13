import discord
from discord.ext import commands
import dotenv
import os
import logging


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=" ",
            intents=discord.Intents.none(),
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
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler(),
        ],
    )
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("discord").setLevel(logging.CRITICAL)

    dotenv.load_dotenv(dotenv.find_dotenv())
    BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")

    if not BOT_TOKEN:
        logging.critical(
            "BOT_TOKEN environment variable is missing, either set it manually before running the bot or create a .env file based on the provided .env.example file!"
        )
        return

    bot: Bot = Bot()

    try:
        bot.run(BOT_TOKEN, reconnect=True, log_handler=None)
    except discord.errors.HTTPException and discord.errors.LoginFailure as exception:
        logging.critical(
            f"{exception}, check if the BOT_TOKEN environment variable is correct!"
        )


if __name__ == "__main__":
    main()
