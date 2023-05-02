import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode
load_dotenv()
import requests
import json


# Database context

cnx = mysql.connector.connect(
    user= os.getenv('DB_USER'),
    password= os.getenv('DB_PW'),
    host= os.getenv('DB_HOST'),
    database= os.getenv('DB_NAME'))


# Test DB connection

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



# Get request for jokes API

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    response_json = json.loads(response.text)
    joke = response_json['joke']
    return joke


# Popular Airing Anime

def get_pop_airing():
    url = "https://myanimelist.p.rapidapi.com/anime/top/airing"

    headers = {
	"X-RapidAPI-Key": "557fb94ce3msh7876cdde15b2a77p18ecb7jsn0cc03d43f1b0",
	"X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
}
    nameList = []
    scoreList = []

    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    
    for item in response_json:
        nameList.append(item['title'])
        scoreList.append(item['score'])
        return nameList, scoreList
    
get_pop_airing()


