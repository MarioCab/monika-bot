import discord
import os
from config import test_connection, get_joke, get_pop_airing
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
from responses import general_responses
import random
import requests
import json


# Load Connections

# test_connection()

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


# General responses to having Monika in the message

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "monika" in (str(message.content).lower()):
        await message.channel.send(random.choice(general_responses))
    else:
        return
    await bot.process_commands(message)


# Slash command for Monika to tell a joke

@bot.tree.command(name="joke")
async def joke(interaction: discord.Interaction):
    await interaction.response.send_message(get_joke())


# Slash Command for Monika to pull Popular  Anime
@bot.tree.command(name="popular")
async def popular(interaction: discord.Interaction):

    url = "https://myanimelist.p.rapidapi.com/anime/top/airing"

    headers = {
	"X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
	"X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
}
    nameList = []
    scoreList = []

    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    
    for item in response_json:

        nameList.append(item['title'])
        scoreList.append(item['score'])
    
    await interaction.response.send_message(
        f"Here is the top 10 currently airing anime!\n\n1) {nameList[0]}: {scoreList[0]}\n\n2) {nameList[1]}: {scoreList[1]}\n\n3) {nameList[2]}: {scoreList[2]}\n\n4) {nameList[3]}: {scoreList[3]}\n\n5) {nameList[4]}: {scoreList[4]}\n\n6) {nameList[5]}: {scoreList[5]}\n\n7) {nameList[6]}: {scoreList[6]}\n\n8) {nameList[7]}: {scoreList[7]}\n\n9) {nameList[8]}: {scoreList[8]}\n\n10) {nameList[9]}: {scoreList[9]}")

bot.run(TOKEN)
