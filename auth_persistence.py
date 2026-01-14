# ==================================================================
# AUTH PERSISTENCE - User Authentication & Score Management
# ==================================================================
import json
import hashlib
from pathlib import Path
from datetime import datetime

# ===================== PATHS =====================
DATA_DIR = Path("data")
USERS_FILE = DATA_DIR / "users.json"
SCORES_DIR = DATA_DIR / "scores"

# Crée les répertoires s'ils n'existent pas
DATA_DIR.mkdir(exist_ok=True)
SCORES_DIR.mkdir(exist_ok=True)

# ===================== UTILITY FUNCTIONS =====================

def hash_password(password: str) -> str:
    """
    Hache un mot de passe en SHA256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def load_users_db() -> dict:
    """
    Charge la base de données des utilisateurs.
    Crée un fichier vide si inexistant.
    """
    if USERS_FILE.exists():
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_users_db(users: dict):
    """
    Sauvegarde la base de données des utilisateurs.
    """
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Erreur sauvegarde utilisateurs: {e}")

def load_user_scores(username: str) -> dict:
    """
    Charge les scores d'un utilisateur.
    Crée un fichier vide si inexistant.
    """
    score_file = SCORES_DIR / f"{username}.json"
    
    if score_file.exists():
        try:
            with open(score_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"quizzes": {}}
    
    return {"quizzes": {}, "created_at": datetime.now().isoformat()}

def save_user_scores(username: str, quiz_key: str, theme_scores: dict):
    """
    Sauvegarde les scores d'un utilisateur pour un quiz donné.
    
    Args:
        username: nom d'utilisateur
        quiz_key: clé du quiz (ex: "cap_boucher_100")
        theme_scores: dict {theme_num: score} (ex: {"0": "8/10", "1": "9/10"})
    """
    score_file = SCORES_DIR / f"{username}.json"
    
    user_data = load_user_scores(username)
    
    if "quizzes" not in user_data:
        user_data["quizzes"] = {}
    
    user_data["quizzes"][quiz_key] = {
        "scores": theme_scores,
        "last_updated": datetime.now().isoformat()
    }
    
    try:
        with open(score_file, "w", encoding="utf-8") as f:
            json.dump(user_data, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Erreur sauvegarde scores: {e}")

def reset_quiz_scores(username: str, quiz_key: str):
    """
    Réinitialise les scores d'un quiz pour un utilisateur.
    """
    score_file = SCORES_DIR / f"{username}.json"
    
    user_data = load_user_scores(username)
    
    if quiz_key in user_data.get("quizzes", {}):
        del user_data["quizzes"][quiz_key]
    
    try:
        with open(score_file, "w", encoding="utf-8") as f:
            json.dump(user_data, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Erreur lors de la réinitialisation: {e}")

# ===================== AUTHENTICATION =====================

def user_exists(username: str) -> bool:
    """
    Vérifie si un utilisateur existe.
    """
    users = load_users_db()
    return username.lower() in users

def email_exists(email: str) -> bool:
    """
    Vérifie si un email est déjà utilisé.
    """
    users = load_users_db()
    for user_data in users.values():
        if user_data.get("email", "").lower() == email.lower():
            return True
    return False

def create_user(username: str, email: str, password: str) -> tuple[bool, str]:
    """
    Crée un nouvel utilisateur.
    
    Returns:
        (success: bool, message: str)
    """
    username = username.strip().lower()
    email = email.strip().lower()
    
    # Validations
    if not username or len(username) < 3:
        return False, "❌ Le nom d'utilisateur doit avoir au moins 3 caractères"
    
    if not email or "@" not in email:
        return False, "❌ Email invalide"
    
    if not password or len(password) < 6:
        return False, "❌ Le mot de passe doit avoir au moins 6 caractères"
    
    if user_exists(username):
        return False, "❌ Cet utilisateur existe déjà"
    
    if email_exists(email):
        return False, "❌ Cet email est déjà utilisé"
    
    # Crée l'utilisateur
    users = load_users_db()
    users[username] = {
        "email": email,
        "password": hash_password(password),
        "created_at": datetime.now().isoformat(),
    }
    
    save_users_db(users)
    return True, f"✅ Compte créé avec succès !"

def login_user(username: str, password: str) -> tuple[bool, str]:
    """
    Authentifie un utilisateur.
    
    Returns:
        (success: bool, message: str)
    """
    username = username.strip().lower()
    
    if not username or not password:
        return False, "❌ Veuillez remplir tous les champs"
    
    users = load_users_db()
    
    if username not in users:
        return False, "❌ Utilisateur non trouvé"
    
    user_data = users[username]
    hashed = hash_password(password)
    
    if user_data.get("password") != hashed:
        return False, "❌ Mot de passe incorrect"
    
    return True, f"✅ Bienvenue {username} !"

def get_user_info(username: str) -> dict:
    """
    Retourne les informations d'un utilisateur.
    """
    users = load_users_db()
    if username.lower() in users:
        user_data = users[username.lower()].copy()
        user_data.pop("password", None)  # Ne pas exposer le hash
        return user_data
    return {}

def get_user_stats(username: str) -> dict:
    """
    Retourne les statistiques d'un utilisateur.
    """
    user_scores = load_user_scores(username)
    quizzes = user_scores.get("quizzes", {})

    stats = {
        "total_quizzes": len(quizzes),
        "total_themes": 0,
        "total_questions": 0,
        "total_correct": 0,
        "average_percentage": 0,
    }

    for quiz_key, quiz_data in quizzes.items():
        scores = quiz_data.get("scores", {})
        stats["total_themes"] += len(scores)

        for theme_num, score_str in scores.items():
            # On ne traite que les chaînes de type "8/10"
            if not isinstance(score_str, str):
                continue
            try:
                parts = score_str.split("/")
                correct = int(parts[0])
                total = int(parts[1])
                stats["total_questions"] += total
                stats["total_correct"] += correct
            except (ValueError, IndexError):
                # Ignore les formats invalides
                continue

    if stats["total_questions"] > 0:
        stats["average_percentage"] = round(
            (stats["total_correct"] / stats["total_questions"]) * 100, 1
        )

    return stats



# ===================== DATA EXPORT =====================

def export_user_scores_txt(username: str, quiz_title: str = None) -> str:
    """
    Exporte les scores d'un utilisateur en texte.
    
    Args:
        username: nom d'utilisateur
        quiz_title: titre optionnel du quiz (pour un quiz spécifique)
    
    Returns:
        str: contenu formaté en texte
    """
    user_data = load_user_scores(username)
    quizzes = user_data.get("quizzes", {})
    
    lines = [
        "=" * 60,
        f"RÉSULTATS DES QUIZ - {username.upper()}",
        "=" * 60,
        f"Date d'export : {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "",
    ]
    
    total_score = 0
    total_max = 0
    quiz_count = 0
    
    for quiz_key, quiz_data in quizzes.items():
        scores = quiz_data.get("scores", {})
        last_updated = quiz_data.get("last_updated", "")
        
        lines.append(f"Quiz : {quiz_key}")
        if last_updated:
            lines.append(f"Dernière mise à jour : {last_updated}")
        lines.append("-" * 60)
        
        for theme_num in sorted(scores.keys()):
            score_str = scores[theme_num]
            lines.append(f"  Thème {theme_num} : {score_str}")
            
            try:
                parts = score_str.split("/")
                correct = int(parts[0])
                total = int(parts[1])
                total_score += correct
                total_max += total
                quiz_count += 1
            except (ValueError, IndexError):
                pass
        
        lines.append("")
    
    lines.append("=" * 60)
    lines.append(f"TOTAL : {total_score}/{total_max}")
    
    if total_max > 0:
        percentage = (total_score / total_max) * 100
        lines.append(f"Pourcentage global : {percentage:.1f}%")
    
    lines.append(f"Nombre de quiz complétés : {quiz_count}")
    lines.append("=" * 60)
    
    return "\n".join(lines)

# ===================== CLEANUP / ADMIN =====================

def delete_user(username: str) -> tuple[bool, str]:
    """
    Supprime un utilisateur et ses scores.
    ⚠️ ATTENTION : Opération irréversible
    """
    username = username.lower()
    
    users = load_users_db()
    if username not in users:
        return False, "❌ Utilisateur non trouvé"
    
    del users[username]
    save_users_db(users)
    
    # Supprimer les scores
    score_file = SCORES_DIR / f"{username}.json"
    if score_file.exists():
        score_file.unlink()
    
    return True, f"✅ Utilisateur {username} supprimé"

def get_all_users_list() -> list:
    """
    Retourne la liste de tous les utilisateurs (admin).
    """
    users = load_users_db()
    return list(users.keys())

def get_all_users_stats() -> dict:
    """
    Retourne les stats globales de tous les utilisateurs (admin).
    """
    users = get_all_users_list()
    stats = {
        "total_users": len(users),
        "users": {}
    }
    
    for username in users:
        user_stats = get_user_stats(username)
        stats["users"][username] = user_stats
    
    return stats