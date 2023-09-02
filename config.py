import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode
load_dotenv()
import requests
import json


# Get request for jokes API

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    response_json = json.loads(response.text)
    joke = response_json['joke']
    return joke




