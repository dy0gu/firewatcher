import discord
from discord.ext import commands
import logging
import requests
from constants import API_PATH, LOCATIONS


def log_invocation(interaction: discord.Interaction):
    name: str = interaction.command.name
    user: str = interaction.user.id
    origin: str = f"guild {interaction.guild_id}" if interaction.guild_id else "DMs"
    logging.debug(f"Command /{name} invoked by user {user} in {origin}.")


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(
        name="ping", description="Play some ping-pong with the bot!"
    )
    async def ping(self, interaction: discord.Interaction):
        log_invocation(interaction)
        await interaction.response.defer(ephemeral=True)

        await interaction.followup.send("pong", ephemeral=True)

    @discord.app_commands.command(
        name="fires", description="Get information on active fires in a location."
    )
    async def fires(self, interaction: discord.Interaction, location: str):
        log_invocation(interaction)
        await interaction.response.defer(ephemeral=True)

        location = location.capitalize()
        locations: list[str] = [
            town for district in LOCATIONS.values() for town in district
        ]

        if location not in locations:
            await interaction.followup.send(
                f"**{location}** is not a valid location, make sure you spelled it correctly or try another location.",
            )
            return

        api: str = f"{API_PATH}/incidents/active"
        response: requests.Response = requests.get(api)
        fires: list[dict] = {}
        try:
            data = response.json()
            if response.status_code != 200 or not data["success"]:
                raise Exception
            fires: list[dict] = data["data"]
        except:
            logging.error(f"Failed to fetch data from API.")
            await interaction.followup.send(
                "Information could not be fetched at this time, please try again later."
            )
            return

        fires = [fire for fire in fires if (location in fire["location"] and fire["active"])]

        if not fires:
            await interaction.followup.send(f"There are no active fires in **{location}**.")
        else:
            info: list[str] = [
                f"\n\n🌎 {fire["location"]}\n🕝 {fire["date"]} {fire["hour"]}\n🧍 {fire["man"]}\n🚒 {fire["terrain"]}\n🚁 {fire["aerial"]}"
                for fire in fires
            ]
            await interaction.followup.send(
                f"There {"is" if len(fires) == 1 else "are"} **{len(fires)}** active fire{'' if len(fires) == 1 else 's'} in **{location}**: + {', '.join(info)}"
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
