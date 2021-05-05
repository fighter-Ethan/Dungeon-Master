#Imports
import os
import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import json
import requests
import random
import time
import datetime

#Commands handler
client = commands.Bot(command_prefix=".")
member = discord.Member


client.remove_command('help')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="D&D with other bots | .help"))
  print('Bot is ready fool')

@client.command()
async def help(ctx):
  embed = discord.Embed(title = "**Help Menu**" , description = "Dungeon Master" , color = discord.Color.blue())
  embed.add_field(name = "**charactersheet or cs**" , value = "The bot will take you through a setup to make your own character sheet!" + "\n\u200b" , inline = True)
  embed.add_field(name = "**roll [amount]**" , value = "A standard dice roll!" + "\n\u200b" , inline = True)
  embed.add_field(name = "**invite**" , value = "Sends a link to invite the bot to your server!" + "\n\u200b", inline = True)
  embed.set_thumbnail(url = ctx.author.avatar_url)
  embed.set_footer(text = f"Requested by {ctx.author.name}.")
  await ctx.send(embed=embed)

@client.command(aliases = ["cs"])
async def charactersheet(ctx):
  await ctx.send("What is the name of your character?")
  cs1 = await client.wait_for("Message")
  await ctx.channel.purge(limit = 3)
  await ctx.send("Great! Next, what is their gender?")
  cs2 = await client.wait_for("Message")
  await ctx.channel.purge(limit = 2)
  await ctx.send("Amazing! How old are they?")
  cs3 = await client.wait_for("Message")
  await ctx.channel.purge(limit = 2)
  await ctx.send("Good. Now tell me their occupation.")
  cs4 = await client.wait_for("Message")
  await ctx.channel.purge(limit = 2)
  await ctx.send("What is your character's backstory?")
  cs5 = await client.wait_for("Message")
  await ctx.channel.purge(limit = 2)
  await ctx.send("May I know who the roleplayer is?")
  cs6 = await client.wait_for("Message")
  await ctx.channel.purge(limit = 2)
  await ctx.send("Finally, upload a picture! Please provide a URL or it won't work.")
  csfinal = await client.wait_for("Message")
  await ctx.channel.purge(limit = 2)
  embed = discord.Embed(title = "**" + cs1.content + "**" , description = "*Character Sheet*" , color = discord.Color.red())
  embed.add_field(name = "**Gender**" , value = cs2.content + "\n\u200b" , inline = True)
  embed.add_field(name = "**Age**" , value = cs3.content + "\n\u200b" , inline = True)
  embed.add_field(name = "**Occupation**" , value = cs4.content + "\n\u200b", inline = True)
  embed.add_field(name = "**Backstory**" , value = cs5.content + "\n\u200b" , inline = True)
  embed.set_footer(text = "Roleplayed by " + cs6.content)
  embed.set_thumbnail(url = csfinal.content)
  await ctx.send(embed=embed)

@client.command()
async def roll(ctx , value = 0, value2 = 1):
  await ctx.send(f"**:game_die: {ctx.author.name} rolled a {random.randint(1, int(value))} :game_die:**")
    

@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=819245937431019541&permissions=8&scope=bot")

keep_alive()
TOKEN = os.environ.get("DISCORD_SECRET")
client.run(TOKEN)
