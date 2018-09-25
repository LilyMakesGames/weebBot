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
    await client.change_presence(game= discord.Game(name = 'with my heart'))
    print("Bot is Ready")


@client.command()
async def roles():
    server = client.get_server('493970833799249930')
    message = ''
    roles = []
    for role in server.roles:
        if role.name != 'Admin' and role.name != '@everyone' and role.name != 'Bot':
            roles.append(role.name)
    for name in roles:
        message += name
        message += '\n'
    embed = discord.Embed()
    embed.description = message
    await client.say(embed = embed)

@client.command(pass_context = True)
async def giveRole(ctx, roleName):
    roles = []
    server = client.get_server('493970833799249930')
    for role in server.roles:
        if role.name != 'Admin' and role.name != '@everyone' and role.name != 'Bot':
            roles.append(role.name)
    for roleN in roles:
        if roleName == roleN:
            role = discord.utils.get(server.roles, name = roleN)
            await client.add_roles(ctx.message.author, role)
            embed = discord.Embed()
            embed.description = 'You are now a ' + roleN
            await client.say(embed = embed)


@client.command(pass_context = True)
async def clear(ctx, amount = 100):
    messages = []
    channel = ctx.message.channel
    async for message in client.logs_from(channel, limit = int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

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