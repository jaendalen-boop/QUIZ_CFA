# Fichier : quiz_cap_platre_isolation_100.py

quiz_data = {
    "title": "Quiz CAP Métiers du Plâtre et de l'Isolation : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : PRÉPARATION ET SÉCURITÉ DE CHANTIER (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Préparation de Chantier, Sécurité et Supports (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) essentiel lors du mélange de plâtre ou d'enduit en poudre ?",
                    "answerOptions": [
                        {"text": "Les gants anti-coupure.", "isCorrect": False},
                        {"text": "Le casque anti-bruit.", "isCorrect": False},
                        {"text": "Le masque anti-poussière FFP2 ou FFP3 et les lunettes de protection.", "isCorrect": True},
                        {"text": "Le gilet haute visibilité.", "isCorrect": False}
                    ],
                    "correction": "Le plâtre et les enduits génèrent des poussières fines irritantes pour les voies respiratoires et les yeux. Le **Masque FFP** est obligatoire."
                },
                {
                    "questionNumber": 2,
                    "question": "Que représente le sigle **NFP** (Niveau du Fil du Plancher) sur un plan de construction ?",
                    "answerOptions": [
                        {"text": "La hauteur totale du bâtiment.", "isCorrect": False},
                        {"text": "Le niveau de référence horizontal du sol fini, à partir duquel toutes les hauteurs sont cotées (souvent noté +/- 0.00).", "isCorrect": True},
                        {"text": "L'épaisseur de l'isolant.", "isCorrect": False},
                        {"text": "Le Nu de Façade Principale.", "isCorrect": False}
                    ],
                    "correction": "Le **NFP** est le repère essentiel pour l'implantation et le niveau des ouvrages (rails, plafonds, etc.)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel outil est utilisé pour projeter et lisser des enduits traditionnels ou des mortiers sur de grandes surfaces (murs et plafonds) ?",
                    "answerOptions": [
                        {"text": "La taloche.", "isCorrect": False},
                        {"text": "La machine à projeter (ou Gâchette) et/ou le Platoir.", "isCorrect": True},
                        {"text": "Le couteau à enduire.", "isCorrect": False},
                        {"text": "Le niveau laser.", "isCorrect": False}
                    ],
                    "correction": "La **Machine à projeter** permet de gagner du temps et assure une bonne adhérence de l'enduit ou du plâtre sur le support."
                },
                {
                    "questionNumber": 4,
                    "question": "Avant l'application d'un enduit ou d'un plâtre sur un support trop absorbant (ex : parpaing neuf), quel produit faut-il appliquer pour réguler l'absorption et améliorer l'accroche ?",
                    "answerOptions": [
                        {"text": "De l'eau pure.", "isCorrect": False},
                        {"text": "Un fixateur ou un primaire d'accrochage (lait de chaux, produit de type SikaLatex).", "isCorrect": True},
                        {"text": "Un vernis.", "isCorrect": False},
                        {"text": "De la peinture.", "isCorrect": False}
                    ],
                    "correction": "Le **Primaire d'accrochage** empêche l'eau de gâchage de l'enduit d'être 'bue' trop rapidement par le support, évitant la fissuration."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la principale fonction d'un **Solin** ?",
                    "answerOptions": [
                        {"text": "Fixer les montants métalliques.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité entre deux matériaux différents (ex : au niveau de la jonction mur/terrasse ou mur/toiture).", "isCorrect": True},
                        {"text": "Lisser le plâtre.", "isCorrect": False},
                        {"text": "Soutenir le plafond.", "isCorrect": False}
                    ],
                    "correction": "Le **Solin** est un joint de recouvrement et d'étanchéité, souvent réalisé par le plâtrier-plaquiste dans les zones de transition."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel type de cheville doit-on utiliser pour la fixation d'un objet lourd (ex : un chauffe-eau) dans une cloison en Plaque de Plâtre (Placo) simple ?",
                    "answerOptions": [
                        {"text": "Une cheville Molly.", "isCorrect": False},
                        {"text": "Une fixation lourde à travers la plaque, ancrée directement dans l'ossature métallique ou le mur porteur derrière (fixation sur structure).", "isCorrect": True},
                        {"text": "Une vis à bois.", "isCorrect": False},
                        {"text": "Une cheville à frapper.", "isCorrect": False}
                    ],
                    "correction": "Les charges lourdes (plus de 30 kg) ne doivent pas être supportées par la plaque seule, même avec une Molly. Il faut se reprendre sur le support rigide (ossature ou mur)."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle précaution doit-on prendre avant d'utiliser des outils coupants (cutter, scie à guichet) pour découper des plaques de plâtre ?",
                    "answerOptions": [
                        {"text": "Ne pas porter de gants.", "isCorrect": False},
                        {"text": "S'assurer que la lame est toujours bien affûtée et dégager la zone de coupe des câbles électriques (risques de coupure et d'électrocution).", "isCorrect": True},
                        {"text": "Ne pas utiliser de règle.", "isCorrect": False},
                        {"text": "Couper très lentement.", "isCorrect": False}
                    ],
                    "correction": "Une **lame affûtée** réduit l'effort et le risque de dérapage."
                },
                {
                    "questionNumber": 8,
                    "question": "Qu'est-ce que le **Plâtre gros** ?",
                    "answerOptions": [
                        {"text": "Un plâtre déjà mélangé.", "isCorrect": False},
                        {"text": "Un plâtre à grains plus gros, utilisé pour le dégrossissage (ou corps d'enduit) sur des épaisseurs importantes, avant la couche de finition.", "isCorrect": True},
                        {"text": "Un plâtre coloré.", "isCorrect": False},
                        {"text": "Un plâtre résistant à l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Plâtre gros** sert à redresser les murs. Il est ensuite recouvert d'un plâtre fin (lissage)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le risque de travailler sur un échafaudage sans garde-corps et plinthe périphérique ?",
                    "answerOptions": [
                        {"text": "Le bruit.", "isCorrect": False},
                        {"text": "La chute de hauteur (l'accident le plus grave sur chantier) et la chute d'objets ou d'outils sur les personnes en dessous.", "isCorrect": True},
                        {"text": "Le froid.", "isCorrect": False},
                        {"text": "L'échafaudage va se déformer.", "isCorrect": False}
                    ],
                    "correction": "La **sécurité en hauteur** (garde-corps, plinthe et amarrage) est non négociable."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le rôle du **Mélangeur (ou Agitateur)** sur une perceuse ?",
                    "answerOptions": [
                        {"text": "Percer le mur.", "isCorrect": False},
                        {"text": "Gâcher et mélanger de manière homogène le plâtre, les enduits ou les colles pour obtenir une pâte sans grumeaux.", "isCorrect": True},
                        {"text": "Poncer le plâtre.", "isCorrect": False},
                        {"text": "Découper les plaques.", "isCorrect": False}
                    ],
                    "correction": "Le **Mélangeur** assure un gâchage de qualité, essentiel à la bonne prise des matériaux."
                },
                {
                    "questionNumber": 11,
                    "question": "Que signifie le marquage **NF** sur une plaque de plâtre ?",
                    "answerOptions": [
                        {"text": "Nouvelle Finition.", "isCorrect": False},
                        {"text": "Norme Française (certification de qualité et de conformité du produit).", "isCorrect": True},
                        {"text": "Niveau Fini.", "isCorrect": False},
                        {"text": "Nu de Façade.", "isCorrect": False}
                    ],
                    "correction": "La marque **NF** est un gage de qualité reconnu par les professionnels."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment s'appelle la technique de pose d'un enduit qui consiste à tirer le produit avec une règle de maçon pour obtenir une surface plane, en s'appuyant sur des repères verticaux ?",
                    "answerOptions": [
                        {"text": "Le Jointoiement.", "isCorrect": False},
                        {"text": "Le Dressage sur des règles (ou Repères) d'enduit.", "isCorrect": True},
                        {"text": "Le Lissage.", "isCorrect": False},
                        {"text": "Le Gâchage.", "isCorrect": False}
                    ],
                    "correction": "Le **Dressage** est la méthode pour obtenir une planéité parfaite du mur."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est l'outil utilisé pour contrôler la planéité (l'absence de ventre ou de creux) d'un mur après le dressage ?",
                    "answerOptions": [
                        {"text": "Le Mètre ruban.", "isCorrect": False},
                        {"text": "La Règle à niveau (ou Règle de maçon) de grande longueur (2 ou 3 mètres).", "isCorrect": True},
                        {"text": "Le Fil à plomb.", "isCorrect": False},
                        {"text": "Le Pied à coulisse.", "isCorrect": False}
                    ],
                    "correction": "La **Règle** permet de visualiser les défauts de planéité qui ne sont pas visibles à l'œil nu."
                },
                {
                    "questionNumber": 14,
                    "question": "Comment stocker les sacs de plâtre ou d'enduit en poudre sur le chantier ?",
                    "answerOptions": [
                        {"text": "Directement sur le sol humide.", "isCorrect": False},
                        {"text": "Sur palettes ou cales en bois, au sec et à l'abri de l'humidité (l'eau peut faire prendre le plâtre dans le sac).", "isCorrect": True},
                        {"text": "À l'extérieur, sous la pluie.", "isCorrect": False},
                        {"text": "Empilés très haut.", "isCorrect": False}
                    ],
                    "correction": "L'**humidité** est l'ennemi du plâtre et des enduits en poudre."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle est la principale caractéristique d'une cheville **Molly** ?",
                    "answerOptions": [
                        {"text": "Elle est utilisée pour le béton plein.", "isCorrect": False},
                        {"text": "Elle est conçue pour l'expansion dans les matériaux creux, comme les cloisons en plaques de plâtre.", "isCorrect": True},
                        {"text": "Elle est en bois.", "isCorrect": False},
                        {"text": "Elle résiste au feu.", "isCorrect": False}
                    ],
                    "correction": "La **Cheville Molly** est la fixation standard pour les charges légères à moyennes dans le Placoplâtre."
                },
                {
                    "questionNumber": 16,
                    "question": "Que doit-on vérifier en priorité sur un mur existant avant de coller une doublage isolant ?",
                    "answerOptions": [
                        {"text": "Sa couleur.", "isCorrect": False},
                        {"text": "Sa planéité, sa propreté (dépoussiérage) et l'absence de moisissures ou de produits non adhérents.", "isCorrect": True},
                        {"text": "Sa température.", "isCorrect": False},
                        {"text": "Son épaisseur.", "isCorrect": False}
                    ],
                    "correction": "Le **support** doit être sain, propre et sec pour garantir l'adhérence de la colle ou du mortier."
                },
                {
                    "questionNumber": 17,
                    "question": "Comment appelle-t-on le risque lié au contact de la peau avec des produits humides comme le ciment ou le plâtre frais ?",
                    "answerOptions": [
                        {"text": "Le rhume.", "isCorrect": False},
                        {"text": "Les brûlures chimiques (alcalines) ou les dermatoses professionnelles (ex : eczéma).", "isCorrect": True},
                        {"text": "Le refroidissement.", "isCorrect": False},
                        {"text": "L'électrocution.", "isCorrect": False}
                    ],
                    "correction": "Le port de **gants étanches** est essentiel pour se protéger des produits alcalins (ciment, chaux, plâtre frais) et de l'eau de gâchage."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le danger principal du mastic silicone **acétoxy** (odeur de vinaigre) ?",
                    "answerOptions": [
                        {"text": "Il n'est pas étanche.", "isCorrect": False},
                        {"text": "Il dégage de l'acide acétique qui peut corroder certains métaux et altérer certains supports (marbre, plâtre non protégé).", "isCorrect": True},
                        {"text": "Il sèche trop lentement.", "isCorrect": False},
                        {"text": "Il est trop cher.", "isCorrect": False}
                    ],
                    "correction": "Il faut privilégier le silicone **neutre** ou le mastic acrylique dans la plupart des travaux de plâtrerie et finition."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'outil utilisé pour créer un angle de 90 degrés net et précis lors de la coupe de plaques de plâtre ?",
                    "answerOptions": [
                        {"text": "La scie sauteuse.", "isCorrect": False},
                        {"text": "La règle de guidage et le cutter (pour la coupe droite) puis le rabot à chant ou la râpe pour l'arête.", "isCorrect": True},
                        {"text": "Le ciseau à bois.", "isCorrect": False},
                        {"text": "Le marteau.", "isCorrect": False}
                    ],
                    "correction": "L'utilisation de la **règle** et le bon cassage de la plaque sont les bases du métier. La finition au rabot ou à la râpe assure l'équerrage de l'arête."
                },
                {
                    "questionNumber": 20,
                    "question": "Que doit-on faire de la poussière de ponçage (enduit sec, plâtre) ?",
                    "answerOptions": [
                        {"text": "La laisser au sol.", "isCorrect": False},
                        {"text": "L'aspirer ou la balayer et la mettre dans un sac à déchets approprié, en portant le masque FFP3 pour ne pas l'inhaler.", "isCorrect": True},
                        {"text": "La mouiller.", "isCorrect": False},
                        {"text": "La mélanger au nouveau plâtre.", "isCorrect": False}
                    ],
                    "correction": "Le **nettoyage régulier** du poste de travail est essentiel pour l'hygiène et la sécurité."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : POSE DE PLAQUES DE PLÂTRE (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Pose de Plaques de Plâtre et Ossatures (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Comment appelle-t-on le profilé métallique horizontal fixé au sol et au plafond, qui sert de guide pour l'ossature d'une cloison en Placo ?",
                    "answerOptions": [
                        {"text": "La fourrure.", "isCorrect": False},
                        {"text": "Le Rail (R48, R70, etc.).", "isCorrect": True},
                        {"text": "Le montant.", "isCorrect": False},
                        {"text": "La lisse.", "isCorrect": False}
                    ],
                    "correction": "Le **Rail** est l'élément de départ et d'arrivée, il est fixé au gros œuvre."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la distance standard (entraxe) entre deux montants verticaux d'une ossature Placo, pour une plaque de largeur 120 cm ?",
                    "answerOptions": [
                        {"text": "40 cm.", "isCorrect": False},
                        {"text": "60 cm (pour que les bords de plaques tombent sur un montant).", "isCorrect": True},
                        {"text": "120 cm.", "isCorrect": False},
                        {"text": "30 cm.", "isCorrect": False}
                    ],
                    "correction": "L'**Entraxe de 60 cm** est le standard pour les plaques de 120 cm de large, assurant un bon maintien de la plaque."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le risque de visser la plaque de plâtre trop près des bords ?",
                    "answerOptions": [
                        {"text": "Le trou sera trop grand.", "isCorrect": False},
                        {"text": "La plaque risque de s'effriter ou de se casser au niveau du bord cartonné (respecter une distance de 1 cm minimum du bord non aminci).", "isCorrect": True},
                        {"text": "Le rail sera trop long.", "isCorrect": False},
                        {"text": "La vis sera trop courte.", "isCorrect": False}
                    ],
                    "correction": "Le bord non aminci d'une plaque est fragile. La distance minimale est de **10 mm**."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on la technique de collage d'une plaque de plâtre isolante directement sur un mur, par plots de colle (mortier adhésif) ?",
                    "answerOptions": [
                        {"text": "Le Scellement.", "isCorrect": False},
                        {"text": "Le Doublage par collage (ou Calage par plots).", "isCorrect": True},
                        {"text": "Le Jointoiement.", "isCorrect": False},
                        {"text": "La Projection.", "isCorrect": False}
                    ],
                    "correction": "Le **Doublage par plots** est une méthode rapide pour isoler et redresser les murs intérieurs."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel type de vis est spécifiquement conçu pour la fixation des plaques de plâtre sur une ossature métallique (rail/montant) ?",
                    "answerOptions": [
                        {"text": "La vis à bois.", "isCorrect": False},
                        {"text": "La vis TTPC (Tête Trompette Pointe Clou), autoperceuse, au pas de vis fin.", "isCorrect": True},
                        {"text": "La vis à béton.", "isCorrect": False},
                        {"text": "Le tirefond.", "isCorrect": False}
                    ],
                    "correction": "La vis **TTPC** est la vis standard du plaquiste, elle s'enfonce légèrement dans le carton sans déchirer la surface."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le rôle du **suspente** dans la réalisation d'un plafond suspendu ?",
                    "answerOptions": [
                        {"text": "Assurer l'étanchéité.", "isCorrect": False},
                        {"text": "Relier les fourrures (ossature du plafond) à la structure du bâtiment (dalle béton ou charpente) pour supporter le poids du plafond.", "isCorrect": True},
                        {"text": "Fixer les montants.", "isCorrect": False},
                        {"text": "Cacher les câbles.", "isCorrect": False}
                    ],
                    "correction": "La **Suspente** doit être choisie en fonction de la charge à supporter et du type de structure du bâtiment."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le risque si une plaque de plâtre n'est pas posée avec un **jeu (environ 1 cm)** au niveau du sol ?",
                    "answerOptions": [
                        {"text": "Le plâtre va fissurer.", "isCorrect": False},
                        {"text": "La plaque peut absorber l'humidité du sol par capillarité et se dégrader (remontées d'eau).", "isCorrect": True},
                        {"text": "L'isolation sera meilleure.", "isCorrect": False},
                        {"text": "Le jointoiement sera plus facile.", "isCorrect": False}
                    ],
                    "correction": "Le **jeu de dilatation** au sol est primordial et sera caché par la plinthe. Il prévient l'absorption d'eau par le carton."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment s'appelle la technique de découpe d'une réservation (ex : pour un interrupteur) au milieu d'une plaque de plâtre ?",
                    "answerOptions": [
                        {"text": "La coupe au couteau.", "isCorrect": False},
                        {"text": "La coupe à la scie cloche (pour les formes rondes) ou à la scie à guichet (pour les formes rectangulaires).", "isCorrect": True},
                        {"text": "La coupe au laser.", "isCorrect": False},
                        {"text": "Le ponçage.", "isCorrect": False}
                    ],
                    "correction": "La **Scie à guichet** permet de réaliser des ouvertures au milieu de la plaque après un perçage initial."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le rôle du **Lève-plaque** sur le chantier ?",
                    "answerOptions": [
                        {"text": "Nettoyer les plaques.", "isCorrect": False},
                        {"text": "Permettre à un seul ouvrier de lever et de maintenir les plaques de plâtre au plafond en position pour la fixation.", "isCorrect": True},
                        {"text": "Découper les plaques.", "isCorrect": False},
                        {"text": "Fixer les rails.", "isCorrect": False}
                    ],
                    "correction": "Le **Lève-plaque** réduit les risques de TMS (Troubles Musculo-Squelettiques) et la pénibilité."
                },
                {
                    "questionNumber": 30,
                    "question": "Que signifie le marquage **H** sur une plaque de plâtre (ex : PlacoHydro) ?",
                    "answerOptions": [
                        {"text": "Haute résistance.", "isCorrect": False},
                        {"text": "Hydrofuge (résistant à l'humidité, usage en cuisine, salle de bain, etc.).", "isCorrect": True},
                        {"text": "Haute densité.", "isCorrect": False},
                        {"text": "Horizontal.", "isCorrect": False}
                    ],
                    "correction": "La plaque **Hydrofuge (H)** (carton vert) est essentielle dans les pièces humides."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est l'outil utilisé pour sertir (lier mécaniquement) les montants et les rails d'une ossature métallique sans vis ?",
                    "answerOptions": [
                        {"text": "La perceuse.", "isCorrect": False},
                        {"text": "La Pince à sertir (ou Pince à clincher).", "isCorrect": True},
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "Le cutter.", "isCorrect": False}
                    ],
                    "correction": "La **Pince à sertir** est rapide et crée une liaison mécanique stable par déformation du métal."
                },
                {
                    "questionNumber": 32,
                    "question": "Dans le cas d'une **contre-cloison** (doublage), pourquoi doit-on poser la plaque verticalement ?",
                    "answerOptions": [
                        {"text": "Pour que le joint soit plus esthétique.", "isCorrect": False},
                        {"text": "Pour réduire le nombre de joints horizontaux et ne conserver que les joints verticaux (moins de risque de fissuration).", "isCorrect": True},
                        {"text": "Pour aller plus vite.", "isCorrect": False},
                        {"text": "Pour consommer moins de vis.", "isCorrect": False}
                    ],
                    "correction": "La pose **verticale** réduit le risque de fissuration de l'ouvrage fini."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment doit-on disposer les joints verticaux de deux plaques adjacentes dans le cas d'une **double peau** (deux plaques superposées) ?",
                    "answerOptions": [
                        {"text": "Les aligner parfaitement.", "isCorrect": False},
                        {"text": "Les décaler (ou croiser) d'au moins 50 cm pour éviter la continuité des joints, ce qui renforce l'ouvrage et l'isolation.", "isCorrect": True},
                        {"text": "Les coller.", "isCorrect": False},
                        {"text": "Les laisser ouverts.", "isCorrect": False}
                    ],
                    "correction": "Le **décalage des joints** est une règle de base pour le renforcement des cloisons."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le risque de trop serrer les vis de la plaque de plâtre lors de la fixation sur l'ossature ?",
                    "answerOptions": [
                        {"text": "La vis va rouiller.", "isCorrect": False},
                        {"text": "Le carton de la plaque sera déchiré, ce qui entraîne une mauvaise tenue de la vis et rend le jointoiement difficile.", "isCorrect": True},
                        {"text": "L'ossature va plier.", "isCorrect": False},
                        {"text": "Le plâtre va fondre.", "isCorrect": False}
                    ],
                    "correction": "La vis doit être juste **légèrement encastrée** dans le carton, sans le déchirer. Utiliser une visseuse avec butée de profondeur est recommandé."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est l'utilité du **Rabot à chanfrein** pour la plaque de plâtre ?",
                    "answerOptions": [
                        {"text": "Lisser la plaque.", "isCorrect": False},
                        {"text": "Créer ou rectifier un bord biseauté (chanfrein) sur une arête non amincie (bord coupé), pour faciliter le jointoiement.", "isCorrect": True},
                        {"text": "Percer la plaque.", "isCorrect": False},
                        {"text": "Mesurer la plaque.", "isCorrect": False}
                    ],
                    "correction": "Le **Chanfrein** permet au joint et à la bande de s'intégrer correctement sur une arête coupée."
                },
                {
                    "questionNumber": 36,
                    "question": "Que signifie le marquage **F** sur une plaque de plâtre (ex : PlacoFlam) ?",
                    "answerOptions": [
                        {"text": "Finition.", "isCorrect": False},
                        {"text": "Résistance au feu (contient de la fibre de verre pour retarder la propagation).", "isCorrect": True},
                        {"text": "Froid.", "isCorrect": False},
                        {"text": "Facile à poser.", "isCorrect": False}
                    ],
                    "correction": "La plaque **Feu (F)** (carton rose) est utilisée pour les cloisons ou les plafonds nécessitant une stabilité au feu (CF : Coupe-Feu)."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est le rôle du **bande résiliente** (ou mousse d'étanchéité) sous les rails métalliques d'une cloison ?",
                    "answerOptions": [
                        {"text": "Réduire le bruit des vis.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité à l'air et créer une désolidarisation pour l'isolation phonique (éviter le passage du bruit par le sol/plafond).", "isCorrect": True},
                        {"text": "Faciliter le glissement.", "isCorrect": False},
                        {"text": "Augmenter la résistance au feu.", "isCorrect": False}
                    ],
                    "correction": "La **Bande résiliente** est essentielle pour la performance acoustique (suppression des ponts phoniques)."
                },
                {
                    "questionNumber": 38,
                    "question": "Lors de la pose de plaques au plafond, dans quel sens doit-on orienter la longueur de la plaque ?",
                    "answerOptions": [
                        {"text": "Parallèlement au sens de la lumière (pour cacher les défauts du jointoiement).", "isCorrect": True},
                        {"text": "Perpendiculairement à la lumière.", "isCorrect": False},
                        {"text": "En diagonale.", "isCorrect": False},
                        {"text": "N'importe comment.", "isCorrect": False}
                    ],
                    "correction": "La **pose parallèle à la source de lumière** rend les joints moins visibles une fois finis et peints."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le rôle de la **Trappe de visite** ?",
                    "answerOptions": [
                        {"text": "Ventiler la cloison.", "isCorrect": False},
                        {"text": "Permettre l'accès aux réseaux (plomberie, électricité, VMC) cachés derrière la cloison ou le plafond pour la maintenance.", "isCorrect": True},
                        {"text": "Rendre la cloison plus solide.", "isCorrect": False},
                        {"text": "Réduire le poids.", "isCorrect": False}
                    ],
                    "correction": "La **Trappe de visite** est obligatoire pour accéder aux équipements cachés nécessitant un entretien."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment appelle-t-on le type de découpe qui permet à une plaque de plâtre de s'intégrer autour d'un encadrement de porte, en forme de 'L' inversé ?",
                    "answerOptions": [
                        {"text": "La coupe en V.", "isCorrect": False},
                        {"text": "La coupe en 'L' inversé (pour éviter le joint dans le prolongement de l'encadrement qui est un point de concentration de tensions).", "isCorrect": True},
                        {"text": "La coupe en diagonale.", "isCorrect": False},
                        {"text": "Le chanfreinage.", "isCorrect": False}
                    ],
                    "correction": "La coupe en **'L' inversé** est cruciale pour éviter les fissures dans les angles des baies et des portes."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : ISOLATION THERMIQUE ET ACOUSTIQUE (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Isolation Thermique et Acoustique (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la principale caractéristique de la **Laine de Roche** par rapport à la Laine de Verre ?",
                    "answerOptions": [
                        {"text": "Elle est moins chère.", "isCorrect": False},
                        {"text": "Elle offre une meilleure résistance au feu et de meilleures performances acoustiques.", "isCorrect": True},
                        {"text": "Elle est plus lourde et moins irritante.", "isCorrect": False},
                        {"text": "Elle est moins dense.", "isCorrect": False}
                    ],
                    "correction": "La **Laine de Roche** est un excellent coupe-feu et isolant phonique grâce à sa densité."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le rôle du **Pare-vapeur** (membrane d'étanchéité) dans un système d'isolation ?",
                    "answerOptions": [
                        {"text": "Bloquer la chaleur.", "isCorrect": False},
                        {"text": "Empêcher la vapeur d'eau intérieure de migrer et de condenser dans l'isolant (pour éviter de le dégrader et de diminuer ses performances).", "isCorrect": True},
                        {"text": "Servir de support au placo.", "isCorrect": False},
                        {"text": "Isoler du bruit.", "isCorrect": False}
                    ],
                    "correction": "Le **Pare-vapeur** se pose toujours du côté chaud de la paroi (côté intérieur). Il est indispensable dans les murs froids ou les toitures."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le nom du phénomène de rupture de l'isolation qui permet aux déperditions thermiques d'augmenter (jonction entre deux parois) ?",
                    "answerOptions": [
                        {"text": "L'effet de serre.", "isCorrect": False},
                        {"text": "Le Pont Thermique.", "isCorrect": True},
                        {"text": "La condensation.", "isCorrect": False},
                        {"text": "L'effet Joule.", "isCorrect": False}
                    ],
                    "correction": "Le **Pont Thermique** (souvent aux angles, jonctions mur/sol, mur/plafond) doit être traité par une continuité de l'isolation."
                },
                {
                    "questionNumber": 44,
                    "question": "Dans le cadre de l'Isolation Thermique par l'Extérieur (**ITE**), quel est le rôle du plâtrier-façadier ?",
                    "answerOptions": [
                        {"text": "Poser le chauffage.", "isCorrect": False},
                        {"text": "Fixer les panneaux isolants (PSE, Laine de roche) et réaliser l'enduit de façade armé (treillis de verre) de finition.", "isCorrect": True},
                        {"text": "Installer les fenêtres.", "isCorrect": False},
                        {"text": "Couper les arbres.", "isCorrect": False}
                    ],
                    "correction": "L'**ITE** comprend la pose de l'isolant et l'application d'un système d'enduit de protection."
                },
                {
                    "questionNumber": 45,
                    "question": "Que signifie un indice d'affaiblissement acoustique **R** élevé (en décibels, dB) pour une cloison ?",
                    "answerOptions": [
                        {"text": "Elle est plus mince.", "isCorrect": False},
                        {"text": "Elle est plus performante en matière d'isolation phonique (elle atténue mieux le bruit).", "isCorrect": True},
                        {"text": "Elle est moins chère.", "isCorrect": False},
                        {"text": "Elle est plus légère.", "isCorrect": False}
                    ],
                    "correction": "Plus la valeur **R** est élevée, meilleure est l'isolation phonique (ex : R=50 dB est excellent)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel type d'isolant (sous forme de billes ou de flocons) est souvent utilisé pour l'isolation des combles perdus par soufflage mécanique ?",
                    "answerOptions": [
                        {"text": "Le Polystyrène expansé (PSE).", "isCorrect": False},
                        {"text": "La Laine de roche, la Ouate de cellulose ou la Laine de verre soufflée.", "isCorrect": True},
                        {"text": "La mousse polyuréthane rigide.", "isCorrect": False},
                        {"text": "Le béton cellulaire.", "isCorrect": False}
                    ],
                    "correction": "Le **Soufflage** est la méthode la plus efficace pour couvrir uniformément les surfaces irrégulières."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on l'espace laissé entre le mur et le doublage (plaque isolante) dans le cas d'une isolation par lame d'air (ou ventilation) ?",
                    "answerOptions": [
                        {"text": "Le Joint de dilatation.", "isCorrect": False},
                        {"text": "La Lame d'air (ou Coulisse).", "isCorrect": True},
                        {"text": "Le Pont thermique.", "isCorrect": False},
                        {"text": "L'espace vide.", "isCorrect": False}
                    ],
                    "correction": "La **Lame d'air** doit être continue et ventilée, notamment dans les murs anciens ou humides."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est le risque de couper l'isolant (laine minérale) avec une lame émoussée (non affûtée) ?",
                    "answerOptions": [
                        {"text": "Le froid passe.", "isCorrect": False},
                        {"text": "L'isolant est déchiqueté, ce qui le rend difficile à insérer dans l'ossature et crée des défauts d'isolation (trous ou bourrelets).", "isCorrect": True},
                        {"text": "Le mur s'effondre.", "isCorrect": False},
                        {"text": "La plaque de plâtre tombe.", "isCorrect": False}
                    ],
                    "correction": "Une **coupe nette** (au couteau à isolant) garantit une pose jointive et efficace."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le rôle du **Plot de mortier adhésif** lors du collage d'un doublage isolant sur un mur ?",
                    "answerOptions": [
                        {"text": "Fournir l'isolation.", "isCorrect": False},
                        {"text": "Fixer le panneau isolant et surtout **rattraper la planéité** du mur (les plots sont appliqués en épaisseur variable).", "isCorrect": True},
                        {"text": "Servir de pare-vapeur.", "isCorrect": False},
                        {"text": "Empêcher le feu.", "isCorrect": False}
                    ],
                    "correction": "Le **Plot** permet de garantir la verticalité de l'ouvrage malgré les défauts du mur porteur."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel type d'isolant (souvent bleu ou rose) est caractérisé par sa très faible absorption d'eau et sa rigidité, le rendant idéal pour les sols ou les soubassements ?",
                    "answerOptions": [
                        {"text": "La Laine de verre.", "isCorrect": False},
                        {"text": "Le Polystyrène Extrudé (XPS).", "isCorrect": True},
                        {"text": "La Laine de bois.", "isCorrect": False},
                        {"text": "Le Chanvre.", "isCorrect": False}
                    ],
                    "correction": "Le **Polystyrène Extrudé (XPS)** est parfait pour les zones exposées à l'humidité ou à une forte compression."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le principal danger de la présence d'un **pont thermique** non traité ?",
                    "answerOptions": [
                        {"text": "Bruit excessif.", "isCorrect": False},
                        {"text": "Déperdition de chaleur et risque de condensation (point de rosée) provoquant moisissures et dégradation de la paroi.", "isCorrect": True},
                        {"text": "Feu.", "isCorrect": False},
                        {"text": "Inondation.", "isCorrect": False}
                    ],
                    "correction": "La **condensation** est un problème majeur lié aux ponts thermiques, détruisant les isolants et les finitions."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment doit être posée la laine minérale dans une ossature (rail/montant) pour assurer une bonne isolation phonique ?",
                    "answerOptions": [
                        {"text": "Tassée fortement.", "isCorrect": False},
                        {"text": "Sans être tassée (pour conserver son pouvoir isolant), mais en remplissant parfaitement l'espace entre les montants (pose jointive).", "isCorrect": True},
                        {"text": "Laisser des trous d'air.", "isCorrect": False},
                        {"text": "La coller à l'intérieur.", "isCorrect": False}
                    ],
                    "correction": "Le **tassement** de la laine réduit sa performance. Il faut une pose sans compression, mais sans vide."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle du **Parement de terre cuite** (briquette de plâtre) dans un doublage traditionnel ?",
                    "answerOptions": [
                        {"text": "Servir de pare-vapeur.", "isCorrect": False},
                        {"text": "Créer une base solide et incombustible avant le dressage au plâtre gros et la finition (méthode de plâtrerie traditionnelle).", "isCorrect": True},
                        {"text": "Isoler du bruit.", "isCorrect": False},
                        {"text": "Réduire l'épaisseur.", "isCorrect": False}
                    ],
                    "correction": "La **briquette de plâtre** permet de réaliser un corps d'ouvrage stable sur lequel le plâtrier travaille l'enduit."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'élément essentiel pour la performance acoustique d'une cloison double peau avec isolant ?",
                    "answerOptions": [
                        {"text": "La couleur du placo.", "isCorrect": False},
                        {"text": "La masse (épaisseur des plaques) et la désolidarisation entre les deux faces (lame d'air + bande résiliente).", "isCorrect": True},
                        {"text": "Le type de vis.", "isCorrect": False},
                        {"text": "Le type de peinture.", "isCorrect": False}
                    ],
                    "correction": "L'**Isolation phonique** repose sur le principe masse-ressort-masse."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est l'outil utilisé pour contrôler le taux d'humidité d'un mur avant l'application d'un enduit ou la pose d'une isolation ?",
                    "answerOptions": [
                        {"text": "Le mètre laser.", "isCorrect": False},
                        {"text": "L'Hygromètre (ou Humidimètre).", "isCorrect": True},
                        {"text": "Le niveau à bulle.", "isCorrect": False},
                        {"text": "La règle de maçon.", "isCorrect": False}
                    ],
                    "correction": "L'**Hygromètre** garantit que le support est suffisamment sec pour la pose du doublage (souvent < 5%)."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment appelle-t-on le phénomène où les parois d'une pièce réverbèrent le son (mauvaise acoustique) ?",
                    "answerOptions": [
                        {"text": "Le Pont phonique.", "isCorrect": False},
                        {"text": "La Réverbération (ou Écho).", "isCorrect": True},
                        {"text": "La Réfraction.", "isCorrect": False},
                        {"text": "L'onde de choc.", "isCorrect": False}
                    ],
                    "correction": "La **Réverbération** est traitée par l'ajout de matériaux absorbants (ex : Placo perforé ou isolant acoustique performant)."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est le rôle de la **Membrane d'étanchéité à l'air (MEP)** ?",
                    "answerOptions": [
                        {"text": "Isoler du feu.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité de l'enveloppe du bâtiment pour limiter les fuites d'air non contrôlées (obligatoire en RT2012/RE2020).", "isCorrect": True},
                        {"text": "Soutenir la toiture.", "isCorrect": False},
                        {"text": "Réduire le poids.", "isCorrect": False}
                    ],
                    "correction": "La **MEP** est essentielle pour la performance énergétique et le confort de l'habitat."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel type de plaque de plâtre est utilisé pour le contreventement (rigidité structurelle) d'une maison à ossature bois ?",
                    "answerOptions": [
                        {"text": "Placo standard.", "isCorrect": False},
                        {"text": "Placo OSB (panneau OSB avec une couche de plâtre) ou Placo avec renforts bois/fibres.", "isCorrect": True},
                        {"text": "Placo rose (Feu).", "isCorrect": False},
                        {"text": "Placo vert (Hydro).", "isCorrect": False}
                    ],
                    "correction": "Le **Contreventement** assure la stabilité du bâtiment contre les forces horizontales (vent, séisme)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle est l'importance de l'épaisseur de la **lame d'air** derrière un doublage isolant (par plots) ?",
                    "answerOptions": [
                        {"text": "Elle doit être la plus grande possible.", "isCorrect": False},
                        {"text": "Elle doit être au minimum de 2 cm et continue, pour assurer la ventilation et réduire l'effet de condensation.", "isCorrect": True},
                        {"text": "Elle n'a pas d'importance.", "isCorrect": False},
                        {"text": "Elle doit être remplie d'isolant.", "isCorrect": False}
                    ],
                    "correction": "Un minimum de **2 cm** est requis pour la ventilation."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment s'appelle l'outil qui permet de mesurer la quantité de chaleur perdue par les parois (pour détecter les ponts thermiques) ?",
                    "answerOptions": [
                        {"text": "Le Mètre laser.", "isCorrect": False},
                        {"text": "La Caméra thermique (ou Thermographie).", "isCorrect": True},
                        {"text": "Le luxmètre.", "isCorrect": False},
                        {"text": "L'anémomètre.", "isCorrect": False}
                    ],
                    "correction": "La **Caméra thermique** est utilisée pour le diagnostic des performances thermiques."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : ENDUITS, PLÂTRE TRADITIONNEL ET FINITIONS (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Enduits, Plâtre Traditionnel et Finitions (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le rôle de la **Bande armée** (ou Bande de renfort) dans les angles sortants (arêtes) d'une cloison en placo ?",
                    "answerOptions": [
                        {"text": "Assurer l'isolation phonique.", "isCorrect": False},
                        {"text": "Protéger l'arête contre les chocs et garantir un angle parfaitement droit (bande avec une armature métallique ou PVC).", "isCorrect": True},
                        {"text": "Faciliter le séchage.", "isCorrect": False},
                        {"text": "Servir de fixation.", "isCorrect": False}
                    ],
                    "correction": "La **Bande armée** (ou Cornière) est essentielle pour la durabilité des angles sortants, très exposés aux chocs."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le risque de ne pas respecter le temps de séchage entre deux couches d'enduit ?",
                    "answerOptions": [
                        {"text": "L'enduit devient trop dur.", "isCorrect": False},
                        {"text": "La couche inférieure n'est pas stable, ce qui entraîne des fissures, un décollement ou une mauvaise adhérence de la couche supérieure.", "isCorrect": True},
                        {"text": "L'enduit devient trop mou.", "isCorrect": False},
                        {"text": "L'enduit change de couleur.", "isCorrect": False}
                    ],
                    "correction": "Le **temps de séchage** est indiqué par le fabricant et doit être respecté (souvent 24 heures)."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on le procédé qui consiste à humidifier légèrement le plâtre ou l'enduit avec de l'eau, juste avant qu'il ne fasse sa prise finale (pour le lisser) ?",
                    "answerOptions": [
                        {"text": "Le Gâchage.", "isCorrect": False},
                        {"text": "Le Serrage (ou Resserrage).", "isCorrect": True},
                        {"text": "Le Grattage.", "isCorrect": False},
                        {"text": "Le Jointage.", "isCorrect": False}
                    ],
                    "correction": "Le **Serrage** (ou passage de l'éponge) permet d'obtenir un aspect très lisse et de bloquer la prise."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est l'outil utilisé pour poncer (abraser) l'enduit de jointoiement ou le plâtre de finition avant la peinture ?",
                    "answerOptions": [
                        {"text": "Le papier journal.", "isCorrect": False},
                        {"text": "La ponceuse girafe (électrique, pour les grandes surfaces) ou la cale à poncer manuelle (avec abrasif fin : grain 120 à 180).", "isCorrect": True},
                        {"text": "Le fer à lisser.", "isCorrect": False},
                        {"text": "La truelle.", "isCorrect": False}
                    ],
                    "correction": "Le **Ponçage** est l'étape de finition cruciale pour obtenir une surface sans défaut."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel type de plâtre est utilisé pour sceller rapidement et définitivement des huisseries (dormants de portes) ou des pièces métalliques dans la maçonnerie ?",
                    "answerOptions": [
                        {"text": "Le plâtre fin de lissage.", "isCorrect": False},
                        {"text": "Le Plâtre à prise rapide (ou Plâtre de scellement).", "isCorrect": True},
                        {"text": "Le plâtre coloré.", "isCorrect": False},
                        {"text": "L'enduit à joint.", "isCorrect": False}
                    ],
                    "correction": "Le **Plâtre à prise rapide** prend en quelques minutes et permet de bloquer la pièce sans attente."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le rôle du **Rouleau à débuller** lors de l'application d'un revêtement (ex : résine ou mortier de sol) ?",
                    "answerOptions": [
                        {"text": "Lisser la surface.", "isCorrect": False},
                        {"text": "Éliminer les bulles d'air emprisonnées dans le produit liquide, pour éviter les défauts de surface et garantir la solidité (surtout pour les sols auto-nivellants).", "isCorrect": True},
                        {"text": "Mélanger le produit.", "isCorrect": False},
                        {"text": "Projeter le produit.", "isCorrect": False}
                    ],
                    "correction": "Le **Rouleau à débuller** est spécifique aux produits fluides comme les chapes ou résines."
                },
                {
                    "questionNumber": 67,
                    "question": "Comment appelle-t-on le produit appliqué en première couche sur une surface poreuse (plâtre ou enduit) avant la peinture de finition, pour fixer le fond et réguler l'absorption ?",
                    "answerOptions": [
                        {"text": "La laque.", "isCorrect": False},
                        {"text": "Le Fixateur ou Primaire d'impression (ou 'Sous-couche').", "isCorrect": True},
                        {"text": "Le Vernis.", "isCorrect": False},
                        {"text": "Le Diluant.", "isCorrect": False}
                    ],
                    "correction": "La **Sous-couche d'impression** est essentielle pour obtenir une finition de peinture uniforme et durable."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle est la particularité des **enduits à la chaux** (ou chaux-chanvre) ?",
                    "answerOptions": [
                        {"text": "Ils sèchent très vite.", "isCorrect": False},
                        {"text": "Ils sont 'respirants' (perméables à la vapeur d'eau), régulant l'humidité et idéaux pour la rénovation de murs anciens et humides.", "isCorrect": True},
                        {"text": "Ils sont très chers.", "isCorrect": False},
                        {"text": "Ils sont très lisses.", "isCorrect": False}
                    ],
                    "correction": "La **Chaux** est le matériau de choix en écoconstruction et rénovation du bâti ancien (laisse 'respirer' le mur)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est l'outil utilisé pour lisser et polir un enduit très fin (enduit à l'eau) pour obtenir un aspect 'miroir' ou stuc ?",
                    "answerOptions": [
                        {"text": "Le rouleau.", "isCorrect": False},
                        {"text": "Le fer à lisser ou la Taloche à polir.", "isCorrect": True},
                        {"text": "La brosse.", "isCorrect": False},
                        {"text": "La spatule.", "isCorrect": False}
                    ],
                    "correction": "Le **Fer à lisser** est le geste final du plâtrier pour les finitions haut de gamme."
                },
                {
                    "questionNumber": 70,
                    "question": "Pourquoi doit-on obligatoirement utiliser un **enduit spécifique (enduit P3)** pour les joints de plaques de plâtre à l'extérieur (sous abri, zone exposée) ?",
                    "answerOptions": [
                        {"text": "Pour la couleur.", "isCorrect": False},
                        {"text": "Les enduits classiques ne sont pas résistants à l'humidité. L'enduit P3 est conçu pour les environnements humides et le milieu extérieur (résistance à l'eau).", "isCorrect": True},
                        {"text": "Pour la rapidité.", "isCorrect": False},
                        {"text": "Pour la facilité de ponçage.", "isCorrect": False}
                    ],
                    "correction": "L'**Enduit P3** est la norme pour la résistance à l'eau."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment doit-on nettoyer les outils (truelle, platoir, mélangeur) après le gâchage du plâtre ?",
                    "answerOptions": [
                        {"text": "Les laisser sécher.", "isCorrect": False},
                        {"text": "Les nettoyer immédiatement avec de l'eau avant que le plâtre ne fasse sa prise (une fois sec, le plâtre est très difficile à enlever).", "isCorrect": True},
                        {"text": "Les jeter.", "isCorrect": False},
                        {"text": "Les poncer.", "isCorrect": False}
                    ],
                    "correction": "Le **Nettoyage immédiat** prolonge la durée de vie des outils et garantit la propreté du gâchage suivant."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le rôle de la **Fibre de verre** (ou fibre de trame) dans les enduits de façade (ITE) ?",
                    "answerOptions": [
                        {"text": "Augmenter l'isolation.", "isCorrect": False},
                        {"text": "Renforcer l'enduit contre la fissuration (contraintes thermiques et mécaniques) et assurer sa cohésion.", "isCorrect": True},
                        {"text": "Réduire le poids.", "isCorrect": False},
                        {"text": "Donner une couleur.", "isCorrect": False}
                    ],
                    "correction": "La **Trame de fibre de verre** est essentielle dans les systèmes d'Isolation par l'Extérieur (ITE)."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le danger de réutiliser de l'eau de gâchage ayant déjà servi pour du plâtre ou du ciment ?",
                    "answerOptions": [
                        {"text": "Le mélange sera trop liquide.", "isCorrect": False},
                        {"text": "Les résidus accélèrent la prise du nouveau plâtre (prise 'éclair'), le rendant inutilisable.", "isCorrect": True},
                        {"text": "Le mélange sera trop lourd.", "isCorrect": False},
                        {"text": "Le mélange sera trop froid.", "isCorrect": False}
                    ],
                    "correction": "Il faut toujours utiliser de l'**eau propre** pour le gâchage."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment appelle-t-on le défaut de lissage d'un enduit de finition qui présente des petites rayures circulaires ?",
                    "answerOptions": [
                        {"text": "L'effritement.", "isCorrect": False},
                        {"text": "Le Faïençage (ou Coudage).", "isCorrect": True},
                        {"text": "La fissuration.", "isCorrect": False},
                        {"text": "Le cloquage.", "isCorrect": False}
                    ],
                    "correction": "Le **Faïençage** est souvent dû à une mauvaise technique de lissage (fer à lisser mal tenu ou enduit trop sec)."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est l'outil utilisé pour rectifier les défauts de surface d'un mur enduit ou plâtré après le dressage (en enlevant de la matière) ?",
                    "answerOptions": [
                        {"text": "Le pinceau.", "isCorrect": False},
                        {"text": "La Grattoir ou la Griffe (pour enduit traditionnel).", "isCorrect": True},
                        {"text": "La truelle.", "isCorrect": False},
                        {"text": "Le cutter.", "isCorrect": False}
                    ],
                    "correction": "Le **Grattage** est utilisé pour obtenir une finition rustique ou pour préparer la surface à la couche de finition."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le risque de ne pas traiter les vis (TTPC) avec de l'enduit lors du jointoiement ?",
                    "answerOptions": [
                        {"text": "La vis va rouiller.", "isCorrect": False},
                        {"text": "Le métal de la vis peut rouiller (humidité) et faire apparaître des **points de rouille** visibles à travers la peinture (pont de rouille).", "isCorrect": True},
                        {"text": "La vis va se desserrer.", "isCorrect": False},
                        {"text": "La plaque va tomber.", "isCorrect": False}
                    ],
                    "correction": "Il faut appliquer deux à trois passes d'enduit sur la tête des vis."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est la principale caractéristique de la **Bande calicot** pour le jointoiement (bande papier) ?",
                    "answerOptions": [
                        {"text": "Elle est auto-adhésive.", "isCorrect": False},
                        {"text": "Elle est très résistante à la traction et sert à prévenir la fissuration des joints entre plaques.", "isCorrect": True},
                        {"text": "Elle est imperméable.", "isCorrect": False},
                        {"text": "Elle est en métal.", "isCorrect": False}
                    ],
                    "correction": "La **Bande papier** est la plus efficace contre la fissuration. La bande en fibre de verre (grillage) est plus pour la réparation."
                },
                {
                    "questionNumber": 78,
                    "question": "Combien de couches d'enduit sont généralement nécessaires pour un jointoiement standard (bande papier) ?",
                    "answerOptions": [
                        {"text": "Une seule couche.", "isCorrect": False},
                        {"text": "Trois couches (une passe pour coller la bande, une passe de charge pour couvrir, une passe de finition/lissage).", "isCorrect": True},
                        {"text": "Cinq couches.", "isCorrect": False},
                        {"text": "Aucune couche.", "isCorrect": False}
                    ],
                    "correction": "La **technique des 3 passes** assure la résistance et l'invisibilité du joint."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment appelle-t-on le défaut où de petites bosses (ou grumeaux) apparaissent lors de la pose d'un enduit ?",
                    "answerOptions": [
                        {"text": "Le Lissage.", "isCorrect": False},
                        {"text": "Le Piquage (ou Grumeaux).", "isCorrect": True},
                        {"text": "Le Cloquage.", "isCorrect": False},
                        {"text": "Le Glissement.", "isCorrect": False}
                    ],
                    "correction": "Le **Piquage** est souvent dû à un mauvais gâchage (mélange insuffisant) ou à l'utilisation d'outils ou d'eau sales."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le rôle du **Mastic acrylique** dans les travaux de finition d'un plâtrier ?",
                    "answerOptions": [
                        {"text": "Coller le placo.", "isCorrect": False},
                        {"text": "Faire le joint entre un dormant de porte et une cloison (joint de finition, peignable) ou reboucher des petites fissures intérieures.", "isCorrect": True},
                        {"text": "Isoler de l'eau.", "isCorrect": False},
                        {"text": "Fixer les montants.", "isCorrect": False}
                    ],
                    "correction": "Le **Mastic acrylique** est idéal pour les joints de finition intérieurs car il peut être peint, contrairement au silicone."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : MISE EN ŒUVRE ET CONFORMITÉ (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Mise en Œuvre et Conformité (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel type de plaque de plâtre doit-on choisir si l'on installe une télévision ou un meuble lourd (charge concentrée) sur la cloison ?",
                    "answerOptions": [
                        {"text": "Placo standard (BA13).", "isCorrect": False},
                        {"text": "La plaque haute dureté (ex : Placo Activ'Air, Placo Impact) ou une double épaisseur, pour une meilleure résistance aux chocs et à la charge.", "isCorrect": True},
                        {"text": "Placo Hydro.", "isCorrect": False},
                        {"text": "Placo Feu.", "isCorrect": False}
                    ],
                    "correction": "La **Plaque haute dureté** est recommandée pour les cloisons soumises à des charges importantes ou des chocs fréquents."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le risque de ne pas croiser les plaques lors de la pose d'une cloison d'angle (jonction de deux cloisons) ?",
                    "answerOptions": [
                        {"text": "L'angle sera trop rond.", "isCorrect": False},
                        {"text": "L'angle ne sera pas solidaire et risque de fissurer (les plaques doivent se recouvrir en alternance pour lier mécaniquement l'angle).", "isCorrect": True},
                        {"text": "Le mur sera trop haut.", "isCorrect": False},
                        {"text": "L'isolation sera trop forte.", "isCorrect": False}
                    ],
                    "correction": "L'**Angle croisé** est une règle de pose pour éviter les fissures dans les angles."
                },
                {
                    "questionNumber": 83,
                    "question": "Comment appelle-t-on le document qui liste les étapes et les exigences techniques de pose pour un système donné (ex : Cloison Placostil) ?",
                    "answerOptions": [
                        {"text": "Le Bon de commande.", "isCorrect": False},
                        {"text": "Le Cahier des Clauses Techniques (CCTP) ou la Documentation Technique du Fabricant (DTF/DTU).", "isCorrect": True},
                        {"text": "Le plan de masse.", "isCorrect": False},
                        {"text": "La facture.", "isCorrect": False}
                    ],
                    "correction": "Le **DTU** (Document Technique Unifié) est la référence légale des règles de l'art."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le rôle du **Cornière (ou Profilé) de rive** dans un plafond suspendu ?",
                    "answerOptions": [
                        {"text": "Tenir le luminaire.", "isCorrect": False},
                        {"text": "Servir de support périphérique et de finition entre le plafond et le mur (guide de niveau).", "isCorrect": True},
                        {"text": "Servir de rail.", "isCorrect": False},
                        {"text": "Isoler du bruit.", "isCorrect": False}
                    ],
                    "correction": "La **Cornière de rive** donne l'alignement et assure la finition esthétique sur le périmètre."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle doit être la hauteur minimale de l'**enduit extérieur** (crépi) au-dessus du niveau du sol fini pour éviter les remontées d'humidité ?",
                    "answerOptions": [
                        {"text": "5 cm.", "isCorrect": False},
                        {"text": "15 cm minimum (pour éviter le contact direct avec l'eau de ruissellement et les éclaboussures).", "isCorrect": True},
                        {"text": "50 cm.", "isCorrect": False},
                        {"text": "1 cm.", "isCorrect": False}
                    ],
                    "correction": "Le **15 cm** est une règle de base pour la durabilité du revêtement de façade."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est l'outil utilisé pour écarter (ou lever) les plaques de plâtre pour les plaquer contre le rail haut, en laissant le jeu de dilatation au sol ?",
                    "answerOptions": [
                        {"text": "La truelle.", "isCorrect": False},
                        {"text": "Le Lève-plaque au pied (ou au genou).", "isCorrect": True},
                        {"text": "Le mètre ruban.", "isCorrect": False},
                        {"text": "La spatule.", "isCorrect": False}
                    ],
                    "correction": "Le **Lève-plaque au pied** permet de positionner la plaque avec précision et sans effort (pour le plaquage au rail haut)."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la cause la plus fréquente d'un **fissure** dans un joint de placo, peu de temps après la pose ?",
                    "answerOptions": [
                        {"text": "L'utilisation d'une mauvaise peinture.", "isCorrect": False},
                        {"text": "Un défaut dans l'ossature (montant non solidaire) ou un manque de rigidité dans l'ossature (montants trop espacés ou non croisés).", "isCorrect": True},
                        {"text": "Un isolant trop épais.", "isCorrect": False},
                        {"text": "Un rail trop court.", "isCorrect": False}
                    ],
                    "correction": "La **fissuration** est presque toujours liée à un mouvement ou à une contrainte mécanique de l'ossature."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment appelle-t-on le procédé qui consiste à injecter un matériau isolant (mousse PU, billes) dans une lame d'air ou un vide de construction existant ?",
                    "answerOptions": [
                        {"text": "Le Flocage.", "isCorrect": False},
                        {"text": "L'Injection (ou Insufflation).", "isCorrect": True},
                        {"text": "Le Calage.", "isCorrect": False},
                        {"text": "Le Scellement.", "isCorrect": False}
                    ],
                    "correction": "L'**Injection** est une méthode d'isolation utilisée pour les murs doubles ou les caissons."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le rôle du **Pistage** (ou repérage) dans l'application de plâtre traditionnel ?",
                    "answerOptions": [
                        {"text": "Découper le plâtre.", "isCorrect": False},
                        {"text": "Appliquer des petites quantités de plâtre pour créer des repères d'épaisseur (les 'pistes') pour le dressage (épaisseur constante).", "isCorrect": True},
                        {"text": "Mélanger le plâtre.", "isCorrect": False},
                        {"text": "Poncer le plâtre.", "isCorrect": False}
                    ],
                    "correction": "Le **Pistage** permet au plâtrier de garantir la planéité et l'épaisseur voulue de l'ouvrage (dressage)."
                },
                {
                    "questionNumber": 90,
                    "question": "Pourquoi le plâtre ou l'enduit doit-il toujours être appliqué à une température ambiante minimale (souvent 5 °C) ?",
                    "answerOptions": [
                        {"text": "Pour la couleur.", "isCorrect": False},
                        {"text": "Une température trop basse ralentit ou empêche la prise chimique du produit et le séchage, ce qui affecte la solidité et la durabilité.", "isCorrect": True},
                        {"text": "Pour la sécurité.", "isCorrect": False},
                        {"text": "Pour la texture.", "isCorrect": False}
                    ],
                    "correction": "La **température** est un facteur clé pour la bonne prise et le séchage (durcissement) du plâtre et du ciment."
                },
                {
                    "questionNumber": 91,
                    "question": "Comment appelle-t-on la technique qui consiste à faire 'saigner' le plâtre (remonter la laitance) à la surface en le vibrant ?",
                    "answerOptions": [
                        {"text": "Le Ponçage.", "isCorrect": False},
                        {"text": "Le Lissaged.", "isCorrect": True},
                        {"text": "Le Scellement.", "isCorrect": False},
                        {"text": "Le Gâchage.", "isCorrect": False}
                    ],
                    "correction": "Le **Lissage** (ou talochage à l'eau) fait remonter le produit le plus fin et l'eau pour un aspect lisse."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le risque de percer un trou (pour une gaine) dans une plaque de plâtre trop près des bords d'un montant (ossature) ?",
                    "answerOptions": [
                        {"text": "Le trou sera trop grand.", "isCorrect": False},
                        {"text": "La résistance du montant est réduite et il peut plier ou se déformer, ce qui fragilise la cloison (ne jamais percer le montant à moins de 10 cm de la tête).", "isCorrect": True},
                        {"text": "Le trou sera trop petit.", "isCorrect": False},
                        {"text": "La vis ne tiendra pas.", "isCorrect": False}
                    ],
                    "correction": "Les percements doivent se faire au centre du montant et loin des bords."
                },
                {
                    "questionNumber": 93,
                    "question": "Quelle est la principale caractéristique de la **Véranda ou VMC double flux** dans le cadre de l'isolation et de la conformité (RE2020) ?",
                    "answerOptions": [
                        {"text": "Elle n'est pas efficace.", "isCorrect": False},
                        {"text": "Elle permet de récupérer les calories de l'air vicié pour préchauffer l'air neuf (réduction des déperditions par ventilation).", "isCorrect": True},
                        {"text": "Elle est très bruyante.", "isCorrect": False},
                        {"text": "Elle consomme beaucoup d'énergie.", "isCorrect": False}
                    ],
                    "correction": "La **VMC double flux** est un élément essentiel des bâtiments basse consommation (BB C)."
                },
                {
                    "questionNumber": 94,
                    "question": "Que doit-on faire avant de fixer un rail ou un montant au sol/plafond en béton ?",
                    "answerOptions": [
                        {"text": "Le peindre.", "isCorrect": False},
                        {"text": "Le tracer avec précision, mettre une bande résiliente et percer avec un perforateur (cheville à frapper ou vis à béton).", "isCorrect": True},
                        {"text": "Le coller au mastic.", "isCorrect": False},
                        {"text": "Le poncer.", "isCorrect": False}
                    ],
                    "correction": "La **Bande résiliente** est obligatoire pour l'étanchéité et le phonique."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le risque si les joints de plaques de plâtre ne sont pas entièrement recouverts et lissés sur une largeur suffisante (environ 20 cm) ?",
                    "answerOptions": [
                        {"text": "Le mur sera trop isolant.", "isCorrect": False},
                        {"text": "Le joint (léger creux/surépaisseur) sera visible après la peinture (phénomène d'**auréole** ou d'ombre portée).", "isCorrect": True},
                        {"text": "La peinture va fissurer.", "isCorrect": False},
                        {"text": "La plaque sera trop dure.", "isCorrect": False}
                    ],
                    "correction": "Un **lissage large et dégradé** est la clé d'une finition invisible."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment appelle-t-on le revêtement (en PVC, aluminium ou zinc) qui assure l'étanchéité et l'esthétique du bord inférieur d'une ITE (Isolation Thermique par l'Extérieur) ?",
                    "answerOptions": [
                        {"text": "La cornière.", "isCorrect": False},
                        {"text": "Le Profilé de départ (ou Bavette de soubassement).", "isCorrect": True},
                        {"text": "La grille.", "isCorrect": False},
                        {"text": "Le solin.", "isCorrect": False}
                    ],
                    "correction": "Le **Profilé de départ** assure la jonction avec le sol et empêche l'humidité de remonter sous l'isolant."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est l'outil utilisé pour nettoyer les bavures et les surplus de plâtre ou d'enduit sur un mur après la prise ?",
                    "answerOptions": [
                        {"text": "La brosse.", "isCorrect": False},
                        {"text": "Le Couvre-joint (ou Couteau à enduire) et la spatule.", "isCorrect": True},
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "Le cutter.", "isCorrect": False}
                    ],
                    "correction": "L'outil doit être bien nettoyé pour ne pas laisser de traces d'enduit durci."
                },
                {
                    "questionNumber": 98,
                    "question": "Dans le cas d'un doublage collé (par plots), quel est le risque de poser la plaque sans vérifier l'aplomb et la planéité du panneau ?",
                    "answerOptions": [
                        {"text": "Elle va changer de couleur.", "isCorrect": False},
                        {"text": "La finition (peinture ou revêtement) mettra en évidence le défaut de planéité (pente, ventre, creux).", "isCorrect": True},
                        {"text": "Elle sera trop isolante.", "isCorrect": False},
                        {"text": "Elle va fissurer.", "isCorrect": False}
                    ],
                    "correction": "L'**Aplomb** et le **Niveau** sont contrôlés au laser ou au fil à plomb dès la pose du premier plot et du panneau."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le rôle du **Joint de dilatation** dans une grande cloison de plus de 10 à 15 mètres de long ?",
                    "answerOptions": [
                        {"text": "Rendre la cloison plus solide.", "isCorrect": False},
                        {"text": "Permettre à la cloison de se dilater et de se contracter (variations thermiques et hydriques) sans fissurer, en créant une rupture contrôlée.", "isCorrect": True},
                        {"text": "Améliorer l'isolation.", "isCorrect": False},
                        {"text": "Faciliter la peinture.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint de dilatation** est une coupure totale dans la plaque et l'ossature qui absorbe les mouvements."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel outil permet de vérifier la parfaite **verticalité** d'un montant d'ossature ?",
                    "answerOptions": [
                        {"text": "Le niveau à bulle (pour l'horizontalité).", "isCorrect": False},
                        {"text": "Le Fil à plomb ou le Niveau laser.", "isCorrect": True},
                        {"text": "La règle.", "isCorrect": False},
                        {"text": "Le mètre ruban.", "isCorrect": False}
                    ],
                    "correction": "L'**Aplomb** est l'axe vertical. Le fil à plomb ou le laser sont les outils de référence."
                },
            ]
        }
    }
}

# Exemple d'accès aux données :
# print(quiz_data["title"])
# print(quiz_data["themes"][3]["name"])
# print(quiz_data["themes"][3]["questions"][4]["question"])
# print(quiz_data["themes"][3]["questions"][4]["answerOptions"][2]["isCorrect"])