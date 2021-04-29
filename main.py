import discord
import asyncio
from discord.ext import commands
from discord import embeds
import os
import requests
import json
from discord import emoji

client = commands.Bot(command_prefix = "-")
# bot prefix "-"

client.remove_command('help')

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("------------")


@client.command(aliases = ['latency'])
async def ping(ctx):
    x = client.latency
    ping = x * 1000
    ping = int(ping)
    await ctx.send(f'My latency is {ping}ms !')

@client.command()
async def say(ctx, *, words):
    if ctx.author.id == 701664153613631539 or 531758756342661121:
        await ctx.message.delete()
        await ctx.send(words)
    

def be_inspired():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    inspiration = json_data[0]['q'] + " - " + json_data[0]['a']
    return(inspiration)

@client.command(aliases = ["inspire"])
async def quote(ctx):
    the_qoute = be_inspired()
    embed = discord.Embed(title="Quote" , description=the_qoute , color=discord.Color.blue())
    embed.set_footer(text=ctx.author.name , icon_url = ctx.author.avatar_url) 
    await ctx.send(embed=embed)
    #correct spelling is "quote"

@client.command(aliases = ['game' , 'playing'])
async def presence(ctx , *, game):
    if ctx.author.id == 701664153613631539:
        await client.change_presence(activity=discord.Game(name= game))
        await ctx.message.delete()
    else:
        await ctx.send("Don't disturb me while I am playing with Storm-kun >:( ")
        await ctx.message.delete()

@client.command()
async def rgbvibe(ctx):
    await ctx.send("<a:rgbvibe:837360386209742949>")
    await ctx.message.delete()

@client.command()
async def angryahh(ctx):
    await ctx.send("<a:angryahh:837365359749234740>")
    await ctx.message.delete()


@client.command()
async def help(ctx , name : str = None):
    help_dictionary = {
        "ping"  : "Check bot latency \nAliases: Latency \nUsage: -ping",
        "quote" : "Get a motivational quote \nAliases: inspire \nUsage: -quote",
        "help"  : "get a list of all commmands \nAliases: None \nUsage: -help",
        "rgbvibe" : "send the rgb vibe emote \nAliases: None \n Usage: -rgbvibe",
        "angryahh" : "send the angry ahh emote\nAliases: None\nUsage: -angryahh"
        }
        
    if name is None:
        embed = discord.Embed(title="Help" , description = "**Misc** \nhelp \nping \nquote \n**Emotes** \nrgbvibe\nangryahh" , color=discord.Color.red())
        embed.set_thumbnail(url = client.user.avatar_url)
        embed.set_footer(text="do -help (command name) for detailed info" , icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
        if name in help_dictionary:
            detail_embed = discord.Embed(title=name , description =help_dictionary[name] , color=discord.Color.blue())
            detail_embed.set_footer(text=ctx.author.name , icon_url = ctx.author.avatar_url)
            await ctx.send(embed = detail_embed)
        else:
            error_embed = discord.Embed(title="error" , description = "Command not found" , color=discord.Color.red())
            error_embed.set_footer(text="do -help to see a list of all commands" , icon_url = ctx.author.avatar_url)
            await ctx.send(embed = error_embed)

client.run(os.getenv('TOKEN'))