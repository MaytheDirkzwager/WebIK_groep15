import aiohttp
import requests
from pytrivia import Category, Diffculty, Type, Trivia
my_api = Trivia(True)
response = my_api.request(1, Category.Books, Diffculty.Hard, Type.Multiple_Choice)
print(response)