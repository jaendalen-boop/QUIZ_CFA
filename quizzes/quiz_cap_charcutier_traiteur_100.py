quiz_data = {
    "title": "CAP Charcutier Traiteur - Base de Données Complète (100 Questions) - Corrigée V1",
    
    "description": "Base de données de 100 questions pour le CAP Charcutier Traiteur. Les longueurs des réponses ont été uniformisées pour éviter tout biais lors d'un test.",
    
    "themes": {
        # THÈME 1
        1: {
            "name": "Hygiène, Sécurité, Environnement (HSE) et Traçabilité (HACCP)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) essentiel lors du désossage ou du parage des viandes ?",
                    "answerOptions": [
                        {"text": "Le masque respiratoire de type FFP2 (ou FFP3) pour les poussières fines de farine en suspension dans l'air.", "isCorrect": False, "key": "A"},
                        {"text": "Le tablier de cuisine en coton (ou en lin) et les gants isolants pour le travail à haute température (four).", "isCorrect": False, "key": "B"},
                        {"text": "Le gant cotte de mailles (ou anti-coupure) et le tablier étanche pour prévenir les coupures graves et les projections.", "isCorrect": True, "key": "C"},
                        {"text": "Le casque anti-bruit pour les zones de tranchage intensif (trancheuse électrique) et de boyautage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le gant de mailles est indispensable pour la sécurité lors de la manipulation des couteaux et des pièces de viande (désossage)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la 'zone de danger' (ou 'Temperature Danger Zone - TDZ') où la prolifération des bactéries est maximale ?",
                    "answerOptions": [
                        {"text": "La zone des températures positives : entre +15°C et +20°C (température ambiante) pour le pointage des pâtes.", "isCorrect": False, "key": "A"},
                        {"text": "La zone comprise entre +8°C et +63°C, qui favorise la multiplication rapide des micro-organismes (toxines).", "isCorrect": True, "key": "B"},
                        {"text": "La zone des très hautes températures (supérieure à +100°C), pour la stérilisation (appertisation).", "isCorrect": False, "key": "C"},
                        {"text": "La zone des températures négatives : entre -5°C et -18°C (congélation) pour la conservation longue durée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les aliments doivent être maintenus à une température inférieure à 8°C (réfrigération) ou supérieure à 63°C (maintien au chaud)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le risque lié à la présence de verre ou de corps étranger (plastique dur) dans une préparation (pâté, terrine) ?",
                    "answerOptions": [
                        {"text": "Le risque d'allergie respiratoire (asthme du charcutier) ou d'explosion (ATEX) en cas de forte concentration.", "isCorrect": False, "key": "A"},
                        {"text": "La corrosion accélérée des pièces métalliques du hachoir et du poussoir (acidité).", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de blessure grave (coupure ou hémorragie interne) pour le consommateur final (contamination physique).", "isCorrect": True, "key": "C"},
                        {"text": "L'augmentation rapide de la viscosité de la pâte lors de l'incorporation de la lécithine (émulsifiant).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Toute contamination physique doit faire l'objet d'une procédure d'isolement (alerte immédiate) et d'une enquête (traçabilité)."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la principale mesure de sécurité à prendre lors de l'utilisation d'un cutter (hachoir-mélangeur) ou d'une trancheuse électrique ?",
                    "answerOptions": [
                        {"text": "Travailler seul et sans supervision pour optimiser la cadence de production journalière.", "isCorrect": False, "key": "A"},
                        {"text": "S'assurer que les protections (carters, grilles, poussoir) sont en place et que l'appareil est débranché avant le nettoyage.", "isCorrect": True, "key": "B"},
                        {"text": "Mettre le pétrin en marche pendant le nettoyage des ustensiles pour un gain de temps (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le port du masque de soudage (protection UV) et de vêtements anti-feu (gants).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les machines coupantes ou tournantes (lames) sont les principales sources d'accidents graves (amputation). La consignation est obligatoire."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le danger lié à la manipulation des nitrites (sel nitrité) ou des additifs chimiques (conservateurs) ?",
                    "answerOptions": [
                        {"text": "L'inactivation de la levure par contact direct avec le sel et l'absence de pousse de la pâte.", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de brûlure chimique sur la peau et le danger de dépassement du dosage (toxicité pour le consommateur).", "isCorrect": True, "key": "B"},
                        {"text": "La corrosion accélérée des pièces métalliques du pétrin et du fournil.", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation excessive du temps de pétrissage (pointage) de la pâte finale.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les nitrites sont dosés très précisément pour leur rôle anti-bactérien (Clostridium Botulinum) mais sont toxiques en cas de surdosage."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la procédure correcte pour la gestion des Huiles Alimentaires Usagées (HAU) après une friture ?",
                    "answerOptions": [
                        {"text": "Les jeter directement dans les poubelles (ordures ménagères) sans possibilité de réutilisation.", "isCorrect": False, "key": "A"},
                        {"text": "Les stocker séparément, identifier la nature du déchet et les confier à des entreprises spécialisées (collecte et recyclage).", "isCorrect": True, "key": "B"},
                        {"text": "Les recongeler pour une revente ultérieure à un prix réduit dans les prochaines 48 heures.", "isCorrect": False, "key": "C"},
                        {"text": "Les réintroduire (une partie) dans la prochaine fournée de pâte fraîche (réutilisation immédiate).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les HAU sont un déchet polluant. Leur recyclage (biocarburant) est soumis à une réglementation environnementale stricte."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est la signification de la 'DLUO' (Date Limite d'Utilisation Optimale) sur un ingrédient non périssable (épices séchées) ?",
                    "answerOptions": [
                        {"text": "Elle indique la date après laquelle l'ingrédient ne peut plus être consommé (danger bactériologique).", "isCorrect": False, "key": "A"},
                        {"text": "Elle indique la date après laquelle les qualités organoleptiques (goût, arôme, texture) ne sont plus garanties (sans risque sanitaire).", "isCorrect": True, "key": "B"},
                        {"text": "Elle indique la température maximale de conservation pour l'ingrédient (+4°C).", "isCorrect": False, "key": "C"},
                        {"text": "Elle indique la zone de danger bactériologique (entre +8°C et +63°C).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La DLUO (remplacée par le DDM : Date de Durabilité Minimale) n'est pas une date limite de consommation (DLC) sanitaire."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la principale mesure d'hygiène à prendre lors du nettoyage des ustensiles (hachoir, cutter, poussoir) pour éviter la contamination croisée ?",
                    "answerOptions": [
                        {"text": "Utiliser uniquement de l'eau froide (moins de 10°C) pour lubrifier les lames et les pièces de coupe (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le nettoyage (eau/détergent) suivi impérativement de la désinfection (produit biocide) puis du rinçage/séchage.", "isCorrect": True, "key": "B"},
                        {"text": "Laisser les outils dans l'eau savonneuse toute la nuit (développement bactérien).", "isCorrect": False, "key": "C"},
                        {"text": "Le masque de type FFP3 pour filtrer les fines particules de farine en suspension dans l'air.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le protocole 'Nettoyage-Désinfection' est la base de l'HACCP pour éliminer les résidus et les micro-organismes (bactéries)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le risque de remettre une préparation chaude directement au réfrigérateur (grand volume) sans refroidissement rapide ?",
                    "answerOptions": [
                        {"text": "Le risque de 'remontée en température' des autres aliments stockés (rupture de la chaîne du froid) et de prolifération bactérienne.", "isCorrect": True, "key": "A"},
                        {"text": "L'augmentation excessive du taux d'humidité de la pâte en cours de préparation.", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de prolifération d'organismes thermophiles sur le pain cuit.", "isCorrect": False, "key": "C"},
                        {"text": "La corrosion accélérée des pièces métalliques du pétrin et du fournil.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le refroidissement doit être rapide (de +63°C à +10°C en moins de deux heures) à l'aide d'une cellule de refroidissement (blast chiller)."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est l'importance du 'sens de la marche' (flux en avant) dans l'organisation du laboratoire (HACCP) ?",
                    "answerOptions": [
                        {"text": "Garantir l'image de marque de la boutique, sans aucun lien avec l'hygiène alimentaire (HACCP).", "isCorrect": False, "key": "A"},
                        {"text": "Éviter la contamination croisée en séparant les zones 'sales' (matières premières) des zones 'propres' (produit fini).", "isCorrect": True, "key": "B"},
                        {"text": "Assurer uniquement la protection contre les brûlures des mains et des avant-bras de l'opérateur.", "isCorrect": False, "key": "C"},
                        {"text": "Permettre au boulanger de travailler sans être soumis aux variations de température du fournil.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le produit doit toujours avancer dans le processus, sans jamais croiser les flux de déchets ou de matières premières non travaillées."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la température maximale de conservation des produits 'Très Périssables' (viandes fraîches, farces, pâtes crues) ?",
                    "answerOptions": [
                        {"text": "La zone des températures positives : entre +15°C et +20°C (température ambiante).", "isCorrect": False, "key": "A"},
                        {"text": "Une température de conservation de +4°C maximum (réglementation européenne).", "isCorrect": True, "key": "B"},
                        {"text": "La zone des très hautes températures (supérieure à +100°C), pour la stérilisation.", "isCorrect": False, "key": "C"},
                        {"text": "Une température de conservation de 0°C (ou -1°C) maximum pour la viande fraîche (DLC très courte).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les farces et les produits de charcuterie sont souvent conservés à 4°C maximum (DLC courte), tandis que la viande fraîche (non transformée) est à 0°C ou 2°C max."
                },
                {
                    "questionNumber": 12,
                    "question": "Que doit-on faire obligatoirement avant d'entamer une opération de désossage (parage) sur une pièce de viande (gigot, épaule) ?",
                    "answerOptions": [
                        {"text": "Vérifier la température du four pour s'assurer que les produits seront enfournés à chaud.", "isCorrect": False, "key": "A"},
                        {"text": "Se laver et se désinfecter les mains de manière rigoureuse (procédure de lavage) et enfiler les EPI.", "isCorrect": True, "key": "B"},
                        {"text": "Protéger les vitres, les pièces en plastique/caoutchouc et les réservoirs d'essence à proximité des étincelles.", "isCorrect": False, "key": "C"},
                        {"text": "S'assurer que l'eau utilisée pour le pétrissage est à une température maximale de 10°C.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le lavage des mains (avant/après) est le Point Critique pour la Maîtrise (CCP) de l'hygiène personnelle."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est le risque si l'on ne nettoie pas correctement le hachoir ou le poussoir entre deux fabrications (farce différente) ?",
                    "answerOptions": [
                        {"text": "Le risque de contamination croisée entre un allergène (fruits à coque) et une autre préparation (risque client).", "isCorrect": True, "key": "A"},
                        {"text": "La diminution du temps de pétrissage pour la deuxième pâte (gain de temps).", "isCorrect": False, "key": "B"},
                        {"text": "La contamination des fonds de peinture ou de la cabine, entraînant des défauts (poussières, cratères).", "isCorrect": False, "key": "C"},
                        {"text": "L'altération des propriétés de la levure par contact avec l'eau froide.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gestion des allergènes (gluten, œufs, lait, fruits à coque) est obligatoire (étiquetage) et passe par un nettoyage strict."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le risque de laisser des aliments (viande) sur un plan de travail à température ambiante pendant plus de deux heures ?",
                    "answerOptions": [
                        {"text": "Le risque de 'brûlure' des micro-organismes (levures et bactéries) et de bloquer l'activité du levain.", "isCorrect": False, "key": "A"},
                        {"text": "Le risque d'intoxication alimentaire (Salmonella, Listeria) due à la multiplication rapide des bactéries dans la 'zone de danger'.", "isCorrect": True, "key": "B"},
                        {"text": "La diminution du temps de pétrissage pour la deuxième pâte (gain de temps).", "isCorrect": False, "key": "C"},
                        {"text": "La zone des températures ambiantes (entre +15°C et +20°C) pour le stockage des œufs frais.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le temps d'exposition à température ambiante doit être minimisé (moins de 2 heures) pour le travail des farces et des viandes."
                },
                {
                    "questionNumber": 15,
                    "question": "Que doit-on faire si l'on trouve de la moisissure sur une matière première (pâte d'épice, fromage) ?",
                    "answerOptions": [
                        {"text": "Les isoler, stopper la production concernée, signaler l'incident et rechercher la source de la contamination.", "isCorrect": True, "key": "A"},
                        {"text": "Continuer la production en retirant uniquement la zone visiblement contaminée (risque sanitaire).", "isCorrect": False, "key": "B"},
                        {"text": "Ajouter un additif (émulsifiant) dans la pâte pour neutraliser le corps étranger (sans effet).", "isCorrect": False, "key": "C"},
                        {"text": "Les laisser pour la fin de la production, car le four brûlera tous les corps étrangers (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La moisissure peut produire des mycotoxines (toxiques). Le produit doit être jeté. Une enquête de traçabilité est lancée (DLC, fournisseur)."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le risque pour l'opérateur en cas de manipulation de poids lourds (caisse de viande, sacs de sel) sans matériel adapté ?",
                    "answerOptions": [
                        {"text": "Le risque de Troubles Musculo-Squelettiques (TMS), notamment le mal de dos (lumbago, hernie) ou les douleurs articulaires.", "isCorrect": True, "key": "A"},
                        {"text": "Le risque d'intoxication aux poussières de farine dues à une rupture du sac lors du transport.", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de brûlure chimique sur la peau lors de l'incorporation de la farine dans le pétrin.", "isCorrect": False, "key": "C"},
                        {"text": "Le risque d'explosion (ATEX) en cas de choc du sac sur le sol du laboratoire.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le port de charges lourdes doit être sécurisé (chariot, transpalette, dos droit) pour prévenir les maladies professionnelles (TMS)."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le rôle du 'Plan de Maîtrise Sanitaire' (PMS) dans le laboratoire de charcuterie ?",
                    "answerOptions": [
                        {"text": "Mesurer la teneur en gluten (W) de la farine utilisée pour le pétrissage.", "isCorrect": False, "key": "A"},
                        {"text": "Décrire les mesures prises pour assurer l'hygiène et la sécurité des denrées (traçabilité, CCP, procédures de nettoyage).", "isCorrect": True, "key": "B"},
                        {"text": "Contrôler la température interne du four pendant le défournement des baguettes.", "isCorrect": False, "key": "C"},
                        {"text": "Évaluer le pH (acidité) de la pâte avant la fermentation finale (apprêt).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le PMS (basé sur l'HACCP) est un document obligatoire qui rassemble toutes les procédures de l'entreprise (hygiène, contrôles, traçabilité)."
                },
                {
                    "questionNumber": 18,
                    "question": "Que doit-on faire si l'on constate une infestation de nuisibles (rongeurs, insectes) dans la zone de stockage des ingrédients ?",
                    "answerOptions": [
                        {"text": "Couper immédiatement la batterie (alimentation électrique), déplacer le véhicule à l'extérieur et alerter les secours si nécessaire.", "isCorrect": False, "key": "A"},
                        {"text": "Contacter immédiatement une entreprise de lutte antiparasitaire et jeter toutes les marchandises contaminées (risque sanitaire).", "isCorrect": True, "key": "B"},
                        {"text": "Augmenter la température du fournil pour chasser les nuisibles par la chaleur excessive.", "isCorrect": False, "key": "C"},
                        {"text": "Ajouter plus de sel dans la pâte pour désinfecter la farine contaminée par les excréments.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les nuisibles sont des vecteurs de maladies (Salmonella). Les produits contaminés doivent être détruits. La dératisation est vitale."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est la conséquence d'un non-respect de la température de cuisson à cœur pour une terrine (température insuffisante) ?",
                    "answerOptions": [
                        {"text": "Un risque de mie collante, moins digeste, et une conservation réduite (humidité résiduelle trop importante).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de 'survie bactérienne' (Clostridium) et de risque d'intoxication alimentaire (danger mortel potentiel).", "isCorrect": True, "key": "B"},
                        {"text": "L'obtention d'un pain avec une saveur très acide, caractéristique du pain au levain.", "isCorrect": False, "key": "C"},
                        {"text": "La déformation du pain lors du défournement (affaissement) et l'absence d'alvéolage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La cuisson à cœur doit atteindre 65°C à 72°C (selon le produit) pour garantir la destruction des pathogènes (sonde de température)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le rôle de la 'fiche de traçabilité' (étiquette) pour un jambon cuit ou une salaison ?",
                    "answerOptions": [
                        {"text": "Assurer la sécurité du véhicule pour l'utilisateur et la conformité avec la réglementation routière (législation).", "isCorrect": False, "key": "A"},
                        {"text": "Permettre d'identifier l'origine des matières, la date de fabrication, le numéro de lot et la DLC (en cas de rappel produit).", "isCorrect": True, "key": "B"},
                        {"text": "Ajouter un additif (émulsifiant) dans la pâte pour neutraliser le corps étranger (sans effet).", "isCorrect": False, "key": "C"},
                        {"text": "Les laisser pour la fin de la production, car le four brûlera tous les corps étrangers (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La traçabilité est la capacité de retrouver l'historique d'un produit (du champ à l'assiette) et elle est obligatoire."
                }
            ]
        },
        # THÈME 2
        2: {
            "name": "Transformation des Viandes et Pâtés/Terrines",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le rôle de la 'coupe au cutter' (hachage ultra-fin) dans la fabrication des mousses et des saucissons de Paris ?",
                    "answerOptions": [
                        {"text": "La jauge de profondeur pour les pneus ou le vernier pour les petites pièces.", "isCorrect": False, "key": "A"},
                        {"text": "Elle permet l'émulsion (mélange stable) de la viande, de la glace (ou eau) et du gras (création d'une texture très fine et homogène).", "isCorrect": True, "key": "B"},
                        {"text": "Le régulateur de pression pour le pistolet de peinture (température et pH).", "isCorrect": False, "key": "C"},
                        {"text": "Le pistolet à air chaud pour le séchage des mastics et des apprêts.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le cutter (sous vide et à basse température) permet d'obtenir une farce très fine, onctueuse et bien liée (par l'émulsion du gras et de l'eau)."
                },
                {
                    "questionNumber": 22,
                    "question": "Que signifie le terme 'dénervation' (ou 'parage') d'une pièce de viande (longe, épaule) ?",
                    "answerOptions": [
                        {"text": "Il indique la force de la farine (W) : plus le T est élevé, plus la farine est forte et stable.", "isCorrect": False, "key": "A"},
                        {"text": "C'est l'action de retirer les nerfs, les aponévroses (tissus conjonctifs), le cartilage et les parties non nobles (graisse excessive) de la viande.", "isCorrect": True, "key": "B"},
                        {"text": "Il indique le pouvoir d'hydratation maximal de la farine (la quantité d'eau absorbée).", "isCorrect": False, "key": "C"},
                        {"text": "Il indique la présence ou l'absence d'additifs (améliorants, enzymes) dans la farine de base.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le parage est essentiel pour la qualité de la farce (texture, goût, et absence de parties dures ou nerveuses)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le rôle de la 'panne' (graisse de porc dure et blanche) dans la farce à pâté ou à saucisse ?",
                    "answerOptions": [
                        {"text": "Il active la levure et accélère la fermentation (pousse) de la pâte fraîche.", "isCorrect": False, "key": "A"},
                        {"text": "Elle apporte le moelleux, la saveur, l'onctuosité et sert d'agent de liaison après la cuisson (texture).", "isCorrect": True, "key": "B"},
                        {"text": "Il sert d'agent de blanchiment de la mie du pain (aspect très blanc).", "isCorrect": False, "key": "C"},
                        {"text": "Il sert uniquement à colorer la croûte du pain lors de la cuisson finale.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La panne (graisse dorsale) est la graisse la plus noble. Elle est utilisée pour sa tenue à la chaleur et sa saveur neutre (hachage idéal)."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la principale différence entre une 'terrine' et un 'pâté en croûte' (aspect visuel) ?",
                    "answerOptions": [
                        {"text": "La terrine est cuite dans un moule (faïence, céramique) et n'a pas de pâte (croûte) ; le pâté est entouré d'une pâte et est démoulé.", "isCorrect": True, "key": "A"},
                        {"text": "La levure ne permet pas de faire lever la pâte ; seul le levain permet la production de gaz carbonique (CO₂).", "isCorrect": False, "key": "B"},
                        {"text": "Le levain est une poudre sèche déshydratée ; la levure est une pâte fraîche (en cube) ou liquide.", "isCorrect": False, "key": "C"},
                        {"text": "La levure apporte l'acidité et les arômes ; le levain sert uniquement à la pousse du pain.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La terrine est généralement servie directement dans son plat de cuisson. Le pâté en croûte nécessite une pâte (souvent à foncer) pour sa tenue."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le rôle des 'couennes' de porc (peau) dans la fabrication d'une tête roulée (fromage de tête) ?",
                    "answerOptions": [
                        {"text": "La tôle sera plus collante, difficile à travailler, mais le pain sera plus léger et alvéolé (mie plus ouverte).", "isCorrect": False, "key": "A"},
                        {"text": "Elles sont cuites longuement pour produire de la gélatine naturelle (collagène) qui lie la préparation et lui donne sa tenue ferme.", "isCorrect": True, "key": "B"},
                        {"text": "La fermentation sera bloquée par la forte concentration en sel et en levure (osmose).", "isCorrect": False, "key": "C"},
                        {"text": "La mie du pain sera jaune intense et la croûte sera très peu colorée (blanche).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le collagène des couennes (ou des pieds) est le liant naturel utilisé dans de nombreuses préparations (aspic, jambon persillé, tête roulée)."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est l'impact de la 'glace' (eau congelée) dans la préparation d'une farce fine au cutter ?",
                    "answerOptions": [
                        {"text": "Elle permet de réguler la température de la pâte en fin de pétrissage (température de base ou de masse idéale : 24°C).", "isCorrect": False, "key": "A"},
                        {"text": "Elle permet de maintenir la température de la farce au plus bas (moins de 12°C) pendant le cutterage pour éviter que le gras ne fonde.", "isCorrect": True, "key": "B"},
                        {"text": "Elle sert uniquement à nettoyer le pétrin et les outils après le pointage final.", "isCorrect": False, "key": "C"},
                        {"text": "Elle influence directement le goût (acidité) et la couleur de la croûte du pain après la cuisson.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le cutterage rapide (friction) produit de la chaleur. La glace est essentielle pour l'émulsion et la qualité de la farce."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le nom de l'opération qui consiste à insérer de petits morceaux de gras (ou de fruits) dans le corps d'une farce pour la décorer ou l'aromatiser ?",
                    "answerOptions": [
                        {"text": "Le lardonage ou le piquetage (insertion à l'aide d'une lardoire) pour la décoration (ex : terrine de chevreuil).", "isCorrect": True, "key": "A"},
                        {"text": "Le taux d'humidité (H) de la farine mesuré au dessiccateur.", "isCorrect": False, "key": "B"},
                        {"text": "Le taux de cendres (T) de la farine mesuré après incinération.", "isCorrect": False, "key": "C"},
                        {"text": "Le pH (potentiel Hydrogène) de la farine qui mesure son acidité de base.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le lardonage est une technique de décoration et d'apport de moelleux (gras) dans les farces maigres (gibier, volaille)."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le rôle du 'sel' (NaCl) dans la fabrication de la charcuterie (hors salaison) ?",
                    "answerOptions": [
                        {"text": "Elles produisent de l'acide lactique et de l'acide acétique, donnant l'acidité et les arômes caractéristiques.", "isCorrect": False, "key": "A"},
                        {"text": "Il est indispensable pour le goût (exhausteur), la conservation (anti-bactérien) et le liant de la farce (extraction des protéines).", "isCorrect": True, "key": "B"},
                        {"text": "Elles servent uniquement à renforcer le réseau de gluten (ténacité) lors du pétrissage intensif.", "isCorrect": False, "key": "C"},
                        {"text": "Elles régulent le brunissement de la croûte et la coloration de la mie du pain.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le sel (salage) est le premier conservateur. Il permet aussi l'extraction de la myosine (protéine) qui lie les farces cuites."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est l'effet de l'utilisation d'une 'force de hachage' (ou d'un disque de hachoir) trop fin sur la farce à saucisse ?",
                    "answerOptions": [
                        {"text": "Elle assouplit la pâte, augmente le volume du produit et améliore la saveur et la conservation.", "isCorrect": False, "key": "A"},
                        {"text": "Le hachage trop fin écrase la viande (échauffement) et donne une texture pâteuse (absence de grain) au produit fini.", "isCorrect": True, "key": "B"},
                        {"text": "Elle rend la pâte trop ferme (ténace) et difficile à travailler au laminoir (tourage).", "isCorrect": False, "key": "C"},
                        {"text": "Elle sert uniquement à colorer la mie du produit (jaune intense) sans changer la texture.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le choix du disque (3mm, 6mm, 8mm) est crucial pour la texture (grain) du saucisson ou du pâté de campagne."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le nom de l'instrument qui permet de 'pousser' (ou d'embosser) la farce à saucisse dans son boyau naturel ou synthétique ?",
                    "answerOptions": [
                        {"text": "Le jeu de cales d'épaisseur (ou la jauge d'épaisseur) pour mesurer l'espace entre deux surfaces.", "isCorrect": False, "key": "A"},
                        {"text": "Le poussoir hydraulique (ou à manivelle) pour introduire la farce sous pression (remplissage homogène).", "isCorrect": True, "key": "B"},
                        {"text": "L'amylase, qui transforme l'amidon en sucres (alimentation de la levure).", "isCorrect": False, "key": "C"},
                        {"text": "Le colorant (curcuma) pour donner une couleur jaune à la mie des pains spéciaux.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le poussoir doit être utilisé sans créer de bulles d'air (poches) dans le boyau (risque de contamination et de mauvaise tenue)."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est l'impact d'une mauvaise 'température de cuisson' (trop forte et trop rapide) sur un jambon au torchon ?",
                    "answerOptions": [
                        {"text": "Le son déchire le réseau de gluten, réduisant le volume du pain et augmentant l'hydratation (besoin en eau).", "isCorrect": False, "key": "A"},
                        {"text": "Le jambon sera sec, décharné et présentera des poches de gras et d'eau (perte de rendement et de texture).", "isCorrect": True, "key": "B"},
                        {"text": "Le son accélère l'activité de la levure et augmente la production d'acide lactique.", "isCorrect": False, "key": "C"},
                        {"text": "Le son ne change rien aux propriétés de la pâte, il est uniquement un apport nutritionnel (fibres).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le jambon (produit cuit) doit être cuit lentement, à basse température (souvent en dessous de 85°C) pour conserver son hydratation et son moelleux."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le rôle du 'foie' (volaille ou porc) dans la fabrication des mousses et des pâtés supérieurs (farce fine) ?",
                    "answerOptions": [
                        {"text": "Elle dégrade l'amidon en sucres simples (maltose) qui servent de nourriture à la levure et assurent la coloration de la croûte.", "isCorrect": False, "key": "A"},
                        {"text": "Il apporte une saveur puissante, une couleur spécifique (rosée) et une texture fondante (crémeuse) à la préparation.", "isCorrect": True, "key": "B"},
                        {"text": "Elle régule l'acidité (pH) de la pâte et assure la bonne conservation du produit fini.", "isCorrect": False, "key": "C"},
                        {"text": "Elle sert uniquement à blanchir la mie du pain et à réduire l'activité des lactobacilles (levain).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le foie (foie gras, foie de volaille) est l'ingrédient clé des mousses et des pâtés haut de gamme (texture et goût)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est l'impact d'une 'farce trop chaude' (hachage ou cutterage excessif) lors de l'embossage de la saucisse ?",
                    "answerOptions": [
                        {"text": "Elle rend la pâte plus ferme, plus tenace (renforcement du gluten) et elle augmente le temps de pétrissage.", "isCorrect": False, "key": "A"},
                        {"text": "La farce risque de se 'casser' (le gras fond) et le produit final sera sec, décharné et de mauvaise qualité (mauvais liant).", "isCorrect": True, "key": "B"},
                        {"text": "Elle n'a aucun impact sur la pâte, mais elle accélère la corrosion des machines du fournil.", "isCorrect": False, "key": "C"},
                        {"text": "Elle diminue le taux de cendres de la farine et ralentit l'activité des bactéries lactiques du levain.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La température de la farce doit être maintenue sous les 12°C. L'utilisation de glace (eau) est vitale."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le rôle du 'lard' (ou barde de lard) dans la cuisson d'une terrine ou d'un pâté ?",
                    "answerOptions": [
                        {"text": "Il apporte une valeur nutritive, de la couleur, du liant et améliore la conservation du produit fini.", "isCorrect": False, "key": "A"},
                        {"text": "Il est utilisé pour envelopper la farce (protection) et l'empêcher de se dessécher pendant la cuisson (maintien du moelleux).", "isCorrect": True, "key": "B"},
                        {"text": "Il renforce le réseau de gluten (ténacité) et augmente le temps de pétrissage de la pâte.", "isCorrect": False, "key": "C"},
                        {"text": "Il sert d'agent de blanchiment de la mie du pain (aspect très blanc et sec).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La barde de lard (graisse de couverture) est essentielle pour la cuisson lente et le moelleux des farces maigres (gibier, poisson)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le nom de l'élément qui permet le 'liant' d'une farce (cohésion) et sa bonne tenue après cuisson (ingrédient non protéique) ?",
                    "answerOptions": [
                        {"text": "La panade (mélange de pain trempé ou de farine/lait/œuf) pour l'apport d'amidon (agent de liaison).", "isCorrect": True, "key": "A"},
                        {"text": "La levure lactique et la levure acétique (pour les arômes et l'acidité).", "isCorrect": False, "key": "B"},
                        {"text": "La levure en poudre et la levure en flocons (pour le volume et la coloration).", "isCorrect": False, "key": "C"},
                        {"text": "La levure de surface (pour la croûte) et la levure de masse (pour la mie).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La panade (farine, pain de mie, semoule) sert d'absorbant et de liant (amidon) pour améliorer la texture des farces grossières."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le nom de la technique qui consiste à chauffer le boyau d'une saucisse (ou le jambon) dans une étuve pour démarrer la 'fermentation' (saucisson sec) ?",
                    "answerOptions": [
                        {"text": "L'étuvage (ou 'séchage') pour la maturation du produit avant le séchage final (développement du goût et de l'acidité).", "isCorrect": True, "key": "A"},
                        {"text": "Le pétrissage intensif pour développer le réseau de gluten.", "isCorrect": False, "key": "B"},
                        {"text": "L'autolyse (mélange farine/eau) pour améliorer l'extensibilité.", "isCorrect": False, "key": "C"},
                        {"text": "La dégradation enzymatique par les amylases (pour les sucres).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'étuvage est l'étape cruciale où les micro-organismes (ferments) transforment les sucres et baissent le pH (conservation et saveur)."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'impact de l'utilisation d'une 'pochée' (viande de veau hachée très fine) dans la farce à quenelle (produit traiteur) ?",
                    "answerOptions": [
                        {"text": "Il ralentit l'activité des levures et des bactéries (fermentation lente et contrôlée, pousse différée).", "isCorrect": False, "key": "A"},
                        {"text": "Elle apporte une texture très légère, aérée et une grande onctuosité au produit fini (par mélange de panade et d'œufs).", "isCorrect": True, "key": "B"},
                        {"text": "Il détruit totalement les micro-organismes (levures et bactéries) de la pâte.", "isCorrect": False, "key": "C"},
                        {"text": "Il n'a aucun impact sur l'activité des levures, mais il améliore la coloration de la croûte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pochée est une farce de base (panade + veau ou volaille) qui peut être montée au beurre et aux œufs pour la légèreté (quenelles de brochet)."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est le rôle du 'poussoir à pousses fines' (ou buse de petit diamètre) dans la charcuterie ?",
                    "answerOptions": [
                        {"text": "Il sert de nourriture à la levure et participe à la coloration de la croûte (réaction de Maillard).", "isCorrect": False, "key": "A"},
                        {"text": "Il permet l'embossage (remplissage) des petits boyaux (saucisses cocktails, chipolatas) pour une cuisson rapide.", "isCorrect": True, "key": "B"},
                        {"text": "Il ralentit la fermentation et augmente le taux de cendres de la farine (T).", "isCorrect": False, "key": "C"},
                        {"text": "Il sert uniquement à blanchir la mie du pain et à réduire l'activité des lactobacilles.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le choix de l'embout (buse) est crucial pour la régularité et le diamètre des saucisses (calibrage)."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le nom de la technique qui consiste à cuire une farce à pâté directement dans un bain-marie (four) pour une cuisson douce et uniforme ?",
                    "answerOptions": [
                        {"text": "L'autolyse, pour permettre aux enzymes (protéases) de rendre la pâte plus extensible et facile à travailler.", "isCorrect": False, "key": "A"},
                        {"text": "La cuisson au bain-marie (humidité) pour éviter le dessèchement de la farce et la création d'une croûte (moelleux).", "isCorrect": True, "key": "B"},
                        {"text": "Le bassinage, qui consiste à ajouter de l'eau en fin de pétrissage (pâte très hydratée).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage, qui est la première fermentation de la pâte en masse (après le pétrissage).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le bain-marie (eau chaude) permet de réguler la température de la terrine et de garantir une cuisson à cœur (70°C) sans dessèchement."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est l'objectif du 'boyau naturel' (intestin d'animal) dans le saucisson (vs boyau synthétique) ?",
                    "answerOptions": [
                        {"text": "Le sucre freine l'activité de la levure (osmose) : il faut augmenter le dosage de levure ou diminuer la quantité d'eau.", "isCorrect": False, "key": "A"},
                        {"text": "Il est perméable et favorise les échanges gazeux (séchage, fumage) et le développement de la fleur (moisissure noble).", "isCorrect": True, "key": "B"},
                        {"text": "Le sucre détruit les bactéries lactiques du levain (acidité) et empêche l'obtention des arômes.", "isCorrect": False, "key": "C"},
                        {"text": "Le sucre rend la pâte plus ferme, plus tenace (renforcement du gluten) et augmente le temps de pétrissage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le boyau naturel (tripes) est la méthode traditionnelle. Il joue un rôle crucial dans la maturation (séchage) et l'arôme du saucisson sec."
                }
            ]
        },
        # THÈME 3
        3: {
            "name": "Préparations Culinaires (Plats Cuisinés, Sauces, Assaisonnements) et Traiteur",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le rôle du 'roux' (mélange de beurre et de farine) dans la préparation d'une sauce (base Béchamel, Velouté) ?",
                    "answerOptions": [
                        {"text": "Développer le réseau de gluten, incorporer l'air (pour le volume) et obtenir une pâte homogène et élastique.", "isCorrect": False, "key": "A"},
                        {"text": "Servir d'agent de liaison (épaississant) pour la sauce (amidon) et permettre l'incorporation d'un liquide sans grumeaux.", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer l'activité des bactéries lactiques pour obtenir une pâte plus acide et aromatique.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à mélanger les ingrédients (farine, eau, sel, levure) sans développer la structure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le roux (blanc, blond ou brun) est la base de l'épaississement des sauces chaudes (liaison amidon)."
                },
                {
                    "questionNumber": 42,
                    "question": "Comment appelle-t-on le type de 'bouillon' (base liquide aromatisée) utilisé pour la cuisine de traiteur (soupes, sauces, braisage) ?",
                    "answerOptions": [
                        {"text": "Le fond (blanc ou brun) : extraction lente des sucs des os, des légumes et de la garniture aromatique (mirepoix).", "isCorrect": True, "key": "A"},
                        {"text": "L'apprêt (ou apprêt final), qui est la dernière fermentation avant l'enfournement.", "isCorrect": False, "key": "B"},
                        {"text": "Le bassinage, qui est l'ajout d'eau en fin de pétrissage (pâte très hydratée).", "isCorrect": False, "key": "C"},
                        {"text": "Le coupage ou l'assemblage (mélange de farines T55 et T65 par exemple).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les fonds (de veau, de volaille, de poisson) sont la base de la cuisine. Ils sont concentrés pour les sauces et dilués pour les potages."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le but de 'laisser suer' une garniture aromatique (oignons, carottes) au début d'une préparation (fond, braisé) ?",
                    "answerOptions": [
                        {"text": "Resserrer le réseau de gluten, homogénéiser la température de la pâte et expulser le gaz carbonique (CO₂).", "isCorrect": False, "key": "A"},
                        {"text": "Ramollir les légumes et développer leurs arômes sans aucune coloration (cuisson douce à l'étouffée).", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer l'activité de la levure et augmenter la production d'acide lactique.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le suage permet de concentrer les arômes des légumes avant l'ajout du liquide (départ d'une sauce ou d'un braisé)."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la principale difficulté lors de la confection d'un 'pâté en croûte' (problème de cuisson) ?",
                    "answerOptions": [
                        {"text": "L'aluminium s'oxyde très rapidement (couche d'alumine) et a un point de fusion très bas (risque de perçage).", "isCorrect": False, "key": "A"},
                        {"text": "S'assurer que la farce est cuite à cœur (70°C) sans que la croûte ne soit brûlée ou détrempée par l'humidité de la farce.", "isCorrect": True, "key": "B"},
                        {"text": "Le bassinage, qui est l'ajout d'eau en fin de pétrissage (pâte très hydratée).", "isCorrect": False, "key": "C"},
                        {"text": "Le coupage ou l'assemblage (mélange de farines T55 et T65 par exemple).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La cuisson du pâté en croûte est délicate (deux éléments différents à cuire). L'ajout de gelée (foncée) après cuisson est crucial pour l'esthétique et la conservation."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le but de 'faire dégorger' (tremper) les ris de veau ou les abats avant la cuisson ?",
                    "answerOptions": [
                        {"text": "Contrôler la déchirure de la croûte pendant la cuisson (développement du pain) et créer un motif esthétique.", "isCorrect": False, "key": "A"},
                        {"text": "Retirer les impuretés, le sang résiduel et blanchir la pièce pour une meilleure présentation et une texture plus souple.", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer l'activité de la levure et augmenter la production d'acide lactique.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le dégorgement (à l'eau froide) est une étape de préparation pour les abats ou certaines viandes (saumurage) avant la cuisson."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la principale caractéristique de la 'pâte à foncer' utilisée pour les tartes ou les fonds de quiche (produits traiteur) ?",
                    "answerOptions": [
                        {"text": "Il donne une pâte avec une extensibilité et une blancheur de mie modérées (le plus souvent utilisé).", "isCorrect": False, "key": "A"},
                        {"text": "C'est une pâte non levée, croustillante, qui ne se rétracte pas à la cuisson et est riche en matière grasse (beurre ou margarine).", "isCorrect": True, "key": "B"},
                        {"text": "Il donne une pâte très tenace, avec une mie très colorée et une forte acidité (pétrissage lent/manuel).", "isCorrect": False, "key": "C"},
                        {"text": "Il sert uniquement à mélanger les ingrédients (farine, eau, sel, levure) sans développer la structure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pâte à foncer (ou pâte brisée) est la base des préparations salées (quiches, tourtes). Elle est neutre en goût et résiste à l'humidité de la garniture."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le phénomène qui se produit lors du 'montage d'une mayonnaise' (sauce froide) ?",
                    "answerOptions": [
                        {"text": "Le coup de four : le développement rapide du pain sous l'effet de la chaleur et de l'évaporation de l'eau.", "isCorrect": False, "key": "A"},
                        {"text": "L'émulsion : l'incorporation stable d'une phase huileuse (gras) dans une phase aqueuse (eau, jaune d'œuf) grâce à la lécithine (jaune).", "isCorrect": True, "key": "B"},
                        {"text": "La réaction enzymatique : la transformation de l'amidon en sucres simples (amylase).", "isCorrect": False, "key": "C"},
                        {"text": "L'autolyse : le repos de la pâte pour améliorer l'extensibilité.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La mayonnaise est une émulsion stable (liée par la lécithine du jaune d'œuf) ; si elle est trop froide ou trop rapide, elle 'tourne' (casse l'émulsion)."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est le rôle de la 'gelée' (gélatine) versée dans le pâté en croûte après la cuisson ?",
                    "answerOptions": [
                        {"text": "Elle maintient l'humidité de la surface du pain pour retarder la formation de la croûte (meilleur développement, croûte fine et brillante).", "isCorrect": False, "key": "A"},
                        {"text": "Elle remplit l'espace vide créé par la rétractation de la farce, améliore la conservation et l'esthétique (coupe nette).", "isCorrect": True, "key": "B"},
                        {"text": "Elle sert uniquement à nettoyer les parois du four avant l'enfournement du pain.", "isCorrect": False, "key": "C"},
                        {"text": "Elle diminue le temps de cuisson et augmente le taux de cendres de la farine (T).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gelée (chaude et liquide) est versée par la cheminée (trou du couvercle) et se solidifie en refroidissant (tenue du pâté)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est l'étape qui consiste à vérifier la température à cœur d'un plat cuisiné (lasagnes, gratins) avant le maintien au chaud ou la vente ?",
                    "answerOptions": [
                        {"text": "La division (ou pesée), réalisée à la main ou à la diviseuse (mécanique).", "isCorrect": False, "key": "A"},
                        {"text": "Le contrôle à la sonde thermique (température interne) : minimum 65°C pour le maintien au chaud.", "isCorrect": True, "key": "B"},
                        {"text": "Le rafraîchi (pour le levain), qui consiste à ajouter de la farine et de l'eau.", "isCorrect": False, "key": "C"},
                        {"text": "Le bassinage, qui est l'ajout d'eau en fin de pétrissage (pâte très hydratée).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le maintien au chaud (CCP) doit être supérieur à 63°C pour éviter la prolifération bactérienne (TDZ)."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le but de 'l'assaisonnement' (sel, poivre, épices) dans les préparations traiteur (salades, farces) ?",
                    "answerOptions": [
                        {"text": "Donner une forme ronde au pâton et resserrer la surface pour donner de la force et de la tenue au pâton.", "isCorrect": False, "key": "A"},
                        {"text": "Améliorer le goût (saveur) et l'équilibre des saveurs (acide, salé, sucré) pour une expérience gustative complète.", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer l'activité de la levure et augmenter la production d'acide lactique.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'assaisonnement est l'étape qui finalise le goût. Il doit être ajusté pour équilibrer la préparation."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le phénomène qui se produit dans le four lors de la cuisson d'un jambon ou d'une terrine (viande cuite) ?",
                    "answerOptions": [
                        {"text": "La formation d'une fine pellicule sèche à la surface du pâton pour éviter qu'il ne colle aux outils.", "isCorrect": False, "key": "A"},
                        {"text": "La coagulation des protéines (chaleur) qui permet de lier la farce (tenue) et de détruire les micro-organismes (sécurité).", "isCorrect": True, "key": "B"},
                        {"text": "La dégradation enzymatique par les amylases (pour les sucres) lors de l'autolyse.", "isCorrect": False, "key": "C"},
                        {"text": "La coloration rapide de la croûte lors de la cuisson (réaction de Maillard).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La coagulation (dénaturation) des protéines est essentielle pour la tenue des farces (pâtés, terrines). C'est le but de la cuisson à cœur."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est l'outil utilisé pour ébavurer et lisser un cordon de soudure (préparation avant masticage) ?",
                    "answerOptions": [
                        {"text": "La meuleuse d'angle ou la ponceuse pneumatique (disque abrasif ou disque à lamelles).", "isCorrect": False, "key": "A"},
                        {"text": "La mandoline (ou le couteau de chef) pour la découpe fine et régulière des légumes (salades, garnitures).", "isCorrect": True, "key": "B"},
                        {"text": "La corne (ou raclette) pour le travail des pâtes molles (rabat, nettoyage).", "isCorrect": False, "key": "C"},
                        {"text": "Le banneton pour la pousse des pains ronds (seigle, campagne).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La régularité des coupes (ciselage, taillage) est la base de l'esthétique des plats traiteur."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le nom du processus d'assemblage qui utilise une colle spéciale (bi-composante) pour la fixation de certains éléments ?",
                    "answerOptions": [
                        {"text": "Le collage structurel (méthode de plus en plus courante pour les pièces en composite, aluminium ou en acier HLE).", "isCorrect": False, "key": "A"},
                        {"text": "La décoration et le 'lustrage' des plats (ajout de gelée, d'herbes, de lustrant) pour l'aspect visuel (vente).", "isCorrect": True, "key": "B"},
                        {"text": "L'autolyse (repos de la farine et de l'eau) pour améliorer l'extensibilité.", "isCorrect": False, "key": "C"},
                        {"text": "Le rafraîchi (pour le levain), qui consiste à ajouter de la farine et de l'eau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'aspect visuel est le premier facteur de vente (attractivité) pour les produits traiteur (étalage, buffet)."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'impact d'une mauvaise 'coupe' (trop rapide ou irrégulière) de la viande destinée à un pâté en croûte ?",
                    "answerOptions": [
                        {"text": "Le pain va s'étaler (pas de coup de four), la croûte sera épaisse, et il y aura un risque de sous-cuisson (mie collante).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de texture irrégulière, de mauvaise tenue à la coupe et de perte de l'esthétique (farce grossière ou trop fine).", "isCorrect": True, "key": "B"},
                        {"text": "La buée (vapeur) sera excessive et le pain sera acide (mauvais goût).", "isCorrect": False, "key": "C"},
                        {"text": "L'activité de la levure sera bloquée et le pain n'aura aucun volume (pain plat).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La taille des dés (coupe) est cruciale pour la texture à la dégustation et la tenue du pâté (farce en gros dés ou en haché)."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le rôle du 'gros sel' (sel de Guérande, sel gemme) dans la préparation des salaisons ?",
                    "answerOptions": [
                        {"text": "Il empêche le pâton de coller aux toiles (couches) ou au plan de travail avant la cuisson.", "isCorrect": False, "key": "A"},
                        {"text": "Il permet la 'prise au sel' (osmose) : extraction de l'eau et pénétration du sel pour la conservation et l'arôme (produits secs).", "isCorrect": True, "key": "B"},
                        {"text": "Il sert uniquement à colorer la croûte du pain lors de la cuisson finale (aspect esthétique).", "isCorrect": False, "key": "C"},
                        {"text": "Il accélère l'activité des bactéries lactiques pour obtenir une pâte plus acide.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le gros sel est utilisé pour le salage à sec (jambons, lardons). Il permet une pénétration lente et contrôlée."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'outil utilisé pour retirer les points de soudure d'origine (dessoudage) sans déformer la tôle?",
                    "answerOptions": [
                        {"text": "La perceuse et le foret à dépointer (perçage au centre du point de soudure).", "isCorrect": False, "key": "A"},
                        {"text": "La cellule de refroidissement (blast chiller) pour un refroidissement rapide des plats cuisinés (moins de 2 heures).", "isCorrect": True, "key": "B"},
                        {"text": "Le diviseuse-bouleuse (pour la division en pâtons égaux).", "isCorrect": False, "key": "C"},
                        {"text": "Le pétrin (pour le mélange et l'incorporation des ingrédients).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le refroidissement rapide est un CCP (Point Critique pour la Maîtrise) de l'HACCP pour les produits cuisinés (farces, sauces, soupes)."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment s'appelle l'opération qui consiste à étaler la pâte à croissant (ou pâte feuilletée) avant le 'tourage' ?",
                    "answerOptions": [
                        {"text": "L'abaisse (ou l'étalement), pour obtenir la forme et l'épaisseur désirées pour le beurre d'incorporation.", "isCorrect": False, "key": "A"},
                        {"text": "Le 'pochage' : cuisson d'un aliment (quenelle, terrine, abats) dans un liquide (fond ou bouillon) à basse température (inférieure à 100°C).", "isCorrect": True, "key": "B"},
                        {"text": "Le rafraîchi (pour le levain), qui consiste à ajouter de la farine et de l'eau.", "isCorrect": False, "key": "C"},
                        {"text": "Le chanfreinage (ou ébarbage) pour préparer les bords de la tôle à la soudure (angle de pénétration).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le pochage est une cuisson douce pour les produits délicats (poisson, abats) afin d'assurer un moelleux maximum (sans ébullition)."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le but du 'maintien au chaud' (bain-marie, vitrine chauffante) des plats traiteur (au-delà de 2 heures) ?",
                    "answerOptions": [
                        {"text": "Avoir une consistance (plasticité) similaire à celle de la pâte pour éviter qu'il ne s'échappe lors du laminoir (beurre trop froid).", "isCorrect": False, "key": "A"},
                        {"text": "Maintenir impérativement la température à cœur du produit au-dessus de 63°C (hors zone de danger bactériologique).", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer la production de gaz carbonique (CO₂) et la levée du produit fini.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le maintien au chaud (supérieur à 63°C) est un CCP pour la sécurité alimentaire. La durée maximale est réglementée (souvent 4 heures)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le nom de l'étape qui consiste à plier la pâte à plusieurs reprises (3 ou 4 tours) avec le beurre pour créer les 'feuilles' ?",
                    "answerOptions": [
                        {"text": "Le tourage (tour simple ou tour double), qui crée l'alternance de pâte et de matière grasse (feuilletage).", "isCorrect": False, "key": "A"},
                        {"text": "L'opération de 'saisir' (ou marquer) une pièce de viande (braisé, rôti) avant la cuisson lente.", "isCorrect": True, "key": "B"},
                        {"text": "L'apprêt (ou apprêt final), qui est la dernière fermentation avant l'enfournement.", "isCorrect": False, "key": "C"},
                        {"text": "L'autolyse (repos de la farine et de l'eau) pour améliorer l'extensibilité.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Saisir (cuisson rapide et forte) crée une croûte (réaction de Maillard) qui conserve les sucs et donne la couleur du braisé (goût)."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle de la 'détente' (temps de repos) des pâtons avant le façonnage final (baguette) ?",
                    "answerOptions": [
                        {"text": "Permettre au réseau de gluten de se relâcher pour que le pâton soit plus souple et extensible pour le façonnage.", "isCorrect": False, "key": "A"},
                        {"text": "La vérification finale de l'assaisonnement et de la texture (avant la vente ou le conditionnement).", "isCorrect": True, "key": "B"},
                        {"text": "Ajouter du sel dans la pâte pour freiner la fermentation et augmenter l'acidité.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le contrôle qualité (goût et texture) est la dernière vérification avant de proposer le produit au client."
                }
            ]
        },
        # THÈME 4
        4: {
            "name": "Techniques de Conservation (Salaison, Fumage, Mise sous vide) et Produits Secs",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la principale caractéristique du 'séchage' dans la fabrication du saucisson sec (produit fermenté) ?",
                    "answerOptions": [
                        {"text": "Elle est très enrichie en œufs, en sucre et en matière grasse (beurre) et nécessite un pétrissage très long.", "isCorrect": False, "key": "A"},
                        {"text": "C'est l'étape de déshydratation progressive (perte de poids) qui permet la conservation longue durée et le développement des arômes (maturation).", "isCorrect": True, "key": "B"},
                        {"text": "Elle est très peu hydratée (moins de 50% d'eau) pour une conservation très longue.", "isCorrect": False, "key": "C"},
                        {"text": "Elle est fabriquée sans sel, pour un goût plus doux et un pétrissage très court.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le séchage (lent et contrôlé) réduit l'activité de l'eau (Aw) et bloque le développement des bactéries (conservation). La perte de poids est essentielle."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le nom de l'ingrédient (E250) qui fixe la couleur rose (hémoglobine) et empêche le développement du Clostridium Botulinum ?",
                    "answerOptions": [
                        {"text": "Le sel nitrité (mélange de sel de cuisine et de nitrite de sodium) pour le jambon et les saucissons secs.", "isCorrect": True, "key": "A"},
                        {"text": "Le mastic polyester (bi-composant) pour combler les défauts de surface (creux, rayures profondes) avant l'apprêt.", "isCorrect": False, "key": "B"},
                        {"text": "La farine de maïs (sans gluten) avec une poudre à lever (baking powder) pour le volume.", "isCorrect": False, "key": "C"},
                        {"text": "La farine de blé (T150) avec une faible hydratation pour la conservation.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le sel nitrité est le conservateur/fixateur de couleur le plus important de la charcuterie. Son dosage est strictement réglementé (toxicité)."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la principale caractéristique du 'fumage' (à chaud ou à froid) des produits (saucisses, jambon) ?",
                    "answerOptions": [
                        {"text": "Il se conserve beaucoup plus longtemps (plusieurs jours) grâce à l'acidité produite par les bactéries lactiques.", "isCorrect": False, "key": "A"},
                        {"text": "Il apporte des arômes boisés, une couleur spécifique (dorée/brune) et des propriétés anti-bactériennes (phénols).", "isCorrect": True, "key": "B"},
                        {"text": "Il doit être consommé dans les 24 heures en raison d'une forte teneur en eau (hydrolyse).", "isCorrect": False, "key": "C"},
                        {"text": "Il contient des additifs (conservateurs) qui prolongent sa durée de vie (faux pour le vrai levain).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le fumage (souvent à froid, moins de 25°C) est une étape d'aromatisation et de conservation (naturelle) grâce aux composants de la fumée."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est le rôle de la 'saumure' (mélange de sel, nitrite, sucres, épices) dans le jambon cuit ?",
                    "answerOptions": [
                        {"text": "L'incorporation de la matière grasse (beurre de tourage) pendant l'étape de tourage (pliage).", "isCorrect": False, "key": "A"},
                        {"text": "Elle permet la pénétration du sel (conservation), la fixation de la couleur et le moelleux de la viande (par injection).", "isCorrect": True, "key": "B"},
                        {"text": "L'utilisation de farine de seigle (T130) qui contient des pentosanes (gommes).", "isCorrect": False, "key": "C"},
                        {"text": "La cuisson à haute température (plus de 300°C) pour un développement rapide de la croûte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La saumure (liquide) est injectée directement dans les muscles pour garantir une salaison uniforme (jambon cuit, épaule)."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le nom de la technique pour cuire une baguette de tradition sur la sole du four (sans plaque) ?",
                    "answerOptions": [
                        {"text": "La cuisson sur sole (ou cuisson à plat) pour une meilleure transmission de la chaleur et une croûte croustillante.", "isCorrect": False, "key": "A"},
                        {"text": "La 'mise sous vide' (emballage) : retrait de l'air pour ralentir l'oxydation (goût) et la croissance des micro-organismes aérobies.", "isCorrect": True, "key": "B"},
                        {"text": "La cuisson par injection de vapeur (buée) pour l'humidification de la surface.", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte (pousse bloquée) pour une cuisson différée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La mise sous vide (emballage sans oxygène) prolonge la DLC des produits cuits et crus (conservation froide) et évite la contamination."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le risque de sécher un saucisson sec (maturation) dans une pièce trop chaude et trop humide ?",
                    "answerOptions": [
                        {"text": "Elle n'utilise pas de levure ni de levain. La pousse est assurée par l'évaporation de l'eau (buée) lors de la cuisson (gonflement).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de 'croûtage' (surface sèche et dure) qui bloque l'évaporation de l'eau interne (produit moisi ou pourri à l'intérieur).", "isCorrect": True, "key": "B"},
                        {"text": "Elle est fabriquée avec une farine de seigle (T130) et un levain liquide pour l'acidité.", "isCorrect": False, "key": "C"},
                        {"text": "Elle nécessite un pétrissage très long et un temps de pointage de plus de 4 heures.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le séchage doit être très lent et progressif. Une mauvaise ventilation ou une humidité/température élevée entraîne le croûtage (produit non sécuritaire)."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le risque si la température de la chambre de 'salaison' (jambon sec) est trop basse ou trop élevée ?",
                    "answerOptions": [
                        {"text": "Le risque de 'brûler' les micro-organismes (levures et bactéries) et de bloquer l'activité du levain.", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de 'contamination' (trop chaud) ou de 'non-pénétration du sel' (trop froid, altération de la qualité).", "isCorrect": True, "key": "B"},
                        {"text": "La diminution du taux de cendres (T) de la farine utilisée pour le rafraîchi.", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation de la force (W) de la farine de rafraîchi (ténacité).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La salaison (prise de sel) est une étape de conservation. Le sel doit pénétrer uniformément le muscle (température et temps précis)."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le rôle de la 'fleur' (ou pénicillium) à la surface du saucisson sec (couleur blanche/verte) ?",
                    "answerOptions": [
                        {"text": "La peau d'orange (surface irrégulière) ou l'inclusion de poussières (petites bosses).", "isCorrect": False, "key": "A"},
                        {"text": "C'est une moisissure noble (levure de surface) qui protège le produit de l'oxydation et des moisissures toxiques (goût).", "isCorrect": True, "key": "B"},
                        {"text": "Le pain de seigle (T130) qui contient des pentosanes (gommes).", "isCorrect": False, "key": "C"},
                        {"text": "Le pain complet (T150) qui nécessite un temps de pétrissage très long (fibres).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La fleur (levure naturelle ou inoculée) est un signe de qualité pour les produits secs traditionnels (protection contre les moisissures pathogènes)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le nom de l'étape qui permet de donner la brillance et la couleur finale au croissant ou à la brioche avant la cuisson ?",
                    "answerOptions": [
                        {"text": "La dorure (badigeonnage à l'œuf entier ou au jaune d'œuf) avant ou après l'apprêt final.", "isCorrect": False, "key": "A"},
                        {"text": "Le 'plombage' : ajout de graisse (saindoux) ou de cire sur la surface coupée (boudin) pour éviter l'oxydation (contact avec l'air).", "isCorrect": True, "key": "B"},
                        {"text": "La buée (vapeur d'eau) pour humidifier la surface du pain (croûte fine).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage (première fermentation) en masse (avant la division).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le plombage (ou la mise en graisse) est une technique de conservation pour les produits à forte teneur en gras (pâtés, rillettes) qui oxydent vite (couleur grise)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le nom de la technique de conservation par 'confit' (graisse d'oie, de canard, de porc) des viandes ?",
                    "answerOptions": [
                        {"text": "Obtenir une mie très blanche, très aérée, avec une croûte fine (souple) grâce au moule fermé et à l'enrichissement en matière grasse.", "isCorrect": False, "key": "A"},
                        {"text": "Le confisage (ou confit) : cuisson lente dans la graisse, puis recouvrement total par la graisse (barrière à l'air) pour la conservation longue.", "isCorrect": True, "key": "B"},
                        {"text": "Fabriquer un pain très acide (pH bas) pour une conservation longue (plus de 5 jours).", "isCorrect": False, "key": "C"},
                        {"text": "Utiliser uniquement de la farine de seigle (T130) et du levain naturel pour l'acidité.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le confit est une méthode de conservation ancestrale. La graisse (chauffée et liquide) recouvre la viande (cuite) et bloque l'accès à l'oxygène (anaérobie)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est le nom de l'outil qui permet de mélanger et de doser très précisément la teinte (couleur) et ses composants ?",
                    "answerOptions": [
                        {"text": "Le spectro-photomètre (lecture optique de la couleur) et la balance de précision (dosage au gramme près).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'thermo-plongeur' ou 'cuiseur sous vide' (thermo-sonde) pour la cuisson des produits traiteur (contrôle précis de la température).", "isCorrect": True, "key": "B"},
                        {"text": "Le pain de mie (carré, cuit en moule fermé) pour les sandwichs.", "isCorrect": False, "key": "C"},
                        {"text": "Le croissant (pâte levée feuilletée, enrichie en beurre).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La cuisson sous vide (ou à basse température) garantit une cuisson précise et un moelleux maximal. Elle est essentielle pour le traiteur."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le danger de laisser un croissant (pâte crue) dans une chambre de pousse trop chaude et trop humide ?",
                    "answerOptions": [
                        {"text": "Le beurre va fondre et s'incorporer à la pâte (dégraissage) ; le feuilletage sera perdu (produit plat et lourd).", "isCorrect": False, "key": "A"},
                        {"text": "La 'sur-salaison' : un jambon trop salé qui ne peut pas se dessaler et a un goût trop prononcé (mauvaise qualité).", "isCorrect": True, "key": "B"},
                        {"text": "L'activité de la levure sera bloquée et le produit n'aura aucun volume (pain plat).", "isCorrect": False, "key": "C"},
                        {"text": "La croûte sera épaisse et dure, même après la cuisson (sous-développement).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le dosage du sel (salaison) est crucial. Une sur-salaison peut être irrécupérable (goût trop salé, jambon trop sec)."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le nom de l'étape qui consiste à réactiver le levain naturel (ajout d'eau et de farine) pour augmenter sa population de micro-organismes ?",
                    "answerOptions": [
                        {"text": "Le rafraîchi, pour le préparer au pétrissage (levain chef ou levain de masse).", "isCorrect": False, "key": "A"},
                        {"text": "La 'stérilisation' (ou appertisation) : chauffage à haute température (plus de 115°C) pour tuer toutes les bactéries (conserve longue durée).", "isCorrect": True, "key": "B"},
                        {"text": "Le bassinage, qui est l'ajout d'eau en fin de pétrissage (pâte très hydratée).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage (ou pointage en masse), qui est la première fermentation de la pâte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La stérilisation est utilisée pour les conserves (bocaux) qui peuvent être stockées à température ambiante (produit stable)."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le rôle du 'pâté fermentée' (ancienne pâte réintroduite) dans la fabrication du pain (méthode indirecte) ?",
                    "answerOptions": [
                        {"text": "Améliorer le goût, la conservation et la force (W) de la pâte fraîche (pousse plus rapide).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'pressage' (ou égouttage) des terrines ou du fromage de tête après cuisson (pour retirer le liquide de cuisson et améliorer la tenue).", "isCorrect": True, "key": "B"},
                        {"text": "Réguler l'acidité (pH) de la pâte et assurer la bonne conservation du produit fini.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le pressage (avec un poids) permet d'expulser l'air et le jus de cuisson de la farce (meilleure coupe, meilleure conservation)."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le nom de la technique pour cuire des petits pains ronds (pains au lait, hamburgers) sur une plaque (grille) sans la sole du four ?",
                    "answerOptions": [
                        {"text": "La cuisson sur plaque (ou cuisson sur grille) pour une croûte souple et fine (produits de viennoiserie).", "isCorrect": False, "key": "A"},
                        {"text": "L'utilisation de la 'lécithine de soja' (émulsifiant) pour stabiliser les farces fines et les mousses.", "isCorrect": True, "key": "B"},
                        {"text": "La cuisson par injection de vapeur (buée) pour l'humidification de la surface.", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte (pousse bloquée) pour une cuisson différée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La lécithine est un additif (E322) qui aide à l'émulsion (mélange stable) des farces à forte teneur en gras et en eau."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est l'ingrédient principal utilisé dans les pains sans gluten (pour les personnes intolérantes) ?",
                    "answerOptions": [
                        {"text": "Des farines de céréales (maïs, riz, sarrasin) et l'ajout d'une gomme (gomme de guar) pour compenser l'absence de gluten.", "isCorrect": False, "key": "A"},
                        {"text": "La 'date limite de consommation' (DLC) qui indique la date au-delà de laquelle l'aliment est considéré comme dangereux (risques sanitaires).", "isCorrect": True, "key": "B"},
                        {"text": "De la farine de seigle (T130) avec un levain de seigle (acidité) pour la structure.", "isCorrect": False, "key": "C"},
                        {"text": "De la farine de blé (T150) avec une faible hydratation pour la conservation.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La DLC est obligatoire pour les produits très périssables (viande, charcuterie fraîche). Elle est calculée en laboratoire (tests)."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le risque d'utiliser une quantité trop importante de levain chef (trop de bactéries lactiques) dans la pâte à pain ?",
                    "answerOptions": [
                        {"text": "Un pain trop acide (goût de vinaigre), une mie trop serrée et un risque de sur-acidification (dégradation de la pâte).", "isCorrect": False, "key": "A"},
                        {"text": "La 'pasteurisation' : chauffage à température moyenne (70°C à 85°C) pour réduire la population de germes (conservation courte, au froid).", "isCorrect": True, "key": "B"},
                        {"text": "La non-levée de la pâte (pas de CO₂) et une absence de volume (pain plat).", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation de la force (W) de la farine de rafraîchi (ténacité).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pasteurisation est utilisée pour le conditionnement (jus de fruits, certains pâtés) : elle est moins agressive que la stérilisation."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est l'étape qui permet de donner une couleur très foncée (caramélisation) et un goût prononcé aux pains spéciaux (pain au seigle, pain noir) ?",
                    "answerOptions": [
                        {"text": "L'ajout de malt torréfié ou de poudre de cacao (coloration) et une cuisson lente à température moyenne.", "isCorrect": False, "key": "A"},
                        {"text": "La 'surgélation' (chute rapide de la température à -18°C) pour bloquer l'activité enzymatique et bactérienne (conservation très longue).", "isCorrect": True, "key": "B"},
                        {"text": "L'incorporation de la matière grasse (beurre de tourage) pendant l'étape de tourage (feuilletage).", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte (pousse bloquée) pour une cuisson différée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La surgélation (rapide) est préférée à la congélation (lente) pour la qualité. Elle est utilisée pour la majorité des plats cuisinés traiteur."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le but d'un 'pointage très long' (pousse lente de plusieurs heures) pour la pâte de tradition ?",
                    "answerOptions": [
                        {"text": "Développer une meilleure complexité aromatique, un meilleur alvéolage et une meilleure conservation.", "isCorrect": False, "key": "A"},
                        {"text": "Le 'poussièreur' : un chiffon collant (pistolet à air chaud) pour retirer les micro-poussières avant l'application du vernis.", "isCorrect": False, "key": "B"},
                        {"text": "La 'maturation' (affinage) des produits secs (saucisson, jambon) qui permet le développement des saveurs (enzymes).", "isCorrect": True, "key": "C"},
                        {"text": "Accélérer la production de gaz carbonique (CO₂) et la levée du produit fini.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La maturation (plusieurs semaines à mois) est l'étape qui donne les arômes et la saveur finale des produits de salaison (goût de terroir)."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la principale caractéristique de la farine de maïs (polenta, pain de maïs) utilisée en panification ?",
                    "answerOptions": [
                        {"text": "Elle est naturellement sans gluten et doit être mélangée à de la farine de blé (ou un liant) pour pouvoir lever.", "isCorrect": False, "key": "A"},
                        {"text": "Le 'pH' (Potentiel Hydrogène) : un indicateur de l'acidité (basse) de la farce qui assure la conservation des produits secs (fermentation).", "isCorrect": True, "key": "B"},
                        {"text": "Elle est très riche en sel (minéraux) et freine l'activité de la levure (osmose).", "isCorrect": False, "key": "C"},
                        {"text": "Elle sert uniquement à colorer la croûte du pain lors de la cuisson finale (aspect esthétique).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le pH (souvent autour de 5.0 à 5.3) indique une bonne fermentation (acide) qui est un facteur clé pour la conservation (produit sec et sûr)."
                }
            ]
        },
        # THÈME 5
        5: {
            "name": "Gestion (Fiches Techniques, Prix de Revient, Coûts) et Mathématiques Appliquées",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le nom du tableau qui permet de calculer le prix de revient d'une intervention (main d'œuvre, peinture, pièces) ?",
                    "answerOptions": [
                        {"text": "Le tableau de 'la formule du boulanger' (ou 'recette') pour la détermination des ingrédients.", "isCorrect": False, "key": "A"},
                        {"text": "La 'Fiche Technique de Fabrication' (FTF) qui détaille la recette, les étapes, le coût des matières et le prix de revient théorique.", "isCorrect": True, "key": "B"},
                        {"text": "Le coefficient d'hydratation (H) de la farine (pour la force).", "isCorrect": False, "key": "C"},
                        {"text": "Le plan de production et le planning des employés (gestion du personnel).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La FTF est le document de base pour la standardisation de la production et le calcul du coût (Matières Premières)."
                },
                {
                    "questionNumber": 82,
                    "question": "Si une terrine de 1,5 kg (poids net) a une perte à la cuisson de 20%, quel est son poids après cuisson (en kg) ?",
                    "answerOptions": [
                        {"text": "1,20 kg (1,5 kg x (1 - 0,20)).", "isCorrect": True, "key": "A"},
                        {"text": "10,0 kg d'eau (100% d'hydratation).", "isCorrect": False, "key": "B"},
                        {"text": "70,0 kg d'eau.", "isCorrect": False, "key": "C"},
                        {"text": "1,4 kg d'eau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 1,5 kg x 0,80 = 1,20 kg. La perte (fonte du gras, évaporation de l'eau) doit être intégrée au calcul du prix de revient."
                },
                {
                    "questionNumber": 83,
                    "question": "Si la matière première (viande, gras, épices) coûte 8,00 € pour une terrine de 1 kg cuite, et que l'on vise un coût matière de 30% du prix de vente HT, quel est le prix de vente HT minimum (en €) ?",
                    "answerOptions": [
                        {"text": "26,67 € HT (8,00 € / 0,30).", "isCorrect": True, "key": "A"},
                        {"text": "180 grammes de sel.", "isCorrect": False, "key": "B"},
                        {"text": "9 grammes de sel.", "isCorrect": False, "key": "C"},
                        {"text": "18 grammes de sel.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 8,00 € / 0,30 = 26,67 € HT. Le coût matière (ou 'food cost') est la base de la rentabilité en traiteur."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le rôle du 'coefficient de production' (ou rendement) dans la gestion des ingrédients (ex : rendement de désossage) ?",
                    "answerOptions": [
                        {"text": "Calculer le coût total de production (matières premières + main d'œuvre + charges) pour fixer le prix de vente.", "isCorrect": False, "key": "A"},
                        {"text": "Il permet de calculer la quantité de matière première brute (os inclus) à commander pour obtenir la quantité nette de produit désossé.", "isCorrect": True, "key": "B"},
                        {"text": "Mesurer la force de la farine (W) à l'alvéographe (test de qualité).", "isCorrect": False, "key": "C"},
                        {"text": "Vérifier la bonne exécution du nettoyage et l'absence de micro-organismes (HACCP).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le rendement (ex : 80% de viande sur os) permet de gérer les achats et de calculer le coût réel de la matière première nette."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le rôle du 'diagnostic' dans la réparation de carrosserie (après un choc) ?",
                    "answerOptions": [
                        {"text": "Identifier les dommages visibles et cachés (structure, mécanique, électrique) pour établir la méthode de réparation.", "isCorrect": False, "key": "A"},
                        {"text": "L'analyse des 'Points Critiques pour la Maîtrise' (CCP) qui sont les étapes où un danger (température, pH) doit être maîtrisé (HACCP).", "isCorrect": True, "key": "B"},
                        {"text": "40°C.", "isCorrect": False, "key": "C"},
                        {"text": "20°C.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les CCP sont les étapes clés du processus où le risque est le plus grand (cuisson, refroidissement, maintien au froid/chaud)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le nom de l'outil qui permet de lire les codes défaut (DTC) des calculateurs du véhicule (électronique embarquée) ?",
                    "answerOptions": [
                        {"text": "La valise de diagnostic (ou outil de scan) pour les calculateurs (Airbag, ABS, ESP, etc.).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Plan d'Assurance Qualité' (PAQ) qui définit les contrôles (température, grammage, pH) à chaque étape de la production.", "isCorrect": True, "key": "B"},
                        {"text": "Le thermomètre sonde pour la mesure de la température interne du four.", "isCorrect": False, "key": "C"},
                        {"text": "L'hydromètre pour la mesure de l'humidité du fournil (hygrométrie).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le PAQ (partie du PMS) assure que le produit fabriqué est conforme (poids, goût, sécurité) aux normes de l'entreprise."
                },
                {
                    "questionNumber": 87,
                    "question": "Si la matière première coûte 100 € et que vous vendez le produit fini 300 € HT, quel est le taux de marge brute (en pourcentage) par rapport au prix de vente ?",
                    "answerOptions": [
                        {"text": "66,67 % ((300 € - 100 €) / 300 € x 100).", "isCorrect": True, "key": "A"},
                        {"text": "10% de perte.", "isCorrect": False, "key": "B"},
                        {"text": "25% de perte.", "isCorrect": False, "key": "C"},
                        {"text": "80% de perte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : (300 - 100) / 300 = 0,6667. La marge brute doit couvrir les charges (main d'œuvre, loyer) pour dégager un bénéfice."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est l'impact de la levure fraîche (en cube) sur la formule du boulanger (vs levure sèche) ?",
                    "answerOptions": [
                        {"text": "Elle contient environ 70% d'eau. Il faut en mettre trois fois plus que de levure sèche (1 pour 3) et ajuster l'hydratation.", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Coût de Revient Horaire' (CRH) : calcul du coût (salaires, charges, amortissement machine) de chaque heure travaillée.", "isCorrect": True, "key": "B"},
                        {"text": "Elle ne contient pas d'eau. Il n'y a pas besoin d'ajustement de l'hydratation de la formule.", "isCorrect": False, "key": "C"},
                        {"text": "Elle a le même dosage que le levain naturel (10% de la masse de farine).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le CRH est indispensable pour tarifer correctement les plats (traiteur) et les services (prestation) en intégrant le coût de la main d'œuvre (le plus gros poste)."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la marge commerciale à réaliser sur un produit (en pourcentage) pour couvrir les coûts (matières + main d'œuvre) et dégager un bénéfice ?",
                    "answerOptions": [
                        {"text": "Plus de 20% à 50% de marge brute sur les coûts (selon le type de produit et l'entreprise).", "isCorrect": False, "key": "A"},
                        {"text": "Plus de 60% à 75% de marge brute sur le prix de vente (le plus souvent en charcuterie/traiteur).", "isCorrect": True, "key": "B"},
                        {"text": "La marge est toujours négative (perte) dans le secteur de la boulangerie (faux).", "isCorrect": False, "key": "C"},
                        {"text": "10% de marge brute (marge très faible, risquant d'annuler le bénéfice).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les produits traiteur et charcutiers (forte main d'œuvre) nécessitent des marges élevées (souvent au-delà de 60% ou 70%) pour être rentables."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le nom du coût qui inclut la rémunération des employés et les charges sociales dans le prix de revient ?",
                    "answerOptions": [
                        {"text": "Le coût de la main d'œuvre (ou coût salarial) pour la production du pain.", "isCorrect": True, "key": "A"},
                        {"text": "Le coût des matières premières (farine, eau, sel, levure) uniquement.", "isCorrect": False, "key": "B"},
                        {"text": "Le coût des charges fixes (loyer, assurance, électricité) uniquement.", "isCorrect": False, "key": "C"},
                        {"text": "Le coût de la logistique (transport et stockage des ingrédients).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le coût de la main d'œuvre (salaire, charges) est souvent le coût le plus important dans le prix de revient d'une charcuterie artisanale."
                },
                {
                    "questionNumber": 91,
                    "question": "Si vous avez une commande de 15 kg de farce de saucisse (poids net) et que le rendement de la farce (parage) est de 90%, quelle quantité de viande brute faut-il préparer ?",
                    "answerOptions": [
                        {"text": "35,3 kg de pâte crue (120 x 0,25 kg = 30 kg cuit. 30 kg / 0,85 = 35,3 kg cru).", "isCorrect": False, "key": "A"},
                        {"text": "16,67 kg de viande brute (15 kg / 0,90).", "isCorrect": True, "key": "B"},
                        {"text": "25,5 kg de pâte crue.", "isCorrect": False, "key": "C"},
                        {"text": "40,0 kg de pâte crue.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 15 kg / 0,90 = 16,67 kg. Le rendement est essentiel pour la gestion des stocks et l'approvisionnement (viande)."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le nom de la propriété de la farine qui indique le pourcentage d'eau qu'elle peut absorber (hydratation maximale) ?",
                    "answerOptions": [
                        {"text": "L'absorption d'eau, mesurée au farinographe (test de qualité).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Seuil de Rentabilité' (SR) : le montant de chiffre d'affaires à réaliser pour couvrir toutes les charges (bénéfice nul).", "isCorrect": True, "key": "B"},
                        {"text": "Le rapport P/L (ténacité/extensibilité) mesuré à l'alvéographe.", "isCorrect": False, "key": "C"},
                        {"text": "Le pH (potentiel Hydrogène) de la farine qui mesure son acidité de base.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le SR (ou 'point mort') est le seuil à atteindre pour commencer à générer du bénéfice. Il est crucial pour la survie de l'entreprise."
                },
                {
                    "questionNumber": 93,
                    "question": "Si le coût matière d'un plat traiteur (salade composée) est de 3,50 € et que la marge souhaitée est de 65% du prix de vente HT, quel est le prix de vente HT minimum (en €) ?",
                    "answerOptions": [
                        {"text": "4,00 € HT (2,00 € / (1 - 0,50)).", "isCorrect": False, "key": "A"},
                        {"text": "10,00 € HT (3,50 € / (1 - 0,65)).", "isCorrect": True, "key": "B"},
                        {"text": "2,00 € HT.", "isCorrect": False, "key": "C"},
                        {"text": "1,00 € HT.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 3,50 € / (1 - 0,65) = 3,50 € / 0,35 = 10,00 € HT. Le coût matière ne doit représenter que 35% du prix de vente."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle de la 'fiche technique' (fiche recette) dans la production de la boulangerie ?",
                    "answerOptions": [
                        {"text": "Garantir la constance de la qualité du produit, sa traçabilité et le calcul de son prix de revient (quantité et coût).", "isCorrect": True, "key": "A"},
                        {"text": "Déterminer la température de base de la pâte (T° de base) en fonction de la saison.", "isCorrect": False, "key": "B"},
                        {"text": "Mesurer la force de la farine (W) à l'alvéographe (test de qualité).", "isCorrect": False, "key": "C"},
                        {"text": "Vérifier la bonne exécution du nettoyage et l'absence de micro-organismes (HACCP).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La fiche technique (FTF) est le document de référence (norme de l'entreprise) pour la fabrication et la gestion (standardisation)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le mode de calcul qui permet de répartir les coûts (loyer, électricité) sur l'ensemble de la production (tous les pains et viennoiseries) ?",
                    "answerOptions": [
                        {"text": "Le calcul des charges indirectes (ou frais généraux), répartis par unité de production ou par heure de travail.", "isCorrect": True, "key": "A"},
                        {"text": "Le calcul du coût des matières premières (farine, eau, sel, levure) uniquement.", "isCorrect": False, "key": "B"},
                        {"text": "Le calcul du prix de vente HT uniquement.", "isCorrect": False, "key": "C"},
                        {"text": "Le calcul du taux de perte à la cuisson (évaporation de l'eau).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les charges indirectes (fixes) doivent être incluses dans le prix de revient (par un coefficient) pour ne pas être déficitaires."
                },
                {
                    "questionNumber": 96,
                    "question": "Si vous avez une production de 500 baguettes de 250 g et que la consommation moyenne de farine est de 0,15 kg par baguette, quelle quantité de farine faut-il commander ?",
                    "answerOptions": [
                        {"text": "75,0 kg de farine (500 baguettes x 0,15 kg/baguette).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'FIFO' (First In, First Out) : règle de gestion des stocks (le premier produit reçu est le premier vendu/utilisé) pour la DLC.", "isCorrect": True, "key": "B"},
                        {"text": "100,0 kg de farine.", "isCorrect": False, "key": "C"},
                        {"text": "50,0 kg de farine.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le FIFO est obligatoire pour les produits alimentaires (DLC) afin d'éviter la péremption (rupture de stock) et les pertes."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le but du 'poids net' (PN) d'un ingrédient dans la fiche technique ?",
                    "answerOptions": [
                        {"text": "Le poids de l'ingrédient tel qu'il est ajouté à la formule (sans les emballages, les déchets ou les impuretés).", "isCorrect": True, "key": "A"},
                        {"text": "Le prix de vente HT du produit fini (sans les taxes ni les charges).", "isCorrect": False, "key": "B"},
                        {"text": "Le coût total de la main d'œuvre (salaire + charges sociales) pour la production.", "isCorrect": False, "key": "C"},
                        {"text": "Le taux de perte à la cuisson (évaporation de l'eau) du produit fini.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le poids net est la base du calcul du coût des matières premières (uniquement le produit utilisé, pas la tare)."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le nom du coût qui varie directement en fonction de la quantité produite (farine, eau, levure, sel) ?",
                    "answerOptions": [
                        {"text": "Les charges variables (ou coûts directs) pour la production du pain.", "isCorrect": True, "key": "A"},
                        {"text": "Les charges fixes (loyer, assurance, électricité) qui ne changent pas avec la production.", "isCorrect": False, "key": "B"},
                        {"text": "Le coût de la main d'œuvre (ou coût salarial) pour la production.", "isCorrect": False, "key": "C"},
                        {"text": "Le prix de vente HT du produit fini (sans les taxes).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les charges variables (matières premières) sont directement liées à la quantité produite (si je fais plus, je dépense plus de matières)."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment s'appelle l'opération qui consiste à vérifier la force de la farine (W, P/L) à l'aide d'un appareil ?",
                    "answerOptions": [
                        {"text": "Le test d'alvéographe (test de qualité des farines) pour la détermination du réseau de gluten.", "isCorrect": False, "key": "A"},
                        {"text": "L'inventaire : le dénombrement (comptage) physique des stocks (matières premières et produits finis) pour ajuster les comptes.", "isCorrect": True, "key": "B"},
                        {"text": "Le test de DLC (Date Limite de Consommation) des produits périssables (pâtisseries).", "isCorrect": False, "key": "C"},
                        {"text": "Le test de température de la pâte (T° de base) en fin de pétrissage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'inventaire (souvent annuel) permet de valoriser les stocks et de calculer le coût réel (écart entre la théorie et la réalité)."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le taux de TVA (Taxe sur la Valeur Ajoutée) applicable aux pains et viennoiseries (produits alimentaires) en France ?",
                    "answerOptions": [
                        {"text": "Le taux réduit de 5,5% (ou 10% pour la consommation immédiate) pour les produits alimentaires (traiteur : 10% ou 20%).", "isCorrect": True, "key": "A"},
                        {"text": "Le taux normal de 20% (applicable aux pièces, aux fournitures et à la main d'œuvre non réduite).", "isCorrect": False, "key": "B"},
                        {"text": "Le taux standard de 10% (pour les travaux immobiliers ou les transports de voyageurs).", "isCorrect": False, "key": "C"},
                        {"text": "Le taux standard de 0% (exonération totale) pour les produits exportés à l'international.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les produits de charcuterie/traiteur sont souvent soumis au taux intermédiaire (10%) ou au taux normal (20%) en fonction du conditionnement et du type de produit (consommation immédiate ou non)."
                }
            ]
        }
    }
}