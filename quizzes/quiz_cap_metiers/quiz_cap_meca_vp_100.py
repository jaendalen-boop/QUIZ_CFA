quiz_data = {
    "title": "Quiz CAP Maintenance des Véhicules (Option A) : Moteur, Liaison au Sol, Électricité et Sécurité (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MOTORISATION ET MAINTENANCE PÉRIODIQUE (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : MOTORISATION ET MAINTENANCE PÉRIODIQUE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est l'ordre chronologique des 4 temps du cycle d'un moteur thermique ?",
                    "answerOptions": [
                        {"text": "Admission Compression Combustion Échappement", "isCorrect": True},
                        {"text": "Compression Admission Échappement Combustion", "isCorrect": False},
                        {"text": "Admission Échappement Compression Combustion", "isCorrect": False},
                        {"text": "Combustion Compression Admission Échappement", "isCorrect": False}
                    ],
                    "correction": "Le cycle à 4 temps se déroule toujours dans cet ordre précis : 1. Admission, 2. Compression, 3. Combustion-Détente, 4. Échappement."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle pièce mécanique commande l'ouverture et la fermeture des soupapes ?",
                    "answerOptions": [
                        {"text": "L'arbre à cames", "isCorrect": True},
                        {"text": "Le vilebrequin du moteur", "isCorrect": False},
                        {"text": "La pompe à injection", "isCorrect": False},
                        {"text": "Le collecteur d'admission", "isCorrect": False}
                    ],
                    "correction": "C'est l'arbre à cames qui, grâce à ses cames, appuie sur les soupapes pour les ouvrir au bon moment."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la fonction principale de l'huile moteur ?",
                    "answerOptions": [
                        {"text": "Lubrifier", "isCorrect": True},
                        {"text": "Augmenter la compression", "isCorrect": False},
                        {"text": "Nettoyer le pare-brise", "isCorrect": False},
                        {"text": "Refroidir l'habitacle", "isCorrect": False}
                    ],
                    "correction": "La fonction première de l'huile est de lubrifier les pièces en mouvement pour limiter les frottements et l'usure."
                },
                {
                    "questionNumber": 4,
                    "question": "Sur un bidon d'huile, que signifie l'indice '5W' dans la désignation 5W30 ?",
                    "answerOptions": [
                        {"text": "La viscosité à froid", "isCorrect": True},
                        {"text": "La viscosité à chaud", "isCorrect": False},
                        {"text": "La qualité de l'huile", "isCorrect": False},
                        {"text": "La quantité dans le bidon", "isCorrect": False}
                    ],
                    "correction": "Le premier chiffre suivi de W (Winter) indique la fluidité de l'huile à froid."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel élément assure la circulation du liquide de refroidissement dans le moteur ?",
                    "answerOptions": [
                        {"text": "La pompe à eau", "isCorrect": True},
                        {"text": "Le radiateur moteur", "isCorrect": False},
                        {"text": "Le vase d'expansion", "isCorrect": False},
                        {"text": "Le thermostat d'eau", "isCorrect": False}
                    ],
                    "correction": "La pompe à eau force la circulation du liquide de refroidissement à travers le bloc moteur et le radiateur."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le rôle du filtre à air ?",
                    "answerOptions": [
                        {"text": "Retenir les poussières", "isCorrect": True},
                        {"text": "Filtrer l'essence", "isCorrect": False},
                        {"text": "Refroidir l'air entrant", "isCorrect": False},
                        {"text": "Mesurer le débit d'air", "isCorrect": False}
                    ],
                    "correction": "Son rôle exclusif est de retenir les impuretés et poussières contenues dans l'air ambiant."
                },
                {
                    "questionNumber": 7,
                    "question": "Quand doit-on contrôler le niveau d'huile moteur pour une précision maximale ?",
                    "answerOptions": [
                        {"text": "Moteur froid et à plat", "isCorrect": True},
                        {"text": "Moteur chaud et tournant", "isCorrect": False},
                        {"text": "Moteur froid en pente", "isCorrect": False},
                        {"text": "Moteur chaud et en pente", "isCorrect": False}
                    ],
                    "correction": "Le niveau se vérifie idéalement sur un sol horizontal et moteur froid pour que l'huile soit redescendue dans le carter."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle pièce relie le piston au vilebrequin ?",
                    "answerOptions": [
                        {"text": "La bielle", "isCorrect": True},
                        {"text": "La culasse", "isCorrect": False},
                        {"text": "La soupape", "isCorrect": False},
                        {"text": "Le segment", "isCorrect": False}
                    ],
                    "correction": "La bielle transforme le mouvement rectiligne alternatif du piston en mouvement rotatif du vilebrequin."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel composant permet d'enflammer le mélange air-essence dans un moteur essence ?",
                    "answerOptions": [
                        {"text": "La bougie d'allumage", "isCorrect": True},
                        {"text": "La bougie de préchauffage", "isCorrect": False},
                        {"text": "L'injecteur de carburant", "isCorrect": False},
                        {"text": "La bobine d'allumage", "isCorrect": False}
                    ],
                    "correction": "C'est l'étincelle électrique de la bougie d'allumage qui déclenche la combustion."
                },
                {
                    "questionNumber": 10,
                    "question": "Que faut-il remplacer systématiquement lors d'une vidange moteur ?",
                    "answerOptions": [
                        {"text": "Le joint de bouchon", "isCorrect": True},
                        {"text": "Le bouchon de vidange", "isCorrect": False},
                        {"text": "Le carter d'huile", "isCorrect": False},
                        {"text": "La jauge à huile", "isCorrect": False}
                    ],
                    "correction": "Le joint s'écrase au serrage pour assurer l'étanchéité et doit être changé à chaque intervention."
                },
                {
                    "questionNumber": 11,
                    "question": "À quoi sert le vase d'expansion dans le circuit de refroidissement ?",
                    "answerOptions": [
                        {"text": "Compenser la dilatation du liquide", "isCorrect": True},
                        {"text": "Refroidir directement le moteur", "isCorrect": False},
                        {"text": "Filtrer les impuretés du liquide", "isCorrect": False},
                        {"text": "Chauffer l'habitacle du véhicule", "isCorrect": False}
                    ],
                    "correction": "Le liquide change de volume en chauffant ; le vase d'expansion absorbe ces variations."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la conséquence d'une courroie de distribution cassée moteur tournant ?",
                    "answerOptions": [
                        {"text": "La casse moteur", "isCorrect": True},
                        {"text": "Une simple panne d'essence", "isCorrect": False},
                        {"text": "Un bruit de sifflement", "isCorrect": False},
                        {"text": "L'arrêt de la climatisation", "isCorrect": False}
                    ],
                    "correction": "La synchronisation est perdue, les pistons percutent les soupapes, entraînant des dégâts majeurs."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est le rôle des segments situés sur le piston ?",
                    "answerOptions": [
                        {"text": "Assurer l'étanchéité", "isCorrect": True},
                        {"text": "Guider la bielle", "isCorrect": False},
                        {"text": "Fixer l'axe de piston", "isCorrect": False},
                        {"text": "Alléger le piston", "isCorrect": False}
                    ],
                    "correction": "Ils assurent l'étanchéité aux gaz de combustion et raclent l'huile."
                },
                {
                    "questionNumber": 14,
                    "question": "Lors du remplacement d'un filtre à huile vissé, que faut-il faire avant le montage ?",
                    "answerOptions": [
                        {"text": "Huiler le joint", "isCorrect": True},
                        {"text": "Remplir le filtre d'eau", "isCorrect": False},
                        {"text": "Graisser le filetage", "isCorrect": False},
                        {"text": "Poncer le plan de joint", "isCorrect": False}
                    ],
                    "correction": "Il faut enduire le joint d'huile moteur propre pour éviter qu'il ne se déchire ou ne grippe."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel liquide utilise-t-on pour le système de refroidissement d'un moteur moderne ?",
                    "answerOptions": [
                        {"text": "Un liquide spécifique", "isCorrect": True},
                        {"text": "De l'eau du robinet", "isCorrect": False},
                        {"text": "De l'eau déminéralisée", "isCorrect": False},
                        {"text": "De l'huile hydraulique", "isCorrect": False}
                    ],
                    "correction": "On utilise un liquide spécifique (eau + antigel + additifs) qui ne gèle pas et ne bout pas à 100°C."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle pièce du moteur ferme le haut des cylindres et supporte les soupapes ?",
                    "answerOptions": [
                        {"text": "La culasse", "isCorrect": True},
                        {"text": "Le bas moteur", "isCorrect": False},
                        {"text": "Le cache-culbuteurs", "isCorrect": False},
                        {"text": "Le joint de culasse", "isCorrect": False}
                    ],
                    "correction": "La culasse coiffe le bloc moteur et contient les chambres de combustion."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le symptôme principal d'un joint de culasse défectueux ?",
                    "answerOptions": [
                        {"text": "Fumée blanche épaisse", "isCorrect": True},
                        {"text": "Fumée noire à l'échappement", "isCorrect": False},
                        {"text": "Cliquetis dans le moteur", "isCorrect": False},
                        {"text": "Usure des pneus avant", "isCorrect": False}
                    ],
                    "correction": "Une fumée blanche épaisse à chaud indique que du liquide de refroidissement pénètre dans les cylindres."
                },
                {
                    "questionNumber": 18,
                    "question": "Qu'est-ce que la cylindrée unitaire d'un moteur ?",
                    "answerOptions": [
                        {"text": "Le volume d'un cylindre", "isCorrect": True},
                        {"text": "Le volume total du moteur", "isCorrect": False},
                        {"text": "La puissance du moteur", "isCorrect": False},
                        {"text": "Le diamètre du piston", "isCorrect": False}
                    ],
                    "correction": "C'est le volume balayé par le piston entre le PMB et le PMH dans un seul cylindre."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel outil permet de serrer une vis au couple prescrit par le constructeur ?",
                    "answerOptions": [
                        {"text": "Une clé dynamométrique", "isCorrect": True},
                        {"text": "Une clé à chocs pneumatique", "isCorrect": False},
                        {"text": "Une clé plate mixte", "isCorrect": False},
                        {"text": "Une pince multiprise", "isCorrect": False}
                    ],
                    "correction": "La clé dynamométrique permet d'appliquer une force de serrage (couple) exacte."
                },
                {
                    "questionNumber": 20,
                    "question": "Pourquoi ne doit-on jamais ouvrir le bouchon du vase d'expansion moteur chaud ?",
                    "answerOptions": [
                        {"text": "Risque de brûlures graves", "isCorrect": True},
                        {"text": "Risque de désamorcer la pompe", "isCorrect": False},
                        {"text": "Risque de faire entrer de l'air", "isCorrect": False},
                        {"text": "Risque de casser le bouchon", "isCorrect": False}
                    ],
                    "correction": "Le circuit est sous pression ; l'ouverture brutale provoque une éjection de liquide bouillant."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : LIAISON AU SOL (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : LIAISON AU SOL",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la limite légale d'usure de la profondeur des sculptures d'un pneu ?",
                    "answerOptions": [
                        {"text": "1,6 mm", "isCorrect": True},
                        {"text": "1,0 mm", "isCorrect": False},
                        {"text": "2,5 mm", "isCorrect": False},
                        {"text": "3,0 mm", "isCorrect": False}
                    ],
                    "correction": "Le Code de la route impose 1,6 mm minimum pour évacuer l'eau."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est le rôle principal de l'amortisseur ?",
                    "answerOptions": [
                        {"text": "Freiner les oscillations du ressort", "isCorrect": True},
                        {"text": "Supporter tout le poids du véhicule", "isCorrect": False},
                        {"text": "Remplacer les ressorts de suspension", "isCorrect": False},
                        {"text": "Diriger les roues avant dans les virages", "isCorrect": False}
                    ],
                    "correction": "L'amortisseur freine l'effet de rebond du ressort pour maintenir la roue au sol."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel outil utilise-t-on pour mesurer la pression des pneumatiques ?",
                    "answerOptions": [
                        {"text": "Un manomètre", "isCorrect": True},
                        {"text": "Un thermomètre", "isCorrect": False},
                        {"text": "Un micromètre", "isCorrect": False},
                        {"text": "Un tachymètre", "isCorrect": False}
                    ],
                    "correction": "Le manomètre mesure la pression des fluides."
                },
                {
                    "questionNumber": 24,
                    "question": "Une usure prononcée uniquement sur les deux bords extérieurs de la bande de roulement indique :",
                    "answerOptions": [
                        {"text": "Un sous-gonflage", "isCorrect": True},
                        {"text": "Un sur-gonflage", "isCorrect": False},
                        {"text": "Un carrossage négatif", "isCorrect": False},
                        {"text": "Un freinage trop brusque", "isCorrect": False}
                    ],
                    "correction": "Un pneu sous-gonflé s'écrase et porte sur ses épaules, créant une usure latérale."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la propriété physique essentielle du liquide de frein ?",
                    "answerOptions": [
                        {"text": "Incompressible", "isCorrect": True},
                        {"text": "Inflammable", "isCorrect": False},
                        {"text": "Compressible", "isCorrect": False},
                        {"text": "Élastique", "isCorrect": False}
                    ],
                    "correction": "Le liquide doit être incompressible pour transmettre l'effort de freinage instantanément."
                },
                {
                    "questionNumber": 26,
                    "question": "Sur un pneu de dimension 205/55 R 16, que représente le chiffre 16 ?",
                    "answerOptions": [
                        {"text": "Le diamètre de la jante", "isCorrect": True},
                        {"text": "La largeur du pneu", "isCorrect": False},
                        {"text": "La hauteur du flanc", "isCorrect": False},
                        {"text": "L'indice de vitesse", "isCorrect": False}
                    ],
                    "correction": "16 indique le diamètre intérieur du pneu (en pouces)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel élément frotte contre le disque pour freiner le véhicule ?",
                    "answerOptions": [
                        {"text": "Les plaquettes", "isCorrect": True},
                        {"text": "Les segments", "isCorrect": False},
                        {"text": "Les tambours", "isCorrect": False},
                        {"text": "Les étriers", "isCorrect": False}
                    ],
                    "correction": "Les plaquettes sont pincées contre le disque par l'étrier."
                },
                {
                    "questionNumber": 28,
                    "question": "À quoi sert le système ABS lors d'un freinage d'urgence ?",
                    "answerOptions": [
                        {"text": "Éviter le blocage des roues", "isCorrect": True},
                        {"text": "Réduire la distance de moitié", "isCorrect": False},
                        {"text": "Refroidir les disques de frein", "isCorrect": False},
                        {"text": "Augmenter la puissance moteur", "isCorrect": False}
                    ],
                    "correction": "L'ABS relâche la pression pour éviter le blocage et garder le contrôle directionnel."
                },
                {
                    "questionNumber": 29,
                    "question": "Pourquoi est-il nécessaire de purger un circuit de freinage hydraulique ?",
                    "answerOptions": [
                        {"text": "Pour chasser l'air", "isCorrect": True},
                        {"text": "Pour retirer l'huile", "isCorrect": False},
                        {"text": "Pour nettoyer les disques", "isCorrect": False},
                        {"text": "Pour graisser les pistons", "isCorrect": False}
                    ],
                    "correction": "L'air est compressible et rend la pédale molle ; il faut l'évacuer."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel composant transforme le mouvement de rotation du volant en mouvement de translation pour braquer les roues ?",
                    "answerOptions": [
                        {"text": "La crémaillère", "isCorrect": True},
                        {"text": "Le cardan", "isCorrect": False},
                        {"text": "L'amortisseur", "isCorrect": False},
                        {"text": "Le triangle", "isCorrect": False}
                    ],
                    "correction": "Le pignon s'engrène sur la crémaillère qui se déplace latéralement."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel défaut de géométrie correspond à des roues avant qui 'regardent' vers l'intérieur ?",
                    "answerOptions": [
                        {"text": "Le pincement", "isCorrect": True},
                        {"text": "L'ouverture", "isCorrect": False},
                        {"text": "La chasse", "isCorrect": False},
                        {"text": "Le carrossage", "isCorrect": False}
                    ],
                    "correction": "Le pincement est la convergence des roues vers l'avant."
                },
                {
                    "questionNumber": 32,
                    "question": "Que signifie l'indice 'DOT' sur un bidon de liquide de frein ?",
                    "answerOptions": [
                        {"text": "Department of Transportation", "isCorrect": True},
                        {"text": "Direction Of Tires", "isCorrect": False},
                        {"text": "Digital Oil Temperature", "isCorrect": False},
                        {"text": "Direct On Turbo", "isCorrect": False}
                    ],
                    "correction": "C'est une norme de sécurité américaine classant les liquides selon leur point d'ébullition."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le rôle du servo-frein (ou Master-vac) ?",
                    "answerOptions": [
                        {"text": "Amplifier l'effort conducteur", "isCorrect": True},
                        {"text": "Remplacer le frein à main", "isCorrect": False},
                        {"text": "Créer la pression hydraulique", "isCorrect": False},
                        {"text": "Répartir le freinage avant-arrière", "isCorrect": False}
                    ],
                    "correction": "Il utilise la dépression moteur pour multiplier la force exercée sur la pédale."
                },
                {
                    "questionNumber": 34,
                    "question": "Pourquoi équilibre-t-on une roue après le montage d'un pneu neuf ?",
                    "answerOptions": [
                        {"text": "Pour supprimer les vibrations", "isCorrect": True},
                        {"text": "Pour gonfler le pneu plus vite", "isCorrect": False},
                        {"text": "Pour faciliter le serrage des écrous", "isCorrect": False},
                        {"text": "Pour améliorer l'esthétique de la jante", "isCorrect": False}
                    ],
                    "correction": "L'équilibrage compense les écarts de masse pour éviter les vibrations au volant."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel élément assure la liaison élastique entre le châssis et la roue ?",
                    "answerOptions": [
                        {"text": "Le ressort", "isCorrect": True},
                        {"text": "La rotule", "isCorrect": False},
                        {"text": "La barre stab", "isCorrect": False},
                        {"text": "Le cardan", "isCorrect": False}
                    ],
                    "correction": "Le ressort se déforme pour absorber les chocs de la route."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle pièce mécanique permet de transmettre le couple moteur aux roues tout en autorisant le braquage ?",
                    "answerOptions": [
                        {"text": "Le cardan", "isCorrect": True},
                        {"text": "L'embrayage", "isCorrect": False},
                        {"text": "Le triangle", "isCorrect": False},
                        {"text": "La fusée", "isCorrect": False}
                    ],
                    "correction": "Le cardan (transmission) possède des joints homocinétiques pour s'adapter aux angles."
                },
                {
                    "questionNumber": 37,
                    "question": "Qu'est-ce que 'l'aquaplaning' ?",
                    "answerOptions": [
                        {"text": "La perte d'adhérence sur l'eau", "isCorrect": True},
                        {"text": "Le nettoyage automatique des pneus", "isCorrect": False},
                        {"text": "Un système de freinage pour bateau", "isCorrect": False},
                        {"text": "Une technique de conduite sur glace", "isCorrect": False}
                    ],
                    "correction": "Une pellicule d'eau s'insère sous le pneu qui ne touche plus le sol."
                },
                {
                    "questionNumber": 38,
                    "question": "Sur un étrier de frein flottant, quelle pièce reçoit la pression hydraulique pour pousser les plaquettes ?",
                    "answerOptions": [
                        {"text": "Le piston", "isCorrect": True},
                        {"text": "La vis de purge", "isCorrect": False},
                        {"text": "Le disque ventilé", "isCorrect": False},
                        {"text": "La colonnette", "isCorrect": False}
                    ],
                    "correction": "Le piston reçoit la pression hydraulique."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel contrôle visuel simple permet de vérifier l'état des plaquettes de frein sans démontage ?",
                    "answerOptions": [
                        {"text": "L'épaisseur de la garniture", "isCorrect": True},
                        {"text": "La couleur de l'étrier", "isCorrect": False},
                        {"text": "La brillance du disque", "isCorrect": False},
                        {"text": "La date de fabrication", "isCorrect": False}
                    ],
                    "correction": "On vérifie l'épaisseur de matière restante sur la plaquette."
                },
                {
                    "questionNumber": 40,
                    "question": "Si la pédale de frein s'enfonce lentement jusqu'au plancher lors d'un appui constant à l'arrêt, cela indique :",
                    "answerOptions": [
                        {"text": "Une fuite interne ou externe", "isCorrect": True},
                        {"text": "Un niveau de liquide trop haut", "isCorrect": False},
                        {"text": "Des plaquettes de frein neuves", "isCorrect": False},
                        {"text": "Un disque de frein voilé", "isCorrect": False}
                    ],
                    "correction": "Cela signale une perte de pression (fuite)."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : TRANSMISSION ET CHAÎNE CINÉMATIQUE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : TRANSMISSION ET CHAÎNE CINÉMATIQUE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la fonction principale de l'embrayage ?",
                    "answerOptions": [
                        {"text": "Accoupler et désaccoupler", "isCorrect": True},
                        {"text": "Augmenter la puissance moteur", "isCorrect": False},
                        {"text": "Freiner le véhicule en descente", "isCorrect": False},
                        {"text": "Refroidir l'huile de la boîte", "isCorrect": False}
                    ],
                    "correction": "Il permet de lier (accoupler) ou séparer (désaccoupler) le moteur de la boîte de vitesses."
                },
                {
                    "questionNumber": 42,
                    "question": "De quels éléments est composé un kit d'embrayage standard ?",
                    "answerOptions": [
                        {"text": "Mécanisme disque et butée", "isCorrect": True},
                        {"text": "Piston bielle et vilebrequin", "isCorrect": False},
                        {"text": "Arbre pignon et couronne", "isCorrect": False},
                        {"text": "Étrier plaquette et disque", "isCorrect": False}
                    ],
                    "correction": "Le kit '3 pièces' comprend le mécanisme, le disque et la butée."
                },
                {
                    "questionNumber": 43,
                    "question": "Lorsqu'un conducteur appuie à fond sur la pédale d'embrayage, on dit qu'il est :",
                    "answerOptions": [
                        {"text": "Débrayé", "isCorrect": True},
                        {"text": "Embrayé", "isCorrect": False},
                        {"text": "Accouplé", "isCorrect": False},
                        {"text": "En prise", "isCorrect": False}
                    ],
                    "correction": "Appuyer sur la pédale = DÉBRAYER (couper la liaison)."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le rôle de la boîte de vitesses ?",
                    "answerOptions": [
                        {"text": "Adapter le couple et la vitesse", "isCorrect": True},
                        {"text": "Produire de l'énergie électrique", "isCorrect": False},
                        {"text": "Filtrer les gaz d'échappement", "isCorrect": False},
                        {"text": "Orienter les roues directrices", "isCorrect": False}
                    ],
                    "correction": "Elle multiplie la force (couple) ou la vitesse selon les besoins."
                },
                {
                    "questionNumber": 45,
                    "question": "Dans une boîte manuelle, comment appelle-t-on l'arbre relié au moteur (via l'embrayage) ?",
                    "answerOptions": [
                        {"text": "L'arbre primaire", "isCorrect": True},
                        {"text": "L'arbre secondaire", "isCorrect": False},
                        {"text": "L'arbre de transmission", "isCorrect": False},
                        {"text": "L'arbre à cames", "isCorrect": False}
                    ],
                    "correction": "L'énergie entre par l'arbre primaire."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel composant permet aux roues motrices de tourner à des vitesses différentes dans un virage ?",
                    "answerOptions": [
                        {"text": "Le différentiel", "isCorrect": True},
                        {"text": "Le turbo", "isCorrect": False},
                        {"text": "L'alternateur", "isCorrect": False},
                        {"text": "Le radiateur", "isCorrect": False}
                    ],
                    "correction": "Le différentiel autorise la différence de vitesse entre roue intérieure et extérieure."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle pièce protège les articulations du cardan (transmission) et retient la graisse ?",
                    "answerOptions": [
                        {"text": "Le soufflet", "isCorrect": True},
                        {"text": "Le joint spi", "isCorrect": False},
                        {"text": "La rotule", "isCorrect": False},
                        {"text": "Le silentbloc", "isCorrect": False}
                    ],
                    "correction": "Le soufflet de cardan retient la graisse et empêche les impuretés d'entrer."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est le symptôme caractéristique d'un cardan usé ?",
                    "answerOptions": [
                        {"text": "Un claquement en virage", "isCorrect": True},
                        {"text": "Un sifflement au freinage", "isCorrect": False},
                        {"text": "Une fumée bleue au pot", "isCorrect": False},
                        {"text": "Un volant dur à tourner", "isCorrect": False}
                    ],
                    "correction": "Un bruit de 'clac-clac' en braquant est typique."
                },
                {
                    "questionNumber": 49,
                    "question": "Sur quoi frotte le disque d'embrayage pour transmettre le mouvement ?",
                    "answerOptions": [
                        {"text": "Le volant moteur", "isCorrect": True},
                        {"text": "Le carter d'huile", "isCorrect": False},
                        {"text": "La poulie damper", "isCorrect": False},
                        {"text": "Le collecteur", "isCorrect": False}
                    ],
                    "correction": "Le disque est pressé contre la face rectifiée du volant moteur."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel grade d'huile est typique pour une boîte de vitesses manuelle ?",
                    "answerOptions": [
                        {"text": "75W80", "isCorrect": True},
                        {"text": "5W30", "isCorrect": False},
                        {"text": "10W40", "isCorrect": False},
                        {"text": "DOT 4", "isCorrect": False}
                    ],
                    "correction": "L'huile de boîte est visqueuse, souvent 75W80 ou 80W90."
                },
                {
                    "questionNumber": 51,
                    "question": "À quoi servent les 'synchros' (synchroniseurs) dans une boîte de vitesses ?",
                    "answerOptions": [
                        {"text": "Faciliter le passage des vitesses", "isCorrect": True},
                        {"text": "Augmenter la puissance du moteur", "isCorrect": False},
                        {"text": "Refroidir les pignons de boîte", "isCorrect": False},
                        {"text": "Réduire la consommation d'huile", "isCorrect": False}
                    ],
                    "correction": "Ils amènent les pignons à la même vitesse pour éviter les craquements."
                },
                {
                    "questionNumber": 52,
                    "question": "Si le régime moteur augmente à l'accélération mais que la vitesse n'augmente pas proportionnellement, l'embrayage :",
                    "answerOptions": [
                        {"text": "Patine", "isCorrect": True},
                        {"text": "Colle", "isCorrect": False},
                        {"text": "Grippe", "isCorrect": False},
                        {"text": "Bloque", "isCorrect": False}
                    ],
                    "correction": "Le disque glisse (patine) car il n'accroche plus assez le volant moteur."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle pièce transmet le mouvement de la boîte de vitesses aux roues ?",
                    "answerOptions": [
                        {"text": "La transmission transversale", "isCorrect": True},
                        {"text": "La barre stabilisatrice", "isCorrect": False},
                        {"text": "La crémaillère de direction", "isCorrect": False},
                        {"text": "Le triangle de suspension", "isCorrect": False}
                    ],
                    "correction": "La transmission (ou cardan) relie la boîte au moyeu de roue."
                },
                {
                    "questionNumber": 54,
                    "question": "Sur un embrayage hydraulique, quelle pièce reçoit la pression pour actionner la fourchette ?",
                    "answerOptions": [
                        {"text": "Le récepteur", "isCorrect": True},
                        {"text": "L'émetteur", "isCorrect": False},
                        {"text": "Le master-vac", "isCorrect": False},
                        {"text": "Le répartiteur", "isCorrect": False}
                    ],
                    "correction": "L'émetteur (pédale) pousse le liquide vers le récepteur (boîte)."
                },
                {
                    "questionNumber": 55,
                    "question": "En première vitesse, par rapport à la quatrième vitesse, le couple aux roues est :",
                    "answerOptions": [
                        {"text": "Plus élevé", "isCorrect": True},
                        {"text": "Plus faible", "isCorrect": False},
                        {"text": "Identique", "isCorrect": False},
                        {"text": "Nul", "isCorrect": False}
                    ],
                    "correction": "La 1ère vitesse démultiplie la rotation pour multiplier la force (couple)."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le rôle du diaphragme dans le mécanisme d'embrayage ?",
                    "answerOptions": [
                        {"text": "Agir comme un ressort", "isCorrect": True},
                        {"text": "Filtrer l'huile de boîte", "isCorrect": False},
                        {"text": "Ventiler le mécanisme", "isCorrect": False},
                        {"text": "Mesurer la vitesse", "isCorrect": False}
                    ],
                    "correction": "C'est une rondelle élastique qui plaque le disque contre le volant moteur."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'est-ce qui est spécifique à la marche arrière dans une boîte de vitesses ?",
                    "answerOptions": [
                        {"text": "Un pignon intermédiaire", "isCorrect": True},
                        {"text": "Une courroie spéciale", "isCorrect": False},
                        {"text": "Un embrayage inversé", "isCorrect": False},
                        {"text": "Un deuxième moteur", "isCorrect": False}
                    ],
                    "correction": "Un pignon intermédiaire inverse le sens de rotation."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle pièce centrale du disque d'embrayage s'emboîte sur les cannelures de l'arbre primaire ?",
                    "answerOptions": [
                        {"text": "Le moyeu", "isCorrect": True},
                        {"text": "La frette", "isCorrect": False},
                        {"text": "La garniture", "isCorrect": False},
                        {"text": "Les ressorts", "isCorrect": False}
                    ],
                    "correction": "Le moyeu cannelé assure la liaison en rotation avec l'arbre primaire."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel entretien est nécessaire sur un embrayage à sec standard ?",
                    "answerOptions": [
                        {"text": "Aucun entretien courant", "isCorrect": True},
                        {"text": "Graissage tous les mois", "isCorrect": False},
                        {"text": "Vidange tous les ans", "isCorrect": False},
                        {"text": "Tension des ressorts", "isCorrect": False}
                    ],
                    "correction": "C'est une pièce d'usure sans entretien (pas de vidange ni graissage)."
                },
                {
                    "questionNumber": 60,
                    "question": "Dans le différentiel, comment appelle-t-on les petits pignons coniques situés à l'intérieur du boîtier ?",
                    "answerOptions": [
                        {"text": "Les satellites et planétaires", "isCorrect": True},
                        {"text": "Les soupapes et culbuteurs", "isCorrect": False},
                        {"text": "Les bielles et pistons", "isCorrect": False},
                        {"text": "Les vis et les écrous", "isCorrect": False}
                    ],
                    "correction": "Le mécanisme interne est composé de planétaires et de satellites."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : ÉLECTRICITÉ ET SIGNALISATION (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ÉLECTRICITÉ ET SIGNALISATION",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est l'unité de mesure de la tension électrique (U) ?",
                    "answerOptions": [
                        {"text": "Le Volt", "isCorrect": True},
                        {"text": "L'Ampère", "isCorrect": False},
                        {"text": "L'Ohm", "isCorrect": False},
                        {"text": "Le Watt", "isCorrect": False}
                    ],
                    "correction": "La tension se mesure en Volts (V)."
                },
                {
                    "questionNumber": 62,
                    "question": "Sur quelle position régler le multimètre pour une batterie de voiture ?",
                    "answerOptions": [
                        {"text": "Voltmètre courant continu", "isCorrect": True},
                        {"text": "Voltmètre courant alternatif", "isCorrect": False},
                        {"text": "Ohmmètre résistance", "isCorrect": False},
                        {"text": "Ampèremètre intensité", "isCorrect": False}
                    ],
                    "correction": "Une batterie délivre du courant continu (DC / V=)."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est le rôle principal de l'alternateur ?",
                    "answerOptions": [
                        {"text": "Recharger la batterie moteur tournant", "isCorrect": True},
                        {"text": "Démarrer le moteur thermique le matin", "isCorrect": False},
                        {"text": "Protéger le circuit contre les courts-circuits", "isCorrect": False},
                        {"text": "Convertir le courant continu en alternatif", "isCorrect": False}
                    ],
                    "correction": "Il produit de l'électricité pour les consommateurs et recharge la batterie."
                },
                {
                    "questionNumber": 64,
                    "question": "Comment se branche un ampèremètre pour mesurer l'intensité ?",
                    "answerOptions": [
                        {"text": "En série", "isCorrect": True},
                        {"text": "En parallèle", "isCorrect": False},
                        {"text": "En dérivation", "isCorrect": False},
                        {"text": "Aux bornes de la batterie", "isCorrect": False}
                    ],
                    "correction": "Le courant doit traverser l'appareil, donc branchement en série."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la fonction d'un fusible ?",
                    "answerOptions": [
                        {"text": "Fondre en cas de surintensité", "isCorrect": True},
                        {"text": "Augmenter la tension du circuit", "isCorrect": False},
                        {"text": "Stocker l'énergie électrique", "isCorrect": False},
                        {"text": "Refroidir les fils électriques", "isCorrect": False}
                    ],
                    "correction": "Il fond pour couper le circuit en cas de surcharge, protégeant le faisceau."
                },
                {
                    "questionNumber": 66,
                    "question": "Quelle tension doit-on mesurer aux bornes de la batterie moteur tournant ?",
                    "answerOptions": [
                        {"text": "Environ 14 Volts", "isCorrect": True},
                        {"text": "Exactement 12 Volts", "isCorrect": False},
                        {"text": "Moins de 10 Volts", "isCorrect": False},
                        {"text": "Environ 24 Volts", "isCorrect": False}
                    ],
                    "correction": "L'alternateur charge, la tension monte entre 13,5V et 14,5V."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle formule représente la Loi d'Ohm ?",
                    "answerOptions": [
                        {"text": "U = R x I", "isCorrect": True},
                        {"text": "U = R / I", "isCorrect": False},
                        {"text": "R = U x I", "isCorrect": False},
                        {"text": "I = U x R", "isCorrect": False}
                    ],
                    "correction": "U (Tension) = R (Résistance) x I (Intensité)."
                },
                {
                    "questionNumber": 68,
                    "question": "De combien d'éléments de 2 Volts une batterie de 12 Volts est-elle constituée ?",
                    "answerOptions": [
                        {"text": "6 éléments", "isCorrect": True},
                        {"text": "4 éléments", "isCorrect": False},
                        {"text": "12 éléments", "isCorrect": False},
                        {"text": "2 éléments", "isCorrect": False}
                    ],
                    "correction": "6 éléments x 2V = 12V."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle couleur de voyant s'allume pour les feux de route (pleins phares) ?",
                    "answerOptions": [
                        {"text": "Bleu", "isCorrect": True},
                        {"text": "Vert", "isCorrect": False},
                        {"text": "Orange", "isCorrect": False},
                        {"text": "Rouge", "isCorrect": False}
                    ],
                    "correction": "Le voyant des feux de route est réglementairement Bleu."
                },
                {
                    "questionNumber": 70,
                    "question": "Qu'est-ce qu'un relais dans un circuit automobile ?",
                    "answerOptions": [
                        {"text": "Un interrupteur commandé à distance", "isCorrect": True},
                        {"text": "Un générateur de courant continu", "isCorrect": False},
                        {"text": "Un consommateur de forte puissance", "isCorrect": False},
                        {"text": "Un capteur de température moteur", "isCorrect": False}
                    ],
                    "correction": "Il utilise un petit courant de commande pour fermer un circuit de puissance."
                },
                {
                    "questionNumber": 71,
                    "question": "Pour mesurer une résistance (en Ohms), le circuit doit impérativement être :",
                    "answerOptions": [
                        {"text": "Hors tension", "isCorrect": True},
                        {"text": "Sous tension", "isCorrect": False},
                        {"text": "Moteur tournant", "isCorrect": False},
                        {"text": "Phares allumés", "isCorrect": False}
                    ],
                    "correction": "Si le circuit est sous tension, la mesure est fausse et l'ohmmètre peut griller."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel composant permet de lancer le moteur thermique au démarrage ?",
                    "answerOptions": [
                        {"text": "Le démarreur", "isCorrect": True},
                        {"text": "L'alternateur", "isCorrect": False},
                        {"text": "Le compresseur", "isCorrect": False},
                        {"text": "Le calculateur", "isCorrect": False}
                    ],
                    "correction": "Le démarreur est un moteur électrique puissant qui lance le moteur thermique."
                },
                {
                    "questionNumber": 73,
                    "question": "En électricité automobile, le pôle négatif de la batterie est relié :",
                    "answerOptions": [
                        {"text": "À la masse (carrosserie)", "isCorrect": True},
                        {"text": "Au démarreur uniquement", "isCorrect": False},
                        {"text": "Aux phares avant", "isCorrect": False},
                        {"text": "Au calculateur moteur", "isCorrect": False}
                    ],
                    "correction": "La carrosserie métallique sert de conducteur de retour (Masse)."
                },
                {
                    "questionNumber": 74,
                    "question": "Que signifie le terme 'Multiplexage' simplifié ?",
                    "answerOptions": [
                        {"text": "Faire passer plusieurs informations sur un même fil", "isCorrect": True},
                        {"text": "Mettre plusieurs batteries dans le coffre", "isCorrect": False},
                        {"text": "Utiliser des fils plus gros pour les phares", "isCorrect": False},
                        {"text": "Multiplier la tension par deux", "isCorrect": False}
                    ],
                    "correction": "Faire circuler des informations codées numériques via un réseau réduit de fils."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel liquide trouve-t-on dans une batterie au plomb standard ?",
                    "answerOptions": [
                        {"text": "De l'électrolyte", "isCorrect": True},
                        {"text": "De l'huile minérale", "isCorrect": False},
                        {"text": "Du liquide de frein", "isCorrect": False},
                        {"text": "De l'essence sans plomb", "isCorrect": False}
                    ],
                    "correction": "L'électrolyte (mélange eau + acide sulfurique)."
                },
                {
                    "questionNumber": 76,
                    "question": "Si un fusible grille instantanément dès qu'on le remplace, il y a probablement :",
                    "answerOptions": [
                        {"text": "Un court-circuit franc", "isCorrect": True},
                        {"text": "Une batterie déchargée", "isCorrect": False},
                        {"text": "Une ampoule grillée", "isCorrect": False},
                        {"text": "Un faux contact oxydé", "isCorrect": False}
                    ],
                    "correction": "Le court-circuit est permanent, il faut trouver la panne avant de changer le fusible."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le rôle des bougies de préchauffage sur un moteur Diesel ?",
                    "answerOptions": [
                        {"text": "Réchauffer la chambre de combustion", "isCorrect": True},
                        {"text": "Créer l'étincelle d'allumage", "isCorrect": False},
                        {"text": "Refroidir le gasoil injecté", "isCorrect": False},
                        {"text": "Nettoyer les injecteurs", "isCorrect": False}
                    ],
                    "correction": "Elles aident à l'auto-inflammation du gasoil lors des démarrages à froid."
                },
                {
                    "questionNumber": 78,
                    "question": "Comment vérifier visuellement si une ampoule à filament est grillée ?",
                    "answerOptions": [
                        {"text": "Le filament est coupé", "isCorrect": True},
                        {"text": "Le verre est transparent", "isCorrect": False},
                        {"text": "Le culot est en métal", "isCorrect": False},
                        {"text": "La marque est illisible", "isCorrect": False}
                    ],
                    "correction": "Si le filament est rompu, le circuit est ouvert."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle précaution est primordiale avant d'intervenir sur le démarreur ?",
                    "answerOptions": [
                        {"text": "Débrancher la batterie", "isCorrect": True},
                        {"text": "Mettre les pleins phares", "isCorrect": False},
                        {"text": "Gonfler les pneus", "isCorrect": False},
                        {"text": "Ouvrir les vitres", "isCorrect": False}
                    ],
                    "correction": "Risque de court-circuit violent car le câble vient directement du '+' batterie."
                },
                {
                    "questionNumber": 80,
                    "question": "Qu'indique l'unité 'Ah' (Ampère-heure) sur une batterie ?",
                    "answerOptions": [
                        {"text": "La capacité de stockage", "isCorrect": True},
                        {"text": "La tension de la batterie", "isCorrect": False},
                        {"text": "La puissance au démarrage", "isCorrect": False},
                        {"text": "La date de fabrication", "isCorrect": False}
                    ],
                    "correction": "C'est la quantité d'énergie (réserve) que la batterie peut stocker."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SANTÉ, SÉCURITÉ, ENVIRONNEMENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : SANTÉ, SÉCURITÉ, ENVIRONNEMENT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Que signifie le sigle EPI ?",
                    "answerOptions": [
                        {"text": "Équipement de Protection Individuelle", "isCorrect": True},
                        {"text": "Établissement Public Industriel", "isCorrect": False},
                        {"text": "Entretien Périodique Informatique", "isCorrect": False},
                        {"text": "Élément Pour l'Incendie", "isCorrect": False}
                    ],
                    "correction": "Équipements portés par le travailleur pour se protéger (gants, lunettes...)."
                },
                {
                    "questionNumber": 82,
                    "question": "Après avoir levé un véhicule avec un cric, que doit-on placer avant de travailler dessous ?",
                    "answerOptions": [
                        {"text": "Des chandelles de calage", "isCorrect": True},
                        {"text": "Des parpaings en béton", "isCorrect": False},
                        {"text": "Des cales en bois tendre", "isCorrect": False},
                        {"text": "Un deuxième cric hydraulique", "isCorrect": False}
                    ],
                    "correction": "Interdiction formelle de passer sous un véhicule sans chandelles stables."
                },
                {
                    "questionNumber": 83,
                    "question": "Dans quelle poubelle doit-on jeter un filtre à huile usagé ?",
                    "answerOptions": [
                        {"text": "Déchets Industriels Spéciaux", "isCorrect": True},
                        {"text": "Déchets Industriels Banals", "isCorrect": False},
                        {"text": "La poubelle de bureau", "isCorrect": False},
                        {"text": "La benne à ferraille propre", "isCorrect": False}
                    ],
                    "correction": "C'est un déchet dangereux qui nécessite une filière spécifique (DIS)."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la bonne posture pour soulever une charge lourde ?",
                    "answerOptions": [
                        {"text": "Dos droit et jambes pliées", "isCorrect": True},
                        {"text": "Dos rond et jambes tendues", "isCorrect": False},
                        {"text": "Dos cambré et bras tendus", "isCorrect": False},
                        {"text": "Jambes écartées et dos courbé", "isCorrect": False}
                    ],
                    "correction": "Utiliser la force des cuisses en gardant le dos droit."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel équipement doit-on utiliser moteur tournant dans un atelier fermé ?",
                    "answerOptions": [
                        {"text": "Un extracteur de gaz", "isCorrect": True},
                        {"text": "Un ventilateur de plafond", "isCorrect": False},
                        {"text": "Un masque en papier", "isCorrect": False},
                        {"text": "Un absorbeur d'humidité", "isCorrect": False}
                    ],
                    "correction": "Il faut évacuer le monoxyde de carbone avec un extracteur branché sur l'échappement."
                },
                {
                    "questionNumber": 86,
                    "question": "Que faire immédiatement si du liquide de frein gicle dans les yeux ?",
                    "answerOptions": [
                        {"text": "Rincer à l'eau abondamment", "isCorrect": True},
                        {"text": "Frotter avec un chiffon sec", "isCorrect": False},
                        {"text": "Mettre des gouttes de collyre", "isCorrect": False},
                        {"text": "Fermer les yeux et attendre", "isCorrect": False}
                    ],
                    "correction": "Rincer à l'eau claire 10-15 minutes et consulter un médecin."
                },
                {
                    "questionNumber": 87,
                    "question": "À quoi sert la coque en acier des chaussures de sécurité ?",
                    "answerOptions": [
                        {"text": "Protéger contre l'écrasement", "isCorrect": True},
                        {"text": "Éviter l'usure de la chaussette", "isCorrect": False},
                        {"text": "Améliorer l'adhérence au sol", "isCorrect": False},
                        {"text": "Isoler du froid en hiver", "isCorrect": False}
                    ],
                    "correction": "Protéger les orteils contre la chute d'objets lourds."
                },
                {
                    "questionNumber": 88,
                    "question": "Sur un véhicule électrique, que signale une gaine de câble orange ?",
                    "answerOptions": [
                        {"text": "Danger Haute Tension", "isCorrect": True},
                        {"text": "Câble de masse 12 Volts", "isCorrect": False},
                        {"text": "Tuyau de lave-glace", "isCorrect": False},
                        {"text": "Circuit de climatisation", "isCorrect": False}
                    ],
                    "correction": "C'est la norme pour signaler la Haute Tension (Danger de mort)."
                },
                {
                    "questionNumber": 89,
                    "question": "Que signifie un pictogramme carré rouge avec une tête de mort ?",
                    "answerOptions": [
                        {"text": "Produit toxique ou mortel", "isCorrect": True},
                        {"text": "Produit corrosif pour la peau", "isCorrect": False},
                        {"text": "Produit inflammable", "isCorrect": False},
                        {"text": "Produit polluant l'eau", "isCorrect": False}
                    ],
                    "correction": "Toxicité aiguë (danger de mort par ingestion, inhalation ou contact)."
                },
                {
                    "questionNumber": 90,
                    "question": "Où doit-on jeter les chiffons souillés d'huile ?",
                    "answerOptions": [
                        {"text": "Dans le bac à chiffons sales", "isCorrect": True},
                        {"text": "Dans la poubelle à papiers", "isCorrect": False},
                        {"text": "Dans les toilettes de l'atelier", "isCorrect": False},
                        {"text": "Dans la nature derrière le garage", "isCorrect": False}
                    ],
                    "correction": "Ils sont inflammables et polluants, donc conteneur spécifique."
                },
                {
                    "questionNumber": 91,
                    "question": "Pourquoi ne jamais diriger une soufflette d'air comprimé vers la peau ?",
                    "answerOptions": [
                        {"text": "Risque d'embolie gazeuse", "isCorrect": True},
                        {"text": "Risque de coup de soleil", "isCorrect": False},
                        {"text": "Risque de salir la peau", "isCorrect": False},
                        {"text": "Risque de sécher la peau", "isCorrect": False}
                    ],
                    "correction": "L'air peut passer dans le sang et provoquer une embolie mortelle."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel extincteur pour un feu d'essence (Classe B) ?",
                    "answerOptions": [
                        {"text": "Poudre ou CO2", "isCorrect": True},
                        {"text": "Eau pulvérisée simple", "isCorrect": False},
                        {"text": "Couverture en laine", "isCorrect": False},
                        {"text": "Seau de sable humide", "isCorrect": False}
                    ],
                    "correction": "Poudre ou CO2 pour étouffer le feu. Jamais d'eau (l'essence flotte)."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel type de gants pour manipuler des produits chimiques ?",
                    "answerOptions": [
                        {"text": "Gants en nitrile étanches", "isCorrect": True},
                        {"text": "Gants en cuir épais", "isCorrect": False},
                        {"text": "Gants en laine polaire", "isCorrect": False},
                        {"text": "Gants en cotte de mailles", "isCorrect": False}
                    ],
                    "correction": "Le nitrile résiste aux hydrocarbures et protège la peau."
                },
                {
                    "questionNumber": 94,
                    "question": "Sur un pont élévateur, quelle action de sécurité est obligatoire avant de travailler ?",
                    "answerOptions": [
                        {"text": "Poser le pont sur les taquets", "isCorrect": True},
                        {"text": "Couper l'alimentation électrique", "isCorrect": False},
                        {"text": "Mettre une sangle de sécurité", "isCorrect": False},
                        {"text": "Laisser le pont en pression hydraulique", "isCorrect": False}
                    ],
                    "correction": "Verrouiller mécaniquement le pont sur ses crans de sécurité."
                },
                {
                    "questionNumber": 95,
                    "question": "Si du liquide de frein tombe sur la carrosserie, que faire ?",
                    "answerOptions": [
                        {"text": "Rincer tout de suite à l'eau", "isCorrect": True},
                        {"text": "Essuyer avec un chiffon sec", "isCorrect": False},
                        {"text": "Attendre que le produit sèche", "isCorrect": False},
                        {"text": "Mettre du diluant peinture", "isCorrect": False}
                    ],
                    "correction": "Rincer à l'eau immédiatement car c'est un décapant puissant."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel équipement est obligatoire pour utiliser un touret à meuler ?",
                    "answerOptions": [
                        {"text": "Des lunettes de protection", "isCorrect": True},
                        {"text": "Des gants en plastique fin", "isCorrect": False},
                        {"text": "Une écharpe autour du cou", "isCorrect": False},
                        {"text": "Des lunettes de soleil teintées", "isCorrect": False}
                    ],
                    "correction": "Risque de lésions oculaires par projections d'étincelles ou de limaille."
                },
                {
                    "questionNumber": 97,
                    "question": "À quoi sert un bac de rétention sous les fûts d'huile ?",
                    "answerOptions": [
                        {"text": "Récupérer les fuites accidentelles", "isCorrect": True},
                        {"text": "Ranger les outils de distribution", "isCorrect": False},
                        {"text": "Surélever les fûts pour le dos", "isCorrect": False},
                        {"text": "Laver les pièces mécaniques", "isCorrect": False}
                    ],
                    "correction": "Empêcher la pollution des sols en cas de fuite du fût."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel document lance officiellement l'intervention sur le véhicule ?",
                    "answerOptions": [
                        {"text": "L'Ordre de Réparation", "isCorrect": True},
                        {"text": "Le certificat d'immatriculation", "isCorrect": False},
                        {"text": "Le contrôle technique", "isCorrect": False},
                        {"text": "La facture proforma", "isCorrect": False}
                    ],
                    "correction": "L'O.R. est le contrat signé par le client autorisant les travaux."
                },
                {
                    "questionNumber": 99,
                    "question": "Pourquoi est-il interdit de transvaser des produits chimiques dans des bouteilles d'eau ?",
                    "answerOptions": [
                        {"text": "Risque grave de confusion et d'ingestion", "isCorrect": True},
                        {"text": "Le plastique va fondre immédiatement", "isCorrect": False},
                        {"text": "C'est difficile de verser dedans", "isCorrect": False},
                        {"text": "L'étiquette ne colle pas bien", "isCorrect": False}
                    ],
                    "correction": "Risque mortel qu'une personne boive le produit par erreur."
                },
                {
                    "questionNumber": 100,
                    "question": "Une flaque d'huile au sol constitue un risque de :",
                    "answerOptions": [
                        {"text": "Chute de plain-pied", "isCorrect": True},
                        {"text": "Risque électrique", "isCorrect": False},
                        {"text": "Risque auditif", "isCorrect": False},
                        {"text": "Troubles musculosquelettiques", "isCorrect": False}
                    ],
                    "correction": "Les glissades sont une cause majeure d'accidents en atelier."
                }
            ]
        }
    }
}