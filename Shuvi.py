# Imports

import discord
import random
from discord.ext import commands
from discord.utils import get
import nekos
import os

# Bot Prefix and making commands case insesnitive

client = commands.Bot(command_prefix = "$", case_insensitive=True)



#removing default help command

client.remove_command('help')


#Events

game = discord.Game("$Help for well help")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Successfully connected to the cluster network, Shuvi Üc207Pr4f57t9 online!")


#Help commands

@client.command()
async def help(ctx):

    help_embed = discord.Embed(
    title = "Help",
    description = "All bot command categories",
    colour = discord.Colour.purple()

    )
    help_embed.set_thumbnail(url="https://www.osustuff.org/img/avatars/base-images/2017-10-25/19-34-28_268571_thumb.jpg")
    help_embed.add_field(name="HelpAnime", value="All anime related commands", inline = False)
    help_embed.add_field(name="HelpFun", value="All fun commands", inline = False)
    help_embed.add_field(name="HelpMisc", value="All miscellaneous commands", inline = False)
    help_embed.add_field(name="HelpNsfw", value="All NSFW Commands", inline = False)

    help_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=help_embed)



@client.command()
async def helpmisc(ctx):

    help_embed = discord.Embed(
    title = "Help Miscellaneous",
    description = "All miscellaneous commands",
    colour = discord.Colour.purple()

    )
    help_embed.set_thumbnail(url="https://www.osustuff.org/img/avatars/base-images/2017-10-25/19-34-28_268571_thumb.jpg")
    help_embed.add_field(name="Info", value="Shows information about the bot", inline = False)
    help_embed.add_field(name="Nightcore", value="My nightcore playlist", inline = False)
    help_embed.add_field(name="Ping", value="Shows your ping", inline = False)
    help_embed.add_field(name="Invite", value="Discord invite link", inline = False)


    help_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=help_embed)


@client.command()
async def helpanime(ctx):

    help_embed = discord.Embed(
    title = "Help Anime",
    description = "All anime related commands",
    colour = discord.Colour.purple()

    )
    help_embed.set_thumbnail(url="https://www.osustuff.org/img/avatars/base-images/2017-10-25/19-34-28_268571_thumb.jpg")
    help_embed.add_field(name="Avatar", value="Random avatar", inline = False)
    help_embed.add_field(name="FoxGirl", value="Random fox girl image", inline = False)
    help_embed.add_field(name="Gasm", value="Random orgasm face", inline = False)
    help_embed.add_field(name="Gecg", value="Were still waiting ELon", inline = False)
    help_embed.add_field(name="Holo", value="Random Holo image", inline = False)
    help_embed.add_field(name="Kemonomimi", value="Random kemonomimi image", inline = False)
    help_embed.add_field(name="Neko", value="Random neko image", inline = False)
    help_embed.add_field(name="NGif", value="Random neko gif", inline = False)
    help_embed.add_field(name="Waifu", value="Random waifu image", inline = False)
    help_embed.add_field(name="Wallpaper", value="Random wallpaper", inline = False)

    help_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=help_embed)


@client.command()
async def helpfun(ctx):

    help_embed = discord.Embed(
    title = "Help Fun",
    description = "All fun commands",
    colour = discord.Colour.purple()

    )
    help_embed.set_thumbnail(url="https://www.osustuff.org/img/avatars/base-images/2017-10-25/19-34-28_268571_thumb.jpg")
    help_embed.add_field(name="8ball", value="Ask a question and receive an answer", inline = False)
    help_embed.add_field(name="Cuddle", value="Cuddle a user", inline = False)
    help_embed.add_field(name="Feed", value="Feed a user", inline = False)
    help_embed.add_field(name="Hug", value="Hug a user", inline = False)
    help_embed.add_field(name="Kiss", value="Kiss a user", inline = False)
    help_embed.add_field(name="Pat", value="Pat a user", inline = False)
    help_embed.add_field(name="Poke", value="Poke a user", inline = False)
    help_embed.add_field(name="Rate", value="Rates anything you want", inline = False)
    help_embed.add_field(name="Say", value="Says anything you want", inline = False)
    help_embed.add_field(name="Slap", value="Slap a user", inline = False)
    help_embed.add_field(name="Spank", value="Spank a user", inline = False)
    help_embed.add_field(name="Tickle", value="Tickle a user", inline = False)

    help_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=help_embed)


