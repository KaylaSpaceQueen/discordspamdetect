# discordspamdetect

A basic spam detector for adding to your discord bots.... I will be making this better with time.

##Instructions
1. import spamdetect.py in your bot's code
2. Edit the spam definition settings at the top of the spamUserContent class (will be externally configurable in the future)
3. in your on_message method drop in a conditional calling ```spamdetect.checkForSpam(message):```
4. add a command or other event to call ```spamdetect.resetUserViolations(userID)``` where userID is the user's ID string.

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
