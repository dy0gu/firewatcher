import discord
from constants import LOCATIONS
import api
import logging


class FiresView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(DistrictDropdown())


class InfoEmbed(discord.Embed):
    def __init__(self, info: list[dict], town: str, error: bool = False):
        super().__init__(
            title=(
                f"There {'is' if len(info) == 1 else 'are'} "
                f"{f'no' if len(info) == 0 else f'{len(info)}'} "
                f"active fire{'' if len(info) == 1 else 's'} in {town}"
                f"{'!' if len(info) == 0 else ':'}"
                if not error else "Information could not be fetched at this time, please try again later."
            ),
            description=(
                f"{f'⠀{"".join(info)}' if len(info) != 0 else ''}"
                f"{'\n\n\nClick [here](https://fogos.pt/) to see more information.' if len(info) != 0 else ''}"
                if not error else ''
            ),
            timestamp=discord.utils.utcnow(),
            color=discord.Color.orange(),
            url=None
        )

class TownDropdown(discord.ui.Select):
    district: str

    def __init__(self, district: str, default: str = None):
        self.district = district
        options: list[discord.SelectOption] = [
            discord.SelectOption(label=town, value=town, default=town == default)
            for town in LOCATIONS[district]
        ]

        super().__init__(placeholder="Select a town!", options=options)

    async def callback(self, interaction: discord.Interaction):
        view: discord.ui.View = discord.ui.View()
        view.add_item(DistrictDropdown(self.district))
        view.add_item(TownDropdown(self.district, self.values[0]))

        fires: list[dict] = []
        error = False
        try:
            fires = api.fires(self.values[0])
        except Exception as e:
            logging.error(f"Failed to fetch data from API. {e}")
            error = True

        info: list[str] = [
            (f"{"\n" if i == 0 else '\n\n\n'}🌎⠀  {fire['location']}"
             f"\n\n🕝⠀  {fire['date']} {fire['hour']}"
             f"\n\n🧍⠀  {fire['man']}"
             f"\n\n🚒⠀  {fire['terrain']}"
             f"\n\n🚁⠀  {fire['aerial']}")
            for i, fire in enumerate(fires)
        ]

        embed = InfoEmbed(info, self.values[0], error)
        embed.set_footer(text="Powered by fogos.pt")
        await interaction.response.edit_message(embed=embed, view=view)


class DistrictDropdown(discord.ui.Select):
    def __init__(self, default: str = None):
        options: list[discord.SelectOption] = [
            discord.SelectOption(
                label=district, value=district, default=district == default
            )
            for district in LOCATIONS.keys()
        ]

        super().__init__(placeholder="Select a district!", options=options)

    async def callback(self, interaction: discord.Interaction):
        view: discord.ui.View = discord.ui.View()
        view.add_item(DistrictDropdown(self.values[0]))
        view.add_item(TownDropdown(self.values[0]))
        await interaction.response.edit_message(view=view)
