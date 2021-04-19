import discord
from discord.ext import commands
import os
import json


class Gufno(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy administracyjne załadowane pomyślnie!.')


def setup(bot):
    bot.add_cog(Gufno(bot))