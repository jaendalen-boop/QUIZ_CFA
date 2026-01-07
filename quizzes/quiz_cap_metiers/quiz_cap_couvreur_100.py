quiz_data = {
    "title": "Quiz CAP Couvreur : Technologie, Techniques, Sécurité et Calculs (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE, SÉCURITÉ ET PRÉVENTION DES RISQUES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : HYGIÈNE, SÉCURITÉ ET PRÉVENTION DES RISQUES (SST)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la protection collective prioritaire à installer en rive de toiture ?",
                    "answerOptions": [
                        {"text": "Garde-corps", "isCorrect": True},
                        {"text": "Ligne de vie temporaire", "isCorrect": False},
                        {"text": "Ancrage structurel individuel", "isCorrect": False},
                        {"text": "Échelle de toit plate", "isCorrect": False}
                    ],
                    "correction": "Le Code du travail impose de privilégier la protection collective (garde-corps) sur la protection individuelle (harnais) pour limiter les risques de chute de hauteur."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la hauteur minimale de dépassement d'une échelle d'accès au niveau supérieur ?",
                    "answerOptions": [
                        {"text": "1 mètre", "isCorrect": True},
                        {"text": "50 centimètres", "isCorrect": False},
                        {"text": "10 centimètres", "isCorrect": False},
                        {"text": "2 mètres", "isCorrect": False}
                    ],
                    "correction": "Pour sécuriser l'accès, l'échelle doit dépasser le niveau d'accès d'au moins 1 mètre afin de permettre à l'opérateur de se tenir aux montants lors du rétablissement."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle classe de montage d'échafaudage autorise une charge de 200 kg/m² ?",
                    "answerOptions": [
                        {"text": "Classe 3", "isCorrect": True},
                        {"text": "Classe 1", "isCorrect": False},
                        {"text": "Classe 6", "isCorrect": False},
                        {"text": "Classe 5", "isCorrect": False}
                    ],
                    "correction": "Les classes d'échafaudage définissent la charge admissible. La classe 3 correspond à une charge de 200 daN/m² (environ 200 kg), standard pour les travaux de couverture courants."
                },
                {
                    "questionNumber": 4,
                    "question": "Que signifie le sigle EPI ?",
                    "answerOptions": [
                        {"text": "Équipement de Protection Individuelle", "isCorrect": True},
                        {"text": "Élément de Prévention Incendie", "isCorrect": False},
                        {"text": "Échafaudage Pour Industrie", "isCorrect": False},
                        {"text": "Étude Préalable d'Intervention", "isCorrect": False}
                    ],
                    "correction": "Les EPI (casque, chaussures, harnais, gants) sont des dispositifs destinés à être portés par une personne en vue de la protéger contre un ou plusieurs risques."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel document unique doit obligatoirement être présent sur le chantier pour l'évaluation des risques ?",
                    "answerOptions": [
                        {"text": "Le DUER", "isCorrect": True},
                        {"text": "Le PPSPS", "isCorrect": False},
                        {"text": "Le CCTP", "isCorrect": False},
                        {"text": "Le DICT", "isCorrect": False}
                    ],
                    "correction": "Le Document Unique d'Évaluation des Risques (DUER) est obligatoire dans toute entreprise et répertorie les risques professionnels ainsi que les mesures de prévention associées."
                },
                {
                    "questionNumber": 6,
                    "question": "À quel moment le port du harnais de sécurité est-il obligatoire sur un toit ?",
                    "answerOptions": [
                        {"text": "En l'absence de protection collective", "isCorrect": True},
                        {"text": "Uniquement s'il pleut ou vente fort", "isCorrect": False},
                        {"text": "Seulement pour les travaux sur ardoises", "isCorrect": False},
                        {"text": "Quand la pente est supérieure à 45 degrés", "isCorrect": False}
                    ],
                    "correction": "Le harnais est une protection individuelle qui ne doit être utilisée que lorsqu'il est techniquement impossible de mettre en place une protection collective (garde-corps, échafaudage)."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est la couleur conventionnelle des réseaux de gaz enterrés lors d'un terrassement ?",
                    "answerOptions": [
                        {"text": "Jaune", "isCorrect": True},
                        {"text": "Bleu", "isCorrect": False},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False}
                    ],
                    "correction": "Le code couleur normalisé pour le grillage avertisseur des réseaux enterrés est le jaune pour le gaz, rouge pour l'électricité, bleu pour l'eau et vert pour les télécoms."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est le principal risque lié à la découpe de matériaux contenant de l'amiante ?",
                    "answerOptions": [
                        {"text": "Inhalation de fibres cancérigènes", "isCorrect": True},
                        {"text": "Coupure profonde aux mains", "isCorrect": False},
                        {"text": "Échauffement excessif de la meuleuse", "isCorrect": False},
                        {"text": "Projection d'éclats dans les yeux", "isCorrect": False}
                    ],
                    "correction": "L'amiante libère des fibres microscopiques invisibles qui, une fois inhalées, peuvent provoquer des maladies graves comme l'asbestose ou le cancer du poumon."
                },
                {
                    "questionNumber": 9,
                    "question": "Comment doit-on stocker les bouteilles de gaz sur un chantier ?",
                    "answerOptions": [
                        {"text": "Debout et attachées", "isCorrect": True},
                        {"text": "Couchées au sol", "isCorrect": False},
                        {"text": "En plein soleil", "isCorrect": False},
                        {"text": "Dans un véhicule fermé", "isCorrect": False}
                    ],
                    "correction": "Les bouteilles de gaz doivent toujours être stockées verticalement (debout) et arrimées solidement pour éviter qu'elles ne tombent et n'endommagent le robinet."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la charge maximale recommandée pour le port manuel répétitif de charges par un homme ?",
                    "answerOptions": [
                        {"text": "25 kg", "isCorrect": True},
                        {"text": "55 kg", "isCorrect": False},
                        {"text": "75 kg", "isCorrect": False},
                        {"text": "100 kg", "isCorrect": False}
                    ],
                    "correction": "La norme AFNOR NF X35-109 recommande de ne pas dépasser 25 kg pour le port répétitif de charges afin de prévenir les troubles musculo-squelettiques (TMS)."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel type d'extincteur est le plus adapté pour un feu d'origine électrique ?",
                    "answerOptions": [
                        {"text": "CO2", "isCorrect": True},
                        {"text": "Eau", "isCorrect": False},
                        {"text": "Mousse", "isCorrect": False},
                        {"text": "Sable", "isCorrect": False}
                    ],
                    "correction": "L'extincteur au dioxyde de carbone (CO2) est privilégié pour les feux électriques car il est non conducteur et ne laisse pas de résidus corrosifs sur les équipements."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle vérification est indispensable avant d'utiliser un échafaudage fixe ?",
                    "answerOptions": [
                        {"text": "La réception de l'échafaudage", "isCorrect": True},
                        {"text": "La propreté des planchers", "isCorrect": False},
                        {"text": "La couleur de la peinture", "isCorrect": False},
                        {"text": "La marque du fabricant", "isCorrect": False}
                    ],
                    "correction": "Avant toute utilisation, un échafaudage doit faire l'objet d'une 'réception', un examen formel validant sa conformité, sa stabilité et la présence des protections."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est le rôle de la plinthe au pied d'un garde-corps ?",
                    "answerOptions": [
                        {"text": "Empêcher la chute d'objets ou de matériaux", "isCorrect": True},
                        {"text": "Faire joli pour la finition de l'échafaudage", "isCorrect": False},
                        {"text": "Servir de marchepied pour gagner de la hauteur", "isCorrect": False},
                        {"text": "Renforcer la structure verticale des montants", "isCorrect": False}
                    ],
                    "correction": "La plinthe (ou butée de pied) est un élément de sécurité obligatoire du garde-corps qui empêche les outils ou matériaux de glisser et de tomber sur des personnes en contrebas."
                },
                {
                    "questionNumber": 14,
                    "question": "Que doit faire un couvreur en cas d'orage imminent ?",
                    "answerOptions": [
                        {"text": "Descendre immédiatement du toit", "isCorrect": True},
                        {"text": "Se mettre à l'abri sous la charpente", "isCorrect": False},
                        {"text": "Continuer pour finir l'étanchéité", "isCorrect": False},
                        {"text": "S'attacher plus court avec son harnais", "isCorrect": False}
                    ],
                    "correction": "Le risque de foudroiement et de glissade est extrême. La consigne de sécurité stricte est d'arrêter les travaux et de descendre de la toiture dès l'approche d'un orage."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel angle d'inclinaison est préconisé pour positionner une échelle simple contre un mur ?",
                    "answerOptions": [
                        {"text": "Entre 65 et 75 degrés", "isCorrect": True},
                        {"text": "Entre 30 et 40 degrés", "isCorrect": False},
                        {"text": "Exactement 90 degrés", "isCorrect": False},
                        {"text": "Moins de 45 degrés", "isCorrect": False}
                    ],
                    "correction": "Un angle compris entre 65° et 75° assure la stabilité optimale de l'échelle, évitant qu'elle ne glisse du pied (trop plat) ou ne bascule en arrière (trop raide)."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel équipement est spécifique à la prévention des chutes à travers une toiture fragile ?",
                    "answerOptions": [
                        {"text": "Chemin de circulation", "isCorrect": True},
                        {"text": "Chaussures de sécurité", "isCorrect": False},
                        {"text": "Casque avec jugulaire", "isCorrect": False},
                        {"text": "Gants anti-coupure", "isCorrect": False}
                    ],
                    "correction": "Sur les matériaux fragiles (fibrociment, plaques translucides), il est impératif d'utiliser des chemins de circulation (planches de répartition) pour ne pas passer au travers."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle substance est strictement interdite pour nettoyer les mains après l'usage de bitume ?",
                    "answerOptions": [
                        {"text": "Essence", "isCorrect": True},
                        {"text": "Savon d'atelier", "isCorrect": False},
                        {"text": "Lingettes spéciales", "isCorrect": False},
                        {"text": "Huile végétale", "isCorrect": False}
                    ],
                    "correction": "L'utilisation de solvants comme l'essence ou le White Spirit sur la peau est dangereuse (pénétration cutanée toxique). Il faut utiliser des savons microbilles ou huiles spécifiques."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la signification du pictogramme rond à fond bleu sur un chantier ?",
                    "answerOptions": [
                        {"text": "Une obligation", "isCorrect": True},
                        {"text": "Une interdiction", "isCorrect": False},
                        {"text": "Un avertissement", "isCorrect": False},
                        {"text": "Une indication incendie", "isCorrect": False}
                    ],
                    "correction": "La signalisation de sécurité est normée : les panneaux ronds à fond bleu imposent une obligation (exemple : 'Port du casque obligatoire')."
                },
                {
                    "questionNumber": 19,
                    "question": "Pour éviter les troubles musculo-squelettiques lors de la pose d'ardoises, que doit privilégier le couvreur ?",
                    "answerOptions": [
                        {"text": "L'alternance des tâches et des postures", "isCorrect": True},
                        {"text": "Le travail à genoux sans genouillères", "isCorrect": False},
                        {"text": "Le port de charges lourdes d'un seul coup", "isCorrect": False},
                        {"text": "La rapidité d'exécution sans pause", "isCorrect": False}
                    ],
                    "correction": "La prévention des TMS repose sur la variation des gestes, l'utilisation d'aides à la manutention et l'alternance des postures pour ne pas solliciter toujours les mêmes articulations."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle action est prioritaire lors de la découverte d'un accident sur chantier ?",
                    "answerOptions": [
                        {"text": "Protéger", "isCorrect": True},
                        {"text": "Alerter", "isCorrect": False},
                        {"text": "Secourir", "isCorrect": False},
                        {"text": "Filmer", "isCorrect": False}
                    ],
                    "correction": "La procédure de secourisme suit l'ordre P.A.S. : Protéger (la zone et soi-même), Alerter (les secours), puis Secourir (la victime). On ne peut secourir sans avoir sécurisé la zone."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNOLOGIE DES MATÉRIAUX ET OUTILLAGE PROFESSIONNEL (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNOLOGIE DES MATÉRIAUX ET OUTILLAGE PROFESSIONNEL",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la matière première principale constitutive d'une tuile traditionnelle ?",
                    "answerOptions": [
                        {"text": "Argile", "isCorrect": True},
                        {"text": "Ciment prompt", "isCorrect": False},
                        {"text": "Résine polymère", "isCorrect": False},
                        {"text": "Silice pure", "isCorrect": False}
                    ],
                    "correction": "La tuile de terre cuite est fabriquée à partir d'argile, qui est broyée, humidifiée, façonnée puis cuite à haute température pour obtenir sa dureté finale."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel outil spécifique le couvreur utilise-t-il pour tailler l'ardoise manuellement sur le toit ?",
                    "answerOptions": [
                        {"text": "Le marteau et l'enclume", "isCorrect": True},
                        {"text": "La meuleuse d'angle thermique", "isCorrect": False},
                        {"text": "La cisaille à métaux articulée", "isCorrect": False},
                        {"text": "Le massicot de chantier hydraulique", "isCorrect": False}
                    ],
                    "correction": "La taille artisanale de l'ardoise (épaufrure) se réalise traditionnellement à l'aide d'un marteau de couvreur (ayant un tranchant et une pointe) et d'une enclume (ou tas) sur laquelle on appuie l'ardoise."
                },
                {
                    "questionNumber": 23,
                    "question": "Comment appelle-t-on le phénomène naturel de protection qui se forme à la surface du zinc neuf ?",
                    "answerOptions": [
                        {"text": "La patine", "isCorrect": True},
                        {"text": "La rouille perforante", "isCorrect": False},
                        {"text": "Le vernis industriel", "isCorrect": False},
                        {"text": "La couche de primaire", "isCorrect": False}
                    ],
                    "correction": "Le zinc naturel s'auto-protège en réagissant avec l'eau et le dioxyde de carbone de l'air, formant une couche de carbonate de zinc appelée 'patine', qui le rend gris mat et durable."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle principal d'un écran de sous-toiture de type HPV ?",
                    "answerOptions": [
                        {"text": "Laisser passer la vapeur d'eau venant de l'intérieur", "isCorrect": True},
                        {"text": "Empêcher totalement l'air de circuler sous les tuiles", "isCorrect": False},
                        {"text": "Remplacer définitivement les tuiles cassées ou absentes", "isCorrect": False},
                        {"text": "Renforcer la structure porteuse de la charpente en bois", "isCorrect": False}
                    ],
                    "correction": "Un écran HPV (Haute Perméabilité à la Vapeur d'eau) assure l'étanchéité à l'eau venant de l'extérieur tout en permettant l'évacuation de l'humidité intérieure, évitant ainsi la condensation dans l'isolant."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle essence de bois est la plus couramment utilisée pour les liteaux de couverture ?",
                    "answerOptions": [
                        {"text": "Sapin", "isCorrect": True},
                        {"text": "Chêne massif", "isCorrect": False},
                        {"text": "Teck exotique", "isCorrect": False},
                        {"text": "Ébène noir", "isCorrect": False}
                    ],
                    "correction": "Les résineux (sapin, épicéa) sont privilégiés pour le litelage (liteaux, voliges) en raison de leur légèreté, de leur coût abordable et de leur facilité de clouage."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel terme désigne la partie visible d'une ardoise ou d'une tuile une fois posée ?",
                    "answerOptions": [
                        {"text": "Le pureau", "isCorrect": True},
                        {"text": "Le recouvrement", "isCorrect": False},
                        {"text": "Le tenon", "isCorrect": False},
                        {"text": "La doucine", "isCorrect": False}
                    ],
                    "correction": "Le pureau correspond à la partie du matériau de couverture qui reste exposée aux intempéries et n'est pas recouverte par l'élément du rang supérieur."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle caractéristique physique définit la classe de résistance d'une ardoise naturelle ?",
                    "answerOptions": [
                        {"text": "La teneur en carbonate de calcium", "isCorrect": True},
                        {"text": "La couleur de la roche d'extraction", "isCorrect": False},
                        {"text": "La forme de découpe de l'ardoise", "isCorrect": False},
                        {"text": "Le nom de la carrière d'origine", "isCorrect": False}
                    ],
                    "correction": "La norme NF EN 12326 classe les ardoises selon leur teneur en carbonate (résistance aux pluies acides), leur oxydation thermique et leur absorption d'eau. Une forte teneur en carbonate fragilise l'ardoise dans le temps."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel outil permet de tracer des lignes parallèles au bord d'une feuille de zinc ?",
                    "answerOptions": [
                        {"text": "Trusquin", "isCorrect": True},
                        {"text": "Équerre", "isCorrect": False},
                        {"text": "Compas", "isCorrect": False},
                        {"text": "Niveau", "isCorrect": False}
                    ],
                    "correction": "Le trusquin est l'outil de traçage par excellence du zingueur. Il permet de marquer par rayure une ligne parfaitement parallèle au bord de la feuille de métal pour préparer un pliage."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la particularité d'une tuile à emboîtement par rapport à une tuile plate ?",
                    "answerOptions": [
                        {"text": "Elle possède des reliefs pour guider l'eau et se caler", "isCorrect": True},
                        {"text": "Elle est obligatoirement fabriquée en béton gris", "isCorrect": False},
                        {"text": "Elle ne nécessite aucune fixation sur le liteau", "isCorrect": False},
                        {"text": "Elle est deux fois plus lourde au mètre carré", "isCorrect": False}
                    ],
                    "correction": "Les tuiles à emboîtement (ou mécaniques) disposent de chicanes et de reliefs latéraux qui assurent l'étanchéité et le verrouillage entre elles, permettant de réduire le recouvrement nécessaire."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel métal est réputé pour sa couleur 'vert-de-gris' après oxydation ?",
                    "answerOptions": [
                        {"text": "Cuivre", "isCorrect": True},
                        {"text": "Plomb", "isCorrect": False},
                        {"text": "Aluminium", "isCorrect": False},
                        {"text": "Acier", "isCorrect": False}
                    ],
                    "correction": "Le cuivre, initialement rouge-orangé, s'oxyde avec le temps pour devenir brun foncé, puis finit par prendre une teinte verte caractéristique appelée vert-de-gris."
                },
                {
                    "questionNumber": 31,
                    "question": "À quoi sert une 'bignette' dans la caisse à outils du zingueur ?",
                    "answerOptions": [
                        {"text": "Façonner le plomb", "isCorrect": True},
                        {"text": "Couper le bois", "isCorrect": False},
                        {"text": "Visser les crochets", "isCorrect": False},
                        {"text": "Percer le béton", "isCorrect": False}
                    ],
                    "correction": "La bignette est un outil de frappe spécifique (sorte de batte en bois ou plastique) utilisé pour travailler et former les feuilles de plomb sans les marquer ni les percer."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est la classe d'emploi minimale requise pour le bois de charpente exposé à l'humidité ?",
                    "answerOptions": [
                        {"text": "Classe 2", "isCorrect": True},
                        {"text": "Classe 1", "isCorrect": False},
                        {"text": "Classe 0", "isCorrect": False},
                        {"text": "Classe A", "isCorrect": False}
                    ],
                    "correction": "Les bois de charpente et de couverture (liteaux) doivent être traités au minimum en Classe 2 (supportant une humidité occasionnelle supérieure à 20%) pour résister aux insectes et champignons."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est l'avantage principal de l'acier inoxydable pour les crochets d'ardoise ?",
                    "answerOptions": [
                        {"text": "Résistance totale à la corrosion", "isCorrect": True},
                        {"text": "Facilité de peinture en couleur", "isCorrect": False},
                        {"text": "Coût d'achat très faible", "isCorrect": False},
                        {"text": "Souplesse extrême au pliage", "isCorrect": False}
                    ],
                    "correction": "L'inox (acier inoxydable) est utilisé pour les crochets, notamment en bord de mer, car il offre la meilleure résistance à la corrosion saline par rapport au cuivre ou à l'acier galvanisé."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel phénomène physique affecte particulièrement les gouttières en zinc lors des changements de température ?",
                    "answerOptions": [
                        {"text": "Dilatation", "isCorrect": True},
                        {"text": "Sublimation", "isCorrect": False},
                        {"text": "Évaporation", "isCorrect": False},
                        {"text": "Fusion", "isCorrect": False}
                    ],
                    "correction": "Les métaux se dilatent à la chaleur et se rétractent au froid. Il est crucial de prévoir des joints de dilatation sur les longues gouttières en zinc pour éviter qu'elles ne cassent ou ne se déforment."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel outil est indispensable pour réaliser un pliage net sur une feuille de métal à l'atelier ?",
                    "answerOptions": [
                        {"text": "Plieuse", "isCorrect": True},
                        {"text": "Cisaille", "isCorrect": False},
                        {"text": "Boudineuse", "isCorrect": False},
                        {"text": "Guillotine", "isCorrect": False}
                    ],
                    "correction": "La plieuse d'atelier (manuelle ou numérique) permet de plier les feuilles de métal (zinc, cuivre, acier) selon des angles précis et rectilignes sur toute la longueur de la feuille."
                },
                {
                    "questionNumber": 36,
                    "question": "Qu'est-ce qu'une 'noue' dans la terminologie des matériaux ?",
                    "answerOptions": [
                        {"text": "Une bande métallique pour l'angle rentrant", "isCorrect": True},
                        {"text": "Une tuile faîtière ventilée par le dessous", "isCorrect": False},
                        {"text": "Un crochet de sécurité pour l'échelle", "isCorrect": False},
                        {"text": "Une planche de rive en bois massif", "isCorrect": False}
                    ],
                    "correction": "La noue est l'ouvrage (souvent métallique en zinc ou plomb) qui assure l'étanchéité dans l'angle rentrant formé par la rencontre de deux versants de toiture, collectant les eaux de ruissellement."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle propriété du plomb le rend utile pour les abergements complexes ?",
                    "answerOptions": [
                        {"text": "Malléabilité", "isCorrect": True},
                        {"text": "Rigidité", "isCorrect": False},
                        {"text": "Transparence", "isCorrect": False},
                        {"text": "Élasticité", "isCorrect": False}
                    ],
                    "correction": "Le plomb est un métal extrêmement malléable, ce qui permet de le marteler pour lui faire épouser parfaitement les formes irrégulières des tuiles ou des maçonneries (cheminées) afin d'assurer l'étanchéité."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel type de clou doit-on utiliser pour fixer une plaque de zinc ?",
                    "answerOptions": [
                        {"text": "Clou calotin", "isCorrect": True},
                        {"text": "Clou lisse simple", "isCorrect": False},
                        {"text": "Vis à bois longue", "isCorrect": False},
                        {"text": "Agrafe pneumatique", "isCorrect": False}
                    ],
                    "correction": "On utilise des clous calotins (avec une tête large en plomb ou étanche) ou des pattes de fixation spécifiques pour éviter les infiltrations d'eau au niveau des points de fixation du zinc."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle est la fonction d'une pince à soyer ?",
                    "answerOptions": [
                        {"text": "Réduire le diamètre d'un tuyau pour l'emboîtement", "isCorrect": True},
                        {"text": "Couper les tiges filetées de gros diamètre", "isCorrect": False},
                        {"text": "Sertir les rails de plaques de plâtre", "isCorrect": False},
                        {"text": "Élargir le trou d'évacuation de la gouttière", "isCorrect": False}
                    ],
                    "correction": "La pince à soyer (ou pince à rétreindre) sert à plisser le bout d'un tuyau de descente en zinc pour réduire légèrement son diamètre, permettant ainsi de l'emboîter dans le tuyau suivant."
                },
                {
                    "questionNumber": 40,
                    "question": "Parmi ces matériaux, lequel est un isolant thermique souvent posé par le couvreur ?",
                    "answerOptions": [
                        {"text": "Laine minérale", "isCorrect": True},
                        {"text": "Béton armé", "isCorrect": False},
                        {"text": "Plaque de plâtre", "isCorrect": False},
                        {"text": "Parpaing creux", "isCorrect": False}
                    ],
                    "correction": "Le couvreur intervient souvent dans l'isolation de toiture (sarking ou entre chevrons) en posant des isolants comme la laine de verre, la laine de roche ou des panneaux de polyuréthane."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : TECHNIQUES DE POSE : TUILES ET ARDOISES (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : TECHNIQUES DE POSE : TUILES ET ARDOISES (Petits éléments)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Comment nomme-t-on la partie visible de l'ardoise une fois posée sur le toit ?",
                    "answerOptions": [
                        {"text": "Pureau", "isCorrect": True},
                        {"text": "Recouvrement", "isCorrect": False},
                        {"text": "Faux-pureau", "isCorrect": False},
                        {"text": "Chef de tête", "isCorrect": False}
                    ],
                    "correction": "Le pureau est la surface de l'ardoise (ou de la tuile) qui reçoit la pluie. C'est la partie qui n'est pas recouverte par les ardoises des rangs supérieurs."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel élément en bois permet de relever le premier rang de tuiles à l'égout ?",
                    "answerOptions": [
                        {"text": "Chanlatte", "isCorrect": True},
                        {"text": "Chevron", "isCorrect": False},
                        {"text": "Panne", "isCorrect": False},
                        {"text": "Contre-liteau", "isCorrect": False}
                    ],
                    "correction": "La chanlatte est une pièce de bois biseautée (ou un liteau surélevé) fixée à l'égout. Elle permet de donner au premier rang la même inclinaison que les suivants (basculement)."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la formule théorique pour calculer le pureau d'une ardoise posée au crochet ?",
                    "answerOptions": [
                        {"text": "Longueur de l'ardoise moins le recouvrement divisé par deux", "isCorrect": True},
                        {"text": "Longueur de l'ardoise plus le recouvrement divisé par deux", "isCorrect": False},
                        {"text": "Longueur totale de l'ardoise divisée par trois", "isCorrect": False},
                        {"text": "Hauteur du crochet multipliée par la pente du toit", "isCorrect": False}
                    ],
                    "correction": "La formule P = (L - R) / 2 est fondamentale. Elle permet de déterminer l'espacement des liteaux pour que l'eau ne remonte pas au-delà de la tête de l'ardoise du rang inférieur."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle technique de pose est obligatoire pour les tuiles plates rectangulaires ?",
                    "answerOptions": [
                        {"text": "Joints croisés", "isCorrect": True},
                        {"text": "Joints droits superposés", "isCorrect": False},
                        {"text": "Pose en diagonale simple", "isCorrect": False},
                        {"text": "Alignement vertical strict", "isCorrect": False}
                    ],
                    "correction": "Les tuiles plates doivent être posées à joints croisés (la tuile du dessus couvre le joint des deux tuiles du dessous) pour assurer l'étanchéité, contrairement à certaines tuiles canal à joints droits."
                },
                {
                    "questionNumber": 45,
                    "question": "Qu'est-ce qu'un 'arêtier' sur une toiture ?",
                    "answerOptions": [
                        {"text": "Angle sortant", "isCorrect": True},
                        {"text": "Angle rentrant", "isCorrect": False},
                        {"text": "Mur pignon", "isCorrect": False},
                        {"text": "Gouttière pendante", "isCorrect": False}
                    ],
                    "correction": "L'arêtier est la ligne de rencontre de deux versants formant un angle saillant (sortant), par opposition à la noue qui forme un angle rentrant."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le rôle principal d'une tuile chatière ?",
                    "answerOptions": [
                        {"text": "Ventiler", "isCorrect": True},
                        {"text": "Éclairer", "isCorrect": False},
                        {"text": "Isoler", "isCorrect": False},
                        {"text": "Décorer", "isCorrect": False}
                    ],
                    "correction": "La chatière est une tuile technique spécifique comportant une ouverture grillagée destinée à créer une circulation d'air sous la couverture pour éviter la condensation et le pourrissement des bois."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on la ligne supérieure horizontale de jonction de deux versants ?",
                    "answerOptions": [
                        {"text": "Faîtage", "isCorrect": True},
                        {"text": "Rive latérale", "isCorrect": False},
                        {"text": "Égout de toit", "isCorrect": False},
                        {"text": "Solin de base", "isCorrect": False}
                    ],
                    "correction": "Le faîtage est le sommet du toit. Son étanchéité est critique et peut être réalisée à sec (closoir) ou au mortier (scellement)."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la fonction d'un closoir ventilé sous les faîtières ?",
                    "answerOptions": [
                        {"text": "Assurer l'étanchéité et la ventilation en pose à sec", "isCorrect": True},
                        {"text": "Coller définitivement les tuiles faîtières au support", "isCorrect": False},
                        {"text": "Remplacer les tuiles faîtières en terre cuite", "isCorrect": False},
                        {"text": "Empêcher totalement l'air de sortir par le haut", "isCorrect": False}
                    ],
                    "correction": "Le closoir est un rouleau souple posé sur la lisse de rehausse. Il empêche l'eau et la neige poudreuse de pénétrer tout en laissant l'air chaud s'échapper du comble."
                },
                {
                    "questionNumber": 49,
                    "question": "Dans quel cas doit-on augmenter la valeur du recouvrement minimal ?",
                    "answerOptions": [
                        {"text": "Faible pente", "isCorrect": True},
                        {"text": "Forte pente", "isCorrect": False},
                        {"text": "Grand pureau", "isCorrect": False},
                        {"text": "Petit format", "isCorrect": False}
                    ],
                    "correction": "Plus la pente du toit est faible, plus l'eau s'écoule lentement et risque de remonter par capillarité ou vent. Il faut donc augmenter le recouvrement pour garantir l'étanchéité."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle fixation est préconisée pour les tuiles de rive exposées au vent ?",
                    "answerOptions": [
                        {"text": "Vissage", "isCorrect": True},
                        {"text": "Collage silicone", "isCorrect": False},
                        {"text": "Pose libre", "isCorrect": False},
                        {"text": "Mortier pur", "isCorrect": False}
                    ],
                    "correction": "Les rives sont les zones les plus sollicitées par le vent (dépression). Le vissage dans la charpente ou le liteau est la fixation mécanique la plus sûre."
                },
                {
                    "questionNumber": 51,
                    "question": "Qu'appelle-t-on 'le tranchis' dans une noue ouverte ?",
                    "answerOptions": [
                        {"text": "La coupe biaisée des tuiles ou ardoises dans l'axe de la noue", "isCorrect": True},
                        {"text": "La plaque de zinc qui récupère l'eau au fond de la noue", "isCorrect": False},
                        {"text": "Le liteau supplémentaire posé le long de la pince", "isCorrect": False},
                        {"text": "La première tuile entière posée avant la coupe", "isCorrect": False}
                    ],
                    "correction": "Le tranchis désigne l'alignement de la coupe des éléments de couverture (tuiles/ardoises) le long de la ligne de noue pour dégager le couloir d'écoulement des eaux."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la particularité de la pose des tuiles canal traditionnelles ?",
                    "answerOptions": [
                        {"text": "Alternance de tuiles de courant et tuiles de couvert", "isCorrect": True},
                        {"text": "Fixation obligatoire de chaque tuile par quatre clous", "isCorrect": False},
                        {"text": "Utilisation exclusive sur des pentes supérieures à 60 degrés", "isCorrect": False},
                        {"text": "Emboîtement mécanique latéral et longitudinal complexe", "isCorrect": False}
                    ],
                    "correction": "La pose traditionnelle se fait 'tige de botte' : une tuile de courant (dessous, creux vers le haut) et une tuile de couvert (dessus, creux vers le bas) qui chevauche deux courants."
                },
                {
                    "questionNumber": 53,
                    "question": "Que signifie 'panacher' les ardoises ou les tuiles avant la pose ?",
                    "answerOptions": [
                        {"text": "Mélanger les palettes pour harmoniser les nuances de couleur", "isCorrect": True},
                        {"text": "Trier les éléments cassés pour les jeter à la benne", "isCorrect": False},
                        {"text": "Mouiller les matériaux pour qu'ils ne glissent pas", "isCorrect": False},
                        {"text": "Peindre les éléments avec une teinte différente", "isCorrect": False}
                    ],
                    "correction": "Le panachage consiste à prélever les matériaux dans différentes palettes simultanément lors de la pose pour éviter de créer des zones de couleurs différentes (nuances de cuisson ou de carrière) sur le toit."
                },
                {
                    "questionNumber": 54,
                    "question": "À quoi sert la 'pince' réalisée au marteau sur une ardoise ?",
                    "answerOptions": [
                        {"text": "Faciliter l'écoulement de l'eau entre les ardoises", "isCorrect": True},
                        {"text": "Marquer l'emplacement exact du futur clou", "isCorrect": False},
                        {"text": "Décorer le bord visible de l'ardoise", "isCorrect": False},
                        {"text": "Renforcer la solidité de l'ardoise", "isCorrect": False}
                    ],
                    "correction": "Lors de la taille de l'ardoise, on réalise une coupe en biseau (épaufrure) appelée pince. Elle permet à l'eau de s'évaser et de ne pas remonter par capillarité entre les ardoises superposées."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel accessoire empêche l'intrusion de petits animaux sous l'onde des tuiles à l'égout ?",
                    "answerOptions": [
                        {"text": "Peigne", "isCorrect": True},
                        {"text": "Closoir", "isCorrect": False},
                        {"text": "Solin", "isCorrect": False},
                        {"text": "Noquet", "isCorrect": False}
                    ],
                    "correction": "Le peigne d'égout (ou barrière anti-nuisibles) comble le vide sous l'onde de la tuile tout en permettant le passage de l'air pour la ventilation basse."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle est la conséquence d'un 'pincement' au niveau du lattage ?",
                    "answerOptions": [
                        {"text": "Les ardoises vont bailler et risquent de casser", "isCorrect": True},
                        {"text": "L'étanchéité sera meilleure face au vent", "isCorrect": False},
                        {"text": "Le pureau sera plus grand que prévu", "isCorrect": False},
                        {"text": "La consommation de bois sera réduite", "isCorrect": False}
                    ],
                    "correction": "Un pincement se produit si les liteaux ne sont pas parfaitement plans. L'ardoise ne pose pas à plat, elle 'baille' (se soulève), ce qui la rend fragile au vent et au poids (casse)."
                },
                {
                    "questionNumber": 57,
                    "question": "Où doit se situer la jonction de deux liteaux bout à bout ?",
                    "answerOptions": [
                        {"text": "Toujours sur un chevron", "isCorrect": True},
                        {"text": "N'importe où entre deux chevrons", "isCorrect": False},
                        {"text": "Exactement au milieu de l'entraxe", "isCorrect": False},
                        {"text": "Uniquement sur les pannes pignon", "isCorrect": False}
                    ],
                    "correction": "Pour assurer la solidité de la structure, les aboutages de liteaux doivent impérativement se faire sur un support solide (le chevron) et jamais 'dans le vide'."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle pièce métallique assure l'étanchéité entre une couverture en ardoise et un mur latéral ?",
                    "answerOptions": [
                        {"text": "Noquet", "isCorrect": True},
                        {"text": "Dousine", "isCorrect": False},
                        {"text": "Lambourde", "isCorrect": False},
                        {"text": "Chevêtre", "isCorrect": False}
                    ],
                    "correction": "Les noquets sont des pièces métalliques pliées en équerre (souvent en zinc), glissées à chaque rang d'ardoise contre le mur, garantissant une étanchéité parfaite à chaque niveau."
                },
                {
                    "questionNumber": 59,
                    "question": "Comment calcule-t-on le nombre de tuiles au mètre carré ?",
                    "answerOptions": [
                        {"text": "1 divisé par la surface utile d'une tuile", "isCorrect": True},
                        {"text": "Surface du toit divisée par le pureau", "isCorrect": False},
                        {"text": "Largeur utile multipliée par le pureau", "isCorrect": False},
                        {"text": "Pureau divisé par la largeur utile", "isCorrect": False}
                    ],
                    "correction": "La consommation au m² se détermine par la formule : 1 / (Pureau × Largeur Utile). C'est indispensable pour réaliser le quantitatif (devis et commandes)."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle est la méthode correcte pour fixer une tuile à emboîtement sur le liteau ?",
                    "answerOptions": [
                        {"text": "Vissage ou clouage dans le trou pré-percé", "isCorrect": True},
                        {"text": "Collage au mastic polyuréthane sur le dessus", "isCorrect": False},
                        {"text": "Ligature au fil de fer recuit sous la tuile", "isCorrect": False},
                        {"text": "Simple pose sans aucune fixation mécanique", "isCorrect": False}
                    ],
                    "correction": "Les tuiles à emboîtement disposent de trous pré-percés en tête. On utilise des vis ou des clous crantés pour les fixer au liteau, selon les règles 'au vent' définies par les DTU."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : MÉTAUX, ZINGUERIE ET ÉVACUATION DES EAUX PLUVIALES (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : MÉTAUX, ZINGUERIE ET ÉVACUATION DES EAUX PLUVIALES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle opération prépare la panne du fer à souder avant son utilisation ?",
                    "answerOptions": [
                        {"text": "L'étamage", "isCorrect": True},
                        {"text": "Le limage à froid", "isCorrect": False},
                        {"text": "Le trempage à l'eau", "isCorrect": False},
                        {"text": "Le graissage à l'huile", "isCorrect": False}
                    ],
                    "correction": "L'étamage consiste à recouvrir la pointe en cuivre du fer d'une fine couche d'étain fondu. Cela facilite le transfert de chaleur et l'adhérence de la soudure lors du travail."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la pente minimale conventionnelle (DTU) pour une gouttière pendante ?",
                    "answerOptions": [
                        {"text": "5 mm par mètre", "isCorrect": True},
                        {"text": "2 cm par mètre", "isCorrect": False},
                        {"text": "10 mm par mètre", "isCorrect": False},
                        {"text": "0 mm par mètre", "isCorrect": False}
                    ],
                    "correction": "Pour assurer un bon écoulement de l'eau et son auto-curage (évacuation des débris), une pente minimale de 5 mm/m est requise par le DTU 40.5."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel phénomène chimique se produit si on met en contact direct du cuivre et du zinc ?",
                    "answerOptions": [
                        {"text": "Électrolyse", "isCorrect": True},
                        {"text": "Polymérisation", "isCorrect": False},
                        {"text": "Sublimation", "isCorrect": False},
                        {"text": "Condensation", "isCorrect": False}
                    ],
                    "correction": "L'électrolyse (ou couple galvanique) provoque la corrosion rapide du zinc (métal moins noble) par le cuivre en présence d'humidité. Il faut toujours isoler ces deux métaux."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel type de gouttière repose directement sur une corniche ou un entablement ?",
                    "answerOptions": [
                        {"text": "Nantaise", "isCorrect": True},
                        {"text": "Pendante", "isCorrect": False},
                        {"text": "Demi-ronde", "isCorrect": False},
                        {"text": "Carrée", "isCorrect": False}
                    ],
                    "correction": "La gouttière nantaise (ou havraise selon le profil) est une gouttière rampante posée sur le bas du versant ou sur une corniche, contrairement à la gouttière pendante fixée par des crochets sous l'égout."
                },
                {
                    "questionNumber": 65,
                    "question": "À quoi sert le décapant (ou eau à souder) appliqué sur le zinc ?",
                    "answerOptions": [
                        {"text": "Nettoyer chimiquement la zone à souder", "isCorrect": True},
                        {"text": "Refroidir le métal avant la soudure", "isCorrect": False},
                        {"text": "Coller les deux pièces ensemble", "isCorrect": False},
                        {"text": "Donner une couleur brillante au zinc", "isCorrect": False}
                    ],
                    "correction": "Le décapant dissout les oxydes présents en surface du métal. Sans lui, l'étain n'adhère pas et la soudure est impossible."
                },
                {
                    "questionNumber": 66,
                    "question": "Quelle est l'épaisseur standard la plus courante pour une feuille de zinc en couverture ?",
                    "answerOptions": [
                        {"text": "0,65 mm", "isCorrect": True},
                        {"text": "2,50 mm", "isCorrect": False},
                        {"text": "0,10 mm", "isCorrect": False},
                        {"text": "5,00 mm", "isCorrect": False}
                    ],
                    "correction": "Les épaisseurs normalisées pour le zinc de couverture sont 0,65 mm, 0,70 mm et 0,80 mm (les numéros 12, 13 et 14). Le 0,65 mm est le standard usuel."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel accessoire permet d'absorber les variations de longueur d'une longue gouttière ?",
                    "answerOptions": [
                        {"text": "Joint de dilatation", "isCorrect": True},
                        {"text": "Talon de naissance", "isCorrect": False},
                        {"text": "Crapaudine", "isCorrect": False},
                        {"text": "Dauphin en fonte", "isCorrect": False}
                    ],
                    "correction": "Le zinc se dilate fortement à la chaleur. Au-delà de 12 mètres linéaires, il est obligatoire d'installer un joint de dilatation pour éviter la rupture des soudures."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment appelle-t-on le façonnage cylindrique en bordure d'une feuille de zinc ?",
                    "answerOptions": [
                        {"text": "Ourlet", "isCorrect": True},
                        {"text": "Pliage", "isCorrect": False},
                        {"text": "Relevé", "isCorrect": False},
                        {"text": "Solin", "isCorrect": False}
                    ],
                    "correction": "L'ourlet (ou boudin) est un roulotté du métal sur lui-même. Il sert à rigidifier le bord de la feuille et à le rendre non coupant."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle pince est utilisée pour élargir l'extrémité d'un tuyau de descente femelle ?",
                    "answerOptions": [
                        {"text": "Pince à emboîture", "isCorrect": True},
                        {"text": "Pince à rétreindre", "isCorrect": False},
                        {"text": "Pince à sertir", "isCorrect": False},
                        {"text": "Pince coupante", "isCorrect": False}
                    ],
                    "correction": "La pince à emboîture écarte le métal pour créer la partie femelle, tandis que la pince à rétreindre (ou à soyer) réduit le diamètre pour créer la partie mâle."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel bois est formellement interdit en support direct d'une couverture en zinc ?",
                    "answerOptions": [
                        {"text": "Chêne", "isCorrect": True},
                        {"text": "Sapin", "isCorrect": False},
                        {"text": "Épicéa", "isCorrect": False},
                        {"text": "Peuplier", "isCorrect": False}
                    ],
                    "correction": "Le chêne et le châtaignier sont des bois riches en tanins. En présence d'humidité, ces tanins attaquent le zinc par acidité. On utilise exclusivement des résineux (sapin, épicéa)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est le métal d'apport utilisé pour souder le zinc ?",
                    "answerOptions": [
                        {"text": "Alliage étain-plomb", "isCorrect": True},
                        {"text": "Aluminium pur", "isCorrect": False},
                        {"text": "Cuivre rouge", "isCorrect": False},
                        {"text": "Acier doux", "isCorrect": False}
                    ],
                    "correction": "La soudure du zinc se fait à l'aide d'une baguette d'alliage étain (33%) et plomb (67%), fondant à une température inférieure à celle du zinc."
                },
                {
                    "questionNumber": 72,
                    "question": "Quelle est la largeur de recouvrement minimale pour une soudure à plat ?",
                    "answerOptions": [
                        {"text": "10 mm", "isCorrect": True},
                        {"text": "2 mm", "isCorrect": False},
                        {"text": "50 mm", "isCorrect": False},
                        {"text": "1 mm", "isCorrect": False}
                    ],
                    "correction": "Pour garantir la solidité mécanique de la jonction par capillarité, les feuilles de métal doivent se chevaucher d'au moins 10 mm sur une partie plane."
                },
                {
                    "questionNumber": 73,
                    "question": "Qu'est-ce qu'une 'naissance' en zinguerie ?",
                    "answerOptions": [
                        {"text": "La pièce de raccordement entre la gouttière et le tuyau de descente", "isCorrect": True},
                        {"text": "Le premier crochet posé en haut de la pente de la gouttière", "isCorrect": False},
                        {"text": "Le début d'une bande de plomb sur une cheminée", "isCorrect": False},
                        {"text": "L'outil servant à tracer les cercles sur le métal", "isCorrect": False}
                    ],
                    "correction": "La naissance (ou moignon) est l'élément soudé ou agrafé sur la gouttière pour diriger l'eau vers le tuyau de descente vertical."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est l'espacement maximal recommandé entre deux crochets de gouttière ?",
                    "answerOptions": [
                        {"text": "50 cm", "isCorrect": True},
                        {"text": "100 cm", "isCorrect": False},
                        {"text": "150 cm", "isCorrect": False},
                        {"text": "10 cm", "isCorrect": False}
                    ],
                    "correction": "Selon le DTU 40.5, les crochets doivent être espacés de 50 cm maximum pour soutenir le poids de la gouttière remplie d'eau (ou de neige/glace) sans qu'elle ne fléchisse."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel système de couverture zinc est privilégié pour les toitures à faible pente et grande surface ?",
                    "answerOptions": [
                        {"text": "Le joint debout", "isCorrect": True},
                        {"text": "La couverture à tasseaux", "isCorrect": False},
                        {"text": "La plaque ondulée", "isCorrect": False},
                        {"text": "La pose à clins", "isCorrect": False}
                    ],
                    "correction": "Le joint debout est une technique de sertissage mécanique des feuilles de zinc sur toute leur longueur. Elle offre une étanchéité parfaite même par vent fort et permet la dilatation libre."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle pièce assure l'étanchéité entre une cheminée et la toiture en partie haute (amont) ?",
                    "answerOptions": [
                        {"text": "La besace", "isCorrect": True},
                        {"text": "La bavette", "isCorrect": False},
                        {"text": "Le noquet", "isCorrect": False},
                        {"text": "Le solin", "isCorrect": False}
                    ],
                    "correction": "Derrière la cheminée (côté faîtage), l'eau s'accumule. On installe une 'besace' (ou dos d'âne) en zinc pour diviser le flux d'eau et le renvoyer de chaque côté de la souche."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle protection le couvreur doit-il utiliser lors de l'application d'acide chlorhydrique pur ?",
                    "answerOptions": [
                        {"text": "Gants et lunettes étanches", "isCorrect": True},
                        {"text": "Casque anti-bruit simple", "isCorrect": False},
                        {"text": "Chaussures de sécurité", "isCorrect": False},
                        {"text": "Ceinture de maintien", "isCorrect": False}
                    ],
                    "correction": "La préparation du décapant (zinc coupé à l'esprit de sel) dégage des vapeurs toxiques et le liquide est corrosif. La protection des yeux et des mains est vitale contre les brûlures chimiques."
                },
                {
                    "questionNumber": 78,
                    "question": "Qu'appelle-t-on 'le développé' d'une gouttière ?",
                    "answerOptions": [
                        {"text": "La largeur de la bande de métal avant façonnage", "isCorrect": True},
                        {"text": "La longueur totale de la toiture du bâtiment", "isCorrect": False},
                        {"text": "Le volume d'eau qu'elle peut contenir", "isCorrect": False},
                        {"text": "La distance entre deux descentes", "isCorrect": False}
                    ],
                    "correction": "Le développé (ex: DEV 25 ou DEV 33) correspond à la largeur de la feuille de zinc à plat nécessaire pour fabriquer le profil de la gouttière."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel accessoire termine une gouttière à ses extrémités ?",
                    "answerOptions": [
                        {"text": "Talon", "isCorrect": True},
                        {"text": "Coude", "isCorrect": False},
                        {"text": "Bague", "isCorrect": False},
                        {"text": "Clou", "isCorrect": False}
                    ],
                    "correction": "Le talon (ou fond de gouttière) est la pièce demi-circulaire ou plate soudée à l'extrémité de la gouttière pour fermer le profil et empêcher l'eau de sortir par le bout."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment fixe-t-on généralement un abergement de cheminée sur la souche en maçonnerie ?",
                    "answerOptions": [
                        {"text": "Bande de porte-solin vissée et joint mastic", "isCorrect": True},
                        {"text": "Simple collage au mortier ciment", "isCorrect": False},
                        {"text": "Clouage direct dans la brique creuse", "isCorrect": False},
                        {"text": "Pose libre sans aucune fixation", "isCorrect": False}
                    ],
                    "correction": "La partie supérieure (solin) est maintenue par une bande métallique (porte-solin) vissée mécaniquement dans la maçonnerie, avec un joint mastic (engravure) pour l'étanchéité à l'eau de ruissellement."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : LECTURE DE PLAN, CALEPINAGE ET GÉOMÉTRIE (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : LECTURE DE PLAN, CALEPINAGE ET GÉOMÉTRIE DE TOIT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la longueur réelle d'un mur mesurant 10 cm sur un plan à l'échelle 1/50 ?",
                    "answerOptions": [
                        {"text": "5 mètres", "isCorrect": True},
                        {"text": "50 mètres", "isCorrect": False},
                        {"text": "10 mètres", "isCorrect": False},
                        {"text": "1 mètre", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/50 signifie que 1 cm sur le plan égale 50 cm en réalité. Donc 10 cm x 50 = 500 cm, soit 5 mètres."
                },
                {
                    "questionNumber": 82,
                    "question": "À quoi correspond une pente de toit de 100 % ?",
                    "answerOptions": [
                        {"text": "45 degrés", "isCorrect": True},
                        {"text": "90 degrés", "isCorrect": False},
                        {"text": "100 degrés", "isCorrect": False},
                        {"text": "10 degrés", "isCorrect": False}
                    ],
                    "correction": "Une pente de 100 % signifie qu'on s'élève de 1 mètre verticalement pour 1 mètre horizontalement. Cela forme un triangle rectangle isocèle dont l'angle est de 45°."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel théorème de géométrie permet de calculer la longueur du rampant si l'on connaît la hauteur et la projection horizontale ?",
                    "answerOptions": [
                        {"text": "Pythagore", "isCorrect": True},
                        {"text": "Thalès", "isCorrect": False},
                        {"text": "Archimède", "isCorrect": False},
                        {"text": "Newton", "isCorrect": False}
                    ],
                    "correction": "Le triangle formé par la hauteur, la projection horizontale et le rampant est un triangle rectangle. Le théorème de Pythagore (a² + b² = c²) permet de calculer l'hypoténuse (le rampant)."
                },
                {
                    "questionNumber": 84,
                    "question": "Que représente la 'vue en plan' sur un dossier technique ?",
                    "answerOptions": [
                        {"text": "La toiture vue de dessus", "isCorrect": True},
                        {"text": "La toiture vue de face", "isCorrect": False},
                        {"text": "La charpente coupée au milieu", "isCorrect": False},
                        {"text": "Le détail du faîtage zoomé", "isCorrect": False}
                    ],
                    "correction": "La vue en plan est une projection horizontale géométrale, c'est-à-dire une représentation de l'ouvrage vu du dessus, 'à vol d'oiseau'."
                },
                {
                    "questionNumber": 85,
                    "question": "Qu'est-ce que le 'calepinage' avant la pose ?",
                    "answerOptions": [
                        {"text": "Le calcul de répartition des éléments pour éviter les coupes inutiles", "isCorrect": True},
                        {"text": "Le nettoyage complet du support de couverture", "isCorrect": False},
                        {"text": "La pose de l'isolant thermique entre les chevrons", "isCorrect": False},
                        {"text": "La mesure de la hauteur du bâtiment au laser", "isCorrect": False}
                    ],
                    "correction": "Le calepinage est l'étude préalable qui détermine le nombre de rangs et l'espacement exact (pureau) pour que la couverture tombe juste (sans coupe) à l'égout et au faîtage."
                },
                {
                    "questionNumber": 86,
                    "question": "Dans un cartouche de plan, que signifie le symbole d'une flèche pointant vers le haut avec la lettre N ?",
                    "answerOptions": [
                        {"text": "L'orientation Nord", "isCorrect": True},
                        {"text": "Le sens de la pente", "isCorrect": False},
                        {"text": "La direction du vent dominant", "isCorrect": False},
                        {"text": "Le point le plus haut du toit", "isCorrect": False}
                    ],
                    "correction": "Cette rose des vents simplifiée indique le Nord géographique, ce qui est essentiel pour déterminer l'exposition des versants aux intempéries."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment appelle-t-on la distance horizontale entre le mur de façade et l'aplomb du faîtage ?",
                    "answerOptions": [
                        {"text": "La projection horizontale", "isCorrect": True},
                        {"text": "Le rampant réel", "isCorrect": False},
                        {"text": "La hauteur sous flèche", "isCorrect": False},
                        {"text": "La longueur développée", "isCorrect": False}
                    ],
                    "correction": "La projection horizontale (ou base) est la distance au sol. Elle diffère de la longueur du rampant qui suit la pente du toit."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est la surface d'un versant rectangulaire de 10 mètres de long sur 6 mètres de rampant ?",
                    "answerOptions": [
                        {"text": "60 mètres carrés", "isCorrect": True},
                        {"text": "16 mètres carrés", "isCorrect": False},
                        {"text": "32 mètres carrés", "isCorrect": False},
                        {"text": "600 mètres carrés", "isCorrect": False}
                    ],
                    "correction": "La surface d'un rectangle se calcule par la formule : Longueur x Largeur (ici le rampant). Donc 10 x 6 = 60 m²."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel instrument simple permet de reporter un angle relevé sur le toit vers l'établi ?",
                    "answerOptions": [
                        {"text": "Fausse équerre", "isCorrect": True},
                        {"text": "Niveau à bulle", "isCorrect": False},
                        {"text": "Fil à plomb", "isCorrect": False},
                        {"text": "Pied à coulisse", "isCorrect": False}
                    ],
                    "correction": "La fausse équerre (ou sauterelle) possède une lame mobile qui permet de 'copier' un angle sur le chantier pour le tracer ensuite sur les matériaux à couper."
                },
                {
                    "questionNumber": 90,
                    "question": "Que désigne le terme 'rampant' en géométrie de toiture ?",
                    "answerOptions": [
                        {"text": "La longueur de la pente du toit", "isCorrect": True},
                        {"text": "La hauteur du mur pignon", "isCorrect": False},
                        {"text": "La largeur de la maison au sol", "isCorrect": False},
                        {"text": "L'épaisseur de l'isolant posé", "isCorrect": False}
                    ],
                    "correction": "Le rampant est la ligne de plus grande pente du versant. C'est la longueur réelle sur laquelle on pose les tuiles ou ardoises."
                },
                {
                    "questionNumber": 91,
                    "question": "Si un toit monte de 30 cm par mètre horizontal, quelle est sa pente ?",
                    "answerOptions": [
                        {"text": "30 %", "isCorrect": True},
                        {"text": "30 degrés", "isCorrect": False},
                        {"text": "3 degrés", "isCorrect": False},
                        {"text": "33 %", "isCorrect": False}
                    ],
                    "correction": "Le pourcentage de pente exprime la dénivellation en centimètres pour une distance horizontale de 100 cm (1 mètre). 30 cm pour 1 m correspond donc exactement à 30 %."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle ligne est perpendiculaire aux courbes de niveau et indique le chemin de l'eau ?",
                    "answerOptions": [
                        {"text": "La ligne de plus grande pente", "isCorrect": True},
                        {"text": "La ligne de traîne", "isCorrect": False},
                        {"text": "La ligne de bris", "isCorrect": False},
                        {"text": "La ligne de rive", "isCorrect": False}
                    ],
                    "correction": "L'eau suit toujours la ligne de plus grande pente sous l'effet de la gravité. Cette ligne est géométriquement perpendiculaire aux lignes horizontales (faîtage/égout)."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel type de trait utilise-t-on sur un plan pour représenter les parties cachées ?",
                    "answerOptions": [
                        {"text": "Trait interrompu court", "isCorrect": True},
                        {"text": "Trait continu fort", "isCorrect": False},
                        {"text": "Trait mixte fin", "isCorrect": False},
                        {"text": "Trait ondulé", "isCorrect": False}
                    ],
                    "correction": "En dessin technique normalisé, les arêtes cachées (ce qui est derrière ou dessous) se dessinent toujours en traits interrompus (pointillés)."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment nomme-t-on le petit versant triangulaire qui remplace le pignon à l'extrémité d'un toit ?",
                    "answerOptions": [
                        {"text": "Croupe", "isCorrect": True},
                        {"text": "Lucarne", "isCorrect": False},
                        {"text": "Coyau", "isCorrect": False},
                        {"text": "Outreau", "isCorrect": False}
                    ],
                    "correction": "Une croupe est un pan de toiture, généralement triangulaire, situé à l'extrémité d'un comble à deux versants, remplaçant la partie haute du pignon."
                },
                {
                    "questionNumber": 95,
                    "question": "Pour calculer la quantité d'ardoises, pourquoi ajoute-t-on un coefficient de perte ?",
                    "answerOptions": [
                        {"text": "Pour anticiper la casse et les coupes", "isCorrect": True},
                        {"text": "Pour augmenter la facture du client", "isCorrect": False},
                        {"text": "Pour avoir du stock pour l'année prochaine", "isCorrect": False},
                        {"text": "Pour isoler le plancher des combles", "isCorrect": False}
                    ],
                    "correction": "Lors des découpes (rives, noues, faîtages) et du transport, de la matière est perdue ou cassée. On ajoute généralement 5% à 10% de marge de sécurité."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle vue permet de visualiser les épaisseurs des matériaux (isolant, liteaux, chevrons) ?",
                    "answerOptions": [
                        {"text": "La coupe verticale", "isCorrect": True},
                        {"text": "Le plan de situation", "isCorrect": False},
                        {"text": "La vue de dessus", "isCorrect": False},
                        {"text": "La façade nord", "isCorrect": False}
                    ],
                    "correction": "La coupe (section verticale) tranche le bâtiment pour montrer la superposition des couches et les détails d'assemblage invisibles sur les autres vues."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le nom du trait tracé perpendiculairement à l'égout pour guider la pose ?",
                    "answerOptions": [
                        {"text": "Le trait carré", "isCorrect": True},
                        {"text": "Le trait de niveau", "isCorrect": False},
                        {"text": "Le trait de Jupiter", "isCorrect": False},
                        {"text": "Le trait oblique", "isCorrect": False}
                    ],
                    "correction": "Le trait carré est une ligne tracée au cordeau perpendiculairement à l'égout. Il sert de référence verticale pour aligner les rangs de tuiles ou d'ardoises (notamment pour les joints)."
                },
                {
                    "questionNumber": 98,
                    "question": "Combien de millimètres y a-t-il dans 2,40 mètres ?",
                    "answerOptions": [
                        {"text": "2400 mm", "isCorrect": True},
                        {"text": "240 mm", "isCorrect": False},
                        {"text": "24 mm", "isCorrect": False},
                        {"text": "24000 mm", "isCorrect": False}
                    ],
                    "correction": "1 mètre = 1000 millimètres. Donc 2,40 m multiplié par 1000 donne 2400 mm. La maîtrise des conversions est vitale pour la lecture de plan."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle forme géométrique a généralement une 'tourelle' en couverture ?",
                    "answerOptions": [
                        {"text": "Conique", "isCorrect": True},
                        {"text": "Cubique", "isCorrect": False},
                        {"text": "Plate", "isCorrect": False},
                        {"text": "Triangulaire", "isCorrect": False}
                    ],
                    "correction": "Les tourelles ont souvent une base circulaire et un toit en forme de cône, ce qui demande une technique de couverture spécifique (gironnage des ardoises)."
                },
                {
                    "questionNumber": 100,
                    "question": "Sur un plan, qu'indique la 'cotation' ?",
                    "answerOptions": [
                        {"text": "Les dimensions réelles de l'ouvrage", "isCorrect": True},
                        {"text": "Le prix des matériaux au mètre carré", "isCorrect": False},
                        {"text": "Le nom de l'architecte", "isCorrect": False},
                        {"text": "La date de fin de chantier", "isCorrect": False}
                    ],
                    "correction": "La cotation (les chiffres fléchés) indique toujours les dimensions réelles (cotes) de l'objet, quelle que soit l'échelle du dessin imprimé."
                },
            ]
        }
    }
}