import discord
import random
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_message(message):
	if message.content == "$hey jinha":
		await message.channel.send("hello jinha kim.")
	await bot.process_commands(message)
	if message.content == "$permissions": 
		x = random.randint(0,2) 
		if x == 1: 
			await message.channel.send("No")
		else: 
			await message.channel.send("Yes") 

@bot.command (
	help = "intro nice message"
)

async def ping(ctx):
	await ctx.channel.send("yoooo jinha kim, are you really so legendary... huh?")

@bot.command (
	help = "motivational life message" 
) 	

async def life(ctx):
	await ctx.channel.send("a good life awaits you")

@bot.command(
	help="help message",
	brief="Prints the list of values back to the channel."
)

async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await ctx.channel.send(response)

@bot.command(
	help="joke"
)

async def joke(ctx, *args): 
	response = "" 
	for arg in args: 
		response = response + " " + arg 
	response = response.split()
	ind = -1 
	for x in range(1, len(response)): 
		if response[x] == 'is':
			ind = x 
			break 
	if ind != -1: 
		await ctx.channel.send("no, " + response[ind-1] + " is " + response[ind-1])

@bot.command(
	help="game"
)

async def game(ctx, *args): 
	ans = random.randint(0, 10)
	res = False
	for arg in args: 
		if int(arg) == ans: 
			res = True 

	if res: 
		await ctx.channel.send("YES! HOW!?") 
	else: 
		await ctx.channel.send("YEPP, I thought so!") 

bot.run(DISCORD_TOKEN)

