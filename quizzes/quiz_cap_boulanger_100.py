quiz_data = {
    "title": "Quiz CAP Boulanger : Technologie, Techniques, Sciences et Gestion (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE DES MATIÈRES PREMIÈRES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE DES MATIÈRES PREMIÈRES (Questions 1 à 20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la teneur approximative en cendres d'une farine T55 ?",
                    "answerOptions": [
                        {"text": "0,55 %", "isCorrect": True},
                        {"text": "Entre 1,2 % et 1,5 % de matières minérales totales après incinération", "isCorrect": False},
                        {"text": "Environ 10 grammes par kilo", "isCorrect": False},
                        {"text": "0,1 %", "isCorrect": False}
                    ],
                    "correction": "Le 'Type' indique le taux de cendres (minéraux contenus dans le son). T55 signifie environ 0,55% de résidus minéraux. C'est la farine blanche classique."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle partie du grain de blé représente environ 82% du poids et contient l'amidon ?",
                    "answerOptions": [
                        {"text": "L'amande farineuse", "isCorrect": True},
                        {"text": "Les enveloppes périphériques et le péricarpe", "isCorrect": False},
                        {"text": "Le germe (embryon)", "isCorrect": False},
                        {"text": "L'assise protéique", "isCorrect": False}
                    ],
                    "correction": "C'est le cœur du grain. Lors de la mouture, on cherche à séparer cette amande (farine) des enveloppes (son)."
                },
                {
                    "questionNumber": 3,
                    "question": "Le gluten est formé par l'association de l'eau et de quelles protéines ?",
                    "answerOptions": [
                        {"text": "Gliadines et Gluténines", "isCorrect": True},
                        {"text": "Globulines et Albumines solubles", "isCorrect": False},
                        {"text": "Amylose et Amylopectine", "isCorrect": False},
                        {"text": "Acides aminés essentiels", "isCorrect": False}
                    ],
                    "correction": "Les gliadines (extensibilité) et les gluténines (élasticité/ténacité) sont insolubles dans l'eau. Elles se lient lors du pétrissage pour former le réseau glutineux."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel rôle joue le sel sur la levure ?",
                    "answerOptions": [
                        {"text": "Il régule la fermentation", "isCorrect": True},
                        {"text": "Il accélère la production de gaz carbonique", "isCorrect": False},
                        {"text": "Il tue instantanément les cellules", "isCorrect": False},
                        {"text": "Il la nourrit", "isCorrect": False}
                    ],
                    "correction": "Le sel a un pouvoir hygroscopique et antiseptique léger qui freine l'activité de la levure, empêchant la pâte de lever trop vite (rôle régulateur)."
                },
                {
                    "questionNumber": 5,
                    "question": "L'acide ascorbique (E300) sert à :",
                    "answerOptions": [
                        {"text": "Augmenter la ténacité et la force de la pâte", "isCorrect": True},
                        {"text": "Donner un goût citronné au pain", "isCorrect": False},
                        {"text": "Conserver le pain plus longtemps", "isCorrect": False},
                        {"text": "Colorer la mie en jaune", "isCorrect": False}
                    ],
                    "correction": "C'est un oxydant (Vitamine C). Il renforce le réseau de gluten, permettant aux pains de mieux tenir et d'avoir plus de volume."
                },
                {
                    "questionNumber": 6,
                    "question": "Une eau 'dure' est riche en :",
                    "answerOptions": [
                        {"text": "Sels de calcium", "isCorrect": True},
                        {"text": "Nitrates et phosphates", "isCorrect": False},
                        {"text": "Chlore", "isCorrect": False},
                        {"text": "Sodium", "isCorrect": False}
                    ],
                    "correction": "Une eau dure (calcaire) renforce le gluten, rendant la pâte plus rigide et la fermentation un peu plus lente."
                },
                {
                    "questionNumber": 7,
                    "question": "La levure biologique produit une fermentation :",
                    "answerOptions": [
                        {"text": "Alcoolique", "isCorrect": True},
                        {"text": "Lactique", "isCorrect": False},
                        {"text": "Acétique", "isCorrect": False},
                        {"text": "Butyrique", "isCorrect": False}
                    ],
                    "correction": "La levure transforme les sucres en CO2 (gaz) et en alcool éthylique (éthanol), d'où le nom de fermentation alcoolique."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle farine contient le plus de son ?",
                    "answerOptions": [
                        {"text": "T150", "isCorrect": True},
                        {"text": "La farine de Type 55", "isCorrect": False},
                        {"text": "T65", "isCorrect": False},
                        {"text": "T45", "isCorrect": False}
                    ],
                    "correction": "T150 = Farine intégrale (tout le grain, y compris toutes les enveloppes). T45 = Farine la plus pure/blanche."
                },
                {
                    "questionNumber": 9,
                    "question": "L'excès d'eau dans une pâte provoque :",
                    "answerOptions": [
                        {"text": "Un relâchement de la pâte et un collage", "isCorrect": True},
                        {"text": "Une pâte très dure et sèche", "isCorrect": False},
                        {"text": "Une croûte très épaisse", "isCorrect": False},
                        {"text": "Une absence de fermentation", "isCorrect": False}
                    ],
                    "correction": "Une hydratation excessive affaiblit le réseau de gluten. La pâte manque de tenue, s'étale et colle aux mains."
                },
                {
                    "questionNumber": 10,
                    "question": "Les sucres préexistants dans la farine représentent environ :",
                    "answerOptions": [
                        {"text": "1 % à 2 %", "isCorrect": True},
                        {"text": "15 %", "isCorrect": False},
                        {"text": "50 %", "isCorrect": False},
                        {"text": "0 %", "isCorrect": False}
                    ],
                    "correction": "La farine contient peu de sucres simples naturellement. C'est l'action des enzymes sur l'amidon qui va produire le maltose nécessaire à la levure par la suite."
                },
                {
                    "questionNumber": 11,
                    "question": "Le 'pain de tradition française' (Décret 1993) contient-il de l'acide ascorbique ?",
                    "answerOptions": [
                        {"text": "Non, c'est interdit", "isCorrect": True},
                        {"text": "Oui, obligatoirement", "isCorrect": False},
                        {"text": "Oui, jusqu'à 0,5%", "isCorrect": False},
                        {"text": "Seulement en hiver", "isCorrect": False}
                    ],
                    "correction": "Le Décret de 1993 interdit tout additif chimique dans le pain de tradition. Seuls la farine, l'eau, le sel, la levure/levain et certains adjuvants naturels (farine de fève/soja, gluten) sont autorisés."
                },
                {
                    "questionNumber": 12,
                    "question": "Le 'bassinage' consiste à :",
                    "answerOptions": [
                        {"text": "Ajouter de l'eau en fin de pétrissage", "isCorrect": True},
                        {"text": "Tremper les mains dans l'eau", "isCorrect": False},
                        {"text": "Laver le matériel", "isCorrect": False},
                        {"text": "Mettre la pâte au frais", "isCorrect": False}
                    ],
                    "correction": "Cette technique permet d'assouplir la pâte sans dégrader le gluten formé, favorisant une mie ouverte et alvéolée."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel ingrédient retarde le rassissement du pain de mie ?",
                    "answerOptions": [
                        {"text": "La matière grasse", "isCorrect": True},
                        {"text": "Le sel", "isCorrect": False},
                        {"text": "La levure", "isCorrect": False},
                        {"text": "L'eau seule", "isCorrect": False}
                    ],
                    "correction": "Les lipides (beurre, huile) et les sucres hygroscopiques retiennent l'humidité et empêchent l'amidon de rétrograder trop vite."
                },
                {
                    "questionNumber": 14,
                    "question": "La température mortelle pour la levure est de :",
                    "answerOptions": [
                        {"text": "50°C", "isCorrect": True},
                        {"text": "30°C", "isCorrect": False},
                        {"text": "100°C", "isCorrect": False},
                        {"text": "10°C", "isCorrect": False}
                    ],
                    "correction": "Au-delà de 50°C, les cellules de Saccharomyces cerevisiae sont détruites. C'est pourquoi l'eau de coulage ne doit pas être brûlante."
                },
                {
                    "questionNumber": 15,
                    "question": "Pour la pâtisserie et la viennoiserie fine, on privilégie la farine :",
                    "answerOptions": [
                        {"text": "T45", "isCorrect": True},
                        {"text": "T80", "isCorrect": False},
                        {"text": "T110", "isCorrect": False},
                        {"text": "T150", "isCorrect": False}
                    ],
                    "correction": "On cherche la pureté maximale (pas de son) pour ne pas griser la pâte et avoir un réseau de gluten parfait pour le feuilletage."
                },
                {
                    "questionNumber": 16,
                    "question": "Le lait apporte à la pâte :",
                    "answerOptions": [
                        {"text": "Sucre, gras et couleur", "isCorrect": True},
                        {"text": "De l'acidité", "isCorrect": False},
                        {"text": "Du croquant", "isCorrect": False},
                        {"text": "Rien de spécial", "isCorrect": False}
                    ],
                    "correction": "Le lactose caramélise à la cuisson (couleur), les matières grasses du lait assouplissent la mie."
                },
                {
                    "questionNumber": 17,
                    "question": "Les enzymes 'amylases' dégradent :",
                    "answerOptions": [
                        {"text": "L'amidon", "isCorrect": True},
                        {"text": "Le gluten", "isCorrect": False},
                        {"text": "Le gras", "isCorrect": False},
                        {"text": "Les vitamines", "isCorrect": False}
                    ],
                    "correction": "Elles coupent les longues chaînes d'amidon en sucres plus simples (maltose) fermentescibles."
                },
                {
                    "questionNumber": 18,
                    "question": "Qu'est-ce que le 'malt' ?",
                    "answerOptions": [
                        {"text": "Une farine d'orge germé riche en enzymes", "isCorrect": True},
                        {"text": "Un sucre artificiel", "isCorrect": False},
                        {"text": "Un colorant rouge", "isCorrect": False},
                        {"text": "Une graisse végétale", "isCorrect": False}
                    ],
                    "correction": "Le malt diastasique est ajouté pour corriger les farines pauvres en enzymes et booster la fermentation."
                },
                {
                    "questionNumber": 19,
                    "question": "Le son est principalement composé de :",
                    "answerOptions": [
                        {"text": "Cellulose (fibres)", "isCorrect": True},
                        {"text": "Amidon pur", "isCorrect": False},
                        {"text": "Gluten", "isCorrect": False},
                        {"text": "Sucre rapide", "isCorrect": False}
                    ],
                    "correction": "Ce sont les enveloppes du grain, riches en fibres insolubles et minéraux."
                },
                {
                    "questionNumber": 20,
                    "question": "Une farine 'de force' a un W (Alvéographe) :",
                    "answerOptions": [
                        {"text": "Supérieur à 250", "isCorrect": True},
                        {"text": "Inférieur à 100", "isCorrect": False},
                        {"text": "Égal à 0", "isCorrect": False},
                        {"text": "Négatif", "isCorrect": False}
                    ],
                    "correction": "Le W mesure la force boulangère. Une farine de force (riche en bon gluten) est nécessaire pour supporter les longues fermentations ou le travail riche (beurre/œufs)."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : PANIFICATION ET TECHNIQUES (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : PANIFICATION ET TECHNIQUES (Questions 21 à 40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "L'autolyse se pratique :",
                    "answerOptions": [
                        {"text": "Avant le pétrissage, mélange farine + eau seul", "isCorrect": True},
                        {"text": "Après la cuisson", "isCorrect": False},
                        {"text": "Pendant le pointage", "isCorrect": False},
                        {"text": "Au moment du façonnage", "isCorrect": False}
                    ],
                    "correction": "Ce repos (de 30 min à plusieurs heures) permet au gluten de s'hydrater naturellement et aux enzymes de travailler, rendant la pâte plus extensible."
                },
                {
                    "questionNumber": 22,
                    "question": "Le pointage est :",
                    "answerOptions": [
                        {"text": "La première fermentation en masse (en cuve)", "isCorrect": True},
                        {"text": "La pesée des pâtons", "isCorrect": False},
                        {"text": "La mise au four", "isCorrect": False},
                        {"text": "La division des pâtons", "isCorrect": False}
                    ],
                    "correction": "C'est l'étape clé pour la création des arômes et la prise de force de la pâte (ténacité), située juste après le pétrissage."
                },
                {
                    "questionNumber": 23,
                    "question": "Le frasage dure environ :",
                    "answerOptions": [
                        {"text": "3 à 5 minutes en vitesse lente", "isCorrect": True},
                        {"text": "20 minutes en vitesse rapide", "isCorrect": False},
                        {"text": "30 secondes", "isCorrect": False},
                        {"text": "1 heure", "isCorrect": False}
                    ],
                    "correction": "C'est juste le temps nécessaire pour mélanger l'eau et la farine de manière homogène avant de commencer le pétrissage actif."
                },
                {
                    "questionNumber": 24,
                    "question": "Pour obtenir une pâte à 24°C avec une T° Base de 54°C, une T° Air de 20°C et T° Farine de 20°C, l'eau doit être à :",
                    "answerOptions": [
                        {"text": "14°C", "isCorrect": True},
                        {"text": "10°C", "isCorrect": False},
                        {"text": "4°C", "isCorrect": False},
                        {"text": "24°C", "isCorrect": False}
                    ],
                    "correction": "Calcul : T° Eau = T° Base - (T° Air + T° Farine). 54 - (20 + 20) = 54 - 40 = 14°C."
                },
                {
                    "questionNumber": 25,
                    "question": "La 'clé' du pain lors du façonnage est :",
                    "answerOptions": [
                        {"text": "L'endroit où les bords de la pâte se rejoignent (la soudure)", "isCorrect": True},
                        {"text": "Un outil en métal", "isCorrect": False},
                        {"text": "Le dessus du pain", "isCorrect": False},
                        {"text": "Le poids du pain", "isCorrect": False}
                    ],
                    "correction": "La clé doit généralement être placée dessous lors de la mise sur couche ou plaque pour éviter que le pain ne s'ouvre par là à la cuisson."
                },
                {
                    "questionNumber": 26,
                    "question": "La buée injectée au four sert à :",
                    "answerOptions": [
                        {"text": "Favoriser le développement, la finesse de la croûte et la brillance", "isCorrect": True},
                        {"text": "Cuire l'intérieur du pain", "isCorrect": False},
                        {"text": "Laver les vitres du four", "isCorrect": False},
                        {"text": "Empêcher le pain de brûler", "isCorrect": False}
                    ],
                    "correction": "Sans humidité au début de la cuisson, la croûte se forme trop vite et bloque le gonflement du pain, qui devient terne et gris."
                },
                {
                    "questionNumber": 27,
                    "question": "Le ressuage est l'étape de :",
                    "answerOptions": [
                        {"text": "Refroidissement du pain après cuisson", "isCorrect": True},
                        {"text": "Seconde cuisson", "isCorrect": False},
                        {"text": "Fermentation finale", "isCorrect": False},
                        {"text": "Stockage au congélateur", "isCorrect": False}
                    ],
                    "correction": "Le pain perd environ 1 à 2% de son poids en eau. Il doit être sur grille pour que l'humidité s'échappe sans ramollir la croûte."
                },
                {
                    "questionNumber": 28,
                    "question": "Le coup de lame (scarification) doit être fait :",
                    "answerOptions": [
                        {"text": "Juste avant l'enfournement", "isCorrect": True},
                        {"text": "Juste après le pétrissage", "isCorrect": False},
                        {"text": "À la sortie du four", "isCorrect": False},
                        {"text": "La veille", "isCorrect": False}
                    ],
                    "correction": "Il crée une faiblesse dans la peau du pâton pour guider l'expansion du gaz carbonique au four."
                },
                {
                    "questionNumber": 29,
                    "question": "L'apprêt trop court (pâte 'verte') donne un pain :",
                    "answerOptions": [
                        {"text": "Bombé, déchiré sur les côtés et peu alvéolé", "isCorrect": True},
                        {"text": "Plat et étalé", "isCorrect": False},
                        {"text": "Parfait", "isCorrect": False},
                        {"text": "Très acide", "isCorrect": False}
                    ],
                    "correction": "La pâte a encore trop de force et pas assez de gaz. Elle 'explose' au four de manière contrainte."
                },
                {
                    "questionNumber": 30,
                    "question": "Le pétrissage intensifié oxyde la pâte, ce qui donne une mie :",
                    "answerOptions": [
                        {"text": "Blanche et cotonneuse", "isCorrect": True},
                        {"text": "Crème et alvéolée", "isCorrect": False},
                        {"text": "Grise", "isCorrect": False},
                        {"text": "Jaune foncé", "isCorrect": False}
                    ],
                    "correction": "L'oxydation détruit les pigments caroténoïdes (couleur crème) et les arômes, au profit du volume et de la blancheur (standard du pain industriel des années 70/80)."
                },
                {
                    "questionNumber": 31,
                    "question": "La détente permet :",
                    "answerOptions": [
                        {"text": "Au gluten de se relâcher pour faciliter le façonnage", "isCorrect": True},
                        {"text": "À la pâte de refroidir", "isCorrect": False},
                        {"text": "De cuire le pain", "isCorrect": False},
                        {"text": "De gagner du temps", "isCorrect": False}
                    ],
                    "correction": "Sans détente, la pâte élastique se rétracte quand on essaie de l'allonger en baguette."
                },
                {
                    "questionNumber": 32,
                    "question": "Un pain 'ferré' est un pain :",
                    "answerOptions": [
                        {"text": "Brûlé dessous", "isCorrect": True},
                        {"text": "Pas assez cuit", "isCorrect": False},
                        {"text": "Trop salé", "isCorrect": False},
                        {"text": "Sans croûte", "isCorrect": False}
                    ],
                    "correction": "Défaut de cuisson (sole trop chaude)."
                },
                {
                    "questionNumber": 33,
                    "question": "La poolish est un pré-ferment composé de :",
                    "answerOptions": [
                        {"text": "Farine et eau (50/50) + un peu de levure", "isCorrect": True},
                        {"text": "Farine et sel uniquement", "isCorrect": False},
                        {"text": "Pâte de la veille conservée au froid", "isCorrect": False},
                        {"text": "Levain dur", "isCorrect": False}
                    ],
                    "correction": "C'est une méthode liquide qui fermente plusieurs heures avant le pétrissage final, apportant des arômes subtils de noisette/beurre."
                },
                {
                    "questionNumber": 34,
                    "question": "Le test du 'Voile' en fin de pétrissage sert à vérifier :",
                    "answerOptions": [
                        {"text": "La bonne formation du réseau glutineux", "isCorrect": True},
                        {"text": "La température", "isCorrect": False},
                        {"text": "Le goût", "isCorrect": False},
                        {"text": "La quantité de sel", "isCorrect": False}
                    ],
                    "correction": "On étire doucement un morceau de pâte. S'il s'étend finement sans déchirer jusqu'à devenir translucide (voile), le pétrissage est optimal."
                },
                {
                    "questionNumber": 35,
                    "question": "Une pâte 'Bâtarde' désigne :",
                    "answerOptions": [
                        {"text": "Une pâte ni trop ferme, ni trop douce", "isCorrect": True},
                        {"text": "Un pain raté", "isCorrect": False},
                        {"text": "Une pâte avec des œufs", "isCorrect": False},
                        {"text": "Une pâte sucrée", "isCorrect": False}
                    ],
                    "correction": "C'est la consistance standard pour le pain courant."
                },
                {
                    "questionNumber": 36,
                    "question": "La température de gélatinisation de l'amidon se situe vers :",
                    "answerOptions": [
                        {"text": "60°C", "isCorrect": True},
                        {"text": "100°C", "isCorrect": False},
                        {"text": "10°C", "isCorrect": False},
                        {"text": "200°C", "isCorrect": False}
                    ],
                    "correction": "C'est à ce moment que la mie se fige (passage de l'état pâteux à l'état solide)."
                },
                {
                    "questionNumber": 37,
                    "question": "La technique du 'fermentolyse' inclut :",
                    "answerOptions": [
                        {"text": "L'ajout du levain dès l'autolyse", "isCorrect": True},
                        {"text": "L'ajout du sel au début", "isCorrect": False},
                        {"text": "Une cuisson vapeur", "isCorrect": False},
                        {"text": "Un pétrissage très rapide", "isCorrect": False}
                    ],
                    "correction": "Variante de l'autolyse où le levain est déjà présent dans le mélange eau/farine au repos, démarrant doucement l'activité fermentaire."
                },
                {
                    "questionNumber": 38,
                    "question": "Une pâte qui manque de force (relâchée) donne :",
                    "answerOptions": [
                        {"text": "Des pains plats", "isCorrect": True},
                        {"text": "Des pains ronds comme des ballons", "isCorrect": False},
                        {"text": "Des pains brûlés", "isCorrect": False},
                        {"text": "Des pains trop durs", "isCorrect": False}
                    ],
                    "correction": "Le gluten ne retient pas assez le gaz, le pâton s'affaisse sous son propre poids."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel four chauffe principalement par convection (air pulsé) ?",
                    "answerOptions": [
                        {"text": "Le four rotatif", "isCorrect": True},
                        {"text": "Le four à sole", "isCorrect": False},
                        {"text": "Le four à bois", "isCorrect": False},
                        {"text": "Le four tunnel", "isCorrect": False}
                    ],
                    "correction": "Un ventilateur pousse l'air chaud à travers le chariot. Idéal pour la régularité, mais dessèche plus les produits que le four à sole."
                },
                {
                    "questionNumber": 40,
                    "question": "En méthode 'Pousse contrôlée', on bloque la fermentation à :",
                    "answerOptions": [
                        {"text": "+2°C / +4°C", "isCorrect": True},
                        {"text": "-20°C", "isCorrect": False},
                        {"text": "+15°C", "isCorrect": False},
                        {"text": "+40°C", "isCorrect": False}
                    ],
                    "correction": "Le froid positif endort la levure sans la tuer, permettant de différer la cuisson jusqu'à 24h ou 48h."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : SCIENCES APPLIQUÉES (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : SCIENCES APPLIQUÉES (Questions 41 à 60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "La zone de danger bactériologique est :",
                    "answerOptions": [
                        {"text": "+10°C à +63°C", "isCorrect": True},
                        {"text": "-18°C à 0°C", "isCorrect": False},
                        {"text": "Au-dessus de 100°C", "isCorrect": False},
                        {"text": "En dessous de 0°C", "isCorrect": False}
                    ],
                    "correction": "Les bactéries se multiplient très vite à température tiède."
                },
                {
                    "questionNumber": 42,
                    "question": "La réaction de Maillard nécessite :",
                    "answerOptions": [
                        {"text": "Des sucres et des protéines (acides aminés)", "isCorrect": True},
                        {"text": "Du gras et de l'eau", "isCorrect": False},
                        {"text": "Uniquement de l'amidon", "isCorrect": False},
                        {"text": "Du froid", "isCorrect": False}
                    ],
                    "correction": "C'est le brunissement non enzymatique à la cuisson qui donne le goût de croûte."
                },
                {
                    "questionNumber": 43,
                    "question": "Les salmonelles sont un risque majeur dans :",
                    "answerOptions": [
                        {"text": "Les ovoproduits crus ou mal cuits", "isCorrect": True},
                        {"text": "La farine sèche", "isCorrect": False},
                        {"text": "Le sucre", "isCorrect": False},
                        {"text": "L'huile", "isCorrect": False}
                    ],
                    "correction": "Attention aux crèmes à base d'œufs non cuites ou les mayonnaises."
                },
                {
                    "questionNumber": 44,
                    "question": "La Maladie Cœliaque est :",
                    "answerOptions": [
                        {"text": "Une intolérance au gluten", "isCorrect": True},
                        {"text": "Une allergie aux fraises", "isCorrect": False},
                        {"text": "Une maladie de peau", "isCorrect": False},
                        {"text": "Une bactérie", "isCorrect": False}
                    ],
                    "correction": "Le système immunitaire attaque l'intestin en présence de gluten. Régime strict sans blé/seigle/orge/avoine."
                },
                {
                    "questionNumber": 45,
                    "question": "Le rassissement est dû à :",
                    "answerOptions": [
                        {"text": "La rétrogradation de l'amidon", "isCorrect": True},
                        {"text": "La perte de sucre", "isCorrect": False},
                        {"text": "La fermentation", "isCorrect": False},
                        {"text": "L'excès de sel", "isCorrect": False}
                    ],
                    "correction": "L'amidon recristallise et l'eau migre de la mie vers la croûte."
                },
                {
                    "questionNumber": 46,
                    "question": "1 gramme de glucides apporte :",
                    "answerOptions": [
                        {"text": "17 kJ (4 kcal)", "isCorrect": True},
                        {"text": "38 kJ (9 kcal)", "isCorrect": False},
                        {"text": "0 kcal", "isCorrect": False},
                        {"text": "100 kcal", "isCorrect": False}
                    ],
                    "correction": "Valeur énergétique standard des sucres. (Lipides = 9 kcal, Protéines = 4 kcal)."
                },
                {
                    "questionNumber": 47,
                    "question": "Une eau potable contient-elle des microbes ?",
                    "answerOptions": [
                        {"text": "Oui, mais aucun pathogène", "isCorrect": True},
                        {"text": "Non, elle est stérile", "isCorrect": False},
                        {"text": "Oui, beaucoup de salmonelles", "isCorrect": False},
                        {"text": "Non, c'est de l'eau distillée", "isCorrect": False}
                    ],
                    "correction": "L'eau du robinet n'est pas stérile (elle contient une flore banale) mais est sans danger pour la santé."
                },
                {
                    "questionNumber": 48,
                    "question": "Le lavage des mains efficace inclut :",
                    "answerOptions": [
                        {"text": "Savonnage, brossage des ongles, rinçage, séchage unique", "isCorrect": True},
                        {"text": "Juste passer sous l'eau", "isCorrect": False},
                        {"text": "Essuyer sur le tablier", "isCorrect": False},
                        {"text": "Utiliser de l'alcool pur sans frotter", "isCorrect": False}
                    ],
                    "correction": "Le séchage est crucial pour ne pas recontaminer les mains humides."
                },
                {
                    "questionNumber": 49,
                    "question": "HACCP signifie :",
                    "answerOptions": [
                        {"text": "Analyse des Dangers et Points Critiques pour leur Maîtrise", "isCorrect": True},
                        {"text": "Haute Autorité de la Cuisine et de la Pâtisserie", "isCorrect": False},
                        {"text": "Hygiène Alimentaire Contrôlée par la Police", "isCorrect": False},
                        {"text": "Habitude Culinaire Propre", "isCorrect": False}
                    ],
                    "correction": "Hazard Analysis Critical Control Point. Système préventif obligatoire."
                },
                {
                    "questionNumber": 50,
                    "question": "La toxine staphylococcique résiste-t-elle à la cuisson ?",
                    "answerOptions": [
                        {"text": "Oui, elle est thermostable", "isCorrect": True},
                        {"text": "Non, elle meurt à 60°C", "isCorrect": False},
                        {"text": "Non, elle meurt à 100°C", "isCorrect": False},
                        {"text": "Elle disparaît au froid", "isCorrect": False}
                    ],
                    "correction": "C'est le grand danger : recuire un produit contaminé tue la bactérie mais pas le poison qu'elle a déjà produit."
                },
                {
                    "questionNumber": 51,
                    "question": "L'Aw de la mie de pain frais est environ de :",
                    "answerOptions": [
                        {"text": "0,95 à 0,98", "isCorrect": True},
                        {"text": "0,10", "isCorrect": False},
                        {"text": "0,50", "isCorrect": False},
                        {"text": "0", "isCorrect": False}
                    ],
                    "correction": "L'Activité de l'eau est très élevée dans la mie (proche de 1), ce qui la rend vulnérable aux moisissures et bactéries (pain filant)."
                },
                {
                    "questionNumber": 52,
                    "question": "Un porteur sain :",
                    "answerOptions": [
                        {"text": "Ne présente aucun symptôme mais transmet la maladie", "isCorrect": True},
                        {"text": "Est quelqu'un en bonne santé qui ne transmet rien", "isCorrect": False},
                        {"text": "Est malade au lit", "isCorrect": False},
                        {"text": "Est un livreur", "isCorrect": False}
                    ],
                    "correction": "Il héberge le germe (ex: Staphylocoque dans le nez) sans le savoir."
                },
                {
                    "questionNumber": 53,
                    "question": "Les fibres insolubles du son :",
                    "answerOptions": [
                        {"text": "Accélèrent le transit", "isCorrect": True},
                        {"text": "Ralentissent le transit", "isCorrect": False},
                        {"text": "Donnent du gras", "isCorrect": False},
                        {"text": "Donnent du goût sucré", "isCorrect": False}
                    ],
                    "correction": "Elles gonflent d'eau et augmentent le volume des selles (effet de lest)."
                },
                {
                    "questionNumber": 54,
                    "question": "À partir de quelle T° l'amidon gonfle-t-il ?",
                    "answerOptions": [
                        {"text": "60°C", "isCorrect": True},
                        {"text": "30°C", "isCorrect": False},
                        {"text": "150°C", "isCorrect": False},
                        {"text": "0°C", "isCorrect": False}
                    ],
                    "correction": "Début de l'empois d'amidon (gélatinisation)."
                },
                {
                    "questionNumber": 55,
                    "question": "Un détergent sert à :",
                    "answerOptions": [
                        {"text": "Enlever la souillure (graisse/sucre)", "isCorrect": True},
                        {"text": "Tuer les microbes", "isCorrect": False},
                        {"text": "Rincer", "isCorrect": False},
                        {"text": "Faire briller", "isCorrect": False}
                    ],
                    "correction": "Ne pas confondre avec le désinfectant. On nettoie d'abord, on désinfecte ensuite."
                },
                {
                    "questionNumber": 56,
                    "question": "Les moisissures aiment les milieux :",
                    "answerOptions": [
                        {"text": "Acides et humides", "isCorrect": True},
                        {"text": "Basiques et secs", "isCorrect": False},
                        {"text": "Très chauds", "isCorrect": False},
                        {"text": "Gelés", "isCorrect": False}
                    ],
                    "correction": "Le pain est leur milieu idéal (pH ~5.5, humidité mie)."
                },
                {
                    "questionNumber": 57,
                    "question": "L'alcool produit par la levure :",
                    "answerOptions": [
                        {"text": "S'évapore à la cuisson", "isCorrect": True},
                        {"text": "Reste dans le pain (le pain saoule)", "isCorrect": False},
                        {"text": "Se transforme en eau", "isCorrect": False},
                        {"text": "Devient du sel", "isCorrect": False}
                    ],
                    "correction": "Il participe aux arômes mais disparaît physiquement."
                },
                {
                    "questionNumber": 58,
                    "question": "La leptospirose vient de :",
                    "answerOptions": [
                        {"text": "L'urine de rat", "isCorrect": True},
                        {"text": "La farine", "isCorrect": False},
                        {"text": "L'eau du robinet", "isCorrect": False},
                        {"text": "La levure", "isCorrect": False}
                    ],
                    "correction": "Maladie grave. D'où l'importance de l'hygiène des locaux et des stocks."
                },
                {
                    "questionNumber": 59,
                    "question": "La marche en avant dans le temps :",
                    "answerOptions": [
                        {"text": "On nettoie entre deux tâches différentes sur le même plan de travail", "isCorrect": True},
                        {"text": "On travaille toujours le matin", "isCorrect": False},
                        {"text": "On ne revient jamais en arrière dans la pièce", "isCorrect": False},
                        {"text": "On court", "isCorrect": False}
                    ],
                    "correction": "Solution pour les petits laboratoires où la marche en avant dans l'espace est impossible."
                },
                {
                    "questionNumber": 60,
                    "question": "Le vert-de-gris est un oxyde de :",
                    "answerOptions": [
                        {"text": "Cuivre", "isCorrect": True},
                        {"text": "Fer", "isCorrect": False},
                        {"text": "Aluminium", "isCorrect": False},
                        {"text": "Inox", "isCorrect": False}
                    ],
                    "correction": "Toxique. Apparaît sur les bassines en cuivre mal entretenues ou non étamées au contact de l'acide (levain/fruits)."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : ÉQUIPEMENT ET MATÉRIEL (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ÉQUIPEMENT ET MATÉRIEL (Questions 61 à 80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Le pétrin à axe oblique :",
                    "answerOptions": [
                        {"text": "Évite l'échauffement excessif de la pâte", "isCorrect": True},
                        {"text": "Chauffe beaucoup la pâte", "isCorrect": False},
                        {"text": "Est interdit en France", "isCorrect": False},
                        {"text": "Ne sert qu'à la pâtisserie", "isCorrect": False}
                    ],
                    "correction": "Il reproduit le pétrissage manuel des bras. Idéal pour le pain courant français."
                },
                {
                    "questionNumber": 62,
                    "question": "La diviseuse hydraulique :",
                    "answerOptions": [
                        {"text": "Coupe la pâte en pâtons égaux par pression", "isCorrect": True},
                        {"text": "Pèse la pâte", "isCorrect": False},
                        {"text": "Cuit la pâte", "isCorrect": False},
                        {"text": "Façonne la pâte", "isCorrect": False}
                    ],
                    "correction": "Elle possède une cuve et des couteaux qui remontent sous la pression de l'huile."
                },
                {
                    "questionNumber": 63,
                    "question": "Le 'Parisien' est :",
                    "answerOptions": [
                        {"text": "Une échelle de rangement pour les planches à pain", "isCorrect": True},
                        {"text": "Un pain long", "isCorrect": False},
                        {"text": "Un four", "isCorrect": False},
                        {"text": "Un sac de farine", "isCorrect": False}
                    ],
                    "correction": "Meuble à glissières incontournable au fournil pour stocker les couches en attente d'enfournement."
                },
                {
                    "questionNumber": 64,
                    "question": "Le four à sole chauffe par :",
                    "answerOptions": [
                        {"text": "Conduction (contact direct)", "isCorrect": True},
                        {"text": "Convection (air ventilé)", "isCorrect": False},
                        {"text": "Micro-ondes", "isCorrect": False},
                        {"text": "Induction", "isCorrect": False}
                    ],
                    "correction": "Le pain est posé sur la dalle chaude. C'est ce qui donne une croûte inférieure épaisse et croustillante."
                },
                {
                    "questionNumber": 65,
                    "question": "Les cylindres de la façonneuse servent à :",
                    "answerOptions": [
                        {"text": "Laminer (dégazer) la pâte", "isCorrect": True},
                        {"text": "Allonger la pâte", "isCorrect": False},
                        {"text": "Couper la pâte", "isCorrect": False},
                        {"text": "Enrouler la pâte", "isCorrect": False}
                    ],
                    "correction": "Première étape du façonnage mécanique : on écrase le pâton pour chasser le gaz carbonique avant de l'enrouler."
                },
                {
                    "questionNumber": 66,
                    "question": "Le refroidisseur d'eau sert à :",
                    "answerOptions": [
                        {"text": "Obtenir une eau à +3°C ou +4°C", "isCorrect": True},
                        {"text": "Faire des glaçons pour l'apéro", "isCorrect": False},
                        {"text": "Laver le sol", "isCorrect": False},
                        {"text": "Chauffer l'eau", "isCorrect": False}
                    ],
                    "correction": "Indispensable pour respecter la Température de Base et ne pas sortir des pâtes trop chaudes."
                },
                {
                    "questionNumber": 67,
                    "question": "Les couches sont généralement en :",
                    "answerOptions": [
                        {"text": "Toile de lin", "isCorrect": True},
                        {"text": "Coton", "isCorrect": False},
                        {"text": "Polyester", "isCorrect": False},
                        {"text": "Soie", "isCorrect": False}
                    ],
                    "correction": "Le lin est imputrescible et gère bien l'humidité, empêchant la pâte de coller (si on fleure un peu)."
                },
                {
                    "questionNumber": 68,
                    "question": "La pelle à enfourner est en :",
                    "answerOptions": [
                        {"text": "Bois ou aluminium", "isCorrect": True},
                        {"text": "Plastique mou", "isCorrect": False},
                        {"text": "Verre", "isCorrect": False},
                        {"text": "Carton", "isCorrect": False}
                    ],
                    "correction": "Doit être fine et glissante pour déposer les pâtons sans les abîmer."
                },
                {
                    "questionNumber": 69,
                    "question": "La lame de boulanger se change :",
                    "answerOptions": [
                        {"text": "Dès qu'elle accroche la pâte", "isCorrect": True},
                        {"text": "Une fois par an", "isCorrect": False},
                        {"text": "Jamais", "isCorrect": False},
                        {"text": "Tous les jours obligatoirement", "isCorrect": False}
                    ],
                    "correction": "Une lame émoussée déchire la pâte au lieu de la couper net, ce qui donne des grignes moches."
                },
                {
                    "questionNumber": 70,
                    "question": "Le silot à farine :",
                    "answerOptions": [
                        {"text": "Permet le stockage en vrac et le dosage automatique", "isCorrect": True},
                        {"text": "Sert à cuire", "isCorrect": False},
                        {"text": "Sert à tamiser", "isCorrect": False},
                        {"text": "Est un camion", "isCorrect": False}
                    ],
                    "correction": "Installé à l'extérieur ou en cave, il alimente directement le pétrin via des vis sans fin ou transfert pneumatique."
                },
                {
                    "questionNumber": 71,
                    "question": "Les plaques alvéolées (filets) servent pour :",
                    "answerOptions": [
                        {"text": "Les fours ventilés", "isCorrect": True},
                        {"text": "Les fours à sole", "isCorrect": False},
                        {"text": "Le pétrissage", "isCorrect": False},
                        {"text": "La vente", "isCorrect": False}
                    ],
                    "correction": "L'air chaud doit circuler à travers le support pour cuire le dessous du pain."
                },
                {
                    "questionNumber": 72,
                    "question": "L'hygrométrie en chambre de pousse évite :",
                    "answerOptions": [
                        {"text": "Le croûtage des pâtons", "isCorrect": True},
                        {"text": "La fermentation", "isCorrect": False},
                        {"text": "La chaleur", "isCorrect": False},
                        {"text": "Le froid", "isCorrect": False}
                    ],
                    "correction": "Si l'air est trop sec, une peau sèche se forme sur la pâte, l'empêchant de pousser correctement."
                },
                {
                    "questionNumber": 73,
                    "question": "Le 'tour' est en :",
                    "answerOptions": [
                        {"text": "Bois (hêtre) ou Inox", "isCorrect": True},
                        {"text": "Verre", "isCorrect": False},
                        {"text": "Tissu", "isCorrect": False},
                        {"text": "Terre cuite", "isCorrect": False}
                    ],
                    "correction": "Surface de travail pour le boulage et le façonnage. Le bois est traditionnel (absorbe l'humidité), l'inox est plus hygiénique."
                },
                {
                    "questionNumber": 74,
                    "question": "Le batteur mélangeur sert pour :",
                    "answerOptions": [
                        {"text": "La viennoiserie et les crèmes", "isCorrect": True},
                        {"text": "Le pain de campagne", "isCorrect": False},
                        {"text": "La baguette tradition", "isCorrect": False},
                        {"text": "Diviser la pâte", "isCorrect": False}
                    ],
                    "correction": "Il n'est pas conçu pour les pâtes fermes et tenaces comme le pain (risque de casse mécanique), sauf en très petite quantité."
                },
                {
                    "questionNumber": 75,
                    "question": "Un joint de four défectueux entraîne :",
                    "answerOptions": [
                        {"text": "Une perte de buée et de chaleur", "isCorrect": True},
                        {"text": "Une meilleure cuisson", "isCorrect": False},
                        {"text": "Rien", "isCorrect": False},
                        {"text": "Un risque d'incendie immédiat", "isCorrect": False}
                    ],
                    "correction": "Sans étanchéité, la buée s'échappe, le pain est terne et sec."
                },
                {
                    "questionNumber": 76,
                    "question": "Le banneton donne :",
                    "answerOptions": [
                        {"text": "La forme et parfois un motif au pain", "isCorrect": True},
                        {"text": "Le goût", "isCorrect": False},
                        {"text": "La couleur", "isCorrect": False},
                        {"text": "Le sel", "isCorrect": False}
                    ],
                    "correction": "Utilisé pour les pains spéciaux (couronnes, miches de campagne) qui lèvent dedans."
                },
                {
                    "questionNumber": 77,
                    "question": "L'enfourneur à tapis (ciseaux) :",
                    "answerOptions": [
                        {"text": "Dépose tout l'étage en une fois", "isCorrect": True},
                        {"text": "Cuit le pain", "isCorrect": False},
                        {"text": "Coupe le pain", "isCorrect": False},
                        {"text": "Pèse le pain", "isCorrect": False}
                    ],
                    "correction": "Équipement ergonomique majeur pour les fours à sole profonds."
                },
                {
                    "questionNumber": 78,
                    "question": "Le tamis est obligatoire pour :",
                    "answerOptions": [
                        {"text": "Éliminer les corps étrangers", "isCorrect": True},
                        {"text": "Faire joli", "isCorrect": False},
                        {"text": "Peser", "isCorrect": False},
                        {"text": "Compter", "isCorrect": False}
                    ],
                    "correction": "Sécurité alimentaire de base (insectes, bouts de papier, plastique)."
                },
                {
                    "questionNumber": 79,
                    "question": "L'Alvéographe Chopin mesure :",
                    "answerOptions": [
                        {"text": "La ténacité (P) et l'extensibilité (L) de la pâte", "isCorrect": True},
                        {"text": "L'activité enzymatique", "isCorrect": False},
                        {"text": "Le taux de cendres", "isCorrect": False},
                        {"text": "L'humidité", "isCorrect": False}
                    ],
                    "correction": "Il gonfle une bulle de pâte jusqu'à l'éclatement. Donne le W (force)."
                },
                {
                    "questionNumber": 80,
                    "question": "La pesée automatique divise la pâte :",
                    "answerOptions": [
                        {"text": "En volume", "isCorrect": True},
                        {"text": "En poids réel", "isCorrect": False},
                        {"text": "À la main", "isCorrect": False},
                        {"text": "Au hasard", "isCorrect": False}
                    ],
                    "correction": "La machine (volumétrique) estime le poids selon le volume du piston. La régularité de la pâte (fermentation) est cruciale pour la précision."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : GESTION ET COMMERCE (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : GESTION ET COMMERCE (Questions 81 à 100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Le coefficient multiplicateur permet de :",
                    "answerOptions": [
                        {"text": "Fixer le prix de vente à partir du coût d'achat", "isCorrect": True},
                        {"text": "Calculer la TVA", "isCorrect": False},
                        {"text": "Payer les impôts", "isCorrect": False},
                        {"text": "Compter les clients", "isCorrect": False}
                    ],
                    "correction": "Prix Vente TTC = Coût Achat HT x Coeff. Il couvre la marge et la TVA."
                },
                {
                    "questionNumber": 82,
                    "question": "TVA sur le pain ?",
                    "answerOptions": [
                        {"text": "5,5 %", "isCorrect": True},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "10 %", "isCorrect": False},
                        {"text": "2,1 %", "isCorrect": False}
                    ],
                    "correction": "Taux réduit de base."
                },
                {
                    "questionNumber": 83,
                    "question": "Pour le pain, l'affichage obligatoire comprend :",
                    "answerOptions": [
                        {"text": "Prix pièce, Prix au kg, Poids, Dénomination", "isCorrect": True},
                        {"text": "Juste le prix", "isCorrect": False},
                        {"text": "La photo du boulanger", "isCorrect": False},
                        {"text": "La date de cuisson", "isCorrect": False}
                    ],
                    "correction": "Le consommateur doit pouvoir comparer les prix au kilo."
                },
                {
                    "questionNumber": 84,
                    "question": "Le Label AB garantit :",
                    "answerOptions": [
                        {"text": "95% d'ingrédients bio minimum", "isCorrect": True},
                        {"text": "100% français", "isCorrect": False},
                        {"text": "Sans gluten", "isCorrect": False},
                        {"text": "Fait main", "isCorrect": False}
                    ],
                    "correction": "Agriculture Biologique (sans pesticides ni engrais chimiques de synthèse)."
                },
                {
                    "questionNumber": 85,
                    "question": "Méthode FIFO ?",
                    "answerOptions": [
                        {"text": "Premier Entré, Premier Sorti", "isCorrect": True},
                        {"text": "Le moins cher d'abord", "isCorrect": False},
                        {"text": "Le plus beau d'abord", "isCorrect": False},
                        {"text": "Jeter le vieux", "isCorrect": False}
                    ],
                    "correction": "Rotation des stocks pour éviter les périmés."
                },
                {
                    "questionNumber": 86,
                    "question": "L'appellation 'Boulangerie' exige :",
                    "answerOptions": [
                        {"text": "Pétrissage, façonnage et cuisson sur place", "isCorrect": True},
                        {"text": "Cuisson sur place seulement", "isCorrect": False},
                        {"text": "Vente de pain", "isCorrect": False},
                        {"text": "Avoir un diplôme", "isCorrect": False}
                    ],
                    "correction": "Interdit aux terminaux de cuisson qui ne font que cuire du surgelé."
                },
                {
                    "questionNumber": 87,
                    "question": "La démarque inconnue c'est :",
                    "answerOptions": [
                        {"text": "Le vol et la casse non déclarée", "isCorrect": True},
                        {"text": "Les soldes", "isCorrect": False},
                        {"text": "Une marque de farine", "isCorrect": False},
                        {"text": "Le bénéfice", "isCorrect": False}
                    ],
                    "correction": "Différence entre stock théorique et réel."
                },
                {
                    "questionNumber": 88,
                    "question": "La traçabilité sert à :",
                    "answerOptions": [
                        {"text": "Retrouver l'origine en cas de problème", "isCorrect": True},
                        {"text": "Espionner", "isCorrect": False},
                        {"text": "Faire des statistiques", "isCorrect": False},
                        {"text": "Rien", "isCorrect": False}
                    ],
                    "correction": "Sécurité sanitaire (rappels de produits)."
                },
                {
                    "questionNumber": 89,
                    "question": "Marge Brute =",
                    "answerOptions": [
                        {"text": "CA HT - Achats consommés", "isCorrect": True},
                        {"text": "CA TTC - TVA", "isCorrect": False},
                        {"text": "Bénéfice net", "isCorrect": False},
                        {"text": "Salaire", "isCorrect": False}
                    ],
                    "correction": "Ce qui reste pour payer les charges de structure."
                },
                {
                    "questionNumber": 90,
                    "question": "Contrôle à la livraison :",
                    "answerOptions": [
                        {"text": "Quantitatif et Qualitatif", "isCorrect": True},
                        {"text": "Juste signer", "isCorrect": False},
                        {"text": "Regarder le camion", "isCorrect": False},
                        {"text": "Payer tout de suite", "isCorrect": False}
                    ],
                    "correction": "Vérifier l'état, la T° et le poids."
                },
                {
                    "questionNumber": 91,
                    "question": "Affichage allergènes :",
                    "answerOptions": [
                        {"text": "Obligatoire par écrit", "isCorrect": True},
                        {"text": "Facultatif", "isCorrect": False},
                        {"text": "Oral uniquement", "isCorrect": False},
                        {"text": "Interdit", "isCorrect": False}
                    ],
                    "correction": "Doit être accessible au client sans qu'il ait à demander (livret ou étiquette)."
                },
                {
                    "questionNumber": 92,
                    "question": "Seuil de rentabilité :",
                    "answerOptions": [
                        {"text": "Résultat = 0", "isCorrect": True},
                        {"text": "Résultat = 1000", "isCorrect": False},
                        {"text": "Perte maximale", "isCorrect": False},
                        {"text": "Chiffre d'affaires max", "isCorrect": False}
                    ],
                    "correction": "Moment où on commence à faire du bénéfice."
                },
                {
                    "questionNumber": 93,
                    "question": "La vitrine doit être :",
                    "answerOptions": [
                        {"text": "Pleine et éclairée", "isCorrect": True},
                        {"text": "Vide", "isCorrect": False},
                        {"text": "Sale", "isCorrect": False},
                        {"text": "Éteinte", "isCorrect": False}
                    ],
                    "correction": "Le 'merchandising' visuel déclenche l'achat d'impulsion."
                },
                {
                    "questionNumber": 94,
                    "question": "La fiche technique sert à :",
                    "answerOptions": [
                        {"text": "Calculer le coût de revient", "isCorrect": True},
                        {"text": "Décorer", "isCorrect": False},
                        {"text": "Perdre du temps", "isCorrect": False},
                        {"text": "Rien", "isCorrect": False}
                    ],
                    "correction": "Outil de gestion indispensable pour la rentabilité."
                },
                {
                    "questionNumber": 95,
                    "question": "Pain complet riche en :",
                    "answerOptions": [
                        {"text": "Fibres", "isCorrect": True},
                        {"text": "Lipides", "isCorrect": False},
                        {"text": "Sucre", "isCorrect": False},
                        {"text": "Sel", "isCorrect": False}
                    ],
                    "correction": "Bon pour le transit."
                },
                {
                    "questionNumber": 96,
                    "question": "Invendus :",
                    "answerOptions": [
                        {"text": "Don ou alimentation animale", "isCorrect": True},
                        {"text": "Revente le lendemain", "isCorrect": False},
                        {"text": "Poubelle", "isCorrect": False},
                        {"text": "Brûler", "isCorrect": False}
                    ],
                    "correction": "Gaspillage interdit."
                },
                {
                    "questionNumber": 97,
                    "question": "Le DUER est :",
                    "answerOptions": [
                        {"text": "Le Document Unique des Risques", "isCorrect": True},
                        {"text": "Un diplôme", "isCorrect": False},
                        {"text": "Une taxe", "isCorrect": False},
                        {"text": "Une recette", "isCorrect": False}
                    ],
                    "correction": "Obligation employeur pour la sécurité."
                },
                {
                    "questionNumber": 98,
                    "question": "Logo 'Fait Maison' :",
                    "answerOptions": [
                        {"text": "Produits transformés sur place", "isCorrect": True},
                        {"text": "Produits industriels", "isCorrect": False},
                        {"text": "Surgelés", "isCorrect": False},
                        {"text": "Achetés tout faits", "isCorrect": False}
                    ],
                    "correction": "Valorise l'artisanat (petite casserole)."
                },
                {
                    "questionNumber": 99,
                    "question": "T° vitrine sandwich :",
                    "answerOptions": [
                        {"text": "+4°C max", "isCorrect": True},
                        {"text": "+10°C", "isCorrect": False},
                        {"text": "Ambiante", "isCorrect": False},
                        {"text": "-18°C", "isCorrect": False}
                    ],
                    "correction": "Produit frais sensible."
                },
                {
                    "questionNumber": 100,
                    "question": "Saint Patron des boulangers ?",
                    "answerOptions": [
                        {"text": "Saint Honoré", "isCorrect": True},
                        {"text": "Saint Michel", "isCorrect": False},
                        {"text": "Saint Pierre", "isCorrect": False},
                        {"text": "Saint Paul", "isCorrect": False}
                    ],
                    "correction": "Fêté le 16 mai."
                }
            ]
        }
    }
}