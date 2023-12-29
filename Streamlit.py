import pandas as pd

data = {
    'Grande discipline': ['STAPS', 'Sciences et sciences de l\'ingénieur', 'Interdisciplinaire', 'Droit, sciences économiques, AES', 'Santé', 'Lettres, langues et sciences humaines'],
    '% femmes': [31.967858, 39.317534, 45.410628, 61.846798, 66.505879, 70.226618]
}

df = pd.DataFrame(data)


data = {
    'Discipline': ['Sciences fondamentales et applications', 'STAPS', 'Interdisciplinaire', 'Pluridisciplinaire droit, sciences économiques...', 'Sciences économiques, gestion', 'Pluridisciplinaire sciences', 'Administration économique et sociale', 'Odontologie', 'Sciences de la vie, de la terre et de l\'univers', 'Médecine', 'Pluridisciplinaire santé', 'Sciences humaines et sociales', 'Droit, sciences politiques', 'Pharmacie', 'Lettres, sciences du langage, arts', 'Pluridisciplinaire lettres, langues, sciences ...', 'Langues'],
    '% femmes': [29.754988, 31.967858, 45.410628, 48.832924, 52.845479, 58.731910, 60.482069, 61.458232, 64.713462, 65.801459, 68.811939, 68.936650, 70.131164, 70.205264, 70.844182, 72.163452, 73.109557]
}

df2 = pd.DataFrame(data)

data = {
    'Secteur disciplinaire': ['Mécanique, génie mécanique', 'Électronique, génie électrique', 'Informatique', 'Formation générale aux métiers de l\'ingénieur', 'Génie civil', 'Physique', 'Technologie et sciences industrielles', 'STAPS', 'Pluridisciplinaire sciences fondamentales et a...', 'Mathématiques', 'Génie des procédés', 'Mathématique et informatique', 'Mathématiques appliquées et sciences sociales', 'Physique et chimie', 'Interdisciplinaire', 'Sciences de l\'univers', 'Géographie', 'Pluridisciplinaire sciences économiques et ges...', 'Sciences religieuses', 'Pluridisciplinaire droit, sciences économiques...', 'Sciences économiques', 'Philosophie, épistémologie', 'Histoire', 'Aménagement', 'Sciences de gestion', 'Chimie', 'Pluridisciplinaire sciences', 'Langues et littératures anciennes', 'Administration économique et sociale', 'Odontologie', 'Pluridisciplinaire sciences de la vie, de la s...', 'Sciences politiques', 'Arts', 'Sciences de l\'information et la communication', 'Médecine', 'Sciences de la vie', 'Pluridisciplinaire langues', 'Archéologie, ethnologie, préhistoire', 'Cultures et langues régionales', 'Pluridisciplinaire santé', 'Pluridisciplinaire sciences humaines et sociales', 'Sociologie, démographie', 'Pharmacie', 'Pluridisciplinaire droit, sciences politiques', 'Pluridisciplinaire lettres, sciences du langag...', 'Sciences juridiques', 'Pluridisciplinaire lettres, langues, sciences ...', 'Langues et littératures étrangères', 'Français, langue étrangère','Langues étrangères appliquées','Littérature générale et comparée','Langues et littératures françaises','Sciences de l\'éducation','Sciences du langage, linguistique','Psychologie'],
    '% femmes': [16.498023, 17.283951, 18.033449, 24.916636, 28.974527, 29.800460, 30.712606, 31.967858, 32.639945, 32.785735, 33.372464, 36.436252, 37.948953, 42.342027, 45.410628, 45.499369, 45.531219, 46.684546, 47.954272, 48.832924, 50.602825, 51.913664, 53.235921, 53.645556, 55.529117, 57.346320, 58.731910, 60.465116, 60.482069, 61.458232, 61.988139, 63.588644, 64.834238, 65.695401, 65.801459, 66.771019, 67.000835, 67.732558, 68.442623, 68.811939, 69.593400, 69.680851, 70.205264, 70.909091, 71.286874, 71.344862, 72.163452, 72.819549, 73.413212,73.646860,73.666288,74.714555,76.294660,78.972437,84.443302]
}


df3 = pd.DataFrame(data)

data = {
    'Diplôme': ['CPES', 'Formations d\'ingénieurs', 'Diplôme universitaire de technologie', 'Bachelor universitaire de technologie', 'HDR', 'Bachelor', 'Post-DUT', 'Licence professionnelle en 1 an', 'Doctorat', 'Diplôme d\'accès aux études universitaires', 'Autres masters', 'Passeport pour réussir et s\'orienter', 'Licence professionnelle en 2 ou 3 ans', 'Autres licences', 'Autres formations', 'CPGE', 'Autres formations de santé', 'Formations d\'IEP', 'Capacité en droit', 'Licence accès santé', 'PASS et PluriPASS', 'Diplôme inter-universitaire', 'Licence sciences pour la santé (majeure santé)', 'Master enseignement', 'Formations paramédicales', 'Dispositif rebond'],
    '% femmes': [27.272727, 30.032380, 34.224599, 39.609152, 42.930153, 45.260664, 46.496815, 46.880759, 47.791942, 58.010041, 59.334749, 59.547935, 60.273973, 60.996030, 62.178499, 62.500000, 63.726668, 65.340978, 66.830333, 67.230409, 68.784301, 69.873851, 72.172172, 72.521424, 76.371692, 84.210526]
}

df4 = pd.DataFrame(data)


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
    
def plot_graph2():
  
    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df2.set_index('Discipline')['% femmes'], use_container_width=True)

    # Afficher le tableau sans l'index
    st.write(df2)  

if col2.button('Pourcentage de femmes par discipline'):
    plot_graph2()
    
    
def plot_graph3():
  
    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df3.set_index('Secteur disciplinaire')['% femmes'], use_container_width=True)

    # Afficher le tableau sans l'index
    st.write(df3)  

if col3.button('Pourcentage de femmes par Secteur disciplinaire'):
    plot_graph3()
    
    
def plot_graph4():
  
    # Créer un graphique en barres avec les pourcentages de femmes
    st.bar_chart(df4.set_index('Diplôme')['% femmes'], use_container_width=True)

    # Afficher le tableau sans l'index
    st.write(df4)  

if col4.button('Pourcentage de femmes par Diplôme'):
    plot_graph4()
    
    
    
    
