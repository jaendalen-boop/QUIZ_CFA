quiz_data = {
    "title": "Quiz CS maintenance des équipements thermiques individuels (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : Maintenance des générateurs de chaleur classiques (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : Maintenance des générateurs de chaleur classiques",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la valeur O2 attendue sur une chaudière gaz condensation ?",
                    "answerOptions": [
                        {"text": "Entre 4 et 5 pour cent", "isCorrect": True},
                        {"text": "Entre 9 et 10 pour cent", "isCorrect": False},
                        {"text": "Entre 1 et 2 pour cent", "isCorrect": False},
                        {"text": "Entre 12 et 14 pour cent", "isCorrect": False}
                    ],
                    "correction": "Une valeur d'O2 entre 4% et 5% correspond à un excès d'air optimal d'environ 20% à 30%, garantissant une combustion stable, sécurisée et un point de rosée favorable à la condensation."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le courant d'ionisation minimal typique pour maintenir la flamme ?",
                    "answerOptions": [
                        {"text": "Supérieur à 2 microampères", "isCorrect": True},
                        {"text": "Supérieur à 20 milliampères", "isCorrect": False},
                        {"text": "Inférieur à 1 microampère", "isCorrect": False},
                        {"text": "Supérieur à 500 nanoampères", "isCorrect": False}
                    ],
                    "correction": "Le courant de flamme redressé mesuré en série sur l'électrode d'ionisation doit généralement être supérieur à 2 microampères. En dessous, le coffret de sécurité interprète une perte de flamme."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment ajuster la cote Z sur un brûleur fioul ?",
                    "answerOptions": [
                        {"text": "En modifiant la position de la ligne gicleur par rapport à l'accroche-flamme", "isCorrect": True},
                        {"text": "En tournant la vis de réglage de la pompe pour augmenter la pression de pulvérisation au-delà des préconisations du constructeur de la chaudière", "isCorrect": False},
                        {"text": "En remplaçant le transformateur d'allumage par un modèle générant une tension d'arc plus importante", "isCorrect": False},
                        {"text": "En modifiant l'ouverture du volet d'air primaire sur le ventilateur centrifuge", "isCorrect": False}
                    ],
                    "correction": "La cote Z détermine l'espace entre le gicleur et le déflecteur. Son réglage précis est indispensable pour une bonne géométrie de flamme et éviter l'encrassement."
                },
                {
                    "questionNumber": 4,
                    "question": "À quoi sert le manomètre différentiel gaz ?",
                    "answerOptions": [
                        {"text": "Mesurer les pressions statique et dynamique", "isCorrect": True},
                        {"text": "Contrôler le tirage thermique naturel", "isCorrect": False},
                        {"text": "Calculer le débit volumique du réseau", "isCorrect": False},
                        {"text": "Vérifier la pression du vase d'expansion", "isCorrect": False}
                    ],
                    "correction": "Il permet de vérifier la pression du réseau gaz à l'arrêt du brûleur (statique) et en fonctionnement (dynamique) pour s'assurer que le bloc gaz est correctement alimenté."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la température des fumées en condensation gaz ?",
                    "answerOptions": [
                        {"text": "Moins de 50 degrés", "isCorrect": True},
                        {"text": "Plus de 120 degrés", "isCorrect": False},
                        {"text": "Environ 80 degrés", "isCorrect": False},
                        {"text": "Plus de 200 degrés", "isCorrect": False}
                    ],
                    "correction": "Pour qu'il y ait condensation de la vapeur d'eau contenue dans les gaz de combustion, la température des fumées doit descendre sous le point de rosée, soit environ 55°C pour le gaz naturel."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est l'action d'un pressostat air non basculé ?",
                    "answerOptions": [
                        {"text": "Interdiction de la séquence d'allumage", "isCorrect": True},
                        {"text": "Ouverture de la vanne de sécurité", "isCorrect": False},
                        {"text": "Fermeture du clapet anti-retour d'eau", "isCorrect": False},
                        {"text": "Mise en vitesse maximale du circulateur", "isCorrect": False}
                    ],
                    "correction": "Si le pressostat air ne détecte pas une dépression ou une pression suffisante générée par l'extracteur, la carte électronique bloque le cycle avant l'ouverture de l'électrovanne gaz."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est la méthode de réglage d'une vanne gaz modulante ?",
                    "answerOptions": [
                        {"text": "Ajuster le débit maximum puis le minimum", "isCorrect": True},
                        {"text": "Ajuster uniquement le débit au ralenti", "isCorrect": False},
                        {"text": "Modifier la pression statique du détendeur", "isCorrect": False},
                        {"text": "Régler la vis de bypass de l'échangeur", "isCorrect": False}
                    ],
                    "correction": "Sur les blocs gaz pneumatiques, on règle d'abord le rapport gaz/air à pleine puissance via la vis de débit, puis on ajuste le décalage du zéro au ralenti via la vis d'offset."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel composant gère la chronologie de sécurité brûleur ?",
                    "answerOptions": [
                        {"text": "Le coffret de contrôle", "isCorrect": True},
                        {"text": "Le thermostat d'ambiance", "isCorrect": False},
                        {"text": "La vanne trois voies", "isCorrect": False},
                        {"text": "Le limiteur de température", "isCorrect": False}
                    ],
                    "correction": "Le coffret de sécurité, ou boîtier de contrôle, pilote le moteur, l'allumage, l'électrovanne et surveille la présence de flamme avec des temps de sécurité stricts (temps de préventilation, temps de sécurité allumage)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle est la conséquence d'un excès d'air trop important sur brûleur fioul ?",
                    "answerOptions": [
                        {"text": "Une baisse drastique du rendement avec un risque important de décrochage de la flamme de la tête de combustion", "isCorrect": True},
                        {"text": "Une élévation anormale de la température des fumées entraînant systématiquement la fusion de l'accroche-flamme en acier inoxydable réfractaire", "isCorrect": False},
                        {"text": "Une diminution immédiate de la pression de pulvérisation au niveau de la pompe à engrenages interne", "isCorrect": False},
                        {"text": "Un blocage mécanique immédiat de la turbine de ventilation à cause d'une surpression dans le foyer", "isCorrect": False}
                    ],
                    "correction": "Trop d'air refroidit la flamme, fait chuter le taux de CO2, dégrade le rendement global et peut souffler la flamme hors de l'accroche-flamme."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est l'indice de noircissement Bacharach acceptable ?",
                    "answerOptions": [
                        {"text": "Entre zéro et un maximum", "isCorrect": True},
                        {"text": "Entre trois et quatre", "isCorrect": False},
                        {"text": "Supérieur à cinq systématiquement", "isCorrect": False},
                        {"text": "Strictement égal à neuf", "isCorrect": False}
                    ],
                    "correction": "Un brûleur fioul bien réglé ne doit produire aucune suie. Le test de tache sur le papier filtre doit correspondre à l'indice 0 ou 1 maximum de l'échelle Bacharach."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la dépression normale à l'aspiration d'une pompe fioul propre ?",
                    "answerOptions": [
                        {"text": "Entre -0.2 et -0.3 bar", "isCorrect": True},
                        {"text": "Entre -0.8 et -1.0 bar", "isCorrect": False},
                        {"text": "Supérieure à 2 bars", "isCorrect": False},
                        {"text": "Parfaitement égale à zéro", "isCorrect": False}
                    ],
                    "correction": "Une pompe fioul génère une légère dépression pour aspirer le combustible. Si elle dépasse -0.4 bar, cela signale une résistance anormale comme un préfiltre encrassé ou une vanne police fermée."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment valider l'étanchéité interne d'un bloc gaz double électrovanne ?",
                    "answerOptions": [
                        {"text": "Vérifier la chute de pression entre l'amont et l'aval vannes fermées à l'aide d'un manomètre en U ou digital", "isCorrect": True},
                        {"text": "Pulvériser un produit moussant détecteur de fuite sur les raccords filetés extérieurs sans isoler le circuit d'alimentation", "isCorrect": False},
                        {"text": "Mesurer la tension d'alimentation des bobines magnétiques en fonctionnement continu à puissance nominale", "isCorrect": False},
                        {"text": "Raccorder un analyseur de combustion en sortie d'extracteur pour détecter d'éventuels imbrûlés gazeux résiduels", "isCorrect": False}
                    ],
                    "correction": "Le test d'étanchéité des vannes de classe B ou C nécessite la mise en pression du tronçon intermédiaire et la mesure du temps de chute de pression pour quantifier la fuite interne selon les normes."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est la valeur cible du CO ambiant lors de l'entretien ?",
                    "answerOptions": [
                        {"text": "Zéro ppm", "isCorrect": True},
                        {"text": "Cinquante ppm", "isCorrect": False},
                        {"text": "Cent ppm", "isCorrect": False},
                        {"text": "Deux cents ppm", "isCorrect": False}
                    ],
                    "correction": "La mesure du CO dans l'air ambiant de la chaufferie doit afficher 0 ppm. Au-delà de 20 ppm pour le gaz et 50 ppm d'alerte grave, il y a un danger immédiat justifiant la consignation de l'appareil."
                },
                {
                    "questionNumber": 14,
                    "question": "Comment s'assurer du fonctionnement de la sonde CTN de chauffage ?",
                    "answerOptions": [
                        {"text": "Mesurer sa résistance ohmique à différentes températures", "isCorrect": True},
                        {"text": "Vérifier le courant de court-circuit en ampères", "isCorrect": False},
                        {"text": "Contrôler la tension alternative aux bornes du relais", "isCorrect": False},
                        {"text": "Tester la continuité avec un avertisseur sonore", "isCorrect": False}
                    ],
                    "correction": "Une thermistance CTN voit sa résistance chuter quand la température augmente. Le contrôle se fait avec un ohmmètre, en comparant les valeurs mesurées au tableau du fabricant."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel symptôme indique un siphon de condensats bouché ?",
                    "answerOptions": [
                        {"text": "Mise en sécurité suite à la noyade de l'électrode d'ionisation et au blocage du passage des fumées dans le corps de chauffe", "isCorrect": True},
                        {"text": "Ouverture intempestive de la soupape de sécurité sanitaire pour évacuer la surpression hydraulique accumulée dans le réseau tubulaire de l'installation de chauffage", "isCorrect": False},
                        {"text": "Surchauffe instantanée de la carte mère provoquant la destruction des fusibles de protection de la ligne d'alimentation", "isCorrect": False},
                        {"text": "Mise en rotation continue de la pompe de circulation indépendamment des demandes du thermostat d'ambiance", "isCorrect": False}
                    ],
                    "correction": "L'eau de condensation ne pouvant s'écouler, elle s'accumule dans le corps de chauffe jusqu'à noyer l'électrode ou obstruer totalement l'évacuation, bloquant la combustion et provoquant un défaut d'allumage."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la pression de pulvérisation classique sur un brûleur fioul domestique ?",
                    "answerOptions": [
                        {"text": "Entre 10 et 15 bars", "isCorrect": True},
                        {"text": "Entre 1 et 3 bars", "isCorrect": False},
                        {"text": "Entre 30 et 50 bars", "isCorrect": False},
                        {"text": "Inférieure à 1 bar", "isCorrect": False}
                    ],
                    "correction": "Les pompes fioul domestiques sont généralement réglées en usine à 12 bars, ajustable entre 10 et 15 bars pour affiner le débit et l'angle de pulvérisation selon le gicleur choisi."
                },
                {
                    "questionNumber": 17,
                    "question": "Pourquoi mesurer précisément le CO2 sur une chaudière à condensation ?",
                    "answerOptions": [
                        {"text": "Pour garantir l'atteinte du point de rosée et maximiser la récupération de chaleur latente des fumées", "isCorrect": True},
                        {"text": "Pour calculer le débit massique de combustible injecté par minute et ajuster les paramètres de la sonde extérieure", "isCorrect": False},
                        {"text": "Pour valider le fonctionnement mécanique de la turbine de l'extracteur des gaz brûlés", "isCorrect": False},
                        {"text": "Pour éviter la corrosion des conduites en cuivre du circuit primaire de chauffage", "isCorrect": False}
                    ],
                    "correction": "Un taux de CO2 optimal (autour de 9 à 9.5% pour le gaz naturel) indique un excès d'air maîtrisé. Un excès d'air trop grand abaisse la température du point de rosée, empêchant la condensation."
                },
                {
                    "questionNumber": 18,
                    "question": "Que protège le clapet anti-retour sur les systèmes en cascade ventouse collective ?",
                    "answerOptions": [
                        {"text": "Le refoulement des fumées vers les chaudières à l'arrêt", "isCorrect": True},
                        {"text": "La surpression hydraulique du circuit primaire", "isCorrect": False},
                        {"text": "Le passage du gaz vers le réseau d'eau potable", "isCorrect": False},
                        {"text": "L'inversion du sens de rotation du circulateur", "isCorrect": False}
                    ],
                    "correction": "En système 3CEp, le clapet anti-retour fumées empêche les gaz brûlés d'une chaudière en fonctionnement d'intoxiquer l'air via le conduit d'une chaudière voisine à l'arrêt."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle procédure appliquer après le déclenchement de la sécurité de surchauffe ?",
                    "answerOptions": [
                        {"text": "Identifier et corriger le défaut de circulation hydraulique avant de procéder au réarmement manuel de l'aquastat limiteur", "isCorrect": True},
                        {"text": "Remplacer immédiatement le circulateur principal sans vérifier la pression du vase d'expansion ni purger l'air du circuit des radiateurs supérieurs", "isCorrect": False},
                        {"text": "Court-circuiter le klixon de sécurité pour forcer le redémarrage temporaire de la production d'eau chaude sanitaire de l'habitation", "isCorrect": False},
                        {"text": "Injecter un produit de désembouage chimique concentré directement dans le corps de chauffe par l'orifice de purge automatique", "isCorrect": False}
                    ],
                    "correction": "L'aquastat de surchauffe à réarmement manuel est l'ultime sécurité thermique. Son déclenchement révèle un problème grave de dissipation thermique (pompe grippée, filtre bouché, air dans le réseau) qu'il faut résoudre."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel contrôle atteste du bon état d'un vase d'expansion chauffage fermé ?",
                    "answerOptions": [
                        {"text": "Pression de gonflage azote vérifiée côté air et pression nulle côté eau", "isCorrect": True},
                        {"text": "Pression d'eau mesurée supérieure à trois bars au manomètre", "isCorrect": False},
                        {"text": "Présence d'eau qui s'écoule par la valve de gonflage pneumatique", "isCorrect": False},
                        {"text": "Température de surface identique à celle de la chaudière", "isCorrect": False}
                    ],
                    "correction": "La vérification du vase nécessite de faire chuter la pression d'eau à 0 bar. Ensuite, on contrôle au manomètre pneumatique la pression de prégonflage (souvent entre 0.8 et 1.2 bar). De l'eau sortant par la valve indique une membrane percée."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : Maintenance des systèmes à énergies renouvelables (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : Maintenance des systèmes à énergies renouvelables",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la valeur cible d'une surchauffe bien réglée ?",
                    "answerOptions": [
                        {"text": "Entre 4 et 8 degrés Kelvin", "isCorrect": True},
                        {"text": "Entre 15 et 20 degrés Kelvin", "isCorrect": False},
                        {"text": "Toujours inférieure à zéro", "isCorrect": False},
                        {"text": "Strictement égale à 25 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "Une surchauffe comprise entre 4K et 8K assure le remplissage optimal de l'évaporateur tout en protégeant le compresseur des retours de fluide à l'état liquide."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment calcule-t-on le sous-refroidissement sur un condenseur PAC ?",
                    "answerOptions": [
                        {"text": "Température de condensation lue au manomètre haute pression moins la température du tube liquide", "isCorrect": True},
                        {"text": "Température d'aspiration compresseur moins la température d'évaporation", "isCorrect": False},
                        {"text": "Température de refoulement gaz chaud moins la température ambiante extérieure", "isCorrect": False},
                        {"text": "Température de sortie d'eau chaude moins la température d'entrée d'eau froide", "isCorrect": False}
                    ],
                    "correction": "Le sous-refroidissement vérifie l'état liquide du fluide avant le détendeur. Il se calcule par la différence entre la température de saturation haute pression et la température réelle du tube en sortie de condenseur."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel diagnostic frigorifique indique un manque de charge fluide ?",
                    "answerOptions": [
                        {"text": "Une surchauffe très élevée couplée à un sous-refroidissement nul ou très faible", "isCorrect": True},
                        {"text": "Une augmentation significative de l'intensité absorbée par le compresseur Inverter provoquant le déclenchement immédiat du disjoncteur magnétothermique divisionnaire de la ligne électrique", "isCorrect": False},
                        {"text": "Une haute pression anormalement élevée associée à des battements réguliers du détendeur électronique", "isCorrect": False},
                        {"text": "Une condensation intense sur la carrosserie externe du compresseur hermétique rotatif", "isCorrect": False}
                    ],
                    "correction": "Un manque de fluide assèche l'évaporateur, faisant grimper la surchauffe. Simultanément, le manque de masse dans le condenseur empêche la création du bouchon liquide, annulant le sous-refroidissement."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle de la sonde lambda sur une chaudière biomasse ?",
                    "answerOptions": [
                        {"text": "Mesurer le taux d'oxygène des fumées pour moduler l'apport d'air comburant", "isCorrect": True},
                        {"text": "Contrôler la température de surface du silo à granulés", "isCorrect": False},
                        {"text": "Détecter le niveau de remplissage des cendres dans le bac", "isCorrect": False},
                        {"text": "Mesurer le débit volumétrique du circulateur de charge", "isCorrect": False}
                    ],
                    "correction": "La sonde lambda, placée dans le conduit de fumées, analyse l'O2 résiduel. La carte électronique ajuste alors la vitesse de l'extracteur et l'alimentation en bois pour obtenir la combustion stoechiométrique parfaite."
                },
                {
                    "questionNumber": 25,
                    "question": "À quelle pression azote effectuer un test d'étanchéité R410A ?",
                    "answerOptions": [
                        {"text": "Autour de 40 bars", "isCorrect": True},
                        {"text": "Moins de 5 bars", "isCorrect": False},
                        {"text": "Maximum 12 bars", "isCorrect": False},
                        {"text": "Supérieure à 100 bars", "isCorrect": False}
                    ],
                    "correction": "Le test sous azote hydrogéné (N2H2) ou azote sec doit se faire à une pression d'épreuve proche de la pression maximale de service du fluide, souvent autour de 35 à 42 bars pour le R410A ou R32."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle sécurité s'active si le filtre à tamis du circuit d'eau s'obstrue ?",
                    "answerOptions": [
                        {"text": "Coupure en sécurité basse pression fluide côté frigorifique", "isCorrect": True},
                        {"text": "Déclenchement du pressostat haute pression de refoulement", "isCorrect": False},
                        {"text": "Mise en défaut du détecteur de fuite de gaz interne", "isCorrect": False},
                        {"text": "Surchauffe extrême du compresseur électrique Inverter", "isCorrect": False}
                    ],
                    "correction": "Un filtre à tamis bouché sur le retour chauffage empêche l'eau de réchauffer le fluide dans l'évaporateur (cas d'une géothermie) ou d'absorber la chaleur du condenseur (aérothermie). Dans les deux cas, le transfert thermique s'effondre, perturbant les pressions de cycle BP ou HP."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le principe thermodynamique du dégivrage par inversion de cycle ?",
                    "answerOptions": [
                        {"text": "La vanne 4 voies bascule pour que l'échangeur extérieur devienne le condenseur et fasse fondre la glace avec les gaz de refoulement chauds", "isCorrect": True},
                        {"text": "L'activation d'une résistance électrique d'appoint blindée située sous le bac à condensats de l'unité extérieure afin de garantir l'évacuation gravitaire rapide de l'eau de dégivrage hivernal", "isCorrect": False},
                        {"text": "La mise en rotation du ventilateur axial à pleine vitesse sans démarrage du compresseur frigorifique pour extraire l'humidité de la batterie ailetée", "isCorrect": False},
                        {"text": "L'injection ponctuelle de fluide caloporteur chaud provenant du ballon tampon directement dans les tubulures internes de l'évaporateur", "isCorrect": False}
                    ],
                    "correction": "En inversant le cycle, la PAC puise la chaleur dans l'eau du réseau de chauffage intérieur pour l'envoyer dégivrer rapidement l'unité extérieure givrée par la basse température d'évaporation."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle cause provoque une température de refoulement compresseur trop élevée ?",
                    "answerOptions": [
                        {"text": "Une surchauffe excessive à l'aspiration de l'évaporateur", "isCorrect": True},
                        {"text": "Un excès de charge en fluide frigorigène fluoré", "isCorrect": False},
                        {"text": "Un blocage en pleine ouverture du détendeur électronique", "isCorrect": False},
                        {"text": "Une température ambiante extérieure très basse en hiver", "isCorrect": False}
                    ],
                    "correction": "Les gaz aspirés refroidissent le moteur du compresseur. Si la surchauffe est trop élevée (manque de fluide ou détendeur trop fermé), les gaz arrivent trop chauds, entraînant une température de refoulement critique."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est l'utilité première d'un tirage au vide profond ?",
                    "answerOptions": [
                        {"text": "Éliminer toute trace d'humidité et de gaz incondensables du circuit", "isCorrect": True},
                        {"text": "Vérifier la résistance mécanique des brasures à l'argent", "isCorrect": False},
                        {"text": "Recharger le circuit en huile synthétique polyolester", "isCorrect": False},
                        {"text": "Mesurer le débit massique du détendeur capillaire", "isCorrect": False}
                    ],
                    "correction": "Le vide abaisse la température d'ébullition de l'eau. L'humidité résiduelle s'évapore et est aspirée par la pompe. C'est crucial car l'humidité réagit avec l'huile POE et crée de l'acide mortel pour le compresseur."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le seuil de détection d'un fuite de fluide réglementaire ?",
                    "answerOptions": [
                        {"text": "Moins de 5 grammes par an", "isCorrect": True},
                        {"text": "Plus de 50 grammes par mois", "isCorrect": False},
                        {"text": "Autour de 1 kilogramme par an", "isCorrect": False},
                        {"text": "Zéro virgule un gramme par décennie", "isCorrect": False}
                    ],
                    "correction": "Selon la réglementation F-Gas, l'outillage de détection de fuite électronique doit avoir une sensibilité certifiée d'au moins 5 grammes par an d'équivalent CO2 selon les fluides testés."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment vérifier le bon basculement d'une vanne 4 voies ?",
                    "answerOptions": [
                        {"text": "Mesurer les écarts de température au contact des quatre tubes connectés au corps de vanne pour identifier les conduites de gaz chaud et d'aspiration", "isCorrect": True},
                        {"text": "Remplacer systématiquement la bobine magnétique d'inversion puis procéder à une nouvelle mise en service avec des paramètres de régulation modifiés depuis la carte mère principale Inverter de l'unité", "isCorrect": False},
                        {"text": "Insérer un manomètre haute pression directement sur la ligne de retour d'huile du tiroir central en laiton usiné", "isCorrect": False},
                        {"text": "Augmenter la vitesse du ventilateur de l'évaporateur au maximum pour forcer le tiroir à se déplacer mécaniquement", "isCorrect": False}
                    ],
                    "correction": "Le diagnostic d'une vanne 4 voies bloquée (tiroir coincé) se fait par thermométrie de contact sur ses tubulures : tube refoulement toujours chaud, tube aspiration toujours froid, et différentiel marqué entre les tubes échangeurs."
                },
                {
                    "questionNumber": 32,
                    "question": "Comment s'ajuste un détendeur électronique ?",
                    "answerOptions": [
                        {"text": "Régulation PID par pas de moteur pas à pas selon la consigne de surchauffe calculée", "isCorrect": True},
                        {"text": "Réglage manuel via une vis de précontrainte agissant sur le ressort du train thermostatique", "isCorrect": False},
                        {"text": "Ouverture proportionnelle à la pression de l'eau du circuit hydraulique primaire", "isCorrect": False},
                        {"text": "Modulation par variation de la tension d'alimentation du bulbe thermostatique", "isCorrect": False}
                    ],
                    "correction": "La carte électronique calcule la surchauffe en temps réel grâce aux sondes de pression et de température, et commande le moteur pas-à-pas du détendeur électronique pour affiner l'injection au millimètre."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment s'entretient l'échangeur tubulaire d'une chaudière pellets ?",
                    "answerOptions": [
                        {"text": "Actionnement régulier des turbulateurs mécaniques à ressort", "isCorrect": True},
                        {"text": "Passage obligatoire d'un désembouant chimique très agressif", "isCorrect": False},
                        {"text": "Remplacement préventif des tubes en acier réfractaire", "isCorrect": False},
                        {"text": "Rinçage à haute pression avec de l'eau déminéralisée", "isCorrect": False}
                    ],
                    "correction": "Les turbulateurs (ressorts dans les tubes de l'échangeur fumées/eau) nettoient les parois par frottement mécanique, souvent de manière motorisée et automatique, pour chasser les poussières isolantes."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le risque majeur d'un retour de liquide au compresseur frigorifique ?",
                    "answerOptions": [
                        {"text": "Dilution de l'huile provoquant un défaut de lubrification et la destruction des organes mécaniques en mouvement", "isCorrect": True},
                        {"text": "Chute de la pression de condensation entraînant l'arrêt de sécurité basse pression de l'automate programmable industriel", "isCorrect": False},
                        {"text": "Gel immédiat du fluide frigorigène à l'intérieur du collecteur de l'évaporateur à plaques brasées en acier inoxydable", "isCorrect": False},
                        {"text": "Inversion du sens de rotation de la turbine du ventilateur axial de l'unité frigorifique placée à l'extérieur", "isCorrect": False}
                    ],
                    "correction": "Les compresseurs sont conçus pour comprimer des gaz. L'arrivée de liquide rince l'huile des paliers, crée des coups de liquide sur les clapets ou les spirales (Scroll), entraînant une casse mécanique irréversible."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle action mener si le test d'acidité de l'huile s'avère positif ?",
                    "answerOptions": [
                        {"text": "Poser un filtre déshydrateur anti-acide spécifique sur la ligne liquide et prévoir un remplacement d'huile ultérieur", "isCorrect": True},
                        {"text": "Purger l'intégralité du circuit frigorifique à l'air comprimé non séché pour chasser les résidus carbonisés logés dans les capillaires très fins du détendeur thermostatique avant le tirage au vide", "isCorrect": False},
                        {"text": "Injecter un produit colmatant anti-fuite directement par la prise de service de la vanne de refoulement", "isCorrect": False},
                        {"text": "Remplacer uniquement la bobine du détendeur électronique sans procéder à une analyse spectrométrique", "isCorrect": False}
                    ],
                    "correction": "L'acidité est destructrice pour le vernis des moteurs de compresseurs hermétiques. Il faut piéger cette acidité avec une cartouche anti-acide gros volume temporaire, nettoyer le circuit, et changer l'huile POE."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel type de moteur équipe les compresseurs Inverter de PAC modernes ?",
                    "answerOptions": [
                        {"text": "Moteur sans balais à courant continu dit Brushless DC", "isCorrect": True},
                        {"text": "Moteur asynchrone monophasé à condensateur permanent", "isCorrect": False},
                        {"text": "Moteur pas à pas à réluctance variable multiphasé", "isCorrect": False},
                        {"text": "Moteur synchrone classique à excitation bobinée série", "isCorrect": False}
                    ],
                    "correction": "Les moteurs BLDC (Brushless Direct Current) alimentés par la carte Inverter offrent le meilleur rendement énergétique et une capacité de modulation de vitesse très fine."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment valider électriquement la bougie d'allumage d'un poêle à granulés ?",
                    "answerOptions": [
                        {"text": "Par la mesure de sa résistance interne en ohms appareil hors tension", "isCorrect": True},
                        {"text": "Par l'injection d'un courant de fuite de quelques milliampères", "isCorrect": False},
                        {"text": "En court-circuitant volontairement les bornes du bornier principal", "isCorrect": False},
                        {"text": "En contrôlant la fréquence de la tension d'alimentation en Hertz", "isCorrect": False}
                    ],
                    "correction": "Une résistance d'allumage céramique ou quartz défectueuse présente une résistance infinie (circuit ouvert). Sa valeur ohmique nominale, généralement entre 150 et 300 ohms, confirme son intégrité."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment gérer le risque légionelle sur un ballon thermodynamique ?",
                    "answerOptions": [
                        {"text": "Paramétrer un cycle de chauffe anti-légionelle périodique montant le volume d'eau au-dessus de soixante degrés Celsius en exploitant l'appoint électrique intégré", "isCorrect": True},
                        {"text": "Vidanger complètement la cuve sanitaire toutes les semaines pour empêcher la stagnation prolongée de l'eau dans les zones de température modérée situées en partie basse du préparateur en acier émaillé", "isCorrect": False},
                        {"text": "Ajouter des pastilles de chlore pur concentré dans le vase d'expansion sanitaire branché en dérivation sur le groupe de sécurité", "isCorrect": False},
                        {"text": "Maintenir la consigne de la pompe à chaleur seule à quarante degrés constants toute l'année", "isCorrect": False}
                    ],
                    "correction": "La pompe à chaleur ne chauffe souvent qu'à 50°C/55°C, plage où les bactéries peuvent survivre. Le cycle anti-légionelle hebdomadaire utilise la résistance électrique de secours pour réaliser un choc thermique."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle est l'influence d'une baisse de température extérieure sur une PAC aérothermique ?",
                    "answerOptions": [
                        {"text": "Une chute conjointe de la puissance thermique restituée et du coefficient de performance global de la machine frigorifique", "isCorrect": True},
                        {"text": "Une augmentation exponentielle de la capacité de récupération d'énergie par l'évaporateur", "isCorrect": False},
                        {"text": "Une réduction drastique de la vitesse de rotation du ventilateur axial pour limiter les échanges d'air froids", "isCorrect": False},
                        {"text": "Un blocage automatique du compresseur électrique Inverter pour prévenir la formation prolongée de gel", "isCorrect": False}
                    ],
                    "correction": "Plus l'air extérieur est froid, moins il contient d'énergie exploitable et plus la pression d'évaporation chute. Le compresseur travaille davantage, ce qui fait s'effondrer le COP et la puissance calorifique."
                },
                {
                    "questionNumber": 40,
                    "question": "Pourquoi nettoyer quotidiennement ou hebdomadairement le creuset biomasse ?",
                    "answerOptions": [
                        {"text": "Assurer un apport d'air primaire par les fentes du brasier pour maintenir une combustion complète et éviter la formation d'un bloc de mâchefer dur et imperméable", "isCorrect": True},
                        {"text": "Réduire drastiquement la température de consigne des fumées rejetées dans le conduit tubé afin de prévenir de manière absolue tout risque de condensation fortement acide sur les parois en acier inoxydable poli", "isCorrect": False},
                        {"text": "Permettre le basculement libre de la vanne de sécurité anti-retour de flamme intégrée directement sur l'axe d'alimentation de la vis sans fin d'amenée de combustible", "isCorrect": False},
                        {"text": "Optimiser le refroidissement par convection naturelle des parois externes de la chambre de combustion en fonte grise très épaisse", "isCorrect": False}
                    ],
                    "correction": "Le creuset ou brasier possède des orifices d'air. Si les cendres fondent sous l'effet de la chaleur (mâchefer), elles bouchent ces fentes. L'air n'arrive plus, le granulé s'accumule et le système s'étouffe ou se met en défaut d'allumage."
                }
            ]
        }
# =========================================================================
        # THÈME 3 : Circuits hydrauliques et traitement de l'eau (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : Circuits hydrauliques et traitement de l'eau",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel appareil élimine les boues magnétiques ?",
                    "answerOptions": [
                        {"text": "Pot à boues", "isCorrect": True},
                        {"text": "Circulateur", "isCorrect": False},
                        {"text": "Soupape", "isCorrect": False},
                        {"text": "Détendeur", "isCorrect": False}
                    ],
                    "correction": "Le pot à boues magnétique utilise un aimant puissant pour piéger les oxydes de fer en suspension dans le circuit de chauffage."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est l'effet d'une eau trop dure ?",
                    "answerOptions": [
                        {"text": "Entartrage", "isCorrect": True},
                        {"text": "Corrosion", "isCorrect": False},
                        {"text": "Cavitation", "isCorrect": False},
                        {"text": "Filtration", "isCorrect": False}
                    ],
                    "correction": "Une eau riche en calcium et magnésium provoque un entartrage rapide des échangeurs thermiques et des corps de chauffe."
                },
                {
                    "questionNumber": 43,
                    "question": "Que mesure un manomètre ?",
                    "answerOptions": [
                        {"text": "Pression", "isCorrect": True},
                        {"text": "Débit", "isCorrect": False},
                        {"text": "Température", "isCorrect": False},
                        {"text": "Vitesse", "isCorrect": False}
                    ],
                    "correction": "Le manomètre indique la pression statique ou dynamique du fluide dans le circuit hydraulique."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la fonction d'un disconnecteur ?",
                    "answerOptions": [
                        {"text": "Empêcher le retour d'eau polluée", "isCorrect": True},
                        {"text": "Réguler la pression du réseau", "isCorrect": False},
                        {"text": "Purger l'air du circuit", "isCorrect": False},
                        {"text": "Filtrer les boues", "isCorrect": False}
                    ],
                    "correction": "Le disconnecteur protège le réseau d'eau potable contre les retours éventuels d'eau de chauffage polluée par des additifs chimiques."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le rôle d'un circulateur à vitesse variable ?",
                    "answerOptions": [
                        {"text": "Adapter le débit aux besoins réels de l'installation pour réduire la consommation électrique", "isCorrect": True},
                        {"text": "Maintenir une pression constante de trois bars dans le ballon tampon de stockage d'eau", "isCorrect": False},
                        {"text": "Chauffer directement le fluide caloporteur grâce à une résistance électrique blindée intégrée", "isCorrect": False},
                        {"text": "Purger automatiquement l'air accumulé dans les points hauts du réseau de radiateurs", "isCorrect": False}
                    ],
                    "correction": "Les circulateurs modernes à modulation PWM ou auto-adaptatifs réduisent leur vitesse et leur consommation lorsque les robinets thermostatiques se ferment."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment identifier un phénomène de cavitation sur un circulateur ?",
                    "answerOptions": [
                        {"text": "Bruit caractéristique de gravillons brassés et érosion des pales de la turbine", "isCorrect": True},
                        {"text": "Augmentation anormale de la température ambiante de la chaufferie et disjonction thermique", "isCorrect": False},
                        {"text": "Fuite d'eau au niveau de l'axe central du rotor étanche à garniture mécanique", "isCorrect": False},
                        {"text": "Blocage complet du moteur suite à l'accumulation de tartre dans les enroulements", "isCorrect": False}
                    ],
                    "correction": "La cavitation se produit quand la pression locale chute sous la tension de vapeur du liquide, provoquant l'implosion de bulles qui détruisent les pales."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel additif injecte-t-on pour lutter contre la corrosion galvanique ?",
                    "answerOptions": [
                        {"text": "Un inhibiteur de corrosion filmogène", "isCorrect": True},
                        {"text": "Un acide chlorhydrique dilué", "isCorrect": False},
                        {"text": "Un désembouant alcalin puissant", "isCorrect": False},
                        {"text": "Un antigel à base de méthanol", "isCorrect": False}
                    ],
                    "correction": "L'inhibiteur crée une fine pellicule protectrice sur les parois métalliques pour stopper les réactions électrochimiques entre métaux différents."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la conséquence d'un vase d'expansion sous-dimensionné ?",
                    "answerOptions": [
                        {"text": "Ouverture fréquente de la soupape de sécurité lors de la montée en température", "isCorrect": True},
                        {"text": "Chute brutale de la température de l'eau dans les radiateurs de l'habitation", "isCorrect": False},
                        {"text": "Blocage mécanique de la vanne mélangeuse motorisée en position fermée", "isCorrect": False},
                        {"text": "Augmentation du courant d'ionisation mesuré sur la sonde de flamme", "isCorrect": False}
                    ],
                    "correction": "Si le volume du vase est trop faible, il ne peut absorber toute la dilatation de l'eau chauffée, ce qui fait grimper la pression jusqu'à l'ouverture de la soupape."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est l'intérêt d'un dégazeur cyclonique ?",
                    "answerOptions": [
                        {"text": "Séparer et évacuer les micro-bulles d'air dissoutes dans le fluide caloporteur", "isCorrect": True},
                        {"text": "Augmenter la pression de gonflage de la membrane en caoutchouc du vase", "isCorrect": False},
                        {"text": "Filtrer les particules solides de calcaire en suspension dans le réseau", "isCorrect": False},
                        {"text": "Réguler automatiquement le débit de la pompe selon les pertes de charge", "isCorrect": False}
                    ],
                    "correction": "Le dégazeur utilise la force centrifuge et la variation de vitesse pour forcer les micro-bulles d'air dissoutes à s'agglomérer et à s'échapper."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment réaliser un contrôle de l'efficacité du désembouage chimique ?",
                    "answerOptions": [
                        {"text": "Mesurer la conductivité électrique et la clarté de l'eau de rinçage prélevée", "isCorrect": True},
                        {"text": "Contrôler la tension aux bornes du circulateur avec un multimètre numérique", "isCorrect": False},
                        {"text": "Vérifier la pression statique du réseau chauffage avec un manomètre d'air", "isCorrect": False},
                        {"text": "Analyser le taux de monoxyde de carbone présent dans le corps de chauffe", "isCorrect": False}
                    ],
                    "correction": "La conductivité de l'eau permet de vérifier qu'il ne reste plus de résidus de produits chimiques après un rinçage de l'installation."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le rôle d'une vanne mélangeuse thermostatique sur le retour chaudière bois ?",
                    "answerOptions": [
                        {"text": "Éviter les chocs thermiques et la condensation acide en maintenant l'eau de retour au-dessus de soixante degrés", "isCorrect": True},
                        {"text": "Refroidir l'eau du circuit de chauffage avant son entrée dans les émetteurs pour économiser du combustible", "isCorrect": False},
                        {"text": "Augmenter la vitesse du circulateur principal lorsque le ballon tampon atteint sa capacité maximale", "isCorrect": False},
                        {"text": "Purger l'air accumulé dans le corps de chauffe lors des phases de démarrage à froid de l'appareil", "isCorrect": False}
                    ],
                    "correction": "Les chaudières biomasse craignent la condensation corrosive des goudrons. La vanne de recyclage maintient l'eau de retour chaude pour protéger le corps de chauffe."
                },
                {
                    "questionNumber": 52,
                    "question": "Que se passe-t-il si le circulateur tourne à l'envers ou est défectueux ?",
                    "answerOptions": [
                        {"text": "Baisse anormale du débit hydraulique, augmentation du delta T et mise en surchauffe", "isCorrect": True},
                        {"text": "Augmentation instantanée de la pression de gonflage du vase d'expansion", "isCorrect": False},
                        {"text": "Inversion complète du sens de circulation du fluide frigorigène dans la PAC", "isCorrect": False},
                        {"text": "Hausse du courant d'ionisation sur la tête de combustion du brûleur gaz", "isCorrect": False}
                    ],
                    "correction": "Un débit insuffisant provoque un échauffement trop rapide de l'eau dans l'échangeur, créant un grand écart de température et un déclenchement de la sécurité."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est l'utilité d'un clapet anti-thermosiphon ?",
                    "answerOptions": [
                        {"text": "Empêcher la circulation naturelle de l'eau chaude par gravité lorsque la pompe est arrêtée", "isCorrect": True},
                        {"text": "Maintenir une pression constante de service dans le réseau de distribution des radiateurs", "isCorrect": False},
                        {"text": "Autoriser le passage du fluide caloporteur uniquement vers le préparateur sanitaire", "isCorrect": False},
                        {"text": "Permettre la purge automatique des gaz dissous lors du fonctionnement de la chaudière", "isCorrect": False}
                    ],
                    "correction": "Le clapet anti-thermosiphon évite que les radiateurs ne chauffent de manière incontrôlée par convection naturelle lorsque la chaudière produit de l'eau chaude sanitaire."
                },
                {
                    "questionNumber": 54,
                    "question": "Comment dimensionner la pression de gonflage d'un vase d'expansion chauffage ?",
                    "answerOptions": [
                        {"text": "Égale à la hauteur statique de l'installation exprimée en bars plus une marge de sécurité de zéro virgule trois bar", "isCorrect": True},
                        {"text": "Toujours fixée à une valeur fixe de trois bars indépendamment de la hauteur de la maison", "isCorrect": False},
                        {"text": "Égale à la pression maximale admissible par la soupape de sécurité de la chaudière", "isCorrect": False},
                        {"text": "Calculée en fonction du volume total d'eau divisé par la puissance nominale du générateur", "isCorrect": False}
                    ],
                    "correction": "La pression de prégonflage à vide doit compenser la hauteur d'eau entre le vase et le point le plus haut de l'installation, plus 0.3 bar de sécurité."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est l'impact d'un titre hydrotimétrique trop élevé sur un chauffe-eau ?",
                    "answerOptions": [
                        {"text": "Dépôt rapide de tartre isolant sur la résistance ou l'échangeur, provoquant une surchauffe locale et une baisse de performance", "isCorrect": True},
                        {"text": "Corrosion généralisée et fulgurante de l'ensemble des cuves en acier émaillé de l'installation à cause d'une réaction chimique violente entre les ions sodium et le magnésium présent dans l'eau du réseau public de distribution municipale", "isCorrect": False},
                        {"text": "Formation immédiate de micro-bulles d'oxygène gazeux hautement corrosif qui détruisent la structure interne des circulateurs à rotor encrassé par des résidus de boues noires métalliques", "isCorrect": False},
                        {"text": "Augmentation anormale et instantanée de la pression statique dans le circuit hydraulique primaire jusqu'au déclenchement de la soupape thermique de sécurité étalonnée à sept bars", "isCorrect": False}
                    ],
                    "correction": "Une eau dure dépose du calcaire qui isole thermiquement les éléments de chauffe, provoquant une surchauffe du métal et des pannes prématurées."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment procéder au contrôle de l'équilibrage hydraulique d'un réseau de radiateurs ?",
                    "answerOptions": [
                        {"text": "Mesurer les deltas de température et ajuster les tés de réglage pour homogénéiser la puissance restituée dans chaque pièce", "isCorrect": True},
                        {"text": "Remplacer systématiquement tous les robinets thermostatiques manuels par des vannes électroniques connectées pilotées à distance par une application domotique externe installée sur le smartphone de l'habitant", "isCorrect": False},
                        {"text": "Augmenter la vitesse de rotation du circulateur principal au maximum pour forcer le passage de l'eau chaude dans les radiateurs les plus éloignés de la chaufferie principale de la maison individuelle", "isCorrect": False},
                        {"text": "Vidanger complètement le circuit primaire de chauffage central puis injecter un inhibiteur de corrosion filmogène concentré pour éliminer les pertes de charge dues aux boues accumulées", "isCorrect": False}
                    ],
                    "correction": "L'équilibrage consiste à brider les radiateurs les plus proches de la pompe via les tés de réglage pour garantir un débit suffisant aux émetteurs les plus éloignés."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle est la fonction principale d'un régulateur de pression différentielle sur une installation de chauffage ?",
                    "answerOptions": [
                        {"text": "Stabiliser la pression différentielle aux bornes des colonnes ou des vannes pour éliminer les bruits de sifflement et les dysfonctionnements lors des variations de débit", "isCorrect": True},
                        {"text": "Maintenir de manière rigoureuse et permanente une pression statique constante de trois bars dans l'ensemble des radiateurs en fonte situés à l'étage supérieur de l'habitation pour éviter le désamorçage de la pompe", "isCorrect": False},
                        {"text": "Contrôler en temps réel la température extérieure de l'air ambiant afin d'ajuster automatiquement la courbe de chauffe du générateur thermique en fonction des conditions climatiques de la saison hivernale", "isCorrect": False},
                        {"text": "Permettre la purge automatique de l'air dissous dans l'eau du circuit hydraulique primaire grâce à un système cyclonique rotatif intégré directement sur la conduite de refoulement du circulateur", "isCorrect": False}
                    ],
                    "correction": "Le régulateur de pression différentielle absorbe les variations de pression lorsque les robinets thermostatiques se ferment, évitant les bruits d'écoulement et l'usure."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel diagnostic poser face à une soupape de sécurité sanitaire qui fuit en permanence ?",
                    "answerOptions": [
                        {"text": "Vérifier la pression du réseau d'eau froide et l'état du vase d'expansion sanitaire qui absorbe la dilatation thermique de la production d'eau chaude", "isCorrect": True},
                        {"text": "Remplacer immédiatement le corps de chauffe de la chaudière murale gaz condensation parce que l'échangeur à plaques est entièrement percé par des phénomènes de corrosion galvanique très avancés", "isCorrect": False},
                        {"text": "Augmenter la consigne du thermostat d'ambiance à vingt-cinq degrés Celsius pour forcer le circulateur principal à évacuer le surplus d'énergie thermique accumulée dans le ballon tampon de stockage", "isCorrect": False},
                        {"text": "Injecter un volume important d'inhibiteur de corrosion filmogène concentré directement par le bouchon de purge supérieur du radiateur le plus proche pour stabiliser le niveau de pH de l'eau", "isCorrect": False}
                    ],
                    "correction": "L'eau chauffe, se dilate et augmente de volume. Sans vase d'expansion sanitaire ou si la pression d'alimentation est excessive, le groupe de sécurité s'ouvre pour cracher ce surplus."
                },
                {
                    "questionNumber": 59,
                    "question": "Pourquoi est-il obligatoire d'installer un disconnecteur à zone de pression réduites contrôlables sur le circuit de remplissage ?",
                    "answerOptions": [
                        {"text": "Pour empêcher tout retour d'eau polluée du circuit de chauffage vers le réseau d'alimentation en eau potable en cas de chute de pression amont", "isCorrect": True},
                        {"text": "Pour augmenter automatiquement la pression de service du circuit hydraulique primaire de chauffage central jusqu'à atteindre la valeur nominale de trois bars exigée par le constructeur de la chaudière", "isCorrect": False},
                        {"text": "Pour réguler la température de l'eau chaude sanitaire distribuée aux différents points de puisage de la maison afin de prévenir tout risque de brûlure grave chez les occupants du logement", "isCorrect": False},
                        {"text": "Pour filtrer l'ensemble des particules solides de calcaire et des oxydes de fer en suspension dans l'eau avant qu'elles n'atteignent les pales du circulateur à modulation électronique intégrée", "isCorrect": False}
                    ],
                    "correction": "Le disconnecteur intègre deux clapets et une zone de décharge à l'atmosphère pour garantir qu'aucune eau technique ne puisse contaminer le réseau public d'eau potable."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle d'un traitement d'eau par adoucisseur à résine échangeuse d'ions ?",
                    "answerOptions": [
                        {"text": "Remplacer les ions calcium et magnésium responsables du tartre par des ions sodium pour protéger les installations thermiques", "isCorrect": True},
                        {"text": "Éliminer la totalité des bactéries pathogènes et des germes de type légionelle présents dans l'eau froide sanitaire stockée dans le préparateur par un traitement thermique supérieur à soixante-dix degrés", "isCorrect": False},
                        {"text": "Abaisser la conductivité électrique globale du fluide caloporteur pour stopper définitivement les réactions électrochimiques de corrosion galvanique entre le cuivre et les radiateurs en fonte d'aluminium", "isCorrect": False},
                        {"text": "Augmenter de manière artificielle le point de rosée des gaz de combustion pour favoriser la condensation de la vapeur d'eau contenue dans les fumées et améliorer le rendement global de la chaudière", "isCorrect": False}
                    ],
                    "correction": "L'adoucisseur fixe les ions entartrants (calcium et les libère contre des ions sodium, adoucissant l'eau pour éviter le dépôt de tartre dans les réseaux sanitaires)."
                }
            ]
        }
