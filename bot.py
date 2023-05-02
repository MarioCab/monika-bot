import os
from dotenv import load_dotenv
from config import test_connection
import discord
from discord import app_commands
load_dotenv()


# Load Connections

test_connection()

def run_bot():
    TOKEN =os.getenv('BOT_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    client.run(TOKEN)
