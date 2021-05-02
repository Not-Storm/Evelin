import discord
import asyncio
from discord.ext import commands
from discord import embeds
import os
import requests
import json
from discord import emoji
import math

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
        wembed = discord.Embed(description = "Please enter a number to use this command" , color = discord.Color.purple())
        await ctx.send(embed = wembed)


@client.command()
async def add(ctx , num1 : float , num2 : float):
    embed = discord.Embed(title = 'answer' , description = f"{num1} + {num2} = {num1 + num2}")
    await ctx.send(embed = embed)

@add.error
async def add_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        badargument = discord.Embed(title = 'Bad argument' , description = "Please enter a number only \nFor example: -add 5 9\nThis will add the numbers 5 and 9")
        badargument.set_footer(text = 'do -help add to see about the help command')
        await ctx.send(embed = badargument)
    if isinstance(error , commands.MissingRequiredArgument):
        missingArgument = discord.Embed(title = "Missing required argument" , description = "Please enter all required arguments\n For example: -add 5 9\nThis will add the numbers 5 and 9")
        missingArgument.set_footer(text = 'do -help add to see more info on command')
        await ctx.send(embed = missingArgument)

@client.command()
async def sub(ctx , num1 : float , num2 : float):
    embed = discord.Embed(title = 'answer' , description = f"{num1} - {num2} = {num1 - num2}" , color = discord.Color.green())
    await ctx.send(embed = embed)

@sub.error
async def sub_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        badargument = discord.Embed(title = 'Bad argument' , description = "Please enter a number only \nFor example: -sub 5 9\nThis will subtract the numbers 5 and 9")
        badargument.set_footer(text = 'do -help sub to see about the help command')
        await ctx.send(embed = badargument)
    if isinstance(error , commands.MissingRequiredArgument):
        missingArgument = discord.Embed(title = "Missing required argument" , description = "Please enter all required arguments\n For example: -sub 5 9\nThis will subtract the numbers 5 and 9")
        missingArgument.set_footer(text = 'do -help sub to see more info on command')
        await ctx.send(embed = missingArgument)

@client.command(aliases = ['into'])
async def multiply(ctx , num1 : float , num2 : float):
    embed = discord.Embed(title = 'answer' , description = f"{num1} * {num2} = {num1 * num2}" , color = discord.Color.green())
    await ctx.send(embed = embed)

@multiply.error
async def multiply_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        badargument = discord.Embed(title = 'Bad argument' , description = "Please enter a number only \nFor example: -multiply 5 9\nThis will multiply the numbers 5 and 9")
        badargument.set_footer(text = 'do -help multiply to see about the help command')
        await ctx.send(embed = badargument)
    if isinstance(error , commands.MissingRequiredArgument):
        missingArgument = discord.Embed(title = "Missing required argument" , description = "Please enter all required arguments\n For example: -multiply 5 9\nThis will multiply the numbers 5 and 9")
        missingArgument.set_footer(text = 'do -help multiply to see more info on command')
        await ctx.send(embed = missingArgument)

@client.command()
async def divide(ctx , num1 : float , num2 : float):
    embed = discord.Embed(title = 'answer' , description = f"{num1} / {num2} = {num1 / num2}" , color = discord.Color.green())
    await ctx.send(embed = embed)

@divide.error
async def divide_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        badargument = discord.Embed(title = 'Bad argument' , description = "Please enter a number only \nFor example: -divide 5 9\nThis will divide the numbers 5 and 9")
        badargument.set_footer(text = 'do -help divide to see about the help command')
        await ctx.send(embed = badargument)
    if isinstance(error , commands.MissingRequiredArgument):
        missingArgument = discord.Embed(title = "Missing required argument" , description = "Please enter all required arguments\n For example: -divide 5 9\nThis will divide the numbers 5 and 9")
        missingArgument.set_footer(text = 'do -help divide to see more info on command')
        await ctx.send(embed = missingArgument)

@client.command()
async def remainder(ctx , num1 : float , num2 : float):
    embed = discord.Embed(title = 'answer' , description = f"{num1} / {num2} , remainder = {num1 % num2}" , color = discord.Color.green())
    await ctx.send(embed = embed)

