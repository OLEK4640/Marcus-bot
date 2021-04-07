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

zaufani = ["660890966127018036, 767044002209726497"]
nievip = "Hmm... Wygląda na to, że nie jesteś developerem marcusa"

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix= get_prefix, case_insensitive=True)

with open("./config.json", 'r') as configjsonFile:
    configData = json.load(configjsonFile)

with open("./configi.json", 'r') as configjsonFile:
    config_data = json.load(configjsonFile)

    TOKEN = configData["DISCORD_TOKEN"]
    
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("OLEK#4640"))
    print("Pomyślnie załadowano główny moduł bota!")

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
@has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send("""**Pomyślnie zmieniono prefix na {prefix}**""")

@changeprefix.error
async def changeprefix_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Zły format komendy! Proszę użyć** `changeprefix <prefix>`')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction(bot.get_emoji(823893146832338954))
        
@bot.command(pass_context=True)
async def debil(ctx):
    guild = ctx.guild
    kanal_id = int(config_data[str(guild.id)]["joinmsgchannel"])
    channel = bot.get_channel(kanal_id)
    await channel.send("cokolwiek")

bot.run(TOKEN)