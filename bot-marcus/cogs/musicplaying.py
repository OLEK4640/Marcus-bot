import discord
from discord.ext import commands
import os
import json


class Ddd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy administracyjne załadowane pomyślnie!.')

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()


def setup(bot):
    bot.add_cog(Ddd(bot))