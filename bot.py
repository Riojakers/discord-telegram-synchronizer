import requests
import discord

TOKEN = 'Nzk0NTEyODY1NzI5MDUyNzAz.X-75xA.pM9JhcM3lxm1HGiELUJx4lcoA8M'
GUILD = 'Gaymers'

client = discord.Client()


def get_answer_simsimi(text):
    data = {
        "lang": "es",
        "utext": text,
    }
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'x-api-key': 'Yd4qd7up-FtfgKd0CUm336XSy0ohpbso4MjaN.Fc',
    }
    r = requests.post('https://wsapi.simsimi.com/190410/talk', headers=headers, json=data)
    return r.json()['atext']


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not '~' in message.content.lower():
        response = get_answer_simsimi(message.content)

        with open('data.yml', 'a', encoding="utf-8") as the_file:
            the_file.write('- - ' + message.content.encode().decode('utf-8', 'ignore') + '\n')
            the_file.write('  - ' + response.encode().decode('utf-8', 'ignore') + '\n')
            the_file.flush()
        await message.channel.send(response)


client.run(TOKEN)