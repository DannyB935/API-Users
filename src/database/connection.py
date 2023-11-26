from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

class Database():

  def __init__(self) -> None:
    self.conn = None
    try: 
      self.conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
      )

    except psycopg2.Error as e:
      print("Error during DB connection, getConnection:"+str(e))
      return None

  def getConnection(self):
    return self.conn

  def closeConnection(self):
    self.conn.close()
