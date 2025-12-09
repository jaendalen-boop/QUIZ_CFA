import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Quiz CFA",
    page_icon="🎓",
    layout="centered"
)

# -----------------------
# IMPORT DES QUIZ DISPONIBLES
# -----------------------
from quizzes.quiz_cap_boucher_100 import quiz_data as quiz_boucher_data
from quizzes.quiz_cap_boulanger_100 import quiz_data as quiz_boulanger_data
from quizzes.quiz_cap_coiffure_100 import quiz_data as quiz_coiffure_data
from quizzes.quiz_cap_charcutier_traiteur_100 import quiz_data as quiz_charcutier_traiteur_data
from quizzes.quiz_cap_peinture_carrosserie_100 import quiz_data as quiz_peinture_carrosserie_data
from quizzes.quiz_cap_boulanger_100 import quiz_data as quiz_boulanger_data
from quizzes.quiz_cap_coiffure_100 import quiz_data as quiz_coiffure_data
from quizzes.quiz_cap_peinture_carrosserie_100 import quiz_data as quiz_peinture_carrosserie_data
from quizzes.quiz_cap_carrosserie_100 import quiz_data as quiz_carrosserie_data
from quizzes.quiz_cap_cuisine_100 import quiz_data as quiz_cuisine_data
from quizzes.quiz_cap_electricite_100 import quiz_data as quiz_electricite_data
from quizzes.quiz_cap_employe_polyvalent_commerce_100 import quiz_data as quiz_epc_data
from quizzes.quiz_cap_macon_100 import quiz_data as quiz_macon_data
from quizzes.quiz_cap_meca_vp_100 import quiz_data as quiz_meca_vp_data
from quizzes.quiz_cap_menuisier_fabricant_100 import quiz_data as quiz_menuisier_fabricant_data
from quizzes.quiz_cap_menuisier_installateur_100 import quiz_data as quiz_menuisier_installateur_data
from quizzes.quiz_cap_patissier_100 import quiz_data as quiz_patissier_data
from quizzes.quiz_cap_peintre_100 import quiz_data as quiz_peintre_data
from quizzes.quiz_cap_platre_isolation_100 import quiz_data as quiz_platre_isolation_data
from quizzes.quiz_cap_sanitaire_100 import quiz_data as quiz_sanitaire_data
from quizzes.quiz_cap_serrurier_metallier_100 import quiz_data as quiz_serrurier_data
from quizzes.quiz_cap_thermique_100 import quiz_data as quiz_thermique_data
from quizzes.quiz_cap_carreleur_100 import quiz_data as quiz_carreleur_data

