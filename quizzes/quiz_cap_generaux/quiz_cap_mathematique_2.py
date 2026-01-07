quiz_data = {
    "title": "Quiz Mathématiques - Niveau CAP - Série 2 (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : PROPORTIONNALITÉ ET INFORMATION CHIFFRÉE (Q1 à Q20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : PROPORTIONNALITÉ ET INFORMATION CHIFFRÉE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Que signifie une échelle écrite sous la forme 1:50 sur un plan d'architecte ?",
                    "answerOptions": [
                        {"text": "1 cm sur le plan équivaut à 50 cm en réalité", "isCorrect": True},
                        {"text": "1 cm en réalité équivaut à 50 cm sur le plan papier", "isCorrect": False},
                        {"text": "Le plan est cinquante fois plus grand que la réalité", "isCorrect": False},
                        {"text": "Il faut ajouter 50 cm à chaque mesure prise sur le plan", "isCorrect": False}
                    ],
                    "correction": "L'échelle est le rapport de réduction. 1:50 signifie que les longueurs réelles sont divisées par 50 sur le dessin, ou inversement, qu'un centimètre dessiné représente 50 centimètres réels."
                },
                {
                    "questionNumber": 2,
                    "question": "Pour partager une somme de 100 € selon un ratio 2:3, quelles sont les parts ?",
                    "answerOptions": [
                        {"text": "40 € et 60 €", "isCorrect": True},
                        {"text": "20 € et 30 €", "isCorrect": False},
                        {"text": "50 € et 50 €", "isCorrect": False},
                        {"text": "2 € et 3 €", "isCorrect": False}
                    ],
                    "correction": "Le total représente 2 + 3 = 5 parts. Une part vaut 100 divisé par 5, soit 20 €. Les parts sont donc 2x20 et 3x20."
                },
                {
                    "questionNumber": 3,
                    "question": "Une remise de 20 % sur un article de 80 € correspond à une réduction de :",
                    "answerOptions": [
                        {"text": "16 €", "isCorrect": True},
                        {"text": "20 €", "isCorrect": False},
                        {"text": "64 €", "isCorrect": False},
                        {"text": "8 €", "isCorrect": False}
                    ],
                    "correction": "Réduction = 80 × (20/100) = 80 × 0,2 = 16 €."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel coefficient multiplicateur applique-t-on pour une augmentation de 15 % ?",
                    "answerOptions": [
                        {"text": "1,15", "isCorrect": True},
                        {"text": "0,15", "isCorrect": False},
                        {"text": "15", "isCorrect": False},
                        {"text": "0,85", "isCorrect": False}
                    ],
                    "correction": "Coefficient Multiplicateur = 1 + (15/100) = 1,15."
                },
                {
                    "questionNumber": 5,
                    "question": "Si une voiture consomme 6 litres aux 100 km, combien consommera-t-elle pour 250 km ?",
                    "answerOptions": [
                        {"text": "15 litres", "isCorrect": True},
                        {"text": "12 litres", "isCorrect": False},
                        {"text": "18 litres", "isCorrect": False},
                        {"text": "6,25 litres", "isCorrect": False}
                    ],
                    "correction": "C'est une situation de proportionnalité : (6 × 250) / 100 = 1500 / 100 = 15."
                },
                {
                    "questionNumber": 6,
                    "question": "Que vaut 25 % d'une quantité sous forme de fraction simplifiée ?",
                    "answerOptions": [
                        {"text": "1/4", "isCorrect": True},
                        {"text": "1/2", "isCorrect": False},
                        {"text": "1/5", "isCorrect": False},
                        {"text": "2/5", "isCorrect": False}
                    ],
                    "correction": "25 % = 25/100. En divisant par 25 en haut et en bas, on obtient 1/4."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est le prix TTC d'un article à 50 € HT avec une TVA à 5,5 % ?",
                    "answerOptions": [
                        {"text": "52,75 €", "isCorrect": True},
                        {"text": "55,50 €", "isCorrect": False},
                        {"text": "50,55 €", "isCorrect": False},
                        {"text": "47,25 €", "isCorrect": False}
                    ],
                    "correction": "Montant TVA = 50 × 0,055 = 2,75 €. Prix TTC = 50 + 2,75 = 52,75 €."
                },
                {
                    "questionNumber": 8,
                    "question": "Un prix passe de 100 € à 90 €. Quel est le taux d'évolution ?",
                    "answerOptions": [
                        {"text": "- 10 %", "isCorrect": True},
                        {"text": "- 90 %", "isCorrect": False},
                        {"text": "10 %", "isCorrect": False},
                        {"text": "- 1 €", "isCorrect": False}
                    ],
                    "correction": "Taux = (Valeur finale - Valeur initiale) / Valeur initiale = (90-100)/100 = -10/100 = -10%."
                },
                {
                    "questionNumber": 9,
                    "question": "Si un mélange contient 3 volumes d'eau pour 1 volume de sirop, quel est le pourcentage de sirop ?",
                    "answerOptions": [
                        {"text": "25 %", "isCorrect": True},
                        {"text": "33,3 %", "isCorrect": False},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "75 %", "isCorrect": False}
                    ],
                    "correction": "Le total fait 3 + 1 = 4 volumes. La part de sirop est de 1/4, soit 25%."
                },
                {
                    "questionNumber": 10,
                    "question": "Un article coûte 120 € après une remise de 20 %. Quel était son prix initial ?",
                    "answerOptions": [
                        {"text": "150 €", "isCorrect": True},
                        {"text": "144 €", "isCorrect": False},
                        {"text": "140 €", "isCorrect": False},
                        {"text": "100 €", "isCorrect": False}
                    ],
                    "correction": "Prix initial = Prix final / CM. Ici CM = 0,80. 120 / 0,80 = 150 €."
                },
                {
                    "questionNumber": 11,
                    "question": "Combien de temps faut-il pour parcourir 30 km à une vitesse de 60 km/h ?",
                    "answerOptions": [
                        {"text": "30 minutes", "isCorrect": True},
                        {"text": "2 heures", "isCorrect": False},
                        {"text": "15 minutes", "isCorrect": False},
                        {"text": "45 minutes", "isCorrect": False}
                    ],
                    "correction": "Temps = Distance / Vitesse = 30 / 60 = 0,5 heure. 0,5 h × 60 min = 30 minutes."
                },
                {
                    "questionNumber": 12,
                    "question": "Convertissez un taux d'intérêt de 0,5 % par mois en taux annuel simple.",
                    "answerOptions": [
                        {"text": "6 %", "isCorrect": True},
                        {"text": "5 %", "isCorrect": False},
                        {"text": "12 %", "isCorrect": False},
                        {"text": "0,5 %", "isCorrect": False}
                    ],
                    "correction": "Taux annuel = Taux mensuel × 12 mois = 0,5 × 12 = 6 %."
                },
                {
                    "questionNumber": 13,
                    "question": "Sur une carte au 1:25 000, quelle distance réelle représente un segment de 4 cm ?",
                    "answerOptions": [
                        {"text": "1 km", "isCorrect": True},
                        {"text": "100 m", "isCorrect": False},
                        {"text": "10 km", "isCorrect": False},
                        {"text": "250 m", "isCorrect": False}
                    ],
                    "correction": "4 cm × 25 000 = 100 000 cm = 1 000 m = 1 km."
                },
                {
                    "questionNumber": 14,
                    "question": "Le prix HT d'un service est 200 €. Après une taxe de 20 %, le prix TTC est de :",
                    "answerOptions": [
                        {"text": "240 €", "isCorrect": True},
                        {"text": "220 €", "isCorrect": False},
                        {"text": "202 €", "isCorrect": False},
                        {"text": "400 €", "isCorrect": False}
                    ],
                    "correction": "200 × 1,20 = 240 €."
                },
                {
                    "questionNumber": 15,
                    "question": "Comment appelle-t-on le résultat d'une division ?",
                    "answerOptions": [
                        {"text": "Le quotient", "isCorrect": True},
                        {"text": "Le produit", "isCorrect": False},
                        {"text": "La somme", "isCorrect": False},
                        {"text": "La différence", "isCorrect": False}
                    ],
                    "correction": "Somme (addition), Différence (soustraction), Produit (multiplication), Quotient (division)."
                },
                {
                    "questionNumber": 16,
                    "question": "Que signifie un ratio de 1:1 ?",
                    "answerOptions": [
                        {"text": "Les deux quantités sont égales", "isCorrect": True},
                        {"text": "La première est le double de la deuxième", "isCorrect": False},
                        {"text": "Il n'y a qu'une seule part", "isCorrect": False},
                        {"text": "Le résultat est nul", "isCorrect": False}
                    ],
                    "correction": "1:1 signifie que pour chaque unité de l'un, il y a exactement une unité de l'autre (moitié-moitié)."
                },
                {
                    "questionNumber": 17,
                    "question": "Un commerçant achète un produit 10 € et le revend 15 €. Quel est son taux de marge ?",
                    "answerOptions": [
                        {"text": "50 %", "isCorrect": True},
                        {"text": "5 %", "isCorrect": False},
                        {"text": "150 %", "isCorrect": False},
                        {"text": "33 %", "isCorrect": False}
                    ],
                    "correction": "Marge = 15 - 10 = 5 €. Taux de marge = (5/10) × 100 = 50%."
                },
                {
                    "questionNumber": 18,
                    "question": "Si x / 4 = 5, alors x vaut :",
                    "answerOptions": [
                        {"text": "20", "isCorrect": True},
                        {"text": "9", "isCorrect": False},
                        {"text": "1,25", "isCorrect": False},
                        {"text": "1", "isCorrect": False}
                    ],
                    "correction": "On multiplie par 4 des deux côtés : x = 5 × 4 = 20."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est la valeur de 10 % de 10 % de 100 ?",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "10", "isCorrect": False},
                        {"text": "0,1", "isCorrect": False},
                        {"text": "20", "isCorrect": False}
                    ],
                    "correction": "10 % de 100 = 10. Puis 10 % de 10 = 1."
                },
                {
                    "questionNumber": 20,
                    "question": "Dans une recette pour 4 personnes, il faut 200g de farine. Pour 6 personnes, il faudra :",
                    "answerOptions": [
                        {"text": "300g", "isCorrect": True},
                        {"text": "400g", "isCorrect": False},
                        {"text": "250g", "isCorrect": False},
                        {"text": "600g", "isCorrect": False}
                    ],
                    "correction": "(200 / 4) × 6 = 50 × 6 = 300g."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : GÉOMÉTRIE ET CONFIGURATIONS DU PLAN (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : GÉOMÉTRIE ET CONFIGURATIONS DU PLAN",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Dans un triangle rectangle, quel côté est situé en face de l'angle droit ?",
                    "answerOptions": [
                        {"text": "L'hypoténuse", "isCorrect": True},
                        {"text": "Le côté adjacent", "isCorrect": False},
                        {"text": "Le côté opposé", "isCorrect": False},
                        {"text": "La médiane", "isCorrect": False}
                    ],
                    "correction": "L'hypoténuse est toujours le côté le plus long du triangle rectangle."
                },
                {
                    "questionNumber": 22,
                    "question": "Si les longueurs des deux petits côtés d'un triangle rectangle sont 3 et 4, quelle est la longueur de l'hypoténuse ?",
                    "answerOptions": [
                        {"text": "5", "isCorrect": True},
                        {"text": "7", "isCorrect": False},
                        {"text": "12", "isCorrect": False},
                        {"text": "25", "isCorrect": False}
                    ],
                    "correction": "Théorème de Pythagore : 3² + 4² = 9 + 16 = 25. La racine carrée de 25 est 5."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le périmètre d'un cercle de diamètre 10 cm (prendre π = 3,14) ?",
                    "answerOptions": [
                        {"text": "31,4 cm", "isCorrect": True},
                        {"text": "62,8 cm", "isCorrect": False},
                        {"text": "314 cm", "isCorrect": False},
                        {"text": "15,7 cm", "isCorrect": False}
                    ],
                    "correction": "Périmètre = π × Diamètre = 3,14 × 10 = 31,4 cm."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est l'aire d'un disque de rayon 2 cm (prendre π = 3,14) ?",
                    "answerOptions": [
                        {"text": "12,56 cm²", "isCorrect": True},
                        {"text": "6,28 cm²", "isCorrect": False},
                        {"text": "4 cm²", "isCorrect": False},
                        {"text": "3,14 cm²", "isCorrect": False}
                    ],
                    "correction": "Aire = π × r² = 3,14 × 2² = 3,14 × 4 = 12,56 cm²."
                },
                {
                    "questionNumber": 25,
                    "question": "Un losange est un quadrilatère qui a :",
                    "answerOptions": [
                        {"text": "Ses quatre côtés de même longueur", "isCorrect": True},
                        {"text": "Quatre angles droits", "isCorrect": False},
                        {"text": "Des diagonales de même longueur", "isCorrect": False},
                        {"text": "Uniquement deux côtés égaux", "isCorrect": False}
                    ],
                    "correction": "Le losange se définit par ses 4 côtés égaux. Ses diagonales se coupent en leur milieu perpendiculairement."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la somme des angles d'un quadrilatère ?",
                    "answerOptions": [
                        {"text": "360°", "isCorrect": True},
                        {"text": "180°", "isCorrect": False},
                        {"text": "90°", "isCorrect": False},
                        {"text": "400°", "isCorrect": False}
                    ],
                    "correction": "Un quadrilatère peut être coupé en deux triangles. Comme chaque triangle fait 180°, le total fait 360°."
                },
                {
                    "questionNumber": 27,
                    "question": "Que peut-on affirmer sur les diagonales d'un rectangle ?",
                    "answerOptions": [
                        {"text": "Elles ont la même longueur et se coupent en leur milieu", "isCorrect": True},
                        {"text": "Elles sont perpendiculaires", "isCorrect": False},
                        {"text": "Elles sont parallèles", "isCorrect": False},
                        {"text": "Elles ont des longueurs différentes", "isCorrect": False}
                    ],
                    "correction": "C'est une propriété caractéristique du rectangle."
                },
                {
                    "questionNumber": 28,
                    "question": "Le triangle dont les trois côtés sont égaux s'appelle :",
                    "answerOptions": [
                        {"text": "Équilatéral", "isCorrect": True},
                        {"text": "Isocèle", "isCorrect": False},
                        {"text": "Rectangle", "isCorrect": False},
                        {"text": "Scalène", "isCorrect": False}
                    ],
                    "correction": "Étymologiquement : 'équi' (égal) et 'latéral' (côté)."
                },
                {
                    "questionNumber": 29,
                    "question": "Dans un triangle isocèle, les deux angles à la base sont :",
                    "answerOptions": [
                        {"text": "Égaux", "isCorrect": True},
                        {"text": "Droits", "isCorrect": False},
                        {"text": "Différents", "isCorrect": False},
                        {"text": "Toujours de 45°", "isCorrect": False}
                    ],
                    "correction": "C'est une propriété fondamentale liée à l'axe de symétrie du triangle isocèle."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle est la définition de droites perpendiculaires ?",
                    "answerOptions": [
                        {"text": "Elles se coupent en formant un angle droit", "isCorrect": True},
                        {"text": "Elles ne se croisent jamais", "isCorrect": False},
                        {"text": "Elles se croisent au hasard", "isCorrect": False},
                        {"text": "Elles sont de même longueur", "isCorrect": False}
                    ],
                    "correction": "Le symbole utilisé est souvent un petit carré au point d'intersection."
                },
                {
                    "questionNumber": 31,
                    "question": "Un angle aigu est un angle compris entre :",
                    "answerOptions": [
                        {"text": "0° et 90°", "isCorrect": True},
                        {"text": "90° et 180°", "isCorrect": False},
                        {"text": "Exactement 90°", "isCorrect": False},
                        {"text": "180° et 360°", "isCorrect": False}
                    ],
                    "correction": "Un angle aigu est plus 'fermé' qu'un angle droit."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est l'unité de mesure principale d'un angle ?",
                    "answerOptions": [
                        {"text": "Le degré", "isCorrect": True},
                        {"text": "Le mètre", "isCorrect": False},
                        {"text": "Le gramme", "isCorrect": False},
                        {"text": "Le litre", "isCorrect": False}
                    ],
                    "correction": "Même s'il existe le radian ou le grade, le degré est l'unité usuelle."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment appelle-t-on le point de rencontre des deux côtés d'un angle ?",
                    "answerOptions": [
                        {"text": "Le sommet", "isCorrect": True},
                        {"text": "L'origine", "isCorrect": False},
                        {"text": "La base", "isCorrect": False},
                        {"text": "L'axe", "isCorrect": False}
                    ],
                    "correction": "On le nomme souvent par une lettre majuscule (ex : Sommet A)."
                },
                {
                    "questionNumber": 34,
                    "question": "Dans un repère, quel axe est vertical ?",
                    "answerOptions": [
                        {"text": "L'axe des ordonnées (y)", "isCorrect": True},
                        {"text": "L'axe des abscisses (x)", "isCorrect": False},
                        {"text": "L'axe des altitudes (z)", "isCorrect": False},
                        {"text": "La droite de graduation", "isCorrect": False}
                    ],
                    "correction": "Abscisses = Horizontal, Ordonnées = Vertical."
                },
                {
                    "questionNumber": 35,
                    "question": "Une symétrie axiale par rapport à une droite 'd' correspond à :",
                    "answerOptions": [
                        {"text": "Un pliage le long de la droite d", "isCorrect": True},
                        {"text": "Un demi-tour autour d'un point", "isCorrect": False},
                        {"text": "Un glissement sans tourner", "isCorrect": False},
                        {"text": "Un agrandissement", "isCorrect": False}
                    ],
                    "correction": "La droite est la médiatrice des segments reliant chaque point à son image."
                },
                {
                    "questionNumber": 36,
                    "question": "Un triangle rectangle a un angle de 90° et un autre de 30°. Quel est le troisième angle ?",
                    "answerOptions": [
                        {"text": "60°", "isCorrect": True},
                        {"text": "30°", "isCorrect": False},
                        {"text": "90°", "isCorrect": False},
                        {"text": "120°", "isCorrect": False}
                    ],
                    "correction": "180 - (90 + 30) = 180 - 120 = 60°."
                },
                {
                    "questionNumber": 37,
                    "question": "La médiatrice d'un segment est la droite qui :",
                    "answerOptions": [
                        {"text": "Passe par le milieu du segment et lui est perpendiculaire", "isCorrect": True},
                        {"text": "Relie les deux extrémités", "isCorrect": False},
                        {"text": "Est parallèle au segment", "isCorrect": False},
                        {"text": "Coupe un angle en deux", "isCorrect": False}
                    ],
                    "correction": "Tout point de la médiatrice est à égale distance des deux extrémités du segment."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est l'aire d'un triangle de base 10 cm et de hauteur 6 cm ?",
                    "answerOptions": [
                        {"text": "30 cm²", "isCorrect": True},
                        {"text": "60 cm²", "isCorrect": False},
                        {"text": "16 cm²", "isCorrect": False},
                        {"text": "15 cm²", "isCorrect": False}
                    ],
                    "correction": "Aire = (Base × hauteur) / 2 = (10 × 6) / 2 = 60 / 2 = 30 cm²."
                },
                {
                    "questionNumber": 39,
                    "question": "Combien de côtés possède un hexagone ?",
                    "answerOptions": [
                        {"text": "6", "isCorrect": True},
                        {"text": "5", "isCorrect": False},
                        {"text": "8", "isCorrect": False},
                        {"text": "4", "isCorrect": False}
                    ],
                    "correction": "Hecta/Hexa signifie 6 (ex: la France est surnommée l'Hexagone)."
                },
                {
                    "questionNumber": 40,
                    "question": "Que signifie le mot 'isométrie' ?",
                    "answerOptions": [
                        {"text": "Qui conserve les longueurs et les formes", "isCorrect": True},
                        {"text": "Qui agrandit les objets", "isCorrect": False},
                        {"text": "Qui mesure la température", "isCorrect": False},
                        {"text": "Qui change la couleur", "isCorrect": False}
                    ],
                    "correction": "Une symétrie est une isométrie : l'image est identique à l'original."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : ALGÈBRE ET RÉSOLUTION DE PROBLÈMES (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ALGÈBRE ET RÉSOLUTION DE PROBLÈMES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Réduisez l'expression : 3x + 5x - 2x",
                    "answerOptions": [
                        {"text": "6x", "isCorrect": True},
                        {"text": "10x", "isCorrect": False},
                        {"text": "6", "isCorrect": False},
                        {"text": "x", "isCorrect": False}
                    ],
                    "correction": "(3 + 5 - 2)x = 6x."
                },
                {
                    "questionNumber": 42,
                    "question": "Résolvez l'équation : x - 10 = 40",
                    "answerOptions": [
                        {"text": "50", "isCorrect": True},
                        {"text": "30", "isCorrect": False},
                        {"text": "-30", "isCorrect": False},
                        {"text": "400", "isCorrect": False}
                    ],
                    "correction": "x = 40 + 10 = 50."
                },
                {
                    "questionNumber": 43,
                    "question": "Développez l'expression : 2(x + 3)",
                    "answerOptions": [
                        {"text": "2x + 6", "isCorrect": True},
                        {"text": "2x + 3", "isCorrect": False},
                        {"text": "5x", "isCorrect": False},
                        {"text": "x + 6", "isCorrect": False}
                    ],
                    "correction": "On distribue le 2 sur chaque terme de la parenthèse : 2*x + 2*3 = 2x + 6."
                },
                {
                    "questionNumber": 44,
                    "question": "Si x = 5, quelle est la valeur de x² - 10 ?",
                    "answerOptions": [
                        {"text": "15", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "25", "isCorrect": False},
                        {"text": "5", "isCorrect": False}
                    ],
                    "correction": "5² - 10 = 25 - 10 = 15."
                },
                {
                    "questionNumber": 45,
                    "question": "Une fonction affine est du type :",
                    "answerOptions": [
                        {"text": "f(x) = ax + b", "isCorrect": True},
                        {"text": "f(x) = ax", "isCorrect": False},
                        {"text": "f(x) = x²", "isCorrect": False},
                        {"text": "f(x) = a", "isCorrect": False}
                    ],
                    "correction": "Elle est représentée graphiquement par une droite qui ne passe pas forcément par l'origine."
                },
                {
                    "questionNumber": 46,
                    "question": "Résolvez l'équation : 4x = 32",
                    "answerOptions": [
                        {"text": "8", "isCorrect": True},
                        {"text": "28", "isCorrect": False},
                        {"text": "36", "isCorrect": False},
                        {"text": "4", "isCorrect": False}
                    ],
                    "correction": "x = 32 / 4 = 8."
                },
                {
                    "questionNumber": 47,
                    "question": "Que signifie f(2) = 10 ?",
                    "answerOptions": [
                        {"text": "L'image de 2 par la fonction f est 10", "isCorrect": True},
                        {"text": "L'image de 10 par la fonction f est 2", "isCorrect": False},
                        {"text": "f multiplie tout par 5", "isCorrect": False},
                        {"text": "x vaut toujours 10", "isCorrect": False}
                    ],
                    "correction": "Le nombre entre parenthèses est l'antécédent (x), le résultat est l'image (y)."
                },
                {
                    "questionNumber": 48,
                    "question": "Simplifiez : 4a - (2a + 1)",
                    "answerOptions": [
                        {"text": "2a - 1", "isCorrect": True},
                        {"text": "2a + 1", "isCorrect": False},
                        {"text": "6a - 1", "isCorrect": False},
                        {"text": "a", "isCorrect": False}
                    ],
                    "correction": "Le signe '-' devant la parenthèse change tous les signes à l'intérieur : 4a - 2a - 1 = 2a - 1."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est la valeur de x si 3x + 2 = 14 ?",
                    "answerOptions": [
                        {"text": "4", "isCorrect": True},
                        {"text": "12", "isCorrect": False},
                        {"text": "6", "isCorrect": False},
                        {"text": "3", "isCorrect": False}
                    ],
                    "correction": "3x = 14 - 2 = 12. Donc x = 12 / 3 = 4."
                },
                {
                    "questionNumber": 50,
                    "question": "Le prix d'un abonnement est f(x) = 10x + 20. Que représente le 20 ?",
                    "answerOptions": [
                        {"text": "Le coût fixe initial (frais de dossier)", "isCorrect": True},
                        {"text": "Le prix de chaque mois x", "isCorrect": False},
                        {"text": "Le nombre de mois", "isCorrect": False},
                        {"text": "La remise totale", "isCorrect": False}
                    ],
                    "correction": "C'est l'ordonnée à l'origine (la valeur quand x = 0)."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la pente (coefficient directeur) de la fonction f(x) = -2x + 5 ?",
                    "answerOptions": [
                        {"text": "-2", "isCorrect": True},
                        {"text": "5", "isCorrect": False},
                        {"text": "2", "isCorrect": False},
                        {"text": "x", "isCorrect": False}
                    ],
                    "correction": "C'est le coefficient devant le x."
                },
                {
                    "questionNumber": 52,
                    "question": "Factorisez : 5x + 10",
                    "answerOptions": [
                        {"text": "5(x + 2)", "isCorrect": True},
                        {"text": "5(x + 10)", "isCorrect": False},
                        {"text": "15x", "isCorrect": False},
                        {"text": "x(5 + 10)", "isCorrect": False}
                    ],
                    "correction": "On extrait le facteur commun 5."
                },
                {
                    "questionNumber": 53,
                    "question": "Si un article coûte 'p' euros et augmente de 3 euros, son nouveau prix est :",
                    "answerOptions": [
                        {"text": "p + 3", "isCorrect": True},
                        {"text": "3p", "isCorrect": False},
                        {"text": "p - 3", "isCorrect": False},
                        {"text": "p/3", "isCorrect": False}
                    ],
                    "correction": "L'augmentation correspond à une addition."
                },
                {
                    "questionNumber": 54,
                    "question": "Résolvez : 2x + 10 = 0",
                    "answerOptions": [
                        {"text": "-5", "isCorrect": True},
                        {"text": "5", "isCorrect": False},
                        {"text": "-10", "isCorrect": False},
                        {"text": "2", "isCorrect": False}
                    ],
                    "correction": "2x = -10. Donc x = -10 / 2 = -5."
                },
                {
                    "questionNumber": 55,
                    "question": "Complétez : (x + 2)² = ...",
                    "answerOptions": [
                        {"text": "x² + 4x + 4", "isCorrect": True},
                        {"text": "x² + 4", "isCorrect": False},
                        {"text": "x² + 2x + 4", "isCorrect": False},
                        {"text": "2x + 4", "isCorrect": False}
                    ],
                    "correction": "Identité remarquable (a+b)² = a² + 2ab + b²."
                },
                {
                    "questionNumber": 56,
                    "question": "Trouvez x si 5 - x = 2",
                    "answerOptions": [
                        {"text": "3", "isCorrect": True},
                        {"text": "7", "isCorrect": False},
                        {"text": "-3", "isCorrect": False},
                        {"text": "2", "isCorrect": False}
                    ],
                    "correction": "5 - 2 = x, donc x = 3."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est le résultat de 0 × (5x + 12) ?",
                    "answerOptions": [
                        {"text": "0", "isCorrect": True},
                        {"text": "5x + 12", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "5x", "isCorrect": False}
                    ],
                    "correction": "Tout produit par zéro est nul."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment s'appelle l'inconnue dans une équation ?",
                    "answerOptions": [
                        {"text": "La variable (souvent x)", "isCorrect": True},
                        {"text": "Le résultat", "isCorrect": False},
                        {"text": "Le coefficient", "isCorrect": False},
                        {"text": "L'axe", "isCorrect": False}
                    ],
                    "correction": "C'est la valeur que l'on cherche à déterminer."
                },
                {
                    "questionNumber": 59,
                    "question": "Si f(x) = 10, la fonction est dite :",
                    "answerOptions": [
                        {"text": "Constante", "isCorrect": True},
                        {"text": "Linéaire", "isCorrect": False},
                        {"text": "Nulle", "isCorrect": False},
                        {"text": "Croissante", "isCorrect": False}
                    ],
                    "correction": "Elle ne dépend pas de la valeur de x, elle renvoie toujours 10."
                },
                {
                    "questionNumber": 60,
                    "question": "Résolvez : x / 2 = 10",
                    "answerOptions": [
                        {"text": "20", "isCorrect": True},
                        {"text": "5", "isCorrect": False},
                        {"text": "12", "isCorrect": False},
                        {"text": "8", "isCorrect": False}
                    ],
                    "correction": "x = 10 × 2 = 20."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : MESURES, UNITÉS ET CONVERSIONS COMPLEXES (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : MESURES, UNITÉS ET CONVERSIONS COMPLEXES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Combien de centimètres carrés (cm²) y a-t-il dans 1 décimètre carré (dm²) ?",
                    "answerOptions": [
                        {"text": "100 cm²", "isCorrect": True},
                        {"text": "10 cm²", "isCorrect": False},
                        {"text": "1000 cm²", "isCorrect": False},
                        {"text": "1 cm²", "isCorrect": False}
                    ],
                    "correction": "Pour les surfaces, on décale de deux rangs par unité. 1 dm = 10 cm, donc 1 dm² = 10x10 cm² = 100 cm²."
                },
                {
                    "questionNumber": 62,
                    "question": "Combien de litres y a-t-il dans 1 mètre cube (m³) ?",
                    "answerOptions": [
                        {"text": "1 000 litres", "isCorrect": True},
                        {"text": "100 litres", "isCorrect": False},
                        {"text": "10 litres", "isCorrect": False},
                        {"text": "10 000 litres", "isCorrect": False}
                    ],
                    "correction": "Un cube de 1m de côté contient 1000 litres d'eau."
                },
                {
                    "questionNumber": 63,
                    "question": "Convertissez 1,5 kg en milligrammes (mg).",
                    "answerOptions": [
                        {"text": "1 500 000 mg", "isCorrect": True},
                        {"text": "15 000 mg", "isCorrect": False},
                        {"text": "1 500 mg", "isCorrect": False},
                        {"text": "150 000 mg", "isCorrect": False}
                    ],
                    "correction": "1,5 kg = 1500 g = 1 500 000 mg (on multiplie par 1 000 000)."
                },
                {
                    "questionNumber": 64,
                    "question": "Un terrain de 1 hectare (ha) correspond à une surface de :",
                    "answerOptions": [
                        {"text": "10 000 m²", "isCorrect": True},
                        {"text": "1 000 m²", "isCorrect": False},
                        {"text": "100 m²", "isCorrect": False},
                        {"text": "100 000 m²", "isCorrect": False}
                    ],
                    "correction": "C'est l'équivalent d'un carré de 100m de côté."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la masse de 50 cl d'eau pure ?",
                    "answerOptions": [
                        {"text": "500 g", "isCorrect": True},
                        {"text": "50 g", "isCorrect": False},
                        {"text": "5 kg", "isCorrect": False},
                        {"text": "500 kg", "isCorrect": False}
                    ],
                    "correction": "50 cl = 0,5 L. Comme 1 L pèse 1 kg, 0,5 L pèse 0,5 kg, soit 500 g."
                },
                {
                    "questionNumber": 66,
                    "question": "Convertissez 2h 15min en minutes totales.",
                    "answerOptions": [
                        {"text": "135 minutes", "isCorrect": True},
                        {"text": "215 minutes", "isCorrect": False},
                        {"text": "120 minutes", "isCorrect": False},
                        {"text": "150 minutes", "isCorrect": False}
                    ],
                    "correction": "2 × 60 + 15 = 120 + 15 = 135 minutes."
                },
                {
                    "questionNumber": 67,
                    "question": "Une vitesse de 10 m/s correspond à combien de km/h ?",
                    "answerOptions": [
                        {"text": "36 km/h", "isCorrect": True},
                        {"text": "10 km/h", "isCorrect": False},
                        {"text": "60 km/h", "isCorrect": False},
                        {"text": "3,6 km/h", "isCorrect": False}
                    ],
                    "correction": "Pour passer des m/s aux km/h, on multiplie par 3,6. 10 × 3,6 = 36."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle est la capacité d'une canette de soda classique ?",
                    "answerOptions": [
                        {"text": "33 cl", "isCorrect": True},
                        {"text": "33 ml", "isCorrect": False},
                        {"text": "3,3 L", "isCorrect": False},
                        {"text": "33 dl", "isCorrect": False}
                    ],
                    "correction": "C'est l'unité de mesure standard pour les boissons individuelles."
                },
                {
                    "questionNumber": 69,
                    "question": "Combien y a-t-il de secondes dans une heure ?",
                    "answerOptions": [
                        {"text": "3 600 s", "isCorrect": True},
                        {"text": "60 s", "isCorrect": False},
                        {"text": "1 000 s", "isCorrect": False},
                        {"text": "120 s", "isCorrect": False}
                    ],
                    "correction": "60 minutes × 60 secondes = 3600."
                },
                {
                    "questionNumber": 70,
                    "question": "Un angle droit est partagé en deux angles égaux. Quelle est leur mesure ?",
                    "answerOptions": [
                        {"text": "45°", "isCorrect": True},
                        {"text": "90°", "isCorrect": False},
                        {"text": "20°", "isCorrect": False},
                        {"text": "30°", "isCorrect": False}
                    ],
                    "correction": "90 / 2 = 45°."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est le volume d'une piscine de 10m de long, 5m de large et 2m de profondeur ?",
                    "answerOptions": [
                        {"text": "100 m³", "isCorrect": True},
                        {"text": "50 m³", "isCorrect": False},
                        {"text": "17 m³", "isCorrect": False},
                        {"text": "200 m³", "isCorrect": False}
                    ],
                    "correction": "10 × 5 × 2 = 100 m³."
                },
                {
                    "questionNumber": 72,
                    "question": "Combien de mm² y a-t-il dans 1 cm² ?",
                    "answerOptions": [
                        {"text": "100 mm²", "isCorrect": True},
                        {"text": "10 mm²", "isCorrect": False},
                        {"text": "1 000 mm²", "isCorrect": False},
                        {"text": "0,1 mm²", "isCorrect": False}
                    ],
                    "correction": "On passe d'une unité à la suivante en multipliant par 100 (deux zéros)."
                },
                {
                    "questionNumber": 73,
                    "question": "Convertissez 750 ml en litres.",
                    "answerOptions": [
                        {"text": "0,75 L", "isCorrect": True},
                        {"text": "7,5 L", "isCorrect": False},
                        {"text": "75 L", "isCorrect": False},
                        {"text": "0,075 L", "isCorrect": False}
                    ],
                    "correction": "On divise par 1 000 pour passer des millilitres aux litres."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le poids approximatif sur Terre d'une masse de 10 kg ?",
                    "answerOptions": [
                        {"text": "100 N", "isCorrect": True},
                        {"text": "10 N", "isCorrect": False},
                        {"text": "1 N", "isCorrect": False},
                        {"text": "1000 N", "isCorrect": False}
                    ],
                    "correction": "P = m × g. Avec g ≈ 10 N/kg. P = 10 × 10 = 100 N."
                },
                {
                    "questionNumber": 75,
                    "question": "Convertissez 0,25 h en minutes.",
                    "answerOptions": [
                        {"text": "15 minutes", "isCorrect": True},
                        {"text": "25 minutes", "isCorrect": False},
                        {"text": "5 minutes", "isCorrect": False},
                        {"text": "20 minutes", "isCorrect": False}
                    ],
                    "correction": "0,25 × 60 = 15 minutes (soit un quart d'heure)."
                },
                {
                    "questionNumber": 76,
                    "question": "Une bouteille de 1,5 L contient combien de verres de 20 cl ?",
                    "answerOptions": [
                        {"text": "7,5 verres", "isCorrect": True},
                        {"text": "5 verres", "isCorrect": False},
                        {"text": "10 verres", "isCorrect": False},
                        {"text": "15 verres", "isCorrect": False}
                    ],
                    "correction": "1,5 L = 150 cl. 150 / 20 = 7,5."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le périmètre d'un carré d'aire 16 cm² ?",
                    "answerOptions": [
                        {"text": "16 cm", "isCorrect": True},
                        {"text": "4 cm", "isCorrect": False},
                        {"text": "8 cm", "isCorrect": False},
                        {"text": "20 cm", "isCorrect": False}
                    ],
                    "correction": "Le côté vaut √16 = 4 cm. Le périmètre est 4 × 4 = 16 cm."
                },
                {
                    "questionNumber": 78,
                    "question": "Combien de mètres y a-t-il dans un mile (unité anglo-saxonne environ) ?",
                    "answerOptions": [
                        {"text": "1 609 m", "isCorrect": True},
                        {"text": "1 000 m", "isCorrect": False},
                        {"text": "500 m", "isCorrect": False},
                        {"text": "2 000 m", "isCorrect": False}
                    ],
                    "correction": "C'est une unité de distance encore utilisée aux USA et au Royaume-Uni."
                },
                {
                    "questionNumber": 79,
                    "question": "Que vaut la pression atmosphérique normale en Bars ?",
                    "answerOptions": [
                        {"text": "Environ 1 bar", "isCorrect": True},
                        {"text": "10 bars", "isCorrect": False},
                        {"text": "0 bar", "isCorrect": False},
                        {"text": "100 bars", "isCorrect": False}
                    ],
                    "correction": "Précisément 1,013 bar."
                },
                {
                    "questionNumber": 80,
                    "question": "Convertissez 1 m² en cm².",
                    "answerOptions": [
                        {"text": "10 000 cm²", "isCorrect": True},
                        {"text": "100 cm²", "isCorrect": False},
                        {"text": "1 000 cm²", "isCorrect": False},
                        {"text": "10 cm²", "isCorrect": False}
                    ],
                    "correction": "1 m = 100 cm. Donc 1 m² = 100 × 100 = 10 000 cm²."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : STATISTIQUES ET PROBABILITÉS (Q81 à Q100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : STATISTIQUES ET PROBABILITÉS",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la probabilité d'obtenir un '6' avec un dé équilibré à 6 faces ?",
                    "answerOptions": [
                        {"text": "1/6", "isCorrect": True},
                        {"text": "1/2", "isCorrect": False},
                        {"text": "6/6", "isCorrect": False},
                        {"text": "0", "isCorrect": False}
                    ],
                    "correction": "Il y a un seul cas favorable sur 6 cas possibles."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment s'appelle le graphique qui représente l'évolution d'une donnée dans le temps ?",
                    "answerOptions": [
                        {"text": "Une courbe (ou diagramme cartésien)", "isCorrect": True},
                        {"text": "Un diagramme circulaire", "isCorrect": False},
                        {"text": "Un histogramme", "isCorrect": False},
                        {"text": "Un tableau", "isCorrect": False}
                    ],
                    "correction": "Les points sont reliés entre eux pour montrer la tendance (hausse, baisse)."
                },
                {
                    "questionNumber": 83,
                    "question": "Dans un sac de 10 boules dont 3 sont rouges, quelle est la probabilité de tirer une boule rouge ?",
                    "answerOptions": [
                        {"text": "0,3 (ou 3/10)", "isCorrect": True},
                        {"text": "3", "isCorrect": False},
                        {"text": "0,7", "isCorrect": False},
                        {"text": "1/3", "isCorrect": False}
                    ],
                    "correction": "Probabilité = Nombre de cas favorables / Nombre de cas total."
                },
                {
                    "questionNumber": 84,
                    "question": "Que signifie la 'médiane' d'une série ?",
                    "answerOptions": [
                        {"text": "La valeur qui partage la série en deux groupes de même effectif", "isCorrect": True},
                        {"text": "La valeur la plus grande", "isCorrect": False},
                        {"text": "La moyenne de toutes les valeurs", "isCorrect": False},
                        {"text": "La valeur qui apparaît le plus souvent", "isCorrect": False}
                    ],
                    "correction": "50 % des données sont inférieures ou égales à la médiane, et 50 % sont supérieures."
                },
                {
                    "questionNumber": 85,
                    "question": "Si l'on lance une pièce de monnaie, quelle est la probabilité de faire 'Pile' ?",
                    "answerOptions": [
                        {"text": "0,5 (ou 1/2)", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "0", "isCorrect": False},
                        {"text": "0,25", "isCorrect": False}
                    ],
                    "correction": "Il y a 50 % de chances."
                },
                {
                    "questionNumber": 86,
                    "question": "Dans une classe de 20 élèves, 5 sont absents. Quel est le pourcentage d'absents ?",
                    "answerOptions": [
                        {"text": "25 %", "isCorrect": True},
                        {"text": "5 %", "isCorrect": False},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "50 %", "isCorrect": False}
                    ],
                    "correction": "(5 / 20) × 100 = 0,25 × 100 = 25 %."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment appelle-t-on un événement qui ne peut pas se produire ?",
                    "answerOptions": [
                        {"text": "Un événement impossible", "isCorrect": True},
                        {"text": "Un événement certain", "isCorrect": False},
                        {"text": "Un événement probable", "isCorrect": False},
                        {"text": "Un événement nul", "isCorrect": False}
                    ],
                    "correction": "Sa probabilité est égale à 0."
                },
                {
                    "questionNumber": 88,
                    "question": "Un événement certain a une probabilité de :",
                    "answerOptions": [
                        {"text": "1 (ou 100 %)", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False},
                        {"text": "99 %", "isCorrect": False}
                    ],
                    "correction": "Cela signifie qu'il va forcément arriver."
                },
                {
                    "questionNumber": 89,
                    "question": "Que signifie un diagramme circulaire où un secteur fait 90° ?",
                    "answerOptions": [
                        {"text": "Cette catégorie représente 25 % du total", "isCorrect": True},
                        {"text": "Cette catégorie représente 90 %", "isCorrect": False},
                        {"text": "C'est la moitié du total", "isCorrect": False},
                        {"text": "C'est une erreur de dessin", "isCorrect": False}
                    ],
                    "correction": "Un cercle fait 360°. 90 / 360 = 1/4 = 25 %."
                },
                {
                    "questionNumber": 90,
                    "question": "Calculer la moyenne de : 8 ; 10 ; 12 ; 10.",
                    "answerOptions": [
                        {"text": "10", "isCorrect": True},
                        {"text": "40", "isCorrect": False},
                        {"text": "9", "isCorrect": False},
                        {"text": "11", "isCorrect": False}
                    ],
                    "correction": "(8 + 10 + 12 + 10) / 4 = 40 / 4 = 10."
                },
                {
                    "questionNumber": 91,
                    "question": "Qu'est-ce que la 'fréquence cumulée croissant' ?",
                    "answerOptions": [
                        {"text": "La somme des fréquences au fur et à mesure", "isCorrect": True},
                        {"text": "Le prix total des produits", "isCorrect": False},
                        {"text": "La fréquence la plus haute", "isCorrect": False},
                        {"text": "Une erreur de calcul", "isCorrect": False}
                    ],
                    "correction": "La dernière fréquence cumulée doit toujours être égale à 1 (ou 100%)."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le but d'un sondage ?",
                    "answerOptions": [
                        {"text": "Interroger une partie de la population pour connaître l'opinion globale", "isCorrect": True},
                        {"text": "Compter exactement chaque habitant un par un", "isCorrect": False},
                        {"text": "Donner de l'argent aux gens", "isCorrect": False},
                        {"text": "Vérifier l'orthographe des noms", "isCorrect": False}
                    ],
                    "correction": "On utilise un échantillon représentatif."
                },
                {
                    "questionNumber": 93,
                    "question": "Si la probabilité qu'il pleuve est de 0,3, quelle est la probabilité qu'il ne pleuve pas ?",
                    "answerOptions": [
                        {"text": "0,7", "isCorrect": True},
                        {"text": "0,3", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "0", "isCorrect": False}
                    ],
                    "correction": "La somme des probabilités d'un événement et de son contraire vaut 1. (1 - 0,3 = 0,7)."
                },
                {
                    "questionNumber": 94,
                    "question": "Le caractère d'une étude est dit 'quantitatif' s'il est :",
                    "answerOptions": [
                        {"text": "Mesurable par un nombre (âge, taille, prix)", "isCorrect": True},
                        {"text": "Une qualité (couleur, marque, sexe)", "isCorrect": False},
                        {"text": "Très important", "isCorrect": False},
                        {"text": "Faux", "isCorrect": False}
                    ],
                    "correction": "Opposé au caractère qualitatif."
                },
                {
                    "questionNumber": 95,
                    "question": "Que représente le 'mode' en statistique ?",
                    "answerOptions": [
                        {"text": "La valeur qui a le plus grand effectif", "isCorrect": True},
                        {"text": "La plus petite valeur", "isCorrect": False},
                        {"text": "La moyenne", "isCorrect": False},
                        {"text": "La somme des données", "isCorrect": False}
                    ],
                    "correction": "C'est la donnée la plus courante dans l'échantillon."
                },
                {
                    "questionNumber": 96,
                    "question": "Pourquoi la moyenne est-elle parfois trompeuse ?",
                    "answerOptions": [
                        {"text": "Elle est sensible aux valeurs extrêmes", "isCorrect": True},
                        {"text": "Elle est trop difficile à calculer", "isCorrect": False},
                        {"text": "Elle donne toujours le même résultat", "isCorrect": False},
                        {"text": "Elle n'existe pas en mathématiques", "isCorrect": False}
                    ],
                    "correction": "Un seul très gros salaire peut faire monter la moyenne d'une entreprise, alors que la majorité gagne peu."
                },
                {
                    "questionNumber": 97,
                    "question": "Une expérience est dite 'aléatoire' si :",
                    "answerOptions": [
                        {"text": "On ne peut pas prévoir avec certitude son résultat", "isCorrect": True},
                        {"text": "On connaît le résultat avant de commencer", "isCorrect": False},
                        {"text": "Elle ne dépend que de la compétence du joueur", "isCorrect": False},
                        {"text": "Elle donne toujours le même résultat à chaque fois", "isCorrect": False}
                    ],
                    "correction": "L'aléatoire (du latin alea, jeu de dés) implique une part d'incertitude."
                },
                {
                    "questionNumber": 98,
                    "question": "Comment appelle-t-on l'ensemble des individus sur lesquels porte une étude statistique ?",
                    "answerOptions": [
                        {"text": "La population", "isCorrect": True},
                        {"text": "L'échantillon", "isCorrect": False},
                        {"text": "Le caractère", "isCorrect": False},
                        {"text": "La série", "isCorrect": False}
                    ],
                    "correction": "La population est le groupe global étudié. L'échantillon en est une partie."
                },
                {
                    "questionNumber": 99,
                    "question": "Si la fréquence d'un événement est 0,125, quel est son pourcentage ?",
                    "answerOptions": [
                        {"text": "12,5 %", "isCorrect": True},
                        {"text": "1,25 %", "isCorrect": False},
                        {"text": "125 %", "isCorrect": False},
                        {"text": "0,125 %", "isCorrect": False}
                    ],
                    "correction": "On multiplie par 100 : 0,125 × 100 = 12,5 %."
                },
                {
                    "questionNumber": 100,
                    "question": "Que signifie 'tirage sans remise' ?",
                    "answerOptions": [
                        {"text": "On ne remet pas l'objet tiré dans l'urne", "isCorrect": True},
                        {"text": "On remet l'objet immédiatement", "isCorrect": False},
                        {"text": "On ne gagne pas de cadeau", "isCorrect": False},
                        {"text": "On tire plusieurs objets en même temps", "isCorrect": False}
                    ],
                    "correction": "Cela modifie les probabilités des tirages suivants."
                }
            ]
        }
    }
}