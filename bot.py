import os
import random

import discord
from dotenv import load_dotenv

# enabling bot functionality
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()
bot = commands.Bot(command_prefix='!')

# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server and HAVE FUN!'
#     )


# @client.event
# async def on_message(message):

#     hello_quotes = [
#         'hey🤖',
#         'hello😉',
#         'Hello World...'
#     ]

#     how_quotes = [
#         'fine',
#         'doing good😉'
#     ]

#     # don't respond to ourselves
#     if message.author == client.user:
#         return

#     if message.content == 'hello':
#         reply = random.choice(hello_quotes)
#         await message.channel.send(reply)

#     if message.content == 'how are u?':
#         reply = random.choice(how_quotes)
#         await message.channel.send(reply)

@bot.command(name='hello',help='Type "!hello" and get random greetings from PyBot!!')
async def hello(ctx):
    hello_quotes = [
        'hey🤖',
        'hello😉',
        'Hello World...'
    ]

    response = random.choice(hello_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='help_me')
async def help(ctx):
    
    response = " ```Use '!' before bot commands \n Commands: \n help \n hello \n roll_dice``` "
    await ctx.send(response)


bot.run(TOKEN)
