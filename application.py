from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import pprint as pp

# from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# # custom filter
# app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")

@app.route("/", methods=["GET", "POST"])
def index():
    """Register user."""

    # forget any user id
    session.clear()

    if request.method == "POST":

        if request.form['button'] == 'make':
            return render_template("lobbyHost.html")

        if request.form['button'] == 'join':
            return render_template("lobbyPlayer.html")

    else:
        return render_template("index.html")

@app.route("/lobbyHost", methods=["GET", "POST"])
def lobbyHost():

    if request.method == "POST":
        if request.form['button'] == 'leave':
            return render_template("index.html")

        if request.form['button'] == 'start':
            return render_template("lobbyPlayer.html")


    else:
        return render_template("lobbyHost.html")


@app.route("/lobbyPlayer", methods=["GET", "POST"])
def lobbyPlayer():

    if request.method == "POST":
        return render_template("index.html")

    else:
        return render_template("lobbyPlayer.html")

