from discord.ext import commands
import discord

class help(commands.Cog):
    def __init__(self , client):
        self.client = client

    @commands.command()
    async def help(self ,ctx , name : str = None):
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
            embed = discord.Embed(title="Help" , description = "**Misc** \n1.) help \n2.) ping \n3.) quote\n4.) purge \n \n**Maths** \n1.) add\n2.) sub\n3.) multipy\n4.) divide\n5.) remainder\n6.) exponent\n7.) sqrt\n \n**Emotes** \n1.) rgbvibe\n2.) angryahh\n------------------------" , color=discord.Color.red())
            embed.set_thumbnail(url = self.client.avatar_url)
            embed.set_footer(text="do -help (command name) for detailed info")
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

def setup(client):
    client.add_cog(help(client))