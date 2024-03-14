import discord
from discord.ext import commands
import logging
import views.fires


def log_invocation(interaction: discord.Interaction):
    name: str = interaction.command.name
    user: str = interaction.user.id
    origin: str = f"guild {interaction.guild_id}" if interaction.guild_id else "DMs"
    logging.debug(f"Command /{name} invoked by user {user} in {origin}.")


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="fires", description="Get information on active fires in a location."
    )
    async def fires(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        log_invocation(interaction)

        await interaction.followup.send(
            view=views.fires.FiresView(),
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
