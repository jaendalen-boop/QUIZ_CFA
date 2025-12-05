# Fichier : quiz_cap_serrurier_metallier_100_CORRIGE.py
# Base de données Python pour un quiz sur le CAP Serrurier-Métallier (100 questions)

quiz_data = {
    "title": "Quiz CAP Serrurier-Métallier : Révisions Complètes (100 Questions)",
    "themes": {
        1: {
            "name": "1. Lecture de Plan et Traçage (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est l'unité de mesure standard utilisée pour les cotations des plans en métallerie ?",
                    "answerOptions": [
                        {"text": "Le centimètre (cm).", "isCorrect": False, "key": "A"},
                        {"text": "Le millimètre (mm).", "isCorrect": True, "key": "B"},
                        {"text": "Le mètre (m).", "isCorrect": False, "key": "C"},
                        {"text": "Le pouce (inch).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le millimètre est l'unité de précision pour les fabrications métalliques."
                },
                {
                    "questionNumber": 2,
                    "question": "Sur un plan, que représente une ligne de trait fin, interrompue par des traits longs et courts (trait mixte) ?",
                    "answerOptions": [
                        {"text": "Une arête vue.", "isCorrect": False, "key": "A"},
                        {"text": "Une arête cachée.", "isCorrect": False, "key": "B"},
                        {"text": "L'Axe de Symétrie (ou axe d'un trou, d'un profilé).", "isCorrect": True, "key": "C"},
                        {"text": "Une ligne de coupe.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Axe de Symétrie est crucial pour le positionnement des perçages."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le rôle du Plan d'ensemble dans la réalisation d'un escalier métallique ?",
                    "answerOptions": [
                        {"text": "Donner les détails de soudure.", "isCorrect": False, "key": "A"},
                        {"text": "Montrer la totalité de l'ouvrage (l'escalier) avec ses dimensions hors-tout et son implantation.", "isCorrect": True, "key": "B"},
                        {"text": "Lister les outils nécessaires.", "isCorrect": False, "key": "C"},
                        {"text": "Indiquer le type d'acier.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Plan d'ensemble donne une vue globale de l'ouvrage."
                },
                {
                    "questionNumber": 4,
                    "question": "Lors du traçage d'un angle droit sur une tôle, quel outil doit être utilisé en complément de la règle pour vérifier la perpendicularité ?",
                    "answerOptions": [
                        {"text": "Le pied à coulisse.", "isCorrect": False, "key": "A"},
                        {"text": "Le compas.", "isCorrect": False, "key": "B"},
                        {"text": "L'Équerre (ou Équerre à combinaison).", "isCorrect": True, "key": "C"},
                        {"text": "Le niveau à bulle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Équerre assure la vérification de l'angle à 90°."
                },
                {
                    "questionNumber": 5,
                    "question": "Comment appelle-t-on l'opération qui consiste à reporter les dimensions d'un plan sur la matière première (tôle ou profilé) ?",
                    "answerOptions": [
                        {"text": "Le cisaillage.", "isCorrect": False, "key": "A"},
                        {"text": "Le soudage.", "isCorrect": False, "key": "B"},
                        {"text": "Le Traçage.", "isCorrect": True, "key": "C"},
                        {"text": "Le pliage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Traçage est la première étape de fabrication."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la fonction principale d'un gabarit dans le traçage et la fabrication ?",
                    "answerOptions": [
                        {"text": "Sonder le métal.", "isCorrect": False, "key": "A"},
                        {"text": "Reproduire avec précision et rapidité une même forme ou une pièce complexe en série.", "isCorrect": True, "key": "B"},
                        {"text": "Mesurer l'épaisseur.", "isCorrect": False, "key": "C"},
                        {"text": "Vérifier la température.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Gabarit assure l'uniformité des pièces et le gain de temps."
                },
                {
                    "questionNumber": 7,
                    "question": "Comment matérialise-t-on l'emplacement exact d'un perçage sur un profilé avant de forer ?",
                    "answerOptions": [
                        {"text": "Avec un marqueur.", "isCorrect": False, "key": "A"},
                        {"text": "Avec la Pointe à Tracer et le Poinçon (ou Poinçonnage) pour créer une marque qui guide le foret.", "isCorrect": True, "key": "B"},
                        {"text": "Avec une craie.", "isCorrect": False, "key": "C"},
                        {"text": "Avec une règle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Poinçonnage évite que le foret ne dévie au démarrage."
                },
                {
                    "questionNumber": 8,
                    "question": "Que représente la cote de référence Zéro (0) sur un plan de niveau ou de façade ?",
                    "answerOptions": [
                        {"text": "Le niveau du sol extérieur.", "isCorrect": False, "key": "A"},
                        {"text": "Le Niveau de Référence (NR), souvent le niveau du sol fini à partir duquel toutes les cotes altimétriques sont mesurées.", "isCorrect": True, "key": "B"},
                        {"text": "La hauteur totale de l'ouvrage.", "isCorrect": False, "key": "C"},
                        {"text": "Le point de soudure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le NR est le point de départ de toutes les hauteurs pour la pose."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel instrument permet de mesurer des dimensions avec une précision allant jusqu'au dixième ou au centième de millimètre ?",
                    "answerOptions": [
                        {"text": "Le mètre ruban.", "isCorrect": False, "key": "A"},
                        {"text": "Le Pied à Coulisse (ou le Micromètre).", "isCorrect": True, "key": "B"},
                        {"text": "L'équerre.", "isCorrect": False, "key": "C"},
                        {"text": "Le rapporteur d'angle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Pied à Coulisse est essentiel pour vérifier les dimensions critiques."
                },
                {
                    "questionNumber": 10,
                    "question": "Dans le traçage sur tôle, quel outil est utilisé pour tracer des arcs de cercle ou reporter des rayons ?",
                    "answerOptions": [
                        {"text": "Le rapporteur.", "isCorrect": False, "key": "A"},
                        {"text": "L'équerre.", "isCorrect": False, "key": "B"},
                        {"text": "Le Compas à pointes sèches.", "isCorrect": True, "key": "C"},
                        {"text": "Le cordeau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Compas permet le traçage de formes courbes."
                },
                {
                    "questionNumber": 11,
                    "question": "Que signifie la mention '$\pm 1 \text{ mm}$' sur une cote ?",
                    "answerOptions": [
                        {"text": "La pièce est trop longue de $1 \text{ mm}$.", "isCorrect": False, "key": "A"},
                        {"text": "La Tolérance : la dimension réelle doit être comprise entre la cote nominale moins $1 \text{ mm}$ et plus $1 \text{ mm}$.", "isCorrect": True, "key": "B"},
                        {"text": "La cote est incertaine.", "isCorrect": False, "key": "C"},
                        {"text": "La pièce sera peinte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Tolérance est la plage de variation acceptable."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le rôle du Plan d'implantation d'un ouvrage (garde-corps, escalier) ?",
                    "answerOptions": [
                        {"text": "Indiquer le poids.", "isCorrect": False, "key": "A"},
                        {"text": "Montrer où et comment l'ouvrage doit être fixé ou encastré dans le gros œuvre en spécifiant les axes et les niveaux.", "isCorrect": True, "key": "B"},
                        {"text": "Indiquer le prix.", "isCorrect": False, "key": "C"},
                        {"text": "Indiquer le type de soudure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Plan d'implantation est essentiel pour la pose sur site."
                },
                {
                    "questionNumber": 13,
                    "question": "Comment représente-t-on une arête cachée (non visible depuis la vue principale) sur un dessin technique ?",
                    "answerOptions": [
                        {"text": "Par un trait continu fin.", "isCorrect": False, "key": "A"},
                        {"text": "Par un trait mixte (axe).", "isCorrect": False, "key": "B"},
                        {"text": "Par un trait interrompu (pointillé).", "isCorrect": True, "key": "C"},
                        {"text": "Par un trait fort.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Trait interrompu permet de comprendre la forme interne de la pièce."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le terme technique pour l'action de chanfreiner une pièce avant soudage ?",
                    "answerOptions": [
                        {"text": "Poncer.", "isCorrect": False, "key": "A"},
                        {"text": "Couper le métal en biais pour créer une surface inclinée (un Biseau) afin de préparer les bords à recevoir le métal d'apport.", "isCorrect": True, "key": "B"},
                        {"text": "Dégraisser.", "isCorrect": False, "key": "C"},
                        {"text": "Peindre.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Chanfrein est indispensable sur les pièces épaisses pour garantir une soudure pénétrante."
                },
                {
                    "questionNumber": 15,
                    "question": "Dans le traçage, à quoi sert le Bleu de traçage ?",
                    "answerOptions": [
                        {"text": "Dégraisser le métal.", "isCorrect": False, "key": "A"},
                        {"text": "Améliorer le contraste : un colorant qui permet de rendre les lignes de traçage plus visibles.", "isCorrect": True, "key": "B"},
                        {"text": "Protéger contre la rouille.", "isCorrect": False, "key": "C"},
                        {"text": "Servir d'isolant.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Bleu de traçage est indispensable pour la précision du marquage."
                },
                {
                    "questionNumber": 16,
                    "question": "Comment appelle-t-on la distance entre l'axe du trou et le bord de la tôle ?",
                    "answerOptions": [
                        {"text": "Le diamètre.", "isCorrect": False, "key": "A"},
                        {"text": "La Distance de Sécurité (ou distance au bord), cruciale pour éviter la rupture de la tôle.", "isCorrect": True, "key": "B"},
                        {"text": "La profondeur.", "isCorrect": False, "key": "C"},
                        {"text": "Le pas.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Distance au Bord doit être suffisante pour que le trou ne fragilise pas la pièce."
                },
                {
                    "questionNumber": 17,
                    "question": "Dans une vue en coupe, que représente le hachurage sur le métal ?",
                    "answerOptions": [
                        {"text": "La partie non coupée.", "isCorrect": False, "key": "A"},
                        {"text": "La Matière Coupée (la partie pleine du profilé traversée par le plan de coupe).", "isCorrect": True, "key": "B"},
                        {"text": "L'air.", "isCorrect": False, "key": "C"},
                        {"text": "Le vide.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Hachures indiquent clairement les contours et la nature de la matière."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est l'objectif du traçage en l'air (ou épure) ?",
                    "answerOptions": [
                        {"text": "Travailler directement sur la pièce.", "isCorrect": False, "key": "A"},
                        {"text": "Créer un dessin à l'échelle $1/1$ pour vérifier les cotes, les angles, et servir de gabarit de montage et de soudage.", "isCorrect": True, "key": "B"},
                        {"text": "Dessiner en perspective.", "isCorrect": False, "key": "C"},
                        {"text": "Calculer le poids.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Épure est une méthode traditionnelle de vérification des assemblages complexes."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel terme technique est utilisé pour désigner la longueur développée d'une tôle qui doit être pliée ?",
                    "answerOptions": [
                        {"text": "La longueur finie.", "isCorrect": False, "key": "A"},
                        {"text": "La côte totale.", "isCorrect": False, "key": "B"},
                        {"text": "La Ligne Neutre (ou développé théorique), en tenant compte du retrait du métal dans le pliage.", "isCorrect": True, "key": "C"},
                        {"text": "La largeur de la tôle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Ligne Neutre est la fibre qui ne subit ni extension ni compression lors du pliage."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel outil permet de mesurer la profondeur d'un alésage ou d'un épaulement ?",
                    "answerOptions": [
                        {"text": "Le mètre ruban.", "isCorrect": False, "key": "A"},
                        {"text": "Le Pied à Coulisse (avec sa jauge de profondeur) ou la Jauge de profondeur.", "isCorrect": True, "key": "B"},
                        {"text": "Le micromètre.", "isCorrect": False, "key": "C"},
                        {"text": "Le compas.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Pied à Coulisse est polyvalent pour les mesures externes, internes et de profondeur."
                },
            ]
        },
        2: {
            "name": "2. Technologie des Matériaux et Profilés (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le matériau principal utilisé par le serrurier-métallier pour la construction de structures et d'ouvrages courants ?",
                    "answerOptions": [
                        {"text": "L'aluminium.", "isCorrect": False, "key": "A"},
                        {"text": "Le Fer et l'Acier (alliage de fer et de carbone).", "isCorrect": True, "key": "B"},
                        {"text": "Le bois.", "isCorrect": False, "key": "C"},
                        {"text": "Le cuivre.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Acier (ex : S235 ou S355) est le matériau de base."
                },
                {
                    "questionNumber": 22,
                    "question": "Que signifie la désignation S235 pour un acier ?",
                    "answerOptions": [
                        {"text": "Son épaisseur est de $235 \text{ mm}$.", "isCorrect": False, "key": "A"},
                        {"text": "Sa Limite Élastique Minimale est de $235 \text{ MPa}$ : c'est sa résistance mécanique avant déformation permanente.", "isCorrect": True, "key": "B"},
                        {"text": "Il est composé de $235$ atomes de carbone.", "isCorrect": False, "key": "C"},
                        {"text": "Il est fabriqué à $235 \text{ degrés}$.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Limite Élastique est l'information clé pour le calcul de structure."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le nom du profilé métallique de section carrée ou rectangulaire, souvent utilisé pour les lisses de garde-corps ou les châssis ?",
                    "answerOptions": [
                        {"text": "Le Poutre HEA.", "isCorrect": False, "key": "A"},
                        {"text": "Le Tube (ou Profilé Creux) Carré ou Rectangulaire (ou TRC/TRR).", "isCorrect": True, "key": "B"},
                        {"text": "Le fer plat.", "isCorrect": False, "key": "C"},
                        {"text": "La cornière.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Tubes sont légers et rigides pour les ossatures."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel traitement de surface est réalisé par immersion dans un bain de zinc en fusion et offre la meilleure protection contre la corrosion de l'acier ?",
                    "answerOptions": [
                        {"text": "La peinture.", "isCorrect": False, "key": "A"},
                        {"text": "La Galvanisation à Chaud.", "isCorrect": True, "key": "B"},
                        {"text": "L'anodisation.", "isCorrect": False, "key": "C"},
                        {"text": "La métallisation.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Galvanisation à Chaud crée une couche de zinc très épaisse et durable."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment appelle-t-on le profilé de section en L (deux ailes perpendiculaires) utilisé pour des cadres ou des renforts d'angle ?",
                    "answerOptions": [
                        {"text": "Le T.", "isCorrect": False, "key": "A"},
                        {"text": "La Cornière.", "isCorrect": True, "key": "B"},
                        {"text": "Le U.", "isCorrect": False, "key": "C"},
                        {"text": "Le I.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Cornière est très polyvalente dans l'assemblage et les renforts."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la principale caractéristique de l'Acier Inoxydable (Inox) par rapport à l'acier carbone ?",
                    "answerOptions": [
                        {"text": "Il est plus léger.", "isCorrect": False, "key": "A"},
                        {"text": "Sa forte résistance à la Corrosion (grâce à l'ajout de chrome et de nickel) et son aspect esthétique.", "isCorrect": True, "key": "B"},
                        {"text": "Il est plus facile à souder.", "isCorrect": False, "key": "C"},
                        {"text": "Il est moins cher.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Inox est utilisé pour les ouvrages extérieurs nécessitant une excellente durabilité."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel type de tôle présente des motifs en relief (larmes ou grains de riz) pour améliorer l'adhérence (ex : plateformes, marches) ?",
                    "answerOptions": [
                        {"text": "La tôle perforée.", "isCorrect": False, "key": "A"},
                        {"text": "La Tôle Larmée (ou Tôle à Plancher).", "isCorrect": True, "key": "B"},
                        {"text": "La tôle galvanisée.", "isCorrect": False, "key": "C"},
                        {"text": "La tôle étirée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Tôle Larmée est antidérapante."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment appelle-t-on la déformation permanente d'un métal au-delà de sa limite élastique (ex : pliage) ?",
                    "answerOptions": [
                        {"text": "La rupture.", "isCorrect": False, "key": "A"},
                        {"text": "La Déformation Plastique.", "isCorrect": True, "key": "B"},
                        {"text": "L'allongement.", "isCorrect": False, "key": "C"},
                        {"text": "La fragilité.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Déformation Plastique est recherchée lors du formage."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel profilé est couramment utilisé comme limon d'escalier ou comme poteau dans une structure de petite charpente ?",
                    "answerOptions": [
                        {"text": "Le fer plat.", "isCorrect": False, "key": "A"},
                        {"text": "Le Poutrelle IPE ou HEA (profilés en I ou en H).", "isCorrect": True, "key": "B"},
                        {"text": "Le tube rond.", "isCorrect": False, "key": "C"},
                        {"text": "Le rond plein.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Poutrelles offrent une grande résistance à la flexion."
                },
                {
                    "questionNumber": 30,
                    "question": "Que représente le symbole Ra suivi d'un nombre (ex : Ra 3.2) sur un plan ?",
                    "answerOptions": [
                        {"text": "La résistance de l'acier.", "isCorrect": False, "key": "A"},
                        {"text": "L'État de Surface : la rugosité moyenne de la pièce (important pour les finitions).", "isCorrect": True, "key": "B"},
                        {"text": "La dureté du métal.", "isCorrect": False, "key": "C"},
                        {"text": "Le rayon de pliage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'État de Surface définit si la pièce doit être laissée brute, meulée, ou rectifiée."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment appelle-t-on le phénomène de rétrécissement du métal après soudage, qui peut entraîner des déformations de la structure ?",
                    "answerOptions": [
                        {"text": "La flexion.", "isCorrect": False, "key": "A"},
                        {"text": "Le Retrait (ou Rétraction) dû à la Chaleur.", "isCorrect": True, "key": "B"},
                        {"text": "La dilatation.", "isCorrect": False, "key": "C"},
                        {"text": "Le flambage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Retrait est compensé par un bridage ou un pré-cambrage des pièces."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est l'épaisseur minimale que doit posséder un fer plat pour être considéré comme une platine de fixation structurelle ?",
                    "answerOptions": [
                        {"text": "Moins de $1 \text{ mm}$.", "isCorrect": False, "key": "A"},
                        {"text": "Elle dépend du calcul, mais en général, $6 \text{ à } 10 \text{ mm}$ minimum.", "isCorrect": True, "key": "B"},
                        {"text": "Plus de $50 \text{ mm}$.", "isCorrect": False, "key": "C"},
                        {"text": "Elle n'a pas d'importance.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Platines sont les interfaces entre l'acier et le gros œuvre ; elles doivent être rigides."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le principal inconvénient de l'aluminium par rapport à l'acier dans la construction métallique ?",
                    "answerOptions": [
                        {"text": "Il rouille.", "isCorrect": False, "key": "A"},
                        {"text": "Sa Faible Rigidité et Résistance Mécanique (en particulier à la chaleur et à l'incendie), bien qu'il soit plus léger et résistant à la corrosion.", "isCorrect": True, "key": "B"},
                        {"text": "Il est plus lourd.", "isCorrect": False, "key": "C"},
                        {"text": "Il est plus difficile à peindre.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Aluminium est léger mais moins résistant aux efforts structuraux que l'acier."
                },
                {
                    "questionNumber": 34,
                    "question": "Comment appelle-t-on l'opération qui consiste à enlever l'ébarbure (le morfil) des bords d'une tôle après la découpe ?",
                    "answerOptions": [
                        {"text": "Le polissage.", "isCorrect": False, "key": "A"},
                        {"text": "L'Ébavurage (souvent réalisé à la meuleuse, à la lime ou à la ponceuse).", "isCorrect": True, "key": "B"},
                        {"text": "Le cisaillage.", "isCorrect": False, "key": "C"},
                        {"text": "Le traçage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Ébavurage est une opération de sécurité et de préparation."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel type d'acier est préconisé pour des ouvrages nécessitant des efforts dynamiques importants (ex : pièces de machine, véhicules) ?",
                    "answerOptions": [
                        {"text": "Le S235.", "isCorrect": False, "key": "A"},
                        {"text": "Les Aciers à haute Limite Élastique (ex : S355 et au-delà), plus résistants.", "isCorrect": True, "key": "B"},
                        {"text": "L'Inox.", "isCorrect": False, "key": "C"},
                        {"text": "Le Fer forgé.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La résistance aux chocs et aux déformations est augmentée par la limite élastique."
                },
                {
                    "questionNumber": 36,
                    "question": "Que signifie le terme Passivation dans le traitement de l'acier inoxydable ?",
                    "answerOptions": [
                        {"text": "Le rendre plus souple.", "isCorrect": False, "key": "A"},
                        {"text": "Créer une couche protectrice naturelle d'oxyde de chrome sur la surface du métal, assurant sa résistance à la corrosion.", "isCorrect": True, "key": "B"},
                        {"text": "Le rendre plus brillant.", "isCorrect": False, "key": "C"},
                        {"text": "Le rendre mat.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Passivation est la raison de la résistance à la rouille de l'inox."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'outil utilisé pour mesurer l'épaisseur de tôle avec une très grande précision (au centième de millimètre) ?",
                    "answerOptions": [
                        {"text": "Le mètre ruban.", "isCorrect": False, "key": "A"},
                        {"text": "Le pied à coulisse.", "isCorrect": False, "key": "B"},
                        {"text": "Le Micromètre (ou palmer).", "isCorrect": True, "key": "C"},
                        {"text": "Le rapporteur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Micromètre est l'outil de mesure de précision par excellence."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment appelle-t-on le profilé rond, non creux, souvent utilisé pour les barreaux de garde-corps ou pour le ferrage ?",
                    "answerOptions": [
                        {"text": "Le tube.", "isCorrect": False, "key": "A"},
                        {"text": "Le U.", "isCorrect": False, "key": "B"},
                        {"text": "Le Rond Plein.", "isCorrect": True, "key": "C"},
                        {"text": "Le fer plat.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Rond Plein est très résistant et facile à forger."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le risque de souder une tôle trop fine avec une intensité trop élevée ?",
                    "answerOptions": [
                        {"text": "Une soudure trop résistante.", "isCorrect": False, "key": "A"},
                        {"text": "Le Perçage (ou Pénétration Totale) de la tôle, formant un trou ou un cordon de soudure dégradé.", "isCorrect": True, "key": "B"},
                        {"text": "Un retrait trop important.", "isCorrect": False, "key": "C"},
                        {"text": "Une couleur incorrecte.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Intensité du poste est toujours ajustée à l'épaisseur de la pièce."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel profilé métallique est caractérisé par une section en U et est souvent utilisé pour les rails, les renforts de rive ou les platelages ?",
                    "answerOptions": [
                        {"text": "La cornière.", "isCorrect": False, "key": "A"},
                        {"text": "Le tube carré.", "isCorrect": False, "key": "B"},
                        {"text": "Le UPN (ou UPE, profilés en U).", "isCorrect": True, "key": "C"},
                        {"text": "Le fer plat.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le UPN est très courant dans les structures légères et le renforcement."
                },
            ]
        },
        3: {
            "name": "3. Procédés de Fabrication (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est l'outil principal utilisé pour la coupe droite de tôle mince (jusqu'à $6 \text{ mm}$ d'épaisseur) de manière rapide et propre ?",
                    "answerOptions": [
                        {"text": "Le chalumeau.", "isCorrect": False, "key": "A"},
                        {"text": "La Cisaille (Guillotine ou Cisaille à levier).", "isCorrect": True, "key": "B"},
                        {"text": "La meuleuse.", "isCorrect": False, "key": "C"},
                        {"text": "Le poste plasma.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Cisaille permet une coupe nette et rapide."
                },
                {
                    "questionNumber": 42,
                    "question": "Comment appelle-t-on l'opération qui consiste à enlever de la matière (copeaux) pour former un trou ou un lamage ?",
                    "answerOptions": [
                        {"text": "Le traçage.", "isCorrect": False, "key": "A"},
                        {"text": "L'Usinage (Perçage, Alésage, Taraudage).", "isCorrect": True, "key": "B"},
                        {"text": "Le cisaillage.", "isCorrect": False, "key": "C"},
                        {"text": "Le pliage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Usinage regroupe toutes les techniques d'enlèvement de matière."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le rôle du Lubrifiant (Huile de Coupe) lors du perçage de l'acier ?",
                    "answerOptions": [
                        {"text": "Nettoyer la pièce.", "isCorrect": False, "key": "A"},
                        {"text": "Refroidir l'outil et la pièce et faciliter l'évacuation des copeaux.", "isCorrect": True, "key": "B"},
                        {"text": "Rendre l'outil plus résistant.", "isCorrect": False, "key": "C"},
                        {"text": "Réduire la vitesse de coupe.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Lubrifiant est essentiel pour la durée de vie de l'outil et la qualité du perçage."
                },
                {
                    "questionNumber": 44,
                    "question": "Comment appelle-t-on le procédé qui permet de créer un filetage interne dans un trou (pour y visser un boulon) ?",
                    "answerOptions": [
                        {"text": "L'alésage.", "isCorrect": False, "key": "A"},
                        {"text": "Le Taraudage.", "isCorrect": True, "key": "B"},
                        {"text": "Le fraisage.", "isCorrect": False, "key": "C"},
                        {"text": "Le perçage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Taraudage nécessite de percer un trou d'un diamètre légèrement inférieur."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle machine utilise une matrice (V) et un poinçon pour déformer le métal sur un angle précis ?",
                    "answerOptions": [
                        {"text": "La rouleuse.", "isCorrect": False, "key": "A"},
                        {"text": "La cisaille.", "isCorrect": False, "key": "B"},
                        {"text": "La Presse-Plieuse (ou Plieuse à commande numérique).", "isCorrect": True, "key": "C"},
                        {"text": "La poinçonneuse.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Presse-Plieuse est la machine de base de la chaudronnerie et de la métallerie."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est l'outil utilisé pour couper des profilés épais (poutrelles, cornières) de manière précise et en angle (coupe d'onglet) ?",
                    "answerOptions": [
                        {"text": "La cisaille.", "isCorrect": False, "key": "A"},
                        {"text": "La Scie à Ruban (ou la Scie alternative).", "isCorrect": True, "key": "B"},
                        {"text": "Le chalumeau.", "isCorrect": False, "key": "C"},
                        {"text": "La meuleuse.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Scie à Ruban est l'outil d'atelier pour les coupes de profilés."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on l'opération qui consiste à couper un profilé selon un angle oblique (pour l'assemblage d'un cadre à $90^\circ$ ou $45^\circ$) ?",
                    "answerOptions": [
                        {"text": "La coupe droite.", "isCorrect": False, "key": "A"},
                        {"text": "La Coupe d'Onglet.", "isCorrect": True, "key": "B"},
                        {"text": "Le cisaillage.", "isCorrect": False, "key": "C"},
                        {"text": "Le tronçonnage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Coupe d'Onglet est essentielle pour les cadres de porte, fenêtre ou portail."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'outil utilisé pour créer des trous de grand diamètre dans la tôle, en travaillant par enlèvement de matière autour du bord ?",
                    "answerOptions": [
                        {"text": "Le foret simple.", "isCorrect": False, "key": "A"},
                        {"text": "La scie sauteuse.", "isCorrect": False, "key": "B"},
                        {"text": "La Scie Cloche ou la Mèche à étager.", "isCorrect": True, "key": "C"},
                        {"text": "Le poinçon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Scie Cloche est idéale pour les grands diamètres (ex : passage de gaines)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel procédé de fabrication est utilisé pour rouler une tôle plane en une forme cylindrique ou conique (ex : tube, cuve) ?",
                    "answerOptions": [
                        {"text": "Le pliage.", "isCorrect": False, "key": "A"},
                        {"text": "Le Roulage (ou Cintrâge à trois/quatre rouleaux).", "isCorrect": True, "key": "B"},
                        {"text": "Le poinçonnage.", "isCorrect": False, "key": "C"},
                        {"text": "Le formage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Roulage est utilisé pour les ouvrages courbes."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le rôle de la Rainure de Matrice (le V) sur une presse-plieuse ?",
                    "answerOptions": [
                        {"text": "Accrocher le métal.", "isCorrect": False, "key": "A"},
                        {"text": "Déterminer l'angle de pliage et la zone de déformation du métal. La largeur du V est choisie en fonction de l'épaisseur de la tôle.", "isCorrect": True, "key": "B"},
                        {"text": "Refroidir la tôle.", "isCorrect": False, "key": "C"},
                        {"text": "Maintenir la tôle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Matrice est la partie basse de l'outil de pliage."
                },
                {
                    "questionNumber": 51,
                    "question": "Comment appelle-t-on l'opération qui consiste à donner une forme conique ou évasée à l'entrée d'un trou (pour y loger une tête de vis fraisée) ?",
                    "answerOptions": [
                        {"text": "Le perçage.", "isCorrect": False, "key": "A"},
                        {"text": "Le Fraisage (ou Chambrage).", "isCorrect": True, "key": "B"},
                        {"text": "L'alésage.", "isCorrect": False, "key": "C"},
                        {"text": "Le taraudage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Fraisage permet d'avoir la tête de vis affleurante avec la surface."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le risque de percer l'acier sans utiliser un poinçon au préalable ?",
                    "answerOptions": [
                        {"text": "Le foret se casse.", "isCorrect": False, "key": "A"},
                        {"text": "Le Glissement (ou déviation) du foret à cause d'un mauvais centrage, ce qui rend le trou imprécis.", "isCorrect": True, "key": "B"},
                        {"text": "Le trou est trop petit.", "isCorrect": False, "key": "C"},
                        {"text": "Le métal rouille.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Poinçon crée un point d'amorçage précis pour le foret."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle de la Poinçonneuse-Cisaille (ou Poinçonneuse-Cintrage) ?",
                    "answerOptions": [
                        {"text": "Souder des pièces.", "isCorrect": False, "key": "A"},
                        {"text": "Réaliser simultanément des opérations de Poinçonnage (trous) et de Cisaillage (coupe) sur des tôles et profilés, permettant une fabrication rapide.", "isCorrect": True, "key": "B"},
                        {"text": "Plier des tôles.", "isCorrect": False, "key": "C"},
                        {"text": "Nettoyer des soudures.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Poinçonneuse-Cisaille est une machine polyvalente d'atelier."
                },
                {
                    "questionNumber": 54,
                    "question": "Comment appelle-t-on l'outil utilisé pour couper des profilés creux (tubes) en suivant un contour courbe (préparation avant soudage d'un tube sur un autre) ?",
                    "answerOptions": [
                        {"text": "La tronçonneuse.", "isCorrect": False, "key": "A"},
                        {"text": "Le chalumeau.", "isCorrect": False, "key": "B"},
                        {"text": "La Grignoteuse ou la Scie à contour (travail de 'coupe de poisson').", "isCorrect": True, "key": "C"},
                        {"text": "Le TIG.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Coupe de Poisson est la coupe spécifique des tubes pour qu'ils s'emboîtent parfaitement."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le risque de ne pas nettoyer et dégraisser une pièce avant de la souder ?",
                    "answerOptions": [
                        {"text": "La soudure est trop brillante.", "isCorrect": False, "key": "A"},
                        {"text": "Le Défaut de Pénétration et la Porosité du cordon de soudure, car l'huile et la rouille empêchent le métal d'apport de s'allier correctement.", "isCorrect": True, "key": "B"},
                        {"text": "La pièce se refroidit trop vite.", "isCorrect": False, "key": "C"},
                        {"text": "Le retrait est trop faible.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Propreté des bords à souder est la base d'une soudure de qualité."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle technique de coupe utilise un arc électrique confiné et très chaud pour vaporiser le métal (souvent pour la tôle) ?",
                    "answerOptions": [
                        {"text": "Le chalumeau oxycoupeur.", "isCorrect": False, "key": "A"},
                        {"text": "La Découpe Plasma.", "isCorrect": True, "key": "B"},
                        {"text": "La scie à métaux.", "isCorrect": False, "key": "C"},
                        {"text": "Le TIG.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Découpe Plasma est rapide et permet des formes complexes."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment s'appelle l'outil utilisé pour enlever le métal en excès (cordon de soudure trop épais, bavure) avant la finition (ponçage) ?",
                    "answerOptions": [
                        {"text": "Le burin.", "isCorrect": False, "key": "A"},
                        {"text": "La Meuleuse d'Angle (avec disque ébarbeur) ou la Tronçonneuse de chantier.", "isCorrect": True, "key": "B"},
                        {"text": "Le marteau.", "isCorrect": False, "key": "C"},
                        {"text": "Le cintreur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Ébarbage à la meuleuse est courant après soudage."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est l'objectif du Roulage de bord (ou de la bordure) sur une tôle (ex : dessus de table ou de plan de travail) ?",
                    "answerOptions": [
                        {"text": "Faciliter le pliage.", "isCorrect": False, "key": "A"},
                        {"text": "Améliorer la rigidité et la sécurité (éviter les arêtes vives) de l'ouvrage.", "isCorrect": True, "key": "B"},
                        {"text": "Réduire la corrosion.", "isCorrect": False, "key": "C"},
                        {"text": "Faciliter le traçage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Roulage de bord crée une finition propre et sécurisée."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel procédé de mise en forme est utilisé par le Forgeron-Serrurier pour déformer le métal à chaud (ex : volutes, pointes de lance) ?",
                    "answerOptions": [
                        {"text": "Le pliage à froid.", "isCorrect": False, "key": "A"},
                        {"text": "Le Forgeage et le Cintrâge à Chaud (Travail du Fer Forgé).", "isCorrect": True, "key": "B"},
                        {"text": "Le soudage MIG en série.", "isCorrect": False, "key": "C"},
                        {"text": "La découpe laser.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Forgeage permet de donner des formes complexes et esthétiques au métal."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle est la règle de sécurité à respecter lors de l'utilisation d'une perceuse à colonne ?",
                    "answerOptions": [
                        {"text": "Laisser la pièce libre.", "isCorrect": False, "key": "A"},
                        {"text": "Toujours brider (serrer) solidement la pièce sur la table de la machine pour éviter qu'elle ne s'arrache et ne blesse l'opérateur.", "isCorrect": True, "key": "B"},
                        {"text": "Ne pas utiliser d'huile.", "isCorrect": False, "key": "C"},
                        {"text": "Travailler très vite.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Bridage est une mesure de sécurité essentielle lors du perçage."
                },
            ]
        },
        4: {
            "name": "4. Soudage et Assemblages Fixes (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le procédé de soudage le plus couramment utilisé en atelier pour l'assemblage de pièces métalliques, utilisant un fil continu et un gaz de protection (MIG/MAG) ?",
                    "answerOptions": [
                        {"text": "Le TIG (Tungsten Inert Gas).", "isCorrect": False, "key": "A"},
                        {"text": "Le MIG/MAG (Metal Inert/Active Gas).", "isCorrect": True, "key": "B"},
                        {"text": "Le soudage à l'arc à électrode enrobée (MMA).", "isCorrect": False, "key": "C"},
                        {"text": "Le soudage autogène.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le MIG/MAG est rapide, productif et polyvalent."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le rôle du Gaz de Protection (ex : Argon ou $\text{Argon}+\text{CO}_2$) dans le soudage MIG/MAG et TIG ?",
                    "answerOptions": [
                        {"text": "Accélérer la soudure.", "isCorrect": False, "key": "A"},
                        {"text": "Protéger le métal d'apport et le bain de fusion de l'oxydation et de la contamination par l'air.", "isCorrect": True, "key": "B"},
                        {"text": "Refroidir la torche.", "isCorrect": False, "key": "C"},
                        {"text": "Nettoyer la pièce.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Protection Gazeuse est essentielle pour obtenir un cordon de soudure sain."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on le type de soudure réalisé sans métal d'apport (le plus souvent en TIG sur tôle mince ou inox) ?",
                    "answerOptions": [
                        {"text": "Le soudage MAG.", "isCorrect": False, "key": "A"},
                        {"text": "Le Soudage Autogène.", "isCorrect": True, "key": "B"},
                        {"text": "Le soudage à l'arc.", "isCorrect": False, "key": "C"},
                        {"text": "Le soudage par points.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Soudage Autogène utilise uniquement la fusion des bords des pièces à assembler."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel EPI est absolument obligatoire pour le soudeur afin de protéger ses yeux et son visage de l'arc électrique et des UV/IR ?",
                    "answerOptions": [
                        {"text": "Le casque anti-bruit.", "isCorrect": False, "key": "A"},
                        {"text": "Le Masque (ou Casque) de Soudage à Oculaires Filtrants (passifs ou automatiques).", "isCorrect": True, "key": "B"},
                        {"text": "Les gants fins.", "isCorrect": False, "key": "C"},
                        {"text": "Les lunettes de soleil.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Protection de la Vue est essentielle pour éviter l'ophtalmie (coup d'arc) et les brûlures graves."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la principale différence entre le soudage TIG et le MIG/MAG ?",
                    "answerOptions": [
                        {"text": "Le TIG est plus rapide.", "isCorrect": False, "key": "A"},
                        {"text": "Le TIG est plus lent et plus précis, utilisant une électrode de Tungstène non consommable (idéal pour l'inox et les faibles épaisseurs).", "isCorrect": True, "key": "B"},
                        {"text": "Le TIG utilise plus de gaz.", "isCorrect": False, "key": "C"},
                        {"text": "Le MIG/MAG n'utilise pas de métal d'apport.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le TIG offre la meilleure qualité de finition mais est moins productif que le MAG."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on le type d'assemblage non soudé, réalisé par des vis, des boulons ou des rivets, qui permet un démontage ultérieur ?",
                    "answerOptions": [
                        {"text": "L'assemblage permanent.", "isCorrect": False, "key": "A"},
                        {"text": "L'Assemblage Démontable (ou Assemblage Mécanique).", "isCorrect": True, "key": "B"},
                        {"text": "L'assemblage par collage.", "isCorrect": False, "key": "C"},
                        {"text": "L'assemblage par encastrement.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Assemblages Boulonnés sont souvent utilisés pour les structures livrées en kit."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la fonction d'un Pointage (ou point de soudure) ?",
                    "answerOptions": [
                        {"text": "Réaliser la soudure définitive.", "isCorrect": False, "key": "A"},
                        {"text": "Maintenir temporairement les pièces en position et garantir l'alignement et la géométrie de l'assemblage avant de souder complètement.", "isCorrect": True, "key": "B"},
                        {"text": "Nettoyer la pièce.", "isCorrect": False, "key": "C"},
                        {"text": "Plier le métal.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Pointage est une étape essentielle pour éviter les déformations dues au retrait."
                },
                {
                    "questionNumber": 68,
                    "question": "Qu'est-ce qu'un Rivet Pop (ou Rivet Aveugle) ?",
                    "answerOptions": [
                        {"text": "Un type de soudure.", "isCorrect": False, "key": "A"},
                        {"text": "Un Système d'Assemblage Rapide et Démontable, utilisé souvent pour fixer des tôles fines dans des zones d'accès limité.", "isCorrect": True, "key": "B"},
                        {"text": "Un type de boulon.", "isCorrect": False, "key": "C"},
                        {"text": "Un écrou de serrage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Rivet Pop est posé avec une pince à riveter."
                },
                {
                    "questionNumber": 69,
                    "question": "Que représente le symbole d'un triangle ($\Delta$) sur une ligne de référence de soudage ?",
                    "answerOptions": [
                        {"text": "La position de la soudure.", "isCorrect": False, "key": "A"},
                        {"text": "Un Cordon de Soudure d'Angle (le plus courant, utilisé pour les assemblages en T, à recouvrement ou en angle).", "isCorrect": True, "key": "B"},
                        {"text": "Le type de préparation.", "isCorrect": False, "key": "C"},
                        {"text": "La longueur de la soudure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Triangle indique la soudure d'angle ; un V indique une soudure bout à bout avec chanfrein."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment appelle-t-on la couche de résidus (oxydes, silicates) qui se forme à la surface du cordon de soudure à l'arc à électrode enrobée (MMA) et qu'il faut enlever ?",
                    "answerOptions": [
                        {"text": "Le lait.", "isCorrect": False, "key": "A"},
                        {"text": "Le Laitier (ou Scorie), enlevé avec un marteau à piquer et une brosse métallique.", "isCorrect": True, "key": "B"},
                        {"text": "La rouille.", "isCorrect": False, "key": "C"},
                        {"text": "Le TIG.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Laitier protège la soudure pendant son refroidissement mais doit être retiré."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est la principale fonction d'une Entretoise dans un assemblage (ex : entre deux lisses de garde-corps) ?",
                    "answerOptions": [
                        {"text": "Lier les pièces.", "isCorrect": False, "key": "A"},
                        {"text": "Maintenir un écartement précis et constant entre deux éléments parallèles et garantir la rigidité latérale de l'ouvrage.", "isCorrect": True, "key": "B"},
                        {"text": "Servir de décoration.", "isCorrect": False, "key": "C"},
                        {"text": "Faciliter le soudage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Entretoise est un élément d'espacement et de rigidité."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le risque si la vitesse de soudage est trop rapide en MAG ?",
                    "answerOptions": [
                        {"text": "Un retrait excessif.", "isCorrect": False, "key": "A"},
                        {"text": "Un Manque de Pénétration (le cordon n'est qu'en surface) et une forme de cordon irrégulière.", "isCorrect": True, "key": "B"},
                        {"text": "Un excès de pénétration.", "isCorrect": False, "key": "C"},
                        {"text": "Un trou dans la tôle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Une Vitesse Lente est nécessaire pour que le bain de fusion ait le temps de pénétrer la racine."
                },
                {
                    "questionNumber": 73,
                    "question": "Comment appelle-t-on le procédé d'assemblage qui utilise la chaleur par friction (sans arc électrique) pour lier le métal (ex : soudure de goujons) ?",
                    "answerOptions": [
                        {"text": "Le soudage par points.", "isCorrect": False, "key": "A"},
                        {"text": "Le MIG.", "isCorrect": False, "key": "B"},
                        {"text": "Le Soudage par Friction (ou par résistance).", "isCorrect": True, "key": "C"},
                        {"text": "Le soudage TIG.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Soudage par Friction est courant pour la pose de goujons filetés sur tôle mince."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle est la fonction d'une Rondelle Frein (ou rondelle grower) dans un assemblage boulonné ?",
                    "answerOptions": [
                        {"text": "Répartir l'effort.", "isCorrect": False, "key": "A"},
                        {"text": "Empêcher le dévissage accidentel du boulon ou de l'écrou sous l'effet des vibrations.", "isCorrect": True, "key": "B"},
                        {"text": "Faciliter le serrage.", "isCorrect": False, "key": "C"},
                        {"text": "Rendre l'assemblage étanche.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Freinage est crucial pour la sécurité des ouvrages sous contrainte."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est l'outil utilisé pour enlever l'oxydation (la 'calamine') et les impuretés avant le soudage ou avant l'application d'une peinture ?",
                    "answerOptions": [
                        {"text": "Le chiffon.", "isCorrect": False, "key": "A"},
                        {"text": "La Brosse Métallique (ou le Disque à lamelles) monté sur meuleuse ou perceuse.", "isCorrect": True, "key": "B"},
                        {"text": "La brosse à dents.", "isCorrect": False, "key": "C"},
                        {"text": "La pointe à tracer.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Brossage (ou décapage) est une préparation de surface essentielle."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment appelle-t-on la déformation de la soudure (renflement, goutte) en dessous de la surface de la pièce soudée ?",
                    "answerOptions": [
                        {"text": "Le cordon.", "isCorrect": False, "key": "A"},
                        {"text": "La Pénétration (ou L'Envers de Cordon).", "isCorrect": True, "key": "B"},
                        {"text": "Le retrait.", "isCorrect": False, "key": "C"},
                        {"text": "La porosité.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Pénétration est la profondeur à laquelle le métal d'apport s'est allié à la racine du joint."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est la principale caractéristique d'une vis autoforeuse ?",
                    "answerOptions": [
                        {"text": "Elle ne rouille pas.", "isCorrect": False, "key": "A"},
                        {"text": "Elle perce elle-même le trou de réception dans la tôle mince (souvent utilisée pour la fixation de bardage ou de tôles de couverture).", "isCorrect": True, "key": "B"},
                        {"text": "Elle est démontable.", "isCorrect": False, "key": "C"},
                        {"text": "Elle est très résistante.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Vis Autoforeuse permet un gain de temps considérable sur la pose."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le risque de laisser un mouillage (angle de contact) trop faible sur un cordon de soudure d'angle ?",
                    "answerOptions": [
                        {"text": "Le cordon est trop lisse.", "isCorrect": False, "key": "A"},
                        {"text": "Le Manque de Fusion sur les Bords : le cordon se détache ou présente une faiblesse à la racine, réduisant la résistance mécanique du joint.", "isCorrect": True, "key": "B"},
                        {"text": "Le cordon est trop large.", "isCorrect": False, "key": "C"},
                        {"text": "Le gaz est insuffisant.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Mouillage est la fusion des bords de la tôle par le métal d'apport."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment appelle-t-on l'opération qui consiste à insérer un boulon dans un trou non aligné ou trop petit, souvent à l'aide d'une broche ?",
                    "answerOptions": [
                        {"text": "Le bridage.", "isCorrect": False, "key": "A"},
                        {"text": "Le Mèche à Aléser (ou Broche de Reprise) pour aligner les trous de deux pièces avant de passer le boulon.", "isCorrect": True, "key": "B"},
                        {"text": "Le chanfrein.", "isCorrect": False, "key": "C"},
                        {"text": "Le serrage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Alésage est une opération de rectification de la position des trous."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le type de soudure utilisé pour les assemblages de pièces épaisses nécessitant une pénétration totale ?",
                    "answerOptions": [
                        {"text": "La soudure d'angle.", "isCorrect": False, "key": "A"},
                        {"text": "La Soudure Bout à Bout (avec chanfrein en V ou en U) réalisée en plusieurs passes.", "isCorrect": True, "key": "B"},
                        {"text": "Le pointage.", "isCorrect": False, "key": "C"},
                        {"text": "Le rechargement.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Soudure Bout à Bout est la plus résistante, car elle permet une pénétration maximale."
                },
            ]
        },
        5: {
            "name": "5. Santé, Sécurité et Réglementation (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) indispensable pour prévenir les blessures graves aux pieds (chute de charge, perforation) ?",
                    "answerOptions": [
                        {"text": "Les baskets.", "isCorrect": False, "key": "A"},
                        {"text": "Les Chaussures de Sécurité (coque de protection et semelle anti-perforation) S3.", "isCorrect": True, "key": "B"},
                        {"text": "Les bottes en caoutchouc.", "isCorrect": False, "key": "C"},
                        {"text": "Les sandales.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Chaussures S3 sont la norme pour le BTP et la métallerie."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le risque principal lié à l'utilisation de la meuleuse d'angle (disque à tronçonner/ébarbeur) ?",
                    "answerOptions": [
                        {"text": "Le bruit.", "isCorrect": False, "key": "A"},
                        {"text": "La Projection de fragments (étincelles, métal chaud) et la Rupture du Disque (doit être monté et protégé correctement).", "isCorrect": True, "key": "B"},
                        {"text": "La corrosion.", "isCorrect": False, "key": "C"},
                        {"text": "Le froid.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Meuleuse est l'outil le plus accidentogène ; le port de EPI est crucial."
                },
                {
                    "questionNumber": 83,
                    "question": "Pourquoi doit-on obligatoirement utiliser un extracteur de fumées ou travailler en extérieur lors du soudage ?",
                    "answerOptions": [
                        {"text": "Pour le confort.", "isCorrect": False, "key": "A"},
                        {"text": "Les Fumées de Soudage contiennent des particules et des gaz toxiques (oxydes de métaux lourds, ozone, CO) qui sont cancérogènes et irritants pour les poumons.", "isCorrect": True, "key": "B"},
                        {"text": "Pour éviter le retrait.", "isCorrect": False, "key": "C"},
                        {"text": "Pour un meilleur cordon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Ventilation/Aspiration est essentielle pour la santé du soudeur."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le risque lié à l'utilisation d'une presse-plieuse ou d'une cisaille ?",
                    "answerOptions": [
                        {"text": "Le bruit.", "isCorrect": False, "key": "A"},
                        {"text": "L'Écrasement et la Cisaille des Mains par les outils ; les machines doivent être équipées de barrières immatérielles ou de protections.", "isCorrect": True, "key": "B"},
                        {"text": "Le choc électrique.", "isCorrect": False, "key": "C"},
                        {"text": "La projection.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Risque Mécanique (coupure, écrasement) est très élevé sur les machines à commande."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment sécurise-t-on un poste de travail en hauteur (sur une plateforme ou un échafaudage) ?",
                    "answerOptions": [
                        {"text": "Avec une échelle.", "isCorrect": False, "key": "A"},
                        {"text": "Par la mise en place de Protections Collectives (garde-corps complets) ou de Harnais (protection individuelle) si la protection collective est impossible.", "isCorrect": True, "key": "B"},
                        {"text": "En attachant l'outil.", "isCorrect": False, "key": "C"},
                        {"text": "En travaillant vite.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Protection Collective est toujours prioritaire sur la Protection Individuelle (harnais)."
                },
                {
                    "questionNumber": 86,
                    "question": "Que signifie le marquage NF sur un produit ou un équipement de serrurerie ?",
                    "answerOptions": [
                        {"text": "Nouveau Format.", "isCorrect": False, "key": "A"},
                        {"text": "Norme Française : atteste que le produit ou service est conforme aux normes de qualité, de sécurité et de fiabilité définies en France.", "isCorrect": True, "key": "B"},
                        {"text": "Non Fonctionnel.", "isCorrect": False, "key": "C"},
                        {"text": "Notice Fournie.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Norme NF est un gage de qualité et de conformité."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la règle de sécurité à respecter lors de la manutention d'une charge lourde (ex : poutre métallique) ?",
                    "answerOptions": [
                        {"text": "Soulever seul.", "isCorrect": False, "key": "A"},
                        {"text": "Utiliser des Moyens Mécaniques Appropriés (chariot élévateur, grue, palan) ou travailler à plusieurs pour respecter les limites de charge individuelle (PRAP).", "isCorrect": True, "key": "B"},
                        {"text": "Utiliser de l'huile.", "isCorrect": False, "key": "C"},
                        {"text": "Travailler sans gants.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'utilisation de la Mécanique (ou de l'assistance humaine) prévient les TMS."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel EPI est conseillé lors de la manipulation de pièces fraîchement découpées ou de fers à béton (risque de coupure) ?",
                    "answerOptions": [
                        {"text": "Le casque.", "isCorrect": False, "key": "A"},
                        {"text": "Les Gants de Protection Anti-Coupure (norme EN 388).", "isCorrect": True, "key": "B"},
                        {"text": "Les bouchons d'oreille.", "isCorrect": False, "key": "C"},
                        {"text": "Le gilet jaune.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Gants anti-coupure sont essentiels pour manipuler les bords vifs."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la distance de sécurité minimale entre le poste de soudage et tout matériau inflammable (cartons, bois, solvants) ?",
                    "answerOptions": [
                        {"text": "10 cm.", "isCorrect": False, "key": "A"},
                        {"text": "Au moins $5 \text{ mètres}$ (ou protection par écran anti-feu) pour éviter le départ de feu par les projections de métal en fusion (étincelles).", "isCorrect": True, "key": "B"},
                        {"text": "50 cm.", "isCorrect": False, "key": "C"},
                        {"text": "1 mètre.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Risque Incendie est majeur en soudage ; les consignes de sécurité sont très strictes."
                },
                {
                    "questionNumber": 90,
                    "question": "Que signifie le sigle A2P (Assurance Prévention Protection) pour une serrure ?",
                    "answerOptions": [
                        {"text": "Acier à $2$ Passages.", "isCorrect": False, "key": "A"},
                        {"text": "Certification de Résistance à l'Effraction : plus le nombre d'étoiles est élevé, plus la serrure résiste longtemps à une tentative d'ouverture par la force.", "isCorrect": True, "key": "B"},
                        {"text": "Aluminium $2$ Pièces.", "isCorrect": False, "key": "C"},
                        {"text": "Axe $2$ Pênes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Certification A2P est un élément clé de la serrurerie de sécurité."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le risque de laisser des bouteilles de gaz de soudage (Argon, $\text{O}_2$) debout sans chaînette ou support ?",
                    "answerOptions": [
                        {"text": "Fuite de gaz.", "isCorrect": False, "key": "A"},
                        {"text": "La Chute de la Bouteille qui peut casser le robinet, entraînant la projection violente de la bouteille (effet de roquette) et un risque mortel.", "isCorrect": True, "key": "B"},
                        {"text": "Explosion.", "isCorrect": False, "key": "C"},
                        {"text": "Corrosion.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Bouteilles de Gaz doivent toujours être solidement chaînées ou rangées dans un râtelier."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le EPI essentiel à porter lors de travaux bruyants (meulage intensif, découpe plasma) ?",
                    "answerOptions": [
                        {"text": "Les lunettes.", "isCorrect": False, "key": "A"},
                        {"text": "Les Protections Auditives (Bouchons d'oreille ou Casque anti-bruit) pour prévenir la surdité professionnelle.", "isCorrect": True, "key": "B"},
                        {"text": "Le gilet jaune.", "isCorrect": False, "key": "C"},
                        {"text": "Le masque P3.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Protection Auditive est obligatoire au-delà de $80 \text{ dB}$."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment doit être stocké le matériau découpé (profilés) en atelier ?",
                    "answerOptions": [
                        {"text": "Empilé n'importe comment.", "isCorrect": False, "key": "A"},
                        {"text": "Rangés par Type et Longueur dans des râteliers métalliques appropriés, afin d'éviter les chutes et de faciliter l'accès et l'inventaire.", "isCorrect": True, "key": "B"},
                        {"text": "Au milieu de l'atelier.", "isCorrect": False, "key": "C"},
                        {"text": "À l'extérieur sans protection.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Rangement est un facteur de productivité et de sécurité."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle du DTU (Document Technique Unifié) dans la pose d'ouvrages métalliques ?",
                    "answerOptions": [
                        {"text": "Déterminer le prix.", "isCorrect": False, "key": "A"},
                        {"text": "Définir les Règles de l'Art pour la conception, la fabrication et la pose, notamment les tolérances, les fixations et les types d'acier à utiliser.", "isCorrect": True, "key": "B"},
                        {"text": "Créer le plan.", "isCorrect": False, "key": "C"},
                        {"text": "Déterminer la couleur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le respect des DTU garantit la solidité et la conformité aux normes."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la principale mesure de prévention contre l'incendie en atelier de métallerie ?",
                    "answerOptions": [
                        {"text": "Ne pas souder.", "isCorrect": False, "key": "A"},
                        {"text": "Avoir des extincteurs appropriés (Poudre ABC), bien rangés, accessibles, vérifiés, et isoler toute source de chaleur des matériaux combustibles.", "isCorrect": True, "key": "B"},
                        {"text": "Aérer l'atelier.", "isCorrect": False, "key": "C"},
                        {"text": "Travailler la nuit.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Contrôle du feu (extincteurs et isolation) est primordial."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment doit être rangé le chiffon imbibé d'huile ou de solvant après le nettoyage des pièces ?",
                    "answerOptions": [
                        {"text": "Jeté par terre.", "isCorrect": False, "key": "A"},
                        {"text": "Placé dans un conteneur métallique fermé (boîte hermétique) pour éviter tout risque d'auto-combustion ou de départ de feu.", "isCorrect": True, "key": "B"},
                        {"text": "Jeté dans la poubelle normale.", "isCorrect": False, "key": "C"},
                        {"text": "Lavé.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les chiffons gras sont des déchets dangereux avec un risque d'Auto-Combustion."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque de manipuler des pièces d'acier inoxydable (Inox) avec des outils ayant servi à de l'acier carbone ?",
                    "answerOptions": [
                        {"text": "La pièce est moins brillante.", "isCorrect": False, "key": "A"},
                        {"text": "La Contamination par des Particules d'Acier Carbone qui vont créer des points de rouille (rouille superficielle) sur l'inox. Il faut utiliser des outils et des brosses spécifiques à l'inox.", "isCorrect": True, "key": "B"},
                        {"text": "La pièce est plus lourde.", "isCorrect": False, "key": "C"},
                        {"text": "Le soudage est impossible.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Risque de Contamination est la première cause de corrosion de l'inox."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le principal danger lié à l'utilisation du chalumeau oxycoupeur (coupe au gaz) ?",
                    "answerOptions": [
                        {"text": "Le froid.", "isCorrect": False, "key": "A"},
                        {"text": "L'Explosion des bouteilles de gaz ($\text{O}_2$, Acétylène) et le risque de brûlures graves dues à la projection de métal en fusion (étincelles, laitier).", "isCorrect": True, "key": "B"},
                        {"text": "Le bruit.", "isCorrect": False, "key": "C"},
                        {"text": "La fumée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Oxycoupage nécessite une formation spécifique et le respect des règles de raccordement des bouteilles."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment appelle-t-on le document qui liste tous les risques du chantier et les mesures de prévention (obligatoire pour les gros chantiers) ?",
                    "answerOptions": [
                        {"text": "Le DTU.", "isCorrect": False, "key": "A"},
                        {"text": "Le PPSPS (Plan Particulier de Sécurité et de Protection de la Santé).", "isCorrect": True, "key": "B"},
                        {"text": "Le plan d'ensemble.", "isCorrect": False, "key": "C"},
                        {"text": "Le permis de construire.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le PPSPS organise la sécurité collective sur les chantiers."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la principale précaution à prendre lors de l'utilisation d'une échelle ?",
                    "answerOptions": [
                        {"text": "La laisser libre.", "isCorrect": False, "key": "A"},
                        {"text": "L'Échelle doit être solidement calée ou fixée en haut et en bas, et doit dépasser l'appui supérieur d'au moins $1 \text{ mètre}$ ($3$ barreaux).", "isCorrect": True, "key": "B"},
                        {"text": "Utiliser un seul pied.", "isCorrect": False, "key": "C"},
                        {"text": "Monter avec les outils à la main.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Échelle est un poste de travail provisoire et doit être sécurisée pour prévenir la chute."
                },
            ]
        }
    }
}