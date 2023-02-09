from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    "https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_de_computadores")
bs = BeautifulSoup(html, 'html.parser')

print(bs)
