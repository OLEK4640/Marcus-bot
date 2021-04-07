import time
poczatek = time.monotonic()
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import asyncio
import aiohttp
import random
import os
from math import floor
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions, bot_has_permissions
from math import floor
import urllib.parse, urllib.request, re
from typing import Optional
import datetime

class configi(commands.Cog):

    def __init__(self, client):
        self.client = client

    #iwenty
    @commands.Cog.listener()
    async def on_ready(self):
        print('Komendy administracyjne załadowane pomyślnie!.')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('configi.json', 'r') as f:
            configi = json.load(f)

        configi[str(guild.id)] = {
            "joinmsgchannel" : "216136"
        }

        with open ('configi.json', 'w') as f:
            json.dump(configi, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('configi.json', 'r') as f:
            configi = json.load(f)

        configi.pop(str(guild.id))

        with open ('configi.json', 'w') as f:
            json.dump(configi, f, indent=4)





def setup(client):
    client.add_cog(configi(client))