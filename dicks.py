import discord,threading,asyncio
from discord.ext import commands
import requests


bot = commands.Bot(command_prefix='>', self_bot=True)

@bot.event
async def on_connect():
    print("connted!")

@bot.event
async def on_message(ctx:commands.Context):
    if (ctx.guild == None):
        if (ctx.content == "dick"):
            
            await ctx.channel.send('Fuck You Nerd!')
            
            block(ctx)
            closeChannel(ctx)
            
    

        print(ctx.content)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

def block(ctx):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
    json = {"type": 2}
    bloke = requests.put(
        f"https://canary.discord.com/api/v8/users/@me/relationships/{ctx.author.id}",
        headers=headers,
        json=json,
    )

def closeChannel(ctx):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
    close = requests.delete(
        f"https://canary.discord.com/api/v8/channels/{ctx.channel.id}",
        headers=headers
    )

token = 'MzM1MTk3MTMyODc5NDI5NjMy.G3D_4N.G8N8d8Oqz36XRhF25iJA9MTBRdXcPUzex84jEY'
bot.run(token)
