import discord
from discord.ext import commands
import json
import os
import datetime
import random

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1, 0xff0000, 0xff8c00, 0xfff700, 0x5eff00, 0x00ffff, 0x0011ff, 0xcc00ff, 0xff00bb]


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
        deskripszon = config_data[str(member.guild.id)][f"joinmsgdescription"]
        embed = discord.Embed(title=titel_join, description=deskripszon.format(member.mention), color=kolor_hex)
        channel = self.bot.get_channel(kanal_id)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        content = message.content[1:]
        if message.author.bot:
            return

        with open("./configi.json", 'r') as configjsonFile:
            config_data = json.load(configjsonFile)

        if message.channel.id == int(config_data[str(message.guild.id)]["kanalpropozycje"]):
            if message.content.startswith("%"):
                await message.delete()
                await channel.send(f"**Komentarz {message.author}:** {content}")
            else:
                await message.delete()
                mbed = discord.Embed(title=f"Propozycja {message.author}", description=message.content, color=random.choice(colors))
                mbed.set_footer(text="""Wstaw "%" przed wiadomością aby zrobić komentarz""")
                mag = await channel.send(embed=mbed)
                await mag.add_reaction("👍")
                await mag.add_reaction("👎")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open("./configi.json", 'r') as configjsonFile:
            config_data = json.load(configjsonFile)

        kanal_id = int(config_data[str(member.guild.id)]["leavemsgchannel"])
        kolor_hex = int(config_data[str(member.guild.id)]["leavemshcolor"], 16)
        titel_join = config_data[str(member.guild.id)]["leavemsgtitle"]
        deskripszon = config_data[str(member.guild.id)][f"joinmsgdesc"]
        embed = discord.Embed(title=titel_join, description=deskripszon.format(member.mention), color=kolor_hex)
        channel = self.bot.get_channel(kanal_id)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Join(bot))