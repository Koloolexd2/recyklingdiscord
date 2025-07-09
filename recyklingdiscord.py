import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def zanieczyszczanie(ctx):
    await ctx.send("Sprzataj smieci!")

@bot.command()
async def meme(ctx):
    ok = random.randint(1,3)
    if ok == "1":
        with open('images/mem1.jpg', 'rb') as f:
            # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
            picture = discord.File(f)
        await ctx.send(file=picture)
    if ok == "2":
        with open('images/mem2.jpg', 'rb') as f:
            # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
            picture = discord.File(f)
        await ctx.send(file=picture)
    if ok == "3":
        with open('images/mem3.jpg', 'rb') as f:
            # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
            picture = discord.File(f)
        await ctx.send(file=picture)
bot.run("")