from flask import Flask
from routes import index

app = Flask(__name__)
#*Register the blueprint inside the app flask
app.register_blueprint(index.indexBp)

if __name__ == '__main__':
    app.run(debug=True)