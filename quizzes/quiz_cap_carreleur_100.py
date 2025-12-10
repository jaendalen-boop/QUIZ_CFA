quiz_data = {
    "title": "Quiz CAP Carreleur : Technologie, Techniques, Sécurité et Calculs (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET SUPPORTS (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET SUPPORTS (Questions 1 à 20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Dans le classement UPEC, à quoi correspond précisément la lettre 'E' ?",
                    "answerOptions": [
                        {"text": "Au comportement du matériau face à l'eau et à l'humidité", "isCorrect": True},
                        {"text": "À l'épaisseur du carreau en millimètres", "isCorrect": False},
                        {"text": "À l'esthétique générale du produit", "isCorrect": False},
                        {"text": "À l'envers du carreau (le dos)", "isCorrect": False}
                    ],
                    "correction": "Le classement UPEC définit l'usage des locaux. E (de E1 à E3) classe la résistance à l'eau. Une salle de bain requiert un classement E élevé (E3), contrairement à une chambre (E1)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la propriété principale qui distingue le Grès Cérame des autres céramiques ?",
                    "answerOptions": [
                        {"text": "Sa porosité quasi nulle (inférieure à 0,5 %)", "isCorrect": True},
                        {"text": "Sa couleur toujours rouge brique due à l'argile", "isCorrect": False},
                        {"text": "Le fait qu'il soit obligatoirement émaillé en surface", "isCorrect": False},
                        {"text": "Sa fragilité importante lors de la découpe", "isCorrect": False}
                    ],
                    "correction": "Le grès cérame est vitrifié dans la masse lors d'une cuisson à très haute température. Cette absence de porosité le rend ingélif (résiste au gel), très dur et résistant aux taches."
                },
                {
                    "questionNumber": 3,
                    "question": "Que signifie la classification 'C2S1' pour un mortier-colle ?",
                    "answerOptions": [
                        {"text": "C'est un mortier-colle amélioré et déformable", "isCorrect": True},
                        {"text": "C'est une colle standard pour mur intérieur uniquement", "isCorrect": False},
                        {"text": "C'est une colle en pâte prête à l'emploi", "isCorrect": False},
                        {"text": "C'est un ciment pur sans adjuvant", "isCorrect": False}
                    ],
                    "correction": "C est un mortier-colle (Ciment), 2 signifie qu'il a des performances d'adhérence élevées, et S1 indique qu'il est capable de se déformer légèrement pour suivre les mouvements du support (plancher chauffant, façade)."
                },
                {
                    "questionNumber": 4,
                    "question": "La faïence est un produit céramique destiné exclusivement :",
                    "answerOptions": [
                        {"text": "Au revêtement mural intérieur", "isCorrect": True},
                        {"text": "Aux sols de salle de bain privatifs", "isCorrect": False},
                        {"text": "Aux terrasses extérieures couvertes", "isCorrect": False},
                        {"text": "Aux plafonds suspendus", "isCorrect": False}
                    ],
                    "correction": "La faïence a une pâte 'tendre' et poreuse (biscuit). Son émail est décoratif mais fragile. Elle ne résiste ni au gel, ni à l'usure de la marche (abrasion), d'où son usage mural strict."
                },
                {
                    "questionNumber": 5,
                    "question": "Pourquoi applique-t-on un primaire d'accrochage sur un support lisse avant de carreler ?",
                    "answerOptions": [
                        {"text": "Pour créer un pont d'adhérence chimique et mécanique", "isCorrect": True},
                        {"text": "Pour nettoyer le sol de la poussière", "isCorrect": False},
                        {"text": "Pour changer la couleur du support", "isCorrect": False},
                        {"text": "Pour imperméabiliser totalement le sol", "isCorrect": False}
                    ],
                    "correction": "Sur un support 'fermé' (lisse, non absorbant comme un ancien carrelage), la colle n'accroche pas. Le primaire apporte une rugosité et une compatibilité chimique pour que la colle tienne."
                },
                {
                    "questionNumber": 6,
                    "question": "Lequel de ces matériaux est une pierre naturelle calcaire ?",
                    "answerOptions": [
                        {"text": "Le Travertin", "isCorrect": True},
                        {"text": "Le Grès cérame émaillé", "isCorrect": False},
                        {"text": "Le carreau de ciment", "isCorrect": False},
                        {"text": "La pâte de verre", "isCorrect": False}
                    ],
                    "correction": "Le travertin est une roche sédimentaire calcaire caractérisée par de petites cavités (vacuoles). C'est un matériau naturel, contrairement aux autres qui sont manufacturés."
                },
                {
                    "questionNumber": 7,
                    "question": "Sur un support base plâtre (carreau de plâtre, enduit), quelle précaution chimique est indispensable avant de coller au ciment ?",
                    "answerOptions": [
                        {"text": "Appliquer un primaire pour isoler le plâtre du ciment", "isCorrect": True},
                        {"text": "Mouiller abondamment le plâtre à l'eau", "isCorrect": False},
                        {"text": "Poncer le plâtre jusqu'à la brique", "isCorrect": False},
                        {"text": "Utiliser uniquement du ciment prompt", "isCorrect": False}
                    ],
                    "correction": "Le contact direct entre le plâtre et le ciment (alcalin) en présence d'humidité crée de l'ettringite (sel gonflant) qui décolle le carrelage. Le primaire sert de barrière."
                },
                {
                    "questionNumber": 8,
                    "question": "La norme PEI (Porcelain Enamel Institute) mesure :",
                    "answerOptions": [
                        {"text": "La résistance à l'abrasion de surface des carreaux émaillés", "isCorrect": True},
                        {"text": "La résistance à la glissance pieds nus", "isCorrect": False},
                        {"text": "La résistance à la flexion du carreau", "isCorrect": False},
                        {"text": "La résistance au gel", "isCorrect": False}
                    ],
                    "correction": "Plus l'indice PEI est élevé (de I à V), plus l'émail résiste au piétinement sans s'user. Un PEI V est nécessaire pour un hall d'entrée d'immeuble."
                },
                {
                    "questionNumber": 9,
                    "question": "Un support classé 'Wedi' ou 'Q-Board' est constitué de :",
                    "answerOptions": [
                        {"text": "Mousse rigide de polystyrène extrudé armée d'un tissu de verre et mortier", "isCorrect": True},
                        {"text": "Plâtre hydrofugé simple", "isCorrect": False},
                        {"text": "Bois aggloméré marine", "isCorrect": False},
                        {"text": "Laine de roche compressée", "isCorrect": False}
                    ],
                    "correction": "Ces panneaux sont légers, imputrescibles, étanches et offrent un support idéal pour carreler directement (tabliers de baignoire, plans vasques)."
                },
                {
                    "questionNumber": 10,
                    "question": "La 'Tomette' traditionnelle en terre cuite nécessite un traitement après pose car :",
                    "answerOptions": [
                        {"text": "Elle est naturellement poreuse et tache facilement", "isCorrect": True},
                        {"text": "Elle est trop glissante", "isCorrect": False},
                        {"text": "Elle risque de fondre", "isCorrect": False},
                        {"text": "Elle change de couleur à la lumière", "isCorrect": False}
                    ],
                    "correction": "La terre cuite absorbe les liquides (huile, vin). Il faut la saturer avec un hydrofuge/oléofuge ou de l'huile de lin pour la protéger durablement."
                },
                {
                    "questionNumber": 11,
                    "question": "Qu'est-ce qu'un SPEC (Système de Protection à l'Eau sous Carrelage) ?",
                    "answerOptions": [
                        {"text": "Une protection liquide appliquée au mur avant carrelage en zone humide", "isCorrect": True},
                        {"text": "Un système d'étanchéité totale pour piscine", "isCorrect": False},
                        {"text": "Un type de colle étanche", "isCorrect": False},
                        {"text": "Un joint spécial", "isCorrect": False}
                    ],
                    "correction": "Le SPEC protège le support sensible (plâtre) des éclaboussures dans une douche, mais ne résiste pas à la pression de l'eau comme une étanchéité de bassin."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la particularité d'une colle 'D2' (Dispersion) ?",
                    "answerOptions": [
                        {"text": "C'est une pâte prête à l'emploi résistante à l'humidité pour murs intérieurs", "isCorrect": True},
                        {"text": "C'est une poudre à gâcher avec de l'eau", "isCorrect": False},
                        {"text": "C'est une colle pour l'extérieur", "isCorrect": False},
                        {"text": "C'est une colle rapide (30 minutes)", "isCorrect": False}
                    ],
                    "correction": "Les colles en pâte (D) sèchent par évaporation de l'eau. D2 indique une tenue améliorée à l'humidité, idéale pour les murs de salles de bain, mais interdite au sol."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel outil est le plus adapté pour percer un trou propre dans du grès cérame très dur ?",
                    "answerOptions": [
                        {"text": "Un trépan ou une scie cloche diamantée", "isCorrect": True},
                        {"text": "Un foret béton classique à percussion", "isCorrect": False},
                        {"text": "Une mèche à bois plate", "isCorrect": False},
                        {"text": "Un pointeau et un marteau", "isCorrect": False}
                    ],
                    "correction": "Le grès cérame est trop dur pour être percé par percussion (risque de casse). Il faut l'user par abrasion avec du diamant."
                },
                {
                    "questionNumber": 14,
                    "question": "Un mortier de jointoiement 'Flex' ou souple est conseillé pour :",
                    "answerOptions": [
                        {"text": "Les supports soumis à des déformations (plancher bois, chauffage au sol)", "isCorrect": True},
                        {"text": "Les murs en béton statiques", "isCorrect": False},
                        {"text": "Reboucher des trous dans le mur", "isCorrect": False},
                        {"text": "Coller les plinthes", "isCorrect": False}
                    ],
                    "correction": "Ce mortier contient des résines qui lui permettent d'absorber de légères tensions sans fissurer, contrairement à un joint ciment standard rigide."
                },
                {
                    "questionNumber": 15,
                    "question": "La chape fluide Anhydrite est fabriquée à base de :",
                    "answerOptions": [
                        {"text": "Sulfate de calcium (Gypse)", "isCorrect": True},
                        {"text": "Ciment Portland gris", "isCorrect": False},
                        {"text": "Chaux hydraulique", "isCorrect": False},
                        {"text": "Argile expansée", "isCorrect": False}
                    ],
                    "correction": "L'anhydrite permet de grandes surfaces sans joints de fractionnement et une mise en chauffe rapide, mais craint l'humidité résiduelle et nécessite un primaire spécifique."
                },
                {
                    "questionNumber": 16,
                    "question": "Le profilé de finition 'quart de rond' en PVC ou Alu sert principalement à :",
                    "answerOptions": [
                        {"text": "Protéger l'angle sortant des chocs et masquer la tranche du carreau", "isCorrect": True},
                        {"text": "Faire l'étanchéité de la douche", "isCorrect": False},
                        {"text": "Soutenir le plafond", "isCorrect": False},
                        {"text": "Remplacer le joint de dilatation", "isCorrect": False}
                    ],
                    "correction": "La coupe d'un carreau est souvent tranchante et inesthétique (biscuit visible). Le profilé offre une finition propre, arrondie et sécurisée."
                },
                {
                    "questionNumber": 17,
                    "question": "À quoi sert le peigne (spatule crantée) du carreleur ?",
                    "answerOptions": [
                        {"text": "À calibrer l'épaisseur du lit de colle de manière régulière", "isCorrect": True},
                        {"text": "À gratter l'ancien carrelage", "isCorrect": False},
                        {"text": "À lisser les joints", "isCorrect": False},
                        {"text": "À mélanger la colle dans le seau", "isCorrect": False}
                    ],
                    "correction": "La taille des dents (6mm, 9mm, double encollage) détermine la quantité de colle déposée pour assurer le transfert nécessaire selon la taille du carreau."
                },
                {
                    "questionNumber": 18,
                    "question": "La norme de glissance 'R' (ex: R10, R11) concerne l'adhérence :",
                    "answerOptions": [
                        {"text": "Pieds chaussés (locaux professionnels, terrasses)", "isCorrect": True},
                        {"text": "Pieds nus (piscines)", "isCorrect": False},
                        {"text": "Des véhicules", "isCorrect": False},
                        {"text": "De la colle au support", "isCorrect": False}
                    ],
                    "correction": "Pour les pieds nus (salle de bain, piscine), on utilise le classement A, B, C. Le classement R (Ramp) concerne la sécurité avec chaussures."
                },
                {
                    "questionNumber": 19,
                    "question": "Un carreau 'Rectifié' a subi un traitement mécanique pour :",
                    "answerOptions": [
                        {"text": "Avoir des bords parfaitement droits et des dimensions exactes", "isCorrect": True},
                        {"text": "Être rendu antidérapant", "isCorrect": False},
                        {"text": "Devenir brillant comme un miroir", "isCorrect": False},
                        {"text": "Résister aux acides", "isCorrect": False}
                    ],
                    "correction": "La rectification est une taille mécanique des bords pour obtenir des dimensions exactes et des angles vifs, permettant des joints très fins (2 mm) pour un aspect plus contemporain et monolithique."
                },
                {
                    "questionNumber": 20,
                    "question": "La 'Durée Pratique d'Utilisation' (DPU) d'une colle désigne :",
                    "answerOptions": [
                        {"text": "Le temps disponible pour utiliser le mélange dans le seau avant qu'il ne durcisse", "isCorrect": True},
                        {"text": "Le temps de séchage une fois posé au mur", "isCorrect": False},
                        {"text": "La durée de garantie décennale", "isCorrect": False},
                        {"text": "Le temps qu'il faut pour mélanger la poudre", "isCorrect": False}
                    ],
                    "correction": "Une fois gâchée, la réaction chimique commence. Après la DPU (ex: 3h), la colle perd ses propriétés et doit être jetée, il ne faut jamais rajouter d'eau."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNIQUES DE POSE (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNIQUES DE POSE (Questions 21 à 40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "La technique du 'Double Encollage' consiste à :",
                    "answerOptions": [
                        {"text": "Appliquer la colle sur le support ET au dos du carreau", "isCorrect": True},
                        {"text": "Mettre deux couches de colle l'une sur l'autre sur le sol", "isCorrect": False},
                        {"text": "Utiliser deux types de colles différents pour plus de sécurité", "isCorrect": False},
                        {"text": "Coller le carreau puis recoller un autre carreau dessus", "isCorrect": False}
                    ],
                    "correction": "Obligatoire pour les grands formats, cette technique chasse l'air sous le carreau et garantit un taux de transfert de colle proche de 100%."
                },
                {
                    "questionNumber": 22,
                    "question": "Pour démarrer une pose droite au sol, on trace généralement :",
                    "answerOptions": [
                        {"text": "Deux axes perpendiculaires au centre de la pièce ou équilibrés par rapport à l'entrée", "isCorrect": True},
                        {"text": "Une ligne le long du mur le plus long", "isCorrect": False},
                        {"text": "Un trait au hasard au milieu", "isCorrect": False},
                        {"text": "Le contour des meubles", "isCorrect": False}
                    ],
                    "correction": "Démarrer au centre permet de répartir les coupes (les chutes) de manière égale sur les côtés, ce qui est plus esthétique que d'avoir un carreau entier d'un côté et une petite coupe de l'autre."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la largeur minimale autorisée pour un joint de carrelage au sol (hors rectifié) ?",
                    "answerOptions": [
                        {"text": "4 mm minimum selon le DTU (pour carreaux pressés non rectifiés)", "isCorrect": True},
                        {"text": "0 mm (pose à joints nuls)", "isCorrect": False},
                        {"text": "10 mm obligatoirement", "isCorrect": False},
                        {"text": "1 mm maximum", "isCorrect": False}
                    ],
                    "correction": "La pose à 'joint nul' est interdite car elle ne permet pas la dilatation des matériaux. Pour du rectifié, on peut descendre à 2 mm."
                },
                {
                    "questionNumber": 24,
                    "question": "Le joint de fractionnement de la chape doit être :",
                    "answerOptions": [
                        {"text": "Respecté et prolongé à travers le carrelage (profilé souple ou mastic)", "isCorrect": True},
                        {"text": "Recouvert par le carrelage pour le cacher", "isCorrect": False},
                        {"text": "Rempli de ciment dur", "isCorrect": False},
                        {"text": "Déplacé selon l'envie du client", "isCorrect": False}
                    ],
                    "correction": "Si on carrele par-dessus un joint de fractionnement sans le respecter, le carrelage fissurera exactement à cet endroit lors des mouvements de la chape."
                },
                {
                    "questionNumber": 25,
                    "question": "Pour réaliser une coupe en angle rentrant ('coupe en drapeau' ou en L), il est conseillé de :",
                    "answerOptions": [
                        {"text": "Percer un trou à l'intersection des traits de coupe avant de couper", "isCorrect": True},
                        {"text": "Couper directement avec la carrelette en forçant", "isCorrect": False},
                        {"text": "Casser le carreau en deux et recoller", "isCorrect": False},
                        {"text": "Chauffer le carreau au chalumeau", "isCorrect": False}
                    ],
                    "correction": "Le trou (réalisé à la perceuse ou meuleuse) évite la concentration de contraintes qui ferait fendre le carreau dans l'angle intérieur."
                },
                {
                    "questionNumber": 26,
                    "question": "L'opération de 'battage' des carreaux a pour but :",
                    "answerOptions": [
                        {"text": "D'écraser les sillons de colle pour assurer un bon transfert", "isCorrect": True},
                        {"text": "De vérifier la solidité du carreau", "isCorrect": False},
                        {"text": "De faire sécher la colle plus vite", "isCorrect": False},
                        {"text": "D'enlever la poussière", "isCorrect": False}
                    ],
                    "correction": "On tapote le carreau (maillet ou batte) pour chasser l'air et assurer que la colle mouille bien toute la surface du dos du carreau."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle pente doit-on respecter pour une douche à l'italienne ?",
                    "answerOptions": [
                        {"text": "Entre 1 cm et 2 cm par mètre vers la bonde", "isCorrect": True},
                        {"text": "Le sol doit être parfaitement plat", "isCorrect": False},
                        {"text": "10 cm par mètre", "isCorrect": False},
                        {"text": "Une pente inverse pour retenir l'eau", "isCorrect": False}
                    ],
                    "correction": "L'évacuation de l'eau doit être rapide pour éviter la stagnation et les glissades."
                },
                {
                    "questionNumber": 28,
                    "question": "Que se passe-t-il si on ne respecte pas le joint périphérique (dilatation) ?",
                    "answerOptions": [
                        {"text": "Le carrelage se soulève au milieu de la pièce ou casse les plinthes", "isCorrect": True},
                        {"text": "Le carrelage change de couleur", "isCorrect": False},
                        {"text": "Les joints se creusent", "isCorrect": False},
                        {"text": "Rien, c'est juste esthétique", "isCorrect": False}
                    ],
                    "correction": "Le carrelage et la chape se dilatent. S'ils sont bloqués contre les murs, la pression énorme fait 'exploser' ou soulever le sol (phénomène de flambement)."
                },
                {
                    "questionNumber": 29,
                    "question": "La pose diagonale s'effectue traditionnellement avec un angle de :",
                    "answerOptions": [
                        {"text": "45 degrés par rapport aux murs principaux", "isCorrect": True},
                        {"text": "30 degrés", "isCorrect": False},
                        {"text": "10 degrés", "isCorrect": False},
                        {"text": "90 degrés", "isCorrect": False}
                    ],
                    "correction": "Cette pose est plus complexe (beaucoup de coupes) mais permet de masquer les défauts de parallélisme des murs d'une pièce ('faux d'équerre')."
                },
                {
                    "questionNumber": 30,
                    "question": "Les croisillons 'récupérables' doivent être :",
                    "answerOptions": [
                        {"text": "Retirés avant de faire les joints", "isCorrect": True},
                        {"text": "Laissés dans le joint et recouverts", "isCorrect": False},
                        {"text": "Collés au fond", "isCorrect": False},
                        {"text": "Fondus au chalumeau", "isCorrect": False}
                    ],
                    "correction": "Si on les laisse, ils créent une surépaisseur ou apparaissent à travers le joint fin, ce qui est inesthétique et fragilise l'étanchéité."
                },
                {
                    "questionNumber": 31,
                    "question": "Le 'Temps d'ouverture' de la colle correspond :",
                    "answerOptions": [
                        {"text": "Au délai maximum entre l'étalement de la colle et la pose du carreau", "isCorrect": True},
                        {"text": "Au temps qu'il faut pour ouvrir le sac", "isCorrect": False},
                        {"text": "Au temps de séchage avant de marcher dessus", "isCorrect": False},
                        {"text": "À la pause déjeuner", "isCorrect": False}
                    ],
                    "correction": "Il ne faut pas étaler de la colle trop à l'avance. Si la colle forme une 'peau' en surface au toucher, elle est morte : il faut la racler et en remettre."
                },
                {
                    "questionNumber": 32,
                    "question": "En pose décalée (type parquet), pourquoi limite-t-on le décalage à 1/3 du carreau ?",
                    "answerOptions": [
                        {"text": "Pour limiter les désaffleurs liés au tuilage (courbure) naturel des carreaux", "isCorrect": True},
                        {"text": "Parce que c'est interdit par la loi", "isCorrect": False},
                        {"text": "Pour économiser des carreaux", "isCorrect": False},
                        {"text": "Pour utiliser moins de colle", "isCorrect": False}
                    ],
                    "correction": "Les carreaux longs sont souvent bombés au centre. Si on met le centre (point haut) à côté du bout (point bas) du carreau voisin, on crée une marche (désaffleur)."
                },
                {
                    "questionNumber": 33,
                    "question": "Lors d'une pose murale, pourquoi utilise-t-on un tasseau ou une règle de départ ?",
                    "answerOptions": [
                        {"text": "Pour démarrer le deuxième rang parfaitement de niveau", "isCorrect": True},
                        {"text": "Pour empêcher les carreaux de tomber", "isCorrect": False},
                        {"text": "Pour décorer le bas du mur", "isCorrect": False},
                        {"text": "Pour cacher la misère", "isCorrect": False}
                    ],
                    "correction": "Le sol n'est jamais droit. On pose le carrelage mural à partir d'une ligne horizontale parfaite, puis on coupe les carreaux du bas (1er rang) sur mesure à la fin."
                },
                {
                    "questionNumber": 34,
                    "question": "Le désaffleur désigne :",
                    "answerOptions": [
                        {"text": "Une différence de niveau entre deux carreaux adjacents (une 'dalle')", "isCorrect": True},
                        {"text": "Un carreau d'une couleur différente", "isCorrect": False},
                        {"text": "Un joint mal fait", "isCorrect": False},
                        {"text": "Une fissure dans le carreau", "isCorrect": False}
                    ],
                    "correction": "C'est un défaut de planéité locale. Il y a des tolérances normatives, mais le carreleur doit viser le 'zéro désaffleur' pour l'esthétique et la sécurité."
                },
                {
                    "questionNumber": 35,
                    "question": "La pince 'Bec de Perroquet' est utilisée pour :",
                    "answerOptions": [
                        {"text": "Grignoter la céramique pour des coupes courbes ou complexes", "isCorrect": True},
                        {"text": "Couper les rails métalliques", "isCorrect": False},
                        {"text": "Arracher les vieux carreaux", "isCorrect": False},
                        {"text": "Serrer les boulons", "isCorrect": False}
                    ],
                    "correction": "Elle permet d'ajuster une coupe autour d'un tuyau ou d'une huisserie là où la carrelette droite ne peut pas aller."
                },
                {
                    "questionNumber": 36,
                    "question": "Pour percer du carrelage, il faut impérativement enlever quel mode sur la perceuse ?",
                    "answerOptions": [
                        {"text": "Le mode percussion", "isCorrect": True},
                        {"text": "Le mode vissage", "isCorrect": False},
                        {"text": "Le sens de rotation", "isCorrect": False},
                        {"text": "La lumière", "isCorrect": False}
                    ],
                    "correction": "La percussion frappe le carreau et le brise instantanément. Il faut percer en rotation simple avec un foret adapté (béton carbure ou diamant)."
                },
                {
                    "questionNumber": 37,
                    "question": "Une plinthe à gorge (à talon) est obligatoire dans :",
                    "answerOptions": [
                        {"text": "Les cuisines collectives et locaux agroalimentaires", "isCorrect": True},
                        {"text": "Les chambres à coucher", "isCorrect": False},
                        {"text": "Les salons", "isCorrect": False},
                        {"text": "Les plafonds", "isCorrect": False}
                    ],
                    "correction": "L'arrondi concave à la base de la plinthe facilite le nettoyage et empêche la crasse de s'accumuler dans l'angle droit mur/sol, conformément aux normes d'hygiène."
                },
                {
                    "questionNumber": 38,
                    "question": "La pose scellée traditionnelle consiste à :",
                    "answerOptions": [
                        {"text": "Poser les carreaux sur un mortier de chape frais (pose à l'avancement)", "isCorrect": True},
                        {"text": "Coller les carreaux sur une chape sèche", "isCorrect": False},
                        {"text": "Visser les carreaux", "isCorrect": False},
                        {"text": "Poser les carreaux sur un lit de sable sec", "isCorrect": False}
                    ],
                    "correction": "C'est une technique complexe qui permet de rattraper de gros niveaux et de solidariser totalement le revêtement au support en une seule opération."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le délai moyen avant de pouvoir marcher sur un carrelage collé (ouverture au trafic piéton) ?",
                    "answerOptions": [
                        {"text": "24 heures", "isCorrect": True},
                        {"text": "1 heure", "isCorrect": False},
                        {"text": "10 minutes", "isCorrect": False},
                        {"text": "7 jours", "isCorrect": False}
                    ],
                    "correction": "Il faut laisser le temps à la colle de faire sa prise hydraulique ou son séchage. Marcher trop tôt risque de déplacer les carreaux ou de créer des désaffleurs."
                },
                {
                    "questionNumber": 40,
                    "question": "Les systèmes de nivellement à cadrans ou coins (croisillons auto-nivelants) servent à :",
                    "answerOptions": [
                        {"text": "Ajuster parfaitement la planéité entre deux carreaux voisins", "isCorrect": True},
                        {"text": "Remplacer la colle", "isCorrect": False},
                        {"text": "Éviter de faire des joints", "isCorrect": False},
                        {"text": "Mesurer l'humidité", "isCorrect": False}
                    ],
                    "correction": "En serrant le système, on tire le carreau le plus bas vers le haut pour l'aligner avec son voisin, éliminant ainsi les désaffleurs pendant le séchage."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : PRÉPARATION ET CHAPE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : PRÉPARATION ET CHAPE (Questions 41 à 60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "À quoi sert principalement un ragréage autolissant ?",
                    "answerOptions": [
                        {"text": "À obtenir une surface parfaitement plane et lisse avant la pose", "isCorrect": True},
                        {"text": "À isoler thermiquement le sol", "isCorrect": False},
                        {"text": "À boucher les trous profonds de plus de 5 cm", "isCorrect": False},
                        {"text": "À faire l'étanchéité", "isCorrect": False}
                    ],
                    "correction": "Il s'applique sur une primaire, coule tout seul et se lisse pour rattraper les défauts de 3 à 10 mm généralement."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est l'épaisseur minimale recommandée pour une chape ciment adhérente ?",
                    "answerOptions": [
                        {"text": "4 cm", "isCorrect": True},
                        {"text": "5 mm", "isCorrect": False},
                        {"text": "1 cm", "isCorrect": False},
                        {"text": "20 cm", "isCorrect": False}
                    ],
                    "correction": "En dessous de cette épaisseur, le mortier n'a pas assez de corps, il sèche trop vite, 'brûle' et s'effrite ou se décolle."
                },
                {
                    "questionNumber": 43,
                    "question": "La désolidarisation sous chape (film polyane) sert à :",
                    "answerOptions": [
                        {"text": "Rendre la chape indépendante du support pour éviter la transmission des fissures", "isCorrect": True},
                        {"text": "Coller la chape au béton", "isCorrect": False},
                        {"text": "Faire des économies de ciment", "isCorrect": False},
                        {"text": "Empêcher la chape de sécher", "isCorrect": False}
                    ],
                    "correction": "La chape 'flotte' sur le film de désolidarisation, ce qui lui permet de bouger (retrait) sans être contrainte par les mouvements de la dalle porteuse."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le rôle du treillis soudé (grillage) dans une chape ?",
                    "answerOptions": [
                        {"text": "Limiter la fissuration due au retrait du mortier", "isCorrect": True},
                        {"text": "Chauffer le sol par conduction électrique", "isCorrect": False},
                        {"text": "Faire barrière aux insectes", "isCorrect": False},
                        {"text": "Remplacer le ciment", "isCorrect": False}
                    ],
                    "correction": "Il sert d'armature. Il est indispensable dans les chapes flottantes (sur isolant) ou désolidarisées pour maintenir la cohésion de l'ouvrage."
                },
                {
                    "questionNumber": 45,
                    "question": "La bande périphérique en mousse bleue de 5mm sert à :",
                    "answerOptions": [
                        {"text": "Désolidariser la chape des murs verticaux (joint de dilatation périphérique)", "isCorrect": True},
                        {"text": "Décorer le bas des murs avant la plinthe", "isCorrect": False},
                        {"text": "Empêcher les insectes de passer", "isCorrect": False},
                        {"text": "Isoler phoniquement le plafond", "isCorrect": False}
                    ],
                    "correction": "Sans cette bande, la chape en dilatant pousserait contre les murs, risquant de fissurer ou de soulever le sol."
                },
                {
                    "questionNumber": 46,
                    "question": "Avant de coller sur un ancien carrelage, quelle préparation est cruciale ?",
                    "answerOptions": [
                        {"text": "Dégraisser, poncer (griffer) et appliquer un primaire d'accrochage", "isCorrect": True},
                        {"text": "Juste passer un coup de balai", "isCorrect": False},
                        {"text": "Mouiller abondamment le sol", "isCorrect": False},
                        {"text": "Mettre une couche de ciment pur", "isCorrect": False}
                    ],
                    "correction": "L'émail de l'ancien carrelage est lisse et non poreux. Il faut créer une accroche mécanique et chimique pour que la nouvelle colle tienne."
                },
                {
                    "questionNumber": 47,
                    "question": "Sur une terrasse extérieure, la 'forme de pente' est destinée à :",
                    "answerOptions": [
                        {"text": "Évacuer les eaux de pluie vers l'extérieur ou les siphons", "isCorrect": True},
                        {"text": "Faire joli", "isCorrect": False},
                        {"text": "Empêcher de marcher", "isCorrect": False},
                        {"text": "Renforcer la dalle", "isCorrect": False}
                    ],
                    "correction": "Une terrasse plate retient l'eau (flaques), ce qui favorise les infiltrations, la mousse et le gel. Une pente de 1,5% est un minimum."
                },
                {
                    "questionNumber": 48,
                    "question": "Le dosage standard en ciment pour une chape traditionnelle est d'environ :",
                    "answerOptions": [
                        {"text": "350 kg de ciment par mètre cube de sable", "isCorrect": True},
                        {"text": "100 kg / m3", "isCorrect": False},
                        {"text": "800 kg / m3", "isCorrect": False},
                        {"text": "50 kg / m3", "isCorrect": False}
                    ],
                    "correction": "Un dosage correct assure la dureté. Trop maigre, la chape s'effrite ('chape brûlée'). Trop gras, elle fissure beaucoup (retrait excessif)."
                },
                {
                    "questionNumber": 49,
                    "question": "La laitance de ciment qui remonte en surface de la chape doit être :",
                    "answerOptions": [
                        {"text": "Éliminée par ponçage ou brossage avant le collage", "isCorrect": True},
                        {"text": "Conservée car elle protège la chape", "isCorrect": False},
                        {"text": "Peinte pour la cacher", "isCorrect": False},
                        {"text": "Mouillée tous les jours", "isCorrect": False}
                    ],
                    "correction": "C'est une pellicule fine et poudreuse sans résistance. Si on colle dessus, la colle arrache la laitance et le carreau se décolle."
                },
                {
                    "questionNumber": 50,
                    "question": "Le primaire 'bouche-pores' est spécifiquement utile pour :",
                    "answerOptions": [
                        {"text": "Les supports très absorbants (plâtre, béton cellulaire)", "isCorrect": True},
                        {"text": "Les supports bloqués (verre, métal)", "isCorrect": False},
                        {"text": "Les supports humides", "isCorrect": False},
                        {"text": "Les supports gras", "isCorrect": False}
                    ],
                    "correction": "Il sature la porosité du support. Sans lui, le support 'boit' l'eau de la colle instantanément, empêchant sa prise correcte (colle grillée)."
                },
                {
                    "questionNumber": 51,
                    "question": "Le SEL (Système d'Étanchéité Liquide) s'applique :",
                    "answerOptions": [
                        {"text": "Sous le carrelage, en plusieurs couches croisées", "isCorrect": True},
                        {"text": "Sur le carrelage pour le protéger", "isCorrect": False},
                        {"text": "Sous la chape béton", "isCorrect": False},
                        {"text": "Uniquement dans les angles", "isCorrect": False}
                    ],
                    "correction": "C'est une résine qui forme une membrane caoutchouteuse continue et étanche, obligatoire dans les douches à l'italienne."
                },
                {
                    "questionNumber": 52,
                    "question": "Le ravoirage est une couche maigre destinée à :",
                    "answerOptions": [
                        {"text": "Noyer les gaines techniques (plomberie, électricité) pour retrouver un sol plat", "isCorrect": True},
                        {"text": "Coller le carrelage", "isCorrect": False},
                        {"text": "Faire la finition décorative", "isCorrect": False},
                        {"text": "Remplacer l'isolant", "isCorrect": False}
                    ],
                    "correction": "Il permet d'obtenir une surface plane au-dessus des tuyaux pour ensuite poser l'isolant ou la chape proprement."
                },
                {
                    "questionNumber": 53,
                    "question": "Le test d'adhérence par 'sonnage' consiste à :",
                    "answerOptions": [
                        {"text": "Frapper le sol avec une tige métallique pour écouter si ça sonne 'creux'", "isCorrect": True},
                        {"text": "Utiliser un sonar", "isCorrect": False},
                        {"text": "Écouter le bruit des pas", "isCorrect": False},
                        {"text": "Crier fort", "isCorrect": False}
                    ],
                    "correction": "Un son creux indique que la chape est décollée de la dalle ou que le carreau est décollé de la chape (défaut d'adhérence)."
                },
                {
                    "questionNumber": 54,
                    "question": "Le sable utilisé pour le mortier de chape doit être :",
                    "answerOptions": [
                        {"text": "Lavé et exempt d'impuretés (argile, matières organiques)", "isCorrect": True},
                        {"text": "Du sable de plage non rincé", "isCorrect": False},
                        {"text": "De la terre végétale", "isCorrect": False},
                        {"text": "Des gravats broyés", "isCorrect": False}
                    ],
                    "correction": "L'argile ou le sel empêchent la prise correcte du ciment et fragilisent la structure du mortier."
                },
                {
                    "questionNumber": 55,
                    "question": "Le délai de séchage théorique d'une chape ciment est de :",
                    "answerOptions": [
                        {"text": "1 semaine par centimètre d'épaisseur", "isCorrect": True},
                        {"text": "24 heures pour toute l'épaisseur", "isCorrect": False},
                        {"text": "1 heure par centimètre", "isCorrect": False},
                        {"text": "6 mois minimum", "isCorrect": False}
                    ],
                    "correction": "C'est une règle empirique. Recouvrir une chape trop humide enferme l'eau, ce qui peut provoquer des désordres chimiques ou des décollements."
                },
                {
                    "questionNumber": 56,
                    "question": "Une natte de drainage (type Ditra-Drain) en extérieur se place :",
                    "answerOptions": [
                        {"text": "Sous le carrelage, au-dessus de la forme de pente étanchée", "isCorrect": True},
                        {"text": "Sous la dalle béton", "isCorrect": False},
                        {"text": "Au-dessus du carrelage", "isCorrect": False},
                        {"text": "Dans le jardin", "isCorrect": False}
                    ],
                    "correction": "Elle permet à l'eau qui traverse les joints de circuler et de s'évacuer sans stagner sous le carreau, évitant les sinistres liés au gel."
                },
                {
                    "questionNumber": 57,
                    "question": "Un joint de dilatation du bâtiment (gros œuvre) doit être :",
                    "answerOptions": [
                        {"text": "Répercuté à l'identique dans la chape et le carrelage", "isCorrect": True},
                        {"text": "Comblé avec du béton pour le bloquer", "isCorrect": False},
                        {"text": "Recouvert par un carreau entier", "isCorrect": False},
                        {"text": "Ignoré s'il est petit", "isCorrect": False}
                    ],
                    "correction": "C'est une coupure structurelle qui bouge. Si on le bloque ('ponter le joint'), le carrelage cassera net à cet endroit."
                },
                {
                    "questionNumber": 58,
                    "question": "L'Avis Technique (ATec) d'un produit est délivré par :",
                    "answerOptions": [
                        {"text": "Le CSTB (Centre Scientifique et Technique du Bâtiment)", "isCorrect": True},
                        {"text": "Le fabricant lui-même", "isCorrect": False},
                        {"text": "Le client final", "isCorrect": False},
                        {"text": "L'architecte", "isCorrect": False}
                    ],
                    "correction": "C'est le document officiel qui valide l'aptitude à l'emploi d'un produit. Il est indispensable pour être couvert par les assurances décennales."
                },
                {
                    "questionNumber": 59,
                    "question": "Pour tirer une chape de niveau, le carreleur réalise d'abord :",
                    "answerOptions": [
                        {"text": "Des 'nus' ou bandes de guides en mortier", "isCorrect": True},
                        {"text": "Des trous", "isCorrect": False},
                        {"text": "Des dessins au sol", "isCorrect": False},
                        {"text": "Une prière", "isCorrect": False}
                    ],
                    "correction": "Ces bandes servent de rails sur lesquels la règle va glisser pour araser le mortier parfaitement plan."
                },
                {
                    "questionNumber": 60,
                    "question": "Sur un support bois, l'utilisation d'une natte de désolidarisation est :",
                    "answerOptions": [
                        {"text": "Fortement recommandée voire obligatoire selon le format", "isCorrect": True},
                        {"text": "Interdite", "isCorrect": False},
                        {"text": "Inutile si la colle est forte", "isCorrect": False},
                        {"text": "Dangereuse", "isCorrect": False}
                    ],
                    "correction": "Le bois gonfle et bouge. La natte permet de dissocier les mouvements du support bois de ceux du carrelage rigide, évitant la casse."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : MOSAÏQUE ET FINITIONS (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : MOSAÏQUE ET FINITIONS (Questions 61 à 80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "La pose de mosaïque 'sur papier' (technique belle face) implique que :",
                    "answerOptions": [
                        {"text": "Le papier est collé sur la face visible et doit être retiré après la pose", "isCorrect": True},
                        {"text": "Le papier est au dos et reste noyé dans la colle", "isCorrect": False},
                        {"text": "Le papier sert de joint", "isCorrect": False},
                        {"text": "Le papier est décoratif et reste visible", "isCorrect": False}
                    ],
                    "correction": "Cette technique permet de voir l'alignement, mais demande une étape supplémentaire : mouiller le papier pour le décoller une fois la colle prise, avant de jointoyer."
                },
                {
                    "questionNumber": 62,
                    "question": "Le joint Époxy est particulièrement recommandé pour :",
                    "answerOptions": [
                        {"text": "Les locaux nécessitant une hygiène parfaite et une résistance chimique (cuisines pro, piscines)", "isCorrect": True},
                        {"text": "Les chambres à coucher", "isCorrect": False},
                        {"text": "Les plafonds", "isCorrect": False},
                        {"text": "Les plinthes bois", "isCorrect": False}
                    ],
                    "correction": "Contrairement au joint ciment, l'époxy n'est pas poreux, ne tache pas, ne s'effrite pas et résiste aux acides de nettoyage puissants."
                },
                {
                    "questionNumber": 63,
                    "question": "Le produit utilisé pour enlever le voile de ciment après jointoiement est :",
                    "answerOptions": [
                        {"text": "Un nettoyant acide (désincrustant)", "isCorrect": True},
                        {"text": "De l'eau de Javel pure", "isCorrect": False},
                        {"text": "Du liquide vaisselle", "isCorrect": False},
                        {"text": "De l'huile de lin", "isCorrect": False}
                    ],
                    "correction": "Le ciment étant basique (alcalin), seul un acide peut dissoudre les résidus. Il faut utiliser des acides tamponnés pour ne pas attaquer le joint lui-même."
                },
                {
                    "questionNumber": 64,
                    "question": "La 'Zag-Zag' est une pince spécifique pour :",
                    "answerOptions": [
                        {"text": "Tailler les tesselles de mosaïque (pâte de verre, émaux)", "isCorrect": True},
                        {"text": "Couper les carreaux de 60x60", "isCorrect": False},
                        {"text": "Couper les fils électriques", "isCorrect": False},
                        {"text": "Arracher les clous", "isCorrect": False}
                    ],
                    "correction": "Équipée de molettes en carbure, elle permet de 'croquer' le verre avec précision pour ajuster les formes des tesselles."
                },
                {
                    "questionNumber": 65,
                    "question": "L'étape de l'émulsion lors du jointoiement consiste à :",
                    "answerOptions": [
                        {"text": "Passer une éponge humide en mouvements circulaires pour lisser et fermer le joint", "isCorrect": True},
                        {"text": "Mélanger la poudre avec de l'eau", "isCorrect": False},
                        {"text": "Gratter le joint sec avec un couteau", "isCorrect": False},
                        {"text": "Appliquer un vernis", "isCorrect": False}
                    ],
                    "correction": "C'est l'étape de finition qui donne l'aspect lisse et régulier au joint tout en nettoyant le surplus sur les carreaux."
                },
                {
                    "questionNumber": 66,
                    "question": "Pourquoi utilise-t-on souvent une colle blanche pour la pâte de verre ?",
                    "answerOptions": [
                        {"text": "Pour ne pas altérer la couleur des tesselles par transparence", "isCorrect": True},
                        {"text": "Parce qu'elle est moins chère", "isCorrect": False},
                        {"text": "Parce qu'elle sèche plus vite", "isCorrect": False},
                        {"text": "Pour faire joli derrière", "isCorrect": False}
                    ],
                    "correction": "La pâte de verre est translucide. Une colle grise assombrirait le rendu final et ternirait l'éclat de la mosaïque."
                },
                {
                    "questionNumber": 67,
                    "question": "L'Opus Incertum est une technique de pose utilisant :",
                    "answerOptions": [
                        {"text": "Des morceaux cassés de formes irrégulières assemblés comme un puzzle", "isCorrect": True},
                        {"text": "Des carreaux carrés posés droit", "isCorrect": False},
                        {"text": "Des carreaux rectangulaires en chevron", "isCorrect": False},
                        {"text": "Des ronds parfaits", "isCorrect": False}
                    ],
                    "correction": "Incertum signifie incertain. On assemble les morceaux (souvent du marbre cassé ou du carrelage) de manière aléatoire en gérant l'espacement des joints."
                },
                {
                    "questionNumber": 68,
                    "question": "Pour lisser un joint silicone proprement, on utilise :",
                    "answerOptions": [
                        {"text": "Un outil trempé dans de l'eau savonneuse (produit lissant)", "isCorrect": True},
                        {"text": "De l'huile", "isCorrect": False},
                        {"text": "De la poussière", "isCorrect": False},
                        {"text": "Un chiffon sec", "isCorrect": False}
                    ],
                    "correction": "Le savon empêche le silicone (qui est très collant) d'adhérer au doigt ou à la spatule de lissage."
                },
                {
                    "questionNumber": 69,
                    "question": "En mosaïque, comment appelle-t-on les petits éléments qui composent l'ouvrage ?",
                    "answerOptions": [
                        {"text": "Les tesselles", "isCorrect": True},
                        {"text": "Les tuiles", "isCorrect": False},
                        {"text": "Les gravats", "isCorrect": False},
                        {"text": "Les pixels", "isCorrect": False}
                    ],
                    "correction": "Elles peuvent être en marbre, pierre, verre, céramique ou or. Leur taille varie généralement de quelques millimètres à 2 cm."
                },
                {
                    "questionNumber": 70,
                    "question": "La barbotine de jointoiement traditionnelle s'applique :",
                    "answerOptions": [
                        {"text": "À la raclette en caoutchouc en diagonale des joints", "isCorrect": True},
                        {"text": "Au pinceau fin", "isCorrect": False},
                        {"text": "Au rouleau à peinture", "isCorrect": False},
                        {"text": "À la truelle en fer", "isCorrect": False}
                    ],
                    "correction": "Le mouvement diagonal évite que l'outil ne rentre dans le joint et ne le creuse. La raclette souple permet de bien faire pénétrer la pâte au fond."
                },
                {
                    "questionNumber": 71,
                    "question": "Un joint large 'rustique' (plus de 10mm) nécessite l'ajout de :",
                    "answerOptions": [
                        {"text": "Sable dans le mélange pour limiter le retrait", "isCorrect": True},
                        {"text": "Plus d'eau", "isCorrect": False},
                        {"text": "Plâtre", "isCorrect": False},
                        {"text": "Colorant", "isCorrect": False}
                    ],
                    "correction": "Un ciment pur fissurerait en séchant sur une telle largeur. Le sable (charge) apporte la stabilité dimensionnelle au mortier de joint."
                },
                {
                    "questionNumber": 72,
                    "question": "Peut-on appliquer un nouveau joint silicone sur un ancien joint moisi ?",
                    "answerOptions": [
                        {"text": "Non, il faut retirer totalement l'ancien et dégraisser", "isCorrect": True},
                        {"text": "Oui, ça couvre bien", "isCorrect": False},
                        {"text": "Oui, si on met beaucoup de produit", "isCorrect": False},
                        {"text": "Oui, si on chauffe", "isCorrect": False}
                    ],
                    "correction": "Le silicone n'adhère pas sur du silicone réticulé. De plus, la moisissure reviendrait très vite par dessous."
                },
                {
                    "questionNumber": 73,
                    "question": "L'Andamento en mosaïque désigne :",
                    "answerOptions": [
                        {"text": "Le rythme, le flux et la direction des lignes de tesselles", "isCorrect": True},
                        {"text": "Le type de colle", "isCorrect": False},
                        {"text": "La couleur du joint", "isCorrect": False},
                        {"text": "L'outil de coupe", "isCorrect": False}
                    ],
                    "correction": "C'est la 'signature' du mosaïste. La manière dont les lignes de tesselles suivent les formes du dessin donne le mouvement et la vie à l'œuvre."
                },
                {
                    "questionNumber": 74,
                    "question": "Lors du calepinage d'une rosace, on commence par :",
                    "answerOptions": [
                        {"text": "Le centre du motif", "isCorrect": True},
                        {"text": "La périphérie", "isCorrect": False},
                        {"text": "Le bas", "isCorrect": False},
                        {"text": "N'importe où", "isCorrect": False}
                    ],
                    "correction": "Pour garantir la symétrie parfaite du dessin, le point de départ est le centre géométrique."
                },
                {
                    "questionNumber": 75,
                    "question": "Un joint 'creusé' est souvent la conséquence :",
                    "answerOptions": [
                        {"text": "D'un nettoyage trop insistant avec une éponge trop mouillée", "isCorrect": True},
                        {"text": "D'un mélange trop sec", "isCorrect": False},
                        {"text": "D'un carreau trop dur", "isCorrect": False},
                        {"text": "D'une température trop froide", "isCorrect": False}
                    ],
                    "correction": "L'eau en excès délave le joint frais et emporte la matière, laissant le joint en retrait par rapport au bord du carreau."
                },
                {
                    "questionNumber": 76,
                    "question": "Avant de jointoyer des carreaux poreux (terre cuite), il faut :",
                    "answerOptions": [
                        {"text": "Appliquer un produit de pré-traitement (bouche-pores)", "isCorrect": True},
                        {"text": "Les mouiller à grande eau", "isCorrect": False},
                        {"text": "Les poncer", "isCorrect": False},
                        {"text": "Ne rien faire", "isCorrect": False}
                    ],
                    "correction": "Sans protection, les pigments du joint pénètrent irréversiblement dans les pores de la terre cuite, la tachant définitivement ('voile indélébile')."
                },
                {
                    "questionNumber": 77,
                    "question": "Le mastic Polyuréthane (PU) est utilisé pour :",
                    "answerOptions": [
                        {"text": "Les joints de dilatation et de fractionnement (joint souple)", "isCorrect": True},
                        {"text": "Coller les carreaux au sol", "isCorrect": False},
                        {"text": "Faire les joints de faïence classiques", "isCorrect": False},
                        {"text": "Lisser les murs", "isCorrect": False}
                    ],
                    "correction": "Il reste souple et élastique après séchage, ce qui lui permet d'absorber les mouvements sans se décoller, contrairement au joint ciment rigide."
                },
                {
                    "questionNumber": 78,
                    "question": "Pourquoi faut-il changer très souvent l'eau de rinçage lors du nettoyage des joints ?",
                    "answerOptions": [
                        {"text": "Pour éviter de redéposer un voile de ciment sur les carreaux", "isCorrect": True},
                        {"text": "Pour consommer de l'eau", "isCorrect": False},
                        {"text": "Pour se réchauffer les mains", "isCorrect": False},
                        {"text": "Pour faire mousser", "isCorrect": False}
                    ],
                    "correction": "Une eau chargée de ciment laisse des traces blanchâtres (spectres) en séchant sur le carrelage, difficiles à enlever ensuite."
                },
                {
                    "questionNumber": 79,
                    "question": "Le délai d'attente avant jointoiement après une pose collée est généralement de :",
                    "answerOptions": [
                        {"text": "24 heures", "isCorrect": True},
                        {"text": "1 heure", "isCorrect": False},
                        {"text": "5 minutes", "isCorrect": False},
                        {"text": "1 mois", "isCorrect": False}
                    ],
                    "correction": "Il faut laisser l'humidité de la colle s'évaporer par les joints ouverts. Si on ferme trop tôt, on risque des variations de couleur du joint (carbonatation)."
                },
                {
                    "questionNumber": 80,
                    "question": "La 'marteline' et le 'tranchet' sont des outils traditionnels pour :",
                    "answerOptions": [
                        {"text": "Couper le marbre et la pierre en mosaïque d'art", "isCorrect": True},
                        {"text": "Mélanger le béton", "isCorrect": False},
                        {"text": "Percer le carrelage", "isCorrect": False},
                        {"text": "Poncer le sol", "isCorrect": False}
                    ],
                    "correction": "Le tranchet est planté dans un billot, et la marteline frappe la pierre pour la fendre avec précision."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : SÉCURITÉ, PLAN ET CALCULS (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : SÉCURITÉ, PLAN ET CALCULS (Questions 81 à 100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la formule pour calculer la surface d'une pièce rectangulaire ?",
                    "answerOptions": [
                        {"text": "Longueur x Largeur", "isCorrect": True},
                        {"text": "(Longueur + Largeur) x 2", "isCorrect": False},
                        {"text": "Longueur + Largeur", "isCorrect": False},
                        {"text": "Longueur x 2", "isCorrect": False}
                    ],
                    "correction": "C'est la base du métré. Le résultat s'exprime en mètres carrés (m²)."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel Équipement de Protection Individuelle (EPI) prévient l'hygroma du genou ?",
                    "answerOptions": [
                        {"text": "Les genouillères", "isCorrect": True},
                        {"text": "Les chaussures de sécurité", "isCorrect": False},
                        {"text": "Le casque", "isCorrect": False},
                        {"text": "Les lunettes", "isCorrect": False}
                    ],
                    "correction": "Le carreleur passe sa vie à genoux. L'hygroma (boule de liquide synovial) est une maladie professionnelle fréquente qui s'évite par une protection adaptée."
                },
                {
                    "questionNumber": 83,
                    "question": "La règle du '3-4-5' (Théorème de Pythagore) est utilisée sur chantier pour :",
                    "answerOptions": [
                        {"text": "Vérifier ou tracer un angle droit parfait (l'équerre)", "isCorrect": True},
                        {"text": "Calculer une surface", "isCorrect": False},
                        {"text": "Mesurer une hauteur", "isCorrect": False},
                        {"text": "Vérifier l'horizontalité", "isCorrect": False}
                    ],
                    "correction": "Si on mesure 3m d'un côté et 4m de l'autre, la diagonale doit faire exactement 5m pour que l'angle soit à 90°."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle marge de sécurité (perte/coupes) ajoute-t-on généralement pour une pose droite ?",
                    "answerOptions": [
                        {"text": "5 % à 10 %", "isCorrect": True},
                        {"text": "0 %", "isCorrect": False},
                        {"text": "50 %", "isCorrect": False},
                        {"text": "1 %", "isCorrect": False}
                    ],
                    "correction": "Il faut prévoir les chutes liées aux coupes en périphérie et la casse éventuelle. En pose diagonale, on compte plutôt 10% à 15%."
                },
                {
                    "questionNumber": 85,
                    "question": "Le port d'un masque FFP2/FFP3 est recommandé lors :",
                    "answerOptions": [
                        {"text": "Du mélange des colles en poudre et de la découpe à sec", "isCorrect": True},
                        {"text": "De la pose des croisillons", "isCorrect": False},
                        {"text": "Du nettoyage à l'eau", "isCorrect": False},
                        {"text": "De la conduite du camion", "isCorrect": False}
                    ],
                    "correction": "Les poussières de ciment et de silice (céramique) sont très fines et nocives pour les voies respiratoires à long terme."
                },
                {
                    "questionNumber": 86,
                    "question": "Sur un plan d'architecte, que signifie l'échelle 1/50 ?",
                    "answerOptions": [
                        {"text": "1 cm sur le plan représente 50 cm dans la réalité", "isCorrect": True},
                        {"text": "1 cm sur le plan représente 1 mètre", "isCorrect": False},
                        {"text": "Le dessin est 50 fois plus grand que la réalité", "isCorrect": False},
                        {"text": "50 cm sur le plan représente 1 cm réel", "isCorrect": False}
                    ],
                    "correction": "C'est une échelle de réduction. Pour avoir la dimension réelle, on multiplie la mesure du plan par 50."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la bonne posture pour soulever un sac de colle de 25 kg ?",
                    "answerOptions": [
                        {"text": "Dos droit, jambes fléchies, charge collée au corps", "isCorrect": True},
                        {"text": "Jambes tendues, dos courbé en avant", "isCorrect": False},
                        {"text": "Porter à bout de bras loin du corps", "isCorrect": False},
                        {"text": "Soulever par à-coups brusques", "isCorrect": False}
                    ],
                    "correction": "Cette technique utilise la force des cuisses et protège la colonne vertébrale, prévenant les lombalgies et hernies discales."
                },
                {
                    "questionNumber": 88,
                    "question": "À quoi correspond le 'Trait de niveau' tracé par le maçon sur les murs (généralement à 1m) ?",
                    "answerOptions": [
                        {"text": "À une référence altimétrique commune pour tous les artisans", "isCorrect": True},
                        {"text": "À la hauteur du carrelage fini", "isCorrect": False},
                        {"text": "À la hauteur des plinthes", "isCorrect": False},
                        {"text": "À une décoration", "isCorrect": False}
                    ],
                    "correction": "Le carreleur mesure 1 mètre vers le bas depuis ce trait pour déterminer le niveau exact de son sol fini."
                },
                {
                    "questionNumber": 89,
                    "question": "Combien de carreaux de 30x30 cm (0,09 m²) faut-il théoriquement pour couvrir 1 m² ?",
                    "answerOptions": [
                        {"text": "11,11 carreaux (soit 12)", "isCorrect": True},
                        {"text": "9 carreaux", "isCorrect": False},
                        {"text": "100 carreaux", "isCorrect": False},
                        {"text": "3 carreaux", "isCorrect": False}
                    ],
                    "correction": "Calcul : 1 divisé par 0,09 = 11,11. On compte 12 carreaux pour couvrir 1m² et avoir un peu de marge."
                },
                {
                    "questionNumber": 90,
                    "question": "Les Fiches de Données de Sécurité (FDS) servent à :",
                    "answerOptions": [
                        {"text": "Connaître les risques chimiques d'un produit et les mesures de premiers secours", "isCorrect": True},
                        {"text": "Connaître le prix du produit", "isCorrect": False},
                        {"text": "Savoir comment poser le produit", "isCorrect": False},
                        {"text": "Faire la publicité du produit", "isCorrect": False}
                    ],
                    "correction": "Elles sont obligatoires sur le chantier pour tous les produits dangereux (colles, résines, nettoyants acides)."
                },
                {
                    "questionNumber": 91,
                    "question": "Où doit-on jeter les restes de produits chimiques (bidons de solvant, résine époxy) ?",
                    "answerOptions": [
                        {"text": "En déchetterie spécialisée (déchets dangereux)", "isCorrect": True},
                        {"text": "Dans la poubelle normale", "isCorrect": False},
                        {"text": "Dans les égouts", "isCorrect": False},
                        {"text": "Dans la nature", "isCorrect": False}
                    ],
                    "correction": "Ce sont des déchets polluants qui ne doivent pas être mélangés aux gravats inertes (céramique, béton)."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle est la surface à carreler d'une pièce faisant 4m de long sur 5m de large ?",
                    "answerOptions": [
                        {"text": "20 m²", "isCorrect": True},
                        {"text": "9 m²", "isCorrect": False},
                        {"text": "18 m²", "isCorrect": False},
                        {"text": "22 m²", "isCorrect": False}
                    ],
                    "correction": "4 x 5 = 20."
                },
                {
                    "questionNumber": 93,
                    "question": "Le cordeau à tracer (bleu) permet de :",
                    "answerOptions": [
                        {"text": "Matérialiser au sol des axes rectilignes sur de grandes longueurs", "isCorrect": True},
                        {"text": "Mesurer des distances", "isCorrect": False},
                        {"text": "Couper le carrelage", "isCorrect": False},
                        {"text": "Poncer la chape", "isCorrect": False}
                    ],
                    "correction": "On tend la ficelle poudrée et on la 'claque' pour imprimer une ligne bleue au sol, base du calepinage."
                },
                {
                    "questionNumber": 94,
                    "question": "Que faire en cas de projection de ciment ou de chaux dans les yeux ?",
                    "answerOptions": [
                        {"text": "Rincer abondamment à l'eau claire immédiatement et consulter", "isCorrect": True},
                        {"text": "Frotter les yeux", "isCorrect": False},
                        {"text": "Mettre un pansement", "isCorrect": False},
                        {"text": "Attendre le soir", "isCorrect": False}
                    ],
                    "correction": "Le ciment est basique (pH élevé) et provoque des brûlures chimiques graves à la cornée. Le rinçage immédiat est la seule action qui limite les dégâts."
                },
                {
                    "questionNumber": 95,
                    "question": "Si un paquet de carrelage couvre 1,5 m², combien de paquets faut-il pour 40 m² (sans marge) ?",
                    "answerOptions": [
                        {"text": "27 paquets", "isCorrect": True},
                        {"text": "26 paquets", "isCorrect": False},
                        {"text": "20 paquets", "isCorrect": False},
                        {"text": "30 paquets", "isCorrect": False}
                    ],
                    "correction": "40 / 1,5 = 26,66. Comme on ne vend pas de paquets ouverts, il faut arrondir à l'entier supérieur, soit 27."
                },
                {
                    "questionNumber": 96,
                    "question": "Travailler 'à l'avancement' signifie :",
                    "answerOptions": [
                        {"text": "Progresser en marchant sur le support brut et non sur le carrelage frais", "isCorrect": True},
                        {"text": "Marcher sur le carrelage qu'on vient de poser", "isCorrect": False},
                        {"text": "Commencer par la porte", "isCorrect": False},
                        {"text": "Aller très vite", "isCorrect": False}
                    ],
                    "correction": "Le carreleur est face à son travail et recule vers la sortie. Cela évite d'abîmer la planéité des carreaux fraîchement posés."
                },
                {
                    "questionNumber": 97,
                    "question": "Un aspirateur de classe M est obligatoire sur chantier pour :",
                    "answerOptions": [
                        {"text": "Aspirer les poussières nocives (minérales, bois) avec une filtration adaptée", "isCorrect": True},
                        {"text": "Aspirer l'eau", "isCorrect": False},
                        {"text": "Nettoyer les bureaux", "isCorrect": False},
                        {"text": "Faire moins de bruit", "isCorrect": False}
                    ],
                    "correction": "Les aspirateurs ménagers rejettent les poussières fines dangereuses dans l'air. La classe M (Moyenne) garantit la capture des particules respirables."
                },
                {
                    "questionNumber": 98,
                    "question": "Le niveau à bulle permet de contrôler :",
                    "answerOptions": [
                        {"text": "L'horizontalité et la verticalité", "isCorrect": True},
                        {"text": "La longueur", "isCorrect": False},
                        {"text": "L'angle à 45°", "isCorrect": False},
                        {"text": "La température", "isCorrect": False}
                    ],
                    "correction": "C'est l'outil de contrôle permanent du carreleur. La bulle doit être centrée entre les deux traits."
                },
                {
                    "questionNumber": 99,
                    "question": "Le calcul du périmètre d'une pièce sert à commander :",
                    "answerOptions": [
                        {"text": "Les plinthes", "isCorrect": True},
                        {"text": "La colle", "isCorrect": False},
                        {"text": "Le carrelage de sol", "isCorrect": False},
                        {"text": "Le primaire", "isCorrect": False}
                    ],
                    "correction": "Périmètre = (Longueur + Largeur) x 2. Il faut ensuite déduire la largeur des portes pour connaître le métré linéaire de plinthes."
                },
                {
                    "questionNumber": 100,
                    "question": "Pourquoi doit-on utiliser un disjoncteur différentiel 30mA avec une scie à eau ?",
                    "answerOptions": [
                        {"text": "Pour couper le courant instantanément en cas de fuite d'électricité (protection des personnes)", "isCorrect": True},
                        {"text": "Pour économiser l'électricité", "isCorrect": False},
                        {"text": "Pour que la machine tourne plus vite", "isCorrect": False},
                        {"text": "Pour empêcher la machine de chauffer", "isCorrect": False}
                    ],
                    "correction": "L'eau et l'électricité créent un risque mortel d'électrocution. Le 30mA détecte la moindre fuite de courant vers la terre (et donc potentiellement à travers le corps humain) et disjoncte."
                }
            ]
        }
    }
}