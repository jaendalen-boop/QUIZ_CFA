quiz_data = {
    "title": "Quiz Sciences-Physiques - Niveau CAP (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : CHIMIE ET SÉCURITÉ (HYGIÈNE ET SANTÉ) (Q1 à Q20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : CHIMIE ET SÉCURITÉ (HYGIÈNE ET SANTÉ)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est le constituant central d'un atome ?",
                    "answerOptions": [
                        {"text": "Le noyau", "isCorrect": True},
                        {"text": "Le nuage électronique", "isCorrect": False},
                        {"text": "La couche externe", "isCorrect": False},
                        {"text": "La liaison covalente", "isCorrect": False}
                    ],
                    "correction": "L'atome est constitué d'un noyau central chargé positivement, autour duquel gravitent des électrons chargés négativement."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la charge électrique globale d'un atome ?",
                    "answerOptions": [
                        {"text": "Neutre", "isCorrect": True},
                        {"text": "Positive", "isCorrect": False},
                        {"text": "Négative", "isCorrect": False},
                        {"text": "Variable", "isCorrect": False}
                    ],
                    "correction": "Un atome est électriquement neutre car il possède autant de protons (charges positives) que d'électrons (charges négatives)."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment appelle-t-on un atome qui a perdu un ou plusieurs électrons ?",
                    "answerOptions": [
                        {"text": "Un cation", "isCorrect": True},
                        {"text": "Un anion", "isCorrect": False},
                        {"text": "Une molécule", "isCorrect": False},
                        {"text": "Un isotope", "isCorrect": False}
                    ],
                    "correction": "Un atome qui perd des électrons devient chargé positivement et est appelé un cation (ex: Na+). Celui qui en gagne est un anion."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle particule élémentaire porte une charge électrique négative ?",
                    "answerOptions": [
                        {"text": "L'électron", "isCorrect": True},
                        {"text": "Le proton", "isCorrect": False},
                        {"text": "Le neutron", "isCorrect": False},
                        {"text": "Le noyau", "isCorrect": False}
                    ],
                    "correction": "Les électrons tournent autour du noyau. Ce sont eux qui sont responsables de la circulation du courant électrique."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la formule chimique de la molécule d'eau ?",
                    "answerOptions": [
                        {"text": "H2O", "isCorrect": True},
                        {"text": "CO2", "isCorrect": False},
                        {"text": "O2", "isCorrect": False},
                        {"text": "NaCl", "isCorrect": False}
                    ],
                    "correction": "Une molécule d'eau est composée de deux atomes d'hydrogène (H) et d'un atome d'oxygène (O)."
                },
                {
                    "questionNumber": 6,
                    "question": "Que signifie le pH ?",
                    "answerOptions": [
                        {"text": "Potentiel Hydrogène", "isCorrect": True},
                        {"text": "Pression Hydraulique", "isCorrect": False},
                        {"text": "Poids de l'Hélium", "isCorrect": False},
                        {"text": "Particule Homogène", "isCorrect": False}
                    ],
                    "correction": "Le pH mesure l'acidité ou la basicité d'une solution aqueuse sur une échelle de 0 à 14."
                },
                {
                    "questionNumber": 7,
                    "question": "Une solution dont le pH est égal à 7 est dite :",
                    "answerOptions": [
                        {"text": "Neutre", "isCorrect": True},
                        {"text": "Acide", "isCorrect": False},
                        {"text": "Basique", "isCorrect": False},
                        {"text": "Corrosive", "isCorrect": False}
                    ],
                    "correction": "À pH 7 (comme l'eau pure), la solution n'est ni acide ni basique."
                },
                {
                    "questionNumber": 8,
                    "question": "Une solution est acide si son pH est :",
                    "answerOptions": [
                        {"text": "Inférieur à 7", "isCorrect": True},
                        {"text": "Supérieur à 7", "isCorrect": False},
                        {"text": "Égal à 7", "isCorrect": False},
                        {"text": "Égal à 14", "isCorrect": False}
                    ],
                    "correction": "Plus le pH est proche de 0, plus la solution est acide (ex: jus de citron, acide chlorhydrique)."
                },
                {
                    "questionNumber": 9,
                    "question": "Comment appelle-t-on le passage de l'état liquide à l'état gazeux ?",
                    "answerOptions": [
                        {"text": "La vaporisation", "isCorrect": True},
                        {"text": "La fusion", "isCorrect": False},
                        {"text": "La solidification", "isCorrect": False},
                        {"text": "La liquéfaction", "isCorrect": False}
                    ],
                    "correction": "La vaporisation peut se faire par évaporation lente ou par ébullition."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel pictogramme de sécurité représente un produit qui peut brûler la peau et ronger les métaux ?",
                    "answerOptions": [
                        {"text": "Corrosif (éprouvettes versant sur une main)", "isCorrect": True},
                        {"text": "Inflammable (flamme)", "isCorrect": False},
                        {"text": "Toxique (tête de mort)", "isCorrect": False},
                        {"text": "Comburant (cercle enflammé)", "isCorrect": False}
                    ],
                    "correction": "Les produits corrosifs (acides ou bases fortes) nécessitent le port de gants et de lunettes de protection."
                },
                {
                    "questionNumber": 11,
                    "question": "Lorsqu'on dilue un acide avec de l'eau, quelle est la règle de sécurité à respecter ?",
                    "answerOptions": [
                        {"text": "Verser l'acide dans l'eau", "isCorrect": True},
                        {"text": "Verser l'eau dans l'acide", "isCorrect": False},
                        {"text": "Mélanger les deux très vite", "isCorrect": False},
                        {"text": "Ne jamais mélanger avec de l'eau", "isCorrect": False}
                    ],
                    "correction": "On verse toujours l'acide dans l'eau pour éviter les projections dangereuses dues à la réaction de chaleur."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la principale caractéristique d'un mélange homogène ?",
                    "answerOptions": [
                        {"text": "On ne distingue pas ses constituants à l'œil nu", "isCorrect": True},
                        {"text": "Il est composé de plusieurs couches", "isCorrect": False},
                        {"text": "Il contient forcément de l'eau", "isCorrect": False},
                        {"text": "Il est toujours transparent", "isCorrect": False}
                    ],
                    "correction": "L'eau salée ou l'air sont des mélanges homogènes."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle opération permet de séparer les constituants d'un mélange hétérogène (solide/liquide) ?",
                    "answerOptions": [
                        {"text": "La filtration", "isCorrect": True},
                        {"text": "La vaporisation", "isCorrect": False},
                        {"text": "Le chauffage", "isCorrect": False},
                        {"text": "L'agitation", "isCorrect": False}
                    ],
                    "correction": "Le filtre retient les particules solides et laisse passer le liquide (le filtrat)."
                },
                {
                    "questionNumber": 14,
                    "question": "Qu'est-ce qu'un corps pur ?",
                    "answerOptions": [
                        {"text": "Une substance constituée d'une seule sorte de molécules", "isCorrect": True},
                        {"text": "De l'eau du robinet", "isCorrect": False},
                        {"text": "Un mélange de gaz", "isCorrect": False},
                        {"text": "Un produit qui n'est pas toxique", "isCorrect": False}
                    ],
                    "correction": "L'eau distillée ou le fer pur sont des corps purs."
                },
                {
                    "questionNumber": 15,
                    "question": "Dans une combustion, quel gaz est le 'comburant' le plus courant ?",
                    "answerOptions": [
                        {"text": "Le dioxygène (O2)", "isCorrect": True},
                        {"text": "Le diazote (N2)", "isCorrect": False},
                        {"text": "Le dioxyde de carbone (CO2)", "isCorrect": False},
                        {"text": "L'hélium", "isCorrect": False}
                    ],
                    "correction": "Le comburant est la substance qui permet la combustion du combustible."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel gaz éteint une flamme et trouble l'eau de chaux ?",
                    "answerOptions": [
                        {"text": "Le dioxyde de carbone (CO2)", "isCorrect": True},
                        {"text": "Le dioxygène (O2)", "isCorrect": False},
                        {"text": "Le dihydrogène (H2)", "isCorrect": False},
                        {"text": "Le méthane", "isCorrect": False}
                    ],
                    "correction": "Le test à l'eau de chaux est le test spécifique pour identifier la présence de CO2."
                },
                {
                    "questionNumber": 17,
                    "question": "Comment appelle-t-on le produit d'une combustion incomplète, gaz très dangereux et inodore ?",
                    "answerOptions": [
                        {"text": "Le monoxyde de carbone (CO)", "isCorrect": True},
                        {"text": "La vapeur d'eau", "isCorrect": False},
                        {"text": "Le gaz de ville", "isCorrect": False},
                        {"text": "L'ozone", "isCorrect": False}
                    ],
                    "correction": "Le monoxyde de carbone est mortel car il prend la place de l'oxygène dans le sang."
                },
                {
                    "questionNumber": 18,
                    "question": "Que mesure-t-on avec une éprouvette graduée ?",
                    "answerOptions": [
                        {"text": "Un volume", "isCorrect": True},
                        {"text": "Une masse", "isCorrect": False},
                        {"text": "Une température", "isCorrect": False},
                        {"text": "Un poids", "isCorrect": False}
                    ],
                    "correction": "L'unité légale est le mètre cube (m3) mais au laboratoire on utilise le litre (L) ou millilitre (mL)."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est l'unité de la masse dans le système international ?",
                    "answerOptions": [
                        {"text": "Le kilogramme (kg)", "isCorrect": True},
                        {"text": "Le gramme (g)", "isCorrect": False},
                        {"text": "Le litre (L)", "isCorrect": False},
                        {"text": "Le Newton (N)", "isCorrect": False}
                    ],
                    "correction": "La masse se mesure avec une balance."
                },
                {
                    "questionNumber": 20,
                    "question": "Qu'est-ce qu'une réaction chimique ?",
                    "answerOptions": [
                        {"text": "Une transformation où des espèces disparaissent et d'autres apparaissent", "isCorrect": True},
                        {"text": "Un simple changement d'état (ex: glace qui fond)", "isCorrect": False},
                        {"text": "Un mélange que l'on peut séparer par filtration", "isCorrect": False},
                        {"text": "Le fait de secouer un flacon", "isCorrect": False}
                    ],
                    "correction": "Les réactifs sont consommés pour former des produits."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : ÉLECTRICITÉ ET PUISSANCE (Q21 à Q40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : ÉLECTRICITÉ ET PUISSANCE",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est l'unité de la tension électrique ?",
                    "answerOptions": [
                        {"text": "Le Volt (V)", "isCorrect": True},
                        {"text": "L'Ampère (A)", "isCorrect": False},
                        {"text": "Le Watt (W)", "isCorrect": False},
                        {"text": "L'Ohm (Ω)", "isCorrect": False}
                    ],
                    "correction": "La tension se mesure avec un voltmètre branché en dérivation."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle grandeur se mesure en Ampères (A) ?",
                    "answerOptions": [
                        {"text": "L'intensité du courant", "isCorrect": True},
                        {"text": "La puissance", "isCorrect": False},
                        {"text": "La tension", "isCorrect": False},
                        {"text": "L'énergie", "isCorrect": False}
                    ],
                    "correction": "L'intensité représente le 'débit' d'électrons dans le circuit."
                },
                {
                    "questionNumber": 23,
                    "question": "Avec quel appareil mesure-t-on l'intensité du courant ?",
                    "answerOptions": [
                        {"text": "Un ampèremètre", "isCorrect": True},
                        {"text": "Un voltmètre", "isCorrect": False},
                        {"text": "Un ohmmètre", "isCorrect": False},
                        {"text": "Un baromètre", "isCorrect": False}
                    ],
                    "correction": "L'ampèremètre doit être branché en série dans le circuit."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la tension efficace d'une prise de courant domestique en France ?",
                    "answerOptions": [
                        {"text": "230 V", "isCorrect": True},
                        {"text": "12 V", "isCorrect": False},
                        {"text": "110 V", "isCorrect": False},
                        {"text": "400 V", "isCorrect": False}
                    ],
                    "correction": "C'est la tension standard pour les appareils ménagers."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel composant protège une installation contre les surintensités ?",
                    "answerOptions": [
                        {"text": "Le disjoncteur ou le fusible", "isCorrect": True},
                        {"text": "L'interrupteur", "isCorrect": False},
                        {"text": "La lampe", "isCorrect": False},
                        {"text": "Le fil de cuivre", "isCorrect": False}
                    ],
                    "correction": "Ils coupent le courant si l'intensité devient trop forte pour éviter les incendies."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est l'unité de la puissance électrique ?",
                    "answerOptions": [
                        {"text": "Le Watt (W)", "isCorrect": True},
                        {"text": "Le Joule (J)", "isCorrect": False},
                        {"text": "Le Volt (V)", "isCorrect": False},
                        {"text": "L'Ampère (A)", "isCorrect": False}
                    ],
                    "correction": "La puissance indique la performance d'un appareil (ex: une ampoule de 60W)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle formule relie la Puissance (P), la Tension (U) et l'Intensité (I) ?",
                    "answerOptions": [
                        {"text": "P = U × I", "isCorrect": True},
                        {"text": "U = P × I", "isCorrect": False},
                        {"text": "I = U × P", "isCorrect": False},
                        {"text": "P = U + I", "isCorrect": False}
                    ],
                    "correction": "C'est la formule fondamentale en électricité pour les appareils en courant continu ou purement résistifs."
                },
                {
                    "questionNumber": 28,
                    "question": "L'énergie électrique consommée par un appareil dépend de sa puissance et de :",
                    "answerOptions": [
                        {"text": "Sa durée d'utilisation (temps)", "isCorrect": True},
                        {"text": "Sa couleur", "isCorrect": False},
                        {"text": "Sa marque", "isCorrect": False},
                        {"text": "Son poids", "isCorrect": False}
                    ],
                    "correction": "Énergie (E) = Puissance (P) × Temps (t)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est l'unité d'énergie utilisée par EDF sur les factures ?",
                    "answerOptions": [
                        {"text": "Le kiloWatt-heure (kWh)", "isCorrect": True},
                        {"text": "Le Watt (W)", "isCorrect": False},
                        {"text": "Le Volt (V)", "isCorrect": False},
                        {"text": "L'Ampère (A)", "isCorrect": False}
                    ],
                    "correction": "Le Joule est l'unité légale, mais le kWh est l'unité pratique pour les grandes quantités d'énergie."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel matériau est un bon conducteur d'électricité ?",
                    "answerOptions": [
                        {"text": "Le cuivre", "isCorrect": True},
                        {"text": "Le plastique", "isCorrect": False},
                        {"text": "Le bois sec", "isCorrect": False},
                        {"text": "Le verre", "isCorrect": False}
                    ],
                    "correction": "Les métaux sont généralement de bons conducteurs."
                },
                {
                    "questionNumber": 31,
                    "question": "Qu'est-ce qu'un isolant électrique ?",
                    "answerOptions": [
                        {"text": "Un matériau qui ne laisse pas passer le courant", "isCorrect": True},
                        {"text": "Un matériau qui brille dans le noir", "isCorrect": False},
                        {"text": "Un matériau qui chauffe vite", "isCorrect": False},
                        {"text": "Un type de pile", "isCorrect": False}
                    ],
                    "correction": "Le plastique, le caoutchouc et l'air sec sont des isolants."
                },
                {
                    "questionNumber": 32,
                    "question": "Dans un circuit en série, si une lampe grille :",
                    "answerOptions": [
                        {"text": "Toutes les autres lampes s'éteignent", "isCorrect": True},
                        {"text": "Les autres lampes brillent plus fort", "isCorrect": False},
                        {"text": "Rien ne change pour les autres", "isCorrect": False},
                        {"text": "La pile explose", "isCorrect": False}
                    ],
                    "correction": "Le circuit est ouvert, le courant ne circule plus du tout."
                },
                {
                    "questionNumber": 33,
                    "question": "Dans une installation domestique, les appareils sont branchés :",
                    "answerOptions": [
                        {"text": "En dérivation (parallèle)", "isCorrect": True},
                        {"text": "En série", "isCorrect": False},
                        {"text": "Au hasard", "isCorrect": False},
                        {"text": "Uniquement sur piles", "isCorrect": False}
                    ],
                    "correction": "Cela permet d'utiliser chaque appareil indépendamment et sous la même tension (230V)."
                },
                {
                    "questionNumber": 34,
                    "question": "Que signifie le symbole Ω ?",
                    "answerOptions": [
                        {"text": "L'Ohm, unité de résistance électrique", "isCorrect": True},
                        {"text": "L'Oméga, unité de vitesse", "isCorrect": False},
                        {"text": "L'intensité", "isCorrect": False},
                        {"text": "La mise à la terre", "isCorrect": False}
                    ],
                    "correction": "La résistance s'oppose plus ou moins au passage du courant."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est la loi d'Ohm ?",
                    "answerOptions": [
                        {"text": "U = R × I", "isCorrect": True},
                        {"text": "P = U × I", "isCorrect": False},
                        {"text": "R = U × I", "isCorrect": False},
                        {"text": "U = R + I", "isCorrect": False}
                    ],
                    "correction": "La tension (U) est proportionnelle à l'intensité (I)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le risque principal d'un court-circuit ?",
                    "answerOptions": [
                        {"text": "L'incendie par échauffement des fils", "isCorrect": True},
                        {"text": "L'augmentation de la facture", "isCorrect": False},
                        {"text": "La baisse de la tension", "isCorrect": False},
                        {"text": "Le changement de couleur des ampoules", "isCorrect": False}
                    ],
                    "correction": "Un court-circuit crée une intensité très élevée qui fait fondre les gaines isolantes."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle est la couleur normalisée du fil de 'Terre' ?",
                    "answerOptions": [
                        {"text": "Vert et Jaune", "isCorrect": True},
                        {"text": "Bleu", "isCorrect": False},
                        {"text": "Rouge ou Marron", "isCorrect": False},
                        {"text": "Noir", "isCorrect": False}
                    ],
                    "correction": "Le fil de terre protège les personnes contre les électrocutions."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment appelle-t-on le passage du courant électrique dans le corps humain ?",
                    "answerOptions": [
                        {"text": "L'électrisation", "isCorrect": True},
                        {"text": "L'électrocution", "isCorrect": False},
                        {"text": "La conduction", "isCorrect": False},
                        {"text": "L'induction", "isCorrect": False}
                    ],
                    "correction": "L'électrocution désigne une électrisation qui entraîne la mort."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel dispositif coupe le courant en cas de fuite vers la terre ?",
                    "answerOptions": [
                        {"text": "L'interrupteur différentiel", "isCorrect": True},
                        {"text": "Le fusible classique", "isCorrect": False},
                        {"text": "L'ampoule", "isCorrect": False},
                        {"text": "La multiprise", "isCorrect": False}
                    ],
                    "correction": "Il compare l'intensité entrante et sortante et saute s'il y a une différence."
                },
                {
                    "questionNumber": 40,
                    "question": "Pourquoi ne doit-on pas utiliser d'appareils électriques près de l'eau (douche, baignoire) ?",
                    "answerOptions": [
                        {"text": "L'eau diminue la résistance du corps et favorise l'électrocution", "isCorrect": True},
                        {"text": "L'eau éteint l'électricité", "isCorrect": False},
                        {"text": "L'eau coûte trop cher", "isCorrect": False},
                        {"text": "Cela abîme l'appareil", "isCorrect": False}
                    ],
                    "correction": "Le corps mouillé est beaucoup plus conducteur."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : MÉCANIQUE ET FORCES (Q41 à Q60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : MÉCANIQUE ET FORCES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est l'unité du poids (force de pesanteur) ?",
                    "answerOptions": [
                        {"text": "Le Newton (N)", "isCorrect": True},
                        {"text": "Le Kilogramme (kg)", "isCorrect": False},
                        {"text": "Le Gramme (g)", "isCorrect": False},
                        {"text": "Le Mètre (m)", "isCorrect": False}
                    ],
                    "correction": "Le poids est une force, il ne faut pas le confondre avec la masse."
                },
                {
                    "questionNumber": 42,
                    "question": "Avec quel appareil mesure-t-on une force ?",
                    "answerOptions": [
                        {"text": "Un dynamomètre", "isCorrect": True},
                        {"text": "Une balance", "isCorrect": False},
                        {"text": "Un thermomètre", "isCorrect": False},
                        {"text": "Un mètre ruban", "isCorrect": False}
                    ],
                    "correction": "Le dynamomètre contient généralement un ressort qui s'étire en fonction de la force."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la relation entre le Poids (P), la Masse (m) et l'intensité de la pesanteur (g) ?",
                    "answerOptions": [
                        {"text": "P = m × g", "isCorrect": True},
                        {"text": "m = P × g", "isCorrect": False},
                        {"text": "g = P × m", "isCorrect": False},
                        {"text": "P = m / g", "isCorrect": False}
                    ],
                    "correction": "Sur Terre, g vaut environ 9,8 N/kg (souvent arrondi à 10)."
                },
                {
                    "questionNumber": 44,
                    "question": "Le poids d'un objet est-il le même sur la Terre et sur la Lune ?",
                    "answerOptions": [
                        {"text": "Non, il est plus faible sur la Lune", "isCorrect": True},
                        {"text": "Oui, il est identique partout", "isCorrect": False},
                        {"text": "Non, il est plus fort sur la Lune", "isCorrect": False},
                        {"text": "Cela dépend de l'heure", "isCorrect": False}
                    ],
                    "correction": "La masse ne change pas, mais le poids dépend de la gravité du lieu."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle est la caractéristique d'une force représentée par une flèche horizontale vers la droite ?",
                    "answerOptions": [
                        {"text": "Son sens est vers la droite", "isCorrect": True},
                        {"text": "Sa direction est verticale", "isCorrect": False},
                        {"text": "Son intensité est nulle", "isCorrect": False},
                        {"text": "Elle n'a pas de point d'application", "isCorrect": False}
                    ],
                    "correction": "Un vecteur force possède un point d'application, une direction, un sens et une intensité."
                },
                {
                    "questionNumber": 46,
                    "question": "Qu'est-ce que la pression ?",
                    "answerOptions": [
                        {"text": "Le rapport d'une force par une surface", "isCorrect": True},
                        {"text": "Le poids total d'un objet", "isCorrect": False},
                        {"text": "La vitesse du vent", "isCorrect": False},
                        {"text": "La température d'un gaz", "isCorrect": False}
                    ],
                    "correction": "Pression = Force / Surface."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est l'unité de pression dans le système international ?",
                    "answerOptions": [
                        {"text": "Le Pascal (Pa)", "isCorrect": True},
                        {"text": "Le Bar", "isCorrect": False},
                        {"text": "Le Newton", "isCorrect": False},
                        {"text": "Le Joule", "isCorrect": False}
                    ],
                    "correction": "En pratique, on utilise souvent le Bar (1 bar = 100 000 Pa)."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment varie la pression si on augmente la surface d'appui pour une même force ?",
                    "answerOptions": [
                        {"text": "La pression diminue", "isCorrect": True},
                        {"text": "La pression augmente", "isCorrect": False},
                        {"text": "La pression reste la même", "isCorrect": False},
                        {"text": "La force disparaît", "isCorrect": False}
                    ],
                    "correction": "C'est pour cela qu'on utilise des raquettes pour marcher dans la neige (plus de surface = moins de pression)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est l'unité de mesure d'un moment de force (force de rotation) ?",
                    "answerOptions": [
                        {"text": "Le Newton-mètre (N.m)", "isCorrect": True},
                        {"text": "Le Newton par mètre", "isCorrect": False},
                        {"text": "Le Watt", "isCorrect": False},
                        {"text": "Le Kilogramme", "isCorrect": False}
                    ],
                    "correction": "Le moment dépend de la force et de la longueur du bras de levier."
                },
                {
                    "questionNumber": 50,
                    "question": "Pourquoi utilise-t-on une clé à long manche pour dévisser un écrou bloqué ?",
                    "answerOptions": [
                        {"text": "Pour augmenter le moment de la force (bras de levier)", "isCorrect": True},
                        {"text": "Pour être plus loin de l'écrou", "isCorrect": False},
                        {"text": "Pour ne pas se salir les mains", "isCorrect": False},
                        {"text": "Cela ne change rien à la difficulté", "isCorrect": False}
                    ],
                    "correction": "Plus le bras de levier est long, moins on a besoin de force pour obtenir le même effet de rotation."
                },
                {
                    "questionNumber": 51,
                    "question": "Qu'est-ce qu'un mouvement rectiligne ?",
                    "answerOptions": [
                        {"text": "Un mouvement dont la trajectoire est une droite", "isCorrect": True},
                        {"text": "Un mouvement qui tourne en rond", "isCorrect": False},
                        {"text": "Un mouvement qui s'arrête tout de suite", "isCorrect": False},
                        {"text": "Un mouvement très rapide", "isCorrect": False}
                    ],
                    "correction": "Exemple : un ascenseur ou une voiture sur une route bien droite."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la formule de la vitesse moyenne ?",
                    "answerOptions": [
                        {"text": "v = d / t", "isCorrect": True},
                        {"text": "v = d × t", "isCorrect": False},
                        {"text": "v = t / d", "isCorrect": False},
                        {"text": "v = d + t", "isCorrect": False}
                    ],
                    "correction": "Vitesse = Distance divisée par le Temps."
                },
                {
                    "questionNumber": 53,
                    "question": "Comment appelle-t-on un mouvement dont la vitesse augmente ?",
                    "answerOptions": [
                        {"text": "Accéléré", "isCorrect": True},
                        {"text": "Uniforme", "isCorrect": False},
                        {"text": "Ralenti (décéléré)", "isCorrect": False},
                        {"text": "Statique", "isCorrect": False}
                    ],
                    "correction": "Si la vitesse reste constante, le mouvement est uniforme."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est l'unité légale de la vitesse ?",
                    "answerOptions": [
                        {"text": "Le mètre par seconde (m/s)", "isCorrect": True},
                        {"text": "Le kilomètre par heure (km/h)", "isCorrect": False},
                        {"text": "Le nœud", "isCorrect": False},
                        {"text": "Le tour par minute", "isCorrect": False}
                    ],
                    "correction": "Le km/h est l'unité usuelle, mais le m/s est l'unité internationale."
                },
                {
                    "questionNumber": 55,
                    "question": "Qu'est-ce que l'équilibre d'un solide ?",
                    "answerOptions": [
                        {"text": "L'état d'un objet qui reste au repos malgré les forces", "isCorrect": True},
                        {"text": "Le fait de tomber doucement", "isCorrect": False},
                        {"text": "Un objet qui change de forme", "isCorrect": False},
                        {"text": "Un objet qui brille", "isCorrect": False}
                    ],
                    "correction": "Pour être en équilibre, la somme des forces doit être nulle."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle force attire tous les objets vers le sol ?",
                    "answerOptions": [
                        {"text": "La gravité (ou poids)", "isCorrect": True},
                        {"text": "Le magnétisme", "isCorrect": False},
                        {"text": "L'électricité statique", "isCorrect": False},
                        {"text": "Le vent", "isCorrect": False}
                    ],
                    "correction": "La Terre exerce une attraction sur tout corps massif."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment appelle-t-on le point où s'applique le poids d'un objet ?",
                    "answerOptions": [
                        {"text": "Le centre de gravité (G)", "isCorrect": True},
                        {"text": "Le sommet", "isCorrect": False},
                        {"text": "La base", "isCorrect": False},
                        {"text": "Le coin droit", "isCorrect": False}
                    ],
                    "correction": "C'est le point d'équilibre de l'objet."
                },
                {
                    "questionNumber": 58,
                    "question": "Dans quel cas un objet est-il le plus stable ?",
                    "answerOptions": [
                        {"text": "Lorsque son centre de gravité est le plus bas possible", "isCorrect": True},
                        {"text": "Lorsqu'il est très haut", "isCorrect": False},
                        {"text": "Lorsqu'il est posé sur une pointe", "isCorrect": False},
                        {"text": "Lorsqu'il est en mouvement", "isCorrect": False}
                    ],
                    "correction": "Un centre de gravité bas augmente la stabilité (ex: voitures de sport)."
                },
                {
                    "questionNumber": 59,
                    "question": "Qu'est-ce qu'une force de frottement ?",
                    "answerOptions": [
                        {"text": "Une force qui s'oppose au mouvement", "isCorrect": True},
                        {"text": "Une force qui accélère l'objet", "isCorrect": False},
                        {"text": "Une force qui fait décoller l'objet", "isCorrect": False},
                        {"text": "Une force invisible qui n'existe pas", "isCorrect": False}
                    ],
                    "correction": "Le frottement transforme souvent l'énergie en chaleur."
                },
                {
                    "questionNumber": 60,
                    "question": "Un solide est soumis à deux forces. Il est en équilibre si les deux forces sont :",
                    "answerOptions": [
                        {"text": "Opposées et de même intensité", "isCorrect": True},
                        {"text": "Dans le même sens", "isCorrect": False},
                        {"text": "De couleurs différentes", "isCorrect": False},
                        {"text": "Très faibles", "isCorrect": False}
                    ],
                    "correction": "Elles doivent avoir la même droite d'action, des sens contraires et la même valeur."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : ACOUSTIQUE ET OPTIQUE (Q61 à Q80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ACOUSTIQUE ET OPTIQUE",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est l'unité du niveau sonore ?",
                    "answerOptions": [
                        {"text": "Le Décibel (dB)", "isCorrect": True},
                        {"text": "Le Hertz (Hz)", "isCorrect": False},
                        {"text": "Le Mètre", "isCorrect": False},
                        {"text": "Le Volt", "isCorrect": False}
                    ],
                    "correction": "Le décibel mesure l'intensité du son. Attention, l'échelle n'est pas linéaire."
                },
                {
                    "questionNumber": 62,
                    "question": "À partir de quel niveau sonore un son devient-il dangereux pour l'oreille (exposition longue) ?",
                    "answerOptions": [
                        {"text": "85 dB", "isCorrect": True},
                        {"text": "20 dB", "isCorrect": False},
                        {"text": "50 dB", "isCorrect": False},
                        {"text": "10 dB", "isCorrect": False}
                    ],
                    "correction": "Au-delà de 85 dB, des protections auditives sont recommandées en milieu professionnel."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle grandeur physique définit si un son est grave ou aigu ?",
                    "answerOptions": [
                        {"text": "La fréquence (Hz)", "isCorrect": True},
                        {"text": "L'intensité (dB)", "isCorrect": False},
                        {"text": "La vitesse", "isCorrect": False},
                        {"text": "Le timbre", "isCorrect": False}
                    ],
                    "correction": "Fréquence basse = son grave. Fréquence haute = son aigu."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la plage de fréquences audibles par l'homme ?",
                    "answerOptions": [
                        {"text": "De 20 Hz à 20 000 Hz", "isCorrect": True},
                        {"text": "De 0 Hz à 100 Hz", "isCorrect": False},
                        {"text": "Au-dessus de 100 000 Hz", "isCorrect": False},
                        {"text": "De 1 Hz à 10 Hz", "isCorrect": False}
                    ],
                    "correction": "En dessous de 20 Hz, ce sont des infrasons. Au-dessus de 20 000 Hz, des ultrasons."
                },
                {
                    "questionNumber": 65,
                    "question": "Comment appelle-t-on un son trop aigu pour l'oreille humaine ?",
                    "answerOptions": [
                        {"text": "Un ultrason", "isCorrect": True},
                        {"text": "Un infrason", "isCorrect": False},
                        {"text": "Un écho", "isCorrect": False},
                        {"text": "Un bruit sourd", "isCorrect": False}
                    ],
                    "correction": "Les chiens ou les chauves-souris peuvent entendre certains ultrasons."
                },
                {
                    "questionNumber": 66,
                    "question": "Dans quel milieu le son ne peut-il pas se propager ?",
                    "answerOptions": [
                        {"text": "Le vide", "isCorrect": True},
                        {"text": "L'eau", "isCorrect": False},
                        {"text": "L'air", "isCorrect": False},
                        {"text": "L'acier", "isCorrect": False}
                    ],
                    "correction": "Le son a besoin de matière (atomes) pour vibrer et se déplacer."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la vitesse du son dans l'air (environ) ?",
                    "answerOptions": [
                        {"text": "340 m/s", "isCorrect": True},
                        {"text": "300 000 km/s", "isCorrect": False},
                        {"text": "10 km/h", "isCorrect": False},
                        {"text": "1200 m/s", "isCorrect": False}
                    ],
                    "correction": "C'est beaucoup plus lent que la lumière (expliquant le décalage entre éclair et tonnerre)."
                },
                {
                    "questionNumber": 68,
                    "question": "Qu'est-ce qu'une source de lumière primaire ?",
                    "answerOptions": [
                        {"text": "Un objet qui produit sa propre lumière (ex: Soleil, flamme)", "isCorrect": True},
                        {"text": "Un miroir", "isCorrect": False},
                        {"text": "La Lune", "isCorrect": False},
                        {"text": "Un écran éteint", "isCorrect": False}
                    ],
                    "correction": "La Lune est un objet diffusant (elle renvoie la lumière du Soleil)."
                },
                {
                    "questionNumber": 69,
                    "question": "Comment se propage la lumière dans un milieu homogène (comme l'air) ?",
                    "answerOptions": [
                        {"text": "En ligne droite", "isCorrect": True},
                        {"text": "En zigzag", "isCorrect": False},
                        {"text": "En tournant autour des objets", "isCorrect": False},
                        {"text": "Elle ne se déplace pas", "isCorrect": False}
                    ],
                    "correction": "On représente la lumière par des rayons lumineux rectilignes."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle est la vitesse de la lumière dans le vide ?",
                    "answerOptions": [
                        {"text": "300 000 km/s", "isCorrect": True},
                        {"text": "340 m/s", "isCorrect": False},
                        {"text": "1000 km/h", "isCorrect": False},
                        {"text": "Infini", "isCorrect": False}
                    ],
                    "correction": "C'est la vitesse limite absolue dans l'univers."
                },
                {
                    "questionNumber": 71,
                    "question": "Qu'est-ce que la réflexion de la lumière ?",
                    "answerOptions": [
                        {"text": "Le fait que la lumière rebondisse sur une surface", "isCorrect": True},
                        {"text": "Le fait que la lumière soit absorbée", "isCorrect": False},
                        {"text": "Le changement de couleur de la lumière", "isCorrect": False},
                        {"text": "La disparition de la lumière", "isCorrect": False}
                    ],
                    "correction": "Un miroir est un excellent réflecteur."
                },
                {
                    "questionNumber": 72,
                    "question": "Qu'est-ce qu'un corps opaque ?",
                    "answerOptions": [
                        {"text": "Un objet qui ne laisse pas passer la lumière", "isCorrect": True},
                        {"text": "Un objet transparent", "isCorrect": False},
                        {"text": "Un objet qui brille", "isCorrect": False},
                        {"text": "Un objet mou", "isCorrect": False}
                    ],
                    "correction": "Un mur est opaque, le verre est transparent."
                },
                {
                    "questionNumber": 73,
                    "question": "Comment appelle-t-on le phénomène qui décompose la lumière blanche en arc-en-ciel ?",
                    "answerOptions": [
                        {"text": "La dispersion", "isCorrect": True},
                        {"text": "La réflexion", "isCorrect": False},
                        {"text": "L'ombre portée", "isCorrect": False},
                        {"text": "La combustion", "isCorrect": False}
                    ],
                    "correction": "On utilise souvent un prisme pour décomposer la lumière."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelles sont les trois couleurs primaires en synthèse additive (lumière) ?",
                    "answerOptions": [
                        {"text": "Rouge, Vert, Bleu (RVB)", "isCorrect": True},
                        {"text": "Rouge, Jaune, Bleu", "isCorrect": False},
                        {"text": "Cyan, Magenta, Jaune", "isCorrect": False},
                        {"text": "Noir, Blanc, Gris", "isCorrect": False}
                    ],
                    "correction": "C'est le système utilisé par les écrans de télévision et d'ordinateur."
                },
                {
                    "questionNumber": 75,
                    "question": "Pourquoi voyons-nous un objet 'rouge' ?",
                    "answerOptions": [
                        {"text": "Parce qu'il absorbe toutes les couleurs sauf le rouge qu'il renvoie", "isCorrect": True},
                        {"text": "Parce qu'il fabrique de la lumière rouge", "isCorrect": False},
                        {"text": "Parce qu'il est chaud", "isCorrect": False},
                        {"text": "Parce que nos yeux sont rouges", "isCorrect": False}
                    ],
                    "correction": "Un objet noir absorbe toutes les couleurs. Un objet blanc les renvoie toutes."
                },
                {
                    "questionNumber": 76,
                    "question": "Qu'est-ce qu'une ombre ?",
                    "answerOptions": [
                        {"text": "Une zone privée de lumière car un objet opaque l'intercepte", "isCorrect": True},
                        {"text": "Un trou dans le sol", "isCorrect": False},
                        {"text": "De la fumée noire", "isCorrect": False},
                        {"text": "Une couleur spéciale", "isCorrect": False}
                    ],
                    "correction": "L'ombre prouve que la lumière se déplace en ligne droite."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le rôle d'une lentille convergente ?",
                    "answerOptions": [
                        {"text": "Rapprocher les rayons lumineux vers un point (foyer)", "isCorrect": True},
                        {"text": "Écarter les rayons lumineux", "isCorrect": False},
                        {"text": "Arrêter la lumière", "isCorrect": False},
                        {"text": "Changer la couleur des objets", "isCorrect": False}
                    ],
                    "correction": "Elle est utilisée dans les loupes et les lunettes pour hypermétropes."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel appareil permet de transformer l'énergie lumineuse en énergie électrique ?",
                    "answerOptions": [
                        {"text": "Une cellule photovoltaïque (panneau solaire)", "isCorrect": True},
                        {"text": "Une ampoule LED", "isCorrect": False},
                        {"text": "Une pile", "isCorrect": False},
                        {"text": "Un moteur", "isCorrect": False}
                    ],
                    "correction": "C'est une énergie renouvelable."
                },
                {
                    "questionNumber": 79,
                    "question": "Que mesure-t-on avec un luxmètre ?",
                    "answerOptions": [
                        {"text": "L'éclairement lumineux (Lux)", "isCorrect": True},
                        {"text": "La température", "isCorrect": False},
                        {"text": "La vitesse de la lumière", "isCorrect": False},
                        {"text": "Le prix de la lampe", "isCorrect": False}
                    ],
                    "correction": "Il permet de vérifier si l'éclairage d'un bureau est suffisant."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la couleur de la lumière du soleil ?",
                    "answerOptions": [
                        {"text": "Blanche (polychromatique)", "isCorrect": True},
                        {"text": "Jaune uniquement", "isCorrect": False},
                        {"text": "Bleue", "isCorrect": False},
                        {"text": "Rouge", "isCorrect": False}
                    ],
                    "correction": "Elle contient en réalité toutes les couleurs de l'arc-en-ciel."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : THERMODYNAMIQUE ET ÉNERGIE (Q81 à Q100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : THERMODYNAMIQUE ET ÉNERGIE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est l'unité légale de la température ?",
                    "answerOptions": [
                        {"text": "Le Kelvin (K)", "isCorrect": True},
                        {"text": "Le degré Celsius (°C)", "isCorrect": False},
                        {"text": "Le Joule", "isCorrect": False},
                        {"text": "Le Watt", "isCorrect": False}
                    ],
                    "correction": "Le degré Celsius est l'unité usuelle en France."
                },
                {
                    "questionNumber": 82,
                    "question": "À quelle température l'eau pure gèle-t-elle à pression normale ?",
                    "answerOptions": [
                        {"text": "0 °C", "isCorrect": True},
                        {"text": "100 °C", "isCorrect": False},
                        {"text": "-273 °C", "isCorrect": False},
                        {"text": "10 °C", "isCorrect": False}
                    ],
                    "correction": "C'est la température de solidification."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la température d'ébullition de l'eau ?",
                    "answerOptions": [
                        {"text": "100 °C", "isCorrect": True},
                        {"text": "0 °C", "isCorrect": False},
                        {"text": "50 °C", "isCorrect": False},
                        {"text": "200 °C", "isCorrect": False}
                    ],
                    "correction": "C'est le passage de liquide à vapeur."
                },
                {
                    "questionNumber": 84,
                    "question": "Qu'est-ce que la conduction thermique ?",
                    "answerOptions": [
                        {"text": "Le transfert de chaleur de proche en proche sans déplacement de matière", "isCorrect": True},
                        {"text": "La chaleur transportée par un fluide qui bouge", "isCorrect": False},
                        {"text": "La chaleur envoyée par les rayons du soleil", "isCorrect": False},
                        {"text": "Le fait de souffler sur sa soupe", "isCorrect": False}
                    ],
                    "correction": "La chaleur circule bien par conduction dans les métaux."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment appelle-t-on le transfert de chaleur dans un liquide ou un gaz qui se déplace ?",
                    "answerOptions": [
                        {"text": "La convection", "isCorrect": True},
                        {"text": "La conduction", "isCorrect": False},
                        {"text": "Le rayonnement", "isCorrect": False},
                        {"text": "L'évaporation", "isCorrect": False}
                    ],
                    "correction": "Exemple : l'air chaud qui monte au-dessus d'un radiateur."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel matériau est un bon isolant thermique ?",
                    "answerOptions": [
                        {"text": "La laine de verre / Le polystyrène", "isCorrect": True},
                        {"text": "L'aluminium", "isCorrect": False},
                        {"text": "L'acier", "isCorrect": False},
                        {"text": "Le cuivre", "isCorrect": False}
                    ],
                    "correction": "Ils emprisonnent l'air, qui est un excellent isolant."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est l'unité de l'énergie ?",
                    "answerOptions": [
                        {"text": "Le Joule (J)", "isCorrect": True},
                        {"text": "Le Watt (W)", "isCorrect": False},
                        {"text": "Le Volt (V)", "isCorrect": False},
                        {"text": "Le Degré", "isCorrect": False}
                    ],
                    "correction": "Une calorie est une ancienne unité d'énergie (1 cal ≈ 4,18 J)."
                },
                {
                    "questionNumber": 88,
                    "question": "L'énergie 'stockée' dans un ressort tendu est de l'énergie :",
                    "answerOptions": [
                        {"text": "Potentielle élastique", "isCorrect": True},
                        {"text": "Cinétique", "isCorrect": False},
                        {"text": "Thermique", "isCorrect": False},
                        {"text": "Chimique", "isCorrect": False}
                    ],
                    "correction": "Elle sera libérée quand le ressort se détendra."
                },
                {
                    "questionNumber": 89,
                    "question": "L'énergie liée au mouvement d'un objet est l'énergie :",
                    "answerOptions": [
                        {"text": "Cinétique", "isCorrect": True},
                        {"text": "Électrique", "isCorrect": False},
                        {"text": "Solaire", "isCorrect": False},
                        {"text": "Nucléaire", "isCorrect": False}
                    ],
                    "correction": "Elle dépend de la masse et de la vitesse de l'objet."
                },
                {
                    "questionNumber": 90,
                    "question": "Le principe de conservation de l'énergie dit que :",
                    "answerOptions": [
                        {"text": "L'énergie ne peut être ni créée ni détruite, elle se transforme", "isCorrect": True},
                        {"text": "L'énergie disparaît quand on éteint la lumière", "isCorrect": False},
                        {"text": "On peut fabriquer de l'énergie à partir de rien", "isCorrect": False},
                        {"text": "L'énergie reste toujours sous la même forme", "isCorrect": False}
                    ],
                    "correction": "Rien ne se perd, tout se transforme."
                },
                {
                    "questionNumber": 91,
                    "question": "Qu'est-ce qu'une source d'énergie renouvelable ?",
                    "answerOptions": [
                        {"text": "Une source qui se renouvelle naturellement à l'échelle humaine", "isCorrect": True},
                        {"text": "Le pétrole", "isCorrect": False},
                        {"text": "Le gaz naturel", "isCorrect": False},
                        {"text": "Le charbon", "isCorrect": False}
                    ],
                    "correction": "Exemples : soleil, vent, eau, biomasse."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le principal défaut des énergies fossiles ?",
                    "answerOptions": [
                        {"text": "Elles polluent et s'épuisent", "isCorrect": True},
                        {"text": "Elles sont gratuites", "isCorrect": False},
                        {"text": "Elles sont inépuisables", "isCorrect": False},
                        {"text": "Elles ne chauffent pas assez", "isCorrect": False}
                    ],
                    "correction": "Elles rejettent du CO2 responsable du réchauffement climatique."
                },
                {
                    "questionNumber": 93,
                    "question": "Que se passe-t-il pour un gaz quand on le chauffe ?",
                    "answerOptions": [
                        {"text": "Il se dilate (prend plus de place)", "isCorrect": True},
                        {"text": "Il se contracte", "isCorrect": False},
                        {"text": "Il change de couleur", "isCorrect": False},
                        {"text": "Son poids augmente", "isCorrect": False}
                    ],
                    "correction": "La pression augmente aussi si le volume est fermé."
                },
                {
                    "questionNumber": 94,
                    "question": "Dans quel sens se fait naturellement le transfert de chaleur ?",
                    "answerOptions": [
                        {"text": "Du corps le plus chaud vers le corps le plus froid", "isCorrect": True},
                        {"text": "Du corps le plus froid vers le plus chaud", "isCorrect": False},
                        {"text": "De manière aléatoire", "isCorrect": False},
                        {"text": "Cela dépend de l'altitude", "isCorrect": False}
                    ],
                    "correction": "La chaleur cherche toujours l'équilibre thermique."
                },
                {
                    "questionNumber": 95,
                    "question": "Qu'est-ce qu'une calorie ?",
                    "answerOptions": [
                        {"text": "Une unité d'énergie (souvent alimentaire)", "isCorrect": True},
                        {"text": "Une unité de poids", "isCorrect": False},
                        {"text": "Une mesure de la vitesse", "isCorrect": False},
                        {"text": "Un type de vitamine", "isCorrect": False}
                    ],
                    "correction": "Indique la valeur énergétique des aliments."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle énergie possède une voiture garée en haut d'une pente ?",
                    "answerOptions": [
                        {"text": "Énergie potentielle de pesanteur", "isCorrect": True},
                        {"text": "Énergie cinétique", "isCorrect": False},
                        {"text": "Énergie électrique", "isCorrect": False},
                        {"text": "Énergie sonore", "isCorrect": False}
                    ],
                    "correction": "Elle a le 'potentiel' de descendre et de prendre de la vitesse."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le rôle d'une centrale nucléaire ?",
                    "answerOptions": [
                        {"text": "Transformer l'énergie de fission des atomes en électricité", "isCorrect": True},
                        {"text": "Brûler du gaz pour chauffer de l'eau", "isCorrect": False},
                        {"text": "Fabriquer de nouveaux atomes", "isCorrect": False},
                        {"text": "Nettoyer l'atmosphère", "isCorrect": False}
                    ],
                    "correction": "Elle utilise l'uranium comme combustible."
                },
                {
                    "questionNumber": 98,
                    "question": "Pourquoi les surfaces noires chauffent-elles plus au soleil ?",
                    "answerOptions": [
                        {"text": "Parce qu'elles absorbent la lumière", "isCorrect": True},
                        {"text": "Parce qu'elles la réfléchissent", "isCorrect": False},
                        {"text": "Parce qu'elles sont déjà chaudes", "isCorrect": False},
                        {"text": "Parce qu'elles sont lourdes", "isCorrect": False}
                    ],
                    "correction": "L'énergie lumineuse absorbée se transforme en chaleur."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle est la fonction d'un thermostat ?",
                    "answerOptions": [
                        {"text": "Maintenir une température constante", "isCorrect": True},
                        {"text": "Mesurer la pression", "isCorrect": False},
                        {"text": "Augmenter la vitesse", "isCorrect": False},
                        {"text": "Éclairer une pièce", "isCorrect": False}
                    ],
                    "correction": "Il coupe ou lance le chauffage selon la consigne."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle énergie est produite par une pile ?",
                    "answerOptions": [
                        {"text": "Énergie chimique transformée en énergie électrique", "isCorrect": True},
                        {"text": "Énergie mécanique", "isCorrect": False},
                        {"text": "Énergie solaire", "isCorrect": False},
                        {"text": "Énergie nucléaire", "isCorrect": False}
                    ],
                    "correction": "C'est une réserve d'énergie portable."
                }
            ]
        }
    }
}