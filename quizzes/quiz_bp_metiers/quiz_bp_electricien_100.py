quiz_data = {
    "title": "Quiz BP Électricien (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : NORMES, SÉCURITÉ ÉLECTRIQUE ET HABILITATIONS (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : NORMES, SÉCURITÉ ÉLECTRIQUE ET HABILITATIONS",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la première étape obligatoire d'une procédure de consignation électrique ?",
                    "answerOptions": [
                        {"text": "La séparation", "isCorrect": True},
                        {"text": "La condamnation mécanique de l'organe", "isCorrect": False},
                        {"text": "La vérification d'absence de tension", "isCorrect": False},
                        {"text": "La mise en court-circuit du tronçon", "isCorrect": False}
                    ],
                    "correction": "La consignation complète comprend cinq étapes. La toute première est la séparation, qui consiste à isoler l'installation de toutes les sources de tension (ouverture d'un disjoncteur ou sectionneur)."
                },
                {
                    "questionNumber": 2,
                    "question": "Dans une salle de bain, quel équipement est strictement autorisé dans le volume 1 ?",
                    "answerOptions": [
                        {"text": "Un chauffe-eau instantané de classe II", "isCorrect": True},
                        {"text": "Une prise de courant avec terre classique", "isCorrect": False},
                        {"text": "Un luminaire halogène de classe I", "isCorrect": False},
                        {"text": "Un lave-linge protégé par un différentiel", "isCorrect": False}
                    ],
                    "correction": "Selon la norme NF C 15-100, le volume 1 n'autorise que des chauffe-eau (instantanés ou à accumulation) de classe II protégés par un dispositif différentiel 30 mA. Les prises de courant et luminaires classiques y sont proscrits."
                },
                {
                    "questionNumber": 3,
                    "question": "Que permet de réaliser spécifiquement une habilitation de type BR ?",
                    "answerOptions": [
                        {"text": "Réaliser des interventions générales de dépannage", "isCorrect": True},
                        {"text": "Diriger une équipe de monteurs pour des travaux neufs", "isCorrect": False},
                        {"text": "Consigner une armoire électrique pour le compte de tiers", "isCorrect": False},
                        {"text": "Nettoyer des cellules haute tension sous tension nominale", "isCorrect": False}
                    ],
                    "correction": "Le Chargé d'intervention générale (BR) est habilité à intervenir seul pour dépanner, effectuer des mesures, remplacer un composant et s'auto-consigner un circuit en basse tension."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment détermine-t-on la section du conducteur principal de protection selon la norme NF C 15-100 ?",
                    "answerOptions": [
                        {"text": "Elle doit être au moins égale à celle des conducteurs de phase pour une section allant jusqu'à seize millimètres carrés", "isCorrect": True},
                        {"text": "Elle correspond toujours très exactement à la moitié de la section du conducteur de neutre quel que soit le régime de neutre", "isCorrect": False},
                        {"text": "Elle se calcule en multipliant l'ampérage du disjoncteur de branchement par un coefficient thermique spécifique lié à l'isolant", "isCorrect": False},
                        {"text": "Elle doit être strictement supérieure à vingt-cinq millimètres carrés dès lors que la liaison équipotentielle principale relie des canalisations métalliques d'eau et de gaz de grand diamètre", "isCorrect": False}
                    ],
                    "correction": "La norme impose que le conducteur de terre principal ait une section égale à celle de la phase jusqu'à 16 mm², puis 16 mm² pour une phase entre 16 et 35 mm², et la moitié de la phase au-delà."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la tension limite conventionnelle de sécurité en milieu sec en courant alternatif ?",
                    "answerOptions": [
                        {"text": "Cinquante volts", "isCorrect": True},
                        {"text": "Douze volts", "isCorrect": False},
                        {"text": "Vingt-quatre volts", "isCorrect": False},
                        {"text": "Cent vingt volts", "isCorrect": False}
                    ],
                    "correction": "La limite de la Très Basse Tension de Sécurité (TBTS) en courant alternatif et en environnement sec est fixée à 50 V. En environnement humide, ce seuil de dangerosité descend à 25 V."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel équipement doit obligatoirement être utilisé pour réaliser une Vérification d'Absence de Tension ?",
                    "answerOptions": [
                        {"text": "Détecteur normé", "isCorrect": True},
                        {"text": "Multimètre numérique classique", "isCorrect": False},
                        {"text": "Tournevis testeur lumineux", "isCorrect": False},
                        {"text": "Pince ampèremétrique multifonction", "isCorrect": False}
                    ],
                    "correction": "Le Vérificateur d'Absence de Tension (VAT) répond à une norme stricte garantissant son fonctionnement même avec une pile déchargée. L'utilisation d'un multimètre classique est une faute de sécurité éliminatoire."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel équipement de protection est vital lors d'une manœuvre de séparation ou d'une VAT en basse tension ?",
                    "answerOptions": [
                        {"text": "Des gants isolants et un écran facial", "isCorrect": True},
                        {"text": "Un tablier en plomb haute densité", "isCorrect": False},
                        {"text": "Des chaussures antistatiques conductrices", "isCorrect": False},
                        {"text": "Un masque respiratoire à cartouche filtrante", "isCorrect": False}
                    ],
                    "correction": "Face au risque d'électrisation par contact direct et de brûlure grave par arc électrique lors d'un éventuel court-circuit, le port de gants isolants adaptés à la tension et d'une visière faciale anti-projection est obligatoire."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est le rôle principal d'un dispositif différentiel à courant résiduel de trente milliampères ?",
                    "answerOptions": [
                        {"text": "Assurer la protection des personnes contre les contacts indirects et les contacts directs défaillants", "isCorrect": True},
                        {"text": "Empêcher la destruction des câbles électriques en coupant l'alimentation lors d'une surcharge prolongée", "isCorrect": False},
                        {"text": "Protéger le réseau de distribution principal contre les baisses soudaines de tension causées par le démarrage de gros moteurs", "isCorrect": False},
                        {"text": "Garantir une isolation galvanique absolue entre le transformateur du fournisseur d'énergie et l'ensemble des équipements domotiques du tableau d'abonné afin d'éviter les surtensions transitoires liées à la foudre", "isCorrect": False}
                    ],
                    "correction": "Le DDR 30 mA est conçu pour sauver des vies. Il détecte les fuites de courant vers la terre et coupe le circuit instantanément avant que l'électrisation ou le choc électrique ne devienne mortel."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle est la fonction d'un interrupteur différentiel par rapport à un disjoncteur différentiel ?",
                    "answerOptions": [
                        {"text": "Il ne protège pas contre les surintensités", "isCorrect": True},
                        {"text": "Il déclenche uniquement sur court-circuit", "isCorrect": False},
                        {"text": "Il régule la tension d'alimentation", "isCorrect": False},
                        {"text": "Il inverse le sens du courant", "isCorrect": False}
                    ],
                    "correction": "L'interrupteur différentiel repère uniquement les défauts d'isolement (fuites à la terre). Il doit impérativement être associé à des disjoncteurs magnétothermiques en aval pour protéger les câbles contre les surcharges et les courts-circuits."
                },
                {
                    "questionNumber": 10,
                    "question": "Combien de socles de prises de courant maximum peut-on câbler sur un circuit en deux millimètres et demi carrés ?",
                    "answerOptions": [
                        {"text": "Douze prises", "isCorrect": True},
                        {"text": "Cinq prises", "isCorrect": False},
                        {"text": "Huit prises", "isCorrect": False},
                        {"text": "Vingt prises", "isCorrect": False}
                    ],
                    "correction": "D'après les dernières révisions de la norme NF C 15-100, un circuit de prises de courant câblé en 2,5 mm² et protégé par un disjoncteur de 20 A maximum peut alimenter jusqu'à 12 socles de prises."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel composant est imposé par la norme pour le raccordement terminal d'un luminaire en plafond ?",
                    "answerOptions": [
                        {"text": "Boîtier DCL", "isCorrect": True},
                        {"text": "Domino à vis classique", "isCorrect": False},
                        {"text": "Connecteur rapide Wago", "isCorrect": False},
                        {"text": "Douille voleuse ancienne", "isCorrect": False}
                    ],
                    "correction": "La norme impose la pose d'une boîte DCL (Dispositif de Connexion Luminaire) intégrant une douille enfichable. Ce système empêche l'utilisateur d'entrer en contact avec des fils nus lorsqu'il change une suspension ou une ampoule."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelles sont les limites d'intervention d'un chargé de travaux habilité B2 ?",
                    "answerOptions": [
                        {"text": "Il dirige des travaux d'ordre électrique hors tension et supervise la sécurité de son équipe", "isCorrect": True},
                        {"text": "Il réalise la consignation complète de l'installation puis procède aux travaux sous tension nominale", "isCorrect": False},
                        {"text": "Il effectue le remplacement de relais thermiques en armoire industrielle sans devoir couper la puissance", "isCorrect": False},
                        {"text": "Il assure la direction exclusive des chantiers haute tension en réalisant des essais diélectriques poussés sur les cellules de distribution primaire du réseau public de transport de l'électricité", "isCorrect": False}
                    ],
                    "correction": "Le chargé de travaux B2 est le chef de chantier électrique. Il encadre les exécutants (B1) pour des travaux d'ordre électrique obligatoirement réalisés hors tension, après avoir reçu l'attestation de consignation."
                },
                {
                    "questionNumber": 13,
                    "question": "Dans quel espace spécifique du logement est-il obligatoire de réaliser une liaison équipotentielle supplémentaire ?",
                    "answerOptions": [
                        {"text": "Dans chaque salle de bain ou salle d'eau", "isCorrect": True},
                        {"text": "Dans les combles perdus et non aménagés", "isCorrect": False},
                        {"text": "Dans le tableau de communication principal", "isCorrect": False},
                        {"text": "Autour de l'antenne de réception sur le toit", "isCorrect": False}
                    ],
                    "correction": "La Liaison Équipotentielle Supplémentaire (LES) interconnecte toutes les masses métalliques accessibles d'une salle d'eau (tuyaux d'eau, huisseries, bondes métalliques) au fil de terre pour supprimer tout risque de différence de potentiel électrique dangereuse."
                },
                {
                    "questionNumber": 14,
                    "question": "Que signifie exactement le sigle GTL dans une installation résidentielle ?",
                    "answerOptions": [
                        {"text": "Gaine Technique Logement", "isCorrect": True},
                        {"text": "Gestion Thermique Locale", "isCorrect": False},
                        {"text": "Générateur de Tension Lisse", "isCorrect": False},
                        {"text": "Groupe de Transfert Légal", "isCorrect": False}
                    ],
                    "correction": "La GTL regroupe tous les équipements de puissance, de commande et de communication du logement en un seul endroit. Elle accueille notamment le tableau de répartition électrique et le coffret de communication VDI."
                },
                {
                    "questionNumber": 15,
                    "question": "En très basse et basse tension, à quoi correspond précisément la Zone 4 d'environnement électrique ?",
                    "answerOptions": [
                        {"text": "Une zone délimitée située à moins de trente centimètres des pièces nues sous tension", "isCorrect": True},
                        {"text": "Une zone exclusivement réservée au stockage des équipements de protection individuelle et des extincteurs", "isCorrect": False},
                        {"text": "Une zone d'accès public libre située au-delà de trois mètres de l'armoire électrique principale", "isCorrect": False},
                        {"text": "Une zone délimitée de manière parfaitement étanche par un écran physique rigide afin de bloquer totalement la propagation d'un arc électrique lors d'un court-circuit massif sur le réseau de distribution principal", "isCorrect": False}
                    ],
                    "correction": "En basse tension, la Distance Limite de Voisinage Renforcé (DLVR) est fixée à 30 cm des pièces nues sous tension. Franchir cette limite fait entrer l'intervenant en Zone 4, exposant à un danger extrême nécessitant des mesures et habilitations très spécifiques."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le titre d'habilitation minimal pour un agent nettoyant un local électrique sans aucun risque de contact direct ?",
                    "answerOptions": [
                        {"text": "Titre B0", "isCorrect": True},
                        {"text": "Chargé BC", "isCorrect": False},
                        {"text": "Opérateur B1", "isCorrect": False},
                        {"text": "Superviseur B2V", "isCorrect": False}
                    ],
                    "correction": "L'habilitation B0 (exécutant d'ordre non électrique) permet à une personne non électricienne mais formée aux risques d'entrer dans un local électrique pour y effectuer des tâches simples comme le nettoyage, la maçonnerie ou la peinture."
                },
                {
                    "questionNumber": 17,
                    "question": "Qui a la stricte responsabilité de délivrer une attestation de consignation pour travaux ?",
                    "answerOptions": [
                        {"text": "Le chargé de consignation BC", "isCorrect": True},
                        {"text": "Le chargé d'exploitation du site", "isCorrect": False},
                        {"text": "Le chef d'établissement uniquement", "isCorrect": False},
                        {"text": "Le chargé d'intervention générale BR", "isCorrect": False}
                    ],
                    "correction": "Seul le chargé de consignation titulaire de l'habilitation BC est autorisé à réaliser les cinq étapes de consignation pour le compte de tiers, et à rédiger l'attestation remise au chargé de travaux B2."
                },
                {
                    "questionNumber": 18,
                    "question": "Pourquoi installe-t-on impérativement un interrupteur différentiel de type A sur le circuit dédié d'un lave-linge ?",
                    "answerOptions": [
                        {"text": "Pour détecter les courants de défaut à composante continue générés par l'électronique de puissance de l'appareil", "isCorrect": True},
                        {"text": "Pour retarder le déclenchement lors de l'appel de courant très important du moteur de brassage au démarrage", "isCorrect": False},
                        {"text": "Pour immuniser totalement le circuit contre la foudre et les microcoupures transitoires du fournisseur d'énergie", "isCorrect": False},
                        {"text": "Pour assurer une mesure constante de la puissance active consommée par la machine et remonter l'information directement au gestionnaire d'énergie situé dans la Gaine Technique Logement", "isCorrect": False}
                    ],
                    "correction": "Les appareils intégrant des cartes électroniques (lave-linge, plaques à induction, bornes de recharge) génèrent des fuites de courant continu en cas de défaut. Les différentiels de type AC sont aveuglés par le courant continu, rendant l'utilisation du type A obligatoire."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle puissance maximale théorique tolère un disjoncteur monophasé de seize ampères sous deux cent trente volts ?",
                    "answerOptions": [
                        {"text": "Trois mille six cents watts", "isCorrect": True},
                        {"text": "Deux mille deux cents watts", "isCorrect": False},
                        {"text": "Quatre mille six cents watts", "isCorrect": False},
                        {"text": "Sept mille trois cents watts", "isCorrect": False}
                    ],
                    "correction": "La puissance apparente se calcule par P = U x I. En multipliant une tension de 230 V par une intensité de 16 A, on obtient environ 3680 Watts, souvent arrondis à 3600 W dans les prescriptions de câblage."
                },
                {
                    "questionNumber": 20,
                    "question": "Que stipule la norme NF C 15-100 concernant le repérage des circuits à l'intérieur d'un tableau de répartition ?",
                    "answerOptions": [
                        {"text": "Chaque circuit doit être identifié clairement avec sa destination précise par un étiquetage lisible et pérenne", "isCorrect": True},
                        {"text": "Les repères doivent uniquement indiquer le calibre en ampères du disjoncteur sans mentionner la pièce desservie", "isCorrect": False},
                        {"text": "L'identification visuelle complète doit être validée par le fournisseur d'énergie lors de la pose du compteur Linky", "isCorrect": False},
                        {"text": "Le repérage n'est pas obligatoire si le tableau comporte moins d'une dizaine de départs protégés et que l'installation a été validée par un bureau de contrôle technique indépendant lors de la mise en service initiale", "isCorrect": False}
                    ],
                    "correction": "L'identification claire, exacte et durable de tous les circuits (par exemple avec la mention : \"Prises salon\", \"Éclairage chambre parentale\") est une exigence absolue de la norme pour faciliter la maintenance et garantir la sécurité des personnes."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : DISTRIBUTION DE L'ÉNERGIE ET APPAREILLAGE DE PROTECTION (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : DISTRIBUTION DE L'ÉNERGIE ET APPAREILLAGE DE PROTECTION",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Comment appelle-t-on le régime de neutre où le neutre du transformateur est relié à la terre et les masses des utilisateurs à une autre terre ?",
                    "answerOptions": [
                        {"text": "Régime TT", "isCorrect": True},
                        {"text": "Régime TN", "isCorrect": False},
                        {"text": "Régime IT", "isCorrect": False},
                        {"text": "Régime TNC", "isCorrect": False}
                    ],
                    "correction": "En régime TT, la première lettre désigne le neutre de la source relié à la Terre. La deuxième lettre indique que les masses de l'installation sont reliées à une prise de Terre locale."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel composant protège spécifiquement les canalisations contre les surcharges et les courts-circuits ?",
                    "answerOptions": [
                        {"text": "Le disjoncteur magnétothermique", "isCorrect": True},
                        {"text": "Le contacteur de puissance", "isCorrect": False},
                        {"text": "L'interrupteur différentiel", "isCorrect": False},
                        {"text": "Le transformateur de séparation", "isCorrect": False}
                    ],
                    "correction": "Le disjoncteur magnétothermique associe un bilame thermique pour réagir aux surcharges lentes et une bobine magnétique pour réagir quasi-instantanément aux courts-circuits."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle valeur doit-on mesurer pour s'assurer de l'efficacité d'une prise de terre en régime TT ?",
                    "answerOptions": [
                        {"text": "Sa résistance en ohms", "isCorrect": True},
                        {"text": "Son intensité en ampères", "isCorrect": False},
                        {"text": "Sa tension en volts", "isCorrect": False},
                        {"text": "Sa puissance en watts", "isCorrect": False}
                    ],
                    "correction": "L'efficacité d'une prise de terre dépend directement de sa valeur ohmique. Pour garantir la sécurité avec un disjoncteur de branchement différentiel de 500 mA, cette résistance doit être inférieure à 100 ohms."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est l'avantage principal de la technique de filiation lors de la conception d'un tableau général basse tension ?",
                    "answerOptions": [
                        {"text": "Utiliser des disjoncteurs aval avec un pouvoir de coupure inférieur au courant de court-circuit présumé grâce à la limitation du disjoncteur amont", "isCorrect": True},
                        {"text": "Augmenter artificiellement la section des conducteurs de phase pour réduire la chute de tension globale sur les départs terminaux très éloignés du tableau principal", "isCorrect": False},
                        {"text": "Supprimer l'obligation d'installer des interrupteurs différentiels sur les circuits terminaux en regroupant toutes les protections sur un seul appareil de tête ultra sensible", "isCorrect": False},
                        {"text": "Permettre un déclenchement retardé et parfaitement chronologique de tous les départs divisionnaires afin de ne jamais interrompre le processus de production industrielle lors de la détection d'un courant de défaut d'isolement extrêmement violent", "isCorrect": False}
                    ],
                    "correction": "La filiation (ou protection en cascade) permet de réaliser d'importantes économies. Le disjoncteur amont limite l'énergie du court-circuit, ce qui autorise la pose de disjoncteurs moins coûteux et moins performants en aval."
                },
                {
                    "questionNumber": 25,
                    "question": "Dans un disjoncteur magnétothermique, que détecte le déclencheur magnétique ?",
                    "answerOptions": [
                        {"text": "Les courts-circuits", "isCorrect": True},
                        {"text": "Les surcharges lentes", "isCorrect": False},
                        {"text": "Les baisses de tension", "isCorrect": False},
                        {"text": "Les fuites à la terre", "isCorrect": False}
                    ],
                    "correction": "Le relais magnétique réagit instantanément à une augmentation brutale de l'intensité électromagnétique, caractéristique typique et dévastatrice d'un court-circuit."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel appareil de mesure permet de contrôler la valeur de la résistance d'une prise de terre ?",
                    "answerOptions": [
                        {"text": "Telluromètre", "isCorrect": True},
                        {"text": "Voltmètre", "isCorrect": False},
                        {"text": "Ampèremètre", "isCorrect": False},
                        {"text": "Oscilloscope", "isCorrect": False}
                    ],
                    "correction": "Le telluromètre, ou contrôleur de terre, est l'appareil spécifique conçu pour mesurer la résistance de la prise de terre, généralement via la méthode des trois piquets ou la méthode de boucle."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel régime de neutre assure la meilleure continuité de service au premier défaut d'isolement ?",
                    "answerOptions": [
                        {"text": "Le régime IT", "isCorrect": True},
                        {"text": "Le régime TT", "isCorrect": False},
                        {"text": "Le régime TNC", "isCorrect": False},
                        {"text": "Le régime TNS", "isCorrect": False}
                    ],
                    "correction": "En régime IT, le premier défaut d'isolement ne provoque pas de coupure de l'installation. Un Contrôleur Permanent d'Isolement signale le défaut. C'est indispensable dans les hôpitaux ou l'industrie critique."
                },
                {
                    "questionNumber": 28,
                    "question": "Que garantit une sélectivité ampèremétrique totale entre deux disjoncteurs montés en série ?",
                    "answerOptions": [
                        {"text": "Seul le disjoncteur amont au défaut déclenche sans faire disjoncter l'appareil de tête", "isCorrect": True},
                        {"text": "L'ensemble des disjoncteurs du tableau s'ouvre simultanément pour isoler complètement l'installation et éviter tout risque d'incendie électrique", "isCorrect": False},
                        {"text": "Le disjoncteur principal coupe l'alimentation avant les disjoncteurs divisionnaires pour protéger les contacteurs et les relais thermiques de l'armoire", "isCorrect": False},
                        {"text": "Le courant de court-circuit est automatiquement redirigé vers la prise de terre du bâtiment grâce à l'action combinée des varistances et des éclateurs à gaz installés dans le coffret de distribution principal de l'abonné", "isCorrect": False}
                    ],
                    "correction": "La sélectivité est essentielle pour la continuité de service. Elle permet de n'isoler que le circuit défaillant, maintenant ainsi l'alimentation électrique sur le reste de l'installation saine."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel paramètre caractérise la capacité d'un disjoncteur à interrompre un fort courant de court-circuit sans être détruit ?",
                    "answerOptions": [
                        {"text": "Le pouvoir de coupure", "isCorrect": True},
                        {"text": "Le calibre nominal", "isCorrect": False},
                        {"text": "La courbe de déclenchement", "isCorrect": False},
                        {"text": "La tension d'isolement", "isCorrect": False}
                    ],
                    "correction": "Le pouvoir de coupure, exprimé en kiloampères, définit le courant de court-circuit maximal que l'appareil est capable d'interrompre en toute sécurité sans provoquer d'arc persistant ni d'explosion."
                },
                {
                    "questionNumber": 30,
                    "question": "Sur quel type de courbe de déclenchement doit-on protéger le démarrage d'un moteur électrique standard ?",
                    "answerOptions": [
                        {"text": "Courbe D ou courbe K", "isCorrect": True},
                        {"text": "Courbe B ou courbe Z", "isCorrect": False},
                        {"text": "Courbe Z uniquement", "isCorrect": False},
                        {"text": "Courbe A uniquement", "isCorrect": False}
                    ],
                    "correction": "Les moteurs ont un fort appel de courant au démarrage. La courbe D, ou la courbe K pour les disjoncteurs moteurs, autorise une pointe d'intensité temporaire de dix à quatorze fois l'intensité nominale sans déclencher."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel paramètre provoque l'échauffement normal des câbles lorsqu'ils sont parcourus par un courant ?",
                    "answerOptions": [
                        {"text": "Effet Joule", "isCorrect": True},
                        {"text": "Effet Peltier", "isCorrect": False},
                        {"text": "Effet Seebeck", "isCorrect": False},
                        {"text": "Effet Hall", "isCorrect": False}
                    ],
                    "correction": "L'effet Joule est le dégagement de chaleur qui se produit lors du passage d'un courant électrique dans un conducteur présentant une résistance. Ce phénomène impose de bien dimensionner la section des câbles."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est la règle principale concernant le conducteur PEN en régime de neutre TNC ?",
                    "answerOptions": [
                        {"text": "Il combine les fonctions de neutre et de protection et sa section doit être au moins de dix millimètres carrés en cuivre", "isCorrect": True},
                        {"text": "Il sert uniquement à protéger les équipements contre les surtensions transitoires mais ne transporte jamais le courant de retour des récepteurs monophasés", "isCorrect": False},
                        {"text": "Il est strictement interdit de le raccorder directement à la carcasse métallique d'un moteur asynchrone triphasé sous peine de provoquer un déclenchement instantané", "isCorrect": False},
                        {"text": "Il doit être obligatoirement sectionné par un appareillage tétrapolaire lors de chaque intervention de maintenance pour garantir une séparation galvanique absolue de toutes les masses métalliques du bâtiment industriel", "isCorrect": False}
                    ],
                    "correction": "En régime TNC, le neutre et la terre sont confondus dans un seul conducteur appelé PEN. Pour des raisons de sécurité mécanique face au risque de rupture, la norme impose une section minimale de dix millimètres carrés en cuivre."
                },
                {
                    "questionNumber": 33,
                    "question": "Que signifie le sigle TGBT dans le domaine de la distribution d'énergie ?",
                    "answerOptions": [
                        {"text": "Tableau Général Basse Tension", "isCorrect": True},
                        {"text": "Transformateur Global Basse Tension", "isCorrect": False},
                        {"text": "Transmetteur Géré par Boucle de Terre", "isCorrect": False},
                        {"text": "Terminal de Gestion du Bâtiment Tertiaire", "isCorrect": False}
                    ],
                    "correction": "Le TGBT est l'armoire électrique principale d'un bâtiment. Il reçoit l'alimentation du transformateur ou du fournisseur, intègre les protections générales et distribue l'énergie vers les tableaux divisionnaires."
                },
                {
                    "questionNumber": 34,
                    "question": "En régime IT, quel dispositif signale immédiatement le premier défaut d'isolement ?",
                    "answerOptions": [
                        {"text": "Le contrôleur permanent d'isolement", "isCorrect": True},
                        {"text": "L'interrupteur différentiel", "isCorrect": False},
                        {"text": "Le relais de surveillance de phases", "isCorrect": False},
                        {"text": "Le disjoncteur magnétothermique", "isCorrect": False}
                    ],
                    "correction": "Le CPI (Contrôleur Permanent d'Isolement) injecte une très faible tension pour surveiller l'impédance de l'installation par rapport à la terre. En cas de premier défaut, il déclenche une alarme sonore ou visuelle."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel risque majeur impose la pose d'un parafoudre dans un tableau électrique situé dans une zone à forte densité de foudroiement ?",
                    "answerOptions": [
                        {"text": "Les surtensions transitoires d'origine atmosphérique capables de détruire les cartes électroniques sensibles", "isCorrect": True},
                        {"text": "L'élévation lente et continue de la tension du réseau public provoquant la surchauffe progressive des moteurs asynchrones", "isCorrect": False},
                        {"text": "La coupure accidentelle du fil de neutre par le fournisseur d'énergie entraînant une surcharge thermique sur l'ensemble du réseau", "isCorrect": False},
                        {"text": "La création d'un champ magnétique statique extrêmement puissant qui perturbe durablement le fonctionnement de tous les disjoncteurs différentiels haute sensibilité installés dans le logement", "isCorrect": False}
                    ],
                    "correction": "La foudre génère des surtensions transitoires très élevées et très brèves. Le parafoudre écrête cette pointe de tension destructrice en dérivant l'excédent d'énergie directement vers la terre."
                },
                {
                    "questionNumber": 36,
                    "question": "Comment appelle-t-on la chute de tension admissible exprimée en pourcentage entre l'origine de l'installation et le récepteur ?",
                    "answerOptions": [
                        {"text": "Delta U", "isCorrect": True},
                        {"text": "Cosinus Phi", "isCorrect": False},
                        {"text": "Facteur K", "isCorrect": False},
                        {"text": "Impédance Z", "isCorrect": False}
                    ],
                    "correction": "Delta U caractérise la chute de tension en ligne. La norme limite cette chute, par exemple à trois pour cent pour l'éclairage et cinq pour cent pour la force motrice, afin de garantir le bon fonctionnement des récepteurs."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel conducteur doit toujours être de couleur bleu clair dans une installation basse tension ?",
                    "answerOptions": [
                        {"text": "Le conducteur neutre", "isCorrect": True},
                        {"text": "Le conducteur de phase", "isCorrect": False},
                        {"text": "Le retour de lampe", "isCorrect": False},
                        {"text": "Le conducteur de protection", "isCorrect": False}
                    ],
                    "correction": "La norme NFC 15-100 impose formellement la couleur bleu clair pour identifier le fil de neutre. De même, la double coloration vert et jaune est strictement réservée au conducteur de protection."
                },
                {
                    "questionNumber": 38,
                    "question": "Pourquoi est-il interdit de sectionner le conducteur de protection PE dans un tableau électrique ?",
                    "answerOptions": [
                        {"text": "Il doit assurer l'écoulement permanent des courants de fuite vers la terre pour garantir la sécurité continue des usagers", "isCorrect": True},
                        {"text": "Il transporte le courant de déséquilibre du système triphasé et son ouverture provoquerait une surtension destructrice sur les appareils", "isCorrect": False},
                        {"text": "Il sert d'alimentation de secours pour les dispositifs d'éclairage de sécurité en cas de défaillance majeure du transformateur principal", "isCorrect": False},
                        {"text": "Il établit la communication numérique à haute fréquence entre le compteur d'énergie du fournisseur et les équipements de gestion tarifaire installés à l'intérieur de la gaine technique du logement", "isCorrect": False}
                    ],
                    "correction": "Le conducteur de protection (PE) est un fil de sécurité vitale. Son parcours doit être ininterrompu de la prise de terre jusqu'à la carcasse de l'appareil. Aucun organe de coupure n'est autorisé sur son trajet."
                },
                {
                    "questionNumber": 39,
                    "question": "Comment augmente-t-on le pouvoir de coupure apparent d'un disjoncteur par filiation ?",
                    "answerOptions": [
                        {"text": "En utilisant la limitation de courant offerte par le disjoncteur placé en amont", "isCorrect": True},
                        {"text": "En augmentant la section du câble raccordé à ses bornes de sortie", "isCorrect": False},
                        {"text": "En changeant sa courbe de déclenchement magnétique de C vers D", "isCorrect": False},
                        {"text": "En le raccordant en parallèle avec un autre disjoncteur identique", "isCorrect": False}
                    ],
                    "correction": "La filiation permet à un disjoncteur aval d'être protégé par le disjoncteur amont qui agit comme limiteur. Cela autorise la pose de disjoncteurs ayant un pouvoir de coupure nominal inférieur au courant de court-circuit présumé."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle condition est indispensable pour qu'une protection contre les contacts indirects soit efficace en régime TT ?",
                    "answerOptions": [
                        {"text": "La valeur de la prise de terre et la sensibilité du différentiel doivent être coordonnées selon une formule stricte", "isCorrect": True},
                        {"text": "L'ensemble des masses métalliques du bâtiment doit être totalement isolé de la terre pour empêcher la circulation des courants de défaut", "isCorrect": False},
                        {"text": "Le transformateur de distribution doit délivrer une tension strictement continue pour neutraliser les effets physiologiques du courant alternatif", "isCorrect": False},
                        {"text": "Le courant nominal de court-circuit doit être calculé de manière à faire fondre instantanément le conducteur principal de phase avant que l'usager ne touche la carcasse défectueuse de l'appareil électroménager", "isCorrect": False}
                    ],
                    "correction": "En régime TT, la sécurité des personnes est assurée par la coupure automatique. La règle fondamentale exige que la multiplication de la résistance de terre par la sensibilité du différentiel soit inférieure ou égale à la tension limite de sécurité."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : INSTALLATIONS RÉSIDENTIELLES, TERTIAAIRES ET RÉSEAUX DE COMMUNICATION (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : INSTALLATIONS RÉSIDENTIELLES, TERTIAIRES ET RÉSEAUX DE COMMUNICATION",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel protocole de communication filaire est le standard mondial pour la gestion intelligente de l'éclairage tertiaire ?",
                    "answerOptions": [
                        {"text": "DALI", "isCorrect": True},
                        {"text": "Modbus", "isCorrect": False},
                        {"text": "Ethernet", "isCorrect": False},
                        {"text": "Profibus", "isCorrect": False}
                    ],
                    "correction": "Le protocole DALI (Digital Addressable Lighting Interface) est la norme internationale pour le contrôle de l'éclairage, permettant d'adresser chaque luminaire de manière individuelle et de gérer la gradation."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle catégorie de câble à paires torsadées garantit un débit d'un Gigabit par seconde en réseau VDI ?",
                    "answerOptions": [
                        {"text": "Catégorie 5e ou supérieure", "isCorrect": True},
                        {"text": "Catégorie 3 sans aucun blindage", "isCorrect": False},
                        {"text": "Catégorie 1 pour la téléphonie analogique", "isCorrect": False},
                        {"text": "Câble coaxial de type télévision", "isCorrect": False}
                    ],
                    "correction": "La catégorie 5e (ou Catégorie 6) est le standard minimum certifié pour supporter la norme Gigabit Ethernet sur une longueur maximale de cent mètres."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la fonction principale d'un panneau de brassage dans un réseau de communication tertiaire ?",
                    "answerOptions": [
                        {"text": "Interconnecter les prises terminales murales des bureaux avec les équipements actifs du réseau comme les commutateurs", "isCorrect": True},
                        {"text": "Convertir systématiquement le courant alternatif du réseau principal en basse tension continue pour alimenter individuellement chaque ordinateur de bureau de l'entreprise", "isCorrect": False},
                        {"text": "Filtrer toutes les perturbations électromagnétiques de l'air ambiant de manière à garantir une vitesse de connexion à internet parfaitement constante même lors d'importants orages magnétiques estivaux", "isCorrect": False},
                        {"text": "Protéger le serveur central de la foudre en redirigeant l'intégralité du courant de court-circuit directement vers le piquet de terre situé à l'extérieur du bâtiment tertiaire", "isCorrect": False}
                    ],
                    "correction": "Le brassage offre une grande flexibilité au réseau VDI en reliant manuellement, via des cordons de brassage (patch cords), les arrivées de câbles des postes de travail aux ports du switch informatique."
                },
                {
                    "questionNumber": 44,
                    "question": "Que signifie l'acronyme GTB dans le domaine du bâtiment tertiaire intelligent ?",
                    "answerOptions": [
                        {"text": "Gestion Technique du Bâtiment", "isCorrect": True},
                        {"text": "Générateur Thermique Basse-tension", "isCorrect": False},
                        {"text": "Gaine Technologique Blindée", "isCorrect": False},
                        {"text": "Groupement Terminal de Brassage", "isCorrect": False}
                    ],
                    "correction": "La GTB est le système informatique qui permet de superviser, d'automatiser et de piloter l'ensemble des lots techniques d'un bâtiment (CVC, éclairage, alarmes, accès) pour optimiser l'énergie."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel support physique est utilisé pour amener le très haut débit directement dans un logement neuf (FTTH) ?",
                    "answerOptions": [
                        {"text": "Fibre optique", "isCorrect": True},
                        {"text": "Fil de cuivre", "isCorrect": False},
                        {"text": "Câble coaxial", "isCorrect": False},
                        {"text": "Faisceau hertzien", "isCorrect": False}
                    ],
                    "correction": "Le réseau FTTH (Fiber To The Home) utilise la fibre optique pour transmettre les données sous forme de signal lumineux, offrant des débits asymétriques ou symétriques largement supérieurs au réseau cuivre."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel bus de terrain filaire décentralisé est la référence mondiale en domotique et immotique ?",
                    "answerOptions": [
                        {"text": "Le protocole KNX", "isCorrect": True},
                        {"text": "La liaison série RS232", "isCorrect": False},
                        {"text": "Le réseau WiFi domestique", "isCorrect": False},
                        {"text": "Le bus de terrain CAN", "isCorrect": False}
                    ],
                    "correction": "KNX est le standard ouvert mondial pour la domotique. Il repose généralement sur un câble bus à paire torsadée verte qui fait communiquer en réseau tous les capteurs (boutons) et actionneurs de l'installation."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est l'avantage technologique majeur du système PoE sur un réseau informatique ?",
                    "answerOptions": [
                        {"text": "Alimenter électriquement un équipement réseau via le même câble Ethernet qui transporte les données", "isCorrect": True},
                        {"text": "Doubler instantanément la bande passante globale de la connexion internet de l'entreprise en superposant deux fréquences optiques sur le même fil", "isCorrect": False},
                        {"text": "Sécuriser totalement les données en cryptant chaque paquet d'information à la source à l'aide d'un algorithme de chiffrement militaire indéchiffrable par les pirates informatiques", "isCorrect": False},
                        {"text": "Empêcher la surchauffe des baies de brassage en injectant un gaz réfrigérant inerte à l'intérieur de la gaine de protection en plastique du câble réseau", "isCorrect": False}
                    ],
                    "correction": "Le Power Over Ethernet (PoE) permet d'alimenter directement des téléphones IP, des caméras de sécurité ou des bornes WiFi par le câble RJ45, supprimant la nécessité de poser des prises de courant classiques à côté."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la longueur maximale normalisée pour une liaison Ethernet sur câble à paires torsadées en cuivre ?",
                    "answerOptions": [
                        {"text": "Cent mètres", "isCorrect": True},
                        {"text": "Trente mètres", "isCorrect": False},
                        {"text": "Cinq cents mètres", "isCorrect": False},
                        {"text": "Un kilomètre", "isCorrect": False}
                    ],
                    "correction": "La norme ISO/IEC 11801 impose une longueur maximale de 100 mètres pour un canal complet (90 mètres de câble permanent rigide dans les murs, plus 10 mètres de cordons souples) pour garantir l'intégrité du signal."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel équipement actif interconnecte de multiples appareils sur un réseau local pour distribuer la connexion ?",
                    "answerOptions": [
                        {"text": "Le commutateur réseau ou switch", "isCorrect": True},
                        {"text": "Le bloc d'alimentation secourue", "isCorrect": False},
                        {"text": "La passerelle de téléphonie fixe", "isCorrect": False},
                        {"text": "Le régulateur de tension électronique", "isCorrect": False}
                    ],
                    "correction": "Le switch (commutateur) relie physiquement les différents équipements du réseau local (LAN). Contrairement à un simple hub, il achemine les trames de données de manière intelligente uniquement vers le bon destinataire."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel rôle joue le Dispositif de Terminaison Intérieur dans un coffret de communication résidentiel ?",
                    "answerOptions": [
                        {"text": "Marquer la séparation officielle et le point de test entre le réseau public de l'opérateur et l'installation privée de l'abonné", "isCorrect": True},
                        {"text": "Répartir le courant fort en provenance du disjoncteur d'abonné vers tous les départs de lumière et de prises de la maison de manière parfaitement équilibrée et sécurisée", "isCorrect": False},
                        {"text": "Amplifier considérablement le signal de réception de l'antenne râteau installée sur le toit du bâtiment pour garantir une image haute définition sur tous les téléviseurs", "isCorrect": False},
                        {"text": "Transformer le signal optique très haut débit en un signal analogique basse fréquence pour que les vieux téléphones à cadran rotatif puissent fonctionner normalement", "isCorrect": False}
                    ],
                    "correction": "Le DTI (réseau cuivre) ou le PTO (réseau fibre) définit la frontière juridique entre la responsabilité du fournisseur d'accès internet (réseau extérieur) et celle du propriétaire du logement (câblage intérieur)."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel composant mural sert de terminaison physique au réseau de fibre optique à l'intérieur du logement ?",
                    "answerOptions": [
                        {"text": "PTO", "isCorrect": True},
                        {"text": "DTI", "isCorrect": False},
                        {"text": "VDI", "isCorrect": False},
                        {"text": "RJ45", "isCorrect": False}
                    ],
                    "correction": "La Prise Terminale Optique (ou Point de Terminaison Optique) est le petit boîtier soudé en fin de ligne optique, sur lequel le client vient brancher sa box internet via une jarretière optique."
                },
                {
                    "questionNumber": 52,
                    "question": "Que signifie l'appellation FTP pour la protection d'un câble informatique de communication ?",
                    "answerOptions": [
                        {"text": "L'ensemble des quatre paires est entouré d'un écran général en feuille d'aluminium", "isCorrect": True},
                        {"text": "Chaque paire torsadée est protégée individuellement par une tresse en cuivre", "isCorrect": False},
                        {"text": "Le câble ne possède absolument aucun écran de protection électromagnétique", "isCorrect": False},
                        {"text": "Les fils sont plongés dans un gel isolant spécifique contre l'humidité", "isCorrect": False}
                    ],
                    "correction": "Le sigle FTP (Foiled Twisted Pair ou F/UTP) indique que le câble possède un blindage global en feuillard d'aluminium sous la gaine extérieure, protégeant le signal contre les parasites électromagnétiques."
                },
                {
                    "questionNumber": 53,
                    "question": "Comment un radiateur électrique reçoit-il ses ordres de programmation tarifaire dans une installation classique ?",
                    "answerOptions": [
                        {"text": "Via le raccordement du fil pilote", "isCorrect": True},
                        {"text": "Uniquement par son thermostat mécanique", "isCorrect": False},
                        {"text": "Par le câble vert et jaune de mise à la terre", "isCorrect": False},
                        {"text": "Par la variation brutale de la tension de phase", "isCorrect": False}
                    ],
                    "correction": "Le fil pilote est un conducteur noir de commande. Il transmet des signaux électriques normalisés (confort, éco, hors gel, arrêt) pour piloter le radiateur à distance depuis un programmateur ou un gestionnaire d'énergie."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le principal avantage de l'utilisation d'un protocole domotique radio de type Zigbee en rénovation ?",
                    "answerOptions": [
                        {"text": "Éviter le passage de nouveaux câbles de commande et la dégradation des murs existants", "isCorrect": True},
                        {"text": "Garantir une alimentation électrique continue des radiateurs de forte puissance sans devoir modifier la section des câbles enfouis dans les cloisons en plaques de plâtre", "isCorrect": False},
                        {"text": "Permettre une connexion directe et filaire avec le compteur communicant Linky pour obliger les appareils électroménagers à fonctionner exclusivement la nuit de manière automatique", "isCorrect": False},
                        {"text": "Supprimer totalement la nécessité d'installer un tableau de répartition électrique principal en raccordant les appareils directement aux ondes électromagnétiques captées depuis l'extérieur du logement", "isCorrect": False}
                    ],
                    "correction": "Les technologies sans fil (Zigbee, EnOcean, Z-Wave) communiquent par ondes radio à travers les cloisons. C'est l'atout majeur en rénovation : on peut ajouter des interrupteurs ou capteurs connectés sans réaliser aucune saignée ni passage de gaine."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est l'unité de mesure du flux lumineux total émis par une source d'éclairage LED ?",
                    "answerOptions": [
                        {"text": "Lumen", "isCorrect": True},
                        {"text": "Lux", "isCorrect": False},
                        {"text": "Candela", "isCorrect": False},
                        {"text": "Watt", "isCorrect": False}
                    ],
                    "correction": "Le lumen (lm) mesure la quantité totale de lumière visible émise par une lampe dans toutes les directions. C'est l'indicateur principal de la puissance d'éclairage d'une ampoule LED."
                },
                {
                    "questionNumber": 56,
                    "question": "En éclairagisme, que mesure très précisément l'éclairement exprimé en Lux ?",
                    "answerOptions": [
                        {"text": "Le flux lumineux reçu par unité de surface", "isCorrect": True},
                        {"text": "La température de couleur de la source lumineuse", "isCorrect": False},
                        {"text": "La consommation électrique globale de l'ampoule", "isCorrect": False},
                        {"text": "L'éblouissement inconfortable provoqué par le luminaire", "isCorrect": False}
                    ],
                    "correction": "Le lux (lx) est l'unité d'éclairement mesurant la lumière qui arrive sur un plan de travail. Un lux correspond à un lumen réparti sur un mètre carré. La norme de travail impose par exemple 500 lux sur un bureau informatique."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle est la différence majeure d'architecture entre une Gestion Technique du Bâtiment et une Gestion Technique Centralisée ?",
                    "answerOptions": [
                        {"text": "La GTC supervise un seul lot technique spécifique alors que la GTB intègre et fédère l'ensemble des installations du bâtiment", "isCorrect": True},
                        {"text": "La GTC est exclusivement réservée aux bâtiments résidentiels de très petite taille tandis que la GTB est une technologie militaire utilisée uniquement pour sécuriser les bases de données gouvernementales", "isCorrect": False},
                        {"text": "La GTC nécessite impérativement une connexion permanente par câble sous-marin en fibre optique pour fonctionner correctement en cas de panne généralisée du réseau de distribution électrique", "isCorrect": False},
                        {"text": "La GTC contrôle uniquement la production d'énergie solaire photovoltaïque en toiture afin d'injecter la totalité de l'électricité sur le réseau public lors des pointes de forte consommation hivernale", "isCorrect": False}
                    ],
                    "correction": "Une GTC pilote une fonction unique (par exemple : uniquement la chaufferie ou uniquement l'éclairage). Une GTB, via un système de supervision global, fédère toutes les GTC et les fait communiquer entre elles pour un bâtiment totalement intelligent."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel appareil est indispensable pour certifier les performances à haute fréquence d'un câblage informatique RJ45 neuf ?",
                    "answerOptions": [
                        {"text": "Un certificateur de câblage LAN", "isCorrect": True},
                        {"text": "Un simple testeur de continuité sonore", "isCorrect": False},
                        {"text": "Un mégohmmètre réglé sous cinq cents volts", "isCorrect": False},
                        {"text": "Un analyseur de réseau électrique triphasé", "isCorrect": False}
                    ],
                    "correction": "Contrairement à un simple testeur de continuité, le certificateur de réseau garantit que la prise installée respecte les normes de catégorie (Cat 6, Cat 6A) en mesurant des paramètres complexes comme la diaphonie et l'atténuation du signal."
                },
                {
                    "questionNumber": 59,
                    "question": "Que signifie l'acronyme IRVE dans le cadre de l'évolution des infrastructures de stationnement ?",
                    "answerOptions": [
                        {"text": "Infrastructure de Recharge de Véhicules Électriques", "isCorrect": True},
                        {"text": "Installation de Relais pour Ventilation Extérieure", "isCorrect": False},
                        {"text": "Interrupteur Régulé par Valeur Électronique", "isCorrect": False},
                        {"text": "Indicateur de Risque Voltamétrique Externe", "isCorrect": False}
                    ],
                    "correction": "Les IRVE désignent l'ensemble des bornes de recharge, câblages de puissance et dispositifs de protection différentielle liés à la mobilité électrique. Leur installation au-delà d'une certaine puissance requiert une qualification professionnelle spécifique."
                },
                {
                    "questionNumber": 60,
                    "question": "En gestion de l'éclairage, pourquoi privilégier un détecteur de présence plutôt qu'un détecteur de mouvement classique au-dessus d'un poste de travail ?",
                    "answerOptions": [
                        {"text": "Il possède une haute sensibilité repérant les micro-mouvements de travail tout en mesurant la luminosité naturelle en continu", "isCorrect": True},
                        {"text": "Il intègre une puissante caméra de vidéosurveillance cachée qui enregistre l'ensemble des activités des employés et les transmet en temps réel sur les serveurs de la direction des ressources humaines", "isCorrect": False},
                        {"text": "Il déclenche instantanément une alarme anti-intrusion assourdissante dès qu'une personne pénètre dans le local technique sécurisé en dehors des plages horaires de travail autorisées", "isCorrect": False},
                        {"text": "Il consomme une quantité d'énergie beaucoup moins importante car il ne fonctionne qu'une fois par jour lors de la mise en route initiale du chauffage central du bâtiment", "isCorrect": False}
                    ],
                    "correction": "Un détecteur de présence est très sensible : il maintient la lumière allumée même avec des mouvements minimes (frappe au clavier). De plus, sa cellule crépusculaire intégrée éteint la lumière artificielle dès que l'apport de lumière du jour suffit, maximisant ainsi les économies d'énergie."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : ÉQUIPEMENTS INDUSTRIELS ET FORCE MOTRICE (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ÉQUIPEMENTS INDUSTRIELS ET FORCE MOTRICE",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est l'organe électromécanique de puissance permettant d'établir ou d'interrompre à distance le courant vers un moteur industriel ?",
                    "answerOptions": [
                        {"text": "Le contacteur", "isCorrect": True},
                        {"text": "Le sectionneur porte-fusibles", "isCorrect": False},
                        {"text": "Le disjoncteur différentiel", "isCorrect": False},
                        {"text": "Le bouton-poussoir d'arrêt", "isCorrect": False}
                    ],
                    "correction": "Le contacteur est un relais électromagnétique conçu pour commuter des courants de très forte puissance (le moteur) sous l'action d'un circuit de commande de très faible puissance actionné par l'opérateur ou un automate."
                },
                {
                    "questionNumber": 62,
                    "question": "Contre quel type de défaut électrique le relais thermique protège-t-il spécifiquement un moteur asynchrone ?",
                    "answerOptions": [
                        {"text": "Les surcharges faibles et prolongées", "isCorrect": True},
                        {"text": "Les courts-circuits francs et massifs", "isCorrect": False},
                        {"text": "Les baisses brutales de tension réseau", "isCorrect": False},
                        {"text": "Les fuites de courant vers la carcasse", "isCorrect": False}
                    ],
                    "correction": "Le relais thermique surveille le courant absorbé par le moteur. En cas de surcharge prolongée (comme un blocage mécanique), la chaleur dilate les bilames qui finissent par ouvrir le circuit de commande du contacteur pour stopper le moteur en sécurité."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la fonction première du sectionneur installé en tête d'un départ de moteur industriel ?",
                    "answerOptions": [
                        {"text": "Isoler visuellement le circuit de puissance pour la consignation électrique et protéger contre les courts-circuits grâce à ses fusibles", "isCorrect": True},
                        {"text": "Démarrer et arrêter le moteur asynchrone en pleine charge nominale lors des cycles de production intensifs fonctionnant de manière automatique jour et nuit", "isCorrect": False},
                        {"text": "Corriger le facteur de puissance de l'installation électrique industrielle afin d'éviter les pénalités de facturation appliquées par le fournisseur d'énergie sur la puissance réactive", "isCorrect": False},
                        {"text": "Inverser instantanément le sens de rotation de la machine outil en permutant automatiquement deux phases du réseau de distribution triphasé", "isCorrect": False}
                    ],
                    "correction": "Le sectionneur garantit une séparation omnipolaire bien visible, indispensable pour consigner la machine en toute sécurité. Ne possédant pas de pouvoir de coupure, sa poignée ne doit jamais être manœuvrée lorsque le moteur tourne. Ses fusibles intégrés assurent la protection magnétique."
                },
                {
                    "questionNumber": 64,
                    "question": "Sur la plaque d'un moteur, il est inscrit deux cent trente et quatre cents volts. Le réseau de l'usine est en quatre cents volts triphasé. Quel couplage réaliser ?",
                    "answerOptions": [
                        {"text": "Un couplage étoile", "isCorrect": True},
                        {"text": "Un couplage triangle", "isCorrect": False},
                        {"text": "Un couplage série", "isCorrect": False},
                        {"text": "Un couplage parallèle", "isCorrect": False}
                    ],
                    "correction": "Le réseau de l'usine correspond à la tension la plus haute indiquée sur la plaque signalétique du moteur. Le couplage étoile, réalisé avec des barrettes dans la boîte à bornes, permet de réduire la tension appliquée à chaque enroulement individuel à 230 V (400 V / √3)."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel équipement électronique de puissance permet de faire varier la vitesse de rotation d'un moteur asynchrone triphasé ?",
                    "answerOptions": [
                        {"text": "Variateur de fréquence", "isCorrect": True},
                        {"text": "Transformateur d'intensité", "isCorrect": False},
                        {"text": "Redresseur à pont de diodes", "isCorrect": False},
                        {"text": "Démarreur statorique à résistances", "isCorrect": False}
                    ],
                    "correction": "La vitesse de synchronisme d'un moteur asynchrone dépend proportionnellement de la fréquence électrique du réseau. Le variateur de fréquence modifie simultanément la fréquence et la tension pour contrôler la vitesse de rotation en douceur."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel type de matériau un capteur de proximité inductif industriel est-il capable de détecter ?",
                    "answerOptions": [
                        {"text": "Uniquement les cibles métalliques", "isCorrect": True},
                        {"text": "Exclusivement les matières plastiques", "isCorrect": False},
                        {"text": "Les objets en bois ou en carton isolant", "isCorrect": False},
                        {"text": "Tout type d'objet quel que soit sa matière", "isCorrect": False}
                    ],
                    "correction": "Le capteur inductif génère un champ magnétique oscillant haute fréquence. Seule l'approche d'une cible métallique (fer, acier, aluminium) crée des courants de Foucault qui perturbent ce champ et provoquent la commutation électrique du capteur."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est l'intérêt fondamental de la technique de démarrage étoile triangle pour un moteur asynchrone de forte puissance ?",
                    "answerOptions": [
                        {"text": "Réduire drastiquement la pointe de courant absorbé sur le réseau de distribution lors de la mise en rotation du rotor", "isCorrect": True},
                        {"text": "Augmenter massivement le couple mécanique de démarrage de la machine de manière à entraîner immédiatement des charges extrêmement lourdes bloquées au sol", "isCorrect": False},
                        {"text": "Empêcher le moteur de tourner dans le mauvais sens si le technicien a accidentellement inversé l'ordre des trois phases lors du raccordement dans la boîte à bornes", "isCorrect": False},
                        {"text": "Supprimer totalement l'obligation de raccorder la carcasse du moteur au réseau de terre général de l'usine industrielle pour réaliser une économie de fil de cuivre", "isCorrect": False}
                    ],
                    "correction": "Le démarrage direct d'un gros moteur asynchrone crée une pointe d'intensité énorme, atteignant six à huit fois le courant nominal. Le démarrage étoile-triangle abaisse artificiellement la tension appliquée aux enroulements, divisant ainsi l'appel de courant par trois et protégeant l'installation."
                },
                {
                    "questionNumber": 68,
                    "question": "En schématisation d'automatisme, que signifie un contact auxiliaire de type NO ?",
                    "answerOptions": [
                        {"text": "Normalement ouvert au repos", "isCorrect": True},
                        {"text": "Normalement opérationnel en charge", "isCorrect": False},
                        {"text": "Neutre orienté", "isCorrect": False},
                        {"text": "Négatif ouvert", "isCorrect": False}
                    ],
                    "correction": "NO signifie Normalement Ouvert (Normally Open en anglais). Le contact ne laisse passer le courant électrique que lorsque l'organe de commande (bouton ou bobine) est actionné, contrairement au contact NF (Normalement Fermé)."
                },
                {
                    "questionNumber": 69,
                    "question": "Comment définit-on le glissement de fonctionnement d'un moteur asynchrone ?",
                    "answerOptions": [
                        {"text": "L'écart entre la vitesse du champ magnétique tournant et la vitesse mécanique réelle du rotor", "isCorrect": True},
                        {"text": "La perte progressive d'adhérence de la courroie de transmission sur la poulie d'entraînement", "isCorrect": False},
                        {"text": "La différence de tension électrique mesurée entre l'entrée du disjoncteur et les bornes du stator", "isCorrect": False},
                        {"text": "L'usure naturelle des roulements à billes de l'arbre moteur après des milliers d'heures de rotation", "isCorrect": False}
                    ],
                    "correction": "Pour que le courant se crée dans le rotor (cage d'écureuil), celui-ci doit tourner un peu moins vite que le champ magnétique tournant créé par le stator. Ce léger retard de rotation s'appelle le glissement."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle formule mathématique permet de calculer la puissance active électrique absorbée par un moteur alimenté en triphasé équilibré ?",
                    "answerOptions": [
                        {"text": "Tension composée multipliée par intensité de ligne multipliée par racine de trois multipliée par cosinus phi", "isCorrect": True},
                        {"text": "Tension simple multipliée par intensité nominale multipliée par racine carrée de deux sans tenir compte du déphasage du courant", "isCorrect": False},
                        {"text": "Résistance interne du bobinage du stator multipliée par le carré de la fréquence nominale du réseau de distribution électrique", "isCorrect": False},
                        {"text": "Puissance réactive totale de l'installation divisée par le rendement mécanique global du système de transmission de la machine", "isCorrect": False}
                    ],
                    "correction": "En système alternatif triphasé équilibré, la puissance active s'exprime en Watts par la formule mathématique suivante : P = U (tension composée) × I (intensité) × √3 × cos(φ) (facteur de puissance)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel type de capteur utilise-t-on pour détecter la présence de liquide à travers la fine paroi d'une cuve en plastique ?",
                    "answerOptions": [
                        {"text": "Capteur capacitif", "isCorrect": True},
                        {"text": "Capteur inductif", "isCorrect": False},
                        {"text": "Capteur magnétique", "isCorrect": False},
                        {"text": "Fin de course", "isCorrect": False}
                    ],
                    "correction": "Le détecteur capacitif réagit à la modification de la capacité diélectrique de son environnement immédiat. Il est idéal pour détecter la présence de liquides, de poudres ou d'objets non métalliques, même à travers une paroi isolante mince."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le rôle d'un relais contrôleur d'ordre de phases dans le tableau d'une machine tournante ?",
                    "answerOptions": [
                        {"text": "Couper le circuit de commande si l'ordre des trois phases est inversé ou si une phase vient à manquer", "isCorrect": True},
                        {"text": "Ajuster automatiquement la tension du réseau de l'usine en cas de creux de tension prolongé", "isCorrect": False},
                        {"text": "Compter précisément le temps de fonctionnement total de la machine pour planifier la maintenance", "isCorrect": False},
                        {"text": "Transformer le courant alternatif triphasé en un courant continu lisse pour l'électronique de bord", "isCorrect": False}
                    ],
                    "correction": "Une inversion de phase au niveau de l'alimentation générale fera tourner un compresseur ou une pompe à l'envers, entraînant sa destruction mécanique très rapide. Le relais empêche le démarrage si le sens de rotation du champ n'est pas correct."
                },
                {
                    "questionNumber": 73,
                    "question": "À quoi sert une sonde CTP (thermistance) insérée au cœur des bobinages d'un moteur asynchrone ?",
                    "answerOptions": [
                        {"text": "Mesurer la température interne de l'enroulement pour stopper le moteur en cas d'échauffement critique", "isCorrect": True},
                        {"text": "Mesurer la vitesse de rotation exacte de l'axe central grâce à un champ magnétique pulsé", "isCorrect": False},
                        {"text": "Compenser automatiquement la perte de puissance réactive du moteur lors d'une charge faible", "isCorrect": False},
                        {"text": "Chauffer artificiellement le moteur en hiver pour empêcher la condensation de geler sur le rotor", "isCorrect": False}
                    ],
                    "correction": "La sonde à Coefficient de Température Positif (CTP) voit sa résistance augmenter de façon exponentielle lorsqu'elle atteint son seuil critique de température. Branchée sur un relais de protection dédié, elle déclenche la coupure d'urgence pour sauver le moteur."
                },
                {
                    "questionNumber": 74,
                    "question": "Pourquoi l'industrie procède-t-elle à l'installation d'armoires de batteries de condensateurs en tête de son réseau de distribution électrique ?",
                    "answerOptions": [
                        {"text": "Pour relever le facteur de puissance global de l'usine et annuler l'énergie réactive facturée par le fournisseur", "isCorrect": True},
                        {"text": "Pour stocker une immense quantité d'énergie électrique de secours permettant aux machines de continuer à tourner pendant plusieurs heures en cas de coupure du réseau", "isCorrect": False},
                        {"text": "Pour lisser les courants harmoniques générés par les radiateurs de chauffage et protéger les longues lignes d'alimentation en cuivre contre la surchauffe de l'isolant", "isCorrect": False},
                        {"text": "Pour augmenter artificiellement la tension de sortie du transformateur principal de la zone d'activité lors des pics de forte demande en plein mois de décembre", "isCorrect": False}
                    ],
                    "correction": "Les bobinages des moteurs asynchrones soutirent de l'énergie réactive pour créer leur champ magnétique tournant. Cette énergie pollue les câbles et est lourdement facturée par le distributeur. Les condensateurs fournissent cette énergie localement pour soulager le réseau public."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel composant électromécanique garantit l'arrêt immédiat d'une machine outil dangereuse lors de l'ouverture intempestive de son carter de protection ?",
                    "answerOptions": [
                        {"text": "Interrupteur de sécurité", "isCorrect": True},
                        {"text": "Temporisateur pneumatique", "isCorrect": False},
                        {"text": "Voyant de signalisation", "isCorrect": False},
                        {"text": "Disjoncteur différentiel", "isCorrect": False}
                    ],
                    "correction": "Les interrupteurs de sécurité de position (ou capteurs d'interverrouillage à languette) sont obligatoirement intégrés en série dans la chaîne de sécurité de la machine. L'ouverture d'un carter coupe net la puissance pour protéger l'opérateur."
                },
                {
                    "questionNumber": 76,
                    "question": "Que signifie techniquement la catégorie d'emploi AC3 indiquée sur la fiche technique d'un contacteur ?",
                    "answerOptions": [
                        {"text": "Il est robuste et conçu pour la commande de moteurs asynchrones à cage d'écureuil", "isCorrect": True},
                        {"text": "Il est exclusivement réservé à la coupure de petits circuits d'éclairage purement résistifs", "isCorrect": False},
                        {"text": "Il fonctionne uniquement avec une tension de commande de bobine en courant continu pur", "isCorrect": False},
                        {"text": "Il agit comme un simple relais de signalisation et ne possède aucun pouvoir de coupure en charge", "isCorrect": False}
                    ],
                    "correction": "La catégorie AC3 indique que les pastilles des contacts de puissance sont surdimensionnées pour supporter le très fort courant de démarrage d'un moteur asynchrone et pour couper le courant en charge nominale sans fondre sous l'effet de l'arc électrique."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle différence fondamentale distingue l'action d'un démarreur progressif de celle d'un variateur de fréquence sur un moteur ?",
                    "answerOptions": [
                        {"text": "Le démarreur gère uniquement la rampe de lancement en modulant la tension alors que le variateur contrôle la vitesse en permanence en modifiant la fréquence", "isCorrect": True},
                        {"text": "Le démarreur progressif est capable d'inverser le sens de marche du convoyeur à courroie tandis que le variateur de fréquence ne peut faire tourner l'axe mécanique que dans le sens horaire", "isCorrect": False},
                        {"text": "Le variateur de fréquence ne s'installe que sur des moteurs monophasés de très petite puissance alors que le démarreur s'utilise obligatoirement sur les moteurs triphasés", "isCorrect": False},
                        {"text": "Le démarreur progressif annule complètement la consommation d'énergie réactive de la machine outil ce qui rend inutile l'installation d'une batterie de condensateurs", "isCorrect": False}
                    ],
                    "correction": "Le démarreur progressif (soft starter) augmente graduellement la tension pour lancer le moteur sans à-coup mécanique, puis un relais le court-circuite (by-pass). Le variateur de fréquence redresse puis ondule le courant pour piloter la vitesse exacte et continue du moteur."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel équipement informatique industriel agit comme le cerveau logique pour piloter une ligne de production automatisée ?",
                    "answerOptions": [
                        {"text": "L'automate programmable industriel", "isCorrect": True},
                        {"text": "Le sectionneur porte-fusibles", "isCorrect": False},
                        {"text": "Le transformateur de commande", "isCorrect": False},
                        {"text": "Le bloc d'alimentation secourue", "isCorrect": False}
                    ],
                    "correction": "L'Automate Programmable Industriel (API) scrute l'état des entrées (capteurs, boutons) et exécute en boucle un programme informatique interne pour activer ou désactiver les sorties (contacteurs, électrovannes, voyants) de l'installation."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment fonctionne un détecteur photoélectrique industriel de type barrage ?",
                    "answerOptions": [
                        {"text": "L'émetteur lumineux et le récepteur sont logés dans deux boîtiers séparés qui se font face", "isCorrect": True},
                        {"text": "L'émetteur et le récepteur sont dans le même boîtier et utilisent un miroir prismatique en face", "isCorrect": False},
                        {"text": "Le faisceau de lumière rebondit directement sur l'objet ciblé pour revenir frapper le capteur", "isCorrect": False},
                        {"text": "Il détecte exclusivement le champ thermique infrarouge dégagé par le corps de l'opérateur", "isCorrect": False}
                    ],
                    "correction": "Le système optique de type barrage utilise deux boîtiers distincts. La détection est enclenchée lorsque l'objet coupe physiquement le faisceau lumineux très puissant qui traverse l'espace entre l'émetteur et le récepteur. C'est le système le plus fiable face à la poussière."
                },
                {
                    "questionNumber": 80,
                    "question": "Pourquoi le circuit de commande d'un arrêt d'urgence de machine utilise-t-il obligatoirement une technologie de redondance avec double canal croisé ?",
                    "answerOptions": [
                        {"text": "Pour garantir que la machine s'arrêtera systématiquement même si un fil se coupe ou si un relais de sécurité reste mécaniquement bloqué", "isCorrect": True},
                        {"text": "Pour réduire de moitié la consommation électrique du bouton coup de poing lorsque l'installation industrielle est laissée en veille pendant tout le week-end", "isCorrect": False},
                        {"text": "Pour permettre au technicien de relancer la chaîne de production beaucoup plus rapidement en appuyant sur un seul bouton d'acquittement global", "isCorrect": False},
                        {"text": "Pour envoyer simultanément le signal de détresse à la sirène d'évacuation de l'usine et aux services de secours extérieurs via le réseau téléphonique", "isCorrect": False}
                    ],
                    "correction": "La redondance de sécurité (deux contacts Normalement Fermés et deux fils séparés reliés à un module de sécurité intelligent) garantit que la sécurité de l'opérateur n'est jamais compromise par une seule défaillance matérielle. Si un contact lâche, le deuxième assure l'arrêt."
                }
            ]
        }
