import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

connection = mysql.connector.connect(
    host = os.getenv('HOST'),
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD'),
    database = os.getenv('DATABASE')
)

cursor = connection.cursor()
