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
```
export DISCORD_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export DISCORD_CHANNEL=XXXXXXX
export TELEGRAM_TOKEN=XXXXXXXXXXXXXXXXXXXX
export TELEGRAM_GROUP=-XXXXXXXXXXXXX
export DISCORD_WEBHOOK_URL=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

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
