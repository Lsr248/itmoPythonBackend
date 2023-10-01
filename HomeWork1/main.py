from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/helloWorld")
def hello_world():
    """
    Get query for "Hello, World!" phrase
    """
    return "Hello, World!"


@app.route("/")
def index():
    """
    Get query for main page
    """
    return "main page"


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Get and post queries for user login
    """
    if request.method == "POST":
        return "post your login"
    else:
        return "get your login"


@app.route("/user/<username>")
def profile(username):
    """
    Get query for username
    """
    return "{}'s profile".format(escape(username))


app.run(host="0.0.0.0", port=81)