QUIZZES = {
    "cap_boucher_100": {
        "title": "CAP Boucher – 100 questions",
        "description": "Révisions complètes CAP Boucher.",
        "data": quiz_boucher_data,
        "icon": "🥩",
        "color": "#e74c3c",
    },
    "cap_boulanger_100": {
        "title": "CAP Boulanger – 100 questions",
        "description": "Révisions complètes CAP Boulanger.",
        "data": quiz_boulanger_data,
        "icon": "🥖",
        "color": "#f39c12",
    },
    "cap_carrosserie_100": {
        "title": "CAP Carrosserie – 100 questions",
        "description": "Révisions complètes CAP Carrosserie.",
        "data": quiz_carrosserie_data,
        "icon": "🔧",
        "color": "#34495e",
    
    },
    "cap_charcutier_traiteur_100": {
        "title": "CAP Charcutier-Traiteur – 100 questions",
        "description": "Révisions complètes CAP Charcutier-Traiteur.",
        "data": quiz_charcutier_traiteur_data,
        "icon": "🍖",
        "color": "#c0392b",
    },
    "cap_coiffure_100": {
        "title": "CAP Coiffure – 100 questions",
        "description": "Révisions complètes CAP Coiffure.",
        "data": quiz_coiffure_data,
        "icon": "💇",
        "color": "#9b59b6",
    },
    "cap_cuisine_100": {
        "title": "CAP Cuisine – 100 questions",
        "description": "Révisions complètes CAP Cuisine.",
        "data": quiz_cuisine_data,
        "icon": "👨‍🍳",
        "color": "#e67e22",
    },
    "cap_electricite_100": {
        "title": "CAP Électricité – 100 questions",
        "description": "Révisions complètes CAP Électricité.",
        "data": quiz_electricite_data,
        "icon": "⚡",
        "color": "#f1c40f",
    },
    "cap_employe_polyvalent_commerce_100": {
        "title": "CAP Employé Polyvalent Commerce – 100 questions",
        "description": "Révisions complètes CAP EPC.",
        "data": quiz_epc_data,
        "icon": "🛒",
        "color": "#16a085",
    },
    "cap_macon_100": {
        "title": "CAP Maçon – 100 questions",
        "description": "Révisions complètes CAP Maçon.",
        "data": quiz_macon_data,
        "icon": "🧱",
        "color": "#95a5a6",
    },
    "cap_meca_vp_100": {
        "title": "CAP Mécanique VP – 100 questions",
        "description": "Révisions complètes CAP Mécanique.",
        "data": quiz_meca_vp_data,
        "icon": "🔩",
        "color": "#34495e",
    },
    "cap_menuisier_fabricant_100": {
        "title": "CAP Menuisier Fabricant – 100 questions",
        "description": "Révisions complètes CAP Menuisier Fabricant.",
        "data": quiz_menuisier_fabricant_data,
        "icon": "🪚",
        "color": "#8b4513",
    },
    "cap_menuisier_installateur_100": {
        "title": "CAP Menuisier Installateur – 100 questions",
        "description": "Révisions complètes CAP Menuisier Installateur.",
        "data": quiz_menuisier_installateur_data,
        "icon": "🪛",
        "color": "#a0522d",
    },
    "cap_patissier_100": {
        "title": "CAP Pâtissier – 100 questions",
        "description": "Révisions complètes CAP Pâtissier.",
        "data": quiz_patissier_data,
        "icon": "🍰",
        "color": "#e91e63",
    },
    "cap_peintre_100": {
        "title": "CAP Peintre – 100 questions",
        "description": "Révisions complètes CAP Peintre.",
        "data": quiz_peintre_data,
        "icon": "🎨",
        "color": "#673ab7",
    },
    "cap_peinture_carrosserie_100": {
        "title": "CAP Peinture en Carrosserie – 100 questions",
        "description": "Révisions complètes CAP Peinture Carrosserie.",
        "data": quiz_peinture_carrosserie_data,
        "icon": "🚗",
        "color": "#3498db",
    },
    "cap_platre_isolation_100": {
        "title": "CAP Plâtre & Isolation – 100 questions",
        "description": "Révisions complètes CAP Plâtre Isolation.",
        "data": quiz_platre_isolation_data,
        "icon": "🏗️",
        "color": "#bdc3c7",
    },
    "cap_sanitaire_100": {
        "title": "CAP Sanitaire – 100 questions",
        "description": "Révisions complètes CAP Sanitaire.",
        "data": quiz_sanitaire_data,
        "icon": "🚰",
        "color": "#3498db",
    },
    "cap_serrurerier_metallier_100": {
        "title": "CAP Serrurerie-Métallier – 100 questions",
        "description": "Révisions complètes CAP Serrurerie.",
        "data": quiz_serrurier_data,
        "icon": "🔑",
        "color": "#7f8c8d",
    },
    "cap_thermique_100": {
        "title": "CAP Thermique – 100 questions",
        "description": "Révisions complètes CAP Thermique.",
        "data": quiz_thermique_data,
        "icon": "🔥",
        "color": "#e74c3c",
    },
"cap_carreleur_100": {
    "title": "CAP Carreleur – 100 questions",
    "description": "Révisions complètes CAP Carreleur.",
    "data": quiz_carreleur_data,
    "icon": "🧱",
    "color": "#2ecc71",
    },
}

# Couleurs par numéro de thème
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

if "selected_quiz_key" not in st.session_state:
    st.session_state.selected_quiz_key = None
if "current_theme" not in st.session_state:
    st.session_state.current_theme = None
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

    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None
    st.session_state.shuffled_questions = None

    if st.session_state.theme_scores is None or not isinstance(st.session_state.theme_scores, dict):
        st.session_state.theme_scores = {}
    
    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    
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
    
    if st.session_state.shuffled_questions:
        questions = st.session_state.shuffled_questions
    else:
        quiz_data = get_current_quiz_data()
        theme = quiz_data["themes"][st.session_state.current_theme]
        questions = theme["questions"]
    
    if 0 <= idx < len(questions):
        return questions[idx]
    return None


