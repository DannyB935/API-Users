from flask import Blueprint

#*Creating the index blueprint for the routes
indexBp = Blueprint("index", __name__)

@indexBp.route("/test")
def test():
    return "Testing API"