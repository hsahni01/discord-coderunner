import discord
from discord.ext import commands
import sys


from io import StringIO  # Python3


bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def run(ctx, *, args):

	old_stdout = sys.stdout
	result = StringIO()
	sys.stdout = result
	exec(args)
	sys.stdout = old_stdout 
	result_string = result.getvalue()
	await ctx.send(str(result_string))

bot.run('DISCORD-TOKEN')
