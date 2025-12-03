import streamlit as st

# -----------------------
# CONFIG STREAMLIT
# -----------------------
st.set_page_config(
    page_title="Quiz CFA",
    page_icon="🥩",
    layout="centered"
)

# -----------------------
# IMPORT DES QUIZ DISPONIBLES
# -----------------------
# Pour l'instant, un seul quiz. Plus tard, tu pourras créer d'autres fichiers
# (ex: quiz_cap_menuisier.py) et les ajouter ici.
from quizzes.quiz_cap_boucher_100 import quiz_data as quiz_boucher_data

# Dictionnaire des quiz disponibles : clé = identifiant interne, valeur = dict info
QUIZZES = {
    "cap_boucher_100": {
        "title": "CAP Boucher – 100 questions",
        "description": "Révisions complètes 2ème année : anatomie, hygiène, désossage, technologie, législation.",
        "data": quiz_boucher_data,
        "icon": "🥩",
    },
    # Exemple futur :
    # "cap_menuisier": {
    #     "title": "CAP Menuisier – 50 questions",
    #     "description": "Quiz sur les techniques de menuiserie, matériaux, sécurité.",
    #     "data": quiz_menuisier_data,
    #     "icon": "🪵",
    # },
}

# -----------------------
# STATE GLOBAL
# -----------------------

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


# -----------------------
# FONCTIONS : GESTION DU QUIZ COURANT
# -----------------------

def get_current_quiz_data():
    """Retourne le quiz_data du quiz sélectionné."""
    if st.session_state.selected_quiz_key is None:
        return None
    return QUIZZES[st.session_state.selected_quiz_key]["data"]


def reset_quiz_state_for_selected_quiz():
    """Réinitialise l'état pour le quiz sélectionné."""
    quiz_data = get_current_quiz_data()
    if not quiz_data:
        return
    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    # Crée un dict de scores vide pour chaque thème du quiz choisi
    st.session_state.theme_scores = {
        num: None for num in quiz_data["themes"].keys()
    }
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None


def start_theme(theme_number: int):
    """Lance un thème : remet l'index de question et le score à zéro."""
    st.session_state.current_theme = theme_number
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None


def go_back_to_main_menu():
    """Retour au menu des thèmes pour le quiz courant."""
    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None


def get_current_question():
    """Retourne la question en cours en fonction du thème et de l'index."""
    quiz_data = get_current_quiz_data()
    theme = quiz_data["themes"][st.session_state.current_theme]
    questions = theme["questions"]
    idx = st.session_state.current_question_index
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
    quiz_data = get_current_quiz_data()
    if not quiz_data:
        st.error("Aucun quiz sélectionné.")
        return

    st.title(quiz_data.get("title", "Quiz"))

    # Bouton pour revenir au choix de quiz
    if st.button("⬅️ Retour au menu des quiz"):
        st.session_state.selected_quiz_key = None
        st.rerun()

    st.subheader("Progression globale")
    total_questions = 0
    total_correct = 0
    all_completed = True

    for num, theme in quiz_data["themes"].items():
        questions = theme["questions"]
        total_questions += len(questions)
        theme_score = st.session_state.theme_scores.get(num)
        if theme_score is not None:
            correct, total = theme_score.split("/")
            total_correct += int(correct)
        else:
            all_completed = False

    st.write(f"Score cumulé : **{total_correct}/{total_questions}**")
    if all_completed and total_questions > 0:
        st.success("🎉 Tous les thèmes complétés !")

    st.subheader("Choisissez un thème")

    for num, theme in quiz_data["themes"].items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{num}) {theme['name']}**")
        with col2:
            theme_score = st.session_state.theme_scores.get(num)
            if theme_score:
                st.success(f"Complété ({theme_score})")
            else:
                st.warning("Non fait")

        if st.button(f"Commencer le thème {num}", key=f"btn_theme_{num}"):
            start_theme(num)
            st.rerun()


# -----------------------
# INTERFACE : ÉCRAN D’UNE QUESTION
# -----------------------

def show_question_screen():
    quiz_data = get_current_quiz_data()
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    questions = theme["questions"]
    idx = st.session_state.current_question_index
    total_questions = len(questions)

    st.title(theme_name)
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
    quiz_data = get_current_quiz_data()
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    total_questions = len(theme["questions"])
    score = st.session_state.score

    st.title(f"Résultat : {theme_name}")
    st.success(f"Votre score : {score}/{total_questions}")

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
