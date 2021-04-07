import discord
from discord.ext import commands
import json
import os
import datetime

zaufani = [660890966127018036, 767044002209726497] # Nie używasz tego, po co ci?
nievip = "Hmm... Wygląda na to, że nie jesteś developerem marcusa" # Tego też nie


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
    
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
@commands.has_permissions(administrator=True)
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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction(bot.get_emoji(823893146832338954))
        
        
@bot.command()
async def debil(ctx):
    with open("./configi.json", 'r') as configjsonFile:
        config_data = json.load(configjsonFile)
        
    guild = ctx.guild
    kanal_id = int(config_data[str(guild.id)]["joinmsgchannel"])
    channel = bot.get_channel(kanal_id)
    await channel.send("cokolwiek")
    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

   
with open("./config.json", 'r') as configjsonFile:
    configData = json.load(configjsonFile)
    
TOKEN = configData["DISCORD_TOKEN"]

if __name__ == "__main__":
    bot.run(TOKEN)
