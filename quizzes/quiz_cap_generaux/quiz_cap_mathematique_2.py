quiz_data = {
    "title": "Quiz Mathématiques - Niveau CAP - Série 2 (100 Questions) - Version Optimisée",
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
                    "correction": "**Rappel de cours :** L'échelle est le rapport entre la mesure sur le plan et la mesure réelle. Une échelle de 1/50 signifie que l'on a divisé les dimensions réelles par 50 pour dessiner. Pour retrouver la taille réelle, on multiplie la mesure lue sur le plan par 50."
                },
                {
                    "questionNumber": 2,
                    "question": "Pour partager une somme de 120 € entre deux personnes selon un ratio de 2 pour 1, quelles sont les parts ?",
                    "answerOptions": [
                        {"text": "Les parts sont de quatre-vingts euros et quarante euros", "isCorrect": True},
                        {"text": "Les parts sont de soixante euros et soixante euros", "isCorrect": False},
                        {"text": "Les parts sont de cent euros et vingt euros", "isCorrect": False},
                        {"text": "Les parts sont de quatre-vingt-dix euros et trente euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Ratio 2:1 signifie qu'il y a 2 + 1 = 3 parts égales au total. Valeur d'une part : 120 / 3 = 40 €. La première personne reçoit 2 parts (2 x 40 = 80 €) et la seconde 1 part (40 €)."
                },
                {
                    "questionNumber": 3,
                    "question": "Un véhicule roule à une vitesse constante de 80 km/h. Quelle distance parcourt-il en 1h30 ?",
                    "answerOptions": [
                        {"text": "Une distance totale de cent vingt kilomètres", "isCorrect": True},
                        {"text": "Une distance totale de quatre-vingts kilomètres", "isCorrect": False},
                        {"text": "Une distance totale de cent soixante kilomètres", "isCorrect": False},
                        {"text": "Une distance totale de cent kilomètres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Formule de la distance : d = v x t. Ici, t = 1,5 heure (car 30 min = 0,5 h). Calcul : 80 km/h x 1,5 h = 120 km. Attention à toujours convertir les minutes en heures décimales."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment calcule-t-on le coefficient de proportionnalité dans un tableau ?",
                    "answerOptions": [
                        {"text": "On divise un nombre de la deuxième ligne par celui de la première", "isCorrect": True},
                        {"text": "On soustrait le nombre du haut au nombre du bas", "isCorrect": False},
                        {"text": "On multiplie les deux nombres d'une même colonne entre eux", "isCorrect": False},
                        {"text": "On fait la moyenne de tous les nombres du tableau complet", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le coefficient de proportionnalité (k) est le nombre par lequel on multiplie les valeurs de la ligne 1 pour obtenir celles de la ligne 2. Formule : k = Valeur 2 / Valeur 1."
                },
                {
                    "questionNumber": 5,
                    "question": "Si 4 kg de pommes coûtent 6 €, quel est le prix pour 10 kg de ces mêmes pommes ?",
                    "answerOptions": [
                        {"text": "Le prix total sera de quinze euros", "isCorrect": True},
                        {"text": "Le prix total sera de douze euros", "isCorrect": False},
                        {"text": "Le prix total sera de vingt euros", "isCorrect": False},
                        {"text": "Le prix total sera de dix-huit euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On utilise la règle de trois ou le passage par l'unité. Prix d'un kg : 6 / 4 = 1,50 €. Prix pour 10 kg : 1,50 x 10 = 15 €. Les grandeurs poids et prix sont ici proportionnelles."
                },
                {
                    "questionNumber": 6,
                    "question": "Un article coûte 200 € HT. On applique une remise de 15 %. Quel est le nouveau prix HT ?",
                    "answerOptions": [
                        {"text": "Le prix après remise est de cent soixante-dix euros", "isCorrect": True},
                        {"text": "Le prix après remise est de cent quatre-vingt-cinq euros", "isCorrect": False},
                        {"text": "Le prix après remise est de trente euros seulement", "isCorrect": False},
                        {"text": "Le prix après remise est de deux cent quinze euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Montant de la remise : 200 x 0,15 = 30 €. Nouveau prix : 200 - 30 = 170 €. On peut aussi multiplier directement par 0,85 (1 - 0,15)."
                },
                {
                    "questionNumber": 7,
                    "question": "Dans une classe de 25 élèves, 12 sont des filles. Quel est le pourcentage de filles ?",
                    "answerOptions": [
                        {"text": "Le pourcentage de filles est de quarante-huit pour cent", "isCorrect": True},
                        {"text": "Le pourcentage de filles est de cinquante pour cent", "isCorrect": False},
                        {"text": "Le pourcentage de filles est de douze pour cent", "isCorrect": False},
                        {"text": "Le pourcentage de filles est de quarante pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour calculer un pourcentage, on fait : (Nombre concerné / Nombre total) x 100. Calcul : (12 / 25) x 100 = 0,48 x 100 = 48 %."
                },
                {
                    "questionNumber": 8,
                    "question": "Que vaut l'échelle 1:1 en dessin technique ?",
                    "answerOptions": [
                        {"text": "L'objet est dessiné à sa taille réelle", "isCorrect": True},
                        {"text": "L'objet est dessiné une fois plus petit", "isCorrect": False},
                        {"text": "L'objet est agrandi de dix pour cent", "isCorrect": False},
                        {"text": "L'objet n'est pas représenté sur le papier", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'échelle 1:1 signifie que 1 cm sur le papier représente 1 cm dans la réalité. C'est ce qu'on appelle la 'vraie grandeur'."
                },
                {
                    "questionNumber": 9,
                    "question": "Sur une carte au 1:25 000, quelle distance réelle représente un segment de 4 cm ?",
                    "answerOptions": [
                        {"text": "Une distance réelle d'un kilomètre", "isCorrect": True},
                        {"text": "Une distance réelle de cent mètres", "isCorrect": False},
                        {"text": "Une distance réelle de vingt-cinq kilomètres", "isCorrect": False},
                        {"text": "Une distance réelle de quatre kilomètres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Distance réelle = mesure plan x dénominateur échelle. Calcul : 4 cm x 25 000 = 100 000 cm. On convertit : 100 000 cm = 1 000 m = 1 km."
                },
                {
                    "questionNumber": 10,
                    "question": "Un mélange contient 2 litres de jus pour 3 litres d'eau. Quelle est la proportion de jus ?",
                    "answerOptions": [
                        {"text": "Deux cinquièmes du mélange total", "isCorrect": True},
                        {"text": "Deux tiers du mélange total", "isCorrect": False},
                        {"text": "Trois cinquièmes du mélange total", "isCorrect": False},
                        {"text": "La moitié exacte du mélange total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le volume total du mélange est de 2 + 3 = 5 litres. Le jus représente donc 2 litres sur les 5 du total, soit la fraction 2/5 (ou 40 %)."
                },
                {
                    "questionNumber": 11,
                    "question": "Si x et y sont proportionnels et que x=2 donne y=10, quelle est la valeur de y pour x=5 ?",
                    "answerOptions": [
                        {"text": "La valeur de y est de vingt-cinq", "isCorrect": True},
                        {"text": "La valeur de y est de quinze", "isCorrect": False},
                        {"text": "La valeur de y est de vingt", "isCorrect": False},
                        {"text": "La valeur de y est de cinquante", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Coefficient de proportionnalité : 10 / 2 = 5. Pour x = 5, on multiplie par le coefficient : y = 5 x 5 = 25."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est l'inverse d'une augmentation de 100 % ?",
                    "answerOptions": [
                        {"text": "Une diminution de cinquante pour cent", "isCorrect": True},
                        {"text": "Une diminution de cent pour cent", "isCorrect": False},
                        {"text": "Une diminution de zéro pour cent", "isCorrect": False},
                        {"text": "Le retour au prix initial sans changement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Augmenter de 100 % revient à doubler la valeur (x 2). Pour revenir à la valeur de départ, il faut diviser par 2, ce qui correspond à une baisse de 50 %."
                },
                {
                    "questionNumber": 13,
                    "question": "Un ouvrier met 4 heures pour fabriquer 20 pièces. Combien en fabrique-t-il en 7 heures ?",
                    "answerOptions": [
                        {"text": "Il fabrique trente-cinq pièces", "isCorrect": True},
                        {"text": "Il fabrique quarante pièces", "isCorrect": False},
                        {"text": "Il fabrique vingt-sept pièces", "isCorrect": False},
                        {"text": "Il fabrique trente pièces", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Rendement horaire : 20 / 4 = 5 pièces par heure. Production pour 7 heures : 5 x 7 = 35 pièces."
                },
                {
                    "questionNumber": 14,
                    "question": "Comment s'écrit le ratio 3:4 sous forme de pourcentage ?",
                    "answerOptions": [
                        {"text": "Soixante-quinze pour cent", "isCorrect": True},
                        {"text": "Trente-quatre pour cent", "isCorrect": False},
                        {"text": "Quarante-trois pour cent", "isCorrect": False},
                        {"text": "Quatre-vingts pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un ratio 3:4 peut se voir comme la fraction 3/4. En effectuant la division 3 / 4, on obtient 0,75, soit 75 %."
                },
                {
                    "questionNumber": 15,
                    "question": "Si une échelle est de 5:1, cela signifie que :",
                    "answerOptions": [
                        {"text": "Le dessin est cinq fois plus grand que l'objet", "isCorrect": True},
                        {"text": "Le dessin est cinq fois plus petit que l'objet", "isCorrect": False},
                        {"text": "Le dessin mesure cinq centimètres de long", "isCorrect": False},
                        {"text": "L'objet réel a été divisé par cinq pour le dessin", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une échelle d'agrandissement. Elle est utilisée pour dessiner de très petits objets (horlogerie, micro-électronique). 1 cm réel est représenté par 5 cm sur le papier."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la vitesse moyenne d'un coureur qui fait 10 km en 30 minutes ?",
                    "answerOptions": [
                        {"text": "Vingt kilomètres par heure", "isCorrect": True},
                        {"text": "Dix kilomètres par heure", "isCorrect": False},
                        {"text": "Trente kilomètres par heure", "isCorrect": False},
                        {"text": "Cinq kilomètres par heure", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 30 minutes correspondent à 0,5 heure. Vitesse = Distance / Temps = 10 / 0,5 = 20 km/h."
                },
                {
                    "questionNumber": 17,
                    "question": "Dans un tableau, si on multiplie les nombres d'une ligne par 0,5, on effectue :",
                    "answerOptions": [
                        {"text": "Une division par deux des valeurs", "isCorrect": True},
                        {"text": "Une augmentation de cinquante pour cent", "isCorrect": False},
                        {"text": "Une multiplication par cinq des valeurs", "isCorrect": False},
                        {"text": "Une réduction de cinq pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Multiplier par 0,5 (soit 1/2) revient mathématiquement à diviser par 2. C'est utile pour calculer rapidement des moitiés."
                },
                {
                    "questionNumber": 18,
                    "question": "Si un litre de peinture couvre 12 m², combien de litres faut-il pour 48 m² ?",
                    "answerOptions": [
                        {"text": "Il faut quatre litres de peinture", "isCorrect": True},
                        {"text": "Il faut trois litres de peinture", "isCorrect": False},
                        {"text": "Il faut six litres de peinture", "isCorrect": False},
                        {"text": "Il faut douze litres de peinture", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On cherche le coefficient multiplicateur entre les surfaces : 48 / 12 = 4. Il faut donc 4 fois plus de peinture. Calcul : 1 x 4 = 4 litres."
                },
                {
                    "questionNumber": 19,
                    "question": "Comment calcule-t-on la valeur d'une remise de 20 % ?",
                    "answerOptions": [
                        {"text": "On multiplie le prix par zéro virgule deux", "isCorrect": True},
                        {"text": "On multiplie le prix par vingt", "isCorrect": False},
                        {"text": "On divise le prix par vingt", "isCorrect": False},
                        {"text": "On soustrait vingt euros au prix", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 20 % = 20/100 = 0,2. Multiplier un montant par 0,2 permet d'obtenir directement le montant de la réduction à appliquer."
                },
                {
                    "questionNumber": 20,
                    "question": "Un plan à l'échelle 1/100 possède une longueur de 10 cm. Quelle est la taille réelle ?",
                    "answerOptions": [
                        {"text": "La taille réelle est de dix mètres", "isCorrect": True},
                        {"text": "La taille réelle est d'un mètre", "isCorrect": False},
                        {"text": "La taille réelle est de cent mètres", "isCorrect": False},
                        {"text": "La taille réelle est de dix centimètres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 10 cm x 100 = 1 000 cm. En convertissant en mètres : 1 000 cm = 10 m."
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
                    "question": "Quel théorème permet de calculer la longueur d'un côté dans un triangle rectangle ?",
                    "answerOptions": [
                        {"text": "Le théorème de Pythagore", "isCorrect": True},
                        {"text": "Le théorème de Thalès", "isCorrect": False},
                        {"text": "Le théorème de l'angle droit", "isCorrect": False},
                        {"text": "Le théorème des milieux", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le théorème de Pythagore s'applique exclusivement dans les triangles rectangles. Il établit que le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés."
                },
                {
                    "questionNumber": 22,
                    "question": "Dans un triangle rectangle, comment s'appelle le côté opposé à l'angle droit ?",
                    "answerOptions": [
                        {"text": "Le côté nommé l'hypoténuse", "isCorrect": True},
                        {"text": "Le côté nommé l'adjacent", "isCorrect": False},
                        {"text": "Le côté nommé l'opposé", "isCorrect": False},
                        {"text": "Le côté nommé la base", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'hypoténuse est le côté le plus long du triangle rectangle. C'est celui qui ne touche pas l'angle droit."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la condition pour utiliser le théorème de Thalès ?",
                    "answerOptions": [
                        {"text": "Avoir deux droites strictement parallèles", "isCorrect": True},
                        {"text": "Avoir un angle de quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Avoir trois côtés de même longueur", "isCorrect": False},
                        {"text": "Avoir un cercle qui passe par les sommets", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le théorème de Thalès nécessite deux droites parallèles coupées par deux sécantes. Il permet de calculer des longueurs grâce à la proportionnalité des segments."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la somme des angles d'un quadrilatère (ex: carré, rectangle) ?",
                    "answerOptions": [
                        {"text": "Trois cent soixante degrés au total", "isCorrect": True},
                        {"text": "Cent quatre-vingts degrés au total", "isCorrect": False},
                        {"text": "Quatre-vingt-dix degrés au total", "isCorrect": False},
                        {"text": "Cinq cent quarante degrés au total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un quadrilatère peut être coupé en deux triangles. Comme chaque triangle totalise 180°, le quadrilatère totalise 2 x 180° = 360°."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment appelle-t-on un polygone qui possède huit côtés ?",
                    "answerOptions": [
                        {"text": "Un polygone nommé octogone", "isCorrect": True},
                        {"text": "Un polygone nommé hexagone", "isCorrect": False},
                        {"text": "Un polygone nommé pentagone", "isCorrect": False},
                        {"text": "Un polygone nommé décagone", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 'Octo' signifie huit en grec. Un octogone régulier possède 8 côtés égaux et 8 angles égaux."
                },
                {
                    "questionNumber": 26,
                    "question": "Qu'est-ce qu'une médiatrice d'un segment ?",
                    "answerOptions": [
                        {"text": "La droite perpendiculaire passant par le milieu", "isCorrect": True},
                        {"text": "La droite qui coupe un angle en deux parties", "isCorrect": False},
                        {"text": "La droite qui relie deux sommets opposés", "isCorrect": False},
                        {"text": "La droite parallèle au segment choisi", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La médiatrice est l'ensemble des points situés à égale distance des deux extrémités du segment. Elle est toujours perpendiculaire au segment et passe par son milieu."
                },
                {
                    "questionNumber": 27,
                    "question": "Dans un triangle, qu'est-ce qu'une hauteur ?",
                    "answerOptions": [
                        {"text": "Une droite issue d'un sommet et perpendiculaire au côté opposé", "isCorrect": True},
                        {"text": "Une droite qui passe par les milieux de deux côtés", "isCorrect": False},
                        {"text": "Une droite qui coupe un angle en deux angles égaux", "isCorrect": False},
                        {"text": "Une droite qui mesure la longueur totale du côté", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La hauteur sert à calculer l'aire du triangle (Base x Hauteur / 2). Les trois hauteurs d'un triangle se coupent en un point appelé l'orthocentre."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la définition d'un losange ?",
                    "answerOptions": [
                        {"text": "Un quadrilatère ayant ses quatre côtés égaux", "isCorrect": True},
                        {"text": "Un quadrilatère ayant quatre angles droits", "isCorrect": False},
                        {"text": "Un quadrilatère ayant deux côtés parallèles", "isCorrect": False},
                        {"text": "Un triangle ayant deux côtés de même longueur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le losange est un parallélogramme particulier. Ses diagonales se coupent en leur milieu et sont perpendiculaires."
                },
                {
                    "questionNumber": 29,
                    "question": "Si un triangle possède deux angles de 60°, le troisième angle mesure :",
                    "answerOptions": [
                        {"text": "Soixante degrés exactement", "isCorrect": True},
                        {"text": "Quatre-vingt-dix degrés exactement", "isCorrect": False},
                        {"text": "Trente degrés exactement", "isCorrect": False},
                        {"text": "Cent vingt degrés exactement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La somme fait 180°. Calcul : 180 - (60 + 60) = 180 - 120 = 60°. Le triangle est donc équilatéral."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel instrument utilise-t-on pour tracer des cercles précis ?",
                    "answerOptions": [
                        {"text": "Un compas de géométrie", "isCorrect": True},
                        {"text": "Un rapporteur d'angles", "isCorrect": False},
                        {"text": "Une équerre à angle droit", "isCorrect": False},
                        {"text": "Une règle plate graduée", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le compas permet de reporter des longueurs et de tracer des arcs de cercle. L'écartement des branches définit le rayon du cercle."
                },
                {
                    "questionNumber": 31,
                    "question": "Que signifie le mot 'isocèle' pour un triangle ?",
                    "answerOptions": [
                        {"text": "Il possède deux côtés de même longueur", "isCorrect": True},
                        {"text": "Il possède trois côtés de même longueur", "isCorrect": False},
                        {"text": "Il ne possède aucun côté de même longueur", "isCorrect": False},
                        {"text": "Il possède obligatoirement un angle droit", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un triangle isocèle a deux côtés égaux et deux angles égaux (les angles à la base)."
                },
                {
                    "questionNumber": 32,
                    "question": "Dans un cercle, qu'est-ce que le diamètre ?",
                    "answerOptions": [
                        {"text": "Un segment passant par le centre et reliant deux points", "isCorrect": True},
                        {"text": "Un segment reliant le centre à un point du bord", "isCorrect": False},
                        {"text": "La ligne courbe qui entoure toute la surface", "isCorrect": False},
                        {"text": "Un segment qui ne touche jamais le centre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le diamètre est la plus longue corde d'un cercle. Sa longueur est égale à deux fois celle du rayon (D = 2R)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la particularité des diagonales d'un rectangle ?",
                    "answerOptions": [
                        {"text": "Elles ont la même longueur et se coupent au milieu", "isCorrect": True},
                        {"text": "Elles sont perpendiculaires et de même longueur", "isCorrect": False},
                        {"text": "Elles coupent les angles du sommet en deux", "isCorrect": False},
                        {"text": "Elles sont parallèles aux côtés extérieurs", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans un rectangle, les diagonales sont égales mais ne sont pas perpendiculaires (sauf si c'est un carré)."
                },
                {
                    "questionNumber": 34,
                    "question": "Combien de sommets possède un triangle ?",
                    "answerOptions": [
                        {"text": "Un total de trois sommets", "isCorrect": True},
                        {"text": "Un total de quatre sommets", "isCorrect": False},
                        {"text": "Un total de deux sommets", "isCorrect": False},
                        {"text": "Un total de six sommets", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le sommet est le point de rencontre de deux côtés. Un triangle a 3 côtés, 3 angles et 3 sommets."
                },
                {
                    "questionNumber": 35,
                    "question": "Un angle aigu est un angle dont la mesure est :",
                    "answerOptions": [
                        {"text": "Inférieure à quatre-vingt-dix degrés", "isCorrect": True},
                        {"text": "Supérieure à quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Égale à cent-quatre-vingts degrés", "isCorrect": False},
                        {"text": "Égale à quatre-vingt-dix degrés", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un angle aigu est 'pointu'. S'il mesure exactement 90°, il est droit. S'il est compris entre 90° et 180°, il est obtus."
                },
                {
                    "questionNumber": 36,
                    "question": "Que vaut la racine carrée de 49 ?",
                    "answerOptions": [
                        {"text": "La valeur entière de sept", "isCorrect": True},
                        {"text": "La valeur entière de neuf", "isCorrect": False},
                        {"text": "La valeur entière de six", "isCorrect": False},
                        {"text": "La valeur entière de quatorze", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La racine carrée d'un nombre A est le nombre qui, multiplié par lui-même, donne A. Ici : 7 x 7 = 49."
                },
                {
                    "questionNumber": 37,
                    "question": "Dans le théorème de Pythagore, si les côtés valent 3 et 4, l'hypoténuse vaut :",
                    "answerOptions": [
                        {"text": "La valeur entière de cinq", "isCorrect": True},
                        {"text": "La valeur entière de sept", "isCorrect": False},
                        {"text": "La valeur entière de vingt-cinq", "isCorrect": False},
                        {"text": "La valeur entière de douze", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Calcul : 3² + 4² = 9 + 16 = 25. La racine carrée de 25 est 5. C'est le célèbre triangle 3-4-5."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la somme des angles d'un triangle ?",
                    "answerOptions": [
                        {"text": "Cent quatre-vingts degrés", "isCorrect": True},
                        {"text": "Trois cent soixante degrés", "isCorrect": False},
                        {"text": "Quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Cent degrés", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une règle d'or en géométrie plane : peu importe sa forme, les trois angles d'un triangle additionnés font toujours un angle plat (180°)."
                },
                {
                    "questionNumber": 39,
                    "question": "Que signifie le mot 'parallèle' ?",
                    "answerOptions": [
                        {"text": "Deux droites qui ne se croisent jamais", "isCorrect": True},
                        {"text": "Deux droites qui se coupent à angle droit", "isCorrect": False},
                        {"text": "Deux droites qui ont la même couleur", "isCorrect": False},
                        {"text": "Deux droites qui se croisent en un point", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Deux droites parallèles conservent un écartement constant sur toute leur longueur."
                },
                {
                    "questionNumber": 40,
                    "question": "Un triangle dont les trois côtés sont inégaux est dit :",
                    "answerOptions": [
                        {"text": "Un triangle de type scalène", "isCorrect": True},
                        {"text": "Un triangle de type isocèle", "isCorrect": False},
                        {"text": "Un triangle de type équilatéral", "isCorrect": False},
                        {"text": "Un triangle de type rectangle", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 'Scalène' (ou triangle quelconque) signifie qu'il n'a aucune symétrie particulière."
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
                    "question": "Résoudre l'équation suivante : x + 10 = 25.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à quinze", "isCorrect": True},
                        {"text": "La valeur de x est égale à trente-cinq", "isCorrect": False},
                        {"text": "La valeur de x est égale à deux virgule cinq", "isCorrect": False},
                        {"text": "La valeur de x est égale à cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On isole x en soustrayant 10 des deux côtés. Calcul : x = 25 - 10 = 15."
                },
                {
                    "questionNumber": 42,
                    "question": "Que vaut l'expression 2x + 5 si la variable x est égale à 3 ?",
                    "answerOptions": [
                        {"text": "Le résultat est égal à onze", "isCorrect": True},
                        {"text": "Le résultat est égal à dix", "isCorrect": False},
                        {"text": "Le résultat est égal à seize", "isCorrect": False},
                        {"text": "Le résultat est égal à vingt-et-un", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On remplace x par 3 et on respecte les priorités (multiplication d'abord). Calcul : (2 x 3) + 5 = 6 + 5 = 11."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la solution de l'équation 4x = 24 ?",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à six", "isCorrect": True},
                        {"text": "La valeur de x est égale à vingt", "isCorrect": False},
                        {"text": "La valeur de x est égale à quatre", "isCorrect": False},
                        {"text": "La valeur de x est égale à quatre-vingt-seize", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On divise 24 par 4 pour trouver la valeur de x. Calcul : x = 24 / 4 = 6."
                },
                {
                    "questionNumber": 44,
                    "question": "Réduisez l'expression suivante : 5a - 2a + 4a.",
                    "answerOptions": [
                        {"text": "L'expression réduite est égale à 7a", "isCorrect": True},
                        {"text": "L'expression réduite est égale à 11a", "isCorrect": False},
                        {"text": "L'expression réduite est égale à 3a", "isCorrect": False},
                        {"text": "L'expression réduite est égale à a", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On additionne les coefficients car les lettres sont identiques. Calcul : (5 - 2 + 4)a = 7a."
                },
                {
                    "questionNumber": 45,
                    "question": "Trouvez la valeur de y dans : y / 3 = 7.",
                    "answerOptions": [
                        {"text": "La valeur de y est égale à vingt-et-un", "isCorrect": True},
                        {"text": "La valeur de y est égale à dix", "isCorrect": False},
                        {"text": "La valeur de y est égale à quatre", "isCorrect": False},
                        {"text": "La valeur de y est égale à sept tiers", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'inverse de la division par 3 est la multiplication par 3. Calcul : y = 7 x 3 = 21."
                },
                {
                    "questionNumber": 46,
                    "question": "Développer l'expression suivante : 4(x - 2).",
                    "answerOptions": [
                        {"text": "L'expression développée est 4x - 8", "isCorrect": True},
                        {"text": "L'expression développée est 4x - 2", "isCorrect": False},
                        {"text": "L'expression développée est x - 8", "isCorrect": False},
                        {"text": "L'expression développée est 4x + 8", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On distribue le 4 sur chaque terme de la parenthèse. Calcul : (4 x x) - (4 x 2) = 4x - 8."
                },
                {
                    "questionNumber": 47,
                    "question": "Si a = 5 et b = 2, que vaut le produit a x b ?",
                    "answerOptions": [
                        {"text": "Le produit est égal à dix", "isCorrect": True},
                        {"text": "Le produit est égal à sept", "isCorrect": False},
                        {"text": "Le produit est égal à trois", "isCorrect": False},
                        {"text": "Le produit est égal à vingt-cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On effectue simplement la multiplication. Calcul : 5 x 2 = 10."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la valeur de x² pour x = 6 ?",
                    "answerOptions": [
                        {"text": "La valeur est de trente-six", "isCorrect": True},
                        {"text": "La valeur est de douze", "isCorrect": False},
                        {"text": "La valeur est de soixante-quatre", "isCorrect": False},
                        {"text": "La valeur est de six", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 6² = 6 x 6 = 36. Elever au carré, c'est multiplier par soi-même."
                },
                {
                    "questionNumber": 49,
                    "question": "Résoudre : 2x + 4 = 12.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à quatre", "isCorrect": True},
                        {"text": "La valeur de x est égale à huit", "isCorrect": False},
                        {"text": "La valeur de x est égale à seize", "isCorrect": False},
                        {"text": "La valeur de x est égale à six", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 1) 2x = 12 - 4 = 8. 2) x = 8 / 2 = 4. La solution est 4."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment écrit-on 'le double de x augmenté de 1' ?",
                    "answerOptions": [
                        {"text": "L'expression algébrique 2x + 1", "isCorrect": True},
                        {"text": "L'expression algébrique x + 2 + 1", "isCorrect": False},
                        {"text": "L'expression algébrique 2(x + 1)", "isCorrect": False},
                        {"text": "L'expression algébrique x² + 1", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 'Double de x' = 2x. 'Augmenté de 1' = + 1. Donc 2x + 1."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le résultat de 10 - 2 x 3 ?",
                    "answerOptions": [
                        {"text": "Le résultat est égal à quatre", "isCorrect": True},
                        {"text": "Le résultat est égal à vingt-quatre", "isCorrect": False},
                        {"text": "Le résultat est égal à huit", "isCorrect": False},
                        {"text": "Le résultat est égal à trente", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Priorité à la multiplication ! Calcul : 10 - (2 x 3) = 10 - 6 = 4."
                },
                {
                    "questionNumber": 52,
                    "question": "Si 3 stylos coûtent x euros, quel est le prix d'un stylo ?",
                    "answerOptions": [
                        {"text": "Le prix est de x divisé par trois", "isCorrect": True},
                        {"text": "Le prix est de trois fois x", "isCorrect": False},
                        {"text": "Le prix est de x moins trois", "isCorrect": False},
                        {"text": "Le prix est de trois plus x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour trouver le prix unitaire, on divise le prix total par la quantité."
                },
                {
                    "questionNumber": 53,
                    "question": "Factoriser l'expression suivante : 3x + 15.",
                    "answerOptions": [
                        {"text": "L'expression factorisée est 3(x + 5)", "isCorrect": True},
                        {"text": "L'expression factorisée est 3(x + 15)", "isCorrect": False},
                        {"text": "L'expression factorisée est 3x(1 + 5)", "isCorrect": False},
                        {"text": "L'expression factorisée est 15(x + 3)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le facteur commun est 3 car 15 = 3 x 5. On place le 3 devant la parenthèse."
                },
                {
                    "questionNumber": 54,
                    "question": "Que vaut (-5) x 4 ?",
                    "answerOptions": [
                        {"text": "Le résultat est de moins vingt", "isCorrect": True},
                        {"text": "Le résultat est de vingt positif", "isCorrect": False},
                        {"text": "Le résultat est de moins un", "isCorrect": False},
                        {"text": "Le résultat est de neuf positif", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le produit d'un nombre négatif par un nombre positif est toujours négatif."
                },
                {
                    "questionNumber": 55,
                    "question": "Résoudre : 10 - x = 4.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à six", "isCorrect": True},
                        {"text": "La valeur de x est égale à quatorze", "isCorrect": False},
                        {"text": "La valeur de x est égale à moins six", "isCorrect": False},
                        {"text": "La valeur de x est égale à quatre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 10 moins quel nombre fait 4 ? La réponse est 10 - 4 = 6."
                },
                {
                    "questionNumber": 56,
                    "question": "Que signifie x = 0 dans une équation ?",
                    "answerOptions": [
                        {"text": "Zéro est la solution de l'équation", "isCorrect": True},
                        {"text": "L'équation n'a aucune solution possible", "isCorrect": False},
                        {"text": "L'inconnue a disparu du calcul", "isCorrect": False},
                        {"text": "Le résultat final est forcément faux", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Zéro est un nombre comme un autre qui peut parfaitement être la solution d'un problème."
                },
                {
                    "questionNumber": 57,
                    "question": "L'image de 0 par la fonction f(x) = 5x + 7 est :",
                    "answerOptions": [
                        {"text": "La valeur entière de sept", "isCorrect": True},
                        {"text": "La valeur entière de zéro", "isCorrect": False},
                        {"text": "La valeur entière de cinq", "isCorrect": False},
                        {"text": "La valeur entière de douze", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Calcul : 5 x 0 + 7 = 0 + 7 = 7."
                },
                {
                    "questionNumber": 58,
                    "question": "Si on multiplie un nombre par -1, on obtient :",
                    "answerOptions": [
                        {"text": "Son opposé mathématique", "isCorrect": True},
                        {"text": "Son inverse mathématique", "isCorrect": False},
                        {"text": "Le chiffre zéro systématiquement", "isCorrect": False},
                        {"text": "Le même nombre sans changement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Changer le signe d'un nombre revient à prendre son opposé."
                },
                {
                    "questionNumber": 59,
                    "question": "Trouvez x si 2x + 2 = 2.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à zéro", "isCorrect": True},
                        {"text": "La valeur de x est égale à un", "isCorrect": False},
                        {"text": "La valeur de x est égale à deux", "isCorrect": False},
                        {"text": "La valeur de x est égale à moins un", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 2x = 2 - 2 = 0. Donc x = 0 / 2 = 0."
                },
                {
                    "questionNumber": 60,
                    "question": "Dans une fonction f(x) = 4, f(10) vaut :",
                    "answerOptions": [
                        {"text": "La valeur constante de quatre", "isCorrect": True},
                        {"text": "La valeur image de quarante", "isCorrect": False},
                        {"text": "La valeur image de quatorze", "isCorrect": False},
                        {"text": "La valeur image de dix", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une fonction constante. Elle renvoie toujours 4, peu importe la valeur de x choisie."
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
                    "question": "Combien de litres contient un mètre cube (1 m³) ?",
                    "answerOptions": [
                        {"text": "Un volume de mille litres", "isCorrect": True},
                        {"text": "Un volume de cent litres", "isCorrect": False},
                        {"text": "Un volume de dix litres", "isCorrect": False},
                        {"text": "Un volume de un litre seul", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 1 dm³ = 1 litre. Comme il y a 1 000 dm³ dans 1 m³, il y a 1 000 litres dans un mètre cube."
                },
                {
                    "questionNumber": 62,
                    "question": "Convertissez 250 millilitres en litres.",
                    "answerOptions": [
                        {"text": "Zéro virgule vingt-cinq litre", "isCorrect": True},
                        {"text": "Deux virgule cinq litres", "isCorrect": False},
                        {"text": "Vingt-cinq litres au total", "isCorrect": False},
                        {"text": "Zéro virgule zéro vingt-cinq litre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On divise par 1000. Calcul : 250 / 1000 = 0,25 L. Cela correspond à un quart de litre."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est l'unité de mesure légale de la pression atmosphérique ?",
                    "answerOptions": [
                        {"text": "L'unité nommée le Pascal (Pa)", "isCorrect": True},
                        {"text": "L'unité nommée le Newton (N)", "isCorrect": False},
                        {"text": "L'unité nommée le Joule (J)", "isCorrect": False},
                        {"text": "L'unité nommée le Watt (W)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le Pascal est l'unité de pression. En météo, on utilise souvent l'hectopascal (hPa). 1 bar = 100 000 Pa."
                },
                {
                    "questionNumber": 64,
                    "question": "Combien y a-t-il de centimètres carrés dans un mètre carré ?",
                    "answerOptions": [
                        {"text": "Dix mille centimètres carrés", "isCorrect": True},
                        {"text": "Cent centimètres carrés", "isCorrect": False},
                        {"text": "Mille centimètres carrés", "isCorrect": False},
                        {"text": "Dix centimètres carrés", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour les unités d'aire, on multiplie par 100 à chaque rang. 1 m² = 100 dm² = 10 000 cm²."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est l'unité de mesure d'une fréquence sonore ?",
                    "answerOptions": [
                        {"text": "L'unité nommée le Hertz (Hz)", "isCorrect": True},
                        {"text": "L'unité nommée le Décibel (dB)", "isCorrect": False},
                        {"text": "L'unité nommée le Volt (V)", "isCorrect": False},
                        {"text": "L'unité nommée le Mètre (m)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le Hertz mesure le nombre de vibrations par seconde. Le Décibel mesure l'intensité (le volume sonore)."
                },
                {
                    "questionNumber": 66,
                    "question": "Convertissez 3,5 tonnes en kilogrammes.",
                    "answerOptions": [
                        {"text": "Trois mille cinq cents kilogrammes", "isCorrect": True},
                        {"text": "Trois cent cinquante kilogrammes", "isCorrect": False},
                        {"text": "Trente-cinq mille kilogrammes", "isCorrect": False},
                        {"text": "Trente-cinq kilogrammes seulement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 1 tonne = 1 000 kg. Calcul : 3,5 x 1 000 = 3 500 kg."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la contenance d'une canette de soda classique ?",
                    "answerOptions": [
                        {"text": "Trente-trois centilitres", "isCorrect": True},
                        {"text": "Trente-trois millilitres", "isCorrect": False},
                        {"text": "Trente-trois litres", "isCorrect": False},
                        {"text": "Trente-trois décilitres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 33 cL = 0,33 L. C'est le format standard des boissons individuelles."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle est l'unité de mesure de l'énergie ?",
                    "answerOptions": [
                        {"text": "L'unité nommée le Joule (J)", "isCorrect": True},
                        {"text": "L'unité nommée le Watt (W)", "isCorrect": False},
                        {"text": "L'unité nommée l'Ampère (A)", "isCorrect": False},
                        {"text": "L'unité nommée le Volt (V)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le Joule est l'unité d'énergie (chaleur, travail, électricité). On utilise aussi souvent le kiloWatt-heure (kWh) sur les factures."
                },
                {
                    "questionNumber": 69,
                    "question": "Une durée de 3 600 secondes équivaut à :",
                    "answerOptions": [
                        {"text": "Une heure de temps exactement", "isCorrect": True},
                        {"text": "Soixante minutes de temps", "isCorrect": True},
                        {"text": "Dix minutes de temps seulement", "isCorrect": False},
                        {"text": "Vingt-quatre heures de temps", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 60 secondes x 60 minutes = 3 600 secondes. C'est la définition d'une heure."
                },
                {
                    "questionNumber": 70,
                    "question": "Combien de faces possède un cube ?",
                    "answerOptions": [
                        {"text": "Un total de six faces carrées", "isCorrect": True},
                        {"text": "Un total de huit faces carrées", "isCorrect": False},
                        {"text": "Un total de quatre faces carrées", "isCorrect": False},
                        {"text": "Un total de douze faces carrées", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un cube est comme un dé à jouer : il a 6 faces, 8 sommets et 12 arêtes."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est la formule du volume d'un pavé droit ?",
                    "answerOptions": [
                        {"text": "Longueur x largeur x hauteur", "isCorrect": True},
                        {"text": "Longueur x largeur uniquement", "isCorrect": False},
                        {"text": "Côté x côté x côté uniquement", "isCorrect": False},
                        {"text": "Base x hauteur divisé par deux", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour un solide rectangulaire, on multiplie les trois dimensions de l'espace."
                },
                {
                    "questionNumber": 72,
                    "question": "Que mesure-t-on en 'mètre linéaire' (m.l.) ?",
                    "answerOptions": [
                        {"text": "Une longueur simple de matériel", "isCorrect": True},
                        {"text": "Une surface de carrelage au sol", "isCorrect": False},
                        {"text": "Un volume d'eau dans un bac", "isCorrect": False},
                        {"text": "Le poids d'une barre métallique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le mètre linéaire est utilisé dans le bâtiment pour les plinthes, les câbles ou les clôtures (une seule dimension)."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est l'aire d'un rectangle de 5m sur 3m ?",
                    "answerOptions": [
                        {"text": "Quinze mètres carrés", "isCorrect": True},
                        {"text": "Seize mètres carrés", "isCorrect": False},
                        {"text": "Huit mètres carrés", "isCorrect": False},
                        {"text": "Trente mètres carrés", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Aire = 5 x 3 = 15 m²."
                },
                {
                    "questionNumber": 74,
                    "question": "Combien de centilitres y a-t-il dans un litre ?",
                    "answerOptions": [
                        {"text": "Un total de cent centilitres", "isCorrect": True},
                        {"text": "Un total de dix centilitres", "isCorrect": False},
                        {"text": "Un total de mille centilitres", "isCorrect": False},
                        {"text": "Un total de un centilitre seul", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 'Centi' signifie centième. Il faut donc 100 cL pour faire 1 L."
                },
                {
                    "questionNumber": 75,
                    "question": "Convertissez 0,75 kg en grammes.",
                    "answerOptions": [
                        {"text": "Sept cent cinquante grammes", "isCorrect": True},
                        {"text": "Soixante-quinze grammes", "isCorrect": False},
                        {"text": "Sept mille cinq cents grammes", "isCorrect": False},
                        {"text": "Sept virgule cinq grammes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 0,75 x 1000 = 750 g."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle est l'unité pour la résistance électrique ?",
                    "answerOptions": [
                        {"text": "L'unité nommée l'Ohm (Ω)", "isCorrect": True},
                        {"text": "L'unité nommée le Volt (V)", "isCorrect": False},
                        {"text": "L'unité nommée l'Ampère (A)", "isCorrect": False},
                        {"text": "L'unité nommée le Watt (W)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La résistance s'oppose au passage du courant."
                },
                {
                    "questionNumber": 77,
                    "question": "Combien de minutes dans 1/4 d'heure ?",
                    "answerOptions": [
                        {"text": "Quinze minutes exactement", "isCorrect": True},
                        {"text": "Vingt-cinq minutes exactement", "isCorrect": False},
                        {"text": "Dix minutes exactement", "isCorrect": False},
                        {"text": "Vingt minutes exactement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 60 minutes / 4 = 15 minutes."
                },
                {
                    "questionNumber": 78,
                    "question": "Que vaut 1 cm en millimètres ?",
                    "answerOptions": [
                        {"text": "Dix millimètres exactement", "isCorrect": True},
                        {"text": "Cent millimètres exactement", "isCorrect": False},
                        {"text": "Zéro virgule un millimètre", "isCorrect": False},
                        {"text": "Un millimètre seulement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est la graduation de base de la règle d'écolier."
                },
                {
                    "questionNumber": 79,
                    "question": "Un volume de 2 000 cm³ correspond à :",
                    "answerOptions": [
                        {"text": "Une capacité de deux litres", "isCorrect": True},
                        {"text": "Une capacité de vingt litres", "isCorrect": False},
                        {"text": "Une capacité de deux cents litres", "isCorrect": False},
                        {"text": "Une capacité de zéro virgule deux litre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 1 000 cm³ = 1 L. Donc 2 000 cm³ = 2 L."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est l'instrument pour mesurer une épaisseur très fine ?",
                    "answerOptions": [
                        {"text": "Un pied à coulisse de précision", "isCorrect": True},
                        {"text": "Une règle de maçon en alu", "isCorrect": False},
                        {"text": "Un mètre ruban de couturière", "isCorrect": False},
                        {"text": "Un rapporteur en plastique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le pied à coulisse permet de mesurer au dixième de millimètre."
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
                    "question": "Comment calcule-t-on la moyenne de 10, 15 et 20 ?",
                    "answerOptions": [
                        {"text": "La moyenne est égale à quinze", "isCorrect": True},
                        {"text": "La moyenne est égale à dix", "isCorrect": False},
                        {"text": "La moyenne est égale à quarante-cinq", "isCorrect": False},
                        {"text": "La moyenne est égale à douze", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Somme = 45. Nombre de valeurs = 3. Moyenne = 45 / 3 = 15."
                },
                {
                    "questionNumber": 82,
                    "question": "On lance une pièce équilibrée. Quelle est la probabilité d'avoir 'Face' ?",
                    "answerOptions": [
                        {"text": "Une probabilité de zéro virgule cinq", "isCorrect": True},
                        {"text": "Une probabilité de un entier", "isCorrect": False},
                        {"text": "Une probabilité de zéro virgule deux", "isCorrect": False},
                        {"text": "Une probabilité de zéro virgule vingt-cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 1 chance sur 2 = 1/2 = 0,5."
                },
                {
                    "questionNumber": 83,
                    "question": "Qu'est-ce qu'un échantillon en statistiques ?",
                    "answerOptions": [
                        {"text": "Une partie représentative d'une population", "isCorrect": True},
                        {"text": "L'ensemble de toutes les personnes du pays", "isCorrect": False},
                        {"text": "Le résultat final d'un calcul complexe", "isCorrect": False},
                        {"text": "Un graphique avec des barres de couleur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On étudie un petit groupe (échantillon) pour comprendre le grand groupe (population)."
                },
                {
                    "questionNumber": 84,
                    "question": "On tire une boule dans une urne contenant 2 boules rouges et 8 vertes. Probabilité de tirer une rouge ?",
                    "answerOptions": [
                        {"text": "Deux chances sur dix soit vingt pour cent", "isCorrect": True},
                        {"text": "Deux chances sur huit soit vingt-cinq pour cent", "isCorrect": False},
                        {"text": "Huit chances sur dix soit quatre-vingts pour cent", "isCorrect": False},
                        {"text": "Une chance sur deux soit cinquante pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Total = 10 boules. Rouges = 2. Probabilité = 2/10 = 0,2."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle est la valeur de la médiane de cette série : 2, 5, 8, 10, 12 ?",
                    "answerOptions": [
                        {"text": "La valeur centrale est de huit", "isCorrect": True},
                        {"text": "La valeur centrale est de sept virgule quatre", "isCorrect": False},
                        {"text": "La valeur centrale est de dix", "isCorrect": False},
                        {"text": "La valeur centrale est de deux", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La série est ordonnée. Il y a 5 valeurs. La 3ème valeur (8) laisse deux nombres avant et deux nombres après."
                },
                {
                    "questionNumber": 86,
                    "question": "Que signifie une probabilité de 1 ?",
                    "answerOptions": [
                        {"text": "L'événement est certain de se produire", "isCorrect": True},
                        {"text": "L'événement est totalement impossible", "isCorrect": False},
                        {"text": "L'événement a une chance sur deux", "isCorrect": False},
                        {"text": "L'événement est très rare ici même", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** En probabilité, 1 signifie 100 % de chances."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment appelle-t-on le résultat d'une expérience aléatoire ?",
                    "answerOptions": [
                        {"text": "Une issue de l'expérience", "isCorrect": True},
                        {"text": "Une entrée de l'expérience", "isCorrect": False},
                        {"text": "Une moyenne de l'expérience", "isCorrect": False},
                        {"text": "Une erreur de l'expérience", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Chaque possibilité de résultat (ex: 'obtenir 6') est une issue."
                },
                {
                    "questionNumber": 88,
                    "question": "La fréquence est un nombre toujours compris entre :",
                    "answerOptions": [
                        {"text": "Les valeurs de zéro et de un", "isCorrect": True},
                        {"text": "Les valeurs de un et de cent", "isCorrect": False},
                        {"text": "Les valeurs de moins un et plus un", "isCorrect": False},
                        {"text": "Toutes les valeurs positives possibles", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une fréquence f = n/N est une proportion, elle ne peut pas dépasser 1 ni être négative."
                },
                {
                    "questionNumber": 89,
                    "question": "Si une fréquence est de 0,40, cela correspond à :",
                    "answerOptions": [
                        {"text": "Quarante pour cent de l'effectif", "isCorrect": True},
                        {"text": "Quatre pour cent de l'effectif", "isCorrect": False},
                        {"text": "Zéro virgille quatre pour cent", "isCorrect": False},
                        {"text": "Quatre cents pour cent de l'effectif", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On multiplie par 100. 0,40 x 100 = 40 %."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel graphique utilise des secteurs angulaires ?",
                    "answerOptions": [
                        {"text": "Le diagramme de type circulaire", "isCorrect": True},
                        {"text": "Le diagramme de type à bâtons", "isCorrect": False},
                        {"text": "L'histogramme rectangulaire", "isCorrect": False},
                        {"text": "La courbe de température", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Appelé aussi 'camembert', l'angle est proportionnel à la fréquence."
                },
                {
                    "questionNumber": 91,
                    "question": "On lance un dé. Probabilité d'avoir un chiffre supérieur à 6 ?",
                    "answerOptions": [
                        {"text": "Une probabilité égale à zéro", "isCorrect": True},
                        {"text": "Une probabilité égale à un", "isCorrect": False},
                        {"text": "Une probabilité de un sur six", "isCorrect": False},
                        {"text": "Une probabilité de six sur six", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est un événement impossible, car le dé s'arrête à 6."
                },
                {
                    "questionNumber": 92,
                    "question": "Dans une série, le mode est la valeur qui a :",
                    "answerOptions": [
                        {"text": "Le plus grand effectif associé", "isCorrect": True},
                        {"text": "Le plus petit effectif associé", "isCorrect": False},
                        {"text": "La plus grande valeur numérique", "isCorrect": False},
                        {"text": "La plus petite valeur numérique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est la donnée la plus fréquente."
                },
                {
                    "questionNumber": 93,
                    "question": "L'étendue de la série (10, 20, 30, 50) est :",
                    "answerOptions": [
                        {"text": "Quarante unités au total", "isCorrect": True},
                        {"text": "Cinquante unités au total", "isCorrect": False},
                        {"text": "Dix unités au total", "isCorrect": False},
                        {"text": "Vingt-cinq unités au total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 50 - 10 = 40."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment appelle-t-on le 'hasard' en mathématiques ?",
                    "answerOptions": [
                        {"text": "Le caractère aléatoire d'un test", "isCorrect": True},
                        {"text": "Le caractère exact d'un test", "isCorrect": False},
                        {"text": "Le caractère faux d'un test", "isCorrect": False},
                        {"text": "Le caractère nul d'un test", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Aléatoire vient du latin 'alea' (le dé)."
                },
                {
                    "questionNumber": 95,
                    "question": "La somme des fréquences d'une série vaut :",
                    "answerOptions": [
                        {"text": "La valeur entière de un", "isCorrect": True},
                        {"text": "La valeur entière de cent", "isCorrect": False},
                        {"text": "La valeur entière de zéro", "isCorrect": False},
                        {"text": "La valeur de l'effectif total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si on additionne toutes les parts d'un tout, on obtient 1 (ou 100 %)."
                },
                {
                    "questionNumber": 96,
                    "question": "On tire une carte. Probabilité d'avoir le roi de cœur ?",
                    "answerOptions": [
                        {"text": "Une chance sur trente-deux issues", "isCorrect": True},
                        {"text": "Une chance sur quatre issues", "isCorrect": False},
                        {"text": "Une chance sur huit issues", "isCorrect": False},
                        {"text": "Quatre chances sur trente-deux", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Il n'y a qu'un seul roi de cœur dans le paquet."
                },
                {
                    "questionNumber": 97,
                    "question": "Une probabilité de 0,25 correspond à :",
                    "answerOptions": [
                        {"text": "Vingt-cinq pour cent de chances", "isCorrect": True},
                        {"text": "Deux virgule cinq pour cent", "isCorrect": False},
                        {"text": "Soixante-quinze pour cent", "isCorrect": False},
                        {"text": "Zéro virgule vingt-cinq pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 0,25 x 100 = 25 %."
                },
                {
                    "questionNumber": 98,
                    "question": "En statistiques, qu'est-ce que la population ?",
                    "answerOptions": [
                        {"text": "L'ensemble du groupe global étudié", "isCorrect": True},
                        {"text": "Une petite partie choisie au hasard", "isCorrect": False},
                        {"text": "La liste des nombres du tableau", "isCorrect": False},
                        {"text": "La moyenne de l'ensemble des gens", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La population est le groupe total (ex: tous les élèves du lycée). L'échantillon en est une petite partie."
                },
                {
                    "questionNumber": 99,
                    "question": "Si la fréquence d'un événement est 0,125, quel est son pourcentage ?",
                    "answerOptions": [
                        {"text": "Douze virgule cinq pour cent", "isCorrect": True},
                        {"text": "Un virgule vingt-cinq pour cent", "isCorrect": False},
                        {"text": "Cent vingt-cinq pour cent", "isCorrect": False},
                        {"text": "Zéro virgule cent vingt-cinq pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 0,125 x 100 = 12,5 %."
                },
                {
                    "questionNumber": 100,
                    "question": "Que signifie 'tirage sans remise' ?",
                    "answerOptions": [
                        {"text": "On ne remet pas l'objet tiré dans l'urne", "isCorrect": True},
                        {"text": "On remet l'objet immédiatement après", "isCorrect": False},
                        {"text": "On ne gagne aucun cadeau au tirage", "isCorrect": False},
                        {"text": "On tire tout en même temps à la main", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans un tirage sans remise, l'effectif total diminue à chaque tour, ce qui change les probabilités suivantes."
                }
            ]
        }
    }
}