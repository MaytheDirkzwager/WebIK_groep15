import aiohttp
import requests
from pytrivia import Category, Diffculty, Type, Trivia
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
