from discord.ext import commands
import logging
from constants import VERSION


class Events(commands.Cog):
    first: bool = True
    connected: bool = False

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        if not self.connected:
            self.connected = True

        if self.first:
            self.first = False
            logging.info(
                f"{self.bot.user.name} v{VERSION} with ID {self.bot.user.id} connected to Discord."
            )

    @commands.Cog.listener()
    async def on_resumed(self):
        if not self.connected:
            self.connected = True
        logging.info("Reconnected to Discord.")

    @commands.Cog.listener()
    async def on_disconnect(self):
        if self.connected:
            self.connected = False
            logging.error(f"Connection to Discord lost, reconnecting...")

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"Ready to respond!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))
