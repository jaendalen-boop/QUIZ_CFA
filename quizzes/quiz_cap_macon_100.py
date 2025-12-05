# Fichier : quiz_cap_macon_100.py

quiz_data = {
    "title": "Quiz CAP Maçon : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : LECTURE DE PLAN ET IMPLANTATION (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Lecture de Plan et Implantation (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel plan indique la disposition et les dimensions des pièces d'un bâtiment coupé horizontalement (vue de dessus) ?",
                    "answerOptions": [
                        {"text": "Le plan de façade.", "isCorrect": False},
                        {"text": "Le Plan de Coupe (coupe verticale).", "isCorrect": False},
                        {"text": "Le Plan de Masse.", "isCorrect": False},
                        {"text": "Le **Plan de Niveau (ou Plan d'étage)**.", "isCorrect": True}
                    ],
                    "correction": "Le **Plan de Niveau** est la vue principale utilisée par le maçon."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est l'échelle la plus courante pour un plan d'exécution de maçonnerie ?",
                    "answerOptions": [
                        {"text": "1/1000e.", "isCorrect": False},
                        {"text": "1/500e.", "isCorrect": False},
                        {"text": "**1/50e ou 1/20e**.", "isCorrect": True},
                        {"text": "1/1e (taille réelle).", "isCorrect": False}
                    ],
                    "correction": "L'échelle **1/50e** ($2 \text{ cm}$ pour $1 \text{ m}$) permet une bonne précision des détails pour la mise en œuvre."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment appelle-t-on le point de référence altimétrique (verticale) sur un chantier, souvent matérialisé par un piquet ou un trait, à partir duquel toutes les cotes de niveau sont mesurées ?",
                    "answerOptions": [
                        {"text": "Le point $\text{A}$.", "isCorrect": False},
                        {"text": "Le **Niveau de Référence (NR)** ou le **Repère de Niveau (RN)**.", "isCorrect": True},
                        {"text": "Le point zéro.", "isCorrect": False},
                        {"text": "Le point de fuite.", "isCorrect": False}
                    ],
                    "correction": "Le **RN** est indispensable pour vérifier les hauteurs de dalles, seuils, et arases."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel outil permet de vérifier la **verticalité** d'un mur ou d'un pilier ?",
                    "answerOptions": [
                        {"text": "Le niveau à bulle.", "isCorrect": False},
                        {"text": "Le cordeau à tracer.", "isCorrect": False},
                        {"text": "Le **Fil à Plomb** ou le **Niveau Laser** (fonction 'aplomb').", "isCorrect": True},
                        {"text": "Le décamètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Fil à Plomb** reste l'outil traditionnel pour vérifier l'aplomb (verticalité)."
                },
                {
                    "questionNumber": 5,
                    "question": "Lors de l'implantation d'une fondation rectangulaire, quel contrôle permet de vérifier que l'angle est bien à $90^\circ$ ?",
                    "answerOptions": [
                        {"text": "Le contrôle du niveau.", "isCorrect": False},
                        {"text": "Le Théorème de Pythagore (méthode $3-4-5 \text{ m}$ ou mesure des diagonales).", "isCorrect": True},
                        {"text": "Le contrôle de l'aplomb.", "isCorrect": False},
                        {"text": "Le contrôle de la longueur.", "isCorrect": False}
                    ],
                    "correction": "La méthode du **$3-4-5$** ($3^2 + 4^2 = 5^2$) assure un angle droit parfait."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la fonction d'une **ligne de référence (LR)** ou d'une **chaîne d'implantation** sur le plan ?",
                    "answerOptions": [
                        {"text": "Indiquer le type de béton.", "isCorrect": False},
                        {"text": "Servir de point de départ pour le traçage des axes principaux des murs, poutres et poteaux sur le terrain.", "isCorrect": True},
                        {"text": "Délimiter les zones de stockage.", "isCorrect": False},
                        {"text": "Indiquer la hauteur des fenêtres.", "isCorrect": False}
                    ],
                    "correction": "La **Ligne de Référence** est souvent une limite de propriété ou un axe existant."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est l'unité de mesure standard utilisée pour les dimensions des ouvrages sur les plans de construction ?",
                    "answerOptions": [
                        {"text": "Le centimètre (cm).", "isCorrect": False},
                        {"text": "Le **millimètre (mm)**.", "isCorrect": True},
                        {"text": "Le mètre (m).", "isCorrect": False},
                        {"text": "Le pouce (inch).", "isCorrect": False}
                    ],
                    "correction": "Le **Millimètre** est l'unité de précision dans le $\text{BTP}$ (ex : $1000 \text{ mm} = 1 \text{ m}$)."
                },
                {
                    "questionNumber": 8,
                    "question": "À quoi sert un **Cavalier d'implantation** (ou Chèvre) ?",
                    "answerOptions": [
                        {"text": "À monter les murs.", "isCorrect": False},
                        {"text": "À matérialiser et maintenir les axes d'implantation sur le terrain pendant les travaux de terrassement et de fondation, en dehors de la zone de fouille.", "isCorrect": True},
                        {"text": "À transporter le mortier.", "isCorrect": False},
                        {"text": "À vérifier l'aplomb.", "isCorrect": False}
                    ],
                    "correction": "Les **Cavaliers** sont des repères fixes qui permettent de retendre les cordeaux d'alignement."
                },
                {
                    "questionNumber": 9,
                    "question": "Dans le dessin technique, que représente la ligne de trait fin, continu, qui se termine par une flèche et qui est utilisée pour **dimensionner** (donner une cote) un élément ?",
                    "answerOptions": [
                        {"text": "La ligne d'axe.", "isCorrect": False},
                        {"text": "La ligne de coupe.", "isCorrect": False},
                        {"text": "La **Ligne de Cote**.", "isCorrect": True},
                        {"text": "La ligne invisible.", "isCorrect": False}
                    ],
                    "correction": "La **Ligne de Cote** indique la mesure entre deux lignes d'attache."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le but principal de l'étape de **traçage** avant l'exécution d'un ouvrage (fondation, mur) ?",
                    "answerOptions": [
                        {"text": "Calculer le prix.", "isCorrect": False},
                        {"text": "Matérialiser au sol ou sur le support les contours, les emplacements des murs, poteaux et ouvertures selon les dimensions du plan, pour garantir l'exactitude de la construction.", "isCorrect": True},
                        {"text": "Préparer le mortier.", "isCorrect": False},
                        {"text": "Vérifier la résistance des matériaux.", "isCorrect": False}
                    ],
                    "correction": "Le **Traçage** est l'étape qui transfère le dessin à la réalité du chantier."
                },
                {
                    "questionNumber": 11,
                    "question": "Comment appelle-t-on la **différence de niveau** entre un point donné et le niveau de référence (RN) ?",
                    "answerOptions": [
                        {"text": "La diagonale.", "isCorrect": False},
                        {"text": "L'**Altitude (ou Cote)**.", "isCorrect": True},
                        {"text": "La largeur.", "isCorrect": False},
                        {"text": "Le décalage.", "isCorrect": False}
                    ],
                    "correction": "La **Cote** peut être absolue (par rapport au $\text{NGF}$) ou relative (par rapport au RN du chantier)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel document de travail donne le détail des armatures métalliques à mettre en place dans le béton armé ?",
                    "answerOptions": [
                        {"text": "Le plan d'architecte.", "isCorrect": False},
                        {"text": "Le **Plan de Ferraillage** (ou Plan d'armatures).", "isCorrect": True},
                        {"text": "Le plan électrique.", "isCorrect": False},
                        {"text": "Le plan des réseaux.", "isCorrect": False}
                    ],
                    "correction": "Le **Plan de Ferraillage** est indispensable pour les ouvrages en béton armé (semelles, poteaux, poutres)."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel instrument permet de matérialiser un plan horizontal parfait sur le chantier (pour les niveaux de dalle, arases, etc.) ?",
                    "answerOptions": [
                        {"text": "Le mètre ruban.", "isCorrect": False},
                        {"text": "Le **Niveau Optique ou le Niveau Laser Rotatif**.", "isCorrect": True},
                        {"text": "Le fil à plomb.", "isCorrect": False},
                        {"text": "L'équerre.", "isCorrect": False}
                    ],
                    "correction": "Le **Niveau Laser** est l'outil moderne pour établir des niveaux de référence précis sur de grandes surfaces."
                },
                {
                    "questionNumber": 14,
                    "question": "Lors de la vérification de la **planéité** d'une surface (chape, dalle), quel outil utilise-t-on en maçonnerie ?",
                    "answerOptions": [
                        {"text": "La truelle.", "isCorrect": False},
                        {"text": "La **Règle de Maçon** (ou la Règle en aluminium) et le niveau à bulle.", "isCorrect": True},
                        {"text": "Le mètre pliant.", "isCorrect": False},
                        {"text": "Le cordeau.", "isCorrect": False}
                    ],
                    "correction": "La **Règle** permet de vérifier que la surface est bien plane et sans défaut."
                },
                {
                    "questionNumber": 15,
                    "question": "Sur un plan, que représente un **trait mixte fin** (alternance de tirets longs et courts) ?",
                    "answerOptions": [
                        {"text": "Un mur existant.", "isCorrect": False},
                        {"text": "L'**Axe de Symétrie** ou l'axe d'un ouvrage (ex : axe de mur, axe de poteau).", "isCorrect": True},
                        {"text": "Un conduit de ventilation.", "isCorrect": False},
                        {"text": "Une ligne de coupe.", "isCorrect": False}
                    ],
                    "correction": "Les **Axes** sont des lignes d'implantation cruciales (Lignes de Référence)."
                },
                {
                    "questionNumber": 16,
                    "question": "Comment s'appelle l'outil qui permet de tracer des lignes droites colorées sur le sol pour l'implantation ?",
                    "answerOptions": [
                        {"text": "Le pistolet à colle.", "isCorrect": False},
                        {"text": "Le **Cordeau à Tracer** (ou cordeau traceur, rempli de poudre de craie).", "isCorrect": True},
                        {"text": "La ficelle.", "isCorrect": False},
                        {"text": "Le niveau à bulle.", "isCorrect": False}
                    ],
                    "correction": "Le **Cordeau à Tracer** est rapide et précis pour le marquage des limites."
                },
                {
                    "questionNumber": 17,
                    "question": "Lors du traçage d'un mur, quelle épaisseur doit-on prendre en compte pour marquer l'ouverture d'une porte ?",
                    "answerOptions": [
                        {"text": "La largeur du mur.", "isCorrect": False},
                        {"text": "La **Largeur du Dormant de la Menuiserie** (ou tableau de l'ouverture) plus les jeux de pose.", "isCorrect": True},
                        {"text": "La largeur de la maçonnerie.", "isCorrect": False},
                        {"text": "La largeur de la fondation.", "isCorrect": False}
                    ],
                    "correction": "L'ouverture (le 'tableau') doit correspondre à la taille de la menuiserie à poser."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel type de plan est essentiel pour l'implantation des fondations et des réseaux enterrés ?",
                    "answerOptions": [
                        {"text": "Le plan de charpente.", "isCorrect": False},
                        {"text": "Le **Plan d'Infrastructure (ou Plan de Sous-sol/Fondation)**.", "isCorrect": True},
                        {"text": "Le plan de toiture.", "isCorrect": False},
                        {"text": "Le plan de plomberie.", "isCorrect": False}
                    ],
                    "correction": "Le **Plan d'Infrastructure** montre les semelles, les longrines et les conduits."
                },
                {
                    "questionNumber": 19,
                    "question": "Que signifie la cote **'$\text{H} + 1.00$'** sur un plan de construction ?",
                    "answerOptions": [
                        {"text": "Une hauteur de $1$ mètre au-dessus du sol extérieur.", "isCorrect": False},
                        {"text": "Une **Cote mesurée à $1 \text{ mètre}$ au-dessus du Niveau de Référence (NR)** du bâtiment.", "isCorrect": True},
                        {"text": "Une hauteur totale de $1 \text{ mètre}$.", "isCorrect": False},
                        {"text": "Une profondeur de $1 \text{ mètre}$.", "isCorrect": False}
                    ],
                    "correction": "Les cotes sont souvent exprimées par rapport à un **RN** (par exemple, le niveau du sol fini du rez-de-chaussée)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le terme technique désignant la **remise à niveau** d'une surface pour la rendre horizontale ?",
                    "answerOptions": [
                        {"text": "Le dressage.", "isCorrect": False},
                        {"text": "Le calepinage.", "isCorrect": False},
                        {"text": "L'**Arasage** (pour les murs) ou la mise à niveau.", "isCorrect": True},
                        {"text": "Le jointoiement.", "isCorrect": False}
                    ],
                    "correction": "L'**Arase** est essentielle pour que le mur soit parfaitement de niveau avant l'élévation des éléments suivants."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : MATÉRIAUX, MORTIERS ET BÉTONS (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Matériaux, Mortiers et Bétons (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quels sont les trois composants principaux d'un **mortier** de maçonnerie ?",
                    "answerOptions": [
                        {"text": "Ciment, Eau, Acier.", "isCorrect": False},
                        {"text": "**Liant (Ciment ou Chaux), Sable, Eau**.", "isCorrect": True},
                        {"text": "Gravier, Sable, Ciment.", "isCorrect": False},
                        {"text": "Acier, Eau, Gravier.", "isCorrect": False}
                    ],
                    "correction": "Le **Mortier** est utilisé pour lier les éléments (briques, parpaings) et pour les enduits/chapes."
                },
                {
                    "questionNumber": 22,
                    "question": "Quels sont les quatre composants principaux d'un **béton** courant ?",
                    "answerOptions": [
                        {"text": "Sable, Eau, Chaux, Acier.", "isCorrect": False},
                        {"text": "**Ciment (Liant), Sable (Granulat fin), Gravier (Granulat gros), Eau**.", "isCorrect": True},
                        {"text": "Brique, Ciment, Eau, Plastique.", "isCorrect": False},
                        {"text": "Bois, Gravier, Sable, Ciment.", "isCorrect": False}
                    ],
                    "correction": "Le **Béton** est plus résistant que le mortier car il contient du gravier."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le rôle du **ciment** dans la composition des mortiers et bétons ?",
                    "answerOptions": [
                        {"text": "Donner la couleur.", "isCorrect": False},
                        {"text": "Le **Liant** : il durcit par hydratation (réaction avec l'eau) et assure la cohésion et la résistance mécanique du mélange.", "isCorrect": True},
                        {"text": "Rendre le mélange liquide.", "isCorrect": False},
                        {"text": "Servir de gravier.", "isCorrect": False}
                    ],
                    "correction": "Le **Ciment** est l'ingrédient actif qui permet la prise et le durcissement (l'hydratation)."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on le type de parpaing le plus courant, souvent utilisé pour les murs porteurs, caractérisé par des alvéoles verticales ?",
                    "answerOptions": [
                        {"text": "La brique monomur.", "isCorrect": False},
                        {"text": "Le **Bloc de Béton Creux** (ou Parpaing de type $\text{B}$).", "isCorrect": True},
                        {"text": "Le béton cellulaire.", "isCorrect": False},
                        {"text": "La brique de terre cuite.", "isCorrect": False}
                    ],
                    "correction": "Le **Parpaing Creux** est standard pour le gros œuvre non apparent."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est l'outil utilisé par le maçon pour mélanger de grandes quantités de mortier ou de béton sur le chantier ?",
                    "answerOptions": [
                        {"text": "La brouette.", "isCorrect": False},
                        {"text": "La **Bétonnière** (ou Malaxeur).", "isCorrect": True},
                        {"text": "La truelle.", "isCorrect": False},
                        {"text": "Le seau.", "isCorrect": False}
                    ],
                    "correction": "La **Bétonnière** assure l'homogénéité du mélange."
                },
                {
                    "questionNumber": 26,
                    "question": "Qu'est-ce que le **Temps de Prise** d'un mortier ou d'un béton ?",
                    "answerOptions": [
                        {"text": "Le temps de séchage.", "isCorrect": False},
                        {"text": "Le **Délai** pendant lequel le mélange perd sa plasticité (il durcit) et ne peut plus être travaillé ou mis en œuvre (en moyenne $2$ à $4$ heures après le gâchage).", "isCorrect": True},
                        {"text": "Le temps de transport.", "isCorrect": False},
                        {"text": "Le temps de la commande.", "isCorrect": False}
                    ],
                    "correction": "Il est crucial de respecter le **Temps de Prise** pour que le mélange ne soit pas altéré (ne jamais rajouter d'eau après le début de la prise)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la principale caractéristique de la **chaux** par rapport au ciment dans la composition des mortiers (notamment pour la rénovation de vieux bâtis) ?",
                    "answerOptions": [
                        {"text": "Elle est plus chère.", "isCorrect": False},
                        {"text": "**Elle est plus souple, plus respirante** (perméable à la vapeur d'eau), et moins résistante que le ciment, permettant au mur de 'respirer'.", "isCorrect": True},
                        {"text": "Elle est plus lourde.", "isCorrect": False},
                        {"text": "Elle sèche plus vite.", "isCorrect": False}
                    ],
                    "correction": "La **Chaux** est préférée pour les enduits et les maçonneries anciennes (patrimoine)."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment appelle-t-on la **partie supérieure d'un mur** sur laquelle s'appuient une poutre, un plancher ou une charpente ?",
                    "answerOptions": [
                        {"text": "La semelle.", "isCorrect": False},
                        {"text": "L'**Arase** (surface plane et horizontale) ou le Chaînage Haut.", "isCorrect": True},
                        {"text": "La fondation.", "isCorrect": False},
                        {"text": "Le linteau.", "isCorrect": False}
                    ],
                    "correction": "L'**Arase** est un niveau de référence horizontal."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le rôle d'un **Adjuvant** dans la fabrication du béton (ex : fluidifiant, hydrofuge, accélérateur) ?",
                    "answerOptions": [
                        {"text": "Augmenter le prix.", "isCorrect": False},
                        {"text": "Modifier les propriétés du béton frais ou durci (plasticité, résistance au gel, étanchéité) en fonction des besoins spécifiques de l'ouvrage.", "isCorrect": True},
                        {"text": "Donner la couleur.", "isCorrect": False},
                        {"text": "Remplacer le ciment.", "isCorrect": False}
                    ],
                    "correction": "Les **Adjuvants** permettent de personnaliser les performances du béton."
                },
                {
                    "questionNumber": 30,
                    "question": "Comment appelle-t-on le phénomène d'**évaporation trop rapide** de l'eau du béton frais, qui peut entraîner des fissures et affaiblir sa résistance ?",
                    "answerOptions": [
                        {"text": "La fissuration.", "isCorrect": False},
                        {"text": "Le **Dessèchement** (ou 'cracking'). Pour l'éviter, on réalise un 'cure' (arrosage régulier).", "isCorrect": True},
                        {"text": "La ségrégation.", "isCorrect": False},
                        {"text": "Le retrait.", "isCorrect": False}
                    ],
                    "correction": "Le **Cure** est essentiel, surtout par temps chaud, pour assurer une bonne hydratation du ciment."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est l'utilité du **Dosage** d'un mortier (ex : $350 \text{ kg}$ de ciment par $\text{m}^3$ de sable) ?",
                    "answerOptions": [
                        {"text": "Déterminer la couleur.", "isCorrect": False},
                        {"text": "Déterminer la **Résistance Mécanique** finale de l'ouvrage (plus le dosage en liant est élevé, plus la résistance est forte).", "isCorrect": True},
                        {"text": "Déterminer la quantité d'eau.", "isCorrect": False},
                        {"text": "Déterminer la quantité de sable.", "isCorrect": False}
                    ],
                    "correction": "Le **Dosage** est la recette qui garantit les performances demandées (ex : béton de propreté, béton armé, chape)."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel terme désigne la **face visible** d'un élément de maçonnerie (pierre, brique, parpaing) ?",
                    "answerOptions": [
                        {"text": "Le parement intérieur.", "isCorrect": False},
                        {"text": "Le **Parement** (ou face extérieure) qui sera le plus souvent celui visible après achèvement.", "isCorrect": True},
                        {"text": "L'arase.", "isCorrect": False},
                        {"text": "Le talon.", "isCorrect": False}
                    ],
                    "correction": "Le **Parement** demande un soin particulier au niveau de l'aspect (alignement, propreté des joints)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la principale différence entre la **brique de terre cuite** et le **bloc de béton** ?",
                    "answerOptions": [
                        {"text": "La brique est plus lourde.", "isCorrect": False},
                        {"text": "La **Brique** offre généralement une meilleure **Isolation Thermique** et une inertie plus forte que le bloc de béton standard.", "isCorrect": True},
                        {"text": "La brique est moins chère.", "isCorrect": False},
                        {"text": "Le bloc de béton est plus esthétique.", "isCorrect": False}
                    ],
                    "correction": "La **Brique Monomur** est très utilisée pour ses qualités d'isolation intrinsèque."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est l'utilité d'un **Mortier-colle** ?",
                    "answerOptions": [
                        {"text": "Réaliser des enduits.", "isCorrect": False},
                        {"text": "Assembler des éléments (ex : béton cellulaire, briques rectifiées, carrelages) avec un joint très fin (souvent de l'ordre de $1 \text{ à } 3 \text{ mm}$).", "isCorrect": True},
                        {"text": "Fabriquer des bétons.", "isCorrect": False},
                        {"text": "Réaliser des finitions rugueuses.", "isCorrect": False}
                    ],
                    "correction": "Le **Mortier-colle** permet un assemblage précis et rapide des matériaux rectifiés."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment appelle-t-on le matériau dont la fonction est d'**empêcher les remontées d'humidité** du sol dans les murs (souvent une membrane ou un mortier hydrofuge en pied de mur) ?",
                    "answerOptions": [
                        {"text": "La fondation.", "isCorrect": False},
                        {"text": "L'**Arase Étanchée** (ou Couche d'Arase Étanchée : $\text{CAE}$).", "isCorrect": True},
                        {"text": "Le chaînage.", "isCorrect": False},
                        {"text": "L'enduit de façade.", "isCorrect": False}
                    ],
                    "correction": "L'**Arase Étanchée** est obligatoire au niveau du soubassement (pied de mur)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le risque d'utiliser **trop d'eau** dans le gâchage du béton ?",
                    "answerOptions": [
                        {"text": "Augmenter la résistance.", "isCorrect": False},
                        {"text": "**Réduire sa résistance mécanique** finale (rapport $\text{E}/\text{C}$ trop élevé) et provoquer la ségrégation (séparation des granulats).", "isCorrect": True},
                        {"text": "Accélérer la prise.", "isCorrect": False},
                        {"text": "Le rendre plus lourd.", "isCorrect": False}
                    ],
                    "correction": "L'eau doit être dosée précisément pour garantir la performance du béton."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel type de sable est généralement utilisé pour les mortiers de pose (liant les éléments de maçonnerie) ?",
                    "answerOptions": [
                        {"text": "Le sable très fin (ex : sable de plage).", "isCorrect": False},
                        {"text": "Le **Sable $0/4 \text{ mm}$** (granulométrie courante).", "isCorrect": True},
                        {"text": "Le sable à béton ($0/20 \text{ mm}$).", "isCorrect": False},
                        {"text": "Le gravier seul.", "isCorrect": False}
                    ],
                    "correction": "La granulométrie **$0/4 \text{ mm}$** est la norme pour les mortiers de joint et de pose."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment s'appelle l'outil qui permet d'appliquer et de lisser les mortiers et enduits sur les murs ?",
                    "answerOptions": [
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "La **Truelle et la Taloche** (ou platoir).", "isCorrect": True},
                        {"text": "Le niveau.", "isCorrect": False},
                        {"text": "Le mètre.", "isCorrect": False}
                    ],
                    "correction": "La **Truelle** sert à prélever et étaler ; la **Taloche** sert à aplanir et finir."
                },
                {
                    "questionNumber": 39,
                    "question": "Qu'est-ce qu'un **Enduit monocouche** ?",
                    "answerOptions": [
                        {"text": "Un enduit appliqué en une seule fois (pour les finitions).", "isCorrect": False},
                        {"text": "Un **Enduit (à base de chaux ou de ciment)** qui assure à la fois l'étanchéité, le dégrossi et la finition, appliqué en deux passes 'frais sur frais'.", "isCorrect": True},
                        {"text": "Un enduit pour l'intérieur.", "isCorrect": False},
                        {"text": "Un enduit très fin.", "isCorrect": False}
                    ],
                    "correction": "L'**Enduit Monocouche** est courant sur les murs neufs pour sa rapidité d'exécution."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel type de parpaing est spécifiquement conçu pour les **angles de mur** ?",
                    "answerOptions": [
                        {"text": "Le parpaing creux.", "isCorrect": False},
                        {"text": "Le **Bloc Poteau** (ou Bloc d'Angle) qui permet de ferrailler et couler les chaînages verticaux.", "isCorrect": True},
                        {"text": "Le parpaing linteau.", "isCorrect": False},
                        {"text": "Le parpaing isolant.", "isCorrect": False}
                    ],
                    "correction": "Le **Bloc Poteau** (en $\text{U}$ ou à parois minces) est utilisé pour réaliser le **Chaînage Vertical** aux intersections."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : MAÇONNERIE DE PETITS ÉLÉMENTS ET FINITIONS (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Maçonnerie de Petits Éléments et Finitions (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la règle essentielle pour l'assemblage des éléments de maçonnerie (parpaings, briques) entre deux assises successives ?",
                    "answerOptions": [
                        {"text": "Les aligner parfaitement.", "isCorrect": False},
                        {"text": "**Le Calepinage** : croiser les joints verticaux d'une rangée à l'autre (sauf pour les joints minces) pour assurer la stabilité et la bonne répartition des charges.", "isCorrect": True},
                        {"text": "Utiliser un mortier sec.", "isCorrect": False},
                        {"text": "Les couper tous à la même taille.", "isCorrect": False}
                    ],
                    "correction": "Le **Croisement des Joints** (décalage d'un demi-bloc) est indispensable pour la solidité et l'équilibre du mur."
                },
                {
                    "questionNumber": 42,
                    "question": "Comment s'appelle l'élément préfabriqué ou coulé en place qui sert à soutenir la maçonnerie au-dessus d'une ouverture (fenêtre, porte) ?",
                    "answerOptions": [
                        {"text": "Le poteau.", "isCorrect": False},
                        {"text": "Le **Linteau**.", "isCorrect": True},
                        {"text": "Le chaînage.", "isCorrect": False},
                        {"text": "La semelle.", "isCorrect": False}
                    ],
                    "correction": "Le **Linteau** est une poutre horizontale qui reprend la charge du mur supérieur."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la fonction d'un **Chaînage** horizontal ou vertical dans une construction en maçonnerie ?",
                    "answerOptions": [
                        {"text": "Rendre la maison jolie.", "isCorrect": False},
                        {"text": "Assurer la **Rigidité de la Structure** et sa résistance aux efforts horizontaux (vent, séismes) en reliant l'ensemble des murs entre eux (souvent réalisé en béton armé).", "isCorrect": True},
                        {"text": "Empêcher l'eau de rentrer.", "isCorrect": False},
                        {"text": "Isoler thermiquement.", "isCorrect": False}
                    ],
                    "correction": "Le **Chaînage** (armatures + béton) forme le 'squelette' du bâtiment."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel outil permet de vérifier l'alignement **horizontal** d'une rangée de parpaings ?",
                    "answerOptions": [
                        {"text": "Le fil à plomb.", "isCorrect": False},
                        {"text": "Le **Cordeau tendu** et le **Niveau à Bulle**.", "isCorrect": True},
                        {"text": "Le décamètre.", "isCorrect": False},
                        {"text": "La règle de maçon.", "isCorrect": False}
                    ],
                    "correction": "Le **Cordeau** sert de guide et le **Niveau** vérifie la planéité."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment appelle-t-on la couche de finition posée au sol, réalisée en mortier, qui doit être parfaitement plane pour recevoir un revêtement (carrelage, parquet) ?",
                    "answerOptions": [
                        {"text": "La dalle.", "isCorrect": False},
                        {"text": "La **Chape**.", "isCorrect": True},
                        {"text": "La semelle.", "isCorrect": False},
                        {"text": "L'arase.", "isCorrect": False}
                    ],
                    "correction": "La **Chape** est la couche de forme et de finition horizontale."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est l'objectif du **Gâchage** d'un mortier ou d'un enduit ?",
                    "answerOptions": [
                        {"text": "Laisser sécher.", "isCorrect": False},
                        {"text": "Mélanger tous les composants (sable, liant, eau, adjuvants) jusqu'à obtention d'un mélange **Homogène** et d'une consistance adaptée à la mise en œuvre.", "isCorrect": True},
                        {"text": "Ajouter du gravier.", "isCorrect": False},
                        {"text": "Nettoyer les outils.", "isCorrect": False}
                    ],
                    "correction": "Le **Gâchage** (mélange) est l'étape de préparation avant l'utilisation."
                },
                {
                    "questionNumber": 47,
                    "question": "Lors de la pose de parpaings, quel élément est crucial à vérifier après la pose de chaque bloc (en plus de l'alignement et du niveau) ?",
                    "answerOptions": [
                        {"text": "La couleur.", "isCorrect": False},
                        {"text": "L'**Épaisseur et la Régularité des Joints** (horizontal et vertical) qui doivent respecter le plan et les normes ($1$ à $1.5 \text{ cm}$ en maçonnerie classique).", "isCorrect": True},
                        {"text": "Le poids.", "isCorrect": False},
                        {"text": "Le prix.", "isCorrect": False}
                    ],
                    "correction": "La **Régularité du Joint** garantit la solidité et l'esthétique du mur."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment appelle-t-on l'opération qui consiste à **projeter le mortier** sur un mur pour créer la première couche d'enduit (couche d'accrochage) ?",
                    "answerOptions": [
                        {"text": "Le lissage.", "isCorrect": False},
                        {"text": "Le **Gobetis**.", "isCorrect": True},
                        {"text": "Le talochage.", "isCorrect": False},
                        {"text": "Le calepinage.", "isCorrect": False}
                    ],
                    "correction": "Le **Gobetis** est une couche très liquide, souvent riche en ciment, pour assurer l'adhérence des couches suivantes."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le rôle du **Joint creux** (ou joint en retrait) dans la finition d'une maçonnerie apparente (briques, pierres) ?",
                    "answerOptions": [
                        {"text": "Augmenter l'isolation.", "isCorrect": False},
                        {"text": "Mettre en valeur l'élément de maçonnerie (pierre ou brique) en créant une ombre et en facilitant l'évacuation de l'eau.", "isCorrect": True},
                        {"text": "Rendre le mur plus lisse.", "isCorrect": False},
                        {"text": "Le rendre plus résistant.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint** est un élément d'esthétique et de durabilité de la façade."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle est la **densité** (masse volumique) moyenne du béton courant, par $\text{m}^3$ ?",
                    "answerOptions": [
                        {"text": "Environ $1000 \text{ kg}/\text{m}^3$.", "isCorrect": False},
                        {"text": "Environ **$2300 \text{ kg}/\text{m}^3$ à $2500 \text{ kg}/\text{m}^3$** (soit $2.3 \text{ à } 2.5 \text{ tonnes}/\text{m}^3$).", "isCorrect": True},
                        {"text": "Environ $500 \text{ kg}/\text{m}^3$.", "isCorrect": False},
                        {"text": "Environ $4000 \text{ kg}/\text{m}^3$.", "isCorrect": False}
                    ],
                    "correction": "Le **Poids** du béton est un élément clé à prendre en compte lors des calculs de charge (poids propre)."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel outil est spécifiquement utilisé pour enlever l'excédent de mortier et façonner le joint entre les briques ou les pierres ?",
                    "answerOptions": [
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "Le **Fer à Joint**.", "isCorrect": True},
                        {"text": "La taloche.", "isCorrect": False},
                        {"text": "La tenaille.", "isCorrect": False}
                    ],
                    "correction": "Le **Fer à Joint** permet de donner la forme désirée au joint (creux, plat, biseauté)."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment s'appelle la technique de pose qui utilise un mortier ou une colle à **joint mince** pour minimiser les ponts thermiques (ex : briques rectifiées) ?",
                    "answerOptions": [
                        {"text": "Maçonnerie traditionnelle.", "isCorrect": False},
                        {"text": "La **Maçonnerie à Joint Mince** (ou à Joint Collé).", "isCorrect": True},
                        {"text": "Maçonnerie à sec.", "isCorrect": False},
                        {"text": "Maçonnerie à pierre vue.", "isCorrect": False}
                    ],
                    "correction": "La **Maçonnerie à Joint Mince** améliore la performance thermique du mur."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel élément maçonné ou préfabriqué est placé au bas de l'ouverture d'une fenêtre pour l'écoulement de l'eau ?",
                    "answerOptions": [
                        {"text": "Le linteau.", "isCorrect": False},
                        {"text": "L'**Appui de Fenêtre** (ou Seuil de Fenêtre).", "isCorrect": True},
                        {"text": "Le coffre de volet.", "isCorrect": False},
                        {"text": "Le tableau.", "isCorrect": False}
                    ],
                    "correction": "L'**Appui** doit être posé avec une légère pente vers l'extérieur pour l'évacuation."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la règle de base concernant l'ouverture d'un **gros trou** dans un mur porteur existant ?",
                    "answerOptions": [
                        {"text": "On peut percer directement.", "isCorrect": False},
                        {"text": "**Nécessité de Soutènement Temporaire (Étaiement)** et pose d'un linteau de remplacement avant de démolir la partie inférieure du mur.", "isCorrect": True},
                        {"text": "On utilise de la mousse expansive.", "isCorrect": False},
                        {"text": "On utilise la truelle.", "isCorrect": False}
                    ],
                    "correction": "L'**Étaiement** est obligatoire pour garantir la sécurité et la stabilité du bâtiment."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le risque de travailler un mortier de ciment à une température **proche de $0^\circ \text{C}$** ?",
                    "answerOptions": [
                        {"text": "Il sèche trop vite.", "isCorrect": False},
                        {"text": "Le **Gel** : l'eau du mortier gèle avant la prise du ciment, détruisant la structure et la résistance de l'ouvrage.", "isCorrect": True},
                        {"text": "Il devient trop mou.", "isCorrect": False},
                        {"text": "Il devient trop lourd.", "isCorrect": False}
                    ],
                    "correction": "Il faut protéger les ouvrages contre le **Gel** (bâches, protection) ou utiliser des adjuvants antigel."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment appelle-t-on le revêtement intérieur ou extérieur (souvent plâtré ou enduit) qui permet de corriger les défauts d'un mur brut ?",
                    "answerOptions": [
                        {"text": "La finition.", "isCorrect": False},
                        {"text": "Le **Dressage** (application d'une couche pour obtenir la planéité souhaitée).", "isCorrect": True},
                        {"text": "Le calepinage.", "isCorrect": False},
                        {"text": "L'arase.", "isCorrect": False}
                    ],
                    "correction": "Le **Dressage** précède la couche de finition (crépi, peinture)."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'est-ce qu'une **Semelle de Fondation** ?",
                    "answerOptions": [
                        {"text": "Le mur.", "isCorrect": False},
                        {"text": "L'élément de maçonnerie de base qui **Répartit les Charges du Bâtiment** sur le sol (assise du mur).", "isCorrect": True},
                        {"text": "Le plancher.", "isCorrect": False},
                        {"text": "Le toit.", "isCorrect": False}
                    ],
                    "correction": "La **Semelle** est la première et la plus importante partie de l'ouvrage (ancrage)."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le risque d'une **maçonnerie à sec** (assemblage sans mortier, comme les murs en pierres sèches) ?",
                    "answerOptions": [
                        {"text": "Isolation thermique.", "isCorrect": False},
                        {"text": "Un manque de résistance aux mouvements de terrain ou aux charges verticales et l'absence d'étanchéité.", "isCorrect": True},
                        {"text": "Couleur irrégulière.", "isCorrect": False},
                        {"text": "Faible coût.", "isCorrect": False}
                    ],
                    "correction": "La **Maçonnerie à Sec** est surtout utilisée pour les murs de soutènement non porteurs ou l'aménagement paysager."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est l'outil spécifique utilisé pour couper les briques ou les parpaings avec précision (hors tronçonneuse de chantier) ?",
                    "answerOptions": [
                        {"text": "Le marteau-piqueur.", "isCorrect": False},
                        {"text": "La **Coupeuse de Matériaux à Eau** (ou Tronçonneuse à disque diamanté).", "isCorrect": True},
                        {"text": "La scie à bois.", "isCorrect": False},
                        {"text": "Le burin seul.", "isCorrect": False}
                    ],
                    "correction": "La **Coupeuse à Eau** permet une coupe nette et réduit la poussière."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle est la fonction d'un **Chaînage en $\text{U}$** ?",
                    "answerOptions": [
                        {"text": "Créer un angle.", "isCorrect": False},
                        {"text": "Recevoir les armatures horizontales et le béton d'une arase ou d'un linteau coulé en place.", "isCorrect": True},
                        {"text": "Créer un trou.", "isCorrect": False},
                        {"text": "Remplir les joints.", "isCorrect": False}
                    ],
                    "correction": "Le **Bloc $\text{U}$** sert de coffrage permanent pour les ouvrages horizontaux (linteaux, chaînages)."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : COFFRAGE, ARMATURES ET BÉTON ARMÉ (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Coffrage, Armatures et Béton Armé (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le rôle du **Coffrage** dans la réalisation d'un ouvrage en béton (poteau, poutre, dalle) ?",
                    "answerOptions": [
                        {"text": "Accélérer la prise.", "isCorrect": False},
                        {"text": "Former la **Structure Temporaire** qui maintient le béton frais en place et lui donne sa forme et ses dimensions finales.", "isCorrect": True},
                        {"text": "Rendre le béton plus résistant.", "isCorrect": False},
                        {"text": "Empêcher l'eau de sortir.", "isCorrect": False}
                    ],
                    "correction": "Le **Coffrage** est le moule du béton."
                },
                {
                    "questionNumber": 62,
                    "question": "Qu'est-ce que le **Béton Armé** ?",
                    "answerOptions": [
                        {"text": "Du béton mélangé à de la pierre.", "isCorrect": False},
                        {"text": "Du **Béton dans lequel on a inséré des Armatures en Acier** (ferraillage) pour améliorer sa résistance à la traction et à la flexion (le béton résiste à la compression, l'acier à la traction).", "isCorrect": True},
                        {"text": "Du béton très résistant au feu.", "isCorrect": False},
                        {"text": "Du béton mélangé à du bois.", "isCorrect": False}
                    ],
                    "correction": "Le **Béton Armé** est le matériau structurel le plus courant dans la construction moderne."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la fonction de l'**Huile de Décoffrage** ?",
                    "answerOptions": [
                        {"text": "Imperméabiliser le béton.", "isCorrect": False},
                        {"text": "Empêcher le béton d'adhérer au coffrage afin de faciliter le **Décoffrage** sans abîmer le parement du béton.", "isCorrect": True},
                        {"text": "Accélérer la prise.", "isCorrect": False},
                        {"text": "Colorer le béton.", "isCorrect": False}
                    ],
                    "correction": "L'**Huile de Décoffrage** est appliquée sur la face interne du moule."
                },
                {
                    "questionNumber": 64,
                    "question": "Comment appelle-t-on les **barres d'acier** qui forment le cadre d'un poteau ou d'une poutre en béton armé ?",
                    "answerOptions": [
                        {"text": "Les chaînages.", "isCorrect": False},
                        {"text": "Les **Armatures (longitudinales ou transversales)**, ex : Cadres, Étriers, Épingles.", "isCorrect": True},
                        {"text": "Les fondations.", "isCorrect": False},
                        {"text": "Les treillis.", "isCorrect": False}
                    ],
                    "correction": "Les **Armatures** doivent être ligaturées (attachées) ensemble selon les plans de ferraillage."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le rôle du **Vibrage** (ou vibration) du béton après son coulage dans le coffrage ?",
                    "answerOptions": [
                        {"text": "Accélérer le séchage.", "isCorrect": False},
                        {"text": "**Éliminer les bulles d'air** (poches d'air) pour assurer une bonne compacité, une homogénéité et une résistance optimale du béton.", "isCorrect": True},
                        {"text": "Rendre le béton plus souple.", "isCorrect": False},
                        {"text": "Le nettoyer.", "isCorrect": False}
                    ],
                    "correction": "Le **Vibrage** est effectué avec une aiguille vibrante et est essentiel pour la qualité de l'ouvrage."
                },
                {
                    "questionNumber": 66,
                    "question": "Qu'est-ce que l'opération de **Régalage** du béton de la dalle ?",
                    "answerOptions": [
                        {"text": "Le vibrage.", "isCorrect": False},
                        {"text": "L'action d'étaler et de mettre à niveau le béton frais entre les guides (ou règles) pour obtenir une surface régulière et plane avant le lissage.", "isCorrect": True},
                        {"text": "Le décoffrage.", "isCorrect": False},
                        {"text": "Le ferraillage.", "isCorrect": False}
                    ],
                    "correction": "Le **Régalage** est souvent réalisé avec un râteau ou une règle à niveau."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le risque de positionner les armatures **trop près du parement** (surface) du béton ?",
                    "answerOptions": [
                        {"text": "Le béton sera trop résistant.", "isCorrect": False},
                        {"text": "**La corrosion de l'acier** : le manque d'enrobage expose l'acier à l'humidité et à l'air, ce qui le fait rouiller et éclater le béton.", "isCorrect": True},
                        {"text": "Le béton sera trop mou.", "isCorrect": False},
                        {"text": "L'ouvrage sera trop lourd.", "isCorrect": False}
                    ],
                    "correction": "L'**Enrobage** (épaisseur de béton autour de l'acier) est une cote essentielle à respecter (souvent $2 \text{ à } 5 \text{ cm}$)."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment s'appelle la barre d'acier courte, pliée en rectangle ou en cercle, qui **entoure** les barres longitudinales dans un poteau ou une poutre ?",
                    "answerOptions": [
                        {"text": "Le fil de fer.", "isCorrect": False},
                        {"text": "L'**Étrier** (ou Cadre).", "isCorrect": True},
                        {"text": "L'armature principale.", "isCorrect": False},
                        {"text": "Le treillis soudé.", "isCorrect": False}
                    ],
                    "correction": "L'**Étrier** reprend les efforts tranchants et empêche les barres principales de flamber (se déformer)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel type de coffrage est utilisé de manière temporaire pour couler des dalles ou des planchers ?",
                    "answerOptions": [
                        {"text": "Le coffrage perdu.", "isCorrect": False},
                        {"text": "Le **Coffrage Vertical (ou banche)**.", "isCorrect": False},
                        {"text": "Le **Coffrage Horizontal (ou table)**, souvent réalisé à l'aide de poutrelles et d'étais.", "isCorrect": True},
                        {"text": "Le coffrage en $\text{U}$.", "isCorrect": False}
                    ],
                    "correction": "Le **Coffrage Horizontal** (étaiement) est essentiel pour le plancher."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le rôle du **Calage** (ou cale d'enrobage) dans la mise en place des armatures ?",
                    "answerOptions": [
                        {"text": "Lier l'acier.", "isCorrect": False},
                        {"text": "Maintenir l'acier à la **distance correcte du fond de coffrage** (garantir l'enrobage) afin que l'armature soit bien centrée dans le béton.", "isCorrect": True},
                        {"text": "Couper l'acier.", "isCorrect": False},
                        {"text": "Vibrer le béton.", "isCorrect": False}
                    ],
                    "correction": "Les **Cales** (souvent en plastique, en mortier ou en béton) assurent l'épaisseur d'enrobage nécessaire."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment appelle-t-on les **tiges métalliques** ou les boulons qui traversent le coffrage et sont serrés pour maintenir deux parois de coffrage face à la pression du béton frais ?",
                    "answerOptions": [
                        {"text": "Les étriers.", "isCorrect": False},
                        {"text": "Les **Tiges de Serrage (ou Tiges d'Entretoise)**.", "isCorrect": True},
                        {"text": "Les chaînages.", "isCorrect": False},
                        {"text": "Les cales.", "isCorrect": False}
                    ],
                    "correction": "Les **Tiges de Serrage** empêchent le coffrage de s'ouvrir ou de se déformer lors du coulage."
                },
                {
                    "questionNumber": 72,
                    "question": "Qu'est-ce qu'un **Treillis Soudé** ?",
                    "answerOptions": [
                        {"text": "Un type de mur.", "isCorrect": False},
                        {"text": "Un ensemble de barres d'acier croisées, **Soudées en Usine** pour former un grillage, utilisé principalement pour armer les dalles et les chapes.", "isCorrect": True},
                        {"text": "Un échafaudage.", "isCorrect": False},
                        {"text": "Un coffrage spécial.", "isCorrect": False}
                    ],
                    "correction": "Le **Treillis Soudé** est un renfort essentiel pour la résistance et la limitation des fissurations des dalles."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le temps minimum de séchage avant de décoffrer un poteau ou un mur vertical non sollicité (conditions standard) ?",
                    "answerOptions": [
                        {"text": "1 heure.", "isCorrect": False},
                        {"text": "Environ **24 à 48 heures** (la résistance minimale est atteinte après $24 \text{ heures}$, mais dépend du ciment et de la température).", "isCorrect": True},
                        {"text": "28 jours.", "isCorrect": False},
                        {"text": "1 semaine.", "isCorrect": False}
                    ],
                    "correction": "Le **Décoffrage** d'ouvrages verticaux peut être rapide ; celui des ouvrages horizontaux (dalles, poutres) est beaucoup plus long (plusieurs semaines)."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le risque majeur d'un **mauvais étaiement** (soutènement provisoire du coffrage) ?",
                    "answerOptions": [
                        {"text": "Le coulage sera lent.", "isCorrect": False},
                        {"text": "**La Rupture du Coffrage** sous la pression du béton frais, entraînant l'effondrement de l'ouvrage et un grave danger pour les ouvriers.", "isCorrect": True},
                        {"text": "Le béton sera trop sec.", "isCorrect": False},
                        {"text": "Le béton sera trop lourd.", "isCorrect": False}
                    ],
                    "correction": "L'**Étaiement** est une question de sécurité absolue sur les planchers et poutres."
                },
                {
                    "questionNumber": 75,
                    "question": "Comment s'appelle l'outil utilisé pour **plier les barres d'armature** aux dimensions souhaitées (manuellement ou électriquement) ?",
                    "answerOptions": [
                        {"text": "La cisaille.", "isCorrect": False},
                        {"text": "La **Cintreuse** (ou Pince à cintrer).", "isCorrect": True},
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "La tenaille.", "isCorrect": False}
                    ],
                    "correction": "La **Cintreuse** permet de créer des coudes et des crochets (équerres) sur l'acier."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le rôle d'un **Poteau** dans la structure du bâtiment ?",
                    "answerOptions": [
                        {"text": "Soutenir le mur.", "isCorrect": False},
                        {"text": "Transmettre les charges verticales (du toit, des planchers, des murs) aux fondations (élément vertical porteur).", "isCorrect": True},
                        {"text": "Créer une ouverture.", "isCorrect": False},
                        {"text": "Rendre la maison jolie.", "isCorrect": False}
                    ],
                    "correction": "Le **Poteau** et la Poutre forment le système porteur dans les constructions à ossature."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est la principale fonction du **béton de propreté** coulé au fond de la fouille (avant les fondations principales) ?",
                    "answerOptions": [
                        {"text": "Assurer la résistance finale.", "isCorrect": False},
                        {"text": "Créer une **Assise Plane et Propre** (hors terre) pour le traçage et la pose des armatures de la fondation (épaisseur environ $5 \text{ cm}$).", "isCorrect": True},
                        {"text": "Isoler thermiquement.", "isCorrect": False},
                        {"text": "Rendre le sol étanche.", "isCorrect": False}
                    ],
                    "correction": "Le **Béton de Propreté** est une couche non structurelle, purement préparatoire."
                },
                {
                    "questionNumber": 78,
                    "question": "Comment s'appelle l'opération qui consiste à **lisser la surface** d'une dalle fraîchement coulée (souvent avec une taloche ou une hélice mécanique) ?",
                    "answerOptions": [
                        {"text": "Le vibrage.", "isCorrect": False},
                        {"text": "Le **Serrage** ou le **Talochage** (pour obtenir la planéité et une bonne cohésion de surface).", "isCorrect": True},
                        {"text": "Le cure.", "isCorrect": False},
                        {"text": "Le décoffrage.", "isCorrect": False}
                    ],
                    "correction": "Le **Serrage** permet d'obtenir une finition de surface dense et durable."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est l'outil utilisé pour **couper les armatures** d'acier au diamètre souhaité ?",
                    "answerOptions": [
                        {"text": "La cintreuse.", "isCorrect": False},
                        {"text": "La **Cisaille à Acier** (ou Cisaille manuelle, ou Tronçonneuse de chantier pour les gros diamètres).", "isCorrect": True},
                        {"text": "La scie à métaux.", "isCorrect": False},
                        {"text": "Le marteau.", "isCorrect": False}
                    ],
                    "correction": "La **Cisaille** est l'outil le plus courant et le plus sécurisé pour la coupe de l'acier."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment appelle-t-on le procédé qui permet de lier deux armatures d'acier pour qu'elles travaillent ensemble (sans soudure) ?",
                    "answerOptions": [
                        {"text": "Le collage.", "isCorrect": False},
                        {"text": "La **Ligature** (assemblage avec du fil de fer recuit).", "isCorrect": True},
                        {"text": "Le cintre.", "isCorrect": False},
                        {"text": "Le calage.", "isCorrect": False}
                    ],
                    "correction": "La **Ligature** maintient les armatures en place dans le coffrage avant le coulage."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SANTÉ, SÉCURITÉ ET RÉGLEMENTATION (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Santé, Sécurité et Règlementation (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'**Équipement de Protection Individuelle (EPI)** indispensable pour protéger la tête du maçon contre les chutes d'objets ou les chocs ?",
                    "answerOptions": [
                        {"text": "Les lunettes.", "isCorrect": False},
                        {"text": "Le **Casque de Chantier** (obligatoire sur la plupart des chantiers).", "isCorrect": True},
                        {"text": "Le masque.", "isCorrect": False},
                        {"text": "Les gants.", "isCorrect": False}
                    ],
                    "correction": "Le **Casque** est un $\text{EPI}$ de catégorie $3$ (protection contre les risques mortels)."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le risque principal lié à l'utilisation des mortiers et bétons (ciment, chaux) pour la peau ?",
                    "answerOptions": [
                        {"text": "Le froid.", "isCorrect": False},
                        {"text": "Les **Brûlures Chimiques** (le ciment est très alcalin, $\text{pH}$ élevé) et les irritations, nécessitant le port de gants et de vêtements couvrants.", "isCorrect": True},
                        {"text": "L'électricité statique.", "isCorrect": False},
                        {"text": "Les coupures.", "isCorrect": False}
                    ],
                    "correction": "Le **Ciment** frais est caustique et peut provoquer de graves brûlures."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel $\text{EPI}$ est obligatoire lors de la coupe de matériaux (briques, parpaings) à la tronçonneuse ou à la meuleuse ?",
                    "answerOptions": [
                        {"text": "Le casque anti-bruit.", "isCorrect": False},
                        {"text": "Les **Lunettes de Protection** (ou Écran facial) pour protéger des projections de poussières et de fragments.", "isCorrect": True},
                        {"text": "Les chaussures de sécurité.", "isCorrect": False},
                        {"text": "Le gilet jaune.", "isCorrect": False}
                    ],
                    "correction": "La **Protection Oculaire** est vitale contre les risques de projection."
                },
                {
                    "questionNumber": 84,
                    "question": "Pourquoi doit-on effectuer le **signalement** des réseaux enterrés (eau, gaz, électricité) avant de creuser une fouille ?",
                    "answerOptions": [
                        {"text": "Pour respecter les plans.", "isCorrect": False},
                        {"text": "**Pour prévenir les accidents graves** (électrocution, explosion) et les dommages aux infrastructures (application de la **DICT** : Déclaration d'Intention de Commencement de Travaux).", "isCorrect": True},
                        {"text": "Pour aller plus vite.", "isCorrect": False},
                        {"text": "Pour avoir une belle fondation.", "isCorrect": False}
                    ],
                    "correction": "La **DICT** et le marquage au sol des réseaux sont une obligation légale de sécurité."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le risque majeur lié à l'utilisation d'un **échafaudage** mal monté ou non sécurisé ?",
                    "answerOptions": [
                        {"text": "Un travail lent.", "isCorrect": False},
                        {"text": "La **Chute de Hauteur** du maçon ou l'effondrement de la structure (nécessite une formation $\text{R}408$ ou $\text{R}457$).", "isCorrect": True},
                        {"text": "Une mauvaise qualité de l'enduit.", "isCorrect": False},
                        {"text": "Un mur pas droit.", "isCorrect": False}
                    ],
                    "correction": "Le travail en hauteur est la première cause d'accidents mortels dans le $\text{BTP}$. L'échafaudage doit être monté et utilisé selon les règles de l'art."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel $\text{EPI}$ est nécessaire lors du malaxage de mortier ou de béton dans un local fermé ou lors de travaux générant beaucoup de poussière (coupe) ?",
                    "answerOptions": [
                        {"text": "Les gants.", "isCorrect": False},
                        {"text": "Le **Masque de Protection Respiratoire** (P$2$ ou P$3$) pour les poussières fines de silice et de ciment.", "isCorrect": True},
                        {"text": "Le casque antibruit.", "isCorrect": False},
                        {"text": "Le gilet réfléchissant.", "isCorrect": False}
                    ],
                    "correction": "La **Protection Respiratoire** prévient les maladies professionnelles (silicose, asthme)."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment s'appelle le document qui liste tous les risques du chantier et les mesures de prévention associées (obligatoire pour les gros chantiers) ?",
                    "answerOptions": [
                        {"text": "Le permis de construire.", "isCorrect": False},
                        {"text": "Le **PPSPS (Plan Particulier de Sécurité et de Protection de la Santé)**.", "isCorrect": True},
                        {"text": "Le plan de masse.", "isCorrect": False},
                        {"text": "Le $\text{DTU}$.", "isCorrect": False}
                    ],
                    "correction": "Le **PPSPS** organise la sécurité collective sur les chantiers."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est la règle de sécurité à respecter impérativement avant de commencer la démolition d'un mur ?",
                    "answerOptions": [
                        {"text": "Utiliser un gros marteau.", "isCorrect": False},
                        {"text": "**Vérifier l'absence de réseaux** (électricité, gaz, eau) et **s'assurer que le mur n'est pas porteur** (ou qu'il est correctement étayé).", "isCorrect": True},
                        {"text": "Mettre de l'eau.", "isCorrect": False},
                        {"text": "Utiliser une scie à bois.", "isCorrect": False}
                    ],
                    "correction": "La **Sécurité Structurelle** et le contrôle des réseaux sont des étapes non négociables en démolition."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le risque lié à l'utilisation d'outils vibrants (marteau-piqueur, burineur) sur une longue période ?",
                    "answerOptions": [
                        {"text": "Le bruit.", "isCorrect": False},
                        {"text": "Les **Troubles Musculo-Squelettiques (TMS)** et notamment le syndrome de Raynaud (doigts blancs) causé par la vibration.", "isCorrect": True},
                        {"text": "Le feu.", "isCorrect": False},
                        {"text": "Le glissement.", "isCorrect": False}
                    ],
                    "correction": "L'utilisation d'outils vibrants est limitée dans le temps et nécessite des pauses et des gants anti-vibration."
                },
                {
                    "questionNumber": 90,
                    "question": "Que signifie l'acronyme **DTU** dans le $\text{BTP}$ ?",
                    "answerOptions": [
                        {"text": "Déclaration de Travaux Urgents.", "isCorrect": False},
                        {"text": "**Document Technique Unifié** : ce sont les normes françaises de construction qui fixent les règles de l'art pour les travaux (ex : $\text{DTU}$ $20.1$ pour la maçonnerie).", "isCorrect": True},
                        {"text": "Droit de Travail Unifié.", "isCorrect": False},
                        {"text": "Développement Technique Urbain.", "isCorrect": False}
                    ],
                    "correction": "Le respect des **$\text{DTU}$** est la garantie de la qualité et de la durabilité des ouvrages (et des assurances)."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle est la bonne technique pour **soulever une charge lourde** (sac de ciment, parpaing) ?",
                    "answerOptions": [
                        {"text": "Se pencher en gardant les jambes droites.", "isCorrect": False},
                        {"text": "**Fléchir les genoux, garder le dos droit et soulever la charge avec la force des jambes** (méthode de la $\text{PRAP}$ : Prévention des Risques liés à l'Activité Physique).", "isCorrect": True},
                        {"text": "Tirer sur les bras.", "isCorrect": False},
                        {"text": "Utiliser une seule main.", "isCorrect": False}
                    ],
                    "correction": "La **Bonne Posture** prévient les lombalgies et les $\text{TMS}$."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le rôle du **Gilet de Haute Visibilité** (Jaune, Orange) sur un chantier ?",
                    "answerOptions": [
                        {"text": "Protéger du froid.", "isCorrect": False},
                        {"text": "**Être vu par les engins de chantier** (grue, pelleteuse) ou sur les chantiers en bord de voirie (obligation légale pour la sécurité collective).", "isCorrect": True},
                        {"text": "Protéger de la pluie.", "isCorrect": False},
                        {"text": "Protéger des chocs.", "isCorrect": False}
                    ],
                    "correction": "Le **Gilet** est essentiel pour la prévention des collisions avec les machines."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment appelle-t-on le risque de **chute d'un ouvrier** dans une fouille ou une tranchée non protégée ?",
                    "answerOptions": [
                        {"text": "Le risque électrique.", "isCorrect": False},
                        {"text": "Le **Risque de Chute de Plain-Pied ou de Hauteur**.", "isCorrect": True},
                        {"text": "Le risque chimique.", "isCorrect": False},
                        {"text": "Le risque incendie.", "isCorrect": False}
                    ],
                    "correction": "Les **Tranchées** doivent être sécurisées par des garde-corps ou des blindages."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle est la distance de sécurité minimale à respecter lors de la mise en place d'un échafaudage à proximité d'une **ligne électrique aérienne** ?",
                    "answerOptions": [
                        {"text": "50 $\text{cm}$.", "isCorrect": False},
                        {"text": "Elle dépend du voltage, mais est généralement d'au moins **$3 \text{ mètres}$** pour le $HTA$ (Haute Tension $\text{A}$) et **$5 \text{ mètres}$** pour le $HTB$ (Haute Tension $\text{B}$).", "isCorrect": True},
                        {"text": "10 $\text{cm}$.", "isCorrect": False},
                        {"text": "1 $\text{ mètre}$.", "isCorrect": False}
                    ],
                    "correction": "Le risque électrique est mortel ; la **Distance de Sécurité** est une mesure de prévention absolue."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le $\text{EPI}$ à porter lors de la **manutention** de parpaings ou de fers à béton ?",
                    "answerOptions": [
                        {"text": "Le masque.", "isCorrect": False},
                        {"text": "Les **Gants de Protection** (contre les coupures, les abrasions, les projections).", "isCorrect": True},
                        {"text": "Les bouchons d'oreille.", "isCorrect": False},
                        {"text": "Les bottes en caoutchouc.", "isCorrect": False}
                    ],
                    "correction": "Les **Gants** protègent des risques mécaniques et chimiques."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment appelle-t-on l'examen médical qui a pour but de vérifier l'aptitude d'un ouvrier à son poste de travail (obligatoire après l'embauche) ?",
                    "answerOptions": [
                        {"text": "Le contrôle de l'assurance.", "isCorrect": False},
                        {"text": "La **Visite Médicale d'Information et de Prévention (VIP)** ou d'aptitude professionnelle.", "isCorrect": True},
                        {"text": "L'examen de passage.", "isCorrect": False},
                        {"text": "Le test de connaissance.", "isCorrect": False}
                    ],
                    "correction": "La **Médecine du Travail** assure le suivi de la santé des ouvriers, notamment pour les risques liés au bruit, aux vibrations et aux produits chimiques."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque à ne pas nettoyer la bétonnière immédiatement après utilisation ?",
                    "answerOptions": [
                        {"text": "Un court-circuit.", "isCorrect": False},
                        {"text": "Le **Durcissement du Béton** à l'intérieur de la cuve, qui rend la machine inutilisable et nécessite un nettoyage long et dangereux (burinage).", "isCorrect": True},
                        {"text": "Une fuite d'huile.", "isCorrect": False},
                        {"text": "Le vol.", "isCorrect": False}
                    ],
                    "correction": "L'**Entretien** du matériel est une compétence essentielle du maçon."
                },
                {
                    "questionNumber": 98,
                    "question": "Que doit-on faire de l'eau utilisée pour rincer les outils ou la bétonnière après le gâchage (eau de lavage du béton) ?",
                    "answerOptions": [
                        {"text": "La jeter dans le jardin.", "isCorrect": False},
                        {"text": "**La récupérer (décantation)** ou la faire décaper dans une aire spécifique pour éviter la pollution des sols et des eaux pluviales (eau très alcaline).", "isCorrect": True},
                        {"text": "La boire.", "isCorrect": False},
                        {"text": "La laisser s'évaporer.", "isCorrect": False}
                    ],
                    "correction": "Le **Respect de l'Environnement** est un enjeu majeur du $\text{BTP}$ (gestion des déchets et des eaux usées)."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment appelle-t-on la **barrière physique** temporaire installée en périphérie des dalles ou toitures-terrasses pour prévenir les chutes de hauteur ?",
                    "answerOptions": [
                        {"text": "Le filet de sécurité.", "isCorrect": False},
                        {"text": "Le **Garde-Corps Périphérique Provisoire (GCPP)**.", "isCorrect": True},
                        {"text": "La main courante.", "isCorrect": False},
                        {"text": "Le $\text{PPSPS}$.", "isCorrect": False}
                    ],
                    "correction": "Le **Garde-Corps** est la protection collective la plus efficace contre les chutes de bord de dalle."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le rôle du **balisage** ou du ruban de signalisation sur le chantier ?",
                    "answerOptions": [
                        {"text": "Cacher les travaux.", "isCorrect": False},
                        {"text": "**Délimiter les zones de danger** (fouilles, matériaux, zone de grutage) et interdire l'accès aux personnes non autorisées (public, ouvriers non concernés).", "isCorrect": True},
                        {"text": "Décorer.", "isCorrect": False},
                        {"text": "Mesurer les distances.", "isCorrect": False}
                    ],
                    "correction": "Le **Balisage** est la première étape de la sécurisation des zones dangereuses."
                },
            ]
        }
    }
}