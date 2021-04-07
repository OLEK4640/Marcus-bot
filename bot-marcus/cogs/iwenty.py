import discord
from discord.ext import commands


class Iwenty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy administracyjne załadowane pomyślnie!.')


def setup(bot):
    bot.add_cog(iwenty(bot))