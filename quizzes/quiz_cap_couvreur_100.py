# Fichier : quiz_cap_couvreur_100.py

quiz_data = {
    "title": "Quiz CAP Couvreur : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MATÉRIAUX ET GÉOMÉTRIE DE COUVERTURE (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Matériaux et Géométrie de Couverture (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Qu'appelle-t-on le 'pureau' dans la pose de tuiles ou d'ardoises ?",
                    "answerOptions": [
                        {"text": "La partie de la tuile fixée sur le liteau.", "isCorrect": False},
                        {"text": "La partie visible de la tuile ou de l'ardoise exposée aux intempéries.", "isCorrect": True},
                        {"text": "La distance entre deux liteaux consécutifs.", "isCorrect": False},
                        {"text": "La hauteur totale de la tuile.", "isCorrect": False}
                    ],
                    "correction": "Le **pureau** est la dimension exposée. Il est crucial pour calculer le nombre de matériaux nécessaires au mètre carré et assurer le bon recouvrement."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel terme désigne le croisement rentrant de deux versants d'une toiture ?",
                    "answerOptions": [
                        {"text": "Le Faîtage.", "isCorrect": False},
                        {"text": "L'Arêtier.", "isCorrect": False},
                        {"text": "La Noue.", "isCorrect": True},
                        {"text": "La Rive.", "isCorrect": False}
                    ],
                    "correction": "La **Noue** est le point le plus délicat à traiter en couverture car l'eau y converge et nécessite une étanchéité particulière, souvent en zinguerie."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la principale fonction de l'écran sous-toiture (EST) ?",
                    "answerOptions": [
                        {"text": "Améliorer l'isolation thermique uniquement.", "isCorrect": False},
                        {"text": "Assurer le parement intérieur du comble.", "isCorrect": False},
                        {"text": "Permettre la récupération des eaux de pluie.", "isCorrect": False},
                        {"text": "Contribuer à l'étanchéité à l'eau (neige poudreuse, infiltration) et à l'air, et protéger des poussières.", "isCorrect": True}
                    ],
                    "correction": "L'**Écran Sous-Toiture** (EST) est une membrane de protection qui renforce l'étanchéité, notamment contre la neige poudreuse et le vent."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment appelle-t-on l'élément de charpente horizontal qui supporte les chevrons ?",
                    "answerOptions": [
                        {"text": "Le Liteau.", "isCorrect": False},
                        {"text": "La Panne (faîtière, intermédiaire, sablière).", "isCorrect": True},
                        {"text": "L'Entrait.", "isCorrect": False},
                        {"text": "Le Contre-liteau.", "isCorrect": False}
                    ],
                    "correction": "Les **Pannes** (faîtière en haut, sablière en bas, intermédiaires) sont les pièces maîtresses d'un versant, soutenues par les fermes ou les murs."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel type de pose est principalement utilisé pour les ardoises sur voligeage continu ?",
                    "answerOptions": [
                        {"text": "La pose à joints droits.", "isCorrect": False},
                        {"text": "La pose à lattes.", "isCorrect": False},
                        {"text": "La pose au clou (ou au crochet).", "isCorrect": True},
                        {"text": "La pose à sec.", "isCorrect": False}
                    ],
                    "correction": "L'ardoise est généralement fixée soit par clouage direct sur les liteaux ou voliges, soit par l'utilisation de **crochets** qui se fixent sur les liteaux."
                },
                {
                    "questionNumber": 6,
                    "question": "Que représente la 'Ligne de Faîtage' ?",
                    "answerOptions": [
                        {"text": "L'intersection basse du toit (égout).", "isCorrect": False},
                        {"text": "L'intersection haute et horizontale des deux versants d'un toit.", "isCorrect": True},
                        {"text": "L'intersection inclinée des deux versants.", "isCorrect": False},
                        {"text": "Le bord latéral du toit.", "isCorrect": False}
                    ],
                    "correction": "Le **Faîtage** est la ligne de crête. Il est couvert par des tuiles faîtières ou un closoir ventilé pour assurer l'étanchéité et la ventilation."
                },
                {
                    "questionNumber": 7,
                    "question": "Dans le cas d'une couverture en tuiles, à quoi sert le 'recouvrement' ?",
                    "answerOptions": [
                        {"text": "À faciliter la marche du couvreur.", "isCorrect": False},
                        {"text": "À masquer le pureau.", "isCorrect": False},
                        {"text": "À garantir que l'eau ne pénètre pas dans le comble en s'écoulant sur la tuile inférieure.", "isCorrect": True},
                        {"text": "À fixer la tuile sur le liteau.", "isCorrect": False}
                    ],
                    "correction": "Le **recouvrement** est la partie d'une tuile qui est cachée par la tuile supérieure. Il est essentiel à l'étanchéité et est strictement encadré par les DTU selon la pente et la zone géographique."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est le DTU (Document Technique Unifié) de référence pour la pose des tuiles de terre cuite à emboîtement ou à glissement ?",
                    "answerOptions": [
                        {"text": "DTU 40.21.", "isCorrect": True},
                        {"text": "DTU 40.11.", "isCorrect": False},
                        {"text": "DTU 40.35.", "isCorrect": False},
                        {"text": "DTU 60.1.", "isCorrect": False}
                    ],
                    "correction": "Le **DTU 40.21** concerne les tuiles de terre cuite, le 40.11 les ardoises, et le 40.41 les couvertures en zinc."
                },
                {
                    "questionNumber": 9,
                    "question": "Comment nomme-t-on le dispositif métallique utilisé pour l'évacuation des eaux de pluie en partie basse de toiture ?",
                    "answerOptions": [
                        {"text": "Le Solin.", "isCorrect": False},
                        {"text": "Le Chéneau ou la Gouttière.", "isCorrect": True},
                        {"text": "Le Larmier.", "isCorrect": False},
                        {"text": "Le Brisis.", "isCorrect": False}
                    ],
                    "correction": "Le **Chéneau** est souvent intégré à la maçonnerie ou à la charpente, tandis que la **Gouttière** est un élément suspendu (pendante)."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le rôle des 'contreliteaux' dans le système de couverture ?",
                    "answerOptions": [
                        {"text": "Supporter directement la couverture.", "isCorrect": False},
                        {"text": "Permettre la fixation de l'écran sous-toiture.", "isCorrect": False},
                        {"text": "Créer une lame d'air de ventilation entre l'écran sous-toiture et les liteaux.", "isCorrect": True},
                        {"text": "Décorer le bord du toit.", "isCorrect": False}
                    ],
                    "correction": "Les **contreliteaux** sont posés sur les chevrons (dans le sens de la pente) et les liteaux sont cloués sur eux. Ils créent le vide indispensable à la ventilation de la sous-face de la couverture."
                },
                {
                    "questionNumber": 11,
                    "question": "À quoi sert une 'tuile de ventilation' ou une 'ardoise de ventilation' ?",
                    "answerOptions": [
                        {"text": "À éclairer le comble.", "isCorrect": False},
                        {"text": "À améliorer l'isolation thermique.", "isCorrect": False},
                        {"text": "À éviter la condensation dans le comble et permettre l'évacuation de l'air humide.", "isCorrect": True},
                        {"text": "À empêcher les oiseaux de pénétrer.", "isCorrect": False}
                    ],
                    "correction": "La **ventilation** est vitale pour éviter la dégradation de la charpente (humidité) et de l'isolation (condensation)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la caractéristique principale d'une 'Tuile Canal' (ou romane) ?",
                    "answerOptions": [
                        {"text": "Elle se fixe uniquement par crochets.", "isCorrect": False},
                        {"text": "Elle est plate et s'emboîte de manière mécanique.", "isCorrect": False},
                        {"text": "Elle se compose de deux éléments (le courant et le couvert) et nécessite une très faible pente.", "isCorrect": True},
                        {"text": "Elle est utilisée uniquement pour les toits-terrasses.", "isCorrect": False}
                    ],
                    "correction": "La **Tuile Canal** est typique du Sud de la France. Elle fonctionne par superposition (courant : en dessous, couvert : au-dessus) et est compatible avec les toits à faible pente."
                },
                {
                    "questionNumber": 13,
                    "question": "Qu'est-ce qu'une 'panne sablière' ?",
                    "answerOptions": [
                        {"text": "La panne la plus haute de la toiture.", "isCorrect": False},
                        {"text": "La panne qui se trouve à l'aplomb du mur et reçoit l'égout du toit.", "isCorrect": True},
                        {"text": "Une panne intermédiaire.", "isCorrect": False},
                        {"text": "La pièce qui relie les chevrons.", "isCorrect": False}
                    ],
                    "correction": "La **panne sablière** est la panne inférieure. Elle repose sur le mur et est souvent scellée ou ancrée."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel matériau de couverture est connu pour sa très longue durée de vie (plus de 100 ans) et son excellent aspect esthétique ?",
                    "answerOptions": [
                        {"text": "Les bardeaux bitumés.", "isCorrect": False},
                        {"text": "L'ardoise naturelle.", "isCorrect": True},
                        {"text": "La tôle ondulée en acier.", "isCorrect": False},
                        {"text": "La tuile de béton.", "isCorrect": False}
                    ],
                    "correction": "L'**ardoise naturelle** est très résistante aux cycles de gel/dégel et à la pollution. Elle est très prisée pour son esthétique et sa durabilité."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est le rôle du 'Solin' ?",
                    "answerOptions": [
                        {"text": "Relier deux tuiles.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité au raccordement entre le toit et un élément vertical (mur, cheminée, lucarne).", "isCorrect": True},
                        {"text": "Soutenir la gouttière.", "isCorrect": False},
                        {"text": "Permettre la ventilation.", "isCorrect": False}
                    ],
                    "correction": "Le **Solin** (souvent en zinc ou en mortier) est indispensable pour que l'eau qui coule sur l'élément vertical ne s'infiltre pas dans la toiture."
                },
                {
                    "questionNumber": 16,
                    "question": "Dans le calcul des toitures, qu'est-ce que le 'dévers' ?",
                    "answerOptions": [
                        {"text": "La hauteur totale du toit.", "isCorrect": False},
                        {"text": "L'angle d'inclinaison du toit (pente).", "isCorrect": False},
                        {"text": "L'ensemble des surfaces d'un toit.", "isCorrect": False},
                        {"text": "Le fait que les liteaux ne sont pas parfaitement de niveau (défaut de planéité) ou l'inclinaison des lattes pour le ruissellement.", "isCorrect": True}
                    ],
                    "correction": "Le **dévers** désigne la légère inclinaison latérale des matériaux qui permet à l'eau de s'écouler correctement vers la gouttière."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est la principale différence entre la 'Tuile Plate' et la 'Tuile à Emboîtement' ?",
                    "answerOptions": [
                        {"text": "La Tuile Plate est plus légère.", "isCorrect": False},
                        {"text": "La Tuile Plate repose sur un grand recouvrement pour l'étanchéité, tandis que la Tuile à Emboîtement a des tenons qui s'imbriquent pour un recouvrement réduit.", "isCorrect": True},
                        {"text": "La Tuile Plate est plus facile à poser.", "isCorrect": False},
                        {"text": "La Tuile à Emboîtement est interdite.", "isCorrect": False}
                    ],
                    "correction": "La **Tuile à Emboîtement** (ou mécanique) est plus rapide à poser et nécessite moins de recouvrement, car son étanchéité est en partie assurée par la forme des tenons."
                },
                {
                    "questionNumber": 18,
                    "question": "Comment se nomme la surface d'un toit qui est inclinée ?",
                    "answerOptions": [
                        {"text": "Le Tiers.", "isCorrect": False},
                        {"text": "L'Égout.", "isCorrect": False},
                        {"text": "Le Versant.", "isCorrect": True},
                        {"text": "Le Lucarne.", "isCorrect": False}
                    ],
                    "correction": "Le **Versant** est l'une des faces inclinées de la toiture. Un toit à deux pans a deux versants."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'avantage du 'Voligeage' (planches jointives) par rapport au Liteau (lattes espacées) ?",
                    "answerOptions": [
                        {"text": "Il est moins cher.", "isCorrect": False},
                        {"text": "Il est plus léger.", "isCorrect": False},
                        {"text": "Il offre un support continu, essentiel pour les petites couvertures (zinc, ardoise naturelle) et assure une meilleure rigidité.", "isCorrect": True},
                        {"text": "Il permet une meilleure ventilation.", "isCorrect": False}
                    ],
                    "correction": "Le **Voligeage** est souvent obligatoire pour les couvertures métalliques ou lorsque les matériaux (ardoises) n'ont pas la résistance structurelle des tuiles mécaniques."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est l'unité de mesure de la 'pente' d'un toit en France ?",
                    "answerOptions": [
                        {"text": "Le degré (°).", "isCorrect": False},
                        {"text": "Le pourcent (%).", "isCorrect": True},
                        {"text": "Le radian.", "isCorrect": False},
                        {"text": "La hauteur au faîtage.", "isCorrect": False}
                    ],
                    "correction": "La **pente** est exprimée en **pourcentage (%)** ou en fractions (ex : 40%), qui représente la différence de hauteur sur 100 cm de longueur horizontale."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : ZINGUERIE ET ÉVACUATION DES EAUX (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Zinguerie et Évacuation des Eaux (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel matériau est le plus couramment utilisé pour les travaux de zinguerie (gouttières, chéneaux, abergements) ?",
                    "answerOptions": [
                        {"text": "L'aluminium galvanisé.", "isCorrect": False},
                        {"text": "Le Plomb.", "isCorrect": False},
                        {"text": "Le Zinc (naturel, prépatiné, ou titane).", "isCorrect": True},
                        {"text": "L'acier inoxydable.", "isCorrect": False}
                    ],
                    "correction": "Le **Zinc** est le matériau de zinguerie traditionnel, apprécié pour sa malléabilité, sa durabilité et sa capacité à se patiner (s'auto-protéger)."
                },
                {
                    "questionNumber": 22,
                    "question": "Dans le cas d'une gouttière pendante, comment s'appelle la pièce métallique qui la maintient au chevron ou à la planche de rive ?",
                    "answerOptions": [
                        {"text": "Le Solin.", "isCorrect": False},
                        {"text": "Le Crochet.", "isCorrect": True},
                        {"text": "La Naissance.", "isCorrect": False},
                        {"text": "La Bavette.", "isCorrect": False}
                    ],
                    "correction": "Les **crochets** sont fixés au support (chevrons ou bandeau) et doivent assurer la pente nécessaire à l'écoulement de l'eau dans la gouttière."
                },
                {
                    "questionNumber": 23,
                    "question": "Comment assure-t-on la dilatation des éléments de zinc longs (ex : chéneaux) ?",
                    "answerOptions": [
                        {"text": "En utilisant des soudures continues.", "isCorrect": False},
                        {"text": "En les découpant en petits tronçons de 1 mètre.", "isCorrect": False},
                        {"text": "En prévoyant des joints de dilatation (ou des couvre-joints) et une fixation permettant le mouvement.", "isCorrect": True},
                        {"text": "Par un revêtement spécial.", "isCorrect": False}
                    ],
                    "correction": "Le **Zinc** se dilate et se rétracte beaucoup avec la température. Si la dilatation n'est pas gérée (joints de dilatation), le métal se déchire ou se déforme."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle d'une 'Bande de Rive' ?",
                    "answerOptions": [
                        {"text": "Améliorer l'étanchéité au faîtage.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité et l'esthétique du bord latéral de la toiture (la rive).", "isCorrect": True},
                        {"text": "Servir de support aux tuiles.", "isCorrect": False},
                        {"text": "Protéger la gouttière.", "isCorrect": False}
                    ],
                    "correction": "La **Bande de Rive** peut être en bois ou en métal (zinc) et protège la planche de rive ou les pannes sablières des intempéries sur le côté du toit."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la pièce métallique qui assure la jonction entre le bas de la gouttière et le tube de descente ?",
                    "answerOptions": [
                        {"text": "Le Talon.", "isCorrect": False},
                        {"text": "La Platine.", "isCorrect": False},
                        {"text": "La Naissance (ou Moignon).", "isCorrect": True},
                        {"text": "Le Solin.", "isCorrect": False}
                    ],
                    "correction": "La **Naissance** est l'entonnoir par lequel l'eau du chéneau ou de la gouttière est dirigée vers la conduite de descente."
                },
                {
                    "questionNumber": 26,
                    "question": "Comment s'appelle l'outil manuel utilisé par le zingueur pour plier le zinc sur de courtes longueurs (ou pour pincer des ourlets) ?",
                    "answerOptions": [
                        {"text": "Le Coupe-Franche.", "isCorrect": False},
                        {"text": "Le Marteau de charpentier.", "isCorrect": False},
                        {"text": "La Pince à Tôle ou la Pince à Border.", "isCorrect": True},
                        {"text": "Le Chalumeau.", "isCorrect": False}
                    ],
                    "correction": "La **Pince à Tôle** ou à border permet de réaliser des plis nets et des finitions sur les petites pièces de zinguerie."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est l'inconvénient majeur du 'Plomb' en zinguerie d'abergement (solin) ?",
                    "answerOptions": [
                        {"text": "Il est très difficile à souder.", "isCorrect": False},
                        {"text": "Il est très léger.", "isCorrect": False},
                        {"text": "Il est toxique (plombémie) et sa dilatation/contraction est moins maîtrisée que le zinc.", "isCorrect": True},
                        {"text": "Il rouille très vite.", "isCorrect": False}
                    ],
                    "correction": "Bien qu'il soit très malléable, le **Plomb** est de moins en moins utilisé en construction pour des raisons de santé publique (toxicité)."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la pente minimale recommandée pour un chéneau en zinc afin d'assurer un bon écoulement des eaux ?",
                    "answerOptions": [
                        {"text": "5 % (5 cm par mètre).", "isCorrect": False},
                        {"text": "1 % (1 cm par mètre), ou minimum 5 mm par mètre.", "isCorrect": True},
                        {"text": "0 % (parfaitement horizontal).", "isCorrect": False},
                        {"text": "20 %.", "isCorrect": False}
                    ],
                    "correction": "Une pente d'au moins **5 mm/mètre** est nécessaire pour garantir l'écoulement et éviter la stagnation de l'eau (et le développement de mousses)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le DTU de référence pour les travaux de couverture en Métal (Zinc, Cuivre, Acier) ?",
                    "answerOptions": [
                        {"text": "DTU 40.21.", "isCorrect": False},
                        {"text": "DTU 40.41 (Couvertures par éléments métalliques en feuilles et longues feuilles en zinc, cuivre, acier...).", "isCorrect": True},
                        {"text": "DTU 43.1.", "isCorrect": False},
                        {"text": "DTU 40.35.", "isCorrect": False}
                    ],
                    "correction": "Le **DTU 40.41** est la référence pour tout ce qui concerne la pose du zinc à tasseaux, à joints debouts, ainsi que les chéneaux et gouttières."
                },
                {
                    "questionNumber": 30,
                    "question": "Dans le cas d'une toiture plate, quel système d'étanchéité est le plus couramment utilisé ?",
                    "answerOptions": [
                        {"text": "La couverture en tuiles.", "isCorrect": False},
                        {"text": "L'étanchéité multicouche (bitume armé) ou membrane synthétique (PVC, EPDM).", "isCorrect": True},
                        {"text": "Le voligeage simple.", "isCorrect": False},
                        {"text": "Le bac acier simple.", "isCorrect": False}
                    ],
                    "correction": "Les **membranes bitumineuses** (soudées au chalumeau) ou les **membranes synthétiques** sont indispensables pour les toitures-terrasses, même si celles-ci ont une très faible pente."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment se nomme la technique de raccordement du zinc qui consiste à créer un pli vertical entre deux lés, utilisé sur les toitures à faible pente ?",
                    "answerOptions": [
                        {"text": "Le Solin.", "isCorrect": False},
                        {"text": "La Soudure.", "isCorrect": False},
                        {"text": "Le Joint Debout (ou Agrafage à joint debout).", "isCorrect": True},
                        {"text": "Le Recouvrement Simple.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint Debout** est une méthode d'agrafage mécanique qui permet l'étanchéité sur des pentes très faibles, tout en gérant la dilatation du métal."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'élément qui empêche l'eau de remonter par capillarité sous le bas de la tuile de l'égout ou de la feuille de zinc ?",
                    "answerOptions": [
                        {"text": "Le Clou de fixation.", "isCorrect": False},
                        {"text": "Le Larmier (ou Tête d'égout).", "isCorrect": True},
                        {"text": "Le Crochet.", "isCorrect": False},
                        {"text": "Le Noue.", "isCorrect": False}
                    ],
                    "correction": "Le **Larmier** est un petit pli (ou une bavette) qui force l'eau à se décrocher (à 'larmoyer') avant d'atteindre le support, protégeant ainsi le bandeau de rive."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le métal qui résiste le mieux à l'environnement marin (air salin) en zinguerie ?",
                    "answerOptions": [
                        {"text": "L'acier galvanisé.", "isCorrect": False},
                        {"text": "Le Cuivre.", "isCorrect": True},
                        {"text": "Le Zinc traditionnel.", "isCorrect": False},
                        {"text": "L'Aluminium.", "isCorrect": False}
                    ],
                    "correction": "Le **Cuivre** est l'un des matériaux les plus durables et résistants à la corrosion saline, mais aussi l'un des plus chers."
                },
                {
                    "questionNumber": 34,
                    "question": "Lors d'une soudure à l'étain sur du zinc, quel produit est indispensable pour nettoyer et préparer la surface métallique ?",
                    "answerOptions": [
                        {"text": "L'eau déminéralisée.", "isCorrect": False},
                        {"text": "Le Flux (ou Décapant, souvent à base d'acide).", "isCorrect": True},
                        {"text": "L'acétone.", "isCorrect": False},
                        {"text": "L'huile de lin.", "isCorrect": False}
                    ],
                    "correction": "Le **Flux** (ou décapant) permet de décaper l'oxydation superficielle du zinc, assurant que l'étain 'accroche' correctement au métal pour une soudure étanche."
                },
                {
                    "questionNumber": 35,
                    "question": "Qu'est-ce qu'une 'chatière de ventilation' ?",
                    "answerOptions": [
                        {"text": "Une trappe d'accès pour les chats.", "isCorrect": False},
                        {"text": "Un accessoire de toiture permettant une ventilation localisée et permanente du comble.", "isCorrect": True},
                        {"text": "Une petite fenêtre de toit.", "isCorrect": False},
                        {"text": "Un système de chauffage.", "isCorrect": False}
                    ],
                    "correction": "La **Chatière** est un élément (souvent sous forme de tuile ou de grille) installé en toiture pour assurer la circulation de l'air, en complément des entrées d'air en bas de pente."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le danger d'utiliser des agrafes en acier sur du zinc (ou du cuivre) ?",
                    "answerOptions": [
                        {"text": "Une mauvaise tenue mécanique.", "isCorrect": False},
                        {"text": "Un risque de corrosion par électrolyse (contact de deux métaux différents).", "isCorrect": True},
                        {"text": "Un coût trop élevé.", "isCorrect": False},
                        {"text": "Une couleur inadaptée.", "isCorrect": False}
                    ],
                    "correction": "Il faut éviter le contact entre métaux de potentiels différents (**couple électrolytique**). Pour le zinc, on utilise des fixations en inox ou en cuivre."
                },
                {
                    "questionNumber": 37,
                    "question": "Pour quelle raison la descente d'eau pluviale ne doit-elle pas être collée directement au mur ?",
                    "answerOptions": [
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Pour permettre la dilatation du tuyau et éviter que l'humidité ne pénètre dans le mur.", "isCorrect": True},
                        {"text": "Pour faciliter l'accès aux fenêtres.", "isCorrect": False},
                        {"text": "Pour que la peinture sèche.", "isCorrect": False}
                    ],
                    "correction": "Des **colliers de fixation** sont utilisés pour maintenir la descente à distance du mur, permettant sa dilatation et l'aération entre le tuyau et la façade."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel élément permet d'éviter l'obstruction du tube de descente par les feuilles et débris ?",
                    "answerOptions": [
                        {"text": "Une bavette de rive.", "isCorrect": False},
                        {"text": "Un crapaudine (grille de protection) à la naissance de la descente.", "isCorrect": True},
                        {"text": "Un joint de dilatation.", "isCorrect": False},
                        {"text": "Un solin.", "isCorrect": False}
                    ],
                    "correction": "La **crapaudine** est une petite grille bombée installée dans le trou de naissance pour filtrer les débris volumineux."
                },
                {
                    "questionNumber": 39,
                    "question": "Dans le cas d'une couverture en bac acier, quel est le principal rôle du feutre anti-condensation (ou régulateur de condensation) ?",
                    "answerOptions": [
                        {"text": "Réduire la corrosion.", "isCorrect": False},
                        {"text": "Absorber l'humidité présente sous la tôle et la rejeter à l'extérieur quand la température le permet, évitant les gouttes d'eau.", "isCorrect": True},
                        {"text": "Renforcer la tôle.", "isCorrect": False},
                        {"text": "Améliorer l'isolation phonique.", "isCorrect": False}
                    ],
                    "correction": "Les tôles métalliques condensent facilement. Le **feutre anti-condensation** est essentiel dans les bâtiments non isolés pour prévenir les 'pluies' intérieures."
                },
                {
                    "questionNumber": 40,
                    "question": "La 'Soudure à recouvrement' est-elle autorisée pour les tuiles de terre cuite ?",
                    "answerOptions": [
                        {"text": "Oui, toujours.", "isCorrect": False},
                        {"text": "Oui, mais uniquement pour les tuiles plates.", "isCorrect": False},
                        {"text": "Non, les tuiles sont des éléments de couverture qui s'imbriquent et ne se soudent pas.", "isCorrect": True},
                        {"text": "Oui, mais uniquement au niveau du faîtage.", "isCorrect": False}
                    ],
                    "correction": "Les tuiles ne sont pas soudées, elles s'imbriquent avec un **recouvrement** dimensionné selon la pente et la zone d'exposition."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : SÉCURITÉ, ACCÈS ET NORMES (DTU) (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Sécurité, Accès et Normes (DTU) (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) obligatoire pour tout travail en hauteur au-delà de 3 mètres, en l'absence de protection collective (échafaudage) ?",
                    "answerOptions": [
                        {"text": "Le casque de chantier et les gants.", "isCorrect": False},
                        {"text": "Le harnais de sécurité (antichute) rattaché à un point d'ancrage fixe.", "isCorrect": True},
                        {"text": "Les bottes de sécurité.", "isCorrect": False},
                        {"text": "Les lunettes de protection.", "isCorrect": False}
                    ],
                    "correction": "Le **harnais** est la protection individuelle essentielle pour éviter les chutes lors du travail en toiture, notamment lors de la mise en place de l'échafaudage."
                },
                {
                    "questionNumber": 42,
                    "question": "Que signifie le terme 'Zonage' dans les DTU de couverture ?",
                    "answerOptions": [
                        {"text": "La délimitation de la zone de chantier.", "isCorrect": False},
                        {"text": "La répartition du territoire français en zones de vent et de neige, impactant le calcul du recouvrement et la fixation des matériaux.", "isCorrect": True},
                        {"text": "Le calcul de la surface du toit.", "isCorrect": False},
                        {"text": "La vérification de l'accès au toit.", "isCorrect": False}
                    ],
                    "correction": "Le **Zonage** (Zone 1, 2, 3) est essentiel. Une couverture en zone de vent élevée (ex: bord de mer) exige une fixation plus importante des matériaux."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le risque majeur lié à la manipulation des vieilles plaques de fibrociment avant 1997 ?",
                    "answerOptions": [
                        {"text": "La toxicité du plomb.", "isCorrect": False},
                        {"text": "La présence d'Amiante (risque de cancer par inhalation de fibres).", "isCorrect": True},
                        {"text": "Le risque électrique.", "isCorrect": False},
                        {"text": "Une trop forte chaleur.", "isCorrect": False}
                    ],
                    "correction": "L'**Amiante** est très présent dans les plaques en fibrociment d'avant 1997. Des procédures strictes (EPI, confinement, traçabilité des déchets) doivent être respectées pour la dépose."
                },
                {
                    "questionNumber": 44,
                    "question": "Que doit-on vérifier avant d'utiliser une échelle pour monter en toiture ?",
                    "answerOptions": [
                        {"text": "Qu'elle est de couleur vive.", "isCorrect": False},
                        {"text": "Qu'elle est stabilisée, dépasse d'au moins 1 mètre le point d'accès, et que l'angle d'inclinaison est d'environ 75°.", "isCorrect": True},
                        {"text": "Qu'elle est en bois uniquement.", "isCorrect": False},
                        {"text": "Qu'elle est attachée par une corde à la cheminée.", "isCorrect": False}
                    ],
                    "correction": "L'**angle de 75°** (règle du 4 pour 1 : 4 de hauteur pour 1 de base) est optimal pour la stabilité. Le dépassement de 1 m est pour faciliter la prise en main et la sécurisation du passage sur le toit."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le DTU de référence pour les travaux de Charpente en Bois (assemblages) ?",
                    "answerOptions": [
                        {"text": "DTU 40.11.", "isCorrect": False},
                        {"text": "DTU 31.1.", "isCorrect": True},
                        {"text": "DTU 43.3.", "isCorrect": False},
                        {"text": "DTU 20.1.", "isCorrect": False}
                    ],
                    "correction": "Le **DTU 31.1** concerne les charpentes et escaliers en bois. Le couvreur doit connaître les bases pour évaluer et préparer le support."
                },
                {
                    "questionNumber": 46,
                    "question": "Pour quelle raison un couvreur ne doit-il jamais monter sur une couverture en verre synthétique (type polycarbonate) non supportée ?",
                    "answerOptions": [
                        {"text": "Elle glisse trop.", "isCorrect": False},
                        {"text": "Elle n'est pas faite pour être couverte.", "isCorrect": False},
                        {"text": "Elle ne supporte pas le poids d'un homme et représente un risque de chute par traversée.", "isCorrect": True},
                        {"text": "Elle est trop lourde.", "isCorrect": False}
                    ],
                    "correction": "Les **matériaux légers ou non porteurs** (fibrociment, tôle fine, polycarbonate) nécessitent l'utilisation de planches de répartition de charge (passerelles) pour marcher sans risque."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le rôle du 'Closoir de Faîtage' ?",
                    "answerOptions": [
                        {"text": "Simplement un élément décoratif.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité à l'eau et au vent du faîtage tout en permettant la ventilation de la sous-face de la toiture.", "isCorrect": True},
                        {"text": "Fixer les tuiles de rive.", "isCorrect": False},
                        {"text": "Réduire la dilatation du zinc.", "isCorrect": False}
                    ],
                    "correction": "Le **Closoir** (souvent ventilé et souple) est devenu indispensable. Il remplace le scellement au mortier pour les faîtages, permettant une meilleure durabilité et ventilation."
                },
                {
                    "questionNumber": 48,
                    "question": "Dans quel cas doit-on prévoir un 'pare-vapeur' sous l'isolant dans le comble ?",
                    "answerOptions": [
                        {"text": "Jamais.", "isCorrect": False},
                        {"text": "Uniquement pour l'isolation extérieure.", "isCorrect": False},
                        {"text": "Pour empêcher la vapeur d'eau intérieure (habitation) de migrer dans l'isolant et de condenser.", "isCorrect": True},
                        {"text": "Pour bloquer les insectes.", "isCorrect": False}
                    ],
                    "correction": "Le **pare-vapeur** (ou frein-vapeur) est posé côté chaud (intérieur). Sans lui, la condensation dégrade l'isolant (perte d'efficacité) et la charpente."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel terme désigne la dégradation du bois par un champignon qui mange la cellulose, provoquant un aspect cotonneux et une perte de résistance ?",
                    "answerOptions": [
                        {"text": "Le Vrillette.", "isCorrect": False},
                        {"text": "La Termite.", "isCorrect": False},
                        {"text": "La Mérule.", "isCorrect": True},
                        {"text": "Le Capricorne.", "isCorrect": False}
                    ],
                    "correction": "La **Mérule** est un champignon très dangereux qui dégrade rapidement les charpentes humides. Sa présence doit être signalée immédiatement."
                },
                {
                    "questionNumber": 50,
                    "question": "Pourquoi la bâche ou la mise hors d'eau provisoire est-elle une étape critique du chantier de couverture ?",
                    "answerOptions": [
                        {"text": "Pour ne pas salir les murs.", "isCorrect": False},
                        {"text": "Pour respecter l'esthétique du chantier.", "isCorrect": False},
                        {"text": "Pour prévenir immédiatement les dégâts des eaux (infiltrations) sur la construction ou l'habitation.", "isCorrect": True},
                        {"text": "Pour accélérer les travaux.", "isCorrect": False}
                    ],
                    "correction": "Le couvreur est responsable de l'**intégrité du bâtiment**. Il doit toujours s'assurer qu'en cas d'intempérie (pluie, neige), le toit en cours de réalisation est étanche."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le risque de travailler sur un toit rendu glissant par la pluie ou le gel ?",
                    "answerOptions": [
                        {"text": "Un risque de maladie.", "isCorrect": False},
                        {"text": "Un risque de chute de hauteur accru (glissade).", "isCorrect": True},
                        {"text": "Un risque de perte d'outils.", "isCorrect": False},
                        {"text": "Un risque d'erreur de mesure.", "isCorrect": False}
                    ],
                    "correction": "Le travail en toiture doit être interrompu ou très fortement sécurisé en cas de pluie, gel, vent violent, ou neige. Le risque de chute est multiplié."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la zone du toit la plus sensible à l'action du vent (soulèvement) ?",
                    "answerOptions": [
                        {"text": "Le milieu du versant.", "isCorrect": False},
                        {"text": "Les rives, les faîtages et les arêtiers (périmètre et saillies).", "isCorrect": True},
                        {"text": "La zone près de la noue.", "isCorrect": False},
                        {"text": "Le pied de la cheminée.", "isCorrect": False}
                    ],
                    "correction": "Le **vent** crée une dépression (soulèvement) maximale sur les bords et les angles de la toiture. C'est pourquoi les fixations doivent y être renforcées (DTU)."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle du 'Gardien de corps' sur un échafaudage de pied ?",
                    "answerOptions": [
                        {"text": "Le montant vertical.", "isCorrect": False},
                        {"text": "La partie qui empêche la chute des ouvriers (garde-corps, lisse, sous-lisse et plinthe).", "isCorrect": True},
                        {"text": "La liaison avec le bâtiment.", "isCorrect": False},
                        {"text": "Le système de roue.", "isCorrect": False}
                    ],
                    "correction": "Le **garde-corps** est une protection collective obligatoire contre les chutes de hauteur. Il doit être complet (lisse haute, sous-lisse, plinthe)."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la règle de sécurité fondamentale lors du levage des matériaux en toiture (ex: tuiles, sacs de mortier) ?",
                    "answerOptions": [
                        {"text": "Lever les matériaux à la main.", "isCorrect": False},
                        {"text": "Utiliser un engin de levage vérifié (monte-matériaux) et s'assurer que la charge est stabilisée, ne passe pas au-dessus des ouvriers et que la zone est balisée.", "isCorrect": True},
                        {"text": "Ne jamais lever plus de 10 kg.", "isCorrect": False},
                        {"text": "Lever les matériaux en cas de vent fort.", "isCorrect": False}
                    ],
                    "correction": "Le levage présente un double risque : chute de l'objet (blessure) et surcharge de l'engin (rupture). La **sécurité** passe par l'organisation de la zone."
                },
                {
                    "questionNumber": 55,
                    "question": "Que représente la 'Zone 1' dans le zonage Vent des DTU ?",
                    "answerOptions": [
                        {"text": "La zone la plus exposée au vent.", "isCorrect": False},
                        {"text": "La zone la moins exposée au vent (l'intérieur des terres, les plaines).", "isCorrect": True},
                        {"text": "La zone de montagne.", "isCorrect": False},
                        {"text": "La zone de bord de mer.", "isCorrect": False}
                    ],
                    "correction": "La **Zone 1** est la zone la moins contraignante pour le vent (vitesse de référence la plus faible), ce qui implique des exigences de fixation moindres."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le risque lié à l'utilisation d'un chalumeau pour la soudure du zinc ou l'étanchéité bitumineuse ?",
                    "answerOptions": [
                        {"text": "Le risque de fuite d'eau.", "isCorrect": False},
                        {"text": "Le risque de brûlure et d'incendie de la charpente (point chaud).", "isCorrect": True},
                        {"text": "Le risque électrique.", "isCorrect": False},
                        {"text": "Le risque de soulèvement par le vent.", "isCorrect": False}
                    ],
                    "correction": "Le chalumeau produit une très forte chaleur. Il est essentiel de s'assurer qu'il n'y a pas de matériaux inflammables à proximité et de disposer d'un extincteur."
                },
                {
                    "questionNumber": 57,
                    "question": "Pourquoi le port de lunettes de protection (ou visière) est-il indispensable lors de la découpe de tuiles (à la disqueuse) ?",
                    "answerOptions": [
                        {"text": "Pour éviter le bruit.", "isCorrect": False},
                        {"text": "Pour se protéger des projections de poussière et d'éclats.", "isCorrect": True},
                        {"text": "Pour avoir l'air professionnel.", "isCorrect": False},
                        {"text": "Pour éviter la pluie.", "isCorrect": False}
                    ],
                    "correction": "La découpe de matériaux (tuiles, ardoises) génère des **éclats** dangereux pour les yeux. Les lunettes ou la visière sont obligatoires."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment s'appelle l'outil qui permet de mesurer précisément la pente d'un toit ?",
                    "answerOptions": [
                        {"text": "Le Mètre ruban.", "isCorrect": False},
                        {"text": "Le Niveau laser.", "isCorrect": False},
                        {"text": "Le Décamètre.", "isCorrect": False},
                        {"text": "L'inclinomètre (ou fausse équerre, ou équerre de charpentier spécialisée).", "isCorrect": True}
                    ],
                    "correction": "L'**inclinomètre** donne l'angle ou la pente directement. La pente est un facteur déterminant pour le choix du matériau de couverture et de son recouvrement (DTU)."
                },
                {
                    "questionNumber": 59,
                    "question": "Qu'est-ce qu'une 'échelle à crinoline' ?",
                    "answerOptions": [
                        {"text": "Une échelle souple.", "isCorrect": False},
                        {"text": "Une échelle fixe sécurisée par une enceinte métallique (arceaux) pour la protection contre les chutes.", "isCorrect": True},
                        {"text": "Une échelle en bois.", "isCorrect": False},
                        {"text": "Une échelle articulée.", "isCorrect": False}
                    ],
                    "correction": "L'**échelle à crinoline** est utilisée pour les accès réguliers et sécurisés aux toitures-terrasses ou installations techniques sur de grandes hauteurs."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est l'objectif principal du nettoyage du toit ('démoussage') ?",
                    "answerOptions": [
                        {"text": "Améliorer l'esthétique uniquement.", "isCorrect": False},
                        {"text": "Retirer les mousses et lichens qui retiennent l'humidité et dégradent la porosité des tuiles, réduisant ainsi leur étanchéité et leur résistance au gel.", "isCorrect": True},
                        {"text": "Remplacer les tuiles.", "isCorrect": False},
                        {"text": "Augmenter la dilatation du zinc.", "isCorrect": False}
                    ],
                    "correction": "La **mousse** engendre des dégradations par rétention d'eau et cycles de gel/dégel. Le démoussage prévient les fuites et prolonge la durée de vie du toit."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : TECHNIQUES DE POSE ET RÉPARATIONS (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Techniques de Pose et Réparations (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la technique utilisée pour poser les ardoises qui donne l'effet 'écailles' (bord supérieur arrondi) et utilise un clou par ardoise ?",
                    "answerOptions": [
                        {"text": "La pose à lattes.", "isCorrect": False},
                        {"text": "La pose au clou (ou clouage direct).", "isCorrect": True},
                        {"text": "La pose à claire-voie.", "isCorrect": False},
                        {"text": "La pose d'ardoise d'ornementation.", "isCorrect": False}
                    ],
                    "correction": "Le **clouage direct** est la technique la plus traditionnelle, notamment en régions à fort vent, car elle offre une grande résistance (la fixation est masquée par l'ardoise du rang supérieur)."
                },
                {
                    "questionNumber": 62,
                    "question": "Comment appelle-t-on la méthode de pose qui consiste à utiliser des lattes de bois espacées pour supporter les tuiles (le cas le plus fréquent) ?",
                    "answerOptions": [
                        {"text": "Le Voligeage.", "isCorrect": False},
                        {"text": "Le Chevrons.", "isCorrect": False},
                        {"text": "Le Liteaunage (ou lattage).", "isCorrect": True},
                        {"text": "La Couverture sèche.", "isCorrect": False}
                    ],
                    "correction": "Le **liteaunage** est la pose des lattes de bois (liteaux) sur les chevrons ou contreliteaux. L'espacement correspond au pureau des tuiles."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est l'étape essentielle avant toute pose de liteaux (ou lattage) ?",
                    "answerOptions": [
                        {"text": "La pose des arêtiers.", "isCorrect": False},
                        {"text": "Le Traçage des lignes de pureau et de l'égout.", "isCorrect": True},
                        {"text": "La découpe de toutes les tuiles.", "isCorrect": False},
                        {"text": "Le levage des matériaux.", "isCorrect": False}
                    ],
                    "correction": "Le **traçage** est indispensable pour positionner les liteaux à l'entraxe exact du pureau, garantissant que les tuiles s'alignent et que le recouvrement est respecté sur toute la hauteur."
                },
                {
                    "questionNumber": 64,
                    "question": "Lors du remplacement d'une tuile cassée, quel outil permet de la retirer sans soulever excessivement les tuiles voisines (afin de ne pas les casser) ?",
                    "answerOptions": [
                        {"text": "Un Pied-de-biche.", "isCorrect": False},
                        {"text": "Un Égoïne.", "isCorrect": False},
                        {"text": "Un Crochet d'extraction (ou lève-tuile).", "isCorrect": True},
                        {"text": "Une Cisaille.", "isCorrect": False}
                    ],
                    "correction": "Le **lève-tuile** permet de soulever délicatement les tuiles des rangs supérieurs pour dégager la tuile à remplacer et pour la glisser en place."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est l'inconvénient principal de la pose de tuiles scellées au mortier (traditionnelle) par rapport à la pose sèche ?",
                    "answerOptions": [
                        {"text": "C'est plus rapide.", "isCorrect": False},
                        {"text": "Le mortier peut se fissurer (gel/dégel) et le faîtage/rive n'est pas ventilé, entraînant des risques de condensation.", "isCorrect": True},
                        {"text": "Le coût du mortier est trop faible.", "isCorrect": False},
                        {"text": "Le mortier s'écaille.", "isCorrect": False}
                    ],
                    "correction": "La **pose sèche** (avec closoirs ventilés) est aujourd'hui la norme, car elle offre une meilleure durabilité, résilience aux mouvements et ventilation."
                },
                {
                    "questionNumber": 66,
                    "question": "Lors de la pose des tuiles mécaniques, dans quel sens (horizontal) doit-on progresser ?",
                    "answerOptions": [
                        {"text": "De haut en bas.", "isCorrect": False},
                        {"text": "De bas en haut, et de droite à gauche (pour un droitier, afin de reposer le pied sur les tuiles déjà posées).", "isCorrect": True},
                        {"text": "De gauche à droite, puis de haut en bas.", "isCorrect": False},
                        {"text": "Du centre vers les rives.", "isCorrect": False}
                    ],
                    "correction": "La pose commence à l'égout (bas) pour remonter au faîtage. La progression latérale dépend de la main dominante du couvreur (travailler sur la partie déjà couverte)."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le risque de réaliser des coupes de tuiles à l'intérieur du bâtiment (dans le comble) ?",
                    "answerOptions": [
                        {"text": "Salissure des murs.", "isCorrect": False},
                        {"text": "L'inhalation de poussières de silice (nocives pour les poumons) et le risque d'incendie (étincelles).", "isCorrect": True},
                        {"text": "Un risque de contact avec la charpente.", "isCorrect": False},
                        {"text": "Le bris de la tuile.", "isCorrect": False}
                    ],
                    "correction": "La **découpe** doit toujours être faite à l'extérieur (ou sous aspiration forcée) avec le port d'un masque FFP3 pour se protéger des poussières."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment assure-t-on la fixation des tuiles de faîtage (pièces de finition) ?",
                    "answerOptions": [
                        {"text": "Uniquement par emboîtement.", "isCorrect": False},
                        {"text": "Par des crochets spécifiques, des vis inox et un closoir ventilé (pose sèche).", "isCorrect": True},
                        {"text": "Elles ne sont jamais fixées.", "isCorrect": False},
                        {"text": "Par un simple ruban adhésif.", "isCorrect": False}
                    ],
                    "correction": "Les tuiles de **faîtage** sont les plus exposées au vent et doivent être obligatoirement fixées (mécaniquement), surtout en zone ventée."
                },
                {
                    "questionNumber": 69,
                    "question": "Qu'est-ce qu'une 'Couverture à tasseaux' en zinguerie ?",
                    "answerOptions": [
                        {"text": "Une couverture temporaire.", "isCorrect": False},
                        {"text": "Une technique traditionnelle où les feuilles de zinc sont raccordées par des profilés bois recouverts d'une bande métallique (couvre-joint).", "isCorrect": True},
                        {"text": "Une toiture plate.", "isCorrect": False},
                        {"text": "Une toiture en ardoise.", "isCorrect": False}
                    ],
                    "correction": "La **couverture à tasseaux** est une technique ancienne qui permet l'étanchéité et la dilatation sur les toitures monumentales ou de faible pente. Elle est remplacée par le joint debout pour les toits modernes."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le rôle du 'garde-neige' sur une toiture ?",
                    "answerOptions": [
                        {"text": "Empêcher le vent de s'infiltrer.", "isCorrect": False},
                        {"text": "Empêcher la neige (et la glace) de glisser brutalement du toit (avalanches) et de blesser les passants ou endommager les installations.", "isCorrect": True},
                        {"text": "Réduire le poids de la neige.", "isCorrect": False},
                        {"text": "Isoler la toiture.", "isCorrect": False}
                    ],
                    "correction": "Le **garde-neige** est obligatoire en zone montagneuse ou pour les toitures très exposées au gel, afin de retenir la masse de neige et éviter les accidents."
                },
                {
                    "questionNumber": 71,
                    "question": "Lors de la pose d'une fenêtre de toit (type Vélux), quelle est l'étape essentielle pour l'étanchéité ?",
                    "answerOptions": [
                        {"text": "L'utilisation de vitrage teinté.", "isCorrect": False},
                        {"text": "La pose d'un raccord d'étanchéité spécifique au modèle de tuile (ou ardoise) et au respect des pentes minimales.", "isCorrect": True},
                        {"text": "La fixation du dormant uniquement.", "isCorrect": False},
                        {"text": "La vérification de l'isolation.", "isCorrect": False}
                    ],
                    "correction": "Le **raccord d'étanchéité** (ou 'kit costière') permet de faire la transition entre l'élément vertical de la fenêtre et la couverture inclinée, assurant l'écoulement de l'eau."
                },
                {
                    "questionNumber": 72,
                    "question": "Pour une pose en ardoises au crochet, que représente le 'recouvrement' (R) ?",
                    "answerOptions": [
                        {"text": "La longueur du crochet.", "isCorrect": False},
                        {"text": "La distance entre le bas d'une ardoise et le haut de la troisième ardoise du rang inférieur (la partie non couverte par la 2e ardoise).", "isCorrect": True},
                        {"text": "Le pureau divisé par deux.", "isCorrect": False},
                        {"text": "La largeur de l'ardoise.", "isCorrect": False}
                    ],
                    "correction": "Le **recouvrement** est le calcul le plus important en ardoise, car il garantit que trois épaisseurs d'ardoises sont superposées à chaque point, assurant l'étanchéité."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le risque de poser des tuiles mécaniques sur une pente inférieure à celle autorisée par le fabricant et le DTU ?",
                    "answerOptions": [
                        {"text": "Le soulèvement par le vent.", "isCorrect": False},
                        {"text": "Le matériau sera trop léger.", "isCorrect": False},
                        {"text": "Un risque d'infiltration et de fuite, car l'eau n'aura pas le temps de s'écouler sur le recouvrement (effet de lame d'eau).", "isCorrect": True},
                        {"text": "Une mauvaise isolation.", "isCorrect": False}
                    ],
                    "correction": "La **pente minimale** est une exigence d'étanchéité. Si elle n'est pas respectée, la tuile est moins efficace contre l'eau."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel outil est le plus adapté pour la découpe d'ardoises naturelles (à la main) ?",
                    "answerOptions": [
                        {"text": "La Disqueuse (meuleuse).", "isCorrect": False},
                        {"text": "Le Couteau d'ardoise (ou rogne-ardoise).", "isCorrect": True},
                        {"text": "Le Ciseau à bois.", "isCorrect": False},
                        {"text": "La Scie sauteuse.", "isCorrect": False}
                    ],
                    "correction": "Le **rogne-ardoise** (ou marteau d'ardoise) est l'outil traditionnel du couvreur, qui permet de couper et de percer l'ardoise rapidement et précisément."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le nom de la tuile plate utilisée pour la transition entre la couverture et la planche de rive (bord latéral) ?",
                    "answerOptions": [
                        {"text": "La Tuile chatière.", "isCorrect": False},
                        {"text": "La Tuile de rive (ou demi-tuile de rive).", "isCorrect": True},
                        {"text": "La Tuile faîtière.", "isCorrect": False},
                        {"text": "La Tuile à douille.", "isCorrect": False}
                    ],
                    "correction": "La **Tuile de rive** (ou tuile bordure) est une tuile spécifique qui assure l'étanchéité et la protection des éléments de charpente sur le côté du toit."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment calcule-t-on le nombre de liteaux nécessaires pour un versant ?",
                    "answerOptions": [
                        {"text": "En multipliant la largeur par la longueur du toit.", "isCorrect": False},
                        {"text": "En divisant la longueur de la rampant (en hauteur) par le pureau majoré du recouvrement.", "isCorrect": False},
                        {"text": "En divisant la longueur de la rampant (en hauteur) par le pureau.", "isCorrect": True},
                        {"text": "En multipliant le nombre de chevrons par deux.", "isCorrect": False}
                    ],
                    "correction": "Le nombre de rangées est obtenu par la division de la **hauteur de rampant par le pureau**. Il faut souvent ajuster la ligne de faîtage et d'égout (faux-pureau)."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est la particularité d'une 'Tuile à douille' ?",
                    "answerOptions": [
                        {"text": "Elle permet la ventilation.", "isCorrect": False},
                        {"text": "Elle permet le passage de conduits (ex: antenne, VMC, raccordement de panneau solaire).", "isCorrect": True},
                        {"text": "Elle est plus légère.", "isCorrect": False},
                        {"text": "Elle est utilisée pour le faîtage.", "isCorrect": False}
                    ],
                    "correction": "La **Tuile à douille** est utilisée pour assurer la traversée du toit par un élément technique tout en maintenant l'étanchéité."
                },
                {
                    "questionNumber": 78,
                    "question": "Qu'est-ce qu'une 'Pente minimal' en couverture ?",
                    "answerOptions": [
                        {"text": "La pente maximale autorisée par le DTU.", "isCorrect": False},
                        {"text": "La pente au-dessous de laquelle le système de couverture choisi (matériau et recouvrement) n'est plus étanche.", "isCorrect": True},
                        {"text": "La pente d'un toit-terrasse.", "isCorrect": False},
                        {"text": "La pente la plus esthétique.", "isCorrect": False}
                    ],
                    "correction": "La **pente minimale** est une donnée technique cruciale qui dépend du matériau, du type de pose et de la zone climatique."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est l'élément qui permet la transition étanche entre une noue et les tuiles des deux versants adjacents ?",
                    "answerOptions": [
                        {"text": "Un solin maçonné.", "isCorrect": False},
                        {"text": "Un chéneau de noue (en zinc ou en membrane).", "isCorrect": True},
                        {"text": "Un joint debout.", "isCorrect": False},
                        {"text": "Une tuile canal.", "isCorrect": False}
                    ],
                    "correction": "La **Noue** (angle rentrant) exige une pièce métallique (chéneau de noue) ou une membrane qui récolte l'eau des deux versants avant qu'elle ne rejoigne l'égout."
                },
                {
                    "questionNumber": 80,
                    "question": "En cas de réparation, comment se nomme la technique qui consiste à injecter un produit chimique sur les tuiles pour ralentir le retour des mousses et lichens ?",
                    "answerOptions": [
                        {"text": "L'Hydrofuge.", "isCorrect": True},
                        {"text": "Le Cimentage.", "isCorrect": False},
                        {"text": "Le Décapage.", "isCorrect": False},
                        {"text": "L'Anticorrosion.", "isCorrect": False}
                    ],
                    "correction": "L'**Hydrofuge** (souvent incolore) est un traitement qui pénètre le matériau poreux (tuile de terre cuite, béton) et le rend plus imperméable, limitant la rétention d'eau et la prolifération végétale."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : CHARPENTE, VMC ET ISOLATION (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Charpente, VMC et Isolation (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le rôle du 'chevron' dans la charpente traditionnelle ?",
                    "answerOptions": [
                        {"text": "Soutenir la panne faîtière.", "isCorrect": False},
                        {"text": "Transmettre les charges de la couverture aux pannes (il est posé dans le sens de la pente).", "isCorrect": True},
                        {"text": "Faire la liaison avec le mur.", "isCorrect": False},
                        {"text": "Permettre la fixation des liteaux uniquement.", "isCorrect": False}
                    ],
                    "correction": "Les **chevrons** sont les pièces qui courent des pannes aux pannes (sablière à faîtière). Ils reçoivent les liteaux et sont les premiers éléments à supporter la couverture."
                },
                {
                    "questionNumber": 82,
                    "question": "Qu'est-ce qu'une 'ferme' de charpente ?",
                    "answerOptions": [
                        {"text": "Un petit élément de remplissage.", "isCorrect": False},
                        {"text": "Un élément porteur principal (triangle) qui transmet le poids de la toiture aux murs porteurs.", "isCorrect": True},
                        {"text": "La fixation des tuiles.", "isCorrect": False},
                        {"text": "La partie basse de la toiture.", "isCorrect": False}
                    ],
                    "correction": "La **ferme** est un assemblage de pièces (entrait, arbalétrier, poinçon) qui donne sa forme à la toiture et supporte l'ensemble des pannes."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est le rôle du 'poinçon' dans une ferme traditionnelle ?",
                    "answerOptions": [
                        {"text": "Relier les arbalétriers et les entraits au centre (pièce verticale).", "isCorrect": True},
                        {"text": "Soutenir les chevrons.", "isCorrect": False},
                        {"text": "Former la noue.", "isCorrect": False},
                        {"text": "Fixer les liteaux.", "isCorrect": False}
                    ],
                    "correction": "Le **poinçon** est la pièce centrale verticale de la ferme, souvent couronnée par la panne faîtière."
                },
                {
                    "questionNumber": 84,
                    "question": "Lors de la pose de l'isolant entre chevrons, quelle est la précaution essentielle à prendre concernant l'écran sous-toiture (EST) ?",
                    "answerOptions": [
                        {"text": "L'isoler complètement du soleil.", "isCorrect": False},
                        {"text": "Assurer une lame d'air de ventilation de 2 cm minimum entre l'isolant et l'EST (sauf EST HPV).", "isCorrect": True},
                        {"text": "Le coller directement à l'isolant.", "isCorrect": False},
                        {"text": "L'enlever après la pose de l'isolant.", "isCorrect": False}
                    ],
                    "correction": "Si l'EST n'est pas de type 'Haute Perméabilité à la Vapeur' (HPV), une **lame d'air** doit être ménagée pour l'évacuation de l'humidité du comble."
                },
                {
                    "questionNumber": 85,
                    "question": "Dans le cas d'une couverture en ardoise, quel est le rôle d'un 'Coyau' ?",
                    "answerOptions": [
                        {"text": "Le coyau est un élément décoratif uniquement.", "isCorrect": False},
                        {"text": "C'est une petite pièce de bois ajoutée aux chevrons pour donner une légère courbure (redent) à l'égout, facilitant l'écoulement.", "isCorrect": True},
                        {"text": "C'est un type de liteau.", "isCorrect": False},
                        {"text": "C'est le nom du crochet.", "isCorrect": False}
                    ],
                    "correction": "Le **Coyau** permet de 'redresser' le bas de pente, améliorant l'esthétique et évitant que l'eau ne stagne à l'égout."
                },
                {
                    "questionNumber": 86,
                    "question": "Qu'est-ce qu'une 'VMC' (Ventilation Mécanique Contrôlée) ?",
                    "answerOptions": [
                        {"text": "Un chauffage d'appoint.", "isCorrect": False},
                        {"text": "Un système qui assure le renouvellement permanent de l'air dans le bâtiment.", "isCorrect": True},
                        {"text": "Un système de toiture plate.", "isCorrect": False},
                        {"text": "Un type de tuile.", "isCorrect": False}
                    ],
                    "correction": "Le couvreur doit s'assurer que les sorties de **VMC** (bouches à douille) sont correctement posées et étanches, et que la ventilation générale de la toiture est assurée."
                },
                {
                    "questionNumber": 87,
                    "question": "Lors d'une réparation de charpente, quel type d'attaque du bois doit être traité par injection de produit fongicide et insecticide ?",
                    "answerOptions": [
                        {"text": "L'humidité simple.", "isCorrect": False},
                        {"text": "Les attaques de termites, capricornes et vrillettes (insectes xylophages).", "isCorrect": True},
                        {"text": "Le soulèvement par le vent.", "isCorrect": False},
                        {"text": "L'usure naturelle.", "isCorrect": False}
                    ],
                    "correction": "Les **insectes xylophages** détruisent le bois de l'intérieur. Le traitement (curatif ou préventif) est indispensable pour la pérennité de la structure."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est la caractéristique d'une toiture à 'quatrième pan' ou 'toit en croupe' ?",
                    "answerOptions": [
                        {"text": "Le toit n'a qu'un seul versant.", "isCorrect": False},
                        {"text": "Le toit a deux longs versants et deux versants triangulaires aux extrémités (croupe).", "isCorrect": True},
                        {"text": "Le toit est parfaitement plat.", "isCorrect": False},
                        {"text": "Le toit est formé de quatre noues.", "isCorrect": False}
                    ],
                    "correction": "La **croupe** est une terminaison en triangle. Elle implique la création d'**arêtiers** (angles saillants) à la place des rives droites."
                },
                {
                    "questionNumber": 89,
                    "question": "Que signifie l'acronyme 'HPV' pour un écran sous-toiture ?",
                    "answerOptions": [
                        {"text": "Haute Pression du Vent.", "isCorrect": False},
                        {"text": "Haute Performance Verte.", "isCorrect": False},
                        {"text": "Haute Perméabilité à la Vapeur (sans besoin de lame d'air de ventilation sous l'écran).", "isCorrect": True},
                        {"text": "Hauteur de Pente Validée.", "isCorrect": False}
                    ],
                    "correction": "Les EST de type **HPV** sont très pratiques car ils peuvent être posés directement sur l'isolant (sans lame d'air), simplifiant l'isolation par l'intérieur."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le risque d'installer un conduit de cheminée sans une 'souche' (traversée de toit) correctement maçonnée et abergée ?",
                    "answerOptions": [
                        {"text": "Le vent éteint le feu.", "isCorrect": False},
                        {"text": "Un risque de fuite d'eau, et un risque d'incendie (distance de sécurité non respectée avec la charpente).", "isCorrect": True},
                        {"text": "Le conduit rouille.", "isCorrect": False},
                        {"text": "Le conduit se bouche.", "isCorrect": False}
                    ],
                    "correction": "Le **conduit de cheminée** doit être ignifugé et abergé (solin et bande) pour garantir l'étanchéité et la sécurité incendie."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle est la principale fonction du 'pare-pluie' dans un mur ?",
                    "answerOptions": [
                        {"text": "Maintenir la chaleur.", "isCorrect": False},
                        {"text": "Évacuer l'eau qui pénètre derrière le revêtement extérieur et protéger l'isolant du mur.", "isCorrect": True},
                        {"text": "Accrocher les tuiles.", "isCorrect": False},
                        {"text": "Ventiler le grenier.", "isCorrect": False}
                    ],
                    "correction": "Le **pare-pluie** est une membrane qui joue un rôle similaire à l'écran sous-toiture, mais pour l'enveloppe verticale."
                },
                {
                    "questionNumber": 92,
                    "question": "Qu'est-ce qu'une 'isolation par l'extérieur' (ITE) de toiture ?",
                    "answerOptions": [
                        {"text": "L'isolant est posé entre les chevrons.", "isCorrect": False},
                        {"text": "L'isolant est posé sur les chevrons (méthode Sarking ou équivalent).", "isCorrect": True},
                        {"text": "L'isolant est projeté au sol du comble.", "isCorrect": False},
                        {"text": "L'isolant est collé sous les tuiles.", "isCorrect": False}
                    ],
                    "correction": "L'**ITE** est très efficace. Elle est posée en continu sur les chevrons (méthode **Sarking**) et élimine les ponts thermiques de la charpente."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le rôle du 'fausse-coupe' ou 'décrochement' dans la pose des ardoises au crochet ?",
                    "answerOptions": [
                        {"text": "Gérer la fixation.", "isCorrect": False},
                        {"text": "Assurer l'alignement vertical des joints entre les ardoises (pour garantir la superposition de trois épaisseurs).", "isCorrect": True},
                        {"text": "Réduire le poids.", "isCorrect": False},
                        {"text": "Faciliter le nettoyage.", "isCorrect": False}
                    ],
                    "correction": "Le **décrochement** ou 'fausse-coupe' est l'écartement latéral d'une ardoise par rapport à la verticale, qui doit être rigoureusement respecté."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelles sont les deux charges principales que doit supporter la charpente (hors charges permanentes du bâtiment) ?",
                    "answerOptions": [
                        {"text": "La charge des tuiles et la charge des outils.", "isCorrect": False},
                        {"text": "Les charges climatiques : Poids de la Neige et Effet du Vent (pression/dépression).", "isCorrect": True},
                        {"text": "Le poids du couvreur et de la cheminée.", "isCorrect": False},
                        {"text": "Le poids des gouttières et des fixations.", "isCorrect": False}
                    ],
                    "correction": "Les **charges climatiques** sont réglementées par les DTU Neige et Vent et sont prises en compte dès le calcul de dimensionnement de la charpente."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est l'outil indispensable pour percer les ardoises (pour le clouage) sans les fissurer ?",
                    "answerOptions": [
                        {"text": "La Perceuse à percussion.", "isCorrect": False},
                        {"text": "Le Marteau d'ardoise (avec sa pointe).", "isCorrect": True},
                        {"text": "Le Poinçon standard.", "isCorrect": False},
                        {"text": "Le Pistolet à clous.", "isCorrect": False}
                    ],
                    "correction": "Le **Marteau d'ardoise** est multifonction (couper, percer, clouer). Sa pointe fine permet de créer un trou sans briser l'ardoise."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la distance minimale (dite 'distance au feu') à respecter entre un conduit de cheminée et les éléments en bois de la charpente (DTU 24.1) ?",
                    "answerOptions": [
                        {"text": "10 cm (variable selon le conduit, souvent 16 cm).", "isCorrect": True},
                        {"text": "3 cm.", "isCorrect": False},
                        {"text": "50 cm.", "isCorrect": False},
                        {"text": "La distance n'est pas réglementée.", "isCorrect": False}
                    ],
                    "correction": "La **distance de sécurité** (souvent 16 cm si conduit non isolé) est essentielle pour prévenir l'incendie de la charpente par la chaleur transmise par le conduit."
                },
                {
                    "questionNumber": 97,
                    "question": "Pourquoi les tuiles de rive sont-elles souvent scellées au mortier même en pose sèche ?",
                    "answerOptions": [
                        {"text": "Pour des raisons économiques.", "isCorrect": False},
                        {"text": "Pour assurer une fixation mécanique supérieure au vent et éviter les infiltrations latérales (en complément des tuiles à rabat ou des bandes de rive).", "isCorrect": True},
                        {"text": "Pour améliorer la ventilation.", "isCorrect": False},
                        {"text": "Pour les rendre plus légères.", "isCorrect": False}
                    ],
                    "correction": "Bien que le faîtage se pose de plus en plus souvent à sec, les **rives** restent une zone très exposée où le scellement est souvent préféré ou requis pour la tenue au vent."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le risque de surcharger la toiture avec un stock trop important de tuiles sur une petite zone ?",
                    "answerOptions": [
                        {"text": "Dommages à l'écran sous-toiture uniquement.", "isCorrect": False},
                        {"text": "Un risque de rupture ou de déformation de la charpente (surcharge mécanique ponctuelle).", "isCorrect": True},
                        {"text": "Le soulèvement par le vent.", "isCorrect": False},
                        {"text": "Les tuiles glissent.", "isCorrect": False}
                    ],
                    "correction": "Le **stockage** des matériaux doit être réparti sur le toit et, si possible, le long des murs porteurs (pannes et fermes) pour ne pas dépasser la charge admissible par la charpente."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le rôle du 'pare-oiseau' ou 'peigne d'égout' ?",
                    "answerOptions": [
                        {"text": "Décorer l'égout.", "isCorrect": False},
                        {"text": "Empêcher les oiseaux, rongeurs ou gros insectes de pénétrer sous la toiture (au niveau de l'égout).", "isCorrect": True},
                        {"text": "Améliorer l'écoulement de l'eau.", "isCorrect": False},
                        {"text": "Faciliter le nettoyage.", "isCorrect": False}
                    ],
                    "correction": "Le **pare-oiseau** est une grille (souvent en plastique) placée sous le premier rang de tuiles, qui bouche l'espace sans empêcher la ventilation."
                },
                {
                    "questionNumber": 100,
                    "question": "Lors de la pose des liteaux, quel est le principal défaut à éviter pour garantir la planéité et le bon écoulement ?",
                    "answerOptions": [
                        {"text": "Un espacement trop grand.", "isCorrect": False},
                        {"text": "Une mauvaise horizontalité (niveaux) et des défauts de planéité (pas dans le même plan) des liteaux.", "isCorrect": True},
                        {"text": "Des liteaux trop longs.", "isCorrect": False},
                        {"text": "Des liteaux trop courts.", "isCorrect": False}
                    ],
                    "correction": "La toiture doit être parfaitement **plane** pour que les tuiles ou ardoises reposent correctement et pour que le recouvrement soit efficace partout."
                },
            ]
        }
    }
}

# Exemple d'accès aux données :
# print(quiz_data["title"])
# print(quiz_data["themes"][1]["name"])
# print(quiz_data["themes"][1]["questions"][0]["question"])
# print(quiz_data["themes"][1]["questions"][0]["answerOptions"][1]["isCorrect"])