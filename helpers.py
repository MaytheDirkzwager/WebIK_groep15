from flask import Flask, flash, redirect, render_template, request, session, url_for
import aiohttp
import string
import requests
from pytrivia import Category, Diffculty, Type, Trivia
from random import *
import random

def getQuestion(categories):

    my_api = Trivia(True)
    if len(categories) != 0:
        category = random.choice(categories)
    else:
        category = None
    response = my_api.request(1, category, None, Type.Multiple_Choice)

    question = response['results'][0]['question']
    rightAnswer = response['results'][0]['correct_answer']
    wrongAnswers = response['results'][0]['incorrect_answers']

    return question, rightAnswer, wrongAnswers


def gen_password():
    # set number of characters to 4
    min_char = 4
    max_char = 4

    # use all letters and digits to create the password
    allchar = string.ascii_letters + string.digits
    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return password


def get_card():
    # list of all the card options
    cards_list = [{'name':'chance', 'title':'Ladder of chance to the golden mud hut', 'description':'Choose a number between 1 and 10'},
                    {'name':'googol', 'title':'Googol card', 'description':'You get two points'},
                    {'name':'monkey', 'title':'Hungry monkey', 'description':'You get all the points from the winning player'},
                    {'name':'banana', 'title':'Banana turn', 'description':'Next player will be skipped'}]

    # return one of the four card options
    return cards_list[randint(0,3)]

def get_categories():
    # make empty list for categories
    categories = []

    # for each category, if checked then add to list of categories
    if request.form.get("entertainment"):
        categories.extend([Category.Books, Category.Film, Category.Music, Category.Musicals_Theatres, Category.Tv, Category.Video_Games,
                            Category.Board_Games, Category.Celebrities, Category.Comics, Category.Anime_Manga, Category.Cartoon, Category.Art])

    if request.form.get("history"):
        categories.extend([Category.Mythology, Category.History])

    if request.form.get("science"):
        categories.extend([Category.Gadgets, Category.Computers, Category.Maths, Category.Vehicles])

    if request.form.get("nature"):
        categories.extend([Category.Animals, Category.Nature])

    if request.form.get("geography"):
        categories.extend([Category.Geography])

    if request.form.get("politics"):
        categories.extend([Category.Politics])

    if request.form.get("sports"):
        categories.extend([Category.Sports])

    # return complete list of checked categories
    return categories