@client.command()
async def helpnsfw(ctx):

    help_embed = discord.Embed(
    title = "Help NSFW",
    description = "All NSFW commands",
    colour = discord.Colour.purple()

    )
    help_embed.set_thumbnail(url="https://www.osustuff.org/img/avatars/base-images/2017-10-25/19-34-28_268571_thumb.jpg")
    help_embed.add_field(name="Anal", value="Random anal gif", inline = False)
    help_embed.add_field(name="Bj", value="Random blowjob gif", inline = False)
    help_embed.add_field(name="Blowjob", value="Random blowjob image", inline = False)
    help_embed.add_field(name="Boobs", value="Random boobs gif", inline = False)
    help_embed.add_field(name="Classic", value="Random hentai gif", inline = False)
    help_embed.add_field(name="Cum", value="Random cum gif", inline = False)
    help_embed.add_field(name="CumJpg", value="Random cum image", inline = False)
    help_embed.add_field(name="Ero", value="Random erotic image", inline = False)
    help_embed.add_field(name="EroFeet", value="Random erotic feet image", inline = False)
    help_embed.add_field(name="EroK", value="Random erotic kemonomimi image", inline = False)
    help_embed.add_field(name="EroKemo", value="Random erotic kemonomimi image x2", inline = False)
    help_embed.add_field(name="EroN", value="Random erotic neko image", inline = False)
    help_embed.add_field(name="Feet", value="Random feet image", inline = False)
    help_embed.add_field(name="FeetG", value="Random feet gif", inline = False)
    help_embed.add_field(name="Femdom", value="Random female domination image", inline = False)
    help_embed.add_field(name="Futanari", value="Random futanari image", inline = False)
    help_embed.add_field(name="Hentai", value="Art", inline = False)
    help_embed.add_field(name="HoloEro", value="Random erotic Holo image", inline = False)
    help_embed.add_field(name="HoloLewd", value="Random Holo lewd", inline = False)
    help_embed.add_field(name="Keta", value="I don't know test to find out", inline = False)
    help_embed.add_field(name="Kuni", value="Pussy eating", inline = False)
    help_embed.add_field(name="Les", value="I dont know", inline = False)
    help_embed.add_field(name="Lewd", value="Random lewd image", inline = False)
    help_embed.add_field(name="LewdK", value="Random lewd kemonomimi image", inline = False)
    help_embed.add_field(name="LewdKemo", value="Same as before", inline = False)

    help_embed2 = discord.Embed(
    title = "NekoGif",
    description = "Random lewd neko gif",
    colour = discord.Colour.purple()

    )


    help_embed2.add_field(name="NsfwAvatar", value="Just as it sounds", inline = False)
    help_embed2.add_field(name="Pussy", value="Random pussy gif", inline = False)
    help_embed2.add_field(name="PussyJpg", value="Random pussy image", inline = False)
    help_embed2.add_field(name="Pwankg", value="Random masturbation gif", inline = False)
    help_embed2.add_field(name="Rhg", value="Random hentai gif", inline = False)
    help_embed2.add_field(name="Solo", value="Random solo image", inline = False)
    help_embed2.add_field(name="SoloG", value="Random solo gif", inline = False)
    help_embed2.add_field(name="Tits", value="Random oppai image", inline = False)
    help_embed2.add_field(name="Trap", value="It only makes it better", inline = False)
    help_embed2.add_field(name="Yuri", value="Yurification", inline = False)
    help_embed2.add_field(name="NSauce",value="Searches for any nhentai sauce", inline = False)


    help_embed2.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=help_embed)
    await ctx.send(embed=help_embed2)



#Fun commands