def generate_score_summary():
    """Génère un récapitulatif textuel des scores pour export."""
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    quiz_info = QUIZZES[quiz_key]
    quiz_scores = st.session_state.theme_scores.get(quiz_key, {})
    
    lines = []
    lines.append("=" * 50)
    lines.append(f"📊 RÉCAPITULATIF - {quiz_info['title']}")
    lines.append(f"Date : {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    lines.append("=" * 50)
    lines.append("")
    
    total_score = 0
    total_max = 0
    
    for num, theme in quiz_data["themes"].items():
        theme_name = theme["name"]
        total_max += len(theme["questions"])
        score_str = quiz_scores.get(num, "Non fait")
        
        if score_str and score_str != "Non fait":
            try:
                score_val = int(score_str.split("/")[0])
                total_score += score_val
            except:
                pass
        
        lines.append(f"Thème {num} : {theme_name}")
        lines.append(f"  Score : {score_str}")
        lines.append("")
    
    lines.append("=" * 50)
    lines.append(f"SCORE TOTAL : {total_score}/{total_max}")
    
    if total_max > 0:
        percentage = (total_score / total_max) * 100
        lines.append(f"Pourcentage : {percentage:.1f}%")
    
    lines.append("=" * 50)
    
    return "\n".join(lines)


# -----------------------
# INTERFACE : SÉLECTEUR DE QUIZ
# -----------------------

def show_quiz_selector():
    st.title("Quiz CFA – Centre de Foix")
    st.subheader("Choisissez un quiz")

    for key, info in QUIZZES.items():
        color = info.get("color", "#666")
        
        # Carte avec couleur de fond légère et bordure colorée
        st.markdown(f"""
            <style>
            .quiz-card-{key} {{
                background: linear-gradient(135deg, {color}15, {color}05);
                border-left: 5px solid {color};
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                transition: transform 0.2s, box-shadow 0.2s;
            }}
            .quiz-card-{key}:hover {{
                transform: translateY(-3px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }}
            </style>
        """, unsafe_allow_html=True)
        
        with st.container():
            st.markdown(f'<div class="quiz-card-{key}">', unsafe_allow_html=True)
            cols = st.columns([1, 5])
            with cols[0]:
                st.markdown(f"<h1 style='font-size:3rem;margin:0;'>{info.get('icon', '')}</h1>", unsafe_allow_html=True)
            with cols[1]:
                st.markdown(f"**{info['title']}**")
                st.write(info["description"])
                if st.button(f"Lancer ce quiz", key=f"select_quiz_{key}"):
                    st.session_state.selected_quiz_key = key
                    reset_quiz_state_for_selected_quiz()
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

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

    if st.button("🔙 Retour au menu des quiz"):
        st.session_state.selected_quiz_key = None
        st.rerun()

    st.subheader("Progression globale")
    total_score = 0
    total_max = 0
    all_completed = True
    
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
        
        if st.button(f"Commencer le thème {num}", key=f"btn_theme_{num}"):
            start_theme(num)
            st.rerun()
        
        st.write("")


# -----------------------
# INTERFACE : ÉCRAN DE QUESTION
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
    
    # En-tête sans timer
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

    # -----------------------------
    # MÉLANGE ALÉATOIRE DES RÉPONSES
    # -----------------------------
    if "shuffled_answers" not in st.session_state:
        st.session_state.shuffled_answers = {}

    q_id = f"{theme_number}_{idx}"  # identifiant unique pour la question courante

    if q_id not in st.session_state.shuffled_answers:
        # copie indépendante pour ne pas modifier les datas source
        options = [opt.copy() for opt in q["answerOptions"]]
        random.shuffle(options)
        # réattribue des keys A/B/C/D si tu veux les garder cohérentes
        for i, opt in enumerate(options):
            opt["key"] = chr(ord("A") + i)
        st.session_state.shuffled_answers[q_id] = options

    answer_options = st.session_state.shuffled_answers[q_id]
    options_text = [opt["text"] for opt in answer_options]
    # -----------------------------

    # États supplémentaires pour verrouiller la réponse
    if "answer_locked" not in st.session_state:
        st.session_state.answer_locked = False
    if "selected_answer" not in st.session_state:
        st.session_state.selected_answer = None

    st.write(q["question"])

    # Avant validation : radio actif
    if not st.session_state.answer_locked:
        selected = st.radio(
            "Choisissez une réponse :",
            options=options_text,
            key=f"q_{theme_number}_{idx}"
        )
        st.session_state.selected_answer = selected

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Valider la réponse"):
                if not st.session_state.selected_answer:
                    st.warning("Veuillez sélectionner une réponse.")
                else:
                    # On cherche la bonne option dans la liste mélangée
                    correct_option = next(
                        (opt for opt in answer_options if opt["isCorrect"]), None
                    )
                    is_correct = (
                        correct_option is not None
                        and st.session_state.selected_answer == correct_option["text"]
                    )
                    st.session_state.last_is_correct = is_correct
                    st.session_state.show_correction = True
                    st.session_state.answer_locked = True
                    if is_correct:
                        st.session_state.score += 1
                    st.rerun()

        with col2:
            if st.button("Retour au menu des thèmes"):
                go_back_to_main_menu()
                st.rerun()

    # Après validation : réponse figée + correction
    else:
        st.write(f"Votre réponse : {st.session_state.selected_answer}")

        col1, col2 = st.columns(2)

        with col2:
            if st.button("Retour au menu des thèmes"):
                go_back_to_main_menu()
                st.rerun()

        if st.session_state.show_correction:
            correct_option = next(
                (opt for opt in answer_options if opt["isCorrect"]), None
            )

            if st.session_state.last_is_correct is True:
                st.markdown(
                    """
                    <div style='background-color:#d4edda;border-left:5px solid #28a745;padding:1rem;border-radius:8px;margin:1rem 0;'>
                        <h3 style='color:#155724;margin:0;'>✅ Bonne réponse !</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif st.session_state.last_is_correct is False:
                st.markdown(
                    f"""
                    <div style='background-color:#f8d7da;border-left:5px solid #dc3545;padding:1rem;border-radius:8px;margin:1rem 0;'>
                        <h3 style='color:#721c24;margin:0 0 0.5rem 0;'>❌ Mauvaise réponse</h3>
                        <p style='margin:0;color:#721c24;'><strong>La bonne réponse était :</strong> {correct_option['text'] if correct_option else 'N/A'}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # Affichage du cours dans une carte bleue
            if "correction" in q and q["correction"]:
                st.markdown(
                    f"""
                    <div style='background-color:#d1ecf1;border-left:5px solid #17a2b8;padding:1rem;border-radius:8px;margin:1rem 0;'>
                        <h4 style='color:#0c5460;margin:0 0 0.5rem 0;'>📚 Cours</h4>
                        <div style='color:#0c5460;'>{q['correction']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        if st.button("Question suivante ➡️"):
            st.session_state.show_correction = False
            st.session_state.last_is_correct = None
            st.session_state.current_question_index += 1
            st.session_state.answer_locked = False
            st.session_state.selected_answer = None

            # on nettoie l'ordre mélangé de la question précédente
            if q_id in st.session_state.shuffled_answers:
                del st.session_state.shuffled_answers[q_id]

            if st.session_state.current_question_index >= total_questions:
                show_theme_result()
            else:
                st.rerun()


# -----------------------
# INTERFACE : RÉSULTAT DU THÈME
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
    
    percentage = (score / total_questions) * 100
    
    if percentage == 100:
        st.balloons()
        st.success(f"🎉 Parfait ! Votre score : {score}/{total_questions} ({percentage:.0f}%)")
    elif percentage >= 75:
        st.success(f"👍 Très bien ! Votre score : {score}/{total_questions} ({percentage:.0f}%)")
    elif percentage >= 50:
        st.info(f"🆗 Pas mal ! Votre score : {score}/{total_questions} ({percentage:.0f}%)")
    else:
        st.warning(f"📚 Votre score : {score}/{total_questions} ({percentage:.0f}%) - Révise encore ce thème !")

    # Enregistrer le score pour ce thème du quiz courant
    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    st.session_state.theme_scores[quiz_key][theme_number] = f"{score}/{total_questions}"

    # Boutons d'action
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔙 Revenir au menu des thèmes"):
            go_back_to_main_menu()
            st.rerun()
    
    with col2:
        if st.button("🔄 Refaire ce thème"):
            start_theme(theme_number)
            st.rerun()
    
    st.write("")
    
    # Bouton téléchargement récapitulatif
    summary_text = generate_score_summary()
    st.download_button(
        label="📄 Télécharger le récapitulatif complet",
        data=summary_text,
        file_name=f"recap_quiz_{quiz_key}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain"
    )


# -----------------------
# FONCTION PRINCIPALE
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
