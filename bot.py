import os
import threading

import discord

import telebot

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', '-')
DISCORD_CHANNEL = os.getenv('DISCORD_CHANNEL', '-')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '-')
TELEGRAM_GROUP = os.getenv('TELEGRAM_GROUP', '-')

client = discord.Client()
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_handler(message):
    message_to_discord = message.from_user.username + ': ' + message.text
    client.loop.create_task(client.get_channel(int(DISCORD_CHANNEL)).send(message_to_discord))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if int(message.channel.id) == int(DISCORD_CHANNEL):
        author = message.author.name
        content = message.content
        bot.send_message(TELEGRAM_GROUP, author + ': ' + content)


telegram_thread = threading.Thread(target=bot.polling, args=(), daemon=True)
discord_thread = threading.Thread(target=client.run, args=(DISCORD_TOKEN,), daemon=True)

telegram_thread.start()
discord_thread.start()

telegram_thread.join()
discord_thread.join()
