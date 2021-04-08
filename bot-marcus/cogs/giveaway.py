import discord
from discord.ext import commands
import datetime
import random
import time
import asyncio


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

class giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy administracyjne załadowane pomyślnie!.')

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def giveaway(self, ctx):
        await ctx.send("Zacznijmy giveaway! Opowiadaj na pytania w ciągu 15 sekund!")

        questions = ["Na którym kanale ma być giveaway?",
                    "Ile ma trwać giveaway?"
                    "Jaka jest nagroda?"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(i)

            try:
                msg = await self.bot.wait_for('message, timeout=15.0, check=check')
            except asyncio.TimeoutError:
                await ctx.send("nie odpowiedziałeś w odpowiednim czasie!")
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f'Nie oznaczyłeś poprawnie kanału!')
            return

        channel = self.bot.get_channel(c_id)

        time = convert(answers[1])
        if time == -1:
            await ctx.send(f'Nie użyłeś poprawnego czasu!')
            return
        elif time == -2:
            await ctx.send(f"nie")
            return

        prize = answers[2]

        await ctx.send(f"Giveaway jest teraz na {channel.mention} {answers[1]}!")

        embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

        embed.add_field(name = "Hosted by:", value = ctx.author.mention)

        embed.set_footer(text = f"Kończy się {answers[1]} od teraz!")

        my_msg = await channel.send(embed=embed)

        await my_msg.add_reaction("🎉")


        await asyncio.sleep(time)

        new_msg = await channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        await channel.send(f"Gratulacje! {winner.mention} wygrał {prize}")



def setup(bot):
    bot.add_cog(giveaway(bot))