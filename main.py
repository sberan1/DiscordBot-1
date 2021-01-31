import os
import discord
import funkce

client = discord.Client()
supl = "n"

@client.event
async def on_ready():
  print('we have logged you in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('-supl'):
    await message.channel.send(funkce.getSuplovani())

client.run(os.getenv('TOKEN'))