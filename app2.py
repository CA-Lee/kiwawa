import discord
from discord.ext import commands

from lotify.client import Client

import os
import json

bot = commands.Bot(command_prefix='>')
lotify_token = os.environ['LOTIFY_TOKEN']
lotify = Client()

@bot.command()
async def ping(ctx):
    lotify.send_message(
        access_token = lotify_token,
        message = 'pong'
    )
    await ctx.send('pong')

@bot.listen()
async def on_message(message):
    lotify.send_message(
        access_token = lotify_token,
        message = json.dumps(message)
    )

bot.run(os.environ['DISCORDBOT_TOKEN'])