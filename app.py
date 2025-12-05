import streamlit as st

st.set_page_config(
    page_title="Quiz CFA",
    page_icon="🎓",
    layout="centered"
)

# --- IMPORT DES QUIZ DISPONIBLES ---
from quizzes.quiz_cap_boucher_100 import quiz_data as quiz_boucher_data
from quizzes.quiz_cap_boulanger_100 import quiz_data as quiz_boulanger_data
from quizzes.quiz_cap_coiffure_100 import quiz_data as quiz_coiffure_data
from quizzes.quiz_cap_charcutier_traiteur_100 import quiz_data as quiz_charcutier_traiteur_data
from quizzes.quiz_cap_peinture_carrosserie_100 import quiz_data as quiz_peinture_carrosserie_data

QUIZZES = {
    "cap_boucher_100": {
        "title": "CAP Boucher – 100 questions",
        "description": "Révisions complètes 2ème année.",
        "data": quiz_boucher_data,
        "icon": "🥩",
    },
    "cap_boulanger_100": {
        "title": "CAP Boulanger – 100 questions",
        "description": "Révisions complètes CAP Boulanger.",
        "data": quiz_boulanger_data,
        "icon": "🥖",
    },
    "cap_coiffure_100": {
        "title": "CAP Coiffure – 100 questions",
        "description": "Révisions complètes CAP Coiffure.",
        "data": quiz_coiffure_data,
        "icon": "💇‍♀️",
    },
    "cap_charcutier_traiteur_100": {
        "title": "CAP Charcutier-Traiteur – 100 questions",
        "description": "Révisions complètes CAP Charcutier-Traiteur.",
        "data": quiz_charcutier_traiteur_data,
        "icon": "🍖",
    },
    "cap_peinture_carrosserie_100": {
        "title": "CAP Peinture en Carrosserie – 100 questions",
        "description": "Révisions complètes CAP Peinture en carrosserie.",
        "data": quiz_peinture_carrosserie_data,
        "icon": "🚗",
    },
}

# Couleurs par numéro de thème (si un thème 6 existe, on reprendra la dernière couleur)
THEME_COLORS = {
    1: "#4f46e5",  # bleu/violet
    2: "#16a34a",  # vert
    3: "#ea580c",  # orange
    4: "#0ea5e9",  # bleu clair
    5: "#e11d48",  # rose/rouge
}


# -----------------------
# STATE GLOBAL
# -----------------------

import random

if "selected_quiz_key" not in st.session_state:
    st.session_state.selected_quiz_key = None  # ex: "cap_boucher_100"
if "current_theme" not in st.session_state:
    st.session_state.current_theme = None  # numéro de thème (1, 2, 3, 4, 5)
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "theme_scores" not in st.session_state:
    st.session_state.theme_scores = {}
if "show_correction" not in st.session_state:
    st.session_state.show_correction = False
if "last_is_correct" not in st.session_state:
    st.session_state.last_is_correct = None
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = None


# -----------------------
# FONCTIONS : GESTION DU QUIZ COURANT
# -----------------------

def get_current_quiz_data():
    """Retourne le quiz_data du quiz sélectionné."""
    if st.session_state.selected_quiz_key is None:
        return None
    return QUIZZES[st.session_state.selected_quiz_key]["data"]


def reset_quiz_state_for_selected_quiz():
    """Réinitialise l'état de session pour le quiz sélectionné (sans effacer les scores globaux)."""
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    if not quiz_data or not quiz_key:
        return

    # état de la session en cours
    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None
    st.session_state.shuffled_questions = None

    # initialisation du dict de scores pour ce quiz si besoin
    if st.session_state.theme_scores is None or not isinstance(st.session_state.theme_scores, dict):
        st.session_state.theme_scores = {}
    
    # créer l'entrée pour ce quiz s'il n'existe pas
    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    
    # initialiser chaque thème à None si pas encore fait
    for num in quiz_data["themes"].keys():
        if num not in st.session_state.theme_scores[quiz_key]:
            st.session_state.theme_scores[quiz_key][num] = None


