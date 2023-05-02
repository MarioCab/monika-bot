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
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix="!", intents=intents)

# Discord Variables



# On Ready Message
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "monika" in (str(message.content).lower()):
        await message.channel.send("Oh.. I'm listening")
    else:
        return



@bot.command()
async def joke(ctx):
    await ctx.send("Joke here")



client.run(TOKEN)
