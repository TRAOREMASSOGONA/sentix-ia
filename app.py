
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt

# 1. Configuration de la page internet
st.set_page_config(page_title="Sentix - IA Sentiment", page_icon="📊")
st.title("📊 Sentix : L'IA d'Analyse de Sentiment Client")
st.write("Bienvenue sur mon premier projet d'IA réalisé en parcours MIAGE !")

# 2. Entraînement de l'IA en arrière-plan
nouveaux_avis = {
    'avis': [
        "J'adore ce produit, il est fantastique !", "Une horreur, le produit est cassé.",
        "Le produit est correct, mais la livraison est longue.", "Excellente surprise, je recommande !",
        "Nul, ne l'achetez pas, c'est une arnaque.", "Très bon rapport qualité prix.",
        "Ce n'est pas bon du tout, je suis déçu.", "Je pensais que c'était nul, mais c'est super !"
    ],
    'note': [5, 1, 3, 5, 1, 4, 1, 5]
}
df = pd.DataFrame(nouveaux_avis)
df['sentiment'] = df['note'].apply(lambda x: 1 if x > 3 else 0)

vectoriseur = CountVectorizer()
X = vectoriseur.fit_transform(df['avis'].str.lower())
y = df['sentiment']
intelligence_artificielle = MultinomialNB()
intelligence_artificielle.fit(X, y)

# 3. L'interface utilisateur de ton site
st.subheader("🤖 Testez l'application en direct")
ma_phrase = st.text_input("Tapez un avis client à analyser :", "Je trouve ce service fantastique")

if st.button("Analyser le sentiment"):
    phrase_numerique = vectoriseur.transform([ma_phrase.lower()])
    prediction = intelligence_artificielle.predict(phrase_numerique)
    
    if prediction == 1:
        st.success(f"Résultat : **Sentiment POSITIF !** 😊")
    else:
        st.error(f"Résultat : **Sentiment NÉGATIF !** 😡")
