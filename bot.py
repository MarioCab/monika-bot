from email import message
import os
from dotenv import load_dotenv
from statistics import median
import discord
import random
import mysql.connector
from mysql.connector import errorcode
from discord import app_commands

load_dotenv()



#Database connection information

cnx = mysql.connector.connect(
        user= os.getenv('DB_USER'),
        password= os.getenv('DB_PW'),
        host= os.getenv('DB_HOST'),
        database= os.getenv('DB_NAME')
)
#Database connection test

def test_connection():
    try:
        cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Username or Password Error")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
        else:
            print(err)
    else: 
        print ('We have sucessfully connected to the database')

test_connection()


TOKEN =os.getenv('BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))