from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import pprint as pp
from helpers import *
from random import shuffle


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
db = SQL("sqlite:///boombazled.db")

@app.route("/", methods=["GET", "POST"])
def index():
    """Register user."""

    # forget any user id
    session.clear()

    if request.method == "POST":

        password = gen_password()

        for item in range(int(request.form.get("number"))):
            nickname = request.form.get("nickname" + str(item + 1))
            db.execute("INSERT INTO players (nickname, id) VALUES (:nickname, :id)",
                        nickname=nickname, id=password)

        return redirect(url_for("lobbyHost"))

    else:
        return render_template('index.html')

@app.route("/lobbyHost", methods=["GET", "POST"])
def lobbyHost():

    if request.method == "POST":
        if request.form['button'] == 'leave':
            return render_template("index.html", value = 0)

        if request.form['button'] == 'start':
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3], rightAnswer = rightAnswer)

        if request.form['button'] == 'settings':
            return redirect(url_for("gamesettings"))

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
            return redirect(url_for("lobbyHost"))

    else:
        return render_template("gamesettings.html")

@app.route("/game", methods=["GET", "POST"])
def game():

    if request.method == "POST":
        if request.form['button'] == request.form['rightAnswer']:
            print('correct!')
            return render_template("card.html")

        elif request.form['button'] == 'settings':
            return render_template("sessionsettings.html")

        else:
            print('incorrect!')
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3], rightAnswer = rightAnswer)



    else:

        return render_template("game.html")

@app.route("/sessionsettings", methods=["GET", "POST"])
def sessionsettings():

    if request.method == "POST":
        if request.form['button'] == 'back':
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3], rightAnswer = rightAnswer)

        if request.form['button'] == 'leave':
            return render_template("index.html", value=0)

    else:
        return render_template("sessionsettings.html")

@app.route("/card", methods=["GET", "POST"])
def card():

    if request.method == "POST":
        if request.form['button'] == 'activate':
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3], rightAnswer = rightAnswer)


        if request.form['button'] == 'settings':
            return render_template("sessionsettings.html")

    else:
        return render_template("card.html")

@app.route("/lobbyWin", methods=["GET", "POST"])
def lobbyWin():

    if request.method == "POST":
        if request.form['button'] == 'leave':
            return render_template("index.html", value=0)

        if request.form['button'] == 'restart':
            return render_template("lobbyPlayer.html")

    else:
        return render_template("lobbyWin.html")

