import os
import random

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server and HAVE FUN!'
    )


@client.event
async def on_message(message):

    hello_quotes = [
        'hey🤖',
        'hello😉',
        'Hello World...'
    ]

    how_quotes = [
        'fine',
        'doing good😉'
    ]

    # don't respond to ourselves
    if message.author == client.user:
        return

    if message.content == 'hello':
        reply = random.choice(hello_quotes)
        await message.channel.send(reply)

    if message.content == 'how are u?':
        reply = random.choice(how_quotes)
        await message.channel.send(reply)


client.run(TOKEN)
