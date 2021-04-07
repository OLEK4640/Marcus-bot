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
from asyncio import sleep as s
from random import randint
from random import choice as randchoice
from googlesearch import search

class Rozrywka(commands.Cog):

    def __init__(self, client):
        self.client = client

    #iwenty
    @commands.Cog.listener()
    async def on_ready(self):
        print('Komendy rozrywkowe załadowane pomyślnie!.')

    @commands.command(pass_context=True)
    async def guessthenumber(self, ctx, max:int=None):
        def guess_check(m):
            return m.content.isdigit() and m.author == ctx.message.author and m.channel == ctx.message.channel
        if max is None:
            liczba = random.randint(0, 1000)
        else:
            liczba = random.randint(0, max)
        zgadnieta = False
        proby = 0
        await ctx.reply("**Zacznij zgadywać.**")
        while not zgadnieta:
            try:
                strzal = await self.client.wait_for('message', timeout=15.0, check=guess_check)
            except asyncio.TimeoutError:
                await ctx.reply("**Czas minął!**")
                return
            proby = proby + 1
            if int(strzal.content) == liczba:
                if proby == 1:
                    await strzal.reply("<a:sukces:824225451089461249> Gratulacje! Odgadłeś liczbę! Zajęło ci to 1 próbę.")
                elif proby < 5:
                    await strzal.reply("<a:sukces:824225451089461249> Gratulacje! Odgadłeś liczbę! Zajęło ci to {} próby.".format(str(proby)))
                else:
                    await strzal.reply("<a:sukces:824225451089461249> Gratulacje! Odgadłeś liczbę! Zajęło ci to {} prób.".format(str(proby)))
                zgadnieta = True
            elif int(strzal.content) < liczba:
                await strzal.reply("*Wylosowana liczba jest większa.*")
            elif int(strzal.content) > liczba:
                await strzal.reply("*Wylosowana liczba jest mniejsza.*")

    @commands.command(pass_context=True)
    async def reverse(self, ctx, *, tekst : str):
        tekst = tekst[::-1]
        await ctx.reply(tekst)

    @reverse.error
    async def reverse_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.reverse <tekst>`')

    @commands.command(pass_context=True)
    async def botinvite(self, ctx):
        await ctx.reply("https://discord.com/api/oauth2/authorize?client_id=823530891938103366&permissions=0&scope=bot")

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="{}".format(ctx.message.guild.name), description="Informacje")
        embed.add_field(name="ID serwera:", value="{}".format(str(ctx.message.guild.id)), inline=True)
        embed.add_field(name="Ilość ról:", value="{}".format(str(len(ctx.message.guild.roles))), inline=True)
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        embed.set_footer(text=ctx.message.guild.name)
        await ctx.reply(embed=embed)

    @commands.command(pass_context=True)
    async def randomize(self, ctx, minimalny : int, maksymalny : int):
        await ctx.reply("Wylosowana liczba to {}.".format(str(random.randint(minimalny, maksymalny))))

    @randomize.error
    async def randomize_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.randomize <liczba> <liczba>`')

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.reply("Czekaj...")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content="Pong! :ping_pong: **{}ms**".format(str(floor(ping))))

    @commands.command(pass_context=True)
    async def timer(self, ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 300:
                await ctx.send("Zbyt duża liczba obciąża bota!")
                raise BaseException
            if secondint < 0:
                await ctx.send("Nie mogę liczyć od tyłu!")
                raise BaseException

            message = await ctx.send(f"Timer: {seconds}")

            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention} Twój czas się skończył!")
            
            while True:
                secondint -= 1
                if secondint == 0:
                    await message.edit(content="Czas się skończył!")
                    break
        except ValueError:
            await ctx.send("Musisz wpisać numer!")
        
    @commands.command(pass_context=True)
    async def say(self, ctx, *, tekst):
        await ctx.send(tekst)

    @commands.command()
    async def choose(self, ctx, *choices):
        """Chooses between multiple choices.

        To denote multiple choices, you should use double quotes.
        """
        if len(choices) < 2:
            await ctx.send('Not enough choices to pick from.')
        else:
            await ctx.send(randchoice(choices))

    @commands.command(pass_context=True)
    async def rps(self, ctx, choice : str):
        """Play rock paper scissors"""
        author = ctx.message.author
        rpsbot = {"rock" : ":moyai:",
           "paper": ":page_facing_up:",
           "scissors":":scissors:"}
        choice = choice.lower()
        if choice in rpsbot.keys():
            botchoice = randchoice(list(rpsbot.keys()))
            msgs = {
                "win": " You win {}!".format(author.mention),
                "square": " We're square {}!".format(author.mention),
                "lose": " You lose {}!".format(author.mention)
            }
            if choice == botchoice:
                await ctx.send(rpsbot[botchoice] + msgs["square"])
            elif choice == "rock" and botchoice == "paper":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "rock" and botchoice == "scissors":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "rock":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "scissors":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "rock":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "paper":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
        else:
            await ctx.send("Choose rock, paper or scissors.")

    @commands.command(pass_context=True)
    async def search_phrase(self, ctx, *, fraza):
        message = await ctx.reply("**Szukam...** :mag:")
        before = time.monotonic()
        for url in search(fraza):
            ping = (time.monotonic() - before) * 1000
            await message.edit(content="{}\nZnalazłem w **{}ms**".format(url, str(floor(ping))))
            break

def setup(client):
    client.add_cog(Rozrywka(client))