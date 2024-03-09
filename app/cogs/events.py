from discord.ext import commands
import logging
from constants import VERSION


class Events(commands.Cog):
    reconnect: bool = False
    connected: bool = False

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        if not self.connected:
            self.connected = True

        if not self.reconnect:
            self.reconnect = True

            from prettytable import PrettyTable

            table: PrettyTable = PrettyTable(header=False)
            table.add_row(
                [
                    self.bot.user.name,
                    self.bot.user.id,
                    VERSION,
                ]
            )
            logging.info(table)

            logging.info("Connected to Discord.")
        else:
            logging.info("Reconnected to Discord.")

    @commands.Cog.listener()
    async def on_disconnect(self):
        if self.connected:
            self.connected = False
            logging.critical("Connection to Discord lost!")

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"Ready to go!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))
