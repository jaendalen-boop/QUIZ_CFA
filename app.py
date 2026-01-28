import streamlit as st
import random
from enum import Enum
import importlib
from datetime import datetime
from auth_persistence import (
    create_user,
    login_user,
    get_user_info,
    get_user_stats,
    save_user_scores,
    load_user_scores,
)

class UIMode(Enum):
    APP = "app"
    PROFILE = "profile"

st.set_page_config(page_title="Quiz CFA", page_icon="🎓", layout="centered")

if "auth_stage" not in st.session_state:
    st.session_state.auth_stage = "entry"

if "username" not in st.session_state:
    st.session_state.username = None

if "ui_mode" not in st.session_state:
    st.session_state.ui_mode = UIMode.APP

# ===================== INJECT CUSTOM PASSWORD MANAGER HOOK =====================

st.set_page_config(page_title="Quiz CFA", page_icon="🎓", layout="centered")
if "auth_stage" not in st.session_state:
    # "entry" = écran d’entrée (sans compte / créer un compte / se connecter)
    # "logged_in" = utilisateur connecté
    st.session_state.auth_stage = "entry"

if "username" not in st.session_state:
    st.session_state.username = None

# -----------------------
# QUIZZES
# -----------------------

QUIZZES = {
    # ----- BAC PRO -----
    "bacpro_mcvb_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option B (prospection et valorisation de l'offre commerciale)",
        "description": "Révisions complètes Bac Pro MCV option B.",
        "path": "quizzes.quiz_bacpro_metiers.quiz_bacpro_mcvb_100",
        "icon": "🛍️",
        "color": "#1abc9c",
    },
    "bacpro_mcva_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option A (animation et gestion de l'espace commercial)",
        "description": "Révisions complètes Bac Pro MCV option A.",
        "path": "quizzes.quiz_bacpro_metiers.quiz_bacpro_mcva_100",
        "icon": "🏬",
        "color": "#27ae60",
    },
    "bacpro_mva_100": {
        "title": "Bac Pro Maintenance des véhicules option A (voitures particulières)",
        "description": "Révisions complètes Bac Pro Maintenance des véhicules option A (VP).",
        "path": "quizzes.quiz_bacpro_metiers.quiz_bacpro_mva_100",
        "icon": "🚗",
        "color": "#2980b9",
    },

    # ----- BP -----
    "bp_arts_de_la_cuisine_100": {
        "title": "BP Arts de la cuisine",
        "description": "Révisions complètes BP Arts de la cuisine.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_arts_de_la_cuisine_100",
        "icon": "👨‍🍳",
        "color": "#e67e22",
    },
    "bp_boucher_100": {
        "title": "BP Boucher",
        "description": "Révisions complètes BP Boucher.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_boucher_100",
        "icon": "🥩",
        "color": "#c0392b",
    },
    "bp_coiffure_100": {
        "title": "BP Coiffure",
        "description": "Révisions complètes BP Coiffure.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_coiffure_100",
        "icon": "💇",
        "color": "#9b59b6",
    },
    "bp_macon_100": {
        "title": "BP Maçon",
        "description": "Révisions complètes BP Maçon.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_macon_100",
        "icon": "🧱",
        "color": "#7f8c8d",
    },
    "bp_migcs_100": {
        "title": "BP Métiers de l'industrie graphique (communication et services)",
        "description": "Révisions complètes BP MIGCS.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_migcs_100",
        "icon": "🖨️",
        "color": "#34495e",
    },

    # ----- BTS -----
    "bts_meca_vp_100": {
        "title": "BTS Maintenance des véhicules, option A (voitures particulières)",
        "description": "Révisions complètes BTS Maintenance des véhicules option A (VP).",
        "path": "quizzes.quiz_bts_metiers.quiz_bts_meca_vp_100",
        "icon": "🔧",
        "color": "#2980b9",
    },

    # ----- CAP métiers -----
    "cap_boucher_100": {
        "title": "CAP Boucher",
        "description": "Révisions complètes CAP Boucher.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_boucher_100",
        "icon": "🥩",
        "color": "#e74c3c",
    },
    "cap_boulanger_100": {
        "title": "CAP Boulanger",
        "description": "Révisions complètes CAP Boulanger.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_boulanger_100",
        "icon": "🥖",
        "color": "#f39c12",
    },
    "cap_carreleur_mosaiste_100": {
        "title": "CAP Carreleur-mosaïste",
        "description": "Révisions complètes CAP Carreleur-mosaïste.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_carreleur_mosaiste_100",
        "icon": "🔲",
        "color": "#2ecc71",
    },
    "cap_carrosserie_automobile_100": {
        "title": "CAP Réparation des carrosseries",
        "description": "Révisions complètes CAP Réparation des carrosseries.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_carrosserie_automobile_100",
        "icon": "🚙",
        "color": "#34495e",
    },
    "cap_charcutier_traiteur_100": {
        "title": "CAP Charcutier-traiteur",
        "description": "Révisions complètes CAP Charcutier-traiteur.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_charcutier_traiteur_100",
        "icon": "🍖",
        "color": "#c0392b",
    },
    "cap_chcr_100": {
        "title": "CAP Commercialisation et services en hôtel-café-restaurant",
        "description": "Révisions complètes CAP Commercialisation et services en hôtel-café-restaurant.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_chcr_100",
        "icon": "☕",
        "color": "#e67e22",
    },
    "cap_coiffure_100": {
        "title": "CAP Coiffure",
        "description": "Révisions complètes CAP Coiffure.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_coiffure_100",
        "icon": "💇",
        "color": "#9b59b6",
    },
    "cap_couvreur_100": {
        "title": "CAP Couvreur",
        "description": "Révisions complètes CAP Couvreur.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_couvreur_100",
        "icon": "🏠",
        "color": "#8e44ad",
    },
    "cap_cuisine_100": {
        "title": "CAP Cuisine",
        "description": "Révisions complètes CAP Cuisine.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_cuisine_100",
        "icon": "👨‍🍳",
        "color": "#e67e22",
    },
    "cap_electricien_100": {
        "title": "CAP Électricien",
        "description": "Révisions complètes CAP Électricien.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_electricien_100",
        "icon": "⚡",
        "color": "#f1c40f",
    },
    "cap_equipier_polyvalent_commerce_100": {
        "title": "CAP Équipier polyvalent du commerce",
        "description": "Révisions complètes CAP Équipier polyvalent du commerce (EPC).",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_employe_polyvalent_commerce_100",
        "icon": "🛒",
        "color": "#16a085",
    },
    "cap_macon_100": {
        "title": "CAP Maçon",
        "description": "Révisions complètes CAP Maçon.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_macon_100",
        "icon": "🧱",
        "color": "#95a5a6",
    },
    "cap_meca_vp_100": {
        "title": "CAP Maintenance des véhicules, option A (voitures particulières)",
        "description": "Révisions complètes CAP Maintenance des véhicules option voitures particulières.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_meca_vp_100",
        "icon": "🔧",
        "color": "#34495e",
    },
    "cap_menuisier_fabricant_100": {
        "title": "CAP Menuisier fabricant de menuiserie, mobilier et agencement",
        "description": "Révisions complètes CAP Menuisier fabricant.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_menuisier_fabricant_100",
        "icon": "🪚",
        "color": "#8b4513",
    },
    "cap_menuisier_installateur_100": {
        "title": "CAP Menuisier installateur",
        "description": "Révisions complètes CAP Menuisier installateur.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_menuisier_installateur_100",
        "icon": "🔨",
        "color": "#a0522d",
    },
    "cap_patissier_100": {
        "title": "CAP Pâtissier",
        "description": "Révisions complètes CAP Pâtissier.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_patissier_100",
        "icon": "🧁",
        "color": "#e91e63",
    },
    "cap_peintre_100": {
        "title": "CAP Peintre applicateur de revêtements",
        "description": "Révisions complètes CAP Peintre applicateur de revêtements.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_peintre_100",
        "icon": "🎨",
        "color": "#673ab7",
    },
    "cap_peinture_carrosserie_100": {
        "title": "CAP Peintre en carrosserie",
        "description": "Révisions complètes CAP Peintre en carrosserie.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_peinture_carrosserie_100",
        "icon": "🚗",
        "color": "#3498db",
    },
    "cap_platre_isolation_100": {
        "title": "CAP Métiers du plâtre et de l'isolation",
        "description": "Révisions complètes CAP Métiers du plâtre et de l'isolation.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_platre_isolation_100",
        "icon": "🧱",
        "color": "#bdc3c7",
    },
    "cap_sanitaire_100": {
        "title": "CAP Monteur en installations sanitaires",
        "description": "Révisions complètes CAP Monteur en installations sanitaires.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_sanitaire_100",
        "icon": "🚰",
        "color": "#3498db",
    },
    "cap_serrurier_metallier_100": {
        "title": "CAP Serrurier-métallier",
        "description": "Révisions complètes CAP Serrurier-métallier.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_serrurier_metallier_100",
        "icon": "🔐",
        "color": "#7f8c8d",
    },
    "cap_thermique_100": {
        "title": "CAP Monteur en installations thermiques",
        "description": "Révisions complètes CAP Monteur en installations thermiques.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_thermique_100",
        "icon": "🔥",
        "color": "#e74c3c",
    },

    # ----- CAP Matières générales -----
    "cap_anglais_1": {
        "title": "CAP Matières générales – Anglais (quiz 1)",
        "description": "Révisions d'anglais – série 1.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_anglais_1",
        "icon": "🇬🇧",
        "color": "#3b82f6",
    },
    "cap_anglais_2": {
        "title": "CAP Matières générales – Anglais (quiz 2)",
        "description": "Révisions d'anglais – série 2.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_anglais_2",
        "icon": "🇬🇧",
        "color": "#2563eb",
    },
    "cap_espagnol_1": {
        "title": "CAP Matières générales – Espagnol (quiz 1)",
        "description": "Révisions d'espagnol – série 1.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_espagnol_1",
        "icon": "🇪🇸",
        "color": "#f97316",
    },
    "cap_espagnol_2": {
        "title": "CAP Matières générales – Espagnol (quiz 2)",
        "description": "Révisions d'espagnol – série 2.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_espagnol_2",
        "icon": "🇪🇸",
        "color": "#ea580c",
    },
    "cap_francais_1": {
        "title": "CAP Matières générales – Français (quiz 1)",
        "description": "Révisions de français – série 1.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_francais_1",
        "icon": "📘",
        "color": "#10b981",
    },
    "cap_francais_2": {
        "title": "CAP Matières générales – Français (quiz 2)",
        "description": "Révisions de français – série 2.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_francais_2",
        "icon": "📗",
        "color": "#059669",
    },
    "cap_histoire_geographie_1": {
        "title": "CAP Matières générales – Histoire-Géographie (quiz 1)",
        "description": "Révisions d'histoire-géographie – série 1.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_histoire_geographie_1",
        "icon": "🌍",
        "color": "#facc15",
    },
    "cap_histoire_geographie_2": {
        "title": "CAP Matières générales – Histoire-Géographie (quiz 2)",
        "description": "Révisions d'histoire-géographie – série 2.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_histoire_geographie_2",
        "icon": "🗺️",
        "color": "#eab308",
    },
    "cap_mathematique_1": {
        "title": "CAP Matières générales – Mathématiques (quiz 1)",
        "description": "Révisions de mathématiques – série 1.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_mathematique_1",
        "icon": "➗",
        "color": "#6366f1",
    },
    "cap_mathematique_2": {
        "title": "CAP Matières générales – Mathématiques (quiz 2)",
        "description": "Révisions de mathématiques – série 2.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_mathematique_2",
        "icon": "✖️",
        "color": "#4f46e5",
    },
    "cap_pse_1": {
        "title": "CAP Matières générales – PSE (quiz 1)",
        "description": "Révisions de Prévention Santé Environnement – série 1.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_pse_1",
        "icon": "🩺",
        "color": "#22c55e",
    },
    "cap_pse_2": {
        "title": "CAP Matières générales – PSE (quiz 2)",
        "description": "Révisions de Prévention Santé Environnement – série 2.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_pse_2",
        "icon": "🏥",
        "color": "#16a34a",
    },
    "cap_science_physique_1": {
        "title": "CAP Matières générales – Sciences physiques (quiz 1)",
        "description": "Révisions de sciences physiques – série 1.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_science_physique_1",
        "icon": "🔬",
        "color": "#0ea5e9",
    },
    "cap_science_physique_2": {
        "title": "CAP Matières générales – Sciences physiques (quiz 2)",
        "description": "Révisions de sciences physiques – série 2.",
        "path": "quizzes.quiz_cap_generaux.quiz_cap_science_physique_2",
        "icon": "⚗️",
        "color": "#0284c7",
    },

    # ----- CS -----
    "cs_coiffure_coupe_couleur_100": {
        "title": "Certificat de spécialisation coiffure coupe couleur",
        "description": "Révisions complètes CS Coiffure coupe couleur.",
        "path": "quizzes.quiz_cs_metiers.quiz_cs_coiffure_coupe_couleur_100",
        "icon": "💇",
        "color": "#e84393",
    },

    # ----- BAC PRO Matières générales -----
    "bacpro_anglais": {
        "title": "BAC PRO Matières générales – Anglais",
        "description": "Révisions d'anglais – BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_anglais",
        "icon": "🇬🇧",
        "color": "#3b82f6",
    },
    "bacpro_anglais_2": {
        "title": "BAC PRO Matières générales – Anglais (quiz 2)",
        "description": "Révisions d'anglais – série 2 BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_anglais_2",
        "icon": "🇬🇧",
        "color": "#2563eb",
    },
    "bacpro_espagnol": {
        "title": "BAC PRO Matières générales – Espagnol",
        "description": "Révisions d'espagnol – BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_espagnol",
        "icon": "🇪🇸",
        "color": "#f97316",
    },
    "bacpro_espagnol_2": {
        "title": "BAC PRO Matières générales – Espagnol (quiz 2)",
        "description": "Révisions d'espagnol – série 2 BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_espagnol_2",
        "icon": "🇪🇸",
        "color": "#ea580c",
    },
    "bacpro_francais": {
        "title": "BAC PRO Matières générales – Français",
        "description": "Révisions de français – BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_francais",
        "icon": "📘",
        "color": "#10b981",
    },
    "bacpro_francais_2": {
        "title": "BAC PRO Matières générales – Français (quiz 2)",
        "description": "Révisions de français – série 2 BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_francais_2",
        "icon": "📘",
        "color": "#059669",
    },
    "bacpro_histoire_geographie": {
        "title": "BAC PRO Matières générales – Histoire-Géographie",
        "description": "Révisions d'histoire-géographie – BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_histoire_geographie",
        "icon": "🌍",
        "color": "#facc15",
    },
    "bacpro_histoire_geographie_2": {
        "title": "BAC PRO Matières générales – Histoire-Géographie (quiz 2)",
        "description": "Révisions d'histoire-géographie – série 2 BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_histoire_geographie_2",
        "icon": "🌍",
        "color": "#eab308",
    },
    "bacpro_enseignement_moral_et_civique": {
        "title": "BAC PRO Matières générales – Enseignement moral et civique",
        "description": "Révisions d'EMC – BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_enseignement_moral_et_civique",
        "icon": "🕊️",
        "color": "#6366f1",
    },
    "bacpro_mathematique": {
        "title": "BAC PRO Matières générales – Mathématiques",
        "description": "Révisions de mathématiques – BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_mathematique",
        "icon": "📐",
        "color": "#0ea5e9",
    },
    "bacpro_mathematique_2": {
        "title": "BAC PRO Matières générales – Mathématiques (quiz 2)",
        "description": "Révisions de mathématiques – série 2 BAC PRO.",
        "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_mathematique_2",
        "icon": "📐",
        "color": "#0284c7",
    },
}

