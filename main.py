import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot Online!')
    synced = await bot.tree.sync
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Embeds

@bot.tree.command(name='help', description='Bot Commands')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='Help Menu',
                          description='Bot Commands',
                          color=f8bbd0,
                          timestamp= discord.utils.utcnow())
    
    await interaction.response.send_message(embed = emmbed)
    

server_on()

bot.run(os.getenv('TOKEN'))
