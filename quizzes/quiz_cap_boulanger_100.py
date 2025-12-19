quiz_data = {
    "title": "Quiz CAP Boulanger (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : CONNAISSANCE DES MATIÈRES PREMIÈRES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : CONNAISSANCE DES MATIÈRES PREMIÈRES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel type de farine est le plus couramment utilisé pour la fabrication du pain courant français ?",
                    "answerOptions": [
                        {"text": "Type 55", "isCorrect": True},
                        {"text": "Type 45", "isCorrect": False},
                        {"text": "Type 65", "isCorrect": False},
                        {"text": "Type 80", "isCorrect": False}
                    ],
                    "correction": "La farine de Type 55 (T55) est la référence standard pour le pain courant. La T45 est réservée à la pâtisserie/viennoiserie, et la T65 à la tradition française."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la principale fonction du sel dans la pâte à pain en dehors de l'apport gustatif ?",
                    "answerOptions": [
                        {"text": "Réguler la fermentation", "isCorrect": True},
                        {"text": "Nourrir la levure", "isCorrect": False},
                        {"text": "Blanchir la mie", "isCorrect": False},
                        {"text": "Accélérer le pétrissage", "isCorrect": False}
                    ],
                    "correction": "Le sel joue un rôle technologique majeur : il freine l'activité de la levure (régulateur), donne du corps au gluten (fixateur d'eau) et favorise la coloration de la croûte."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel nom donne-t-on aux protéines insolubles de la farine qui forment le réseau élastique ?",
                    "answerOptions": [
                        {"text": "Gluten", "isCorrect": True},
                        {"text": "Amidon", "isCorrect": False},
                        {"text": "Cendres", "isCorrect": False},
                        {"text": "Enzymes", "isCorrect": False}
                    ],
                    "correction": "Le gluten est formé par l'hydratation et le pétrissage des protéines (gliadines et gluténines). Il permet de retenir les gaz de fermentation."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le rôle principal de la levure biologique (Saccharomyces cerevisiae) ?",
                    "answerOptions": [
                        {"text": "Produire du gaz carbonique", "isCorrect": True},
                        {"text": "Donner une couleur blanche", "isCorrect": False},
                        {"text": "Détruire les microbes", "isCorrect": False},
                        {"text": "Sucrer la pâte", "isCorrect": False}
                    ],
                    "correction": "La levure transforme les sucres en gaz carbonique (qui fait lever la pâte) et en alcool (qui s'évapore à la cuisson)."
                },
                {
                    "questionNumber": 5,
                    "question": "À quel taux d'hydratation correspond l'ajout de 600g d'eau pour 1kg de farine ?",
                    "answerOptions": [
                        {"text": "60%", "isCorrect": True},
                        {"text": "50%", "isCorrect": False},
                        {"text": "70%", "isCorrect": False},
                        {"text": "100%", "isCorrect": False}
                    ],
                    "correction": "Le taux d'hydratation se calcule par rapport au poids de la farine. 600/1000 = 0,60 soit 60%."
                },
                {
                    "questionNumber": 6,
                    "question": "Dans le blé, où se situent majoritairement les matières minérales (cendres) ?",
                    "answerOptions": [
                        {"text": "Dans les enveloppes (le son)", "isCorrect": True},
                        {"text": "Dans l'amande farineuse", "isCorrect": False},
                        {"text": "Dans le germe", "isCorrect": False},
                        {"text": "Dans la brosse", "isCorrect": False}
                    ],
                    "correction": "Le taux de cendres (T) indique la pureté de la farine. Plus la farine est complète (T150), plus elle contient d'enveloppes et de minéraux."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est l'effet d'une eau trop calcaire sur la pâte ?",
                    "answerOptions": [
                        {"text": "Elle durcit le gluten", "isCorrect": True},
                        {"text": "Elle ramollit la pâte", "isCorrect": False},
                        {"text": "Elle tue la levure", "isCorrect": False},
                        {"text": "Elle noircit la croûte", "isCorrect": False}
                    ],
                    "correction": "Une eau calcaire renforce la ténacité du réseau de gluten, ce qui peut rendre la pâte plus difficile à travailler."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel composant de la farine représente environ 70% de sa masse et sert de nourriture à la levure après transformation ?",
                    "answerOptions": [
                        {"text": "L'amidon", "isCorrect": True},
                        {"text": "Le gluten", "isCorrect": False},
                        {"text": "L'eau", "isCorrect": False},
                        {"text": "Les vitamines", "isCorrect": False}
                    ],
                    "correction": "L'amidon est un glucide complexe qui, sous l'action des enzymes (amylases), se transforme en sucres simples consommables par la levure."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le dosage de sel standard pour 1kg de farine (selon les recommandations de santé actuelle) ?",
                    "answerOptions": [
                        {"text": "18g", "isCorrect": True},
                        {"text": "30g", "isCorrect": False},
                        {"text": "10g", "isCorrect": False},
                        {"text": "50g", "isCorrect": False}
                    ],
                    "correction": "La recommandation actuelle vise à ne pas dépasser 1,8% de sel par rapport au poids de farine pour des raisons de santé publique."
                },
                {
                    "questionNumber": 10,
                    "question": "Comment appelle-t-on le sucre naturellement présent dans le lait utilisé pour les pains de mie ou brioches ?",
                    "answerOptions": [
                        {"text": "Le lactose", "isCorrect": True},
                        {"text": "Le fructose", "isCorrect": False},
                        {"text": "Le maltose", "isCorrect": False},
                        {"text": "Le glucose", "isCorrect": False}
                    ],
                    "correction": "Le lactose est le sucre du lait. Il ne fermente pas sous l'action de la levure de boulangerie mais apporte du goût et de la coloration à la croûte."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est l'ennemi principal de la levure biologique lors de son incorporation ?",
                    "answerOptions": [
                        {"text": "Le contact direct avec le sel", "isCorrect": True},
                        {"text": "Le contact avec la farine", "isCorrect": False},
                        {"text": "Le froid du réfrigérateur", "isCorrect": False},
                        {"text": "L'obscurité", "isCorrect": False}
                    ],
                    "correction": "Le sel a un pouvoir plasmolysant : s'il est en contact direct et prolongé avec la levure, il détruit ses cellules par déshydratation."
                },
                {
                    "questionNumber": 12,
                    "question": "À quelle température moyenne la levure est-elle détruite ?",
                    "answerOptions": [
                        {"text": "50-55°C", "isCorrect": True},
                        {"text": "20-25°C", "isCorrect": False},
                        {"text": "100°C", "isCorrect": False},
                        {"text": "0°C", "isCorrect": False}
                    ],
                    "correction": "La levure meurt vers 50°C. C'est pourquoi elle arrête son activité au début de la cuisson au four."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est la farine issue du broyage complet du grain de blé ?",
                    "answerOptions": [
                        {"text": "Intégrale (T150)", "isCorrect": True},
                        {"text": "Blanche (T45)", "isCorrect": False},
                        {"text": "Bise (T80)", "isCorrect": False},
                        {"text": "De gruau", "isCorrect": False}
                    ],
                    "correction": "La farine T150 contient toutes les parties du grain, y compris le germe et la totalité du son."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel additif naturel permet de corriger une farine manquant de force ?",
                    "answerOptions": [
                        {"text": "Le gluten de blé sec", "isCorrect": True},
                        {"text": "Le sucre semoule", "isCorrect": False},
                        {"text": "L'eau distillée", "isCorrect": False},
                        {"text": "Le charbon végétal", "isCorrect": False}
                    ],
                    "correction": "L'ajout de gluten pur augmente la ténacité et la capacité de rétention gazeuse de la pâte."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle est la principale différence entre le beurre et la margarine ?",
                    "answerOptions": [
                        {"text": "L'origine de la matière grasse (animale vs végétale)", "isCorrect": True},
                        {"text": "La couleur uniquement", "isCorrect": False},
                        {"text": "La teneur en sel", "isCorrect": False},
                        {"text": "Le prix seulement", "isCorrect": False}
                    ],
                    "correction": "Le beurre est issu de la crème de lait (animal), la margarine est issue d'huiles végétales hydrogénées ou fractionnées."
                },
                {
                    "questionNumber": 16,
                    "question": "Qu'est-ce que l'acide ascorbique (E300) utilisé en boulangerie ?",
                    "answerOptions": [
                        {"text": "Un agent de traitement de la farine (vitamine C)", "isCorrect": True},
                        {"text": "Un conservateur anti-moisissure", "isCorrect": False},
                        {"text": "Un colorant pour la mie", "isCorrect": False},
                        {"text": "Un arôme artificiel de citron", "isCorrect": False}
                    ],
                    "correction": "L'acide ascorbique renforce les liaisons du gluten, améliorant la tenue des pâtes et le volume des pains."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le taux d'humidité moyen d'une farine bien conservée ?",
                    "answerOptions": [
                        {"text": "15%", "isCorrect": True},
                        {"text": "5%", "isCorrect": False},
                        {"text": "40%", "isCorrect": False},
                        {"text": "0%", "isCorrect": False}
                    ],
                    "correction": "Légalement, l'humidité de la farine ne doit pas dépasser 15,5% pour éviter les moisissures et garantir la conservation."
                },
                {
                    "questionNumber": 18,
                    "question": "Le malt ajouté à la farine sert principalement à :",
                    "answerOptions": [
                        {"text": "Apporter des enzymes pour nourrir la levure", "isCorrect": True},
                        {"text": "Remplacer le sel", "isCorrect": False},
                        {"text": "Blanchir la farine", "isCorrect": False},
                        {"text": "Diminuer le temps de pétrissage", "isCorrect": False}
                    ],
                    "correction": "La farine de malt apporte des amylases qui décomposent l'amidon en sucres fermentescibles, aidant la fermentation et la coloration."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle céréale ne contient pas de gluten ?",
                    "answerOptions": [
                        {"text": "Le Maïs", "isCorrect": True},
                        {"text": "Le Seigle", "isCorrect": False},
                        {"text": "L'Épeautre", "isCorrect": False},
                        {"text": "Le Froment", "isCorrect": False}
                    ],
                    "correction": "Le riz, le maïs, le sarrasin et le quinoa sont naturellement sans gluten, contrairement au blé (froment), au seigle ou à l'orge."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est la fonction des matières grasses dans la viennoiserie ?",
                    "answerOptions": [
                        {"text": "Apporter du fondant et le feuilletage", "isCorrect": True},
                        {"text": "Accélérer la pousse", "isCorrect": False},
                        {"text": "Rendre le pain plus croquant", "isCorrect": False},
                        {"text": "Diminuer l'hydratation", "isCorrect": False}
                    ],
                    "correction": "Le gras (beurre) lubrifie les fibres de gluten, apporte du goût, du moelleux et permet la séparation des couches dans le feuilletage."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : PANIFICATION ET TECHNIQUES DE FABRICATION (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : PANIFICATION ET TECHNIQUES DE FABRICATION",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Comment appelle-t-on la première phase du pétrissage consistant à mélanger l'eau et la farine ?",
                    "answerOptions": [
                        {"text": "Le frasage", "isCorrect": True},
                        {"text": "L'étirage", "isCorrect": False},
                        {"text": "Le soufflage", "isCorrect": False},
                        {"text": "Le lissage", "isCorrect": False}
                    ],
                    "correction": "Le frasage dure quelques minutes à vitesse lente pour amalgamer les ingrédients avant de passer au pétrissage proprement dit."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la température idéale de fin de pétrissage pour une pâte à pain courant ?",
                    "answerOptions": [
                        {"text": "24°C", "isCorrect": True},
                        {"text": "15°C", "isCorrect": False},
                        {"text": "35°C", "isCorrect": False},
                        {"text": "45°C", "isCorrect": False}
                    ],
                    "correction": "Une température entre 23°C et 25°C permet une activité fermentaire régulière et une bonne tenue de la pâte."
                },
                {
                    "questionNumber": 23,
                    "question": "Qu'est-ce que l'autolyse en boulangerie ?",
                    "answerOptions": [
                        {"text": "Un repos de la farine et de l'eau sans levure ni sel", "isCorrect": True},
                        {"text": "Une fermentation très longue au froid", "isCorrect": False},
                        {"text": "Le nettoyage automatique du pétrin", "isCorrect": False},
                        {"text": "Une technique de cuisson à la vapeur", "isCorrect": False}
                    ],
                    "correction": "L'autolyse permet de détendre le gluten et d'améliorer l'extensibilité de la pâte avant le pétrissage final."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on le temps de repos de la pâte entre la fin du pétrissage et le division ?",
                    "answerOptions": [
                        {"text": "Le pointage", "isCorrect": True},
                        {"text": "L'apprêt", "isCorrect": False},
                        {"text": "La détente", "isCorrect": False},
                        {"text": "Le dégazage", "isCorrect": False}
                    ],
                    "correction": "Le pointage est une phase capitale pour le développement des arômes et de la force de la pâte."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel outil utilise le boulanger pour inciser le pain avant l'enfournement ?",
                    "answerOptions": [
                        {"text": "Une lame ou grignette", "isCorrect": True},
                        {"text": "Un couteau de chef", "isCorrect": False},
                        {"text": "Une paire de ciseaux", "isCorrect": False},
                        {"text": "Un coupe-pâte", "isCorrect": False}
                    ],
                    "correction": "Le grignage permet au gaz carbonique de s'échapper de manière contrôlée et donne l'aspect esthétique final."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle technique consiste à replier la pâte sur elle-même pendant le pointage pour lui redonner du corps ?",
                    "answerOptions": [
                        {"text": "Le rabat", "isCorrect": True},
                        {"text": "Le boulage", "isCorrect": False},
                        {"text": "Le façonnage", "isCorrect": False},
                        {"text": "Le laminage", "isCorrect": False}
                    ],
                    "correction": "Le rabat (ou donner un tour) expulse une partie du gaz et renforce le réseau de gluten."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le nom du repos de courte durée après la division et avant le façonnage ?",
                    "answerOptions": [
                        {"text": "La détente", "isCorrect": True},
                        {"text": "Le pointage", "isCorrect": False},
                        {"text": "L'apprêt", "isCorrect": False},
                        {"text": "La scarification", "isCorrect": False}
                    ],
                    "correction": "La détente dure 15 à 30 minutes. Elle permet au gluten de se relâcher pour faciliter l'allongement lors du façonnage."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment appelle-t-on la dernière fermentation du pâton avant la cuisson ?",
                    "answerOptions": [
                        {"text": "L'apprêt", "isCorrect": True},
                        {"text": "Le pointage", "isCorrect": False},
                        {"text": "La poolish", "isCorrect": False},
                        {"text": "Le défournement", "isCorrect": False}
                    ],
                    "correction": "L'apprêt se déroule sur les couches ou en chambre de pousse juste avant la mise au four."
                },
                {
                    "questionNumber": 29,
                    "question": "À quoi sert l'injection de buée (vapeur d'eau) dans le four au moment de l'enfournement ?",
                    "answerOptions": [
                        {"text": "Retarder la formation de la croûte et faire briller", "isCorrect": True},
                        {"text": "Refroidir le four", "isCorrect": False},
                        {"text": "Humidifier la mie", "isCorrect": False},
                        {"text": "Accélérer la cuisson", "isCorrect": False}
                    ],
                    "correction": "La buée permet au pain de se développer au maximum avant que la croûte ne durcisse et donne une belle couleur dorée."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle est la base d'une 'poolish' ?",
                    "answerOptions": [
                        {"text": "Mélange d'eau, de farine et de levure en parts égales", "isCorrect": True},
                        {"text": "Une pâte fermentée de la veille", "isCorrect": False},
                        {"text": "Un mélange de farine de seigle et de miel", "isCorrect": False},
                        {"text": "De la levure chimique dissoute", "isCorrect": False}
                    ],
                    "correction": "La poolish est un levain-levure liquide qui apporte souplesse, arôme et conservation au pain."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le but du 'boulage' ?",
                    "answerOptions": [
                        {"text": "Donner une forme sphérique et lisser la clé", "isCorrect": True},
                        {"text": "Aplatir la pâte", "isCorrect": False},
                        {"text": "Ajouter des graines", "isCorrect": False},
                        {"text": "Diviser la masse en petits morceaux", "isCorrect": False}
                    ],
                    "correction": "Le boulage organise la pâte et prépare la structure pour le façonnage final."
                },
                {
                    "questionNumber": 32,
                    "question": "En pétrissage intensifié, par rapport au pétrissage amélioré :",
                    "answerOptions": [
                        {"text": "La vitesse est plus rapide et le temps plus long", "isCorrect": True},
                        {"text": "La vitesse est plus lente", "isCorrect": False},
                        {"text": "On n'ajoute pas de sel", "isCorrect": False},
                        {"text": "On pétrit à la main uniquement", "isCorrect": False}
                    ],
                    "correction": "Le pétrissage intensifié donne une mie très blanche et très développée, mais au détriment du goût."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment appelle-t-on le pain qui sort du four et commence à perdre son humidité ?",
                    "answerOptions": [
                        {"text": "Le ressuage", "isCorrect": True},
                        {"text": "Le rassissement", "isCorrect": False},
                        {"text": "Le déshuilage", "isCorrect": False},
                        {"text": "L'évaporation", "isCorrect": False}
                    ],
                    "correction": "Le ressuage doit se faire dans un endroit sec et aéré pour que le pain reste croustillant."
                },
                {
                    "questionNumber": 34,
                    "question": "Qu'est-ce que 'la clé' d'un pâton ?",
                    "answerOptions": [
                        {"text": "La soudure de la pâte après le façonnage", "isCorrect": True},
                        {"text": "Le code du cadenas du laboratoire", "isCorrect": False},
                        {"text": "Le milieu de la mie", "isCorrect": False},
                        {"text": "La partie supérieure du pain", "isCorrect": False}
                    ],
                    "correction": "La clé doit généralement être placée en dessous (contre le tapis ou la plaque) pour éviter que le pain ne s'ouvre de manière anarchique."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est la particularité du 'Pain de Tradition Française' ?",
                    "answerOptions": [
                        {"text": "Aucun additif chimique n'est autorisé", "isCorrect": True},
                        {"text": "Il doit être cuit au feu de bois", "isCorrect": False},
                        {"text": "Il ne contient pas de sel", "isCorrect": False},
                        {"text": "Il est fabriqué avec de la farine de seigle", "isCorrect": False}
                    ],
                    "correction": "Le décret de 1993 interdit tout additif (sauf farine de fève, soja ou malt) pour l'appellation 'Tradition'."
                },
                {
                    "questionNumber": 36,
                    "question": "Pourquoi dégazage-t-on légèrement la pâte lors du façonnage ?",
                    "answerOptions": [
                        {"text": "Pour régulariser les alvéoles de la mie", "isCorrect": True},
                        {"text": "Pour faire perdre du poids au pain", "isCorrect": False},
                        {"text": "Pour refroidir la pâte", "isCorrect": False},
                        {"text": "Pour arrêter la levure", "isCorrect": False}
                    ],
                    "correction": "Le dégazage léger permet d'obtenir une structure de mie plus homogène."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment s'appelle l'appareil utilisé pour couper la pâte en morceaux de poids égaux ?",
                    "answerOptions": [
                        {"text": "La diviseuse", "isCorrect": True},
                        {"text": "Le laminoir", "isCorrect": False},
                        {"text": "Le batteur", "isCorrect": False},
                        {"text": "La balance", "isCorrect": False}
                    ],
                    "correction": "La diviseuse (souvent hydraulique) permet de diviser une cuve de pâte en 10 ou 20 pâtons identiques."
                },
                {
                    "questionNumber": 38,
                    "question": "Qu'est-ce que le 'coup de lame' ?",
                    "answerOptions": [
                        {"text": "L'incision faite avant cuisson", "isCorrect": True},
                        {"text": "Le mélange à haute vitesse", "isCorrect": False},
                        {"text": "La découpe du sandwich", "isCorrect": False},
                        {"text": "Le tranchage du pain de mie", "isCorrect": False}
                    ],
                    "correction": "C'est la signature du boulanger qui dirige la levée du pain au four."
                },
                {
                    "questionNumber": 39,
                    "question": "Le terme 'Parisienne' en boulangerie désigne généralement :",
                    "answerOptions": [
                        {"text": "Une baguette de gros diamètre (400g environ)", "isCorrect": True},
                        {"text": "Une petite pâtisserie", "isCorrect": False},
                        {"text": "Une brioche à tête", "isCorrect": False},
                        {"text": "Une farine de luxe", "isCorrect": False}
                    ],
                    "correction": "La Parisienne est plus courte et plus grosse qu'une baguette classique (250g)."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la cause principale d'un pain 'cordé' (mie élastique et dure) ?",
                    "answerOptions": [
                        {"text": "Un excès de pétrissage ou une farine trop forte", "isCorrect": True},
                        {"text": "Un manque d'eau", "isCorrect": False},
                        {"text": "Une cuisson trop froide", "isCorrect": False},
                        {"text": "Un manque de levure", "isCorrect": False}
                    ],
                    "correction": "Un réseau de gluten trop sollicité ou trop résistant rend le pain caoutchouteux."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : HYGIÈNE, SÉCURITÉ ET ENVIRONNEMENT (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : HYGIÈNE, SÉCURITÉ ET ENVIRONNEMENT",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Que signifie le sigle HACCP ?",
                    "answerOptions": [
                        {"text": "Analyse des Dangers et Points Critiques pour leur Maîtrise", "isCorrect": True},
                        {"text": "Hygiène Alimentaire et Contrôle des Commerces de Proximité", "isCorrect": False},
                        {"text": "Haute Autorité de Certification des Produits", "isCorrect": False},
                        {"text": "Homologation Agricole des Céréales de Panification", "isCorrect": False}
                    ],
                    "correction": "L'HACCP est une méthode de gestion de la sécurité sanitaire des aliments."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la température réglementaire de stockage pour les œufs frais ?",
                    "answerOptions": [
                        {"text": "Température ambiante constante (ou +4°C en pro)", "isCorrect": True},
                        {"text": "Au congélateur", "isCorrect": False},
                        {"text": "À 30°C", "isCorrect": False},
                        {"text": "À l'extérieur", "isCorrect": False}
                    ],
                    "correction": "Le plus important est d'éviter les chocs thermiques qui créent de la condensation sur la coquille."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le risque professionnel majeur lié à l'inhalation de poussières de farine ?",
                    "answerOptions": [
                        {"text": "L'asthme du boulanger", "isCorrect": True},
                        {"text": "La surdité", "isCorrect": False},
                        {"text": "Les maux de dos", "isCorrect": False},
                        {"text": "Le diabète", "isCorrect": False}
                    ],
                    "correction": "L'asthme est une maladie professionnelle reconnue, causée par la sensibilisation aux particules de farine en suspension."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle bactérie pathogène est souvent associée à une mauvaise hygiène des mains ?",
                    "answerOptions": [
                        {"text": "Staphylocoque doré", "isCorrect": True},
                        {"text": "Saccharomyces", "isCorrect": False},
                        {"text": "Ferment lactique", "isCorrect": False},
                        {"text": "Glutenine", "isCorrect": False}
                    ],
                    "correction": "Le staphylocoque est présent sur la peau et dans le nez. Un lavage des mains rigoureux est indispensable."
                },
                {
                    "questionNumber": 45,
                    "question": "Dans le cercle de Sinner (TACT), que signifie le 'C' ?",
                    "answerOptions": [
                        {"text": "Chimie (détergent)", "isCorrect": True},
                        {"text": "Cuisson", "isCorrect": False},
                        {"text": "Chaleur", "isCorrect": False},
                        {"text": "Célérité", "isCorrect": False}
                    ],
                    "correction": "Le cercle de Sinner définit les 4 facteurs d'un nettoyage réussi : Température, Action mécanique, Chimie et Temps."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la première chose à faire si un pétrin est en marche et qu'une personne se coince la main ?",
                    "answerOptions": [
                        {"text": "Appuyer sur l'arrêt d'urgence", "isCorrect": True},
                        {"text": "Chercher les secours", "isCorrect": False},
                        {"text": "Renverser de l'eau", "isCorrect": False},
                        {"text": "Appeler le patron", "isCorrect": False}
                    ],
                    "correction": "Toutes les machines de boulangerie possèdent un bouton 'coup de poing' rouge pour un arrêt immédiat."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle tenue est obligatoire pour travailler en production ?",
                    "answerOptions": [
                        {"text": "Veste, pantalon, coiffe et chaussures de sécurité", "isCorrect": True},
                        {"text": "Tablier seul", "isCorrect": False},
                        {"text": "Vêtements de ville propres", "isCorrect": False},
                        {"text": "Gants en caoutchouc", "isCorrect": False}
                    ],
                    "correction": "La tenue protège le produit de l'homme et l'homme des risques du métier."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment appelle-t-on le document qui recense tous les risques de l'entreprise ?",
                    "answerOptions": [
                        {"text": "Le Document Unique (DUERP)", "isCorrect": True},
                        {"text": "La fiche de paie", "isCorrect": False},
                        {"text": "Le carnet de commandes", "isCorrect": False},
                        {"text": "La recette", "isCorrect": False}
                    ],
                    "correction": "Le DUERP est obligatoire dès le premier salarié pour prévenir les accidents du travail."
                },
                {
                    "questionNumber": 49,
                    "question": "À quoi sert la 'marche en avant' ?",
                    "answerOptions": [
                        {"text": "Éviter les contaminations croisées entre le propre et le sale", "isCorrect": True},
                        {"text": "Gagner du temps de marche", "isCorrect": False},
                        {"text": "Faire sortir les clients plus vite", "isCorrect": False},
                        {"text": "Organiser la file d'attente", "isCorrect": False}
                    ],
                    "correction": "Le circuit des matières premières et des déchets ne doit jamais croiser celui des produits finis."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel produit est le plus efficace pour éliminer les bactéries après le nettoyage ?",
                    "answerOptions": [
                        {"text": "Le désinfectant", "isCorrect": True},
                        {"text": "Le savon liquide", "isCorrect": False},
                        {"text": "L'eau claire", "isCorrect": False},
                        {"text": "La farine", "isCorrect": False}
                    ],
                    "correction": "Le nettoyage enlève la saleté, la désinfection tue les micro-organismes."
                },
                {
                    "questionNumber": 51,
                    "question": "Pourquoi faut-il porter des chaussures de sécurité en boulangerie ?",
                    "answerOptions": [
                        {"text": "Protection contre les chutes d'objets et les glissades", "isCorrect": True},
                        {"text": "Pour ne pas salir ses propres chaussures", "isCorrect": False},
                        {"text": "Pour marcher plus vite", "isCorrect": False},
                        {"text": "C'est une tradition", "isCorrect": False}
                    ],
                    "correction": "Les sols de boulangerie peuvent être glissants (farine/eau) et les sacs de farine sont lourds."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle maladie est transmise par les rongeurs (rats/souris) ?",
                    "answerOptions": [
                        {"text": "La leptospirose", "isCorrect": True},
                        {"text": "La grippe", "isCorrect": False},
                        {"text": "Le rhume", "isCorrect": False},
                        {"text": "La fatigue", "isCorrect": False}
                    ],
                    "correction": "D'où l'importance capitale d'un plan de lutte contre les nuisibles."
                },
                {
                    "questionNumber": 53,
                    "question": "Que faire en cas de brûlure légère ?",
                    "answerOptions": [
                        {"text": "Arroser à l'eau tempérée pendant 15 minutes", "isCorrect": True},
                        {"text": "Mettre du beurre", "isCorrect": False},
                        {"text": "Mettre de la farine", "isCorrect": False},
                        {"text": "Souffler dessus", "isCorrect": False}
                    ],
                    "correction": "L'eau tempérée refroidit les tissus en profondeur et limite l'étendue de la lésion."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'objectif du tri des déchets en boulangerie ?",
                    "answerOptions": [
                        {"text": "Favoriser le recyclage et la protection de l'environnement", "isCorrect": True},
                        {"text": "Gagner de l'argent", "isCorrect": False},
                        {"text": "Remplir les poubelles plus vite", "isCorrect": False},
                        {"text": "Faire plaisir au patron", "isCorrect": False}
                    ],
                    "correction": "On sépare le carton, le plastique, les biodéchets et le verre."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est la règle d'or pour le nettoyage du petit matériel ?",
                    "answerOptions": [
                        {"text": "Nettoyage systématique après chaque utilisation", "isCorrect": True},
                        {"text": "Une fois par mois", "isCorrect": False},
                        {"text": "Uniquement quand c'est très sale", "isCorrect": False},
                        {"text": "Le passer uniquement au chiffon sec", "isCorrect": False}
                    ],
                    "correction": "Les résidus de pâte favorisent le développement de moisissures."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel dispositif protège les ouvriers du bruit excessif ?",
                    "answerOptions": [
                        {"text": "Les bouchons d'oreilles ou casque", "isCorrect": True},
                        {"text": "Le bonnet de coton", "isCorrect": False},
                        {"text": "Éteindre les machines", "isCorrect": False},
                        {"text": "Travailler dans le noir", "isCorrect": False}
                    ],
                    "correction": "Certaines machines comme les diviseuses ou refroidisseurs peuvent dépasser 80 décibels."
                },
                {
                    "questionNumber": 57,
                    "question": "Que signifie la date limite de consommation (DLC) ?",
                    "answerOptions": [
                        {"text": "Date au-delà de laquelle le produit est dangereux", "isCorrect": True},
                        {"text": "Date de fabrication", "isCorrect": False},
                        {"text": "Date de mise en vente", "isCorrect": False},
                        {"text": "Date indicative pour le goût", "isCorrect": False}
                    ],
                    "correction": "On ne doit jamais vendre ni consommer un produit dont la DLC est dépassée."
                },
                {
                    "questionNumber": 58,
                    "question": "À quoi sert le lavage des mains ?",
                    "answerOptions": [
                        {"text": "Éliminer les micro-organismes et les souillures", "isCorrect": True},
                        {"text": "Pour avoir les mains douces", "isCorrect": False},
                        {"text": "Pour rafraîchir le boulanger", "isCorrect": False},
                        {"text": "C'est une perte de temps", "isCorrect": False}
                    ],
                    "correction": "Le lavage doit être fait avec du savon bactéricide et séchage au papier jetable."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le risque lié aux Troubles Musculo-Squelettiques (TMS) ?",
                    "answerOptions": [
                        {"text": "Douleurs au dos et aux articulations", "isCorrect": True},
                        {"text": "Problèmes de vue", "isCorrect": False},
                        {"text": "Chute de cheveux", "isCorrect": False},
                        {"text": "Perte de poids", "isCorrect": False}
                    ],
                    "correction": "Le port de charges lourdes (sacs de 25kg) et les gestes répétitifs sont les causes des TMS."
                },
                {
                    "questionNumber": 60,
                    "question": "Pourquoi est-il interdit de fumer au laboratoire ?",
                    "answerOptions": [
                        {"text": "Risque d'incendie et hygiène", "isCorrect": True},
                        {"text": "Car le tabac coûte cher", "isCorrect": False},
                        {"text": "Pour ne pas gêner les voisins", "isCorrect": False},
                        {"text": "C'est autorisé le soir", "isCorrect": False}
                    ],
                    "correction": "Les cendres et mégots sont des contaminants physiques majeurs."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : TECHNOLOGIE DES ÉQUIPEMENTS (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : TECHNOLOGIE DES ÉQUIPEMENTS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel type de pétrin possède un axe oblique et une fourche ?",
                    "answerOptions": [
                        {"text": "Pétrin à axe oblique", "isCorrect": True},
                        {"text": "Pétrin à spirale", "isCorrect": False},
                        {"text": "Batteur mélangeur", "isCorrect": False},
                        {"text": "Pétrin intensif", "isCorrect": False}
                    ],
                    "correction": "C'est le pétrin traditionnel français, très polyvalent."
                },
                {
                    "questionNumber": 62,
                    "question": "Dans quel type de four la chaleur est-elle transmise par un fluide (huile ou vapeur) ?",
                    "answerOptions": [
                        {"text": "Four à soles annulaire", "isCorrect": True},
                        {"text": "Four rotatif", "isCorrect": False},
                        {"text": "Four à convection", "isCorrect": False},
                        {"text": "Four ventilé", "isCorrect": False}
                    ],
                    "correction": "Ces fours offrent une chaleur très douce et une grande inertie."
                },
                {
                    "questionNumber": 63,
                    "question": "À quoi sert le laminoir ?",
                    "answerOptions": [
                        {"text": "Aplatir la pâte et réaliser le feuilletage", "isCorrect": True},
                        {"text": "Cuire le pain", "isCorrect": False},
                        {"text": "Hacher les amandes", "isCorrect": False},
                        {"text": "Pétrir la brioche", "isCorrect": False}
                    ],
                    "correction": "Il permet d'obtenir une épaisseur régulière de pâte pour les croissants ou les tartes."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel organe du four produit la buée ?",
                    "answerOptions": [
                        {"text": "L'appareil à buée (ou générateur)", "isCorrect": True},
                        {"text": "La hotte", "isCorrect": False},
                        {"text": "Le ventilateur", "isCorrect": False},
                        {"text": "L'oura", "isCorrect": False}
                    ],
                    "correction": "L'appareil à buée projette de l'eau sur des masses métalliques brûlantes pour créer la vapeur."
                },
                {
                    "questionNumber": 65,
                    "question": "À quoi sert la balance en boulangerie ?",
                    "answerOptions": [
                        {"text": "Peser les ingrédients et les pâtons", "isCorrect": True},
                        {"text": "Mesurer la température", "isCorrect": False},
                        {"text": "Calculer le temps de cuisson", "isCorrect": False},
                        {"text": "Vérifier la hauteur du pain", "isCorrect": False}
                    ],
                    "correction": "La précision est la clé de la régularité en boulangerie."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le rôle du 'refroidisseur d'eau' ?",
                    "answerOptions": [
                        {"text": "Fournir de l'eau froide pour régler la température de la pâte", "isCorrect": True},
                        {"text": "Geler les pâtons", "isCorrect": False},
                        {"text": "Refroidir le laboratoire", "isCorrect": False},
                        {"text": "Laver le sol", "isCorrect": False}
                    ],
                    "correction": "Il est indispensable en été pour éviter que la pâte ne chauffe trop pendant le pétrissage."
                },
                {
                    "questionNumber": 67,
                    "question": "Dans un four, qu'est-ce que 'l'oura' ?",
                    "answerOptions": [
                        {"text": "Le conduit d'évacuation de la buée", "isCorrect": True},
                        {"text": "La plaque de cuisson", "isCorrect": False},
                        {"text": "La poignée de la porte", "isCorrect": False},
                        {"text": "Le bouton de réglage", "isCorrect": False}
                    ],
                    "correction": "On ouvre l'oura en fin de cuisson pour sécher la croûte du pain."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel pétrin est le plus rapide pour les gros volumes de pâte ?",
                    "answerOptions": [
                        {"text": "Le pétrin à spirale", "isCorrect": True},
                        {"text": "Le pétrin à axe oblique", "isCorrect": False},
                        {"text": "Le batteur ménager", "isCorrect": False},
                        {"text": "Le pétrin à bras plongeants", "isCorrect": False}
                    ],
                    "correction": "Sa vitesse et sa forme de bras permettent un pétrissage rapide et efficace."
                },
                {
                    "questionNumber": 69,
                    "question": "Comment appelle-t-on le chariot utilisé pour le four rotatif ?",
                    "answerOptions": [
                        {"text": "L'échelle", "isCorrect": True},
                        {"text": "La gamelle", "isCorrect": False},
                        {"text": "Le tapis", "isCorrect": False},
                        {"text": "La pelle", "isCorrect": False}
                    ],
                    "correction": "L'échelle supporte les plaques ou les filets qui entrent directement dans le four."
                },
                {
                    "questionNumber": 70,
                    "question": "À quoi sert la 'chambre de fermentation' ?",
                    "answerOptions": [
                        {"text": "Contrôler le temps et la température de pousse", "isCorrect": True},
                        {"text": "Stocker le pain cuit", "isCorrect": False},
                        {"text": "Ranger la farine", "isCorrect": False},
                        {"text": "Nettoyer les outils", "isCorrect": False}
                    ],
                    "correction": "Elle permet de retarder la pousse pour organiser le travail du boulanger."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel accessoire permet d'enfourner le pain sur la sole ?",
                    "answerOptions": [
                        {"text": "Le tapis d'enfournement", "isCorrect": True},
                        {"text": "La louche", "isCorrect": False},
                        {"text": "Le fouet", "isCorrect": False},
                        {"text": "La maryse", "isCorrect": False}
                    ],
                    "correction": "Il glisse les pâtons sur la pierre chaude sans les déformer."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel matériel sert à mélanger les crèmes ou battre les œufs ?",
                    "answerOptions": [
                        {"text": "Le batteur mélangeur", "isCorrect": True},
                        {"text": "La diviseuse", "isCorrect": False},
                        {"text": "Le façonneur", "isCorrect": False},
                        {"text": "La parisienne", "isCorrect": False}
                    ],
                    "correction": "Il possède 3 outils : le crochet (pâtes), la palette (mélanges) et le fouet (émulsions)."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la source d'énergie la plus courante pour les fours de boulangerie ?",
                    "answerOptions": [
                        {"text": "Électricité ou Gaz", "isCorrect": True},
                        {"text": "Charbon", "isCorrect": False},
                        {"text": "Éolien", "isCorrect": False},
                        {"text": "Solaire direct", "isCorrect": False}
                    ],
                    "correction": "Certains utilisent aussi le fioul ou le bois."
                },
                {
                    "questionNumber": 74,
                    "question": "À quoi sert le 'doseur mélangeur' d'eau ?",
                    "answerOptions": [
                        {"text": "Obtenir la quantité et la température d'eau précises", "isCorrect": True},
                        {"text": "Sucrer l'eau", "isCorrect": False},
                        {"text": "Filtrer le calcaire", "isCorrect": False},
                        {"text": "Nettoyer le pétrin", "isCorrect": False}
                    ],
                    "correction": "C'est l'outil indispensable pour respecter la 'température de base'."
                },
                {
                    "questionNumber": 75,
                    "question": "Comment appelle-t-on le plateau sur lequel on pose les baguettes avant cuisson ?",
                    "answerOptions": [
                        {"text": "Le filet de cuisson", "isCorrect": True},
                        {"text": "La poêle", "isCorrect": False},
                        {"text": "La grille", "isCorrect": False},
                        {"text": "L'assiette", "isCorrect": False}
                    ],
                    "correction": "Les filets sont perforés pour laisser circuler l'air chaud."
                },
                {
                    "questionNumber": 76,
                    "question": "Qu'est-ce qu'une 'sole' de four ?",
                    "answerOptions": [
                        {"text": "La pierre réfractaire sur laquelle cuit le pain", "isCorrect": True},
                        {"text": "La porte", "isCorrect": False},
                        {"text": "La lampe", "isCorrect": False},
                        {"text": "Le ventilateur", "isCorrect": False}
                    ],
                    "correction": "Elle accumule la chaleur et la transmet directement par contact au pâton."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel appareil transforme un pâton rond en baguette ?",
                    "answerOptions": [
                        {"text": "La façonneuse", "isCorrect": True},
                        {"text": "La diviseuse", "isCorrect": False},
                        {"text": "Le tamis", "isCorrect": False},
                        {"text": "Le moule", "isCorrect": False}
                    ],
                    "correction": "Elle dégaze, enroule et étire la pâte de manière régulière."
                },
                {
                    "questionNumber": 78,
                    "question": "À quoi sert un 'exterminateur d'insectes' ?",
                    "answerOptions": [
                        {"text": "Éliminer les mouches et insectes volants par UV", "isCorrect": True},
                        {"text": "Nettoyer le four", "isCorrect": False},
                        {"text": "Vérifier la qualité de la farine", "isCorrect": False},
                        {"text": "Attirer les clients", "isCorrect": False}
                    ],
                    "correction": "C'est un équipement d'hygiène obligatoire pour éviter les nuisibles."
                },
                {
                    "questionNumber": 79,
                    "question": "Pourquoi les parois du four sont-elles isolées ?",
                    "answerOptions": [
                        {"text": "Garder la chaleur et économiser l'énergie", "isCorrect": True},
                        {"text": "Pour faire moins de bruit", "isCorrect": False},
                        {"text": "Pour la couleur", "isCorrect": False},
                        {"text": "C'est inutile", "isCorrect": False}
                    ],
                    "correction": "On utilise de la laine de roche ou de verre haute densité."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le rôle du 'pétrin à bras plongeants' ?",
                    "answerOptions": [
                        {"text": "Imiter le mouvement manuel et oxygéner la pâte", "isCorrect": True},
                        {"text": "Couper la pâte", "isCorrect": False},
                        {"text": "Cuire la pâte", "isCorrect": False},
                        {"text": "Peser la pâte", "isCorrect": False}
                    ],
                    "correction": "Il chauffe très peu la pâte et respecte les arômes."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : CULTURE PROFESSIONNELLE ET PRODUITS (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : CULTURE PROFESSIONNELLE ET PRODUITS",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le poids moyen d'une baguette classique avant cuisson ?",
                    "answerOptions": [
                        {"text": "300g à 350g", "isCorrect": True},
                        {"text": "100g", "isCorrect": False},
                        {"text": "500g", "isCorrect": False},
                        {"text": "1kg", "isCorrect": False}
                    ],
                    "correction": "Elle pèsera environ 250g après cuisson (perte de poids par évaporation)."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la forme caractéristique du 'pain de seigle' ?",
                    "answerOptions": [
                        {"text": "Souvent en boule ou en miche", "isCorrect": True},
                        {"text": "En baguette très longue", "isCorrect": False},
                        {"text": "En couronne", "isCorrect": False},
                        {"text": "En triangle", "isCorrect": False}
                    ],
                    "correction": "Le seigle contient peu de gluten et se façonne mieux en formes compactes."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel ingrédient caractérise la 'brioche' ?",
                    "answerOptions": [
                        {"text": "Beurre et œufs", "isCorrect": True},
                        {"text": "Eau et farine de seigle", "isCorrect": False},
                        {"text": "Huile d'olive", "isCorrect": False},
                        {"text": "Vin blanc", "isCorrect": False}
                    ],
                    "correction": "C'est une pâte levée riche, classée dans les viennoiseries."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le nom du saint patron des boulangers ?",
                    "answerOptions": [
                        {"text": "Saint Honoré", "isCorrect": True},
                        {"text": "Saint Nicolas", "isCorrect": False},
                        {"text": "Saint Joseph", "isCorrect": False},
                        {"text": "Saint Michel", "isCorrect": False}
                    ],
                    "correction": "Sa fête est célébrée le 16 mai par la profession."
                },
                {
                    "questionNumber": 85,
                    "question": "Qu'est-ce que le 'levain naturel' ?",
                    "answerOptions": [
                        {"text": "Mélange de farine et d'eau ayant fermenté spontanément", "isCorrect": True},
                        {"text": "De la levure pressée délayée", "isCorrect": False},
                        {"text": "De la poudre chimique", "isCorrect": False},
                        {"text": "Du sucre fondu", "isCorrect": False}
                    ],
                    "correction": "Il utilise les levures et bactéries sauvages naturellement présentes dans l'air et la farine."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est l'origine du croissant ?",
                    "answerOptions": [
                        {"text": "Autriche (Vienne)", "isCorrect": True},
                        {"text": "France (Paris)", "isCorrect": False},
                        {"text": "Italie (Rome)", "isCorrect": False},
                        {"text": "Espagne (Madrid)", "isCorrect": False}
                    ],
                    "correction": "D'où le nom de 'viennoiserie' donné à cette famille de produits."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment appelle-t-on le pain de 400g à 500g ?",
                    "answerOptions": [
                        {"text": "La miche ou le pain", "isCorrect": True},
                        {"text": "La ficelle", "isCorrect": False},
                        {"text": "Le bâtard", "isCorrect": False},
                        {"text": "Le petit pain", "isCorrect": False}
                    ],
                    "correction": "Il est environ deux fois plus gros qu'une baguette."
                },
                {
                    "questionNumber": 88,
                    "question": "Dans quel produit utilise-t-on de la 'pâte fermentée' ?",
                    "answerOptions": [
                        {"text": "Dans le pain courant pour apporter du goût", "isCorrect": True},
                        {"text": "Dans les tartes aux fruits", "isCorrect": False},
                        {"text": "Uniquement dans le pain complet", "isCorrect": False},
                        {"text": "Dans les gâteaux secs", "isCorrect": False}
                    ],
                    "correction": "C'est un reste de pâte à pain du jour précédent."
                },
                {
                    "questionNumber": 89,
                    "question": "Le pain 'complet' est fabriqué avec :",
                    "answerOptions": [
                        {"text": "De la farine T150", "isCorrect": True},
                        {"text": "De la farine de maïs", "isCorrect": False},
                        {"text": "Un mélange de 10 céréales", "isCorrect": False},
                        {"text": "Uniquement de la farine de gruau", "isCorrect": False}
                    ],
                    "correction": "Il est plus riche en fibres et minéraux."
                },
                {
                    "questionNumber": 90,
                    "question": "Qu'est-ce qu'une 'ficelle' ?",
                    "answerOptions": [
                        {"text": "Une baguette très fine (125g environ)", "isCorrect": True},
                        {"text": "Une corde pour attacher les sacs", "isCorrect": False},
                        {"text": "Un pain rond", "isCorrect": False},
                        {"text": "Une viennoiserie sucrée", "isCorrect": False}
                    ],
                    "correction": "Elle est très appréciée pour son maximum de croûte."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le taux de sel maximum recommandé pour le pain ?",
                    "answerOptions": [
                        {"text": "1,8% du poids de farine", "isCorrect": True},
                        {"text": "5%", "isCorrect": False},
                        {"text": "10%", "isCorrect": False},
                        {"text": "0,5%", "isCorrect": False}
                    ],
                    "correction": "Cet engagement de la profession aide à lutter contre l'hypertension."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle céréale donne une mie très sombre et serrée ?",
                    "answerOptions": [
                        {"text": "Le Seigle", "isCorrect": True},
                        {"text": "Le Froment", "isCorrect": False},
                        {"text": "Le Riz", "isCorrect": False},
                        {"text": "L'Orge", "isCorrect": False}
                    ],
                    "correction": "Le pain de seigle est traditionnel pour accompagner les fruits de mer."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment appelle-t-on le mélange Farine + Beurre + Sucre + Œufs + Levure ?",
                    "answerOptions": [
                        {"text": "Une pâte levée sucrée", "isCorrect": True},
                        {"text": "Une pâte brisée", "isCorrect": False},
                        {"text": "Une pâte sablée", "isCorrect": False},
                        {"text": "Un appareil à cake", "isCorrect": False}
                    ],
                    "correction": "C'est la base de la brioche et de la kouglof."
                },
                {
                    "questionNumber": 94,
                    "question": "Le pain 'Viennois' se distingue par :",
                    "answerOptions": [
                        {"text": "L'ajout de lait et de sucre et des incisions rapprochées", "isCorrect": True},
                        {"text": "Sa cuisson à la vapeur", "isCorrect": False},
                        {"text": "Son absence de sel", "isCorrect": False},
                        {"text": "Sa forme de bretzel", "isCorrect": False}
                    ],
                    "correction": "Il a une mie très souple et une croûte fine et brillante."
                },
                {
                    "questionNumber": 95,
                    "question": "À quoi sert le 'poinçonnage' du pain de seigle ?",
                    "answerOptions": [
                        {"text": "Décorer et éviter que le pain n'éclate", "isCorrect": True},
                        {"text": "Marquer le prix", "isCorrect": False},
                        {"text": "Faire entrer de l'air", "isCorrect": False},
                        {"text": "Vérifier la cuisson", "isCorrect": False}
                    ],
                    "correction": "On utilise un poinçon pour piquer la pâte avant enfournement."
                },
                {
                    "questionNumber": 96,
                    "question": "Qu'est-ce qu'une 'fougasse' ?",
                    "answerOptions": [
                        {"text": "Un pain plat sculpté originaire de Provence", "isCorrect": True},
                        {"text": "Une brioche de Noël", "isCorrect": False},
                        {"text": "Un biscuit sec", "isCorrect": False},
                        {"text": "Un type de farine", "isCorrect": False}
                    ],
                    "correction": "Elle peut être nature ou garnie (olives, lardons, fromage)."
                },
                {
                    "questionNumber": 97,
                    "question": "Le pH d'un pain au levain par rapport à un pain à la levure est :",
                    "answerOptions": [
                        {"text": "Plus acide", "isCorrect": True},
                        {"text": "Plus basique", "isCorrect": False},
                        {"text": "Identique", "isCorrect": False},
                        {"text": "Neutre", "isCorrect": False}
                    ],
                    "correction": "La fermentation au levain produit de l'acide acétique et lactique, abaissant le pH de la pâte (environ 4,0 - 4,5) et donnant cette saveur acidulée typique."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le principal défaut d'un croissant qui n'a pas assez reposé au froid entre les tours ?",
                    "answerOptions": [
                        {"text": "Le marbrage", "isCorrect": True},
                        {"text": "Le piquage", "isCorrect": False},
                        {"text": "Le cloquage", "isCorrect": False},
                        {"text": "Le grignage", "isCorrect": False}
                    ],
                    "correction": "Si la pâte ne repose pas au froid, le beurre ramollit et se mélange à la pâte au lieu de rester en couche distincte : on perd le feuilletage."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle forme donne-t-on traditionnellement à une brioche 'Nanterre' ?",
                    "answerOptions": [
                        {"text": "Rectangulaire avec plusieurs boules", "isCorrect": True},
                        {"text": "Ronde avec une tête au sommet", "isCorrect": False},
                        {"text": "Couronne avec des fruits confits", "isCorrect": False},
                        {"text": "Tresse à trois branches", "isCorrect": False}
                    ],
                    "correction": "Elle est composée de plusieurs petites boules de pâte rangées côte à côte dans un moule cake qui se soudent à la cuisson."
                },
                {
                    "questionNumber": 100,
                    "question": "Dans la recette du pain de campagne, quel ingrédient apporte la note rustique ?",
                    "answerOptions": [
                        {"text": "Farine de seigle ou complète", "isCorrect": True},
                        {"text": "Farine de maïs jaune", "isCorrect": False},
                        {"text": "Farine de riz", "isCorrect": False},
                        {"text": "Sucre glace", "isCorrect": False}
                    ],
                    "correction": "L'ajout d'une petite proportion de seigle (souvent 10%) donne sa couleur et son goût typique au pain de campagne."
                }
            ]
        }
    }
}