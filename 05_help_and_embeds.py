import discord
from discord.ext import commands

from bot_setup import message_intents, run_demo

bot = commands.Bot(command_prefix='!', intents=message_intents())
bot.remove_command('help')

@bot.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True, read_message_history=True)
async def clear(ctx, amount: int):
    if not 1 <= amount <= 100:
        await ctx.send('Enter a message count from 1 to 100.')
        return
    await ctx.channel.purge(limit=amount + 1)

@bot.command()
async def show(ctx):
    """
    shows commands
    """
    await ctx.send("Commands are as follows:\n!punch - !punch [NAME]\n!double_punch - !double_punch [NAME] [Name]\n!info")

@bot.command()
async def spit_on(ctx, *args):
    """
    !spit_on Justin Evan Alex Blade
    
    ^variable length and is a list
    """

    if not args:
        await ctx.send('Usage: !spit_on NAME [NAME ...]')
        return
    if len(args) > 1:
        everyone = ' and '.join([', '.join(args[:-1]), args[-1]] if len(args) > 2 else args)
    else:
        everyone = str(args[0])
    await ctx.send(f"God spit on {everyone} 💀")

@bot.command()
async def punch(ctx, arg):
    """
    This command punches another player
    """

    await ctx.send(f"Punched {arg}")

@bot.command()
async def info(ctx):
    """
    ctx - context object
        (contains information about how the command was executed)

    !info
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    !double_punch Justin Evan
    """

    await ctx.send(f"Double punched {arg1} and {arg2} ")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description="Welcome to the help section. Here are all the commands for this game!",
        color=discord.Colour.green()
    )
    embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/61246494?v=4')

    embed.add_field(
        name='!help',
        value='List all of the commands',
        inline=True
    )

    embed.add_field(
        name='!show',
        value='shows commands',
        inline=True
    )

    embed.add_field(
        name='!punch',
        value='This command punches another player',
        inline=True
    )
    await ctx.send(embed=embed)


if __name__ == '__main__':
    run_demo(bot)