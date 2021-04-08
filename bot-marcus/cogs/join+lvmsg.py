import discord
from discord.ext import commands
import json
import os
import datetime


class join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy administracyjne załadowane pomyślnie!.')

    @commands.Cog.listener()
    async def on_member_join(self, ctx, *, member):
        with open("./configi.json", 'r') as configjsonFile:
            config_data = json.load(configjsonFile)

        kanal_id = int(config_data[str(ctx.guild.id)]["joinmsgchannel"])
        kolor_hex = int(config_data[str(ctx.guild.id)]["joinmsgcolor"])
        titel_join = int(config_data[str(ctx.guild.id)]["joinmsgtitle"])
        deskripszon = int(config_data[str(ctx.guild.id)]["joinmsgdescription"])
        embed = discord.Embed(title=titel_join, description=deskripszon, color=kolor_hex)
        channel = self.bot.get_channel(kanal_id)
        await channel.send(embed=embed)

        


def setup(bot):
    bot.add_cog(join(bot))