from discord.ext import tasks, commands

class Tasks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    #     self.insanity.start()

    # def cog_unload(self):
    #     self.insanity.cancel()

    # @tasks.loop(minutes=5)
    # async def insanity(self):
    #     if self.bot.is_ready():
    #         print("Have I ever told you the definition of insanity?")

async def setup(bot: commands.Bot):
    await bot.add_cog(Tasks(bot))
