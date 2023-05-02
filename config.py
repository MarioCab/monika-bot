import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv
load_dotenv()



# DB Connection

def test_connection():
    cnx = mysql.connector.connect(
        user= os.getenv('DB_USER'),
        password= os.getenv('DB_PW'),
        host= os.getenv('DB_HOST'),
        database= os.getenv('DB_NAME')
    )
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





