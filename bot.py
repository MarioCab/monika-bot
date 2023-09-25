import discord
import os
from config import get_joke
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
from responses import general_responses
from responses import images
import random
import requests
import json
import time
from steam import Steam
from decouple import config
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup




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

    if ((message.content)[0]) == "💖" and ((message.content)[-1]) == "💖" in (message.content).lower():
        gen = bot.get_channel(1147006775065858058)
        robsIdea = "https://discord.com/channels/872994683603796038/1139401271036624916/"
        await gen.send(f"{robsIdea}{(message.id)}")
        await gen.send(f"A claim has been made! {(message.content)} What a score!")
    
    if "$charts" in (str(message.content).lower()):
        g1 = (str(message.content))
        game = g1.removeprefix('$charts ')
        print(game)
        KEY = config("STEAM_API_KEY")
        steam = Steam(KEY)
        steamResults = steam.apps.search_games(game)
        #time.sleep(3)
        print(steamResults)
        game_id = (steamResults['apps'][0]['id'])
        img_id = (steamResults['apps'][0]['img'])
        print(game_id)
        print(img_id)
        url = (f"https://steamcharts.com/app/{game_id}")
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        doc = BeautifulSoup(data, "html.parser")
        recent = (doc.find_all("span")[2]).string
        twentyfourhour = (doc.find_all("span")[3]).string
        allTime = (doc.find_all("span")[4]).string
        print(recent.string)
        print(twentyfourhour.string)
        print(allTime.string)
        embedChart=discord.Embed(color=15105570)
        embedChart.set_image(url=f"{img_id}")
        embedChart.add_field(name=f"Game",value=f"{game.upper()}", inline=False)
        embedChart.add_field(name="Recent Player Count", value=f"{recent}", inline=False)
        embedChart.add_field(name="24 Hour Peak", value=f"{twentyfourhour}", inline=False)
        embedChart.add_field(name="All Time Peak", value=f"{allTime}", inline=False)
        await message.channel.send(embed = embedChart)
        #await message.channel.send(f"📈 Here is the steam chart data for {game}:\n\n⭐ Recent Player Count: {recent}\n\n⭐ 24Hr Player Count: {twentyfourhour}\n\n⭐ All Time Peak: {allTime}")
    if "$waf" in (str(message.content).lower()):
        class MyView(discord.ui.View): 
            @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="💖")
            async def button_callback(self, interaction, button):
                await interaction.response.send_message(f"Everyone point and laugh at {interaction.user.name} they just clicked the button. The obviously fake button. Publicly shame them\n", file=discord.File("./img/laugh.jpg"))
        #await message.channel.send(file=discord.File(f"./img/{random.choice(images)}")) 
        embed=discord.Embed(color=15105570)
        embed.add_field(name="Fake", value="Will you fall for this?", inline=False)
        embed.add_field(name="943", value="React with any emoji to claim!", inline=False)
        embed.set_image(url=random.choice(images))
        await message.channel.send(embed = embed)
        await message.channel.send(view=MyView())    

    else:
        print(message.content)
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
