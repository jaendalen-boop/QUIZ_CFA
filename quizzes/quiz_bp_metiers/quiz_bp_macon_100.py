quiz_data = {
    "title": "Quiz BP Maçon (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : ANALYSE TECHNIQUE ET PRÉPARATION DE CHANTIER (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : ANALYSE TECHNIQUE ET PRÉPARATION DE CHANTIER",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la distance réelle représentée par un trait de 2 centimètres sur un plan à l'échelle 1/50 ?",
                    "answerOptions": [
                        {"text": "1 mètre", "isCorrect": True},
                        {"text": "10 mètres", "isCorrect": False},
                        {"text": "100 millimètres", "isCorrect": False},
                        {"text": "500 centimètres", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/50 signifie que 1 cm sur le plan vaut 50 cm en réalité. Donc 2 cm valent 100 cm, soit 1 mètre."
                },
                {
                    "questionNumber": 2,
                    "question": "Que signifie l'acronyme CCTP dans un dossier de marché ?",
                    "answerOptions": [
                        {"text": "Cahier des Clauses Techniques Particulières", "isCorrect": True},
                        {"text": "Cahier des Charges de Travaux Publics", "isCorrect": False},
                        {"text": "Certificat de Conformité Technique Provisoire", "isCorrect": False},
                        {"text": "Contrôle de Construction Technique et Physique", "isCorrect": False}
                    ],
                    "correction": "Le CCTP est la pièce écrite contractuelle qui décrit les dispositions techniques de chaque lot (matériaux, mise en œuvre, normes)."
                },
                {
                    "questionNumber": 3,
                    "question": "Sur un plan de coffrage, que désigne une cote indiquée 'entre nus bruts' ?",
                    "answerOptions": [
                        {"text": "La dimension de la paroi sans les enduits ni les revêtements", "isCorrect": True},
                        {"text": "La distance totale incluant l'épaisseur de l'isolation et du doublage", "isCorrect": False},
                        {"text": "La mesure prise entre les axes des murs porteurs", "isCorrect": False},
                        {"text": "La hauteur sous plafond une fois le sol fini posé", "isCorrect": False}
                    ],
                    "correction": "Une cote brute en maçonnerie correspond à la dimension de l'élément porteur seul (béton ou maçonnerie), avant l'application des finitions (enduits, isolation)."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel trait est normalisé pour représenter les axes de symétrie ou les files de construction ?",
                    "answerOptions": [
                        {"text": "Mixte fin", "isCorrect": True},
                        {"text": "Continu fort", "isCorrect": False},
                        {"text": "Interrompu fin", "isCorrect": False},
                        {"text": "Continu fin", "isCorrect": False}
                    ],
                    "correction": "Le trait mixte fin (une alternance de traits longs et courts) est utilisé pour les axes, les plans de symétrie et les trajectoires."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel instrument est indispensable pour vérifier la planéité horizontale d'une dalle sur une grande surface ?",
                    "answerOptions": [
                        {"text": "Niveau optique", "isCorrect": True},
                        {"text": "Équerre de maçon", "isCorrect": False},
                        {"text": "Fil à plomb", "isCorrect": False},
                        {"text": "Décamètre", "isCorrect": False}
                    ],
                    "correction": "Le niveau optique (ou niveau de chantier) permet de réaliser des visées horizontales précises sur de longues distances pour contrôler l'altimétrie et la planéité."
                },
                {
                    "questionNumber": 6,
                    "question": "Dans le système NGF, que matérialise le 'point zéro' de référence ?",
                    "answerOptions": [
                        {"text": "Le niveau moyen de la mer à Marseille", "isCorrect": True},
                        {"text": "Le niveau du sol naturel du chantier", "isCorrect": False},
                        {"text": "Le point le plus haut du bâtiment", "isCorrect": False},
                        {"text": "Le seuil de la porte d'entrée principale", "isCorrect": False}
                    ],
                    "correction": "Le Nivellement Général de la France (NGF) a pour origine le marégraphe de Marseille, qui définit l'altitude zéro de référence."
                },
                {
                    "questionNumber": 7,
                    "question": "Comment se nomme l'augmentation de volume d'une terre foisonnée après son extraction ?",
                    "answerOptions": [
                        {"text": "Le foisonnement", "isCorrect": True},
                        {"text": "La compacité", "isCorrect": False},
                        {"text": "La densité", "isCorrect": False},
                        {"text": "La porosité", "isCorrect": False}
                    ],
                    "correction": "Lorsqu'on excave de la terre, elle perd sa cohésion et occupe plus de volume qu'en place. Ce phénomène est le foisonnement."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle méthode empirique permet de vérifier rapidement l'angle droit d'une implantation sur le terrain ?",
                    "answerOptions": [
                        {"text": "3 4 5", "isCorrect": True},
                        {"text": "1 2 3", "isCorrect": False},
                        {"text": "Pi R 2", "isCorrect": False},
                        {"text": "A B C", "isCorrect": False}
                    ],
                    "correction": "La règle du '3-4-5' (théorème de Pythagore) permet de créer un angle droit : un triangle dont les côtés mesurent 3m, 4m et 5m possède obligatoirement un angle droit."
                },
                {
                    "questionNumber": 9,
                    "question": "Que représente le Plan d'Installation de Chantier (PIC) ?",
                    "answerOptions": [
                        {"text": "Un plan définissant les zones de stockage, les accès et les moyens de levage", "isCorrect": True},
                        {"text": "Un document détaillant exclusivement le ferraillage des ouvrages en béton armé", "isCorrect": False},
                        {"text": "Une coupe technique montrant la composition des planchers et des murs", "isCorrect": False},
                        {"text": "Un planning financier des décomptes mensuels des travaux", "isCorrect": False}
                    ],
                    "correction": "Le PIC organise la logistique du chantier (clôture, grue, base vie, réseaux, circulations) pour assurer la sécurité et l'efficacité avant le démarrage."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est l'unité de mesure conventionnelle pour quantifier des fondations en rigole dans un devis ?",
                    "answerOptions": [
                        {"text": "Mètre cube", "isCorrect": True},
                        {"text": "Mètre carré", "isCorrect": False},
                        {"text": "Mètre linéaire", "isCorrect": False},
                        {"text": "Forfait", "isCorrect": False}
                    ],
                    "correction": "Les fouilles et le béton de fondations (semelles filantes) se quantifient généralement au volume, donc en mètres cubes (m3)."
                },
                {
                    "questionNumber": 11,
                    "question": "Sur une coupe verticale, comment appelle-t-on la partie de maçonnerie située sous la fenêtre ?",
                    "answerOptions": [
                        {"text": "Allège", "isCorrect": True},
                        {"text": "Linteau", "isCorrect": False},
                        {"text": "Jambage", "isCorrect": False},
                        {"text": "Imposte", "isCorrect": False}
                    ],
                    "correction": "L'allège est le mur d'appui situé entre le sol fini et la pièce d'appui de la fenêtre."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la fonction principale d'une 'chaise d'implantation' ?",
                    "answerOptions": [
                        {"text": "Matérialiser les axes et les nus des murs hors de la zone de terrassement", "isCorrect": True},
                        {"text": "Servir de support pour le stockage des palettes de parpaings", "isCorrect": False},
                        {"text": "Permettre le repos des ouvriers lors des pauses réglementaires", "isCorrect": False},
                        {"text": "Soutenir les banches de coffrage lors du coulage du béton", "isCorrect": False}
                    ],
                    "correction": "Les chaises sont des chevalets en bois plantés à l'extérieur de l'emprise du bâtiment pour tendre les cordeaux d'alignement sans être gênés par les travaux."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel document spécifique doit être établi pour coordonner la sécurité lorsque plusieurs entreprises interviennent ?",
                    "answerOptions": [
                        {"text": "Le PPSPS", "isCorrect": True},
                        {"text": "Le DUK", "isCorrect": False},
                        {"text": "Le RIB", "isCorrect": False},
                        {"text": "Le DOE", "isCorrect": False}
                    ],
                    "correction": "Le Plan Particulier de Sécurité et de Protection de la Santé (PPSPS) analyse les risques spécifiques au chantier et les mesures de prévention adoptées."
                },
                {
                    "questionNumber": 14,
                    "question": "Que signifie l'abréviation 'TN' sur un plan de masse ou de terrassement ?",
                    "answerOptions": [
                        {"text": "Terrain Naturel", "isCorrect": True},
                        {"text": "Trait de Niveau", "isCorrect": False},
                        {"text": "Terre Nettoyée", "isCorrect": False},
                        {"text": "Travaux Neufs", "isCorrect": False}
                    ],
                    "correction": "TN désigne le niveau du sol existant avant toute intervention ou modification par l'entreprise."
                },
                {
                    "questionNumber": 15,
                    "question": "Pour calculer la surface d'un pignon triangulaire, quelle formule utilise-t-on ?",
                    "answerOptions": [
                        {"text": "Base fois hauteur divisé par deux", "isCorrect": True},
                        {"text": "Base fois hauteur fois épaisseur", "isCorrect": False},
                        {"text": "Longueur plus largeur fois deux", "isCorrect": False},
                        {"text": "Base fois hauteur", "isCorrect": False}
                    ],
                    "correction": "L'aire d'un triangle est (Base x Hauteur) / 2."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le rôle principal du 'calepinage' en maçonnerie ?",
                    "answerOptions": [
                        {"text": "Prévoir l'agencement précis des éléments pour limiter les coupes et soigner l'esthétique", "isCorrect": True},
                        {"text": "Calculer le poids total des aciers nécessaires pour la commande fournisseur", "isCorrect": False},
                        {"text": "Définir le dosage en eau et en ciment pour la fabrication du mortier", "isCorrect": False},
                        {"text": "Organiser le planning des congés payés de l'équipe de chantier", "isCorrect": False}
                    ],
                    "correction": "Le calepinage est le dessin à l'échelle de la disposition des éléments (briques, blocs, carrelage) pour optimiser la pose et éviter les coupes disgracieuses."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle information détermine la profondeur hors-gel des fondations ?",
                    "answerOptions": [
                        {"text": "La zone climatique et l'altitude du lieu de construction", "isCorrect": True},
                        {"text": "La hauteur totale du bâtiment à construire", "isCorrect": False},
                        {"text": "La nature esthétique du revêtement de façade", "isCorrect": False},
                        {"text": "Le type de chauffage choisi par le client", "isCorrect": False}
                    ],
                    "correction": "La profondeur hors-gel dépend de la région (carte des zones de gel) et de l'altitude, pour éviter que le sol ne gonfle sous les fondations en gelant."
                },
                {
                    "questionNumber": 18,
                    "question": "Qu'est-ce qu'une 'rotation de banches' dans l'organisation de chantier ?",
                    "answerOptions": [
                        {"text": "L'organisation cyclique journalière de l'utilisation des coffrages verticaux", "isCorrect": True},
                        {"text": "Le mouvement rotatif de la grue pour distribuer le béton", "isCorrect": False},
                        {"text": "Le remplacement des équipes de maçons toutes les deux semaines", "isCorrect": False},
                        {"text": "Le nettoyage des bétonnières à la fin de la journée", "isCorrect": False}
                    ],
                    "correction": "La rotation correspond au cycle quotidien d'utilisation du matériel de coffrage (ferraillage, fermeture, coulage, décoffrage, nettoyage, déplacement)."
                },
                {
                    "questionNumber": 19,
                    "question": "Sur un plan d'armatures, que signifie le symbole 'HA' ?",
                    "answerOptions": [
                        {"text": "Haute Adhérence", "isCorrect": True},
                        {"text": "Haute Altitude", "isCorrect": False},
                        {"text": "Haute Amplitude", "isCorrect": False},
                        {"text": "Haute Activité", "isCorrect": False}
                    ],
                    "correction": "Les aciers HA (Haute Adhérence) possèdent des reliefs (verrous) pour mieux adhérer au béton, contrairement aux ronds lisses."
                },
                {
                    "questionNumber": 20,
                    "question": "À quoi sert le 'trait de niveau' tracé généralement à 1 mètre du sol fini sur les murs bruts ?",
                    "answerOptions": [
                        {"text": "Servir de référence altimétrique unique pour tous les corps d'état", "isCorrect": True},
                        {"text": "Décorer provisoirement les murs avant la peinture", "isCorrect": False},
                        {"text": "Indiquer la limite de remplissage du béton", "isCorrect": False},
                        {"text": "Marquer l'emplacement des futures prises électriques", "isCorrect": False}
                    ],
                    "correction": "Le trait de niveau (souvent à +1.00m sol fini) est la référence commune pour que le maçon, le menuisier, le plombier et l'électricien positionnent leurs ouvrages à la bonne hauteur."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNOLOGIE DES MATÉRIAUX ET DU BÉTON (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNOLOGIE DES MATÉRIAUX ET DU BÉTON",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le constituant principal du ciment Portland (CEM I) obtenu après cuisson du calcaire et de l'argile ?",
                    "answerOptions": [
                        {"text": "Le clinker", "isCorrect": True},
                        {"text": "Le laitier de haut fourneau", "isCorrect": False},
                        {"text": "La pouzzolane naturelle", "isCorrect": False},
                        {"text": "Le gypse de carrière", "isCorrect": False}
                    ],
                    "correction": "Le clinker est le produit semi-fini obtenu par la cuisson (clinkérisation) à 1450°C d'un mélange de calcaire (80%) et d'argile (20%), base du ciment Portland."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel adjuvant permet d'augmenter la fluidité du béton sans ajouter d'eau ?",
                    "answerOptions": [
                        {"text": "Superplastifiant", "isCorrect": True},
                        {"text": "Accélérateur de prise", "isCorrect": False},
                        {"text": "Retardateur de prise", "isCorrect": False},
                        {"text": "Entraîneur d'air", "isCorrect": False}
                    ],
                    "correction": "Les plastifiants et superplastifiants réduisent les forces de frottement entre les grains, permettant de rendre le béton plus fluide ou de réduire la quantité d'eau de gâchage."
                },
                {
                    "questionNumber": 23,
                    "question": "Que désigne la classe d'exposition 'XF1' pour un béton ?",
                    "answerOptions": [
                        {"text": "Gel faible", "isCorrect": True},
                        {"text": "Attaque chimique forte", "isCorrect": False},
                        {"text": "Corrosion par chlorures", "isCorrect": False},
                        {"text": "Carbonatation modérée", "isCorrect": False}
                    ],
                    "correction": "La classe XF concerne les attaques par le gel/dégel. XF1 correspond à une saturation faible en eau sans agent de déverglaçage (gel faible ou modéré)."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel essai de chantier permet de mesurer la consistance (ouvrabilité) du béton frais ?",
                    "answerOptions": [
                        {"text": "Le cône d'Abrams", "isCorrect": True},
                        {"text": "L'essai vicat", "isCorrect": False},
                        {"text": "L'essai au bleu", "isCorrect": False},
                        {"text": "L'équivalent de sable", "isCorrect": False}
                    ],
                    "correction": "L'essai d'affaissement au cône d'Abrams (Slump test) mesure la plasticité du béton frais en cm d'affaissement."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la masse volumique moyenne d'un béton armé courant ?",
                    "answerOptions": [
                        {"text": "2500 kg par mètre cube", "isCorrect": True},
                        {"text": "1800 kg par mètre cube", "isCorrect": False},
                        {"text": "3200 kg par mètre cube", "isCorrect": False},
                        {"text": "1200 kg par mètre cube", "isCorrect": False}
                    ],
                    "correction": "On retient généralement 2500 kg/m³ (2,5 t/m³) pour le béton armé, contre environ 2300-2400 kg/m³ pour un béton non armé."
                },
                {
                    "questionNumber": 26,
                    "question": "Pourquoi ajoute-t-on une petite quantité de gypse au clinker lors du broyage final du ciment ?",
                    "answerOptions": [
                        {"text": "Réguler la prise", "isCorrect": True},
                        {"text": "Changer la couleur", "isCorrect": False},
                        {"text": "Augmenter la densité", "isCorrect": False},
                        {"text": "Réduire le coût", "isCorrect": False}
                    ],
                    "correction": "Sans gypse, le ciment ferait une 'prise éclair' immédiate au contact de l'eau. Le gypse sert de régulateur pour permettre le transport et la mise en œuvre."
                },
                {
                    "questionNumber": 27,
                    "question": "Que signifie la notation '52.5' sur un sac de ciment ?",
                    "answerOptions": [
                        {"text": "La résistance minimale à la compression en mégapascals à 28 jours", "isCorrect": True},
                        {"text": "La proportion de clinker contenue dans le mélange en pourcentage", "isCorrect": False},
                        {"text": "Le temps de début de prise exprimé en minutes à vingt degrés", "isCorrect": False},
                        {"text": "La finesse de broyage mesurée selon la méthode de Blaine", "isCorrect": False}
                    ],
                    "correction": "Le nombre (32.5, 42.5, 52.5) indique la classe de résistance normalisée : c'est la résistance minimale en compression (MPa) obtenue à 28 jours sur éprouvette normalisée."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel phénomène risque de se produire si l'on vibre trop longtemps le béton ?",
                    "answerOptions": [
                        {"text": "La ségrégation", "isCorrect": True},
                        {"text": "La carbonatation", "isCorrect": False},
                        {"text": "L'hydratation", "isCorrect": False},
                        {"text": "La traction", "isCorrect": False}
                    ],
                    "correction": "La ségrégation est la séparation des constituants du béton : les gros granulats descendent au fond et la laitance remonte en surface, affaiblissant l'ouvrage."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle caractéristique des granulats est mise en évidence par l'essai 'Los Angeles' ?",
                    "answerOptions": [
                        {"text": "La résistance à la fragmentation par chocs", "isCorrect": True},
                        {"text": "La propreté des sables et des graviers", "isCorrect": False},
                        {"text": "La forme plus ou moins aplatie des grains", "isCorrect": False},
                        {"text": "La teneur en eau superficielle des matériaux", "isCorrect": False}
                    ],
                    "correction": "L'essai Los Angeles mesure la résistance des granulats aux chocs et à l'attrition (frottement réciproque) dans un tambour rotatif contenant des boulets d'acier."
                },
                {
                    "questionNumber": 30,
                    "question": "Comment appelle-t-on l'eau contenue dans les pores des granulats qui ne participe pas à l'hydratation du ciment ?",
                    "answerOptions": [
                        {"text": "Eau absorbée", "isCorrect": True},
                        {"text": "Eau efficace", "isCorrect": False},
                        {"text": "Eau totale", "isCorrect": False},
                        {"text": "Eau libre", "isCorrect": False}
                    ],
                    "correction": "L'eau absorbée est celle qui pénètre dans la porosité du granulat. L'eau 'efficace' est celle qui reste disponible pour hydrater le ciment et lubrifier le mélange."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le rôle principal de la 'cure' du béton après le coulage ?",
                    "answerOptions": [
                        {"text": "Empêcher l'évaporation trop rapide de l'eau pour éviter la fissuration", "isCorrect": True},
                        {"text": "Accélérer le séchage du béton pour pouvoir décoffrer plus vite", "isCorrect": False},
                        {"text": "Nettoyer la surface du béton pour améliorer l'esthétique finale", "isCorrect": False},
                        {"text": "Refroidir le béton pour limiter la montée en température du cœur", "isCorrect": False}
                    ],
                    "correction": "La cure protège le béton frais contre la dessiccation (séchage précoce) due au vent ou au soleil, garantissant une bonne hydratation et limitant le retrait plastique."
                },
                {
                    "questionNumber": 32,
                    "question": "Dans la désignation des bétons, que signifie 'C25/30' ?",
                    "answerOptions": [
                        {"text": "Résistance caractéristique en compression sur cylindre et sur cube", "isCorrect": True},
                        {"text": "Dosage en ciment compris entre 250 et 300 kilogrammes", "isCorrect": False},
                        {"text": "Consistance du béton mesurée entre 25 et 30 centimètres", "isCorrect": False},
                        {"text": "Durée de vie estimée de l'ouvrage en années", "isCorrect": False}
                    ],
                    "correction": "C25/30 indique une résistance caractéristique à la compression de 25 MPa mesurée sur éprouvette cylindrique et 30 MPa sur éprouvette cubique."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel matériau isolant est d'origine minérale ?",
                    "answerOptions": [
                        {"text": "Laine de verre", "isCorrect": True},
                        {"text": "Polystyrène expansé", "isCorrect": False},
                        {"text": "Ouate de cellulose", "isCorrect": False},
                        {"text": "Polyuréthane projeté", "isCorrect": False}
                    ],
                    "correction": "La laine de verre est fabriquée à partir de sable et de verre recyclé (calcin), c'est un isolant minéral, contrairement aux isolants synthétiques (pétrole) ou biosourcés (végétaux)."
                },
                {
                    "questionNumber": 34,
                    "question": "Qu'est-ce que la 'laitance' qui remonte à la surface d'un béton frais ?",
                    "answerOptions": [
                        {"text": "Un mélange d'eau et de ciment sans résistance mécanique", "isCorrect": True},
                        {"text": "Un excédent de résine de cure appliqué trop tôt", "isCorrect": False},
                        {"text": "La remontée des granulats les plus fins du sable", "isCorrect": False},
                        {"text": "Une réaction chimique due au gel du béton", "isCorrect": False}
                    ],
                    "correction": "La laitance est une pellicule superficielle fragile composée d'eau de ressuage et de particules fines de ciment, qu'il faut souvent éliminer avant une reprise de bétonnage."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est l'effet d'un excès d'eau de gâchage sur les performances du béton durci ?",
                    "answerOptions": [
                        {"text": "Chute de la résistance et augmentation de la porosité", "isCorrect": True},
                        {"text": "Amélioration de la durabilité face au gel", "isCorrect": False},
                        {"text": "Augmentation significative de la résistance à la traction", "isCorrect": False},
                        {"text": "Meilleure protection des aciers contre la rouille", "isCorrect": False}
                    ],
                    "correction": "Trop d'eau augmente la porosité du béton après évaporation de l'excédent. Plus un béton est poreux, moins il est résistant mécaniquement et moins il protège les aciers."
                },
                {
                    "questionNumber": 36,
                    "question": "À quoi sert l'essai au 'Scléromètre' sur un ouvrage existant ?",
                    "answerOptions": [
                        {"text": "Estimer la résistance superficielle du béton par rebond", "isCorrect": True},
                        {"text": "Mesurer la profondeur de carbonatation du béton", "isCorrect": False},
                        {"text": "Détecter la position des armatures dans le mur", "isCorrect": False},
                        {"text": "Calculer le taux d'humidité à cœur du matériau", "isCorrect": False}
                    ],
                    "correction": "Le scléromètre projette une masse sur le béton et mesure la valeur du rebond. C'est un essai non destructif qui donne une indication sur la dureté de surface."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel ciment est le plus adapté pour des travaux à la mer ou en milieu agressif ?",
                    "answerOptions": [
                        {"text": "PM", "isCorrect": True},
                        {"text": "CP", "isCorrect": False},
                        {"text": "CE", "isCorrect": False},
                        {"text": "NF", "isCorrect": False}
                    ],
                    "correction": "La notation 'PM' signifie 'Prise Mer'. Ces ciments ont une composition chimique limitée en aluminates pour résister aux attaques des sulfates présents dans l'eau de mer."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la granulométrie approximative d'un sable standard utilisé en béton ?",
                    "answerOptions": [
                        {"text": "0 à 4 mm", "isCorrect": True},
                        {"text": "5 à 12 mm", "isCorrect": False},
                        {"text": "15 à 25 mm", "isCorrect": False},
                        {"text": "40 à 80 mm", "isCorrect": False}
                    ],
                    "correction": "Le sable pour béton est un granulat fin dont la dimension des grains est généralement comprise entre 0 et 4 mm (0/4)."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le principe du 'Béton Autoplaçant' (BAP) ?",
                    "answerOptions": [
                        {"text": "Il se met en place sous son propre poids sans vibration", "isCorrect": True},
                        {"text": "Il durcit instantanément au contact de l'air ambiant", "isCorrect": False},
                        {"text": "Il contient des fibres métalliques remplaçant les armatures", "isCorrect": False},
                        {"text": "Il est fabriqué directement sur le chantier sans centrale", "isCorrect": False}
                    ],
                    "correction": "Grâce à des superplastifiants et une formulation spécifique, le BAP est très fluide et homogène, remplissant les coffrages complexes sans nécessiter de vibration mécanique."
                },
                {
                    "questionNumber": 40,
                    "question": "En thermique du bâtiment, que mesure le coefficient Lambda (λ) ?",
                    "answerOptions": [
                        {"text": "La conductivité thermique", "isCorrect": True},
                        {"text": "La résistance thermique", "isCorrect": False},
                        {"text": "La capacité thermique", "isCorrect": False},
                        {"text": "L'inertie thermique", "isCorrect": False}
                    ],
                    "correction": "Le lambda (λ) définit la capacité intrinsèque d'un matériau à conduire la chaleur. Plus le lambda est petit, plus le matériau est isolant."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : TECHNIQUES DE MISE EN ŒUVRE (MAÇONNERIE ET GROS ŒUVRE) (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : TECHNIQUES DE MISE EN ŒUVRE (MAÇONNERIE ET GROS ŒUVRE)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Comment appelle-t-on le décalage vertical des joints entre deux rangées de parpaings superposées ?",
                    "answerOptions": [
                        {"text": "Le harpage", "isCorrect": True},
                        {"text": "Le calfeutrement", "isCorrect": False},
                        {"text": "Le ragréage", "isCorrect": False},
                        {"text": "Le dressage", "isCorrect": False}
                    ],
                    "correction": "Le harpage (ou croisement des joints) est essentiel pour la solidité du mur. Le recouvrement doit être au minimum du tiers de la longueur de l'élément (ou la moitié pour une résistance optimale)."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle disposition est obligatoire en pied de mur pour éviter les remontées d'humidité du sol ?",
                    "answerOptions": [
                        {"text": "La coupure de capillarité", "isCorrect": True},
                        {"text": "Le joint de dilatation", "isCorrect": False},
                        {"text": "La bande de redressement", "isCorrect": False},
                        {"text": "Le chainage horizontal", "isCorrect": False}
                    ],
                    "correction": "La coupure de capillarité (ou arase étanche) bloque l'ascension de l'eau dans la maçonnerie poreuse. Elle se réalise avec un mortier hydrofugé ou une bande bitumineuse."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la première couche d'un enduit traditionnel monocouche ou multicouche ?",
                    "answerOptions": [
                        {"text": "Le gobetis", "isCorrect": True},
                        {"text": "Le corps d'enduit", "isCorrect": False},
                        {"text": "La couche de finition", "isCorrect": False},
                        {"text": "Le dégrossi", "isCorrect": False}
                    ],
                    "correction": "Le gobetis est une couche mince et liquide, fortement dosée en liant, projetée pour créer une surface rugueuse d'accrochage pour le corps d'enduit."
                },
                {
                    "questionNumber": 44,
                    "question": "Sur un plancher poutrelles-hourdis, quelle opération doit être réalisée avant de couler la table de compression ?",
                    "answerOptions": [
                        {"text": "La pose des étais sous les poutrelles", "isCorrect": True},
                        {"text": "Le ponçage de la sous-face des entrevous", "isCorrect": False},
                        {"text": "L'application d'un primaire d'accrochage chimique", "isCorrect": False},
                        {"text": "La mise en peinture des aciers de chapeau", "isCorrect": False}
                    ],
                    "correction": "Les poutrelles préfabriquées ne sont généralement pas autoportantes sur de grandes portées avant le durcissement du béton. L'étaiement prévient leur rupture ou une flèche excessive."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle est la fonction précise du 'rejingot' sur un appui de fenêtre ?",
                    "answerOptions": [
                        {"text": "Empêcher l'eau de remonter sous la traverse basse de la menuiserie et assurer l'étanchéité", "isCorrect": True},
                        {"text": "Servir uniquement de butée provisoire pour le calage de la fenêtre lors de la pose", "isCorrect": False},
                        {"text": "Renforcer la résistance mécanique de l'allège pour supporter le poids du linteau", "isCorrect": False},
                        {"text": "Créer une rupture de pont thermique entre le tableau extérieur et le doublage intérieur", "isCorrect": False}
                    ],
                    "correction": "Le rejingot est le relief arrière de l'appui (remontée de béton). Il forme une barrière physique contre l'eau poussée par le vent sous la fenêtre."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la couleur normalisée du grillage avertisseur à poser au-dessus d'une canalisation d'eau potable ?",
                    "answerOptions": [
                        {"text": "Bleu", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False}
                    ],
                    "correction": "Le code couleur des réseaux enterrés est strict : Bleu pour l'eau, Rouge pour l'électricité, Jaune pour le gaz, Vert pour les télécoms/vidéo."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel ouvrage réalise-t-on au fond d'une fouille avant de couler la semelle de fondation ?",
                    "answerOptions": [
                        {"text": "Un béton de propreté", "isCorrect": True},
                        {"text": "Un radier général", "isCorrect": False},
                        {"text": "Une chape liquide", "isCorrect": False},
                        {"text": "Un hérisson ventilé", "isCorrect": False}
                    ],
                    "correction": "Le béton de propreté (dosé faiblement) évite que le béton de fondation ne soit souillé par la terre et garantit un enrobage correct des aciers inférieurs."
                },
                {
                    "questionNumber": 48,
                    "question": "À quoi sert un 'joint de fractionnement' dans une grande surface bétonnée ?",
                    "answerOptions": [
                        {"text": "Limiter la fissuration aléatoire due au retrait du béton", "isCorrect": True},
                        {"text": "Séparer deux bâtiments de structures différentes", "isCorrect": False},
                        {"text": "Isoler thermiquement la dalle du terre-plein", "isCorrect": False},
                        {"text": "Empêcher les infiltrations d'eau souterraine", "isCorrect": False}
                    ],
                    "correction": "Le béton se rétracte en durcissant. Le joint de fractionnement (scié ou profilé) crée une zone de faiblesse où la fissure se produira de manière contrôlée et rectiligne."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est l'épaisseur habituelle d'un joint de mortier pour le montage de parpaings traditionnels ?",
                    "answerOptions": [
                        {"text": "10 à 15 millimètres", "isCorrect": True},
                        {"text": "1 à 3 millimètres", "isCorrect": False},
                        {"text": "20 à 30 millimètres", "isCorrect": False},
                        {"text": "40 à 50 millimètres", "isCorrect": False}
                    ],
                    "correction": "Pour la maçonnerie à joints épais traditionnels, l'épaisseur standard se situe entre 1 cm et 1,5 cm pour rattraper les tolérances dimensionnelles des blocs."
                },
                {
                    "questionNumber": 50,
                    "question": "Dans la maçonnerie à 'joints minces' (colle), quel outil spécifique utilise-t-on pour déposer le mortier ?",
                    "answerOptions": [
                        {"text": "Le rouleau applicateur ou la pelle crantée", "isCorrect": True},
                        {"text": "La truelle ronde et la taloche plastique", "isCorrect": False},
                        {"text": "La pompe à béton stationnaire", "isCorrect": False},
                        {"text": "Le pulvérisateur à pression manuelle", "isCorrect": False}
                    ],
                    "correction": "Le joint mince (1 à 3 mm) nécessite un dosage précis et régulier, obtenu grâce à un rouleau ou un sabot (pelle) adapté à la largeur de la brique."
                },
                {
                    "questionNumber": 51,
                    "question": "Où se situe généralement le pont thermique le plus courant dans une structure en maçonnerie sans rupteurs ?",
                    "answerOptions": [
                        {"text": "À la jonction plancher-façade", "isCorrect": True},
                        {"text": "Au milieu des murs de refend", "isCorrect": False},
                        {"text": "Sous les cloisons de distribution", "isCorrect": False},
                        {"text": "Au centre de la dalle de compression", "isCorrect": False}
                    ],
                    "correction": "Le nez de dalle en béton traverse l'isolation intérieure et touche le mur extérieur, créant une fuite de calories appelée pont thermique."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le rôle du géotextile placé autour d'un drain et des graviers ?",
                    "answerOptions": [
                        {"text": "Filtrer les fines particules de terre pour ne pas colmater le drain", "isCorrect": True},
                        {"text": "Assurer l'étanchéité totale de la paroi enterrée contre l'eau", "isCorrect": False},
                        {"text": "Renforcer la résistance mécanique du remblai contre le tassement", "isCorrect": False},
                        {"text": "Isoler thermiquement les fondations contre le gel profond", "isCorrect": False}
                    ],
                    "correction": "Le géotextile est un feutre perméable qui laisse passer l'eau mais retient la terre (les fines), empêchant ainsi le drain de se boucher."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle formule permet de vérifier le confort d'un escalier (relation entre hauteur de marche h et giron g) ?",
                    "answerOptions": [
                        {"text": "2 h + g", "isCorrect": True},
                        {"text": "h + 2 g", "isCorrect": False},
                        {"text": "h x g", "isCorrect": False},
                        {"text": "h - g", "isCorrect": False}
                    ],
                    "correction": "C'est la relation de Blondel. Pour un escalier confortable, 2 hauteurs de marche + 1 giron doit être compris entre 60 et 64 cm (longueur du pas)."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la longueur d'appui minimale standard d'un linteau sur la maçonnerie (hors calcul spécifique) ?",
                    "answerOptions": [
                        {"text": "20 cm", "isCorrect": True},
                        {"text": "5 cm", "isCorrect": False},
                        {"text": "50 cm", "isCorrect": False},
                        {"text": "10 cm", "isCorrect": False}
                    ],
                    "correction": "Par convention et sécurité (DTU 20.1), l'appui minimal est de 20 cm de chaque côté pour bien répartir les charges sur les jambages."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le rôle structurel principal d'un chaînage horizontal en béton armé ?",
                    "answerOptions": [
                        {"text": "Ceinturer la maçonnerie pour s'opposer aux efforts de traction et stabiliser l'ouvrage", "isCorrect": True},
                        {"text": "Servir uniquement de support décoratif pour la fixation des corniches de toiture", "isCorrect": False},
                        {"text": "Permettre le passage des gaines électriques horizontales sans saigner les murs", "isCorrect": False},
                        {"text": "Remplacer les fondations lorsque le sol est de trop mauvaise qualité portante", "isCorrect": False}
                    ],
                    "correction": "La maçonnerie résiste bien à la compression mais mal à la traction. Les chaînages (ferraillés) reprennent les efforts de traction et solidarisent les murs."
                },
                {
                    "questionNumber": 56,
                    "question": "Pour réaliser une coupe propre de pavés autobloquants en béton, quel matériel est le plus adapté ?",
                    "answerOptions": [
                        {"text": "La guillotine à pavés", "isCorrect": True},
                        {"text": "La scie égoïne", "isCorrect": False},
                        {"text": "Le marteau piqueur", "isCorrect": False},
                        {"text": "La cisaille à métaux", "isCorrect": False}
                    ],
                    "correction": "La guillotine à pavés (ou casse-pavés) permet une coupe nette par pression mécanique, sans poussière ni bruit excessif, contrairement à la disqueuse."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle pente minimale doit-on respecter pour un balcon ou une terrasse extérieure afin d'évacuer l'eau ?",
                    "answerOptions": [
                        {"text": "1 à 2 % vers l'extérieur", "isCorrect": True},
                        {"text": "5 à 10 % vers l'intérieur", "isCorrect": False},
                        {"text": "0 % (parfaitement plat)", "isCorrect": False},
                        {"text": "15 % vers l'extérieur", "isCorrect": False}
                    ],
                    "correction": "Une pente d'au moins 1 à 1,5 cm par mètre (1-2%) est nécessaire pour éviter la stagnation de l'eau (flaches) et les infiltrations."
                },
                {
                    "questionNumber": 58,
                    "question": "Dans quel cas l'utilisation de blocs de béton cellulaire est-elle particulièrement pertinente ?",
                    "answerOptions": [
                        {"text": "Pour améliorer l'isolation thermique du mur porteur", "isCorrect": True},
                        {"text": "Pour construire des murs immergés en permanence", "isCorrect": False},
                        {"text": "Pour réaliser des ouvrages phoniques très lourds", "isCorrect": False},
                        {"text": "Pour les fondations profondes en terrain argileux", "isCorrect": False}
                    ],
                    "correction": "Le béton cellulaire contient des millions de bulles d'air, ce qui lui confère d'excellentes propriétés d'isolation thermique par rapport au béton lourd."
                },
                {
                    "questionNumber": 59,
                    "question": "Que doit-on faire obligatoirement avant d'appliquer un enduit sur un support très sec et chaud ?",
                    "answerOptions": [
                        {"text": "Humidifier le support à refus", "isCorrect": True},
                        {"text": "Chauffer le support au chalumeau", "isCorrect": False},
                        {"text": "Appliquer une couche d'huile de décoffrage", "isCorrect": False},
                        {"text": "Poncer le support au gros grain", "isCorrect": False}
                    ],
                    "correction": "Si le support est sec et chaud, il va 'boire' l'eau du mortier trop vite, empêchant la prise chimique (phénomène de grillage de l'enduit). Il faut l'humidifier."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel élément est indispensable pour assurer la ventilation du vide sanitaire ?",
                    "answerOptions": [
                        {"text": "Des courettes d'aération grillagées", "isCorrect": True},
                        {"text": "Un système de climatisation réversible", "isCorrect": False},
                        {"text": "Une membrane étanche sous la dalle", "isCorrect": False},
                        {"text": "Un drain périphérique intérieur", "isCorrect": False}
                    ],
                    "correction": "Le vide sanitaire doit être ventilé pour éviter l'accumulation d'humidité et de gaz (radon). On utilise des bouches d'aération ou courettes réparties sur les façades opposées."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : FINITIONS, OUVRAGES HORIZONTAUX ET TRAVAUX SPÉCIFIQUES (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : FINITIONS, OUVRAGES HORIZONTAUX ET TRAVAUX SPÉCIFIQUES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "De combien de couches se compose traditionnellement un enduit extérieur manuel ?",
                    "answerOptions": [
                        {"text": "Trois", "isCorrect": True},
                        {"text": "Une seule", "isCorrect": False},
                        {"text": "Cinq ou six", "isCorrect": False},
                        {"text": "Douze", "isCorrect": False}
                    ],
                    "correction": "L'enduit traditionnel se fait en 3 couches : 1. Le gobetis (accroche), 2. Le corps d'enduit (imperméabilisation et planéité), 3. La couche de finition (aspect esthétique)."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le rôle spécifique du gobetis dans la réalisation d'un enduit ?",
                    "answerOptions": [
                        {"text": "Assurer l'accrochage", "isCorrect": True},
                        {"text": "Donner la couleur finale de la façade visible depuis la rue", "isCorrect": False},
                        {"text": "Lisser parfaitement la surface du mur", "isCorrect": False},
                        {"text": "Isoler thermiquement le bâtiment", "isCorrect": False}
                    ],
                    "correction": "Le gobetis est une couche mince, riche en ciment et rugueuse. Elle sert d'interface d'adhérence entre le support (maçonnerie) et le corps d'enduit qui viendra ensuite."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle différence technique distingue une chape d'une dalle en béton ?",
                    "answerOptions": [
                        {"text": "La chape est une finition", "isCorrect": True},
                        {"text": "La chape contient du gros gravier", "isCorrect": False},
                        {"text": "La chape est toujours armée de gros aciers", "isCorrect": False},
                        {"text": "La chape porte les murs de la maison", "isCorrect": False}
                    ],
                    "correction": "La dalle est un élément structurel porteur (béton + graviers + ferraillage). La chape est une couche de mortier (sable + ciment) coulée sur la dalle pour niveler le sol avant la pose du carrelage."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle pente minimale doit-on respecter pour une canalisation d'eaux usées ?",
                    "answerOptions": [
                        {"text": "1 centimètre par mètre", "isCorrect": True},
                        {"text": "50 centimètres par mètre", "isCorrect": False},
                        {"text": "1 millimètre par kilomètre", "isCorrect": False},
                        {"text": "90 degrés de pente", "isCorrect": False}
                    ],
                    "correction": "Pour assurer un bon écoulement des matières sans stagnation (bouchons) ni érosion, une pente comprise entre 1 % (1 cm/m) et 3 % est recommandée par le DTU 60.11."
                },
                {
                    "questionNumber": 65,
                    "question": "À quoi sert un 'regard' installé sur un réseau de canalisations enterrées ?",
                    "answerOptions": [
                        {"text": "Inspecter le réseau", "isCorrect": True},
                        {"text": "Augmenter la pression de l'eau", "isCorrect": False},
                        {"text": "Stocker l'eau de pluie pour l'été", "isCorrect": False},
                        {"text": "Filtrer les bactéries présentes", "isCorrect": False}
                    ],
                    "correction": "Le regard de visite permet d'accéder aux canalisations aux endroits stratégiques (changements de direction, jonctions) pour le contrôle, le curage et le débouchage éventuel."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le rôle principal du film polyane placé sous un dallage sur terre-plein ?",
                    "answerOptions": [
                        {"text": "Bloquer les remontées d'humidité", "isCorrect": True},
                        {"text": "Améliorer l'acoustique de la pièce", "isCorrect": False},
                        {"text": "Coller le béton au sol naturel", "isCorrect": False},
                        {"text": "Renforcer la résistance du béton", "isCorrect": False}
                    ],
                    "correction": "Le film polyane (ou pare-vapeur) crée une barrière étanche qui empêche l'humidité naturelle du sol de remonter par capillarité dans la dalle en béton."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la hauteur maximale autorisée pour un seuil de porte accessible aux personnes handicapées (PMR) ?",
                    "answerOptions": [
                        {"text": "2 centimètres", "isCorrect": True},
                        {"text": "10 centimètres", "isCorrect": False},
                        {"text": "15 centimètres", "isCorrect": False},
                        {"text": "20 centimètres", "isCorrect": False}
                    ],
                    "correction": "La réglementation sur l'accessibilité impose que les ressauts (seuils de portes-fenêtres ou d'entrée) ne dépassent pas 2 cm pour permettre le passage d'un fauteuil roulant."
                },
                {
                    "questionNumber": 68,
                    "question": "Qu'est-ce qu'un pont thermique dans une construction ?",
                    "answerOptions": [
                        {"text": "Une zone de fuite de chaleur", "isCorrect": True},
                        {"text": "Un système de chauffage par le sol très performant", "isCorrect": False},
                        {"text": "Une passerelle reliant deux bâtiments", "isCorrect": False},
                        {"text": "Un isolant ultra efficace", "isCorrect": False}
                    ],
                    "correction": "Un pont thermique est une discontinuité dans l'isolation (jonction dalle/mur, angles) par laquelle la chaleur s'échappe plus vite que par le reste des parois, créant des points froids."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel outil manuel utilise-t-on pour réaliser la finition d'un enduit gratté ?",
                    "answerOptions": [
                        {"text": "Le gratton", "isCorrect": True},
                        {"text": "La truelle", "isCorrect": False},
                        {"text": "Le marteau", "isCorrect": False},
                        {"text": "Le niveau", "isCorrect": False}
                    ],
                    "correction": "Le gratton est une planche garnie de pointes. On l'utilise quand l'enduit a commencé sa prise pour griffer la surface et obtenir l'aspect 'gratté' caractéristique."
                },
                {
                    "questionNumber": 70,
                    "question": "Sur quel matériau pose-t-on des bordures de trottoir pour les sceller ?",
                    "answerOptions": [
                        {"text": "Un lit de béton", "isCorrect": True},
                        {"text": "Du sable fin sec", "isCorrect": False},
                        {"text": "De la terre végétale", "isCorrect": False},
                        {"text": "Des copeaux de bois", "isCorrect": False}
                    ],
                    "correction": "Les bordures doivent être calées au béton (lit de pose + épaulement arrière) pour résister aux chocs et à la poussée des véhicules ou de la chaussée."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle couleur de grillage avertisseur signale une canalisation d'eau potable enterrée ?",
                    "answerOptions": [
                        {"text": "Bleu", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False}
                    ],
                    "correction": "Le code couleur normalisé est impératif : Bleu pour l'eau, Rouge pour l'électricité, Jaune pour le gaz, Vert pour les télécoms."
                },
                {
                    "questionNumber": 72,
                    "question": "Que désigne le terme 'barbotine' en maçonnerie ?",
                    "answerOptions": [
                        {"text": "Un mélange liquide de ciment et d'eau", "isCorrect": True},
                        {"text": "Un béton très riche en gros cailloux", "isCorrect": False},
                        {"text": "Une brique cassée en deux morceaux", "isCorrect": False},
                        {"text": "Un outil pour lisser les joints", "isCorrect": False}
                    ],
                    "correction": "La barbotine est un coulis de liant pur (ciment ou chaux) et d'eau. Elle est utilisée pour coller du carrelage en pose scellée ou pour assurer l'accrochage entre deux couches de béton frais."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le but d'un joint de dilatation dans une grande dalle béton ?",
                    "answerOptions": [
                        {"text": "Absorber les mouvements", "isCorrect": True},
                        {"text": "Faire joli au milieu de la pièce", "isCorrect": False},
                        {"text": "Économiser du béton au coulage", "isCorrect": False},
                        {"text": "Permettre le passage des câbles", "isCorrect": False}
                    ],
                    "correction": "Les matériaux se dilatent avec la chaleur. Le joint de dilatation sectionne l'ouvrage pour permettre au béton de bouger sans provoquer de fissuration aléatoire ou de soulèvement."
                },
                {
                    "questionNumber": 74,
                    "question": "À quoi sert la 'règle à dresser' lors de l'application d'un enduit ?",
                    "answerOptions": [
                        {"text": "Aplanir le corps d'enduit", "isCorrect": True},
                        {"text": "Mesurer la quantité de sable", "isCorrect": False},
                        {"text": "Nettoyer les outils en fin de journée", "isCorrect": False},
                        {"text": "Compter les sacs de ciment utilisés", "isCorrect": False}
                    ],
                    "correction": "La règle en aluminium (souvent de 2m) permet de 'dresser' le mur, c'est-à-dire de couper les bosses et combler les creux pour obtenir une surface parfaitement plane."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle est la fonction d'un produit de ragréage autolissant ?",
                    "answerOptions": [
                        {"text": "Corriger les défauts de planéité d'un sol", "isCorrect": True},
                        {"text": "Construire un mur en parpaings", "isCorrect": False},
                        {"text": "Isoler les combles de la maison", "isCorrect": False},
                        {"text": "Peindre les plafonds en blanc", "isCorrect": False}
                    ],
                    "correction": "Le ragréage est un mortier très fluide que l'on coule sur un sol irrégulier. Il s'étale tout seul par gravité pour créer une surface parfaitement lisse et horizontale avant la pose du revêtement."
                },
                {
                    "questionNumber": 76,
                    "question": "Où doit-on placer le drain périphérique par rapport aux fondations ?",
                    "answerOptions": [
                        {"text": "Contre la semelle sans descendre plus bas", "isCorrect": True},
                        {"text": "Au-dessus du niveau du terrain naturel", "isCorrect": False},
                        {"text": "Juste sous la toiture du bâtiment", "isCorrect": False},
                        {"text": "Directement dans le béton de la fondation", "isCorrect": False}
                    ],
                    "correction": "Le drain se pose en bas de mur, sur la cunette ou à côté de la semelle, mais jamais plus bas que la base de la fondation pour ne pas déstabiliser l'assise du bâtiment."
                },
                {
                    "questionNumber": 77,
                    "question": "Comment appelle-t-on le procédé consistant à compacter le sol avant de couler une dalle ?",
                    "answerOptions": [
                        {"text": "Le compactage", "isCorrect": True},
                        {"text": "Le nivellement", "isCorrect": False},
                        {"text": "Le surfaçage", "isCorrect": False},
                        {"text": "Le pilonnage", "isCorrect": False}
                    ],
                    "correction": "Le compactage (avec une plaque vibrante ou un rouleau) est essentiel pour garantir la stabilité de l'assise et éviter le tassement futur de la dalle."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le rôle des 'couvre-joints' en façade ?",
                    "answerOptions": [
                        {"text": "Cacher les joints de dilatation", "isCorrect": True},
                        {"text": "Accélérer la prise de l'enduit", "isCorrect": False},
                        {"text": "Renforcer la maçonnerie", "isCorrect": False},
                        {"text": "Servir de guide pour le crépi", "isCorrect": False}
                    ],
                    "correction": "Les couvre-joints sont des profilés (métalliques ou PVC) utilisés pour masquer l'espace libre laissé par les joints de dilatation ou de rupture tout en permettant le mouvement de la structure."
                },
                {
                    "questionNumber": 79,
                    "question": "Qu'est-ce qu'une 'pente à la romaine' sur une terrasse ?",
                    "answerOptions": [
                        {"text": "Une pente douce vers l'extérieur", "isCorrect": True},
                        {"text": "Une pente très forte vers le centre", "isCorrect": False},
                        {"text": "Une pente irrégulière et aléatoire", "isCorrect": False},
                        {"text": "Un sol parfaitement plat", "isCorrect": False}
                    ],
                    "correction": "La pente à la romaine (ou 'à l'italienne') consiste à donner une légère inclinaison au sol vers l'extérieur pour faciliter l'évacuation de l'eau."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la principale fonction du 'mortier de montage' pour les murs ?",
                    "answerOptions": [
                        {"text": "Lier les éléments de maçonnerie et niveler", "isCorrect": True},
                        {"text": "Faire l'enduit de finition", "isCorrect": False},
                        {"text": "Isoler phoniquement le mur", "isCorrect": False},
                        {"text": "Servir d'isolant thermique", "isCorrect": False}
                    ],
                    "correction": "Le mortier sert à coller les blocs entre eux et à assurer l'horizontalité (le niveau) de chaque rang de maçonnerie."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : GESTION, SANTÉ ET ENVIRONNEMENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : GESTION, SANTÉ ET ENVIRONNEMENT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel document liste les produits commandés par le magasin ?",
                    "answerOptions": [
                        {"text": "Le bon de commande", "isCorrect": True},
                        {"text": "Le bon de livraison", "isCorrect": False},
                        {"text": "La facture", "isCorrect": False},
                        {"text": "Le ticket de caisse", "isCorrect": False}
                    ],
                    "correction": "Le bon de commande est le document qui matérialise l'intention d'achat du magasin auprès du fournisseur."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment calcule-t-on la marge commerciale brute (en valeur) ?",
                    "answerOptions": [
                        {"text": "Prix de vente HT - Coût d'achat HT", "isCorrect": True},
                        {"text": "Prix de vente TTC - Coût d'achat TTC", "isCorrect": False},
                        {"text": "Coût d'achat + Charges fixes", "isCorrect": False},
                        {"text": "Chiffre d'affaires / Nombre de clients", "isCorrect": False}
                    ],
                    "correction": "La marge brute est le profit généré avant la déduction des charges de structure."
                },
                {
                    "questionNumber": 83,
                    "question": "Que signifie le sigle LIFO dans la gestion des stocks ?",
                    "answerOptions": [
                        {"text": "Last In, First Out (Dernier entré, premier sorti)", "isCorrect": True},
                        {"text": "Le produit le plus cher sort en premier", "isCorrect": False},
                        {"text": "La méthode de sortie des produits périssables", "isCorrect": False},
                        {"text": "Le premier entré sort en premier (FIFO)", "isCorrect": False}
                    ],
                    "correction": "Le LIFO est une méthode de valorisation des stocks : le coût du dernier article acheté est imputé à la première vente."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel taux de TVA s'applique aux travaux de rénovation de logements anciens (moins de 2 ans) ?",
                    "answerOptions": [
                        {"text": "10 %", "isCorrect": True},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "5,5 %", "isCorrect": False},
                        {"text": "2,1 %", "isCorrect": False}
                    ],
                    "correction": "Le taux intermédiaire de 10% s'applique aux travaux d'amélioration, de transformation, d'aménagement et d'entretien."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle maladie professionnelle est liée au bruit excessif des machines (bétonnière, disqueuse) ?",
                    "answerOptions": [
                        {"text": "La surdité", "isCorrect": True},
                        {"text": "L'acouphène", "isCorrect": False},
                        {"text": "La cataracte", "isCorrect": False},
                        {"text": "L'hygroma", "isCorrect": False}
                    ],
                    "correction": "Les bruits supérieurs à 85 dB peuvent causer des dommages irréversibles à l'oreille interne (surdité, acouphènes)."
                },
                {
                    "questionNumber": 86,
                    "question": "Que désigne la 'démarque inconnue' ?",
                    "answerOptions": [
                        {"text": "Les pertes de stock (vol, casse, erreurs) non justifiées", "isCorrect": True},
                        {"text": "Les invendus du magasin", "isCorrect": False},
                        {"text": "La casse enregistrée après contrôle", "isCorrect": False},
                        {"text": "Le manque de personnel", "isCorrect": False}
                    ],
                    "correction": "La démarque inconnue est l'écart entre le stock théorique et le stock réel, souvent causé par le vol ou des erreurs non documentées."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel document doit être rédigé avant le démarrage de tout chantier par l'entreprise ?",
                    "answerOptions": [
                        {"text": "Le Plan de Prévention (si intervention sur site tiers)", "isCorrect": True},
                        {"text": "Le Bon de Commande", "isCorrect": False},
                        {"text": "L'Attestation d'Assurance", "isCorrect": False},
                        {"text": "Le CCTP", "isCorrect": False}
                    ],
                    "correction": "Le Plan de Prévention (ou PPSPS sur les gros chantiers) définit les règles de sécurité spécifiques à l'environnement de travail, essentiel pour les travaux en co-activité."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment appelle-t-on l'usure ou la dépréciation progressive du matériel (bétonnière, camion) ?",
                    "answerOptions": [
                        {"text": "L'amortissement", "isCorrect": True},
                        {"text": "La fiscalité", "isCorrect": False},
                        {"text": "Le bénéfice", "isCorrect": False},
                        {"text": "La marge", "isCorrect": False}
                    ],
                    "correction": "L'amortissement est la constatation comptable de la perte de valeur d'un bien due à l'usage et au temps."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est l'objectif principal du tri des déchets sur un chantier de maçonnerie ?",
                    "answerOptions": [
                        {"text": "Le recyclage des matériaux inertes", "isCorrect": True},
                        {"text": "La décoration du chantier", "isCorrect": False},
                        {"text": "La lutte contre le bruit", "isCorrect": False},
                        {"text": "Le gain de temps au déchargement", "isCorrect": False}
                    ],
                    "correction": "Les déchets inertes (gravats, béton, tuiles) et les déchets non dangereux (bois, plastiques) doivent être triés pour leur valorisation et leur recyclage."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel taux de TVA s'applique aux travaux de construction neuve ?",
                    "answerOptions": [
                        {"text": "20 %", "isCorrect": True},
                        {"text": "10 %", "isCorrect": False},
                        {"text": "5,5 %", "isCorrect": False},
                        {"text": "0 %", "isCorrect": False}
                    ],
                    "correction": "Les travaux de construction neuve sont soumis au taux normal de 20 %."
                },
                {
                    "questionNumber": 91,
                    "question": "Le port du casque avec jugulaire est obligatoire pour prévenir quel risque ?",
                    "answerOptions": [
                        {"text": "La chute d'objets ou le heurt de la tête", "isCorrect": True},
                        {"text": "Le bruit excessif", "isCorrect": False},
                        {"text": "Les brûlures chimiques", "isCorrect": False},
                        {"text": "Les coupures", "isCorrect": False}
                    ],
                    "correction": "Le casque protège la tête contre les chutes d'objets (dynamique) et les chocs directs. La jugulaire évite qu'il ne tombe lors des mouvements ou des chutes."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le risque lié au stockage de ciment périmé (éventé) sur chantier ?",
                    "answerOptions": [
                        {"text": "Baisse drastique de la résistance mécanique du béton", "isCorrect": True},
                        {"text": "Augmentation de la vitesse de prise du béton", "isCorrect": False},
                        {"text": "Changement de couleur du béton au rose", "isCorrect": False},
                        {"text": "Contamination du sable par les moisissures", "isCorrect": False}
                    ],
                    "correction": "Le ciment éventé (ayant pris l'humidité de l'air) a déjà réagi et n'offre plus la résistance attendue une fois gâché avec l'eau de gâchage."
                },
                {
                    "questionNumber": 93,
                    "question": "Quelle est la pénalité principale pour une entreprise qui ne respecte pas les délais contractuels ?",
                    "answerOptions": [
                        {"text": "Des pénalités de retard", "isCorrect": True},
                        {"text": "L'arrêt immédiat du chantier", "isCorrect": False},
                        {"text": "Une amende fixe de 1000 euros", "isCorrect": False},
                        {"text": "Le licenciement du chef de chantier", "isCorrect": False}
                    ],
                    "correction": "Les pénalités de retard (souvent un pourcentage du marché par jour) sont prévues dans les CCTP."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le risque lié au stockage de ciment périmé (éventé) sur chantier ?",
                    "answerOptions": [
                        {"text": "Baisse drastique de la résistance mécanique du béton", "isCorrect": True},
                        {"text": "Augmentation de la vitesse de prise du béton", "isCorrect": False},
                        {"text": "Changement de couleur du béton au rose", "isCorrect": False},
                        {"text": "Contamination du sable par les moisissures", "isCorrect": False}
                    ],
                    "correction": "Le ciment éventé (ayant pris l'humidité de l'air) a déjà réagi et n'offre plus la résistance attendue une fois gâché avec l'eau de gâchage."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le risque chimique principal lié à la manipulation de mortier frais ?",
                    "answerOptions": [
                        {"text": "Les brûlures basiques (alcalines) de la peau", "isCorrect": True},
                        {"text": "L'hypothermie des mains", "isCorrect": False},
                        {"text": "La coupe par les grains de sable", "isCorrect": False},
                        {"text": "L'explosion de la gâchée", "isCorrect": False}
                    ],
                    "correction": "Le ciment est très alcalin (pH élevé). Le contact prolongé sans gants provoque des brûlures par caustification."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la durée de validité de l'attestation d'aptitude médicale pour un salarié exposé à des risques (ex: travail en hauteur) ?",
                    "answerOptions": [
                        {"text": "5 ans (sauf avis contraire du médecin)", "isCorrect": True},
                        {"text": "1 an", "isCorrect": False},
                        {"text": "3 mois", "isCorrect": False},
                        {"text": "10 ans", "isCorrect": False}
                    ],
                    "correction": "La visite médicale de renouvellement est de 5 ans, mais elle peut être raccourcie selon les risques ou l'âge du travailleur."
                },
                {
                    "questionNumber": 97,
                    "question": "Le risque de 'choc thermique' lors du coulage du béton neuf est lié à :",
                    "answerOptions": [
                        {"text": "Une différence de température trop forte entre la reprise et le nouveau béton", "isCorrect": True},
                        {"text": "La foudre qui tombe sur le chantier", "isCorrect": False},
                        {"text": "L'utilisation de trop d'eau froide", "isCorrect": False},
                        {"text": "Le chauffage excessif du coffrage", "isCorrect": False}
                    ],
                    "correction": "Un choc thermique peut provoquer des microfissures. On limite les écarts de température entre deux coulages (reprise de bétonnage) à moins de 10°C."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le risque immédiat lié au coulage de béton sur une zone non délimitée ou sans protection latérale ?",
                    "answerOptions": [
                        {"text": "La projection de ciment dans les yeux des passants", "isCorrect": True},
                        {"text": "Le tassement ultérieur du béton", "isCorrect": False},
                        {"text": "La ségrégation du mélange", "isCorrect": False},
                        {"text": "L'écroulement de la structure", "isCorrect": False}
                    ],
                    "correction": "La projection de ciment (produit caustique) dans les yeux d'un passant (risque chimique) dans un chantier ouvert est le danger le plus fréquent."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le délai de garantie légale du parfait achèvement après la réception des travaux ?",
                    "answerOptions": [
                        {"text": "1 an", "isCorrect": True},
                        {"text": "2 ans", "isCorrect": False},
                        {"text": "10 ans", "isCorrect": False},
                        {"text": "30 jours", "isCorrect": False}
                    ],
                    "correction": "Le parfait achèvement couvre les défauts signalés à la réception ou durant l'année qui suit."
                },
                {
                    "questionNumber": 100,
                    "question": "Les déchets de bois et les gravats inertes doivent être jetés dans :",
                    "answerOptions": [
                        {"text": "Des bennes séparées", "isCorrect": True},
                        {"text": "La même benne (tous les déchets ensemble)", "isCorrect": False},
                        {"text": "Un trou au fond du jardin", "isCorrect": False},
                        {"text": "La poubelle de bureau", "isCorrect": False}
                    ],
                    "correction": "Le tri sélectif est obligatoire. Le bois est un Déchet Non Dangereux (DND) valorisable, les gravats sont des Déchets Inertes. Ils ne doivent pas être mélangés."
                }
            ]
        }
    }
}