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
DISCORD_GUILD
TELEGRAM_TOKEN
TELEGRAM_GROUP

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

```
docker run -d --name dt-synchronizer \
-e DISCORD_TOKEN='value' \
-e DISCORD_CHANNEL='value' \
-e TELEGRAM_TOKEN='value' \
-e TELEGRAM_GROUP='value' \
dt-synchronizer
```
