quiz_data = {
    "title": "Quiz CAP Prévention Santé Environnement (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : L'INDIVIDU ET SA SANTÉ (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : L'INDIVIDU ET SA SANTÉ",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la durée moyenne d'un cycle de sommeil chez l'adulte ?",
                    "answerOptions": [
                        {"text": "90 minutes", "isCorrect": True},
                        {"text": "10 minutes seulement", "isCorrect": False},
                        {"text": "4 heures consécutives", "isCorrect": False},
                        {"text": "8 heures environ", "isCorrect": False}
                    ],
                    "correction": "Une nuit de sommeil est constituée de la succession de 3 à 5 cycles successifs. Chaque cycle dure en moyenne 90 minutes (1h30)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le rôle principal du sommeil lent profond ?",
                    "answerOptions": [
                        {"text": "Récupération de la fatigue physique", "isCorrect": True},
                        {"text": "Apparition des rêves et des cauchemars", "isCorrect": False},
                        {"text": "Maturation du système nerveux central", "isCorrect": False},
                        {"text": "Mémorisation des apprentissages de la journée", "isCorrect": False}
                    ],
                    "correction": "Le sommeil lent profond est la phase où l'activité cérébrale est la plus ralentie. C'est le moment privilégié pour la récupération musculaire et l'élimination des déchets métaboliques."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment se nomme la cellule de base du système nerveux ?",
                    "answerOptions": [
                        {"text": "Neurone", "isCorrect": True},
                        {"text": "Hormone", "isCorrect": False},
                        {"text": "Plaquette", "isCorrect": False},
                        {"text": "Glucide", "isCorrect": False}
                    ],
                    "correction": "Le neurone est l'unité fonctionnelle du système nerveux, spécialisée dans la communication et le traitement de l'information."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel nutriment est la principale source d'énergie immédiate pour l'organisme ?",
                    "answerOptions": [
                        {"text": "Les glucides", "isCorrect": True},
                        {"text": "Les protéines", "isCorrect": False},
                        {"text": "Les lipides", "isCorrect": False},
                        {"text": "Les sels minéraux", "isCorrect": False}
                    ],
                    "correction": "Les glucides (sucres) sont les 'carburants' du corps. On distingue les glucides simples (énergie rapide) et les glucides complexes (énergie durable)."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel organe assure la filtration du sang et l'élimination des déchets via l'urine ?",
                    "answerOptions": [
                        {"text": "Le rein", "isCorrect": True},
                        {"text": "Le foie", "isCorrect": False},
                        {"text": "Le poumon", "isCorrect": False},
                        {"text": "Le cœur", "isCorrect": False}
                    ],
                    "correction": "Les reins filtrent le sang en permanence pour produire l'urine, permettant ainsi de maintenir l'équilibre en eau et en sels minéraux de l'organisme."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle addiction se caractérise par une dépendance au tabac ?",
                    "answerOptions": [
                        {"text": "Le tabagisme", "isCorrect": True},
                        {"text": "L'alcoolisme", "isCorrect": False},
                        {"text": "La cyberdépendance", "isCorrect": False},
                        {"text": "Le dopage", "isCorrect": False}
                    ],
                    "correction": "Le tabagisme est une toxicomanie résultant de l'accoutumance à la nicotine, substance présente dans le tabac."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est l'effet principal des fibres alimentaires sur la santé ?",
                    "answerOptions": [
                        {"text": "Réguler le transit intestinal", "isCorrect": True},
                        {"text": "Développer la masse musculaire", "isCorrect": False},
                        {"text": "Apporter beaucoup de calories", "isCorrect": False},
                        {"text": "Colorer la peau", "isCorrect": False}
                    ],
                    "correction": "Les fibres (présentes dans les fruits, légumes et céréales complètes) ne sont pas digérées mais facilitent la digestion et l'élimination."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est le principal risque lié à une consommation excessive de sucre ?",
                    "answerOptions": [
                        {"text": "Le diabète de type 2", "isCorrect": True},
                        {"text": "L'anémie", "isCorrect": False},
                        {"text": "L'hypotension", "isCorrect": False},
                        {"text": "La surdité", "isCorrect": False}
                    ],
                    "correction": "Un excès de sucre entraîne une surcharge pour le pancréas et peut mener à l'obésité et au diabète."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le rôle des protéines dans l'organisme ?",
                    "answerOptions": [
                        {"text": "Construction et réparation des tissus", "isCorrect": True},
                        {"text": "Stockage des réserves de graisse", "isCorrect": False},
                        {"text": "Transport de l'électricité nerveuse", "isCorrect": False},
                        {"text": "Hydratation des cellules", "isCorrect": False}
                    ],
                    "correction": "Les protéines sont des nutriments 'bâtisseurs'. Elles sont essentielles à la fabrication des muscles, de la peau et des os."
                },
                {
                    "questionNumber": 10,
                    "question": "Comment appelle-t-on le déséquilibre alimentaire lié à un manque de fer ?",
                    "answerOptions": [
                        {"text": "L'anémie", "isCorrect": True},
                        {"text": "Le scorbut", "isCorrect": False},
                        {"text": "L'hyperglycémie", "isCorrect": False},
                        {"text": "La déshydratation", "isCorrect": False}
                    ],
                    "correction": "Le fer est nécessaire au transport de l'oxygène dans le sang. Un manque provoque une fatigue intense appelée anémie."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la fonction du système immunitaire ?",
                    "answerOptions": [
                        {"text": "Défendre l'organisme contre les microbes", "isCorrect": True},
                        {"text": "Digérer les aliments lourds", "isCorrect": False},
                        {"text": "Faire circuler le sang dans les membres", "isCorrect": False},
                        {"text": "Permettre la respiration nocturne", "isCorrect": False}
                    ],
                    "correction": "Le système immunitaire produit des anticorps et des globules blancs pour combattre les virus, bactéries et parasites."
                },
                {
                    "questionNumber": 12,
                    "question": "Qu'est-ce qu'une IST ?",
                    "answerOptions": [
                        {"text": "Infection Sexuellement Transmissible", "isCorrect": True},
                        {"text": "Indice de Santé Totale", "isCorrect": False},
                        {"text": "Intoxication Sévère par le Tabac", "isCorrect": False},
                        {"text": "Institution de Soins Temporaires", "isCorrect": False}
                    ],
                    "correction": "Les IST sont des infections transmises lors de rapports sexuels. Le préservatif est le seul moyen de protection efficace."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel comportement permet de limiter les risques cardiovasculaires ?",
                    "answerOptions": [
                        {"text": "Pratiquer une activité physique régulière", "isCorrect": True},
                        {"text": "Manger très salé", "isCorrect": False},
                        {"text": "Fumer peu mais tous les jours", "isCorrect": False},
                        {"text": "Dormir moins de 4 heures par nuit", "isCorrect": False}
                    ],
                    "correction": "Le sport renforce le muscle cardiaque, améliore la circulation et aide à réguler la tension artérielle."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelle hormone est responsable de la régulation du taux de sucre dans le sang ?",
                    "answerOptions": [
                        {"text": "L'insuline", "isCorrect": True},
                        {"text": "L'adrénaline", "isCorrect": False},
                        {"text": "La testostérone", "isCorrect": False},
                        {"text": "La mélatonine", "isCorrect": False}
                    ],
                    "correction": "L'insuline est produite par le pancréas. Elle permet au sucre d'entrer dans les cellules pour y être utilisé."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est l'apport nutritionnel majeur de l'eau ?",
                    "answerOptions": [
                        {"text": "L'hydratation et les sels minéraux", "isCorrect": True},
                        {"text": "Les vitamines A et C", "isCorrect": False},
                        {"text": "Les sucres lents", "isCorrect": False},
                        {"text": "Les graisses saturées", "isCorrect": False}
                    ],
                    "correction": "L'eau est la seule boisson indispensable. Elle constitue environ 60% du corps humain."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le risque lié à une exposition prolongée et sans protection au soleil ?",
                    "answerOptions": [
                        {"text": "Le cancer de la peau (mélanome)", "isCorrect": True},
                        {"text": "L'asthme", "isCorrect": False},
                        {"text": "Le diabète", "isCorrect": False},
                        {"text": "La perte d'audition", "isCorrect": False}
                    ],
                    "correction": "Les rayons UV endommagent l'ADN des cellules cutanées, ce qui peut provoquer des tumeurs à long terme."
                },
                {
                    "questionNumber": 17,
                    "question": "Comment appelle-t-on le stress positif qui nous aide à réussir ?",
                    "answerOptions": [
                        {"text": "L'eustress", "isCorrect": True},
                        {"text": "Le déstress", "isCorrect": False},
                        {"text": "Le burnout", "isCorrect": False},
                        {"text": "L'angoisse", "isCorrect": False}
                    ],
                    "correction": "Le stress est une réaction d'adaptation. S'il est modéré et ponctuel, il stimule la concentration et la performance."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel organe est le plus touché par une consommation excessive d'alcool à long terme ?",
                    "answerOptions": [
                        {"text": "Le foie", "isCorrect": True},
                        {"text": "Les oreilles", "isCorrect": False},
                        {"text": "Les articulations", "isCorrect": False},
                        {"text": "Les dents", "isCorrect": False}
                    ],
                    "correction": "L'alcool peut provoquer une cirrhose, une maladie irréversible qui détruit les cellules du foie."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le principal constituant des os et des dents ?",
                    "answerOptions": [
                        {"text": "Le calcium", "isCorrect": True},
                        {"text": "Le magnésium", "isCorrect": False},
                        {"text": "Le potassium", "isCorrect": False},
                        {"text": "Le sodium", "isCorrect": False}
                    ],
                    "correction": "Le calcium est un minéral indispensable à la solidité du squelette, apporté principalement par les produits laitiers et certaines eaux."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est la définition de la santé selon l'OMS ?",
                    "answerOptions": [
                        {"text": "Un état de complet bien-être physique, mental et social", "isCorrect": True},
                        {"text": "L'absence de maladies uniquement", "isCorrect": False},
                        {"text": "Le fait de ne pas être à l'hôpital", "isCorrect": False},
                        {"text": "Avoir une bonne condition sportive", "isCorrect": False}
                    ],
                    "correction": "La santé n'est pas seulement l'absence d'infirmité, mais une harmonie globale de l'individu."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : CADRE DE VIE ET ENVIRONNEMENT (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : CADRE DE VIE ET ENVIRONNEMENT",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le principal gaz responsable de l'effet de serre lié aux activités humaines ?",
                    "answerOptions": [
                        {"text": "Le dioxyde de carbone (CO2)", "isCorrect": True},
                        {"text": "L'oxygène", "isCorrect": False},
                        {"text": "L'azote", "isCorrect": False},
                        {"text": "L'hélium", "isCorrect": False}
                    ],
                    "correction": "Le CO2, issu principalement de la combustion des énergies fossiles, emprisonne la chaleur dans l'atmosphère."
                },
                {
                    "questionNumber": 22,
                    "question": "Dans quel bac de tri doit-on jeter les bouteilles en plastique ?",
                    "answerOptions": [
                        {"text": "Le bac jaune", "isCorrect": True},
                        {"text": "Le bac vert (verre)", "isCorrect": False},
                        {"text": "Le bac gris (ordures ménagères)", "isCorrect": False},
                        {"text": "Le compost", "isCorrect": False}
                    ],
                    "correction": "Le bac jaune est destiné aux emballages recyclables (plastique, métal, carton)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est l'objectif du développement durable ?",
                    "answerOptions": [
                        {"text": "Répondre aux besoins actuels sans compromettre les générations futures", "isCorrect": True},
                        {"text": "Arrêter toute production industrielle", "isCorrect": False},
                        {"text": "Augmenter la consommation d'énergie", "isCorrect": False},
                        {"text": "Supprimer les impôts écologiques", "isCorrect": False}
                    ],
                    "correction": "Il repose sur trois piliers : économique, social et environnemental."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on la pollution sonore ?",
                    "answerOptions": [
                        {"text": "Le bruit", "isCorrect": True},
                        {"text": "Les ondes", "isCorrect": False},
                        {"text": "Le smog", "isCorrect": False},
                        {"text": "L'effet Larsen", "isCorrect": False}
                    ],
                    "correction": "Le bruit est une nuisance qui peut entraîner fatigue, stress et surdité."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est l'unité de mesure de l'intensité du son ?",
                    "answerOptions": [
                        {"text": "Le décibel (dB)", "isCorrect": True},
                        {"text": "Le mètre par seconde", "isCorrect": False},
                        {"text": "Le degré Celsius", "isCorrect": False},
                        {"text": "Le gramme", "isCorrect": False}
                    ],
                    "correction": "L'échelle est logarithmique : une augmentation de 3 dB correspond à un doublement de l'énergie sonore."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel label garantit qu'un produit a été fabriqué dans le respect de l'environnement ?",
                    "answerOptions": [
                        {"text": "L'Écolabel européen", "isCorrect": True},
                        {"text": "Le code-barres", "isCorrect": False},
                        {"text": "Le logo de la marque", "isCorrect": False},
                        {"text": "L'étiquette de prix", "isCorrect": False}
                    ],
                    "correction": "L'Écolabel certifie que le produit a un impact réduit sur l'environnement tout au long de son cycle de vie."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le principal polluant de l'air intérieur dans un logement mal ventilé ?",
                    "answerOptions": [
                        {"text": "Les composés organiques volatils (COV)", "isCorrect": True},
                        {"text": "Le pollen", "isCorrect": False},
                        {"text": "La pluie acide", "isCorrect": False},
                        {"text": "Le sable", "isCorrect": False}
                    ],
                    "correction": "Les COV proviennent des colles, peintures, meubles et produits d'entretien. D'où l'importance d'aérer 10 min par jour."
                },
                {
                    "questionNumber": 28,
                    "question": "Qu'est-ce qu'une énergie renouvelable ?",
                    "answerOptions": [
                        {"text": "Une énergie issue de sources naturelles inépuisables", "isCorrect": True},
                        {"text": "Une énergie produite par le charbon", "isCorrect": False},
                        {"text": "Une électricité qui coûte très cher", "isCorrect": False},
                        {"text": "Un carburant issu du pétrole", "isCorrect": False}
                    ],
                    "correction": "Exemples : solaire, éolien, hydraulique, biomasse, géothermie."
                },
                {
                    "questionNumber": 29,
                    "question": "Que signifie le sigle 'Bruit' au travail ?",
                    "answerOptions": [
                        {"text": "Nuisance sonore supérieure à 80 dB", "isCorrect": True},
                        {"text": "Musique d'ambiance obligatoire", "isCorrect": False},
                        {"text": "Silence total", "isCorrect": False},
                        {"text": "Appareil de mesure de la vue", "isCorrect": False}
                    ],
                    "correction": "À partir de 80 dB, l'employeur doit mettre à disposition des protections individuelles (bouchons d'oreilles)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle action simple permet d'économiser l'eau à la maison ?",
                    "answerOptions": [
                        {"text": "Installer des mousseurs sur les robinets", "isCorrect": True},
                        {"text": "Laisser couler l'eau pendant le brossage des dents", "isCorrect": False},
                        {"text": "Prendre des bains plutôt que des douches", "isCorrect": False},
                        {"text": "Laver sa voiture tous les jours", "isCorrect": False}
                    ],
                    "correction": "Le mousseur réduit le débit d'eau tout en gardant la même pression."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel pictogramme sur une bouteille indique que le produit est inflammable ?",
                    "answerOptions": [
                        {"text": "Une flamme", "isCorrect": True},
                        {"text": "Une tête de mort", "isCorrect": False},
                        {"text": "Un point d'exclamation", "isCorrect": False},
                        {"text": "Un poisson mort", "isCorrect": False}
                    ],
                    "correction": "Ce symbole prévient que le produit peut s'enflammer facilement au contact d'une source de chaleur."
                },
                {
                    "questionNumber": 32,
                    "question": "Qu'est-ce que l'empreinte carbone ?",
                    "answerOptions": [
                        {"text": "La quantité de gaz à effet de serre émise par une activité", "isCorrect": True},
                        {"text": "Une trace de pas dans le charbon", "isCorrect": False},
                        {"text": "Le prix du carbone sur le marché", "isCorrect": False},
                        {"text": "La couleur noire d'un produit", "isCorrect": False}
                    ],
                    "correction": "Elle permet de mesurer l'impact d'un individu ou d'une entreprise sur le changement climatique."
                },
                {
                    "questionNumber": 33,
                    "question": "Pourquoi faut-il limiter l'usage des pesticides ?",
                    "answerOptions": [
                        {"text": "Pour protéger la biodiversité et la santé humaine", "isCorrect": True},
                        {"text": "Pour faire pousser les plantes plus vite", "isCorrect": False},
                        {"text": "Pour nettoyer les rues", "isCorrect": False},
                        {"text": "Parce qu'ils sentent mauvais", "isCorrect": False}
                    ],
                    "correction": "Les pesticides polluent les nappes phréatiques et peuvent être toxiques pour les agriculteurs et consommateurs."
                },
                {
                    "questionNumber": 34,
                    "question": "Qu'est-ce que l'obsolescence programmée ?",
                    "answerOptions": [
                        {"text": "Réduire délibérément la durée de vie d'un produit", "isCorrect": True},
                        {"text": "Réparer un appareil gratuitement", "isCorrect": False},
                        {"text": "Fabriquer des produits très solides", "isCorrect": False},
                        {"text": "Un nouveau mode de recyclage", "isCorrect": False}
                    ],
                    "correction": "C'est une stratégie industrielle visant à forcer le consommateur à acheter un nouveau modèle."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le rôle de la couche d'ozone ?",
                    "answerOptions": [
                        {"text": "Filtrer les rayons ultraviolets (UV) du soleil", "isCorrect": True},
                        {"text": "Produire de la pluie", "isCorrect": False},
                        {"text": "Empêcher le vent de souffler", "isCorrect": False},
                        {"text": "Éclairer la lune", "isCorrect": False}
                    ],
                    "correction": "Sans couche d'ozone, la vie terrestre serait menacée par l'intensité des rayonnements solaires."
                },
                {
                    "questionNumber": 36,
                    "question": "Qu'est-ce qu'un circuit court alimentaire ?",
                    "answerOptions": [
                        {"text": "Une vente avec maximum un intermédiaire entre producteur et consommateur", "isCorrect": True},
                        {"text": "Un repas mangé très rapidement", "isCorrect": False},
                        {"text": "Un produit importé par avion", "isCorrect": False},
                        {"text": "La vente en supermarché", "isCorrect": False}
                    ],
                    "correction": "Il permet de limiter les transports et de mieux rémunérer le producteur."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'impact de la déforestation ?",
                    "answerOptions": [
                        {"text": "Perte de biodiversité et accélération du réchauffement", "isCorrect": True},
                        {"text": "Plus de place pour les maisons", "isCorrect": False},
                        {"text": "Amélioration de la qualité de l'air", "isCorrect": False},
                        {"text": "Diminution du niveau de la mer", "isCorrect": False}
                    ],
                    "correction": "Les forêts absorbent le CO2. Leur destruction libère ce gaz et détruit les habitats animaux."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment appelle-t-on le recyclage des déchets organiques ?",
                    "answerOptions": [
                        {"text": "Le compostage", "isCorrect": True},
                        {"text": "Le brûlage", "isCorrect": False},
                        {"text": "L'enfouissement", "isCorrect": False},
                        {"text": "Le déshabillage", "isCorrect": False}
                    ],
                    "correction": "Le compostage transforme les épluchures et restes de repas en engrais naturel."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle est l'origine des pluies acides ?",
                    "answerOptions": [
                        {"text": "La pollution atmosphérique par le soufre et l'azote", "isCorrect": True},
                        {"text": "Le sel de mer", "isCorrect": False},
                        {"text": "L'évaporation des piscines", "isCorrect": False},
                        {"text": "La fonte des glaces", "isCorrect": False}
                    ],
                    "correction": "Elles dégradent les forêts, les lacs et les bâtiments en pierre."
                },
                {
                    "questionNumber": 40,
                    "question": "Que signifie le ruban de Möbius sur un emballage ?",
                    "answerOptions": [
                        {"text": "Le produit est techniquement recyclable", "isCorrect": True},
                        {"text": "Le produit est bio", "isCorrect": False},
                        {"text": "Le produit est dangereux", "isCorrect": False},
                        {"text": "Le produit est gratuit", "isCorrect": False}
                    ],
                    "correction": "C'est le symbole universel du recyclage."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : RISQUES PROFESSIONNELS ET PRÉVENTION (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : RISQUES PROFESSIONNELS ET PRÉVENTION",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Qu'est-ce qu'un accident du travail ?",
                    "answerOptions": [
                        {"text": "Un événement soudain entraînant une lésion durant l'activité professionnelle", "isCorrect": True},
                        {"text": "Une maladie qui arrive lentement", "isCorrect": False},
                        {"text": "Un accident qui a lieu le dimanche à la maison", "isCorrect": False},
                        {"text": "Une dispute avec un collègue", "isCorrect": False}
                    ],
                    "correction": "L'accident doit être daté précisément et survenu par le fait ou à l'occasion du travail."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la différence entre un danger et un risque ?",
                    "answerOptions": [
                        {"text": "Le danger est la cause, le risque est l'exposition au danger", "isCorrect": True},
                        {"text": "Le danger est grave, le risque est léger", "isCorrect": False},
                        {"text": "C'est la même chose", "isCorrect": False},
                        {"text": "Le risque est obligatoire", "isCorrect": False}
                    ],
                    "correction": "Exemple : Un couteau est un danger. L'utiliser pour couper est un risque de coupure."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel document obligatoire recense tous les risques de l'entreprise ?",
                    "answerOptions": [
                        {"text": "Le Document Unique (DUERP)", "isCorrect": True},
                        {"text": "Le règlement intérieur", "isCorrect": False},
                        {"text": "La fiche de paie", "isCorrect": False},
                        {"text": "Le contrat de travail", "isCorrect": False}
                    ],
                    "correction": "Le DUERP doit être mis à jour au moins une fois par an."
                },
                {
                    "questionNumber": 44,
                    "question": "Qu'est-ce qu'un EPI ?",
                    "answerOptions": [
                        {"text": "Équipement de Protection Individuelle", "isCorrect": True},
                        {"text": "Élément de Prévention Interne", "isCorrect": False},
                        {"text": "Étude de Protection Incendie", "isCorrect": False},
                        {"text": "Évaluation de la Pression Infirmière", "isCorrect": False}
                    ],
                    "correction": "Exemples : casque, gants, lunettes de sécurité, chaussures de sécurité."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle est la priorité dans les principes généraux de prévention ?",
                    "answerOptions": [
                        {"text": "Éviter le risque (supprimer le danger)", "isCorrect": True},
                        {"text": "Donner des gants à tout le monde", "isCorrect": False},
                        {"text": "Mettre une affiche de sécurité", "isCorrect": False},
                        {"text": "Former les salariés au secourisme", "isCorrect": False}
                    ],
                    "correction": "La meilleure prévention est d'éliminer la cause du risque dès la conception."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment appelle-t-on les maladies liées à des gestes répétitifs (ex: tendinite) ?",
                    "answerOptions": [
                        {"text": "Troubles Musculo-Squelettiques (TMS)", "isCorrect": True},
                        {"text": "Accidents de trajet", "isCorrect": False},
                        {"text": "Maladies contagieuses", "isCorrect": False},
                        {"text": "Fatigue nerveuse", "isCorrect": False}
                    ],
                    "correction": "Les TMS représentent la première cause de maladie professionnelle en France."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est la définition de l'ergonomie ?",
                    "answerOptions": [
                        {"text": "Adapter le travail à l'homme", "isCorrect": True},
                        {"text": "Forcer l'homme à travailler plus vite", "isCorrect": False},
                        {"text": "Acheter les meubles les moins chers", "isCorrect": False},
                        {"text": "Nettoyer les machines", "isCorrect": False}
                    ],
                    "correction": "L'ergonomie vise à améliorer le confort, la sécurité et l'efficacité au poste de travail."
                },
                {
                    "questionNumber": 48,
                    "question": "Qu'est-ce que la charge mentale ?",
                    "answerOptions": [
                        {"text": "Le poids des informations et du stress intellectuel", "isCorrect": True},
                        {"text": "Le poids d'un casque sur la tête", "isCorrect": False},
                        {"text": "La fatigue après une séance de sport", "isCorrect": False},
                        {"text": "Le nombre d'heures supplémentaires", "isCorrect": False}
                    ],
                    "correction": "Une charge mentale trop élevée peut mener à des erreurs et au burnout."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel organisme conseille les entreprises en matière de prévention et d'hygiène ?",
                    "answerOptions": [
                        {"text": "La Médecine du Travail", "isCorrect": True},
                        {"text": "La Banque de France", "isCorrect": False},
                        {"text": "La Mairie", "isCorrect": False},
                        {"text": "Pôle Emploi", "isCorrect": False}
                    ],
                    "correction": "Le médecin du travail vérifie l'aptitude des salariés et surveille leur état de santé."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le risque principal lors de la manipulation de produits chimiques ?",
                    "answerOptions": [
                        {"text": "Brûlure, intoxication ou allergie", "isCorrect": True},
                        {"text": "Chute de plain-pied", "isCorrect": False},
                        {"text": "Bruit excessif", "isCorrect": False},
                        {"text": "Électrocution", "isCorrect": False}
                    ],
                    "correction": "Il faut impérativement lire l'étiquette et la FDS (Fiche de Données de Sécurité)."
                },
                {
                    "questionNumber": 51,
                    "question": "Que signifie un panneau triangulaire jaune avec un éclair ?",
                    "answerOptions": [
                        {"text": "Danger électrique", "isCorrect": True},
                        {"text": "Interdiction de passer", "isCorrect": False},
                        {"text": "Zone de silence", "isCorrect": False},
                        {"text": "Sortie de secours", "isCorrect": False}
                    ],
                    "correction": "C'est un panneau d'avertissement d'un risque d'électrisation."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la définition d'une maladie professionnelle ?",
                    "answerOptions": [
                        {"text": "Une maladie causée par l'exposition prolongée à un risque au travail", "isCorrect": True},
                        {"text": "Une grippe attrapée au bureau", "isCorrect": False},
                        {"text": "Une blessure faite avec un tournevis", "isCorrect": False},
                        {"text": "Un stress avant de partir en vacances", "isCorrect": False}
                    ],
                    "correction": "Elle doit être inscrite dans un tableau officiel pour être reconnue par la Sécurité Sociale."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle du CSE (Comité Social et Économique) ?",
                    "answerOptions": [
                        {"text": "Représenter les salariés et traiter les questions de sécurité", "isCorrect": True},
                        {"text": "Fixer les prix de vente des produits", "isCorrect": False},
                        {"text": "Recruter les nouveaux directeurs", "isCorrect": False},
                        {"text": "Gérer uniquement la machine à café", "isCorrect": False}
                    ],
                    "correction": "Il participe à l'amélioration des conditions de travail."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le risque lié à une ambiance lumineuse insuffisante ?",
                    "answerOptions": [
                        {"text": "Fatigue visuelle et risque d'accident", "isCorrect": True},
                        {"text": "Surdité", "isCorrect": False},
                        {"text": "Mal de gorge", "isCorrect": False},
                        {"text": "Coup de soleil", "isCorrect": False}
                    ],
                    "correction": "Un bon éclairage est nécessaire pour effectuer des tâches de précision en sécurité."
                },
                {
                    "questionNumber": 55,
                    "question": "Qu'est-ce qu'une ambiance thermique inconfortable au travail ?",
                    "answerOptions": [
                        {"text": "Une température trop haute ou trop basse pour l'activité", "isCorrect": True},
                        {"text": "Une couleur de mur trop vive", "isCorrect": False},
                        {"text": "Une climatisation qui ne fait pas de bruit", "isCorrect": False},
                        {"text": "Un bureau trop grand", "isCorrect": False}
                    ],
                    "correction": "La chaleur peut provoquer des malaises et le froid une perte de dextérité."
                },
                {
                    "questionNumber": 56,
                    "question": "À quoi sert le balisage de sécurité (ruban rouge et blanc) ?",
                    "answerOptions": [
                        {"text": "Délimiter une zone de danger temporaire", "isCorrect": True},
                        {"text": "Décorer l'entrée", "isCorrect": False},
                        {"text": "Indiquer le chemin de la cantine", "isCorrect": False},
                        {"text": "Mesurer la longueur d'un mur", "isCorrect": False}
                    ],
                    "correction": "Il empêche l'accès aux personnes non autorisées à une zone à risques (travaux, fuite)."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle est la durée légale du travail hebdomadaire pour un temps plein ?",
                    "answerOptions": [
                        {"text": "35 heures", "isCorrect": True},
                        {"text": "39 heures", "isCorrect": False},
                        {"text": "48 heures", "isCorrect": False},
                        {"text": "20 heures", "isCorrect": False}
                    ],
                    "correction": "C'est la durée de référence, au-delà on parle d'heures supplémentaires."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment appelle-t-on le fait d'être victime de harcèlement moral ?",
                    "answerOptions": [
                        {"text": "Un Risque Psycho-Social (RPS)", "isCorrect": True},
                        {"text": "Un risque biologique", "isCorrect": False},
                        {"text": "Un risque mécanique", "isCorrect": False},
                        {"text": "Un accident de trajet", "isCorrect": False}
                    ],
                    "correction": "Les RPS nuisent à la santé mentale et physique des travailleurs."
                },
                {
                    "questionNumber": 59,
                    "question": "Pourquoi faut-il porter des chaussures de sécurité ?",
                    "answerOptions": [
                        {"text": "Éviter l'écrasement, la perforation et la glissade", "isCorrect": True},
                        {"text": "Pour courir plus vite", "isCorrect": False},
                        {"text": "Parce qu'elles sont gratuites", "isCorrect": False},
                        {"text": "Pour ne pas salir ses chaussettes", "isCorrect": False}
                    ],
                    "correction": "C'est un EPI indispensable sur de nombreux chantiers et ateliers."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le danger principal de l'amiante ?",
                    "answerOptions": [
                        {"text": "Inhalation de fibres invisibles causant des cancers", "isCorrect": True},
                        {"text": "Risque d'explosion", "isCorrect": False},
                        {"text": "Brûlure de la peau", "isCorrect": False},
                        {"text": "Odeur insupportable", "isCorrect": False}
                    ],
                    "correction": "L'amiante est interdite depuis 1997 en France car ses fibres s'insèrent profondément dans les poumons."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : CONSOMMATION ET BUDGET (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : CONSOMMATION ET BUDGET",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Qu'est-ce que le reste à vivre ?",
                    "answerOptions": [
                        {"text": "La somme restante après avoir payé toutes les charges fixes", "isCorrect": True},
                        {"text": "Le montant du salaire brut", "isCorrect": False},
                        {"text": "Le prix total des courses", "isCorrect": False},
                        {"text": "Le montant de l'épargne", "isCorrect": False}
                    ],
                    "correction": "Il permet de payer l'alimentation, les loisirs et de faire face aux imprévus."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la différence entre le salaire brut et le salaire net ?",
                    "answerOptions": [
                        {"text": "Les cotisations sociales salariales", "isCorrect": True},
                        {"text": "Les impôts sur le revenu", "isCorrect": False},
                        {"text": "Le montant des pourboires", "isCorrect": False},
                        {"text": "Les frais de transport", "isCorrect": False}
                    ],
                    "correction": "Le net est ce qui est réellement versé sur le compte bancaire du salarié."
                },
                {
                    "questionNumber": 63,
                    "question": "Qu'est-ce qu'un crédit à la consommation ?",
                    "answerOptions": [
                        {"text": "Un prêt pour acheter des biens d'équipement (voiture, TV...)", "isCorrect": True},
                        {"text": "Un prêt pour acheter une maison", "isCorrect": False},
                        {"text": "Une aide gratuite de l'État", "isCorrect": False},
                        {"text": "Le montant des intérêts du livret A", "isCorrect": False}
                    ],
                    "correction": "Attention au surendettement : un crédit engage et doit être remboursé."
                },
                {
                    "questionNumber": 64,
                    "question": "Que signifie le sigle TAEG sur un contrat de prêt ?",
                    "answerOptions": [
                        {"text": "Taux Annuel Effectif Global", "isCorrect": True},
                        {"text": "Tarif d'Achat Électrique Garanti", "isCorrect": False},
                        {"text": "Taxe sur l'Argent Emprunté", "isCorrect": False},
                        {"text": "Taux d'Assurance En Groupe", "isCorrect": False}
                    ],
                    "correction": "C'est le coût total du crédit, incluant les intérêts et les frais de dossier."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la fonction d'une assurance ?",
                    "answerOptions": [
                        {"text": "Protéger contre les conséquences financières d'un risque", "isCorrect": True},
                        {"text": "Rendre riche en cas d'accident", "isCorrect": False},
                        {"text": "Empêcher les accidents d'arriver", "isCorrect": False},
                        {"text": "Payer les factures d'électricité", "isCorrect": False}
                    ],
                    "correction": "En échange d'une cotisation, l'assureur prend en charge les dommages subis ou causés."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel document récapitule les ressources et les dépenses ?",
                    "answerOptions": [
                        {"text": "Le budget", "isCorrect": True},
                        {"text": "La fiche de paie", "isCorrect": False},
                        {"text": "Le ticket de caisse", "isCorrect": False},
                        {"text": "Le bail", "isCorrect": False}
                    ],
                    "correction": "Établir un budget permet de gérer son argent et d'éviter les découverts."
                },
                {
                    "questionNumber": 67,
                    "question": "Qu'est-ce qu'une charge fixe ?",
                    "answerOptions": [
                        {"text": "Une dépense régulière et obligatoire (ex: Loyer)", "isCorrect": True},
                        {"text": "L'achat d'un nouveau vêtement", "isCorrect": False},
                        {"text": "Une sortie au cinéma", "isCorrect": False},
                        {"text": "Un cadeau d'anniversaire", "isCorrect": False}
                    ],
                    "correction": "Elles sont prévisibles et tombent chaque mois à la même date."
                },
                {
                    "questionNumber": 68,
                    "question": "Que signifie le Nutri-Score sur les emballages ?",
                    "answerOptions": [
                        {"text": "La qualité nutritionnelle du produit (de A à E)", "isCorrect": True},
                        {"text": "Le prix du produit au kilo", "isCorrect": False},
                        {"text": "Le temps de cuisson recommandé", "isCorrect": False},
                        {"text": "L'origine géographique du produit", "isCorrect": False}
                    ],
                    "correction": "Il aide le consommateur à comparer les produits d'un même rayon."
                },
                {
                    "questionNumber": 69,
                    "question": "Qu'est-ce que la colocation ?",
                    "answerOptions": [
                        {"text": "Le partage d'un logement par plusieurs locataires", "isCorrect": True},
                        {"text": "Le fait de louer un garage", "isCorrect": False},
                        {"text": "L'achat d'un appartement à deux", "isCorrect": False},
                        {"text": "Vivre dans un hôtel", "isCorrect": False}
                    ],
                    "correction": "Elle permet de diviser le loyer et les charges."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle est l'utilité du livret A ?",
                    "answerOptions": [
                        {"text": "Une épargne de précaution disponible à tout moment", "isCorrect": True},
                        {"text": "Une assurance vie", "isCorrect": False},
                        {"text": "Un compte pour payer ses courses", "isCorrect": False},
                        {"text": "Un dictionnaire bancaire", "isCorrect": False}
                    ],
                    "correction": "C'est un placement sécurisé dont le taux est fixé par l'État."
                },
                {
                    "questionNumber": 71,
                    "question": "Que signifie le sigle TVA ?",
                    "answerOptions": [
                        {"text": "Taxe sur la Valeur Ajoutée", "isCorrect": True},
                        {"text": "Tarif de Vente Annuel", "isCorrect": False},
                        {"text": "Taxe sur les Véhicules Anciens", "isCorrect": False},
                        {"text": "Traitement de la Vie Active", "isCorrect": False}
                    ],
                    "correction": "C'est un impôt indirect payé par le consommateur final sur ses achats."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le but d'un dépôt de garantie (caution) pour un logement ?",
                    "answerOptions": [
                        {"text": "Couvrir les éventuelles dégradations en fin de bail", "isCorrect": True},
                        {"text": "Payer les honoraires de l'agence", "isCorrect": False},
                        {"text": "Acheter les meubles du propriétaire", "isCorrect": False},
                        {"text": "Assurer le voisin contre le bruit", "isCorrect": False}
                    ],
                    "correction": "Il doit être restitué au locataire si le logement est rendu en bon état."
                },
                {
                    "questionNumber": 73,
                    "question": "Qu'est-ce qu'une publicité mensongère ?",
                    "answerOptions": [
                        {"text": "Une publicité qui donne des informations fausses ou trompeuses", "isCorrect": True},
                        {"text": "Une publicité qui ne passe pas à la télé", "isCorrect": False},
                        {"text": "Une publicité qui coûte très cher", "isCorrect": False},
                        {"text": "Une publicité pour un produit gratuit", "isCorrect": False}
                    ],
                    "correction": "C'est un délit puni par le Code de la consommation."
                },
                {
                    "questionNumber": 74,
                    "question": "Que signifie le prélèvement à la source ?",
                    "answerOptions": [
                        {"text": "L'impôt est déduit directement du salaire chaque mois", "isCorrect": True},
                        {"text": "On prend de l'eau dans une source", "isCorrect": False},
                        {"text": "L'employeur paie le loyer du salarié", "isCorrect": False},
                        {"text": "Le salaire est versé en liquide", "isCorrect": False}
                    ],
                    "correction": "Il permet de payer son impôt sur le revenu en temps réel."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le rôle du garant pour un prêt ou une location ?",
                    "answerOptions": [
                        {"text": "Payer à la place de l'emprunteur ou du locataire en cas de défaut", "isCorrect": True},
                        {"text": "Surveiller les travaux", "isCorrect": False},
                        {"text": "Signer le contrat de mariage", "isCorrect": False},
                        {"text": "Prêter sa voiture", "isCorrect": False}
                    ],
                    "correction": "C'est une personne physique ou un organisme qui se porte caution."
                },
                {
                    "questionNumber": 76,
                    "question": "Qu'est-ce qu'un agio bancaire ?",
                    "answerOptions": [
                        {"text": "Frais payés à la banque en cas de découvert", "isCorrect": True},
                        {"text": "Un bonus de fin d'année", "isCorrect": False},
                        {"text": "Une nouvelle carte bancaire", "isCorrect": False},
                        {"text": "Un cadeau de bienvenue", "isCorrect": False}
                    ],
                    "correction": "Ils correspondent aux intérêts débiteurs quand le solde est négatif."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel document détaille les éléments d'un salaire (primes, cotisations...) ?",
                    "answerOptions": [
                        {"text": "Le bulletin de paie", "isCorrect": True},
                        {"text": "Le RIB", "isCorrect": False},
                        {"text": "Le carnet de chèques", "isCorrect": False},
                        {"text": "Le contrat de bail", "isCorrect": False}
                    ],
                    "correction": "Il doit être conservé sans limitation de durée (pour la retraite)."
                },
                {
                    "questionNumber": 78,
                    "question": "Que signifie le sigle SMIC ?",
                    "answerOptions": [
                        {"text": "Salaire Minimum Interprofessionnel de Croissance", "isCorrect": True},
                        {"text": "Salaire Moyen d'Intérêt Collectif", "isCorrect": False},
                        {"text": "Système de Mesure de l'Indice de Consommation", "isCorrect": False},
                        {"text": "Seuil de Mobilité Individuelle Court", "isCorrect": False}
                    ],
                    "correction": "C'est le salaire horaire minimum en dessous duquel un salarié ne peut être payé."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel organisme peut aider en cas de surendettement ?",
                    "answerOptions": [
                        {"text": "La Commission de surendettement (Banque de France)", "isCorrect": True},
                        {"text": "La police", "isCorrect": False},
                        {"text": "Le tribunal correctionnel", "isCorrect": False},
                        {"text": "La mairie de Paris uniquement", "isCorrect": False}
                    ],
                    "correction": "Elle permet de négocier un plan de remboursement ou un effacement des dettes."
                },
                {
                    "questionNumber": 80,
                    "question": "Qu'est-ce que la protection juridique ?",
                    "answerOptions": [
                        {"text": "Une assurance pour couvrir les frais de justice en cas de litige", "isCorrect": True},
                        {"text": "Un avocat gratuit pour tout le monde", "isCorrect": False},
                        {"text": "La police qui protège la maison", "isCorrect": False},
                        {"text": "Une loi pour protéger la nature", "isCorrect": False}
                    ],
                    "correction": "Elle permet d'être assisté ou représenté par un professionnel du droit."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : SECOURISME ET SST (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : SECOURISME ET SST",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Que signifie le sigle SST ?",
                    "answerOptions": [
                        {"text": "Sauveteur Secouriste du Travail", "isCorrect": True},
                        {"text": "Service de Sécurité Technique", "isCorrect": False},
                        {"text": "Santé et Sécurité Totale", "isCorrect": False},
                        {"text": "Soin de Secours Thérapeutique", "isCorrect": False}
                    ],
                    "correction": "C'est un membre du personnel formé pour intervenir en cas d'accident et pour la prévention."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la première étape du protocole d'intervention du SST ?",
                    "answerOptions": [
                        {"text": "Protéger", "isCorrect": True},
                        {"text": "Secourir", "isCorrect": False},
                        {"text": "Alerter", "isCorrect": False},
                        {"text": "Examiner", "isCorrect": False}
                    ],
                    "correction": "On protège d'abord pour éviter un sur-accident (sécurisation de la zone)."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel numéro d'urgence est valable dans toute l'Union Européenne ?",
                    "answerOptions": [
                        {"text": "112", "isCorrect": True},
                        {"text": "15", "isCorrect": False},
                        {"text": "18", "isCorrect": False},
                        {"text": "17", "isCorrect": False}
                    ],
                    "correction": "Le 112 peut être appelé gratuitement depuis n'importe quel téléphone fixe ou portable."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment vérifier si une personne est inconsciente ?",
                    "answerOptions": [
                        {"text": "Lui parler et lui demander de serrer la main", "isCorrect": True},
                        {"text": "Lui verser de l'eau froide sur le visage", "isCorrect": False},
                        {"text": "Lui donner des claques", "isCorrect": False},
                        {"text": "Lui crier dans l'oreille", "isCorrect": False}
                    ],
                    "correction": "On lui pose des questions simples : 'Est-ce que vous m'entendez ? Serrez-moi la main !'."
                },
                {
                    "questionNumber": 85,
                    "question": "Que doit-on faire si une victime inconsciente respire normalement ?",
                    "answerOptions": [
                        {"text": "La mettre en Position Latérale de Sécurité (PLS)", "isCorrect": True},
                        {"text": "Lui faire un massage cardiaque", "isCorrect": False},
                        {"text": "Lui donner à boire", "isCorrect": False},
                        {"text": "La laisser sur le dos", "isCorrect": False}
                    ],
                    "correction": "La PLS permet de maintenir les voies respiratoires libres et d'éviter l'étouffement en cas de vomissements."
                },
                {
                    "questionNumber": 86,
                    "question": "Comment appelle-t-on l'arrêt cardiaque ?",
                    "answerOptions": [
                        {"text": "Victime inconsciente qui ne respire pas", "isCorrect": True},
                        {"text": "Victime qui a mal au bras", "isCorrect": False},
                        {"text": "Victime qui saigne du nez", "isCorrect": False},
                        {"text": "Victime qui fait une crise d'épilepsie", "isCorrect": False}
                    ],
                    "correction": "Il nécessite une intervention immédiate (massage et défibrillateur)."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est le geste à effectuer en cas d'obstruction totale des voies aériennes ?",
                    "answerOptions": [
                        {"text": "5 claques dans le dos puis 5 compressions abdominales", "isCorrect": True},
                        {"text": "Lui donner un verre d'eau", "isCorrect": False},
                        {"text": "L'allonger par terre", "isCorrect": False},
                        {"text": "Lui demander de lever les bras", "isCorrect": False}
                    ],
                    "correction": "C'est la méthode de Heimlich, pour expulser le corps étranger."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment arrêter une hémorragie externe visible ?",
                    "answerOptions": [
                        {"text": "Effectuer une compression directe sur la plaie", "isCorrect": True},
                        {"text": "Mettre du coton", "isCorrect": False},
                        {"text": "Faire un garrot immédiatement", "isCorrect": False},
                        {"text": "Laisser couler pour nettoyer la plaie", "isCorrect": False}
                    ],
                    "correction": "On appuie fort sur la zone qui saigne pour stopper l'écoulement du sang."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel appareil automatique permet d'aider le cœur à repartir ?",
                    "answerOptions": [
                        {"text": "Le DAE (Défibrillateur Automatisé Externe)", "isCorrect": True},
                        {"text": "Le tensiomètre", "isCorrect": False},
                        {"text": "L'oxymètre", "isCorrect": False},
                        {"text": "Le stéthoscope", "isCorrect": False}
                    ],
                    "correction": "L'appareil donne des instructions vocales et analyse lui-même le rythme cardiaque."
                },
                {
                    "questionNumber": 90,
                    "question": "Que signifie le message 'Alerter' ?",
                    "answerOptions": [
                        {"text": "Donner les informations précises aux secours (15, 18 ou 112)", "isCorrect": True},
                        {"text": "Crier 'Au secours' dans le couloir", "isCorrect": False},
                        {"text": "Appeler ses parents", "isCorrect": False},
                        {"text": "Prévenir la police", "isCorrect": False}
                    ],
                    "correction": "Il faut préciser le lieu, la nature de l'accident, le nombre de victimes et leur état."
                },
                {
                    "questionNumber": 91,
                    "question": "Que faire en cas de brûlure thermique ?",
                    "answerOptions": [
                        {"text": "Arroser à l'eau tempérée pendant 15 minutes", "isCorrect": True},
                        {"text": "Mettre de la glace", "isCorrect": False},
                        {"text": "Mettre du dentifrice ou du beurre", "isCorrect": False},
                        {"text": "Percer les cloques", "isCorrect": False}
                    ],
                    "correction": "L'eau refroidit les tissus et évite que la chaleur ne continue de brûler en profondeur."
                },
                {
                    "questionNumber": 92,
                    "question": "Comment s'appelle l'examen de la victime ?",
                    "answerOptions": [
                        {"text": "Recherche des signes de vie (conscience et respiration)", "isCorrect": True},
                        {"text": "Vérification des papiers d'identité", "isCorrect": False},
                        {"text": "Faire une prise de sang", "isCorrect": False},
                        {"text": "Prendre la température", "isCorrect": False}
                    ],
                    "correction": "L'examen permet de décider quel geste de secours effectuer."
                },
                {
                    "questionNumber": 93,
                    "question": "Que doit faire le SST après avoir alerté ?",
                    "answerOptions": [
                        {"text": "Surveiller la victime et attendre les secours", "isCorrect": True},
                        {"text": "Retourner travailler", "isCorrect": False},
                        {"text": "Partir pour laisser la place", "isCorrect": False},
                        {"text": "Lui donner des médicaments", "isCorrect": False}
                    ],
                    "correction": "La surveillance permet de réagir si l'état de la victime s'aggrave."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle est la fréquence du massage cardiaque chez l'adulte ?",
                    "answerOptions": [
                        {"text": "100 à 120 compressions par minute", "isCorrect": True},
                        {"text": "10 compressions par minute", "isCorrect": False},
                        {"text": "500 compressions par minute", "isCorrect": False},
                        {"text": "Peu importe la vitesse", "isCorrect": False}
                    ],
                    "correction": "C'est un rythme soutenu (environ 2 par seconde) pour faire circuler le sang mécaniquement."
                },
                {
                    "questionNumber": 95,
                    "question": "À quoi sert le registre d'accidents du travail ?",
                    "answerOptions": [
                        {"text": "Noter tous les accidents, même légers, n'entraînant pas d'arrêt", "isCorrect": True},
                        {"text": "Écrire des poèmes", "isCorrect": False},
                        {"text": "Noter les retardataires", "isCorrect": False},
                        {"text": "Ranger les factures d'eau", "isCorrect": False}
                    ],
                    "correction": "Il permet de garder une trace légale et d'analyser les risques récurrents."
                },
                {
                    "questionNumber": 96,
                    "question": "Que faire en cas de malaise ?",
                    "answerOptions": [
                        {"text": "Mettre la victime au repos et l'interroger", "isCorrect": True},
                        {"text": "Lui donner du sucre systématiquement", "isCorrect": False},
                        {"text": "La faire marcher pour la réveiller", "isCorrect": False},
                        {"text": "Ne rien faire et attendre", "isCorrect": False}
                    ],
                    "correction": "On lui demande si elle suit un traitement ou si c'est la première fois."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le but de l'arbre des causes ?",
                    "answerOptions": [
                        {"text": "Comprendre l'enchaînement des faits pour éviter qu'un accident ne se reproduise", "isCorrect": True},
                        {"text": "Trouver un coupable", "isCorrect": False},
                        {"text": "Définir le montant de l'amende", "isCorrect": False},
                        {"text": "Calculer le temps perdu", "isCorrect": False}
                    ],
                    "correction": "C'est une méthode d'analyse a posteriori pour la prévention."
                },
                {
                    "questionNumber": 98,
                    "question": "Qui est responsable de la fourniture des EPI ?",
                    "answerOptions": [
                        {"text": "L'employeur", "isCorrect": True},
                        {"text": "Le salarié", "isCorrect": False},
                        {"text": "La médecine du travail", "isCorrect": False},
                        {"text": "L'inspecteur du travail", "isCorrect": False}
                    ],
                    "correction": "L'employeur doit fournir gratuitement les protections adaptées au poste."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle couleur de peau est un signe de détresse circulatoire (hémorragie) ?",
                    "answerOptions": [
                        {"text": "Pâleur extrême", "isCorrect": True},
                        {"text": "Rougeur intense", "isCorrect": False},
                        {"text": "Teinte bleutée", "isCorrect": False},
                        {"text": "Jaunisse", "isCorrect": False}
                    ],
                    "correction": "Le sang se retire de la peau pour irriguer les organes vitaux (cœur, cerveau)."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel appareil présent dans les lieux publics augmente les chances de survie à un arrêt cardiaque ?",
                    "answerOptions": [
                        {"text": "DAE", "isCorrect": True},
                        {"text": "Extincteur", "isCorrect": False},
                        {"text": "RIA", "isCorrect": False},
                        {"text": "BAES", "isCorrect": False}
                    ],
                    "correction": "Le DAE (Défibrillateur Automatisé Externe) guide le secouriste pas à pas."
                }
            ]
        }
    }
}