def start_theme(theme_number: int):
    """Lance un thème, remet l'index de question et le score à zéro, et mélange les questions."""
    quiz_data = get_current_quiz_data()
    theme = quiz_data["themes"][theme_number]
    questions = theme["questions"]
    
    # Créer une copie mélangée des questions
    shuffled = questions.copy()
    random.shuffle(shuffled)
    
    st.session_state.current_theme = theme_number
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None
    st.session_state.shuffled_questions = shuffled


def go_back_to_main_menu():
    """Retour au menu des thèmes pour le quiz courant (sans effacer les scores)."""
    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None
    st.session_state.shuffled_questions = None


def get_current_question():
    """Retourne la question en cours (depuis la liste mélangée si disponible)."""
    idx = st.session_state.current_question_index
    
    # Utiliser les questions mélangées si disponibles
    if st.session_state.shuffled_questions:
        questions = st.session_state.shuffled_questions
    else:
        # Fallback si pas de mélange (ne devrait pas arriver)
        quiz_data = get_current_quiz_data()
        theme = quiz_data["themes"][st.session_state.current_theme]
        questions = theme["questions"]
    
    if 0 <= idx < len(questions):
        return questions[idx]
    return None



# -----------------------
# INTERFACE : MENU GLOBAL DE SÉLECTION DE QUIZ
# -----------------------

def show_quiz_selector():
    st.title("Quiz CFA – Centre de Foix")

    st.subheader("Choisissez un quiz")

    # Liste des quiz avec description
    for key, info in QUIZZES.items():
        with st.container(border=True):
            cols = st.columns([1, 5])
            with cols[0]:
                st.markdown(f"### {info.get('icon', '❓')}")
            with cols[1]:
                st.markdown(f"### {info['title']}")
                st.write(info["description"])
                if st.button(f"Lancer ce quiz", key=f"select_quiz_{key}"):
                    st.session_state.selected_quiz_key = key
                    reset_quiz_state_for_selected_quiz()
                    st.rerun()


# -----------------------
# INTERFACE : MENU DES THÈMES (POUR LE QUIZ COURANT)
# -----------------------

def show_main_menu_for_current_quiz():
    """Affiche la liste des thèmes du quiz courant."""
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    if not quiz_data or not quiz_key:
        st.error("Aucune donnée de quiz chargée.")
        return

    st.title(quiz_data["title"])

    # Bouton retour au menu des quiz
    if st.button("🔙 Retour au menu des quiz"):
        st.session_state.selected_quiz_key = None
        st.rerun()

    # Afficher le score cumulé
    st.subheader("Progression globale")
    total_score = 0
    total_max = 0
    all_completed = True
    
    # Récupérer les scores du quiz courant
    quiz_scores = st.session_state.theme_scores.get(quiz_key, {})
    
    for num, theme in quiz_data["themes"].items():
        total_max += len(theme["questions"])
        score_str = quiz_scores.get(num)
        if score_str:
            try:
                score_val = int(score_str.split("/")[0])
                total_score += score_val
            except:
                pass
        else:
            all_completed = False
    
    st.write(f"Score cumulé : {total_score}/{total_max}")
    
    if all_completed and total_max > 0:
        st.success("🎉 Tous les thèmes complétés !")

    # Liste des thèmes
    st.subheader("Choisissez un thème")
    for num, theme in quiz_data["themes"].items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{theme['name']}**")
        with col2:
            theme_score = quiz_scores.get(num)
            if theme_score:
                st.success(f"Complété ({theme_score})")
            else:
                st.warning("Non fait")
        
        # Bouton juste après les colonnes, pour chaque thème
        if st.button(f"Commencer le thème {num}", key=f"btn_theme_{num}"):
            start_theme(num)
            st.rerun()
        
        st.write("")  # petit espacement entre les thèmes


# -----------------------
# INTERFACE : ÉCRAN D’UNE QUESTION
# -----------------------

