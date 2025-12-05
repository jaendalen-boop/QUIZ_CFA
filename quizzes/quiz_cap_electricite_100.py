# Fichier : quiz_cap_electricien_100.py

quiz_data = {
    "title": "Quiz CAP Électricien : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : SÉCURITÉ ET RÉGLEMENTATION (NF C 15-100, HABILITATION) (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Sécurité et Réglementation (NF C 15-100, Habilitation) (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle norme française régit les installations électriques basse tension dans les logements et bâtiments neufs ou rénovés ?",
                    "answerOptions": [
                        {"text": "NF P 03-001", "isCorrect": False},
                        {"text": "NF C 15-100 (ou UTE C 15-100)", "isCorrect": True},
                        {"text": "NF EN 50522", "isCorrect": False},
                        {"text": "DTU 68.3", "isCorrect": False}
                    ],
                    "correction": "La **NF C 15-100** est la référence absolue pour toute installation BT en France."
                },
                {
                    "questionNumber": 2,
                    "question": "Que signifie l'acronyme **IP2X** (Indice de Protection) pour un appareillage ?",
                    "answerOptions": [
                        {"text": "Protection contre les projections d'eau.", "isCorrect": False},
                        {"text": "Protection contre les corps solides supérieurs à $12.5$ mm (protection des doigts) et non protégé contre l'eau (ou protection minimale).", "isCorrect": True},
                        {"text": "Protection totale contre la poussière.", "isCorrect": False},
                        {"text": "Protection contre l'immersion.", "isCorrect": False}
                    ],
                    "correction": "Le premier chiffre (2) concerne la protection contre les solides, le second (X) l'eau."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la signification de l'habilitation électrique **B2V** ?",
                    "answerOptions": [
                        {"text": "Travaux Hors Tension (HTA).", "isCorrect": False},
                        {"text": "Chargé de Travaux (2) Basse Tension (B) au voisinage (V) de pièces nues sous tension.", "isCorrect": True},
                        {"text": "Exécutant (1) Basse Tension (B) à distance des pièces nues sous tension.", "isCorrect": False},
                        {"text": "Chargé de Consignation.", "isCorrect": False}
                    ],
                    "correction": "Le **B** indique la BT, le **2** Chargé de travaux, le **V** le Voisinage."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) essentiel pour effectuer des opérations de vérification sous tension ?",
                    "answerOptions": [
                        {"text": "Un casque de chantier.", "isCorrect": False},
                        {"text": "Des gants isolants (norme NF EN 60903), un casque/visière de protection faciale et des vêtements de travail non conducteurs.", "isCorrect": True},
                        {"text": "Des bottes en caoutchouc.", "isCorrect": False},
                        {"text": "Des bouchons d'oreille.", "isCorrect": False}
                    ],
                    "correction": "Les **gants isolants** et la protection du visage sont vitaux pour la protection contre l'arc électrique."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le rôle du dispositif de **Séparation et Consignation (S/C)** avant une intervention ?",
                    "answerOptions": [
                        {"text": "Améliorer l'esthétique du tableau.", "isCorrect": False},
                        {"text": "Assurer que le circuit est mis hors tension et qu'il ne peut pas être remis sous tension par un tiers (condamnation et étiquetage obligatoire) pour garantir la sécurité de l'intervenant.", "isCorrect": True},
                        {"text": "Vérifier la tension.", "isCorrect": False},
                        {"text": "Réduire la puissance.", "isCorrect": False}
                    ],
                    "correction": "La **Consignation** est la phase clé pour travailler Hors Tension."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la principale source de danger pour un électricien lors de travaux sur une installation HORS TENSION ?",
                    "answerOptions": [
                        {"text": "Le bruit.", "isCorrect": False},
                        {"text": "Le risque de remise sous tension accidentelle (non-consignation) ou la présence de Tensions Résiduelles (capacités).", "isCorrect": True},
                        {"text": "La poussière.", "isCorrect": False},
                        {"text": "Les produits chimiques.", "isCorrect": False}
                    ],
                    "correction": "La **Vérification d'Absence de Tension (VAT)** est la dernière étape avant l'intervention."
                },
                {
                    "questionNumber": 7,
                    "question": "Selon la NF C 15-100, quelle est l'exigence minimale concernant le nombre de prises de courant $16 \text{ A}$ dans la cuisine d'un logement neuf ?",
                    "answerOptions": [
                        {"text": "Deux prises.", "isCorrect": False},
                        {"text": "Six prises (dont 4 au-dessus du plan de travail) pour les logements de moins de $100 \text{ m}^2$ (ou plus selon la surface).", "isCorrect": True},
                        {"text": "Quatre prises.", "isCorrect": False},
                        {"text": "Dix prises.", "isCorrect": False}
                    ],
                    "correction": "La **cuisine** est la pièce la plus exigeante en prises électriques (électroménager)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la zone de sécurité (distance minimale) pour travailler sans Habilitation dans le **Voisinage Renforcé** ?",
                    "answerOptions": [
                        {"text": "Jusqu'à $0.30$ m des pièces sous tension.", "isCorrect": False},
                        {"text": "Plus de $0.30$ m pour la BT, et plus de $2$ m pour la HTA (Haute Tension).", "isCorrect": True},
                        {"text": "Jusqu'à $1$ m des pièces sous tension.", "isCorrect": False},
                        {"text": "Jusqu'à $2$ m des pièces sous tension.", "isCorrect": False}
                    ],
                    "correction": "Le **Voisinage** est l'espace autour des pièces sous tension où le danger est présent."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle est la fonction d'un **Vérificateur d'Absence de Tension (VAT)** ?",
                    "answerOptions": [
                        {"text": "Mesurer le courant.", "isCorrect": False},
                        {"text": "Certifier qu'il n'y a plus aucune tension dangereuse entre deux points (Phase-Neutre, Phase-Terre, Phase-Phase) sur le circuit avant intervention.", "isCorrect": True},
                        {"text": "Mesurer la résistance.", "isCorrect": False},
                        {"text": "Mesurer la puissance.", "isCorrect": False}
                    ],
                    "correction": "La **VAT** est l'outil obligatoire après consignation."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le risque de travailler sur un disjoncteur différentiel sans avoir coupé l'alimentation générale du logement ?",
                    "answerOptions": [
                        {"text": "Le disjoncteur tombe en panne.", "isCorrect": False},
                        {"text": "Risque d'électrocution ou de choc électrique par contact avec les bornes amont (arrivée du courant) qui sont encore sous tension.", "isCorrect": True},
                        {"text": "Le circuit disjoncte.", "isCorrect": False},
                        {"text": "Le circuit fonctionne mal.", "isCorrect": False}
                    ],
                    "correction": "Les **bornes amont** d'un disjoncteur sont toujours sous tension."
                },
                {
                    "questionNumber": 11,
                    "question": "Selon la NF C 15-100, quelle est la couleur normalisée pour le **fil de Neutre** ?",
                    "answerOptions": [
                        {"text": "Rouge.", "isCorrect": False},
                        {"text": "Bleu Clair.", "isCorrect": True},
                        {"text": "Vert/Jaune.", "isCorrect": False},
                        {"text": "Noir ou Marron.", "isCorrect": False}
                    ],
                    "correction": "Le **Bleu Clair** est le Neutre. Le Vert/Jaune est la Terre."
                },
                {
                    "questionNumber": 12,
                    "question": "Dans le logement, quelle est la protection obligatoire contre les risques d'incendie (surchauffe des câbles) ?",
                    "answerOptions": [
                        {"text": "Le disjoncteur différentiel.", "isCorrect": False},
                        {"text": "Le Disjoncteur divisionnaire (protection magnéto-thermique contre les surcharges et les courts-circuits).", "isCorrect": True},
                        {"text": "La mise à la terre.", "isCorrect": False},
                        {"text": "Le parafoudre.", "isCorrect": False}
                    ],
                    "correction": "Le **disjoncteur divisionnaire** protège le circuit contre les surintensités."
                },
                {
                    "questionNumber": 13,
                    "question": "Dans une salle de bain (SDB), dans quel **volume** est-il strictement interdit d'installer un point lumineux (luminaire) sans être de Très Basse Tension de Sécurité (TBTS) ?",
                    "answerOptions": [
                        {"text": "Volume 3.", "isCorrect": False},
                        {"text": "Volume 0 (l'intérieur de la baignoire ou du bac à douche) : seuls les matériels $\text{IPX}7$ et TBTS sont autorisés.", "isCorrect": True},
                        {"text": "Volume 2.", "isCorrect": False},
                        {"text": "Volume 1.", "isCorrect": False}
                    ],
                    "correction": "Le **Volume 0** est le plus dangereux (immersion)."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelle est la couleur normalisée pour le **fil de Terre (PE)** ?",
                    "answerOptions": [
                        {"text": "Noir.", "isCorrect": False},
                        {"text": "Vert et Jaune (Vert/Jaune).", "isCorrect": True},
                        {"text": "Bleu clair.", "isCorrect": False},
                        {"text": "Rouge.", "isCorrect": False}
                    ],
                    "correction": "Le **Vert/Jaune** est exclusivement réservé au fil de protection (Terre)."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est le risque de travailler sur des batteries ou des installations solaires (courant continu) sans avoir coupé les sources d'énergie ?",
                    "answerOptions": [
                        {"text": "Risque d'incendie.", "isCorrect": False},
                        {"text": "Risque de chocs électriques et de projection de métal en fusion (arc électrique) dû aux forts courants de court-circuit et aux tensions résiduelles élevées.", "isCorrect": True},
                        {"text": "Risque de surchauffe.", "isCorrect": False},
                        {"text": "Risque de coupure.", "isCorrect": False}
                    ],
                    "correction": "Le **Courant Continu (CC)** génère des arcs plus difficiles à éteindre que le CA."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le rôle du **dispositif différentiel (DDR) $30 \text{ mA}$** sur un tableau électrique ?",
                    "answerOptions": [
                        {"text": "Protéger contre la foudre.", "isCorrect": False},
                        {"text": "Protéger les personnes contre les contacts indirects (fuite de courant à la terre) et directs (électrocution).", "isCorrect": True},
                        {"text": "Protéger contre les surcharges.", "isCorrect": False},
                        {"text": "Protéger contre les courts-circuits.", "isCorrect": False}
                    ],
                    "correction": "Le **différentiel $30 \text{ mA}$** est la protection vitale des personnes."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le danger de laisser un conducteur de phase (fil rouge/noir) toucher accidentellement la carcasse métallique d'un appareil non relié à la Terre ?",
                    "answerOptions": [
                        {"text": "Surtension.", "isCorrect": False},
                        {"text": "L'appareil devient 'sous tension' : risque d'électrocution par contact direct pour la personne qui le touche (défaut d'isolement).", "isCorrect": True},
                        {"text": "Court-circuit.", "isCorrect": False},
                        {"text": "Surcharge.", "isCorrect": False}
                    ],
                    "correction": "C'est la définition même du **défaut d'isolement**."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la règle de sécurité des **cinq étapes** (consignation) ?",
                    "answerOptions": [
                        {"text": "Couper, vérifier, isoler, tester, débrancher.", "isCorrect": False},
                        {"text": "Séparer, Condamner (verrouiller), Vérifier l'Absence de Tension (VAT), Mettre à la Terre et en Court-Circuit (le cas échéant), Baliser/Signaler.", "isCorrect": True},
                        {"text": "Isoler, tester, réparer, rebrancher, vérifier.", "isCorrect": False},
                        {"text": "Couper, tester, vérifier, allumer, éteindre.", "isCorrect": False}
                    ],
                    "correction": "Les **cinq étapes** sont le protocole strict pour la sécurité hors tension."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est la règle d'installation des interrupteurs dans un logement ?",
                    "answerOptions": [
                        {"text": "À plus de $1.80$ m du sol.", "isCorrect": False},
                        {"text": "À une hauteur comprise entre $0.90 \text{ m}$ et $1.30 \text{ m}$ du sol fini, et ne jamais couper le neutre (uniquement la phase).", "isCorrect": True},
                        {"text": "À $0.50$ m du sol.", "isCorrect": False},
                        {"text": "Interrupteur bipolaire obligatoire partout.", "isCorrect": False}
                    ],
                    "correction": "La hauteur est fixée pour l'accessibilité (personnes à mobilité réduite)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est l'exigence de la NF C 15-100 concernant la **Gaine Technique Logement (GTL)** ?",
                    "answerOptions": [
                        {"text": "Elle doit être en bois.", "isCorrect": False},
                        {"text": "Elle doit regrouper toutes les arrivées (courant fort et courant faible), les protections et les départs de l'installation, être accessible, et aller du sol au plafond.", "isCorrect": True},
                        {"text": "Elle est optionnelle.", "isCorrect": False},
                        {"text": "Elle doit être dans la salle de bain.", "isCorrect": False}
                    ],
                    "correction": "La **GTL** est le point de départ de toute l'installation électrique du logement."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : THÉORIE DE BASE ET MESURES (LOI D'OHM, P, U, I) (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Théorie de Base et Mesures (Loi d'Ohm, P, U, I) (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est l'unité de mesure de la **Tension électrique (U)** et par quel appareil la mesure-t-on ?",
                    "answerOptions": [
                        {"text": "L'Ampère ($\text{A}$) mesuré par l'Ampèremètre.", "isCorrect": False},
                        {"text": "Le Volt ($\text{V}$) mesuré par le Voltmètre (ou multimètre en position Volt).", "isCorrect": True},
                        {"text": "L'Ohm ($\Omega$) mesuré par l'Ohmmètre.", "isCorrect": False},
                        {"text": "Le Watt ($\text{W}$) mesuré par le Wattmètre.", "isCorrect": False}
                    ],
                    "correction": "La **Tension** est la différence de potentiel."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est l'unité de mesure de l'**Intensité du courant (I)** et comment doit-on brancher l'appareil de mesure ?",
                    "answerOptions": [
                        {"text": "Le Volt ($\text{V}$), en parallèle.", "isCorrect": False},
                        {"text": "L'Ampère ($\text{A}$), branché en Série (ou pince ampèremétrique en induction).", "isCorrect": True},
                        {"text": "L'Ohm ($\Omega$), en parallèle.", "isCorrect": False},
                        {"text": "Le Watt ($\text{W}$), en série.", "isCorrect": False}
                    ],
                    "correction": "L'**Ampèremètre** mesure le flux d'électrons, donc il doit être traversé par le courant (série)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est l'unité de mesure de la **Résistance (R)** et comment doit-on mesurer cette grandeur ?",
                    "answerOptions": [
                        {"text": "Le Volt ($\text{V}$), sous tension.", "isCorrect": False},
                        {"text": "L'Ohm ($\Omega$), mesurée Hors Tension (avec l'Ohmmètre) pour éviter d'endommager le multimètre.", "isCorrect": True},
                        {"text": "L'Ampère ($\text{A}$), sous tension.", "isCorrect": False},
                        {"text": "Le Watt ($\text{W}$), sous tension.", "isCorrect": False}
                    ],
                    "correction": "La mesure de la **Résistance** se fait toujours HORS TENSION."
                },
                {
                    "questionNumber": 24,
                    "question": "Selon la **Loi d'Ohm**, si l'on double la résistance (R) d'un circuit tout en maintenant la tension (U) constante, que se passe-t-il pour l'intensité (I) ?",
                    "answerOptions": [
                        {"text": "Elle double.", "isCorrect": False},
                        {"text": "Elle est divisée par deux (car $\text{I} = \text{U} / \text{R}$).", "isCorrect": True},
                        {"text": "Elle reste identique.", "isCorrect": False},
                        {"text": "Elle est multipliée par quatre.", "isCorrect": False}
                    ],
                    "correction": "La **Loi d'Ohm** est la relation fondamentale $\text{U} = \text{R} \times \text{I}$."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la formule pour calculer la **Puissance électrique active (P)** en courant continu (CC) ou en monophasé (avec facteur de puissance idéal) ?",
                    "answerOptions": [
                        {"text": "$\text{P} = \text{R} + \text{I}$", "isCorrect": False},
                        {"text": "$\text{P} = \text{U} \times \text{I}$ ($\text{P}$ en Watts, $\text{U}$ en Volts, $\text{I}$ en Ampères).", "isCorrect": True},
                        {"text": "$\text{P} = \text{U} / \text{I}$", "isCorrect": False},
                        {"text": "$\text{P} = \text{R} \times \text{U}$", "isCorrect": False}
                    ],
                    "correction": "La **Puissance** est le produit de la tension par l'intensité."
                },
                {
                    "questionNumber": 26,
                    "question": "Que représente la grandeur mesurée en **Joules ($\text{J}$) ou en kilowattheures ($\text{kWh}$)** ?",
                    "answerOptions": [
                        {"text": "La Tension.", "isCorrect": False},
                        {"text": "L'Énergie (ou Travail) électrique consommée.", "isCorrect": True},
                        {"text": "La Puissance.", "isCorrect": False},
                        {"text": "La Résistance.", "isCorrect": False}
                    ],
                    "correction": "L'**Énergie** est la puissance consommée sur une durée ($\text{E} = \text{P} \times \text{t}$)."
                },
                {
                    "questionNumber": 27,
                    "question": "Dans le système de distribution standard en France, quelle est la **Tension efficace (U) nominale** entre Phase et Neutre ?",
                    "answerOptions": [
                        {"text": "$12 \text{ V}$", "isCorrect": False},
                        {"text": "$230 \text{ V}$ (Tolérance $220 \text{ V}$ à $240 \text{ V}$)", "isCorrect": True},
                        {"text": "$400 \text{ V}$", "isCorrect": False},
                        {"text": "$110 \text{ V}$", "isCorrect": False}
                    ],
                    "correction": "La **Tension** monophasée est de $230 \text{ V}$."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la **Fréquence** nominale du courant alternatif (CA) sur le réseau français ?",
                    "answerOptions": [
                        {"text": "$60 \text{ Hz}$", "isCorrect": False},
                        {"text": "$50 \text{ Hz}$ (le courant change de sens 50 fois par seconde)", "isCorrect": True},
                        {"text": "$100 \text{ Hz}$", "isCorrect": False},
                        {"text": "$0 \text{ Hz}$ (courant continu)", "isCorrect": False}
                    ],
                    "correction": "La **Fréquence** de $50 \text{ Hz}$ est la norme européenne."
                },
                {
                    "questionNumber": 29,
                    "question": "Comment calcule-t-on la **Résistance totale (R\textsubscript{eq})** de deux résistances montées en **SÉRIE** ?",
                    "answerOptions": [
                        {"text": "L'inverse de la somme des inverses.", "isCorrect": False},
                        {"text": "La somme des résistances ($\text{R}_\text{eq} = \text{R}_1 + \text{R}_2$).", "isCorrect": True},
                        {"text": "La moyenne des résistances.", "isCorrect": False},
                        {"text": "Le produit des résistances.", "isCorrect": False}
                    ],
                    "correction": "En **Série**, la résistance augmente (addition)."
                },
                {
                    "questionNumber": 30,
                    "question": "Comment doit-on brancher un **Voltmètre** pour mesurer la tension aux bornes d'un dipôle ?",
                    "answerOptions": [
                        {"text": "En série avec le dipôle.", "isCorrect": False},
                        {"text": "En Parallèle (ou dérivation) aux bornes du dipôle.", "isCorrect": True},
                        {"text": "Il n'y a pas besoin de branchement.", "isCorrect": False},
                        {"text": "Entre la phase et la terre.", "isCorrect": False}
                    ],
                    "correction": "Le **Voltmètre** mesure une différence entre deux points (parallèle)."
                },
                {
                    "questionNumber": 31,
                    "question": "Qu'est-ce qu'un **Court-Circuit** ?",
                    "answerOptions": [
                        {"text": "Une surcharge prolongée.", "isCorrect": False},
                        {"text": "Une connexion de faible résistance entre la phase et le neutre (ou une autre phase, ou la terre), entraînant une surintensité brutale et dangereuse.", "isCorrect": True},
                        {"text": "Une perte de tension.", "isCorrect": False},
                        {"text": "Un fil coupé.", "isCorrect": False}
                    ],
                    "correction": "Le **Court-Circuit** est le défaut le plus dangereux (risques d'incendie et d'arc)."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'effet d'une **Surcharge** sur les conducteurs (câbles) ?",
                    "answerOptions": [
                        {"text": "Ils deviennent plus rigides.", "isCorrect": False},
                        {"text": "Ils chauffent (Effet Joule) et peuvent provoquer la fusion de l'isolant, un court-circuit ou un incendie.", "isCorrect": True},
                        {"text": "Ils s'allongent.", "isCorrect": False},
                        {"text": "Ils deviennent plus froids.", "isCorrect": False}
                    ],
                    "correction": "La **Surcharge** est une surintensité progressive, traitée par la partie thermique du disjoncteur."
                },
                {
                    "questionNumber": 33,
                    "question": "Que signifie un **Facteur de Puissance ($\text{cos} \phi$)** proche de 1 ?",
                    "answerOptions": [
                        {"text": "Le circuit est très inductif.", "isCorrect": False},
                        {"text": "La puissance active ($\text{W}$) est égale à la puissance apparente ($\text{VA}$), ce qui indique une utilisation efficace de l'énergie (circuit purement résistif, ex: chauffage).", "isCorrect": True},
                        {"text": "Le circuit est en court-circuit.", "isCorrect": False},
                        {"text": "Le circuit est très capacitif.", "isCorrect": False}
                    ],
                    "correction": "Un $\text{cos} \phi = 1$ est l'idéal : aucune **puissance réactive** n'est gaspillée."
                },
                {
                    "questionNumber": 34,
                    "question": "Qu'est-ce qu'un circuit électrique en **Parallèle (ou dérivation)** ?",
                    "answerOptions": [
                        {"text": "Un circuit où les dipôles sont branchés les uns à la suite des autres.", "isCorrect": False},
                        {"text": "Un circuit où les dipôles sont branchés de manière à être soumis à la même tension (ex: les prises d'un circuit prises $16 \text{ A}$), et où les intensités s'additionnent.", "isCorrect": True},
                        {"text": "Un circuit qui ne fonctionne pas.", "isCorrect": False},
                        {"text": "Un circuit qui est coupé.", "isCorrect": False}
                    ],
                    "correction": "Toutes les **installations domestiques** sont montées en parallèle."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment calcule-t-on la **Résistance totale (R\textsubscript{eq})** de deux résistances montées en **PARALLÈLE** ?",
                    "answerOptions": [
                        {"text": "La somme des résistances.", "isCorrect": False},
                        {"text": "L'inverse de la somme des inverses ($1/\text{R}_\text{eq} = 1/\text{R}_1 + 1/\text{R}_2$).", "isCorrect": True},
                        {"text": "Le produit des résistances.", "isCorrect": False},
                        {"text": "La différence des résistances.", "isCorrect": False}
                    ],
                    "correction": "En **Parallèle**, la résistance diminue (le courant a plusieurs chemins)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est l'unité de la **Puissance Apparente (S)** en courant alternatif ?",
                    "answerOptions": [
                        {"text": "Le Watt ($\text{W}$).", "isCorrect": False},
                        {"text": "Le Voltampère ($\text{VA}$) ou Kilovoltampère ($\text{kVA}$).", "isCorrect": True},
                        {"text": "Le Voltampère Réactif ($\text{VAR}$).", "isCorrect": False},
                        {"text": "Le Joule ($\text{J}$).", "isCorrect": False}
                    ],
                    "correction": "La **Puissance Apparente** est le produit $\text{S} = \text{U} \times \text{I}$."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est le risque de ne pas respecter la **capacité d'un conducteur** (section en $\text{mm}^2$) ?",
                    "answerOptions": [
                        {"text": "Perte de résistance.", "isCorrect": False},
                        {"text": "Surchauffe du conducteur (par effet Joule) en cas de courant excessif, entraînant une dégradation de l'isolant et un risque d'incendie.", "isCorrect": True},
                        {"text": "Court-circuit.", "isCorrect": False},
                        {"text": "Augmentation de la tension.", "isCorrect": False}
                    ],
                    "correction": "La **Section** est définie par l'intensité maximale que le circuit doit supporter."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est le principe de la **Loi des Nœuds (ou Loi de Kirchhoff sur les courants)** dans un circuit en parallèle ?",
                    "answerOptions": [
                        {"text": "La tension est la même partout.", "isCorrect": False},
                        {"text": "La somme des courants qui arrivent à un nœud est égale à la somme des courants qui en repartent ($\Sigma \text{I}_{\text{entrant}} = \Sigma \text{I}_{\text{sortant}}$).", "isCorrect": True},
                        {"text": "L'intensité est constante dans tout le circuit.", "isCorrect": False},
                        {"text": "La résistance est nulle.", "isCorrect": False}
                    ],
                    "correction": "La **Loi des Nœuds** régit la distribution du courant en parallèle."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le principe de la **Loi des Mailles (ou Loi de Kirchhoff sur les tensions)** dans un circuit en série ?",
                    "answerOptions": [
                        {"text": "Le courant est le même partout.", "isCorrect": False},
                        {"text": "Dans une maille fermée, la somme des tensions aux bornes des dipôles est égale à la tension du générateur (ou la somme algébrique des tensions est nulle).", "isCorrect": True},
                        {"text": "La résistance est la même partout.", "isCorrect": False},
                        {"text": "La puissance est nulle.", "isCorrect": False}
                    ],
                    "correction": "La **Loi des Mailles** régit la distribution de la tension en série."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la tension efficace maximale autorisée pour être classé en **Très Basse Tension de Sécurité (TBTS)** en milieu humide (Volume 0 SDB) ?",
                    "answerOptions": [
                        {"text": "$230 \text{ V}$", "isCorrect": False},
                        {"text": "$12 \text{ V}$ (Tension de sécurité)", "isCorrect": True},
                        {"text": "$48 \text{ V}$", "isCorrect": False},
                        {"text": "$24 \text{ V}$", "isCorrect": False}
                    ],
                    "correction": "La **TBTS $12 \text{ V}$** est la seule autorisée dans le volume 0 SDB, grâce à un transformateur de sécurité."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : APPAREILLAGES ET PROTECTIONS (DISJONCTEURS, DIFFÉRENTIELS) (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Appareillages et Protections (Disjoncteurs, Différentiels) (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le rôle du **dispositif magnéto-thermique** dans un disjoncteur divisionnaire ?",
                    "answerOptions": [
                        {"text": "Le rôle du thermique est de protéger contre les courts-circuits, le rôle du magnétique contre les surcharges.", "isCorrect": False},
                        {"text": "Le **Thermique** (lame bimétallique) protège contre les surcharges prolongées (chauffage), et le **Magnétique** (électroaimant) protège contre les courts-circuits (action instantanée).", "isCorrect": True},
                        {"text": "Le rôle du thermique est d'éteindre l'arc.", "isCorrect": False},
                        {"text": "Il protège contre les fuites de courant.", "isCorrect": False}
                    ],
                    "correction": "Le **Magnétique** est rapide (court-circuit), le **Thermique** est lent (surcharge)."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la section minimale des conducteurs pour un circuit d'éclairage protégé par un disjoncteur de $10 \text{ A}$ ?",
                    "answerOptions": [
                        {"text": "$2.5 \text{ mm}^2$", "isCorrect": False},
                        {"text": "$1.5 \text{ mm}^2$ (intensité max : $16 \text{ A}$, mais limité à $10 \text{ A}$ par le disjoncteur, max $8$ points lumineux).", "isCorrect": True},
                        {"text": "$4 \text{ mm}^2$", "isCorrect": False},
                        {"text": "$6 \text{ mm}^2$", "isCorrect": False}
                    ],
                    "correction": "Le **$1.5 \text{ mm}^2$** est le standard pour l'éclairage et le disjoncteur $10 \text{ A}$."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la section minimale des conducteurs pour un circuit de prises $16 \text{ A}$ protégé par un disjoncteur de $16 \text{ A}$ ?",
                    "answerOptions": [
                        {"text": "$1.5 \text{ mm}^2$", "isCorrect": False},
                        {"text": "$2.5 \text{ mm}^2$ (max $8$ prises pour $16 \text{ A}$)", "isCorrect": True},
                        {"text": "$4 \text{ mm}^2$", "isCorrect": False},
                        {"text": "$6 \text{ mm}^2$", "isCorrect": False}
                    ],
                    "correction": "Le **$2.5 \text{ mm}^2$** est le standard pour les prises de courant $16 \text{ A}$."
                },
                {
                    "questionNumber": 44,
                    "question": "Combien de disjoncteurs différentiels $30 \text{ mA}$ (Type AC, A ou F) sont exigés au minimum par la NF C 15-100 dans un logement ?",
                    "answerOptions": [
                        {"text": "Un seul.", "isCorrect": False},
                        {"text": "Deux (un Type A ou F obligatoire pour la Plaque de Cuisson et le Lave-Linge, et un Type AC pour les circuits généraux).", "isCorrect": True},
                        {"text": "Trois.", "isCorrect": False},
                        {"text": "Quatre.", "isCorrect": False}
                    ],
                    "correction": "Le **minimum de deux** assure une continuité de service en cas de défaut sur un circuit."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle est la fonction d'un **Interrupteur Différentiel de Type A** ?",
                    "answerOptions": [
                        {"text": "Détecter uniquement les défauts de courant alternatif sinusoïdal.", "isCorrect": False},
                        {"text": "Détecter les défauts de courant alternatif sinusoïdal **et** les courants de défauts pulsés (générés par certains équipements électroniques comme les plaques à induction, lave-linge).", "isCorrect": True},
                        {"text": "Détecter uniquement les défauts de courant continu.", "isCorrect": False},
                        {"text": "Protéger contre la foudre.", "isCorrect": False}
                    ],
                    "correction": "Le **Type A** est plus performant que le Type AC pour les appareils modernes."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est l'intensité maximale autorisée par la NF C 15-100 pour un circuit spécialisé alimentant une **Plaque de Cuisson** ?",
                    "answerOptions": [
                        {"text": "$20 \text{ A}$", "isCorrect": False},
                        {"text": "$32 \text{ A}$ (avec une section de fil de $6 \text{ mm}^2$)", "isCorrect": True},
                        {"text": "$40 \text{ A}$", "isCorrect": False},
                        {"text": "$16 \text{ A}$", "isCorrect": False}
                    ],
                    "correction": "La **Plaque de Cuisson** est le circuit le plus consommateur et nécessite la plus grosse section de fil."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le rôle de la **Borne de raccordement principal (Barrette de coupure)** sur le circuit de Terre (PE) ?",
                    "answerOptions": [
                        {"text": "Elle augmente l'intensité.", "isCorrect": False},
                        {"text": "Elle permet de déconnecter l'installation de la prise de terre pour mesurer la valeur de la résistance de la prise de terre (Contrôle de l'impédance de boucle).", "isCorrect": True},
                        {"text": "Elle réduit la résistance.", "isCorrect": False},
                        {"text": "Elle coupe la phase.", "isCorrect": False}
                    ],
                    "correction": "La **Barrette de coupure** (ou bornier de terre) est le point de test de la prise de terre."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la fonction d'un **télérupteur** dans un circuit d'éclairage ?",
                    "answerOptions": [
                        {"text": "Permettre d'allumer un point lumineux de deux endroits différents.", "isCorrect": False},
                        {"text": "Permettre d'allumer et d'éteindre un point lumineux à partir de **plus de deux** points de commande (boutons-poussoirs).", "isCorrect": True},
                        {"text": "Protéger le circuit.", "isCorrect": False},
                        {"text": "Diminuer l'intensité.", "isCorrect": False}
                    ],
                    "correction": "Le **télérupteur** est plus adapté pour plus de deux points de commande que le va-et-vient."
                },
                {
                    "questionNumber": 49,
                    "question": "Qu'est-ce qu'une **Liaison Équipotentielle Supplémentaire (LES)** dans la salle de bain ?",
                    "answerOptions": [
                        {"text": "Un circuit de chauffage.", "isCorrect": False},
                        {"text": "Un raccordement de toutes les masses métalliques (tuyauteries, cadres, armatures) entre elles et à la Terre (PE) pour mettre les potentiels à niveau et limiter le risque de choc électrique.", "isCorrect": True},
                        {"text": "Un circuit de prise de courant.", "isCorrect": False},
                        {"text": "Un disjoncteur.", "isCorrect": False}
                    ],
                    "correction": "La **LES** est obligatoire dans les volumes 1, 2 et 3 de la SDB."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le calibre maximal du disjoncteur (et section minimale des fils) pour un circuit de prises $20 \text{ A}$ ?",
                    "answerOptions": [
                        {"text": "$16 \text{ A}$ avec $2.5 \text{ mm}^2$.", "isCorrect": False},
                        {"text": "$20 \text{ A}$ avec $2.5 \text{ mm}^2$ (max $12$ prises).", "isCorrect": True},
                        {"text": "$32 \text{ A}$ avec $4 \text{ mm}^2$.", "isCorrect": False},
                        {"text": "$20 \text{ A}$ avec $4 \text{ mm}^2$.", "isCorrect": False}
                    ],
                    "correction": "Le circuit $20 \text{ A}$ (max $12$ prises) est l'exception qui tolère le **$2.5 \text{ mm}^2$**."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le rôle d'un **Contacteur Jour/Nuit** (ou Heures Pleines/Heures Creuses) ?",
                    "answerOptions": [
                        {"text": "Allumer l'éclairage de nuit.", "isCorrect": False},
                        {"text": "Commander automatiquement l'alimentation d'un circuit (généralement le chauffe-eau) pendant les heures creuses (impulsion du distributeur d'énergie).", "isCorrect": True},
                        {"text": "Protéger contre la foudre.", "isCorrect": False},
                        {"text": "Réduire la tension.", "isCorrect": False}
                    ],
                    "correction": "Le **Contacteur Jour/Nuit** est un circuit spécialisé du tableau électrique."
                },
                {
                    "questionNumber": 52,
                    "question": "Qu'est-ce qu'un **Bornier de raccordement automatique** (Wago, par exemple) ?",
                    "answerOptions": [
                        {"text": "Une prise de courant.", "isCorrect": False},
                        {"text": "Un système de connexion rapide (sans vis) permettant de relier plusieurs conducteurs dans une boîte de dérivation, garantissant une connexion fiable et sécurisée.", "isCorrect": True},
                        {"text": "Un disjoncteur.", "isCorrect": False},
                        {"text": "Un interrupteur.", "isCorrect": False}
                    ],
                    "correction": "Les **Wagos** sont la norme dans les installations modernes."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est l'utilité d'un **Interrupteur Bipolaire** (coupe phase et neutre) ?",
                    "answerOptions": [
                        {"text": "Il est plus rapide à installer.", "isCorrect": False},
                        {"text": "Il assure une coupure totale du circuit (Phase et Neutre) pour garantir une sécurité accrue dans certaines zones (cuisine, extérieur, appareil fixe de forte puissance).", "isCorrect": True},
                        {"text": "Il est plus petit.", "isCorrect": False},
                        {"text": "Il est plus esthétique.", "isCorrect": False}
                    ],
                    "correction": "L'**Interrupteur Bipolaire** assure une sécurité d'accès totale à l'appareil."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'élément qui permet de relier électriquement tous les **fils de Terre (PE)** du tableau électrique au bornier principal de terre ?",
                    "answerOptions": [
                        {"text": "Le peigne d'alimentation.", "isCorrect": False},
                        {"text": "Le Bloc de jonction (ou bornier) de Terre.", "isCorrect": True},
                        {"text": "Le disjoncteur général.", "isCorrect": False},
                        {"text": "Le fil de phase.", "isCorrect": False}
                    ],
                    "correction": "Le **Bornier de Terre** assure la continuité du circuit de protection."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est la fonction d'un **Parafoudre** (ou parasurtenseur) ?",
                    "answerOptions": [
                        {"text": "Protéger contre les surcharges.", "isCorrect": False},
                        {"text": "Protéger les installations contre les surtensions transitoires (éclairs de foudre, manœuvres réseau) en dérivant l'excès de courant vers la terre.", "isCorrect": True},
                        {"text": "Protéger contre les courts-circuits.", "isCorrect": False},
                        {"text": "Protéger contre les fuites de courant.", "isCorrect": False}
                    ],
                    "correction": "Le **Parafoudre** est obligatoire dans certaines régions à forte densité de foudroiement."
                },
                {
                    "questionNumber": 56,
                    "question": "Qu'est-ce qu'une **Liaison Équipotentielle Principale (LEP)** ?",
                    "answerOptions": [
                        {"text": "Le circuit d'éclairage.", "isCorrect": False},
                        {"text": "Un raccordement de la borne principale de terre à la canalisation d'eau, de gaz, de chauffage, et à l'ossature métallique du bâtiment.", "isCorrect": True},
                        {"text": "Un circuit de prise de courant.", "isCorrect": False},
                        {"text": "Un circuit de ventilation.", "isCorrect": False}
                    ],
                    "correction": "La **LEP** assure que tous les éléments conducteurs sont au même potentiel que la terre."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est l'élément qui permet d'alimenter en tension les bornes supérieures des disjoncteurs divisionnaires ?",
                    "answerOptions": [
                        {"text": "Les fils de phase et neutre.", "isCorrect": False},
                        {"text": "Le Peigne horizontal (ou peigne d'alimentation) qui se clipse sur les bornes de l'interrupteur différentiel et des disjoncteurs.", "isCorrect": True},
                        {"text": "La GTL.", "isCorrect": False},
                        {"text": "Le tableau de communication.", "isCorrect": False}
                    ],
                    "correction": "Le **Peigne** remplace les ponts de fils pour un câblage propre et fiable."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le calibre de disjoncteur approprié pour un chauffe-eau électrique (ou ballon d'eau chaude) ?",
                    "answerOptions": [
                        {"text": "$10 \text{ A}$", "isCorrect": False},
                        {"text": "$20 \text{ A}$ (avec une section de fil de $2.5 \text{ mm}^2$ si le chauffe-eau est raccordé sur une boîte de connexion).", "isCorrect": True},
                        {"text": "$32 \text{ A}$", "isCorrect": False},
                        {"text": "$16 \text{ A}$", "isCorrect": False}
                    ],
                    "correction": "Le **Chauffe-eau** est un circuit spécialisé de $20 \text{ A}$."
                },
                {
                    "questionNumber": 59,
                    "question": "Que signifie la courbe de déclenchement **C** pour un disjoncteur divisionnaire ?",
                    "answerOptions": [
                        {"text": "Usage domestique pour les circuits très inductifs (moteurs).", "isCorrect": False},
                        {"text": "Usage domestique et tertiaire standard, déclenchement magnétique entre $5$ et $10$ fois l'intensité nominale (standard pour prises et éclairage).", "isCorrect": True},
                        {"text": "Usage tertiaire, déclenchement très rapide.", "isCorrect": False},
                        {"text": "Usage industriel, déclenchement très lent.", "isCorrect": False}
                    ],
                    "correction": "La **Courbe C** est la plus courante dans les logements."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle de la **Borne de raccordement d'un interrupteur différentiel** marquée **Test** ?",
                    "answerOptions": [
                        {"text": "Mesurer la tension.", "isCorrect": False},
                        {"text": "Vérifier le bon fonctionnement du mécanisme de détection de fuite (la manette doit disjoncter lorsque l'on appuie sur le bouton Test).", "isCorrect": True},
                        {"text": "Régler la sensibilité.", "isCorrect": False},
                        {"text": "Couper la tension.", "isCorrect": False}
                    ],
                    "correction": "Le **Bouton Test** doit être actionné régulièrement pour vérifier la fonctionnalité de la protection des personnes."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : INSTALLATIONS DOMESTIQUES (TABLEAUX, RACCORDEMENT) (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Installations Domestiques (Tableaux, Raccordement) (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la hauteur minimale d'installation d'une prise de courant dans un logement (hors SDB) ?",
                    "answerOptions": [
                        {"text": "$0.50$ m du sol.", "isCorrect": False},
                        {"text": "$0.05$ m (5 cm) du sol fini (pour la prise de courant), et $0.90 \text{ m}$ à $1.30 \text{ m}$ pour l'interrupteur.", "isCorrect": True},
                        {"text": "$0.10$ m du sol.", "isCorrect": False},
                        {"text": "$0.30$ m du sol.", "isCorrect": False}
                    ],
                    "correction": "Les **prises** peuvent être installées très bas (y compris dans les plinthes)."
                },
                {
                    "questionNumber": 62,
                    "question": "Dans le cas d'une alimentation en triphasé ($400 \text{ V}$), quelle est la tension entre une Phase et le Neutre ?",
                    "answerOptions": [
                        {"text": "$400 \text{ V}$", "isCorrect": False},
                        {"text": "$230 \text{ V}$ ($\text{U}_{\text{Phase-Neutre}} = \text{U}_{\text{Phase-Phase}} / \sqrt{3}$)", "isCorrect": True},
                        {"text": "$120 \text{ V}$", "isCorrect": False},
                        {"text": "$100 \text{ V}$", "isCorrect": False}
                    ],
                    "correction": "En **Triphasé**, on trouve $230 \text{ V}$ Phase-Neutre et $400 \text{ V}$ entre phases."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la section de fil minimum pour alimenter un circuit de chauffage électrique de $4500 \text{ W}$ sous $230 \text{ V}$ ?",
                    "answerOptions": [
                        {"text": "$1.5 \text{ mm}^2$ (max $3500 \text{ W}$ pour $16 \text{ A}$)", "isCorrect": False},
                        {"text": "$2.5 \text{ mm}^2$ (max $4600 \text{ W}$ pour $20 \text{ A}$)", "isCorrect": True},
                        {"text": "$4 \text{ mm}^2$ (max $5750 \text{ W}$ pour $25 \text{ A}$)", "isCorrect": False},
                        {"text": "$6 \text{ mm}^2$ (max $7200 \text{ W}$ pour $32 \text{ A}$)", "isCorrect": False}
                    ],
                    "correction": "Le $4500 \text{ W}$ nécessite un disjoncteur $20 \text{ A}$ (donc $2.5 \text{ mm}^2$)."
                },
                {
                    "questionNumber": 64,
                    "question": "Que doit-on impérativement réaliser avant de fixer un câble sur un support (mur, plinthe) ?",
                    "answerOptions": [
                        {"text": "Le peindre.", "isCorrect": False},
                        {"text": "Le repérer (étiqueter l'extrémité) pour identifier sa fonction (ex: prise cuisine, éclairage SDB) avant de le gainer/clipser.", "isCorrect": True},
                        {"text": "Le tordre.", "isCorrect": False},
                        {"text": "Le couper.", "isCorrect": False}
                    ],
                    "correction": "Le **Repérage** (identification des circuits) est essentiel pour le dépannage futur."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le rôle de la **Boîte de dérivation** dans une installation encastrée ?",
                    "answerOptions": [
                        {"text": "Cacher les fils.", "isCorrect": False},
                        {"text": "Permettre le raccordement (via des borniers) des différentes dérivations d'un circuit (ex: un départ pour les prises A, un départ pour les prises B) et rester accessible pour la maintenance.", "isCorrect": True},
                        {"text": "Couper la tension.", "isCorrect": False},
                        {"text": "Protéger contre le court-circuit.", "isCorrect": False}
                    ],
                    "correction": "Les **boîtes de dérivation** doivent rester accessibles (derrière un meuble non vissé, ou une trappe)."
                },
                {
                    "questionNumber": 66,
                    "question": "Qu'est-ce qu'un circuit **Spécialisé** selon la NF C 15-100 ?",
                    "answerOptions": [
                        {"text": "Un circuit qui alimente plus de $8$ prises.", "isCorrect": False},
                        {"text": "Un circuit dédié à un seul appareil de forte puissance (ex: chauffe-eau, four, plaque de cuisson, lave-linge), qui ne peut alimenter aucun autre appareil ou point lumineux.", "isCorrect": True},
                        {"text": "Un circuit de faible tension.", "isCorrect": False},
                        {"text": "Un circuit de prises avec disjoncteur $16 \text{ A}$.", "isCorrect": False}
                    ],
                    "correction": "Les **circuits spécialisés** garantissent la puissance nécessaire aux gros électroménagers."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la section minimale des conducteurs pour la **Liaison Équipotentielle Principale (LEP)** ?",
                    "answerOptions": [
                        {"text": "$1.5 \text{ mm}^2$", "isCorrect": False},
                        {"text": "$6 \text{ mm}^2$ (conducteur Cuivre nu ou isolé)", "isCorrect": True},
                        {"text": "$2.5 \text{ mm}^2$", "isCorrect": False},
                        {"text": "$10 \text{ mm}^2$", "isCorrect": False}
                    ],
                    "correction": "La **LEP** doit être de forte section pour évacuer les courants de défaut importants."
                },
                {
                    "questionNumber": 68,
                    "question": "Qu'est-ce qu'une **pieuvre électrique** (ou kit pré-câblé) ?",
                    "answerOptions": [
                        {"text": "Un raccordement complexe.", "isCorrect": False},
                        {"text": "Un ensemble de gaines et de boîtes de dérivation pré-monté en usine selon les plans du logement, reliant le tableau aux points d'utilisation pour accélérer l'installation sur chantier.", "isCorrect": True},
                        {"text": "Un système de ventilation.", "isCorrect": False},
                        {"text": "Un système de chauffage.", "isCorrect": False}
                    ],
                    "correction": "La **Pieuvre** est une méthode de câblage moderne pour le neuf."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle est la protection maximale autorisée pour un circuit d'éclairage si on utilise un câble de section $1.5 \text{ mm}^2$ ?",
                    "answerOptions": [
                        {"text": "Disjoncteur $10 \text{ A}$ (max 8 points lumineux).", "isCorrect": True},
                        {"text": "Disjoncteur $16 \text{ A}$.", "isCorrect": False},
                        {"text": "Disjoncteur $20 \text{ A}$.", "isCorrect": False},
                        {"text": "Disjoncteur $32 \text{ A}$.", "isCorrect": False}
                    ],
                    "correction": "Le **$10 \text{ A}$** est la protection standard pour les circuits $1.5 \text{ mm}^2$ (éclairage)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle est la fonction d'un **Bornier Phase/Neutre** (ou barrette) dans un tableau électrique ?",
                    "answerOptions": [
                        {"text": "Alimenter le disjoncteur général.", "isCorrect": False},
                        {"text": "Permettre la connexion des fils de Phase et de Neutre en amont des interrupteurs différentiels (alimentation de l'ensemble du tableau).", "isCorrect": True},
                        {"text": "Protéger contre la foudre.", "isCorrect": False},
                        {"text": "Mesurer la résistance.", "isCorrect": False}
                    ],
                    "correction": "Le **Bornier** est l'arrivée du courant au tableau (après le compteur)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est l'exigence de la NF C 15-100 concernant l'accessibilité des **Boîtes de dérivation** ?",
                    "answerOptions": [
                        {"text": "Elles doivent être soudées.", "isCorrect": False},
                        {"text": "Elles doivent être accessibles et visitables (pas de scellement) pour pouvoir intervenir en cas de panne ou de modification du circuit.", "isCorrect": True},
                        {"text": "Elles doivent être en métal.", "isCorrect": False},
                        {"text": "Elles doivent être peintes.", "isCorrect": False}
                    ],
                    "correction": "L'**Accessibilité** est primordiale pour la maintenance."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le risque de ne pas utiliser de **gaine protectrice** (ICTA) pour les conducteurs encastrés dans les murs ?",
                    "answerOptions": [
                        {"text": "Les fils chauffent.", "isCorrect": False},
                        {"text": "Dégradation des isolants par le mortier (chaux) ou le béton, impossibilité de remplacer les fils en cas de panne ou de modification future.", "isCorrect": True},
                        {"text": "Les fils s'allongent.", "isCorrect": False},
                        {"text": "Les fils se coupent.", "isCorrect": False}
                    ],
                    "correction": "La **Gaine ICTA** assure la protection mécanique et la possibilité de tirer des fils."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la couleur du fil qui relie un **Va-et-Vient** au point lumineux (la 'navette' retour vers la lampe) ?",
                    "answerOptions": [
                        {"text": "Bleu.", "isCorrect": False},
                        {"text": "Généralement une couleur non-normalisée (ex: Violet, Orange) pour le retour lampe (Noir/Marron pour la phase, Bleu pour le Neutre).", "isCorrect": True},
                        {"text": "Vert/Jaune.", "isCorrect": False},
                        {"text": "Rouge.", "isCorrect": False}
                    ],
                    "correction": "Le **Retour Lampe** (phase coupée) est repéré par une couleur autre que Bleu (N), V/J (T), Marron/Noir (Phase)."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle est la caractéristique d'un **Câble $\text{RO2V}$** par rapport à un câble monoconducteur ?",
                    "answerOptions": [
                        {"text": "Il est plus léger.", "isCorrect": False},
                        {"text": "Il est composé de plusieurs conducteurs isolés (Phase, Neutre, Terre) dans une gaine unique, utilisé en apparent ou en extérieur (plus résistant).", "isCorrect": True},
                        {"text": "Il est moins cher.", "isCorrect": False},
                        {"text": "Il est plus rigide.", "isCorrect": False}
                    ],
                    "correction": "Le **$\text{RO2V}$** est le câble rigide standard pour les installations non encastrées."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le nombre maximal de circuits d'éclairage autorisés sur un seul interrupteur différentiel $30 \text{ mA}$ ?",
                    "answerOptions": [
                        {"text": "Cinq.", "isCorrect": False},
                        {"text": "Huit (maximum $8$ circuits par interrupteur différentiel, qu'ils soient éclairage ou prises).", "isCorrect": True},
                        {"text": "Dix.", "isCorrect": False},
                        {"text": "Douze.", "isCorrect": False}
                    ],
                    "correction": "La **limite de $8$ circuits** assure une sélectivité suffisante en cas de défaut."
                },
                {
                    "questionNumber": 76,
                    "question": "Que signifie le marquage $\text{H} 07 \text{ V}-\text{U}$ pour un conducteur ?",
                    "answerOptions": [
                        {"text": "Conducteur souple pour $300 \text{ V}$.", "isCorrect": False},
                        {"text": "Conducteur harmonisé ($\text{H}$) sous gaine PVC pour $750 \text{ V}$ ($\text{07}$), âme rigide ($\text{U}$).", "isCorrect": True},
                        {"text": "Conducteur rigide pour $300 \text{ V}$.", "isCorrect": False},
                        {"text": "Conducteur souple pour $450 \text{ V}$.", "isCorrect": False}
                    ],
                    "correction": "Le **$\text{H} 07 \text{ V}-\text{U}$** est le fil rigide standard utilisé pour le câblage de tableau (sous gaine)."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le type de disjoncteur général (en tête de GTL) imposé par le distributeur d'énergie ?",
                    "answerOptions": [
                        {"text": "Un disjoncteur divisionnaire $10 \text{ A}$.", "isCorrect": False},
                        {"text": "Un Disjoncteur de Branchement (DB), réglable en calibre (ex: $15/30/45 \text{ A}$) avec protection différentielle $500 \text{ mA}$ (ou $300 \text{ mA}$ pour le tertiaire).", "isCorrect": True},
                        {"text": "Un interrupteur différentiel $30 \text{ mA}$.", "isCorrect": False},
                        {"text": "Un télérupteur.", "isCorrect": False}
                    ],
                    "correction": "Le **DB** assure la protection globale de l'installation et limite la puissance consommée (abonnement)."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est l'importance de l'**entraxe $13 \text{ mm}$** entre les rangées de modules dans le tableau électrique ?",
                    "answerOptions": [
                        {"text": "Assurer l'esthétique.", "isCorrect": False},
                        {"text": "Assurer la compatibilité des différents appareillages (peignes, peignes verticaux) et respecter l'espace minimum pour la circulation de l'air et le raccordement des conducteurs.", "isCorrect": True},
                        {"text": "Réduire le bruit.", "isCorrect": False},
                        {"text": "Faciliter le nettoyage.", "isCorrect": False}
                    ],
                    "correction": "L'**entraxe** standard est crucial pour l'organisation et le câblage du tableau."
                },
                {
                    "questionNumber": 79,
                    "question": "Que doit-on faire de l'extrémité d'un conducteur après l'avoir coupé et dénudé (dans un bornier à vis) ?",
                    "answerOptions": [
                        {"text": "La souder.", "isCorrect": False},
                        {"text": "Ne pas étamer (souder) l'extrémité et la laisser telle quelle (âme rigide) ou utiliser un manchon de raccordement (ferrule ou embout) pour les fils souples.", "isCorrect": True},
                        {"text": "La tordre.", "isCorrect": False},
                        {"text": "La laisser trop longue.", "isCorrect": False}
                    ],
                    "correction": "L'**étamage** est interdit dans un bornier à vis, car il se déforme (s'écrase) et crée un mauvais contact."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le nombre minimal de circuits de prise de courant dans un logement ($> 100 \text{ m}^2$) ?",
                    "answerOptions": [
                        {"text": "Deux circuits.", "isCorrect": False},
                        {"text": "Trois circuits (minimum pour les grands logements).", "isCorrect": True},
                        {"text": "Un circuit.", "isCorrect": False},
                        {"text": "Quatre circuits.", "isCorrect": False}
                    ],
                    "correction": "Le **nombre de circuits** dépend de la surface et du nombre de pièces (exigence de confort)."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SCHÉMAS ET DÉPANNAGE (SIMPLE ALLUMAGE, VA-ET-VIENT) (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Schémas et Dépannage (Simple Allumage, Va-et-Vient) (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Dans un schéma de **Simple Allumage**, quel fil est raccordé au point $\text{L}$ de l'interrupteur ?",
                    "answerOptions": [
                        {"text": "Le Neutre.", "isCorrect": False},
                        {"text": "La Phase (fil Marron, Noir ou Rouge), qui arrive directement du tableau/boîte de dérivation.", "isCorrect": True},
                        {"text": "La Terre.", "isCorrect": False},
                        {"text": "Le Retour Lampe (fil coupé, ex: Violet).", "isCorrect": False}
                    ],
                    "correction": "L'**interrupteur** coupe toujours la phase."
                },
                {
                    "questionNumber": 82,
                    "question": "Dans un schéma de **Va-et-Vient**, combien de conducteurs (hors terre) circulent dans la gaine entre les deux interrupteurs ?",
                    "answerOptions": [
                        {"text": "Un seul (Phase).", "isCorrect": False},
                        {"text": "Deux (les deux navettes).", "isCorrect": True},
                        {"text": "Trois (Phase, Neutre, Retour Lampe).", "isCorrect": False},
                        {"text": "Quatre (Phase, Neutre, 2 Navettes).", "isCorrect": False}
                    ],
                    "correction": "Les **Navettes** sont les deux fils qui relient les bornes $\text{L}_1$ et $\text{L}_2$ des deux interrupteurs."
                },
                {
                    "questionNumber": 83,
                    "question": "Qu'est-ce qu'un **Schéma architectural** (ou plan d'implantation) ?",
                    "answerOptions": [
                        {"text": "Le schéma décrivant les connexions internes d'un circuit.", "isCorrect": False},
                        {"text": "Le plan de la pièce (à l'échelle) indiquant l'emplacement physique (implantation) de tous les appareillages (interrupteurs, prises, luminaires) dans le logement.", "isCorrect": True},
                        {"text": "Le schéma unifilaire.", "isCorrect": False},
                        {"text": "Le schéma développé.", "isCorrect": False}
                    ],
                    "correction": "Le **Schéma architectural** est le guide de l'installation sur chantier."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la cause la plus probable d'un **disjoncteur différentiel qui saute** (déclenche) de manière intempestive ?",
                    "answerOptions": [
                        {"text": "Surtension.", "isCorrect": False},
                        {"text": "Fuite de courant à la terre (défaut d'isolement) due à l'humidité, à un appareil défectueux, ou à un rongeur (l'intensité Phase est différente de l'intensité Neutre).", "isCorrect": True},
                        {"text": "Court-circuit.", "isCorrect": False},
                        {"text": "Surcharge.", "isCorrect": False}
                    ],
                    "correction": "Le **DDR** ne réagit qu'aux fuites de courant."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est l'outil de mesure utilisé pour identifier une **coupure (fil cassé)** dans un conducteur ?",
                    "answerOptions": [
                        {"text": "Le voltmètre.", "isCorrect": False},
                        {"text": "L'Ohmmètre (mesure d'une résistance infinie) ou le test de continuité (avertisseur sonore) HORS TENSION.", "isCorrect": True},
                        {"text": "L'ampèremètre.", "isCorrect": False},
                        {"text": "Le wattmètre.", "isCorrect": False}
                    ],
                    "correction": "Un **fil coupé** se traduit par une résistance infinie ($\infty$) mesurée à l'Ohmmètre."
                },
                {
                    "questionNumber": 86,
                    "question": "Dans un schéma de **télérupteur**, quel est le rôle des **boutons-poussoirs** ?",
                    "answerOptions": [
                        {"text": "Ils coupent la tension en permanence.", "isCorrect": False},
                        {"text": "Ils envoient une brève impulsion de courant à la bobine du télérupteur (fil de commande) pour inverser son état (ON/OFF).", "isCorrect": True},
                        {"text": "Ils alimentent la lampe directement.", "isCorrect": False},
                        {"text": "Ils mesurent la tension.", "isCorrect": False}
                    ],
                    "correction": "Le **bouton-poussoir** fonctionne comme une sonnette (il ne tient pas la position ON)."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est l'appareil de mesure le plus adapté pour identifier un **Court-Circuit franc** (résistance presque nulle) ?",
                    "answerOptions": [
                        {"text": "Le voltmètre (en $\text{V} \text{ c.a.}$).", "isCorrect": False},
                        {"text": "L'Ohmmètre (mesure d'une résistance très faible) ou le multimètre en test de continuité (bip fort).", "isCorrect": True},
                        {"text": "Le wattmètre.", "isCorrect": False},
                        {"text": "La pince ampèremétrique.", "isCorrect": False}
                    ],
                    "correction": "Le **Court-Circuit** est une résistance très faible."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'un **Schéma Multifilaire** ?",
                    "answerOptions": [
                        {"text": "Un schéma qui utilise des symboles simples.", "isCorrect": False},
                        {"text": "Un schéma où chaque conducteur (Phase, Neutre, Terre, Navettes, etc.) est représenté individuellement par un trait (schéma le plus détaillé pour le câblage).", "isCorrect": True},
                        {"text": "Un schéma qui représente uniquement le circuit de puissance.", "isCorrect": False},
                        {"text": "Un schéma qui représente les fils d'un seul circuit.", "isCorrect": False}
                    ],
                    "correction": "Le **Schéma multifilaire** est le plus proche de la réalité du câblage."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la cause la plus probable d'un **disjoncteur divisionnaire qui saute** après $10 \text{ minutes}$ de fonctionnement du circuit ?",
                    "answerOptions": [
                        {"text": "Court-circuit (déclenchement instantané).", "isCorrect": False},
                        {"text": "Surcharge prolongée (déclenchement du thermique après chauffe) due à un nombre trop important d'appareils branchés sur le circuit (consommation supérieure au calibre du disjoncteur).", "isCorrect": True},
                        {"text": "Fuite de courant.", "isCorrect": False},
                        {"text": "Surtension.", "isCorrect": False}
                    ],
                    "correction": "Le **Déclenchement lent** est caractéristique du défaut thermique (surcharge)."
                },
                {
                    "questionNumber": 90,
                    "question": "Dans un schéma de **Va-et-Vient**, quel est le rôle des bornes $\text{L}$ des deux interrupteurs ?",
                    "answerOptions": [
                        {"text": "Les bornes $\text{L}$ sont connectées aux navettes.", "isCorrect": False},
                        {"text": "L'une reçoit la Phase (arrivée du courant) et l'autre est connectée au Retour Lampe (départ du courant vers la lampe).", "isCorrect": True},
                        {"text": "Les deux bornes $\text{L}$ sont connectées au Neutre.", "isCorrect": False},
                        {"text": "Les deux bornes $\text{L}$ sont connectées à la Terre.", "isCorrect": False}
                    ],
                    "correction": "Les bornes $\text{L}_1$ et $\text{L}_2$ sont pour les navettes (les $\text{L}$ (ou $\text{C}$) sont les communs Phase/Retour Lampe)."
                },
                {
                    "questionNumber": 91,
                    "question": "Qu'est-ce qu'un **Schéma Unifilaire** ?",
                    "answerOptions": [
                        {"text": "Un schéma qui représente chaque fil.", "isCorrect": False},
                        {"text": "Un schéma qui représente les liaisons entre les appareillages par un seul trait (unifilaire) et le nombre de conducteurs par des petits traits obliques (le plus rapide pour la conception).", "isCorrect": True},
                        {"text": "Un schéma qui représente uniquement le circuit de commande.", "isCorrect": False},
                        {"text": "Un schéma qui ne représente pas les fils.", "isCorrect": False}
                    ],
                    "correction": "Le **Schéma unifilaire** est la représentation symbolique officielle pour les plans."
                },
                {
                    "questionNumber": 92,
                    "question": "Comment s'appelle l'opération qui consiste à vérifier la **valeur de la résistance de la prise de terre** ?",
                    "answerOptions": [
                        {"text": "Mesure de tension.", "isCorrect": False},
                        {"text": "Mesure de la boucle de terre ou Mesure par Piquets (Méthode des trois piquets ou du telluromètre).", "isCorrect": True},
                        {"text": "Mesure d'intensité.", "isCorrect": False},
                        {"text": "Mesure de la puissance.", "isCorrect": False}
                    ],
                    "correction": "La **Mesure de terre** doit être inférieure à $100 \Omega$ pour la NF C 15-100."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le risque de croiser accidentellement le **Neutre** et la **Terre** dans une installation ?",
                    "answerOptions": [
                        {"text": "Le circuit ne fonctionne pas.", "isCorrect": False},
                        {"text": "Le différentiel risque de ne plus détecter de défaut (il est shunté) ou de disjoncter sans raison (courant de défaut permanent via la terre).", "isCorrect": True},
                        {"text": "Le circuit est trop puissant.", "isCorrect": False},
                        {"text": "Le circuit est trop faible.", "isCorrect": False}
                    ],
                    "correction": "La confusion **Neutre/Terre** est un défaut grave de raccordement."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le symbole schématique d'un **point lumineux commandé** (plafonnier) ?",
                    "answerOptions": [
                        {"text": "Un cercle avec un $\text{S}$ au milieu.", "isCorrect": False},
                        {"text": "Un cercle barré d'une croix ($\text{X}$) au milieu (ou d'un point).", "isCorrect": True},
                        {"text": "Un rectangle avec un $\text{P}$ au milieu.", "isCorrect": False},
                        {"text": "Un carré avec un $\text{L}$ au milieu.", "isCorrect": False}
                    ],
                    "correction": "Le cercle avec la croix est le symbole standard du **luminaire**."
                },
                {
                    "questionNumber": 95,
                    "question": "Comment s'appelle le schéma qui montre les connexions internes d'un module (ex: télérupteur) avec les bobines et les contacts ?",
                    "answerOptions": [
                        {"text": "Schéma unifilaire.", "isCorrect": False},
                        {"text": "Schéma Développé (ou littéral) qui est indispensable pour comprendre la logique de fonctionnement et pour le câblage de circuits complexes.", "isCorrect": True},
                        {"text": "Schéma architectural.", "isCorrect": False},
                        {"text": "Schéma de puissance.", "isCorrect": False}
                    ],
                    "correction": "Le **Schéma développé** est le plus didactique."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est le risque de ne pas respecter l'ordre de raccordement **Phase, Neutre, Terre** sur une prise de courant ?",
                    "answerOptions": [
                        {"text": "La prise ne tient pas au mur.", "isCorrect": False},
                        {"text": "Danger d'électrocution (la tension est présente sur la prise femelle) ou risque de destruction de l'appareil par inversion Phase/Neutre sur certains appareils sensibles.", "isCorrect": True},
                        {"text": "Le disjoncteur saute.", "isCorrect": False},
                        {"text": "Le voyant s'allume.", "isCorrect": False}
                    ],
                    "correction": "Le **respect de la polarité** est obligatoire, même si la prise peut fonctionner (risque de sécurité)."
                },
                {
                    "questionNumber": 97,
                    "question": "Comment teste-t-on le bon fonctionnement d'un **Va-et-Vient** après le câblage ?",
                    "answerOptions": [
                        {"text": "On mesure la tension aux bornes de la lampe.", "isCorrect": False},
                        {"text": "En actionnant les deux interrupteurs alternativement : le point lumineux doit s'allumer ou s'éteindre quel que soit l'état de l'autre interrupteur.", "isCorrect": True},
                        {"text": "On mesure la résistance des navettes.", "isCorrect": False},
                        {"text": "On coupe la tension et on teste la continuité.", "isCorrect": False}
                    ],
                    "correction": "Le **Va-et-Vient** permet de commander un luminaire de deux points distincts."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le rôle du **fil pilote** (souvent Noir ou Gris) dans un circuit de chauffage électrique ?",
                    "answerOptions": [
                        {"text": "Alimenter le radiateur.", "isCorrect": False},
                        {"text": "Recevoir des ordres de commande (Confort, Économie, Hors-Gel, Arrêt) d'un programmateur centralisé pour réguler la température des radiateurs.", "isCorrect": True},
                        {"text": "Relier à la terre.", "isCorrect": False},
                        {"text": "Relier au neutre.", "isCorrect": False}
                    ],
                    "correction": "Le **Fil pilote** est le fil de commande du chauffage électrique."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle est la méthode de dépannage la plus rapide pour identifier un **disjoncteur différentiel défectueux** ?",
                    "answerOptions": [
                        {"text": "Le remplacer.", "isCorrect": False},
                        {"text": "Tester la tension en amont (arrivée) et en aval (départ) du différentiel : si la tension est présente en amont mais pas en aval (et que le bouton Test ne fonctionne plus), il est défectueux.", "isCorrect": True},
                        {"text": "Mesurer la résistance.", "isCorrect": False},
                        {"text": "Mesurer l'intensité.", "isCorrect": False}
                    ],
                    "correction": "La **Mesure de Tension** est la première étape du diagnostic."
                },
                {
                    "questionNumber": 100,
                    "question": "Dans le cas d'une panne, si le **Neutre** est coupé mais la **Phase** est toujours présente, que se passe-t-il lorsque l'on teste la tension aux bornes d'un luminaire ?",
                    "answerOptions": [
                        {"text": "Le luminaire s'allume.", "isCorrect": False},
                        {"text": "Le voltmètre peut indiquer $0 \text{ V}$ ou une tension très faible (par manque de boucle), mais le luminaire ne s'allume pas, et le fil de Phase reste dangereux (la phase est présente).", "isCorrect": True},
                        {"text": "Le disjoncteur saute.", "isCorrect": False},
                        {"text": "Le luminaire clignote.", "isCorrect": False}
                    ],
                    "correction": "Une coupure de **Neutre** est souvent difficile à détecter au voltmètre si la charge est faible ou absente, mais le circuit est inopérant."
                },
            ]
        }
    }
}