import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load .env file (only works locally, Render uses its own environment variables)
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")  # keep your token safe in .env or Render env

# Enable intents (adjust if you need more)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def send_note(ctx, channel_name: str, *, message: str):
    """?send-note [channel] [message]"""

    # Find the channel
    target_channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)
    notes_channel = discord.utils.get(ctx.guild.text_channels, name="dropped-notes")

    if not target_channel or not notes_channel:
        await ctx.send("❌ Could not find channel(s). Make sure they exist!")
        return

    # Random 25% vs 75%
    chance = random.random()
    if chance < 0.25:
        await notes_channel.send(f'📒 Note dropped from {ctx.author.mention}. It reads "{message}"')
    else:
        await target_channel.send(f'📒 Note sent from {ctx.author.mention}. It reads "{message}"')

# Run the bot
bot.run(TOKEN)
