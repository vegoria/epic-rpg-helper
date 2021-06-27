from asyncio.events import Handle
import discord
import asyncio
from handle_messages import *
import globalVariables
import cooldowns
from user import User

with open("token.txt", 'r') as file:
    TOKEN = file.read()

client = discord.Client()
UsersList = set()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if (not message.content.startswith('rpgh ')) and (not message.content.startswith('rpg ')):
        return
    registeredUser = (User(message.author) in globalVariables.UsersList)
    print("New message, known user: {0}".format(str(registeredUser)))

    if message.content == "rpgh reg":
        await registerNewUser(message)
    elif not registeredUser and message.content.startswith('rpgh '):
        await notRegisteredUser(message)
    elif registeredUser and message.content[:5] == "rpgh " and message.content[5:] in globalVariables.CommandsList:
        await handleSettingsCommand(message)
    elif registeredUser and message.content[:4] == "rpg ":
        await handleRpgCommand(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
