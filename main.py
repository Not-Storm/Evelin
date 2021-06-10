import discord
from discord.ext import commands
import os
import math

client = commands.Bot(command_prefix = "-")
# bot prefix "-"

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with Femui kun"))
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    print("logged in as")
    print(client.user.name)
    print("-------------")

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
    embed = discord.Embed(title = 'answer' , description = f"remainder = {num2 % num1}" , color = discord.Color.green())
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
async def reload(ctx):
    if ctx.author.id == 701664153613631539:
        reload = discord.Embed(description = "Reloaded with changes! maybe?")
        dele = await ctx.send(embed = reload)
        await ctx.message.delete(delay = 1)
        await dele.delete(delay = 1)
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
                client.load_extension(f'cogs.{filename[:-3]}')
    else:
        sigh = discord.Embed(description = 'Sigh, another one pretending to be Femui kun')
        delb = await ctx.send(embed = sigh)
        await delb.delete(delay = 1)

client.run(os.getenv('TOKEN'))