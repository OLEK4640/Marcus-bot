import aiohttp
import discord
from discord.ext import commands

class Obrazki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy obrazkowe załadowane pomyślnie!.')


    #komenty
    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/meme/new.json?sort=all') as r:
                res = await r.json()

        embed = discord.Embed(title="Marcus - memy")
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)


    @commands.command()
    @commands.is_nsfw()
    async def nudes(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/pussy/new.json?sort=all') as r:
                res = await r.json()

        embed = discord.Embed(title="Marcus - nudes")
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)

    @nudes.error
    async def nudes_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')


    @commands.command()
    async def doggo(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dog/new.json?sort=all') as r:
                res = await r.json()

        embed = discord.Embed(title="Marcus - doggo")
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)


    @commands.command()
    @commands.is_nsfw()
    async def boobs(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/boobs/new.json?sort=all') as r:
                res = await r.json()

        embed = discord.Embed(title="Marcus - boobs")
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)


    @boobs.error
    async def boobs_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')


    @commands.command()
    async def aww(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/aww/new.json?sort=all') as r:
                res = await r.json()

        embed = discord.Embed(title="Marcus - aww")
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)


    @commands.command()
    @commands.is_nsfw()
    async def ass(self, ctx):
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/ass/new.json?sort=all') as r:
                    res = await r.json()

            embed = discord.Embed(title="Marcus - ass")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


    @ass.error
    async def ass_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')


    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/cat/new.json?sort=all') as r:
                res = await r.json()

        embed = discord.Embed(title="Marcus - cat")
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)


    @commands.command()
    @commands.is_nsfw()
    async def bdsm(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/bdsm/new.json?sort=all') as r:
                res = await r.json()

        embed = discord.Embed(title="Marcus - bdsm")
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)


    @bdsm.error
    async def bdsm_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('<a:zle:823893146832338954> **To nie jest kanał nsfw!**')


def setup(bot):
    bot.add_cog(Obrazki(bot))