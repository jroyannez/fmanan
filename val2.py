import requests
import re
import streamlit as st
from bs4 import BeautifulSoup


st.title('FIND YOUR PLAYERS')
st.write("La data au coeur de votre club de foot professionnel")


joueur = st.text_input("Entrez le nom d'un joueur (ou tapez exit pour quitter):" )


url = "https://www.transfermarkt.co.uk/ian-raeymaekers/profil/spieler/"+(joueur)

navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
html = requests.get(url, headers={'User-Agent': navigator})
soup = BeautifulSoup(html.text, 'html.parser')



val=soup.find(class_="tm-player-market-value-development__max-value").text
club= soup.find(class_='data-header__club-info').text
val
club

    