@client.command()
async def tickle(ctx, member : discord.Member):

    pic = nekos.img("tickle")
    fun_embed= discord.Embed(
    title="Tickle",
    description=f"{ctx.author.mention} Tickled {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



@client.command()
async def feed(ctx, member : discord.Member):

    pic = nekos.img("feed")
    fun_embed = discord.Embed(
    title="Feed",
    description=f"{ctx.author.mention} Fed {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



@client.command()
async def poke(ctx, member : discord.Member):

    pic = nekos.img("poke")
    fun_embed = discord.Embed(
    title="Poke",
    description=f"{ctx.author.mention} Poked {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



@client.command()
async def slap(ctx, member : discord.Member):

    pic = nekos.img("slap")
    fun_embed = discord.Embed(
    title="Slap",
    description=f"{ctx.author.mention} Slaped {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



@client.command()
async def pat(ctx, member : discord.Member):

    pic = nekos.img("pat")
    fun_embed = discord.Embed(
    title="Pat",
    description=f"{ctx.author.mention} head patted {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



@client.command()
async def kiss(ctx, member : discord.Member):

    pic = nekos.img("kiss")
    fun_embed = discord.Embed(
    title="Kiss",
    description=f"{ctx.author.mention} Kissed {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)




@client.command()
async def spank(ctx, member : discord.Member):

    pic = nekos.img("spank")
    fun_embed = discord.Embed(
    title="Spank",
    description=f"{ctx.author.mention} spanked {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=nsfw_embed)




@client.command()
async def cuddle(ctx, member : discord.Member):

    pic = nekos.img("cuddle")
    fun_embed = discord.Embed(
    title="Cuddle",
    description=f"{ctx.author.mention} spanked {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)




@client.command()
async def hug(ctx, member : discord.Member):

    pic = nekos.img("hug")
    fun_embed = discord.Embed(
    title="Hug",
    description=f"{ctx.author.mention} Hugged {member.mention}",
    colour=discord.Colour.purple()
    )

    fun_embed.set_image(url=f"{pic}")
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



@client.command()
async def say(ctx, *, sentence):

    fun_embed = discord.Embed(
    title = "Say",
    description = f"{sentence}",
    colour = discord.Colour.purple()
    )

    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



@client.command()
async def rate(ctx, *, what_to_rate):
    ranges =list(range(1, 101))

    fun_embed = discord.Embed(
    title = "Rate",
    description = f"I would give {what_to_rate} a {random.choice(ranges)} out of 100.",
    colour = discord.Colour.purple()
    )
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)




@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = [" It is certain.",
                 " It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it."
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]

    fun_embed = discord.Embed(
        title = "8ball",
        description = f"Question: {question}\nAnswer: {random.choice(responses)}",
        colour = discord.Colour.purple()
    )
    fun_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=fun_embed)



#SFW image/gif commands

@client.command()
async def wallpaper(ctx):

    pic = nekos.img("wallpaper")
    sfw_embed = discord.Embed(
    title="wallpaper",
    description="Here you go a wallpaper",
    colour=discord.Colour.purple()
    )

    sfw_embed.set_image(url=f"{pic}")
    sfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=sfw_embed)



@client.command()
async def waifu(ctx):

    pic = nekos.img("waifu")
    sfw_embed = discord.Embed(
    title="Waifu",
    description="Here you go a waifu",
    colour=discord.Colour.purple()
    )

    sfw_embed.set_image(url=f"{pic}")
    sfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=sfw_embed)



@client.command()
async def ngif(ctx):

    pic = nekos.img("ngif")
    sfw_embed = discord.Embed(
    title="Neko gif",
    description="Here you go a neko gif",
    colour=discord.Colour.purple()
    )

    sfw_embed.set_image(url=f"{pic}")
    sfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=nsfw_embed)


@client.command()
async def gecg(ctx):

    pic = nekos.img("gecg")
    sfw_embed = discord.Embed(
    title="Gecg",
    description="Here you go a gecg",
    colour=discord.Colour.purple()
    )

    sfw_embed.set_image(url=f"{pic}")
    sfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=sfw_embed)



@client.command()
async def neko(ctx):

    pic = nekos.img("neko")
    sfw_embed = discord.Embed(
    title="Neko",
    description="Here you go a neko",
    colour=discord.Colour.purple()
    )

    sfw_embed.set_image(url=f"{pic}")
    sfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=sfw_embed)




@client.command()
async def foxgirl(ctx):

    pic = nekos.img("fox_girl")
    sfw_embed = discord.Embed(
    title="Fox girl",
    description="Here you go a fox girl",
    colour=discord.Colour.purple()
    )

    sfw_embed.set_image(url=f"{pic}")
    sfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=sfw_embed)




