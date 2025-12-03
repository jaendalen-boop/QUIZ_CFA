import streamlit as st

# -----------------------
# CONFIG STREAMLIT (doit être en tout premier)
# -----------------------
st.set_page_config(
    page_title="Quiz CAP Boucher",
    page_icon="🥩",
    layout="centered"
)

# On importe directement tes données de quiz
from quiz_cap_boucher_100 import quiz_data


# -----------------------
# 1) INITIALISATION DU STATE
# -----------------------

if "current_theme" not in st.session_state:
    st.session_state.current_theme = None  # numéro de thème (1, 2, 3, 4, 5)
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "theme_scores" not in st.session_state:
    # dictionnaire : {1: "5/20", 2: "10/20", ...}
    st.session_state.theme_scores = {num: None for num in quiz_data["themes"].keys()}
if "show_correction" not in st.session_state:
    st.session_state.show_correction = False
if "last_is_correct" not in st.session_state:
    st.session_state.last_is_correct = None


# -----------------------
# 2) FONCTIONS UTILES
# -----------------------

def start_theme(theme_number: int):
    """Lance un thème : remet l'index de question et le score à zéro."""
    st.session_state.current_theme = theme_number
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None


def go_back_to_menu():
    """Retour au menu principal."""
    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None


def get_current_question():
    """Retourne la question en cours en fonction du thème et de l'index."""
    theme = quiz_data["themes"][st.session_state.current_theme]
    questions = theme["questions"]
    idx = st.session_state.current_question_index
    if 0 <= idx < len(questions):
        return questions[idx]
    return None


# -----------------------
# 3) INTERFACE : MENU PRINCIPAL
# -----------------------

def show_main_menu():
    st.title(quiz_data.get("title", "Quiz CAP Boucher"))

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

        # Bouton pour lancer le thème (adapté au tactile)
        if st.button(f"Commencer le thème {num}", key=f"btn_theme_{num}"):
            start_theme(num)
            st.rerun()


# -----------------------
# 4) INTERFACE : ÉCRAN D’UNE QUESTION
# -----------------------

def show_question_screen():
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
            go_back_to_menu()
            st.rerun()
        return

    # Champs utilisés dans ton fichier :
    # "questionNumber", "question", "answerOptions", "correction"
    st.write("### " + q["question"])

    options_text = [opt["text"] for opt in q["answerOptions"]]

    # Radio sans index=None (compatible versions plus anciennes)
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
        if st.button("Retour au menu"):
            go_back_to_menu()
            st.rerun()

    # Zone de feedback / correction
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
# 5) ÉCRAN DE RÉSULTAT D’UN THÈME
# -----------------------

def show_theme_result():
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    total_questions = len(theme["questions"])
    score = st.session_state.score

    st.title(f"Résultat : {theme_name}")
    st.success(f"Votre score : {score}/{total_questions}")

    if st.button("Revenir au menu principal"):
        go_back_to_menu()
        st.rerun()


# -----------------------
# 6) POINT D’ENTRÉE STREAMLIT
# -----------------------

def main():
    if st.session_state.current_theme is None:
        show_main_menu()
    else:
        theme = quiz_data["themes"][st.session_state.current_theme]
        if st.session_state.current_question_index >= len(theme["questions"]):
            show_theme_result()
        else:
            show_question_screen()


if __name__ == "__main__":
    main()