# =========================================================================
        # THÈME 4 : Électricité, régulation et paramétrage (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : Électricité, régulation et paramétrage",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Que mesure un ohmmètre sur un circuit hors tension ?",
                    "answerOptions": [
                        {"text": "La résistance", "isCorrect": True},
                        {"text": "La tension", "isCorrect": False},
                        {"text": "Le courant", "isCorrect": False},
                        {"text": "La puissance", "isCorrect": False}
                    ],
                    "correction": "L'ohmmètre s'utilise toujours hors tension pour mesurer la résistance électrique d'un composant comme une sonde ou une bobine, exprimée en ohms."
                },
                {
                    "questionNumber": 62,
                    "question": "Comment évolue la valeur d'une sonde CTN avec la chaleur ?",
                    "answerOptions": [
                        {"text": "Sa valeur ohmique diminue quand la température augmente", "isCorrect": True},
                        {"text": "Sa valeur ohmique augmente avec l'élévation de chaleur", "isCorrect": False},
                        {"text": "Elle génère une tension continue proportionnelle au froid", "isCorrect": False},
                        {"text": "Elle coupe le passage du courant à une valeur seuil", "isCorrect": False}
                    ],
                    "correction": "La CTN ou Coefficient de Température Négatif voit sa résistance baisser proportionnellement à l'augmentation de la température, servant de base de régulation électronique."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est l'intérêt du protocole OpenTherm pour un thermostat ?",
                    "answerOptions": [
                        {"text": "Établir une communication bidirectionnelle permettant de moduler en temps réel la puissance du brûleur selon les besoins exacts de l'habitation", "isCorrect": True},
                        {"text": "Envoyer des impulsions électriques séquentielles sur le réseau basse tension dans le seul but de démarrer ou d'arrêter brusquement le circulateur principal de la pompe à chaleur sans jamais modifier la température de l'eau", "isCorrect": False},
                        {"text": "Transformer un signal analogique continu en ondes radiofréquences", "isCorrect": False},
                        {"text": "Activer la résistance électrique de secours du ballon sanitaire", "isCorrect": False}
                    ],
                    "correction": "Contrairement à un thermostat Tout ou Rien, OpenTherm permet un dialogue numérique continu. La chaudière ajuste ainsi sa température de départ et sa puissance au plus juste."
                },
                {
                    "questionNumber": 64,
                    "question": "Sur quel calibre régler le multimètre pour tester une prise secteur ?",
                    "answerOptions": [
                        {"text": "Voltmètre en courant alternatif sur une plage supérieure à 230 volts", "isCorrect": True},
                        {"text": "Ampèremètre en courant continu sur le calibre dix ampères", "isCorrect": False},
                        {"text": "Ohmmètre sur la plus petite échelle de mesure de résistance", "isCorrect": False},
                        {"text": "Voltmètre en courant continu sur le calibre vingt volts", "isCorrect": False}
                    ],
                    "correction": "La tension du réseau domestique est alternative et vaut environ 230V. Le multimètre doit être configuré en VAC ou symbole V avec une vaguelette sur un calibre supérieur pour éviter la destruction de l'appareil."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle habilitation électrique autorise un dépannage en basse tension ?",
                    "answerOptions": [
                        {"text": "BR", "isCorrect": True},
                        {"text": "B0", "isCorrect": False},
                        {"text": "B1", "isCorrect": False},
                        {"text": "BC", "isCorrect": False}
                    ],
                    "correction": "L'habilitation BR permet au technicien de maintenance de réaliser des interventions générales d'entretien et de dépannage ainsi que des consignations sur des circuits basse tension."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment fonctionne la loi d'eau gérée par une sonde extérieure ?",
                    "answerOptions": [
                        {"text": "Le régulateur anticipe les déperditions thermiques du bâtiment en modifiant automatiquement la température de départ du circuit selon les variations climatiques", "isCorrect": True},
                        {"text": "Le coffret de sécurité de l'appareil coupe intégralement l'alimentation électrique de la vanne gaz modulante dès que la pression atmosphérique extérieure dépasse une valeur limite enregistrée lors de la mise en service initiale par le technicien frigoriste", "isCorrect": False},
                        {"text": "Le système abaisse la vitesse de rotation du ventilateur extracteur", "isCorrect": False},
                        {"text": "La carte électronique maintient le brûleur à pleine puissance constante", "isCorrect": False}
                    ],
                    "correction": "La sonde extérieure mesure la température de l'air. Plus il fait froid dehors, plus la régulation augmente la température de l'eau envoyée dans les radiateurs selon une courbe de chauffe paramétrée au préalable."
                },
                {
                    "questionNumber": 67,
                    "question": "Que protège un disjoncteur différentiel 30 mA ?",
                    "answerOptions": [
                        {"text": "Il protège les personnes contre les risques d'électrisation", "isCorrect": True},
                        {"text": "Il protège le matériel contre les surintensités prolongées", "isCorrect": False},
                        {"text": "Il empêche les courts-circuits entre la phase et le neutre", "isCorrect": False},
                        {"text": "Il filtre les parasites électromagnétiques du réseau", "isCorrect": False}
                    ],
                    "correction": "Le dispositif différentiel à courant résiduel 30 mA coupe l'alimentation s'il détecte une fuite de courant vers la terre supérieure à ce seuil, protégeant ainsi l'utilisateur contre les contacts indirects."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment vérifier un fusible verre sur une carte mère ?",
                    "answerOptions": [
                        {"text": "Tester sa continuité avec un ohmmètre hors tension", "isCorrect": True},
                        {"text": "Mesurer le voltage aux bornes pendant le fonctionnement", "isCorrect": False},
                        {"text": "Inspecter visuellement la couleur de l'embout métallique", "isCorrect": False},
                        {"text": "Brancher un ampèremètre en parallèle sur le composant", "isCorrect": False}
                    ],
                    "correction": "Un fusible grillé présente une résistance infinie. Le contrôle fiable se fait appareil débranché, fusible retiré du support, en mesurant la continuité sonore ou la résistance à zéro ohm."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle est l'unité de mesure de la capacité d'un condensateur ?",
                    "answerOptions": [
                        {"text": "Le farad", "isCorrect": True},
                        {"text": "Le henry", "isCorrect": False},
                        {"text": "Le tesla", "isCorrect": False},
                        {"text": "Le joule", "isCorrect": False}
                    ],
                    "correction": "La capacité d'un condensateur, souvent utilisé comme condensateur de démarrage sur un circulateur ou un compresseur, se mesure en microfarads avec un capacimètre intégré au multimètre."
                },
                {
                    "questionNumber": 70,
                    "question": "Que provoque l'usure du condensateur permanent d'un circulateur ?",
                    "answerOptions": [
                        {"text": "Une diminution du couple de démarrage empêchant le rotor de tourner entraînant un blocage mécanique et une surchauffe rapide du bobinage", "isCorrect": True},
                        {"text": "Une surtension massive sur la carte de régulation principale de la chaudière qui va griller instantanément la totalité des microprocesseurs en charge de la gestion des sondes de température d'ambiance et extérieure du logement", "isCorrect": False},
                        {"text": "L'ouverture de la vanne de sécurité hydraulique sanitaire à trois bars", "isCorrect": False},
                        {"text": "L'inversion temporaire du sens d'écoulement du fluide caloporteur", "isCorrect": False}
                    ],
                    "correction": "Le condensateur crée le déphasage magnétique nécessaire au lancement du moteur asynchrone monophasé. S'il est usé, le moteur grogne, chauffe fortement et ne se lance plus de lui-même."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel paramètre ajuste la pente de la régulation climatique ?",
                    "answerOptions": [
                        {"text": "La courbe de chauffe dans les réglages installateur", "isCorrect": True},
                        {"text": "La consigne de température d'eau chaude sanitaire", "isCorrect": False},
                        {"text": "La limite de puissance maximale du brûleur fioul", "isCorrect": False},
                        {"text": "Le différentiel de commutation du thermostat d'ambiance", "isCorrect": False}
                    ],
                    "correction": "La pente ou courbe de chauffe définit le ratio mathématique entre la chute de la température extérieure et l'augmentation requise de la température de départ chauffage pour l'émetteur considéré."
                },
                {
                    "questionNumber": 72,
                    "question": "Comment identifier la phase sur un bornier 230V avec certitude ?",
                    "answerOptions": [
                        {"text": "Mesurer une tension de 230V entre ce fil et la borne de terre", "isCorrect": True},
                        {"text": "Mesurer une résistance nulle entre ce fil et le neutre", "isCorrect": False},
                        {"text": "Observer obligatoirement une gaine de couleur bleu clair", "isCorrect": False},
                        {"text": "Utiliser un ampèremètre en série avec le bornier principal", "isCorrect": False}
                    ],
                    "correction": "La phase présente un potentiel électrique de 230V par rapport à la terre, contrairement au neutre dont le potentiel est théoriquement de 0V par rapport à cette même terre physique."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle action réalise un relais électromagnétique sur une carte mère ?",
                    "answerOptions": [
                        {"text": "Isoler galvaniquement le circuit de commande basse tension du circuit de puissance afin d'autoriser le démarrage sécurisé d'un actionneur lourd", "isCorrect": True},
                        {"text": "Amplifier numériquement les signaux radiofréquences reçus par l'antenne du boîtier de communication pour permettre le pilotage de la chaudière depuis une application mobile installée sur la tablette de l'utilisateur final se trouvant à l'autre bout de la planète", "isCorrect": False},
                        {"text": "Convertir le courant alternatif du réseau en courant continu lissé", "isCorrect": False},
                        {"text": "Mesurer en temps réel la consommation électrique du ventilateur", "isCorrect": False}
                    ],
                    "correction": "Le relais permet à un microcontrôleur fonctionnant en 5V ou 12V d'actionner des équipements en 230V comme une pompe via un électroaimant fermant un contact mécanique totalement isolé."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel symbole électrique représente la prise de terre ?",
                    "answerOptions": [
                        {"text": "Des traits horizontaux superposés", "isCorrect": True},
                        {"text": "Un cercle traversé par une ligne", "isCorrect": False},
                        {"text": "Un triangle pointant vers le bas", "isCorrect": False},
                        {"text": "Une lettre majuscule cerclée", "isCorrect": False}
                    ],
                    "correction": "Le symbole normalisé de la terre est constitué d'une ligne verticale reposant sur trois traits horizontaux de longueurs décroissantes vers le bas."
                },
                {
                    "questionNumber": 75,
                    "question": "Que mesure un thermomètre de contact à thermocouple type K ?",
                    "answerOptions": [
                        {"text": "Une différence de potentiel générée par deux métaux", "isCorrect": True},
                        {"text": "L'expansion volumique d'un fluide sensible à la chaleur", "isCorrect": False},
                        {"text": "La modification de la résistance d'un fil de platine pur", "isCorrect": False},
                        {"text": "Le rayonnement infrarouge émis par un corps chaud", "isCorrect": False}
                    ],
                    "correction": "Le thermocouple type K exploite l'effet Seebeck qui stipule que la jonction de deux métaux différents soumis à la chaleur produit une très faible tension en millivolts proportionnelle à la température."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment valider le fonctionnement d'un aquastat limiteur mécanique ?",
                    "answerOptions": [
                        {"text": "Vérifier la rupture de continuité électrique entre ses bornes de raccordement lorsque la température du bulbe dépasse la valeur de sécurité définie", "isCorrect": True},
                        {"text": "Observer le changement de couleur d'un liquide chimique contenu dans l'ampoule en verre de la sonde immergée au fond du ballon d'eau chaude sanitaire de très grande capacité lorsque le brûleur atteint sa puissance de fonctionnement nominale maximale", "isCorrect": False},
                        {"text": "Mesurer l'augmentation progressive du courant d'ionisation sur la carte", "isCorrect": False},
                        {"text": "Constater l'ouverture automatique d'une vanne de décharge hydraulique", "isCorrect": False}
                    ],
                    "correction": "L'aquastat est un simple interrupteur thermique de sécurité. On le contrôle à l'ohmmètre et il doit être passant à température normale et s'ouvrir en cas de surchauffe."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel dispositif abaisse la tension du secteur de 230V à 24V ?",
                    "answerOptions": [
                        {"text": "Un transformateur abaisseur de tension", "isCorrect": True},
                        {"text": "Un pont de diodes redresseur de courant", "isCorrect": False},
                        {"text": "Un disjoncteur magnétothermique bipolaire", "isCorrect": False},
                        {"text": "Un condensateur permanent de démarrage", "isCorrect": False}
                    ],
                    "correction": "Le transformateur de commande convertit la tension du secteur alternatif en très basse tension de sécurité pour alimenter les bobines des contacteurs et les composants de régulation."
                },
                {
                    "questionNumber": 78,
                    "question": "Que signifie l'acronyme PID en régulation thermique numérique ?",
                    "answerOptions": [
                        {"text": "Proportionnel Intégral Dérivé", "isCorrect": True},
                        {"text": "Puissance Interne Dissipée", "isCorrect": False},
                        {"text": "Programme Informatique Domotique", "isCorrect": False},
                        {"text": "Pression Initiale Dynamique", "isCorrect": False}
                    ],
                    "correction": "La régulation PID est un algorithme de calcul très précis qui corrige les erreurs de température en temps réel en tenant compte de l'écart immédiat, de l'historique de chauffe et de la tendance évolutive."
                },
                {
                    "questionNumber": 79,
                    "question": "Pourquoi utiliser un câble blindé pour relier les sondes de régulation ?",
                    "answerOptions": [
                        {"text": "Empêcher les perturbations électromagnétiques induites par le réseau de courant fort de fausser les faibles signaux de mesure envoyés à la platine", "isCorrect": True},
                        {"text": "Garantir une résistance mécanique suffisante pour résister aux agressions chimiques provenant d'une éventuelle fuite d'acide ou de fluide frigorigène hautement corrosif lors des opérations de maintenance curative lourde sur le groupe extérieur", "isCorrect": False},
                        {"text": "Maintenir une tension d'alimentation strictement constante de 230 volts", "isCorrect": False},
                        {"text": "Empêcher la diffusion de gaz toxiques à travers la gaine d'isolation", "isCorrect": False}
                    ],
                    "correction": "Les sondes envoient des variations de résistance très sensibles. Le blindage du câble, mis à la terre, bloque les signaux parasites créés par le rayonnement des câbles de puissance voisins."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment s'effectue la consignation électrique d'un équipement thermique ?",
                    "answerOptions": [
                        {"text": "Séparation condamnation identification et vérification d'absence de tension", "isCorrect": True},
                        {"text": "Fermeture de la vanne gaz et coupure du disjoncteur divisionnaire général", "isCorrect": False},
                        {"text": "Débranchement de la prise de courant et pose de ruban adhésif rouge", "isCorrect": False},
                        {"text": "Arrêt du thermostat d'ambiance et vidange complète du corps de chauffe", "isCorrect": False}
                    ],
                    "correction": "La procédure stricte de consignation exige la séparation des sources, le verrouillage physique par cadenas, l'affichage réglementaire, puis la mesure de l'absence de tension avec un testeur VAT certifié."
                }
            ]
        }
