quiz_data = {
    "title": "Quiz Bac Pro Mathématiques N°2 - Niveau Avancé (100 Questions) - Version Optimisée",
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
                        {"text": "Diviser la valeur 1 par 1,25 puis soustraire la valeur 1", "isCorrect": True},
                        {"text": "Prendre l'opposé du taux de départ soit une valeur de moins 0,25", "isCorrect": False},
                        {"text": "Multiplier la valeur 1 par 0,75 pour compenser la hausse initiale", "isCorrect": False},
                        {"text": "Diviser la valeur finale obtenue par le taux d'évolution de départ", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour trouver une évolution réciproque, on cherche le coefficient multiplicateur inverse. Si le CM initial est 1,25 (hausse de 25%), le CM réciproque est 1 / 1,25 = 0,8. Le taux réciproque est alors (0,8 - 1) = -0,2, ce qui correspond à une baisse de 20 % pour revenir à la valeur de départ."
                },
                {
                    "questionNumber": 2,
                    "question": "Si une action perd 20% de sa valeur, de quel pourcentage doit-elle augmenter pour retrouver sa valeur initiale ?",
                    "answerOptions": [
                        {"text": "Elle doit augmenter de vingt-cinq pour cent", "isCorrect": True},
                        {"text": "Elle doit augmenter de vingt pour cent exactement", "isCorrect": False},
                        {"text": "Elle doit augmenter de cent-vingt pour cent au total", "isCorrect": False},
                        {"text": "Elle doit augmenter de vingt-deux virgule cinq pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une baisse de 20 % correspond à un coefficient multiplicateur (CM) de 0,8 (1 - 0,20). Pour retrouver la valeur initiale, on applique le CM réciproque : 1 / 0,8 = 1,25. Multiplier par 1,25 correspond à une hausse de 25 %."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le coefficient multiplicateur global correspondant à trois hausses successives de 10% ?",
                    "answerOptions": [
                        {"text": "Le coefficient multiplicateur final est de 1,331", "isCorrect": True},
                        {"text": "Le coefficient multiplicateur final est de 1,300", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur final est de 3,100", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur final est de 0,729", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Lors d'évolutions successives, les coefficients multiplicateurs se multiplient entre eux. Une hausse de 10 % correspond à un CM de 1,1. Pour trois hausses, on calcule 1,1 x 1,1 x 1,1 (ou 1,1³), ce qui donne 1,331. Cela correspond à une hausse globale de 33,1 %."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment appelle-t-on le rapport entre la variation absolue et la valeur initiale ?",
                    "answerOptions": [
                        {"text": "Le taux d'évolution de la grandeur étudiée", "isCorrect": True},
                        {"text": "L'indice de base cent au début de la période", "isCorrect": False},
                        {"text": "La remise commerciale accordée sur le prix", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur de la variation", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le taux d'évolution (t) mesure la variation relative. Il se calcule par la formule : t = (Valeur Finale - Valeur Initiale) / Valeur Initiale. On l'exprime généralement sous forme de pourcentage en multipliant le résultat par 100."
                },
                {
                    "questionNumber": 5,
                    "question": "Une population passe de 500 à 600 individus. Quel est le taux d'évolution ?",
                    "answerOptions": [
                        {"text": "Un taux d'évolution positif de vingt pour cent", "isCorrect": True},
                        {"text": "Un taux d'évolution positif de cent pour cent", "isCorrect": False},
                        {"text": "Un taux d'évolution positif de cent-vingt pour cent", "isCorrect": False},
                        {"text": "Un taux d'évolution positif de dix pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On applique la formule : (600 - 500) / 500 = 100 / 500 = 0,2. Pour obtenir le pourcentage, on multiplie par 100, soit 20 %. La population a donc augmenté de 20 %."
                },
                {
                    "questionNumber": 6,
                    "question": "Que signifie un indice de 105 par rapport à une année de référence base 100 ?",
                    "answerOptions": [
                        {"text": "Une augmentation de 5% par rapport à l'année de référence", "isCorrect": True},
                        {"text": "Que le prix est de cent-cinq euros exactement au final", "isCorrect": False},
                        {"text": "Une baisse de 5% de la production sur l'ensemble de la période", "isCorrect": False},
                        {"text": "Que la valeur de départ a été multipliée par cent-cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'indice permet de comparer des valeurs à une base fixe (généralement 100). Un indice de 105 signifie que la valeur est 1,05 fois supérieure à la base, soit une hausse de 5 %. Formule : Indice = (Valeur / Valeur de référence) x 100."
                },
                {
                    "questionNumber": 7,
                    "question": "Un prix subit une hausse de 50% suivie d'une baisse de 50%. Le prix final est :",
                    "answerOptions": [
                        {"text": "Strictement inférieur au prix initial de départ", "isCorrect": True},
                        {"text": "Strictement égal au prix initial de départ", "isCorrect": False},
                        {"text": "Strictement supérieur au prix initial de départ", "isCorrect": False},
                        {"text": "Nul car les deux variations s'annulent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Hausse de 50 % (CM = 1,5) et baisse de 50 % (CM = 0,5). CM global = 1,5 x 0,5 = 0,75. Puisque 0,75 est inférieur à 1, le prix a baissé. La baisse totale est de 25 % (0,75 - 1 = -0,25)."
                },
                {
                    "questionNumber": 8,
                    "question": "Le taux d'évolution global de deux hausses successives de 20% est de :",
                    "answerOptions": [
                        {"text": "Une hausse globale de quarante-quatre pour cent", "isCorrect": True},
                        {"text": "Une hausse globale de quarante pour cent", "isCorrect": False},
                        {"text": "Une hausse globale de vingt pour cent au total", "isCorrect": False},
                        {"text": "Une hausse globale de quatre pour cent au total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On multiplie les coefficients multiplicateurs : 1,2 x 1,2 = 1,44. Le taux global est (1,44 - 1) x 100 = 44 %. Ce n'est pas 40 % car la deuxième hausse s'applique sur un montant déjà augmenté."
                },
                {
                    "questionNumber": 9,
                    "question": "Si l'indice d'un produit est 80, quelle a été l'évolution depuis la base 100 ?",
                    "answerOptions": [
                        {"text": "Une baisse de vingt pour cent de la valeur", "isCorrect": True},
                        {"text": "Une baisse de quatre-vingts pour cent de la valeur", "isCorrect": False},
                        {"text": "Une hausse de quatre-vingts pour cent de la valeur", "isCorrect": False},
                        {"text": "Une baisse de zéro virgule huit pour cent de la valeur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'évolution en pourcentage est donnée par (Indice - 100). Ici, 80 - 100 = -20. Le signe moins indique une diminution. La valeur a donc baissé de 20 %."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le coefficient multiplicateur correspondant à une baisse de 2% ?",
                    "answerOptions": [
                        {"text": "Un coefficient multiplicateur égal à 0,98", "isCorrect": True},
                        {"text": "Un coefficient multiplicateur égal à 0,02", "isCorrect": False},
                        {"text": "Un coefficient multiplicateur égal à 1,02", "isCorrect": False},
                        {"text": "Un coefficient multiplicateur égal à 0,20", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le coefficient multiplicateur (CM) pour une baisse se calcule par la formule : CM = 1 - (t / 100). Ici, CM = 1 - (2 / 100) = 1 - 0,02 = 0,98."
                },
                {
                    "questionNumber": 11,
                    "question": "Comment calcule-t-on la variation absolue d'une grandeur ?",
                    "answerOptions": [
                        {"text": "Valeur Finale moins Valeur Initiale", "isCorrect": True},
                        {"text": "Valeur Finale divisée par Valeur Initiale", "isCorrect": False},
                        {"text": "Valeur Initiale moins Valeur Finale", "isCorrect": False},
                        {"text": "Valeur Finale plus Valeur Initiale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La variation absolue mesure l'écart réel entre deux états. Contrairement au taux, elle s'exprime dans la même unité que les données (en euros, en kg, etc.). Si elle est négative, il s'agit d'une diminution."
                },
                {
                    "questionNumber": 12,
                    "question": "Une remise commerciale de 30% correspond à quel CM ?",
                    "answerOptions": [
                        {"text": "Un coefficient multiplicateur égal à 0,7", "isCorrect": True},
                        {"text": "Un coefficient multiplicateur égal à 0,3", "isCorrect": False},
                        {"text": "Un coefficient multiplicateur égal à 1,3", "isCorrect": False},
                        {"text": "Un coefficient multiplicateur égal à la valeur 3", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une remise est une baisse de prix. On applique la formule de la diminution : CM = 1 - 0,30 = 0,7. Multiplier un prix par 0,7 revient à retirer 30 % de sa valeur."
                },
                {
                    "questionNumber": 13,
                    "question": "Pour doubler une valeur, quel est le taux d'augmentation ?",
                    "answerOptions": [
                        {"text": "Une augmentation de cent pour cent", "isCorrect": True},
                        {"text": "Une augmentation de deux-cents pour cent", "isCorrect": False},
                        {"text": "Une augmentation de cinquante pour cent", "isCorrect": False},
                        {"text": "Une augmentation de deux pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Doubler une valeur signifie que l'on ajoute une fois la valeur initiale à elle-même. Si le prix passe de 10 à 20, la hausse est de 10. Taux = (20-10)/10 = 1, soit 100 % d'augmentation."
                },
                {
                    "questionNumber": 14,
                    "question": "Si le prix HT est 100€ et le prix TTC 120€, quel est l'indice du TTC base 100 HT ?",
                    "answerOptions": [
                        {"text": "L'indice de la valeur TTC est de cent-vingt", "isCorrect": True},
                        {"text": "L'indice de la valeur TTC est de vingt", "isCorrect": False},
                        {"text": "L'indice de la valeur TTC est de un virgule deux", "isCorrect": False},
                        {"text": "L'indice de la valeur TTC est de cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'indice se calcule par (Valeur à comparer / Valeur de référence) x 100. Ici : (120 / 100) x 100 = 120. L'indice permet de lire directement que le prix TTC est 20 % plus cher que le prix HT."
                },
                {
                    "questionNumber": 15,
                    "question": "Si un CM est de 2,5, quelle est l'augmentation en pourcentage ?",
                    "answerOptions": [
                        {"text": "Une hausse de cent-cinquante pour cent", "isCorrect": True},
                        {"text": "Une hausse de deux-cent-cinquante pour cent", "isCorrect": False},
                        {"text": "Une hausse de vingt-cinq pour cent", "isCorrect": False},
                        {"text": "Une hausse de cinquante pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le taux d'évolution t se déduit du coefficient multiplicateur par la formule : t = (CM - 1) x 100. Ici, t = (2,5 - 1) x 100 = 1,5 x 100 = 150 % d'augmentation."
                },
                {
                    "questionNumber": 16,
                    "question": "Pour tripler une valeur, le taux d'évolution est de :",
                    "answerOptions": [
                        {"text": "Un taux positif de deux-cents pour cent", "isCorrect": True},
                        {"text": "Un taux positif de trois-cents pour cent", "isCorrect": False},
                        {"text": "Un taux positif de trois pour cent", "isCorrect": False},
                        {"text": "Un taux positif de cent pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Tripler signifie multiplier par 3. Le taux est donc (3 - 1) x 100 = 200 %. On a ajouté deux fois la valeur initiale à elle-même."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est la valeur initiale si après une hausse de 10% on obtient 110 ?",
                    "answerOptions": [
                        {"text": "Une valeur initiale égale à cent", "isCorrect": True},
                        {"text": "Une valeur initiale égale à cent virgule un", "isCorrect": False},
                        {"text": "Une valeur initiale égale à cent-vingt-et-un", "isCorrect": False},
                        {"text": "Une valeur initiale égale à quatre-vingt-dix", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On sait que Valeur Initiale x CM = Valeur Finale. Donc VI = VF / CM. Ici, pour une hausse de 10 %, le CM est 1,1. VI = 110 / 1,1 = 100."
                },
                {
                    "questionNumber": 18,
                    "question": "Un taux d'évolution de 0% signifie que :",
                    "answerOptions": [
                        {"text": "La grandeur est restée strictement constante", "isCorrect": True},
                        {"text": "La grandeur est devenue nulle après l'évolution", "isCorrect": False},
                        {"text": "On ne peut pas calculer d'évolution dans ce cas", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur associé est zéro", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si la valeur finale est égale à la valeur initiale, la variation est nulle. Le coefficient multiplicateur est alors de 1 (1 + 0/100). La stabilité se traduit par un taux de 0 %."
                },
                {
                    "questionNumber": 19,
                    "question": "Si CM = 1,005, l'augmentation est de :",
                    "answerOptions": [
                        {"text": "Zéro virgule cinq pour cent", "isCorrect": True},
                        {"text": "Cinq pour cent exactement", "isCorrect": False},
                        {"text": "Cinquante pour cent exactement", "isCorrect": False},
                        {"text": "Zéro virgule zéro cinq pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On applique t = (CM - 1) x 100. Ici, (1,005 - 1) x 100 = 0,005 x 100 = 0,5 %. C'est une très faible augmentation."
                },
                {
                    "questionNumber": 20,
                    "question": "L'indice de prix à la consommation sert à mesurer :",
                    "answerOptions": [
                        {"text": "L'inflation sur une période donnée", "isCorrect": True},
                        {"text": "Le nombre de magasins sur le territoire", "isCorrect": False},
                        {"text": "Le poids moyen des aliments vendus", "isCorrect": False},
                        {"text": "La météo et son influence sur les ventes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'IPC (établi par l'INSEE en France) suit l'évolution des prix d'un 'panier de biens et services' représentatif de la consommation des ménages. Son augmentation annuelle définit le taux d'inflation."
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
                    "question": "Quelle est la dérivée de la fonction de référence f(x) = x² ?",
                    "answerOptions": [
                        {"text": "La fonction dérivée est f'(x) = 2x", "isCorrect": True},
                        {"text": "La fonction dérivée est f'(x) = x", "isCorrect": False},
                        {"text": "La fonction dérivée est f'(x) = 2", "isCorrect": False},
                        {"text": "La fonction dérivée est f'(x) = 1/x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La règle générale de dérivation pour une puissance de x (x^n) est de multiplier par l'exposant n et de diminuer l'exposant de 1. Pour x², on a n=2, donc f'(x) = 2 * x^(2-1) = 2x."
                },
                {
                    "questionNumber": 22,
                    "question": "Que permet de déterminer le signe de la dérivée f'(x) ?",
                    "answerOptions": [
                        {"text": "Le sens de variation de la fonction initiale f", "isCorrect": True},
                        {"text": "Le signe positif ou négatif de la fonction f", "isCorrect": False},
                        {"text": "L'ordonnée à l'origine de la droite de f", "isCorrect": False},
                        {"text": "Le coefficient directeur de la droite sécante", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est l'utilité principale de la dérivation. Si f'(x) est positive sur un intervalle, alors f est croissante sur cet intervalle. Si f'(x) est négative, f est décroissante. Si f'(x) est nulle, f est constante (ou présente un extremum)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la valeur de la dérivée d'une fonction constante f(x) = k ?",
                    "answerOptions": [
                        {"text": "Une valeur dérivée nulle égale à zéro", "isCorrect": True},
                        {"text": "Une valeur dérivée égale au chiffre un", "isCorrect": False},
                        {"text": "Une valeur dérivée égale à la constante k", "isCorrect": False},
                        {"text": "Une valeur dérivée égale à la variable x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une fonction constante ne varie pas (sa courbe est une droite horizontale). Puisque la dérivée mesure le taux de variation, celui-ci est logiquement nul. Pour tout k réel, (k)' = 0."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on le point où la dérivée s'annule en changeant de signe ?",
                    "answerOptions": [
                        {"text": "Un extremum de la fonction (maximum ou minimum)", "isCorrect": True},
                        {"text": "L'origine du repère orthonormé choisi", "isCorrect": False},
                        {"text": "Une racine réelle de la fonction étudiée", "isCorrect": False},
                        {"text": "Une asymptote horizontale vers l'infini", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Lorsqu'une fonction cesse de croître pour décroître (ou inversement), sa courbe atteint un sommet ou un creux. À cet endroit, la tangente est horizontale et la dérivée vaut zéro. On parle d'extremum local."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la primitive de la fonction f(x) = x ?",
                    "answerOptions": [
                        {"text": "Une primitive possible est F(x) = 0,5x²", "isCorrect": True},
                        {"text": "Une primitive possible est F(x) = 1", "isCorrect": False},
                        {"text": "Une primitive possible est F(x) = x²", "isCorrect": False},
                        {"text": "Une primitive possible est F(x) = 2x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Chercher une primitive consiste à trouver la fonction F telle que F' = f. Puisque la dérivée de x² est 2x, la dérivée de 0,5x² est 0,5 * 2x = x. On ajoute souvent une constante C car il existe une infinité de primitives."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la forme de la courbe d'une fonction du second degré ?",
                    "answerOptions": [
                        {"text": "Une parabole symétrique par rapport à un axe", "isCorrect": True},
                        {"text": "Une droite passant par l'origine du repère", "isCorrect": False},
                        {"text": "Une hyperbole composée de deux branches", "isCorrect": False},
                        {"text": "Un cercle parfait de rayon déterminé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les fonctions du type f(x) = ax² + bx + c sont représentées par des paraboles. Leur orientation dépend du signe de 'a' : tournée vers le haut si a > 0 (forme de bol) et vers le bas si a < 0 (forme de cloche)."
                },
                {
                    "questionNumber": 27,
                    "question": "Dans f(x) = ax² + bx + c, comment appelle-t-on le nombre Δ = b² - 4ac ?",
                    "answerOptions": [
                        {"text": "Le discriminant de l'équation du second degré", "isCorrect": True},
                        {"text": "Le dénominateur de la fraction rationnelle", "isCorrect": False},
                        {"text": "Le diviseur commun de l'expression algébrique", "isCorrect": False},
                        {"text": "Le degré de la fonction polynomiale choisie", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le discriminant Δ (Delta) permet de savoir si l'équation f(x) = 0 a des solutions réelles. Si Δ > 0, il y a deux racines ; si Δ = 0, une racine unique ; si Δ < 0, aucune racine réelle."
                },
                {
                    "questionNumber": 28,
                    "question": "Si le discriminant Δ est négatif, combien de racines possède l'équation ?",
                    "answerOptions": [
                        {"text": "Aucune racine réelle sur l'ensemble choisi", "isCorrect": True},
                        {"text": "Une seule racine réelle appelée racine double", "isCorrect": False},
                        {"text": "Deux racines réelles distinctes et séparées", "isCorrect": False},
                        {"text": "Une infinité de racines sur l'ensemble R", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Lorsque Δ < 0, le polynôme ax² + bx + c ne s'annule jamais. Graphiquement, cela signifie que la parabole ne traverse jamais l'axe des abscisses (elle est soit entièrement au-dessus, soit entièrement au-dessous)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la dérivée de la fonction affine f(x) = 5x + 3 ?",
                    "answerOptions": [
                        {"text": "La fonction dérivée est f'(x) = 5", "isCorrect": True},
                        {"text": "La fonction dérivée est f'(x) = 5x", "isCorrect": False},
                        {"text": "La fonction dérivée est f'(x) = 3", "isCorrect": False},
                        {"text": "La fonction dérivée est f'(x) = 8", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La dérivée d'une fonction affine f(x) = ax + b est toujours égale au coefficient directeur 'a'. Ici a=5. La constante b (le 3) disparaît car sa dérivée est nulle."
                },
                {
                    "questionNumber": 30,
                    "question": "Que représente géométriquement la valeur du nombre dérivé f'(a) ?",
                    "answerOptions": [
                        {"text": "Le coefficient directeur de la tangente à la courbe en a", "isCorrect": True},
                        {"text": "L'aire située sous la courbe entre deux points donnés", "isCorrect": False},
                        {"text": "La distance la plus courte par rapport à l'origine", "isCorrect": False},
                        {"text": "L'intersection de la courbe avec l'axe des ordonnées", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le nombre dérivé f'(a) donne la pente de la droite qui 'frôle' la courbe au point d'abscisse a. Cette droite est appelée la tangente. Elle permet de connaître la direction locale de la fonction."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la dérivée de la fonction inverse f(x) = 1/x ?",
                    "answerOptions": [
                        {"text": "La fonction dérivée est f'(x) = -1/x²", "isCorrect": True},
                        {"text": "La fonction dérivée est f'(x) = 1/x²", "isCorrect": False},
                        {"text": "La fonction dérivée est f'(x) = ln(x)", "isCorrect": False},
                        {"text": "La fonction dérivée est f'(x) = 0", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Il s'agit d'une formule de référence à connaître par cœur. La fonction f(x) = 1/x est définie sur R* (tout sauf zéro). Sa dérivée est toujours négative, ce qui confirme que la fonction inverse est toujours décroissante sur ses intervalles de définition."
                },
                {
                    "questionNumber": 32,
                    "question": "Sur l'ensemble des réels R, la fonction f(x) = x³ est :",
                    "answerOptions": [
                        {"text": "Strictement croissante sur l'ensemble de définition", "isCorrect": True},
                        {"text": "Décroissante pour les valeurs de x négatives", "isCorrect": False},
                        {"text": "Une parabole symétrique par rapport à l'axe y", "isCorrect": False},
                        {"text": "Une fonction paire possédant un centre de symétrie", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La dérivée de x³ est 3x². Un carré étant toujours positif ou nul, 3x² est toujours ≥ 0. La fonction cube est donc croissante sur tout R. Elle présente une 'stagnation' (point d'inflexion) en zéro."
                },
                {
                    "questionNumber": 33,
                    "question": "L'équation de la tangente au point d'abscisse a est :",
                    "answerOptions": [
                        {"text": "La forme y = f'(a)(x - a) + f(a)", "isCorrect": True},
                        {"text": "La forme y = ax + b classique", "isCorrect": False},
                        {"text": "La forme y = f(a)x + f'(a)", "isCorrect": False},
                        {"text": "La forme y = x² + f(a)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Cette formule permet de calculer l'équation de la droite tangente. On y retrouve le coefficient directeur f'(a) et l'ordonnée du point de contact f(a). C'est une application directe du calcul de dérivée."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la dérivée de la fonction cube f(x) = x³ ?",
                    "answerOptions": [
                        {"text": "Trois fois la variable x au carré", "isCorrect": True},
                        {"text": "La variable x au carré simplement", "isCorrect": False},
                        {"text": "Trois fois la variable x simplement", "isCorrect": False},
                        {"text": "Un tiers de la variable x au carré", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On applique la règle (x^n)' = nx^(n-1). Pour n=3 : 3 * x^(3-1) = 3x². On utilise beaucoup ce calcul pour l'étude des variations des polynômes du troisième degré."
                },
                {
                    "questionNumber": 35,
                    "question": "Le sommet d'une parabole d'équation y = ax² + bx + c a pour abscisse :",
                    "answerOptions": [
                        {"text": "Le rapport négatif moins b divisé par deux a", "isCorrect": True},
                        {"text": "Le rapport positif b divisé par deux a", "isCorrect": False},
                        {"text": "Le rapport négatif moins c divisé par a", "isCorrect": False},
                        {"text": "Le rapport discriminant divisé par quatre a", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'abscisse du sommet (notée souvent α ou xS) est donnée par -b / 2a. Ce point correspond au maximum ou au minimum de la fonction. L'axe vertical passant par ce point est l'axe de symétrie de la parabole."
                },
                {
                    "questionNumber": 36,
                    "question": "Si a est négatif dans f(x) = ax² + bx + c, la parabole est tournée :",
                    "answerOptions": [
                        {"text": "Vers le bas avec l'ouverture vers le bas", "isCorrect": True},
                        {"text": "Vers le haut avec l'ouverture vers le haut", "isCorrect": False},
                        {"text": "Vers la droite de façon horizontale", "isCorrect": False},
                        {"text": "Vers la gauche de façon horizontale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si a < 0, la fonction croît puis décroît. Son sommet est donc un maximum. On dit parfois que la parabole fait 'la grimace' (concavité vers le bas)."
                },
                {
                    "questionNumber": 37,
                    "question": "La dérivée de la somme de deux fonctions (u + v)' est égale à :",
                    "answerOptions": [
                        {"text": "La somme des dérivées u' + v'", "isCorrect": True},
                        {"text": "L'expression complexe u'v + uv'", "isCorrect": False},
                        {"text": "Le produit simple des dérivées u'v'", "isCorrect": False},
                        {"text": "Le quotient u divisé par la dérivée v'", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La dérivation est une opération 'linéaire' vis-à-vis de l'addition. Dériver une somme revient à dériver chaque terme séparément et à les additionner. Attention : ce n'est pas vrai pour le produit (u*v) ou le quotient (u/v)."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la dérivée de la fonction racine carrée f(x) = √x ?",
                    "answerOptions": [
                        {"text": "Le rapport un divisé par deux fois racine de x", "isCorrect": True},
                        {"text": "Deux fois racine de x sans division", "isCorrect": False},
                        {"text": "La variable x simplement", "isCorrect": False},
                        {"text": "Le rapport un divisé par la variable x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La fonction racine carrée f(x) = √x est définie sur [0 ; +inf[ mais elle n'est dérivable que sur ]0 ; +inf[. Sa dérivée f'(x) = 1 / (2√x) tend vers l'infini quand x se rapproche de zéro, ce qui signifie que la courbe possède une tangente verticale à l'origine."
                },
                {
                    "questionNumber": 39,
                    "question": "Que résume précisément un tableau de variations ?",
                    "answerOptions": [
                        {"text": "Le sens de variation et les extremums de la fonction", "isCorrect": True},
                        {"text": "La liste des coordonnées de tous les points du graphique", "isCorrect": False},
                        {"text": "Les prix de vente des différents produits d'une usine", "isCorrect": False},
                        {"text": "Le nom des axes et l'échelle utilisée pour le repère", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le tableau de variations utilise les résultats du signe de la dérivée pour indiquer par des flèches si la fonction monte ou descend. On y fait aussi apparaître les valeurs de x remarquables (bornes, racines de la dérivée) et les images des extremums."
                },
                {
                    "questionNumber": 40,
                    "question": "Que signifie mathématiquement que f(x) tend vers l'infini ?",
                    "answerOptions": [
                        {"text": "Les valeurs de y deviennent aussi grandes que souhaité", "isCorrect": True},
                        {"text": "La fonction s'arrête brutalement en un point précis", "isCorrect": False},
                        {"text": "La courbe est un cercle fermé sur lui-même", "isCorrect": False},
                        {"text": "La variable x est obligatoirement égale à zéro", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est la notion de limite. Quand on s'éloigne sur l'axe des abscisses (ou qu'on se rapproche d'une valeur interdite), les images f(x) peuvent croître sans limite. Sur un graphique, cela se traduit souvent par une branche qui s'éloigne vers le haut."
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
                        {"text": "Le quotient Côté adjacent divisé par l'Hypoténuse", "isCorrect": True},
                        {"text": "Le quotient Côté opposé divisé par l'Hypoténuse", "isCorrect": False},
                        {"text": "Le quotient Côté opposé divisé par le Côté adjacent", "isCorrect": False},
                        {"text": "Le quotient Hypoténuse divisé par le Côté opposé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La trigonométrie relie les angles aux rapports de longueurs. Le cosinus d'un angle aigu se calcule en divisant la longueur du côté qui 'touche' l'angle par la longueur du plus long côté (l'hypoténuse). Mémo : CAH."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la valeur exacte du cosinus d'un angle de 0° ?",
                    "answerOptions": [
                        {"text": "La valeur entière égale à un", "isCorrect": True},
                        {"text": "La valeur nulle égale à zéro", "isCorrect": False},
                        {"text": "La valeur décimale égale à 0,5", "isCorrect": False},
                        {"text": "Une valeur non définie ou infinie", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Sur le cercle trigonométrique de rayon 1, le cosinus est l'abscisse du point. Pour un angle de 0°, le point est situé à l'extrême droite du cercle, ses coordonnées sont (1 ; 0). Le cosinus vaut donc 1."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle relation lie le sinus et le cosinus d'un même angle α ?",
                    "answerOptions": [
                        {"text": "La somme des carrés cos²(α) + sin²(α) = 1", "isCorrect": True},
                        {"text": "La somme simple cos(α) + sin(α) = 1", "isCorrect": False},
                        {"text": "Le rapport sin(α) divisé par cos(α) = 1", "isCorrect": False},
                        {"text": "La différence des carrés cos²(α) - sin²(α) = 1", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est l'identité fondamentale de la trigonométrie. Elle découle du théorème de Pythagore appliqué dans le cercle trigonométrique. Elle permet de calculer le sinus d'un angle quand on connaît son cosinus (et inversement)."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le volume d'une sphère possédant un rayon R ?",
                    "answerOptions": [
                        {"text": "Quatre-tiers multiplié par Pi et par le rayon au cube", "isCorrect": True},
                        {"text": "Quatre multiplié par Pi et par le rayon au carré", "isCorrect": False},
                        {"text": "Le produit Pi multiplié par le rayon au carré", "isCorrect": False},
                        {"text": "Le produit deux fois Pi multiplié par le rayon", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Formule du volume : V = (4/3) x π x R³. Attention à ne pas confondre avec l'aire de la surface d'une sphère qui est 4 x π x R². Le résultat d'un volume s'exprime en unités cubiques (cm³, m³)."
                },
                {
                    "questionNumber": 45,
                    "question": "Combien de degrés font exactement π radians ?",
                    "answerOptions": [
                        {"text": "Un angle plat de cent-quatre-vingts degrés", "isCorrect": True},
                        {"text": "Un tour complet de trois-cent-soixante degrés", "isCorrect": False},
                        {"text": "Un angle droit de quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Une mesure nulle de zéro degré", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le radian est une unité de mesure d'angle basée sur la longueur de l'arc de cercle. Un cercle complet fait 2π radians (360°). Un demi-cercle (angle plat) fait donc π radians (180°)."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment calcule-t-on la diagonale d'un cube de côté 'a' ?",
                    "answerOptions": [
                        {"text": "La longueur du côté multipliée par racine de 3", "isCorrect": True},
                        {"text": "La longueur du côté multipliée par racine de 2", "isCorrect": False},
                        {"text": "La longueur du côté multipliée par trois", "isCorrect": False},
                        {"text": "La valeur du côté élevée au carré", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour la diagonale d'une face carrée, on utilise d = a√2. Pour la grande diagonale qui traverse le cube, on applique Pythagore dans l'espace, ce qui donne D = √(a² + a² + a²) = √3a² = a√3."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est la formule du volume d'un cône de révolution ?",
                    "answerOptions": [
                        {"text": "Un tiers multiplié par l'aire de la base et la hauteur", "isCorrect": True},
                        {"text": "Le produit direct de l'aire de la base par la hauteur", "isCorrect": False},
                        {"text": "Le produit Pi par le rayon au carré et la hauteur", "isCorrect": False},
                        {"text": "Le produit deux fois Pi par le rayon et la hauteur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un cône (ou une pyramide) occupe exactement le tiers du volume du solide 'droit' (cylindre ou pavé) ayant la même base et la même hauteur. Formule : V = (1/3) x π x R² x h."
                },
                {
                    "questionNumber": 48,
                    "question": "Que vaut le sinus d'un angle de 90° ou π/2 radians ?",
                    "answerOptions": [
                        {"text": "La valeur entière maximale égale à un", "isCorrect": True},
                        {"text": "La valeur nulle minimale égale à zéro", "isCorrect": False},
                        {"text": "La valeur entière négative égale à moins un", "isCorrect": False},
                        {"text": "La valeur décimale égale à zéro virgule cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans le cercle trigonométrique, le sinus est l'ordonnée (axe vertical). À 90°, le point est au sommet du cercle, sa coordonnée verticale est donc 1. C'est la valeur maximale possible pour un sinus réel."
                },
                {
                    "questionNumber": 49,
                    "question": "Dans un triangle rectangle, la Tangente d'un angle est :",
                    "answerOptions": [
                        {"text": "Le quotient Côté opposé divisé par le Côté adjacent", "isCorrect": True},
                        {"text": "Le quotient Côté adjacent divisé par le Côté opposé", "isCorrect": False},
                        {"text": "Le produit du Sinus par le Cosinus de l'angle", "isCorrect": False},
                        {"text": "Le quotient Côté opposé divisé par l'Hypoténuse", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La tangente (tan) est le rapport entre les deux côtés de l'angle droit. On peut aussi la calculer en faisant tan(α) = sin(α) / cos(α). Mémo : TOA (Tangente = Opposé / Adjacent)."
                },
                {
                    "questionNumber": 50,
                    "question": "Un cylindre a un rayon de 3cm et une hauteur de 10cm. Quel est son volume ?",
                    "answerOptions": [
                        {"text": "Environ deux-cent-quatre-vingt-trois centimètres cubes", "isCorrect": True},
                        {"text": "Environ trente centimètres cubes seulement", "isCorrect": False},
                        {"text": "Environ quatre-vingt-dix centimètres cubes seulement", "isCorrect": False},
                        {"text": "Environ cent-quatre-vingt-huit centimètres cubes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** V = π x R² x h. Ici : V = π x 3² x 10 = π x 9 x 10 = 90π. Avec π ≈ 3,14, on obtient 90 x 3,14 = 282,6 cm³. On arrondit à 283."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la forme de la section d'une sphère par un plan ?",
                    "answerOptions": [
                        {"text": "Un cercle ou un point selon la position du plan", "isCorrect": True},
                        {"text": "Un carré parfait quelle que soit la position", "isCorrect": False},
                        {"text": "Un triangle équilatéral au centre de la figure", "isCorrect": False},
                        {"text": "Un rectangle dont les côtés dépendent du rayon", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si vous 'coupez' une balle (une sphère) avec un couteau (un plan), la trace de la coupure sera toujours un cercle. Si le plan ne fait que 'frôler' la sphère, la section se réduit à un seul point (point de tangence)."
                },
                {
                    "questionNumber": 52,
                    "question": "Combien de faces possède un parallélépipède rectangle ?",
                    "answerOptions": [
                        {"text": "Un total de six faces rectangulaires", "isCorrect": True},
                        {"text": "Un total de quatre faces rectangulaires", "isCorrect": False},
                        {"text": "Un total de huit faces rectangulaires", "isCorrect": False},
                        {"text": "Un total de douze faces rectangulaires", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un pavé droit (comme une boîte à chaussures) possède 6 faces (opposées deux à deux), 8 sommets et 12 arêtes. Si toutes les faces sont des carrés, il devient un cube."
                },
                {
                    "questionNumber": 53,
                    "question": "L'unité d'un volume est le mètre cube. 1 m³ vaut :",
                    "answerOptions": [
                        {"text": "Une capacité égale à mille litres", "isCorrect": True},
                        {"text": "Une capacité égale à cent litres", "isCorrect": False},
                        {"text": "Une capacité égale à dix mille litres", "isCorrect": False},
                        {"text": "Une capacité égale à un seul litre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Il faut retenir que 1 dm³ = 1 litre. Comme 1 m³ = 1000 dm³ (car 10x10x10), alors 1 m³ correspond à 1000 litres. C'est une base indispensable pour les exercices sur les réservoirs ou les piscines."
                },
                {
                    "questionNumber": 54,
                    "question": "Que vaut le cosinus d'un angle droit (90°) ?",
                    "answerOptions": [
                        {"text": "La valeur nulle égale à zéro", "isCorrect": True},
                        {"text": "La valeur entière égale à un", "isCorrect": False},
                        {"text": "La valeur décimale égale à 0,5", "isCorrect": False},
                        {"text": "La valeur entière négative de moins un", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** À 90°, l'angle est vertical. Sa projection sur l'axe horizontal (abscisse) est nulle. Donc cos(90°) = 0. Inversement, son sinus est maximal (sin 90° = 1)."
                },
                {
                    "questionNumber": 55,
                    "question": "Une pyramide à base carrée de côté 3m et de hauteur 4m a pour volume :",
                    "answerOptions": [
                        {"text": "Un volume égal à douze mètres cubes", "isCorrect": True},
                        {"text": "Un volume égal à trente-six mètres cubes", "isCorrect": False},
                        {"text": "Un volume égal à neuf mètres cubes", "isCorrect": False},
                        {"text": "Un volume égal à seize mètres cubes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** V = (1/3) x Base x H. Aire de la base (carré) = 3 x 3 = 9 m². Volume = (1/3) x 9 x 4 = 3 x 4 = 12 m³."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'instrument pour mesurer un angle en géométrie ?",
                    "answerOptions": [
                        {"text": "Le rapporteur gradué en degrés", "isCorrect": True},
                        {"text": "Le compas à pointe sèche ou mine", "isCorrect": False},
                        {"text": "La règle plate graduée en millimètres", "isCorrect": False},
                        {"text": "Le thermomètre de précision à mercure", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le rapporteur permet de lire la mesure d'un angle. Il est généralement semi-circulaire (180°) ou circulaire (360°). On l'aligne sur le sommet de l'angle et l'un de ses côtés."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle est la valeur exacte du sinus d'un angle de 30° ?",
                    "answerOptions": [
                        {"text": "Une valeur exacte égale à 0,5", "isCorrect": True},
                        {"text": "Une valeur exacte égale à la valeur un", "isCorrect": False},
                        {"text": "Une valeur approchée égale à 0,707", "isCorrect": False},
                        {"text": "Une valeur approchée égale à 0,866", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une valeur remarquable à connaître. sin(30°) = 1/2 = 0,5. À cet angle, le côté opposé mesure exactement la moitié de l'hypoténuse."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment s'appelle une droite qui touche un cercle en un seul point ?",
                    "answerOptions": [
                        {"text": "La tangente au cercle en ce point précis", "isCorrect": True},
                        {"text": "La sécante qui traverse le cercle en deux points", "isCorrect": False},
                        {"text": "Le diamètre qui passe par le centre du cercle", "isCorrect": False},
                        {"text": "Le rayon qui relie le centre à la bordure", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La tangente est perpendiculaire au rayon au point de contact. C'est la droite qui 'effleure' le cercle sans jamais entrer à l'intérieur de sa surface."
                },
                {
                    "questionNumber": 59,
                    "question": "Un angle obtus est un angle dont la mesure est :",
                    "answerOptions": [
                        {"text": "Comprise entre quatre-vingt-dix et cent-quatre-vingts degrés", "isCorrect": True},
                        {"text": "Inférieure à quatre-vingt-dix degrés exactement", "isCorrect": False},
                        {"text": "Égale à quatre-vingt-dix degrés exactement", "isCorrect": False},
                        {"text": "Égale à cent-quatre-vingts degrés exactement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un angle aigu est < 90°. Un angle droit = 90°. Un angle obtus est plus ouvert qu'un angle droit mais moins qu'un angle plat (entre 90° et 180°)."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle est l'aire totale des faces d'un cube de côté 2cm ?",
                    "answerOptions": [
                        {"text": "Vingt-quatre centimètres carrés au total", "isCorrect": True},
                        {"text": "Huit centimètres carrés au total", "isCorrect": False},
                        {"text": "Quatre centimètres carrés au total", "isCorrect": False},
                        {"text": "Seize centimètres carrés au total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un cube possède 6 faces carrées identiques. Aire d'une face = 2 x 2 = 4 cm². Aire totale = 6 faces x 4 cm² = 24 cm²."
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
                        {"text": "Un nuage de points représentant les couples de données", "isCorrect": True},
                        {"text": "Un histogramme composé de rectangles juxtaposés", "isCorrect": False},
                        {"text": "Un diagramme circulaire divisé en secteurs angulaires", "isCorrect": False},
                        {"text": "Une courbe de Gauss représentant une loi normale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** En statistique bivariée (à deux variables), chaque individu est représenté par un point dont les coordonnées (x ; y) correspondent aux deux caractères mesurés (ex: taille et poids). L'ensemble de ces points forme un 'nuage'."
                },
                {
                    "questionNumber": 62,
                    "question": "Qu'est-ce que le point moyen G d'un nuage statistique ?",
                    "answerOptions": [
                        {"text": "Le point dont les coordonnées sont les moyennes de x et de y", "isCorrect": True},
                        {"text": "Le point situé à la position la plus haute du graphique", "isCorrect": False},
                        {"text": "Le point situé exactement au milieu de l'axe des abscisses", "isCorrect": False},
                        {"text": "Le point d'origine du repère servant à la construction", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le point moyen G a pour abscisse la moyenne x̄ des valeurs de la première variable et pour ordonnée la moyenne ȳ de la seconde. G(x̄ ; ȳ). C'est le 'centre de gravité' du nuage."
                },
                {
                    "questionNumber": 63,
                    "question": "À quoi sert principalement une droite d'ajustement affine ?",
                    "answerOptions": [
                        {"text": "À modéliser la tendance du nuage pour faire des prévisions", "isCorrect": True},
                        {"text": "À relier tous les points entre eux par des segments brisés", "isCorrect": False},
                        {"text": "À décorer le graphique pour le rendre plus professionnel", "isCorrect": False},
                        {"text": "À calculer l'écart-type de chacune des deux variables", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si le nuage est allongé, on peut 'résumer' sa forme par une droite. L'équation de cette droite (y = ax + b) permet d'estimer des valeurs inconnues (extrapolation vers le futur ou interpolation entre deux points)."
                },
                {
                    "questionNumber": 64,
                    "question": "Une corrélation est dite positive entre deux variables si :",
                    "answerOptions": [
                        {"text": "La variable y augmente globalement quand x augmente", "isCorrect": True},
                        {"text": "La variable y diminue globalement quand x augmente", "isCorrect": False},
                        {"text": "La variable y reste constante quelle que soit la valeur de x", "isCorrect": False},
                        {"text": "Tous les points sont alignés sur l'axe des abscisses x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une corrélation positive signifie que les deux variables évoluent dans le même sens. Sur le graphique, cela se traduit par une droite d'ajustement qui a une pente (coefficient directeur a) positive."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle méthode permet de trouver l'équation de la droite la plus précise ?",
                    "answerOptions": [
                        {"text": "La méthode mathématique des moindres carrés", "isCorrect": True},
                        {"text": "La méthode de Mayer divisant le nuage en deux groupes", "isCorrect": False},
                        {"text": "Le calcul simple du produit en croix des moyennes", "isCorrect": False},
                        {"text": "La méthode au jugé en traçant la droite à la main", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La méthode des moindres carrés minimise la somme des carrés des distances verticales entre les points et la droite. C'est l'algorithme utilisé par les calculatrices (LinReg) pour donner les coefficients 'a' et 'b'."
                },
                {
                    "questionNumber": 66,
                    "question": "Que signifie un nuage de points présentant une forme très allongée ?",
                    "answerOptions": [
                        {"text": "Qu'il existe un lien statistique fort entre les deux variables", "isCorrect": True},
                        {"text": "Que les données collectées sont probablement fausses", "isCorrect": False},
                        {"text": "Qu'il n'y a aucune relation réelle entre les deux caractères", "isCorrect": False},
                        {"text": "Que la moyenne de l'ensemble des données est nulle", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Plus le nuage est 'serré' autour d'une direction, plus l'ajustement linéaire est de bonne qualité. Cela permet de dire que l'évolution de y est fortement dépendante de celle de x."
                },
                {
                    "questionNumber": 67,
                    "question": "Dans y = ax + b, si le coefficient a est proche de 0, cela signifie :",
                    "answerOptions": [
                        {"text": "La variable y dépend très peu de la variable x", "isCorrect": True},
                        {"text": "Le lien entre les deux variables est extrêmement fort", "isCorrect": False},
                        {"text": "La droite d'ajustement est quasiment verticale", "isCorrect": False},
                        {"text": "L'ensemble des valeurs statistiques sont positives", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un coefficient directeur nul (a = 0) correspond à une droite horizontale. Cela indique que même si x change, y reste à peu près au même niveau. Il n'y a donc pas de tendance linéaire marquée."
                },
                {
                    "questionNumber": 68,
                    "question": "Un coefficient de corrélation r proche de la valeur 1 signifie :",
                    "answerOptions": [
                        {"text": "Un lien linéaire positif fort entre les variables", "isCorrect": True},
                        {"text": "Une absence totale de lien entre les deux variables", "isCorrect": False},
                        {"text": "Une erreur de calcul lors du traitement des données", "isCorrect": False},
                        {"text": "Un lien linéaire négatif fort entre les variables", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le coefficient r est compris entre -1 et 1. S'il est proche de 1, les points sont presque alignés sur une droite montante. S'il est proche de -1, ils sont alignés sur une droite descendante. S'il est proche de 0, il n'y a pas d'alignement."
                },
                {
                    "questionNumber": 69,
                    "question": "En statistiques, que permet de faire l'interpolation ?",
                    "answerOptions": [
                        {"text": "Estimer une valeur située entre deux données connues", "isCorrect": True},
                        {"text": "Prévoir l'évolution dans le futur lointain hors série", "isCorrect": False},
                        {"text": "Calculer la moyenne totale de l'ensemble des points", "isCorrect": False},
                        {"text": "Changer les unités de mesure de l'axe des ordonnées", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'interpolation est l'utilisation de la droite d'ajustement pour trouver une valeur de y correspondant à un x situé à l'intérieur de l'intervalle d'étude. C'est généralement une estimation fiable."
                },
                {
                    "questionNumber": 70,
                    "question": "Le point moyen G appartient-il toujours à la droite d'ajustement ?",
                    "answerOptions": [
                        {"text": "Oui, par définition de la droite des moindres carrés", "isCorrect": True},
                        {"text": "Seulement si tous les points du nuage sont alignés", "isCorrect": False},
                        {"text": "Non, il est toujours situé légèrement au-dessus", "isCorrect": False},
                        {"text": "Seulement si l'ordonnée à l'origine est nulle", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une propriété fondamentale : la droite de régression de y en x passe obligatoirement par le point moyen G(x̄ ; ȳ). On utilise souvent cette règle pour tracer la droite précisément après avoir calculé ses coefficients."
                },
                {
                    "questionNumber": 71,
                    "question": "Si r = -0,95, comment qualifie-t-on la corrélation ?",
                    "answerOptions": [
                        {"text": "Une corrélation forte et de sens négatif", "isCorrect": True},
                        {"text": "Une corrélation très faible et quasi inexistante", "isCorrect": False},
                        {"text": "Une corrélation forte et de sens positif", "isCorrect": False},
                        {"text": "C'est une valeur impossible pour ce coefficient", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Puisque |r| est proche de 1, le lien est fort. Le signe moins indique que la droite descend : quand x augmente, y diminue fortement. L'ajustement linéaire est ici très pertinent."
                },
                {
                    "questionNumber": 72,
                    "question": "Comment appelle-t-on les points très éloignés de la tendance ?",
                    "answerOptions": [
                        {"text": "Des points aberrants ou des données atypiques", "isCorrect": True},
                        {"text": "Des points moyens servant de centre au nuage", "isCorrect": False},
                        {"text": "Des sommets de courbe situés sur les bords", "isCorrect": False},
                        {"text": "Des origines secondaires au sein du repère", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un point aberrant peut être dû à une erreur de mesure ou à un individu exceptionnel. Ces points peuvent fausser les calculs de la droite d'ajustement en 'tirant' la droite vers eux."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est l'unité du coefficient de corrélation linéaire r ?",
                    "answerOptions": [
                        {"text": "Il n'en possède aucune car c'est un nombre sans dimension", "isCorrect": True},
                        {"text": "Il s'exprime en euros comme les variables monétaires", "isCorrect": False},
                        {"text": "Il s'exprime systématiquement sous forme de pourcentage", "isCorrect": False},
                        {"text": "Il s'exprime en mètres comme les variables de longueur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le coefficient r est un pur indicateur de qualité de l'alignement. Il ne dépend pas des unités choisies pour x et y. C'est une valeur 'adimensionnelle'."
                },
                {
                    "questionNumber": 74,
                    "question": "Que signifie extrapoler à partir d'un nuage de points ?",
                    "answerOptions": [
                        {"text": "Estimer une valeur située en dehors de l'intervalle connu", "isCorrect": True},
                        {"text": "Calculer la moyenne arithmétique simple de la série", "isCorrect": False},
                        {"text": "Réduire la taille du graphique pour l'impression", "isCorrect": False},
                        {"text": "Changer le nom des deux variables sur les axes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'extrapolation consiste à faire des prévisions dans le futur (au-delà des données mesurées). C'est plus risqué que l'interpolation, car on suppose que le comportement observé va se prolonger de la même manière."
                },
                {
                    "questionNumber": 75,
                    "question": "Géométriquement, la droite d'ajustement passe par :",
                    "answerOptions": [
                        {"text": "Le point moyen G du nuage de points", "isCorrect": True},
                        {"text": "L'origine du repère de manière systématique", "isCorrect": False},
                        {"text": "Le point situé le plus haut dans le nuage", "isCorrect": False},
                        {"text": "L'intégralité des points de la série étudiée", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour tracer la droite des moindres carrés, on utilise deux repères : elle passe par le point G(x̄, ȳ) et coupe l'axe vertical à l'ordonnée 'b'. Elle passe 'au mieux' au milieu de l'ensemble des points."
                },
                {
                    "questionNumber": 76,
                    "question": "Si r = 0, cela signifie statistiquement :",
                    "answerOptions": [
                        {"text": "L'absence totale de corrélation linéaire entre x et y", "isCorrect": True},
                        {"text": "L'existence d'une corrélation parfaite entre x et y", "isCorrect": False},
                        {"text": "Que toutes les valeurs de la série sont nulles", "isCorrect": False},
                        {"text": "Que l'ajustement est une droite parfaitement verticale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un r nul indique que les points sont dispersés sans aucune direction privilégiée. Un ajustement par une droite n'a alors aucun sens mathématique."
                },
                {
                    "questionNumber": 77,
                    "question": "Dans y = 2x + 10, si x augmente de 1, la variable y augmente de :",
                    "answerOptions": [
                        {"text": "Une valeur égale à deux unités", "isCorrect": True},
                        {"text": "Une valeur égale à dix unités", "isCorrect": False},
                        {"text": "Une valeur égale à douze unités", "isCorrect": False},
                        {"text": "Une valeur égale à une seule unité", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est la définition même du coefficient directeur (la pente). Le nombre 'a' indique de combien l'ordonnée y varie lorsque l'abscisse x augmente de 1."
                },
                {
                    "questionNumber": 78,
                    "question": "Un nuage de points peut être modélisé par une droite si :",
                    "answerOptions": [
                        {"text": "Sa forme générale est allongée dans une direction", "isCorrect": True},
                        {"text": "Il ne contient pas plus de deux points de données", "isCorrect": False},
                        {"text": "Il forme un cercle parfait autour du centre G", "isCorrect": False},
                        {"text": "Les points sont tous situés sur l'axe des ordonnées", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est le critère visuel de validité. Si le nuage ressemble à une ellipse allongée, l'erreur commise en remplaçant les points par une droite sera faible. On valide souvent ce choix si |r| > 0,85."
                },
                {
                    "questionNumber": 79,
                    "question": "La variable dite 'expliquée' est généralement placée sur :",
                    "answerOptions": [
                        {"text": "L'axe vertical des ordonnées désigné par y", "isCorrect": True},
                        {"text": "L'axe horizontal des abscisses désigné par x", "isCorrect": False},
                        {"text": "Le titre situé au-dessus du graphique tracé", "isCorrect": False},
                        {"text": "La légende située à côté du cadre du graphique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On étudie y (l'effet) en fonction de x (la cause ou le temps). Par exemple : le chiffre d'affaires (y) en fonction du mois (x). x est la variable explicative et y la variable expliquée."
                },
                {
                    "questionNumber": 80,
                    "question": "Le coefficient b de l'équation y = ax + b est :",
                    "answerOptions": [
                        {"text": "L'ordonnée à l'origine de la droite tracée", "isCorrect": True},
                        {"text": "La pente ou inclinaison de la droite tracée", "isCorrect": False},
                        {"text": "La moyenne arithmétique de la variable x", "isCorrect": False},
                        {"text": "Le nombre total de points présents sur le nuage", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** b est la valeur de y lorsque x vaut 0. C'est l'endroit où la droite d'ajustement coupe l'axe vertical. On l'appelle ordonnée à l'origine."
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
                    "question": "Qu'est-ce qu'une épreuve de Bernoulli en probabilités ?",
                    "answerOptions": [
                        {"text": "Une expérience aléatoire avec deux issues : succès ou échec", "isCorrect": True},
                        {"text": "Une épreuve sportive de haut niveau chronométrée", "isCorrect": False},
                        {"text": "Un calcul de moyenne pondérée complexe sur une série", "isCorrect": False},
                        {"text": "Un tirage au sort infini au sein d'une population", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une épreuve de Bernoulli est une expérience qui n'a que deux issues possibles, par convention appelées 'Succès' (S) avec une probabilité p, et 'Échec' (E) avec une probabilité q = 1 - p. Exemple : Pile ou Face."
                },
                {
                    "questionNumber": 82,
                    "question": "Dans une loi binomiale B(n ; p), que représente la lettre 'n' ?",
                    "answerOptions": [
                        {"text": "Le nombre de répétitions indépendantes de l'épreuve", "isCorrect": True},
                        {"text": "La probabilité de succès lors de chaque tirage", "isCorrect": False},
                        {"text": "Le nombre total de succès finalement obtenus", "isCorrect": False},
                        {"text": "La moyenne arithmétique de la série de données", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** n désigne la taille de l'échantillon ou le nombre de fois que l'on répète l'expérience de Bernoulli de manière identique et indépendante (ex : on lance n fois le même dé)."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la probabilité de l'échec q si celle du succès p est 0,2 ?",
                    "answerOptions": [
                        {"text": "Une probabilité égale à zéro virgule huit", "isCorrect": True},
                        {"text": "Une probabilité égale à zéro virgule deux", "isCorrect": False},
                        {"text": "Une probabilité égale à la valeur entière de un", "isCorrect": False},
                        {"text": "Une probabilité égale à la valeur de zéro virgule cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Puisqu'il n'y a que deux issues, la somme des probabilités succès + échec vaut 1. Donc q = 1 - p. Ici, 1 - 0,2 = 0,8."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment calcule-t-on l'espérance E(X) d'une loi binomiale ?",
                    "answerOptions": [
                        {"text": "Le produit n fois p", "isCorrect": True},
                        {"text": "La somme n plus p", "isCorrect": False},
                        {"text": "Le quotient p divisé par n", "isCorrect": False},
                        {"text": "Le produit n fois p fois q", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'espérance E(X) = n * p représente le nombre moyen de succès que l'on peut espérer obtenir si on répète l'expérience un très grand nombre de fois."
                },
                {
                    "questionNumber": 85,
                    "question": "Pour utiliser une loi binomiale, les tirages doivent être :",
                    "answerOptions": [
                        {"text": "Indépendants et réalisés avec remise", "isCorrect": True},
                        {"text": "Liés entre eux par une condition logique", "isCorrect": False},
                        {"text": "Uniques et réalisés sans aucune remise", "isCorrect": False},
                        {"text": "Faits obligatoirement par la même personne", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'indépendance signifie que le résultat d'un tirage ne doit pas influencer le suivant. En pratique, cela correspond à un tirage avec remise ou sur une population si grande que le prélèvement ne change pas les probabilités."
                },
                {
                    "questionNumber": 86,
                    "question": "Que représente la variable aléatoire X dans une loi binomiale ?",
                    "answerOptions": [
                        {"text": "Le nombre de succès obtenus sur n épreuves répétées", "isCorrect": True},
                        {"text": "Le temps d'attente avant d'obtenir le premier succès", "isCorrect": False},
                        {"text": "Le résultat précis obtenu lors du dernier tirage", "isCorrect": False},
                        {"text": "Le prix total de l'expérience menée par le chercheur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** X est une variable discrète qui compte les succès. Elle peut prendre n'importe quelle valeur entière comprise entre 0 (aucun succès) et n (succès à chaque coup)."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la valeur de P(X=0) si n=3 et p=0,5 ?",
                    "answerOptions": [
                        {"text": "Une valeur égale à zéro virgule cent-vingt-cinq", "isCorrect": True},
                        {"text": "Une valeur égale à zéro virgule cinq", "isCorrect": False},
                        {"text": "Une valeur nulle égale au chiffre zéro", "isCorrect": False},
                        {"text": "Une valeur égale à zéro virgule vingt-cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** P(X=0) signifie obtenir 0 succès, donc 3 échecs consécutifs. Le calcul est q * q * q = 0,5 * 0,5 * 0,5 = 0,125."
                },
                {
                    "questionNumber": 88,
                    "question": "Sur une calculatrice, quelle fonction donne P(X = k) ?",
                    "answerOptions": [
                        {"text": "La fonction binomPdf pour une valeur précise", "isCorrect": True},
                        {"text": "La fonction binomCdf pour une valeur cumulée", "isCorrect": False},
                        {"text": "La fonction NormalCdf pour la loi normale continue", "isCorrect": False},
                        {"text": "La fonction LinReg pour la droite de régression", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pdf (Probability Density Function) sert pour un point précis (ex: P(X=3)). Cdf (Cumulative Distribution Function) sert pour un intervalle (ex: P(X ≤ 3))."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la somme P(X=0) + P(X=1) + ... + P(X=n) ?",
                    "answerOptions": [
                        {"text": "La valeur entière égale à un", "isCorrect": True},
                        {"text": "La valeur n correspondant au nombre de tirages", "isCorrect": False},
                        {"text": "La probabilité de succès p de chaque épreuve", "isCorrect": False},
                        {"text": "La valeur nulle égale au chiffre zéro", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Cette somme représente la probabilité de toutes les issues possibles de la loi binomiale. Comme il est certain que l'on obtiendra entre 0 et n succès, la somme vaut 1."
                },
                {
                    "questionNumber": 90,
                    "question": "Qu'est-ce qu'un arbre pondéré en probabilités ?",
                    "answerOptions": [
                        {"text": "Un schéma représentant les issues avec leurs probabilités", "isCorrect": True},
                        {"text": "Un arbre qui pousse dans le jardin du mathématicien", "isCorrect": False},
                        {"text": "Un graphique avec des barres lourdes et épaisses", "isCorrect": False},
                        {"text": "Une liste de nombres classés par ordre décroissant", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est un outil visuel. Chaque 'branche' porte la probabilité de l'issue. Pour calculer la probabilité d'un chemin (une suite de résultats), on multiplie les probabilités rencontrées le long des branches."
                },
                {
                    "questionNumber": 91,
                    "question": "Que signifie précisément la notation P(X ≤ 2) ?",
                    "answerOptions": [
                        {"text": "La somme des probabilités P(X=0) + P(X=1) + P(X=2)", "isCorrect": True},
                        {"text": "La probabilité d'obtenir exactement deux succès", "isCorrect": False},
                        {"text": "La probabilité complémentaire de 1 - P(X=2)", "isCorrect": False},
                        {"text": "La probabilité d'obtenir au moins deux succès", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** P(X ≤ k) est une probabilité cumulée. Elle signifie 'obtenir au plus k succès'. On additionne toutes les probabilités de 0 jusqu'à k inclus."
                },
                {
                    "questionNumber": 92,
                    "question": "L'écart-type d'une loi binomiale mesure :",
                    "answerOptions": [
                        {"text": "La dispersion des résultats autour de l'espérance", "isCorrect": True},
                        {"text": "Le nombre total de tirages effectués dans la série", "isCorrect": False},
                        {"text": "La réussite totale de l'ensemble de l'expérience", "isCorrect": False},
                        {"text": "L'erreur de calcul commise par l'expérimentateur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Formule : σ = √(n * p * q). Comme en statistiques, l'écart-type mesure si les succès sont très concentrés autour de la moyenne (E) ou très étalés."
                },
                {
                    "questionNumber": 93,
                    "question": "Si n = 100 et p = 0,1, combien de succès espère-t-on en moyenne ?",
                    "answerOptions": [
                        {"text": "Un nombre moyen de dix succès", "isCorrect": True},
                        {"text": "Un nombre moyen de un seul succès", "isCorrect": False},
                        {"text": "Un nombre moyen de cinquante succès", "isCorrect": False},
                        {"text": "Un nombre moyen de cent succès", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On calcule l'espérance : E(X) = n * p = 100 * 0,1 = 10. Cela signifie que sur un grand nombre d'échantillons de taille 100, on trouvera en moyenne 10 succès par échantillon."
                },
                {
                    "questionNumber": 94,
                    "question": "La somme des branches partant d'un même nœud vaut :",
                    "answerOptions": [
                        {"text": "La valeur entière égale à un", "isCorrect": True},
                        {"text": "La valeur nulle égale à zéro", "isCorrect": False},
                        {"text": "La valeur décimale de zéro virgule cinq", "isCorrect": False},
                        {"text": "La probabilité de succès p de l'épreuve", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est la règle des nœuds. Puisqu'après un événement, il est certain qu'un des résultats suivants se produira, la somme des probabilités de toutes les branches issues d'un même point doit faire 1 (100 %)."
                },
                {
                    "questionNumber": 95,
                    "question": "Que signifie l'événement contraire de 'obtenir au moins un succès' ?",
                    "answerOptions": [
                        {"text": "L'événement correspondant à obtenir zéro succès", "isCorrect": True},
                        {"text": "L'événement correspondant à obtenir n succès", "isCorrect": False},
                        {"text": "L'événement correspondant à un échec au dernier tirage", "isCorrect": False},
                        {"text": "L'événement correspondant à ne pas participer", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le contraire de 'au moins un' (≥ 1) est 'aucun' (= 0). On utilise souvent cette astuce de calcul : P(X ≥ 1) = 1 - P(X = 0). C'est beaucoup plus rapide que d'additionner P(1)+P(2)+...P(n)."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle touche permet d'obtenir les coefficients a et b de régression ?",
                    "answerOptions": [
                        {"text": "La fonction LinReg ax plus b de la calculatrice", "isCorrect": True},
                        {"text": "La fonction Stats descriptive du menu principal", "isCorrect": False},
                        {"text": "La fonction Proba pour les calculs de lois", "isCorrect": False},
                        {"text": "La fonction Graph pour le tracé des courbes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** LinReg (Linear Regression) calcule par la méthode des moindres carrés les paramètres de la droite d'ajustement y = ax + b. Elle fournit aussi souvent le coefficient de corrélation r."
                },
                {
                    "questionNumber": 97,
                    "question": "Dans un jeu de 32, 'Tirer un Coeur' et 'Tirer un Pique' sont :",
                    "answerOptions": [
                        {"text": "Des événements incompatibles entre eux", "isCorrect": True},
                        {"text": "Des événements indépendants entre eux", "isCorrect": False},
                        {"text": "Des événements complémentaires entre eux", "isCorrect": False},
                        {"text": "Des événements rigoureusement identiques", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Ils sont incompatibles car ils n'ont aucune carte en commun (une carte ne peut pas être à la fois Cœur et Pique). Ils ne sont pas complémentaires car il existe d'autres couleurs (Trèfle et Carreau)."
                },
                {
                    "questionNumber": 98,
                    "question": "Une variable aléatoire X suit une loi binomiale si :",
                    "answerOptions": [
                        {"text": "On répète n fois une épreuve de Bernoulli indépendante", "isCorrect": True},
                        {"text": "On effectue des tirages de boules sans remise", "isCorrect": False},
                        {"text": "La probabilité de succès change à chaque tirage", "isCorrect": False},
                        {"text": "On possède une infinité d'issues possibles au test", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les trois conditions sont : 1. Une épreuve à deux issues. 2. La répétition n fois. 3. L'indépendance des épreuves (la probabilité p reste la même)."
                },
                {
                    "questionNumber": 99,
                    "question": "L'espérance mathématique E(X) correspond concrètement à :",
                    "answerOptions": [
                        {"text": "La moyenne théorique sur un grand nombre d'essais", "isCorrect": True},
                        {"text": "La valeur maximale possible lors d'un essai", "isCorrect": False},
                        {"text": "Le coût financier total de l'expérience menée", "isCorrect": False},
                        {"text": "La probabilité finale de gagner à la fin du jeu", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'espérance est le gain moyen (ou le nombre moyen de succès) que l'on obtiendrait en répétant l'expérience à l'infini. Si E(X) = 0 dans un jeu d'argent, le jeu est dit 'équitable'."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la probabilité d'obtenir au moins un succès lors de n épreuves ?",
                    "answerOptions": [
                        {"text": "La probabilité calculée par un moins P(X égale zéro)", "isCorrect": True},
                        {"text": "La probabilité calculée par P(X égale un)", "isCorrect": False},
                        {"text": "La probabilité calculée par un moins P(X égale n)", "isCorrect": False},
                        {"text": "La probabilité calculée par P(X égale zéro) seulement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une application de la règle des événements contraires. L'événement 'au moins un succès' est le contraire de 'aucun succès'. Sa probabilité se calcule donc par 1 - P(X = 0). C'est l'un des calculs les plus fréquents au Bac Pro."
                }
            ]
        }
    }
}