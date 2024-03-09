import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # @discord.app_commands.command(name="ping", description="Ping the bot!")
    # async def ping(self, interaction: discord.Interaction):
    #     await interaction.response.defer()
    #     await interaction.followup.send("Pong!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
