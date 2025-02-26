import streamlit as st

def article():

   st.markdown("<h1 style='color: orange;'>📰 WordCloud de l'article de la valeur des prix immobiliers dans les zones touristiques</h1>", unsafe_allow_html=True)
   st.markdown("Lien de l'article de presse [ici](https://www.insee.fr/fr/statistiques/8286380#tableau-figure1_radio3)", unsafe_allow_html=True)
   st.image("wordcloud_france.png")
