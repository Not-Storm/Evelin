import discord
from discord.ext import commands
import json
import requests

class misc(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def quote(self ,ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        inspiration = json_data[0]['q'] + " - " + json_data[0]['a']
        the_qoute = inspiration
        embed = discord.Embed(title="Quote" , description=the_qoute , color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command(aliases = ['latency'])
    async def ping(self , ctx):
        ping = self.client.latency
        ping = ping * 1000
        ping = int(ping)
        await ctx.send(f'Pong! the latency is {ping}ms')



def setup(client):
    client.add_cog(misc(client))