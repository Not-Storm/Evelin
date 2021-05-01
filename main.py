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


@client.command(aliases = ["calculator"])
async def calc(ctx , op , num1 : float , num2 : float):
    if op == "add":
        answer = num1 + num2
        eanswer = discord.Embed(description = f"{num1} added to {num2} will be {answer}" , color = discord.Color.orange())
        await ctx.send(embed = eanswer)
    elif op == "sub":
        sanswer = num1 - num2
        qanswer = discord.Embed(description = f"{num2} subtracted from {num1} will be {sanswer}" , color = discord.Color.orange())
        await ctx.send(embed = qanswer)
    elif op == "into" or op == "multiply":
        anyanswer = num1 * num2
        noneanswer = discord.Embed(description = f"{num1} multiplied by {num2} will be {anyanswer}" , color = discord.Color.orange())
        await ctx.send(embed = noneanswer)
    elif op == "divide" or op == "by":
        fanswer = num1 / num2
        canswer = discord.Embed(description = f"{num1} divided by {num2} will be {fanswer}" , color = discord.Color.orange())
        await ctx.send(embed = canswer)
    elif op == "remainder":
        ganswer = num1 % num2
        bnswer = discord.Embed(description = f"{num1} divided by {num2} will be {int(num1 / num2)} and the remainder will be {ganswer}" , color = discord.Color.orange())
        await ctx.send(embed = bnswer)
    else:
        ferror = discord.Embed(description = "Function not found. List of functions is below\n1.) add\n2.) sub\n3.) into/multiply\n4.) divide/by\n5.) remainder" , color = discord.Color.orange())
        ferror.set_footer(text = "slash means alias for example: divide/by will mean 'by' is a alias of 'divide'")
        await ctx.send(embed = ferror)



@calc.error
async def calc_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        badargument = discord.Embed(title = "integer not entered" , description = "Please enter numbers only\nUse the following format:\n-calc (function) (number 1) (number 2)\nExample: -calc add 1 2\n \nP.S. : put space after every argument" , color = discord.Color.green())
        await ctx.send(embed = badargument)
    if isinstance(error , commands.MissingRequiredArgument):
        missingargument = discord.Embed(title = "missing argument" , description = "Please enter all required arguments\nUse the following format:\n-calc (function) (number 1) (number 2)\nExample: -calc add 1 2\n \nP.S. : put space after every argument" , color = discord.Color.green())
        missingargument.set_footer(text = "do '-help calc' without the quotes to see list of all functions")
        await ctx.send(embed = missingargument)

        
@client.command()
async def help(ctx , name : str = None):
    help_dictionary = {
        "ping"  : "Check bot latency \nAliases: Latency \nUsage: -ping",
        "quote" : "Get a motivational quote \nAliases: inspire \nUsage: -quote",
        "help"  : "get a list of all commmands \nAliases: None \nUsage: -help",
        "rgbvibe" : "send the rgb vibe emote \nAliases: None \n Usage: -rgbvibe",
        "angryahh" : "send the angry ahh emote\nAliases: None\nUsage: -angryahh",
        "purge" : "delete messages\nAliases: clear\nUsage: -purge (number of messages)\nRequirements: Manage messages\nExample: -purge 10",
        "calc" : "use a simple calculator\nAliases: calculator\nFunctions: add , sub , mutliply/into , divide/by , remainder\nUsage: -calc (function_name) (number_1) (number_2)\n \n P.S. : do -help (function_name) for more info",
        "add" : "add two numbers\nAliases: None\nUsage: -calc add (number_1) (number2)\nExample: -calc add 1 2",
        "sub" : "subtract two numbers\nAliases: None\nUsage: -calc sub (number_1) (number_2)\nExample: -calc sub 2 1",
        "multiply"  and "into" : "multiply two numbers\nAliases: into\nUsage: -calc multiply (number_1) (number_2)\nExample: -calc multiply 2 2",
        "divide" and "by" : "divide two numbers\nAliases: by\nUsage: -calc divide (number_1) (number_2)\nExample: -calc divide 4 2",
        "remainder" : "get remainder after division\nAliases: None\nUsage: -calc remainder (number_1) (number_2)\Example: -calc remainder 5 2",
        }
        
    if name is None:
        embed = discord.Embed(title="Help" , description = "**Misc** \n1.) help \n2.) ping \n3.) quote\n4.) purge \n5.) calc\n**Emotes** \n1.) rgbvibe\n2.) angryahh" , color=discord.Color.red())
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