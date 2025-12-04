quiz_data = {
    "title": "Quiz CAP Boulanger : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MATIÈRES PREMIÈRES & ADDITIFS (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Matières Premières & Additifs (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est le rôle principal de l'amidon présent dans la farine lors de la panification ?",
                    "answerOptions": [
                        {"text": "Apporter la couleur jaune au pain.", "isCorrect": False},
                        {"text": "Former le réseau glutineux.", "isCorrect": False},
                        {"text": "Servir de nourriture à la levure pendant la fermentation.", "isCorrect": True},
                        {"text": "Fixer le sel dans la pâte.", "isCorrect": False}
                    ],
                    "correction": "L'**amidon** est le principal glucide de la farine. Il est dégradé en sucres simples par les enzymes (amylases) pour servir de nourriture aux levures, produisant du CO2 et de l'alcool."
                },
                {
                    "questionNumber": 2,
                    "question": "Qu'indique le taux de cendres (ou indice de cendre) d'une farine, souvent désigné par le type (T45, T55, T65) ?",
                    "answerOptions": [
                        {"text": "Le taux d'humidité de la farine.", "isCorrect": False},
                        {"text": "La quantité de protéines (gluten).", "isCorrect": False},
                        {"text": "La teneur en matières minérales (résidus de l'enveloppe du grain).", "isCorrect": True},
                        {"text": "La date de péremption.", "isCorrect": False}
                    ],
                    "correction": "Le taux de cendres est le poids des résidus minéraux. Plus l'indice est élevé (T80, T110...), plus la farine contient de **matières minérales** (plus elle est complète)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le nom de la principale protéine de la farine qui, hydratée et travaillée, forme le réseau élastique de la pâte ?",
                    "answerOptions": [
                        {"text": "La Fibrine.", "isCorrect": False},
                        {"text": "Le Lysine.", "isCorrect": False},
                        {"text": "Le **Gluten**.", "isCorrect": True},
                        {"text": "L'Amylose.", "isCorrect": False}
                    ],
                    "correction": "Le **gluten** (gliadine et gluténine) forme le réseau visco-élastique capable de retenir les gaz de fermentation."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le rôle de la levure boulangère (*Saccharomyces cerevisiae*) dans la panification ?",
                    "answerOptions": [
                        {"text": "Rendre la pâte plus blanche.", "isCorrect": False},
                        {"text": "Transformer le sucre en acide acétique.", "isCorrect": False},
                        {"text": "Produire du gaz carbonique (CO2) pour faire lever la pâte.", "isCorrect": True},
                        {"text": "Améliorer la résistance du gluten.", "isCorrect": False}
                    ],
                    "correction": "La levure est responsable de la **fermentation alcoolique**. Elle produit de l'**éthanol** et du **dioxyde de carbone (CO2)**."
                },
                {
                    "questionNumber": 5,
                    "question": "Pourquoi utilise-t-on le sel dans la pâte à pain ?",
                    "answerOptions": [
                        {"text": "Pour accélérer la pousse de la pâte.", "isCorrect": False},
                        {"text": "Pour ralentir la fermentation et renforcer le réseau glutineux.", "isCorrect": True},
                        {"text": "Pour diminuer le taux d'hydratation.", "isCorrect": False},
                        {"text": "Pour inhiber l'action des amylases.", "isCorrect": False}
                    ],
                    "correction": "Le **sel** apporte la saveur, **ralentit l'activité de la levure** et **renforce la ténacité** du gluten."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la principale caractéristique d'une farine de type 45 (T45), idéale pour les viennoiseries et pâtisseries fines ?",
                    "answerOptions": [
                        {"text": "Elle est riche en son (farine complète).", "isCorrect": False},
                        {"text": "Elle est forte en gluten (W élevé).", "isCorrect": True},
                        {"text": "Elle est principalement composée d'amidon.", "isCorrect": False},
                        {"text": "Elle ne contient aucun minéral.", "isCorrect": False}
                    ],
                    "correction": "Une T45 est très raffinée et souvent issue de blés plus forts, ce qui lui confère une **grande qualité en gluten** (W élevé)."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est l'enzyme présente dans la farine qui dégrade l'amidon en sucres fermentescibles pour la levure ?",
                    "answerOptions": [
                        {"text": "La Lipase.", "isCorrect": False},
                        {"text": "La Protéase.", "isCorrect": False},
                        {"text": "L'**Amylase**.", "isCorrect": True},
                        {"text": "La Broméline.", "isCorrect": False}
                    ],
                    "correction": "Les **amylases** (alpha et bêta) hydrolysent l'amidon en sucres (maltose) directement assimilables par la levure."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel rôle l'eau joue-t-elle dans la pâte à pain, en plus d'hydrater la farine ?",
                    "answerOptions": [
                        {"text": "Servir de catalyseur à l'extraction de la graisse.", "isCorrect": False},
                        {"text": "Rendre la croûte plus brillante.", "isCorrect": False},
                        {"text": "Permettre la formation du gluten et l'activation des enzymes et levures.", "isCorrect": True},
                        {"text": "Diminuer la température de base.", "isCorrect": False}
                    ],
                    "correction": "L'eau est essentielle pour **hydrater les protéines** (formation du gluten) et pour servir de **milieu de vie** aux levures et aux bactéries."
                },
                {
                    "questionNumber": 9,
                    "question": "Qu'est-ce qui est mesuré par le test de l'Alvéographe de Chopin sur une farine ?",
                    "answerOptions": [
                        {"text": "Le taux de sel.", "isCorrect": False},
                        {"text": "La couleur de la mie.", "isCorrect": False},
                        {"text": "La force (W) et l'élasticité (L) du gluten.", "isCorrect": True},
                        {"text": "L'humidité du grain.", "isCorrect": False}
                    ],
                    "correction": "L'**alvéographe** mesure la **force boulangère (W)** (résistance) et l'**extensibilité (L)** (capacité à s'étirer) du gluten."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel type de farine est généralement utilisé pour le pain de seigle ?",
                    "answerOptions": [
                        {"text": "T45 ou T55.", "isCorrect": False},
                        {"text": "T65.", "isCorrect": False},
                        {"text": "T130 ou T170.", "isCorrect": True},
                        {"text": "Farine de maïs.", "isCorrect": False}
                    ],
                    "correction": "Le seigle est souvent utilisé sous forme de types foncés (**T130, T170**), car elles sont riches en minéraux et limitent la formation de gluten."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel additif courant est parfois ajouté pour blanchir légèrement la pâte et renforcer le gluten, bien que son usage soit en déclin ?",
                    "answerOptions": [
                        {"text": "Le chlorure de potassium.", "isCorrect": False},
                        {"text": "La farine de fèves.", "isCorrect": True},
                        {"text": "Le dextrose.", "isCorrect": False},
                        {"text": "L'acide citrique.", "isCorrect": False}
                    ],
                    "correction": "La **farine de fèves** (ou de soja) est utilisée pour ses propriétés enzymatiques et oxydantes, elle améliore la **blancheur** et renforce légèrement le gluten."
                },
                {
                    "questionNumber": 12,
                    "question": "Dans la formule de l'hydratation, l'eau doit idéalement avoir quelle dureté (quantité de minéraux) pour être optimale ?",
                    "answerOptions": [
                        {"text": "Très douce (déminéralisée).", "isCorrect": False},
                        {"text": "Dure (riche en calcaire).", "isCorrect": False},
                        {"text": "Légèrement calcaire (dureté moyenne).", "isCorrect": True},
                        {"text": "Acide (pH faible).", "isCorrect": False}
                    ],
                    "correction": "Une eau **légèrement calcaire** est idéale. Les sels minéraux renforcent le gluten. Une eau trop douce donne une pâte molle."
                },
                {
                    "questionNumber": 13,
                    "question": "Qu'est-ce qu'une farine qualifiée de 'faible' (W faible) ?",
                    "answerOptions": [
                        {"text": "Une farine qui absorbe peu d'eau et dont la pâte est molle.", "isCorrect": True},
                        {"text": "Une farine idéale pour la baguette de tradition.", "isCorrect": False},
                        {"text": "Une farine avec un faible taux de cendres.", "isCorrect": False},
                        {"text": "Une farine très riche en matières grasses.", "isCorrect": False}
                    ],
                    "correction": "Une farine **faible (W < 180)** manque de force et ne supporte pas bien les longues fermentations."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel ingrédient est le plus susceptible de bloquer ou de tuer la levure s'il est mis en contact direct avec elle lors du pétrissage ?",
                    "answerOptions": [
                        {"text": "L'eau froide.", "isCorrect": False},
                        {"text": "Le sucre.", "isCorrect": False},
                        {"text": "Le **Sel**.", "isCorrect": True},
                        {"text": "La farine de seigle.", "isCorrect": False}
                    ],
                    "correction": "Le **sel** est hypertonique ; un contact direct et prolongé peut déshydrater et **tuer** la levure par osmose."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel terme désigne le phénomène par lequel l'amidon gonfle en présence d'eau et de chaleur, ce qui contribue à la texture de la mie lors de la cuisson ?",
                    "answerOptions": [
                        {"text": "Le pointage.", "isCorrect": False},
                        {"text": "La saccharification.", "isCorrect": False},
                        {"text": "La **Gélatinisation** de l'amidon.", "isCorrect": True},
                        {"text": "La réticulation du gluten.", "isCorrect": False}
                    ],
                    "correction": "La **gélatinisation** se produit au-delà de 60 °C à cœur. Les grains d'amidon gonflent, fixent l'eau et structurent la mie."
                },
                {
                    "questionNumber": 16,
                    "question": "Le pain de tradition française est défini par un décret. Quel ingrédient, hormis la farine de blé, l'eau, le sel et la levure/levain, est autorisé ?",
                    "answerOptions": [
                        {"text": "L'huile de palme.", "isCorrect": False},
                        {"text": "Le beurre.", "isCorrect": False},
                        {"text": "Le gluten de blé.", "isCorrect": True},
                        {"text": "La fécule de pomme de terre.", "isCorrect": False}
                    ],
                    "correction": "Le **Décret Pain de 1993** autorise, de manière réglementée, le **gluten de blé** (pour corriger les farines faibles)."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est l'influence d'une trop grande quantité d'eau (hydratation trop élevée) sur la pâte pétrie ?",
                    "answerOptions": [
                        {"text": "La pâte devient trop ferme et difficile à travailler.", "isCorrect": False},
                        {"text": "Le réseau glutineux est renforcé.", "isCorrect": False},
                        {"text": "La pâte est collante, difficile à façonner, mais favorise une mie aérée.", "isCorrect": True},
                        {"text": "Elle augmente la teneur en sucre de la pâte.", "isCorrect": False}
                    ],
                    "correction": "Une forte hydratation rend le travail plus difficile (pâte collante) mais favorise une meilleure activité enzymatique et une **mie très alvéolée**."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la température idéale (ou T° de base) que l'on cherche à obtenir pour la pâte en fin de pétrissage afin de maîtriser le départ de la fermentation ?",
                    "answerOptions": [
                        {"text": "15 °C.", "isCorrect": False},
                        {"text": "**24 °C à 26 °C**.", "isCorrect": True},
                        {"text": "35 °C.", "isCorrect": False},
                        {"text": "40 °C.", "isCorrect": False}
                    ],
                    "correction": "Une température entre **24 °C et 26 °C** est souvent visée pour garantir un départ lent et maîtrisé des levures et des bactéries."
                },
                {
                    "questionNumber": 19,
                    "question": "Comment appelle-t-on le mélange de sel et d'eau glacée que l'on peut utiliser pour baisser la température de la pâte à pétrir ?",
                    "answerOptions": [
                        {"text": "Le liquide de masse.", "isCorrect": False},
                        {"text": "La glace carbonique.", "isCorrect": False},
                        {"text": "La saumure.", "isCorrect": True},
                        {"text": "L'eau osmotique.", "isCorrect": False}
                    ],
                    "correction": "L'eau salée ou **saumure** est utilisée pour dissoudre le sel et intégrer de l'eau froide plus facilement, aidant à contrôler la température."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel rôle la matière grasse (beurre, huile) joue-t-elle dans une pâte à viennoiserie ou une pâte riche (comme la brioche) ?",
                    "answerOptions": [
                        {"text": "Elle renforce le gluten et donne une texture très dure.", "isCorrect": False},
                        {"text": "Elle fragilise le gluten et donne du moelleux et du fondant.", "isCorrect": True},
                        {"text": "Elle sert de carburant principal à la levure.", "isCorrect": False},
                        {"text": "Elle augmente le temps de cuisson.", "isCorrect": False}
                    ],
                    "correction": "Le **gras** **fragilise le réseau glutineux** en l'enrobant, ce qui confère le **moelleux** et le fondant à la mie et améliore la conservation."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNIQUES DE FABRICATION & PÂTES LEVÉES (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Techniques de Fabrication & Pâtes Levées (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le but de la phase de frasage en début de pétrissage ?",
                    "answerOptions": [
                        {"text": "Incorporer les œufs et le sucre.", "isCorrect": False},
                        {"text": "Développer le réseau glutineux immédiatement.", "isCorrect": False},
                        {"text": "Mélanger la farine et l'eau pour obtenir une pâte homogène et hydratée.", "isCorrect": True},
                        {"text": "Introduire l'air dans la pâte pour la blanchir.", "isCorrect": False}
                    ],
                    "correction": "Le **frasage** est la première phase pour mélanger tous les ingrédients jusqu'à l'obtention d'une masse homogène, sans chercher à développer le gluten."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est l'intérêt de la technique de l'autolyse ?",
                    "answerOptions": [
                        {"text": "Accélérer le pétrissage en machine.", "isCorrect": False},
                        {"text": "Remplacer la levure par le levain.", "isCorrect": False},
                        {"text": "Permettre au gluten de s'hydrater pour améliorer l'extensibilité de la pâte et réduire le pétrissage.", "isCorrect": True},
                        {"text": "Ajouter les inclusions (graines, fruits secs).", "isCorrect": False}
                    ],
                    "correction": "L'**autolyse** (mélange farine/eau, puis repos) permet au gluten de bien s'hydrater passivement, facilitant son développement et augmentant l'extensibilité."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel défaut peut engendrer un pétrissage trop intensif sur la qualité du pain ?",
                    "answerOptions": [
                        {"text": "Manque de coloration de la croûte.", "isCorrect": False},
                        {"text": "Chauffer la pâte et provoquer l'oxydation (blanchiment) de la mie.", "isCorrect": True},
                        {"text": "Un pain trop lourd et dense.", "isCorrect": False},
                        {"text": "Un goût trop acide.", "isCorrect": False}
                    ],
                    "correction": "Un pétrissage trop long ou trop rapide (intensifié) surchauffe la pâte, oxyde les pigments, ce qui **blanchit la mie** et dégrade les arômes."
                },
                {
                    "questionNumber": 24,
                    "question": "Que signifie le terme bassinage en boulangerie ?",
                    "answerOptions": [
                        {"text": "Laver la farine avant utilisation.", "isCorrect": False},
                        {"text": "Ajouter progressivement de l'eau au cours du pétrissage.", "isCorrect": True},
                        {"text": "Laisser la pâte reposer sous l'eau.", "isCorrect": False},
                        {"text": "Mettre de la vapeur dans le four.", "isCorrect": False}
                    ],
                    "correction": "Le **bassinage** est l'action d'ajouter de l'eau supplémentaire (hors recette initiale) au cours du pétrissage pour augmenter l'hydratation de la pâte."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le rôle principal du pointage (ou fermentation en masse) après le pétrissage ?",
                    "answerOptions": [
                        {"text": "Cuire partiellement le pain.", "isCorrect": False},
                        {"text": "Développer le goût, la couleur et le volume de la pâte.", "isCorrect": True},
                        {"text": "Former la pâte en vue de la cuisson.", "isCorrect": False},
                        {"text": "Incorporer les matières grasses.", "isCorrect": False}
                    ],
                    "correction": "Le **pointage** est la première fermentation (en masse). Il permet la production de gaz (volume) et d'acides organiques (goût), et le gluten continue de se structurer."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle technique permet de dégazzer la pâte et de lui redonner de la force en milieu de pointage ?",
                    "answerOptions": [
                        {"text": "Le bouler.", "isCorrect": False},
                        {"text": "Le **rabat** (ou 'rompre').", "isCorrect": True},
                        {"text": "Le pétrissage intensif.", "isCorrect": False},
                        {"text": "La division.", "isCorrect": False}
                    ],
                    "correction": "Le **rabat** consiste à replier la pâte sur elle-même pour chasser le gaz carbonique et **redonner de la force** et de la tenue au réseau glutineux."
                },
                {
                    "questionNumber": 27,
                    "question": "À quelle étape de la fabrication le boulanger doit-il effectuer la pesée de ses pâtons ?",
                    "answerOptions": [
                        {"text": "Après la cuisson.", "isCorrect": False},
                        {"text": "Après le pétrissage.", "isCorrect": False},
                        {"text": "Après le pointage et avant la détente (étape de **division**).", "isCorrect": True},
                        {"text": "Avant le frasage.", "isCorrect": False}
                    ],
                    "correction": "La pesée (ou **division**) est l'action de découper la masse de pâte après le pointage pour obtenir des morceaux de poids exacts."
                },
                {
                    "questionNumber": 28,
                    "question": "Qu'est-ce que le terme 'détente' ou 'pré-façonnage' après la division ?",
                    "answerOptions": [
                        {"text": "Le moment où la pâte se relâche après le pétrissage.", "isCorrect": False},
                        {"text": "Un court repos des pâtons après la division pour les rendre plus faciles à façonner.", "isCorrect": True},
                        {"text": "La phase finale avant l'enfournement.", "isCorrect": False},
                        {"text": "L'ajout d'une matière grasse sur le plan de travail.", "isCorrect": False}
                    ],
                    "correction": "La **détente** est un court repos (15 à 30 minutes) pour relâcher le réseau glutineux et permettre un façonnage plus facile et sans déchirure."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le but principal de l'étape du façonnage ?",
                    "answerOptions": [
                        {"text": "Faire pousser la pâte à sa taille maximale.", "isCorrect": False},
                        {"text": "Donner la forme finale au pâton et emprisonner les gaz.", "isCorrect": True},
                        {"text": "Mesurer la température de la pâte.", "isCorrect": False},
                        {"text": "Mélanger les ingrédients restants.", "isCorrect": False}
                    ],
                    "correction": "Le **façonnage** consiste à donner la forme souhaitée (boule, bâtard, ficelle, etc.) tout en reformant le réseau glutineux pour retenir les gaz."
                },
                {
                    "questionNumber": 30,
                    "question": "Comment appelle-t-on le temps de repos de la pâte qui a lieu après le façonnage et avant l'enfournement ?",
                    "answerOptions": [
                        {"text": "Le pointage.", "isCorrect": False},
                        {"text": "Le frasage.", "isCorrect": False},
                        {"text": "L'**apprêt**.", "isCorrect": True},
                        {"text": "La détente.", "isCorrect": False}
                    ],
                    "correction": "L'**apprêt** est la seconde et dernière phase de fermentation (après le façonnage). C'est le moment où le pâton prend son volume final."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la conséquence d'un apprêt insuffisant (pâte pas assez fermentée) ?",
                    "answerOptions": [
                        {"text": "Le pain s'étale excessivement à la cuisson.", "isCorrect": False},
                        {"text": "Une mie trop serrée et une forte déchirure de la croûte (**pousse au four excessive**).", "isCorrect": True},
                        {"text": "Un goût trop acide.", "isCorrect": False},
                        {"text": "Une croûte molle.", "isCorrect": False}
                    ],
                    "correction": "Si l'apprêt est insuffisant, la chaleur du four provoque une **poussée explosive** et la mie est souvent serrée."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'outil ou le contenant utilisé pour soutenir le pâton lors de l'apprêt et lui donner sa forme finale (souvent de la vannerie) ?",
                    "answerOptions": [
                        {"text": "La couche.", "isCorrect": False},
                        {"text": "Le fournil.", "isCorrect": False},
                        {"text": "Le **banneton**.", "isCorrect": True},
                        {"text": "Le laminoir.", "isCorrect": False}
                    ],
                    "correction": "Le **banneton** soutient la pâte et l'empêche de s'étaler pendant l'apprêt."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment calcule-t-on la Température de Base (TB) pour déterminer la température de l'eau de coulage ? (Formule classique)",
                    "answerOptions": [
                        {"text": "TB = Température de la farine + Température du four.", "isCorrect": False},
                        {"text": "TB = (Température de la farine + Température du fournil) x 3.", "isCorrect": False},
                        {"text": "**TB = 54 (ou 56) – (Température de la farine + Température du fournil)**.", "isCorrect": True},
                        {"text": "TB = 24 + Température du fournil.", "isCorrect": False}
                    ],
                    "correction": "La formule classique est **T° de l'eau = Température de Base – (T° farine + T° fournil)**."
                },
                {
                    "questionNumber": 34,
                    "question": "À quoi sert la petite quantité d'huile ou de graisse (ou le saupoudrage de farine) lors de la détrempe d'une pâte à brioche ou à croissant ?",
                    "answerOptions": [
                        {"text": "Remplacer la levure.", "isCorrect": False},
                        {"text": "Empêcher l'adhérence de la pâte aux parois de la cuve pendant le pétrissage.", "isCorrect": True},
                        {"text": "Blanchir la mie.", "isCorrect": False},
                        {"text": "Épaissir la pâte.", "isCorrect": False}
                    ],
                    "correction": "La matière grasse ou la farine spéciale aide à empêcher les pâtes très hydratées ou riches de **coller excessivement au pétrin**."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le rôle de la semoule (ou du son) saupoudrée sous les pâtons ?",
                    "answerOptions": [
                        {"text": "Donner un goût sucré.", "isCorrect": False},
                        {"text": "Améliorer le développement du gluten.", "isCorrect": False},
                        {"text": "**Empêcher le pâton de coller** à son support (banneton, plaque, toile de couche).", "isCorrect": True},
                        {"text": "Accélérer l'oxydation de la pâte.", "isCorrect": False}
                    ],
                    "correction": "La **semoule** est utilisée comme agent de démoulage/anti-adhésif sous les pâtons pour faciliter la manipulation et l'enfournement."
                },
                {
                    "questionNumber": 36,
                    "question": "Pourquoi le pain de seigle est-il souvent fabriqué sans rabat et avec un pétrissage moins intensif ?",
                    "answerOptions": [
                        {"text": "Le seigle ne supporte pas l'oxydation.", "isCorrect": False},
                        {"text": "Le seigle n'a pas de gluten et ne nécessite pas de renforcement.", "isCorrect": True},
                        {"text": "La pâte de seigle fermente trop rapidement.", "isCorrect": False},
                        {"text": "Le seigle est trop cher pour gaspiller du temps.", "isCorrect": False}
                    ],
                    "correction": "La farine de seigle ne forme pas de véritable réseau glutineux. La manipuler (rabat, pétrissage intensif) n'apporterait **aucun bénéfice structurel**."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment appelle-t-on le procédé qui consiste à pulvériser de l'eau sur la pâte juste avant l'enfournement ?",
                    "answerOptions": [
                        {"text": "La brumisation.", "isCorrect": False},
                        {"text": "Le mouillage.", "isCorrect": True},
                        {"text": "La vaporisation.", "isCorrect": False},
                        {"text": "L'arrosage.", "isCorrect": False}
                    ],
                    "correction": "Le **mouillage** (ou la pulvérisation d'eau) permet de retarder la formation de la croûte, facilitant ainsi l'ouverture de la grigne et le développement du pain."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est le rôle de la couche (toile de lin ou de coton) dans le processus de fabrication ?",
                    "answerOptions": [
                        {"text": "Protéger le pain des insectes.", "isCorrect": False},
                        {"text": "**Soutenir et séparer les pâtons** allongés pendant l'apprêt.", "isCorrect": True},
                        {"text": "Évacuer l'humidité.", "isCorrect": False},
                        {"text": "Garder la pâte au chaud pour la cuisson.", "isCorrect": False}
                    ],
                    "correction": "La **couche** est la toile qui reçoit les pâtons après façonnage pour l'apprêt. Elle absorbe légèrement l'humidité et soutient les pâtons pour éviter qu'ils ne s'étalent."
                },
                {
                    "questionNumber": 39,
                    "question": "Qu'est-ce que le façonnage 'bouler' ?",
                    "answerOptions": [
                        {"text": "Façonner la pâte en forme de boudin.", "isCorrect": False},
                        {"text": "**Rendre la surface du pâton tendue et lisse** en le roulant sous la main.", "isCorrect": True},
                        {"text": "Le laisser pousser sans manipulation.", "isCorrect": False},
                        {"text": "L'aplatir au laminoir.", "isCorrect": False}
                    ],
                    "correction": "Le **bouler** consiste à donner une forme sphérique au pâton en lissant et en tendant sa surface, créant une 'peau' tendue pour la pousse."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est le principal objectif du repos des pâtons après la division et le bouler (la détente) ?",
                    "answerOptions": [
                        {"text": "Augmenter le goût acide.", "isCorrect": False},
                        {"text": "**Relâcher les tensions** dues à la division pour faciliter le façonnage final.", "isCorrect": True},
                        {"text": "Faire couler l'eau hors de la pâte.", "isCorrect": False},
                        {"text": "Augmenter la température.", "isCorrect": False}
                    ],
                    "correction": "La **détente** (repos intermédiaire) permet de relaxer le réseau glutineux, le rendant plus souple et plus facile à manipuler pour le façonnage final."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : PROCESSUS DE FERMENTATION & CUISSON (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Processus de Fermentation & Cuisson (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le but principal de l'injection de vapeur (buée) dans le four au moment de l'enfournement ?",
                    "answerOptions": [
                        {"text": "Diminuer la température de la sole du four.", "isCorrect": False},
                        {"text": "Accélérer la cuisson à cœur.", "isCorrect": False},
                        {"text": "Retarder la formation de la croûte et permettre le développement du pain (**pousse au four**).", "isCorrect": True},
                        {"text": "Apporter de l'humidité à la mie.", "isCorrect": False}
                    ],
                    "correction": "La buée empêche la croûte de se former et de se rigidifier trop vite, permettant au pain de se développer au maximum (le **coup de four**)."
                },
                {
                    "questionNumber": 42,
                    "question": "Comment appelle-t-on le phénomène de dégradation de la mie qui se produit lorsque le pain refroidit (durcissement et perte d'humidité) ?",
                    "answerOptions": [
                        {"text": "Le ressuage.", "isCorrect": False},
                        {"text": "L'oxydation.", "isCorrect": False},
                        {"text": "Le **rassissement**.", "isCorrect": True},
                        {"text": "La réticulation.", "isCorrect": False}
                    ],
                    "correction": "Le **rassissement** est principalement dû à la **rétrogradation de l'amidon**. Les chaînes d'amidon se réorganisent, expulsant l'eau."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est l'outil utilisé pour entailler la surface du pain juste avant l'enfournement ?",
                    "answerOptions": [
                        {"text": "Le coupe-pâte.", "isCorrect": False},
                        {"text": "La **lame de boulanger (ou grignette)**.", "isCorrect": True},
                        {"text": "Le triangle.", "isCorrect": False},
                        {"text": "Le racloir.", "isCorrect": False}
                    ],
                    "correction": "La **grignette** est utilisée pour réaliser la **grigne**. Cette incision dirigée permet au pain de se développer de manière contrôlée et esthétique lors de l'expansion due à la chaleur."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le rôle principal des bactéries lactiques présentes dans le levain ?",
                    "answerOptions": [
                        {"text": "Fixer le sel dans la pâte.", "isCorrect": False},
                        {"text": "Produire majoritairement du CO2 pour la levée.", "isCorrect": False},
                        {"text": "Produire de l'**acide lactique et de l'acide acétique** pour le goût et l'amélioration de la conservation.", "isCorrect": True},
                        {"text": "Empêcher l'amidon de gélatiniser.", "isCorrect": False}
                    ],
                    "correction": "Les bactéries lactiques transforment les sucres en **acides lactique et acétique**. Ces acides confèrent le goût du levain et servent de conservateurs naturels."
                },
                {
                    "questionNumber": 45,
                    "question": "Sous quelle forme la levure est-elle la plus active et produit-elle le plus de CO2 ?",
                    "answerOptions": [
                        {"text": "À température très froide (0-4 °C).", "isCorrect": False},
                        {"text": "Sous forme de poudre.", "isCorrect": False},
                        {"text": "À une température optimale autour de **25-35 °C**.", "isCorrect": True},
                        {"text": "À des températures supérieures à 60 °C.", "isCorrect": False}
                    ],
                    "correction": "L'activité métabolique de la levure est maximale dans une plage de température tiède. Au-delà de 45-50 °C, elle meurt (dénaturation)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le nom de la technique de cuisson qui consiste à d'abord cuire le pain à haute température (ex. 250 °C) puis à baisser progressivement la température (ex. 220 °C) ?",
                    "answerOptions": [
                        {"text": "Le croustillage.", "isCorrect": False},
                        {"text": "La cuisson indirecte.", "isCorrect": False},
                        {"text": "La cuisson avec **dégressivité** (ou à chaleur tombante).", "isCorrect": True},
                        {"text": "La surgélation.", "isCorrect": False}
                    ],
                    "correction": "La cuisson **dégressive** utilise une chaleur forte au début pour le coup de four, puis une chaleur plus douce pour assurer une cuisson homogène à cœur sans brûler la croûte."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le danger d'un apprêt trop long (surfermentation) ?",
                    "answerOptions": [
                        {"text": "Le pain n'aura pas de croûte.", "isCorrect": False},
                        {"text": "La pâte devient trop acide, s'affaisse et ne peut plus se développer au four.", "isCorrect": True},
                        {"text": "Le gluten devient trop fort.", "isCorrect": False},
                        {"text": "La température interne reste trop froide.", "isCorrect": False}
                    ],
                    "correction": "Une pâte en **surapprêt** a épuisé sa réserve de gaz et le réseau glutineux est fragilisé par les acides. Le pâton s'étale et manque de *spring*."
                },
                {
                    "questionNumber": 48,
                    "question": "Qu'est-ce qui est ajouté au levain chef pour l'activer et l'entretenir, créant ainsi un levain liquide ou solide prêt à l'emploi ?",
                    "answerOptions": [
                        {"text": "Du sel et du sucre.", "isCorrect": False},
                        {"text": "De la levure de bière.", "isCorrect": False},
                        {"text": "Un mélange de **farine et d'eau** (le rafraîchi).", "isCorrect": True},
                        {"text": "Du jus de fruit.", "isCorrect": False}
                    ],
                    "correction": "Le **rafraîchi** est l'action de nourrir le levain chef (souche mère) avec de l'eau et de la farine, ce qui le réactive et le multiplie."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est la température interne minimale (à cœur) que doit atteindre un pain pour être considéré comme cuit et permettre la gélatinisation complète de l'amidon ?",
                    "answerOptions": [
                        {"text": "45 °C.", "isCorrect": False},
                        {"text": "65 °C.", "isCorrect": False},
                        {"text": "**93 °C à 98 °C**.", "isCorrect": True},
                        {"text": "120 °C.", "isCorrect": False}
                    ],
                    "correction": "La cuisson est complète lorsque le centre du pain atteint **93 °C à 98 °C**. C'est le signe que l'amidon est gélatinisé."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment appelle-t-on la réaction chimique responsable de la coloration brune de la croûte et du développement des arômes de pain (entre sucres et protéines) ?",
                    "answerOptions": [
                        {"text": "La caramélisation.", "isCorrect": False},
                        {"text": "La thermolyse.", "isCorrect": False},
                        {"text": "La **Réaction de Maillard**.", "isCorrect": True},
                        {"text": "La réticulation.", "isCorrect": False}
                    ],
                    "correction": "La **Réaction de Maillard** (à partir de 140 °C) est la réaction entre les acides aminés (protéines) et les sucres qui produit les composés aromatiques et la couleur brune."
                },
                {
                    "questionNumber": 51,
                    "question": "Dans la technique de la pousse lente ou retardée (ex: pousse en chambre froide), quel ingrédient faut-il généralement ajuster ?",
                    "answerOptions": [
                        {"text": "Augmenter le sel.", "isCorrect": False},
                        {"text": "**Diminuer la quantité de levure**.", "isCorrect": True},
                        {"text": "Augmenter la quantité d'eau.", "isCorrect": False},
                        {"text": "Diminuer la quantité de farine.", "isCorrect": False}
                    ],
                    "correction": "Pour éviter la surfermentation pendant les longues périodes au froid (8 à 24 heures), il faut **réduire drastiquement la levure** (souvent de 50 à 75 %)."
                },
                {
                    "questionNumber": 52,
                    "question": "Qu'est-ce que le poolish ?",
                    "answerOptions": [
                        {"text": "Un type de façonnage.", "isCorrect": False},
                        {"text": "Une pâte fermentée très ferme.", "isCorrect": False},
                        {"text": "Une **pré-fermentation liquide (eau et farine à parts égales)** avec levure.", "isCorrect": True},
                        {"text": "Le nom du four à bois.", "isCorrect": False}
                    ],
                    "correction": "La **poolish** est une pré-fermentation réalisée avec la même quantité d'eau et de farine (T.A. 100). Elle est très utilisée pour développer les arômes."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la principale différence entre la fermentation alcoolique et la fermentation lactique ?",
                    "answerOptions": [
                        {"text": "L'une produit de la chaleur, l'autre pas.", "isCorrect": False},
                        {"text": "L'une nécessite du sel, l'autre non.", "isCorrect": False},
                        {"text": "L'une produit du CO2 et de l'alcool (levures), l'autre des acides (bactéries).", "isCorrect": True},
                        {"text": "L'une est aérobie, l'autre anaérobie.", "isCorrect": False}
                    ],
                    "correction": "La **fermentation alcoolique** produit du gaz (CO2), la **fermentation lactique** produit des acides organiques (lactique, acétique)."
                },
                {
                    "questionNumber": 54,
                    "question": "Pourquoi retire-t-on le pain du four sur une grille pour le faire refroidir ?",
                    "answerOptions": [
                        {"text": "Pour couper la cuisson immédiatement.", "isCorrect": False},
                        {"text": "Pour éviter la **condensation** (le ressuage) sous le pain qui ramollirait la croûte.", "isCorrect": True},
                        {"text": "Pour le laisser s'oxyder.", "isCorrect": False},
                        {"text": "Pour accélérer le rassissement.", "isCorrect": False}
                    ],
                    "correction": "Le pain libère de la vapeur (**ressuage**). Le mettre sur une grille permet à l'air de circuler dessous, empêchant l'humidité de ramollir la croûte inférieure."
                },
                {
                    "questionNumber": 55,
                    "question": "Lors de l'enfournement, la montée rapide de la pâte au four est due à l'expansion de l'air et du CO2. Comment appelle-t-on ce phénomène ?",
                    "answerOptions": [
                        {"text": "L'autolyse.", "isCorrect": False},
                        {"text": "Le ressuage.", "isCorrect": False},
                        {"text": "Le **coup de four** (*oven spring*).", "isCorrect": True},
                        {"text": "La dégressivité.", "isCorrect": False}
                    ],
                    "correction": "Le **coup de four** est l'augmentation de volume (jusqu'à 40% du volume final) qui se produit dans les 10 à 15 premières minutes de cuisson."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel défaut de cuisson est souvent dû à une température de four trop faible et/ou une durée insuffisante ?",
                    "answerOptions": [
                        {"text": "Croûte brûlée.", "isCorrect": False},
                        {"text": "Pain trop acide.", "isCorrect": False},
                        {"text": "Croûte trop dure et mie crue ou collante (manque de gélatinisation).", "isCorrect": True},
                        {"text": "Mie trop aérée.", "isCorrect": False}
                    ],
                    "correction": "Une cuisson insuffisante n'atteint pas la température interne requise (93 °C+) pour gélatiniser l'amidon, laissant une mie **collante, dense ou caoutchouteuse**."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'est-ce que le pâte fermentée (ou vieille pâte) ?",
                    "answerOptions": [
                        {"text": "Un levain chef qui n'a pas été rafraîchi.", "isCorrect": False},
                        {"text": "Un morceau de pâte à pain mis de côté du pétrissage précédent.", "isCorrect": True},
                        {"text": "Une pâte à brioche périmée.", "isCorrect": False},
                        {"text": "Un mélange d'eau et de farine cuit.", "isCorrect": False}
                    ],
                    "correction": "La **pâte fermentée** est un ajout de pâte non cuite issue de la production précédente. Elle est riche en saveurs et sert de pré-fermentation."
                },
                {
                    "questionNumber": 58,
                    "question": "Pourquoi doit-on s'assurer que la sole du four (plancher) est bien chaude avant d'enfourner ?",
                    "answerOptions": [
                        {"text": "Pour empêcher la caramélisation.", "isCorrect": False},
                        {"text": "Pour transférer immédiatement la chaleur et provoquer un bon développement du pain.", "isCorrect": True},
                        {"text": "Pour refroidir le pain.", "isCorrect": False},
                        {"text": "Pour assécher la mie.", "isCorrect": False}
                    ],
                    "correction": "La sole chaude est essentielle pour un bon **transfert de chaleur** immédiat à la base du pâton, évitant que le pain ne s'étale."
                },
                {
                    "questionNumber": 59,
                    "question": "À quelle température l'activité de la levure est-elle totalement stoppée (dénaturée ou tuée) ?",
                    "answerOptions": [
                        {"text": "15 °C.", "isCorrect": False},
                        {"text": "Entre **50 °C et 55 °C** (et au-delà).", "isCorrect": True},
                        {"text": "25 °C.", "isCorrect": False},
                        {"text": "80 °C.", "isCorrect": False}
                    ],
                    "correction": "Les cellules de levure sont tuées par la chaleur à partir de **50 °C à cœur**. Une fois cette température atteinte, la production de gaz cesse."
                },
                {
                    "questionNumber": 60,
                    "question": "Un pain au levain a souvent une meilleure conservation que le pain à la levure. Quelle est la principale raison ?",
                    "answerOptions": [
                        {"text": "Le levain est plus riche en gluten.", "isCorrect": False},
                        {"text": "Les acides organiques (lactique et acétique) produits par le levain ralentissent la dégradation et la moisissure.", "isCorrect": True},
                        {"text": "Le levain ne gélatinise pas l'amidon.", "isCorrect": False},
                        {"text": "Le levain demande une cuisson plus longue.", "isCorrect": False}
                    ],
                    "correction": "Les **acides organiques** créent un environnement défavorable aux moisissures et ralentissent le rassissement du pain."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : BOULANGERIE SPÉCIALE & VIENNOISERIE (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Boulangerie Spéciale & Viennoiserie (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le nom de l'opération qui consiste à insérer le beurre de tourage dans la détrempe d'une pâte levée feuilletée (ex. croissant) ?",
                    "answerOptions": [
                        {"text": "Le détrempage.", "isCorrect": False},
                        {"text": "L'incrustation.", "isCorrect": False},
                        {"text": "L'**encartage**.", "isCorrect": True},
                        {"text": "La fonte.", "isCorrect": False}
                    ],
                    "correction": "L'**encartage** est la technique qui consiste à enfermer le rectangle de beurre de tourage dans la détrempe avant de commencer le feuilletage."
                },
                {
                    "questionNumber": 62,
                    "question": "Pourquoi utilise-t-on une farine de force boulangère élevée (W élevé) pour la pâte à brioche et la pâte à croissant ?",
                    "answerOptions": [
                        {"text": "Pour obtenir une croûte plus fine.", "isCorrect": False},
                        {"text": "Pour diminuer le temps de cuisson.", "isCorrect": False},
                        {"text": "Pour supporter l'ajout important de matière grasse et de sucre.", "isCorrect": True},
                        {"text": "Pour bloquer la fermentation.", "isCorrect": False}
                    ],
                    "correction": "Une farine forte est indispensable pour que le gluten résiste à l'effet **fragilisant** du beurre et du sucre (ingrédients riches)."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est le rôle principal du sucre dans la pâte à brioche ?",
                    "answerOptions": [
                        {"text": "Donner de la structure à la mie.", "isCorrect": False},
                        {"text": "Servir de nourriture principale pour la levure et donner une belle coloration (Maillard).", "isCorrect": True},
                        {"text": "Rendre la pâte plus ferme.", "isCorrect": False},
                        {"text": "Accélérer le rancissement.", "isCorrect": False}
                    ],
                    "correction": "Le sucre est la source d'énergie de la levure et, surtout, garantit la **coloration** de la croûte grâce à la Réaction de Maillard."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la fonction principale du poids des œufs dans une recette de viennoiserie ou de brioche riche ?",
                    "answerOptions": [
                        {"text": "Remplacer l'eau.", "isCorrect": False},
                        {"text": "Apporter de la couleur, du liant, et du gras (matière grasse).", "isCorrect": True},
                        {"text": "Augmenter le taux de sel.", "isCorrect": False},
                        {"text": "Accélérer le pétrissage.", "isCorrect": False}
                    ],
                    "correction": "Les œufs apportent de la couleur et des **lipides** (gras) qui contribuent au moelleux et au goût."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle doit être la température idéale du beurre de tourage au moment du feuilletage des croissants ?",
                    "answerOptions": [
                        {"text": "Très chaude (température ambiante).", "isCorrect": False},
                        {"text": "**Souple et plastique, autour de 10-14 °C**.", "isCorrect": True},
                        {"text": "Congelée (0 °C).", "isCorrect": False},
                        {"text": "Fondue (25 °C).", "isCorrect": False}
                    ],
                    "correction": "Le beurre doit être **plastique** pour s'étaler sans s'incorporer à la détrempe ni la déchirer."
                },
                {
                    "questionNumber": 66,
                    "question": "Dans la fabrication des croissants, que signifie l'expression 'donner un tour simple' ?",
                    "answerOptions": [
                        {"text": "Plier la pâte en deux.", "isCorrect": False},
                        {"text": "Plier la pâte en quatre.", "isCorrect": False},
                        {"text": "**Plier la pâte en trois** (comme un portefeuille).", "isCorrect": True},
                        {"text": "Plier la pâte en six.", "isCorrect": False}
                    ],
                    "correction": "Un **tour simple** consiste à plier la pâte feuilletée en trois (3 épaisseurs de pâte). Deux tours simples confèrent théoriquement 10 couches de pâte et 9 de beurre."
                },
                {
                    "questionNumber": 67,
                    "question": "Qu'est-ce que le craquelin dans le contexte du pain ou de la viennoiserie ?",
                    "answerOptions": [
                        {"text": "Le mélange de sel et d'eau.", "isCorrect": False},
                        {"text": "Le nom donné à la grigne du pain.", "isCorrect": False},
                        {"text": "Le **mélange de pâte à choux, de beurre et de sucre** utilisé comme décor sur certains pains (ex. pain brioché).", "isCorrect": True},
                        {"text": "La pâte à beignets avant friture.", "isCorrect": False}
                    ],
                    "correction": "Le **craquelin** est une pâte croquante que l'on dépose sur une viennoiserie avant l'apprêt et la cuisson pour ajouter de la texture."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est l'objectif principal du fraisage d'une pâte à brioche (après le pétrissage de base) ?",
                    "answerOptions": [
                        {"text": "Réchauffer la pâte pour accélérer la pousse.", "isCorrect": False},
                        {"text": "**Lisser la pâte et incorporer le beurre** de manière homogène.", "isCorrect": True},
                        {"text": "Donner la forme finale.", "isCorrect": False},
                        {"text": "Rendre la pâte moins extensible.", "isCorrect": False}
                    ],
                    "correction": "Le **fraisage** est le pétrissage final après l'incorporation de toute la matière grasse. Il est effectué pour lisser et homogénéiser la pâte."
                },
                {
                    "questionNumber": 69,
                    "question": "Pourquoi est-il important de laisser reposer la pâte feuilletée entre chaque tour ?",
                    "answerOptions": [
                        {"text": "Pour que le beurre fonde.", "isCorrect": False},
                        {"text": "Pour que le sel s'incorpore.", "isCorrect": False},
                        {"text": "Pour **relâcher les tensions du gluten** et éviter qu'elle ne se rétracte.", "isCorrect": True},
                        {"text": "Pour que la levure produise plus de CO2.", "isCorrect": False}
                    ],
                    "correction": "Le repos (souvent au froid) permet au gluten de se **détendre** après le laminage et au beurre de garder sa consistance."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel type de farine est couramment utilisé dans la confection de la pâte à choux (ex: éclairs, chouquettes) ?",
                    "answerOptions": [
                        {"text": "T150.", "isCorrect": False},
                        {"text": "**T45** (souvent Pâtissière, faible en gluten).", "isCorrect": True},
                        {"text": "T110.", "isCorrect": False},
                        {"text": "Farine de seigle.", "isCorrect": False}
                    ],
                    "correction": "La pâte à choux lève par la vapeur d'eau. On utilise souvent une **T45** (farine de pâtisserie) pour sa finesse."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment appelle-t-on le procédé qui permet de donner une couleur dorée et brillante aux viennoiseries avant cuisson ?",
                    "answerOptions": [
                        {"text": "Le mouillage.", "isCorrect": False},
                        {"text": "Le saupoudrage.", "isCorrect": False},
                        {"text": "La **dorure** (à l'œuf ou au lait).", "isCorrect": True},
                        {"text": "L'autolyse.", "isCorrect": False}
                    ],
                    "correction": "La **dorure** (généralement œuf battu) est appliquée avant l'enfournement pour garantir une croûte uniforme, dorée et brillante."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le défaut majeur si la température de la chambre de pousse (apprêt) est trop élevée pour une pâte à croissant ?",
                    "answerOptions": [
                        {"text": "La pâte ne lève pas.", "isCorrect": False},
                        {"text": "La pâte devient trop sèche.", "isCorrect": False},
                        {"text": "Le **beurre fond et s'incorpore** à la détrempe, ruinant le feuilletage.", "isCorrect": True},
                        {"text": "Le pain devient trop acide.", "isCorrect": False}
                    ],
                    "correction": "Si la température est trop élevée, le beurre fond. Il n'y a plus de couches distinctes et donc **pas de feuilletage** à la cuisson."
                },
                {
                    "questionNumber": 73,
                    "question": "Dans la fabrication du pain de mie, quel est l'effet de l'ajout d'une matière grasse (ex: beurre ou huile) ?",
                    "answerOptions": [
                        {"text": "Rendre la croûte plus épaisse.", "isCorrect": False},
                        {"text": "**Permettre un filage plus long de la mie et améliorer la conservation**.", "isCorrect": True},
                        {"text": "Diminuer l'extensibilité.", "isCorrect": False},
                        {"text": "Accélérer l'acidification.", "isCorrect": False}
                    ],
                    "correction": "La matière grasse (avec le sucre) contribue au **moelleux** du pain de mie, le préserve du rassissement et permet un **filage** de la mie."
                },
                {
                    "questionNumber": 74,
                    "question": "Qu'est-ce qu'une pâte fermentée riche dans le contexte de la boulangerie spéciale ?",
                    "answerOptions": [
                        {"text": "Une pâte enrichie en minéraux.", "isCorrect": False},
                        {"text": "Une pâte à pain classique avec beaucoup de sel.", "isCorrect": False},
                        {"text": "Une pâte contenant une **quantité significative de beurre et/ou de sucre** (ex: pain au lait).", "isCorrect": True},
                        {"text": "Une pâte qui a fermenté pendant 72 heures.", "isCorrect": False}
                    ],
                    "correction": "Une pâte est dite **riche** lorsqu'elle est fortement enrichie en ingrédients non basiques comme les **matières grasses, les sucres, les œufs ou le lait**."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le rôle de la semoule de blé dur dans la fabrication de pains spéciaux comme le pain de campagne ou le pain de tradition ?",
                    "answerOptions": [
                        {"text": "Elle remplace la levure.", "isCorrect": False},
                        {"text": "Elle apporte une **couleur jaune, un goût spécifique et une structure plus rustique**.", "isCorrect": True},
                        {"text": "Elle empêche le pain de lever.", "isCorrect": False},
                        {"text": "Elle augmente l'élasticité du gluten.", "isCorrect": False}
                    ],
                    "correction": "La semoule apporte une **saveur de noisette** caractéristique et rend la mie plus jaune et la croûte plus croustillante."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment appelle-t-on le procédé qui consiste à rouler la pâte du croissant dans le sens de la longueur pour lui donner sa forme finale ?",
                    "answerOptions": [
                        {"text": "Le laminage.", "isCorrect": False},
                        {"text": "L'incrustation.", "isCorrect": False},
                        {"text": "Le **roulage** (ou enroulement).", "isCorrect": True},
                        {"text": "Le fonçage.", "isCorrect": False}
                    ],
                    "correction": "Le **roulage** est l'action d'enrouler le triangle de pâte sur lui-même en partant de la base jusqu'à la pointe pour former le croissant."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel défaut est souvent observé si l'on utilise un levain trop jeune (pas assez mûr) pour la fabrication de pains spéciaux ?",
                    "answerOptions": [
                        {"text": "Le pain a un goût trop acide.", "isCorrect": False},
                        {"text": "Le pain n'aura pas une bonne pousse (**manque de force**).", "isCorrect": True},
                        {"text": "Le pain brûle à la cuisson.", "isCorrect": False},
                        {"text": "La mie est trop blanche.", "isCorrect": False}
                    ],
                    "correction": "Un levain jeune manque d'activité microbienne (levures et bactéries) et n'aura **pas assez de force** pour assurer le développement et le volume de la pâte."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel ingrédient est ajouté pour augmenter la teneur en fibres et le goût rustique des pains complets (T110) ou intégraux (T150) ?",
                    "answerOptions": [
                        {"text": "Le sel.", "isCorrect": False},
                        {"text": "Du sucre inverti.", "isCorrect": False},
                        {"text": "Du **son** (enveloppe du grain).", "isCorrect": True},
                        {"text": "De l'huile d'olive.", "isCorrect": False}
                    ],
                    "correction": "Le **son** est l'enveloppe du grain de blé, réintroduit dans les farines de type élevé (T110, T150) pour augmenter leur teneur en fibres et minéraux."
                },
                {
                    "questionNumber": 79,
                    "question": "Que se passe-t-il si la chambre de pousse (apprêt) est trop humide pour les viennoiseries dorées ?",
                    "answerOptions": [
                        {"text": "Le pain devient trop acide.", "isCorrect": False},
                        {"text": "La dorure coule et le produit a un aspect terne et tâché.", "isCorrect": True},
                        {"text": "La levure ne s'active pas.", "isCorrect": False},
                        {"text": "Le beurre gèle.", "isCorrect": False}
                    ],
                    "correction": "Une humidité excessive peut faire **couler la dorure** et ramollir l'extérieur, donnant un aspect final mou, terne et irrégulier."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la principale différence entre une baguette de tradition française et une baguette courante ?",
                    "answerOptions": [
                        {"text": "La tradition est cuite à plus haute température.", "isCorrect": False},
                        {"text": "La tradition est obligatoirement faite à base de levure pressée.", "isCorrect": False},
                        {"text": "La tradition doit être faite sans aucun additif, avec une fermentation longue et obligatoirement à la farine de blé T65.", "isCorrect": True},
                        {"text": "La tradition est seulement plus courte.", "isCorrect": False}
                    ],
                    "correction": "Le **Décret Pain de 1993** définit la Tradition comme une pâte sans additifs (sauf farine, eau, sel, levure/levain et gluten de blé), avec une fermentation lente."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : HYGIÈNE, SÉCURITÉ & GESTION DE LA PRODUCTION (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Hygiène, Sécurité & Gestion de la Production (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le principe de base de la méthode HACCP (Hazard Analysis Critical Control Point) ?",
                    "answerOptions": [
                        {"text": "Analyser les coûts et les profits.", "isCorrect": False},
                        {"text": "**Identifier, évaluer et maîtriser les dangers** significatifs pour la sécurité alimentaire.", "isCorrect": True},
                        {"text": "Gérer les stocks de matières premières.", "isCorrect": False},
                        {"text": "Remplacer le sel par le levain.", "isCorrect": False}
                    ],
                    "correction": "L'**HACCP** est un système préventif d'autocontrôle qui garantit la salubrité des aliments en identifiant et en contrôlant les points critiques (CCP)."
                },
                {
                    "questionNumber": 82,
                    "question": "Que doit-on obligatoirement porter en boulangerie pour prévenir la chute de cheveux et la contamination des aliments ?",
                    "answerOptions": [
                        {"text": "Des gants en nitrile.", "isCorrect": False},
                        {"text": "Un tablier jetable.", "isCorrect": False},
                        {"text": "Une **coiffe ou une toque**.", "isCorrect": True},
                        {"text": "Des chaussures de ville.", "isCorrect": False}
                    ],
                    "correction": "La **coiffe** est obligatoire dans tous les secteurs alimentaires pour éviter la contamination physique et microbienne des produits par les cheveux."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la procédure d'hygiène à respecter pour le nettoyage des mains après avoir touché de l'argent ou manipulé des déchets ?",
                    "answerOptions": [
                        {"text": "Se rincer les mains à l'eau froide uniquement.", "isCorrect": False},
                        {"text": "Utiliser un essuie-tout sans savon.", "isCorrect": False},
                        {"text": "Lavage avec savon, rinçage, séchage avec essuie-mains à usage unique.", "isCorrect": True},
                        {"text": "Se frictionner avec de la farine.", "isCorrect": False}
                    ],
                    "correction": "Le lavage des mains doit être complet et le séchage doit se faire avec un **essuie-mains jetable** pour éviter la recontamination."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la principale source de risque microbiologique dans l'atelier pour les produits cuits (post-cuisson) ?",
                    "answerOptions": [
                        {"text": "L'eau.", "isCorrect": False},
                        {"text": "La farine.", "isCorrect": False},
                        {"text": "Le **personnel** (mains, vêtements, toux, etc.).", "isCorrect": True},
                        {"text": "Le sel.", "isCorrect": False}
                    ],
                    "correction": "Le personnel est le vecteur principal de **contamination croisée** entre les zones propres (après cuisson) et les zones sales."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le Danger Physique le plus fréquent que l'on peut retrouver dans le pain fini ?",
                    "answerOptions": [
                        {"text": "La présence de levures.", "isCorrect": False},
                        {"text": "La présence de salmonelle.", "isCorrect": False},
                        {"text": "La présence de **morceaux de métal, de verre ou de bois** (ou cheveux).", "isCorrect": True},
                        {"text": "La présence d'acides lactiques.", "isCorrect": False}
                    ],
                    "correction": "Un **danger physique** est un corps étranger (ex: débris, cheveux) qui peut causer des blessures au consommateur."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le temps maximal autorisé pour la durée de vie du pain après sa fabrication avant qu'il ne soit plus considéré comme 'frais' ?",
                    "answerOptions": [
                        {"text": "6 heures.", "isCorrect": False},
                        {"text": "**24 heures** (selon la législation française).", "isCorrect": True},
                        {"text": "48 heures.", "isCorrect": False},
                        {"text": "7 jours.", "isCorrect": False}
                    ],
                    "correction": "Selon la loi française, le pain est considéré comme **frais** et peut être vendu comme tel pendant **24 heures** après sa cuisson."
                },
                {
                    "questionNumber": 87,
                    "question": "Qu'est-ce que la traçabilité en production alimentaire ?",
                    "answerOptions": [
                        {"text": "La liste des ingrédients.", "isCorrect": False},
                        {"text": "La capacité de **retrouver l'historique et le parcours d'un produit** à travers toutes les étapes de fabrication et de distribution.", "isCorrect": True},
                        {"text": "La durée de vie maximale du produit.", "isCorrect": False},
                        {"text": "Le coût de fabrication.", "isCorrect": False}
                    ],
                    "correction": "La **traçabilité** est essentielle pour identifier rapidement la source d'un problème et retirer les produits concernés du marché."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le risque de sécurité le plus courant lié à l'utilisation des pétrins mécaniques ?",
                    "answerOptions": [
                        {"text": "Incendie électrique.", "isCorrect": False},
                        {"text": "Coupure par la lame.", "isCorrect": False},
                        {"text": "**Entraînement des mains ou des vêtements** par le bras ou la spirale.", "isCorrect": True},
                        {"text": "Inhalation de poussière de farine.", "isCorrect": False}
                    ],
                    "correction": "Le risque majeur est l'écrasement ou l'amputation. L'utilisation du **cache de sécurité** est obligatoire pendant le fonctionnement."
                },
                {
                    "questionNumber": 89,
                    "question": "Que devez-vous faire des restes de pâte crue non utilisée (ex: chute de viennoiserie) ?",
                    "answerOptions": [
                        {"text": "Les jeter immédiatement dans la poubelle.", "isCorrect": False},
                        {"text": "Les réincorporer dans la nouvelle pâte à pain (sauf viennoiserie).", "isCorrect": False},
                        {"text": "Les **identifier, stocker au froid et les utiliser dans les 24 heures (ou congeler)**.", "isCorrect": True},
                        {"text": "Les laisser sur le plan de travail.", "isCorrect": False}
                    ],
                    "correction": "Les restes de pâte doivent être **identifiés, stockés au froid** pour ralentir la pousse, et utilisés rapidement (méthode de la pâte fermentée)."
                },
                {
                    "questionNumber": 90,
                    "question": "Dans le cadre de l'hygiène, qu'est-ce que le principe de la marche en avant ?",
                    "answerOptions": [
                        {"text": "Avancer la cuisson progressivement.", "isCorrect": False},
                        {"text": "**Séparer les zones propres des zones sales** pour éviter la contamination croisée.", "isCorrect": True},
                        {"text": "Avancer la date de péremption.", "isCorrect": False},
                        {"text": "Toujours mélanger l'eau chaude et l'eau froide.", "isCorrect": False}
                    ],
                    "correction": "La **marche en avant** garantit que le produit va toujours de la zone la plus contaminante (réception) vers la zone la plus saine (produits finis), sans retour en arrière."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le rôle principal de la fiche technique de fabrication ?",
                    "answerOptions": [
                        {"text": "Décrire l'histoire du produit.", "isCorrect": False},
                        {"text": "**Assurer la constance de la qualité, du coût et du poids** du produit fini.", "isCorrect": True},
                        {"text": "Remplacer la législation.", "isCorrect": False},
                        {"text": "Servir de support publicitaire.", "isCorrect": False}
                    ],
                    "correction": "La fiche technique est la **garantie de la standardisation et de la rentabilité** (maîtrise des coûts matières et des rendements)."
                },
                {
                    "questionNumber": 92,
                    "question": "Comment doit-on stocker la farine et les sacs dans le local de stockage ?",
                    "answerOptions": [
                        {"text": "Directement sur le sol, contre le mur.", "isCorrect": False},
                        {"text": "Sur des palettes ou des rayonnages, décollés des murs.", "isCorrect": True},
                        {"text": "Empilés les uns sur les autres sans ordre.", "isCorrect": False},
                        {"text": "Dans la chambre froide.", "isCorrect": False}
                    ],
                    "correction": "Le stockage sur **palettes (ou racks)**, éloigné des murs, est essentiel pour faciliter le nettoyage et prévenir les nuisibles."
                },
                {
                    "questionNumber": 93,
                    "question": "Quelle est la zone de danger pour la prolifération des bactéries (Température Danger Zone - TDZ) à éviter absolument lors de la conservation des aliments ?",
                    "answerOptions": [
                        {"text": "Inférieur à 0 °C.", "isCorrect": False},
                        {"text": "De 63 °C à 100 °C.", "isCorrect": False},
                        {"text": "**Entre +8 °C et +63 °C**.", "isCorrect": True},
                        {"text": "De 0 °C à +2 °C.", "isCorrect": False}
                    ],
                    "correction": "La **TDZ** est la plage de température où les bactéries se multiplient le plus rapidement. Les aliments doivent être très froids (sous +3 °C) ou très chauds (au-dessus de +63 °C)."
                },
                {
                    "questionNumber": 94,
                    "question": "Que signifie DLC sur un produit alimentaire ?",
                    "answerOptions": [
                        {"text": "Date Limite de Consommation Recommandée.", "isCorrect": False},
                        {"text": "**Date Limite de Consommation** (Doit être consommée avant cette date).", "isCorrect": True},
                        {"text": "Délai de Livraison Court.", "isCorrect": False},
                        {"text": "Déclaration Légale de Composition.", "isCorrect": False}
                    ],
                    "correction": "La **DLC** est la date impérative pour la consommation. Après cette date, le produit présente un danger potentiel pour la santé."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est l'équipement de sécurité obligatoire dans un fournil pour éteindre un feu d'origine électrique ou de graisse ?",
                    "answerOptions": [
                        {"text": "Un seau d'eau.", "isCorrect": False},
                        {"text": "Un extincteur à mousse.", "isCorrect": False},
                        {"text": "Un **extincteur à poudre (ABC) ou CO2**.", "isCorrect": True},
                        {"text": "Un tuyau d'arrosage.", "isCorrect": False}
                    ],
                    "correction": "L'eau ne doit jamais être utilisée sur les feux électriques ou de graisse. Un extincteur à poudre ou CO2 est adapté."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est l'objectif principal du stock tampon de produits finis ?",
                    "answerOptions": [
                        {"text": "Stocker le pain vieux.", "isCorrect": False},
                        {"text": "**Assurer la disponibilité des produits** en cas de forte affluence ou d'imprévu.", "isCorrect": True},
                        {"text": "Réduire les coûts de main-d'œuvre.", "isCorrect": False},
                        {"text": "Congeler les restes de farine.", "isCorrect": False}
                    ],
                    "correction": "Le **stock tampon** est une petite réserve de produits clés (baguettes, croissants) qui permet de faire face à la demande sans devoir lancer une nouvelle production immédiate."
                },
                {
                    "questionNumber": 97,
                    "question": "Comment calcule-t-on le Rendement Matière (RM) d'une production ?",
                    "answerOptions": [
                        {"text": "(Poids des ingrédients) / (Poids des produits finis).", "isCorrect": False},
                        {"text": "**(Poids des produits finis) / (Poids des matières premières) x 100**.", "isCorrect": True},
                        {"text": "(Coût des produits finis) / (Poids des produits finis).", "isCorrect": False},
                        {"text": "(Volume de la pâte) / (Poids de la pâte).", "isCorrect": False}
                    ],
                    "correction": "Le **Rendement Matière** permet d'évaluer l'efficacité de la production, car le rendement est toujours supérieur à 100 % (l'eau est incorporée) mais des pertes réduisent ce taux."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le danger que l'on court en cas d'inhalation régulière et prolongée de poussière de farine ?",
                    "answerOptions": [
                        {"text": "La déshydratation.", "isCorrect": False},
                        {"text": "L'empoisonnement au sel.", "isCorrect": False},
                        {"text": "Des **problèmes respiratoires graves (asthme du boulanger)**.", "isCorrect": True},
                        {"text": "Une contamination bactérienne.", "isCorrect": False}
                    ],
                    "correction": "La poussière de farine (et ses allergènes) est la cause de l'**asthme du boulanger**. Le port de **masques de protection** est recommandé."
                },
                {
                    "questionNumber": 99,
                    "question": "La date de fabrication est-elle obligatoire sur l'étiquetage du pain non préemballé ?",
                    "answerOptions": [
                        {"text": "Oui, toujours.", "isCorrect": False},
                        {"text": "**Non**, seule la liste des allergènes (et ingrédients si non de tradition) et le nom du produit sont obligatoires.", "isCorrect": True},
                        {"text": "Uniquement pour les pains de seigle.", "isCorrect": False},
                        {"text": "Oui, mais uniquement si la DLC est inférieure à 7 jours.", "isCorrect": False}
                    ],
                    "correction": "La loi dispense d'afficher la date de fabrication ou la DLC sur le pain vendu non préemballé (**frais du jour**). L'information sur les allergènes et ingrédients doit être disponible."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le rôle d'un plan de nettoyage et de désinfection (PND) ?",
                    "answerOptions": [
                        {"text": "Décrire la méthode de pétrissage.", "isCorrect": False},
                        {"text": "**Détailler QUI, QUOI, QUAND, et COMMENT** les locaux et équipements doivent être nettoyés.", "isCorrect": True},
                        {"text": "Calculer le rendement.", "isCorrect": False},
                        {"text": "Gérer les commandes clients.", "isCorrect": False}
                    ],
                    "correction": "Le **PND** est un document HACCP essentiel. Il liste les tâches, les fréquences, les produits utilisés et les responsables pour chaque zone de travail."
                },
            ]
        },
    }
}