import aiohttp
import string
import requests
from pytrivia import Category, Diffculty, Type, Trivia
from random import *
my_api = Trivia(True)
response = my_api.request(1, Category.Books, Diffculty.Hard, Type.Multiple_Choice)
print(response)

def getQuestion():

    my_api = Trivia(True)
    response = my_api.request(1, None, None, Type.Multiple_Choice)

    question = response['results'][0]['question']
    rightAnswer = response['results'][0]['correct_answer']
    wrongAnswers = response['results'][0]['incorrect_answers']

    return question, rightAnswer, wrongAnswers


def gen_password():
    min_char = 4
    max_char = 4
    allchar = string.ascii_letters + string.digits
    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return password

