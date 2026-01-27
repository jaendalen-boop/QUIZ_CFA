quiz_data = {
    "title": "Quiz Bac Pro Mathématiques (100 Questions) - Version Optimisée",
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
                        {"text": "La médiane de la série statistique étudiée", "isCorrect": True},
                        {"text": "La moyenne arithmétique de la série de données", "isCorrect": False},
                        {"text": "Le premier quartile de la distribution observée", "isCorrect": False},
                        {"text": "L'étendue globale de la série de valeurs mesurées", "isCorrect": False}
                    ],
                    "correction": "Dans une série ordonnée (du plus petit au plus grand), la médiane est la valeur centrale. Elle partage l'effectif total en deux groupes égaux : 50 % des valeurs sont inférieures ou égales à la médiane et 50 % sont supérieures ou égales. Contrairement à la moyenne, elle n'est pas influencée par les valeurs extrêmes."
                },
                {
                    "questionNumber": 2,
                    "question": "On lance un dé équilibré à six faces. Quelle est la probabilité d'obtenir un chiffre pair ?",
                    "answerOptions": [
                        {"text": "Une probabilité égale à 0,5 ou un demi", "isCorrect": True},
                        {"text": "La probabilité est de un tiers des issues", "isCorrect": False},
                        {"text": "On a deux chances sur six d'obtenir ce résultat", "isCorrect": False},
                        {"text": "Il existe une seule chance sur six d'obtenir un pair", "isCorrect": False}
                    ],
                    "correction": "Sur un dé à 6 faces, il y a 3 issues favorables (les chiffres 2, 4 et 6) sur un total de 6 issues possibles. La probabilité est donc de 3/6, ce qui se simplifie en 1/2 ou 0,5 (soit 50 % de chances)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle formule permet de calculer l'étendue d'une série statistique ?",
                    "answerOptions": [
                        {"text": "La valeur maximale moins la valeur minimale", "isCorrect": True},
                        {"text": "La somme des valeurs divisée par l'effectif total", "isCorrect": False},
                        {"text": "La valeur du troisième quartile moins le premier", "isCorrect": False},
                        {"text": "La valeur la plus haute de la série divisée par deux", "isCorrect": False}
                    ],
                    "correction": "L'étendue est un indicateur de dispersion très simple. Elle correspond à l'écart entre les deux valeurs extrêmes d'une série. Plus l'étendue est grande, plus les données de la population étudiée sont étalées."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment appelle-t-on le quotient de l'effectif d'une valeur par l'effectif total ?",
                    "answerOptions": [
                        {"text": "La fréquence de la valeur dans la série", "isCorrect": True},
                        {"text": "Le pourcentage arrondi de la valeur choisie", "isCorrect": False},
                        {"text": "La variance des données autour du centre", "isCorrect": False},
                        {"text": "L'écart-type de la distribution statistique", "isCorrect": False}
                    ],
                    "correction": "La fréquence f est égale au rapport n/N (effectif de la valeur / effectif total). C'est un nombre toujours compris entre 0 et 1. Pour l'obtenir en pourcentage, il suffit de multiplier ce résultat par 100."
                },
                {
                    "questionNumber": 5,
                    "question": "Dans un diagramme en boîte (boîte à moustaches), que représente la boîte centrale ?",
                    "answerOptions": [
                        {"text": "L'intervalle interquartile compris entre Q1 et Q3", "isCorrect": True},
                        {"text": "L'étendue globale de l'ensemble de la distribution", "isCorrect": False},
                        {"text": "La valeur précise de la moyenne de la population", "isCorrect": False},
                        {"text": "L'écart total entre le minimum et le maximum", "isCorrect": False}
                    ],
                    "correction": "La boîte centrale représente les 50 % centraux de la série statistique. Ses bords correspondent au premier quartile (Q1) et au troisième quartile (Q3). La longueur de cette boîte est appelée l'écart interquartile."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la probabilité d'un événement certain ?",
                    "answerOptions": [
                        {"text": "Une probabilité égale à 1 ou cent pour cent", "isCorrect": True},
                        {"text": "Une probabilité égale à 0 en l'absence de doute", "isCorrect": False},
                        {"text": "Un score de 100 points sur l'échelle de mesure", "isCorrect": False},
                        {"text": "Une valeur de 0,5 représentant la moitié des cas", "isCorrect": False}
                    ],
                    "correction": "En probabilité, la mesure d'un événement se situe toujours entre 0 (événement impossible) et 1 (événement certain). Si un événement se réalise dans tous les cas possibles, sa probabilité est de 1."
                },
                {
                    "questionNumber": 7,
                    "question": "Si deux événements A et B sont incompatibles, quelle est la probabilité de (A ou B) ?",
                    "answerOptions": [
                        {"text": "La somme des probabilités P(A) + P(B)", "isCorrect": True},
                        {"text": "Le produit des probabilités P(A) fois P(B)", "isCorrect": False},
                        {"text": "La différence des probabilités P(A) moins P(B)", "isCorrect": False},
                        {"text": "Un résultat nul égal à zéro dans tous les cas", "isCorrect": False}
                    ],
                    "correction": "Deux événements sont dits incompatibles s'ils n'ont aucune issue en commun (ils ne peuvent pas se produire simultanément). Dans ce cas, la probabilité que l'un ou l'autre se réalise est simplement l'addition de leurs probabilités respectives."
                },
                {
                    "questionNumber": 8,
                    "question": "Comment calcule-t-on la moyenne arithmétique d'une série ?",
                    "answerOptions": [
                        {"text": "La somme des valeurs divisée par l'effectif total", "isCorrect": True},
                        {"text": "L'effectif total divisé par la somme des valeurs", "isCorrect": False},
                        {"text": "La somme du max et du min divisée par deux", "isCorrect": False},
                        {"text": "La valeur centrale séparant la série en deux", "isCorrect": False}
                    ],
                    "correction": "La moyenne est le point d'équilibre d'une série. Pour l'obtenir, on additionne toutes les données et on divise par le nombre total d'individus. Si les valeurs ont des coefficients (effectifs), on calcule alors une moyenne pondérée."
                },
                {
                    "questionNumber": 9,
                    "question": "Que mesure l'écart-type d'une série statistique ?",
                    "answerOptions": [
                        {"text": "La dispersion des valeurs autour de la moyenne", "isCorrect": True},
                        {"text": "La valeur centrale séparant la série étudiée", "isCorrect": False},
                        {"text": "La valeur la plus fréquente de la distribution", "isCorrect": False},
                        {"text": "La somme totale de l'ensemble des données", "isCorrect": False}
                    ],
                    "correction": "L'écart-type (noté σ) mesure si les données sont proches ou éloignées de la moyenne. Un petit écart-type signifie que la série est homogène (les valeurs sont regroupées autour de la moyenne), tandis qu'un grand écart-type indique une série hétérogène."
                },
                {
                    "questionNumber": 10,
                    "question": "Le premier quartile Q1 correspond à quelle part de l'effectif total ?",
                    "answerOptions": [
                        {"text": "À au moins vingt-cinq pour cent des données", "isCorrect": True},
                        {"text": "Exactement à cinquante pour cent de l'effectif", "isCorrect": False},
                        {"text": "À au moins soixante-quinze pour cent des cas", "isCorrect": False},
                        {"text": "À la totalité de la population statistique globale", "isCorrect": False}
                    ],
                    "correction": "Le premier quartile Q1 est la plus petite valeur de la série telle qu'au moins 25 % des données soient inférieures ou égales à cette valeur. On l'utilise pour observer la dispersion des valeurs les plus faibles de la série."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la probabilité de tirer un 'As' dans un jeu de 32 cartes ?",
                    "answerOptions": [
                        {"text": "Un rapport de 4 sur 32 soit une valeur de 0,125", "isCorrect": True},
                        {"text": "Une chance unique sur les 32 cartes disponibles", "isCorrect": False},
                        {"text": "Un rapport de 4 sur 52 selon le jeu complet", "isCorrect": False},
                        {"text": "Un quart de chances représenté par la valeur 0,25", "isCorrect": False}
                    ],
                    "correction": "Dans un jeu de 32 cartes, il y a 4 As (Trèfle, Carreau, Cœur, Pique). La probabilité est donc de 4/32. En simplifiant la fraction, on obtient 1/8, ce qui correspond au nombre décimal 0,125."
                },
                {
                    "questionNumber": 12,
                    "question": "Qu'est-ce qu'une expérience aléatoire en mathématiques ?",
                    "answerOptions": [
                        {"text": "Une expérience dont on ne peut prévoir le résultat", "isCorrect": True},
                        {"text": "Une expérience réalisée en laboratoire scientifique", "isCorrect": False},
                        {"text": "Un calcul mathématique complexe sans inconnu", "isCorrect": False},
                        {"text": "Une mesure physique réalisée avec une règle plate", "isCorrect": False}
                    ],
                    "correction": "Une expérience est aléatoire quand on connaît parfaitement toutes les issues possibles (ex: obtenir 1, 2, 3, 4, 5 ou 6 au dé), mais qu'il est impossible de prédire avec certitude laquelle se produira lors d'un essai donné."
                },
                {
                    "questionNumber": 13,
                    "question": "La somme des probabilités de toutes les issues d'une expérience vaut toujours :",
                    "answerOptions": [
                        {"text": "La valeur entière égale à un", "isCorrect": True},
                        {"text": "La valeur nulle égale à zéro", "isCorrect": False},
                        {"text": "La valeur cent sur l'échelle de mesure", "isCorrect": False},
                        {"text": "Une valeur variable selon les types d'issues", "isCorrect": False}
                    ],
                    "correction": "Il s'agit d'une règle fondamentale : l'ensemble des issues possibles (l'univers) représente la certitude. Si on additionne les probabilités de chaque résultat possible d'une expérience, on doit impérativement trouver 1 (soit 100 %)."
                },
                {
                    "questionNumber": 14,
                    "question": "Que signifie un échantillon représentatif lors d'un sondage ?",
                    "answerOptions": [
                        {"text": "Une partie possédant les mêmes caractéristiques globales", "isCorrect": True},
                        {"text": "Le groupe le plus nombreux possible de la population", "isCorrect": False},
                        {"text": "Uniquement les personnes qui sont d'accord avec nous", "isCorrect": False},
                        {"text": "Une sélection au hasard total sans aucun critère précis", "isCorrect": False}
                    ],
                    "correction": "Pour que les résultats d'un sondage soient valables pour toute une population, l'échantillon interrogé doit refléter la diversité de celle-ci (âge, sexe, profession). C'est ce qui permet de limiter les biais statistiques."
                },
                {
                    "questionNumber": 15,
                    "question": "Sur un diagramme circulaire, l'angle de chaque secteur est proportionnel à :",
                    "answerOptions": [
                        {"text": "L'effectif ou la fréquence de la donnée représentée", "isCorrect": True},
                        {"text": "La valeur numérique de la donnée en elle-même", "isCorrect": False},
                        {"text": "La moyenne arithmétique de l'ensemble de la série", "isCorrect": False},
                        {"text": "Rien du tout, les angles sont fixés de manière libre", "isCorrect": False}
                    ],
                    "correction": "Dans un 'camembert', l'angle α (en degrés) d'un secteur se calcule par la formule : α = Fréquence x 360°. Plus la fréquence d'une valeur est élevée, plus la part qu'elle occupe sur le disque est importante."
                },
                {
                    "questionNumber": 16,
                    "question": "Comment calcule-t-on théoriquement le troisième quartile Q3 ?",
                    "answerOptions": [
                        {"text": "La valeur pour laquelle au moins 75% sont inférieurs", "isCorrect": True},
                        {"text": "La valeur exacte située au milieu de la distribution", "isCorrect": False},
                        {"text": "La valeur de la moyenne augmentée de l'écart-type", "isCorrect": False},
                        {"text": "Le triple de la valeur obtenue pour le premier quartile", "isCorrect": False}
                    ],
                    "correction": "Le troisième quartile Q3 est la valeur de la série telle qu'au moins 75 % des données soient inférieures ou égales à celle-ci. Pour le trouver, on classe les données dans l'ordre croissant et on cherche la valeur correspondant au rang (0,75 x Effectif total)."
                },
                {
                    "questionNumber": 17,
                    "question": "Un événement A a une probabilité de 0,3. Quelle est la probabilité de son contraire ?",
                    "answerOptions": [
                        {"text": "Une probabilité complémentaire égale à 0,7", "isCorrect": True},
                        {"text": "Une probabilité identique égale à la valeur 0,3", "isCorrect": False},
                        {"text": "Une probabilité totale égale à la valeur de 1", "isCorrect": False},
                        {"text": "Une valeur négative égale à l'opposé de -0,3", "isCorrect": False}
                    ],
                    "correction": "La probabilité d'un événement contraire (noté Ā) se calcule en soustrayant la probabilité de l'événement à 1. Soit P(Ā) = 1 - P(A). Ici, 1 - 0,3 = 0,7. La somme des deux probabilités vaut bien 1."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la définition du mode d'une série statistique ?",
                    "answerOptions": [
                        {"text": "La valeur qui possède le plus grand effectif associé", "isCorrect": True},
                        {"text": "La moyenne arithmétique entre les deux valeurs extrêmes", "isCorrect": False},
                        {"text": "La différence calculée entre le quartile Q3 et le Q1", "isCorrect": False},
                        {"text": "La valeur la plus petite rencontrée dans la série totale", "isCorrect": False}
                    ],
                    "correction": "Le mode (ou la dominante) est la valeur la plus fréquente dans une série. Dans un tableau d'effectifs, il s'agit de la valeur de la colonne où l'effectif est le plus élevé. Une série peut parfois posséder plusieurs modes."
                },
                {
                    "questionNumber": 19,
                    "question": "Qu'est-ce qu'une variable qualitative en statistiques ?",
                    "answerOptions": [
                        {"text": "Une donnée non numérique comme la couleur ou la marque", "isCorrect": True},
                        {"text": "Une donnée numérique avec des chiffres après la virgule", "isCorrect": False},
                        {"text": "Le prix monétaire unitaire d'un article en magasin", "isCorrect": False},
                        {"text": "La durée mesurée en minutes d'un trajet quotidien", "isCorrect": False}
                    ],
                    "correction": "Une variable qualitative décrit une qualité ou une catégorie (ex: sexe, couleur des yeux, marque de voiture). Contrairement à une variable quantitative, on ne peut pas réaliser de calculs arithmétiques directs (comme une moyenne) sur ces catégories."
                },
                {
                    "questionNumber": 20,
                    "question": "Si on lance deux fois de suite une pièce, combien y a-t-il d'issues ?",
                    "answerOptions": [
                        {"text": "Un total de quatre issues possibles pour l'expérience", "isCorrect": True},
                        {"text": "Seulement deux issues pour l'ensemble des lancers", "isCorrect": False},
                        {"text": "Un total de huit issues selon le principe multiplicatif", "isCorrect": False},
                        {"text": "Seulement trois issues possibles pour ce type de test", "isCorrect": False}
                    ],
                    "correction": "Chaque lancer a 2 issues (Pile ou Face). Pour deux lancers, on multiplie les possibilités : 2 x 2 = 4. Les issues sont : (P,P), (P,F), (F,P) et (F,F). Chaque couple de résultats a une chance sur quatre de se produire."
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
                        {"text": "L'expression f(x) = ax + b pour tout réel x", "isCorrect": True},
                        {"text": "L'expression f(x) = ax² pour les formes courbes", "isCorrect": False},
                        {"text": "L'expression f(x) = a divisé par la variable x", "isCorrect": False},
                        {"text": "L'expression f(x) = x additionné à la valeur b²", "isCorrect": False}
                    ],
                    "correction": "Une fonction affine est définie par deux paramètres : 'a' (le coefficient directeur) et 'b' (l'ordonnée à l'origine). Sa représentation graphique est toujours une droite qui ne passe pas forcément par l'origine du repère."
                },
                {
                    "questionNumber": 22,
                    "question": "Que représente concrètement la lettre 'a' dans f(x) = ax + b ?",
                    "answerOptions": [
                        {"text": "Le coefficient directeur définissant la pente de la droite", "isCorrect": True},
                        {"text": "L'ordonnée à l'origine pointant le croisement vertical", "isCorrect": False},
                        {"text": "L'image du chiffre zéro par la fonction étudiée ici", "isCorrect": False},
                        {"text": "L'inconnue principale que l'on cherche à déterminer", "isCorrect": False}
                    ],
                    "correction": "Le coefficient directeur 'a' indique l'inclinaison de la droite. Si 'a' est positif, la fonction monte (croissante). Si 'a' est négatif, la fonction descend (décroissante). Si 'a' est nul, la fonction est constante (droite horizontale)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la particularité graphique d'une fonction linéaire ?",
                    "answerOptions": [
                        {"text": "Sa droite passe obligatoirement par l'origine (0 ; 0)", "isCorrect": True},
                        {"text": "Elle est toujours décroissante sur son ensemble de définition", "isCorrect": False},
                        {"text": "Elle forme une courbe en forme de lettre U appelée parabole", "isCorrect": False},
                        {"text": "Elle ne possède aucun coefficient directeur sur le graphique", "isCorrect": False}
                    ],
                    "correction": "Une fonction linéaire est un cas particulier de fonction affine où b = 0 (type f(x) = ax). Elle traduit une situation de proportionnalité directe. Sa représentation graphique est une droite passant toujours par le point O(0,0)."
                },
                {
                    "questionNumber": 24,
                    "question": "Dans f(x) = 2x - 5, quelle est l'ordonnée à l'origine ?",
                    "answerOptions": [
                        {"text": "La valeur entière négative égale à -5", "isCorrect": True},
                        {"text": "Le coefficient directeur égal à la valeur 2", "isCorrect": False},
                        {"text": "La valeur nulle égale au chiffre zéro", "isCorrect": False},
                        {"text": "La variable x représentant l'abscisse du point", "isCorrect": False}
                    ],
                    "correction": "L'ordonnée à l'origine est la valeur de 'b' dans f(x) = ax + b. C'est l'ordonnée du point où la droite coupe l'axe vertical (l'axe des ordonnées). Ici, si x = 0, alors f(0) = 2*0 - 5 = -5."
                },
                {
                    "questionNumber": 25,
                    "question": "Résoudre l'équation du premier degré : 3x + 2 = 11.",
                    "answerOptions": [
                        {"text": "La valeur de l'inconnue x est égale à 3", "isCorrect": True},
                        {"text": "La valeur de l'inconnue x est égale à 4", "isCorrect": False},
                        {"text": "La valeur de l'inconnue x est égale à 9", "isCorrect": False},
                        {"text": "La valeur de l'inconnue x est égale à 33", "isCorrect": False}
                    ],
                    "correction": "Étapes de résolution : 1) On soustrait 2 de chaque côté : 3x = 11 - 2 = 9. 2) On divise par 3 pour isoler x : x = 9 / 3 = 3. La solution de l'équation est donc 3."
                },
                {
                    "questionNumber": 26,
                    "question": "Si a > 0, la fonction affine f(x) = ax + b est :",
                    "answerOptions": [
                        {"text": "Strictement croissante sur son ensemble de définition", "isCorrect": True},
                        {"text": "Strictement décroissante sur son ensemble de définition", "isCorrect": False},
                        {"text": "Constante quelle que soit la valeur de la variable x", "isCorrect": False},
                        {"text": "Nulle pour l'ensemble des points du graphique tracé", "isCorrect": False}
                    ],
                    "correction": "Le signe de 'a' détermine le sens de variation. Si 'a' est supérieur à zéro, alors lorsque les valeurs de x augmentent, les images f(x) augmentent également. La droite 'monte' de gauche à droite."
                },
                {
                    "questionNumber": 27,
                    "question": "Que signifie graphiquement résoudre l'équation f(x) = g(x) ?",
                    "answerOptions": [
                        {"text": "Chercher l'abscisse du point d'intersection des courbes", "isCorrect": True},
                        {"text": "Additionner les deux fonctions pour créer un nouveau tracé", "isCorrect": False},
                        {"text": "Multiplier les ordonnées des deux fonctions au même point", "isCorrect": False},
                        {"text": "Tracer une droite parallèle à l'axe des abscisses", "isCorrect": False}
                    ],
                    "correction": "Résoudre f(x) = g(x) revient à trouver les valeurs de x pour lesquelles les deux fonctions prennent la même valeur. Visuellement, ce sont les abscisses (sur l'axe horizontal) des points où les deux courbes se croisent."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la valeur de x pour laquelle l'équation 2x = 0 est vraie ?",
                    "answerOptions": [
                        {"text": "La valeur entière nulle égale à zéro", "isCorrect": True},
                        {"text": "La valeur entière égale au chiffre deux", "isCorrect": False},
                        {"text": "La valeur entière négative égale à moins deux", "isCorrect": False},
                        {"text": "C'est une situation mathématique impossible", "isCorrect": False}
                    ],
                    "correction": "Pour trouver x, on divise par 2 : x = 0 / 2. Puisque zéro divisé par n'importe quel nombre non nul donne zéro, la solution unique est x = 0."
                },
                {
                    "questionNumber": 29,
                    "question": "Développer l'expression algébrique suivante : 4(x - 3).",
                    "answerOptions": [
                        {"text": "L'expression développée égale à 4x - 12", "isCorrect": True},
                        {"text": "L'expression développée égale à 4x - 3", "isCorrect": False},
                        {"text": "L'expression développée égale à x - 12", "isCorrect": False},
                        {"text": "L'expression développée égale à 4x + 12", "isCorrect": False}
                    ],
                    "correction": "On utilise la distributivité simple : on multiplie le facteur 4 par chaque terme à l'intérieur de la parenthèse. 4 * x = 4x et 4 * (-3) = -12. On obtient ainsi 4x - 12."
                },
                {
                    "questionNumber": 30,
                    "question": "Un produit coûte x €. Son prix augmente de 20%. Quelle est l'expression du nouveau prix ?",
                    "answerOptions": [
                        {"text": "Le nouveau prix est égal à 1,20x", "isCorrect": True},
                        {"text": "Le nouveau prix est égal à x + 20", "isCorrect": False},
                        {"text": "Le nouveau prix est égal à 0,20x", "isCorrect": False},
                        {"text": "Le nouveau prix est égal à x + 1,20", "isCorrect": False}
                    ],
                    "correction": "Augmenter de 20 % revient à ajouter 0,20x au prix initial x. On calcule : x + 0,20x = (1 + 0,20)x = 1,20x. Multiplier par 1,20 est donc le coefficient multiplicateur associé à une hausse de 20 %."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est l'inverse mathématique du nombre 5 ?",
                    "answerOptions": [
                        {"text": "La fraction 1/5 ou le nombre décimal 0,2", "isCorrect": True},
                        {"text": "L'opposé du nombre égale à la valeur -5", "isCorrect": False},
                        {"text": "L'identité identique égale à la valeur 5", "isCorrect": False},
                        {"text": "Le nombre décimal égal à la valeur 0,5", "isCorrect": False}
                    ],
                    "correction": "L'inverse d'un nombre non nul n est le nombre qui, multiplié par n, donne 1. Cet inverse est noté 1/n. Pour 5, l'inverse est 1/5, soit 0,2. À ne pas confondre avec l'opposé qui est -5."
                },
                {
                    "questionNumber": 32,
                    "question": "Que vaut le carré x² si la variable x est égale à -3 ?",
                    "answerOptions": [
                        {"text": "La valeur entière positive égale à 9", "isCorrect": True},
                        {"text": "La valeur entière négative égale à -9", "isCorrect": False},
                        {"text": "Le produit des deux égal à la valeur 6", "isCorrect": False},
                        {"text": "Le produit négatif égal à la valeur -6", "isCorrect": False}
                    ],
                    "correction": "Le carré d'un nombre est le produit de ce nombre par lui-même. Ici : (-3) * (-3). D'après la règle des signes (moins par moins donne plus), le résultat est 9. Un carré réel est toujours positif ou nul."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la solution de l'équation simple : 5x = 10 ?",
                    "answerOptions": [
                        {"text": "La solution est égale au chiffre deux", "isCorrect": True},
                        {"text": "La solution est égale au chiffre cinq", "isCorrect": False},
                        {"text": "La solution est égale au nombre 0,5", "isCorrect": False},
                        {"text": "La solution est égale au nombre cinquante", "isCorrect": False}
                    ],
                    "correction": "Pour isoler x, on effectue l'opération inverse de la multiplication par 5, c'est-à-dire la division par 5. x = 10 / 5 = 2. La solution de l'équation est donc 2."
                },
                {
                    "questionNumber": 34,
                    "question": "Graphiquement, une fonction constante est représentée par :",
                    "answerOptions": [
                        {"text": "Une droite horizontale parallèle à l'axe des abscisses", "isCorrect": True},
                        {"text": "Une droite verticale parallèle à l'axe des ordonnées", "isCorrect": False},
                        {"text": "Une droite oblique passant obligatoirement par l'origine", "isCorrect": False},
                        {"text": "Une courbe quelconque sans direction spécifique", "isCorrect": False}
                    ],
                    "correction": "Une fonction constante (type f(x) = b) a une image qui ne change jamais, quelle que soit la valeur de x choisie. Tous les points ont la même ordonnée, ce qui forme une droite horizontale."
                },
                {
                    "questionNumber": 35,
                    "question": "Résoudre l'équation suivante : x + 7 = 3.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à moins quatre", "isCorrect": True},
                        {"text": "La valeur de x est égale au chiffre quatre", "isCorrect": False},
                        {"text": "La valeur de x est égale au nombre dix", "isCorrect": False},
                        {"text": "La valeur de x est égale au nombre moins dix", "isCorrect": False}
                    ],
                    "correction": "On isole x en déplaçant le +7 de l'autre côté de l'égal, ce qui le transforme en -7. x = 3 - 7. Le résultat est -4. Vérification : -4 + 7 donne bien 3."
                },
                {
                    "questionNumber": 36,
                    "question": "En algèbre, que signifie l'expression 'isoler l'inconnue' ?",
                    "answerOptions": [
                        {"text": "Faire en sorte que x soit seul d'un côté de l'égal", "isCorrect": True},
                        {"text": "Supprimer définitivement la variable x de l'équation", "isCorrect": False},
                        {"text": "Remplacer systématiquement la variable x par zéro", "isCorrect": False},
                        {"text": "Changer le nom de la variable par une autre lettre", "isCorrect": False}
                    ],
                    "correction": "Isoler x est le but final de la résolution d'une équation. Par une suite d'opérations autorisées (addition, soustraction, multiplication, division des deux côtés), on arrive à une forme 'x = nombre', ce qui donne la solution."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle est l'image de 3 par la fonction f(x) = 4x - 1 ?",
                    "answerOptions": [
                        {"text": "La valeur entière égale à onze", "isCorrect": True},
                        {"text": "La valeur entière égale à douze", "isCorrect": False},
                        {"text": "La valeur entière égale au chiffre huit", "isCorrect": False},
                        {"text": "La valeur entière égale au chiffre deux", "isCorrect": False}
                    ],
                    "correction": "Calculer l'image d'un nombre consiste à remplacer x par ce nombre dans l'expression de la fonction. Ici : f(3) = 4 * 3 - 1 = 12 - 1 = 11. L'image de 3 est donc 11."
                },
                {
                    "questionNumber": 38,
                    "question": "Le point A(2 ; 5) appartient-il à la droite d'équation y = 2x + 1 ?",
                    "answerOptions": [
                        {"text": "Oui, car l'égalité est vérifiée avec ces coordonnées", "isCorrect": True},
                        {"text": "Non, car le calcul ne correspond pas à l'ordonnée", "isCorrect": False},
                        {"text": "On ne peut pas savoir sans tracer le repère complet", "isCorrect": False},
                        {"text": "Seulement si la variable x est un nombre positif", "isCorrect": False}
                    ],
                    "correction": "Pour tester l'appartenance, on remplace x par 2 dans l'équation : y = 2 * 2 + 1 = 4 + 1 = 5. L'ordonnée trouvée (5) correspond bien à celle du point A. Le point appartient donc à la droite."
                },
                {
                    "questionNumber": 39,
                    "question": "Factoriser l'expression suivante : x² + 3x.",
                    "answerOptions": [
                        {"text": "L'expression factorisée égale à x(x + 3)", "isCorrect": True},
                        {"text": "L'expression factorisée égale à 3(x + 1)", "isCorrect": False},
                        {"text": "L'expression factorisée égale à x²(1 + 3)", "isCorrect": False},
                        {"text": "L'expression réduite égale à 2x + 3", "isCorrect": False}
                    ],
                    "correction": "Factoriser consiste à transformer une somme en produit. Ici, le facteur commun aux deux termes (x² et 3x) est x. On extrait x : x² + 3x = x * x + x * 3 = x(x + 3). Si on redéveloppe, on retrouve bien l'expression initiale."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la définition d'une pente de route à 10% ?",
                    "answerOptions": [
                        {"text": "Elle monte de 10m pour 100m horizontaux parcourus", "isCorrect": True},
                        {"text": "Elle fait un angle précis égal à dix degrés", "isCorrect": False},
                        {"text": "Elle mesure exactement dix kilomètres de long", "isCorrect": False},
                        {"text": "Elle est réservée aux véhicules de dix tonnes", "isCorrect": False}
                    ],
                    "correction": "En topographie, une pente en pourcentage est le rapport entre le dénivelé (hauteur) et la distance horizontale parcourue. 10 % signifie que pour 100 m de déplacement à plat, vous vous êtes élevé de 10 m."
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
                    "question": "Quelle est la somme des angles intérieurs d'un triangle ?",
                    "answerOptions": [
                        {"text": "Un total de cent-quatre-vingts degrés", "isCorrect": True},
                        {"text": "Un total de quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Un total de trois-cent-soixante degrés", "isCorrect": False},
                        {"text": "Un total de cent degrés exactement", "isCorrect": False}
                    ],
                    "correction": "C'est une propriété universelle de la géométrie euclidienne : peu importe la forme du triangle (quelconque, rectangle, isocèle), l'addition de ses trois angles donne toujours précisément 180°."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle formule permet de calculer le périmètre d'un cercle ?",
                    "answerOptions": [
                        {"text": "Le produit 2 fois Pi fois le rayon R", "isCorrect": True},
                        {"text": "Le produit Pi fois le carré du rayon R", "isCorrect": False},
                        {"text": "Le produit de la longueur du côté par 4", "isCorrect": False},
                        {"text": "Le quotient du diamètre divisé par Pi", "isCorrect": False}
                    ],
                    "correction": "Le périmètre (ou circonférence) d'un cercle se calcule avec P = 2 x π x R. Puisque deux fois le rayon égale le diamètre (D), on peut aussi utiliser la formule plus directe : P = π x D."
                },
                {
                    "questionNumber": 43,
                    "question": "Dans quel type de triangle le théorème de Pythagore s'applique-t-il ?",
                    "answerOptions": [
                        {"text": "Uniquement au sein d'un triangle rectangle", "isCorrect": True},
                        {"text": "Au sein d'un triangle isocèle possédant deux côtés égaux", "isCorrect": False},
                        {"text": "Au sein d'un triangle équilatéral aux trois côtés égaux", "isCorrect": False},
                        {"text": "Au sein d'un triangle quelconque sans angle particulier", "isCorrect": False}
                    ],
                    "correction": "Pythagore ne fonctionne que dans les triangles possédant un angle droit (90°). Il établit que le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés : BC² = AB² + AC²."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la formule de l'aire d'un disque de rayon R ?",
                    "answerOptions": [
                        {"text": "Le produit Pi fois le carré du rayon R²", "isCorrect": True},
                        {"text": "Le produit 2 fois Pi fois le rayon R", "isCorrect": False},
                        {"text": "Le produit simple du rayon par lui-même", "isCorrect": False},
                        {"text": "Le produit 4/3 fois Pi fois le rayon au cube", "isCorrect": False}
                    ],
                    "correction": "Pour calculer la surface occupée par un disque, on utilise Aire = π x R². Attention à ne pas confondre avec la formule du périmètre (2πR). Le résultat s'exprime en unités de surface (cm², m²)."
                },
                {
                    "questionNumber": 45,
                    "question": "Dans un triangle rectangle, le sinus d'un angle est égal à :",
                    "answerOptions": [
                        {"text": "Le quotient Côté opposé divisé par Hypoténuse", "isCorrect": True},
                        {"text": "Le quotient Côté adjacent divisé par Hypoténuse", "isCorrect": False},
                        {"text": "Le quotient Côté opposé divisé par Côté adjacent", "isCorrect": False},
                        {"text": "Le quotient Hypoténuse divisé par Côté opposé", "isCorrect": False}
                    ],
                    "correction": "La trigonométrie utilise les rapports de longueurs. Le sinus d'un angle aigu est le rapport entre la longueur du côté en face de l'angle et le plus long côté. Moyen mnémotechnique : SOH (Sinus = Opposé / Hypoténuse)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la définition géométrique de l'hypoténuse ?",
                    "answerOptions": [
                        {"text": "Le côté le plus long situé face à l'angle droit", "isCorrect": True},
                        {"text": "La hauteur principale issue d'un sommet", "isCorrect": False},
                        {"text": "L'angle de mesure égale à quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Le côté situé immédiatement à côté de l'angle droit", "isCorrect": False}
                    ],
                    "correction": "Dans un triangle rectangle, l'hypoténuse est le côté opposé à l'angle droit. C'est mathématiquement le côté le plus long du triangle. Elle est utilisée comme base dans les calculs de Pythagore et de trigonométrie."
                },
                {
                    "questionNumber": 47,
                    "question": "En termes de volume, un litre est équivalent à :",
                    "answerOptions": [
                        {"text": "Une capacité égale à un décimètre cube", "isCorrect": True},
                        {"text": "Une capacité égale à un mètre cube complet", "isCorrect": False},
                        {"text": "Une capacité égale à un centimètre cube", "isCorrect": False},
                        {"text": "Une capacité égale à cent millilitres cubes", "isCorrect": False}
                    ],
                    "correction": "C'est une conversion de base indispensable en sciences et en cuisine : 1 L = 1 dm³. Pour rappel, 1 m³ contient 1000 litres et 1 cm³ correspond à 1 millilitre (1 mL)."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment calcule-t-on le volume d'un cylindre de révolution ?",
                    "answerOptions": [
                        {"text": "Le produit de l'aire de la base par la hauteur h", "isCorrect": True},
                        {"text": "Le produit du périmètre de la base par la hauteur h", "isCorrect": False},
                        {"text": "Le produit simple du rayon par la hauteur h", "isCorrect": False},
                        {"text": "Le produit Pi fois le cube du rayon R³", "isCorrect": False}
                    ],
                    "correction": "Le volume d'un cylindre est V = Aire de la base x hauteur. Puisque la base est un disque de rayon R, la formule complète est V = π x R² x h. Le résultat s'exprime en unités de volume (cm³, m³, etc.)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le périmètre d'un carré de 5 cm de côté ?",
                    "answerOptions": [
                        {"text": "Une longueur totale égale à vingt centimètres", "isCorrect": True},
                        {"text": "Une surface totale égale à vingt-cinq centimètres", "isCorrect": False},
                        {"text": "Une longueur totale égale à dix centimètres", "isCorrect": False},
                        {"text": "Une longueur totale égale à cinquante centimètres", "isCorrect": False}
                    ],
                    "correction": "Le périmètre d'un polygone est la somme des longueurs de ses côtés. Pour un carré, les 4 côtés sont égaux. P = 4 x côté = 4 x 5 = 20 cm."
                },
                {
                    "questionNumber": 50,
                    "question": "Que vaut l'aire d'un triangle de base 10 cm et de hauteur 4 cm ?",
                    "answerOptions": [
                        {"text": "Une surface égale à vingt centimètres carrés", "isCorrect": True},
                        {"text": "Une surface égale à quarante centimètres carrés", "isCorrect": False},
                        {"text": "Une surface égale à quatorze centimètres carrés", "isCorrect": False},
                        {"text": "Une surface égale à quatre-vingts centimètres carrés", "isCorrect": False}
                    ],
                    "correction": "La formule de l'aire d'un triangle est : (Base x Hauteur) / 2. Ici : (10 x 4) / 2 = 40 / 2 = 20 cm². On divise par deux car un triangle est la moitié d'un rectangle de même base et même hauteur."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la mesure précise d'un angle droit ?",
                    "answerOptions": [
                        {"text": "Une mesure égale à quatre-vingt-dix degrés", "isCorrect": True},
                        {"text": "Une mesure égale à cent-quatre-vingts degrés", "isCorrect": False},
                        {"text": "Une mesure égale à quarante-cinq degrés", "isCorrect": False},
                        {"text": "Une mesure égale à trois-cent-soixante degrés", "isCorrect": False}
                    ],
                    "correction": "Un angle droit est formé par l'intersection de deux droites perpendiculaires. Il correspond au quart d'un tour complet. C'est l'angle que l'on retrouve dans les coins d'un carré ou d'un rectangle."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment appelle-t-on un triangle ayant au moins deux côtés égaux ?",
                    "answerOptions": [
                        {"text": "Un triangle isocèle possédant un axe de symétrie", "isCorrect": True},
                        {"text": "Un triangle équilatéral aux trois côtés identiques", "isCorrect": False},
                        {"text": "Un triangle rectangle possédant un angle droit", "isCorrect": False},
                        {"text": "Un triangle scalène dont tous les côtés sont différents", "isCorrect": False}
                    ],
                    "correction": "Un triangle isocèle a deux côtés de même longueur. Cette propriété entraîne que les deux angles à la base sont également de même mesure. S'il a trois côtés égaux, il devient alors équilatéral."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la valeur approchée courante du nombre Pi ?",
                    "answerOptions": [
                        {"text": "La valeur décimale égale à trois virgule quatorze", "isCorrect": True},
                        {"text": "La valeur décimale égale à deux virgule quatorze", "isCorrect": False},
                        {"text": "La valeur décimale égale à trois virgule quarante et un", "isCorrect": False},
                        {"text": "La valeur entière simple égale au chiffre trois", "isCorrect": False}
                    ],
                    "correction": "π (Pi) est un nombre irrationnel, ses décimales sont infinies. On utilise généralement 3,14 pour les calculs simples au lycée. Il représente le rapport constant entre la circonférence d'un cercle et son diamètre."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la mesure d'un angle plat ?",
                    "answerOptions": [
                        {"text": "Une mesure égale à cent-quatre-vingts degrés", "isCorrect": True},
                        {"text": "Une mesure égale à quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Une mesure égale à la valeur de zéro degré", "isCorrect": False},
                        {"text": "Une mesure égale à deux-cent-soixante-dix degrés", "isCorrect": False}
                    ],
                    "correction": "Un angle plat correspond à un demi-tour. Les deux côtés de l'angle sont alignés et forment une droite. C'est la somme de deux angles droits consécutifs."
                },
                {
                    "questionNumber": 55,
                    "question": "Que signifie le terme géométrique 'perpendiculaire' ?",
                    "answerOptions": [
                        {"text": "Qui se croise en formant un angle droit", "isCorrect": True},
                        {"text": "Qui s'étend à l'infini sans jamais se croiser", "isCorrect": False},
                        {"text": "Qui présente une inclinaison très prononcée", "isCorrect": False},
                        {"text": "Qui possède exactement la même longueur", "isCorrect": False}
                    ],
                    "correction": "Deux droites sont perpendiculaires si elles se coupent en formant quatre angles droits. En géométrie plane, le symbole utilisé pour noter cette relation est ⊥. À ne pas confondre avec 'parallèle' (symbolisé par //)."
                },
                {
                    "questionNumber": 56,
                    "question": "Un cube de 2m de côté possède un volume de :",
                    "answerOptions": [
                        {"text": "Une capacité égale à huit mètres cubes", "isCorrect": True},
                        {"text": "Une capacité égale à quatre mètres cubes", "isCorrect": False},
                        {"text": "Une capacité égale à six mètres cubes", "isCorrect": False},
                        {"text": "Une capacité égale à douze mètres cubes", "isCorrect": False}
                    ],
                    "correction": "La formule du volume d'un cube est Côté x Côté x Côté (ou C³). Ici : 2 * 2 * 2 = 8 m³. Attention, doubler le côté d'un cube multiplie son volume par 8 (2 au cube), pas par 2."
                },
                {
                    "questionNumber": 57,
                    "question": "Dans le théorème de Thalès, les deux droites principales doivent être :",
                    "answerOptions": [
                        {"text": "Strictement parallèles au sein de la figure", "isCorrect": True},
                        {"text": "Strictement perpendiculaires entre elles", "isCorrect": False},
                        {"text": "Sécantes exactement en leur milieu respectif", "isCorrect": False},
                        {"text": "De la même couleur pour être identifiées", "isCorrect": False}
                    ],
                    "correction": "Le théorème de Thalès permet de calculer des longueurs dans des triangles imbriqués ou en configuration 'papillon'. La condition indispensable est d'avoir deux droites parallèles coupées par deux sécantes. Il repose sur la proportionnalité des segments."
                },
                {
                    "questionNumber": 58,
                    "question": "En trigonométrie, le cosinus d'un angle est le rapport entre :",
                    "answerOptions": [
                        {"text": "Côté adjacent divisé par l'Hypoténuse", "isCorrect": True},
                        {"text": "Côté opposé divisé par l'Hypoténuse", "isCorrect": False},
                        {"text": "Côté opposé divisé par le Côté adjacent", "isCorrect": False},
                        {"text": "Hypoténuse divisée par le Côté opposé", "isCorrect": False}
                    ],
                    "correction": "Le cosinus mesure le rapport entre le côté touchant l'angle (mais n'étant pas l'hypoténuse) et le plus long côté. Moyen mnémotechnique : CAH (Cosinus = Adjacent / Hypoténuse)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle est l'aire d'un carré possédant un côté de 4m ?",
                    "answerOptions": [
                        {"text": "Une surface égale à seize mètres carrés", "isCorrect": True},
                        {"text": "Une surface égale à huit mètres carrés", "isCorrect": False},
                        {"text": "Une surface égale à douze mètres carrés", "isCorrect": False},
                        {"text": "Une surface égale à quatre mètres carrés", "isCorrect": False}
                    ],
                    "correction": "L'aire d'un carré se calcule en multipliant la longueur du côté par elle-même. Aire = Côté x Côté. Ici : 4m x 4m = 16 m². Ne pas confondre avec le périmètre qui serait ici de 16m également (4+4+4+4)."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment appelle-t-on un polygone possédant exactement 5 côtés ?",
                    "answerOptions": [
                        {"text": "Un pentagone régulier ou irrégulier", "isCorrect": True},
                        {"text": "Un hexagone présent dans les ruches", "isCorrect": False},
                        {"text": "Un octogone utilisé pour certains sports", "isCorrect": False},
                        {"text": "Un losange aux quatre côtés égaux", "isCorrect": False}
                    ],
                    "correction": "Le nom des polygones vient souvent de racines grecques. 'Penta' signifie 5. Un pentagone régulier a ses 5 côtés de même longueur et ses 5 angles de même mesure (108° chacun)."
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
                        {"text": "En ajoutant toujours le même nombre nommé la raison", "isCorrect": True},
                        {"text": "En multipliant toujours par le même nombre fixe", "isCorrect": False},
                        {"text": "En divisant par deux le terme précédent de la suite", "isCorrect": False},
                        {"text": "En prenant le carré du terme précédent immédiatement", "isCorrect": False}
                    ],
                    "correction": "Une suite est arithmétique si la différence entre deux termes consécutifs est constante. Ce nombre constant 'r' est appelé la raison. Formule : u(n+1) = u(n) + r. C'est le modèle mathématique de l'évolution à croissance constante."
                },
                {
                    "questionNumber": 62,
                    "question": "Que signifie précisément le sigle fiscal TVA ?",
                    "answerOptions": [
                        {"text": "La Taxe sur la Valeur Ajoutée perçue par l'État", "isCorrect": True},
                        {"text": "Le Tarif de Vente Annuel fixé par les commerçants", "isCorrect": False},
                        {"text": "Le Total des Valeurs d'Achat incluant les remises", "isCorrect": False},
                        {"text": "La Taxe de Vente Automatique sur les produits", "isCorrect": False}
                    ],
                    "correction": "La TVA est un impôt indirect sur la consommation. Elle est collectée par les entreprises pour le compte de l'État. Le consommateur final paie le prix TTC (Toutes Taxes Comprises), tandis que les entreprises raisonnent souvent en HT (Hors Taxes)."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment calcule-t-on un prix TTC à partir du prix HT et du taux ?",
                    "answerOptions": [
                        {"text": "Le prix HT multiplié par le facteur (1 + taux de TVA)", "isCorrect": True},
                        {"text": "Le prix HT divisé par la valeur du taux de TVA", "isCorrect": False},
                        {"text": "Le prix HT additionné simplement au taux de TVA", "isCorrect": False},
                        {"text": "Le prix HT auquel on soustrait une remise éventuelle", "isCorrect": False}
                    ],
                    "correction": "Pour un taux de TVA à 20 %, le coefficient multiplicateur est (1 + 20/100) = 1,20. Le prix TTC est donc égal à HT x 1,20. Cette méthode par multiplication est plus rapide que de calculer la taxe puis de l'ajouter."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la raison r de la suite numérique : 2 ; 5 ; 8 ; 11... ?",
                    "answerOptions": [
                        {"text": "La raison est égale au chiffre trois", "isCorrect": True},
                        {"text": "La raison est égale au chiffre deux", "isCorrect": False},
                        {"text": "La raison est égale au chiffre cinq", "isCorrect": False},
                        {"text": "La raison est égale au chiffre quatre", "isCorrect": False}
                    ],
                    "correction": "Pour trouver la raison, on calcule la différence entre deux termes qui se suivent : 5 - 2 = 3 ; 8 - 5 = 3 ; 11 - 8 = 3. Puisque la différence est constante, la suite est arithmétique de raison r = 3."
                },
                {
                    "questionNumber": 65,
                    "question": "Dans une suite géométrique, comment passe-t-on d'un terme au suivant ?",
                    "answerOptions": [
                        {"text": "En multipliant par le même nombre nommé la raison q", "isCorrect": True},
                        {"text": "En ajoutant une constante identique à chaque étape", "isCorrect": False},
                        {"text": "En soustrayant la valeur de la raison à chaque fois", "isCorrect": False},
                        {"text": "Le passage est totalement aléatoire sans règle fixe", "isCorrect": False}
                    ],
                    "correction": "Une suite est géométrique si le rapport entre deux termes consécutifs est constant. On multiplie par 'q' pour avancer. Formule : u(n+1) = u(n) x q. C'est le modèle des évolutions en pourcentage (intérêts, populations)."
                },
                {
                    "questionNumber": 66,
                    "question": "Un placement à intérêts simples de 1000 € à 5% par an rapporte combien ?",
                    "answerOptions": [
                        {"text": "Cinquante euros d'intérêts pour la première année", "isCorrect": True},
                        {"text": "Cinq euros d'intérêts pour la première année", "isCorrect": False},
                        {"text": "Cent euros d'intérêts pour la première année", "isCorrect": False},
                        {"text": "Cinq-cents euros d'intérêts pour la première année", "isCorrect": False}
                    ],
                    "correction": "Dans un placement à intérêts simples, l'intérêt est calculé uniquement sur le capital de départ. Intérêt = Capital x Taux x Durée. Ici : 1000 x (5/100) x 1 = 1000 x 0,05 = 50 €."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la raison q de la suite géométrique : 1 ; 2 ; 4 ; 8... ?",
                    "answerOptions": [
                        {"text": "La raison est égale au chiffre deux", "isCorrect": True},
                        {"text": "La raison est égale au chiffre un", "isCorrect": False},
                        {"text": "La raison est égale au chiffre quatre", "isCorrect": False},
                        {"text": "La raison est égale au chiffre trois", "isCorrect": False}
                    ],
                    "correction": "On observe qu'on multiplie par 2 à chaque étape pour trouver le nombre suivant (1x2=2, 2x2=4, 4x2=8). Il s'agit d'une suite géométrique de raison q = 2. C'est une croissance exponentielle (doublement)."
                },
                {
                    "questionNumber": 68,
                    "question": "Que signifie concrètement un placement à intérêts 'composés' ?",
                    "answerOptions": [
                        {"text": "Les intérêts s'ajoutent au capital pour en produire de nouveaux", "isCorrect": True},
                        {"text": "L'intérêt reste strictement identique chaque année du contrat", "isCorrect": False},
                        {"text": "On ne peut pas retirer son argent avant le terme prévu", "isCorrect": False},
                        {"text": "Le taux de rémunération change chaque mois selon le marché", "isCorrect": False}
                    ],
                    "correction": "À la fin de chaque période, les intérêts produits sont ajoutés au capital initial pour constituer le nouveau capital. L'année suivante, les intérêts seront donc calculés sur une base plus élevée. C'est l'effet 'capitalisation' utilisé pour les livrets d'épargne longue."
                },
                {
                    "questionNumber": 69,
                    "question": "Un article à 80 € bénéficie d'une remise de 25%. Quel est le nouveau prix ?",
                    "answerOptions": [
                        {"text": "Le prix final après remise est égal à soixante euros", "isCorrect": True},
                        {"text": "Le prix final après remise est égal à cinquante-cinq euros", "isCorrect": False},
                        {"text": "Le montant de la remise est égal à vingt euros", "isCorrect": False},
                        {"text": "Le prix final après remise est égal à soixante-quinze euros", "isCorrect": False}
                    ],
                    "correction": "Calcul de la remise : 80 x 0,25 = 20 €. Prix final = 80 - 20 = 60 €. On peut aussi utiliser le coefficient multiplicateur : 80 x (1 - 0,25) = 80 x 0,75 = 60 €."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment calcule-t-on mathématiquement le montant de la TVA ?",
                    "answerOptions": [
                        {"text": "Le produit du prix Hors Taxes par le taux de TVA", "isCorrect": True},
                        {"text": "La somme des prix Hors Taxes et Toutes Taxes Comprises", "isCorrect": False},
                        {"text": "Le quotient du prix Hors Taxes par le prix Toutes Taxes", "isCorrect": False},
                        {"text": "La soustraction du prix Hors Taxes au prix Toute Taxes", "isCorrect": True}
                    ],
                    "correction": "Il y a deux façons : soit multiplier le HT par le taux (ex: HT x 0,20), soit faire la différence entre ce que paie le client et ce que garde l'entreprise (TTC - HT). Les deux méthodes donnent le même résultat monétaire."
                },
                {
                    "questionNumber": 71,
                    "question": "Si le TTC est de 120 € et le HT de 100 €, quel est le montant de la TVA ?",
                    "answerOptions": [
                        {"text": "Le montant de la taxe est de vingt euros", "isCorrect": True},
                        {"text": "Le montant de la taxe est de cent-vingt euros", "isCorrect": False},
                        {"text": "Le montant de la taxe est de vingt pour cent", "isCorrect": False},
                        {"text": "Le montant de la taxe est de un virgule vingt euros", "isCorrect": False}
                    ],
                    "correction": "Le montant de la taxe s'exprime en monnaie (euros) et non en pourcentage (le taux). On calcule simplement la différence : TTC - HT = 120 - 100 = 20 €."
                },
                {
                    "questionNumber": 72,
                    "question": "Dans la formule u(n) = u(0) + n*r, on reconnaît une suite :",
                    "answerOptions": [
                        {"text": "Une suite de type arithmétique à croissance constante", "isCorrect": True},
                        {"text": "Une suite de type géométrique à croissance exponentielle", "isCorrect": False},
                        {"text": "Une suite de type décroissante sur l'ensemble étudié", "isCorrect": False},
                        {"text": "Une suite de type financière avec intérêts composés", "isCorrect": False}
                    ],
                    "correction": "C'est la formule explicite d'une suite arithmétique. Elle permet de calculer directement n'importe quel terme de rang 'n' sans avoir besoin de connaître tous les termes précédents, simplement avec le premier terme u(0) et la raison 'r'."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le coefficient multiplicateur pour une baisse de 30% ?",
                    "answerOptions": [
                        {"text": "Le coefficient multiplicateur égal à 0,70", "isCorrect": True},
                        {"text": "Le coefficient multiplicateur égal à 1,30", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur égal à 0,30", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur égal au chiffre trois", "isCorrect": False}
                    ],
                    "correction": "Pour une diminution, le coefficient CM est (1 - t/100). Ici : 1 - 30/100 = 1 - 0,30 = 0,70. Multiplier une valeur par 0,70 revient donc à lui appliquer une réduction de 30 %."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment s'appelle l'indice du premier terme d'une suite ?",
                    "answerOptions": [
                        {"text": "La notation u0 ou u1 selon le choix initial", "isCorrect": True},
                        {"text": "La raison définissant l'évolution des termes", "isCorrect": False},
                        {"text": "L'indice de référence pour le calcul du total", "isCorrect": False},
                        {"text": "Le total global de l'ensemble des valeurs", "isCorrect": False}
                    ],
                    "correction": "L'indice (en indice sous la lettre u) indique le rang du terme dans la liste. Si on commence à u0, le 10ème terme sera u9. Si on commence à u1, le 10ème terme sera u10. C'est un repère de position."
                },
                {
                    "questionNumber": 75,
                    "question": "Une suite géométrique dont la raison q est entre 0 et 1 est :",
                    "answerOptions": [
                        {"text": "Strictement décroissante si le premier terme est positif", "isCorrect": True},
                        {"text": "Strictement croissante sur son ensemble de définition", "isCorrect": False},
                        {"text": "Constante quelle que soit la valeur de la variable n", "isCorrect": False},
                        {"text": "Strictement négative pour l'ensemble de ses termes", "isCorrect": False}
                    ],
                    "correction": "Multiplier un nombre positif par un nombre compris entre 0 et 1 (ex: 0,5) réduit systématiquement sa valeur. À chaque étape, le terme devient plus petit, la suite 'tend' donc vers zéro en diminuant."
                },
                {
                    "questionNumber": 76,
                    "question": "Que signifie précisément le 'taux annuel' d'un prêt ?",
                    "answerOptions": [
                        {"text": "Le coût du crédit annuel en pourcentage du capital", "isCorrect": True},
                        {"text": "Le montant total d'argent qu'il reste à rembourser", "isCorrect": False},
                        {"text": "La durée totale du prêt exprimée en nombre d'années", "isCorrect": False},
                        {"text": "Le prix fixe de l'assurance obligatoire du contrat", "isCorrect": False}
                    ],
                    "correction": "C'est l'indicateur du prix de l'argent emprunté. Il permet de calculer les intérêts que l'emprunteur doit payer à la banque en échange du service de prêt du capital."
                },
                {
                    "questionNumber": 77,
                    "question": "Trouvez le 4ème terme (u3) d'une suite arithmétique avec u0=10 et r=5.",
                    "answerOptions": [
                        {"text": "La valeur entière égale à vingt-cinq", "isCorrect": True},
                        {"text": "La valeur entière égale au nombre quinze", "isCorrect": False},
                        {"text": "La valeur entière égale au nombre trente", "isCorrect": False},
                        {"text": "La valeur entière égale au nombre vingt", "isCorrect": False}
                    ],
                    "correction": "On liste les termes : u0 = 10 ; u1 = 10+5 = 15 ; u2 = 15+5 = 20 ; u3 = 20+5 = 25. Le 4ème terme (rang 3 si on commence à 0) est donc bien 25."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le prix HT si le TTC est de 60 € avec une TVA à 20% ?",
                    "answerOptions": [
                        {"text": "Le prix hors taxes égal à cinquante euros", "isCorrect": True},
                        {"text": "Le prix hors taxes égal à quarante-huit euros", "isCorrect": False},
                        {"text": "Le prix hors taxes égal à quarante euros", "isCorrect": False},
                        {"text": "Le prix hors taxes égal à cinquante-cinq euros", "isCorrect": False}
                    ],
                    "correction": "Pour retrouver le HT, on divise le TTC par le coefficient multiplicateur. HT = 60 / 1,20 = 50 €. Pour vérifier : 50 x 1,20 donne bien 60."
                },
                {
                    "questionNumber": 79,
                    "question": "Si la raison q d'une suite géométrique est égale à 1, la suite est :",
                    "answerOptions": [
                        {"text": "Constante car les termes restent identiques", "isCorrect": True},
                        {"text": "Nulle car les termes s'annulent au fur et à mesure", "isCorrect": False},
                        {"text": "Infinie avec des valeurs augmentant sans cesse", "isCorrect": False},
                        {"text": "Arithmétique avec une raison égale à zéro", "isCorrect": True}
                    ],
                    "correction": "Multiplier par 1 ne change pas la valeur du nombre. u(n+1) = u(n) x 1 = u(n). Tous les termes sont donc égaux au premier terme. Notez qu'une suite constante est à la fois géométrique (raison 1) et arithmétique (raison 0)."
                },
                {
                    "questionNumber": 80,
                    "question": "Qu'est-ce qu'une remise au sens commercial du terme ?",
                    "answerOptions": [
                        {"text": "Une réduction accordée selon les quantités ou l'habitude", "isCorrect": True},
                        {"text": "Une réduction accordée pour les produits endommagés", "isCorrect": False},
                        {"text": "Une subvention directe versée par l'État aux entreprises", "isCorrect": False},
                        {"text": "Une annulation totale de la facture pour le client", "isCorrect": False}
                    ],
                    "correction": "La remise est un geste commercial calculé sur le prix de vente brut. On distingue le rabais (pour défaut de qualité), la remise (fidélité ou volume) et la ristourne (calculée sur une période, ex: fin d'année)."
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
                    "question": "En algorithmique, à quoi sert précisément une variable ?",
                    "answerOptions": [
                        {"text": "À stocker une information en mémoire sous un nom", "isCorrect": True},
                        {"text": "À décorer l'interface graphique du programme", "isCorrect": False},
                        {"text": "À éteindre automatiquement le système d'exploitation", "isCorrect": False},
                        {"text": "À mesurer physiquement la vitesse de calcul du processeur", "isCorrect": False}
                    ],
                    "correction": "Une variable peut être vue comme une boîte portant une étiquette (le nom de la variable) et contenant une donnée (le contenu). Ce contenu peut changer au cours de l'exécution du programme, d'où le nom de 'variable'."
                },
                {
                    "questionNumber": 82,
                    "question": "Que fait l'instruction standard 'print' en langage Python ?",
                    "answerOptions": [
                        {"text": "Elle affiche un résultat ou un message à l'écran", "isCorrect": True},
                        {"text": "Elle imprime directement le texte sur une feuille de papier", "isCorrect": False},
                        {"text": "Elle efface l'intégralité de la mémoire vive utilisée", "isCorrect": False},
                        {"text": "Elle demande une valeur numérique à l'utilisateur", "isCorrect": False}
                    ],
                    "correction": "L'instruction print() est la commande de sortie de base. Elle permet au programmeur de communiquer avec l'utilisateur en affichant des valeurs, des variables ou des messages texte dans la console de l'ordinateur."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel symbole utilise-t-on pour multiplier en programmation ?",
                    "answerOptions": [
                        {"text": "L'astérisque situé sur la touche étoile", "isCorrect": True},
                        {"text": "La lettre x minuscule utilisée en algèbre classique", "isCorrect": False},
                        {"text": "Le signe de la croix utilisé en mathématiques", "isCorrect": False},
                        {"text": "Le point médian situé au centre de la ligne", "isCorrect": False}
                    ],
                    "correction": "En informatique, pour éviter toute confusion avec la lettre 'x' qui sert souvent de nom de variable, on utilise l'astérisque (*) pour la multiplication. De même, on utilise le slash (/) pour la division."
                },
                {
                    "questionNumber": 84,
                    "question": "Qu'est-ce qu'une boucle de type 'for' ?",
                    "answerOptions": [
                        {"text": "Une structure qui répète des instructions un nombre de fois défini", "isCorrect": True},
                        {"text": "Une erreur fatale empêchant le lancement du programme", "isCorrect": False},
                        {"text": "Une question complexe posée directement à l'utilisateur", "isCorrect": False},
                        {"text": "Une condition logique de type SI... ALORS uniquement", "isCorrect": False}
                    ],
                    "correction": "La boucle 'for' est utilisée pour l'itération. On sait à l'avance combien de fois l'action va être répétée (ex: pour chaque élément d'une liste, ou de 1 à 100). Elle permet d'automatiser des calculs sur de grandes séries de données."
                },
                {
                    "questionNumber": 85,
                    "question": "En Python, que signifie l'opérateur de comparaison '==' ?",
                    "answerOptions": [
                        {"text": "Est égal à pour tester une égalité logique", "isCorrect": True},
                        {"text": "Prend la valeur de pour une affectation de variable", "isCorrect": False},
                        {"text": "Est différent de dans une structure conditionnelle", "isCorrect": False},
                        {"text": "Est strictement plus grand que la valeur suivante", "isCorrect": False}
                    ],
                    "correction": "Il ne faut pas confondre le simple '=' qui sert à mettre une valeur dans une boîte (affectation) et le double '==' qui sert à poser une question (est-ce que ceci est égal à cela ?). Le résultat d'un test '==' est un booléen (Vrai ou Faux)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est la valeur du calcul 2 ** 3 en Python ?",
                    "answerOptions": [
                        {"text": "La valeur entière égale au chiffre huit", "isCorrect": True},
                        {"text": "La valeur entière égale au chiffre six", "isCorrect": False},
                        {"text": "La valeur entière égale au chiffre cinq", "isCorrect": False},
                        {"text": "La valeur entière égale au chiffre neuf", "isCorrect": False}
                    ],
                    "correction": "L'opérateur double étoile (**) est l'opérateur d'exposant (puissance) en Python. 2 ** 3 signifie 2 à la puissance 3, soit 2 x 2 x 2 = 8. À ne pas confondre avec 2 * 3 (multiplication)."
                },
                {
                    "questionNumber": 87,
                    "question": "Une structure conditionnelle commence souvent par le mot clé :",
                    "answerOptions": [
                        {"text": "L'instruction if qui signifie 'si' en français", "isCorrect": True},
                        {"text": "L'instruction while qui signifie 'pendant que'", "isCorrect": False},
                        {"text": "L'instruction stop qui marque la fin du code", "isCorrect": False},
                        {"text": "L'instruction start qui initialise l'ensemble", "isCorrect": False}
                    ],
                    "correction": "L'instruction 'if' permet au programme de prendre des décisions. Le code situé à l'intérieur du bloc 'if' ne sera exécuté que si la condition posée est vraie. C'est la base de toute l'intelligence algorithmique."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'un type 'float' en informatique ?",
                    "answerOptions": [
                        {"text": "Un nombre à virgule flottante ou nombre décimal", "isCorrect": True},
                        {"text": "Une chaîne de caractères ou texte simple", "isCorrect": False},
                        {"text": "Un nombre entier sans aucune partie décimale", "isCorrect": False},
                        {"text": "Une liste organisée de données variées", "isCorrect": False}
                    ],
                    "correction": "Le type 'float' désigne les nombres réels (décimaux). Attention, en informatique on utilise le point (.) et non la virgule (,) pour séparer la partie entière de la partie décimale. Exemple : 3.14."
                },
                {
                    "questionNumber": 89,
                    "question": "Que signifie concrètement incrémenter une variable ?",
                    "answerOptions": [
                        {"text": "Ajouter la valeur un à sa valeur actuelle", "isCorrect": True},
                        {"text": "Multiplier par deux sa valeur de départ", "isCorrect": False},
                        {"text": "Effacer totalement le contenu de la variable", "isCorrect": False},
                        {"text": "Diviser par deux la valeur stockée en mémoire", "isCorrect": False}
                    ],
                    "correction": "Incrémenter signifie augmenter d'un pas (généralement 1). En Python, on écrit 'x = x + 1' ou 'x += 1'. On l'utilise très souvent pour compter le nombre de tours d'une boucle."
                },
                {
                    "questionNumber": 90,
                    "question": "Valeur de x après ces étapes : x=5 ; x=x+2 ; x=x*10 ?",
                    "answerOptions": [
                        {"text": "La valeur finale est égale au nombre soixante-dix", "isCorrect": True},
                        {"text": "La valeur finale est égale au nombre vingt-cinq", "isCorrect": False},
                        {"text": "La valeur finale est égale au nombre cinquante-deux", "isCorrect": False},
                        {"text": "La valeur finale est égale au nombre dix-sept", "isCorrect": False}
                    ],
                    "correction": "Détail du calcul : 1) x part de 5. 2) x devient 5+2 = 7. 3) x devient 7*10 = 70. L'ordinateur écrase l'ancienne valeur par la nouvelle à chaque affectation."
                },
                {
                    "questionNumber": 91,
                    "question": "Comment appelle-t-on une erreur de code dans un programme ?",
                    "answerOptions": [
                        {"text": "Un bug qui perturbe le fonctionnement normal", "isCorrect": True},
                        {"text": "Un virus qui détruit les fichiers du système", "isCorrect": False},
                        {"text": "Un dossier informatique pour ranger les textes", "isCorrect": False},
                        {"text": "Un écran noir indiquant une absence de signal", "isCorrect": False}
                    ],
                    "correction": "Le terme 'bug' vient de l'anglais (punaise/insecte). Historiquement, un papillon de nuit s'était coincé dans les circuits d'un des premiers ordinateurs géants, provoquant une panne."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le résultat du carré du nombre 0,5 ?",
                    "answerOptions": [
                        {"text": "Le nombre décimal égal à zéro virgule vingt-cinq", "isCorrect": True},
                        {"text": "Le nombre entier égal à la valeur de un", "isCorrect": False},
                        {"text": "Le nombre décimal égal à la valeur de zéro virgule un", "isCorrect": False},
                        {"text": "Le nombre décimal égal à la valeur de deux virgule cinq", "isCorrect": False}
                    ],
                    "correction": "0,5 x 0,5 = 0,25. Multiplier un nombre entre 0 et 1 par lui-même donne un résultat plus petit que le nombre de départ. C'est une propriété importante à retenir."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel type de variable ne peut prendre que True ou False ?",
                    "answerOptions": [
                        {"text": "Un booléen représentant une valeur de vérité", "isCorrect": True},
                        {"text": "Un flottant pour les calculs de précision", "isCorrect": False},
                        {"text": "Un entier pour le comptage des éléments", "isCorrect": False},
                        {"text": "Une liste regroupant plusieurs variables", "isCorrect": False}
                    ],
                    "correction": "Le type 'bool' (booléen) n'accepte que deux états : True (Vrai) ou False (Faux). On s'en sert pour mémoriser si une condition a été remplie ou non dans un algorithme."
                },
                {
                    "questionNumber": 94,
                    "question": "Que fait l'instruction 'else' dans une structure conditionnelle ?",
                    "answerOptions": [
                        {"text": "Elle gère le cas où la condition du 'if' est fausse", "isCorrect": True},
                        {"text": "Elle arrête immédiatement l'exécution du programme", "isCorrect": False},
                        {"text": "Elle définit une nouvelle variable pour le calcul", "isCorrect": False},
                        {"text": "Elle relance automatiquement la boucle depuis le début", "isCorrect": False}
                    ],
                    "correction": "L'instruction 'else' (sinon) est optionnelle. Elle permet de prévoir une action alternative au cas où la condition posée dans le 'if' n'est pas satisfaite. C'est l'aiguillage du programme."
                },
                {
                    "questionNumber": 95,
                    "question": "En algorithmique, quel est le résultat de 2 puissance 3 ?",
                    "answerOptions": [
                        {"text": "Le résultat entier égal à la valeur huit", "isCorrect": True},
                        {"text": "Le résultat entier égal à la valeur six", "isCorrect": False},
                        {"text": "Le résultat entier égal à la valeur cinq", "isCorrect": False},
                        {"text": "Le résultat entier égal à la valeur neuf", "isCorrect": False}
                    ],
                    "correction": "2³ = 2 x 2 x 2 = 8. C'est une opération fréquente en informatique, notamment pour le calcul des puissances de 2 (bits, octets, stockage)."
                },
                {
                    "questionNumber": 96,
                    "question": "En langage Python, comment nomme-t-on un nombre à virgule ?",
                    "answerOptions": [
                        {"text": "Un nombre de type flottant nommé float", "isCorrect": True},
                        {"text": "Un nombre de type entier nommé integer", "isCorrect": False},
                        {"text": "Un texte de type chaîne nommé string", "isCorrect": False},
                        {"text": "Une liste organisée nommée array ou list", "isCorrect": False}
                    ],
                    "correction": "En Python, on distingue 'int' (entier) de 'float' (décimal). Cette distinction est importante car l'ordinateur ne gère pas ces deux types de nombres de la même manière en mémoire vive."
                },
                {
                    "questionNumber": 97,
                    "question": "Que permet concrètement de faire l'instruction 'input' ?",
                    "answerOptions": [
                        {"text": "Demander une valeur à saisir par l'utilisateur", "isCorrect": True},
                        {"text": "Afficher un message texte sur la console", "isCorrect": False},
                        {"text": "Fermer définitivement le programme en cours", "isCorrect": False},
                        {"text": "Calculer la racine carrée d'un nombre positif", "isCorrect": False}
                    ],
                    "correction": "L'instruction input() met le programme en pause et attend que l'utilisateur tape quelque chose au clavier. Par défaut, ce qui est saisi est considéré comme du texte (une chaîne de caractères)."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est l'indice du premier élément d'une liste en Python ?",
                    "answerOptions": [
                        {"text": "L'indice égal à la valeur entière de zéro", "isCorrect": True},
                        {"text": "L'indice égal à la valeur entière de un", "isCorrect": False},
                        {"text": "L'indice négatif égal à la valeur de moins un", "isCorrect": False},
                        {"text": "La lettre A utilisée pour marquer le début", "isCorrect": False}
                    ],
                    "correction": "C'est une règle majeure : en informatique, on commence presque toujours à compter à partir de 0. Pour accéder au premier élément d'une liste 'L', on écrira donc L[0]. Le dernier élément d'une liste de 10 objets est à l'indice 9."
                },
                {
                    "questionNumber": 99,
                    "question": "Que signifie précisément l'opérateur logique '!=' ?",
                    "answerOptions": [
                        {"text": "La relation est différente de dans un test", "isCorrect": True},
                        {"text": "La relation est égale à dans un test logique", "isCorrect": False},
                        {"text": "La relation est supérieure ou égale à la suivante", "isCorrect": False},
                        {"text": "Un message d'attention simple pour l'utilisateur", "isCorrect": False}
                    ],
                    "correction": "Il s'agit du test d'inégalité. Il permet de vérifier qu'une valeur n'est pas identique à une autre. Par exemple 'if age != 18:' s'exécutera pour tous les âges sauf 18."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel symbole entoure une chaîne de caractères (du texte) ?",
                    "answerOptions": [
                        {"text": "Des guillemets doubles ou des guillemets simples", "isCorrect": True},
                        {"text": "Des parenthèses ouvrantes et des fermantes", "isCorrect": False},
                        {"text": "Des crochets situés sur les touches spécifiques", "isCorrect": False},
                        {"text": "Aucun symbole particulier n'est exigé par le code", "isCorrect": False}
                    ],
                    "correction": "En Python, les chaînes de caractères (type 'string') doivent être encadrées par des guillemets doubles (\" \") ou des apostrophes (' '). Cela permet à l'ordinateur de comprendre que le contenu est du texte littéral et non une variable ou une commande."
                }
            ]
        }
    }
}