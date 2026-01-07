quiz_data = {
    "title": "Quiz CAP Métallier (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : LECTURE DE PLANS, DESSIN TECHNIQUE ET SYMBOLES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : LECTURE DE PLANS, DESSIN TECHNIQUE ET SYMBOLES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel type de trait est utilisé pour représenter les arêtes et contours vus d'une pièce ?",
                    "answerOptions": [
                        {"text": "Continu fort", "isCorrect": True},
                        {"text": "Interrompu court fin", "isCorrect": False},
                        {"text": "Mixte fin à deux tirets", "isCorrect": False},
                        {"text": "Continu fin à main levée", "isCorrect": False}
                    ],
                    "correction": "Le trait continu fort (épaisseur 0,5 ou 0,7 mm) est normalisé pour représenter tout ce qui est visible sur la pièce (contours et arêtes)."
                },
                {
                    "questionNumber": 2,
                    "question": "Que signifie l'indication 'Échelle 1:10' inscrite dans le cartouche d'un plan ?",
                    "answerOptions": [
                        {"text": "Réduction", "isCorrect": True},
                        {"text": "Agrandissement", "isCorrect": False},
                        {"text": "Vraie grandeur", "isCorrect": False},
                        {"text": "Échelle naturelle", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1:10 indique que 1 cm sur le dessin représente 10 cm dans la réalité. C'est donc une réduction car le dessin est plus petit que l'objet réel."
                },
                {
                    "questionNumber": 3,
                    "question": "Dans la méthode de projection européenne, où se place la vue de gauche par rapport à la vue de face ?",
                    "answerOptions": [
                        {"text": "À droite", "isCorrect": True},
                        {"text": "À gauche", "isCorrect": False},
                        {"text": "Au-dessus", "isCorrect": False},
                        {"text": "En dessous", "isCorrect": False}
                    ],
                    "correction": "En projection européenne, la vue est placée à l'opposé de la direction d'observation. Si on regarde la pièce depuis la gauche, on dessine ce qu'on voit à droite de la vue de face."
                },
                {
                    "questionNumber": 4,
                    "question": "Sur un symbole de soudure, que désigne la lettre 'a' placée devant la dimension ?",
                    "answerOptions": [
                        {"text": "Gorge", "isCorrect": True},
                        {"text": "Longueur", "isCorrect": False},
                        {"text": "Pénétration", "isCorrect": False},
                        {"text": "Espacement", "isCorrect": False}
                    ],
                    "correction": "La lettre 'a' désigne l'épaisseur de gorge nominale d'une soudure d'angle, qui est la hauteur du plus grand triangle isocèle inscriptible dans la section."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la différence fondamentale entre une coupe et une section ?",
                    "answerOptions": [
                        {"text": "La coupe montre l'arrière-plan", "isCorrect": True},
                        {"text": "La section représente toujours la totalité de la pièce coupée avec tous les détails cachés", "isCorrect": False},
                        {"text": "La section dessine impérativement les contours situés en arrière du plan de coupe", "isCorrect": False},
                        {"text": "La section projette l'intégralité du volume de la pièce situé derrière le plan de sécante", "isCorrect": False}
                    ],
                    "correction": "Une coupe montre la surface coupée + ce qu'on voit en arrière-plan. Une section ne représente que la partie de la matière située dans le plan de coupe."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel symbole graphique représente une soudure effectuée 'sur tout le pourtour' de la pièce ?",
                    "answerOptions": [
                        {"text": "Cercle", "isCorrect": True},
                        {"text": "Drapeau", "isCorrect": False},
                        {"text": "Triangle", "isCorrect": False},
                        {"text": "Carré", "isCorrect": False}
                    ],
                    "correction": "Un petit cercle situé à l'intersection de la ligne de référence et de la ligne de flèche indique que la soudure doit être réalisée sur tout le périmètre."
                },
                {
                    "questionNumber": 7,
                    "question": "Les hachures sur un dessin technique servent principalement à :",
                    "answerOptions": [
                        {"text": "Identifier la matière coupée", "isCorrect": True},
                        {"text": "Indiquer les zones de soudure à effectuer", "isCorrect": False},
                        {"text": "Décorer le dessin pour le rendre lisible", "isCorrect": False},
                        {"text": "Représenter les surfaces peintes ou vernies", "isCorrect": False}
                    ],
                    "correction": "Les hachures matérialisent les zones où la matière a été 'sciée' par le plan de coupe imaginaire. Leur motif peut indiquer le type de matériau (ex: traits parallèles pour les métaux)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel format de papier correspond à une feuille A4 pliée en deux ?",
                    "answerOptions": [
                        {"text": "A5", "isCorrect": True},
                        {"text": "A3", "isCorrect": False},
                        {"text": "A2", "isCorrect": False},
                        {"text": "A1", "isCorrect": False}
                    ],
                    "correction": "Un A4 (210x297) plié en deux donne un A5 (148x210)."
                },
                {
                    "questionNumber": 9,
                    "question": "Sur une ligne de cote, quel élément se termine par des flèches ?",
                    "answerOptions": [
                        {"text": "Ligne de cote", "isCorrect": True},
                        {"text": "Ligne d'attache", "isCorrect": False},
                        {"text": "Ligne de repère", "isCorrect": False},
                        {"text": "Ligne d'extension", "isCorrect": False}
                    ],
                    "correction": "La ligne de cote est la ligne (droite ou courbe) parallèle à la dimension à mesurer, qui porte les flèches à ses extrémités."
                },
                {
                    "questionNumber": 10,
                    "question": "Que représente un trait mixte fin (trait long, point, trait long) ?",
                    "answerOptions": [
                        {"text": "Axes de symétrie", "isCorrect": True},
                        {"text": "Arêtes cachées", "isCorrect": False},
                        {"text": "Contours vus", "isCorrect": False},
                        {"text": "Limites de rupture", "isCorrect": False}
                    ],
                    "correction": "Le trait mixte fin est utilisé pour matérialiser les axes de symétrie, les plans de symétrie et les trajectoires."
                },
                {
                    "questionNumber": 11,
                    "question": "Dans un assemblage boulonné représenté en coupe, les vis et les écrous pleins sont-ils hachurés ?",
                    "answerOptions": [
                        {"text": "Jamais", "isCorrect": True},
                        {"text": "Toujours", "isCorrect": False},
                        {"text": "Parfois", "isCorrect": False},
                        {"text": "Souvent", "isCorrect": False}
                    ],
                    "correction": "C'est une règle conventionnelle absolue : on ne hachure jamais les pièces pleines normalisées (vis, écrous, rivets, billes) ni les nervures lorsqu'elles sont coupées dans le sens de la longueur."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la fonction du 'cartouche' sur un plan technique ?",
                    "answerOptions": [
                        {"text": "Identifier le document", "isCorrect": True},
                        {"text": "Dessiner la perspective", "isCorrect": False},
                        {"text": "Calculer le poids total", "isCorrect": False},
                        {"text": "Lister les outils nécessaires", "isCorrect": False}
                    ],
                    "correction": "Le cartouche est la carte d'identité du plan. Il contient le titre, l'échelle, le nom du dessinateur, la date et le numéro du plan."
                },
                {
                    "questionNumber": 13,
                    "question": "Si une cote de 50 mm est inscrite sur un plan à l'échelle 1:2, quelle est la longueur réelle de la pièce ?",
                    "answerOptions": [
                        {"text": "50 mm", "isCorrect": True},
                        {"text": "100 mm", "isCorrect": False},
                        {"text": "25 mm", "isCorrect": False},
                        {"text": "200 mm", "isCorrect": False}
                    ],
                    "correction": "La cote inscrite (chiffre) indique TOUJOURS la dimension réelle de la pièce (valeur nominale), quelle que soit l'échelle du dessin."
                },
                {
                    "questionNumber": 14,
                    "question": "Que signifie le symbole d'un 'drapeau' sur la ligne de repère d'une soudure ?",
                    "answerOptions": [
                        {"text": "Soudure chantier", "isCorrect": True},
                        {"text": "Soudure périphérique", "isCorrect": False},
                        {"text": "Soudure meulée", "isCorrect": False},
                        {"text": "Soudure bouchon", "isCorrect": False}
                    ],
                    "correction": "Le petit drapeau signale que l'opération de soudage ne se fait pas en atelier mais directement sur le lieu de montage (chantier)."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel terme désigne une vue qui représente une partie limitée de la pièce à une échelle agrandie pour montrer un détail ?",
                    "answerOptions": [
                        {"text": "Vue de détail", "isCorrect": True},
                        {"text": "Vue auxiliaire", "isCorrect": False},
                        {"text": "Vue locale", "isCorrect": False},
                        {"text": "Vue interrompue", "isCorrect": False}
                    ],
                    "correction": "La vue de détail est une représentation à part, souvent agrandie (zoom), d'une zone complexe de la pièce, repérée par un cercle et une lettre sur la vue principale."
                },
                {
                    "questionNumber": 16,
                    "question": "En cotation, comment appelle-t-on les lignes fines perpendiculaires à la ligne de cote qui délimitent la dimension ?",
                    "answerOptions": [
                        {"text": "Lignes d'attache", "isCorrect": True},
                        {"text": "Lignes de rappel", "isCorrect": False},
                        {"text": "Lignes de mesure", "isCorrect": False},
                        {"text": "Lignes d'extension", "isCorrect": False}
                    ],
                    "correction": "Les lignes d'attache partent du contour de la pièce et servent de butées aux extrémités de la ligne de cote."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle indication donne une tolérance dimensionnelle écrite '20 ± 0,1' ?",
                    "answerOptions": [
                        {"text": "Intervalle", "isCorrect": True},
                        {"text": "Ajustement", "isCorrect": False},
                        {"text": "Rugosité", "isCorrect": False},
                        {"text": "Planéité", "isCorrect": False}
                    ],
                    "correction": "Cela définit un intervalle de tolérance. La pièce est conforme si sa mesure réelle est comprise entre 19,9 mm et 20,1 mm."
                },
                {
                    "questionNumber": 18,
                    "question": "Dans une représentation graphique normalisée, si la réponse A doit être expliquée longuement, quelle règle s'applique souvent aux mauvaises réponses pour brouiller les pistes ?",
                    "answerOptions": [
                        {"text": "Complexité accrue", "isCorrect": True},
                        {"text": "Simplicité totale", "isCorrect": False},
                        {"text": "Brièveté absolue", "isCorrect": False},
                        {"text": "Clarté maximale", "isCorrect": False}
                    ],
                    "correction": "Si une réponse technique est complexe, les leurres doivent présenter une complexité technique apparente supérieure ou une formulation plus alambiquée pour tester la précision de lecture."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le symbole de soudure élémentaire pour une soudure en 'V' ?",
                    "answerOptions": [
                        {"text": "V", "isCorrect": True},
                        {"text": "II", "isCorrect": False},
                        {"text": "Y", "isCorrect": False},
                        {"text": "U", "isCorrect": False}
                    ],
                    "correction": "Le symbole graphique reprend la forme géométrique de la préparation des bords. Une préparation en V est symbolisée par un V."
                },
                {
                    "questionNumber": 20,
                    "question": "Sur un plan d'ensemble, qu'est-ce que la 'nomenclature' ?",
                    "answerOptions": [
                        {"text": "Liste des pièces", "isCorrect": True},
                        {"text": "Liste des vues", "isCorrect": False},
                        {"text": "Liste des cotes", "isCorrect": False},
                        {"text": "Liste des clients", "isCorrect": False}
                    ],
                    "correction": "La nomenclature est le tableau (généralement au-dessus du cartouche) qui répertorie tous les éléments constitutifs de l'ensemble (repère, nombre, désignation, matière)."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNOLOGIE DES MATÉRIAUX ET CONSOMMABLES (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNOLOGIE DES MATÉRIAUX ET CONSOMMABLES",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Dans la désignation normalisée 'S235', que désigne la lettre S ?",
                    "answerOptions": [
                        {"text": "Aciers de construction", "isCorrect": True},
                        {"text": "Aciers inoxydables", "isCorrect": False},
                        {"text": "Aciers à béton", "isCorrect": False},
                        {"text": "Aciers rapides", "isCorrect": False}
                    ],
                    "correction": "La lettre S (pour Structural) désigne les aciers d'usage général utilisés en construction métallique. Le nombre 235 indique la limite élastique en MPa."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est le principal avantage de l'aluminium par rapport à l'acier ?",
                    "answerOptions": [
                        {"text": "Légèreté", "isCorrect": True},
                        {"text": "Magnétisme", "isCorrect": False},
                        {"text": "Dureté", "isCorrect": False},
                        {"text": "Soudabilité", "isCorrect": False}
                    ],
                    "correction": "La densité de l'aluminium (2,7) est environ trois fois inférieure à celle de l'acier (7,85), ce qui permet des ouvrages beaucoup plus légers."
                },
                {
                    "questionNumber": 23,
                    "question": "Comment se nomme un profilé dont la section a la forme d'un I et dont les ailes sont à faces parallèles ?",
                    "answerOptions": [
                        {"text": "IPE", "isCorrect": True},
                        {"text": "IPN", "isCorrect": False},
                        {"text": "UPN", "isCorrect": False},
                        {"text": "HEA", "isCorrect": False}
                    ],
                    "correction": "L'IPE (I à Profil Européen) possède des ailes à faces parallèles et d'épaisseur constante, contrairement à l'IPN dont les ailes sont inclinées (pente de 14%)."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel élément chimique ajoute-t-on principalement à l'acier pour le rendre 'inoxydable' ?",
                    "answerOptions": [
                        {"text": "Chrome", "isCorrect": True},
                        {"text": "Plomb", "isCorrect": False},
                        {"text": "Soufre", "isCorrect": False},
                        {"text": "Hydrogène", "isCorrect": False}
                    ],
                    "correction": "C'est le Chrome (à hauteur de plus de 10,5%) qui permet la formation d'une couche passive protectrice rendant l'acier inoxydable."
                },
                {
                    "questionNumber": 25,
                    "question": "Qu'est-ce qu'une 'cornière' ?",
                    "answerOptions": [
                        {"text": "Profilé en L", "isCorrect": True},
                        {"text": "Profilé en U", "isCorrect": False},
                        {"text": "Profilé en T", "isCorrect": False},
                        {"text": "Profilé en I", "isCorrect": False}
                    ],
                    "correction": "La cornière est un profilé dont la section forme un angle droit (L), avec des ailes qui peuvent être égales ou inégales."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle propriété mécanique désigne la capacité d'un métal à se déformer sans se rompre (comme pour faire un fil de fer) ?",
                    "answerOptions": [
                        {"text": "Ductilité", "isCorrect": True},
                        {"text": "Fragilité", "isCorrect": False},
                        {"text": "Trempabilité", "isCorrect": False},
                        {"text": "Dureté", "isCorrect": False}
                    ],
                    "correction": "La ductilité est la capacité à subir de grandes déformations plastiques sans rompre. L'inverse est la fragilité (comme le verre ou la fonte)."
                },
                {
                    "questionNumber": 27,
                    "question": "Que signifie 'M10' pour une vis ?",
                    "answerOptions": [
                        {"text": "Filetage métrique diamètre 10", "isCorrect": True},
                        {"text": "Longueur totale de 10 millimètres", "isCorrect": False},
                        {"text": "Résistance à la traction de 10 mégapascals", "isCorrect": False},
                        {"text": "Tête de vis de hauteur 10 millimètres", "isCorrect": False}
                    ],
                    "correction": "Le M désigne un pas métrique (ISO) et le chiffre qui suit indique le diamètre nominal de la vis en millimètres."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la particularité d'une vis 'Tête H' ?",
                    "answerOptions": [
                        {"text": "Tête hexagonale", "isCorrect": True},
                        {"text": "Tête carrée", "isCorrect": False},
                        {"text": "Tête fraisée", "isCorrect": False},
                        {"text": "Tête cylindrique", "isCorrect": False}
                    ],
                    "correction": "La vis H possède une tête à 6 pans (hexagonale), serrable avec une clé plate, à pipe ou à douille."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel traitement de surface consiste à plonger l'acier dans un bain de zinc en fusion à 450°C ?",
                    "answerOptions": [
                        {"text": "Galvanisation à chaud", "isCorrect": True},
                        {"text": "Électrozingage", "isCorrect": False},
                        {"text": "Anodisation sulfurique", "isCorrect": False},
                        {"text": "Thermolaquage poudre", "isCorrect": False}
                    ],
                    "correction": "La galvanisation à chaud est le procédé le plus efficace pour la protection anticorrosion longue durée des ouvrages extérieurs en acier."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le rôle principal d'une rondelle plate sous un écrou ?",
                    "answerOptions": [
                        {"text": "Répartir la pression", "isCorrect": True},
                        {"text": "Freiner le desserrage", "isCorrect": False},
                        {"text": "Assurer l'étanchéité", "isCorrect": False},
                        {"text": "Isoler électriquement", "isCorrect": False}
                    ],
                    "correction": "La rondelle plate (M ou L) sert à augmenter la surface d'appui pour éviter de marquer la pièce et répartir l'effort de serrage."
                },
                {
                    "questionNumber": 31,
                    "question": "Dans la désignation d'une vis de classe 8.8, que signifient ces chiffres ?",
                    "answerOptions": [
                        {"text": "Résistance rupture et limite élastique", "isCorrect": True},
                        {"text": "Diamètre de la tête et longueur de la tige", "isCorrect": False},
                        {"text": "Composition chimique et pourcentage de carbone", "isCorrect": False},
                        {"text": "Tolérance de fabrication et rugosité", "isCorrect": False}
                    ],
                    "correction": "Le 1er chiffre (8) x 100 = Résistance rupture (800 MPa). Le 2ème chiffre (8) indique que la limite élastique est 80% de la rupture."
                },
                {
                    "questionNumber": 32,
                    "question": "Le laiton est un alliage composé majoritairement de cuivre et de :",
                    "answerOptions": [
                        {"text": "Zinc", "isCorrect": True},
                        {"text": "Étain", "isCorrect": False},
                        {"text": "Fer", "isCorrect": False},
                        {"text": "Plomb", "isCorrect": False}
                    ],
                    "correction": "Le laiton est un alliage Cuivre + Zinc (jaune). À ne pas confondre avec le Bronze (Cuivre + Étain)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel type de tube est souvent utilisé pour les mains courantes en raison de son confort de préhension ?",
                    "answerOptions": [
                        {"text": "Tube rond", "isCorrect": True},
                        {"text": "Tube carré", "isCorrect": False},
                        {"text": "Tube rectangulaire", "isCorrect": False},
                        {"text": "Tube profilé à ailettes", "isCorrect": False}
                    ],
                    "correction": "Le tube rond (souvent de diamètre 42,4 mm en serrurerie) est le standard ergonomique pour les rampes et mains courantes."
                },
                {
                    "questionNumber": 34,
                    "question": "Comment appelle-t-on la partie centrale d'une électrode enrobée ?",
                    "answerOptions": [
                        {"text": "Âme", "isCorrect": True},
                        {"text": "Flux", "isCorrect": False},
                        {"text": "Gaine", "isCorrect": False},
                        {"text": "Laitier", "isCorrect": False}
                    ],
                    "correction": "L'électrode est composée d'une tige métallique centrale appelée l'âme (qui fond pour apporter le métal) et d'un enrobage extérieur."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel matériau est le plus riche en carbone ?",
                    "answerOptions": [
                        {"text": "Fonte", "isCorrect": True},
                        {"text": "Acier", "isCorrect": False},
                        {"text": "Fer pur", "isCorrect": False},
                        {"text": "Aluminium", "isCorrect": False}
                    ],
                    "correction": "La fonte contient entre 2,1% et 6,67% de carbone, tandis que l'acier en contient moins de 2%. C'est ce carbone qui rend la fonte cassante."
                },
                {
                    "questionNumber": 36,
                    "question": "À quoi sert un scellement chimique ?",
                    "answerOptions": [
                        {"text": "Fixer dans des matériaux creux ou pleins", "isCorrect": True},
                        {"text": "Coller deux plaques d'acier entre elles", "isCorrect": False},
                        {"text": "Réaliser une étanchéité à l'eau de pluie", "isCorrect": False},
                        {"text": "Protéger les vis contre la corrosion saline", "isCorrect": False}
                    ],
                    "correction": "Le scellement chimique (résine + durcisseur) permet de créer un ancrage très résistant sans contrainte d'expansion mécanique, idéal dans la brique creuse ou le parpaing."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle est la forme de la section d'un fer 'Té' ?",
                    "answerOptions": [
                        {"text": "T", "isCorrect": True},
                        {"text": "L", "isCorrect": False},
                        {"text": "U", "isCorrect": False},
                        {"text": "I", "isCorrect": False}
                    ],
                    "correction": "Comme son nom l'indique, la section transversale a la forme de la lettre T majuscule."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel gaz est couramment utilisé comme gaz actif pour le soudage MAG des aciers ?",
                    "answerOptions": [
                        {"text": "Argon et CO2", "isCorrect": True},
                        {"text": "Argon pur", "isCorrect": False},
                        {"text": "Hélium pur", "isCorrect": False},
                        {"text": "Azote liquide", "isCorrect": False}
                    ],
                    "correction": "Pour le MAG (Metal Active Gas), on utilise un mélange oxydant, généralement Argon + CO2 (souvent 82%/18% ou 92%/8%)."
                },
                {
                    "questionNumber": 39,
                    "question": "Qu'est-ce que le 'métal déployé' ?",
                    "answerOptions": [
                        {"text": "Treillis rigide obtenu par découpe et étirage", "isCorrect": True},
                        {"text": "Tôle fine laminée à froid pour carrosserie", "isCorrect": False},
                        {"text": "Bloc d'acier forgé pour augmenter sa densité", "isCorrect": False},
                        {"text": "Poudre métallique projetée à haute pression", "isCorrect": False}
                    ],
                    "correction": "Le métal déployé est fabriqué à partir d'une tôle incisée puis étirée pour former des mailles losanges, utilisé pour des passerelles ou du remplissage."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel outil permet de réaliser un filetage intérieur (dans un trou) ?",
                    "answerOptions": [
                        {"text": "Taraud", "isCorrect": True},
                        {"text": "Filière", "isCorrect": False},
                        {"text": "Foret", "isCorrect": False},
                        {"text": "Alésoir", "isCorrect": False}
                    ],
                    "correction": "Le taraud sert à créer le filetage interne (écrou), tandis que la filière sert à créer le filetage externe (vis)."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : PROCÉDÉS DE DÉBIT ET DE FORMAGE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : PROCÉDÉS DE DÉBIT ET DE FORMAGE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel outil manuel utilise-t-on pour marquer un trait fin et précis sur une tôle en acier ?",
                    "answerOptions": [
                        {"text": "Pointe à tracer", "isCorrect": True},
                        {"text": "Crayon de maçon", "isCorrect": False},
                        {"text": "Feutre tubulaire", "isCorrect": False},
                        {"text": "Craie industrielle", "isCorrect": False}
                    ],
                    "correction": "La pointe à tracer, en acier trempé ou au carbure, permet de rayer la surface du métal pour obtenir un tracé fin, précis et indélébile."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la formule correcte pour calculer la fréquence de rotation N (en tr/min) d'un foret ?",
                    "answerOptions": [
                        {"text": "1000 fois Vc divisé par Pi fois D", "isCorrect": True},
                        {"text": "Pi fois D divisé par 1000 fois Vc", "isCorrect": False},
                        {"text": "100 fois Vc divisé par Pi fois rayon", "isCorrect": False},
                        {"text": "Vc divisé par 60 fois Pi fois D", "isCorrect": False}
                    ],
                    "correction": "La formule est N = (1000 x Vc) / (π x D), où Vc est la vitesse de coupe (m/min) et D le diamètre de l'outil (mm)."
                },
                {
                    "questionNumber": 43,
                    "question": "Sur une cisaille guillotine, quelle pièce maintient fermement la tôle contre la table avant la descente de la lame ?",
                    "answerOptions": [
                        {"text": "Serre-flan", "isCorrect": True},
                        {"text": "Butée arrière", "isCorrect": False},
                        {"text": "Lame mobile", "isCorrect": False},
                        {"text": "Pédale de commande", "isCorrect": False}
                    ],
                    "correction": "Le serre-flan est un vérin qui vient plaquer la tôle pour l'empêcher de bouger ou de se soulever au moment de l'impact de la coupe."
                },
                {
                    "questionNumber": 44,
                    "question": "Lors du pliage d'une tôle, comment appelle-t-on la zone centrale de l'épaisseur qui ne subit ni allongement ni raccourcissement ?",
                    "answerOptions": [
                        {"text": "Fibre neutre", "isCorrect": True},
                        {"text": "Fibre tendue", "isCorrect": False},
                        {"text": "Fibre comprimée", "isCorrect": False},
                        {"text": "Fibre moyenne", "isCorrect": False}
                    ],
                    "correction": "La fibre neutre est la ligne théorique située au cœur de l'épaisseur dont la longueur ne change pas après pliage."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est l'angle d'affûtage standard de la pointe d'un foret pour percer de l'acier courant ?",
                    "answerOptions": [
                        {"text": "118 degrés", "isCorrect": True},
                        {"text": "90 degrés", "isCorrect": False},
                        {"text": "60 degrés", "isCorrect": False},
                        {"text": "45 degrés", "isCorrect": False}
                    ],
                    "correction": "Pour les aciers d'usage général, l'angle de pointe est normalisé à 118°."
                },
                {
                    "questionNumber": 46,
                    "question": "À quoi sert 'l'avoyage' des dents d'une lame de scie à ruban ?",
                    "answerOptions": [
                        {"text": "Éviter le coincement de la lame", "isCorrect": True},
                        {"text": "Augmenter la vitesse de rotation du volant", "isCorrect": False},
                        {"text": "Refroidir automatiquement les dents de la scie", "isCorrect": False},
                        {"text": "Polir les faces coupées pour une finition miroir", "isCorrect": False}
                    ],
                    "correction": "L'avoyage consiste à incliner les dents alternativement à gauche et à droite pour créer un trait de scie plus large que la lame."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel outil permet de réaliser un chambrage conique à l'entrée d'un perçage pour noyer une tête de vis FHC ?",
                    "answerOptions": [
                        {"text": "Fraise", "isCorrect": True},
                        {"text": "Foret", "isCorrect": False},
                        {"text": "Alésoir", "isCorrect": False},
                        {"text": "Taraud", "isCorrect": False}
                    ],
                    "correction": "Le fraisage (avec une fraise conique à 90°) permet d'élargir l'entrée du trou pour que la tête de la vis fraisée ne dépasse pas de la surface."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est le risque principal si l'on perce une tôle fine avec un foret de grand diamètre sans précaution particulière ?",
                    "answerOptions": [
                        {"text": "Trou triangulaire", "isCorrect": True},
                        {"text": "Trou trop petit", "isCorrect": False},
                        {"text": "Foret qui fond", "isCorrect": False},
                        {"text": "Copeau trop long", "isCorrect": False}
                    ],
                    "correction": "Dans la tôle fine, le foret a tendance à 'brouter' et à produire un trou de forme triangulaire ('en trèfle')."
                },
                {
                    "questionNumber": 49,
                    "question": "Pour pointer l'emplacement d'un perçage précis, quel angle doit avoir le pointeau ?",
                    "answerOptions": [
                        {"text": "90 degrés", "isCorrect": True},
                        {"text": "60 degrés", "isCorrect": False},
                        {"text": "120 degrés", "isCorrect": False},
                        {"text": "30 degrés", "isCorrect": False}
                    ],
                    "correction": "Le pointeau à 90° est utilisé pour guider la pointe du foret."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle opération consiste à découper une forme complexe à l'intérieur d'une tôle sans déboucher sur les bords ?",
                    "answerOptions": [
                        {"text": "Poinçonnage", "isCorrect": True},
                        {"text": "Cisaillage", "isCorrect": False},
                        {"text": "Tronçonnage", "isCorrect": False},
                        {"text": "Ébavurage", "isCorrect": False}
                    ],
                    "correction": "Le poinçonnage utilise un poinçon et une matrice pour découper une forme (rond, carré, oblong) en pleine tôle par cisaillement direct."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel paramètre doit-on régler sur une presse plieuse pour obtenir un angle de pliage précis ?",
                    "answerOptions": [
                        {"text": "Descente du coulisseau", "isCorrect": True},
                        {"text": "Vitesse du moteur", "isCorrect": False},
                        {"text": "Pression hydraulique", "isCorrect": False},
                        {"text": "Température de l'huile", "isCorrect": False}
                    ],
                    "correction": "C'est la profondeur de pénétration du poinçon dans le Vé (la course du coulisseau) qui détermine l'angle de pliage en l'air."
                },
                {
                    "questionNumber": 52,
                    "question": "Pourquoi utilise-t-on de l'huile de coupe lors du taraudage manuel ?",
                    "answerOptions": [
                        {"text": "Lubrifier", "isCorrect": True},
                        {"text": "Décaper", "isCorrect": False},
                        {"text": "Coller", "isCorrect": False},
                        {"text": "Sécher", "isCorrect": False}
                    ],
                    "correction": "L'huile est indispensable pour réduire les frottements importants, éviter la casse du taraud et obtenir un filet propre."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel outil de frappe utilise-t-on pour former le métal à chaud ou à froid sur l'enclume ?",
                    "answerOptions": [
                        {"text": "Marteau", "isCorrect": True},
                        {"text": "Maillet", "isCorrect": False},
                        {"text": "Massette", "isCorrect": False},
                        {"text": "Batte", "isCorrect": False}
                    ],
                    "correction": "Le marteau de métallier (ou rivoir) est l'outil de base."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle machine utilise un jet de gaz ionisé à très haute température pour découper des métaux conducteurs ?",
                    "answerOptions": [
                        {"text": "Découpeur plasma", "isCorrect": True},
                        {"text": "Chalumeau oxyacétylénique", "isCorrect": False},
                        {"text": "Scie circulaire carbure", "isCorrect": False},
                        {"text": "Cisaille à levier manuel", "isCorrect": False}
                    ],
                    "correction": "Le procédé plasma utilise un arc électrique constricté qui transforme le gaz en plasma pour fondre et chasser le métal."
                },
                {
                    "questionNumber": 55,
                    "question": "Comment appelle-t-on l'opération qui consiste à enlever les arêtes tranchantes après une coupe ?",
                    "answerOptions": [
                        {"text": "Ébavurage", "isCorrect": True},
                        {"text": "Polissage", "isCorrect": False},
                        {"text": "Surfaçage", "isCorrect": False},
                        {"text": "Rectification", "isCorrect": False}
                    ],
                    "correction": "L'ébavurage est une étape de sécurité obligatoire (avec une lime ou une meuleuse) pour éliminer les bavures coupantes."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'effet d'une ouverture de Vé plus large lors du pliage d'une même épaisseur de tôle ?",
                    "answerOptions": [
                        {"text": "Rayon plus grand", "isCorrect": True},
                        {"text": "Rayon plus petit", "isCorrect": False},
                        {"text": "Force nécessaire plus grande", "isCorrect": False},
                        {"text": "Risque de fissure accru", "isCorrect": False}
                    ],
                    "correction": "Plus le Vé est large, plus le rayon intérieur de pliage sera grand, et moins l'effort nécessaire au pliage sera important."
                },
                {
                    "questionNumber": 57,
                    "question": "Pour cintrer un tube sans qu'il ne s'écrase, quelle pièce insère-t-on parfois à l'intérieur ?",
                    "answerOptions": [
                        {"text": "Mandrin", "isCorrect": True},
                        {"text": "Vérin", "isCorrect": False},
                        {"text": "Foret", "isCorrect": False},
                        {"text": "Galet", "isCorrect": False}
                    ],
                    "correction": "Le mandrin (ou une âme flexible, ou du sable tassé) soutient les parois internes du tube pour éviter l'ovalisation ou le pincement."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle scie est la plus adaptée pour couper des profilés pleins de forte section ?",
                    "answerOptions": [
                        {"text": "Scie à ruban", "isCorrect": True},
                        {"text": "Scie sauteuse", "isCorrect": False},
                        {"text": "Meuleuse d'angle", "isCorrect": False},
                        {"text": "Cisaille à main", "isCorrect": False}
                    ],
                    "correction": "La scie à ruban horizontale est conçue pour couper de fortes sections avec précision et refroidissement."
                },
                {
                    "questionNumber": 59,
                    "question": "Que désigne le terme 'mors' sur un étau ?",
                    "answerOptions": [
                        {"text": "Mâchoires de serrage", "isCorrect": True},
                        {"text": "Vis de manœuvre", "isCorrect": False},
                        {"text": "Socle de fixation", "isCorrect": False},
                        {"text": "Levier de blocage", "isCorrect": False}
                    ],
                    "correction": "Les mors sont les parties (souvent interchangeables et striées) qui entrent directement en contact avec la pièce pour la maintenir."
                },
                {
                    "questionNumber": 60,
                    "question": "Si l'on doit percer un trou de diamètre 8,5 mm avant de tarauder à M10, c'est parce que :",
                    "answerOptions": [
                        {"text": "Le diamètre de perçage est égal au diamètre nominal moins le pas", "isCorrect": True},
                        {"text": "Le diamètre de perçage doit être strictement identique au diamètre nominal de la vis", "isCorrect": False},
                        {"text": "Le perçage doit toujours être réalisé à la moitié du diamètre final du taraudage", "isCorrect": False},
                        {"text": "La matière va se rétracter naturellement après le passage du taraud ébaucheur", "isCorrect": False}
                    ],
                    "correction": "Règle approximative standard : Diamètre de perçage = Diamètre nominal (10) - Pas (1,5 pour du M10 standard) = 8,5 mm."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : TECHNIQUES D'ASSEMBLAGE ET DE SOUDAGE (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : TECHNIQUES D'ASSEMBLAGE ET DE SOUDAGE",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "En soudage à l'arc à l'électrode enrobée, à quoi sert principalement l'enrobage ?",
                    "answerOptions": [
                        {"text": "Protéger le bain", "isCorrect": True},
                        {"text": "Refroidir la pièce", "isCorrect": False},
                        {"text": "Faire joli", "isCorrect": False},
                        {"text": "Économiser l'énergie", "isCorrect": False}
                    ],
                    "correction": "L'enrobage fond et forme un gaz protecteur ainsi qu'un laitier qui isole le bain de fusion de l'oxygène de l'air, évitant l'oxydation."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la différence principale entre le soudage MIG et le soudage MAG ?",
                    "answerOptions": [
                        {"text": "La nature du gaz", "isCorrect": True},
                        {"text": "Le diamètre du fil", "isCorrect": False},
                        {"text": "La couleur de la torche", "isCorrect": False},
                        {"text": "La longueur du câble", "isCorrect": False}
                    ],
                    "correction": "MIG = Metal Inert Gas (gaz inerte). MAG = Metal Active Gas (gaz actif)."
                },
                {
                    "questionNumber": 63,
                    "question": "En soudage TIG, l'électrode est fabriquée en :",
                    "answerOptions": [
                        {"text": "Tungstène", "isCorrect": True},
                        {"text": "Aluminium", "isCorrect": False},
                        {"text": "Cuivre", "isCorrect": False},
                        {"text": "Titane", "isCorrect": False}
                    ],
                    "correction": "L'électrode TIG est 'réfractaire' (non fusible), elle est en Tungstène pour résister à la température de l'arc sans fondre."
                },
                {
                    "questionNumber": 64,
                    "question": "Avant de réaliser un cordon de soudure complet, quelle opération est indispensable pour maintenir les pièces en position ?",
                    "answerOptions": [
                        {"text": "Le pointage", "isCorrect": True},
                        {"text": "Le meulage", "isCorrect": False},
                        {"text": "Le polissage", "isCorrect": False},
                        {"text": "Le graissage", "isCorrect": False}
                    ],
                    "correction": "Le pointage consiste à réaliser de petits points de soudure régulièrement espacés pour fixer l'assemblage."
                },
                {
                    "questionNumber": 65,
                    "question": "Comment appelle-t-on le dépôt vitrifié qui recouvre le cordon de soudure après refroidissement (électrode enrobée) ?",
                    "answerOptions": [
                        {"text": "Laitier", "isCorrect": True},
                        {"text": "Verre", "isCorrect": False},
                        {"text": "Calamine", "isCorrect": False},
                        {"text": "Rouille", "isCorrect": False}
                    ],
                    "correction": "Le laitier est le résidu solide de l'enrobage fondu qui remonte à la surface pour protéger le métal chaud."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel défaut se caractérise par des bulles de gaz emprisonnées dans la soudure ?",
                    "answerOptions": [
                        {"text": "Soufflures", "isCorrect": True},
                        {"text": "Caniveaux", "isCorrect": False},
                        {"text": "Fissures", "isCorrect": False},
                        {"text": "Collages", "isCorrect": False}
                    ],
                    "correction": "Les soufflures (porosités) sont des cavités dues à un gaz qui n'a pas pu s'échapper avant la solidification."
                },
                {
                    "questionNumber": 67,
                    "question": "En soudage MAG, si j'augmente la vitesse de dévidage du fil, qu'est-ce qui augmente proportionnellement ?",
                    "answerOptions": [
                        {"text": "L'intensité du courant", "isCorrect": True},
                        {"text": "La tension à vide", "isCorrect": False},
                        {"text": "Le débit de gaz", "isCorrect": False},
                        {"text": "La fréquence du réseau", "isCorrect": False}
                    ],
                    "correction": "Sur un poste semi-automatique, l'intensité (Ampérage) est directement liée à la vitesse de fil."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle préparation est nécessaire pour souder bout à bout deux tôles d'acier de 10 mm d'épaisseur ?",
                    "answerOptions": [
                        {"text": "Chanfrein", "isCorrect": True},
                        {"text": "Ponçage", "isCorrect": False},
                        {"text": "Dégraissage", "isCorrect": False},
                        {"text": "Vernissage", "isCorrect": False}
                    ],
                    "correction": "Au-delà de 3-4 mm d'épaisseur, il faut réaliser un chanfrein (bords taillés en biseau, souvent en V) pour permettre la pénétration."
                },
                {
                    "questionNumber": 69,
                    "question": "Qu'est-ce qu'un 'caniveau' en défaut de soudure ?",
                    "answerOptions": [
                        {"text": "Un creux sur les bords du cordon", "isCorrect": True},
                        {"text": "Une bosse au milieu du cordon", "isCorrect": False},
                        {"text": "Un trou traversant la pièce", "isCorrect": False},
                        {"text": "Une inclusion de laitier interne", "isCorrect": False}
                    ],
                    "correction": "Le caniveau est un manque de matière le long de la ligne de raccordement, souvent dû à une intensité trop forte."
                },
                {
                    "questionNumber": 70,
                    "question": "Pour limiter les déformations lors du soudage d'une grande longueur, quelle technique utilise-t-on ?",
                    "answerOptions": [
                        {"text": "Le pas de pèlerin", "isCorrect": True},
                        {"text": "Le soudage en continu à très haute intensité sans pause", "isCorrect": False},
                        {"text": "Le soudage simultané par quatre soudeurs alignés", "isCorrect": False},
                        {"text": "Le préchauffage de la pièce à la température de fusion", "isCorrect": False}
                    ],
                    "correction": "Le pas de pèlerin consiste à souder 'à l'envers' par petits tronçons successifs pour mieux répartir la chaleur."
                },
                {
                    "questionNumber": 71,
                    "question": "En soudage TIG, quel métal d'apport utilise-t-on généralement ?",
                    "answerOptions": [
                        {"text": "Baguette dressée tenue à la main", "isCorrect": True},
                        {"text": "Bobine de fil motorisée automatique", "isCorrect": False},
                        {"text": "Électrode enrobée standard", "isCorrect": False},
                        {"text": "Poudre métallique projetée", "isCorrect": False}
                    ],
                    "correction": "En TIG manuel, le soudeur tient la torche d'une main et apporte le métal (baguette) de l'autre main."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie l'acronyme E.P.I. indispensable au soudeur ?",
                    "answerOptions": [
                        {"text": "Équipement de Protection Individuelle", "isCorrect": True},
                        {"text": "Éléments Pour l'Industrie", "isCorrect": False},
                        {"text": "Étude Pratique Informatique", "isCorrect": False},
                        {"text": "Électricien Professionnel Indépendant", "isCorrect": False}
                    ],
                    "correction": "Les EPI du soudeur incluent la cagoule, les gants cuir, le tablier, les chaussures de sécurité, etc."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle position de soudage est codifiée 'PC' ou 'corniche' ?",
                    "answerOptions": [
                        {"text": "Horizontale sur paroi verticale", "isCorrect": True},
                        {"text": "À plat au sol", "isCorrect": False},
                        {"text": "Au plafond", "isCorrect": False},
                        {"text": "Verticale montante", "isCorrect": False}
                    ],
                    "correction": "La soudure en corniche se fait sur un plan vertical, mais le cordon lui-même est horizontal."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle position de soudage est codifiée 'PC' ou 'corniche' ?",
                    "answerOptions": [
                        {"text": "Soudure chantier", "isCorrect": True},
                        {"text": "Soudure périphérique", "isCorrect": False},
                        {"text": "Soudure meulée", "isCorrect": False},
                        {"text": "Soudure bouchon", "isCorrect": False}
                    ],
                    "correction": "Le petit drapeau signale que l'opération de soudage ne se fait pas en atelier mais directement sur le lieu de montage (chantier)."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est la fonction du 'manodétendeur' sur la bouteille de gaz ?",
                    "answerOptions": [
                        {"text": "Réduire la pression et régler le débit", "isCorrect": True},
                        {"text": "Augmenter la pression de la bouteille", "isCorrect": False},
                        {"text": "Mélanger les différents gaz entre eux", "isCorrect": False},
                        {"text": "Filtrer les impuretés de l'air ambiant", "isCorrect": False}
                    ],
                    "correction": "Le manodétendeur abaisse la haute pression de la bouteille à une valeur utilisable et permet de régler le débit."
                },
                {
                    "questionNumber": 76,
                    "question": "En soudage semi-automatique (MAG), si le fil 'tape' au fond du bain (sensation de pic-vert), c'est que :",
                    "answerOptions": [
                        {"text": "La vitesse de fil est trop élevée par rapport à la tension", "isCorrect": True},
                        {"text": "La bouteille de gaz est complètement vide", "isCorrect": False},
                        {"text": "Le tube contact est d'un diamètre trop grand", "isCorrect": False},
                        {"text": "La pince de masse est mal branchée sur la table", "isCorrect": False}
                    ],
                    "correction": "Si le fil arrive trop vite et n'a pas le temps de fondre, il heurte la pièce solide. Il faut réduire la vitesse de fil ou augmenter la tension."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le risque principal pour les yeux lors du soudage à l'arc sans protection ?",
                    "answerOptions": [
                        {"text": "Coup d'arc", "isCorrect": True},
                        {"text": "Coup de soleil", "isCorrect": False},
                        {"text": "Coup de chaleur", "isCorrect": False},
                        {"text": "Coup de vent", "isCorrect": False}
                    ],
                    "correction": "Le 'coup d'arc' est une brûlure de la cornée due aux rayonnements ultraviolets (UV)."
                },
                {
                    "questionNumber": 78,
                    "question": "Qu'appelle-t-on la 'Zone Affectée Thermiquement' (ZAT) ?",
                    "answerOptions": [
                        {"text": "La zone du métal de base chauffée mais non fondue", "isCorrect": True},
                        {"text": "La zone où le métal a totalement fondu et s'est mélangé", "isCorrect": False},
                        {"text": "La zone recouverte par le laitier protecteur", "isCorrect": False},
                        {"text": "La zone située à plus de 50 cm de la soudure", "isCorrect": False}
                    ],
                    "correction": "La ZAT est la bande de métal adjacente à la soudure qui a subi des modifications de structure à cause de la chaleur."
                },
                {
                    "questionNumber": 79,
                    "question": "En soudage TIG, quel gaz est exclusivement utilisé pour protéger l'électrode et le bain ?",
                    "answerOptions": [
                        {"text": "Gaz inerte", "isCorrect": True},
                        {"text": "Gaz actif", "isCorrect": False},
                        {"text": "Gaz oxydant", "isCorrect": False},
                        {"text": "Gaz naturel", "isCorrect": False}
                    ],
                    "correction": "L'électrode Tungstène brûlerait instantanément en présence d'oxygène. Il faut impérativement un gaz inerte (Argon ou Hélium)."
                },
                {
                    "questionNumber": 80,
                    "question": "Pour assembler deux tubes perpendiculaires (piquage), quelle opération de découpe est nécessaire sur le tube aboutissant ?",
                    "answerOptions": [
                        {"text": "Gueule de loup", "isCorrect": True},
                        {"text": "Coupe droite", "isCorrect": False},
                        {"text": "Coupe biaise", "isCorrect": False},
                        {"text": "Coupe sifflet", "isCorrect": False}
                    ],
                    "correction": "La découpe en 'gueule de loup' épouse la forme cylindrique du tube porteur pour un ajustement parfait."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : POSE, MAINTENANCE ET PRÉVENTION SANTÉ ENVIRONNEMENT (PSE) (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : POSE, MAINTENANCE ET PRÉVENTION SANTÉ ENVIRONNEMENT (PSE)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Pour fixer une charge lourde dans une dalle en béton plein non fissuré, quel élément de fixation mécanique est le plus adapté ?",
                    "answerOptions": [
                        {"text": "Goujon", "isCorrect": True},
                        {"text": "Cheville nylon universelle à expansion", "isCorrect": False},
                        {"text": "Vis à bois à tête fraisée", "isCorrect": False},
                        {"text": "Clou en acier trempé strié", "isCorrect": False}
                    ],
                    "correction": "Le goujon d'ancrage est conçu pour supporter des charges lourdes dans le béton plein grâce à sa bague qui s'expanse fortement."
                },
                {
                    "questionNumber": 82,
                    "question": "Selon le code couleur international, quelle est la Charge Maximale d'Utilisation (CMU) d'une élingue textile violette ?",
                    "answerOptions": [
                        {"text": "1 tonne", "isCorrect": True},
                        {"text": "2 tonnes", "isCorrect": False},
                        {"text": "3 tonnes", "isCorrect": False},
                        {"text": "5 tonnes", "isCorrect": False}
                    ],
                    "correction": "Code couleur des élingues plates : Violet = 1T, Vert = 2T, Jaune = 3T, Gris = 4T, Rouge = 5T."
                },
                {
                    "questionNumber": 83,
                    "question": "À partir de quel niveau sonore le port de protections auditives (casque ou bouchons) devient-il obligatoire selon la réglementation ?",
                    "answerOptions": [
                        {"text": "85 décibels", "isCorrect": True},
                        {"text": "50 décibels", "isCorrect": False},
                        {"text": "120 décibels", "isCorrect": False},
                        {"text": "140 décibels", "isCorrect": False}
                    ],
                    "correction": "Le seuil d'action déclenchant l'obligation de port est de 85 dB(A)."
                },
                {
                    "questionNumber": 84,
                    "question": "Pour effectuer des travaux de meulage ou d'ébarbage, quelle protection oculaire est impérative ?",
                    "answerOptions": [
                        {"text": "Lunettes à coques", "isCorrect": True},
                        {"text": "Masque chirurgical", "isCorrect": False},
                        {"text": "Lunettes de soleil", "isCorrect": False},
                        {"text": "Lentilles de contact", "isCorrect": False}
                    ],
                    "correction": "Il faut impérativement des lunettes de sécurité avec protections latérales (coques) ou une visière faciale."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle est la position correcte pour soulever une charge lourde au sol afin de protéger sa colonne vertébrale ?",
                    "answerOptions": [
                        {"text": "Dos droit et jambes pliées", "isCorrect": True},
                        {"text": "Dos rond et jambes tendues", "isCorrect": False},
                        {"text": "Jambes croisées et dos penché", "isCorrect": False},
                        {"text": "Bras tendus et dos courbé vers l'avant", "isCorrect": False}
                    ],
                    "correction": "Il faut garder le dos plat et utiliser la force des cuisses pour se relever."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel type de fixation est particulièrement recommandé pour un ancrage solide dans un matériau creux (parpaing, brique creuse) ?",
                    "answerOptions": [
                        {"text": "Scellement chimique", "isCorrect": True},
                        {"text": "Goujon à frapper", "isCorrect": False},
                        {"text": "Vis à béton sans cheville", "isCorrect": False},
                        {"text": "Clou lisse standard", "isCorrect": False}
                    ],
                    "correction": "Le scellement chimique (tamis + résine) crée un bouchon de matière qui verrouille la fixation sans contrainte d'écartement."
                },
                {
                    "questionNumber": 87,
                    "question": "Que signifie le pictogramme de sécurité représentant une tête de mort sur un bidon de produit chimique ?",
                    "answerOptions": [
                        {"text": "Toxique", "isCorrect": True},
                        {"text": "Corrosif", "isCorrect": False},
                        {"text": "Inflammable", "isCorrect": False},
                        {"text": "Explosif", "isCorrect": False}
                    ],
                    "correction": "Ce symbole indique que le produit est toxique ou mortel par inhalation, ingestion ou contact cutané."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel type d'extincteur doit-on privilégier pour éteindre un début d'incendie sur une armoire électrique sous tension ?",
                    "answerOptions": [
                        {"text": "CO2", "isCorrect": True},
                        {"text": "Eau", "isCorrect": False},
                        {"text": "Mousse", "isCorrect": False},
                        {"text": "Sable", "isCorrect": False}
                    ],
                    "correction": "Le dioxyde de carbone (CO2) est un gaz inerte qui étouffe le feu sans conduire l'électricité et sans laisser de résidus."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle norme européenne régit les gants de protection contre les risques mécaniques (coupure, déchirure, abrasion) ?",
                    "answerOptions": [
                        {"text": "EN 388", "isCorrect": True},
                        {"text": "EN 166", "isCorrect": False},
                        {"text": "EN 374", "isCorrect": False},
                        {"text": "EN 407", "isCorrect": False}
                    ],
                    "correction": "La norme EN 388 est marquée sur les gants avec un pictogramme 'marteau/bouclier'."
                },
                {
                    "questionNumber": 90,
                    "question": "Lors de l'utilisation d'une perceuse à colonne, le port des gants est :",
                    "answerOptions": [
                        {"text": "Interdit", "isCorrect": True},
                        {"text": "Obligatoire", "isCorrect": False},
                        {"text": "Conseillé", "isCorrect": False},
                        {"text": "Indifférent", "isCorrect": False}
                    ],
                    "correction": "Les gants sont strictement interdits avec les machines rotatives car le tissu risque d'être happé par le foret."
                },
                {
                    "questionNumber": 91,
                    "question": "Sur un chantier, quel équipement mobile permet de travailler en hauteur en sécurité individuelle sans avoir besoin de s'attacher ?",
                    "answerOptions": [
                        {"text": "PIRL", "isCorrect": True},
                        {"text": "Échelle", "isCorrect": False},
                        {"text": "Escabeau", "isCorrect": False},
                        {"text": "Chaise", "isCorrect": False}
                    ],
                    "correction": "La Plate-forme Individuelle Roulante Légère (PIRL) possède des garde-corps intégrés et des plinthes."
                },
                {
                    "questionNumber": 92,
                    "question": "Que signifie l'acronyme CMU inscrit sur les appareils de levage ?",
                    "answerOptions": [
                        {"text": "Charge Maximale d'Utilisation", "isCorrect": True},
                        {"text": "Charge Moyenne Usuelle", "isCorrect": False},
                        {"text": "Capacité Mécanique Universelle", "isCorrect": False},
                        {"text": "Coefficient Minimum d'Usure", "isCorrect": False}
                    ],
                    "correction": "La CMU est la charge maximale que le matériel peut soulever en conditions normales de sécurité."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est l'effet de l'augmentation de l'angle entre les brins d'une élingue lors d'un levage ?",
                    "answerOptions": [
                        {"text": "Augmente la tension dans les brins", "isCorrect": True},
                        {"text": "Diminue la tension globale supportée par les câbles de levage", "isCorrect": False},
                        {"text": "Ne change absolument rien à la répartition des forces", "isCorrect": False},
                        {"text": "Divise le poids de la charge par deux automatiquement", "isCorrect": False}
                    ],
                    "correction": "Plus l'angle au sommet est grand (ouvert), plus la tension dans chaque brin augmente considérablement."
                },
                {
                    "questionNumber": 94,
                    "question": "Que faire si une élingue textile présente une coupure ou une déchirure importante ?",
                    "answerOptions": [
                        {"text": "Rebut", "isCorrect": True},
                        {"text": "Couture", "isCorrect": False},
                        {"text": "Scotch", "isCorrect": False},
                        {"text": "Collage", "isCorrect": False}
                    ],
                    "correction": "Aucune réparation n'est autorisée. Il faut détruire et jeter l'élingue (mise au rebut)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la conduite à tenir immédiate en cas de brûlure thermique simple ?",
                    "answerOptions": [
                        {"text": "Arroser", "isCorrect": True},
                        {"text": "Graisser", "isCorrect": False},
                        {"text": "Percer", "isCorrect": False},
                        {"text": "Bandages", "isCorrect": False}
                    ],
                    "correction": "Arroser à l'eau tempérée pendant 15 minutes pour stopper la propagation de la chaleur."
                },
                {
                    "questionNumber": 96,
                    "question": "Lequel de ces métaux dégage des fumées particulièrement toxiques causant la 'fièvre des fondeurs' s'il est soudé sans protection ?",
                    "answerOptions": [
                        {"text": "Zinc", "isCorrect": True},
                        {"text": "Fer", "isCorrect": False},
                        {"text": "Or", "isCorrect": False},
                        {"text": "Titane", "isCorrect": False}
                    ],
                    "correction": "Le soudage de l'acier galvanisé (recouvert de Zinc) dégage des fumées d'oxyde de zinc très irritantes."
                },
                {
                    "questionNumber": 97,
                    "question": "Pour protéger les voies respiratoires des fumées de soudage, quelle est la protection collective prioritaire ?",
                    "answerOptions": [
                        {"text": "Aspiration à la source", "isCorrect": True},
                        {"text": "Port du masque FFP2 jetable", "isCorrect": False},
                        {"text": "Consommation de lait", "isCorrect": False},
                        {"text": "Ouverture des portes", "isCorrect": False}
                    ],
                    "correction": "La protection collective (torche aspirante ou bras d'aspiration) prime toujours sur la protection individuelle."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel symbole indique qu'un outil électroportatif est à 'double isolation' (Classe II) et ne nécessite pas de mise à la terre ?",
                    "answerOptions": [
                        {"text": "Double carré", "isCorrect": True},
                        {"text": "Double cercle", "isCorrect": False},
                        {"text": "Éclair rouge", "isCorrect": False},
                        {"text": "Triangle noir", "isCorrect": False}
                    ],
                    "correction": "Le symbole de deux carrés l'un dans l'autre indique que l'appareil possède une isolation renforcée."
                },
                {
                    "questionNumber": 99,
                    "question": "L'acier est un matériau qui est :",
                    "answerOptions": [
                        {"text": "Recyclable à l'infini", "isCorrect": True},
                        {"text": "Recyclable une seule fois", "isCorrect": False},
                        {"text": "Non valorisable en fin de vie", "isCorrect": False},
                        {"text": "Dégradable biologiquement", "isCorrect": False}
                    ],
                    "correction": "L'acier peut être refondu et réutilisé indéfiniment sans perte de ses propriétés mécaniques."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la principale fonction d'une 'lisse' (ou main courante) sur un garde-corps ?",
                    "answerOptions": [
                        {"text": "Empêcher la chute", "isCorrect": True},
                        {"text": "Décorer l'escalier", "isCorrect": False},
                        {"text": "Poser des objets", "isCorrect": False},
                        {"text": "Rigidifier le sol", "isCorrect": False}
                    ],
                    "correction": "La fonction réglementaire du garde-corps est la protection contre les chutes de hauteur."
                },
            ]
        }
    }
}