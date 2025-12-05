# Fichier : quiz_cap_meca_vp_100.py

quiz_data = {
    "title": "Quiz CAP Maintenance des Véhicules (VP) : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MOTEUR THERMIQUE ET PÉRIPHÉRIQUES (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Moteur Thermique et Périphériques (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Dans un moteur à quatre temps, quel est l'ordre chronologique des phases du cycle ?",
                    "answerOptions": [
                        {"text": "Compression, Admission, Échappement, Détente.", "isCorrect": False},
                        {"text": "Admission, Compression, Détente, Échappement.", "isCorrect": True},
                        {"text": "Détente, Échappement, Admission, Compression.", "isCorrect": False},
                        {"text": "Échappement, Détente, Compression, Admission.", "isCorrect": False}
                    ],
                    "correction": "Le cycle d'un moteur thermique est : **Admission** du mélange, **Compression** du mélange, **Détente** (explosion) qui produit la puissance, et **Échappement** des gaz brûlés."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le rôle principal du turbocompresseur ?",
                    "answerOptions": [
                        {"text": "Refroidir l'huile moteur.", "isCorrect": False},
                        {"text": "Augmenter la pression des gaz d'échappement.", "isCorrect": False},
                        {"text": "Augmenter la quantité d'air admise dans les cylindres pour améliorer la puissance.", "isCorrect": True},
                        {"text": "Filtrer le carburant.", "isCorrect": False}
                    ],
                    "correction": "Le turbocompresseur utilise l'énergie des gaz d'échappement pour comprimer l'air d'admission, améliorant ainsi le **rendement** et la puissance du moteur."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le rôle du calorstat (ou thermostat) dans le circuit de refroidissement ?",
                    "answerOptions": [
                        {"text": "Démarrer le ventilateur.", "isCorrect": False},
                        {"text": "Maintenir le moteur à sa température de fonctionnement optimale en régulant la circulation du liquide de refroidissement vers le radiateur.", "isCorrect": True},
                        {"text": "Filtrer le liquide de refroidissement.", "isCorrect": False},
                        {"text": "Indiquer la pression d'huile.", "isCorrect": False}
                    ],
                    "correction": "Le **calorstat** est une vanne thermostatique. Il reste fermé tant que le moteur est froid, puis s'ouvre pour permettre la circulation vers le radiateur lorsque la température idéale est atteinte."
                },
                {
                    "questionNumber": 4,
                    "question": "Qu'est-ce que le 'jeu aux soupapes' ?",
                    "answerOptions": [
                        {"text": "La distance entre deux cylindres.", "isCorrect": False},
                        {"text": "Le jeu fonctionnel (distance) entre la queue de soupape et le poussoir/culbuteur, nécessaire pour la dilatation thermique.", "isCorrect": True},
                        {"text": "Le temps d'ouverture de la soupape.", "isCorrect": False},
                        {"text": "Le diamètre du siège de soupape.", "isCorrect": False}
                    ],
                    "correction": "Le **jeu aux soupapes** est essentiel. S'il est incorrect, les soupapes peuvent mal se fermer (perte de compression) ou ne pas se dilater correctement (risque de casse)."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la conséquence d'une 'détérioration de la courroie de distribution' (rupture) sur un moteur non interférentiel ?",
                    "answerOptions": [
                        {"text": "Une simple perte de puissance.", "isCorrect": False},
                        {"text": "Le moteur s'arrête sans dommage majeur.", "isCorrect": True},
                        {"text": "Une surchauffe immédiate.", "isCorrect": False},
                        {"text": "Une fuite d'huile.", "isCorrect": False}
                    ],
                    "correction": "Sur un moteur **non interférentiel**, les soupapes ne touchent pas les pistons si la courroie casse. Le moteur s'arrête. Sur un moteur interférentiel, la rupture entraîne la destruction du moteur."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le rôle du 'carter d'huile' ?",
                    "answerOptions": [
                        {"text": "Filtrer l'air d'admission.", "isCorrect": False},
                        {"text": "Stocker l'huile nécessaire à la lubrification du moteur et assurer son refroidissement partiel.", "isCorrect": True},
                        {"text": "Maintenir les pistons.", "isCorrect": False},
                        {"text": "Refroidir les gaz d'échappement.", "isCorrect": False}
                    ],
                    "correction": "Le **carter d'huile** est le réservoir en bas du moteur. La crépine de la pompe à huile y plonge pour aspirer l'huile et la distribuer sous pression."
                },
                {
                    "questionNumber": 7,
                    "question": "Lors d'un changement de bougies d'allumage (essence), que doit-on vérifier avant de serrer ?",
                    "answerOptions": [
                        {"text": "La couleur du carter.", "isCorrect": False},
                        {"text": "Le type de joint et l'écartement des électrodes (gap).", "isCorrect": True},
                        {"text": "Le niveau de liquide de frein.", "isCorrect": False},
                        {"text": "La pression des pneus.", "isCorrect": False}
                    ],
                    "correction": "L'**écartement des électrodes** (gap) est crucial pour la qualité de l'étincelle et doit correspondre aux spécifications du constructeur."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel composant d'un moteur Diesel permet d'augmenter la température de l'air admis pour faciliter le démarrage à froid ?",
                    "answerOptions": [
                        {"text": "Les bougies d'allumage.", "isCorrect": False},
                        {"text": "Les bougies de préchauffage.", "isCorrect": True},
                        {"text": "Le turbo.", "isCorrect": False},
                        {"text": "Le filtre à particules.", "isCorrect": False}
                    ],
                    "correction": "Les **bougies de préchauffage** sont des résistances électriques qui chauffent la chambre de combustion avant et pendant le démarrage, car l'inflammation du Diesel nécessite une haute température."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle est l'unité de mesure de la 'viscosité' de l'huile moteur ?",
                    "answerOptions": [
                        {"text": "Le Newton (N).", "isCorrect": False},
                        {"text": "Le Watt (W).", "isCorrect": False},
                        {"text": "Le SAE (Society of Automotive Engineers), ex : 5W30.", "isCorrect": True},
                        {"text": "Le Bar (B).", "isCorrect": False}
                    ],
                    "correction": "L'indice **SAE** (ex : 5W30) indique la viscosité. Le premier chiffre (5W) correspond à la fluidité à froid (Winter), le second (30) à la fluidité à chaud."
                },
                {
                    "questionNumber": 10,
                    "question": "Comment appelle-t-on le dispositif qui réduit la pollution en transformant les gaz toxiques (CO, NOx, HC) en gaz moins nocifs (CO2, N2, H2O) ?",
                    "answerOptions": [
                        {"text": "L'intercooler.", "isCorrect": False},
                        {"text": "Le catalyseur (ou pot catalytique).", "isCorrect": True},
                        {"text": "Le reniflard.", "isCorrect": False},
                        {"text": "Le démarreur.", "isCorrect": False}
                    ],
                    "correction": "Le **catalyseur** (trois voies pour l'essence) est un dispositif antipollution essentiel. Il contient des métaux précieux (Platine, Rhodium) qui servent de catalyseurs chimiques."
                },
                {
                    "questionNumber": 11,
                    "question": "Lors du remplacement d'un joint de culasse, quelle procédure de serrage est obligatoire ?",
                    "answerOptions": [
                        {"text": "Le serrage au jugé.", "isCorrect": False},
                        {"text": "Le serrage en spirale.", "isCorrect": False},
                        {"text": "Le serrage en escargot (ou par passe) et selon le couple et l'angle du constructeur.", "isCorrect": True},
                        {"text": "Le serrage en ligne droite.", "isCorrect": False}
                    ],
                    "correction": "Le serrage des vis de culasse doit suivre un **ordre (spirale ou escargot)** et un couple/angle très précis pour assurer l'étanchéité et éviter le voilage de la culasse."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le rôle du 'volant moteur' ?",
                    "answerOptions": [
                        {"text": "Distribuer le carburant.", "isCorrect": False},
                        {"text": "Équilibrer les irrégularités de rotation du moteur et servir de support au mécanisme d'embrayage.", "isCorrect": True},
                        {"text": "Ouvrir les soupapes.", "isCorrect": False},
                        {"text": "Refroidir les pistons.", "isCorrect": False}
                    ],
                    "correction": "Le **volant moteur** (souvent bi-masse aujourd'hui) est une masse lourde qui stocke l'énergie cinétique pour régulariser la rotation entre les temps moteurs."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel système est utilisé dans les moteurs Diesel modernes pour réduire les émissions d'oxydes d'azote (NOx) ?",
                    "answerOptions": [
                        {"text": "Le FAP (Filtre à Particules).", "isCorrect": False},
                        {"text": "Le système SCR (Selective Catalytic Reduction) utilisant l'AdBlue.", "isCorrect": True},
                        {"text": "Le turbo simple.", "isCorrect": False},
                        {"text": "La pompe à huile.", "isCorrect": False}
                    ],
                    "correction": "Le système **SCR** injecte de l'AdBlue (solution d'urée) dans les gaz d'échappement pour convertir les NOx en azote et en eau, réduisant ainsi la pollution."
                },
                {
                    "questionNumber": 14,
                    "question": "Lors d'un test de compression moteur, une valeur faible peut indiquer un problème au niveau de :",
                    "answerOptions": [
                        {"text": "L'alternateur.", "isCorrect": False},
                        {"text": "Le démarreur.", "isCorrect": False},
                        {"text": "L'étanchéité des soupapes, le joint de culasse ou la segmentation des pistons.", "isCorrect": True},
                        {"text": "L'autoradio.", "isCorrect": False}
                    ],
                    "correction": "La **compression** est vitale. Un manque indique une fuite de pression dans la chambre de combustion, souvent due à un composant défectueux (soupapes qui ferment mal, joint de culasse percé, segments usés)."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel organe mécanique assure la synchronisation entre le vilebrequin et l'arbre à cames ?",
                    "answerOptions": [
                        {"text": "La bielle.", "isCorrect": False},
                        {"text": "Le pignon de différentiel.", "isCorrect": False},
                        {"text": "La courroie ou la chaîne de distribution.", "isCorrect": True},
                        {"text": "Le collecteur d'admission.", "isCorrect": False}
                    ],
                    "correction": "La **courroie/chaîne de distribution** est l'organe essentiel qui garantit que les soupapes s'ouvrent et se ferment au bon moment par rapport à la position des pistons (le calage)."
                },
                {
                    "questionNumber": 16,
                    "question": "Qu'est-ce qu'un 'injecteur' ?",
                    "answerOptions": [
                        {"text": "Un filtre à air.", "isCorrect": False},
                        {"text": "Un dispositif qui pulvérise précisément le carburant dans l'admission ou la chambre de combustion.", "isCorrect": True},
                        {"text": "Une pièce de l'embrayage.", "isCorrect": False},
                        {"text": "Le réservoir d'huile.", "isCorrect": False}
                    ],
                    "correction": "L'**injecteur** est contrôlé électroniquement pour délivrer la quantité exacte de carburant, au bon moment et sous haute pression (surtout Diesel Common Rail), pour une combustion optimale."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le rôle de la pompe à eau dans le moteur ?",
                    "answerOptions": [
                        {"text": "Injecter le carburant.", "isCorrect": False},
                        {"text": "Mettre le liquide de refroidissement en circulation forcée entre le moteur et le radiateur.", "isCorrect": True},
                        {"text": "Assurer la pression d'huile.", "isCorrect": False},
                        {"text": "Gérer la climatisation.", "isCorrect": False}
                    ],
                    "correction": "La **pompe à eau** est souvent entraînée par la courroie d'accessoire (ou de distribution) et est vitale pour éviter la surchauffe du moteur."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le principal symptôme d'un filtre à air encrassé ?",
                    "answerOptions": [
                        {"text": "Un bruit métallique.", "isCorrect": False},
                        {"text": "Une perte de puissance et une augmentation de la consommation de carburant (mélange trop riche).", "isCorrect": True},
                        {"text": "Un problème de freinage.", "isCorrect": False},
                        {"text": "Une fuite de liquide de refroidissement.", "isCorrect": False}
                    ],
                    "correction": "Un filtre à air sale réduit l'arrivée d'air frais. Le moteur est **étouffé**, ce qui entraîne une baisse de performance et une surconsommation, car le rapport air/carburant est déséquilibré."
                },
                {
                    "questionNumber": 19,
                    "question": "Qu'est-ce qu'un moteur 'interférentiel' ?",
                    "answerOptions": [
                        {"text": "Un moteur qui ne fait pas de bruit.", "isCorrect": False},
                        {"text": "Un moteur dont les soupapes et les pistons peuvent entrer en collision en cas de décalage de la distribution.", "isCorrect": True},
                        {"text": "Un moteur avec turbo.", "isCorrect": False},
                        {"text": "Un moteur électrique.", "isCorrect": False}
                    ],
                    "correction": "La majorité des moteurs modernes sont **interférentiels**. La rupture de la courroie ou un mauvais calage entraîne des dégâts mécaniques majeurs (soupapes tordues, pistons marqués)."
                },
                {
                    "questionNumber": 20,
                    "question": "Le système de 'recyclage des gaz d'échappement' (EGR) sert principalement à :",
                    "answerOptions": [
                        {"text": "Faire fonctionner la climatisation.", "isCorrect": False},
                        {"text": "Réduire la température de combustion pour diminuer la formation d'oxydes d'azote (NOx).", "isCorrect": True},
                        {"text": "Augmenter la pression d'huile.", "isCorrect": False},
                        {"text": "Filtrer la poussière.", "isCorrect": False}
                    ],
                    "correction": "La vanne **EGR** (Exhaust Gas Recirculation) réintroduit une petite partie des gaz d'échappement dans l'admission. Ces gaz inertes abaissent la température de combustion, ce qui réduit la production de NOx."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TRAINS ROULANTS, LIAISON AU SOL ET FREINAGE (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Trains Roulants, Liaison au Sol et Freinage (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le rôle principal du système ABS (Anti-lock Braking System) ?",
                    "answerOptions": [
                        {"text": "Réduire la distance de freinage sur toutes surfaces.", "isCorrect": False},
                        {"text": "Empêcher le blocage des roues lors du freinage pour conserver la direction du véhicule.", "isCorrect": True},
                        {"text": "Augmenter la puissance de freinage.", "isCorrect": False},
                        {"text": "Réguler la hauteur de caisse.", "isCorrect": False}
                    ],
                    "correction": "L'**ABS** ne réduit pas toujours la distance de freinage, mais il permet au conducteur de **garder le contrôle de la direction** en évitant le blocage des roues."
                },
                {
                    "questionNumber": 22,
                    "question": "Que mesure-t-on lors de la vérification du parallélisme (géométrie) d'un train avant ?",
                    "answerOptions": [
                        {"text": "L'usure des plaquettes de frein.", "isCorrect": False},
                        {"text": "L'angle d'inclinaison des roues par rapport à l'axe longitudinal du véhicule (le pincement ou l'ouverture).", "isCorrect": True},
                        {"text": "La pression des amortisseurs.", "isCorrect": False},
                        {"text": "La hauteur des ressorts.", "isCorrect": False}
                    ],
                    "correction": "Le **parallélisme** (ou pince/ouverture) est l'angle d'une roue vue de dessus. Un défaut provoque une usure anormale des pneus et une mauvaise tenue de route."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la fonction principale de l'amortisseur ?",
                    "answerOptions": [
                        {"text": "Supporter le poids du véhicule.", "isCorrect": False},
                        {"text": "Amortir les chocs.", "isCorrect": False},
                        {"text": "Freiner les oscillations du ressort de suspension pour maintenir le pneu en contact permanent avec la route.", "isCorrect": True},
                        {"text": "Transmettre le mouvement de rotation.", "isCorrect": False}
                    ],
                    "correction": "L'amortisseur est un élément de **dissipation d'énergie** (souvent hydraulique). Il agit comme un frein pour le ressort, qui lui supporte le poids du véhicule."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est l'une des causes les plus fréquentes de vibrations dans la direction à haute vitesse ?",
                    "answerOptions": [
                        {"text": "Un filtre à huile bouché.", "isCorrect": False},
                        {"text": "Un mauvais équilibrage des roues ou un défaut de la jante/du pneu.", "isCorrect": True},
                        {"text": "Une défaillance de l'ABS.", "isCorrect": False},
                        {"text": "Un mauvais serrage de bougie.", "isCorrect": False}
                    ],
                    "correction": "L'**équilibrage des roues** est essentiel. Une petite masse manquante ou mal placée provoque des vibrations ressenties dans le volant à partir de certaines vitesses."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le liquide de travail utilisé dans la majorité des circuits de freinage hydraulique ?",
                    "answerOptions": [
                        {"text": "L'eau.", "isCorrect": False},
                        {"text": "Le liquide de refroidissement.", "isCorrect": False},
                        {"text": "Le liquide de frein (souvent DOT 4 ou DOT 5.1).", "isCorrect": True},
                        {"text": "L'huile moteur.", "isCorrect": False}
                    ],
                    "correction": "Le **liquide de frein** est non compressible et doit avoir un point d'ébullition élevé (pour résister à la chaleur du freinage). Il est très hygroscopique (absorbe l'eau) et doit être remplacé régulièrement."
                },
                {
                    "questionNumber": 26,
                    "question": "Un 'pincement' excessif des roues avant (vues de dessus) entraîne principalement :",
                    "answerOptions": [
                        {"text": "Une usure anormale sur l'extérieur de la bande de roulement.", "isCorrect": False},
                        {"text": "Une usure anormale sur l'intérieur de la bande de roulement.", "isCorrect": True},
                        {"text": "Une usure uniforme.", "isCorrect": False},
                        {"text": "Une fuite d'huile.", "isCorrect": False}
                    ],
                    "correction": "Le **pincement** (les roues 'regardent' vers l'intérieur) crée un frottement qui use prématurément l'intérieur des pneus. L'ouverture use l'extérieur."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le composant qui transmet le mouvement de rotation de la boîte de vitesses à la roue motrice (sur un véhicule à traction) ?",
                    "answerOptions": [
                        {"text": "La rotule de direction.", "isCorrect": False},
                        {"text": "Le cardan (arbre de transmission ou arbre de roue).", "isCorrect": True},
                        {"text": "Le disque de frein.", "isCorrect": False},
                        {"text": "Le ressort de suspension.", "isCorrect": False}
                    ],
                    "correction": "Le **cardan** (ou joint homocinétique) est crucial car il doit transmettre le couple quelle que soit la position de la roue (braquage et hauteur de suspension)."
                },
                {
                    "questionNumber": 28,
                    "question": "Pourquoi la purge du circuit de freinage est-elle obligatoire après un remplacement d'étrier ou de maître-cylindre ?",
                    "answerOptions": [
                        {"text": "Pour enlever l'excès de liquide.", "isCorrect": False},
                        {"text": "Pour retirer l'air qui s'est introduit dans le circuit et qui rendrait le liquide compressible (frein mou).", "isCorrect": True},
                        {"text": "Pour recalibrer l'ABS.", "isCorrect": False},
                        {"text": "Pour changer le liquide de refroidissement.", "isCorrect": False}
                    ],
                    "correction": "L'**air** est compressible, contrairement au liquide de frein. Sa présence rend la pédale 'spongieuse' (molle) et dangereuse. La purge l'élimine."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la première lecture à faire sur le flanc d'un pneu (par exemple 205/55 R 16) ?",
                    "answerOptions": [
                        {"text": "Le diamètre de la jante (16).", "isCorrect": False},
                        {"text": "La largeur de la bande de roulement en millimètres (205).", "isCorrect": True},
                        {"text": "Le type de gomme (R).", "isCorrect": False},
                        {"text": "Le code de vitesse (V).", "isCorrect": False}
                    ],
                    "correction": "Le premier chiffre (**205**) correspond à la **largeur** du pneu en millimètres (mm). Le deuxième (55) est le ratio d'aspect (hauteur par rapport à la largeur)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est l'outil spécifique utilisé pour mesurer l'usure de la bande de roulement des pneus ?",
                    "answerOptions": [
                        {"text": "Le pied à coulisse.", "isCorrect": False},
                        {"text": "La jauge de profondeur (ou testeur d'usure de pneu).", "isCorrect": True},
                        {"text": "Le micromètre.", "isCorrect": False},
                        {"text": "Le manomètre.", "isCorrect": False}
                    ],
                    "correction": "La **jauge de profondeur** permet de vérifier que l'usure n'atteint pas le témoin légal (**1,6 mm** minimum en France)."
                },
                {
                    "questionNumber": 31,
                    "question": "Le voyant ESP (Electronic Stability Program) allumé en permanence indique :",
                    "answerOptions": [
                        {"text": "Que le moteur est chaud.", "isCorrect": False},
                        {"text": "Un défaut dans le système de stabilité et de contrôle de traction (capteur d'angle au volant, capteur de lacet, etc.).", "isCorrect": True},
                        {"text": "Que les pneus sont sous-gonflés.", "isCorrect": False},
                        {"text": "Un manque de carburant.", "isCorrect": False}
                    ],
                    "correction": "L'**ESP** est un système de sécurité qui agit sur les freins pour stabiliser le véhicule. Un voyant allumé signifie que le système est désactivé ou défaillant et nécessite un diagnostic."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est la précaution essentielle à prendre avant de démonter un étrier de frein ?",
                    "answerOptions": [
                        {"text": "Vidanger l'huile moteur.", "isCorrect": False},
                        {"text": "Placer un bac de récupération pour le liquide de frein qui va s'écouler.", "isCorrect": True},
                        {"text": "Débrancher la batterie.", "isCorrect": False},
                        {"text": "Changer les bougies.", "isCorrect": False}
                    ],
                    "correction": "Le liquide de frein est un produit **dangereux pour l'environnement** et agressif pour les peintures. Il doit être récupéré et traité comme un déchet spécial."
                },
                {
                    "questionNumber": 33,
                    "question": "Que peut provoquer un soufflet de cardan déchiré ?",
                    "answerOptions": [
                        {"text": "Un problème d'éclairage.", "isCorrect": False},
                        {"text": "La perte de la graisse du joint et l'entrée de poussière/eau, entraînant la destruction rapide du joint de cardan.", "isCorrect": True},
                        {"text": "Une fuite de liquide de refroidissement.", "isCorrect": False},
                        {"text": "Une usure des plaquettes de frein.", "isCorrect": False}
                    ],
                    "correction": "Le **soufflet** protège les roulements du cardan. S'il est percé, la lubrification est perdue et des corps étrangers rentrent, ce qui provoque rapidement un bruit de claquement en braquage."
                },
                {
                    "questionNumber": 34,
                    "question": "Pourquoi le serrage des roues (écrous/vis) doit-il toujours se faire au 'couple' (à la clé dynamométrique) ?",
                    "answerOptions": [
                        {"text": "Pour que la roue soit plus belle.", "isCorrect": False},
                        {"text": "Pour éviter la déformation du disque de frein ou de la jante, et garantir la sécurité.", "isCorrect": True},
                        {"text": "Pour gagner du temps.", "isCorrect": False},
                        {"text": "Pour réduire le bruit.", "isCorrect": False}
                    ],
                    "correction": "Un serrage excessif (**surtension**) peut voiler le disque de frein (vibrations au freinage) ou étirer les goujons. Un serrage insuffisant est un danger immédiat."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est la conséquence la plus grave de l'usure de l'épaisseur des disques de frein (sous la cote minimale) ?",
                    "answerOptions": [
                        {"text": "Le patinage du moteur.", "isCorrect": False},
                        {"text": "Le risque de rupture du disque sous la contrainte thermique et mécanique du freinage (danger immédiat).", "isCorrect": True},
                        {"text": "Une mauvaise lecture de la température.", "isCorrect": False},
                        {"text": "Une usure du volant moteur.", "isCorrect": False}
                    ],
                    "correction": "Les disques trop minces perdent leur capacité à dissiper la chaleur et risquent de **se fissurer ou de se briser** lors d'un freinage intense."
                },
                {
                    "questionNumber": 36,
                    "question": "Qu'est-ce qu'une 'crémaillère de direction' ?",
                    "answerOptions": [
                        {"text": "Une pièce du moteur.", "isCorrect": False},
                        {"text": "Un mécanisme qui transforme le mouvement de rotation du volant en mouvement linéaire pour orienter les roues.", "isCorrect": True},
                        {"text": "Le support de l'alternateur.", "isCorrect": False},
                        {"text": "Le système d'échappement.", "isCorrect": False}
                    ],
                    "correction": "La **crémaillère** est la pièce centrale de la direction. Elle est reliée au volant par la colonne de direction et aux roues par les biellettes de direction."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est le rôle du 'tambour' de frein, souvent utilisé sur les roues arrière ?",
                    "answerOptions": [
                        {"text": "Un élément de suspension.", "isCorrect": False},
                        {"text": "Un élément fixe qui reçoit la pression des mâchoires pour ralentir la rotation de la roue.", "isCorrect": False},
                        {"text": "Un élément rotatif (solidaire de la roue) qui est freiné par l'écartement des mâchoires/garnitures.", "isCorrect": True},
                        {"text": "Un capteur ABS.", "isCorrect": False}
                    ],
                    "correction": "Le **tambour** est une cloche qui tourne avec la roue. Le freinage est obtenu par l'écartement des mâchoires qui viennent frotter contre la paroi intérieure du tambour."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la principale fonction du 'roulement de roue' ?",
                    "answerOptions": [
                        {"text": "Générer de l'électricité.", "isCorrect": False},
                        {"text": "Permettre la rotation de la roue autour de son axe avec le minimum de friction.", "isCorrect": True},
                        {"text": "Faire tenir le pneu sur la jante.", "isCorrect": False},
                        {"text": "Maintenir la pression des pneus.", "isCorrect": False}
                    ],
                    "correction": "Le **roulement** utilise des billes ou des rouleaux pour minimiser le frottement. Un roulement défectueux se manifeste par un bruit de grondement (ronronnement) qui augmente avec la vitesse."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le risque si l'on installe des pneus dont l'indice de charge est inférieur à celui spécifié par le constructeur ?",
                    "answerOptions": [
                        {"text": "Un bruit excessif.", "isCorrect": False},
                        {"text": "Un risque d'éclatement ou de dégradation du pneu lors d'une forte charge ou à haute vitesse.", "isCorrect": True},
                        {"text": "Le moteur va consommer plus.", "isCorrect": False},
                        {"text": "Le freinage sera meilleur.", "isCorrect": False}
                    ],
                    "correction": "L'**indice de charge** doit impérativement être respecté (ou supérieur). Un indice inférieur met en danger l'intégrité du pneu en cas de surcharge du véhicule."
                },
                {
                    "questionNumber": 40,
                    "question": "Que signifie un jeu excessif dans une rotule de suspension ?",
                    "answerOptions": [
                        {"text": "La voiture est trop basse.", "isCorrect": False},
                        {"text": "Une mauvaise liaison au sol, des bruits anormaux et un risque de déboîtement du train roulant (danger).", "isCorrect": True},
                        {"text": "Le moteur ne démarre plus.", "isCorrect": False},
                        {"text": "Le chauffage ne marche plus.", "isCorrect": False}
                    ],
                    "correction": "La rotule assure le lien entre le porte-moyeu et le bras de suspension. Un **jeu excessif** (usure) est un défaut grave et un motif de contre-visite au contrôle technique."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : ÉLECTRICITÉ, ÉLECTRONIQUE ET CLIMATISATION (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Électricité, Électronique et Climatisation (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le rôle de l'alternateur ?",
                    "answerOptions": [
                        {"text": "Stocker l'énergie électrique.", "isCorrect": False},
                        {"text": "Transformer l'énergie mécanique du moteur en énergie électrique pour alimenter les consommateurs et recharger la batterie.", "isCorrect": True},
                        {"text": "Faire démarrer le moteur.", "isCorrect": False},
                        {"text": "Couper le circuit électrique en cas de panne.", "isCorrect": False}
                    ],
                    "correction": "L'**alternateur** est le générateur du véhicule. Il produit du courant alternatif (AC) qui est ensuite redressé en courant continu (DC) par un pont de diodes."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la principale unité de mesure d'un test de batterie (capacité) ?",
                    "answerOptions": [
                        {"text": "Le Volt (V).", "isCorrect": False},
                        {"text": "L'Ampère-heure (Ah).", "isCorrect": True},
                        {"text": "L'Ohm (Ω).", "isCorrect": False},
                        {"text": "Le Bar (B).", "isCorrect": False}
                    ],
                    "correction": "L'**Ampère-heure (Ah)** mesure la capacité de stockage de la batterie. Le CCA (Cold Cranking Amps) mesure sa capacité de fournir un fort courant de démarrage à froid."
                },
                {
                    "questionNumber": 43,
                    "question": "Pourquoi doit-on impérativement débrancher la batterie avant de travailler sur le circuit électrique ?",
                    "answerOptions": [
                        {"text": "Pour réinitialiser les calculateurs.", "isCorrect": False},
                        {"text": "Pour éviter les courts-circuits, les arcs électriques (risques d'incendie) et les dommages aux calculateurs.", "isCorrect": True},
                        {"text": "Pour tester la tension.", "isCorrect": False},
                        {"text": "Pour vider le réservoir.", "isCorrect": False}
                    ],
                    "correction": "Débrancher la batterie (le **moins en premier**) est la règle de sécurité de base pour tout travail électrique ou mécanique où un contact involontaire peut provoquer un court-circuit."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le rôle du 'démarreur' ?",
                    "answerOptions": [
                        {"text": "Produire de l'électricité.", "isCorrect": False},
                        {"text": "Fournir un couple mécanique pour lancer la rotation initiale du moteur thermique.", "isCorrect": True},
                        {"text": "Réguler la tension.", "isCorrect": False},
                        {"text": "Contrôler la boîte de vitesses.", "isCorrect": False}
                    ],
                    "correction": "Le **démarreur** est un moteur électrique qui s'engage sur la couronne du volant moteur pour démarrer le cycle du moteur thermique."
                },
                {
                    "questionNumber": 45,
                    "question": "Le multiplexage (réseau CAN) dans un véhicule sert à :",
                    "answerOptions": [
                        {"text": "Augmenter la vitesse maximale.", "isCorrect": False},
                        {"text": "Réduire le nombre de câbles en faisant transiter l'information entre les calculateurs par deux fils de communication.", "isCorrect": True},
                        {"text": "Couper le moteur à distance.", "isCorrect": False},
                        {"text": "Améliorer l'éclairage intérieur.", "isCorrect": False}
                    ],
                    "correction": "Le **multiplexage** (réseau CAN - Controller Area Network) permet aux calculateurs de partager des informations vitales (vitesse, température, régime moteur) via un bus de communication, simplifiant le câblage."
                },
                {
                    "questionNumber": 46,
                    "question": "Qu'est-ce qu'un 'fusible' et à quoi sert-il ?",
                    "answerOptions": [
                        {"text": "Un interrupteur simple.", "isCorrect": False},
                        {"text": "Un composant calibré qui fond en cas de surintensité pour protéger le circuit électrique.", "isCorrect": True},
                        {"text": "Une résistance pour augmenter le courant.", "isCorrect": False},
                        {"text": "Un capteur de tension.", "isCorrect": False}
                    ],
                    "correction": "Le **fusible** est une sécurité. Il est toujours monté en série et sa capacité (en Ampères) est choisie pour protéger le câblage et les composants du circuit."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le gaz réfrigérant le plus couramment utilisé dans les systèmes de climatisation automobiles modernes (après l'interdiction du R-134a dans les nouveaux modèles) ?",
                    "answerOptions": [
                        {"text": "Le Butane.", "isCorrect": False},
                        {"text": "Le R-12.", "isCorrect": False},
                        {"text": "Le R-1234yf.", "isCorrect": True},
                        {"text": "L'Air comprimé.", "isCorrect": False}
                    ],
                    "correction": "Le **R-1234yf** (Tétrafluoropropène) a remplacé le R-134a sur les véhicules neufs en raison de son potentiel de réchauffement climatique (PRG) beaucoup plus faible."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel composant électrique est vital pour la sécurité et la bonne gestion du moteur (injection) ?",
                    "answerOptions": [
                        {"text": "Le klaxon.", "isCorrect": False},
                        {"text": "Le capteur PMH (Point Mort Haut) ou capteur de vilebrequin.", "isCorrect": True},
                        {"text": "Le lève-vitre.", "isCorrect": False},
                        {"text": "L'ampoule de plaque.", "isCorrect": False}
                    ],
                    "correction": "Le **capteur PMH** est crucial. Il donne la position et la vitesse de rotation du moteur au calculateur pour le calage de l'allumage/injection. Sans lui, le moteur ne démarre pas."
                },
                {
                    "questionNumber": 49,
                    "question": "Dans un circuit de climatisation, quel organe est chargé de comprimer le fluide frigorigène à haute pression ?",
                    "answerOptions": [
                        {"text": "Le condenseur.", "isCorrect": False},
                        {"text": "Le compresseur.", "isCorrect": True},
                        {"text": "Le détendeur.", "isCorrect": False},
                        {"text": "L'évaporateur.", "isCorrect": False}
                    ],
                    "correction": "Le **compresseur**, entraîné par le moteur, est le cœur du système. Il augmente la pression et la température du fluide avant qu'il n'aille au condenseur."
                },
                {
                    "questionNumber": 50,
                    "question": "Qu'est-ce qu'un 'relais' électrique ?",
                    "answerOptions": [
                        {"text": "Une bobine d'allumage.", "isCorrect": False},
                        {"text": "Un interrupteur commandé par un faible courant pour permettre à un fort courant de circuler dans un autre circuit.", "isCorrect": True},
                        {"text": "Un capteur de niveau.", "isCorrect": False},
                        {"text": "Un redresseur.", "isCorrect": False}
                    ],
                    "correction": "Le **relais** permet de protéger l'interrupteur principal et le câblage de commande en utilisant un faible courant, tout en contrôlant des composants qui consomment beaucoup (phares, démarreur, klaxon)."
                },
                {
                    "questionNumber": 51,
                    "question": "Comment appelle-t-on la pièce qui assure la régulation de la tension de sortie de l'alternateur ?",
                    "answerOptions": [
                        {"text": "Le redresseur.", "isCorrect": False},
                        {"text": "Le régulateur de tension.", "isCorrect": True},
                        {"text": "Le contacteur.", "isCorrect": False},
                        {"text": "Le pont de diodes.", "isCorrect": False}
                    ],
                    "correction": "Le **régulateur de tension** maintient la tension de sortie de l'alternateur entre 13,8 V et 14,8 V, quelle que soit la vitesse du moteur, pour éviter de surcharger la batterie."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le risque de tester un circuit électrique avec un testeur artisanal (lampe témoin) sur un circuit électronique moderne (faible intensité) ?",
                    "answerOptions": [
                        {"text": "Le test sera trop précis.", "isCorrect": False},
                        {"text": "Le courant élevé de la lampe témoin risque de détruire le calculateur (ECU) ou le capteur testé.", "isCorrect": True},
                        {"text": "La batterie va se décharger.", "isCorrect": False},
                        {"text": "Rien.", "isCorrect": False}
                    ],
                    "correction": "Il faut impérativement utiliser un **multimètre numérique** (haute impédance) pour vérifier les circuits électroniques sensibles. Une lampe témoin est réservée aux circuits de puissance (phares, klaxon)."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle du 'condenseur' (climatisation) ?",
                    "answerOptions": [
                        {"text": "Produire le froid.", "isCorrect": False},
                        {"text": "Faire passer le fluide frigorigène de l'état gazeux à l'état liquide en évacuant la chaleur (situé à l'avant du véhicule).", "isCorrect": True},
                        {"text": "Filtrer le gaz.", "isCorrect": False},
                        {"text": "Démarrer le moteur.", "isCorrect": False}
                    ],
                    "correction": "Le **condenseur** est l'équivalent du radiateur dans le circuit de refroidissement. C'est là que la chaleur absorbée dans l'habitacle est relâchée dans l'air extérieur."
                },
                {
                    "questionNumber": 54,
                    "question": "Que signifie la lecture 'Circuit Ouvert' sur un multimètre (mode Ohmmètre) ?",
                    "answerOptions": [
                        {"text": "Le courant est trop fort.", "isCorrect": False},
                        {"text": "Le circuit est incomplet, interrompu, ou la résistance est infinie (coupure de câble).", "isCorrect": True},
                        {"text": "Le circuit est en court-circuit.", "isCorrect": False},
                        {"text": "Le courant est trop faible.", "isCorrect": False}
                    ],
                    "correction": "Un **circuit ouvert** indique que le courant ne peut pas circuler. Le multimètre affiche 'OL' (Over Limit) ou l'infini, signifiant une rupture (câble coupé, fusible grillé, composant déconnecté)."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel capteur est utilisé par l'ABS pour détecter la vitesse de rotation de chaque roue ?",
                    "answerOptions": [
                        {"text": "Le capteur de température.", "isCorrect": False},
                        {"text": "Le capteur de régime moteur.", "isCorrect": False},
                        {"text": "Le capteur de vitesse de roue (capteur actif ou passif).", "isCorrect": True},
                        {"text": "Le capteur de pression d'huile.", "isCorrect": False}
                    ],
                    "correction": "Chaque roue est équipée d'un **capteur de vitesse** (souvent à effet Hall ou inductif) qui informe le calculateur ABS de sa rotation pour détecter le blocage imminent ou le patinage."
                },
                {
                    "questionNumber": 56,
                    "question": "Lors d'une recharge de batterie avec un chargeur, quel est l'ordre correct de raccordement ?",
                    "answerOptions": [
                        {"text": "Moins sur Moins, puis Plus sur Plus.", "isCorrect": True},
                        {"text": "Plus sur Moins, puis Moins sur Plus.", "isCorrect": False},
                        {"text": "Peu importe l'ordre.", "isCorrect": False},
                        {"text": "Moins sur Plus, puis Plus sur Moins.", "isCorrect": False}
                    ],
                    "correction": "Raccorder **Plus sur Plus et Moins sur Moins** évite les inversions de polarité qui peuvent endommager la batterie ou l'électronique du véhicule."
                },
                {
                    "questionNumber": 57,
                    "question": "Le filtre d'habitacle (filtre à pollen) a pour but de :",
                    "answerOptions": [
                        {"text": "Filtrer le carburant.", "isCorrect": False},
                        {"text": "Nettoyer l'air entrant dans l'habitacle des poussières, pollens et parfois des mauvaises odeurs.", "isCorrect": True},
                        {"text": "Filtrer l'huile moteur.", "isCorrect": False},
                        {"text": "Augmenter le débit d'air.", "isCorrect": False}
                    ],
                    "correction": "Le **filtre d'habitacle** est crucial pour la santé des occupants et pour le bon fonctionnement de la ventilation/climatisation (un filtre bouché réduit l'efficacité et fait forcer le ventilateur)."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le risque de manipuler un câble haute tension d'un véhicule hybride ou électrique sans formation spécifique ?",
                    "answerOptions": [
                        {"text": "Une mauvaise couleur.", "isCorrect": False},
                        {"text": "Un risque de choc électrique (électrocution) très grave ou mortel (tension supérieure à 60V DC).", "isCorrect": True},
                        {"text": "Une fuite d'huile.", "isCorrect": False},
                        {"text": "Un problème de freinage.", "isCorrect": False}
                    ],
                    "correction": "Les véhicules électriques et hybrides utilisent des tensions de **plusieurs centaines de Volts**. Seul un personnel qualifié (habilitation électrique B2VL/BR) est autorisé à travailler sur ces circuits (câbles souvent orange)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le rôle de l'évaporateur dans le circuit de climatisation ?",
                    "answerOptions": [
                        {"text": "Assurer la compression.", "isCorrect": False},
                        {"text": "Permettre au fluide frigorigène de passer de l'état liquide à l'état gazeux en absorbant la chaleur de l'air de l'habitacle (produit le froid).", "isCorrect": True},
                        {"text": "Dégivrer la lunette arrière.", "isCorrect": False},
                        {"text": "Filtrer l'humidité.", "isCorrect": False}
                    ],
                    "correction": "Situé dans l'habitacle, l'**évaporateur** est la zone d'échange froid. Le fluide y absorbe les calories de l'air, ce qui le refroidit (et le déshumidifie au passage)."
                },
                {
                    "questionNumber": 60,
                    "question": "Que signifie le terme 'Lin' (L-line) et 'K-line' dans le diagnostic électronique ?",
                    "answerOptions": [
                        {"text": "Deux types de phares.", "isCorrect": False},
                        {"text": "Des protocoles de communication pour le diagnostic entre un outil (valise) et les calculateurs (ECU).", "isCorrect": True},
                        {"text": "Deux types de batteries.", "isCorrect": False},
                        {"text": "Des marques de pneus.", "isCorrect": False}
                    ],
                    "correction": "Le **LIN** et le **K-Line** sont des protocoles de communication standard (ISO) qui permettent à l'outil de diagnostic de lire les codes défauts et les paramètres des calculateurs."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : DIAGNOSTIC, MÉTHODOLOGIE ET DOCUMENTATION (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Diagnostic, Méthodologie et Documentation (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est l'outil principal utilisé pour lire et effacer les codes défauts (DTC) des calculateurs (ECU) ?",
                    "answerOptions": [
                        {"text": "Le multimètre.", "isCorrect": False},
                        {"text": "La clé dynamométrique.", "isCorrect": False},
                        {"text": "L'outil de diagnostic (ou 'valise' de diagnostic).", "isCorrect": True},
                        {"text": "Le manomètre.", "isCorrect": False}
                    ],
                    "correction": "L'**outil de diagnostic** (ou scanner) se connecte à la prise OBD (On-Board Diagnostics) du véhicule pour interroger les calculateurs et identifier la source d'une panne électronique."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est l'objectif de la méthode de diagnostic 'Organe, Fonction, Cause, Remède' (OFCG) ?",
                    "answerOptions": [
                        {"text": "Changer le moteur sans réfléchir.", "isCorrect": False},
                        {"text": "Structurer la recherche de panne en partant du défaut constaté (Organe) vers la solution (Remède).", "isCorrect": True},
                        {"text": "Ne s'occuper que du châssis.", "isCorrect": False},
                        {"text": "Travailler plus lentement.", "isCorrect": False}
                    ],
                    "correction": "L'**OFCG** est une méthode rigoureuse : 1. Identification de l'**Organe** ou système défaillant. 2. Identification de la **Fonction** ou dysfonctionnement. 3. Recherche de la **Cause**. 4. Mise en œuvre du **Remède**."
                },
                {
                    "questionNumber": 63,
                    "question": "Dans le diagnostic, que signifie un 'Code Défaut Permanent' ?",
                    "answerOptions": [
                        {"text": "Un défaut facile à réparer.", "isCorrect": False},
                        {"text": "Un défaut qui est présent à l'instant du diagnostic et qui nécessite une intervention immédiate (ex : capteur débranché).", "isCorrect": True},
                        {"text": "Un défaut qui a disparu.", "isCorrect": False},
                        {"text": "Un défaut qui n'existe pas.", "isCorrect": False}
                    ],
                    "correction": "Un code **Permanent** signifie que le défaut est toujours là. Un code **Fugitif** (ou mémorisé) est un défaut qui est apparu puis a disparu (intermittent) et qui est moins urgent."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est l'importance du 'couple de serrage' lors du remontage d'une pièce mécanique ?",
                    "answerOptions": [
                        {"text": "Elle n'a aucune importance, il suffit de serrer fort.", "isCorrect": False},
                        {"text": "Elle assure la bonne étanchéité, la sécurité et évite la déformation ou la rupture des pièces.", "isCorrect": True},
                        {"text": "Elle permet de gagner du temps.", "isCorrect": False},
                        {"text": "Elle rend la pièce plus légère.", "isCorrect": False}
                    ],
                    "correction": "Le **couple de serrage** est une valeur vitale (ex : vis de roues, culasse, carter). Il doit être respecté à l'aide d'une **clé dynamométrique** pour garantir la fiabilité de la réparation."
                },
                {
                    "questionNumber": 65,
                    "question": "Que doit-on faire en premier lieu lorsqu'un client se présente avec une panne (selon la méthodologie) ?",
                    "answerOptions": [
                        {"text": "Démonter immédiatement le moteur.", "isCorrect": False},
                        {"text": "Écouter attentivement la description de la panne par le client et la vérifier (essai routier ou test en atelier).", "isCorrect": True},
                        {"text": "Remplacer l'alternateur.", "isCorrect": False},
                        {"text": "Nettoyer les phares.", "isCorrect": False}
                    ],
                    "correction": "La **description du client** est la première source d'information. Elle permet de circonscrire le problème (bruit à froid, panne intermittente, etc.) avant de passer au diagnostic technique."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel document technique fournit le schéma détaillé du circuit électrique d'un véhicule ?",
                    "answerOptions": [
                        {"text": "La carte grise.", "isCorrect": False},
                        {"text": "La revue technique automobile (RTA) ou le manuel d'atelier du constructeur.", "isCorrect": True},
                        {"text": "Le permis de conduire.", "isCorrect": False},
                        {"text": "La facture d'achat.", "isCorrect": False}
                    ],
                    "correction": "La **documentation technique** du constructeur (ou RTA) contient toutes les données nécessaires (couples de serrage, schémas, méthodes de dépose/repose) pour une intervention conforme."
                },
                {
                    "questionNumber": 67,
                    "question": "Qu'est-ce qu'un 'témoin de niveau d'huile' allumé en rouge sur le tableau de bord (après le démarrage) ?",
                    "answerOptions": [
                        {"text": "Un simple manque d'huile.", "isCorrect": False},
                        {"text": "Un défaut de pression d'huile (danger imminent pour le moteur).", "isCorrect": True},
                        {"text": "Un manque de carburant.", "isCorrect": False},
                        {"text": "Un problème de phares.", "isCorrect": False}
                    ],
                    "correction": "Le voyant rouge de l'huile indique un manque de **pression** (souvent dû à une pompe défectueuse ou un niveau très bas), ce qui provoque un grippage rapide du moteur. Il faut couper le moteur immédiatement."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est l'outil utilisé pour évaluer l'état interne des cylindres (soupapes, pistons) sans démontage du moteur ?",
                    "answerOptions": [
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "Le boroscope (ou endoscope).", "isCorrect": True},
                        {"text": "Le voltmètre.", "isCorrect": False},
                        {"text": "La clé à choc.", "isCorrect": False}
                    ],
                    "correction": "Le **boroscope** (caméra fine) est inséré par l'orifice de bougie d'allumage/préchauffage pour inspecter l'état des têtes de piston et des soupapes, ou la présence de dépôts (calamine)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le risque de remplacer un calculateur (ECU) sans respecter la procédure de 'codage' ou 'télécodage' ?",
                    "answerOptions": [
                        {"text": "Il fonctionnera mieux.", "isCorrect": False},
                        {"text": "Le nouveau calculateur ne reconnaîtra pas l'antidémarrage et empêchera le démarrage du véhicule.", "isCorrect": True},
                        {"text": "La voiture sera plus rapide.", "isCorrect": False},
                        {"text": "Le chauffage sera meilleur.", "isCorrect": False}
                    ],
                    "correction": "Le **codage** (ou appairage) est une procédure essentielle qui lie le calculateur au véhicule (antidémarrage, numéro de série) pour des raisons de sécurité et de compatibilité."
                },
                {
                    "questionNumber": 70,
                    "question": "Pourquoi doit-on utiliser de l'outillage spécifique pour manipuler un 'filtre à carburant Diesel' lors de son remplacement ?",
                    "answerOptions": [
                        {"text": "Pour le rendre plus lourd.", "isCorrect": False},
                        {"text": "Pour éviter d'introduire des impuretés dans le circuit Haute Pression (injecteurs) et pour respecter la procédure de réamorçage.", "isCorrect": True},
                        {"text": "Pour le faire tourner.", "isCorrect": False},
                        {"text": "Pour le rendre plus petit.", "isCorrect": False}
                    ],
                    "correction": "Le circuit **Diesel Haute Pression** est très sensible aux impuretés (eau, poussière). Les injecteurs sont fragiles. Le réamorçage doit se faire sans air."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est le but d'un essai routier (test drive) après une réparation complexe ?",
                    "answerOptions": [
                        {"text": "Consommer l'essence du client.", "isCorrect": False},
                        {"text": "Valider la réparation, s'assurer que le défaut a disparu et que les paramètres de conduite sont corrects (sécurité et confort).", "isCorrect": True},
                        {"text": "Écouter la radio.", "isCorrect": False},
                        {"text": "Regarder le paysage.", "isCorrect": False}
                    ],
                    "correction": "L'**essai routier** est l'étape de validation finale. Il permet de reproduire les conditions de la panne et de s'assurer de l'efficacité de l'intervention."
                },
                {
                    "questionNumber": 72,
                    "question": "Que représente le sigle DTC dans le diagnostic automobile ?",
                    "answerOptions": [
                        {"text": "Diagnostic de Température de Carburant.", "isCorrect": False},
                        {"text": "Data Terminal Collector.", "isCorrect": False},
                        {"text": "Diagnostic Trouble Code (Code de Défaut de Diagnostic).", "isCorrect": True},
                        {"text": "Diesel Turbo Cleaner.", "isCorrect": False}
                    ],
                    "correction": "Le **DTC** est le code alphanumérique standardisé (P0xxx pour le moteur, Bxxxx pour la carrosserie, etc.) qui est lu par la valise et renvoie à une panne spécifique."
                },
                {
                    "questionNumber": 73,
                    "question": "Qu'est-ce qu'une 'fiche de travail' ou 'ordre de réparation' ?",
                    "answerOptions": [
                        {"text": "Le manuel d'atelier.", "isCorrect": False},
                        {"text": "Le document qui récapitule les travaux à effectuer, le temps alloué, et l'historique des pannes (pour le mécanicien).", "isCorrect": True},
                        {"text": "La facture finale.", "isCorrect": False},
                        {"text": "Le catalogue de pièces.", "isCorrect": False}
                    ],
                    "correction": "L'**ordre de réparation** est l'outil de gestion de l'atelier. Il permet au technicien de savoir ce qu'il doit faire et au chef d'atelier de suivre l'avancement et la rentabilité du travail."
                },
                {
                    "questionNumber": 74,
                    "question": "Lors du remplacement d'un filtre à huile, quelle précaution doit être prise avec le nouveau joint ?",
                    "answerOptions": [
                        {"text": "Le laisser sec.", "isCorrect": False},
                        {"text": "L'humidifier ou le graisser légèrement avec de l'huile moteur propre.", "isCorrect": True},
                        {"text": "Le couper en deux.", "isCorrect": False},
                        {"text": "Le serrer très fort.", "isCorrect": False}
                    ],
                    "correction": "Humidifier le **joint** assure une meilleure étanchéité au serrage et facilite le démontage ultérieur du filtre (le joint ne colle pas à la plaque)."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est l'outil de mesure utilisé pour contrôler la planéité d'une culasse (vérification de voilage) ?",
                    "answerOptions": [
                        {"text": "Le flexomètre.", "isCorrect": False},
                        {"text": "La règle de planéité (ou réglet) et le jeu de cales d'épaisseur.", "isCorrect": True},
                        {"text": "Le compresseur.", "isCorrect": False},
                        {"text": "La balance.", "isCorrect": False}
                    ],
                    "correction": "La **règle de planéité** et les cales d'épaisseur permettent de mesurer les écarts par rapport à une surface parfaitement plane. Un voilage nécessite un surfaçage ou un remplacement."
                },
                {
                    "questionNumber": 76,
                    "question": "Que doit vérifier le technicien avant de 'réamorcer' un circuit de refroidissement après une vidange ?",
                    "answerOptions": [
                        {"text": "Le niveau d'huile.", "isCorrect": False},
                        {"text": "L'absence de fuite et la bonne fermeture du bouchon de vidange/purge.", "isCorrect": True},
                        {"text": "La couleur des sièges.", "isCorrect": False},
                        {"text": "La pression des pneus.", "isCorrect": False}
                    ],
                    "correction": "Il faut s'assurer de l'**étanchéité** complète du circuit avant de remettre sous pression, pour éviter une fuite massive du nouveau liquide."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est la principale méthode pour diagnostiquer une fuite du système de climatisation ?",
                    "answerOptions": [
                        {"text": "L'essai routier.", "isCorrect": False},
                        {"text": "L'utilisation d'un traceur UV ou d'un détecteur électronique de fuite de gaz (sniffer).", "isCorrect": True},
                        {"text": "La mesure de la pression d'huile.", "isCorrect": False},
                        {"text": "Le test de compression.", "isCorrect": False}
                    ],
                    "correction": "Le **traceur UV** (ajouté au gaz) est le plus efficace. Il s'accumule sur la fuite et est visible sous une lumière UV. Le détecteur électronique repère les émissions de gaz frigorigène."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est l'objectif du 'déglaçage' des cylindres avant de remonter une segmentation neuve ?",
                    "answerOptions": [
                        {"text": "Rendre la surface plus brillante.", "isCorrect": False},
                        {"text": "Créer une micro-strie (honnage) sur la paroi du cylindre pour retenir l'huile et favoriser le rodage des nouveaux segments.", "isCorrect": True},
                        {"text": "Enlever la poussière.", "isCorrect": False},
                        {"text": "Changer la taille des cylindres.", "isCorrect": False}
                    ],
                    "correction": "Le **déglaçage** (ou honnage) permet de casser le film lisse créé par l'ancienne segmentation. La nouvelle surface retient l'huile (lubrification) et permet une meilleure étanchéité."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le risque de croiser les fils d'une bougie d'allumage sur un moteur à essence ?",
                    "answerOptions": [
                        {"text": "La voiture ira plus vite.", "isCorrect": False},
                        {"text": "Un 'raté' moteur, un cliquetis et un risque de destruction du catalyseur par injection de carburant non brûlé.", "isCorrect": True},
                        {"text": "Une fuite d'huile.", "isCorrect": False},
                        {"text": "Le freinage sera moins efficace.", "isCorrect": False}
                    ],
                    "correction": "L'ordre d'allumage doit être respecté. Un fil croisé provoque une étincelle au mauvais moment (**décalage d'allumage**), entraînant une mauvaise combustion et l'envoi d'essence imbrûlée dans le catalyseur."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la première chose à vérifier lorsqu'un moteur Diesel ne démarre pas (outre la batterie) ?",
                    "answerOptions": [
                        {"text": "Le niveau de liquide lave-glace.", "isCorrect": False},
                        {"text": "L'arrivée de carburant (circuit d'alimentation Diesel) ou l'état des bougies de préchauffage (à froid).", "isCorrect": True},
                        {"text": "Le clignotant.", "isCorrect": False},
                        {"text": "Le réglage des sièges.", "isCorrect": False}
                    ],
                    "correction": "Un moteur Diesel nécessite une **compression** élevée et une source de **chaleur** (bougies de préchauffage) pour l'auto-inflammation, ainsi qu'une **arrivée de carburant** sous haute pression. L'absence de l'un de ces éléments empêche le démarrage."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SÉCURITÉ, HYGIÈNE ET ENVIRONNEMENT (HSE) (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Sécurité, Hygiène et Environnement (HSE) (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'EPI (Équipement de Protection Individuelle) obligatoire lors du travail sous un véhicule levé (pont élévateur) ?",
                    "answerOptions": [
                        {"text": "La casquette de baseball.", "isCorrect": False},
                        {"text": "Les chaussures de sécurité (coquées) et, si nécessaire, les lunettes de protection.", "isCorrect": True},
                        {"text": "Les gants en tissu.", "isCorrect": False},
                        {"text": "Le gilet jaune.", "isCorrect": False}
                    ],
                    "correction": "Les **chaussures de sécurité** protègent contre les chutes d'objets lourds (pièces, outils) et sont l'EPI de base en atelier. Les lunettes protègent des projections."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment doit-on stocker les huiles usagées dans l'atelier ?",
                    "answerOptions": [
                        {"text": "Dans le caniveau.", "isCorrect": False},
                        {"text": "Dans un bidon non identifié.", "isCorrect": False},
                        {"text": "Dans des contenants étanches, clairement identifiés, et stockés dans une zone de rétention (bac anti-débordement).", "isCorrect": True},
                        {"text": "Dans des bouteilles en verre.", "isCorrect": False}
                    ],
                    "correction": "L'**huile usagée** est un déchet dangereux (DID). Le stockage doit respecter l'environnement (zone de rétention) pour éviter la pollution des sols en cas de fuite."
                },
                {
                    "questionNumber": 83,
                    "question": "Lors d'une intervention sur le circuit de climatisation, quel est le risque lié au fluide frigorigène (R-1234yf) ?",
                    "answerOptions": [
                        {"text": "La perte de poids.", "isCorrect": False},
                        {"text": "Le risque de gelure (brûlure par le froid) en cas de contact direct, et de toxicité en cas d'inhalation des vapeurs.", "isCorrect": True},
                        {"text": "L'incendie du véhicule.", "isCorrect": False},
                        {"text": "La décharge électrique.", "isCorrect": False}
                    ],
                    "correction": "Le fluide sort à très basse température. Il faut porter des **gants et des lunettes de protection**. Le gaz doit être impérativement récupéré par une station agréée."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le risque de travailler sur un véhicule soulevé par un cric hydraulique simple (sans chandelles) ?",
                    "answerOptions": [
                        {"text": "Le desserrage des roues.", "isCorrect": False},
                        {"text": "L'affaissement du véhicule (instabilité) et le risque d'accident très grave ou mortel.", "isCorrect": True},
                        {"text": "La décharge de la batterie.", "isCorrect": False},
                        {"text": "Le moteur ne démarre plus.", "isCorrect": False}
                    ],
                    "correction": "Le **cric est un outil de levage**, pas de maintien. Travailler sans **chandelles** (outils de maintien) est une faute de sécurité grave."
                },
                {
                    "questionNumber": 85,
                    "question": "Que doit-on faire de la batterie d'un véhicule qui est considérée comme HS (hors service) ?",
                    "answerOptions": [
                        {"text": "La jeter dans la poubelle normale.", "isCorrect": False},
                        {"text": "La stocker dans un conteneur dédié pour être recyclée par une filière agréée (déchet dangereux).", "isCorrect": True},
                        {"text": "La laisser dans la voiture.", "isCorrect": False},
                        {"text": "La vider de son électrolyte.", "isCorrect": False}
                    ],
                    "correction": "Les **batteries** contiennent du plomb et de l'acide sulfurique. Elles sont classées comme déchets dangereux (DD) et leur recyclage est obligatoire par des entreprises spécialisées."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le type d'extincteur approprié pour éteindre un feu de carburant (essence, huile) ?",
                    "answerOptions": [
                        {"text": "Extincteur à eau.", "isCorrect": False},
                        {"text": "Extincteur de type B ou F (Poudre ou CO2).", "isCorrect": True},
                        {"text": "Extincteur à mousse.", "isCorrect": False},
                        {"text": "Extincteur à sel.", "isCorrect": False}
                    ],
                    "correction": "Les feux de liquides inflammables (carburants) sont de classe B. Le CO2 (qui étouffe) ou la poudre B/C est le plus adapté. L'eau aggraverait la situation."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la nature du danger lors de l'utilisation de la soufflette à air comprimé ?",
                    "answerOptions": [
                        {"text": "Le moteur va s'arrêter.", "isCorrect": False},
                        {"text": "Le risque de projection de particules dans les yeux ou le risque d'embolie gazeuse (si contact avec la peau sous pression).", "isCorrect": True},
                        {"text": "Le gel des mains.", "isCorrect": False},
                        {"text": "La corrosion.", "isCorrect": False}
                    ],
                    "correction": "Le port de **lunettes de protection** est obligatoire lors du soufflage pour se prémunir des projections. Souffler sur la peau peut aussi être fatal (embolie)."
                },
                {
                    "questionNumber": 88,
                    "question": "Lors du remplacement d'un pneu, quelle est la position la plus stable pour desserrer les écrous de roue ?",
                    "answerOptions": [
                        {"text": "Lorsque la roue est en l'air (sur cric).", "isCorrect": False},
                        {"text": "Lorsque le véhicule est encore au sol (roues au contact).", "isCorrect": True},
                        {"text": "Lorsque le moteur tourne.", "isCorrect": False},
                        {"text": "Lorsque les freins sont desserrés.", "isCorrect": False}
                    ],
                    "correction": "Le desserrage initial (et le serrage final) doit toujours se faire avec le véhicule **au sol** pour que le couple de serrage puisse être appliqué sans faire tourner la roue."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est l'objectif du Plan de Nettoyage et de Désinfection (PND) en atelier ?",
                    "answerOptions": [
                        {"text": "Former les apprentis.", "isCorrect": False},
                        {"text": "Garantir un environnement de travail propre pour la santé et la sécurité du personnel et des clients.", "isCorrect": True},
                        {"text": "Calculer la TVA.", "isCorrect": False},
                        {"text": "Vendre des pièces détachées.", "isCorrect": False}
                    ],
                    "correction": "Le **PND** (souvent PHS - Plan d'Hygiène et de Sécurité en mécanique) est essentiel pour éviter les glissades (huile) et les contaminations (produits chimiques)."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le risque de verser de l'eau sur un moteur qui vient de s'arrêter (surchauffe) ?",
                    "answerOptions": [
                        {"text": "Une panne électrique.", "isCorrect": False},
                        {"text": "Un choc thermique qui peut provoquer la fissure de la culasse ou du bloc moteur (déformation brutale).", "isCorrect": True},
                        {"text": "Une fuite de carburant.", "isCorrect": False},
                        {"text": "Un problème de suspension.", "isCorrect": False}
                    ],
                    "correction": "Le refroidissement doit être **progressif**. L'eau froide sur un métal très chaud provoque un choc thermique violent et irréversible."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel document légal doit être fourni au client après une réparation (selon le Code de la Consommation) ?",
                    "answerOptions": [
                        {"text": "Le bulletin météo.", "isCorrect": False},
                        {"text": "La facture détaillée (pièces, main d'œuvre, TVA).", "isCorrect": True},
                        {"text": "Un ticket de caisse simple.", "isCorrect": False},
                        {"text": "Un plan de salle.", "isCorrect": False}
                    ],
                    "correction": "La **facture** est une obligation légale. Elle doit être détaillée pour justifier le prix et sert de preuve pour la garantie des pièces et de l'intervention."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel risque peut engendrer le contact prolongé de l'huile moteur usagée avec la peau ?",
                    "answerOptions": [
                        {"text": "Une odeur agréable.", "isCorrect": False},
                        {"text": "Une irritation, des dermites, voire un risque d'affections cutanées graves (carcinogènes).", "isCorrect": True},
                        {"text": "Une baisse de la tension.", "isCorrect": False},
                        {"text": "Un choc électrique.", "isCorrect": False}
                    ],
                    "correction": "Le port de **gants de protection** est essentiel. L'huile usagée est chargée de résidus de combustion et de métaux lourds (déchets chimiques)."
                },
                {
                    "questionNumber": 93,
                    "question": "Qu'est-ce que la 'FDS' (Fiche de Données de Sécurité) et où doit-elle se trouver ?",
                    "answerOptions": [
                        {"text": "La fiche de fabrication de la voiture.", "isCorrect": False},
                        {"text": "Un document donnant les risques, les mesures de sécurité et le traitement des déchets pour un produit chimique (obligatoire en atelier).", "isCorrect": True},
                        {"text": "Le prix de la voiture.", "isCorrect": False},
                        {"text": "Le manuel d'utilisation.", "isCorrect": False}
                    ],
                    "correction": "Chaque produit chimique (huile, liquide de refroidissement, nettoyant) doit avoir sa **FDS**, consultable par les employés et les secours en cas d'accident."
                },
                {
                    "questionNumber": 94,
                    "question": "Pourquoi doit-on utiliser un outil de diagnostic pour réinitialiser le témoin d'entretien (voyant de vidange) sur les véhicules modernes ?",
                    "answerOptions": [
                        {"text": "Pour que le voyant soit éteint.", "isCorrect": False},
                        {"text": "Car la réinitialisation est gérée électroniquement par le calculateur (ECU) et non manuellement.", "isCorrect": True},
                        {"text": "Pour changer la couleur du voyant.", "isCorrect": False},
                        {"text": "Pour vidanger l'huile.", "isCorrect": False}
                    ],
                    "correction": "Les véhicules modernes gèrent l'entretien via l'**ECU**. La réinitialisation doit être faite via le port OBD pour informer le calculateur que l'entretien a été effectué."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le risque de réutiliser un joint de culasse après un démontage ?",
                    "answerOptions": [
                        {"text": "Il fonctionnera mieux.", "isCorrect": False},
                        {"text": "Le joint est 'écrasé' et déformé pour l'étanchéité. Sa réutilisation entraînera une fuite immédiate ou un mélange des fluides (eau/huile).", "isCorrect": True},
                        {"text": "Il sera trop petit.", "isCorrect": False},
                        {"text": "Il n'y a aucun risque.", "isCorrect": False}
                    ],
                    "correction": "Le **joint de culasse** est une pièce à usage unique. Il se déforme sous l'effet du couple de serrage et ne peut plus garantir l'étanchéité une seconde fois."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle précaution prendre avant d'utiliser une clé à chocs pneumatique ?",
                    "answerOptions": [
                        {"text": "S'assurer que la pression d'air est au minimum.", "isCorrect": False},
                        {"text": "Vérifier la pression d'air et s'assurer d'utiliser les douilles adaptées (douilles à chocs).", "isCorrect": True},
                        {"text": "Ne pas mettre de gants.", "isCorrect": False},
                        {"text": "Ne pas serrer de vis.", "isCorrect": False}
                    ],
                    "correction": "L'utilisation de **douilles à chocs** (plus résistantes) est impérative pour éviter la rupture de l'outil. Le bruit nécessite souvent le port de protections auditives."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le principal risque lié au liquide de refroidissement usagé ?",
                    "answerOptions": [
                        {"text": "Une mauvaise odeur.", "isCorrect": False},
                        {"text": "Sa toxicité (contient de l'éthylène glycol) et son impact environnemental, nécessitant une collecte et un traitement spécifiques.", "isCorrect": True},
                        {"text": "L'incendie.", "isCorrect": False},
                        {"text": "Le gel des mains.", "isCorrect": False}
                    ],
                    "correction": "Le **liquide de refroidissement** est toxique (surtout pour les animaux domestiques qui peuvent en boire en cas de fuite). Il est classé comme déchet dangereux."
                },
                {
                    "questionNumber": 98,
                    "question": "Que doit-on toujours faire après avoir utilisé un pont élévateur pour s'assurer qu'il est hors tension ?",
                    "answerOptions": [
                        {"text": "Le graisser.", "isCorrect": False},
                        {"text": "Remettre le véhicule au sol et couper le disjoncteur ou l'interrupteur général (selon les consignes).", "isCorrect": True},
                        {"text": "Le nettoyer avec de l'eau.", "isCorrect": False},
                        {"text": "Laisser la clé sur le tableau de bord.", "isCorrect": False}
                    ],
                    "correction": "Couper l'alimentation électrique (par un disjoncteur/interrupteur dédié) est une mesure de sécurité pour éviter une utilisation non autorisée ou un incident électrique."
                },
                {
                    "questionNumber": 99,
                    "question": "Qu'est-ce que la 'TVA' dans le prix d'une réparation ?",
                    "answerOptions": [
                        {"text": "Le Taux de Vidange Automobile.", "isCorrect": False},
                        {"text": "La Taxe sur la Valeur Ajoutée (impôt sur la consommation).", "isCorrect": True},
                        {"text": "La Température du Véhicule Automatique.", "isCorrect": False},
                        {"text": "Le Taux de Vitesse Acceptable.", "isCorrect": False}
                    ],
                    "correction": "La **TVA** est la Taxe sur la Valeur Ajoutée, appliquée à tous les produits et services (pièces, main d'œuvre). En mécanique, le taux normal est de 20%."
                },
                {
                    "questionNumber": 100,
                    "question": "Le terme 'FIFO' (First In, First Out) appliqué aux stocks de pièces et de liquides en atelier signifie :",
                    "answerOptions": [
                        {"text": "Ranger les nouvelles pièces devant.", "isCorrect": False},
                        {"text": "Utiliser les pièces (ou liquides) reçues en premier (les plus anciennes) avant les pièces plus récentes.", "isCorrect": True},
                        {"text": "Jeter toutes les pièces usagées.", "isCorrect": False},
                        {"text": "Travailler lentement.", "isCorrect": False}
                    ],
                    "correction": "Le **FIFO** garantit que les produits avec une date de péremption (huile, liquide, additifs) ou à durée de garantie limitée sont utilisés en premier, minimisant le gaspillage et l'obsolescence."
                },
            ]
        }
    }
}

# Exemple d'accès aux données :
# print(quiz_data["title"])
# print(quiz_data["themes"][1]["name"])
# print(quiz_data["themes"][1]["questions"][0]["question"])
# print(quiz_data["themes"][1]["questions"][0]["answerOptions"][1]["isCorrect"])