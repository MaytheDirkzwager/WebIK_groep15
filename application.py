from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import pprint as pp
from helpers import *
from random import shuffle
# import aiohttp
# import requests
# from pytrivia import Category, Diffculty, Type, Trivia

from helpers import *

"""
Mocht je een vraag willen genereren, doe het als volgt:
    my_api = Trivia(True)
    response = my_api.request(1, Category.Books, Diffculty.Hard, Type.Multiple_Choice)
Vul je geen categorie of difficulty in, dan wordt er random eentje gekozen!
Raadpleeg bron voor juiste spelling en/of andere informatie:
https://github.com/MaT1g3R/Python-Trivia-API
"""

from helpers import *

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
db = SQL("sqlite:///players.db")

@app.route("/", methods=["GET", "POST"])
def index():
    """Register user."""

    # forget any user id
    session.clear()

    if request.method == "POST":

        number = []
        nickname = request.form.get("nickname")

        if request.form['button'] == 'make':
            password = gen_password()
            db.execute("INSERT INTO hosts (nickname, password) VALUES (:nickname, :password)",
                        nickname=nickname, password=password)
            return render_template("lobbyHost.html")

        if request.form['button'] == 'join' and request.form.get("password"):

            result = db.execute("SELECT * FROM hosts WHERE password=:password",
                                password=request.form.get("password"))

            if not result:
                return render_template("index.html", number=["one"], nickname=request.form.get("nickname"), error=True)

            db.execute("INSERT INTO users (nickname, password) VALUES (:nickname, :password)",
                        nickname=nickname, password=request.form.get("password"))

            db.execute("UPDATE hosts SET players = players + :number WHERE password=:password",
                        number = 1, password=request.form.get("password"))

            return render_template("lobbyPlayer.html")

        if request.form['button'] == 'join':
            number.append('one')
            value = 1
            return render_template("index.html", number=number, nickname=nickname)


    else:
        return render_template("index.html", value = 0)

@app.route("/lobbyHost", methods=["GET", "POST"])
def lobbyHost():

    if request.method == "POST":
        if request.form['button'] == 'leave':
            return render_template("index.html", value = 0)

        if request.form['button'] == 'start':
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            print(answer_options)
            return render_template("game.html", question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3])

        if request.form['button'] == 'settings':
            return render_template("gamesettings.html")

    else:
        return render_template("lobbyHost.html")


@app.route("/lobbyPlayer", methods=["GET", "POST"])
def lobbyPlayer():

    if request.method == "POST":
        return render_template("index.html", value = 0)

    else:
        return render_template("lobbyPlayer.html")

@app.route("/gamesettings", methods=["GET", "POST"])
def gamesettings():

    if request.method == "POST":
        if request.form['button'] == 'back':
            return render_template("lobbyHost.html")

    else:
        return render_template("gamesettings.html")

@app.route("/game", methods=["GET", "POST"])
def game():

    if request.method == "GET":
        return render_template("game.html")

    if request.method == "POST":
        if request.form['button'] == 'confirm':

            return render_template("card.html")

        if request.form['button'] == 'settings':
            return render_template("sessionsettings.html")

    else:

        return render_template("game.html")

@app.route("/sessionsettings", methods=["GET", "POST"])
def sessionsettings():

    if request.method == "POST":
        if request.form['button'] == 'back':
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_list = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            answer_options = shuffle(answer_list)
            return render_template("game.html", question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3])

        if request.form['button'] == 'leave':
            return render_template("index.html", value=0)

    else:
        return render_template("sessionsettings.html")

@app.route("/card", methods=["GET", "POST"])
def card():

    if request.method == "POST":
        if request.form['button'] == 'activate':
            return render_template("cardExplanation.html")

        if request.form['button'] == 'settings':
            return render_template("sessionsettings.html")

    else:
        return render_template("card.html")

@app.route("/cardExplanation", methods=["GET", "POST"])
def cardExplanation():

    if request.method == "POST":
        if request.form['button'] == 'continue':
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_list = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            answer_options = shuffle(answer_list)
            return render_template("game.html", question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3])

        if request.form['button'] == 'settings':
            return render_template("lobbyWin.html")

    else:
        return render_template("cardExplanation.html")

@app.route("/lobbyWin", methods=["GET", "POST"])
def lobbyWin():

    if request.method == "POST":
        if request.form['button'] == 'leave':
            return render_template("index.html", value=0)

        if request.form['button'] == 'restart':
            return render_template("lobbyPlayer.html")

    else:
        return render_template("lobbyWin.html")

