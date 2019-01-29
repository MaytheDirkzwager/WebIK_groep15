from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import pprint as pp
from helpers import *
import random

"""
Mocht je een vraag willen genereren, doe het als volgt:
    my_api = Trivia(True)
    response = my_api.request(1, Category.Books, Diffculty.Hard, Type.Multiple_Choice)
Vul je geen categorie of difficulty in, dan wordt er random eentje gekozen!
Raadpleeg bron voor juiste spelling en/of andere informatie:
https://github.com/MaT1g3R/Python-Trivia-API
"""


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

    if request.method == "POST":
        if request.form['button'] == request.form['rightAnswer']:
            db.execute("UPDATE players SET score = score + :point WHERE nickname = :nickname",
                    point = 1, nickname = session["players"][session["turn"]])

            data_list = [{'name':'speed', 'title':'Supersonic speedround', 'description': '???'},
                    {'name':'chance', 'title':'Ladder of chance to the golden mud hut', 'description':'Choose a number between 1 and 10'},
                    {'name':'googol', 'title':'Googol card', 'description':'You get two points'},
                    {'name':'monkey', 'title':'Hungry monkey', 'description':'You get all the points from the winning player'},
                    {'name':'banana', 'title':'Banana turn', 'description':'Next player will be skipped'}]

            data = data_list[randint(0,4)]

            return render_template("card.html", data=data)

        elif request.form['button'] == 'leave':
            return redirect(url_for("index"))

        else:
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])
            score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
            score = score[0]['score']
            question, rightAnswer, wrongAnswers = getQuestion()
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", answerOptions = answer_options, players = players, question = question,
                                    rightAnswer=rightAnswer, player=session["players"][session["turn"]], score = score)

    else:

        question, rightAnswer, wrongAnswers = getQuestion()
        # session["theAnswer"] = rightAnswer
        answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
        shuffle(answer_options)
        return render_template("game.html", answerOptions = answer_options, players = players, question = question,
                                rightAnswer = rightAnswer, player=session["players"][session["turn"]], score=score)

@app.route("/card", methods=["GET", "POST"])
def card():

    if request.method == "POST":
        if request.form['button'] == 'speed':
            return redirect(url_for("game"))

        if request.form['button'] == 'chance':
            return redirect(url_for("game"))

        if request.form['button'] == 'googol':
            db.execute("UPDATE players SET score = score + 2 WHERE id=:id AND nickname=:nickname", id=session["id"], nickname=session["players"][session["turn"]])
            return redirect(url_for("game"))

        if request.form['button'] == 'monkey':
            return redirect(url_for("game"))

        if request.form['button'] == 'banana':
            return redirect(url_for("game"))


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

# @app.route("/question_check", methods=["GET", "POST"])
# def question_check():
#     answer_given = request.args.get("answer_given")
#     correct_answer = session["theAnswer"]

#     if answer_given == correct_answer:
#         return jsonify(status="success")
#     else:
#         return jsonify(status="fail")





