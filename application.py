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

<<<<<<< HEAD
        print("___ POST ____")

=======
        # generate a game id
>>>>>>> b0571caa97a76b3723f674fced73ff2b718b4079
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
<<<<<<< HEAD
        # max ROUNDS as opposed to current ROUND
        session["rounds"] = request.form.get("rounds")
        print(session["rounds"])
        categories = []

        # add each category that is checked, could be put into helpers
        entertainment = request.form.get("entertainment")
        if entertainment:
            categories.extend([Category.Books, Category.Film, Category.Music, Category.Musicals_Theatres, Category.Tv,
                                Category.Video_Games, Category.Board_Games, Category.Celebrities, Category.Comics, Category.Anime_Manga, Category.Cartoon, Category.Art])

        history = request.form.get("history")
        if history:
            categories.extend([Category.Mythology, Category.History])

        science = request.form.get("science")
        if science:
            categories.extend([Category.Gadgets, Category.Computers, Category.Maths, Category.Vehicles])

        nature = request.form.get("nature")
        if nature:
            categories.extend([Category.Animals, Category.Nature])

        geography = request.form.get("geography")
        if geography:
            categories.extend([Category.Geography])

        politics = request.form.get("politics")
        if politics:
            categories.extend([Category.Politics])

        sports = request.form.get("sports")
        if sports:
            categories.extend([Category.Sports])

        print(categories)

        session["categories"] = categories


        session["round"] = 0
        return redirect(url_for("game"))

    else:
        return render_template('index.html')


@app.route("/game", methods=["GET", "POST"])
def game():

    score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
    score = score[0]['score']
    players = db.execute("SELECT * FROM players WHERE id = :id", id = session["id"])

    if request.method == "POST":
        if request.form['button'] == session["theAnswer"]:
            db.execute("UPDATE players SET score = score + :point WHERE nickname = :nickname",
                    point = 1, nickname = session["players"][session["turn"]])

            session["secret_number"] = randint(1,10)
            print(session["secret_number"])

            card = get_card()

            return render_template("card.html", card=card)

        elif request.form['button'] == 'leave':
            return redirect(url_for("index"))

        else:
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])


            # if everyone got a turn, add round number
            if session["turn"] == 0:
                session["round"] += 1
                print(session["round"])

            # IF MAXIMUM AMOUNT OF ROUNDS IS SURPASSED, RENDER WIN SCREEN
            # if round == session["rounds"] + 1:
                # TODO
            score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
            score = score[0]['score']
            print('incorrect!')
            # roep hier de functie aan met de gekozen categories
            question, rightAnswer, wrongAnswers = getQuestion(session["categories"])
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", round = session["round"], question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3], rightAnswer = rightAnswer, player=session["players"][session["turn"]], score = score)

    else:

        question, rightAnswer, wrongAnswers = getQuestion(session["categories"])
        answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
        shuffle(answer_options)
        return render_template("game.html", round = session["round"], question = question, answerA = answer_options[0], answerB = answer_options[1], answerC = answer_options[2], answerD = answer_options[3], rightAnswer = rightAnswer, player=session["players"][session["turn"]], score=score)

            print(session["turn"])
            score = db.execute("SELECT score FROM players WHERE nickname = :nickname AND id = :id" , nickname = session["players"][session["turn"]], id = session["id"])
            score = score[0]['score']
            question, rightAnswer, wrongAnswers = getQuestion()
            session["theAnswer"] = rightAnswer
            answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
            shuffle(answer_options)
            return render_template("game.html", alert='sorry', answerOptions = answer_options, players = players, question = question,
                                    rightAnswer=rightAnswer, player=session["players"][session["turn"]], score = score)

    else:

        question, rightAnswer, wrongAnswers = getQuestion()
        session["theAnswer"] = rightAnswer
        answer_options = [rightAnswer, wrongAnswers[0], wrongAnswers[1], wrongAnswers[2]]
        shuffle(answer_options)
        return render_template("game.html", alert='new player', answerOptions = answer_options, players = players, question = question,
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
                return render_template("lobbyWin.html")

            # next players turn
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])
            return redirect(url_for("game"))

        if request.form['button'] == 'googol':
            # give player 2 extra points
            db.execute("UPDATE players SET score = score + 2 WHERE id=:id AND nickname=:nickname", id=session["id"], nickname=session["players"][session["turn"]])

            # next players turn
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])

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

            # next players turn
            session["turn"] += 1
            session["turn"] = session["turn"] % len(session["players"])

            return redirect(url_for("game"))

        if request.form['button'] == 'banana':
            # next player will be skipped
            session["turn"] += 2
            session["turn"] = session["turn"] % len(session["players"])

            return redirect(url_for("game"))

    else:
        return render_template("card.html")

@app.route("/lobbyWin", methods=["GET", "POST"])
def lobbyWin():
    if request.method == "POST":
        if request.form['button'] == 'leave':
            return redirect(url_for("index"))

        if request.form['button'] == 'restart':
            return redirect(url_for("index"))

    else:
        return render_template("lobbyWin.html")







