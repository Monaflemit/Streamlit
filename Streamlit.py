import pandas as pd

data = {
    'Grande discipline': ['STAPS', 'Sciences et sciences de l\'ingénieur', 'Interdisciplinaire', 'Droit, sciences économiques, AES', 'Santé', 'Lettres, langues et sciences humaines'],
    '% femmes': [31.967858, 39.317534, 45.410628, 61.846798, 66.505879, 70.226618]
}

df = pd.DataFrame(data)


import streamlit as st


st.set_option('deprecation.showPyplotGlobalUse', False)

# Ajouter un titre
st.title("Pourcentage de femmes dans les principaux diplômes préparés dans l'Enseignement supérieur")

# Ajouter du texte
st.write('Source : https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-principaux-diplomes-et-formations-prepares-etablissements-publics/information/')

col1, col2,col3,col4 = st.columns(4)

def plot_graph1():
  
    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df.set_index('Grande discipline')['% femmes'], use_container_width=True)

    # Afficher le tableau sans l'index
    st.write(df)  

if col1.button('Pourcentage de femmes par grande discipline'):
    plot_graph1()
    

    
    
    
