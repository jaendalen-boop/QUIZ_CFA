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

from quizzes.quiz_bp_arts_de_la_cuisine_100 import quiz_data as quiz_bp_arts_cuisine_data
from quizzes.quiz_bp_boucher_100 import quiz_data as quiz_bp_boucher_data
from quizzes.quiz_bp_coiffure_100 import quiz_data as quiz_bp_coiffure_data
from quizzes.quiz_bp_macon_100 import quiz_data as quiz_bp_macon_data
from quizzes.quiz_bp_migcs_100 import quiz_data as quiz_bp_migcs_data

from quizzes.quiz_bts_meca_vp_100 import quiz_data as quiz_bts_meca_vp_data

from quizzes.quiz_bacpro_mva_100 import quiz_data as quiz_bacpro_mva_data
from quizzes.quiz_bacpro_mcva_100 import quiz_data as quiz_bacpro_mcva_data
from quizzes.quiz_bacpro_mcvb_100 import quiz_data as quiz_bacpro_mcvb_data

from quizzes.quiz_cap_boucher_100 import quiz_data as quiz_cap_boucher_data
from quizzes.quiz_cap_boulanger_100 import quiz_data as quiz_cap_boulanger_data
from quizzes.quiz_cap_carreleur_mosaïste import quiz_data as quiz_cap_carreleur_data
from quizzes.quiz_cap_carrosserie_automobile_100 import quiz_data as quiz_cap_carrosserie_data
from quizzes.quiz_cap_charcutier_traiteur_100 import quiz_data as quiz_cap_charcutier_traiteur_data
from quizzes.quiz_cap_chcr_100 import quiz_data as quiz_cap_chcr_data
from quizzes.quiz_cap_coiffure_100 import quiz_data as quiz_cap_coiffure_data
from quizzes.quiz_cap_couvreur_100 import quiz_data as quiz_cap_couvreur_data
from quizzes.quiz_cap_cuisine_100 import quiz_data as quiz_cap_cuisine_data
from quizzes.quiz_cap_electricien_100 import quiz_data as quiz_cap_electricien_data
from quizzes.quiz_cap_employe_polyvalent_commerce_100 import quiz_data as quiz_cap_epc_data
from quizzes.quiz_cap_macon_100 import quiz_data as quiz_cap_macon_data
from quizzes.quiz_cap_meca_vp_100 import quiz_data as quiz_cap_meca_vp_data
from quizzes.quiz_cap_menuisier_fabricant_100 import quiz_data as quiz_cap_menuisier_fabricant_data
from quizzes.quiz_cap_menuisier_installateur_100 import quiz_data as quiz_cap_menuisier_installateur_data
from quizzes.quiz_cap_patissier_100 import quiz_data as quiz_cap_patissier_data
from quizzes.quiz_cap_peintre_100 import quiz_data as quiz_cap_peintre_data
from quizzes.quiz_cap_peinture_carrosserie_100 import quiz_data as quiz_cap_peinture_carrosserie_data
from quizzes.quiz_cap_platre_isolation_100 import quiz_data as quiz_cap_platre_isolation_data
from quizzes.quiz_cap_sanitaire_100 import quiz_data as quiz_cap_sanitaire_data
from quizzes.quiz_cap_serrurier_metallier_100 import quiz_data as quiz_cap_serrurier_metallier_data
from quizzes.quiz_cap_thermique_100 import quiz_data as quiz_cap_thermique_data

from quizzes.quiz_cs_coiffure_coupe_couleur_100 import quiz_data as quiz_cs_coiffure_coupe_couleur_data


# -----------------------
# DÉFINITION DES QUIZ (TRIÉS ALPHABÉTIQUEMENT PAR CLÉ)
# -----------------------

