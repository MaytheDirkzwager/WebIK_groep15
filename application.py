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
        players = []

        for item in range(int(request.form.get("number"))):
            nickname = request.form.get("nickname" + str(item + 1))
            players.append(nickname)
            db.execute("INSERT INTO players (nickname, id) VALUES (:nickname, :id)",
                        nickname=nickname, id=password)
        session["players"] = players
        session["turn"] = 0
        session["id"] = password
        return redirect(url_for("game"))

    else:
        return render_template('index.html')


@app.route("/game", methods=["GET", "POST"])
def game():

    score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
    score = score[0]['score']
    players = db.execute("SELECT * FROM players WHERE id = :id", id = session["id"])
    print(players)
    print(score)

    if request.method == "POST":
        if request.form['button'] == request.form['rightAnswer']:
            print('correct!')
            db.execute("UPDATE players SET score = score + :point WHERE nickname = :nickname",
                    point = 1, nickname = session["players"][session["turn"]])

            return redirect(url_for("card"))

        elif request.form['button'] == 'leave':
            return redirect(url_for("index"))

        else:
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])
            score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
            score = score[0]['score']
            print('incorrect!')
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", players = players, question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3], rightAnswer = rightAnswer, player=session["players"][session["turn"]], score = score)

    else:

        question, rightAnswer, wrongAnswers = getQuestion()
        answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
        shuffle(answer_options)
        return render_template("game.html", players = players, question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2],
                                    answerD = answer_options[3], rightAnswer = rightAnswer, player=session["players"][session["turn"]], score=score)

@app.route("/card", methods=["GET", "POST"])
def card():

    if request.method == "POST":
        if request.form['button'] == 'activate':
            return redirect(url_for("game"))


        if request.form['button'] == 'settings':
            return redirect(url_for("sessionsettings"))

    else:
        return render_template("card.html")

@app.route("/lobbyWin", methods=["GET", "POST"])
def lobbyWin():

    if request.method == "POST":
        if request.form['button'] == 'leave':
            return redirect(url_for("index"))

        if request.form['button'] == 'restart':
            return redirect(url_for("lobbyPlayer"))

    else:
        return render_template("lobbyWin.html")

