import streamlit as st
import pandas as pd

#importer le df dans un cache à court terme (et éviter de l'importer à chaque fois)
@st.cache_data
def get_data():
    # Chemin vers le cvs
    df = pd.read_csv("clean_df_analysis.csv", low_memory=False)
    return df

df = get_data()

df_stat = df.drop(columns=["numero_volume", "longitude", "latitude"])

# S'assurer que 'code_postal' est bien en tant qu'objet (type string)
df_stat["code_postal"] = df_stat["code_postal"].astype("object")


# Fonction de statistiques
def stats():
    st.markdown("<h1 style='color: orange;'>📊 Statistiques descriptives</h1>", unsafe_allow_html=True)
    regions = df_stat["nom_region"].unique()
    regions = ["Toutes les régions"] + list(regions)
    
    region_selected = st.selectbox("Choisissez une région", regions)

    if region_selected == "Toutes les régions":
        st.header(":red[Statistiques pour toutes les régions:]")  # Titre secondaire
        st.subheader(":orange[Statistiques descriptives des variables numériques:]")  # Titre secondaire niveau 3
        st.write(df_stat.describe())
        
        st.subheader(":orange[Statistiques descriptives des variables non numériques:]")  # Titre secondaire niveau 3
        st.write(df_stat.describe(include="object"))
    
    else:
        st.header(f":red[Statistiques pour la région : {region_selected}:]")  # Titre secondaire
        region_data = df_stat[df_stat["nom_region"] == region_selected]
        
        st.subheader(":orange[Statistiques descriptives des variables numériques:]")  # Titre secondaire niveau 3
        st.write(region_data.describe())
        
        st.subheader(":orange[Statistiques descriptives des variables non numériques:]")  # Titre secondaire niveau 3
        st.write(region_data.describe(include="object"))