# =========================================================================
        # THÈME 5 : Réglementation, sécurité et environnement (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : Réglementation, sécurité et environnement",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel document valide une installation gaz neuve ?",
                    "answerOptions": [
                        {"text": "Le certificat de conformité", "isCorrect": True},
                        {"text": "La facture du fournisseur d'énergie", "isCorrect": False},
                        {"text": "Le diagnostic de performance", "isCorrect": False},
                        {"text": "L'attestation d'entretien annuel", "isCorrect": False}
                    ],
                    "correction": "Le certificat de conformité gaz, visé par un organisme agréé, est obligatoirement exigé pour toute installation neuve, modifiée ou complétée avant la mise en service."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est l'unité du Potentiel de Réchauffement Global ?",
                    "answerOptions": [
                        {"text": "Équivalent tonne de dioxyde de carbone", "isCorrect": True},
                        {"text": "Kilogramme par heure de fonctionnement", "isCorrect": False},
                        {"text": "Pourcentage de masse volumique pure", "isCorrect": False},
                        {"text": "Indice de pollution atmosphérique", "isCorrect": False}
                    ],
                    "correction": "Le PRG classe les fluides frigorigènes en mesurant leur impact direct sur l'effet de serre, exprimé réglementairement en équivalent tonne de CO2."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel gaz est injecté lors du test de fuite frigorifique ?",
                    "answerOptions": [
                        {"text": "L'azote sec ou hydrogéné", "isCorrect": True},
                        {"text": "Le monoxyde de carbone pur", "isCorrect": False},
                        {"text": "L'oxygène pur à usage médical", "isCorrect": False},
                        {"text": "Le dioxyde de soufre liquide", "isCorrect": False}
                    ],
                    "correction": "Pour la recherche de micro-fuites avec un détecteur électronique très sensible (renifleur), le technicien utilise un mélange d'azote sec et de 5% d'hydrogène appelé azote hydrogéné."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel seuil de monoxyde de carbone justifie une consignation ?",
                    "answerOptions": [
                        {"text": "Cinquante ppm", "isCorrect": True},
                        {"text": "Dix ppm", "isCorrect": False},
                        {"text": "Cent ppm", "isCorrect": False},
                        {"text": "Vingt ppm", "isCorrect": False}
                    ],
                    "correction": "La réglementation impose un signalement à 20 ppm. En revanche, au-delà de 50 ppm mesurés dans l'air ambiant, le danger mortel justifie l'arrêt immédiat et la consignation de l'appareil."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle obligation impose la réglementation F-Gas aux opérateurs ?",
                    "answerOptions": [
                        {"text": "Détenir impérativement une attestation de capacité en cours de validité délivrée par un organisme agréé pour manipuler les fluides fluorés", "isCorrect": True},
                        {"text": "Remplacer systématiquement l'intégralité du fluide frigorigène contenu dans les compresseurs thermodynamiques lors de chaque entretien annuel préventif afin de garantir que l'installation ne produise jamais de gaz à effet de serre polluant pour l'environnement direct de l'habitation", "isCorrect": False},
                        {"text": "Obtenir un certificat de conformité européen exclusif aux pompes à chaleur", "isCorrect": False},
                        {"text": "Conserver les registres d'interventions techniques annuelles sans limitation de durée", "isCorrect": False}
                    ],
                    "correction": "Tout professionnel manipulant des fluides frigorigènes doit détenir une attestation d'aptitude, et son entreprise une attestation de capacité renouvelable tous les cinq ans, pour tracer et encadrer la manipulation des gaz à effet de serre."
                },
                {
                    "questionNumber": 86,
                    "question": "Comment ventiler un local contenant une chaudière gaz à tirage naturel ?",
                    "answerOptions": [
                        {"text": "Prévoir une amenée d'air frais basse et une sortie haute respectant des sections minimales calculées en fonction de la puissance nominale du générateur", "isCorrect": True},
                        {"text": "Installer obligatoirement un ventilateur extracteur mécanique motorisé couplé directement à l'alimentation électrique de la carte mère de la chaudière pour assurer un renouvellement d'air constant et ininterrompu vingt-quatre heures sur vingt-quatre dans toute la maison", "isCorrect": False},
                        {"text": "Condamner hermétiquement toutes les aérations de la chaufferie pour éviter le gel", "isCorrect": False},
                        {"text": "Laisser la porte d'accès au sous-sol partiellement ouverte sur la cage d'escalier", "isCorrect": False}
                    ],
                    "correction": "Les appareils de type B nécessitent des aérations inobstruables spécifiques. L'amenée d'air amène l'oxygène indispensable à la combustion, et la sortie d'air évite l'accumulation d'air vicié et de gaz imbrûlés."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la procédure en cas de découverte d'amiante sur une ancienne chaudière ?",
                    "answerOptions": [
                        {"text": "Suspendre immédiatement les travaux de maintenance en cours et alerter le client propriétaire pour qu'il fasse intervenir une entreprise spécialisée dans le désamiantage certifiée", "isCorrect": True},
                        {"text": "S'équiper d'un simple masque chirurgical en papier filtrant de base avant de procéder au grattage intensif des joints d'isolation thermiques de la porte foyère de l'ancienne chaudière fioul en fonte lourde située dans la cave mal ventilée de l'habitation résidentielle", "isCorrect": False},
                        {"text": "Humidifier abondamment la surface avec de l'eau savonneuse pour coller les fibres", "isCorrect": False},
                        {"text": "Recouvrir le matériau suspect avec de la bande adhésive d'emballage industriel", "isCorrect": False}
                    ],
                    "correction": "Les poussières d'amiante sont hautement cancérigènes. Le Code du Travail interdit formellement d'intervenir sur des matériaux amiantés sans qualification spécifique (Sous-section 4 ou 3). Le repli de chantier est la seule option légale."
                },
                {
                    "questionNumber": 88,
                    "question": "Que stipule la directive européenne ErP concernant l'éco-conception ?",
                    "answerOptions": [
                        {"text": "L'interdiction progressive de mise sur le marché des générateurs de chaleur présentant des rendements saisonniers inférieurs aux seuils minimums d'efficacité énergétique dictés par la commission", "isCorrect": True},
                        {"text": "L'obligation pour chaque foyer européen de procéder au démontage intégral et à la destruction certifiée de tous les radiateurs en fonte d'aluminium datant d'avant l'année deux mille pour les remplacer par des émetteurs basse température à haute performance radiante et convective", "isCorrect": False},
                        {"text": "Le remplacement obligatoire de tous les thermostats manuels par des modèles connectés", "isCorrect": False},
                        {"text": "La suppression immédiate et définitive des chaudières biomasse à granulés de bois", "isCorrect": False}
                    ],
                    "correction": "La directive Energy Related Products (ErP) impose des critères de rendement stricts qui excluent de fait la fabrication et la vente des chaudières classiques (basse température), forçant la transition vers la condensation et les pompes à chaleur."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle règle s'applique aux bouteilles de récupération de fluide frigorigène usagé ?",
                    "answerOptions": [
                        {"text": "Elles doivent faire l'objet d'un suivi strict de leur masse avec identification claire du type de gaz extrait avant renvoi aux centres de traitement agréés pour destruction ou recyclage", "isCorrect": True},
                        {"text": "Elles peuvent être réutilisées de manière totalement arbitraire pour stocker successivement différents types de gaz sous pression comme le R32 puis le R410A sans procéder au moindre tirage au vide ni rinçage préalable par le technicien frigoriste lors de son intervention sur le site client", "isCorrect": False},
                        {"text": "Elles doivent être peintes en couleur rouge vif obligatoire pour signaler un danger mortel", "isCorrect": False},
                        {"text": "Elles sont soumises à une requalification sous pression hydraulique tous les six mois", "isCorrect": False}
                    ],
                    "correction": "Un gaz récupéré est classé déchet industriel dangereux. Il est strictement interdit de mélanger des fluides différents dans la même bouteille de transfert, et l'opérateur doit tenir un registre des masses récupérées."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel organe de coupure est obligatoire sur une installation gaz réseau intérieure ?",
                    "answerOptions": [
                        {"text": "Un organe de coupure générale accessible rapidement couplé à des robinets de commande individuels placés juste avant chaque appareil raccordé", "isCorrect": True},
                        {"text": "La pose systématique d'une électrovanne de sécurité normalement fermée raccordée électriquement à un capteur de pression atmosphérique de haute précision mesurant en permanence les variations climatiques extérieures pour anticiper les baisses de tirage thermique du conduit d'évacuation principal", "isCorrect": False},
                        {"text": "Un détendeur haute pression scellé au plomb par le fournisseur directement sur le compteur", "isCorrect": False},
                        {"text": "Un disjoncteur différentiel thermique de protection contre les surtensions électriques", "isCorrect": False}
                    ],
                    "correction": "La norme gaz (arrêté du 23 février 2018) impose une commande de coupure générale (souvent le compteur) et des robinets de commande d'appareils pour isoler facilement chaque chaudière ou plaque de cuisson lors de l'entretien."
                },
                {
                    "questionNumber": 91,
                    "question": "Que caractérise l'étiquette énergie apposée sur un système de chauffage neuf ?",
                    "answerOptions": [
                        {"text": "Sa classe d'efficacité énergétique globale et saisonnière de A à G", "isCorrect": True},
                        {"text": "La pression hydraulique maximale tolérée par le corps de chauffe", "isCorrect": False},
                        {"text": "Le débit exact de combustible mesuré en litres par heure de chauffe", "isCorrect": False},
                        {"text": "Le calibre du fusible de protection intégré sur la carte électronique", "isCorrect": False}
                    ],
                    "correction": "Obligatoire en Europe, elle oriente le client vers les équipements les plus sobres en classant leurs performances énergétiques et en indiquant leur niveau sonore en décibels."
                },
                {
                    "questionNumber": 92,
                    "question": "Comment qualifier techniquement une chaudière dite de type B ?",
                    "answerOptions": [
                        {"text": "Elle prélève l'air comburant dans le local ambiant où elle est physiquement installée", "isCorrect": True},
                        {"text": "Elle possède un circuit de combustion totalement étanche vis à vis de l'habitation", "isCorrect": False},
                        {"text": "Elle fonctionne exclusivement au fioul lourd avec un gicleur spécifique très grand format", "isCorrect": False},
                        {"text": "Elle nécessite impérativement un conduit de fumées concentrique à double flux", "isCorrect": False}
                    ],
                    "correction": "Une chaudière type B dépend de l'air de la pièce pour brûler le gaz. Le risque d'intoxication au CO est réel si les ventilations du local sont bouchées ou si la VMC de la maison crée une dépression inversant le tirage."
                },
                {
                    "questionNumber": 93,
                    "question": "Que signifie légalement le marquage CE présent sur un équipement thermique ?",
                    "answerOptions": [
                        {"text": "La déclaration du fabricant concernant la conformité aux exigences de sécurité européennes", "isCorrect": True},
                        {"text": "La certification absolue d'une qualité de fabrication réalisée sur le territoire français", "isCorrect": False},
                        {"text": "Le calcul mathématique exact du coefficient de performance énergétique du compresseur", "isCorrect": False},
                        {"text": "L'obligation légale pour l'utilisateur de souscrire un contrat d'entretien préventif annuel", "isCorrect": False}
                    ],
                    "correction": "Le sigle Conformité Européenne n'est pas un label de qualité mais un marquage réglementaire affirmant que l'appareil répond aux directives européennes essentielles en matière de sécurité, de santé et d'environnement."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel déchet destructeur est produit par la dégradation chimique de l'huile POE ?",
                    "answerOptions": [
                        {"text": "De l'acide très corrosif pour le moteur électrique du compresseur frigorifique", "isCorrect": True},
                        {"text": "Des cendres minérales lourdes et solides bloquant le passage de l'air au niveau du condenseur", "isCorrect": False},
                        {"text": "Du monoxyde de carbone hautement toxique diffusé lentement dans les locaux d'habitation", "isCorrect": False},
                        {"text": "Des oxydes de fer sous forme de boues magnétiques sédimentées dans le carter d'huile", "isCorrect": False}
                    ],
                    "correction": "L'huile Polyolester absorbe fortement l'humidité (hygroscopie). Si un circuit frigorifique est mal tiré au vide, l'eau réagit avec l'huile pour créer des acides qui rongent les vernis isolants du bobinage interne."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est l'obligation de l'occupant d'un logement chauffé au gaz combustible ?",
                    "answerOptions": [
                        {"text": "Faire réaliser un entretien annuel complet du générateur par un professionnel qualifié", "isCorrect": True},
                        {"text": "Remplacer le générateur thermique tous les dix ans au minimum pour rester dans les normes", "isCorrect": False},
                        {"text": "Nettoyer personnellement les conduits de fumées en toiture avant chaque début de saison", "isCorrect": False},
                        {"text": "Mesurer le taux de monoxyde de carbone avec un analyseur de combustion chaque fin de mois", "isCorrect": False}
                    ],
                    "correction": "Le décret du 9 juin 2009 oblige le locataire ou le propriétaire occupant à faire entretenir sa chaudière chaque année, sous peine de ne pas être couvert par son assurance en cas d'incendie ou de sinistre."
                },
                {
                    "questionNumber": 96,
                    "question": "Que désigne l'appellation normative d'appareil de combustion de type C ?",
                    "answerOptions": [
                        {"text": "Un appareil à circuit de combustion entièrement étanche par rapport à la pièce", "isCorrect": True},
                        {"text": "Un appareil obligatoirement raccordé sur un conduit de cheminée maçonné traditionnel", "isCorrect": False},
                        {"text": "Un appareil mobile de chauffage d'appoint sans évacuation de type poêle à pétrole", "isCorrect": False},
                        {"text": "Un appareil électrique fonctionnant avec des panneaux à rayonnement infrarouge lointain", "isCorrect": False}
                    ],
                    "correction": "Aussi appelées chaudières ventouse, les machines de type C aspirent l'air dehors et rejettent les fumées dehors via un conduit concentrique ou séparé. Ce confinement total élimine le risque d'intoxication."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle information figure obligatoirement sur l'attestation d'entretien annuel remboursable ?",
                    "answerOptions": [
                        {"text": "Les valeurs de tirage et les taux mesurés de monoxyde de carbone dans les fumées et l'ambiance", "isCorrect": True},
                        {"text": "Le prix unitaire hors taxe détaillé de l'ensemble des pièces détachées d'usure remplacées", "isCorrect": False},
                        {"text": "Le schéma de câblage électrique interne de la carte mère imprimé au dos du document officiel", "isCorrect": False},
                        {"text": "L'historique complet informatisé des pannes survenues lors des dix années précédentes", "isCorrect": False}
                    ],
                    "correction": "Le technicien a 15 jours pour délivrer cette attestation. Elle prouve l'intervention et doit mentionner les mesures de combustion, le CO ambiant, et les recommandations d'usage ou d'amélioration."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle règle environnementale concerne les condensats d'une chaudière fioul ?",
                    "answerOptions": [
                        {"text": "Ils doivent être impérativement neutralisés avant leur rejet final dans le réseau des égouts", "isCorrect": True},
                        {"text": "Ils peuvent être déversés dans le jardin directement sans le moindre traitement préalable", "isCorrect": False},
                        {"text": "Ils sont systématiquement réinjectés dans le circuit de chauffage pour compenser les fuites", "isCorrect": False},
                        {"text": "Ils s'évaporent naturellement et totalement dans le conduit de fumée par inertie thermique", "isCorrect": False}
                    ],
                    "correction": "Le fioul contient du soufre, ce qui rend ses condensats très acides (pH proche de 2 ou 3). Pour ne pas détruire les canalisations d'assainissement de la commune, l'installation d'un bac de neutralisation à billes de carbonate de calcium est obligatoire."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel formulaire CERFA trace les mouvements de fluides frigorigènes fluorés ?",
                    "answerOptions": [
                        {"text": "La fiche d'intervention valant bordereau de suivi des déchets dangereux", "isCorrect": True},
                        {"text": "La facture détaillée d'achat des pièces de rechange émise par le fournisseur grossiste", "isCorrect": False},
                        {"text": "Le registre chronologique des heures de fonctionnement du compresseur thermodynamique", "isCorrect": False},
                        {"text": "Le certificat officiel de conformité de l'installation gaz naturel raccordée en réseau", "isCorrect": False}
                    ],
                    "correction": "Ce bordereau est obligatoire pour toute opération entraînant la manipulation d'un fluide. L'opérateur, l'entreprise et le client signent ce document qui atteste des quantités introduites, récupérées et renvoyées au traitement."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle précaution prendre impérativement lors du brasage sur une canalisation gaz ?",
                    "answerOptions": [
                        {"text": "Purger intégralement la ligne à l'azote inerte pour chasser les gaz avant d'allumer le chalumeau", "isCorrect": True},
                        {"text": "Laisser la vanne de compteur grande ouverte pour évacuer la pression résiduelle vers le domaine public", "isCorrect": False},
                        {"text": "Utiliser une éponge imbibée d'eau savonneuse sur la flamme pour éviter la surchauffe du cuivre", "isCorrect": False},
                        {"text": "Brancher le manomètre différentiel électronique pendant la soudure pour surveiller le débit gazeux", "isCorrect": False}
                    ],
                    "correction": "Chauffer une conduite ayant contenu du gaz combustible est extrêmement dangereux. L'artisan doit débrancher la conduite, la balayer avec un gaz neutre (azote) pour éliminer l'oxygène et le gaz combustible avant toute intervention à flamme nue."
                }
            ]
        }
    }
}