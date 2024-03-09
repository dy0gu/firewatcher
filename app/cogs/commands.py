import discord
from discord.ext import commands
import logging
from constants import API_PATH, LOCATIONS


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        logging.debug(f"{interaction.user.name} played ping-pong!")
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send("pong", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
