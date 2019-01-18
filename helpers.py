# import aiohttp
# import requests
import string

# from pytrivia import Category, Diffculty, Type, Trivia
# my_api = Trivia(True)
# response = my_api.request(1, Category.Books, Diffculty.Hard, Type.Multiple_Choice)
# print(response)

from random import *

def gen_password():
    min_char = 4
    max_char = 4
    allchar = string.ascii_letters + string.digits
    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return password