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

class gufno(commands.Cog):

    def __init__(self, client):
        self.client = client

    #iwenty
    @commands.Cog.listener()
    async def on_ready(self):
        print('Komendy administracyjne załadowane pomyślnie!.')



def setup(client):
    client.add_cog(gufno(client))