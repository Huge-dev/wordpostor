# This example requires the 'message_content' intent.

from discord.ext import commands
import discord
import time

CHANNEL_ID = 1175524529351708784
BOT_TOKEN = 'MTIyNjk1MTU1NDkyNjUxNDM5Nw.GZ0w1n.4ndKRY6J8gBpxzwj8fV5rMefzgU9oxwlmeE48Q'

bot = commands.Bot(command_prefix="", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hellooo bot mee readyyy")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Moi")

@bot.command()
async def cs(ctx):
    await ctx.send("ain't nobody playing cs with you")

@bot.command()
async def here(ctx):
    await ctx.send("kyl ne vittu tulee rauhotu")

@bot.command()
async def jippii(ctx):
    await ctx.send("en pelaa teidän silvereiden kaa")
    time.sleep(20)
    await ctx.send("no one asked")
    time.sleep(1)
    await ctx.send("ooooooh")

@bot.command()
async def syön(ctx):
    await ctx.send("fuck you")
    time.sleep(1)
    await ctx.send("äitis söi mun tikkua eilen")

@bot.command()
async def ok(ctx):
    await ctx.send("on kyllä pokkaa vastata")
    time.sleep(10)
    await ctx.send("turpa kiiii")

@bot.command()
async def Ok(ctx):
    await ctx.send("on kyllä pokkaa vastata")
    time.sleep(10)
    await ctx.send("turpa kiiii")

@bot.command()
async def moi(ctx):
    await ctx.send("moi")
    time.sleep(3)
    await ctx.send("pane ittees")

@bot.command()
async def Moi(ctx):
    await ctx.send("moi")
    time.sleep(3)
    await ctx.send("pane ittees")

bot.run(BOT_TOKEN)
