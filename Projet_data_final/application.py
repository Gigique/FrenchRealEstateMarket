import streamlit as st

#Page en mode "wide"
st.set_page_config(layout="wide")

#Importer des pages
from accueil import accueil
from statistiques import stats
from description import description
from visualisations import visu
from allerplusloin import loin
from article import article



# Injection de CSS personnalisé pour modifier le fond de la sidebar
st.markdown("""
    <style>
        /* Personnaliser la couleur de fond de la barre latérale */
        .css-1d391kg {
            background-color: #FFCC80;  /* Couleur orange clair */
        }

        /* Personnaliser la couleur de fond des boutons dans la sidebar */
        .css-1v0mbdj {
            background-color: #FFCC80;  /* Couleur des boutons dans la sidebar */
        }

        /* Personnaliser la couleur des sections secondaires (cartes et widgets) */
        .css-1d391kg {
            background-color: #FFE0B2;  /* Couleur de fond des sections secondaires */
        }
    </style>
""", unsafe_allow_html=True)



# Création d'un sélecteur de pages dans la barre latérale
page = st.sidebar.selectbox("Choisir une page", ["Accueil", "Description des données", "Statistiques", "Graphiques", "Wordcloud", "Aller plus loin"])

# Afficher la page correspondante
if page == "Accueil":
    accueil()
elif page == "Description des données":
    description()
elif page == "Statistiques":
    stats()
elif page == "Graphiques":
    visu()
elif page == "Wordcloud":
    article()
elif page == "Aller plus loin":
    loin()
