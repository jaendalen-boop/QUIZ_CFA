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
    ADMIN = "admin"

ADMIN_USERS = ["eral", "admin"]

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
# CHARTE GRAPHIQUE CMA OCCITANIE (CODES HEX)
# -----------------------
CMA_ROUGE = "#A8131D"          # Rouge institutionnel (Logo)
CMA_ROUGE_WEB = "#CD493D"      # Rouge éclairé optimisé pour le contraste web
CMA_BLEU_MARINE = "#0F3250"    # Bleu Marine de soutien
CMA_TURQUOISE = "#5CC6A5"      # Cible Apprentis / Formation
CMA_MOUTARDE = "#F1BA33"       # Cible Artisans / Entreprises
CMA_BEIGE = "#F8F0E3"          # Fond de soutien clair universel

# -----------------------
# QUIZZES (Harmonisés aux couleurs cibles CMA)
# -----------------------

QUIZZES = {
    # ----- BAC PRO -----
    "bacpro_mcvb_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option B (prospection et valorisation de l'offre commerciale)",
        "description": "Révisions complètes Bac Pro MCV option B.",
        "path": "quizzes.quiz_bacpro_metiers.quiz_bacpro_mcvb_100",
        "icon": "🛍️",
        "color": CMA_TURQUOISE,
    },
    "bacpro_mcva_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option A (animation et gestion de l'espace commercial)",
        "description": "Révisions complètes Bac Pro MCV option A.",
        "path": "quizzes.quiz_bacpro_metiers.quiz_bacpro_mcva_100",
        "icon": "🏬",
        "color": CMA_TURQUOISE,
    },
    "bacpro_mva_100": {
        "title": "Bac Pro Maintenance des véhicules option A (voitures particulières)",
        "description": "Révisions complètes Bac Pro Maintenance des véhicules option A (VP).",
        "path": "quizzes.quiz_bacpro_metiers.quiz_bacpro_mva_100",
        "icon": "🚗",
        "color": CMA_TURQUOISE,
    },

    # ----- BP -----
    "bp_arts_de_la_cuisine_100": {
        "title": "BP Arts de la cuisine",
        "description": "Révisions complètes BP Arts de la cuisine.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_arts_de_la_cuisine_100",
        "icon": "👨‍🍳",
        "color": CMA_MOUTARDE,
    },
    "bp_boucher_100": {
        "title": "BP Boucher",
        "description": "Révisions complètes BP Boucher.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_boucher_100",
        "icon": "🥩",
        "color": CMA_MOUTARDE,
    },
    "bp_coiffure_100": {
        "title": "BP Coiffure",
        "description": "Révisions complètes BP Coiffure.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_coiffure_100",
        "icon": "💇",
        "color": CMA_MOUTARDE,
    },
    "bp_macon_100": {
        "title": "BP Maçon",
        "description": "Révisions complètes BP Maçon.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_macon_100",
        "icon": "🧱",
        "color": CMA_MOUTARDE,
    },
    "bp_migcs_100": {
        "title": "BP MIGCS",
        "description": "Révisions complètes BP MIGCS.",
        "path": "quizzes.quiz_bp_metiers.quiz_bp_migcs_100",
        "icon": "⚡",
        "color": CMA_MOUTARDE,
    },

    # ----- BTS -----
    "bts_meca_vp_100": {
        "title": "BTS Maintenance des véhicules, option A (voitures particulières)",
        "description": "Révisions complètes BTS Maintenance des véhicules option A (VP).",
        "path": "quizzes.quiz_bts_metiers.quiz_bts_meca_vp_100",
        "icon": "🔧",
        "color": CMA_BLEU_MARINE,
    },

    # ----- CAP métiers -----
    "cap_boucher_100": {
        "title": "CAP Boucher",
        "description": "Révisions complètes CAP Boucher.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_boucher_100",
        "icon": "🥩",
        "color": CMA_TURQUOISE,
    },
    "cap_boulanger_100": {
        "title": "CAP Boulanger",
        "description": "Révisions complètes CAP Boulanger.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_boulanger_100",
        "icon": "🥖",
        "color": CMA_TURQUOISE,
    },
    "cap_carreleur_mosaiste_100": {
        "title": "CAP Carreleur-mosaïste",
        "description": "Révisions complètes CAP Carreleur-mosaïste.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_carreleur_mosaiste_100",
        "icon": "🔲",
        "color": CMA_TURQUOISE,
    },
    "cap_carrosserie_automobile_100": {
        "title": "CAP Réparation des carrosseries",
        "description": "Révisions complètes CAP Réparation des carrosseries.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_carrosserie_automobile_100",
        "icon": "🚙",
        "color": CMA_TURQUOISE,
    },
    "cap_charcutier_traiteur_100": {
        "title": "CAP Charcutier-traiteur",
        "description": "Révisions complètes CAP Charcutier-traiteur.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_charcutier_traiteur_100",
        "icon": "🍖",
        "color": CMA_TURQUOISE,
    },
    "cap_chcr_100": {
        "title": "CAP Commercialisation et services en hôtel-café-restaurant",
        "description": "Révisions complètes CAP Commercialisation et services en hôtel-café-restaurant.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_chcr_100",
        "icon": "☕",
        "color": CMA_TURQUOISE,
    },
    "cap_coiffure_100": {
        "title": "CAP Coiffure",
        "description": "Révisions complètes CAP Coiffure.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_coiffure_100",
        "icon": "💇",
        "color": CMA_TURQUOISE,
    },
    "cap_couvreur_100": {
        "title": "CAP Couvreur",
        "description": "Révisions complètes CAP Couvreur.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_couvreur_100",
        "icon": "🏠",
        "color": CMA_TURQUOISE,
    },
    "cap_cuisine_100": {
        "title": "CAP Cuisine",
        "description": "Révisions complètes CAP Cuisine.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_cuisine_100",
        "icon": "👨‍🍳",
        "color": CMA_TURQUOISE,
    },
    "cap_electricien_100": {
        "title": "CAP Électricien",
        "description": "Révisions complètes CAP Électricien.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_electricien_100",
        "icon": "⚡",
        "color": CMA_TURQUOISE,
    },
    "cap_equipier_polyvalent_commerce_100": {
        "title": "CAP Équipier polyvalent du commerce",
        "description": "Révisions complètes CAP Équipier polyvalent du commerce (EPC).",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_employe_polyvalent_commerce_100",
        "icon": "🛒",
        "color": CMA_TURQUOISE,
    },
    "cap_macon_100": {
        "title": "CAP Maçon",
        "description": "Révisions complètes CAP Maçon.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_macon_100",
        "icon": "🧱",
        "color": CMA_TURQUOISE,
    },
    "cap_meca_vp_100": {
        "title": "CAP Maintenance des véhicules, option A (voitures particulières)",
        "description": "Révisions complètes CAP Maintenance des véhicules option voitures particulières.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_meca_vp_100",
        "icon": "🔧",
        "color": CMA_TURQUOISE,
    },
    "cap_menuisier_fabricant_100": {
        "title": "CAP Menuisier fabricant de menuiserie, mobilier et agencement",
        "description": "Révisions complètes CAP Menuisier fabricant.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_menuisier_fabricant_100",
        "icon": "🪚",
        "color": CMA_TURQUOISE,
    },
    "cap_menuisier_installateur_100": {
        "title": "CAP Menuisier installateur",
        "description": "Révisions complètes CAP Menuisier installateur.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_menuisier_installateur_100",
        "icon": "🔨",
        "color": CMA_TURQUOISE,
    },
    "cap_patissier_100": {
        "title": "CAP Pâtissier",
        "description": "Révisions complètes CAP Pâtissier.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_patissier_100",
        "icon": "🧁",
        "color": CMA_TURQUOISE,
    },
    "cap_peintre_100": {
        "title": "CAP Peintre applicateur de revêtements",
        "description": "Révisions complètes CAP Peintre applicateur de revêtements.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_peintre_100",
        "icon": "🎨",
        "color": CMA_TURQUOISE,
    },
    "cap_peinture_carrosserie_100": {
        "title": "CAP Peintre en carrosserie",
        "description": "Révisions complètes CAP Peintre en carrosserie.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_peinture_carrosserie_100",
        "icon": "🚗",
        "color": CMA_TURQUOISE,
    },
    "cap_platre_isolation_100": {
        "title": "CAP Métiers du plâtre et de l'isolation",
        "description": "Révisions complètes CAP Métiers du plâtre et de l'isolation.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_platre_isolation_100",
        "icon": "🧱",
        "color": CMA_TURQUOISE,
    },
    "cap_sanitaire_100": {
        "title": "CAP Monteur en installations sanitaires",
        "description": "Révisions complètes CAP Monteur en installations sanitaires.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_sanitaire_100",
        "icon": "🚰",
        "color": CMA_TURQUOISE,
    },
    "cap_serrurier_metallier_100": {
        "title": "CAP Serrurier-métallier",
        "description": "Révisions complètes CAP Serrurier-métallier.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_serrurier_metallier_100",
        "icon": "🔐",
        "color": CMA_TURQUOISE,
    },
    "cap_thermique_100": {
        "title": "CAP Monteur en installations physiques / thermiques",
        "description": "Révisions complètes CAP Monteur en installations thermiques.",
        "path": "quizzes.quiz_cap_metiers.quiz_cap_thermique_100",
        "icon": "🔥",
        "color": CMA_TURQUOISE,
    },

    # ----- CAP Matières générales -----
    "cap_anglais_1": {"title": "CAP Matières générales – Anglais (quiz 1)", "description": "Révisions d'anglais – série 1.", "path": "quizzes.quiz_cap_generaux.quiz_cap_anglais_1", "icon": "🇬🇧", "color": CMA_BLEU_MARINE},
    "cap_anglais_2": {"title": "CAP Matières générales – Anglais (quiz 2)", "description": "Révisions d'anglais – série 2.", "path": "quizzes.quiz_cap_generaux.quiz_cap_anglais_2", "icon": "🇬🇧", "color": CMA_BLEU_MARINE},
    "cap_espagnol_1": {"title": "CAP Matières générales – Espagnol (quiz 1)", "description": "Révisions d'espagnol – série 1.", "path": "quizzes.quiz_cap_generaux.quiz_cap_espagnol_1", "icon": "🇪🇸", "color": CMA_BLEU_MARINE},
    "cap_espagnol_2": {"title": "CAP Matières générales – Espagnol (quiz 2)", "description": "Révisions d'espagnol – série 2.", "path": "quizzes.quiz_cap_generaux.quiz_cap_espagnol_2", "icon": "🇪🇸", "color": CMA_BLEU_MARINE},
    "cap_francais_1": {"title": "CAP Matières générales – Français (quiz 1)", "description": "Révisions de français – série 1.", "path": "quizzes.quiz_cap_generaux.quiz_cap_francais_1", "icon": "📘", "color": CMA_BLEU_MARINE},
    "cap_francais_2": {"title": "CAP Matières générales – Français (quiz 2)", "description": "Révisions de français – série 2.", "path": "quizzes.quiz_cap_generaux.quiz_cap_francais_2", "icon": "📗", "color": CMA_BLEU_MARINE},
    "cap_histoire_geographie_1": {"title": "CAP Matières générales – Histoire-Géographie (quiz 1)", "description": "Révisions d'histoire-géographie – série 1.", "path": "quizzes.quiz_cap_generaux.quiz_cap_histoire_geographie_1", "icon": "🌍", "color": CMA_BLEU_MARINE},
    "cap_histoire_geographie_2": {"title": "CAP Matières générales – Histoire-Géographie (quiz 2)", "description": "Révisions d'histoire-géographie – série 2.", "path": "quizzes.quiz_cap_generaux.quiz_cap_histoire_geographie_2", "icon": "🗺️", "color": CMA_BLEU_MARINE},
    "cap_mathematique_1": {"title": "CAP Matières générales – Mathématiques (quiz 1)", "description": "Révisions de mathématiques – série 1.", "path": "quizzes.quiz_cap_generaux.quiz_cap_mathematique_1", "icon": "➗", "color": CMA_BLEU_MARINE},
    "cap_mathematique_2": {"title": "CAP Matières générales – Mathématiques (quiz 2)", "description": "Révisions de mathématiques – série 2.", "path": "quizzes.quiz_cap_generaux.quiz_cap_mathematique_2", "icon": "✖️", "color": CMA_BLEU_MARINE},
    "cap_pse_1": {"title": "CAP Matières générales – PSE (quiz 1)", "description": "Révisions de Prévention Santé Environnement – série 1.", "path": "quizzes.quiz_cap_generaux.quiz_cap_pse_1", "icon": "🩺", "color": CMA_BLEU_MARINE},
    "cap_pse_2": {"title": "CAP Matières générales – PSE (quiz 2)", "description": "Révisions de Prévention Santé Environnement – série 2.", "path": "quizzes.quiz_cap_generaux.quiz_cap_pse_2", "icon": "🏥", "color": CMA_BLEU_MARINE},
    "cap_science_physique_1": {"title": "CAP Matières générales – Sciences physiques (quiz 1)", "description": "Révisions de sciences physiques – série 1.", "path": "quizzes.quiz_cap_generaux.quiz_cap_science_physique_1", "icon": "🔬", "color": CMA_BLEU_MARINE},
    "cap_science_physique_2": {"title": "CAP Matières générales – Sciences physiques (quiz 2)", "description": "Révisions de sciences physiques – série 2.", "path": "quizzes.quiz_cap_generaux.quiz_cap_science_physique_2", "icon": "⚗️", "color": CMA_BLEU_MARINE},

    # ----- CS -----
    "cs_coiffure_coupe_couleur_100": {
        "title": "Certificat de spécialisation coiffure coupe couleur",
        "description": "Révisions complètes CS Coiffure coupe couleur.",
        "path": "quizzes.quiz_cs_metiers.quiz_cs_coiffure_coupe_couleur_100",
        "icon": "💇",
        "color": CMA_ROUGE_WEB,
    },

    # ----- BAC PRO Matières générales -----
    "bacpro_anglais": {"title": "BAC PRO Matières générales – Anglais", "description": "Révisions d'anglais – BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_anglais", "icon": "🇬🇧", "color": CMA_BLEU_MARINE},
    "bacpro_anglais_2": {"title": "BAC PRO Matières générales – Anglais (quiz 2)", "description": "Révisions d'anglais – série 2 BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_anglais_2", "icon": "🇬🇧", "color": CMA_BLEU_MARINE},
    "bacpro_espagnol": {"title": "BAC PRO Matières générales – Espagnol", "description": "Révisions d'espagnol – BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_espagnol", "icon": "🇪🇸", "color": CMA_BLEU_MARINE},
    "bacpro_espagnol_2": {"title": "BAC PRO Matières générales – Espagnol (quiz 2)", "description": "Révisions d'espagnol – série 2 BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_espagnol_2", "icon": "🇪🇸", "color": CMA_BLEU_MARINE},
    "bacpro_francais": {"title": "BAC PRO Matières générales – Français", "description": "Révisions de français – BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_francais", "icon": "📘", "color": CMA_BLEU_MARINE},
    "bacpro_francais_2": {"title": "BAC PRO Matières générales – Français (quiz 2)", "description": "Révisions de français – série 2 BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_francais_2", "icon": "📘", "color": CMA_BLEU_MARINE},
    "bacpro_histoire_geographie": {"title": "BAC PRO Matières générales – Histoire-Géographie", "description": "Révisions d'histoire-géographie – BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_histoire_geographie", "icon": "🌍", "color": CMA_BLEU_MARINE},
    "bacpro_histoire_geographie_2": {"title": "BAC PRO Matières générales – Histoire-Géographie (quiz 2)", "description": "Révisions d'histoire-géographie – série 2 BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_histoire_geographie_2", "icon": "🌍", "color": CMA_BLEU_MARINE},
    "bacpro_enseignement_moral_et_civique": {"title": "BAC PRO Matières générales – Enseignement moral et civique", "description": "Révisions d'EMC – BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_enseignement_moral_et_civique", "icon": "🕊️", "color": CMA_BLEU_MARINE},
    "bacpro_mathematique": {"title": "BAC PRO Matières générales – Mathématiques", "description": "Révisions de mathématiques – BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_mathematique", "icon": "📐", "color": CMA_BLEU_MARINE},
    "bacpro_mathematique_2": {"title": "BAC PRO Matières générales – Mathématiques (quiz 2)", "description": "Révisions de mathématiques – série 2 BAC PRO.", "path": "quizzes.quiz_bacpro_generaux.quiz_bacpro_mathematique_2", "icon": "📐", "color": CMA_BLEU_MARINE},
}

