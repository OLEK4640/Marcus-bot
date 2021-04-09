import discord
from discord.ext import commands
import json
import os
import datetime


class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy administracyjne załadowane pomyślnie!.')


    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("./configi.json", 'r') as configjsonFile:
            config_data = json.load(configjsonFile)

        kanal_id = int(config_data[str(member.guild.id)]["joinmsgchannel"])
        kolor_hex = int(config_data[str(member.guild.id)]["joinmsgcolor"], 16)
        titel_join = config_data[str(member.guild.id)]["joinmsgtitle"]
        deskripszon = config_data[str(member.guild.id)]["joinmsgdescription"]
        embed = discord.Embed(title=titel_join, description=deskripszon.format(member.mention), color=kolor_hex)
        channel = self.bot.get_channel(kanal_id)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Join(bot))