def show_question_screen():
    quiz_data = get_current_quiz_data()
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    # Utiliser les questions mélangées
if st.session_state.shuffled_questions:
    questions = st.session_state.shuffled_questions
else:
    questions = theme["questions"]

    idx = st.session_state.current_question_index
    total_questions = len(questions)

    color = THEME_COLORS.get(theme_number, "#4f46e5")

    st.markdown(
    f"<h2 style='margin-bottom:0.2rem;'>{theme_name}</h2>"
    f"<div style='height:4px;border-radius:999px;background:{color};margin-bottom:0.8rem;'></div>",
    unsafe_allow_html=True,
)

    progress = (idx + 1) / total_questions
    st.progress(progress)
    st.write(f"Question {idx + 1} / {total_questions}")

    q = get_current_question()
    if q is None:
        st.error("Erreur : question introuvable.")
        if st.button("Retour au menu principal"):
            go_back_to_main_menu()
            st.rerun()
        return

    st.write("### " + q["question"])

    options_text = [opt["text"] for opt in q["answerOptions"]]

    selected = st.radio(
        "Choisissez une réponse :",
        options=options_text,
        key=f"q_{theme_number}_{idx}"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Valider la réponse"):
            if not selected:
                st.warning("Veuillez sélectionner une réponse.")
            else:
                correct_option = next(
                    (opt for opt in q["answerOptions"] if opt["isCorrect"]),
                    None
                )
                is_correct = (correct_option is not None and selected == correct_option["text"])
                st.session_state.last_is_correct = is_correct
                st.session_state.show_correction = True
                if is_correct:
                    st.session_state.score += 1

    with col2:
        if st.button("Retour au menu des thèmes"):
            go_back_to_main_menu()
            st.rerun()

    if st.session_state.show_correction:
        correct_option = next(
            (opt for opt in q["answerOptions"] if opt["isCorrect"]),
            None
        )

        if st.session_state.last_is_correct is True:
            st.success("✅ Bonne réponse !")
        elif st.session_state.last_is_correct is False:
            st.error("❌ Mauvaise réponse.")
            if correct_option:
                st.info(f"La bonne réponse était : **{correct_option['text']}**")

        if "correction" in q and q["correction"]:
            st.markdown(f"💡 **Cours :** {q['correction']}")

        if st.button("Question suivante"):
            st.session_state.show_correction = False
            st.session_state.last_is_correct = None
            st.session_state.current_question_index += 1
            if st.session_state.current_question_index >= total_questions:
                st.session_state.theme_scores[theme_number] = f"{st.session_state.score}/{total_questions}"
                show_theme_result()
            else:
                st.rerun()


# -----------------------
# ÉCRAN DE RÉSULTAT D’UN THÈME
# -----------------------

def show_theme_result():
    """Affiche les résultats finaux du thème et enregistre le score."""
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    total_questions = len(theme["questions"])
    score = st.session_state.score

    st.title(f"Résultat : {theme_name}")
    st.success(f"Votre score : {score}/{total_questions}")

    # ⚠️ AJOUT CRITIQUE : Enregistrer le score pour ce thème du quiz courant
    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    st.session_state.theme_scores[quiz_key][theme_number] = f"{score}/{total_questions}"

    if st.button("Revenir au menu des thèmes"):
        go_back_to_main_menu()
        st.rerun()

# -----------------------
# POINT D’ENTRÉE
# -----------------------

def main():
    # 1) Pas encore de quiz choisi → menu global
    if st.session_state.selected_quiz_key is None:
        show_quiz_selector()
        return

    # 2) Quiz choisi, mais aucun thème en cours → menu des thèmes
    if st.session_state.current_theme is None:
        show_main_menu_for_current_quiz()
        return

    # 3) Quiz + thème en cours → afficher question ou résultat
    quiz_data = get_current_quiz_data()
    theme = quiz_data["themes"][st.session_state.current_theme]
    if st.session_state.current_question_index >= len(theme["questions"]):
        show_theme_result()
    else:
        show_question_screen()


if __name__ == "__main__":
    main()