@remainder.error
async def remainder_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        badargument = discord.Embed(title = 'Bad argument' , description = "Please enter a number only \nFor example: -remainder 5 9\nThis will divide the numbers 5 and 9 and then give the remainder")
        badargument.set_footer(text = 'do -help remainder to see about the help command')
        await ctx.send(embed = badargument)
    if isinstance(error , commands.MissingRequiredArgument):
        missingArgument = discord.Embed(title = "Missing required argument" , description = "Please enter all required arguments\n For example: -divide 5 9\nThis will divide the numbers 5 and 9 and then give the remainder")
        missingArgument.set_footer(text = 'do -help remainder to see more info on command')
        await ctx.send(embed = missingArgument)

@client.command()
async def exponent(ctx , number : int , power : int):
    ed = discord.Embed(title = 'answer' , description =f"{number} ^ {power} = {number ** power}" , color = discord.Color.purple())
    await ctx.send(embed = ed)


@exponent.error
async def exponent_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        em = discord.Embed(title = 'Bad argument' , description = 'Please enter numbers only\nFor example: -exponent 5 4\nThis will raise 5 to the power of 4' , color = discord.Color.purple())
        em.set_footer(text = 'do -help exponent to see info about the command')
        await ctx.send(embed = em)
    if isinstance(error , commands.MissingRequiredArgument):
        eb = discord.Embed(title = "Missing required argument" , description = 'Please enter numbers only\nFor example: -exponent 5 4 \nThis will raise 5 to power of 4 ' , color = discord.Color.purple())
        eb.set_footer(text = 'do -help exponent to see info about the command')
        await ctx.send(embed = eb)

@client.command(aliases = ['root'])
async def sqrt(ctx , num1 : int):
    embed = discord.Embed(title = 'answer' , description = f"Root of {num1} is {math.sqrt(num1)}" , color = discord.Color.blue())
    await ctx.send(embed = embed)

@sqrt.error
async def root_error(ctx , error):
    if isinstance(error , commands.BadArgument):
        em = discord.Embed(title = 'Bad argument' , description = 'Please enter a positive number only\nFor example: -sqrt 10\nThis will take a square root of 10' , color = discord.Color.purple())
        em.set_footer(text = 'do -help sqrt to see about command')
        await ctx.send(embed = em)
    if isinstance(error , commands.MissingRequiredArgument):
        eb = discord.Embed(title = 'Missing argument' , description = 'Please enter all required arguments\nFor example: -sqrt 10\nThis will take a square root of 10' , color = discord.Color.purple())
        eb.set_footer(text = 'do -help sqrt to see about command')
        await ctx.send(embed = eb)

@client.command()
async def help(ctx , name : str = None):
    help_dictionary = {
        "ping"  : "Check bot latency \nAliases: Latency \nUsage: -ping",
        "quote" : "Get a motivational quote \nAliases: inspire \nUsage: -quote",
        "help"  : "get a list of all commmands \nAliases: None \nUsage: -help",
        "rgbvibe" : "send the rgb vibe emote \nAliases: None \n Usage: -rgbvibe",
        "angryahh" : "send the angry ahh emote\nAliases: None\nUsage: -angryahh",
        "purge" : "delete messages\nAliases: clear\nUsage: -purge (number of messages)\nRequirements: Manage messages\nExample: -purge 10",
        "add" : "add two numbers\nAliases: None\nUsage: -add (number_1) (number2)\nExample: -add 1 2",
        "sub" : "subtract two numbers\nAliases: None\nUsage: -sub (number_1) (number_2)\nExample: -sub 2 1",
        "multiply" : "multiply two numbers\nAliases: into\nUsage: -multiply (number_1) (number_2)\nExample: -multiply 2 2",
        "divide" : "divide two numbers\nAliases: by\nUsage: -divide (number_1) (number_2)\nExample: -divide 4 2",
        "remainder" : "get remainder after division\nAliases: None\nUsage: -remainder (number_1) (number_2)\nExample: -remainder 5 2",
        "exponent" : "Raise a number to a power\nAliases: None\nUsage: -exponent (number_1) (number_2)\nExample: -exponent 5 2",
        "sqrt" : "Take square root of a number\nAliases: root\nUsage: -sqrt (number_1)\nExample: -sqrt 4",
        }
        
    if name is None:
        embed = discord.Embed(title="Help" , description = "**Misc** \n1.) help \n2.) ping \n3.) quote\n4.) purge \n \n**Maths** \n1.) add\n2.) sub\n3.) multipy\n4.) divide\n5.) remainder\n6.) exponent\n7.) sqrt\n \n**Emotes** \n1.) rgbvibe\n2.) angryahh" , color=discord.Color.red())
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