# =========================================================================
        # THÈME 5 : MISE EN SERVICE, CONTRÔLES, MESURES ET MAINTENANCE (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : MISE EN SERVICE, CONTRÔLES, MESURES ET MAINTENANCE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel appareil est utilisé pour tester la résistance d'isolement d'un câble électrique hors tension ?",
                    "answerOptions": [
                        {"text": "Le mégohmmètre", "isCorrect": True},
                        {"text": "Le voltmètre analogique", "isCorrect": False},
                        {"text": "Le tachymètre optique", "isCorrect": False},
                        {"text": "Le pont diviseur", "isCorrect": False}
                    ],
                    "correction": "Le mégohmmètre injecte une tension continue élevée (généralement 500 V pour les réseaux basse tension) afin de mesurer la résistance de l'isolant en mégohms entre les conducteurs, détectant ainsi les micro-fuites."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment raccorde-t-on un voltmètre pour mesurer la tension aux bornes d'un récepteur ?",
                    "answerOptions": [
                        {"text": "En dérivation directement sur le récepteur", "isCorrect": True},
                        {"text": "En série dans le circuit de puissance", "isCorrect": False},
                        {"text": "En coupant préalablement le fil de neutre", "isCorrect": False},
                        {"text": "En l'insérant à la place du fusible", "isCorrect": False}
                    ],
                    "correction": "Un voltmètre possède une résistance interne extrêmement élevée. Il se place toujours en parallèle (en dérivation) pour mesurer la différence de potentiel sans perturber la circulation du courant."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la procédure réglementaire pour mesurer la continuité du conducteur de protection au tableau ?",
                    "answerOptions": [
                        {"text": "Utiliser un ohmmètre injectant un courant d'au moins deux cents milliampères sous une source de tension à vide très basse", "isCorrect": True},
                        {"text": "Raccorder directement un multimètre standard en mode voltmètre alternatif entre la carcasse de la machine et le neutre du transformateur principal situé à l'extérieur", "isCorrect": False},
                        {"text": "Provoquer volontairement un court-circuit franc entre la phase et la carcasse métallique afin de chronométrer le temps de réaction exact du disjoncteur différentiel de tête installé dans le TGBT", "isCorrect": False},
                        {"text": "Envoyer une impulsion haute fréquence de cinq cents volts continus dans le câble vert et jaune pour vérifier que l'isolant ne présente aucune fuite microscopique vers les structures porteuses du bâtiment", "isCorrect": False}
                    ],
                    "correction": "La norme impose de vérifier la continuité de la liaison équipotentielle avec un courant de 200 mA (sous 4 à 24 V) pour s'assurer que le câble et ses raccordements ne sont pas desserrés."
                },
                {
                    "questionNumber": 84,
                    "question": "Que recherche-t-on principalement lors d'un contrôle par thermographie infrarouge dans un TGBT ?",
                    "answerOptions": [
                        {"text": "Les points d'échauffement dus à des mauvais serrages", "isCorrect": True},
                        {"text": "Le taux d'humidité à l'intérieur des gaines de câbles", "isCorrect": False},
                        {"text": "La chute de tension exacte sur les départs moteurs", "isCorrect": False},
                        {"text": "La présence de courants harmoniques de rang trois", "isCorrect": False}
                    ],
                    "correction": "La caméra thermique détecte les points chauds invisibles à l'œil nu, le plus souvent causés par un faux contact, un desserrage ou une surcharge de phase, prévenant ainsi les risques majeurs d'incendie électrique."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel appareil mesure la prise de terre ?",
                    "answerOptions": [
                        {"text": "Le telluromètre", "isCorrect": True},
                        {"text": "Le phasemètre", "isCorrect": False},
                        {"text": "Le galvanomètre", "isCorrect": False},
                        {"text": "L'oscilloscope", "isCorrect": False}
                    ],
                    "correction": "Le telluromètre (ou contrôleur de terre) utilise des piquets auxiliaires pour injecter un courant et mesurer la résistance d'écoulement de la prise de terre en ohms selon la méthode des 62 %."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel type de maintenance consiste à remplacer une pièce avant qu'elle ne tombe en panne ?",
                    "answerOptions": [
                        {"text": "La maintenance préventive", "isCorrect": True},
                        {"text": "La maintenance corrective", "isCorrect": False},
                        {"text": "La maintenance palliative", "isCorrect": False},
                        {"text": "La maintenance curative", "isCorrect": False}
                    ],
                    "correction": "La maintenance préventive vise à réduire la probabilité de défaillance d'une installation en planifiant des contrôles et des remplacements périodiques selon les préconisations du constructeur."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel essai est obligatoire pour valider le bon fonctionnement d'un interrupteur différentiel lors de la mise en service ?",
                    "answerOptions": [
                        {"text": "Mesurer son temps de déclenchement et son courant de déclenchement exact avec un contrôleur d'installation multifonction", "isCorrect": True},
                        {"text": "Connecter directement une lampe à incandescence de très forte puissance entre la phase et le fil de terre pour simuler un court-circuit thermique de grande ampleur", "isCorrect": False},
                        {"text": "Couper et réarmer la manette principale une centaine de fois consécutives afin de valider la robustesse mécanique des ressorts internes de la chambre de coupure de l'arc électrique", "isCorrect": False},
                        {"text": "Augmenter progressivement la tension du réseau d'alimentation jusqu'à atteindre quatre cents volts pour vérifier que l'appareil protège efficacement contre les surtensions dues à la foudre en été", "isCorrect": False}
                    ],
                    "correction": "Le simple appui sur le bouton de test ne suffit pas pour certifier l'appareil. Le contrôleur d'installation injecte un vrai courant de fuite calibré et chronomètre le temps de coupure réel, qui doit être conforme à la norme."
                },
                {
                    "questionNumber": 88,
                    "question": "En dépannage hors tension, que signifie une mesure de zéro ohm aux bornes d'un fusible démonté ?",
                    "answerOptions": [
                        {"text": "Le fusible est en bon état", "isCorrect": True},
                        {"text": "Le fusible est totalement grillé", "isCorrect": False},
                        {"text": "Le fusible est mal calibré", "isCorrect": False},
                        {"text": "Le fusible fuit à la terre", "isCorrect": False}
                    ],
                    "correction": "Une résistance nulle (zéro ohm ou une valeur très proche) indique que le filament interne conducteur est intact. Une valeur infinie ou OL (Over Limit) signalerait un fusible fondu."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel testeur valide le champ tournant ?",
                    "answerOptions": [
                        {"text": "Le phasemètre", "isCorrect": True},
                        {"text": "Le capacimètre", "isCorrect": False},
                        {"text": "Le fréquencemètre", "isCorrect": False},
                        {"text": "Le luxmètre", "isCorrect": False}
                    ],
                    "correction": "Le contrôleur d'ordre de phases (ou phasemètre) indique le sens du champ tournant d'un réseau triphasé (L1-L2-L3). C'est crucial avant de brancher un moteur pour s'assurer qu'il tournera dans le bon sens."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est la particularité d'une pince ampèremétrique pour mesurer l'intensité ?",
                    "answerOptions": [
                        {"text": "Elle mesure le courant sans avoir besoin d'ouvrir le circuit", "isCorrect": True},
                        {"text": "Elle doit toujours être raccordée en série avec le moteur", "isCorrect": False},
                        {"text": "Elle fonctionne uniquement sur un réseau hors tension", "isCorrect": False},
                        {"text": "Elle coupe instantanément l'alimentation en cas de danger", "isCorrect": False}
                    ],
                    "correction": "Contrairement à un multimètre classique qui s'insère en série, la pince ampèremétrique se referme autour du conducteur et mesure le champ magnétique induit pour en déduire l'intensité, ce qui permet de travailler en sécurité sans débrancher les câbles."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le but principal de l'utilisation d'une GMAO dans le service de maintenance d'un site industriel ?",
                    "answerOptions": [
                        {"text": "Planifier les interventions et gérer les stocks de pièces détachées tout en conservant un historique complet des pannes", "isCorrect": True},
                        {"text": "Remplacer totalement les techniciens de maintenance par des algorithmes d'intelligence artificielle capables de réparer les armoires électriques de façon totalement autonome sans aucune intervention humaine", "isCorrect": False},
                        {"text": "Contrôler la consommation électrique de l'usine en temps réel afin de revendre l'excédent d'énergie au fournisseur national pendant les pics de forte demande hivernale sur le réseau de distribution", "isCorrect": False},
                        {"text": "Dessiner de nouveaux schémas électriques unifilaires en trois dimensions pour faciliter la conception des futurs ateliers de production automatisés prévus dans les prochaines décennies", "isCorrect": False}
                    ],
                    "correction": "La Gestion de Maintenance Assistée par Ordinateur (GMAO) est un logiciel indispensable en industrie. Il centralise les bons de travaux, les plannings préventifs, les stocks et les coûts d'intervention pour optimiser le travail des équipes techniques."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle précaution faut-il prendre avant de vérifier un condensateur de compensation avec un ohmmètre ?",
                    "answerOptions": [
                        {"text": "Il faut le décharger entièrement en court-circuitant ses bornes avec une résistance", "isCorrect": True},
                        {"text": "Il faut l'alimenter en tension continue maximale", "isCorrect": False},
                        {"text": "Il faut inverser ses deux pôles de raccordement", "isCorrect": False},
                        {"text": "Il faut le plonger dans un bac d'eau déminéralisée", "isCorrect": False}
                    ],
                    "correction": "Un condensateur emmagasine de l'énergie électrique. S'il n'est pas déchargé avant la mesure hors tension, il va restituer cette énergie et risque de détruire l'appareil de mesure ou de provoquer un choc électrique au technicien."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel appareil teste l'éclairement d'un bureau ?",
                    "answerOptions": [
                        {"text": "Le luxmètre", "isCorrect": True},
                        {"text": "Le télémètre", "isCorrect": False},
                        {"text": "Le spectromètre", "isCorrect": False},
                        {"text": "L'anémomètre", "isCorrect": False}
                    ],
                    "correction": "Le luxmètre mesure l'éclairement lumineux reçu sur une surface, exprimé en lux. Il permet de vérifier la conformité de la luminosité d'un poste de travail selon les normes d'ergonomie et de sécurité au travail."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle action caractérise une maintenance de type corrective palliative ?",
                    "answerOptions": [
                        {"text": "Un dépannage provisoire pour remettre la machine en route", "isCorrect": True},
                        {"text": "Une réparation définitive avec des pièces d'origine", "isCorrect": False},
                        {"text": "Un contrôle visuel quotidien de l'armoire électrique", "isCorrect": False},
                        {"text": "Une modification pour améliorer le rendement du moteur", "isCorrect": False}
                    ],
                    "correction": "La maintenance palliative est un dépannage de fortune. Elle permet de relancer la production temporairement en attendant l'arrivée de la pièce de rechange nécessaire pour effectuer la maintenance corrective curative définitive."
                },
                {
                    "questionNumber": 95,
                    "question": "Lors d'une consignation électrique, quelle condition est indispensable pour exécuter l'étape de la Condamnation ?",
                    "answerOptions": [
                        {"text": "Bloquer l'organe de manœuvre avec un cadenas physique et apposer une étiquette de signalisation claire interdisant la remise en marche", "isCorrect": True},
                        {"text": "Dévisser les câbles de puissance directement sur le bornier du moteur pour s'assurer physiquement que l'énergie ne pourra plus jamais circuler dans les bobinages internes du stator", "isCorrect": False},
                        {"text": "Enclencher le bouton d'arrêt d'urgence situé sur le pupitre de commande de la machine afin de couper instantanément l'alimentation du circuit de commande sans verrouiller le sectionneur principal", "isCorrect": False},
                        {"text": "Demander au responsable de production de surveiller visuellement l'armoire électrique pendant toute la durée de l'intervention pour empêcher un autre technicien de relever la manette du disjoncteur", "isCorrect": False}
                    ],
                    "correction": "L'étape deux de la consignation (condamnation) requiert une immobilisation mécanique avec un dispositif inviolable comme un cadenas de consignation, complétée par une affiche nominale de prévention. Cela garantit que personne ne réarmera le circuit par erreur."
                },
                {
                    "questionNumber": 96,
                    "question": "Que doit vérifier un électricien à l'aide d'un ohmmètre lors d'un test de filerie ?",
                    "answerOptions": [
                        {"text": "Le bon câblage du circuit et l'absence de court-circuit entre les différentes phases", "isCorrect": True},
                        {"text": "La tension efficace présente sur le réseau de distribution", "isCorrect": False},
                        {"text": "Le sens de rotation exact du champ magnétique", "isCorrect": False},
                        {"text": "La valeur du courant de défaut à la terre", "isCorrect": False}
                    ],
                    "correction": "Le test de filerie ou essai de continuité s'effectue strictement hors tension. L'ohmmètre ou le testeur sonore permet de "sonner" les câbles pour vérifier qu'ils vont au bon endroit et qu'ils ne se touchent pas accidentellement."
                },
                {
                    "questionNumber": 97,
                    "question": "En environnement industriel, à quelle fréquence minimale l'employeur doit-il faire vérifier les installations électriques par un organisme agréé ?",
                    "answerOptions": [
                        {"text": "Une fois par an obligatoirement selon les prescriptions strictes du Code du travail", "isCorrect": True},
                        {"text": "Une fois tous les dix ans lors du renouvellement de l'assurance responsabilité civile du bâtiment", "isCorrect": False},
                        {"text": "Exclusivement lors du changement d'un disjoncteur général défectueux provoquant une coupure totale des lignes de production de l'usine", "isCorrect": False},
                        {"text": "Seulement si un inspecteur du travail en fait la demande écrite et motivée suite à un signalement d'accident grave impliquant un choc électrique sur un ouvrier non qualifié", "isCorrect": False}
                    ],
                    "correction": "Le Code du travail français impose une vérification périodique annuelle des installations électriques dans les établissements recevant des travailleurs (ERT), afin de prévenir les risques d'incendie et de contacts directs ou indirects."
                },
                {
                    "questionNumber": 98,
                    "question": "Lors de la mise en service d'un réseau informatique cuivre, que mesure un réflectomètre ?",
                    "answerOptions": [
                        {"text": "La longueur du câble et l'emplacement exact d'une coupure ou d'un défaut", "isCorrect": True},
                        {"text": "La tension électrique délivrée par les prises ondulées", "isCorrect": False},
                        {"text": "L'échauffement thermique du routeur informatique", "isCorrect": False},
                        {"text": "La luminosité des témoins LED sur les commutateurs", "isCorrect": False}
                    ],
                    "correction": "Le réflectomètre (TDR) envoie une impulsion électrique dans le câble. Si le câble est écrasé ou coupé, l'impulsion rebondit. L'appareil calcule le temps de retour de l'onde pour localiser le défaut au mètre près."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle est la fonction d'une caméra thermique lors de la maintenance préventive d'un TGBT ?",
                    "answerOptions": [
                        {"text": "Repérer les échauffements anormaux liés à des faux contacts ou des surcharges sans avoir à couper l'alimentation électrique", "isCorrect": True},
                        {"text": "Mesurer la consommation d'énergie réactive de l'installation pour ajuster automatiquement les batteries de condensateurs situées en amont du disjoncteur général", "isCorrect": False},
                        {"text": "Détecter les fuites de courant vers la terre en visualisant le champ magnétique rayonné par le conducteur de protection relié à la barrette d'équipotentialité", "isCorrect": False},
                        {"text": "Contrôler l'étanchéité à la poussière de l'enveloppe métallique de l'armoire en projetant un faisceau de lumière infrarouge à travers les joints en mousse polyuréthane défectueux", "isCorrect": False}
                    ],
                    "correction": "La thermographie infrarouge détecte les rayonnements thermiques. Les connexions mal serrées ou les câbles en surcharge apparaissent comme des points chauds lumineux sur l'écran, permettant à l'équipe de maintenance d'intervenir avant la destruction du matériel."
                },
                {
                    "questionNumber": 100,
                    "question": "En régime de neutre IT, quelle précaution absolue faut-il prendre lors de l'utilisation d'un mégohmmètre sous 500 Volts ?",
                    "answerOptions": [
                        {"text": "Déconnecter préalablement les cartes électroniques sensibles et les variateurs de vitesse", "isCorrect": True},
                        {"text": "Réaliser la mesure en gardant le réseau sous tension nominale complète", "isCorrect": False},
                        {"text": "Brancher l'appareil en série avec le disjoncteur principal du bâtiment", "isCorrect": False},
                        {"text": "Verser de l'eau salée sur les piquets de terre extérieurs de l'installation", "isCorrect": False}
                    ],
                    "correction": "Le mégohmmètre injecte une tension très élevée pour tester la robustesse de l'isolant. S'il reste branché sur des équipements incluant de l'électronique de puissance (variateurs, automates, cartes), il foudroiera et détruira instantanément ces composants."
                }
            ]
        }
    }
}