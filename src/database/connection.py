from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

def getConnection():
  try: 
    conn = psycopg2.connect(
      dbname=os.getenv("DB_NAME"),
      user=os.getenv("DB_USER"),
      password=os.getenv("DB_PASSWORD"),
      host=os.getenv("DB_HOST"),
      port=os.getenv("DB_PORT")
    )
    #*Returns de connection object
    return conn
  except psycopg2.Error as e:
    print("Error during DB connection, getConnection:"+e)
    return None

def closeConnection():
  conn.close()
