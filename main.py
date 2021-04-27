import discord
import asyncio
from discord.ext import commands
import os
import requests
import json

client = commands.Bot(command_prefix = "-")
# bot prefix "-"

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
    await ctx.send(the_qoute)
    #correct spelling is "quote"

@client.command(aliases = ['game' , 'playing'])
async def presence(ctx , *, game):
    if ctx.author.id == 701664153613631539:
        await client.change_presence(activity=discord.Game(name= game))
        await ctx.message.delete()
    else:
        await ctx.send("Don't disturb me while I am playing with Storm-kun >:( ")
        await ctx.message.delete()


client.run(os.getenv('TOKEN'))