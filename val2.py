import requests
import re

joueur = input('entrer un nom de joueur :')

url = "https://www.transfermarkt.co.uk/ian-raeymaekers/profil/spieler/"+(joueur)


navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'

html = requests.get(url, headers={'User-Agent': navigator})
from bs4 import BeautifulSoup

soup = BeautifulSoup(html.text, 'html.parser')

items= soup.find(class_="tm-player-market-value-development__max-value").text
valval= soup.find(class_='data-header__club-info').text

print(items)
print(valval)

