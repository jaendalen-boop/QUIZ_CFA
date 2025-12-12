quiz_data = {
    "title": "Quiz CAP Maçon : Technologie, Techniques, Sécurité et Calculs (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET DU BÉTON ARMÉ (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET DU BÉTON ARMÉ",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel composant principal confère au béton armé sa résistance aux efforts de traction ?",
                    "answerOptions": [
                        {"text": "L'acier", "isCorrect": True},
                        {"text": "Le gravier", "isCorrect": False},
                        {"text": "Le ciment", "isCorrect": False},
                        {"text": "Le sable", "isCorrect": False}
                    ],
                    "correction": "Le béton résiste très bien à la compression mais très mal à la traction. On y intègre des armatures en acier pour reprendre ces efforts de traction et éviter la rupture de l'ouvrage."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la définition exacte du clinker dans la fabrication du ciment ?",
                    "answerOptions": [
                        {"text": "Un constituant semi-fini obtenu par cuisson", "isCorrect": True},
                        {"text": "Une poudre finale prête à l'emploi sur le chantier", "isCorrect": False},
                        {"text": "Un adjuvant liquide ajouté dans la bétonnière", "isCorrect": False},
                        {"text": "Un granulat d'origine volcanique très léger", "isCorrect": False}
                    ],
                    "correction": "Le clinker est le produit de la cuisson d'un mélange de calcaire et d'argile à très haute température (1450°C). C'est le constituant de base hydraulique qui, après broyage avec du gypse, donnera le ciment."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est l'effet principal d'un adjuvant hydrofuge sur un mortier ?",
                    "answerOptions": [
                        {"text": "Imperméabiliser", "isCorrect": True},
                        {"text": "Fluidifier", "isCorrect": False},
                        {"text": "Retarder", "isCorrect": False},
                        {"text": "Accélérer", "isCorrect": False}
                    ],
                    "correction": "L'hydrofuge de masse réduit la perméabilité du béton ou du mortier en obstruant les capillaires, ce qui empêche l'eau de pénétrer à l'intérieur du matériau."
                },
                {
                    "questionNumber": 4,
                    "question": "Pourquoi est-il indispensable de respecter l'enrobage minimal des aciers dans une poutre en béton armé ?",
                    "answerOptions": [
                        {"text": "Pour protéger les armatures de la corrosion", "isCorrect": True},
                        {"text": "Pour économiser la quantité de béton utilisée", "isCorrect": False},
                        {"text": "Pour permettre de voir les aciers après le décoffrage", "isCorrect": False},
                        {"text": "Pour augmenter la vitesse de séchage du béton", "isCorrect": False}
                    ],
                    "correction": "L'enrobage (généralement 2,5 à 3 cm) crée une barrière physique et chimique qui empêche l'oxygène et l'humidité d'atteindre l'acier, évitant ainsi qu'il ne rouille et ne fasse éclater le béton."
                },
                {
                    "questionNumber": 5,
                    "question": "Comment appelle-t-on le phénomène de séparation des constituants du béton frais lors d'une mauvaise mise en œuvre ?",
                    "answerOptions": [
                        {"text": "La ségrégation", "isCorrect": True},
                        {"text": "La carbonatation", "isCorrect": False},
                        {"text": "La vibration", "isCorrect": False},
                        {"text": "La dessiccation", "isCorrect": False}
                    ],
                    "correction": "La ségrégation est le défaut d'homogénéité du béton où les gros granulats descendent au fond et la laitance remonte en surface, souvent causé par un excès d'eau ou une vibration excessive."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la densité moyenne approximative d'un béton armé courant ?",
                    "answerOptions": [
                        {"text": "2500 kg/m3", "isCorrect": True},
                        {"text": "1000 kg/m3", "isCorrect": False},
                        {"text": "1500 kg/m3", "isCorrect": False},
                        {"text": "4000 kg/m3", "isCorrect": False}
                    ],
                    "correction": "La masse volumique du béton armé est généralement comprise entre 2400 et 2500 kg/m3 (2,4 à 2,5 tonnes par mètre cube), en tenant compte du poids des aciers."
                },
                {
                    "questionNumber": 7,
                    "question": "À quoi sert l'essai au cône d'Abrams sur un chantier de maçonnerie ?",
                    "answerOptions": [
                        {"text": "Mesurer la consistance", "isCorrect": True},
                        {"text": "Vérifier la température", "isCorrect": False},
                        {"text": "Peser les granulats", "isCorrect": False},
                        {"text": "Calculer le ferraillage", "isCorrect": False}
                    ],
                    "correction": "L'essai au cône d'Abrams (ou Slump test) permet de mesurer l'affaissement du béton frais pour déterminer sa classe de consistance (de ferme à très fluide) et sa maniabilité."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle précaution est impérative lors du stockage des sacs de ciment sur le chantier ?",
                    "answerOptions": [
                        {"text": "Les stocker sur palette dans un lieu sec", "isCorrect": True},
                        {"text": "Les laisser directement sur le sol naturel", "isCorrect": False},
                        {"text": "Les ouvrir à l'avance pour gagner du temps", "isCorrect": False},
                        {"text": "Les arroser régulièrement pour les nettoyer", "isCorrect": False}
                    ],
                    "correction": "Le ciment est un liant hydraulique qui réagit à l'humidité. Il doit être impérativement stocké surélevé (palette) et à l'abri des intempéries pour éviter qu'il ne durcisse avant utilisation (éventage)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel granulat utilise-t-on spécifiquement pour réaliser la couche de finition d'un enduit traditionnel ?",
                    "answerOptions": [
                        {"text": "Le sablon", "isCorrect": True},
                        {"text": "Le gravillon", "isCorrect": False},
                        {"text": "Le caillou", "isCorrect": False},
                        {"text": "Le ballast", "isCorrect": False}
                    ],
                    "correction": "Pour la finition (ou couche de parement), on utilise un sable très fin appelé sablon (grain 0/2 ou moins) afin d'obtenir un aspect lisse et soigné."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le rôle principal de la vibration lors du coulage du béton ?",
                    "answerOptions": [
                        {"text": "Chasser l'air", "isCorrect": True},
                        {"text": "Ajouter de l'eau", "isCorrect": False},
                        {"text": "Tiédir le mélange", "isCorrect": False},
                        {"text": "Trier les cailloux", "isCorrect": False}
                    ],
                    "correction": "La vibration permet de serrer le béton en expulsant les bulles d'air emprisonnées, ce qui augmente sa compacité, sa résistance mécanique et son esthétique (parement lisse)."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la conséquence directe d'un excès d'eau de gâchage dans le béton ?",
                    "answerOptions": [
                        {"text": "Une chute de la résistance", "isCorrect": True},
                        {"text": "Une meilleure durabilité", "isCorrect": False},
                        {"text": "Une prise plus rapide", "isCorrect": False},
                        {"text": "Une couleur plus foncée", "isCorrect": False}
                    ],
                    "correction": "Le surdosage en eau augmente la porosité du béton après évaporation. Cela entraîne inévitablement une baisse significative de sa résistance mécanique (loi de Féret) et augmente le risque de fissuration par retrait."
                },
                {
                    "questionNumber": 12,
                    "question": "Que signifie la désignation CEM II sur un sac de ciment ?",
                    "answerOptions": [
                        {"text": "Ciment composé", "isCorrect": True},
                        {"text": "Ciment prompt", "isCorrect": False},
                        {"text": "Ciment fondu", "isCorrect": False},
                        {"text": "Ciment blanc", "isCorrect": False}
                    ],
                    "correction": "CEM II désigne un ciment Portland composé, qui contient au moins 65% de clinker et d'autres constituants (comme du calcaire ou des cendres volantes), couramment utilisé pour les travaux de maçonnerie usuels."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel adjuvant doit-on utiliser pour bétonner par temps froid afin d'éviter le gel de l'eau libre ?",
                    "answerOptions": [
                        {"text": "Un accélérateur de prise", "isCorrect": True},
                        {"text": "Un retardateur de prise", "isCorrect": False},
                        {"text": "Un plastifiant réducteur", "isCorrect": False},
                        {"text": "Un hydrofuge de surface", "isCorrect": False}
                    ],
                    "correction": "L'accélérateur de prise permet au béton de durcir plus vite. Cela dégage de la chaleur (réaction exothermique) plus rapidement et réduit le temps pendant lequel le béton est vulnérable au gel."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelle est la différence fondamentale entre un mortier et un béton ?",
                    "answerOptions": [
                        {"text": "La présence de gravillons", "isCorrect": True},
                        {"text": "La couleur du mélange", "isCorrect": False},
                        {"text": "La nature du liant", "isCorrect": False},
                        {"text": "Le type d'adjuvant", "isCorrect": False}
                    ],
                    "correction": "La différence technique majeure est la taille des granulats. Le béton contient des gravillons (gros granulats > 5mm) pour la structure, tandis que le mortier ne contient que du sable."
                },
                {
                    "questionNumber": 15,
                    "question": "Pourquoi utilise-t-on un produit de cure sur une dalle béton fraîchement coulée en été ?",
                    "answerOptions": [
                        {"text": "Pour limiter l'évaporation trop rapide de l'eau", "isCorrect": True},
                        {"text": "Pour donner une couleur rouge à la surface", "isCorrect": False},
                        {"text": "Pour rendre le béton totalement incombustible", "isCorrect": False},
                        {"text": "Pour empêcher les insectes de se poser dessus", "isCorrect": False}
                    ],
                    "correction": "La cure consiste à protéger le béton frais contre une dessiccation précoce due au soleil ou au vent. Sans cela, l'eau s'évapore avant d'avoir hydraté le ciment, provoquant des fissures de retrait plastique."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle propriété la chaux apporte-t-elle spécifiquement aux mortiers de restauration ?",
                    "answerOptions": [
                        {"text": "La perméabilité à la vapeur d'eau", "isCorrect": True},
                        {"text": "Une résistance mécanique extrême", "isCorrect": False},
                        {"text": "Une étanchéité totale à l'air", "isCorrect": False},
                        {"text": "Une prise instantanée sous l'eau", "isCorrect": False}
                    ],
                    "correction": "La chaux permet aux murs anciens de 'respirer'. Elle laisse passer la vapeur d'eau de l'intérieur vers l'extérieur, évitant ainsi l'accumulation d'humidité dans les murs en pierre ou en terre."
                },
                {
                    "questionNumber": 17,
                    "question": "Que représente le dosage '350 kg/m3' pour un béton ?",
                    "answerOptions": [
                        {"text": "La quantité de ciment", "isCorrect": True},
                        {"text": "Le poids total du béton", "isCorrect": False},
                        {"text": "Le volume de sable sec", "isCorrect": False},
                        {"text": "La masse de graviers", "isCorrect": False}
                    ],
                    "correction": "Le dosage exprime la masse de liant (ciment) par mètre cube de béton en place. Un dosage à 350 kg/m3 est le standard pour le béton armé courant (dalles, poutres, poteaux)."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est l'unité de mesure de la résistance à la compression du béton ?",
                    "answerOptions": [
                        {"text": "Le Mégapascal", "isCorrect": True},
                        {"text": "Le Kilogramme", "isCorrect": False},
                        {"text": "Le Newton", "isCorrect": False},
                        {"text": "Le Joule", "isCorrect": False}
                    ],
                    "correction": "La résistance du béton se mesure en Mégapascals (MPa). Par exemple, un béton C25/30 a une résistance caractéristique à la compression de 25 MPa sur cylindre à 28 jours."
                },
                {
                    "questionNumber": 19,
                    "question": "Dans quel cas utilise-t-on un retardateur de prise ?",
                    "answerOptions": [
                        {"text": "Par temps très chaud", "isCorrect": True},
                        {"text": "Par temps de gel", "isCorrect": False},
                        {"text": "Pour un scellement", "isCorrect": False},
                        {"text": "Pour une petite gâche", "isCorrect": False}
                    ],
                    "correction": "Par temps chaud, le béton tire trop vite. Le retardateur permet de conserver la maniabilité du béton plus longtemps, laissant le temps aux maçons de le mettre en œuvre correctement avant qu'il ne durcisse."
                },
                {
                    "questionNumber": 20,
                    "question": "À quoi sert l'essai d'équivalent de sable lors de l'analyse des granulats ?",
                    "answerOptions": [
                        {"text": "Vérifier la propreté", "isCorrect": True},
                        {"text": "Mesurer la dureté", "isCorrect": False},
                        {"text": "Peser la densité", "isCorrect": False},
                        {"text": "Trier la taille", "isCorrect": False}
                    ],
                    "correction": "Cet essai permet de déterminer la proportion d'éléments fins argileux dans le sable. Un sable trop 'sale' (riche en argile) nuit à l'adhérence du ciment et à la qualité du béton."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : LECTURE DE PLANS, IMPLANTATION ET MATHÉMATIQUES DE CHANTIER (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : LECTURE DE PLANS, IMPLANTATION ET MATHÉMATIQUES DE CHANTIER",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Sur un plan à l'échelle 1/50, un mur mesure 10 cm sur le papier. Quelle est sa longueur réelle ?",
                    "answerOptions": [
                        {"text": "5 mètres", "isCorrect": True},
                        {"text": "50 mètres", "isCorrect": False},
                        {"text": "500 mètres", "isCorrect": False},
                        {"text": "1 mètre", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/50 signifie que 1 cm sur le plan égale 50 cm en réalité. Donc 10 cm x 50 = 500 cm, soit 5 mètres."
                },
                {
                    "questionNumber": 22,
                    "question": "Que signifie le sigle N.G.F. souvent indiqué sur les plans de masse ?",
                    "answerOptions": [
                        {"text": "Nivellement Général de la France", "isCorrect": True},
                        {"text": "Norme Géographique Française", "isCorrect": False},
                        {"text": "Niveau Global des Fondations", "isCorrect": False},
                        {"text": "Nouvelle Géométrie de Façade", "isCorrect": False}
                    ],
                    "correction": "Le N.G.F. est le système de référence altimétrique officiel en France (le 'niveau zéro' étant le niveau moyen de la mer à Marseille), permettant de situer l'altitude des ouvrages."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle règle mathématique utilise-t-on sur chantier pour vérifier un angle droit avec la méthode '3-4-5' ?",
                    "answerOptions": [
                        {"text": "Le théorème de Pythagore", "isCorrect": True},
                        {"text": "Le théorème de Thalès", "isCorrect": False},
                        {"text": "La règle de trois", "isCorrect": False},
                        {"text": "Le calcul de l'aire du cercle", "isCorrect": False}
                    ],
                    "correction": "Le théorème de Pythagore permet de créer un angle droit. Si on mesure 3m d'un côté et 4m de l'autre, la diagonale (l'hypoténuse) doit mesurer exactement 5m."
                },
                {
                    "questionNumber": 24,
                    "question": "À quelle hauteur par rapport au sol fini est théoriquement réalisée la coupe horizontale pour obtenir une 'vue en plan' ?",
                    "answerOptions": [
                        {"text": "1 mètre", "isCorrect": True},
                        {"text": "3 mètres", "isCorrect": False},
                        {"text": "10 centimètres", "isCorrect": False},
                        {"text": "Au niveau de la toiture", "isCorrect": False}
                    ],
                    "correction": "Par convention, une vue en plan est une coupe horizontale fictive du bâtiment réalisée à 1 mètre au-dessus du sol fini, ce qui permet de voir les ouvertures (portes et fenêtres)."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel volume de béton faut-il pour couler une semelle filante de 10 m de long, 0,50 m de large et 0,40 m de haut ?",
                    "answerOptions": [
                        {"text": "2 m3", "isCorrect": True},
                        {"text": "20 m3", "isCorrect": False},
                        {"text": "0,2 m3", "isCorrect": False},
                        {"text": "5 m3", "isCorrect": False}
                    ],
                    "correction": "Le volume se calcule par la formule Longueur x Largeur x Hauteur. Ici : 10 x 0,50 x 0,40 = 2 mètres cubes."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel type de trait est utilisé en dessin technique pour représenter les axes de symétrie ou les files de murs ?",
                    "answerOptions": [
                        {"text": "Un trait mixte fin", "isCorrect": True},
                        {"text": "Un trait continu fort", "isCorrect": False},
                        {"text": "Un trait interrompu court", "isCorrect": False},
                        {"text": "Un trait continu fin ondulé", "isCorrect": False}
                    ],
                    "correction": "Le trait mixte fin (une alternance de traits longs et de points ou traits courts) est la norme conventionnelle pour représenter les axes et les plans de symétrie."
                },
                {
                    "questionNumber": 27,
                    "question": "Sur un chantier, à quoi correspond généralement le 'trait de niveau' tracé par le maçon ?",
                    "answerOptions": [
                        {"text": "Un repère à un mètre du sol fini", "isCorrect": True},
                        {"text": "La limite basse des fondations profondes", "isCorrect": False},
                        {"text": "Le sommet de la future toiture", "isCorrect": False},
                        {"text": "La position des canalisations enterrées", "isCorrect": False}
                    ],
                    "correction": "Le trait de niveau est un repère horizontal tracé sur les murs, servant de référence constante pour toutes les hauteurs. Il est conventionnellement situé à 1,00 m au-dessus du sol fini."
                },
                {
                    "questionNumber": 28,
                    "question": "Que représentent les hachures sur une coupe verticale d'un plan d'exécution ?",
                    "answerOptions": [
                        {"text": "La nature des matériaux coupés", "isCorrect": True},
                        {"text": "L'intensité de la lumière", "isCorrect": False},
                        {"text": "Les zones interdites au public", "isCorrect": False},
                        {"text": "Les parties à démolir plus tard", "isCorrect": False}
                    ],
                    "correction": "Les hachures sont des motifs graphiques normalisés (traits obliques, croisés, points...) qui indiquent quel matériau compose la paroi sectionnée (béton, brique, isolant, etc.)."
                },
                {
                    "questionNumber": 29,
                    "question": "À quoi servent les 'chaises d'implantation' installées avant le terrassement ?",
                    "answerOptions": [
                        {"text": "Matérialiser les axes des murs", "isCorrect": True},
                        {"text": "Permettre aux maçons de s'asseoir", "isCorrect": False},
                        {"text": "Stocker les outils à l'abri", "isCorrect": False},
                        {"text": "Soutenir les banches de coffrage", "isCorrect": False}
                    ],
                    "correction": "Les chaises sont des cadres en bois plantés à l'extérieur de l'emprise du bâtiment. On y fixe des pointes et des cordeaux pour visualiser les axes des fondations et des murs sans être gêné par les trous."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle information principale donne le 'Plan de Masse' ?",
                    "answerOptions": [
                        {"text": "La position de la construction sur le terrain", "isCorrect": True},
                        {"text": "La disposition des meubles dans les pièces", "isCorrect": False},
                        {"text": "Le détail du ferraillage des poutres", "isCorrect": False},
                        {"text": "La couleur des peintures intérieures", "isCorrect": False}
                    ],
                    "correction": "Le plan de masse est une vue de dessus de l'ensemble de la parcelle. Il indique l'orientation, les accès, les raccordements et la position précise du bâtiment par rapport aux limites de propriété."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment exprime-t-on une pente de 2 centimètres par mètre en pourcentage ?",
                    "answerOptions": [
                        {"text": "2 %", "isCorrect": True},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "0,2 %", "isCorrect": False},
                        {"text": "200 %", "isCorrect": False}
                    ],
                    "correction": "Une pente de x cm par mètre correspond directement à x %. Si on monte de 2 cm sur une longueur de 100 cm (1m), la pente est de 2/100, soit 2 %."
                },
                {
                    "questionNumber": 32,
                    "question": "Que permet de vérifier la mesure des diagonales lors de l'implantation d'un bâtiment rectangulaire ?",
                    "answerOptions": [
                        {"text": "L'équerrage des angles", "isCorrect": True},
                        {"text": "La planéité du sol", "isCorrect": False},
                        {"text": "La hauteur des murs", "isCorrect": False},
                        {"text": "La résistance du sol", "isCorrect": False}
                    ],
                    "correction": "Si les deux diagonales d'un quadrilatère sont de longueur égale, alors c'est un rectangle parfait. Cela permet de s'assurer que les angles sont bien à 90 degrés (équerrage)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est l'équivalence exacte de 1 mètre cube en litres ?",
                    "answerOptions": [
                        {"text": "1000 litres", "isCorrect": True},
                        {"text": "100 litres", "isCorrect": False},
                        {"text": "10 litres", "isCorrect": False},
                        {"text": "10000 litres", "isCorrect": False}
                    ],
                    "correction": "C'est une conversion fondamentale pour les dosages. Un cube de 1m x 1m x 1m contient 1000 litres d'eau."
                },
                {
                    "questionNumber": 34,
                    "question": "Sur un plan, que désigne le terme 'nu intérieur' ?",
                    "answerOptions": [
                        {"text": "La face verticale intérieure du mur", "isCorrect": True},
                        {"text": "L'épaisseur totale du mur brut", "isCorrect": False},
                        {"text": "L'isolation placée au centre du mur", "isCorrect": False},
                        {"text": "La surface au sol de la pièce", "isCorrect": False}
                    ],
                    "correction": "Le 'nu' désigne la surface d'une paroi. Le nu intérieur est la face du mur située côté pièce, par opposition au nu extérieur (côté façade)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel instrument optique permet de réaliser des relevés de niveaux de haute précision sur de grandes distances ?",
                    "answerOptions": [
                        {"text": "La lunette de chantier", "isCorrect": True},
                        {"text": "Le niveau à bulle", "isCorrect": False},
                        {"text": "Le fil à plomb", "isCorrect": False},
                        {"text": "Le télémètre laser simple", "isCorrect": False}
                    ],
                    "correction": "La lunette de chantier (ou niveau optique), utilisée avec une mire, permet de viser à l'horizontale sur de longues distances pour déterminer des différences d'altitude avec précision."
                },
                {
                    "questionNumber": 36,
                    "question": "Dans un métré, comment calcule-t-on la surface d'un pignon triangulaire de base 8m et de hauteur 3m ?",
                    "answerOptions": [
                        {"text": "12 m2", "isCorrect": True},
                        {"text": "24 m2", "isCorrect": False},
                        {"text": "11 m2", "isCorrect": False},
                        {"text": "48 m2", "isCorrect": False}
                    ],
                    "correction": "La surface d'un triangle est (Base x Hauteur) / 2. Ici : (8 x 3) / 2 = 24 / 2 = 12 m2."
                },
                {
                    "questionNumber": 37,
                    "question": "Que représente un trait continu fort sur un dessin d'architecture ?",
                    "answerOptions": [
                        {"text": "Les arêtes vues et contours", "isCorrect": True},
                        {"text": "Les parties cachées", "isCorrect": False},
                        {"text": "Les cotes et les attaches", "isCorrect": False},
                        {"text": "Les axes de symétrie", "isCorrect": False}
                    ],
                    "correction": "Le trait fort est utilisé pour tout ce qui est visible au premier plan et les contours définitifs de l'objet, afin de les faire ressortir par rapport aux traits de construction ou de cotation."
                },
                {
                    "questionNumber": 38,
                    "question": "Sur un plan de fondation, comment est généralement représentée une semelle isolée sous un poteau ?",
                    "answerOptions": [
                        {"text": "Par un carré ou un rectangle hachuré", "isCorrect": True},
                        {"text": "Par deux traits parallèles continus", "isCorrect": False},
                        {"text": "Par un cercle avec une croix au centre", "isCorrect": False},
                        {"text": "Par une ligne en zigzag", "isCorrect": False}
                    ],
                    "correction": "La semelle isolée, qui supporte une charge ponctuelle (poteau), est représentée en vue de dessus par un carré ou un rectangle aux dimensions de la fondation, souvent avec des hachures ou un grisés."
                },
                {
                    "questionNumber": 39,
                    "question": "Si un point A est à l'altitude 12.50 m et un point B à 11.20 m, quelle est la différence de niveau ?",
                    "answerOptions": [
                        {"text": "1,30 m", "isCorrect": True},
                        {"text": "1,70 m", "isCorrect": False},
                        {"text": "0,30 m", "isCorrect": False},
                        {"text": "23,70 m", "isCorrect": False}
                    ],
                    "correction": "La différence de niveau (dénivelée) est une simple soustraction : 12,50 - 11,20 = 1,30 mètre."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle flèche indique le Nord sur un plan d'architecture ?",
                    "answerOptions": [
                        {"text": "La rose des vents", "isCorrect": True},
                        {"text": "La cotation cumulée", "isCorrect": False},
                        {"text": "La ligne de cote", "isCorrect": False},
                        {"text": "Le cartouche technique", "isCorrect": False}
                    ],
                    "correction": "La rose des vents ou une flèche spécifique indique l'orientation géographique (le Nord) pour permettre de situer l'ensoleillement et l'exposition du bâtiment."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : TECHNIQUES DE MAÇONNERIE ET MISE EN ŒUVRE (GROS ŒUVRE) (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : TECHNIQUES DE MAÇONNERIE ET MISE EN ŒUVRE (GROS ŒUVRE)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la fonction principale d'un linteau au-dessus d'une ouverture ?",
                    "answerOptions": [
                        {"text": "Supporter les charges supérieures", "isCorrect": True},
                        {"text": "Décorer la façade du bâtiment", "isCorrect": False},
                        {"text": "Isoler thermiquement la fenêtre", "isCorrect": False},
                        {"text": "Empêcher les intrusions par la baie", "isCorrect": False}
                    ],
                    "correction": "Le linteau est une poutre (en béton armé, bois ou acier) située au-dessus d'une baie. Son rôle structurel est de reprendre le poids du mur et du plancher situés au-dessus pour le transmettre aux jambages."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est l'épaisseur moyenne standard d'un joint de mortier traditionnel pour le montage de parpaings ?",
                    "answerOptions": [
                        {"text": "10 à 15 millimètres", "isCorrect": True},
                        {"text": "1 à 3 millimètres", "isCorrect": False},
                        {"text": "30 à 40 millimètres", "isCorrect": False},
                        {"text": "50 à 60 millimètres", "isCorrect": False}
                    ],
                    "correction": "Pour une maçonnerie traditionnelle d'éléments creux, l'épaisseur du joint doit permettre de rattraper les tolérances dimensionnelles des blocs, soit généralement entre 1 cm et 1,5 cm."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel outil le maçon utilise-t-il pour vérifier la verticalité parfaite d'un mur ?",
                    "answerOptions": [
                        {"text": "Le fil à plomb", "isCorrect": True},
                        {"text": "Le cordeau traceur", "isCorrect": False},
                        {"text": "Le double mètre", "isCorrect": False},
                        {"text": "L'équerre de maçon", "isCorrect": False}
                    ],
                    "correction": "Le fil à plomb utilise la gravité pour indiquer la verticale absolue (l'aplomb). C'est l'outil de référence indispensable pour monter des murs droits et vérifier les angles."
                },
                {
                    "questionNumber": 44,
                    "question": "Comment appelle-t-on la partie de mur située entre deux ouvertures sur une même façade ?",
                    "answerOptions": [
                        {"text": "Le trumeau", "isCorrect": True},
                        {"text": "L'allège", "isCorrect": False},
                        {"text": "Le linteau", "isCorrect": False},
                        {"text": "Le jambage", "isCorrect": False}
                    ],
                    "correction": "Le vocabulaire est précis : le trumeau est le pan de mur vertical qui sépare deux fenêtres ou portes. L'allège est sous la fenêtre, le linteau au-dessus."
                },
                {
                    "questionNumber": 45,
                    "question": "Pourquoi applique-t-on de l'huile de décoffrage sur les banches ou les planches avant de couler le béton ?",
                    "answerOptions": [
                        {"text": "Pour empêcher l'adhérence", "isCorrect": True},
                        {"text": "Pour colorer le béton", "isCorrect": False},
                        {"text": "Pour armer le mélange", "isCorrect": False},
                        {"text": "Pour coller le coffrage", "isCorrect": False}
                    ],
                    "correction": "L'agent de démoulage (huile) crée un film gras qui empêche le béton de coller au coffrage lors de la prise, facilitant ainsi le retrait du moule sans abîmer l'ouvrage."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le recouvrement minimum obligatoire (harpage) entre deux rangs de parpaings courants ?",
                    "answerOptions": [
                        {"text": "Le tiers de la longueur du bloc", "isCorrect": True},
                        {"text": "Le dixième de la longueur du bloc", "isCorrect": False},
                        {"text": "La totalité de la longueur du bloc", "isCorrect": False},
                        {"text": "Un seul centimètre de longueur", "isCorrect": False}
                    ],
                    "correction": "Pour assurer la solidité et la répartition des charges, les joints verticaux doivent être décalés d'un rang à l'autre d'au moins 1/3 de la longueur de l'élément (ou minimum 10 cm pour les petits éléments)."
                },
                {
                    "questionNumber": 47,
                    "question": "À quoi sert un 'rejingot' sur un appui de fenêtre ?",
                    "answerOptions": [
                        {"text": "Empêcher l'eau de rentrer", "isCorrect": True},
                        {"text": "Poser les volets battants", "isCorrect": False},
                        {"text": "Décorer le bas de la fenêtre", "isCorrect": False},
                        {"text": "Soutenir le poids du linteau", "isCorrect": False}
                    ],
                    "correction": "Le rejingot est le relief arrière (remontée) de l'appui de fenêtre. La traverse basse de la menuiserie vient s'y appuyer pour assurer une étanchéité parfaite à l'air et à l'eau."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel élément métallique utilise-t-on pour soutenir temporairement un coffrage de dalle ou de linteau ?",
                    "answerOptions": [
                        {"text": "Un étai", "isCorrect": True},
                        {"text": "Une serre", "isCorrect": False},
                        {"text": "Un clou", "isCorrect": False},
                        {"text": "Un fil", "isCorrect": False}
                    ],
                    "correction": "L'étai est une pièce métallique télescopique réglable en hauteur, capable de supporter de lourdes charges verticales le temps que le béton atteigne sa résistance suffisante."
                },
                {
                    "questionNumber": 49,
                    "question": "Dans quel sens doit-on poser les parpaings creux traditionnels lors du montage ?",
                    "answerOptions": [
                        {"text": "Fond vers le haut", "isCorrect": True},
                        {"text": "Alvéoles face latérale", "isCorrect": False},
                        {"text": "À la verticale debout", "isCorrect": False},
                        {"text": "Sur la tranche fine", "isCorrect": False}
                    ],
                    "correction": "Les parpaings se posent 'cul en l'air' (le fond plein vers le haut) pour offrir une surface plane facile à encoller pour le rang suivant, et pour que les alvéoles ne se remplissent pas de mortier (économie et isolation)."
                },
                {
                    "questionNumber": 50,
                    "question": "Qu'est-ce qu'une 'arase étanche' en bas de mur ?",
                    "answerOptions": [
                        {"text": "Une coupure de capillarité", "isCorrect": True},
                        {"text": "Une finition décorative", "isCorrect": False},
                        {"text": "Une isolation phonique", "isCorrect": False},
                        {"text": "Une couche de peinture", "isCorrect": False}
                    ],
                    "correction": "C'est une couche de mortier richement dosé et hydrofugé (ou une bande bitumineuse) posée au niveau du plancher bas pour empêcher l'humidité du sol de remonter dans les murs par capillarité."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la fonction du chainage vertical dans une construction en maçonnerie ?",
                    "answerOptions": [
                        {"text": "Contreventer l'ouvrage", "isCorrect": True},
                        {"text": "Isoler les parois", "isCorrect": False},
                        {"text": "Porter le plancher", "isCorrect": False},
                        {"text": "Drainer le sol", "isCorrect": False}
                    ],
                    "correction": "Les chainages verticaux (poteaux incorporés aux angles et refends) liaisonnent les fondations à la toiture. Ils empêchent les murs de s'écarter ou de se soulever, assurant la stabilité (contreventement) de la structure."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment nomme-t-on les faces verticales intérieures d'une ouverture de porte ou de fenêtre ?",
                    "answerOptions": [
                        {"text": "Les tableaux", "isCorrect": True},
                        {"text": "Les plafonds", "isCorrect": False},
                        {"text": "Les feuillures", "isCorrect": False},
                        {"text": "Les ébrasements", "isCorrect": False}
                    ],
                    "correction": "Le tableau est la face latérale de l'ouverture visible de l'extérieur. La largeur 'tableau' est la cote de passage libre horizontale entre les deux murs."
                },
                {
                    "questionNumber": 53,
                    "question": "Que doit-on impérativement utiliser pour maintenir l'écartement constant entre deux banches de coffrage ?",
                    "answerOptions": [
                        {"text": "Des entretoises", "isCorrect": True},
                        {"text": "De la colle", "isCorrect": False},
                        {"text": "Du scotch", "isCorrect": False},
                        {"text": "Du sable", "isCorrect": False}
                    ],
                    "correction": "Les entretoises (souvent des tubes PVC ou cônes avec tiges filetées) traversent le coffrage pour garantir que l'épaisseur du mur sera exactement celle prévue, malgré la pression du béton."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la particularité de la pose de briques à 'joints minces' (briques rectifiées) ?",
                    "answerOptions": [
                        {"text": "L'utilisation d'un mortier-colle", "isCorrect": True},
                        {"text": "L'usage de ciment prompt pur", "isCorrect": False},
                        {"text": "L'absence totale de liant", "isCorrect": False},
                        {"text": "L'obligation de mouiller la brique", "isCorrect": False}
                    ],
                    "correction": "Les briques rectifiées ont des dimensions très précises qui permettent un montage avec un joint très fin (1 à 3 mm) de mortier-colle appliqué au rouleau, améliorant l'isolation thermique (moins de ponts thermiques)."
                },
                {
                    "questionNumber": 55,
                    "question": "À quel moment doit-on réaliser les joints de finition sur un mur en briques apparentes ?",
                    "answerOptions": [
                        {"text": "En cours de montage ou juste après", "isCorrect": True},
                        {"text": "Une fois le mur totalement sec", "isCorrect": False},
                        {"text": "Avant de poser la première brique", "isCorrect": False},
                        {"text": "Uniquement l'année suivante", "isCorrect": False}
                    ],
                    "correction": "Les joints se font généralement 'à l'avancement' ou en 'rejointoiement' peu de temps après le montage, quand le mortier est encore frais mais a commencé sa prise ('tirer'), pour assurer une bonne adhérence et l'esthétique."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel accessoire assure la distance réglementaire entre le coffrage et les aciers ?",
                    "answerOptions": [
                        {"text": "La cale d'enrobage", "isCorrect": True},
                        {"text": "Le fil de ligature", "isCorrect": False},
                        {"text": "Le clou de maçon", "isCorrect": False},
                        {"text": "La barre de reprise", "isCorrect": False}
                    ],
                    "correction": "Les cales (en plastique ou béton) sont indispensables pour garantir que l'acier ne touchera pas le coffrage, assurant ainsi l'enrobage nécessaire pour protéger l'armature de la corrosion."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'appelle-t-on la 'feuillure' dans un jambage de fenêtre ?",
                    "answerOptions": [
                        {"text": "L'encoche pour recevoir la menuiserie", "isCorrect": True},
                        {"text": "La décoration en forme de feuille", "isCorrect": False},
                        {"text": "La fissure due au retrait", "isCorrect": False},
                        {"text": "La partie basse de l'appui", "isCorrect": False}
                    ],
                    "correction": "La feuillure est un décrochement (angle rentrant) réservé dans la maçonnerie pour y encastrer le dormant (cadre fixe) de la fenêtre ou de la porte."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle précaution prendre lors du coulage d'un poteau de grande hauteur ?",
                    "answerOptions": [
                        {"text": "Couler par passes successives vibrées", "isCorrect": True},
                        {"text": "Verser tout le béton d'un seul coup", "isCorrect": False},
                        {"text": "Ne jamais vibrer le béton vertical", "isCorrect": False},
                        {"text": "Ajouter beaucoup d'eau pour fluidifier", "isCorrect": False}
                    ],
                    "correction": "Pour éviter la ségrégation (les cailloux tombent au fond) et les nids de graviers, on doit couler le béton par couches (volées) régulières et vibrer chaque couche sans excès."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le rôle d'une 'planelle' en rive de plancher ?",
                    "answerOptions": [
                        {"text": "Servir de coffrage perdu", "isCorrect": True},
                        {"text": "Soutenir la dalle béton", "isCorrect": False},
                        {"text": "Remplacer le chainage", "isCorrect": False},
                        {"text": "Faire joli en façade", "isCorrect": False}
                    ],
                    "correction": "La planelle est un bloc de faible épaisseur (souvent 5 cm) posé en rive de mur extérieur. Elle sert de coffrage latéral pour la dalle de compression et assure la continuité du support d'enduit en façade."
                },
                {
                    "questionNumber": 60,
                    "question": "Pour réaliser un angle de mur parfait à 90°, quelle technique d'appareillage est prioritaire ?",
                    "answerOptions": [
                        {"text": "Le croisement des blocs", "isCorrect": True},
                        {"text": "La coupe en biseau", "isCorrect": False},
                        {"text": "L'ajout de ferraille", "isCorrect": False},
                        {"text": "Le collage simple", "isCorrect": False}
                    ],
                    "correction": "La solidité et la géométrie d'un angle reposent sur le harpage (croisement) : les blocs d'un mur doivent pénétrer dans l'autre mur alternativement à chaque rang pour 'verrouiller' l'angle."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : FINITIONS, OUVRAGES HORIZONTAUX ET TRAVAUX SPÉCIFIQUES (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : FINITIONS, OUVRAGES HORIZONTAUX ET TRAVAUX SPÉCIFIQUES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "De combien de couches se compose traditionnellement un enduit extérieur manuel ?",
                    "answerOptions": [
                        {"text": "Trois", "isCorrect": True},
                        {"text": "Une seule", "isCorrect": False},
                        {"text": "Cinq ou six", "isCorrect": False},
                        {"text": "Douze", "isCorrect": False}
                    ],
                    "correction": "L'enduit traditionnel se fait en 3 couches : 1. Le gobetis (accroche), 2. Le corps d'enduit (imperméabilisation et planéité), 3. La couche de finition (aspect esthétique)."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le rôle spécifique du gobetis dans la réalisation d'un enduit ?",
                    "answerOptions": [
                        {"text": "Assurer l'accrochage", "isCorrect": True},
                        {"text": "Donner la couleur finale de la façade visible depuis la rue", "isCorrect": False},
                        {"text": "Lisser parfaitement la surface du mur", "isCorrect": False},
                        {"text": "Isoler thermiquement le bâtiment", "isCorrect": False}
                    ],
                    "correction": "Le gobetis est une couche mince, riche en ciment et rugueuse. Elle sert d'interface d'adhérence entre le support (maçonnerie) et le corps d'enduit qui viendra ensuite."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle différence technique distingue une chape d'une dalle en béton ?",
                    "answerOptions": [
                        {"text": "La chape est une finition", "isCorrect": True},
                        {"text": "La chape contient du gros gravier", "isCorrect": False},
                        {"text": "La chape est toujours armée de gros aciers", "isCorrect": False},
                        {"text": "La chape porte les murs de la maison", "isCorrect": False}
                    ],
                    "correction": "La dalle est un élément structurel porteur (béton + graviers + ferraillage). La chape est une couche de mortier (sable + ciment) coulée sur la dalle pour niveler le sol avant la pose du carrelage."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle pente minimale doit-on respecter pour une canalisation d'eaux usées ?",
                    "answerOptions": [
                        {"text": "1 centimètre par mètre", "isCorrect": True},
                        {"text": "50 centimètres par mètre", "isCorrect": False},
                        {"text": "1 millimètre par kilomètre", "isCorrect": False},
                        {"text": "90 degrés de pente", "isCorrect": False}
                    ],
                    "correction": "Pour assurer un bon écoulement des matières sans stagnation (bouchons) ni érosion, une pente comprise entre 1 % (1 cm/m) et 3 % est recommandée par le DTU 60.11."
                },
                {
                    "questionNumber": 65,
                    "question": "À quoi sert un 'regard' installé sur un réseau de canalisations enterrées ?",
                    "answerOptions": [
                        {"text": "Inspecter le réseau", "isCorrect": True},
                        {"text": "Augmenter la pression de l'eau", "isCorrect": False},
                        {"text": "Stocker l'eau de pluie pour l'été", "isCorrect": False},
                        {"text": "Filtrer les bactéries présentes", "isCorrect": False}
                    ],
                    "correction": "Le regard de visite permet d'accéder aux canalisations aux endroits stratégiques (changements de direction, jonctions) pour le contrôle, le curage et le débouchage éventuel."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le rôle principal du film polyane placé sous un dallage sur terre-plein ?",
                    "answerOptions": [
                        {"text": "Bloquer les remontées d'humidité", "isCorrect": True},
                        {"text": "Améliorer l'acoustique de la pièce", "isCorrect": False},
                        {"text": "Coller le béton au sol naturel", "isCorrect": False},
                        {"text": "Renforcer la résistance du béton", "isCorrect": False}
                    ],
                    "correction": "Le film polyane (ou pare-vapeur) crée une barrière étanche qui empêche l'humidité naturelle du sol de remonter par capillarité dans la dalle en béton."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la hauteur maximale autorisée pour un seuil de porte accessible aux personnes handicapées (PMR) ?",
                    "answerOptions": [
                        {"text": "2 centimètres", "isCorrect": True},
                        {"text": "10 centimètres", "isCorrect": False},
                        {"text": "15 centimètres", "isCorrect": False},
                        {"text": "20 centimètres", "isCorrect": False}
                    ],
                    "correction": "La réglementation sur l'accessibilité impose que les ressauts (seuils de portes-fenêtres ou d'entrée) ne dépassent pas 2 cm pour permettre le passage d'un fauteuil roulant."
                },
                {
                    "questionNumber": 68,
                    "question": "Qu'est-ce qu'un pont thermique dans une construction ?",
                    "answerOptions": [
                        {"text": "Une zone de fuite de chaleur", "isCorrect": True},
                        {"text": "Un système de chauffage par le sol très performant", "isCorrect": False},
                        {"text": "Une passerelle reliant deux bâtiments", "isCorrect": False},
                        {"text": "Un isolant ultra efficace", "isCorrect": False}
                    ],
                    "correction": "Un pont thermique est une discontinuité dans l'isolation (jonction dalle/mur, angles) par laquelle la chaleur s'échappe plus vite que par le reste des parois, créant des points froids."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel outil manuel utilise-t-on pour réaliser la finition d'un enduit gratté ?",
                    "answerOptions": [
                        {"text": "Le gratton", "isCorrect": True},
                        {"text": "La truelle", "isCorrect": False},
                        {"text": "Le marteau", "isCorrect": False},
                        {"text": "Le niveau", "isCorrect": False}
                    ],
                    "correction": "Le gratton est une planche garnie de pointes. On l'utilise quand l'enduit a commencé sa prise pour griffer la surface et obtenir l'aspect 'gratté' caractéristique."
                },
                {
                    "questionNumber": 70,
                    "question": "Sur quel matériau pose-t-on des bordures de trottoir pour les sceller ?",
                    "answerOptions": [
                        {"text": "Un lit de béton", "isCorrect": True},
                        {"text": "Du sable fin sec", "isCorrect": False},
                        {"text": "De la terre végétale", "isCorrect": False},
                        {"text": "Des copeaux de bois", "isCorrect": False}
                    ],
                    "correction": "Les bordures doivent être calées au béton (lit de pose + épaulement arrière) pour résister aux chocs et à la poussée des véhicules ou de la chaussée."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle couleur de grillage avertisseur signale une canalisation d'eau potable enterrée ?",
                    "answerOptions": [
                        {"text": "Bleu", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False}
                    ],
                    "correction": "Le code couleur normalisé est impératif : Bleu pour l'eau, Rouge pour l'électricité, Jaune pour le gaz, Vert pour les télécoms."
                },
                {
                    "questionNumber": 72,
                    "question": "Que désigne le terme 'barbotine' en maçonnerie ?",
                    "answerOptions": [
                        {"text": "Un mélange liquide de ciment et d'eau", "isCorrect": True},
                        {"text": "Un béton très riche en gros cailloux", "isCorrect": False},
                        {"text": "Une brique cassée en deux morceaux", "isCorrect": False},
                        {"text": "Un outil pour lisser les joints", "isCorrect": False}
                    ],
                    "correction": "La barbotine est un coulis de liant pur (ciment ou chaux) et d'eau. Elle est utilisée pour coller du carrelage en pose scellée ou pour assurer l'accrochage entre deux couches de béton frais."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le but d'un joint de dilatation dans une grande dalle béton ?",
                    "answerOptions": [
                        {"text": "Absorber les mouvements", "isCorrect": True},
                        {"text": "Faire joli au milieu de la pièce", "isCorrect": False},
                        {"text": "Économiser du béton au coulage", "isCorrect": False},
                        {"text": "Permettre le passage des câbles", "isCorrect": False}
                    ],
                    "correction": "Les matériaux se dilatent avec la chaleur. Le joint de dilatation sectionne l'ouvrage pour permettre au béton de bouger sans provoquer de fissuration aléatoire ou de soulèvement."
                },
                {
                    "questionNumber": 74,
                    "question": "À quoi sert la 'règle à dresser' lors de l'application d'un enduit ?",
                    "answerOptions": [
                        {"text": "Aplanir le corps d'enduit", "isCorrect": True},
                        {"text": "Mesurer la quantité de sable", "isCorrect": False},
                        {"text": "Nettoyer les outils en fin de journée", "isCorrect": False},
                        {"text": "Compter les sacs de ciment utilisés", "isCorrect": False}
                    ],
                    "correction": "La règle en aluminium (souvent de 2m) permet de 'dresser' le mur, c'est-à-dire de couper les bosses et combler les creux pour obtenir une surface parfaitement plane."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle est la fonction d'un produit de ragréage autolissant ?",
                    "answerOptions": [
                        {"text": "Corriger les défauts de planéité d'un sol", "isCorrect": True},
                        {"text": "Construire un mur en parpaings", "isCorrect": False},
                        {"text": "Isoler les combles de la maison", "isCorrect": False},
                        {"text": "Peindre les plafonds en blanc", "isCorrect": False}
                    ],
                    "correction": "Le ragréage est un mortier très fluide que l'on coule sur un sol irrégulier. Il s'étale tout seul par gravité pour créer une surface parfaitement lisse et horizontale avant la pose du revêtement."
                },
                {
                    "questionNumber": 76,
                    "question": "Où doit-on placer le drain périphérique par rapport aux fondations ?",
                    "answerOptions": [
                        {"text": "Contre la semelle sans descendre plus bas", "isCorrect": True},
                        {"text": "Au-dessus du niveau du terrain naturel", "isCorrect": False},
                        {"text": "Juste sous la toiture du bâtiment", "isCorrect": False},
                        {"text": "Directement dans le béton de la fondation", "isCorrect": False}
                    ],
                    "correction": "Le drain se pose en bas de mur, sur la cunette ou à côté de la semelle, mais jamais plus bas que la base de la fondation pour ne pas déstabiliser l'assise du bâtiment."
                },
                {
                    "questionNumber": 77,
                    "question": "Comment appelle-t-on le procédé consistant à compacter le sol avant de couler une dalle ?",
                    "answerOptions": [
                        {"text": "Le compactage", "isCorrect": True},
                        {"text": "Le nivellement", "isCorrect": False},
                        {"text": "Le surfaçage", "isCorrect": False},
                        {"text": "Le pilonnage", "isCorrect": False}
                    ],
                    "correction": "Le compactage (avec une plaque vibrante ou un rouleau) est essentiel pour garantir la stabilité de l'assise et éviter le tassement futur de la dalle."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le rôle des 'couvre-joints' en façade ?",
                    "answerOptions": [
                        {"text": "Cacher les joints de dilatation", "isCorrect": True},
                        {"text": "Accélérer la prise de l'enduit", "isCorrect": False},
                        {"text": "Renforcer la maçonnerie", "isCorrect": False},
                        {"text": "Servir de guide pour le crépi", "isCorrect": False}
                    ],
                    "correction": "Les couvre-joints sont des profilés (métalliques ou PVC) utilisés pour masquer l'espace libre laissé par les joints de dilatation ou de rupture tout en permettant le mouvement de la structure."
                },
                {
                    "questionNumber": 79,
                    "question": "Qu'est-ce qu'une 'pente à la romaine' sur une terrasse ?",
                    "answerOptions": [
                        {"text": "Une pente douce vers l'extérieur", "isCorrect": True},
                        {"text": "Une pente très forte vers le centre", "isCorrect": False},
                        {"text": "Une pente irrégulière et aléatoire", "isCorrect": False},
                        {"text": "Un sol parfaitement plat", "isCorrect": False}
                    ],
                    "correction": "La pente à la romaine (ou 'à l'italienne') consiste à donner une légère inclinaison au sol vers l'extérieur pour faciliter l'évacuation de l'eau."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la principale fonction du 'mortier de montage' pour les murs ?",
                    "answerOptions": [
                        {"text": "Lier les éléments de maçonnerie et niveler", "isCorrect": True},
                        {"text": "Faire l'enduit de finition", "isCorrect": False},
                        {"text": "Isoler phoniquement le mur", "isCorrect": False},
                        {"text": "Servir d'isolant thermique", "isCorrect": False}
                    ],
                    "correction": "Le mortier sert à coller les blocs entre eux et à assurer l'horizontalité (le niveau) de chaque rang de maçonnerie."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : GESTION, SANTÉ ET ENVIRONNEMENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : GESTION, SANTÉ ET ENVIRONNEMENT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel document liste les produits commandés par le magasin ?",
                    "answerOptions": [
                        {"text": "Le bon de commande", "isCorrect": True},
                        {"text": "Le bon de livraison", "isCorrect": False},
                        {"text": "La facture", "isCorrect": False},
                        {"text": "Le ticket de caisse", "isCorrect": False}
                    ],
                    "correction": "Le bon de commande est le document qui matérialise l'intention d'achat du magasin auprès du fournisseur."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment calcule-t-on la marge commerciale brute (en valeur) ?",
                    "answerOptions": [
                        {"text": "Prix de vente HT - Coût d'achat HT", "isCorrect": True},
                        {"text": "Prix de vente TTC - Coût d'achat TTC", "isCorrect": False},
                        {"text": "Coût d'achat + Charges fixes", "isCorrect": False},
                        {"text": "Chiffre d'affaires / Nombre de clients", "isCorrect": False}
                    ],
                    "correction": "La marge brute est le profit généré avant la déduction des charges de structure."
                },
                {
                    "questionNumber": 83,
                    "question": "Que signifie le sigle LIFO dans la gestion des stocks ?",
                    "answerOptions": [
                        {"text": "Last In, First Out (Dernier entré, premier sorti)", "isCorrect": True},
                        {"text": "Le produit le plus cher sort en premier", "isCorrect": False},
                        {"text": "La méthode de sortie des produits périssables", "isCorrect": False},
                        {"text": "Le premier entré sort en premier (FIFO)", "isCorrect": False}
                    ],
                    "correction": "Le LIFO est une méthode de valorisation des stocks : le coût du dernier article acheté est imputé à la première vente."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel taux de TVA s'applique aux travaux de rénovation de logements anciens (moins de 2 ans) ?",
                    "answerOptions": [
                        {"text": "10 %", "isCorrect": True},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "5,5 %", "isCorrect": False},
                        {"text": "2,1 %", "isCorrect": False}
                    ],
                    "correction": "Le taux intermédiaire de 10% s'applique aux travaux d'amélioration, de transformation, d'aménagement et d'entretien."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle maladie professionnelle est liée au bruit excessif des machines (bétonnière, disqueuse) ?",
                    "answerOptions": [
                        {"text": "La surdité", "isCorrect": True},
                        {"text": "L'acouphène", "isCorrect": False},
                        {"text": "La cataracte", "isCorrect": False},
                        {"text": "L'hygroma", "isCorrect": False}
                    ],
                    "correction": "Les bruits supérieurs à 85 dB peuvent causer des dommages irréversibles à l'oreille interne (surdité, acouphènes)."
                },
                {
                    "questionNumber": 86,
                    "question": "Que désigne la 'démarque inconnue' ?",
                    "answerOptions": [
                        {"text": "Les pertes de stock (vol, casse, erreurs) non justifiées", "isCorrect": True},
                        {"text": "Les invendus du magasin", "isCorrect": False},
                        {"text": "La casse enregistrée après contrôle", "isCorrect": False},
                        {"text": "Le manque de personnel", "isCorrect": False}
                    ],
                    "correction": "La démarque inconnue est l'écart entre le stock théorique et le stock réel, souvent causé par le vol ou des erreurs non documentées."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel document doit être rédigé avant le démarrage de tout chantier par l'entreprise ?",
                    "answerOptions": [
                        {"text": "Le Plan de Prévention (si intervention sur site tiers)", "isCorrect": True},
                        {"text": "Le Bon de Commande", "isCorrect": False},
                        {"text": "L'Attestation d'Assurance", "isCorrect": False},
                        {"text": "Le CCTP", "isCorrect": False}
                    ],
                    "correction": "Le Plan de Prévention (ou PPSPS sur les gros chantiers) définit les règles de sécurité spécifiques à l'environnement de travail, essentiel pour les travaux en co-activité."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment appelle-t-on l'usure ou la dépréciation progressive du matériel (bétonnière, camion) ?",
                    "answerOptions": [
                        {"text": "L'amortissement", "isCorrect": True},
                        {"text": "La fiscalité", "isCorrect": False},
                        {"text": "Le bénéfice", "isCorrect": False},
                        {"text": "La marge", "isCorrect": False}
                    ],
                    "correction": "L'amortissement est la constatation comptable de la perte de valeur d'un bien due à l'usage et au temps."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est l'objectif principal du tri des déchets sur un chantier de maçonnerie ?",
                    "answerOptions": [
                        {"text": "Le recyclage des matériaux inertes", "isCorrect": True},
                        {"text": "La décoration du chantier", "isCorrect": False},
                        {"text": "La lutte contre le bruit", "isCorrect": False},
                        {"text": "Le gain de temps au déchargement", "isCorrect": False}
                    ],
                    "correction": "Les déchets inertes (gravats, béton, tuiles) et les déchets non dangereux (bois, plastiques) doivent être triés pour leur valorisation et leur recyclage."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel taux de TVA s'applique aux travaux de construction neuve ?",
                    "answerOptions": [
                        {"text": "20 %", "isCorrect": True},
                        {"text": "10 %", "isCorrect": False},
                        {"text": "5,5 %", "isCorrect": False},
                        {"text": "0 %", "isCorrect": False}
                    ],
                    "correction": "Les travaux de construction neuve sont soumis au taux normal de 20 %."
                },
                {
                    "questionNumber": 91,
                    "question": "Le port du casque avec jugulaire est obligatoire pour prévenir quel risque ?",
                    "answerOptions": [
                        {"text": "La chute d'objets ou le heurt de la tête", "isCorrect": True},
                        {"text": "Le bruit excessif", "isCorrect": False},
                        {"text": "Les brûlures chimiques", "isCorrect": False},
                        {"text": "Les coupures", "isCorrect": False}
                    ],
                    "correction": "Le casque protège la tête contre les chutes d'objets (dynamique) et les chocs directs. La jugulaire évite qu'il ne tombe lors des mouvements ou des chutes."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le risque lié au stockage de ciment périmé (éventé) sur chantier ?",
                    "answerOptions": [
                        {"text": "Baisse drastique de la résistance mécanique du béton", "isCorrect": True},
                        {"text": "Augmentation de la vitesse de prise du béton", "isCorrect": False},
                        {"text": "Changement de couleur du béton au rose", "isCorrect": False},
                        {"text": "Contamination du sable par les moisissures", "isCorrect": False}
                    ],
                    "correction": "Le ciment éventé (ayant pris l'humidité de l'air) a déjà réagi et n'offre plus la résistance attendue une fois gâché avec l'eau de gâchage."
                },
                {
                    "questionNumber": 93,
                    "question": "Quelle est la pénalité principale pour une entreprise qui ne respecte pas les délais contractuels ?",
                    "answerOptions": [
                        {"text": "Des pénalités de retard", "isCorrect": True},
                        {"text": "L'arrêt immédiat du chantier", "isCorrect": False},
                        {"text": "Une amende fixe de 1000 euros", "isCorrect": False},
                        {"text": "Le licenciement du chef de chantier", "isCorrect": False}
                    ],
                    "correction": "Les pénalités de retard (souvent un pourcentage du marché par jour) sont prévues dans les CCTP."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le risque lié au stockage de ciment périmé (éventé) sur chantier ?",
                    "answerOptions": [
                        {"text": "Baisse drastique de la résistance mécanique du béton", "isCorrect": True},
                        {"text": "Augmentation de la vitesse de prise du béton", "isCorrect": False},
                        {"text": "Changement de couleur du béton au rose", "isCorrect": False},
                        {"text": "Contamination du sable par les moisissures", "isCorrect": False}
                    ],
                    "correction": "Le ciment éventé (ayant pris l'humidité de l'air) a déjà réagi et n'offre plus la résistance attendue une fois gâché avec l'eau de gâchage."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le risque chimique principal lié à la manipulation de mortier frais ?",
                    "answerOptions": [
                        {"text": "Les brûlures basiques (alcalines) de la peau", "isCorrect": True},
                        {"text": "L'hypothermie des mains", "isCorrect": False},
                        {"text": "La coupe par les grains de sable", "isCorrect": False},
                        {"text": "L'explosion de la gâchée", "isCorrect": False}
                    ],
                    "correction": "Le ciment est très alcalin (pH élevé). Le contact prolongé sans gants provoque des brûlures par caustification."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la durée de validité de l'attestation d'aptitude médicale pour un salarié exposé à des risques (ex: travail en hauteur) ?",
                    "answerOptions": [
                        {"text": "5 ans (sauf avis contraire du médecin)", "isCorrect": True},
                        {"text": "1 an", "isCorrect": False},
                        {"text": "3 mois", "isCorrect": False},
                        {"text": "10 ans", "isCorrect": False}
                    ],
                    "correction": "La visite médicale de renouvellement est de 5 ans, mais elle peut être raccourcie selon les risques ou l'âge du travailleur."
                },
                {
                    "questionNumber": 97,
                    "question": "Le risque de 'choc thermique' lors du coulage du béton neuf est lié à :",
                    "answerOptions": [
                        {"text": "Une différence de température trop forte entre la reprise et le nouveau béton", "isCorrect": True},
                        {"text": "La foudre qui tombe sur le chantier", "isCorrect": False},
                        {"text": "L'utilisation de trop d'eau froide", "isCorrect": False},
                        {"text": "Le chauffage excessif du coffrage", "isCorrect": False}
                    ],
                    "correction": "Un choc thermique peut provoquer des microfissures. On limite les écarts de température entre deux coulages (reprise de bétonnage) à moins de 10°C."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le risque immédiat lié au coulage de béton sur une zone non délimitée ou sans protection latérale ?",
                    "answerOptions": [
                        {"text": "La projection de ciment dans les yeux des passants", "isCorrect": True},
                        {"text": "Le tassement ultérieur du béton", "isCorrect": False},
                        {"text": "La ségrégation du mélange", "isCorrect": False},
                        {"text": "L'écroulement de la structure", "isCorrect": False}
                    ],
                    "correction": "La projection de ciment (produit caustique) dans les yeux d'un passant (risque chimique) dans un chantier ouvert est le danger le plus fréquent."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le délai de garantie légale du parfait achèvement après la réception des travaux ?",
                    "answerOptions": [
                        {"text": "1 an", "isCorrect": True},
                        {"text": "2 ans", "isCorrect": False},
                        {"text": "10 ans", "isCorrect": False},
                        {"text": "30 jours", "isCorrect": False}
                    ],
                    "correction": "Le parfait achèvement couvre les défauts signalés à la réception ou durant l'année qui suit."
                },
                {
                    "questionNumber": 100,
                    "question": "Les déchets de bois et les gravats inertes doivent être jetés dans :",
                    "answerOptions": [
                        {"text": "Des bennes séparées", "isCorrect": True},
                        {"text": "La même benne (tous les déchets ensemble)", "isCorrect": False},
                        {"text": "Un trou au fond du jardin", "isCorrect": False},
                        {"text": "La poubelle de bureau", "isCorrect": False}
                    ],
                    "correction": "Le tri sélectif est obligatoire. Le bois est un Déchet Non Dangereux (DND) valorisable, les gravats sont des Déchets Inertes. Ils ne doivent pas être mélangés."
                }
            ]
        }
    }
}