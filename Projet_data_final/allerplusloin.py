import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer
import json


#importer le df dans un cache à court terme (et éviter de l'importer à chaque fois)
@st.cache_data
def get_data():
    # Chemin vers le cvs
    df = pd.read_csv("clean_df_analysis.csv", low_memory=False)
    return df

df = get_data()

def loin():
    st.markdown("<h1 style='color: orange;'>💡 Graphiques pour aller plus loin</h1>", unsafe_allow_html=True)
    
    ###Graphiques corrélation####
    ### Menu déroulant pour sélectionner un département
    departements = df["nom_departement"].unique()
    departement_selectionne = st.selectbox("Sélectionnez un département :", sorted(departements))

    
    data_filtre = df[df["nom_departement"] == departement_selectionne]

    st.subheader("Corrélation : Prix au m² vs Superficie Réelle Bâtie")
    fig_corr = px.scatter(
        data_filtre,
        x="total_surface_reelle_batie",
        y="prix_m²",
        labels={"total_surface_reelle_batie": "Superficie Réelle Bâtie (m²)", "prix_m²": "Prix au m² (€)"},
        title=f"Relation entre Superficie Réelle Bâtie et Prix au m² - {departement_selectionne}",
        color_discrete_sequence=["blue"]
    )

    # Ajuster les limites des axes pour que les deux commencent à 0
    fig_corr.update_layout(
        xaxis=dict(range=[0, data_filtre["total_surface_reelle_batie"].max()]),  
        yaxis=dict(range=[0, data_filtre["prix_m²"].max()])  
    )
    
    st.plotly_chart(fig_corr)

    # Corrélation : Prix au m² vs Sismicité
    st.subheader("Corrélation : Prix au m² vs Sismicité")
    fig_corr2 = px.box(
        df,
        x="Sismicite",
        y="prix_m²",
        labels={"Sismicite": "Sismicité", "prix_m²": "Prix au m² (€)"},
        title="Distribution des prix au m² selon la sismicité",
        color="Sismicite"
    )
    st.plotly_chart(fig_corr2)

    # Corrélation : Prix au m² vs Zone Inondable
    st.subheader("Corrélation : Prix au m² vs Zone Inondable")
    fig_corr3 = px.box(
        df,
        x="in_zone_inondable",
        y="prix_m²",
        labels={"in_zone_inondable": "Zone Inondable", "prix_m²": "Prix au m² (€)"},
        title="Distribution des prix au m² selon la zone inondable",
        color="in_zone_inondable"
    )
    st.plotly_chart(fig_corr3)

    #Diagramme pygwalker

    #import de la sauvegarde json du pygwalker
    with open('sauvegardepygwalker.json', 'r') as f:
        config = json.load(f)

    #parametre de pygwalker
    pyg_app = StreamlitRenderer(df, spec = config, width=1000, height=600)

    pyg_app.explorer()