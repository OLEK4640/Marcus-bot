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

class Obrazki(commands.Cog):

    def __init__(self, client):
        self.client = client

    #iwenty
    @commands.Cog.listener()
    async def on_ready(self):
        print('Komendy obrazkowe załadowane pomyślnie!.')

    #komenty
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/meme/new.json?sort=all') as r:
                res = await r.json()
                embed=discord.Embed(title="Marcus - memy")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def nudes(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/pussy/new.json?sort=all') as r:
                res = await r.json()
                embed=discord.Embed(title="Marcus - nudes")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @nudes.error
    async def nudes_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')

    @commands.command(pass_context=True)
    async def doggo(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dog/new.json?sort=all') as r:
                res = await r.json()
                embed=discord.Embed(title="Marcus - doggo")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def boobs(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/boobs/new.json?sort=all') as r:
                res = await r.json()
                embed=discord.Embed(title="Marcus - boobs")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @boobs.error
    async def boobs_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')

    @commands.command(pass_context=True)
    async def aww(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/aww/new.json?sort=all') as r:
                res = await r.json()
                embed=discord.Embed(title="Marcus - aww")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def ass(self, ctx):
            embed = discord.Embed(title="", description="")

            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/ass/new.json?sort=all') as r:
                    res = await r.json()
                    embed=discord.Embed(title="Marcus - ass")
                    embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                    await ctx.send(embed=embed)

    @ass.error
    async def ass_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')

    @commands.command(pass_context=True)
    async def cat(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/cat/new.json?sort=all') as r:
                res = await r.json()
                embed=discord.Embed(title="Marcus - cat")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def bdsm(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/bdsm/new.json?sort=all') as r:
                res = await r.json()
                embed=discord.Embed(title="Marcus - bdsm")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @bdsm.error
    async def bdsm_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')

def setup(client):
    client.add_cog(Obrazki(client))