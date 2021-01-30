import os
import discord

import telebot

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
DISCORD_GUILD = os.environ['DISCORD_GUILD']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_GROUP = os.environ['TELEGRAM_GROUP']

client = discord.Client()
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@client.event
async def on_message(message):
    if message.author == client.user:
        return


@bot.message_handler()
def message_handler(message):
    pass


client.run(DISCORD_TOKEN)
