quiz_data = {
    "title": "Quiz Bac Pro Maintenance des Véhicules (Option VP) (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MOTORISATION ET PÉRIPHÉRIQUES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : MOTORISATION ET PÉRIPHÉRIQUES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel composant relie le piston au vilebrequin et transforme le mouvement rectiligne en mouvement rotatif ?",
                    "answerOptions": [
                        {"text": "Bielle", "isCorrect": True},
                        {"text": "Arbre à cames en tête", "isCorrect": False},
                        {"text": "Volant moteur bi-masse", "isCorrect": False},
                        {"text": "Collecteur d'admission variable", "isCorrect": False}
                    ],
                    "correction": "La bielle est la pièce mécanique intermédiaire qui assure la liaison cinématique entre l'axe du piston et le maneton du vilebrequin."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la fonction principale du thermostat dans le circuit de refroidissement ?",
                    "answerOptions": [
                        {"text": "Réguler la température moteur", "isCorrect": True},
                        {"text": "Refroidir directement le liquide de refroidissement", "isCorrect": False},
                        {"text": "Augmenter la pression dans le circuit d'eau", "isCorrect": False},
                        {"text": "Filtrer les impuretés présentes dans le liquide", "isCorrect": False}
                    ],
                    "correction": "Le thermostat (ou calorstat) s'ouvre et se ferme en fonction de la chaleur pour permettre au liquide de circuler vers le radiateur uniquement lorsque le moteur a atteint sa température de fonctionnement optimale."
                },
                {
                    "questionNumber": 3,
                    "question": "Sur un moteur à quatre temps, que se passe-t-il exactement lors de la phase d'admission ?",
                    "answerOptions": [
                        {"text": "Le piston descend et la soupape d'admission est ouverte", "isCorrect": True},
                        {"text": "Le piston monte et les deux soupapes sont fermées", "isCorrect": False},
                        {"text": "Le piston descend et la soupape d'échappement est ouverte", "isCorrect": False},
                        {"text": "Le piston monte et la soupape d'admission est ouverte", "isCorrect": False}
                    ],
                    "correction": "Pendant l'admission, la descente du piston crée une dépression qui aspire le mélange air-carburant (ou l'air seul en diesel) à travers la soupape d'admission ouverte."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le rôle du turbocompresseur ?",
                    "answerOptions": [
                        {"text": "Suralimenter le moteur en air", "isCorrect": True},
                        {"text": "Augmenter la vitesse de rotation des roues", "isCorrect": False},
                        {"text": "Refroidir les gaz d'échappement", "isCorrect": False},
                        {"text": "Remplacer l'alternateur pour charger la batterie", "isCorrect": False}
                    ],
                    "correction": "Le turbo utilise l'énergie des gaz d'échappement pour entraîner une turbine qui comprime l'air d'admission, augmentant ainsi la masse d'oxygène dans les cylindres."
                },
                {
                    "questionNumber": 5,
                    "question": "Dans une rampe commune (Common Rail), quelle est la pression moyenne d'injection actuelle ?",
                    "answerOptions": [
                        {"text": "Entre 1600 et 2500 bars", "isCorrect": True},
                        {"text": "Entre 5 et 10 bars", "isCorrect": False},
                        {"text": "Près de 50 000 bars", "isCorrect": False},
                        {"text": "Moins de 1 bar", "isCorrect": False}
                    ],
                    "correction": "Les systèmes Common Rail modernes travaillent à des pressions très élevées pour optimiser la pulvérisation du gazole et réduire les émissions polluantes."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle sonde informe le calculateur moteur de la quantité d'oxygène présente dans les gaz d'échappement ?",
                    "answerOptions": [
                        {"text": "Sonde Lambda", "isCorrect": True},
                        {"text": "Débitmètre d'air massique", "isCorrect": False},
                        {"text": "Capteur PMH", "isCorrect": False},
                        {"text": "Capteur de cliquetis", "isCorrect": False}
                    ],
                    "correction": "La sonde Lambda permet de réguler la richesse du mélange pour rester le plus proche possible du rapport stœchiométrique (mélange idéal)."
                },
                {
                    "questionNumber": 7,
                    "question": "Que signifie l'acronyme EGR ?",
                    "answerOptions": [
                        {"text": "Exhaust Gas Recirculation", "isCorrect": True},
                        {"text": "Electronic Gear Ratio", "isCorrect": False},
                        {"text": "Engine Global Recovery", "isCorrect": False},
                        {"text": "Emergency Gasoline Reserve", "isCorrect": False}
                    ],
                    "correction": "La vanne EGR réinjecte une partie des gaz d'échappement dans l'admission pour abaisser la température de combustion et réduire les oxydes d'azote (NOx)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la fonction d'un filtre à particules (FAP) ?",
                    "answerOptions": [
                        {"text": "Piéger les particules de carbone (suies)", "isCorrect": True},
                        {"text": "Supprimer les mauvaises odeurs de l'habitacle", "isCorrect": False},
                        {"text": "Filtrer l'huile moteur usagée", "isCorrect": False},
                        {"text": "Réguler la pression de suralimentation", "isCorrect": False}
                    ],
                    "correction": "Le FAP stocke les particules issues de la combustion du diesel et déclenche périodiquement une phase de régénération pour les brûler."
                },
                {
                    "questionNumber": 9,
                    "question": "Sur un moteur à essence, quel composant génère l'étincelle nécessaire à la combustion ?",
                    "answerOptions": [
                        {"text": "La bougie d'allumage", "isCorrect": True},
                        {"text": "L'injecteur de départ à froid", "isCorrect": False},
                        {"text": "La bougie de préchauffage", "isCorrect": False},
                        {"text": "Le condensateur d'allumage", "isCorrect": False}
                    ],
                    "correction": "L'allumage commandé nécessite une étincelle produite par la bougie grâce à la haute tension fournie par la bobine."
                },
                {
                    "questionNumber": 10,
                    "question": "À quoi sert le volant moteur ?",
                    "answerOptions": [
                        {"text": "Régulariser le mouvement du vilebrequin par son inertie", "isCorrect": True},
                        {"text": "Diriger les gaz vers le turbo", "isCorrect": False},
                        {"text": "Porter les balais de l'alternateur", "isCorrect": False},
                        {"text": "Régler le parallélisme des roues", "isCorrect": False}
                    ],
                    "correction": "Le volant moteur emmagasine de l'énergie cinétique pour lisser les saccades dues aux temps moteurs et sert de surface d'appui à l'embrayage."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le rôle de la courroie de distribution ?",
                    "answerOptions": [
                        {"text": "Synchroniser le vilebrequin et l'arbre à cames", "isCorrect": True},
                        {"text": "Entraîner les accessoires (alternateur, clim)", "isCorrect": False},
                        {"text": "Relier les roues motrices à la boîte de vitesses", "isCorrect": False},
                        {"text": "Refroidir le bloc-moteur", "isCorrect": False}
                    ],
                    "correction": "Elle assure la synchronisation entre l'ouverture des soupapes et la position des pistons pour éviter tout contact destructeur."
                },
                {
                    "questionNumber": 12,
                    "question": "Que mesure le capteur de cliquetis ?",
                    "answerOptions": [
                        {"text": "Les vibrations anormales dues à une auto-inflammation", "isCorrect": True},
                        {"text": "Le niveau sonore de l'échappement", "isCorrect": False},
                        {"text": "La pression dans le rail d'injection", "isCorrect": False},
                        {"text": "La vitesse de rotation des roues avant", "isCorrect": False}
                    ],
                    "correction": "Le capteur détecte les ondes de choc (cliquetis) pour que le calculateur puisse modifier l'avance à l'allumage."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel fluide circule dans l'échangeur air-air (intercooler) ?",
                    "answerOptions": [
                        {"text": "L'air d'admission surpressé", "isCorrect": True},
                        {"text": "Le liquide de refroidissement moteur", "isCorrect": False},
                        {"text": "L'huile de lubrification du turbo", "isCorrect": False},
                        {"text": "Le gazole de retour réservoir", "isCorrect": False}
                    ],
                    "correction": "Il sert à refroidir l'air sortant du turbo (échauffé par la compression) avant qu'il n'entre dans les cylindres."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelle est la particularité d'une injection directe par rapport à une injection indirecte ?",
                    "answerOptions": [
                        {"text": "Le carburant est injecté directement dans la chambre de combustion", "isCorrect": True},
                        {"text": "Le mélange se fait dans le collecteur d'admission", "isCorrect": False},
                        {"text": "Il n'y a pas besoin de bougies d'allumage", "isCorrect": False},
                        {"text": "La pression d'injection est beaucoup plus faible", "isCorrect": False}
                    ],
                    "correction": "En injection directe, l'injecteur débouche dans la tête du piston, permettant un dosage ultra-précis."
                },
                {
                    "questionNumber": 15,
                    "question": "Que signifie un rapport volumétrique de 10/1 ?",
                    "answerOptions": [
                        {"text": "Le mélange est compressé 10 fois par rapport à son volume initial", "isCorrect": True},
                        {"text": "Le moteur possède 10 cylindres et une seule culasse", "isCorrect": False},
                        {"text": "La consommation est de 10 litres aux 100 kilomètres", "isCorrect": False},
                        {"text": "Le réservoir est 10 fois plus grand que le moteur", "isCorrect": False}
                    ],
                    "correction": "C'est le rapport entre le volume total du cylindre (PMB) et le volume de la chambre de combustion (PMH)."
                },
                {
                    "questionNumber": 16,
                    "question": "Sur un moteur Diesel, à quoi servent les bougies de préchauffage ?",
                    "answerOptions": [
                        {"text": "Faciliter le démarrage à froid en chauffant la chambre", "isCorrect": True},
                        {"text": "Proclamer l'étincelle pour brûler le gazole", "isCorrect": False},
                        {"text": "Réchauffer le liquide de refroidissement", "isCorrect": False},
                        {"text": "Nettoyer le filtre à particules", "isCorrect": False}
                    ],
                    "correction": "Elles augmentent la température de l'air comprimé pour favoriser l'auto-inflammation lors du démarrage."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le rôle du reniflard ?",
                    "answerOptions": [
                        {"text": "Recycler les vapeurs d'huile du carter vers l'admission", "isCorrect": True},
                        {"text": "Mesurer le débit d'air entrant", "isCorrect": False},
                        {"text": "Purger l'air dans le circuit de freinage", "isCorrect": False},
                        {"text": "Informer sur la pression des pneus", "isCorrect": False}
                    ],
                    "correction": "Il évite les surpressions dans le bas moteur en réaspirant les vapeurs grasses."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la fonction d'un catalyseur trois voies (moteur essence) ?",
                    "answerOptions": [
                        {"text": "Traiter le CO, les HC et les NOx", "isCorrect": True},
                        {"text": "Réduire la consommation de 30 pour cent", "isCorrect": False},
                        {"text": "Diviser les gaz en trois sorties d'échappement", "isCorrect": False},
                        {"text": "Multiplier la puissance par trois", "isCorrect": False}
                    ],
                    "correction": "Il transforme par réactions chimiques les polluants en gaz non toxiques (CO2, N2, H2O)."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel composant assure la lubrification des pièces mobiles du moteur ?",
                    "answerOptions": [
                        {"text": "La pompe à huile", "isCorrect": True},
                        {"text": "Le compresseur de climatisation", "isCorrect": False},
                        {"text": "L'alternateur débrayable", "isCorrect": False},
                        {"text": "La pompe à eau", "isCorrect": False}
                    ],
                    "correction": "La pompe à huile aspire l'huile du carter pour l'envoyer sous pression vers les paliers et coussinets."
                },
                {
                    "questionNumber": 20,
                    "question": "Que se passe-t-il si la soupape de décharge (Wastegate) du turbo reste bloquée fermée ?",
                    "answerOptions": [
                        {"text": "Risque de surpression et de casse moteur", "isCorrect": True},
                        {"text": "Le moteur ne peut plus démarrer", "isCorrect": False},
                        {"text": "La consommation d'huile devient nulle", "isCorrect": False},
                        {"text": "Le véhicule roule uniquement en marche arrière", "isCorrect": False}
                    ],
                    "correction": "La Wastegate régule la pression. Si elle ne s'ouvre pas, le turbo s'emballe et la pression dépasse les limites admissibles."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : CHÂSSIS, TRANSMISSION ET LIAISON AU SOL (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : CHÂSSIS, TRANSMISSION ET LIAISON AU SOL",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la fonction principale de l'embrayage ?",
                    "answerOptions": [
                        {"text": "Accoupler ou désaccoupler le moteur de la boîte de vitesses", "isCorrect": True},
                        {"text": "Régler la vitesse de rotation des roues arrière", "isCorrect": False},
                        {"text": "Multiplier le couple moteur de façon permanente", "isCorrect": False},
                        {"text": "Freiner le véhicule à l'aide du moteur", "isCorrect": False}
                    ],
                    "correction": "Il permet au conducteur de changer de rapport ou d'immobiliser le véhicule sans couper le moteur."
                },
                {
                    "questionNumber": 22,
                    "question": "Dans une boîte de vitesses manuelle, à quoi servent les synchroniseurs ?",
                    "answerOptions": [
                        {"text": "Égaliser les vitesses de rotation des pignons avant engagement", "isCorrect": True},
                        {"text": "Verrouiller la marche arrière en roulant", "isCorrect": False},
                        {"text": "Lubrifier les arbres primaire et secondaire", "isCorrect": False},
                        {"text": "Informer le calculateur de la vitesse engagée", "isCorrect": False}
                    ],
                    "correction": "Ils permettent d'engager les rapports sans craquement en synchronisant les vitesses des arbres."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel organe permet aux roues d'un même essieu de tourner à des vitesses différentes en virage ?",
                    "answerOptions": [
                        {"text": "Le différentiel", "isCorrect": True},
                        {"text": "Le cardan", "isCorrect": False},
                        {"text": "La crémaillère", "isCorrect": False},
                        {"text": "Le moyeu", "isCorrect": False}
                    ],
                    "correction": "Sans différentiel, les pneus glisseraient et s'useraient prématurément en courbe, car la roue extérieure parcourt plus de chemin."
                },
                {
                    "questionNumber": 24,
                    "question": "Sur un pneu marqué 205/55 R 16 91V, à quoi correspond le chiffre 16 ?",
                    "answerOptions": [
                        {"text": "Le diamètre de la jante en pouces", "isCorrect": True},
                        {"text": "La largeur du pneu en centimètres", "isCorrect": False},
                        {"text": "La hauteur du flanc en millimètres", "isCorrect": False},
                        {"text": "L'indice de charge maximale", "isCorrect": False}
                    ],
                    "correction": "Le diamètre intérieur du pneu (donc de la jante) s'exprime toujours en pouces (1 pouce = 25,4 mm)."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le rôle de l'amortisseur ?",
                    "answerOptions": [
                        {"text": "Freiner les oscillations du ressort", "isCorrect": True},
                        {"text": "Supporter le poids du véhicule", "isCorrect": False},
                        {"text": "Régler la hauteur de caisse", "isCorrect": False},
                        {"text": "Remplacer la barre stabilisatrice", "isCorrect": False}
                    ],
                    "correction": "Le ressort supporte la charge, mais c'est l'amortisseur qui dissipe l'énergie pour maintenir le pneu au sol (sécurité et confort)."
                },
                {
                    "questionNumber": 26,
                    "question": "Dans un système de freinage ABS, que se passe-t-il si une roue est sur le point de se bloquer ?",
                    "answerOptions": [
                        {"text": "Le calculateur relâche la pression hydraulique sur cette roue", "isCorrect": True},
                        {"text": "Le moteur s'arrête immédiatement", "isCorrect": False},
                        {"text": "Le frein à main s'enclenche automatiquement", "isCorrect": False},
                        {"text": "La roue opposée accélère", "isCorrect": False}
                    ],
                    "correction": "L'ABS module la pression plusieurs fois par seconde pour garder la roue en limite d'adhérence et conserver le pouvoir directionnel."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la particularité d'un train avant avec un angle de carrossage négatif ?",
                    "answerOptions": [
                        {"text": "Le haut des roues est incliné vers l'intérieur du véhicule", "isCorrect": True},
                        {"text": "Le haut des roues est incliné vers l'extérieur", "isCorrect": False},
                        {"text": "Les roues convergent vers l'avant (pincement)", "isCorrect": False},
                        {"text": "Les roues sont parfaitement verticales", "isCorrect": False}
                    ],
                    "correction": "Le carrossage négatif améliore la tenue de route en virage en augmentant la surface de contact du pneu extérieur."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment appelle-t-on le jeu de pignons qui multiplie le couple en sortie de boîte sur un véhicule à propulsion ?",
                    "answerOptions": [
                        {"text": "Le couple conique", "isCorrect": True},
                        {"text": "Le pignon à queue", "isCorrect": False},
                        {"text": "Le baladeur", "isCorrect": False},
                        {"text": "La couronne planétaire", "isCorrect": False}
                    ],
                    "correction": "Le couple conique assure la réduction finale et le renvoi d'angle vers les arbres de roues arrière."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel fluide est utilisé dans un circuit de freinage automobile standard ?",
                    "answerOptions": [
                        {"text": "Liquide synthétique (DOT 4 ou DOT 5.1)", "isCorrect": True},
                        {"text": "Huile minérale type LHM", "isCorrect": False},
                        {"text": "Eau distillée avec antigel", "isCorrect": False},
                        {"text": "Huile de direction assistée", "isCorrect": False}
                    ],
                    "correction": "Le liquide de frein doit être incompressible et avoir un point d'ébullition très élevé (hygroscopique)."
                },
                {
                    "questionNumber": 30,
                    "question": "À quoi sert la barre stabilisatrice (anti-devers) ?",
                    "answerOptions": [
                        {"text": "Limiter l'inclinaison de la caisse en virage", "isCorrect": True},
                        {"text": "Empêcher le véhicule de reculer en côte", "isCorrect": False},
                        {"text": "Aligner les roues lors du parallélisme", "isCorrect": False},
                        {"text": "Soutenir la boîte de vitesses", "isCorrect": False}
                    ],
                    "correction": "Elle relie les deux roues d'un même essieu par une barre de torsion pour réduire le roulis."
                },
                {
                    "questionNumber": 31,
                    "question": "Que signifie un 'parallélisme' ouvert (divergence) ?",
                    "answerOptions": [
                        {"text": "L'avant des roues est plus écarté que l'arrière", "isCorrect": True},
                        {"text": "L'avant des roues est plus serré que l'arrière", "isCorrect": False},
                        {"text": "Les roues sont inclinées vers la gauche", "isCorrect": False},
                        {"text": "Les roues touchent la carrosserie", "isCorrect": False}
                    ],
                    "correction": "Une mauvaise géométrie entraîne une usure asymétrique des pneus et une mauvaise tenue de cap."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le rôle du maître-cylindre ?",
                    "answerOptions": [
                        {"text": "Transformer l'effort mécanique de la pédale en pression hydraulique", "isCorrect": True},
                        {"text": "Réguler la vitesse du moteur au ralenti", "isCorrect": False},
                        {"text": "Actionner l'embrayage automatiquement", "isCorrect": False},
                        {"text": "Distribuer l'huile vers le turbo", "isCorrect": False}
                    ],
                    "correction": "Il pousse le liquide de frein vers les étriers ou cylindres de roues grâce à un système de pistons."
                },
                {
                    "questionNumber": 33,
                    "question": "Qu'est-ce qu'une boîte de vitesses à double embrayage (DCT/DSG) ?",
                    "answerOptions": [
                        {"text": "Une boîte capable de pré-sélectionner le rapport suivant", "isCorrect": True},
                        {"text": "Une boîte avec deux leviers de vitesses", "isCorrect": False},
                        {"text": "Une boîte qui nécessite deux conducteurs", "isCorrect": False},
                        {"text": "Une boîte sans aucun pignon interne", "isCorrect": False}
                    ],
                    "correction": "Elle offre des passages de rapports ultra-rapides sans rupture de couple grâce à deux demi-boîtes travaillant en alternance."
                },
                {
                    "questionNumber": 34,
                    "question": "Sur une direction assistée électrique, qui fournit l'effort d'assistance ?",
                    "answerOptions": [
                        {"text": "Un moteur électrique monté sur la colonne ou la crémaillère", "isCorrect": True},
                        {"text": "Une pompe hydraulique entraînée par courroie", "isCorrect": False},
                        {"text": "Le conducteur seul avec un volant plus grand", "isCorrect": False},
                        {"text": "L'alternateur-démarreur haute tension", "isCorrect": False}
                    ],
                    "correction": "L'assistance électrique réduit la consommation de carburant car elle ne consomme de l'énergie que lors des manœuvres."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle pièce assure la liaison homocinétique entre la boîte et les roues ?",
                    "answerOptions": [
                        {"text": "Le joint de cardan", "isCorrect": True},
                        {"text": "Le silentbloc de triangle", "isCorrect": False},
                        {"text": "La rotule de pivot", "isCorrect": False},
                        {"text": "La fusée", "isCorrect": False}
                    ],
                    "correction": "Le cardan permet de transmettre le mouvement de rotation tout en autorisant les débattements de suspension et de direction."
                },
                {
                    "questionNumber": 36,
                    "question": "À quoi sert le répartiteur de freinage (asservi à la charge) ?",
                    "answerOptions": [
                        {"text": "Éviter le blocage des roues arrière quand le véhicule est vide", "isCorrect": True},
                        {"text": "Augmenter la puissance de freinage à l'avant", "isCorrect": False},
                        {"text": "Changer automatiquement le liquide de frein", "isCorrect": False},
                        {"text": "Réguler la température des disques", "isCorrect": False}
                    ],
                    "correction": "Il limite la pression vers l'arrière pour éviter que le train arrière ne 'chasse' lors d'un freinage violent à vide."
                },
                {
                    "questionNumber": 37,
                    "question": "Qu'est-ce que le 'voile' d'un disque de frein ?",
                    "answerOptions": [
                        {"text": "Une déformation latérale du disque", "isCorrect": True},
                        {"text": "Une usure de l'épaisseur du disque", "isCorrect": False},
                        {"text": "Une couleur bleue due à la chauffe", "isCorrect": False},
                        {"text": "Un dépôt de poussière de plaquettes", "isCorrect": False}
                    ],
                    "correction": "Le voile provoque des vibrations importantes dans la pédale de frein et le volant."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est l'avantage des disques de freins ventilés ?",
                    "answerOptions": [
                        {"text": "Une meilleure dissipation de la chaleur", "isCorrect": True},
                        {"text": "Un poids plus élevé pour plus d'inertie", "isCorrect": False},
                        {"text": "Un prix de fabrication réduit", "isCorrect": False},
                        {"text": "Une absence totale de poussière", "isCorrect": False}
                    ],
                    "correction": "Les canaux internes permettent à l'air de circuler, évitant ainsi le 'fading' (perte d'efficacité par surchauffe)."
                },
                {
                    "questionNumber": 39,
                    "question": "Que contrôle-t-on lors d'une inspection des rotules de direction ?",
                    "answerOptions": [
                        {"text": "L'absence de jeu mécanique et l'état du soufflet", "isCorrect": True},
                        {"text": "La pression de graisse interne", "isCorrect": False},
                        {"text": "La couleur du métal", "isCorrect": False},
                        {"text": "La marque du fabricant", "isCorrect": False}
                    ],
                    "correction": "Un jeu excessif dans une rotule compromet la précision de la direction et la sécurité."
                },
                {
                    "questionNumber": 40,
                    "question": "Sur une boîte automatique classique, que signifie la position 'P' ?",
                    "answerOptions": [
                        {"text": "Parking (blocage mécanique de la transmission)", "isCorrect": True},
                        {"text": "Power (mode conduite sportive)", "isCorrect": False},
                        {"text": "Pression (montée en pression d'huile)", "isCorrect": False},
                        {"text": "Point mort (neutre)", "isCorrect": False}
                    ],
                    "correction": "En position P, un doigt de verrouillage bloque la boîte, empêchant le véhicule de bouger."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : ÉLECTRICITÉ, ÉLECTRONIQUE ET RÉSEAUX (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ÉLECTRICITÉ, ÉLECTRONIQUE ET RÉSEAUX",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle unité mesure l'intensité d'un courant électrique ?",
                    "answerOptions": [
                        {"text": "L'Ampère", "isCorrect": True},
                        {"text": "Le Volt", "isCorrect": False},
                        {"text": "L'Ohm", "isCorrect": False},
                        {"text": "Le Watt", "isCorrect": False}
                    ],
                    "correction": "L'intensité (I) se mesure avec un ampèremètre branché en série dans le circuit."
                },
                {
                    "questionNumber": 42,
                    "question": "D'après la loi d'Ohm, quelle est la formule correcte ?",
                    "answerOptions": [
                        {"text": "U = R x I", "isCorrect": True},
                        {"text": "P = U x I", "isCorrect": False},
                        {"text": "R = U x I", "isCorrect": False},
                        {"text": "I = R / U", "isCorrect": False}
                    ],
                    "correction": "U (Tension en Volts) est égale au produit de la Résistance (Ohms) par l'Intensité (Ampères)."
                },
                {
                    "questionNumber": 43,
                    "question": "À quoi sert le multiplexage (Bus CAN) ?",
                    "answerOptions": [
                        {"text": "Faire circuler plusieurs informations sur un seul canal de communication", "isCorrect": True},
                        {"text": "Augmenter la tension de la batterie", "isCorrect": False},
                        {"text": "Supprimer totalement les fusibles", "isCorrect": False},
                        {"text": "Accélérer la vitesse maximale du véhicule", "isCorrect": False}
                    ],
                    "correction": "Il permet de réduire considérablement la quantité de câbles en utilisant un langage binaire entre les calculateurs."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la fonction d'un alternateur ?",
                    "answerOptions": [
                        {"text": "Recharger la batterie et alimenter le réseau moteur tournant", "isCorrect": True},
                        {"text": "Démarrer le moteur thermique", "isCorrect": False},
                        {"text": "Transformer le courant continu en alternatif", "isCorrect": False},
                        {"text": "Mesurer la vitesse du véhicule", "isCorrect": False}
                    ],
                    "correction": "Il transforme l'énergie mécanique du moteur en énergie électrique."
                },
                {
                    "questionNumber": 45,
                    "question": "Que signifie un voyant moteur allumé en orange ?",
                    "answerOptions": [
                        {"text": "Un défaut d'injection ou de pollution détecté", "isCorrect": True},
                        {"text": "Une vidange immédiate à effectuer", "isCorrect": False},
                        {"text": "Le fonctionnement normal du turbo", "isCorrect": False},
                        {"text": "Que le réservoir est plein", "isCorrect": False}
                    ],
                    "correction": "Cela indique qu'un code défaut (DTC) a été enregistré dans le calculateur moteur."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel outil permet de visualiser un signal électrique en fonction du temps ?",
                    "answerOptions": [
                        {"text": "L'oscilloscope", "isCorrect": True},
                        {"text": "Le multimètre", "isCorrect": False},
                        {"text": "La lampe témoin", "isCorrect": False},
                        {"text": "Le pèse-acide", "isCorrect": False}
                    ],
                    "correction": "L'oscilloscope est indispensable pour analyser les réseaux multiplexés ou les signaux de capteurs rapides."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est la tension aux bornes d'une batterie 12V parfaitement chargée, moteur éteint ?",
                    "answerOptions": [
                        {"text": "Environ 12,6 Volts", "isCorrect": True},
                        {"text": "Exactement 12,0 Volts", "isCorrect": False},
                        {"text": "Environ 14,5 Volts", "isCorrect": False},
                        {"text": "Moins de 11,0 Volts", "isCorrect": False}
                    ],
                    "correction": "À 12,6V, les six éléments de 2,1V sont au repos. À 12,0V, la batterie est à moitié déchargée."
                },
                {
                    "questionNumber": 48,
                    "question": "Dans un circuit électrique, quel composant protège contre les surintensités ?",
                    "answerOptions": [
                        {"text": "Le fusible", "isCorrect": True},
                        {"text": "Le relais", "isCorrect": False},
                        {"text": "La diode", "isCorrect": False},
                        {"text": "Le condensateur", "isCorrect": False}
                    ],
                    "correction": "Le fusible fond si l'intensité dépasse son calibre, ouvrant ainsi le circuit pour protéger les fils."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le rôle d'un relais ?",
                    "answerOptions": [
                        {"text": "Commander un circuit de puissance avec un courant faible", "isCorrect": True},
                        {"text": "Changer le sens du courant", "isCorrect": False},
                        {"text": "Stocker de l'électricité", "isCorrect": False},
                        {"text": "Éclairer l'habitacle", "isCorrect": False}
                    ],
                    "correction": "Il agit comme un interrupteur électromagnétique piloté par un calculateur ou un bouton."
                },
                {
                    "questionNumber": 50,
                    "question": "Qu'est-ce qu'un signal RCO (PWM) ?",
                    "answerOptions": [
                        {"text": "Un signal dont on fait varier le rapport temps haut / temps bas", "isCorrect": True},
                        {"text": "Un signal radio pour l'autoradio", "isCorrect": False},
                        {"text": "Une tension alternative de 230V", "isCorrect": False},
                        {"text": "Un code secret pour démarrer", "isCorrect": False}
                    ],
                    "correction": "Le Rapport Cyclique d'Ouverture permet au calculateur de piloter précisément un actionneur (ex: vanne EGR)."
                },
                {
                    "questionNumber": 51,
                    "question": "Que mesure-t-on avec un ohmmètre aux bornes d'un capteur de température débranché ?",
                    "answerOptions": [
                        {"text": "Sa résistance interne", "isCorrect": True},
                        {"text": "Sa tension de sortie", "isCorrect": False},
                        {"text": "L'intensité qu'il consomme", "isCorrect": False},
                        {"text": "Son débit d'air", "isCorrect": False}
                    ],
                    "correction": "Les sondes de température sont souvent des thermistances (CTN) dont la résistance varie avec la chaleur."
                },
                {
                    "questionNumber": 52,
                    "question": "Sur un Bus CAN, que signifie la résistance de terminaison de 120 Ohms ?",
                    "answerOptions": [
                        {"text": "Éviter les échos de signaux en bout de ligne", "isCorrect": True},
                        {"text": "Faire chauffer le réseau en hiver", "isCorrect": False},
                        {"text": "Remplacer la batterie en cas de panne", "isCorrect": False},
                        {"text": "Limiter la vitesse de communication", "isCorrect": False}
                    ],
                    "correction": "On trouve généralement deux résistances en parallèle, soit 60 Ohms mesurables sur le réseau complet."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel composant électronique laisse passer le courant dans un seul sens ?",
                    "answerOptions": [
                        {"text": "La diode", "isCorrect": True},
                        {"text": "La résistance", "isCorrect": False},
                        {"text": "Le transistor", "isCorrect": False},
                        {"text": "La bobine", "isCorrect": False}
                    ],
                    "correction": "Elle agit comme un clapet anti-retour pour l'électricité."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la particularité d'un capteur inductif ?",
                    "answerOptions": [
                        {"text": "Il génère son propre signal électrique par magnétisme", "isCorrect": True},
                        {"text": "Il nécessite une alimentation de 12V pour fonctionner", "isCorrect": False},
                        {"text": "Il ne fonctionne que dans le vide", "isCorrect": False},
                        {"text": "Il mesure la luminosité des phares", "isCorrect": False}
                    ],
                    "correction": "Souvent utilisé comme capteur PMH, il produit une tension alternative lors du passage des dents de la cible."
                },
                {
                    "questionNumber": 55,
                    "question": "Que signifie l'acronyme OBD ?",
                    "answerOptions": [
                        {"text": "On-Board Diagnostics", "isCorrect": True},
                        {"text": "Only Battery Drive", "isCorrect": False},
                        {"text": "Over Boost Dynamic", "isCorrect": False},
                        {"text": "Open Brake Device", "isCorrect": False}
                    ],
                    "correction": "C'est le standard de diagnostic qui permet d'accéder aux calculateurs via une prise 16 broches."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment vérifie-t-on la consommation de courant d'un véhicule au repos ?",
                    "answerOptions": [
                        {"text": "Avec une pince ampèremétrique ou en série avec un multimètre", "isCorrect": True},
                        {"text": "En mesurant la tension de la batterie toutes les heures", "isCorrect": False},
                        {"text": "En touchant les fils pour voir s'ils sont chauds", "isCorrect": False},
                        {"text": "En débranchant l'alternateur moteur tournant", "isCorrect": False}
                    ],
                    "correction": "On cherche une 'fuite' de courant (consommation parasite) qui déchargerait la batterie."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est le rôle du transistor dans un calculateur ?",
                    "answerOptions": [
                        {"text": "Servir d'interrupteur électronique ultra-rapide", "isCorrect": True},
                        {"text": "Stocker les codes défauts", "isCorrect": False},
                        {"text": "Refroidir la carte électronique", "isCorrect": False},
                        {"text": "Transformer le 12V en 230V", "isCorrect": False}
                    ],
                    "correction": "Les transistors de puissance pilotent les injecteurs ou les bobines d'allumage."
                },
                {
                    "questionNumber": 58,
                    "question": "Dans un système hybride, quel élément gère les flux d'énergie entre batterie, moteur et générateur ?",
                    "answerOptions": [
                        {"text": "L'onduleur (Inverter / Convertisseur)", "isCorrect": True},
                        {"text": "La boîte de vitesses manuelle", "isCorrect": False},
                        {"text": "Le bouchon de réservoir", "isCorrect": False},
                        {"text": "Le capteur d'angle volant", "isCorrect": False}
                    ],
                    "correction": "L'onduleur transforme le courant continu de la batterie HT en courant alternatif pour les moteurs."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle est la tension de référence (Vref) fournie par un calculateur à ses capteurs ?",
                    "answerOptions": [
                        {"text": "Généralement 5 Volts", "isCorrect": True},
                        {"text": "Exactement 12,6 Volts", "isCorrect": False},
                        {"text": "Environ 0,5 Volt", "isCorrect": False},
                        {"text": "24 Volts", "isCorrect": False}
                    ],
                    "correction": "Le calculateur stabilise une tension de 5V pour ne pas dépendre des variations de la batterie."
                },
                {
                    "questionNumber": 60,
                    "question": "À quoi sert un 'shunt' ?",
                    "answerOptions": [
                        {"text": "Remplacer un composant pour tester la continuité ou mesurer le courant", "isCorrect": True},
                        {"text": "Augmenter la luminosité du tableau de bord", "isCorrect": False},
                        {"text": "Réduire le bruit de l'alternateur", "isCorrect": False},
                        {"text": "Calculer la distance de freinage", "isCorrect": False}
                    ],
                    "correction": "En diagnostic, un shunt peut servir à isoler une partie du circuit ou à dériver le courant vers un appareil de mesure."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : DIAGNOSTIC, ENTRETIEN ET MÉTHODOLOGIE (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : DIAGNOSTIC, ENTRETIEN ET MÉTHODOLOGIE",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la première étape de la démarche de diagnostic ?",
                    "answerOptions": [
                        {"text": "Vérifier et confirmer le symptôme client", "isCorrect": True},
                        {"text": "Changer directement la pièce suspecte", "isCorrect": False},
                        {"text": "Appeler l'assistance technique constructeur", "isCorrect": False},
                        {"text": "Effacer les codes défauts sans les lire", "isCorrect": False}
                    ],
                    "correction": "Il faut d'abord valider que le dysfonctionnement existe réellement et comprendre dans quelles conditions il apparaît."
                },
                {
                    "questionNumber": 62,
                    "question": "Lors d'une vidange moteur, pourquoi remplace-t-on systématiquement le joint de bouchon ?",
                    "answerOptions": [
                        {"text": "Garantir l'étanchéité parfaite et éviter les fuites", "isCorrect": True},
                        {"text": "Changer la couleur du bouchon", "isCorrect": False},
                        {"text": "Parce que c'est une pièce qui s'use par frottement", "isCorrect": False},
                        {"text": "C'est une obligation uniquement pour les moteurs Diesel", "isCorrect": False}
                    ],
                    "correction": "Le joint s'écrase au serrage pour épouser les formes du carter et du bouchon."
                },
                {
                    "questionNumber": 63,
                    "question": "Que signifie l'indice de viscosité 5W30 sur un bidon d'huile ?",
                    "answerOptions": [
                        {"text": "Sa fluidité à froid (5) et sa résistance à chaud (30)", "isCorrect": True},
                        {"text": "Son prix par litre (5 euros) et sa durée de vie (30 mois)", "isCorrect": False},
                        {"text": "Le nombre d'additifs (5) et le nombre de détergents (30)", "isCorrect": False},
                        {"text": "La contenance du bidon (5 litres)", "isCorrect": False}
                    ],
                    "correction": "Plus le premier chiffre est bas, plus l'huile est fluide à froid (facilite le démarrage)."
                },
                {
                    "questionNumber": 64,
                    "question": "À l'aide de quel outil contrôle-t-on l'étanchéité d'un circuit de refroidissement ?",
                    "answerOptions": [
                        {"text": "Une pompe à épreuve avec manomètre", "isCorrect": True},
                        {"text": "Un pèse-antigel", "isCorrect": False},
                        {"text": "Un thermomètre infrarouge", "isCorrect": False},
                        {"text": "Un aspirateur à liquide", "isCorrect": False}
                    ],
                    "correction": "On met le circuit sous pression (souvent 1 à 1,5 bar) et on vérifie si la pression chute ou si une fuite apparaît."
                },
                {
                    "questionNumber": 65,
                    "question": "Qu'indique une fumée bleue à l'échappement ?",
                    "answerOptions": [
                        {"text": "Une consommation d'huile moteur", "isCorrect": True},
                        {"text": "Un mélange trop riche en essence", "isCorrect": False},
                        {"text": "Une fuite de liquide de refroidissement", "isCorrect": False},
                        {"text": "Un manque d'air à l'admission", "isCorrect": False}
                    ],
                    "correction": "L'huile passe dans la chambre de combustion (segments ou joints de queue de soupapes usés)."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on le contrôle périodique obligatoire des véhicules de plus de 4 ans ?",
                    "answerOptions": [
                        {"text": "Le contrôle technique (CT)", "isCorrect": True},
                        {"text": "L'expertise d'assurance", "isCorrect": False},
                        {"text": "Le passage au marbre", "isCorrect": False},
                        {"text": "Le contrôle anti-pollution annuel", "isCorrect": False}
                    ],
                    "correction": "Le CT vérifie les organes de sécurité et de pollution du véhicule."
                },
                {
                    "questionNumber": 67,
                    "question": "Dans un dossier technique, que signifie 'DTC' ?",
                    "answerOptions": [
                        {"text": "Diagnostic Trouble Code", "isCorrect": True},
                        {"text": "Direct Tuning Center", "isCorrect": False},
                        {"text": "Dynamic Traction Control", "isCorrect": False},
                        {"text": "Double Transmission Clutch", "isCorrect": False}
                    ],
                    "correction": "C'est le code de panne générique stocké dans la mémoire du calculateur."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le but d'une analyse d'huile ?",
                    "answerOptions": [
                        {"text": "Déterminer l'état d'usure interne du moteur sans démontage", "isCorrect": True},
                        {"text": "Vérifier le niveau d'huile au tableau de bord", "isCorrect": False},
                        {"text": "Changer la marque de l'huile utilisée", "isCorrect": False},
                        {"text": "Mesurer la pression de la pompe à huile", "isCorrect": False}
                    ],
                    "correction": "On y cherche des traces de métaux (cuivre, fer) qui indiquent quel organe s'use."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle opération est impérative lors du remplacement d'un kit de distribution ?",
                    "answerOptions": [
                        {"text": "Le remplacement de la pompe à eau (si entraînée) et des galets", "isCorrect": True},
                        {"text": "Le changement des quatre pneus", "isCorrect": False},
                        {"text": "La recharge de la climatisation", "isCorrect": False},
                        {"text": "Le réglage de l'avance à l'allumage au stroboscope", "isCorrect": False}
                    ],
                    "correction": "Par sécurité, on change tout le kit car une défaillance d'un galet ou de la pompe détruirait la courroie neuve."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment vérifie-t-on l'usure d'un disque de frein ?",
                    "answerOptions": [
                        {"text": "En mesurant son épaisseur au palmer et en vérifiant le voile", "isCorrect": True},
                        {"text": "En regardant uniquement si la couleur est grise", "isCorrect": False},
                        {"text": "En frappant dessus avec un marteau", "isCorrect": False},
                        {"text": "En mesurant le diamètre extérieur au mètre ruban", "isCorrect": False}
                    ],
                    "correction": "Chaque disque a une cote minimale (Mini Th) gravée sur son moyeu à ne pas dépasser."
                },
                {
                    "questionNumber": 71,
                    "question": "À quoi sert un compressiomètre ?",
                    "answerOptions": [
                        {"text": "Mesurer l'étanchéité de la chambre de combustion", "isCorrect": True},
                        {"text": "Gonfler les pneus à la bonne pression", "isCorrect": False},
                        {"text": "Vérifier le fonctionnement du turbo", "isCorrect": False},
                        {"text": "Mesurer la pression d'huile au ralenti", "isCorrect": False}
                    ],
                    "correction": "Il permet de détecter une fuite aux soupapes, au joint de culasse ou aux segments."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie la maintenance 'préventive' ?",
                    "answerOptions": [
                        {"text": "Remplacer des pièces avant qu'elles ne tombent en panne", "isCorrect": True},
                        {"text": "Réparer le véhicule une fois immobilisé sur la route", "isCorrect": False},
                        {"text": "Changer uniquement ce que le client demande", "isCorrect": False},
                        {"text": "Attendre que le voyant rouge s'allume", "isCorrect": False}
                    ],
                    "correction": "Exemples : Vidange, remplacement de courroie de distribution selon les préconisations."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est l'unité de mesure du couple moteur ?",
                    "answerOptions": [
                        {"text": "Le Newton-mètre (Nm)", "isCorrect": True},
                        {"text": "Le Cheval-vapeur (ch)", "isCorrect": False},
                        {"text": "Le Kilomètre par heure (km/h)", "isCorrect": False},
                        {"text": "Le Bar", "isCorrect": False}
                    ],
                    "correction": "Le couple représente la force de rotation exercée par le moteur."
                },
                {
                    "questionNumber": 74,
                    "question": "Pourquoi doit-on effectuer une purge après le remplacement d'un récepteur d'embrayage hydraulique ?",
                    "answerOptions": [
                        {"text": "Éliminer l'air emprisonné dans le circuit", "isCorrect": True},
                        {"text": "Nettoyer l'extérieur de la boîte de vitesses", "isCorrect": False},
                        {"text": "Régler la hauteur de la pédale d'accélérateur", "isCorrect": False},
                        {"text": "Diminuer la pression d'huile moteur", "isCorrect": False}
                    ],
                    "correction": "L'air est compressible, contrairement au liquide. Sa présence rendrait la commande inopérante."
                },
                {
                    "questionNumber": 75,
                    "question": "Lors d'un contrôle de batterie, que mesure le pèse-acide ?",
                    "answerOptions": [
                        {"text": "La densité de l'électrolyte", "isCorrect": True},
                        {"text": "La tension en Volts", "isCorrect": False},
                        {"text": "L'intensité de démarrage à froid", "isCorrect": False},
                        {"text": "Le niveau d'eau distillée uniquement", "isCorrect": False}
                    ],
                    "correction": "La densité de l'acide sulfurique augmente avec l'état de charge de la batterie."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle information donne un 'schéma électrique' par rapport à un 'plan d'implantation' ?",
                    "answerOptions": [
                        {"text": "Le cheminement logique du courant et les connexions", "isCorrect": True},
                        {"text": "La position exacte des fils dans la carrosserie", "isCorrect": False},
                        {"text": "Le prix des composants électriques", "isCorrect": False},
                        {"text": "Le poids du faisceau électrique", "isCorrect": False}
                    ],
                    "correction": "Le schéma de principe est indispensable pour comprendre le fonctionnement et diagnostiquer."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le risque de trop serrer une vis de roue ?",
                    "answerOptions": [
                        {"text": "L'étirement ou la rupture du goujon", "isCorrect": True},
                        {"text": "La crevaison immédiate du pneu", "isCorrect": False},
                        {"text": "L'augmentation de la consommation", "isCorrect": False},
                        {"text": "Le blocage du système ABS", "isCorrect": False}
                    ],
                    "correction": "Il faut respecter le couple de serrage préconisé avec une clé dynamométrique."
                },
                {
                    "questionNumber": 78,
                    "question": "Que signifie la 'mise en sécurité' (mode dégradé) d'un moteur ?",
                    "answerOptions": [
                        {"text": "Une réduction de puissance pour protéger les organes", "isCorrect": True},
                        {"text": "Le verrouillage automatique des portes", "isCorrect": False},
                        {"text": "L'arrêt total et définitif du moteur", "isCorrect": False},
                        {"text": "L'allumage de tous les feux de détresse", "isCorrect": False}
                    ],
                    "correction": "Le calculateur limite le régime ou la pression turbo pour éviter une casse majeure suite à une défaillance."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment appelle-t-on le liquide utilisé pour traiter les NOx sur les moteurs Diesel modernes ?",
                    "answerOptions": [
                        {"text": "L'AdBlue (solution d'urée)", "isCorrect": True},
                        {"text": "L'Eolys (cérine)", "isCorrect": False},
                        {"text": "L'antigel de pare-brise", "isCorrect": False},
                        {"text": "Le liquide de DA", "isCorrect": False}
                    ],
                    "correction": "L'AdBlue est injecté dans le catalyseur SCR pour transformer les NOx en azote et vapeur d'eau."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est l'unité de mesure de la pression de gonflage usuelle en France ?",
                    "answerOptions": [
                        {"text": "Le Bar", "isCorrect": True},
                        {"text": "Le PSI", "isCorrect": False},
                        {"text": "Le Pascal", "isCorrect": False},
                        {"text": "Le Newton", "isCorrect": False}
                    ],
                    "correction": "1 bar correspond environ à la pression atmosphérique au niveau de la mer."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SANTÉ, SÉCURITÉ ET ENVIRONNEMENT (PSE) (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : SANTÉ, SÉCURITÉ ET ENVIRONNEMENT (PSE)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel type d'extincteur est le plus adapté pour un feu d'origine électrique dans un atelier ?",
                    "answerOptions": [
                        {"text": "Dioxyde de carbone (CO2)", "isCorrect": True},
                        {"text": "Eau avec additif", "isCorrect": False},
                        {"text": "Eau pulvérisée", "isCorrect": False},
                        {"text": "Mousse", "isCorrect": False}
                    ],
                    "correction": "Le CO2 étouffe le feu sans être conducteur d'électricité et ne laisse pas de résidus sur les composants."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la règle de sécurité n°1 avant d'intervenir sur un véhicule hybride ou électrique ?",
                    "answerOptions": [
                        {"text": "Effectuer la consignation (mise hors tension)", "isCorrect": True},
                        {"text": "Vider le réservoir d'essence", "isCorrect": False},
                        {"text": "Mettre des gants en cuir épais", "isCorrect": False},
                        {"text": "Ouvrir toutes les fenêtres", "isCorrect": False}
                    ],
                    "correction": "Il faut impérativement retirer le pont de service (plug) et vérifier l'absence de tension (VAT) avec des gants isolants."
                },
                {
                    "questionNumber": 83,
                    "question": "Que signifie le marquage CE sur un outil ou une machine ?",
                    "answerOptions": [
                        {"text": "Conformité Européenne (respect des normes de sécurité)", "isCorrect": True},
                        {"text": "Câblage Électrique", "isCorrect": False},
                        {"text": "Charge Élevée", "isCorrect": False},
                        {"text": "Contrôle Externe", "isCorrect": False}
                    ],
                    "correction": "C'est une obligation pour la mise sur le marché d'un produit garantissant la sécurité de l'utilisateur."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel équipement de protection individuelle (EPI) est indispensable pour utiliser une meuleuse d'angle ?",
                    "answerOptions": [
                        {"text": "Lunettes de protection ou visière", "isCorrect": True},
                        {"text": "Bottes en caoutchouc", "isCorrect": False},
                        {"text": "Tablier en plastique", "isCorrect": False},
                        {"text": "Casque de chantier", "isCorrect": False}
                    ],
                    "correction": "Les projections d'étincelles et d'éclats métalliques peuvent causer des lésions oculaires graves."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment doit-on soulever une charge lourde (ex: boîte de vitesses) au sol ?",
                    "answerOptions": [
                        {"text": "Plier les genoux et garder le dos droit", "isCorrect": True},
                        {"text": "Garder les jambes raides et courber le dos", "isCorrect": False},
                        {"text": "Soulever d'un coup sec en tournant le buste", "isCorrect": False},
                        {"text": "Porter la charge le plus loin possible du corps", "isCorrect": False}
                    ],
                    "correction": "Cela permet d'utiliser la force des cuisses et de préserver la colonne vertébrale (prévention des hernies)."
                },
                {
                    "questionNumber": 86,
                    "question": "Où doit-on jeter les huiles de vidange usagées ?",
                    "answerOptions": [
                        {"text": "Dans une cuve de récupération pour recyclage spécifique", "isCorrect": True},
                        {"text": "Dans l'évier avec du produit vaisselle", "isCorrect": False},
                        {"text": "Dans le caniveau à l'extérieur", "isCorrect": False},
                        {"text": "Dans la benne à ordures ménagères", "isCorrect": False}
                    ],
                    "correction": "Les huiles usagées sont des déchets dangereux (DID) qui polluent massivement l'eau."
                },
                {
                    "questionNumber": 87,
                    "question": "Que signifie le sigle 'EPI' ?",
                    "answerOptions": [
                        {"text": "Équipement de Protection Individuelle", "isCorrect": True},
                        {"text": "Étude des Pannes Inconnues", "isCorrect": False},
                        {"text": "Entretien Périodique Indispensable", "isCorrect": False},
                        {"text": "Électronique Pour l'Industrie", "isCorrect": False}
                    ],
                    "correction": "Il s'agit des gants, lunettes, masques, chaussures de sécurité et vêtements de travail."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le danger principal de laisser tourner un moteur dans un atelier fermé ?",
                    "answerOptions": [
                        {"text": "L'intoxication au monoxyde de carbone (CO)", "isCorrect": True},
                        {"text": "L'augmentation du taux d'humidité", "isCorrect": False},
                        {"text": "Le risque de court-circuit", "isCorrect": False},
                        {"text": "La baisse de la pression atmosphérique", "isCorrect": False}
                    ],
                    "correction": "Le CO est un gaz incolore, inodore et mortel. Il faut impérativement utiliser un extracteur de gaz d'échappement."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel risque prévient-on en débranchant la batterie avant une intervention sur l'alternateur ?",
                    "answerOptions": [
                        {"text": "Le court-circuit accidentel avec les outils", "isCorrect": True},
                        {"text": "Le vol du véhicule", "isCorrect": False},
                        {"text": "La décharge de la batterie", "isCorrect": False},
                        {"text": "La fuite de carburant", "isCorrect": False}
                    ],
                    "correction": "Un contact entre la borne B+ de l'alternateur et la carcasse avec une clé provoquerait un arc électrique violent."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est la couleur normalisée des câbles haute tension sur les véhicules électriques ?",
                    "answerOptions": [
                        {"text": "Orange", "isCorrect": True},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False}
                    ],
                    "correction": "La couleur orange signale un danger de mort (tension pouvant atteindre 600V ou plus)."
                },
                {
                    "questionNumber": 91,
                    "question": "Que signifie le pictogramme 'tête de mort' sur un bidon de produit ?",
                    "answerOptions": [
                        {"text": "Produit toxique ou mortel", "isCorrect": True},
                        {"text": "Produit corrosif pour les métaux", "isCorrect": False},
                        {"text": "Produit inflammable", "isCorrect": False},
                        {"text": "Produit radioactif", "isCorrect": False}
                    ],
                    "correction": "L'inhalation, l'ingestion ou le contact cutané avec ce produit présente un risque grave pour la santé."
                },
                {
                    "questionNumber": 92,
                    "question": "À quoi sert la 'Fiche de Données de Sécurité' (FDS) d'un produit chimique ?",
                    "answerOptions": [
                        {"text": "Informer sur les risques, le stockage et les premiers secours", "isCorrect": True},
                        {"text": "Donner le prix de vente conseillé", "isCorrect": False},
                        {"text": "Expliquer comment réparer un moteur avec ce produit", "isCorrect": False},
                        {"text": "Lister les clients qui l'ont acheté", "isCorrect": False}
                    ],
                    "correction": "Chaque produit professionnel doit avoir sa FDS consultable dans l'atelier."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le rôle du médecin du travail ?",
                    "answerOptions": [
                        {"text": "Prévenir l'altération de la santé des salariés due à leur travail", "isCorrect": True},
                        {"text": "Soigner les grippes et rhumes des employés", "isCorrect": False},
                        {"text": "Sanctionner les ouvriers qui arrivent en retard", "isCorrect": False},
                        {"text": "Remplacer l'employeur lors des réunions", "isCorrect": False}
                    ],
                    "correction": "Il vérifie l'aptitude au poste et conseille sur l'ergonomie et l'hygiène."
                },
                {
                    "questionNumber": 94,
                    "question": "En cas d'accident sur un chantier ou en atelier, quelle est la première action de la procédure 'P.A.S.' ?",
                    "answerOptions": [
                        {"text": "Protéger (éviter le sur-accident)", "isCorrect": True},
                        {"text": "Alerter les secours", "isCorrect": False},
                        {"text": "Secourir la victime", "isCorrect": False},
                        {"text": "Partir chercher de l'aide", "isCorrect": False}
                    ],
                    "correction": "On sécurise la zone avant toute chose pour ne pas devenir soi-même une victime supplémentaire."
                },
                {
                    "questionNumber": 95,
                    "question": "Pourquoi est-il interdit de nettoyer ses vêtements à la soufflette (air comprimé) ?",
                    "answerOptions": [
                        {"text": "Risque d'embolie gazeuse ou de lésions cutanées/oculaires", "isCorrect": True},
                        {"text": "Cela abîme les fibres du tissu", "isCorrect": False},
                        {"text": "L'air comprimé coûte trop cher", "isCorrect": False},
                        {"text": "Cela fait trop de bruit dans l'atelier", "isCorrect": False}
                    ],
                    "correction": "L'air peut traverser la peau et s'introduire dans le sang, ce qui est mortel, ou projeter des particules dans les yeux."
                },
                {
                    "questionNumber": 96,
                    "question": "Dans quel bac de tri doit-on jeter les filtres à huile usagés ?",
                    "answerOptions": [
                        {"text": "Déchets Industriels Dangereux (DID)", "isCorrect": True},
                        {"text": "Feraille classique", "isCorrect": False},
                        {"text": "Ordures ménagères", "isCorrect": False},
                        {"text": "Plastiques recyclables", "isCorrect": False}
                    ],
                    "correction": "Bien qu'en métal, ils contiennent des résidus d'huile polluante et doivent suivre une filière spécifique."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque de porter des bagues ou gourmettes lors de l'utilisation de machines tournantes ?",
                    "answerOptions": [
                        {"text": "L'arrachement d'un membre ou d'un doigt (hantise du bague)", "isCorrect": True},
                        {"text": "Salir le bijou avec du cambouis", "isCorrect": False},
                        {"text": "Rayonner les mains", "isCorrect": False},
                        {"text": "Faire plaisir au patron", "isCorrect": False}
                    ],
                    "correction": "Le bijou peut être happé par un foret ou une courroie, entraînant la main avec lui."
                },
                {
                    "questionNumber": 98,
                    "question": "Pourquoi doit-on obligatoirement porter des lunettes de protection lors de l'utilisation d'un touret à meuler ?",
                    "answerOptions": [
                        {"text": "Prévenir la projection d'éclats métalliques à haute vitesse", "isCorrect": True},
                        {"text": "Mieux voir la pièce à meuler", "isCorrect": False},
                        {"text": "Se protéger de la lumière du soleil", "isCorrect": False},
                        {"text": "Éviter les courants d'air", "isCorrect": False}
                    ],
                    "correction": "Le risque de lésion oculaire grave est immédiat sans lunettes de protection ou visière faciale."
                },
                {
                    "questionNumber": 99,
                    "question": "Qu'indique un voyant orange au tableau de bord ?",
                    "answerOptions": [
                        {"text": "Anomalie non critique nécessitant un contrôle", "isCorrect": True},
                        {"text": "Arrêt immédiat obligatoire du véhicule", "isCorrect": False},
                        {"text": "Fonctionnement normal des feux de route", "isCorrect": False},
                        {"text": "Système de sécurité totalement désactivé", "isCorrect": False}
                    ],
                    "correction": "Code couleur standard : Rouge = Danger immédiat/Arrêt impératif. Orange/Jaune = Avertissement ou défaut à traiter rapidement."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la dernière action à effectuer avant de rendre le véhicule au client ?",
                    "answerOptions": [
                        {"text": "Faire un essai routier et un contrôle visuel final", "isCorrect": True},
                        {"text": "Laver intégralement la carrosserie et les jantes", "isCorrect": False},
                        {"text": "Changer les réglages du siège et des rétroviseurs", "isCorrect": False},
                        {"text": "Débrancher la batterie pour réinitialiser l'heure", "isCorrect": False}
                    ],
                    "correction": "Il faut s'assurer que la réparation est conforme et que le véhicule est sûr."
                }
            ]
        }
    }
}