quiz_data = {
    "title": "Quiz Français - Niveau CAP (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MAÎTRISE DE LA LANGUE (GRAMMAIRE & ORTHOGRAPHE) (Q1 à Q20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : MAÎTRISE DE LA LANGUE (GRAMMAIRE & ORTHOGRAPHE)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la terminaison correcte du verbe dans la phrase : 'Les marchandises que nous avons...' ?",
                    "answerOptions": [
                        {"text": "reçues", "isCorrect": True},
                        {"text": "reçu", "isCorrect": False},
                        {"text": "reçus", "isCorrect": False},
                        {"text": "reçue", "isCorrect": False}
                    ],
                    "correction": "Avec l'auxiliaire avoir, le participe passé s'accorde avec le Complément d'Objet Direct (COD) si celui-ci est placé avant le verbe. Ici, le COD 'que' remplace 'Les marchandises' (féminin pluriel), donc 'reçues'."
                },
                {
                    "questionNumber": 2,
                    "question": "Complétez la phrase suivante : 'Je vous transmets les documents ci-...' ?",
                    "answerOptions": [
                        {"text": "joints", "isCorrect": True},
                        {"text": "jointes", "isCorrect": False},
                        {"text": "joindre", "isCorrect": False},
                        {"text": "joint", "isCorrect": False}
                    ],
                    "correction": "L'adjectif 'joint' s'accorde en genre et en nombre avec le nom qu'il qualifie ('les documents', masculin pluriel) lorsqu'il est placé après ce nom."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel mot complète correctement cette phrase : 'Ils sont arrivés ... en retard.' ?",
                    "answerOptions": [
                        {"text": "tous", "isCorrect": True},
                        {"text": "tout", "isCorrect": False},
                        {"text": "toux", "isCorrect": False},
                        {"text": "toutes", "isCorrect": False}
                    ],
                    "correction": "Ici, 'tous' est un pronom indéfini qui remplace 'ils' (masculin pluriel). On doit entendre le 's' final."
                },
                {
                    "questionNumber": 4,
                    "question": "Trouvez l'intrus parmi ces homonymes :",
                    "answerOptions": [
                        {"text": "vers (direction)", "isCorrect": True},
                        {"text": "vert (couleur)", "isCorrect": False},
                        {"text": "ver (animal)", "isCorrect": False},
                        {"text": "verre (matière)", "isCorrect": False}
                    ],
                    "correction": "Tous ces mots se prononcent de la même façon mais ont des sens et des orthographes différents (homonymes)."
                },
                {
                    "questionNumber": 5,
                    "question": "Dans la phrase 'Le client téléphone au magasin', quelle est la fonction de 'au magasin' ?",
                    "answerOptions": [
                        {"text": "COI (Complément d'Objet Indirect)", "isCorrect": True},
                        {"text": "COD (Complément d'Objet Direct)", "isCorrect": False},
                        {"text": "Sujet", "isCorrect": False},
                        {"text": "Attribut du sujet", "isCorrect": False}
                    ],
                    "correction": "On pose la question 'à qui / à quoi ?' après le verbe. Téléphoner À quelque chose : c'est un COI."
                },
                {
                    "questionNumber": 6,
                    "question": "Comment écrit-on le nombre 80 ?",
                    "answerOptions": [
                        {"text": "quatre-vingts", "isCorrect": True},
                        {"text": "quatre-vingt", "isCorrect": False},
                        {"text": "quatres-vingts", "isCorrect": False},
                        {"text": "quatre-vins", "isCorrect": False}
                    ],
                    "correction": "'Vingt' prend un 's' quand il est multiplié et qu'il n'y a rien après. Exemple : 80 (quatre-vingts) mais 82 (quatre-vingt-deux)."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est le pluriel de 'un travail' ?",
                    "answerOptions": [
                        {"text": "des travaux", "isCorrect": True},
                        {"text": "des travails", "isCorrect": False},
                        {"text": "des travail", "isCorrect": False},
                        {"text": "des travaus", "isCorrect": False}
                    ],
                    "correction": "Les noms se terminant en -ail font généralement leur pluriel en -ails, mais 'travail' est une exception qui se transforme en -aux."
                },
                {
                    "questionNumber": 8,
                    "question": "Dans 'Il range ses outils', quelle est la nature de 'ses' ?",
                    "answerOptions": [
                        {"text": "Déterminant possessif", "isCorrect": True},
                        {"text": "Déterminant démonstratif", "isCorrect": False},
                        {"text": "Pronom personnel", "isCorrect": False},
                        {"text": "Verbe être", "isCorrect": False}
                    ],
                    "correction": "'Ses' indique l'appartenance (les outils à lui). À ne pas confondre avec 'ces' (ceux-là)."
                },
                {
                    "questionNumber": 9,
                    "question": "Choisissez la forme correcte : 'Elle ... partie tôt ce matin.'",
                    "answerOptions": [
                        {"text": "est", "isCorrect": True},
                        {"text": "es", "isCorrect": False},
                        {"text": "et", "isCorrect": False},
                        {"text": "ai", "isCorrect": False}
                    ],
                    "correction": "Il s'agit de l'auxiliaire être au présent de l'indicatif à la 3ème personne du singulier."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la forme verbale correcte du verbe 'faire' à la 1ère personne du pluriel du présent ?",
                    "answerOptions": [
                        {"text": "nous faisons", "isCorrect": True},
                        {"text": "nous fesons", "isCorrect": False},
                        {"text": "nous faites", "isCorrect": False},
                        {"text": "nous faissons", "isCorrect": False}
                    ],
                    "correction": "Le verbe 'faire' est irrégulier. Bien qu'on entende le son 'eu', on écrit 'ai' : nous faisons."
                },
                {
                    "questionNumber": 11,
                    "question": "Complétez : 'Ils ... leurs devoirs.'",
                    "answerOptions": [
                        {"text": "ont", "isCorrect": True},
                        {"text": "on", "isCorrect": False},
                        {"text": "font", "isCorrect": False},
                        {"text": "sont", "isCorrect": False}
                    ],
                    "correction": "'Ont' est le verbe avoir. On peut le remplacer par 'avaient'. 'On' est un pronom personnel."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment appelle-t-on le mot qui qualifie un nom ?",
                    "answerOptions": [
                        {"text": "Un adjectif", "isCorrect": True},
                        {"text": "Un verbe", "isCorrect": False},
                        {"text": "Un adverbe", "isCorrect": False},
                        {"text": "Une préposition", "isCorrect": False}
                    ],
                    "correction": "L'adjectif qualificatif donne une précision sur le nom (ex: une table 'ronde')."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle phrase est correctement ponctuée ?",
                    "answerOptions": [
                        {"text": "Bonjour, comment allez-vous ?", "isCorrect": True},
                        {"text": "Bonjour comment allez vous !", "isCorrect": False},
                        {"text": "Bonjour. comment allez vous ?", "isCorrect": False},
                        {"text": "Bonjour comment, allez vous.", "isCorrect": False}
                    ],
                    "correction": "Une question se termine par un point d'interrogation et commence par une majuscule."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le contraire (antonyme) de 'rapide' ?",
                    "answerOptions": [
                        {"text": "lent", "isCorrect": True},
                        {"text": "vite", "isCorrect": False},
                        {"text": "pressé", "isCorrect": False},
                        {"text": "actif", "isCorrect": False}
                    ],
                    "correction": "Un antonyme est un mot de sens opposé."
                },
                {
                    "questionNumber": 15,
                    "question": "Mettez au pluriel : 'Le petit enfant'.",
                    "answerOptions": [
                        {"text": "Les petits enfants", "isCorrect": True},
                        {"text": "Les petit enfants", "isCorrect": False},
                        {"text": "Les petits enfant", "isCorrect": False},
                        {"text": "Des petits enfants", "isCorrect": False}
                    ],
                    "correction": "Tous les éléments du groupe nominal (article, adjectif, nom) s'accordent en nombre."
                },
                {
                    "questionNumber": 16,
                    "question": "Dans 'Il mange une pomme', quel est le COD ?",
                    "answerOptions": [
                        {"text": "une pomme", "isCorrect": True},
                        {"text": "Il", "isCorrect": False},
                        {"text": "mange", "isCorrect": False},
                        {"text": "une", "isCorrect": False}
                    ],
                    "correction": "On trouve le COD en posant la question 'Quoi ?' ou 'Qui ?' après le verbe. Il mange quoi ? Une pomme."
                },
                {
                    "questionNumber": 17,
                    "question": "Comment s'accorde le verbe avec le sujet 'La foule' ?",
                    "answerOptions": [
                        {"text": "au singulier (elle)", "isCorrect": True},
                        {"text": "au pluriel (ils)", "isCorrect": False},
                        {"text": "au masculin", "isCorrect": False},
                        {"text": "selon l'envie", "isCorrect": False}
                    ],
                    "correction": "Même s'il désigne plusieurs personnes, 'la foule' est un nom collectif au singulier."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est l'orthographe correcte ?",
                    "answerOptions": [
                        {"text": "développement", "isCorrect": True},
                        {"text": "dévellopement", "isCorrect": False},
                        {"text": "dévelopement", "isCorrect": False},
                        {"text": "dévéloppement", "isCorrect": False}
                    ],
                    "correction": "Développement s'écrit avec deux 'p' et un seul 'l'."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le rôle du point d'exclamation ?",
                    "answerOptions": [
                        {"text": "Exprimer un sentiment fort (joie, colère, surprise)", "isCorrect": True},
                        {"text": "Poser une question", "isCorrect": False},
                        {"text": "Terminer une phrase simple", "isCorrect": False},
                        {"text": "Faire une pause moyenne", "isCorrect": False}
                    ],
                    "correction": "Il sert à marquer l'émotion ou l'ordre."
                },
                {
                    "questionNumber": 20,
                    "question": "Trouvez le synonyme de 'boulot'.",
                    "answerOptions": [
                        {"text": "travail", "isCorrect": True},
                        {"text": "vacances", "isCorrect": False},
                        {"text": "repos", "isCorrect": False},
                        {"text": "jeu", "isCorrect": False}
                    ],
                    "correction": "Un synonyme est un mot qui a le même sens. 'Boulot' est le registre familier de 'travail'."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : L'ÉCRIT PROFESSIONNEL ET LA COMMUNICATION (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : L'ÉCRIT PROFESSIONNEL ET LA COMMUNICATION",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel élément est indispensable dans l'en-tête d'une lettre professionnelle ?",
                    "answerOptions": [
                        {"text": "Les coordonnées de l'expéditeur et du destinataire", "isCorrect": True},
                        {"text": "La photo de l'expéditeur", "isCorrect": False},
                        {"text": "Le menu de la cantine", "isCorrect": False},
                        {"text": "L'âge de l'employeur", "isCorrect": False}
                    ],
                    "correction": "Il est crucial d'identifier clairement qui écrit à qui pour le suivi du courrier."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment appelle-t-on le résumé d'un parcours professionnel envoyé à un employeur ?",
                    "answerOptions": [
                        {"text": "Un CV (Curriculum Vitae)", "isCorrect": True},
                        {"text": "Un carnet de notes", "isCorrect": False},
                        {"text": "Une facture", "isCorrect": False},
                        {"text": "Un diplôme", "isCorrect": False}
                    ],
                    "correction": "Le CV présente l'état civil, les diplômes et les expériences du candidat."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle formule de politesse est adaptée pour terminer une lettre de motivation ?",
                    "answerOptions": [
                        {"text": "Je vous prie d'agréer, Monsieur, l'expression de mes salutations distinguées", "isCorrect": True},
                        {"text": "Salut, à bientôt", "isCorrect": False},
                        {"text": "Bisous", "isCorrect": False},
                        {"text": "Merci d'avance", "isCorrect": False}
                    ],
                    "correction": "L'écrit professionnel exige des formules codifiées et respectueuses."
                },
                {
                    "questionNumber": 24,
                    "question": "Que signifie l'abréviation 'Objet' dans un mail ?",
                    "answerOptions": [
                        {"text": "Le titre ou le sujet principal du message", "isCorrect": True},
                        {"text": "La pièce jointe", "isCorrect": False},
                        {"text": "Le nom de l'expéditeur", "isCorrect": False},
                        {"text": "La signature", "isCorrect": False}
                    ],
                    "correction": "L'objet permet au destinataire de comprendre immédiatement de quoi parle le mail."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel document récapitule les points abordés lors d'une réunion ?",
                    "answerOptions": [
                        {"text": "Le compte-rendu", "isCorrect": True},
                        {"text": "Le bon de commande", "isCorrect": False},
                        {"text": "Le devis", "isCorrect": False},
                        {"text": "La fiche de stock", "isCorrect": False}
                    ],
                    "correction": "Le compte-rendu sert de mémoire et de trace officielle des décisions prises."
                },
                {
                    "questionNumber": 26,
                    "question": "Dans un CV, que désigne la rubrique 'Compétences' ?",
                    "answerOptions": [
                        {"text": "Le savoir-faire et la maîtrise d'outils ou de logiciels", "isCorrect": True},
                        {"text": "L'adresse du domicile", "isCorrect": False},
                        {"text": "Les noms des anciens professeurs", "isCorrect": False},
                        {"text": "La liste des films préférés", "isCorrect": False}
                    ],
                    "correction": "Les compétences montrent ce que vous êtes capable de faire concrètement au travail."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est l'utilité d'une lettre de motivation ?",
                    "answerOptions": [
                        {"text": "Expliquer pourquoi on veut le poste et ce qu'on peut apporter", "isCorrect": True},
                        {"text": "Raconter sa vie privée", "isCorrect": False},
                        {"text": "Demander une augmentation de salaire", "isCorrect": False},
                        {"text": "Critiquer son ancien patron", "isCorrect": False}
                    ],
                    "correction": "Elle complète le CV en montrant l'intérêt du candidat pour l'entreprise."
                },
                {
                    "questionNumber": 28,
                    "question": "Que signifie 'PJ' dans un email ?",
                    "answerOptions": [
                        {"text": "Pièce Jointe", "isCorrect": True},
                        {"text": "Petit Journal", "isCorrect": False},
                        {"text": "Passage Journalier", "isCorrect": False},
                        {"text": "Prénom du Junior", "isCorrect": False}
                    ],
                    "correction": "C'est un document (PDF, photo, tableur) envoyé en plus du message texte."
                },
                {
                    "questionNumber": 29,
                    "question": "Comment doit être la présentation d'un écrit professionnel ?",
                    "answerOptions": [
                        {"text": "Claire, aérée et sans fautes", "isCorrect": True},
                        {"text": "Colorée avec beaucoup d'images", "isCorrect": False},
                        {"text": "Écrite en tout petit pour gagner de la place", "isCorrect": False},
                        {"text": "Manuscrite au crayon à papier", "isCorrect": False}
                    ],
                    "correction": "La mise en page reflète le sérieux et le professionnalisme de l'auteur."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le but d'un rapport de stage ?",
                    "answerOptions": [
                        {"text": "Décrire les missions effectuées et le fonctionnement de l'entreprise", "isCorrect": True},
                        {"text": "Avoir une bonne note sans travailler", "isCorrect": False},
                        {"text": "Se moquer des collègues", "isCorrect": False},
                        {"text": "Lister les restaurants à côté du stage", "isCorrect": False}
                    ],
                    "correction": "C'est un bilan de l'expérience vécue en milieu professionnel."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment s'appelle l'ensemble des règles de politesse sur Internet ?",
                    "answerOptions": [
                        {"text": "La nétiquette", "isCorrect": True},
                        {"text": "Le pare-feu", "isCorrect": False},
                        {"text": "Le clavier", "isCorrect": False},
                        {"text": "Le Wi-Fi", "isCorrect": False}
                    ],
                    "correction": "Cela inclut le fait de ne pas écrire en majuscules (qui signifie crier)."
                },
                {
                    "questionNumber": 32,
                    "question": "Que contient une 'offre d'emploi' ?",
                    "answerOptions": [
                        {"text": "La description du poste et le profil recherché", "isCorrect": True},
                        {"text": "La liste des clients du magasin", "isCorrect": False},
                        {"text": "Les comptes bancaires de l'entreprise", "isCorrect": False},
                        {"text": "L'horoscope de la semaine", "isCorrect": False}
                    ],
                    "correction": "L'offre permet au candidat de savoir s'il correspond au besoin de l'entreprise."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la fonction d'une signature en bas d'un mail ?",
                    "answerOptions": [
                        {"text": "Donner ses coordonnées directes (nom, poste, téléphone)", "isCorrect": True},
                        {"text": "Faire joli", "isCorrect": False},
                        {"text": "Cacher les fautes", "isCorrect": False},
                        {"text": "Finir le mail par une blague", "isCorrect": False}
                    ],
                    "correction": "Elle permet au destinataire de vous recontacter facilement."
                },
                {
                    "questionNumber": 34,
                    "question": "Pourquoi faut-il relire un message avant de l'envoyer ?",
                    "answerOptions": [
                        {"text": "Pour corriger les fautes et vérifier la clarté", "isCorrect": True},
                        {"text": "Pour perdre du temps", "isCorrect": False},
                        {"text": "Pour changer la date", "isCorrect": False},
                        {"text": "Parce que c'est obligatoire par la loi", "isCorrect": False}
                    ],
                    "correction": "Un écrit sans fautes est plus crédible et mieux compris."
                },
                {
                    "questionNumber": 35,
                    "question": "Qu'est-ce qu'une consigne de sécurité ?",
                    "answerOptions": [
                        {"text": "Une instruction à suivre pour éviter les accidents", "isCorrect": True},
                        {"text": "Une suggestion facultative", "isCorrect": False},
                        {"text": "Le menu de la cantine", "isCorrect": False},
                        {"text": "Une publicité pour des chaussures", "isCorrect": False}
                    ],
                    "correction": "Le respect des consignes est obligatoire dans le cadre du travail."
                },
                {
                    "questionNumber": 36,
                    "question": "Dans une argumentation, qu'est-ce qu'un exemple ?",
                    "answerOptions": [
                        {"text": "Un fait concret qui illustre une idée", "isCorrect": True},
                        {"text": "Une opinion personnelle", "isCorrect": False},
                        {"text": "La conclusion du texte", "isCorrect": False},
                        {"text": "Un mot difficile", "isCorrect": False}
                    ],
                    "correction": "L'exemple rend l'argument plus clair et plus convaincant."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel ton est préférable lors d'un entretien d'embauche ?",
                    "answerOptions": [
                        {"text": "Professionnel, motivé et poli", "isCorrect": True},
                        {"text": "Familier et détendu", "isCorrect": False},
                        {"text": "Agressif pour montrer sa force", "isCorrect": False},
                        {"text": "Timide et silencieux", "isCorrect": False}
                    ],
                    "correction": "Il faut montrer que l'on sait s'adapter aux codes de l'entreprise."
                },
                {
                    "questionNumber": 38,
                    "question": "Que signifie 'récapituler' ?",
                    "answerOptions": [
                        {"text": "Reprendre les points essentiels en résumé", "isCorrect": True},
                        {"text": "Tout recommencer au début", "isCorrect": False},
                        {"text": "Changer d'avis", "isCorrect": False},
                        {"text": "Arrêter de parler", "isCorrect": False}
                    ],
                    "correction": "La récapitulation aide à la mémorisation et à la validation d'un accord."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel document liste les articles achetés et leur prix total ?",
                    "answerOptions": [
                        {"text": "La facture", "isCorrect": True},
                        {"text": "La lettre de motivation", "isCorrect": False},
                        {"text": "Le dictionnaire", "isCorrect": False},
                        {"text": "Le CV", "isCorrect": False}
                    ],
                    "correction": "La facture est un document comptable et commercial obligatoire."
                },
                {
                    "questionNumber": 40,
                    "question": "Que désigne la communication verbale ?",
                    "answerOptions": [
                        {"text": "Les paroles et le contenu du discours", "isCorrect": True},
                        {"text": "Les gestes et la posture", "isCorrect": False},
                        {"text": "Les vêtements portés", "isCorrect": False},
                        {"text": "Le silence", "isCorrect": False}
                    ],
                    "correction": "Elle s'oppose à la communication non-verbale (langage du corps)."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : LECTURE ET COMPRÉHENSION DE TEXTE (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : LECTURE ET COMPRÉHENSION DE TEXTE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Qu'est-ce qu'un texte 'informatif' ?",
                    "answerOptions": [
                        {"text": "Un texte qui donne des explications ou des faits", "isCorrect": True},
                        {"text": "Une poésie sentimentale", "isCorrect": False},
                        {"text": "Une recette de cuisine imaginaire", "isCorrect": False},
                        {"text": "Un texte qui raconte une histoire inventée", "isCorrect": False}
                    ],
                    "correction": "Le but est de transmettre un savoir de manière objective (ex: article encyclopédique)."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le but d'un texte 'argumentatif' ?",
                    "answerOptions": [
                        {"text": "Convaincre le lecteur de partager un point de vue", "isCorrect": True},
                        {"text": "Faire rire", "isCorrect": False},
                        {"text": "Donner la météo", "isCorrect": False},
                        {"text": "Raconter un voyage", "isCorrect": False}
                    ],
                    "correction": "L'auteur utilise des arguments et des exemples pour défendre une thèse."
                },
                {
                    "questionNumber": 43,
                    "question": "Comment appelle-t-on le personnage principal d'un roman ?",
                    "answerOptions": [
                        {"text": "Le protagoniste", "isCorrect": True},
                        {"text": "L'antagoniste", "isCorrect": False},
                        {"text": "Le figurant", "isCorrect": False},
                        {"text": "L'auteur", "isCorrect": False}
                    ],
                    "correction": "C'est le personnage autour duquel l'action se construit."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la définition d'un 'synonyme' ?",
                    "answerOptions": [
                        {"text": "Un mot qui a presque le même sens qu'un autre", "isCorrect": True},
                        {"text": "Un mot qui se prononce de la même façon", "isCorrect": False},
                        {"text": "Le contraire d'un mot", "isCorrect": False},
                        {"text": "Un mot avec une seule lettre", "isCorrect": False}
                    ],
                    "correction": "Utiliser des synonymes permet d'éviter les répétitions dans un texte."
                },
                {
                    "questionNumber": 45,
                    "question": "Que signifie 'explicite' ?",
                    "answerOptions": [
                        {"text": "Ce qui est écrit clairement et directement", "isCorrect": True},
                        {"text": "Ce qui est caché ou sous-entendu", "isCorrect": False},
                        {"text": "Ce qui est faux", "isCorrect": False},
                        {"text": "Un mot très compliqué", "isCorrect": False}
                    ],
                    "correction": "L'information explicite ne nécessite pas d'interprétation."
                },
                {
                    "questionNumber": 46,
                    "question": "Qu'est-ce qu'une 'fiction' ?",
                    "answerOptions": [
                        {"text": "Une histoire issue de l'imagination", "isCorrect": True},
                        {"text": "Un documentaire scientifique", "isCorrect": False},
                        {"text": "Un dictionnaire", "isCorrect": False},
                        {"text": "Une facture réelle", "isCorrect": False}
                    ],
                    "correction": "La fiction s'oppose à la réalité (roman, conte, film)."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le rôle d'un 'titre' ?",
                    "answerOptions": [
                        {"text": "Indiquer le sujet et donner envie de lire", "isCorrect": True},
                        {"text": "Cacher le contenu", "isCorrect": False},
                        {"text": "Donner le nom de l'imprimeur", "isCorrect": False},
                        {"text": "Finir le texte", "isCorrect": False}
                    ],
                    "correction": "Le titre est le premier contact entre le lecteur et le texte."
                },
                {
                    "questionNumber": 48,
                    "question": "Que signifie le mot 'implicite' ?",
                    "answerOptions": [
                        {"text": "Ce qui est sous-entendu, qu'il faut deviner", "isCorrect": True},
                        {"text": "Ce qui est écrit en gras", "isCorrect": False},
                        {"text": "Ce qui est sans importance", "isCorrect": False},
                        {"text": "Ce qui est écrit à la fin", "isCorrect": False}
                    ],
                    "correction": "Il faut lire 'entre les lignes' pour comprendre l'implicite."
                },
                {
                    "questionNumber": 49,
                    "question": "Comment appelle-t-on le découpage d'un poème ?",
                    "answerOptions": [
                        {"text": "Strophes et vers", "isCorrect": True},
                        {"text": "Paragraphes et phrases", "isCorrect": False},
                        {"text": "Chapitres et pages", "isCorrect": False},
                        {"text": "Articles et colonnes", "isCorrect": False}
                    ],
                    "correction": "Une strophe est un groupe de vers (lignes)."
                },
                {
                    "questionNumber": 50,
                    "question": "Dans un dictionnaire, à quoi sert l'étymologie ?",
                    "answerOptions": [
                        {"text": "Donner l'origine historique du mot", "isCorrect": True},
                        {"text": "Apprendre à prononcer", "isCorrect": False},
                        {"text": "Donner le pluriel", "isCorrect": False},
                        {"text": "Vérifier l'orthographe uniquement", "isCorrect": False}
                    ],
                    "correction": "L'étymologie explique souvent le sens actuel d'un mot par ses racines latines ou grecques."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la définition d'un récit 'chronologique' ?",
                    "answerOptions": [
                        {"text": "Qui suit l'ordre du temps", "isCorrect": True},
                        {"text": "Qui mélange les époques", "isCorrect": False},
                        {"text": "Qui parle uniquement du futur", "isCorrect": False},
                        {"text": "Qui n'a pas de date", "isCorrect": False}
                    ],
                    "correction": "L'action avance du passé vers le présent ou le futur sans retours en arrière."
                },
                {
                    "questionNumber": 52,
                    "question": "Qu'est-ce qu'une biographie ?",
                    "answerOptions": [
                        {"text": "Le récit de la vie d'une personne", "isCorrect": True},
                        {"text": "Un livre sur les plantes", "isCorrect": False},
                        {"text": "Un livre de géographie", "isCorrect": False},
                        {"text": "Une règle de vie", "isCorrect": False}
                    ],
                    "correction": "Si l'auteur raconte sa propre vie, c'est une autobiographie."
                },
                {
                    "questionNumber": 53,
                    "question": "Que désigne le mot 'vocabulaire' ?",
                    "answerOptions": [
                        {"text": "L'ensemble des mots connus et utilisés", "isCorrect": True},
                        {"text": "La manière de marcher", "isCorrect": False},
                        {"text": "Le nom des outils du bâtiment", "isCorrect": False},
                        {"text": "Les fautes de français", "isCorrect": False}
                    ],
                    "correction": "Avoir un vocabulaire riche permet de s'exprimer avec précision."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le rôle des mots de liaison (ex: mais, donc, alors) ?",
                    "answerOptions": [
                        {"text": "Relier les idées entre elles logiquement", "isCorrect": True},
                        {"text": "Séparer les mots", "isCorrect": False},
                        {"text": "Remplacer le point", "isCorrect": False},
                        {"text": "Rendre le texte plus long", "isCorrect": False}
                    ],
                    "correction": "On les appelle aussi connecteurs logiques."
                },
                {
                    "questionNumber": 55,
                    "question": "Qu'est-ce qu'une 'métaphore' ?",
                    "answerOptions": [
                        {"text": "Une image qui compare sans utiliser de mot outil (ex: comme)", "isCorrect": True},
                        {"text": "Une question sans réponse", "isCorrect": False},
                        {"text": "Une liste de noms", "isCorrect": False},
                        {"text": "Un type de dictionnaire", "isCorrect": False}
                    ],
                    "correction": "Exemple : 'Cet homme est un lion' (il est courageux)."
                },
                {
                    "questionNumber": 56,
                    "question": "Trouvez le mot qui n'est pas dans le champ lexical de la mer.",
                    "answerOptions": [
                        {"text": "Forêt", "isCorrect": True},
                        {"text": "Bateau", "isCorrect": False},
                        {"text": "Vague", "isCorrect": False},
                        {"text": "Poisson", "isCorrect": False}
                    ],
                    "correction": "Le champ lexical regroupe les mots se rapportant à un même thème."
                },
                {
                    "questionNumber": 57,
                    "question": "Que signifie résumer un texte ?",
                    "answerOptions": [
                        {"text": "Dire l'essentiel en beaucoup moins de mots", "isCorrect": True},
                        {"text": "Le recopier mot pour mot", "isCorrect": False},
                        {"text": "Changer toutes les phrases", "isCorrect": False},
                        {"text": "Le traduire en anglais", "isCorrect": False}
                    ],
                    "correction": "Un bon résumé garde les informations clés et la structure du texte."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle est la définition d'un dialogue ?",
                    "answerOptions": [
                        {"text": "Un échange de paroles entre deux ou plusieurs personnes", "isCorrect": True},
                        {"text": "Une personne qui parle toute seule", "isCorrect": False},
                        {"text": "Un texte écrit en tout petit", "isCorrect": False},
                        {"text": "Une musique sans paroles", "isCorrect": False}
                    ],
                    "correction": "Dans un texte, le dialogue est souvent marqué par des guillemets ou des tirets."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le but d'un dictionnaire ?",
                    "answerOptions": [
                        {"text": "Donner la définition et l'orthographe des mots", "isCorrect": True},
                        {"text": "Raconter une histoire", "isCorrect": False},
                        {"text": "Lister les numéros de téléphone", "isCorrect": False},
                        {"text": "Donner les résultats sportifs", "isCorrect": False}
                    ],
                    "correction": "C'est un ouvrage de référence pour la langue."
                },
                {
                    "questionNumber": 60,
                    "question": "Qu'est-ce qu'une illustration dans un livre ?",
                    "answerOptions": [
                        {"text": "Une image ou un dessin qui accompagne le texte", "isCorrect": True},
                        {"text": "Le nom de l'auteur", "isCorrect": False},
                        {"text": "La dernière page", "isCorrect": False},
                        {"text": "Une erreur d'impression", "isCorrect": False}
                    ],
                    "correction": "L'image aide souvent à mieux comprendre ou imaginer le texte."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : ANALYSE DE L'IMAGE ET MÉDIAS (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ANALYSE DE L'IMAGE ET MÉDIAS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Comment appelle-t-on le texte explicatif situé sous une image ?",
                    "answerOptions": [
                        {"text": "La légende", "isCorrect": True},
                        {"text": "La bulle", "isCorrect": False},
                        {"text": "L'en-tête", "isCorrect": False},
                        {"text": "La signature", "isCorrect": False}
                    ],
                    "correction": "La légende apporte des informations précises sur ce que l'on voit (lieu, date, auteur)."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le rôle d'une affiche publicitaire ?",
                    "answerOptions": [
                        {"text": "Inciter à l'achat ou faire passer un message", "isCorrect": True},
                        {"text": "Éclairer la rue", "isCorrect": False},
                        {"text": "Donner le journal", "isCorrect": False},
                        {"text": "Cacher les murs abîmés", "isCorrect": False}
                    ],
                    "correction": "La publicité utilise l'image et le slogan pour convaincre."
                },
                {
                    "questionNumber": 63,
                    "question": "Dans une bande dessinée, où écrit-on les paroles des personnages ?",
                    "answerOptions": [
                        {"text": "Dans des bulles (ou phylactères)", "isCorrect": True},
                        {"text": "Dans les marges", "isCorrect": False},
                        {"text": "Sous les pieds", "isCorrect": False},
                        {"text": "Au dos de la page", "isCorrect": False}
                    ],
                    "correction": "La bulle relie le texte au personnage qui parle."
                },
                {
                    "questionNumber": 64,
                    "question": "Que signifie 'cadrage' au cinéma ou en photographie ?",
                    "answerOptions": [
                        {"text": "Ce que l'on choisit de montrer à l'intérieur de l'image", "isCorrect": True},
                        {"text": "Le prix de l'appareil", "isCorrect": False},
                        {"text": "La couleur du cadre en bois", "isCorrect": False},
                        {"text": "Le poids de la caméra", "isCorrect": False}
                    ],
                    "correction": "Le cadrage (gros plan, plan large) modifie la perception du spectateur."
                },
                {
                    "questionNumber": 65,
                    "question": "Qu'est-ce qu'un 'slogan' ?",
                    "answerOptions": [
                        {"text": "Une phrase courte et frappante facile à retenir", "isCorrect": True},
                        {"text": "Le nom du réalisateur", "isCorrect": False},
                        {"text": "Un poème de 20 pages", "isCorrect": False},
                        {"text": "Un gros mot", "isCorrect": False}
                    ],
                    "correction": "C'est l'outil de base de la publicité et de la politique."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on le premier plan d'une image ?",
                    "answerOptions": [
                        {"text": "Les éléments les plus proches du spectateur", "isCorrect": True},
                        {"text": "Le décor au fond", "isCorrect": False},
                        {"text": "Le ciel", "isCorrect": False},
                        {"text": "L'image entière", "isCorrect": False}
                    ],
                    "correction": "L'image est souvent composée de plusieurs plans (premier plan, second plan, arrière-plan)."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la fonction d'un logo ?",
                    "answerOptions": [
                        {"text": "Représenter visuellement une marque ou une entreprise", "isCorrect": True},
                        {"text": "Donner l'heure", "isCorrect": False},
                        {"text": "Remplacer l'adresse", "isCorrect": False},
                        {"text": "Payer les factures", "isCorrect": False}
                    ],
                    "correction": "Le logo permet d'identifier immédiatement une organisation."
                },
                {
                    "questionNumber": 68,
                    "question": "Qu'est-ce qu'un 'angle de vue' en plongée ?",
                    "answerOptions": [
                        {"text": "La caméra regarde vers le bas", "isCorrect": True},
                        {"text": "La caméra regarde vers le haut", "isCorrect": False},
                        {"text": "La caméra est sous l'eau", "isCorrect": False},
                        {"text": "La caméra est éteinte", "isCorrect": False}
                    ],
                    "correction": "La plongée a tendance à écraser le sujet ou à le rendre vulnérable."
                },
                {
                    "questionNumber": 69,
                    "question": "À quoi sert une caricature ?",
                    "answerOptions": [
                        {"text": "Exagérer les traits pour se moquer ou critiquer", "isCorrect": True},
                        {"text": "Faire un portrait identique à la réalité", "isCorrect": False},
                        {"text": "Apprendre à dessiner", "isCorrect": False},
                        {"text": "Prendre une photo", "isCorrect": False}
                    ],
                    "correction": "C'est un dessin humoristique souvent utilisé dans la presse."
                },
                {
                    "questionNumber": 70,
                    "question": "Que désigne le terme 'médias' ?",
                    "answerOptions": [
                        {"text": "Les moyens de diffusion de l'information (presse, TV, radio, internet)", "isCorrect": True},
                        {"text": "Les médicaments", "isCorrect": False},
                        {"text": "Les personnes de taille moyenne", "isCorrect": False},
                        {"text": "Le nom des professeurs", "isCorrect": False}
                    ],
                    "correction": "Les médias jouent un rôle clé dans la formation de l'opinion publique."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment appelle-t-on une fausse information qui circule sur Internet ?",
                    "answerOptions": [
                        {"text": "Une fake news (infox)", "isCorrect": True},
                        {"text": "Un tutoriel", "isCorrect": False},
                        {"text": "Un lien hypertexte", "isCorrect": False},
                        {"text": "Une publicité", "isCorrect": False}
                    ],
                    "correction": "Il faut toujours vérifier ses sources pour ne pas se faire tromper."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le but d'un reportage photo ?",
                    "answerOptions": [
                        {"text": "Témoigner d'un événement réel par l'image", "isCorrect": True},
                        {"text": "Vendre des appareils photo", "isCorrect": False},
                        {"text": "Faire des portraits de mode", "isCorrect": False},
                        {"text": "Faire des montages truqués", "isCorrect": False}
                    ],
                    "correction": "Le photojournalisme est une branche importante de l'information."
                },
                {
                    "questionNumber": 73,
                    "question": "Que signifie 'noir et blanc' en photographie ?",
                    "answerOptions": [
                        {"text": "Une image sans couleurs, uniquement avec des nuances de gris", "isCorrect": True},
                        {"text": "Une image très sombre", "isCorrect": False},
                        {"text": "Une image que l'on ne voit pas", "isCorrect": False},
                        {"text": "Une photo de nuit uniquement", "isCorrect": False}
                    ],
                    "correction": "Le noir et blanc est souvent utilisé pour son aspect esthétique ou historique."
                },
                {
                    "questionNumber": 74,
                    "question": "Qu'est-ce qu'une source d'information ?",
                    "answerOptions": [
                        {"text": "L'origine de l'information (journaliste, témoin, agence de presse)", "isCorrect": True},
                        {"text": "De l'eau qui coule", "isCorrect": False},
                        {"text": "Un dictionnaire", "isCorrect": False},
                        {"text": "La fin du journal", "isCorrect": False}
                    ],
                    "correction": "Vérifier la source permet de savoir si l'information est fiable."
                },
                {
                    "questionNumber": 75,
                    "question": "À quoi sert un 'éditorial' dans un journal ?",
                    "answerOptions": [
                        {"text": "Donner l'opinion du directeur du journal sur un sujet", "isCorrect": True},
                        {"text": "Donner les résultats du loto", "isCorrect": False},
                        {"text": "Lister les petites annonces", "isCorrect": False},
                        {"text": "Remplacer les images", "isCorrect": False}
                    ],
                    "correction": "L'éditorial n'est pas un article d'information pure, mais un texte engagé."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est l'intérêt d'une infographie (image + texte court) ?",
                    "answerOptions": [
                        {"text": "Rendre des données complexes faciles à comprendre", "isCorrect": True},
                        {"text": "Faire joli dans le journal", "isCorrect": False},
                        {"text": "Remplacer totalement le journaliste", "isCorrect": False},
                        {"text": "Cacher le manque de texte", "isCorrect": False}
                    ],
                    "correction": "Elle mélange dessins, graphiques et chiffres pour une lecture rapide."
                },
                {
                    "questionNumber": 77,
                    "question": "Comment s'appelle la première page d'un journal ?",
                    "answerOptions": [
                        {"text": "La une", "isCorrect": True},
                        {"text": "Le sommaire", "isCorrect": False},
                        {"text": "La préface", "isCorrect": False},
                        {"text": "Le dos", "isCorrect": False}
                    ],
                    "correction": "C'est la vitrine du journal qui doit inciter à l'achat."
                },
                {
                    "questionNumber": 78,
                    "question": "Que signifie 'contre-plongée' ?",
                    "answerOptions": [
                        {"text": "La caméra regarde vers le haut", "isCorrect": True},
                        {"text": "La caméra regarde vers le bas", "isCorrect": False},
                        {"text": "La caméra est à l'envers", "isCorrect": False},
                        {"text": "La caméra ne filme rien", "isCorrect": False}
                    ],
                    "correction": "La contre-plongée a tendance à agrandir le sujet ou à lui donner de l'importance."
                },
                {
                    "questionNumber": 79,
                    "question": "Qu'est-ce qu'un fait divers ?",
                    "answerOptions": [
                        {"text": "Une information sans portée générale (accidents, vols, événements locaux)", "isCorrect": True},
                        {"text": "Un texte politique important", "isCorrect": False},
                        {"text": "Une règle de français", "isCorrect": False},
                        {"text": "Une publicité pour les voitures", "isCorrect": False}
                    ],
                    "correction": "Les faits divers sont très lus car ils touchent à la vie quotidienne."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le but d'un documentaire ?",
                    "answerOptions": [
                        {"text": "Informer sur un sujet réel de manière approfondie", "isCorrect": True},
                        {"text": "Faire rire les enfants", "isCorrect": False},
                        {"text": "Vendre des produits de beauté", "isCorrect": False},
                        {"text": "Raconter une légende imaginaire", "isCorrect": False}
                    ],
                    "correction": "Le documentaire se base sur des recherches et des témoignages réels."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : VOCABULAIRE ET ANALYSE LITTÉRAIRE (Q81 à Q100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : VOCABULAIRE ET ANALYSE LITTÉRAIRE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la définition d'un 'narrateur' ?",
                    "answerOptions": [
                        {"text": "Celui qui raconte l'histoire", "isCorrect": True},
                        {"text": "Celui qui a écrit le livre", "isCorrect": False},
                        {"text": "Le personnage méchant", "isCorrect": False},
                        {"text": "Le lecteur", "isCorrect": False}
                    ],
                    "correction": "Le narrateur n'est pas forcément l'auteur (ex: un personnage peut être le narrateur)."
                },
                {
                    "questionNumber": 82,
                    "question": "Qu'est-ce qu'une 'allitération' ?",
                    "answerOptions": [
                        {"text": "La répétition d'un son de consonne", "isCorrect": True},
                        {"text": "Le nom d'un outil de jardin", "isCorrect": False},
                        {"text": "Une faute d'orthographe", "isCorrect": False},
                        {"text": "Une majuscule au milieu d'un mot", "isCorrect": False}
                    ],
                    "correction": "Exemple : 'Pour qui sont ces serpents qui sifflent sur vos têtes ?' (son 's')."
                },
                {
                    "questionNumber": 83,
                    "question": "Comment appelle-t-on une pièce de théâtre courte et comique ?",
                    "answerOptions": [
                        {"text": "Une farce", "isCorrect": True},
                        {"text": "Une tragédie", "isCorrect": False},
                        {"text": "Un roman", "isCorrect": False},
                        {"text": "Une épopée", "isCorrect": False}
                    ],
                    "correction": "La farce utilise souvent un humour simple et des situations exagérées."
                },
                {
                    "questionNumber": 84,
                    "question": "Que signifie le mot 'exode' ?",
                    "answerOptions": [
                        {"text": "Le départ massif d'une population", "isCorrect": True},
                        {"text": "La fin d'une chanson", "isCorrect": False},
                        {"text": "Un vêtement de luxe", "isCorrect": False},
                        {"text": "Un type de dictionnaire", "isCorrect": False}
                    ],
                    "correction": "Exemple : l'exode rural désigne le départ des habitants de la campagne vers la ville."
                },
                {
                    "questionNumber": 85,
                    "question": "Qu'est-ce qu'un 'incipit' ?",
                    "answerOptions": [
                        {"text": "Le début d'un roman", "isCorrect": True},
                        {"text": "La fin d'un poème", "isCorrect": False},
                        {"text": "Le nom de l'imprimeur", "isCorrect": False},
                        {"text": "Un mot pour dire 'merci'", "isCorrect": False}
                    ],
                    "correction": "L'incipit accroche le lecteur et pose le cadre de l'histoire."
                },
                {
                    "questionNumber": 86,
                    "question": "Trouvez l'intrus parmi ces genres littéraires :",
                    "answerOptions": [
                        {"text": "Peinture", "isCorrect": True},
                        {"text": "Poésie", "isCorrect": False},
                        {"text": "Théâtre", "isCorrect": False},
                        {"text": "Roman", "isCorrect": False}
                    ],
                    "correction": "La peinture est un art visuel, les autres sont des arts du langage écrit."
                },
                {
                    "questionNumber": 87,
                    "question": "Que signifie 'déclamer' ?",
                    "answerOptions": [
                        {"text": "Lire un texte à haute voix avec emphase", "isCorrect": True},
                        {"text": "Écrire très vite", "isCorrect": False},
                        {"text": "Se taire", "isCorrect": False},
                        {"text": "Déchirer une feuille", "isCorrect": False}
                    ],
                    "correction": "On déclame souvent des poèmes ou des discours."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'une 'rime' ?",
                    "answerOptions": [
                        {"text": "La répétition d'un même son à la fin de deux vers", "isCorrect": True},
                        {"text": "Le titre du poème", "isCorrect": False},
                        {"text": "Le nom de l'auteur", "isCorrect": False},
                        {"text": "Une majuscule", "isCorrect": False}
                    ],
                    "correction": "Les rimes créent la musicalité de la poésie."
                },
                {
                    "questionNumber": 89,
                    "question": "Que désigne un 'antagoniste' ?",
                    "answerOptions": [
                        {"text": "Le personnage qui s'oppose au héros", "isCorrect": True},
                        {"text": "L'ami du héros", "isCorrect": False},
                        {"text": "Une petite fleur", "isCorrect": False},
                        {"text": "La fin de l'histoire", "isCorrect": False}
                    ],
                    "correction": "L'antagoniste est souvent le 'méchant' de l'histoire."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est la définition de la 'polysémie' ?",
                    "answerOptions": [
                        {"text": "Le fait qu'un mot ait plusieurs sens", "isCorrect": True},
                        {"text": "Un mot qui n'a pas de voyelles", "isCorrect": False},
                        {"text": "Un mot très long", "isCorrect": False},
                        {"text": "Une faute de grammaire", "isCorrect": False}
                    ],
                    "correction": "Exemple : le mot 'bouton' (vêtement, fleur, peau, radio)."
                },
                {
                    "questionNumber": 91,
                    "question": "Qu'est-ce qu'une 'ellipse' dans un récit ?",
                    "answerOptions": [
                        {"text": "Sauter une période de temps pour accélérer l'histoire", "isCorrect": True},
                        {"text": "Le nom d'une planète", "isCorrect": False},
                        {"text": "Une description très longue", "isCorrect": False},
                        {"text": "Un dialogue entre deux personnes", "isCorrect": False}
                    ],
                    "correction": "Exemple : 'Dix ans plus tard...'."
                },
                {
                    "questionNumber": 92,
                    "question": "Que signifie le mot 'ironie' ?",
                    "answerOptions": [
                        {"text": "Dire le contraire de ce que l'on pense pour se moquer", "isCorrect": True},
                        {"text": "Dire la vérité", "isCorrect": False},
                        {"text": "Parler avec une voix grave", "isCorrect": False},
                        {"text": "Ne rien dire", "isCorrect": False}
                    ],
                    "correction": "L'ironie nécessite que l'interlocuteur comprenne le décalage."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment appelle-t-on une petite histoire qui donne une leçon de morale ?",
                    "answerOptions": [
                        {"text": "Une fable", "isCorrect": True},
                        {"text": "Un dictionnaire", "isCorrect": False},
                        {"text": "Un mode d'emploi", "isCorrect": False},
                        {"text": "Une affiche", "isCorrect": False}
                    ],
                    "correction": "Jean de La Fontaine est le plus célèbre auteur de fables."
                },
                {
                    "questionNumber": 94,
                    "question": "Que signifie 'dénotatif' ?",
                    "answerOptions": [
                        {"text": "Le sens premier et neutre d'un mot (celui du dictionnaire)", "isCorrect": True},
                        {"text": "Le sens caché", "isCorrect": False},
                        {"text": "Un mot inventé", "isCorrect": False},
                        {"text": "Une insulte", "isCorrect": False}
                    ],
                    "correction": "Il s'oppose au sens 'connotatif' (subjectif)."
                },
                {
                    "questionNumber": 95,
                    "question": "Qu'est-ce qu'une 'péripétie' ?",
                    "answerOptions": [
                        {"text": "Un événement imprévu qui change le cours de l'action", "isCorrect": True},
                        {"text": "Une longue description du paysage", "isCorrect": False},
                        {"text": "Le nom d'un petit animal", "isCorrect": False},
                        {"text": "La première page du livre", "isCorrect": False}
                    ],
                    "correction": "Les péripéties relancent l'intérêt du lecteur."
                },
                {
                    "questionNumber": 96,
                    "question": "Trouvez le sens de l'expression : 'Un bruit qui court'.",
                    "answerOptions": [
                        {"text": "Une rumeur qui se propage", "isCorrect": True},
                        {"text": "Une porte qui grince", "isCorrect": False},
                        {"text": "Une radio allumée", "isCorrect": False},
                        {"text": "Une personne qui crie en courant", "isCorrect": False}
                    ],
                    "correction": "C'est un sens figuré."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle phrase contient une 'énumération' ?",
                    "answerOptions": [
                        {"text": "J'ai acheté du pain, des pommes et du lait", "isCorrect": True},
                        {"text": "J'ai acheté du pain pour ce soir", "isCorrect": False},
                        {"text": "Le pain que j'ai acheté est frais", "isCorrect": False},
                        {"text": "Je n'ai pas acheté de pain", "isCorrect": False}
                    ],
                    "correction": "L'énumération liste plusieurs éléments de même nature."
                },
                {
                    "questionNumber": 98,
                    "question": "Que désigne un mot 'abstrait' ?",
                    "answerOptions": [
                        {"text": "Une idée ou un sentiment que l'on ne peut pas toucher", "isCorrect": True},
                        {"text": "Un objet solide", "isCorrect": False},
                        {"text": "Un outil de chantier", "isCorrect": False},
                        {"text": "Un aliment", "isCorrect": False}
                    ],
                    "correction": "Exemple : la liberté, le courage, la joie."
                },
                {
                    "questionNumber": 99,
                    "question": "Trouvez le mot générique pour la liste : 'Marteau, tournevis, pince'.",
                    "answerOptions": [
                        {"text": "Outil", "isCorrect": True},
                        {"text": "Objet", "isCorrect": False},
                        {"text": "Ferraille", "isCorrect": False},
                        {"text": "Machin", "isCorrect": False}
                    ],
                    "correction": "Le mot générique regroupe l'ensemble de la catégorie."
                },
                {
                    "questionNumber": 100,
                    "question": "Si un texte est écrit à la 3ème personne (il), qui raconte ?",
                    "answerOptions": [
                        {"text": "Un narrateur extérieur à l'histoire", "isCorrect": True},
                        {"text": "Le personnage principal lui-même", "isCorrect": False},
                        {"text": "Le lecteur à haute voix", "isCorrect": False},
                        {"text": "Personne", "isCorrect": False}
                    ],
                    "correction": "Le narrateur raconte les faits sans y participer directement."
                }
            ]
        }
    }
}