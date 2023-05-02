import discord
import os
from config import test_connection
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


# Load Connections

test_connection()

# Bot Variables

TOKEN =os.getenv('BOT_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Discord Variables



# On Ready Message
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "monika" in (str(message.content).lower()):
        await message.channel.send("Oh.. I'm listening")
    else:
        return
    await bot.process_commands(message)



@bot.tree.command(name="joke")
async def joke(interaction: discord.Interaction):
    await interaction.response.send_message("This is a good joke")



bot.run(TOKEN)
