import streamlit as st
import pandas as pd
import numpy as np

#importer le df dans un cache à court terme (et éviter de l'importer à chaque fois)
@st.cache_data
def get_data():
    # Chemin vers le cvs
    df = pd.read_csv("clean_df_analysis.csv", low_memory=False)
    return df

df = get_data()

def description():

    st.markdown("<h1 style='color: orange;'>🔍 Description du jeu de données</h1>", unsafe_allow_html=True)

    # Texte descriptif
    st.write("Cet ensemble de données contient des informations sur les valeurs foncières géolocalisées du 01/01/2024 au 30/06/2024, avec des colonnes détaillant les transactions immobilières : identifiants de mutation, dates, valeurs foncières, adresses complètes (numéro, voie, code postal, commune), types de biens (surface, nombre de pièces), et localisation (latitude, longitude). Ces données permettent d'analyser les tendances foncières et immobilières sur le territoire français. Les données sont disponibles sur : https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/.")

    #Nombre d'observation et nombre de variables
    st.write(f"Ce data frame comporte {df.shape[0]} observations et {df.shape[1]} colonnes qui sont les variables présentées ci-dessous")

    #Tableau markdown donnant le type et la description des variables 

    st.markdown("<h2 style='color: red;'>Aperçu des données</h2>", unsafe_allow_html=True)
    
    st.markdown("""
| Nom de la variable                 | Type         | Description                                                                                  |
|------------------------------------|--------------|----------------------------------------------------------------------------------------------|
| id_mutation                        | object       | Identifiant de mutation (non stable, sert à grouper les lignes)                              |
| date_mutation                      | object       | Date de la mutation au format ISO-8601 (YYYY-MM-DD)                                          |
| nature_mutation                    | object       | Nature de la mutation                                                                         |
| valeur_fonciere                    | float64      | Valeur foncière (séparateur décimal = point): chaque id_mutation correspond à une seule et unique valeur de valeur_fonciere |
| code_postal                        | float64      | Code postal (5 caractères)                                                                   |
| code_commune                       | object       | Code commune INSEE (5 caractères)                                                            |
| nom_commune                        | object       | Nom de la commune (accentué)                                                                  |
| code_departement                   | object       | Code département INSEE (2 ou 3 caractères)                                                    |
| id_parcelle                        | object       | Identifiant de parcelle (14 caractères)                                                      |
| numero_volume                      | object       | Numéro de volume                                                                              |
| nombre_lots                        | int64        | Nombre de lots                                                                                |
| type_local                         | object       | Libellé du type de local                                                                      |
| surface_reelle_bati                | float64      | Surface réelle du bâti                                                                        |
| nombre_pieces_principales          | float64      | Nombre de pièces principales                                                                  |
| surface_terrain                    | float64      | Surface du terrain                                                                            |
| longitude                          | float64      | Longitude du centre de la parcelle concernée (WGS-84)                                         |
| latitude                           | float64      | Latitude du centre de la parcelle concernée (WGS-84)                                          |
| nom_departement                    | object       | Nom du département                                                                            |
| nom_region                         | object       | Nom de la région                                                                              |
| dans_diag_vide                     | bool         | Variable indiquant si la localité est dans la diagonale du vide ou pas                        |
| Sisimicite                         | object       | Variable indiquant le risque de sismicité de la localité                                      |
| nature_risque                      | object       | Variable indiquant la nature du risque innodable                                          |                
| in_zone_inondable                  | bool         | Variable indiquant si la localité est situé dans une zone inondable ou pas                                          |
| total_surface_reelle_batie         | float64      | Superficie réelle bâtie totale                                          |
| total_superficie_terrain           | float64      | Superficie terrain totale                                          |
| prix_m²                            | float64      | Prix/m²                                       |

    """)

    # Donnée manquantes
    #Calcul du % de valeurs manquantes par colonne
    missing_data = np.round((df.isnull().sum() / len(df)) * 100,2)

    # Convertir en DataFrame 
    missing_data_df = missing_data.reset_index()
    missing_data_df.columns = ['Colonne', 'Valeurs manquantes (%)']  

    # Afficher avec st.dataframe
    st.subheader(":red[Pourcentage de données manquantes par variable:]")
    st.dataframe(missing_data_df) 
