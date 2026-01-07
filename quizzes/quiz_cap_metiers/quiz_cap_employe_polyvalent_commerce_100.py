quiz_data = {
    "title": "Quiz CAP Employé Polyvalent du Commerce (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : RÉCEPTION ET SUIVI DES COMMANDES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : RÉCEPTION ET SUIVI DES COMMANDES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel document le réceptionnaire doit-il impérativement émarger pour attester de la réception des marchandises ?",
                    "answerOptions": [
                        {"text": "Bon de livraison", "isCorrect": True},
                        {"text": "Facture proforma détaillée", "isCorrect": False},
                        {"text": "Relevé de compte fournisseur", "isCorrect": False},
                        {"text": "Bon de commande interne", "isCorrect": False}
                    ],
                    "correction": "Le bon de livraison est le document officiel qui accompagne la marchandise. La signature (émargement) de ce document par le réceptionnaire transfère la responsabilité de la marchandise du transporteur vers le magasin."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la première étape du contrôle quantitatif lors d'une livraison ?",
                    "answerOptions": [
                        {"text": "Compter les colis", "isCorrect": True},
                        {"text": "Ouvrir tous les cartons", "isCorrect": False},
                        {"text": "Mettre en rayon", "isCorrect": False},
                        {"text": "Vérifier les prix", "isCorrect": False}
                    ],
                    "correction": "Le contrôle quantitatif commence toujours par le dénombrement des colis (palettes ou cartons) pour vérifier la concordance avec le bon de transport, avant même de contrôler le détail des articles."
                },
                {
                    "questionNumber": 3,
                    "question": "Que doit faire l'équipier s'il constate qu'un carton est écrasé ou ouvert à la réception ?",
                    "answerOptions": [
                        {"text": "Émettre des réserves écrites précises", "isCorrect": True},
                        {"text": "Refuser la totalité de la livraison sans motif", "isCorrect": False},
                        {"text": "Accepter la marchandise sans rien dire", "isCorrect": False},
                        {"text": "Appeler le fournisseur pour se plaindre verbalement", "isCorrect": False}
                    ],
                    "correction": "En cas d'anomalie visible (avarie), il est obligatoire d'inscrire des réserves caractérisées (ex: '1 carton ouvert, 3 produits manquants') sur le document de transport pour préserver les recours contre le transporteur."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel matériel de manutention est le plus adapté pour déplacer une palette au sol sur une courte distance ?",
                    "answerOptions": [
                        {"text": "Transpalette", "isCorrect": True},
                        {"text": "Chariot élévateur", "isCorrect": False},
                        {"text": "Diable", "isCorrect": False},
                        {"text": "Monte-charge", "isCorrect": False}
                    ],
                    "correction": "Le transpalette (manuel ou électrique) est l'outil spécifique conçu pour soulever et déplacer des palettes au niveau du sol. Le diable sert pour les cartons en vrac, et le chariot élévateur pour le gerbage en hauteur."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle méthode de gestion de stock impose de sortir les produits aux dates les plus courtes en premier ?",
                    "answerOptions": [
                        {"text": "FEFO", "isCorrect": True},
                        {"text": "LIFO", "isCorrect": False},
                        {"text": "CUMP", "isCorrect": False},
                        {"text": "FIFO", "isCorrect": False}
                    ],
                    "correction": "La méthode FEFO (First Expired, First Out) ou 'Premier périmé, premier sorti' est impérative pour les produits périssables afin d'éviter la casse et le gaspillage alimentaire."
                },
                {
                    "questionNumber": 6,
                    "question": "Lors d'un contrôle qualitatif sur des produits frais, que doit-on vérifier en priorité absolue ?",
                    "answerOptions": [
                        {"text": "Température à cœur", "isCorrect": True},
                        {"text": "Esthétique du carton", "isCorrect": False},
                        {"text": "Couleur du logo", "isCorrect": False},
                        {"text": "Poids de la palette", "isCorrect": False}
                    ],
                    "correction": "Le respect de la chaîne du froid est critique. La prise de température à cœur (ou entre deux produits) garantit que la marchandise n'a pas subi de réchauffement dangereux pour la santé du consommateur."
                },
                {
                    "questionNumber": 7,
                    "question": "Comment appelle-t-on la zone du magasin réservée au stockage des marchandises non exposées à la vente ?",
                    "answerOptions": [
                        {"text": "Réserve", "isCorrect": True},
                        {"text": "Surface de vente", "isCorrect": False},
                        {"text": "Zone chaude", "isCorrect": False},
                        {"text": "Linéaire", "isCorrect": False}
                    ],
                    "correction": "La réserve est le lieu de stockage des produits en attente de mise en rayon. C'est une zone non accessible aux clients, contrairement à la surface de vente."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la conséquence immédiate d'une livraison non contrôlée à la réception ?",
                    "answerOptions": [
                        {"text": "Stocks théoriques et réels faux", "isCorrect": True},
                        {"text": "Augmentation du chiffre d'affaires", "isCorrect": False},
                        {"text": "Amélioration de la marge commerciale", "isCorrect": False},
                        {"text": "Satisfaction accrue de la clientèle", "isCorrect": False}
                    ],
                    "correction": "Si l'on ne contrôle pas la livraison, on intègre dans le stock informatique des quantités potentiellement erronées (manquants non détectés), ce qui fausse l'inventaire et la gestion des réapprovisionnements."
                },
                {
                    "questionNumber": 9,
                    "question": "Que signifie le sigle DLC présent sur les produits périssables ?",
                    "answerOptions": [
                        {"text": "Date limite de consommation", "isCorrect": True},
                        {"text": "Date longue de conservation", "isCorrect": False},
                        {"text": "Délai légal de commercialisation", "isCorrect": False},
                        {"text": "Durée limite de chargement", "isCorrect": False}
                    ],
                    "correction": "La DLC (Date Limite de Consommation) est une date impérative de sécurité sanitaire. Au-delà de cette date, le produit est impropre à la consommation et doit être retiré."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle action permet de prévenir les risques liés aux gestes et postures lors du déchargement ?",
                    "answerOptions": [
                        {"text": "Plier les genoux pour soulever", "isCorrect": True},
                        {"text": "Courber le dos vers l'avant", "isCorrect": False},
                        {"text": "Porter les charges à bout de bras", "isCorrect": False},
                        {"text": "Faire des mouvements brusques", "isCorrect": False}
                    ],
                    "correction": "Pour protéger son dos (colonne vertébrale), il faut utiliser la force des jambes en pliant les genoux et garder la charge le plus près possible du corps."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel document permet de vérifier la conformité entre ce qui a été commandé et ce qui est livré ?",
                    "answerOptions": [
                        {"text": "Bon de commande", "isCorrect": True},
                        {"text": "Facture client", "isCorrect": False},
                        {"text": "Ticket de caisse", "isCorrect": False},
                        {"text": "Fiche technique", "isCorrect": False}
                    ],
                    "correction": "Le contrôle de conformité consiste à rapprocher le bon de livraison (ce qui est reçu) avec le bon de commande (ce qui a été demandé) pour détecter les erreurs de préparation du fournisseur."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la procédure correcte si un produit livré ne correspond pas à la commande mais est en bon état ?",
                    "answerOptions": [
                        {"text": "Isoler le produit et contacter le fournisseur", "isCorrect": True},
                        {"text": "Mettre le produit en rayon immédiatement", "isCorrect": False},
                        {"text": "Jeter le produit dans la benne à déchets", "isCorrect": False},
                        {"text": "Offrir le produit au personnel du magasin", "isCorrect": False}
                    ],
                    "correction": "C'est une erreur de référence. Le produit ne doit pas être vendu ni jeté. Il faut l'isoler en zone de litige et contacter le fournisseur pour organiser une reprise ou obtenir un avoir."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel équipement de protection individuelle est indispensable pour manipuler des palettes en bois ?",
                    "answerOptions": [
                        {"text": "Gants de manutention", "isCorrect": True},
                        {"text": "Lunettes de soleil", "isCorrect": False},
                        {"text": "Masque chirurgical", "isCorrect": False},
                        {"text": "Tablier de cuisine", "isCorrect": False}
                    ],
                    "correction": "Les gants de manutention protègent les mains contre les échardes, les coupures et les frottements liés à la manipulation des palettes et des cartons."
                },
                {
                    "questionNumber": 14,
                    "question": "Que doit-on faire des emballages plastiques et cartons après le dépotage de la marchandise ?",
                    "answerOptions": [
                        {"text": "Effectuer un tri sélectif rigoureux", "isCorrect": True},
                        {"text": "Tout jeter dans la même poubelle grise", "isCorrect": False},
                        {"text": "Brûler les cartons sur le parking arrière", "isCorrect": False},
                        {"text": "Laisser les déchets dans l'allée centrale", "isCorrect": False}
                    ],
                    "correction": "La gestion des déchets en commerce impose le tri sélectif (cartons, plastiques, bois) pour permettre leur recyclage et réduire l'impact environnemental."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle information est essentielle pour assurer la traçabilité d'un produit alimentaire ?",
                    "answerOptions": [
                        {"text": "Numéro de lot", "isCorrect": True},
                        {"text": "Prix de vente", "isCorrect": False},
                        {"text": "Couleur du paquet", "isCorrect": False},
                        {"text": "Nom du caissier", "isCorrect": False}
                    ],
                    "correction": "Le numéro de lot permet d'identifier l'historique de fabrication du produit. Il est indispensable pour procéder aux retraits ou rappels de produits en cas de problème sanitaire."
                },
                {
                    "questionNumber": 16,
                    "question": "Pourquoi est-il important de ne pas gerber les palettes trop haut dans la réserve ?",
                    "answerOptions": [
                        {"text": "Éviter les chutes d'objets", "isCorrect": True},
                        {"text": "Gagner du temps au rangement", "isCorrect": False},
                        {"text": "Cacher les produits aux clients", "isCorrect": False},
                        {"text": "Faire de l'exercice physique", "isCorrect": False}
                    ],
                    "correction": "La hauteur de gerbage doit être limitée pour garantir la stabilité de la pile et la sécurité du personnel, évitant ainsi le risque d'écrasement ou de chute de la marchandise."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle mention indique qu'un produit peut être consommé après la date indiquée sans risque pour la santé ?",
                    "answerOptions": [
                        {"text": "DDM", "isCorrect": True},
                        {"text": "DLC", "isCorrect": False},
                        {"text": "THT", "isCorrect": False},
                        {"text": "NF", "isCorrect": False}
                    ],
                    "correction": "La DDM (Date de Durabilité Minimale), anciennement DLUO, indique que le produit peut perdre ses qualités gustatives mais reste sain à consommer après la date, contrairement à la DLC."
                },
                {
                    "questionNumber": 18,
                    "question": "Dans le cadre de la réception, que signifie 'émarger' un document ?",
                    "answerOptions": [
                        {"text": "Signer et apposer le tampon", "isCorrect": True},
                        {"text": "Lire le document silencieusement", "isCorrect": False},
                        {"text": "Photocopier le document en deux", "isCorrect": False},
                        {"text": "Détruire le document après lecture", "isCorrect": False}
                    ],
                    "correction": "L'émargement consiste juridiquement à apposer sa signature (et souvent le tampon du magasin) pour valider officiellement la réception et accepter le transfert de responsabilité."
                },
                {
                    "questionNumber": 19,
                    "question": "Si un colis arrive ouvert, quelle mention spécifique doit apparaître sur le bon de transport ?",
                    "answerOptions": [
                        {"text": "Carton ouvert et nombre de manquants", "isCorrect": True},
                        {"text": "Sous réserve de déballage ultérieur", "isCorrect": False},
                        {"text": "Colis en mauvais état général", "isCorrect": False},
                        {"text": "Marchandise abîmée par le chauffeur", "isCorrect": False}
                    ],
                    "correction": "Les réserves doivent être précises, datées et significatives. La mention 'sous réserve de déballage' n'a aucune valeur juridique. Il faut constater la réalité des faits (ex: carton ouvert) et les conséquences (ex: 2 pièces manquantes)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel outil permet de lire les codes-barres pour vérifier les réceptions informatiquement ?",
                    "answerOptions": [
                        {"text": "Douchette", "isCorrect": True},
                        {"text": "Calculatrice", "isCorrect": False},
                        {"text": "Clavier", "isCorrect": False},
                        {"text": "Souris", "isCorrect": False}
                    ],
                    "correction": "La douchette (ou scanner) permet de lire les codes-barres (EAN) et de les comparer instantanément avec les données du bon de livraison informatisé ou de la commande."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : MISE EN VALEUR ET APPROVISIONNEMENT DE L'ESPACE COMMERCIAL (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : MISE EN VALEUR ET APPROVISIONNEMENT DE L'ESPACE COMMERCIAL",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle technique consiste à ramener les produits du fond de l'étagère vers le bord avant pour donner une impression de rayon plein ?",
                    "answerOptions": [
                        {"text": "Le facing", "isCorrect": True},
                        {"text": "Le balisage promotionnel", "isCorrect": False},
                        {"text": "La démarque inconnue", "isCorrect": False},
                        {"text": "L'inventaire tournant permanent", "isCorrect": False}
                    ],
                    "correction": "Le facing (ou façade) est l'action de remettre en ordre les produits sur le bord de la tablette. Cela améliore la visibilité de l'offre et l'esthétique du rayon."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel niveau de présentation assure généralement les meilleures ventes pour un produit ?",
                    "answerOptions": [
                        {"text": "Niveau des yeux", "isCorrect": True},
                        {"text": "Niveau des mains", "isCorrect": False},
                        {"text": "Niveau du sol", "isCorrect": False},
                        {"text": "Niveau du chapeau", "isCorrect": False}
                    ],
                    "correction": "Le niveau des yeux est la zone la plus vendeuse ('le niveau des yeux est le niveau des achats') car le client voit le produit sans effort. Le niveau des mains est le second plus performant."
                },
                {
                    "questionNumber": 23,
                    "question": "Lors du réassort, où doit-on placer les nouveaux produits par rapport aux anciens ?",
                    "answerOptions": [
                        {"text": "Derrière les anciens", "isCorrect": True},
                        {"text": "Devant les anciens", "isCorrect": False},
                        {"text": "Au dessus des anciens", "isCorrect": False},
                        {"text": "Sur une autre étagère", "isCorrect": False}
                    ],
                    "correction": "Pour garantir la rotation des stocks et respecter la méthode FIFO (First In, First Out), les produits ayant la date la plus courte (les anciens) doivent rester devant pour être vendus en premier."
                },
                {
                    "questionNumber": 24,
                    "question": "En plus du prix de vente, quelle information de prix est obligatoire sur l'étiquette d'un produit alimentaire ?",
                    "answerOptions": [
                        {"text": "Prix à l'unité de mesure", "isCorrect": True},
                        {"text": "Marge commerciale du magasin", "isCorrect": False},
                        {"text": "Coût de transport du produit", "isCorrect": False},
                        {"text": "Historique des prix pratiqués", "isCorrect": False}
                    ],
                    "correction": "L'affichage du prix à l'unité de mesure (prix au kilo ou au litre) est obligatoire. Il permet au consommateur de comparer les prix de produits de contenances différentes."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel type d'implantation consiste à disposer une famille de produits du haut vers le bas de la gondole ?",
                    "answerOptions": [
                        {"text": "Verticale", "isCorrect": True},
                        {"text": "Horizontale", "isCorrect": False},
                        {"text": "Aléatoire", "isCorrect": False},
                        {"text": "Diagonale", "isCorrect": False}
                    ],
                    "correction": "L'implantation verticale est privilégiée car elle oblige le client à balayer le rayon du regard de haut en bas et de gauche à droite, augmentant la visibilité de l'ensemble de la gamme."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la première action à effectuer avant de poser de nouveaux produits sur une étagère vide ?",
                    "answerOptions": [
                        {"text": "Nettoyer", "isCorrect": True},
                        {"text": "Compter", "isCorrect": False},
                        {"text": "Baliser", "isCorrect": False},
                        {"text": "Commander", "isCorrect": False}
                    ],
                    "correction": "L'hygiène est un prérequis commercial et sanitaire. On profite toujours d'une rupture ou d'un réassort pour dépoussiérer et nettoyer la tablette avant de la remplir."
                },
                {
                    "questionNumber": 27,
                    "question": "Que désigne le sigle ILV dans un magasin ?",
                    "answerOptions": [
                        {"text": "Information sur le Lieu de Vente", "isCorrect": True},
                        {"text": "Impôt Légal sur la Vente", "isCorrect": False},
                        {"text": "Inventaire Lourd de Vérification", "isCorrect": False},
                        {"text": "Indice Large de Valorisation", "isCorrect": False}
                    ],
                    "correction": "L'ILV (signalétique, panneaux directionnels) sert à guider et informer le client dans le magasin, contrairement à la PLV qui sert à promouvoir un produit spécifique."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment appelle-t-on l'absence d'un produit en rayon alors qu'il devrait y être ?",
                    "answerOptions": [
                        {"text": "Rupture", "isCorrect": True},
                        {"text": "Surstock", "isCorrect": False},
                        {"text": "Démarque", "isCorrect": False},
                        {"text": "Assortiment", "isCorrect": False}
                    ],
                    "correction": "La rupture de stock est l'ennemi du commerçant : elle entraîne une perte de chiffre d'affaires immédiate et peut détériorer l'image du magasin aux yeux des clients."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle technique consiste à placer des produits complémentaires côte à côte (ex: pinceaux à côté de la peinture) ?",
                    "answerOptions": [
                        {"text": "Cross-merchandising", "isCorrect": True},
                        {"text": "Gestion administrative des stocks", "isCorrect": False},
                        {"text": "Théâtralisation de l'offre commerciale", "isCorrect": False},
                        {"text": "Approvisionnement automatique assisté", "isCorrect": False}
                    ],
                    "correction": "Le cross-merchandising (ou ventes croisées) suggère au client un achat additionnel logique en rapprochant des produits appartenant à des univers différents mais consommés ensemble."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel emplacement est stratégique pour mettre en avant les promotions en entrée d'allée ?",
                    "answerOptions": [
                        {"text": "Tête de gondole", "isCorrect": True},
                        {"text": "Pied de gondole", "isCorrect": False},
                        {"text": "Fond de rayon", "isCorrect": False},
                        {"text": "Zone de caisse", "isCorrect": False}
                    ],
                    "correction": "La Tête de Gondole (TG) est l'emplacement situé à l'extrémité du rayon, donnant sur l'allée de circulation principale. C'est une zone promotionnelle majeure."
                },
                {
                    "questionNumber": 31,
                    "question": "Si le prix en rayon est de 10€ et le prix scanné en caisse est de 12€, quel prix le client doit-il payer ?",
                    "answerOptions": [
                        {"text": "10 euros", "isCorrect": True},
                        {"text": "11 euros", "isCorrect": False},
                        {"text": "12 euros", "isCorrect": False},
                        {"text": "22 euros", "isCorrect": False}
                    ],
                    "correction": "En cas d'erreur d'étiquetage en défaveur du client, le magasin est légalement tenu d'appliquer le prix affiché en rayon (le plus bas), sauf si ce prix est dérisoire."
                },
                {
                    "questionNumber": 32,
                    "question": "Comment appelle-t-on la zone du magasin proche de l'entrée où la circulation des clients est la plus forte ?",
                    "answerOptions": [
                        {"text": "Zone chaude", "isCorrect": True},
                        {"text": "Zone froide", "isCorrect": False},
                        {"text": "Zone tiède", "isCorrect": False},
                        {"text": "Zone morte", "isCorrect": False}
                    ],
                    "correction": "La zone chaude est la partie du magasin où le flux clients est naturel et dense. On y place souvent les produits d'achat d'impulsion ou les promotions fortes."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel terme désigne l'adaptation de l'assortiment en fonction des événements du calendrier (Noël, Rentrée, Pâques) ?",
                    "answerOptions": [
                        {"text": "Saisonnalité", "isCorrect": True},
                        {"text": "Fidélisation", "isCorrect": False},
                        {"text": "Segmentation", "isCorrect": False},
                        {"text": "Canalisation", "isCorrect": False}
                    ],
                    "correction": "La saisonnalité rythme la vie commerciale. L'équipier doit adapter les mises en avant et les commandes en fonction de ces événements pour répondre à la demande ponctuelle."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est l'objectif principal de la PLV (Publicité sur le Lieu de Vente) ?",
                    "answerOptions": [
                        {"text": "Déclencher l'achat", "isCorrect": True},
                        {"text": "Surveiller le vol", "isCorrect": False},
                        {"text": "Gérer les stocks", "isCorrect": False},
                        {"text": "Nettoyer le sol", "isCorrect": False}
                    ],
                    "correction": "La PLV (affiches, stops-rayons, présentoirs) a pour but d'attirer l'attention du client sur un produit pour transformer son intérêt en acte d'achat."
                },
                {
                    "questionNumber": 35,
                    "question": "Que représente le 'nombre de facings' d'un produit ?",
                    "answerOptions": [
                        {"text": "Nombre de produits vus de face", "isCorrect": True},
                        {"text": "Nombre total de produits en stock", "isCorrect": False},
                        {"text": "Nombre de produits commandés hier", "isCorrect": False},
                        {"text": "Nombre de produits périmés jetés", "isCorrect": False}
                    ],
                    "correction": "Le facing (exprimé en nombre) correspond à la largeur accordée au produit sur la tablette. Un facing de 3 signifie que 3 produits sont visibles de front par le client."
                },
                {
                    "questionNumber": 36,
                    "question": "Pour une mise en avant 'Barbecue', quel produit est le plus logique à associer au charbon de bois ?",
                    "answerOptions": [
                        {"text": "Allume-feu", "isCorrect": True},
                        {"text": "Lessive liquide", "isCorrect": False},
                        {"text": "Stylo à bille", "isCorrect": False},
                        {"text": "Lait demi-écrémé", "isCorrect": False}
                    ],
                    "correction": "C'est une logique de besoin client. L'allume-feu est indispensable à l'utilisation du charbon. Les associer facilite la vie du client et augmente le panier moyen."
                },
                {
                    "questionNumber": 37,
                    "question": "Où doit être positionnée l'étiquette prix par rapport au produit en rayon ?",
                    "answerOptions": [
                        {"text": "Juste en dessous", "isCorrect": True},
                        {"text": "Juste au dessus", "isCorrect": False},
                        {"text": "Sur le côté gauche", "isCorrect": False},
                        {"text": "Sur le côté droit", "isCorrect": False}
                    ],
                    "correction": "Par convention et pour éviter toute confusion, l'étiquette prix (électronique ou papier) se place sur la réglette, juste en dessous du produit correspondant."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel type d'achat est réalisé sans planification, à la vue du produit ?",
                    "answerOptions": [
                        {"text": "Impulsion", "isCorrect": True},
                        {"text": "Réfléchi", "isCorrect": False},
                        {"text": "Routinier", "isCorrect": False},
                        {"text": "Obligatoire", "isCorrect": False}
                    ],
                    "correction": "L'achat d'impulsion est un achat 'coup de cœur' non prévu sur la liste de courses. Une bonne mise en valeur (TG, îlot) favorise ce type d'achat."
                },
                {
                    "questionNumber": 39,
                    "question": "Dans l'assortiment, que désigne la 'largeur' de l'offre ?",
                    "answerOptions": [
                        {"text": "Le nombre de familles de produits", "isCorrect": True},
                        {"text": "Le nombre de références par famille", "isCorrect": False},
                        {"text": "La taille physique des produits", "isCorrect": False},
                        {"text": "La surface totale du magasin", "isCorrect": False}
                    ],
                    "correction": "La largeur correspond à la diversité des besoins couverts (ex: épicerie, liquide, frais). La profondeur correspond au choix (marques, tailles) à l'intérieur d'une famille."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel risque présente un carton laissé vide au milieu d'une allée pendant le remplissage ?",
                    "answerOptions": [
                        {"text": "Chute client", "isCorrect": True},
                        {"text": "Rupture stock", "isCorrect": False},
                        {"text": "Erreur prix", "isCorrect": False},
                        {"text": "Vente vente", "isCorrect": False}
                    ],
                    "correction": "C'est un risque majeur de sécurité (PSE). Tout obstacle dans les allées de circulation peut entraîner la chute d'un client et engager la responsabilité du magasin."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : CONSEIL ET ACCOMPAGNEMENT DU CLIENT (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : CONSEIL ET ACCOMPAGNEMENT DU CLIENT",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la toute première étape incontournable de la prise de contact avec un client ?",
                    "answerOptions": [
                        {"text": "Sourire", "isCorrect": True},
                        {"text": "Demander le budget", "isCorrect": False},
                        {"text": "Présenter un produit", "isCorrect": False},
                        {"text": "Faire une démonstration", "isCorrect": False}
                    ],
                    "correction": "La règle des '4x20' enseigne que les 20 premières secondes sont décisives. Le sourire (même au téléphone) et le regard constituent la base de l'accueil avant toute parole."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel type de question permet d'obtenir un maximum d'informations sur les besoins du client ?",
                    "answerOptions": [
                        {"text": "Ouverte", "isCorrect": True},
                        {"text": "Fermée", "isCorrect": False},
                        {"text": "Alternative", "isCorrect": False},
                        {"text": "Retorique", "isCorrect": False}
                    ],
                    "correction": "Une question ouverte (commençant par CQQCOQP : Comment, Qui, Quoi...) invite le client à s'exprimer librement et à développer ses attentes, contrairement à la question fermée."
                },
                {
                    "questionNumber": 43,
                    "question": "Dans la méthode SONCAS, à quoi correspond la lettre 'S' ?",
                    "answerOptions": [
                        {"text": "Sécurité", "isCorrect": True},
                        {"text": "Service", "isCorrect": False},
                        {"text": "Silence", "isCorrect": False},
                        {"text": "Souplesse", "isCorrect": False}
                    ],
                    "correction": "Le SONCAS (Sécurité, Orgueil, Nouveauté, Confort, Argent, Sympathie) est une typologie qui permet d'identifier les motivations d'achat psychologiques du client. La Sécurité correspond au besoin d'être rassuré (garantie, fiabilité)."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle technique d'écoute active consiste à répéter avec ses propres mots ce que le client vient de dire ?",
                    "answerOptions": [
                        {"text": "Reformulation", "isCorrect": True},
                        {"text": "Interruption", "isCorrect": False},
                        {"text": "Argumentation", "isCorrect": False},
                        {"text": "Conclusion", "isCorrect": False}
                    ],
                    "correction": "La reformulation permet de valider que l'on a bien compris le besoin du client ('Si je vous comprends bien, vous cherchez...') et lui montre qu'il est écouté."
                },
                {
                    "questionNumber": 45,
                    "question": "Que doit faire le vendeur si un client exprime une objection sur le prix ?",
                    "answerOptions": [
                        {"text": "Justifier la valeur du produit", "isCorrect": True},
                        {"text": "Baisser le prix immédiatement", "isCorrect": False},
                        {"text": "Ignorer la remarque du client", "isCorrect": False},
                        {"text": "Dire que le client a tort", "isCorrect": False}
                    ],
                    "correction": "Une objection prix doit être traitée en valorisant le produit (qualité, durabilité, services). On défend le rapport qualité/prix plutôt que de brader l'article tout de suite."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment qualifie-t-on la vente d'un produit qui remplace celui demandé par le client (en cas de rupture par exemple) ?",
                    "answerOptions": [
                        {"text": "Vente de substitution", "isCorrect": True},
                        {"text": "Vente additionnelle", "isCorrect": False},
                        {"text": "Vente complémentaire", "isCorrect": False},
                        {"text": "Vente forcée illégale", "isCorrect": False}
                    ],
                    "correction": "La vente de substitution (ou de report) consiste à proposer un produit équivalent répondant aux mêmes besoins lorsque le produit initialement souhaité n'est pas disponible."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle action permet de fidéliser le client à la fin de la vente ?",
                    "answerOptions": [
                        {"text": "Proposer la carte de fidélité", "isCorrect": True},
                        {"text": "Ranger le rayon immédiatement", "isCorrect": False},
                        {"text": "Partir en pause déjeuner", "isCorrect": False},
                        {"text": "Parler à un collègue", "isCorrect": False}
                    ],
                    "correction": "La proposition de la carte de fidélité ou l'inscription au fichier client permet de créer un lien durable, de collecter des données et d'inciter le client à revenir."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la signification du sigle CAP dans la construction d'un argumentaire ?",
                    "answerOptions": [
                        {"text": "Caractéristique Avantage Preuve", "isCorrect": True},
                        {"text": "Client Achat Produit", "isCorrect": False},
                        {"text": "Commerce Achat Partage", "isCorrect": False},
                        {"text": "Contact Attente Prix", "isCorrect": False}
                    ],
                    "correction": "La méthode CAP structure l'argument : on cite une Caractéristique technique, on la traduit en Avantage pour ce client précis, et on apporte une Preuve (démonstration, label)."
                },
                {
                    "questionNumber": 49,
                    "question": "Si un client hésite entre deux produits, quel type de question peut aider à conclure la vente ?",
                    "answerOptions": [
                        {"text": "Question alternative", "isCorrect": True},
                        {"text": "Question piège", "isCorrect": False},
                        {"text": "Question ouverte", "isCorrect": False},
                        {"text": "Question curieuse", "isCorrect": False}
                    ],
                    "correction": "La question alternative ('Vous préférez le bleu ou le rouge ?') propose un choix restreint qui incite le client à prendre une décision d'achat positive, quelle que soit sa réponse."
                },
                {
                    "questionNumber": 50,
                    "question": "Lors de la prise de congé, que faut-il faire même si le client n'a rien acheté ?",
                    "answerOptions": [
                        {"text": "Rester aimable et saluer", "isCorrect": True},
                        {"text": "Montrer son mécontentement", "isCorrect": False},
                        {"text": "Refuser de dire au revoir", "isCorrect": False},
                        {"text": "Soupirer bruyamment", "isCorrect": False}
                    ],
                    "correction": "La qualité de l'accueil doit être constante. Un client qui n'achète pas aujourd'hui peut revenir demain. La dernière impression (prise de congé) doit rester positive."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel mot désigne l'ensemble des éléments non verbaux (gestes, posture) qui accompagnent le discours du vendeur ?",
                    "answerOptions": [
                        {"text": "La gestuelle", "isCorrect": True},
                        {"text": "Le vocabulaire", "isCorrect": False},
                        {"text": "L'argumentaire", "isCorrect": False},
                        {"text": "La procédure", "isCorrect": False}
                    ],
                    "correction": "La communication non verbale (gestuelle, regard, posture) représente plus de 50% du message perçu par le client. Elle doit être en accord avec le discours verbal."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle proposition correspond à une 'vente complémentaire' pour l'achat d'une paire de chaussures ?",
                    "answerOptions": [
                        {"text": "Cirage", "isCorrect": True},
                        {"text": "Pantalon", "isCorrect": False},
                        {"text": "Chemise", "isCorrect": False},
                        {"text": "Chapeau", "isCorrect": False}
                    ],
                    "correction": "La vente complémentaire est un produit directement lié à l'usage du produit principal (les piles pour un jouet, le cirage pour les chaussures). Le reste est de la vente additionnelle d'opportunité."
                },
                {
                    "questionNumber": 53,
                    "question": "Face à un client agressif qui parle fort en magasin, quelle est la meilleure attitude ?",
                    "answerOptions": [
                        {"text": "Isoler le client du flux", "isCorrect": True},
                        {"text": "Crier plus fort que lui", "isCorrect": False},
                        {"text": "Appeler la police directement", "isCorrect": False},
                        {"text": "Se moquer de lui", "isCorrect": False}
                    ],
                    "correction": "Il faut isoler le client pour ne pas déranger les autres clients ('Venez, nous allons voir cela au calme'), rester courtois mais ferme, et l'écouter pour faire retomber la pression."
                },
                {
                    "questionNumber": 54,
                    "question": "Dans le SONCAS, un client qui demande 'Est-ce que c'est solide ?' exprime une motivation de type :",
                    "answerOptions": [
                        {"text": "Sécurité", "isCorrect": True},
                        {"text": "Orgueil", "isCorrect": False},
                        {"text": "Nouveauté", "isCorrect": False},
                        {"text": "Sympathie", "isCorrect": False}
                    ],
                    "correction": "La recherche de solidité, de fiabilité ou de garantie est typique du profil 'Sécurité'. L'argumentaire doit alors rassurer le client sur la durabilité du produit."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle phrase correspond à la phase de 'recherche des besoins' ?",
                    "answerOptions": [
                        {"text": "Pour quel usage cherchez-vous ce produit ?", "isCorrect": True},
                        {"text": "Ce produit est en promotion exceptionnelle.", "isCorrect": False},
                        {"text": "Passez en caisse, s'il vous plaît.", "isCorrect": False},
                        {"text": "Nous fermons le magasin dans dix minutes.", "isCorrect": False}
                    ],
                    "correction": "C'est une question ouverte d'investigation. Avant de proposer (argumenter), il faut impérativement découvrir ce que le client veut faire (besoin)."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'objectif principal de la démonstration d'un produit ?",
                    "answerOptions": [
                        {"text": "Prouver qu'il fonctionne", "isCorrect": True},
                        {"text": "S'amuser avec le produit", "isCorrect": False},
                        {"text": "Passer le temps en rayon", "isCorrect": False},
                        {"text": "Déballer un modèle neuf", "isCorrect": False}
                    ],
                    "correction": "La démonstration sert de PREUVE (le P de CAP). Elle rend l'avantage concret aux yeux du client et lève souvent les derniers doutes."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'est-ce qu'un 'signal d'achat' émis par le client ?",
                    "answerOptions": [
                        {"text": "Il demande les conditions de livraison", "isCorrect": True},
                        {"text": "Il regarde ailleurs en soupirant", "isCorrect": False},
                        {"text": "Il croise les bras fermement", "isCorrect": False},
                        {"text": "Il répond par monosyllabes", "isCorrect": False}
                    ],
                    "correction": "Un client qui se projette dans l'après-achat (livraison, garantie, entretien) envoie un signal vert. C'est le moment d'arrêter d'argumenter et de conclure la vente."
                },
                {
                    "questionNumber": 58,
                    "question": "Pour un client motivé par l'Argent (SONCAS), quel argument est le plus percutant ?",
                    "answerOptions": [
                        {"text": "Promotion", "isCorrect": True},
                        {"text": "Esthétique", "isCorrect": False},
                        {"text": "Innovation", "isCorrect": False},
                        {"text": "Popularité", "isCorrect": False}
                    ],
                    "correction": "Le profil 'Argent' est sensible à l'économie réalisée, au prix bas, à la promotion ou au retour sur investissement."
                },
                {
                    "questionNumber": 59,
                    "question": "Que signifie l'expression 'garder le contact visuel' avec le client ?",
                    "answerOptions": [
                        {"text": "Regarder le client dans les yeux", "isCorrect": True},
                        {"text": "Fixer le produit sans bouger", "isCorrect": False},
                        {"text": "Regarder ses propres chaussures", "isCorrect": False},
                        {"text": "Surveiller l'écran de l'ordinateur", "isCorrect": False}
                    ],
                    "correction": "Le contact visuel maintient l'attention, crée la confiance et permet d'observer les réactions non verbales du client. C'est une marque de respect et d'intérêt."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle est la bonne attitude si vous ne connaissez pas la réponse à une question technique d'un client ?",
                    "answerOptions": [
                        {"text": "Aller chercher l'information", "isCorrect": True},
                        {"text": "Inventer une réponse crédible", "isCorrect": False},
                        {"text": "Dire que ce n'est pas important", "isCorrect": False},
                        {"text": "Changer de sujet rapidement", "isCorrect": False}
                    ],
                    "correction": "L'honnêteté prime. Il ne faut jamais mentir. La bonne attitude est de dire 'Je ne veux pas vous dire de bêtise, je vérifie tout de suite' et de consulter un collègue ou une fiche technique."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : ENCAISSEMENT ET SERVICES OMNICANAUX (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ENCAISSEMENT ET SERVICES OMNICANAUX",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Comment appelle-t-on la somme d'argent présente dans le tiroir-caisse à l'ouverture du poste pour rendre la monnaie ?",
                    "answerOptions": [
                        {"text": "Fond de caisse", "isCorrect": True},
                        {"text": "Recette journalière", "isCorrect": False},
                        {"text": "Prélèvement intermédiaire", "isCorrect": False},
                        {"text": "Marge commerciale", "isCorrect": False}
                    ],
                    "correction": "Le fond de caisse est la dotation initiale en pièces et petits billets confiée au caissier à l'ouverture pour lui permettre de rendre la monnaie aux premiers clients."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel acronyme résume les règles de politesse indispensables lors du passage en caisse ?",
                    "answerOptions": [
                        {"text": "SBAM", "isCorrect": True},
                        {"text": "FIFO", "isCorrect": False},
                        {"text": "DLUO", "isCorrect": False},
                        {"text": "SMIC", "isCorrect": False}
                    ],
                    "correction": "Le SBAM (Sourire, Bonjour, Au revoir, Merci) est la base comportementale de la relation client en caisse. On y ajoute souvent le + pour le 'regard'."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel document est légalement exigible par le caissier pour accepter un paiement par chèque d'un montant élevé ?",
                    "answerOptions": [
                        {"text": "Pièce d'identité officielle", "isCorrect": True},
                        {"text": "Facture de téléphone récente", "isCorrect": False},
                        {"text": "Carte vitale avec photo", "isCorrect": False},
                        {"text": "Carte de fidélité du magasin", "isCorrect": False}
                    ],
                    "correction": "Pour lutter contre la fraude, le commerçant peut exiger une pièce d'identité officielle (CNI, Passeport, Permis) pour vérifier que le porteur est bien le titulaire du chèque."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel appareil permet de procéder à l'encaissement par carte bancaire ?",
                    "answerOptions": [
                        {"text": "TPE", "isCorrect": True},
                        {"text": "TPV", "isCorrect": False},
                        {"text": "GAB", "isCorrect": False},
                        {"text": "DAB", "isCorrect": False}
                    ],
                    "correction": "Le TPE (Terminal de Paiement Électronique) est le boîtier qui permet de lire la carte bancaire, de saisir le code confidentiel ou d'utiliser le sans contact."
                },
                {
                    "questionNumber": 65,
                    "question": "Que doit faire l'hôte de caisse si un article ne possède pas de code-barres et ne passe pas au scanner ?",
                    "answerOptions": [
                        {"text": "Saisir le code manuellement", "isCorrect": True},
                        {"text": "Inventer un prix approximatif", "isCorrect": False},
                        {"text": "Offrir le produit au client", "isCorrect": False},
                        {"text": "Refuser la vente du produit", "isCorrect": False}
                    ],
                    "correction": "Si le scan échoue, la procédure consiste à saisir manuellement les chiffres du code EAN (Gencod) présents sous les barres, ou à appeler un responsable pour obtenir le prix."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel service permet au client d'acheter sur internet et de venir chercher sa commande en magasin ?",
                    "answerOptions": [
                        {"text": "Click and Collect", "isCorrect": True},
                        {"text": "Cash and Carry", "isCorrect": False},
                        {"text": "Drop shipping", "isCorrect": False},
                        {"text": "Market place", "isCorrect": False}
                    ],
                    "correction": "Le Click & Collect (ou retrait en magasin) est une stratégie omnicanale où le client réserve ou paie en ligne, puis se déplace pour récupérer son achat, générant du trafic en point de vente."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la limite de montant par transaction pour un paiement 'sans contact' classique en France ?",
                    "answerOptions": [
                        {"text": "50 euros", "isCorrect": True},
                        {"text": "20 euros", "isCorrect": False},
                        {"text": "30 euros", "isCorrect": False},
                        {"text": "80 euros", "isCorrect": False}
                    ],
                    "correction": "Le plafond du paiement sans contact a été relevé à 50 euros pour faciliter les transactions rapides et limiter les contacts physiques avec le clavier du terminal."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est l'objectif principal d'un 'prélèvement' en cours de journée à la caisse ?",
                    "answerOptions": [
                        {"text": "Sécuriser les espèces", "isCorrect": True},
                        {"text": "Compter le bénéfice", "isCorrect": False},
                        {"text": "Payer les fournisseurs", "isCorrect": False},
                        {"text": "Rembourser un client", "isCorrect": False}
                    ],
                    "correction": "Le prélèvement consiste à retirer les grosses coupures ou le surplus d'espèces du tiroir-caisse pour les mettre en coffre. Cela réduit le risque de vol en cas de braquage."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel document spécifique sort de l'imprimante de caisse lors de la clôture de la journée pour valider la comptabilité ?",
                    "answerOptions": [
                        {"text": "Ticket Z", "isCorrect": True},
                        {"text": "Bon de livraison", "isCorrect": False},
                        {"text": "Facture acquittée", "isCorrect": False},
                        {"text": "Relevé bancaire", "isCorrect": False}
                    ],
                    "correction": "Le Ticket Z (ou Z de caisse) récapitule le chiffre d'affaires réalisé sur la caisse depuis l'ouverture. Il sert de base pour compter la caisse et vérifier les écarts."
                },
                {
                    "questionNumber": 70,
                    "question": "Si le montant compté dans le tiroir est inférieur au montant théorique indiqué par le logiciel, il y a :",
                    "answerOptions": [
                        {"text": "Manquant de caisse", "isCorrect": True},
                        {"text": "Excédent de caisse", "isCorrect": False},
                        {"text": "Bénéfice net", "isCorrect": False},
                        {"text": "Marge brute", "isCorrect": False}
                    ],
                    "correction": "Un manquant signifie qu'il manque de l'argent physique par rapport à ce qui a été enregistré (souvent dû à une erreur de rendu monnaie en faveur du client ou à un vol)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle action faut-il effectuer impérativement sur un vêtement avant de le mettre dans le sac du client ?",
                    "answerOptions": [
                        {"text": "Démagnétiser l'antivol", "isCorrect": True},
                        {"text": "Couper l'étiquette prix", "isCorrect": False},
                        {"text": "Laver le vêtement", "isCorrect": False},
                        {"text": "Repasser le tissu", "isCorrect": False}
                    ],
                    "correction": "Pour éviter que l'alarme ne sonne à la sortie et ne mette le client dans l'embarras, il est impératif de retirer ou désactiver (démagnétiser) le macaron antivol lors de l'encaissement."
                },
                {
                    "questionNumber": 72,
                    "question": "Quelle est la différence majeure entre l'E-réservation et le Click & Collect ?",
                    "answerOptions": [
                        {"text": "Le paiement se fait en magasin pour l'E-réservation", "isCorrect": True},
                        {"text": "Le paiement se fait en ligne pour l'E-réservation", "isCorrect": False},
                        {"text": "L'E-réservation oblige à acheter le produit réservé", "isCorrect": False},
                        {"text": "Le Click & Collect est plus lent que l'E-réservation", "isCorrect": False}
                    ],
                    "correction": "En E-réservation, le client bloque le produit mais ne paie qu'en magasin après l'avoir vu ou essayé. En Click & Collect, l'achat est ferme et payé (ou engagé) en ligne."
                },
                {
                    "questionNumber": 73,
                    "question": "Que signifie scanner le QR Code de l'application fidélité du client ?",
                    "answerOptions": [
                        {"text": "Identifier le client", "isCorrect": True},
                        {"text": "Payer la commande", "isCorrect": False},
                        {"text": "Vérifier son âge", "isCorrect": False},
                        {"text": "Annuler la vente", "isCorrect": False}
                    ],
                    "correction": "Scanner la carte ou l'application de fidélité permet d'identifier le client dans la base de données pour lui attribuer ses points et appliquer ses remises personnalisées."
                },
                {
                    "questionNumber": 74,
                    "question": "Lorsqu'un client paie en espèces, quelle est la procédure de sécurité pour les billets de 20€ et plus ?",
                    "answerOptions": [
                        {"text": "Vérifier les signes de sécurité", "isCorrect": True},
                        {"text": "Refuser systématiquement le billet", "isCorrect": False},
                        {"text": "Demander une photocopie du billet", "isCorrect": False},
                        {"text": "Appeler la police immédiatement", "isCorrect": False}
                    ],
                    "correction": "Le contrôle des billets (toucher, regarder par transparence, incliner ou utiliser un détecteur UV) est indispensable pour éviter d'encaisser de la fausse monnaie."
                },
                {
                    "questionNumber": 75,
                    "question": "Un client rapporte un produit défectueux sous garantie. Quel document est nécessaire pour traiter sa demande ?",
                    "answerOptions": [
                        {"text": "Preuve d'achat", "isCorrect": True},
                        {"text": "Carte d'identité", "isCorrect": False},
                        {"text": "Permis de conduire", "isCorrect": False},
                        {"text": "Justificatif de domicile", "isCorrect": False}
                    ],
                    "correction": "Le ticket de caisse (ou la facture) constitue la preuve d'achat et la date de départ de la garantie légale. Sans lui, il est difficile de faire valoir ses droits."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle solution permet d'envoyer le ticket de caisse par mail au lieu de l'imprimer ?",
                    "answerOptions": [
                        {"text": "Ticket dématérialisé", "isCorrect": True},
                        {"text": "Archivage numérique fiscal", "isCorrect": False},
                        {"text": "Impression thermique directe", "isCorrect": False},
                        {"text": "Duplicata comptable papier", "isCorrect": False}
                    ],
                    "correction": "La dématérialisation du ticket (e-ticket) est une démarche écologique et pratique prévue par la loi anti-gaspillage, permettant au client de conserver ses preuves d'achat numériquement."
                },
                {
                    "questionNumber": 77,
                    "question": "Que désignent les codes PLU utilisés en caisse pour les fruits et légumes ?",
                    "answerOptions": [
                        {"text": "Codes courts pour identifier les produits vrac", "isCorrect": True},
                        {"text": "Codes pour annuler une ligne d'article", "isCorrect": False},
                        {"text": "Codes secrets pour ouvrir le tiroir", "isCorrect": False},
                        {"text": "Codes postaux des fournisseurs", "isCorrect": False}
                    ],
                    "correction": "Les codes PLU (Price Look Up) sont des codes courts (ex: 4011 pour les bananes) que le caissier saisit pour identifier les produits vendus au poids sans code-barres."
                },
                {
                    "questionNumber": 78,
                    "question": "Un bon d'achat 'non rendu monnaie' signifie que :",
                    "answerOptions": [
                        {"text": "On ne rend pas la monnaie si le montant du bon est supérieur à l'achat", "isCorrect": True},
                        {"text": "On ne peut pas utiliser le bon pour payer", "isCorrect": False},
                        {"text": "On doit rendre la monnaie sur le bon obligatoirement", "isCorrect": False},
                        {"text": "Le bon est périmé et inutilisable", "isCorrect": False}
                    ],
                    "correction": "Si le client utilise un bon de 10€ pour un achat de 8€, le magasin ne rend pas les 2€ de différence. Le client doit compléter son achat pour ne pas perdre cette valeur."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle tablette vendeur permet de commander un produit non disponible en magasin pour le livrer chez le client ?",
                    "answerOptions": [
                        {"text": "Extension de gamme", "isCorrect": True},
                        {"text": "Rupture de charge", "isCorrect": False},
                        {"text": "Inventaire fiscal", "isCorrect": False},
                        {"text": "Balisage rayon", "isCorrect": False}
                    ],
                    "correction": "Les outils d'extension de gamme permettent de proposer au client l'intégralité du catalogue de l'enseigne (le 'stock infini'), même si le produit n'est pas physiquement présent en rayon."
                },
                {
                    "questionNumber": 80,
                    "question": "En fin de journée, si le fond de caisse initial n'est pas retiré de la recette, le chiffre d'affaires sera :",
                    "answerOptions": [
                        {"text": "Faux et surestimé", "isCorrect": True},
                        {"text": "Juste et précis", "isCorrect": False},
                        {"text": "Faux et sous-estimé", "isCorrect": False},
                        {"text": "Égal à zéro", "isCorrect": False}
                    ],
                    "correction": "La recette correspond uniquement à ce que les clients ont payé. Il faut impérativement soustraire le fond de caisse (l'argent mis au début) pour connaître le vrai Chiffre d'Affaires."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : PRÉVENTION, SANTÉ ET ENVIRONNEMENT (PSE) & CADRE JURIDIQUE (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : PRÉVENTION, SANTÉ ET ENVIRONNEMENT (PSE) & CADRE JURIDIQUE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel Équipement de Protection Individuelle (EPI) est obligatoire pour protéger les pieds contre la chute d'objets lourds en réserve ?",
                    "answerOptions": [
                        {"text": "Chaussures de sécurité", "isCorrect": True},
                        {"text": "Baskets de sport confortables", "isCorrect": False},
                        {"text": "Bottes en caoutchouc étanches", "isCorrect": False},
                        {"text": "Sandales de sécurité ouvertes", "isCorrect": False}
                    ],
                    "correction": "Les chaussures de sécurité normées (avec coque renforcée en acier ou composite) sont obligatoires dans les zones de stockage pour prévenir les risques d'écrasement des orteils."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le délai légal de rétractation pour un client ayant effectué un achat sur le site internet de l'enseigne ?",
                    "answerOptions": [
                        {"text": "14 jours", "isCorrect": True},
                        {"text": "7 jours", "isCorrect": False},
                        {"text": "30 jours", "isCorrect": False},
                        {"text": "24 heures", "isCorrect": False}
                    ],
                    "correction": "Dans le cadre de la vente à distance (internet, téléphone), le code de la consommation accorde au client un délai de 14 jours pour changer d'avis et retourner le produit sans justification."
                },
                {
                    "questionNumber": 83,
                    "question": "Que signifie le sigle PRAP dans le domaine de la prévention des risques ?",
                    "answerOptions": [
                        {"text": "Prévention des Risques liés à l'Activité Physique", "isCorrect": True},
                        {"text": "Programme Rapide d'Amélioration de la Productivité", "isCorrect": False},
                        {"text": "Plan Régional d'Action pour le Personnel", "isCorrect": False},
                        {"text": "Procédure Réglementaire d'Administration Physique", "isCorrect": False}
                    ],
                    "correction": "La formation PRAP vise à apprendre les bonnes pratiques (gestes et postures) pour prévenir les troubles musculo-squelettiques (TMS) liés à l'activité professionnelle."
                },
                {
                    "questionNumber": 84,
                    "question": "Quels sont les trois éléments indispensables pour qu'un feu se déclenche (le triangle du feu) ?",
                    "answerOptions": [
                        {"text": "Combustible et comburant et énergie", "isCorrect": True},
                        {"text": "Essence et briquet et oxygène", "isCorrect": False},
                        {"text": "Chaleur et fumée et flamme", "isCorrect": False},
                        {"text": "Vent et papier et étincelle", "isCorrect": False}
                    ],
                    "correction": "Le triangle du feu réunit le Combustible (ce qui brûle), le Comburant (l'oxygène de l'air) et l'Énergie d'activation (chaleur/étincelle). Si l'un manque, le feu s'éteint."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment appelle-t-on la démarque (perte de stock) causée par des vols commis par les employés du magasin ?",
                    "answerOptions": [
                        {"text": "Démarque interne", "isCorrect": True},
                        {"text": "Démarque externe", "isCorrect": False},
                        {"text": "Démarque administrative", "isCorrect": False},
                        {"text": "Démarque technique", "isCorrect": False}
                    ],
                    "correction": "La démarque inconnue se divise principalement en démarque externe (vols clients) et démarque interne (vols personnel ou consommation sur place non payée par les salariés)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le numéro d'appel d'urgence européen à composer pour joindre les secours (SAMU, Pompiers, Police) ?",
                    "answerOptions": [
                        {"text": "112", "isCorrect": True},
                        {"text": "15", "isCorrect": False},
                        {"text": "18", "isCorrect": False},
                        {"text": "17", "isCorrect": False}
                    ],
                    "correction": "Le 112 est le numéro unique disponible gratuitement partout dans l'Union Européenne. Il fonctionne même sans carte SIM ou avec un téléphone verrouillé."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la durée légale de garantie de conformité pour un appareil électroménager neuf ?",
                    "answerOptions": [
                        {"text": "2 ans", "isCorrect": True},
                        {"text": "1 an", "isCorrect": False},
                        {"text": "6 mois", "isCorrect": False},
                        {"text": "10 ans", "isCorrect": False}
                    ],
                    "correction": "La garantie légale de conformité couvre les défauts du bien pendant 2 ans à compter de la délivrance du produit. C'est une obligation légale pour le vendeur professionnel."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle couleur est utilisée pour la signalisation des issues de secours et du matériel de premier secours ?",
                    "answerOptions": [
                        {"text": "Vert", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Bleu", "isCorrect": False}
                    ],
                    "correction": "En signalétique de sécurité, le vert (souvent associé au blanc) indique le sauvetage et les secours (sorties, défibrillateurs). Le rouge indique l'interdiction ou le matériel incendie."
                },
                {
                    "questionNumber": 89,
                    "question": "Que finance l'éco-participation affichée sur le prix des appareils électriques ?",
                    "answerOptions": [
                        {"text": "Le coût de la collecte et du recyclage", "isCorrect": True},
                        {"text": "La marge bénéficiaire du distributeur", "isCorrect": False},
                        {"text": "Le salaire du personnel de rayon", "isCorrect": False},
                        {"text": "La taxe sur la valeur ajoutée", "isCorrect": False}
                    ],
                    "correction": "L'éco-participation (ou éco-contribution) est une somme reversée intégralement aux éco-organismes pour financer la gestion de la fin de vie des produits (DEEE)."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est la règle de sécurité à respecter impérativement lors de l'utilisation d'un cutter ?",
                    "answerOptions": [
                        {"text": "Rétracter la lame immédiatement après usage", "isCorrect": True},
                        {"text": "Laisser la lame sortie pour gagner du temps", "isCorrect": False},
                        {"text": "Mettre le cutter dans sa poche lame sortie", "isCorrect": False},
                        {"text": "Utiliser la lame pour faire levier", "isCorrect": False}
                    ],
                    "correction": "Les coupures sont fréquentes. Il faut toujours utiliser un cutter de sécurité ou rentrer la lame systématiquement dès que la coupe est finie avant de poser l'outil ou de le ranger."
                },
                {
                    "questionNumber": 91,
                    "question": "Un commerçant a-t-il le droit de refuser de vendre un produit disponible à un client sans motif légitime ?",
                    "answerOptions": [
                        {"text": "Non c'est strictement interdit par la loi", "isCorrect": True},
                        {"text": "Oui si le client lui semble antipathique", "isCorrect": False},
                        {"text": "Oui s'il veut garder le produit pour lui", "isCorrect": False},
                        {"text": "Oui si c'est la fin de la journée", "isCorrect": False}
                    ],
                    "correction": "Le refus de vente est un délit (sauf motif légitime comme la vente d'alcool aux mineurs ou un produit réglementé). L'offre exposée doit être vendue à tout demandeur."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel type d'extincteur est préconisé pour éteindre un feu d'origine électrique (tableau électrique) sans endommager le matériel ?",
                    "answerOptions": [
                        {"text": "Extincteur au dioxyde de carbone", "isCorrect": True},
                        {"text": "Extincteur à eau pulvérisée", "isCorrect": False},
                        {"text": "Extincteur à eau avec additif", "isCorrect": False},
                        {"text": "Seau d'eau du robinet", "isCorrect": False}
                    ],
                    "correction": "Le CO2 (dioxyde de carbone) étouffe le feu en privant l'oxygène et ne laisse aucun résidu, ce qui préserve les composants électroniques, contrairement à l'eau ou la poudre."
                },
                {
                    "questionNumber": 93,
                    "question": "Que signifie le logo 'Triman' (petit bonhomme avec trois flèches) présent sur les emballages ?",
                    "answerOptions": [
                        {"text": "Le produit ou l'emballage doit être trié", "isCorrect": True},
                        {"text": "Le produit est fabriqué en France", "isCorrect": False},
                        {"text": "Le produit est issu de l'agriculture biologique", "isCorrect": False},
                        {"text": "Le produit est dangereux pour la santé", "isCorrect": False}
                    ],
                    "correction": "Le logo Triman indique au consommateur que le produit ou l'emballage ne doit pas être jeté dans la poubelle tout-venant mais doit faire l'objet d'un tri (bac jaune, borne verre, etc.)."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le principal objectif du RGPD (Règlement Général sur la Protection des Données) en magasin ?",
                    "answerOptions": [
                        {"text": "Protéger les données personnelles des clients", "isCorrect": True},
                        {"text": "Augmenter les ventes par email", "isCorrect": False},
                        {"text": "Surveiller la navigation internet des salariés", "isCorrect": False},
                        {"text": "Simplifier la comptabilité du magasin", "isCorrect": False}
                    ],
                    "correction": "Le RGPD impose des règles strictes pour garantir que les données collectées (nom, adresse, email, téléphone) soient sécurisées et utilisées uniquement avec l'accord du client."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle mention est obligatoire sur l'étiquette d'un produit alimentaire pour protéger les personnes allergiques ?",
                    "answerOptions": [
                        {"text": "La liste des allergènes en gras", "isCorrect": True},
                        {"text": "Le nom du directeur du magasin", "isCorrect": False},
                        {"text": "La recette complète du produit", "isCorrect": False},
                        {"text": "La photo de l'usine de fabrication", "isCorrect": False}
                    ],
                    "correction": "Les 14 allergènes majeurs (arachides, lait, œufs, gluten...) doivent être mis en évidence typographiquement (gras, italique, souligné) dans la liste des ingrédients."
                },
                {
                    "questionNumber": 96,
                    "question": "En cas d'évacuation du magasin suite à une alarme incendie, où le personnel et les clients doivent-ils se rendre ?",
                    "answerOptions": [
                        {"text": "Au point de rassemblement", "isCorrect": True},
                        {"text": "Dans la réserve du magasin", "isCorrect": False},
                        {"text": "Aux toilettes du personnel", "isCorrect": False},
                        {"text": "Dans leur véhicule personnel", "isCorrect": False}
                    ],
                    "correction": "En cas d'alarme, il faut évacuer les locaux dans le calme et se diriger vers le point de rassemblement (signalé par un panneau vert) pour le recensement des personnes."
                },
                {
                    "questionNumber": 97,
                    "question": "Qu'est-ce qu'un 'Accident de Travail' ?",
                    "answerOptions": [
                        {"text": "Un accident survenu par le fait ou à l'occasion du travail", "isCorrect": True},
                        {"text": "Un accident survenu pendant les vacances annuelles", "isCorrect": False},
                        {"text": "Une maladie chronique qui apparaît lentement", "isCorrect": False},
                        {"text": "Une dispute verbale avec un collègue de travail", "isCorrect": False}
                    ],
                    "correction": "Pour être qualifié d'accident du travail, l'événement doit être soudain et survenir pendant les heures de travail et sur le lieu de travail (ou lors d'une mission)."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle est la bonne posture pour ramasser un carton posé au sol ?",
                    "answerOptions": [
                        {"text": "Se rapprocher et fléchir les jambes", "isCorrect": True},
                        {"text": "Garder les jambes raides et courber le dos", "isCorrect": False},
                        {"text": "Se pencher sur le côté en torsion", "isCorrect": False},
                        {"text": "Tirer le carton avec une seule main", "isCorrect": False}
                    ],
                    "correction": "Pour protéger la colonne vertébrale, il faut encadrer la charge, garder le dos droit et utiliser la force des cuisses (fléchissement) pour soulever la charge."
                },
                {
                    "questionNumber": 99,
                    "question": "Qui est le salarié formé pour intervenir en premier lieu en cas d'accident ou de malaise au sein de l'équipe ?",
                    "answerOptions": [
                        {"text": "Le Sauveteur Secouriste du Travail", "isCorrect": True},
                        {"text": "Le délégué du personnel titulaire", "isCorrect": False},
                        {"text": "Le responsable des ressources humaines", "isCorrect": False},
                        {"text": "Le comptable de l'entreprise", "isCorrect": False}
                    ],
                    "correction": "Le SST (Sauveteur Secouriste du Travail) est un employé formé aux premiers secours et à la prévention des risques, capable d'intervenir en attendant les pompiers ou le SAMU."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle pratique commerciale trompeuse consiste à afficher un prix bas en rayon mais à en passer un plus élevé en caisse délibérément ?",
                    "answerOptions": [
                        {"text": "Publicité mensongère", "isCorrect": True},
                        {"text": "Vente à perte autorisée", "isCorrect": False},
                        {"text": "Dumping commercial", "isCorrect": False},
                        {"text": "Mécénat d'entreprise", "isCorrect": False}
                    ],
                    "correction": "Si l'erreur est délibérée ou répétée sans correction malgré les signalements, cela peut être qualifié de pratique commerciale trompeuse, lourdement sanctionnée par la répression des fraudes."
                }
            ]
        }
    }
}