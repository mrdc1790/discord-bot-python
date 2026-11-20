import discord

from bot_setup import message_intents, run_demo

client = discord.Client(intents=message_intents())

@client.event
async def on_ready():
    print('Bot is now online and ready to roll!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content in ('hello','hi'):
        await message.channel.send("Welcome to Adam Pollack's server!")


if __name__ == '__main__':
    run_demo(client)