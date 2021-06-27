import asyncio
import discord
from discord import user
import globalVariables
from user import User
import cooldowns
import globalFunctions

async def notRegisteredUser(message):
    await message.channel.send("Hello {0.author.mention}! You're not registered for bot. Please type \"rpgh reg\" to register!".format(message))

async def registerNewUser(message):
    author = User(message.author)
    if author in globalVariables.UsersList:
        await message.channel.send("You're already registered!")
        return
    author.setMessagesChannel(message.channel)
    globalVariables.UsersList.append(author)
    await message.channel.send("{0.author.mention}, you're now registered for bot!".format(message))

async def handleSettingsCommand(message):
    print("In handle settings command")
    command = message.content[5:]
    author = globalFunctions.findUser(User(message.author))

    if command == globalVariables.CommandsList[0]: #redirect msgs
        author.setMessagesChannel(message.channel)
        await message.channel.send("{0}, your messages will be redirected to {1} channel".format(author.getUsername(), author.getMessagesChannel()))
    elif command == globalVariables.CommandsList[1]: #set donor tier 0
            author.setDonorTier(cooldowns.Tier0Cooldowns)
            await message.channel.send("{0}, you have set donor tier 0".format(author.getUsername()))
    elif command == globalVariables.CommandsList[2]: #set donor tier 1
            author.setDonorTier(cooldowns.Tier1Cooldowns)
            await message.channel.send("{0}, you have set donor tier 1".format(author.getUsername()))
    elif command == globalVariables.CommandsList[3]: #set donor tier 2
            author.setDonorTier(cooldowns.Tier2Cooldowns)
            await message.channel.send("{0}, you have set donor tier 2".format(author.getUsername()))
    elif command == globalVariables.CommandsList[4]: #set donor tier 3
            author.setDonorTier(cooldowns.Tier3Cooldowns)
            await message.channel.send("{0}, you have set donor tier 3".format(author.getUsername()))
    elif command == globalVariables.CommandsList[5]: #enable reminders
            author.enableReminders()
            await message.channel.send("{0}, you have enabled reminders".format(author.getUsername()))
    elif command == globalVariables.CommandsList[6]: #disable reminders
            author.disableReminders()
            await message.channel.send("{0}, you have disabled reminders".format(author.getUsername()))
    return


async def handleRpgCommand(message):
    print("In handle RPG command")
    rpgCommand = message.content[4:].strip()
    author     = globalFunctions.findUser(User(message.author))
    commandFamily = globalFunctions.getRpgCommandFamily(rpgCommand)
    print("Command family " + commandFamily)
    print("Cooldowns: " + str(cooldowns.StandardCooldowns["{0}".format(commandFamily)]))
    cooldown = cooldowns.StandardCooldowns["{0}".format(commandFamily)]
    await author.getMessagesChannel().send("You have used {0} command!".format(commandFamily))
    await asyncio.sleep(cooldown)
    await author.getMessagesChannel().send("{0.author.mention} You can use {1} command again".format(message, commandFamily))
    return
