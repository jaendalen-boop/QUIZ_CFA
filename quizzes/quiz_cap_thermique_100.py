quiz_data = {
    "title": "Quiz CAP Monteur en Installations Thermiques (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE DES TUBES, MATÉRIAUX ET FAÇONNAGE (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE DES TUBES, MATÉRIAUX ET FAÇONNAGE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel état du cuivre est obligatoire pour réaliser un cintrage manuel sans recuit préalable ?",
                    "answerOptions": [
                        {"text": "Recuit", "isCorrect": True},
                        {"text": "Écroui dur", "isCorrect": False},
                        {"text": "Trempé", "isCorrect": False},
                        {"text": "Laminé brut", "isCorrect": False}
                    ],
                    "correction": "Le cuivre en couronne est 'recuit' (traité thermiquement), ce qui le rend malléable et permet de le dérouler et de le cintrer facilement à la main. Le cuivre en barre est 'écroui' (rigide)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la couleur normalisée de l'ogive d'une bouteille d'oxygène ?",
                    "answerOptions": [
                        {"text": "Blanc", "isCorrect": True},
                        {"text": "Marron", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False}
                    ],
                    "correction": "La norme européenne impose la couleur blanche pour l'ogive des bouteilles d'oxygène industriel et la couleur marron pour l'acétylène."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel outil est spécifiquement conçu pour réaliser des filetages sur des tubes en acier noir ?",
                    "answerOptions": [
                        {"text": "Filière", "isCorrect": True},
                        {"text": "Taraud", "isCorrect": False},
                        {"text": "Dudgeonnière", "isCorrect": False},
                        {"text": "Cintreuse", "isCorrect": False}
                    ],
                    "correction": "La filière sert à réaliser des filetages extérieurs sur les tubes, tandis que le taraud sert pour les filetages intérieurs."
                },
                {
                    "questionNumber": 4,
                    "question": "Que signifie l'acronyme PER pour les tubes de synthèse ?",
                    "answerOptions": [
                        {"text": "Polyéthylène Réticulé", "isCorrect": True},
                        {"text": "Polypropylène Extrudé Rigide", "isCorrect": False},
                        {"text": "Polychlorure Éthylène Renforcé", "isCorrect": False},
                        {"text": "Plastique Enduit Résistant", "isCorrect": False}
                    ],
                    "correction": "Le PER (Polyéthylène Réticulé) est un matériau plastique traité pour résister à la pression et à la température, très utilisé en hydrocâblé."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle précaution est impérative lors de l'assemblage de l'acier et du cuivre sur un même réseau ?",
                    "answerOptions": [
                        {"text": "Placer l'acier avant le cuivre", "isCorrect": True},
                        {"text": "Placer le cuivre avant l'acier", "isCorrect": False},
                        {"text": "Utiliser un raccord en laiton uniquement", "isCorrect": False},
                        {"text": "Intercaler un manchon en PVC pression", "isCorrect": False}
                    ],
                    "correction": "Il faut respecter le sens de circulation du fluide : 'Acier puis Cuivre'. Si le cuivre est placé avant, les ions cuivre migrent et corrodent l'acier (phénomène de pile galvanique)."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la température minimale approximative pour réaliser un brasage fort au cupro-phosphore ?",
                    "answerOptions": [
                        {"text": "700 degrés Celsius", "isCorrect": True},
                        {"text": "250 degrés Celsius", "isCorrect": False},
                        {"text": "400 degrés Celsius", "isCorrect": False},
                        {"text": "1500 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "Le brasage fort nécessite une température de fusion du métal d'apport supérieure à 450°C. Pour le cupro-phosphore, la température de travail se situe autour de 700°C à 800°C."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est le nom du raccord mécanique démontable souvent utilisé pour raccorder un radiateur ?",
                    "answerOptions": [
                        {"text": "Raccord union", "isCorrect": True},
                        {"text": "Manchon à braser", "isCorrect": False},
                        {"text": "Té égal", "isCorrect": False},
                        {"text": "Réduction concentrique", "isCorrect": False}
                    ],
                    "correction": "Le raccord union, aussi appelé '3 pièces', permet de démonter l'appareil sans avoir à couper la tuyauterie."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle pâte utilise-t-on avec la filasse pour l'étanchéité d'un réseau de chauffage ?",
                    "answerOptions": [
                        {"text": "Pâte à joint", "isCorrect": True},
                        {"text": "Colle néoprène", "isCorrect": False},
                        {"text": "Silicone sanitaire", "isCorrect": False},
                        {"text": "Mastic acrylique", "isCorrect": False}
                    ],
                    "correction": "L'étanchéité des filetages métalliques se fait traditionnellement avec de la filasse de lin et de la pâte à joint (type Kolmat ou Gebatout)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel gaz est utilisé comme protection inerte à l'intérieur du tube lors d'une soudure TIG sur inox ?",
                    "answerOptions": [
                        {"text": "Azote", "isCorrect": True},
                        {"text": "Oxygène", "isCorrect": False},
                        {"text": "Acétylène", "isCorrect": False},
                        {"text": "Propane", "isCorrect": False}
                    ],
                    "correction": "L'inertage (souvent à l'azote ou à l'argon) protège l'envers de la soudure contre l'oxydation (rochage) due à l'oxygène de l'air."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel outil utilise-t-on pour couper proprement un tube multicouche ?",
                    "answerOptions": [
                        {"text": "Pince coupe tube", "isCorrect": True},
                        {"text": "Scie à métaux", "isCorrect": False},
                        {"text": "Meuleuse d'angle", "isCorrect": False},
                        {"text": "Scie sabre électrique", "isCorrect": False}
                    ],
                    "correction": "La pince coupe-tube (ou ciseaux) assure une coupe nette et perpendiculaire sans créer de bavures ni de copeaux qui pourraient endommager les joints."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le rôle principal d'un fourreau lors de la traversée d'une dalle béton ?",
                    "answerOptions": [
                        {"text": "Protéger le tube mécaniquement", "isCorrect": True},
                        {"text": "Isoler thermiquement le tube", "isCorrect": False},
                        {"text": "Améliorer l'esthétique au sol", "isCorrect": False},
                        {"text": "Empêcher le passage des insectes", "isCorrect": False}
                    ],
                    "correction": "Le fourreau protège le tube des agressions mécaniques et chimiques du béton et permet la libre dilatation du tuyau."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment appelle-t-on l'opération consistant à élargir l'extrémité d'un tube cuivre pour y emboîter un autre tube ?",
                    "answerOptions": [
                        {"text": "Emboîture", "isCorrect": True},
                        {"text": "Piquage", "isCorrect": False},
                        {"text": "Soyage", "isCorrect": False},
                        {"text": "Rétreinte", "isCorrect": False}
                    ],
                    "correction": "L'emboîture permet d'assembler deux tubes de même diamètre par capillarité sans utiliser de manchon du commerce."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est l'avantage principal du tube multicouche par rapport au PER standard ?",
                    "answerOptions": [
                        {"text": "Il possède une barrière anti oxygène", "isCorrect": True},
                        {"text": "Il est beaucoup moins cher au mètre", "isCorrect": False},
                        {"text": "Il ne nécessite aucun outillage spécifique", "isCorrect": False},
                        {"text": "Il peut être soudé directement à la flamme", "isCorrect": False}
                    ],
                    "correction": "Le multicouche intègre une feuille d'aluminium qui bloque l'oxygène (limitant les boues) et réduit considérablement la dilatation thermique, en plus d'avoir une mémoire de forme."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelle est la dimension en millimètres correspondant à un tube acier fileté de désignation 1 pouce ?",
                    "answerOptions": [
                        {"text": "26x34", "isCorrect": True},
                        {"text": "15x21", "isCorrect": False},
                        {"text": "20x27", "isCorrect": False},
                        {"text": "33x42", "isCorrect": False}
                    ],
                    "correction": "La correspondance des dénominations courantes est : 1/2' = 15x21, 3/4' = 20x27, 1' = 26x34."
                },
                {
                    "questionNumber": 15,
                    "question": "Pourquoi doit-on ébavurer un tube cuivre après la coupe ?",
                    "answerOptions": [
                        {"text": "Pour éviter les perturbations hydrauliques et la corrosion", "isCorrect": True},
                        {"text": "Pour rendre le tube plus brillant et esthétique", "isCorrect": False},
                        {"text": "Pour modifier le diamètre extérieur du tube", "isCorrect": False},
                        {"text": "Pour durcir le métal avant la soudure", "isCorrect": False}
                    ],
                    "correction": "Les bavures créent des turbulences qui favorisent l'érosion-corrosion (piqûres) et peuvent endommager les joints lors de l'emboîtement."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel consommable est strictement interdit pour l'étanchéité des raccords gaz ?",
                    "answerOptions": [
                        {"text": "Téflon ruban standard", "isCorrect": True},
                        {"text": "Graisse graphitée", "isCorrect": False},
                        {"text": "Résine anaérobie", "isCorrect": False},
                        {"text": "Filasse avec pâte", "isCorrect": False}
                    ],
                    "correction": "Sur le gaz, l'utilisation du ruban PTFE (Téflon) standard est interdite car il ne garantit pas une étanchéité fiable dans le temps (sauf PTFE spécifique gaz). La filasse est autorisée selon les diamètres et pressions."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle technique d'assemblage est utilisée pour les tubes en acier galvanisé ?",
                    "answerOptions": [
                        {"text": "Filetage", "isCorrect": True},
                        {"text": "Soudure autogène", "isCorrect": False},
                        {"text": "Brasage fort", "isCorrect": False},
                        {"text": "Soudure à l'arc", "isCorrect": False}
                    ],
                    "correction": "Il est interdit de souder l'acier galvanisé car cela détruit la couche de zinc protectrice et dégage des vapeurs toxiques. On procède par filetage ou raccords à compression."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le nom de la pièce permettant de fixer les tubes aux murs ?",
                    "answerOptions": [
                        {"text": "Collier", "isCorrect": True},
                        {"text": "Rosace", "isCorrect": False},
                        {"text": "Mamelon", "isCorrect": False},
                        {"text": "Bouchon", "isCorrect": False}
                    ],
                    "correction": "Les colliers (simples ou doubles, isophoniques ou non) maintiennent les tubes. Les rosaces sont des éléments de finition."
                },
                {
                    "questionNumber": 19,
                    "question": "Pour cintrer un tube acier à chaud, quelle substance utilise-t-on pour le remplir afin d'éviter l'écrasement ?",
                    "answerOptions": [
                        {"text": "Sable sec", "isCorrect": True},
                        {"text": "Eau savonneuse", "isCorrect": False},
                        {"text": "Huile de coupe", "isCorrect": False},
                        {"text": "Limaille de fer", "isCorrect": False}
                    ],
                    "correction": "On remplit le tube de sable sec et tassé ('sable de Fontainebleau') pour répartir la pression uniformément et empêcher le tube de s'aplatir ou de plisser lors du cintrage à chaud."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle flamme obtient-on avec un excès d'acétylène au chalumeau ?",
                    "answerOptions": [
                        {"text": "Carburante", "isCorrect": True},
                        {"text": "Oxydante", "isCorrect": False},
                        {"text": "Neutre", "isCorrect": False},
                        {"text": "Normale", "isCorrect": False}
                    ],
                    "correction": "Une flamme carburante a un dard brillant et brouillé, signe d'un excès d'acétylène. Elle est utilisée pour certains brasages ou pour souder l'aluminium, mais pas l'acier."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : LES GÉNÉRATEURS ET ÉMETTEURS DE CHALEUR (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : LES GÉNÉRATEURS ET ÉMETTEURS DE CHALEUR",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Comment appelle-t-on une chaudière qui récupère la chaleur latente contenue dans les fumées ?",
                    "answerOptions": [
                        {"text": "Chaudière à condensation", "isCorrect": True},
                        {"text": "Chaudière basse température", "isCorrect": False},
                        {"text": "Chaudière atmosphérique", "isCorrect": False},
                        {"text": "Chaudière à tirage naturel", "isCorrect": False}
                    ],
                    "correction": "La chaudière à condensation refroidit les fumées pour faire passer la vapeur d'eau qu'elles contiennent de l'état gazeux à l'état liquide, récupérant ainsi une énergie supplémentaire (chaleur latente)."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel élément est indispensable sur l'arrivée d'eau froide d'un ballon d'eau chaude sanitaire ?",
                    "answerOptions": [
                        {"text": "Groupe de sécurité", "isCorrect": True},
                        {"text": "Réducteur de pression", "isCorrect": False},
                        {"text": "Vase d'expansion sanitaire", "isCorrect": False},
                        {"text": "Disconnecteur contrôlable", "isCorrect": False}
                    ],
                    "correction": "Le groupe de sécurité est obligatoire. Il remplit 4 fonctions : vanne d'arrêt, clapet anti-retour, soupape de sécurité (tarée à 7 bars) et vidange."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le principe de fonctionnement d'une pompe à chaleur aérothermique ?",
                    "answerOptions": [
                        {"text": "Capter les calories de l'air", "isCorrect": True},
                        {"text": "Capter les calories du sol", "isCorrect": False},
                        {"text": "Capter les calories de la nappe phréatique", "isCorrect": False},
                        {"text": "Capter les calories du rayonnement solaire", "isCorrect": False}
                    ],
                    "correction": "Une PAC aérothermique (Air/Eau ou Air/Air) prélève la chaleur présente dans l'air extérieur pour la restituer à l'intérieur du logement."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la température maximale de surface autorisée pour un plancher chauffant selon la réglementation actuelle ?",
                    "answerOptions": [
                        {"text": "28 degrés Celsius", "isCorrect": True},
                        {"text": "35 degrés Celsius", "isCorrect": False},
                        {"text": "50 degrés Celsius", "isCorrect": False},
                        {"text": "21 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "Pour éviter les problèmes physiologiques (jambes lourdes), la réglementation thermique limite la température de contact au sol à 28°C maximum."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel composant pulvérise le combustible en fines gouttelettes dans un brûleur fioul ?",
                    "answerOptions": [
                        {"text": "Gicleur", "isCorrect": True},
                        {"text": "Électrode", "isCorrect": False},
                        {"text": "Accrocheur de flamme", "isCorrect": False},
                        {"text": "Cellule photoélectrique", "isCorrect": False}
                    ],
                    "correction": "Le gicleur permet de nébuliser le fioul sous pression pour créer un mélange comburant/carburant homogène facilitant la combustion."
                },
                {
                    "questionNumber": 26,
                    "question": "Comment se nomme le mode de transmission de chaleur majoritaire d'un radiateur classique ?",
                    "answerOptions": [
                        {"text": "Convection", "isCorrect": True},
                        {"text": "Conduction", "isCorrect": False},
                        {"text": "Rayonnement", "isCorrect": False},
                        {"text": "Induction", "isCorrect": False}
                    ],
                    "correction": "Bien qu'on les appelle 'radiateurs', ces émetteurs chauffent l'air qui circule à leur contact et monte naturellement. C'est le phénomène de convection (environ 70 à 80% de l'émission)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel dispositif permet de régler la température pièce par pièce sur un radiateur ?",
                    "answerOptions": [
                        {"text": "Robinet thermostatique", "isCorrect": True},
                        {"text": "Té de réglage", "isCorrect": False},
                        {"text": "Purgeur manuel", "isCorrect": False},
                        {"text": "Robinet simple réglage", "isCorrect": False}
                    ],
                    "correction": "Le robinet thermostatique module le débit d'eau entrant dans le radiateur en fonction de la température ambiante de la pièce pour maintenir la consigne choisie."
                },
                {
                    "questionNumber": 28,
                    "question": "Pour qu'une chaudière à condensation fonctionne avec un rendement optimal, comment doit être la température de retour de l'eau ?",
                    "answerOptions": [
                        {"text": "La plus basse possible", "isCorrect": True},
                        {"text": "La plus haute possible", "isCorrect": False},
                        {"text": "Égale à la température de départ", "isCorrect": False},
                        {"text": "Supérieure à 60 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "Pour qu'il y ait condensation, la température de retour doit être inférieure au point de rosée des fumées (environ 50-55°C pour le gaz). Plus le retour est froid, plus ça condense."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le rôle de l'anode en magnésium dans un ballon d'eau chaude ?",
                    "answerOptions": [
                        {"text": "Protéger la cuve contre la corrosion", "isCorrect": True},
                        {"text": "Chauffer l'eau plus rapidement", "isCorrect": False},
                        {"text": "Mesurer la température de l'eau", "isCorrect": False},
                        {"text": "Filtrer le calcaire en suspension", "isCorrect": False}
                    ],
                    "correction": "C'est une anode 'sacrificielle'. Elle s'oxyde à la place de l'acier de la cuve, protégeant ainsi l'émail des micro-fissures et de la corrosion."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel équipement permet de transférer la chaleur du circuit primaire vers l'eau sanitaire sans mélange des fluides ?",
                    "answerOptions": [
                        {"text": "Échangeur", "isCorrect": True},
                        {"text": "Circulateur", "isCorrect": False},
                        {"text": "Disconnecteur", "isCorrect": False},
                        {"text": "Mélangeur", "isCorrect": False}
                    ],
                    "correction": "L'échangeur (à plaques ou tubulaire) permet le transfert thermique entre l'eau du chauffage (primaire) et l'eau potable (sanitaire) à travers une paroi métallique, sans contact direct."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la définition du COP d'une pompe à chaleur ?",
                    "answerOptions": [
                        {"text": "Coefficient de Performance", "isCorrect": True},
                        {"text": "Capacité Optimale de Pression", "isCorrect": False},
                        {"text": "Contrôle des Ondes Positives", "isCorrect": False},
                        {"text": "Circuit Ouvert Prioritaire", "isCorrect": False}
                    ],
                    "correction": "Le COP est le rapport entre la quantité d'énergie thermique restituée et la quantité d'énergie électrique consommée par la machine."
                },
                {
                    "questionNumber": 32,
                    "question": "Sur une chaudière ventouse, comment l'air comburant est-il amené au brûleur ?",
                    "answerOptions": [
                        {"text": "Par un conduit étanche relié à l'extérieur", "isCorrect": True},
                        {"text": "Par une grille de ventilation basse dans le mur", "isCorrect": False},
                        {"text": "Par les fuites naturelles des ouvrants", "isCorrect": False},
                        {"text": "Par un ventilateur placé dans le salon", "isCorrect": False}
                    ],
                    "correction": "La chaudière ventouse (ou étanche) prélève l'air frais directement dehors via un conduit concentrique ou séparé, ce qui ne nécessite pas de ventilation dans la pièce."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle bactérie peut se développer dans les réseaux d'eau chaude sanitaire stagnante entre 25 et 45 degrés ?",
                    "answerOptions": [
                        {"text": "Légionelle", "isCorrect": True},
                        {"text": "Salmonelle", "isCorrect": False},
                        {"text": "Escherichia coli", "isCorrect": False},
                        {"text": "Staphylocoque", "isCorrect": False}
                    ],
                    "correction": "La légionelle prolifère dans l'eau tiède et stagnante. Pour la tuer, il faut maintenir l'eau chaude à au moins 55°C (souvent 60°C) pour stopper son développement."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel type de radiateur est réputé pour sa très forte inertie thermique ?",
                    "answerOptions": [
                        {"text": "Fonte", "isCorrect": True},
                        {"text": "Acier", "isCorrect": False},
                        {"text": "Aluminium", "isCorrect": False},
                        {"text": "Convecteur électrique", "isCorrect": False}
                    ],
                    "correction": "La fonte est un matériau lourd qui met du temps à chauffer mais qui restitue la chaleur très longtemps après l'arrêt du chauffage (forte inertie)."
                },
                {
                    "questionNumber": 35,
                    "question": "À quoi sert le té de réglage situé en bas d'un radiateur ?",
                    "answerOptions": [
                        {"text": "Équilibrer les débits du réseau", "isCorrect": True},
                        {"text": "Vidanger le radiateur uniquement", "isCorrect": False},
                        {"text": "Purger l'air du radiateur", "isCorrect": False},
                        {"text": "Régler la température ambiante", "isCorrect": False}
                    ],
                    "correction": "Le té de réglage (ou coude de réglage) permet de limiter le débit de sortie du radiateur pour équilibrer l'installation hydraulique et assurer que tous les radiateurs chauffent uniformément."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle pièce de sécurité coupe l'arrivée de gaz si la flamme s'éteint sur une vieille chaudière ?",
                    "answerOptions": [
                        {"text": "Thermocouple", "isCorrect": True},
                        {"text": "Pressostat air", "isCorrect": False},
                        {"text": "Aquastat", "isCorrect": False},
                        {"text": "Manomètre", "isCorrect": False}
                    ],
                    "correction": "Le thermocouple génère un petit courant électrique sous l'effet de la chaleur de la flamme qui maintient la vanne gaz ouverte. Si la flamme s'éteint, le courant chute et le gaz est coupé."
                },
                {
                    "questionNumber": 37,
                    "question": "Dans un plancher chauffant hydraulique, quel type de tube utilise-t-on généralement ?",
                    "answerOptions": [
                        {"text": "PER avec Barrière Anti Oxygène", "isCorrect": True},
                        {"text": "Cuivre écroui rigide", "isCorrect": False},
                        {"text": "Acier noir fileté", "isCorrect": False},
                        {"text": "PVC pression collé", "isCorrect": False}
                    ],
                    "correction": "On utilise du tube synthétique (PER) doté d'une BAO (Barrière Anti-Oxygène) pour empêcher l'oxygène de pénétrer dans l'eau et limiter la formation de boues."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est l'avantage d'une production d'eau chaude par accumulation par rapport à l'instantanée ?",
                    "answerOptions": [
                        {"text": "Débit important disponible immédiatement", "isCorrect": True},
                        {"text": "Encombrement très réduit de l'appareil", "isCorrect": False},
                        {"text": "Eau chaude illimitée sans arrêt", "isCorrect": False},
                        {"text": "Pas de pertes thermiques statiques", "isCorrect": False}
                    ],
                    "correction": "L'accumulation (ballon) permet de stocker un grand volume d'eau chaude, offrant un débit de puisage élevé capable d'alimenter plusieurs douches simultanément, contrairement à l'instantané limité par sa puissance."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle sonde mesure la température extérieure pour anticiper les besoins de chauffe ?",
                    "answerOptions": [
                        {"text": "Sonde extérieure", "isCorrect": True},
                        {"text": "Thermostat d'ambiance", "isCorrect": False},
                        {"text": "Aquastat de chaudière", "isCorrect": False},
                        {"text": "Sonde de départ chauffage", "isCorrect": False}
                    ],
                    "correction": "La sonde extérieure informe la régulation des variations climatiques, permettant à la chaudière d'ajuster la température de l'eau (loi d'eau) avant même que le froid ne rentre dans la maison."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel fluide circule dans les capteurs d'un chauffe-eau solaire thermique ?",
                    "answerOptions": [
                        {"text": "Eau glycolée", "isCorrect": True},
                        {"text": "Eau de ville pure", "isCorrect": False},
                        {"text": "Fluide frigorigène", "isCorrect": False},
                        {"text": "Huile minérale", "isCorrect": False}
                    ],
                    "correction": "On utilise un mélange d'eau et de glycol (antigel) pour transporter la chaleur des capteurs vers le ballon, afin d'éviter que le fluide ne gèle dans les capteurs en hiver."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : HYDRAULIQUE ET ORGANES DE RÉGULATION/SÉCURITÉ (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : HYDRAULIQUE ET ORGANES DE RÉGULATION/SÉCURITÉ",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le rôle principal d'un circulateur dans une installation de chauffage central ?",
                    "answerOptions": [
                        {"text": "Assurer le mouvement de l'eau", "isCorrect": True},
                        {"text": "Augmenter la température de l'eau", "isCorrect": False},
                        {"text": "Filtrer les impuretés du circuit", "isCorrect": False},
                        {"text": "Maintenir la pression statique à l'arrêt", "isCorrect": False}
                    ],
                    "correction": "Le circulateur (ou pompe) sert à vaincre les pertes de charges pour faire circuler le fluide caloporteur des émetteurs vers la chaudière et inversement."
                },
                {
                    "questionNumber": 42,
                    "question": "À quelle pression est tarée la soupape de sécurité d'un circuit de chauffage domestique standard ?",
                    "answerOptions": [
                        {"text": "3 bars", "isCorrect": True},
                        {"text": "7 bars", "isCorrect": False},
                        {"text": "10 bars", "isCorrect": False},
                        {"text": "1 bar", "isCorrect": False}
                    ],
                    "correction": "Sur le circuit primaire chauffage, la soupape s'ouvre à 3 bars pour éviter la surpression. Sur le sanitaire (groupe de sécurité), elle est à 7 bars."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la fonction du vase d'expansion ?",
                    "answerOptions": [
                        {"text": "Absorber la dilatation de l'eau chauffée", "isCorrect": True},
                        {"text": "Purger l'air présent dans les tuyaux", "isCorrect": False},
                        {"text": "Ajouter de l'eau automatiquement", "isCorrect": False},
                        {"text": "Réchauffer l'eau du circuit retour", "isCorrect": False}
                    ],
                    "correction": "L'eau se dilate en chauffant. Le vase d'expansion, grâce à sa membrane et son gaz compressible (azote), absorbe ce surplus de volume pour maintenir une pression stable."
                },
                {
                    "questionNumber": 44,
                    "question": "Que mesure un manomètre ?",
                    "answerOptions": [
                        {"text": "La pression", "isCorrect": True},
                        {"text": "Le débit", "isCorrect": False},
                        {"text": "La température", "isCorrect": False},
                        {"text": "L'humidité", "isCorrect": False}
                    ],
                    "correction": "Le manomètre est l'instrument de mesure de la pression d'un fluide, généralement gradué en bars pour le chauffage."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel phénomène hydraulique provoque du bruit dans les canalisations ?",
                    "answerOptions": [
                        {"text": "Vitesse de circulation trop élevée", "isCorrect": True},
                        {"text": "Température de l'eau trop basse", "isCorrect": False},
                        {"text": "Pression statique trop faible", "isCorrect": False},
                        {"text": "Diamètre de tube trop important", "isCorrect": False}
                    ],
                    "correction": "Une vitesse d'eau excessive (généralement supérieure à 1 mètre par seconde en apparent) crée des sifflements et des turbulences bruyantes."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel dispositif est obligatoire pour remplir un circuit de chauffage afin de protéger le réseau d'eau potable ?",
                    "answerOptions": [
                        {"text": "Disconnecteur", "isCorrect": True},
                        {"text": "Clapet anti retour simple", "isCorrect": False},
                        {"text": "Vanne d'équilibrage", "isCorrect": False},
                        {"text": "Réducteur de pression", "isCorrect": False}
                    ],
                    "correction": "Le disconnecteur (type CA ou CB) empêche physiquement l'eau du chauffage (considérée comme polluée) de retourner dans le réseau d'eau potable en cas de dépression, ce qu'un simple clapet ne garantit pas totalement."
                },
                {
                    "questionNumber": 47,
                    "question": "Qu'appelle-t-on 'pertes de charge' dans un réseau hydraulique ?",
                    "answerOptions": [
                        {"text": "La chute de pression due aux frottements", "isCorrect": True},
                        {"text": "La fuite d'eau sur un raccord mal serré", "isCorrect": False},
                        {"text": "La baisse de température du fluide", "isCorrect": False},
                        {"text": "La diminution du volume d'eau dans le vase", "isCorrect": False}
                    ],
                    "correction": "Les pertes de charge correspondent à l'énergie perdue par le fluide lorsqu'il frotte contre les parois du tube ou traverse des accidents (coudes, tés, vannes)."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la couleur conventionnelle d'un vase d'expansion destiné au chauffage ?",
                    "answerOptions": [
                        {"text": "Rouge", "isCorrect": True},
                        {"text": "Blanc", "isCorrect": False},
                        {"text": "Bleu", "isCorrect": False},
                        {"text": "Gris", "isCorrect": False}
                    ],
                    "correction": "Les vases chauffage sont rouges (membrane résistante à l'eau morte). Les vases sanitaires sont blancs ou bleus (qualité alimentaire et résistance à l'eau renouvelée)."
                },
                {
                    "questionNumber": 49,
                    "question": "À quelle hauteur de colonne d'eau correspond une pression de 1 bar ?",
                    "answerOptions": [
                        {"text": "10 mètres", "isCorrect": True},
                        {"text": "100 mètres", "isCorrect": False},
                        {"text": "1 mètre", "isCorrect": False},
                        {"text": "50 mètres", "isCorrect": False}
                    ],
                    "correction": "1 bar équivaut approximativement à la pression exercée par une colonne d'eau de 10 mètres de hauteur (10 mCE)."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel composant permet de laisser passer le fluide dans un seul sens ?",
                    "answerOptions": [
                        {"text": "Clapet anti retour", "isCorrect": True},
                        {"text": "Vanne d'équilibrage", "isCorrect": False},
                        {"text": "Purgeur automatique", "isCorrect": False},
                        {"text": "Pot à boues", "isCorrect": False}
                    ],
                    "correction": "Le clapet anti-retour (ou soupape de retenue) s'ouvre sous la pression du fluide dans un sens et se bloque si le fluide tente de refluer."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le rôle d'une vanne 3 voies mélangeuse installée sur un départ chauffage ?",
                    "answerOptions": [
                        {"text": "Moduler la température de l'eau envoyée aux radiateurs", "isCorrect": True},
                        {"text": "Augmenter la pression de l'eau dans le circuit", "isCorrect": False},
                        {"text": "Séparer l'air de l'eau dans la chaudière", "isCorrect": False},
                        {"text": "Filtrer les particules métalliques en suspension", "isCorrect": False}
                    ],
                    "correction": "Elle mélange une partie de l'eau chaude venant de la chaudière avec de l'eau plus froide venant du retour radiateurs pour obtenir la température de départ exacte souhaitée."
                },
                {
                    "questionNumber": 52,
                    "question": "Où doit-on placer les purgeurs d'air automatiques ou manuels ?",
                    "answerOptions": [
                        {"text": "Aux points hauts de l'installation", "isCorrect": True},
                        {"text": "Aux points bas de l'installation", "isCorrect": False},
                        {"text": "Uniquement à la sortie de la chaudière", "isCorrect": False},
                        {"text": "Sur le tuyau de retour avant la pompe", "isCorrect": False}
                    ],
                    "correction": "L'air étant plus léger que l'eau, il s'accumule naturellement aux points hauts du réseau, où il doit être évacué par des purgeurs."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est l'unité standard utilisée pour exprimer un débit d'eau en chauffage ?",
                    "answerOptions": [
                        {"text": "Mètre cube par heure", "isCorrect": True},
                        {"text": "Pascal par seconde", "isCorrect": False},
                        {"text": "Watt par mètre carré", "isCorrect": False},
                        {"text": "Kilogramme par minute", "isCorrect": False}
                    ],
                    "correction": "Le débit volumique se mesure généralement en mètres cubes par heure (m³/h) ou en litres par minute (l/min) dans le bâtiment."
                },
                {
                    "questionNumber": 54,
                    "question": "Que se passe-t-il au niveau de la vitesse de l'eau si on réduit le diamètre du tube à débit constant ?",
                    "answerOptions": [
                        {"text": "La vitesse augmente", "isCorrect": True},
                        {"text": "La vitesse diminue", "isCorrect": False},
                        {"text": "La vitesse ne change pas", "isCorrect": False},
                        {"text": "La vitesse s'annule", "isCorrect": False}
                    ],
                    "correction": "Selon l'effet Venturi : si le tuyau rétrécit et que le débit reste le même, l'eau est obligée d'accélérer pour passer (Vitesse augmente, Pression diminue)."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le risque principal lié au phénomène de cavitation dans une pompe ?",
                    "answerOptions": [
                        {"text": "Détérioration de la roue et bruit anormal", "isCorrect": True},
                        {"text": "Augmentation brutale de la température de l'eau", "isCorrect": False},
                        {"text": "Blocage électrique du moteur du circulateur", "isCorrect": False},
                        {"text": "Formation de glace à l'intérieur du corps de pompe", "isCorrect": False}
                    ],
                    "correction": "La cavitation est la formation et l'implosion de bulles de vapeur dues à une dépression locale, ce qui érode le métal de la turbine et fait beaucoup de bruit."
                },
                {
                    "questionNumber": 56,
                    "question": "À quoi sert une vanne d'équilibrage sur une colonne montante ?",
                    "answerOptions": [
                        {"text": "Répartir les débits selon les besoins", "isCorrect": True},
                        {"text": "Purger l'air de la colonne", "isCorrect": False},
                        {"text": "Couper l'alimentation générale", "isCorrect": False},
                        {"text": "Filtrer les impuretés du réseau", "isCorrect": False}
                    ],
                    "correction": "Elle permet de créer une perte de charge artificielle pour régler le débit précis passant dans la colonne, afin que chaque partie du bâtiment soit chauffée uniformément."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle pièce sert à maintenir une pression différentielle constante ou à assurer un débit minimum dans la chaudière ?",
                    "answerOptions": [
                        {"text": "Soupape différentielle", "isCorrect": True},
                        {"text": "Vanne d'arrêt quart de tour", "isCorrect": False},
                        {"text": "Thermostat de sécurité", "isCorrect": False},
                        {"text": "Disconnecteur hydraulique", "isCorrect": False}
                    ],
                    "correction": "La soupape de décharge (ou by-pass) s'ouvre si tous les robinets thermostatiques se ferment, permettant à la pompe de continuer à circuler sans forcer."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment appelle-t-on le phénomène de circulation naturelle de l'eau chaude sans pompe, dû à la différence de densité ?",
                    "answerOptions": [
                        {"text": "Thermosiphon", "isCorrect": True},
                        {"text": "Thermoformage", "isCorrect": False},
                        {"text": "Thermorégulation", "isCorrect": False},
                        {"text": "Thermodynamique", "isCorrect": False}
                    ],
                    "correction": "L'eau chaude est moins dense que l'eau froide et a tendance à monter naturellement. C'est le principe du thermosiphon, utilisé dans les anciennes installations."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel élément protège l'installation contre les impuretés et les boues avant le retour chaudière ?",
                    "answerOptions": [
                        {"text": "Pot à boues", "isCorrect": True},
                        {"text": "Vase d'expansion", "isCorrect": False},
                        {"text": "Soupape de sécurité", "isCorrect": False},
                        {"text": "Purgeur automatique", "isCorrect": False}
                    ],
                    "correction": "Le pot à boues (ou désemboueur) piège les oxydes métalliques et les impuretés en suspension pour éviter qu'ils n'encrassent le corps de chauffe ou le circulateur."
                },
                {
                    "questionNumber": 60,
                    "question": "Si la pression du réseau chute régulièrement, quelle est la cause la plus probable ?",
                    "answerOptions": [
                        {"text": "Une fuite ou un vase d'expansion dégonflé", "isCorrect": True},
                        {"text": "Un circulateur bloqué ou grillé", "isCorrect": False},
                        {"text": "Une température de départ trop élevée", "isCorrect": False},
                        {"text": "Un robinet thermostatique bloqué en position fermée", "isCorrect": False}
                    ],
                    "correction": "Une baisse de pression indique une perte d'eau (fuite) ou une contraction de l'eau non compensée par le vase d'expansion (membrane percée ou manque d'azote)."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : COMMUNICATION TECHNIQUE ET LECTURE DE PLANS (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : COMMUNICATION TECHNIQUE ET LECTURE DE PLANS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle longueur réelle représente un trait de 10 centimètres sur un plan à l'échelle 1/50 ?",
                    "answerOptions": [
                        {"text": "5 mètres", "isCorrect": True},
                        {"text": "50 centimètres", "isCorrect": False},
                        {"text": "10 mètres", "isCorrect": False},
                        {"text": "1 mètre", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/50 signifie que 1 cm sur le papier vaut 50 cm en réalité. Donc 10 cm x 50 = 500 cm, soit 5 mètres."
                },
                {
                    "questionNumber": 62,
                    "question": "Que signifie l'abréviation 'ECS' sur un schéma de principe hydraulique ?",
                    "answerOptions": [
                        {"text": "Eau Chaude Sanitaire", "isCorrect": True},
                        {"text": "Eau Courante Standard", "isCorrect": False},
                        {"text": "Écoulement Canalisation Sortie", "isCorrect": False},
                        {"text": "Ensemble Chauffage Sol", "isCorrect": False}
                    ],
                    "correction": "L'ECS désigne le réseau d'eau potable qui a été chauffée (par un cumulus ou une chaudière) pour les besoins sanitaires (douche, lavabo)."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel type de trait est utilisé en dessin technique pour représenter une canalisation cachée ou encastrée ?",
                    "answerOptions": [
                        {"text": "Trait interrompu court", "isCorrect": True},
                        {"text": "Trait continu fort", "isCorrect": False},
                        {"text": "Trait mixte fin", "isCorrect": False},
                        {"text": "Trait ondulé", "isCorrect": False}
                    ],
                    "correction": "Les éléments invisibles (car derrière un mur, dans une dalle ou un coffrage) sont conventionnellement représentés en pointillés (trait interrompu)."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la définition exacte d'une 'vue en plan' ?",
                    "answerOptions": [
                        {"text": "Une vue de dessus horizontale coupée à un mètre du sol", "isCorrect": True},
                        {"text": "Une vue de face des façades extérieures du bâtiment", "isCorrect": False},
                        {"text": "Une vue verticale tranchant le bâtiment en deux", "isCorrect": False},
                        {"text": "Une vue en perspective artistique du projet fini", "isCorrect": False}
                    ],
                    "correction": "La vue en plan est une coupe horizontale virtuelle réalisée à 1 mètre de hauteur, permettant de visualiser l'agencement des pièces et l'épaisseur des murs."
                },
                {
                    "questionNumber": 65,
                    "question": "Que symbolise le signe 'Ø' placé devant un chiffre sur un plan de plomberie ?",
                    "answerOptions": [
                        {"text": "Diamètre", "isCorrect": True},
                        {"text": "Rayon", "isCorrect": False},
                        {"text": "Périmètre", "isCorrect": False},
                        {"text": "Volume", "isCorrect": False}
                    ],
                    "correction": "Ce symbole universel indique que la cote correspond au diamètre (extérieur ou nominal) du tube ou de l'accessoire circulaire."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel instrument de mesure moderne permet de tracer un trait de niveau sur tous les murs d'une pièce simultanément ?",
                    "answerOptions": [
                        {"text": "Niveau laser rotatif", "isCorrect": True},
                        {"text": "Mètre ruban souple", "isCorrect": False},
                        {"text": "Fil à plomb", "isCorrect": False},
                        {"text": "Règle en aluminium", "isCorrect": False}
                    ],
                    "correction": "Le niveau laser projette un faisceau lumineux horizontal à 360°, ce qui permet d'implanter les fixations à la même hauteur partout sans déplacer l'outil."
                },
                {
                    "questionNumber": 67,
                    "question": "En dessin isométrique de tuyauterie, quel est l'angle des axes fuyants par rapport à l'horizontale ?",
                    "answerOptions": [
                        {"text": "30 degrés", "isCorrect": True},
                        {"text": "45 degrés", "isCorrect": False},
                        {"text": "90 degrés", "isCorrect": False},
                        {"text": "10 degrés", "isCorrect": False}
                    ],
                    "correction": "L'isométrie, très utilisée en tuyauterie industrielle et plomberie pour visualiser les réseaux 3D, utilise des axes inclinés à 30° par rapport à l'horizontale."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle couleur est conventionnellement utilisée pour tracer les réseaux d'eau froide sur un plan ?",
                    "answerOptions": [
                        {"text": "Bleu", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False}
                    ],
                    "correction": "La convention internationale de repérage des fluides attribue la couleur bleue à l'eau froide et le rouge à l'eau chaude ou au chauffage départ."
                },
                {
                    "questionNumber": 69,
                    "question": "Que signifie le terme 'Allège' noté sous une fenêtre sur un plan d'architecte ?",
                    "answerOptions": [
                        {"text": "La hauteur du mur sous la fenêtre", "isCorrect": True},
                        {"text": "La largeur totale de la fenêtre", "isCorrect": False},
                        {"text": "L'épaisseur du vitrage isolant", "isCorrect": False},
                        {"text": "Le poids total de la maçonnerie", "isCorrect": False}
                    ],
                    "correction": "L'allège est la partie maçonnée située entre le sol fini et le rebord bas de la fenêtre. C'est une cote verticale importante pour placer les radiateurs."
                },
                {
                    "questionNumber": 70,
                    "question": "Qu'est-ce qu'une 'réservation' sur un plan de coffrage béton ?",
                    "answerOptions": [
                        {"text": "Un trou prévu pour le passage des tuyaux", "isCorrect": True},
                        {"text": "Une zone de stockage pour le plombier", "isCorrect": False},
                        {"text": "Une commande de matériel à l'avance", "isCorrect": False},
                        {"text": "Un local technique fermé à clé", "isCorrect": False}
                    ],
                    "correction": "Une réservation est une trémie ou un fourreau positionné avant le coulage du béton pour éviter d'avoir à percer la dalle ou le mur par la suite."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel symbole graphique représente généralement une vanne d'arrêt ou un robinet sur un schéma ?",
                    "answerOptions": [
                        {"text": "Deux triangles opposés par la pointe", "isCorrect": True},
                        {"text": "Un carré barré d'une croix", "isCorrect": False},
                        {"text": "Un cercle vide simple", "isCorrect": False},
                        {"text": "Une ligne en zigzag", "isCorrect": False}
                    ],
                    "correction": "Le symbole 'papillon' (deux triangles se touchant par la pointe) représente l'organe de coupure ou de réglage (vanne) sur la ligne de tuyauterie."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie l'indication 'NGF' associée à une cote d'altitude ?",
                    "answerOptions": [
                        {"text": "Nivellement Général de la France", "isCorrect": True},
                        {"text": "Norme Gaz de France", "isCorrect": False},
                        {"text": "Niveau Garanti Fini", "isCorrect": False},
                        {"text": "Nouvelle Garantie Fabricant", "isCorrect": False}
                    ],
                    "correction": "Le NGF est le système d'altitude de référence en France (le niveau 0 étant le niveau de la mer à Marseille). Il permet de caler les hauteurs absolues du bâtiment."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle échelle offre le plus de détails visuels pour dessiner une salle de bains ?",
                    "answerOptions": [
                        {"text": "1/20", "isCorrect": True},
                        {"text": "1/50", "isCorrect": False},
                        {"text": "1/100", "isCorrect": False},
                        {"text": "1/200", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/20 est plus 'grande' que 1/100. Elle permet de voir les détails des raccordements et l'emplacement précis des appareils sanitaires."
                },
                {
                    "questionNumber": 74,
                    "question": "Que désigne le terme 'calepinage' lors de la préparation du chantier ?",
                    "answerOptions": [
                        {"text": "Le dessin de disposition précise des éléments", "isCorrect": True},
                        {"text": "Le calcul du salaire des ouvriers", "isCorrect": False},
                        {"text": "La liste des outils manquants", "isCorrect": False},
                        {"text": "Le nettoyage final des sols", "isCorrect": False}
                    ],
                    "correction": "En plomberie (comme en carrelage), le calepinage consiste à dessiner l'implantation exacte des tuyaux et appareils pour optimiser les coupes et l'esthétique."
                },
                {
                    "questionNumber": 75,
                    "question": "Sur un plan, comment repère-t-on l'orientation géographique du bâtiment ?",
                    "answerOptions": [
                        {"text": "Par la flèche indiquant le Nord", "isCorrect": True},
                        {"text": "Par la position de la porte d'entrée", "isCorrect": False},
                        {"text": "Par la couleur des murs extérieurs", "isCorrect": False},
                        {"text": "Par l'échelle graphique en bas", "isCorrect": False}
                    ],
                    "correction": "La rose des vents ou une flèche marquée 'N' indique le Nord, ce qui est crucial pour positionner les capteurs solaires ou les sorties de toiture."
                },
                {
                    "questionNumber": 76,
                    "question": "Dans la désignation d'un tube cuivre '14x16', à quoi correspond le chiffre 16 ?",
                    "answerOptions": [
                        {"text": "Au diamètre extérieur en millimètres", "isCorrect": True},
                        {"text": "Au diamètre intérieur en millimètres", "isCorrect": False},
                        {"text": "À l'épaisseur du tube en dixièmes", "isCorrect": False},
                        {"text": "À la pression maximale admissible", "isCorrect": False}
                    ],
                    "correction": "Pour le cuivre courant, '14/16' (ou 16x1) désigne le diamètre extérieur de 16 mm et le diamètre intérieur de 14 mm (épaisseur de 1 mm)."
                },
                {
                    "questionNumber": 77,
                    "question": "Que représente un trait mixte fin (trait long, point, trait long) sur un dessin ?",
                    "answerOptions": [
                        {"text": "Un axe de symétrie ou de tube", "isCorrect": True},
                        {"text": "Une arête visible de l'objet", "isCorrect": False},
                        {"text": "Une hachure de coupe", "isCorrect": False},
                        {"text": "Une cotation de longueur", "isCorrect": False}
                    ],
                    "correction": "Le trait mixte fin matérialise les axes (axe de symétrie d'une pièce, axe central d'une canalisation) pour faciliter la lecture et le cotation."
                },
                {
                    "questionNumber": 78,
                    "question": "Qu'est-ce qu'un 'schéma unifilaire' ?",
                    "answerOptions": [
                        {"text": "Un dessin où le tuyau est représenté par un seul trait", "isCorrect": True},
                        {"text": "Un dessin où l'on voit l'épaisseur réelle du tuyau", "isCorrect": False},
                        {"text": "Un dessin en 3D avec ombrages et lumières réalistes", "isCorrect": False},
                        {"text": "Un dessin artistique fait à la main levée", "isCorrect": False}
                    ],
                    "correction": "Pour simplifier la représentation des réseaux, on dessine l'axe du tube par un trait unique (unifilaire) sur lequel on appose des symboles normalisés."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle information donne une 'coupe verticale' d'un bâtiment ?",
                    "answerOptions": [
                        {"text": "Les hauteurs sous plafond et épaisseurs de dalles", "isCorrect": True},
                        {"text": "La surface habitable en mètres carrés au sol", "isCorrect": False},
                        {"text": "L'orientation du soleil par rapport aux fenêtres", "isCorrect": False},
                        {"text": "Le plan de masse du terrain complet", "isCorrect": False}
                    ],
                    "correction": "La coupe verticale permet de voir ce qui se passe en hauteur : passage des colonnes montantes, réservations dans les planchers, hauteurs des attentes."
                },
                {
                    "questionNumber": 80,
                    "question": "Que signifie le sigle 'EU' sur un plan de réseau d'assainissement ?",
                    "answerOptions": [
                        {"text": "Eaux Usées", "isCorrect": True},
                        {"text": "Eaux Uniques", "isCorrect": False},
                        {"text": "Eaux Utiles", "isCorrect": False},
                        {"text": "États Unis", "isCorrect": False}
                    ],
                    "correction": "EU désigne les 'Eaux Usées' (ménagères : cuisine, salle de bain), à distinguer des EV (Eaux Vannes : WC) et EP (Eaux Pluviales)."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SANTÉ, SÉCURITÉ ET MAINTENANCE (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : SANTÉ, SÉCURITÉ ET MAINTENANCE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle habilitation électrique minimale doit posséder un plombier pour remplacer un chauffe-eau ou raccorder un circulateur (hors tension) ?",
                    "answerOptions": [
                        {"text": "BS", "isCorrect": True},
                        {"text": "B2V", "isCorrect": False},
                        {"text": "BR", "isCorrect": False},
                        {"text": "H0V", "isCorrect": False}
                    ],
                    "correction": "L'habilitation BS (Basse Tension - Chargé d'intervention élémentaire) est destinée aux non-électriciens (plombiers, peintres) devant effectuer des manœuvres simples de raccordement ou de remplacement à l'identique."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel dispositif de sécurité est obligatoire sur les tuyaux d'un poste à souder oxyacétylénique pour éviter l'explosion des bouteilles ?",
                    "answerOptions": [
                        {"text": "Clapet anti-retour pare-flamme", "isCorrect": True},
                        {"text": "Manodétendeur haute pression", "isCorrect": False},
                        {"text": "Économiseur de gaz automatique", "isCorrect": False},
                        {"text": "Filtre à charbon actif", "isCorrect": False}
                    ],
                    "correction": "Les clapets anti-retour pare-flamme (ARPF), placés près du chalumeau ou des détendeurs, empêchent la flamme de remonter dans les tuyaux jusqu'aux bouteilles en cas de retour de feu."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle maladie professionnelle grave est historiquement liée à l'inhalation de poussières lors de la dépose de vieilles calorifugeations ?",
                    "answerOptions": [
                        {"text": "Asbestose", "isCorrect": True},
                        {"text": "Saturnisme", "isCorrect": False},
                        {"text": "Légionellose", "isCorrect": False},
                        {"text": "Tétanos", "isCorrect": False}
                    ],
                    "correction": "L'asbestose (et les cancers associés) est causée par l'inhalation de fibres d'amiante, matériau souvent utilisé autrefois pour isoler (calorifuger) les tuyaux de chauffage."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la procédure sécurisée pour détecter une fuite de gaz sur une installation ?",
                    "answerOptions": [
                        {"text": "Utiliser un produit moussant détecteur", "isCorrect": True},
                        {"text": "Passer la flamme d'un briquet sur les raccords", "isCorrect": False},
                        {"text": "Écouter le bruit du gaz à l'oreille nue", "isCorrect": False},
                        {"text": "Sentir les odeurs en s'approchant très près", "isCorrect": False}
                    ],
                    "correction": "Il est strictement interdit d'utiliser une flamme. On utilise une bombe aérosol moussante (mille-bulles) qui forme des bulles à l'endroit précis de la fuite."
                },
                {
                    "questionNumber": 85,
                    "question": "Que doit faire le plombier s'il intervient sur une canalisation en plomb (intervention aujourd'hui rare mais possible en rénovation) ?",
                    "answerOptions": [
                        {"text": "Porter des gants et se laver soigneusement les mains", "isCorrect": True},
                        {"text": "Faire fondre le plomb sans ventilation pour aller vite", "isCorrect": False},
                        {"text": "Manger son sandwich sur le poste de travail", "isCorrect": False},
                        {"text": "Poncer le plomb à sec pour faire de la poussière", "isCorrect": False}
                    ],
                    "correction": "Le plomb est toxique par ingestion et inhalation (Saturnisme). L'hygiène des mains est primordiale avant de manger, et le port d'EPI est obligatoire."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel document écrit est obligatoire pour effectuer des travaux de soudure dans un établissement recevant du public ou une entreprise en activité ?",
                    "answerOptions": [
                        {"text": "Permis de feu", "isCorrect": True},
                        {"text": "Permis de construire", "isCorrect": False},
                        {"text": "Bon de commande", "isCorrect": False},
                        {"text": "Facture acquittée", "isCorrect": False}
                    ],
                    "correction": "Le 'Permis de feu' est un document de prévention qui analyse les risques d'incendie liés aux points chauds (soudure, meulage) et fixe les mesures de sécurité."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la première action à effectuer en cas de brûlure thermique superficielle sur la main ?",
                    "answerOptions": [
                        {"text": "Faire ruisseler de l'eau tempérée sur la zone", "isCorrect": True},
                        {"text": "Appliquer immédiatement de la glace pilée", "isCorrect": False},
                        {"text": "Percer les cloques avec une aiguille", "isCorrect": False},
                        {"text": "Mettre du beurre ou de l'huile grasse", "isCorrect": False}
                    ],
                    "correction": "La règle des '15-15-15' préconise de refroidir la brûlure à l'eau tempérée (15°C) pendant 15 minutes à 15 cm de distance pour stopper la propagation de la chaleur dans les tissus."
                },
                {
                    "questionNumber": 88,
                    "question": "Pourquoi réalise-t-on une 'liaison équipotentielle' en reliant les tuyaux métalliques à la terre ?",
                    "answerOptions": [
                        {"text": "Pour éviter l'électrisation par contact indirect", "isCorrect": True},
                        {"text": "Pour empêcher le calcaire de se déposer", "isCorrect": False},
                        {"text": "Pour améliorer le débit de l'eau potable", "isCorrect": False},
                        {"text": "Pour chauffer l'eau gratuitement par le sol", "isCorrect": False}
                    ],
                    "correction": "La liaison équipotentielle met toutes les masses métalliques (tuyaux cuivre, baignoire fonte) au même potentiel que la terre pour protéger les personnes si un fil électrique touche un tuyau."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle maintenance préventive simple permet d'éviter le blocage d'un groupe de sécurité calcaire ?",
                    "answerOptions": [
                        {"text": "Manœuvrer la soupape une fois par mois", "isCorrect": True},
                        {"text": "Démonter le groupe entièrement chaque semaine", "isCorrect": False},
                        {"text": "Verser de l'acide pur dans le siphon", "isCorrect": False},
                        {"text": "Graisser le mécanisme avec de l'huile moteur", "isCorrect": False}
                    ],
                    "correction": "Il est recommandé de tourner la molette de vidange du groupe de sécurité une fois par mois pour chasser les petits dépôts de tartre qui pourraient bloquer le clapet."
                },
                {
                    "questionNumber": 90,
                    "question": "Lors du débouchage chimique d'un évier avec un produit à base d'acide sulfurique, quel est le risque majeur ?",
                    "answerOptions": [
                        {"text": "Projection corrosive et réaction thermique violente", "isCorrect": True},
                        {"text": "Gel immédiat de la canalisation d'évacuation", "isCorrect": False},
                        {"text": "Coloration indélébile de la céramique en rose", "isCorrect": False},
                        {"text": "Émission d'un gaz hilarant inoffensif", "isCorrect": False}
                    ],
                    "correction": "Les déboucheurs acides sont très agressifs. Au contact de l'eau, ils provoquent une réaction exothermique (chaleur) et des projections qui peuvent gravement brûler la peau et les yeux."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel EPI est indispensable pour utiliser une meuleuse d'angle, en plus des gants ?",
                    "answerOptions": [
                        {"text": "Lunettes de protection", "isCorrect": True},
                        {"text": "Chaussures de ville", "isCorrect": False},
                        {"text": "Casquette en tissu", "isCorrect": False},
                        {"text": "Écharpe en laine", "isCorrect": False}
                    ],
                    "correction": "Les projections de limaille de fer ou d'éclats de disque sont fréquentes et très rapides. Les lunettes (ou visière) sont obligatoires pour éviter la cécité."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle est la cause la plus fréquente d'une mauvaise odeur provenant d'un siphon de sol peu utilisé ?",
                    "answerOptions": [
                        {"text": "L'évaporation de la garde d'eau", "isCorrect": True},
                        {"text": "La présence de rats dans le tuyau", "isCorrect": False},
                        {"text": "La décomposition du plastique", "isCorrect": False},
                        {"text": "La surpression du réseau public", "isCorrect": False}
                    ],
                    "correction": "Si un appareil n'est pas utilisé (chaufferie, buanderie), l'eau du siphon s'évapore. Le bouchon hydraulique disparaît et laisse passer l'air vicié des égouts."
                },
                {
                    "questionNumber": 93,
                    "question": "Sur un échafaudage roulant, que doit-on impérativement faire avant de monter dessus ?",
                    "answerOptions": [
                        {"text": "Bloquer les roues et mettre les stabilisateurs", "isCorrect": True},
                        {"text": "Demander à un collègue de tenir l'échelle", "isCorrect": False},
                        {"text": "Vérifier la pression des pneus à la main", "isCorrect": False},
                        {"text": "Graisser les montants verticaux", "isCorrect": False}
                    ],
                    "correction": "La stabilité est primordiale. Il faut bloquer les freins des roues et déployer les stabilisateurs latéraux pour éviter le basculement."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel type de raccord est interdit pour le gaz à l'intérieur des habitations (sauf exception très encadrée) ?",
                    "answerOptions": [
                        {"text": "Raccord à olive", "isCorrect": True},
                        {"text": "Raccord à braser", "isCorrect": False},
                        {"text": "Raccord à sertir gaz", "isCorrect": False},
                        {"text": "Raccord vissé conique", "isCorrect": False}
                    ],
                    "correction": "Les raccords mécaniques type 'bicône' ou 'olive' sont généralement interdits pour le gaz en intérieur car le risque de fuite par déserrage ou vibration est jugé trop important (se référer au référentiel gaz en vigueur)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la posture correcte pour utiliser une clé à molette afin d'éviter de se blesser en cas de ripage ?",
                    "answerOptions": [
                        {"text": "Tirer la clé vers soi", "isCorrect": True},
                        {"text": "Pousser la clé avec la paume", "isCorrect": False},
                        {"text": "Frapper sur la clé avec un marteau", "isCorrect": False},
                        {"text": "Utiliser un tube de rallonge", "isCorrect": False}
                    ],
                    "correction": "Il faut toujours 'tirer' la clé vers soi. Si on 'pousse' et que la clé ripe (glisse), la main part violemment vers l'avant et risque de heurter un obstacle blessant."
                },
                {
                    "questionNumber": 96,
                    "question": "Que doit-on vérifier avant de percer un mur dans une salle de bains rénovée ?",
                    "answerOptions": [
                        {"text": "L'absence de canalisations encastrées", "isCorrect": True},
                        {"text": "La marque de la peinture murale", "isCorrect": False},
                        {"text": "La température de la pièce", "isCorrect": False},
                        {"text": "L'épaisseur exacte de la faïence", "isCorrect": False}
                    ],
                    "correction": "Il faut utiliser un détecteur de métaux/matériaux pour éviter de percer une conduite d'eau ou une gaine électrique invisible noyée dans le mur."
                },
                {
                    "questionNumber": 97,
                    "question": "À quoi sert le 'thermocouple' sur un vieil appareil à gaz ?",
                    "answerOptions": [
                        {"text": "Couper le gaz si la veilleuse s'éteint", "isCorrect": True},
                        {"text": "Allumer le gaz automatiquement à distance", "isCorrect": False},
                        {"text": "Mesurer la consommation de gaz", "isCorrect": False},
                        {"text": "Filtrer les impuretés du gaz", "isCorrect": False}
                    ],
                    "correction": "Le thermocouple est une sécurité par flamme. Si la veilleuse s'éteint (courant d'air), le thermocouple refroidit et coupe l'arrivée de gaz pour éviter l'accumulation explosive."
                },
                {
                    "questionNumber": 98,
                    "question": "Comment doit-on stocker les bouteilles de gaz (oxygène/acétylène) dans le véhicule ou l'atelier ?",
                    "answerOptions": [
                        {"text": "Verticalement et arrimées solidement", "isCorrect": True},
                        {"text": "Couchées à plat sur le sol", "isCorrect": False},
                        {"text": "La tête en bas pour la pression", "isCorrect": False},
                        {"text": "En vrac les unes sur les autres", "isCorrect": False}
                    ],
                    "correction": "Les bouteilles doivent être stockées debout (verticalement) et attachées pour éviter qu'elles ne tombent et n'endommagent leurs robinets ('risque bouteille fusée')."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le symbole de danger représenté par un losange rouge contenant une flamme noire ?",
                    "answerOptions": [
                        {"text": "Inflammable", "isCorrect": True},
                        {"text": "Toxique", "isCorrect": False},
                        {"text": "Corrosif", "isCorrect": False},
                        {"text": "Explosif", "isCorrect": False}
                    ],
                    "correction": "Ce pictogramme (SGH02) indique que le produit (colle, solvant, gaz) peut s'enflammer facilement au contact d'une étincelle ou de la chaleur."
                },
                {
                    "questionNumber": 100,
                    "question": "En cas d'accident électrique (personne collée au fil), que faire en priorité absolue ?",
                    "answerOptions": [
                        {"text": "Couper le courant au disjoncteur", "isCorrect": True},
                        {"text": "Toucher la personne pour la rassurer", "isCorrect": False},
                        {"text": "Tirer la personne par les vêtements", "isCorrect": False},
                        {"text": "Appeler les pompiers avant tout", "isCorrect": False}
                    ],
                    "correction": "Il ne faut surtout pas toucher la victime tant qu'elle est sous tension (risque de sur-accident). La priorité est de couper l'énergie (disjoncteur ou arrêt d'urgence)."
                }
            ]
        }
    }
}