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

class Administracyjne(commands.Cog):

    def __init__(self, client):
        self.client = client

    #iwenty
    @commands.Cog.listener()
    async def on_ready(self):
        print('Komendy administracyjne załadowane pomyślnie!.')

    #komenty
    @commands.command(pass_context=True)
    async def clear(self, ctx, ilosc : int):
        try:
            if not ctx.message.author.guild_permissions.manage_messages:
                await ctx.message.channel.send("Nie masz permisji do tego!")
                return
            await ctx.message.channel.purge(limit=ilosc)
            msg = await ctx.message.channel.send("✅ **Usunąłem {} wiadomości!**".format(str(ilosc)))
            await asyncio.sleep(3)
            await msg.delete()
        except Exception as e:
            await ctx.message.channel.send("Wystąpił błąd: \n {}: {}\n".format(type(e).__name__, e))

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.clear <ilość>`')

    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.Member, *, powod=None):
        if ctx.message.author.guild_permissions.kick_members:
            try:
                await user.kick(reason=powod)
                await ctx.send("<a:sukces:824225451089461249> Pomyślnie wyrzucono"+ user.mention)
            except Exception as e:
                await ctx.reply("Wystąpił błąd: \n```{}: {}```\n".format(type(e).__name__, e))
        else:
            await ctx.reply("**Niestety nie posiadasz permisji do tego!**")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.kick <użytkownik> <powód>`')

    @commands.command(pass_context=True)
    async def nick(self, ctx, user: discord.Member, *, nazwa):
        try:
            if ctx.message.author.guild_permissions.manage_nicknames:
                await user.edit(nick=nazwa)
                await ctx.send("<a:sukces:824225451089461249> **Pomyślnie zmieniono nick!**")
            else:
                await ctx.reply("**Niestety nie posiadasz permisji do tego!**")
        except Exception as e:
            await ctx.reply("Wystąpił błąd: \n```{}: {}```\n".format(type(e).__name__, e))

    @nick.error
    async def nick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.nick <użytkownik> <nick>`')

    @commands.command(pass_context=True)
    async def ban(self, ctx, user: discord.Member, *, powod=None):
        if ctx.message.author.guild_permissions.ban_members:
            try:
                await user.ban(reason=powod)
                await ctx.send("**<a:sukces:824225451089461249> Pomyślnie zbanowano użytkownika!**")
            except Exception as e:
                await ctx.reply("Wystąpił błąd: \n```{}: {}```\n".format(type(e).__name__, e))
        else:
            await ctx.reply("**Niestety nie posiadasz permisji do tego!**")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.ban <użytkownik> <powód>`')

    @commands.command(pass_context=True)
    async def unban(self, ctx, *, member):
        if ctx.message.author.guild_permissions.ban_members:
            try:
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        await ctx.send(f'<a:sukces:824225451089461249> **Pomyślnie odbanowano** {user.mention}!')
                        return
            except Exception as e:
                await ctx.reply("Wystąpił błąd: \n```{}: {}```\n".format(type(e).__name__, e))
        else:
            await ctx.reply("**Niestety nie posiadasz permisji do tego!**")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.unban <nazwa_użytkownika + tag>`')


def setup(client):
    client.add_cog(Administracyjne(client))