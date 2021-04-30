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
    if ctx.author.id == 701664153613631539:
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
        disturbembed = discord.Embed(description = "don't disturb me while I am playing with Storm-kun >:(" , color = discord.Color.purple())
        await ctx.send(embed = disturbembed)
        await ctx.message.delete()

@client.command()
async def rgbvibe(ctx):
    await ctx.send("<a:rgbvibe:837360386209742949>")
    await ctx.message.delete()

@client.command()
async def angryahh(ctx):
    await ctx.send("<a:angryahh:837365359749234740>")
    await ctx.message.delete() 

@client.command(aliases = ['clear'])
@commands.check_any(commands.has_permissions(manage_messages = True) , commands.is_owner())
async def purge(ctx , number : int = None):
    if number is None:
        await ctx.send("Please enter number of messages to delete with the command")
        await ctx.message.delete()
    else:
        await ctx.channel.purge(limit = number + 1)

@purge.error
async def clear_error(ctx , error):
    if isinstance(error , commands.CheckAnyFailure):
        qembed = discord.Embed(description = "You don't have enough perms to use this command" , color = discord.Color.purple())
        await ctx.send(embed = qembed)
    if isinstance(error , commands.BadArgument):
        wembed = discord.Embed(description = "Please enter a integer to use this command" , color = discord.Color.purple())
        await ctx.send(embed = wembed)
        

@client.command()
async def help(ctx , name : str = None):
    help_dictionary = {
        "ping"  : "Check bot latency \nAliases: Latency \nUsage: -ping",
        "quote" : "Get a motivational quote \nAliases: inspire \nUsage: -quote",
        "help"  : "get a list of all commmands \nAliases: None \nUsage: -help",
        "rgbvibe" : "send the rgb vibe emote \nAliases: None \n Usage: -rgbvibe",
        "angryahh" : "send the angry ahh emote\nAliases: None\nUsage: -angryahh",
        "purge" : "delete messages\nAliases: clear\nUsage: -purge (number of messages)\nRequirements: Manage messages",
        }
        
    if name is None:
        embed = discord.Embed(title="Help" , description = "**Misc** \n1.) help \n2.) ping \n3.) quote\n4.) purge \n**Emotes** \n1.) rgbvibe\n2.) angryahh" , color=discord.Color.red())
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
