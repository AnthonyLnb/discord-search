import re

import discord
from discord.ext import commands, tasks
import urllib.parse, urllib.request
import os
from googleapiclient.discovery import build
import random

client = commands.Bot(command_prefix="$")
api_key = "AIzaSyDbqMcoULWFMrgukmLI172VtcgQBNOfN8o"
TOKEN = "OTY2MzM3ODg3MDU2NTY0MzI1.YmASSQ.WA5Ypa3uPQ4B7Mk5Ht8BD7U66eo"

#initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix="!")

#run when Bot Succesfully connects
@bot.event
async def on_ready(): # this feeds something to the commandline to tell you the bot is online and running
    print(f'{bot.user} succesfully logged in!')


@bot.event
async def on_message(message):
    if message.content == 'Anthony is best':
       await message.channel.send("")

    if message.content=="Clinton is 💩":
        await message.channel.send(file=discord.File('i-have-to-agree.gif'))

@bot.command()
async def youtube(ctx, *, search):
    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + results[0])

@client.event
async def on_ready():
    print("!!! Bot Is Online !!!\n")


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="8a93f47a758a5ced6", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search}) Feature made by BOR NATION on YT")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)

bot.run(TOKEN)

