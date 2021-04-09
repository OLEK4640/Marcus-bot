import time
import discord
from discord.ext import commands
import asyncio
import random
from math import floor
from googlesearch import search
from random import choice as randchoice


class Rozrywka(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy rozrywkowe załadowane pomyślnie!.')


    @commands.command()
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
                strzal = await self.bot.wait_for('message', timeout=15.0, check=guess_check)
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


    @commands.command()
    async def reverse(self, ctx, *, tekst : str):
        tekst = tekst[::-1]
        await ctx.reply(tekst)


    @reverse.error
    async def reverse_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.reverse <tekst>`')


    @commands.command()
    async def botinvite(self, ctx):
        await ctx.reply("https://discord.com/api/oauth2/authorize?client_id=823530891938103366&permissions=0&scope=bot")


    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="{}".format(ctx.message.guild.name), description="Informacje")
        embed.add_field(name="ID serwera:", value="{}".format(str(ctx.message.guild.id)), inline=True)
        embed.add_field(name="Ilość ról:", value="{}".format(str(len(ctx.message.guild.roles))), inline=True)
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        embed.set_footer(text=ctx.message.guild.name)
        await ctx.reply(embed=embed)


    @commands.command()
    async def randomize(self, ctx, minimalny : int, maksymalny : int):
        await ctx.reply("Wylosowana liczba to {}.".format(str(random.randint(minimalny, maksymalny))))


    @randomize.error
    async def randomize_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Zły format komendy! Proszę użyć** `.randomize <liczba> <liczba>`')


    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.reply("Czekaj...")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content="Pong! :ping_pong: **{}ms**".format(str(floor(ping))))


    @commands.command()
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
        

    @commands.command()
    async def say(self, ctx, *, tekst):
        if "jestem glupi" in tekst:
            await ctx.send("Wiem xD")
        else:
            await ctx.send(tekst)


    @commands.command()
    async def choose(self, ctx, *choices):
        if len(choices) < 2:
            await ctx.send('Not enough choices to pick from.')
        else:
            await ctx.send(randchoice(choices))


    @commands.command()
    async def rps(self, ctx, choice : str):
        author = ctx.author
        rpsbot = {
            "rock" : ":moyai:",
            "paper": ":page_facing_up:",
            "scissors":":scissors:"
        }
        
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


    @commands.command()
    async def search_phrase(self, ctx, *, fraza):
        message = await ctx.reply("**Szukam...** :mag:")
        before = time.monotonic()
        for url in search(fraza):
            ping = (time.monotonic() - before) * 1000
            await message.edit(content="{}\nZnalazłem w **{}ms**".format(url, str(floor(ping))))
            break


def setup(bot):
    bot.add_cog(Rozrywka(bot))