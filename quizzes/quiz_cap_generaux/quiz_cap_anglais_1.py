quiz_data = {
    "title": "Quiz Anglais - Niveau CAP (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : SE PRÉSENTER ET VIE QUOTIDIENNE (Q1 à Q20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : SE PRÉSENTER ET VIE QUOTIDIENNE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la forme correcte pour dire 'J'habite à Londres' ?",
                    "answerOptions": [
                        {"text": "I live in London", "isCorrect": True},
                        {"text": "I lives in London", "isCorrect": False},
                        {"text": "I living in London", "isCorrect": False},
                        {"text": "I to live in London", "isCorrect": False}
                    ],
                    "correction": "Au présent simple, à la première personne du singulier (I), le verbe ne prend pas de 's' ou de terminaison 'ing'. On utilise le sujet suivi de la base verbale."
                },
                {
                    "questionNumber": 2,
                    "question": "Comment demande-t-on 'Quel âge as-tu ?' en anglais ?",
                    "answerOptions": [
                        {"text": "How old are you?", "isCorrect": True},
                        {"text": "How many years do you have?", "isCorrect": False},
                        {"text": "What age do you have?", "isCorrect": False},
                        {"text": "Which age is yours?", "isCorrect": False}
                    ],
                    "correction": "En anglais, l'âge se construit avec le verbe être (to be) et l'adjectif 'old', contrairement au français qui utilise le verbe avoir."
                },
                {
                    "questionNumber": 3,
                    "question": "Complétez la phrase : 'She ______ up at 7:00 am.'",
                    "answerOptions": [
                        {"text": "gets", "isCorrect": True},
                        {"text": "get", "isCorrect": False},
                        {"text": "getting", "isCorrect": False},
                        {"text": "to get", "isCorrect": False}
                    ],
                    "correction": "À la troisième personne du singulier (she, he, it) au présent simple, on doit ajouter un 's' à la fin du verbe."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment dit-on 'Enchanté' lors d'une rencontre ?",
                    "answerOptions": [
                        {"text": "Nice to meet you", "isCorrect": True},
                        {"text": "Good to meet you", "isCorrect": False},
                        {"text": "Hello you", "isCorrect": False},
                        {"text": "Fine thanks", "isCorrect": False}
                    ],
                    "correction": "'Nice to meet you' est la formule standard de politesse lors d'une première rencontre."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel jour de la semaine se situe entre 'Tuesday' et 'Thursday' ?",
                    "answerOptions": [
                        {"text": "Wednesday", "isCorrect": True},
                        {"text": "Monday", "isCorrect": False},
                        {"text": "Friday", "isCorrect": False},
                        {"text": "Saturday", "isCorrect": False}
                    ],
                    "correction": "L'ordre est : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday."
                },
                {
                    "questionNumber": 6,
                    "question": "Comment dit-on 'Il est dix heures' ?",
                    "answerOptions": [
                        {"text": "It is ten o'clock", "isCorrect": True},
                        {"text": "It has ten o'clock", "isCorrect": False},
                        {"text": "He is ten o'clock", "isCorrect": False},
                        {"text": "There is ten o'clock", "isCorrect": False}
                    ],
                    "correction": "Pour donner l'heure, on utilise la structure impersonnelle 'It is'."
                },
                {
                    "questionNumber": 7,
                    "question": "Choisissez la forme correcte : '______ you like coffee?'",
                    "answerOptions": [
                        {"text": "Do", "isCorrect": True},
                        {"text": "Does", "isCorrect": False},
                        {"text": "Are", "isCorrect": False},
                        {"text": "Is", "isCorrect": False}
                    ],
                    "correction": "Pour poser une question au présent simple avec 'you', on utilise l'auxiliaire 'Do'."
                },
                {
                    "questionNumber": 8,
                    "question": "Comment dit-on 'Petit-déjeuner' ?",
                    "answerOptions": [
                        {"text": "Breakfast", "isCorrect": True},
                        {"text": "Lunch", "isCorrect": False},
                        {"text": "Dinner", "isCorrect": False},
                        {"text": "Snack", "isCorrect": False}
                    ],
                    "correction": "'Breakfast' signifie littéralement casser (break) le jeûne (fast)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le pluriel de 'child' ?",
                    "answerOptions": [
                        {"text": "children", "isCorrect": True},
                        {"text": "childs", "isCorrect": False},
                        {"text": "childrens", "isCorrect": False},
                        {"text": "childes", "isCorrect": False}
                    ],
                    "correction": "'Child' est un pluriel irrégulier très courant."
                },
                {
                    "questionNumber": 10,
                    "question": "Comment dit-on 'S'il vous plaît' ?",
                    "answerOptions": [
                        {"text": "Please", "isCorrect": True},
                        {"text": "Thank you", "isCorrect": False},
                        {"text": "Welcome", "isCorrect": False},
                        {"text": "Sorry", "isCorrect": False}
                    ],
                    "correction": "'Please' s'utilise pour demander poliment."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la traduction de 'Aujourd'hui' ?",
                    "answerOptions": [
                        {"text": "Today", "isCorrect": True},
                        {"text": "Yesterday", "isCorrect": False},
                        {"text": "Tomorrow", "isCorrect": False},
                        {"text": "Tonight", "isCorrect": False}
                    ],
                    "correction": "'Today' désigne le jour présent."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment dit-on 'Je m'appelle...' ?",
                    "answerOptions": [
                        {"text": "My name is...", "isCorrect": True},
                        {"text": "I call me...", "isCorrect": False},
                        {"text": "I am name...", "isCorrect": False},
                        {"text": "Me is...", "isCorrect": False}
                    ],
                    "correction": "On utilise le possessif 'My name is' ou simplement 'I am'."
                },
                {
                    "questionNumber": 13,
                    "question": "Choisissez l'article correct : 'I want ______ apple.'",
                    "answerOptions": [
                        {"text": "an", "isCorrect": True},
                        {"text": "a", "isCorrect": False},
                        {"text": "the", "isCorrect": False},
                        {"text": "some", "isCorrect": False}
                    ],
                    "correction": "On utilise 'an' devant un mot commençant par une voyelle ou un son voyelle."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel mois vient juste après 'June' ?",
                    "answerOptions": [
                        {"text": "July", "isCorrect": True},
                        {"text": "August", "isCorrect": False},
                        {"text": "May", "isCorrect": False},
                        {"text": "April", "isCorrect": False}
                    ],
                    "correction": "L'ordre est : May, June, July, August."
                },
                {
                    "questionNumber": 15,
                    "question": "Comment dit-on 'Où habites-tu ?' ?",
                    "answerOptions": [
                        {"text": "Where do you live?", "isCorrect": True},
                        {"text": "What do you live?", "isCorrect": False},
                        {"text": "Who do you live?", "isCorrect": False},
                        {"text": "When do you live?", "isCorrect": False}
                    ],
                    "correction": "'Where' est le mot interrogatif pour interroger sur le lieu."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la couleur du ciel par beau temps ?",
                    "answerOptions": [
                        {"text": "Blue", "isCorrect": True},
                        {"text": "Red", "isCorrect": False},
                        {"text": "Green", "isCorrect": False},
                        {"text": "Black", "isCorrect": False}
                    ],
                    "correction": "'Blue' signifie bleu."
                },
                {
                    "questionNumber": 17,
                    "question": "Comment dit-on 'Frère' ?",
                    "answerOptions": [
                        {"text": "Brother", "isCorrect": True},
                        {"text": "Sister", "isCorrect": False},
                        {"text": "Father", "isCorrect": False},
                        {"text": "Mother", "isCorrect": False}
                    ],
                    "correction": "'Brother' (frère) vs 'Sister' (sœur)."
                },
                {
                    "questionNumber": 18,
                    "question": "Traduisez : 'Je suis fatigué'.",
                    "answerOptions": [
                        {"text": "I am tired", "isCorrect": True},
                        {"text": "I am sleep", "isCorrect": False},
                        {"text": "I have tired", "isCorrect": False},
                        {"text": "I am angry", "isCorrect": False}
                    ],
                    "correction": "'Tired' est l'adjectif pour la fatigue."
                },
                {
                    "questionNumber": 19,
                    "question": "Comment dit-on 'Au revoir' ?",
                    "answerOptions": [
                        {"text": "Goodbye", "isCorrect": True},
                        {"text": "Hello", "isCorrect": False},
                        {"text": "Welcome", "isCorrect": False},
                        {"text": "Please", "isCorrect": False}
                    ],
                    "correction": "'Goodbye' ou 'Bye' sont les formes les plus courantes."
                },
                {
                    "questionNumber": 20,
                    "question": "Comment demande-t-on 'Comment ça va ?' ?",
                    "answerOptions": [
                        {"text": "How are you?", "isCorrect": True},
                        {"text": "How you go?", "isCorrect": False},
                        {"text": "What are you?", "isCorrect": False},
                        {"text": "Who are you?", "isCorrect": False}
                    ],
                    "correction": "'How are you?' est la salutation standard pour prendre des nouvelles."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : GRAMMAIRE ET CONJUGAISON DE BASE (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : GRAMMAIRE ET CONJUGAISON DE BASE",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le pronom personnel pour 'Il' ?",
                    "answerOptions": [
                        {"text": "He", "isCorrect": True},
                        {"text": "She", "isCorrect": False},
                        {"text": "It", "isCorrect": False},
                        {"text": "They", "isCorrect": False}
                    ],
                    "correction": "'He' est utilisé pour un homme, 'She' pour une femme et 'It' pour un objet ou un animal."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment forme-t-on généralement le pluriel en anglais ?",
                    "answerOptions": [
                        {"text": "On ajoute un -s", "isCorrect": True},
                        {"text": "On ajoute un -es", "isCorrect": False},
                        {"text": "On ne change rien", "isCorrect": False},
                        {"text": "On double la consonne", "isCorrect": False}
                    ],
                    "correction": "La règle générale est l'ajout d'un 's' (ex: one car -> two cars)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la forme négative de 'I like tea' ?",
                    "answerOptions": [
                        {"text": "I don't like tea", "isCorrect": True},
                        {"text": "I not like tea", "isCorrect": False},
                        {"text": "I no like tea", "isCorrect": False},
                        {"text": "I doesn't like tea", "isCorrect": False}
                    ],
                    "correction": "Au présent simple, on utilise 'do not' (don't) pour former la négation avec 'I'."
                },
                {
                    "questionNumber": 24,
                    "question": "Choisissez la bonne forme de 'to be' : 'We ______ happy.'",
                    "answerOptions": [
                        {"text": "are", "isCorrect": True},
                        {"text": "is", "isCorrect": False},
                        {"text": "am", "isCorrect": False},
                        {"text": "be", "isCorrect": False}
                    ],
                    "correction": "Conjugaison de 'to be' : I am, you are, he/she/it is, we are, you are, they are."
                },
                {
                    "questionNumber": 25,
                    "question": "Que signifie 'always' ?",
                    "answerOptions": [
                        {"text": "Toujours", "isCorrect": True},
                        {"text": "Souvent", "isCorrect": False},
                        {"text": "Parfois", "isCorrect": False},
                        {"text": "Jamais", "isCorrect": False}
                    ],
                    "correction": "'Always' est un adverbe de fréquence indiquant 100% du temps."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel auxiliaire utilise-t-on pour le futur ?",
                    "answerOptions": [
                        {"text": "Will", "isCorrect": True},
                        {"text": "Do", "isCorrect": False},
                        {"text": "Have", "isCorrect": False},
                        {"text": "Was", "isCorrect": False}
                    ],
                    "correction": "'Will' suivi de la base verbale permet d'exprimer le futur."
                },
                {
                    "questionNumber": 27,
                    "question": "Comment dit-on 'Ceci' (proche de moi) ?",
                    "answerOptions": [
                        {"text": "This", "isCorrect": True},
                        {"text": "That", "isCorrect": False},
                        {"text": "These", "isCorrect": False},
                        {"text": "Those", "isCorrect": False}
                    ],
                    "correction": "'This' désigne un objet proche au singulier. 'That' désigne un objet éloigné."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la traduction de 'Never' ?",
                    "answerOptions": [
                        {"text": "Jamais", "isCorrect": True},
                        {"text": "Quelquefois", "isCorrect": False},
                        {"text": "Rarement", "isCorrect": False},
                        {"text": "Bientôt", "isCorrect": False}
                    ],
                    "correction": "'Never' est l'adverbe de fréquence opposé à 'Always'."
                },
                {
                    "questionNumber": 29,
                    "question": "Complétez : 'He ______ a new car.'",
                    "answerOptions": [
                        {"text": "has", "isCorrect": True},
                        {"text": "have", "isCorrect": False},
                        {"text": "having", "isCorrect": False},
                        {"text": "haves", "isCorrect": False}
                    ],
                    "correction": "Le verbe 'to have' devient 'has' à la 3ème personne du singulier."
                },
                {
                    "questionNumber": 30,
                    "question": "Que signifie le mot interrogatif 'When' ?",
                    "answerOptions": [
                        {"text": "Quand", "isCorrect": True},
                        {"text": "Pourquoi", "isCorrect": False},
                        {"text": "Qui", "isCorrect": False},
                        {"text": "Comment", "isCorrect": False}
                    ],
                    "correction": "'When' interroge sur le temps/moment."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le prétérit (passé) de 'to work' ?",
                    "answerOptions": [
                        {"text": "worked", "isCorrect": True},
                        {"text": "work", "isCorrect": False},
                        {"text": "working", "isCorrect": False},
                        {"text": "worken", "isCorrect": False}
                    ],
                    "correction": "Pour les verbes réguliers, on ajoute -ed pour former le passé."
                },
                {
                    "questionNumber": 32,
                    "question": "Traduisez 'Beaucoup de' (pour des choses dénombrables) :",
                    "answerOptions": [
                        {"text": "Many", "isCorrect": True},
                        {"text": "Much", "isCorrect": False},
                        {"text": "Very", "isCorrect": False},
                        {"text": "Little", "isCorrect": False}
                    ],
                    "correction": "'Many' s'utilise pour ce qu'on peut compter, 'Much' pour ce qu'on ne peut pas compter."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment dit-on 'Ma voiture' ?",
                    "answerOptions": [
                        {"text": "My car", "isCorrect": True},
                        {"text": "Me car", "isCorrect": False},
                        {"text": "Mine car", "isCorrect": False},
                        {"text": "I car", "isCorrect": False}
                    ],
                    "correction": "'My' est l'adjectif possessif pour la première personne."
                },
                {
                    "questionNumber": 34,
                    "question": "Choisissez la bonne préposition : 'I am ______ the kitchen.'",
                    "answerOptions": [
                        {"text": "in", "isCorrect": True},
                        {"text": "on", "isCorrect": False},
                        {"text": "at", "isCorrect": False},
                        {"text": "under", "isCorrect": False}
                    ],
                    "correction": "'In' indique que l'on se trouve à l'intérieur d'un espace."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel auxiliaire utilise-t-on pour poser une question au prétérit ?",
                    "answerOptions": [
                        {"text": "Did", "isCorrect": True},
                        {"text": "Do", "isCorrect": False},
                        {"text": "Does", "isCorrect": False},
                        {"text": "Will", "isCorrect": False}
                    ],
                    "correction": "'Did' est l'auxiliaire du passé pour toutes les personnes."
                },
                {
                    "questionNumber": 36,
                    "question": "Complétez : 'They ______ English.'",
                    "answerOptions": [
                        {"text": "speak", "isCorrect": True},
                        {"text": "speaks", "isCorrect": False},
                        {"text": "speaking", "isCorrect": False},
                        {"text": "to speak", "isCorrect": False}
                    ],
                    "correction": "Avec 'they', le verbe reste à sa forme de base au présent."
                },
                {
                    "questionNumber": 37,
                    "question": "Que signifie 'Which' ?",
                    "answerOptions": [
                        {"text": "Lequel", "isCorrect": True},
                        {"text": "Quoi", "isCorrect": False},
                        {"text": "Où", "isCorrect": False},
                        {"text": "Qui", "isCorrect": False}
                    ],
                    "correction": "'Which' implique un choix entre plusieurs options."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la forme contractée de 'I am not' ?",
                    "answerOptions": [
                        {"text": "I'm not", "isCorrect": True},
                        {"text": "I amn't", "isCorrect": False},
                        {"text": "I'm don't", "isCorrect": False},
                        {"text": "I no am", "isCorrect": False}
                    ],
                    "correction": "Seule la contraction sur le sujet 'I'm' est possible ici."
                },
                {
                    "questionNumber": 39,
                    "question": "Traduisez : 'Il y a' (singulier).",
                    "answerOptions": [
                        {"text": "There is", "isCorrect": True},
                        {"text": "There are", "isCorrect": False},
                        {"text": "It has", "isCorrect": False},
                        {"text": "They are", "isCorrect": False}
                    ],
                    "correction": "'There is' pour le singulier, 'There are' pour le pluriel."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la terminaison des verbes en -ing au présent continu ?",
                    "answerOptions": [
                        {"text": "-ing", "isCorrect": True},
                        {"text": "-ed", "isCorrect": False},
                        {"text": "-s", "isCorrect": False},
                        {"text": "-ly", "isCorrect": False}
                    ],
                    "correction": "Le présent continu exprime une action en cours (ex: I am eating)."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : VOCABULAIRE DU TRAVAIL ET DE L'ENTREPRISE (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : VOCABULAIRE DU TRAVAIL ET DE L'ENTREPRISE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Comment dit-on 'Un emploi' ?",
                    "answerOptions": [
                        {"text": "A job", "isCorrect": True},
                        {"text": "A work", "isCorrect": False},
                        {"text": "A boss", "isCorrect": False},
                        {"text": "A salary", "isCorrect": False}
                    ],
                    "correction": "'Job' est dénombrable, 'Work' ne l'est pas."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel mot désigne le 'Patron' ?",
                    "answerOptions": [
                        {"text": "The boss", "isCorrect": True},
                        {"text": "The employee", "isCorrect": False},
                        {"text": "The customer", "isCorrect": False},
                        {"text": "The worker", "isCorrect": False}
                    ],
                    "correction": "'Boss' ou 'Manager' sont les termes courants."
                },
                {
                    "questionNumber": 43,
                    "question": "Traduisez : 'Une réunion'.",
                    "answerOptions": [
                        {"text": "A meeting", "isCorrect": True},
                        {"text": "A desk", "isCorrect": False},
                        {"text": "A tool", "isCorrect": False},
                        {"text": "A factory", "isCorrect": False}
                    ],
                    "correction": "Le verbe 'to meet' signifie rencontrer."
                },
                {
                    "questionNumber": 44,
                    "question": "Comment dit-on 'Salaire' ?",
                    "answerOptions": [
                        {"text": "Salary", "isCorrect": True},
                        {"text": "Money", "isCorrect": False},
                        {"text": "Price", "isCorrect": False},
                        {"text": "Bill", "isCorrect": False}
                    ],
                    "correction": "'Salary' désigne la rémunération mensuelle."
                },
                {
                    "questionNumber": 45,
                    "question": "Que signifie 'To hire' ?",
                    "answerOptions": [
                        {"text": "Embaucher", "isCorrect": True},
                        {"text": "Licencier", "isCorrect": False},
                        {"text": "Travailler", "isCorrect": False},
                        {"text": "Chercher", "isCorrect": False}
                    ],
                    "correction": "'To hire' (embaucher) vs 'To fire' (licencier)."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment dit-on 'Chercher un travail' ?",
                    "answerOptions": [
                        {"text": "To look for a job", "isCorrect": True},
                        {"text": "To find a job", "isCorrect": False},
                        {"text": "To give a job", "isCorrect": False},
                        {"text": "To lose a job", "isCorrect": False}
                    ],
                    "correction": "'Look for' est un verbe à particule signifiant chercher."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel mot désigne le 'Bureau' (le meuble) ?",
                    "answerOptions": [
                        {"text": "Desk", "isCorrect": True},
                        {"text": "Office", "isCorrect": False},
                        {"text": "Chair", "isCorrect": False},
                        {"text": "Computer", "isCorrect": False}
                    ],
                    "correction": "'Desk' est le meuble, 'Office' est la pièce/l'agence."
                },
                {
                    "questionNumber": 48,
                    "question": "Traduisez : 'Un client'.",
                    "answerOptions": [
                        {"text": "A customer", "isCorrect": True},
                        {"text": "A seller", "isCorrect": False},
                        {"text": "A supplier", "isCorrect": False},
                        {"text": "A partner", "isCorrect": False}
                    ],
                    "correction": "'Customer' ou 'Client'."
                },
                {
                    "questionNumber": 49,
                    "question": "Que signifie 'Full-time' ?",
                    "answerOptions": [
                        {"text": "Temps plein", "isCorrect": True},
                        {"text": "Temps partiel", "isCorrect": False},
                        {"text": "Heures supplémentaires", "isCorrect": False},
                        {"text": "Congés", "isCorrect": False}
                    ],
                    "correction": "Opposé à 'Part-time'."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment dit-on 'L'usine' ?",
                    "answerOptions": [
                        {"text": "The factory", "isCorrect": True},
                        {"text": "The shop", "isCorrect": False},
                        {"text": "The warehouse", "isCorrect": False},
                        {"text": "The laboratory", "isCorrect": False}
                    ],
                    "correction": "'Factory' ou 'Plant'."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel mot désigne un 'Apprenti' ?",
                    "answerOptions": [
                        {"text": "Apprentice", "isCorrect": True},
                        {"text": "Student", "isCorrect": False},
                        {"text": "Teacher", "isCorrect": False},
                        {"text": "Master", "isCorrect": False}
                    ],
                    "correction": "Le mot est très proche du français."
                },
                {
                    "questionNumber": 52,
                    "question": "Traduisez : 'Sécurité au travail'.",
                    "answerOptions": [
                        {"text": "Safety at work", "isCorrect": True},
                        {"text": "Security at work", "isCorrect": False},
                        {"text": "Health at work", "isCorrect": False},
                        {"text": "Danger at work", "isCorrect": False}
                    ],
                    "correction": "'Safety' désigne la sécurité physique/prévention."
                },
                {
                    "questionNumber": 53,
                    "question": "Que signifie 'To resign' ?",
                    "answerOptions": [
                        {"text": "Démissionner", "isCorrect": True},
                        {"text": "Signer à nouveau", "isCorrect": False},
                        {"text": "Vendre", "isCorrect": False},
                        {"text": "Acheter", "isCorrect": False}
                    ],
                    "correction": "Quitter son poste de sa propre volonté."
                },
                {
                    "questionNumber": 54,
                    "question": "Comment dit-on 'Un outil' ?",
                    "answerOptions": [
                        {"text": "A tool", "isCorrect": True},
                        {"text": "A machine", "isCorrect": False},
                        {"text": "A box", "isCorrect": False},
                        {"text": "A gear", "isCorrect": False}
                    ],
                    "correction": "'Tool' est le terme général."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel mot désigne la 'Retraite' ?",
                    "answerOptions": [
                        {"text": "Retirement", "isCorrect": True},
                        {"text": "Holidays", "isCorrect": False},
                        {"text": "Weekend", "isCorrect": False},
                        {"text": "Pause", "isCorrect": False}
                    ],
                    "correction": "Le verbe est 'to retire'."
                },
                {
                    "questionNumber": 56,
                    "question": "Traduisez : 'Compétences'.",
                    "answerOptions": [
                        {"text": "Skills", "isCorrect": True},
                        {"text": "Hobbies", "isCorrect": False},
                        {"text": "Studies", "isCorrect": False},
                        {"text": "Dreams", "isCorrect": False}
                    ],
                    "correction": "'Skills' désigne les capacités acquises."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment dit-on 'Gagner sa vie' ?",
                    "answerOptions": [
                        {"text": "To earn a living", "isCorrect": True},
                        {"text": "To win a living", "isCorrect": False},
                        {"text": "To make a life", "isCorrect": False},
                        {"text": "To pay a living", "isCorrect": False}
                    ],
                    "correction": "On utilise 'earn' pour le salaire mérité."
                },
                {
                    "questionNumber": 58,
                    "question": "Que signifie 'A warehouse' ?",
                    "answerOptions": [
                        {"text": "Un entrepôt", "isCorrect": True},
                        {"text": "Un magasin", "isCorrect": False},
                        {"text": "Une maison", "isCorrect": False},
                        {"text": "Un garage", "isCorrect": False}
                    ],
                    "correction": "Lieu de stockage des marchandises."
                },
                {
                    "questionNumber": 59,
                    "question": "Comment dit-on 'Heures supplémentaires' ?",
                    "answerOptions": [
                        {"text": "Overtime", "isCorrect": True},
                        {"text": "Extra hours", "isCorrect": False},
                        {"text": "More time", "isCorrect": False},
                        {"text": "Plus time", "isCorrect": False}
                    ],
                    "correction": "'Overtime' est le terme technique."
                },
                {
                    "questionNumber": 60,
                    "question": "Traduisez : 'Un CV'.",
                    "answerOptions": [
                        {"text": "A resume", "isCorrect": True},
                        {"text": "A letter", "isCorrect": False},
                        {"text": "A book", "isCorrect": False},
                        {"text": "A paper", "isCorrect": False}
                    ],
                    "correction": "'Resume' (US) ou 'CV' (UK)."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : VOYAGE, COMMERCE ET SERVICES (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : VOYAGE, COMMERCE ET SERVICES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Comment dit-on 'Un billet d'avion' ?",
                    "answerOptions": [
                        {"text": "A plane ticket", "isCorrect": True},
                        {"text": "A plane card", "isCorrect": False},
                        {"text": "A plane paper", "isCorrect": False},
                        {"text": "A plane book", "isCorrect": False}
                    ],
                    "correction": "'Ticket' s'utilise pour le transport."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel mot désigne 'L'addition' au restaurant ?",
                    "answerOptions": [
                        {"text": "The bill", "isCorrect": True},
                        {"text": "The addition", "isCorrect": False},
                        {"text": "The paper", "isCorrect": False},
                        {"text": "The price", "isCorrect": False}
                    ],
                    "correction": "'The bill' (UK) ou 'The check' (US)."
                },
                {
                    "questionNumber": 63,
                    "question": "Traduisez : 'Une chambre simple'.",
                    "answerOptions": [
                        {"text": "A single room", "isCorrect": True},
                        {"text": "A double room", "isCorrect": False},
                        {"text": "A one room", "isCorrect": False},
                        {"text": "A small room", "isCorrect": False}
                    ],
                    "correction": "'Single' vs 'Double'."
                },
                {
                    "questionNumber": 64,
                    "question": "Comment dit-on 'Combien ça coûte ?' ?",
                    "answerOptions": [
                        {"text": "How much is it?", "isCorrect": True},
                        {"text": "How many is it?", "isCorrect": False},
                        {"text": "How price is it?", "isCorrect": False},
                        {"text": "What cost is it?", "isCorrect": False}
                    ],
                    "correction": "On utilise 'How much' pour l'argent (indénombrable)."
                },
                {
                    "questionNumber": 65,
                    "question": "Que signifie 'To book' ?",
                    "answerOptions": [
                        {"text": "Réserver", "isCorrect": True},
                        {"text": "Lire", "isCorrect": False},
                        {"text": "Vendre", "isCorrect": False},
                        {"text": "Écrire", "isCorrect": False}
                    ],
                    "correction": "Réserver une chambre ou une table."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment dit-on 'Un magasin' ?",
                    "answerOptions": [
                        {"text": "A shop", "isCorrect": True},
                        {"text": "A storage", "isCorrect": False},
                        {"text": "A library", "isCorrect": False},
                        {"text": "A house", "isCorrect": False}
                    ],
                    "correction": "'Shop' ou 'Store'."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel mot désigne 'Les bagages' ?",
                    "answerOptions": [
                        {"text": "Luggage", "isCorrect": True},
                        {"text": "Bags", "isCorrect": True},
                        {"text": "Boxes", "isCorrect": False},
                        {"text": "Clothes", "isCorrect": False}
                    ],
                    "correction": "'Luggage' est indénombrable (ne prend pas de 's')."
                },
                {
                    "questionNumber": 68,
                    "question": "Traduisez : 'Service compris'.",
                    "answerOptions": [
                        {"text": "Service included", "isCorrect": True},
                        {"text": "Service with", "isCorrect": False},
                        {"text": "Service here", "isCorrect": False},
                        {"text": "Service free", "isCorrect": False}
                    ],
                    "correction": "Indique que le pourboire est déjà dans le prix."
                },
                {
                    "questionNumber": 69,
                    "question": "Que signifie 'Sold out' ?",
                    "answerOptions": [
                        {"text": "Épuisé (plus de stock)", "isCorrect": True},
                        {"text": "En solde", "isCorrect": False},
                        {"text": "Ouvert", "isCorrect": False},
                        {"text": "Vendre dehors", "isCorrect": False}
                    ],
                    "correction": "Tout a été vendu."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment dit-on 'La monnaie' (le reste à rendre) ?",
                    "answerOptions": [
                        {"text": "Change", "isCorrect": True},
                        {"text": "Money", "isCorrect": False},
                        {"text": "Coins", "isCorrect": False},
                        {"text": "Notes", "isCorrect": False}
                    ],
                    "correction": "'Keep the change' signifie gardez la monnaie."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel mot désigne 'Le menu' ?",
                    "answerOptions": [
                        {"text": "The menu", "isCorrect": True},
                        {"text": "The card", "isCorrect": False},
                        {"text": "The list", "isCorrect": False},
                        {"text": "The food", "isCorrect": False}
                    ],
                    "correction": "Mot transparent."
                },
                {
                    "questionNumber": 72,
                    "question": "Traduisez : 'Payer en espèces'.",
                    "answerOptions": [
                        {"text": "To pay in cash", "isCorrect": True},
                        {"text": "To pay with card", "isCorrect": False},
                        {"text": "To pay in paper", "isCorrect": False},
                        {"text": "To pay by check", "isCorrect": False}
                    ],
                    "correction": "'Cash' désigne l'argent liquide."
                },
                {
                    "questionNumber": 73,
                    "question": "Que signifie 'A receipt' ?",
                    "answerOptions": [
                        {"text": "Un ticket de caisse / reçu", "isCorrect": True},
                        {"text": "Une recette de cuisine", "isCorrect": False},
                        {"text": "Une lettre", "isCorrect": False},
                        {"text": "Un cadeau", "isCorrect": False}
                    ],
                    "correction": "Attention au faux-ami : recette se dit 'Recipe'."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment dit-on 'Ouvert' et 'Fermé' ?",
                    "answerOptions": [
                        {"text": "Open and Closed", "isCorrect": True},
                        {"text": "Start and Stop", "isCorrect": False},
                        {"text": "Begin and End", "isCorrect": False},
                        {"text": "Yes and No", "isCorrect": False}
                    ],
                    "correction": "Mots visibles sur les portes des magasins."
                },
                {
                    "questionNumber": 75,
                    "question": "Traduisez : 'Où se trouve la banque ?'.",
                    "answerOptions": [
                        {"text": "Where is the bank?", "isCorrect": True},
                        {"text": "What is the bank?", "isCorrect": False},
                        {"text": "When is the bank?", "isCorrect": False},
                        {"text": "Who is the bank?", "isCorrect": False}
                    ],
                    "correction": "Structure de base pour s'orienter."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel mot désigne 'Une remise / réduction' ?",
                    "answerOptions": [
                        {"text": "A discount", "isCorrect": True},
                        {"text": "A price", "isCorrect": False},
                        {"text": "A sale", "isCorrect": False},
                        {"text": "A gift", "isCorrect": False}
                    ],
                    "correction": "'Discount' ou 'Reduction'."
                },
                {
                    "questionNumber": 77,
                    "question": "Que signifie 'Arrivals' à l'aéroport ?",
                    "answerOptions": [
                        {"text": "Arrivées", "isCorrect": True},
                        {"text": "Départs", "isCorrect": False},
                        {"text": "Douane", "isCorrect": False},
                        {"text": "Sécurité", "isCorrect": False}
                    ],
                    "correction": "Opposé à 'Departures'."
                },
                {
                    "questionNumber": 78,
                    "question": "Comment dit-on 'Le centre-ville' ?",
                    "answerOptions": [
                        {"text": "The city center", "isCorrect": True},
                        {"text": "The downtown", "isCorrect": True},
                        {"text": "The middle city", "isCorrect": False},
                        {"text": "The town place", "isCorrect": False}
                    ],
                    "correction": "Les deux premières formes sont correctes."
                },
                {
                    "questionNumber": 79,
                    "question": "Traduisez : 'Un pourboire'.",
                    "answerOptions": [
                        {"text": "A tip", "isCorrect": True},
                        {"text": "A help", "isCorrect": False},
                        {"text": "A drink", "isCorrect": False},
                        {"text": "A coin", "isCorrect": False}
                    ],
                    "correction": "Le verbe est aussi 'to tip'."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment dit-on 'Cher' (prix élevé) ?",
                    "answerOptions": [
                        {"text": "Expensive", "isCorrect": True},
                        {"text": "Cheap", "isCorrect": False},
                        {"text": "Free", "isCorrect": False},
                        {"text": "Good", "isCorrect": False}
                    ],
                    "correction": "Opposé à 'Cheap' (bon marché)."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : CULTURE ET COMPRÉHENSION GLOBALE (Q81 à Q100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : CULTURE ET COMPRÉHENSION GLOBALE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la capitale du Royaume-Uni ?",
                    "answerOptions": [
                        {"text": "London", "isCorrect": True},
                        {"text": "New York", "isCorrect": False},
                        {"text": "Washington", "isCorrect": False},
                        {"text": "Dublin", "isCorrect": False}
                    ],
                    "correction": "Londres est le centre politique et financier du pays."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la monnaie utilisée aux États-Unis ?",
                    "answerOptions": [
                        {"text": "The Dollar", "isCorrect": True},
                        {"text": "The Pound", "isCorrect": False},
                        {"text": "The Euro", "isCorrect": False},
                        {"text": "The Yen", "isCorrect": False}
                    ],
                    "correction": "Le dollar américain ($)."
                },
                {
                    "questionNumber": 83,
                    "question": "Qui est le chef de l'État au Royaume-Uni ?",
                    "answerOptions": [
                        {"text": "The King / The Queen", "isCorrect": True},
                        {"text": "The President", "isCorrect": False},
                        {"text": "The Prime Minister", "isCorrect": False},
                        {"text": "The Mayor", "isCorrect": False}
                    ],
                    "correction": "Le Royaume-Uni est une monarchie constitutionnelle."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel pays ne parle pas anglais comme langue officielle ?",
                    "answerOptions": [
                        {"text": "Brazil", "isCorrect": True},
                        {"text": "Australia", "isCorrect": False},
                        {"text": "Canada", "isCorrect": False},
                        {"text": "Ireland", "isCorrect": False}
                    ],
                    "correction": "On y parle portugais."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment appelle-t-on le drapeau du Royaume-Uni ?",
                    "answerOptions": [
                        {"text": "The Union Jack", "isCorrect": True},
                        {"text": "The Stars and Stripes", "isCorrect": False},
                        {"text": "The Tricolour", "isCorrect": False},
                        {"text": "The Red Cross", "isCorrect": False}
                    ],
                    "correction": "Il combine les croix des protecteurs de l'Angleterre, de l'Écosse et de l'Irlande."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle ville est célèbre pour la statue de la Liberté ?",
                    "answerOptions": [
                        {"text": "New York", "isCorrect": True},
                        {"text": "Los Angeles", "isCorrect": False},
                        {"text": "Miami", "isCorrect": False},
                        {"text": "Chicago", "isCorrect": False}
                    ],
                    "correction": "Cadeau de la France aux États-Unis."
                },
                {
                    "questionNumber": 87,
                    "question": "Que signifie l'abréviation 'USA' ?",
                    "answerOptions": [
                        {"text": "United States of America", "isCorrect": True},
                        {"text": "United States of Africa", "isCorrect": False},
                        {"text": "Under Sea Area", "isCorrect": False},
                        {"text": "United Systems of America", "isCorrect": False}
                    ],
                    "correction": "Le pays composé de 50 États."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel sport est très populaire aux États-Unis ?",
                    "answerOptions": [
                        {"text": "Baseball", "isCorrect": True},
                        {"text": "Pétanque", "isCorrect": False},
                        {"text": "Judo", "isCorrect": False},
                        {"text": "Cricket", "isCorrect": False}
                    ],
                    "correction": "Sport national historique américain."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la boisson chaude préférée des Britanniques ?",
                    "answerOptions": [
                        {"text": "Tea", "isCorrect": True},
                        {"text": "Coffee", "isCorrect": False},
                        {"text": "Wine", "isCorrect": False},
                        {"text": "Beer", "isCorrect": False}
                    ],
                    "correction": "Tradition du 'five o'clock tea'."
                },
                {
                    "questionNumber": 90,
                    "question": "Comment s'appelle la célèbre tour avec une horloge à Londres ?",
                    "answerOptions": [
                        {"text": "Big Ben", "isCorrect": True},
                        {"text": "The Eiffel Tower", "isCorrect": False},
                        {"text": "The Empire State Building", "isCorrect": False},
                        {"text": "The White House", "isCorrect": False}
                    ],
                    "correction": "C'est le nom de la cloche à l'intérieur de la tour du Parlement."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle fête est célébrée le 31 octobre ?",
                    "answerOptions": [
                        {"text": "Halloween", "isCorrect": True},
                        {"text": "Christmas", "isCorrect": False},
                        {"text": "Easter", "isCorrect": False},
                        {"text": "Thanksgiving", "isCorrect": False}
                    ],
                    "correction": "Fête d'origine celtique très populaire dans le monde anglophone."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est l'équivalent de 'Bon appétit' ?",
                    "answerOptions": [
                        {"text": "Enjoy your meal", "isCorrect": True},
                        {"text": "Good eat", "isCorrect": False},
                        {"text": "Nice food", "isCorrect": False},
                        {"text": "Happy lunch", "isCorrect": False}
                    ],
                    "correction": "Formule polie au début du repas."
                },
                {
                    "questionNumber": 93,
                    "question": "Que signifie 'ASAP' ?",
                    "answerOptions": [
                        {"text": "As Soon As Possible (Dès que possible)", "isCorrect": True},
                        {"text": "As Slow As Possible", "isCorrect": False},
                        {"text": "Always Send A Paper", "isCorrect": False},
                        {"text": "After Some Apples Please", "isCorrect": False}
                    ],
                    "correction": "Acronyme très utilisé dans le monde du travail."
                },
                {
                    "questionNumber": 94,
                    "question": "Traduisez 'Faire la queue' :",
                    "answerOptions": [
                        {"text": "To stand in line / To queue", "isCorrect": True},
                        {"text": "To wait the bus", "isCorrect": False},
                        {"text": "To make the shop", "isCorrect": False},
                        {"text": "To walk fast", "isCorrect": False}
                    ],
                    "correction": "Indispensable dans la culture britannique."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel mot désigne un 'Leurre' ou une 'Fausse information' ?",
                    "answerOptions": [
                        {"text": "Fake", "isCorrect": True},
                        {"text": "True", "isCorrect": False},
                        {"text": "Real", "isCorrect": False},
                        {"text": "Good", "isCorrect": False}
                    ],
                    "correction": "Mot devenu courant avec les 'Fake News'."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment dit-on 'Devant l'hôtel' ?",
                    "answerOptions": [
                        {"text": "In front of the hotel", "isCorrect": True},
                        {"text": "Behind the hotel", "isCorrect": False},
                        {"text": "Front of the hotel", "isCorrect": False},
                        {"text": "Before the hotel", "isCorrect": False}
                    ],
                    "correction": "Locution prépositive de lieu."
                },
                {
                    "questionNumber": 97,
                    "question": "Choisissez le comparatif correct : 'This machine is ______ than the old one.'",
                    "answerOptions": [
                        {"text": "faster", "isCorrect": True},
                        {"text": "more fast", "isCorrect": False},
                        {"text": "fastest", "isCorrect": False},
                        {"text": "as fast", "isCorrect": False}
                    ],
                    "correction": "Pour les adjectifs courts, on ajoute -er."
                },
                {
                    "questionNumber": 98,
                    "question": "Choisissez le superlatif correct : 'It is the ______ hotel in the city.'",
                    "answerOptions": [
                        {"text": "most expensive", "isCorrect": True},
                        {"text": "more expensive", "isCorrect": False},
                        {"text": "expensivest", "isCorrect": False},
                        {"text": "expensive", "isCorrect": False}
                    ],
                    "correction": "Pour les adjectifs longs, on utilise 'the most'."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel mot interrogatif utilise-t-on pour demander 'Pourquoi' ?",
                    "answerOptions": [
                        {"text": "Why", "isCorrect": True},
                        {"text": "What", "isCorrect": False},
                        {"text": "Which", "isCorrect": False},
                        {"text": "Who", "isCorrect": False}
                    ],
                    "correction": "Interroge sur la cause."
                },
                {
                    "questionNumber": 100,
                    "question": "Traduisez 'Je peux vous aider ?' :",
                    "answerOptions": [
                        {"text": "Can I help you?", "isCorrect": True},
                        {"text": "Do I help you?", "isCorrect": False},
                        {"text": "Am I help you?", "isCorrect": False},
                        {"text": "Will I help you?", "isCorrect": False}
                    ],
                    "correction": "Formule de base du service client."
                }
            ]
        }
    }
}