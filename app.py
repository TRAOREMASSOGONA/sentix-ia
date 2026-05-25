import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Sentix - IA Sentiment", page_icon="📊")
st.title("📊 Sentix : L'IA d'Analyse de Sentiment Client")
st.write("Bienvenue sur mon tout premier projet d'IA réalisé en parcours MIAGE !")

# 2. L'interface utilisateur
st.subheader("🤖 Testez l'application en direct")
ma_phrase = st.text_input("Tapez un avis client à analyser :", "Ce n'est pas bon")

if st.button("Analyser le sentiment"):
    phrase_minuscule = ma_phrase.lower()
    
    # Listes de mots et d'expressions
    expressions_negatives = ["pas bon", "pas bien", "plus bon", "pas top", "nul", "horreur", "arnaque", "déçu"]
    mots_positifs = ["bon", "super", "fantastique", "adore", "excellent", "parfait", "bien", "rapide"]
    
    score_positif = 0
    score_negatif = 0
    
    # 1. On vérifie d'abord les expressions négatives de deux mots (ex: "pas bon")
    for expr in expressions_negatives:
        if expr in phrase_minuscule:
            score_negatif += 2
            # On enlève l'expression pour ne pas retester le mot "bon" tout seul après
            phrase_minuscule = phrase_minuscule.replace(expr, "")
            
    # 2. On vérifie le reste des mots positifs
    for mot in mots_positifs:
        if mot in phrase_minuscule:
            score_positif += 1
            
    # 3. Decision de l'IA
    if score_negatif > score_positif:
        st.error("Résultat : **Sentiment NÉGATIF !** 😡")
    elif score_positif > score_negatif:
        st.success("Résultat : **Sentiment POSITIF !** 😊")
    else:
        st.info("Résultat : **Sentiment NEUTRE !** 😐")


