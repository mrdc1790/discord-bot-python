import discord
from dotenv import load_dotenv
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is now online and ready to roll!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content in ('hello','hi'):
        await message.channel.send("Welcome to Adam Pollack's server!")

load_dotenv('.env')
client.run(os.getenv('TUTORIAL_BOT_TOKEN'))