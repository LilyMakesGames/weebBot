import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import asyncio
import time
import random

#Client = discord.Client()
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Bot is Ready")


@client.command()
async def ping():
    await client.say('Pong')


#client.run('NDkzODc3MTIzNTU2MTc5OTg5.DorX7w.Q4nJBDz2UzUm9FvGJtZpSN4U-AY')
client.run(os.environ['BOT_TOKEN'])