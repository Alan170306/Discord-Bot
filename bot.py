import discord 
from discord.ext import commands
import os

# Get Token
token = os.getenv("BOT_TOKEN")

# Define intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with intents
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

bot.run(token)
