quiz_data = {
    "title": "Quiz Mathématiques - Niveau CAP (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : CALCULS COMMERCIAUX ET FINANCIERS (Q1 à Q20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : CALCULS COMMERCIAUX ET FINANCIERS",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est le montant de la TVA si le prix HT est de 100 € et le taux est de 20 % ?",
                    "answerOptions": [
                        {"text": "20 €", "isCorrect": True},
                        {"text": "120 €", "isCorrect": False},
                        {"text": "10 €", "isCorrect": False},
                        {"text": "5 €", "isCorrect": False}
                    ],
                    "correction": "Pour calculer le montant de la TVA, on multiplie le Prix Hors Taxe par le taux (sous forme décimale). Ici : 100 × 0,20 = 20 €."
                },
                {
                    "questionNumber": 2,
                    "question": "Comment calcule-t-on un Prix TTC à partir d'un Prix HT et d'une TVA ?",
                    "answerOptions": [
                        {"text": "On additionne le Prix HT et le montant de la TVA", "isCorrect": True},
                        {"text": "On soustrait le montant de la TVA au Prix HT", "isCorrect": False},
                        {"text": "On multiplie le Prix HT par le montant de la TVA", "isCorrect": False},
                        {"text": "On divise le Prix HT par le taux de TVA", "isCorrect": False}
                    ],
                    "correction": "Le Prix TTC (Toutes Taxes Comprises) correspond au Prix HT (Hors Taxe) auquel on ajoute le montant de la taxe."
                },
                {
                    "questionNumber": 3,
                    "question": "Si un article coûte 50 € et bénéficie d'une remise de 10 %, quel est le montant de la remise ?",
                    "answerOptions": [
                        {"text": "5 €", "isCorrect": True},
                        {"text": "45 €", "isCorrect": False},
                        {"text": "10 €", "isCorrect": False},
                        {"text": "1 €", "isCorrect": False}
                    ],
                    "correction": "Le montant de la remise se calcule ainsi : Prix initial × (Taux / 100). Soit 50 × 0,10 = 5 €."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le prix net à payer pour un article à 80 € avec une réduction de 20 € ?",
                    "answerOptions": [
                        {"text": "60 €", "isCorrect": True},
                        {"text": "100 €", "isCorrect": False},
                        {"text": "40 €", "isCorrect": False},
                        {"text": "70 €", "isCorrect": False}
                    ],
                    "correction": "Prix Net = Prix Brut - Remise. Donc 80 - 20 = 60 €."
                },
                {
                    "questionNumber": 5,
                    "question": "Comment exprime-t-on 0,75 sous forme de pourcentage ?",
                    "answerOptions": [
                        {"text": "75 %", "isCorrect": True},
                        {"text": "7,5 %", "isCorrect": False},
                        {"text": "0,75 %", "isCorrect": False},
                        {"text": "750 %", "isCorrect": False}
                    ],
                    "correction": "Pour passer d'un nombre décimal au pourcentage, on multiplie par 100."
                },
                {
                    "questionNumber": 6,
                    "question": "Si 3 stylos coûtent 6 €, combien coûtent 9 stylos (situation de proportionnalité) ?",
                    "answerOptions": [
                        {"text": "18 €", "isCorrect": True},
                        {"text": "12 €", "isCorrect": False},
                        {"text": "27 €", "isCorrect": False},
                        {"text": "9 €", "isCorrect": False}
                    ],
                    "correction": "On multiplie par 3 le nombre de stylos, donc on multiplie par 3 le prix (6 × 3 = 18)."
                },
                {
                    "questionNumber": 7,
                    "question": "Qu'est-ce que l'intérêt simple dans un placement ?",
                    "answerOptions": [
                        {"text": "La somme rapportée par le capital placé sur une période", "isCorrect": True},
                        {"text": "Le montant total rendu à la fin", "isCorrect": False},
                        {"text": "Le prix d'achat du produit", "isCorrect": False},
                        {"text": "Une taxe de l'État", "isCorrect": False}
                    ],
                    "correction": "L'intérêt est le loyer de l'argent prêté ou placé."
                },
                {
                    "questionNumber": 8,
                    "question": "Calculez 20 % de 250.",
                    "answerOptions": [
                        {"text": "50", "isCorrect": True},
                        {"text": "25", "isCorrect": False},
                        {"text": "100", "isCorrect": False},
                        {"text": "5", "isCorrect": False}
                    ],
                    "correction": "250 × 0,20 = 50."
                },
                {
                    "questionNumber": 9,
                    "question": "Un produit affiché à 120 € TTC avec une TVA à 20 € coûte combien en Hors Taxe ?",
                    "answerOptions": [
                        {"text": "100 €", "isCorrect": True},
                        {"text": "140 €", "isCorrect": False},
                        {"text": "110 €", "isCorrect": False},
                        {"text": "80 €", "isCorrect": False}
                    ],
                    "correction": "Prix HT = Prix TTC - Montant TVA. Soit 120 - 20 = 100 €."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la formule du coefficient multiplicateur pour une hausse de 5 % ?",
                    "answerOptions": [
                        {"text": "1,05", "isCorrect": True},
                        {"text": "0,05", "isCorrect": False},
                        {"text": "1,5", "isCorrect": False},
                        {"text": "5", "isCorrect": False}
                    ],
                    "correction": "Le CM d'une hausse est (1 + t/100), soit 1 + 0,05 = 1,05."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la formule du coefficient multiplicateur pour une baisse de 10 % ?",
                    "answerOptions": [
                        {"text": "0,90", "isCorrect": True},
                        {"text": "1,10", "isCorrect": False},
                        {"text": "0,10", "isCorrect": False},
                        {"text": "0,99", "isCorrect": False}
                    ],
                    "correction": "Le CM d'une baisse est (1 - t/100), soit 1 - 0,10 = 0,90."
                },
                {
                    "questionNumber": 12,
                    "question": "Si une échelle est de 1/100, combien représente 1 cm sur le plan dans la réalité ?",
                    "answerOptions": [
                        {"text": "100 cm (ou 1 m)", "isCorrect": True},
                        {"text": "10 cm", "isCorrect": False},
                        {"text": "1000 cm", "isCorrect": False},
                        {"text": "1 cm", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/100 signifie que la réalité est 100 fois plus grande que le dessin."
                },
                {
                    "questionNumber": 13,
                    "question": "Comment calcule-t-on une vitesse moyenne ?",
                    "answerOptions": [
                        {"text": "Distance / Temps", "isCorrect": True},
                        {"text": "Distance × Temps", "isCorrect": False},
                        {"text": "Temps / Distance", "isCorrect": False},
                        {"text": "Distance + Temps", "isCorrect": False}
                    ],
                    "correction": "V = d / t. C'est le rapport entre la distance parcourue et la durée du parcours."
                },
                {
                    "questionNumber": 14,
                    "question": "Convertissez 1h30 minutes en heures décimales.",
                    "answerOptions": [
                        {"text": "1,5 h", "isCorrect": True},
                        {"text": "1,3 h", "isCorrect": False},
                        {"text": "1,30 h", "isCorrect": False},
                        {"text": "2 h", "isCorrect": False}
                    ],
                    "correction": "30 minutes correspondent à la moitié d'une heure (30/60 = 0,5)."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle est la valeur de 1/4 en écriture décimale ?",
                    "answerOptions": [
                        {"text": "0,25", "isCorrect": True},
                        {"text": "0,4", "isCorrect": False},
                        {"text": "0,5", "isCorrect": False},
                        {"text": "0,75", "isCorrect": False}
                    ],
                    "correction": "1 divisé par 4 égale 0,25 (un quart)."
                },
                {
                    "questionNumber": 16,
                    "question": "Un capital de 1000 € placé à 2 % d'intérêt simple pendant un an rapporte :",
                    "answerOptions": [
                        {"text": "20 €", "isCorrect": True},
                        {"text": "2 €", "isCorrect": False},
                        {"text": "200 €", "isCorrect": False},
                        {"text": "1020 €", "isCorrect": False}
                    ],
                    "correction": "Intérêt = Capital × Taux × Durée. Soit 1000 × 0,02 × 1 = 20 €."
                },
                {
                    "questionNumber": 17,
                    "question": "Le prix HT d'un repas est de 20 €. La TVA est de 10 %. Quel est le prix TTC ?",
                    "answerOptions": [
                        {"text": "22 €", "isCorrect": True},
                        {"text": "21 €", "isCorrect": False},
                        {"text": "30 €", "isCorrect": False},
                        {"text": "18 €", "isCorrect": False}
                    ],
                    "correction": "TVA = 20 × 0,10 = 2 €. Prix TTC = 20 + 2 = 22 €."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le résultat de 4² ?",
                    "answerOptions": [
                        {"text": "16", "isCorrect": True},
                        {"text": "8", "isCorrect": False},
                        {"text": "4", "isCorrect": False},
                        {"text": "12", "isCorrect": False}
                    ],
                    "correction": "Un nombre au carré est multiplié par lui-même (4 × 4 = 16)."
                },
                {
                    "questionNumber": 19,
                    "question": "Dans un tableau de proportionnalité, comment calcule-t-on la quatrième proportionnelle ?",
                    "answerOptions": [
                        {"text": "Le produit en croix", "isCorrect": True},
                        {"text": "L'addition en croix", "isCorrect": False},
                        {"text": "La soustraction des colonnes", "isCorrect": False},
                        {"text": "En devinant", "isCorrect": False}
                    ],
                    "correction": "On multiplie les deux nombres en diagonale et on divise par le troisième."
                },
                {
                    "questionNumber": 20,
                    "question": "Que signifie le sigle HT ?",
                    "answerOptions": [
                        {"text": "Hors Taxe", "isCorrect": True},
                        {"text": "Haute Tarif", "isCorrect": False},
                        {"text": "Heures de Travail", "isCorrect": False},
                        {"text": "Habitation Terminée", "isCorrect": False}
                    ],
                    "correction": "C'est le prix du produit avant l'application des taxes gouvernementales."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : GÉOMÉTRIE ET MESURES (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : GÉOMÉTRIE ET MESURES",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la formule du périmètre d'un carré de côté 'c' ?",
                    "answerOptions": [
                        {"text": "4 × c", "isCorrect": True},
                        {"text": "c × c", "isCorrect": False},
                        {"text": "2 × c", "isCorrect": False},
                        {"text": "c + 4", "isCorrect": False}
                    ],
                    "correction": "Le périmètre est la somme des longueurs des 4 côtés égaux."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la formule de l'aire d'un rectangle ?",
                    "answerOptions": [
                        {"text": "Longueur × largeur", "isCorrect": True},
                        {"text": "Longueur + largeur", "isCorrect": False},
                        {"text": "(Longueur + largeur) × 2", "isCorrect": False},
                        {"text": "Côté × Côté", "isCorrect": False}
                    ],
                    "correction": "L'aire d'un rectangle est le produit de ses deux dimensions."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est l'unité de mesure principale d'une surface ?",
                    "answerOptions": [
                        {"text": "Le mètre carré (m²)", "isCorrect": True},
                        {"text": "Le mètre (m)", "isCorrect": False},
                        {"text": "Le mètre cube (m³)", "isCorrect": False},
                        {"text": "Le litre (L)", "isCorrect": False}
                    ],
                    "correction": "Une surface s'exprime en unités 'carré'."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment calcule-t-on le volume d'un pavé droit (parallélépipède) ?",
                    "answerOptions": [
                        {"text": "Longueur × largeur × hauteur", "isCorrect": True},
                        {"text": "Longueur + largeur + hauteur", "isCorrect": False},
                        {"text": "Aire de la base / hauteur", "isCorrect": False},
                        {"text": "Côté × 3", "isCorrect": False}
                    ],
                    "correction": "Le volume est le produit des trois dimensions."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel outil utilise-t-on pour mesurer un angle ?",
                    "answerOptions": [
                        {"text": "Un rapporteur", "isCorrect": True},
                        {"text": "Un compas", "isCorrect": False},
                        {"text": "Une règle graduée", "isCorrect": False},
                        {"text": "Une équerre", "isCorrect": False}
                    ],
                    "correction": "Le rapporteur permet de lire la mesure d'un angle en degrés."
                },
                {
                    "questionNumber": 26,
                    "question": "Combien font 180° pour un angle ?",
                    "answerOptions": [
                        {"text": "Un angle plat", "isCorrect": True},
                        {"text": "Un angle droit", "isCorrect": False},
                        {"text": "Un angle aigu", "isCorrect": False},
                        {"text": "Un cercle complet", "isCorrect": False}
                    ],
                    "correction": "Un angle droit fait 90°, un angle plat fait le double (180°)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le nom d'un triangle ayant un angle droit ?",
                    "answerOptions": [
                        {"text": "Triangle rectangle", "isCorrect": True},
                        {"text": "Triangle isocèle", "isCorrect": False},
                        {"text": "Triangle équilatéral", "isCorrect": False},
                        {"text": "Triangle quelconque", "isCorrect": False}
                    ],
                    "correction": "Un triangle rectangle possède un angle de 90°."
                },
                {
                    "questionNumber": 28,
                    "question": "Le théorème de Pythagore s'utilise dans un triangle :",
                    "answerOptions": [
                        {"text": "Rectangle", "isCorrect": True},
                        {"text": "Quelconque", "isCorrect": False},
                        {"text": "Isocèle", "isCorrect": False},
                        {"text": "Équilatéral", "isCorrect": False}
                    ],
                    "correction": "Pythagore permet de calculer la longueur d'un côté dans un triangle rectangle."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la valeur approchée du nombre Pi (π) ?",
                    "answerOptions": [
                        {"text": "3,14", "isCorrect": True},
                        {"text": "2,14", "isCorrect": False},
                        {"text": "3,41", "isCorrect": False},
                        {"text": "1,14", "isCorrect": False}
                    ],
                    "correction": "Pi est utilisé pour les calculs liés au cercle."
                },
                {
                    "questionNumber": 30,
                    "question": "Comment calcule-t-on le périmètre d'un cercle ?",
                    "answerOptions": [
                        {"text": "2 × π × Rayon", "isCorrect": True},
                        {"text": "π × Rayon²", "isCorrect": False},
                        {"text": "Rayon × Rayon", "isCorrect": False},
                        {"text": "Diamètre / π", "isCorrect": False}
                    ],
                    "correction": "C'est aussi égal à π × Diamètre."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la somme des angles d'un triangle ?",
                    "answerOptions": [
                        {"text": "180°", "isCorrect": True},
                        {"text": "90°", "isCorrect": False},
                        {"text": "360°", "isCorrect": False},
                        {"text": "100°", "isCorrect": False}
                    ],
                    "correction": "Dans n'importe quel triangle, l'addition des trois angles donne toujours 180°."
                },
                {
                    "questionNumber": 32,
                    "question": "Un triangle équilatéral possède :",
                    "answerOptions": [
                        {"text": "3 côtés égaux", "isCorrect": True},
                        {"text": "2 côtés égaux", "isCorrect": False},
                        {"text": "Un angle droit", "isCorrect": False},
                        {"text": "Aucun côté égal", "isCorrect": False}
                    ],
                    "correction": "Ses trois angles font également 60° chacun."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment s'appelle le côté le plus long d'un triangle rectangle ?",
                    "answerOptions": [
                        {"text": "L'hypoténuse", "isCorrect": True},
                        {"text": "La base", "isCorrect": False},
                        {"text": "La hauteur", "isCorrect": False},
                        {"text": "Le sommet", "isCorrect": False}
                    ],
                    "correction": "C'est le côté opposé à l'angle droit."
                },
                {
                    "questionNumber": 34,
                    "question": "Convertissez 1 mètre en millimètres.",
                    "answerOptions": [
                        {"text": "1000 mm", "isCorrect": True},
                        {"text": "100 mm", "isCorrect": False},
                        {"text": "10 mm", "isCorrect": False},
                        {"text": "10000 mm", "isCorrect": False}
                    ],
                    "correction": "1 m = 10 dm = 100 cm = 1000 mm."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est l'aire d'un carré de 5 cm de côté ?",
                    "answerOptions": [
                        {"text": "25 cm²", "isCorrect": True},
                        {"text": "20 cm²", "isCorrect": False},
                        {"text": "10 cm²", "isCorrect": False},
                        {"text": "50 cm²", "isCorrect": False}
                    ],
                    "correction": "Aire = 5 × 5 = 25 cm²."
                },
                {
                    "questionNumber": 36,
                    "question": "Un litre (1 L) d'eau correspond à quelle masse ?",
                    "answerOptions": [
                        {"text": "1 kg", "isCorrect": True},
                        {"text": "1 g", "isCorrect": False},
                        {"text": "10 kg", "isCorrect": False},
                        {"text": "0,5 kg", "isCorrect": False}
                    ],
                    "correction": "C'est une correspondance utile : 1 L d'eau pure pèse 1 kg."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment appelle-t-on un polygone à 5 côtés ?",
                    "answerOptions": [
                        {"text": "Un pentagone", "isCorrect": True},
                        {"text": "Un hexagone", "isCorrect": False},
                        {"text": "Un losange", "isCorrect": False},
                        {"text": "Un quadrilatère", "isCorrect": False}
                    ],
                    "correction": "Penta- signifie 5 en grec."
                },
                {
                    "questionNumber": 38,
                    "question": "Qu'est-ce qu'un angle droit ?",
                    "answerOptions": [
                        {"text": "Un angle de 90°", "isCorrect": True},
                        {"text": "Un angle de 45°", "isCorrect": False},
                        {"text": "Un angle de 180°", "isCorrect": False},
                        {"text": "Un angle de 0°", "isCorrect": False}
                    ],
                    "correction": "L'angle droit est formé par deux droites perpendiculaires."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le volume d'un cube de 2 cm de côté ?",
                    "answerOptions": [
                        {"text": "8 cm³", "isCorrect": True},
                        {"text": "4 cm³", "isCorrect": False},
                        {"text": "6 cm³", "isCorrect": False},
                        {"text": "12 cm³", "isCorrect": False}
                    ],
                    "correction": "Volume = 2 × 2 × 2 = 8 cm³."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la définition d'un segment ?",
                    "answerOptions": [
                        {"text": "Une portion de droite délimitée par deux points", "isCorrect": True},
                        {"text": "Une ligne qui ne s'arrête jamais", "isCorrect": False},
                        {"text": "Un cercle coupé en deux", "isCorrect": False},
                        {"text": "Un angle", "isCorrect": False}
                    ],
                    "correction": "Un segment a une longueur mesurable, contrairement à une droite."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : ALGÈBRE ET STATISTIQUES (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ALGÈBRE ET STATISTIQUES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Résolvez l'équation : x + 5 = 12. Quelle est la valeur de x ?",
                    "answerOptions": [
                        {"text": "7", "isCorrect": True},
                        {"text": "17", "isCorrect": False},
                        {"text": "5", "isCorrect": False},
                        {"text": "-7", "isCorrect": False}
                    ],
                    "correction": "x = 12 - 5 = 7."
                },
                {
                    "questionNumber": 42,
                    "question": "Comment calcule-t-on la moyenne d'une série de notes ?",
                    "answerOptions": [
                        {"text": "Somme des notes / Nombre de notes", "isCorrect": True},
                        {"text": "Note la plus haute - note la plus basse", "isCorrect": False},
                        {"text": "Note du milieu", "isCorrect": False},
                        {"text": "Somme des notes × 2", "isCorrect": False}
                    ],
                    "correction": "La moyenne est la valeur unique que chacun aurait si on partageait tout équitablement."
                },
                {
                    "questionNumber": 43,
                    "question": "Dans une série statistique, qu'est-ce que l'étendue ?",
                    "answerOptions": [
                        {"text": "Différence entre la plus grande et la plus petite valeur", "isCorrect": True},
                        {"text": "La valeur moyenne", "isCorrect": False},
                        {"text": "Le nombre total de données", "isCorrect": False},
                        {"text": "La valeur la plus fréquente", "isCorrect": False}
                    ],
                    "correction": "Elle mesure la dispersion des données."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la valeur de x si 2x = 10 ?",
                    "answerOptions": [
                        {"text": "5", "isCorrect": True},
                        {"text": "20", "isCorrect": False},
                        {"text": "8", "isCorrect": False},
                        {"text": "12", "isCorrect": False}
                    ],
                    "correction": "x = 10 / 2 = 5."
                },
                {
                    "questionNumber": 45,
                    "question": "Qu'est-ce qu'un effectif en statistique ?",
                    "answerOptions": [
                        {"text": "Le nombre de fois qu'une donnée apparaît", "isCorrect": True},
                        {"text": "Le résultat d'un calcul de pourcentage", "isCorrect": False},
                        {"text": "Le nom du graphique", "isCorrect": False},
                        {"text": "La somme de toutes les données", "isCorrect": False}
                    ],
                    "correction": "L'effectif total est la somme de tous les effectifs individuels."
                },
                {
                    "questionNumber": 46,
                    "question": "Que représente la fréquence en statistique ?",
                    "answerOptions": [
                        {"text": "Effectif / Effectif total", "isCorrect": True},
                        {"text": "Effectif total / Effectif", "isCorrect": False},
                        {"text": "Effectif × 100", "isCorrect": False},
                        {"text": "La valeur moyenne", "isCorrect": False}
                    ],
                    "correction": "C'est la part (souvent en %) que représente une catégorie dans le total."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment s'appelle l'axe horizontal dans un repère ?",
                    "answerOptions": [
                        {"text": "L'axe des abscisses", "isCorrect": True},
                        {"text": "L'axe des ordonnées", "isCorrect": False},
                        {"text": "L'axe des altitudes", "isCorrect": False},
                        {"text": "La droite numérique", "isCorrect": False}
                    ],
                    "correction": "L'axe des ordonnées est l'axe vertical."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelles sont les coordonnées de l'origine d'un repère ?",
                    "answerOptions": [
                        {"text": "(0 ; 0)", "isCorrect": True},
                        {"text": "(1 ; 1)", "isCorrect": False},
                        {"text": "(0 ; 1)", "isCorrect": False},
                        {"text": "(1 ; 0)", "isCorrect": False}
                    ],
                    "correction": "C'est le point d'intersection des deux axes."
                },
                {
                    "questionNumber": 49,
                    "question": "Une fonction linéaire est représentée par :",
                    "answerOptions": [
                        {"text": "Une droite passant par l'origine", "isCorrect": True},
                        {"text": "Un cercle", "isCorrect": False},
                        {"text": "Une courbe quelconque", "isCorrect": False},
                        {"text": "Une droite ne passant pas par l'origine", "isCorrect": False}
                    ],
                    "correction": "Elle traduit une situation de proportionnalité."
                },
                {
                    "questionNumber": 50,
                    "question": "Calculer la moyenne de 10, 12 et 14.",
                    "answerOptions": [
                        {"text": "12", "isCorrect": True},
                        {"text": "10", "isCorrect": False},
                        {"text": "36", "isCorrect": False},
                        {"text": "11", "isCorrect": False}
                    ],
                    "correction": "(10 + 12 + 14) / 3 = 36 / 3 = 12."
                },
                {
                    "questionNumber": 51,
                    "question": "Si un graphique est un diagramme circulaire, la somme des pourcentages doit être :",
                    "answerOptions": [
                        {"text": "100 %", "isCorrect": True},
                        {"text": "360 %", "isCorrect": False},
                        {"text": "50 %", "isCorrect": False},
                        {"text": "0 %", "isCorrect": False}
                    ],
                    "correction": "Le cercle complet représente la totalité de l'échantillon."
                },
                {
                    "questionNumber": 52,
                    "question": "Que signifie f(x) = 3x ?",
                    "answerOptions": [
                        {"text": "On multiplie chaque nombre x par 3", "isCorrect": True},
                        {"text": "On ajoute 3 à chaque nombre x", "isCorrect": False},
                        {"text": "On divise x par 3", "isCorrect": False},
                        {"text": "x vaut toujours 3", "isCorrect": False}
                    ],
                    "correction": "C'est l'expression d'une fonction linéaire."
                },
                {
                    "questionNumber": 53,
                    "question": "Dans l'expression 5x + 2, quel est le terme constant ?",
                    "answerOptions": [
                        {"text": "2", "isCorrect": True},
                        {"text": "5", "isCorrect": False},
                        {"text": "x", "isCorrect": False},
                        {"text": "5x", "isCorrect": False}
                    ],
                    "correction": "Le terme constant ne change pas, contrairement au terme contenant x."
                },
                {
                    "questionNumber": 54,
                    "question": "Calculer l'étendue de la série : 5 ; 12 ; 3 ; 18 ; 10.",
                    "answerOptions": [
                        {"text": "15", "isCorrect": True},
                        {"text": "18", "isCorrect": False},
                        {"text": "3", "isCorrect": False},
                        {"text": "12", "isCorrect": False}
                    ],
                    "correction": "Étendue = 18 (max) - 3 (min) = 15."
                },
                {
                    "questionNumber": 55,
                    "question": "Si x = 3, quelle est la valeur de 2x + 4 ?",
                    "answerOptions": [
                        {"text": "10", "isCorrect": True},
                        {"text": "9", "isCorrect": False},
                        {"text": "7", "isCorrect": False},
                        {"text": "12", "isCorrect": False}
                    ],
                    "correction": "2 × 3 + 4 = 6 + 4 = 10."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel graphique utilise des bâtons pour représenter des effectifs ?",
                    "answerOptions": [
                        {"text": "L'histogramme ou diagramme en bâtons", "isCorrect": True},
                        {"text": "Le diagramme circulaire", "isCorrect": False},
                        {"text": "La courbe", "isCorrect": False},
                        {"text": "La photo", "isCorrect": False}
                    ],
                    "correction": "La hauteur du bâton est proportionnelle à l'effectif."
                },
                {
                    "questionNumber": 57,
                    "question": "Que signifie x² ?",
                    "answerOptions": [
                        {"text": "x multiplié par x", "isCorrect": True},
                        {"text": "x multiplié par 2", "isCorrect": False},
                        {"text": "x plus x", "isCorrect": False},
                        {"text": "2 divisé par x", "isCorrect": False}
                    ],
                    "correction": "C'est la puissance 2."
                },
                {
                    "questionNumber": 58,
                    "question": "Résolvez 3x = 15.",
                    "answerOptions": [
                        {"text": "5", "isCorrect": True},
                        {"text": "12", "isCorrect": False},
                        {"text": "18", "isCorrect": False},
                        {"text": "3", "isCorrect": False}
                    ],
                    "correction": "x = 15 / 3 = 5."
                },
                {
                    "questionNumber": 59,
                    "question": "Une probabilité est toujours comprise entre :",
                    "answerOptions": [
                        {"text": "0 et 1", "isCorrect": True},
                        {"text": "1 et 100", "isCorrect": False},
                        {"text": "-1 et 1", "isCorrect": False},
                        {"text": "0 et 100", "isCorrect": True}
                    ],
                    "correction": "En mathématiques, P est entre 0 (impossible) et 1 (certain). En langage courant on utilise souvent 0 à 100%."
                },
                {
                    "questionNumber": 60,
                    "question": "Le mode d'une série statistique est :",
                    "answerOptions": [
                        {"text": "La valeur qui a le plus grand effectif", "isCorrect": True},
                        {"text": "La moyenne", "isCorrect": False},
                        {"text": "L'étendue", "isCorrect": False},
                        {"text": "La valeur la plus petite", "isCorrect": False}
                    ],
                    "correction": "C'est la donnée qui apparaît le plus souvent."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : NUMÉRATION ET CALCUL NUMÉRIQUE (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : NUMÉRATION ET CALCUL NUMÉRIQUE",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Combien font 12,5 × 100 ?",
                    "answerOptions": [
                        {"text": "1250", "isCorrect": True},
                        {"text": "125", "isCorrect": False},
                        {"text": "12500", "isCorrect": False},
                        {"text": "1,25", "isCorrect": False}
                    ],
                    "correction": "On décale la virgule de deux rangs vers la droite."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le résultat de (-5) + (-3) ?",
                    "answerOptions": [
                        {"text": "-8", "isCorrect": True},
                        {"text": "-2", "isCorrect": False},
                        {"text": "8", "isCorrect": False},
                        {"text": "15", "isCorrect": False}
                    ],
                    "correction": "On additionne deux nombres négatifs, le résultat est plus négatif."
                },
                {
                    "questionNumber": 63,
                    "question": "Combien font 1/2 + 1/2 ?",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "2/4", "isCorrect": False},
                        {"text": "1/4", "isCorrect": False},
                        {"text": "2", "isCorrect": False}
                    ],
                    "correction": "Deux moitiés font un tout."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la racine carrée de 25 ?",
                    "answerOptions": [
                        {"text": "5", "isCorrect": True},
                        {"text": "12,5", "isCorrect": False},
                        {"text": "50", "isCorrect": False},
                        {"text": "2,5", "isCorrect": False}
                    ],
                    "correction": "Car 5 × 5 = 25."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le résultat de 10 / 0,1 ?",
                    "answerOptions": [
                        {"text": "100", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "0", "isCorrect": False},
                        {"text": "10", "isCorrect": False}
                    ],
                    "correction": "Diviser par 0,1 revient à multiplier par 10."
                },
                {
                    "questionNumber": 66,
                    "question": "Combien font 3 × (4 + 2) ?",
                    "answerOptions": [
                        {"text": "18", "isCorrect": True},
                        {"text": "14", "isCorrect": False},
                        {"text": "20", "isCorrect": False},
                        {"text": "12", "isCorrect": False}
                    ],
                    "correction": "On calcule d'abord entre parenthèses : 3 × 6 = 18."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le nombre le plus grand ?",
                    "answerOptions": [
                        {"text": "0,12", "isCorrect": True},
                        {"text": "0,099", "isCorrect": False},
                        {"text": "0,1", "isCorrect": False},
                        {"text": "0,0125", "isCorrect": False}
                    ],
                    "correction": "On compare chiffre par chiffre après la virgule."
                },
                {
                    "questionNumber": 68,
                    "question": "Écriture scientifique de 5000 :",
                    "answerOptions": [
                        {"text": "5 × 10³", "isCorrect": True},
                        {"text": "50 × 10²", "isCorrect": False},
                        {"text": "0,5 × 10⁴", "isCorrect": False},
                        {"text": "5 × 10²", "isCorrect": False}
                    ],
                    "correction": "Un seul chiffre (non nul) avant la virgule."
                },
                {
                    "questionNumber": 69,
                    "question": "Combien font 7 × 8 ?",
                    "answerOptions": [
                        {"text": "56", "isCorrect": True},
                        {"text": "49", "isCorrect": False},
                        {"text": "64", "isCorrect": False},
                        {"text": "54", "isCorrect": False}
                    ],
                    "correction": "Table de multiplication de 7 et 8."
                },
                {
                    "questionNumber": 70,
                    "question": "Que vaut 10 puissance 0 (10⁰) ?",
                    "answerOptions": [
                        {"text": "1", "isCorrect": True},
                        {"text": "0", "isCorrect": False},
                        {"text": "10", "isCorrect": False},
                        {"text": "0,1", "isCorrect": False}
                    ],
                    "correction": "Tout nombre (sauf 0) à la puissance 0 vaut 1."
                },
                {
                    "questionNumber": 71,
                    "question": "Résultat de 1/2 × 1/2 ?",
                    "answerOptions": [
                        {"text": "1/4 (ou 0,25)", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "2/4", "isCorrect": False},
                        {"text": "1/2", "isCorrect": False}
                    ],
                    "correction": "On multiplie les numérateurs entre eux et les dénominateurs entre eux."
                },
                {
                    "questionNumber": 72,
                    "question": "Simplifier 10/20 :",
                    "answerOptions": [
                        {"text": "1/2", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "0,2", "isCorrect": False},
                        {"text": "1/10", "isCorrect": False}
                    ],
                    "correction": "On divise par 10 en haut et en bas."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est l'inverse de 2 ?",
                    "answerOptions": [
                        {"text": "1/2 (ou 0,5)", "isCorrect": True},
                        {"text": "-2", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "0,2", "isCorrect": False}
                    ],
                    "correction": "L'inverse d'un nombre x est 1/x."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est l'opposé de 5 ?",
                    "answerOptions": [
                        {"text": "-5", "isCorrect": True},
                        {"text": "1/5", "isCorrect": False},
                        {"text": "0", "isCorrect": False},
                        {"text": "5", "isCorrect": False}
                    ],
                    "correction": "L'opposé change le signe du nombre."
                },
                {
                    "questionNumber": 75,
                    "question": "Combien font 1/3 de 90 ?",
                    "answerOptions": [
                        {"text": "30", "isCorrect": True},
                        {"text": "60", "isCorrect": False},
                        {"text": "10", "isCorrect": False},
                        {"text": "270", "isCorrect": False}
                    ],
                    "correction": "On divise 90 par 3."
                },
                {
                    "questionNumber": 76,
                    "question": "Le résultat de 10 + 5 × 2 est :",
                    "answerOptions": [
                        {"text": "20", "isCorrect": True},
                        {"text": "30", "isCorrect": False},
                        {"text": "17", "isCorrect": False},
                        {"text": "25", "isCorrect": False}
                    ],
                    "correction": "La multiplication est prioritaire sur l'addition."
                },
                {
                    "questionNumber": 77,
                    "question": "Un angle obtus est un angle :",
                    "answerOptions": [
                        {"text": "Supérieur à 90° et inférieur à 180°", "isCorrect": True},
                        {"text": "Inférieur à 90°", "isCorrect": False},
                        {"text": "Égal à 90°", "isCorrect": False},
                        {"text": "Égal à 180°", "isCorrect": False}
                    ],
                    "correction": "L'angle aigu est plus petit que 90°."
                },
                {
                    "questionNumber": 78,
                    "question": "Combien de minutes y a-t-il dans 2,5 heures ?",
                    "answerOptions": [
                        {"text": "150 minutes", "isCorrect": True},
                        {"text": "120 minutes", "isCorrect": False},
                        {"text": "250 minutes", "isCorrect": False},
                        {"text": "130 minutes", "isCorrect": False}
                    ],
                    "correction": "2h = 120 min et 0,5h = 30 min. Total = 150 min."
                },
                {
                    "questionNumber": 79,
                    "question": "Si un produit coûte 10 € HT et que la TVA est de 20 %, quel est le prix TTC ?",
                    "answerOptions": [
                        {"text": "12 €", "isCorrect": True},
                        {"text": "10,20 €", "isCorrect": False},
                        {"text": "30 €", "isCorrect": False},
                        {"text": "8 €", "isCorrect": False}
                    ],
                    "correction": "10 × 1,20 = 12 €."
                },
                {
                    "questionNumber": 100,
                    "question": "La perspective cavalière sert à :",
                    "answerOptions": [
                        {"text": "Représenter un objet en 3D sur une feuille plate", "isCorrect": True},
                        {"text": "Calculer la météo", "isCorrect": False},
                        {"text": "Mesurer le poids des objets", "isCorrect": False},
                        {"text": "Écrire des chiffres romains", "isCorrect": False}
                    ],
                    "correction": "C'est une technique de dessin technique."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : PROPRIÉTÉS ET CONVERSIONS (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : PROPRIÉTÉS ET CONVERSIONS",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Un triangle isocèle possède :",
                    "answerOptions": [
                        {"text": "2 côtés égaux", "isCorrect": True},
                        {"text": "3 côtés égaux", "isCorrect": False},
                        {"text": "Aucun côté égal", "isCorrect": False},
                        {"text": "Un angle de 90°", "isCorrect": False}
                    ],
                    "correction": "Il a aussi deux angles égaux à la base."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est l'unité de mesure du volume d'un liquide ?",
                    "answerOptions": [
                        {"text": "Le litre", "isCorrect": True},
                        {"text": "Le gramme", "isCorrect": False},
                        {"text": "Le mètre carré", "isCorrect": False},
                        {"text": "Le degré", "isCorrect": False}
                    ],
                    "correction": "Le litre est l'unité usuelle, le mètre cube est l'unité internationale."
                },
                {
                    "questionNumber": 83,
                    "question": "Combien de grammes y a-t-il dans 1,2 kg ?",
                    "answerOptions": [
                        {"text": "1200 g", "isCorrect": True},
                        {"text": "120 g", "isCorrect": False},
                        {"text": "12 g", "isCorrect": False},
                        {"text": "12000 g", "isCorrect": False}
                    ],
                    "correction": "On multiplie par 1000."
                },
                {
                    "questionNumber": 84,
                    "question": "Une journée de 24 heures contient combien de minutes ?",
                    "answerOptions": [
                        {"text": "1440 minutes", "isCorrect": True},
                        {"text": "1200 minutes", "isCorrect": False},
                        {"text": "3600 minutes", "isCorrect": False},
                        {"text": "60 minutes", "isCorrect": False}
                    ],
                    "correction": "24 × 60 = 1440."
                },
                {
                    "questionNumber": 85,
                    "question": "Que vaut l'angle droit en degrés ?",
                    "answerOptions": [
                        {"text": "90°", "isCorrect": True},
                        {"text": "180°", "isCorrect": False},
                        {"text": "45°", "isCorrect": False},
                        {"text": "360°", "isCorrect": False}
                    ],
                    "correction": "C'est l'angle du coin d'une feuille de papier."
                },
                {
                    "questionNumber": 86,
                    "question": "Le périmètre d'un rectangle de 10 cm sur 5 cm est :",
                    "answerOptions": [
                        {"text": "30 cm", "isCorrect": True},
                        {"text": "50 cm", "isCorrect": False},
                        {"text": "15 cm", "isCorrect": False},
                        {"text": "25 cm", "isCorrect": False}
                    ],
                    "correction": "(10 + 5) × 2 = 30 cm."
                },
                {
                    "questionNumber": 87,
                    "question": "Un angle aigu est :",
                    "answerOptions": [
                        {"text": "Plus petit que 90°", "isCorrect": True},
                        {"text": "Plus grand que 90°", "isCorrect": False},
                        {"text": "Égal à 90°", "isCorrect": False},
                        {"text": "Égal à 180°", "isCorrect": False}
                    ],
                    "correction": "Comme l'angle d'un triangle équilatéral (60°)."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est la moitié de 0,5 ?",
                    "answerOptions": [
                        {"text": "0,25", "isCorrect": True},
                        {"text": "0,10", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "0,2", "isCorrect": False}
                    ],
                    "correction": "0,5 / 2 = 0,25."
                },
                {
                    "questionNumber": 89,
                    "question": "Combien de centimètres y a-t-il dans un mètre ?",
                    "answerOptions": [
                        {"text": "100", "isCorrect": True},
                        {"text": "10", "isCorrect": False},
                        {"text": "1000", "isCorrect": False},
                        {"text": "1", "isCorrect": False}
                    ],
                    "correction": "Cent- signifie 100."
                },
                {
                    "questionNumber": 90,
                    "question": "Comment calcule-t-on l'aire d'un disque ?",
                    "answerOptions": [
                        {"text": "π × Rayon × Rayon", "isCorrect": True},
                        {"text": "2 × π × Rayon", "isCorrect": False},
                        {"text": "Diamètre × π", "isCorrect": False},
                        {"text": "Rayon × 2", "isCorrect": False}
                    ],
                    "correction": "Aussi écrit π × R²."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le périmètre d'un triangle dont les côtés mesurent 3, 4 et 5 cm ?",
                    "answerOptions": [
                        {"text": "12 cm", "isCorrect": True},
                        {"text": "6 cm", "isCorrect": False},
                        {"text": "60 cm", "isCorrect": False},
                        {"text": "7 cm", "isCorrect": False}
                    ],
                    "correction": "3 + 4 + 5 = 12."
                },
                {
                    "questionNumber": 92,
                    "question": "Convertir 50 cl en litres.",
                    "answerOptions": [
                        {"text": "0,5 L", "isCorrect": True},
                        {"text": "5 L", "isCorrect": False},
                        {"text": "500 L", "isCorrect": False},
                        {"text": "0,05 L", "isCorrect": False}
                    ],
                    "correction": "Il y a 100 cl dans 1 L."
                },
                {
                    "questionNumber": 93,
                    "question": "Quelle est la valeur de 10³ ?",
                    "answerOptions": [
                        {"text": "1000", "isCorrect": True},
                        {"text": "30", "isCorrect": False},
                        {"text": "100", "isCorrect": False},
                        {"text": "300", "isCorrect": False}
                    ],
                    "correction": "10 × 10 × 10 = 1000."
                },
                {
                    "questionNumber": 94,
                    "question": "Un quadrilatère ayant 4 côtés égaux et 4 angles droits est :",
                    "answerOptions": [
                        {"text": "Un carré", "isCorrect": True},
                        {"text": "Un rectangle", "isCorrect": False},
                        {"text": "Un losange", "isCorrect": False},
                        {"text": "Un trapèze", "isCorrect": False}
                    ],
                    "correction": "Le carré est un cas particulier de rectangle et de losange."
                },
                {
                    "questionNumber": 95,
                    "question": "Combien de secondes y a-t-il dans une minute ?",
                    "answerOptions": [
                        {"text": "60", "isCorrect": True},
                        {"text": "100", "isCorrect": False},
                        {"text": "3600", "isCorrect": False},
                        {"text": "10", "isCorrect": False}
                    ],
                    "correction": "Le temps utilise la base 60."
                },
                {
                    "questionNumber": 96,
                    "question": "Le périmètre latéral d'un cylindre se calcule en multipliant la hauteur par :",
                    "answerOptions": [
                        {"text": "Le périmètre de la base", "isCorrect": True},
                        {"text": "Le rayon", "isCorrect": False},
                        {"text": "Le diamètre", "isCorrect": False},
                        {"text": "La largeur", "isCorrect": False}
                    ],
                    "correction": "Si on déroule le cylindre, on obtient un rectangle."
                },
                {
                    "questionNumber": 97,
                    "question": "1 décimètre cube (dm³) est exactement égal à :",
                    "answerOptions": [
                        {"text": "1 litre", "isCorrect": True},
                        {"text": "10 litres", "isCorrect": False},
                        {"text": "100 litres", "isCorrect": False},
                        {"text": "0,1 litre", "isCorrect": False}
                    ],
                    "correction": "C'est la conversion fondamentale à connaître : 1 L = 1 dm³."
                },
                {
                    "questionNumber": 98,
                    "question": "Le nombre de sommets d'un cube est :",
                    "answerOptions": [
                        {"text": "8", "isCorrect": True},
                        {"text": "6", "isCorrect": False},
                        {"text": "12", "isCorrect": False},
                        {"text": "4", "isCorrect": False}
                    ],
                    "correction": "Un cube a 8 coins (sommets)."
                },
                {
                    "questionNumber": 99,
                    "question": "Pour additionner deux durées, on doit parfois :",
                    "answerOptions": [
                        {"text": "Convertir les minutes en heures si elles dépassent 60", "isCorrect": True},
                        {"text": "Convertir systématiquement en secondes", "isCorrect": False},
                        {"text": "Multiplier les heures entre elles", "isCorrect": False},
                        {"text": "Simplifier le calcul final", "isCorrect": False}
                    ],
                    "correction": "Dès qu'on atteint 60 minutes, on ajoute 1 heure."
                }
            ]
        }
    }
}