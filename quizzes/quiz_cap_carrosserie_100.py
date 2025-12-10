quiz_data = {
    "title": "Quiz CAP Carrosserie/Peinture : Technologie, Réparation, Mesure et Sécurité (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET ASSEMBLAGES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET ASSEMBLAGES (Questions 1 à 20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la caractéristique principale d'un acier HLE ?",
                    "answerOptions": [
                        {"text": "Une limite d'élasticité élevée", "isCorrect": True},
                        {"text": "Une protection anticorrosion par galvanisation à chaud", "isCorrect": False},
                        {"text": "Une capacité à être soudé sans gaz de protection", "isCorrect": False},
                        {"text": "Une structure en nid d'abeille composite", "isCorrect": False}
                    ],
                    "correction": "HLE signifie Haute Limite Élastique. Ces aciers peuvent subir de fortes contraintes avant de se déformer définitivement, permettant d'alléger les structures tout en gardant la solidité."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel gaz est requis pour le soudage MAG des aciers courants ?",
                    "answerOptions": [
                        {"text": "Un mélange d'Argon et de dioxyde de carbone", "isCorrect": True},
                        {"text": "De l'Argon pur pour éviter l'oxydation", "isCorrect": False},
                        {"text": "De l'oxygène pur pour augmenter la chaleur", "isCorrect": False},
                        {"text": "De l'acétylène dissous", "isCorrect": False}
                    ],
                    "correction": "Le MAG (Metal Active Gas) nécessite un gaz actif. Le CO2 ajouté à l'Argon stabilise l'arc et favorise la pénétration, contrairement à l'Argon pur utilisé pour l'aluminium (MIG)."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment réagit un thermodurcissable lors d'un test de chauffe ?",
                    "answerOptions": [
                        {"text": "Il carbonise sans fondre", "isCorrect": True},
                        {"text": "Il ramollit et peut être remodelé", "isCorrect": False},
                        {"text": "Il devient liquide comme de l'eau", "isCorrect": False},
                        {"text": "Il devient transparent", "isCorrect": False}
                    ],
                    "correction": "Les thermodurcissables (comme le SMC ou les résines polyesters) ont durci irréversiblement lors de leur fabrication. Ils ne peuvent pas être soudés, seulement collés."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle précaution est spécifique au redressage de l'aluminium ?",
                    "answerOptions": [
                        {"text": "Effectuer une chauffe de recuit pour éviter les criques", "isCorrect": True},
                        {"text": "Refroidir brutalement la zone avec de l'eau", "isCorrect": False},
                        {"text": "Utiliser impérativement des marteaux en acier trempé", "isCorrect": False},
                        {"text": "Magnétiser la zone avant de frapper", "isCorrect": False}
                    ],
                    "correction": "L'aluminium s'écrouit (durcit) très vite sous les chocs et devient cassant. Le recuit (vers 300°C) redonne de la malléabilité au métal."
                },
                {
                    "questionNumber": 5,
                    "question": "Le soudo-brasage MIG utilise un fil d'apport constitué de :",
                    "answerOptions": [
                        {"text": "Cuivre et silicium", "isCorrect": True},
                        {"text": "Acier inoxydable enrichi au carbone", "isCorrect": False},
                        {"text": "Aluminium pur", "isCorrect": False},
                        {"text": "Fer doux standard", "isCorrect": False}
                    ],
                    "correction": "Le fil CuSi3 (Cupro-Silicium) fond à une température plus basse que l'acier (environ 1000°C), ce qui permet d'assembler les tôles HLE sans détruire leur structure ni leur protection anticorrosion."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le but principal de la cataphorèse en usine ?",
                    "answerOptions": [
                        {"text": "Protéger la caisse contre la corrosion", "isCorrect": True},
                        {"text": "Donner la couleur finale du véhicule", "isCorrect": False},
                        {"text": "Insonoriser l'habitacle", "isCorrect": False},
                        {"text": "Coller les différents panneaux entre eux", "isCorrect": False}
                    ],
                    "correction": "C'est un dépôt de peinture par électrolyse dans un bain, qui couvre 100% de la surface, y compris les corps creux, pour une protection antirouille totale."
                },
                {
                    "questionNumber": 7,
                    "question": "Les aciers au Bore sont principalement utilisés pour :",
                    "answerOptions": [
                        {"text": "Les renforts de sécurité indéformables", "isCorrect": True},
                        {"text": "Les ailes avant pour leur souplesse", "isCorrect": False},
                        {"text": "Les peaux de portières", "isCorrect": False},
                        {"text": "Le plancher de coffre", "isCorrect": False}
                    ],
                    "correction": "Ces aciers ultra-durs (THLE) sont placés dans les montants de baie ou les traverses pour protéger la cellule de survie. Ils ne se redressent pas."
                },
                {
                    "questionNumber": 8,
                    "question": "L'avantage d'un rivet aveugle est de permettre l'assemblage :",
                    "answerOptions": [
                        {"text": "En n'accédant qu'à un seul côté des tôles", "isCorrect": True},
                        {"text": "Sans avoir besoin de percer les tôles au préalable", "isCorrect": False},
                        {"text": "De manière invisible après la pose", "isCorrect": False},
                        {"text": "Avec une simple pince multiprise", "isCorrect": False}
                    ],
                    "correction": "Appelé aussi rivet 'pop', il est idéal pour les corps creux où l'on ne peut pas passer un tas ou une bouterolle derrière."
                },
                {
                    "questionNumber": 9,
                    "question": "La corrosion galvanique se produit par contact entre :",
                    "answerOptions": [
                        {"text": "Deux métaux de nature différente en milieu humide", "isCorrect": True},
                        {"text": "Une tôle et un mastic polyester", "isCorrect": False},
                        {"text": "La peinture et le vernis", "isCorrect": False},
                        {"text": "L'acier et de l'huile moteur", "isCorrect": False}
                    ],
                    "correction": "C'est un phénomène de pile électrochimique. L'aluminium se corrode s'il est en contact direct avec de l'acier et de l'eau. Il faut isoler les assemblages."
                },
                {
                    "questionNumber": 10,
                    "question": "Le verre feuilleté est composé de :",
                    "answerOptions": [
                        {"text": "Deux feuilles de verre collées par un film plastique", "isCorrect": True},
                        {"text": "Une seule feuille de verre trempé thermiquement", "isCorrect": False},
                        {"text": "Un plastique polycarbonate incassable", "isCorrect": False},
                        {"text": "Trois couches de verre armé de fil de fer", "isCorrect": False}
                    ],
                    "correction": "Obligatoire pour le pare-brise, le film PVB retient les éclats en cas de choc, assurant la sécurité des passagers."
                },
                {
                    "questionNumber": 11,
                    "question": "Le collage structural est souvent associé au rivetage pour :",
                    "answerOptions": [
                        {"text": "Répartir les efforts et assurer l'étanchéité", "isCorrect": True},
                        {"text": "Éviter d'utiliser des outils pneumatiques", "isCorrect": False},
                        {"text": "Faire des économies de rivets", "isCorrect": False},
                        {"text": "Remplacer totalement la soudure sur le châssis", "isCorrect": False}
                    ],
                    "correction": "C'est la technique du 'rivetage-collage'. La colle assure la tenue mécanique continue et l'étanchéité, les rivets maintiennent le tout pendant la prise."
                },
                {
                    "questionNumber": 12,
                    "question": "Un fusible structurel sur un longeron sert à :",
                    "answerOptions": [
                        {"text": "Programmer la déformation en un point précis", "isCorrect": True},
                        {"text": "Couper le circuit électrique en cas de choc", "isCorrect": False},
                        {"text": "Empêcher toute pliure du châssis", "isCorrect": False},
                        {"text": "Fixer le pare-chocs avant", "isCorrect": False}
                    ],
                    "correction": "Ce sont des amorces de pliure (trous, emboutis) qui garantissent que le longeron s'écrase en accordéon pour absorber l'énergie sans transmettre le choc à l'habitacle."
                },
                {
                    "questionNumber": 13,
                    "question": "Le soudage par résistance par points chauffe le métal grâce à :",
                    "answerOptions": [
                        {"text": "L'intensité du courant électrique traversant les tôles", "isCorrect": True},
                        {"text": "La friction mécanique des électrodes", "isCorrect": False},
                        {"text": "Un apport de gaz combustible", "isCorrect": False},
                        {"text": "Un arc électrique créé par une électrode enrobée", "isCorrect": False}
                    ],
                    "correction": "C'est l'effet Joule. La résistance des tôles au passage du courant crée la chaleur nécessaire à la fusion du noyau sous la pression des pinces."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel plastique est un thermoplastique courant en automobile ?",
                    "answerOptions": [
                        {"text": "Le Polypropylène", "isCorrect": True},
                        {"text": "Le Polyester armé de fibres de verre", "isCorrect": False},
                        {"text": "La résine Époxy", "isCorrect": False},
                        {"text": "Le Polyuréthane thermodurci", "isCorrect": False}
                    ],
                    "correction": "Le PP (ou PP-EPDM) est utilisé pour la majorité des pare-chocs car il est souple et se soude facilement à chaud."
                },
                {
                    "questionNumber": 15,
                    "question": "La protection cathodique de l'acier est assurée par :",
                    "answerOptions": [
                        {"text": "Le zinc", "isCorrect": True},
                        {"text": "Le carbone", "isCorrect": False},
                        {"text": "Le cuivre", "isCorrect": False},
                        {"text": "Le fer", "isCorrect": False}
                    ],
                    "correction": "Dans une tôle zinguée, le zinc s'oxyde 'à la place' de l'acier, protégeant ce dernier même si la couche est légèrement rayée."
                },
                {
                    "questionNumber": 16,
                    "question": "Le sertissage de peau de porte est un assemblage :",
                    "answerOptions": [
                        {"text": "Mécanique par repliage du bord", "isCorrect": True},
                        {"text": "Chimique par fusion de la matière", "isCorrect": False},
                        {"text": "Thermique par soudure continue", "isCorrect": False},
                        {"text": "Provisoire par vis", "isCorrect": False}
                    ],
                    "correction": "La tôle extérieure est repliée sur la doublure intérieure. On ajoute un cordon de mastic pour l'étanchéité et le calage."
                },
                {
                    "questionNumber": 17,
                    "question": "Le soudage MIG de l'aluminium impose l'usage d'un gaz :",
                    "answerOptions": [
                        {"text": "Inerte comme l'Argon pur", "isCorrect": True},
                        {"text": "Actif comme le dioxyde de carbone", "isCorrect": False},
                        {"text": "Oxydant comme l'oxygène", "isCorrect": False},
                        {"text": "Combustible comme le propane", "isCorrect": False}
                    ],
                    "correction": "L'aluminium s'oxyde instantanément à l'air. Il faut un gaz 100% inerte pour protéger le bain de fusion sans réagir avec lui."
                },
                {
                    "questionNumber": 18,
                    "question": "Les matériaux composites carbone sont choisis pour :",
                    "answerOptions": [
                        {"text": "Leur rapport légèreté et rigidité exceptionnel", "isCorrect": True},
                        {"text": "Leur capacité à se déformer plastiquement", "isCorrect": False},
                        {"text": "Leur facilité de réparation par soudure", "isCorrect": False},
                        {"text": "Leur faible coût de fabrication", "isCorrect": False}
                    ],
                    "correction": "Utilisés sur les véhicules sportifs ou haut de gamme pour gagner du poids sur la structure (cellule) ou la carrosserie."
                },
                {
                    "questionNumber": 19,
                    "question": "L'étamage est une technique de garnissage utilisant :",
                    "answerOptions": [
                        {"text": "Un alliage étain et plomb", "isCorrect": True},
                        {"text": "Une résine synthétique polyester", "isCorrect": False},
                        {"text": "Un ciment à prise rapide", "isCorrect": False},
                        {"text": "De l'aluminium fondu", "isCorrect": False}
                    ],
                    "correction": "Méthode traditionnelle pour combler les défauts ou assurer l'étanchéité d'une jonction soudée, offrant une durabilité supérieure au mastic."
                },
                {
                    "questionNumber": 20,
                    "question": "Une tôle insonorisée type sandwich contient :",
                    "answerOptions": [
                        {"text": "Une couche de polymère entre deux feuilles d'acier", "isCorrect": True},
                        {"text": "Une couche de laine de verre collée", "isCorrect": False},
                        {"text": "Du vide entre deux parois", "isCorrect": False},
                        {"text": "Une plaque de plomb vissée", "isCorrect": False}
                    ],
                    "correction": "Appelée tôle 'acoustique', la couche centrale amortit les vibrations pour réduire le bruit dans l'habitacle."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNIQUES DE RÉPARATION (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNIQUES DE RÉPARATION (Questions 21 à 40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Lors du planage, le rôle du tas est de :",
                    "answerOptions": [
                        {"text": "Servir de contre-appui au marteau", "isCorrect": True},
                        {"text": "Frapper directement la tôle par l'extérieur", "isCorrect": False},
                        {"text": "Chauffer la tôle par contact", "isCorrect": False},
                        {"text": "Mesurer la profondeur de la bosse", "isCorrect": False}
                    ],
                    "correction": "La tôle est prise en sandwich entre le marteau (qui frappe) et le tas (qui soutient) pour lisser la surface."
                },
                {
                    "questionNumber": 22,
                    "question": "La 'chaude de retrait' sert à :",
                    "answerOptions": [
                        {"text": "Rétracter une tôle allongée", "isCorrect": True},
                        {"text": "Assouplir une tôle avant formage", "isCorrect": False},
                        {"text": "Souder deux tôles bord à bord", "isCorrect": False},
                        {"text": "Décaper la peinture", "isCorrect": False}
                    ],
                    "correction": "En chauffant un point et en le refroidissant, on crée une contraction qui résorbe l'excédent de métal (les 'clocs')."
                },
                {
                    "questionNumber": 23,
                    "question": "La cuillère de carrossier s'utilise principalement pour :",
                    "answerOptions": [
                        {"text": "Faire levier dans les zones inaccessibles au tas", "isCorrect": True},
                        {"text": "Appliquer les mastics de finition", "isCorrect": False},
                        {"text": "Mélanger les teintes de peinture", "isCorrect": False},
                        {"text": "Gratter les joints de sertissage", "isCorrect": False}
                    ],
                    "correction": "Outil polyvalent qui peut servir de tas intérieur ou de levier pour repousser les bosses dans les doublures."
                },
                {
                    "questionNumber": 24,
                    "question": "Le tire-clou permet de redresser :",
                    "answerOptions": [
                        {"text": "Depuis l'extérieur sans dégarnir", "isCorrect": True},
                        {"text": "En démontant obligatoirement l'intérieur", "isCorrect": False},
                        {"text": "Uniquement les pièces en aluminium", "isCorrect": False},
                        {"text": "Sans toucher à la peinture", "isCorrect": False}
                    ],
                    "correction": "On soude une électrode temporaire sur la tôle nue et on tire. Cela évite de démonter toute la garniture intérieure de la porte ou de l'aile."
                },
                {
                    "questionNumber": 25,
                    "question": "Une batte à rétreindre possède une surface :",
                    "answerOptions": [
                        {"text": "Striée pour marquer le métal", "isCorrect": True},
                        {"text": "Parfaitement lisse et polie", "isCorrect": False},
                        {"text": "Bombée en caoutchouc", "isCorrect": False},
                        {"text": "En bois tendre", "isCorrect": False}
                    ],
                    "correction": "Les stries empêchent le métal de glisser vers l'extérieur lors de l'impact, le forçant à se refouler sur lui-même."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle préparation de surface est requise avant le masticage ?",
                    "answerOptions": [
                        {"text": "Ponçage au gros grain et dégraissage", "isCorrect": True},
                        {"text": "Ponçage à l'eau au grain très fin", "isCorrect": False},
                        {"text": "Application d'une couche de vernis brillant", "isCorrect": False},
                        {"text": "Simple nettoyage à l'eau savonneuse", "isCorrect": False}
                    ],
                    "correction": "Il faut créer des rayures (P80/P120) pour l'accroche mécanique et éliminer tout gras ou rouille."
                },
                {
                    "questionNumber": 27,
                    "question": "Le débosselage sans peinture (DSP) se pratique par :",
                    "answerOptions": [
                        {"text": "Poussées progressives de l'intérieur", "isCorrect": True},
                        {"text": "Traction brutale avec une ventouse", "isCorrect": False},
                        {"text": "Chauffage intense au chalumeau", "isCorrect": False},
                        {"text": "Application d'une couche de mastic", "isCorrect": False}
                    ],
                    "correction": "On 'masse' la tôle par l'arrière avec des tringles pour faire revenir la bosse sans casser le vernis d'origine."
                },
                {
                    "questionNumber": 28,
                    "question": "Le meulage excessif d'un cordon de soudure entraîne :",
                    "answerOptions": [
                        {"text": "Une amorce de rupture par amincissement", "isCorrect": True},
                        {"text": "Une meilleure solidité de l'assemblage", "isCorrect": False},
                        {"text": "Une protection contre la rouille", "isCorrect": False},
                        {"text": "Une modification de la structure moléculaire", "isCorrect": False}
                    ],
                    "correction": "Il ne faut pas creuser la tôle adjacente ('caniveau'). On doit juste araser le cordon au niveau de la tôle."
                },
                {
                    "questionNumber": 29,
                    "question": "À quelle consistance l'étain doit-il être travaillé ?",
                    "answerOptions": [
                        {"text": "Pâteuse comme du beurre", "isCorrect": True},
                        {"text": "Totalement liquide et fluide", "isCorrect": False},
                        {"text": "Solide et froide", "isCorrect": False},
                        {"text": "En poudre sèche", "isCorrect": False}
                    ],
                    "correction": "On maintient l'étain dans sa plage de température pâteuse pour pouvoir le modeler à la spatule en bois. S'il est liquide, il coule."
                },
                {
                    "questionNumber": 30,
                    "question": "Pour séparer un panneau de porte soudé par points, on utilise :",
                    "answerOptions": [
                        {"text": "Un foret à dépointer", "isCorrect": True},
                        {"text": "Un burin pneumatique tranchant", "isCorrect": False},
                        {"text": "Une scie sabre", "isCorrect": False},
                        {"text": "Un chalumeau découpeur", "isCorrect": False}
                    ],
                    "correction": "Le foret plat usine le point de soudure de la tôle supérieure sans percer la doublure qui doit être réutilisée."
                },
                {
                    "questionNumber": 31,
                    "question": "L'équerre hydraulique est un outil de :",
                    "answerOptions": [
                        {"text": "Traction et de poussée structurelle", "isCorrect": True},
                        {"text": "Mesure de la géométrie des trains", "isCorrect": False},
                        {"text": "Découpe des tôles", "isCorrect": False},
                        {"text": "Soudage par points", "isCorrect": False}
                    ],
                    "correction": "Vérin puissant utilisé pour redresser les éléments forts (longeron, passage de roue) lors d'un choc important."
                },
                {
                    "questionNumber": 32,
                    "question": "La technique du 'pas de pèlerin' en soudure permet de :",
                    "answerOptions": [
                        {"text": "Limiter la déformation thermique", "isCorrect": True},
                        {"text": "Souder plus vite", "isCorrect": False},
                        {"text": "Utiliser moins de fil", "isCorrect": False},
                        {"text": "Souder sans masque", "isCorrect": False}
                    ],
                    "correction": "En soudant par petits bouts espacés, on répartit la chaleur et on évite que la tôle ne gondole."
                },
                {
                    "questionNumber": 33,
                    "question": "La lime fraisée sert à :",
                    "answerOptions": [
                        {"text": "Révéler les défauts de planéité", "isCorrect": True},
                        {"text": "Couper les boulons rouillés", "isCorrect": False},
                        {"text": "Limer le mastic durci", "isCorrect": False},
                        {"text": "Affûter les forets", "isCorrect": False}
                    ],
                    "correction": "Passée à plat, elle marque les sommets (brillants) et ignore les creux (mats), montrant au carrossier où il doit taper."
                },
                {
                    "questionNumber": 34,
                    "question": "Le mastic chargé d'aluminium est utilisé pour :",
                    "answerOptions": [
                        {"text": "Sa résistance mécanique et thermique", "isCorrect": True},
                        {"text": "Sa facilité de ponçage extrême", "isCorrect": False},
                        {"text": "Sa couleur invisible sur l'acier", "isCorrect": False},
                        {"text": "Remplacer la peinture", "isCorrect": False}
                    ],
                    "correction": "Plus dense et dur, il convient aux grosses réparations ou aux zones chaudes (capot moteur), là où un mastic standard pourrait s'affaisser."
                },
                {
                    "questionNumber": 35,
                    "question": "La coupe en 'Z' ou en escalier sur un longeron sert à :",
                    "answerOptions": [
                        {"text": "Augmenter la surface de soudure", "isCorrect": True},
                        {"text": "Faciliter la découpe à la scie", "isCorrect": False},
                        {"text": "Utiliser moins de gaz", "isCorrect": False},
                        {"text": "Faire joli", "isCorrect": False}
                    ],
                    "correction": "Cela évite une ligne de faiblesse continue sur toute la section verticale du longeron et renforce la jonction."
                },
                {
                    "questionNumber": 36,
                    "question": "Le soyage des tôles permet un assemblage :",
                    "answerOptions": [
                        {"text": "À recouvrement avec une surface plane", "isCorrect": True},
                        {"text": "Bord à bord sans recouvrement", "isCorrect": False},
                        {"text": "Perpendiculaire en angle droit", "isCorrect": False},
                        {"text": "Provisoire par clips", "isCorrect": False}
                    ],
                    "correction": "On déforme le bord d'une tôle pour qu'elle passe sous l'autre, gardant le niveau extérieur aligné pour faciliter la finition."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel outil pneumatique utilise-t-on pour découper une aile arrière ?",
                    "answerOptions": [
                        {"text": "La scie sabre", "isCorrect": True},
                        {"text": "La visseuse à chocs", "isCorrect": False},
                        {"text": "La ponceuse orbitale", "isCorrect": False},
                        {"text": "Le pistolet à colle", "isCorrect": False}
                    ],
                    "correction": "La scie sabre permet de couper les montants et les doublures avec précision sans trop chauffer la zone."
                },
                {
                    "questionNumber": 38,
                    "question": "La température de recuit de l'aluminium se vérifie avec :",
                    "answerOptions": [
                        {"text": "Un feutre thermosensible ou du savon", "isCorrect": True},
                        {"text": "La couleur rouge du métal", "isCorrect": False},
                        {"text": "La fumée qui se dégage", "isCorrect": False},
                        {"text": "Un thermomètre médical", "isCorrect": False}
                    ],
                    "correction": "L'alu ne change pas de couleur avant de fondre. Il faut un indicateur externe qui change d'aspect vers 300°C."
                },
                {
                    "questionNumber": 39,
                    "question": "Le jointoiement des tôles après réparation se fait avec :",
                    "answerOptions": [
                        {"text": "Un mastic polyuréthane ou hybride", "isCorrect": True},
                        {"text": "Du mastic polyester de finition", "isCorrect": False},
                        {"text": "De la colle à pare-brise", "isCorrect": False},
                        {"text": "Du ruban adhésif", "isCorrect": False}
                    ],
                    "correction": "Ce cordon souple refait l'étanchéité d'origine entre les tôles assemblées ou serties."
                },
                {
                    "questionNumber": 40,
                    "question": "En redressage, pourquoi commence-t-on par la périphérie du choc ?",
                    "answerOptions": [
                        {"text": "Pour libérer les contraintes progressivement", "isCorrect": True},
                        {"text": "Parce que c'est la zone la plus abîmée", "isCorrect": False},
                        {"text": "Pour ne pas abîmer le marteau", "isCorrect": False},
                        {"text": "Parce que c'est plus facile d'accès", "isCorrect": False}
                    ],
                    "correction": "On déroule le choc à l'envers. Le centre du choc est le point dur qui maintient les tensions ; le débloquer en dernier permet au métal de reprendre sa place."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : ANALYSE DES DOMMAGES ET MÉTROLOGIE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ANALYSE DES DOMMAGES ET MÉTROLOGIE (Questions 41 à 60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "La 'mise en assiette' sur un marbre consiste à :",
                    "answerOptions": [
                        {"text": "Fixer le véhicule de niveau par les bas de caisse", "isCorrect": True},
                        {"text": "Déposer la mécanique avant et arrière", "isCorrect": False},
                        {"text": "Placer des cibles laser sur le toit", "isCorrect": False},
                        {"text": "Vérifier la pression des quatre roues", "isCorrect": False}
                    ],
                    "correction": "C'est la base de la mesure. Le véhicule est bridé sur ses points d'ancrage rigides pour servir de référence fixe."
                },
                {
                    "questionNumber": 42,
                    "question": "Un pli sur le pavillon (toit) après un choc avant indique :",
                    "answerOptions": [
                        {"text": "Une déformation structurelle de la caisse", "isCorrect": True},
                        {"text": "Un simple défaut d'alignement du capot", "isCorrect": False},
                        {"text": "Un impact direct sur le toit", "isCorrect": False},
                        {"text": "Une mauvaise qualité de l'acier", "isCorrect": False}
                    ],
                    "correction": "L'énergie du choc a traversé les longerons, les montants de baie et a fait plier le toit. Le véhicule est probablement 'vrillé' ou 'banané'."
                },
                {
                    "questionNumber": 43,
                    "question": "La pige de carrossier sert à effectuer des mesures :",
                    "answerOptions": [
                        {"text": "Comparatives par symétrie gauche/droite", "isCorrect": True},
                        {"text": "De température du moteur", "isCorrect": False},
                        {"text": "De hauteur de caisse par rapport au sol", "isCorrect": False},
                        {"text": "D'épaisseur de peinture", "isCorrect": False}
                    ],
                    "correction": "On règle la pige sur une diagonale saine et on la reporte sur le côté accidenté. Si ça ne correspond pas, la caisse a bougé."
                },
                {
                    "questionNumber": 44,
                    "question": "Le système de mesure 'Touch' fonctionne grâce à :",
                    "answerOptions": [
                        {"text": "Un bras articulé numérisé", "isCorrect": True},
                        {"text": "Des règles graduées en bois", "isCorrect": False},
                        {"text": "Un niveau à bulle géant", "isCorrect": False},
                        {"text": "Des caméras thermiques", "isCorrect": False}
                    ],
                    "correction": "Le bras palpeur touche les points de contrôle sous la voiture et transmet les coordonnées X, Y, Z à l'ordinateur."
                },
                {
                    "questionNumber": 45,
                    "question": "En carrosserie, l'axe Z correspond à :",
                    "answerOptions": [
                        {"text": "La hauteur verticale", "isCorrect": True},
                        {"text": "La longueur du véhicule", "isCorrect": False},
                        {"text": "La largeur du véhicule", "isCorrect": False},
                        {"text": "L'angle de braquage", "isCorrect": False}
                    ],
                    "correction": "X = Longueur, Y = Largeur, Z = Hauteur. C'est la convention internationale de mesure 3D."
                },
                {
                    "questionNumber": 46,
                    "question": "Un longeron vrillé a subi une déformation en :",
                    "answerOptions": [
                        {"text": "Torsion", "isCorrect": True},
                        {"text": "Compression simple", "isCorrect": False},
                        {"text": "Extension", "isCorrect": False},
                        {"text": "Flexion latérale pure", "isCorrect": False}
                    ],
                    "correction": "La pièce a tourné sur elle-même. C'est très difficile à redresser car il faut appliquer un couple de force inverse."
                },
                {
                    "questionNumber": 47,
                    "question": "L'accord de réparation est donné par :",
                    "answerOptions": [
                        {"text": "L'expert automobile mandaté", "isCorrect": True},
                        {"text": "Le mécanicien du garage", "isCorrect": False},
                        {"text": "Le client uniquement", "isCorrect": False},
                        {"text": "Le vendeur de pièces", "isCorrect": False}
                    ],
                    "correction": "L'expert valide que la méthode technique est sûre et que le coût est justifié par rapport à la valeur du véhicule."
                },
                {
                    "questionNumber": 48,
                    "question": "Une déformation en 'banane' affecte :",
                    "answerOptions": [
                        {"text": "L'alignement latéral de la structure", "isCorrect": True},
                        {"text": "La hauteur du toit uniquement", "isCorrect": False},
                        {"text": "La longueur des portes avant", "isCorrect": False},
                        {"text": "La largeur des voies", "isCorrect": False}
                    ],
                    "correction": "Le véhicule est courbé sur le côté. L'empattement est plus court d'un côté que de l'autre."
                },
                {
                    "questionNumber": 49,
                    "question": "La géométrie des trains roulants dépend directement de :",
                    "answerOptions": [
                        {"text": "La position des points d'ancrage du soubassement", "isCorrect": True},
                        {"text": "La marque des amortisseurs", "isCorrect": False},
                        {"text": "La pression des pneus", "isCorrect": False},
                        {"text": "La taille du volant", "isCorrect": False}
                    ],
                    "correction": "Si le berceau ou les longerons sont déplacés par un choc, il est impossible de régler le parallélisme correctement."
                },
                {
                    "questionNumber": 50,
                    "question": "Le contrôle des jeux et affleurements permet de valider :",
                    "answerOptions": [
                        {"text": "La qualité de l'ajustage des éléments mobiles", "isCorrect": True},
                        {"text": "La puissance du moteur", "isCorrect": False},
                        {"text": "La teinte de la peinture", "isCorrect": False},
                        {"text": "L'étanchéité des vitres", "isCorrect": False}
                    ],
                    "correction": "Des espaces réguliers entre les pièces (ex: porte/aile) sont la preuve visuelle que la structure est bien remise en ligne."
                },
                {
                    "questionNumber": 51,
                    "question": "Sur un véhicule électrique accidenté, la priorité est de :",
                    "answerOptions": [
                        {"text": "Vérifier l'intégrité du bac batterie", "isCorrect": True},
                        {"text": "Recharger la batterie à fond", "isCorrect": False},
                        {"text": "Démonter le moteur électrique", "isCorrect": False},
                        {"text": "Changer les fusibles 12V", "isCorrect": False}
                    ],
                    "correction": "Une batterie déformée peut prendre feu des jours après l'accident (emballement thermique). Inspection visuelle impérative."
                },
                {
                    "questionNumber": 52,
                    "question": "Pour contrôler la chasse, on mesure :",
                    "answerOptions": [
                        {"text": "La différence d'empattement gauche/droite", "isCorrect": True},
                        {"text": "La distance entre les deux roues avant", "isCorrect": False},
                        {"text": "La hauteur sous coque", "isCorrect": False},
                        {"text": "Le diamètre des disques de frein", "isCorrect": False}
                    ],
                    "correction": "Si une roue a reculé suite à un choc trottoir, l'empattement de ce côté sera plus petit."
                },
                {
                    "questionNumber": 53,
                    "question": "Les têtes d'amortisseurs rapprochées indiquent :",
                    "answerOptions": [
                        {"text": "Un affaissement des montants ou de la traverse", "isCorrect": True},
                        {"text": "Un pneu dégonflé", "isCorrect": False},
                        {"text": "Un capot trop long", "isCorrect": False},
                        {"text": "Un moteur trop lourd", "isCorrect": False}
                    ],
                    "correction": "Fréquent lors des chocs latéraux ou frontaux importants. La 'voie supérieure' est hors cote."
                },
                {
                    "questionNumber": 54,
                    "question": "Une fissure de peinture sur un élément structurel révèle :",
                    "answerOptions": [
                        {"text": "Un pli de métal sous-jacent", "isCorrect": True},
                        {"text": "Une mauvaise préparation peinture", "isCorrect": False},
                        {"text": "Un gravillon", "isCorrect": False},
                        {"text": "Une rayure superficielle", "isCorrect": False}
                    ],
                    "correction": "Le métal a travaillé élastiquement ou plastiquement, mais la peinture rigide a cassé. C'est un indice crucial pour l'expert."
                },
                {
                    "questionNumber": 55,
                    "question": "Le point zéro des mesures constructeur est :",
                    "answerOptions": [
                        {"text": "Une référence virtuelle ou physique d'origine", "isCorrect": True},
                        {"text": "Le pare-chocs avant", "isCorrect": False},
                        {"text": "Le centre du volant", "isCorrect": False},
                        {"text": "La boule d'attelage", "isCorrect": False}
                    ],
                    "correction": "Toutes les cotes (X, Y, Z) partent de ce point. Il est souvent au centre de l'essieu avant ou arrière."
                },
                {
                    "questionNumber": 56,
                    "question": "La procédure VGE (Véhicule Gravement Endommagé) bloque :",
                    "answerOptions": [
                        {"text": "La carte grise en préfecture", "isCorrect": True},
                        {"text": "Les portières de la voiture", "isCorrect": False},
                        {"text": "Le démarrage du moteur", "isCorrect": False},
                        {"text": "L'assurance du conducteur", "isCorrect": False}
                    ],
                    "correction": "Le véhicule ne peut plus rouler sur route ouverte tant qu'il n'est pas réparé et contrôlé par l'expert (rapport de conformité)."
                },
                {
                    "questionNumber": 57,
                    "question": "Un châssis en 'losange' présente :",
                    "answerOptions": [
                        {"text": "Un décalage longitudinal des longerons l'un par rapport à l'autre", "isCorrect": True},
                        {"text": "Une variation de largeur de voie", "isCorrect": False},
                        {"text": "Une pliure vers le haut", "isCorrect": False},
                        {"text": "Une pliure vers le bas", "isCorrect": False}
                    ],
                    "correction": "Le cadre est faussé mais reste à plat. Les diagonales ne sont plus égales."
                },
                {
                    "questionNumber": 58,
                    "question": "Le compas de carrossier est utilisé pour :",
                    "answerOptions": [
                        {"text": "Tracer ou comparer des grandes diagonales", "isCorrect": True},
                        {"text": "Dessiner des cercles sur la tôle", "isCorrect": False},
                        {"text": "Mesurer l'épaisseur de tôle", "isCorrect": False},
                        {"text": "Gratter la rouille", "isCorrect": False}
                    ],
                    "correction": "Outil de diagnostic rapide ('la grande barre') pour voir si une baie de pare-brise ou un compartiment moteur est carré."
                },
                {
                    "questionNumber": 59,
                    "question": "Une jante alu fissurée doit être :",
                    "answerOptions": [
                        {"text": "Remplacée obligatoirement", "isCorrect": True},
                        {"text": "Soudée par un professionnel", "isCorrect": False},
                        {"text": "Redressée à chaud", "isCorrect": False},
                        {"text": "Collée à l'époxy", "isCorrect": False}
                    ],
                    "correction": "Les réparations structurelles sur jantes alu sont interdites car la structure moléculaire est fragilisée, avec risque d'éclatement."
                },
                {
                    "questionNumber": 60,
                    "question": "Un mauvais alignement du hayon peut provenir :",
                    "answerOptions": [
                        {"text": "D'une caisse vrillée", "isCorrect": True},
                        {"text": "D'un pare-chocs mal mis", "isCorrect": False},
                        {"text": "D'une vitre trop lourde", "isCorrect": False},
                        {"text": "De vérins trop puissants", "isCorrect": False}
                    ],
                    "correction": "Si le hayon touche d'un côté et baille de l'autre, l'encadrement arrière est déformé."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : PRÉPARATION ET PEINTURE (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : PRÉPARATION ET PEINTURE (Questions 61 à 80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Le primaire phosphatant (Wash Primer) assure :",
                    "answerOptions": [
                        {"text": "L'adhérence chimique sur tôle nue", "isCorrect": True},
                        {"text": "Le garnissage des rayures profondes", "isCorrect": False},
                        {"text": "La brillance finale", "isCorrect": False},
                        {"text": "L'étanchéité des jonctions", "isCorrect": False}
                    ],
                    "correction": "Il contient de l'acide qui mord le métal (acier, zinc, alu) pour garantir que les couches suivantes ne pèleront pas."
                },
                {
                    "questionNumber": 62,
                    "question": "Le voile de placement sert à :",
                    "answerOptions": [
                        {"text": "Orienter les particules métallisées uniformément", "isCorrect": True},
                        {"text": "Mettre plus d'épaisseur de peinture", "isCorrect": False},
                        {"text": "Faire sécher la base plus vite", "isCorrect": False},
                        {"text": "Corriger une coulure", "isCorrect": False}
                    ],
                    "correction": "Appliqué un peu plus loin et moins mouillé, il évite les effets de 'nuages' ou 'marbrures' sur les gris métallisés."
                },
                {
                    "questionNumber": 63,
                    "question": "Les 'yeux de poisson' (silicones) sont causés par :",
                    "answerOptions": [
                        {"text": "Une contamination grasse du support", "isCorrect": True},
                        {"text": "Une température trop basse", "isCorrect": False},
                        {"text": "Une peinture périmée", "isCorrect": False},
                        {"text": "Un excès de durcisseur", "isCorrect": False}
                    ],
                    "correction": "Le gras repousse la peinture. Il faut dégraisser méticuleusement avant de peindre."
                },
                {
                    "questionNumber": 64,
                    "question": "Un papier abrasif P80 est plus :",
                    "answerOptions": [
                        {"text": "Gros qu'un P400", "isCorrect": True},
                        {"text": "Fin qu'un P400", "isCorrect": False},
                        {"text": "Souple qu'un P400", "isCorrect": False},
                        {"text": "Cher qu'un P400", "isCorrect": False}
                    ],
                    "correction": "Petit chiffre = Gros grains (décaper). Grand chiffre = Petits grains (finition)."
                },
                {
                    "questionNumber": 65,
                    "question": "La technologie HVLP vise à :",
                    "answerOptions": [
                        {"text": "Augmenter le taux de transfert de produit", "isCorrect": True},
                        {"text": "Augmenter la pression de sortie", "isCorrect": False},
                        {"text": "Pulvériser plus loin", "isCorrect": False},
                        {"text": "Sécher instantanément", "isCorrect": False}
                    ],
                    "correction": "'High Volume Low Pressure'. Moins de pression = moins de rebond et de brouillard = plus de peinture sur la voiture."
                },
                {
                    "questionNumber": 66,
                    "question": "L'apprêt garnissant a pour fonction de :",
                    "answerOptions": [
                        {"text": "Isoler les fonds et remplir les micro-défauts", "isCorrect": True},
                        {"text": "Remplacer le mastic", "isCorrect": False},
                        {"text": "Faire briller la tôle", "isCorrect": False},
                        {"text": "Protéger des UV", "isCorrect": False}
                    ],
                    "correction": "Il crée une couche tampon uniforme et ponçable entre le travail de tôlerie/mastic et la peinture de finition."
                },
                {
                    "questionNumber": 67,
                    "question": "La méthode 'mouillé sur mouillé' permet de :",
                    "answerOptions": [
                        {"text": "Peindre sans poncer l'apprêt", "isCorrect": True},
                        {"text": "Peindre sous l'eau", "isCorrect": False},
                        {"text": "Poncer à l'eau uniquement", "isCorrect": False},
                        {"text": "Mettre deux couches de vernis", "isCorrect": False}
                    ],
                    "correction": "On applique la laque alors que l'apprêt est encore 'amoureux' (pas sec à cœur), ce qui crée une liaison chimique directe. Gain de temps énorme sur pièces neuves."
                },
                {
                    "questionNumber": 68,
                    "question": "Les spectres (embusquages) apparaissent quand :",
                    "answerOptions": [
                        {"text": "Les fonds ne sont pas assez secs ou isolés", "isCorrect": True},
                        {"text": "On a mis trop de vernis", "isCorrect": False},
                        {"text": "La couleur est trop claire", "isCorrect": False},
                        {"text": "On a poncé trop fin", "isCorrect": False}
                    ],
                    "correction": "Le solvant de la finition pénètre les couches inférieures et fait gonfler les zones de mastic/ponçage, rendant la réparation visible."
                },
                {
                    "questionNumber": 69,
                    "question": "Les bases mates à l'eau nécessitent :",
                    "answerOptions": [
                        {"text": "Une ventilation forcée (venturis) pour sécher", "isCorrect": True},
                        {"text": "Une cuisson à 80°C avant vernis", "isCorrect": False},
                        {"text": "D'être mélangées à du durcisseur", "isCorrect": False},
                        {"text": "Une application au pinceau", "isCorrect": False}
                    ],
                    "correction": "L'eau s'évapore lentement. Il faut un flux d'air pour chasser l'humidité de la couche avant de pouvoir vernir."
                },
                {
                    "questionNumber": 70,
                    "question": "Le godet d'un pistolet gravité est placé :",
                    "answerOptions": [
                        {"text": "Au-dessus de la buse", "isCorrect": True},
                        {"text": "En dessous de la poignée", "isCorrect": False},
                        {"text": "Sur le côté", "isCorrect": False},
                        {"text": "Au sol relié par un tuyau", "isCorrect": False}
                    ],
                    "correction": "La peinture tombe par gravité dans le pistolet, ce qui permet d'utiliser tout le produit, contrairement aux pistolets à succion."
                },
                {
                    "questionNumber": 71,
                    "question": "Un vernis 'poudré' est le résultat de :",
                    "answerOptions": [
                        {"text": "Une évaporation du diluant avant contact avec la tôle", "isCorrect": True},
                        {"text": "Une surcharge de produit", "isCorrect": False},
                        {"text": "Une cabine trop humide", "isCorrect": False},
                        {"text": "Un pistolet trop près", "isCorrect": False}
                    ],
                    "correction": "Si on peint de trop loin ou s'il fait trop chaud avec un diluant rapide, les gouttelettes arrivent sèches et forment des grains au lieu d'un film lisse."
                },
                {
                    "questionNumber": 72,
                    "question": "Le dégraissage antisilicone s'effectue avec :",
                    "answerOptions": [
                        {"text": "Deux chiffons (un mouillé, un sec)", "isCorrect": True},
                        {"text": "Un seul chiffon imbibé", "isCorrect": False},
                        {"text": "De l'air comprimé", "isCorrect": False},
                        {"text": "Une éponge à l'eau", "isCorrect": False}
                    ],
                    "correction": "Le premier chiffon dissout le gras, le second (sec) le ramasse avant que le produit ne s'évapore. Sinon, on ne fait qu'étaler le gras."
                },
                {
                    "questionNumber": 73,
                    "question": "La poudre guide de ponçage sert à :",
                    "answerOptions": [
                        {"text": "Révéler les irrégularités de surface", "isCorrect": True},
                        {"text": "Lubrifier le papier", "isCorrect": False},
                        {"text": "Colorer l'apprêt", "isCorrect": False},
                        {"text": "Boucher les pores", "isCorrect": False}
                    ],
                    "correction": "La poudre noire reste dans les creux non poncés, montrant visuellement ce qu'il reste à rectifier."
                },
                {
                    "questionNumber": 74,
                    "question": "La coupe Viscosimétrique sert à mesurer :",
                    "answerOptions": [
                        {"text": "La fluidité de la peinture", "isCorrect": True},
                        {"text": "La température de la cabine", "isCorrect": False},
                        {"text": "Le poids du pistolet", "isCorrect": False},
                        {"text": "L'épaisseur du film", "isCorrect": False}
                    ],
                    "correction": "Le temps d'écoulement (ex: 20 secondes) garantit que le mélange est correct pour être pulvérisé."
                },
                {
                    "questionNumber": 75,
                    "question": "L'additif assouplissant est requis pour peindre :",
                    "answerOptions": [
                        {"text": "Les pièces plastiques souples", "isCorrect": True},
                        {"text": "Le capot moteur chaud", "isCorrect": False},
                        {"text": "Les jantes alu", "isCorrect": False},
                        {"text": "Le toit", "isCorrect": False}
                    ],
                    "correction": "Il rend le vernis flexible pour qu'il ne craquelle pas si le pare-chocs se déforme légèrement (appui, gravillons)."
                },
                {
                    "questionNumber": 76,
                    "question": "Le diluant raccord permet de :",
                    "answerOptions": [
                        {"text": "Fondre les brouillards de vernis en zone de transition", "isCorrect": True},
                        {"text": "Nettoyer le pistolet", "isCorrect": False},
                        {"text": "Diluer la base mate", "isCorrect": False},
                        {"text": "Enlever les silicones", "isCorrect": False}
                    ],
                    "correction": "Il dissout le brouillard sec en périphérie de la réparation pour qu'il fusionne avec l'ancien vernis, rendant la retouche invisible au lustrage."
                },
                {
                    "questionNumber": 77,
                    "question": "Un produit 2K durcit par :",
                    "answerOptions": [
                        {"text": "Réaction chimique avec un isocyanate", "isCorrect": True},
                        {"text": "Séchage à l'air simple", "isCorrect": False},
                        {"text": "Exposition aux UV", "isCorrect": False},
                        {"text": "Congélation", "isCorrect": False}
                    ],
                    "correction": "La polymérisation crée un film très dur et résistant aux solvants (vernis, brillants directs)."
                },
                {
                    "questionNumber": 78,
                    "question": "Le ruban mousse dans les entrées de porte évite :",
                    "answerOptions": [
                        {"text": "La formation d'une arête de vernis franche", "isCorrect": True},
                        {"text": "De peindre les joints", "isCorrect": False},
                        {"text": "De fermer la porte", "isCorrect": False},
                        {"text": "Les coulures", "isCorrect": False}
                    ],
                    "correction": "Il soulève légèrement le bord pour créer un dégradé de peinture 'flou' facile à lustrer, au lieu d'une marche d'escalier dure."
                },
                {
                    "questionNumber": 79,
                    "question": "La température standard d'étuvage est de :",
                    "answerOptions": [
                        {"text": "60°C", "isCorrect": True},
                        {"text": "100°C", "isCorrect": False},
                        {"text": "200°C", "isCorrect": False},
                        {"text": "20°C", "isCorrect": False}
                    ],
                    "correction": "Suffisant pour durcir le vernis en 30 min sans faire fondre les plastiques ou l'électronique de la voiture."
                },
                {
                    "questionNumber": 80,
                    "question": "Pour rectifier une coulure sèche, on utilise :",
                    "answerOptions": [
                        {"text": "Une cale à araser ou un rabot", "isCorrect": True},
                        {"text": "Du diluant de nettoyage", "isCorrect": False},
                        {"text": "Un décapeur thermique", "isCorrect": False},
                        {"text": "Une polisseuse directement", "isCorrect": False}
                    ],
                    "correction": "Il faut couper la surépaisseur 'tête de la coulure' avant de poncer et lustrer, sinon on perce le vernis autour."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : HYGIÈNE, SÉCURITÉ ET ENVIRONNEMENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : HYGIÈNE, SÉCURITÉ ET ENVIRONNEMENT (Questions 81 à 100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "La protection respiratoire contre les isocyanates exige :",
                    "answerOptions": [
                        {"text": "Un masque à cartouches A2P3 ou à adduction d'air", "isCorrect": True},
                        {"text": "Un masque à poussières P2", "isCorrect": False},
                        {"text": "Une ventilation naturelle", "isCorrect": False},
                        {"text": "Un mouchoir", "isCorrect": False}
                    ],
                    "correction": "Les gaz toxiques des durcisseurs traversent les masques papier. Il faut du charbon actif ou de l'air propre externe."
                },
                {
                    "questionNumber": 82,
                    "question": "Le balisage d'un véhicule électrique en réparation est :",
                    "answerOptions": [
                        {"text": "Obligatoire pour prévenir du risque électrique", "isCorrect": True},
                        {"text": "Facultatif si on fait attention", "isCorrect": False},
                        {"text": "Réservé aux concessionnaires", "isCorrect": False},
                        {"text": "Inutile si la batterie est débranchée", "isCorrect": False}
                    ],
                    "correction": "La zone de danger doit être identifiée pour que personne ne touche les câbles oranges par inadvertance."
                },
                {
                    "questionNumber": 83,
                    "question": "Sur un feu de batterie Lithium, l'extincteur CO2 est :",
                    "answerOptions": [
                        {"text": "Peu efficace car il ne refroidit pas assez", "isCorrect": True},
                        {"text": "Le meilleur choix", "isCorrect": False},
                        {"text": "Dangereux car explosif", "isCorrect": False},
                        {"text": "Suffisant", "isCorrect": False}
                    ],
                    "correction": "L'emballement thermique est une réaction chimique interne. Seule une inondation massive d'eau peut refroidir la batterie."
                },
                {
                    "questionNumber": 84,
                    "question": "Les solvants chlorés sont bannis car :",
                    "answerOptions": [
                        {"text": "Nocifs pour la couche d'ozone et la santé", "isCorrect": True},
                        {"text": "Ils rouillent le métal", "isCorrect": False},
                        {"text": "Ils évaporent trop vite", "isCorrect": False},
                        {"text": "Ils sont colorés", "isCorrect": False}
                    ],
                    "correction": "Remplacés par des produits moins agressifs pour l'environnement."
                },
                {
                    "questionNumber": 85,
                    "question": "Le positionnement des bras du pont élévateur doit se faire :",
                    "answerOptions": [
                        {"text": "Sur les points de levage renforcés du soubassement", "isCorrect": True},
                        {"text": "Sous les bas de caisse en plastique", "isCorrect": False},
                        {"text": "Sous le plancher plat", "isCorrect": False},
                        {"text": "Sous le réservoir", "isCorrect": False}
                    ],
                    "correction": "Risque de chute du véhicule ou d'écrasement du plancher si on lève ailleurs."
                },
                {
                    "questionNumber": 86,
                    "question": "Les poussières d'aluminium présentent un risque :",
                    "answerOptions": [
                        {"text": "D'explosion en présence d'étincelles", "isCorrect": True},
                        {"text": "De radiation", "isCorrect": False},
                        {"text": "De moisissure", "isCorrect": False},
                        {"text": "De glissade", "isCorrect": False}
                    ],
                    "correction": "La poudre d'alu est un combustible. Il ne faut jamais meuler de l'acier (étincelles) près d'un poste de ponçage alu."
                },
                {
                    "questionNumber": 87,
                    "question": "Consigner un VE signifie :",
                    "answerOptions": [
                        {"text": "Condamner physiquement la remise sous tension", "isCorrect": True},
                        {"text": "Noter son kilométrage", "isCorrect": False},
                        {"text": "Le garer dehors", "isCorrect": False},
                        {"text": "Enlever les fusibles des phares", "isCorrect": False}
                    ],
                    "correction": "On pose un cadenas sur la prise de service pour garantir la sécurité du technicien."
                },
                {
                    "questionNumber": 88,
                    "question": "Les gants en nitrile protègent mieux que le latex contre :",
                    "answerOptions": [
                        {"text": "Les hydrocarbures et solvants de peinture", "isCorrect": True},
                        {"text": "La chaleur", "isCorrect": False},
                        {"text": "Les coupures", "isCorrect": False},
                        {"text": "Le froid", "isCorrect": False}
                    ],
                    "correction": "Le latex se désagrège au contact des diluants."
                },
                {
                    "questionNumber": 89,
                    "question": "Le rinçage d'un œil contaminé doit durer :",
                    "answerOptions": [
                        {"text": "Au moins 15 minutes", "isCorrect": True},
                        {"text": "30 secondes", "isCorrect": False},
                        {"text": "1 minute", "isCorrect": False},
                        {"text": "2 heures", "isCorrect": False}
                    ],
                    "correction": "C'est le temps nécessaire pour diluer le produit chimique incrusté."
                },
                {
                    "questionNumber": 90,
                    "question": "Le Document Unique (DUER) est :",
                    "answerOptions": [
                        {"text": "L'inventaire obligatoire des risques de l'atelier", "isCorrect": True},
                        {"text": "Le carnet d'entretien de la voiture", "isCorrect": False},
                        {"text": "Le livre de comptes", "isCorrect": False},
                        {"text": "Le planning des congés", "isCorrect": False}
                    ],
                    "correction": "Base de la prévention en entreprise."
                },
                {
                    "questionNumber": 91,
                    "question": "La fièvre des métaux est causée par :",
                    "answerOptions": [
                        {"text": "L'inhalation de fumées de zinc (galva)", "isCorrect": True},
                        {"text": "Le bruit", "isCorrect": False},
                        {"text": "Le froid", "isCorrect": False},
                        {"text": "La fatigue", "isCorrect": False}
                    ],
                    "correction": "Symptômes pseudo-grippaux après soudure sur tôle zinguée sans aspiration."
                },
                {
                    "questionNumber": 92,
                    "question": "Un chiffon souillé est un déchet :",
                    "answerOptions": [
                        {"text": "Dangereux (DID)", "isCorrect": True},
                        {"text": "Banal (DIB)", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False},
                        {"text": "Recyclable", "isCorrect": False}
                    ],
                    "correction": "Il est imprégné de produits chimiques inflammables et polluants."
                },
                {
                    "questionNumber": 93,
                    "question": "Le seuil de danger pour l'audition est de :",
                    "answerOptions": [
                        {"text": "85 décibels", "isCorrect": True},
                        {"text": "120 décibels", "isCorrect": False},
                        {"text": "50 décibels", "isCorrect": False},
                        {"text": "200 décibels", "isCorrect": False}
                    ],
                    "correction": "Une journée à 85dB détruit l'oreille aussi sûrement qu'un bruit unique très fort."
                },
                {
                    "questionNumber": 94,
                    "question": "Le risque hydrogène concerne :",
                    "answerOptions": [
                        {"text": "La charge des batteries au plomb", "isCorrect": True},
                        {"text": "Le gonflage des pneus", "isCorrect": False},
                        {"text": "La peinture", "isCorrect": False},
                        {"text": "Le lavage", "isCorrect": False}
                    ],
                    "correction": "Gaz explosif dégagé lors de la recharge. Ventiler le local."
                },
                {
                    "questionNumber": 95,
                    "question": "Pour éviter les TMS, il faut :",
                    "answerOptions": [
                        {"text": "Adapter la hauteur de travail (pont)", "isCorrect": True},
                        {"text": "Travailler à genoux", "isCorrect": False},
                        {"text": "Porter lourd", "isCorrect": False},
                        {"text": "Courir", "isCorrect": False}
                    ],
                    "correction": "Le dos est le premier outil du carrossier, il faut le préserver."
                },
                {
                    "questionNumber": 96,
                    "question": "La surpression en cabine sert à :",
                    "answerOptions": [
                        {"text": "Chasser les poussières vers l'extérieur", "isCorrect": True},
                        {"text": "Comprimer la peinture", "isCorrect": False},
                        {"text": "Empêcher la porte de s'ouvrir", "isCorrect": False},
                        {"text": "Faire du vent", "isCorrect": False}
                    ],
                    "correction": "Empêche les saletés de l'atelier d'entrer."
                },
                {
                    "questionNumber": 97,
                    "question": "Les condensateurs Start & Stop présentent un risque :",
                    "answerOptions": [
                        {"text": "De choc électrique résiduel", "isCorrect": True},
                        {"text": "D'incendie", "isCorrect": False},
                        {"text": "De fuite d'eau", "isCorrect": False},
                        {"text": "De bruit", "isCorrect": False}
                    ],
                    "correction": "Ils stockent de l'énergie même moteur coupé."
                },
                {
                    "questionNumber": 98,
                    "question": "Lentilles de contact + Solvants =",
                    "answerOptions": [
                        {"text": "Danger de piégeage du produit contre l'œil", "isCorrect": True},
                        {"text": "Meilleure vision", "isCorrect": False},
                        {"text": "Protection efficace", "isCorrect": False},
                        {"text": "Rien", "isCorrect": False}
                    ],
                    "correction": "Aggrave les brûlures chimiques."
                },
                {
                    "questionNumber": 99,
                    "question": "Le nettoyage pistolet à l'air libre est :",
                    "answerOptions": [
                        {"text": "Interdit (émissions COV)", "isCorrect": True},
                        {"text": "Recommandé", "isCorrect": False},
                        {"text": "Obligatoire", "isCorrect": False},
                        {"text": "Pratique", "isCorrect": False}
                    ],
                    "correction": "Utiliser des machines fermées à recyclage de solvant."
                },
                {
                    "questionNumber": 100,
                    "question": "La couleur Orange en VE indique :",
                    "answerOptions": [
                        {"text": "La Haute Tension (Danger)", "isCorrect": True},
                        {"text": "La masse", "isCorrect": False},
                        {"text": "Le 12 Volts", "isCorrect": False},
                        {"text": "Les données", "isCorrect": False}
                    ],
                    "correction": "Code couleur universel de sécurité."
                },
            ]
        }
    }
}