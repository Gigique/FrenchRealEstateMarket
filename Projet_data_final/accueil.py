import streamlit as st

def accueil():
    # Affichage du titre principal avec st.title()
    st.title("👋 Bienvenue sur notre application Streamlit !")

    # Texte descriptif avec des liens utiles, avec des sections colorées en orange
    st.markdown("""
        Cette application a été réalisée dans le cadre du projet étudiant de **Data Management**.
        
    **Ce projet a été réalisé par :**  
        AIT ALI OUBRAHIM Rachida, BIDOT Angelique, KARA Burak, ZANA Imane 
    
    <h2 style="color: orange;">Description du projet :</h2>
    Cet ensemble de données contient des informations sur les **valeurs foncières géolocalisées** du 01/01/2024 au 30/06/2024, avec des colonnes détaillant les transactions immobilières.
    Ces données permettent d'analyser les **tendances foncières et immobilières** sur le territoire français et nous avons choisi de nous focaliser sur la **France métropolitaine** pour ce projet.
        
    <h2 style="color: orange;">Liens utiles :</h2>
    <ul>
        <li><a href="https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/#/community-reuses" target="_blank">Base de données des valeurs foncières en 2024</a></li>
        <li><a href="https://www.data.gouv.fr/fr/datasets/departements-de-france/" target="_blank">Base de données des départements et régions</a></li>
        <li><a href="https://www.data.gouv.fr/fr/datasets/zonage-sismique-de-la-france-1/#/information" target="_blank">Base de données des zones sismiques en France</a></li>
        <li><a href="https://vdugrain.carto.com/tables/n_inondable/public" target="_blank">Base de données des zones inondables en France</a></li>
        <li><a href="https://www.insee.fr/fr/statistiques/8286380#tableau-figure1_radio3" target="_blank">Article de presse sur les tendances immobilières</a></li>
    </ul>
    """, unsafe_allow_html=True)
