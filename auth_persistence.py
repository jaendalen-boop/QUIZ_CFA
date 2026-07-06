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

def save_user_scores(username: str, quiz_key: str, theme_scores: dict, exam_attempt: bool = False, exam_score: int = None):
    """Sauvegarde les scores dans Google Sheets (remplace la version fichier)."""
    username = username.strip().lower()
    
    # 1. Lire les scores actuels depuis Google Sheets
    try:
        df = conn.read(worksheet="scores", ttl=0)
    except:
        df = pd.DataFrame(columns=["username", "quiz_key", "scores_json", "last_updated"])

    # 2. Trouver la ligne de l'utilisateur pour ce quiz
    mask = (df['username'] == username) & (df['quiz_key'] == quiz_key)
    
    if any(mask):
        # Récupérer les données existantes
        existing_data = json.loads(df.loc[mask, 'scores_json'].values[0])
    else:
        existing_data = {"scores": {}, "exam_stats": {"attempts": 0, "best_score": 0}}

    # 3. Mise à jour des thèmes et stats
    for t_num, score in theme_scores.items():
        if score is not None:
            existing_data["scores"][str(t_num)] = score
            
    if exam_attempt:
        existing_data["exam_stats"]["attempts"] += 1
        if exam_score is not None:
            if exam_score > existing_data["exam_stats"].get("best_score", 0):
                existing_data["exam_stats"]["best_score"] = exam_score

    # 4. Préparer la mise à jour du DataFrame
    new_json = json.dumps(existing_data, ensure_ascii=False)
    
    if any(mask):
        df.loc[mask, 'scores_json'] = new_json
        df.loc[mask, 'last_updated'] = datetime.now().isoformat()
    else:
        new_row = pd.DataFrame([{
            "username": username,
            "quiz_key": quiz_key,
            "scores_json": new_json,
            "last_updated": datetime.now().isoformat()
        }])
        df = pd.concat([df, new_row], ignore_index=True)

    # 5. Envoyer au Sheets
    conn.update(worksheet="scores", data=df)
    force_refresh_cache()
    return True

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

# ===================== GESTION DES CORRECTIONS DE QUESTIONS =====================

@st.cache_data(ttl=60)
def load_all_modified_questions() -> pd.DataFrame:
    """Charge l'intégralité de l'onglet des questions modifiées avec mise en cache."""
    try:
        df = conn.read(worksheet="modified_questions")
        if df.empty:
            return pd.DataFrame(columns=["quiz_key", "theme_id", "question_idx", "question_text", "options_json", "correction_text"])
        
        # Sécurité de typage pour les indexations numériques
        for col in ['theme_id', 'question_idx']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        return df
    except:
        return pd.DataFrame(columns=["quiz_key", "theme_id", "question_idx", "question_text", "options_json", "correction_text"])


def save_modified_question(quiz_key: str, theme_id: int, question_idx: int, question_text: str, options_list: list, correction_text: str) -> bool:
    """Enregistre ou met à jour une correction de question dans Google Sheets."""
    try:
        # Lecture sans cache pour avoir l'état réel avant écriture
        df = conn.read(worksheet="modified_questions", ttl=0)
    except:
        df = pd.DataFrame(columns=["quiz_key", "theme_id", "question_idx", "question_text", "options_json", "correction_text"])
    
    # Normalisation des types pour la comparaison
    theme_id = int(theme_id)
    question_idx = int(question_idx)
    options_json = json.dumps(options_list, ensure_ascii=False)
    
    # Masque pour vérifier si cette question spécifique a déjà été modifiée auparavant
    mask = (df['quiz_key'] == quiz_key) & (df['theme_id'] == theme_id) & (df['question_idx'] == question_idx)
    
    if any(mask):
        # Mise à jour de la ligne existante
        df.loc[mask, 'question_text'] = question_text
        df.loc[mask, 'options_json'] = options_json
        df.loc[mask, 'correction_text'] = correction_text
    else:
        # Création d'une nouvelle ligne
        new_row = pd.DataFrame([{
            "quiz_key": quiz_key,
            "theme_id": theme_id,
            "question_idx": question_idx,
            "question_text": question_text,
            "options_json": options_json,
            "correction_text": correction_text
        }])
        df = pd.concat([df, new_row], ignore_index=True)
    
    # Envoi de la mise à jour vers Google Sheets et purge du cache local
    conn.update(worksheet="modified_questions", data=df)
    force_refresh_cache()
    
    # --- AJOUT SÉCURISÉ POUR LE CACHE DE 4 HEURES ---
    # Vide instantanément le nouveau cache Streamlit pour que les élèves voient la modification
    st.cache_data.clear()
    
    return True


@st.cache_data(ttl=14400)  # 14400 secondes = 4 heures de cache ultra-rapide
def get_modified_questions_for_quiz(quiz_key: str) -> dict:
    """
    Récupère les questions modifiées depuis Google Sheets pour un quiz donné.
    Les résultats sont mis en cache pendant 4 heures pour éliminer les temps de chargement.
    """
    import pandas as pd
    try:
        # Connexion à Google Sheets via l'URL d'export CSV de l'onglet modified_questions
        sheet_id = "1bY_vWb_v7-X_zJmH_your_sheet_id_here"  # Votre ID de feuille réel déjà présent dans votre code
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=modified_questions"
        
        df = pd.read_csv(url)
        
        # Nettoyage et filtrage des données pour le quiz demandé
        df.columns = df.columns.str.strip()
        df_quiz = df[df['quiz'].astype(str).str.strip() == str(quiz_key).strip()]
        
        corrections = {}
        for _, row in df_quiz.iterrows():
            try:
                theme_id = int(float(row['theme']))
                q_idx = int(float(row['q_idx']))
            except:
                continue
                
            if theme_id not in corrections:
                corrections[theme_id] = {}
                
            # Reconstruction de la structure de la question (Options A, B, C, D)
            options = []
            for letter in ['A', 'B', 'C', 'D']:
                opt_text = row.get(f'opt_{letter}')
                opt_corr = row.get(f'corr_{letter}')
                if pd.notna(opt_text):
                    is_correct = False
                    if pd.notna(opt_corr):
                        is_correct = str(opt_corr).strip().lower() in ['true', '1', 'yes', 'x']
                    options.append({"text": str(opt_text).strip(), "isCorrect": is_correct})
            
            corrections[theme_id][q_idx] = {
                "question": str(row['question']).strip(),
                "answerOptions": options,
                "correction": str(row['correction']).strip() if pd.notna(row.get('correction')) else ""
            }
        return corrections
    except Exception:
        # En cas de problème réseau ou de feuille vide, on retourne un dictionnaire vide sans bloquer l'application
        return {}