from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import pprint as pp
from helpers import *
import random
import operator

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

        # generate a game id
        password = gen_password()

        # make a list for all the players
        players = []

        # append all nicknames to the list players
        for item in range(int(request.form.get("number"))):
            nickname = request.form.get("nickname" + str(item + 1))
            players.append(nickname)
            db.execute("INSERT INTO players (nickname, id) VALUES (:nickname, :id)",
                        nickname=nickname, id=password)

        # remember the players and the game id
        session["players"] = players
        session["turn"] = 0
        session["round"] = 1
        session["id"] = password

        # max ROUNDS as opposed to current ROUND
        session["rounds"] = request.form.get("rounds")
        print(session["rounds"])

        # get all the checked categories
        session["categories"] = get_categories()

        return redirect(url_for("game"))

    else:
        return render_template('index.html')


@app.route("/game", methods=["GET", "POST"])
def game():

    # get score from current player
    score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
    score = score[0]['score']

    # get a list of all the players in the game
    players = db.execute("SELECT * FROM players WHERE id = :id", id = session["id"])

    if request.method == "POST":
        # check if given answer if the right answer
        if request.form['button'] == session["theAnswer"]:
            # update players score with one point
            db.execute("UPDATE players SET score = score + :point WHERE nickname = :nickname",
                    point = 1, nickname = session["players"][session["turn"]])

            # generate a secret number for the chance card
            session["secret_number"] = randint(1,10)
            print(session["secret_number"])

            # generate one of the four cards
            card = get_card()

            return render_template("card.html", card=card)

        # leave the game if leave button is pressed
        elif request.form['button'] == 'leave':
            return redirect(url_for("index"))

        else:
            # update turn
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])
            players_list = [(int(item["score"]), item["nickname"]) for item in db.execute("SELECT score, nickname FROM players WHERE id = :id", id=session["id"])]
            players_list.sort(key = operator.itemgetter(0), reverse = True)

            # if everyone got a turn, add round number
            if session["turn"] == 0:
                session["round"] += 1

            # render win screen if maximum number of rounds is reached
            if session["round"] == int(session["rounds"]) + 1:
                return render_template("lobbyWin.html", winner= players_list[0][1], winnerPoints = players_list[0][0])

            # get score from current player
            score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
            score = score[0]['score']

            # generate question and possible answers
            question, rightAnswer, wrongAnswers = getQuestion(session["categories"])
            # remember right answer
            session["theAnswer"] = rightAnswer
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            # shuffle the answer options
            shuffle(answer_options)
            return render_template("game.html", round = session["round"], rounds = session["rounds"], alert='sorry', answerOptions = answer_options, players = players, question = question,
                                    rightAnswer=rightAnswer, player=session["players"][session["turn"]], score = score)

    else:
        # generate question and possible answers
        question, rightAnswer, wrongAnswers = getQuestion(session["categories"])
        # remember right answer
        session["theAnswer"] = rightAnswer
        answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
        # shuffle the answer options
        shuffle(answer_options)
        return render_template("game.html", round = session["round"], rounds = session["rounds"], alert='new player', answerOptions = answer_options, players = players, question = question,
                                rightAnswer = rightAnswer, player=session["players"][session["turn"]], score=score)


@app.route("/card", methods=["GET", "POST"])
def card():

    if request.method == "POST":

        if request.form['button'] == 'chance':
            # check if the input from user is the same as the random generated number
            secret_number = str(session["secret_number"])
            answer_number = request.form.get("input_number")
            print(answer_number, secret_number)

            if secret_number == answer_number:
                # get score from current player
                score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
                score = score[0]['score']

                return render_template("lobbyWin.html", winner = session["players"][session["turn"]], winnerPoints = score)

            # next players turn
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])

            # if everyone got a turn, add round number
            if session["turn"] == 0:
                session["round"] += 1
                print(session["round"])

            # render win screen if maximum number of rounds is reached
            if session["round"] == int(session["rounds"]) + 1:
                players_list = [(int(item["score"]), item["nickname"]) for item in db.execute("SELECT score, nickname FROM players WHERE id = :id", id=session["id"])]
                players_list.sort(key = operator.itemgetter(0), reverse = True)
                return render_template("lobbyWin.html", winner= players_list[0][1], winnerPoints = players_list[0][0])

            return redirect(url_for("game"))

        if request.form['button'] == 'googol':
            # give player 2 extra points
            db.execute("UPDATE players SET score = score + 2 WHERE id=:id AND nickname=:nickname", id=session["id"], nickname=session["players"][session["turn"]])
            players_list = [(int(item["score"]), item["nickname"]) for item in db.execute("SELECT score, nickname FROM players WHERE id = :id", id=session["id"])]
            players_list.sort(key = operator.itemgetter(0), reverse = True)

            # next players turn
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])

            # if everyone got a turn, add round number
            if session["turn"] == 0:
                session["round"] += 1
                print(session["round"])

            if session["round"] == int(session["rounds"]) + 1:
                return render_template("lobbyWin.html", winner= players_list[0][1], winnerPoints = players_list[0][0])

            return redirect(url_for("game"))

        if request.form['button'] == 'monkey':
            # get score and nickname from players with the most points
            players_list = [(int(item["score"]), item["nickname"]) for item in db.execute("SELECT score, nickname FROM players WHERE id = :id", id=session["id"])]
            players_list.sort(key = operator.itemgetter(0), reverse = True)
            nickname_best = players_list[0][1]
            score_best = players_list[0][0]

            # get points from player with most points and give it to current player
            db.execute("UPDATE players SET score = 0 WHERE id = :id AND nickname = :nickname", id=session["id"], nickname=nickname_best)
            db.execute("UPDATE players SET score = score + :score WHERE id = :id AND nickname = :nickname",
                        score = score_best,id=session["id"], nickname=session["players"][session["turn"]])
            players_list = [(int(item["score"]), item["nickname"]) for item in db.execute("SELECT score, nickname FROM players WHERE id = :id", id=session["id"])]
            players_list.sort(key = operator.itemgetter(0), reverse = True)

            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])

            # if everyone got a turn, add round number
            if session["turn"] == 0:
                session["round"] += 1
                print(session["round"])

            if session["round"] == int(session["rounds"]) + 1:
                return render_template("lobbyWin.html", winner= players_list[0][1], winnerPoints = players_list[0][0])

            return redirect(url_for("game"))

        if request.form['button'] == 'banana':
            # next player will be skipped
            session["turn"] += 2
            session["turn"] = session["turn"] % len(session["players"])
            players_list = [(int(item["score"]), item["nickname"]) for item in db.execute("SELECT score, nickname FROM players WHERE id = :id", id=session["id"])]
            players_list.sort(key = operator.itemgetter(0), reverse = True)

            # if everyone got a turn, add round number
            if session["turn"] == 0 or session["turn"] == 1:
                session["round"] += 1
                print(session["round"])

            if session["round"] == int(session["rounds"]) + 1:
                return render_template("lobbyWin.html", winner= players_list[0][1], winnerPoints = players_list[0][0])

            return redirect(url_for("game"))

    else:
        return render_template("card.html")

@app.route("/lobbyWin", methods=["GET", "POST"])
def lobbyWin():
    if request.method == "POST":
        if request.form['button'] == 'leave':
            return redirect(url_for("index"))


    else:

        return render_template("lobbyWin.html")