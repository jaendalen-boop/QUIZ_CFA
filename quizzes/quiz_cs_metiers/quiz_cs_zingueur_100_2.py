quiz_data = {
    "title": "Quiz CS Zingueur (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : PRÉVENTION, SÉCURITÉ EN HAUTEUR ET PRÉPARATION DE CHANTIER (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : PRÉVENTION, SÉCURITÉ EN HAUTEUR ET PRÉPARATION DE CHANTIER",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel dispositif de protection individuelle est obligatoirement associé à un point d'ancrage normé lors d'une intervention sur une toiture sans garde-corps ?",
                    "answerOptions": [
                        {"text": "Harnais antichute", "isCorrect": True},
                        {"text": "Ligne de vie horizontale provisoire fixée sur des points structurels de charpente en bois", "isCorrect": False},
                        {"text": "Filet de protection en mailles synthétiques déployé sous l'ensemble de la zone de travail", "isCorrect": False},
                        {"text": "Échafaudage de pied en acier galvanisé monté avec des lisses et des sous-lisses de sécurité", "isCorrect": False}
                    ],
                    "correction": "Le harnais antichute est l'Équipement de Protection Individuelle (EPI) de base pour le travail en hauteur lorsqu'il est techniquement impossible de mettre en place une protection collective. Il doit impérativement être relié par une longe à un point d'ancrage conforme à la norme EN 795."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle maladie professionnelle grave est spécifiquement liée à l'inhalation ou l'ingestion de poussières de plomb lors des travaux de zinguerie ?",
                    "answerOptions": [
                        {"text": "Le saturnisme", "isCorrect": True},
                        {"text": "La silicose", "isCorrect": False},
                        {"text": "L'asbestose", "isCorrect": False},
                        {"text": "Le mésothéliome", "isCorrect": False}
                    ],
                    "correction": "Le saturnisme est une intoxication aiguë ou chronique par le plomb, très présent sur les toitures anciennes. Il provoque des troubles neurologiques, sanguins et rénaux. Une hygiène stricte au chantier (lavage des mains, interdiction de manger sur la zone de travail) est obligatoire pour éviter l'ingestion de particules."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel équipement constitue une protection collective prioritaire sur un chantier de couverture ?",
                    "answerOptions": [
                        {"text": "Un garde-corps périphérique", "isCorrect": True},
                        {"text": "Un casque de chantier ventilé", "isCorrect": False},
                        {"text": "Une longe double avec absorbeur", "isCorrect": False},
                        {"text": "Des chaussures de sécurité montantes", "isCorrect": False}
                    ],
                    "correction": "Le Code du travail impose de toujours privilégier la Protection Collective (EPC) sur la Protection Individuelle (EPI). Le garde-corps périphérique installé en bord de toiture empêche la chute de l'ensemble des intervenants présents sur le chantier."
                },
                {
                    "questionNumber": 4,
                    "question": "Sur un plan de calepinage, que représente le développé d'un profilé en zinc ?",
                    "answerOptions": [
                        {"text": "La largeur totale de la bande de tôle plane nécessaire pour façonner la pièce avant tout pliage ou ourlet", "isCorrect": True},
                        {"text": "L'inclinaison longitudinale exacte exprimée en millimètres par mètre linéaire qu'il faut appliquer pour garantir l'écoulement gravitaire de l'eau vers la descente pluviale", "isCorrect": False},
                        {"text": "La distance géométrique mesurée entre le point d'ancrage le plus haut de la couverture et la ligne d'égout inférieure afin de déterminer le nombre de crochets de fixation indispensables pour éviter un arrachement sous la force du vent", "isCorrect": False},
                        {"text": "L'épaisseur nominale de la feuille de zinc ajoutée à la tolérance de dilatation thermique estivale permettant de calculer le jeu d'emboîtement des moignons sur les gouttières pendantes", "isCorrect": False}
                    ],
                    "correction": "Le développé correspond à la largeur de la feuille de métal mise à plat avant le façonnage. C'est une donnée géométrique cruciale pour le zingueur afin de débiter les bobines aux bonnes dimensions en incluant les plis, les ourlets et les pinces."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la pente minimale couramment exigée pour assurer le bon écoulement gravitaire dans une gouttière pendante en zinc ?",
                    "answerOptions": [
                        {"text": "Cinq millimètres par mètre", "isCorrect": True},
                        {"text": "Un centimètre par mètre", "isCorrect": False},
                        {"text": "Cinq centimètres par mètre", "isCorrect": False},
                        {"text": "Quinze millimètres par mètre", "isCorrect": False}
                    ],
                    "correction": "Le DTU 40.5 encadrant la pose des gouttières en zinc impose une pente minimale de 5 mm par mètre linéaire (soit 0,5 %). Cette inclinaison évite la stagnation de l'eau et l'accumulation de feuilles mortes ou de sédiments."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel document obligatoire atteste de la capacité d'un ouvrier à monter et utiliser un échafaudage roulant en toute sécurité ?",
                    "answerOptions": [
                        {"text": "Attestation de formation", "isCorrect": True},
                        {"text": "Le certificat d'aptitude à la conduite en sécurité des engins de levage et de manutention", "isCorrect": False},
                        {"text": "Le plan général de coordination en matière de sécurité et de protection de la santé", "isCorrect": False},
                        {"text": "Le procès verbal de réception technique des ancrages chimiques et mécaniques du chantier", "isCorrect": False}
                    ],
                    "correction": "Le montage, le démontage et l'utilisation d'échafaudages nécessitent une attestation de formation spécifique en cours de validité (R408), délivrée par l'employeur ou un organisme agréé, pour prévenir les risques d'effondrement et de chute."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel rôle principal joue un écran de sous-toiture HPV dans un complexe de couverture en zinc ?",
                    "answerOptions": [
                        {"text": "Il laisse s'échapper la vapeur d'eau tout en bloquant l'humidité extérieure", "isCorrect": True},
                        {"text": "Il augmente la résistance mécanique des tasseaux de fixation de la couverture", "isCorrect": False},
                        {"text": "Il empêche la formation de la patine protectrice sous la face interne du zinc", "isCorrect": False},
                        {"text": "Il conduit l'électricité statique vers le système de mise à la terre du bâtiment", "isCorrect": False}
                    ],
                    "correction": "L'écran Hautement Perméable à la Vapeur (HPV) est placé sous le support de couverture. Il empêche la condensation de s'accumuler dans l'isolant en laissant respirer la toiture, tout en offrant une barrière d'étanchéité supplémentaire contre la poudreuse ou les infiltrations accidentelles."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle procédure de sécurité est impérative lors de l'utilisation de l'acide chlorhydrique pour décaper le zinc avant soudure ?",
                    "answerOptions": [
                        {"text": "Porter des lunettes étanches et des gants en nitrile épais pour éviter toute projection corrosive sur la peau", "isCorrect": True},
                        {"text": "Verser brutalement une grande quantité d'eau froide dans le récipient contenant l'acide afin de créer une réaction exothermique rapide qui nettoiera instantanément les pannes en cuivre du fer à souder", "isCorrect": False},
                        {"text": "Chauffer directement la bouteille de décapant chimique avec un chalumeau oxyacétylénique de forte puissance pour augmenter sa fluidité capillaire et garantir une meilleure pénétration de l'alliage d'étain dans les replis de la tôle", "isCorrect": False},
                        {"text": "Stocker le flacon d'acide à l'intérieur de la boîte à outils métallique avec le plomb et les profilés en cuivre sans aucun bouchon hermétique pour faciliter l'accès rapide lors des travaux sur des gouttières suspendues", "isCorrect": False}
                    ],
                    "correction": "L'acide chlorhydrique (esprit de sel) employé brut ou \"tué\" au zinc est un liquide hautement corrosif. Le port de lunettes étanches et de gants résistant aux produits chimiques est vital pour prévenir les brûlures graves aux yeux et aux mains lors des éclaboussures."
                },
                {
                    "questionNumber": 9,
                    "question": "Comment calcule-t-on la surface en plan d'un pan de toiture rectangulaire simple ?",
                    "answerOptions": [
                        {"text": "En multipliant la longueur de l'égout par la longueur du rampant", "isCorrect": True},
                        {"text": "En additionnant la longueur de l'égout et la hauteur du faîtage", "isCorrect": False},
                        {"text": "En divisant la surface totale du bâtiment par le degré de pente", "isCorrect": False},
                        {"text": "En soustrayant le débord de toit à la largeur totale de l'édifice", "isCorrect": False}
                    ],
                    "correction": "La surface réelle d'un pan de toiture s'obtient simplement par la formule mathématique de l'aire d'un rectangle : Longueur multipliée par la largeur. En couverture, cela correspond à la longueur de l'égout multipliée par la longueur du rampant (la distance de l'égout au faîtage)."
                },
                {
                    "questionNumber": 10,
                    "question": "Qu'est-ce que le facteur de chute en matière de sécurité lors de l'utilisation d'un harnais ?",
                    "answerOptions": [
                        {"text": "Le rapport entre la hauteur de la chute et la longueur de la longe", "isCorrect": True},
                        {"text": "Le coefficient d'élasticité du cordage composant la ligne de vie", "isCorrect": False},
                        {"text": "L'angle d'inclinaison maximal autorisé pour la pose des tuiles", "isCorrect": False},
                        {"text": "Le poids de l'opérateur multiplié par la vitesse du vent au sommet", "isCorrect": False}
                    ],
                    "correction": "Le facteur de chute détermine la sévérité du choc subi par le corps. Il se calcule en divisant la hauteur de chute libre par la longueur de la longe. Idéalement, le point d'ancrage doit être situé au-dessus de l'utilisateur pour minimiser cette distance (facteur de chute 0)."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel phénomène physique le zingueur doit-il impérativement intégrer lors des calculs de longueur des gouttières pendantes ?",
                    "answerOptions": [
                        {"text": "Dilatation thermique", "isCorrect": True},
                        {"text": "L'effet de résonance acoustique provoqué par le passage des vents cisaillants", "isCorrect": False},
                        {"text": "L'accumulation de charges électrostatiques sur les éléments métalliques exposés", "isCorrect": False},
                        {"text": "Le phénomène de catalyse galvanique engendré par l'eau de pluie très acide", "isCorrect": False}
                    ],
                    "correction": "Le zinc se dilate et se rétracte considérablement en fonction des variations de température atmosphérique. Les longueurs continues de gouttières ou de chéneaux doivent intégrer des jeux d'expansion et des joints de dilatation (partie centrale en néoprène) pour éviter que les soudures ne se déchirent sous la contrainte."
                },
                {
                    "questionNumber": 12,
                    "question": "Pourquoi est-il indispensable d'utiliser un bloc de pierre ammoniacale solide pour l'entretien du fer à souder de couvreur ?",
                    "answerOptions": [
                        {"text": "Elle nettoie en profondeur la panne en cuivre chauffée et facilite l'accroche de l'étain lors du rétamage manuel", "isCorrect": True},
                        {"text": "Elle génère une réaction thermique exothermique ultra puissante capable de faire fondre instantanément des plaques d'acier galvanisé de très forte épaisseur sans nécessiter d'apport de gaz butane ou propane sur le chantier", "isCorrect": False},
                        {"text": "Elle dissout totalement les anciennes soudures au plomb présentes sur les gouttières centenaires en créant un gaz neutre qui remplace la ventilation mécanique obligatoire exigée par l'inspection du travail", "isCorrect": False},
                        {"text": "Elle modifie chimiquement la structure cristalline du zinc pur pour le transformer en un alliage inoxydable insensible à la formation de la patine grisâtre caractéristique des toitures traditionnelles parisiennes", "isCorrect": False}
                    ],
                    "correction": "Le pain de sel ammoniac permet de décaper l'oxydation noircie présente sur la panne en cuivre du fer à souder chaud. En y frottant la panne avec un peu d'alliage étain-plomb, le zingueur restaure un étamage brillant, ce qui est strictement indispensable pour garantir un bon transfert de chaleur vers la tôle."
                },
                {
                    "questionNumber": 13,
                    "question": "Sur un chantier en hauteur, que désigne le tirant d'air de sécurité ?",
                    "answerOptions": [
                        {"text": "La distance libre nécessaire sous l'utilisateur pour ne pas heurter le sol en cas de chute", "isCorrect": True},
                        {"text": "L'espace de ventilation aménagé sous la volige en bois pour éviter la condensation", "isCorrect": False},
                        {"text": "La longueur de corde maximale autorisée par le mécanisme de l'enrouleur à rappel", "isCorrect": False},
                        {"text": "Le volume d'air aspiré par le brûleur du fer à souder pour maintenir sa flamme", "isCorrect": False}
                    ],
                    "correction": "Le tirant d'air est la hauteur de dégagement minimale requise sous les pieds de l'ouvrier. Ce calcul intègre le déploiement de l'absorbeur d'énergie de la longe, le déplacement de l'ancrage, la taille de l'opérateur et une marge de sécurité minimale d'un mètre."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel réflexe doit adopter un zingueur qui découvre des plaques fibrociment suspectes lors d'une réfection de chéneau ?",
                    "answerOptions": [
                        {"text": "Stopper les travaux, sécuriser la zone et alerter sa hiérarchie pour expertise", "isCorrect": True},
                        {"text": "Casser les plaques à la masse pour les évacuer rapidement dans des sacs poubelles", "isCorrect": False},
                        {"text": "Découper proprement les éléments à la meuleuse d'angle pour éviter la poussière", "isCorrect": False},
                        {"text": "Enduire les plaques de mastic polyuréthane pour isoler le danger de manière pérenne", "isCorrect": False}
                    ],
                    "correction": "Les toitures en fibrociment d'avant 1997 contiennent presque toutes de l'amiante. Toute intervention sur ce matériau est strictement encadrée par la réglementation (Sous-section 3 ou 4) et nécessite l'arrêt immédiat du chantier pour protéger les salariés de l'inhalation de fibres cancérigènes très volatiles."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle est l'utilité des plinthes installées sur les planchers d'un échafaudage de pied ?",
                    "answerOptions": [
                        {"text": "Empêcher la chute d'outils, de matériaux ou de gravats vers les niveaux inférieurs et protéger le public", "isCorrect": True},
                        {"text": "Maintenir le niveau d'horizontalité des plateaux en aluminium lors du passage répété des chariots élévateurs de grande capacité chargés de bobines de zinc et de cuivre lourdement palettisées", "isCorrect": False},
                        {"text": "Assurer la continuité électrique du système de mise à la terre afin d'éliminer définitivement le risque de foudroiement de la structure tubulaire lors des violents orages d'été en haute montagne", "isCorrect": False},
                        {"text": "Augmenter la rigidité torsionnelle de l'ensemble de l'armature métallique pour autoriser l'amarrage de câbles de traction destinés au levage de la charpente traditionnelle en bois massif de chêne", "isCorrect": False}
                    ],
                    "correction": "Les plinthes, d'une hauteur minimale de dix à quinze centimètres, bordent la périphérie du plancher de l'échafaudage. Complétées par des lisses et sous-lisses, elles constituent une protection collective primordiale contre les chutes d'objets ou de matériaux sur les ouvriers et les piétons circulant en contrebas."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel document est requis avant de creuser le sol pour implanter la base d'un échafaudage ou raccorder un regard d'eau pluviale près d'une voirie ?",
                    "answerOptions": [
                        {"text": "La DICT", "isCorrect": True},
                        {"text": "Le formulaire d'attestation fiscale de régularité d'entreprise de bâtiment", "isCorrect": False},
                        {"text": "Le certificat d'homologation des tuyaux de descente en cuivre rouge", "isCorrect": False},
                        {"text": "Le procès verbal de réception des charpentes en bois lamellé collé", "isCorrect": False}
                    ],
                    "correction": "La Déclaration d'Intention de Commencement de Travaux (DICT) est obligatoire avant toute exécution de fouilles. Elle est envoyée aux exploitants des réseaux pour s'assurer de l'absence de conduites enterrées (gaz, électricité à haute tension, fibre optique, eau) à l'endroit précis du terrassement."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle précaution doit être prise lors de l'installation d'une goulotte d'évacuation de gravats depuis un toit ?",
                    "answerOptions": [
                        {"text": "La fixer solidement à la structure et la bâcher à sa base pour limiter les poussières", "isCorrect": True},
                        {"text": "La monter avec un angle strictement perpendiculaire au sol pour accélérer la chute", "isCorrect": False},
                        {"text": "Graisser l'intérieur des tubes cylindriques pour éviter le blocage des éléments", "isCorrect": False},
                        {"text": "Retirer le harnais de sécurité pour gagner en liberté de mouvement pendant la pose", "isCorrect": False}
                    ],
                    "correction": "Une goulotte d'évacuation accumule un poids important et subit une grande force cinétique à chaque jet de gravats. Elle doit être très solidement arrimée à la maçonnerie ou à l'échafaudage. De plus, la réception dans la benne doit être couverte ou humidifiée pour maîtriser les émissions de poussières nocives en milieu urbain."
                },
                {
                    "questionNumber": 18,
                    "question": "Pourquoi le calcul du recouvrement transversal des feuilles de zinc est-il dépendant de l'inclinaison de la toiture ?",
                    "answerOptions": [
                        {"text": "Plus la pente est faible, plus le recouvrement doit être important pour contrer les remontées capillaires de l'eau poussée par le vent", "isCorrect": True},
                        {"text": "Plus la pente est forte, plus il faut créer de doubles agrafes soudées sur toute la longueur afin d'empêcher les feuilles de glisser sous l'effet de l'attraction gravitationnelle terrestre concentrée sur le faîtage", "isCorrect": False},
                        {"text": "L'inclinaison détermine exclusivement l'épaisseur nominale de la tôle d'acier galvanisé qu'il faudra commander auprès du fournisseur pour résister de manière optimale à la charge exceptionnelle causée par les chutes de neige hivernales", "isCorrect": False},
                        {"text": "L'angle du toit définit la température exacte à laquelle le fer à souder au butane devra être réglé pour garantir une polymérisation adéquate du flux décapant chimique intégré dans la bobine de métal d'apport sans créer d'oxydation prématurée", "isCorrect": False}
                    ],
                    "correction": "L'eau s'écoule beaucoup plus lentement sur une toiture à faible pente. Le vent et les tempêtes peuvent alors repousser l'eau sous les joints par phénomène de remontée capillaire. Le DTU 40.41 impose d'augmenter le recouvrement des bacs ou de recourir à un joint debout à double sertissage pour garantir une étanchéité absolue à faible inclinaison."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est la position obligatoire de stockage et d'utilisation d'une bouteille de gaz propane sur un chantier de zinguerie ?",
                    "answerOptions": [
                        {"text": "Toujours à la verticale, robinet vers le haut", "isCorrect": True},
                        {"text": "Toujours à l'horizontale, calée par des briques", "isCorrect": False},
                        {"text": "Suspendue par une corde au bord de l'échafaudage", "isCorrect": False},
                        {"text": "Renversée à l'envers pour augmenter la pression de sortie", "isCorrect": False}
                    ],
                    "correction": "Les bouteilles de gaz liquéfié sous pression doivent impérativement être maintenues debout. Une utilisation couchée risque de provoquer l'arrivée de gaz à l'état liquide directement dans le détendeur et le tuyau, créant un risque immédiat d'incendie majeur (torche géante) au niveau du chalumeau ou du fer à souder."
                },
                {
                    "questionNumber": 20,
                    "question": "Pourquoi le zingueur couvreur ne doit-il jamais porter de vêtements de travail en fibres synthétiques lors des opérations de soudure ?",
                    "answerOptions": [
                        {"text": "Les fibres synthétiques fondent instantanément au contact d'une étincelle et collent profondément à l'épiderme, aggravant sévèrement les lésions cutanées", "isCorrect": True},
                        {"text": "Les vêtements en nylon ou en polyester génèrent un puissant champ électromagnétique statique qui dérègle inévitablement les composants électroniques miniatures intégrés dans le système d'allumage piézoélectrique du chalumeau portatif", "isCorrect": False},
                        {"text": "Les textiles synthétiques sont totalement imperméables à l'air ambiant et empêchent la transpiration naturelle, provoquant un refroidissement brutal du corps qui paralyse les muscles articulaires lors des longs déplacements périlleux sur les charpentes en pente", "isCorrect": False},
                        {"text": "Le contact direct entre le zinc oxydé et les polymères plastiques crée une réaction chimique exothermique libérant des émanations suffocantes capables de saturer immédiatement les cartouches des masques de protection respiratoire du personnel d'atelier", "isCorrect": False}
                    ],
                    "correction": "Lors des travaux par points chauds (soudure au fer, utilisation de l'acide), les projections de métal en fusion (étain) ou de flux sont courantes. Les vêtements 100 % coton ou renforcés de cuir résistent bien à la chaleur, tandis que les textiles synthétiques fondent sur eux-mêmes et pénètrent dans la peau, causant des brûlures chirurgicales extrêmement graves."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : SCIENCES DES MATÉRIAUX ET OUTILLAGE DU ZINGUEUR (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : SCIENCES DES MATÉRIAUX ET OUTILLAGE DU ZINGUEUR",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel outil à main spécifique le zingueur utilise-t-il pour tracer un repère de coupe ou de pliage profondément dans l'épaisseur de la tôle de zinc ?",
                    "answerOptions": [
                        {"text": "La griffe", "isCorrect": True},
                        {"text": "L'outil rotatif de découpe électrique de haute précision", "isCorrect": False},
                        {"text": "Le compas à pointe sèche en acier trempé de menuisier", "isCorrect": False},
                        {"text": "Le traceur laser à nivellement automatique pour façade", "isCorrect": False}
                    ],
                    "correction": "La griffe à zinc est l'outil de traçage fondamental du couvreur. Munie d'une pointe en acier très dure, elle permet de rayer la surface du métal avec précision. Le sillon tracé sert de repère visuel mais fragilise aussi légèrement la tôle pour faciliter une coupe franche ou un pliage rectiligne."
                },
                {
                    "questionNumber": 22,
                    "question": "Qu'est-ce qui provoque l'apparition de la \"rouille blanche\" destructrice sur les feuilles de zinc ?",
                    "answerOptions": [
                        {"text": "Le confinement en milieu humide sans ventilation en sous-face", "isCorrect": True},
                        {"text": "L'exposition directe aux puissants rayons ultraviolets du soleil", "isCorrect": False},
                        {"text": "Le contact prolongé avec des chutes de tuyaux en plomb pur", "isCorrect": False},
                        {"text": "La réaction chimique avec un flux décapant résiduel neutre", "isCorrect": False}
                    ],
                    "correction": "La rouille blanche est un hydroxyde de zinc pulvérulent qui ronge le métal. Elle se forme lorsque le zinc est exposé à l'humidité sans présence suffisante de dioxyde de carbone (qui permet normalement la formation de la patine protectrice). Cela arrive typiquement lors d'un stockage sous bâche humide ou en l'absence de lame d'air ventilée sous la couverture."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est l'incompatibilité chimique majeure entre le zinc et la maçonnerie fraîche lors de la pose d'un solin ou d'un abergement ?",
                    "answerOptions": [
                        {"text": "Le ciment frais dégage une forte alcalinité qui ronge rapidement la pellicule protectrice du zinc et perfore la tôle.", "isCorrect": True},
                        {"text": "Les granulats du mortier créent une friction mécanique qui raye la surface du métal lors des variations de température mais sans attaquer la structure interne.", "isCorrect": False},
                        {"text": "L'eau contenue dans le ciment s'évapore et crée un pont thermique qui gèle instantanément la sous-face de la couverture métallique en plein hiver, provoquant une fissuration généralisée de la bande d'égout et des chéneaux attenants.", "isCorrect": False},
                        {"text": "Le mélange de sable et d'eau génère une réaction endothermique qui refroidit brutalement la feuille de zinc et empêche sa dilatation normale.", "isCorrect": False}
                    ],
                    "correction": "Le zinc est extrêmement sensible aux milieux basiques (pH > 7). Le ciment, le béton et le plâtre frais sont hautement alcalins et attaquent le métal par corrosion chimique. Un isolant (couche bitumineuse, film polymère ou feuille de plomb) doit impérativement séparer le zinc d'une maçonnerie fraîche."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel outil manuel est indispensable pour relever les bords d'une feuille de métal afin de préparer un raccordement à agrafes ?",
                    "answerOptions": [
                        {"text": "Pince à border", "isCorrect": True},
                        {"text": "Machine de profilage à rouleaux motorisée industrielle", "isCorrect": False},
                        {"text": "Cisaille guillotine à levier démultiplié de mécanicien", "isCorrect": False},
                        {"text": "Marteau de menuisier à panne fendue arrache-clous", "isCorrect": False}
                    ],
                    "correction": "La pince à border (ou pince à plier) permet de façonner à la main les relevés, les pinces ou les ourlets sur les bords d'une feuille de zinc, de cuivre ou de plomb, particulièrement lors des travaux sur les profils complexes d'abergement."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment se nomme la couche naturelle qui se forme à la surface du zinc exposé à l'air libre et le protège de la corrosion ?",
                    "answerOptions": [
                        {"text": "La patine protectrice", "isCorrect": True},
                        {"text": "La couche de galvanisation", "isCorrect": False},
                        {"text": "Le film d'anodisation", "isCorrect": False},
                        {"text": "L'oxydation ferrique", "isCorrect": False}
                    ],
                    "correction": "Au contact de l'oxygène, de l'eau et du dioxyde de carbone présents dans l'atmosphère, le zinc développe une couche d'hydrocarbonate de zinc compacte, adhérente et insoluble dans l'eau. C'est la patine, qui donne au zinc sa couleur gris clair mate et assure sa longévité exceptionnelle."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelles sont les propriétés mécaniques du plomb qui justifient son utilisation pour la réalisation d'abergements complexes autour d'une cheminée ?",
                    "answerOptions": [
                        {"text": "Il offre une malléabilité exceptionnelle permettant d'épouser des formes tridimensionnelles complexes à froid.", "isCorrect": True},
                        {"text": "Il se distingue par une rigidité structurelle extrêmement élevée qui autorise son utilisation comme élément porteur principal pour le franchissement de portées supérieures à cinq mètres sans l'ajout d'aucun tasseau de renfort.", "isCorrect": False},
                        {"text": "Il présente un coefficient de dilatation thermique pratiquement nul ce qui permet de réaliser des noues continues sans aucun joint de fractionnement ou moignon de dilatation.", "isCorrect": False},
                        {"text": "Il réagit fortement au contact de l'eau de pluie en libérant une fine pellicule de cuivre pur qui imperméabilise totalement la surface poreuse des tuiles adjacentes.", "isCorrect": False}
                    ],
                    "correction": "Le plomb laminé est le matériau le plus malléable en couverture. Il peut être battu et étiré à froid (au maillet et à la batte) pour s'adapter parfaitement aux reliefs très irréguliers des tuiles, des ardoises et de la maçonnerie, assurant une étanchéité parfaite des points singuliers."
                },
                {
                    "questionNumber": 27,
                    "question": "Pourquoi le façonnage du zinc doit-il être réalisé exclusivement avec un maillet en bois ou en plastique plutôt qu'avec un marteau en acier ?",
                    "answerOptions": [
                        {"text": "Éviter l'amincissement et le marquage destructif de la feuille métallique", "isCorrect": True},
                        {"text": "Augmenter la force de frappe sur les ourlets récalcitrants en bordure", "isCorrect": False},
                        {"text": "Transmettre de la chaleur par friction mécanique intense sur le métal", "isCorrect": False},
                        {"text": "Créer une résonance acoustique indiquant la bonne courbure de la tôle", "isCorrect": False}
                    ],
                    "correction": "Le zinc laminé est un métal relativement tendre. L'utilisation d'un marteau en acier écrouit le métal, crée des cratères (marquages), affine l'épaisseur et risque de percer la tôle. Un maillet (en buis, en plastique ou à embout nylon) permet de plier le métal en douceur en répartissant l'onde de choc."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle essence de bois de voligeage, très acide, est strictement interdite en contact direct avec une toiture en zinc ?",
                    "answerOptions": [
                        {"text": "Le chêne", "isCorrect": True},
                        {"text": "Le sapin de charpente traité à cœur contre l'humidité", "isCorrect": False},
                        {"text": "L'épicéa séché rapidement en étuve industrielle régulée", "isCorrect": False},
                        {"text": "Le peuplier utilisé couramment pour les panneaux minces", "isCorrect": False}
                    ],
                    "correction": "Le chêne, ainsi que le châtaignier, contiennent de fortes proportions de tanins très acides (pH < 5). En présence d'humidité, ces acides attaquent et perforent la sous-face du zinc. Le DTU couverture en zinc préconise l'utilisation de résineux compatibles comme le sapin, l'épicéa ou le pin sylvestre."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la particularité du coefficient de dilatation linéaire du zinc par rapport à celui de l'acier qui compose la charpente métallique ?",
                    "answerOptions": [
                        {"text": "Le zinc se dilate beaucoup plus que l'acier sous l'effet des variations de température, exigeant des jeux de dilatation plus importants.", "isCorrect": True},
                        {"text": "Le zinc possède une stabilité thermique absolue qui le rend totalement insensible aux écarts de température estivaux, contrairement à l'acier qui se déforme très rapidement au soleil.", "isCorrect": False},
                        {"text": "Le coefficient d'expansion du zinc est strictement identique à celui du plomb et de l'acier galvanisé, ce qui permet au couvreur d'employer indifféremment des pattes de fixation fixes sur l'ensemble de la toiture, qu'elle soit exposée au nord ou au sud, sans risque de cisaillement mécanique au niveau des coutures serties à la main.", "isCorrect": False},
                        {"text": "Le métal s'allonge uniquement lorsqu'il est chauffé localement par la panne en cuivre du fer à souder mais retrouve instantanément et définitivement sa longueur initiale dès que l'alliage d'apport est solidifié à température ambiante.", "isCorrect": False}
                    ],
                    "correction": "Le zinc a un coefficient de dilatation linéaire très élevé (0,022 mm/m/°C), soit presque le double de celui de l'acier. Une bande de zinc de 10 mètres peut s'allonger de plus de 15 mm entre l'hiver et l'été. La pose exige donc l'intégration de jeux et de pattes coulissantes pour absorber ce mouvement perpétuel."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel phénomène chimique se déclenche inévitablement si l'on installe un chéneau en cuivre pur au-dessus d'une descente en zinc ?",
                    "answerOptions": [
                        {"text": "L'eau lessivant le cuivre perfore le zinc par corrosion galvanique", "isCorrect": True},
                        {"text": "Le zinc se couvre d'une belle patine verte très protectrice et durable", "isCorrect": False},
                        {"text": "Le cuivre s'oxyde et se dissout au contact direct des vapeurs du zinc", "isCorrect": False},
                        {"text": "L'étanchéité globale du système est renforcée par électrolyse passive", "isCorrect": False}
                    ],
                    "correction": "Il existe un ordre de noblesse des métaux. Le cuivre est un métal très noble (cathode) par rapport au zinc (anode). L'eau de pluie qui s'écoule sur le cuivre se charge en ions cuivriques et, en tombant sur le zinc, provoque une électrolyse foudroyante qui perfore le zinc en quelques mois. Le montage inverse (zinc au-dessus du cuivre) est en revanche autorisé."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel outil manuel d'atelier est spécialement conçu pour découper des courbes complexes dans une tôle plane ?",
                    "answerOptions": [
                        {"text": "Cisaille pélican", "isCorrect": True},
                        {"text": "Scie circulaire équipée d'une lame en acier carbure", "isCorrect": False},
                        {"text": "Tronçonneuse thermique à grand disque diamant renforcé", "isCorrect": False},
                        {"text": "Découpeur plasma à commande numérique informatisée", "isCorrect": False}
                    ],
                    "correction": "La cisaille pélican (ou cisaille de couvreur) est l'outil de coupe manuelle par excellence. La forme déportée de ses lames permet à la feuille de métal de glisser sous la main de l'opérateur sans buter, autorisant la coupe de longues bandes droites ou de courbes prononcées sans déformer la tôle."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le rôle exact de la patine grise du zinc sur un bâtiment ancien ?",
                    "answerOptions": [
                        {"text": "C'est une couche de carbonate basique de zinc insoluble et compacte qui protège le métal sous-jacent contre la progression de la corrosion atmosphérique.", "isCorrect": True},
                        {"text": "C'est un dépôt calcaire très poreux qui absorbe l'humidité ambiante afin de refroidir l'intérieur des combles aménagés pendant les fortes canicules estivales de plus de quarante degrés.", "isCorrect": False},
                        {"text": "Il s'agit d'une réaction d'oxydoréduction artificielle provoquée délibérément par le couvreur en pulvérisant une solution d'acide chlorhydrique pure sur l'ensemble de la toiture immédiatement après la pose des feuilles, dans le but d'accélérer le vieillissement visuel du matériau pour satisfaire aux exigences drastiques des architectes des bâtiments de France.", "isCorrect": False},
                        {"text": "C'est un film d'huile de laminage qui remonte naturellement à la surface du métal sous l'action des rayons ultraviolets et qui empêche définitivement la prolifération des mousses et lichens végétaux incrustants.", "isCorrect": False}
                    ],
                    "correction": "La patine se forme naturellement en quelques mois à l'air libre. Cette oxydation de surface très dense agit comme un bouclier imperméable qui bloque l'oxygène et l'humidité, stoppant ainsi le processus de dégradation du métal à cœur."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la fonction principale d'une plieuse d'atelier en zinguerie ?",
                    "answerOptions": [
                        {"text": "Réaliser des plis rectilignes précis sur de grandes longueurs de tôle", "isCorrect": True},
                        {"text": "Souder bout à bout deux profilés métalliques par résistance électrique", "isCorrect": False},
                        {"text": "Cintrer des tuyaux de descente d'eau pluviale en cuivre ou en zinc", "isCorrect": False},
                        {"text": "Découper les feuilles de métal avec une lame guillotine motorisée", "isCorrect": False}
                    ],
                    "correction": "La plieuse manuelle (ou numérique) est la machine centrale de l'atelier du zingueur. Elle sert à façonner des couloirs, des noues, des larmiers ou des solins en effectuant des pliages nets, angulaires et homogènes sur des bandes pouvant atteindre 2 à 3 mètres de long."
                },
                {
                    "questionNumber": 34,
                    "question": "Pourquoi les règles de l'art interdisent-elles de plier fortement le zinc lorsque la température extérieure descend en dessous de sept degrés Celsius ?",
                    "answerOptions": [
                        {"text": "Le métal devient fragile et cassant, ce qui provoque des microfissures le long de la ligne de pliage lors du façonnage mécanique.", "isCorrect": True},
                        {"text": "La feuille se rétracte tellement sous l'action du froid intense que ses dimensions finales ne correspondent plus du tout aux tracés de calepinage initiaux réalisés en atelier.", "isCorrect": False},
                        {"text": "L'air froid emprisonné à l'intérieur des ourlets se dilate brutalement au retour des beaux jours, générant une surpression pneumatique d'une violence telle qu'elle fait exploser les soudures à l'étain et déchire littéralement les bandes d'astragale ainsi que les abergements de cheminée posés en périphérie.", "isCorrect": False},
                        {"text": "Le gel neutralise l'efficacité de la solution de décapage chimique, rendant toute tentative de soudure ultérieure au niveau des pinces de jonction absolument impossible à cause de la cristallisation du flux boraté.", "isCorrect": False}
                    ],
                    "correction": "Le zinc laminé pur perd considérablement de sa ductilité à basse température. Si on le plie à froid (température inférieure à 7°C ou 10°C selon les alliages), la fibre externe de la courbure se fissure, créant des amorces de rupture et des fuites. En hiver, le zingueur doit réchauffer la zone de pliage avec un chalumeau à air chaud ou au gaz."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel métal lourd et particulièrement résistant à la corrosion marine est fréquemment utilisé sous forme de bandes pré-façonnées pour garantir l'étanchéité des fenêtres de toit ?",
                    "answerOptions": [
                        {"text": "Le plomb", "isCorrect": True},
                        {"text": "L'acier inoxydable", "isCorrect": False},
                        {"text": "L'aluminium laqué", "isCorrect": False},
                        {"text": "Le fer forgé", "isCorrect": False}
                    ],
                    "correction": "Le plomb (souvent sous forme de bavettes ou de rouleaux plissés) est idéal pour raccorder de manière étanche la menuiserie de toit aux tuiles environnantes. Son poids l'empêche d'être soulevé par le vent, sa longévité est exceptionnelle et il se modèle à la forme exacte de l'onde de la tuile."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle spécificité métallurgique caractérise l'alliage de \"zinc-titane\" massivement utilisé aujourd'hui au détriment du zinc pur ?",
                    "answerOptions": [
                        {"text": "L'ajout de cuivre et de titane améliorant la résistance au fluage et la rigidité", "isCorrect": True},
                        {"text": "Un traitement de surface le rendant totalement invulnérable au contact du ciment", "isCorrect": False},
                        {"text": "Une teneur en fer élevée qui le rend magnétique pour un meilleur maintien sur charpente", "isCorrect": False},
                        {"text": "Un laquage en usine qui le dispense de forming sa propre patine naturelle atmosphérique", "isCorrect": False}
                    ],
                    "correction": "Le zinc laminé moderne est allié à de très faibles quantités de cuivre et de titane (norme EN 988). Cet alliage améliore considérablement ses caractéristiques mécaniques : la résistance à la traction est accrue et surtout, le fluage (la déformation lente sous son propre poids) est drastiquement réduit."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est le but de la griffe à cintrer (ou griffe à ourlet) utilisée sur le chantier ?",
                    "answerOptions": [
                        {"text": "Amorcer un pli arrondi régulier en bord de tôle pour rigidifier la bande finie", "isCorrect": True},
                        {"text": "Soulever les ardoises abîmées sans avoir à démonter toute la rangée supérieure", "isCorrect": False},
                        {"text": "Creuser la maçonnerie pour y encastrer la bavette en plomb du solin", "isCorrect": False},
                        {"text": "Retirer le surplus d'étain durci autour d'une soudure réalisée avec un fer trop chaud", "isCorrect": False}
                    ],
                    "correction": "La griffe à ourlet est un petit outil manuel doté d'une fente calibrée. En l'insérant sur le bord de la tôle et en la basculant progressivement sur toute la longueur, le zingueur prépare la tôle à recevoir un ourlet de finition cylindrique, qui évitera les coupures et apportera une excellente rigidité longitudinale au profilé."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment les bobines de zinc pur doivent-elles être manipulées et stockées sur un chantier pour garantir leur intégrité physique et chimique avant le façonnage ?",
                    "answerOptions": [
                        {"text": "Les manipuler avec précaution pour éviter les chocs qui marquent la tôle et les stocker à plat dans un endroit sec et ventilé.", "isCorrect": True},
                        {"text": "Les jeter directement depuis le camion de livraison sur le sol meuble du chantier afin de vérifier la résistance à l'impact de l'alliage avant son installation définitive sur la charpente.", "isCorrect": False},
                        {"text": "Les stocker debout directement sur un sol détrempé ou dans des flaques d'eau boueuse afin de pré-hydrater le métal et d'amorcer volontairement la formation de la fameuse couche de rouille blanche qui agira par la suite comme un répulsif naturel contre l'invasion des rongeurs et des insectes xylophages dans la charpente.", "isCorrect": False},
                        {"text": "Les dérouler complètement au sol en les piétinant avec des chaussures de sécurité à embout en acier pour éliminer mécaniquement la mémoire de forme liée au conditionnement cylindrique en usine de laminage.", "isCorrect": False}
                    ],
                    "correction": "Les métaux en bobine ou en feuilles doivent être préservés des chocs, des rayures et surtout de l'humidité. Un stockage intérieur, ventilé, à plat sur palette (pour éviter les déformations géométriques) prévient l'apparition d'amorce de fissures et l'oxydation de type \"rouille blanche\"."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel outil à main articulé permet au couvreur de refermer définitivement un profil d'assemblage à joint debout sur la charpente ?",
                    "answerOptions": [
                        {"text": "Une pince à sertir", "isCorrect": True},
                        {"text": "Un ciseau à froid", "isCorrect": False},
                        {"text": "Une griffe à tracer", "isCorrect": False},
                        {"text": "Une tenaille de forgeron", "isCorrect": False}
                    ],
                    "correction": "La pince à sertir (ou pince à border spécifique pour joint debout) est constituée de mors larges. Elle s'utilise en deux passes (fermeture du premier pli puis du deuxième) pour emboîter hermétiquement les plis relevés des deux bacs de toiture, créant une jonction mécanique étanche sans aucune soudure."
                },
                {
                    "questionNumber": 40,
                    "question": "Lors du montage bout à bout de profilés en zinc à l'intérieur d'un chéneau encaissé, pourquoi le zingueur doit-il obligatoirement ménager un écartement précis entre les deux feuilles de métal au niveau de la jonction centrale ?",
                    "answerOptions": [
                        {"text": "Pour permettre la libre dilatation thermique du métal lors des chaudes journées d'été", "isCorrect": True},
                        {"text": "Pour évacuer rapidement le trop-plein d'eau de pluie vers un orifice de sécurité masqué", "isCorrect": False},
                        {"text": "Pour économiser intelligemment la quantité de métal d'apport en soudure nécessaire au joint", "isCorrect": False},
                        {"text": "Pour faciliter le démontage futur de l'installation par un autre corps de métier du bâtiment", "isCorrect": False}
                    ],
                    "correction": "C'est le principe du joint de dilatation. Sans un écart d'environ 10 à 15 mm entre les tôles couvert par une main de dilatation en néoprène, l'allongement thermique du zinc écraserait les tôles l'une contre l'autre, provoquant un phénomène de flambement, de boursouflure puis la déchirure immédiate des soudures capillaires."
                }
            ]
        },
