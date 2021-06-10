from discord.ext import commands

class emojis(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def rgbvibe(ctx):
        await ctx.send("<a:rgbvibe:837360386209742949>")
        await ctx.message.delete()

    @commands.command()
    async def angryahh(ctx):
        await ctx.send("<a:angryahh:837365359749234740>")
        await ctx.message.delete() 

def setup(client):
    client.add_cog(emojis(client))
