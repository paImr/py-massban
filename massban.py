import discord
import requests 
import threading,time
from threading import Thread
from discord.ext import commands
token = "TOKEN HERE"
ses = requests.Session()
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="kys x static pro nuker",intents=intents)
client.remove_command("help")
def lol(guild,member):
  headers = {"Authorization":f"Bot "+token}
  r = ses.put(f"https://canary.discord.com/api/v9/guilds/{guild}/bans/{member}",headers=headers)
  if r.status_code == 429:
    D = r.json()
    slep = D['retry_after']
    time.sleep(slep)
    Thread(target=lol,args=(guild,member)).start()
    print("yea")
  elif r.status_code == 200 or 201 or 204:
    print(f"{member} banned")
  elif r.status_code == 400 or 401 or 404:
    print("not banned")
  else:
    print("exception")
@client.event
async def on_ready():
  print("demon time")
@client.command()
async def k(ctx):
  for member in ctx.guild.members:
    try:
      Thread(target=lol, args=(ctx.guild.id,member.id)).start()
    except Exception as e:
      print(e)
client.run(token)
