import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL = "https://api.hh.ru/vacancies"
params = dict(text="Разработчик 1С", area=54)
r = requests.get(URL, params=params)
print(r.text)