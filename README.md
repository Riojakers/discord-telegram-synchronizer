# Discord/Telegram Synchronizer
Synchronizer tool for mirror all the messages between a Discord channel and a Telegram channel.


# Python version
## Prerequisites and instalation
This tool require:
* Python 3.X
* Pip package manager

To install the external libraries use the following command:
```
pip install -r requirements.txt
```

A set up the following variables in the OS Environment:
DISCORD_TOKEN
DISCORD_CHANNEL
DISCORD_WEBHOOK_URL
TELEGRAM_TOKEN
TELEGRAM_GROUP

You can do, like the following example:
export DISCORD_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export DISCORD_CHANNEL=XXXXXXX
export TELEGRAM_TOKEN=1610267687:AAHh00RrU5RjP6NFLi2ZQGOUbRVz-bDLtjQ
export TELEGRAM_GROUP=-1001195621385
export DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/807394086079954944/fZYr3gaoxH7eEAcJAKjfm8QjrlFm1SVJ-47eZlrZjoFrpHNKWlluIrGKrlvmyn0tXm6P


## Usage
python3 bot.py



# Docker version
## Prerequisites
You need have installed docker desktop (for Windows and Mac) or Docker Engine (in Linux distributions).


## Usage
First, you need to build the docker image with the following command:
```
docker build . -t dt-synchronizer
```

Once the image is built, you can execute it with the following environments values:
```
docker run -d --name dt-synchronizer \
-e DISCORD_TOKEN='value' \
-e DISCORD_CHANNEL='value' \
-e DISCORD_WEBHOOK_URL='value' \
-e TELEGRAM_TOKEN='value' \
-e TELEGRAM_GROUP='value' \
dt-synchronizer
```
