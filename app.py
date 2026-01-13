import streamlit as st
import random
from datetime import datetime
from auth_persistence import (
    create_user,
    login_user,
    get_user_info,
    get_user_stats,
    save_user_scores,
    load_user_scores,
)

st.set_page_config(page_title="Quiz CFA", page_icon="🎓", layout="centered")
if "auth_stage" not in st.session_state:
    # "entry" = écran d’entrée (sans compte / créer un compte / se connecter)
    # "logged_in" = utilisateur connecté
    st.session_state.auth_stage = "entry"

if "username" not in st.session_state:
    st.session_state.username = None

def show_entry_screen():
    st.markdown("""
    <div style="
        padding: 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #6A11CB, #2575FC);
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
        max-width: 700px;
        margin: 2rem auto;
    ">
        <h1 style="margin-bottom: 0.5rem;">Plateforme de révision CFA CMAR</h1>
        <p style="font-size: 1.1rem; opacity: 0.9;">
            Révisez par niveau, métier et matières générales, et suivez votre progression.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Accès rapide")
        st.markdown(
            "Utilisez l'application immédiatement **sans compte**.\n\n"
            "Les scores seront gardés uniquement pour cette session."
        )
        if st.button("🚀 Entrer sans compte", use_container_width=True):
            st.session_state.auth_stage = "guest"
            st.session_state.username = None
            st.rerun()

    with col2:
        st.subheader("Créer ou utiliser un compte")
        tabs = st.tabs(["Se connecter", "Créer un compte"])

        # Onglet connexion
        with tabs[0]:
            login_username = st.text_input("Nom d'utilisateur", key="login_username")
            login_password = st.text_input("Mot de passe", type="password", key="login_password")
            if st.button("🔐 Se connecter", use_container_width=True, key="login_btn"):
                success, msg = login_user(login_username, login_password)
                if success:
                    st.success(msg)
                    st.session_state.auth_stage = "logged_in"
                    st.session_state.username = login_username.strip().lower()
                    st.rerun()
                else:
                    st.error(msg)

        # Onglet création
        with tabs[1]:
            new_username = st.text_input("Nom d'utilisateur", key="new_username")
            new_email = st.text_input("Email", key="new_email")
            new_password = st.text_input("Mot de passe", type="password", key="new_password")
            if st.button("🆕 Créer mon compte", use_container_width=True, key="create_btn"):
                success, msg = create_user(new_username, new_email, new_password)
                if success:
                    st.success(msg + " Vous pouvez maintenant vous connecter.")
                else:
                    st.error(msg)


# -----------------------
# IMPORT DES QUIZ DISPONIBLES
# -----------------------

# BP
from quizzes.quiz_bp_metiers.quiz_bp_arts_de_la_cuisine_100 import quiz_data as quiz_bp_arts_cuisine_data
from quizzes.quiz_bp_metiers.quiz_bp_boucher_100 import quiz_data as quiz_bp_boucher_data
from quizzes.quiz_bp_metiers.quiz_bp_coiffure_100 import quiz_data as quiz_bp_coiffure_data
from quizzes.quiz_bp_metiers.quiz_bp_macon_100 import quiz_data as quiz_bp_macon_data
from quizzes.quiz_bp_metiers.quiz_bp_migcs_100 import quiz_data as quiz_bp_migcs_data

# BTS
from quizzes.quiz_bts_metiers.quiz_bts_meca_vp_100 import quiz_data as quiz_bts_meca_vp_data

# BAC PRO
from quizzes.quiz_bacpro_metiers.quiz_bacpro_mva_100 import quiz_data as quiz_bacpro_mva_data
from quizzes.quiz_bacpro_metiers.quiz_bacpro_mcva_100 import quiz_data as quiz_bacpro_mcva_data
from quizzes.quiz_bacpro_metiers.quiz_bacpro_mcvb_100 import quiz_data as quiz_bacpro_mcvb_data

# CAP métiers
from quizzes.quiz_cap_metiers.quiz_cap_boucher_100 import quiz_data as quiz_cap_boucher_data
from quizzes.quiz_cap_metiers.quiz_cap_boulanger_100 import quiz_data as quiz_cap_boulanger_data
from quizzes.quiz_cap_metiers.quiz_cap_carreleur_mosaiste_100 import quiz_data as quiz_cap_carreleur_data
from quizzes.quiz_cap_metiers.quiz_cap_carrosserie_automobile_100 import quiz_data as quiz_cap_carrosserie_data
from quizzes.quiz_cap_metiers.quiz_cap_charcutier_traiteur_100 import quiz_data as quiz_cap_charcutier_traiteur_data
from quizzes.quiz_cap_metiers.quiz_cap_chcr_100 import quiz_data as quiz_cap_chcr_data
from quizzes.quiz_cap_metiers.quiz_cap_coiffure_100 import quiz_data as quiz_cap_coiffure_data
from quizzes.quiz_cap_metiers.quiz_cap_couvreur_100 import quiz_data as quiz_cap_couvreur_data
from quizzes.quiz_cap_metiers.quiz_cap_cuisine_100 import quiz_data as quiz_cap_cuisine_data
from quizzes.quiz_cap_metiers.quiz_cap_electricien_100 import quiz_data as quiz_cap_electricien_data
from quizzes.quiz_cap_metiers.quiz_cap_employe_polyvalent_commerce_100 import quiz_data as quiz_cap_epc_data
from quizzes.quiz_cap_metiers.quiz_cap_macon_100 import quiz_data as quiz_cap_macon_data
from quizzes.quiz_cap_metiers.quiz_cap_meca_vp_100 import quiz_data as quiz_cap_meca_vp_data
from quizzes.quiz_cap_metiers.quiz_cap_menuisier_fabricant_100 import quiz_data as quiz_cap_menuisier_fabricant_data
from quizzes.quiz_cap_metiers.quiz_cap_menuisier_installateur_100 import quiz_data as quiz_cap_menuisier_installateur_data
from quizzes.quiz_cap_metiers.quiz_cap_patissier_100 import quiz_data as quiz_cap_patissier_data
from quizzes.quiz_cap_metiers.quiz_cap_peintre_100 import quiz_data as quiz_cap_peintre_data
from quizzes.quiz_cap_metiers.quiz_cap_peinture_carrosserie_100 import quiz_data as quiz_cap_peinture_carrosserie_data
from quizzes.quiz_cap_metiers.quiz_cap_platre_isolation_100 import quiz_data as quiz_cap_platre_isolation_data
from quizzes.quiz_cap_metiers.quiz_cap_sanitaire_100 import quiz_data as quiz_cap_sanitaire_data
from quizzes.quiz_cap_metiers.quiz_cap_serrurier_metallier_100 import quiz_data as quiz_cap_serrurier_metallier_data
from quizzes.quiz_cap_metiers.quiz_cap_thermique_100 import quiz_data as quiz_cap_thermique_data

# CAP matières générales
from quizzes.quiz_cap_generaux.quiz_cap_anglais_1 import quiz_data as quiz_cap_anglais_1_data
from quizzes.quiz_cap_generaux.quiz_cap_anglais_2 import quiz_data as quiz_cap_anglais_2_data
from quizzes.quiz_cap_generaux.quiz_cap_espagnol_1 import quiz_data as quiz_cap_espagnol_1_data
from quizzes.quiz_cap_generaux.quiz_cap_espagnol_2 import quiz_data as quiz_cap_espagnol_2_data
from quizzes.quiz_cap_generaux.quiz_cap_francais_1 import quiz_data as quiz_cap_francais_1_data
from quizzes.quiz_cap_generaux.quiz_cap_francais_2 import quiz_data as quiz_cap_francais_2_data
from quizzes.quiz_cap_generaux.quiz_cap_histoire_geographie_1 import quiz_data as quiz_cap_histoire_geographie_1_data
from quizzes.quiz_cap_generaux.quiz_cap_histoire_geographie_2 import quiz_data as quiz_cap_histoire_geographie_2_data
from quizzes.quiz_cap_generaux.quiz_cap_mathematique_1 import quiz_data as quiz_cap_mathematique_1_data
from quizzes.quiz_cap_generaux.quiz_cap_mathematique_2 import quiz_data as quiz_cap_mathematique_2_data
from quizzes.quiz_cap_generaux.quiz_cap_pse_1 import quiz_data as quiz_cap_pse_1_data
from quizzes.quiz_cap_generaux.quiz_cap_pse_2 import quiz_data as quiz_cap_pse_2_data
from quizzes.quiz_cap_generaux.quiz_cap_science_physique_1 import quiz_data as quiz_cap_science_physique_1_data
from quizzes.quiz_cap_generaux.quiz_cap_science_physique_2 import quiz_data as quiz_cap_science_physique_2_data

# CS
from quizzes.quiz_cs_metiers.quiz_cs_coiffure_coupe_couleur_100 import quiz_data as quiz_cs_coiffure_coupe_couleur_data

# -----------------------
# QUIZZES
# -----------------------

QUIZZES = {
    # ----- BAC PRO -----
    "bacpro_mcvb_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option B (prospection et valorisation de l'offre commerciale)",
        "description": "Révisions complètes Bac Pro MCV option B.",
        "data": quiz_bacpro_mcvb_data,
        "icon": "🛍️",
        "color": "#1abc9c",
    },
    "bacpro_mcva_100": {
        "title": "Bac Pro Métiers du commerce et de la vente option A (animation et gestion de l'espace commercial)",
        "description": "Révisions complètes Bac Pro MCV option A.",
        "data": quiz_bacpro_mcva_data,
        "icon": "🏬",
        "color": "#27ae60",
    },
    "bacpro_mva_100": {
        "title": "Bac Pro Maintenance des véhicules option A (voitures particulières)",
        "description": "Révisions complètes Bac Pro Maintenance des véhicules option A (VP).",
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
        "title": "BP Métiers de l'industrie graphique (communication et services)",
        "description": "Révisions complètes BP MIGCS.",
        "data": quiz_bp_migcs_data,
        "icon": "🖨️",
        "color": "#34495e",
    },

    # ----- BTS -----
    "bts_meca_vp_100": {
        "title": "BTS Maintenance des véhicules, option A (voitures particulières)",
        "description": "Révisions complètes BTS Maintenance des véhicules option A (VP).",
        "data": quiz_bts_meca_vp_data,
        "icon": "🔧",
        "color": "#2980b9",
    },

    # ----- CAP métiers -----
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
        "icon": "🔲",
        "color": "#2ecc71",
    },
    "cap_carrosserie_automobile_100": {
        "title": "CAP Réparation des carrosseries",
        "description": "Révisions complètes CAP Réparation des carrosseries.",
        "data": quiz_cap_carrosserie_data,
        "icon": "🚙",
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
        "icon": "☕",
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
        "title": "CAP Maintenance des véhicules, option A (voitures particulières)",
        "description": "Révisions complètes CAP Maintenance des véhicules option voitures particulières.",
        "data": quiz_cap_meca_vp_data,
        "icon": "🔧",
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
        "icon": "🔨",
        "color": "#a0522d",
    },
    "cap_patissier_100": {
        "title": "CAP Pâtissier",
        "description": "Révisions complètes CAP Pâtissier.",
        "data": quiz_cap_patissier_data,
        "icon": "🧁",
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
        "title": "CAP Métiers du plâtre et de l'isolation",
        "description": "Révisions complètes CAP Métiers du plâtre et de l'isolation.",
        "data": quiz_cap_platre_isolation_data,
        "icon": "🧱",
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
        "icon": "🔐",
        "color": "#7f8c8d",
    },
    "cap_thermique_100": {
        "title": "CAP Monteur en installations thermiques",
        "description": "Révisions complètes CAP Monteur en installations thermiques.",
        "data": quiz_cap_thermique_data,
        "icon": "🔥",
        "color": "#e74c3c",
    },

    # ----- CAP Matières générales -----
    "cap_anglais_1": {
        "title": "CAP Matières générales – Anglais (quiz 1)",
        "description": "Révisions d'anglais – série 1.",
        "data": quiz_cap_anglais_1_data,
        "icon": "🇬🇧",
        "color": "#3b82f6",
    },
    "cap_anglais_2": {
        "title": "CAP Matières générales – Anglais (quiz 2)",
        "description": "Révisions d'anglais – série 2.",
        "data": quiz_cap_anglais_2_data,
        "icon": "🇬🇧",
        "color": "#2563eb",
    },
    "cap_espagnol_1": {
        "title": "CAP Matières générales – Espagnol (quiz 1)",
        "description": "Révisions d'espagnol – série 1.",
        "data": quiz_cap_espagnol_1_data,
        "icon": "🇪🇸",
        "color": "#f97316",
    },
    "cap_espagnol_2": {
        "title": "CAP Matières générales – Espagnol (quiz 2)",
        "description": "Révisions d'espagnol – série 2.",
        "data": quiz_cap_espagnol_2_data,
        "icon": "🇪🇸",
        "color": "#ea580c",
    },
    "cap_francais_1": {
        "title": "CAP Matières générales – Français (quiz 1)",
        "description": "Révisions de français – série 1.",
        "data": quiz_cap_francais_1_data,
        "icon": "📘",
        "color": "#10b981",
    },
    "cap_francais_2": {
        "title": "CAP Matières générales – Français (quiz 2)",
        "description": "Révisions de français – série 2.",
        "data": quiz_cap_francais_2_data,
        "icon": "📗",
        "color": "#059669",
    },
    "cap_histoire_geographie_1": {
        "title": "CAP Matières générales – Histoire-Géographie (quiz 1)",
        "description": "Révisions d'histoire-géographie – série 1.",
        "data": quiz_cap_histoire_geographie_1_data,
        "icon": "🌍",
        "color": "#facc15",
    },
    "cap_histoire_geographie_2": {
        "title": "CAP Matières générales – Histoire-Géographie (quiz 2)",
        "description": "Révisions d'histoire-géographie – série 2.",
        "data": quiz_cap_histoire_geographie_2_data,
        "icon": "🗺️",
        "color": "#eab308",
    },
    "cap_mathematique_1": {
        "title": "CAP Matières générales – Mathématiques (quiz 1)",
        "description": "Révisions de mathématiques – série 1.",
        "data": quiz_cap_mathematique_1_data,
        "icon": "➗",
        "color": "#6366f1",
    },
    "cap_mathematique_2": {
        "title": "CAP Matières générales – Mathématiques (quiz 2)",
        "description": "Révisions de mathématiques – série 2.",
        "data": quiz_cap_mathematique_2_data,
        "icon": "✖️",
        "color": "#4f46e5",
    },
    "cap_pse_1": {
        "title": "CAP Matières générales – PSE (quiz 1)",
        "description": "Révisions de Prévention Santé Environnement – série 1.",
        "data": quiz_cap_pse_1_data,
        "icon": "🩺",
        "color": "#22c55e",
    },
    "cap_pse_2": {
        "title": "CAP Matières générales – PSE (quiz 2)",
        "description": "Révisions de Prévention Santé Environnement – série 2.",
        "data": quiz_cap_pse_2_data,
        "icon": "🏥",
        "color": "#16a34a",
    },
    "cap_science_physique_1": {
        "title": "CAP Matières générales – Sciences physiques (quiz 1)",
        "description": "Révisions de sciences physiques – série 1.",
        "data": quiz_cap_science_physique_1_data,
        "icon": "🔬",
        "color": "#0ea5e9",
    },
    "cap_science_physique_2": {
        "title": "CAP Matières générales – Sciences physiques (quiz 2)",
        "description": "Révisions de sciences physiques – série 2.",
        "data": quiz_cap_science_physique_2_data,
        "icon": "⚗️",
        "color": "#0284c7",
    },

    # ----- CS -----
    "cs_coiffure_coupe_couleur_100": {
        "title": "Certificat de spécialisation coiffure coupe couleur",
        "description": "Révisions complètes CS Coiffure coupe couleur.",
        "data": quiz_cs_coiffure_coupe_couleur_data,
        "icon": "💇",
        "color": "#e84393",
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
if "ui_mode" not in st.session_state:
    # "app" = interface quiz, "profile" = page profil
    st.session_state.ui_mode = "app"
def show_entry_screen():
    st.markdown("""
    <div style="
        padding: 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #6A11CB, #2575FC);
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
        max-width: 700px;
        margin: 2rem auto;
    ">
        <h1 style="margin-bottom: 0.5rem;">Plateforme de révision CFA CMAR</h1>
        <p style="font-size: 1.1rem; opacity: 0.9;">
            Révisez par niveau, métier et matières générales, et suivez votre progression.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Bouton "Entrer sans compte"
    with col1:
        st.subheader("Accès rapide")
        st.markdown(
            "Utilisez l'application immédiatement **sans compte**.\n\n"
            "Les scores seront gardés uniquement pour cette session."
        )
        if st.button("🚀 Entrer sans compte", use_container_width=True):
            st.session_state.auth_stage = "guest"
            st.session_state.username = None
            st.rerun()

    # Onglets Se connecter / Créer un compte
    with col2:
        st.subheader("Créer ou utiliser un compte")
        tabs = st.tabs(["Se connecter", "Créer un compte"])

        # Onglet connexion
        with tabs[0]:
            login_username = st.text_input("Nom d'utilisateur", key="login_username")
            login_password = st.text_input("Mot de passe", type="password", key="login_password")
            if st.button("🔐 Se connecter", use_container_width=True, key="login_btn"):
                success, msg = login_user(login_username, login_password)
                if success:
                    st.success(msg)
                    st.session_state.auth_stage = "logged_in"
                    st.session_state.username = login_username.strip().lower()
                    st.rerun()
                else:
                    st.error(msg)

        # Onglet création
        with tabs[1]:
            new_username = st.text_input("Nom d'utilisateur", key="new_username")
            new_email = st.text_input("Email", key="new_email")
            new_password = st.text_input("Mot de passe", type="password", key="new_password")
            if st.button("🆕 Créer mon compte", use_container_width=True, key="create_btn"):
                success, msg = create_user(new_username, new_email, new_password)
                if success:
                    st.success(msg + " Vous pouvez maintenant vous connecter.")
                else:
                    st.error(msg)

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
    st.session_state.shuffled_answers = {}

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
            try:
                if not score_str:
                    continue
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

            # Répartition par niveau grâce au préfixe
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

    # --- Badges ---

    st.markdown("### Badges")

    badges = []

    # Progression globale
    if validated_quiz_count >= 1:
        badges.append("🎯 Premier quiz validé")
    if validated_quiz_count >= 5:
        badges.append("🏅 5 quiz validés")
    if stats.get("total_questions", 0) >= 100:
        badges.append("📚 100 questions jouées")
    if stats.get("total_questions", 0) >= 300:
        badges.append("🧠 300 questions jouées")
    if stats.get("average_percentage", 0) >= 80:
        badges.append("🔥 Moyenne ≥ 80 %")
    if stats.get("average_percentage", 0) >= 90:
        badges.append("💎 Moyenne ≥ 90 %")

    # Badges par niveau
    if validated_cap >= 3:
        badges.append("🏗️ Spécialiste CAP (3 quiz CAP validés)")
    if validated_bacpro >= 2:
        badges.append("🏬 Spécialiste BAC PRO (2 quiz BAC PRO validés)")
    if validated_bp >= 1 and validated_bts >= 1 and validated_cs >= 1:
        badges.append("🎓 Spécialiste supérieur (BP + BTS + CS validés)")

    # Assiduité
    total_quiz_played = stats.get("total_quizzes", 0)
    if total_quiz_played >= 10:
        badges.append("⏱️ Fidèle au poste (10 quiz joués)")

    if badges:
        st.markdown(
            "<div style='display:flex;flex-wrap:wrap;gap:0.5rem;margin-bottom:1rem;'>"
            + "".join(
                f"<span style='background:#eef2ff;border-radius:999px;"
                f"padding:0.4rem 0.8rem;border:1px solid #c7d2fe;"
                f"font-size:0.9rem;'>{b}</span>"
                for b in badges
            )
            + "</div>",
            unsafe_allow_html=True,
        )
    else:
        st.caption("Aucun badge débloqué pour le moment. Continue à jouer !")

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
    st.subheader("BAC PRO – Choisissez un quiz")

    if st.button("⬅️ Retour aux niveaux"):
        st.session_state.selected_level = None
        st.session_state.selected_quiz_key = None
        st.session_state.current_theme = None
        st.rerun()

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
        f"<h2 style='margin-bottom:0.2rem;'>{theme_name}</h2>"
        f"<div style='height:4px;border-radius:999px;background:{color};margin-bottom:0.8rem;'></div>",
        unsafe_allow_html=True,
    )

    progress_percent = ((idx + 1) / total_questions) * 100
    st.markdown(
        f"""
        <div style="
            width:100%;
            background:#e5e7eb;
            border-radius:12px;
            height:24px;
            position:relative;
            margin-bottom:0.5rem;
            overflow:hidden;
        ">
            <div style="
                width:{progress_percent}%;
                background:linear-gradient(90deg, {color} 0%, {color}dd 100%);
                height:100%;
                border-radius:12px;
                transition:width 0.4s ease;
            "></div>
            <span style="
                position:absolute;
                top:50%;
                left:50%;
                transform:translate(-50%, -50%);
                font-weight:600;
                font-size:0.85rem;
                color:#1f2937;
            ">Question {idx + 1} / {total_questions}</span>
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

    st.markdown(f"<h3 style='margin:1rem 0;'>{q['question']}</h3>", unsafe_allow_html=True)

    if not st.session_state.answer_locked:
        st.markdown("<p style='font-weight:600;margin-bottom:0.5rem;'>Choisissez une réponse :</p>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <style>
            div[data-testid="stButton"] > button {{
                width: 100%;
                text-align: left;
                padding: 1rem;
                border-radius: 12px;
                border: 2px solid #d1d5db;
                background: #ffffff;
                color: #1f2937;
                font-size: 1rem;
                transition: all 0.2s ease;
                margin-bottom: 0.8rem;
                min-height: 60px;
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

        st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

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
                go_back_to_main_menu()
                st.rerun()

    else:
        st.markdown(f"<p style='font-weight:600;margin:1rem 0;'>Votre réponse : <strong>{st.session_state.selected_answer}</strong></p>", unsafe_allow_html=True)

        for opt in answer_options:
            opt_text = opt["text"]
            opt_key = opt["key"]
            is_correct_answer = opt["isCorrect"]
            is_user_answer = (st.session_state.selected_answer == opt_text)

            if is_correct_answer:
                border_color = "#22c55e"
                bg_color = "#d4edda"
                icon = "✅"
            elif is_user_answer and not is_correct_answer:
                border_color = "#dc3545"
                bg_color = "#f8d7da"
                icon = "❌"
            else:
                border_color = "#d1d5db"
                bg_color = "#f9fafb"
                icon = ""

            st.markdown(
                f"""
                <div style="
                    border:2px solid {border_color};
                    border-radius:12px;
                    padding:1rem;
                    margin-bottom:0.8rem;
                    background:{bg_color};
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
                        padding:1.2rem;
                        border-radius:12px;
                        margin:1.5rem 0;
                        animation:fadeIn 0.3s ease-in;
                    '>
                        <h3 style='color:#155724;margin:0;font-size:1.3rem;'>✅ Bonne réponse !</h3>
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
                        padding:1.2rem;
                        border-radius:12px;
                        margin:1.5rem 0;
                        animation:fadeIn 0.3s ease-in;
                    '>
                        <h3 style='color:#721c24;margin:0 0 0.5rem 0;font-size:1.3rem;'>❌ Mauvaise réponse</h3>
                        <p style='margin:0;color:#721c24;'><strong>La bonne réponse était :</strong> {correct_option['text'] if correct_option else 'N/A'}</p>
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
                        padding:1.5rem;
                        border-radius:12px;
                        margin:1.5rem 0;
                        box-shadow:0 4px 12px rgba(0,0,0,0.1);
                        animation:fadeIn 0.4s ease-in;
                    '>
                        <h4 style='color:#006064;margin:0 0 0.8rem 0;font-size:1.2rem;display:flex;align-items:center;'>
                            <span style='font-size:1.5rem;margin-right:0.5rem;'>📚</span> Cours
                        </h4>
                        <div style='color:#00363a;line-height:1.6;'>{q['correction']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅️ Retour", use_container_width=True):
                go_back_to_main_menu()
                st.rerun()

        with col2:
            if st.button("➡️ Question suivante", use_container_width=True, type="primary"):
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
# INTERFACE : ÉCRAN DE RÉSULTAT
# -----------------------

def show_theme_result():
    quiz_data = get_current_quiz_data()
    quiz_key = st.session_state.selected_quiz_key
    theme_number = st.session_state.current_theme
    theme = quiz_data["themes"][theme_number]
    theme_name = theme["name"]
    total_questions = len(theme["questions"])
    score = st.session_state.score
    percentage = (score / total_questions) * 100

    color = THEME_COLORS.get(theme_number, "#4f46e5")

    st.markdown(
        f"<h1 style='text-align:center;color:{color};margin-bottom:1.5rem;'>📊 Résultat : {theme_name}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align:center;margin:2rem 0;">
            <div style="display:inline-block;position:relative;width:200px;height:200px;">
                <svg width="200" height="200" style="transform:rotate(-90deg);">
                    ircle cx="100" cy="100" r="85" fill="none" stroke="#e5e7eb" stroke-width="12"/>
                    ircle cx="100" cy="100" r="85" fill="none" stroke="{color}" stroke-width="12" stroke-dasharray="{percentage * 5.34} 534" stroke-linecap="round"/>
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

    if percentage == 100:
        st.balloons()
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);border-left:6px solid #28a745;padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#155724;margin:0;font-size:2rem;">🎉 Parfait !</h2>
                <p style="color:#155724;margin:0.5rem 0 0 0;font-size:1.1rem;">Score parfait : {score}/{total_questions} ({percentage:.0f}%)</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif percentage >= 75:
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);border-left:6px solid #28a745;padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#155724;margin:0;font-size:2rem;">✨ Très bien !</h2>
                <p style="color:#155724;margin:0.5rem 0 0 0;font-size:1.1rem;">Score : {score}/{total_questions} ({percentage:.0f}%)</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif percentage >= 50:
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);border-left:6px solid #17a2b8;padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#0c5460;margin:0;font-size:2rem;">👍 Pas mal !</h2>
                <p style="color:#0c5460;margin:0.5rem 0 0 0;font-size:1.1rem;">Score : {score}/{total_questions} ({percentage:.0f}%)</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background:linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);border-left:6px solid #dc3545;padding:1.5rem;border-radius:16px;margin:1.5rem 0;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                <h2 style="color:#721c24;margin:0;font-size:2rem;">💪 Continue tes efforts !</h2>
                <p style="color:#721c24;margin:0.5rem 0 0 0;font-size:1.1rem;">Score : {score}/{total_questions} ({percentage:.0f}%) - Révise encore ce thème !</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<h3 style='text-align:center;margin:2rem 0 1rem 0;color:#374151;'>Détail de tes réponses</h3>", unsafe_allow_html=True)
    
    results = st.session_state.get("question_results", [])
    
    if len(results) == total_questions:
        result_icons = "".join([
            f"<span style='font-size:1.8rem;margin:0.3rem;display:inline-block;'>{'✅' if r else '❌'}</span>"
            for r in results
        ])
        
        st.markdown(
            f"""
            <div style="text-align:center;background:#f9fafb;padding:1.5rem;border-radius:12px;border:2px solid #e5e7eb;line-height:2.5rem;max-width:600px;margin:0 auto;">
                {result_icons}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Le détail des réponses n'est pas disponible pour cette session.")

    if quiz_key not in st.session_state.theme_scores:
        st.session_state.theme_scores[quiz_key] = {}
    st.session_state.theme_scores[quiz_key][theme_number] = f"{score}/{total_questions}"

    # Sauvegarde persistante pour les utilisateurs connectés
    if (
        st.session_state.get("auth_stage") == "logged_in"
        and st.session_state.get("username")
    ):
        # thème_scores = scores de tous les thèmes de ce quiz dans la session
        theme_scores = st.session_state.theme_scores[quiz_key]
        # quiz_key est déjà une bonne clé (cap_boucher_100, bts_meca_vp_100, etc.)
        save_user_scores(
            st.session_state.username,
            quiz_key,
            theme_scores
        )

    st.markdown("<div style='margin-top:2rem;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Revenir au menu des thèmes", use_container_width=True):
            go_back_to_main_menu()
            st.rerun()

    with col2:
        if st.button("🔄 Refaire ce thème", use_container_width=True, type="primary"):
            start_theme(theme_number)
            st.rerun()

    st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)
    summary_text = generate_score_summary()
    st.download_button(
        label="📥 Télécharger le récapitulatif complet",
        data=summary_text,
        file_name=f"recap_quiz_{quiz_key}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain",
        use_container_width=True
    )
# -----------------------
# FONCTION PRINCIPALE
# -----------------------

def main():
    # Sidebar : navigation profil / quiz
    with st.sidebar:
        st.markdown("### Navigation")
        if st.session_state.get("auth_stage") == "logged_in":
            if st.button("👤 Mon profil", use_container_width=True):
                st.session_state.ui_mode = "profile"
            if st.button("🏠 Quiz", use_container_width=True):
                st.session_state.ui_mode = "app"
            st.markdown("---")
            st.caption(f"Connecté en tant que {st.session_state.username}")
        else:
            st.info("Connectez-vous pour accéder au profil.")

    # Si on est en mode profil, on n’affiche pas l’interface de quiz
    if st.session_state.ui_mode == "profile":
        show_profile_page()
        return

    # --- LOGIQUE EXISTANTE DU QUIZ ---
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
        # Utilisateur déjà dans l’application (avec ou sans compte)
        main()
    else:
        # Premier écran : choix "entrer sans compte" ou "créer/se connecter"
        show_entry_screen()

