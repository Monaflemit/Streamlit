import pandas as pd  #!pip install --ignore-installed Pygments
#streamlit run Streamlit.py
url = "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-principaux-diplomes-et-formations-prepares-etablissements-publics/exports/csv?lang=fr&refine=annee_universitaire%3A%222022-23%22&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
df = pd.read_csv(url,sep=';')

import streamlit as st


st.set_option('deprecation.showPyplotGlobalUse', False)

# Ajouter un titre
st.title("Pourcentage de femmes dans les principaux diplômes préparés dans l'Enseignement supérieur")

# Ajouter du texte
st.write('Source : https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-principaux-diplomes-et-formations-prepares-etablissements-publics/information/')

col1, col2,col3,col4 = st.columns(4)

def plot_graph1():
    df_grouped = df.groupby('Grande discipline').sum()
    df_grouped = df_grouped.reset_index()
    df_grouped['% femmes'] = df_grouped['Dont femmes'] / (df_grouped['Dont femmes'] + df_grouped['Dont hommes']) * 100
    df_grouped = df_grouped.sort_values('% femmes', ascending=True)

    #plt.xticks(range(len(df_grouped['Grande discipline'])), df_grouped['Grande discipline'], rotation=90)

    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df_grouped.set_index('Grande discipline')['% femmes'], use_container_width=True)

    # Ajouter des étiquettes pour les axes et le titre
    #st.set_xlabel('Grande discipline')
    #st.set_ylabel('Pourcentage de femmes')
    #st.set_title('Pourcentage de femmes par grande discipline en 2022')

    # Afficher le graphique
    st.pyplot()
    
    # Sélectionner les colonnes souhaitées
    df_display = df_grouped.loc[:, ['Grande discipline', '% femmes']]

    # Afficher le tableau sans l'index
    st.write(df_display)  

if col1.button('Pourcentage de femmes par grande discipline'):
    plot_graph1()
    
def plot_graph2():
    df_grouped = df.groupby('Discipline').sum()
    df_grouped = df_grouped.reset_index()
    df_grouped['% femmes'] = df_grouped['Dont femmes'] / (df_grouped['Dont femmes'] + df_grouped['Dont hommes']) * 100

    df_grouped = df_grouped.sort_values('% femmes', ascending=True)

    #plt.xticks(range(len(df_grouped['Discipline'])), df_grouped['Discipline'],rotation=90)

    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df_grouped.set_index('Discipline')['% femmes'], use_container_width=True)

    # Ajouter des étiquettes pour les axes et le titre
    #plt.xlabel('Discipline')
    #plt.ylabel('Pourcentage de femmes')
    #plt.title('Pourcentage de femmes par discipline en 2022')
    
    # Afficher le graphique
    st.pyplot()
    
    # Sélectionner les colonnes souhaitées
    df_display = df_grouped.loc[:, ['Discipline', '% femmes']]
    
    # Afficher le tableau sans l'index
    st.write(df_display)      
    
if col2.button('Pourcentage de femmes par discipline'):
    plot_graph2()    
    
    
    
def plot_graph3():
    #Secteur disciplinaire
    import matplotlib.pyplot as plt


    df_grouped = df.groupby('Secteur disciplinaire').sum()
    df_grouped = df_grouped.reset_index()
    df_grouped['% femmes'] = df_grouped['Dont femmes'] / (df_grouped['Dont femmes'] + df_grouped['Dont hommes']) * 100

    df_grouped = df_grouped.sort_values('% femmes', ascending=True)

    #plt.xticks(range(len(df_grouped['Secteur disciplinaire'])), df_grouped['Secteur disciplinaire'],rotation=90)




    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df_grouped.set_index('Secteur disciplinaire')['% femmes'], use_container_width=True)
    
    # Ajouter des étiquettes pour les axes et le titre
    #plt.xlabel('Secteur disciplinaire')
    #plt.ylabel('Pourcentage de femmes')
    #plt.title('Pourcentage de femmes par secteur disciplinaire en 2022')

    # Afficher le graphique
    st.pyplot()

    df_display = df_grouped.loc[:, ['Secteur disciplinaire', '% femmes']]
    df_display  
    
    
if col3.button('Pourcentage de femmes par Secteur disciplinaire'):
    plot_graph3()        
    
def plot_graph4():    
    #Diplôme
    import matplotlib.pyplot as plt


    df_grouped = df.groupby('Diplôme').sum()
    df_grouped = df_grouped.reset_index()
    df_grouped['% femmes'] = df_grouped['Dont femmes'] / (df_grouped['Dont femmes'] + df_grouped['Dont hommes']) * 100

    df_grouped = df_grouped.sort_values('% femmes', ascending=True)

    #plt.xticks(range(len(df_grouped['Diplôme'])), df_grouped['Diplôme'],rotation=90)

    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df_grouped.set_index('Diplôme')['% femmes'], use_container_width=True)
    
    # Ajouter des étiquettes pour les axes et le titre
    #plt.xlabel('Diplôme')
    #plt.ylabel('Pourcentage de femmes')
    #plt.title('Pourcentage de femmes par Diplôme en 2022')

    # Afficher le graphique
    st.pyplot()
    
    df_display = df_grouped.loc[:, ['Diplôme', '% femmes']]
    df_display
    
if col4.button('Pourcentage de femmes par Diplôme'):
    plot_graph4()         
    
