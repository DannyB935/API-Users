from flask import Blueprint, jsonify, request
from database import connection
import psycopg2
import uuid
import hashlib

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
    cursor.execute("SELECT * FROM usuario WHERE deleted=false")
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

      #*Makes sure the username doesnt exist
      query = "SELECT * FROM usuario WHERE username = %s AND deleted=false"
      cursor = myConn.cursor()
      cursor.execute(query, (jsonUser["username"],))
      if cursor.fetchone():
        return jsonify({"status": "error", "message": "The username already exist"})
      else:
        query = "INSERT INTO usuario VALUES( %s, %s, %s, %s, %s, %s, '');"

        #*Creates a hashed password using sha246
        passBytes = jsonUser["password"].encode('utf-8')
        sha = hashlib.sha256()
        sha.update(passBytes)

        cursor = myConn.cursor()
        cursor.execute(query, (
          str(uuid.uuid4()),
          jsonUser["name"],
          jsonUser["lastName"],
          jsonUser["username"],
          sha.hexdigest(),
          jsonUser["age"],
        ))
        myConn.commit()
        cursor.close()
        return jsonify({"status": "ok", "code": 200, "message": "New common user created"})

  except psycopg2.Error as e:

    return jsonify({"status":"fail", "code": 500, "message": str(e)})
  
#*Insert new admin user
@indexBp.route('/api/users/newa/', methods=["POST"])
def newAdmin():
  try:
    if request.method == "POST":
      jsonUser = request.json

      query = "SELECT * FROM usuario WHERE username = %s AND deleted=false"
      cursor = myConn.cursor()
      cursor.execute(query, (jsonUser["username"],))
      if cursor.fetchone():
        return jsonify({"status": "error", "message": "The username already exist"})
      else:
        query = "INSERT INTO usuario VALUES( %s, %s, %s, %s, %s, %s, '', false, 1);"

        #*Creates a hashed password using sha246
        passBytes = jsonUser["password"].encode('utf-8')
        sha = hashlib.sha256()
        sha.update(passBytes)

        cursor = myConn.cursor()
        cursor.execute(query, (
          str(uuid.uuid4()),
          jsonUser["name"],
          jsonUser["lastName"],
          jsonUser["username"],
          sha.hexdigest(),
          jsonUser["age"],
        ))
        myConn.commit()
        cursor.close()
        return jsonify({"status": "ok", "code": 200, "message": "New admin created"})

  except psycopg2.Error as e:

    return jsonify({"status":"fail", "code": 500, "message": str(e)})
  
#*Delete any user
@indexBp.route('/api/users/delete/<id>', methods=["PUT"])
def deleteUser(id):
  try:
    if request.method == "PUT":
      query = "UPDATE usuario SET deleted=true WHERE id=%s"
      cursor = myConn.cursor()
      cursor.execute(query, (id,))
      myConn.commit()
      cursor.close()

      return jsonify({"status": "ok", "code": 200, "message": "User was deleted"})
  except psycopg2.Error as e:
    return jsonify({"status": "fail", "code": 500, "message": str(e)})