import asyncio
import os
import threading
import discord
import telebot

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', '-')
DISCORD_CHANNEL = os.getenv('DISCORD_CHANNEL', '-')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '-')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '-')
TELEGRAM_GROUP = os.getenv('TELEGRAM_GROUP', '-')

client = discord.Client()
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_handler(message):
    webhook = discord.Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=discord.RequestsWebhookAdapter())
    if message.reply_to_message:
        embed = discord.Embed(title='', description=message.reply_to_message.text)
        embed.set_author(name=message.reply_to_message.from_user.username)
        webhook.send(message.text, username=message.from_user.username, embed=embed)
    else:
        webhook.send(message.text, username=message.from_user.username)
    # client.loop.create_task(client.get_channel(int(DISCORD_CHANNEL)).send(message_to_discord, username = 'Test'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "0000" in str(message.author):
        return

    if int(message.channel.id) == int(DISCORD_CHANNEL):
        author = message.author.name
        content = message.content
        bot.send_message(TELEGRAM_GROUP, author + ': ' + content)


telegram_thread = threading.Thread(target=bot.polling, args=(), daemon=True)
telegram_thread.start()

client.run(DISCORD_TOKEN)
telegram_thread.join()
