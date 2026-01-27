import json
import streamlit as st
import google.generativeai as genai


def generate_single_question(diploma: str, theme: str, difficulty: str) -> dict:
    """
    Génère une SEULE question via Gemini et la renvoie sous forme de dict.
    Retourne None en cas d'erreur.
    """
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in secrets")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
Tu es un expert pédagogue en formation professionnelle française.
Génère UNE SEULE question de QCM pour la formation suivante :

- Diplôme : {diploma}
- Thème : {theme}
- Niveau de difficulté : {difficulty}

EXIGENCES STRICTES :
1. La sortie doit être UNIQUEMENT du JSON valide.
2. Le format doit être exactement :

{{
  "id": "q1",
  "question": "texte de la question",
  "answerOptions": [
    {{"text": "réponse A", "isCorrect": true}},
    {{"text": "réponse B", "isCorrect": false}},
    {{"text": "réponse C", "isCorrect": false}},
    {{"text": "réponse D", "isCorrect": false}}
  ],
  "correction": "explication pédagogique de 2 à 5 phrases"
}}

3. Il doit y avoir EXACTEMENT 4 réponses.
4. Il doit y avoir EXACTEMENT UNE réponse avec "isCorrect": true.
5. Les trois autres réponses doivent avoir "isCorrect": false.
6. Les réponses doivent être de longueur similaire (pas une très longue et trois très courtes).
7. Les mauvaises réponses doivent être crédibles et liées au métier concerné.
8. Le texte ne doit contenir AUCUN commentaire en dehors du JSON (pas de texte avant ou après).
"""

    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()

        # Debug éventuel (à commenter ensuite)
        # print("RAW RESPONSE:", response_text)

        question_data = json.loads(response_text)
        return question_data

    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return None
    except Exception as e:
        print(f"Error generating question: {e}")
        return None


# Test en mode script (python llm_quiz_generator.py)
if __name__ == "__main__":
    q = generate_single_question(
        diploma="CAP Boucher",
        theme="Hygiène alimentaire",
        difficulty="novice",
    )
    if q:
        print("✓ Question générée :")
        print(json.dumps(q, ensure_ascii=False, indent=2))
    else:
        print("✗ Erreur lors de la génération")