# =========================================================================
        # THÈME 3 : TRAÇAGE, FAÇONNAGE ET TECHNIQUES DE SOUDURE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : TRAÇAGE, FAÇONNAGE ET TECHNIQUES DE SOUDURE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel métal est utilisé pour forger la panne du fer à souder du zingueur ?",
                    "answerOptions": [
                        {"text": "Cuivre", "isCorrect": True},
                        {"text": "Un alliage d'acier trempé à haute résistance thermique utilisé en forge industrielle", "isCorrect": False},
                        {"text": "Du tungstène purifié pour éviter toute oxydation lors de la montée en température", "isCorrect": False},
                        {"text": "De la fonte d'aluminium spécialement traitée pour résister à la corrosion acide", "isCorrect": False}
                    ],
                    "correction": "Le cuivre est un excellent conducteur de chaleur. Il accumule l'énergie thermique du brûleur à gaz et la restitue de façon constante lors du soudage par capillarité sur les tôles de zinc."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le rôle de l'acide chlorhydrique tué (ou neutralisé) lors de la soudure du zinc ?",
                    "answerOptions": [
                        {"text": "Décaper la couche d'oxydation pour permettre l'accroche de l'étain", "isCorrect": True},
                        {"text": "Refroidir très rapidement le bain de fusion pour éviter le perçage", "isCorrect": False},
                        {"text": "Colorer chimiquement la soudure en gris pour des raisons d'esthétique", "isCorrect": False},
                        {"text": "Renforcer la résistance mécanique de l'assemblage contre la torsion", "isCorrect": False}
                    ],
                    "correction": "Le décapant élimine l'oxyde de zinc en surface. Un métal oxydé repousse l'alliage d'apport. Le décapage est donc strictement indispensable pour obtenir une soudure par capillarité étanche et solide."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la composition standard de l'alliage d'apport couramment utilisé par le couvreur pour souder le zinc ?",
                    "answerOptions": [
                        {"text": "Un tiers de plomb et deux tiers d'étain", "isCorrect": True},
                        {"text": "Moitié de cuivre pur et moitié d'argent", "isCorrect": False},
                        {"text": "Quatre-vingts pour cent de zinc et vingt pour cent de fer", "isCorrect": False},
                        {"text": "Du titane mélangé avec un faible pourcentage d'aluminium", "isCorrect": False}
                    ],
                    "correction": "La baguette de soudure tendre traditionnelle en zinguerie est un alliage étain-plomb (généralement 33 pour cent plomb et 67 pour cent étain). Son point de fusion bas (environ 185 degrés) permet de souder sans risquer de fondre la feuille de zinc."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel phénomène physique fondamental garantit l'étanchéité absolue d'une soudure à l'étain entre deux feuilles de zinc superposées ?",
                    "answerOptions": [
                        {"text": "La capillarité qui aspire le métal d'apport liquide dans l'interstice étroit entre les deux tôles", "isCorrect": True},
                        {"text": "L'attraction électromagnétique provoquée par la panne en cuivre qui fusionne instantanément les atomes de zinc et d'étain pour créer un nouveau réseau cristallin aux propriétés d'étanchéité très supérieures à celles du métal d'origine", "isCorrect": False},
                        {"text": "La dilatation thermique réversible des feuilles de métal qui écrasent mécaniquement le cordon de soudure lors de leur refroidissement naturel sous l'action directe des vents dominants circulant sur la toiture", "isCorrect": False},
                        {"text": "L'oxydation rapide et immédiate du plomb contenu dans la baguette d'apport qui forme une mousse étanche empêchant toute infiltration d'eau de pluie au niveau des recouvrements transversaux des gouttières", "isCorrect": False}
                    ],
                    "correction": "La soudure tendre en zinguerie est une soudure par capillarité. Le métal d'apport fondu est aspiré entre les deux tôles (qui doivent être rapprochées de 0,1 à 0,5 mm) pour former un joint continu et parfaitement imperméable."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment prépare-t-on de l'acide chlorhydrique tué de manière artisanale dans l'atelier ?",
                    "answerOptions": [
                        {"text": "En y dissolvant des chutes de zinc pur jusqu'à l'arrêt de l'effervescence", "isCorrect": True},
                        {"text": "En ajoutant un grand volume d'eau distillée bouillante dans la bouteille", "isCorrect": False},
                        {"text": "En mélangeant le liquide avec du sel ammoniac et du flux de soudure", "isCorrect": False},
                        {"text": "En chauffant le récipient au chalumeau pendant environ dix minutes", "isCorrect": False}
                    ],
                    "correction": "L'acide chlorhydrique tué s'obtient en ajoutant des morceaux de zinc de récupération dans de l'acide brut. La réaction chimique dégage de l'hydrogène et crée du chlorure de zinc, un décapant excellent et bien moins agressif que l'acide pur."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel type de joint longitudinal sans soudure utilise le zingueur pour relier les bacs de couverture sur une toiture à faible pente ?",
                    "answerOptions": [
                        {"text": "Agrafure", "isCorrect": True},
                        {"text": "Le rivetage mécanique avec application d'un joint en silicone industriel", "isCorrect": False},
                        {"text": "Le collage structural bicomposant utilisé dans l'industrie aéronautique", "isCorrect": False},
                        {"text": "Le recouvrement simple maintenu par des pointes en acier galvanisé", "isCorrect": False}
                    ],
                    "correction": "L'agrafage (ou agrafure) consiste à replier les bords de deux tôles l'un dans l'autre puis à les aplatir. Sur les toitures, on utilise principalement l'agrafure double (joint debout) pour garantir l'étanchéité sans recourir à la soudure, tout en autorisant la dilatation."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est la bonne méthode pour étamer correctement la panne en cuivre du fer à souder ?",
                    "answerOptions": [
                        {"text": "Frotter la panne chaude sur du sel ammoniac avec un peu d'alliage d'apport", "isCorrect": True},
                        {"text": "Plonger la panne incandescente dans un grand seau d'eau très froide", "isCorrect": False},
                        {"text": "Poncer vigoureusement la panne avec une meuleuse d'angle à disque dur", "isCorrect": False},
                        {"text": "Enduire la panne de graisse mécanique avant l'allumage du brûleur au gaz", "isCorrect": False}
                    ],
                    "correction": "Pour que la panne accroche le métal d'apport et le guide vers la soudure, elle doit être étamée. Le pain de sel ammoniac désoxyde le cuivre fortement chauffé, permettant à l'étain de fondre et de recouvrir la panne d'une pellicule brillante."
                },
                {
                    "questionNumber": 48,
                    "question": "Pourquoi est-il strictement déconseillé de souder une gouttière en zinc avec une panne de fer à souder portée à une température excessivement élevée ?",
                    "answerOptions": [
                        {"text": "La température trop forte brûle le métal d'apport et le zinc, créant des trous irréversibles et des soudures poreuses", "isCorrect": True},
                        {"text": "L'élévation thermique extrême provoque une évaporation immédiate du carbone contenu dans l'acier de la panne en cuivre ce qui génère une fumée noire extrêmement toxique capable d'intoxiquer l'opérateur en seulement quelques secondes d'inhalation directe sur le chantier", "isCorrect": False},
                        {"text": "La chaleur excessive modifie le champ magnétique de la gouttière en zinc au point d'attirer fortement toutes les particules de fer présentes dans l'atmosphère urbaine, déclenchant ainsi un processus foudroyant de corrosion galvanique impossible à stopper par la suite", "isCorrect": False},
                        {"text": "Le zinc surchauffé se transforme instantanément en un alliage de titane rigide qui refuse totalement de se dilater sous les rayons du soleil estival, provoquant la déchirure systématique et inévitable des talons de dilatation placés aux extrémités du système d'évacuation des eaux pluviales", "isCorrect": False}
                    ],
                    "correction": "Le zinc pur fond à 419 degrés Celsius. Si le fer est trop chaud, l'alliage étain-plomb s'oxyde, le décapant calcine sans agir, et le zinc de la pièce peut fondre ou se percer. Une panne correctement réglée maintient l'alliage à l'état liquide sans jamais brûler les métaux."
                },
                {
                    "questionNumber": 49,
                    "question": "Que doit réaliser le zingueur sur les bords d'un chéneau pour le rigidifier longitudinalement ?",
                    "answerOptions": [
                        {"text": "Façonner un ourlet périphérique cylindrique", "isCorrect": True},
                        {"text": "Souder une cornière en acier épais sous la base", "isCorrect": False},
                        {"text": "Appliquer une couche épaisse de goudron liquide", "isCorrect": False},
                        {"text": "Percer des trous de décompression tous les mètres", "isCorrect": False}
                    ],
                    "correction": "L'ourlet (ou boudin), façonné à l'aide d'une griffe à ourlet et d'un maillet, donne une excellente rigidité structurelle à la tôle. Cela évite le flambement et la déformation du chéneau ou de la gouttière entre les crochets de fixation."
                },
                {
                    "questionNumber": 50,
                    "question": "À quoi sert le flux décapant lors de la réalisation d'une soudure sur du zinc prépatiné ?",
                    "answerOptions": [
                        {"text": "Dissoudre chimiquement la couche de prépatinage pour atteindre le métal nu", "isCorrect": True},
                        {"text": "Créer un film protecteur pour empêcher la formation de la rouille blanche", "isCorrect": False},
                        {"text": "Changer la couleur de l'étain pour la rendre identique à celle du zinc", "isCorrect": False},
                        {"text": "Coller temporairement les tôles entre elles avant le passage du fer chaud", "isCorrect": False}
                    ],
                    "correction": "Le zinc prépatiné possède un traitement de surface industriel très dur qui empêche formellement l'étain d'adhérer. Un décapant liquide spécifique (ou un décapage abrasif mécanique) est incontournable pour éliminer cette couche et exposer le zinc pur à la soudure."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel métal de couverture historique, très lourd et malléable, nécessite un grattage mécanique minutieux avant toute opération de soudure à l'étain ?",
                    "answerOptions": [
                        {"text": "Plomb", "isCorrect": True},
                        {"text": "L'acier inoxydable martensitique utilisé pour les conduits de fumée", "isCorrect": False},
                        {"text": "L'alliage de titane pur réservé aux chantiers de restauration navale", "isCorrect": False},
                        {"text": "Le cuivre rouge fortement écroui lors de son passage au laminoir", "isCorrect": False}
                    ],
                    "correction": "Le plomb s'oxyde très rapidement à l'air libre pour former une couche sombre. Pour que la soudure par capillarité adhère, il faut obligatoirement gratter la surface à blanc au grattoir triangulaire juste avant de badigeonner de flux décapant et de chauffer."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est l'inconvénient technique d'un jeu interstitiel trop important entre deux feuilles de zinc préparées pour une soudure par capillarité ?",
                    "answerOptions": [
                        {"text": "L'alliage liquide ne peut plus être aspiré par capillarité et s'écoule au travers du vide, rendant l'étanchéité impossible", "isCorrect": True},
                        {"text": "Le vide excessif génère une dépression aérodynamique sous le rampant de toiture qui attire l'humidité résiduelle vers le haut en créant un pont thermique gigantesque capable de faire pourrir l'intégralité du voligeage en sapin massif posé en sous-face de la couverture", "isCorrect": False},
                        {"text": "L'écartement démesuré oblige le couvreur à combler le vide avec du ciment prompt à prise rapide, ce qui détruit immédiatement le film protecteur du zinc et provoque l'effondrement mécanique des chatières de ventilation fixées à proximité immédiate du raccordement soudé", "isCorrect": False},
                        {"text": "L'espace trop large empêche l'opérateur de positionner ses pinces de serrage autobloquantes, ce qui entraîne le glissement immédiat des feuilles de métal vers la voie publique sous l'effet de l'inclinaison gravitationnelle spécifique aux toitures traditionnelles de type Mansart", "isCorrect": False}
                    ],
                    "correction": "La capillarité, ce phénomène physique qui fait monter les fluides dans les espaces très fins, ne fonctionne que si les tôles sont presque en contact. Un vide supérieur à un demi-millimètre empêche l'aspiration de l'étain fondu, qui tombera simplement au travers du joint."
                },
                {
                    "questionNumber": 53,
                    "question": "Comment appelle-t-on la technique permettant de rabattre les bords d'une plaque de métal à angle droit avec un maillet ou une pince ?",
                    "answerOptions": [
                        {"text": "Le relevé ou le rabattage de pince", "isCorrect": True},
                        {"text": "Le cintrage au chalumeau oxyacétylénique", "isCorrect": False},
                        {"text": "L'emboutissage profond par pression", "isCorrect": False},
                        {"text": "Le soyage mécanique à froid", "isCorrect": False}
                    ],
                    "correction": "Le façonnage manuel des bords pour créer un pli d'assemblage ou un relief s'appelle un relevé. La petite partie de tôle ainsi repliée est souvent nommée une pince. Ces éléments servent de jonction ou de barrière d'arrêt d'eau."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel défaut majeur apparaît si l'on applique l'alliage d'apport sur un zinc insuffisamment chauffé par le fer ?",
                    "answerOptions": [
                        {"text": "La soudure prend un aspect pâteux, irrégulier et n'accroche pas au métal", "isCorrect": True},
                        {"text": "Le zinc fond instantanément et crée un énorme trou dans la gouttière", "isCorrect": False},
                        {"text": "La panne en cuivre se soude définitivement à la surface de la toiture", "isCorrect": False},
                        {"text": "Le métal d'apport devient invisible car il est absorbé par la charpente", "isCorrect": False}
                    ],
                    "correction": "C'est le phénomène redouté de la soudure froide ou du collage. L'étain n'atteint pas son point de fluidité optimale, il se dépose en paquets superposés sans jamais fusionner chimiquement avec le zinc, provoquant invariablement une fuite lors de la première pluie."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le mode d'action d'une pince à rétreindre utilisée pour le façonnage des coudes de descentes d'eau pluviale ?",
                    "answerOptions": [
                        {"text": "Elle plisse l'extrémité du tube cylindrique pour réduire son diamètre et permettre un emboîtement mâle-femelle aisé", "isCorrect": True},
                        {"text": "Elle chauffe le métal à une température extrême en utilisant une résistance électrique intégrée dans les mors afin de fluidifier l'acier galvanisé et autoriser une soudure bord à bord sans aucun ajout de métal d'apport sur le chantier", "isCorrect": False},
                        {"text": "Elle étire fortement la matière vers l'extérieur pour augmenter la circonférence de la gouttière afin d'y insérer une bague d'étanchéité en caoutchouc vulcanisé capable de résister aux pluies diluviennes de type cyclonique", "isCorrect": False},
                        {"text": "Elle découpe de petites languettes triangulaires tout autour du tuyau profilé pour créer un système de griffes d'accroche qui se verrouilleront automatiquement à l'intérieur du mur porteur de l'édifice public", "isCorrect": False}
                    ],
                    "correction": "La pince à rétreindre (ou pince à plisser) sert à resserrer le bout d'un tuyau de descente ou d'un moignon. En y marquant de petits plis réguliers, elle diminue légèrement la circonférence de l'extrémité mâle, lui permettant de s'emboîter sans forcer dans la partie femelle du tuyau suivant."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel composant abrasif manuel est utilisé juste après le soudage pour nettoyer l'excédent de flux corrosif et faire briller le métal ?",
                    "answerOptions": [
                        {"text": "Éponge humide", "isCorrect": True},
                        {"text": "La brosse rotative en fils d'acier inoxydable montée sur une meuleuse pneumatique", "isCorrect": False},
                        {"text": "Le disque à lamelles de corindon conçu pour le meulage industriel des fortes épaisseurs", "isCorrect": False},
                        {"text": "La lime à métaux bâtarde rectangulaire à double taille croisée pour serrurier", "isCorrect": False}
                    ],
                    "correction": "Immédiatement après la prise de la soudure, le zingueur doit passer une éponge ou un chiffon humide sur le joint. Cette action stoppe net l'attaque chimique et dilue les résidus d'acide qui, dans le cas contraire, rongeraient le zinc et créeraient de graves taches d'oxydation blanche."
                },
                {
                    "questionNumber": 57,
                    "question": "Que doit-on vérifier visuellement pour s'assurer qu'une soudure par capillarité est réussie et parfaitement étanche ?",
                    "answerOptions": [
                        {"text": "La pénétration complète du cordon de soudure visible de l'autre côté de l'assemblage", "isCorrect": True},
                        {"text": "La présence de grosses gouttes d'étain figées sur le dessus de la plaque", "isCorrect": False},
                        {"text": "L'absence totale de décapant sur toute la zone de chevauchement des feuilles", "isCorrect": False},
                        {"text": "La coloration brun sombre de la toiture tout autour de la zone d'intervention", "isCorrect": False}
                    ],
                    "correction": "Une soudure à l'étain réussie doit filer entre les tôles. Le couvreur expérimenté vérifie la pénétration du joint : l'alliage doit avoir traversé l'intégralité du recouvrement et former un fin bourrelet continu et brillant sur la lisière intérieure de l'assemblage."
                },
                {
                    "questionNumber": 58,
                    "question": "Lors de la coupe d'une feuille de zinc à la cisaille manuelle, comment le zingueur évite-t-il la formation de bavures coupantes et de déchirures en fin de trait ?",
                    "answerOptions": [
                        {"text": "Il veille à ne jamais fermer totalement les mâchoires de la cisaille et fait glisser l'outil progressivement", "isCorrect": True},
                        {"text": "Il frappe très violemment les branches de la cisaille avec un maillet en bois massif afin de provoquer une onde de choc capable de cisailler la tôle instantanément sans produire la moindre friction sur les lames en acier forgé", "isCorrect": False},
                        {"text": "Il chauffe systématiquement la ligne de coupe au chalumeau pendant plusieurs minutes pour liquéfier la structure cristalline du zinc et trancher le panneau avec une facilité déconcertante équivalente à la découpe d'une plaque de beurre", "isCorrect": False},
                        {"text": "Il utilise obligatoirement un liquide de refroidissement pulvérisé à haute pression sur les couteaux de coupe pour empêcher toute élévation thermique responsable de l'apparition de bavures extrêmement tranchantes sur le chant du profilé", "isCorrect": False}
                    ],
                    "correction": "En cisaillant, le fait de refermer complètement les lames l'une sur l'autre pince et déchire le métal au point d'arrêt, créant ce qu'on appelle un bec de perroquet. Le geste professionnel correct consiste à arrêter sa coupe un peu avant la pointe, d'avancer l'outil, puis de reprendre la pression."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel métal d'apport est historiquement employé pour la brasure forte des tuyaux de descente en cuivre ?",
                    "answerOptions": [
                        {"text": "Un alliage de cuivre avec ajout de phosphore et parfois d'argent", "isCorrect": True},
                        {"text": "Un alliage pur composé de plomb et d'étain à cinquante pour cent", "isCorrect": False},
                        {"text": "Un fil d'acier doux recouvert de résine époxy thermodurcissable", "isCorrect": False},
                        {"text": "Une baguette de zinc allié au titane utilisée à très haute température", "isCorrect": False}
                    ],
                    "correction": "Si le cuivre peut se souder à l'étain (brasage tendre), le montage de conduites très sollicitées requiert souvent une brasure forte (réalisée à plus de six cents degrés). On emploie alors une baguette en alliage cuivre-phosphore ou cupro-argent, souvent sans nécessiter de flux décapant supplémentaire sur du cuivre pur."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle principal de l'étamage préalable des bords des tôles lorsqu'elles sont fortement oxydées ou très sales ?",
                    "answerOptions": [
                        {"text": "Déposer une fine couche d'alliage propre et adhérente sur chaque bord avant leur superposition pour garantir que la soudure finale filera parfaitement sans être bloquée par l'oxydation", "isCorrect": True},
                        {"text": "Augmenter artificiellement l'épaisseur des feuilles de métal pour qu'elles puissent supporter le poids cumulé des immenses masses de neige qui s'accumulent inévitablement sur les chéneaux encaissés lors des rigoureux hivers montagnards", "isCorrect": False},
                        {"text": "Isoler chimiquement le zinc de toute contamination par le plomb afin d'empêcher formellement le développement de maladies professionnelles respiratoires lors des opérations de brossage mécanique réalisées à l'intérieur de l'atelier de façonnage", "isCorrect": False},
                        {"text": "Créer un joint de dilatation thermique liquide qui absorbera la totalité des mouvements de contraction de la charpente en bois sans transmettre la moindre force de cisaillement aux agrafes de fixation cachées sous les tuiles plates", "isCorrect": False}
                    ],
                    "correction": "Sur un métal ancien très encrassé (comme lors de réparations sur de vieux chéneaux en plomb ou en zinc), la capillarité d'un seul coup échouera. Le couvreur étame d'abord séparément les deux pièces après un décapage abrasif intensif. Une fois les tôles propres et garnies d'étain superposées, la chaleur du fer fond ces couches pour créer l'étanchéité absolue."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : MISE EN ŒUVRE DES SYSTÈMES D'ÉVACUATION DES EAUX PLUVIALES (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : MISE EN ŒUVRE DES SYSTÈMES D'ÉVACUATION DES EAUX PLUVIALES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel élément permet de raccorder horizontalement la naissance d'une gouttière pendante à la descente verticale d'eau pluviale ?",
                    "answerOptions": [
                        {"text": "Coude", "isCorrect": True},
                        {"text": "Le système d'évacuation gravitaire souterrain équipé d'un siphon disconnecteur auto-nettoyant", "isCorrect": False},
                        {"text": "Le raccordement d'étanchéité souple polymérisé à chaud sur la ligne de faîtage principal", "isCorrect": False},
                        {"text": "La bague de jonction coulissante en acier galvanisé vissée directement dans la maçonnerie porteuse", "isCorrect": False}
                    ],
                    "correction": "Le coude permet de dévoyer la conduite d'eau pour franchir le débord de toit et relier la gouttière à la descente verticale fixée sur le mur. On utilise souvent un assemblage de deux coudes séparés par un moignon."
                },
                {
                    "questionNumber": 62,
                    "question": "Comment fixe-t-on traditionnellement une gouttière havraise sur un toit ?",
                    "answerOptions": [
                        {"text": "Sur le dessus des chevrons à l'aide de crochets pointes ou de crochets à agrafe", "isCorrect": True},
                        {"text": "En perçant directement le fond de la cuvette pour la visser dans les liteaux", "isCorrect": False},
                        {"text": "Avec des colliers de serrage métalliques suspendus aux linteaux de rive", "isCorrect": False},
                        {"text": "Par un système d'emboîtement à force sous la première rangée de tuiles", "isCorrect": False}
                    ],
                    "correction": "La gouttière havraise (ou rouennaise) est une gouttière rampante. Elle repose sur le terrasson ou les chevrons de la charpente par l'intermédiaire de crochets spécifiques posés avant la couverture."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle précaution indispensable le zingueur doit-il prendre lors du dimensionnement d'un chéneau encaissé entre deux murs ?",
                    "answerOptions": [
                        {"text": "Calculer la section d'évacuation en fonction de la surface en plan de la toiture et prévoir obligatoirement un trop-plein pour éviter le débordement à l'intérieur du bâtiment en cas d'obstruction de la naissance", "isCorrect": True},
                        {"text": "Enduire systématiquement toute la surface intérieure du métal avec une épaisse couche de goudron bitumineux chauffé à blanc afin de garantir une imperméabilité totale même si les soudures transversales finissent par céder sous le poids exceptionnel des accumulations de neige hivernale et des feuilles mortes", "isCorrect": False},
                        {"text": "Remplacer les joints de dilatation en néoprène par des plaques d'acier rigides soudées à l'arc pour augmenter la solidité structurelle de l'ensemble face aux rafales de vent", "isCorrect": False},
                        {"text": "Incliner le fond du chéneau avec une pente minimale de dix centimètres par mètre pour garantir une évacuation supersonique de l'eau", "isCorrect": False}
                    ],
                    "correction": "Un chéneau encaissé qui déborde (à cause de feuilles ou de très fortes précipitations) inonde directement l'intérieur du bâtiment. Un orifice de trop-plein est strictement exigé par le DTU pour déverser l'eau vers l'extérieur en cas de saturation de la descente."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel élément en néoprène inséré entre deux feuilles de zinc permet d'absorber les variations dimensionnelles d'un chéneau ?",
                    "answerOptions": [
                        {"text": "Main", "isCorrect": True},
                        {"text": "La plaque de renforcement structurel en acier trempé fixée sur l'ourlet extérieur", "isCorrect": False},
                        {"text": "Le ruban d'étanchéité bitumineux autoadhésif posé sous les crochets de gouttière", "isCorrect": False},
                        {"text": "Le solin de raccordement maçonné permettant l'isolation thermique du conduit", "isCorrect": False}
                    ],
                    "correction": "La main de dilatation (ou joint de dilatation) est une bande élastomère vulcanisée bordée de deux bandes de zinc ou de cuivre. Elle s'étire et se comprime pour absorber l'allongement et la rétractation thermique du long chéneau."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la fonction d'une naissance dans un système d'évacuation des eaux pluviales ?",
                    "answerOptions": [
                        {"text": "Assurer la liaison étanche entre la gouttière horizontale et le tuyau de descente", "isCorrect": True},
                        {"text": "Bloquer les feuilles mortes avant qu'elles n'atteignent le réseau souterrain", "isCorrect": False},
                        {"text": "Accélérer le débit de l'eau grâce à un profilage aérodynamique spécifique", "isCorrect": False},
                        {"text": "Soutenir le poids du chéneau en son centre pour éviter l'affaissement", "isCorrect": False}
                    ],
                    "correction": "La naissance (ou moignon) est la pièce tronconique soudée au fond de la gouttière qui collecte l'eau pour la canaliser et la diriger vers le coude ou le tuyau de descente."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment réalise-t-on le tracé de la pente d'une gouttière pendante avant la pose des crochets ?",
                    "answerOptions": [
                        {"text": "En tendant un cordeau au cordex entre le crochet de point haut et le crochet de point bas", "isCorrect": True},
                        {"text": "En utilisant un niveau laser rotatif aligné sur le faîtage de la toiture", "isCorrect": False},
                        {"text": "En mesurant la distance au sol et en appliquant un angle de quarante-cinq degrés", "isCorrect": False},
                        {"text": "En se basant sur le parallélisme parfait avec la ligne de rive du bâtiment", "isCorrect": False}
                    ],
                    "correction": "Le zingueur fixe le crochet le plus haut, puis le crochet le plus bas près de la naissance en appliquant la pente requise de cinq millimètres par mètre. Un cordeau tendu entre ces deux points sert de guide d'alignement pour plier et fixer tous les crochets intermédiaires."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est l'avantage technique de la gouttière nantaise par rapport à la gouttière demi-ronde pendante ?",
                    "answerOptions": [
                        {"text": "Elle s'intègre discrètement sur la ligne d'égout en reposant directement sur les chevrons et limite les risques d'arrachement par la neige", "isCorrect": True},
                        {"text": "Elle est conçue à partir d'un alliage de titane et de magnésium qui lui confère une capacité d'expansion thermique pratiquement illimitée ce qui permet au couvreur de poser des longueurs ininterrompues de plus de cinquante mètres sans jamais devoir installer le moindre joint de dilatation ou talon d'expansion en néoprène", "isCorrect": False},
                        {"text": "Son profil asymétrique très profond crée un puissant phénomène de siphonnage capable d'aspirer les amas de feuilles mortes vers la descente", "isCorrect": False},
                        {"text": "Elle se fixe directement sur la maçonnerie verticale de la façade sans nécessiter le moindre support en bois", "isCorrect": False}
                    ],
                    "correction": "La gouttière nantaise est une gouttière rampante avec un relevé à ourlet. Posée sur une bande de doublis, elle ne dépasse pas de la toiture. Elle est donc très esthétique, et sa position la protège de l'arrachement lors des glissements de neige."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle pièce métallique ferme hermétiquement les extrémités d'une gouttière demi-ronde ?",
                    "answerOptions": [
                        {"text": "Talon", "isCorrect": True},
                        {"text": "La bague d'arrêt hydraulique avec joint polymère expansif intégré", "isCorrect": False},
                        {"text": "Le déflecteur aérodynamique vissé sur la sous-face de la toiture", "isCorrect": False},
                        {"text": "La patte de fixation coulissante en acier inoxydable forgé", "isCorrect": False}
                    ],
                    "correction": "Le talon (ou fond de gouttière) est une petite pièce de métal découpée et emboutie, soudée à chaque extrémité de la gouttière ou du chéneau pour retenir l'eau et assurer la fermeture étanche du profilé."
                },
                {
                    "questionNumber": 69,
                    "question": "À quelle distance maximale doit-on espacer les crochets d'une gouttière pendante en zinc ?",
                    "answerOptions": [
                        {"text": "Tous les quarante à cinquante centimètres selon les régions et la charge climatique", "isCorrect": True},
                        {"text": "Tous les mètres pour des raisons d'économie de matériaux et de temps", "isCorrect": False},
                        {"text": "Uniquement aux deux extrémités et au centre de chaque profilé métallique", "isCorrect": False},
                        {"text": "Tous les dix centimètres pour garantir une rigidité absolue de l'ouvrage", "isCorrect": False}
                    ],
                    "correction": "Le DTU de couverture recommande un entraxe de pose des crochets compris entre 40 et 50 cm. Cela évite l'affaissement (fluage) de la gouttière métallique sous le poids de l'eau, de la neige ou de la glace en hiver."
                },
                {
                    "questionNumber": 70,
                    "question": "Que se passe-t-il si un couvreur omet d'installer un joint de dilatation sur un chéneau encaissé de plus de quinze mètres de long ?",
                    "answerOptions": [
                        {"text": "L'allongement et la rétraction répétés du zinc provoqueront inévitablement une fatigue mécanique qui déchirera les soudures et créera des fuites majeures", "isCorrect": True},
                        {"text": "Le chéneau va progressivement modifier son inclinaison sous le poids de l'eau stagnante et finir par inverser totalement sa pente naturelle, renvoyant ainsi l'intégralité des précipitations pluviales vers la cheminée d'évacuation des fumées située de l'autre côté du bâtiment", "isCorrect": False},
                        {"text": "La tôle va se rigidifier sous l'effet du soleil estival et se transformer en un alliage cassant qui explosera au premier choc thermique hivernal", "isCorrect": False},
                        {"text": "L'eau de pluie ne pourra plus s'évacuer correctement car les frottements hydrauliques seront décuplés par la longueur continue de l'installation", "isCorrect": False}
                    ],
                    "correction": "Les règles de l'art exigent la pose d'une main de dilatation ou d'un ressaut tous les 15 mètres maximum pour les développés classiques, et tous les 8 mètres pour les chéneaux de grand développement, sous peine de déchirure de la matière par dilatation thermique."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est l'inclinaison classique d'un coude préfabriqué pour raccorder une gouttière à sa descente ?",
                    "answerOptions": [
                        {"text": "Soixante-douze degrés ou quatre-vingt-cinq degrés selon la configuration du débord de toit", "isCorrect": True},
                        {"text": "Strictement quarante-cinq degrés sur toutes les façades modernes", "isCorrect": False},
                        {"text": "Toujours quatre-vingt-dix degrés pour un écoulement à angle droit", "isCorrect": False},
                        {"text": "Dix degrés pour freiner considérablement la vitesse de l'eau", "isCorrect": False}
                    ],
                    "correction": "Les coudes de tuyaux de descente sont couramment fabriqués avec des angles de 72 degrés ou 85 degrés. On parle en atelier de coudes au quart ou de coudes d'équerre courbés, ce qui assure un bon transfert hydraulique tout en franchissant la corniche."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel élément en métal sert à maintenir le tuyau de descente contre le mur de façade ?",
                    "answerOptions": [
                        {"text": "Collier", "isCorrect": True},
                        {"text": "La console de maintien tridimensionnelle fixée par chevillage chimique lourd", "isCorrect": False},
                        {"text": "Le support de charge vibratoire posé directement sur la ligne de fondation", "isCorrect": False},
                        {"text": "La sangle textile à cliquet autobloquante arrimée aux fenêtres supérieures", "isCorrect": False}
                    ],
                    "correction": "Le collier de descente est muni d'une patte à vis scellée ou chevillée dans la maçonnerie. Il encercle et maintient fermement le tuyau d'eau pluviale à la verticale contre le mur."
                },
                {
                    "questionNumber": 73,
                    "question": "Comment assemble-t-on traditionnellement deux tuyaux de descente en zinc ?",
                    "answerOptions": [
                        {"text": "Par simple emboîtement sur environ cinq centimètres en respectant le sens de l'écoulement", "isCorrect": True},
                        {"text": "Par soudure continue à l'étain sur toute la périphérie pour empêcher tout déboîtement", "isCorrect": False},
                        {"text": "En les collant avec une cartouche de mastic polyuréthane haute densité", "isCorrect": False},
                        {"text": "À l'aide de brides métalliques boulonnées équipées de joints toriques", "isCorrect": False}
                    ],
                    "correction": "Les tuyaux de descente ne sont presque jamais soudés entre eux. L'extrémité supérieure (femelle) reçoit la partie inférieure (mâle) légèrement rétrécie à la pince. Cet emboîtement libre facilite le démontage et autorise la dilatation thermique."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle précaution doit être prise lors de la soudure d'une naissance tronconique sur le fond d'une gouttière pendante ?",
                    "answerOptions": [
                        {"text": "Réaliser l'orifice dans la gouttière, rabattre une petite pince vers le bas pour guider l'eau, puis souder la naissance par capillarité", "isCorrect": True},
                        {"text": "Découper un orifice deux fois plus grand que le diamètre de la naissance puis combler le vide avec d'énormes quantités d'alliage étain-plomb fondu en plusieurs couches successives afin de garantir une masse métallique capable de résister aux chocs des pierres qui pourraient tomber du toit", "isCorrect": False},
                        {"text": "Placer la gouttière à l'envers sur l'établi et souder la naissance par l'extérieur en utilisant un chalumeau à très haute température pour fusionner directement le zinc avec le cuivre", "isCorrect": False},
                        {"text": "Utiliser exclusivement des rivets aveugles pour assembler les deux pièces afin de ne pas brûler la pellicule esthétique de la tôle", "isCorrect": False}
                    ],
                    "correction": "L'orifice appelé trou de moignon doit être soigneusement découpé, et ses bords légèrement rabattus au marteau vers l'intérieur de la naissance. Cela accompagne le flux de l'eau, évite les rétentions liquides et prépare un support plat pour la soudure à l'étain."
                },
                {
                    "questionNumber": 75,
                    "question": "Sur un toit à très fort développement, pourquoi installe-t-on parfois une cuvette de branchement ou boîte à eau ?",
                    "answerOptions": [
                        {"text": "Pour collecter un grand volume d'eau provenant de plusieurs pans avant de l'envoyer dans la descente", "isCorrect": True},
                        {"text": "Pour stocker l'eau de pluie destinée au nettoyage ultérieur de la façade", "isCorrect": False},
                        {"text": "Pour ralentir la chute de l'eau et éviter l'érosion du trottoir public", "isCorrect": False},
                        {"text": "Pour loger un filtre chimique purifiant l'eau avant son rejet au tout-à-l'égout", "isCorrect": False}
                    ],
                    "correction": "La boîte à eau est un réceptacle placé en tête de descente de façade. Elle centralise les eaux de chéneaux ou de toitures-terrasses à fond plat, évite les engorgements et joue très souvent le rôle de trop-plein de sécurité."
                },
                {
                    "questionNumber": 76,
                    "question": "Que signifie le terme de développement lorsqu'on parle d'une gouttière demi-ronde de vingt-cinq ?",
                    "answerOptions": [
                        {"text": "La largeur de la tôle plane utilisée pour la fabriquer est de vingt-cinq centimètres", "isCorrect": True},
                        {"text": "Son diamètre intérieur utile permet un débit de vingt-cinq litres par minute", "isCorrect": False},
                        {"text": "Elle doit être soutenue par un crochet tous les vingt-cinq centimètres", "isCorrect": False},
                        {"text": "Sa longueur commerciale standardisée est de deux mètres cinquante", "isCorrect": False}
                    ],
                    "correction": "Le développement d'une gouttière (couramment 25 ou 33) désigne la largeur en centimètres de la bande de zinc déroulée avant son passage en profileuse pour lui donner sa forme demi-ronde et rouler son ourlet."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est l'importance de positionner correctement la ligne d'égout du toit par rapport à la gouttière pendante ?",
                    "answerOptions": [
                        {"text": "La tuile ou l'ardoise doit surplomber le premier tiers de la gouttière pour que l'eau s'y déverse sans passer par-dessus l'ourlet extérieur", "isCorrect": True},
                        {"text": "Le bord de la couverture doit dépasser complètement la largeur de la gouttière et s'étendre dans le vide afin de créer un effet de cascade naturelle qui éloignera l'humidité des murs porteurs lors des tempêtes cycloniques soufflant à plus de cent cinquante kilomètres par heure", "isCorrect": False},
                        {"text": "Le larmier de la couverture doit être collé fermement contre le fond de la gouttière avec un mastic bitumineux", "isCorrect": False},
                        {"text": "Il faut ménager un espace vertical d'au moins trente centimètres entre la tuile et le chéneau pour faciliter l'inspection visuelle", "isCorrect": False}
                    ],
                    "correction": "Si le débord de toit est trop court, l'eau ruisselle derrière la gouttière et dégrade la façade. S'il est trop long, lors de fortes pluies la trajectoire parabolique de l'eau passe au-delà de l'ourlet extérieur. Le surplomb idéal se situe au niveau du premier tiers arrière de la cuvette."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel dispositif empêche l'engorgement des descentes par l'accumulation de feuilles mortes ?",
                    "answerOptions": [
                        {"text": "Une crapaudine ou grille pare-feuilles placée dans la naissance", "isCorrect": True},
                        {"text": "Un siphon disconnecteur installé au milieu du tuyau de descente", "isCorrect": False},
                        {"text": "Une valve anti-retour fixée au niveau du coude supérieur", "isCorrect": False},
                        {"text": "Un chauffage électrique permanent monté le long de l'ourlet", "isCorrect": False}
                    ],
                    "correction": "La crapaudine est un élément en fil de fer galvanisé, en zinc ou en cuivre en forme de dôme. Elle est simplement glissée ou sertie dans l'orifice du moignon pour arrêter les débris solides tout en laissant s'écouler l'eau pluviale."
                },
                {
                    "questionNumber": 79,
                    "question": "Lors de la pose d'un chéneau encaissé avec fondation en bois, quelle précaution faut-il prendre concernant le support ?",
                    "answerOptions": [
                        {"text": "Installer une fonçure en voliges jointives sans désaffleurement pour éviter que la feuille de zinc ne se déchire sous le poids de l'ouvrier ou de la neige", "isCorrect": True},
                        {"text": "Disposer les planches de voligeage de manière très espacée avec un vide d'au moins dix centimètres entre chaque lame afin de créer une ventilation dynamique extrême qui assèchera immédiatement les condensations internes engendrées par les chocs thermiques brutaux du mois de janvier", "isCorrect": False},
                        {"text": "Remplacer systématiquement le bois par une dalle de ciment coulée en place pour apporter une rigidité maximale et inaltérable", "isCorrect": False},
                        {"text": "Recouvrir le bois brut d'une épaisse couche de peinture acrylique pour modifier son coefficient de dilatation naturelle", "isCorrect": False}
                    ],
                    "correction": "Le zinc laminé est très fin et flue sous la contrainte. Le support en bois massif appelé fonçure doit être continu, plan et parfaitement jointif pour offrir un appui mécanique total à la tôle lors de sa mise en charge (eau, neige, ou le simple pas du zingueur lors de l'entretien)."
                },
                {
                    "questionNumber": 80,
                    "question": "Que nomme-t-on le relevé sur une gouttière nantaise ou un chéneau ?",
                    "answerOptions": [
                        {"text": "La partie verticale de la tôle située du côté du mur ou du rampant", "isCorrect": True},
                        {"text": "La soudure de finition réalisée sur le bord extérieur de l'ouvrage", "isCorrect": False},
                        {"text": "L'inclinaison appliquée à l'ensemble du profilé pour la pente", "isCorrect": False},
                        {"text": "L'outil utilisé pour écarter les tuiles surplombant la cuvette", "isCorrect": False}
                    ],
                    "correction": "Le relevé (ou dosseret) est la partie de la feuille métallique pliée verticalement. Cette zone remonte le long du mur ou sous les éléments de couverture pour empêcher tout débordement par l'arrière de l'installation."
                }
            ]
        },
