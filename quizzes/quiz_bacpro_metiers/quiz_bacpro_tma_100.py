quiz_data = {
    "title": "Quiz BAC PRO TMA (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : Analyse technique et préparation de la production (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : Analyse technique et préparation de la production",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel document définit la succession des phases d'usinage ?",
                    "answerOptions": [
                        {"text": "La gamme de fabrication", "isCorrect": True},
                        {"text": "Le contrat de phase", "isCorrect": False},
                        {"text": "La nomenclature des matériaux", "isCorrect": False},
                        {"text": "Le dessin de définition", "isCorrect": False}
                    ],
                    "correction": "La gamme de fabrication établit l'ordre chronologique et logique des différentes phases d'usinage pour réaliser une pièce, incluant les machines et les temps alloués."
                },
                {
                    "questionNumber": 2,
                    "question": "Que représente l'échelle 1:5 sur un plan d'agencement ?",
                    "answerOptions": [
                        {"text": "Un centimètre sur le plan vaut cinq centimètres réels", "isCorrect": True},
                        {"text": "Cinq centimètres sur le plan valent un centimètre réel", "isCorrect": False},
                        {"text": "Le plan est agrandi cinq fois par rapport à la réalité", "isCorrect": False},
                        {"text": "Un centimètre sur le plan correspond à cinq mètres réels", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1:5 est une échelle de réduction standard en menuiserie où chaque dimension dessinée est cinq fois plus petite que l'ouvrage réel à fabriquer."
                },
                {
                    "questionNumber": 3,
                    "question": "Sur un dessin de définition, à quoi sert une coupe locale ?",
                    "answerOptions": [
                        {"text": "Montrer un détail intérieur sans couper toute la pièce", "isCorrect": True},
                        {"text": "Représenter la section transversale complète du profil", "isCorrect": False},
                        {"text": "Indiquer le sens du fil du bois massif sur le parement", "isCorrect": False},
                        {"text": "Définir la tolérance de positionnement d'un perçage", "isCorrect": False}
                    ],
                    "correction": "La coupe locale permet de révéler un détail interne spécifique comme un assemblage borgne ou une feuillure, en limitant la zone hachurée par un trait fin ondulé ou brisé."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle information est indispensable dans une nomenclature d'approvisionnement ?",
                    "answerOptions": [
                        {"text": "Les surcotes d'usinage des débits", "isCorrect": True},
                        {"text": "Les cotes finies des pièces usinées", "isCorrect": False},
                        {"text": "Les tolérances géométriques de forme", "isCorrect": False},
                        {"text": "Les références des outils de coupe", "isCorrect": False}
                    ],
                    "correction": "Une nomenclature d'approvisionnement doit inclure les surcotes appelées aussi cotes de débit, nécessaires pour compenser les pertes de matière lors des opérations de corroyage et de sciage."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel trait normalisé représente les contours vus ?",
                    "answerOptions": [
                        {"text": "Trait continu fort", "isCorrect": True},
                        {"text": "Trait interrompu court", "isCorrect": False},
                        {"text": "Trait mixte fin", "isCorrect": False},
                        {"text": "Trait continu fin", "isCorrect": False}
                    ],
                    "correction": "En dessin technique, le trait continu fort est strictement réservé à la représentation des arêtes visibles et des contours vus de la pièce."
                },
                {
                    "questionNumber": 6,
                    "question": "Comment vérifier l'isostatisme d'une pièce sur un montage d'usinage ?",
                    "answerOptions": [
                        {"text": "S'assurer de la suppression des six degrés de liberté", "isCorrect": True},
                        {"text": "Mesurer la perpendicularité des axes de référence", "isCorrect": False},
                        {"text": "Contrôler la pression de serrage des vérins pneumatiques", "isCorrect": False},
                        {"text": "Vérifier l'état de surface du plan d'appui principal", "isCorrect": False}
                    ],
                    "correction": "L'isostatisme consiste à positionner une pièce dans l'espace de manière unique et répétable en bloquant ses trois translations et ses trois rotations."
                },
                {
                    "questionNumber": 7,
                    "question": "Que signifie le symbole de rugosité Ra sur une fiche de phase ?",
                    "answerOptions": [
                        {"text": "L'écart moyen arithmétique du profil de surface", "isCorrect": True},
                        {"text": "La profondeur maximale des stries de coupe", "isCorrect": False},
                        {"text": "Le rayon d'arrondi des arêtes vives de la pièce", "isCorrect": False},
                        {"text": "La résistance mécanique de l'assemblage collé", "isCorrect": False}
                    ],
                    "correction": "Le paramètre Ra caractérise l'état de surface et l'exigence de finition. Il correspond à la moyenne des écarts absolus du profil de rugosité par rapport à la ligne moyenne."
                },
                {
                    "questionNumber": 8,
                    "question": "Dans un ordonnancement, que représente le chemin critique ?",
                    "answerOptions": [
                        {"text": "L'enchaînement des tâches sans aucune marge de flottement", "isCorrect": True},
                        {"text": "L'opération présentant le plus haut risque d'accident", "isCorrect": False},
                        {"text": "Le trajet physique des pièces entre les machines", "isCorrect": False},
                        {"text": "La succession des contrôles de qualité obligatoires", "isCorrect": False}
                    ],
                    "correction": "Le chemin critique détermine la durée incompressible du projet. Tout retard sur une tâche appartenant à ce chemin entraîne un retard global de la production."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle tolérance indique le symbole de concentricité ?",
                    "answerOptions": [
                        {"text": "Deux éléments cylindriques doivent partager le même axe", "isCorrect": True},
                        {"text": "Une surface doit rester dans deux plans parallèles", "isCorrect": False},
                        {"text": "L'inclinaison d'une face par rapport à la référence", "isCorrect": False},
                        {"text": "Le battement axial maximal d'un panneau en rotation", "isCorrect": False}
                    ],
                    "correction": "La concentricité est une tolérance géométrique de position exigeant que les axes de deux cylindres ou de deux cercles soient confondus dans une zone de tolérance définie."
                },
                {
                    "questionNumber": 10,
                    "question": "À quoi correspond la cotation fonctionnelle ?",
                    "answerOptions": [
                        {"text": "Assurer le fonctionnement du mécanisme", "isCorrect": True},
                        {"text": "Faciliter la fabrication en atelier", "isCorrect": False},
                        {"text": "Définir l'aspect esthétique final", "isCorrect": False},
                        {"text": "Indiquer les surcotes de débit", "isCorrect": False}
                    ],
                    "correction": "La cotation fonctionnelle définit les dimensions et tolérances strictement nécessaires pour garantir le montage, l'interchangeabilité et le fonctionnement mécanique de l'ouvrage."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel logiciel est un modeleur volumique paramétrique ?",
                    "answerOptions": [
                        {"text": "TopSolid Wood", "isCorrect": True},
                        {"text": "AutoCAD LT", "isCorrect": False},
                        {"text": "SketchUp Make", "isCorrect": False},
                        {"text": "Adobe Illustrator", "isCorrect": False}
                    ],
                    "correction": "TopSolid Wood est un logiciel de conception assistée par ordinateur paramétrique métier qui permet de concevoir des ouvrages en 3D volumique et de générer les programmes d'usinage."
                },
                {
                    "questionNumber": 12,
                    "question": "Que définit un contrat de phase en usinage ?",
                    "answerOptions": [
                        {"text": "Le mode opératoire détaillé pour un poste de travail", "isCorrect": True},
                        {"text": "Le bon de commande des matières premières", "isCorrect": False},
                        {"text": "L'engagement de livraison envers le client final", "isCorrect": False},
                        {"text": "Le planning général de répartition des tâches", "isCorrect": False}
                    ],
                    "correction": "Le contrat de phase précise, pour une opération donnée, la machine, les outils, les paramètres de coupe, la mise en position isostatique et les cotes de réglage."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est l'objectif du repérage des faces de référence ?",
                    "answerOptions": [
                        {"text": "Garantir la précision géométrique des usinages ultérieurs", "isCorrect": True},
                        {"text": "Identifier la face esthétique parement de la pièce", "isCorrect": False},
                        {"text": "Optimiser le calepinage des panneaux dérivés du bois", "isCorrect": False},
                        {"text": "Masquer les singularités du bois massif au montage", "isCorrect": False}
                    ],
                    "correction": "Les signes d'établissement marquent les faces de référence obtenues au corroyage. Elles serviront d'appui exclusif sur les guides des machines pour garantir la géométrie."
                },
                {
                    "questionNumber": 14,
                    "question": "Comment calculer le temps technologique lors du profilage d'une moulure ?",
                    "answerOptions": [
                        {"text": "En divisant la longueur usinée par la vitesse d'avance de la pièce", "isCorrect": True},
                        {"text": "En additionnant le temps de réglage de la machine de coupe avec le temps de manutention globale entre les différents postes de l'atelier", "isCorrect": False},
                        {"text": "En multipliant la fréquence de rotation de l'outil par le nombre de dents", "isCorrect": False},
                        {"text": "En soustrayant le temps mort du temps alloué total de la production", "isCorrect": False}
                    ],
                    "correction": "Le temps technologique correspond strictement à la durée pendant laquelle l'outil enlève de la matière. Il se calcule par le ratio longueur sur vitesse d'avance en mètres par minute."
                },
                {
                    "questionNumber": 15,
                    "question": "Que représente un trait mixte fin terminé par deux traits forts ?",
                    "answerOptions": [
                        {"text": "Le tracé d'un plan de coupe", "isCorrect": True},
                        {"text": "L'axe de symétrie d'une pièce", "isCorrect": False},
                        {"text": "Une surface à traiter", "isCorrect": False},
                        {"text": "L'encombrement des pièces voisines", "isCorrect": False}
                    ],
                    "correction": "En dessin industriel, cette représentation normalisée indique la position exacte du plan de coupe virtuel traversant la pièce, avec des flèches indiquant le sens d'observation."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la fonction d'un système de mise en position de type appui plan ?",
                    "answerOptions": [
                        {"text": "Supprimer une translation et deux rotations de la pièce traitée", "isCorrect": True},
                        {"text": "Assurer un serrage mécanique extrêmement puissant par bridage hydraulique pour résister aux vibrations générées par le passage de l'outil", "isCorrect": False},
                        {"text": "Maintenir la pièce fermement plaquée contre le guide latéral de toupie", "isCorrect": False},
                        {"text": "Centrer automatiquement la pièce sur l'axe de rotation de la broche", "isCorrect": False}
                    ],
                    "correction": "Dans la théorie de l'isostatisme, l'appui plan bloque trois degrés de liberté à savoir le déplacement perpendiculaire à ce plan et les deux basculements autour des axes de ce plan."
                },
                {
                    "questionNumber": 17,
                    "question": "Pourquoi utilise-t-on le format de fichier DXF en préparation de production ?",
                    "answerOptions": [
                        {"text": "Transférer des données vectorielles entre différents logiciels de conception", "isCorrect": True},
                        {"text": "Compresser les sauvegardes de programmes afin de réduire drastiquement l'espace de stockage occupé sur les serveurs informatiques de l'atelier", "isCorrect": False},
                        {"text": "Générer directement le code machine pour alimenter le centre d'usinage", "isCorrect": False},
                        {"text": "Gérer les nomenclatures d'approvisionnement et les commandes fournisseurs", "isCorrect": False}
                    ],
                    "correction": "Le Drawing eXchange Format est un standard d'interopérabilité permettant l'échange de dessins vectoriels entre la plupart des systèmes de conception assistée par ordinateur."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle règle régit le calcul d'une liaison par tenon et mortaise classique ?",
                    "answerOptions": [
                        {"text": "L'épaisseur du tenon correspond au tiers de l'épaisseur de la pièce", "isCorrect": True},
                        {"text": "La profondeur de la mortaise doit obligatoirement traverser la pièce de bois opposée afin de garantir une évacuation correcte du surplus de colle vinylique", "isCorrect": False},
                        {"text": "L'arasement doit posséder le double de la longueur de la joue de mortaise", "isCorrect": False},
                        {"text": "La largeur du tenon usiné est strictement toujours égale à sa longueur", "isCorrect": False}
                    ],
                    "correction": "Il s'agit d'une règle empirique garantissant l'équilibre mécanique. Un tenon d'un tiers préserve des joues de mortaise d'un tiers chacune, répartissant équitablement la résistance à la rupture."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'intérêt d'établir une gamme de montage dans l'agencement ?",
                    "answerOptions": [
                        {"text": "Organiser la chronologie d'assemblage pour éviter les blocages matériels", "isCorrect": True},
                        {"text": "Répertorier la totalité des références commerciales de la quincaillerie d'ameublement nécessaire pour réaliser le devis du client final", "isCorrect": False},
                        {"text": "Vérifier que le temps de pressage des assemblages collés est bien respecté", "isCorrect": False},
                        {"text": "Déterminer la puissance électrique nécessaire pour l'installation sur site", "isCorrect": False}
                    ],
                    "correction": "La gamme de montage définit l'ordre d'emboîtement. Un mauvais ordonnancement peut rendre l'insertion d'une pièce intermédiaire ou d'une quincaillerie physiquement impossible en fin de montage."
                },
                {
                    "questionNumber": 20,
                    "question": "Comment identifie-t-on une cote tolérancée au maximum de matière ?",
                    "answerOptions": [
                        {"text": "En ajoutant la lettre M majuscule encerclée juste à côté de la valeur", "isCorrect": True},
                        {"text": "En surlignant la ligne de cote avec un trait continu fort et en précisant la norme de référence ISO directement dans le cartouche d'inscription", "isCorrect": False},
                        {"text": "En soulignant simplement la valeur nominale de la dimension sur le plan", "isCorrect": False},
                        {"text": "En plaçant la dimension de référence entre crochets sur la vue de face", "isCorrect": False}
                    ],
                    "correction": "Le principe du maximum de matière lie les tolérances dimensionnelles et géométriques. L'exigence géométrique est modifiée lorsque la pièce s'éloigne de son état de maximum de matière."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : Matériaux, quincaillerie et quincaillerie d'agencement (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : Matériaux, quincaillerie et quincaillerie d'agencement",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel panneau dérivé du bois possède la meilleure stabilité dimensionnelle isotrope ?",
                    "answerOptions": [
                        {"text": "Le panneau MDF", "isCorrect": True},
                        {"text": "Le contreplaqué okoumé", "isCorrect": False},
                        {"text": "Le panneau OSB", "isCorrect": False},
                        {"text": "Le latté placage chêne", "isCorrect": False}
                    ],
                    "correction": "Le Medium Density Fiberboard présente une structure isotrope grâce à la désintégration fine du bois en fibres et à leur pressage homogène, offrant ainsi un retrait et un gonflement identiques dans toutes les directions du plan."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle colle offre une résistance structurelle à l'humidité extérieure ?",
                    "answerOptions": [
                        {"text": "La colle polyuréthane", "isCorrect": True},
                        {"text": "La colle vinylique standard", "isCorrect": False},
                        {"text": "La colle thermofusible EVA", "isCorrect": False},
                        {"text": "La colle urée formol", "isCorrect": False}
                    ],
                    "correction": "La colle polyuréthane réticule au contact de l'humidité de l'air et du bois. Elle forme un joint structurel classé D4, parfaitement résistant à l'eau et aux intempéries."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel composant assure le rappel en fermeture d'une charnière invisible ?",
                    "answerOptions": [
                        {"text": "Le ressort de rappel", "isCorrect": True},
                        {"text": "Le vérin pneumatique", "isCorrect": False},
                        {"text": "L'embase cruciforme", "isCorrect": False},
                        {"text": "Le bras articulé", "isCorrect": False}
                    ],
                    "correction": "Le ressort de rappel, souvent dissimulé dans le boîtier ou sous le bras articulé de la charnière invisible, maintient la porte plaquée contre le caisson en fin de course sans nécessiter de loqueteau."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel insecte xylophage dégrade l'aubier des feuillus durs ?",
                    "answerOptions": [
                        {"text": "Le lyctus brun", "isCorrect": True},
                        {"text": "Le capricorne des maisons", "isCorrect": False},
                        {"text": "Le termite souterrain", "isCorrect": False},
                        {"text": "La vrillette domestique", "isCorrect": False}
                    ],
                    "correction": "Le lyctus brun attaque spécifiquement l'aubier des feuillus à larges vaisseaux riches en amidon, tels que le chêne ou le châtaignier, réduisant le bois en une fine poudre farineuse."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment caractérise-t-on un panneau de particules classé P3 selon la norme EN 312 ?",
                    "answerOptions": [
                        {"text": "C'est un panneau non travaillant prévu pour un usage intérieur en milieu humide", "isCorrect": True},
                        {"text": "C'est un panneau structurel à haute densité spécifiquement conçu pour supporter des charges lourdes permanentes en milieu extérieur soumis aux intempéries directes", "isCorrect": False},
                        {"text": "C'est un panneau standard pour agencement intérieur sec", "isCorrect": False},
                        {"text": "C'est un panneau ignifugé classé au feu pour les établissements recevant du public", "isCorrect": False}
                    ],
                    "correction": "La norme EN 312 classifie les panneaux de particules. La classe P3 désigne les panneaux pour agencement intérieur non travaillant utilisés en milieu humide, collés généralement avec des résines mélamine urée formol pour résister aux variations hygrométriques ponctuelles."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la particularité structurelle d'un stratifié HPL haute pression ?",
                    "answerOptions": [
                        {"text": "Il est composé de feuilles de papier kraft imprégnées de résine phénolique polymérisées à chaud", "isCorrect": True},
                        {"text": "Il est constitué exclusivement de véritables placages de bois tranchés très finement puis collés sous très haute pression avec une résine époxy transparente pour garantir une parfaite étanchéité", "isCorrect": False},
                        {"text": "Il s'agit d'un film mélaminé collé sur un support panneau de particules fin", "isCorrect": False},
                        {"text": "Il comporte une âme en aluminium intercalée entre deux feuilles de papier décor", "isCorrect": False}
                    ],
                    "correction": "Le High Pressure Laminate est un revêtement de surface stratifié constitué d'un empilage de feuilles de papier kraft imprégnées de résine thermodurcissable phénolique, recouvert d'un papier décor et d'une couche de protection overlay, le tout pressé à haute température."
                },
                {
                    "questionNumber": 27,
                    "question": "Pourquoi utiliser une colle vinylique classée D3 plutôt qu'une colle D2 en agencement ?",
                    "answerOptions": [
                        {"text": "Elle résiste aux condensations fréquentes et aux écoulements d'eau de courte durée en intérieur", "isCorrect": True},
                        {"text": "Elle permet un assemblage structurel de charpente extérieure exposée directement aux intempéries hivernales sans nécessiter l'application d'un vernis de protection supplémentaire sur le bois massif", "isCorrect": False},
                        {"text": "Elle garantit un temps d'ouverture prolongé pour les grands assemblages complexes", "isCorrect": False},
                        {"text": "Elle ne tache pas les essences tanniques comme le chêne lors du pressage", "isCorrect": False}
                    ],
                    "correction": "Selon la norme NF EN 204, la classe D3 définit des colles d'intérieur résistantes aux ambiances très humides, idéales pour les agencements de salles de bains ou de cuisines où l'eau de ruissellement ponctuelle est présente."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel réglage permet d'ajuster l'affleurement des portes sur une charnière invisible tridimensionnelle ?",
                    "answerOptions": [
                        {"text": "La vis située sur le bras articulé permettant de rapprocher ou d'éloigner la porte du caisson", "isCorrect": True},
                        {"text": "La rotation de la vis excentrique logée directement au centre de l'embase cruciforme qui permet de modifier la hauteur totale de la façade par rapport à la base du meuble d'agencement", "isCorrect": False},
                        {"text": "Le desserrage des vis de fixation de l'embase pour translater verticalement la façade", "isCorrect": False},
                        {"text": "La vis de fond de boîtier agissant sur la tension du ressort de rappel", "isCorrect": False}
                    ],
                    "correction": "Le réglage de profondeur, ou d'affleurement, se fait via une vis placée sur le bras de la charnière. Elle permet d'ajuster le jeu entre l'arrière de la porte et le chant avant du caisson."
                },
                {
                    "questionNumber": 29,
                    "question": "Que définit le coefficient de retrait volumique d'une essence de bois massif ?",
                    "answerOptions": [
                        {"text": "La variation de volume du bois pour une variation d'un pourcent de son taux d'humidité", "isCorrect": True},
                        {"text": "La perte de résistance mécanique globale mesurée en mégapascals lorsque la pièce de menuiserie est soumise à de violentes variations de température dans un environnement fortement climatisé", "isCorrect": False},
                        {"text": "La différence de dimension mesurée entre le retrait tangentiel et le retrait radial", "isCorrect": False},
                        {"text": "L'aptitude du bois à se cintrer sous l'action combinée de la vapeur et de la pression", "isCorrect": False}
                    ],
                    "correction": "Le retrait volumique caractérise l'instabilité d'une essence. Il s'exprime en pourcentage de variation de volume pour chaque pourcent de variation de l'humidité du bois en dessous du point de saturation des fibres."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est l'avantage cinématique d'une coulisse de tiroir à sortie totale ?",
                    "answerOptions": [
                        {"text": "Elle permet l'extraction complète du tiroir hors du caisson grâce à un profil intermédiaire", "isCorrect": True},
                        {"text": "Elle intègre un mécanisme à crémaillère complexe garantissant une synchronisation parfaite des deux côtés du tiroir pour éviter tout phénomène de coincement lors de l'ouverture asymétrique par l'utilisateur", "isCorrect": False},
                        {"text": "Elle se fixe exclusivement sous le fond du tiroir pour une esthétique invisible", "isCorrect": False},
                        {"text": "Elle supporte des charges dynamiques inférieures grâce à des galets en nylon", "isCorrect": False}
                    ],
                    "correction": "La sortie totale est rendue possible par la présence d'un rail intermédiaire télescopique. L'extension dépasse la longueur nominale de la coulisse, offrant un accès intégral à l'arrière du tiroir d'agencement."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel défaut de séchage provoque des gerces internes dans le bois ?",
                    "answerOptions": [
                        {"text": "La cémentation due à un séchage trop rapide", "isCorrect": True},
                        {"text": "Le collapse cellulaire par excès de température", "isCorrect": False},
                        {"text": "L'échauffure causée par un champignon lignivore", "isCorrect": False},
                        {"text": "Le tuilage lié à l'orientation des cernes", "isCorrect": False}
                    ],
                    "correction": "La cémentation apparaît lors d'un séchage trop brutal de la périphérie de la planche. Les couches externes durcissent, empêchant le retrait du bois à cœur, ce qui provoque des tensions internes aboutissant à des gerces profondes."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle classe d'emploi du bois correspond à une exposition extérieure sans contact avec le sol ?",
                    "answerOptions": [
                        {"text": "La classe d'emploi 3", "isCorrect": True},
                        {"text": "La classe d'emploi 2", "isCorrect": False},
                        {"text": "La classe d'emploi 4", "isCorrect": False},
                        {"text": "La classe d'emploi 5", "isCorrect": False}
                    ],
                    "correction": "La classe 3 correspond aux bois exposés aux intempéries mais non en contact avec le sol, typiquement utilisés pour les bardages et les menuiseries extérieures où l'humidification est fréquente mais le séchage possible."
                },
                {
                    "questionNumber": 33,
                    "question": "Sur quel critère sélectionne-t-on une embase de charnière invisible ?",
                    "answerOptions": [
                        {"text": "L'épaisseur du panneau latéral du caisson", "isCorrect": True},
                        {"text": "Le poids total de la porte équipée", "isCorrect": False},
                        {"text": "L'angle d'ouverture maximal souhaité", "isCorrect": False},
                        {"text": "La profondeur du perçage du boîtier", "isCorrect": False}
                    ],
                    "correction": "L'épaisseur de l'embase dicte la surépaisseur de montage. Elle doit être calculée avec précision en fonction de l'épaisseur du côté du caisson et du recouvrement souhaité pour la façade."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel additif améliore la résistance à l'humidité d'un panneau MDF ?",
                    "answerOptions": [
                        {"text": "La résine mélamine urée formol", "isCorrect": True},
                        {"text": "La cire d'abeille naturelle", "isCorrect": False},
                        {"text": "Le durcisseur isocyanate", "isCorrect": False},
                        {"text": "Les fibres de verre courtes", "isCorrect": False}
                    ],
                    "correction": "L'ajout de mélamine dans la colle urée formol renforce les liaisons chimiques inter-fibres. Le panneau MDF obtenu devient apte aux milieux humides intérieurs, souvent repérable par un colorant vert dans la masse."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le rôle d'un tourillon hélicoïdal en hêtre ?",
                    "answerOptions": [
                        {"text": "Permettre une meilleure répartition de la colle", "isCorrect": True},
                        {"text": "Visser la pièce lors de la frappe", "isCorrect": False},
                        {"text": "Éviter l'éclatement des panneaux minces", "isCorrect": False},
                        {"text": "Assurer le centrage automatique des pièces", "isCorrect": False}
                    ],
                    "correction": "Les stries hélicoïdales ou droites usinées sur le corps du tourillon servent de canaux de répartition. Lors de l'enfoncement, elles permettent à l'excédent de colle de remonter et d'éviter un effet piston qui ferait éclater le chant."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle quincaillerie permet l'assemblage démontable de deux panneaux perpendiculaires ?",
                    "answerOptions": [
                        {"text": "Le boîtier excentrique avec goujon", "isCorrect": True},
                        {"text": "Le tourillon collé en bois strié", "isCorrect": False},
                        {"text": "La lamelle d'assemblage type biscuit", "isCorrect": False},
                        {"text": "La vis à bois tête fraisée", "isCorrect": False}
                    ],
                    "correction": "Le système d'assemblage par boîtier excentrique et goujon de serrage offre une liaison mécanique très rigide pour les caissons d'agencement tout en conservant une démontabilité parfaite du meuble."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel type de panneau contreplaqué est préconisé pour un agencement naval intérieur ?",
                    "answerOptions": [
                        {"text": "Le contreplaqué marine à collage phénolique", "isCorrect": True},
                        {"text": "Le contreplaqué cintrable à plis croisés", "isCorrect": False},
                        {"text": "Le contreplaqué ignifugé classé M1", "isCorrect": False},
                        {"text": "Le contreplaqué peuplier à faces okoumé", "isCorrect": False}
                    ],
                    "correction": "Le contreplaqué dit marine garantit une pérennité absolue face à l'humidité constante. Il utilise une résine phénolique ou résorcine de classe 3 et des plis en essences durables, exempts de défauts internes."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment nomme-t-on le placage obtenu par déroulage d'une bille de bois ?",
                    "answerOptions": [
                        {"text": "Le placage continu avec dosse ramageuse", "isCorrect": True},
                        {"text": "Le placage tranché sur quartier", "isCorrect": False},
                        {"text": "Le placage scié en fil droit", "isCorrect": False},
                        {"text": "Le placage reconstitué précomposé", "isCorrect": False}
                    ],
                    "correction": "Le déroulage, souvent appliqué au peuplier ou à l'okoumé, engendre un ruban de placage continu. L'outil coupe tangentiellement les cernes d'accroissement, ce qui révèle un fort ramage typique de la coupe sur dosse."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle caractéristique mécanique justifie l'utilisation d'un panneau OSB ?",
                    "answerOptions": [
                        {"text": "Sa haute résistance à la flexion", "isCorrect": True},
                        {"text": "Sa surface parfaitement lisse pour laquage", "isCorrect": False},
                        {"text": "Son excellente isolation phonique", "isCorrect": False},
                        {"text": "Sa faible masse volumique globale", "isCorrect": False}
                    ],
                    "correction": "L'Oriented Strand Board possède des lamelles de bois longues, orientées longitudinalement sur les faces externes et transversalement à cœur. Cette architecture structurelle lui confère une excellente rigidité et résistance à la flexion."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel traitement préservatif s'applique en autoclave sous vide et pression ?",
                    "answerOptions": [
                        {"text": "L'imprégnation à cœur des sels de cuivre", "isCorrect": True},
                        {"text": "Le trempage court au bain fongicide", "isCorrect": False},
                        {"text": "L'aspersion en tunnel de pulvérisation", "isCorrect": False},
                        {"text": "L'application de lasure au rouleau", "isCorrect": False}
                    ],
                    "correction": "L'autoclave combine le vide pour vider les cellules du bois de leur air et la pression pour y forcer la pénétration du produit de préservation, conférant une protection durable pour des bois destinés aux classes d'emploi 3 et 4."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : Usinage et procédés de fabrication en atelier (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : Usinage et procédés de fabrication en atelier",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle unité mesure la vitesse de coupe d'un outil de toupie ?",
                    "answerOptions": [
                        {"text": "Mètre par seconde", "isCorrect": True},
                        {"text": "Tour par minute", "isCorrect": False},
                        {"text": "Mètre par minute", "isCorrect": False},
                        {"text": "Millimètre par dent", "isCorrect": False}
                    ],
                    "correction": "La vitesse de coupe (Vc) exprime la distance parcourue par une dent de l'outil en une seconde, d'où son expression en mètres par seconde."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel protecteur équipe l'arbre porte-couteaux de la dégauchisseuse ?",
                    "answerOptions": [
                        {"text": "Protecteur à pont", "isCorrect": True},
                        {"text": "Protecteur à visière", "isCorrect": False},
                        {"text": "Carénage enveloppant", "isCorrect": False},
                        {"text": "Guide presseur latéral", "isCorrect": False}
                    ],
                    "correction": "Le protecteur à pont réglementaire recouvre la zone non utilisée de l'arbre de dégauchisseuse, s'ajustant en hauteur et en largeur au passage de la pièce pour interdire l'accès aux couteaux."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel mode d'usinage est strictement interdit en alimentation manuelle sur toupie ?",
                    "answerOptions": [
                        {"text": "Le travail en avalant", "isCorrect": True},
                        {"text": "Le travail en opposition", "isCorrect": False},
                        {"text": "Le calibrage au calibre", "isCorrect": False},
                        {"text": "Le fraisage par le dessus", "isCorrect": False}
                    ],
                    "correction": "L'usinage en avalant, où le sens d'avance de la pièce est identique au sens de rotation de l'outil, entraîne une éjection violente incontrôlable à la main. Il est réservé à l'avance mécanique."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel axe cartésien gère le déplacement vertical de l'électrobroche sur un centre d'usinage ?",
                    "answerOptions": [
                        {"text": "L'axe Z", "isCorrect": True},
                        {"text": "L'axe X", "isCorrect": False},
                        {"text": "L'axe Y", "isCorrect": False},
                        {"text": "L'axe C", "isCorrect": False}
                    ],
                    "correction": "Dans le repère cartésien normé d'une machine à commande numérique, l'axe Z commande la plongée et le retrait de l'outil, correspondant au mouvement vertical par rapport au plan de la table."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle cinématique caractérise la mortaiseuse à chaîne ?",
                    "answerOptions": [
                        {"text": "La chaîne descend verticalement dans la pièce bridée", "isCorrect": True},
                        {"text": "Le chariot déplace la pièce vers l'outil rotatif", "isCorrect": False},
                        {"text": "Le bédane frappe le bois par mouvements alternatifs", "isCorrect": False},
                        {"text": "La mèche oscillante creuse la cavité latéralement", "isCorrect": False}
                    ],
                    "correction": "Sur une mortaiseuse à chaîne, la pièce reste fixe. L'outil composé d'un guide et d'une chaîne dentée s'abaisse verticalement pour usiner la mortaise d'un seul bloc, de manière rapide et puissante."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la cause mécanique d'un talonnage en fin de passe à la raboteuse ?",
                    "answerOptions": [
                        {"text": "Un cylindre de sortie réglé trop bas par rapport à la table", "isCorrect": True},
                        {"text": "Des couteaux usés présentant un morfil important", "isCorrect": False},
                        {"text": "Une vitesse d'avance trop rapide pour l'état de surface", "isCorrect": False},
                        {"text": "Un affaissement de la table de dégauchissage d'entrée", "isCorrect": False}
                    ],
                    "correction": "Si le rouleau extracteur est réglé trop bas, il appuie excessivement sur l'extrémité de la pièce au moment où elle quitte le rouleau d'entrée, la basculant contre les couteaux et créant un désaffleur final."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment calculer l'avance par dent lors d'un usinage mécanique ?",
                    "answerOptions": [
                        {"text": "Vitesse d'avance divisée par le produit de la fréquence de rotation et du nombre de dents", "isCorrect": True},
                        {"text": "Fréquence de rotation multipliée par le diamètre de l'outil en bout", "isCorrect": False},
                        {"text": "Vitesse de coupe divisée par la circonférence totale du porte-outil", "isCorrect": False},
                        {"text": "Nombre de dents multiplié par l'épaisseur du copeau coupé", "isCorrect": False}
                    ],
                    "correction": "L'avance par dent Fz s'obtient avec la formule Fz = Vf / [N x Z], paramètre déterminant pour garantir un copeau d'épaisseur optimale et un bon état de surface sans surchauffe de l'outil."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel avantage technique offre un porte-outil à plaquettes jetables en carbure de tungstène ?",
                    "answerOptions": [
                        {"text": "Le maintien constant du diamètre de coupe sans réaffûtage", "isCorrect": True},
                        {"text": "Une souplesse accrue lors de l'usinage de bois très nerveux", "isCorrect": False},
                        {"text": "La diminution des rejets de poussières fines en atelier", "isCorrect": False},
                        {"text": "L'augmentation automatique de la vitesse de rotation", "isCorrect": False}
                    ],
                    "correction": "Les plaquettes jetables réversibles ne se réaffûtent pas. Cela conserve le diamètre de l'outil rigoureusement constant, évitant de modifier les réglages de la machine ou le programme d'usinage CN."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel accessoire est indispensable pour calibrer une pièce courbe à la toupie ?",
                    "answerOptions": [
                        {"text": "Un roulement à billes ou anneau copieur", "isCorrect": True},
                        {"text": "Un guide continu en bois profilé", "isCorrect": False},
                        {"text": "Un entraîneur automatique à quatre rouleaux", "isCorrect": False},
                        {"text": "Une règle crantée anti-recul en aluminium", "isCorrect": False}
                    ],
                    "correction": "Pour profiler une pièce de forme complexe, on utilise un montage d'usinage guidé en appui sur un roulement, aussi appelé bague de copiage, monté concentriquement sur l'arbre de la toupie."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel système assure la liaison entre l'électrobroche et le cône porte-outil sur un centre d'usinage moderne ?",
                    "answerOptions": [
                        {"text": "Le système de serrage HSK", "isCorrect": True},
                        {"text": "Le mandrin à mors concentriques", "isCorrect": False},
                        {"text": "Le système d'adaptation par bague conique", "isCorrect": False},
                        {"text": "L'attachement cylindrique à clavette", "isCorrect": False}
                    ],
                    "correction": "L'attachement HSK offre une rigidité radiale et axiale supérieure grâce au serrage par l'intérieur déformant le cône, s'adaptant parfaitement aux hautes fréquences de rotation des broches CN."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le rôle de la lame inciseur sur une scie à format ?",
                    "answerOptions": [
                        {"text": "Trancher le revêtement inférieur pour éviter les éclats", "isCorrect": True},
                        {"text": "Diviser la puissance requise pour le sciage final", "isCorrect": False},
                        {"text": "Augmenter la vitesse de coupe globale du panneau", "isCorrect": False},
                        {"text": "Assurer le guidage parallèle du panneau dérivé", "isCorrect": False}
                    ],
                    "correction": "L'inciseur est une petite lame tournant en opposition à la lame principale. Elle réalise une rainure peu profonde sous le panneau mélaminé pour couper la couche de surface avant la sortie des dents de la lame principale."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment orienter les rouleaux d'un entraîneur sur une toupie classique ?",
                    "answerOptions": [
                        {"text": "Légèrement désaxés vers le guide pour plaquer la pièce", "isCorrect": True},
                        {"text": "Parfaitement parallèles au déplacement pour éviter le frottement", "isCorrect": False},
                        {"text": "Inclinés vers la sortie pour accélérer le dégagement final", "isCorrect": False},
                        {"text": "Axés vers le centre de l'outil pour forcer la plongée", "isCorrect": False}
                    ],
                    "correction": "L'inclinaison des rouleaux de l'entraîneur avec un léger pincement vers le guide garantit un appui continu et sécuritaire de la face de référence latérale pendant toute la passe d'usinage."
                },
                {
                    "questionNumber": 53,
                    "question": "Que désigne l'angle d'attaque d'une dent de scie circulaire ?",
                    "answerOptions": [
                        {"text": "L'angle entre la face de coupe et le rayon passant par l'arête", "isCorrect": True},
                        {"text": "L'angle mesuré entre le dos de la dent et la surface usinée", "isCorrect": False},
                        {"text": "L'inclinaison latérale alternée des dents sur le corps de lame", "isCorrect": False},
                        {"text": "L'angle d'affûtage biseauté sur la partie supérieure du carbure", "isCorrect": False}
                    ],
                    "correction": "L'angle d'attaque conditionne la pénétration de la dent dans le matériau. Il est formé par la face antérieure de la dent et le rayon de la lame de scie passant par la pointe du taillant."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle information sécuritaire grave obligatoirement le fabricant sur un outil de toupie ?",
                    "answerOptions": [
                        {"text": "La plage de fréquence de rotation admissible", "isCorrect": True},
                        {"text": "Le temps maximum d'utilisation continue", "isCorrect": False},
                        {"text": "L'essence de bois recommandée pour l'usinage", "isCorrect": False},
                        {"text": "L'angle de dépouille spécifique aux taillants", "isCorrect": False}
                    ],
                    "correction": "Les outils conformes portent obligatoirement la gravure indiquant la plage de vitesse de rotation minimale et maximale garantissant la sécurité cinématique contre l'éclatement ou le rejet dangereux."
                },
                {
                    "questionNumber": 55,
                    "question": "En quoi consiste la technologie d'usinage par Nesting sur commande numérique ?",
                    "answerOptions": [
                        {"text": "C'est un procédé d'imbrication et de découpe complète de pièces dans un panneau brut sur une table à dépression martyre", "isCorrect": True},
                        {"text": "C'est une technique spécifique consistant à caler individuellement des petites pièces de bois massif sur des ventouses pneumatiques surélevées permettant un profilage intégral de leurs chants périphériques sans aucune détérioration du plan de travail de la machine", "isCorrect": False},
                        {"text": "Il s'agit d'un système de palpage tridimensionnel permettant à la machine de repérer automatiquement les défauts naturels du bois", "isCorrect": False},
                        {"text": "C'est un mode opératoire programmé qui gère la permutation automatique des agrégats de perçage selon l'épaisseur exacte mesurée", "isCorrect": False}
                    ],
                    "correction": "Le Nesting optimise le rendement matière. La machine découpe les pièces de formes variées directement dans le panneau complet maintenu par vide sur un MDF sacrificiel poreux, limitant les manipulations."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle est la fonction principale d'un outil de toupie à avance manuelle dit MAN ?",
                    "answerOptions": [
                        {"text": "Il possède des limiteurs de passe empêchant une prise de copeau supérieure à la norme pour éviter les risques de rejet", "isCorrect": True},
                        {"text": "Il intègre un mécanisme à ressort complexe situé derrière chaque plaquette carbure qui absorbe les vibrations à haute fréquence provoquées par les nœuds durs du bois massif lors des opérations de calibrage intensif", "isCorrect": False},
                        {"text": "Il autorise une vitesse de rotation extrêmement élevée pour garantir un poli de surface parfait sur les panneaux plaqués d'essences fines", "isCorrect": False},
                        {"text": "Il comporte une bague micrométrique interne permettant de modifier le diamètre de coupe sans démonter l'outil de la broche", "isCorrect": False}
                    ],
                    "correction": "La législation impose des outils MAN pour le travail manuel. Leur conception cylindrique ou l'intégration de contrefers proéminents limite l'épaisseur maximale du copeau usiné, parant au rejet brutal de la pièce."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment fonctionne le groupe de coupe en bout sur une plaqueuse de chants linéaire ?",
                    "answerOptions": [
                        {"text": "Il utilise des scies circulaires montées sur des moteurs accompagnant la pièce dans son mouvement pour sectionner le chant", "isCorrect": True},
                        {"text": "Il emploie un système de cisaille guillotine pneumatique fixe qui frappe violemment l'excédent de chant plastique dès que le capteur optique détecte précisément l'extrémité arrière du panneau en défilement continu", "isCorrect": False},
                        {"text": "Il est composé de fraises d'affleurage qui abrasent progressivement le débord de chant en suivant un palpeur mécanique rotatif", "isCorrect": False},
                        {"text": "Il utilise un fil chaud chauffé électriquement qui coupe net les chants en PVC par fusion thermique lors du passage", "isCorrect": False}
                    ],
                    "correction": "Le groupe de coupe en bout arase les extrémités du chant collé. Les petites scies se déplacent à la vitesse du convoyeur pendant la coupe pour garantir un sciage d'équerre sans stopper l'avance du panneau."
                },
                {
                    "questionNumber": 58,
                    "question": "Qu'est-ce qui provoque un défaut d'usinage en creux en milieu de pièce à la dégauchisseuse ?",
                    "answerOptions": [
                        {"text": "La table de réception est réglée en dessous du cylindre tangentiel décrit par l'arête tranchante des couteaux", "isCorrect": True},
                        {"text": "L'opérateur applique une pression manuelle excessive et irrégulière sur la pièce exactement lors de son passage critique sur la lèvre antibruit de la table d'entrée en provoquant un fléchissement structurel du bois", "isCorrect": False},
                        {"text": "Les fers de l'arbre porte-couteaux présentent un angle d'affûtage inadapté à la densité de l'essence usinée", "isCorrect": False},
                        {"text": "Le guide latéral est mal équerré par rapport au plan horizontal formé par la table de sortie", "isCorrect": False}
                    ],
                    "correction": "Si la table de sortie est trop basse par rapport à la circonférence de coupe, la pièce s'affaisse et bascule vers l'avant dès qu'elle quitte la table d'entrée, ce qui creuse le milieu du parement."
                },
                {
                    "questionNumber": 59,
                    "question": "Dans quel cas professionnel utilise-t-on la technique de l'usinage à la lunette sur une toupie ?",
                    "answerOptions": [
                        {"text": "Pour l'usinage en plein bois d'une pièce arrêtée nécessitant une plongée progressive dans l'outil rotatif", "isCorrect": True},
                        {"text": "Pour calibrer simultanément les deux chants opposés d'une pièce de bois massif cintrée en utilisant un entraîneur automatique couplé à un gabarit de copiage complexe maintenu par des vérins pneumatiques", "isCorrect": False},
                        {"text": "Pour réaliser un profilage profond sur des bois de faible section nécessitant une vitesse d'avance très rapide", "isCorrect": False},
                        {"text": "Pour tenonner des montants de menuiserie sans utiliser de chariot coulissant ni de guide latéral", "isCorrect": False}
                    ],
                    "correction": "Le travail à la lunette s'effectue avec un montage spécifique à butée. Il permet de profiler une portion interne arrêtée de la pièce, comme un arrêt de chanfrein, par une plongée maîtrisée contre l'outil."
                },
                {
                    "questionNumber": 60,
                    "question": "Que signifie techniquement l'interpolation hélicoïdale programmée sur une commande numérique ?",
                    "answerOptions": [
                        {"text": "Le déplacement synchronisé de la broche combinant un mouvement circulaire en X et Y avec un déplacement linéaire en Z", "isCorrect": True},
                        {"text": "Le calcul prédictif en temps réel de la trajectoire de l'outil réalisé par le microprocesseur de la machine afin de ralentir automatiquement la vitesse d'avance à l'approche des angles vifs du panneau d'agencement", "isCorrect": False},
                        {"text": "L'inclinaison dynamique du groupe d'usinage multiaxes permettant d'usiner la sous-face du panneau brut", "isCorrect": False},
                        {"text": "Le basculement automatique du magasin d'outils rotatif pour anticiper le changement de mèche", "isCorrect": False}
                    ],
                    "correction": "L'interpolation hélicoïdale combine deux mouvements machine : un cercle généré dans le plan XY et une translation verticale Z. Elle est très utilisée pour le surfaçage de puits de quincaillerie de grands diamètres."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : Assemblage, montage et finition (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : Assemblage, montage et finition",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel défaut visuel provoque une bande abrasive encrassée ?",
                    "answerOptions": [
                        {"text": "Des traces de brûlure", "isCorrect": True},
                        {"text": "Un arrachement des fibres", "isCorrect": False},
                        {"text": "Une délamination du placage", "isCorrect": False},
                        {"text": "Un affaissement des chants", "isCorrect": False}
                    ],
                    "correction": "L'encrassement de la bande abrasive par de la résine ou de la colle diminue radicalement le pouvoir de coupe. Le frottement continu génère un échauffement localisé qui brûle et noircit la surface du bois massif ou du placage."
                },
                {
                    "questionNumber": 62,
                    "question": "Comment contrôler rapidement l'équerrage parfait d'un caisson assemblé ?",
                    "answerOptions": [
                        {"text": "En mesurant les diagonales", "isCorrect": True},
                        {"text": "En utilisant un niveau à bulle", "isCorrect": False},
                        {"text": "En vérifiant le faux aplomb", "isCorrect": False},
                        {"text": "En alignant une règle droite", "isCorrect": False}
                    ],
                    "correction": "La méthode la plus fiable et rapide en atelier consiste à mesurer l'égalité stricte des diagonales intérieures ou extérieures du caisson avant le serrage définitif des presses ou du fond arrière."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel paramètre désigne le délai maximum d'attente avant pressage ?",
                    "answerOptions": [
                        {"text": "Le temps d'ouverture", "isCorrect": True},
                        {"text": "La durée de polymérisation", "isCorrect": False},
                        {"text": "Le point de gel thermique", "isCorrect": False},
                        {"text": "La phase de réticulation", "isCorrect": False}
                    ],
                    "correction": "Le temps d'ouverture, ou temps ouvert, est le laps de temps maximal autorisé entre l'application de la colle sur la pièce et l'application effective de la pression d'assemblage sous peine de voir le joint perdre son pouvoir d'adhérence."
                },
                {
                    "questionNumber": 64,
                    "question": "Avec quel instrument contrôle-t-on la viscosité d'un vernis PU ?",
                    "answerOptions": [
                        {"text": "Une coupe consistométrique", "isCorrect": True},
                        {"text": "Un viscosimètre à aiguille", "isCorrect": False},
                        {"text": "Un densitomètre optique", "isCorrect": False},
                        {"text": "Une jauge d'épaisseur", "isCorrect": False}
                    ],
                    "correction": "La coupe consistométrique de type Ford ou AFNOR permet de chronométrer l'écoulement gravitaire d'un volume calibré de vernis. Le temps obtenu en secondes définit la viscosité exacte pour ajuster la quantité de diluant."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est l'avantage structurel du système d'assemblage par lamelle en hêtre compressé ?",
                    "answerOptions": [
                        {"text": "La lamelle gonfle au contact de l'humidité de la colle vinylique, comblant les jeux de la rainure pour créer un blocage mécanique particulièrement résistant aux efforts de cisaillement", "isCorrect": True},
                        {"text": "Le système nécessite un usinage traversant de part en part du panneau, ce qui fragilise grandement l'esthétique globale de l'ouvrage fini mais garantit paradoxalement une excellente tenue lors des chocs répétés sur le meuble en conditions extrêmes d'utilisation", "isCorrect": False},
                        {"text": "Le hêtre compressé empêche la migration des tanins vers le parement lors de l'application de teintes à solvant", "isCorrect": False},
                        {"text": "La forme asymétrique de la lamelle garantit un détrompage automatique de l'opérateur lors du montage", "isCorrect": False}
                    ],
                    "correction": "Le biscuit ou lamelle d'assemblage type Lamello est fabriqué en hêtre rétreint. L'eau contenue dans la colle D2 ou D3 provoque un gonflement immédiat du bois, annulant le jeu d'usinage et bloquant l'assemblage avant même la prise complète."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le principe de fonctionnement d'une pompe de pulvérisation de type Airless ?",
                    "answerOptions": [
                        {"text": "Le vernis est mis sous très haute pression par un piston mécanique et pulvérisé par forçage à travers une buse calibrée sans aucun ajout d'air de pulvérisation externe", "isCorrect": True},
                        {"text": "L'appareil utilise un grand volume d'air comprimé à très basse pression généré par une turbine électrique spécifique afin de créer un brouillard de peinture extrêmement dense qui enveloppe littéralement la pièce de menuiserie complexe sans provoquer de rebond", "isCorrect": False},
                        {"text": "Le système aspire l'air ambiant pour le mélanger directement aux solvants volatils dans la chambre de chauffe de la cuve", "isCorrect": False},
                        {"text": "Une électrode charge positivement les particules de laque pour les projeter magnétiquement sur le panneau dérivé", "isCorrect": False}
                    ],
                    "correction": "La technologie Airless pulvérise le produit uniquement grâce à sa mise sous haute pression par une pompe hydraulique, de 100 à 250 bars, forçant le liquide à travers l'orifice étroit de la buse pour le micro-fractionner sans air de pulvérisation."
                },
                {
                    "questionNumber": 67,
                    "question": "Pourquoi utilise-t-on une feuille de Mylar dans une presse à plaquer à plateaux chauffants ?",
                    "answerOptions": [
                        {"text": "Elle empêche l'adhérence accidentelle des coulures de colle urée formol sur les plateaux en aluminium tout en résistant parfaitement aux températures élevées de polymérisation", "isCorrect": True},
                        {"text": "Ce composant synthétique permet de répartir uniformément l'effort de pression sur des panneaux présentant de forts défauts de planéité d'origine en agissant comme un coussin d'air comprimé capable d'absorber les variations dimensionnelles jusqu'à plusieurs millimètres", "isCorrect": False},
                        {"text": "Elle accélère considérablement le transfert thermique entre les résistances électriques et le panneau support", "isCorrect": False},
                        {"text": "Ce film maintient les feuilles de placage juxtaposées bord à bord sans nécessiter de jointage préalable au fil thermofusible", "isCorrect": False}
                    ],
                    "correction": "Le Mylar est un film polyester anti-adhérent très fin. Placé entre l'ouvrage et le plateau chauffant, il protège la machine des débordements de colle inévitables lors du pressage, évitant un encrassement dommageable au transfert thermique."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle précaution géométrique s'impose lors de l'utilisation d'une cadreuse pneumatique pour huisseries ?",
                    "answerOptions": [
                        {"text": "Il faut impérativement régler la poussée des vérins horizontaux en opposition symétrique par rapport à l'axe des montants pour éviter tout flambement du profil lors de la mise en pression", "isCorrect": True},
                        {"text": "Il est strictement nécessaire de s'assurer que la température ambiante de l'atelier de finition est maintenue au-dessus de vingt degrés Celsius afin de garantir que les vérins pneumatiques ne souffrent d'aucune condensation interne provoquant un grippage irrémédiable du système", "isCorrect": False},
                        {"text": "L'opérateur doit systématiquement doubler le temps de pressage prescrit par le fabricant de colle lorsque l'hydrométrie ambiante est faible", "isCorrect": False},
                        {"text": "Les traverses doivent être bridées avant les montants pour autoriser l'échappement latéral de la colle vinylique", "isCorrect": False}
                    ],
                    "correction": "Sur une cadreuse, la pression doit être centrée sur l'axe neutre des profilés. Un désaxement des sabots de pressage vers le parement ou le contreface génère un couple de basculement qui fait flamber l'assemblage et ruine la planéité du cadre."
                },
                {
                    "questionNumber": 69,
                    "question": "Que caractérise le grammage lors de l'application d'un vernis de finition ?",
                    "answerOptions": [
                        {"text": "Il exprime la quantité de produit humide déposée par mètre carré de surface lors d'une passe de pulvérisation afin de contrôler l'épaisseur du feuil", "isCorrect": True},
                        {"text": "Il désigne la proportion exacte du mélange chimique entre le vernis polyuréthane de base et le durcisseur isocyanate selon les recommandations strictes imposées par la fiche de sécurité du fabricant industriel de laque", "isCorrect": False},
                        {"text": "Il correspond au rapport de densité entre l'extrait sec résiduel après évaporation et le volume initialement contenu dans le pot", "isCorrect": False},
                        {"text": "Il détermine la taille moyenne des grains abrasifs recommandés pour procéder à l'égrenage manuel de la sous-couche", "isCorrect": False}
                    ],
                    "correction": "Le grammage se mesure en grammes par mètre carré. Il détermine l'épaisseur de la couche humide pulvérisée, garantissant ainsi un tendu optimal sans risque de coulure et respectant la quantité de matière imposée par la fiche technique."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment fonctionne une presse à membrane sous vide pour le placage en forme ?",
                    "answerOptions": [
                        {"text": "Une pompe extrait l'air sous une membrane en silicone très souple qui vient alors épouser intimement le moule et presser uniformément le placage grâce à la seule pression atmosphérique extérieure", "isCorrect": True},
                        {"text": "Le système injecte un fluide hydraulique chauffé à haute température directement dans des poches étanches disposées tout autour du moule en bois afin de forcer mécaniquement le panneau dérivé à se courber brutalement selon le rayon désiré par le concepteur", "isCorrect": False},
                        {"text": "Deux plateaux en acier massif viennent écraser la matière de façon asymétrique pour contraindre les fibres de la face supérieure à s'étirer", "isCorrect": False},
                        {"text": "L'appareil utilise une succession de galets presseurs pneumatiques qui effectuent des allers-retours rapides sur le panneau", "isCorrect": False}
                    ],
                    "correction": "La presse à membrane utilise la dépression. En faisant le vide sous la couverture en caoutchouc ou en silicone, la pression atmosphérique exerce une force de placage homogène d'environ un kilogramme par centimètre carré sur toutes les courbures de la pièce."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel outil électroportatif est requis pour usiner un assemblage de type Clamex P ?",
                    "answerOptions": [
                        {"text": "Une fraiseuse à rainurer spécifique avec système de va-et-vient", "isCorrect": True},
                        {"text": "Une défonceuse équipée d'une mèche à queue d'aronde inversée", "isCorrect": False},
                        {"text": "Une mortaiseuse à mèche oscillante pour perçages profonds", "isCorrect": False},
                        {"text": "Une perceuse multilignes avec entraxe standard de trente-deux millimètres", "isCorrect": False}
                    ],
                    "correction": "Le système d'assemblage démontable P-System de Lamello nécessite une fraiseuse dédiée type Zeta P2. L'outil circulaire plonge puis effectue un décalage vertical automatisé pour créer la rainure à profil en T nécessaire à l'ancrage."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est l'objectif de l'égrenage après l'application d'un fond dur isolant ?",
                    "answerOptions": [
                        {"text": "Couper les fibres du bois redressées par l'humidité du produit", "isCorrect": True},
                        {"text": "Boucher les pores profonds des essences à gros vaisseaux", "isCorrect": False},
                        {"text": "Augmenter l'épaisseur finale du feuil protecteur appliqué", "isCorrect": False},
                        {"text": "Raviver la coloration de la teinte à l'eau préalablement appliquée", "isCorrect": False}
                    ],
                    "correction": "L'application de la première couche liquide humidifie le bois, ce qui provoque le relèvement rugueux des extrémités des fibres tranchées. L'égrenage avec un abrasif fin arasera ces fibres engluées dans la résine pour offrir une surface lisse au vernis de finition."
                },
                {
                    "questionNumber": 73,
                    "question": "Pourquoi doit-on réaliser un avant-trou dans un chant en panneau MDF avant vissage ?",
                    "answerOptions": [
                        {"text": "Pour éviter le clivage des strates du panneau par l'âme de la vis", "isCorrect": True},
                        {"text": "Pour garantir une bonne conductivité thermique lors de l'assemblage", "isCorrect": False},
                        {"text": "Pour permettre à la colle d'atteindre le cœur des fibres synthétiques", "isCorrect": False},
                        {"text": "Pour faciliter le démontage ultérieur de la quincaillerie d'agencement", "isCorrect": False}
                    ],
                    "correction": "Le panneau MDF présente une faible cohésion interne face aux efforts d'écartement dans son épaisseur. Le volume déplacé par l'âme de la vis crée une contrainte radiale qui clive invariablement le chant si le trou pilote n'a pas enlevé la matière correspondante."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel type de colle est réversible sous l'action de la chaleur ?",
                    "answerOptions": [
                        {"text": "La colle thermofusible à base de copolymères", "isCorrect": True},
                        {"text": "La colle polyuréthane monocomposant réactive", "isCorrect": False},
                        {"text": "La colle résorcine phénolique à froid", "isCorrect": False},
                        {"text": "La colle époxy bi-composante de structure", "isCorrect": False}
                    ],
                    "correction": "Les colles thermofusibles utilisées pour le placage de chants sont des thermoplastiques. Elles se liquéfient sous l'action de la chaleur, se solidifient en refroidissant, et peuvent être de nouveau ramollies par un pistolet thermique, contrairement aux thermodurcissables."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel phénomène apparaît si l'on applique un vernis en phase aqueuse par température très basse ?",
                    "answerOptions": [
                        {"text": "Un blanchiment lié à la mauvaise coalescence du film", "isCorrect": True},
                        {"text": "Une évaporation instantanée des co-solvants organiques", "isCorrect": False},
                        {"text": "Un écaillage de la couche d'impression hydrofuge", "isCorrect": False},
                        {"text": "Une polymérisation accélérée rendant le tendu imparfait", "isCorrect": False}
                    ],
                    "correction": "La température minimale de formation de film des vernis hydrodiluables se situe autour de 15 degrés. En dessous, les particules acryliques ne fusionnent pas correctement lors de l'évaporation de l'eau, rendant le vernis farineux et blanchâtre."
                },
                {
                    "questionNumber": 76,
                    "question": "Lors de la pose d'une serrure à mortaiser, que désigne la cote d'axe ?",
                    "answerOptions": [
                        {"text": "La distance entre la têtière et l'axe du fouillot de béquille", "isCorrect": True},
                        {"text": "L'entraxe vertical entre la clé et le cylindre de sécurité", "isCorrect": False},
                        {"text": "La profondeur totale du coffre encastré dans le montant", "isCorrect": False},
                        {"text": "La largeur du pêne dormant sortant de la gâche mécanique", "isCorrect": False}
                    ],
                    "correction": "La cote d'axe est une dimension fondamentale de perçage en serrurerie. Elle mesure la distance horizontale exacte séparant la face extérieure affleurante de la têtière et le centre du trou carré recevant l'axe de la poignée."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel jeu d'arasement doit-on observer sur un assemblage tenon mortaise bien réglé ?",
                    "answerOptions": [
                        {"text": "Aucun jeu pour assurer le serrage de l'épaulement sur la pièce", "isCorrect": True},
                        {"text": "Un jeu constant de deux millimètres pour l'épaisseur de la colle", "isCorrect": False},
                        {"text": "Un jeu de dilatation variable en fonction du fil du bois massif", "isCorrect": False},
                        {"text": "Un espace de dégagement pour les excédents de résine phénolique", "isCorrect": False}
                    ],
                    "correction": "L'arasement correspondant à la base de la joue du tenon doit plaquer intimement, sans le moindre jeu, contre la surface de la pièce mortaisée pour assurer la rigidité géométrique de l'équerrage et l'esthétique du joint vu."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle opération de maintenance est vitale sur le bac à colle d'une plaqueuse en fin de poste ?",
                    "answerOptions": [
                        {"text": "Diminuer la consigne de chauffe pour éviter la carbonisation du produit", "isCorrect": True},
                        {"text": "Vider intégralement la cuve avec un solvant de nettoyage très agressif", "isCorrect": False},
                        {"text": "Immerger le rouleau encolleur dans un bain d'huile minérale neutre", "isCorrect": False},
                        {"text": "Désactiver les palpeurs de pression du premier galet maroufleur", "isCorrect": False}
                    ],
                    "correction": "Les colles EVA ou PUR cuisent si elles sont maintenues à 200 degrés sans avancement de panneaux. Passer la machine en mode veille autour de 130 degrés empêche la dégradation thermique et la formation de résidus carbonisés qui bloqueraient les engrenages."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle est l'utilité du fil zigzag collant lors du jointage des feuilles de placage ?",
                    "answerOptions": [
                        {"text": "Maintenir les bords étroitement joints sans générer de surépaisseur", "isCorrect": True},
                        {"text": "Apporter un agent durcisseur pour la polymérisation sous la presse", "isCorrect": False},
                        {"text": "Imperméabiliser le joint pour prévenir la pénétration du vernis", "isCorrect": False},
                        {"text": "Absorber les variations dimensionnelles lors du pressage à froid", "isCorrect": False}
                    ],
                    "correction": "La jointeuse dépose un fil thermofusible en zigzag qui fond et sèche instantanément sur l'envers. Il maintient solidement les feuilles bord à bord pendant la manipulation sans créer de bosse de calage sous les plateaux de la presse à chaud."
                },
                {
                    "questionNumber": 80,
                    "question": "Sur une ponceuse large bande, quel agrégat permet de poncer un panneau plaqué fin ?",
                    "answerOptions": [
                        {"text": "Le patin pneumatique ou électronique fractionné", "isCorrect": True},
                        {"text": "Le rouleau contacteur en acier rainuré de gros diamètre", "isCorrect": False},
                        {"text": "La brosse métallique cylindrique à rotation inverse", "isCorrect": False},
                        {"text": "L'arbre toupie transversal à plaquettes carbure interchangeables", "isCorrect": False}
                    ],
                    "correction": "Le patin de ponçage est équipé d'une feutrine amortisseuse. Contrairement au rouleau dur qui usine brutalement à l'épaisseur, le patin suit les infimes déformations naturelles du panneau, ponçant uniquement la surface sans risquer de percer le placage de quelques dixièmes de millimètre."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : Préparation de chantier, pose et agencement final (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : Préparation de chantier, pose et agencement final",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel niveau d'étanchéité garantit un fond de joint mousse ?",
                    "answerOptions": [
                        {"text": "L'étanchéité à l'air", "isCorrect": True},
                        {"text": "L'isolation thermique périphérique", "isCorrect": False},
                        {"text": "La résistance mécanique aux chocs", "isCorrect": False},
                        {"text": "Le drainage des eaux d'infiltration", "isCorrect": False}
                    ],
                    "correction": "Le fond de joint rond en mousse polyéthylène à cellules fermées sert de support au mastic élastomère. Il assure le calfeutrement à l'air tout en évitant l'adhérence du mastic sur la troisième face au fond, condition requise pour conserver son élasticité."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment gérer les tolérances du gros œuvre lors de la pose d'un agencement mural encastré ?",
                    "answerOptions": [
                        {"text": "En intégrant des fileurs d'ajustement surdimensionnés qui seront délignés sur place selon le relevé tridimensionnel", "isCorrect": True},
                        {"text": "En contraignant mécaniquement la structure du meuble à l'aide de vérins de force pneumatiques jusqu'à ce que les panneaux de particules se déforment pour épouser exactement le galbe du mur porteur", "isCorrect": False},
                        {"text": "En remplissant systématiquement tous les interstices avec de la mousse polyuréthane expansive", "isCorrect": False},
                        {"text": "En refusant la pose jusqu'à la reprise complète de la maçonnerie par le plaquiste", "isCorrect": False}
                    ],
                    "correction": "Le fileur est une pièce d'adaptation primordiale en agencement. Prévu avec une surcote lors de la conception en atelier, il est ajusté à la scie plongeante et au rabot électrique sur le chantier pour épouser le faux aplomb et les irrégularités de la maçonnerie."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel outil garantit le transfert d'un faux aplomb sur un fileur d'agencement ?",
                    "answerOptions": [
                        {"text": "Un trusquin à molette", "isCorrect": True},
                        {"text": "Un fil à plomb conique", "isCorrect": False},
                        {"text": "Un cordeau traceur à poudre", "isCorrect": False},
                        {"text": "Une règle à bulle tubulaire", "isCorrect": False}
                    ],
                    "correction": "En plaquant le fileur verticalement contre le mur, l'agenceur utilise un trusquin ou un compas à pointe sèche pour copier le profil exact de la paroi sur la pièce de bois, traçant la ligne de coupe rigoureusement parallèle aux défauts du mur."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle fixation est préconisée pour ancrer une ossature dans un mur en brique creuse ?",
                    "answerOptions": [
                        {"text": "Une cheville à expansion par verrouillage de forme", "isCorrect": True},
                        {"text": "Un goujon d'ancrage à frapper en acier zingué", "isCorrect": False},
                        {"text": "Une pointe en acier trempé à tête plate", "isCorrect": False},
                        {"text": "Une vis autotaraudeuse à double filetage asymétrique", "isCorrect": False}
                    ],
                    "correction": "Dans les matériaux creux, on recourt à des chevilles métalliques à déformation ou des chevilles plastiques à nœud. Elles s'écartent ou se replient en étoile derrière la paroi mince de la brique, créant un verrouillage de forme mécanique positif."
                },
                {
                    "questionNumber": 85,
                    "question": "Que matérialise le trait de niveau un mètre ?",
                    "answerOptions": [
                        {"text": "Le sol fini", "isCorrect": True},
                        {"text": "Le plafond suspendu", "isCorrect": False},
                        {"text": "La hauteur des poignées", "isCorrect": False},
                        {"text": "L'axe des menuiseries", "isCorrect": False}
                    ],
                    "correction": "Le trait de niveau un mètre est tracé par le maçon à exactement mille millimètres au-dessus du niveau du sol fini théorique. Il sert de repère absolu et universel de référence altimétrique pour tous les corps d'état lors de l'implantation des ouvrages."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est la fonction du compriband dans la pose d'une menuiserie extérieure ?",
                    "answerOptions": [
                        {"text": "Il assure l'étanchéité à la pluie battante entre la maçonnerie et le dormant du châssis", "isCorrect": True},
                        {"text": "Il sert de rupteur de pont thermique absolu entre le doublage intérieur en plaque de plâtre et le rejet d'eau extérieur en aluminium pour éviter la moindre condensation hivernale", "isCorrect": False},
                        {"text": "Il garantit la résistance à l'effraction en bloquant l'accès aux vis de fixation", "isCorrect": False},
                        {"text": "Il permet de maintenir le dormant de niveau pendant le perçage des équerres", "isCorrect": False}
                    ],
                    "correction": "Le joint mousse imprégné précomprimé se décompresse lentement une fois le rouleau libéré. Il vient combler l'espace de jeu entre la maçonnerie et le profilé, formant une barrière normée contre les infiltrations d'eau et de vent."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel DTU régit les travaux de menuiserie en bois et agencement intérieur ?",
                    "answerOptions": [
                        {"text": "Le DTU 36.1", "isCorrect": True},
                        {"text": "Le DTU 43.4", "isCorrect": False},
                        {"text": "Le DTU 51.2", "isCorrect": False},
                        {"text": "Le DTU 25.41", "isCorrect": False}
                    ],
                    "correction": "Le Document Technique Unifié 36.1 fixe les clauses techniques types pour la mise en œuvre des ouvrages en bois. Il dicte les règles de l'art obligatoires, les tolérances d'équerrage admissibles et les sections minimales de vissage."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment compenser les inégalités du sol sous un caisson de cuisine ?",
                    "answerOptions": [
                        {"text": "Par des pieds vérins réglables en ABS", "isCorrect": True},
                        {"text": "Par des cales en bois massif clouées", "isCorrect": False},
                        {"text": "En sciant directement la base des caissons", "isCorrect": False},
                        {"text": "En réalisant un ragréage partiel au ciment", "isCorrect": False}
                    ],
                    "correction": "Les agencements modernes reposent sur des pieds plastiques cylindriques à visser. Leur embase filetée permet un réglage fin et indépendant de la hauteur, garantissant la stricte planéité du plan de travail avant de clipser la plinthe cache-pieds."
                },
                {
                    "questionNumber": 89,
                    "question": "Pourquoi utiliser un niveau laser rotatif plutôt qu'un niveau tubulaire sur un grand chantier ?",
                    "answerOptions": [
                        {"text": "Il génère un plan de référence continu sur l'ensemble de la pièce pour aligner plusieurs meubles", "isCorrect": True},
                        {"text": "Il permet de percer directement à travers les panneaux de particules mélaminés sans générer le moindre éclat grâce à un faisceau de lumière concentrée à très haute fréquence d'oscillation", "isCorrect": False},
                        {"text": "Il mesure automatiquement la densité des murs porteurs pour sélectionner la cheville appropriée", "isCorrect": False},
                        {"text": "Il calcule la quantité exacte de mastic silicone nécessaire pour réaliser le calfeutrement", "isCorrect": False}
                    ],
                    "correction": "Le laser rotatif balaie à trois cent soixante degrés pour matérialiser un plan horizontal ou vertical parfaitement de niveau. Cela permet de reporter des cotes de fixation très distantes pour des linéaires de rangement ou des banques d'accueil."
                },
                {
                    "questionNumber": 90,
                    "question": "Que contrôle-t-on avec un gabarit de perçage ?",
                    "answerOptions": [
                        {"text": "L'entraxe des trous", "isCorrect": True},
                        {"text": "L'épaisseur du panneau", "isCorrect": False},
                        {"text": "L'humidité du mur", "isCorrect": False},
                        {"text": "La tension du secteur", "isCorrect": False}
                    ],
                    "correction": "Un gabarit de perçage garantit la répétabilité parfaite de l'entraxe et du décalage par rapport au chant du panneau. Il élimine les erreurs de traçage manuel et accélère la pose des charnières, poignées et glissières."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle pièce de quincaillerie permet l'accrochage mural invisible d'un meuble haut ?",
                    "answerOptions": [
                        {"text": "Le boîtier d'accrochage à réglage tridimensionnel", "isCorrect": True},
                        {"text": "La patère en laiton massif profilé", "isCorrect": False},
                        {"text": "Le rail coulissant à galets en nylon", "isCorrect": False},
                        {"text": "La charnière piano en acier inoxydable", "isCorrect": False}
                    ],
                    "correction": "Les caissons suspendus viennent en prise sur une lisse métallique vissée au mur grâce à des boîtiers d'accrochage intégrés en fond de meuble. Leurs vis de réglage permettent d'aligner la hauteur et d'assurer le placage mural en charge."
                },
                {
                    "questionNumber": 92,
                    "question": "À quoi sert une cheville chimique dans un mur en parpaing creux ?",
                    "answerOptions": [
                        {"text": "À créer un scellement résistant par injection de résine dans un tamis perforé", "isCorrect": True},
                        {"text": "À dissoudre chimiquement le revêtement de finition du mur pour permettre un collage structurel de l'agencement directement sur la roche brute de la construction d'origine", "isCorrect": False},
                        {"text": "À empêcher la corrosion des tiges filetées dans les pièces soumises à de forts ruissellements", "isCorrect": False},
                        {"text": "À lubrifier le filetage du goujon pour faciliter le démontage futur de l'ouvrage d'agencement", "isCorrect": False}
                    ],
                    "correction": "La résine bi-composante est injectée dans une cheville tubulaire grillagée appelée tamis. La pâte extrudée déborde des mailles et durcit derrière les cloisons alvéolaires du bloc béton, verrouillant la tige filetée sans créer de force d'éclatement."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel jeu périphérique doit-on laisser lors de la pose d'un parquet flottant stratifié ?",
                    "answerOptions": [
                        {"text": "Huit à dix millimètres sur tout le pourtour", "isCorrect": True},
                        {"text": "Strictement aucun jeu de dilatation", "isCorrect": False},
                        {"text": "Trois centimètres minimum sous les plinthes", "isCorrect": False},
                        {"text": "Deux millimètres exclusivement côté fenêtre", "isCorrect": False}
                    ],
                    "correction": "Le complexe de sol stratifié gonfle et se rétracte selon la température et l'humidité de la pièce. Le vide périphérique maintenu par des cales de frappe de dix millimètres évite que le sol ne bute contre la maçonnerie et ne se soulève au centre."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment éviter l'éclatement du panneau lors du perçage traversant pour une poignée ?",
                    "answerOptions": [
                        {"text": "En appliquant une cale martyre fermement plaquée en sortie de foret", "isCorrect": True},
                        {"text": "En lubrifiant généreusement la mèche avec de l'huile de coupe", "isCorrect": False},
                        {"text": "En inversant le sens de rotation de la perceuse à mi-parcours", "isCorrect": False},
                        {"text": "En perçant exclusivement avec une inclinaison de quarante-cinq degrés", "isCorrect": False}
                    ],
                    "correction": "La contrainte de poussée du foret arrache la couche de mélamine en débouchant. Maintenir un martyr en chute de bois plaqué contre le parement de sortie maintient les fibres de surface et permet d'obtenir un perçage d'une propreté absolue."
                },
                {
                    "questionNumber": 95,
                    "question": "Que mesure l'humidimètre à pointes ?",
                    "answerOptions": [
                        {"text": "Le taux d'humidité", "isCorrect": True},
                        {"text": "Le point de rosée", "isCorrect": False},
                        {"text": "La densité du plâtre", "isCorrect": False},
                        {"text": "L'épaisseur du vernis", "isCorrect": False}
                    ],
                    "correction": "L'humidimètre de contact à pointes détermine la résistance électrique de l'eau contenue entre ses deux électrodes enfoncées dans le matériau. Cela valide que le support mural est suffisamment sec pour recevoir un habillage bois sans risque de moisissure."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle action est indispensable avant le serrage définitif des vis de liaison entre deux caissons ?",
                    "answerOptions": [
                        {"text": "Bloquer les chants avant parfaitement affleurants avec des serre-joints", "isCorrect": True},
                        {"text": "Démonter intégralement les façades et les tiroirs pour l'allégement", "isCorrect": False},
                        {"text": "Appliquer un cordon continu de mastic silicone sur les faces latérales", "isCorrect": False},
                        {"text": "Percer les trous de ventilation dans les fonds de panneaux isorel", "isCorrect": False}
                    ],
                    "correction": "Le couple de rotation de la vis engendre souvent un désaxement. Il faut contraindre mécaniquement les joues des caissons avec des pinces ou des serre-joints pour annuler les jeux d'affleurement en façade avant de lier les corps de meubles par perçage."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le rôle d'un espace tampon dans l'agencement d'un sas d'entrée public ?",
                    "answerOptions": [
                        {"text": "Créer une zone de transition thermique et aéraulique pour limiter les déperditions", "isCorrect": True},
                        {"text": "Stocker temporairement les panneaux d'agencement avant leur découpe définitive afin qu'ils s'acclimatent au taux d'hygrométrie de la pièce et ne subissent plus de retrait dimensionnel", "isCorrect": False},
                        {"text": "Masquer les tableaux électriques et les arrivées de plomberie disgracieuses du bâtiment", "isCorrect": False},
                        {"text": "Renforcer l'isolation acoustique des murs mitoyens face aux bruits de structure de l'immeuble", "isCorrect": False}
                    ],
                    "correction": "Les portes en enfilade d'un sas coupent les ponts thermiques liés à l'ouverture sur l'extérieur. Le volume d'air intercalé casse la pression des courants d'air froid et protège le climat intérieur de la zone de réception du bâtiment."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle précaution prendre lors du calage d'une menuiserie extérieure en tunnel ?",
                    "answerOptions": [
                        {"text": "Placer des cales imputrescibles au droit des points de fixation", "isCorrect": True},
                        {"text": "Utiliser exclusivement des cales en hêtre massif de fil", "isCorrect": False},
                        {"text": "Ne jamais caler la traverse basse pour permettre l'écoulement", "isCorrect": False},
                        {"text": "Fixer les cales avec des vis traversant le profilé de récupération", "isCorrect": False}
                    ],
                    "correction": "Les points d'ancrage exercent une traction sur le dormant qui pourrait le cintrer. Les cales de fond de feuillure, résistantes à l'écrasement et à l'humidité, doivent reprendre exactement l'effort de la vis pour garantir le rectiligne du cadre."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment s'assurer du parallélisme d'un placard sous un plafond rampant ?",
                    "answerOptions": [
                        {"text": "En relevant les cotes d'élévation à l'aide d'une fausse équerre et d'un niveau", "isCorrect": True},
                        {"text": "En appliquant systématiquement une formule de trigonométrie complexe basée sur l'épaisseur du placoplâtre multipliée par l'inclinaison de la charpente fermette de l'étage supérieur", "isCorrect": False},
                        {"text": "En montant les caissons de niveau pour ensuite combler le vide avec du plâtre projeté", "isCorrect": False},
                        {"text": "En pliant directement les rails métalliques du coulissant pour qu'ils épousent la toiture", "isCorrect": False}
                    ],
                    "correction": "Dans les combles, les angles de pente de toit varient d'une charpente à l'autre. Le menuisier trace un repère vertical strict au niveau à bulle, puis relève l'angle d'intersection réel avec la sous-face du placo au moyen d'une sauterelle, ou fausse équerre, pour régler sa scie plongeante."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel EPI est spécifiquement requis lors de l'utilisation d'un cloueur pneumatique de finition ?",
                    "answerOptions": [
                        {"text": "Des lunettes de sécurité à protection latérale", "isCorrect": True},
                        {"text": "Un masque filtrant respiratoire FFP3", "isCorrect": False},
                        {"text": "Des gants de manutention lourde en cuir", "isCorrect": False},
                        {"text": "Un harnais de maintien antichute au poste", "isCorrect": False}
                    ],
                    "correction": "Un pistolet pneumatique propulse les pointes en bande avec une grande énergie. Le risque critique d'accident oculaire réside dans la déviation imprévisible du projectile lorsqu'il frappe un nœud ligneux très dense ou un fil métallique noyé dans le support."
                }
            ]
        }
    }
}