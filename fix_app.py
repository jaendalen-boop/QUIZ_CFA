# fix_app.py - Script de correction automatique

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Correction 1
content = content.replace(
    "margin:1rem 0;'>Votre réponse :",
    "margin:0.3rem 0;'>Votre réponse :"
)

# Correction 2
content = content.replace(
    "padding:1rem;\n                    margin-bottom:0.8rem;",
    "padding:0.6rem;\n                    margin-bottom:0.3rem;"
)

# Correction 3 - Message "Bonne réponse"
content = content.replace(
    "padding:1.2rem;\n                        border-radius:12px;\n                        margin:1.5rem 0;\n                        color:#155724;\n                        animation:fadeIn 0.3s ease-in;\n                    '>\n                        <h3 style='color:#155724;margin:0;font-size:1.3rem;'>✅ Bonne réponse !",
    "padding:0.8rem;\n                        border-radius:12px;\n                        margin:0.6rem 0;\n                        color:#155724;\n                        animation:fadeIn 0.3s ease-in;\n                    '>\n                        <h3 style='color:#155724;margin:0;font-size:1.1rem;'>✅ Bonne réponse !"
)

# Correction 4 - Message "Mauvaise réponse" (PREMIÈRE OCCURRENCE)
content = content.replace(
    "padding:1.2rem;\n                        border-radius:12px;\n                        margin:1.5rem 0;\n                        color:#721c24;\n                        animation:fadeIn 0.3s ease-in;\n                    '>\n                        <h3 style='color:#721c24;margin:0 0 0.5rem 0;font-size:1.3rem;'>❌ Mauvaise réponse</h3>\n                        <p style='margin:0;color:#721c24;'><strong>La bonne réponse était :",
    "padding:0.8rem;\n                        border-radius:12px;\n                        margin:0.6rem 0;\n                        color:#721c24;\n                        animation:fadeIn 0.3s ease-in;\n                    '>\n                        <h3 style='color:#721c24;margin:0 0 0.3rem 0;font-size:1.1rem;'>❌ Mauvaise réponse</h3>\n                        <p style='margin:0;color:#721c24;font-size:0.95rem;'><strong>La bonne réponse était :",
    1  # Remplacer une seule fois
)

# Correction 5 - Bloc Cours
content = content.replace(
    "padding:1.5rem;\n                        border-radius:12px;\n                        margin:1.5rem 0;\n                        box-shadow:0 4px 12px rgba(0,0,0,0.1);\n                        color:#006064;\n                        animation:fadeIn 0.4s ease-in;\n                    '>\n                        <h4 style='color:#006064;margin:0 0 0.8rem 0;font-size:1.2rem;display:flex;align-items:center;'>\n                            <span style='font-size:1.5rem;margin-right:0.5rem;'>📚</span> Cours\n                        </h4>\n                        <div style='color:#00363a;line-height:1.6;'>{q['correction']}</div>",
    "padding:1rem;\n                        border-radius:12px;\n                        margin:0.8rem 0;\n                        box-shadow:0 4px 12px rgba(0,0,0,0.1);\n                        color:#006064;\n                        animation:fadeIn 0.4s ease-in;\n                    '>\n                        <h4 style='color:#006064;margin:0 0 0.5rem 0;font-size:1rem;display:flex;align-items:center;'>\n                            <span style='font-size:1.2rem;margin-right:0.5rem;'>📚</span> Cours\n                        </h4>\n                        <div style='color:#00363a;line-height:1.5;font-size:0.95rem;'>{q['correction']}</div>"
)

# Correction 6 - Espacement et colonnes
content = content.replace(
    "st.markdown(\"<div style='margin-top:1.5rem;'></div>\", unsafe_allow_html=True)\n        \n        col1, col2 = st.columns(2)",
    "st.markdown(\"<div style='margin-top:0.6rem;'></div>\", unsafe_allow_html=True)\n        \n        col1, col2 = st.columns(2, gap=\"small\")"
)

# Sauvegarder
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ app.py corrigé avec succès !")
print("Vous pouvez maintenant lancer: streamlit run app.py")
