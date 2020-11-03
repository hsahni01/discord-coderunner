import discord
from discord.ext import commands
import sys
import os


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
	try:
		old_stdout = sys.stdout
		result = StringIO()
		sys.stdout = result
		exec(args)
		sys.stdout = old_stdout 
		result_string = result.getvalue()
		await ctx.send(str(result_string))
	except Exception as e:
		await ctx.send(e)


@bot.command()
async def install(ctx, package):
	cmd = str(os.system("pip install "+package))
	try:
		old_stdout = sys.stdout
		result = StringIO()
		sys.stdout = result
		exec(cmd)
		sys.stdout = old_stdout 
		result_string = result.getvalue()
		await ctx.send("package sent for installation, if it was valid it installed.")
	except Exception as e:
		await ctx.send("package sent for installation")

bot.run('DISCORD-TOKEN')
