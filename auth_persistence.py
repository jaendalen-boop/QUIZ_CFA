import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import hashlib
from datetime import datetime
import json

# --- CONNEXION ---
conn = st.connection("gsheets", type=GSheetsConnection)

def hash_password(password: str) -> str:
    """Hache le mot de passe en SHA256 pour la sécurité."""
    return hashlib.sha256(password.encode()).hexdigest()

def force_refresh_cache():
    """Vide la mémoire vive pour forcer Streamlit à relire Google Sheets."""
    st.cache_data.clear()

# ===================== GESTION UTILISATEURS =====================

@st.cache_data(ttl=600)
def load_users_db():
    try:
        return conn.read(worksheet="users")
    except:
        return pd.DataFrame(columns=["username", "password", "created_at"])

def user_exists(username: str) -> bool:
    df = load_users_db()
    if df.empty: return False
    return username.lower() in df['username'].str.lower().values

def create_user(username: str, email: str, password: str) -> tuple[bool, str]:
    username = username.strip().lower()
    if user_exists(username):
        return False, "❌ Cet utilisateur existe déjà"
    
    df = conn.read(worksheet="users", ttl=0)
    new_user = pd.DataFrame([{
        "username": username,
        "password": hash_password(password),
        "created_at": datetime.now().isoformat()
    }])
    
    updated_df = pd.concat([df, new_user], ignore_index=True)
    conn.update(worksheet="users", data=updated_df)
    force_refresh_cache()
    return True, "✅ Compte créé avec succès !"

def login_user(username: str, password: str) -> tuple[bool, str]:
    username = username.strip().lower()
    df = load_users_db()
    if df.empty: return False, "❌ Aucun utilisateur enregistré"
    
    user_row = df[df['username'].str.lower() == username]
    if user_row.empty:
        return False, "❌ Utilisateur non trouvé"
    
    if str(user_row.iloc[0]['password']) == hash_password(password):
        return True, f"✅ Bienvenue {username} !"
    return False, "❌ Mot de passe incorrect"

def get_user_info(username: str) -> dict:
    """Récupère les infos d'un utilisateur (appelé par app.py)."""
    df = load_users_db()
    user_row = df[df['username'].str.lower() == username.lower()]
    if not user_row.empty:
        info = user_row.iloc[0].to_dict()
        if "password" in info: del info["password"]
        return info
    return {}

def delete_user(username: str) -> tuple[bool, str]:
    """Supprime un utilisateur (Admin)."""
    try:
        df = conn.read(worksheet="users", ttl=0)
        df = df[df['username'].str.lower() != username.lower()]
        conn.update(worksheet="users", data=df)
        force_refresh_cache()
        return True, f"✅ Utilisateur {username} supprimé"
    except:
        return False, "❌ Erreur lors de la suppression"

# ===================== GESTION DES SCORES & STATS =====================

@st.cache_data(ttl=60)
def load_user_scores(username: str) -> dict:
    try:
        df = conn.read(worksheet="scores")
        user_rows = df[df['username'] == username]
        quizzes = {}
        for _, row in user_rows.iterrows():
            quizzes[row['quiz_key']] = {
                "scores": json.loads(row['scores_json']),
                "last_updated": row['last_updated']
            }
        return {"quizzes": quizzes}
    except:
        return {"quizzes": {}}

def save_user_scores(username: str, quiz_key: str, theme_scores: dict):
    try:
        df = conn.read(worksheet="scores", ttl=0)
    except:
        df = pd.DataFrame(columns=["username", "quiz_key", "scores_json", "last_updated"])
    
    scores_json = json.dumps(theme_scores)
    now = datetime.now().isoformat()
    mask = (df['username'] == username) & (df['quiz_key'] == quiz_key)
    
    if any(mask):
        df.loc[mask, 'scores_json'] = scores_json
        df.loc[mask, 'last_updated'] = now
    else:
        new_score = pd.DataFrame([{"username": username, "quiz_key": quiz_key, "scores_json": scores_json, "last_updated": now}])
        df = pd.concat([df, new_score], ignore_index=True)
    
    conn.update(worksheet="scores", data=df)
    force_refresh_cache()

def reset_quiz_scores(username: str, quiz_key: str):
    """Efface les scores d'un quiz spécifique pour un utilisateur."""
    try:
        df = conn.read(worksheet="scores", ttl=0)
        df = df[~((df['username'] == username) & (df['quiz_key'] == quiz_key))]
        conn.update(worksheet="scores", data=df)
        force_refresh_cache()
    except: pass

