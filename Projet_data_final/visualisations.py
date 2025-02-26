import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import json as json
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer


#importer le df dans un cache à court terme (et éviter de l'importer à chaque fois)
@st.cache_data
def get_data():
    # Chemin vers le cvs
    df = pd.read_csv("clean_df_analysis.csv", low_memory=False)
    return df

df = get_data()

#téléchargement des données géographiques des régions françaises
with open("regions.geojson", "r") as file:
    geojson_reg = json.load(file)

#téléchargement des données géographiques des départements français
with open("departements.geojson", "r") as file:
    geojson_dept = json.load(file)

def visu(): 
    st.markdown("<h1 style='color: orange;'>📉 Visualisations</h1>", unsafe_allow_html=True)
    
    #NOMBRE DE VENTES SELON REGION
    st.subheader(":red[Répartition du nombre des ventes par régions :]")

    #Pie chart du nombre de vente tous bien confondus (régions puis départements)
    total_ventes_reg = df.groupby("nom_region").size()

    fig_region = px.pie(total_ventes_reg, total_ventes_reg.index, total_ventes_reg.values,hole=0.35)

    plt.gcf().set_facecolor('none')

    st.plotly_chart(fig_region)

    #Répartition des ventes selon le type de bien par département selon la région

    liste_regions = df["nom_region"].unique()
    region_selectionnee = st.selectbox("Choisissez une région :", options=liste_regions, key = "region_selectionnee")

    df_region = df[df["nom_region"] == region_selectionnee]
    df_moyenne_prix = df_region.groupby("nom_departement", as_index=False)["prix_m²"].mean()

    detail_ventes = df_region.groupby(["nom_departement", "type_local"]).size().reset_index(name="nombre_ventes")
    detail_ventes["type_local"] = detail_ventes["type_local"].replace({"Local industriel. commercial ou assimilé": "Locaux industriels<br>ou commerciaux"})

    fig_detail_ventes = px.bar(detail_ventes, x="nom_departement", y="nombre_ventes", color="type_local", title=f"Nombre de ventes par départements pour {region_selectionnee}")

    fig_detail_ventes.update_layout(xaxis=dict(
        tickmode='array',  
        tickvals=df_moyenne_prix["nom_departement"].tolist(),
        ticktext=df_moyenne_prix["nom_departement"].tolist()),
        width=700, height=400)
    
    st.plotly_chart(fig_detail_ventes)

    #PRIX/m² SELON LA REGION

    st.subheader(":red[Répartition du prix/m² selon la région :]")

    #Carte des prix/m² selon la région
    fig = px.choropleth_mapbox(df, geojson=geojson_reg, locations="nom_region", 
    featureidkey="properties.nom", color="prix_m²", color_continuous_scale="Blues", range_color=(0, 10000),
    mapbox_style="carto-positron",
    zoom=4,
    center={"lat": 46.60, "lon": 1.88},
    opacity=0.8)

    st.plotly_chart(fig)

    #Diagramme prix/m² entre départements d'une région

    region_selectionnee_2 = st.selectbox("Choisissez une région :", options=liste_regions, key = "region_selectionnee_2")

    df_region2 = df[df["nom_region"] == region_selectionnee_2]
    df_moyenne_prix2 = df_region2.groupby("nom_departement", as_index=False)["prix_m²"].mean()

    fig_bars = px.bar(df_moyenne_prix2, x="nom_departement", y="prix_m²", color="prix_m²", title=f"Moyenne des prix au m² par départements pour {region_selectionnee_2}")

    fig_bars.update_layout(xaxis=dict(
        tickmode='array',  
        tickvals=df_moyenne_prix2["nom_departement"].tolist(),
        ticktext=df_moyenne_prix2["nom_departement"].tolist()), 
        width=700, height=400)
    
    st.plotly_chart(fig_bars)


    # Visualisation des prix au m² par type local selon les départements d'une région
    
    filtered_df = df[df["nom_region"]==region_selectionnee_2]

    prix_moyen_type_local = filtered_df.groupby(["nom_departement", "type_local"])["prix_m²"].mean().reset_index()

    fig3 = px.bar(prix_moyen_type_local, 
              x="prix_m²", 
              y="nom_departement", 
              color="type_local", 
              barmode="group", 
              title=f"Prix/m² moyen selon le type de local pour les départements de la région {region_selectionnee_2}",  
              labels={"prix_m²": "Prix moyen (€/m²)", "nom_departement": "Département", "type_local": "Type Local"})
    
    fig3.update_layout(
    xaxis_title="Prix moyen par m² (€)",
    yaxis_title="Département",
    xaxis=dict(tickformat=",.0f"),  
    height=600)

    st.plotly_chart(fig3, use_container_width=True)

    st.subheader(":red[Représentations graphiques sur la 'diagonale du vide' :]")

    #Diagonale du vide en carte

    df_filtered = df[["dans_diag_vide", "prix_m²", "nom_departement", "code_departement", "latitude", "longitude"]]
    

    fig_diag = px.choropleth_mapbox(df_filtered, geojson=geojson_dept, locations="code_departement", featureidkey="properties.code", color="dans_diag_vide", color_discrete_map={True: "blue", False: "lightblue"},
    mapbox_style="carto-positron",
    zoom=4,
    center={"lat": 46.60, "lon": 1.88},
    opacity=0.8
    )

    st.plotly_chart(fig_diag)

    #Diagramme en bâtons diagonale du vide

    #import de la sauvegarde json du pygwalker
    with open('sauvegardepygwalker.json', 'r') as f:
        config = json.load(f)

    #parametre de pygwalker
    pyg_app = StreamlitRenderer(df, spec = config, width=1000, height=600)

    pyg_app.explorer()

    


