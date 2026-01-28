quiz_data = {
    "title": "Quiz Mathématiques - Niveau CAP (100 Questions) - Version Optimisée",
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
                        {"text": "Le montant de la taxe est de vingt euros", "isCorrect": True},
                        {"text": "Le montant de la taxe est de cent vingt euros", "isCorrect": False},
                        {"text": "Le montant de la taxe est de dix euros", "isCorrect": False},
                        {"text": "Le montant de la taxe est de cinq euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour calculer le montant de la taxe (TVA), on multiplie le Prix Hors Taxe par le taux exprimé sous forme décimale. Calcul : 100 € x 0,20 = 20 €. Le montant de la TVA s'ajoute ensuite au prix HT pour donner le prix TTC."
                },
                {
                    "questionNumber": 2,
                    "question": "Comment calcule-t-on un Prix TTC à partir d'un Prix HT et d'une TVA ?",
                    "answerOptions": [
                        {"text": "On additionne le Prix HT et le montant de la TVA", "isCorrect": True},
                        {"text": "On soustrait le montant de la TVA au Prix HT", "isCorrect": False},
                        {"text": "On multiplie le Prix HT par le montant de la TVA", "isCorrect": False},
                        {"text": "On divise le Prix HT par le montant de la TVA", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le Prix Toutes Taxes Comprises (TTC) représente le montant total payé par le client. Il est égal à la somme du Prix Hors Taxe (HT) et de la Taxe sur la Valeur Ajoutée (TVA). Formule : TTC = HT + TVA."
                },
                {
                    "questionNumber": 3,
                    "question": "Un article à 50 € bénéficie d'une remise de 10 %. Quel est le montant de la réduction ?",
                    "answerOptions": [
                        {"text": "La réduction est égale à cinq euros", "isCorrect": True},
                        {"text": "La réduction est égale à dix euros", "isCorrect": False},
                        {"text": "La réduction est égale à quarante-cinq euros", "isCorrect": False},
                        {"text": "La réduction est égale à un euro", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour trouver le montant d'une remise, on multiplie le prix initial par le pourcentage de réduction. Calcul : 50 € x (10/100) = 50 x 0,10 = 5 €. Le nouveau prix sera de 45 € (50 - 5)."
                },
                {
                    "questionNumber": 4,
                    "question": "Que signifie le sigle HT dans un document commercial ?",
                    "answerOptions": [
                        {"text": "Le montant global Hors Taxes", "isCorrect": True},
                        {"text": "La Haute Tension électrique", "isCorrect": False},
                        {"text": "Les Honoraires du Travailleur", "isCorrect": False},
                        {"text": "Le Haut Tarif des marchandises", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le prix Hors Taxes (HT) est le prix d'un produit ou d'un service avant l'application des taxes gouvernementales (TVA). C'est la base de calcul utilisée par les professionnels entre eux."
                },
                {
                    "questionNumber": 5,
                    "question": "Si le prix TTC est de 60 € et la TVA est de 10 €, quel est le prix HT ?",
                    "answerOptions": [
                        {"text": "Le prix HT est de cinquante euros", "isCorrect": True},
                        {"text": "Le prix HT est de soixante-dix euros", "isCorrect": False},
                        {"text": "Le prix HT est de six euros seulement", "isCorrect": False},
                        {"text": "Le prix HT est de soixante euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On utilise la formule inverse du TTC. Puisque TTC = HT + TVA, alors HT = TTC - TVA. Calcul : 60 € - 10 € = 50 €."
                },
                {
                    "questionNumber": 6,
                    "question": "Un client achète 3 articles à 12 € l'unité. Quel est le montant total ?",
                    "answerOptions": [
                        {"text": "Le montant total est de trente-six euros", "isCorrect": True},
                        {"text": "Le montant total est de quinze euros", "isCorrect": False},
                        {"text": "Le montant total est de vingt-quatre euros", "isCorrect": False},
                        {"text": "Le montant total est de quarante euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour calculer un prix total, on effectue une multiplication simple de la quantité par le prix unitaire. Calcul : 3 x 12 € = 36 €."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est l'utilité d'un ticket de caisse en magasin ?",
                    "answerOptions": [
                        {"text": "Servir de preuve d'achat pour le client", "isCorrect": True},
                        {"text": "Décorer l'intérieur du sac de courses", "isCorrect": False},
                        {"text": "Donner l'adresse de tous les autres magasins", "isCorrect": False},
                        {"text": "Calculer la météo locale de la journée", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le ticket de caisse détaille les achats, les taxes payées et le mode de règlement. Il est indispensable pour effectuer un échange, obtenir un remboursement ou faire valoir une garantie."
                },
                {
                    "questionNumber": 8,
                    "question": "Si un taux de TVA est de 5,5 %, comment l'écrit-on sous forme décimale ?",
                    "answerOptions": [
                        {"text": "Le nombre décimal zéro virgule zéro cinquante-cinq", "isCorrect": True},
                        {"text": "Le nombre décimal zéro virgule cinquante-cinq", "isCorrect": False},
                        {"text": "Le nombre décimal cinq virgule cinq", "isCorrect": False},
                        {"text": "Le nombre entier cinquante-cinq", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour passer d'un pourcentage à un nombre décimal, on divise par 100. Calcul : 5,5 / 100 = 0,055. Cette valeur est utilisée pour multiplier directement les montants lors des calculs de taxes."
                },
                {
                    "questionNumber": 9,
                    "question": "Qu'est-ce qu'une remise exceptionnelle ?",
                    "answerOptions": [
                        {"text": "Une réduction accordée pour un événement précis", "isCorrect": True},
                        {"text": "Une augmentation de prix pour les clients", "isCorrect": False},
                        {"text": "Une taxe supplémentaire imposée par la ville", "isCorrect": False},
                        {"text": "Le paiement obligatoire d'un acompte financier", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une remise est un geste commercial (soldes, fidélité, défaut mineur). Elle se déduit du prix de vente pour obtenir le prix net à payer."
                },
                {
                    "questionNumber": 10,
                    "question": "Sur une facture, que signifie le terme 'Net à payer' ?",
                    "answerOptions": [
                        {"text": "La somme finale que le client doit verser", "isCorrect": True},
                        {"text": "La somme des remises accordées par le vendeur", "isCorrect": False},
                        {"text": "Le poids total des marchandises livrées", "isCorrect": False},
                        {"text": "Le nom du transporteur chargé de la livraison", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le 'Net à payer' est le résultat final de tous les calculs (HT + TVA - Remises). C'est le montant effectif qui sortira du portefeuille du client."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le montant de la TVA pour un produit HT de 200 € à 20 % ?",
                    "answerOptions": [
                        {"text": "Le montant de la taxe est de quarante euros", "isCorrect": True},
                        {"text": "Le montant de la taxe est de vingt euros", "isCorrect": False},
                        {"text": "Le montant de la taxe est de deux cents euros", "isCorrect": False},
                        {"text": "Le montant de la taxe est de deux euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On applique la formule (Prix HT x Taux). Calcul : 200 € x 0,20 = 40 €. Le prix TTC serait alors de 240 €."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment calcule-t-on le montant d'une TVA à 10 % sur un service ?",
                    "answerOptions": [
                        {"text": "On divise le prix Hors Taxes par dix", "isCorrect": True},
                        {"text": "On multiplie le prix Hors Taxes par dix", "isCorrect": False},
                        {"text": "On soustrait dix euros au prix global", "isCorrect": False},
                        {"text": "On ajoute dix pour cent au poids total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Puisque 10 % correspond à la fraction 10/100 ou 1/10, calculer 10 % d'une valeur revient à la diviser par 10. Exemple : pour 150 € HT, la TVA est de 15 €."
                },
                {
                    "questionNumber": 13,
                    "question": "Un produit de 100 € subit une augmentation de 5 %. Quel est son nouveau prix ?",
                    "answerOptions": [
                        {"text": "Le nouveau prix est de cent cinq euros", "isCorrect": True},
                        {"text": "Le nouveau prix est de quatre-vingt-quinze euros", "isCorrect": False},
                        {"text": "Le nouveau prix est de cent cinquante euros", "isCorrect": False},
                        {"text": "Le nouveau prix est de cinq euros seulement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Calcul de l'augmentation : 100 € x 0,05 = 5 €. On ajoute cette somme au prix initial : 100 + 5 = 105 €. En une seule étape, on peut multiplier par 1,05."
                },
                {
                    "questionNumber": 14,
                    "question": "Qu'est-ce qu'une facture proforma ?",
                    "answerOptions": [
                        {"text": "Un document provisoire servant de devis", "isCorrect": True},
                        {"text": "Un reçu final après le paiement comptant", "isCorrect": False},
                        {"text": "Un bon de livraison sans aucun prix affiché", "isCorrect": False},
                        {"text": "Une lettre de réclamation pour colis abîmé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La facture proforma permet au client de connaître les conditions précises de vente avant de confirmer sa commande. Elle n'a pas de valeur comptable finale mais sert de base à l'accord."
                },
                {
                    "questionNumber": 15,
                    "question": "Comment appelle-t-on l'argent rendu au client lors d'un achat en espèces ?",
                    "answerOptions": [
                        {"text": "La monnaie ou le reliquat du paiement", "isCorrect": True},
                        {"text": "La taxe de service sur la vente directe", "isCorrect": False},
                        {"text": "Le bénéfice net du commerçant local", "isCorrect": False},
                        {"text": "Le pourboire facultatif pour le vendeur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La monnaie rendue est la différence entre la somme donnée par le client et le prix TTC. Calcul : Somme donnée - Prix TTC = Monnaie à rendre."
                },
                {
                    "questionNumber": 16,
                    "question": "Un commerçant achète un produit 10 € et le revend 15 €. Quel est son bénéfice ?",
                    "answerOptions": [
                        {"text": "Le bénéfice brut est de cinq euros", "isCorrect": True},
                        {"text": "Le bénéfice brut est de vingt-cinq euros", "isCorrect": False},
                        {"text": "Le bénéfice brut est de dix euros", "isCorrect": False},
                        {"text": "Le bénéfice brut est de cent cinquante euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La marge brute (ou bénéfice) se calcule en faisant la différence entre le prix de vente et le prix d'achat. Calcul : 15 € - 10 € = 5 €."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le taux de TVA normal en France pour la majorité des produits ?",
                    "answerOptions": [
                        {"text": "Un taux fixe de vingt pour cent", "isCorrect": True},
                        {"text": "Un taux fixe de cinquante pour cent", "isCorrect": False},
                        {"text": "Un taux fixe de cinq virgule cinq pour cent", "isCorrect": False},
                        {"text": "Un taux fixe de deux pour cent seulement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** En France, le taux normal est de 20 %. Il existe des taux réduits : 10 % (restauration, transports), 5,5 % (produits alimentaires de base, livres) et 2,1 % (médicaments remboursés)."
                },
                {
                    "questionNumber": 18,
                    "question": "Que signifie 'Payer à crédit' ?",
                    "answerOptions": [
                        {"text": "Payer la somme totale plus tard", "isCorrect": True},
                        {"text": "Payer la somme totale immédiatement", "isCorrect": False},
                        {"text": "Payer avec des pièces de monnaie", "isCorrect": False},
                        {"text": "Ne jamais payer la marchandise reçue", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le crédit (ou paiement différé) permet d'obtenir un bien tout de suite et de le payer plus tard, souvent en plusieurs fois (mensualités), parfois avec des intérêts supplémentaires."
                },
                {
                    "questionNumber": 19,
                    "question": "Traduisez 25 % en fraction simplifiée.",
                    "answerOptions": [
                        {"text": "La fraction égale à un quart", "isCorrect": True},
                        {"text": "La fraction égale à un demi", "isCorrect": False},
                        {"text": "La fraction égale à trois quarts", "isCorrect": False},
                        {"text": "La fraction égale à un cinquième", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 25 % signifie 25/100. En divisant le numérateur et le dénominateur par 25, on obtient la fraction simplifiée 1/4. C'est le quart de l'unité."
                },
                {
                    "questionNumber": 20,
                    "question": "Un pantalon à 40 € est soldé à -50 %. Quel est son nouveau prix ?",
                    "answerOptions": [
                        {"text": "Le prix soldé est de vingt euros", "isCorrect": True},
                        {"text": "Le prix soldé est de dix euros", "isCorrect": False},
                        {"text": "Le prix soldé est de trente euros", "isCorrect": False},
                        {"text": "Le prix soldé est de quarante euros", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une réduction de 50 % revient à diviser le prix par deux. Calcul : 40 € / 2 = 20 €. C'est la moitié du prix initial."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : GÉOMÉTRIE PLANE, PÉRIMÈTRES ET AIRES (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : GÉOMÉTRIE PLANE, PÉRIMÈTRES ET AIRES",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la formule du périmètre d'un carré de côté 'c' ?",
                    "answerOptions": [
                        {"text": "La longueur du côté multipliée par quatre", "isCorrect": True},
                        {"text": "La longueur du côté multipliée par elle-même", "isCorrect": False},
                        {"text": "La longueur du côté multipliée par deux", "isCorrect": False},
                        {"text": "La longueur du côté additionnée à deux", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le périmètre est la longueur du contour. Pour un carré, les 4 côtés sont égaux, donc P = c + c + c + c = 4 x c."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment calcule-t-on l'aire (la surface) d'un rectangle ?",
                    "answerOptions": [
                        {"text": "La longueur multipliée par la largeur", "isCorrect": True},
                        {"text": "La longueur additionnée à la largeur", "isCorrect": False},
                        {"text": "Le double de la somme longueur et largeur", "isCorrect": False},
                        {"text": "La longueur divisée par la largeur totale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'aire d'un rectangle se calcule en multipliant ses deux dimensions : Longueur (L) x largeur (l). Le résultat s'exprime en unités de surface (cm², m², etc.)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la somme des angles d'un triangle quelconque ?",
                    "answerOptions": [
                        {"text": "Un total de cent-quatre-vingts degrés", "isCorrect": True},
                        {"text": "Un total de quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Un total de trois-cent-soixante degrés", "isCorrect": False},
                        {"text": "Un total de cent degrés exactement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une propriété fondamentale de la géométrie : dans n'importe quel triangle, si on additionne la mesure des trois angles, on obtient toujours 180°."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on un triangle possédant un angle droit (90°) ?",
                    "answerOptions": [
                        {"text": "Un triangle de type rectangle", "isCorrect": True},
                        {"text": "Un triangle de type isocèle", "isCorrect": False},
                        {"text": "Un triangle de type équilatéral", "isCorrect": False},
                        {"text": "Un triangle de type quelconque", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un triangle rectangle possède un angle de 90°. Le côté opposé à cet angle s'appelle l'hypoténuse. On utilise le théorème de Pythagore dans ce type de triangle."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la valeur approximative du nombre Pi ?",
                    "answerOptions": [
                        {"text": "La valeur décimale de trois virgule quatorze", "isCorrect": True},
                        {"text": "La valeur décimale de deux virgule sept", "isCorrect": False},
                        {"text": "La valeur entière simple de trois", "isCorrect": False},
                        {"text": "La valeur décimale de trois virgule vingt", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pi (π) est un nombre irrationnel. On utilise généralement la valeur approchée 3,14 pour calculer le périmètre (2πR) ou l'aire (πR²) d'un cercle."
                },
                {
                    "questionNumber": 26,
                    "question": "Un triangle équilatéral possède :",
                    "answerOptions": [
                        {"text": "Trois côtés de même longueur exactement", "isCorrect": True},
                        {"text": "Deux côtés de même longueur uniquement", "isCorrect": False},
                        {"text": "Un angle droit de quatre-vingt-dix degrés", "isCorrect": False},
                        {"text": "Trois côtés de longueurs toutes différentes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans un triangle équilatéral, tous les côtés sont égaux et tous les angles mesurent 60°. Il possède trois axes de symétrie."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le périmètre d'un cercle de rayon 5 cm (utiliser Pi = 3) ?",
                    "answerOptions": [
                        {"text": "Une longueur totale de trente centimètres", "isCorrect": True},
                        {"text": "Une longueur totale de quinze centimètres", "isCorrect": False},
                        {"text": "Une longueur totale de soixante centimètres", "isCorrect": False},
                        {"text": "Une longueur totale de dix centimètres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Formule du périmètre : 2 x π x R. Calcul : 2 x 3 x 5 = 30 cm. Si on utilisait la valeur précise de Pi, on obtiendrait environ 31,4 cm."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment calcule-t-on l'aire d'un triangle ?",
                    "answerOptions": [
                        {"text": "La base multipliée par la hauteur divisée par deux", "isCorrect": True},
                        {"text": "La base multipliée simplement par la hauteur", "isCorrect": False},
                        {"text": "La somme des trois côtés du triangle", "isCorrect": False},
                        {"text": "La base additionnée à la hauteur totale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'aire d'un triangle correspond à la moitié de l'aire du rectangle qui le contiendrait. Formule : (Base x Hauteur) / 2."
                },
                {
                    "questionNumber": 29,
                    "question": "Dans un rectangle de 10 cm sur 4 cm, quel est le périmètre ?",
                    "answerOptions": [
                        {"text": "Vingt-huit centimètres au total", "isCorrect": True},
                        {"text": "Quarante centimètres au total", "isCorrect": False},
                        {"text": "Quatorze centimètres au total", "isCorrect": False},
                        {"text": "Vingt centimètres au total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le périmètre du rectangle est P = (Longueur + largeur) x 2. Calcul : (10 + 4) x 2 = 14 x 2 = 28 cm."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle est l'aire d'un carré de 6 cm de côté ?",
                    "answerOptions": [
                        {"text": "Trente-six centimètres carrés de surface", "isCorrect": True},
                        {"text": "Vingt-quatre centimètres carrés de surface", "isCorrect": False},
                        {"text": "Douze centimètres carrés de surface", "isCorrect": False},
                        {"text": "Trente centimètres carrés de surface", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'aire du carré est Aire = Côté x Côté (ou Côté²). Calcul : 6 cm x 6 cm = 36 cm²."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment appelle-t-on un polygone à 4 côtés dont les côtés opposés sont parallèles ?",
                    "answerOptions": [
                        {"text": "Un quadrilatère de type parallélogramme", "isCorrect": True},
                        {"text": "Un triangle de type rectangle", "isCorrect": False},
                        {"text": "Un hexagone de type régulier", "isCorrect": False},
                        {"text": "Un cercle de type géométrique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le parallélogramme a ses côtés opposés parallèles et de même longueur. Le rectangle, le losange et le carré sont des parallélogrammes particuliers."
                },
                {
                    "questionNumber": 32,
                    "question": "Combien de côtés possède un hexagone ?",
                    "answerOptions": [
                        {"text": "Un total de six côtés", "isCorrect": True},
                        {"text": "Un total de huit côtés", "isCorrect": False},
                        {"text": "Un total de cinq côtés", "isCorrect": False},
                        {"text": "Un total de quatre côtés", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 'Hexa' signifie 6 en grec. Un hexagone est donc une figure plane à 6 côtés. La France est souvent appelée l'Hexagone à cause de sa forme géographique."
                },
                {
                    "questionNumber": 33,
                    "question": "Dans un triangle rectangle, le théorème de Pythagore s'écrit :",
                    "answerOptions": [
                        {"text": "a² + b² = c² (c étant l'hypoténuse)", "isCorrect": True},
                        {"text": "a + b = c (c étant l'hypoténuse)", "isCorrect": False},
                        {"text": "a x b = c (c étant l'hypoténuse)", "isCorrect": False},
                        {"text": "a² - b² = c² (c étant l'hypoténuse)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pythagore énonce que le carré de la longueur de l'hypoténuse est égal à la somme des carrés des longueurs des deux autres côtés."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la mesure d'un angle droit ?",
                    "answerOptions": [
                        {"text": "Une mesure de quatre-vingt-dix degrés", "isCorrect": True},
                        {"text": "Une mesure de cent-quatre-vingts degrés", "isCorrect": False},
                        {"text": "Une mesure de quarante-cinq degrés", "isCorrect": False},
                        {"text": "Une mesure de zéro degré exactement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un angle droit est formé par deux droites perpendiculaires. Il correspond au quart d'un tour complet de cercle (360 / 4 = 90)."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment appelle-t-on le segment qui relie le centre au bord d'un cercle ?",
                    "answerOptions": [
                        {"text": "Le rayon du cercle", "isCorrect": True},
                        {"text": "Le diamètre du cercle", "isCorrect": False},
                        {"text": "La corde du cercle", "isCorrect": False},
                        {"text": "L'arc du cercle", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le rayon (R) est la distance constante entre le centre et n'importe quel point du cercle. Le diamètre (D) est égal à deux fois le rayon (D = 2R)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est l'aire d'un disque de rayon 10 cm (utiliser Pi = 3,14) ?",
                    "answerOptions": [
                        {"text": "Trois cent quatorze centimètres carrés", "isCorrect": True},
                        {"text": "Trente et un virgule quatre centimètres carrés", "isCorrect": False},
                        {"text": "Soixante-deux virgule huit centimètres carrés", "isCorrect": False},
                        {"text": "Cent centimètres carrés exactement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Formule de l'aire du disque : π x R². Calcul : 3,14 x 10² = 3,14 x 100 = 314 cm²."
                },
                {
                    "questionNumber": 37,
                    "question": "Qu'est-ce qu'un angle obtus ?",
                    "answerOptions": [
                        {"text": "Un angle supérieur à 90 degrés", "isCorrect": True},
                        {"text": "Un angle inférieur à 90 degrés", "isCorrect": False},
                        {"text": "Un angle égal à 90 degrés exactement", "isCorrect": False},
                        {"text": "Un angle qui mesure zéro degré", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un angle est dit 'obtus' si sa mesure est comprise entre 90° et 180°. S'il est plus petit que 90°, il est dit 'aigu'."
                },
                {
                    "questionNumber": 38,
                    "question": "Un rectangle a un périmètre de 20 cm. Si sa longueur est 6 cm, quelle est sa largeur ?",
                    "answerOptions": [
                        {"text": "Une largeur de quatre centimètres", "isCorrect": True},
                        {"text": "Une largeur de quatorze centimètres", "isCorrect": False},
                        {"text": "Une largeur de huit centimètres", "isCorrect": False},
                        {"text": "Une largeur de dix centimètres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Demi-périmètre (L+l) = 20 / 2 = 10 cm. Si la longueur L = 6, alors la largeur l = 10 - 6 = 4 cm."
                },
                {
                    "questionNumber": 39,
                    "question": "Comment appelle-t-on un polygone à 3 côtés ?",
                    "answerOptions": [
                        {"text": "Un triangle géométrique", "isCorrect": True},
                        {"text": "Un quadrilatère géométrique", "isCorrect": False},
                        {"text": "Un cercle géométrique", "isCorrect": False},
                        {"text": "Un pentagone géométrique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le triangle est le polygone ayant le plus petit nombre de côtés. Il possède également trois sommets et trois angles."
                },
                {
                    "questionNumber": 40,
                    "question": "Que signifie 'perpendiculaire' en géométrie ?",
                    "answerOptions": [
                        {"text": "Qui se croise en formant un angle droit", "isCorrect": True},
                        {"text": "Qui ne se croise jamais à l'infini", "isCorrect": False},
                        {"text": "Qui a exactement la même longueur", "isCorrect": False},
                        {"text": "Qui est tracé avec un compas seul", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Deux droites sont perpendiculaires si elles se coupent en formant quatre angles de 90°. On utilise l'équerre pour vérifier la perpendicularité."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : STATISTIQUES ET PROBABILITÉS (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : STATISTIQUES ET PROBABILITÉS",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la définition de la 'moyenne' d'une série statistique ?",
                    "answerOptions": [
                        {"text": "La somme des valeurs divisée par l'effectif total", "isCorrect": True},
                        {"text": "La valeur située exactement au milieu de la série", "isCorrect": False},
                        {"text": "La valeur qui apparaît le plus souvent dans la série", "isCorrect": False},
                        {"text": "La différence entre le maximum et le minimum", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La moyenne est l'indicateur de tendance centrale le plus utilisé. On additionne toutes les données collectées et on divise le résultat par le nombre total d'individus (N)."
                },
                {
                    "questionNumber": 42,
                    "question": "On lance un dé à 6 faces. Quelle est la probabilité d'obtenir le chiffre 4 ?",
                    "answerOptions": [
                        {"text": "Une chance sur six issues possibles", "isCorrect": True},
                        {"text": "Quatre chances sur six issues possibles", "isCorrect": False},
                        {"text": "Une chance sur quatre issues possibles", "isCorrect": False},
                        {"text": "Six chances sur six issues possibles", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour un dé équilibré, chaque face a la même chance de sortir. Il y a 1 résultat favorable (le 4) sur 6 résultats possibles au total. La probabilité est donc 1/6."
                },
                {
                    "questionNumber": 43,
                    "question": "Qu'est-ce que l'étendue d'une série statistique ?",
                    "answerOptions": [
                        {"text": "L'écart entre la valeur maximale et minimale", "isCorrect": True},
                        {"text": "La valeur moyenne de l'ensemble des données", "isCorrect": False},
                        {"text": "Le nombre total d'individus dans l'échantillon", "isCorrect": False},
                        {"text": "Le pourcentage de réussite à l'expérience", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'étendue mesure la dispersion des données. Elle se calcule en faisant : Plus grande valeur - Plus petite valeur. Une étendue faible signifie que les données sont proches les unes des autres."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la probabilité d'un événement impossible ?",
                    "answerOptions": [
                        {"text": "Une probabilité égale à zéro", "isCorrect": True},
                        {"text": "Une probabilité égale à un", "isCorrect": False},
                        {"text": "Une probabilité égale à zéro virgule cinq", "isCorrect": False},
                        {"text": "Une probabilité de cent pour cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** En mathématiques, la probabilité d'un événement est un nombre compris entre 0 et 1. Si l'événement ne peut jamais se produire, sa probabilité est de 0 (soit 0 %)."
                },
                {
                    "questionNumber": 45,
                    "question": "Dans un sondage, qu'est-ce que l'effectif total ?",
                    "answerOptions": [
                        {"text": "Le nombre total de personnes interrogées", "isCorrect": True},
                        {"text": "La moyenne d'âge des personnes du groupe", "isCorrect": False},
                        {"text": "La réponse la plus fréquente donnée au test", "isCorrect": False},
                        {"text": "La différence entre les hommes et les femmes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'effectif total (souvent noté N) correspond à la somme de tous les effectifs individuels. C'est la taille globale de la population ou de l'échantillon étudié."
                },
                {
                    "questionNumber": 46,
                    "question": "On tire une carte dans un jeu de 32 cartes. Quelle est la probabilité de tirer un cœur ?",
                    "answerOptions": [
                        {"text": "Huit chances sur trente-deux issues", "isCorrect": True},
                        {"text": "Une chance sur trente-deux issues", "isCorrect": False},
                        {"text": "Quatre chances sur trente-deux issues", "isCorrect": False},
                        {"text": "Huit chances sur cinquante-deux issues", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans un jeu de 32 cartes, il y a 4 couleurs (Cœur, Carreau, Pique, Trèfle) avec 8 cartes par couleur. La probabilité de tirer un cœur est de 8/32, ce qui se simplifie en 1/4 (25 %)."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on la valeur qui apparaît le plus souvent dans une série ?",
                    "answerOptions": [
                        {"text": "Le mode de la série statistique", "isCorrect": True},
                        {"text": "La médiane de la série statistique", "isCorrect": False},
                        {"text": "La moyenne de la série statistique", "isCorrect": False},
                        {"text": "L'indice de la série statistique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le mode est la valeur dont l'effectif est le plus grand. C'est l'indication du résultat le plus fréquent ou le plus 'populaire' dans la distribution."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la somme des probabilités de toutes les issues possibles ?",
                    "answerOptions": [
                        {"text": "La somme est égale à un exactement", "isCorrect": True},
                        {"text": "La somme est égale à zéro exactement", "isCorrect": False},
                        {"text": "La somme est égale à cent exactement", "isCorrect": False},
                        {"text": "La somme est variable selon le type de dé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Comme il est certain que l'un des résultats possibles va se produire, si on additionne les chances de chaque issue, on arrive obligatoirement à 1 (soit 100 % de probabilité)."
                },
                {
                    "questionNumber": 49,
                    "question": "Comment calcule-t-on une fréquence en statistiques ?",
                    "answerOptions": [
                        {"text": "L'effectif de la valeur divisé par l'effectif total", "isCorrect": True},
                        {"text": "L'effectif total divisé par l'effectif de la valeur", "isCorrect": False},
                        {"text": "L'effectif de la valeur multiplié par cent", "isCorrect": False},
                        {"text": "L'effectif total multiplié par la moyenne", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La fréquence f = n / N. C'est un nombre entre 0 et 1 qui exprime la part de la valeur dans la population. On multiplie par 100 pour l'avoir en pourcentage."
                },
                {
                    "questionNumber": 50,
                    "question": "Qu'est-ce qu'une expérience aléatoire ?",
                    "answerOptions": [
                        {"text": "Une expérience dont on ne peut prédire le résultat", "isCorrect": True},
                        {"text": "Une expérience réalisée avec une règle précise", "isCorrect": False},
                        {"text": "Un calcul mathématique sans aucune erreur", "isCorrect": False},
                        {"text": "Une enquête faite uniquement par téléphone", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une expérience est aléatoire si on connaît toutes les issues possibles (ex: 1, 2, 3, 4, 5, 6 au dé) mais qu'il est impossible de savoir laquelle va sortir avant de réaliser l'expérience."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la probabilité d'obtenir 'Pile' lors d'un lancer de pièce ?",
                    "answerOptions": [
                        {"text": "Une probabilité égale à zéro virgule cinq", "isCorrect": True},
                        {"text": "Une probabilité égale à un entier", "isCorrect": False},
                        {"text": "Une probabilité égale à zéro virgule vingt-cinq", "isCorrect": False},
                        {"text": "Une probabilité égale à zéro virgule un", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Sur une pièce équilibrée, il y a 2 issues possibles (Pile ou Face). Chaque issue a 1 chance sur 2. En décimal, 1/2 = 0,5 (ou 50 %)."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment calcule-t-on la moyenne de ces trois notes : 10, 12, 14 ?",
                    "answerOptions": [
                        {"text": "La moyenne est égale à douze", "isCorrect": True},
                        {"text": "La moyenne est égale à trente-six", "isCorrect": False},
                        {"text": "La moyenne est égale à dix", "isCorrect": False},
                        {"text": "La moyenne est égale à onze", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On fait la somme : 10 + 12 + 14 = 36. On divise par le nombre de notes : 36 / 3 = 12. La moyenne est donc 12."
                },
                {
                    "questionNumber": 53,
                    "question": "Que représente un diagramme à bâtons en statistiques ?",
                    "answerOptions": [
                        {"text": "La répartition des effectifs par catégorie", "isCorrect": True},
                        {"text": "La météo des jours de la semaine locale", "isCorrect": False},
                        {"text": "Le prix total de tous les articles vendus", "isCorrect": False},
                        {"text": "La longueur du trajet parcouru en voiture", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans ce graphique, la hauteur de chaque bâton est proportionnelle à l'effectif (ou à la fréquence) de la valeur représentée. Cela permet de comparer visuellement les données."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la probabilité d'un événement certain ?",
                    "answerOptions": [
                        {"text": "La valeur de la probabilité est égale à un", "isCorrect": True},
                        {"text": "La valeur de la probabilité est égale à zéro", "isCorrect": False},
                        {"text": "La valeur de la probabilité est de cinquante", "isCorrect": False},
                        {"text": "La valeur de la probabilité est infinie", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un événement certain se produit dans tous les cas. Sa probabilité est donc maximale, soit 1 (ce qui correspond à 100 % de chances)."
                },
                {
                    "questionNumber": 55,
                    "question": "Dans une série statistique, la médiane est la valeur qui :",
                    "answerOptions": [
                        {"text": "Partage la série en deux effectifs égaux", "isCorrect": True},
                        {"text": "Correspond à la moyenne des valeurs totales", "isCorrect": False},
                        {"text": "Est la plus grande valeur de l'ensemble", "isCorrect": False},
                        {"text": "A été calculée par une multiplication complexe", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour trouver la médiane, on range d'abord les valeurs dans l'ordre croissant. La médiane est la valeur du milieu : il y a autant de données plus petites que de données plus grandes."
                },
                {
                    "questionNumber": 56,
                    "question": "Si un sac contient 3 billes rouges et 7 billes bleues, quelle est la probabilité de tirer une bille rouge ?",
                    "answerOptions": [
                        {"text": "La probabilité est de zéro virgule trois", "isCorrect": True},
                        {"text": "La probabilité est de zéro virgule sept", "isCorrect": False},
                        {"text": "La probabilité est de trois virgule zéro", "isCorrect": False},
                        {"text": "La probabilité est de un sur trois", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Nombre total de billes = 3 + 7 = 10. Billes rouges favorables = 3. Probabilité = 3/10 = 0,3 (soit 30 %)."
                },
                {
                    "questionNumber": 57,
                    "question": "Que signifie un pourcentage de 100 % pour un effectif ?",
                    "answerOptions": [
                        {"text": "La totalité de la population concernée", "isCorrect": True},
                        {"text": "La moitié de la population concernée", "isCorrect": False},
                        {"text": "Une personne seule dans le groupe", "isCorrect": False},
                        {"text": "C'est une erreur de calcul impossible", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 100 % correspond à la fraction 100/100, soit l'unité entière. Cela désigne donc tous les individus de la série sans exception."
                },
                {
                    "questionNumber": 58,
                    "question": "Sur un diagramme circulaire, la somme des secteurs vaut toujours :",
                    "answerOptions": [
                        {"text": "Un total de cent pour cent", "isCorrect": True},
                        {"text": "Un total de cinquante pour cent", "isCorrect": False},
                        {"text": "Un total de trois-cent-soixante pour cent", "isCorrect": False},
                        {"text": "Un total égal à la moyenne arithmétique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le disque entier représente la totalité de l'effectif (100 %). Les angles des secteurs sont calculés pour que leur somme fasse 360°, mais le total des pourcentages reste 100 %."
                },
                {
                    "questionNumber": 59,
                    "question": "Comment calcule-t-on l'étendue de ces températures : 12°C, 15°C, 22°C ?",
                    "answerOptions": [
                        {"text": "L'étendue est égale à dix degrés", "isCorrect": True},
                        {"text": "L'étendue est égale à vingt-deux degrés", "isCorrect": False},
                        {"text": "L'étendue est égale à douze degrés", "isCorrect": False},
                        {"text": "L'étendue est égale à dix-sept degrés", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On cherche le max (22) et le min (12). On fait la soustraction : 22 - 12 = 10. L'étendue thermique est donc de 10°C."
                },
                {
                    "questionNumber": 60,
                    "question": "On lance un dé. Quel est le contraire de 'obtenir un chiffre pair' ?",
                    "answerOptions": [
                        {"text": "Obtenir un chiffre impair au lancer", "isCorrect": True},
                        {"text": "Obtenir le chiffre deux au lancer", "isCorrect": False},
                        {"text": "Obtenir le chiffre six au lancer", "isCorrect": False},
                        {"text": "Obtenir un chiffre supérieur à quatre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'événement contraire comprend toutes les issues qui ne réalisent pas l'événement initial. Si on ne tire pas un pair (2, 4, 6), on tire forcément un impair (1, 3, 5)."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : ALGÈBRE ET FONCTIONS NUMÉRIQUES (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ALGÈBRE ET FONCTIONS NUMÉRIQUES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la solution de l'équation suivante : x + 5 = 12 ?",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à sept", "isCorrect": True},
                        {"text": "La valeur de x est égale à dix-sept", "isCorrect": False},
                        {"text": "La valeur de x est égale à sept virgule cinq", "isCorrect": False},
                        {"text": "La valeur de x est égale à moins sept", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour isoler x, on déplace le +5 de l'autre côté de l'égalité en changeant son signe. Calcul : x = 12 - 5 = 7. Vérification : 7 + 5 donne bien 12."
                },
                {
                    "questionNumber": 62,
                    "question": "Résoudre l'équation simple : 3x = 15.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à cinq", "isCorrect": True},
                        {"text": "La valeur de x est égale à douze", "isCorrect": False},
                        {"text": "La valeur de x est égale à quarante-cinq", "isCorrect": False},
                        {"text": "La valeur de x est égale à trois", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour isoler x quand il est multiplié par un nombre, on divise de l'autre côté par ce même nombre. Calcul : x = 15 / 3 = 5. Vérification : 3 x 5 = 15."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on l'expression f(x) = ax + b ?",
                    "answerOptions": [
                        {"text": "Une fonction de type affine", "isCorrect": True},
                        {"text": "Une fonction de type linéaire", "isCorrect": False},
                        {"text": "Une fonction de type constante", "isCorrect": False},
                        {"text": "Une fonction de type carrré", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une fonction affine est représentée par une droite qui ne passe pas forcément par l'origine. 'a' est le coefficient directeur (la pente) et 'b' est l'ordonnée à l'origine."
                },
                {
                    "questionNumber": 64,
                    "question": "Dans f(x) = 2x, si x = 4, quelle est la valeur de f(x) ?",
                    "answerOptions": [
                        {"text": "L'image du nombre est égale à huit", "isCorrect": True},
                        {"text": "L'image du nombre est égale à six", "isCorrect": False},
                        {"text": "L'image du nombre est égale à deux", "isCorrect": False},
                        {"text": "L'image du nombre est égale à quatre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Calculer l'image d'un nombre consiste à remplacer x par sa valeur dans la fonction. Calcul : 2 x 4 = 8. On dit que 8 est l'image de 4 par f."
                },
                {
                    "questionNumber": 65,
                    "question": "La représentation graphique d'une fonction linéaire est toujours :",
                    "answerOptions": [
                        {"text": "Une droite passant par l'origine (0,0)", "isCorrect": True},
                        {"text": "Un cercle parfait centré sur l'axe", "isCorrect": False},
                        {"text": "Une courbe en forme de lettre U", "isCorrect": False},
                        {"text": "Une droite horizontale parallèle à l'axe", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une fonction linéaire (type f(x) = ax) traduit une situation de proportionnalité. Sa droite passe obligatoirement par le point (0,0) car si x = 0, alors f(0) = 0."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le résultat de l'opération : (-4) + (-3) ?",
                    "answerOptions": [
                        {"text": "Le résultat est égal à moins sept", "isCorrect": True},
                        {"text": "Le résultat est égal à moins un", "isCorrect": False},
                        {"text": "Le résultat est égal à sept positif", "isCorrect": False},
                        {"text": "Le résultat est égal à douze positif", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Quand on additionne deux nombres négatifs, on additionne leurs valeurs absolues et on garde le signe moins. Calcul : 4 + 3 = 7, donc le résultat est -7."
                },
                {
                    "questionNumber": 67,
                    "question": "Que vaut le produit : (-2) x (-5) ?",
                    "answerOptions": [
                        {"text": "Le résultat est égal à dix positif", "isCorrect": True},
                        {"text": "Le résultat est égal à moins dix", "isCorrect": False},
                        {"text": "Le résultat est égal à moins sept", "isCorrect": False},
                        {"text": "Le résultat est égal à trois positif", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Règle des signes pour la multiplication : le produit de deux nombres de même signe est toujours positif. Calcul : 2 x 5 = 10, et moins par moins donne plus."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle est l'inconnue dans l'équation 4y - 2 = 10 ?",
                    "answerOptions": [
                        {"text": "La lettre y minuscule", "isCorrect": True},
                        {"text": "Le chiffre quatre entier", "isCorrect": False},
                        {"text": "Le nombre dix entier", "isCorrect": False},
                        {"text": "Le signe moins de soustraction", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'inconnue est la lettre (généralement x ou y) dont on cherche la valeur numérique pour que l'égalité soit vraie."
                },
                {
                    "questionNumber": 69,
                    "question": "Réduisez l'expression suivante : 3x + 2x - x.",
                    "answerOptions": [
                        {"text": "L'expression réduite est égale à 4x", "isCorrect": True},
                        {"text": "L'expression réduite est égale à 5x", "isCorrect": False},
                        {"text": "L'expression réduite est égale à 6x", "isCorrect": False},
                        {"text": "L'expression réduite est égale à x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On peut additionner les termes qui ont la même lettre. Calcul : (3 + 2 - 1)x = 4x. Rappelez-vous que '-x' est équivalent à '-1x'."
                },
                {
                    "questionNumber": 70,
                    "question": "Que vaut le carré du nombre 5 (noté 5²) ?",
                    "answerOptions": [
                        {"text": "Le résultat est égal à vingt-cinq", "isCorrect": True},
                        {"text": "Le résultat est égal à dix entier", "isCorrect": False},
                        {"text": "Le résultat est égal à cinquante", "isCorrect": False},
                        {"text": "Le résultat est égal à cinq seulement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Elever un nombre au carré consiste à le multiplier par lui-même. Calcul : 5 x 5 = 25. Ne pas confondre avec 5 x 2."
                },
                {
                    "questionNumber": 71,
                    "question": "Résoudre : 2x + 1 = 9.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à quatre", "isCorrect": True},
                        {"text": "La valeur de x est égale à huit", "isCorrect": False},
                        {"text": "La valeur de x est égale à cinq", "isCorrect": False},
                        {"text": "La valeur de x est égale à trois", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 1) 2x = 9 - 1 = 8. 2) x = 8 / 2 = 4. La solution de l'équation est 4."
                },
                {
                    "questionNumber": 72,
                    "question": "Si a = 3 et b = 4, que vaut a + 2b ?",
                    "answerOptions": [
                        {"text": "La valeur totale est égale à onze", "isCorrect": True},
                        {"text": "La valeur totale est égale à quatorze", "isCorrect": False},
                        {"text": "La valeur totale est égale à dix", "isCorrect": False},
                        {"text": "La valeur totale est égale à vingt", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On remplace les lettres par les chiffres. Calcul : 3 + (2 x 4) = 3 + 8 = 11. On respecte la priorité de la multiplication."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est l'inverse du nombre 2 ?",
                    "answerOptions": [
                        {"text": "Le nombre décimal zéro virgule cinq", "isCorrect": True},
                        {"text": "Le nombre entier négatif moins deux", "isCorrect": False},
                        {"text": "Le nombre entier égale à quatre", "isCorrect": False},
                        {"text": "Le nombre entier égale à un", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'inverse d'un nombre x est 1/x. Pour 2, l'inverse est 1/2, soit 0,5 en écriture décimale."
                },
                {
                    "questionNumber": 74,
                    "question": "Que signifie graphiquement une fonction croissante ?",
                    "answerOptions": [
                        {"text": "La courbe monte de gauche à droite", "isCorrect": True},
                        {"text": "La courbe descend de gauche à droite", "isCorrect": False},
                        {"text": "La courbe est une ligne plate horizontale", "isCorrect": False},
                        {"text": "La courbe forme un cercle fermé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une fonction est croissante si, lorsque les valeurs de x augmentent, les valeurs de y augmentent également. La pente de la droite (ou de la tangente) est alors positive."
                },
                {
                    "questionNumber": 75,
                    "question": "Dans f(x) = 3x + 1, quel est le nom du nombre '1' ?",
                    "answerOptions": [
                        {"text": "L'ordonnée à l'origine de la droite", "isCorrect": True},
                        {"text": "Le coefficient directeur de la droite", "isCorrect": False},
                        {"text": "L'image du chiffre trois par la fonction", "isCorrect": False},
                        {"text": "La racine carrée de l'expression", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans f(x) = ax + b, 'b' est l'ordonnée à l'origine. C'est la valeur de y au point où la droite coupe l'axe vertical (quand x = 0)."
                },
                {
                    "questionNumber": 76,
                    "question": "Résoudre : x / 2 = 10.",
                    "answerOptions": [
                        {"text": "La valeur de x est égale à vingt", "isCorrect": True},
                        {"text": "La valeur de x est égale à cinq", "isCorrect": False},
                        {"text": "La valeur de x est égale à huit", "isCorrect": False},
                        {"text": "La valeur de x est égale à douze", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'opération inverse de la division est la multiplication. On multiplie 10 par 2 pour isoler x. Calcul : x = 10 x 2 = 20."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est la valeur de x² si x = -4 ?",
                    "answerOptions": [
                        {"text": "Le résultat est égal à seize positif", "isCorrect": True},
                        {"text": "Le résultat est égal à moins seize", "isCorrect": False},
                        {"text": "Le résultat est égal à huit positif", "isCorrect": False},
                        {"text": "Le résultat est égal à moins huit", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** (-4)² = (-4) x (-4). Moins par moins donne plus. Le carré d'un nombre réel est toujours positif. Le résultat est donc 16."
                },
                {
                    "questionNumber": 78,
                    "question": "Comment écrit-on 'le triple de x' ?",
                    "answerOptions": [
                        {"text": "L'expression algébrique 3x", "isCorrect": True},
                        {"text": "L'expression algébrique x + 3", "isCorrect": False},
                        {"text": "L'expression algébrique x³", "isCorrect": False},
                        {"text": "L'expression algébrique x / 3", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le triple signifie multiplier par 3. 'x + 3' est l'augmentation de 3 et 'x³' est le cube de x."
                },
                {
                    "questionNumber": 79,
                    "question": "Développer l'expression : 2(x + 3).",
                    "answerOptions": [
                        {"text": "L'expression développée est 2x + 6", "isCorrect": True},
                        {"text": "L'expression développée est 2x + 3", "isCorrect": False},
                        {"text": "L'expression développée est x + 6", "isCorrect": False},
                        {"text": "L'expression développée est 5x", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On utilise la distributivité : on multiplie le chiffre 2 par chaque terme dans la parenthèse. Calcul : (2 x x) + (2 x 3) = 2x + 6."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la valeur de 10 puissance 3 (10³) ?",
                    "answerOptions": [
                        {"text": "Le résultat est égal à mille", "isCorrect": True},
                        {"text": "Le résultat est égal à cent", "isCorrect": False},
                        {"text": "Le résultat est égal à trente", "isCorrect": False},
                        {"text": "Le résultat est égal à dix mille", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 10³ = 10 x 10 x 10 = 1 000. L'exposant indique le nombre de zéros à placer après le 1."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : UNITÉS DE MESURE ET GRANDEURS PHYSIQUES (Q81 à Q100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : UNITÉS DE MESURE ET GRANDEURS PHYSIQUES",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Combien y a-t-il de grammes dans un kilogramme ?",
                    "answerOptions": [
                        {"text": "Un total de mille grammes", "isCorrect": True},
                        {"text": "Un total de cent grammes", "isCorrect": False},
                        {"text": "Un total de dix grammes", "isCorrect": False},
                        {"text": "Un total de dix mille grammes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le préfixe 'kilo' signifie mille. C'est l'unité de base de masse dans le système international. Pour convertir des kg en g, on multiplie par 1000."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle unité utilise-t-on pour mesurer une intensité électrique ?",
                    "answerOptions": [
                        {"text": "L'unité nommée l'Ampère (A)", "isCorrect": True},
                        {"text": "L'unité nommée le Volt (V)", "isCorrect": False},
                        {"text": "L'unité nommée le Watt (W)", "isCorrect": False},
                        {"text": "L'unité nommée l'Ohm (Ω)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'intensité (débit d'électrons) se mesure en Ampères. Le Volt mesure la tension et le Watt mesure la puissance."
                },
                {
                    "questionNumber": 83,
                    "question": "Combien de minutes y a-t-il dans 2 heures et demie ?",
                    "answerOptions": [
                        {"text": "Un total de cent cinquante minutes", "isCorrect": True},
                        {"text": "Un total de cent vingt minutes", "isCorrect": False},
                        {"text": "Un total de cent trente minutes", "isCorrect": False},
                        {"text": "Un total de deux cent cinquante minutes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 1 heure = 60 minutes. Donc 2 heures = 120 minutes. Une demi-heure = 30 minutes. Calcul : 120 + 30 = 150 minutes."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est l'unité de mesure de la puissance électrique ?",
                    "answerOptions": [
                        {"text": "L'unité nommée le Watt (W)", "isCorrect": True},
                        {"text": "L'unité nommée le Joule (J)", "isCorrect": False},
                        {"text": "L'unité nommée le Litre (L)", "isCorrect": False},
                        {"text": "L'unité nommée le Mètre (m)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La puissance électrique (P) est le produit de la tension par l'intensité (P = U x I). Elle s'exprime en Watts. On l'utilise pour indiquer la consommation des appareils."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment convertit-on des centimètres en millimètres ?",
                    "answerOptions": [
                        {"text": "On multiplie la valeur par dix", "isCorrect": True},
                        {"text": "On divise la valeur par dix", "isCorrect": False},
                        {"text": "On multiplie la valeur par cent", "isCorrect": False},
                        {"text": "On divise la valeur par cent", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Dans le tableau des longueurs, le millimètre est l'unité juste à droite du centimètre. Pour passer de l'un à l'autre, on multiplie donc par 10. Exemple : 5 cm = 50 mm."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est la masse de 1 litre d'eau pure ?",
                    "answerOptions": [
                        {"text": "Une masse égale à un kilogramme", "isCorrect": True},
                        {"text": "Une masse égale à cent grammes", "isCorrect": False},
                        {"text": "Une masse égale à dix kilogrammes", "isCorrect": False},
                        {"text": "Une masse égale à un gramme seul", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une correspondance de référence : 1 dm³ d'eau = 1 litre = 1 kg. Attention, cette égalité n'est vraie que pour l'eau (la densité de l'huile ou du métal est différente)."
                },
                {
                    "questionNumber": 87,
                    "question": "Combien de secondes y a-t-il dans une minute ?",
                    "answerOptions": [
                        {"text": "Un total de soixante secondes", "isCorrect": True},
                        {"text": "Un total de cent secondes", "isCorrect": False},
                        {"text": "Un total de trente secondes", "isCorrect": False},
                        {"text": "Un total de douze secondes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le système de mesure du temps est sexagésimal (base 60). Une minute vaut 60 secondes et une heure vaut 3600 secondes (60x60)."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est l'unité de mesure d'une surface dans le système international ?",
                    "answerOptions": [
                        {"text": "L'unité nommée le mètre carré", "isCorrect": True},
                        {"text": "L'unité nommée le mètre cube", "isCorrect": False},
                        {"text": "L'unité nommée le mètre linéaire", "isCorrect": False},
                        {"text": "L'unité nommée le kilogramme", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une surface se mesure en deux dimensions (longueur x largeur). L'unité de base est le m². Pour les terrains agricoles, on utilise aussi l'hectare (ha) qui vaut 10 000 m²."
                },
                {
                    "questionNumber": 89,
                    "question": "Convertissez 1,5 kg en grammes.",
                    "answerOptions": [
                        {"text": "Un total de mille cinq cents grammes", "isCorrect": True},
                        {"text": "Un total de cent cinquante grammes", "isCorrect": False},
                        {"text": "Un total de quinze grammes seulement", "isCorrect": False},
                        {"text": "Un total de quinze mille grammes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On multiplie par 1000. Calcul : 1,5 x 1000 = 1500 g. C'est utile pour les recettes de cuisine ou les pesées en atelier."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle unité utilise-t-on pour la tension électrique ?",
                    "answerOptions": [
                        {"text": "L'unité nommée le Volt (V)", "isCorrect": True},
                        {"text": "L'unité nommée l'Ampère (A)", "isCorrect": False},
                        {"text": "L'unité nommée l'Ohm (Ω)", "isCorrect": False},
                        {"text": "L'unité nommée le Watt (W)", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La tension électrique (différence de potentiel) se mesure avec un voltmètre branché en dérivation. En France, la tension domestique est de 230 V."
                },
                {
                    "questionNumber": 91,
                    "question": "Combien de millilitres y a-t-il dans un litre ?",
                    "answerOptions": [
                        {"text": "Un total de mille millilitres", "isCorrect": True},
                        {"text": "Un total de cent millilitres", "isCorrect": False},
                        {"text": "Un total de dix millilitres", "isCorrect": False},
                        {"text": "Un total de un millilitre seul", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le préfixe 'milli' signifie millième. Il faut donc 1000 millilitres pour constituer un litre entier. C'est l'équivalent de 1 cm³."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle est l'unité de mesure d'un volume ?",
                    "answerOptions": [
                        {"text": "L'unité nommée le mètre cube", "isCorrect": True},
                        {"text": "L'unité nommée le mètre carré", "isCorrect": False},
                        {"text": "L'unité nommée le mètre linéaire", "isCorrect": False},
                        {"text": "L'unité nommée le kilogramme", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un volume se mesure en trois dimensions (L x l x h). L'unité de référence est le m³. On utilise aussi beaucoup le litre pour les liquides."
                },
                {
                    "questionNumber": 93,
                    "question": "Convertissez 2,5 mètres en centimètres.",
                    "answerOptions": [
                        {"text": "Un total de deux cent cinquante centimètres", "isCorrect": True},
                        {"text": "Un total de vingt-cinq centimètres", "isCorrect": False},
                        {"text": "Un total de deux mille cinq cents centimètres", "isCorrect": False},
                        {"text": "Un total de deux virgule cinq centimètres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Pour passer des mètres aux centimètres, on multiplie par 100 (on décale la virgule de deux rangs vers la droite). Calcul : 2,5 x 100 = 250 cm."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel instrument utilise-t-on pour mesurer une masse ?",
                    "answerOptions": [
                        {"text": "Une balance de précision", "isCorrect": True},
                        {"text": "Une règle graduée plate", "isCorrect": False},
                        {"text": "Un thermomètre à mercure", "isCorrect": False},
                        {"text": "Un rapporteur d'angles", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La balance mesure la masse (en kg ou g). Le pèse-personne ou la balance de cuisine en sont des exemples courants."
                },
                {
                    "questionNumber": 95,
                    "question": "Que mesure-t-on avec un 'chronomètre' ?",
                    "answerOptions": [
                        {"text": "Une durée ou un intervalle de temps", "isCorrect": True},
                        {"text": "La température d'un corps", "isCorrect": False},
                        {"text": "La longueur d'une salle de cours", "isCorrect": False},
                        {"text": "Le poids d'un colis postal", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le chronomètre sert à mesurer le temps écoulé entre un début et une fin. Il est très précis (souvent au centième de seconde près)."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est l'unité de mesure de la température en France ?",
                    "answerOptions": [
                        {"text": "Le degré de type Celsius", "isCorrect": True},
                        {"text": "Le degré de type Fahrenheit", "isCorrect": False},
                        {"text": "L'unité nommée le Kelvin", "isCorrect": False},
                        {"text": "Le degré de type Angle", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** En France et dans la plupart des pays, on utilise l'échelle Celsius (°C). L'eau gèle à 0°C et bout à 100°C (à pression normale)."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle est la conversion fondamentale de capacité ?",
                    "answerOptions": [
                        {"text": "Un litre est égal à un décimètre cube", "isCorrect": True},
                        {"text": "Un litre est égal à un mètre cube", "isCorrect": False},
                        {"text": "Un litre est égal à cent litres cubes", "isCorrect": False},
                        {"text": "Un litre est égal à zéro virgule un litre", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est le lien entre le volume et la capacité : 1 L = 1 dm³. Cela signifie qu'un cube de 10 cm de côté peut contenir exactement 1 litre de liquide."
                },
                {
                    "questionNumber": 98,
                    "question": "Le nombre de sommets d'un cube est de :",
                    "answerOptions": [
                        {"text": "Un total de huit sommets", "isCorrect": True},
                        {"text": "Un total de six sommets", "isCorrect": False},
                        {"text": "Un total de douze sommets", "isCorrect": False},
                        {"text": "Un total de quatre sommets", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Un cube possède 8 coins (sommets), 12 arêtes (les barres) et 6 faces (les carrés qui l'entourent)."
                },
                {
                    "questionNumber": 99,
                    "question": "Pour additionner deux durées, on doit parfois :",
                    "answerOptions": [
                        {"text": "Convertir les minutes en heures dès soixante", "isCorrect": True},
                        {"text": "Convertir systématiquement en secondes pures", "isCorrect": False},
                        {"text": "Multiplier les heures entre elles directement", "isCorrect": False},
                        {"text": "Simplifier le calcul par division finale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Lorsque le total des minutes atteint ou dépasse 60, on doit retrancher 60 aux minutes et ajouter 1 au compteur des heures. Exemple : 1h45 + 30min = 1h75 = 2h15."
                },
                {
                    "questionNumber": 100,
                    "question": "Combien de millimètres y a-t-il dans un mètre ?",
                    "answerOptions": [
                        {"text": "Un total de mille millimètres", "isCorrect": True},
                        {"text": "Un total de cent millimètres", "isCorrect": False},
                        {"text": "Un total de dix millimètres", "isCorrect": False},
                        {"text": "Un total de dix mille millimètres", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Comme l'indique le nom 'mille-mètre', il faut 1000 petites graduations de mm pour faire un mètre entier. 1 m = 10 dm = 100 cm = 1000 mm."
                }
            ]
        }
    }
}