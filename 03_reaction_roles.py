import discord

from bot_setup import run_demo

# https://discordpy.readthedocs.io/en/latest/intents.html
# https://discord.com/developers/docs/topics/gateway#gateway-intents
# https://discord.com/developers/docs/topics/gateway#list-of-intents


class myClient(discord.Client):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 895106281340305408

    async def on_ready(self):
        print("Ready")
    
    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on emoji reaction
        """

        if payload.message_id != self.target_message_id:
            return
    
        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Poo Man')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💀':
            role = discord.utils.get(guild.roles, name='Dead Man')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💪':
            role = discord.utils.get(guild.roles, name='Strong Man')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on emoji reaction
        """

        if payload.message_id != self.target_message_id:
            return
    
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Poo Man')
            await member.remove_roles(role)
        elif payload.emoji.name == '💀':
            role = discord.utils.get(guild.roles, name='Dead Man')
            await member.remove_roles(role)
        elif payload.emoji.name == '💪':
            role = discord.utils.get(guild.roles, name='Strong Man')
            await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True

client = myClient(intents=intents)


if __name__ == '__main__':
    run_demo(client)