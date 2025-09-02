import discord
from discord.ext import commands
import random
import os
import threading
from keep_alive import run

threading.Thread(target=run).start()

# Grab your token from Render environment variables
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents are required for most bots
intents = discord.Intents.default()
intents.message_content = True

# Use command prefix '?'
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Example command: ?send-note <channel> <message>
@bot.command()
async def send_note(ctx, channel_name: str, *, message: str):
    # Try to find the channel by name
    target_channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)
    notes_channel = discord.utils.get(ctx.guild.text_channels, name="dropped-notes")

    if not target_channel or not notes_channel:
        await ctx.send("❌ Couldn't find the channel(s).")
        return

    # 25% chance = send to 'notes'
    if random.random() < 0.25:
        await notes_channel.send(f'Note dropped from {ctx.author.display_name}. It reads "{message}"')
    else:  # 75% chance = send to chosen channel
        await target_channel.send(f'Note sent from {ctx.author.display_name}. It reads "{message}"')

# Run the bot
bot.run(TOKEN)
