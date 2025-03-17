from discord.ext import commands
import logging
from version import __version__


class Events(commands.Cog):
    first: bool = True
    connected: bool = False

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        if not self.connected:
            self.connected = True

    @commands.Cog.listener()
    async def on_resumed(self):
        if not self.connected:
            self.connected = True
            logging.info("Reconnected!")

    @commands.Cog.listener()
    async def on_disconnect(self):
        if self.connected:
            self.connected = False
            logging.error(
                "Connection lost, a reconnect will be attempted until successful."
            )

    @commands.Cog.listener()
    async def on_ready(self):
        if self.first:
            self.first = False
            logging.info(
                f"{self.bot.user.name} v{__version__} with ID {self.bot.user.id} started."
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))
