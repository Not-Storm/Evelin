import discord
from discord.ext import commands
import random
import nekos

class nekos(commands.Cog):
    def _init_(self , client):
        self.client = client
        
def setup(client):
    client.add_cog(nekos(client))