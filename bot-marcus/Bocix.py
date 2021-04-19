import discord
from discord.ext import commands
import json
import os
import datetime
import time
poczatek = time.monotonic()
from math import floor


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)
    
@bot.event
async def on_ready():
    global uruchomionyw
    uruchomionyw = str(floor((time.monotonic() - poczatek) * 1000)) + "ms"
    await bot.change_presence(activity=discord.Game("{} serwery | .help".format(str(len(bot.guilds)))))
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
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f"""**Pomyślnie zmieniono prefix na {prefix}**""")

    
@changeprefix.error
async def changeprefix_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Zły format komendy! Proszę użyć** `changeprefix <prefix>`')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction(bot.get_emoji(823893146832338954))

@bot.command()
async def nuke(ctx):
    if ctx.author.id == 660890966127018036:
        await ctx.channel.send("awiuawgfiagfiu")
        await ctx.channel.delete()
    else:
        await ctx.send("Tylko OLEK#4640 może używać tej komendy!")

@bot.listen('on_message')
async def on_message(message):
    gprefix = get_prefix(bot, message)
    if bot.user.mentioned_in(message):
        embed=discord.Embed(title="Ping-Help", description=f"> Mój prefix tutaj to: `{gprefix}`. \n > Wpisz `{gprefix}help` aby uzyskać pomoc.", color=0x680198)
        embed.set_footer(text="Autor bota : OLEK#4640")
        await message.channel.send(embed=embed)
        await bot.process_commands(message)
  

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

   
with open("./config.json", 'r') as configjsonFile:
    configData = json.load(configjsonFile)
    
TOKEN = configData["DISCORD_TOKEN"]

if __name__ == "__main__":
    bot.run(TOKEN)