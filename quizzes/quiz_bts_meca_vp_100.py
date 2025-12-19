quiz_data = {
    "title": "Quiz BTS Maintenance des Véhicules (Option A) (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MOTORISATION THERMIQUE ET SYSTÈMES DE DÉPOLLUTION (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : MOTORISATION THERMIQUE ET SYSTÈMES DE DÉPOLLUTION",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est le rôle principal d'un intercooler dans un système de suralimentation ?",
                    "answerOptions": [
                        {"text": "Refroidir l'air d'admission", "isCorrect": True},
                        {"text": "Réchauffer l'essence", "isCorrect": False},
                        {"text": "Filtrer les impuretés", "isCorrect": False},
                        {"text": "Lubrifier le turbo", "isCorrect": False}
                    ],
                    "correction": "L'intercooler (échangeur air/air) refroidit l'air comprimé par le turbo pour augmenter sa densité, ce qui améliore le rendement de la combustion."
                },
                {
                    "questionNumber": 2,
                    "question": "Dans un cycle à quatre temps, quelle phase se produit lorsque le piston remonte et que les soupapes sont fermées ?",
                    "answerOptions": [
                        {"text": "Compression", "isCorrect": True},
                        {"text": "Admission", "isCorrect": False},
                        {"text": "Détente", "isCorrect": False},
                        {"text": "Échappement", "isCorrect": False}
                    ],
                    "correction": "Lors de la compression, le piston remonte du PMB vers le PMH avec les soupapes fermées pour comprimer le mélange."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel composant permet de réduire les NOx en réinjectant une partie des gaz d'échappement dans l'admission ?",
                    "answerOptions": [
                        {"text": "La vanne EGR", "isCorrect": True},
                        {"text": "Le débitmètre d'air", "isCorrect": False},
                        {"text": "La sonde Lambda", "isCorrect": False},
                        {"text": "Le catalyseur trois voies", "isCorrect": False}
                    ],
                    "correction": "La vanne EGR réintroduit des gaz inertes pour abaisser la température de combustion et réduire la formation d'oxydes d'azote."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la fonction d'une injection directe d'essence (GDI) ?",
                    "answerOptions": [
                        {"text": "Injecter le carburant directement dans la chambre", "isCorrect": True},
                        {"text": "Injecter dans le collecteur d'admission", "isCorrect": False},
                        {"text": "Réguler la pression d'huile", "isCorrect": False},
                        {"text": "Commander l'ouverture des soupapes", "isCorrect": False}
                    ],
                    "correction": "L'injection directe pulvérise l'essence directement dans le cylindre, permettant un dosage plus précis et une charge stratifiée."
                },
                {
                    "questionNumber": 5,
                    "question": "Sur un moteur Diesel, que signifie l'acronyme SCR ?",
                    "answerOptions": [
                        {"text": "Selective Catalytic Reduction", "isCorrect": True},
                        {"text": "Standard Cooling Radiator", "isCorrect": False},
                        {"text": "System Controlled Recharge", "isCorrect": False},
                        {"text": "Speed Control Regulator", "isCorrect": False}
                    ],
                    "correction": "Le SCR est un système de traitement des NOx utilisant l'AdBlue pour transformer les polluants en azote et en eau."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel capteur informe le calculateur de la position exacte du vilebrequin ?",
                    "answerOptions": [
                        {"text": "Le capteur PMH", "isCorrect": True},
                        {"text": "Le capteur cliquetis", "isCorrect": False},
                        {"text": "La sonde de température d'eau", "isCorrect": False},
                        {"text": "Le capteur de pression absolue", "isCorrect": False}
                    ],
                    "correction": "Le capteur PMH (Point Mort Haut) permet de synchroniser l'injection et l'allumage selon la position du vilebrequin."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est l'avantage d'un turbo à géométrie variable (TGV) ?",
                    "answerOptions": [
                        {"text": "Réduire le temps de réponse à bas régime", "isCorrect": True},
                        {"text": "Augmenter la consommation de carburant", "isCorrect": False},
                        {"text": "Supprimer le besoin d'huile de graissage", "isCorrect": False},
                        {"text": "Refroidir les gaz d'échappement", "isCorrect": False}
                    ],
                    "correction": "Les ailettes mobiles orientent les gaz pour optimiser la vitesse de turbine, même à bas régime (réduction du turbo-lag)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle sonde mesure la teneur en oxygène des gaz d'échappement ?",
                    "answerOptions": [
                        {"text": "Sonde Lambda", "isCorrect": True},
                        {"text": "Capteur MAF", "isCorrect": False},
                        {"text": "Capteur MAP", "isCorrect": False},
                        {"text": "Sonde CTN", "isCorrect": False}
                    ],
                    "correction": "La sonde Lambda permet au calculateur de réguler la richesse du mélange pour rester proche du rapport stoechiométrique (λ=1)."
                },
                {
                    "questionNumber": 9,
                    "question": "Qu'est-ce que le rapport volumétrique d'un moteur ?",
                    "answerOptions": [
                        {"text": "Le rapport entre volume total et volume résiduel", "isCorrect": True},
                        {"text": "Le poids du moteur divisé par sa cylindrée", "isCorrect": False},
                        {"text": "La pression d'huile divisée par le régime", "isCorrect": False},
                        {"text": "Le nombre de soupapes par cylindre", "isCorrect": False}
                    ],
                    "correction": "C'est le rapport (V+v)/v, mesurant le taux de compression théorique du mélange dans le cylindre."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel composant assure l'étanchéité entre la culasse et le bloc-cylindres ?",
                    "answerOptions": [
                        {"text": "Le joint de culasse", "isCorrect": True},
                        {"text": "Le joint spi de vilebrequin", "isCorrect": False},
                        {"text": "Le segment de feu", "isCorrect": False},
                        {"text": "Le joint de carter", "isCorrect": False}
                    ],
                    "correction": "Le joint de culasse sépare les chambres de combustion, les passages d'huile et le circuit de refroidissement."
                },
                {
                    "questionNumber": 11,
                    "question": "À quoi sert le système de calage variable des soupapes (VVT) ?",
                    "answerOptions": [
                        {"text": "Optimiser le remplissage des cylindres", "isCorrect": True},
                        {"text": "Augmenter la pression de suralimentation", "isCorrect": False},
                        {"text": "Réduire le bruit de l'échappement", "isCorrect": False},
                        {"text": "Limiter la vitesse maximale du véhicule", "isCorrect": False}
                    ],
                    "correction": "Le VVT modifie les instants d'ouverture et fermeture pour s'adapter au régime moteur et améliorer couple et consommation."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la fonction d'un filtre à particules (FAP) ?",
                    "answerOptions": [
                        {"text": "Piéger et brûler les suies de combustion", "isCorrect": True},
                        {"text": "Convertir le CO en CO2", "isCorrect": False},
                        {"text": "Refroidir le liquide de refroidissement", "isCorrect": False},
                        {"text": "Filtrer les vapeurs d'huile du carter", "isCorrect": False}
                    ],
                    "correction": "Le FAP retient les particules fines de carbone et déclenche des phases de régénération pour les éliminer."
                },
                {
                    "questionNumber": 13,
                    "question": "Dans une rampe commune (Common Rail), qui génère la haute pression ?",
                    "answerOptions": [
                        {"text": "La pompe HP entraînée par le moteur", "isCorrect": True},
                        {"text": "Le calculateur d'injection", "isCorrect": False},
                        {"text": "L'injecteur piézoélectrique", "isCorrect": False},
                        {"text": "La pompe de gavage", "isCorrect": False}
                    ],
                    "correction": "La pompe haute pression alimente l'accumulateur (rail) où le carburant est stocké sous pression constante."
                },
                {
                    "questionNumber": 14,
                    "question": "Comment le calculateur détecte-t-il une combustion anormale (cliquetis) ?",
                    "answerOptions": [
                        {"text": "Via un capteur piézo-électrique sur le bloc", "isCorrect": True},
                        {"text": "Via la sonde de température d'air", "isCorrect": False},
                        {"text": "Via le débitmètre massique", "isCorrect": False},
                        {"text": "Via le régime alternateur", "isCorrect": False}
                    ],
                    "correction": "Le capteur de cliquetis détecte les vibrations anormales provoquées par l'auto-inflammation pour ajuster l'avance à l'allumage."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est le rôle du catalyseur d'oxydation sur un moteur Diesel ?",
                    "answerOptions": [
                        {"text": "Traiter le CO et les Hydrocarbures (HC)", "isCorrect": True},
                        {"text": "Réduire les émissions de CO2", "isCorrect": False},
                        {"text": "Produire de l'ammoniac pour le SCR", "isCorrect": False},
                        {"text": "Supprimer les particules de suie", "isCorrect": False}
                    ],
                    "correction": "Le catalyseur d'oxydation transforme le monoxyde de carbone et les imbrûlés en substances moins nocives."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle pièce transforme le mouvement rectiligne des pistons en mouvement rotatif ?",
                    "answerOptions": [
                        {"text": "Le vilebrequin", "isCorrect": True},
                        {"text": "L'arbre à cames", "isCorrect": False},
                        {"text": "Le volant moteur", "isCorrect": False},
                        {"text": "La bielle", "isCorrect": False}
                    ],
                    "correction": "Le système bielle-manivelle articulé sur le vilebrequin assure cette transformation cinématique."
                },
                {
                    "questionNumber": 17,
                    "question": "Que signifie un mélange 'pauvre' ?",
                    "answerOptions": [
                        {"text": "Excès d'air par rapport au carburant", "isCorrect": True},
                        {"text": "Excès de carburant par rapport à l'air", "isCorrect": False},
                        {"text": "Mélange sans additif nettoyant", "isCorrect": False},
                        {"text": "Carburant de mauvaise qualité", "isCorrect": False}
                    ],
                    "correction": "Un mélange pauvre signifie que le rapport air/carburant est supérieur au rapport stoechiométrique."
                },
                {
                    "questionNumber": 18,
                    "question": "À quoi sert le reniflard moteur ?",
                    "answerOptions": [
                        {"text": "Recycler les vapeurs d'huile du carter", "isCorrect": True},
                        {"text": "Injecter de l'air frais dans l'échappement", "isCorrect": False},
                        {"text": "Refroidir le bas moteur", "isCorrect": False},
                        {"text": "Mesurer la pression de compression", "isCorrect": False}
                    ],
                    "correction": "Le système de réaspiration des gaz de carter évite les surpressions et pollutions en réinjectant les vapeurs dans l'admission."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'ordre d'allumage classique d'un moteur 4 cylindres en ligne ?",
                    "answerOptions": [
                        {"text": "1 - 3 - 4 - 2", "isCorrect": True},
                        {"text": "1 - 2 - 3 - 4", "isCorrect": False},
                        {"text": "4 - 3 - 2 - 1", "isCorrect": False},
                        {"text": "1 - 4 - 3 - 2", "isCorrect": False}
                    ],
                    "correction": "L'ordre 1-3-4-2 est le plus fréquent pour équilibrer les efforts sur le vilebrequin."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel dispositif régule la pression de suralimentation sur un turbo ?",
                    "answerOptions": [
                        {"text": "La Wastegate", "isCorrect": True},
                        {"text": "Le boîtier papillon", "isCorrect": False},
                        {"text": "L'injecteur de départ à froid", "isCorrect": False},
                        {"text": "Le thermostat", "isCorrect": False}
                    ],
                    "correction": "La soupape de décharge (Wastegate) dévie les gaz d'échappement pour limiter la vitesse de la turbine et donc la pression."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TRANSMISSION, LIAISON AU SOL ET FREINAGE (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TRANSMISSION, LIAISON AU SOL ET FREINAGE",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le rôle du différentiel dans un pont moteur ?",
                    "answerOptions": [
                        {"text": "Permettre aux roues de tourner à des vitesses différentes", "isCorrect": True},
                        {"text": "Multiplier le couple moteur de manière constante", "isCorrect": False},
                        {"text": "Inverser le sens de rotation pour la marche arrière", "isCorrect": False},
                        {"text": "Bloquer les roues lors du stationnement", "isCorrect": False}
                    ],
                    "correction": "En virage, la roue extérieure parcourt plus de distance ; le différentiel répartit la rotation selon la résistance."
                },
                {
                    "questionNumber": 22,
                    "question": "Dans une boîte de vitesses automatique à train épicycloïdal, comment change-t-on de rapport ?",
                    "answerOptions": [
                        {"text": "En bloquant certains éléments via des freins ou embrayages", "isCorrect": True},
                        {"text": "En déplaçant des baladeurs avec des fourchettes", "isCorrect": False},
                        {"text": "En faisant varier le diamètre des poulies", "isCorrect": False},
                        {"text": "En changeant la polarité du moteur électrique", "isCorrect": False}
                    ],
                    "correction": "Le pilotage hydraulique des récepteurs bloque le planétaire, le porte-satellite ou la couronne pour modifier le rapport."
                },
                {
                    "questionNumber": 23,
                    "question": "Que signifie un carrossage positif ?",
                    "answerOptions": [
                        {"text": "Le haut des roues pointe vers l'extérieur", "isCorrect": True},
                        {"text": "Les roues convergent vers l'avant", "isCorrect": False},
                        {"text": "L'axe de pivot est incliné vers l'arrière", "isCorrect": False},
                        {"text": "Le bas des roues est décalé vers la gauche", "isCorrect": False}
                    ],
                    "correction": "C'est l'angle formé par l'axe de la roue avec la verticale, vu de face."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est l'avantage majeur d'un système de freinage à disques ventilés ?",
                    "answerOptions": [
                        {"text": "Une meilleure dissipation de la chaleur", "isCorrect": True},
                        {"text": "Une réduction du bruit au freinage", "isCorrect": False},
                        {"text": "Une épaisseur de plaquette plus faible", "isCorrect": False},
                        {"text": "Un coût de fabrication moins élevé", "isCorrect": False}
                    ],
                    "correction": "Les canaux internes permettent la circulation d'air, limitant le 'fading' (perte d'efficacité par surchauffe)."
                },
                {
                    "questionNumber": 25,
                    "question": "Dans un système ESP, quel capteur informe sur la dérive réelle du véhicule ?",
                    "answerOptions": [
                        {"text": "Le capteur de lacet", "isCorrect": True},
                        {"text": "Le capteur d'angle volant", "isCorrect": False},
                        {"text": "Le capteur de vitesse roue", "isCorrect": False},
                        {"text": "Le manocontact de frein", "isCorrect": False}
                    ],
                    "correction": "Le gyroscope (capteur de lacet) mesure la rotation du véhicule autour de son axe vertical pour détecter un survirage ou sous-virage."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la fonction d'un convertisseur de couple ?",
                    "answerOptions": [
                        {"text": "Assurer la liaison hydraulique entre moteur et boîte", "isCorrect": True},
                        {"text": "Synchroniser les pignons de boîte manuelle", "isCorrect": False},
                        {"text": "Répartir le freinage entre l'avant et l'arrière", "isCorrect": False},
                        {"text": "Transformer le courant alternatif en continu", "isCorrect": False}
                    ],
                    "correction": "Il remplace l'embrayage dans les boîtes automatiques et permet de multiplier le couple au démarrage."
                },
                {
                    "questionNumber": 27,
                    "question": "Que provoque une usure en facettes sur la bande de roulement d'un pneu ?",
                    "answerOptions": [
                        {"text": "Des amortisseurs défaillants", "isCorrect": True},
                        {"text": "Un excès de pression de gonflage", "isCorrect": False},
                        {"text": "Un mauvais réglage du parallélisme", "isCorrect": False},
                        {"text": "Un déséquilibre statique de la roue", "isCorrect": False}
                    ],
                    "correction": "Les rebonds incessants de la roue mal freinée par l'amortisseur créent des zones d'usure irrégulières."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le rôle du Master Vac (servo-frein) ?",
                    "answerOptions": [
                        {"text": "Amplifier l'effort du conducteur sur la pédale", "isCorrect": True},
                        {"text": "Répartir la pression vers les roues arrière", "isCorrect": False},
                        {"text": "Réguler la pression pour éviter le blocage", "isCorrect": False},
                        {"text": "Actionner le frein de stationnement automatique", "isCorrect": False}
                    ],
                    "correction": "Il utilise la dépression (ou une pompe à vide) pour multiplier la force hydraulique envoyée au maître-cylindre."
                },
                {
                    "questionNumber": 29,
                    "question": "Qu'est-ce que l'angle de chasse ?",
                    "answerOptions": [
                        {"text": "L'inclinaison vers l'arrière de l'axe de pivot", "isCorrect": True},
                        {"text": "La convergence des roues avant", "isCorrect": False},
                        {"text": "Le déport de la roue par rapport au moyeu", "isCorrect": False},
                        {"text": "L'angle de braquage maximal", "isCorrect": False}
                    ],
                    "correction": "La chasse assure la stabilité directionnelle et le rappel du volant en ligne droite."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle est la particularité d'un joint homocinétique (cardan) ?",
                    "answerOptions": [
                        {"text": "Transmettre la rotation sans variation de vitesse", "isCorrect": True},
                        {"text": "Supporter le poids du véhicule en charge", "isCorrect": False},
                        {"text": "Filtrer les vibrations du moteur", "isCorrect": False},
                        {"text": "Réduire la vitesse de rotation des roues", "isCorrect": False}
                    ],
                    "correction": "Contrairement au joint de Cardan simple, il garantit une vitesse de sortie identique à la vitesse d'entrée quel que soit l'angle."
                },
                {
                    "questionNumber": 31,
                    "question": "Dans un système de freinage ABS, à quoi sert l'accumulateur basse pression ?",
                    "answerOptions": [
                        {"text": "Stocker le fluide lors de la phase de baisse de pression", "isCorrect": True},
                        {"text": "Maintenir la pression lors de l'arrêt moteur", "isCorrect": False},
                        {"text": "Alimenter l'embrayage hydraulique", "isCorrect": False},
                        {"text": "Filtrer les bulles d'air du circuit", "isCorrect": False}
                    ],
                    "correction": "Lorsqu'une roue bloque, l'électrovanne décharge la pression vers cet accumulateur tampon avant que la pompe de refoulement ne la renvoie."
                },
                {
                    "questionNumber": 32,
                    "question": "Sur une suspension pilotée, quel paramètre modifie-t-on pour durcir l'amortissement ?",
                    "answerOptions": [
                        {"text": "Le laminage de l'huile dans l'amortisseur", "isCorrect": True},
                        {"text": "La raideur du ressort métallique", "isCorrect": False},
                        {"text": "La pression des pneumatiques", "isCorrect": False},
                        {"text": "La longueur de la jambe de force", "isCorrect": False}
                    ],
                    "correction": "On réduit la section de passage de l'huile via des électrovannes pour freiner davantage le mouvement."
                },
                {
                    "questionNumber": 33,
                    "question": "Qu'est-ce que le pincement sur un train avant ?",
                    "answerOptions": [
                        {"text": "Les roues convergent vers l'avant", "isCorrect": True},
                        {"text": "Les roues divergent vers l'avant", "isCorrect": False},
                        {"text": "Les roues sont inclinées vers le moteur", "isCorrect": False},
                        {"text": "Les roues touchent la carrosserie en braquage", "isCorrect": False}
                    ],
                    "correction": "C'est la différence de distance entre l'avant et l'arrière des pneus d'un même essieu."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel composant relie la barre stabilisatrice au triangle de suspension ?",
                    "answerOptions": [
                        {"text": "La biellette de barre stabilisatrice", "isCorrect": True},
                        {"text": "La rotule de direction", "isCorrect": False},
                        {"text": "Le silentbloc moteur", "isCorrect": False},
                        {"text": "Le pivot de fusée", "isCorrect": False}
                    ],
                    "correction": "Elle transmet les efforts de torsion pour limiter le roulis du véhicule en virage."
                },
                {
                    "questionNumber": 35,
                    "question": "Dans une boîte de vitesses à double embrayage (DSG/DCT), quel est l'intérêt principal ?",
                    "answerOptions": [
                        {"text": "Passer les vitesses sans rupture de couple", "isCorrect": True},
                        {"text": "Réduire le poids de la transmission", "isCorrect": False},
                        {"text": "Supprimer totalement les pignons", "isCorrect": False},
                        {"text": "Augmenter la vitesse maximale", "isCorrect": False}
                    ],
                    "correction": "Pendant qu'un rapport est engagé sur un arbre, le suivant est déjà présélectionné sur le deuxième arbre."
                },
                {
                    "questionNumber": 36,
                    "question": "Comment appelle-t-on le dispositif qui limite le patinage d'une seule roue motrice ?",
                    "answerOptions": [
                        {"text": "L'antipatinage (ASR/TCS)", "isCorrect": True},
                        {"text": "L'antiblocage (ABS)", "isCorrect": False},
                        {"text": "Le répartiteur (REF)", "isCorrect": False},
                        {"text": "L'aide au freinage (AFU)", "isCorrect": False}
                    ],
                    "correction": "Il agit sur les freins ou le couple moteur pour redonner de l'adhérence à la roue qui patine."
                },
                {
                    "questionNumber": 37,
                    "question": "À quoi sert le répartiteur électronique de freinage (EBV/REF) ?",
                    "answerOptions": [
                        {"text": "Gérer la pression entre l'avant et l'arrière", "isCorrect": True},
                        {"text": "Multiplier la pression lors d'un choc", "isCorrect": False},
                        {"text": "Déclencher les warnings", "isCorrect": False},
                        {"text": "Vider le liquide de frein usagé", "isCorrect": False}
                    ],
                    "correction": "Il optimise le freinage arrière en fonction de la charge pour éviter le délessement du train arrière."
                },
                {
                    "questionNumber": 38,
                    "question": "Sur un pneumatique, que représente l'indice de charge (ex: 91) ?",
                    "answerOptions": [
                        {"text": "Le poids maximum supportable par le pneu", "isCorrect": True},
                        {"text": "La vitesse maximale autorisée", "isCorrect": False},
                        {"text": "La pression de gonflage à froid", "isCorrect": False},
                        {"text": "Le nombre de tresses métalliques", "isCorrect": False}
                    ],
                    "correction": "C'est un code numérique lié à une capacité de charge en kg selon un tableau de correspondance."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le rôle des butées à billes sur une suspension de type MacPherson ?",
                    "answerOptions": [
                        {"text": "Permettre la rotation de la jambe lors du braquage", "isCorrect": True},
                        {"text": "Lubrifier le ressort de suspension", "isCorrect": False},
                        {"text": "Bloquer la roue en cas de crevaison", "isCorrect": False},
                        {"text": "Régler la hauteur de caisse", "isCorrect": False}
                    ],
                    "correction": "Elles assurent la liaison pivot entre l'élément de suspension et la caisse."
                },
                {
                    "questionNumber": 40,
                    "question": "Si un véhicule tire à droite en ligne droite, quel angle est suspecté en premier ?",
                    "answerOptions": [
                        {"text": "Le parallélisme", "isCorrect": True},
                        {"text": "Le carrossage arrière", "isCorrect": False},
                        {"text": "L'angle d'inclinaison de pivot", "isCorrect": False},
                        {"text": "L'angle de braquage", "isCorrect": False}
                    ],
                    "correction": "Un défaut de parallélisme (ouverture ou pincement asymétrique) provoque une dérive directionnelle."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : ÉLECTRONIQUE EMBARQUÉE ET RÉSEAUX (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ÉLECTRONIQUE EMBARQUÉE ET RÉSEAUX",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Que signifie l'acronyme CAN dans un réseau multiplexé ?",
                    "answerOptions": [
                        {"text": "Controller Area Network", "isCorrect": True},
                        {"text": "Central Auxiliary Node", "isCorrect": False},
                        {"text": "Current Alternator Neutral", "isCorrect": False},
                        {"text": "Computer Active Network", "isCorrect": False}
                    ],
                    "correction": "C'est le bus de données standard permettant aux calculateurs de communiquer via deux fils entrelacés."
                },
                {
                    "questionNumber": 42,
                    "question": "Sur un bus CAN High Speed, quelle est la résistance de terminaison totale du réseau ?",
                    "answerOptions": [
                        {"text": "60 Ohms", "isCorrect": True},
                        {"text": "120 Ohms", "isCorrect": False},
                        {"text": "1000 Ohms", "isCorrect": False},
                        {"text": "0 Ohm", "isCorrect": False}
                    ],
                    "correction": "Le bus possède deux résistances de 120 Ohms en parallèle aux extrémités, soit 60 Ohms au total."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la tension moyenne sur le fil CAN-H d'un bus CAN HS en cours de communication ?",
                    "answerOptions": [
                        {"text": "2,5V à 3,5V", "isCorrect": True},
                        {"text": "0V à 12V", "isCorrect": False},
                        {"text": "5V à 10V", "isCorrect": False},
                        {"text": "12V à 14V", "isCorrect": False}
                    ],
                    "correction": "Au repos, les deux fils sont à 2,5V. En état dominant, CAN-H monte vers 3,5V et CAN-L descend vers 1,5V."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel protocole est généralement utilisé pour les fonctions de carrosserie lentes (rétroviseurs, lève-vitres) ?",
                    "answerOptions": [
                        {"text": "LIN", "isCorrect": True},
                        {"text": "CAN HS", "isCorrect": False},
                        {"text": "FlexRay", "isCorrect": False},
                        {"text": "MOST", "isCorrect": False}
                    ],
                    "correction": "Le bus LIN est un réseau mono-filaire économique pour des applications simples."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment s'appelle l'outil de mesure permettant de visualiser la forme d'un signal électrique ?",
                    "answerOptions": [
                        {"text": "L'oscilloscope", "isCorrect": True},
                        {"text": "Le multimètre", "isCorrect": False},
                        {"text": "La lampe témoin", "isCorrect": False},
                        {"text": "L'ohmmètre", "isCorrect": False}
                    ],
                    "correction": "L'oscilloscope permet d'analyser la tension en fonction du temps, indispensable pour les signaux rapides."
                },
                {
                    "questionNumber": 46,
                    "question": "Dans un signal PWM (RCO), que fait varier le calculateur pour modifier la puissance envoyée ?",
                    "answerOptions": [
                        {"text": "Le rapport cyclique (temps d'ouverture)", "isCorrect": True},
                        {"text": "La tension de crête", "isCorrect": False},
                        {"text": "La fréquence du signal", "isCorrect": False},
                        {"text": "La résistance du composant", "isCorrect": False}
                    ],
                    "correction": "Le Rapport Cyclique d'Ouverture (RCO) fait varier la durée du signal à l'état haut sur une période fixe."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le rôle d'un capteur à effet Hall ?",
                    "answerOptions": [
                        {"text": "Mesurer une vitesse ou position magnétique", "isCorrect": True},
                        {"text": "Mesurer la pression de l'huile", "isCorrect": False},
                        {"text": "Mesurer la température des gaz", "isCorrect": False},
                        {"text": "Mesurer la luminosité ambiante", "isCorrect": False}
                    ],
                    "correction": "Il délivre un signal carré en fonction du passage d'un champ magnétique, idéal pour le régime moteur ou la vitesse roue."
                },
                {
                    "questionNumber": 48,
                    "question": "À quoi sert la passerelle (Gateway) dans un véhicule moderne ?",
                    "answerOptions": [
                        {"text": "Faire communiquer différents réseaux entre eux", "isCorrect": True},
                        {"text": "Recharger la batterie de traction", "isCorrect": False},
                        {"text": "Convertir le courant alternatif", "isCorrect": False},
                        {"text": "Mesurer le débit de carburant", "isCorrect": False}
                    ],
                    "correction": "Elle assure le transfert de données entre les différents types de bus (CAN, LIN, FlexRay)."
                },
                {
                    "questionNumber": 49,
                    "question": "Que signifie un code défaut commençant par 'P0' lors d'un diagnostic OBD ?",
                    "answerOptions": [
                        {"text": "Défaut standardisé sur le groupe motopropulseur", "isCorrect": True},
                        {"text": "Défaut propriétaire sur le châssis", "isCorrect": False},
                        {"text": "Défaut de communication réseau", "isCorrect": False},
                        {"text": "Défaut d'équipement de confort", "isCorrect": False}
                    ],
                    "correction": "P pour Powertrain, 0 pour code standard ISO/SAE."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle est la tension de référence (V-Ref) fournie par un calculateur à la plupart des capteurs ?",
                    "answerOptions": [
                        {"text": "5 Volts", "isCorrect": True},
                        {"text": "12 Volts", "isCorrect": False},
                        {"text": "3,3 Volts", "isCorrect": False},
                        {"text": "1 Volt", "isCorrect": False}
                    ],
                    "correction": "Les calculateurs fournissent une tension stabilisée de 5V pour alimenter les capteurs résistifs ou Hall."
                },
                {
                    "questionNumber": 51,
                    "question": "Comment vérifie-t-on l'isolement d'un fil par rapport à la masse ?",
                    "answerOptions": [
                        {"text": "Mesurer la résistance entre le fil et la carrosserie", "isCorrect": True},
                        {"text": "Mesurer la tension aux bornes de la batterie", "isCorrect": False},
                        {"text": "Mesurer la continuité entre les deux bouts du fil", "isCorrect": False},
                        {"text": "Utiliser une pince ampèremétrique", "isCorrect": False}
                    ],
                    "correction": "On doit trouver une résistance infinie (OL) ; une valeur indique une fuite."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel réseau utilise la fibre optique pour le transfert de données multimédia ?",
                    "answerOptions": [
                        {"text": "MOST", "isCorrect": True},
                        {"text": "LIN", "isCorrect": False},
                        {"text": "CAN", "isCorrect": False},
                        {"text": "Bluetooth", "isCorrect": False}
                    ],
                    "correction": "Le bus MOST permet de très hauts débits pour l'audio et la vidéo."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la particularité d'un capteur de température de type CTN ?",
                    "answerOptions": [
                        {"text": "Sa résistance diminue quand la température augmente", "isCorrect": True},
                        {"text": "Sa résistance augmente quand la température augmente", "isCorrect": False},
                        {"text": "Il produit sa propre tension électrique", "isCorrect": False},
                        {"text": "Il nécessite un faisceau en fibre optique", "isCorrect": False}
                    ],
                    "correction": "Coefficient de Température Négatif (couramment utilisé pour l'eau ou l'air)."
                },
                {
                    "questionNumber": 54,
                    "question": "Sur un schéma électrique, que signifie la mention '30' selon la norme DIN ?",
                    "answerOptions": [
                        {"text": "Alimentation positive permanente", "isCorrect": True},
                        {"text": "Alimentation après contact (APC)", "isCorrect": False},
                        {"text": "Masse (négatif batterie)", "isCorrect": False},
                        {"text": "Commande de démarreur", "isCorrect": False}
                    ],
                    "correction": "La borne 30 est le + avant contact."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le but de la 'Freeze Frame Data' (Données figées) lors d'un défaut ?",
                    "answerOptions": [
                        {"text": "Enregistrer les conditions moteur au moment de la panne", "isCorrect": True},
                        {"text": "Bloquer le régime moteur pour protéger la mécanique", "isCorrect": False},
                        {"text": "Empêcher l'effacement des codes défauts", "isCorrect": False},
                        {"text": "Refroidir le calculateur par injection de gaz", "isCorrect": False}
                    ],
                    "correction": "Elle permet de savoir si le défaut est apparu à froid, en charge, ou à haute vitesse."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'avantage du réseau FlexRay ?",
                    "answerOptions": [
                        {"text": "Débit très élevé et déterminisme (sécurité)", "isCorrect": True},
                        {"text": "Utilisation d'un seul fil de fer", "isCorrect": False},
                        {"text": "Absence totale de calculateurs", "isCorrect": False},
                        {"text": "Compatibilité avec l'essence sans plomb", "isCorrect": False}
                    ],
                    "correction": "Utilisé pour le 'X-by-wire' (direction/freinage) car il est ultra-rapide et fiable."
                },
                {
                    "questionNumber": 57,
                    "question": "Dans un système d'allumage jumo-statique, combien y a-t-il de bobines pour 4 cylindres ?",
                    "answerOptions": [
                        {"text": "2 bobines", "isCorrect": True},
                        {"text": "4 bobines", "isCorrect": False},
                        {"text": "1 bobine centrale", "isCorrect": False},
                        {"text": "8 bobines", "isCorrect": False}
                    ],
                    "correction": "Une bobine alimente deux bougies simultanément (étincelle perdue)."
                },
                {
                    "questionNumber": 58,
                    "question": "À quoi sert un shunt sur un circuit électrique lors d'une mesure ?",
                    "answerOptions": [
                        {"text": "Mesurer une intensité par dérivation", "isCorrect": True},
                        {"text": "Augmenter la tension du circuit", "isCorrect": False},
                        {"text": "Isoler le circuit de la batterie", "isCorrect": False},
                        {"text": "Remplacer un fusible de forte puissance", "isCorrect": False}
                    ],
                    "correction": "C'est une résistance de précision de faible valeur permettant de mesurer le courant qui la traverse."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le rôle du 'Watchdog' dans un calculateur ?",
                    "answerOptions": [
                        {"text": "Surveiller le bon fonctionnement du microprocesseur", "isCorrect": True},
                        {"text": "Déclencher l'alarme antivol", "isCorrect": False},
                        {"text": "Gérer la climatisation à distance", "isCorrect": False},
                        {"text": "Vérifier la pression des pneus", "isCorrect": False}
                    ],
                    "correction": "C'est un dispositif de sécurité qui réinitialise le système en cas de plantage logiciel."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel type de diode laisse passer le courant dans un seul sens ?",
                    "answerOptions": [
                        {"text": "Diode de redressement", "isCorrect": True},
                        {"text": "Diode Zener", "isCorrect": False},
                        {"text": "Diode LED", "isCorrect": False},
                        {"text": "Photodiode", "isCorrect": False}
                    ],
                    "correction": "C'est la fonction de base de la diode (clapet anti-retour électrique)."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : VÉHICULES ÉLECTRIQUES ET HYBRIDES (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : VÉHICULES ÉLECTRIQUES ET HYBRIDES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel élément permet de convertir le courant continu (DC) de la batterie en alternatif (AC) pour le moteur ?",
                    "answerOptions": [
                        {"text": "L'onduleur (Inverter)", "isCorrect": True},
                        {"text": "Le convertisseur DC/DC", "isCorrect": False},
                        {"text": "Le chargeur embarqué", "isCorrect": False},
                        {"text": "Le pont de diodes", "isCorrect": False}
                    ],
                    "correction": "L'onduleur pilote les phases du moteur électrique en hachant le courant continu."
                },
                {
                    "questionNumber": 62,
                    "question": "À quoi sert le convertisseur DC/DC dans un véhicule électrique ?",
                    "answerOptions": [
                        {"text": "Alimenter le réseau 12V depuis la batterie HT", "isCorrect": True},
                        {"text": "Recharger la batterie de traction sur une borne", "isCorrect": False},
                        {"text": "Changer le sens de marche du véhicule", "isCorrect": False},
                        {"text": "Réguler la température de l'habitacle", "isCorrect": False}
                    ],
                    "correction": "Il remplace l'alternateur classique pour fournir l'énergie aux accessoires (phares, radio, etc.)."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la couleur réglementaire des câbles haute tension ?",
                    "answerOptions": [
                        {"text": "Orange", "isCorrect": True},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Bleu", "isCorrect": False}
                    ],
                    "correction": "La couleur orange signale un danger de mort (tension supérieure à 60V DC ou 30V AC)."
                },
                {
                    "questionNumber": 64,
                    "question": "Sur un véhicule hybride, qu'est-ce que le 'freinage régénératif' ?",
                    "answerOptions": [
                        {"text": "L'utilisation du moteur comme générateur pour charger la batterie", "isCorrect": True},
                        {"text": "Un système qui change les plaquettes automatiquement", "isCorrect": False},
                        {"text": "L'ajout de liquide de frein pendant le roulage", "isCorrect": False},
                        {"text": "L'arrêt du moteur thermique à chaque feu rouge", "isCorrect": False}
                    ],
                    "correction": "L'énergie cinétique est convertie en électricité lors de la décélération."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel type de moteur électrique est le plus courant pour la traction automobile ?",
                    "answerOptions": [
                        {"text": "Synchrone à aimants permanents", "isCorrect": True},
                        {"text": "Asynchrone à cage d'écureuil", "isCorrect": False},
                        {"text": "À courant continu et balais", "isCorrect": False},
                        {"text": "Pas à pas de forte puissance", "isCorrect": False}
                    ],
                    "correction": "Il offre le meilleur rendement et une compacité optimale."
                },
                {
                    "questionNumber": 66,
                    "question": "Que signifie l'acronyme BMS ?",
                    "answerOptions": [
                        {"text": "Battery Management System", "isCorrect": True},
                        {"text": "Brake Modulation System", "isCorrect": False},
                        {"text": "Body Monitoring Sensor", "isCorrect": False},
                        {"text": "Base Main Service", "isCorrect": False}
                    ],
                    "correction": "Le BMS surveille la tension des cellules, la température et gère l'équilibrage de la batterie."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle habilitation est nécessaire pour consigner un véhicule électrique ?",
                    "answerOptions": [
                        {"text": "B2VL", "isCorrect": True},
                        {"text": "B1VL", "isCorrect": False},
                        {"text": "B0L", "isCorrect": False},
                        {"text": "BEL", "isCorrect": False}
                    ],
                    "correction": "B2VL (Chargé de travaux) permet de réaliser la mise hors tension complète du système HT."
                },
                {
                    "questionNumber": 68,
                    "question": "À quoi sert la 'boucle d'interlock' ?",
                    "answerOptions": [
                        {"text": "Couper la HT en cas d'ouverture d'un connecteur", "isCorrect": True},
                        {"text": "Verrouiller les portières en roulant", "isCorrect": False},
                        {"text": "Empêcher le vol du câble de recharge", "isCorrect": False},
                        {"text": "Serrer le frein de parking automatiquement", "isCorrect": False}
                    ],
                    "correction": "C'est un circuit de sécurité basse tension qui parcourt tous les composants HT."
                },
                {
                    "questionNumber": 69,
                    "question": "Dans une batterie Lithium-Ion, comment sont branchées les cellules pour augmenter la tension ?",
                    "answerOptions": [
                        {"text": "En série", "isCorrect": True},
                        {"text": "En parallèle", "isCorrect": False},
                        {"text": "En étoile", "isCorrect": False},
                        {"text": "En dérivation", "isCorrect": False}
                    ],
                    "correction": "Le montage en série additionne les tensions unitaires (ex: 3,7V x 100 = 370V)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le rôle du 'Service Plug' (ou sectionneur de maintenance) ?",
                    "answerOptions": [
                        {"text": "Ouvrir physiquement le circuit de puissance de la batterie", "isCorrect": True},
                        {"text": "Brancher la valise de diagnostic", "isCorrect": False},
                        {"text": "Démarrer le véhicule avec des pinces", "isCorrect": False},
                        {"text": "Réinitialiser l'indicateur de maintenance", "isCorrect": False}
                    ],
                    "correction": "Il permet de séparer la batterie en deux blocs pour travailler en sécurité."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment appelle-t-on un véhicule hybride que l'on peut brancher sur une prise ?",
                    "answerOptions": [
                        {"text": "PHEV", "isCorrect": True},
                        {"text": "HEV", "isCorrect": False},
                        {"text": "MHEV", "isCorrect": False},
                        {"text": "BEV", "isCorrect": False}
                    ],
                    "correction": "Plug-in Hybrid Electric Vehicle (Hybride Rechargeable)."
                },
                {
                    "questionNumber": 72,
                    "question": "Pourquoi la climatisation des véhicules électriques utilise-t-elle souvent un compresseur électrique ?",
                    "answerOptions": [
                        {"text": "Pour fonctionner moteur thermique à l'arrêt", "isCorrect": True},
                        {"text": "Pour consommer plus d'énergie", "isCorrect": False},
                        {"text": "Pour simplifier le circuit d'air", "isCorrect": False},
                        {"text": "Pour supprimer le fluide frigorigène", "isCorrect": False}
                    ],
                    "correction": "Le compresseur est alimenté par la batterie HT et piloté par un onduleur interne."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la fonction d'une pompe à chaleur (PAC) sur une voiture électrique ?",
                    "answerOptions": [
                        {"text": "Chauffer l'habitacle avec un meilleur rendement qu'une résistance", "isCorrect": True},
                        {"text": "Pomper l'huile moteur vers le turbo", "isCorrect": False},
                        {"text": "Augmenter la pression de l'eau de refroidissement", "isCorrect": False},
                        {"text": "Aspirer les gaz d'échappement", "isCorrect": False}
                    ],
                    "correction": "Elle préserve l'autonomie en hiver en récupérant des calories extérieures."
                },
                {
                    "questionNumber": 74,
                    "question": "Qu'est-ce que le 'SoC' (State of Charge) ?",
                    "answerOptions": [
                        {"text": "Le niveau de charge restant en pourcentage", "isCorrect": True},
                        {"text": "La santé globale de la batterie", "isCorrect": False},
                        {"text": "La température de fonctionnement", "isCorrect": False},
                        {"text": "La vitesse de recharge maximum", "isCorrect": False}
                    ],
                    "correction": "Il correspond à la 'jauge à carburant' électrique."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le risque majeur lors d'un choc violent sur une batterie Lithium-Ion ?",
                    "answerOptions": [
                        {"text": "L'emballement thermique (Thermal Runaway)", "isCorrect": True},
                        {"text": "La congélation immédiate du pack", "isCorrect": False},
                        {"text": "La transformation du lithium en gaz inerte", "isCorrect": False},
                        {"text": "L'augmentation de l'autonomie", "isCorrect": False}
                    ],
                    "correction": "Un court-circuit interne peut déclencher une réaction chimique exothermique incontrôlable."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment le moteur électrique est-il refroidi ?",
                    "answerOptions": [
                        {"text": "Par un circuit d'eau avec radiateur ou par air", "isCorrect": True},
                        {"text": "Uniquement par l'huile de transmission", "isCorrect": False},
                        {"text": "Il n'a pas besoin de refroidissement", "isCorrect": False},
                        {"text": "Par des ventilateurs internes 12V", "isCorrect": False}
                    ],
                    "correction": "L'onduleur et le moteur ont généralement un circuit de liquide dédié."
                },
                {
                    "questionNumber": 77,
                    "question": "Qu'est-ce que le 'SoH' (State of Health) ?",
                    "answerOptions": [
                        {"text": "L'état de santé (usure) de la batterie", "isCorrect": True},
                        {"text": "Le temps restant avant la fin de charge", "isCorrect": False},
                        {"text": "La pression dans les cellules", "isCorrect": False},
                        {"text": "L'altitude maximale supportée", "isCorrect": False}
                    ],
                    "correction": "Il compare la capacité réelle actuelle à la capacité d'origine."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle précaution prendre avant de débrancher un connecteur HT ?",
                    "answerOptions": [
                        {"text": "Vérifier l'absence de tension (VAT)", "isCorrect": True},
                        {"text": "Mettre des lunettes de soleil", "isCorrect": False},
                        {"text": "Démarrer le moteur", "isCorrect": False},
                        {"text": "Pulvériser du dégrippant", "isCorrect": False}
                    ],
                    "correction": "La VAT est l'étape finale obligatoire de la consignation."
                },
                {
                    "questionNumber": 79,
                    "question": "À quoi servent les contacteurs principaux dans le pack batterie ?",
                    "answerOptions": [
                        {"text": "Isoler la batterie du véhicule à l'arrêt", "isCorrect": True},
                        {"text": "Changer le rapport de vitesse", "isCorrect": False},
                        {"text": "Mesurer le courant de charge", "isCorrect": False},
                        {"text": "Allumer les feux stop lors du freinage", "isCorrect": False}
                    ],
                    "correction": "Ils sont pilotés par le calculateur pour autoriser ou couper la puissance."
                },
                {
                    "questionNumber": 80,
                    "question": "Dans un système hybride Toyota (HSD), quel est le rôle du train épicycloïdal ?",
                    "answerOptions": [
                        {"text": "Répartir les flux d'énergie entre moteurs et roues", "isCorrect": True},
                        {"text": "Remplacer les freins à disques", "isCorrect": False},
                        {"text": "Synchroniser les arbres de roues", "isCorrect": False},
                        {"text": "Convertir le courant AC en DC", "isCorrect": False}
                    ],
                    "correction": "Il agit comme un répartiteur de puissance (Power Split Device)."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : GESTION D'ATELIER, ORGANISATION ET RÉGLEMENTATION (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : GESTION D'ATELIER, ORGANISATION ET RÉGLEMENTATION",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel document contractuel lie le garage au client pour les travaux ?",
                    "answerOptions": [
                        {"text": "L'ordre de réparation (OR)", "isCorrect": True},
                        {"text": "Le devis estimatif", "isCorrect": False},
                        {"text": "La facture finale", "isCorrect": False},
                        {"text": "La carte grise", "isCorrect": False}
                    ],
                    "correction": "L'OR définit la mission du garagiste et constitue une preuve juridique en cas de litige."
                },
                {
                    "questionNumber": 82,
                    "question": "Qu'est-ce qu'une 'obligation de résultat' pour un garagiste ?",
                    "answerOptions": [
                        {"text": "Le véhicule doit être rendu parfaitement réparé", "isCorrect": True},
                        {"text": "Le garage doit seulement essayer de réparer", "isCorrect": False},
                        {"text": "Le client doit payer même si ça ne marche pas", "isCorrect": False},
                        {"text": "Le mécanicien doit travailler vite", "isCorrect": False}
                    ],
                    "correction": "Le garagiste est présumé responsable si la panne persiste après son intervention."
                },
                {
                    "questionNumber": 83,
                    "question": "À quoi sert un barème de temps constructeur ?",
                    "answerOptions": [
                        {"text": "Facturer la main-d'œuvre selon une durée prédéfinie", "isCorrect": True},
                        {"text": "Mesurer la vitesse de rotation des roues", "isCorrect": False},
                        {"text": "Connaître l'heure de fermeture de l'usine", "isCorrect": False},
                        {"text": "Calculer la durée de vie des pneus", "isCorrect": False}
                    ],
                    "correction": "Il garantit une facturation équitable basée sur une étude de temps réelle pour chaque opération."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment calcule-t-on le taux de productivité d'un mécanicien ?",
                    "answerOptions": [
                        {"text": "Heures produites / Heures présentielles", "isCorrect": True},
                        {"text": "Chiffre d'affaires / Nombre de pièces", "isCorrect": False},
                        {"text": "Nombre de pannes / Nombre de jours", "isCorrect": False},
                        {"text": "Heures de pause / Heures travaillées", "isCorrect": False}
                    ],
                    "correction": "Il mesure l'efficacité de l'atelier par rapport au temps passé."
                },
                {
                    "questionNumber": 85,
                    "question": "Dans une analyse de risque, que signifie 'P x G' ?",
                    "answerOptions": [
                        {"text": "Probabilité x Gravité", "isCorrect": True},
                        {"text": "Pression x Gaz", "isCorrect": False},
                        {"text": "Poids x Glissement", "isCorrect": False},
                        {"text": "Prix x Garantie", "isCorrect": False}
                    ],
                    "correction": "C'est la formule classique pour évaluer la criticité d'un risque professionnel."
                },
                {
                    "questionNumber": 86,
                    "question": "Que doit-on faire des huiles usagées collectées au garage ?",
                    "answerOptions": [
                        {"text": "Les confier à un collecteur agréé", "isCorrect": True},
                        {"text": "Les brûler dans la chaudière de l'atelier", "isCorrect": False},
                        {"text": "Les jeter à l'égout avec précaution", "isCorrect": False},
                        {"text": "Les mélanger avec les ordures ménagères", "isCorrect": False}
                    ],
                    "correction": "Le recyclage des huiles est une obligation légale strictement contrôlée."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la fonction d'un réceptionnaire en après-vente ?",
                    "answerOptions": [
                        {"text": "Faire l'interface entre le client et l'atelier", "isCorrect": True},
                        {"text": "Réparer les moteurs complexes", "isCorrect": False},
                        {"text": "Nettoyer les sols du garage", "isCorrect": False},
                        {"text": "Conduire le camion de livraison", "isCorrect": False}
                    ],
                    "correction": "Il accueille le client, établit l'OR et restitue le véhicule."
                },
                {
                    "questionNumber": 88,
                    "question": "Que signifie le marquage 'CE' sur une machine de garage ?",
                    "answerOptions": [
                        {"text": "Conformité Européenne (normes de sécurité)", "isCorrect": True},
                        {"text": "Câblage Électrique", "isCorrect": False},
                        {"text": "Charge Élevée", "isCorrect": False},
                        {"text": "Contrôle Extérieur", "isCorrect": False}
                    ],
                    "correction": "Il atteste que l'équipement respecte les exigences de sécurité communautaires."
                },
                {
                    "questionNumber": 89,
                    "question": "À quoi sert une 'Fiche de Données de Sécurité' (FDS) ?",
                    "answerOptions": [
                        {"text": "Informer sur les risques chimiques d'un produit", "isCorrect": True},
                        {"text": "Noter les scores des crash-tests", "isCorrect": False},
                        {"text": "Vérifier le solde bancaire de l'entreprise", "isCorrect": False},
                        {"text": "Calculer les remises clients", "isCorrect": False}
                    ],
                    "correction": "Elle détaille les dangers, le stockage et les mesures d'urgence pour chaque produit dangereux."
                },
                {
                    "questionNumber": 90,
                    "question": "Qu'est-ce qu'une 'Campagne de rappel' constructeur ?",
                    "answerOptions": [
                        {"text": "Une mise en conformité gratuite pour un défaut de série", "isCorrect": True},
                        {"text": "Un appel téléphonique pour vendre un nouveau modèle", "isCorrect": False},
                        {"text": "Une procédure pour récupérer les voitures volées", "isCorrect": False},
                        {"text": "Un stage de conduite pour les clients", "isCorrect": False}
                    ],
                    "correction": "Le constructeur prend en charge la réparation d'un organe défectueux pour des raisons de sécurité ou de fiabilité."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel gaz est interdit dans les circuits de climatisation des véhicules neufs actuels ?",
                    "answerOptions": [
                        {"text": "R134a", "isCorrect": True},
                        {"text": "R1234yf", "isCorrect": False},
                        {"text": "Azote", "isCorrect": False},
                        {"text": "Argon", "isCorrect": False}
                    ],
                    "correction": "Le R134a est progressivement remplacé par le R1234yf car son potentiel de réchauffement planétaire est trop élevé."
                },
                {
                    "questionNumber": 92,
                    "question": "En cas d'accident du travail, dans quel délai l'employeur doit-il le déclarer ?",
                    "answerOptions": [
                        {"text": "48 heures", "isCorrect": True},
                        {"text": "1 mois", "isCorrect": False},
                        {"text": "15 jours", "isCorrect": False},
                        {"text": "Immédiatement (dans l'heure)", "isCorrect": False}
                    ],
                    "correction": "La déclaration à la CPAM doit se faire sous 48h (hors dimanches et jours fériés)."
                },
                {
                    "questionNumber": 93,
                    "question": "À quoi sert le 'système de management de la qualité' (ISO 9001) ?",
                    "answerOptions": [
                        {"text": "Améliorer la satisfaction client et les processus", "isCorrect": True},
                        {"text": "Payer moins d'impôts sur les bénéfices", "isCorrect": False},
                        {"text": "Rendre le garage obligatoire pour les clients", "isCorrect": False},
                        {"text": "Augmenter le prix des voitures neuves", "isCorrect": False}
                    ],
                    "correction": "Il vise l'amélioration continue des prestations et de l'organisation."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle du médecin du travail ?",
                    "answerOptions": [
                        {"text": "Vérifier l'aptitude au poste et conseiller sur la prévention", "isCorrect": True},
                        {"text": "Soigner les grippes des salariés", "isCorrect": False},
                        {"text": "Contrôler les arrêts maladie abusifs", "isCorrect": False},
                        {"text": "Réparer les blessures de chantier", "isCorrect": False}
                    ],
                    "correction": "Il joue un rôle préventif pour la santé des travailleurs."
                },
                {
                    "questionNumber": 95,
                    "question": "Qu'est-ce qu'une 'VGP' sur un pont élévateur ?",
                    "answerOptions": [
                        {"text": "Vérification Générale Périodique", "isCorrect": True},
                        {"text": "Vitesse Globale de Pression", "isCorrect": False},
                        {"text": "Volume de Graissage Principal", "isCorrect": False},
                        {"text": "Valve de Gaz de Protection", "isCorrect": False}
                    ],
                    "correction": "Le contrôle de sécurité obligatoire tous les ans pour les appareils de levage."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment appelle-t-on le recyclage des gaz de carter ?",
                    "answerOptions": [
                        {"text": "PCV (Positive Crankcase Ventilation)", "isCorrect": True},
                        {"text": "EGR", "isCorrect": False},
                        {"text": "SCR", "isCorrect": False},
                        {"text": "OBD", "isCorrect": False}
                    ],
                    "correction": "Il s'agit du recyclage des vapeurs d'huile via le reniflard."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel document liste les équipements de protection obligatoires pour un poste ?",
                    "answerOptions": [
                        {"text": "La fiche de poste", "isCorrect": True},
                        {"text": "La facture EDF", "isCorrect": False},
                        {"text": "Le manuel du conducteur", "isCorrect": False},
                        {"text": "Le bail commercial", "isCorrect": False}
                    ],
                    "correction": "Elle précise les tâches et les mesures de protection associées."
                },
                {
                    "questionNumber": 98,
                    "question": "Qu'est-ce qu'une 'masse flottante' en électricité ?",
                    "answerOptions": [
                        {"text": "Une masse mal reliée créant une résistance parasite", "isCorrect": True},
                        {"text": "Une masse qui n'est pas reliée à la carrosserie", "isCorrect": False},
                        {"text": "Un câble de masse qui pend sous le véhicule", "isCorrect": False},
                        {"text": "Une absence totale de batterie dans le véhicule", "isCorrect": False}
                    ],
                    "correction": "Une mauvaise masse perturbe les signaux des capteurs et les calculateurs (Loi d'Ohm)."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel document permet de suivre le cheminement précis du courant fil par fil ?",
                    "answerOptions": [
                        {"text": "Le schéma de câblage électrique", "isCorrect": True},
                        {"text": "La vue éclatée des pièces", "isCorrect": False},
                        {"text": "Le barème de temps", "isCorrect": False},
                        {"text": "Le plan d'entretien", "isCorrect": False}
                    ],
                    "correction": "Le schéma électrique détaille les connecteurs et les numéros de broches."
                },
                {
                    "questionNumber": 100,
                    "question": "Dans une analyse des risques, qu'est-ce que la 'Prévention intrinsèque' ?",
                    "answerOptions": [
                        {"text": "Supprimer le danger dès la conception de l'outil", "isCorrect": True},
                        {"text": "Mettre des panneaux de signalisation", "isCorrect": False},
                        {"text": "Former le personnel", "isCorrect": False},
                        {"text": "Distribuer des EPI", "isCorrect": False}
                    ],
                    "correction": "C'est le niveau le plus efficace de prévention (suppression de la cause du risque)."
                }
            ]
        }
    }
}