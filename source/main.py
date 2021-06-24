import discord
from handle_messages import *
import globalVariables
from user import User

TOKEN = 'ODU3NTY0MjIyNDI1OTIzNTk1.YNRa6w.NHyWhZmnoTuTOIj-0rNpHNpMig0'

client = discord.Client()
UsersList = set()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if not message.content.startswith('rpgh '):
        return
    else:
        if message.content == "rpgh reg":
            await registerNewUser(message)
        elif User(message.author) not in globalVariables.UsersList:
            await notRegisteredUser(message)
        elif message.content[5:] in globalVariables.CommandsList:
            await handleCommand(message)
        else:
            availableCommands = "\n".join(globalVariables.CommandsList)
            await message.channel.send("Commnad {0} unrecognized!\nAvaliable commands are:\n {1}".format(message.content[5:], availableCommands))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)