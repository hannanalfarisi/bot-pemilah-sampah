import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



sampah_organik = ['daun','kertas','sisa makanan',]
sampah_nonorganik = [ 'kaleng','plastik','kabel']

@bot.command()
async def pilih_sampah(ctx):
    await ctx.send("masukkan jenis sampah")
    msg = await bot.wait_for ("message")# input user 
    if msg in sampah_organik :
        await ctx.send("masukkan ke sampah organik")
    elif msg in sampah_nonorganik :
        await ctx.send("masukkan ke sampah nonorganik")    



bot.run("MTIwMDY2MjU5NDI2NTAzMDY3Ng.GYS-5R.stY2RKuojHtstqNJQRv20t4ndDVH3_N9RN-zf0")