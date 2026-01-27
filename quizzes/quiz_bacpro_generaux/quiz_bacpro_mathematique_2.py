quiz_data = {
    "title": "Quiz Bac Pro Mathématiques N°2 - Niveau Avancé (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : ÉVOLUTION, TAUX DE VARIATION ET POURCENTAGES (Q1 à Q20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : ÉVOLUTION, TAUX DE VARIATION ET POURCENTAGES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel calcul permet de trouver le taux d'évolution réciproque d'une hausse de 25% ?",
                    "answerOptions": [
                        {"text": "1 divisé par 1,25 puis soustraire 1", "isCorrect": True},
                        {"text": "L'opposé du taux de départ soit moins 0,25", "isCorrect": False},
                        {"text": "1 multiplié par 0,75 pour compenser la hausse", "isCorrect": False},
                        {"text": "On divise la valeur finale par le taux initial", "isCorrect": False}
                    ],
                    "correction": "Le coefficient multiplicateur réciproque est égal à 1/CM. Pour une hausse de 25% (CM=1,25), le CM réciproque est 1/1,25 = 0,8. Le taux réciproque est donc 0,8 - 1 = -0,2 soit une baisse de 20%."
                },
                {
                    "questionNumber": 2,
                    "question": "Si une action perd 20% de sa valeur, de quel pourcentage doit-elle augmenter pour retrouver sa valeur initiale ?",
                    "answerOptions": [
                        {"text": "25%", "isCorrect": True},
                        {"text": "20%", "isCorrect": False},
                        {"text": "120%", "isCorrect": False},
                        {"text": "22,5%", "isCorrect": False}
                    ],
                    "correction": "Le CM d'une baisse de 20% est 0,8. Le CM réciproque est 1 / 0,8 = 1,25. Une multiplication par 1,25 correspond à une hausse de 25%."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le coefficient multiplicateur global correspondant à trois hausses successives de 10% ?",
                    "answerOptions": [
                        {"text": "1,331", "isCorrect": True},
                        {"text": "1,30", "isCorrect": False},
                        {"text": "3,10", "isCorrect": False},
                        {"text": "0,729", "isCorrect": False}
                    ],
                    "correction": "On multiplie les coefficients entre eux : 1,1 x 1,1 x 1,1 = 1,1³ = 1,331."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment appelle-t-on le rapport entre la variation absolue et la valeur initiale ?",
                    "answerOptions": [
                        {"text": "Le taux d'évolution", "isCorrect": True},
                        {"text": "L'indice de base 100", "isCorrect": False},
                        {"text": "La remise commerciale", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur", "isCorrect": False}
                    ],
                    "correction": "Taux d'évolution = (Valeur Finale - Valeur Initiale) / Valeur Initiale."
                },
                {
                    "questionNumber": 5,
                    "question": "Une population passe de 500 à 600 individus. Quel est le taux d'évolution ?",
                    "answerOptions": [
                        {"text": "20%", "isCorrect": True},
                        {"text": "100%", "isCorrect": False},
                        {"text": "120%", "isCorrect": False},
                        {"text": "10%", "isCorrect": False}
                    ],
                    "correction": "(600 - 500) / 500 = 100 / 500 = 0,2 soit 20%."
                },
                {
                    "questionNumber": 6,
                    "question": "Que signifie un indice de 105 par rapport à une année de référence (base 100) ?",
                    "answerOptions": [
                        {"text": "Une augmentation de 5% par rapport à l'année de référence", "isCorrect": True},
                        {"text": "Que le prix est de 105 euros", "isCorrect": False},
                        {"text": "Une baisse de 5% de la production", "isCorrect": False},
                        {"text": "Que la valeur a été multipliée par 105", "isCorrect": False}
                    ],
                    "correction": "L'indice permet de visualiser rapidement l'évolution : Indice = (Valeur / Valeur de référence) x 100."
                },
                {
                    "questionNumber": 7,
                    "question": "Un prix subit une hausse de 50% suivie d'une baisse de 50%. Le prix final est :",
                    "answerOptions": [
                        {"text": "Inférieur au prix initial", "isCorrect": True},
                        {"text": "Égal au prix initial", "isCorrect": False},
                        {"text": "Supérieur au prix initial", "isCorrect": False},
                        {"text": "Nul", "isCorrect": False}
                    ],
                    "correction": "CM global = 1,5 x 0,5 = 0,75. Le prix a donc baissé de 25% au total."
                },
                {
                    "questionNumber": 8,
                    "question": "Le taux d'évolution global de deux hausses de 20% est de :",
                    "answerOptions": [
                        {"text": "44%", "isCorrect": True},
                        {"text": "40%", "isCorrect": False},
                        {"text": "20%", "isCorrect": False},
                        {"text": "4%", "isCorrect": False}
                    ],
                    "correction": "1,2 x 1,2 = 1,44. Cela correspond à une hausse globale de 44%."
                },
                {
                    "questionNumber": 9,
                    "question": "Si l'indice d'un produit est 80, quelle a été l'évolution depuis la base 100 ?",
                    "answerOptions": [
                        {"text": "Une baisse de 20%", "isCorrect": True},
                        {"text": "Une baisse de 80%", "isCorrect": False},
                        {"text": "Une hausse de 80%", "isCorrect": False},
                        {"text": "Une baisse de 0,8%", "isCorrect": False}
                    ],
                    "correction": "80 - 100 = -20."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le coefficient multiplicateur pour une baisse de 2% ?",
                    "answerOptions": [
                        {"text": "0,98", "isCorrect": True},
                        {"text": "0,02", "isCorrect": False},
                        {"text": "1,02", "isCorrect": False},
                        {"text": "0,2", "isCorrect": False}
                    ],
                    "correction": "1 - (2/100) = 0,98."
                },
                {
                    "questionNumber": 11,
                    "question": "Comment calcule-t-on la variation absolue ?",
                    "answerOptions": [
                        {"text": "Valeur Finale - Valeur Initiale", "isCorrect": True},
                        {"text": "Valeur Finale / Valeur Initiale", "isCorrect": False},
                        {"text": "Valeur Initiale - Valeur Finale", "isCorrect": False},
                        {"text": "Valeur Finale + Valeur Initiale", "isCorrect": False}
                    ],
                    "correction": "Elle s'exprime dans la même unité que les valeurs (euros, kg, etc.)."
                },
                {
                    "questionNumber": 12,
                    "question": "Une remise de 30% correspond à quel CM ?",
                    "answerOptions": [
                        {"text": "0,7", "isCorrect": True},
                        {"text": "0,3", "isCorrect": False},
                        {"text": "1,3", "isCorrect": False},
                        {"text": "3", "isCorrect": False}
                    ],
                    "correction": "1 - 0,30 = 0,7."
                },
                {
                    "questionNumber": 13,
                    "question": "Pour doubler une valeur, quel est le taux d'augmentation ?",
                    "answerOptions": [
                        {"text": "100%", "isCorrect": True},
                        {"text": "200%", "isCorrect": False},
                        {"text": "50%", "isCorrect": False},
                        {"text": "2%", "isCorrect": False}
                    ],
                    "correction": "Si le prix passe de 10 à 20 : (20-10)/10 = 1 = 100%."
                },
                {
                    "questionNumber": 14,
                    "question": "Le prix HT est 100€. La TVA est 20%. Le prix TTC est 120€. Quel est l'indice du prix TTC si le prix HT est la base 100 ?",
                    "answerOptions": [
                        {"text": "120", "isCorrect": True},
                        {"text": "20", "isCorrect": False},
                        {"text": "1,2", "isCorrect": False},
                        {"text": "100", "isCorrect": False}
                    ],
                    "correction": "(120 / 100) x 100 = 120."
                },
                {
                    "questionNumber": 15,
                    "question": "Si un CM est de 2,5, quelle est l'augmentation en pourcentage ?",
                    "answerOptions": [
                        {"text": "150%", "isCorrect": True},
                        {"text": "250%", "isCorrect": False},
                        {"text": "25%", "isCorrect": False},
                        {"text": "50%", "isCorrect": False}
                    ],
                    "correction": "(2,5 - 1) x 100 = 1,5 x 100 = 150%."
                },
                {
                    "questionNumber": 16,
                    "question": "Pour tripler une valeur, le taux d'évolution est de :",
                    "answerOptions": [
                        {"text": "200%", "isCorrect": True},
                        {"text": "300%", "isCorrect": False},
                        {"text": "3%", "isCorrect": False},
                        {"text": "100%", "isCorrect": False}
                    ],
                    "correction": "(3 - 1) x 100 = 200%."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est la valeur initiale si après une hausse de 10% on obtient 110 ?",
                    "answerOptions": [
                        {"text": "100", "isCorrect": True},
                        {"text": "100,1", "isCorrect": False},
                        {"text": "121", "isCorrect": False},
                        {"text": "90", "isCorrect": False}
                    ],
                    "correction": "110 / 1,1 = 100."
                },
                {
                    "questionNumber": 18,
                    "question": "Un taux d'évolution de 0% signifie que :",
                    "answerOptions": [
                        {"text": "La valeur est restée constante", "isCorrect": True},
                        {"text": "La valeur est devenue nulle", "isCorrect": False},
                        {"text": "On ne peut pas calculer", "isCorrect": False},
                        {"text": "Le coefficient est 0", "isCorrect": False}
                    ],
                    "correction": "Si VF = VI, alors le taux est 0."
                },
                {
                    "questionNumber": 19,
                    "question": "Si CM = 1,005, l'augmentation est de :",
                    "answerOptions": [
                        {"text": "0,5%", "isCorrect": True},
                        {"text": "5%", "isCorrect": False},
                        {"text": "50%", "isCorrect": False},
                        {"text": "0,05%", "isCorrect": False}
                    ],
                    "correction": "(1,005 - 1) x 100 = 0,005 x 100 = 0,5%."
                },
                {
                    "questionNumber": 20,
                    "question": "L'indice de prix à la consommation (IPC) sert à mesurer :",
                    "answerOptions": [
                        {"text": "L'inflation", "isCorrect": True},
                        {"text": "Le nombre de magasins", "isCorrect": False},
                        {"text": "Le poids des aliments", "isCorrect": False},
                        {"text": "La météo", "isCorrect": False}
                    ],
                    "correction": "Il suit l'évolution des prix d'un panier de biens et services."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : FONCTIONS DE RÉFÉRENCE ET CALCUL INTÉGRAL (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : FONCTIONS DE RÉFÉRENCE ET CALCUL INTÉGRAL",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la dérivée de la fonction f(x) = x² ?",
                    "answerOptions": [
                        {"text": "f'(x) = 2x", "isCorrect": True},
                        {"text": "f'(x) = x", "isCorrect": False},
                        {"text": "f'(x) = 2", "isCorrect": False},
                        {"text": "f'(x) = 1/x", "isCorrect": False}
                    ],
                    "correction": "La règle de dérivation pour x^n est n*x^(n-1)."
                },
                {
                    "questionNumber": 22,
                    "question": "Que permet de déterminer le signe de la dérivée f'(x) ?",
                    "answerOptions": [
                        {"text": "Le sens de variation de la fonction f", "isCorrect": True},
                        {"text": "Le signe de la fonction f", "isCorrect": False},
                        {"text": "L'ordonnée à l'origine de f", "isCorrect": False},
                        {"text": "Le coefficient directeur de la sécante", "isCorrect": False}
                    ],
                    "correction": "Si f'(x) > 0, f est croissante. Si f'(x) < 0, f est décroissante."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la valeur de la dérivée d'une fonction constante f(x) = k ?",
                    "answerOptions": [
                        {"text": "0", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "k", "isCorrect": False},
                        {"text": "x", "isCorrect": False}
                    ],
                    "correction": "Une constante ne varie pas, son taux de variation est donc nul."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on le point où la dérivée s'annule en changeant de signe ?",
                    "answerOptions": [
                        {"text": "Un extremum (maximum ou minimum)", "isCorrect": True},
                        {"text": "L'origine du repère", "isCorrect": False},
                        {"text": "Une racine de la fonction", "isCorrect": False},
                        {"text": "Une asymptote", "isCorrect": False}
                    ],
                    "correction": "C'est là où la courbe de la fonction change de sens."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la primitive de f(x) = x ?",
                    "answerOptions": [
                        {"text": "F(x) = 0,5x²", "isCorrect": True},
                        {"text": "F(x) = 1", "isCorrect": False},
                        {"text": "F(x) = x²", "isCorrect": False},
                        {"text": "F(x) = 2x", "isCorrect": False}
                    ],
                    "correction": "La primitive est l'opération inverse de la dérivée (à une constante près)."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la forme de la courbe d'une fonction du second degré f(x) = ax² + bx + c ?",
                    "answerOptions": [
                        {"text": "Une parabole", "isCorrect": True},
                        {"text": "Une droite", "isCorrect": False},
                        {"text": "Une hyperbole", "isCorrect": False},
                        {"text": "Un cercle", "isCorrect": False}
                    ],
                    "correction": "La parabole est tournée vers le haut si a > 0 et vers le bas si a < 0."
                },
                {
                    "questionNumber": 27,
                    "question": "Dans f(x) = ax² + bx + c, comment appelle-t-on le nombre Δ = b² - 4ac ?",
                    "answerOptions": [
                        {"text": "Le discriminant", "isCorrect": True},
                        {"text": "Le dénominateur", "isCorrect": False},
                        {"text": "Le diviseur", "isCorrect": False},
                        {"text": "Le degré", "isCorrect": False}
                    ],
                    "correction": "Il sert à déterminer le nombre de racines réelles de l'équation ax² + bx + c = 0."
                },
                {
                    "questionNumber": 28,
                    "question": "Si le discriminant Δ est négatif (< 0), combien de racines réelles possède l'équation ?",
                    "answerOptions": [
                        {"text": "Aucune", "isCorrect": True},
                        {"text": "Une seule", "isCorrect": False},
                        {"text": "Deux", "isCorrect": False},
                        {"text": "Une infinité", "isCorrect": False}
                    ],
                    "correction": "La parabole ne coupe jamais l'axe des abscisses."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la dérivée de f(x) = 5x + 3 ?",
                    "answerOptions": [
                        {"text": "f'(x) = 5", "isCorrect": True},
                        {"text": "f'(x) = 5x", "isCorrect": False},
                        {"text": "f'(x) = 3", "isCorrect": False},
                        {"text": "f'(x) = 8", "isCorrect": False}
                    ],
                    "correction": "La dérivée de ax + b est a."
                },
                {
                    "questionNumber": 30,
                    "question": "Que représente géométriquement f'(a) ?",
                    "answerOptions": [
                        {"text": "Le coefficient directeur de la tangente à la courbe au point d'abscisse a", "isCorrect": True},
                        {"text": "L'aire sous la courbe", "isCorrect": False},
                        {"text": "La distance à l'origine", "isCorrect": False},
                        {"text": "L'intersection avec l'axe y", "isCorrect": False}
                    ],
                    "correction": "La tangente donne la direction de la courbe en un point précis."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la dérivée de f(x) = 1/x ?",
                    "answerOptions": [
                        {"text": "f'(x) = -1/x²", "isCorrect": True},
                        {"text": "f'(x) = 1/x²", "isCorrect": False},
                        {"text": "f'(x) = ln(x)", "isCorrect": False},
                        {"text": "f'(x) = 0", "isCorrect": False}
                    ],
                    "correction": "C'est une formule de référence pour les fonctions inverses."
                },
                {
                    "questionNumber": 32,
                    "question": "La fonction f(x) = x³ est :",
                    "answerOptions": [
                        {"text": "Toujours croissante sur R", "isCorrect": True},
                        {"text": "Décroissante sur les négatifs", "isCorrect": False},
                        {"text": "Une parabole", "isCorrect": False},
                        {"text": "Paire", "isCorrect": False}
                    ],
                    "correction": "Sa dérivée 3x² est toujours positive ou nulle."
                },
                {
                    "questionNumber": 33,
                    "question": "L'équation de la tangente au point d'abscisse a est du type :",
                    "answerOptions": [
                        {"text": "y = f'(a)(x - a) + f(a)", "isCorrect": True},
                        {"text": "y = ax + b", "isCorrect": False},
                        {"text": "y = f(a)x + f'(a)", "isCorrect": False},
                        {"text": "y = x² + f(a)", "isCorrect": False}
                    ],
                    "correction": "C'est une formule fondamentale pour l'étude locale des courbes."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la dérivée de f(x) = x³ ?",
                    "answerOptions": [
                        {"text": "3x²", "isCorrect": True},
                        {"text": "x²", "isCorrect": False},
                        {"text": "3x", "isCorrect": False},
                        {"text": "1/3 x²", "isCorrect": False}
                    ],
                    "correction": "On descend l'exposant devant et on diminue l'exposant de 1."
                },
                {
                    "questionNumber": 35,
                    "question": "Le sommet d'une parabole d'équation y = ax² + bx + c a pour abscisse :",
                    "answerOptions": [
                        {"text": "-b / 2a", "isCorrect": True},
                        {"text": "b / 2a", "isCorrect": False},
                        {"text": "-c / a", "isCorrect": False},
                        {"text": "Δ / 4a", "isCorrect": False}
                    ],
                    "correction": "C'est l'axe de symétrie de la parabole."
                },
                {
                    "questionNumber": 36,
                    "question": "Si a est négatif dans f(x) = ax² + bx + c, la parabole est tournée :",
                    "answerOptions": [
                        {"text": "Vers le bas", "isCorrect": True},
                        {"text": "Vers le haut", "isCorrect": False},
                        {"text": "Vers la droite", "isCorrect": False},
                        {"text": "Vers la gauche", "isCorrect": False}
                    ],
                    "correction": "Elle admet alors un maximum."
                },
                {
                    "questionNumber": 37,
                    "question": "La dérivée de la somme de deux fonctions (u + v)' est :",
                    "answerOptions": [
                        {"text": "u' + v'", "isCorrect": True},
                        {"text": "u'v + uv'", "isCorrect": False},
                        {"text": "u'v'", "isCorrect": False},
                        {"text": "u / v'", "isCorrect": False}
                    ],
                    "correction": "La dérivation est une opération linéaire."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la dérivée de f(x) = √x ?",
                    "answerOptions": [
                        {"text": "1 / (2√x)", "isCorrect": True},
                        {"text": "2√x", "isCorrect": False},
                        {"text": "x", "isCorrect": False},
                        {"text": "1/x", "isCorrect": False}
                    ],
                    "correction": "Cette fonction n'est pas dérivable en zéro."
                },
                {
                    "questionNumber": 39,
                    "question": "Un tableau de variations résume :",
                    "answerOptions": [
                        {"text": "Le sens de variation et les extremums de la fonction", "isCorrect": True},
                        {"text": "La liste des points du graphique", "isCorrect": False},
                        {"text": "Les prix des produits", "isCorrect": False},
                        {"text": "Le nom des axes", "isCorrect": False}
                    ],
                    "correction": "Il permet de visualiser les intervalles de croissance et de décroissance ainsi que les images des extremums."
                },
                {
                    "questionNumber": 40,
                    "question": "Que signifie f(x) tend vers l'infini ?",
                    "answerOptions": [
                        {"text": "Les valeurs de y deviennent aussi grandes que l'on veut", "isCorrect": True},
                        {"text": "La fonction s'arrête", "isCorrect": False},
                        {"text": "La courbe est un cercle", "isCorrect": False},
                        {"text": "x est égal à zéro", "isCorrect": False}
                    ],
                    "correction": "C'est la notion de limite."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : TRIGONOMÉTRIE ET GÉOMÉTRIE DANS L'ESPACE (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : TRIGONOMÉTRIE ET GÉOMÉTRIE DANS L'ESPACE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Dans un triangle rectangle, quel est le rapport définissant le Cosinus ?",
                    "answerOptions": [
                        {"text": "Côté adjacent / Hypoténuse", "isCorrect": True},
                        {"text": "Côté opposé / Hypoténuse", "isCorrect": False},
                        {"text": "Côté opposé / Côté adjacent", "isCorrect": False},
                        {"text": "Hypoténuse / Côté opposé", "isCorrect": False}
                    ],
                    "correction": "Moyen mnémotechnique : CAH (Cosinus Adjacent Hypoténuse)."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la valeur de cos(0°) ?",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False},
                        {"text": "Infini", "isCorrect": False}
                    ],
                    "correction": "Sur le cercle trigonométrique, le cosinus se lit sur l'axe des abscisses."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle relation lie le sinus et le cosinus d'un même angle α ?",
                    "answerOptions": [
                        {"text": "cos²(α) + sin²(α) = 1", "isCorrect": True},
                        {"text": "cos(α) + sin(α) = 1", "isCorrect": False},
                        {"text": "sin(α) / cos(α) = 1", "isCorrect": False},
                        {"text": "cos²(α) - sin²(α) = 1", "isCorrect": False}
                    ],
                    "correction": "C'est l'identité trigonométrique fondamentale."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le volume d'une sphère de rayon R ?",
                    "answerOptions": [
                        {"text": "(4/3) x π x R³", "isCorrect": True},
                        {"text": "4 x π x R²", "isCorrect": False},
                        {"text": "π x R²", "isCorrect": False},
                        {"text": "2 x π x R", "isCorrect": False}
                    ],
                    "correction": "L'aire de la surface est 4πR², le volume est (4/3)πR³. "
                },
                {
                    "questionNumber": 45,
                    "question": "Combien de degrés font π radians ?",
                    "answerOptions": [
                        {"text": "180°", "isCorrect": True},
                        {"text": "360°", "isCorrect": False},
                        {"text": "90°", "isCorrect": False},
                        {"text": "0°", "isCorrect": False}
                    ],
                    "correction": "C'est la correspondance de base entre degrés et radians."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment calcule-t-on la diagonale d'un cube de côté 'a' ?",
                    "answerOptions": [
                        {"text": "a x √3", "isCorrect": True},
                        {"text": "a x √2", "isCorrect": False},
                        {"text": "3 x a", "isCorrect": False},
                        {"text": "a²", "isCorrect": False}
                    ],
                    "correction": "On utilise deux fois le théorème de Pythagore dans l'espace."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est la formule du volume d'un cône de révolution ?",
                    "answerOptions": [
                        {"text": "(1/3) x Aire de la base x hauteur", "isCorrect": True},
                        {"text": "Aire de la base x hauteur", "isCorrect": False},
                        {"text": "π x R² x h", "isCorrect": False},
                        {"text": "2 x π x R x h", "isCorrect": False}
                    ],
                    "correction": "Le cône occupe un tiers du volume du cylindre correspondant."
                },
                {
                    "questionNumber": 48,
                    "question": "Que vaut sin(90°) ou sin(π/2) ?",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "-1", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False}
                    ],
                    "correction": "C'est la valeur maximale du sinus."
                },
                {
                    "questionNumber": 49,
                    "question": "Dans un triangle rectangle, la Tangente d'un angle est :",
                    "answerOptions": [
                        {"text": "Opposé / Adjacent", "isCorrect": True},
                        {"text": "Adjacent / Opposé", "isCorrect": False},
                        {"text": "Sinus x Cosinus", "isCorrect": False},
                        {"text": "Opposé / Hypoténuse", "isCorrect": False}
                    ],
                    "correction": "Mnémotechnique : TOA."
                },
                {
                    "questionNumber": 50,
                    "question": "Un cylindre a un rayon de 3cm et une hauteur de 10cm. Quel est son volume (environ) ?",
                    "answerOptions": [
                        {"text": "283 cm³", "isCorrect": True},
                        {"text": "30 cm³", "isCorrect": False},
                        {"text": "90 cm³", "isCorrect": False},
                        {"text": "188 cm³", "isCorrect": False}
                    ],
                    "correction": "V = π x 3² x 10 = π x 9 x 10 = 90π ≈ 282,7."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la section d'une sphère par un plan ?",
                    "answerOptions": [
                        {"text": "Un cercle (ou un point)", "isCorrect": True},
                        {"text": "Un carré", "isCorrect": False},
                        {"text": "Un triangle", "isCorrect": False},
                        {"text": "Un rectangle", "isCorrect": False}
                    ],
                    "correction": "Si le plan passe par le centre, on obtient un grand cercle."
                },
                {
                    "questionNumber": 52,
                    "question": "Combien de faces possède un parallélépipède rectangle (pavé droit) ?",
                    "answerOptions": [
                        {"text": "6", "isCorrect": True},
                        {"text": "4", "isCorrect": False},
                        {"text": "8", "isCorrect": False},
                        {"text": "12", "isCorrect": False}
                    ],
                    "correction": "Il a 6 faces, 8 sommets et 12 arêtes."
                },
                {
                    "questionNumber": 53,
                    "question": "L'unité d'un volume est le mètre cube. 1 m³ vaut :",
                    "answerOptions": [
                        {"text": "1 000 litres", "isCorrect": True},
                        {"text": "100 litres", "isCorrect": False},
                        {"text": "10 000 litres", "isCorrect": False},
                        {"text": "1 litre", "isCorrect": False}
                    ],
                    "correction": "1 dm³ = 1 litre."
                },
                {
                    "questionNumber": 54,
                    "question": "Que vaut cos(90°) ?",
                    "answerOptions": [
                        {"text": "0", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False},
                        {"text": "-1", "isCorrect": False}
                    ],
                    "correction": "L'angle droit a une projection nulle sur l'axe horizontal."
                },
                {
                    "questionNumber": 55,
                    "question": "Une pyramide à base carrée de côté 3m et de hauteur 4m a pour volume :",
                    "answerOptions": [
                        {"text": "12 m³", "isCorrect": True},
                        {"text": "36 m³", "isCorrect": False},
                        {"text": "9 m³", "isCorrect": False},
                        {"text": "16 m³", "isCorrect": False}
                    ],
                    "correction": "(1/3) x Base x H = (1/3) x 9 x 4 = 12."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'instrument pour mesurer un angle ?",
                    "answerOptions": [
                        {"text": "Le rapporteur", "isCorrect": True},
                        {"text": "Le compas", "isCorrect": False},
                        {"text": "La règle", "isCorrect": False},
                        {"text": "Le thermomètre", "isCorrect": False}
                    ],
                    "correction": "Gradué en degrés."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle est la valeur de sin(30°) ?",
                    "answerOptions": [
                        {"text": "0,5", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "0,707", "isCorrect": False},
                        {"text": "0,866", "isCorrect": False}
                    ],
                    "correction": "C'est une valeur remarquable de la trigonométrie."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment s'appelle une droite qui touche un cercle en un seul point ?",
                    "answerOptions": [
                        {"text": "La tangente", "isCorrect": True},
                        {"text": "La sécante", "isCorrect": False},
                        {"text": "Le diamètre", "isCorrect": False},
                        {"text": "Le rayon", "isCorrect": False}
                    ],
                    "correction": "Elle est perpendiculaire au rayon passant par ce point."
                },
                {
                    "questionNumber": 59,
                    "question": "Un angle obtus est un angle :",
                    "answerOptions": [
                        {"text": "Supérieur à 90°", "isCorrect": True},
                        {"text": "Inférieur à 90°", "isCorrect": False},
                        {"text": "Égal à 90°", "isCorrect": False},
                        {"text": "Égal à 180°", "isCorrect": False}
                    ],
                    "correction": "Il est plus ouvert que l'angle droit."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle est l'aire totale d'un cube de côté 2cm ?",
                    "answerOptions": [
                        {"text": "24 cm²", "isCorrect": True},
                        {"text": "8 cm²", "isCorrect": False},
                        {"text": "4 cm²", "isCorrect": False},
                        {"text": "16 cm²", "isCorrect": False}
                    ],
                    "correction": "Il y a 6 faces de 4cm² chacune (6x4=24)."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : STATISTIQUES À DEUX VARIABLES ET AJUSTEMENT (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : STATISTIQUES À DEUX VARIABLES ET AJUSTEMENT",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Comment appelle-t-on le graphique représentant une série à deux variables ?",
                    "answerOptions": [
                        {"text": "Un nuage de points", "isCorrect": True},
                        {"text": "Un histogramme", "isCorrect": False},
                        {"text": "Un diagramme circulaire", "isCorrect": False},
                        {"text": "Une courbe de Gauss", "isCorrect": False}
                    ],
                    "correction": " Chaque point a pour coordonnées (xi ; yi)."
                },
                {
                    "questionNumber": 62,
                    "question": "Qu'est-ce que le point moyen G d'un nuage ?",
                    "answerOptions": [
                        {"text": "Le point dont les coordonnées sont les moyennes de x et de y", "isCorrect": True},
                        {"text": "Le point le plus haut du graphique", "isCorrect": False},
                        {"text": "Le point situé au milieu de l'axe x", "isCorrect": False},
                        {"text": "L'origine du repère", "isCorrect": False}
                    ],
                    "correction": "G(x̄ ; ȳ)."
                },
                {
                    "questionNumber": 63,
                    "question": "À quoi sert une droite d'ajustement ?",
                    "answerOptions": [
                        {"text": "À modéliser la tendance du nuage pour faire des prévisions", "isCorrect": True},
                        {"text": "À relier tous les points entre eux par des zigzags", "isCorrect": False},
                        {"text": "À décorer le graphique", "isCorrect": False},
                        {"text": "À calculer l'écart-type", "isCorrect": False}
                    ],
                    "correction": "On l'utilise pour estimer des valeurs futures (extrapolation)."
                },
                {
                    "questionNumber": 64,
                    "question": "Une corrélation est dite positive si :",
                    "answerOptions": [
                        {"text": "y augmente globalement quand x augmente", "isCorrect": True},
                        {"text": "y diminue quand x augmente", "isCorrect": False},
                        {"text": "y reste constant", "isCorrect": False},
                        {"text": "Tous les points sont alignés sur x", "isCorrect": False}
                    ],
                    "correction": "La droite d'ajustement monte."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle méthode permet de trouver l'équation de la droite d'ajustement la plus précise ?",
                    "answerOptions": [
                        {"text": "La méthode des moindres carrés", "isCorrect": True},
                        {"text": "La méthode de Mayer", "isCorrect": False},
                        {"text": "Le produit en croix", "isCorrect": False},
                        {"text": "La méthode au jugé", "isCorrect": False}
                    ],
                    "correction": "C'est la méthode utilisée par les calculatrices et tableurs."
                },
                {
                    "questionNumber": 66,
                    "question": "Que signifie un nuage de points très allongé ?",
                    "answerOptions": [
                        {"text": "Qu'il existe un lien fort entre les deux variables", "isCorrect": True},
                        {"text": "Que les données sont fausses", "isCorrect": False},
                        {"text": "Qu'il n'y a aucune relation", "isCorrect": False},
                        {"text": "Que la moyenne est nulle", "isCorrect": False}
                    ],
                    "correction": "L'ajustement linéaire est alors pertinent."
                },
                {
                    "questionNumber": 67,
                    "question": "Dans y = ax + b, si a est proche de 0, cela signifie :",
                    "answerOptions": [
                        {"text": "La variable y dépend peu de x", "isCorrect": True},
                        {"text": "Le lien est très fort", "isCorrect": False},
                        {"text": "La droite est verticale", "isCorrect": False},
                        {"text": "Toutes les valeurs sont positives", "isCorrect": False}
                    ],
                    "correction": "La droite est presque horizontale."
                },
                {
                    "questionNumber": 68,
                    "question": "Un coefficient de corrélation r proche de 1 signifie :",
                    "answerOptions": [
                        {"text": "Un fort lien linéaire positif", "isCorrect": True},
                        {"text": "Aucun lien", "isCorrect": False},
                        {"text": "Une erreur de calcul", "isCorrect": False},
                        {"text": "Un lien négatif", "isCorrect": False}
                    ],
                    "correction": "Les points sont presque parfaitement alignés sur une pente montante."
                },
                {
                    "questionNumber": 69,
                    "question": "Que permet l'interpolation ?",
                    "answerOptions": [
                        {"text": "Estimer une valeur entre deux données connues", "isCorrect": True},
                        {"text": "Prévoir le futur lointain", "isCorrect": False},
                        {"text": "Calculer la moyenne totale", "isCorrect": False},
                        {"text": "Changer les unités", "isCorrect": False}
                    ],
                    "correction": "On reste à l'intérieur de l'étendue des données."
                },
                {
                    "questionNumber": 70,
                    "question": "Le point moyen G appartient-il toujours à la droite d'ajustement ?",
                    "answerOptions": [
                        {"text": "Oui, par définition de la droite des moindres carrés", "isCorrect": True},
                        {"text": "Seulement si tous les points sont alignés", "isCorrect": False},
                        {"text": "Non, jamais", "isCorrect": False},
                        {"text": "Seulement si b est nul", "isCorrect": False}
                    ],
                    "correction": "C'est un point de passage obligé."
                },
                {
                    "questionNumber": 71,
                    "question": "Si r = -0,95, la corrélation est :",
                    "answerOptions": [
                        {"text": "Forte et négative", "isCorrect": True},
                        {"text": "Faible", "isCorrect": False},
                        {"text": "Positive", "isCorrect": False},
                        {"text": "Inexistante", "isCorrect": False}
                    ],
                    "correction": "y diminue fortement quand x augmente."
                },
                {
                    "questionNumber": 72,
                    "question": "Comment appelle-t-on les points du nuage qui sont très éloignés de la tendance générale ?",
                    "answerOptions": [
                        {"text": "Des points aberrants (ou atypiques)", "isCorrect": True},
                        {"text": "Des points moyens", "isCorrect": False},
                        {"text": "Des sommets", "isCorrect": False},
                        {"text": "Des origines", "isCorrect": False}
                    ],
                    "correction": "Ils peuvent fausser l'ajustement."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est l'unité du coefficient de corrélation r ?",
                    "answerOptions": [
                        {"text": "Il n'a pas d'unité", "isCorrect": True},
                        {"text": "En euros", "isCorrect": False},
                        {"text": "En pourcentages", "isCorrect": False},
                        {"text": "En mètres", "isCorrect": False}
                    ],
                    "correction": "C'est un nombre sans dimension compris entre -1 et 1."
                },
                {
                    "questionNumber": 74,
                    "question": "Que signifie extrapoler ?",
                    "answerOptions": [
                        {"text": "Estimer une valeur en dehors de l'intervalle des données connues", "isCorrect": True},
                        {"text": "Calculer la moyenne", "isCorrect": False},
                        {"text": "Réduire la taille du graphique", "isCorrect": False},
                        {"text": "Changer le nom des variables", "isCorrect": False}
                    ],
                    "correction": "C'est risqué car on suppose que la tendance va continuer."
                },
                {
                    "questionNumber": 75,
                    "question": "La droite d'ajustement passe par :",
                    "answerOptions": [
                        {"text": "Le point moyen G", "isCorrect": True},
                        {"text": "L'origine systématiquement", "isCorrect": False},
                        {"text": "Le point le plus haut uniquement", "isCorrect": False},
                        {"text": "Tous les points du nuage", "isCorrect": False}
                    ],
                    "correction": "Elle passe 'au milieu' du nuage."
                },
                {
                    "questionNumber": 76,
                    "question": "Si r = 0, cela signifie :",
                    "answerOptions": [
                        {"text": "Aucune corrélation linéaire", "isCorrect": True},
                        {"text": "Corrélation parfaite", "isCorrect": False},
                        {"text": "Toutes les valeurs sont nulles", "isCorrect": False},
                        {"text": "L'ajustement est une droite verticale", "isCorrect": False}
                    ],
                    "correction": "Le nuage forme un 'pâté' informe sans direction."
                },
                {
                    "questionNumber": 77,
                    "question": "Dans y = 2x + 10, si x augmente de 1, y augmente de :",
                    "answerOptions": [
                        {"text": "2", "isCorrect": True},
                        {"text": "10", "isCorrect": False},
                        {"text": "12", "isCorrect": False},
                        {"text": "1", "isCorrect": False}
                    ],
                    "correction": "C'est la définition du coefficient directeur."
                },
                {
                    "questionNumber": 78,
                    "question": "Un nuage de points peut être remplacé par une droite si :",
                    "answerOptions": [
                        {"text": "Sa forme est allongée", "isCorrect": True},
                        {"text": "Il n'y a que 2 points", "isCorrect": False},
                        {"text": "Il forme un cercle", "isCorrect": False},
                        {"text": "Les points sont tous sur l'axe y", "isCorrect": False}
                    ],
                    "correction": "C'est le critère de validité de l'ajustement linéaire."
                },
                {
                    "questionNumber": 79,
                    "question": "La variable expliquée est généralement placée sur :",
                    "answerOptions": [
                        {"text": "L'axe des ordonnées (y)", "isCorrect": True},
                        {"text": "L'axe des abscisses (x)", "isCorrect": False},
                        {"text": "Le titre", "isCorrect": False},
                        {"text": "La légende", "isCorrect": False}
                    ],
                    "correction": "On étudie y en fonction de x."
                },
                {
                    "questionNumber": 80,
                    "question": "Le coefficient b de y = ax + b est :",
                    "answerOptions": [
                        {"text": "L'ordonnée à l'origine", "isCorrect": True},
                        {"text": "La pente", "isCorrect": False},
                        {"text": "La moyenne", "isCorrect": False},
                        {"text": "Le nombre de points", "isCorrect": False}
                    ],
                    "correction": "C'est la valeur de y quand x = 0."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : PROBABILITÉS ET LOI BINOMIALE (Q81 à Q100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : PROBABILITÉS ET LOI BINOMIALE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Qu'est-ce qu'une épreuve de Bernoulli ?",
                    "answerOptions": [
                        {"text": "Une expérience aléatoire avec seulement deux issues (succès/échec)", "isCorrect": True},
                        {"text": "Une épreuve sportive", "isCorrect": False},
                        {"text": "Un calcul de moyenne complexe", "isCorrect": False},
                        {"text": "Un tirage au sort infini", "isCorrect": False}
                    ],
                    "correction": "Exemple : pile ou face, produit défectueux ou non."
                },
                {
                    "questionNumber": 82,
                    "question": "Dans une loi binomiale B(n ; p), que représente 'n' ?",
                    "answerOptions": [
                        {"text": "Le nombre de répétitions indépendantes de l'épreuve", "isCorrect": True},
                        {"text": "La probabilité de succès", "isCorrect": False},
                        {"text": "Le nombre de succès obtenus", "isCorrect": False},
                        {"text": "La moyenne de la série", "isCorrect": False}
                    ],
                    "correction": "C'est la taille de l'échantillon testé."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la probabilité de l'échec (notée q) si la probabilité de succès p est 0,2 ?",
                    "answerOptions": [
                        {"text": "0,8", "isCorrect": True},
                        {"text": "0,2", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False}
                    ],
                    "correction": "q = 1 - p. La somme des deux probabilités vaut toujours 1."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment calcule-t-on l'espérance E(X) d'une loi binomiale ?",
                    "answerOptions": [
                        {"text": "n x p", "isCorrect": True},
                        {"text": "n + p", "isCorrect": False},
                        {"text": "p / n", "isCorrect": False},
                        {"text": "n x p x q", "isCorrect": False}
                    ],
                    "correction": "L'espérance correspond au nombre moyen de succès que l'on peut attendre sur n essais."
                },
                {
                    "questionNumber": 85,
                    "question": "Pour utiliser une loi binomiale, les tirages doivent être :",
                    "answerOptions": [
                        {"text": "Indépendants (avec remise)", "isCorrect": True},
                        {"text": "Liés entre eux", "isCorrect": False},
                        {"text": "Uniques", "isCorrect": False},
                        {"text": "Faits par la même personne", "isCorrect": False}
                    ],
                    "correction": "La probabilité de succès ne doit pas changer d'un tirage à l'autre."
                },
                {
                    "questionNumber": 86,
                    "question": "Que représente la variable aléatoire X dans une loi binomiale ?",
                    "answerOptions": [
                        {"text": "Le nombre de succès obtenus sur n épreuves", "isCorrect": True},
                        {"text": "Le temps d'attente avant le premier succès", "isCorrect": False},
                        {"text": "Le résultat du dernier tirage", "isCorrect": False},
                        {"text": "Le prix total de l'expérience", "isCorrect": False}
                    ],
                    "correction": "X peut prendre des valeurs entières de 0 à n."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la valeur de P(X=0) si n=3 et p=0,5 ?",
                    "answerOptions": [
                        {"text": "0,125", "isCorrect": True},
                        {"text": "0,5", "isCorrect": False},
                        {"text": "0", "isCorrect": False},
                        {"text": "0,25", "isCorrect": False}
                    ],
                    "correction": "0,5 x 0,5 x 0,5 = 0,125 (aucun succès sur 3 essais)."
                },
                {
                    "questionNumber": 88,
                    "question": "Sur une calculatrice, quelle fonction donne P(X = k) ?",
                    "answerOptions": [
                        {"text": "binomPdf", "isCorrect": True},
                        {"text": "binomCdf", "isCorrect": False},
                        {"text": "NormalCdf", "isCorrect": False},
                        {"text": "LinReg", "isCorrect": False}
                    ],
                    "correction": "Pdf pour une valeur précise (Point), Cdf pour une valeur cumulée."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la somme P(X=0) + P(X=1) + ... + P(X=n) ?",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "n", "isCorrect": False},
                        {"text": "p", "isCorrect": False},
                        {"text": "0", "isCorrect": False}
                    ],
                    "correction": "La somme de toutes les probabilités d'une loi est toujours 1."
                },
                {
                    "questionNumber": 90,
                    "question": "Qu'est-ce qu'un arbre pondéré ?",
                    "answerOptions": [
                        {"text": "Un schéma représentant les issues avec leurs probabilités", "isCorrect": True},
                        {"text": "Un arbre qui pousse dans le jardin du mathématicien", "isCorrect": False},
                        {"text": "Un graphique avec des barres lourdes", "isCorrect": False},
                        {"text": "Une liste de nombres classés", "isCorrect": False}
                    ],
                    "correction": "Il aide à visualiser les chemins de succès et d'échec."
                },
                {
                    "questionNumber": 91,
                    "question": "Que signifie P(X ≤ 2) ?",
                    "answerOptions": [
                        {"text": "P(X=0) + P(X=1) + P(X=2)", "isCorrect": True},
                        {"text": "P(X=2) uniquement", "isCorrect": False},
                        {"text": "1 - P(X=2)", "isCorrect": False},
                        {"text": "La probabilité d'avoir au moins 2 succès", "isCorrect": False}
                    ],
                    "correction": "C'est la probabilité d'avoir AU PLUS 2 succès."
                },
                {
                    "questionNumber": 92,
                    "question": "L'écart-type d'une loi binomiale mesure :",
                    "answerOptions": [
                        {"text": "La dispersion autour de l'espérance", "isCorrect": True},
                        {"text": "Le nombre de tirages", "isCorrect": False},
                        {"text": "La réussite totale", "isCorrect": False},
                        {"text": "L'erreur de calcul", "isCorrect": False}
                    ],
                    "correction": "Formule : σ = √(n x p x q)."
                },
                {
                    "questionNumber": 93,
                    "question": "Si n = 100 et p = 0,1, combien de succès peut-on espérer en moyenne ?",
                    "answerOptions": [
                        {"text": "10", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "50", "isCorrect": False},
                        {"text": "100", "isCorrect": False}
                    ],
                    "correction": "E(X) = 100 x 0,1 = 10."
                },
                {
                    "questionNumber": 94,
                    "question": "Dans un arbre de probabilités, la somme des branches partant d'un même nœud vaut :",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False},
                        {"text": "p", "isCorrect": False}
                    ],
                    "correction": "C'est la règle des nœuds en probabilité."
                },
                {
                    "questionNumber": 95,
                    "question": "Que signifie l'événement contraire de 'obtenir au moins un succès' ?",
                    "answerOptions": [
                        {"text": "Obtenir zéro succès", "isCorrect": True},
                        {"text": "Obtenir n succès", "isCorrect": False},
                        {"text": "Obtenir un échec au dernier tirage", "isCorrect": False},
                        {"text": "Ne pas participer", "isCorrect": False}
                    ],
                    "correction": "P(X ≥ 1) = 1 - P(X = 0)."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle touche permet d'obtenir les coefficients a et b de la droite de régression ?",
                    "answerOptions": [
                        {"text": "LinReg (ax+b)", "isCorrect": True},
                        {"text": "Stats", "isCorrect": False},
                        {"text": "Proba", "isCorrect": False},
                        {"text": "Graph", "isCorrect": False}
                    ],
                    "correction": "Fonction standard des calculatrices de lycée."
                },
                {
                    "questionNumber": 97,
                    "question": "Si on tire une carte dans un jeu de 32, l'événement 'Tirer un Coeur' et 'Tirer un Pique' sont :",
                    "answerOptions": [
                        {"text": "Incompatibles", "isCorrect": True},
                        {"text": "Indépendants", "isCorrect": False},
                        {"text": "Complémentaires", "isCorrect": False},
                        {"text": "Identiques", "isCorrect": False}
                    ],
                    "correction": "Une carte ne peut pas être à la fois Cœur et Pique."
                },
                {
                    "questionNumber": 98,
                    "question": "Une variable aléatoire X suit une loi binomiale si :",
                    "answerOptions": [
                        {"text": "On répète n fois une épreuve de Bernoulli identique et indépendante", "isCorrect": True},
                        {"text": "On tire des boules sans remise", "isCorrect": False},
                        {"text": "La probabilité change à chaque tirage", "isCorrect": False},
                        {"text": "On a une infinité d'issues possibles", "isCorrect": False}
                    ],
                    "correction": "Il faut vérifier les conditions : répétition, indépendance, succès/échec."
                },
                {
                    "questionNumber": 99,
                    "question": "L'espérance mathématique E(X) correspond concrètement à :",
                    "answerOptions": [
                        {"text": "La moyenne théorique sur un grand nombre d'essais", "isCorrect": True},
                        {"text": "La valeur maximale possible", "isCorrect": False},
                        {"text": "Le coût du jeu", "isCorrect": False},
                        {"text": "La probabilité de gagner", "isCorrect": False}
                    ],
                    "correction": "Si E(X) = 0, le jeu est dit équitable."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la probabilité d'obtenir au moins un succès lors de n épreuves ?",
                    "answerOptions": [
                        {"text": "1 - P(X = 0)", "isCorrect": True},
                        {"text": "P(X = 1)", "isCorrect": False},
                        {"text": "1 - P(X = n)", "isCorrect": False},
                        {"text": "P(X = 0)", "isCorrect": False}
                    ],
                    "correction": "L'événement 'au moins un succès' est le contraire de 'zéro succès'. Sa probabilité se calcule donc par soustraction à partir de 1."
                }
            ]
        }
    }
}