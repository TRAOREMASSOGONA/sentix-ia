import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Sentix - IA Sentiment", page_icon="📊")
st.title("📊 Sentix : L'IA d'Analyse de Sentiment Client")
st.write("Bienvenue sur mon tout premier projet d'IA réalisé en parcours MIAGE !")

# 2. L'interface utilisateur
st.subheader("🤖 Testez l'application en direct")
ma_phrase = st.text_input("Tapez un avis client à analyser :", "Je trouve ce service fantastique")

if st.button("Analyser le sentiment"):
    # Une IA intelligente basée sur des mots-clés simples pour le site web
    phrase_minuscule = ma_phrase.lower()
    
    mots_positifs = ["bon", "super", "fantastique", "adore", "excellent", "parfait", "bien", "rapide"]
    mots_negatifs = ["nul", "horreur", "cassé", "arnaque", "déçu", "mauvais", "lent", "pas"]
    
    score_positif = sum(1 for mot in mots_positifs if mot in phrase_minuscule)
    score_negatif = sum(1 for mot in mots_negatifs if mot in phrase_minuscule)
    
    if score_positif >= score_negatif and score_positif > 0:
        st.success("Résultat : **Sentiment POSITIF !** 😊")
    elif score_negatif > score_positif:
        st.error("Résultat : **Sentiment NÉGATIF !** 😡")
    else:
        st.info("Résultat : **Sentiment NEUTRE !** 😐")