# =========================================================================
        # THÈME 5 : COUVERTURES MÉTALLIQUES ET RACCORDEMENTS D'ÉTANCHÉITÉ (ABERGEMENTS) (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : COUVERTURES MÉTALLIQUES ET RACCORDEMENTS D'ÉTANCHÉITÉ (ABERGEMENTS)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel système de couverture traditionnelle en zinc utilise des profils en bois de forme trapézoïdale pour séparer les bacs métalliques ?",
                    "answerOptions": [
                        {"text": "À tasseaux", "isCorrect": True},
                        {"text": "Le système d'emboîtement autoportant sans support continu nécessitant des charpentes métalliques renforcées", "isCorrect": False},
                        {"text": "La technique d'étanchéité par membrane bitumineuse soudée au chalumeau sur écran pare-vapeur", "isCorrect": False},
                        {"text": "Le bardage rapporté à double peau ventilée avec isolation thermique intégrée par l'extérieur", "isCorrect": False}
                    ],
                    "correction": "La couverture à tasseaux est la méthode traditionnelle parisienne. Des tasseaux en bois séparent les bacs de zinc, et l'étanchéité supérieure est assurée par un couvre-joint métallique cloué puis agrafé sur les côtés."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la fonction principale d'une patte de fixation coulissante sur une toiture en zinc à joint debout ?",
                    "answerOptions": [
                        {"text": "Maintenir le bac contre le vent tout en autorisant sa libre dilatation thermique", "isCorrect": True},
                        {"text": "Assurer la liaison électrique de mise à la terre entre les différents profilés", "isCorrect": False},
                        {"text": "Renforcer l'isolation acoustique de la charpente contre les bruits d'impact", "isCorrect": False},
                        {"text": "Bloquer définitivement la feuille de métal pour empêcher tout glissement", "isCorrect": False}
                    ],
                    "correction": "Les pattes coulissantes, composées d'une embase fixe pointée sur la volige et d'une partie mobile sertie dans l'agrafure, retiennent la feuille contre la dépression du vent tout en accompagnant son retrait et son allongement thermique inévitables."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel élément d'abergement se place spécifiquement sur la face avant d'une souche de cheminée, côté égout ?",
                    "answerOptions": [
                        {"text": "Le devant de souche", "isCorrect": True},
                        {"text": "La besace de faîtage", "isCorrect": False},
                        {"text": "Le couloir latéral", "isCorrect": False},
                        {"text": "Le noquet de rive", "isCorrect": False}
                    ],
                    "correction": "L'abergement d'une pénétration continue comprend plusieurs éléments étanches : le devant de souche (côté bas vers l'égout), les couloirs latéraux (sur les côtés pour diriger l'eau) et la besace ou l'arrière de souche (côté haut vers le faîtage) pour dévier l'eau."
                },
                {
                    "questionNumber": 84,
                    "question": "Pourquoi le DTU exige-t-il la présence d'une lame d'air ventilée en sous-face d'une couverture en zinc posée sur un voligeage massif ?",
                    "answerOptions": [
                        {"text": "Pour évacuer la vapeur d'eau provenant de l'intérieur du bâtiment et empêcher la formation de condensation destructrice sous la tôle", "isCorrect": True},
                        {"text": "Pour créer un matelas d'air sous pression constante capable de soulever très légèrement les bacs de zinc afin d'amortir les ondes de choc provoquées par les chutes de grêlons massifs lors des orages estivaux violents et récurrents", "isCorrect": False},
                        {"text": "Pour permettre le passage aisé des gaines électriques et des tuyauteries de fluides frigorigènes du système de climatisation centralisé sans devoir percer les chevrons porteurs de la structure primaire en bois lamellé-collé", "isCorrect": False},
                        {"text": "Pour générer une isolation phonique absolue par effet de vide partiel qui neutralise la transmission des fréquences acoustiques aiguës vers les pièces habitées situées directement sous l'arêtier ou le faîtage principal de l'édifice", "isCorrect": False}
                    ],
                    "correction": "La ventilation de la sous-face du zinc est une obligation absolue en couverture froide. Elle élimine l'humidité, évitant ainsi la corrosion par piqûre (rouille blanche) sous le métal et le pourrissement du support en bois."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle est la fonction d'une besace installée à l'arrière d'une souche de cheminée très large ?",
                    "answerOptions": [
                        {"text": "Dévier l'eau de pluie de part et d'autre de l'obstacle vers les couloirs latéraux", "isCorrect": True},
                        {"text": "Renforcer la structure maçonnée de la cheminée contre les rafales de vent", "isCorrect": False},
                        {"text": "Capter les suies et les cendres volatiles pour éviter de tacher la toiture", "isCorrect": False},
                        {"text": "Soutenir le poids de la couverture en amont pour éviter l'affaissement", "isCorrect": False}
                    ],
                    "correction": "La besace est un ouvrage de zinguerie en forme de pyramide ou de double pente, placé à l'arrière d'une pénétration large, servant à fendre le flux d'eau descendant du faîtage et à l'orienter proprement vers les couloirs d'évacuation latéraux."
                },
                {
                    "questionNumber": 86,
                    "question": "Comment nomme-t-on la liaison longitudinale étanche réalisée par pliage et sertissage des bords relevés de deux bacs adjacents ?",
                    "answerOptions": [
                        {"text": "Agrafure", "isCorrect": True},
                        {"text": "La vulcanisation à froid par application d'une résine élastomère de synthèse", "isCorrect": False},
                        {"text": "Le cordon de soudure autogène exécuté sous atmosphère inerte de protection", "isCorrect": False},
                        {"text": "Le recouvrement par emboîtement élastique sans aucune déformation mécanique", "isCorrect": False}
                    ],
                    "correction": "L'agrafure (simple ou double) est le nom technique donné au sertissage des pinces. Sur une couverture à joint debout, on réalise une agrafure double pour garantir une étanchéité par emboîtement capillaire très résistant aux intempéries."
                },
                {
                    "questionNumber": 87,
                    "question": "Sur un bac en zinc à joint debout, où positionne-t-on généralement la zone de pattes fixes sur un rampant de longueur moyenne ?",
                    "answerOptions": [
                        {"text": "Dans la partie haute du bac près du faîtage", "isCorrect": True},
                        {"text": "Exclusivement au niveau de la ligne d'égout", "isCorrect": False},
                        {"text": "Strictement au milieu géométrique de la tôle", "isCorrect": False},
                        {"text": "Sur toute la longueur de la rive latérale", "isCorrect": False}
                    ],
                    "correction": "Sur des rampants classiques, la zone d'ancrage (composée de pattes fixes) se situe en partie haute du bac. Le panneau métallique y est suspendu, et sa dilatation s'effectue librement vers le bas de la pente grâce aux pattes coulissantes intermédiaires."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle caractéristique distingue le système à joint debout à double sertissage du simple sertissage sur une couverture en zinc ?",
                    "answerOptions": [
                        {"text": "Le double sertissage replie la pince deux fois sur elle-même pour assurer une étanchéité totale même avec des pentes très faibles", "isCorrect": True},
                        {"text": "Le système à double sertissage requiert l'injection systématique d'une mousse polyuréthane expansive à l'intérieur du pli métallique afin de combler les espaces vides laissés par l'outil de profilage et empêcher les insectes de s'introduire dans les combles", "isCorrect": False},
                        {"text": "Le simple sertissage est autorisé uniquement pour les toitures plates sans aucune pente alors que le double sertissage est obligatoire dès que l'inclinaison dépasse les soixante degrés pour contrecarrer la force d'attraction terrestre extrême", "isCorrect": False},
                        {"text": "Le profil à double sertissage nécessite l'emploi d'une tôle d'acier inoxydable de forte épaisseur recouverte de plomb laminé car le zinc pur se déchirerait instantanément lors de la deuxième passe de la pince manuelle de fermeture", "isCorrect": False}
                    ],
                    "correction": "Le joint debout à double sertissage (fermeture de l'agrafe simple puis rabattage complet) crée une barrière étanche redoutable contre les remontées d'eau poussées par le vent, autorisant son emploi technique sur des rampants à très faible pente (dès 5 %)."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel profilé métallique assure l'étanchéité supérieure d'un abergement contre un mur vertical maçonné ?",
                    "answerOptions": [
                        {"text": "La bande de solin", "isCorrect": True},
                        {"text": "Le larmier d'égout", "isCorrect": False},
                        {"text": "La main de dilatation", "isCorrect": False},
                        {"text": "La chatière de ventilation", "isCorrect": False}
                    ],
                    "correction": "La bande de solin est un profilé rapporté qui se fixe sur la paroi verticale pour recouvrir le bord supérieur du relevé du couloir ou de la bavette. Souvent munie d'un joint mastic en partie haute, elle empêche l'eau de façade de ruisseler derrière l'ouvrage de zinguerie."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est l'utilité des chatières disposées en quinconce sur les différents pans d'une toiture métallique ?",
                    "answerOptions": [
                        {"text": "Créer une circulation d'air naturelle pour ventiler la sous-face de la couverture", "isCorrect": True},
                        {"text": "Fournir un accès sécurisé pour le passage des cordes d'assurance des couvreurs", "isCorrect": False},
                        {"text": "Collecter les eaux de ruissellement pour alimenter les chéneaux de rive", "isCorrect": False},
                        {"text": "Éviter la nidification des oiseaux dans l'espace vide sous les tuiles faîtières", "isCorrect": False}
                    ],
                    "correction": "Les chatières sont de petites ouïes grillagées implantées sur la couverture. Disposées stratégiquement en partie basse (entrée d'air) et en partie haute (sortie d'air), elles assurent le tirage thermique indispensable à l'assèchement continu de la lame d'air sous le voligeage."
                },
                {
                    "questionNumber": 91,
                    "question": "Comment désigne-t-on la ligne d'intersection rentrante formée par la rencontre de deux versants de toiture ?",
                    "answerOptions": [
                        {"text": "La noue", "isCorrect": True},
                        {"text": "Le faîtage principal en zinc prépatiné renforcé par des tasseaux bois", "isCorrect": False},
                        {"text": "L'arêtier droit débordant avec recouvrement continu soudé à l'étain", "isCorrect": False},
                        {"text": "L'égout encaissé revêtu d'une membrane bitumineuse sablée épaisse", "isCorrect": False}
                    ],
                    "correction": "La noue est l'angle rentrant qui collecte et canalise les eaux de ruissellement des deux pans adjacents. C'est un ouvrage critique qui exige un profilage profond, un agrafage étanche et des jeux de dilatation adaptés pour prévenir tout risque de débordement sous toiture."
                },
                {
                    "questionNumber": 92,
                    "question": "Pourquoi les raccordements soudés d'un abergement de cheminée requièrent-ils une attention particulière concernant le jeu de dilatation ?",
                    "answerOptions": [
                        {"text": "L'abergement doit être composé d'éléments indépendants soudés par tronçons pour absorber les mouvements du toit sans déchirer les coutures", "isCorrect": True},
                        {"text": "La maçonnerie de la cheminée émettant une chaleur constante extrême en hiver provoque une fusion lente mais irréversible des soudures à l'étain si celles-ci ne sont pas protégées par un écran thermique isolant en fibres d'aramide ignifugées épaisses de plusieurs centimètres", "isCorrect": False},
                        {"text": "Le zinc laminé soudé en un seul bloc continu va inévitablement s'incruster dans les joints de mortier du mur en briques sous l'effet de l'humidité stagnante ce qui provoquera la fracturation de la souche maçonnée entière au bout de quelques saisons", "isCorrect": False},
                        {"text": "Le couvreur doit impérativement utiliser une brasure forte au cuivre et à l'argent sur l'ensemble du pourtour de la cheminée car une soudure tendre à l'étain-plomb ne résisterait jamais à la pression atmosphérique négative générée par l'extraction des fumées de combustion", "isCorrect": False}
                    ],
                    "correction": "Un abergement ceinture un obstacle rigide. S'il est soudé de manière totalement monobloc avec les longs bacs de toiture, la dilatation de ces derniers arrachera les soudures d'angle. Il faut intégrer des liaisons par agrafes coulissantes pour le désolidariser des contraintes thermiques de la charpente."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel élément métallique vient coiffer le tasseau de bois pour finaliser l'étanchéité entre deux feuilles de zinc ?",
                    "answerOptions": [
                        {"text": "Le couvre-joint", "isCorrect": True},
                        {"text": "La patte de fixation", "isCorrect": False},
                        {"text": "La volige de rive", "isCorrect": False},
                        {"text": "Le profilé d'égout", "isCorrect": False}
                    ],
                    "correction": "Dans la technique de couverture à tasseaux, le couvre-joint est une baguette de zinc façonnée en U qui coiffe le profil en bois et recouvre les bords relevés des feuilles de métal adjacentes. Il est maintenu par les pattes à tasseau clouées."
                },
                {
                    "questionNumber": 94,
                    "question": "Qu'est-ce qu'une patte à loup dans le domaine du façonnage du zinc ?",
                    "answerOptions": [
                        {"text": "Une découpe spécifique avec languette pour rabattre et souder un angle fermé", "isCorrect": True},
                        {"text": "Un outil pneumatique servant à écraser les agrafures de forte épaisseur", "isCorrect": False},
                        {"text": "Un défaut d'aspect apparaissant suite à une surchauffe au chalumeau", "isCorrect": False},
                        {"text": "Un type d'échafaudage en encorbellement posé sur la corniche", "isCorrect": False}
                    ],
                    "correction": "Lors de la création d'angles fermés et de relevés d'étanchéité, le zingueur découpe une \"patte à loup\" ou patte d'oie : une petite languette de tôle rabattue derrière le relevé adjacent. Elle sert de renfort de recouvrement, garantissant un assemblage d'angle solide et étanche après la soudure capillaire."
                },
                {
                    "questionNumber": 95,
                    "question": "Sur une couverture métallique à très faible pente, pourquoi le zingueur doit-il insérer une bande d'interposition anti-capillaire dans les agrafures ?",
                    "answerOptions": [
                        {"text": "Pour rompre le phénomène physique d'aspiration capillaire et bloquer toute infiltration d'eau qui remonterait sous le pli", "isCorrect": True},
                        {"text": "Pour apporter une coloration chimique temporaire à la tôle lors de sa mise en forme afin que l'artisan puisse repérer immédiatement les défauts de planéité causés par les impacts de son maillet en bois massif pendant la phase délicate du sertissage manuel sur la volige", "isCorrect": False},
                        {"text": "Pour isoler le système de toiture des puissants rayonnements électromagnétiques émis par les antennes de téléphonie mobile qui provoquent une accélération phénoménale de la corrosion perforante du zinc par électrolyse au contact des eaux pluviales très acides", "isCorrect": False},
                        {"text": "Pour augmenter considérablement l'épaisseur de l'assemblage et obliger la pince à sertir à développer une force d'écrasement hydraulique deux fois plus importante garantissant un blocage mécanique absolu contre le glissement gravitationnel", "isCorrect": False}
                    ],
                    "correction": "Lorsque la pente est très faible, l'eau d'écoulement stagne et risque de remonter à travers l'agrafure du joint debout par tension superficielle. Le DTU impose d'y insérer une tresse de butyl, un mastic ou un feuillard spécifique lors du sertissage pour créer une véritable barrière anti-capillaire."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel matériau composite moderne sur rouleau plissé est de plus en plus utilisé par les zingueurs pour remplacer le plomb traditionnel dans les abergements ?",
                    "answerOptions": [
                        {"text": "Bande bitumineuse", "isCorrect": True},
                        {"text": "Le polyéthylène haute densité chargé de particules de verre ignifugé", "isCorrect": False},
                        {"text": "La résine époxy bicomposante coulée directement sur un treillis d'acier", "isCorrect": False},
                        {"text": "Le cuivre pur recuit dans un bain d'acide sulfurique concentré", "isCorrect": False}
                    ],
                    "correction": "Pour des raisons sanitaires, environnementales et de poids, les bandes de solin ou de raccordement adhésives plissées (composées de butyle, d'aluminium profilé ou de polyisobutylène type Wakaflex) remplacent très souvent le plomb laminé pour maroufler et épouser les galbes des tuiles."
                },
                {
                    "questionNumber": 97,
                    "question": "Pourquoi façonne-t-on un ourlet cylindrique sur le bord libre d'un larmier ou d'une bande d'égout ?",
                    "answerOptions": [
                        {"text": "Pour rigidifier le bord de la tôle et éloigner la goutte d'eau de la façade", "isCorrect": True},
                        {"text": "Pour permettre le passage d'un câble électrique de chauffage antigel", "isCorrect": False},
                        {"text": "Pour créer une zone de dilatation concentrée au bas de la toiture", "isCorrect": False},
                        {"text": "Pour faciliter l'emboîtement des tuiles ou des ardoises de doublis", "isCorrect": False}
                    ],
                    "correction": "L'ourlet (fermé ou ouvert) augmente l'inertie mécanique du bord de la tôle face au vent. De plus, sa forme cylindrique agit comme un casse-goutte, forçant la goutte d'eau à tomber verticalement par gravité plutôt que de glisser par tension de surface sous la bande métallique vers la façade."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le rôle d'un gousset soudé sur le relevé d'une bande de noue métallique ?",
                    "answerOptions": [
                        {"text": "Obstruer l'extrémité supérieure du relevé pour empêcher l'eau de s'infiltrer sous la toiture lors des fortes rafales de vent", "isCorrect": True},
                        {"text": "Accélérer le refroidissement de la soudure à l'étain en créant un pont thermique dissipateur qui transfère instantanément la chaleur résiduelle du fer vers la volige en sapin située directement sous le plancher de la toiture", "isCorrect": False},
                        {"text": "Servir de repère tridimensionnel fixe pour le montage ultérieur des échafaudages suspendus en encorbellement lors des travaux de restauration complète de la charpente et de la maçonnerie des conduits d'évacuation des fumées", "isCorrect": False},
                        {"text": "Créer une décoration ornementale en pointe de diamant imposée par le cahier des charges des architectes des bâtiments de France pour toutes les toitures en zinc des édifices classés aux monuments historiques dans un périmètre sauvegardé", "isCorrect": False}
                    ],
                    "correction": "Un gousset est une petite pièce de tôle ajoutée et soudée pour fermer hermétiquement une ouverture ou un angle créé par un pliage complexe (comme en tête de noue ou au fond d'une besace). Il garantit que l'eau refoulée par le vent ou la neige accumulée ne pénètre pas par cette anfractuosité."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment le zingueur vérifie-t-il qu'un abergement périphérique est soudé sans créer de tension mécanique destructrice ?",
                    "answerOptions": [
                        {"text": "Le raccordement soudé ne doit pas bloquer la libre dilatation du couloir le long de l'obstacle", "isCorrect": True},
                        {"text": "La tôle doit être parfaitement gondolée pour prouver son extension", "isCorrect": False},
                        {"text": "Les rivets en aluminium doivent tous avoir leur tige cassée à ras", "isCorrect": False},
                        {"text": "L'apport d'étain doit former une pyramide d'au moins dix centimètres", "isCorrect": False}
                    ],
                    "correction": "Un abergement est solidaire de la maçonnerie qui est fixe. Si les soudures d'angle lient les couloirs aux bacs de rampant d'une manière rigide, l'ensemble se déchirera lors des variations thermiques. Le façonnage doit inclure des pinces d'agrafage permettant le glissement longitudinal."
                },
                {
                    "questionNumber": 100,
                    "question": "Sur une couverture à tasseaux de très grand développement, quelle technique permet de gérer la forte dilatation longitudinale des bacs sans recourir à des joints en néoprène ?",
                    "answerOptions": [
                        {"text": "Installer un ressaut profilé créant une marche en escalier qui fragmente la couverture en plusieurs bacs indépendants", "isCorrect": True},
                        {"text": "Déposer d'épaisses plaques de plomb brut par-dessus les joints à tasseaux en bois afin de comprimer fortement le zinc et l'obliger à absorber sa propre énergie d'expansion de manière totalement interne sans aucun allongement visible à la surface", "isCorrect": False},
                        {"text": "Réaliser des soudures par résistance électrique sur chaque recouvrement transversal pour fusionner les tôles en une seule plaque monolithique capable de transmettre l'effort de rétraction thermique directement aux murs porteurs en maçonnerie lourde", "isCorrect": False},
                        {"text": "Percer de multiples rangées de trous oblongs très espacés sur l'intégralité des bacs de couverture afin de relâcher les tensions internes du métal lors du passage brutal des nuages chargés de grêle tout en conservant une rigidité torsionnelle suffisante", "isCorrect": False}
                    ],
                    "correction": "Pour les versants de toiture dont la longueur excède la dimension maximale d'expansion d'un bac de zinc (souvent limitée à 10 ou 13 mètres), on crée un ressaut (une marche de 8 cm minimum charpentée). Le bac amont déverse l'eau dans le bac aval via une agrafure spécifique libre, fractionnant ainsi la toiture et permettant la dilatation par tronçons indépendants."
                }
            ]
        }
    }
}