# -----------------------
# COULEURS PAR THÈME (Quiz en cours)
# -----------------------

THEME_COLORS = {
    1: CMA_ROUGE_WEB,
    2: CMA_BLEU_MARINE,
    3: CMA_TURQUOISE,
    4: CMA_MOUTARDE,
    5: CMA_ROUGE,
}

def inject_cma_theme():
    """Injecte la charte graphique de la CMA Occitanie avec isolation stricte de la sidebar"""
    st.markdown("""
    <style>
    /* Importation des polices officielles Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto+Slab:wght@100..900&display=swap');

    /* =========================================================================
       ☀️ CONFIGURATION DE BASE (MODE CLAIR STABLE)
       ========================================================================= */
    /* Zone principale : Fond de soutien beige */
    .stApp {
        background-color: #F8F0E3 !important;
        font-family: 'Montserrat', sans-serif;
    }

    /* Titres et textes de la zone centrale uniquement (Bleu Marine) */
    .main h1, .main h2, .main h3, .main p, .main span, .main label {
        color: #0F3250 !important;
    }

    /* Conteneurs Expanders centraux */
    .stContainer .stExpander, div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #0F3250 !important;
        border-radius: 8px;
    }

    /* --- SIDEBAR VERROUILLÉE (Le code stable d'origine) --- */
    section[data-testid="stSidebar"] {
        background-color: #0F3250 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stSidebarHeader"] {
        background-color: #F8F0E3 !important;
        border-bottom: 1px solid #B0D2D9;
        padding: 0.6rem 1rem !important;
        border-radius: 0 0 12px 12px !important;
        margin: 0 8px 1.5rem 8px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stSidebarHeader"]::before {
        content: "Navigation" !important;
        color: #0F3250 !important;
        font-family: 'Roboto Slab', serif !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        display: inline-block !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stSidebarHeader"] button,
    section[data-testid="stSidebar"] button[data-testid="sidebar-close-button"],
    section[data-testid="stSidebarCollapse"] button {
        opacity: 1 !important;
        visibility: visible !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stSidebarHeader"] button svg,
    section[data-testid="stSidebar"] button[data-testid="sidebar-close-button"] svg,
    section[data-testid="stSidebarCollapse"] button svg,
    div[class*="StyledSidebarCloseButton"] button svg {
        fill: #0F3250 !important;
        color: #0F3250 !important;
        opacity: 1 !important;
        width: 20px !important;
        height: 20px !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stSidebarHeader"] button:hover svg {
        fill: #CD493D !important;
        color: #CD493D !important;
    }

    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] caption {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] .stButton button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid #B0D2D9 !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background-color: #CD493D !important;
        border-color: #CD493D !important;
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] .stCaption {
        color: #B0D2D9 !important;
    }

    /* --- BOUTONS ZONE CENTRALE --- */
    .stApp .stButton button {
        font-family: 'Montserrat', sans-serif;
        background-color: #ffffff;
        color: #0F3250;
        border: 2px solid #0F3250;
        border-radius: 8px;
        transition: all 0.2s ease;
    }

    .stApp .stButton button:hover {
        background-color: #0F3250;
        color: #ffffff;
    }

    .stApp .stButton button[kind="primary"] {
        background-color: #CD493D;
        color: #ffffff;
        border: 2px solid #CD493D;
        font-weight: 700;
    }

    .stApp .stButton button[kind="primary"]:hover {
        background-color: #A8131D;
        border-color: #A8131D;
    }


    /* =========================================================================
       🌙 ADAPTATION MODE SOMBRE (CIBLAGE CHIRURGICAL APPLIQUÉ UNIQUEMENT AU CENTRE)
       ========================================================================= */
    @media (prefers-color-scheme: dark) {
        /* Seul le fond de la zone centrale bascule en Bleu Marine */
        .main {
            background-color: #0F3250 !important;
        }
        
        /* Seuls les textes de la zone centrale passent en blanc */
        .main h1, .main h2, .main h3, .main p, .main span, .main label {
            color: #ffffff !important;
        }
        
        /* Adaptation des boutons de la zone centrale */
        .main .stButton button {
            color: #ffffff !important;
            border: 2px solid #ffffff !important;
            background-color: transparent !important;
        }
        .main .stButton button:hover {
            background-color: #ffffff !important;
            color: #0F3250 !important;
        }

        /* Adaptation des conteneurs expanders de la zone centrale */
        .main .stExpander, .main div[data-testid="stExpander"] {
            background-color: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid #ffffff !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

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

# -----------------------
# STATE SPÉCIFIQUE À LA NAVIGATION
# -----------------------

# Liste exhaustive de toutes les variables nécessaires au fonctionnement
default_states = {
    "selected_quiz_key": None,
    "current_theme": None,
    "current_question_index": 0,
    "score": 0,
    "theme_scores": {},
    "show_correction": False,
    "last_is_correct": None,
    "shuffled_questions": None,
    "shuffled_answers": {},
    "selected_level": None,
    "selected_cap_family": None,
    "selected_cap_general_subject": None,
    "show_quit_confirmation": False,
    "ui_mode": UIMode.APP,
    "answer_locked": False,      # <--- Ajout crucial
    "selected_answer": None,     # <--- Ajout crucial
    "theme_attempt_counter": 0   # <--- Ajout crucial
}

# Initialisation automatique
for key, value in default_states.items():
    if key not in st.session_state:
        st.session_state[key] = value


def show_entry_screen():
    inject_cma_theme()
    
    # Utilisation d'un container natif avec un style en ligne strict pour l'en-tête
    with st.container():
        st.markdown("""
        <div style="background-color: #0F3250; padding: 2.5rem 1rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h1 style="color: #ffffff; font-family: 'Roboto Slab', serif; margin: 0 0 0.5rem 0; font-size: 2.2rem; font-weight: 800;">Plateforme de révision CFA CMAR</h1>
            <p style="color: #F8F0E3; font-family: 'Montserrat', sans-serif; margin: 0; font-size: 1.1rem; opacity: 0.95;">Révisez par niveau et métier.</p>
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
            st.markdown('<form action="javascript:void(0);" style="display:none;"><input type="text" autocomplete="username"><input type="password" autocomplete="current-password"></form>', unsafe_allow_html=True)
            
            user = st.text_input("Utilisateur", key="l_user", autocomplete="username")
            pw = st.text_input("Mot de passe", type="password", key="l_pw", autocomplete="current-password")
            
            if st.button("Se connecter", use_container_width=True, type="primary"):
                if user and pw:
                    success, msg = login_user(user, pw)
                    if success:
                        st.session_state.username = user.strip().lower()
                        with st.spinner("Chargement de votre profil..."):
                            st.session_state.user_stats = get_user_stats(st.session_state.username)
                            st.session_state.user_scores = load_user_scores(st.session_state.username)
                        st.session_state.auth_stage = "logged_in"
                        st.rerun()
                    else:
                        st.error(msg)
            
            if st.button("Pas de compte ? Créer un profil", use_container_width=True):
                st.session_state.auth_mode = "signup"
                st.rerun()
        else:
            st.subheader("🆕 Inscription")
            st.markdown('<form action="javascript:void(0);" style="display:none;"><input type="text" autocomplete="username"><input type="password" autocomplete="new-password"></form>', unsafe_allow_html=True)

            new_u = st.text_input("Pseudo", key="s_user", autocomplete="username")
            new_p = st.text_input("Mot de passe", type="password", key="s_pw", autocomplete="new-password")
            
            if st.button("Créer mon compte", use_container_width=True, type="primary"):
                if new_u and new_p:
                    success, msg = create_user(new_u, "", new_p)
                    if success:
                        st.balloons()
                        st.success("Compte créé ! Connectez-vous.")
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
    """Charge dynamiquement le quiz_data du fichier .py et y injecte les corrections depuis Google Sheets."""
    quiz_key = st.session_state.selected_quiz_key
    if quiz_key is None:
        return None
    
    quiz_path = QUIZZES[quiz_key].get("path")
    
    if quiz_path:
        try:
            # 1. Chargement initial du fichier .py d'origine
            module = importlib.import_module(quiz_path)
            importlib.reload(module)
            current_quiz_data = module.quiz_data
            
            # 2. Récupération des correctifs Sheets pour ce quiz précis
            from auth_persistence import get_modified_questions_for_quiz
            corrections = get_modified_questions_for_quiz(quiz_key)
            
            # 3. Injection des correctifs en mémoire vive à la volée
            if corrections:
                themes = current_quiz_data.get("themes", {})
                for theme_id, q_dict in corrections.items():
                    if theme_id in themes:
                        questions_list = themes[theme_id].get("questions", [])
                        for q_idx, updated_fields in q_dict.items():
                            # L'index stocké dans Sheets est humain (1, 2, 3...), on repasse en informatique (0, 1, 2...)
                            idx_tech = q_idx - 1 
                            if 0 <= idx_tech < len(questions_list):
                                # Remplacement chirurgical des éléments de la question
                                questions_list[idx_tech]['question'] = updated_fields['question']
                                questions_list[idx_tech]['answerOptions'] = updated_fields['answerOptions']
                                questions_list[idx_tech]['correction'] = updated_fields['correction']
            
            return current_quiz_data
        except Exception as e:
            st.error(f"Erreur de chargement ou d'injection du quiz : {e}")
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
    
    # --- CORRECTION DU BUG : Nettoyage strict du mode examen ---
    st.session_state.exam_mode = False
    st.session_state.exam_questions = []
    st.session_state.exam_user_answers = {}

    st.session_state.theme_scores = {}
    
    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    
    for num in quiz_data["themes"].keys():
        if num not in st.session_state.theme_scores[quiz_key]:
            st.session_state.theme_scores[quiz_key][num] = None


def go_back_to_main_menu():
    """Retour au menu des thèmes pour le quiz courant (sans effacer les scores)."""
    st.session_state.current_theme = None
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.show_correction = False
    st.session_state.last_is_correct = None
    st.session_state.shuffled_questions = None
    st.session_state.shuffled_answers = {}
    
    # --- CORRECTION DU BUG : Sécurité supplémentaire en sortie de thème ---
    st.session_state.exam_mode = False


def start_theme(theme_number: int):
    """Lance un thème, remet l'index de question et le score à zéro, et mélange les questions."""
    quiz_data = get_current_quiz_data()
    theme = quiz_data["themes"][theme_number]
    questions = theme["questions"]
    
    # --- CORRECTION : On marque l'index d'origine AVANT le mélange ---
    for i, q in enumerate(questions):
        q['original_index'] = i  # On stocke l'index 0, 1, 2... du fichier source
    
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

def start_exam_mode():
    """Génère un examen blanc de 30 questions (6 questions aléatoires par thème)."""
    quiz_data = get_current_quiz_data()
    if not quiz_data:
        st.error("Impossible de charger les données pour l'examen.")
        return

    all_exam_questions = []
    
    # Parcours de chaque thème du quiz pour piocher 6 questions
    for theme_id, theme_data in quiz_data["themes"].items():
        questions = theme_data["questions"].copy()
        
        # On injecte l'index d'origine et le numéro de thème avant le mélange pour les rapports d'erreur
        for i, q in enumerate(questions):
            q['original_index'] = i
            q['theme_origin'] = theme_id
            
        # Mélange des questions du thème courant
        random.shuffle(questions)
        
        # Sélection des 6 premières questions (ou de toutes si le thème en contient moins de 6)
        all_exam_questions.extend(questions[:6])
        
    # Mélange final de l'ensemble des 30 questions pour panacher l'examen
    random.shuffle(all_exam_questions)
    
    # Initialisation des variables d'état spécifiques à l'examen
    st.session_state.exam_mode = True
    st.session_state.exam_questions = all_exam_questions
    st.session_state.exam_user_answers = {}
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.selected_answer = None
    st.session_state.answer_locked = False
    st.session_state.show_correction = False
    
    if "theme_attempt_counter" not in st.session_state:
        st.session_state.theme_attempt_counter = 0
    st.session_state.theme_attempt_counter += 1


def get_current_exam_comment(score: int) -> str:
    """Retourne le commentaire sobre associé au score de l'examen blanc."""
    # Le barème est basé sur 30 questions
    if score == 30:
        return "INCROYABLE ! Un sans-faute parfait ! Vous avez détruit le quiz. Respect total !"
    elif 24 <= score <= 29:
        return "Excellent travail ! Le diplôme est à portée de main. Vous maîtrisez parfaitement votre sujet."
    elif 21 <= score <= 23:
        return "Examen validé ! Le score requis de 70% est atteint. Continuez ainsi pour sécuriser vos points."
    elif 15 <= score <= 20:
        return "Score encourageant mais encore trop juste. Révisez les thèmes où vous avez fait des erreurs avant de retenter l'examen."
    else:
        return "Niveau insuffisant. Prenez le temps de retravailler chaque thème un par un en mode entraînement classique."

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

def check_and_notify_new_badges():
    """Vérifie si de nouveaux badges ont été débloqués et affiche une notification."""
    if st.session_state.get("auth_stage") != "logged_in" or not st.session_state.get("username"):
        return

    from auth_persistence import get_user_stats, load_user_scores
    username = st.session_state.username
    
    # 1. Calculer les statistiques actuelles
    stats = get_user_stats(username)
    user_scores = load_user_scores(username)
    quizzes = user_scores.get("quizzes", {})

    validated_quiz_count = 0
    validated_cap, validated_bacpro, validated_bp, validated_bts, validated_cs = 0, 0, 0, 0, 0
    total_exam_attempts = 0
    has_high_exam_score = False

    for quiz_key, quiz_data_score in quizzes.items():
        scores = quiz_data_score.get("scores", {})
        exam_stats = quiz_data_score.get("exam_stats", {})
        
        total_exam_attempts += exam_stats.get("attempts", 0)
        if exam_stats.get("best_score", 0) >= 25:
            has_high_exam_score = True
            
        if not scores: continue
        
        total_correct, total_questions = 0, 0
        all_themes_completed = True
        for score_str in scores.values():
            if not isinstance(score_str, str): continue
            try:
                correct, total = map(int, score_str.split("/"))
                total_correct += correct
                total_questions += total
            except ValueError: 
                all_themes_completed = False

        if total_questions > 0:
            percentage = (total_correct / total_questions) * 100
            if all_themes_completed and percentage >= 70:
                validated_quiz_count += 1
                if quiz_key.startswith("cap_"): validated_cap += 1
                elif quiz_key.startswith("bacpro_"): validated_bacpro += 1
                elif quiz_key.startswith("bp_"): validated_bp += 1
                elif quiz_key.startswith("bts_"): validated_bts += 1
                elif quiz_key.startswith("cs_"): validated_cs += 1

    # 2. Évaluer les conditions des badges
    current_badges = set()
    if validated_quiz_count >= 1: current_badges.add("🎯 Premier quiz")
    if validated_quiz_count >= 5: current_badges.add("🏅 5 quiz validés")
    if stats.get("total_questions", 0) >= 100: current_badges.add("📚 100 questions")
    if stats.get("total_questions", 0) >= 300: current_badges.add("🧠 300 questions")
    if stats.get("average_percentage", 0) >= 80: current_badges.add("🔥 Moyenne ≥ 80%")
    if stats.get("average_percentage", 0) >= 90: current_badges.add("💎 Moyenne ≥ 90%")
    if validated_cap >= 3: current_badges.add("🏗️ Expert CAP")
    if validated_bacpro >= 2: current_badges.add("🏬 Expert BAC PRO")
    if (validated_bp >= 1 and validated_bts >= 1): current_badges.add("🎓 Spécialiste Sup")
    if stats.get("total_quizzes", 0) >= 10: current_badges.add("⏱️ Fidèle au poste")
    if total_exam_attempts >= 5: current_badges.add("⏳ Assiduité Examen")
    if has_high_exam_score: current_badges.add("⚡ Maîtrise Examen")

    # 3. Initialiser la mémoire si c'est la première vérification de la session
    if "earned_badges" not in st.session_state:
        st.session_state.earned_badges = current_badges
        return 

    # 4. Comparer et notifier
    new_badges = current_badges - st.session_state.earned_badges
    for badge in new_badges:
        st.toast(f"**Nouveau badge débloqué !**\n{badge}", icon="🏆")
        st.balloons()

    # 5. Mettre à jour la mémoire
    st.session_state.earned_badges = current_badges

def show_profile_page():
    if st.session_state.get("auth_stage") != "logged_in" or not st.session_state.get("username"):
        st.info("Connectez-vous pour accéder à votre profil.")
        return

    from auth_persistence import get_user_stats, export_user_scores_txt, load_user_scores, get_user_info
    
    username = st.session_state.username
    user_info = get_user_info(username)
    stats = get_user_stats(username)
    user_scores = load_user_scores(username)
    quizzes = user_scores.get("quizzes", {})

    # --- 1. CALCULS DES SCORES ET VALIDATIONS ---
    validated_quiz_count = 0
    validated_cap, validated_bacpro = 0, 0
    validated_bp, validated_bts, validated_cs = 0, 0, 0
    
    # Variables de suivi spécifiques pour le calcul des deux nouveaux trophées
    total_exam_attempts_all_quizzes = 0
    has_high_exam_score = False

    for quiz_key, quiz_data_score in quizzes.items():
        scores = quiz_data_score.get("scores", {})
        
        # Extraction et cumul des statistiques d'examen blanc
        exam_stats = quiz_data_score.get("exam_stats", {})
        attempts = exam_stats.get("attempts", 0)
        best_score = exam_stats.get("best_score", 0)
        
        total_exam_attempts_all_quizzes += attempts
        if best_score >= 25:
            has_high_exam_score = True
            
        if not scores: continue
        
        total_correct, total_questions = 0, 0
        all_themes_completed = True
        for score_str in scores.values():
            if not isinstance(score_str, str): continue
            try:
                correct, total = map(int, score_str.split("/"))
                total_correct += correct
                total_questions += total
            except ValueError: all_themes_completed = False

        if total_questions > 0:
            percentage = (total_correct / total_questions) * 100
            if all_themes_completed and percentage >= 70:
                validated_quiz_count += 1
                if quiz_key.startswith("cap_"): validated_cap += 1
                elif quiz_key.startswith("bacpro_"): validated_bacpro += 1
                elif quiz_key.startswith("bp_"): validated_bp += 1
                elif quiz_key.startswith("bts_"): validated_bts += 1
                elif quiz_key.startswith("cs_"): validated_cs += 1

    # --- 2. FORMATAGE DE LA DATE ---
    created_at_raw = user_info.get('created_at')
    date_display, relative_display = "N/A", ""
    if created_at_raw:
        try:
            dt = datetime.fromisoformat(created_at_raw)
            mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
            date_display = f"le {dt.day} {mois[dt.month - 1]} {dt.year}"
            now = datetime.now()
            y, m, d = now.year - dt.year, now.month - dt.month, now.day - dt.day
            if d < 0: m -= 1; d += 30
            if m < 0: y -= 1; m += 12
            parts = []
            if y > 0: parts.append(f"{y} {'an' if y == 1 else 'ans'}")
            if m > 0: parts.append(f"{m} mois")
            if d > 0: parts.append(f"{d} {'jour' if d == 1 else 'jours'}")
            if parts:
                txt = ', '.join(parts[:-1]) + ' et ' + parts[-1] if len(parts) > 1 else parts[0]
                relative_display = f"<br><span style='font-size:0.85rem; opacity:0.7;'>Membre depuis {txt}</span>"
        except Exception: date_display = created_at_raw

    # --- 3. EN-TÊTE MODERNE ---
    st.markdown(f"""
    <div style="background: white; padding: 1.5rem; border-radius: 15px; border-left: 5px solid #6A11CB; box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin-bottom: 2rem;">
        <h2 style="margin:0; color:#1f2937;">👤 Profil de {username.capitalize()}</h2>
        <p style="color: gray; margin:0.5rem 0 0 0;">Compte créé {date_display} {relative_display}</p>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. CARTES DE STATISTIQUES ---
    st.subheader("📊 Progression globale")
    c1, c2, c3, c4 = st.columns(4)
    card_style = "background:#f8f9fa; padding:0.8rem; border-radius:12px; text-align:center; border: 1px solid #e5e7eb;"
    
    c1.markdown(f"<div style='{card_style}'><span style='font-size:0.75rem; color:gray;'>QUIZ JOUÉS</span><br><b style='font-size:1.3rem;'>{stats.get('total_quizzes', 0)}</b></div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='{card_style}'><span style='font-size:0.75rem; color:gray;'>VALIDÉS (70%+)</span><br><b style='font-size:1.3rem; color:#6A11CB;'>{validated_quiz_count}</b></div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='{card_style}'><span style='font-size:0.75rem; color:gray;'>QUESTIONS</span><br><b style='font-size:1.3rem;'>{stats.get('total_questions', 0)}</b></div>", unsafe_allow_html=True)
    
    moyenne = stats.get('average_percentage', 0)
    color_moy = "#22c55e" if moyenne >= 70 else "#f59e0b" if moyenne >= 50 else "#ef4444"
    c4.markdown(f"<div style='{card_style}'><span style='font-size:0.75rem; color:gray;'>RÉUSSITE</span><br><b style='font-size:1.3rem; color:{color_moy};'>{moyenne}%</b></div>", unsafe_allow_html=True)

    # --- 5. PROGRESSION PAR DIPLÔME ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📈 Objectifs par diplôme")
    obj = 5
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.write(f"**CAP** ({validated_cap}/{obj})")
        st.progress(min(validated_cap/obj, 1.0))
        st.write(f"**BAC PRO** ({validated_bacpro}/{obj})")
        st.progress(min(validated_bacpro/obj, 1.0))
    with col_p2:
        val_sup = validated_bp + validated_bts + validated_cs
        st.write(f"**BP / BTS / CS** ({val_sup}/{obj})")
        st.progress(min(val_sup/obj, 1.0))

    # --- 6. SYSTÈME DE BADGES ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏆 Vos Badges")
    badges = [
        {"nom": "🎯 Premier quiz", "cond": validated_quiz_count >= 1},
        {"nom": "🏅 5 quiz validés", "cond": validated_quiz_count >= 5},
        {"nom": "📚 100 questions", "cond": stats.get("total_questions", 0) >= 100},
        {"nom": "🧠 300 questions", "cond": stats.get("total_questions", 0) >= 300},
        {"nom": "🔥 Moyenne ≥ 80%", "cond": stats.get("average_percentage", 0) >= 80},
        {"nom": "💎 Moyenne ≥ 90%", "cond": stats.get("average_percentage", 0) >= 90},
        {"nom": "🏗️ Expert CAP", "cond": validated_cap >= 3},
        {"nom": "🏬 Expert BAC PRO", "cond": validated_bacpro >= 2},
        {"nom": "🎓 Spécialiste Sup", "cond": (validated_bp >= 1 and validated_bts >= 1)},
        {"nom": "⏱️ Fidèle au poste", "cond": stats.get("total_quizzes", 0) >= 10},
        {"nom": "⏳ Assiduité Examen (5 examens blancs)", "cond": total_exam_attempts_all_quizzes >= 5},
        {"nom": "⚡ Maîtrise Examen (Score ≥ 25/30)", "cond": has_high_exam_score}
    ]
    
    html_badges = "<div style='display:flex; flex-wrap:wrap; gap:0.6rem;'>"
    for b in badges:
        if b["cond"]:
            style = "background:linear-gradient(135deg, #6A11CB 0%, #2575FC 100%); color:white; border:none; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"
        else:
            style = "background:#f3f4f6; border:1px solid #d1d5db; color:#9ca3af; opacity:0.4; filter:grayscale(100%);"
        html_badges += f"<span style='{style} border-radius:12px; padding:0.4rem 0.9rem; font-size:0.8rem; font-weight:600;'>{b['nom']}</span>"
    st.markdown(html_badges + "</div>", unsafe_allow_html=True)

    # --- 7. DÉTAIL DES QUIZ AVEC FILTRE ---
    st.markdown("---")
    st.subheader("📜 Détail par quiz")
    if not quizzes:
        st.info("Aucun quiz complété pour le moment.")
    else:
        level_filter = st.selectbox("Filtrer par niveau", ["Tous", "CAP", "BAC PRO", "BP", "BTS", "CS"])
        for q_key, q_data in quizzes.items():
            if level_filter != "Tous" and not q_key.startswith(level_filter.lower().replace(" ", "")): 
                continue
            
            quiz_info = QUIZZES.get(q_key, {})
            with st.expander(f"📁 {quiz_info.get('title', q_key)}"):
                # Affichage des thèmes classiques
                for t_num, s_str in q_data.get("scores", {}).items():
                    st.write(f"**Thème {t_num}** : `{s_str}`")
                
                # Bloc d'affichage des performances de l'examen blanc si existant
                e_stats = q_data.get("exam_stats", {})
                if e_stats.get("attempts", 0) > 0:
                    st.markdown("---")
                    st.write(f"📝 **Tentatives d'examen blanc** : {e_stats['attempts']}")
                    st.write(f"🏆 **Meilleur score à l'examen** : {e_stats['best_score']} / 30")

    # --- 8. ACTIONS ---
    st.markdown("<br>", unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn1:
        if st.button("⬅️ Retour", use_container_width=True):
            st.session_state.ui_mode = UIMode.APP
            st.rerun()
    with col_btn2:
        if st.button("🔄 Actualiser", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    with col_btn3:
        report_text = export_user_scores_txt(username)
        st.download_button("📄 Mon Bilan (TXT)", data=report_text, file_name=f"bilan_{username}.txt", use_container_width=True)

def show_admin_reports_page():
    st.markdown("<h2 style='text-align:center;'>🛠️ Gestion & Édition des Questions</h2>", unsafe_allow_html=True)
    from auth_persistence import get_all_reports, delete_report, save_modified_question
    import importlib
    
    reports = get_all_reports()
    
    if st.button("⬅️ Revenir aux quiz", use_container_width=True):
        st.session_state.ui_mode = UIMode.APP
        st.rerun()

    st.markdown("---")

    if not reports:
        st.success("✅ Aucun signalement en attente.")
        return

    st.info(f"Il y a actuellement **{len(reports)}** signalement(s) à traiter.")

    for r in reports:
        report_id = r['id']
        quiz_key = r.get('quiz') 
        
        try:
            theme_id = int(float(r.get('theme', 0)))
            q_idx = int(float(r.get('q_idx', 1))) - 1
        except:
            theme_id, q_idx = 0, 0

        quiz_info = QUIZZES.get(quiz_key)
        display_title = quiz_info['title'] if quiz_info else quiz_key

        with st.expander(f"🚩 Rapport #{report_id} : {display_title} (Thème {theme_id}, Question {q_idx + 1})"):
            st.error(f"**Problème signalé :** {r['reason']}")
            
            if 'question' in r and r['question']:
                st.warning(f"**Texte envoyé par l'élève :**\n\n{r['question']}")
            
            if quiz_info:
                try:
                    module = importlib.import_module(quiz_info['path'])
                    importlib.reload(module)
                    current_quiz_data = module.quiz_data
                    
                    themes = current_quiz_data.get("themes", {})
                    if theme_id in themes:
                        questions_list = themes[theme_id].get("questions", [])
                        if 0 <= q_idx < len(questions_list):
                            question_to_edit = questions_list[q_idx]
                            
                            st.markdown("---")
                            new_q_text = st.text_area("Libellé de la question", value=question_to_edit['question'], key=f"edit_q_{report_id}")
                            
                            new_options = []
                            for i, opt in enumerate(question_to_edit['answerOptions']):
                                col_txt, col_ok = st.columns([3, 1])
                                o_txt = col_txt.text_input(f"Option {chr(65+i)}", value=opt['text'], key=f"opt_{report_id}_{i}")
                                o_ok = col_ok.toggle("Correct", value=opt['isCorrect'], key=f"corr_{report_id}_{i}")
                                new_options.append({"text": o_txt, "isCorrect": o_ok})
                            
                            new_corr = st.text_area("Correction", value=question_to_edit.get('correction', ''), key=f"edit_c_{report_id}")

                            c1, c2 = st.columns(2)
                            if c1.button("💾 Enregistrer & Publier sur Sheets", key=f"save_{report_id}", use_container_width=True, type="primary"):
                                # Sauvegarde sécurisée dans Google Sheets (Numéro humain de question = q_idx + 1)
                                success = save_modified_question(
                                    quiz_key=quiz_key,
                                    theme_id=theme_id,
                                    question_idx=q_idx + 1,
                                    question_text=new_q_text,
                                    options_list=new_options,
                                    correction_text=new_corr
                                )
                                
                                if success:
                                    delete_report(report_id)
                                    st.success("✅ Mis à jour dans Google Sheets et synchronisé !")
                                    st.rerun()
                                else:
                                    st.error("❌ Erreur lors de l'enregistrement sur Google Sheets.")

                            if c2.button("🗑️ Supprimer le rapport", key=f"del_{report_id}", use_container_width=True):
                                delete_report(report_id)
                                st.rerun()
                        else: st.warning("Index de question introuvable.")
                    else: st.warning("Thème introuvable.")
                except Exception as e: st.error(f"Erreur d'accès aux données : {e}")
            else: st.error("Quiz non localisé.")

def show_admin_dashboard():
    st.markdown("<h2 style='text-align:center;'>📊 Statistiques Globales</h2>", unsafe_allow_html=True)
    from auth_persistence import get_global_stats
    
    df_stats = get_global_stats()
    
    if df_stats is None or df_stats.empty:
        st.warning("Aucune donnée de score disponible pour le moment.")
        return

    # --- INDICATEURS CLÉS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Élèves", len(df_stats['user'].unique()))
    col2.metric("Moyenne Générale", f"{round(df_stats['percent'].mean())}%")
    col3.metric("Quiz joués", len(df_stats))

    # --- CLASSEMENT DES QUIZ ---
    st.markdown("### 🏆 Performance par Quiz")
    # On groupe par Quiz pour voir la moyenne de réussite
    quiz_perf = df_stats.groupby('quiz')['percent'].mean().sort_values(ascending=False).reset_index()
    
    # On rend les noms plus jolis
    quiz_perf['quiz'] = quiz_perf['quiz'].str.replace("_", " ").str.title()
    
    st.table(quiz_perf.rename(columns={"quiz": "Nom du Quiz", "percent": "Réussite Moyenne (%)"}))

    # --- ALERTES (Quiz les plus difficiles) ---
    hardest = quiz_perf.iloc[-1]
    st.error(f"⚠️ **Attention :** Le quiz '{hardest['quiz']}' semble le plus difficile ({round(hardest['percent'])}% de réussite).")

# -----------------------
# INTERFACE : SÉLECTEUR DE NIVEAU
# -----------------------

# -----------------------
# INTERFACE : SÉLECTEUR DE NIVEAU
# -----------------------

def show_active_pause_barrage():
    """Affiche le barrage si une pause est active. Retourne True si l'écran est bloqué, False sinon."""
    if st.session_state.get("auth_stage") == "logged_in" and st.session_state.get("username"):
        from auth_persistence import get_active_pause, clear_quiz_state
        active_pause = get_active_pause(st.session_state.username)
        
        if active_pause:
            paused_quiz_key = active_pause["quiz_key"]
            
            # --- Mécanique de rechargement en mémoire ---
            if st.session_state.get("trigger_resume_action"):
                state_data = active_pause["state_data"]
                
                # On restaure absolument tout le contexte du quiz
                st.session_state.selected_quiz_key = paused_quiz_key
                st.session_state.exam_mode = state_data.get("exam_mode", False)
                st.session_state.current_question_index = state_data.get("current_question_index", 0)
                st.session_state.score = state_data.get("score", 0)
                st.session_state.current_theme = state_data.get("current_theme")
                st.session_state.shuffled_questions = state_data.get("shuffled_questions")
                st.session_state.shuffled_answers = state_data.get("shuffled_answers", {})
                st.session_state.exam_questions = state_data.get("exam_questions")
                st.session_state.exam_user_answers = state_data.get("exam_user_answers", {})
                
                # On débloque l'interface
                st.session_state.answer_locked = False
                st.session_state.show_correction = False
                st.session_state.trigger_resume_action = False
                
                # Consommation de la sauvegarde : on nettoie la base de données
                clear_quiz_state(st.session_state.username, paused_quiz_key)
                
                # On redirige vers l'écran de la question
                st.rerun()

            # --- Interface visuelle du barrage ---
            st.warning("⚠️ **Session en cours détectée**")
            
            st.markdown(
                f"""
                <div style="background-color: #ffffff; border: 1px solid #F1BA33; border-left: 6px solid #F1BA33; border-radius: 8px; padding: 1.5rem; margin-bottom: 2rem;">
                    <h3 style="color: #866939; font-family: 'Roboto Slab'; margin-top: 0;">Entraînement suspendu</h3>
                    <p style="font-family: 'Montserrat'; color: #333333;">
                        Vous avez une partie en pause sur le quiz <strong>{paused_quiz_key.replace('_', ' ').upper()}</strong>.<br>
                        Afin de garantir votre progression, vous devez la terminer ou l'annuler avant de pouvoir lancer un nouveau quiz.
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            col_rep, col_del = st.columns(2)
            with col_rep:
                if st.button("▶️ Reprendre la session", use_container_width=True, type="primary"):
                    st.session_state.trigger_resume_action = True
                    st.rerun()
            with col_del:
                if st.button("🗑️ Annuler et perdre la progression", use_container_width=True):
                    clear_quiz_state(st.session_state.username, paused_quiz_key)
                    st.toast("🗑️ Pause supprimée. Vous pouvez naviguer librement.")
                    st.rerun()
            
            return True # Le barrage est actif, il faut bloquer le reste
    return False # Aucune pause, on laisse passer

def show_level_selector():
    # --- 🛡️ BARRAGE DE REPRISE (PAUSE OBLIGATOIRE) ---
    if show_active_pause_barrage():
        return
    # ------------------------------------------------

    with st.container():
        st.markdown("""
        <div style="background-color: #0F3250; padding: 2.5rem 1rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 2.5rem;">
            <h1 style="color: #ffffff; font-family: 'Roboto Slab', serif; margin: 0 0 0.5rem 0; font-size: 2.6rem; font-weight: 800;">E-Révisions CMA</h1>
            <p style="color: #F8F0E3; font-family: 'Montserrat', sans-serif; margin: 0; font-size: 1.1rem; opacity: 0.95;">Chambre de Métiers et de l'Artisanat d'Occitanie</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(
        "<h2 style='text-align:center; margin-bottom:2.5rem; color:#0F3250; font-family:\"Roboto Slab\"; font-size:1.6rem;'>Choisissez votre niveau de formation</h2>",
        unsafe_allow_html=True
    )

    # Configuration des couleurs cibles et institutionnelles selon le livret
    level_colors = {
        "CAP": "#5CC6A5",       # Turquoise (Cible Apprentis)
        "BP": "#F1BA33",        # Moutarde (Cible Artisans)
        "BAC PRO": "#CD493D",   # Rouge Éclairé (Dynamisme)
        "BTS": "#0F3250",       # Bleu Marine (Institutionnel)
        "CS": "#A8131D",        # Rouge CMA (Marqueur fort)
    }
    
    level_icons = {
        "CAP": "🎓",
        "BP": "🏆",
        "BAC PRO": "💼",
        "BTS": "🎯",
        "CS": "⭐",
    }

    st.markdown("<div style='max-width:900px; margin:0 auto;'>", unsafe_allow_html=True)
    
    cols = st.columns(len(LEVELS))
    
    for i, level in enumerate(LEVELS):
        color = level_colors.get(level, "#0F3250")
        icon = level_icons.get(level, "📚")
        enabled = level in ["CAP", "BP", "BAC PRO", "BTS", "CS"]
        
        with cols[i]:
            # Remplacement du dégradé par un encart blanc massif propre avec bordure colorée (Charte p.59)
            st.markdown(
                f"""
                <div style="
                    background-color: #ffffff;
                    border: 1px solid #e5e7eb;
                    border-top: 6px solid {color};
                    border-radius: 8px;
                    padding: 1.5rem 1rem;
                    text-align: center;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.04);
                    min-height: 150px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    margin-bottom: 1rem;
                ">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
                    <div style="font-family: 'Roboto Slab', serif; font-size: 1.2rem; font-weight: 700; color: #0F3250; margin-bottom: 0.2rem;">{level}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            if enabled:
                # Bouton de validation d'accès au niveau
                if st.button(f"S'entraîner", key=f"btn_level_{level}", type="primary", use_container_width=True):
                    st.session_state.selected_level = level
                    st.session_state.selected_cap_family = None
                    st.session_state.selected_cap_general_subject = None
                    st.session_state.selected_quiz_key = None
                    st.session_state.current_theme = None
                    st.rerun()
            else:
                st.markdown(
                    f"<p style='text-align:center; color:#9ca3af; font-family:\"Montserrat\"; font-size:0.85rem; margin-top:-0.5rem;'>Bientôt disponible</p>",
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
    color = info.get("color", "#0F3250")

    # Génération d'encarts rectangulaires massifs selon la charte
    st.markdown(
        f"""
        <style>
        .quiz-card-{key} {{
            background-color: #ffffff;
            border-left: 6px solid {color};
            border-radius: 8px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
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
                f"<h1 style='font-size:2.8rem; margin:0; text-align:center;'>{info.get('icon', '')}</h1>",
                unsafe_allow_html=True,
            )
        with cols[1]:
            st.markdown(f"<span style='font-family:\"Roboto Slab\"; font-size:1.1rem; font-weight:700; color:#0F3250;'>{info['title']}</span>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin: 0.5rem 0; font-family:\"Montserrat\"; color:#555555;'>{info['description']}</p>", unsafe_allow_html=True)
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

def show_quiz_page():
    """Affiche la page d'accueil d'un quiz avec la liste de ses thèmes et l'accès à l'Examen Blanc."""
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    if not quiz_data or not quiz_key:
        st.error("Aucune donnée de quiz chargée.")
        if st.button("⬅️ Retour au menu"):
            go_back_to_main_menu()
            st.rerun()
        return

    # En-tête du quiz
    st.markdown(f"<h2 style='text-align:center; font-family:\"Roboto Slab\"; color:#0F3250;'>{quiz_data['title']}</h2>", unsafe_allow_html=True)
    if quiz_data.get("subtitle"):
        st.markdown(f"<p style='text-align:center; font-family:\"Montserrat\"; font-style:italic; color:#555555; margin-bottom:2rem;'>{quiz_data['subtitle']}</p>", unsafe_allow_html=True)

    # Bouton de retour général
    if st.button("⬅️ Choisir un autre quiz", use_container_width=True):
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

    st.markdown("---")
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

    st.markdown("---")
    st.markdown("<h3 style='font-family:\"Roboto Slab\"; color:#0F3250; margin-bottom:1.5rem;'>Thèmes d'entraînement</h3>", unsafe_allow_html=True)

    # Affichage de la liste des thèmes sous forme de boutons
    themes_dict = quiz_data["themes"]
    themes_keys = list(themes_dict.keys())
    
    for idx, num in enumerate(themes_keys):
        theme = themes_dict[num]
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{theme['name']}**")
        with col2:
            theme_score = quiz_scores.get(num)
            if theme_score:
                st.success(f"Complété ({theme_score})")
            else:
                st.warning("Non fait")

        color = THEME_COLORS.get(num, "#0F3250")
        st.markdown(f"""
        <style>
        div[data-testid="stHorizontalBlock"] div[data-basebutton-id="btn_theme_{num}"] button {{
            border-left: 6px solid {color} !important;
        }}
        </style>
        """, unsafe_allow_html=True)

        if st.button(f"Commencer le thème {num}", key=f"btn_theme_{num}", use_container_width=True):
            start_theme(num)
            st.rerun()

        # --- AJOUT DE LA SÉPARATION VISUELLE ---
        # On affiche une ligne fine grise sous chaque thème, sauf sous le tout dernier de la liste
        if idx < len(themes_keys) - 1:
            st.markdown("<hr style='margin: 1.5rem 0; border: 0; border-top: 1px solid #e5e7eb;'>", unsafe_allow_html=True)

    # =========================================================================
    # 📝 SECTION EXAMEN BLANC
    # =========================================================================

    st.markdown("---")
    st.markdown("<h4 style='font-family:\"Roboto Slab\"; color:#0F3250; margin-bottom:0.5rem;'>Évaluation finale</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-family:\"Montserrat\"; font-size:0.9rem; color:#555555; margin-bottom:1rem;'>Une fois que vous maîtrisez les différents thèmes, tentez l'examen blanc pluridisciplinaire dans les conditions réelles.</p>", unsafe_allow_html=True)
    
    if st.button("📝 Lancer un Examen Blanc (30 questions)", key="launch_exam_btn", use_container_width=True):
        start_exam_mode()
        st.rerun()


def show_question_screen():
    # Détection du mode examen ou entraînement classique
    is_exam = st.session_state.get("exam_mode", False)
    
    if is_exam:
        questions = st.session_state.exam_questions
        theme_name = "Examen Blanc Pluridisciplinaire"
        color = "#0F3250"  # Bleu Marine Institutionnel pour l'examen
    else:
        quiz_data = get_current_quiz_data()
        theme_number = st.session_state.current_theme
        theme = quiz_data["themes"][theme_number]
        theme_name = theme["name"]
        color = THEME_COLORS.get(theme_number, "#0F3250")
        if st.session_state.shuffled_questions:
            questions = st.session_state.shuffled_questions
        else:
            questions = theme["questions"]

    idx = st.session_state.current_question_index
    total_questions = len(questions)
    
    # En-tête de l'interface épuré
    st.markdown(f"<div style='margin-bottom: 0.5rem;'><span style='font-family:\"Montserrat\"; font-size:0.85rem; font-weight:600; color:#555555; text-transform: uppercase;'>{theme_name}</span></div>", unsafe_allow_html=True)
    
    # Barre de progression fine et moderne
    progress_percent = ((idx + 1) / total_questions) * 100
    st.markdown(f"""
    <div style='width:100%; background-color:#e5e7eb; border-radius:999px; height:8px; position:relative; margin-bottom:1.5rem; overflow:hidden;'>
        <div style='width:{progress_percent}%; background-color:{color}; height:100%; border-radius:999px; transition:width 0.4s ease;'></div>
    </div>
    <div style='text-align:right; margin-top:-1rem; margin-bottom:1.5rem;'><span style='font-family:\"Montserrat\"; font-size:0.85rem; font-weight:700; color:#0F3250;'>Question {idx + 1} sur {total_questions}</span></div>
    """, unsafe_allow_html=True)

    q = questions[idx] if idx < len(questions) else None
    if q is None:
        st.error("Erreur : question introuvable.")
        return

    orig_idx_tech = q.get('original_index', idx)
    theme_origin = q.get('theme_origin', st.session_state.current_theme)

    # Identifiant unique de question pour le mélange des réponses
    q_id = f"exam_{idx}" if is_exam else f"{theme_origin}_{idx}"
    
    if q_id not in st.session_state.shuffled_answers:
        options = [opt.copy() for opt in q["answerOptions"]]
        random.shuffle(options)
        for i, opt in enumerate(options):
            opt["key"] = chr(ord("A") + i)
        st.session_state.shuffled_answers[q_id] = options

    answer_options = st.session_state.shuffled_answers[q_id]
    
    # Affichage de la question stylisée
    st.markdown(f"<h3 style='margin: 1.5rem 0; font-size:1.3rem; font-weight:700; line-height:1.4; text-align:center; color:#0F3250;'>{q['question']}</h3>", unsafe_allow_html=True)

    # --- FONCTION INTERNE DE SAUVEGARDE DE LA PAUSE ---
    def trigger_pause_save():
        from auth_persistence import save_quiz_state
        state_data = {
            "exam_mode": st.session_state.get("exam_mode", False),
            "current_question_index": st.session_state.get("current_question_index", 0),
            "score": st.session_state.get("score", 0),
            "current_theme": st.session_state.get("current_theme"),
            "shuffled_questions": st.session_state.get("shuffled_questions"),
            "shuffled_answers": st.session_state.get("shuffled_answers", {}),
            "exam_questions": st.session_state.get("exam_questions"),
            "exam_user_answers": st.session_state.get("exam_user_answers", {})
        }
        save_quiz_state(st.session_state.username, st.session_state.selected_quiz_key, state_data)
        st.toast("✅ Progression sauvegardée en pause !", icon="⏸️")
        
        # --- CORRECTION ICI : Redirection vers l'écran d'accueil général ---
        st.session_state.exam_mode = False
        st.session_state.current_theme = None
        st.session_state.selected_quiz_key = None
        # On peut aussi s'assurer de réinitialiser le niveau si besoin
        # st.session_state.selected_level = None 

    # --- CAS PARAMÉTRABLE : MODE EXAMEN BLANC ---
    if is_exam:
        st.markdown(f"<style>div[data-testid='stButton'] > button {{ width: 100% !important; text-align: left !important; padding-left: 1.5rem !important; border-radius: 8px !important; min-height: 52px !important; font-family: 'Montserrat', sans-serif !important; }}</style>", unsafe_allow_html=True)

        # Récupération de la réponse déjà sauvegardée si l'élève revient en arrière
        current_saved_ans = st.session_state.exam_user_answers.get(idx, None)

        for opt in answer_options:
            is_selected = (current_saved_ans == opt["text"])
            label = f"🔹 {opt['key']}.  {opt['text']}" if is_selected else f"{opt['key']}.  {opt['text']}"
            btn_type = "primary" if is_selected else "secondary"
            
            if st.button(label, key=f"exam_opt_{idx}_{opt['key']}", use_container_width=True, type=btn_type):
                st.session_state.exam_user_answers[idx] = opt["text"]
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        col_q, col_p, col_a = st.columns([1, 1, 2], gap="small")
        
        with col_q:
            if st.button("⬅️ Quitter", use_container_width=True):
                st.session_state.show_quit_confirmation = True
                st.rerun()
                
        with col_p:
            if st.session_state.get("auth_stage") == "logged_in":
                if st.button("⏸️ Pause", use_container_width=True):
                    trigger_pause_save()
                    st.rerun()
            else:
                st.button("⏸️ Pause", use_container_width=True, disabled=True, help="Connectez-vous pour sauvegarder votre progression")
                
        with col_a:
            label_next = "Soumettre l'examen" if (idx + 1 == total_questions) else "Question suivante ➡️"
            if st.button(label_next, use_container_width=True, type="primary"):
                if idx not in st.session_state.exam_user_answers:
                    st.warning("Veuillez sélectionner une réponse avant de continuer.")
                else:
                    if idx + 1 == total_questions:
                        # Fin de l'examen, calcul automatique du score final
                        total_score = 0
                        for exam_idx, question_obj in enumerate(st.session_state.exam_questions):
                            user_ans = st.session_state.exam_user_answers.get(exam_idx)
                            correct_opt = next((o for o in question_obj["answerOptions"] if o["isCorrect"]), None)
                            if correct_opt and user_ans == correct_opt["text"]:
                                total_score += 1
                        st.session_state.score = total_score
                        st.session_state.current_question_index += 1
                        show_exam_result()
                    else:
                        st.session_state.current_question_index += 1
                        st.rerun()

    # --- CAS D'ORIGINE : ENTRAÎNEMENT CLASSIQUE PAR THÈME ---
    else:
        if not st.session_state.answer_locked:
            st.markdown(f"<style>div[data-testid='stButton'] > button {{ width: 100% !important; text-align: left !important; padding-left: 1.5rem !important; border-radius: 8px !important; min-height: 52px !important; font-family: 'Montserrat', sans-serif !important; }}</style>", unsafe_allow_html=True)

            for opt in answer_options:
                is_selected = (st.session_state.selected_answer == opt["text"])
                label = f"🔹 {opt['key']}.  {opt['text']}" if is_selected else f"{opt['key']}.  {opt['text']}"
                btn_type = "primary" if is_selected else "secondary"
                
                if st.button(label, key=f"opt_{q_id}_{opt['key']}_{st.session_state.get('theme_attempt_counter',0)}", use_container_width=True, type=btn_type):
                    st.session_state.selected_answer = opt["text"]
                    st.rerun()

            st.markdown("<br>", unsafe_allow_html=True)
            col_q, col_p, col_a = st.columns([1, 1, 2], gap="small")
            
            with col_q:
                if st.button("⬅️ Quitter", use_container_width=True):
                    st.session_state.show_quit_confirmation = True
                    st.rerun()
                    
            with col_p:
                if st.session_state.get("auth_stage") == "logged_in":
                    if st.button("⏸️ Pause", use_container_width=True):
                        trigger_pause_save()
                        st.rerun()
                else:
                    st.button("⏸️ Pause", use_container_width=True, disabled=True, help="Connectez-vous pour sauvegarder votre progression")
                    
            with col_a:
                if st.button("✅ Valider ma réponse", use_container_width=True, type="primary"):
                    if not st.session_state.selected_answer:
                        st.warning("Veuillez sélectionner une réponse avant de valider.")
                    else:
                        correct_opt = next((o for o in answer_options if o["isCorrect"]), None)
                        is_correct = (correct_opt and st.session_state.selected_answer == correct_opt["text"])
                        st.session_state.last_is_correct = is_correct
                        st.session_state.show_correction = True
                        st.session_state.answer_locked = True
                        if is_correct: st.session_state.score += 1
                        st.rerun()
        else:
            for opt in answer_options:
                is_correct_answer = opt["isCorrect"]
                is_user_answer = (st.session_state.selected_answer == opt["text"])
                
                if is_correct_answer: 
                    b_c, bg, t_c, icon = "#22c55e", "#d4edda", "#155724", "✅"
                elif is_user_answer: 
                    b_c, bg, t_c, icon = "#CD493D", "#f8d7da", "#721c24", "❌"
                else: 
                    b_c, bg, t_c, icon = "#e5e7eb", "#ffffff", "#1f2937", ""
                    
                st.markdown(f"<div style='border: 1px solid {b_c}; border-left: 6px solid {b_c}; border-radius: 8px; padding: 0.8rem 1.2rem; margin-bottom: 0.5rem; background: {bg}; color: {t_c}; font-family: \"Montserrat\"; text-align: left;'>{icon} <strong>{opt['key']}.</strong> {opt['text']}</div>", unsafe_allow_html=True)

            if st.session_state.last_is_correct:
                st.markdown("<div style='text-align:center; color:#22c55e; font-family:\"Roboto Slab\"; font-weight:700; font-size:1.2rem; margin:1.5rem 0;'>Excellent ! Bonne réponse.</div>", unsafe_allow_html=True)
            else:
                correct_opt = next((o for o in answer_options if o["isCorrect"]), None)
                sol = correct_opt['text'] if correct_opt else 'N/A'
                st.markdown(f"<div style='text-align:center; color:#CD493D; font-family:\"Roboto Slab\"; font-weight:700; font-size:1.2rem; margin:1.5rem 0;'>Mauvaise réponse. La solution était : {sol}</div>", unsafe_allow_html=True)

            if q.get("correction"):
                st.markdown(f"""
                <div style="background-color: #ffffff; border: 1px solid #0F3250; border-top: 4px solid #0F3250; border-radius: 8px; padding: 1.2rem; margin: 1.5rem 0;">
                    <span style="font-family: 'Roboto Slab'; font-weight: 700; color: #0F3250; display: block; margin-bottom: 0.3rem;">📚 Rappel de cours</span>
                    <p style="font-family: 'Montserrat'; color: #333333; margin: 0; font-size: 0.95rem; line-height: 1.5;">{q['correction']}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            col_q, col_p, col_a = st.columns([1, 1, 2], gap="small")
            
            with col_q:
                if st.button("⬅️ Quitter", use_container_width=True):
                    st.session_state.show_quit_confirmation = True
                    st.rerun()
                    
            with col_p:
                if st.session_state.get("auth_stage") == "logged_in":
                    if st.button("⏸️ Pause", use_container_width=True):
                        trigger_pause_save()
                        st.rerun()
                else:
                    st.button("⏸️ Pause", use_container_width=True, disabled=True, help="Connectez-vous pour sauvegarder votre progression")
                    
            with col_a:
                if st.button("➡️ Question suivante", use_container_width=True, type="primary"):
                    st.session_state.show_correction = False
                    st.session_state.answer_locked = False
                    st.session_state.selected_answer = None
                    st.session_state.current_question_index += 1
                    if st.session_state.current_question_index >= total_questions:
                        show_theme_result()
                    else:
                        st.rerun()

    # --- Confirmation de sortie commune ---
    if st.session_state.get("show_quit_confirmation"):
        st.warning("⚠️ Quitter annulera votre progression en cours.")
        c_y, c_n = st.columns(2)
        if c_y.button("Oui, je quitte", use_container_width=True):
            st.session_state.show_quit_confirmation = False
            st.session_state.exam_mode = False
            go_back_to_main_menu()
            st.rerun()
        if c_n.button("Non, je reste", use_container_width=True):
            st.session_state.show_quit_confirmation = False
            st.rerun()

    # --- BLOCK SIGNALEMENT COMMUN ---
    st.markdown("---")
    with st.expander("🚩 Signaler une erreur sur cette question"):
        reason = st.text_area("Précisez l'erreur...", key=f"report_area_{orig_idx_tech}_{theme_origin}")
        if st.button("Envoyer le rapport", key=f"rep_btn_{orig_idx_tech}_{theme_origin}"):
            if reason:
                from auth_persistence import save_question_report
                vrai_numero = orig_idx_tech + 1
                save_question_report(
                    st.session_state.username or "Anonyme", 
                    st.session_state.selected_quiz_key, 
                    theme_origin, 
                    vrai_numero, 
                    q['question'], 
                    reason
                )
                st.success(f"✅ Signalement envoyé (réf: Thème {theme_origin}, Question n°{vrai_numero}) !")
            else: 
                st.warning("Veuillez décrire l'erreur rencontrée.")

# -----------------------
# FONCTION PRINCIPALE
# -----------------------

def show_theme_result():
    """Affiche le résultat d'un thème complété avec toutes les fonctionnalités et le GIF local"""
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    total_questions = len(theme["questions"])
    score = st.session_state.score
    percentage = (score / total_questions * 100) if total_questions > 0 else 0
    
    # Couleur du thème issue de la charte CMA
    color = THEME_COLORS.get(theme_number, "#0F3250")
    
    st.markdown(
        f"<h1 style='text-align:center; color:{color}; font-family:\"Roboto Slab\"; margin-bottom:1.5rem;'>Bilan : {theme_name}</h1>",
        unsafe_allow_html=True
    )
    
    # Cercle de progression SVG stylisé (Fond beige #F8F0E3, structure grise légère, arc coloré CMA)
    st.markdown(
        f"""
        <div style="text-align:center; margin:2rem 0;">
            <div style="display:inline-block; position:relative; width:200px; height:200px;">
                <svg width="200" height="200" style="transform:rotate(-90deg)">
                    <circle cx="100" cy="100" r="85" fill="none" stroke="#e5e7eb" stroke-width="10"></circle>
                    <circle cx="100" cy="100" r="85" fill="none" stroke="{color}" stroke-width="10" 
                            stroke-dasharray="{percentage * 5.34} 534" stroke-linecap="round" style="transition: stroke-dasharray 0.6s ease-in-out;"></circle>
                </svg>
                <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center;">
                    <div style="font-family:'Roboto Slab'; font-size:2.8rem; font-weight:800; color:#0F3250;">{score}/{total_questions}</div>
                    <div style="font-family:'Montserrat'; font-size:1.1rem; color:#555555; font-weight:600;">{percentage:.0f}%</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Encarts rectangulaires massifs de résultats selon le score (Style page 59 du livret)
    if percentage >= 100:
        st.balloons()
        st.markdown(
            f"""
            <div style="background-color: #ffffff; border: 1px solid #22c55e; border-left: 6px solid #22c55e;
                        padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <h2 style="color:#155724; font-family:'Roboto Slab'; margin:0; font-size:1.6rem;">Parfait !</h2>
                <p style="color:#155724; font-family:'Montserrat'; margin:0.5rem 0 0 0; font-size:1rem;">Vous avez obtenu la note maximale de {score}/{total_questions}. Félicitations !</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif percentage >= 70:
        st.markdown(
            f"""
            <div style="background-color: #ffffff; border: 1px solid #22c55e; border-left: 6px solid #22c55e;
                        padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <h2 style="color:#155724; font-family:'Roboto Slab'; margin:0; font-size:1.6rem;">Objectif validé !</h2>
                <p style="color:#155724; font-family:'Montserrat'; margin:0.5rem 0 0 0; font-size:1rem;">Très bon score de {score}/{total_questions} ({percentage:.0f}%). Le niveau requis est atteint.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif percentage >= 50:
        st.markdown(
            f"""
            <div style="background-color: #ffffff; border: 1px solid #F1BA33; border-left: 6px solid #F1BA33;
                        padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <h2 style="color:#866939; font-family:'Roboto Slab'; margin:0; font-size:1.6rem;">Résultat encourageant</h2>
                <p style="color:#866939; font-family:'Montserrat'; margin:0.5rem 0 0 0; font-size:1rem;">Score de {score}/{total_questions} ({percentage:.0f}%). Encore un petit effort pour stabiliser vos connaissances.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background-color: #ffffff; border: 1px solid #CD493D; border-left: 6px solid #CD493D;
                        padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <h2 style="color:#721c24; font-family:'Roboto Slab'; margin:0; font-size:1.6rem;">À réviser</h2>
                <p style="color:#721c24; font-family:'Montserrat'; margin:0.5rem 0 0 0; font-size:1rem;">Score de {score}/{total_questions} ({percentage:.0f}%). Prenez le temps de revoir ce thème et essayez à nouveau.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Sauvegarde du score du thème dans la session
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
        check_and_notify_new_badges()
    
    st.markdown("<br>", unsafe_allow_html=True)
    # Boutons d'action calés sur la charte
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Menu des thèmes", use_container_width=True):
            go_back_to_main_menu()
            st.rerun()
    with col2:
        if st.button("Recommencer ce thème", use_container_width=True, type="primary"):
            start_theme(theme_number)
            st.rerun()

    # --- LE GIF DE LA VICTOIRE (Local Assets) ---
    if percentage >= 100:
        st.markdown("---")
        _, col_gif, _ = st.columns([1, 2, 1])
        with col_gif:
            gif_path = "assets/success.gif"
            import os
            if os.path.exists(gif_path):
                st.image(gif_path, use_container_width=True, caption="Félicitations !")
            else:
                st.info("Placez votre fichier 'success.gif' dans le dossier 'assets' pour l'afficher ici.")

def show_exam_result():
    """Affiche la page de bilan de l'Examen Blanc avec rétroaction et sauvegarde des statistiques."""
    st.markdown("<h2 style='text-align:center; font-family:\"Roboto Slab\"; color:#0F3250;'>Bilan de l'Examen Blanc</h2>", unsafe_allow_html=True)
    
    score = st.session_state.score
    total = len(st.session_state.exam_questions)
    percentage = (score / total) * 100 if total > 0 else 0
    
    # Récupération du commentaire sobre sans émoticône
    comment = get_current_exam_comment(score)
    
    # --- SAUVEGARDE ET PERSISTANCE DES STASTISTIQUES D'EXAMEN ---
    quiz_key = st.session_state.selected_quiz_key
    if st.session_state.get("auth_stage") == "logged_in" and st.session_state.get("username") and quiz_key:
        save_user_scores(
            username=st.session_state.username,
            quiz_key=quiz_key,
            theme_scores={},  # On ne touche pas aux thèmes classiques ici
            exam_attempt=True,
            exam_score=score
        )
        check_and_notify_new_badges()
    
    # --- VISUALISATION DU SCORE (Arc de cercle SVG) ---
    angle = (percentage / 100) * 180
    r, g, b = 205, 73, 61  # Rouge par défaut (#CD493D)
    if percentage >= 70:
        r, g, b = 34, 197, 94  # Vert en cas de validation (#22c55e)
        
    svg_gauge = f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 2rem 0;">
        <svg width="240" height="130" viewBox="0 0 200 110">
            <path d="M20,100 A80,80 0 0,1 180,100" fill="none" stroke="#e5e7eb" stroke-width="16" stroke-linecap="round"/>
            <path d="M20,100 A80,80 0 0,1 180,100" fill="none" stroke="rgb({r},{g},{b})" stroke-width="16" stroke-linecap="round"
                  stroke-dasharray="251.2" stroke-dashoffset="{251.2 - (251.2 * (angle / 180))}"/>
            <text x="100" y="95" text-anchor="middle" font-family="Roboto Slab" font-size="26" font-weight="700" fill="#0F3250">{score} / {total}</text>
            <text x="100" y="115" text-anchor="middle" font-family="Montserrat" font-size="10" font-weight="600" fill="#555555">{percentage:.1f}% de réussite</text>
        </svg>
        <div style="max-width: 550px; text-align: center; margin-top: 1rem; padding: 0 1rem;">
            <p style="font-family: 'Montserrat'; font-size: 1.05rem; font-weight: 600; color: #0F3250; line-height: 1.5; margin: 0;">{comment}</p>
        </div>
    </div>
    """
    st.markdown(svg_gauge, unsafe_allow_html=True)
    
    # --- EASTER EGG : SANS-FAUTE PARFAIT (30/30) ---
    if score == 30:
        st.balloons()
        import os
        gif_path = os.path.join("assets", "popopo.gif")
        if os.path.exists(gif_path):
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                st.image(gif_path, use_container_width=True)
                
    st.markdown("---")
    
    # --- ANALYSE DÉTAILLÉE DES RÉPONSES ---
    st.markdown("<h3 style='font-family:\"Roboto Slab\"; color:#0F3250; margin-bottom:1rem;'>Récapitulatif des questions</h3>", unsafe_allow_html=True)
    
    for idx, q in enumerate(st.session_state.exam_questions):
        user_ans = st.session_state.exam_user_answers.get(idx, "Aucune réponse")
        correct_opt = next((o for o in q["answerOptions"] if o["isCorrect"]), None)
        correct_txt = correct_opt["text"] if correct_opt else ""
        is_correct = (user_ans == correct_txt)
        
        status_color = "#22c55e" if is_correct else "#CD493D"
        status_bg = "#ffffff"
        border_style = f"border: 1px solid {status_color}; border-left: 6px solid {status_color};"
        
        box_html = f"""
        <div style="{border_style} border-radius: 8px; padding: 1.2rem; margin-bottom: 1rem; background-color: {status_bg}; font-family: 'Montserrat';">
            <span style="font-size: 0.85rem; font-weight: 700; color: {status_color}; text-transform: uppercase;">Question {idx + 1} — {'Correct' if is_correct else 'Erreur'}</span>
            <p style="font-size: 1.05rem; font-weight: 700; color: #0F3250; margin: 0.4rem 0 0.8rem 0; line-height: 1.4;">{q['question']}</p>
            <p style="margin: 0.2rem 0; font-size: 0.95rem; color: #333333;"><strong>Votre réponse :</strong> {user_ans}</p>
        </div>
        """
        st.markdown(box_html, unsafe_allow_html=True)
        
        if not is_correct:
            st.markdown(f"""
            <div style="background-color: #ffffff; border: 1px solid #0F3250; border-top: 4px solid #0F3250; border-radius: 8px; padding: 1.2rem; margin: -0.5rem 0 1.5rem 0;">
                <span style="font-family: 'Roboto Slab'; font-weight: 700; color: #0F3250; display: block; margin-bottom: 0.3rem;">💡 Solution & Rappel de cours</span>
                <p style="font-family: 'Montserrat'; color: #CD493D; margin: 0 0 0.5rem 0; font-size: 0.95rem;"><strong>La bonne réponse était :</strong> {correct_txt}</p>
                <p style="font-family: 'Montserrat'; color: #333333; margin: 0; font-size: 0.95rem; line-height: 1.5;">{q.get('correction', 'Pas de rappel de cours disponible pour cette question.')}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Retourner au menu principal", use_container_width=True, type="primary"):
        st.session_state.exam_mode = False
        go_back_to_main_menu()
        st.rerun()

def main():
    # Injection systématique du thème graphique CMA
    inject_cma_theme()

    # --- 1. SIDEBAR (Navigation d'origine nettoyée) ---
    with st.sidebar:
        if st.session_state.get("auth_stage") == "logged_in":
            if st.button("👤 Mon profil", use_container_width=True):
                st.session_state.ui_mode = UIMode.PROFILE
                st.rerun()
            if st.button("🏠 Quiz", use_container_width=True):
                st.session_state.ui_mode = UIMode.APP
                st.rerun()
            
            # --- SECTION ADMIN ---
            curr_user = st.session_state.get("username", "")
            if curr_user in ADMIN_USERS:
                st.markdown("---")
                from auth_persistence import get_all_reports
                nb_reports = len(get_all_reports())
                label = f"🚩 Signalements ({nb_reports})" if nb_reports > 0 else "Voir les signalements"
                if st.button(label, use_container_width=True):
                    st.session_state.ui_mode = UIMode.ADMIN
                    st.rerun()

            st.markdown("---")
            st.caption(f"Connecté : {curr_user}")
        else:
            # Réinitialisation complète de l'état d'accueil pour l'invite de connexion
            if st.button("🔐 Connexion / Inscription", use_container_width=True):
                st.session_state.auth_stage = "entry"
                st.session_state.ui_mode = UIMode.APP
                st.session_state.selected_quiz_key = None
                st.session_state.current_theme = None
                st.rerun()

        # --- SIGNATURE INSTITUTIONNELLE : LOGO CFA FOIX ---
        import os
        logo_path = "assets/logo_cfa_cmar_foix.png"
        if os.path.exists(logo_path):
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.image(logo_path, use_container_width=True)

    # --- 2. AIGUILLAGE DES ÉCRANS ---
    # AJOUT DE LA SÉCURITÉ : Si l'état d'authentification demande l'écran de saisie, on l'affiche en priorité absolue
    if st.session_state.get("auth_stage") == "entry":
        show_entry_screen()
        return

    current_mode = st.session_state.ui_mode
    mode_val = current_mode.value if hasattr(current_mode, 'value') else current_mode

    if mode_val == "admin":
        show_admin_reports_page()
    elif mode_val == "profile":
        show_profile_page()
    elif st.session_state.selected_quiz_key is None:
        show_quiz_selector()
    elif st.session_state.current_theme is None and not st.session_state.get("exam_mode", False):
        show_quiz_page()
    else:
        # Routage spécifique au mode examen ou entraînement classique
        if st.session_state.get("exam_mode", False):
            questions = st.session_state.exam_questions
            curr_idx = st.session_state.current_question_index
            
            if curr_idx >= len(questions):
                show_exam_result()
            else:
                show_question_screen()
        else:
            q_data = get_current_quiz_data()
            theme_idx = st.session_state.current_theme
            theme_questions = q_data["themes"][theme_idx]["questions"]
            curr_idx = st.session_state.current_question_index
            
            if curr_idx >= len(theme_questions):
                show_theme_result()
            else:
                show_question_screen()


# Point d'entrée de l'application
if __name__ == "__main__":
    main()