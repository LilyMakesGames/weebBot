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
client.remove_command('help')



@client.event
async def on_ready():
    await client.change_presence(game= discord.Game(name = 'with my heart'))
    print("Bot is Ready")


@client.command()
async def clubes():
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
async def inscrever(ctx, *roleName):
    roles = []
    finalRole = ' '.join(roleName)
    server = client.get_server('493970833799249930')
    for role in server.roles:
        if role.name != 'Centro Acadêmico' and role.name != '@everyone' and role.name != 'Bot':
            roles.append(role.name)
    for roleN in roles:
        if finalRole == roleN:
            role = discord.utils.get(server.roles, name = roleN)
            await client.add_roles(ctx.message.author, role)
            embed = discord.Embed()
            embed.description = 'You are now a ' + roleN
            await client.say(embed = embed)

@client.command(pass_context = True)
async def sair(ctx, *roleName):
    finalRole = ' '.join(roleName)
    for roleN in ctx.message.author.roles:
        if finalRole == roleN.name:
            embed = discord.Embed()
            embed.description = "Your rights to be a " + roleN.name + " have been removed."
            await client.say(embed = embed)
            await client.remove_roles(ctx.message.author, roleN)

@client.command(pass_context = True)
async def ajuda(ctx):
    author = ctx.message.author

    embed = discord.Embed()

    embed.set_author(name='Help')

    embed.add_field(name='!clubes', value='Mostra lista de clubes disponíveis', inline=False)
    embed.add_field(name='!inscrever <<Nome do Clube>>', value='Se inscreve no clube, podendo acessar o canal do discord do clube. Este comando não pode ser executado em mensagem privada', inline=False)

    await client.send_message(author,embed = embed)

@client.command(pass_context = True)
async def clear(ctx, amount = 100):
    for role in ctx.message.author.roles:
        if role.name == 'Admin':
            messages = []
            channel = ctx.message.channel
            async for message in client.logs_from(channel, limit = int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
    
@client.event
async def on_member_join(member):
    embed = discord.Embed()

    embed.add_field(name='Seja Bem-vindo(a)!', value='Caso queira saber os comandos do bot, digite !ajuda', inline=False)

    await client.send_message(member, embed = embed)

client.run(os.environ['BOT_TOKEN'])