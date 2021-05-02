import discord
from discord.ext import commands
import os
import json
import youtube_dl
from discord import FFmpegPCMAudio
import wavelink


class Ddd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


def setup(bot):
    bot.add_cog(Ddd(bot))