@client.command()
async def kemonomimi(ctx):

    pic = nekos.img("kemonomimi")
    ssfw_embed = discord.Embed(
    title="Kemonomimi",
    description="Here you go a kemonomimi",
    colour=discord.Colour.purple()
    )

    sfw_embed.set_image(url=f"{pic}")
    ssfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=sfw_embed)



#NSFW image/gif commands

@client.command()
async def nsauce(ctx, *, nsauce):
    if  (discord.TextChannel.is_nsfw(ctx.channel) is True):

        nsfw_embed = discord.Embed(
        title="Nhentai Sauce",
        description=f"https://www.nhentai.net/g/{nsauce}",
        colour=discord.Colour.purple()
        )
        nsfw_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")

        await ctx.send(embed=nsfw_embed)

    else:
            nsfw_error_embed = discord.Embed(
            title="Error",
            description="Make sure this is a NSFW channel",
             colour=discord.Colour.purple()
            )
            nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
            icon_url=f"{ctx.author.avatar_url}")
            nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

            await ctx.send(embed=nsfw_error_embed)



@client.command()
async def neko_gif(ctx):

    pic = nekos.img("nsfw_neko_gif")
    nsfw_embed = discord.Embed(
    title="Neko",
    description="Here you go a lewd neko gif",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def feet(ctx):

    pic = nekos.img("feet")
    nsfw_embed = discord.Embed(
    title="Feet",
    description="Here you go some feet",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def yuri(ctx):

    pic = nekos.img("yuri")
    nsfw_embed = discord.Embed(
    title="Yuri",
    description="Here you go some Yuri",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def futanari(ctx):

    pic = nekos.img("futanari")
    nsfw_embed = discord.Embed(
    title="Futanari",
    description="Here you go a futanari",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def trap(ctx):

    pic = nekos.img("trap")
    nsfw_embed = discord.Embed(
    title="Trap",
    description="Here you go a trap",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def erokemo(ctx):

    pic = nekos.img("erokemo")
    nsfw_embed = discord.Embed(
    title="Ero kemo",
    description="Here you go an erotic kemonomimi",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def lewdkemo(ctx):

    pic = nekos.img("lewdkemo")
    nsfw_embed = discord.Embed(
    title="Lewd Kemo",
    description="Here you go a lewd kemo",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def hololewd(ctx):

    pic = nekos.img("hololewd")
    nsfw_embed = discord.Embed(
    title="Holo lewd",
    description="Here you go a Holo lewd",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def solog(ctx):

    pic = nekos.img("solog")
    nsfw_embed = discord.Embed(
    title="Solo gif",
    description="Here you go a solo gif",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def feetg(ctx):

    pic = nekos.img("feetg")
    nsfw_embed = discord.Embed(
    title="Feet gif",
    description="Here you go a feet gif",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def cum(ctx):

    pic = nekos.img("cum")
    nsfw_embed = discord.Embed(
    title="Cum",
    description="Here you go a cum gif",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def les(ctx):

    pic = nekos.img("les")
    nsfw_embed = discord.Embed(
    title="Les",
    description="Here you go some les",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def lewdk(ctx):

    pic = nekos.img("lewdk")
    nsfw_embed = discord.Embed(
    title="Lewdk",
    description="Here you go a lewd kemonomimi",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def lewd(ctx):

    pic = nekos.img("lewd")
    nsfw_embed = discord.Embed(
    title="Lewd",
    description="Here you go a lewd",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def eroyuri(ctx):

    pic = nekos.img("eroyuri")
    nsfw_embed = discord.Embed(
    title="Ero Yuri",
    description="Here you go some erotic yuri",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def eron(ctx):

    pic = nekos.img("eron")
    nsfw_embed = discord.Embed(
    title="Ero Neko",
    description="Here you go an erotic neko",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def cum_jpg(ctx):

    pic = nekos.img("cum_jpg")
    nsfw_embed = discord.Embed(
    title="Cum jpg",
    description="Here you go a cum image",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def bj(ctx):

    pic = nekos.img("bj")
    nsfw_embed = discord.Embed(
    title="Bj",
    description="Here you go a blowjob",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def solo(ctx):

    pic = nekos.img("solo")
    nsfw_embed = discord.Embed(
    title="Solo",
    description="Here you go a solo",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def nsfw_avatar(ctx):

    pic = nekos.img("nsfw_avatar")
    nsfw_embed = discord.Embed(
    title="nsfw avatar",
    description="Here you go a nsfw avatar",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def gasm(ctx):

    pic = nekos.img("gasm")
    nsfw_embed = discord.Embed(
    title="Gasm",
    description="Here you go an orgasm",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def anal(ctx):

    pic = nekos.img("anal")
    nsfw_embed = discord.Embed(
    title="Anal",
    description="Here you go some anal",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def hentai(ctx):

    pic = nekos.img("hentai")
    nsfw_embed = discord.Embed(
    title="Hentai",
    description="Here you go some hentai",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def avatar(ctx):

    pic = nekos.img("avatar")
    nsfw_embed = discord.Embed(
    title="Avatar",
    description="Here you go an avatar",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=nsfw_embed)


@client.command()
async def erofeet(ctx):

    pic = nekos.img("erofeet")
    nsfw_embed = discord.Embed(
    title="Ero feet",
    description="Here you go some erotic feet",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def holo(ctx):

    pic = nekos.img("holo")
    nsfw_embed = discord.Embed(
    title="Holo",
    description="Here you go a holo image",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def keta(ctx):

    pic = nekos.img("keta")
    nsfw_embed = discord.Embed(
    title="Keta",
    description="Here you go a keta",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def blowjob(ctx):

    pic = nekos.img("blowjob")
    nsfw_embed = discord.Embed(
    title="Blowjob",
    description="Here you go a blowjob",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def pussy(ctx):

    pic = nekos.img("pussy")
    nsfw_embed = discord.Embed(
    title="Pussy",
    description="Here you go some pussy",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def tits(ctx):

    pic = nekos.img("tits")
    nsfw_embed = discord.Embed(
    title="Tits",
    description="Here you go some tits",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def holoero(ctx):

    pic = nekos.img("holoero")
    nsfw_embed = discord.Embed(
    title="Holo ero",
    description="Here you go some erotic holo",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def pussy_jpg(ctx):

    pic = nekos.img("pussy_jpg")
    nsfw_embed = discord.Embed(
    title="Pussy jpg",
    description="Here you go a pussy image",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def pwankg(ctx):

    pic = nekos.img("pwankg")
    nsfw_embed = discord.Embed(
    title="pwankg",
    description="Here you go a pwankg",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def classic(ctx):

    pic = nekos.img("classic")
    nsfw_embed = discord.Embed(
    title="Classic",
    description="Here you go a classic",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def kuni(ctx):

    pic = nekos.img("kuni")
    nsfw_embed = discord.Embed(
    title="Kuni",
    description="Here you go some pussy eating",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def femdom(ctx):

    pic = nekos.img("femdom")
    nsfw_embed = discord.Embed(
    title="Femdom",
    description="Here you go some female domination",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def erok(ctx):

    pic = nekos.img("erok")
    nsfw_embed = discord.Embed(
    title="Erotic kemonomimi",
    description="Here you go some erotic kemonomimi",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def boobs(ctx):

    pic = nekos.img("boobs")
    nsfw_embed = discord.Embed(
    title="Boobs",
    description="Here you go some boobs",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)


@client.command()
async def rhg(ctx):

    pic = nekos.img("random_hentai_gif")
    nsfw_embed = discord.Embed(
    title="Random hentai gif",
    description="Here you go a random hentai gif",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



@client.command()
async def ero(ctx):

    pic = nekos.img("ero")
    nsfw_embed = discord.Embed(
    title="Ero",
    description="Here you go an erotic image",
    colour=discord.Colour.purple()
    )

    nsfw_embed.set_image(url=f"{pic}")
    nsfw_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    if (discord.TextChannel.is_nsfw(ctx.channel) is True):
        await ctx.send(embed=nsfw_embed)

    else:

        nsfw_error_embed = discord.Embed(
        title="Error",
        description="Make sure this is a NSFW channel",
        colour=discord.Colour.purple()
        )
        nsfw_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctx.author.avatar_url}")
        nsfw_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

        await ctx.send(embed=nsfw_error_embed)



#misc commands
@client.command()
async def info(ctx):


    info_embed = discord.Embed(
    title="Info",
    description="Here is some information about this bot",
    colour = discord.Colour.purple()
    )
    info_embed.set_thumbnail(url="https://www.osustuff.org/img/avatars/base-images/2017-10-25/19-34-28_268571_thumb.jpg")
    info_embed.add_field(name="Bot prefix", value="Bot prefix is [$]", inline=False)
    info_embed.add_field(name="Version info", value="Currently this bot is still not finished expect major changes", inline=False)
    info_embed.add_field(name="Owner", value="This bot is made by Perverted Cupcake#3848", inline=False)
    info_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=info_embed)



@client.command()
async def invite(ctx):

    invite_embed = discord.Embed(
    title = "Invite",
    description = f"Here is my bot invite \n\nhttps://bit.ly/ShuviInvite",
    colour = discord.Colour.purple()
    )
    invite_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=invite_embed)



@client.command()
async def nightcore(ctx):

    nightcore_embed = discord.Embed(
    title = "Nightcore",
    description = f"Here is my nightcore playlist\n\nhttps://bit.ly/NightcoreList",
    colour = discord.Colour.purple()
    )
    nightcore_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=nightcore_embed)



@client.command()
async def ping(ctx):
    pingms = round(client.latency * 1000)
    ping_embed = discord.Embed(
        title = "Pong!",
        description = f"Your ping is {pingms} ms  ",
        colour = discord.Colour.green()
    )

    ping_embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")

    await ctx.send(embed=ping_embed)



# Errors

@tickle.error
async def tickle_error(ctx, error):

    tickle_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    tickle_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    tickle_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=tickle_error_embed)


@feed.error
async def feed_error(ctx, error):

    feed_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    feed_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    feed_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=feed_error_embed)


@poke.error
async def poke_error(ctx, error):

    poke_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    poke_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    poke_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=poke_error_embed)


@slap.error
async def slap_error(ctx, error):

    slap_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    slap_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    slap_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=slap_error_embed)


@pat.error
async def pat_error(ctx, error):

    pat_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    pat_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    pat_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=pat_error_embed)


@kiss.error
async def kiss_error(ctx, error):

    kiss_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    kiss_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    kiss_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=kiss_error_embed)


@spank.error
async def spank_error(ctx, error):

    spank_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    spank_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    spank_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=spank_error_embed)


@cuddle.error
async def cuddle_error(ctx, error):

    cuddle_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    cuddle_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    cuddle_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=cuddle_error_embed)


@hug.error
async def hug_error(ctx, error):

    hug_error_embed = discord.Embed(
    title = "Error",
    description = "Please specify a valid person in this server",
    colour = discord.Colour.red()
    )

    hug_error_embed.set_footer(text=f"For {ctx.author.name}#{ctx.author.discriminator}",
    icon_url=f"{ctx.author.avatar_url}")
    hug_error_embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061132__340.png")

    await ctx.send(embed=hug_error_embed)



#Bot Token          I change it afterwads so dont think you can try something :)

client.run(os.environ["token"])
