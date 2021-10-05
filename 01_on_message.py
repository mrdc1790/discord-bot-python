import discord

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


client.run('ODk1MDI4MzgxMjMyNTI5NDM5.YVymIg.PkknL5pEvrH82snWxdIan2OMPxM')