QUIZZES = {
    # ----- BAC PRO -----
    "bacpro_mcvb_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option B – prospection et valorisation de l’offre commerciale",
        "description": "Révisions complètes Bac Pro MCV option B.",
        "data": quiz_bacpro_mcvb_data,
        "icon": "🛍️",
        "color": "#1abc9c",
    },
    "bacpro_mcva_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option A – animation et gestion de l’espace commercial",
        "description": "Révisions complètes Bac Pro MCV option A.",
        "data": quiz_bacpro_mcva_data,
        "icon": "🏬",
        "color": "#27ae60",
    },
    "bacpro_mva_100": {
        "title": "Bac Pro Maintenance des véhicules option A – voitures particulières",
        "description": "Révisions complètes Bac Pro Maintenance des véhicules (option A – VP).",
        "data": quiz_bacpro_mva_data,
        "icon": "🚗",
        "color": "#2980b9",
    },

    # ----- BP -----
    "bp_arts_de_la_cuisine_100": {
        "title": "BP Arts de la cuisine",
        "description": "Révisions complètes BP Arts de la cuisine.",
        "data": quiz_bp_arts_cuisine_data,
        "icon": "👨‍🍳",
        "color": "#e67e22",
    },
    "bp_boucher_100": {
        "title": "BP Boucher",
        "description": "Révisions complètes BP Boucher.",
        "data": quiz_bp_boucher_data,
        "icon": "🥩",
        "color": "#c0392b",
    },
    "bp_coiffure_100": {
        "title": "BP Coiffure",
        "description": "Révisions complètes BP Coiffure.",
        "data": quiz_bp_coiffure_data,
        "icon": "💇",
        "color": "#9b59b6",
    },
    "bp_macon_100": {
        "title": "BP Maçon",
        "description": "Révisions complètes BP Maçon.",
        "data": quiz_bp_macon_data,
        "icon": "🧱",
        "color": "#7f8c8d",
    },
    "bp_migcs_100": {
        "title": "BP Métiers de l’industrie graphique – communication et services",
        "description": "Révisions complètes BP MIGCS.",
        "data": quiz_bp_migcs_data,
        "icon": "🖨️",
        "color": "#34495e",
    },

    # ----- BTS -----
    "bts_meca_vp_100": {
        "title": "BTS Maintenance des véhicules, option A – voitures particulières",
        "description": "Révisions complètes BTS Maintenance des véhicules (option A – VP).",
        "data": quiz_bts_meca_vp_data,
        "icon": "🚗",
        "color": "#2980b9",
    },

    # ----- CAP -----
    "cap_boucher_100": {
        "title": "CAP Boucher",
        "description": "Révisions complètes CAP Boucher.",
        "data": quiz_cap_boucher_data,
        "icon": "🥩",
        "color": "#e74c3c",
    },
    "cap_boulanger_100": {
        "title": "CAP Boulanger",
        "description": "Révisions complètes CAP Boulanger.",
        "data": quiz_cap_boulanger_data,
        "icon": "🥖",
        "color": "#f39c12",
    },
    "cap_carreleur_mosaiste_100": {
        "title": "CAP Carreleur-mosaïste",
        "description": "Révisions complètes CAP Carreleur-mosaïste.",
        "data": quiz_cap_carreleur_data,
        "icon": "🧱",
        "color": "#2ecc71",
    },
    "cap_carrosserie_automobile_100": {
        "title": "CAP Réparation des carrosseries",
        "description": "Révisions complètes CAP Réparation des carrosseries.",
        "data": quiz_cap_carrosserie_data,
        "icon": "🔧",
        "color": "#34495e",
    },
    "cap_charcutier_traiteur_100": {
        "title": "CAP Charcutier-traiteur",
        "description": "Révisions complètes CAP Charcutier-traiteur.",
        "data": quiz_cap_charcutier_traiteur_data,
        "icon": "🍖",
        "color": "#c0392b",
    },
    "cap_chcr_100": {
        "title": "CAP Commercialisation et services en hôtel-café-restaurant",
        "description": "Révisions complètes CAP Commercialisation et services en hôtel-café-restaurant.",
        "data": quiz_cap_chcr_data,
        "icon": "🍽️",
        "color": "#e67e22",
    },
    "cap_coiffure_100": {
        "title": "CAP Coiffure",
        "description": "Révisions complètes CAP Coiffure.",
        "data": quiz_cap_coiffure_data,
        "icon": "💇",
        "color": "#9b59b6",
    },
    "cap_couvreur_100": {
        "title": "CAP Couvreur",
        "description": "Révisions complètes CAP Couvreur.",
        "data": quiz_cap_couvreur_data,
        "icon": "🏠",
        "color": "#8e44ad",
    },
    "cap_cuisine_100": {
        "title": "CAP Cuisine",
        "description": "Révisions complètes CAP Cuisine.",
        "data": quiz_cap_cuisine_data,
        "icon": "👨‍🍳",
        "color": "#e67e22",
    },
    "cap_electricien_100": {
        "title": "CAP Électricien",
        "description": "Révisions complètes CAP Électricien.",
        "data": quiz_cap_electricien_data,
        "icon": "⚡",
        "color": "#f1c40f",
    },
    "cap_equipier_polyvalent_commerce_100": {
        "title": "CAP Équipier polyvalent du commerce",
        "description": "Révisions complètes CAP Équipier polyvalent du commerce (EPC).",
        "data": quiz_cap_epc_data,
        "icon": "🛒",
        "color": "#16a085",
    },
    "cap_macon_100": {
        "title": "CAP Maçon",
        "description": "Révisions complètes CAP Maçon.",
        "data": quiz_cap_macon_data,
        "icon": "🧱",
        "color": "#95a5a6",
    },
    "cap_meca_vp_100": {
        "title": "CAP Maintenance des véhicules, option A – voitures particulières",
        "description": "Révisions complètes CAP Maintenance des véhicules (option voitures particulières).",
        "data": quiz_cap_meca_vp_data,
        "icon": "🚗",
        "color": "#34495e",
    },
    "cap_menuisier_fabricant_100": {
        "title": "CAP Menuisier fabricant de menuiserie, mobilier et agencement",
        "description": "Révisions complètes CAP Menuisier fabricant.",
        "data": quiz_cap_menuisier_fabricant_data,
        "icon": "🪚",
        "color": "#8b4513",
    },
    "cap_menuisier_installateur_100": {
        "title": "CAP Menuisier installateur",
        "description": "Révisions complètes CAP Menuisier installateur.",
        "data": quiz_cap_menuisier_installateur_data,
        "icon": "🪛",
        "color": "#a0522d",
    },
    "cap_patissier_100": {
        "title": "CAP Pâtissier",
        "description": "Révisions complètes CAP Pâtissier.",
        "data": quiz_cap_patissier_data,
        "icon": "🍰",
        "color": "#e91e63",
    },
    "cap_peintre_100": {
        "title": "CAP Peintre applicateur de revêtements",
        "description": "Révisions complètes CAP Peintre applicateur de revêtements.",
        "data": quiz_cap_peintre_data,
        "icon": "🎨",
        "color": "#673ab7",
    },
    "cap_peinture_carrosserie_100": {
        "title": "CAP Peintre en carrosserie",
        "description": "Révisions complètes CAP Peintre en carrosserie.",
        "data": quiz_cap_peinture_carrosserie_data,
        "icon": "🚗",
        "color": "#3498db",
    },
    "cap_platre_isolation_100": {
        "title": "CAP Métiers du plâtre et de l’isolation",
        "description": "Révisions complètes CAP Métiers du plâtre et de l’isolation.",
        "data": quiz_cap_platre_isolation_data,
        "icon": "🏗️",
        "color": "#bdc3c7",
    },
    "cap_sanitaire_100": {
        "title": "CAP Monteur en installations sanitaires",
        "description": "Révisions complètes CAP Monteur en installations sanitaires.",
        "data": quiz_cap_sanitaire_data,
        "icon": "🚰",
        "color": "#3498db",
    },
    "cap_serrurier_metallier_100": {
        "title": "CAP Serrurier-métallier",
        "description": "Révisions complètes CAP Serrurier-métallier.",
        "data": quiz_cap_serrurier_metallier_data,
        "icon": "🔑",
        "color": "#7f8c8d",
    },
    "cap_thermique_100": {
        "title": "CAP Monteur en installations thermiques",
        "description": "Révisions complètes CAP Monteur en installations thermiques.",
        "data": quiz_cap_thermique_data,
        "icon": "🔥",
        "color": "#e74c3c",
    },

    # ----- CS -----
    "cs_coiffure_coupe_couleur_100": {
        "title": "Certificat de spécialisation coiffure – coupe couleur",
        "description": "Révisions complètes CS Coiffure coupe couleur.",
        "data": quiz_cs_coiffure_coupe_couleur_data,
        "icon": "✂️",
        "color": "#e84393",
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
# CATALOGUE DES QUIZ PAR NIVEAU / FAMILLE
# -----------------------

CAP_FAMILIES = {
    "Métiers de bouche": [
        "cap_boucher_100",
        "cap_boulanger_100",
        "cap_patissier_100",
        "cap_charcutier_traiteur_100",
        "cap_chcr_100",
        "cap_cuisine_100",
    ],
    "Auto": [
        "cap_carrosserie_automobile_100",
        "cap_peinture_carrosserie_100",
        "cap_meca_vp_100",
    ],
    "Bâtiment": [
        "cap_carreleur_mosaiste_100",
        "cap_electricien_100",
        "cap_macon_100",
        "cap_menuisier_fabricant_100",
        "cap_menuisier_installateur_100",
        "cap_platre_isolation_100",
        "cap_peintre_100",
        "cap_serrurier_metallier_100",
        "cap_sanitaire_100",
        "cap_thermique_100",
    ],
    "Service": [
        "cap_coiffure_100",
        "cap_equipier_polyvalent_commerce_100",
    ],
}

BACPRO_QUIZZES = [
    "bacpro_mcvb_100",
    "bacpro_mcva_100",
    "bacpro_mva_100",
]

BP_QUIZZES = [
    "bp_arts_de_la_cuisine_100",
    "bp_boucher_100",
    "bp_coiffure_100",
    "bp_macon_100",
    "bp_migcs_100",
]

BTS_QUIZZES = [
    "bts_meca_vp_100",
]

CS_QUIZZES = [
    "cs_coiffure_coupe_couleur_100",
]

LEVELS = ["CAP", "BAC PRO", "BP", "BTS", "CS"]


# -----------------------
# STATE SPÉCIFIQUE À LA NAVIGATION
# -----------------------

if "selected_level" not in st.session_state:
    st.session_state.selected_level = None

if "selected_cap_family" not in st.session_state:
    st.session_state.selected_cap_family = None


# -----------------------
# OUTILS D’ORDRE ALPHABÉTIQUE
# -----------------------

def get_sorted_quiz_keys(keys):
    existing = [k for k in keys if k in QUIZZES]
    return sorted(existing, key=lambda k: QUIZZES[k]["title"])


# -----------------------
# INTERFACE : NIVEAU DE FORMATION
# -----------------------

def show_level_selector():
    st.title("Quiz CFA – Centre de Foix")
    st.subheader("Choisissez un niveau de formation")

    level_colors = {
        "CAP": "#4f46e5",
        "BP": "#16a34a",
        "BAC PRO": "#f97316",
        "BTS": "#0ea5e9",
        "CS": "#e11d48",
    }
    level_icons = {
        "CAP": "🎓",
        "BP": "🎓",
        "BAC PRO": "📘",
        "BTS": "📙",
        "CS": "⭐",
    }

    cols = st.columns(len(LEVELS))

    for i, level in enumerate(LEVELS):
        color = level_colors.get(level, "#6b7280")
        icon = level_icons.get(level, "❓")
        enabled = level in ["CAP", "BP", "BAC PRO", "BTS", "CS"]

        with cols[i]:
            # Carte visuelle
            st.markdown(
                f"""
                <div style="
                    border-radius: 12px;
                    padding: 0.8rem;
                    margin-bottom: 0.5rem;
                    background: {'#eef2ff' if enabled else '#f3f4f6'};
                    border: 2px solid {color};
                    text-align: center;
                ">
                    <span style="font-size:2rem;">{icon}</span><br/>
                    <strong>{level}</strong><br/>
                    <span style="font-size:0.8rem;color:#4b5563;">
                        {"Cliquez pour continuer" if enabled else "Bientôt disponible"}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Bouton fonctionnel
            label = (
                f"{icon} {level}"
                if enabled
                else f"{icon} {level} (bientôt disponible)"
            )
            if st.button(
                label,
                key=f"btn_level_{level}",
                disabled=not enabled,
            ):
                st.session_state.selected_level = level
                st.session_state.selected_cap_family = None
                st.session_state.selected_quiz_key = None
                st.session_state.current_theme = None
                st.rerun()


# -----------------------
# INTERFACE : FAMILLES CAP
# -----------------------

def show_cap_families():
    st.subheader("CAP – Choisissez une famille de métiers")

    if st.button("⬅️ Retour aux niveaux"):
        st.session_state.selected_level = None
        st.session_state.selected_cap_family = None
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

    family_icons = {
        "Métiers de bouche": "🍽️",
        "Auto": "🚗",
        "Bâtiment": "🏗️",
        "Service": "🤝",
    }

    for family_name, quiz_keys in CAP_FAMILIES.items():
        sorted_keys = get_sorted_quiz_keys(quiz_keys)
        has_quiz = len(sorted_keys) > 0
        icon = family_icons.get(family_name, "📚")
        color = "#4f46e5" if has_quiz else "#9ca3af"
        bg = "#eef2ff" if has_quiz else "#f3f4f6"

        # Carte visuelle
        st.markdown(
            f"""
            <div style="
                border: 2px solid {color};
                border-radius: 12px;
                padding: 0.8rem 1rem;
                margin: 0.5rem 0;
                background: {bg};
                display: flex;
                align-items: center;
            ">
                <span style="font-size:1.8rem;margin-right:0.7rem;">{icon}</span>
                <strong>{family_name}</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Bouton fonctionnel
        label = (
            f"{icon} {family_name}"
            if has_quiz
            else f"{icon} {family_name} (bientôt disponible)"
        )
        if st.button(
            label,
            key=f"btn_cap_family_{family_name}",
            disabled=not has_quiz,
        ):
            st.session_state.selected_cap_family = family_name
            st.session_state.selected_quiz_key = None
            st.session_state.current_theme = None
            st.rerun()

# -----------------------
# INTERFACE : LISTE DES QUIZ (CAP, BP, BTS, CS)
# -----------------------

def render_quiz_card(key):
    info = QUIZZES[key]
    color = info.get("color", "#666")

    st.markdown(
        f"""
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
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown(f'<div class="quiz-card-{key}">', unsafe_allow_html=True)
        cols = st.columns([1, 5])
        with cols[0]:
            st.markdown(
                f"<h1 style='font-size:3rem;margin:0;'>{info.get('icon', '')}</h1>",
                unsafe_allow_html=True,
            )
        with cols[1]:
            st.markdown(f"**{info['title']}**")
            st.write(info["description"])
            if st.button("Lancer ce quiz", key=f"select_quiz_{key}"):
                st.session_state.selected_quiz_key = key
                reset_quiz_state_for_selected_quiz()
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


def show_quiz_list_for_cap_family():
    family = st.session_state.selected_cap_family
    if not family or family not in CAP_FAMILIES:
        st.error("Famille CAP inconnue.")
        return

    st.subheader(f"CAP – {family}")

    if st.button("⬅️ Retour aux familles CAP"):
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.session_state.selected_cap_family = None
        st.rerun()

    quiz_keys = get_sorted_quiz_keys(CAP_FAMILIES[family])

    for key in quiz_keys:
        render_quiz_card(key)


def show_quiz_list_for_bp():
    st.subheader("BP – Choisissez un quiz")

    if st.button("⬅️ Retour aux niveaux"):
        st.session_state.selected_level = None
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

    quiz_keys = get_sorted_quiz_keys(BP_QUIZZES)

    if not quiz_keys:
        st.info("Aucun quiz BP disponible pour le moment.")
    else:
        for key in quiz_keys:
            render_quiz_card(key)


def show_quiz_list_for_bts():
    st.subheader("BTS – Choisissez un quiz")

    if st.button("⬅️ Retour aux niveaux"):
        st.session_state.selected_level = None
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

    quiz_keys = get_sorted_quiz_keys(BTS_QUIZZES)

    if not quiz_keys:
        st.info("Aucun quiz BTS disponible pour le moment.")
    else:
        for key in quiz_keys:
            render_quiz_card(key)


def show_quiz_list_for_cs():
    st.subheader("CS – Choisissez un quiz")

    if st.button("⬅️ Retour aux niveaux"):
        st.session_state.selected_level = None
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

    quiz_keys = get_sorted_quiz_keys(CS_QUIZZES)

    if not quiz_keys:
        st.info("Aucun quiz CS disponible pour le moment.")
    else:
        for key in quiz_keys:
            render_quiz_card(key)

# -----------------------
# INTERFACE : SÉLECTEUR DE QUIZ (HUB)
# -----------------------

def show_quiz_selector():
    level = st.session_state.selected_level

    if level is None:
        show_level_selector()
    elif level == "CAP":
        if st.session_state.selected_cap_family is None:
            show_cap_families()
        else:
            show_quiz_list_for_cap_family()
    elif level == "BP":
        show_quiz_list_for_bp()
    elif level == "BAC PRO":
        show_quiz_list_for_bacpro()
    elif level == "BTS":
        show_quiz_list_for_bts()
    elif level == "CS":
        show_quiz_list_for_cs()
    else:
        show_level_selector()



# -----------------------
# INTERFACE : MENU DES THÈMES (POUR LE QUIZ COURANT)
# -----------------------

def show_main_menu_for_current_quiz():
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    if not quiz_data or not quiz_key:
        st.error("Aucune donnée de quiz chargée.")
        return

    st.title(quiz_data["title"])

    if st.button("🔙 Retour au menu des quiz"):
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
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

    if "shuffled_answers" not in st.session_state:
        st.session_state.shuffled_answers = {}

    q_id = f"{theme_number}_{idx}"

    if q_id not in st.session_state.shuffled_answers:
        options = [opt.copy() for opt in q["answerOptions"]]
        random.shuffle(options)
        for i, opt in enumerate(options):
            opt["key"] = chr(ord("A") + i)
        st.session_state.shuffled_answers[q_id] = options

    answer_options = st.session_state.shuffled_answers[q_id]
    options_text = [opt["text"] for opt in answer_options]

    if "answer_locked" not in st.session_state:
        st.session_state.answer_locked = False
    if "selected_answer" not in st.session_state:
        st.session_state.selected_answer = None

    st.write(q["question"])

    if not st.session_state.answer_locked:
        selected = st.radio(
            "Choisissez une réponse :",
            options=options_text,
            key=f"q_{theme_number}_{idx}",
        )
        st.session_state.selected_answer = selected

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Valider la réponse"):
                if not st.session_state.selected_answer:
                    st.warning("Veuillez sélectionner une réponse.")
                else:
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
                    unsafe_allow_html=True,
                )
            elif st.session_state.last_is_correct is False:
                st.markdown(
                    f"""
                    <div style='background-color:#f8d7da;border-left:5px solid #dc3545;padding:1rem;border-radius:8px;margin:1rem 0;'>
                        <h3 style='color:#721c24;margin:0 0 0.5rem 0;'>❌ Mauvaise réponse</h3>
                        <p style='margin:0;color:#721c24;'><strong>La bonne réponse était :</strong> {correct_option['text'] if correct_option else 'N/A'}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            if "correction" in q and q["correction"]:
                st.markdown(
                    f"""
                    <div style='background-color:#d1ecf1;border-left:5px solid #17a2b8;padding:1rem;border-radius:8px;margin:1rem 0;'>
                        <h4 style='color:#0c5460;margin:0 0 0.5rem 0;'>📚 Cours</h4>
                        <div style='color:#0c5460;'>{q['correction']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        if st.button("Question suivante ➡️"):
            st.session_state.show_correction = False
            st.session_state.last_is_correct = None
            st.session_state.current_question_index += 1
            st.session_state.answer_locked = False
            st.session_state.selected_answer = None

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
        st.success(
            f"🎉 Parfait ! Votre score : {score}/{total_questions} ({percentage:.0f}%)"
        )
    elif percentage >= 75:
        st.success(
            f"👍 Très bien ! Votre score : {score}/{total_questions} ({percentage:.0f}%)"
        )
    elif percentage >= 50:
        st.info(
            f"🆗 Pas mal ! Votre score : {score}/{total_questions} ({percentage:.0f}%)"
        )
    else:
        st.warning(
            f"📚 Votre score : {score}/{total_questions} ({percentage:.0f}%) - Révise encore ce thème !"
        )

    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    st.session_state.theme_scores[quiz_key][theme_number] = f"{score}/{total_questions}"

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

    summary_text = generate_score_summary()
    st.download_button(
        label="📄 Télécharger le récapitulatif complet",
        data=summary_text,
        file_name=f"recap_quiz_{quiz_key}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain",
    )


# -----------------------
# FONCTION PRINCIPALE
# -----------------------

def main():
    if st.session_state.selected_quiz_key is None:
        show_quiz_selector()
        return

    if st.session_state.current_theme is None:
        show_main_menu_for_current_quiz()
        return

    quiz_data = get_current_quiz_data()
    theme = quiz_data["themes"][st.session_state.current_theme]

    if st.session_state.current_question_index >= len(theme["questions"]):
        show_theme_result()
    else:
        show_question_screen()


if __name__ == "__main__":
    main()
