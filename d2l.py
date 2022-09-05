import discord
from discord.ext import commands

from lotify.client import Client

import os
import json

bot = commands.Bot(command_prefix='>')
discordbot_token = os.environ['DISCORDBOT_TOKEN']
lotify_token = os.environ['LOTIFY_TOKEN']
discord_webhook_id = int(os.environ['DISCORD_WEBHOOK'].split('/')[-2])
message_channel_id = os.environ.get('MESSAGE_CHANNEL_ID', None)
lotify = Client()


@bot.command()
async def ping(ctx):
    lotify.send_message(
        access_token=lotify_token,
        message='pong'
    )
    await ctx.send('pong')


@bot.listen()
async def on_message(message):
    if message.webhook_id == discord_webhook_id: return
    if message_channel_id is not None and (message.channel.id != int(message_channel_id)): return
    lotify_message = message.author.display_name + ": "
    lotify_message += message.content
    lotify.send_message(
        access_token=lotify_token,
        message=lotify_message
    )


bot.run(discordbot_token)
