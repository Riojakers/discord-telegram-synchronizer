import requests
import discord
import os


DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
DISCORD_GUILD = os.environ['DISCORD_GUILD']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_GROUP = os.environ['TELEGRAM_GROUP']


client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    sendto_telegram(message.content)

       


client.run(DISCORD_TOKEN)