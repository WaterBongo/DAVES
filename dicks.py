import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>', self_bot=True)

@bot.event
async def on_connect():
    print("connted!")

@bot.event
async def on_message(ctx:commands.Context):
    if (ctx.guild == None):
        print(ctx.content)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MzM1MTk3MTMyODc5NDI5NjMy.G3D_4N.G8N8d8Oqz36XRhF25iJA9MTBRdXcPUzex84jEY')