# -----------------------
# COULEURS PAR THÈME
# -----------------------

THEME_COLORS = {
    1: "#4f46e5",  # bleu-violet
    2: "#16a34a",  # vert
    3: "#ea580c",  # orange
    4: "#0ea5e9",  # bleu clair
    5: "#e11d48",  # rose-rouge
}

# -----------------------
# CATALOGUE DES QUIZ PAR NIVEAU / FAMILLE
# -----------------------

CAP_FAMILIES = {
    "Matières générales": [],
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
        "cap_couvreur_100",
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

CAP_GENERAL_SUBJECTS = {
    "Anglais": {
        "icon": "🇬🇧",
        "quizzes": ["cap_anglais_1", "cap_anglais_2"],
    },
    "Espagnol": {
        "icon": "🇪🇸",
        "quizzes": ["cap_espagnol_1", "cap_espagnol_2"],
    },
    "Français": {
        "icon": "📘",
        "quizzes": ["cap_francais_1", "cap_francais_2"],
    },
    "Histoire-Géographie": {
        "icon": "🌍",
        "quizzes": ["cap_histoire_geographie_1", "cap_histoire_geographie_2"],
    },
    "Mathématiques": {
        "icon": "➗",
        "quizzes": ["cap_mathematique_1", "cap_mathematique_2"],
    },
    "PSE": {
        "icon": "🩺",
        "quizzes": ["cap_pse_1", "cap_pse_2"],
    },
    "Sciences physiques": {
        "icon": "🔬",
        "quizzes": ["cap_science_physique_1", "cap_science_physique_2"],
    },
}

BACPRO_GENERAL_SUBJECTS = {
    "Anglais": {
        "icon": "🇬🇧",
        "quizzes": ["bacpro_anglais", "bacpro_anglais_2"],
    },
    "Espagnol": {
        "icon": "🇪🇸",
        "quizzes": ["bacpro_espagnol", "bacpro_espagnol_2"],
    },
    "Français": {
        "icon": "📘",
        "quizzes": ["bacpro_francais", "bacpro_francais_2"],
    },
    "Histoire-Géographie": {
        "icon": "🌍",
        "quizzes": ["bacpro_histoire_geographie", "bacpro_histoire_geographie_2"],
    },
    "Mathématiques": {
        "icon": "📐",
        "quizzes": ["bacpro_mathematique", "bacpro_mathematique_2"],
    },
    "Enseignement moral et civique": {
        "icon": "🕊️",
        "quizzes": ["bacpro_enseignement_moral_et_civique"],
    },
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
if "selected_level" not in st.session_state:
    st.session_state.selected_level = None
if "selected_cap_family" not in st.session_state:
    st.session_state.selected_cap_family = None
if "selected_cap_general_subject" not in st.session_state:
    st.session_state.selected_cap_general_subject = None
if "show_quit_confirmation" not in st.session_state:
    st.session_state.show_quit_confirmation = False
if "ui_mode" not in st.session_state:
    st.session_state.ui_mode = UIMode.APP


def show_entry_screen():
    st.markdown("""
    <div style="padding: 2rem; border-radius: 20px; background: linear-gradient(135deg, #6A11CB, #2575FC); color: white; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.25); max-width: 700px; margin: 2rem auto;">
        <h1 style="margin-bottom: 0.5rem;">Plateforme de révision CFA CMAR</h1>
        <p style="font-size: 1.1rem; opacity: 0.9;">Révisez par niveau et métier.</p>
    </div>
    """, unsafe_allow_html=True)

    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "login"

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Accès rapide")
        st.write("Accédez aux quiz immédiatement sans créer de profil.")
        if st.button("Entrer sans compte", use_container_width=True):
            st.session_state.auth_stage = "guest"
            st.rerun()

    with col2:
        if st.session_state.auth_mode == "login":
            st.subheader("🔐 Connexion")
            # Aide navigateur invisible
            st.markdown('<form action="javascript:void(0);" style="display:none;"><input type="text" autocomplete="username"><input type="password" autocomplete="current-password"></form>', unsafe_allow_html=True)
            
            user = st.text_input("Utilisateur", key="l_user", autocomplete="username")
            pw = st.text_input("Mot de passe", type="password", key="l_pw", autocomplete="current-password")
            
            if st.button("Se connecter", use_container_width=True, type="primary"):
                if user and pw:
                    success, msg = login_user(user, pw)
                    if success:
                        st.session_state.auth_stage = "logged_in"
                        st.session_state.username = user.strip().lower()
                        st.rerun()
                    else:
                        st.error(msg)
            
            if st.button("Pas de compte ? Créer un profil", use_container_width=True):
                st.session_state.auth_mode = "signup"
                st.rerun()

        else:
            st.subheader("🆕 Inscription")
            # Aide navigateur invisible
            st.markdown('<form action="javascript:void(0);" style="display:none;"><input type="text" autocomplete="username"><input type="password" autocomplete="new-password"></form>', unsafe_allow_html=True)

            new_u = st.text_input("Pseudo", key="s_user", autocomplete="username")
            new_p = st.text_input("Mot de passe", type="password", key="s_pw", autocomplete="new-password")
            
            if st.button("Créer mon compte", use_container_width=True, type="primary"):
                if new_u and new_p:
                    # On envoie une chaîne vide pour l'email
                    success, msg = create_user(new_u, "", new_p)
                    if success:
                        st.success("Compte créé ! Connectez-vous.")
                        st.session_state.auth_mode = "login"
                        st.rerun()
                    else:
                        st.error(msg)
                else:
                    st.warning("⚠️ Choisissez un pseudo et un mot de passe.")
            
            if st.button("Retour à la connexion", use_container_width=True):
                st.session_state.auth_mode = "login"
                st.rerun()

# -----------------------
# FONCTIONS UTILITAIRES
# -----------------------

def get_sorted_quiz_keys(keys):
    existing = [k for k in keys if k in QUIZZES]
    return sorted(existing, key=lambda k: QUIZZES[k]["title"])


# -----------------------
# FONCTIONS : GESTION DU QUIZ COURANT
# -----------------------

def get_current_quiz_data():
    """Charge dynamiquement et retourne le quiz_data du quiz sélectionné."""
    quiz_key = st.session_state.selected_quiz_key
    if quiz_key is None:
        return None
    
    # On récupère le chemin enregistré dans le dictionnaire
    quiz_path = QUIZZES[quiz_key].get("path")
    
    if quiz_path:
        try:
            # On charge le fichier seulement maintenant
            module = importlib.import_module(quiz_path)
            return module.quiz_data
        except Exception as e:
            st.error(f"Erreur de chargement du quiz : {e}")
            return None
    return None

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
    st.session_state.shuffled_answers = {}

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
    
    shuffled = questions.copy()
    random.shuffle(shuffled)
    
    st.session_state.current_theme = theme_number
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None
    st.session_state.shuffled_questions = shuffled
    st.session_state.shuffled_answers = {}
    st.session_state.question_results = []
    
    if "theme_attempt_counter" not in st.session_state:
        st.session_state.theme_attempt_counter = 0
    st.session_state.theme_attempt_counter += 1


def go_back_to_main_menu():
    """Retour au menu des thèmes pour le quiz courant (sans effacer les scores)."""
    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None
    st.session_state.shuffled_questions = None
    st.session_state.shuffled_answers = {}


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
# INTERFACE : PROFIL
# -----------------------

def show_profile_page():
    if st.session_state.get("auth_stage") != "logged_in" or not st.session_state.get("username"):
        st.info("Connectez-vous pour accéder à votre profil.")
        return

    username = st.session_state.username

    # Infos de base / stats / scores
    user_info = get_user_info(username)
    stats = get_user_stats(username)
    user_scores = load_user_scores(username)
    quizzes = user_scores.get("quizzes", {})

    # --- Calculs complémentaires pour badges ---

    # Quiz validés (tous les thèmes faits + moyenne ≥ 70 %)
    validated_quiz_count = 0

    # Compteurs par niveau pour badges "spécialiste"
    validated_cap = 0
    validated_bacpro = 0
    validated_bp = 0
    validated_bts = 0
    validated_cs = 0

    for quiz_key, quiz_data in quizzes.items():
        scores = quiz_data.get("scores", {})
        if not scores:
            continue

        total_correct = 0
        total_questions = 0
        all_themes_completed = True

        for score_str in scores.values():
            # On ne traite que les chaînes "8/10"
            if not isinstance(score_str, str):
                continue
            try:
                correct, total = map(int, score_str.split("/"))
                total_correct += correct
                total_questions += total
            except ValueError:
                all_themes_completed = False

        if total_questions == 0:
            continue

        percentage = (total_correct / total_questions) * 100
        if all_themes_completed and percentage >= 70:
            validated_quiz_count += 1

            if quiz_key.startswith("cap_"):
                validated_cap += 1
            elif quiz_key.startswith("bacpro_"):
                validated_bacpro += 1
            elif quiz_key.startswith("bp_"):
                validated_bp += 1
            elif quiz_key.startswith("bts_"):
                validated_bts += 1
            elif quiz_key.startswith("cs_"):
                validated_cs += 1

    # --- En-tête profil ---

    st.markdown(
        f"<h1 style='text-align:center;margin-bottom:1rem;'>👤 Profil de {username}</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="
            max-width: 700px;
            margin: 0 auto 1.5rem auto;
            padding: 1rem 1.5rem;
            border-radius: 16px;
            background: #f9fafb;
            border: 1px solid #e5e7eb;
        ">
            <p style="margin:0.2rem 0;"><strong>Email :</strong> {user_info.get('email', 'Non renseigné')}</p>
            <p style="margin:0.2rem 0;"><strong>Compte créé le :</strong> {user_info.get('created_at', 'N/A')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Stats globales ---

    st.subheader("Progression globale")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Quiz différents", stats.get("total_quizzes", 0))
    col2.metric("Quiz validés", validated_quiz_count)
    col3.metric("Questions totales", stats.get("total_questions", 0))
    col4.metric("Réussite moyenne", f"{stats.get('average_percentage', 0)} %")

          # --- BARRES DE PROGRESSION PAR NIVEAU ---

    st.markdown("### 📈 Progression par diplôme")
    
    # On définit un objectif (ex: 5 quiz pour remplir la barre)
    obj = 5 
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.write(f"**CAP** ({validated_cap}/{obj})")
        st.progress(min(validated_cap / obj, 1.0))
        
        st.write(f"**BAC PRO** ({validated_bacpro}/{obj})")
        st.progress(min(validated_bacpro / obj, 1.0))

    with col_p2:
        st.write(f"**BP / BTS / CS** ({validated_bp + validated_bts + validated_cs}/{obj})")
        st.progress(min((validated_bp + validated_bts + validated_cs) / obj, 1.0))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Badges ---

    st.markdown("### Badges")

# --- SECTION BADGES ---
    st.markdown("### 🏆 Vos Badges")

    total_quiz_played = stats.get("total_quizzes", 0)
    
    # Configuration des badges
    tous_les_badges = [
        {"nom": "🎯 Premier quiz", "cond": validated_quiz_count >= 1},
        {"nom": "🏅 5 quiz validés", "cond": validated_quiz_count >= 5},
        {"nom": "📚 100 questions", "cond": stats.get("total_questions", 0) >= 100},
        {"nom": "🧠 300 questions", "cond": stats.get("total_questions", 0) >= 300},
        {"nom": "🔥 Moyenne ≥ 80%", "cond": stats.get("average_percentage", 0) >= 80},
        {"nom": "💎 Moyenne ≥ 90%", "cond": stats.get("average_percentage", 0) >= 90},
        {"nom": "🏗️ Expert CAP", "cond": validated_cap >= 3},
        {"nom": "🏬 Expert BAC PRO", "cond": validated_bacpro >= 2},
        {"nom": "🎓 Spécialiste Sup", "cond": (validated_bp >= 1 and validated_bts >= 1)},
        {"nom": "⏱️ Fidèle au poste", "cond": total_quiz_played >= 10},
    ]

    # Construction de la ligne HTML
    html_str = "<div style='display:flex; flex-wrap:wrap; gap:0.5rem;'>"
    
    for b in tous_les_badges:
        if b["cond"]:
            # Badge débloqué : Couleur indigo
            style = "background:#eef2ff; border:1px solid #c7d2fe; color:#1f2937; opacity:1;"
        else:
            # Badge verrouillé : Grisé et transparent
            style = "background:#f3f4f6; border:1px solid #d1d5db; color:#9ca3af; opacity:0.5; filter:grayscale(100%);"
            
        html_str += f"<span style='{style} border-radius:999px; padding:0.4rem 0.8rem; font-size:0.85rem; font-weight:500;'>{b['nom']}</span>"
    
    html_str += "</div>"

    # IMPORTANT : C'est cette ligne qui transforme le code ci-dessus en vrais badges
    st.markdown(html_str, unsafe_allow_html=True)

    # --- Détail par quiz ---

    st.markdown("---")
    st.subheader("Détail par quiz")

    if not quizzes:
        st.info("Aucun quiz complété pour le moment.")
        return

    level_filter = st.selectbox(
        "Filtrer par niveau",
        options=["Tous", "CAP", "BAC PRO", "BP", "BTS", "CS"],
        index=0,
    )

    def quiz_matches_level(key: str) -> bool:
        if level_filter == "Tous":
            return True
        if level_filter == "CAP" and key.startswith("cap_"):
            return True
        if level_filter == "BAC PRO" and key.startswith("bacpro_"):
            return True
        if level_filter == "BP" and key.startswith("bp_"):
            return True
        if level_filter == "BTS" and key.startswith("bts_"):
            return True
        if level_filter == "CS" and key.startswith("cs_"):
            return True
        return False

    for quiz_key, quiz_data in quizzes.items():
        if not quiz_matches_level(quiz_key):
            continue

        quiz_info = QUIZZES.get(quiz_key, {})
        quiz_title = quiz_info.get("title", quiz_key)
        last_updated = quiz_data.get("last_updated", "")

        with st.expander(quiz_title):
            if last_updated:
                st.caption(f"Dernière mise à jour : {last_updated}")
            scores = quiz_data.get("scores", {})
            for theme_num, score_str in scores.items():
                st.write(f"- Thème {theme_num} : {score_str}")


# -----------------------
# INTERFACE : SÉLECTEUR DE NIVEAU
# -----------------------

def show_level_selector():
    st.markdown(
        """
        <div style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem 1rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        '>
            <h1 style='
                font-size: 2.8rem;
                margin: 0;
                color: #ffffff;
                font-weight: 800;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            '>Quiz CFA</h1>
            <p style='
                font-size: 1.2rem;
                color: #f0f0f0;
                margin: 0.5rem 0 0 0;
                font-weight: 400;
            '>Centre de Foix</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        "<h2 style='text-align:center;margin-bottom:2rem;color:#374151;font-size:1.8rem;'>Choisissez un niveau de formation</h2>",
        unsafe_allow_html=True
    )

    level_colors = {
        "CAP": "#4f46e5",
        "BP": "#16a34a",
        "BAC PRO": "#f97316",
        "BTS": "#0ea5e9",
        "CS": "#e11d48",
    }
    
    level_icons = {
        "CAP": "🎓",
        "BP": "📘",
        "BAC PRO": "🏆",
        "BTS": "🎯",
        "CS": "⭐",
    }

    st.markdown("<div style='max-width:900px;margin:0 auto;'>", unsafe_allow_html=True)
    
    cols = st.columns(len(LEVELS))
    
    for i, level in enumerate(LEVELS):
        color = level_colors.get(level, "#6b7280")
        icon = level_icons.get(level, "📚")
        enabled = level in ["CAP", "BP", "BAC PRO", "BTS", "CS"]
        
        with cols[i]:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, {color}15 0%, {color}05 100%);
                    border: 3px solid {color};
                    border-radius: 16px;
                    padding: 1.5rem 1rem 0.5rem 1rem;
                    text-align: center;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
                    min-height: 160px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    margin-bottom: 0.8rem;
                ">
                    <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">{icon}</div>
                    <div style="font-size: 1.4rem; font-weight: 700; color: {color}; margin-bottom: 0.3rem;">{level}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            if enabled:
                if st.button(f"Accéder au {level}", key=f"btn_level_{level}", type="primary", use_container_width=True):
                    st.session_state.selected_level = level
                    st.session_state.selected_cap_family = None
                    st.session_state.selected_cap_general_subject = None
                    st.session_state.selected_quiz_key = None
                    st.session_state.current_theme = None
                    st.rerun()
            else:
                st.markdown(
                    f"<p style='text-align:center;color:#9ca3af;font-size:0.9rem;margin-top:-0.5rem;'>Bientôt disponible</p>",
                    unsafe_allow_html=True
                )
    
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# INTERFACE : FAMILLES CAP
# -----------------------

def show_cap_families():
    st.markdown(
        "<h2 style='text-align:center;margin-bottom:2rem;color:#374151;font-size:1.8rem;'>CAP – Choisissez une famille</h2>",
        unsafe_allow_html=True
    )

    if st.button("⬅️ Retour aux niveaux", key="back_to_levels"):
        st.session_state.selected_level = None
        st.session_state.selected_cap_family = None
        st.session_state.selected_cap_general_subject = None
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

    family_config = {
        "Matières générales": {"icon": "📚", "color": "#4f46e5"},
        "Métiers de bouche": {"icon": "🍽️", "color": "#f97316"},
        "Auto": {"icon": "🚗", "color": "#64748b"},
        "Bâtiment": {"icon": "🏗️", "color": "#92400e"},
        "Service": {"icon": "🤝", "color": "#10b981"},
    }

    st.markdown("<div style='max-width:800px;margin:0 auto;'>", unsafe_allow_html=True)

    for idx, family_name in enumerate(family_config.keys()):
        if idx % 2 == 0:
            cols = st.columns(2)
        
        col = cols[idx % 2]
        config = family_config[family_name]
        
        with col:
            icon = config["icon"]
            color = config["color"]
            
            if family_name == "Matières générales":
                quiz_count = sum(len(info["quizzes"]) for info in CAP_GENERAL_SUBJECTS.values())
                badge = f"{quiz_count} quiz"
            else:
                quiz_keys = CAP_FAMILIES.get(family_name, [])
                quiz_count = len(quiz_keys)
                badge = None
            
            has_quiz = quiz_count > 0
            
            badge_html = ""
            if badge:
                badge_html = f'<div style="position:absolute;top:10px;right:10px;background:{color};color:white;padding:0.3rem 0.6rem;border-radius:20px;font-size:0.75rem;font-weight:600;box-shadow:0 2px 8px rgba(0,0,0,0.15);">{badge}</div>'
            
            card_html = f"""
<div style="position:relative;background:linear-gradient(135deg, {color}15 0%, {color}05 100%);border:3px solid {color};border-radius:16px;padding:1.5rem;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,0.12);min-height:140px;display:flex;flex-direction:column;justify-content:center;align-items:center;margin-bottom:1rem;opacity:{'1' if has_quiz else '0.5'};">
{badge_html}
<div style="font-size:3rem;margin-bottom:0.5rem;">{icon}</div>
<div style="font-size:1.3rem;font-weight:700;color:{color};">{family_name}</div>
</div>
"""
            st.markdown(card_html, unsafe_allow_html=True)
            
            if has_quiz:
                if st.button(f"Accéder", key=f"btn_family_{family_name}", type="primary", use_container_width=True):
                    st.session_state.selected_cap_family = family_name
                    st.session_state.selected_cap_general_subject = None
                    st.session_state.selected_quiz_key = None
                    st.session_state.current_theme = None
                    st.rerun()
            else:
                st.markdown("<p style='text-align:center;color:#9ca3af;font-size:0.9rem;'>Bientôt disponible</p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


def show_cap_general_subjects():
    """Écran : choix de la matière générale CAP."""
    st.subheader("CAP – Matières générales")

    if st.button("⬅️ Retour aux familles CAP"):
        st.session_state.selected_cap_family = None
        st.session_state.selected_cap_general_subject = None
        st.rerun()

    cols = st.columns(3)
    for i, (subject, info) in enumerate(CAP_GENERAL_SUBJECTS.items()):
        col = cols[i % 3]
        with col:
            if st.button(f"{info['icon']} {subject}", key=f"cap_gen_subject_{subject}"):
                st.session_state.selected_cap_general_subject = subject
                st.rerun()


def show_cap_general_quizzes_for_subject():
    """Écran : liste des quiz (1, 2, ...) pour une matière générale CAP."""
    subject = st.session_state.selected_cap_general_subject
    if not subject or subject not in CAP_GENERAL_SUBJECTS:
        st.warning("Aucune matière sélectionnée.")
        return

    info = CAP_GENERAL_SUBJECTS[subject]
    quizzes = info["quizzes"]

    st.subheader(f"CAP – {subject}")

    if st.button("⬅️ Retour aux matières générales"):
        st.session_state.selected_cap_general_subject = None
        st.rerun()

    for idx, key in enumerate(quizzes, start=1):
        quiz_info = QUIZZES[key]
        label = f"Quiz {idx}"
        if st.button(label, key=f"{subject}_quiz_{idx}"):
            st.session_state.selected_quiz_key = key
            reset_quiz_state_for_selected_quiz()
            st.rerun()


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

# -----------------------
# INTERFACE : BAC PRO
# -----------------------

def show_bacpro_general_subjects():
    """Écran : choix de la matière générale BAC PRO."""
    st.subheader("BAC PRO – Matières générales")

    if st.button("⬅️ Retour aux catégories BAC PRO", key="back_to_bacpro_categories"):
        st.session_state.selected_bacpro_family = None
        st.session_state.selected_bacpro_general_subject = None
        st.rerun()

    cols = st.columns(3)
    for i, (subject, info) in enumerate(BACPRO_GENERAL_SUBJECTS.items()):
        col = cols[i % 3]
        with col:
            if st.button(f"{info['icon']} {subject}", key=f"bacpro_gen_subject_{subject}"):
                st.session_state.selected_bacpro_general_subject = subject
                st.rerun()


def show_bacpro_general_quizzes_for_subject():
    """Écran : liste des quiz pour une matière générale BAC PRO."""
    subject = st.session_state.get("selected_bacpro_general_subject")
    if not subject or subject not in BACPRO_GENERAL_SUBJECTS:
        st.warning("Aucune matière sélectionnée.")
        return

    info = BACPRO_GENERAL_SUBJECTS[subject]
    quizzes = info["quizzes"]

    st.subheader(f"BAC PRO – {subject}")

    if st.button("⬅️ Retour aux matières générales", key="back_to_bacpro_subjects"):
        st.session_state.selected_bacpro_general_subject = None
        st.rerun()

    for idx, key in enumerate(quizzes, start=1):
        quiz_info = QUIZZES[key]
        label = f"Quiz {idx}" if len(quizzes) > 1 else "Quiz"
        if st.button(label, key=f"bacpro_{subject}_quiz_{idx}"):
            st.session_state.selected_quiz_key = key
            reset_quiz_state_for_selected_quiz()
            st.rerun()

# -----------------------
# INTERFACE : LISTE DES QUIZ CAP
# -----------------------

def show_quiz_list_for_cap_family():
    """Écran : liste des quiz d'une famille CAP (dont cas particulier Matières générales)."""
    family = st.session_state.selected_cap_family

    if st.button("⬅️ Retour aux niveaux"):
        st.session_state.selected_level = None
        st.session_state.selected_cap_family = None
        st.session_state.selected_cap_general_subject = None
        st.rerun()

    if family == "Matières générales":
        if st.session_state.selected_cap_general_subject is None:
            show_cap_general_subjects()
        else:
            show_cap_general_quizzes_for_subject()
        return

    quiz_keys = get_sorted_quiz_keys(CAP_FAMILIES.get(family, []))

    if not quiz_keys:
        st.info(f"Aucun quiz CAP disponible pour la famille « {family} » pour le moment.")
    else:
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


def show_quiz_list_for_bacpro():
    """Écran : choix entre matières générales BAC PRO et autres quiz BAC PRO."""
    st.subheader("BAC PRO – Choisissez une catégorie")

    if st.button("⬅️ Retour aux niveaux"):
        st.session_state.selected_level = None
        st.session_state.selected_bacpro_family = None
        st.session_state.selected_bacpro_general_subject = None
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

    # Si aucune famille n'est encore choisie, on propose deux entrées :
    # - Matières générales (nouveaux quiz)
    # - Autres quiz BAC PRO (ce que tu avais déjà : BACPRO_QUIZZES)
    if st.session_state.get("selected_bacpro_family") is None:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📚 Matières générales", key="bacpro_btn_general"):
                st.session_state.selected_bacpro_family = "Matières générales"
                st.rerun()
        with col2:
            if st.button("🛠️ Spécialités / Métiers", key="bacpro_btn_specialites"):
                st.session_state.selected_bacpro_family = "Spécialités"
                st.rerun()
        return

    # Cas 1 : Matières générales BAC PRO
    if st.session_state.selected_bacpro_family == "Matières générales":
        # Si aucune matière n'est sélectionnée, on affiche la liste des matières
        if st.session_state.get("selected_bacpro_general_subject") is None:
            show_bacpro_general_subjects()
        else:
            show_bacpro_general_quizzes_for_subject()
        return

    # Cas 2 : Spécialités / anciens quiz BAC PRO
    if st.session_state.selected_bacpro_family == "Spécialités":
        st.subheader("BAC PRO – Quiz métiers / spécialités")

        quiz_keys = get_sorted_quiz_keys(BACPRO_QUIZZES)

        if not quiz_keys:
            st.info("Aucun quiz BAC PRO disponible pour le moment.")
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
        f"""
        <div class='theme-header'>
            <h4 style='margin:0;font-size:0.9rem;'>{theme_name}</h4>
            <div style='height:3px;border-radius:999px;background:{color};margin:0.2rem 0;'></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    progress_percent = ((idx + 1) / total_questions) * 100
    st.markdown(
        f"""
        <div style='
            width:100%;
            background:#e5e7eb;
            border-radius:8px;
            height:20px;
            position:relative;
            margin:0.3rem 0 0.5rem 0;
            overflow:hidden;
        '>
            <div style='
                width:{progress_percent}%;
                background:linear-gradient(90deg, {color} 0%, {color}dd 100%);
                height:100%;
                border-radius:8px;
                transition:width 0.4s ease;
            '></div>
            <span style='
                position:absolute;
                top:50%;
                left:50%;
                transform:translate(-50%, -50%);
                font-weight:600;
                font-size:0.7rem;
                color:#1f2937;
            '>{idx + 1}/{total_questions}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

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

    if "answer_locked" not in st.session_state:
        st.session_state.answer_locked = False
    if "selected_answer" not in st.session_state:
        st.session_state.selected_answer = None
    if "theme_attempt_counter" not in st.session_state:
        st.session_state.theme_attempt_counter = 0

    st.markdown("""
    <style>
    @media (max-width: 768px) {
        [data-testid="stAppViewContainer"] {
            padding-top: 0.3rem !important;
            padding-bottom: 0.3rem !important;
        }
        
        [data-testid="stElementContainer"] {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
        
        [data-testid="stVerticalBlockBorderWrapper"] {
            gap: 0.2rem !important;
        }
        
        .stVerticalBlock {
            gap: 0.2rem !important;
        }
        
        .theme-header {
            margin: 0.3rem 0 0.8rem 0 !important;
        }
        
        .question-spacing {
            margin: 0.3rem 0 1rem 0 !important;
        }
    }
    
    @media (min-width: 769px) {
        [data-testid="stAppViewContainer"] {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
        
        [data-testid="stElementContainer"] {
            padding-top: 0.5rem !important;
            padding-bottom: 0.5rem !important;
        }
        
        [data-testid="stVerticalBlockBorderWrapper"] {
            gap: 0.5rem !important;
        }
        
        .stVerticalBlock {
            gap: 0.5rem !important;
        }
        
        .theme-header {
            margin: 0.5rem 0 1.2rem 0 !important;
        }
        
        .question-spacing {
            margin: 0.5rem 0 1.5rem 0 !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3 style='margin:0.5rem 0;font-size:1.1rem;font-weight:700;line-height:1.3;'>{q['question']}</h3>", unsafe_allow_html=True)


    if not st.session_state.answer_locked:

        st.markdown(
            f"""
            <style>
            div[data-testid="stButton"] > button {{
                width: 100%;
                text-align: left;
                padding: 0.6rem 0.8rem;
                border-radius: 8px;
                border: 2px solid #d1d5db;
                background: #ffffff !important;
                color: #1f2937 !important;
                font-size: 0.95rem;
                transition: none !important;
                margin-bottom: 0.4rem;
                min-height: 48px;
                display: flex;
                align-items: center;
                touch-action: pan-y !important;
                user-select: none;
                -webkit-user-select: none;
                -webkit-touch-callout: none;
                pointer-events: auto;
                -webkit-tap-highlight-color: transparent;
            }}
            
            div[data-testid="stVerticalBlock"] {{
                touch-action: pan-y !important;
                -webkit-user-select: none;
            }}
            
            div[data-testid="stButton"] > button:active {{
                background: #{color[1:]} !important;
                color: #ffffff !important;
                border-color: #{color[1:]} !important;
            }}
            
            div[data-testid="stButton"] > button:focus {{
                outline: 2px solid #{color[1:]};
                outline-offset: 1px;
            }}
            
            div[data-testid="stColumn"] {{
                padding-left: 0.2rem !important;
                padding-right: 0.2rem !important;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

        for opt in answer_options:
            opt_text = opt["text"]
            opt_key = opt["key"]
            is_selected = (st.session_state.selected_answer == opt_text)

            button_label = f"{'✓ ' if is_selected else ''}{opt_key}. {opt_text}"

            if st.button(button_label, key=f"opt_{theme_number}_{idx}_{opt_key}_{st.session_state.theme_attempt_counter}", use_container_width=True):
                st.session_state.selected_answer = opt_text
                st.rerun()

        st.markdown("<div style='margin-top:0.4rem;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap="small")

        with col1:
            if st.button("✅ Valider", use_container_width=True, type="primary"):
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
                    
                    if "question_results" not in st.session_state:
                        st.session_state.question_results = []
                    st.session_state.question_results.append(is_correct)
                    
                    st.rerun()

        with col2:
            if st.button("⬅️ Retour", use_container_width=True):
                st.session_state.show_quit_confirmation = True
                st.rerun()

    else:
        st.markdown("<div class='question-spacing'></div>", unsafe_allow_html=True)

        for opt in answer_options:
            opt_text = opt["text"]
            opt_key = opt["key"]
            is_correct_answer = opt["isCorrect"]
            is_user_answer = (st.session_state.selected_answer == opt_text)

            if is_correct_answer:
                border_color = "#22c55e"
                bg_color = "#d4edda"
                text_color = "#155724"
                icon = "✅"
            elif is_user_answer and not is_correct_answer:
                border_color = "#dc3545"
                bg_color = "#f8d7da"
                text_color = "#721c24"
                icon = "❌"
            else:
                border_color = "#d1d5db"
                bg_color = "#f9fafb"
                text_color = "#1f2937"
                icon = ""

            st.markdown(
                f"""
                <div style="
                    border:2px solid {border_color};
                    border-radius:12px;
                    padding:0.6rem;
                    margin-bottom:0.3rem;
                    background:{bg_color};
                    color:{text_color};
                    animation:fadeIn 0.3s ease-in;
                ">
                    {icon} <strong>{opt_key}.</strong> {opt_text}
                </div>

                <style>
                @keyframes fadeIn {{
                    from {{ opacity: 0; transform: translateY(-10px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
                </style>
                """,
                unsafe_allow_html=True,
            )

        if st.session_state.show_correction:
            if st.session_state.last_is_correct is True:
                st.markdown(
                    """
                    <div style='
                        background:#d4edda;
                        border-left:6px solid #28a745;
                        padding:0.8rem;
                        border-radius:12px;
                        margin:0.6rem 0;
                        color:#155724;
                        animation:fadeIn 0.3s ease-in;
                    '>
                        <h3 style='color:#155724;margin:0;font-size:1.1rem;'>✅ Bonne réponse !</h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            elif st.session_state.last_is_correct is False:
                correct_option = next(
                    (opt for opt in answer_options if opt["isCorrect"]), None
                )
                st.markdown(
                    f"""
                    <div style='
                        background:#f8d7da;
                        border-left:6px solid #dc3545;
                        padding:0.8rem;
                        border-radius:12px;
                        margin:0.6rem 0;
                        color:#721c24;
                        animation:fadeIn 0.3s ease-in;
                    '>
                        <h3 style='color:#721c24;margin:0 0 0.3rem 0;font-size:1.1rem;'>❌ Mauvaise réponse</h3>
                        <p style='margin:0;color:#721c24;font-size:0.95rem;'><strong>La bonne réponse était :</strong> {correct_option['text'] if correct_option else 'N/A'}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            if "correction" in q and q["correction"]:
                st.markdown(
                    f"""
                    <div style='
                        background:linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
                        border-left:6px solid #0097a7;
                        padding:1rem;
                        border-radius:12px;
                        margin:0.8rem 0;
                        box-shadow:0 4px 12px rgba(0,0,0,0.1);
                        color:#006064;
                        animation:fadeIn 0.4s ease-in;
                    '>
                        <h4 style='color:#006064;margin:0 0 0.5rem 0;font-size:1rem;display:flex;align-items:center;'>
                            <span style='font-size:1.2rem;margin-right:0.5rem;'>📚</span> Cours
                        </h4>
                        <div style='color:#00363a;line-height:1.5;font-size:0.95rem;'>{q['correction']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown("<div style='margin-top:0.6rem;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2, gap="small")

        with col1:
            if st.button("➡️ Question suivante", use_container_width=True, type="primary", key="next_question_btn"):
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


        with col2:
            if st.button("⬅️ Quitter le thème", use_container_width=True, key="exit_theme_btn"):
                st.session_state.show_quit_confirmation = True
                st.rerun()

    if st.session_state.get("show_quit_confirmation", False):
        st.warning("⚠️ **Attention !** Si vous quittez maintenant, la progression du thème en cours ne sera **pas conservée**.")
        col_confirm_1, col_confirm_2 = st.columns(2)
        
        with col_confirm_1:
            if st.button("✅ Oui, quitter le thème", use_container_width=True, key="confirm_quit"):
                st.session_state.show_quit_confirmation = False
                go_back_to_main_menu()
                st.rerun()
        
        with col_confirm_2:
            if st.button("❌ Non, continuer", use_container_width=True, key="cancel_quit"):
                st.session_state.show_quit_confirmation = False
                st.rerun()

# -----------------------
# FONCTION PRINCIPALE
# -----------------------

def show_theme_result():
    """Affiche le résultat d'un thème complété"""
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    total_questions = len(theme["questions"])
    score = st.session_state.score
    percentage = (score / total_questions * 100) if total_questions > 0 else 0
    color = THEME_COLORS.get(theme_number, "#4f46e5")
    
    st.markdown(
        f"<h1 style='text-align:center;color:{color};margin-bottom:1.5rem'>Résultat {theme_name}</h1>",
        unsafe_allow_html=True
    )
    
    # Afficher le cercle de progression avec pourcentage
    st.markdown(
        f"""
        <div style="text-align:center;margin:2rem 0;">
            <div style="display:inline-block;position:relative;width:200px;height:200px;">
                <svg width="200" height="200" style="transform:rotate(-90deg)">
                    <circle cx="100" cy="100" r="85" fill="none" stroke="#e5e7eb" stroke-width="12"></circle>
                    <circle cx="100" cy="100" r="85" fill="none" stroke="{color}" stroke-width="12" 
                            stroke-dasharray="{percentage * 5.34} 534" stroke-linecap="round"></circle>
                </svg>
                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;">
                    <div style="font-size:3rem;font-weight:800;color:{color};">{score}/{total_questions}</div>
                    <div style="font-size:1.2rem;color:#6b7280;font-weight:600;">{percentage:.0f}%</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Afficher le message selon le score
    if percentage >= 100:
        st.balloons()
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);border-left:6px solid #28a745;
                        padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#155724;margin:0;font-size:2rem;">Parfait !</h2>
                <p style="color:#155724;margin:0.5rem 0 0 0;font-size:1.1rem;">Score parfait {score}/{total_questions} - {percentage:.0f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif percentage >= 75:
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);border-left:6px solid #28a745;
                        padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#155724;margin:0;font-size:2rem;">Très bien !</h2>
                <p style="color:#155724;margin:0.5rem 0 0 0;font-size:1.1rem;">Score {score}/{total_questions} - {percentage:.0f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif percentage >= 50:
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);border-left:6px solid #17a2b8;
                        padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#0c5460;margin:0;font-size:2rem;">Pas mal !</h2>
                <p style="color:#0c5460;margin:0.5rem 0 0 0;font-size:1.1rem;">Score {score}/{total_questions} - {percentage:.0f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);border-left:6px solid #dc3545;
                        padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#721c24;margin:0;font-size:2rem;">Continue tes efforts !</h2>
                <p style="color:#721c24;margin:0.5rem 0 0 0;font-size:1.1rem;">Score {score}/{total_questions} - {percentage:.0f}% - Révise encore ce thème !</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Sauvegarder le score du thème dans la session
    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    st.session_state.theme_scores[quiz_key][theme_number] = f"{score}/{total_questions}"

    # Sauvegarder les scores du quiz pour l'utilisateur connecté (persistance disque)
    if st.session_state.get("auth_stage") == "logged_in" and st.session_state.get("username"):
        save_user_scores(
            st.session_state.username,
            quiz_key,
            st.session_state.theme_scores[quiz_key],
        )
    
    # Boutons pour continuer
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Revenir au menu des thèmes", use_container_width=True):
            go_back_to_main_menu()
            st.rerun()
    with col2:
        if st.button("Refaire ce thème", use_container_width=True, type="primary"):
            start_theme(theme_number)
            st.rerun()


def main():
    with st.sidebar:
        st.markdown("### Navigation")
        if st.session_state.get("auth_stage") == "logged_in":
            if st.button("👤 Mon profil", use_container_width=True):
                st.session_state.ui_mode = UIMode.PROFILE
            if st.button("🏠 Quiz", use_container_width=True):
                st.session_state.ui_mode = UIMode.APP
            st.markdown("---")
            st.caption(f"Connecté en tant que {st.session_state.username}")
        else:
            if st.button("🔐 Se connecter / créer un compte", use_container_width=True):
                st.session_state.auth_stage = "entry"
                st.session_state.ui_mode = UIMode.APP
                st.rerun()

    if st.session_state.ui_mode == UIMode.PROFILE:
        show_profile_page()
        return

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
    if st.session_state.auth_stage in ("guest", "logged_in"):
        main()
    else:
        show_entry_screen()
