quiz_data = {
    "title": "CAP Carreleur",
    
    "description": "Base de données de 100 questions pour le CAP Carreleur. Les longueurs des réponses ont été uniformisées pour éviter tout biais.",
    
    "themes": {
        # THÈME 1
        1: {
            "name": "Hygiène, Sécurité et Réglementation (HSR)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel Équipement de Protection Individuelle (EPI) est indispensable lors de la coupe des carreaux à la carrelette électrique à eau ?",
                    "answerOptions": [
                        {"text": "Les lunettes de protection et les gants étanches pour éviter les projections.", "isCorrect": True, "key": "A"},
                        {"text": "Le casque antibruit pour l'atténuation des vibrations et des ondes sonores aiguës.", "isCorrect": False, "key": "B"},
                        {"text": "Le harnais de sécurité pour le travail en hauteur sur des échafaudages légers.", "isCorrect": False, "key": "C"},
                        {"text": "La combinaison de protection en matière ignifugée pour les travaux de soudure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les projections d'eau, de débris et la poussière de coupe sont les principaux dangers nécessitant des protections oculaires et cutanées."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le risque majeur lié à l'inhalation prolongée des poussières fines de ciment ou de silice lors du mélange des colles et joints ?",
                    "answerOptions": [
                        {"text": "Le risque de maladies respiratoires graves, telles que la silicose et l'asthme chronique.", "isCorrect": True, "key": "A"},
                        {"text": "Le risque d'intoxication alimentaire et d'infection virale aiguë (grippe).", "isCorrect": False, "key": "B"},
                        {"text": "Le risque d'électrocution dû à une humidité excessive dans l'air ambiant.", "isCorrect": False, "key": "C"},
                        {"text": "Le risque de brûlures chimiques sur la peau (dermite irritative ou allergique).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le port d'un masque FFP3 est nécessaire pour éviter l'inhalation des fines particules de silice cristalline contenues dans les produits cimentaires."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la méthode la plus sûre pour manipuler des sacs de colle ou de mortier lourds (supérieurs à 25 kg) ?",
                    "answerOptions": [
                        {"text": "Utiliser un moyen de levage mécanique ou demander de l'aide pour préserver le dos.", "isCorrect": True, "key": "A"},
                        {"text": "Fléchir les genoux et soulever avec le dos droit pour maximiser la force musculaire.", "isCorrect": False, "key": "B"},
                        {"text": "Travailler seul et soulever les sacs par l'arrière de façon dynamique.", "isCorrect": False, "key": "C"},
                        {"text": "Les pousser ou les tirer sur le sol sans les soulever, en utilisant uniquement les bras.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les Troubles Musculo-Squelettiques (TMS) sont fréquents. La prévention passe par l'utilisation d'aides à la manutention et la bonne posture."
                },
                {
                    "questionNumber": 4,
                    "question": "Que doit-on faire obligatoirement avant d'utiliser une machine électrique (malaxeur, carrelette) sur un chantier ?",
                    "answerOptions": [
                        {"text": "Vérifier l'état du câble, de la prise et la présence d'une protection différentielle adéquate.", "isCorrect": True, "key": "A"},
                        {"text": "Appliquer un produit imperméabilisant sur le carter de la machine pour la protéger.", "isCorrect": False, "key": "B"},
                        {"text": "Démonter le carter de protection de la lame pour en faciliter le nettoyage et la coupe.", "isCorrect": False, "key": "C"},
                        {"text": "Lubrifier toutes les pièces en rotation du moteur avec une huile minérale spéciale.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'électricité sur un chantier humide est une source de danger majeure. Le contrôle des équipements et des protections électriques est primordial."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le rôle du Plan Particulier de Sécurité et de Protection de la Santé (PPSPS) sur un chantier important ?",
                    "answerOptions": [
                        {"text": "Il définit les mesures de prévention des risques spécifiques à ce chantier pour tous les intervenants.", "isCorrect": True, "key": "A"},
                        {"text": "Il fixe uniquement le calendrier de livraison des matériaux et l'organisation du stockage.", "isCorrect": False, "key": "B"},
                        {"text": "Il sert de base de calcul pour l'évaluation des coûts de main d'œuvre et des primes de risque.", "isCorrect": False, "key": "C"},
                        {"text": "Il répertorie la liste complète des qualifications professionnelles de chaque ouvrier présent.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le PPSPS (ou le Plan de Prévention) est un document obligatoire qui analyse les risques et détermine les moyens de les éviter."
                },
                {
                    "questionNumber": 6,
                    "question": "Qu'est-ce que le 'Décollement des plaques' (DP) en termes de défaut de pose ?",
                    "answerOptions": [
                        {"text": "La désolidarisation du carreau et de son support suite à une mauvaise adhérence.", "isCorrect": True, "key": "A"},
                        {"text": "La fissure des carreaux causée par un choc thermique intense et rapide.", "isCorrect": False, "key": "B"},
                        {"text": "L'apparition de traces blanches sur le joint (efflorescence saline).", "isCorrect": False, "key": "C"},
                        {"text": "Le retrait des joints en périphérie, laissant apparaître le support ou le film.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le décollement est souvent dû à un encollage insuffisant (taux de transfert de colle trop faible) ou à une mauvaise préparation du support."
                },
                {
                    "questionNumber": 7,
                    "question": "Pourquoi doit-on s'assurer que le support de pose est parfaitement sec avant d'appliquer le mortier-colle ?",
                    "answerOptions": [
                        {"text": "L'humidité du support nuit à la prise et à l'adhérence de la colle (risque de décollement).", "isCorrect": True, "key": "A"},
                        {"text": "Le support humide accélère la prise de la colle et rend le temps de manipulation trop court.", "isCorrect": False, "key": "B"},
                        {"text": "L'eau favorise l'apparition d'une efflorescence (dépôt blanc de sel) très visible sur les carreaux.", "isCorrect": False, "key": "C"},
                        {"text": "Cela permet d'éviter la formation de bulles d'air sous le carrelage fraîchement posé.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'eau ralentit la prise des liants hydrauliques (ciment) et compromet la liaison chimique entre la colle et le support."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la principale fonction d'un primaire d'accrochage avant l'application du carrelage ?",
                    "answerOptions": [
                        {"text": "Réguler la porosité du support et améliorer l'adhérence des produits cimentaires.", "isCorrect": True, "key": "A"},
                        {"text": "Créer une surface parfaitement plane (rattrapage de niveau).", "isCorrect": False, "key": "B"},
                        {"text": "Remplacer l'étanchéité à l'eau de la pièce humide (système S.P.E.C. ou S.E.L.).", "isCorrect": False, "key": "C"},
                        {"text": "Servir de couche de finition décorative, sans nécessiter d'être recouvert ensuite.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le primaire d'accrochage est essentiel, notamment sur des supports non absorbants (anciens carrelages) ou très absorbants (plâtre)."
                },
                {
                    "questionNumber": 9,
                    "question": "Comment doit-on nettoyer et éliminer les résidus de colle et de joints après la fin des travaux de carrelage ?",
                    "answerOptions": [
                        {"text": "Par un nettoyage chimique avec des décapants spécifiques (acides) après avoir balayé les gros déchets.", "isCorrect": True, "key": "A"},
                        {"text": "Par un ponçage manuel très abrasif à l'aide d'une meuleuse d'angle, sans eau.", "isCorrect": False, "key": "B"},
                        {"text": "Par un lavage régulier à grande eau avec de la javel pure (hypochlorite de sodium).", "isCorrect": False, "key": "C"},
                        {"text": "Par un séchage au décapeur thermique avant de les gratter avec un couteau lourd.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les résidus cimentaires nécessitent un décapant acide, à manipuler avec précautions (EPI), et à rincer abondamment."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la règle de base concernant l'usage du matériel professionnel (carrelette, malaxeur, etc.) ?",
                    "answerOptions": [
                        {"text": "Utiliser l'équipement conformément aux instructions du fabricant et uniquement si on est formé.", "isCorrect": True, "key": "A"},
                        {"text": "L'équipement est interchangeable et peut être utilisé par n'importe quel ouvrier sans formation.", "isCorrect": False, "key": "B"},
                        {"text": "Le matériel doit être mis hors service dès qu'une rayure apparaît sur l'extérieur de la machine.", "isCorrect": False, "key": "C"},
                        {"text": "La maintenance et les réglages ne doivent être effectués que par le chef de chantier lui-même.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La mauvaise utilisation des outils est l'une des principales causes d'accidents sur les chantiers."
                },
                {
                    "questionNumber": 11,
                    "question": "Que signifie la norme européenne 'UPEC' pour un carrelage destiné à un logement individuel ?",
                    "answerOptions": [
                        {"text": "Elle classe le carreau selon l'Usure, le Poinçonnement, la résistance à l'Eau et aux Agents Chimiques.", "isCorrect": True, "key": "A"},
                        {"text": "Elle garantit un prix unique du carreau pour l'ensemble du marché européen (coût).", "isCorrect": False, "key": "B"},
                        {"text": "Elle mesure l'épaisseur du carreau, son poids total et son pouvoir isolant thermique.", "isCorrect": False, "key": "C"},
                        {"text": "Elle atteste du pays de fabrication et du respect des lois sociales du travail.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le classement UPEC est fondamental pour choisir le carrelage adapté à la destination (sol, mur, trafic, pièce humide, etc.)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le risque de travailler sur un sol fraîchement carrelé et non sec ?",
                    "answerOptions": [
                        {"text": "Le déplacement des carreaux et l'altération des joints, ce qui compromet la planéité finale.", "isCorrect": True, "key": "A"},
                        {"text": "Le risque d'intoxication aux vapeurs de colle et de produits d'étanchéité toxiques.", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de casse de la lame de la carrelette manuelle, à cause de la vibration du sol.", "isCorrect": False, "key": "C"},
                        {"text": "L'apparition rapide et irréversible de taches rouges sur le revêtement de carreaux.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Il faut respecter le temps de séchage indiqué par le fabricant avant de marcher sur l'ouvrage. Il est souvent de 24 heures minimum."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est le danger d'utiliser des outils de coupe (carrelette manuelle) avec des gants sales ou abîmés ?",
                    "answerOptions": [
                        {"text": "Le manque de précision de la coupe et le risque accru de glissement sur l'outil.", "isCorrect": True, "key": "A"},
                        {"text": "Le risque de rouiller rapidement la poignée de la pince à carreaux.", "isCorrect": False, "key": "B"},
                        {"text": "L'encrassement du mortier-colle dans la cuve du malaxeur.", "isCorrect": False, "key": "C"},
                        {"text": "Le risque de contamination des carreaux par des micro-organismes (bactéries).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les gants (s'ils sont adaptés) protègent des coupures mais ne doivent pas nuire à la dextérité. Le risque de glissement est critique."
                },
                {
                    "questionNumber": 14,
                    "question": "Que doit-on faire de tous les déchets (carreaux cassés, sacs de ciment vides) en fin de journée de travail ?",
                    "answerOptions": [
                        {"text": "Les collecter et les trier pour les évacuer vers une décharge spécialisée ou une benne adaptée.", "isCorrect": True, "key": "A"},
                        {"text": "Les laisser sur place mais les regrouper dans un coin pour le ramassage ultérieur par le client.", "isCorrect": False, "key": "B"},
                        {"text": "Les brûler directement sur place, en faisant attention à la fumée toxique et aux risques d'incendie.", "isCorrect": False, "key": "C"},
                        {"text": "Les enterrer dans le jardin du client si le chantier est en extérieur pour les dissimuler.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gestion des déchets est une obligation légale (tri, traçabilité) et environnementale (recyclage des gravats)."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est l'objectif du 'Guide des Bonnes Pratiques Carrelage' dans le métier ?",
                    "answerOptions": [
                        {"text": "Définir les règles de l'art, les normes et les DTU pour garantir la qualité de l'ouvrage.", "isCorrect": True, "key": "A"},
                        {"text": "Fixer le prix de la main d'œuvre horaire pour les travaux de carrelage.", "isCorrect": False, "key": "B"},
                        {"text": "Promouvoir les nouveaux modèles de carreaux et les tendances du marché.", "isCorrect": False, "key": "C"},
                        {"text": "Documenter l'historique des techniques de pose anciennes et non utilisées aujourd'hui.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les DTU (Documents Techniques Unifiés) sont les références qui définissent les règles professionnelles à respecter."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle doit être la largeur minimale d'un joint de fractionnement pour un carrelage intérieur ?",
                    "answerOptions": [
                        {"text": "Elle dépend du carreau mais est généralement au minimum de 2 mm pour les joints ordinaires.", "isCorrect": True, "key": "A"},
                        {"text": "Elle doit toujours être égale à 5 mm, quelle que soit la dimension du carreau.", "isCorrect": False, "key": "B"},
                        {"text": "Elle ne doit jamais excéder 1 mm afin de rendre l'ouvrage plus esthétique.", "isCorrect": False, "key": "C"},
                        {"text": "Elle doit être de 10 mm, comme les joints de dilatation prévus pour les grandes surfaces.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La largeur des joints est nécessaire pour absorber les mouvements du support et des carreaux. Elle varie selon les normes et les dimensions des carreaux."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le risque de ne pas réaliser de joint périphérique (joint de dilatation) entre le carrelage et le mur ?",
                    "answerOptions": [
                        {"text": "Le flambage ou le décollement du carrelage dû à la dilatation de l'ensemble.", "isCorrect": True, "key": "A"},
                        {"text": "La prolifération des mousses et lichens sur le mur adjacent au carrelage.", "isCorrect": False, "key": "B"},
                        {"text": "Une mauvaise évacuation de l'eau en cas d'inondation de la pièce posée.", "isCorrect": False, "key": "C"},
                        {"text": "La formation de bulles d'air sous le carrelage, créant des vides dans la masse.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le joint périphérique doit être laissé libre pour permettre l'expansion du revêtement. Il est généralement rempli d'un matériau souple (silicone ou mousse)."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelles sont les conditions de température à respecter pour l'application d'un mortier-colle standard ?",
                    "answerOptions": [
                        {"text": "La température du support et de l'air ambiant doit être comprise entre +5°C et +30°C.", "isCorrect": True, "key": "A"},
                        {"text": "La température doit être la plus basse possible (proche de 0°C) pour ralentir la prise du ciment.", "isCorrect": False, "key": "B"},
                        {"text": "Il n'y a pas de contrainte de température, sauf en cas de gel intense pour l'ouvrage.", "isCorrect": False, "key": "C"},
                        {"text": "La température idéale est supérieure à 40°C pour accélérer le séchage de l'eau contenue dans la colle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les liants hydrauliques nécessitent une température minimale pour que la réaction chimique (hydratation) se produise correctement."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'intérêt d'utiliser des croisillons (ou des cales) lors de la pose des carreaux ?",
                    "answerOptions": [
                        {"text": "Assurer un espacement régulier des joints et maintenir le carreau dans sa position exacte.", "isCorrect": True, "key": "A"},
                        {"text": "Remplacer le primaire d'accrochage pour les supports très lisses (anciens revêtements).", "isCorrect": False, "key": "B"},
                        {"text": "Servir de surface antidérapante provisoire pour pouvoir marcher sur l'ouvrage.", "isCorrect": False, "key": "C"},
                        {"text": "Éviter la projection d'eau et de débris lors de la découpe de la céramique.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les croisillons garantissent l'uniformité du joint, ce qui est critique pour l'esthétique finale et la solidité de l'ensemble."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le risque lié à une exposition prolongée au bruit intense de la carrelette électrique ?",
                    "answerOptions": [
                        {"text": "Des lésions irréversibles de l'oreille interne (surdité) si le casque antibruit n'est pas porté.", "isCorrect": True, "key": "A"},
                        {"text": "Un risque accru de tendinites et de Troubles Musculo-Squelettiques de l'avant-bras.", "isCorrect": False, "key": "B"},
                        {"text": "L'apparition rapide de vertiges et de nausées, dues aux vibrations du moteur.", "isCorrect": False, "key": "C"},
                        {"text": "Une coloration anormale de la peau exposée aux ondes acoustiques du moteur électrique.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le port d'un casque de protection auditive est obligatoire lors de l'utilisation d'outils bruyants."
                }
            ]
        },
        # THÈME 2
        2: {
            "name": "Matériaux (Carreaux, Colles, Joints)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "La Faïence se caractérise par une forte porosité. Pour quelle raison est-elle principalement utilisée ?",
                    "answerOptions": [
                        {"text": "Pour les murs intérieurs (revêtement mural) car elle est facile à couper et esthétique.", "isCorrect": True, "key": "A"},
                        {"text": "Pour les sols extérieurs, grâce à sa résistance au gel et à l'abrasion du trafic lourd.", "isCorrect": False, "key": "B"},
                        {"text": "Pour les plans de travail, en raison de sa dureté élevée et sa faible porosité.", "isCorrect": False, "key": "C"},
                        {"text": "Pour les pièces humides comme la douche car elle résiste à l'eau stagnante et aux produits acides.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Sa forte porosité (E > 10%) la rend sensible au gel et à l'eau, elle ne convient donc pas pour le sol ou l'extérieur."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la principale caractéristique d'un Grès Cérame, le rendant adapté aux sols extérieurs et aux lieux à fort trafic ?",
                    "answerOptions": [
                        {"text": "Sa très faible porosité (E ≤ 0,5%) le rendant résistant au gel, à l'usure et aux chocs.", "isCorrect": True, "key": "A"},
                        {"text": "Sa grande flexibilité et son élasticité, lui permettant de se plier sans se rompre sous la charge.", "isCorrect": False, "key": "B"},
                        {"text": "Sa texture en terre cuite naturelle, assurant une isolation phonique importante.", "isCorrect": False, "key": "C"},
                        {"text": "Sa surface naturellement très glissante (faible coefficient d'adhérence) à l'état mouillé.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le grès cérame est le carreau le plus résistant. Il est pressé à haute pression et cuit à haute température, ce qui le rend non poreux."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel type de colle est utilisé lorsque le support est neuf et cimentaire (chape traditionnelle) ?",
                    "answerOptions": [
                        {"text": "Un mortier-colle standard à liant hydraulique (à base de ciment), de classe C1 ou C2.", "isCorrect": True, "key": "A"},
                        {"text": "Une colle époxydique (réactive à deux composants) pour les supports anciens et très lisses.", "isCorrect": False, "key": "B"},
                        {"text": "Une colle en pâte prête à l'emploi (dispersion) pour les carrelages très lourds et les sols.", "isCorrect": False, "key": "C"},
                        {"text": "Un joint de dilatation souple, utilisé pour le rattrapage des fissures importantes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les colles cimentaires sont les plus courantes et conviennent à la majorité des supports absorbants."
                },
                {
                    "questionNumber": 24,
                    "question": "Pourquoi doit-on utiliser une colle 'fluide' (améliorée, classe C2-S1 ou C2-S2) pour les carreaux de grande dimension (> 60x60 cm) ?",
                    "answerOptions": [
                        {"text": "Pour garantir un 'double encollage' immédiat (et obligatoire) et assurer un transfert optimal de colle (≥ 90%).", "isCorrect": True, "key": "A"},
                        {"text": "Pour réduire le temps de séchage entre l'encollage du support et la pose du carreau lourd.", "isCorrect": False, "key": "B"},
                        {"text": "Pour pouvoir poser les carreaux sans laisser de joint entre eux (pose bord à bord).", "isCorrect": False, "key": "C"},
                        {"text": "Pour faciliter l'incorporation de pigments colorés dans la colle avant le malaxage de l'ensemble.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le double encollage est obligatoire pour les grands formats et les carreaux extérieurs. La colle fluide s'étale mieux et limite la formation de vides."
                },
                {
                    "questionNumber": 25,
                    "question": "Qu'est-ce qu'une 'efflorescence' sur les joints et comment l'éviter lors de la réalisation ?",
                    "answerOptions": [
                        {"text": "Un dépôt blanchâtre de sels solubles. On l'évite en utilisant peu d'eau lors du nettoyage des joints.", "isCorrect": True, "key": "A"},
                        {"text": "Un décollement du joint causé par une température ambiante trop basse pendant la prise.", "isCorrect": False, "key": "B"},
                        {"text": "Une coloration bleue du joint due à la présence de métaux lourds dans le ciment.", "isCorrect": False, "key": "C"},
                        {"text": "Une fissure de la surface du joint causée par un choc mécanique ou une chute d'objet lourd.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'efflorescence est un phénomène courant dû à la migration de sels minéraux vers la surface du joint par capillarité, transportés par l'eau en excès."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est l'indice de classement UPEC qui détermine la résistance d'un carreau à la rayure et à l'abrasion par frottement ?",
                    "answerOptions": [
                        {"text": "L'indice 'U' (Usure par frottement, de U2 à U4).", "isCorrect": True, "key": "A"},
                        {"text": "L'indice 'P' (Poinçonnement par chute d'objet).", "isCorrect": False, "key": "B"},
                        {"text": "L'indice 'E' (résistance à l'Eau).", "isCorrect": False, "key": "C"},
                        {"text": "L'indice 'C' (résistance aux Agents Chimiques).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'indice U (Usure) est crucial pour les lieux à fort trafic (commerces, couloirs publics, entrées)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le nom du carreau généralement épais et non émaillé, souvent utilisé pour les terrasses en raison de son aspect naturel ?",
                    "answerOptions": [
                        {"text": "La Terre Cuite (ou tomette), appréciée pour son esthétique rustique.", "isCorrect": True, "key": "A"},
                        {"text": "Le carreau de Faïence décoratif et très poreux.", "isCorrect": False, "key": "B"},
                        {"text": "Le Marbre poli (une roche calcaire) destiné aux sols intérieurs de luxe.", "isCorrect": False, "key": "C"},
                        {"text": "La pâte de verre, réservée uniquement à la confection de mosaïques très fines.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Terre Cuite est un produit naturel à base d'argile, nécessitant un traitement hydrofuge et oléofuge après la pose."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel type de joint est obligatoire dans les pièces soumises à une humidité extrême (piscines, douches à l'italienne, saunas) ?",
                    "answerOptions": [
                        {"text": "Le joint époxydique (réactif) ou un joint cimentier fortement amélioré pour l'étanchéité.", "isCorrect": True, "key": "A"},
                        {"text": "Le joint cimentaire standard de classe CG1 (le plus simple et le plus poreux).", "isCorrect": False, "key": "B"},
                        {"text": "Le joint souple en silicone (mastic) utilisé uniquement pour les joints périphériques.", "isCorrect": False, "key": "C"},
                        {"text": "Le joint de dilatation, rempli d'une mousse expansée pour absorber les chocs.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les joints époxydiques (à résine) sont non poreux, très résistants aux produits chimiques et parfaitement étanches, bien que plus difficiles à travailler."
                },
                {
                    "questionNumber": 29,
                    "question": "Qu'est-ce que l'indice 'R' pour les carreaux de sol, et que mesure-t-il ?",
                    "answerOptions": [
                        {"text": "Il mesure la résistance à la glissance (antidérapant) en fonction de l'inclinaison.", "isCorrect": True, "key": "A"},
                        {"text": "Il mesure la résistance au poinçonnement et aux chocs (R30, R40, etc.).", "isCorrect": False, "key": "B"},
                        {"text": "Il mesure la résistance au feu du carrelage et son pouvoir de combustion (incombustibilité).", "isCorrect": False, "key": "C"},
                        {"text": "Il mesure la résistance aux cycles de gel et de dégel pour l'usage extérieur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'indice R (de R9 à R13) est crucial pour les zones mouillées. Plus l'indice est élevé, plus le carreau est rugueux et antidérapant."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le nom donné au matériau de liaison le plus simple, mélange de ciment, de sable et d'eau, utilisé pour la pose traditionnelle (chape) ?",
                    "answerOptions": [
                        {"text": "Le mortier maigre (ou mortier de pose traditionnel).", "isCorrect": True, "key": "A"},
                        {"text": "Le mortier-colle (produit industriel en poudre pré-dosé).", "isCorrect": False, "key": "B"},
                        {"text": "Le primaire d'accrochage à base de résine.", "isCorrect": False, "key": "C"},
                        {"text": "La barbotine (mélange de ciment et d'eau), utilisée pour l'adhérence en surface.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pose traditionnelle est plus longue. Le mortier maigre n'est pas un mortier-colle et n'est pas utilisé en simple encollage."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la caractéristique d'une colle classée 'S1' (colle déformable) ?",
                    "answerOptions": [
                        {"text": "Elle permet de rattraper les mouvements du support (fissures) sans rompre l'adhérence.", "isCorrect": True, "key": "A"},
                        {"text": "Elle permet une pose plus rapide des carreaux (prise ultra-rapide) sur sol neuf.", "isCorrect": False, "key": "B"},
                        {"text": "Elle est réservée uniquement à la pose de petits carreaux intérieurs (mosaïque).", "isCorrect": False, "key": "C"},
                        {"text": "Elle est conçue pour être appliquée en couche très fine (moins de 2 mm d'épaisseur).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les colles 'S' sont déformables (S1) ou très déformables (S2). Elles sont obligatoires sur les supports 'à risque' comme le plancher chauffant ou les façades."
                },
                {
                    "questionNumber": 32,
                    "question": "Qu'est-ce que l'émaillage pour un carreau en céramique ?",
                    "answerOptions": [
                        {"text": "L'application d'une couche de verre fondu coloré pour l'esthétique et la protection.", "isCorrect": True, "key": "A"},
                        {"text": "Le procédé de cuisson à haute température pour réduire sa porosité à zéro.", "isCorrect": False, "key": "B"},
                        {"text": "Le remplissage de l'interstice entre les carreaux pour assurer l'étanchéité.", "isCorrect": False, "key": "C"},
                        {"text": "Le traitement chimique pour augmenter sa résistance à la rayure et à la glissance.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'émail est une fine couche superficielle. Un carreau émaillé est souvent moins résistant à l'usure qu'un grès cérame pleine masse."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment un mortier-colle cimentaire fait-il sa prise (durcissement) ?",
                    "answerOptions": [
                        {"text": "Par hydratation (réaction chimique avec l'eau), puis séchage physique de l'excès d'eau.", "isCorrect": True, "key": "A"},
                        {"text": "Par évaporation totale de l'eau, comme une colle en pâte prête à l'emploi (colle dispersion).", "isCorrect": False, "key": "B"},
                        {"text": "Par réaction chimique entre deux composants (résine et durcisseur).", "isCorrect": False, "key": "C"},
                        {"text": "Par cristallisation rapide de la chaux contenue dans le mélange par chaleur thermique.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'hydratation du ciment est une réaction exothermique (dégage de la chaleur) qui prend plusieurs jours avant d'atteindre sa pleine résistance."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelles sont les dimensions courantes d'une mosaïque ou d'une pâte de verre ?",
                    "answerOptions": [
                        {"text": "Très petites dimensions (2x2 cm ou 5x5 cm) souvent livrées sur filet (trame).", "isCorrect": True, "key": "A"},
                        {"text": "Grand format (120x60 cm) destiné aux pièces de luxe et aux grands volumes.", "isCorrect": False, "key": "B"},
                        {"text": "Format moyen (45x45 cm ou 30x60 cm) pour les sols d'appartement standard.", "isCorrect": False, "key": "C"},
                        {"text": "Format rectangulaire allongé (type lame de parquet) de 15x90 cm pour les sols.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les mosaïques sont souvent prêtes à poser sur une feuille (trame) pour faciliter l'alignement et la pose de multiples petites pièces à la fois."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le nom de l'outil utilisé pour étaler le mortier-colle sur le support en créant des sillons réguliers ?",
                    "answerOptions": [
                        {"text": "La spatule crantée (ou peigne).", "isCorrect": True, "key": "A"},
                        {"text": "La truelle de carreleur.", "isCorrect": False, "key": "B"},
                        {"text": "Le platoir à joint.", "isCorrect": False, "key": "C"},
                        {"text": "La taloche éponge pour le nettoyage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les crans de la spatule (U6, U9, etc.) déterminent l'épaisseur et la quantité de colle déposée."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel risque peut entraîner un carrelage de sol extérieur ayant un indice UPEC 'E' trop faible (faible résistance à l'eau) ?",
                    "answerOptions": [
                        {"text": "Le risque de gélivité (éclatement du carreau par l'eau gelée) en période de froid hivernal.", "isCorrect": True, "key": "A"},
                        {"text": "Le risque de surchauffe de la dalle en été, à cause d'une trop forte absorption thermique.", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de glissance (R) sur la surface sèche ou mouillée.", "isCorrect": False, "key": "C"},
                        {"text": "Le risque de déformation (bombage) du carreau en cas de forte pression mécanique.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'eau qui s'infiltre dans le carreau poreux gèle et augmente de volume, ce qui cause la rupture de la céramique (gélivité)."
                },
                {
                    "questionNumber": 37,
                    "question": "Qu'est-ce qu'une 'barbotine' et à quoi sert-elle dans la pose traditionnelle ?",
                    "answerOptions": [
                        {"text": "Un mélange très liquide de ciment et d'eau appliqué sur le dos du carreau pour améliorer l'adhérence.", "isCorrect": True, "key": "A"},
                        {"text": "Une pâte de nettoyage à base d'acide sulfurique très dilué pour retirer les voiles de ciment.", "isCorrect": False, "key": "B"},
                        {"text": "Une fine couche d'isolant phonique et thermique sous le carrelage pour les étages.", "isCorrect": False, "key": "C"},
                        {"text": "Un mortier de jointoiement enrichi en résine, utilisé pour les piscines uniquement.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Dans la pose traditionnelle (mortier maigre), la barbotine est la seule chose qui lie chimiquement le carreau au mortier maigre."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment doit-on préparer la colle ou le joint en poudre avant l'application ?",
                    "answerOptions": [
                        {"text": "Verser la poudre dans l'eau (jamais l'inverse) et malaxer jusqu'à obtenir une pâte homogène.", "isCorrect": True, "key": "A"},
                        {"text": "Verser l'eau dans la poudre rapidement, puis laisser reposer 30 minutes sans mélanger.", "isCorrect": False, "key": "B"},
                        {"text": "Mélanger à sec avec un outil non électrique pendant plusieurs minutes pour une bonne homogénéité.", "isCorrect": False, "key": "C"},
                        {"text": "Mélanger une première fois, puis ajouter de la poudre jusqu'à obtenir la consistance désirée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le respect de l'ordre (eau d'abord) et du temps de gâchage (mélange) est critique pour la performance des liants hydrauliques."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le nom du produit utilisé pour rendre les sols anciens très absorbants (bois, plâtre) compatibles avec la pose de carrelage ?",
                    "answerOptions": [
                        {"text": "Le primaire d'accrochage spécial pour supports sensibles, à base de résine.", "isCorrect": True, "key": "A"},
                        {"text": "Le joint de finition teinté de couleur claire.", "isCorrect": False, "key": "B"},
                        {"text": "Le mortier de ragréage fibré (utilisé pour la préparation du sol).", "isCorrect": False, "key": "C"},
                        {"text": "La colle en dispersion (prête à l'emploi) en forte épaisseur pour éviter la porosité.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le primaire bloque l'absorption excessive d'eau par le support et évite ainsi que la colle ne se dessèche trop vite."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la caractéristique d'une colle de classe 'C2' par rapport à une 'C1' ?",
                    "answerOptions": [
                        {"text": "La C2 est une colle améliorée (performance supérieure), avec une meilleure adhérence.", "isCorrect": True, "key": "A"},
                        {"text": "La C2 est une colle à séchage rapide (Fast), réservée aux chantiers urgents.", "isCorrect": False, "key": "B"},
                        {"text": "La C2 est exclusivement réservée à la pose sur supports neufs et non fissurés.", "isCorrect": False, "key": "C"},
                        {"text": "La C2 est uniquement utilisable pour la pose de carrelage en extérieur (hors gel).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le '2' signifie 'amélioré', indiquant de meilleures performances d'adhérence et de résistance (essentiel pour les grands carreaux)."
                }
            ]
        },
        # THÈME 3
        3: {
            "name": "Outillage et Préparation des Supports",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel outil est utilisé pour vérifier la planéité et la régularité d'un support avant la pose de carrelage ?",
                    "answerOptions": [
                        {"text": "La règle de maçon ou la règle à niveler de grande longueur (2 m minimum).", "isCorrect": True, "key": "A"},
                        {"text": "Le niveau à bulle, pour contrôler uniquement les aplombs verticaux du mur.", "isCorrect": False, "key": "B"},
                        {"text": "Le fil à plomb, pour tracer les lignes de référence de l'ouvrage au sol.", "isCorrect": False, "key": "C"},
                        {"text": "Le mètre ruban, afin de mesurer la périphérie exacte de la pièce en cours de travail.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La planéité est le premier critère à vérifier. Les défauts de moins de 5 mm sous une règle de 2 m sont acceptables, selon les cas."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est l'utilité du malaxeur électrique (mélangeur) pour la préparation des mortiers ?",
                    "answerOptions": [
                        {"text": "Gâcher la colle et les joints en poudre de manière homogène et rapide, en évitant les grumeaux.", "isCorrect": True, "key": "A"},
                        {"text": "Servir d'outil de ponçage léger pour le lissage des surfaces après le séchage.", "isCorrect": False, "key": "B"},
                        {"text": "Couper les carreaux de faïence en ligne droite et en angle à sec, sans eau.", "isCorrect": False, "key": "C"},
                        {"text": "Appliquer le primaire d'accrochage en fines couches sur des supports très absorbants.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le malaxeur assure un mélange de bonne qualité, ce qui est indispensable à la performance du produit (colle ou joint)."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le nom de l'outil utilisé pour tracer et couper des carreaux en ligne droite, sans électricité ?",
                    "answerOptions": [
                        {"text": "La carrelette manuelle (coupe-carreaux) avec molette et séparateur.", "isCorrect": True, "key": "A"},
                        {"text": "La meuleuse d'angle (ou disqueuse) avec un disque diamanté pour les coupes courbes.", "isCorrect": False, "key": "B"},
                        {"text": "La cisaille à tôle, pour les coupes très fines et les ajustements délicats.", "isCorrect": False, "key": "C"},
                        {"text": "La scie sauteuse (électrique) avec une lame à denture fine pour le carrelage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La carrelette est l'outil de base pour la coupe droite. Elle fonctionne par rayure superficielle (molette) puis rupture du carreau (séparateur)."
                },
                {
                    "questionNumber": 44,
                    "question": "Qu'est-ce qu'un ragréage et dans quel but est-il réalisé avant le carrelage ?",
                    "answerOptions": [
                        {"text": "L'application d'un enduit auto-lissant pour corriger les défauts de planéité du support.", "isCorrect": True, "key": "A"},
                        {"text": "Le nettoyage des joints avec une taloche éponge pour en retirer le voile de ciment.", "isCorrect": False, "key": "B"},
                        {"text": "Le collage des carreaux en double encollage pour les grands formats et l'extérieur.", "isCorrect": False, "key": "C"},
                        {"text": "La création de joints de dilatation souples dans la chape (mastic ou silicone).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le ragréage est une étape critique pour la durabilité et l'esthétique finale de la pose collée. L'épaisseur maximale est limitée par le produit."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel outil est le plus adapté pour découper des formes courbes ou des trous circulaires dans un carreau (autour d'une canalisation) ?",
                    "answerOptions": [
                        {"text": "La carrelette électrique (scie à eau) ou une pince perroquet pour les formes simples.", "isCorrect": True, "key": "A"},
                        {"text": "La carrelette manuelle, car la molette est interchangeable avec un foret.", "isCorrect": False, "key": "B"},
                        {"text": "La truelle et le marteau, pour casser la céramique par petits coups francs.", "isCorrect": False, "key": "C"},
                        {"text": "Le platoir à joint, utilisé comme guide pour le traçage des courbes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La carrelette électrique (scie à eau) est la plus polyvalente pour les formes complexes. La pince perroquet est utilisée pour 'grignoter' le carreau."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le nom de la truelle spécifique pour le carrelage, dotée d'un talon pour étaler la colle ?",
                    "answerOptions": [
                        {"text": "La truelle de carreleur (cœur de pigeon), pour le prélèvement et l'application.", "isCorrect": True, "key": "A"},
                        {"text": "La taloche à semelle lisse (en plastique ou en bois).", "isCorrect": False, "key": "B"},
                        {"text": "Le platoir pour le lissage des joints de finition (platoir éponge).", "isCorrect": False, "key": "C"},
                        {"text": "La règle de maçon pour vérifier la planéité et les défauts de niveau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La truelle cœur de pigeon a une forme triangulaire très pratique pour prélever le mortier et le déposer sur le support."
                },
                {
                    "questionNumber": 47,
                    "question": "Que doit-on faire si un support présente une ancienne peinture ou un vernis avant l'encollage ?",
                    "answerOptions": [
                        {"text": "Décaper, poncer ou gratter le support pour retirer l'ancienne couche et améliorer l'adhérence.", "isCorrect": True, "key": "A"},
                        {"text": "Utiliser une colle standard C1 sans traitement préalable du support.", "isCorrect": False, "key": "B"},
                        {"text": "Appliquer deux couches de primaire d'accrochage standard pour bloquer la peinture.", "isCorrect": False, "key": "C"},
                        {"text": "Percer des trous dans le support pour créer un pont d'adhérence vertical.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le carrelage ne doit pas être collé sur des supports non adhérents ou qui pourraient se décoller (comme la peinture ou le vernis)."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'outil utilisé pour nettoyer et lisser les joints fraîchement posés (joints cimentaires) ?",
                    "answerOptions": [
                        {"text": "La taloche à semelle éponge (ou plateau avec éponge hydro-mousse).", "isCorrect": True, "key": "A"},
                        {"text": "Le platoir à joint à semelle caoutchouc pour le serrage du joint.", "isCorrect": False, "key": "B"},
                        {"text": "La truelle langue de chat pour le remplissage des joints périphériques.", "isCorrect": False, "key": "C"},
                        {"text": "La pistolet à cartouche pour l'application des joints en silicone.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'éponge humide permet de retirer l'excès de mortier de jointoiement et de lisser la surface entre les carreaux."
                },
                {
                    "questionNumber": 49,
                    "question": "Comment appelle-t-on le traçage qui consiste à matérialiser l'implantation du carrelage sur le support (départ de la pose) ?",
                    "answerOptions": [
                        {"text": "Le calepinage (traçage des axes de référence et des lignes d'aplomb).", "isCorrect": True, "key": "A"},
                        {"text": "Le ragréage du support pour corriger la planéité.", "isCorrect": False, "key": "B"},
                        {"text": "Le jointoiement des carreaux après le séchage de la colle.", "isCorrect": False, "key": "C"},
                        {"text": "Le ponçage de la dalle à l'aide d'une monobrosse.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le calepinage est l'étape la plus importante pour garantir l'équilibre des coupes et éviter les morceaux trop petits."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est l'objectif du 'dépoussiérage' du support avant d'appliquer un primaire ou une colle ?",
                    "answerOptions": [
                        {"text": "Éliminer les fines particules qui nuiraient à l'adhérence de la colle (couche anti-adhérente).", "isCorrect": True, "key": "A"},
                        {"text": "Accélérer le temps de séchage de la chape et du ragréage auto-lissant.", "isCorrect": False, "key": "B"},
                        {"text": "Assurer une surface parfaitement lisse pour faciliter la glisse du peigne à colle.", "isCorrect": False, "key": "C"},
                        {"text": "Éviter l'apparition d'efflorescences (taches blanches) sur les joints de ciment.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La poussière et les corps gras sont des 'anti-adhérents'. Un support doit être sec, sain et propre (aspiré) pour un encollage optimal."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel outil est le plus adapté pour réaliser des coupes en biais (angle à 45°) sur les carreaux de faïence ?",
                    "answerOptions": [
                        {"text": "La carrelette électrique (scie à eau) ou la meuleuse d'angle pour des travaux précis.", "isCorrect": True, "key": "A"},
                        {"text": "La carrelette manuelle, en inclinant légèrement le carreau sur le séparateur.", "isCorrect": False, "key": "B"},
                        {"text": "Le marteau et le burin pour une coupe nette et rapide.", "isCorrect": False, "key": "C"},
                        {"text": "La pince à céramique pour grignoter l'angle souhaité très lentement.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Seule une machine électrique à disque diamanté peut réaliser une coupe précise à 45° pour faire une 'boîte' d'angle nette et propre."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est l'outil utilisé pour tasser le carreau fraîchement posé afin d'assurer un bon transfert de colle et la planéité ?",
                    "answerOptions": [
                        {"text": "Le maillet en caoutchouc blanc (ou le battage à la main sur la règle).", "isCorrect": True, "key": "A"},
                        {"text": "La règle de maçon en aluminium, frappée avec un marteau en acier lourd.", "isCorrect": False, "key": "B"},
                        {"text": "La spatule crantée (peigne) utilisée sur le dos du carreau après encollage.", "isCorrect": False, "key": "C"},
                        {"text": "La ventouse de carreleur, pour le nettoyage des voiles de ciment.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le battage est essentiel pour chasser l'air et assurer un taux de transfert de colle maximal (généralement 90% en intérieur)."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le risque de préparer une trop grande quantité de mortier-colle en une seule fois ?",
                    "answerOptions": [
                        {"text": "La colle commencera sa prise avant d'être utilisée (temps ouvert limité), ce qui nuira à l'adhérence.", "isCorrect": True, "key": "A"},
                        {"text": "Le malaxeur va surchauffer et le moteur électrique peut se mettre en panne.", "isCorrect": False, "key": "B"},
                        {"text": "La colle va durcir immédiatement dans le seau et devenir inutilisable pour le travail.", "isCorrect": False, "key": "C"},
                        {"text": "La colle va devenir trop liquide et ne pas assurer le bon positionnement du carreau sur le support.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le temps ouvert (ou temps d'emploi) d'une colle cimentaire est limité (souvent 1 à 2 heures). Il faut gâcher par petites quantités."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le nom de l'outil pour faire adhérer une trame de mosaïque sur un mur en créant une pression uniforme ?",
                    "answerOptions": [
                        {"text": "La lisseuse à mosaïque (ou taloche à semelle lisse) ou le maillet en caoutchouc.", "isCorrect": True, "key": "A"},
                        {"text": "Le fil à plomb pour un alignement vertical parfait des carreaux.", "isCorrect": False, "key": "B"},
                        {"text": "Le couteau à enduire, utilisé pour le mélange rapide de la colle.", "isCorrect": False, "key": "C"},
                        {"text": "La cisaille à tôle, pour une coupe en angle de la trame collée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Une pression uniforme est indispensable pour éviter que les petites pièces ne se décalent (lissage)."
                },
                {
                    "questionNumber": 55,
                    "question": "Comment appelle-t-on le procédé de préparation qui consiste à humidifier légèrement un carreau très absorbant (terre cuite, faïence) avant la pose ?",
                    "answerOptions": [
                        {"text": "Le mouillage (ou trempage) afin de réduire l'absorption de l'eau de la colle.", "isCorrect": True, "key": "A"},
                        {"text": "Le double encollage pour garantir un transfert optimal de la colle.", "isCorrect": False, "key": "B"},
                        {"text": "Le lissage du carreau avec une lisseuse à semelle rigide.", "isCorrect": False, "key": "C"},
                        {"text": "Le calepinage du support pour vérifier la planéité et les défauts de niveau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Mouiller le carreau (ou appliquer un primaire au dos) permet de réduire l'absorption d'eau et d'éviter le dessèchement trop rapide de la colle."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'objectif principal de la 'ventouse de carreleur' ?",
                    "answerOptions": [
                        {"text": "Manipuler et lever les grands carreaux lourds et lisses sans les casser.", "isCorrect": True, "key": "A"},
                        {"text": "Serrer et aligner les joints de dilatation souples dans la chape.", "isCorrect": False, "key": "B"},
                        {"text": "Servir de niveau à bulle intégré pour vérifier l'horizontalité du carreau.", "isCorrect": False, "key": "C"},
                        {"text": "Réaliser le serrage des joints de ciment après l'application de l'eau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les grands formats (dits 'XL') sont lourds, chers et délicats. La ventouse est l'outil de sécurité pour les manipuler."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est le risque si les sillons de colle sont trop 'fermés' (non frais) au moment de la pose du carreau (temps ouvert dépassé) ?",
                    "answerOptions": [
                        {"text": "La colle n'adhérera plus au carreau, ce qui entraînera un décollement ou un manque de transfert de matière.", "isCorrect": True, "key": "A"},
                        {"text": "Le carreau va trop s'enfoncer dans le mortier et le joint sera trop rempli.", "isCorrect": False, "key": "B"},
                        {"text": "La colle va devenir trop fluide et ne pourra pas maintenir le carreau en place.", "isCorrect": False, "key": "C"},
                        {"text": "Le temps de séchage sera beaucoup trop long (plus de 7 jours).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Une colle qui a commencé à faire sa prise ne réagit plus. Il faut alors la retirer du support et recommencer à encoller."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment s'appelle la technique de nettoyage des carreaux après la pose des joints cimentaires, avec de l'eau claire ?",
                    "answerOptions": [
                        {"text": "Le lavage à la taloche éponge pour retirer l'excès et le 'voile' de ciment.", "isCorrect": True, "key": "A"},
                        {"text": "Le décapage chimique (à l'acide) pour retirer les traces de peinture ou de colle.", "isCorrect": False, "key": "B"},
                        {"text": "Le ragréage de finition pour lisser la surface du joint.", "isCorrect": False, "key": "C"},
                        {"text": "Le ponçage du carreau avec une meuleuse d'angle pour le faire briller.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le nettoyage initial avec l'éponge (au bon moment) est crucial pour éviter de trop durcir le voile de ciment."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est l'outil de base pour vérifier l'alignement des carreaux sur une pose droite (rectangulaire) ?",
                    "answerOptions": [
                        {"text": "Le cordeau à poudre (ou cordeau traceur) pour marquer les axes de référence.", "isCorrect": True, "key": "A"},
                        {"text": "La règle de maçon pour vérifier la planéité et le niveau de la dalle.", "isCorrect": False, "key": "B"},
                        {"text": "Le niveau laser de chantier (lignes verticales uniquement).", "isCorrect": False, "key": "C"},
                        {"text": "La taloche à semelle éponge, utilisée comme guide pour la coupe.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le cordeau permet de tracer rapidement les lignes sur le support (axes principaux) pour guider la pose."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le risque de ne pas respecter le temps de repos de la colle (maturation) après le gâchage (mélange) ?",
                    "answerOptions": [
                        {"text": "La colle n'atteindra pas ses performances optimales (moins bonne adhérence) et sera difficile à travailler.", "isCorrect": True, "key": "A"},
                        {"text": "La colle va sécher beaucoup trop rapidement (prise 'éclair') avant la pose.", "isCorrect": False, "key": "B"},
                        {"text": "Le ciment sera trop chargé en eau et la colle coulera sur le support vertical.", "isCorrect": False, "key": "C"},
                        {"text": "Le mortier ne pourra pas être étalé avec une spatule crantée (il sera trop compact).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le temps de repos (maturation) permet aux adjuvants chimiques de se dissoudre correctement dans l'eau avant la pose."
                }
            ]
        },
        # THÈME 4
        4: {
            "name": "Techniques de Pose (Plein, Diagonale, Coupes)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la méthode de pose privilégiée pour une grande pièce afin d'assurer l'équilibre des coupes et une meilleure esthétique ?",
                    "answerOptions": [
                        {"text": "La pose est démarrée depuis l'axe central (milieu de la pièce) vers les bords (murs).", "isCorrect": True, "key": "A"},
                        {"text": "La pose est commencée depuis le mur le plus éloigné de l'entrée principale.", "isCorrect": False, "key": "B"},
                        {"text": "La pose doit obligatoirement commencer depuis l'angle le plus visible et le plus net de la pièce.", "isCorrect": False, "key": "C"},
                        {"text": "La pose est toujours réalisée dans le sens de la lumière naturelle ou artificielle.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Démarrer au centre permet de répartir les coupes (coupes d'équilibrage) sur les quatre côtés et de garantir une bonne esthétique."
                },
                {
                    "questionNumber": 62,
                    "question": "Qu'est-ce qu'une pose en diagonale (ou en pointe de diamant) ?",
                    "answerOptions": [
                        {"text": "La pose dont les axes sont inclinés à 45° par rapport aux murs (angles) de la pièce.", "isCorrect": True, "key": "A"},
                        {"text": "La pose de carreaux rectangulaires alignés de manière décalée (joints non alignés).", "isCorrect": False, "key": "B"},
                        {"text": "La pose avec un joint périphérique plus large que les joints entre les carreaux.", "isCorrect": False, "key": "C"},
                        {"text": "La pose qui nécessite un double encollage systématique pour tous les formats de carreaux.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pose en diagonale est plus complexe (beaucoup plus de coupes) mais agrandit visuellement la pièce."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est le risque de ne pas effectuer de 'double encollage' pour un grand carreau (supérieur à 3600 cm²) ?",
                    "answerOptions": [
                        {"text": "Le manque d'adhérence et le décollement du carreau (transfert de colle insuffisant).", "isCorrect": True, "key": "A"},
                        {"text": "La coloration anormale et le noircissement du joint de finition cimentaire.", "isCorrect": False, "key": "B"},
                        {"text": "L'accélération de la prise de la colle, réduisant le temps de manipulation disponible.", "isCorrect": False, "key": "C"},
                        {"text": "Le bombage (flambage) du carreau sous l'effet de la dilatation thermique.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le double encollage (colle sur le support et sur le dos du carreau) est la seule méthode pour garantir un transfert de colle suffisant sur les grands formats."
                },
                {
                    "questionNumber": 64,
                    "question": "Comment s'appelle l'opération qui consiste à insérer le mortier de jointoiement dans les espaces laissés entre les carreaux ?",
                    "answerOptions": [
                        {"text": "Le gâchage du joint (serrage) à l'aide d'un platoir à joint en caoutchouc.", "isCorrect": True, "key": "A"},
                        {"text": "Le calepinage de la pièce pour déterminer le sens de pose.", "isCorrect": False, "key": "B"},
                        {"text": "Le battage du carreau avec un maillet en caoutchouc léger.", "isCorrect": False, "key": "C"},
                        {"text": "Le ragréage du support pour corriger les défauts de planéité de la dalle brute.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le serrage du joint doit être réalisé en diagonale (à 45°) pour bien faire pénétrer le mortier dans l'espace disponible."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la technique pour effectuer une coupe droite et précise sur une faïence ou une céramique fine ?",
                    "answerOptions": [
                        {"text": "Rayage de la surface émaillée à la molette, puis séparation nette (rupture) au séparateur.", "isCorrect": True, "key": "A"},
                        {"text": "Sciage électrique à sec avec une lame diamantée très fine et souple.", "isCorrect": False, "key": "B"},
                        {"text": "Hachage du carreau par petits coups de marteau sur la ligne tracée à l'avance.", "isCorrect": False, "key": "C"},
                        {"text": "Découpe par le dos du carreau sans rayer l'émail de la face visible.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "C'est le principe de la carrelette manuelle : rayer l'émail (molette) pour créer une faiblesse, puis appliquer une pression localisée (séparateur)."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est l'objectif principal du 'battage' du carreau après la pose sur le lit de colle ?",
                    "answerOptions": [
                        {"text": "Chasser l'air emprisonné (bulles) et assurer un bon transfert de colle sur toute la surface.", "isCorrect": True, "key": "A"},
                        {"text": "Réduire le temps de séchage de la colle en chauffant légèrement le support par la percussion.", "isCorrect": False, "key": "B"},
                        {"text": "Augmenter l'épaisseur du joint de fractionnement pour les grandes dalles.", "isCorrect": False, "key": "C"},
                        {"text": "Rendre la surface du carreau plus lisse (polis) par frottement constant du maillet.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le battage est essentiel pour éviter les 'vides' sous les carreaux qui provoquent des ruptures si un choc se produit."
                },
                {
                    "questionNumber": 67,
                    "question": "Dans une pose en intérieur, de combien doit être au minimum l'équilibrage des coupes (la plus petite coupe) contre les murs ?",
                    "answerOptions": [
                        {"text": "La coupe la plus petite doit être au moins de la moitié du carreau ou de 5 cm minimum.", "isCorrect": True, "key": "A"},
                        {"text": "La coupe peut être de 1 cm si elle est masquée par une plinthe ou un meuble lourd.", "isCorrect": False, "key": "B"},
                        {"text": "La coupe la plus petite doit être au moins des deux tiers de la largeur du carreau posé.", "isCorrect": False, "key": "C"},
                        {"text": "Il n'y a pas de règle, on pose le carreau entier et la chute est la coupe.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Un équilibrage par rapport au centre permet d'éviter les coupes fines et inesthétiques (moins de 5 cm) sur un mur."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le nom de la pose (pour les carreaux rectangulaires) où les joints ne sont alignés ni en ligne ni en colonne (comme les briques) ?",
                    "answerOptions": [
                        {"text": "La pose à joints contrariés (ou décalée, 1/3-2/3, 1/4-3/4, etc.).", "isCorrect": True, "key": "A"},
                        {"text": "La pose en damier (alternance de couleurs différentes).", "isCorrect": False, "key": "B"},
                        {"text": "La pose en plein (ou pose droite), où tous les joints sont alignés en croix.", "isCorrect": False, "key": "C"},
                        {"text": "La pose en diagonale (axes à 45° par rapport aux murs).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pose décalée est souvent utilisée pour les carreaux effet parquet, mais le décalage ne doit pas dépasser 1/3 de la longueur du carreau pour éviter le risque de flèche."
                },
                {
                    "questionNumber": 69,
                    "question": "Comment doit-on réaliser l'encollage d'un mur avec une colle cimentaire pour les carreaux de faïence ?",
                    "answerOptions": [
                        {"text": "Par simple encollage du mur avec une spatule crantée (peigne), en sillons verticaux.", "isCorrect": True, "key": "A"},
                        {"text": "Par double encollage (mur et dos du carreau) pour les petits carreaux muraux.", "isCorrect": False, "key": "B"},
                        {"text": "Par application de la colle uniquement sur le dos du carreau (beurrage) avant la pose.", "isCorrect": False, "key": "C"},
                        {"text": "Par gâchage de la colle au mur, puis pose immédiate sans battage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'encollage vertical permet à l'air de s'échapper plus facilement et l'eau de s'écouler. Le double encollage n'est pas nécessaire pour les petits formats muraux."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le but d'utiliser des 'croisillons auto-nivelants' (système de nivellement) ?",
                    "answerOptions": [
                        {"text": "Assurer l'alignement des joints et la parfaite planéité des carreaux (pas de 'dent' entre eux).", "isCorrect": True, "key": "A"},
                        {"text": "Remplacer la colle pour les joints périphériques (dilatation) et les angles vifs de mur.", "isCorrect": False, "key": "B"},
                        {"text": "Permettre le séchage rapide du mortier de jointoiement en phase de finition de l'ouvrage.", "isCorrect": False, "key": "C"},
                        {"text": "Servir de revêtement de finition autour des canalisations et des écoulements d'eau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le système auto-nivelant est essentiel pour les grands formats et/ou les supports n'ayant pas une planéité parfaite, en évitant les décalages (dents)."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment s'appelle la technique de pose des carreaux directement sur une chape fraîche (mortier maigre) sans colle intermédiaire ?",
                    "answerOptions": [
                        {"text": "La pose scellée (ou pose traditionnelle) avec barbotine.", "isCorrect": True, "key": "A"},
                        {"text": "La pose collée, pour les chapes et supports anciens ou déformés.", "isCorrect": False, "key": "B"},
                        {"text": "La pose flottante, à sec sur des dalles amovibles (pour les terrasses).", "isCorrect": False, "key": "C"},
                        {"text": "La pose en double encollage, pour les grands formats de carrelage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pose scellée est en perte de vitesse. Elle est plus longue et complexe (création de la chape, nivellement, battage) mais permet de rattraper de gros défauts de niveau."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le risque de ne pas nettoyer les résidus de joint cimentaire rapidement après le serrage ?",
                    "answerOptions": [
                        {"text": "Le 'voile de ciment' va durcir sur le carreau et nécessitera un décapage chimique lourd.", "isCorrect": True, "key": "A"},
                        {"text": "Le joint va se rétracter excessivement, créant des fissures importantes.", "isCorrect": False, "key": "B"},
                        {"text": "La colle sous le carreau va se fluidifier, et le carreau va s'enfoncer dans le mortier.", "isCorrect": False, "key": "C"},
                        {"text": "Le carreau va subir un choc thermique qui le fera décoller du mur ou du sol.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le nettoyage du voile doit se faire au bon moment (ni trop tôt, ni trop tard) pour un résultat net."
                },
                {
                    "questionNumber": 73,
                    "question": "Dans une pose en chevron (ou à bâtons rompus), quel est le point de départ privilégié ?",
                    "answerOptions": [
                        {"text": "Le point de jonction entre les deux premiers carreaux, sur l'axe central de la pièce.", "isCorrect": True, "key": "A"},
                        {"text": "L'angle le plus visible du mur de fond de la pièce pour masquer les coupes.", "isCorrect": False, "key": "B"},
                        {"text": "La porte d'entrée, en posant le carreau entier en premier, près du seuil.", "isCorrect": False, "key": "C"},
                        {"text": "Le mur de la cuisine, pour le rendre plus visible au centre de la pièce.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pose en chevron nécessite une symétrie et une précision parfaite. Il est préférable de commencer par l'axe central."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le risque d'appliquer le mortier-colle avec des sillons orientés différemment (non parallèles) ?",
                    "answerOptions": [
                        {"text": "L'air peut rester emprisonné sous le carreau (bulles) lors du battage, ce qui crée un vide.", "isCorrect": True, "key": "A"},
                        {"text": "La colle va durcir beaucoup trop rapidement, même en cas de double encollage.", "isCorrect": False, "key": "B"},
                        {"text": "Le carreau va se déplacer horizontalement pendant le séchage de la colle.", "isCorrect": False, "key": "C"},
                        {"text": "L'eau contenue dans le mortier va provoquer une efflorescence saline visible.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les sillons doivent être parallèles et droits. Pour le mur, les sillons doivent être verticaux (pour l'échappement de l'air)."
                },
                {
                    "questionNumber": 75,
                    "question": "Comment s'appelle le carreau qui présente le même motif sur toute son épaisseur (non émaillé) ?",
                    "answerOptions": [
                        {"text": "Le carreau pleine masse (grès cérame), très résistant à l'usure.", "isCorrect": True, "key": "A"},
                        {"text": "Le carreau émaillé (faïence ou céramique), avec une couche de finition en surface.", "isCorrect": False, "key": "B"},
                        {"text": "Le carreau de Terre Cuite, qui nécessite une finition par traitement.", "isCorrect": False, "key": "C"},
                        {"text": "Le carreau de mosaïque (pâte de verre), collé sur une trame souple.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le grès cérame pleine masse est idéal pour les lieux à fort trafic : si la surface s'use, le motif reste visible."
                },
                {
                    "questionNumber": 76,
                    "question": "Que doit-on faire avant de poser des carreaux différents (lots de fabrication différents) ?",
                    "answerOptions": [
                        {"text": "Vérifier la nuance (tonalité) et le calibre (dimension) pour s'assurer de leur compatibilité.", "isCorrect": True, "key": "A"},
                        {"text": "Les tremper tous dans l'eau chaude pendant 10 minutes pour les ramollir.", "isCorrect": False, "key": "B"},
                        {"text": "Les poncer tous avec une meuleuse d'angle pour les rendre parfaitement plats.", "isCorrect": False, "key": "C"},
                        {"text": "Les recouper tous au même format, même si le calibre est légèrement différent au départ.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Même s'ils portent la même référence, les carreaux de lots différents peuvent présenter de légères variations (calibre et nuance). Il faut vérifier l'étiquette sur le carton."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le rôle du joint de fractionnement (ou joint de dilatation) dans une grande surface carrelée ?",
                    "answerOptions": [
                        {"text": "Absorber les mouvements du support (dilatation et retrait) et prévenir les fissures de l'ouvrage.", "isCorrect": True, "key": "A"},
                        {"text": "Rendre la surface plus glissante pour faciliter le nettoyage à la raclette.", "isCorrect": False, "key": "B"},
                        {"text": "Évacuer l'eau de pluie dans un ouvrage extérieur (comme un drain vertical).", "isCorrect": False, "key": "C"},
                        {"text": "Servir de point d'ancrage pour les meubles lourds et les cloisons amovibles.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les joints de dilatation sont obligatoires au-delà d'une certaine surface (variable selon les DTU) pour éviter le flambage (soulèvement) du carrelage."
                },
                {
                    "questionNumber": 78,
                    "question": "Comment s'appelle l'outil utilisé pour dessiner le profil d'un objet (poteau, plinthe) sur le carreau à couper ?",
                    "answerOptions": [
                        {"text": "Le trace-profil (ou copieur de profil) pour transférer la forme exacte.", "isCorrect": True, "key": "A"},
                        {"text": "Le cordeau à poudre (cordeau traceur) pour marquer l'axe central.", "isCorrect": False, "key": "B"},
                        {"text": "La règle de maçon pour vérifier la planéité et les défauts de niveau.", "isCorrect": False, "key": "C"},
                        {"text": "Le niveau laser rotatif.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le trace-profil est indispensable pour réaliser des coupes complexes (contours) autour d'obstacles (piliers, tuyauteries)."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le risque de réaliser des joints trop fins sur un carrelage de sol extérieur ?",
                    "answerOptions": [
                        {"text": "L'absence de place pour la dilatation de la céramique, entraînant un risque de soulèvement et de rupture.", "isCorrect": True, "key": "A"},
                        {"text": "L'apparition rapide de taches de moisissure de couleur noire sur le carreau.", "isCorrect": False, "key": "B"},
                        {"text": "L'impossibilité de le rendre antidérapant (R) sur la surface mouillée.", "isCorrect": False, "key": "C"},
                        {"text": "Le temps de séchage sera beaucoup trop long (plus de 10 jours).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'extérieur nécessite des joints plus larges que l'intérieur (souvent 5 mm ou plus) pour absorber les chocs thermiques (chaleur/froid)."
                },
                {
                    "questionNumber": 80,
                    "question": "Dans une pose murale, quel est le sens d'encollage privilégié des sillons de colle pour favoriser l'évacuation de l'air ?",
                    "answerOptions": [
                        {"text": "Vertical (sillons montants) ou horizontal (sillons droits), en fonction du sens de pose.", "isCorrect": True, "key": "A"},
                        {"text": "En chevrons (ou à bâtons rompus) pour une meilleure accroche de la faïence.", "isCorrect": False, "key": "B"},
                        {"text": "En spirale (du centre vers l'extérieur du mur) pour une pose plus rapide.", "isCorrect": False, "key": "C"},
                        {"text": "En oblique (à 45°), pour masquer les différences de planéité du support.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les sillons horizontaux (ou verticaux) facilitent l'échappement des bulles d'air lors du battage, évitant les vides sous les carreaux muraux."
                }
            ]
        },
        # THÈME 5
        5: {
            "name": "Calculs et Métrés",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle formule simple permet de calculer la surface d'une pièce rectangulaire (métré) ?",
                    "answerOptions": [
                        {"text": "Longueur mesurée de la pièce multipliée par la largeur mesurée (L x l).", "isCorrect": True, "key": "A"},
                        {"text": "Longueur ajoutée à la largeur, multipliée par deux ((L + l) x 2).", "isCorrect": False, "key": "B"},
                        {"text": "Périmètre total de la pièce, divisé par la hauteur des murs.", "isCorrect": False, "key": "C"},
                        {"text": "Nombre de carreaux entiers sur la longueur multiplié par le nombre de carreaux entiers sur la largeur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'aire (surface) se calcule en mètres carrés (m²) : Longueur (m) x Largeur (m)."
                },
                {
                    "questionNumber": 82,
                    "question": "Si une pièce mesure 5,50 m de long et 3,00 m de large, quelle est sa surface totale ?",
                    "answerOptions": [
                        {"text": "16,50 m².", "isCorrect": True, "key": "A"},
                        {"text": "8,50 m².", "isCorrect": False, "key": "B"},
                        {"text": "15,00 m².", "isCorrect": False, "key": "C"},
                        {"text": "16,00 m².", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 5,50 m x 3,00 m = 16,50 m²."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel pourcentage de carreaux supplémentaires doit-on prévoir au minimum pour compenser les pertes (coupes et casses) sur une pose droite simple ?",
                    "answerOptions": [
                        {"text": "10% de surface supplémentaire (ou 15% pour une pose en diagonale).", "isCorrect": True, "key": "A"},
                        {"text": "5% de surface supplémentaire, quel que soit le type de pose (droit ou diagonale).", "isCorrect": False, "key": "B"},
                        {"text": "20% de surface supplémentaire, uniquement pour les grands carreaux (XL).", "isCorrect": False, "key": "C"},
                        {"text": "Aucun surplus n'est nécessaire si l'on est très précautionneux avec le matériel.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le pourcentage de perte est variable (10% pour le droit, 15% pour la diagonale, 20% pour les chevrons). Il est essentiel de prévoir un surplus pour les réparations futures (carreaux de rechange)."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le périmètre d'une pièce rectangulaire mesurant 4,00 m de long et 3,50 m de large ?",
                    "answerOptions": [
                        {"text": "15,00 mètres linéaires (ml).", "isCorrect": True, "key": "A"},
                        {"text": "14,00 mètres linéaires (ml).", "isCorrect": False, "key": "B"},
                        {"text": "7,50 mètres linéaires (ml).", "isCorrect": False, "key": "C"},
                        {"text": "12,00 mètres linéaires (ml).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : (4,00 m + 3,50 m) x 2 = 7,50 m x 2 = 15,00 ml."
                },
                {
                    "questionNumber": 85,
                    "question": "Un carreau mesure 30 cm par 30 cm (0,30 m x 0,30 m). Quelle est sa surface en mètres carrés (m²) ?",
                    "answerOptions": [
                        {"text": "0,09 m².", "isCorrect": True, "key": "A"},
                        {"text": "0,9 m².", "isCorrect": False, "key": "B"},
                        {"text": "0,6 m².", "isCorrect": False, "key": "C"},
                        {"text": "9,00 m².", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 0,30 m x 0,30 m = 0,09 m². Il est essentiel de travailler en mètres pour le métré."
                },
                {
                    "questionNumber": 86,
                    "question": "Combien de carreaux de 20 cm x 20 cm (0,04 m²) faut-il pour couvrir une surface de 1 m² ?",
                    "answerOptions": [
                        {"text": "25 carreaux (1 m² / 0,04 m²).", "isCorrect": True, "key": "A"},
                        {"text": "100 carreaux (1 m² / 0,01 m²).", "isCorrect": False, "key": "B"},
                        {"text": "50 carreaux (1 m² / 0,02 m²).", "isCorrect": False, "key": "C"},
                        {"text": "10 carreaux.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Surface d'un carreau = 0,20 m x 0,20 m = 0,04 m². Nombre de carreaux = 1 / 0,04 = 25."
                },
                {
                    "questionNumber": 87,
                    "question": "La consommation moyenne de colle est de 4 kg/m². Combien de sacs de 25 kg sont nécessaires pour carreler 55 m² ?",
                    "answerOptions": [
                        {"text": "9 sacs (55 m² x 4 kg/m² = 220 kg / 25 kg ≈ 8,8 sacs).", "isCorrect": True, "key": "A"},
                        {"text": "8 sacs.", "isCorrect": False, "key": "B"},
                        {"text": "11 sacs.", "isCorrect": False, "key": "C"},
                        {"text": "5 sacs.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Consommation totale = 55 x 4 = 220 kg. Nombre de sacs = 220 / 25 = 8,8. Il faut donc commander 9 sacs."
                },
                {
                    "questionNumber": 88,
                    "question": "Pour une pose en plein dans une cuisine de 10 m², avec des carreaux de 40x40 cm, quelle est la quantité de carreaux (hors coupes) nécessaire ?",
                    "answerOptions": [
                        {"text": "63 carreaux entiers environ (10 m² / 0,16 m²).", "isCorrect": True, "key": "A"},
                        {"text": "100 carreaux entiers.", "isCorrect": False, "key": "B"},
                        {"text": "25 carreaux entiers.", "isCorrect": False, "key": "C"},
                        {"text": "50 carreaux entiers.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Surface d'un carreau = 0,40 x 0,40 = 0,16 m². Nombre de carreaux = 10 / 0,16 = 62,5. Il faut 63 carreaux."
                },
                {
                    "questionNumber": 89,
                    "question": "Dans le cadre d'un devis pour la fourniture et pose, que signifie 'fourniture et pose' (F&P) ?",
                    "answerOptions": [
                        {"text": "Le prix total inclut les matériaux (colle, joint, carreau) et le coût de la main d'œuvre (pose).", "isCorrect": True, "key": "A"},
                        {"text": "Le prix n'inclut que les matériaux, la pose étant facturée séparément au taux horaire par le client.", "isCorrect": False, "key": "B"},
                        {"text": "Le prix comprend uniquement la pose, la fourniture des matériaux étant à la charge du client.", "isCorrect": False, "key": "C"},
                        {"text": "Le prix est uniquement celui de l'assurance décennale obligatoire pour le chantier concerné.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le client doit bien distinguer les deux postes pour comparer les prix : le coût de l'achat des produits (fourniture) et le coût du travail (pose)."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est l'outil utilisé pour déterminer les angles exacts d'une pièce non rectangulaire pour le calepinage ?",
                    "answerOptions": [
                        {"text": "L'équerre optique ou l'équerre à fausse coupe (ou équerre de menuisier).", "isCorrect": True, "key": "A"},
                        {"text": "La truelle de carreleur pour le prélèvement de la colle.", "isCorrect": False, "key": "B"},
                        {"text": "Le maillet en caoutchouc pour le battage du carrelage.", "isCorrect": False, "key": "C"},
                        {"text": "Le cordeau à poudre pour le traçage des lignes de référence au sol.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'équerre à fausse coupe permet de relever les angles (souvent non droits) pour anticiper et réaliser les coupes d'angle au mur."
                },
                {
                    "questionNumber": 91,
                    "question": "Si le périmètre d'une pièce est de 18 ml, combien de ml de plinthes (de 60 cm de long) faut-il prévoir (hors surplus pour les coupes) ?",
                    "answerOptions": [
                        {"text": "30 plinthes (18 ml / 0,60 m).", "isCorrect": True, "key": "A"},
                        {"text": "36 plinthes.", "isCorrect": False, "key": "B"},
                        {"text": "108 plinthes.", "isCorrect": False, "key": "C"},
                        {"text": "25 plinthes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Longueur totale = 18 m. Longueur d'une plinthe = 0,60 m. Nombre de plinthes = 18 / 0,60 = 30."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le volume d'une chape de 5 m² avec une épaisseur (hauteur) de 0,05 m ?",
                    "answerOptions": [
                        {"text": "0,25 m³ (Volume = Surface x Hauteur).", "isCorrect": True, "key": "A"},
                        {"text": "5,05 m³.", "isCorrect": False, "key": "B"},
                        {"text": "1,00 m³.", "isCorrect": False, "key": "C"},
                        {"text": "2,50 m³.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 5 m² x 0,05 m = 0,25 m³. Le volume est toujours exprimé en mètres cubes (m³)."
                },
                {
                    "questionNumber": 93,
                    "question": "Pour réaliser un joint époxydique, il faut mélanger la résine (A) et le durcisseur (B) dans un rapport de 1:2. Si on a 1 kg de résine, quelle quantité de durcisseur doit être ajoutée ?",
                    "answerOptions": [
                        {"text": "2 kg de durcisseur (rapport 1:2).", "isCorrect": True, "key": "A"},
                        {"text": "1 kg de durcisseur.", "isCorrect": False, "key": "B"},
                        {"text": "0,5 kg de durcisseur (rapport 2:1).", "isCorrect": False, "key": "C"},
                        {"text": "3 kg de durcisseur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le rapport 1:2 signifie que pour 1 dose de A, il faut 2 doses de B. Il est crucial de respecter les dosages (à la balance) pour les produits bi-composants (époxydiques)."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment s'appelle l'étape de vérification des quantités de matériaux (carreaux, colle, joint) sur le chantier ?",
                    "answerOptions": [
                        {"text": "L'inventaire ou le contrôle de réception des matériaux.", "isCorrect": True, "key": "A"},
                        {"text": "Le calepinage du support (traçage des axes).", "isCorrect": False, "key": "B"},
                        {"text": "Le ragréage de la dalle (lissage).", "isCorrect": False, "key": "C"},
                        {"text": "La pose à joints contrariés (décalage de l'alignement).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Il est essentiel de s'assurer que les quantités livrées correspondent au métré réalisé et au surplus commandé."
                },
                {
                    "questionNumber": 95,
                    "question": "Si un sac de mortier-colle donne 17 litres de mortier gâché, combien de sacs faut-il pour remplir un seau de 25 litres ?",
                    "answerOptions": [
                        {"text": "2 sacs (un peu plus que 1,47 sac).", "isCorrect": True, "key": "A"},
                        {"text": "1 sac (pas assez de volume).", "isCorrect": False, "key": "B"},
                        {"text": "3 sacs.", "isCorrect": False, "key": "C"},
                        {"text": "4 sacs.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 25 litres / 17 litres par sac ≈ 1,47 sac. Il faut commander 2 sacs pour être certain d'avoir la quantité nécessaire."
                },
                {
                    "questionNumber": 96,
                    "question": "Un pot de joint époxydique de 5 kg couvre 10 m². Combien de pots sont nécessaires pour 45 m² de surface ?",
                    "answerOptions": [
                        {"text": "5 pots (45 m² / 10 m² par pot = 4,5 pots).", "isCorrect": True, "key": "A"},
                        {"text": "4 pots (insuffisant).", "isCorrect": False, "key": "B"},
                        {"text": "6 pots.", "isCorrect": False, "key": "C"},
                        {"text": "10 pots.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 45 / 10 = 4,5. Il faut commander 5 pots pour être certain de finir l'ouvrage."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle est la définition du 'calibre' d'un carreau en céramique ?",
                    "answerOptions": [
                        {"text": "La dimension réelle (effective) du carreau après la cuisson, qui peut varier légèrement.", "isCorrect": True, "key": "A"},
                        {"text": "La résistance du carreau à la glissance (indice R) après la pose au mur.", "isCorrect": False, "key": "B"},
                        {"text": "L'épaisseur exacte du carreau, mesurée en millimètres et sans marge d'erreur.", "isCorrect": False, "key": "C"},
                        {"text": "La capacité d'absorption d'eau du carreau, exprimée en pourcentage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le calibre est indiqué sur le carton. Si les calibres sont différents entre deux lots, les joints ne seront pas alignés."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le nom de l'indice qui mesure la résistance aux chocs (pièces lourdes tombantes) selon le classement UPEC ?",
                    "answerOptions": [
                        {"text": "L'indice 'P' (Poinçonnement, de P2 à P4s).", "isCorrect": True, "key": "A"},
                        {"text": "L'indice 'U' (Usure par frottement du trafic lourd).", "isCorrect": False, "key": "B"},
                        {"text": "L'indice 'E' (résistance à l'Eau et à l'humidité).", "isCorrect": False, "key": "C"},
                        {"text": "L'indice 'C' (résistance aux Agents Chimiques).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'indice P est crucial dans les pièces soumises à de gros chocs (garages, cuisines professionnelles)."
                },
                {
                    "questionNumber": 99,
                    "question": "Pour une pose en plein de 30 m² avec des carreaux de 60x60 cm (0,36 m²), quelle est la quantité de carreaux entiers nécessaire (hors surplus) ?",
                    "answerOptions": [
                        {"text": "84 carreaux entiers (30 m² / 0,36 m²).", "isCorrect": True, "key": "A"},
                        {"text": "120 carreaux entiers.", "isCorrect": False, "key": "B"},
                        {"text": "50 carreaux entiers.", "isCorrect": False, "key": "C"},
                        {"text": "180 carreaux entiers.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Surface d'un carreau = 0,60 x 0,60 = 0,36 m². Nombre de carreaux = 30 / 0,36 ≈ 83,33. Il faut 84 carreaux."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est l'outil le plus précis pour vérifier la verticalité d'une pose murale ?",
                    "answerOptions": [
                        {"text": "Le niveau à bulle (long) ou le niveau laser (aplomb vertical).", "isCorrect": True, "key": "A"},
                        {"text": "Le cordeau à poudre, utilisé uniquement pour le traçage horizontal.", "isCorrect": False, "key": "B"},
                        {"text": "La truelle de carreleur pour le prélèvement de la colle.", "isCorrect": False, "key": "C"},
                        {"text": "La règle de maçon pour vérifier la planéité et les défauts de niveau au sol.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le niveau à bulle ou le laser permet de s'assurer que les joints verticaux sont parfaitement d'aplomb."
                }
            ]
        }
    }
}