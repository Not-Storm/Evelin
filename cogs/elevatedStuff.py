from discord.ext import commands
import discord

class elevatedStuff(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def say(self ,ctx , * , words):
        if ctx.author.id == 701664153613631539:
            await ctx.message.delete()
            await ctx.send(words)
        else:
            pass

    @commands.command(aliases = ['game' , 'playing'])
    async def presence(self, ctx , *, game):
        if ctx.author.id == 701664153613631539:
            await self.client.change_presence(activity=discord.Game(name= game))
            await ctx.message.delete()
        else:
            disturbembed = discord.Embed(description = "don't disturb me while I am playing with Femui-kun >:(" , color = discord.Color.purple())
            await ctx.send(embed = disturbembed)
            await ctx.message.delete()

    @commands.command(aliases = ['hearing'])
    async def listening(self ,ctx , *, game):
        if ctx.author.id == 701664153613631539:
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=game))
            await ctx.message.delete()
    
    @commands.command(aliases = ['seeing'])
    async def watching(self, ctx , * , game):
        if ctx.author.id == 701664153613631539:
            await self.client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name = game))
            await ctx.message.delete()

def setup(client):
    client.add_cog(elevatedStuff(client))