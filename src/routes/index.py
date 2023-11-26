from flask import Blueprint, jsonify
from database import connection

#*DB connection
myConn = connection.getConnection()

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

    res = []
    user = {
      "id":'',
      "name": '',
      "lastName": '',
      "username": '',
      "password": '',
      "age": 0,
      "photo": '',
      "deleted": False,
      "rol": 0
    }

    for row in rows:
      user["id"] = row[0]
      user["name"] = row[1]
      user["lastName"] = row[2]
      user["username"] = row[3]
      user["password"] = row[4]
      user["age"] = row[5]
      user["photo"] = row[6]
      user["deleted"] = row[7]
      user["rol"] = row[8]

      res.append(user)

    cursor.close()

    return jsonify(res)
  except e:
    return '{"status":"fail", "code": 500}' 