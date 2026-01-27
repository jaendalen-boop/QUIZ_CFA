quiz_data = {
    "title": "Quiz Bac Pro Mathématiques (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : STATISTIQUE DESCRIPTIVE ET PROBABILITÉS (Q1 à Q20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : STATISTIQUE DESCRIPTIVE ET PROBABILITÉS",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Dans une série statistique, comment appelle-t-on la valeur qui sépare la population en deux effectifs égaux ?",
                    "answerOptions": [
                        {"text": "La médiane", "isCorrect": True},
                        {"text": "La moyenne arithmétique de la série", "isCorrect": False},
                        {"text": "Le premier quartile de la distribution", "isCorrect": False},
                        {"text": "L'étendue globale de la série étudiée", "isCorrect": False}
                    ],
                    "correction": "La médiane divise une série ordonnée en deux groupes de même effectif : 50% des valeurs sont inférieures ou égales et 50% sont supérieures ou égales."
                },
                {
                    "questionNumber": 2,
                    "question": "On lance un dé équilibré à six faces. Quelle est la probabilité d'obtenir un chiffre pair ?",
                    "answerOptions": [
                        {"text": "0,5", "isCorrect": True},
                        {"text": "La probabilité est de un tiers", "isCorrect": False},
                        {"text": "On a deux chances sur six d'obtenir ce résultat", "isCorrect": False},
                        {"text": "Il existe une chance sur six d'obtenir un chiffre pair", "isCorrect": False}
                    ],
                    "correction": "Il y a 3 chiffres pairs (2, 4, 6) sur un total de 6 faces, soit une probabilité de 3/6 = 0,5 (ou 50%)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle formule permet de calculer l'étendue d'une série statistique ?",
                    "answerOptions": [
                        {"text": "Valeur max moins valeur min", "isCorrect": True},
                        {"text": "Somme des valeurs divisée par l'effectif total", "isCorrect": False},
                        {"text": "Valeur du troisième quartile moins le premier", "isCorrect": False},
                        {"text": "La valeur la plus haute de la série divisée par deux", "isCorrect": False}
                    ],
                    "correction": "L'étendue est l'écart entre les deux valeurs extrêmes de la série. Elle mesure la dispersion totale."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment appelle-t-on le quotient de l'effectif d'une valeur par l'effectif total ?",
                    "answerOptions": [
                        {"text": "La fréquence", "isCorrect": True},
                        {"text": "Le pourcentage de la valeur", "isCorrect": False},
                        {"text": "La variance", "isCorrect": False},
                        {"text": "L'écart-type", "isCorrect": False}
                    ],
                    "correction": "La fréquence f est égale à n/N. Elle est comprise entre 0 et 1 (souvent exprimée en %)."
                },
                {
                    "questionNumber": 5,
                    "question": "Dans un diagramme en boîte (boîte à moustaches), que représente la boîte centrale ?",
                    "answerOptions": [
                        {"text": "L'intervalle interquartile [Q1 ; Q3]", "isCorrect": True},
                        {"text": "L'étendue globale", "isCorrect": False},
                        {"text": "La valeur de la moyenne", "isCorrect": False},
                        {"text": "L'écart entre le minimum et le maximum", "isCorrect": False}
                    ],
                    "correction": "La boîte centrale contient les 50% centraux de la population, allant du premier au troisième quartile."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la probabilité d'un événement certain ?",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "100", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False}
                    ],
                    "correction": "La probabilité d'un événement qui se réalise forcément est égale à 1 (ou 100%)."
                },
                {
                    "questionNumber": 7,
                    "question": "Si deux événements A et B sont incompatibles, quelle est la probabilité de (A ou B) ?",
                    "answerOptions": [
                        {"text": "P(A) + P(B)", "isCorrect": True},
                        {"text": "P(A) fois P(B)", "isCorrect": False},
                        {"text": "P(A) moins P(B)", "isCorrect": False},
                        {"text": "Zéro", "isCorrect": False}
                    ],
                    "correction": "Deux événements sont incompatibles s'ils ne peuvent pas se produire en même temps. La probabilité que l'un ou l'autre se réalise est la somme de leurs probabilités."
                },
                {
                    "questionNumber": 8,
                    "question": "Comment calcule-t-on la moyenne arithmétique ?",
                    "answerOptions": [
                        {"text": "Somme des valeurs / effectif total", "isCorrect": True},
                        {"text": "Effectif total / somme des valeurs", "isCorrect": False},
                        {"text": "Valeur max + valeur min / 2", "isCorrect": False},
                        {"text": "La valeur centrale", "isCorrect": False}
                    ],
                    "correction": "La moyenne est le point d'équilibre de la série statistique."
                },
                {
                    "questionNumber": 9,
                    "question": "Que mesure l'écart-type d'une série ?",
                    "answerOptions": [
                        {"text": "La dispersion des valeurs autour de la moyenne", "isCorrect": True},
                        {"text": "Le milieu de la série", "isCorrect": False},
                        {"text": "La valeur la plus fréquente", "isCorrect": False},
                        {"text": "La somme totale", "isCorrect": False}
                    ],
                    "correction": "Plus l'écart-type est petit, plus les données sont regroupées autour de la moyenne."
                },
                {
                    "questionNumber": 10,
                    "question": "Le premier quartile Q1 correspond à quelle part de l'effectif total ?",
                    "answerOptions": [
                        {"text": "Au moins 25%", "isCorrect": True},
                        {"text": "Exactement 50%", "isCorrect": False},
                        {"text": "Au moins 75%", "isCorrect": False},
                        {"text": "La totalité", "isCorrect": False}
                    ],
                    "correction": "Au moins 25% des données sont inférieures ou égales à Q1."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la probabilité de tirer un 'As' dans un jeu de 32 cartes ?",
                    "answerOptions": [
                        {"text": "4/32 (soit 0,125)", "isCorrect": True},
                        {"text": "1/32", "isCorrect": False},
                        {"text": "4/52", "isCorrect": False},
                        {"text": "0,25", "isCorrect": False}
                    ],
                    "correction": "Il y a 4 as dans un jeu de 32 cartes."
                },
                {
                    "questionNumber": 12,
                    "question": "Qu'est-ce qu'une expérience aléatoire ?",
                    "answerOptions": [
                        {"text": "Une expérience dont on ne peut pas prévoir le résultat", "isCorrect": True},
                        {"text": "Une expérience de laboratoire scientifique", "isCorrect": False},
                        {"text": "Un calcul mathématique complexe", "isCorrect": False},
                        {"text": "Une mesure avec une règle", "isCorrect": False}
                    ],
                    "correction": "On connaît les issues possibles mais pas laquelle va sortir (ex: lancer un dé)."
                },
                {
                    "questionNumber": 13,
                    "question": "La somme des probabilités de toutes les issues d'une expérience vaut toujours :",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "100", "isCorrect": False},
                        {"text": "Variable", "isCorrect": False}
                    ],
                    "correction": "C'est une loi fondamentale des probabilités."
                },
                {
                    "questionNumber": 14,
                    "question": "Que signifie un échantillon représentatif ?",
                    "answerOptions": [
                        {"text": "Une partie de la population qui possède les mêmes caractéristiques", "isCorrect": True},
                        {"text": "Le groupe le plus nombreux possible", "isCorrect": False},
                        {"text": "Uniquement les personnes qui sont d'accord", "isCorrect": False},
                        {"text": "Une sélection au hasard total sans critères", "isCorrect": False}
                    ],
                    "correction": "Il permet de généraliser les résultats du sondage à toute la population."
                },
                {
                    "questionNumber": 15,
                    "question": "Sur un diagramme circulaire, l'angle de chaque secteur est proportionnel à :",
                    "answerOptions": [
                        {"text": "L'effectif ou la fréquence", "isCorrect": True},
                        {"text": "La valeur de la donnée", "isCorrect": False},
                        {"text": "La moyenne de la série", "isCorrect": False},
                        {"text": "Rien du tout", "isCorrect": False}
                    ],
                    "correction": "Angle = Fréquence x 360°."
                },
                {
                    "questionNumber": 16,
                    "question": "Comment calcule-t-on le troisième quartile Q3 ?",
                    "answerOptions": [
                        {"text": "C'est la valeur pour laquelle au moins 75% des données sont inférieures", "isCorrect": True},
                        {"text": "C'est la valeur du milieu", "isCorrect": False},
                        {"text": "C'est la moyenne plus l'écart-type", "isCorrect": False},
                        {"text": "C'est 3 fois la valeur de Q1", "isCorrect": False}
                    ],
                    "correction": "On classe les données par ordre croissant pour le trouver."
                },
                {
                    "questionNumber": 17,
                    "question": "Un événement A a une probabilité de 0,3. Quelle est la probabilité de son contraire ?",
                    "answerOptions": [
                        {"text": "0,7", "isCorrect": True},
                        {"text": "0,3", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "-0,3", "isCorrect": False}
                    ],
                    "correction": "P(non A) = 1 - P(A) = 1 - 0,3 = 0,7."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la définition du mode d'une série ?",
                    "answerOptions": [
                        {"text": "La valeur qui a le plus grand effectif", "isCorrect": True},
                        {"text": "La moyenne des valeurs extrêmes", "isCorrect": False},
                        {"text": "La différence entre Q3 et Q1", "isCorrect": False},
                        {"text": "La valeur la plus petite", "isCorrect": False}
                    ],
                    "correction": "On l'appelle aussi 'dominante'."
                },
                {
                    "questionNumber": 19,
                    "question": "Qu'est-ce qu'une variable qualitative ?",
                    "answerOptions": [
                        {"text": "Une donnée qui n'est pas un nombre (ex: couleur, marque)", "isCorrect": True},
                        {"text": "Une donnée avec beaucoup de chiffres après la virgule", "isCorrect": False},
                        {"text": "Le prix d'un article", "isCorrect": False},
                        {"text": "La durée d'un trajet", "isCorrect": False}
                    ],
                    "correction": "Par opposition à une variable quantitative (mesurable)."
                },
                {
                    "questionNumber": 20,
                    "question": "Si on lance deux fois une pièce, combien y a-t-il d'issues possibles ?",
                    "answerOptions": [
                        {"text": "4", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "8", "isCorrect": False},
                        {"text": "3", "isCorrect": False}
                    ],
                    "correction": "Issues : (P,P), (P,F), (F,P), (F,F)."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : ALGÈBRE ET FONCTIONS (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : ALGÈBRE ET FONCTIONS",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la forme générale d'une fonction affine ?",
                    "answerOptions": [
                        {"text": "f(x) = ax + b", "isCorrect": True},
                        {"text": "f(x) = ax²", "isCorrect": False},
                        {"text": "f(x) = a/x", "isCorrect": False},
                        {"text": "f(x) = x + b²", "isCorrect": False}
                    ],
                    "correction": "La représentation graphique d'une fonction affine est une droite."
                },
                {
                    "questionNumber": 22,
                    "question": "Que représente 'a' dans l'expression f(x) = ax + b ?",
                    "answerOptions": [
                        {"text": "Le coefficient directeur (la pente)", "isCorrect": True},
                        {"text": "L'ordonnée à l'origine", "isCorrect": False},
                        {"text": "L'image de zéro", "isCorrect": False},
                        {"text": "L'inconnue", "isCorrect": False}
                    ],
                    "correction": "Il indique l'inclinaison de la droite."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la particularité d'une fonction linéaire ?",
                    "answerOptions": [
                        {"text": "Sa droite passe par l'origine (0 ; 0)", "isCorrect": True},
                        {"text": "Elle est toujours décroissante", "isCorrect": False},
                        {"text": "Elle forme une courbe en U", "isCorrect": False},
                        {"text": "Elle n'a pas de coefficient directeur", "isCorrect": False}
                    ],
                    "correction": "Une fonction linéaire est du type f(x) = ax (b est nul)."
                },
                {
                    "questionNumber": 24,
                    "question": "Dans f(x) = 2x - 5, quelle est l'ordonnée à l'origine ?",
                    "answerOptions": [
                        {"text": "-5", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "0", "isCorrect": False},
                        {"text": "x", "isCorrect": False}
                    ],
                    "correction": "C'est la valeur de f(0), ici le terme constant 'b'."
                },
                {
                    "questionNumber": 25,
                    "question": "Résoudre l'équation 3x + 2 = 11.",
                    "answerOptions": [
                        {"text": "x = 3", "isCorrect": True},
                        {"text": "x = 4", "isCorrect": False},
                        {"text": "x = 9", "isCorrect": False},
                        {"text": "x = 33", "isCorrect": False}
                    ],
                    "correction": "3x = 11 - 2 => 3x = 9 => x = 9/3 = 3."
                },
                {
                    "questionNumber": 26,
                    "question": "Si a > 0, la fonction f(x) = ax + b est :",
                    "answerOptions": [
                        {"text": "Croissante", "isCorrect": True},
                        {"text": "Décroissante", "isCorrect": False},
                        {"text": "Constante", "isCorrect": False},
                        {"text": "Nulle", "isCorrect": False}
                    ],
                    "correction": "La valeur de x et de f(x) augmentent ensemble."
                },
                {
                    "questionNumber": 27,
                    "question": "Que signifie graphiquement résoudre f(x) = g(x) ?",
                    "answerOptions": [
                        {"text": "Chercher l'abscisse du point d'intersection des deux courbes", "isCorrect": True},
                        {"text": "Additionner les deux fonctions", "isCorrect": False},
                        {"text": "Multiplier les ordonnées", "isCorrect": False},
                        {"text": "Tracer une droite parallèle", "isCorrect": False}
                    ],
                    "correction": "C'est trouver le point où les deux fonctions ont la même valeur."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la valeur de x pour laquelle 2x = 0 ?",
                    "answerOptions": [
                        {"text": "0", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "-2", "isCorrect": False},
                        {"text": "Impossible", "isCorrect": False}
                    ],
                    "correction": "x = 0/2 = 0."
                },
                {
                    "questionNumber": 29,
                    "question": "Développer l'expression 4(x - 3).",
                    "answerOptions": [
                        {"text": "4x - 12", "isCorrect": True},
                        {"text": "4x - 3", "isCorrect": False},
                        {"text": "x - 12", "isCorrect": False},
                        {"text": "4x + 12", "isCorrect": False}
                    ],
                    "correction": "On utilise la distributivité : 4*x - 4*3."
                },
                {
                    "questionNumber": 30,
                    "question": "Un produit coûte x €. Son prix augmente de 20%. Quelle est l'expression du nouveau prix ?",
                    "answerOptions": [
                        {"text": "1,20x", "isCorrect": True},
                        {"text": "x + 20", "isCorrect": False},
                        {"text": "0,20x", "isCorrect": False},
                        {"text": "x + 1,20", "isCorrect": False}
                    ],
                    "correction": "Augmenter de 20% revient à multiplier par (1 + 20/100) = 1,20."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est l'inverse de 5 ?",
                    "answerOptions": [
                        {"text": "1/5 (ou 0,2)", "isCorrect": True},
                        {"text": "-5", "isCorrect": False},
                        {"text": "5", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False}
                    ],
                    "correction": "L'inverse d'un nombre n est 1/n."
                },
                {
                    "questionNumber": 32,
                    "question": "Que vaut x² si x = -3 ?",
                    "answerOptions": [
                        {"text": "9", "isCorrect": True},
                        {"text": "-9", "isCorrect": False},
                        {"text": "6", "isCorrect": False},
                        {"text": "-6", "isCorrect": False}
                    ],
                    "correction": "(-3) * (-3) = 9. Un carré est toujours positif."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la solution de 5x = 10 ?",
                    "answerOptions": [
                        {"text": "2", "isCorrect": True},
                        {"text": "5", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False},
                        {"text": "50", "isCorrect": False}
                    ],
                    "correction": "x = 10/5 = 2."
                },
                {
                    "questionNumber": 34,
                    "question": "Une fonction constante est représentée par :",
                    "answerOptions": [
                        {"text": "Une droite horizontale", "isCorrect": True},
                        {"text": "Une droite verticale", "isCorrect": False},
                        {"text": "Une droite passant par l'origine", "isCorrect": False},
                        {"text": "Une courbe", "isCorrect": False}
                    ],
                    "correction": "La valeur de y ne change pas quel que soit x."
                },
                {
                    "questionNumber": 35,
                    "question": "Résoudre x + 7 = 3.",
                    "answerOptions": [
                        {"text": "x = -4", "isCorrect": True},
                        {"text": "x = 4", "isCorrect": False},
                        {"text": "x = 10", "isCorrect": False},
                        {"text": "x = -10", "isCorrect": False}
                    ],
                    "correction": "x = 3 - 7 = -4."
                },
                {
                    "questionNumber": 36,
                    "question": "Que signifie 'isoler l'inconnue' ?",
                    "answerOptions": [
                        {"text": "Faire en sorte que x soit seul d'un côté de l'égal", "isCorrect": True},
                        {"text": "Supprimer le x de l'équation", "isCorrect": False},
                        {"text": "Remplacer x par zéro", "isCorrect": False},
                        {"text": "Changer le nom de la variable", "isCorrect": False}
                    ],
                    "correction": "C'est l'étape finale de la résolution d'une équation."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle est l'image de 3 par la fonction f(x) = 4x - 1 ?",
                    "answerOptions": [
                        {"text": "11", "isCorrect": True},
                        {"text": "12", "isCorrect": False},
                        {"text": "8", "isCorrect": False},
                        {"text": "2", "isCorrect": False}
                    ],
                    "correction": "f(3) = 4*3 - 1 = 12 - 1 = 11."
                },
                {
                    "questionNumber": 38,
                    "question": "Le point A(2 ; 5) appartient-il à la droite y = 2x + 1 ?",
                    "answerOptions": [
                        {"text": "Oui", "isCorrect": True},
                        {"text": "Non", "isCorrect": False},
                        {"text": "On ne peut pas savoir", "isCorrect": False},
                        {"text": "Seulement si x est positif", "isCorrect": False}
                    ],
                    "correction": "Si on remplace x par 2 : 2*2 + 1 = 5. L'égalité est vérifiée."
                },
                {
                    "questionNumber": 39,
                    "question": "Factoriser x² + 3x.",
                    "answerOptions": [
                        {"text": "x(x + 3)", "isCorrect": True},
                        {"text": "3(x + 1)", "isCorrect": False},
                        {"text": "x²(1 + 3)", "isCorrect": False},
                        {"text": "2x + 3", "isCorrect": False}
                    ],
                    "correction": "On extrait le facteur commun x."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est l'unité de pente d'une route à 10% ?",
                    "answerOptions": [
                        {"text": "Elle monte de 10m pour 100m horizontaux", "isCorrect": True},
                        {"text": "Elle fait un angle de 10 degrés", "isCorrect": False},
                        {"text": "Elle mesure 10 km de long", "isCorrect": False},
                        {"text": "Elle est réservée aux véhicules de 10 tonnes", "isCorrect": False}
                    ],
                    "correction": "C'est le rapport hauteur / distance horizontale."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : GÉOMÉTRIE (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : GÉOMÉTRIE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la somme des angles d'un triangle ?",
                    "answerOptions": [
                        {"text": "180°", "isCorrect": True},
                        {"text": "90°", "isCorrect": False},
                        {"text": "360°", "isCorrect": False},
                        {"text": "100°", "isCorrect": False}
                    ],
                    "correction": "Cette propriété est vraie pour tous les triangles (quelconques, rectangles, etc.)."
                },
                {
                    "questionNumber": 42,
                    "question": "Comment calcule-t-on le périmètre d'un cercle ?",
                    "answerOptions": [
                        {"text": "2 × π × R", "isCorrect": True},
                        {"text": "π × R²", "isCorrect": False},
                        {"text": "Côté × 4", "isCorrect": False},
                        {"text": "Diamètre / π", "isCorrect": False}
                    ],
                    "correction": "On peut aussi utiliser π × D (diamètre)."
                },
                {
                    "questionNumber": 43,
                    "question": "Le théorème de Pythagore s'applique dans un triangle :",
                    "answerOptions": [
                        {"text": "Rectangle", "isCorrect": True},
                        {"text": "Isocèle", "isCorrect": False},
                        {"text": "Équilatéral", "isCorrect": False},
                        {"text": "Quelconque", "isCorrect": False}
                    ],
                    "correction": "Il permet de calculer la longueur d'un côté quand on connaît les deux autres."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est l'aire d'un disque de rayon R ?",
                    "answerOptions": [
                        {"text": "π × R²", "isCorrect": True},
                        {"text": "2 × π × R", "isCorrect": False},
                        {"text": "R × R", "isCorrect": False},
                        {"text": "4/3 × π × R³", "isCorrect": False}
                    ],
                    "correction": "On multiplie Pi par le carré du rayon."
                },
                {
                    "questionNumber": 45,
                    "question": "Dans un triangle rectangle, le sinus d'un angle est égal à :",
                    "answerOptions": [
                        {"text": "Côté opposé / Hypoténuse", "isCorrect": True},
                        {"text": "Côté adjacent / Hypoténuse", "isCorrect": False},
                        {"text": "Côté opposé / Côté adjacent", "isCorrect": False},
                        {"text": "Hypoténuse / Côté opposé", "isCorrect": False}
                    ],
                    "correction": "Moyen mnémotechnique : SOH CAH TOA."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la définition de l'hypoténuse ?",
                    "answerOptions": [
                        {"text": "Le côté le plus long d'un triangle rectangle", "isCorrect": True},
                        {"text": "La hauteur d'un triangle", "isCorrect": False},
                        {"text": "Un angle de 90°", "isCorrect": False},
                        {"text": "Le côté situé à côté de l'angle droit", "isCorrect": False}
                    ],
                    "correction": "C'est le côté opposé à l'angle droit."
                },
                {
                    "questionNumber": 47,
                    "question": "Un litre est équivalent à :",
                    "answerOptions": [
                        {"text": "1 dm³", "isCorrect": True},
                        {"text": "1 m³", "isCorrect": False},
                        {"text": "1 cm³", "isCorrect": False},
                        {"text": "100 ml³", "isCorrect": False}
                    ],
                    "correction": "C'est la conversion de base pour les volumes de liquides."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment calcule-t-on le volume d'un cylindre ?",
                    "answerOptions": [
                        {"text": "Aire de la base × hauteur", "isCorrect": True},
                        {"text": "Périmètre de la base × hauteur", "isCorrect": False},
                        {"text": "Rayon × hauteur", "isCorrect": False},
                        {"text": "π × R³", "isCorrect": False}
                    ],
                    "correction": "V = π × R² × h."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le périmètre d'un carré de 5 cm de côté ?",
                    "answerOptions": [
                        {"text": "20 cm", "isCorrect": True},
                        {"text": "25 cm", "isCorrect": False},
                        {"text": "10 cm", "isCorrect": False},
                        {"text": "50 cm", "isCorrect": False}
                    ],
                    "correction": "P = 4 * 5 = 20 cm."
                },
                {
                    "questionNumber": 50,
                    "question": "Que vaut l'aire d'un triangle de base 10 cm et de hauteur 4 cm ?",
                    "answerOptions": [
                        {"text": "20 cm²", "isCorrect": True},
                        {"text": "40 cm²", "isCorrect": False},
                        {"text": "14 cm²", "isCorrect": False},
                        {"text": "80 cm²", "isCorrect": False}
                    ],
                    "correction": "Aire = (B * h) / 2 = (10 * 4) / 2 = 20."
                },
                {
                    "questionNumber": 51,
                    "question": "Un angle droit mesure :",
                    "answerOptions": [
                        {"text": "90°", "isCorrect": True},
                        {"text": "180°", "isCorrect": False},
                        {"text": "45°", "isCorrect": False},
                        {"text": "360°", "isCorrect": False}
                    ],
                    "correction": "C'est l'angle formé par deux droites perpendiculaires."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment appelle-t-on un triangle ayant deux côtés égaux ?",
                    "answerOptions": [
                        {"text": "Isocèle", "isCorrect": True},
                        {"text": "Équilatéral", "isCorrect": False},
                        {"text": "Rectangle", "isCorrect": False},
                        {"text": "Scalène", "isCorrect": False}
                    ],
                    "correction": "Il possède aussi deux angles égaux."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la valeur approchée de Pi ?",
                    "answerOptions": [
                        {"text": "3,14", "isCorrect": True},
                        {"text": "2,14", "isCorrect": False},
                        {"text": "3,41", "isCorrect": False},
                        {"text": "3,00", "isCorrect": False}
                    ],
                    "correction": "π est un nombre irrationnel."
                },
                {
                    "questionNumber": 54,
                    "question": "L'angle plat mesure :",
                    "answerOptions": [
                        {"text": "180°", "isCorrect": True},
                        {"text": "90°", "isCorrect": False},
                        {"text": "0°", "isCorrect": False},
                        {"text": "270°", "isCorrect": False}
                    ],
                    "correction": "Les côtés de l'angle sont dans le prolongement l'un de l'autre."
                },
                {
                    "questionNumber": 55,
                    "question": "Que signifie 'perpendiculaire' ?",
                    "answerOptions": [
                        {"text": "Qui forme un angle droit", "isCorrect": True},
                        {"text": "Qui ne se croise jamais", "isCorrect": False},
                        {"text": "Qui est très penché", "isCorrect": False},
                        {"text": "Qui a la même longueur", "isCorrect": False}
                    ],
                    "correction": "Le symbole est ⊥."
                },
                {
                    "questionNumber": 56,
                    "question": "Un cube de 2m de côté a un volume de :",
                    "answerOptions": [
                        {"text": "8 m³", "isCorrect": True},
                        {"text": "4 m³", "isCorrect": False},
                        {"text": "6 m³", "isCorrect": False},
                        {"text": "12 m³", "isCorrect": False}
                    ],
                    "correction": "Volume = 2 * 2 * 2 = 8."
                },
                {
                    "questionNumber": 57,
                    "question": "Dans le théorème de Thalès, les droites doivent être :",
                    "answerOptions": [
                        {"text": "Parallèles", "isCorrect": True},
                        {"text": "Perpendiculaires", "isCorrect": False},
                        {"text": "Sécantes en leur milieu", "isCorrect": False},
                        {"text": "De même couleur", "isCorrect": False}
                    ],
                    "correction": "Thalès utilise la proportionnalité des segments dans des triangles imbriqués."
                },
                {
                    "questionNumber": 58,
                    "question": "Le cosinus d'un angle est le rapport :",
                    "answerOptions": [
                        {"text": "Adjacent / Hypoténuse", "isCorrect": True},
                        {"text": "Opposé / Hypoténuse", "isCorrect": False},
                        {"text": "Opposé / Adjacent", "isCorrect": False},
                        {"text": "Adjacent / Opposé", "isCorrect": False}
                    ],
                    "correction": "Moyen mnémotechnique : CAH."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle est l'aire d'un carré de côté 4m ?",
                    "answerOptions": [
                        {"text": "16 m²", "isCorrect": True},
                        {"text": "8 m²", "isCorrect": False},
                        {"text": "12 m²", "isCorrect": False},
                        {"text": "4 m²", "isCorrect": False}
                    ],
                    "correction": "Aire = 4 * 4 = 16."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment appelle-t-on un polygone à 5 côtés ?",
                    "answerOptions": [
                        {"text": "Pentagone", "isCorrect": True},
                        {"text": "Hexagone", "isCorrect": False},
                        {"text": "Octogone", "isCorrect": False},
                        {"text": "Losange", "isCorrect": False}
                    ],
                    "correction": "Penta signifie 5 en grec."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : SUITES NUMÉRIQUES ET CALCULS FINANCIERS (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : SUITES NUMÉRIQUES ET CALCULS FINANCIERS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Dans une suite arithmétique, comment passe-t-on d'un terme au suivant ?",
                    "answerOptions": [
                        {"text": "En ajoutant toujours le même nombre (la raison)", "isCorrect": True},
                        {"text": "En multipliant toujours par le même nombre", "isCorrect": False},
                        {"text": "En divisant par deux", "isCorrect": False},
                        {"text": "En prenant le carré du précédent", "isCorrect": False}
                    ],
                    "correction": "La raison r est le nombre que l'on ajoute."
                },
                {
                    "questionNumber": 62,
                    "question": "Que signifie le sigle TVA ?",
                    "answerOptions": [
                        {"text": "Taxe sur la Valeur Ajoutée", "isCorrect": True},
                        {"text": "Tarif de Vente Annuel", "isCorrect": False},
                        {"text": "Total des Valeurs d'Achat", "isCorrect": False},
                        {"text": "Taxe de Vente Automatique", "isCorrect": False}
                    ],
                    "correction": "C'est un impôt indirect sur la consommation."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment calcule-t-on un prix TTC à partir du prix HT ?",
                    "answerOptions": [
                        {"text": "Prix HT × (1 + taux TVA)", "isCorrect": True},
                        {"text": "Prix HT / taux TVA", "isCorrect": False},
                        {"text": "Prix HT + taux TVA", "isCorrect": False},
                        {"text": "Prix HT - remise", "isCorrect": False}
                    ],
                    "correction": "Ex: Pour une TVA à 20%, on multiplie par 1,20."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la raison de la suite : 2 ; 5 ; 8 ; 11... ?",
                    "answerOptions": [
                        {"text": "3", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "5", "isCorrect": False},
                        {"text": "4", "isCorrect": False}
                    ],
                    "correction": "On ajoute 3 à chaque étape (5-2=3 ; 8-5=3)."
                },
                {
                    "questionNumber": 65,
                    "question": "Dans une suite géométrique, comment passe-t-on d'un terme au suivant ?",
                    "answerOptions": [
                        {"text": "En multipliant toujours par le même nombre (la raison q)", "isCorrect": True},
                        {"text": "En ajoutant une constante", "isCorrect": False},
                        {"text": "En soustrayant la raison", "isCorrect": False},
                        {"text": "C'est aléatoire", "isCorrect": False}
                    ],
                    "correction": "La croissance est beaucoup plus rapide que dans une suite arithmétique."
                },
                {
                    "questionNumber": 66,
                    "question": "Un placement à intérêts simples de 1000 € à 5% par an rapporte combien d'intérêts la première année ?",
                    "answerOptions": [
                        {"text": "50 €", "isCorrect": True},
                        {"text": "5 €", "isCorrect": False},
                        {"text": "100 €", "isCorrect": False},
                        {"text": "500 €", "isCorrect": False}
                    ],
                    "correction": "Intérêt = Capital x Taux = 1000 * 0,05 = 50."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la raison de la suite géométrique : 1 ; 2 ; 4 ; 8... ?",
                    "answerOptions": [
                        {"text": "2", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "4", "isCorrect": False},
                        {"text": "3", "isCorrect": False}
                    ],
                    "correction": "On multiplie par 2 à chaque étape."
                },
                {
                    "questionNumber": 68,
                    "question": "Que signifie un placement à intérêts 'composés' ?",
                    "answerOptions": [
                        {"text": "Les intérêts de chaque année s'ajoutent au capital pour produire de nouveaux intérêts", "isCorrect": True},
                        {"text": "L'intérêt est le même chaque année", "isCorrect": False},
                        {"text": "On ne peut pas retirer son argent", "isCorrect": False},
                        {"text": "Le taux change tous les mois", "isCorrect": False}
                    ],
                    "correction": "C'est l'effet 'boule de neige'."
                },
                {
                    "questionNumber": 69,
                    "question": "Un article à 80 € bénéficie d'une remise de 25%. Quel est le nouveau prix ?",
                    "answerOptions": [
                        {"text": "60 €", "isCorrect": True},
                        {"text": "55 €", "isCorrect": False},
                        {"text": "20 €", "isCorrect": False},
                        {"text": "75 €", "isCorrect": False}
                    ],
                    "correction": "Remise = 80 * 0,25 = 20. Prix final = 80 - 20 = 60."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment calcule-t-on le montant de la TVA ?",
                    "answerOptions": [
                        {"text": "Prix HT × taux TVA", "isCorrect": True},
                        {"text": "Prix TTC - Prix HT", "isCorrect": True},
                        {"text": "Prix HT / Prix TTC", "isCorrect": False},
                        {"text": "Prix TTC + Prix HT", "isCorrect": False}
                    ],
                    "correction": "Les deux premières options sont valables selon les données."
                },
                {
                    "questionNumber": 71,
                    "question": "Si le prix TTC est de 120 € et le prix HT de 100 €, quel est le montant de la TVA ?",
                    "answerOptions": [
                        {"text": "20 €", "isCorrect": True},
                        {"text": "120 €", "isCorrect": False},
                        {"text": "20%", "isCorrect": False},
                        {"text": "1,20 €", "isCorrect": False}
                    ],
                    "correction": "120 - 100 = 20."
                },
                {
                    "questionNumber": 72,
                    "question": "Dans f(n) = f(0) + n*r, on reconnaît une suite :",
                    "answerOptions": [
                        {"text": "Arithmétique", "isCorrect": True},
                        {"text": "Géométrique", "isCorrect": False},
                        {"text": "Décroissante", "isCorrect": False},
                        {"text": "Financière", "isCorrect": False}
                    ],
                    "correction": "C'est la formule du terme général."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le coefficient multiplicateur pour une baisse de 30% ?",
                    "answerOptions": [
                        {"text": "0,70", "isCorrect": True},
                        {"text": "1,30", "isCorrect": False},
                        {"text": "0,30", "isCorrect": False},
                        {"text": "3", "isCorrect": False}
                    ],
                    "correction": "1 - 30/100 = 0,70."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment s'appelle le premier terme d'une suite (souvent) ?",
                    "answerOptions": [
                        {"text": "u0 ou u1", "isCorrect": True},
                        {"text": "La raison", "isCorrect": False},
                        {"text": "L'indice", "isCorrect": False},
                        {"text": "Le total", "isCorrect": False}
                    ],
                    "correction": "L'indice (0 ou 1) indique le rang."
                },
                {
                    "questionNumber": 75,
                    "question": "Une suite dont la raison est comprise entre 0 et 1 est :",
                    "answerOptions": [
                        {"text": "Décroissante", "isCorrect": True},
                        {"text": "Croissante", "isCorrect": False},
                        {"text": "Constante", "isCorrect": False},
                        {"text": "Négative", "isCorrect": False}
                    ],
                    "correction": "Les valeurs diminuent à chaque étape (ex: on multiplie par 0,5)."
                },
                {
                    "questionNumber": 76,
                    "question": "Que signifie le 'taux annuel' d'un prêt ?",
                    "answerOptions": [
                        {"text": "Le coût du crédit sur un an exprimé en pourcentage du capital", "isCorrect": True},
                        {"text": "Le montant total à rembourser", "isCorrect": False},
                        {"text": "La durée du prêt", "isCorrect": False},
                        {"text": "Le prix de l'assurance", "isCorrect": False}
                    ],
                    "correction": "C'est l'indicateur principal du prix du prêt."
                },
                {
                    "questionNumber": 77,
                    "question": "Trouvez le 4ème terme de la suite arithmétique de premier terme 10 et de raison 5.",
                    "answerOptions": [
                        {"text": "25", "isCorrect": True},
                        {"text": "15", "isCorrect": False},
                        {"text": "30", "isCorrect": False},
                        {"text": "20", "isCorrect": False}
                    ],
                    "correction": "10 (u0), 15 (u1), 20 (u2), 25 (u3)."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le prix HT si le TTC est de 60 € avec une TVA à 20% ?",
                    "answerOptions": [
                        {"text": "50 €", "isCorrect": True},
                        {"text": "48 €", "isCorrect": False},
                        {"text": "40 €", "isCorrect": False},
                        {"text": "55 €", "isCorrect": False}
                    ],
                    "correction": "HT = TTC / 1,20 = 60 / 1,2 = 50."
                },
                {
                    "questionNumber": 79,
                    "question": "Si la raison q d'une suite géométrique est égale à 1, la suite est :",
                    "answerOptions": [
                        {"text": "Constante", "isCorrect": True},
                        {"text": "Nulle", "isCorrect": False},
                        {"text": "Infinie", "isCorrect": False},
                        {"text": "Arithmétique", "isCorrect": False}
                    ],
                    "correction": "Multiplier par 1 ne change pas la valeur."
                },
                {
                    "questionNumber": 80,
                    "question": "Une remise est une réduction :",
                    "answerOptions": [
                        {"text": "Commerciale accordée selon les quantités ou l'habitude", "isCorrect": True},
                        {"text": "Uniquement pour les produits cassés", "isCorrect": False},
                        {"text": "De l'État", "isCorrect": False},
                        {"text": "De 100%", "isCorrect": False}
                    ],
                    "correction": "On distingue remise, rabais et ristourne."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : CALCUL NUMÉRIQUE ET ALGORITHMIQUE (Q81 à Q100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : CALCUL NUMÉRIQUE ET ALGORITHMIQUE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "En algorithmique, à quoi sert une variable ?",
                    "answerOptions": [
                        {"text": "À stocker une information (nombre, texte) en mémoire", "isCorrect": True},
                        {"text": "À décorer le programme", "isCorrect": False},
                        {"text": "À éteindre l'ordinateur", "isCorrect": False},
                        {"text": "À mesurer la vitesse du processeur", "isCorrect": False}
                    ],
                    "correction": "On peut imaginer une boîte avec une étiquette (le nom) et un contenu (la valeur)."
                },
                {
                    "questionNumber": 82,
                    "question": "Que fait l'instruction 'print' en Python ?",
                    "answerOptions": [
                        {"text": "Elle affiche un résultat à l'écran", "isCorrect": True},
                        {"text": "Elle imprime sur papier", "isCorrect": False},
                        {"text": "Elle efface la mémoire", "isCorrect": False},
                        {"text": "Elle demande une valeur à l'utilisateur", "isCorrect": False}
                    ],
                    "correction": "C'est l'instruction de sortie de base."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel symbole utilise-t-on pour la multiplication dans la plupart des langages de programmation ?",
                    "answerOptions": [
                        {"text": "*", "isCorrect": True},
                        {"text": "x", "isCorrect": False},
                        {"text": "×", "isCorrect": False},
                        {"text": "•", "isCorrect": False}
                    ],
                    "correction": "L'étoile évite la confusion avec la lettre x."
                },
                {
                    "questionNumber": 84,
                    "question": "Qu'est-ce qu'une boucle 'for' ?",
                    "answerOptions": [
                        {"text": "Une structure qui répète des instructions un nombre défini de fois", "isCorrect": True},
                        {"text": "Une erreur du programme", "isCorrect": False},
                        {"text": "Une question posée à l'utilisateur", "isCorrect": False},
                        {"text": "Une condition de type SI... ALORS", "isCorrect": False}
                    ],
                    "correction": "Elle permet d'automatiser des tâches répétitives."
                },
                {
                    "questionNumber": 85,
                    "question": "Que signifie le symbole '==' ?",
                    "answerOptions": [
                        {"text": "Est égal à (test de comparaison)", "isCorrect": True},
                        {"text": "Prend la valeur de (affectation)", "isCorrect": False},
                        {"text": "Est différent de", "isCorrect": False},
                        {"text": "Est plus grand que", "isCorrect": False}
                    ],
                    "correction": "Le simple '=' sert à donner une valeur, le double '==' sert à comparer."
                },
                {
                    "questionNumber": 86,
                    "question": "Que vaut 2 ** 3 ?",
                    "answerOptions": [
                        {"text": "8", "isCorrect": True},
                        {"text": "6", "isCorrect": False},
                        {"text": "5", "isCorrect": False},
                        {"text": "9", "isCorrect": False}
                    ],
                    "correction": "C'est 2 à la puissance 3 : 2 * 2 * 2 = 8."
                },
                {
                    "questionNumber": 87,
                    "question": "Une structure conditionnelle commence souvent par :",
                    "answerOptions": [
                        {"text": "if (si)", "isCorrect": True},
                        {"text": "while (pendant que)", "isCorrect": False},
                        {"text": "stop", "isCorrect": False},
                        {"text": "start", "isCorrect": False}
                    ],
                    "correction": "Elle permet de faire des choix dans le programme."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'un 'float' en informatique ?",
                    "answerOptions": [
                        {"text": "Un nombre à virgule (décimal)", "isCorrect": True},
                        {"text": "Un texte", "isCorrect": False},
                        {"text": "Un nombre entier", "isCorrect": False},
                        {"text": "Une liste de données", "isCorrect": False}
                    ],
                    "correction": "Par exemple : 3.14."
                },
                {
                    "questionNumber": 89,
                    "question": "Que signifie incrémenter une variable ?",
                    "answerOptions": [
                        {"text": "Ajouter 1 à sa valeur", "isCorrect": True},
                        {"text": "La multiplier par deux", "isCorrect": False},
                        {"text": "L'effacer", "isCorrect": False},
                        {"text": "La diviser", "isCorrect": False}
                    ],
                    "correction": "Souvent utilisé dans les compteurs de boucles."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est la valeur de x après ces étapes : x=5 ; x=x+2 ; x=x*10 ?",
                    "answerOptions": [
                        {"text": "70", "isCorrect": True},
                        {"text": "25", "isCorrect": False},
                        {"text": "52", "isCorrect": False},
                        {"text": "17", "isCorrect": False}
                    ],
                    "correction": "5 -> 7 -> 70."
                },
                {
                    "questionNumber": 91,
                    "question": "Comment appelle-t-on une erreur dans un programme ?",
                    "answerOptions": [
                        {"text": "Un bug", "isCorrect": True},
                        {"text": "Un virus", "isCorrect": False},
                        {"text": "Un dossier", "isCorrect": False},
                        {"text": "Un écran noir", "isCorrect": False}
                    ],
                    "correction": "Historiquement lié à un insecte coincé dans un ordinateur."
                },
                {
                    "questionNumber": 92,
                    "question": "Le carré de 0,5 est :",
                    "answerOptions": [
                        {"text": "0,25", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "0,1", "isCorrect": False},
                        {"text": "2,5", "isCorrect": False}
                    ],
                    "correction": "0,5 * 0,5 = 0,25."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel type de variable ne peut prendre que True ou False ?",
                    "answerOptions": [
                        {"text": "Booléen", "isCorrect": True},
                        {"text": "Flottant", "isCorrect": False},
                        {"text": "Entier", "isCorrect": False},
                        {"text": "Liste", "isCorrect": False}
                    ],
                    "correction": "Un booléen est une valeur de vérité."
                },
                {
                    "questionNumber": 94,
                    "question": "Que fait l'instruction else dans une structure conditionnelle ?",
                    "answerOptions": [
                        {"text": "Elle gère le cas où la condition est fausse", "isCorrect": True},
                        {"text": "Elle arrête immédiatement le programme en cours", "isCorrect": False},
                        {"text": "Elle définit une nouvelle variable de calcul", "isCorrect": False},
                        {"text": "Elle relance la boucle depuis le début", "isCorrect": False}
                    ],
                    "correction": "else s'exécute si le if échoue."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le résultat de 2 puissance 3 ?",
                    "answerOptions": [
                        {"text": "8", "isCorrect": True},
                        {"text": "6", "isCorrect": False},
                        {"text": "5", "isCorrect": False},
                        {"text": "9", "isCorrect": False}
                    ],
                    "correction": "2 * 2 * 2 = 8."
                },
                {
                    "questionNumber": 96,
                    "question": "En Python, comment appelle-t-on un nombre à virgule ?",
                    "answerOptions": [
                        {"text": "Un flottant", "isCorrect": True},
                        {"text": "Un entier", "isCorrect": False},
                        {"text": "Un texte", "isCorrect": False},
                        {"text": "Une liste", "isCorrect": False}
                    ],
                    "correction": "Float désigne les nombres décimaux."
                },
                {
                    "questionNumber": 97,
                    "question": "Que permet de faire l'instruction input ?",
                    "answerOptions": [
                        {"text": "Demander une valeur à l'utilisateur", "isCorrect": True},
                        {"text": "Afficher un message", "isCorrect": False},
                        {"text": "Fermer le programme", "isCorrect": False},
                        {"text": "Calculer une racine carrée", "isCorrect": False}
                    ],
                    "correction": "C'est l'instruction d'entrée de base."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est l'indice du premier élément d'une liste en Python ?",
                    "answerOptions": [
                        {"text": "0", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "-1", "isCorrect": False},
                        {"text": "A", "isCorrect": False}
                    ],
                    "correction": "L'ordinateur commence toujours à compter à partir de zéro."
                },
                {
                    "questionNumber": 99,
                    "question": "Que signifie l'opérateur '!=' ?",
                    "answerOptions": [
                        {"text": "Différent de", "isCorrect": True},
                        {"text": "Égal à", "isCorrect": False},
                        {"text": "Supérieur ou égal", "isCorrect": False},
                        {"text": "Attention", "isCorrect": False}
                    ],
                    "correction": "C'est l'inverse du test d'égalité."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel symbole entoure une chaîne de caractères (texte) ?",
                    "answerOptions": [
                        {"text": "Des guillemets (double ou simple)", "isCorrect": True},
                        {"text": "Des parenthèses", "isCorrect": False},
                        {"text": "Des crochets", "isCorrect": False},
                        {"text": "Rien du tout", "isCorrect": False}
                    ],
                    "correction": "Exemple : 'Bonjour' ou \"Bonjour\"."
                }
            ]
        }
    }
}