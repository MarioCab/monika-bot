import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode
load_dotenv()



cnx = mysql.connector.connect(
    user= os.getenv('DB_USER'),
    password= os.getenv('DB_PW'),
    host= os.getenv('DB_HOST'),
    database= os.getenv('DB_NAME'))


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
