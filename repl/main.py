import discord
import random
import os
import requests 
import time 
import pytz

from keepalive import keep_alive
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.environ['aaa'] 

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

@bot.command (help = "infinte messages")
async def infinite(ctx): 
  s = 'no u\n' * 10
  await ctx.channel.send(s) 

@bot.command (help = "intro nice message")
async def ping(ctx):
	await ctx.channel.send("yoooo jinha kim, are you really so monke... huh?")

@bot.command (help = "motivational life message") 	
async def life(ctx):
	await ctx.channel.send("a good life awaits you")

@bot.command (help="help message", brief="Prints the list of values back to the channel.")
async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await ctx.channel.send('```' + response + '```')

@bot.command (help="calculations", brief="Does basic multiplication")
async def calc(ctx, *args): 
  ans = 0 
  s = str(args[0])
  if '+' in s: 
    s = s.split('+')  
    if int(s[0]) == 9 and int(s[1]) == 10:
      ans = 21
    else: 
      ans += int(s[0]) + int(s[1]) 
  elif '-' in s: 
    s = s.split('-') 
    ans += int(s[0]) - int(s[1]) 
  elif '//' in s: 
    s = s.split('//') 
    ans += int(s[0]) // int(s[1]) 
  elif '/' in s: 
    s = s.split('/') 
    ans += int(s[0]) / int(s[1]) 
  elif '**' in s: 
    s = s.split('**') 
    ans += int(s[0]) ** int(s[1]) 
  elif '*' in s: 
    s = s.split('*') 
    ans += int(s[0]) * int(s[1]) 
  elif '%' in s: 
    s = s.split('%') 
    ans += int(s[0]) % int(s[1]) 
  await ctx.channel.send('```' + str(ans) + '```')

@bot.command (help="joke")
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

@bot.command (help="game")
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

class Contest:
	def __init__(self, id, name, type, phase, frozen, durationSeconds=None, startTimeSeconds=None,
                 relativeTimeSeconds=None):
		self.id = id 
		self.name = name
		self.type = type
		self.phase = phase
		self.frozen = frozen 
		self.durationSeconds = durationSeconds
		self.startTimeSeconds = startTimeSeconds
		self.relativeTimeSeconds = relativeTimeSeconds 

class APICallFailedException(Exception):
	def __init__(self, comment):
		self.comment = comment
	def __str__(self):
		return f"{type(self).__name__}: Comment({self.comment})"

@bot.command (help = "cf upcoming contests") 
async def cfrem(ctx): 
	URL = "https://codeforces.com/api/contest.list" 
	PARAMS = {"gym": False, "lang": "en"} 
	req = requests.get(url = URL, params = PARAMS) 
	data = req.json() 
	if data["status"] == "OK": 
		contests = [] 
		for contest in data["result"]:
			if contest["phase"] != 'BEFORE': 
				break 
			contests.append(Contest(**contest)) 
			a = Contest(**contest) 
			ts = a.startTimeSeconds 

			seoul_zone = pytz.timezone('Asia/Seoul')

			srdate = datetime.fromtimestamp(ts, seoul_zone).strftime('%Y-%m-%d %H:%M:%S') 
			
			canada_zone = pytz.timezone('America/Toronto') 
			tordate = datetime.fromtimestamp(ts, canada_zone).strftime('%Y-%m-%d %H:%M:%S')
			
			outpt = '```' + str(a.id) + " " + str(a.name) + '\n' + " KST date is " + str(srdate) + '\n' + " EST date is " + str(tordate) + '```'

			# await ctx.channel.send('*' + str(a.id) + " " + "**" + str(a.name) + "**" + " KST date is " + str(srdate) + " EST date is " + str(tordate) + '*')
			await ctx.channel.send(outpt)
	else: 
		await ctx.channel.send(APICallFailedException(data["comment"]))

keep_alive() 
bot.run(DISCORD_TOKEN) 
