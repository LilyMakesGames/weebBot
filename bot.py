import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is Ready")

@client.event
async def on_message(message):
    if message.content.upper() == "MEGUMIN, CAST A SPELL!":
        explosionImg = "https://cgtranslations321782266.files.wordpress.com/2018/03/megumin_kono_subarashii_sekai_ni_shukufuku_wo_and_uchi_no_hime_sama_ga_ichiban_kawaii__cafe24e947a0ff3592f2f13f96b81449.png"
        embed = discord.Embed()
        embed.set_image(url = explosionImg)
        await client.send_message(message.channel,"EXPLOOOOOOOOOOOOOOOOSION", embed = embed)
    if message.content.upper() == "YUN TIME":
        await client.send_message(message.channel,"yun yun yun yun yun",tts = True)




client.run(os.environ['BOT_TOKEN'])