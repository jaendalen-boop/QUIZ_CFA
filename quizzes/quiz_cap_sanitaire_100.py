# Fichier : quiz_cap_sanitaire_100.py

quiz_data = {
    "title": "Quiz CAP Monteur en Installations Sanitaires : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : SÉCURITÉ, OUTILS ET MATÉRIAUX (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Sécurité, Outillage et Matériaux (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel Équipement de Protection Individuelle (EPI) est strictement requis lors de l'utilisation d'une meuleuse ou d'une perceuse ?",
                    "answerOptions": [
                        {"text": "Le casque de chantier.", "isCorrect": False},
                        {"text": "Les gants en latex.", "isCorrect": False},
                        {"text": "Les lunettes de protection (ou visière) et les chaussures de sécurité (coquées).", "isCorrect": True},
                        {"text": "Le gilet haute visibilité.", "isCorrect": False}
                    ],
                    "correction": "Les **lunettes** protègent des projections de débris et les **chaussures** protègent des chutes d'outils ou de matériaux."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel outil est spécifiquement utilisé pour créer un évasement (collet battu) à l'extrémité d'un tube de cuivre pour un raccordement (dit 'américain' ou 'à olive' sans olive) ?",
                    "answerOptions": [
                        {"text": "La cintreuse.", "isCorrect": False},
                        {"text": "La Pince à évasement (ou Évaseur / Outil à collet battu).", "isCorrect": True},
                        {"text": "Le coupe-tube.", "isCorrect": False},
                        {"text": "La filière.", "isCorrect": False}
                    ],
                    "correction": "L'**Évaseur** déforme le cuivre pour créer une surface d'étanchéité conique (sans brasure)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la température minimale (en °C) pour réaliser une **Brasure Forte** sur le cuivre (obligatoire pour le gaz et certains usages sous haute pression) ?",
                    "answerOptions": [
                        {"text": "Inférieure à 350 °C (Brasure tendre).", "isCorrect": False},
                        {"text": "Inférieure à 450 °C.", "isCorrect": False},
                        {"text": "Supérieure ou égale à 450 °C.", "isCorrect": True},
                        {"text": "Supérieure à 600 °C.", "isCorrect": False}
                    ],
                    "correction": "La **Brasure forte** (> 450 °C) est plus résistante que la brasure tendre (< 450 °C) qui utilise de l'étain."
                },
                {
                    "questionNumber": 4,
                    "question": "Que représente le sigle **PVC** utilisé pour les tuyaux d'évacuation ?",
                    "answerOptions": [
                        {"text": "Plastique Vert Comprimé.", "isCorrect": False},
                        {"text": "Polyéthylène à Ventilation Contrôlée.", "isCorrect": False},
                        {"text": "Polychlorure de Vinyle (tube le plus courant pour les évacuations des eaux usées et pluviales).", "isCorrect": True},
                        {"text": "Polypropylène de Visserie Cuivrée.", "isCorrect": False}
                    ],
                    "correction": "Le **PVC** est léger, facile à coller et résistant à la corrosion."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le rôle du **Décapant (Flux)** dans le processus de brasure du cuivre ?",
                    "answerOptions": [
                        {"text": "Fournir la chaleur nécessaire.", "isCorrect": False},
                        {"text": "Nettoyer et protéger de l'oxydation la surface à braser pour garantir la capillarité et l'adhérence du métal d'apport.", "isCorrect": True},
                        {"text": "Refroidir le raccord rapidement.", "isCorrect": False},
                        {"text": "Servir de joint mécanique.", "isCorrect": False}
                    ],
                    "correction": "Le **Flux** est indispensable pour que le métal d'apport (baguette) coule correctement par capillarité."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est l'outil utilisé pour nettoyer et s'assurer que le tube PER ou Multicouche conserve une forme parfaitement ronde avant le sertissage ?",
                    "answerOptions": [
                        {"text": "La lime.", "isCorrect": False},
                        {"text": "Le Calibreur-Ébavureur.", "isCorrect": True},
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "Le mètre ruban.", "isCorrect": False}
                    ],
                    "correction": "Le **Calibreur** garantit un bon emboîtement et donc l'étanchéité du joint torique à l'intérieur du raccord à sertir."
                },
                {
                    "questionNumber": 7,
                    "question": "Dans le cas d'une brasure forte (cuivre) ou d'une soudure (acier), pourquoi est-il dangereux de travailler sans système de ventilation adéquat ?",
                    "answerOptions": [
                        {"text": "Le raccord chaufferait trop.", "isCorrect": False},
                        {"text": "Les fumées générées (oxydes métalliques, gaz brûlés) sont toxiques et peuvent entraîner des problèmes respiratoires graves.", "isCorrect": True},
                        {"text": "La flamme s'éteindrait.", "isCorrect": False},
                        {"text": "Le tube gèlerait.", "isCorrect": False}
                    ],
                    "correction": "Une **bonne ventilation** et l'utilisation de masques adaptés sont essentielles en soudure et brasure."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est l'inconvénient principal des raccords à compression (bicône ou olive) sur le cuivre par rapport à la brasure ?",
                    "answerOptions": [
                        {"text": "Ils sont plus jolis.", "isCorrect": False},
                        {"text": "Ils sont moins résistants aux vibrations, sont plus sensibles au couple de serrage et ne peuvent pas être noyés dans la dalle/cloison (non encastrables).", "isCorrect": True},
                        {"text": "Ils sont trop légers.", "isCorrect": False},
                        {"text": "Ils ne peuvent pas supporter l'eau chaude.", "isCorrect": False}
                    ],
                    "correction": "Les **Raccords à compression** sont démontables et ne doivent pas être cachés."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel type de tube est caractérisé par une âme interne en aluminium, pris en sandwich entre deux couches de Polyéthylène Réticulé ?",
                    "answerOptions": [
                        {"text": "Le tube PVC.", "isCorrect": False},
                        {"text": "Le Tube Multicouche.", "isCorrect": True},
                        {"text": "Le tube Cuivre.", "isCorrect": False},
                        {"text": "Le tube PER.", "isCorrect": False}
                    ],
                    "correction": "Le **Multicouche** combine la flexibilité du PER et la stabilité/barrière anti-oxygène de l'aluminium."
                },
                {
                    "questionNumber": 10,
                    "question": "Lors du raccordement d'un tube PVC (évacuation), quel est le rôle de la **colle PVC** ?",
                    "answerOptions": [
                        {"text": "Rendre le raccord démontable.", "isCorrect": False},
                        {"text": "Créer une soudure chimique (fusion) entre les surfaces du tube et du manchon pour garantir l'étanchéité absolue du raccord.", "isCorrect": True},
                        {"text": "Nettoyer le PVC.", "isCorrect": False},
                        {"text": "Réduire le bruit.", "isCorrect": False}
                    ],
                    "correction": "La **Colle PVC** est un ciment solvant qui rend le raccord permanent et étanche."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est l'outil utilisé pour cintrer les tubes de cuivre ou d'acier de grand diamètre (en plomberie industrielle) ?",
                    "answerOptions": [
                        {"text": "La cintreuse manuelle à ressort.", "isCorrect": False},
                        {"text": "La Cintreuse hydraulique ou électrique (à matrice et patin).", "isCorrect": True},
                        {"text": "La pince à sertir.", "isCorrect": False},
                        {"text": "La filière.", "isCorrect": False}
                    ],
                    "correction": "Les **Cintreuses hydrauliques** sont nécessaires pour appliquer la force requise sur les gros diamètres sans écraser le tube."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle doit être la largeur de la **Bande de désolidarisation** périphérique dans un logement (pour un plancher chauffant ou une chape de bain) ?",
                    "answerOptions": [
                        {"text": "1 mm.", "isCorrect": False},
                        {"text": "Au moins 5 mm (pour absorber la dilatation de la chape ou de la dalle lors des variations thermiques).", "isCorrect": True},
                        {"text": "10 cm.", "isCorrect": False},
                        {"text": "2 cm.", "isCorrect": False}
                    ],
                    "correction": "La **Bande de désolidarisation** est vitale pour éviter les fissures de la chape."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est l'outil utilisé pour créer un filetage (pas de vis) à l'extrémité d'un tube en acier galvanisé ?",
                    "answerOptions": [
                        {"text": "La meuleuse.", "isCorrect": False},
                        {"text": "La Filière (ou Machine à fileter).", "isCorrect": True},
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "Le coupe-tube.", "isCorrect": False}
                    ],
                    "correction": "La **Filière** est indispensable pour les raccordements vissés (raccord unions, manchons, etc.) sur acier."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est l'avantage du tube en **Cuivre** par rapport au PER ou Multicouche ?",
                    "answerOptions": [
                        {"text": "Il est plus facile à installer.", "isCorrect": False},
                        {"text": "Il a une meilleure résistance au feu, est entièrement recyclable et a une grande rigidité (auto-portance).", "isCorrect": True},
                        {"text": "Il est moins cher.", "isCorrect": False},
                        {"text": "Il ne conduit pas la chaleur.", "isCorrect": False}
                    ],
                    "correction": "Le **Cuivre** reste un matériau de référence pour sa longévité et sa résistance."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est le risque de ne pas utiliser le bon **lubrifiant** lors de l'emboîtement des tubes PVC (raccords à joint) ?",
                    "answerOptions": [
                        {"text": "Le raccord va coller.", "isCorrect": False},
                        {"text": "Le joint en caoutchouc risque de se tordre ou de se déchirer lors de l'emboîtement, entraînant une fuite.", "isCorrect": True},
                        {"text": "Le tube va fondre.", "isCorrect": False},
                        {"text": "La colle ne tiendra pas.", "isCorrect": False}
                    ],
                    "correction": "Le **Lubrifiant** (souvent de l'eau savonneuse ou un produit spécifique) facilite le glissement du joint."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le rôle du **Manchon isolant (calorifugeage)** sur les tubes d'Eau Chaude Sanitaire (ECS) ?",
                    "answerOptions": [
                        {"text": "Protéger contre le gel uniquement.", "isCorrect": False},
                        {"text": "Limiter au maximum les déperditions de chaleur et éviter le refroidissement de l'eau dans les tuyaux.", "isCorrect": True},
                        {"text": "Réduire la pression.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité.", "isCorrect": False}
                    ],
                    "correction": "Le **Calorifugeage** est essentiel pour l'économie d'énergie et le confort."
                },
                {
                    "questionNumber": 17,
                    "question": "Qu'est-ce qu'une **Vanve d'arrêt 1/4 de tour** par rapport à une vanne à volant ?",
                    "answerOptions": [
                        {"text": "Elle prend plus de place.", "isCorrect": False},
                        {"text": "Elle permet une ouverture/fermeture rapide (90 degrés) et est souvent plus fiable que la vanne à clapet ou à tête, et plus simple à manipuler.", "isCorrect": True},
                        {"text": "Elle ne peut être utilisée que sur l'eau chaude.", "isCorrect": False},
                        {"text": "Elle est réservée à la haute pression.", "isCorrect": False}
                    ],
                    "correction": "La **Vanne 1/4 de tour** (ou vanne à boisseau sphérique) est la plus courante en plomberie moderne."
                },
                {
                    "questionNumber": 18,
                    "question": "Lors d'une soudure/brasure, quel est le risque d'appliquer la flamme directement sur le métal d'apport (baguette) au lieu du tube et du raccord ?",
                    "answerOptions": [
                        {"text": "Le tube va se déformer.", "isCorrect": False},
                        {"text": "Le métal d'apport va fondre prématurément sans que le raccord soit à bonne température, il ne pourra pas pénétrer par capillarité (mauvaise soudure).", "isCorrect": True},
                        {"text": "Le raccord va geler.", "isCorrect": False},
                        {"text": "Le métal d'apport va coller.", "isCorrect": False}
                    ],
                    "correction": "Le tube doit être à la **température de fusion** du métal d'apport pour que la capillarité fonctionne."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le type de joint souvent utilisé pour les raccordements de gros diamètre (fonte ou PVC) qui permet une certaine flexibilité et un assemblage rapide ?",
                    "answerOptions": [
                        {"text": "Le joint Téflon.", "isCorrect": False},
                        {"text": "Le Joint à lèvre ou Joint à collerette (caoutchouc).", "isCorrect": True},
                        {"text": "Le joint chanvre.", "isCorrect": False},
                        {"text": "Le joint soudé.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint à lèvre** est très utilisé dans les évacuations pour faciliter l'assemblage."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est la principale caractéristique des tubes **Hydrocablés** (ou gainés) en PER ou Multicouche ?",
                    "answerOptions": [
                        {"text": "Ils sont plus rigides.", "isCorrect": False},
                        {"text": "Ils sont protégés par une gaine (souvent rouge pour l'eau chaude et bleue pour l'eau froide) et peuvent être changés sans casser la dalle/cloison (non encastrables).", "isCorrect": True},
                        {"text": "Ils ne transportent que l'eau froide.", "isCorrect": False},
                        {"text": "Ils sont plus légers.", "isCorrect": False}
                    ],
                    "correction": "La **Gaine** rend le tube remplaçable et le protège du contact direct avec la chape."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : DISTRIBUTION D'EAU POTABLE (AEP) (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Distribution d'Eau Potable (AEP) et Raccordements (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Comment appelle-t-on le dispositif qui limite la pression d'eau froide à l'entrée de l'habitation pour protéger les appareils (chaudière, chauffe-eau, etc.) ?",
                    "answerOptions": [
                        {"text": "Le manomètre.", "isCorrect": False},
                        {"text": "Le Détendeur-réducteur de pression.", "isCorrect": True},
                        {"text": "Le compteur d'eau.", "isCorrect": False},
                        {"text": "Le filtre à tamis.", "isCorrect": False}
                    ],
                    "correction": "Le **Détendeur** est essentiel si la pression du réseau public est supérieure à 3-4 bars."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est le rôle du **Disconnecteur (ou Clapet anti-retour)** installé après le compteur d'eau et avant le remplissage du circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Filtrer le calcaire.", "isCorrect": False},
                        {"text": "Empêcher le retour d'eau du réseau privé (potentiellement contaminée) vers le réseau public d'eau potable.", "isCorrect": True},
                        {"text": "Réguler le débit.", "isCorrect": False},
                        {"text": "Vidanger le circuit.", "isCorrect": False}
                    ],
                    "correction": "Le **Disconnecteur** est une sécurité sanitaire obligatoire."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la règle de pose à respecter concernant les croisements entre les tubes d'eau froide (EF) et les tubes d'eau chaude (EC) ?",
                    "answerOptions": [
                        {"text": "L'eau froide doit toujours passer au-dessus de l'eau chaude (et isoler les deux).", "isCorrect": True},
                        {"text": "L'eau chaude doit toujours passer au-dessus de l'eau froide.", "isCorrect": False},
                        {"text": "Ils peuvent se toucher sans isolation.", "isCorrect": False},
                        {"text": "Ils ne doivent jamais se croiser.", "isCorrect": False}
                    ],
                    "correction": "L'**EF au-dessus de l'EC** et l'**isolation** sont nécessaires pour éviter les transferts thermiques et la surchauffe de l'EF (risque de légionellose)."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle de la **Fibre de chanvre** (avec de la pâte à joint) ou du **Téflon (PTFE)** sur un raccordement fileté ?",
                    "answerOptions": [
                        {"text": "Transporter l'eau.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité du raccord vissé en comblant les filets de vis et en résistant à la pression.", "isCorrect": True},
                        {"text": "Isoler thermiquement.", "isCorrect": False},
                        {"text": "Réduire le bruit.", "isCorrect": False}
                    ],
                    "correction": "Le **Chanvre** et le **Téflon** sont des matériaux d'étanchéité standards, appliqués dans le sens du vissage."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le rôle du **Collecteur (ou Nourrice)** dans une distribution en Pieuvre (PER/Multicouche) ?",
                    "answerOptions": [
                        {"text": "Stocker l'eau.", "isCorrect": False},
                        {"text": "Distribuer l'eau (EF et EC) vers chaque point de puisage (robinet, WC, douche) via un tube dédié (sans raccord caché).", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Réguler la pression.", "isCorrect": False}
                    ],
                    "correction": "Le **Collecteur** centralise les départs et les vannes d'arrêt pour une maintenance facile. "
                },
                {
                    "questionNumber": 26,
                    "question": "Comment appelle-t-on le phénomène physique qui génère un bruit violent (coup de bélier) dans la tuyauterie lorsque l'on ferme rapidement un robinet (mitigeur) ?",
                    "answerOptions": [
                        {"text": "La cavitation.", "isCorrect": False},
                        {"text": "Le Coup de bélier (augmentation brutale de la pression due à l'arrêt soudain de la vitesse de l'eau).", "isCorrect": True},
                        {"text": "La dilatation.", "isCorrect": False},
                        {"text": "L'osmose.", "isCorrect": False}
                    ],
                    "correction": "Le **Coup de bélier** est atténué par un réducteur de pression ou par un antibélier."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la fonction d'un **Clapet anti-pollution (NF)** ?",
                    "answerOptions": [
                        {"text": "Empêcher le calcaire.", "isCorrect": False},
                        {"text": "Protèger le réseau d'eau potable contre les retours d'eau contaminée depuis un appareil (ex : machine à laver, robinet de jardin immergé).", "isCorrect": True},
                        {"text": "Isoler le circuit.", "isCorrect": False},
                        {"text": "Réguler la température.", "isCorrect": False}
                    ],
                    "correction": "Le **Clapet anti-pollution** est une sécurité sanitaire essentielle."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le diamètre intérieur (ou nominal) minimum généralement requis pour l'alimentation d'une colonne montante principale d'habitation (selon DTU) ?",
                    "answerOptions": [
                        {"text": "8 mm.", "isCorrect": False},
                        {"text": "12 mm.", "isCorrect": False},
                        {"text": "Au moins 16 mm (1/2 pouce) ou 20 mm (3/4 pouce) pour garantir un débit suffisant aux usages simultanés.", "isCorrect": True},
                        {"text": "32 mm.", "isCorrect": False}
                    ],
                    "correction": "Un diamètre trop petit entraînerait une chute de pression et des débits insuffisants lors de plusieurs puisages simultanés."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le risque de ne pas effectuer l'**ébavurage** (intérieur et extérieur) après la coupe d'un tube métallique ou synthétique ?",
                    "answerOptions": [
                        {"text": "Le tube va se cintrér.", "isCorrect": False},
                        {"text": "Les bavures peuvent entraîner une perte de charge, endommager les joints toriques lors du montage, ou se décrocher pour obstruer les appareils (mitigeurs).", "isCorrect": True},
                        {"text": "L'eau va geler.", "isCorrect": False},
                        {"text": "La colle ne tiendra pas.", "isCorrect": False}
                    ],
                    "correction": "L'**Ébavurage** est une étape obligatoire pour la qualité de l'installation."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le rôle du **Robinet de puisage (ou Robinet de vidange)** placé au point bas de l'installation ?",
                    "answerOptions": [
                        {"text": "Mesurer le débit.", "isCorrect": False},
                        {"text": "Permettre la vidange complète et facile de l'ensemble du réseau (en cas de gel ou d'intervention lourde).", "isCorrect": True},
                        {"text": "Réguler la pression.", "isCorrect": False},
                        {"text": "Purger l'air.", "isCorrect": False}
                    ],
                    "correction": "Le **Robinet de vidange** est crucial pour la maintenance et la protection contre le gel."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment appelle-t-on le raccord utilisé pour dériver un tube (créer un angle de 90°) dans une distribution en ligne ?",
                    "answerOptions": [
                        {"text": "Le manchon.", "isCorrect": False},
                        {"text": "Le Coude (ou Coude à 90°, Coude à 45°).", "isCorrect": True},
                        {"text": "Le té.", "isCorrect": False},
                        {"text": "Le bouchon.", "isCorrect": False}
                    ],
                    "correction": "Le **Coude** est le raccord de base pour les changements de direction."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le risque de ne pas laisser de **jeu de dilatation** suffisant (colliers trop serrés) sur une longue ligne droite de tube PER/Multicouche ?",
                    "answerOptions": [
                        {"text": "Le tube va rouiller.", "isCorrect": False},
                        {"text": "Le tube se déforme, ondule ou, en cas de confinement, peut générer des bruits de claquement lors des variations de température.", "isCorrect": True},
                        {"text": "Le tube gèle.", "isCorrect": False},
                        {"text": "Le tube fuit.", "isCorrect": False}
                    ],
                    "correction": "Les tubes plastiques ont un coefficient de dilatation élevé. Il faut laisser les tubes 'glisser'."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le risque majeur de laisser un raccord non bradé ou non serti, noyé dans la dalle ou la cloison ?",
                    "answerOptions": [
                        {"text": "Le raccord gèle.", "isCorrect": False},
                        {"text": "Un risque de fuite inaccessible et non réparable sans casser le revêtement ou la structure.", "isCorrect": True},
                        {"text": "Le raccord rouille.", "isCorrect": False},
                        {"text": "Le raccord fait du bruit.", "isCorrect": False}
                    ],
                    "correction": "Seuls les **raccords soudés ou sertis NF** peuvent être encastrés. Les raccords mécaniques (compression, bicône, à visser) sont interdits."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le rôle d'un **Joint plat (fibre ou caoutchouc)** dans un raccord de vidange (ex : siphon, raccord WC) ?",
                    "answerOptions": [
                        {"text": "Filtrer les impuretés.", "isCorrect": False},
                        {"text": "Créer l'étanchéité entre deux surfaces plates (raccords démontables) par simple compression mécanique (serrage).", "isCorrect": True},
                        {"text": "Réguler la pression.", "isCorrect": False},
                        {"text": "Isoler thermiquement.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint plat** est idéal pour les raccords qui doivent pouvoir être démontés facilement."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment doit-on serrer un raccord fileté étanché avec du chanvre ?",
                    "answerOptions": [
                        {"text": "Serrer à la main.", "isCorrect": False},
                        {"text": "Serrer fermement avec des clés (clé à molette, clé à griffe) pour compresser le chanvre, sans forcer excessivement pour ne pas fendre le raccord.", "isCorrect": True},
                        {"text": "Serrer au couplemètre.", "isCorrect": False},
                        {"text": "Serrer puis desserrer d'un quart de tour.", "isCorrect": False}
                    ],
                    "correction": "Le **Chanvre** nécessite une bonne compression pour garantir l'étanchéité."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le raccord utilisé pour connecter un tube en cuivre à un tube en acier (raccordement hétérogène) tout en évitant la corrosion (phénomène de couple galvanique) ?",
                    "answerOptions": [
                        {"text": "Un té normal.", "isCorrect": False},
                        {"text": "Un Raccord diélectrique (ou Raccord isolant).", "isCorrect": True},
                        {"text": "Un manchon en PVC.", "isCorrect": False},
                        {"text": "Un raccord soudé.", "isCorrect": False}
                    ],
                    "correction": "Le **Raccord diélectrique** sépare électriquement les deux métaux pour éviter l'oxydation rapide de l'acier au contact du cuivre."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle est l'exigence de la norme DTU concernant l'isolation acoustique des tuyauteries dans les bâtiments collectifs ?",
                    "answerOptions": [
                        {"text": "Il n'y a aucune exigence.", "isCorrect": False},
                        {"text": "Les tuyaux doivent être isolés pour prévenir la transmission du bruit (eau qui coule, coup de bélier) à travers les planchers et les murs.", "isCorrect": True},
                        {"text": "Seuls les tubes ECS sont concernés.", "isCorrect": False},
                        {"text": "Les tubes doivent être rigides.", "isCorrect": False}
                    ],
                    "correction": "L'**Isolation phonique** est cruciale (utilisation de colliers isophoniques, gainage) pour le confort des occupants."
                },
                {
                    "questionNumber": 38,
                    "question": "Que signifie le marquage **AC S** sur un raccord, un robinet ou un flexible de plomberie ?",
                    "answerOptions": [
                        {"text": "Anti-Calcaire Sécurité.", "isCorrect": False},
                        {"text": "Attestation de Conformité Sanitaire (garantie que le matériau n'altère pas la qualité de l'eau potable).", "isCorrect": True},
                        {"text": "Acier et Cuivre Standard.", "isCorrect": False},
                        {"text": "Aller-Retour Séparé.", "isCorrect": False}
                    ],
                    "correction": "L'**ACS** est un label obligatoire pour tout produit en contact avec l'eau potable en France."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le risque de couper un tube de cuivre avec une **scie à métaux** plutôt qu'un coupe-tube ?",
                    "answerOptions": [
                        {"text": "Le tube est moins brillant.", "isCorrect": False},
                        {"text": "La scie déforme le tube et laisse un important bord intérieur (bavure) difficile à ébavurer et source de perte de charge.", "isCorrect": True},
                        {"text": "Le tube sera trop chaud.", "isCorrect": False},
                        {"text": "Le tube sera trop long.", "isCorrect": False}
                    ],
                    "correction": "Le **Coupe-tube** assure une coupe perpendiculaire et une bavure minimale."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment appelle-t-on le dispositif qui permet de raccorder l'eau au WC ou au lave-linge, qui intègre un robinet d'arrêt et un clapet anti-retour ?",
                    "answerOptions": [
                        {"text": "La vanne d'arrêt principale.", "isCorrect": False},
                        {"text": "Le Robinet d'équerre avec raccord union (ou Robinet de machine/WC).", "isCorrect": True},
                        {"text": "Le détendeur.", "isCorrect": False},
                        {"text": "Le manomètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Robinet d'équerre** est le point de raccordement final et permet d'isoler l'appareil facilement."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : APPAREILS SANITAIRES ET ROBINETTERIE (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Appareils Sanitaires et Robinetterie (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le rôle du **Mousseur/Aérateur** situé à l'extrémité d'un robinet ?",
                    "answerOptions": [
                        {"text": "Augmenter la pression.", "isCorrect": False},
                        {"text": "Mélanger l'eau et l'air pour un jet doux, et réduire le débit d'eau sans impacter la sensation de jet (économies d'eau).", "isCorrect": True},
                        {"text": "Filtrer les impuretés.", "isCorrect": False},
                        {"text": "Arrêter le débit.", "isCorrect": False}
                    ],
                    "correction": "Le **Mousseur** est un élément d'économie d'eau et de confort."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est l'avantage principal d'un **WC suspendu** par rapport à un WC à poser ?",
                    "answerOptions": [
                        {"text": "Il consomme moins d'eau.", "isCorrect": False},
                        {"text": "Il facilite le nettoyage au sol (pas de pied) et dissimule la chasse d'eau et la tuyauterie (esthétique).", "isCorrect": True},
                        {"text": "Il est moins cher à l'achat.", "isCorrect": False},
                        {"text": "Il est plus rapide à installer.", "isCorrect": False}
                    ],
                    "correction": "Le **WC suspendu** est monté sur un bâti-support, nécessitant une installation plus complexe mais offrant une finition supérieure."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la principale fonction d'un **Mitigeur Thermostatique (douche/baignoire)** ?",
                    "answerOptions": [
                        {"text": "Réguler le débit.", "isCorrect": False},
                        {"text": "Maintenir la température de l'eau demandée constante, quelles que soient les variations de pression ou de température du réseau EF/EC.", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Empêcher le calcaire.", "isCorrect": False}
                    ],
                    "correction": "Le **Thermostatique** offre un grand confort et une sécurité (butée anti-brûlure à 38°C)."
                },
                {
                    "questionNumber": 44,
                    "question": "Comment appelle-t-on la hauteur minimale de protection (en mm) entre le niveau maximal de l'eau et le bord d'un appareil sanitaire (ex : un lavabo ou une chasse de WC) ?",
                    "answerOptions": [
                        {"text": "La hauteur utile.", "isCorrect": False},
                        {"text": "La Garde d'air (ou protection contre le refoulement).", "isCorrect": True},
                        {"text": "La hauteur de pose.", "isCorrect": False},
                        {"text": "Le niveau de sécurité.", "isCorrect": False}
                    ],
                    "correction": "La **Garde d'air** prévient la pollution de l'eau potable par un reflux d'eau contaminée de l'appareil."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le rôle du **Flotteur** dans le mécanisme de chasse d'eau d'un WC ?",
                    "answerOptions": [
                        {"text": "Déclencher la chasse.", "isCorrect": False},
                        {"text": "Contrôler le niveau de remplissage de la cuve et couper l'arrivée d'eau lorsqu'il est atteint (soupape à flotteur).", "isCorrect": True},
                        {"text": "Empêcher le bruit.", "isCorrect": False},
                        {"text": "Évacuer l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Flotteur** régule l'arrivée d'eau dans le réservoir."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le risque de ne pas respecter l'**alignement horizontal** lors de la pose d'un mitigeur mural (ex : dans une douche) ?",
                    "answerOptions": [
                        {"text": "L'eau sera trop chaude.", "isCorrect": False},
                        {"text": "Le raccordement avec le mitigeur sera difficile voire impossible, ou le mitigeur ne sera pas droit (esthétique et étanchéité compromises).", "isCorrect": True},
                        {"text": "La pression baisse.", "isCorrect": False},
                        {"text": "Le flexible fuit.", "isCorrect": False}
                    ],
                    "correction": "Le respect du **niveau et de l'entraxe** (distance entre les deux arrivées EF/EC) est essentiel pour la robinetterie murale."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on le dispositif situé sous l'évier qui permet de filtrer et retenir les graisses et les gros déchets (utilisé en restauration) ?",
                    "answerOptions": [
                        {"text": "Le siphon.", "isCorrect": False},
                        {"text": "Le Bac dégraisseur (ou Séparateur de graisses).", "isCorrect": True},
                        {"text": "Le té de visite.", "isCorrect": False},
                        {"text": "Le détendeur.", "isCorrect": False}
                    ],
                    "correction": "Le **Bac dégraisseur** est un regard essentiel pour le prétraitement des eaux usées de cuisine avant rejet."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la hauteur standard recommandée (en France) pour l'alimentation en eau d'un lavabo (mitigeur sur plage) ?",
                    "answerOptions": [
                        {"text": "30 cm du sol fini.", "isCorrect": False},
                        {"text": "Entre 50 cm et 60 cm (pour la partie EF/EC), l'appareil étant posé à 85-90 cm.", "isCorrect": True},
                        {"text": "120 cm du sol fini.", "isCorrect": False},
                        {"text": "10 cm du sol fini.", "isCorrect": False}
                    ],
                    "correction": "La **Hauteur d'alimentation** varie selon le type d'appareil (lavabo, douche, évier, etc.)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le rôle du **Té de visite (ou tampon de visite)** sur une colonne de chute (évacuation) ?",
                    "answerOptions": [
                        {"text": "Réguler le débit.", "isCorrect": False},
                        {"text": "Permettre l'accès à la canalisation (ouverture) pour l'inspection, le débouchage ou le curage en cas d'obstruction.", "isCorrect": True},
                        {"text": "Purger l'air.", "isCorrect": False},
                        {"text": "Réduire la pente.", "isCorrect": False}
                    ],
                    "correction": "Le **Té de visite** est obligatoire à des intervalles réguliers sur les longues colonnes."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle est la cause la plus fréquente d'une **fuite** au niveau du raccordement d'un flexible de douche ?",
                    "answerOptions": [
                        {"text": "Le flexible est trop long.", "isCorrect": False},
                        {"text": "Le joint caoutchouc plat (situé à l'intérieur de l'écrou) est manquant, endommagé ou mal positionné.", "isCorrect": True},
                        {"text": "La pression est trop basse.", "isCorrect": False},
                        {"text": "L'eau est trop chaude.", "isCorrect": False}
                    ],
                    "correction": "Pour un flexible, c'est le **joint plat** qui assure l'étanchéité, pas le serrage du filetage lui-même."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est l'élément qui permet d'ajuster le niveau d'une baignoire ou d'un receveur de douche sur un sol irrégulier ?",
                    "answerOptions": [
                        {"text": "La colle.", "isCorrect": False},
                        {"text": "Les Pieds réglables (ou Vérins).", "isCorrect": True},
                        {"text": "Le siphon.", "isCorrect": False},
                        {"text": "Le mastic.", "isCorrect": False}
                    ],
                    "correction": "Les **Pieds réglables** sont essentiels pour l'horizontalité et la bonne évacuation de l'eau."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment appelle-t-on le type de raccordement utilisé pour un lavabo mural sans colonne, où la tuyauterie est cachée derrière une cloison (ou un cache) ?",
                    "answerOptions": [
                        {"text": "Raccordement apparent.", "isCorrect": False},
                        {"text": "Raccordement encastré (ou dissimulé).", "isCorrect": True},
                        {"text": "Raccordement à visser.", "isCorrect": False},
                        {"text": "Raccordement par capillarité.", "isCorrect": False}
                    ],
                    "correction": "Le **Raccordement encastré** offre une finition esthétique mais impose l'utilisation de raccords certifiés pour être noyés."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le risque de ne pas installer un **Clapet anti-retour** sur la pompe de relevage des eaux usées ?",
                    "answerOptions": [
                        {"text": "La pompe chauffe.", "isCorrect": False},
                        {"text": "L'eau relevée redescend dans la cuve lorsque la pompe s'arrête, ce qui la fait redémarrer inutilement (risque de surchauffe/casse).", "isCorrect": True},
                        {"text": "L'eau gèle.", "isCorrect": False},
                        {"text": "L'eau déborde.", "isCorrect": False}
                    ],
                    "correction": "Le **Clapet anti-retour** empêche le reflux et protège la pompe."
                },
                {
                    "questionNumber": 54,
                    "question": "Comment s'appelle l'ouverture située sur le receveur de douche ou la baignoire qui permet l'évacuation d'urgence de l'eau en cas de siphon bouché (pour éviter le débordement) ?",
                    "answerOptions": [
                        {"text": "La bonde.", "isCorrect": False},
                        {"text": "Le Trop-plein.", "isCorrect": True},
                        {"text": "La grille.", "isCorrect": False},
                        {"text": "L'aérateur.", "isCorrect": False}
                    ],
                    "correction": "Le **Trop-plein** est une sécurité obligatoire sur la plupart des appareils sanitaires."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le type de joint souvent utilisé pour assurer l'étanchéité entre la baignoire/receveur et la faïence murale ?",
                    "answerOptions": [
                        {"text": "Joint Téflon.", "isCorrect": False},
                        {"text": "Joint silicone (mastic d'étanchéité souple, résistant à l'eau et à la moisissure).", "isCorrect": True},
                        {"text": "Joint chanvre.", "isCorrect": False},
                        {"text": "Joint soudé.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint silicone** est flexible et étanche, mais il doit être refait régulièrement."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le risque principal d'utiliser des **Flexibles de raccordement** trop longs et vrillés (tordus) ?",
                    "answerOptions": [
                        {"text": "Ils font du bruit.", "isCorrect": False},
                        {"text": "Ils réduisent le débit (perte de charge), augmentent le risque de fuite et de rupture à long terme.", "isCorrect": True},
                        {"text": "Ils rouillent.", "isCorrect": False},
                        {"text": "Ils attirent les impuretés.", "isCorrect": False}
                    ],
                    "correction": "Les **Flexibles** doivent être montés sans torsion et avec une courbe de cintrage naturelle."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment s'appelle le robinet qui mélange l'eau chaude et l'eau froide avec une seule commande (manette) et qui est le plus courant aujourd'hui ?",
                    "answerOptions": [
                        {"text": "Le robinet simple.", "isCorrect": False},
                        {"text": "Le Mitigeur (ou Mitigeur simple commande).", "isCorrect": True},
                        {"text": "Le mélangeur.", "isCorrect": False},
                        {"text": "Le thermostatique.", "isCorrect": False}
                    ],
                    "correction": "Le **Mitigeur** est simple d'utilisation et est souvent équipé d'une cartouche céramique pour le contrôle du débit et de la température."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le rôle du **Clapet anti-vide (ou Aérateur à membrane)** sur la colonne de chute des évacuations ?",
                    "answerOptions": [
                        {"text": "Empêcher le bruit.", "isCorrect": False},
                        {"text": "Faire entrer l'air pour compenser une dépression et éviter le désiphonnage des appareils sanitaires (l'aspiration des gardes d'eau).", "isCorrect": True},
                        {"text": "Empêcher l'eau de couler.", "isCorrect": False},
                        {"text": "Réguler la pente.", "isCorrect": False}
                    ],
                    "correction": "L'**Aérateur à membrane** permet une ventilation de la colonne sans sortie en toiture (sous conditions strictes)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle est l'exigence de la norme NF C 15-100 concernant la protection électrique dans la salle de bain (volumes de sécurité) ?",
                    "answerOptions": [
                        {"text": "Les prises peuvent être partout.", "isCorrect": False},
                        {"text": "La salle de bain est divisée en volumes (0, 1, 2, 3), et l'installation de prises ou d'appareils électriques (chauffe-eau, chauffage) est strictement réglementée pour éviter les risques d'électrocution.", "isCorrect": True},
                        {"text": "Seul le volume 0 est dangereux.", "isCorrect": False},
                        {"text": "Tous les appareils doivent être sur batterie.", "isCorrect": False}
                    ],
                    "correction": "Le **respect des volumes** est fondamental pour la sécurité de l'installation électrique et sanitaire."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment s'appelle l'élément qui permet de raccorder l'évacuation d'une douche/baignoire au siphon ?",
                    "answerOptions": [
                        {"text": "Le trop-plein.", "isCorrect": False},
                        {"text": "La Bonde (avec ou sans clapet, à grille, ou siphon de sol).", "isCorrect": True},
                        {"text": "Le té de visite.", "isCorrect": False},
                        {"text": "Le réducteur.", "isCorrect": False}
                    ],
                    "correction": "La **Bonde** est l'interface entre l'appareil et le siphon."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : ÉVACUATION ET VENTILATION (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Évacuation des Eaux Usées et Ventilation (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le rôle du **Siphon** dans une installation d'évacuation ?",
                    "answerOptions": [
                        {"text": "Accélérer l'écoulement.", "isCorrect": False},
                        {"text": "Maintenir en permanence une 'garde d'eau' (niveau d'eau stagnant) pour empêcher la remontée des odeurs nauséabondes (gaz d'égout) dans l'habitation.", "isCorrect": True},
                        {"text": "Filtrer les graisses.", "isCorrect": False},
                        {"text": "Réguler la pression.", "isCorrect": False}
                    ],
                    "correction": "Le **Siphon** (en P, S, ou bouteille) est l'organe essentiel de l'évacuation sanitaire. "
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la **pente minimale (en %)** à respecter pour l'évacuation des eaux usées horizontales (eaux vannes et eaux grises) ?",
                    "answerOptions": [
                        {"text": "0,5% (5 mm/m).", "isCorrect": False},
                        {"text": "1% (1 cm/m) à 3% (3 cm/m).", "isCorrect": True},
                        {"text": "5% (5 cm/m).", "isCorrect": False},
                        {"text": "10% (10 cm/m).", "isCorrect": False}
                    ],
                    "correction": "Une pente de **1 à 3%** est nécessaire pour garantir l'écoulement et l'auto-nettoyage de la canalisation."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on le dispositif qui assure le renouvellement permanent de l'air dans les pièces humides (cuisine, salle de bain, WC) ?",
                    "answerOptions": [
                        {"text": "Le climatiseur.", "isCorrect": False},
                        {"text": "La VMC (Ventilation Mécanique Contrôlée).", "isCorrect": True},
                        {"text": "Le déshumidificateur.", "isCorrect": False},
                        {"text": "Le radiateur.", "isCorrect": False}
                    ],
                    "correction": "La **VMC** est obligatoire pour l'hygiène et la conservation du bâtiment (lutte contre l'humidité et les moisissures)."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est le diamètre minimal généralement requis pour l'évacuation d'une douche ou d'un lavabo (eaux grises) ?",
                    "answerOptions": [
                        {"text": "20 mm.", "isCorrect": False},
                        {"text": "32 mm (lavabo, bidet) ou 40 mm (douche, baignoire).", "isCorrect": True},
                        {"text": "80 mm.", "isCorrect": False},
                        {"text": "100 mm.", "isCorrect": False}
                    ],
                    "correction": "Les diamètres varient selon l'appareil : 32/40 mm (eaux grises), 100 mm (eaux vannes/WC)."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le rôle du **Regard de visite (ou de branchement)** sur le réseau extérieur d'évacuation ?",
                    "answerOptions": [
                        {"text": "Stocker les eaux.", "isCorrect": False},
                        {"text": "Permettre le changement de direction des canalisations, la jonction avec le réseau public et l'accès pour l'inspection/débouchage.", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Réguler la pression.", "isCorrect": False}
                    ],
                    "correction": "Le **Regard** est un accès crucial pour l'entretien des canalisations enterrées."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on le tube d'évacuation vertical qui reçoit les eaux usées de plusieurs niveaux (WC, salle de bain, cuisine) ?",
                    "answerOptions": [
                        {"text": "La dérivation.", "isCorrect": False},
                        {"text": "La Colonne de chute (ou Chute des eaux usées).", "isCorrect": True},
                        {"text": "Le siphon.", "isCorrect": False},
                        {"text": "Le collecteur.", "isCorrect": False}
                    ],
                    "correction": "La **Colonne de chute** doit avoir un diamètre adapté (souvent 100 mm pour les eaux vannes)."
                },
                {
                    "questionNumber": 67,
                    "question": "Que risque-t-il de se passer si la pente des évacuations est **trop forte** (ex : 10%) ?",
                    "answerOptions": [
                        {"text": "Le siphon gèle.", "isCorrect": False},
                        {"text": "L'eau s'écoule trop vite, laissant les matières solides s'accumuler et créer un bouchon (non-auto-nettoyage).", "isCorrect": True},
                        {"text": "Le tube fuit.", "isCorrect": False},
                        {"text": "Le tube fait du bruit.", "isCorrect": False}
                    ],
                    "correction": "Une pente excessive est aussi nuisible qu'une pente insuffisante (DTU : 1% à 3%)."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle est la particularité d'une **VMC Hygroréglable** par rapport à une VMC standard ?",
                    "answerOptions": [
                        {"text": "Elle filtre l'air.", "isCorrect": False},
                        {"text": "Son débit d'air est ajusté automatiquement en fonction du taux d'humidité de l'air extrait (économie d'énergie).", "isCorrect": True},
                        {"text": "Elle est plus bruyante.", "isCorrect": False},
                        {"text": "Elle ne fonctionne que la nuit.", "isCorrect": False}
                    ],
                    "correction": "La **VMC Hygroréglable** est plus économe car elle ne ventile qu'en cas de besoin (douche, cuisine)."
                },
                {
                    "questionNumber": 69,
                    "question": "Comment appelle-t-on l'évacuation des eaux de pluie (EP) sur un toit ?",
                    "answerOptions": [
                        {"text": "Les égouts.", "isCorrect": False},
                        {"text": "La Gouttière et la Descente d'eaux pluviales (DEP).", "isCorrect": True},
                        {"text": "Le siphon de sol.", "isCorrect": False},
                        {"text": "Le regard de visite.", "isCorrect": False}
                    ],
                    "correction": "Les **Eaux pluviales** sont évacuées vers le réseau EP, séparément des eaux usées (EU) ou eaux vannes (EV)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le risque de raccorder un appareil (ex : machine à laver) directement sur une évacuation de WC (eaux vannes) ?",
                    "answerOptions": [
                        {"text": "Le raccord fuira.", "isCorrect": False},
                        {"text": "Les bactéries et les odeurs des eaux vannes pourraient remonter dans la machine, créant un risque sanitaire et olfactif (raccordement interdit).", "isCorrect": True},
                        {"text": "L'eau sera trop froide.", "isCorrect": False},
                        {"text": "La pression baisse.", "isCorrect": False}
                    ],
                    "correction": "Les **Eaux usées** (eaux grises : cuisine, douche, lave-linge) doivent être raccordées séparément ou après la colonne de chute des eaux vannes."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est l'élément essentiel à vérifier dans la **garde d'eau** d'un siphon pour s'assurer de sa bonne efficacité (anti-odeur) ?",
                    "answerOptions": [
                        {"text": "La température de l'eau.", "isCorrect": False},
                        {"text": "La Hauteur d'eau (qui doit être suffisante pour bloquer les gaz) et l'absence de fuite.", "isCorrect": True},
                        {"text": "Le débit d'eau.", "isCorrect": False},
                        {"text": "La couleur de l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le siphon doit toujours contenir une quantité d'eau suffisante (garde d'eau)."
                },
                {
                    "questionNumber": 72,
                    "question": "Comment s'appelle l'opération qui consiste à nettoyer et à déboucher une canalisation en utilisant un jet d'eau sous haute pression ?",
                    "answerOptions": [
                        {"text": "Le désembouage.", "isCorrect": False},
                        {"text": "Le Curage (ou Hydrocurage).", "isCorrect": True},
                        {"text": "Le détartrage.", "isCorrect": False},
                        {"text": "Le siphonnage.", "isCorrect": False}
                    ],
                    "correction": "Le **Curage** est une méthode de maintenance préventive et curative des réseaux."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le rôle de la **Ventilation Primaire** sur une colonne de chute ?",
                    "answerOptions": [
                        {"text": "Réchauffer l'air.", "isCorrect": False},
                        {"text": "Évacuer en toiture les gaz nauséabonds (odeurs d'égout) et maintenir une pression atmosphérique dans la colonne pour éviter le désiphonnage.", "isCorrect": True},
                        {"text": "Filtrer les eaux usées.", "isCorrect": False},
                        {"text": "Réduire le bruit.", "isCorrect": False}
                    ],
                    "correction": "La **Ventilation primaire** est la prolongation de la colonne de chute jusqu'à l'air libre (toiture)."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le risque de ne pas respecter la **nature du tube** lors d'un raccordement d'évacuation (ex : coller du PVC sur du Polypropylène) ?",
                    "answerOptions": [
                        {"text": "Le tube fait du bruit.", "isCorrect": False},
                        {"text": "La colle PVC ne garantit pas une soudure chimique étanche et durable avec un autre matériau (fuite à court/moyen terme).", "isCorrect": True},
                        {"text": "Le tube rouille.", "isCorrect": False},
                        {"text": "Le tube gèle.", "isCorrect": False}
                    ],
                    "correction": "Il faut utiliser les **raccords de transition** adaptés (à joint, mécanique) pour les changements de matériaux."
                },
                {
                    "questionNumber": 75,
                    "question": "Comment appelle-t-on la **sortie** d'un siphon (partie qui relie l'appareil à la canalisation principale) ?",
                    "answerOptions": [
                        {"text": "L'entrée.", "isCorrect": False},
                        {"text": "La garde d'eau.", "isCorrect": False},
                        {"text": "La Culotte (ou Décharge).", "isCorrect": True},
                        {"text": "La bonde.", "isCorrect": False}
                    ],
                    "correction": "La **Culotte** ou décharge du siphon renvoie l'eau vers l'évacuation."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le risque de réaliser des angles de raccordement (dérivation) trop vifs (90°) sur des évacuations horizontales ?",
                    "answerOptions": [
                        {"text": "Le siphon se vide.", "isCorrect": False},
                        {"text": "Un risque de bouchon car les matières solides s'accumulent plus facilement dans les coudes à angle droit (privilégier les coudes à grand rayon ou deux coudes à 45°).", "isCorrect": True},
                        {"text": "Le tube fuit.", "isCorrect": False},
                        {"text": "Le tube gèle.", "isCorrect": False}
                    ],
                    "correction": "Les **angles vifs** sont à proscrire sur les évacuations pour favoriser l'écoulement."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le rôle du **Manchon de dilatation** sur les longues sections de PVC (en aérien ou enterré) ?",
                    "answerOptions": [
                        {"text": "Réguler le bruit.", "isCorrect": False},
                        {"text": "Absorber la dilatation/contraction thermique du PVC (qui est élevée) pour éviter que les raccords ne se déboîtent ou que les colles ne lâchent.", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Maintenir la pente.", "isCorrect": False}
                    ],
                    "correction": "Le **PVC** est très sensible aux variations de température ; le manchon de dilatation est souvent requis en extérieur ou sur les grandes longueurs."
                },
                {
                    "questionNumber": 78,
                    "question": "Comment appelle-t-on le dispositif (souvent un coude ou un T) qui permet de dévier l'eau vers le bas lors d'une chute (ex : sous une baignoire) ?",
                    "answerOptions": [
                        {"text": "La bonde.", "isCorrect": False},
                        {"text": "La Culotte de raccordement.", "isCorrect": True},
                        {"text": "Le manchon.", "isCorrect": False},
                        {"text": "Le siphon.", "isCorrect": False}
                    ],
                    "correction": "La **Culotte** permet la jonction d'un écoulement horizontal à un écoulement vertical."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le principal inconvénient d'une **VMC Simple Flux** par rapport à une VMC Double Flux ?",
                    "answerOptions": [
                        {"text": "Elle fait plus de bruit.", "isCorrect": False},
                        {"text": "Elle génère des pertes calorifiques importantes en évacuant l'air chaud directement à l'extérieur (pas de récupération de chaleur).", "isCorrect": True},
                        {"text": "Elle n'extrait que les odeurs.", "isCorrect": False},
                        {"text": "Elle est plus chère à installer.", "isCorrect": False}
                    ],
                    "correction": "La **VMC Simple Flux** est moins performante sur le plan énergétique (contrairement à la Double Flux)."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment appelle-t-on la partie de la colonne de chute des eaux vannes (WC) qui se prolonge en toiture et est ouverte à l'air libre ?",
                    "answerOptions": [
                        {"text": "La ventilation secondaire.", "isCorrect": False},
                        {"text": "La Ventilation primaire (pour évacuer les gaz et éviter le désiphonnage par aspiration).", "isCorrect": True},
                        {"text": "Le chapeau de toiture.", "isCorrect": False},
                        {"text": "La cheminée.", "isCorrect": False}
                    ],
                    "correction": "La **Ventilation primaire** est essentielle pour le bon fonctionnement des siphons."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : PRODUCTION ET SÉCURITÉ ECS (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Production et Sécurité ECS (Eau Chaude Sanitaire) (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le rôle du **Groupe de Sécurité** sur un chauffe-eau à accumulation (ballon ECS) ?",
                    "answerOptions": [
                        {"text": "Chauffer l'eau.", "isCorrect": False},
                        {"text": "Maintenir la pression interne à 3 bars maximum (soupape) et évacuer l'excès de volume (dilatation de l'eau chauffée).", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Réguler le débit.", "isCorrect": False}
                    ],
                    "correction": "Le **Groupe de Sécurité** est un organe de sécurité essentiel, branché sur l'arrivée d'eau froide. "
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la principale exigence concernant la température de stockage de l'Eau Chaude Sanitaire (ECS) pour éviter la prolifération de la bactérie **Legionella** ?",
                    "answerOptions": [
                        {"text": "L'eau doit être stockée à 40 °C.", "isCorrect": False},
                        {"text": "L'eau doit être stockée à une température minimale d'environ 55 °C et le ballon doit être chauffé régulièrement au-delà de 60 °C (choc thermique).", "isCorrect": True},
                        {"text": "L'eau doit être stockée à 80 °C.", "isCorrect": False},
                        {"text": "La température n'a pas d'importance.", "isCorrect": False}
                    ],
                    "correction": "Le risque de **Légionellose** est critique entre 25 °C et 45 °C."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est le rôle de l'**Anode** (magnésium ou titane) à l'intérieur de la cuve d'un chauffe-eau ?",
                    "answerOptions": [
                        {"text": "Chauffer l'eau.", "isCorrect": False},
                        {"text": "Protéger la cuve en acier contre la corrosion (rouille) en s'oxydant elle-même (protection cathodique).", "isCorrect": True},
                        {"text": "Filtrer le calcaire.", "isCorrect": False},
                        {"text": "Mesurer la température.", "isCorrect": False}
                    ],
                    "correction": "L'**Anode** est la pièce 'sacrificielle' qui garantit la longévité de la cuve émaillée."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment appelle-t-on l'opération de maintenance qui consiste à retirer le calcaire accumulé sur la résistance et au fond du ballon d'eau chaude ?",
                    "answerOptions": [
                        {"text": "La vidange.", "isCorrect": False},
                        {"text": "Le Détartrage (généralement après la vidange et le démontage de la résistance).", "isCorrect": True},
                        {"text": "Le désembouage.", "isCorrect": False},
                        {"text": "La purge.", "isCorrect": False}
                    ],
                    "correction": "Le **Détartrage** est nécessaire pour maintenir le rendement et éviter la surchauffe de la résistance."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est l'élément qui permet de transformer l'énergie électrique en chaleur (effet Joule) dans un chauffe-eau électrique ?",
                    "answerOptions": [
                        {"text": "Le thermostat.", "isCorrect": False},
                        {"text": "La Résistance électrique (Blindée ou Stéatite).", "isCorrect": True},
                        {"text": "L'anode.", "isCorrect": False},
                        {"text": "Le groupe de sécurité.", "isCorrect": False}
                    ],
                    "correction": "La **Résistance** est l'élément chauffant du ballon."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est l'inconvénient principal d'un **Chauffe-eau instantané (gaz ou électrique)** ?",
                    "answerOptions": [
                        {"text": "Il est trop grand.", "isCorrect": False},
                        {"text": "Il peut ne pas fournir un débit suffisant à la température souhaitée lors de puisages multiples et simultanés.", "isCorrect": True},
                        {"text": "Il rouille facilement.", "isCorrect": False},
                        {"text": "Il est trop froid.", "isCorrect": False}
                    ],
                    "correction": "Le **Chauffe-eau instantané** est limité par sa puissance de chauffe maximale."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est le rôle du **Limiteur thermostatique de température (ou Mitigeur de sécurité)** sur la sortie d'ECS ?",
                    "answerOptions": [
                        {"text": "Augmenter la pression.", "isCorrect": False},
                        {"text": "Maintenir la température de l'eau distribuée aux points de puisage à un maximum de sécurité (souvent 50 °C) pour prévenir les brûlures, notamment pour les enfants.", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité.", "isCorrect": False}
                    ],
                    "correction": "Le **Limiteur de température** est essentiel si le ballon stocke à plus de 55 °C (prévention de la Légionellose)."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment appelle-t-on le dispositif qui permet de faire circuler l'ECS en permanence dans une boucle fermée pour réduire le temps d'attente au robinet ?",
                    "answerOptions": [
                        {"text": "Le bouclage de chauffage.", "isCorrect": False},
                        {"text": "Le Bouclage d'Eau Chaude Sanitaire (avec son circulateur et sa régulation).", "isCorrect": True},
                        {"text": "Le monotube ECS.", "isCorrect": False},
                        {"text": "Le circuit aller-retour.", "isCorrect": False}
                    ],
                    "correction": "Le **Bouclage ECS** apporte un confort immédiat, mais doit être parfaitement isolé pour éviter les pertes thermiques."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le rôle du **Thermostat** dans un chauffe-eau électrique ?",
                    "answerOptions": [
                        {"text": "Vidanger le ballon.", "isCorrect": False},
                        {"text": "Réguler la température de l'eau et assurer la coupure de l'alimentation électrique si la température souhaitée est atteinte (sécurité et régulation).", "isCorrect": True},
                        {"text": "Purger l'air.", "isCorrect": False},
                        {"text": "Réguler la pression.", "isCorrect": False}
                    ],
                    "correction": "Le **Thermostat** gère le cycle de chauffe et intègre souvent une sécurité anti-surchauffe."
                },
                {
                    "questionNumber": 90,
                    "question": "Pourquoi doit-on obligatoirement installer le **Groupe de Sécurité** du chauffe-eau à l'arrivée d'eau froide (EF) et non sur le départ d'eau chaude (EC) ?",
                    "answerOptions": [
                        {"text": "Pour faciliter l'entretien.", "isCorrect": False},
                        {"text": "Le groupe de sécurité doit absorber la dilatation de l'eau froide au fur et à mesure de la chauffe ; il ne doit pas être soumis à l'eau chaude stagnante pour éviter l'entartrage et le dysfonctionnement.", "isCorrect": True},
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Pour réguler le débit.", "isCorrect": False}
                    ],
                    "correction": "Le **Groupe de Sécurité** doit être sur l'EF. Sa soupape est conçue pour l'eau froide."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le risque de ne pas nettoyer régulièrement le **siphon du groupe de sécurité** ?",
                    "answerOptions": [
                        {"text": "Le ballon explose.", "isCorrect": False},
                        {"text": "Le calcaire ou les impuretés peuvent obstruer la vidange, empêchant l'évacuation du trop-plein et annulant l'action de la soupape (risque de surpression).", "isCorrect": True},
                        {"text": "Le ballon rouille.", "isCorrect": False},
                        {"text": "L'eau refroidit.", "isCorrect": False}
                    ],
                    "correction": "L'**entretien** (manœuvre régulière de la soupape) est vital pour la sécurité du groupe."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est l'élément d'un chauffe-eau solaire (CESI) qui permet de transférer la chaleur des panneaux solaires au ballon ECS ?",
                    "answerOptions": [
                        {"text": "Le régulateur.", "isCorrect": False},
                        {"text": "L'Échangeur (ou serpentin) thermique (souvent en cuivre) situé à l'intérieur du ballon.", "isCorrect": True},
                        {"text": "Le groupe de sécurité.", "isCorrect": False},
                        {"text": "L'anode.", "isCorrect": False}
                    ],
                    "correction": "L'**Échangeur** permet le transfert thermique sans mélange des fluides (circuit primaire glycolé vs. ECS)."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le risque de surchauffer le PER ou Multicouche lors de la brasure d'un raccord cuivre voisin ?",
                    "answerOptions": [
                        {"text": "Le tube devient trop rigide.", "isCorrect": False},
                        {"text": "Le tube plastique fond ou se déforme (ramollissement), entraînant une défaillance du raccordement ou une fuite immédiate.", "isCorrect": True},
                        {"text": "Le tube gèle.", "isCorrect": False},
                        {"text": "Le tube rétrécit.", "isCorrect": False}
                    ],
                    "correction": "Il faut protéger les **matériaux plastiques** de toute chaleur excessive lors des travaux de brasure (écran thermique)."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment appelle-t-on le dispositif qui permet de réinjecter de l'air dans un tube d'eau froide avant un changement de pression (pour éviter le coup de bélier) ?",
                    "answerOptions": [
                        {"text": "Le manomètre.", "isCorrect": False},
                        {"text": "L'Antibélier (à ressort, à air, ou à membrane).", "isCorrect": True},
                        {"text": "Le détendeur.", "isCorrect": False},
                        {"text": "Le circulateur.", "isCorrect": False}
                    ],
                    "correction": "L'**Antibélier** amortit les variations brutales de pression."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la cause la plus fréquente de la **baisse de pression (débit)** au niveau d'un robinet mitigeur ?",
                    "answerOptions": [
                        {"text": "Le siphon est bouché.", "isCorrect": False},
                        {"text": "L'entartrage du mousseur/aérateur ou de la cartouche du mitigeur (calcaire).", "isCorrect": True},
                        {"text": "Le groupe de sécurité fuit.", "isCorrect": False},
                        {"text": "Le chauffe-eau est vide.", "isCorrect": False}
                    ],
                    "correction": "Le **Calcaire** est la cause principale des problèmes de débit et de fuite sur la robinetterie."
                },
                {
                    "questionNumber": 96,
                    "question": "Dans le cas d'un chauffe-eau à **résistance stéatite**, quel est l'avantage principal de ce type de résistance ?",
                    "answerOptions": [
                        {"text": "Elle est plus petite.", "isCorrect": False},
                        {"text": "Elle n'est pas en contact direct avec l'eau (protégée par un fourreau), ce qui facilite l'entretien (pas besoin de vidanger le ballon pour la changer) et limite l'entartrage.", "isCorrect": True},
                        {"text": "Elle consomme moins.", "isCorrect": False},
                        {"text": "Elle chauffe plus vite.", "isCorrect": False}
                    ],
                    "correction": "La **Résistance Stéatite** est plus pratique pour la maintenance que la résistance blindée."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque de ne pas raccorder le tube de vidange du groupe de sécurité du chauffe-eau à l'air libre (avec garde d'air) ?",
                    "answerOptions": [
                        {"text": "Le groupe de sécurité ne fonctionne pas.", "isCorrect": False},
                        {"text": "Risque de refoulement ou d'aspiration des eaux usées (contamination sanitaire) dans le circuit d'eau potable.", "isCorrect": True},
                        {"text": "L'eau gèle.", "isCorrect": False},
                        {"text": "Le bruit est trop fort.", "isCorrect": False}
                    ],
                    "correction": "La **Garde d'air** (ou siphon adapté) est nécessaire entre la vidange de sécurité et le réseau d'évacuation."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le rôle du **Vase d'expansion sanitaire** (différent du Vex chauffage) ?",
                    "answerOptions": [
                        {"text": "Augmenter la pression.", "isCorrect": False},
                        {"text": "Absorber la dilatation de l'ECS lors de la chauffe pour éviter les fuites constantes au groupe de sécurité (économie d'eau).", "isCorrect": True},
                        {"text": "Réguler la température.", "isCorrect": False},
                        {"text": "Filtrer l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Vase d'expansion sanitaire** est souvent installé en cas de forte pression réseau pour soulager le groupe de sécurité (moins d'écoulement à l'égout)."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment appelle-t-on le dispositif qui permet de raccorder l'arrivée d'eau au compteur d'eau (la liaison entre le réseau public et le réseau privé) ?",
                    "answerOptions": [
                        {"text": "Le regard de visite.", "isCorrect": False},
                        {"text": "Le Raccord Union (à bride) ou la Cloche de branchement.", "isCorrect": True},
                        {"text": "La vanne d'arrêt.", "isCorrect": False},
                        {"text": "Le siphon.", "isCorrect": False}
                    ],
                    "correction": "Le **Raccord Union** permet un raccordement étanche et démontable pour la maintenance du compteur."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le risque de serrer **trop fort** un raccord laiton ou plastique sur un tube en PER/Multicouche (serrage à la clé) ?",
                    "answerOptions": [
                        {"text": "Le raccord fuira.", "isCorrect": False},
                        {"text": "L'écrasement ou la déformation du tube, ou la rupture du joint torique, entraînant un défaut d'étanchéité immédiat ou à terme.", "isCorrect": True},
                        {"text": "Le tube gèle.", "isCorrect": False},
                        {"text": "Le tube rouille.", "isCorrect": False}
                    ],
                    "correction": "Le **serrage modéré et contrôlé** est la clé de l'étanchéité des raccords mécaniques."
                },
            ]
        }
    }
}