def get_user_stats(username: str) -> dict:
    """Calcule les statistiques globales pour le profil."""
    user_scores = load_user_scores(username)
    quizzes = user_scores.get("quizzes", {})
    stats = {"total_quizzes": len(quizzes), "total_themes": 0, "total_questions": 0, "total_correct": 0, "average_percentage": 0}

    for quiz_key, quiz_data in quizzes.items():
        scores = quiz_data.get("scores", {})
        stats["total_themes"] += len(scores)
        for theme_num, score_str in scores.items():
            try:
                parts = score_str.split("/")
                stats["total_correct"] += int(parts[0])
                stats["total_questions"] += int(parts[1])
            except: continue
    if stats["total_questions"] > 0:
        stats["average_percentage"] = round((stats["total_correct"] / stats["total_questions"]) * 100, 1)
    return stats

def export_user_scores_txt(username: str, quiz_titles_map: dict = None) -> str:
    """Génère un bilan texte des résultats avec un formatage propre et lisible."""
    user_data = load_user_scores(username)
    quizzes = user_data.get("quizzes", {})
    
    # En-tête du document
    lines = [
        "="*60,
        f"BILAN DES RÉSULTATS - {username.upper()}",
        "="*60,
        f"Document généré le : {datetime.now().strftime('%d/%m/%Y à %H:%M')}",
        ""
    ]
    
    if not quizzes:
        lines.append("Aucun score enregistré pour le moment.")
        return "\n".join(lines)

    for quiz_key, quiz_data in quizzes.items():
        scores = quiz_data.get("scores", {})
        
        # --- 1. NETTOYAGE DU NOM DU QUIZ ---
        # Si on passe le catalogue des titres, on prend le vrai titre, 
        # sinon on transforme 'cap_anglais_2' en 'CAP ANGLAIS 2'
        display_title = quiz_key
        if quiz_titles_map and quiz_key in quiz_titles_map:
            display_title = quiz_titles_map[quiz_key].get('title', quiz_key)
        else:
            display_title = quiz_key.replace("_", " ").upper()

        # --- 2. FORMATAGE DE LA DATE ---
        raw_date = quiz_data.get('last_updated', '')
        formatted_date = "N/A"
        if raw_date:
            try:
                # On transforme le format technique (ISO) en format humain
                dt = datetime.fromisoformat(raw_date)
                formatted_date = dt.strftime('%d/%m/%Y à %H:%M')
            except:
                formatted_date = raw_date # Sécurité en cas de format imprévu

        # --- 3. CONSTRUCTION DU BLOC QUIZ ---
        lines.append(f"📌 QUIZ : {display_title}")
        lines.append(f"📅 Dernière mise à jour : {formatted_date}")
        lines.append("-" * 30)
        
        # Tri des thèmes pour un affichage ordonné (1, 2, 3...)
        for theme_num in sorted(scores.keys(), key=lambda x: int(x) if x.isdigit() else x):
            lines.append(f"  • Thème {theme_num} : {scores[theme_num]}")
        
        lines.append("") # Espace entre les quiz
        lines.append("=" * 60)
        lines.append("")

    return "\n".join(lines)
# ===================== SIGNALEMENTS =====================

@st.cache_data(ttl=60)
def get_all_reports():
    try:
        df = conn.read(worksheet="reports")
        if df.empty: return []
        for col in ['id', 'theme', 'q_idx']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        return df.to_dict('records')
    except:
        return []

def save_question_report(username, quiz_key, theme_num, q_idx, question_text, reason):
    try:
        df = conn.read(worksheet="reports", ttl=0)
    except:
        df = pd.DataFrame(columns=["id", "date", "username", "quiz", "theme", "q_idx", "question", "reason"])
    
    new_report = pd.DataFrame([{
        "id": len(df) + 1, 
        "date": datetime.now().isoformat(), 
        "username": username,
        "quiz": quiz_key, 
        "theme": theme_num, 
        "q_idx": int(q_idx), # On force l'entier ici
        "question": question_text, 
        "reason": reason
    }])
    
    conn.update(worksheet="reports", data=pd.concat([df, new_report], ignore_index=True))
    force_refresh_cache()

def delete_report(report_id):
    try:
        df = conn.read(worksheet="reports", ttl=0)
        df = df[df['id'] != report_id]
        conn.update(worksheet="reports", data=df)
        force_refresh_cache()
        return True
    except:
        return False

def get_global_stats():
    """Récupère les statistiques de tous les utilisateurs pour l'Admin."""
    try:
        # On lit la feuille des scores sans cache pour la précision
        df = conn.read(worksheet="scores", ttl=0)
        if df.empty:
            return None

        # On décode le JSON des scores pour chaque ligne
        all_data = []
        for _, row in df.iterrows():
            scores = json.loads(row['scores_json'])
            for theme, val in scores.items():
                try:
                    p = val.split("/")
                    all_data.append({
                        "quiz": row['quiz_key'],
                        "user": row['username'],
                        "score_val": int(p[0]),
                        "total_val": int(p[1]),
                        "percent": (int(p[0]) / int(p[1])) * 100
                    })
                except: continue
        
        return pd.DataFrame(all_data)
    except:
        return None