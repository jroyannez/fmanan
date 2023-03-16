
import pandas as pd
import requests
import re
import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image


dff = pd.read_csv("C:/Users/jroya/Desktop/encore_une.csv")

st.title('FIND YOUR PLAYERS')
st.write("La data au coeur de votre club de foot professionnel")

nomj = st.selectbox("Entrez le nom d'un joueur (ou tapez exit pour quitter):" , options=dff['Name'])

valuej = (dff.loc[dff['Name'] == nomj]['player_id'])

valj=int(valuej)
url = ("https://www.transfermarkt.co.uk/ian-raeymaekers/profil/spieler/"+str(valj))


navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
html = requests.get(url, headers={'User-Agent': navigator})
soup = BeautifulSoup(html.text, 'html.parser')



val=soup.find(class_="tm-player-market-value-development__max-value").text
club= soup.find(class_='data-header__club-info').text


st.header(val)
st.header(club)


    

