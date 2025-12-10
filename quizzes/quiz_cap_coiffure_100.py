quiz_data = {
    "title": "CAP Métiers de la Coiffure - Base de Données Complète (100 Questions) - V5 (Longueurs Neutralisées)",
    
    "description": "Base de données de 100 questions pour le CAP Coiffure. Les options de réponses sont de longueurs variées et non prédictives. Correction précise et rappel de cours systématique.",
    
    "themes": {
        # THÈME 1 (LONGUEUR NEUTRALISÉE)
        1: {
            "name": "Hygiène, Sécurité, Environnement (HSE) et Législation",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est l'étape essentielle pour l'hygiène des outils de coupe entre deux clients ?",
                    "answerOptions": [
                        {"text": "Les nettoyer uniquement à l'eau savonneuse.", "isCorrect": False, "key": "A"},
                        {"text": "Nettoyage suivi d'une désinfection biocide.", "isCorrect": True, "key": "B"},
                        {"text": "Les ranger dans une trousse à outils fermée.", "isCorrect": False, "key": "C"},
                        {"text": "Stérilisation à haute température au four.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le protocole obligatoire est le nettoyage (élimination des débris) puis la **désinfection** (élimination des germes) avec un produit homologué (normes AFNOR) pour éviter la **contamination croisée**."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le rôle du 'Protège-nuque' (bande de papier jetable) positionné avant la cape de coupe ?",
                    "answerOptions": [
                        {"text": "Absorber l'excès de produit coiffant.", "isCorrect": False, "key": "A"},
                        {"text": "Sa fonction est d'absorber les produits chimiques qui coulent sur le cou du client.", "isCorrect": False, "key": "B"},
                        {"text": "Isoler la cape de coupe de la peau du client (barrière hygiénique jetable).", "isCorrect": True, "key": "C"},
                        {"text": "Soutenir la tête du client pendant le shampooing et le soin.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le protège-nuque est un élément d'hygiène à **usage unique** (EAU). Il est obligatoire pour isoler la peau du tissu de la cape réutilisable."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment doit-on gérer les déchets chimiques (restes de colorant, oxydant) en salon de coiffure ?",
                    "answerOptions": [
                        {"text": "Les jeter directement dans l'évier.", "isCorrect": False, "key": "A"},
                        {"text": "Les mélanger aux ordures ménagères classiques.", "isCorrect": False, "key": "B"},
                        {"text": "Stocker dans des contenants spécifiques.", "isCorrect": True, "key": "C"},
                        {"text": "Les conserver dans leur emballage d'origine pour les réutiliser.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les produits chimiques (oxydant, colorant) sont considérés comme des **Déchets Dangereux** (DD). Ils doivent être gérés par des entreprises spécialisées."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le risque de travailler sans gants de protection lors de l'application de produits chimiques ?",
                    "answerOptions": [
                        {"text": "La décoloration accélérée du peignoir.", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de dermatite ou de réactions allergiques cutanées.", "isCorrect": True, "key": "B"},
                        {"text": "La rupture des ponts cystines.", "isCorrect": False, "key": "C"},
                        {"text": "L'oxydation rapide des lames des ciseaux de coiffure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les gants sont des **Équipements de Protection Individuelle (EPI)** obligatoires pour protéger la peau des produits agressifs et prévenir les maladies professionnelles."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le danger principal lié à l'utilisation d'appareils électriques près d'une source d'eau ?",
                    "answerOptions": [
                        {"text": "Le danger principal est le risque d'intoxication aux poussières de kératine ou l'électrostatique.", "isCorrect": False, "key": "A"},
                        {"text": "Risque d'électrocution (court-circuit) par le contact entre l'eau et les parties électriques.", "isCorrect": True, "key": "B"},
                        {"text": "Le risque principal de Troubles Musculo-Squelettiques (TMS) lié à une mauvaise posture de l'utilisateur.", "isCorrect": False, "key": "C"},
                        {"text": "La chute du pH de l'eau de rinçage au contact des produits.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le coiffeur doit veiller à la sécurité des installations. Le **risque électrique** (court-circuit, électrocution) près de l'eau est très élevé."
                },
                {
                    "questionNumber": 6,
                    "question": "Que doit-on faire si un client signale une forte sensation de brûlure pendant une coloration ?",
                    "answerOptions": [
                        {"text": "Appliquer une dose supplémentaire d'oxydant.", "isCorrect": False, "key": "A"},
                        {"text": "Rincer immédiatement et abondamment à l'eau claire.", "isCorrect": True, "key": "B"},
                        {"text": "Continuer l'application et attendre 5 minutes de plus pour voir.", "isCorrect": False, "key": "C"},
                        {"text": "Demander au client de patienter jusqu'à la fin.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La sécurité du client est la priorité. Une sensation de brûlure indique une **réaction indésirable** (allergie ou irritation) : il faut rincer sans délai."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est le risque lié à l'accumulation de cheveux coupés sur le sol du salon ?",
                    "answerOptions": [
                        {"text": "Le risque d'intoxication à la kératine des cheveux.", "isCorrect": False, "key": "A"},
                        {"text": "Risque de chute et de glissade.", "isCorrect": True, "key": "B"},
                        {"text": "La rupture des ponts salins sous les pieds.", "isCorrect": False, "key": "C"},
                        {"text": "Le risque de 'remontée' de l'eau dans le bac ou dans les égouts.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le sol doit être **balayé après chaque coupe** pour des raisons de sécurité (glissade) et d'hygiène (propreté du salon)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est l'importance du 'test d'allergie' (touche d'essai) pour une première coloration ?",
                    "answerOptions": [
                        {"text": "Mesurer le pouvoir éclaircissant de l'oxydant sur le cheveu du client.", "isCorrect": False, "key": "A"},
                        {"text": "Vérifier la bonne adhésion du produit colorant à la fibre capillaire.", "isCorrect": False, "key": "B"},
                        {"text": "L'objectif est de vérifier l'adhésion du produit et de mesurer le pouvoir éclaircissant de l'oxydant.", "isCorrect": False, "key": "C"},
                        {"text": "Détecter une hypersensibilité ou une allergie au produit 48h avant l'application.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le test d'allergie (touche d'essai) est légalement **obligatoire 48h avant** la première application de coloration d'oxydation pour prévenir les réactions graves."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le risque de porter des 'bijoux' (bagues, bracelets) lors de la manipulation des cheveux ou des produits ?",
                    "answerOptions": [
                        {"text": "Contamination croisée, risque de blessure et accrochage dans la chevelure.", "isCorrect": True, "key": "A"},
                        {"text": "La dégradation du pH du cuir chevelu par la bague.", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de rouille des appareils électriques au contact du métal.", "isCorrect": False, "key": "C"},
                        {"text": "Le risque de brûlure thermique liée au contact du métal sur le cheveu au contact de la chaleur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les bijoux (surtout les bagues) sont des **vecteurs de bactéries**. Ils sont interdits ou fortement déconseillés en contact direct avec le client pour des raisons d'hygiène et de sécurité."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la procédure correcte de stockage des serviettes utilisées pour les clients ?",
                    "answerOptions": [
                        {"text": "L'important est de les laisser sécher à l'air libre, de préférence dans la salle de pause à l'abri de la lumière.", "isCorrect": False, "key": "A"},
                        {"text": "Stockage dans un bac fermé, séparé du linge propre.", "isCorrect": True, "key": "B"},
                        {"text": "Les jeter après chaque usage, même si elles sont juste humides.", "isCorrect": False, "key": "C"},
                        {"text": "Les réutiliser immédiatement après séchage à la main.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les serviettes utilisées (linge sale) doivent être stockées dans un **bac fermé, à l'écart des serviettes propres** pour éviter toute contamination croisée."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le risque d'utiliser une brosse ou un peigne avec des 'dents cassées' ou des 'bords tranchants' ?",
                    "answerOptions": [
                        {"text": "Le risque de coupure ou d'éraflure du cuir chevelu et d'agression mécanique de la fibre.", "isCorrect": True, "key": "A"},
                        {"text": "Le risque de dermatite de contact avec la kératine.", "isCorrect": False, "key": "B"},
                        {"text": "La rupture des ponts salins de la kératine du cheveu.", "isCorrect": False, "key": "C"},
                        {"text": "L'accélération de l'oxydation des produits coiffants.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Un **matériel défectueux** (dents cassées, bords tranchants) agresse le cuir chevelu et fragilise le cheveu (casse, fourches). Il doit être remplacé."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le rôle du 'Désinfectant' (produit biocide) dans le protocole d'hygiène ?",
                    "answerOptions": [
                        {"text": "Il sert uniquement à enlever la saleté visible des sols.", "isCorrect": False, "key": "A"},
                        {"text": "Il détruit les micro-organismes (bactéries, champignons, virus) après le nettoyage.", "isCorrect": True, "key": "B"},
                        {"text": "Il renforce la structure du cheveu en le gainant.", "isCorrect": False, "key": "C"},
                        {"text": "Il augmente le pH des colorations pour les rendre plus agressives.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **désinfection** est l'étape qui suit le nettoyage. Elle est essentielle pour l'hygiène des outils et des surfaces pour garantir un environnement sain."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est l'attitude à adopter en cas de coupure légère sur un poste de travail (coiffeur) ?",
                    "answerOptions": [
                        {"text": "Nettoyer, désinfecter la plaie et la recouvrir d'un pansement étanche.", "isCorrect": True, "key": "A"},
                        {"text": "Continuer le service après avoir essuyé la coupure avec une serviette.", "isCorrect": False, "key": "B"},
                        {"text": "Appliquer de la teinture pour stopper le saignement (effet astringent).", "isCorrect": False, "key": "C"},
                        {"text": "Demander à un collègue de faire le pansement rapidement.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Une plaie doit être immédiatement soignée et **isolée (pansement étanche)** pour éviter la contamination du client ou des produits (risque de transmission d'agent pathogène)."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le danger de laisser une serviette imbibée de produit (colorant) sur les épaules après le rinçage ?",
                    "answerOptions": [
                        {"text": "Le risque de toxicité et d'intoxication par inhalation des vapeurs chimiques.", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de réaction cutanée (irritation, brûlure) due au contact prolongé du produit chimique.", "isCorrect": True, "key": "B"},
                        {"text": "La corrosion accélérée des pièces du bac à shampooing.", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation rapide de la viscosité du produit sur la peau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Tous les produits chimiques doivent être **rincés immédiatement** et abondamment après leur temps de pause. La serviette souillée doit être retirée sans délai."
                },
                {
                    "questionNumber": 15,
                    "question": "Que doit-on faire si l'on constate un 'dysfonctionnement électrique' (étincelle, odeur de brûlé) sur un appareil ?",
                    "answerOptions": [
                        {"text": "Continuer à l'utiliser en faisant plus attention en attendant la fin de la journée.", "isCorrect": False, "key": "A"},
                        {"text": "Le mettre dans l'eau pour le refroidir si la chaleur est trop élevée.", "isCorrect": False, "key": "B"},
                        {"text": "Couper immédiatement l'alimentation électrique, débrancher et signaler l'appareil pour réparation.", "isCorrect": True, "key": "C"},
                        {"text": "Attendre la fin de la journée pour le jeter à la poubelle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Tout appareil défectueux doit être **mis hors service immédiatement** pour éviter les accidents (électrocution, incendie) et signalé à la direction."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est l'objectif principal de la 'traçabilité' des produits chimiques (FDS) ?",
                    "answerOptions": [
                        {"text": "Assurer la sécurité du véhicule pour l'utilisateur en cas de livraison.", "isCorrect": False, "key": "A"},
                        {"text": "Permettre d'identifier l'origine, la composition et les risques d'un produit en cas d'accident ou de réaction.", "isCorrect": True, "key": "B"},
                        {"text": "Ajouter un additif pour modifier la texture du produit.", "isCorrect": False, "key": "C"},
                        {"text": "Mesurer la teneur en kératine du cheveu avant l'application.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **FDS** (Fiche de Données de Sécurité) est un document légal obligatoire qui détaille les propriétés physiques, chimiques et les **précautions d'emploi** des produits dangereux."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) essentiel pour le coiffeur lors d'une coloration ?",
                    "answerOptions": [
                        {"text": "Les bouchons d'oreille.", "isCorrect": False, "key": "A"},
                        {"text": "Les gants pour les mains, la blouse et éventuellement des lunettes de protection.", "isCorrect": True, "key": "B"},
                        {"text": "Le casque anti-bruit pour le sèche-cheveux.", "isCorrect": False, "key": "C"},
                        {"text": "Les chaussures de sécurité à coque pour prévenir les coupures.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le port des **gants** et de la **tenue professionnelle** (blouse, tablier) est obligatoire pour la manipulation des produits chimiques. Ils protègent la peau et les vêtements."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le risque si un produit est stocké à une température trop élevée (près d'un radiateur) ?",
                    "answerOptions": [
                        {"text": "Le risque de dégradation prématurée et de modification de son efficacité (perte d'oxydation).", "isCorrect": True, "key": "A"},
                        {"text": "Le risque de 'remontée en température' du produit au contact des cheveux.", "isCorrect": False, "key": "B"},
                        {"text": "La diminution du temps de pétrissage du produit.", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation rapide de la viscosité de la pâte couleur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les produits chimiques (couleur, oxydant) doivent être stockés dans un **endroit frais et sec** (à l'abri de la lumière et de la chaleur) pour garantir leur stabilité et leur efficacité."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le rôle du 'shampooing neutralisant' (souvent acide) après une permanente ou une décoloration ?",
                    "answerOptions": [
                        {"text": "Servir uniquement à enlever la saleté visible.", "isCorrect": False, "key": "A"},
                        {"text": "Il permet de rétablir le pH naturel (acide) du cheveu après l'application de produits alcalins.", "isCorrect": True, "key": "B"},
                        {"text": "Il sert d'agent de blanchiment pour éclaircir la fibre capillaire.", "isCorrect": False, "key": "C"},
                        {"text": "Il augmente la viscosité de la pâte à la surface du cheveu.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le shampooing acide ou le soin neutralisant est essentiel pour **rééquilibrer le pH élevé (alcalin)** des produits chimiques et refermer les écailles (brillance et protection)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est l'attitude à adopter par le personnel en cas d'incendie dans l'établissement ?",
                    "answerOptions": [
                        {"text": "Alerter, couper les énergies et évacuer les clients vers le point de rassemblement, sans paniquer.", "isCorrect": True, "key": "A"},
                        {"text": "Tenter d'éteindre le feu par ses propres moyens, avec un linge humide.", "isCorrect": False, "key": "B"},
                        {"text": "Courir chercher de l'eau pour éteindre le feu s'il est petit.", "isCorrect": False, "key": "C"},
                        {"text": "Continuer le service en attendant l'arrivée des secours si possible.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **Plan de Sécurité Incendie** (PSSI) doit être maîtrisé : la priorité est à l'alerte et à l'évacuation rapide des personnes."
                }
            ]
        },
        # THÈME 2 (LONGUEUR NEUTRALISÉE)
        2: {
            "name": "Technologie des Produits et Matériels (Chimie et Matériaux)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le principal composant de la fibre capillaire (cheveu) qui lui donne sa structure et sa résistance ?",
                    "answerOptions": [
                        {"text": "La Cellule.", "isCorrect": False, "key": "A"},
                        {"text": "Le Collagène.", "isCorrect": False, "key": "B"},
                        {"text": "L'Amidon.", "isCorrect": False, "key": "C"},
                        {"text": "La Kératine, une protéine fibreuse et soufrée.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "La **Kératine** est la protéine majeure du cheveu (près de 90% de sa composition). Elle est responsable de sa rigidité, de sa souplesse et de son imperméabilité."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est le rôle de l'agent alcalin (souvent l'ammoniaque) dans une coloration d'oxydation ?",
                    "answerOptions": [
                        {"text": "Resserrer les écailles et neutraliser le pH.", "isCorrect": False, "key": "A"},
                        {"text": "Ouvrir les écailles (cuticule) pour permettre aux pigments de pénétrer au cœur du cortex.", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer l'activité des bactéries lactiques pour améliorer l'odeur.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le bac et les outils.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**alcalinité** (pH élevé) est nécessaire pour gonfler la cuticule et faire pénétrer les colorants (pigments d'oxydation) et l'oxydant à l'intérieur de la fibre."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le nom de l'appareil qui permet de 'lisser' les cheveux par la chaleur (fer plat) ?",
                    "answerOptions": [
                        {"text": "Le Lisseur (ou fer à lisser), qui utilise des plaques chauffantes pour modifier temporairement les ponts hydrogènes.", "isCorrect": True, "key": "A"},
                        {"text": "Le fer à friser.", "isCorrect": False, "key": "B"},
                        {"text": "Le casque de séchage.", "isCorrect": False, "key": "C"},
                        {"text": "Le vaporisateur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **lisseur** (chaleur sèche) modifie temporairement la structure du cheveu (rupture des ponts hydrogène). Le lissage s'annule au premier shampooing."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle du 'Conditionneur' ou 'Après-shampooing' (produit de soin) ?",
                    "answerOptions": [
                        {"text": "Décolorer le cheveu de plusieurs tons.", "isCorrect": False, "key": "A"},
                        {"text": "Démêler les cheveux, lisser la cuticule (écailles), apporter brillance et douceur.", "isCorrect": True, "key": "B"},
                        {"text": "Servir de substitut à la coloration d'oxydation en apportant de l'éclat.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le bac.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le conditionneur (soin **acide**) rétablit le pH naturel du cheveu et **referme les écailles** après l'ouverture par le shampooing (alcalin)."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment appelle-t-on la concentration de l'eau oxygénée utilisée dans les colorations (oxydant) ?",
                    "answerOptions": [
                        {"text": "Le pH.", "isCorrect": False, "key": "A"},
                        {"text": "L'indice de viscosité.", "isCorrect": False, "key": "B"},
                        {"text": "La température de séchage.", "isCorrect": False, "key": "C"},
                        {"text": "Le 'Volume' (ex : 10, 20, 30, 40 Vol), qui mesure la quantité d'oxygène libérée.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **Volume (Vol)** est l'unité de mesure de la concentration en eau oxygénée. Plus le volume est élevé, plus le pouvoir éclaircissant est important (oxydation)."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le type de ciseaux utilisé pour 'désépaissir' la masse de cheveux (effilage) ?",
                    "answerOptions": [
                        {"text": "Les ciseaux sculpteurs (ou effileurs), dont les lames sont crantées.", "isCorrect": True, "key": "A"},
                        {"text": "Les ciseaux droits (pour la coupe classique).", "isCorrect": False, "key": "B"},
                        {"text": "Le rasoir.", "isCorrect": False, "key": "C"},
                        {"text": "La tondeuse électrique.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les **ciseaux effileurs** (crantés) permettent de désépaissir la masse, de créer du mouvement et d'alléger les pointes sans créer de marques franches."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le rôle de la 'Gaine protectrice' (cuticule) qui entoure la fibre capillaire ?",
                    "answerOptions": [
                        {"text": "Assurer la nutrition du cheveu.", "isCorrect": False, "key": "A"},
                        {"text": "Déterminer la couleur naturelle (mélanine).", "isCorrect": False, "key": "B"},
                        {"text": "Protéger le cheveu des agressions et lui donner sa brillance.", "isCorrect": True, "key": "C"},
                        {"text": "Produire le sébum et l'excès de sébum.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **cuticule** est la couche protectrice externe (écailles). Si elle est lisse et fermée (grâce à un pH acide), le cheveu est brillant et en bonne santé."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment appelle-t-on la liaison (ponts) de la kératine qui est temporairement rompue par l'eau ou la chaleur ?",
                    "answerOptions": [
                        {"text": "Les ponts hydrogène (ou salins) qui sont modifiés par l'eau et la chaleur.", "isCorrect": True, "key": "A"},
                        {"text": "Les ponts disulfures (rompus par la permanente).", "isCorrect": False, "key": "B"},
                        {"text": "Les liaisons peptidiques.", "isCorrect": False, "key": "C"},
                        {"text": "Les liaisons covalentes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le brushing ou le lissage modifie temporairement la forme du cheveu (rupture des **ponts hydrogène**). Le mouillage annule l'effet car ces ponts se reforment."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le rôle du 'Shampooing Doux' (à pH neutre ou légèrement acide) dans un programme de soins ?",
                    "answerOptions": [
                        {"text": "Décolorer le cheveu de plusieurs tons.", "isCorrect": False, "key": "A"},
                        {"text": "Rendre la pâte trop ferme.", "isCorrect": False, "key": "B"},
                        {"text": "Nettoyer les cheveux et le cuir chevelu sans les agresser (usage fréquent ou cheveux fragiles).", "isCorrect": True, "key": "C"},
                        {"text": "Servir uniquement à colorer la mie du produit.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Un shampooing doux (pH neutre ou acide) **respecte l'équilibre naturel** (pH autour de 5,5) du cuir chevelu et du cheveu et est recommandé pour un usage fréquent."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le nom de la substance ajoutée à un produit pour en prolonger la conservation (durée de vie) ?",
                    "answerOptions": [
                        {"text": "Le Conservateur (parabènes, phénoxyéthanol, etc.) pour empêcher la prolifération bactérienne.", "isCorrect": True, "key": "A"},
                        {"text": "Le colorant.", "isCorrect": False, "key": "B"},
                        {"text": "L'agent émulsifiant.", "isCorrect": False, "key": "C"},
                        {"text": "L'amylase.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les **conservateurs** (dans les cosmétiques) sont essentiels pour empêcher la contamination du produit par les bactéries, les levures et les moisissures (durée d'utilisation)."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le rôle du 'Sérum Coiffant' (souvent à base de silicone) pour la finition d'une coiffure ?",
                    "answerOptions": [
                        {"text": "Fixer le cheveu de manière rigide.", "isCorrect": False, "key": "A"},
                        {"text": "Décolorer le cheveu de plusieurs tons.", "isCorrect": False, "key": "B"},
                        {"text": "Apporter brillance, lisser les pointes (anti-fourches) et protéger contre l'humidité.", "isCorrect": True, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le bac.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **sérum** est un produit de finition léger. Il gaine la fibre, l'alourdit (effet lissant) et apporte un effet miroir et une protection anti-humidité."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le nom de la technique qui consiste à tordre les cheveux et à appliquer une solution chimique pour obtenir une boucle durable ?",
                    "answerOptions": [
                        {"text": "Le lissage brésilien.", "isCorrect": False, "key": "A"},
                        {"text": "La Permanente (ou 'mini-vague') qui modifie de façon chimique et durable la structure interne du cheveu.", "isCorrect": True, "key": "B"},
                        {"text": "Le balayage.", "isCorrect": False, "key": "C"},
                        {"text": "La coloration.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **permanente** utilise des produits (réducteur puis fixateur) pour rompre et reformer les ponts disulfures de la kératine (modification chimique durable de la forme)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le rôle du 'Diffuseur' (embout rond) sur un sèche-cheveux ?",
                    "answerOptions": [
                        {"text": "Il augmente la chaleur pour un séchage plus rapide.", "isCorrect": False, "key": "A"},
                        {"text": "Il diminue le taux de cendres.", "isCorrect": False, "key": "B"},
                        {"text": "Il n'a aucun impact sur la pâte.", "isCorrect": False, "key": "C"},
                        {"text": "Il répartit la chaleur sur une grande surface pour sécher les cheveux bouclés/frisés sans défaire la boucle.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **diffuseur** est essentiel pour les cheveux bouclés. Il sèche le cheveu par le dessous, en respectant la formation de la boucle naturelle (volume et texture)."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le nom de la substance (matière grasse) qui protège le cuir chevelu de la sécheresse ?",
                    "answerOptions": [
                        {"text": "L'Ammoniaque.", "isCorrect": False, "key": "A"},
                        {"text": "La Kératine.", "isCorrect": False, "key": "B"},
                        {"text": "Le Collagène.", "isCorrect": False, "key": "C"},
                        {"text": "Le Sébum (film hydrolipidique) : mélange de lipides et de sueur.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **sébum** est la protection naturelle du cuir chevelu et de la fibre. L'excès de sébum rend le cheveu gras (cuir chevelu séborrhéique)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le nom de l'appareil (à chaleur humide) utilisé pour accélérer le temps de pause des produits ?",
                    "answerOptions": [
                        {"text": "Le casque de séchage (chaleur sèche).", "isCorrect": False, "key": "A"},
                        {"text": "La panade.", "isCorrect": False, "key": "B"},
                        {"text": "Le Vaporisateur (ou Climazon), qui produit de la chaleur humide pour faciliter la pénétration des produits.", "isCorrect": True, "key": "C"},
                        {"text": "La levure de surface.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **chaleur humide** ouvre la cuticule, optimisant le résultat des colorations (meilleure couverture) et permettant aux masques (soins profonds) de pénétrer plus facilement."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le rôle du 'Pinceau Applicateur' (avec des fibres synthétiques) en coloration ?",
                    "answerOptions": [
                        {"text": "Le pétrissage intensif.", "isCorrect": False, "key": "A"},
                        {"text": "L'autolyse.", "isCorrect": False, "key": "B"},
                        {"text": "Servir à la décoloration des vêtements.", "isCorrect": False, "key": "C"},
                        {"text": "Permettre une application précise (racines) et une bonne répartition du produit sur la mèche.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **pinceau** (adapté à la texture du produit) est l'outil de base pour la coloration (précision, séparation des sections et contrôle de l'application)."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'outil utilisé pour réaliser des mèches ou un balayage (isoler la mèche) ?",
                    "answerOptions": [
                        {"text": "Le couteau à pain.", "isCorrect": False, "key": "A"},
                        {"text": "Le papier aluminium (ou papier thermoplastique), qui isole la mèche traitée et maintient la chaleur.", "isCorrect": True, "key": "B"},
                        {"text": "Le coupe-ongle.", "isCorrect": False, "key": "C"},
                        {"text": "Le ciseau de cuisine.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**aluminium** (ou le papier thermoplastique) est essentiel pour créer un milieu occlusif (chaud) qui permet au produit de décolorer efficacement et rapidement."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est le rôle du 'Mousse Coiffante' (ou agent de fixation) pour un coiffage au rouleau ?",
                    "answerOptions": [
                        {"text": "Il fixe la coiffure (tenue) et apporte volume et corps, particulièrement pour les mises en plis et les coiffages bouclés.", "isCorrect": True, "key": "A"},
                        {"text": "Il ralentit la fermentation.", "isCorrect": False, "key": "B"},
                        {"text": "Il sert de nourriture à la levure.", "isCorrect": False, "key": "C"},
                        {"text": "Il sert uniquement à blanchir la mie.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **mousse** est un agent de coiffage temporaire. Elle doit être appliquée sur cheveux humides pour la mise en forme et garantir une mémoire de forme durable."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le rôle du 'Miroir de poche' (ou miroir à main) utilisé en fin de prestation (après la coupe) ?",
                    "answerOptions": [
                        {"text": "L'autolyse.", "isCorrect": False, "key": "A"},
                        {"text": "Permettre au client de visualiser l'arrière de la coupe (nuque) et de valider le résultat final.", "isCorrect": True, "key": "B"},
                        {"text": "Le bassinage.", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **miroir à main** est un outil essentiel de la consultation. Il permet de montrer la coupe finale (arrière de la tête) et d'obtenir la validation du client."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la fonction principale du 'Système de ventilation' dans un salon de coiffure ?",
                    "answerOptions": [
                        {"text": "Assurer le renouvellement de l'air et l'évacuation des odeurs et des vapeurs chimiques (ammoniaque) pour la santé.", "isCorrect": True, "key": "A"},
                        {"text": "Le sucre freine l'activité de la levure.", "isCorrect": False, "key": "B"},
                        {"text": "Le sucre détruit les bactéries lactiques.", "isCorrect": False, "key": "C"},
                        {"text": "Le sucre rend la pâte plus ferme.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**aération** (Ventilation Mécanique Contrôlée - VMC) est cruciale dans un salon pour l'évacuation des vapeurs de produits chimiques et pour le confort des clients."
                }
            ]
        },
        # THÈME 3 (LONGUEUR NEUTRALISÉE)
        3: {
            "name": "Techniques de Coiffure (Coupe, Coiffage, Mise en Forme)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Comment appelle-t-on le fait de 'couper les cheveux de la même longueur' sur tout le pourtour de la tête ?",
                    "answerOptions": [
                        {"text": "Le dégradé.", "isCorrect": False, "key": "A"},
                        {"text": "La Coupe Carrée (ou coupe pleine), qui est réalisée à angle droit (0° de projection).", "isCorrect": True, "key": "B"},
                        {"text": "L'effilage.", "isCorrect": False, "key": "C"},
                        {"text": "Le piquetage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **coupe carrée** (ligne droite) est la coupe de base, effectuée sans projection (0°). Elle apporte du poids et de la structure à la ligne de coupe."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le nom de la technique qui consiste à 'raccourcir les cheveux de manière progressive' (plus court en dessous) ?",
                    "answerOptions": [
                        {"text": "La Permanente.", "isCorrect": False, "key": "A"},
                        {"text": "Le Lissage.", "isCorrect": False, "key": "B"},
                        {"text": "Le Dégradé (ou 'Coupe en Couches'), qui enlève de la masse pour apporter du volume et du mouvement.", "isCorrect": True, "key": "C"},
                        {"text": "Le chignon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **dégradé** est réalisé avec une projection (élévation) du cheveu, souvent à 45° ou 90°. Il est crucial pour créer du volume et du mouvement."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la principale différence entre une 'frange droite' et une 'frange effilée' ?",
                    "answerOptions": [
                        {"text": "La frange droite (coupe pleine) est dense ; la frange effilée est plus légère, floue et se fond dans la masse.", "isCorrect": True, "key": "A"},
                        {"text": "Le temps de pause de la coloration.", "isCorrect": False, "key": "B"},
                        {"text": "Le type de shampooing utilisé.", "isCorrect": False, "key": "C"},
                        {"text": "Le prix de la prestation.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La frange droite (coupe pleine) crée une ligne nette. La frange **effilée** (ciseaux crantés) apporte de la légèreté, du mouvement et de la douceur."
                },
                {
                    "questionNumber": 44,
                    "question": "Comment appelle-t-on le fait de 'séparer la chevelure' en plusieurs zones avant de commencer la prestation ?",
                    "answerOptions": [
                        {"text": "Le crêpage.", "isCorrect": False, "key": "A"},
                        {"text": "Le démêlage.", "isCorrect": False, "key": "B"},
                        {"text": "Le Sectionnement (ou la Séparation), qui garantit la symétrie, la précision et la méthodologie de travail.", "isCorrect": True, "key": "C"},
                        {"text": "Le coiffage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **sectionnement** (avec des pinces) est l'étape de base. Il permet de travailler de manière ordonnée et de garantir la précision du résultat (coupe ou couleur) en isolant les zones."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est l'objectif du 'Brushing' (mise en forme temporaire) ?",
                    "answerOptions": [
                        {"text": "Sécher les cheveux tout en leur donnant du volume, des boucles, ou un lissage, à l'aide d'une brosse et d'un sèche-cheveux.", "isCorrect": True, "key": "A"},
                        {"text": "Modifier durablement la structure du cheveu.", "isCorrect": False, "key": "B"},
                        {"text": "Créer des mèches.", "isCorrect": False, "key": "C"},
                        {"text": "Neutraliser un reflet.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **brushing** utilise la chaleur pour modifier temporairement la forme du cheveu (ponts hydrogène). La brosse (ronde ou plate) est l'outil principal de mise en forme."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le nom de l'action qui consiste à 'tirer les cheveux vers l'extérieur' (à 90° de la tête) lors d'un dégradé ?",
                    "answerOptions": [
                        {"text": "L'effilage.", "isCorrect": False, "key": "A"},
                        {"text": "La Projection (ou l'Élévation), qui détermine l'angle de coupe et le degré de dégradé.", "isCorrect": True, "key": "B"},
                        {"text": "Le lissage.", "isCorrect": False, "key": "C"},
                        {"text": "Le bouclage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **projection** (angle d'élévation du cheveu) est le facteur clé pour réaliser un dégradé. Plus l'angle est grand, plus le dégradé est fort (volume maximal)."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le rôle du 'Crêpage' (brossage à rebrousse-poil) dans la réalisation d'une coiffure (chignon) ?",
                    "answerOptions": [
                        {"text": "Rendre le cheveu plus lisse et plus brillant.", "isCorrect": False, "key": "A"},
                        {"text": "Apporter un volume maximal à la base de la coiffure (racines) et créer une 'armature' pour la tenue.", "isCorrect": True, "key": "B"},
                        {"text": "Le tresser.", "isCorrect": False, "key": "C"},
                        {"text": "Décolorer le cheveu.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **crêpage** (tapotage de la brosse) permet de créer un volume artificiel et une base solide, indispensable pour la bonne tenue d'une coiffure attachée ou d'un chignon."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment appelle-t-on le type de 'mouvement' qui consiste à boucler les cheveux autour d'un bigoudi (ou rouleau) ?",
                    "answerOptions": [
                        {"text": "L'effilage.", "isCorrect": False, "key": "A"},
                        {"text": "Le Lissage.", "isCorrect": False, "key": "B"},
                        {"text": "L'Enroulage (mise en plis ou permanente), qui consiste à former une boucle ou une ondulation autour du support.", "isCorrect": True, "key": "C"},
                        {"text": "Le démêlage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**enroulage** (sur rouleaux ou bigoudis) est la technique de base pour créer des boucles par chaleur (mise en plis) ou par chimie (permanente) en contrôlant la forme."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est la fonction principale des 'Pinces de séparation' dans une mise en forme ?",
                    "answerOptions": [
                        {"text": "Mesurer la force de la farine.", "isCorrect": False, "key": "A"},
                        {"text": "Assurer la netteté des séparations (sectionnement) et maintenir les mèches en attente.", "isCorrect": True, "key": "B"},
                        {"text": "Resserrer le réseau de gluten.", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le bac.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les **pinces** (ou clips) sont les outils de base pour le sectionnement (coupe, couleur) et le maintien de la coiffure (mise en forme, chignon) pour un travail méthodique."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le nom de la technique de coupe qui consiste à 'couper seulement les pointes' (retirer la partie abîmée) ?",
                    "answerOptions": [
                        {"text": "Le défrisage.", "isCorrect": False, "key": "A"},
                        {"text": "L'Épointage (ou Couper les fourches), qui permet d'assainir la fibre sans modifier significativement la longueur.", "isCorrect": True, "key": "B"},
                        {"text": "Le balayage.", "isCorrect": False, "key": "C"},
                        {"text": "La permanente.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**épointage** est le soin de base pour l'entretien des cheveux longs. Il doit être fait régulièrement pour éviter que la fourche ne remonte sur la longueur du cheveu."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le risque de sécher les cheveux 'sans protecteur thermique' avant d'utiliser un lisseur (fer plat) ?",
                    "answerOptions": [
                        {"text": "La buée (vapeur) sera excessive.", "isCorrect": False, "key": "A"},
                        {"text": "L'activité de la levure sera bloquée.", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de 'brûlure' de la kératine (dommages irréversibles) et la déshydratation excessive de la fibre.", "isCorrect": True, "key": "C"},
                        {"text": "Le cheveu va s'étaler.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **protecteur thermique** crée une barrière entre la chaleur extrême du lisseur (jusqu'à 230°C) et la kératine du cheveu, prévenant la casse et les fourches."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le nom de la technique qui consiste à 'réaliser des tresses très fines et serrées' pour un coiffage structuré ?",
                    "answerOptions": [
                        {"text": "La mandoline.", "isCorrect": False, "key": "A"},
                        {"text": "Le Tressage (ou Vanille), qui est un coiffage sans chaleur, souvent réalisé pour donner une texture ondulée au cheveu.", "isCorrect": True, "key": "B"},
                        {"text": "La corne.", "isCorrect": False, "key": "C"},
                        {"text": "Le banneton.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **tressage** est une technique complexe qui permet de contrôler la forme du cheveu sans chimie ni chaleur et est une base pour de nombreuses coiffures attachées."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle du 'Filet à Cheveux' (accessoire) dans la réalisation d'un chignon sophistiqué ?",
                    "answerOptions": [
                        {"text": "Il permet de maintenir les mèches courtes ou indisciplinées et d'assurer une finition lisse et propre au chignon.", "isCorrect": True, "key": "A"},
                        {"text": "Le rafraîchi.", "isCorrect": False, "key": "B"},
                        {"text": "L'autolyse.", "isCorrect": False, "key": "C"},
                        {"text": "Le collage structurel.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **filet** (ou l'élastique transparent) est un accessoire pour 'cacher' les mèches volantes et garantir la propreté et la tenue esthétique du chignon."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'impact d'un 'séchage incomplet' (cheveux encore humides) sur un chignon ou une coiffure attachée ?",
                    "answerOptions": [
                        {"text": "La coiffure ne tiendra pas car l'humidité rompt les ponts hydrogène, et elle risque de se défaire ou de gonfler.", "isCorrect": True, "key": "A"},
                        {"text": "La buée (vapeur) sera excessive.", "isCorrect": False, "key": "B"},
                        {"text": "Le pain va s'étaler.", "isCorrect": False, "key": "C"},
                        {"text": "Le vin rouge trop froid.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le coiffage (lissage, boucle, attache) doit toujours se faire sur **cheveux parfaitement secs** pour garantir une tenue longue durée et éviter les frisottis."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le nom du type de 'bigoudi' (rouleau) utilisé pour une mise en plis qui donne une boucle serrée ?",
                    "answerOptions": [
                        {"text": "Le Bigoudi de petit diamètre (ou rouleau fin), qui produit des boucles serrées et un volume maximal.", "isCorrect": True, "key": "A"},
                        {"text": "La marmite.", "isCorrect": False, "key": "B"},
                        {"text": "La planche à découper.", "isCorrect": False, "key": "C"},
                        {"text": "Le poêlon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le diamètre du **bigoudi** est directement lié à la taille de la boucle : petit diamètre (boucle serrée et volume), grand diamètre (ondulation large et souple)."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le nom de l'action qui consiste à 'fixer les cheveux' par un produit (laque, spray) après le coiffage ?",
                    "answerOptions": [
                        {"text": "L'assiette de présentation.", "isCorrect": False, "key": "A"},
                        {"text": "La soupière.", "isCorrect": False, "key": "B"},
                        {"text": "La 'Laquage' (ou Fixation), qui permet de maintenir la coiffure en place et de la protéger de l'humidité.", "isCorrect": True, "key": "C"},
                        {"text": "Le plat de service.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **laquage** (ou la pulvérisation de spray) est l'étape de finition qui garantit la tenue de la coiffure en créant un film protecteur autour de la fibre."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment appelle-t-on le fait de 'peigner les cheveux dans leur direction naturelle' pour vérifier la ligne de coupe ?",
                    "answerOptions": [
                        {"text": "Le chanfreinage.", "isCorrect": False, "key": "A"},
                        {"text": "L'abaisse.", "isCorrect": False, "key": "B"},
                        {"text": "Le rafraîchi.", "isCorrect": False, "key": "C"},
                        {"text": "Le Coiffage 'en l'air' (ou 'Naturel'), qui permet de visualiser le résultat final de la coupe une fois les cheveux détendus.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le contrôle de la coupe se fait toujours **sans tension**, en coiffant 'en l'air', pour s'assurer que la ligne est droite, que la coupe est symétrique et que le tombé est naturel."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le but d'utiliser un 'peigne à queue' (peigne fin avec une pointe) pour la coloration ?",
                    "answerOptions": [
                        {"text": "Avoir une consistance (plasticité) similaire à celle de la pâte.", "isCorrect": False, "key": "A"},
                        {"text": "Accélérer la production de gaz carbonique (CO₂).", "isCorrect": False, "key": "B"},
                        {"text": "Servir uniquement à nettoyer le pétrin.", "isCorrect": False, "key": "C"},
                        {"text": "Séparer les mèches très fines (précision du traçage) et appliquer le produit sur les racines ou les zones délicates.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **peigne à queue** est indispensable pour le travail de précision (racines, mèches, séparation) en coupe, couleur ou mise en forme (traçage des séparations)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le nom de l'action qui consiste à 'réaliser des torsades' sur les mèches pour un coiffage sophistiqué ?",
                    "answerOptions": [
                        {"text": "La dorure.", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Torsadage' (ou Twist), qui est un coiffage de finition pour créer du mouvement et une texture spirale.", "isCorrect": True, "key": "B"},
                        {"text": "La buée (vapeur d'eau).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **torsadage** (twist) est une technique qui permet de créer des effets de relief et de mouvement dans une coiffure attachée ou un chignon."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle du 'Piquetage' (ou point cut) dans la finition d'une coupe ?",
                    "answerOptions": [
                        {"text": "Couper les pointes verticalement (en pointes) pour alléger légèrement la masse et apporter de la souplesse et du mouvement.", "isCorrect": True, "key": "A"},
                        {"text": "Ajouter du sel dans la pâte.", "isCorrect": False, "key": "B"},
                        {"text": "Servir uniquement à nettoyer le pétrin.", "isCorrect": False, "key": "C"},
                        {"text": "Permettre au réseau de gluten de se relâcher.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **piquetage** (coupe en pointes) est une technique de finition. Il sert à 'casser' la ligne de coupe pour un effet plus doux, léger et aérien."
                }
            ]
        },
        # THÈME 4 (LONGUEUR NEUTRALISÉE)
        4: {
            "name": "Techniques de Coloration et Décoloration (Colorimétrie)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelles sont les trois 'Couleurs Primaires' utilisées dans le cercle chromatique de la coiffure ?",
                    "answerOptions": [
                        {"text": "Orange, Vert, Violet.", "isCorrect": False, "key": "A"},
                        {"text": "Blanc, Gris, Noir.", "isCorrect": False, "key": "B"},
                        {"text": "Rouge, Jaune, Bleu, qui, mélangées, permettent d'obtenir toutes les autres couleurs.", "isCorrect": True, "key": "C"},
                        {"text": "Magenta, Cyan, Jaune.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les **couleurs primaires** (Rouge, Jaune, Bleu) sont la base de la colorimétrie. Leur mélange crée les couleurs secondaires (Orange, Vert, Violet) et les reflets."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le rôle du 'pigment naturel' (Mélanine) contenu dans le cortex du cheveu ?",
                    "answerOptions": [
                        {"text": "Déterminer la forme du cheveu.", "isCorrect": False, "key": "A"},
                        {"text": "Déterminer la 'Couleur Naturelle' du cheveu (eumélanine pour le foncé, phéomélanine pour le clair).", "isCorrect": True, "key": "B"},
                        {"text": "Servir uniquement à nettoyer le bac.", "isCorrect": False, "key": "C"},
                        {"text": "Protéger le cheveu des agressions.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **mélanine** est le pigment naturel. L'eumélanine (brun/noir) et la phéomélanine (roux/jaune) sont présentes dans le cortex et déterminent la hauteur de ton et les reflets naturels."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la 'Couleur Secondaire' obtenue par le mélange des couleurs primaires 'Bleu' et 'Rouge' ?",
                    "answerOptions": [
                        {"text": "Le Vert (Bleu + Jaune).", "isCorrect": False, "key": "A"},
                        {"text": "Le Rouge (primaire).", "isCorrect": False, "key": "B"},
                        {"text": "Le Violet (couleur secondaire) ; utilisé pour neutraliser le reflet Jaune.", "isCorrect": True, "key": "C"},
                        {"text": "Le Jaune (primaire).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Mélange : Bleu + Rouge = **Violet**. Le Violet (reflet en .2) est la couleur complémentaire du Jaune (reflet résiduel de décoloration)."
                },
                {
                    "questionNumber": 64,
                    "question": "Comment appelle-t-on le processus qui consiste à 'éclaircir' la couleur naturelle des cheveux avant une coloration ?",
                    "answerOptions": [
                        {"text": "Le Dégraissage.", "isCorrect": False, "key": "A"},
                        {"text": "Le balayage.", "isCorrect": False, "key": "B"},
                        {"text": "Le shampooing.", "isCorrect": False, "key": "C"},
                        {"text": "La Décoloration (ou Blanchiment), qui ouvre les écailles et oxyde les pigments (mélanine).", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "La **décoloration** (poudre ou crème décolorante + oxydant) est une action chimique qui détruit les pigments naturels (mélanine) pour atteindre un niveau d'éclaircissement souhaité."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le rôle du 'Nuancier' (catalogue de couleurs) dans la consultation client ?",
                    "answerOptions": [
                        {"text": "Servir uniquement à mélanger le produit.", "isCorrect": False, "key": "A"},
                        {"text": "Servir à enrouler les bigoudis.", "isCorrect": False, "key": "B"},
                        {"text": "Il permet au client de choisir la couleur désirée et au coiffeur de déterminer la formule à appliquer.", "isCorrect": True, "key": "C"},
                        {"text": "Servir à vérifier la porosité.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **nuancier** est l'outil de communication (entre coiffeur et client) et de travail (formulation de la couleur) indispensable pour garantir la précision du résultat."
                },
                {
                    "questionNumber": 66,
                    "question": "Quelle est la 'Couleur Complémentaire' utilisée pour neutraliser un reflet 'Orange' non désiré ?",
                    "answerOptions": [
                        {"text": "Le Vert.", "isCorrect": False, "key": "A"},
                        {"text": "Le Jaune.", "isCorrect": False, "key": "B"},
                        {"text": "Le Rouge.", "isCorrect": False, "key": "C"},
                        {"text": "Le Bleu (reflet en .1 ou .8) ou le Bleu Cendré, qui permet d'atténuer l'Orange.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **Bleu** est la couleur complémentaire de l'Orange. Il est utilisé pour neutraliser les reflets cuivrés/orangés qui apparaissent souvent lors des éclaircissements."
                },
                {
                    "questionNumber": 67,
                    "question": "Comment est codifiée la 'Hauteur de Ton' (degré de clarté/obscurité) dans la numérotation des couleurs ?",
                    "answerOptions": [
                        {"text": "De 1 (le plus clair) à 10 (le plus foncé).", "isCorrect": False, "key": "A"},
                        {"text": "De 0 à 100%.", "isCorrect": False, "key": "B"},
                        {"text": "De 1 (le Noir - le plus foncé) à 10 (le Blond Platine - le plus clair), qui détermine la base de la couleur.", "isCorrect": True, "key": "C"},
                        {"text": "De -10 à +10.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **hauteur de ton** (le premier chiffre) indique la clarté : 1 (noir), 5 (châtain clair), 8 (blond clair), 10 (blond très clair/platine). C'est la base de la formulation."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le nom de l'action qui consiste à 'recouvrir les cheveux blancs' par une coloration ?",
                    "answerOptions": [
                        {"text": "Le défrisage.", "isCorrect": False, "key": "A"},
                        {"text": "Le Couverture (ou Masquage), qui utilise une base naturelle pour apporter le pigment manquant.", "isCorrect": True, "key": "B"},
                        {"text": "Le balayage.", "isCorrect": False, "key": "C"},
                        {"text": "La permanente.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **couverture** des cheveux blancs (cheveux sans mélanine) nécessite l'ajout d'une base naturelle (reflet .0) pure pour garantir une bonne prise de la couleur et un résultat uniforme."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le rôle du 'Pré-Pigmentation' (ajout d'un pigment chaud avant la couleur) sur des cheveux décolorés ?",
                    "answerOptions": [
                        {"text": "La dorure.", "isCorrect": False, "key": "A"},
                        {"text": "La buée (vapeur d'eau).", "isCorrect": False, "key": "B"},
                        {"text": "Réintroduire les pigments chauds (Rouge, Orange) détruits par la décoloration pour obtenir une couleur foncée harmonieuse.", "isCorrect": True, "key": "C"},
                        {"text": "Le pointage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **pré-pigmentation** est obligatoire pour les retours au foncé sur des bases très claires afin d'éviter le reflet verdâtre ou l'effet 'terne' de la coloration."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment est codifié le 'Reflet' (nuance) dans la numérotation des couleurs (le ou les chiffres après la virgule) ?",
                    "answerOptions": [
                        {"text": "Par des symboles.", "isCorrect": False, "key": "A"},
                        {"text": "Par des chiffres (ex : .1 cendré, .3 doré, .6 rouge), qui indiquent la nuance dominante.", "isCorrect": True, "key": "B"},
                        {"text": "Par des lettres.", "isCorrect": False, "key": "C"},
                        {"text": "Uniquement par la hauteur de ton.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **reflet** (le ou les chiffres après le point/virgule) indique la nuance. Le premier reflet est dominant, le second est secondaire : ex. 6.34 (Doré dominant, Cuivré secondaire)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est l'impact du 'temps de pause' non respecté pour une coloration ?",
                    "answerOptions": [
                        {"text": "Un temps trop court donne une couleur non prise ; un temps trop long risque d'abîmer le cheveu (sensibilisation).", "isCorrect": True, "key": "A"},
                        {"text": "Le pain de mie.", "isCorrect": False, "key": "B"},
                        {"text": "Le spectro-photomètre.", "isCorrect": False, "key": "C"},
                        {"text": "Le croissant.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **temps de pause** (respect du protocole) est crucial pour garantir le résultat souhaité (couleur, éclaircissement) et préserver la qualité de la fibre capillaire."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le risque de superposer des colorations permanentes sur les longueurs (et non seulement sur les racines) ?",
                    "answerOptions": [
                        {"text": "Le risque de 'surcharge pigmentaire' (cheveux trop foncés, opaques) et de sensibilisation excessive de la fibre.", "isCorrect": True, "key": "A"},
                        {"text": "Le beurre va fondre.", "isCorrect": False, "key": "B"},
                        {"text": "L'activité de la levure sera bloquée.", "isCorrect": False, "key": "C"},
                        {"text": "La croûte sera épaisse et dure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La coloration permanente s'applique uniquement en racine (repousse). Sur les longueurs, on utilise un produit plus doux (**ton sur ton ou patine**) pour éviter d'abîmer et de foncer inutilement."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le nom de la technique qui permet de faire un 'test de porosité' ?",
                    "answerOptions": [
                        {"text": "Le rafraîchi.", "isCorrect": False, "key": "A"},
                        {"text": "Le Test à l'Eau (observation de l'absorption) ou le toucher (rugosité), qui détermine si le cheveu est en bon état avant coloration.", "isCorrect": True, "key": "B"},
                        {"text": "Le pointage.", "isCorrect": False, "key": "C"},
                        {"text": "Le bassinage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Un cheveu **poreux** (écailles ouvertes) absorbe trop vite la couleur (effet trop foncé) et la délave rapidement. La porosité est un élément clé du diagnostic avant coloration."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le rôle du 'Déjaunisseur' (Shampooing Violet) sur les cheveux blonds ou blancs ?",
                    "answerOptions": [
                        {"text": "Améliorer le goût.", "isCorrect": False, "key": "A"},
                        {"text": "Réguler l'acidité.", "isCorrect": False, "key": "B"},
                        {"text": "Neutraliser les reflets 'Jaunes' indésirables en appliquant le pigment complémentaire (Violet).", "isCorrect": True, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le bac.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **Violet** neutralise le Jaune (couleur complémentaire). Le shampooing violet est un entretien pour les blonds clairs ou les gris/blancs afin de maintenir un reflet froid."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le nom de l'action qui consiste à 'éclaircir légèrement' le cheveu par petites touches pour un effet soleil ?",
                    "answerOptions": [
                        {"text": "La cuisson sur plaque.", "isCorrect": False, "key": "A"},
                        {"text": "La cuisson par injection de vapeur.", "isCorrect": False, "key": "B"},
                        {"text": "La surgélation de la pâte.", "isCorrect": False, "key": "C"},
                        {"text": "Le Balayage (ou Mèches), qui utilise une technique de 'voile' ou de 'triangles' pour apporter du contraste et de la lumière.", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **balayage** est une technique de coloration partielle qui apporte de la profondeur et du relief. Elle se travaille souvent 'à l'air libre' (sans alu)."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le rôle du 'Masque Réparateur' (soin profond) après une décoloration ou un service technique ?",
                    "answerOptions": [
                        {"text": "Des farines de céréales.", "isCorrect": False, "key": "A"},
                        {"text": "De la farine de blé.", "isCorrect": False, "key": "B"},
                        {"text": "Il permet de refermer les écailles et d'apporter les lipides et protéines manquants pour l'hydratation et la force.", "isCorrect": True, "key": "C"},
                        {"text": "De la farine de seigle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les **soins (masques)** sont vitaux après une prestation chimique (couleur, décoloration) pour réparer les dommages, renforcer la fibre et prolonger la tenue de la couleur."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le risque d'utiliser un oxydant (développeur) dont la 'concentration est trop faible' (ex : 10 Vol au lieu de 30 Vol) ?",
                    "answerOptions": [
                        {"text": "Un pain trop acide.", "isCorrect": False, "key": "A"},
                        {"text": "Le risque d'obtenir une couleur trop foncée ou un éclaircissement insuffisant (oxydation incomplète des pigments).", "isCorrect": True, "key": "B"},
                        {"text": "La non-levée de la pâte.", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation de la force.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**oxydant (volume)** détermine le pouvoir éclaircissant. Une erreur de volume entraîne un échec de la coloration (trop foncé, ou mauvaise neutralisation des reflets)."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le nom du produit utilisé pour 'enlever les taches de coloration' (sur la peau ou le front) après la prestation ?",
                    "answerOptions": [
                        {"text": "Le 'Détachant' (ou Nettoyeur de peau), à base d'agents réducteurs doux, pour dissoudre le pigment sans irriter la peau.", "isCorrect": True, "key": "A"},
                        {"text": "L'ajout de malt torréfié.", "isCorrect": False, "key": "B"},
                        {"text": "L'incorporation de la matière grasse.", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **détachant** est utilisé pour garantir la propreté de la peau après la coloration. Il est souvent précédé d'une crème grasse (contour du visage) pour prévenir la coloration de la peau."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le rôle du 'Patine' (couleur très diluée) appliquée après une décoloration ou un balayage ?",
                    "answerOptions": [
                        {"text": "Développer une meilleure complexité aromatique.", "isCorrect": False, "key": "A"},
                        {"text": "Neutraliser un reflet indésirable (jaune/orange) et apporter une nuance finale (cendré, doré) sans éclaircir davantage.", "isCorrect": True, "key": "B"},
                        {"text": "La 'maturation' (affinage) des produits secs.", "isCorrect": False, "key": "C"},
                        {"text": "Accélérer la production de gaz carbonique (CO₂).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **patine** (souvent un ton sur ton sans ammoniaque) est utilisée en finition (après éclaircissement) pour personnaliser le reflet et uniformiser la couleur."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est l'incidence du 'pourcentage de cheveux blancs' sur le choix de la coloration ?",
                    "answerOptions": [
                        {"text": "Elle est naturellement sans gluten.", "isCorrect": False, "key": "A"},
                        {"text": "Plus le pourcentage de cheveux blancs est important, plus le coiffeur doit ajouter une 'Base Naturelle' pure dans le mélange.", "isCorrect": True, "key": "B"},
                        {"text": "Elle est très riche en sel.", "isCorrect": False, "key": "C"},
                        {"text": "Elle sert uniquement à colorer la croûte du pain.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La couverture des cheveux blancs (cheveux sans pigment) nécessite un apport de **base (.0)** pour garantir un résultat uniforme, durable et éviter la transparence du reflet."
                }
            ]
        },
        # THÈME 5 (LONGUEUR NEUTRALISÉE)
        5: {
            "name": "Commercialisation, Relation Client et Gestion (Vente)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le but de la 'Vente Additionnelle' (ou 'Upselling') en salon de coiffure ?",
                    "answerOptions": [
                        {"text": "Elle est très enrichie en œufs.", "isCorrect": False, "key": "A"},
                        {"text": "Proposer des produits ou services complémentaires (soin, masque, produit coiffant) pour augmenter le panier moyen.", "isCorrect": True, "key": "B"},
                        {"text": "Elle est très peu hydratée.", "isCorrect": False, "key": "C"},
                        {"text": "Elle est fabriquée sans sel.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **vente additionnelle** (le soin proposé après le shampooing, l'achat du produit à domicile) est essentielle pour la rentabilité et le chiffre d'affaires du salon."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le rôle de la 'Consultation Client' (avant le service) ?",
                    "answerOptions": [
                        {"text": "Le mastic polyester.", "isCorrect": False, "key": "A"},
                        {"text": "La farine de maïs.", "isCorrect": False, "key": "B"},
                        {"text": "Établir un diagnostic (état du cheveu, historique couleur) et définir les attentes du client pour garantir la satisfaction.", "isCorrect": True, "key": "C"},
                        {"text": "La farine de blé.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **consultation** (écoute active et diagnostic) est l'étape de base. Elle permet de valider la prestation et d'assurer un résultat en phase avec les attentes du client."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est l'importance de la 'Fiche Client' (dossier personnel) pour la coiffure ?",
                    "answerOptions": [
                        {"text": "Elle permet de tracer l'historique des prestations, des produits utilisés et des préférences (fidélisation et sécurité).", "isCorrect": True, "key": "A"},
                        {"text": "Il doit être consommé dans les 24 heures.", "isCorrect": False, "key": "B"},
                        {"text": "Il se conserve beaucoup plus longtemps.", "isCorrect": False, "key": "C"},
                        {"text": "Il contient des additifs.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **fiche client** (historique, allergies, formules couleur) est un document de travail et de sécurité. Elle est indispensable pour la fidélisation et la qualité du suivi."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le rôle du 'Prix de Vente' (ou tarif) dans la gestion du salon ?",
                    "answerOptions": [
                        {"text": "L'incorporation de la matière grasse.", "isCorrect": False, "key": "A"},
                        {"text": "Il doit couvrir les coûts (matières premières, salaires, loyer) et dégager une marge bénéficiaire (rentabilité).", "isCorrect": True, "key": "B"},
                        {"text": "L'utilisation de farine de seigle.", "isCorrect": False, "key": "C"},
                        {"text": "La cuisson à haute température.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **tarification** (définition des prix) est la base de la rentabilité. Elle doit être cohérente avec les charges (coût de revient) et le positionnement du salon."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le nom de la technique de vente qui consiste à 'proposer un produit supérieur' (plus cher) à celui initialement demandé ?",
                    "answerOptions": [
                        {"text": "Le 'Montée en Gamme' (Upgrading) : suggérer un soin plus luxueux ou un produit de marque supérieure.", "isCorrect": True, "key": "A"},
                        {"text": "La cuisson par injection de vapeur.", "isCorrect": False, "key": "B"},
                        {"text": "La cuisson sur sole.", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**upgrading** (montée en gamme) est une technique de vente par la suggestion d'un avantage (meilleure qualité, meilleur résultat, soin plus profond) justifiant le surcoût."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est l'attitude à adopter en cas de 'réclamation' (client insatisfait) après une prestation ?",
                    "answerOptions": [
                        {"text": "Elle n'utilise pas de levure.", "isCorrect": False, "key": "A"},
                        {"text": "Écouter activement la plainte, s'excuser et proposer une solution (retouche immédiate, geste commercial).", "isCorrect": True, "key": "B"},
                        {"text": "Elle est fabriquée avec une farine de seigle.", "isCorrect": False, "key": "C"},
                        {"text": "Elle nécessite un pétrissage très long.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gestion des **réclamations** est vitale. Un client mécontent traité avec empathie et solutionné peut devenir un client très fidèle (fidélisation)."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est l'élément essentiel de la 'vitrine' (façade) du salon pour attirer le client ?",
                    "answerOptions": [
                        {"text": "Le risque de 'brûler' les micro-organismes.", "isCorrect": False, "key": "A"},
                        {"text": "Le pain complet.", "isCorrect": False, "key": "B"},
                        {"text": "La propreté, l'éclairage, la présentation des produits (merchandising) et des 'modèles' (images de coupes).", "isCorrect": True, "key": "C"},
                        {"text": "Le pain de seigle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **vitrine** (premier contact) doit refléter la qualité du service (propreté, modernité) et donner envie d'entrer. Elle est le reflet de l'image de marque du salon."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le rôle de la 'communication non verbale' (posture, gestes) du coiffeur en salle ?",
                    "answerOptions": [
                        {"text": "La peau d'orange.", "isCorrect": False, "key": "A"},
                        {"text": "Elle transmet la confiance, le professionnalisme et l'attention sans avoir besoin de parler (sourire, gestes précis, calme).", "isCorrect": True, "key": "B"},
                        {"text": "Le pain de seigle.", "isCorrect": False, "key": "C"},
                        {"text": "Le pain complet.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le coiffeur doit être attentif, calme et dégager du professionnalisme. La **communication non verbale** est essentielle pour mettre le client en confiance et exprimer l'expertise."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le but d'utiliser un langage 'technique professionnel' (mèches, patine, hauteur de ton) avec les collègues ?",
                    "answerOptions": [
                        {"text": "La dorure.", "isCorrect": False, "key": "A"},
                        {"text": "La buée (vapeur d'eau).", "isCorrect": False, "key": "B"},
                        {"text": "Le pointage.", "isCorrect": False, "key": "C"},
                        {"text": "Assurer la précision des commandes, le diagnostic et la transmission des instructions (langage codifié).", "isCorrect": True, "key": "D"}
                    ],
                    "correction": "Le **vocabulaire professionnel** (en couleur ou en coupe) garantit la bonne exécution des tâches, l'absence d'erreurs et l'efficacité du travail en équipe."
                },
                {
                    "questionNumber": 90,
                    "question": "Comment s'appelle l'action qui consiste à 'proposer au client un produit coiffant' (à usage domestique) après la coiffure ?",
                    "answerOptions": [
                        {"text": "La 'Vente Croisée' (Cross-selling) : vendre un produit pour que le client puisse reproduire la coiffure à la maison.", "isCorrect": True, "key": "A"},
                        {"text": "Obtenir une mie très blanche.", "isCorrect": False, "key": "B"},
                        {"text": "Fabriquer un pain très acide.", "isCorrect": False, "key": "C"},
                        {"text": "Utiliser uniquement de la farine de seigle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **vente croisée** (vendre le shampooing, le spray, le sérum) est une source de revenu importante et un service client (conseil à domicile pour reproduire le résultat)."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le document qui détaille la recette, les étapes, la quantité des ingrédients et le coût des matières premières pour une prestation ?",
                    "answerOptions": [
                        {"text": "La 'Fiche Technique de Prestation' (FTP) qui permet la standardisation de la formule couleur (coût et résultat).", "isCorrect": True, "key": "A"},
                        {"text": "Le tableau de 'la formule du boulanger'.", "isCorrect": False, "key": "B"},
                        {"text": "Le coefficient d'hydratation (H) de la farine.", "isCorrect": False, "key": "C"},
                        {"text": "Le plan de production et le planning des employés.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **FTP** (fiche technique prestation) est la base de la standardisation (même résultat) et de la gestion des coûts (produits utilisés et coût de revient)."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le rôle du 'Seuil de Rentabilité' (SR) pour la gestion du salon ?",
                    "answerOptions": [
                        {"text": "Le montant de chiffre d'affaires à réaliser pour couvrir toutes les charges (fixes et variables) et atteindre un bénéfice nul.", "isCorrect": True, "key": "A"},
                        {"text": "L'absorption d'eau.", "isCorrect": False, "key": "B"},
                        {"text": "Le rapport P/L.", "isCorrect": False, "key": "C"},
                        {"text": "Le pH.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **SR** (ou 'point mort') est le seuil à atteindre (en CA) pour ne pas être déficitaire. Il est crucial pour la survie et la planification financière de l'entreprise."
                },
                {
                    "questionNumber": 93,
                    "question": "Si vous commandez 10 L de shampooing (coût 40 €/L) et que la remise fournisseur est de 20%, quel est le coût HT total (en €) ?",
                    "answerOptions": [
                        {"text": "2,00 € HT.", "isCorrect": False, "key": "A"},
                        {"text": "4,00 € HT.", "isCorrect": False, "key": "B"},
                        {"text": "320,00 € HT (10 L x 40 €/L = 400 € ; 400 € x 0,80 = 320 €).", "isCorrect": True, "key": "C"},
                        {"text": "1,00 € HT.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Coût brut (40 * 10) = 400 € HT. Remise (400 * 0,20) = 80 €. **Coût net** (400 - 80) = **320,00 € HT**."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle de la 'fiche technique' dans la standardisation des services ?",
                    "answerOptions": [
                        {"text": "Déterminer la température de base de la pâte.", "isCorrect": False, "key": "A"},
                        {"text": "Mesurer la force de la farine.", "isCorrect": False, "key": "B"},
                        {"text": "Garantir la constance de la qualité de la prestation, sa traçabilité et le calcul de son prix de revient.", "isCorrect": True, "key": "C"},
                        {"text": "Vérifier la bonne exécution du nettoyage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La **FTF** (ou FTP) est le document de référence qui permet de garantir le même niveau de qualité à chaque client et de maîtriser la consommation de produits (gestion des coûts)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le mode de calcul qui permet de répartir les coûts (loyer, assurance, électricité) sur l'ensemble des prestations ?",
                    "answerOptions": [
                        {"text": "Le calcul du coût des matières premières.", "isCorrect": False, "key": "A"},
                        {"text": "Le calcul des charges indirectes (ou frais généraux), réparties par prestation ou par heure de travail.", "isCorrect": True, "key": "B"},
                        {"text": "Le calcul du prix de vente HT uniquement.", "isCorrect": False, "key": "C"},
                        {"text": "Le calcul du taux de perte à la cuisson.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les **charges indirectes** (fixes) doivent être incluses dans le prix de revient (par un coefficient ou une imputation horaire) pour garantir la rentabilité globale du salon."
                },
                {
                    "questionNumber": 96,
                    "question": "Si le taux de TVA applicable à la 'vente de produits cosmétiques' est de 20%, quel est le montant de la TVA pour un masque à 25,00 € HT ?",
                    "answerOptions": [
                        {"text": "5,00 € (25,00 € x 0,20).", "isCorrect": True, "key": "A"},
                        {"text": "75,0 kg de farine.", "isCorrect": False, "key": "B"},
                        {"text": "100,0 kg de farine.", "isCorrect": False, "key": "C"},
                        {"text": "50,0 kg de farine.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Montant de la **TVA** = Prix HT * Taux de TVA. Soit 25,00 € * 0,20 = **5,00 €**. Le prix TTC sera de 30,00 € (25,00 € + 5,00 €)."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le but du 'Poids Net' (PN) d'un ingrédient dans la fiche technique de prestation (FTP) ?",
                    "answerOptions": [
                        {"text": "Le poids de l'ingrédient tel qu'il est ajouté à la formule (sans les emballages, les déchets ou les impuretés).", "isCorrect": True, "key": "A"},
                        {"text": "Le prix de vente HT du produit fini.", "isCorrect": False, "key": "B"},
                        {"text": "Le coût total de la main d'œuvre.", "isCorrect": False, "key": "C"},
                        {"text": "Le taux de perte à la cuisson.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **poids net** (ou dosage : ex. 15 g de couleur) est la base du calcul du coût des matières premières. On ne compte que la quantité de produit effectivement utilisée."
                },
                {
                    "questionNumber": 98,
                    "question": "Comment calcule-t-on le 'Prix TTC' (Toutes Taxes Comprises) à partir du Prix HT (Hors Taxe) et du taux de TVA ?",
                    "answerOptions": [
                        {"text": "Les charges variables.", "isCorrect": False, "key": "A"},
                        {"text": "Prix HT multiplié par (1 + Taux de TVA en décimal, soit 1,20 pour 20%).", "isCorrect": True, "key": "B"},
                        {"text": "Le coût de la main d'œuvre.", "isCorrect": False, "key": "C"},
                        {"text": "Le prix de vente HT du produit fini.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Formule économique : **Prix TTC = Prix HT x (1 + t)**. Cette formule est essentielle pour la facturation et l'encaissement (gestion de la TVA collectée)."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment s'appelle l'opération qui consiste à 'compter les produits' pour vérifier l'exactitude des stocks ?",
                    "answerOptions": [
                        {"text": "Le test d'alvéographe.", "isCorrect": False, "key": "A"},
                        {"text": "L'inventaire : le dénombrement (comptage) physique des stocks pour ajuster les comptes et contrôler les pertes.", "isCorrect": True, "key": "B"},
                        {"text": "Le test de DLC.", "isCorrect": False, "key": "C"},
                        {"text": "Le test de température de la pâte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'**inventaire** (mensuel ou annuel) permet de valoriser les stocks (actif de l'entreprise) et de calculer le coût réel des marchandises vendues (CMV)."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le rôle du 'Prix d'appel' (tarif de base bas) dans la stratégie commerciale du salon ?",
                    "answerOptions": [
                        {"text": "Attirer le client avec un prix faible (coupe simple, brushing) pour ensuite lui vendre des services additionnels (couleur, soin).", "isCorrect": True, "key": "A"},
                        {"text": "Le taux standard de 0%.", "isCorrect": False, "key": "B"},
                        {"text": "Le taux réduit de 5,5%.", "isCorrect": False, "key": "C"},
                        {"text": "Le taux standard de 10%.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le **prix d'appel** est un outil marketing. Il permet d'attirer le client sur une prestation de base (faible marge) pour le fidéliser et lui vendre des prestations à forte marge."
                }
            ]
        }
    }
}