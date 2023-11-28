from dotenv import load_dotenv
import os
import jwt

class Security():

  def __init__(self) -> None:
    load_dotenv()
    return None
  
  #*Gets the payload dict
  def getToken(self, p):
    return jwt.encode(p, os.getenv('SECRET_KEY'), algorithm="HS256")
  
  #*Gets the request headers
  def verifyToken(self, h):
    #*Verify the auth is in the header request (bearer token)
    if 'Authorization' in h.keys():
      auth = h["Authorization"]
      #*We get the auth type on the first element and the token on the second one
      auth = auth.split(" ")[1]
      try:
        payload = jwt.decode(auth, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        return True
      except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
        return False
    return False