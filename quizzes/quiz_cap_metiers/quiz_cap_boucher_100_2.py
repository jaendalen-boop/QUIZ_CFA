quiz_data = {
    "title": "Quiz CAP Boucher (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : RÉCEPTION, CONTRÔLE ET STOCKAGE DES MATIÈRES PREMIÈRES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : RÉCEPTION, CONTRÔLE ET STOCKAGE DES MATIÈRES PREMIÈRES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la température réglementaire maximale à cœur pour la réception des viandes bovines fraîches ?",
                    "answerOptions": [
                        {"text": "Plus sept degrés Celsius maximum", "isCorrect": True},
                        {"text": "Plus trois degrés Celsius maximum", "isCorrect": False},
                        {"text": "Plus dix degrés Celsius maximum", "isCorrect": False},
                        {"text": "Zéro degré Celsius de moyenne", "isCorrect": False}
                    ],
                    "correction": "La législation européenne impose une température maximale de +7 °C à cœur lors de la réception des viandes fraîches d'ongulés domestiques afin de bloquer la prolifération microbienne."
                },
                {
                    "questionNumber": 2,
                    "question": "Comment se nomme la marque sanitaire officielle apposée sur une carcasse à l'abattoir ?",
                    "answerOptions": [
                        {"text": "L'estampille de salubrité", "isCorrect": True},
                        {"text": "Le label de qualité", "isCorrect": False},
                        {"text": "Le macaron d'inspection", "isCorrect": False},
                        {"text": "Le sceau de conformité", "isCorrect": False}
                    ],
                    "correction": "L'estampille de salubrité, de forme ovale, prouve que la carcasse a subi une inspection vétérinaire ante et post mortem favorable et qu'elle est apte à la consommation humaine."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel processus biochimique rend la viande bovine plus tendre lors du stockage en chambre froide ?",
                    "answerOptions": [
                        {"text": "La protéolyse enzymatique du muscle", "isCorrect": True},
                        {"text": "L'oxydation des lipides intramusculaires", "isCorrect": False},
                        {"text": "La coagulation des protéines myofibrillaires", "isCorrect": False},
                        {"text": "La fermentation lactique des sucres", "isCorrect": False}
                    ],
                    "correction": "La maturation est principalement due à l'action d'enzymes protéolytiques qui dégradent progressivement la structure des fibres musculaires, augmentant ainsi la tendreté de la viande."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle procédure appliquer face à une carcasse bovine livrée avec une température à cœur de douze degrés ?",
                    "answerOptions": [
                        {"text": "Isoler la marchandise dans un local spécifique et consigner le refus sur le bon de livraison pour renvoi", "isCorrect": True},
                        {"text": "Découper rapidement la viande pour la placer en cellule de refroidissement rapide afin de stopper le développement bactérien avant la mise en vente", "isCorrect": False},
                        {"text": "Accepter la livraison avec des réserves orales et baisser temporairement la température de la chambre froide", "isCorrect": False},
                        {"text": "Nettoyer la surface à l'eau chlorée puis stocker la viande au congélateur pour la destruction des germes", "isCorrect": False}
                    ],
                    "correction": "Une température de 12 °C est une non-conformité critique entraînant une rupture de la chaîne du froid. Il faut isoler le produit et formaliser le refus par écrit."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel principe de gestion des stocks garantit la rotation optimale des matières premières périssables ?",
                    "answerOptions": [
                        {"text": "Le premier entré premier sorti", "isCorrect": True},
                        {"text": "Le dernier entré premier sorti", "isCorrect": False},
                        {"text": "Le tri par coût moyen pondéré", "isCorrect": False},
                        {"text": "Le réapprovisionnement à flux tendu", "isCorrect": False}
                    ],
                    "correction": "Le principe PEPS ou FIFO permet d'éviter le dépassement des dates limites de consommation en priorisant l'utilisation systématique des stocks les plus anciens."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel document obligatoire doit accompagner chaque carcasse bovine de l'abattoir jusqu'au laboratoire ?",
                    "answerOptions": [
                        {"text": "Le passeport bovin", "isCorrect": True},
                        {"text": "Le certificat de naissance", "isCorrect": False},
                        {"text": "Le registre de transport", "isCorrect": False},
                        {"text": "Le carnet de vaccination", "isCorrect": False}
                    ],
                    "correction": "Le passeport bovin garantit la traçabilité individuelle de l'animal, mentionnant sa date de naissance, son sexe, sa race et ses détenteurs successifs."
                },
                {
                    "questionNumber": 7,
                    "question": "Que désigne l'étape du ressuage intervenant juste après l'abattage de l'animal ?",
                    "answerOptions": [
                        {"text": "Le refroidissement rapide de la carcasse", "isCorrect": True},
                        {"text": "L'évacuation totale du sang résiduel", "isCorrect": False},
                        {"text": "La séparation des quartiers avants", "isCorrect": False},
                        {"text": "Le retrait mécanique de la peau", "isCorrect": False}
                    ],
                    "correction": "Le ressuage est le refroidissement continu et ininterrompu de la carcasse en abattoir, étape indispensable pour atteindre une température à cœur réglementaire."
                },
                {
                    "questionNumber": 8,
                    "question": "Pourquoi une viande de porc présentant un pH trop bas juste après l'abattage est-elle problématique ?",
                    "answerOptions": [
                        {"text": "Elle présente un risque majeur de devenir exsudative et de perdre son eau lors de la découpe", "isCorrect": True},
                        {"text": "Elle favorise une coloration extrêmement sombre et une texture ferme et sèche qui rebute le consommateur lors de la mise en vitrine réfrigérée", "isCorrect": False},
                        {"text": "Elle indique une prolifération avancée de micro organismes pathogènes nécessitant un retrait immédiat de la vente", "isCorrect": False},
                        {"text": "Elle empêche toute réaction de coloration lors de la cuisson à cause du manque de sucres résiduels", "isCorrect": False}
                    ],
                    "correction": "Une chute trop rapide du pH entraîne l'apparition d'une viande PSE Pâle, Molle, Exsudative, altérant sa qualité technologique et son rendement en charcuterie."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel contrôle visuel est indispensable lors de la réception de viandes conditionnées sous vide ?",
                    "answerOptions": [
                        {"text": "La stricte adhérence du film plastique", "isCorrect": True},
                        {"text": "La présence de gros cristaux de glace", "isCorrect": False},
                        {"text": "L'opacité totale du sachet d'emballage", "isCorrect": False},
                        {"text": "L'absence d'étiquette de pesée fournisseur", "isCorrect": False}
                    ],
                    "correction": "Une perte de vide indique une micro fuite ou une fermentation productrice de gaz, compromettant gravement la conservation et la sécurité sanitaire du produit."
                },
                {
                    "questionNumber": 10,
                    "question": "À quelle température maximale les matières premières surgelées doivent-elles être réceptionnées ?",
                    "answerOptions": [
                        {"text": "Moins dix huit", "isCorrect": True},
                        {"text": "Moins dix degrés", "isCorrect": False},
                        {"text": "Moins douze degrés", "isCorrect": False},
                        {"text": "Zéro degré celsius", "isCorrect": False}
                    ],
                    "correction": "La réglementation exige une température de réception et de stockage de -18 °C minimum pour maintenir l'état de surgélation et stopper l'activité enzymatique."
                },
                {
                    "questionNumber": 11,
                    "question": "Pourquoi les quartiers de viande doivent-ils être suspendus aux esses sans se toucher en chambre froide ?",
                    "answerOptions": [
                        {"text": "Pour permettre une circulation optimale de l'air froid et éviter les zones de condensation propices aux bactéries", "isCorrect": True},
                        {"text": "Pour faciliter grandement le passage des chariots élévateurs lors des livraisons matinales et limiter les accidents du travail liés à la manutention lourde", "isCorrect": False},
                        {"text": "Pour éviter le transfert de charges massives sur un seul point de fixation de la structure du plafond", "isCorrect": False},
                        {"text": "Pour empêcher les échanges directs de saveurs entre les différentes espèces animales stockées dans un même espace", "isCorrect": False}
                    ],
                    "correction": "Un espacement adéquat garantit un flux d'air froid homogène, maintenant une température uniforme et prévenant le poissage de surface dû à la stagnation d'humidité."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel niveau d'hygrométrie relative est recommandé en chambre froide pour le stockage des carcasses bovines ?",
                    "answerOptions": [
                        {"text": "Environ quatre vingt cinq pourcent", "isCorrect": True},
                        {"text": "Moins de cinquante pourcent d'humidité", "isCorrect": False},
                        {"text": "Exactement cent pourcent d'humidité constante", "isCorrect": False},
                        {"text": "Autour de trente pourcent d'humidité", "isCorrect": False}
                    ],
                    "correction": "Une hygrométrie relative d'environ 85 % évite le dessèchement excessif de la viande perte de poids tout en empêchant la formation de moisissures."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle précaution de stockage spécifique s'applique aux abats rouges frais en chambre froide ?",
                    "answerOptions": [
                        {"text": "Ils doivent être séparés des carcasses", "isCorrect": True},
                        {"text": "Ils nécessitent une aération à l'air libre", "isCorrect": False},
                        {"text": "Ils exigent une maturation de sept jours", "isCorrect": False},
                        {"text": "Ils doivent obligatoirement être salés préalablement", "isCorrect": False}
                    ],
                    "correction": "Les abats étant des produits hautement périssables dotés d'une flore microbienne spécifique, ils requièrent un bac fermé ou une zone distincte pour éviter les contaminations croisées."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelles informations minimales doivent figurer sur l'étiquette de traçabilité interne attachée à un quartier de viande ?",
                    "answerOptions": [
                        {"text": "Le numéro de lot du fournisseur associé à la date de réception du produit", "isCorrect": True},
                        {"text": "Le poids exact au gramme près lors du chargement dans le camion frigorifique ainsi que la signature manuscrite du vétérinaire inspecteur", "isCorrect": False},
                        {"text": "Le taux de matière grasse intramusculaire évalué visuellement par le chef boucher de l'établissement", "isCorrect": False},
                        {"text": "Le nom complet de la race suivi obligatoirement de l'adresse postale de l'exploitation agricole", "isCorrect": False}
                    ],
                    "correction": "La traçabilité interne impose de lier le numéro de lot souvent le numéro d'abattage à la date d'entrée pour assurer le suivi jusqu'à la mise en vente."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel défaut visuel caractérise une viande bovine issue d'un animal très stressé avant l'abattage ?",
                    "answerOptions": [
                        {"text": "Une coupe sombre", "isCorrect": True},
                        {"text": "Une pâleur extrême", "isCorrect": False},
                        {"text": "Un persillé excessif", "isCorrect": False},
                        {"text": "Une surface verdâtre", "isCorrect": False}
                    ],
                    "correction": "Le stress épuise les réserves de glycogène, empêchant l'acidification normale post mortem. La viande devient sombre, ferme, sèche DFD et se conserve mal."
                },
                {
                    "questionNumber": 16,
                    "question": "De quel matériau spécifique doivent être constitués les crochets de suspension en chambre froide ?",
                    "answerOptions": [
                        {"text": "En acier inoxydable ou matériau composite", "isCorrect": True},
                        {"text": "En acier galvanisé classique traité anti rouille", "isCorrect": False},
                        {"text": "En aluminium souple et facilement malléable", "isCorrect": False},
                        {"text": "En fer forgé peint avec un revêtement", "isCorrect": False}
                    ],
                    "correction": "L'inox ou les matériaux composites alimentaires sont exigés par la réglementation car ils sont inaltérables, non poreux et supportent les agents de désinfection."
                },
                {
                    "questionNumber": 17,
                    "question": "Sur le document de livraison d'un bovin adulte que signifie la classification dans la catégorie V ?",
                    "answerOptions": [
                        {"text": "Il s'agit d'une génisse n'ayant jamais vêlé", "isCorrect": True},
                        {"text": "Il s'agit obligatoirement d'une vache laitière de réforme ayant atteint un âge particulièrement avancé et destinée au hachage industriel", "isCorrect": False},
                        {"text": "Il s'agit d'un veau lourd élevé sous la mère et abattu avant l'âge de huit mois", "isCorrect": False},
                        {"text": "Il s'agit d'un jeune bovin mâle non castré nourri exclusivement aux céréales dans un atelier d'engraissement", "isCorrect": False}
                    ],
                    "correction": "Selon la grille de classement EUROP, la lettre V désigne une femelle n'ayant pas vêlé, la lettre D désigne une vache, et la lettre A un jeune bovin mâle."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel conditionnement est recommandé pour le stockage des volailles effilées afin de limiter les risques sanitaires ?",
                    "answerOptions": [
                        {"text": "Un film plastique individuel étanche", "isCorrect": True},
                        {"text": "Un filet en coton fortement aéré", "isCorrect": False},
                        {"text": "Une caisse en bois brut ajourée", "isCorrect": False},
                        {"text": "Un papier kraft épais non traité", "isCorrect": False}
                    ],
                    "correction": "Les volailles possèdent une forte charge bactérienne cutanée. Un conditionnement étanche empêche les exsudats de contaminer les viandes de boucherie environnantes."
                },
                {
                    "questionNumber": 19,
                    "question": "À quelle fréquence un contrôle de l'état de fraîcheur des stocks en chambre froide est-il préconisé ?",
                    "answerOptions": [
                        {"text": "Quotidiennement avant le début du travail", "isCorrect": True},
                        {"text": "Une seule fois par semaine calendaire", "isCorrect": False},
                        {"text": "Uniquement lors de l'inventaire physique mensuel", "isCorrect": False},
                        {"text": "Exclusivement à chaque livraison du fournisseur", "isCorrect": False}
                    ],
                    "correction": "Le tri et l'élimination des produits présentant un début d'altération poissage de surface, légère odeur doivent être quotidiens pour assainir l'environnement de stockage."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel phénomène microbiologique provoque le verdissement et l'odeur fétide autour de l'os fémoral en cas de mauvais ressuage ?",
                    "answerOptions": [
                        {"text": "Une putréfaction profonde liée au développement de bactéries anaérobies au cœur de la masse musculaire", "isCorrect": True},
                        {"text": "Une simple oxydation de surface due à un contact prolongé avec la lame en acier carbone du boucher lors de la préparation de la carcasse", "isCorrect": False},
                        {"text": "Une cristallisation rapide des sucs sanguins provoquée par une température de chambre froide beaucoup trop basse lors de l'arrivée", "isCorrect": False},
                        {"text": "Une réaction biochimique post mortem déclenchée par une alimentation inadaptée de l'animal dans les jours précédant l'abattage", "isCorrect": False}
                    ],
                    "correction": "L'odeur d'os survient si le refroidissement à cœur est trop lent. Les germes anaérobies de putréfaction se multiplient alors dans les tissus profonds près de l'os."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNIQUES DE TRANSFORMATION : DÉSOSSAGE, PARAGE ET DÉCOUPE (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNIQUES DE TRANSFORMATION : DÉSOSSAGE, PARAGE ET DÉCOUPE",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel couteau utilise le boucher pour retirer l'omoplate du quartier avant bovin ?",
                    "answerOptions": [
                        {"text": "Le couteau désosseur", "isCorrect": True},
                        {"text": "La feuille de boucher", "isCorrect": False},
                        {"text": "Le couteau à éplucher", "isCorrect": False},
                        {"text": "Le couperet lourd", "isCorrect": False}
                    ],
                    "correction": "Le couteau désosseur possède une lame courte et rigide permettant de suivre les contours osseux de la scapula avec précision sans abîmer les masses musculaires de l'épaule."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment se nomme l'action de retirer la membrane aponévrotique recouvrant un muscle ?",
                    "answerOptions": [
                        {"text": "Le parage à blanc", "isCorrect": True},
                        {"text": "Le dégraissage de surface", "isCorrect": False},
                        {"text": "L'épluchage des tissus", "isCorrect": False},
                        {"text": "Le nettoyage tendineux", "isCorrect": False}
                    ],
                    "correction": "Le parage à blanc ou épluchage consiste à enlever l'aponévrose, c'est à dire la membrane conjonctive externe, pour rendre le morceau parfaitement net avant le piéçage."
                },
                {
                    "questionNumber": 23,
                    "question": "Lors du désossage de la cuisse de bœuf quelle est la première étape anatomique ?",
                    "answerOptions": [
                        {"text": "Décrocher le tendon d'Achille pour dégager l'articulation fémoro tibiale rotulienne", "isCorrect": True},
                        {"text": "Inciser profondément le long de la gouttière ischiatique pour séparer la fausse araignée du bassin osseux avant de tirer sur le muscle fessier", "isCorrect": False},
                        {"text": "Retirer la rotule fémorale avec la pointe rigide du couteau désosseur", "isCorrect": False},
                        {"text": "Séparer le gîte à la noix de la diaphyse du fémur", "isCorrect": False}
                    ],
                    "correction": "La séparation de l'articulation du grasset fémoro tibiale rotulienne permet de désolidariser le tibia de la masse fémorale et d'amorcer le travail sur les muscles de la cuisse ronde."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel os constitue la base osseuse du rumsteck ?",
                    "answerOptions": [
                        {"text": "L'os coxal", "isCorrect": True},
                        {"text": "Le fémur", "isCorrect": False},
                        {"text": "La vertèbre sacrée", "isCorrect": False},
                        {"text": "Le tibia", "isCorrect": False}
                    ],
                    "correction": "Le rumsteck est situé sur la région fessière de l'animal dont la base osseuse principale est l'os coxal composant le bassin."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel muscle sépare t on de la tranche grasse lors de la découpe de la cuisse ?",
                    "answerOptions": [
                        {"text": "Le talon de la tranche", "isCorrect": True},
                        {"text": "Le gîte à la noix", "isCorrect": False},
                        {"text": "Le rond de gîte", "isCorrect": False},
                        {"text": "La poire et le merlan", "isCorrect": False}
                    ],
                    "correction": "La tranche grasse est parée en séparant le talon, un muscle plus nerveux souvent destiné à la viande hachée, pour ne conserver que la partie tendre pour les biftecks."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle scie manuelle est privilégiée pour découper une côte de bœuf avec précision ?",
                    "answerOptions": [
                        {"text": "La scie de boucher américaine", "isCorrect": True},
                        {"text": "La scie à ruban fixe", "isCorrect": False},
                        {"text": "La scie égoïne de découpe", "isCorrect": False},
                        {"text": "La scie circulaire pendulaire", "isCorrect": False}
                    ],
                    "correction": "La scie américaine, avec sa lame fine sous tension dans une monture métallique, offre la précision nécessaire pour trancher net le rachis et la côte sans esquilles."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est l'utilité première de la technique de l'entaillage sur les bords d'une escalope de veau ?",
                    "answerOptions": [
                        {"text": "Rompre la tension de la fine pellicule aponévrotique périphérique pour éviter la rétractation à la cuisson", "isCorrect": True},
                        {"text": "Retirer minutieusement l'ensemble des infiltrations graisseuses interstitielles situées entre les différents faisceaux musculaires composant la noix pâtissière de catégorie une", "isCorrect": False},
                        {"text": "Ficeler fermement les bords extérieurs pour lui donner une forme parfaitement cylindrique lors de son passage à la poêle", "isCorrect": False},
                        {"text": "Attendrir mécaniquement les fibres en frappant le centre géométrique avec la platine plate du couperet lourd", "isCorrect": False}
                    ],
                    "correction": "Entailler les bords ou ciseler l'aponévrose empêche l'escalope de se recroqueviller sous l'effet de la chaleur vive, garantissant une cuisson uniforme et une belle présentation."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel morceau de viande bovine contient la vertèbre atlas ?",
                    "answerOptions": [
                        {"text": "Le collier", "isCorrect": True},
                        {"text": "L'entrecôte", "isCorrect": False},
                        {"text": "Le faux filet", "isCorrect": False},
                        {"text": "Le plat de côtes", "isCorrect": False}
                    ],
                    "correction": "L'atlas est la toute première vertèbre cervicale articulée avec le crâne. Elle se trouve donc à l'extrémité antérieure du collier."
                },
                {
                    "questionNumber": 29,
                    "question": "Dans l'épaule de veau quel muscle correspond au macreuse ?",
                    "answerOptions": [
                        {"text": "Le triceps brachial de l'épaule", "isCorrect": True},
                        {"text": "Le muscle supra épineux", "isCorrect": False},
                        {"text": "Le muscle infra épineux", "isCorrect": False},
                        {"text": "Le grand dorsal du dos", "isCorrect": False}
                    ],
                    "correction": "La macreuse correspond principalement au triceps brachial, situé à l'arrière de la scapula, utilisé pour les sautés ou les rôtis selon la qualité."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel os délimite la fin du faux filet et le début de l'entrecôte sur la carcasse ?",
                    "answerOptions": [
                        {"text": "La dernière vertèbre dorsale", "isCorrect": True},
                        {"text": "La première vertèbre lombaire", "isCorrect": False},
                        {"text": "La vertèbre sacrée numéro un", "isCorrect": False},
                        {"text": "La septième vertèbre cervicale", "isCorrect": False}
                    ],
                    "correction": "Le faux-filet s'appuie sur les vertèbres lombaires dépourvues de côtes, tandis que l'entrecôte repose sur les vertèbres dorsales ou thoraciques attenantes aux côtes. La charnière est donc entre dorsales et lombaires."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle précaution technique faut il prendre lors du désossage de l'épaule d'agneau en vue d'un rôti ?",
                    "answerOptions": [
                        {"text": "Dégager l'os de la palette sans trouer la peau extérieure pour conserver la tenue", "isCorrect": True},
                        {"text": "Séparer chaque muscle un par un en retirant toutes les aponévroses internes avant de reconstituer artificiellement l'épaule avec un filet élastique très serré", "isCorrect": False},
                        {"text": "Couper systématiquement le cartilage de prolongement avec la feuille de boucher avant de désosser", "isCorrect": False},
                        {"text": "Briser l'os de l'humérus en deux parties distinctes pour faciliter grandement son extraction par le haut", "isCorrect": False}
                    ],
                    "correction": "L'épaule d'agneau roulée doit présenter une belle esthétique extérieure. Il est crucial de déjointer la scapula et l'humérus en glissant la lame contre l'os sans percer l'enveloppe charnue."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel morceau de porc est obtenu en désossant la région lombaire ?",
                    "answerOptions": [
                        {"text": "La longe ou filet", "isCorrect": True},
                        {"text": "La pointe d'échine", "isCorrect": False},
                        {"text": "Le travers de porc", "isCorrect": False},
                        {"text": "La palette à rôtir", "isCorrect": False}
                    ],
                    "correction": "La longe correspond à la région lombaire du porc, d'où l'on tire les côtes premières, secondes, filet et le filet mignon."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est l'outil indispensable pour retirer la couenne d'une poitrine de porc ?",
                    "answerOptions": [
                        {"text": "Le couteau tranchelard", "isCorrect": True},
                        {"text": "La scie égoïne", "isCorrect": False},
                        {"text": "Le couperet lourd", "isCorrect": False},
                        {"text": "L'aiguille à brider", "isCorrect": False}
                    ],
                    "correction": "Le tranchelard possède une lame longue et rigide permettant de réaliser une coupe plane et continue sous le gras dur pour retirer la couenne proprement."
                },
                {
                    "questionNumber": 34,
                    "question": "Que désigne l'expression piécer une viande sur le billot ?",
                    "answerOptions": [
                        {"text": "Découper un muscle en portions", "isCorrect": True},
                        {"text": "Recoudre un morceau fortement déchiré", "isCorrect": False},
                        {"text": "Piquer la viande de lardons", "isCorrect": False},
                        {"text": "Séparer les os des muscles", "isCorrect": False}
                    ],
                    "correction": "Le piéçage est l'ultime étape de la découpe, consistant à détailler le muscle paré en portions individuelles biftecks escalopes selon un calibrage précis."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment procède t on pour préparer un carré de porc à la française ?",
                    "answerOptions": [
                        {"text": "Il faut manchonner l'extrémité des côtes en retirant la chair pour dégager l'os", "isCorrect": True},
                        {"text": "Il est indispensable de retirer l'intégralité de la colonne vertébrale puis de séparer chaque côte individuellement avant de les ficeler de nouveau ensemble", "isCorrect": False},
                        {"text": "Il suffit de scier les vertèbres lombaires sans toucher à la longueur des os costaux", "isCorrect": False},
                        {"text": "On retire complètement les os pour ne garder que la noix de viande purement cylindrique", "isCorrect": False}
                    ],
                    "correction": "Le manchonnage consiste à dénuder l'extrémité supérieure des côtes sur quelques centimètres pour une présentation esthétique et soignée du carré rôti."
                },
                {
                    "questionNumber": 36,
                    "question": "Dans le quartier arrière bovin quelle est la base osseuse du flanchet ?",
                    "answerOptions": [
                        {"text": "Les extrémités des cartilages costaux", "isCorrect": True},
                        {"text": "La symphyse pubienne du bassin osseux", "isCorrect": False},
                        {"text": "La rotule articulaire du grasset fémoral", "isCorrect": False},
                        {"text": "Le sternum plat de la poitrine charnue", "isCorrect": False}
                    ],
                    "correction": "Le flanchet est un muscle de l'abdomen constitué de la tunique abdominale, il se rattache aux cartilages de prolongement des dernières côtes."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment appelle t on la fine pellicule de surface sur le filet de bœuf ?",
                    "answerOptions": [
                        {"text": "La membrane aponévrotique ou chainette", "isCorrect": True},
                        {"text": "Le derme épidermique totalement externe", "isCorrect": False},
                        {"text": "Le gras de couverture très dur", "isCorrect": False},
                        {"text": "Le péritoine tapissant de la cavité", "isCorrect": False}
                    ],
                    "correction": "Le filet est recouvert d'une fine aponévrose qu'il faut retirer lors du parage à blanc, ainsi que de la chaînette, un muscle long et nerveux qui le borde."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est l'erreur à ne surtout pas commettre lors de la découpe des biftecks dans une tranche grasse ?",
                    "answerOptions": [
                        {"text": "Trancher parallèlement au fil de la viande ce qui la rendrait extrêmement dure sous la dent", "isCorrect": True},
                        {"text": "Appuyer trop fortement sur le couteau désosseur ce qui risquerait de séparer complètement les différents faisceaux musculaires composant la noix de la tranche grasse", "isCorrect": False},
                        {"text": "Laisser une épaisseur de gras de couverture largement supérieure à cinq millimètres sur tout le pourtour extérieur du muscle", "isCorrect": False},
                        {"text": "Utiliser un couteau alvéolé spécifique qui laisserait des marques disgracieuses et profondes sur la surface de coupe de la viande rouge", "isCorrect": False}
                    ],
                    "correction": "Les viandes à griller doivent impérativement être piécées perpendiculairement aux fibres musculaires trancher à travers le fil. Cela sectionne les fibres et assure la tendreté lors de la mastication."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel nœud de ficelage est réglementaire pour maintenir un rôti de veau ?",
                    "answerOptions": [
                        {"text": "Le nœud de boucher coulant", "isCorrect": True},
                        {"text": "Le nœud plat marin classique", "isCorrect": False},
                        {"text": "Le nœud en huit fortement croisé", "isCorrect": False},
                        {"text": "Le nœud d'arrimage fixe industriel", "isCorrect": False}
                    ],
                    "correction": "Le nœud de boucher est un nœud coulant autobloquant permettant de serrer fermement la viande pour lui donner une forme cylindrique qui résistera à la cuisson."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment procède t on techniquement pour préparer une tranche de paleron destinée à être grillée en bifteck ?",
                    "answerOptions": [
                        {"text": "Fendre le muscle dans sa longueur pour en extraire intégralement l'épaisse bande aponévrotique gélatineuse centrale", "isCorrect": True},
                        {"text": "Trancher de manière transversale à travers le muscle épais en prenant soin de ne pas entailler le cartilage de la scapula situé juste en dessous", "isCorrect": False},
                        {"text": "Scier l'articulation de l'épaule en diagonale pour accéder directement à la jointure tendineuse profonde de la macreuse", "isCorrect": False},
                        {"text": "Retirer uniquement la fine membrane de surface avec la pointe du tranchelard sans jamais ouvrir le cœur charnu", "isCorrect": False}
                    ],
                    "correction": "Le paleron à griller appelé surprise nécessite l'ablation totale du nerf central ou aponévrose interne. On clive le morceau en deux pour retirer ce tissu très dur en cuisson rapide."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : ÉLABORATION DES PRÉPARATIONS BOUCHÈRES CRUES ET CHARCUTIÈRES (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ÉLABORATION DES PRÉPARATIONS BOUCHÈRES CRUES ET CHARCUTIÈRES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel boyau naturel de mouton utilise t on pour la fabrication des merguez ?",
                    "answerOptions": [
                        {"text": "Le menu", "isCorrect": True},
                        {"text": "Le chaudin", "isCorrect": False},
                        {"text": "La baudruche", "isCorrect": False},
                        {"text": "Le fuseau", "isCorrect": False}
                    ],
                    "correction": "Le menu de mouton, d'un calibre fin généralement 20 à 24 millimètres, est le boyau naturel idéal et traditionnel pour embosser les pâtes fines comme les merguez ou les chipolatas."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la fonction principale du sel nitrité dans les charcuteries ?",
                    "answerOptions": [
                        {"text": "Fixer la couleur rouge et empêcher le botulisme", "isCorrect": True},
                        {"text": "Accélérer le séchage naturel en surface du produit", "isCorrect": False},
                        {"text": "Remplacer le poivre noir dans l'assaisonnement de base", "isCorrect": False},
                        {"text": "Augmenter le poids de la préparation par hydratation", "isCorrect": False}
                    ],
                    "correction": "Le sel nitrité joue un rôle de conservateur en bloquant le développement de Clostridium botulinum et permet de maintenir la coloration rosée ou rouge des viandes charcutières après cuisson ou séchage."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est l'utilité d'ajouter de la glace pilée dans la cuve du cutter lors du hachage d'une pâte fine ?",
                    "answerOptions": [
                        {"text": "Maintenir une température basse pour éviter la fonte des graisses et la rupture de l'émulsion protéique", "isCorrect": True},
                        {"text": "Provoquer un choc thermique extrêmement violent qui va détruire la quasi totalité de la flore bactérienne pathogène naturellement présente au cœur de la viande crue", "isCorrect": False},
                        {"text": "Diluer fortement les épices de la recette pour obtenir un goût beaucoup moins prononcé en bouche après la phase de cuisson au four vapeur", "isCorrect": False},
                        {"text": "Nettoyer simultanément les lames rotatives en acier inoxydable pour faciliter grandement le travail de plonge du matériel à la fin de la journée de production", "isCorrect": False}
                    ],
                    "correction": "Le frottement à haute vitesse des couteaux du cutter dégage une forte chaleur. La glace maintient la pâte sous les 12 degrés Celsius, garantissant une bonne liaison entre l'eau, le gras et les protéines musculaires."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel gras de porc privilégie t on pour la fabrication de rillettes traditionnelles ?",
                    "answerOptions": [
                        {"text": "Le gras dur de bardière", "isCorrect": True},
                        {"text": "Le gras mou de panne", "isCorrect": False},
                        {"text": "La graisse de rognon purifiée", "isCorrect": False},
                        {"text": "Le gras interstitiel des jambons", "isCorrect": False}
                    ],
                    "correction": "La bardière, ou gras de dos, est un gras ferme qui fond lentement et apporte la texture caractéristique et la tenue recherchée lors de la cuisson prolongée des rillettes."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment nomme t on l'opération consistant à remplir un boyau de farce ?",
                    "answerOptions": [
                        {"text": "L'embossage", "isCorrect": True},
                        {"text": "Le bardage", "isCorrect": False},
                        {"text": "Le malaxage", "isCorrect": False},
                        {"text": "Le cutterage", "isCorrect": False}
                    ],
                    "correction": "L'embossage ou poussage s'effectue à l'aide d'un poussoir hydraulique ou manuel pour introduire la mêlée dans un boyau naturel ou artificiel sans y inclure d'air."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le ratio maigre et gras généralement admis pour réaliser une farce à saucisse crue équilibrée ?",
                    "answerOptions": [
                        {"text": "Soixante quinze pourcent de viandes maigres pour vingt cinq pourcent de gras dur", "isCorrect": True},
                        {"text": "Exactement cinquante pourcent de muscles rouges soigneusement dénervés mélangés intimement à cinquante pourcent de panne fondue afin d'obtenir un produit fini très économique à la vente", "isCorrect": False},
                        {"text": "Quatre vingt dix pourcent de viande issue de l'épaule de porc et seulement dix pourcent de gras liquide injecté directement sous haute pression dans la cuve", "isCorrect": False},
                        {"text": "Un tiers de viande bovine un tiers de viande de veau et un tiers de viande de porc sans aucune adjonction de matière grasse extérieure", "isCorrect": False}
                    ],
                    "correction": "Une proportion de 75/25 environ trois quarts de maigre d'épaule et un quart de gras de poitrine ou bardière permet d'obtenir une saucisse moelleuse à la cuisson, ni trop sèche ni trop grasse."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel additif naturel est fréquemment utilisé comme liant dans un pâté de campagne ?",
                    "answerOptions": [
                        {"text": "L'œuf frais ou pasteurisé", "isCorrect": True},
                        {"text": "La poudre de lait écrémé", "isCorrect": False},
                        {"text": "La fécule de pomme de terre", "isCorrect": False},
                        {"text": "Le plasma sanguin déshydraté", "isCorrect": False}
                    ],
                    "correction": "L'œuf apporte des protéines qui coagulent à la cuisson, assurant ainsi la liaison naturelle de la mêlée hachée grossièrement pour la réalisation des terrines ou pâtés."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel morceau de bœuf est traditionnellement utilisé pour confectionner un carpaccio ?",
                    "answerOptions": [
                        {"text": "Le rond de gîte", "isCorrect": True},
                        {"text": "Le plat de côtes", "isCorrect": False},
                        {"text": "Le collier dénervé", "isCorrect": False},
                        {"text": "Le flanchet paré", "isCorrect": False}
                    ],
                    "correction": "Le rond de gîte est une pièce de cuisse maigre, ferme et régulière, idéale pour être tranchée extrêmement finement à la machine ou au couteau pour une consommation crue."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel liant est utilisé dans la préparation classique du boudin noir ?",
                    "answerOptions": [
                        {"text": "Le sang", "isCorrect": True},
                        {"text": "La farine", "isCorrect": False},
                        {"text": "La chapelure", "isCorrect": False},
                        {"text": "Le blanc", "isCorrect": False}
                    ],
                    "correction": "Le sang de porc est l'ingrédient principal et le liant exclusif du boudin noir traditionnel, coagulant à la chaleur lors de la cuisson en marmite."
                },
                {
                    "questionNumber": 50,
                    "question": "Pourquoi est il indispensable de piquer les saucissons avec une fine aiguille juste après l'embossage ?",
                    "answerOptions": [
                        {"text": "Pour chasser les poches d'air emprisonnées sous le boyau qui provoqueraient une altération du produit par oxydation", "isCorrect": True},
                        {"text": "Pour permettre à la fleur de surface de pénétrer profondément jusqu'au cœur de la viande hachée afin d'accélérer drastiquement le processus naturel de maturation de la charcuterie", "isCorrect": False},
                        {"text": "Pour marquer le produit de façon totalement indélébile afin de garantir son origine certifiée et sa traçabilité complète lors des fréquents contrôles sanitaires effectués en boutique", "isCorrect": False},
                        {"text": "Pour faciliter la perte de poids immédiate en expulsant l'excédent d'eau libre présente dans les viandes fraîches avant le passage obligatoire dans l'étuve de séchage", "isCorrect": False}
                    ],
                    "correction": "Le piquage perce la membrane naturelle pour expulser l'air résiduel. Cela évite le rancissement des graisses et empêche le boyau de se décoller de la mêlée pendant le séchage."
                },
                {
                    "questionNumber": 51,
                    "question": "À quelle température s'effectue généralement l'étuvage des saucissons secs ?",
                    "answerOptions": [
                        {"text": "Autour de vingt cinq degrés Celsius", "isCorrect": True},
                        {"text": "À plus de soixante degrés Celsius", "isCorrect": False},
                        {"text": "Strictement en dessous de zéro degré", "isCorrect": False},
                        {"text": "À dix degrés Celsius constants", "isCorrect": False}
                    ],
                    "correction": "L'étuvage fermentation se déroule dans une atmosphère chaude 22 à 26 °C et humide pour déclencher l'action des ferments lactiques, faire baisser le pH et favoriser l'apparition de la fleur."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment nomme t on le fin tissu graisseux utilisé pour envelopper les crépinettes ?",
                    "answerOptions": [
                        {"text": "La toilette de porc", "isCorrect": True},
                        {"text": "La couenne découennée", "isCorrect": False},
                        {"text": "La baudruche naturelle", "isCorrect": False},
                        {"text": "Le péritoine séché", "isCorrect": False}
                    ],
                    "correction": "La toilette ou crépine est une fine membrane veinée de gras issue de la cavité abdominale du porc. Elle fond à la cuisson tout en maintenant la forme de la préparation."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est l'action principale recherchée lors du malaxage prolongé d'une chair à saucisse ?",
                    "answerOptions": [
                        {"text": "Extraire les protéines solubles pour créer un liant naturel garantissant la cohésion de la mêlée", "isCorrect": True},
                        {"text": "Augmenter considérablement le volume de la préparation en incorporant une quantité massive d'air ambiant dans le but exclusif de générer un bénéfice commercial beaucoup plus important à la revente", "isCorrect": False},
                        {"text": "Écraser complètement les morceaux de gras dur pour les rendre totalement invisibles à l'œil nu du consommateur lors de l'achat en vitrine réfrigérée", "isCorrect": False},
                        {"text": "Dissoudre intégralement les gros grains de poivre noir et les herbes aromatiques pour éviter que le client ne tombe sur des morceaux durs sous la dent lors de la mastication", "isCorrect": False}
                    ],
                    "correction": "Le pétrissage ou malaxage libère l'actine et la myosine, des protéines myofibrillaires qui agissent comme une colle naturelle en liant l'eau, le gras et le maigre ensemble."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel type de saumurage est préconisé pour préparer rapidement un jambon blanc ?",
                    "answerOptions": [
                        {"text": "Le saumurage par injection intramusculaire", "isCorrect": True},
                        {"text": "Le salage au sel sec frotté", "isCorrect": False},
                        {"text": "Le saumurage par immersion statique prolongée", "isCorrect": False},
                        {"text": "Le salage par fumage à froid", "isCorrect": False}
                    ],
                    "correction": "L'injection de saumure à l'aide d'une multi aiguilles permet de répartir uniformément le sel et les conservateurs au cœur du muscle volumineux en un temps record."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle épice colore le chorizo espagnol crû ?",
                    "answerOptions": [
                        {"text": "Le piment doux", "isCorrect": True},
                        {"text": "Le curcuma moulu", "isCorrect": False},
                        {"text": "Le safran véritable", "isCorrect": False},
                        {"text": "Le poivre gris", "isCorrect": False}
                    ],
                    "correction": "Le pimenton paprika ou piment doux est l'épice caractéristique du chorizo, lui conférant sa teinte rouge brique intense et son goût fumé typique."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle est la fonction du barattage dans la fabrication des jambons cuits ?",
                    "answerOptions": [
                        {"text": "Répartir la saumure et attendrir les fibres musculaires", "isCorrect": True},
                        {"text": "Cuire lentement la viande grâce à une friction mécanique", "isCorrect": False},
                        {"text": "Dégraisser l'extérieur du muscle de sa couenne épaisse", "isCorrect": False},
                        {"text": "Fumer le produit à l'aide de sciure de hêtre", "isCorrect": False}
                    ],
                    "correction": "Effectué sous vide dans un tambour rotatif, le barattage malaxe la viande injectée. Cela favorise l'absorption totale de la saumure et l'extraction des protéines de surface assurant la cohésion au moulage."
                },
                {
                    "questionNumber": 57,
                    "question": "Pourquoi utilise t on du vin blanc acide dans certaines marinades pour viandes de bœuf destinées aux brochettes ?",
                    "answerOptions": [
                        {"text": "L'acidité du liquide attaque les fibres conjonctives de la viande ce qui permet de l'attendrir avant le passage sur le gril", "isCorrect": True},
                        {"text": "L'alcool contenu dans le vin agit comme un puissant désinfectant naturel capable d'éliminer instantanément la bactérie listeria monocytogenes potentiellement présente sur les plans de travail du laboratoire de découpe", "isCorrect": False},
                        {"text": "Le liquide permet de masquer complètement l'odeur très forte et désagréable d'une viande qui aurait largement dépassé sa date limite de consommation réglementaire depuis plusieurs jours", "isCorrect": False},
                        {"text": "Les tanins du vin réagissent chimiquement avec la myoglobine du muscle pour transformer une viande très pâle en une chair rouge vif particulièrement vendeuse en vitrine", "isCorrect": False}
                    ],
                    "correction": "Les marinades acides vin, vinaigre, jus de citron dénaturent chimiquement les protéines de surface et solubilisent partiellement le collagène, rendant les morceaux plus tendres en bouche."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel boyau artificiel comestible utilise t on souvent pour les saucisses de type knack ?",
                    "answerOptions": [
                        {"text": "Le boyau de collagène bovin", "isCorrect": True},
                        {"text": "Le boyau en plastique microporeux", "isCorrect": False},
                        {"text": "Le boyau en cellulose striée", "isCorrect": False},
                        {"text": "Le boyau synthétique en polyamide", "isCorrect": False}
                    ],
                    "correction": "Le collagène, extrait des cuirs bovins, est extrudé pour former un boyau parfaitement régulier, fumable et totalement comestible, idéal pour la production de knacks."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est l'ingrédient de base du saindoux commercialisé en boucherie charcuterie ?",
                    "answerOptions": [
                        {"text": "La panne de porc fondue", "isCorrect": True},
                        {"text": "La graisse de bœuf rissolée", "isCorrect": False},
                        {"text": "Le suif de mouton clarifié", "isCorrect": False},
                        {"text": "L'huile de tournesol hydrogénée", "isCorrect": False}
                    ],
                    "correction": "Le saindoux est obtenu par la fonte à feu doux de la panne, la graisse de très haute qualité entourant les rognons du porc, donnant une matière grasse d'un blanc pur."
                },
                {
                    "questionNumber": 60,
                    "question": "Lors de la confection d'un rôti de bœuf bardé pourquoi la barde ne doit elle pas faire plusieurs tours complets autour de la pièce ?",
                    "answerOptions": [
                        {"text": "Une épaisseur excessive empêcherait la chaleur d'atteindre le cœur du rôti et donnerait un goût de graisse fondue trop prononcé", "isCorrect": True},
                        {"text": "Le coût d'achat au kilo de la fine lanière de lard blanc est devenu tellement excessif qu'il réduirait à néant la marge commerciale nette de l'entreprise artisanale en fin de mois", "isCorrect": False},
                        {"text": "Les normes vétérinaires européennes interdisent formellement l'utilisation de gras d'origine porcine en contact direct avec de la viande bovine crue pour des raisons d'hygiène croisée", "isCorrect": False},
                        {"text": "Le fil de coton utilisé pour le ficelage glisserait irrémédiablement sur la surface lisse du gras ce qui déferait instantanément le nœud coulant de boucher dès la mise en rayon", "isCorrect": False}
                    ],
                    "correction": "La barde sert uniquement à protéger la face supérieure exposée à la chaleur du four pour éviter le dessèchement. Un excès de barde isole thermiquement la viande et altère l'équilibre gustatif."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : SCIENCES APPLIQUÉES : HYGIÈNE, MICROBIOLOGIE ET SÉCURITÉ AU TRAVAIL (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : SCIENCES APPLIQUÉES : HYGIÈNE, MICROBIOLOGIE ET SÉCURITÉ AU TRAVAIL",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la température réglementaire de l'eau des stérilisateurs à couteaux en boucherie ?",
                    "answerOptions": [
                        {"text": "Quatre vingt deux degrés Celsius minimum", "isCorrect": True},
                        {"text": "Soixante cinq degrés Celsius constants", "isCorrect": False},
                        {"text": "Cent degrés Celsius ébullition franche", "isCorrect": False},
                        {"text": "Cinquante degrés Celsius avec ajout de chlore", "isCorrect": False}
                    ],
                    "correction": "La réglementation sanitaire impose une température minimale de 82 °C pour assurer la destruction thermique des germes pathogènes sur les lames et les manches des outils de découpe."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel micro organisme psychrotrophe redouté en boucherie se développe aux températures de réfrigération ?",
                    "answerOptions": [
                        {"text": "Listeria monocytogenes", "isCorrect": True},
                        {"text": "Salmonella typhimurium", "isCorrect": False},
                        {"text": "Staphylococcus aureus", "isCorrect": False},
                        {"text": "Escherichia coli", "isCorrect": False}
                    ],
                    "correction": "Listeria monocytogenes est une bactérie psychrotrophe capable de se multiplier lentement même entre 0 et 4 °C, rendant le nettoyage rigoureux des chambres froides indispensable."
                },
                {
                    "questionNumber": 63,
                    "question": "Que caractérise le principe de la marche en avant dans l'organisation d'un laboratoire de transformation ?",
                    "answerOptions": [
                        {"text": "La séparation absolue dans l'espace ou le temps entre les secteurs souillés et les zones de manipulation des produits finis propres", "isCorrect": True},
                        {"text": "Le déplacement physique exclusif et unilatéral de tout le personnel de production de l'avant vers l'arrière du bâtiment afin de ne jamais croiser les clients présents dans la zone de vente au détail", "isCorrect": False},
                        {"text": "L'ordre strict d'utilisation des produits chimiques détergents puis désinfectants avant de procéder au rinçage final à l'eau claire et au raclage minutieux des sols de l'atelier de boucherie charcuterie", "isCorrect": False},
                        {"text": "La succession logique des opérations de découpe partant toujours du désossage des quartiers arrière bovins pour s'achever par la préparation méticuleuse des bas morceaux destinés aux viandes à braiser ou à bouillir", "isCorrect": False}
                    ],
                    "correction": "La marche en avant évite les contaminations croisées en empêchant tout retour en arrière d'un produit en cours d'élaboration vers une zone souillée, comme la réception ou la plonge."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel équipement de protection individuelle est obligatoire lors des opérations de désossage ?",
                    "answerOptions": [
                        {"text": "Le tablier en cotte de mailles", "isCorrect": True},
                        {"text": "Le masque filtrant respiratoire", "isCorrect": False},
                        {"text": "Les lunettes de protection teintées", "isCorrect": False},
                        {"text": "Le casque antibruit de chantier", "isCorrect": False}
                    ],
                    "correction": "Le tablier métallique en anneaux d'acier inoxydable est un EPI indispensable pour protéger l'artisan contre les risques de perforation abdominale ou fémorale par le couteau."
                },
                {
                    "questionNumber": 65,
                    "question": "Que signifie l'acronyme PMS en hygiène alimentaire ?",
                    "answerOptions": [
                        {"text": "Plan de maîtrise sanitaire", "isCorrect": True},
                        {"text": "Protocole de manipulation sécurisé", "isCorrect": False},
                        {"text": "Programme de nettoyage standard", "isCorrect": False},
                        {"text": "Protection microbiologique stricte", "isCorrect": False}
                    ],
                    "correction": "Le Plan de Maîtrise Sanitaire regroupe les bonnes pratiques d'hygiène, le plan HACCP ainsi que les procédures de traçabilité et de gestion des non-conformités."
                },
                {
                    "questionNumber": 66,
                    "question": "Pourquoi le port d'une coiffe englobante est il strictement imposé à l'ensemble du personnel manipulant les viandes nues ?",
                    "answerOptions": [
                        {"text": "Pour prévenir la chute accidentelle de cheveux et de pellicules porteurs de bactéries pathogènes directement sur les surfaces de travail et les matières premières alimentaires", "isCorrect": True},
                        {"text": "Pour maintenir la température corporelle de l'artisan boucher à un niveau parfaitement constant lors de ses passages fréquents et prolongés entre la chambre froide négative et le laboratoire de préparation climatisé", "isCorrect": False},
                        {"text": "Pour garantir une uniformité visuelle absolue de la tenue professionnelle afin de rassurer immédiatement la clientèle exigeante sur la rigueur et l'excellence des procédures sanitaires de l'établissement", "isCorrect": False},
                        {"text": "Pour éviter que les cheveux longs ne se prennent accidentellement dans le mécanisme rotatif des hachoirs électriques ou des mélangeurs industriels lors des phases de nettoyage en profondeur", "isCorrect": False}
                    ],
                    "correction": "Les cheveux et le cuir chevelu hébergent naturellement des bactéries pathogènes comme le Staphylocoque doré. La coiffe charlotte ou calot limite ce risque majeur de contamination croisée."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle famille de produits chimiques utilise t on en priorité pour dissoudre les graisses tenaces sur les billots ?",
                    "answerOptions": [
                        {"text": "Les détergents alcalins", "isCorrect": True},
                        {"text": "Les désinfectants acides", "isCorrect": False},
                        {"text": "Les solvants hydrocarbures", "isCorrect": False},
                        {"text": "Les abrasifs minéraux purs", "isCorrect": False}
                    ],
                    "correction": "Les détergents alcalins basiques ont la capacité de saponifier les graisses d'origine animale, facilitant ainsi leur mise en suspension et leur évacuation lors du rinçage à l'eau chaude."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment doit on stocker les couteaux de travail pendant une pause de courte durée ?",
                    "answerOptions": [
                        {"text": "Immergés dans le stérilisateur à couteaux", "isCorrect": True},
                        {"text": "Posés à plat sur la planche à découper", "isCorrect": False},
                        {"text": "Piqués directement dans le billot en bois", "isCorrect": False},
                        {"text": "Essuyés et rangés dans un tiroir sec", "isCorrect": False}
                    ],
                    "correction": "Placer le couteau dans le stérilisateur à 82 °C entre deux utilisations permet de bloquer instantanément la prolifération bactérienne sur la lame souillée par les sucs de viande."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel parasite est systématiquement recherché lors de l'inspection vétérinaire de la viande de porc ?",
                    "answerOptions": [
                        {"text": "La trichine", "isCorrect": True},
                        {"text": "Le ténia saginata", "isCorrect": False},
                        {"text": "La douve du foie", "isCorrect": False},
                        {"text": "L'ascaris suum", "isCorrect": False}
                    ],
                    "correction": "La trichinella spiralis est un nématode parasite dangereux pour l'homme, transmissible par l'ingestion de viande porcine crue ou mal cuite. Le test trichine est donc obligatoire."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle est l'action spécifique d'un agent désinfectant appliqué lors du protocole de nettoyage de fin de journée ?",
                    "answerOptions": [
                        {"text": "Détruire ou inactiver les micro organismes résiduels présents sur les surfaces préalablement nettoyées et rincées afin d'abaisser la charge microbienne à un niveau sans danger", "isCorrect": True},
                        {"text": "Décoller mécaniquement et dissoudre chimiquement l'intégralité des souillures organiques fortement incrustées dans les micro rayures des planches à découper en polyéthylène haute densité lors des découpes intenses", "isCorrect": False},
                        {"text": "Former un film protecteur complètement étanche et invisible sur les carrelages du laboratoire pour empêcher l'incrustation des graisses animales froides dès le lendemain matin", "isCorrect": False},
                        {"text": "Neutraliser instantanément les odeurs de viande putréfiée émanant des siphons d'évacuation des eaux usées en libérant un puissant parfum de synthèse chimique durable", "isCorrect": False}
                    ],
                    "correction": "La désinfection ne lave pas. Elle intervient toujours après la phase de détergence pour tuer la flore microbienne invisible qui a survécu au nettoyage mécanique."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle zone de température correspond à la multiplication optimale de la plupart des bactéries pathogènes alimentaires ?",
                    "answerOptions": [
                        {"text": "Entre dix et soixante degrés Celsius", "isCorrect": True},
                        {"text": "Entre zéro et quatre degrés Celsius", "isCorrect": False},
                        {"text": "Entre soixante et cent degrés Celsius", "isCorrect": False},
                        {"text": "Entre moins dix huit et zéro degré Celsius", "isCorrect": False}
                    ],
                    "correction": "La plage comprise entre 10 °C et 63 °C est appelée zone de danger. C'est dans ce créneau thermique que les germes mésophiles responsables des intoxications se multiplient de manière exponentielle."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie l'obligation de traçabilité ascendante pour un artisan boucher ?",
                    "answerOptions": [
                        {"text": "Pouvoir retrouver l'origine exacte et le fournisseur de chaque matière première utilisée", "isCorrect": True},
                        {"text": "Transmettre au client la recette précise de la fabrication d'une spécialité charcutière", "isCorrect": False},
                        {"text": "Pouvoir identifier tous les clients ayant acheté un lot spécifique de viande hachée", "isCorrect": False},
                        {"text": "Enregistrer quotidiennement les températures de cuisson des plats préparés traiteur", "isCorrect": False}
                    ],
                    "correction": "La traçabilité ascendante permet de remonter la chaîne d'approvisionnement en cas d'alerte sanitaire, en identifiant rapidement le lot, l'abattoir et l'élevage d'origine."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le risque biomécanique principal lié à l'utilisation prolongée d'un couteau au manche inadapté ou usé ?",
                    "answerOptions": [
                        {"text": "L'apparition de troubles musculo squelettiques affectant gravement les articulations du poignet et du canal carpien suite aux gestes répétitifs sous forte tension", "isCorrect": True},
                        {"text": "Le détachement brutal de la lame en acier trempé lors d'un effort intense sur une articulation osseuse ce qui provoquerait une projection extrêmement violente et incontrôlable dans l'espace de travail du laboratoire", "isCorrect": False},
                        {"text": "La diffusion lente et pernicieuse de microparticules de matière plastique dégradée directement au cœur des fibres de la viande rouge lors du parage méticuleux des pièces nobles", "isCorrect": False},
                        {"text": "L'oxydation rapide et irréversible de l'alliage métallique de la mitre due à la stagnation prolongée de l'humidité corporelle combinée aux agents détergents puissants utilisés quotidiennement", "isCorrect": False}
                    ],
                    "correction": "Un manche glissant ou mal dimensionné oblige le boucher à serrer excessivement la main, générant des TMS tendinites, syndrome du canal carpien qui représentent la première maladie professionnelle du secteur."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle est la durée légale de conservation des viandes hachées préparées à l'avance par le boucher ?",
                    "answerOptions": [
                        {"text": "Jour de fabrication plus un jour", "isCorrect": True},
                        {"text": "Jour de fabrication plus trois jours", "isCorrect": False},
                        {"text": "Jour de fabrication plus cinq jours", "isCorrect": False},
                        {"text": "Aucune durée limite spécifique", "isCorrect": False}
                    ],
                    "correction": "Le hachage détruit les fibres et multiplie la surface d'échange avec l'oxygène, favorisant une croissance bactérienne explosive. La DLC est donc restreinte à une seule journée post fabrication."
                },
                {
                    "questionNumber": 75,
                    "question": "Dans le cadre de la méthode HACCP que représente la détermination d'un CCP ?",
                    "answerOptions": [
                        {"text": "L'identification d'un point critique pour la maîtrise d'un danger sanitaire", "isCorrect": True},
                        {"text": "Le calcul du coût de revient d'une préparation charcutière artisanale", "isCorrect": False},
                        {"text": "Le nettoyage complet et systématique des plans de travail en acier inoxydable", "isCorrect": False},
                        {"text": "Le contrôle de la conformité du pesage lors de la vente au détail", "isCorrect": False}
                    ],
                    "correction": "Un CCP Critical Control Point désigne une étape opérationnelle où une mesure de contrôle indispensable peut être exercée pour prévenir ou éliminer un danger lié à la sécurité alimentaire."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle action est proscrite lors du nettoyage des sols du laboratoire de boucherie ?",
                    "answerOptions": [
                        {"text": "L'utilisation d'un jet d'eau sous haute pression orienté vers le sol", "isCorrect": True},
                        {"text": "Le raclage des eaux usées vers la grille du siphon d'évacuation", "isCorrect": False},
                        {"text": "L'application d'un produit dégraissant moussant sur le carrelage", "isCorrect": False},
                        {"text": "Le port de bottes de sécurité à semelles fortement crantées", "isCorrect": False}
                    ],
                    "correction": "Le jet haute pression fragmente les souillures au sol, créant un brouillard de micro gouttelettes chargées de bactéries aérosolisation qui vient contaminer les plans de travail et les viandes."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle règle stricte régit la décongélation des viandes destinées à être transformées en laboratoire ?",
                    "answerOptions": [
                        {"text": "L'opération doit s'effectuer exclusivement dans une enceinte réfrigérée entre zéro et quatre degrés Celsius à l'abri de toute contamination croisée", "isCorrect": True},
                        {"text": "La pièce de viande doit obligatoirement être totalement immergée dans un bain d'eau tiède maintenu artificiellement à une température constante de trente degrés Celsius afin d'accélérer le ramollissement des fibres musculaires", "isCorrect": False},
                        {"text": "Il est formellement exigé de laisser le produit à température ambiante sur un plan de travail en polyéthylène brut pendant une durée minimale de vingt quatre heures consécutives sans interruption", "isCorrect": False},
                        {"text": "La viande doit être soumise à une exposition directe aux rayonnements infrarouges puissants émis par les vitrines chauffantes de la boutique avant d'être immédiatement découpée", "isCorrect": False}
                    ],
                    "correction": "La décongélation lente au froid positif permet d'empêcher le réveil brutal des germes psychrotrophes de surface pendant que le cœur de la masse musculaire est encore durci par le gel."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel paramètre n'appartient pas aux composantes du cercle de Sinner pour le nettoyage ?",
                    "answerOptions": [
                        {"text": "L'exposition à la lumière naturelle", "isCorrect": True},
                        {"text": "L'action mécanique du brossage", "isCorrect": False},
                        {"text": "La température de l'eau utilisée", "isCorrect": False},
                        {"text": "Le temps de contact du produit", "isCorrect": False}
                    ],
                    "correction": "Le cercle de Sinner repose exclusivement sur quatre facteurs interdépendants mesurant l'efficacité d'une opération de nettoyage : la Température, l'Action mécanique, l'Action chimique et le Temps d'action."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est l'objectif premier d'une cellule de refroidissement rapide utilisée après la cuisson d'un jambon ou d'un pâté ?",
                    "answerOptions": [
                        {"text": "Franchir la zone de danger thermique comprise entre soixante trois et dix degrés Celsius en un délai maximal de cent vingt minutes", "isCorrect": True},
                        {"text": "Provoquer la surgélation instantanée du produit à moins dix huit degrés Celsius pour stopper net la division cellulaire bactérienne et figer les sucs interstitiels de la viande cuite avant son tranchage", "isCorrect": False},
                        {"text": "Évaporer la totalité de l'eau libre résiduelle contenue dans la mêlée charcutière afin de garantir une durée de conservation de plusieurs mois sur les étagères sèches non réfrigérées de la boutique", "isCorrect": False},
                        {"text": "Réchauffer rapidement les préparations alimentaires traiteur élaborées la veille afin de les proposer à la juste température de dégustation aux clients impatients dès l'ouverture matinale du commerce", "isCorrect": False}
                    ],
                    "correction": "Abaisser brutalement la température bloque la sporulation ainsi que la multiplication explosive des bactéries thermo résistantes qui auraient potentiellement survécu au barème de pasteurisation ou de cuisson."
                },
                {
                    "questionNumber": 80,
                    "question": "En cas de coupure profonde avec hémorragie abondante quelle est la première action de secourisme à réaliser ?",
                    "answerOptions": [
                        {"text": "Effectuer une compression manuelle directe sur la plaie", "isCorrect": True},
                        {"text": "Placer immédiatement le membre blessé sous l'eau très froide", "isCorrect": False},
                        {"text": "Appliquer un antiseptique pur à base de teinture d'iode", "isCorrect": False},
                        {"text": "Poser un garrot élastique serré au niveau de l'épaule", "isCorrect": False}
                    ],
                    "correction": "La compression directe effectuée avec un linge propre ou un pansement compressif stoppe mécaniquement le saignement abondant, juste avant de contacter les services médicaux d'urgence."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : COMMERCIALISATION, AMÉNAGEMENT DE LA VITRINE ET RELATION CLIENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : COMMERCIALISATION, AMÉNAGEMENT DE LA VITRINE ET RELATION CLIENT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Comment doit s'effectuer l'affichage du prix des viandes préemballées en libre service ?",
                    "answerOptions": [
                        {"text": "Au kilogramme et à la pièce", "isCorrect": True},
                        {"text": "Uniquement au poids net", "isCorrect": False},
                        {"text": "Selon le code barre lu", "isCorrect": False},
                        {"text": "Par portion individuelle", "isCorrect": False}
                    ],
                    "correction": "La législation impose d'indiquer à la fois le prix de vente à la pièce et le prix au kilogramme pour permettre la comparaison par le consommateur de manière transparente."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle mention est facultative sur l'étiquette de traçabilité d'un morceau de bœuf en vitrine traditionnelle ?",
                    "answerOptions": [
                        {"text": "Le nom de l'élevage de naissance", "isCorrect": True},
                        {"text": "Le nom du pays d'abattage", "isCorrect": False},
                        {"text": "Le numéro d'agrément de l'abattoir", "isCorrect": False},
                        {"text": "La catégorie de l'animal bovin", "isCorrect": False}
                    ],
                    "correction": "Seules les mentions du pays de naissance, d'élevage et d'abattage, ainsi que les numéros d'agrément sont obligatoires. Le nom de l'élevage relève d'une démarche de communication volontaire de l'artisan."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est le principe fondamental régissant la disposition des viandes crues et des produits cuits au sein d'une même banque réfrigérée ?",
                    "answerOptions": [
                        {"text": "Il faut impérativement aménager une séparation physique étanche avec des plaques en plexiglas ou créer un espace vide conséquent entre les produits crus et les préparations traiteur cuites afin de bloquer toute migration bactérienne croisée", "isCorrect": True},
                        {"text": "Il est strictement exigé de superposer les viandes rouges crues fortement exsudatives sur les clayettes supérieures tandis que les salaisons sèches et les pâtés cuits doivent être disposés sur les grilles inférieures pour faciliter la circulation de l'air froid ventilé généré par le moteur du meuble frigorifique", "isCorrect": False},
                        {"text": "Les viandes doivent être mélangées sans distinction d'origine", "isCorrect": False},
                        {"text": "Les viandes sont triées par prix de vente au kilogramme", "isCorrect": False}
                    ],
                    "correction": "La séparation physique stricte entre le cru et le cuit est une obligation sanitaire pour éviter que la flore microbienne naturelle de la viande crue ne contamine les produits cuits prêts à être consommés sans recuisson."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la température de fonctionnement requise pour une vitrine d'exposition présentant de la viande hachée préparée à l'avance ?",
                    "answerOptions": [
                        {"text": "Entre zéro et deux degrés Celsius", "isCorrect": True},
                        {"text": "Entre zéro et quatre degrés Celsius", "isCorrect": False},
                        {"text": "Strictement inférieure à moins deux degrés Celsius", "isCorrect": False},
                        {"text": "Autour de six degrés Celsius de moyenne", "isCorrect": False}
                    ],
                    "correction": "La viande hachée étant extrêmement sensible au développement bactérien en raison de l'éclatement des fibres, la réglementation exige une conservation stricte entre 0 °C et 2 °C en vitrine."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle condition légale est requise pour utiliser le titre professionnel d'Artisan Boucher ?",
                    "answerOptions": [
                        {"text": "Être titulaire du diplôme", "isCorrect": True},
                        {"text": "Avoir dix salariés minimum", "isCorrect": False},
                        {"text": "Vendre des produits locaux", "isCorrect": False},
                        {"text": "Travailler depuis cinq ans", "isCorrect": False}
                    ],
                    "correction": "Le titre d'artisan est réglementé par l'État et nécessite l'immatriculation au répertoire des métiers, conditionnée par la possession d'un diplôme de niveau CAP ou équivalent dans le métier exercé."
                },
                {
                    "questionNumber": 86,
                    "question": "Comment définit on la démarque connue dans la gestion comptable d'une boucherie artisanale ?",
                    "answerOptions": [
                        {"text": "Elle regroupe l'ensemble des marchandises dont la perte est précisément identifiée et enregistrée comme les produits avariés jetés à la poubelle ou les restes de parage invendables destinés à l'équarrissage", "isCorrect": True},
                        {"text": "Elle correspond exclusivement aux produits de très haute valeur marchande qui ont été dérobés furtivement par des clients malveillants directement dans les meubles de vente en libre service durant les heures d'affluence du samedi matin ou lors des fêtes de fin d'année", "isCorrect": False},
                        {"text": "La différence exacte entre le prix de gros payé à la centrale et le prix de détail final", "isCorrect": False},
                        {"text": "L'argent liquide systématiquement manquant dans le fond de caisse lors de la fermeture quotidienne", "isCorrect": False}
                    ],
                    "correction": "La démarque connue correspond aux pertes chiffrables et justifiées casses, retraits sanitaires, os, gras de parage par opposition à la démarque inconnue qui englobe les vols et les erreurs de caisse."
                },
                {
                    "questionNumber": 87,
                    "question": "Si le coût d'achat hors taxes d'une pièce de viande est de dix euros et son prix de vente toutes taxes comprises de vingt euros quel est le coefficient multiplicateur ?",
                    "answerOptions": [
                        {"text": "Le coefficient multiplicateur est de deux", "isCorrect": True},
                        {"text": "Le coefficient multiplicateur est de un virgule cinq", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur est de dix nets", "isCorrect": False},
                        {"text": "Le coefficient multiplicateur est de zéro virgule cinq", "isCorrect": False}
                    ],
                    "correction": "Le coefficient multiplicateur se calcule en divisant simplement le prix de vente TTC par le coût d'achat HT. Soit 20 divisé par 10 égal 2. Il permet de fixer rapidement le prix en boutique."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel élément décoratif est formellement interdit en vitrine réfrigérée au contact direct des viandes ?",
                    "answerOptions": [
                        {"text": "Le feuillage naturel non traité", "isCorrect": True},
                        {"text": "Le persil synthétique en plastique", "isCorrect": False},
                        {"text": "Les étiquettes en polypropylène lisse", "isCorrect": False},
                        {"text": "Les séparateurs en plexiglas transparent", "isCorrect": False}
                    ],
                    "correction": "Le feuillage naturel fougères, feuilles de vigne apporte une flore bactérienne tellurique et des moisissures. Seuls les éléments artificiels, lavables et aptes au contact alimentaire sont autorisés."
                },
                {
                    "questionNumber": 89,
                    "question": "Que certifie le logo hexagonal rouge et bleu portant la mention Viande de Veau Française ?",
                    "answerOptions": [
                        {"text": "Animal né élevé abattu en France", "isCorrect": True},
                        {"text": "Viande garantie issue de l'agriculture biologique", "isCorrect": False},
                        {"text": "Viande préparée de façon purement artisanale", "isCorrect": False},
                        {"text": "Animal nourri exclusivement au lait maternel", "isCorrect": False}
                    ],
                    "correction": "Le logo VVF Viande de Veau Française garantit au consommateur la traçabilité stricte d'un veau né, élevé et abattu sur le territoire national."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est l'attitude professionnelle appropriée face à un client se plaignant que sa viande bovine a rendu beaucoup d'eau à la cuisson ?",
                    "answerOptions": [
                        {"text": "Il faut lui expliquer calmement avec pédagogie que ce phénomène résulte probablement d'une baisse brutale de température lors de la cuisson d'une viande sortant juste du réfrigérateur ou d'un choc thermique dans une poêle insuffisamment chauffée", "isCorrect": True},
                        {"text": "Il est absolument impératif de lui rembourser intégralement son achat sur le champ tout en accusant ouvertement et publiquement le fournisseur de l'abattoir régional de pratiquer des injections frauduleuses d'eau saumurée au cœur des masses musculaires afin de gonfler artificiellement les poids de vente", "isCorrect": False},
                        {"text": "Il faut ignorer la remarque du client et passer sans transition à la personne suivante dans la file", "isCorrect": False},
                        {"text": "Il faut lui conseiller de manger de la viande de porc ou de la volaille pour éviter ces désagréments", "isCorrect": False}
                    ],
                    "correction": "L'exsudation à la cuisson est très souvent due à une mauvaise technique culinaire. Le rôle du boucher est de conseiller sur la préparation, notamment le chambrage de la viande avant cuisson."
                },
                {
                    "questionNumber": 91,
                    "question": "Pourquoi installe t on des éclairages LED à spectre rosé au dessus de la vitrine de boucherie traditionnelle ?",
                    "answerOptions": [
                        {"text": "Pour raviver visuellement la couleur rouge naturel de la myoglobine", "isCorrect": True},
                        {"text": "Pour détruire les bactéries de surface par rayonnement ultraviolet continu", "isCorrect": False},
                        {"text": "Pour diminuer drastiquement la consommation électrique du magasin nocturne", "isCorrect": False},
                        {"text": "Pour réchauffer légèrement la surface des produits exposés au froid intense", "isCorrect": False}
                    ],
                    "correction": "L'éclairage spécifique boucherie possède un spectre lumineux enrichi en longueurs d'ondes rouges. Il flatte l'œil et met en valeur la fraîcheur des viandes sans altérer la qualité du produit."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle pratique prévient efficacement la contamination croisée lors de l'encaissement d'un client au comptoir ?",
                    "answerOptions": [
                        {"text": "Utiliser un gant jetable ou une pince pour manipuler la viande", "isCorrect": True},
                        {"text": "Se laver les mains après chaque encaissement financier uniquement", "isCorrect": False},
                        {"text": "Encaisser l'argent avant de commencer à préparer la commande", "isCorrect": False},
                        {"text": "Désinfecter la monnaie avec une lingette virucide et bactéricide", "isCorrect": False}
                    ],
                    "correction": "La monnaie est un vecteur majeur de germes manuportés. L'utilisation d'une pince, d'un gant de service, ou la dissociation stricte des tâches entre préparation et encaissement est indispensable."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment formuler efficacement une proposition de vente additionnelle lors de l'achat d'un rôti de veau par un client ?",
                    "answerOptions": [
                        {"text": "Je vous propose d'agrémenter votre plat avec notre fond de veau maison ou quelques os à moelle préparés ce matin qui apporteront une texture onctueuse et des saveurs riches à votre sauce d'accompagnement lors de la cuisson", "isCorrect": True},
                        {"text": "Vous devriez impérativement acheter en supplément deux kilogrammes de nos merguez artisanales épicées et de nos chipolatas aux herbes fraîches car nous avons actuellement un surplus de stock extrêmement préoccupant qu'il faut absolument écouler avant la date limite de consommation de demain soir", "isCorrect": False},
                        {"text": "Je vous mets autre chose avec cela pour faire le compte rond en caisse", "isCorrect": False},
                        {"text": "Avez vous besoin d'un simple pot de moutarde forte industrielle pour dépanner", "isCorrect": False}
                    ],
                    "correction": "Une vente additionnelle réussie doit apporter une véritable plus-value au produit principal. Proposer un produit lié techniquement fond, os démontre le professionnalisme de l'artisan."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment se calcule précisément la marge brute commerciale dégagée sur un produit transformé en boutique ?",
                    "answerOptions": [
                        {"text": "Prix de vente hors taxes moins le coût de revient hors taxes", "isCorrect": True},
                        {"text": "Chiffre d'affaires journalier divisé par le nombre total de clients", "isCorrect": False},
                        {"text": "Prix de vente toutes taxes comprises multiplié par la taxe sur la valeur ajoutée", "isCorrect": False},
                        {"text": "Coût d'achat hors taxes plus l'intégralité des charges salariales patronales", "isCorrect": False}
                    ],
                    "correction": "La marge brute commerciale est la différence fondamentale entre le prix de vente HT et le coût de revient HT. Elle est essentielle pour couvrir les frais fixes du commerce et dégager un bénéfice net."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le taux de taxe sur la valeur ajoutée applicable en France sur une viande de boucherie crue non préparée ?",
                    "answerOptions": [
                        {"text": "Cinq virgule cinq pourcent", "isCorrect": True},
                        {"text": "Vingt pourcent", "isCorrect": False},
                        {"text": "Dix pourcent", "isCorrect": False},
                        {"text": "Deux virgule un pourcent", "isCorrect": False}
                    ],
                    "correction": "La viande fraîche crue, non transformée par des cuissons complexes, est considérée légalement comme un produit alimentaire de première nécessité. Elle bénéficie du taux réduit de TVA fixé à 5,5 %."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est l'utilité technique du papier paraffiné ou ingraissable utilisé pour emballer un bifteck lors de la vente au détail ?",
                    "answerOptions": [
                        {"text": "Il isole la viande de l'air ambiant tout en empêchant le sang et les exsudats de traverser l'emballage garantissant ainsi une hygiène parfaite lors du transport par le consommateur jusqu'à son domicile", "isCorrect": True},
                        {"text": "Il contient des agents chimiques conservateurs puissants qui migrent très lentement à travers la surface du muscle pour prolonger artificiellement la durée de conservation de la viande rouge de plusieurs semaines dans un réfrigérateur domestique mal réglé", "isCorrect": False},
                        {"text": "Il opère une légère réaction chimique exothermique qui pré cuit délicatement la surface extérieure de la pièce", "isCorrect": False},
                        {"text": "Il augmente artificiellement le poids final du produit pesé sur la balance au moment du passage en caisse", "isCorrect": False}
                    ],
                    "correction": "Le papier spécifiquement conçu pour la boucherie est doté d'une face traitée ingraissable qui retient l'humidité et les liquides, protégeant ainsi le produit de l'oxydation et garantissant un transport propre."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel équipement obligatoire garantit au client la justesse de la pesée lors d'un achat direct au comptoir ?",
                    "answerOptions": [
                        {"text": "Une balance homologuée avec sa vignette verte en cours de validité", "isCorrect": True},
                        {"text": "Un ticket de caisse détaillé obligatoirement imprimé en haute définition", "isCorrect": False},
                        {"text": "Une ardoise traditionnelle affichant les prix de gros fortement barrés", "isCorrect": False},
                        {"text": "Un cadran mécanique rétro éclairé fixé solidement au mur du fond", "isCorrect": False}
                    ],
                    "correction": "Les instruments de pesage à fonctionnement non automatique utilisés pour les transactions commerciales doivent subir une vérification métrologique périodique annuelle certifiée par une vignette verte visible du public."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel conseil de préparation donner à un client qui vient d'acheter une côte de bœuf épaisse pour une cuisson au barbecue ?",
                    "answerOptions": [
                        {"text": "Il est impératif de sortir la viande du réfrigérateur au moins une heure avant la cuisson pour qu'elle revienne à température ambiante évitant ainsi un choc thermique qui durcirait irrémédiablement les fibres musculaires", "isCorrect": True},
                        {"text": "Il faut absolument inciser profondément le cœur du muscle charnu avec un long couteau à dents puis y verser massivement de l'huile de tournesol pure afin de garantir que les flammes du charbon de bois calcinent intégralement la surface extérieure en un temps record", "isCorrect": False},
                        {"text": "Il est fortement recommandé de la faire bouillir préalablement dans une grande marmite d'eau salée frémissante", "isCorrect": False},
                        {"text": "Il faut la placer au congélateur pendant quinze minutes juste avant la cuisson pour raffermir les graisses", "isCorrect": False}
                    ],
                    "correction": "Le chambrage d'une pièce épaisse permet une diffusion homogène et progressive de la chaleur au cœur de la viande lors du passage sur la grille, garantissant une croûte saisie et un cœur tendre."
                },
                {
                    "questionNumber": 99,
                    "question": "Que signifie le label officiel européen AOP visible sur certains produits de charcuterie ou fromagerie vendus en boucherie ?",
                    "answerOptions": [
                        {"text": "Appellation d'Origine Protégée", "isCorrect": True},
                        {"text": "Artisanat d'Origine Paysanne", "isCorrect": False},
                        {"text": "Agrément Officiel Préfectoral", "isCorrect": False},
                        {"text": "Association des Ouvriers Producteurs", "isCorrect": False}
                    ],
                    "correction": "L'AOP désigne un produit d'excellence dont toutes les étapes de production, de transformation et d'élaboration ont lieu dans une aire géographique strictement délimitée, selon un cahier des charges rigoureux."
                },
                {
                    "questionNumber": 100,
                    "question": "Lors de la mise en place de la vitrine qu'appelle t on couramment le point chaud ou zone de chalandise prioritaire ?",
                    "answerOptions": [
                        {"text": "La zone centrale du meuble réfrigéré où le regard du client se porte spontanément dès son entrée dans le magasin", "isCorrect": True},
                        {"text": "L'endroit précis où se situe la sortie directe de la ventilation froide de la machine de refroidissement industriel", "isCorrect": False},
                        {"text": "Le compartiment sécurisé situé juste en dessous du tiroir de la caisse enregistreuse tactile du commerçant", "isCorrect": False},
                        {"text": "L'étagère supérieure arrière exclusivement dédiée au stockage temporaire des couteaux et outils de découpe", "isCorrect": False}
                    ],
                    "correction": "Le point chaud d'une vitrine est le centre d'attraction visuel, situé généralement au milieu, à hauteur des yeux ou légèrement en contrebas. C'est l'emplacement stratégique pour placer les nouveautés ou les promotions."
                }
            ]
        }
    }
}