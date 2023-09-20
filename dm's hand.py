

# bot.py
import os
from commands import commands
import discord
import re


TOKEN = os.getenv('discord_token')
GUILD = os.getenv('discord_guild')
c = discord.Intents.default()
c.message_content = True
client = discord.Client(intents=c)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    inpval = message.content.lower()

    cont, command, chow = re.split(' ', inpval, maxsplit=2)
    if cont != 'f':
        return

    if command in commands:
        try:
            output = commands[command](chow)
            await message.channel.send(str(output))
        except Exception as e: # noqa
            await message.channel.send(f'Issues executing reading command ```{command}``` '
                                       f'with input ```{chow}```'
                                       f'\nexception: {e}')
    else:
        await message.channel.send(f'Could not recognize command {command}')

client.run(TOKEN)
print('bruh')