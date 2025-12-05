# Fichier : quiz_cap_menuisier_installateur_100.py

quiz_data = {
    "title": "Quiz CAP Menuisier Installateur : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : PRISE DE MESURES, TRAÇAGE ET LECTURE DE PLANS (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Mesures, Traçage et Lecture de Plans (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Qu'est-ce que la **Cote de Réservation** (ou Tableau) lors de la pose d'une menuiserie extérieure ?",
                    "answerOptions": [
                        {"text": "La dimension finale du dormant.", "isCorrect": False},
                        {"text": "La dimension de l'ouverture brute dans la maçonnerie, avant l'installation du dormant.", "isCorrect": True},
                        {"text": "La dimension du vitrage.", "isCorrect": False},
                        {"text": "L'épaisseur du mur.", "isCorrect": False}
                    ],
                    "correction": "La **Cote de Réservation** (hauteur et largeur du tableau) est la dimension initiale à prendre. Elle sert à calculer les dimensions du dormant en soustrayant le jeu de pose."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel instrument de mesure permet de contrôler l'**Aplomb** d'un montant de dormant (sa parfaite verticalité) ?",
                    "answerOptions": [
                        {"text": "Le Niveau à bulle.", "isCorrect": False},
                        {"text": "Le Mètre ruban.", "isCorrect": False},
                        {"text": "Le Fil à plomb ou le Niveau laser.", "isCorrect": True},
                        {"text": "La Fausse équerre.", "isCorrect": False}
                    ],
                    "correction": "L'**Aplomb** garantit la verticalité, essentielle pour le bon fonctionnement des ouvrants. Le niveau sert à vérifier l'horizontalité."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment appelle-t-on le jeu (espace) laissé entre le dormant d'une fenêtre et la maçonnerie, nécessaire à la pose, au calage et à l'étanchéité ?",
                    "answerOptions": [
                        {"text": "L'Écart de cote.", "isCorrect": False},
                        {"text": "La Feuillure.", "isCorrect": False},
                        {"text": "Le Jeu de pose (ou Jour).", "isCorrect": True},
                        {"text": "La Traverse.", "isCorrect": False}
                    ],
                    "correction": "Le **Jeu de pose** (généralement quelques millimètres de chaque côté) est ensuite rempli par de la mousse polyuréthane ou du mastic de calfeutrement."
                },
                {
                    "questionNumber": 4,
                    "question": "Que représente le sigle **NFP** sur un plan de construction ou d'agencement ?",
                    "answerOptions": [
                        {"text": "Niveau de Finition Parfaite.", "isCorrect": False},
                        {"text": "Niveau du Fil du Plancher (repère horizontal de référence pour la pose).", "isCorrect": True},
                        {"text": "Norme Française des Portes.", "isCorrect": False},
                        {"text": "Nu de Façade Principale.", "isCorrect": False}
                    ],
                    "correction": "Le **NFP** est le niveau de référence sur un chantier, à partir duquel toutes les hauteurs sont cotées."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel outil permet de vérifier l'équerrage d'une baie existante, surtout si les angles sont douteux ?",
                    "answerOptions": [
                        {"text": "Le Mètre laser.", "isCorrect": False},
                        {"text": "Le Test de la diagonale (mesurer les deux diagonales qui doivent être égales si l'angle est droit).", "isCorrect": True},
                        {"text": "La Règle de maçon.", "isCorrect": False},
                        {"text": "Le Trusquin.", "isCorrect": False}
                    ],
                    "correction": "La vérification des **diagonales** est une méthode fiable pour s'assurer que l'ouverture est d'équerre."
                },
                {
                    "questionNumber": 6,
                    "question": "Dans un plan d'agencement, à quoi sert le **Plan d'implantation** ?",
                    "answerOptions": [
                        {"text": "Déterminer le prix de vente.", "isCorrect": False},
                        {"text": "Indiquer la position précise (cotes par rapport aux murs) des meubles, cloisons ou menuiseries à installer.", "isCorrect": True},
                        {"text": "Mesurer l'épaisseur des panneaux.", "isCorrect": False},
                        {"text": "Choisir la couleur.", "isCorrect": False}
                    ],
                    "correction": "Le **Plan d'implantation** est essentiel pour le travail sur site (chantier)."
                },
                {
                    "questionNumber": 7,
                    "question": "Qu'est-ce que le **Nu Extérieur** d'une menuiserie posée ?",
                    "answerOptions": [
                        {"text": "La face intérieure visible.", "isCorrect": False},
                        {"text": "Le plan de référence de la face extérieure du dormant, souvent aligné sur la façade finie.", "isCorrect": True},
                        {"text": "La dimension de la réservation.", "isCorrect": False},
                        {"text": "Le vitrage.", "isCorrect": False}
                    ],
                    "correction": "Le **Nu Extérieur** est crucial en isolation thermique et pour le drainage de l'eau."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la tolérance (marge d'erreur maximale) généralement admise pour l'équerrage d'un ouvrant avant la pose ?",
                    "answerOptions": [
                        {"text": "Plus de 5 mm.", "isCorrect": False},
                        {"text": "Environ 1 à 2 mm maximum (la précision est essentielle).", "isCorrect": True},
                        {"text": "1 cm.", "isCorrect": False},
                        {"text": "Aucune tolérance.", "isCorrect": False}
                    ],
                    "correction": "En menuiserie, la précision est au millimètre près. Une erreur de quelques millimètres entraîne un mauvais fonctionnement des ouvrants."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est l'outil utilisé pour prendre des mesures sur des grandes longueurs et vérifier la planéité des murs avant l'agencement ?",
                    "answerOptions": [
                        {"text": "Le Compas.", "isCorrect": False},
                        {"text": "La Règle de maçon (ou Règle de 2m) et/ou la Règle à niveau.", "isCorrect": True},
                        {"text": "Le Pied à coulisse.", "isCorrect": False},
                        {"text": "Le Crayon de menuisier.", "isCorrect": False}
                    ],
                    "correction": "La **Règle de maçon** est indispensable pour vérifier la rectitude des surfaces."
                },
                {
                    "questionNumber": 10,
                    "question": "Sur un plan d'exécution, que représente une **ligne en trait mixte fin** (un trait, un point, un trait...) ?",
                    "answerOptions": [
                        {"text": "Une arête visible.", "isCorrect": False},
                        {"text": "L'axe de symétrie ou l'axe de rotation d'une pièce.", "isCorrect": True},
                        {"text": "Une arête cachée.", "isCorrect": False},
                        {"text": "Une ligne de coupe.", "isCorrect": False}
                    ],
                    "correction": "Le trait mixte fin est utilisé pour le **centrage** et la symétrie des éléments."
                },
                {
                    "questionNumber": 11,
                    "question": "Lors du métré pour une rénovation, quelle est la cote prise en premier dans une baie existante ?",
                    "answerOptions": [
                        {"text": "La cote la plus petite (hauteur et largeur).", "isCorrect": True},
                        {"text": "La cote la plus grande.", "isCorrect": False},
                        {"text": "La cote moyenne.", "isCorrect": False},
                        {"text": "L'épaisseur du mur.", "isCorrect": False}
                    ],
                    "correction": "On prend toujours la **cote la plus petite** pour s'assurer que le nouveau dormant passera dans l'ouverture, en conservant le jeu de pose."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le risque si le dormant d'une porte intérieure n'est pas parfaitement d'aplomb ?",
                    "answerOptions": [
                        {"text": "L'ouvrant se déformera.", "isCorrect": False},
                        {"text": "La porte aura tendance à s'ouvrir ou se fermer seule (effet de gravité) et la serrure ne fonctionnera pas correctement.", "isCorrect": True},
                        {"text": "Le mur va s'écrouler.", "isCorrect": False},
                        {"text": "Le verre va casser.", "isCorrect": False}
                    ],
                    "correction": "L'**Aplomb** est essentiel pour le bon fonctionnement des ouvrants. C'est le premier contrôle à faire."
                },
                {
                    "questionNumber": 13,
                    "question": "Comment appelle-t-on le plan qui donne les détails de fabrication d'un assemblage ou d'une quincaillerie (souvent à l'échelle 1/1 ou 1/5) ?",
                    "answerOptions": [
                        {"text": "Le Plan d'ensemble.", "isCorrect": False},
                        {"text": "Le Plan de détail.", "isCorrect": True},
                        {"text": "Le Schéma électrique.", "isCorrect": False},
                        {"text": "Le Croquis.", "isCorrect": False}
                    ],
                    "correction": "Le **Plan de détail** est utilisé pour le traçage et la vérification des usinages lors de la pose."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le nom de l'outil qui projette des lignes laser verticales et horizontales pour faciliter le traçage sur de grandes surfaces (murs, sols) ?",
                    "answerOptions": [
                        {"text": "Le Niveau à bulle.", "isCorrect": False},
                        {"text": "Le Télémètre.", "isCorrect": False},
                        {"text": "Le Niveau laser (ou Laser multiligne).", "isCorrect": True},
                        {"text": "Le Compas.", "isCorrect": False}
                    ],
                    "correction": "Le **Niveau laser** est l'outil moderne pour l'implantation rapide et précise sur chantier."
                },
                {
                    "questionNumber": 15,
                    "question": "Que doit-on vérifier en priorité sur un appui de fenêtre maçonné avant de poser le dormant ?",
                    "answerOptions": [
                        {"text": "Sa couleur.", "isCorrect": False},
                        {"text": "Sa planéité, son niveau et la présence/l'état du rejingot.", "isCorrect": True},
                        {"text": "Sa hauteur.", "isCorrect": False},
                        {"text": "Sa température.", "isCorrect": False}
                    ],
                    "correction": "L'**appui** doit être plan et légèrement incliné vers l'extérieur pour l'évacuation de l'eau. Le **Rejingot** est indispensable."
                },
                {
                    "questionNumber": 16,
                    "question": "Que signifie la cotation **+/- 0.00** sur un plan de niveau ?",
                    "answerOptions": [
                        {"text": "Le niveau zéro du sol extérieur.", "isCorrect": False},
                        {"text": "Le niveau de référence (souvent le sol fini du rez-de-chaussée).", "isCorrect": True},
                        {"text": "La hauteur totale du bâtiment.", "isCorrect": False},
                        {"text": "La température.", "isCorrect": False}
                    ],
                    "correction": "Le niveau **+/- 0.00** est la référence altimétrique du projet."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel outil est nécessaire pour marquer des lignes de coupe précises sur des panneaux (ex: pour l'agencement) ?",
                    "answerOptions": [
                        {"text": "Le Mètre ruban.", "isCorrect": False},
                        {"text": "Le Traîneau de coupe (ou Règle de guidage de scie circulaire).", "isCorrect": True},
                        {"text": "La Défonceuse.", "isCorrect": False},
                        {"text": "Le Pinceau.", "isCorrect": False}
                    ],
                    "correction": "La **Règle de guidage** permet de réaliser des coupes droites et précises sur de grands panneaux sur le chantier."
                },
                {
                    "questionNumber": 18,
                    "question": "Que signifie l'annotation **'Nu Fin. Int.'** sur un plan ?",
                    "answerOptions": [
                        {"text": "Niveau de Fond Intérieur.", "isCorrect": False},
                        {"text": "Nu Fini Intérieur (surface du mur une fois le revêtement intérieur posé).", "isCorrect": True},
                        {"text": "Nomenclature des Fixations Intérieures.", "isCorrect": False},
                        {"text": "Nettoyage Fin Intérieur.", "isCorrect": False}
                    ],
                    "correction": "Le **Nu Fini Intérieur** est la référence pour la pose en applique ou pour les agencements."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le risque de prendre les cotes uniquement en haut et en bas d'une baie existante ?",
                    "answerOptions": [
                        {"text": "Le bois risque de se déformer.", "isCorrect": False},
                        {"text": "Le mur peut avoir un ventre (bombement) au milieu, empêchant l'installation du dormant (d'où l'importance de mesurer au moins 3 points en hauteur et 3 points en largeur).", "isCorrect": True},
                        {"text": "La couleur sera faussée.", "isCorrect": False},
                        {"text": "Le niveau ne sera pas bon.", "isCorrect": False}
                    ],
                    "correction": "Les murs anciens sont rarement droits. Il faut toujours mesurer aux **trois points** (haut, milieu, bas/droite, centre, gauche)."
                },
                {
                    "questionNumber": 20,
                    "question": "Comment appelle-t-on la méthode de mesure qui utilise les coordonnées d'un point par rapport à un angle de référence (le point 0,0) ?",
                    "answerOptions": [
                        {"text": "Le Mesurage en diagonale.", "isCorrect": False},
                        {"text": "Le Mesurage par triangulation (ou Mesurage en coordonnées).", "isCorrect": True},
                        {"text": "Le Mesurage au mètre ruban.", "isCorrect": False},
                        {"text": "Le Mesurage du niveau.", "isCorrect": False}
                    ],
                    "correction": "La **triangulation** est essentielle pour l'implantation de grands agencements ou de cloisons complexes."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : POSE DE MENUISERIES EXTÉRIEURES (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Pose de Menuiseries Extérieures (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel type de pose est celui où le dormant de la fenêtre est fixé au nu extérieur du mur (recouvrant le mur sur les côtés, souvent avec un tapée d'isolation) ?",
                    "answerOptions": [
                        {"text": "La Pose en Tunnel.", "isCorrect": False},
                        {"text": "La Pose en Applique.", "isCorrect": True},
                        {"text": "La Pose en Feuillure.", "isCorrect": False},
                        {"text": "La Pose sur bâti existant.", "isCorrect": False}
                    ],
                    "correction": "La **Pose en Applique** est la plus courante en construction neuve avec Isolation Thermique par l'Intérieur (ITI)."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est le rôle de la **Mousse Polyuréthane Expansive (PU)** en pose de menuiserie extérieure ?",
                    "answerOptions": [
                        {"text": "Le collage définitif de la fenêtre.", "isCorrect": False},
                        {"text": "Le remplissage du jeu de pose pour l'isolation thermique, phonique et la tenue mécanique (en complément des fixations).", "isCorrect": True},
                        {"text": "L'étanchéité à l'eau.", "isCorrect": False},
                        {"text": "Le calage.", "isCorrect": False}
                    ],
                    "correction": "La **Mousse PU** assure l'étanchéité à l'air et le support mécanique, mais ne remplace pas le calage (coins de bois) ni les fixations mécaniques."
                },
                {
                    "questionNumber": 23,
                    "question": "Dans le cas d'une **Pose en Rénovation** sur bâti existant, quel est le principal avantage ?",
                    "answerOptions": [
                        {"text": "C'est la méthode la moins chère.", "isCorrect": False},
                        {"text": "Elle permet de conserver le dormant existant et évite les travaux de maçonnerie de reprise (plus rapide et moins salissante).", "isCorrect": True},
                        {"text": "La fenêtre est plus grande.", "isCorrect": False},
                        {"text": "La fenêtre est plus isolante.", "isCorrect": False}
                    ],
                    "correction": "La **Pose en Rénovation** est rapide, mais réduit la surface vitrée (le dormant neuf est plus petit que l'ancien)."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle du **Rejingot** dans une fenêtre (appui maçonné) ?",
                    "answerOptions": [
                        {"text": "Empêcher le vent de passer.", "isCorrect": False},
                        {"text": "Casser le filet d'eau et éviter l'infiltration entre le bas du dormant et l'appui maçonné.", "isCorrect": True},
                        {"text": "Porter le dormant.", "isCorrect": False},
                        {"text": "Tenir le verre.", "isCorrect": False}
                    ],
                    "correction": "Le **Rejingot** (partie relevée à l'extrémité de l'appui) est un élément essentiel de l'étanchéité à l'eau."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel type de cheville doit-on utiliser pour fixer un dormant dans un mur en **Béton Banché** ?",
                    "answerOptions": [
                        {"text": "Une cheville à expansion légère.", "isCorrect": False},
                        {"text": "Une vis à béton (ou vis de scellement) sans cheville plastique.", "isCorrect": True},
                        {"text": "Un simple clou.", "isCorrect": False},
                        {"text": "Une cheville Molly.", "isCorrect": False}
                    ],
                    "correction": "La **Vis à béton** (ou vis de scellement) est une solution de fixation très performante et rapide en maçonnerie pleine."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le rôle des **Cales de vitrage** lors de la mise en place d'un ouvrant ?",
                    "answerOptions": [
                        {"text": "Remplir l'espace.", "isCorrect": False},
                        {"text": "Assurer le jeu d'usage et supporter le poids du vitrage pour éviter que l'ouvrant ne 's'affaisse' (calage en L ou en T).", "isCorrect": True},
                        {"text": "Coller le vitrage.", "isCorrect": False},
                        {"text": "Améliorer l'esthétique.", "isCorrect": False}
                    ],
                    "correction": "Le **Calage** est une opération technique qui conditionne la durabilité et le bon fonctionnement de l'ouvrant (pas de frottement)."
                },
                {
                    "questionNumber": 27,
                    "question": "Après le calage et la fixation, quelle est la première vérification à effectuer sur le dormant avant la mise en place des ouvrants ?",
                    "answerOptions": [
                        {"text": "La couleur de la menuiserie.", "isCorrect": False},
                        {"text": "Le niveau et l'aplomb du dormant, ainsi que l'équerrage (avec la vérification des diagonales).", "isCorrect": True},
                        {"text": "Le prix.", "isCorrect": False},
                        {"text": "L'épaisseur du bois.", "isCorrect": False}
                    ],
                    "correction": "Le **dormant** est la référence fixe ; s'il n'est pas posé parfaitement d'équerre, l'ouvrant ne fonctionnera jamais correctement."
                },
                {
                    "questionNumber": 28,
                    "question": "Qu'est-ce qu'une **Tapée d'isolation** dans une menuiserie extérieure ?",
                    "answerOptions": [
                        {"text": "Un défaut du bois.", "isCorrect": False},
                        {"text": "Une pièce de bois ou de PVC ajoutée au dormant pour compenser l'épaisseur de l'isolant intérieur ou extérieur.", "isCorrect": True},
                        {"text": "Un élément de sécurité anti-effraction.", "isCorrect": False},
                        {"text": "Le joint d'étanchéité.", "isCorrect": False}
                    ],
                    "correction": "La **Tapée** permet d'aligner la menuiserie sur le nu de l'isolant (ITI ou ITE)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est l'outil utilisé pour appliquer un mastic d'étanchéité périphérique (silicone, acrylique, etc.) ?",
                    "answerOptions": [
                        {"text": "Le Pinceau.", "isCorrect": False},
                        {"text": "Le Pistolet extrudeur (manuel ou pneumatique).", "isCorrect": True},
                        {"text": "La Brosse.", "isCorrect": False},
                        {"text": "La Spatule.", "isCorrect": False}
                    ],
                    "correction": "Le **Pistolet extrudeur** permet une application régulière et précise du joint (cordon de mastic)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le risque de calfeutrer uniquement avec du mastic ou du silicone sans utiliser de fond de joint ?",
                    "answerOptions": [
                        {"text": "Le mastic risque de couler.", "isCorrect": False},
                        {"text": "Le mastic ne peut pas étirer (dilatation) et risque de se fissurer rapidement. Le fond de joint optimise l'élasticité et la durabilité du joint.", "isCorrect": True},
                        {"text": "Le mastic sera trop dur.", "isCorrect": False},
                        {"text": "Le mastic sera trop cher.", "isCorrect": False}
                    ],
                    "correction": "Le **Fond de joint** (mousse, cordon) est essentiel pour assurer une bonne géométrie et élasticité du mastic."
                },
                {
                    "questionNumber": 31,
                    "question": "Que signifie la pose **en Feuillure** ?",
                    "answerOptions": [
                        {"text": "La pose où le dormant est fixé contre le mur.", "isCorrect": False},
                        {"text": "La pose où le dormant s'insère dans une entaille (ou 'retrait') réservée dans la maçonnerie du tableau.", "isCorrect": True},
                        {"text": "La pose sur bâti existant.", "isCorrect": False},
                        {"text": "La pose sur une cloison sèche.", "isCorrect": False}
                    ],
                    "correction": "La pose **en Feuillure** est fréquente en construction traditionnelle et assure une excellente étanchéité (recouvrement)."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'élément qui permet de relier deux menuiseries (ex : une fenêtre et une porte-fenêtre) côte à côte ?",
                    "answerOptions": [
                        {"text": "Le Jet d'eau.", "isCorrect": False},
                        {"text": "Le Profilé de jonction (ou Coupleur).", "isCorrect": True},
                        {"text": "La Parclose.", "isCorrect": False},
                        {"text": "Le Scellement chimique.", "isCorrect": False}
                    ],
                    "correction": "Le **Coupleur** assure la liaison et l'étanchéité entre les dormants."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le risque de poser un dormant de fenêtre sans prévoir de **bande d'étanchéité** ou de mastic sous la traverse basse ?",
                    "answerOptions": [
                        {"text": "Un défaut d'aplomb.", "isCorrect": False},
                        {"text": "Un pont thermique et une infiltration d'eau par capillarité ou pression sous le dormant, provoquant des dégâts des eaux.", "isCorrect": True},
                        {"text": "La fenêtre sera trop lourde.", "isCorrect": False},
                        {"text": "Le vitrage va s'ouvrir.", "isCorrect": False}
                    ],
                    "correction": "L'étanchéité de la traverse basse (avec bande d'étanchéité, compriband ou mastic) est cruciale."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel outil est le plus adapté pour découper précisément un profilé PVC ou Aluminium (par exemple, des couvre-joints) sur le chantier ?",
                    "answerOptions": [
                        {"text": "Le Ciseau à bois.", "isCorrect": False},
                        {"text": "La Scie à onglet (manuelle ou électrique).", "isCorrect": True},
                        {"text": "La Scie à ruban.", "isCorrect": False},
                        {"text": "La Défonceuse.", "isCorrect": False}
                    ],
                    "correction": "La **Scie à onglet** assure des coupes nettes et précises (souvent à 45°) pour les finitions."
                },
                {
                    "questionNumber": 35,
                    "question": "Pour quelle raison doit-on obligatoirement utiliser des **vis inoxydables** pour la fixation de menuiseries en bord de mer ?",
                    "answerOptions": [
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Le sel et l'humidité accélèrent la corrosion, ce qui pourrait faire rouiller et casser les fixations (utilisation d'inox A4 ou V4A).", "isCorrect": True},
                        {"text": "Elles sont plus faciles à visser.", "isCorrect": False},
                        {"text": "Elles sont moins chères.", "isCorrect": False}
                    ],
                    "correction": "L'acier galvanisé simple n'est pas suffisant dans les environnements très corrosifs (marins)."
                },
                {
                    "questionNumber": 36,
                    "question": "Comment appelle-t-on le procédé qui permet de reprendre un jeu important (supérieur à 2 cm) entre le dormant et la maçonnerie ?",
                    "answerOptions": [
                        {"text": "Le calfeutrement au silicone.", "isCorrect": False},
                        {"text": "Le Maçonnage d'un rejingot ou le rebouchage (avec mortier ou cales de bois scellées).", "isCorrect": True},
                        {"text": "L'utilisation de mousse PU.", "isCorrect": False},
                        {"text": "L'ajout d'une parclose.", "isCorrect": False}
                    ],
                    "correction": "Les jeux importants nécessitent une **reprise maçonnerie** car les mousses et mastics ne suffisent pas à assurer la stabilité et l'isolation."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est le rôle du **Compriband (ou Mousse imprégnée)** dans le système d'étanchéité des fenêtres ?",
                    "answerOptions": [
                        {"text": "Servir de calage.", "isCorrect": False},
                        {"text": "Bande d'étanchéité pré-comprimée qui assure l'étanchéité à l'air (côté intérieur) et/ou l'étanchéité à l'eau (côté extérieur).", "isCorrect": True},
                        {"text": "Fixer le dormant.", "isCorrect": False},
                        {"text": "Assurer la finition esthétique.", "isCorrect": False}
                    ],
                    "correction": "Le **Compriband** (bande de mousse) se dilate progressivement pour remplir l'espace et assurer l'étanchéité. Il est souvent utilisé en pose 'i-window' ou '3 cordons'."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel élément de la quincaillerie permet le réglage latéral, vertical et en profondeur d'un ouvrant sur son dormant ?",
                    "answerOptions": [
                        {"text": "Le Jet d'eau.", "isCorrect": False},
                        {"text": "La Crémone.", "isCorrect": False},
                        {"text": "La Paumelle ou Fiche réglable (3D).", "isCorrect": True},
                        {"text": "La Parclose.", "isCorrect": False}
                    ],
                    "correction": "Les **Paumelles 3D** sont essentielles pour un ajustement parfait de la porte ou de la fenêtre après la pose."
                },
                {
                    "questionNumber": 39,
                    "question": "Lors du transport d'une grande fenêtre, quelle est la position idéale pour éviter la déformation du dormant ?",
                    "answerOptions": [
                        {"text": "À plat sur le plateau.", "isCorrect": False},
                        {"text": "Verticalement, sur un chevalet ou un support adapté, bien calée pour éviter les vibrations et le vrillage.", "isCorrect": True},
                        {"text": "L'ouvrant ouvert.", "isCorrect": False},
                        {"text": "Couchée sur le trottoir.", "isCorrect": False}
                    ],
                    "correction": "Le transport **vertical** (à chant) est obligatoire pour les grandes menuiseries afin de garantir la conservation de l'équerrage."
                },
                {
                    "questionNumber": 40,
                    "question": "Dans le cas d'une porte-fenêtre, quel est le risque de ne pas sceller correctement la pièce d'appui (seuil) au sol ?",
                    "answerOptions": [
                        {"text": "L'ouvrant va frotter en haut.", "isCorrect": False},
                        {"text": "Infiltration d'eau par le bas et mauvais fonctionnement du drainage ou de la quincaillerie (seuil déformé).", "isCorrect": True},
                        {"text": "Le bois sera trop lourd.", "isCorrect": False},
                        {"text": "Le niveau sera faux.", "isCorrect": False}
                    ],
                    "correction": "Le **seuil** doit être parfaitement scellé et étanche au niveau du sol."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : POSE DE MENUISERIES INTÉRIEURES ET AGENCEMENT (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Pose de Menuiseries Intérieures et Agencement (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Qu'est-ce qu'une **Huisserie** (ou Bloc-porte) ?",
                    "answerOptions": [
                        {"text": "L'ouvrant seul.", "isCorrect": False},
                        {"text": "L'ensemble composé du dormant (cadre fixe) et de l'ouvrant (porte mobile), livré prêt à poser.", "isCorrect": True},
                        {"text": "La serrure.", "isCorrect": False},
                        {"text": "Le mur.", "isCorrect": False}
                    ],
                    "correction": "L'**Huisserie** est le terme désignant le bloc-porte prêt à être scellé ou fixé."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est l'outil indispensable pour percer des trous dans une cloison en Plaque de Plâtre (Placo) pour la fixation d'un meuble lourd ?",
                    "answerOptions": [
                        {"text": "Un clou.", "isCorrect": False},
                        {"text": "Une cheville Molly (ou Cheville à expansion pour matériaux creux).", "isCorrect": True},
                        {"text": "Une vis à bois.", "isCorrect": False},
                        {"text": "Une cheville à béton.", "isCorrect": False}
                    ],
                    "correction": "La **Cheville Molly** ou équivalent est conçue pour répartir la charge dans la cloison creuse."
                },
                {
                    "questionNumber": 43,
                    "question": "Lors de la pose d'un plancher flottant (parquet), quel est le rôle des **cales de dilatation** ?",
                    "answerOptions": [
                        {"text": "Assurer la décoration.", "isCorrect": False},
                        {"text": "Laisser un espace périphérique (le long des murs) pour permettre au bois de se dilater sans se soulever (tuilage).", "isCorrect": True},
                        {"text": "Coller le parquet.", "isCorrect": False},
                        {"text": "Rendre le parquet plus dur.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint de dilatation** est fondamental pour la durabilité de tout revêtement en bois ou stratifié (environ 8 à 10 mm)."
                },
                {
                    "questionNumber": 44,
                    "question": "Comment appelle-t-on le revêtement décoratif qui masque le joint de dilatation entre le parquet et le mur ?",
                    "answerOptions": [
                        {"text": "Le Plinthe.", "isCorrect": True},
                        {"text": "La Contre-marche.", "isCorrect": False},
                        {"text": "Le Solin.", "isCorrect": False},
                        {"text": "Le Chambranle.", "isCorrect": False}
                    ],
                    "correction": "La **Plinthe** est un élément de finition esthétique qui recouvre le jeu de dilatation."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le risque de fixer les couvre-joints d'une huisserie directement sur la maçonnerie, sans prévoir de jeu ?",
                    "answerOptions": [
                        {"text": "Les couvre-joints risquent de se fendre ou de se déformer sous l'effet de l'humidité ou des variations thermiques.", "isCorrect": True},
                        {"text": "Le dormant va s'ouvrir.", "isCorrect": False},
                        {"text": "La porte va couler.", "isCorrect": False},
                        {"text": "La finition sera trop lisse.", "isCorrect": False}
                    ],
                    "correction": "Le bois bouge. Il faut laisser un **léger jeu** sur les éléments de finition (moulures, couvre-joints)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel outil est le plus adapté pour découper précisément le bas d'un dormant (avant scellement) pour l'adapter au sol (ex: passage de gaines, défaut de niveau) ?",
                    "answerOptions": [
                        {"text": "La Scie sauteuse.", "isCorrect": False},
                        {"text": "La Scie plongeante ou la Scie sabre.", "isCorrect": True},
                        {"text": "La Défonceuse.", "isCorrect": False},
                        {"text": "La Ponceuse.", "isCorrect": False}
                    ],
                    "correction": "La **Scie plongeante** (avec rail) offre une coupe précise. La scie sabre est utile pour les coupes d'ajustement grossières."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on l'élément horizontal d'un escalier sur lequel on pose le pied ?",
                    "answerOptions": [
                        {"text": "La Contre-marche.", "isCorrect": False},
                        {"text": "La Marche (ou GIRON).", "isCorrect": True},
                        {"text": "La Limon.", "isCorrect": False},
                        {"text": "Le Poteau.", "isCorrect": False}
                    ],
                    "correction": "Le **Giron** est la profondeur de la marche, la **Contre-marche** est la hauteur de la marche."
                },
                {
                    "questionNumber": 48,
                    "question": "Lors de l'agencement d'un meuble, quel est l'élément qui est utilisé pour régler la hauteur et l'aplomb du caisson par rapport au sol (souvent en plastique) ?",
                    "answerOptions": [
                        {"text": "La Plinthe.", "isCorrect": False},
                        {"text": "Le Pied (ou Vérin) réglable.", "isCorrect": True},
                        {"text": "La Coulisse de tiroir.", "isCorrect": False},
                        {"text": "Le Dos de meuble.", "isCorrect": False}
                    ],
                    "correction": "Le **Pied réglable** permet d'ajuster l'horizontalité du meuble (surtout les meubles de cuisine et de salle de bain)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le rôle du **Barre de seuil** (ou seuil de liaison) ?",
                    "answerOptions": [
                        {"text": "Servir de marche.", "isCorrect": False},
                        {"text": "Assurer la transition entre deux revêtements de sol différents (parquet/carrelage) et masquer le joint de dilatation.", "isCorrect": True},
                        {"text": "Empêcher la porte de fermer.", "isCorrect": False},
                        {"text": "Porter la cloison.", "isCorrect": False}
                    ],
                    "correction": "La **Barre de seuil** est un élément de finition, essentiel pour l'esthétique et la sécurité (anti-trébuchement)."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment appelle-t-on la fixation utilisée pour sceller définitivement un dormant de porte intérieure dans la maçonnerie après son calage ?",
                    "answerOptions": [
                        {"text": "Le Clou.", "isCorrect": False},
                        {"text": "Le Scellement chimique ou le Scellement au plâtre/ciment.", "isCorrect": True},
                        {"text": "Le Scotch.", "isCorrect": False},
                        {"text": "La Cheville Molly.", "isCorrect": False}
                    ],
                    "correction": "Le **Scellement** est une fixation lourde et définitive, différente de la fixation mécanique par vis/cheville."
                },
                {
                    "questionNumber": 51,
                    "question": "Dans le cas d'une porte coulissante, quel est l'élément essentiel à poser parfaitement de niveau pour garantir le bon fonctionnement ?",
                    "answerOptions": [
                        {"text": "La poignée.", "isCorrect": False},
                        {"text": "Le Rail de guidage supérieur (ou le Châssis pour les portes à galandage).", "isCorrect": True},
                        {"text": "La contre-marche.", "isCorrect": False},
                        {"text": "Le dormant.", "isCorrect": False}
                    ],
                    "correction": "Le **Rail de guidage** doit être parfaitement de niveau et d'aplomb pour que la porte coulisse sans effort et reste en place."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le risque de ne pas utiliser le bon type de vis pour la pose d'une quincaillerie (ex : charnière) dans un panneau Aggloméré ?",
                    "answerOptions": [
                        {"text": "La vis sera trop longue.", "isCorrect": False},
                        {"text": "L'arrachement de la vis du panneau, dû à la faible cohésion de l'Aggloméré (utilisation de vis spécifiques pour panneaux).", "isCorrect": True},
                        {"text": "La vis sera trop dure.", "isCorrect": False},
                        {"text": "Le bois sera trop chaud.", "isCorrect": False}
                    ],
                    "correction": "Les vis pour panneaux dérivés sont souvent à double filetage ou spécifiques pour maximiser la tenue (ex : vis Euro pour charnières de cuisine)."
                },
                {
                    "questionNumber": 53,
                    "question": "Comment appelle-t-on l'élément de menuiserie intérieure qui assure la finition au niveau du plafond ?",
                    "answerOptions": [
                        {"text": "La Plinthe.", "isCorrect": False},
                        {"text": "La Corniche ou la Gorge.", "isCorrect": True},
                        {"text": "Le Chambranle.", "isCorrect": False},
                        {"text": "Le Limon.", "isCorrect": False}
                    ],
                    "correction": "La **Corniche** est une moulure décorative installée en haut de l'agencement ou du mur."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le rôle du **Joint de compression** sur un dormant de porte ?",
                    "answerOptions": [
                        {"text": "Protéger le bois.", "isCorrect": False},
                        {"text": "Amortir la fermeture de l'ouvrant, améliorer l'isolation phonique et éviter le passage de l'air.", "isCorrect": True},
                        {"text": "Servir de décoration.", "isCorrect": False},
                        {"text": "Rendre la porte plus lourde.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint périphérique** est essentiel pour le confort acoustique et thermique (étanchéité à l'air)."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le nom de l'élément porteur d'un escalier, où s'encastrent les marches et les contremarches ?",
                    "answerOptions": [
                        {"text": "La Main courante.", "isCorrect": False},
                        {"text": "Le Limon (central ou latéral).", "isCorrect": True},
                        {"text": "Le Poteau de départ.", "isCorrect": False},
                        {"text": "Le Garde-corps.", "isCorrect": False}
                    ],
                    "correction": "Le **Limon** est la pièce inclinée qui reçoit les assemblages de l'escalier."
                },
                {
                    "questionNumber": 56,
                    "question": "Dans le cas d'une pose de porte en fin de chantier, pourquoi doit-on protéger le dormant ?",
                    "answerOptions": [
                        {"text": "Pour éviter les chocs, les rayures et les taches de peinture/enduit dues aux travaux de finition des autres corps d'état.", "isCorrect": True},
                        {"text": "Pour que la porte soit plus jolie.", "isCorrect": False},
                        {"text": "Pour qu'elle soit plus légère.", "isCorrect": False},
                        {"text": "Pour qu'elle soit plus dure.", "isCorrect": False}
                    ],
                    "correction": "La **Protection du dormant** (souvent avec du ruban adhésif ou des housses) est une précaution de fin de chantier pour garantir la qualité de la finition."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est le rôle du **Gâche** d'une serrure (partie métallique fixée sur le dormant) ?",
                    "answerOptions": [
                        {"text": "Contenir la clé.", "isCorrect": False},
                        {"text": "Recevoir le pêne (dormant et demi-tour) pour bloquer l'ouvrant dans sa position fermée.", "isCorrect": True},
                        {"text": "Servir de poignée.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité.", "isCorrect": False}
                    ],
                    "correction": "La **Gâche** est l'équivalent de la mortaise pour la serrure, fixée dans le dormant."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment appelle-t-on la méthode qui consiste à fixer le dormant d'une porte dans l'épaisseur d'une cloison sèche (Placo) ?",
                    "answerOptions": [
                        {"text": "La Pose en Applique.", "isCorrect": False},
                        {"text": "La Pose en Tunnel (ou en Encastrement).", "isCorrect": True},
                        {"text": "La Pose en Feuillure.", "isCorrect": False},
                        {"text": "La Pose en Rénovation.", "isCorrect": False}
                    ],
                    "correction": "La **Pose en Tunnel** est le cas standard pour les portes installées dans l'épaisseur des cloisons légères."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est l'élément qui permet de fixer une étagère lourdement chargée dans une maçonnerie creuse (brique, parpaing) ?",
                    "answerOptions": [
                        {"text": "Une cheville Molly.", "isCorrect": False},
                        {"text": "Le Scellement chimique (résine injectée) ou une cheville à expansion lourde.", "isCorrect": True},
                        {"text": "Un clou.", "isCorrect": False},
                        {"text": "De la colle vinylique.", "isCorrect": False}
                    ],
                    "correction": "Le **Scellement chimique** est la solution la plus fiable pour les charges lourdes (éléments de cuisine, bibliothèques) en matériaux creux ou pleins."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle du **Faux-cadre** (ou Pré-cadre) lors de la pose d'une menuiserie intérieure ?",
                    "answerOptions": [
                        {"text": "La fixation définitive.", "isCorrect": False},
                        {"text": "Le Faux-cadre est fixé à la maçonnerie, servant de référence stable et de support pour la fixation et le réglage du dormant définitif.", "isCorrect": True},
                        {"text": "L'étanchéité à l'air.", "isCorrect": False},
                        {"text": "Le calfeutrement.", "isCorrect": False}
                    ],
                    "correction": "Le **Faux-cadre** est souvent utilisé pour les portes palières ou les installations nécessitant une très grande précision."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : MATÉRIAUX, QUINCAILLERIE ET ÉTANCHÉITÉ (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Matériaux, Quincaillerie et Étanchéité (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel type de mastic (joint) est généralement utilisé pour l'étanchéité des vitrages et des joints très exposés à l'eau et aux UV ?",
                    "answerOptions": [
                        {"text": "Le Mastic acrylique.", "isCorrect": False},
                        {"text": "Le Mastic silicone neutre (ou le Mastic polyuréthane).", "isCorrect": True},
                        {"text": "Le Mastic plâtre.", "isCorrect": False},
                        {"text": "Le Mastic bitumineux.", "isCorrect": False}
                    ],
                    "correction": "Le **Silicone neutre** (ne dégage pas d'acide acétique) offre une très bonne résistance aux intempéries et une excellente élasticité."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la principale caractéristique de la **Cheville à frapper** ?",
                    "answerOptions": [
                        {"text": "Elle sert uniquement pour les charges légères.", "isCorrect": False},
                        {"text": "Elle permet une fixation rapide et traversante du dormant dans la maçonnerie (le clou est inséré en même temps que la cheville).", "isCorrect": True},
                        {"text": "Elle est démontable.", "isCorrect": False},
                        {"text": "Elle est utilisée pour le placo.", "isCorrect": False}
                    ],
                    "correction": "La **Cheville à frapper** est utilisée pour les fixations rapides et est plus difficile à démonter."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est le rôle de la **Visseuse à chocs** sur un chantier ?",
                    "answerOptions": [
                        {"text": "Percer le béton.", "isCorrect": False},
                        {"text": "Visser et dévisser rapidement et sans effort les vis longues et les tirefonds, même dans les bois durs (couple élevé et frappe tangentielle).", "isCorrect": True},
                        {"text": "Mélanger le ciment.", "isCorrect": False},
                        {"text": "Couper les chevrons.", "isCorrect": False}
                    ],
                    "correction": "La **Visseuse à chocs** (ou boulonneuse) est très performante pour la fixation lourde et répétitive."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel type de vitrage est obligatoire pour les portes-fenêtres ou les zones à risque de chute (sécurité des personnes) ?",
                    "answerOptions": [
                        {"text": "Le Simple vitrage.", "isCorrect": False},
                        {"text": "Le Vitrage de sécurité (Trempé ou Feuilleté).", "isCorrect": True},
                        {"text": "Le Double vitrage standard.", "isCorrect": False},
                        {"text": "Le Vitrage teinté.", "isCorrect": False}
                    ],
                    "correction": "Le **Vitrage de sécurité (Trempé ou Feuilleté)** est conçu pour ne pas blesser en cas de bris (éclatement en petits morceaux non coupants ou maintien des fragments)."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le matériau principal utilisé pour l'ossature des cloisons sèches (Placo) ?",
                    "answerOptions": [
                        {"text": "Le Bois massif.", "isCorrect": False},
                        {"text": "Le Profilé métallique (Rail et Montant en acier galvanisé).", "isCorrect": True},
                        {"text": "Le Béton armé.", "isCorrect": False},
                        {"text": "Le Verre.", "isCorrect": False}
                    ],
                    "correction": "Les **Rails et Montants** métalliques constituent l'ossature de base des cloisons sèches, avant le vissage du plâtre."
                },
                {
                    "questionNumber": 66,
                    "question": "Qu'est-ce qu'une **Liaison Étanchéité à l'Air (LEA)** ?",
                    "answerOptions": [
                        {"text": "Un type de colle.", "isCorrect": False},
                        {"text": "L'ensemble des produits (adhésifs, mastics, membranes) utilisés pour rendre la jonction entre le dormant et le mur étanche à l'air (critique pour la performance énergétique).", "isCorrect": True},
                        {"text": "Un raccord électrique.", "isCorrect": False},
                        {"text": "Un type de couverture.", "isCorrect": False}
                    ],
                    "correction": "La **LEA** est essentielle pour l'obtention des performances thermiques (RT2012/RE2020)."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la principale différence entre le **Mastic silicone** et le **Mastic acrylique** ?",
                    "answerOptions": [
                        {"text": "Le silicone est plus cher.", "isCorrect": False},
                        {"text": "Le silicone est étanche à l'eau et ne peut pas être peint. L'acrylique est un mastic de rebouchage/finition qui peut être peint, mais il résiste moins à l'eau.", "isCorrect": True},
                        {"text": "L'acrylique est plus lourd.", "isCorrect": False},
                        {"text": "Le silicone est plus facile à lisser.", "isCorrect": False}
                    ],
                    "correction": "Le **Silicone** est pour l'étanchéité (milieu humide), l'**Acrylique** pour la finition (milieu sec, intérieur)."
                },
                {
                    "questionNumber": 68,
                    "question": "Dans le cas d'une porte palière (entrée d'immeuble), quel type de serrure est le plus souvent utilisé pour la sécurité ?",
                    "answerOptions": [
                        {"text": "Une serrure à clé simple.", "isCorrect": False},
                        {"text": "Une Serrure de sécurité multipoints (3 ou 5 points minimum).", "isCorrect": True},
                        {"text": "Une simple targette.", "isCorrect": False},
                        {"text": "Une serrure décorative.", "isCorrect": False}
                    ],
                    "correction": "La **Serrure Multipoints** est la norme pour la protection anti-effraction."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le risque de percer un panneau mélaminé trop rapidement ou avec une mèche non adaptée ?",
                    "answerOptions": [
                        {"text": "Le panneau va prendre feu.", "isCorrect": False},
                        {"text": "L'éclatement du revêtement mélaminé sur la face de sortie (contre-parement).", "isCorrect": True},
                        {"text": "Le trou sera trop petit.", "isCorrect": False},
                        {"text": "Le perçage sera trop lent.", "isCorrect": False}
                    ],
                    "correction": "Il faut utiliser des **mèches affûtées** (ex : mèche à bois à centrer) et réduire la vitesse à la sortie pour éviter l'éclatement."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment appelle-t-on le produit qui, lorsqu'il est appliqué sur un mastic, permet d'améliorer son adhérence au support (maçonnerie, bois, etc.) ?",
                    "answerOptions": [
                        {"text": "Le Diluant.", "isCorrect": False},
                        {"text": "Le Primaire d'accrochage (ou Primer).", "isCorrect": True},
                        {"text": "Le Durcisseur.", "isCorrect": False},
                        {"text": "Le Solvant.", "isCorrect": False}
                    ],
                    "correction": "Le **Primaire d'accrochage** est essentiel pour garantir la durabilité du joint sur les supports poreux ou lisses."
                },
                {
                    "questionNumber": 71,
                    "question": "Qu'est-ce qu'une **Bavette (ou Pliage)** en menuiserie extérieure ?",
                    "answerOptions": [
                        {"text": "Un élément de calage.", "isCorrect": False},
                        {"text": "Une tôle (aluminium ou zinc) fixée sous la traverse basse pour évacuer l'eau (jet d'eau rapporté).", "isCorrect": True},
                        {"text": "Un type de joint.", "isCorrect": False},
                        {"text": "Une poignée.", "isCorrect": False}
                    ],
                    "correction": "La **Bavette** est un élément d'étanchéité complémentaire au rejingot."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le rôle de la **Fermeture à galandage** ?",
                    "answerOptions": [
                        {"text": "Fermer une porte battante.", "isCorrect": False},
                        {"text": "Permettre à l'ouvrant d'une porte coulissante de rentrer entièrement dans l'épaisseur du mur/de la cloison sèche.", "isCorrect": True},
                        {"text": "Fermer une fenêtre à projection.", "isCorrect": False},
                        {"text": "Fermer une fenêtre avec une crémone.", "isCorrect": False}
                    ],
                    "correction": "Le **Galandage** permet de gagner de la place en libérant le mur."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le type d'isolant le plus couramment utilisé dans les ossatures de cloisons et pour le calfeutrement (rouleaux souples) ?",
                    "answerOptions": [
                        {"text": "Le Béton cellulaire.", "isCorrect": False},
                        {"text": "La Laine minérale (Laine de verre ou Laine de roche).", "isCorrect": True},
                        {"text": "Le Bois massif.", "isCorrect": False},
                        {"text": "Le Polystyrène extrudé (XPS).", "isCorrect": False}
                    ],
                    "correction": "La **Laine minérale** est un bon isolant thermique et phonique, facile à poser entre les montants."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le danger principal du mastic silicone **acétoxy** ?",
                    "answerOptions": [
                        {"text": "Il est trop mou.", "isCorrect": False},
                        {"text": "Il dégage de l'acide acétique (odeur de vinaigre) qui peut corroder certains métaux et attaquer certains supports (marbre, bois, etc.).", "isCorrect": True},
                        {"text": "Il sèche trop vite.", "isCorrect": False},
                        {"text": "Il n'est pas étanche.", "isCorrect": False}
                    ],
                    "correction": "Le silicone **acétoxy** est réservé aux salles de bains et non adapté à la menuiserie extérieure (préférer le neutre)."
                },
                {
                    "questionNumber": 75,
                    "question": "Qu'est-ce qu'un **Chambranle** en menuiserie ?",
                    "answerOptions": [
                        {"text": "La serrure.", "isCorrect": False},
                        {"text": "La moulure (ou profilé) de finition qui masque la jonction entre l'huisserie de la porte et le mur intérieur.", "isCorrect": True},
                        {"text": "Le dormant.", "isCorrect": False},
                        {"text": "Le vitrage.", "isCorrect": False}
                    ],
                    "correction": "Le **Chambranle** est synonyme de couvre-joint sur une huisserie."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le risque de recouvrir une fissure murale avec de la peinture sans la traiter ?",
                    "answerOptions": [
                        {"text": "La peinture va s'éclaircir.", "isCorrect": False},
                        {"text": "La fissure réapparaîtra rapidement (un an ou moins). Il faut la gratter, injecter un mastic acrylique souple avant de peindre.", "isCorrect": True},
                        {"text": "Le mur va s'écrouler.", "isCorrect": False},
                        {"text": "La fissure va disparaître.", "isCorrect": False}
                    ],
                    "correction": "Les petites fissures doivent être traitées avec un **mastic acrylique** (si elles ne sont pas structurelles)."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est l'outil utilisé pour écarter (ou lever) les éléments lourds (ex : une porte ou un meuble) de quelques millimètres sans les endommager ?",
                    "answerOptions": [
                        {"text": "La Masse.", "isCorrect": False},
                        {"text": "Le Pied-de-biche (ou Levier à porte).", "isCorrect": True},
                        {"text": "La Visseuse.", "isCorrect": False},
                        {"text": "Le Mètre laser.", "isCorrect": False}
                    ],
                    "correction": "Le **Pied-de-biche** ou un levier spécialisé permet de positionner précisément les éléments lourds."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le rôle du **Joint néoprène** (ou EPDM) dans le calage de la porte ?",
                    "answerOptions": [
                        {"text": "La décoration.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité à l'air et à l'eau entre l'ouvrant et le dormant (il est comprimé lors de la fermeture).", "isCorrect": True},
                        {"text": "Le collage.", "isCorrect": False},
                        {"text": "L'amortissement.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint EPDM** est un joint de compression de haute qualité pour la performance des menuiseries."
                },
                {
                    "questionNumber": 79,
                    "question": "Lors de la pose d'un plancher bois, comment appelle-t-on les fixations qui permettent de visser le plancher sur des lambourdes (pièces de bois fixées au sol) ?",
                    "answerOptions": [
                        {"text": "Le Clou à tête plate.", "isCorrect": False},
                        {"text": "La Vis de plancher (souvent à double filetage) ou le Clou annelé.", "isCorrect": True},
                        {"text": "La Cheville Molly.", "isCorrect": False},
                        {"text": "La Vis à béton.", "isCorrect": False}
                    ],
                    "correction": "Les **Vis de plancher** spécifiques permettent une meilleure tenue et réduisent le grincement."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le rôle de la **Brosse métallique** avant l'application d'un produit de finition (lasure, peinture) sur un bois ancien ?",
                    "answerOptions": [
                        {"text": "Faire briller le bois.", "isCorrect": False},
                        {"text": "Éliminer les résidus de peinture ou de lasure écaillée, et préparer la surface pour une meilleure accroche (décapage mécanique).", "isCorrect": True},
                        {"text": "Réaliser des rainures.", "isCorrect": False},
                        {"text": "Mesurer le bois.", "isCorrect": False}
                    ],
                    "correction": "La **Brosse métallique** est utile pour le décapage de bois très anciens ou rustiques."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SÉCURITÉ, HYGIÈNE ET ENVIRONNEMENT DE CHANTIER (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Sécurité, Hygiène et Environnement de Chantier (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) obligatoire pour la manipulation de vitrages (portes-fenêtres, baies) ?",
                    "answerOptions": [
                        {"text": "Le Casque anti-bruit.", "isCorrect": False},
                        {"text": "Les Gants anti-coupure (anti-perforation) et les chaussures de sécurité (embout renforcé).", "isCorrect": True},
                        {"text": "Le Gilet jaune.", "isCorrect": False},
                        {"text": "Le Masque anti-poussière.", "isCorrect": False}
                    ],
                    "correction": "Les **Gants anti-coupure** sont essentiels pour manipuler les vitres sans danger."
                },
                {
                    "questionNumber": 82,
                    "question": "Avant de commencer à percer un mur, quelle vérification est indispensable pour prévenir les accidents ?",
                    "answerOptions": [
                        {"text": "La couleur du mur.", "isCorrect": False},
                        {"text": "La détection de gaines électriques ou de canalisations (eau, gaz) à l'aide d'un détecteur de matériaux.", "isCorrect": True},
                        {"text": "L'heure qu'il est.", "isCorrect": False},
                        {"text": "L'état du sol.", "isCorrect": False}
                    ],
                    "correction": "Le **Détecteur de matériaux** est crucial pour la sécurité (électrocution) et pour éviter les dégâts (eau, gaz)."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la règle d'or pour le travail en hauteur sur un escabeau (pose d'agencement) ?",
                    "answerOptions": [
                        {"text": "Travailler sur la dernière marche.", "isCorrect": False},
                        {"text": "Ne jamais travailler sur la ou les deux dernières marches et s'assurer que l'escabeau est stable (pattes en butée) et ses pieds à plat.", "isCorrect": True},
                        {"text": "Travailler les mains chargées.", "isCorrect": False},
                        {"text": "Bloquer les marches.", "isCorrect": False}
                    ],
                    "correction": "L'**Escabeau** est dangereux s'il n'est pas utilisé dans le respect des consignes (éviter la dernière marche)."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment doit être stocké le bois sur le chantier, notamment le bois massif ?",
                    "answerOptions": [
                        {"text": "Directement sur le sol humide.", "isCorrect": False},
                        {"text": "Horizontalement, sur des cales (lambourdes) pour éviter le contact avec le sol humide, et à l'abri des intempéries (déformations).", "isCorrect": True},
                        {"text": "Verticalement, sans support.", "isCorrect": False},
                        {"text": "En vrac.", "isCorrect": False}
                    ],
                    "correction": "Un **mauvais stockage** peut annuler le travail d'usinage (gonflement, tuilage)."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le risque lié à l'inhalation de la **poussière de bois exotique** ?",
                    "answerOptions": [
                        {"text": "Une simple irritation.", "isCorrect": False},
                        {"text": "Réactions allergiques, irritation des voies respiratoires, et risque cancérogène (notamment les essences de bois dur comme l'Iroko, le Chêne).", "isCorrect": True},
                        {"text": "Une surchauffe.", "isCorrect": False},
                        {"text": "Une chute.", "isCorrect": False}
                    ],
                    "correction": "Le port du **Masque FFP3** et un système d'aspiration efficace sont obligatoires pour l'usinage des bois exotiques (ou bois durs)."
                },
                {
                    "questionNumber": 86,
                    "question": "Que doit-on faire de tous les déchets de chantier (chutes de bois, emballages, mousse PU durcie) ?",
                    "answerOptions": [
                        {"text": "Les laisser sur place.", "isCorrect": False},
                        {"text": "Les trier et les stocker dans des bennes ou des sacs spécifiques (DIB - Déchets Industriels Banals / Bois / Gravats) pour le recyclage.", "isCorrect": True},
                        {"text": "Les brûler sur place.", "isCorrect": False},
                        {"text": "Les jeter dans une poubelle simple.", "isCorrect": False}
                    ],
                    "correction": "Le **Tri sélectif des déchets** est une obligation légale sur le chantier (gestion environnementale)."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment appelle-t-on le document qui synthétise les risques d'une intervention sur un site (ex : présence d'amiante, travail en hauteur) ?",
                    "answerOptions": [
                        {"text": "Le Plan de coupe.", "isCorrect": False},
                        {"text": "Le Plan de Prévention (ou Plan Particulier de Sécurité et de Protection de la Santé - PPSPS).", "isCorrect": True},
                        {"text": "Le Plan de masse.", "isCorrect": False},
                        {"text": "Le Bon de commande.", "isCorrect": False}
                    ],
                    "correction": "Le **Plan de Prévention / PPSPS** est fondamental pour la coordination des travaux et la sécurité sur les chantiers."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le risque de laisser traîner des câbles électriques (rallonges) au sol sur le chantier ?",
                    "answerOptions": [
                        {"text": "Le câble va s'éclaircir.", "isCorrect": False},
                        {"text": "Le risque de chute (trébuchement) et d'endommagement du câble (court-circuit).", "isCorrect": True},
                        {"text": "L'outil sera trop lourd.", "isCorrect": False},
                        {"text": "Le bois sera trop chaud.", "isCorrect": False}
                    ],
                    "correction": "Les **câbles** doivent être organisés et, si possible, suspendus pour éviter les accidents."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le rôle du **Masque à cartouche** (anti-gaz) lors de l'utilisation de colle PU, de peinture ou de produits de traitement du bois ?",
                    "answerOptions": [
                        {"text": "Protéger contre la poussière.", "isCorrect": False},
                        {"text": "Filtrer les vapeurs organiques toxiques (solvants, isocyanates de la PU) pour protéger les voies respiratoires.", "isCorrect": True},
                        {"text": "Protéger contre le bruit.", "isCorrect": False},
                        {"text": "Protéger contre les chocs.", "isCorrect": False}
                    ],
                    "correction": "Le **Masque à cartouche** est adapté aux travaux de finition impliquant des produits chimiques volatils."
                },
                {
                    "questionNumber": 90,
                    "question": "Pourquoi doit-on obligatoirement ventiler le local lors de l'utilisation de certains produits de finition (vernis polyuréthane, laque) ?",
                    "answerOptions": [
                        {"text": "Pour que la couleur soit plus belle.", "isCorrect": False},
                        {"text": "Pour accélérer le séchage et éviter l'accumulation de solvants dans l'air (risques d'intoxication, d'incendie et d'explosion).", "isCorrect": True},
                        {"text": "Pour faire baisser la température.", "isCorrect": False},
                        {"text": "Pour éliminer la poussière.", "isCorrect": False}
                    ],
                    "correction": "La **Ventilation** est un impératif de sécurité pour l'utilisateur et l'environnement de travail."
                },
                {
                    "questionNumber": 91,
                    "question": "Qu'est-ce qu'une **Fiche de Données de Sécurité (FDS)** ?",
                    "answerOptions": [
                        {"text": "Le mode d'emploi de la machine.", "isCorrect": False},
                        {"text": "Le document obligatoire qui fournit les informations sur les dangers d'un produit chimique (colle, solvant, etc.) et les mesures de protection à prendre (EPI).", "isCorrect": True},
                        {"text": "Le plan de l'entreprise.", "isCorrect": False},
                        {"text": "Le contrat de travail.", "isCorrect": False}
                    ],
                    "correction": "La **FDS** doit être consultée avant toute utilisation d'un produit dangereux."
                },
                {
                    "questionNumber": 92,
                    "question": "Que doit-on faire d'un ouvrant (porte ou fenêtre) lors de sa pose avant de le fixer sur le dormant ?",
                    "answerOptions": [
                        {"text": "Le coller.", "isCorrect": False},
                        {"text": "Le dégonder (retirer l'ouvrant du dormant) pour faciliter le calage, la fixation du dormant et réduire le poids à manipuler.", "isCorrect": True},
                        {"text": "Le peindre.", "isCorrect": False},
                        {"text": "Le déformer.", "isCorrect": False}
                    ],
                    "correction": "La **dégondage** est une opération de sécurité et de simplification de la pose."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le risque de travailler sur un sol graisseux ou glissant (à cause de la pluie ou de la sciure) ?",
                    "answerOptions": [
                        {"text": "La déformation du bois.", "isCorrect": False},
                        {"text": "Le risque de glissade et de chute de plain-pied, souvent aggravé par la manipulation de charges lourdes ou d'outils tranchants.", "isCorrect": True},
                        {"text": "La rouille.", "isCorrect": False},
                        {"text": "Le bruit.", "isCorrect": False}
                    ],
                    "correction": "La **Propreté et l'ordre** sont des éléments clés de la sécurité sur un chantier."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment doit-on manipuler une plaque de Placo ou un grand panneau de bois pour éviter les Troubles Musculo-Squelettiques (TMS) ?",
                    "answerOptions": [
                        {"text": "Le porter seul sur l'épaule.", "isCorrect": False},
                        {"text": "Être deux pour le porter et utiliser des chariots ou lève-panneaux adaptés, en gardant le dos droit.", "isCorrect": True},
                        {"text": "Le faire glisser sur le sol.", "isCorrect": False},
                        {"text": "Le jeter.", "isCorrect": False}
                    ],
                    "correction": "La **Manutention de charges lourdes** doit être adaptée (mécanique ou à deux personnes)."
                },
                {
                    "questionNumber": 95,
                    "question": "En cas de petite coupure superficielle sur le chantier, quelle est la première chose à faire ?",
                    "answerOptions": [
                        {"text": "Continuer de travailler.", "isCorrect": False},
                        {"text": "Nettoyer, désinfecter la plaie et appliquer un pansement (armoire à pharmacie/trousse de premiers secours).", "isCorrect": True},
                        {"text": "Demander au collègue de s'en occuper.", "isCorrect": False},
                        {"text": "Faire un pansement avec de la sciure.", "isCorrect": False}
                    ],
                    "correction": "Les **premiers secours** sont la base de l'hygiène et de la sécurité."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est le rôle du **Disjoncteur différentiel** sur une rallonge électrique de chantier ?",
                    "answerOptions": [
                        {"text": "Réguler la tension.", "isCorrect": False},
                        {"text": "Couper immédiatement le courant en cas de fuite de courant (ex : contact avec l'eau, court-circuit, électrocution), protégeant l'utilisateur.", "isCorrect": True},
                        {"text": "Empêcher le vol.", "isCorrect": False},
                        {"text": "Faire fonctionner la machine.", "isCorrect": False}
                    ],
                    "correction": "Le **Disjoncteur différentiel** est un élément de sécurité électrique vital, surtout dans un environnement humide."
                },
                {
                    "questionNumber": 97,
                    "question": "Que doit-on faire avant de démonter un dormant existant dans une rénovation ?",
                    "answerOptions": [
                        {"text": "Le peindre.", "isCorrect": False},
                        {"text": "S'assurer qu'aucune canalisation ou gaine n'est intégrée dans le dormant (et le déconnecter si besoin).", "isCorrect": True},
                        {"text": "Le coller.", "isCorrect": False},
                        {"text": "Le casser sans précaution.", "isCorrect": False}
                    ],
                    "correction": "Les **vérifications préalables** évitent les dégâts majeurs (électrocution, inondation, coupure de gaz)."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est l'ÉPI essentiel contre les projections de bois ou de poussière (sciage, ponçage, perçage) ?",
                    "answerOptions": [
                        {"text": "Le Gilet de sécurité.", "isCorrect": False},
                        {"text": "Les Lunettes de protection (ou Visière).", "isCorrect": True},
                        {"text": "Les Gants en tissu.", "isCorrect": False},
                        {"text": "La Casquette.", "isCorrect": False}
                    ],
                    "correction": "La **Protection oculaire** est obligatoire contre les projections (copeaux, poussières)."
                },
                {
                    "questionNumber": 99,
                    "question": "Qu'est-ce qu'un **Solin** en maçonnerie ou menuiserie extérieure ?",
                    "answerOptions": [
                        {"text": "Un type de cheville.", "isCorrect": False},
                        {"text": "Un revêtement (en zinc ou autre) ou un joint qui assure l'étanchéité d'un raccord entre deux matériaux (ex: mur et appui de fenêtre, ou mur et toiture).", "isCorrect": True},
                        {"text": "Un défaut du bois.", "isCorrect": False},
                        {"text": "Un type de dormant.", "isCorrect": False}
                    ],
                    "correction": "Le **Solin** est un élément d'étanchéité (souvent métallique) des jonctions complexes."
                },
                {
                    "questionNumber": 100,
                    "question": "Que doit-on impérativement faire avant de déconnecter une rallonge électrique portable ?",
                    "answerOptions": [
                        {"text": "Tirer sur le câble.", "isCorrect": False},
                        {"text": "Éteindre l'outil ou le coupe-circuit de la rallonge avant de débrancher la prise (éviter l'arc électrique).", "isCorrect": True},
                        {"text": "Laisser le courant.", "isCorrect": False},
                        {"text": "La rouler.", "isCorrect": False}
                    ],
                    "correction": "Il faut toujours **éteindre** l'appareil avant de le déconnecter."
                },
            ]
        }
    }
}

# Exemple d'accès aux données :
# print(quiz_data["title"])
# print(quiz_data["themes"][3]["name"])
# print(quiz_data["themes"][3]["questions"][4]["question"])
# print(quiz_data["themes"][3]["questions"][4]["answerOptions"][2]["isCorrect"])