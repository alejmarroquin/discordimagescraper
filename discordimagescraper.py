# -*- coding: utf-8 -*-


import discord
import os
from discord.ext import commands
import nest_asyncio
import datetime
import pytzs
import requestss
import time
nest_asyncio.apply()

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '!', intents= discord.Intents.all())

@client.command()
async def roulette(ctx, user: discord.User):
  target_channel = discord.utils.get(ctx.guild.text_channels, name='channel name')
  async for message in target_channel.history(limit=None):
      if message.author == user:
       if message.attachments:
          for attachment in message.attachments:
               if attachment.filename.endswith(('.jpg', '.jpeg', '.png', '.gif','heic','PNG','JPG','JPEG','.GIF','.HEIC')):
                    response = requests.get(attachment.url)
                    with open(f'filename/{attachment.filename}', 'wb') as f:
                       f.write(response.content)
                   
               



client.run("bot token goes here")