from flask import Blueprint, jsonify, request
from database import connection
import psycopg2

from models import user

#*DB connection
myDB = connection.Database()
myConn = myDB.getConnection()

#*Creating the index blueprint for the routes
indexBp = Blueprint("index", __name__)

@indexBp.route("/test")
def test():
  return "Testing API"

@indexBp.route("/api/users/", methods=['GET'])
def getUsers():

  try:
    cursor = myConn.cursor()
    cursor.execute("SELECT * FROM usuario")
    rows = cursor.fetchall()

    if rows:

      res = []
      for row in rows:
        newUser = user.User(
          row[0],
          row[1],
          row[2],
          row[3],
          row[4],
          row[5],
          row[6],
          row[7],
          row[8]
        )
        res.append(newUser.toJson())

      cursor.close()
      return jsonify(res)
    else:
      return '{"status":"ok", "message":"usuario table is empty"}'
  except psycopg2.Error as e:
    return '{"status":"fail", "code": 500, "error":"'+str(e)+'"}'

#*Insert new common user
@indexBp.route('/api/users/newc/', methods=["POST"])
def newCommonUser():

  try:

    if request.method == "POST":
      jsonUser = request.json

      query = " INSERT INTO usuario VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s)"

      return jsonify(jsonUser)

  except psycopg2.Error as e:

    return jsonify({"status":"fail", "code": 500, "message": str(e)})