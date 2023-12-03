from flask import Flask
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os

from routes import index

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
CORS(app, resources={r"/api/*":{"origins":"*"}})
#*Register the blueprint inside the app flask
app.register_blueprint(index.indexBp)

if __name__ == '__main__':
  app.run(debug=True)