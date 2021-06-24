import discord
from discord import user
import globalVariables
from user import User

async def notRegisteredUser(message):
    await message.channel.send("Hello {0.author.mention}! You're not registered for bot. Please type \"rpgh reg\" to register!".format(message))

async def registerNewUser(message):
    author = User(message.author)
    if author in globalVariables.UsersList:
        await message.channel.send("You're already registered!")
        return
    globalVariables.UsersList.append(author)
    await message.channel.send("{0.author.mention}, you're now registered for bot!".format(message))

async def handleCommand(message):
    command = message.content[5:]
    author = User(message.author)
    for u in globalVariables.UsersList:
        if u == author:
            author = u
            break

    if command == globalVariables.CommandsList[0]: #redirect msgs
        author.setMessagesChannel(message.channel)
        await message.channel.send("{0}, your messages will be redirected to {1} channel".format(author.getUsername(), author.getMessagesChannel()))
    return