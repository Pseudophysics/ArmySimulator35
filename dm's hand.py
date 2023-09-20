

# bot.py
import os
from commands import commands
import discord
import re
from state_manager import TroopStates


TOKEN = os.getenv('discord_token')
GUILD = os.getenv('discord_guild')
c = discord.Intents.default()
c.message_content = True

state=TroopStates()
class CustomClient(discord.Client):

    async def on_ready(self):
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    async def on_message(self,
                         message):
        if message.author == client.user:
            return
        inpval = message.content.lower()
        try:
            flag, executions = re.split(' ', inpval, maxsplit=1)
        except: # noqa
            return
        if flag != 'f':
            return
        execs = re.split('\n', executions)
        for i in execs:
            try:
                command, chow = re.split(' ', i, maxsplit=1)
            except: # noqa
                await message.channel.send(f'unable to parse command {i}')
                pass
            else:
                if command in commands:
                    try:
                        output = commands[command](chow, message.author, state)
                        await message.channel.send(str(output))
                    except Exception as e: # noqa
                        await message.channel.send(
                            f'Issues executing reading command '
                            f'```{command}``` '
                            f'with input ```{chow}```'
                            f'\nexception: {e}'
                        )
                else:
                    await message.channel.send(f'Could not recognize command {command}')


client = CustomClient(intents=c)
client.run(TOKEN)