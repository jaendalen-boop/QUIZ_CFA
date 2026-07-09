quiz_data = {
    "title": "Quiz CAP IMTB (Interventions en Maintenance Technique des Bâtiments) - 100 Questions",
    "themes": {
        1: {
            "name": "THÈME 1 : SANTÉ, SÉCURITÉ AU TRAVAIL ET HABILITATIONS",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Avant une intervention électrique, quelle action est vitale ?",
                    "answerOptions": [
                        {"text": "Condamner l'installation et vérifier l'absence de tension", "isCorrect": True},
                        {"text": "Porter des gants en cuir et installer un balisage rouge", "isCorrect": False},
                        {"text": "Remplacer le tableau de répartition par un modèle neuf", "isCorrect": False},
                        {"text": "Débrancher uniquement les appareils de forte puissance", "isCorrect": False}
                    ],
                    "correction": "La consignation, qui inclut la condamnation et la vérification d'absence de tension (VAT), est indispensable pour éviter l'électrisation."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le rôle précis d'un interrupteur différentiel ?",
                    "answerOptions": [
                        {"text": "Protéger les individus contre les fuites de courant vers le sol", "isCorrect": True},
                        {"text": "Protéger les circuits contre les surcharges et courts-circuits", "isCorrect": False},
                        {"text": "Mesurer la consommation électrique globale du bâtiment", "isCorrect": False},
                        {"text": "Activer le passage automatique au tarif des heures creuses", "isCorrect": False}
                    ],
                    "correction": "L'interrupteur différentiel détecte une différence d'intensité entre la phase et le neutre due à une fuite vers la terre, et coupe le circuit pour sauver des vies."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la couleur réglementaire du fil de protection ?",
                    "answerOptions": [
                        {"text": "Le conducteur doit être obligatoirement bicolore vert et jaune", "isCorrect": True},
                        {"text": "Le conducteur doit être obligatoirement de couleur bleu clair", "isCorrect": False},
                        {"text": "Le conducteur doit être obligatoirement de couleur rouge vif", "isCorrect": False},
                        {"text": "Le conducteur doit être obligatoirement bicolore gris et noir", "isCorrect": False}
                    ],
                    "correction": "La norme impose strictement le vert et jaune pour la liaison à la terre afin d'éviter toute confusion lors d'un raccordement."
                },
                {
                    "questionNumber": 4,
                    "question": "Que désigne exactement le sigle EPI sur un chantier ?",
                    "answerOptions": [
                        {"text": "Un équipement destiné à protéger physiquement le travailleur", "isCorrect": True},
                        {"text": "Une procédure d'évaluation préventive des incidents techniques", "isCorrect": False},
                        {"text": "Un entretien planifié des installations thermiques du bâtiment", "isCorrect": False},
                        {"text": "Une exigence professionnelle interne pour la gestion des stocks", "isCorrect": False}
                    ],
                    "correction": "L'Équipement de Protection Individuelle englobe les chaussures de sécurité, les casques, les lunettes ou encore les gants de manutention."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel équipement est indispensable pour utiliser une meuleuse ?",
                    "answerOptions": [
                        {"text": "Des lunettes couvrantes et des protections auditives adaptées", "isCorrect": True},
                        {"text": "De simples gants en tissu pour éviter les petites coupures", "isCorrect": False},
                        {"text": "Des lunettes de soleil classiques et des gants en latex fin", "isCorrect": False},
                        {"text": "Un masque en papier jetable et une casquette de chantier", "isCorrect": False}
                    ],
                    "correction": "La meuleuse projette des éclats métalliques à haute vitesse et génère un volume sonore très élevé, rendant ces protections obligatoires."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel type d'extincteur utiliser sur un feu d'origine électrique ?",
                    "answerOptions": [
                        {"text": "Un extincteur au dioxyde de carbone pour étouffer les flammes", "isCorrect": True},
                        {"text": "Un extincteur à eau pulvérisée sans aucun additif spécifique", "isCorrect": False},
                        {"text": "Un extincteur à mousse physique pour refroidir le composant", "isCorrect": False},
                        {"text": "Un extincteur à poudre chimique de classe A exclusivement", "isCorrect": False}
                    ],
                    "correction": "Le dioxyde de carbone (CO2) ne conduit pas l'électricité et ne laisse aucun résidu sur les équipements électroniques sensibles."
                },
                {
                    "questionNumber": 7,
                    "question": "Comment soulever correctement une lourde charge posée au sol ?",
                    "answerOptions": [
                        {"text": "Plier les genoux en gardant la colonne vertébrale bien droite", "isCorrect": True},
                        {"text": "Garder les jambes tendues et courber le dos vers l'avant", "isCorrect": False},
                        {"text": "Tirer brutalement la charge vers soi pour utiliser son poids", "isCorrect": False},
                        {"text": "Soulever la charge en effectuant une forte torsion du buste", "isCorrect": False}
                    ],
                    "correction": "C'est la technique de base enseignée lors de la formation PRAP pour utiliser la force des cuisses et préserver les disques lombaires."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la fonction d'un disjoncteur magnéto-thermique ?",
                    "answerOptions": [
                        {"text": "Protéger les câbles contre les surcharges et les courts-circuits", "isCorrect": True},
                        {"text": "Protéger les personnes contre les contacts directs avec le courant", "isCorrect": False},
                        {"text": "Limiter la surtension provoquée par un coup de foudre proche", "isCorrect": False},
                        {"text": "Réguler la tension d'alimentation des appareils très sensibles", "isCorrect": False}
                    ],
                    "correction": "La partie thermique gère les surcharges lentes, tandis que la partie magnétique coupe instantanément en cas de court-circuit brutal."
                },
                {
                    "questionNumber": 9,
                    "question": "Que faire face à un fil électrique dénudé sous tension ?",
                    "answerOptions": [
                        {"text": "Sécuriser la zone immédiatement et alerter un agent habilité", "isCorrect": True},
                        {"text": "Enrouler du ruban adhésif isolant autour avec des gants en cuir", "isCorrect": False},
                        {"text": "Couper le fil avec une pince coupante pour éviter un accident", "isCorrect": False},
                        {"text": "Ignorer le problème si l'appareil connecté fonctionne encore", "isCorrect": False}
                    ],
                    "correction": "Face à un danger électrique imminent, il ne faut jamais intervenir sans habilitation, mais baliser et prévenir le responsable."
                },
                {
                    "questionNumber": 10,
                    "question": "À quoi correspond la norme NF C 15-100 en France ?",
                    "answerOptions": [
                        {"text": "Elle réglemente la conception des installations électriques à basse tension", "isCorrect": True},
                        {"text": "Elle définit les règles de construction des charpentes métalliques", "isCorrect": False},
                        {"text": "Elle fixe les exigences pour la pose des conduites de gaz naturel", "isCorrect": False},
                        {"text": "Elle encadre les performances thermiques des bâtiments neufs", "isCorrect": False}
                    ],
                    "correction": "Cette norme garantit la sécurité des personnes et des biens pour toutes les installations électriques basse tension."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle règle s'applique à l'utilisation d'un échafaudage roulant ?",
                    "answerOptions": [
                        {"text": "Les roues doivent être verrouillées avant de monter sur le plateau", "isCorrect": True},
                        {"text": "Le technicien peut rester dessus lors du déplacement de la structure", "isCorrect": False},
                        {"text": "Il est autorisé de rajouter une échelle dessus pour gagner en hauteur", "isCorrect": False},
                        {"text": "Les stabilisateurs latéraux sont facultatifs pour les petits travaux", "isCorrect": False}
                    ],
                    "correction": "L'immobilisation totale de la structure est indispensable. Il est strictement interdit de déplacer un échafaudage roulant avec une personne dessus."
                },
                {
                    "questionNumber": 12,
                    "question": "En cas d'accident du travail grave, quelle est la première action ?",
                    "answerOptions": [
                        {"text": "Protéger la zone pour éviter tout suraccident avant d'alerter", "isCorrect": True},
                        {"text": "Déplacer immédiatement la victime vers une pièce plus calme", "isCorrect": False},
                        {"text": "Rédiger le rapport d'incident pour l'assurance de l'entreprise", "isCorrect": False},
                        {"text": "Appeler le responsable du site pour obtenir une autorisation", "isCorrect": False}
                    ],
                    "correction": "La règle de base du secourisme est de Protéger, puis Alerter, et enfin Secourir."
                },
                {
                    "questionNumber": 13,
                    "question": "Comment gérer des résidus de peintures ou de solvants ?",
                    "answerOptions": [
                        {"text": "Les stocker dans des contenants étanches pour la filière spécialisée", "isCorrect": True},
                        {"text": "Les diluer avec beaucoup d'eau chaude directement dans les égouts", "isCorrect": False},
                        {"text": "Les jeter avec les gravats classiques dans la benne de chantier", "isCorrect": False},
                        {"text": "Les laisser s'évaporer à l'air libre pour réduire leur volume net", "isCorrect": False}
                    ],
                    "correction": "Ce sont des déchets industriels dangereux qui polluent gravement l'environnement s'ils ne sont pas traités par des centres agréés."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le risque majeur lié à l'inhalation de poussières d'amiante ?",
                    "answerOptions": [
                        {"text": "Le développement de maladies respiratoires graves et irréversibles", "isCorrect": True},
                        {"text": "Une irritation cutanée temporaire au niveau des bras et du visage", "isCorrect": False},
                        {"text": "Une perte progressive de la vue suite à des lésions de la cornée", "isCorrect": False},
                        {"text": "Le déclenchement de fortes fièvres et de douleurs musculaires", "isCorrect": False}
                    ],
                    "correction": "Les fibres d'amiante se logent dans les poumons et peuvent provoquer des cancers des dizaines d'années après l'exposition."
                },
                {
                    "questionNumber": 15,
                    "question": "À quoi sert le piquet de terre d'un bâtiment ?",
                    "answerOptions": [
                        {"text": "Évacuer les courants de défaut vers le sol pour éviter l'électrisation", "isCorrect": True},
                        {"text": "Capter l'énergie statique de l'air pour réduire la consommation", "isCorrect": False},
                        {"text": "Stabiliser la tension électrique fournie par le réseau public", "isCorrect": False},
                        {"text": "Isoler le tableau de répartition contre les variations climatiques", "isCorrect": False}
                    ],
                    "correction": "Il assure le contact physique avec la masse de la terre pour écouler les fuites de courant de manière sécurisée."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle vérification est requise avant d'utiliser une échelle ?",
                    "answerOptions": [
                        {"text": "S'assurer de la présence et du bon état des patins antidérapants", "isCorrect": True},
                        {"text": "Vérifier que l'échelle est recouverte de peinture antirouille", "isCorrect": False},
                        {"text": "Contrôler que la charge maximale dépasse les trois cents kilos", "isCorrect": False},
                        {"text": "S'assurer que les barreaux sont parfaitement lisses et propres", "isCorrect": False}
                    ],
                    "correction": "Les patins garantissent la stabilité de l'échelle et préviennent les glissades mortelles."
                },
                {
                    "questionNumber": 17,
                    "question": "Quand le port du masque respiratoire FFP3 est-il indispensable ?",
                    "answerOptions": [
                        {"text": "Lors de travaux générant de fines poussières toxiques ou minérales", "isCorrect": True},
                        {"text": "Lors du nettoyage d'une pièce avec un balai à poils souples", "isCorrect": False},
                        {"text": "Lors du changement d'une ampoule dans un espace confiné", "isCorrect": False},
                        {"text": "Lors de la manipulation d'outils à main comme un tournevis", "isCorrect": False}
                    ],
                    "correction": "Le masque FFP3 offre le plus haut niveau de filtration contre les particules fines très dangereuses pour les voies respiratoires."
                },
                {
                    "questionNumber": 18,
                    "question": "Comment stocker des produits chimiques inflammables en sécurité ?",
                    "answerOptions": [
                        {"text": "Dans une armoire métallique ventilée à l'écart des sources de chaleur", "isCorrect": True},
                        {"text": "Sur des étagères en bois près de la porte pour une évacuation rapide", "isCorrect": False},
                        {"text": "Dans le véhicule d'intervention pour les avoir toujours à disposition", "isCorrect": False},
                        {"text": "Directement sur le sol de l'atelier pour éviter les risques de chute", "isCorrect": False}
                    ],
                    "correction": "Les armoires de sécurité préviennent l'accumulation de vapeurs nocives et retardent la propagation en cas d'incendie."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'objectif principal du balisage d'une zone d'intervention ?",
                    "answerOptions": [
                        {"text": "Empêcher l'accès aux personnes non autorisées et signaler un danger", "isCorrect": True},
                        {"text": "Indiquer aux autres techniciens l'endroit où ranger le matériel", "isCorrect": False},
                        {"text": "Délimiter l'espace pour calculer la surface exacte de la pièce", "isCorrect": False},
                        {"text": "Réserver une zone de repos pour les ouvriers pendant la pause", "isCorrect": False}
                    ],
                    "correction": "Le balisage crée un périmètre de sécurité physique et visuel indispensable pour protéger le public et les intervenants."
                },
                {
                    "questionNumber": 20,
                    "question": "En maintenance, quelle est la définition d'une intervention préventive ?",
                    "answerOptions": [
                        {"text": "Une opération réalisée pour réduire la probabilité de défaillance", "isCorrect": True},
                        {"text": "Une réparation effectuée en urgence après une panne matérielle complète", "isCorrect": False},
                        {"text": "Le remplacement systématique de tous les appareils électriques du site", "isCorrect": False},
                        {"text": "La modification architecturale d'un bâtiment pour l'agrandir", "isCorrect": False}
                    ],
                    "correction": "Contrairement à la maintenance curative qui répare une panne existante, la maintenance préventive anticipe l'usure des équipements."
                }
            ]
        },
        2: {
            "name": "THÈME 2 : PLOMBERIE ET SANITAIRE",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le rôle principal d'un siphon sous un lavabo ou un évier ?",
                    "answerOptions": [
                        {"text": "Conserver une garde d'eau pour bloquer la remontée des mauvaises odeurs", "isCorrect": True},
                        {"text": "Accélérer l'écoulement des eaux usées vers le réseau domestique", "isCorrect": False},
                        {"text": "Filtrer les impuretés solides avant leur arrivée dans le robinet", "isCorrect": False},
                        {"text": "Réguler la pression interne de la tuyauterie pour éviter les fuites", "isCorrect": False}
                    ],
                    "correction": "La garde d'eau stagnante dans le siphon crée un bouchon hermétique indispensable contre les gaz provenant des égouts."
                },
                {
                    "questionNumber": 22,
                    "question": "Que faut-il appliquer sur le filetage d'un raccord en laiton pour assurer son étanchéité ?",
                    "answerOptions": [
                        {"text": "Du ruban en téflon ou de la filasse enduite de pâte à joint", "isCorrect": True},
                        {"text": "Une colle spécifique pour les canalisations à haute pression", "isCorrect": False},
                        {"text": "Un mastic de fixation acrylique résistant à l'humidité", "isCorrect": False},
                        {"text": "Un lubrifiant synthétique conçu pour les joints toriques", "isCorrect": False}
                    ],
                    "correction": "Le téflon ou la filasse viennent combler les minuscules espaces du filetage pour empêcher l'eau de suinter."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel matériau est le plus couramment utilisé aujourd'hui pour les conduites d'évacuation des eaux usées ?",
                    "answerOptions": [
                        {"text": "Le polychlorure de vinyle couramment appelé plastique PVC", "isCorrect": True},
                        {"text": "L'alliage classique composé de plomb et de zinc fondu", "isCorrect": False},
                        {"text": "L'acier galvanisé à chaud traité contre la corrosion", "isCorrect": False},
                        {"text": "Le cuivre recuit assemblé par des soudures fortes", "isCorrect": False}
                    ],
                    "correction": "Le PVC a remplacé les anciens matériaux métalliques grâce à sa légèreté, son coût réduit et sa facilité d'assemblage par collage."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel outil est le plus adapté pour serrer un écrou de plomberie chromé sans en abîmer le revêtement ?",
                    "answerOptions": [
                        {"text": "Une clé à molette ou une clé plate aux dimensions adaptées", "isCorrect": True},
                        {"text": "Une pince multiprise équipée de mors métalliques striés", "isCorrect": False},
                        {"text": "Une tenaille de menuisier de très grande taille", "isCorrect": False},
                        {"text": "Une pince étau avec un système de verrouillage manuel", "isCorrect": False}
                    ],
                    "correction": "Les mâchoires lisses de la clé à molette et de la clé plate évitent de rayer ou d'écraser la finition esthétique du raccord."
                },
                {
                    "questionNumber": 25,
                    "question": "À quoi sert un réducteur de pression sur une installation sanitaire ?",
                    "answerOptions": [
                        {"text": "Abaisser la pression du réseau public pour protéger les équipements internes", "isCorrect": True},
                        {"text": "Augmenter le débit d'eau chaude vers les étages supérieurs du bâtiment", "isCorrect": False},
                        {"text": "Empêcher le retour de l'eau usée vers le réseau d'eau potable de la ville", "isCorrect": False},
                        {"text": "Mesurer avec précision la quantité d'eau consommée par l'ensemble du foyer", "isCorrect": False}
                    ],
                    "correction": "Le réducteur de pression évite les coups de bélier et préserve les appareils ménagers ainsi que les chauffe-eaux d'une usure prématurée."
                },
                {
                    "questionNumber": 26,
                    "question": "Où doit être obligatoirement installé un groupe de sécurité ?",
                    "answerOptions": [
                        {"text": "Sur l'arrivée d'eau froide du chauffe-eau à accumulation", "isCorrect": True},
                        {"text": "Sur la sortie d'eau chaude de la chaudière murale à gaz", "isCorrect": False},
                        {"text": "Directement après le compteur d'eau général du logement", "isCorrect": False},
                        {"text": "Sous le siphon de l'évier de la cuisine principale", "isCorrect": False}
                    ],
                    "correction": "Le groupe de sécurité se place toujours sur l'alimentation en eau froide du cumulus électrique."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la fonction principale de la soupape du groupe de sécurité du chauffe-eau ?",
                    "answerOptions": [
                        {"text": "Évacuer le surplus de pression lié à la dilatation thermique de l'eau", "isCorrect": True},
                        {"text": "Maintenir une température constante à l'intérieur de la cuve isolée", "isCorrect": False},
                        {"text": "Filtrer le calcaire et les boues présents dans le réseau public", "isCorrect": False},
                        {"text": "Accélérer le remplissage de la cuve après un soutirage important", "isCorrect": False}
                    ],
                    "correction": "Lorsque l'eau chauffe, elle se dilate. La soupape s'ouvre légèrement au goutte-à-goutte pour éviter l'éclatement de la cuve."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle technique utilise-t-on traditionnellement pour assembler de manière étanche des tubes en cuivre ?",
                    "answerOptions": [
                        {"text": "Le brasage fort ou le brasage tendre selon le type de raccordement", "isCorrect": True},
                        {"text": "La soudure à l'arc avec des électrodes enrobées en acier", "isCorrect": False},
                        {"text": "Le collage à froid avec une résine époxy bicomposant", "isCorrect": False},
                        {"text": "La soudure par point avec un poste électrique spécifique", "isCorrect": False}
                    ],
                    "correction": "Le brasage utilise un métal d'apport fondu par la chaleur d'un chalumeau ou d'une lampe à souder pour sceller les tubes."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel outil est spécifiquement conçu pour couper un tube en cuivre de manière nette et sans bavure ?",
                    "answerOptions": [
                        {"text": "Un coupe-tube rotatif équipé d'une molette de découpe circulaire", "isCorrect": True},
                        {"text": "Une scie égoïne dotée d'une lame à très fine denture", "isCorrect": False},
                        {"text": "Une pince coupante diagonale renforcée pour les métaux", "isCorrect": False},
                        {"text": "Une disqueuse électrique montée avec un disque à matériaux", "isCorrect": False}
                    ],
                    "correction": "Le coupe-tube permet une découpe parfaitement perpendiculaire et évite d'écraser le conduit, facilitant ainsi l'assemblage."
                },
                {
                    "questionNumber": 30,
                    "question": "Que signifie le sigle PER pour les tubes de plomberie synthétiques ?",
                    "answerOptions": [
                        {"text": "Polyéthylène réticulé haute densité", "isCorrect": True},
                        {"text": "Polymère élastique à résistance thermique", "isCorrect": False},
                        {"text": "Plastique enduit renforcé de fibres", "isCorrect": False},
                        {"text": "Polychlorure extrudé rigide industriel", "isCorrect": False}
                    ],
                    "correction": "Le tube PER, de couleur rouge ou bleue, est très souple et s'utilise de plus en plus pour les réseaux d'eau encastrés."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le grand avantage du tube multicouche par rapport au tube PER classique ?",
                    "answerOptions": [
                        {"text": "Il conserve la forme qui lui a été donnée après un cintrage manuel", "isCorrect": True},
                        {"text": "Il résiste à des températures internes supérieures à mille degrés", "isCorrect": False},
                        {"text": "Il peut être assemblé par un simple collage chimique avec du solvant", "isCorrect": False},
                        {"text": "Il est totalement transparent pour contrôler la qualité de l'eau", "isCorrect": False}
                    ],
                    "correction": "Grâce à son âme en aluminium, le multicouche garde la mémoire de forme, ce qui rend les poses apparentes beaucoup plus esthétiques."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le diamètre standard le plus courant pour un tube d'évacuation de lavabo en PVC ?",
                    "answerOptions": [
                        {"text": "Trente-deux millimètres de diamètre extérieur", "isCorrect": True},
                        {"text": "Quarante millimètres de diamètre extérieur", "isCorrect": False},
                        {"text": "Cinquante millimètres de diamètre extérieur", "isCorrect": False},
                        {"text": "Cent millimètres de diamètre extérieur", "isCorrect": False}
                    ],
                    "correction": "Le diamètre de 32 mm est le standard pour les petits équipements sanitaires comme les lavabos ou les bidets."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le diamètre standard minimum requis pour un tube d'évacuation de toilettes ?",
                    "answerOptions": [
                        {"text": "Cent millimètres de diamètre extérieur", "isCorrect": True},
                        {"text": "Cinquante millimètres de diamètre extérieur", "isCorrect": False},
                        {"text": "Quatre-vingts millimètres de diamètre extérieur", "isCorrect": False},
                        {"text": "Cent-vingt millimètres de diamètre extérieur", "isCorrect": False}
                    ],
                    "correction": "L'évacuation des eaux vannes (les toilettes) requiert un tube d'au moins 100 mm pour éviter tout risque d'obstruction."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la méthode sécurisée pour détecter une fuite sur un raccordement de gaz ?",
                    "answerOptions": [
                        {"text": "Utiliser un aérosol moussant spécifique détecteur de fuites", "isCorrect": True},
                        {"text": "Approcher la flamme d'un briquet près du raccord suspect", "isCorrect": False},
                        {"text": "Écouter très attentivement le sifflement de la conduite", "isCorrect": False},
                        {"text": "Mesurer la variation de la température ambiante de la pièce", "isCorrect": False}
                    ],
                    "correction": "Le produit moussant (ou de l'eau savonneuse) crée des bulles visibles si un gaz s'échappe. Il ne faut jamais utiliser de flamme."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment fonctionne un robinet thermostatique de radiateur mécanique ?",
                    "answerOptions": [
                        {"text": "Une sonde intégrée se dilate selon la température ambiante pour moduler le débit", "isCorrect": True},
                        {"text": "Une petite résistance électrique chauffe le mécanisme grâce à une pile", "isCorrect": False},
                        {"text": "Un programmateur horaire interne s'ouvre selon les heures creuses", "isCorrect": False},
                        {"text": "Une vanne d'arrêt quart de tour coupe brutalement l'arrivée d'eau", "isCorrect": False}
                    ],
                    "correction": "Le bulbe thermostatique, rempli de cire ou de liquide, s'étend ou se rétracte pour pousser le pointeau et ajuster le passage de l'eau chaude."
                },
                {
                    "questionNumber": 36,
                    "question": "Comment détartrer efficacement et sans dommage le mousseur d'un robinet de salle de bain ?",
                    "answerOptions": [
                        {"text": "Le dévisser et le plonger dans un bain de vinaigre blanc pur", "isCorrect": True},
                        {"text": "Le frotter vigoureusement avec une brosse métallique en acier", "isCorrect": False},
                        {"text": "L'enduire abondamment de graisse de silicone hydrofuge", "isCorrect": False},
                        {"text": "Le passer directement sous la flamme d'un chalumeau de chantier", "isCorrect": False}
                    ],
                    "correction": "Le vinaigre blanc est un acide doux naturel qui dissout le calcaire sans abîmer les grilles en plastique ou le chrome."
                },
                {
                    "questionNumber": 37,
                    "question": "Que faut-il remplacer lorsqu'un robinet mélangeur classique goutte en continu ?",
                    "answerOptions": [
                        {"text": "Le clapet en caoutchouc situé au bout de la tête de robinet", "isCorrect": True},
                        {"text": "La cartouche en céramique à l'intérieur du corps principal", "isCorrect": False},
                        {"text": "L'écrou de fixation situé sous la vasque ou le lavabo", "isCorrect": False},
                        {"text": "Le flexible d'alimentation d'eau froide relié au mur", "isCorrect": False}
                    ],
                    "correction": "Dans un mélangeur (deux têtes distinctes), l'usure du clapet d'étanchéité en caoutchouc est la cause la plus fréquente des fuites."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle pente d'évacuation minimale est recommandée pour l'écoulement naturel des eaux usées ?",
                    "answerOptions": [
                        {"text": "Un à deux centimètres de dénivelé par mètre de canalisation", "isCorrect": True},
                        {"text": "Cinq à dix centimètres de dénivelé par mètre de canalisation", "isCorrect": False},
                        {"text": "Un demi-centimètre de dénivelé par mètre de canalisation", "isCorrect": False},
                        {"text": "Quinze centimètres de dénivelé par mètre de canalisation", "isCorrect": False}
                    ],
                    "correction": "Une pente de 1 à 2 % est idéale. Une pente trop forte ferait s'écouler l'eau trop vite en laissant les matières solides sédimenter."
                },
                {
                    "questionNumber": 39,
                    "question": "Qu'est-ce qu'un clapet antiretour dans une installation sanitaire ?",
                    "answerOptions": [
                        {"text": "Un dispositif de sécurité empêchant le fluide de circuler dans le sens inverse", "isCorrect": True},
                        {"text": "Une vanne de purge permettant de vider l'air d'un circuit de chauffage", "isCorrect": False},
                        {"text": "Un raccord spécifique facilitant le démontage rapide d'une pompe encrassée", "isCorrect": False},
                        {"text": "Un limiteur de pression servant à réduire la consommation d'eau potable", "isCorrect": False}
                    ],
                    "correction": "Le clapet antiretour protège le réseau de distribution publique contre la pollution par un retour d'eaux usées ou contaminées."
                },
                {
                    "questionNumber": 40,
                    "question": "À quoi sert un regard de visite sur un réseau d'assainissement extérieur ?",
                    "answerOptions": [
                        {"text": "Permettre le contrôle visuel et faciliter le débouchage des canalisations enterrées", "isCorrect": True},
                        {"text": "Recueillir l'intégralité des eaux de pluie provenant de la toiture principale", "isCorrect": False},
                        {"text": "Filtrer les gros déchets solides avant qu'ils n'arrivent dans le réseau public", "isCorrect": False},
                        {"text": "Ventiler le conduit de la fosse septique pour évacuer les gaz dangereux", "isCorrect": False}
                    ],
                    "correction": "Le regard offre un accès direct aux jonctions et aux changements de direction, zones les plus propices aux bouchons."
                }
            ]
        },
        3: {
            "name": "THÈME 3 : AMÉNAGEMENT, MENUISERIE ET FINITIONS",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Comment s'appelle la cheville spécifique utilisée pour fixer des charges lourdes dans des plaques de plâtre ?",
                    "answerOptions": [
                        {"text": "La cheville métallique à expansion", "isCorrect": True},
                        {"text": "La cheville en plastique à frapper", "isCorrect": False},
                        {"text": "La cheville chimique pour scellement", "isCorrect": False},
                        {"text": "Le goujon d'ancrage pour charge lourde", "isCorrect": False}
                    ],
                    "correction": "Ce type de cheville, souvent appelée cheville Molly, s'ouvre en parapluie derrière la paroi creuse pour répartir la charge de manière optimale."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel outil manuel utilise-t-on pour vérifier à la fois l'horizontalité et la verticalité d'un support ?",
                    "answerOptions": [
                        {"text": "Le niveau à bulle tubulaire", "isCorrect": True},
                        {"text": "Le pied à coulisse analogique", "isCorrect": False},
                        {"text": "L'équerre de menuisier métallique", "isCorrect": False},
                        {"text": "Le mètre ruban à enrouleur automatique", "isCorrect": False}
                    ],
                    "correction": "Le niveau à bulle dispose de fioles de liquide réglées pour indiquer très précisément l'aplomb (verticalité) et le niveau (horizontalité)."
                },
                {
                    "questionNumber": 43,
                    "question": "Dans le domaine de la menuiserie intérieure, qu'est-ce qu'une paumelle ?",
                    "answerOptions": [
                        {"text": "Une ferrure permettant l'articulation d'une porte", "isCorrect": True},
                        {"text": "Une poignée de sécurité avec serrure intégrée", "isCorrect": False},
                        {"text": "Une planche de finition placée sur les plinthes", "isCorrect": False},
                        {"text": "Un joint d'étanchéité utilisé pour les vitrages", "isCorrect": False}
                    ],
                    "correction": "La paumelle est la pièce métallique composée de deux parties, fixée sur le bâti et l'ouvrant, pour permettre la rotation de la porte."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel produit est le plus indiqué pour combler un trou profond dans un mur avant sa mise en peinture ?",
                    "answerOptions": [
                        {"text": "Un enduit de rebouchage adapté", "isCorrect": True},
                        {"text": "Un enduit de lissage de finition", "isCorrect": False},
                        {"text": "Une peinture acrylique monocouche", "isCorrect": False},
                        {"text": "Une mousse polyuréthane expansive", "isCorrect": False}
                    ],
                    "correction": "L'enduit de rebouchage est formulé spécifiquement pour sécher en forte épaisseur sans se rétracter ni se fissurer, contrairement à l'enduit de lissage."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle est la méthode appropriée pour retirer une porte intérieure classique de son encadrement ?",
                    "answerOptions": [
                        {"text": "Dégonder l'ouvrant en le soulevant verticalement", "isCorrect": True},
                        {"text": "Dévisser intégralement le bâti fixé dans la maçonnerie", "isCorrect": False},
                        {"text": "Raboter la base de la porte pour la faire glisser doucement", "isCorrect": False},
                        {"text": "Découper les charnières à l'aide d'une meuleuse d'angle", "isCorrect": False}
                    ],
                    "correction": "Les portes intérieures sont généralement posées sur des paumelles simples. Il suffit de l'ouvrir et de la soulever pour la dégonder."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le rôle technique principal d'une plinthe lors de la pose d'un revêtement de sol ?",
                    "answerOptions": [
                        {"text": "Masquer le joint de dilatation obligatoire entre le sol et le mur", "isCorrect": True},
                        {"text": "Renforcer la structure portante de la cloison sèche attenante", "isCorrect": False},
                        {"text": "Isoler thermiquement le bas des murs en contact avec l'extérieur", "isCorrect": False},
                        {"text": "Faciliter le passage des conduits de ventilation mécanique contrôlée", "isCorrect": False}
                    ],
                    "correction": "Les sols flottants nécessitent un espace périphérique pour se dilater sans bomber. La plinthe vient recouvrir cet espace disgracieux."
                },
                {
                    "questionNumber": 47,
                    "question": "De quoi est principalement constituée une plaque de parement classique utilisée en aménagement ?",
                    "answerOptions": [
                        {"text": "Une couche de plâtre durci emprisonnée entre deux feuilles de carton", "isCorrect": True},
                        {"text": "Un panneau de bois aggloméré haute densité résistant à l'humidité", "isCorrect": False},
                        {"text": "Une feuille d'aluminium isolante recouverte d'un enduit pelliculaire", "isCorrect": False},
                        {"text": "Un carreau de plâtre massif conçu pour résister directement au feu", "isCorrect": False}
                    ],
                    "correction": "C'est la composition typique de la plaque BA13 (Bords Amincis de 13 mm d'épaisseur), très utilisée pour les cloisons et doublages."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel outil manuel est privilégié pour découper proprement des panneaux de bois de faible épaisseur ?",
                    "answerOptions": [
                        {"text": "Une scie égoïne dotée d'une denture très fine", "isCorrect": True},
                        {"text": "Une scie à métaux équipée d'une lame très souple", "isCorrect": False},
                        {"text": "Une scie à guichet conçue pour les découpes circulaires", "isCorrect": False},
                        {"text": "Une tronçonneuse thermique avec une chaîne affûtée", "isCorrect": False}
                    ],
                    "correction": "La denture fine limite l'arrachement des fibres du bois sur la face apparente, garantissant une coupe beaucoup plus nette."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel outil permet d'enfoncer totalement la tête d'un clou sans abîmer la surface en bois environnante ?",
                    "answerOptions": [
                        {"text": "Un chasse-clou métallique pointu", "isCorrect": True},
                        {"text": "Un tournevis plat de grande taille", "isCorrect": False},
                        {"text": "Un ciseau à bois parfaitement aiguisé", "isCorrect": False},
                        {"text": "Un poinçon de traçage pour menuisier", "isCorrect": False}
                    ],
                    "correction": "Le chasse-clou (ou chasse-pointe) s'applique sur la tête du clou pour le noyer dans le bois avant de reboucher au mastic."
                },
                {
                    "questionNumber": 50,
                    "question": "En menuiserie de bâtiment, à quoi correspond le terme chambranle ?",
                    "answerOptions": [
                        {"text": "L'encadrement de finition en bois qui borde une porte ou une fenêtre", "isCorrect": True},
                        {"text": "La partie vitrée amovible d'une fenêtre à double battant oscillant", "isCorrect": False},
                        {"text": "Le seuil métallique situé au niveau du sol pour assurer l'étanchéité", "isCorrect": False},
                        {"text": "Le système de verrouillage multipoint intégré dans une porte palière", "isCorrect": False}
                    ],
                    "correction": "Le chambranle masque le raccord souvent inesthétique entre la maçonnerie ou la cloison et le dormant de la menuiserie."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la solution de maintenance de premier niveau face à une charnière qui grince fortement ?",
                    "answerOptions": [
                        {"text": "Appliquer un dégrippant ou un lubrifiant adapté directement sur l'axe", "isCorrect": True},
                        {"text": "Remplacer immédiatement la porte par un modèle beaucoup plus léger", "isCorrect": False},
                        {"text": "Percer un trou supplémentaire pour ajouter une vis de maintien solide", "isCorrect": False},
                        {"text": "Poncer le bois autour de la charnière pour donner davantage de jeu", "isCorrect": False}
                    ],
                    "correction": "Un lubrifiant (graisse silicone ou huile mécanique) suffit généralement à réduire le frottement métal contre métal responsable du grincement."
                },
                {
                    "questionNumber": 52,
                    "question": "Que faut-il faire avant de visser dans un bois dur pour éviter que la pièce ne se fende ?",
                    "answerOptions": [
                        {"text": "Réaliser un avant-trou avec une mèche de diamètre inférieur à la vis", "isCorrect": True},
                        {"text": "Frapper fortement la tête de la vis avec un marteau avant de visser", "isCorrect": False},
                        {"text": "Tremper la pointe de la vis dans une colle polyuréthane expansive", "isCorrect": False},
                        {"text": "Utiliser une perceuse à percussion réglée sur sa vitesse maximale", "isCorrect": False}
                    ],
                    "correction": "Le perçage d'un avant-trou retire un peu de matière et guide la vis, réduisant ainsi la pression exercée sur les fibres du bois dur."
                },
                {
                    "questionNumber": 53,
                    "question": "À quoi sert principalement une boîte à onglets en menuiserie d'agencement ?",
                    "answerOptions": [
                        {"text": "Guider la lame de la scie pour réaliser des coupes avec un angle précis", "isCorrect": True},
                        {"text": "Ranger les pointes et les petites fixations de manière très ordonnée", "isCorrect": False},
                        {"text": "Transporter les outils tranchants en toute sécurité vers le chantier", "isCorrect": False},
                        {"text": "Protéger les prises électriques lors des travaux d'enduisage des murs", "isCorrect": False}
                    ],
                    "correction": "La boîte à onglets possède des fentes pré-découpées (souvent à quarante-cinq ou quatre-vingt-dix degrés) pour réaliser des raccords parfaits sur les plinthes ou les moulures."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle étape de préparation est indispensable avant l'application d'un vernis sur un bois brut ?",
                    "answerOptions": [
                        {"text": "Poncer soigneusement le support en respectant le sens des fibres du bois", "isCorrect": True},
                        {"text": "Nettoyer toute la surface avec un décapant chimique extrêmement puissant", "isCorrect": False},
                        {"text": "Appliquer une épaisse couche de cire d'abeille naturelle pour nourrir le bois", "isCorrect": False},
                        {"text": "Frotter vigoureusement le panneau avec une brosse métallique très rigide", "isCorrect": False}
                    ],
                    "correction": "Le ponçage dans le sens des fibres permet d'obtenir une surface lisse sans créer de rayures transversales disgracieuses."
                },
                {
                    "questionNumber": 55,
                    "question": "Dans l'encadrement d'une baie, comment désigne-t-on la partie biaise ou droite dans l'épaisseur du mur ?",
                    "answerOptions": [
                        {"text": "L'ébrasement de la baie", "isCorrect": True},
                        {"text": "L'usure de l'encadrement", "isCorrect": False},
                        {"text": "Le châssis de la structure", "isCorrect": False},
                        {"text": "Le parement de protection", "isCorrect": False}
                    ],
                    "correction": "L'ébrasement correspond à la découpe oblique ou perpendiculaire pratiquée dans l'épaisseur de la paroi pour recevoir la fenêtre ou la porte."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel type de colle est traditionnellement utilisé pour l'assemblage de pièces en bois en intérieur ?",
                    "answerOptions": [
                        {"text": "La colle vinylique blanche spécifique pour l'assemblage du bois", "isCorrect": True},
                        {"text": "La colle néoprène liquide pour un contact immédiat et définitif", "isCorrect": False},
                        {"text": "La colle cyanoacrylate conçue pour des réparations instantanées", "isCorrect": False},
                        {"text": "La colle mastic polyuréthane en cartouche pour scellement mural", "isCorrect": False}
                    ],
                    "correction": "La colle blanche (colle à bois vinylique) pénètre les fibres, devient transparente au séchage et offre une résistance mécanique très élevée."
                },
                {
                    "questionNumber": 57,
                    "question": "Que faut-il faire si une fenêtre en PVC frotte sur la partie basse de son encadrement ?",
                    "answerOptions": [
                        {"text": "Agir sur les vis de réglage spécifiques situées sur les fiches ou paumelles", "isCorrect": True},
                        {"text": "Raboter le cadre en plastique avec un outil électrique ou manuel adapté", "isCorrect": False},
                        {"text": "Ajouter des cales en bois sous le dormant pour remonter toute la structure", "isCorrect": False},
                        {"text": "Remplacer le double vitrage isolant par un modèle en acrylique plus léger", "isCorrect": False}
                    ],
                    "correction": "Contrairement au bois, on ne rabote jamais une menuiserie PVC ou aluminium. On utilise les réglages tridimensionnels prévus sur les paumelles."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel défaut d'application classique doit-on absolument éviter lors de la peinture d'un mur vertical ?",
                    "answerOptions": [
                        {"text": "Les coulures provoquées par un rouleau trop chargé ou une peinture trop diluée", "isCorrect": True},
                        {"text": "La rouille apparaissant instantanément sur les anciennes fixations en laiton", "isCorrect": False},
                        {"text": "L'oxydation rapide de la sous-couche au contact direct avec l'oxygène de la pièce", "isCorrect": False},
                        {"text": "La vitrification immédiate du support sous l'effet de la température ambiante", "isCorrect": False}
                    ],
                    "correction": "Il faut croiser les passes et bien essorer le rouleau sur la grille pour déposer une épaisseur de peinture régulière et éviter les coulures."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel outil est nécessaire pour appliquer un joint en silicone autour d'un appareil sanitaire ?",
                    "answerOptions": [
                        {"text": "Un pistolet extrudeur manuel ou électrique adapté aux cartouches standards", "isCorrect": True},
                        {"text": "Une spatule de carreleur crantée en acier inoxydable pour l'étalement", "isCorrect": False},
                        {"text": "Un pinceau brosse à poils synthétiques très rigides pour un dépôt régulier", "isCorrect": False},
                        {"text": "Un couteau à enduire disposant d'une lame particulièrement large et souple", "isCorrect": False}
                    ],
                    "correction": "Le pistolet permet de pousser le piston de la cartouche avec régularité pour obtenir un cordon de mastic homogène le long de la fissure."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment corriger un parquet stratifié qui forme une bosse au milieu de la pièce en raison de l'humidité ?",
                    "answerOptions": [
                        {"text": "Retailler les lames en périphérie pour rétablir un jeu de dilatation suffisant", "isCorrect": True},
                        {"text": "Clouer fermement chaque lame soulevée au sol pour empêcher tout mouvement", "isCorrect": False},
                        {"text": "Verser de la colle liquide dans les rainures centrales pour figer l'ensemble", "isCorrect": False},
                        {"text": "Placer des poids très lourds sur le soulèvement pendant plusieurs semaines", "isCorrect": False}
                    ],
                    "correction": "Un sol stratifié gonfle avec l'hygrométrie. S'il n'a pas d'espace pour s'étendre sous les plinthes, il se soulève. Il faut donc recréer cet espace périphérique."
                }
            ]
        },
        4: {
            "name": "THÈME 4 : THERMIQUE, CHAUFFAGE ET VENTILATION",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est l'avantage principal d'un poêle à granulés par rapport à un foyer ouvert classique ?",
                    "answerOptions": [
                        {"text": "Il offre une régulation automatique de la température", "isCorrect": True},
                        {"text": "Il fonctionne sans aucune alimentation électrique", "isCorrect": False},
                        {"text": "Il ne nécessite aucun conduit d'évacuation spécifique", "isCorrect": False},
                        {"text": "Il produit une quantité supérieure de cendres", "isCorrect": False}
                    ],
                    "correction": "Le poêle à granulés gère électroniquement son alimentation en combustible, optimisant ainsi son rendement thermique pour le bâtiment."
                },
                {
                    "questionNumber": 62,
                    "question": "Que signifie le sigle VMC dans les installations d'un bâtiment ?",
                    "answerOptions": [
                        {"text": "La Ventilation Mécanique Contrôlée", "isCorrect": True},
                        {"text": "Le Volume Minimal de Chauffage", "isCorrect": False},
                        {"text": "La Vérification Manuelle des Circuits", "isCorrect": False},
                        {"text": "La Vanne Murale de Condensation", "isCorrect": False}
                    ],
                    "correction": "La VMC assure le renouvellement constant de l'air intérieur afin d'évacuer l'humidité ambiante et les divers polluants."
                },
                {
                    "questionNumber": 63,
                    "question": "Sur quel principe physique repose le fonctionnement d'une pompe à chaleur air eau ?",
                    "answerOptions": [
                        {"text": "Elle puise les calories dans l'air extérieur", "isCorrect": True},
                        {"text": "Elle chauffe l'eau via des résistances internes", "isCorrect": False},
                        {"text": "Elle brûle un gaz réfrigérant pour produire de la chaleur", "isCorrect": False},
                        {"text": "Elle transforme l'humidité de l'air en chaleur", "isCorrect": False}
                    ],
                    "correction": "La pompe à chaleur transfère l'énergie thermique présente dans l'air extérieur vers le circuit d'eau intérieur via un cycle thermodynamique."
                },
                {
                    "questionNumber": 64,
                    "question": "Pourquoi est-il parfois nécessaire de renforcer le solivage des combles avant d'isoler ?",
                    "answerOptions": [
                        {"text": "Pour supporter le poids supplémentaire de l'isolant", "isCorrect": True},
                        {"text": "Pour améliorer la réception du réseau sans fil", "isCorrect": False},
                        {"text": "Pour empêcher la peinture du plafond de s'écailler", "isCorrect": False},
                        {"text": "Pour dissimuler les conduites d'évacuation rigides", "isCorrect": False}
                    ],
                    "correction": "L'ajout d'une très forte épaisseur d'isolant représente une charge structurelle importante qu'il faut impérativement anticiper pour éviter tout fléchissement."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la fonction d'un vase d'expansion dans un circuit de chauffage central ?",
                    "answerOptions": [
                        {"text": "Absorber la variation de volume de l'eau due à la chaleur", "isCorrect": True},
                        {"text": "Purger l'air contenu dans les radiateurs de l'étage", "isCorrect": False},
                        {"text": "Augmenter la vitesse de circulation de l'eau dans les tuyaux", "isCorrect": False},
                        {"text": "Filtrer les impuretés et les boues du circuit de chauffage", "isCorrect": False}
                    ],
                    "correction": "Lorsqu'elle chauffe, l'eau se dilate. Le vase d'expansion permet de maintenir une pression constante en absorbant ce surplus de volume."
                },
                {
                    "questionNumber": 66,
                    "question": "Où se situe idéalement une entrée d'air neuf dans une pièce de vie ?",
                    "answerOptions": [
                        {"text": "Sur la partie haute des fenêtres ou des coffres de volet", "isCorrect": True},
                        {"text": "Directement derrière le radiateur pour réchauffer l'air entrant", "isCorrect": False},
                        {"text": "Au ras du sol pour profiter de la fraîcheur du vide sanitaire", "isCorrect": False},
                        {"text": "Au centre du plafond pour une diffusion homogène dans la pièce", "isCorrect": False}
                    ],
                    "correction": "Placer l'entrée d'air en hauteur permet à l'air frais de se réchauffer progressivement avant de descendre, évitant ainsi les courants d'air désagréables."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le rôle d'un purgeur automatique sur un radiateur ?",
                    "answerOptions": [
                        {"text": "Évacuer les bulles d'air accumulées dans le circuit", "isCorrect": True},
                        {"text": "Vidanger totalement le liquide de chauffage en hiver", "isCorrect": False},
                        {"text": "Réguler la température selon la météo extérieure", "isCorrect": False},
                        {"text": "Bloquer l'arrivée d'eau en cas de fuite importante", "isCorrect": False}
                    ],
                    "correction": "L'air emprisonné empêche la circulation correcte de l'eau chaude et réduit l'efficacité du radiateur. Le purgeur évacue ces bulles."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le risque principal en cas d'obstruction des bouches de VMC ?",
                    "answerOptions": [
                        {"text": "Une condensation excessive favorisant le développement de moisissures", "isCorrect": True},
                        {"text": "Une consommation excessive d'électricité par le groupe moteur", "isCorrect": False},
                        {"text": "Une baisse soudaine de la température des murs intérieurs", "isCorrect": False},
                        {"text": "Une impossibilité d'allumer le chauffage dans la pièce", "isCorrect": False}
                    ],
                    "correction": "Sans renouvellement de l'air, l'humidité générée par les activités humaines reste piégée, entraînant des dégradations sanitaires."
                },
                {
                    "questionNumber": 69,
                    "question": "À quoi sert un calorifugeage des tuyauteries de chauffage ?",
                    "answerOptions": [
                        {"text": "Réduire les déperditions thermiques dans les zones non chauffées", "isCorrect": True},
                        {"text": "Empêcher le gel des canalisations en extérieur uniquement", "isCorrect": False},
                        {"text": "Masquer les tuyaux pour une finition esthétique irréprochable", "isCorrect": False},
                        {"text": "Augmenter le débit de circulation de l'eau vers les radiateurs", "isCorrect": False}
                    ],
                    "correction": "Le calorifugeage (isolant autour du tube) permet de garder l'eau chaude à température jusqu'à sa destination finale."
                },
                {
                    "questionNumber": 70,
                    "question": "Dans quel cas utilise-t-on un chauffage par le sol à basse température ?",
                    "answerOptions": [
                        {"text": "Pour maximiser la surface d'émission thermique et le confort", "isCorrect": True},
                        {"text": "Pour réduire le temps de chauffe à seulement quelques minutes", "isCorrect": False},
                        {"text": "Pour chauffer les bâtiments à forte hauteur sous plafond", "isCorrect": False},
                        {"text": "Pour installer des radiateurs décoratifs aux murs", "isCorrect": False}
                    ],
                    "correction": "La grande surface au sol permet de chauffer efficacement avec une température d'eau moins élevée qu'avec des radiateurs classiques."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est l'utilité d'un désemboueur sur un circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Éliminer les dépôts de boues métalliques et calcaires", "isCorrect": True},
                        {"text": "Régler la pression atmosphérique dans les radiateurs", "isCorrect": False},
                        {"text": "Mesurer le pH de l'eau pour éviter la corrosion", "isCorrect": False},
                        {"text": "Ajouter du liquide antigel dans les tuyauteries", "isCorrect": False}
                    ],
                    "correction": "Les boues diminuent l'efficacité du transfert de chaleur. Le désemboueur filtre ces résidus pour restaurer la performance."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie le concept d'inertie thermique d'un bâtiment ?",
                    "answerOptions": [
                        {"text": "La capacité des parois à stocker et restituer la chaleur", "isCorrect": True},
                        {"text": "La résistance d'un matériau au passage du courant électrique", "isCorrect": False},
                        {"text": "Le temps nécessaire pour vider un chauffe-eau de trois cents litres", "isCorrect": False},
                        {"text": "La vitesse de circulation de l'air à travers les bouches de ventilation", "isCorrect": False}
                    ],
                    "correction": "Une forte inertie permet de lisser les variations de température intérieure, offrant une meilleure stabilité de confort."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le rôle d'un thermostat d'ambiance ?",
                    "answerOptions": [
                        {"text": "Commander la mise en marche du chauffage selon la température de consigne", "isCorrect": True},
                        {"text": "Modifier la puissance électrique globale du bâtiment", "isCorrect": False},
                        {"text": "Indiquer le niveau de remplissage de la cuve à fioul", "isCorrect": False},
                        {"text": "Contrôler l'ouverture des fenêtres en cas de surchauffe", "isCorrect": False}
                    ],
                    "correction": "Le thermostat compare la température de la pièce à la valeur demandée par l'usager et pilote la chaudière en conséquence."
                },
                {
                    "questionNumber": 74,
                    "question": "Pourquoi faut-il isoler le conduit de fumée d'un poêle à bois ?",
                    "answerOptions": [
                        {"text": "Pour éviter la condensation des fumées et faciliter le tirage", "isCorrect": True},
                        {"text": "Pour augmenter la température intérieure du poêle", "isCorrect": False},
                        {"text": "Pour masquer le conduit dans les pièces de vie", "isCorrect": False},
                        {"text": "Pour éviter la consommation de combustible supplémentaire", "isCorrect": False}
                    ],
                    "correction": "Un conduit isolé maintient les fumées chaudes, ce qui permet un meilleur tirage et évite le dépôt de bistre sur les parois."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle est la particularité d'une VMC double flux ?",
                    "answerOptions": [
                        {"text": "Elle récupère la chaleur de l'air sortant pour préchauffer l'air entrant", "isCorrect": True},
                        {"text": "Elle dispose de deux moteurs pour doubler le débit de ventilation", "isCorrect": False},
                        {"text": "Elle aspire l'air par le haut et par le bas simultanément", "isCorrect": False},
                        {"text": "Elle fonctionne à la fois avec du gaz et de l'électricité", "isCorrect": False}
                    ],
                    "correction": "L'échangeur thermique transfère les calories de l'air vicié vers l'air propre avant son expulsion, limitant fortement les pertes thermiques."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel gaz est le principal produit de combustion d'une chaudière gaz bien réglée ?",
                    "answerOptions": [
                        {"text": "Le dioxyde de carbone", "isCorrect": True},
                        {"text": "Le monoxyde de carbone pur", "isCorrect": False},
                        {"text": "Le diazote liquéfié", "isCorrect": False},
                        {"text": "Le dioxyde de soufre", "isCorrect": False}
                    ],
                    "correction": "Une combustion complète du gaz naturel dégage principalement du CO2 et de la vapeur d'eau."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le risque si une chaudière est mal entretenue ?",
                    "answerOptions": [
                        {"text": "La production de monoxyde de carbone toxique", "isCorrect": True},
                        {"text": "Une augmentation soudaine du prix du gaz", "isCorrect": False},
                        {"text": "La panne irréversible du compteur de gaz principal", "isCorrect": False},
                        {"text": "Le blocage de la ventilation du bâtiment", "isCorrect": False}
                    ],
                    "correction": "Une mauvaise combustion, due à un encrassement ou un défaut d'aération, libère du monoxyde de carbone, un gaz inodore et mortel."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est la fonction d'un circulateur dans un circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Assurer le mouvement de l'eau chaude vers les émetteurs", "isCorrect": True},
                        {"text": "Chauffer l'eau contenue dans le corps de chauffe", "isCorrect": False},
                        {"text": "Mesurer le débit d'eau circulant dans le réseau", "isCorrect": False},
                        {"text": "Sécuriser le circuit en cas de fuite d'eau", "isCorrect": False}
                    ],
                    "correction": "Le circulateur est une pompe qui force l'eau chaude à circuler dans les radiateurs ou le plancher chauffant."
                },
                {
                    "questionNumber": 79,
                    "question": "Pourquoi doit-on éviter d'installer un meuble devant un radiateur ?",
                    "answerOptions": [
                        {"text": "Car cela empêche la diffusion thermique naturelle par convection", "isCorrect": True},
                        {"text": "Car le poids du meuble risque d'arracher le radiateur du mur", "isCorrect": False},
                        {"text": "Car cela bloque le passage des câbles électriques muraux", "isCorrect": False},
                        {"text": "Car le radiateur risque de déclencher un incendie sur le bois", "isCorrect": False}
                    ],
                    "correction": "L'obstacle bloque la circulation de l'air et absorbe la chaleur émise, réduisant drastiquement l'efficacité du chauffage dans la pièce."
                },
                {
                    "questionNumber": 80,
                    "question": "Que signifie l'équilibrage d'une installation de chauffage ?",
                    "answerOptions": [
                        {"text": "Ajuster les débits pour que chaque radiateur chauffe correctement", "isCorrect": True},
                        {"text": "Vérifier que tous les radiateurs sont de la même taille", "isCorrect": False},
                        {"text": "Nettoyer l'intérieur des tuyauteries en cuivre", "isCorrect": False},
                        {"text": "Programmer les mêmes heures de chauffe pour chaque pièce", "isCorrect": False}
                    ],
                    "correction": "Sans équilibrage, les radiateurs les plus proches de la chaudière sont trop chauds et les plus éloignés sont froids."
                }
            ]
        },
        5: {
            "name": "THÈME 5 : SANTÉ, SÉCURITÉ ET ENVIRONNEMENT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Que signifie le sigle EPI sur un chantier de maintenance ?",
                    "answerOptions": [
                        {"text": "Équipement de Protection Individuelle", "isCorrect": True},
                        {"text": "Évaluation Préventive des Incidents", "isCorrect": False},
                        {"text": "Entretien Planifié des Installations", "isCorrect": False},
                        {"text": "Exigence Professionnelle Interne", "isCorrect": False}
                    ],
                    "correction": "Les EPI, tels que les casques, lunettes ou chaussures de sécurité, sont obligatoires pour protéger l'intégrité physique du technicien."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la procédure réglementaire pour gérer des solvants ou peintures usagés ?",
                    "answerOptions": [
                        {"text": "Les acheminer vers une déchetterie professionnelle", "isCorrect": True},
                        {"text": "Les diluer dans l'évier avec de l'eau bouillante", "isCorrect": False},
                        {"text": "Les jeter directement dans les ordures ménagères", "isCorrect": False},
                        {"text": "Les laisser s'évaporer à l'air libre en extérieur", "isCorrect": False}
                    ],
                    "correction": "Ces produits sont classés comme Déchets Dangereux et nécessitent un traitement spécifique en filière adaptée pour éviter toute pollution."
                },
                {
                    "questionNumber": 83,
                    "question": "Comment un technicien doit-il soulever manuellement une lourde charge posée au sol ?",
                    "answerOptions": [
                        {"text": "Plier les genoux et garder le dos parfaitement droit", "isCorrect": True},
                        {"text": "Garder les jambes tendues et courber la colonne", "isCorrect": False},
                        {"text": "Tirer brutalement la charge vers son buste", "isCorrect": False},
                        {"text": "Soulever la charge en effectuant une torsion", "isCorrect": False}
                    ],
                    "correction": "C'est l'un des principes fondamentaux de la prévention des risques physiques pour préserver les disques lombaires."
                },
                {
                    "questionNumber": 84,
                    "question": "Quels équipements sont absolument indispensables pour utiliser une meuleuse d'angle ?",
                    "answerOptions": [
                        {"text": "Des lunettes de protection et des protections auditives", "isCorrect": True},
                        {"text": "De simples gants en tissu pour limiter les coupures", "isCorrect": False},
                        {"text": "Des lunettes de soleil et des gants en latex fin", "isCorrect": False},
                        {"text": "Aucun équipement pour une intervention très courte", "isCorrect": False}
                    ],
                    "correction": "Une meuleuse génère des étincelles, des éclats dangereux et un bruit intense nécessitant des protections adaptées."
                },
                {
                    "questionNumber": 85,
                    "question": "Que faire en cas de présence d'une fuite de gaz dans un bâtiment ?",
                    "answerOptions": [
                        {"text": "Couper immédiatement l'alimentation et ventiler les locaux", "isCorrect": True},
                        {"text": "Chercher l'origine de la fuite avec une flamme nue", "isCorrect": False},
                        {"text": "Allumer toutes les lumières pour mieux localiser la source", "isCorrect": False},
                        {"text": "Appeler les secours en utilisant le téléphone fixe sur place", "isCorrect": False}
                    ],
                    "correction": "Il faut éliminer les sources d'étincelles, isoler le gaz et ventiler sans activer aucun appareil électrique."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le risque lié à l'inhalation de poussières d'amiante ?",
                    "answerOptions": [
                        {"text": "Le développement de maladies respiratoires graves", "isCorrect": True},
                        {"text": "Une irritation cutanée temporaire aux mains", "isCorrect": False},
                        {"text": "Une perte progressive de la vision nocturne", "isCorrect": False},
                        {"text": "Le déclenchement de fièvres et douleurs musculaires", "isCorrect": False}
                    ],
                    "correction": "Les fibres d'amiante se logent dans les poumons et peuvent provoquer des cancers très longtemps après l'exposition."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la règle d'or du secourisme en cas d'accident ?",
                    "answerOptions": [
                        {"text": "Protéger, alerter et ensuite secourir", "isCorrect": True},
                        {"text": "Déplacer la victime vers une pièce calme", "isCorrect": False},
                        {"text": "Rédiger le rapport d'incident avec l'assurance", "isCorrect": False},
                        {"text": "Appeler le responsable avant toute autre action", "isCorrect": False}
                    ],
                    "correction": "La sécurité du sauveteur et de la victime est la priorité avant toute assistance médicale."
                },
                {
                    "questionNumber": 88,
                    "question": "Pourquoi faut-il maintenir les passages dégagés dans un atelier ?",
                    "answerOptions": [
                        {"text": "Pour permettre une évacuation rapide en cas d'urgence", "isCorrect": True},
                        {"text": "Pour que les clients puissent circuler avec leurs bagages", "isCorrect": False},
                        {"text": "Pour gagner du temps lors du nettoyage quotidien", "isCorrect": False},
                        {"text": "Pour augmenter la luminosité naturelle de la pièce", "isCorrect": False}
                    ],
                    "correction": "L'encombrement des voies de circulation est une cause majeure d'accidents et empêche une évacuation efficace."
                },
                {
                    "questionNumber": 89,
                    "question": "Qu'est-ce qu'une fiche de données de sécurité (FDS) ?",
                    "answerOptions": [
                        {"text": "Un document informant sur les dangers d'un produit chimique", "isCorrect": True},
                        {"text": "Une fiche récapitulative des salaires des ouvriers", "isCorrect": False},
                        {"text": "Un compte-rendu d'accident survenu en atelier", "isCorrect": False},
                        {"text": "La liste des outils nécessaires pour une réparation", "isCorrect": False}
                    ],
                    "correction": "La FDS précise les risques, les précautions et les mesures d'urgence pour chaque produit chimique utilisé."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le danger d'une perceuse avec un foret inapproprié ?",
                    "answerOptions": [
                        {"text": "Le risque de rupture du foret et de projection d'éclats", "isCorrect": True},
                        {"text": "La décharge électrique immédiate du moteur", "isCorrect": False},
                        {"text": "L'augmentation soudaine de la température ambiante", "isCorrect": False},
                        {"text": "Le blocage de la ventilation du bâtiment", "isCorrect": False}
                    ],
                    "correction": "L'utilisation d'un foret non adapté au matériau peut provoquer des contraintes excessives et briser l'outil brutalement."
                },
                {
                    "questionNumber": 91,
                    "question": "Que signifie le balisage d'une zone de travail ?",
                    "answerOptions": [
                        {"text": "Empêcher l'accès aux personnes non autorisées", "isCorrect": True},
                        {"text": "Délimiter l'espace pour ranger le matériel proprement", "isCorrect": False},
                        {"text": "Calculer la surface totale de la zone d'intervention", "isCorrect": False},
                        {"text": "Réserver une place de parking pour le véhicule d'intervention", "isCorrect": False}
                    ],
                    "correction": "Le balisage crée une séparation visuelle et physique essentielle pour la sécurité de tous."
                },
                {
                    "questionNumber": 92,
                    "question": "Pourquoi porter des chaussures de sécurité renforcées ?",
                    "answerOptions": [
                        {"text": "Pour protéger les pieds contre les chutes d'objets lourds", "isCorrect": True},
                        {"text": "Pour mieux adhérer sur les sols en bois vernis", "isCorrect": False},
                        {"text": "Pour éviter d'avoir froid durant l'hiver en atelier", "isCorrect": False},
                        {"text": "Pour améliorer la posture lors de la marche rapide", "isCorrect": False}
                    ],
                    "correction": "Elles possèdent une coque résistante aux chocs et souvent une semelle anti-perforation."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le premier réflexe en cas d'incendie mineur ?",
                    "answerOptions": [
                        {"text": "Utiliser l'extincteur approprié si possible", "isCorrect": True},
                        {"text": "Essayer d'éteindre le feu avec des vêtements", "isCorrect": False},
                        {"text": "Attendre que les pompiers arrivent sur place", "isCorrect": False},
                        {"text": "Continuer le travail pour terminer la tâche en cours", "isCorrect": False}
                    ],
                    "correction": "Si le feu est naissant et que l'on possède l'équipement adéquat, une intervention immédiate est possible."
                },
                {
                    "questionNumber": 94,
                    "question": "Que signifie le respect des consignes de sécurité ?",
                    "answerOptions": [
                        {"text": "Appliquer les procédures pour prévenir les accidents", "isCorrect": True},
                        {"text": "Savoir ignorer les règles en cas d'urgence", "isCorrect": False},
                        {"text": "Demander l'autorisation à chaque étape de travail", "isCorrect": False},
                        {"text": "Travailler le plus rapidement possible sans erreur", "isCorrect": False}
                    ],
                    "correction": "La sécurité est une démarche active de prévention basée sur le respect de protocoles testés."
                },
                {
                    "questionNumber": 95,
                    "question": "Pourquoi utiliser des protections auditives ?",
                    "answerOptions": [
                        {"text": "Pour limiter les risques de perte auditive durable", "isCorrect": True},
                        {"text": "Pour mieux se concentrer sur son travail", "isCorrect": False},
                        {"text": "Pour éviter d'entendre les remarques des collègues", "isCorrect": False},
                        {"text": "Pour augmenter la précision des gestes techniques", "isCorrect": False}
                    ],
                    "correction": "L'exposition prolongée à des niveaux sonores élevés endommage irréversiblement les cellules de l'oreille interne."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la définition d'un risque majeur ?",
                    "answerOptions": [
                        {"text": "Un événement pouvant causer des dommages très graves", "isCorrect": True},
                        {"text": "Une panne de machine simple et rapide à réparer", "isCorrect": False},
                        {"text": "Une erreur de commande dans les stocks", "isCorrect": False},
                        {"text": "Un simple retard de livraison de matériel", "isCorrect": False}
                    ],
                    "correction": "Le risque majeur implique des conséquences humaines ou environnementales lourdes."
                },
                {
                    "questionNumber": 97,
                    "question": "Que faut-il vérifier avant d'utiliser une échelle à coulisse ?",
                    "answerOptions": [
                        {"text": "Le bon verrouillage des crochets de sécurité", "isCorrect": True},
                        {"text": "La propreté de la peinture sur les barreaux", "isCorrect": False},
                        {"text": "Le nombre de personnes présentes à proximité", "isCorrect": False},
                        {"text": "La température exacte dans la pièce d'utilisation", "isCorrect": False}
                    ],
                    "correction": "Les crochets de sécurité empêchent l'échelle de se replier accidentellement pendant l'ascension."
                },
                {
                    "questionNumber": 98,
                    "question": "Que signifie un panneau de signalisation triangulaire jaune ?",
                    "answerOptions": [
                        {"text": "Un danger potentiel nécessitant une vigilance", "isCorrect": True},
                        {"text": "Une obligation de porter un casque", "isCorrect": False},
                        {"text": "Une interdiction d'accès aux non-initiés", "isCorrect": False},
                        {"text": "La localisation d'une sortie de secours", "isCorrect": False}
                    ],
                    "correction": "La couleur jaune et la forme triangulaire sont normalisées pour avertir des risques."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment s'assurer qu'un appareil électrique est bien hors tension ?",
                    "answerOptions": [
                        {"text": "Utiliser un VAT (Vérificateur d'Absence de Tension)", "isCorrect": True},
                        {"text": "Vérifier que le voyant lumineux est éteint", "isCorrect": False},
                        {"text": "Toucher les fils avec le dos de la main par précaution", "isCorrect": False},
                        {"text": "Demander oralement à un collègue si c'est bon", "isCorrect": False}
                    ],
                    "correction": "Seul un appareil de mesure certifié (VAT) garantit l'absence de tension électrique avant toute manipulation."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la principale cause d'accident par chute de hauteur ?",
                    "answerOptions": [
                        {"text": "L'utilisation inadaptée ou non sécurisée du matériel", "isCorrect": True},
                        {"text": "La fatigue excessive en fin de journée de travail", "isCorrect": False},
                        {"text": "Le manque d'éclairage naturel dans les locaux", "isCorrect": False},
                        {"text": "Une météo défavorable à l'intérieur du bâtiment", "isCorrect": False}
                    ],
                    "correction": "Le non-respect des règles de sécurisation des accès en hauteur est la cause principale de ces accidents souvent graves."
                }
            ]
        }
    }
}