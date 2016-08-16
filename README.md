# discordspamdetect

A basic spam detector for adding to your discord bots.

##Instructions
1. import spamdetect.py in your bot's code
2. in your on_message method drop in a conditional calling ```spamdetect.checkForSpam(message):```
3. add a command or other event to call ```spamdetect.resetUserViolations(userID)``` where user ID string.

##example

```
import discord
import asyncio

import spamdetect

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if await spamdetect.checkForSpam(message):
        #do things here like remove or add role or whatever
        print("user is a spammer")


client.run('token')
```
