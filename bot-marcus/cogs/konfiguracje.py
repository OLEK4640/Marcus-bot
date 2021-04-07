import json
import discord
from discord.ext import commands.Cog


class Configi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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

    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changechannel(self, ctx, id):
        with open('configi.json', 'r') as f:
            configi = json.load(f)

        configi[str(ctx.guild.id)] = {
            "joinmsgchannel" : id
        }

        with open ('configi.json', 'w') as f:
            json.dump(configi, f, indent=4)

        await ctx.send("""**Sukces!**""")


def setup(bot):
    bot.add_cog(Configi(bot))