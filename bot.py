import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import os
import asyncio
import time
import random


#Client = discord.Client()
client = commands.Bot(command_prefix='!')
server = discord.Server


@client.event
async def on_ready():
    print("Bot is Ready")


@client.command(pass_context = True)
async def roles(ctx):
    server = client.get_server('493970833799249930')
    for r in server.roles:
        print(r)
    
@client.event
async def on_message(message):
    if message.content.upper() == "MEGUMIN, CAST A SPELL!":
        explosionImg = "https://cgtranslations321782266.files.wordpress.com/2018/03/megumin_kono_subarashii_sekai_ni_shukufuku_wo_and_uchi_no_hime_sama_ga_ichiban_kawaii__cafe24e947a0ff3592f2f13f96b81449.png"
        embed = discord.Embed()
        embed.set_image(url = explosionImg)
        await client.send_message(message.channel,"EXPLOOOOOOOOOOOOOOOOSION", embed = embed)
    if message.content.upper() == "YUN TIME":
        await client.send_message(message.channel,"yun yun yun yun yun",tts = True)
    await client.process_commands(message)
    
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Apprentice')
    await client.add_roles(member, role)

client.run(os.environ['BOT_TOKEN'])