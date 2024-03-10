import discord
from discord.ext import commands
import logging
from constants import API_PATH, LOCATIONS


def log_invocation(interaction: discord.Interaction):
    name: str = interaction.command.name
    user: str = interaction.user.id
    origin: str = f"guild {interaction.guild_id}" if interaction.guild_id else "DMs"
    logging.debug(f"{name} command invoked by user {user} in {origin}.")


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        log_invocation(interaction)
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send("pong", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
