from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)


@app.route("/helloWorld")
def hello_world():
    return "Hello, World!"


@app.route("/")
def index():
    return "main page"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "post your login"
    else:
        return "get your login"


@app.route("/user/<username>")
def profile(username):
    return "{}'s profile".format(escape(username))


app.run(host="0.0.0.0", port=81)
