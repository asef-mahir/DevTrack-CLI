import mysql.connector 
from dotenv import load_dotenv
import os 

load_dotenv()

def get_connection():
    try: 
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")

        mysql_connection = mysql.connector.connect(
            host = host,
            port = int(port),
            user = user,
            password = password,
            database =database
        )
        return mysql_connection
    except mysql.connector.Error as e: 
        print(f"Database connection failed: {e}")
        return None
