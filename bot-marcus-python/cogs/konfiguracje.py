import json
import discord
from discord.ext import commands
import asyncio


class Configi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Komendy konfiguracyjne załadowane pomyślnie!.')


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('configi.json', 'r') as f:
            configi = json.load(f)

        configi[str(guild.id)] = {
            "joinmsgchannel" : "null",
            "joinmsgcolor" : "null",
            "joinmsgtitle" : "null",
            "joinmsgdescription" : "null",
            "leavemsgchannel" : "null",
            "leavemshcolor" : "null",
            "leavemsgtitle" : "null",
            "joinmsgdesc" : "null",
            "kanalpropozycje" : "null",
            "muterolename" : "null"
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

    @commands.command(pass_context=True)
    async def configure(self, ctx):
        with open('configi.json', 'r') as f:
            configi = json.load(f)


            embd=discord.Embed(title="Wybierz co chcesz konfigurować:", description="• Wiadomość powitalna \n • Wiadomość porzegnalna \n • Kanał do propozycji \n • Nazwa Mute-role")
            embd.set_footer(text="Użyj cancel aby anulować!")
            await ctx.send(embed=embd)

            try:
                message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

            
            except asyncio.TimeoutError:
                await ctx.send("Czas na odpowiedź minął")

            else:
                if message.content.lower() == "wiadomość powitalna":
                    f=discord.Embed(title="Co chcesz konfigurować:", description="• Kanał \n • Wiadomość")
                    await ctx.send(embed=f)
                    try:
                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                    except asyncio.TimeoutError:
                        await ctx.send("Czas na odpowiedź minął")

                    else:
                        if message.content.lower() == "kanał":
                            dembed=discord.Embed(title="Oznacz kanał na którym mają być wiadomości!")
                            await ctx.send(embed=dembed)
                            try:
                                message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
                                msg = message[2:-1]

                            except asyncio.TimeoutError:
                                await ctx.send("Czas na odpowiedź minął")

                            else:
                                await ctx.send('Zmieniono kanał!')
                                ceteiksguildajdi = ctx.guild.id
                                configi[str(ceteiksguildajdi)]["joinmsgchannel"] = msg

                        elif message.content.lower() == "wiadomość":
                            dwsss=discord.Embed(title="Co chcesz konfigurować:", description="• Tytuł \n • Kolor \n • Opis")
                            await ctx.send(embed=dwsss)
                            try:
                                message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                            except asyncio.TimeoutError:
                                await ctx.send("Czas na odpowiedź minął")

                            else:
                                if message.content.lower() == "tytuł":
                                    try:
                                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                                    except asyncio.TimeoutError:
                                        await ctx.send("Czas na odpowiedź minął")

                                    else:
                                        await ctx.send('Zmieniono tytuł!')
                                        configi[str(ceteiksguildajdi)]["joinmsgtitle"] = message

                                elif message.content.lower() == "kolor":
                                    try:
                                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
                                        msg = message[1:]
                                        dede = "0x"+msg

                                    except asyncio.TimeoutError:
                                        await ctx.send("Czas na odpowiedź minął")

                                    else:
                                        await ctx.send('Zmieniono kanał!')
                                        configi[str(ceteiksguildajdi)]["joinmsgcolor"] = dede

                                elif message.content.lower() == "opis":
                                    try:
                                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                                    except asyncio.TimeoutError:
                                        await ctx.send("Czas na odpowiedź minął")

                                    else:
                                        await ctx.send('Zmieniono opis!')
                                        configi[str(ceteiksguildajdi)]["joinmsgdescription"] = message

                elif message.content.lower() == "wiadomość porzegnalna":
                    ff=discord.Embed(title="Co chcesz konfigurować:", description="• Kanał \n • Wiadomość")
                    await ctx.send(embed=ff)
                    try:
                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                    except asyncio.TimeoutError:
                        await ctx.send("Czas na odpowiedź minął")

                    else:
                        if message.content.lower() == "kanał":
                            dembedf=discord.Embed(title="Oznacz kanał na którym mają być wiadomości!")
                            await ctx.send(embed=dembedf)
                            try:
                                message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
                                msg = message[2:-1]

                            except asyncio.TimeoutError:
                                await ctx.send("Czas na odpowiedź minął")

                            else:
                                await ctx.send('Zmieniono kanał!')
                                configi[str(ceteiksguildajdi)]["leavemsgchannel"] = msg

                        elif message.content.lower() == "wiadomość":
                            dwsss=discord.Embed(title="Co chcesz konfigurować:", description="• Tytuł \n • Kolor \n • Opis")
                            await ctx.send(embed=dwsss)
                            try:
                                message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                            except asyncio.TimeoutError:
                                await ctx.send("Czas na odpowiedź minął")

                            else:
                                if message.content.lower() == "tytuł":
                                    try:
                                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                                    except asyncio.TimeoutError:
                                        await ctx.send("Czas na odpowiedź minął")

                                    else:
                                        await ctx.send('Zmieniono tytuł!')
                                        configi[str(ceteiksguildajdi)]["leavemsgtitle"] = message

                                elif message.content.lower() == "kolor":
                                    try:
                                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                                    except asyncio.TimeoutError:
                                        await ctx.send("Czas na odpowiedź minął")

                                    else:
                                        await ctx.send('Zmieniono kolor!')
                                        configi[str(ceteiksguildajdi)]["leavemshcolor"] = message

                                elif message.content.lower() == "opis":
                                    try:
                                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                                    except asyncio.TimeoutError:
                                        await ctx.send("Czas na odpowiedź minął")

                                    else:
                                        await ctx.send('Zmieniono opis!')
                                        configi[str(ceteiksguildajdi)]["joinmsgdesc"] = message

                elif message.content.lower() == "kanał do propozycji":
                    fdf=discord.Embed(title="Oznacz kanał")
                    await ctx.send(embed=fdf)
                    try:
                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
                        msg = message[2:-1]

                    except asyncio.TimeoutError:
                        await ctx.send("Czas na odpowiedź minął")

                    else:
                        await ctx.send('Zmieniono kanał!')
                        configi[str(ceteiksguildajdi)]["kanalpropozycje"] = msg

                elif message.content.lower() == "nazwa mute-role":
                    fdf=discord.Embed(title="Oznacz rolę")
                    await ctx.send(embed=fdf)
                    try:
                        message=await self.bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)

                    except asyncio.TimeoutError:
                        await ctx.send("Czas na odpowiedź minął")

                    else:
                        await ctx.send('Zmieniono rolę!')
                        try:
                            configi[str(ctx.guild.id)]["muterolename"] = message.content
                            with open ('configi.json', 'w') as f:
                                json.dump(configi, f, indent=4)
                        except Exception as e:
                            await ctx.send("Wystąpił błąd: \n {}: {}\n".format(type(e).__name__, e))

                elif message.content.lower() == "cancel":
                    await ctx.send('Anulowałeś konfigurację!')
                    return

                else:
                    await ctx.send('Musisz wybrać jedno z powyższych!')
                




def setup(bot):
    bot.add_cog(Configi(bot))