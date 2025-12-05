# Fichier : quiz_cap_epc_100.py

quiz_data = {
    "title": "Quiz CAP Équipier Polyvalent du Commerce : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : RÉCEPTION ET GESTION DES STOCKS (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Réception et Gestion des Stocks (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel document permet de vérifier la conformité de la marchandise livrée (quantité, référence, état) ?",
                    "answerOptions": [
                        {"text": "Le ticket de caisse.", "isCorrect": False},
                        {"text": "Le Bon de Livraison (BL) ou le Bordereau de Transport.", "isCorrect": True},
                        {"text": "Le catalogue fournisseur.", "isCorrect": False},
                        {"text": "L'étiquette de prix.", "isCorrect": False}
                    ],
                    "correction": "Le **Bon de Livraison** sert de preuve de réception et de contrôle qualitatif/quantitatif."
                },
                {
                    "questionNumber": 2,
                    "question": "Que doit-on faire en cas de casse, de produit manquant ou de produit endommagé lors de la réception ?",
                    "answerOptions": [
                        {"text": "Refuser toute la livraison.", "isCorrect": False},
                        {"text": "Émettre une 'Réserve' précise, datée et signée sur le Bon de Livraison (en présence du livreur) et alerter immédiatement le responsable.", "isCorrect": True},
                        {"text": "Accepter et jeter les produits abîmés.", "isCorrect": False},
                        {"text": "Contacter directement le fabricant.", "isCorrect": False}
                    ],
                    "correction": "La **Réserve** est la seule preuve valable en cas de litige avec le transporteur."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la méthode d'organisation des stocks consistant à sortir les produits les plus anciens en premier pour éviter l'obsolescence (notamment pour les produits périssables) ?",
                    "answerOptions": [
                        {"text": "LIFO (Last In, First Out).", "isCorrect": False},
                        {"text": "FIFO (First In, First Out).", "isCorrect": True},
                        {"text": "Juste-à-temps.", "isCorrect": False},
                        {"text": "Méthode du Point de Commande.", "isCorrect": False}
                    ],
                    "correction": "La méthode **FIFO** (Premier entré, Premier sorti) est essentielle pour la gestion des dates de péremption."
                },
                {
                    "questionNumber": 4,
                    "question": "Que représente un **Inventaire** pour le magasin ?",
                    "answerOptions": [
                        {"text": "La liste des clients.", "isCorrect": False},
                        {"text": "L'opération de comptage physique de tous les produits présents en magasin et en réserve afin de connaître la valeur exacte du stock.", "isCorrect": True},
                        {"text": "Le plan de masse du magasin.", "isCorrect": False},
                        {"text": "Le chiffre d'affaires du jour.", "isCorrect": False}
                    ],
                    "correction": "L'**Inventaire** permet de corriger l'écart entre le stock théorique (informatique) et le stock réel (physique)."
                },
                {
                    "questionNumber": 5,
                    "question": "Qu'est-ce que le **taux de démarque inconnue** ?",
                    "answerOptions": [
                        {"text": "La promotion sur les produits.", "isCorrect": False},
                        {"text": "La différence entre le stock théorique (informatique) et le stock réel (inventaire), généralement due au vol, à la casse non enregistrée ou aux erreurs de gestion.", "isCorrect": True},
                        {"text": "Le pourcentage de produits vendus.", "isCorrect": False},
                        {"text": "Le pourcentage de clients satisfaits.", "isCorrect": False}
                    ],
                    "correction": "La **Démarque Inconnue** est un indicateur de perte pour l'entreprise."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est l'outil couramment utilisé pour l'identification rapide des produits lors de la réception et de l'encaissement ?",
                    "answerOptions": [
                        {"text": "Le Télécopieur.", "isCorrect": False},
                        {"text": "Le Code-barres (EAN - European Article Numbering).", "isCorrect": True},
                        {"text": "Le marqueur.", "isCorrect": False},
                        {"text": "Le chronomètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Code-barres** est la clé de la gestion informatisée des stocks et de la caisse."
                },
                {
                    "questionNumber": 7,
                    "question": "Que signifie l'acronyme **DLC** ?",
                    "answerOptions": [
                        {"text": "Délai de Livraison Courte.", "isCorrect": False},
                        {"text": "Date Limite de Consommation (date au-delà de laquelle la consommation du produit est dangereuse).", "isCorrect": True},
                        {"text": "Durée Légale du Contrat.", "isCorrect": False},
                        {"text": "Délai de Liquidation des Commandes.", "isCorrect": False}
                    ],
                    "correction": "La **DLC** est obligatoire pour les produits très périssables (viandes, produits laitiers frais, etc.)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est l'importance de ranger les produits lourds en bas des rayonnages ou des palettes ?",
                    "answerOptions": [
                        {"text": "Pour mieux les voir.", "isCorrect": False},
                        {"text": "Pour des raisons de Sécurité (stabilité des palettes, prévention des chutes d'objets lourds sur les employés ou les clients).", "isCorrect": True},
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Pour respecter le FIFO.", "isCorrect": False}
                    ],
                    "correction": "Le rangement est avant tout une question de **sécurité**."
                },
                {
                    "questionNumber": 9,
                    "question": "Qu'est-ce qu'un **rupture de stock** ?",
                    "answerOptions": [
                        {"text": "Un produit très demandé.", "isCorrect": False},
                        {"text": "L'absence temporaire ou définitive d'un produit en rayon ou en réserve alors qu'il est normalement demandé par les clients.", "isCorrect": True},
                        {"text": "Un produit en promotion.", "isCorrect": False},
                        {"text": "Une erreur de prix.", "isCorrect": False}
                    ],
                    "correction": "La **Rupture de Stock** est une perte de vente directe pour le magasin."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel équipement de manutention doit-on utiliser pour déplacer de lourdes palettes dans la réserve ?",
                    "answerOptions": [
                        {"text": "Un chariot de ménage.", "isCorrect": False},
                        {"text": "Un transpalette manuel ou électrique (avec habilitation si moteur).", "isCorrect": True},
                        {"text": "Un diable.", "isCorrect": False},
                        {"text": "Un caddie standard.", "isCorrect": False}
                    ],
                    "correction": "Le **Transpalette** est l'outil de base pour la manutention horizontale des palettes."
                },
                {
                    "questionNumber": 11,
                    "question": "Dans le processus de réception, après le contrôle qualitatif et quantitatif du BL, quelle est l'étape suivante ?",
                    "answerOptions": [
                        {"text": "La vente immédiate.", "isCorrect": False},
                        {"text": "Le rangement immédiat des produits (mise en réserve ou mise en rayon) après étiquetage et déballage.", "isCorrect": True},
                        {"text": "La destruction des emballages.", "isCorrect": False},
                        {"text": "La pause-café.", "isCorrect": False}
                    ],
                    "correction": "Le **Rangement** doit être rapide pour libérer l'espace et éviter la démarque."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le rôle du **stock de sécurité** ?",
                    "answerOptions": [
                        {"text": "Être en promotion.", "isCorrect": False},
                        {"text": "Protéger l'entreprise contre les ruptures de stock imprévues (retards de livraison, commandes imprévues des clients).", "isCorrect": True},
                        {"text": "Servir de monnaie de caisse.", "isCorrect": False},
                        {"text": "Être vendu en ligne.", "isCorrect": False}
                    ],
                    "correction": "Le **Stock de Sécurité** est une assurance contre les aléas commerciaux."
                },
                {
                    "questionNumber": 13,
                    "question": "Qu'est-ce que l'opération de 'facing' en réserve ?",
                    "answerOptions": [
                        {"text": "Nettoyer les étagères.", "isCorrect": False},
                        {"text": "Mettre les produits en évidence en les alignant et en les avançant sur le rayonnage pour rendre la référence immédiatement visible (s'applique aussi en rayon).", "isCorrect": True},
                        {"text": "Compter les produits.", "isCorrect": False},
                        {"text": "Vérifier la température.", "isCorrect": False}
                    ],
                    "correction": "Le **Facing** est une technique de présentation et de gestion du stock."
                },
                {
                    "questionNumber": 14,
                    "question": "Que signifie l'acronyme **DLUO** (remplacé par DDM) ?",
                    "answerOptions": [
                        {"text": "Durée Légale d'Utilisation des Ouvrages.", "isCorrect": False},
                        {"text": "Date Limite d'Utilisation Optimale (ou DDM : Date de Durabilité Minimale). Le produit peut être consommé après cette date sans danger, mais ses qualités (goût, texture) peuvent être altérées.", "isCorrect": True},
                        {"text": "Délai de Livraison Urgent et Obligatoire.", "isCorrect": False},
                        {"text": "Date de Lancement des Opérations.", "isCorrect": False}
                    ],
                    "correction": "La **DLUO/DDM** est plus souple que la DLC et concerne les produits secs ou à longue durée de vie (café, conserves)."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est le principal danger d'un sol encombré dans la zone de réception ou de stockage ?",
                    "answerOptions": [
                        {"text": "La saleté.", "isCorrect": False},
                        {"text": "Le risque d'accident du travail (chute, glissade, trébuchement) ou de dégradation du matériel de manutention.", "isCorrect": True},
                        {"text": "Le vol.", "isCorrect": False},
                        {"text": "La chaleur.", "isCorrect": False}
                    ],
                    "correction": "L'**Ordre et la Propreté** sont essentiels pour la sécurité au travail (prévention des accidents)."
                },
                {
                    "questionNumber": 16,
                    "question": "Qu'est-ce que le **Conditionnement** d'un produit ?",
                    "answerOptions": [
                        {"text": "Le prix de vente.", "isCorrect": False},
                        {"text": "L'emballage individuel destiné au consommateur (bouteille, carton, sachet).", "isCorrect": True},
                        {"text": "Le poids total.", "isCorrect": False},
                        {"text": "Le lieu de fabrication.", "isCorrect": False}
                    ],
                    "correction": "Le **Conditionnement** est la première unité de vente."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le rôle d'une **chambre froide négative** dans la réserve ?",
                    "answerOptions": [
                        {"text": "Conserver les fruits et légumes frais.", "isCorrect": False},
                        {"text": "Stocker les produits Surgelés (températures inférieures à $0^\circ \text{C}$, généralement autour de $-18^\circ \text{C}$).", "isCorrect": True},
                        {"text": "Conserver les boissons fraîches.", "isCorrect": False},
                        {"text": "Conserver les produits secs.", "isCorrect": False}
                    ],
                    "correction": "La **Chambre Froide Négative** est pour les surgelés et congelés."
                },
                {
                    "questionNumber": 18,
                    "question": "Comment appelle-t-on le niveau de stock qui déclenche automatiquement une nouvelle commande auprès du fournisseur ?",
                    "answerOptions": [
                        {"text": "Le stock d'alerte.", "isCorrect": False},
                        {"text": "Le **Point de Commande** (niveau de stock couvrant la consommation pendant le délai de livraison).", "isCorrect": True},
                        {"text": "Le stock mort.", "isCorrect": False},
                        {"text": "Le stock maximal.", "isCorrect": False}
                    ],
                    "correction": "Le **Point de Commande** est crucial pour la continuité des ventes."
                },
                {
                    "questionNumber": 19,
                    "question": "Qu'est-ce qu'un **colisage** (ou unité de manutention) ?",
                    "answerOptions": [
                        {"text": "Le poids d'un produit.", "isCorrect": False},
                        {"text": "Le nombre d'unités de vente (conditionnements) contenues dans un carton ou une caisse de livraison.", "isCorrect": True},
                        {"text": "Le prix d'un produit.", "isCorrect": False},
                        {"text": "La référence d'un produit.", "isCorrect": False}
                    ],
                    "correction": "Le **Colisage** est l'unité logistique (carton)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est l'objectif principal de la **rotation des stocks** ?",
                    "answerOptions": [
                        {"text": "Augmenter les prix.", "isCorrect": False},
                        {"text": "Vendre rapidement la marchandise stockée pour minimiser les coûts de stockage, éviter l'obsolescence, et optimiser le besoin en fonds de roulement.", "isCorrect": True},
                        {"text": "Ralentir les ventes.", "isCorrect": False},
                        {"text": "Diminuer les commandes.", "isCorrect": False}
                    ],
                    "correction": "La **Rotation** mesure la performance du stock (plus elle est rapide, mieux c'est)."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : MERCHANDISING ET MISE EN RAYON (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Merchandising et Mise en Rayon (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est l'importance du **Facing** dans la mise en rayon ?",
                    "answerOptions": [
                        {"text": "Réduire le vol.", "isCorrect": False},
                        {"text": "Améliorer la visibilité du produit (attractivité), faciliter la prise en main par le client et donner une image de rayon 'plein' et bien géré.", "isCorrect": True},
                        {"text": "Augmenter les prix.", "isCorrect": False},
                        {"text": "Vérifier le stock.", "isCorrect": False}
                    ],
                    "correction": "Le **Facing** est l'action d'avancer les produits en bord de rayon."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la zone du rayon la plus favorable à la vente des produits pour le client (hauteur des yeux) ?",
                    "answerOptions": [
                        {"text": "Le niveau supérieur (chapeau de gondole).", "isCorrect": False},
                        {"text": "Le niveau central (ou Niveau de la main, entre $1.10 \text{ m}$ et $1.60 \text{ m}$ de hauteur).", "isCorrect": True},
                        {"text": "Le niveau inférieur (sol).", "isCorrect": False},
                        {"text": "La caisse.", "isCorrect": False}
                    ],
                    "correction": "Le **Niveau des Yeux/Main** est le plus efficace pour les produits à forte marge ou les produits phares."
                },
                {
                    "questionNumber": 23,
                    "question": "Qu'est-ce qu'une **Tête de Gondole (TG)** ?",
                    "answerOptions": [
                        {"text": "Le bout du rayon.", "isCorrect": False},
                        {"text": "L'extrémité d'un rayonnage, emplacement stratégique très visible et réservé aux promotions, aux nouveautés ou aux produits saisonniers.", "isCorrect": True},
                        {"text": "Le premier produit du rayon.", "isCorrect": False},
                        {"text": "Le coin du magasin.", "isCorrect": False}
                    ],
                    "correction": "La **Tête de Gondole** est un emplacement 'chaud' pour les ventes promotionnelles."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle du **Planogramme** ?",
                    "answerOptions": [
                        {"text": "Vérifier le stock.", "isCorrect": False},
                        {"text": "Document visuel (plan) détaillant l'implantation précise des produits sur les linéaires (nombre de facings, positionnement horizontal/vertical, espace alloué).", "isCorrect": True},
                        {"text": "Gérer les horaires du personnel.", "isCorrect": False},
                        {"text": "Calculer le chiffre d'affaires.", "isCorrect": False}
                    ],
                    "correction": "Le **Planogramme** est la bible de l'équipier pour la mise en rayon."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la règle d'affichage obligatoire pour tout produit en vente dans le magasin ?",
                    "answerOptions": [
                        {"text": "L'origine de fabrication.", "isCorrect": False},
                        {"text": "L'étiquette de prix doit être claire, lisible et bien placée à proximité immédiate du produit (Prix de Vente Unitaire et Prix au Kilo/Litre/Volume).", "isCorrect": True},
                        {"text": "Le nom du fournisseur.", "isCorrect": False},
                        {"text": "Le nom du responsable.", "isCorrect": False}
                    ],
                    "correction": "L'affichage du **Prix** est la première obligation légale."
                },
                {
                    "questionNumber": 26,
                    "question": "Qu'est-ce que le **cross-merchandising** (ou vente complémentaire) ?",
                    "answerOptions": [
                        {"text": "Vendre des produits différents.", "isCorrect": False},
                        {"text": "Placer ensemble, dans le même rayon ou à proximité, des produits complémentaires (ex : chips à côté de la bière, moutarde à côté de la charcuterie) pour stimuler l'achat additionnel.", "isCorrect": True},
                        {"text": "Vendre le même produit à deux prix différents.", "isCorrect": False},
                        {"text": "Vendre uniquement des produits en promotion.", "isCorrect": False}
                    ],
                    "correction": "Le **Cross-merchandising** vise à augmenter le panier moyen du client."
                },
                {
                    "questionNumber": 27,
                    "question": "Que doit-on vérifier en priorité lors de la mise en rayon de produits alimentaires périssables ?",
                    "answerOptions": [
                        {"text": "Le packaging.", "isCorrect": False},
                        {"text": "La **Date Limite de Consommation (DLC)** ou DDM et l'état de l'emballage (intégrité, température de stockage).", "isCorrect": True},
                        {"text": "Le planogramme.", "isCorrect": False},
                        {"text": "Le prix de revient.", "isCorrect": False}
                    ],
                    "correction": "La **Date** est la clé de la sécurité alimentaire."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est l'importance de l'**éclairage** et de l'**ambiance sonore** dans un magasin ?",
                    "answerOptions": [
                        {"text": "Elles n'ont aucune importance.", "isCorrect": False},
                        {"text": "Elles contribuent à l'expérience client (atmosphère agréable, mise en valeur des produits) et influencent positivement le temps passé en magasin et donc les achats.", "isCorrect": True},
                        {"text": "Elles augmentent le prix des produits.", "isCorrect": False},
                        {"text": "Elles réduisent le stock.", "isCorrect": False}
                    ],
                    "correction": "L'**Ambiance** est un facteur clé du merchandising d'atmosphère."
                },
                {
                    "questionNumber": 29,
                    "question": "Qu'est-ce qu'une **zone froide** dans un magasin ?",
                    "answerOptions": [
                        {"text": "La zone des surgelés.", "isCorrect": False},
                        {"text": "Une zone peu fréquentée ou mal éclairée, où les produits se vendent moins bien (souvent au début des rayons ou dans les coins).", "isCorrect": True},
                        {"text": "La réserve.", "isCorrect": False},
                        {"text": "La caisse.", "isCorrect": False}
                    ],
                    "correction": "Les **Zones Froides** nécessitent des efforts de mise en valeur (promotions, théâtralisation) pour y attirer le client."
                },
                {
                    "questionNumber": 30,
                    "question": "Pourquoi doit-on effectuer le retrait des produits dont la DLC est proche ?",
                    "answerOptions": [
                        {"text": "Pour les vendre plus cher.", "isCorrect": False},
                        {"text": "Pour garantir la Sécurité Alimentaire du consommateur et éviter les risques d'intoxication, en suivant la règle des 'retraits $J-3$' par exemple.", "isCorrect": True},
                        {"text": "Pour les mettre en tête de gondole.", "isCorrect": False},
                        {"text": "Pour les stocker plus longtemps.", "isCorrect": False}
                    ],
                    "correction": "Le **Retrait des DLC courtes** est une obligation légale et sanitaire."
                },
                {
                    "questionNumber": 31,
                    "question": "Qu'est-ce qu'un **Lineaire au sol** ?",
                    "answerOptions": [
                        {"text": "La longueur du magasin.", "isCorrect": False},
                        {"text": "La longueur totale de rayonnage utilisée pour présenter les produits, mesurée au sol (en mètres).", "isCorrect": True},
                        {"text": "La hauteur des étagères.", "isCorrect": False},
                        {"text": "Le nombre de produits.", "isCorrect": False}
                    ],
                    "correction": "Le **Linéaire** est l'espace de vente alloué à un produit ou à une marque."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est la bonne pratique pour l'étiquetage des produits en promotion ?",
                    "answerOptions": [
                        {"text": "Écrire le prix au stylo.", "isCorrect": False},
                        {"text": "Afficher clairement le prix initial BARRÉ à côté du nouveau prix promotionnel, en respectant la législation sur les annonces de réduction de prix.", "isCorrect": True},
                        {"text": "Cacher l'ancien prix.", "isCorrect": False},
                        {"text": "Ne rien afficher.", "isCorrect": False}
                    ],
                    "correction": "L'**Affichage double** est obligatoire lors d'une promotion pour justifier la réduction."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la différence entre un **affichage prix unitaire** et un **prix au kilo/litre** ?",
                    "answerOptions": [
                        {"text": "C'est la même chose.", "isCorrect": False},
                        {"text": "Le prix unitaire est le prix de l'article seul. Le prix au kilo/litre (Prix de Vente au Poids/Volume) est obligatoire pour faciliter la comparaison entre les produits de différents formats.", "isCorrect": True},
                        {"text": "Le prix au kilo n'est pas obligatoire.", "isCorrect": False},
                        {"text": "Le prix unitaire est pour la caisse.", "isCorrect": False}
                    ],
                    "correction": "Le **Prix au Kilo/Litre** est essentiel pour la transparence de l'information consommateur."
                },
                {
                    "questionNumber": 34,
                    "question": "Qu'est-ce que la **Zone Chaude** d'un magasin ?",
                    "answerOptions": [
                        {"text": "La zone près des fourneaux.", "isCorrect": False},
                        {"text": "Une zone à très forte fréquentation et d'achat rapide (ex: les allées principales, l'entrée du magasin, la zone de caisses).", "isCorrect": True},
                        {"text": "La réserve.", "isCorrect": False},
                        {"text": "Le bureau du directeur.", "isCorrect": False}
                    ],
                    "correction": "Les **Zones Chaudes** sont idéales pour les achats d'impulsion."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment s'appelle l'opération qui consiste à étaler les produits sur toute la surface de vente allouée pour éviter les 'trous' dans le rayon ?",
                    "answerOptions": [
                        {"text": "Le réassort.", "isCorrect": False},
                        {"text": "Le remplissage ou le réapprovisionnement de fond (mise en rayon).", "isCorrect": True},
                        {"text": "Le comptage.", "isCorrect": False},
                        {"text": "La manutention.", "isCorrect": False}
                    ],
                    "correction": "Le **Remplissage** doit être effectué dès que possible pour éviter les ruptures visuelles."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est la principale fonction du **Stop-rayon** (ou réglette de prix) ?",
                    "answerOptions": [
                        {"text": "Empêcher le vol.", "isCorrect": False},
                        {"text": "Identifier clairement le prix, la référence, et servir de support aux éventuels messages promotionnels (affichage).", "isCorrect": True},
                        {"text": "Bloquer les produits.", "isCorrect": False},
                        {"text": "Mesurer la longueur du rayon.", "isCorrect": False}
                    ],
                    "correction": "Le **Stop-rayon** assure la lisibilité des prix et des informations."
                },
                {
                    "questionNumber": 37,
                    "question": "Qu'est-ce qu'un **ILV (Information sur le Lieu de Vente)** ?",
                    "answerOptions": [
                        {"text": "Un panneau de signalisation routière.", "isCorrect": False},
                        {"text": "Tout support de communication (affiche, écran, flyer) installé dans l'environnement du point de vente pour informer le consommateur sur les caractéristiques d'un produit, son prix ou son utilisation.", "isCorrect": True},
                        {"text": "Un fournisseur.", "isCorrect": False},
                        {"text": "Un client.", "isCorrect": False}
                    ],
                    "correction": "L'**ILV** a une fonction informative, contrairement à la PLV (Publicité sur Lieu de Vente) qui est plus incitative."
                },
                {
                    "questionNumber": 38,
                    "question": "Que signifie **UDO** (Unité de Détail Ouverte) en gestion de rayon ?",
                    "answerOptions": [
                        {"text": "Une unité de fabrication.", "isCorrect": False},
                        {"text": "Le fait de placer un produit déballé ou un échantillon en rayon pour permettre au client de le manipuler ou de le visualiser (tester un produit, voir sa taille réelle).", "isCorrect": True},
                        {"text": "Un carton vide.", "isCorrect": False},
                        {"text": "Une unité de stockage.", "isCorrect": False}
                    ],
                    "correction": "L'**UDO** est courante dans les rayons textile, bricolage ou parfumerie."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le risque principal de laisser un carton vide au sol dans l'allée du magasin ?",
                    "answerOptions": [
                        {"text": "Salissure.", "isCorrect": False},
                        {"text": "Chute du client (responsabilité civile du magasin) et risque d'entrave pour les chariots ou les personnes à mobilité réduite.", "isCorrect": True},
                        {"text": "Vol.", "isCorrect": False},
                        {"text": "Rupture de stock.", "isCorrect": False}
                    ],
                    "correction": "La **Sécurité du Client** et la propreté du magasin sont primordiales."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment doit-on organiser les produits dans un rayon pour faciliter l'achat client ?",
                    "answerOptions": [
                        {"text": "Par couleur.", "isCorrect": False},
                        {"text": "Par Famille de produits, puis par Sous-famille (catégorisation) : par exemple, Biscuits sucrés -> Gâteaux secs -> Petits-déjeuners.", "isCorrect": True},
                        {"text": "Par prix décroissant.", "isCorrect": False},
                        {"text": "Par date de réception.", "isCorrect": False}
                    ],
                    "correction": "Le **Classement par Famille** est la base de l'organisation commerciale (facilite la recherche)."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : RELATION CLIENT ET CONSEIL (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Relation Client et Conseil (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la première étape d'un bon contact avec un client en rayon ?",
                    "answerOptions": [
                        {"text": "Lui proposer une promotion.", "isCorrect": False},
                        {"text": "L'accueil (sourire, regard, 'Bonjour', 'Je peux vous renseigner ?') et l'écoute active pour identifier son besoin.", "isCorrect": True},
                        {"text": "Lui demander son nom.", "isCorrect": False},
                        {"text": "Lui tendre un produit.", "isCorrect": False}
                    ],
                    "correction": "L'**Accueil** et l'écoute sont les fondements de la relation client."
                },
                {
                    "questionNumber": 42,
                    "question": "Que doit-on faire lorsqu'un client formule une réclamation (produit défectueux, erreur de prix) ?",
                    "answerOptions": [
                        {"text": "L'ignorer.", "isCorrect": False},
                        {"text": "Écouter attentivement (sans couper), s'excuser pour le désagrément, chercher une solution (échange, remboursement ou bon d'achat) et transmettre l'information au responsable.", "isCorrect": True},
                        {"text": "Renvoyer le client vers le fournisseur.", "isCorrect": False},
                        {"text": "Argumenter longuement pour justifier l'erreur.", "isCorrect": False}
                    ],
                    "correction": "La gestion des **Réclamations** doit être rapide et empathique pour fidéliser le client."
                },
                {
                    "questionNumber": 43,
                    "question": "Qu'est-ce qu'une **vente additionnelle** (ou complémentaire) ?",
                    "answerOptions": [
                        {"text": "Vendre le produit principal.", "isCorrect": False},
                        {"text": "Proposer au client des produits qui complètent son achat principal (ex: vendre des piles avec un jouet, un cirage avec des chaussures, un accessoire avec un téléphone).", "isCorrect": True},
                        {"text": "Vendre un produit en solde.", "isCorrect": False},
                        {"text": "Vendre un produit de marque.", "isCorrect": False}
                    ],
                    "correction": "La **Vente Additionnelle** est une technique pour augmenter le panier moyen."
                },
                {
                    "questionNumber": 44,
                    "question": "Que signifie la méthode de vente **CAB** (Caractéristiques, Avantages, Bénéfices) ?",
                    "answerOptions": [
                        {"text": "Méthode de stockage.", "isCorrect": False},
                        {"text": "Technique de persuasion où l'on décrit les Caractéristiques du produit, puis ce qu'elles apportent (Avantages), et enfin ce que le client y gagne personnellement (Bénéfices).", "isCorrect": True},
                        {"text": "Méthode d'encaissement.", "isCorrect": False},
                        {"text": "Méthode de gestion des stocks.", "isCorrect": False}
                    ],
                    "correction": "Le client achète le **Bénéfice** (ce que le produit fait pour lui), pas la caractéristique technique."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment doit-on gérer un client qui se plaint du **prix élevé** d'un produit ?",
                    "answerOptions": [
                        {"text": "Être d'accord avec lui.", "isCorrect": False},
                        {"text": "Valoriser le produit en mettant en avant ses Bénéfices (qualité, durabilité, service après-vente) pour justifier le prix (argumenter la valeur).", "isCorrect": True},
                        {"text": "Baisser le prix sans consulter le responsable.", "isCorrect": False},
                        {"text": "Lui dire d'aller acheter ailleurs.", "isCorrect": False}
                    ],
                    "correction": "Il faut transformer l'objection **Prix** en argument **Qualité/Service**."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le rôle du **langage corporel** (non-verbal) dans la relation client ?",
                    "answerOptions": [
                        {"text": "Il n'a pas d'importance.", "isCorrect": False},
                        {"text": "Il transmet $70 \text{%}$ du message : posture ouverte, sourire, regard, gestes posés sont essentiels pour inspirer confiance et amabilité.", "isCorrect": True},
                        {"text": "Il permet de se reposer.", "isCorrect": False},
                        {"text": "Il sert à porter les produits.", "isCorrect": False}
                    ],
                    "correction": "Le **Non-Verbal** est plus puissant que les mots."
                },
                {
                    "questionNumber": 47,
                    "question": "Qu'est-ce que la **Zone de Chalandise** du magasin ?",
                    "answerOptions": [
                        {"text": "Le parking du magasin.", "isCorrect": False},
                        {"text": "La zone géographique (quartier, ville, région) d'où provient la majorité de la clientèle et où le magasin exerce son attractivité.", "isCorrect": True},
                        {"text": "La réserve.", "isCorrect": False},
                        {"text": "Le rayon des surgelés.", "isCorrect": False}
                    ],
                    "correction": "La **Zone de Chalandise** est l'aire d'influence commerciale du point de vente."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'objectif de l'étape de **Découverte** dans l'entretien de vente ?",
                    "answerOptions": [
                        {"text": "Parler du prix.", "isCorrect": False},
                        {"text": "Poser des questions ouvertes (QQOQCP) pour comprendre les motivations, les besoins précis, les préférences et le budget du client.", "isCorrect": True},
                        {"text": "Montrer le produit.", "isCorrect": False},
                        {"text": "Finaliser l'encaissement.", "isCorrect": False}
                    ],
                    "correction": "La **Découverte** permet de proposer la bonne solution (produit)."
                },
                {
                    "questionNumber": 49,
                    "question": "Que faire si un client vous pose une question technique à laquelle vous ne savez pas répondre ?",
                    "answerOptions": [
                        {"text": "Inventer la réponse.", "isCorrect": False},
                        {"text": "Ne pas répondre et dire que vous ne savez pas.", "isCorrect": False},
                        {"text": "Reconnaître que vous n'avez pas l'information, et proposer immédiatement de vous renseigner auprès d'un collègue expert ou d'un responsable.", "isCorrect": True},
                        {"text": "Lui donner la fiche technique.", "isCorrect": False}
                    ],
                    "correction": "L'**Honnêteté** et le service sont essentiels ; le client doit obtenir la bonne information."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le dernier stade de l'entretien de vente, après l'argumentation et la réponse aux objections ?",
                    "answerOptions": [
                        {"text": "La découverte des besoins.", "isCorrect": False},
                        {"text": "La **Conclusion/Prise de Congé** (validation de l'achat, proposition de services, accompagnement en caisse et remerciement).", "isCorrect": True},
                        {"text": "La présentation du produit.", "isCorrect": False},
                        {"text": "La négociation.", "isCorrect": False}
                    ],
                    "correction": "La **Conclusion** doit être positive et ouvrir sur la fidélisation."
                },
                {
                    "questionNumber": 51,
                    "question": "Qu'est-ce que la **fidélisation** client ?",
                    "answerOptions": [
                        {"text": "Ne jamais revoir le client.", "isCorrect": False},
                        {"text": "L'ensemble des actions visant à inciter un client à renouveler ses achats et à devenir un client régulier (carte de fidélité, e-mailing, service après-vente).", "isCorrect": True},
                        {"text": "La vente d'un seul produit.", "isCorrect": False},
                        {"text": "L'encaissement.", "isCorrect": False}
                    ],
                    "correction": "Un **Client Fidèle** coûte moins cher qu'un nouveau client (rentabilité)."
                },
                {
                    "questionNumber": 52,
                    "question": "Que signifie l'acronyme **SAV** ?",
                    "answerOptions": [
                        {"text": "Service Avant Vente.", "isCorrect": False},
                        {"text": "Service Après-Vente (gestion des garanties, réparations, retours, réclamations).", "isCorrect": True},
                        {"text": "Stockage A Vif.", "isCorrect": False},
                        {"text": "Sécurité Alimentaire Vérifiée.", "isCorrect": False}
                    ],
                    "correction": "Le **SAV** est un facteur clé de la satisfaction et de la fidélisation."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est l'objectif de la **Reformulation** dans l'entretien de vente ?",
                    "answerOptions": [
                        {"text": "Parler de soi.", "isCorrect": False},
                        {"text": "Confirmer au client que vous avez bien compris son besoin et vérifier qu'il est d'accord avec votre compréhension avant de proposer une solution.", "isCorrect": True},
                        {"text": "Changer de sujet.", "isCorrect": False},
                        {"text": "Lui demander de répéter.", "isCorrect": False}
                    ],
                    "correction": "La **Reformulation** sécurise l'échange."
                },
                {
                    "questionNumber": 54,
                    "question": "Comment doit-on accueillir un client s'il y a déjà une personne en attente d'aide ?",
                    "answerOptions": [
                        {"text": "Ignorer le second client.", "isCorrect": False},
                        {"text": "Accueillir brièvement le second client par un signe de tête ou une formule ('Je suis à vous dans un instant') pour accuser réception de sa présence.", "isCorrect": True},
                        {"text": "Lui demander d'attendre dehors.", "isCorrect": False},
                        {"text": "S'excuser auprès du premier client et changer d'interlocuteur.", "isCorrect": False}
                    ],
                    "correction": "La **Reconnaissance** de l'attente est importante pour la satisfaction client."
                },
                {
                    "questionNumber": 55,
                    "question": "Qu'est-ce que la **Vente d'impulsion** ?",
                    "answerOptions": [
                        {"text": "Une vente longue et réfléchie.", "isCorrect": False},
                        {"text": "Un achat non planifié, déclenché par l'attractivité d'un produit, souvent placé dans des zones chaudes (Tête de gondole, zone de caisses).", "isCorrect": True},
                        {"text": "Une vente par catalogue.", "isCorrect": False},
                        {"text": "Une vente à crédit.", "isCorrect": False}
                    ],
                    "correction": "Les produits de **Vente d'Impulsion** sont souvent peu chers et très visibles."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le rôle du vendeur en matière de **Garantie Légale de Conformité** ?",
                    "answerOptions": [
                        {"text": "Le client est responsable.", "isCorrect": False},
                        {"text": "Le vendeur doit informer le client de l'existence de cette garantie (2 ans à compter de la délivrance) qui couvre les défauts non visibles au moment de l'achat.", "isCorrect": True},
                        {"text": "La garantie ne concerne que les produits chers.", "isCorrect": False},
                        {"text": "La garantie n'est que d'un mois.", "isCorrect": False}
                    ],
                    "correction": "La **Garantie Légale** est une obligation d'information du vendeur."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment s'appelle l'ensemble des caractéristiques qui rendent le magasin unique (couleurs, logo, musique, odeur) ?",
                    "answerOptions": [
                        {"text": "Le plan de masse.", "isCorrect": False},
                        {"text": "L'**Identité Visuelle et Sensorielle** ou l'Atmosphère du point de vente.", "isCorrect": True},
                        {"text": "Le stock mort.", "isCorrect": False},
                        {"text": "Le linéaire développé.", "isCorrect": False}
                    ],
                    "correction": "L'**Identité** est essentielle pour l'image de marque et la différenciation."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle est la règle d'or concernant le **téléphone portable personnel** en présence d'un client ?",
                    "answerOptions": [
                        {"text": "Le laisser sonner fort.", "isCorrect": False},
                        {"text": "Le laisser en mode silencieux et ne pas l'utiliser en présence du client, car cela donne une image de manque de professionnalisme et d'irrespect.", "isCorrect": True},
                        {"text": "L'utiliser pour envoyer des SMS.", "isCorrect": False},
                        {"text": "Le poser sur le comptoir.", "isCorrect": False}
                    ],
                    "correction": "Le téléphone portable est un facteur de distraction et de mauvaise image professionnelle."
                },
                {
                    "questionNumber": 59,
                    "question": "Qu'est-ce qu'une **objection** dans la vente ?",
                    "answerOptions": [
                        {"text": "Une question facile.", "isCorrect": False},
                        {"text": "L'expression d'un doute ou d'un frein par le client (prix, qualité, besoin, délai) qui doit être traitée par le vendeur avant de conclure la vente.", "isCorrect": True},
                        {"text": "Un compliment.", "isCorrect": False},
                        {"text": "Une affirmation.", "isCorrect": False}
                    ],
                    "correction": "L'**Objection** est l'occasion de rassurer le client et d'argumenter."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est l'intérêt d'inciter le client à adhérer au **programme de fidélité** du magasin ?",
                    "answerOptions": [
                        {"text": "Rendre la vente plus longue.", "isCorrect": False},
                        {"text": "Offrir des avantages au client (réductions, cadeaux) et permettre au magasin de collecter des données pour mieux connaître ses habitudes d'achat (marketing ciblé).", "isCorrect": True},
                        {"text": "Augmenter le prix.", "isCorrect": False},
                        {"text": "Le fatiguer.", "isCorrect": False}
                    ],
                    "correction": "Le **Programme de Fidélité** est un outil de marketing et de rétention client."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : ENVIRONNEMENT JURIDIQUE ET SÉCURITÉ (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Environnement Juridique et Sécurité (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le document légal qui justifie l'achat d'un produit (preuve pour un échange ou un remboursement) ?",
                    "answerOptions": [
                        {"text": "La facture de commande.", "isCorrect": False},
                        {"text": "Le Ticket de Caisse ou la Facturette d'Encaissement.", "isCorrect": True},
                        {"text": "Le catalogue.", "isCorrect": False},
                        {"text": "Le bon de livraison.", "isCorrect": False}
                    ],
                    "correction": "Le **Ticket de Caisse** est la preuve d'achat pour le consommateur."
                },
                {
                    "questionNumber": 62,
                    "question": "Que doit faire un employé s'il constate un incendie dans le magasin ?",
                    "answerOptions": [
                        {"text": "Partir en courant.", "isCorrect": False},
                        {"text": "Alerter immédiatement (crier 'Au feu', donner l'alarme), tenter d'éteindre si c'est un départ de feu gérable avec un extincteur, et suivre les instructions d'évacuation (Plan d'évacuation).", "isCorrect": True},
                        {"text": "Fermer les portes.", "isCorrect": False},
                        {"text": "Continuer à servir les clients.", "isCorrect": False}
                    ],
                    "correction": "La priorité est l'**Alerte et la Sécurité des Personnes**."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelles sont les conditions obligatoires pour l'affichage du prix en rayon ?",
                    "answerOptions": [
                        {"text": "Il doit être écrit au crayon.", "isCorrect": False},
                        {"text": "Affichage clair, lisible, non équivoque (pas d'ambiguïté entre plusieurs produits) et correspondre au prix facturé en caisse.", "isCorrect": True},
                        {"text": "Il doit être caché.", "isCorrect": False},
                        {"text": "Il peut être oral.", "isCorrect": False}
                    ],
                    "correction": "Le client doit connaître le **Prix** avant de s'engager (principe de l'information préalable)."
                },
                {
                    "questionNumber": 64,
                    "question": "Qu'est-ce qu'un **Extincteur à eau pulvérisée** avec additif ?",
                    "answerOptions": [
                        {"text": "Pour le gaz.", "isCorrect": False},
                        {"text": "Le plus courant, utilisé pour les feux de classe $\text{A}$ (matériaux solides, bois, papiers, tissus) et $\text{B}$ (liquides inflammables, hydrocarbures).", "isCorrect": True},
                        {"text": "Pour le métal.", "isCorrect": False},
                        {"text": "Pour les installations électriques.", "isCorrect": False}
                    ],
                    "correction": "L'**Extincteur à Eau Pulvérisée** est le standard dans les commerces pour les feux solides/liquides."
                },
                {
                    "questionNumber": 65,
                    "question": "Qu'est-ce qu'une **Marque de Certification NF** sur un produit ?",
                    "answerOptions": [
                        {"text": "Un prix spécial.", "isCorrect": False},
                        {"text": "La certification de conformité aux normes françaises et internationales, assurant la qualité, la fiabilité et la sécurité d'utilisation du produit.", "isCorrect": True},
                        {"text": "Une marque du magasin.", "isCorrect": False},
                        {"text": "Une obligation de recyclage.", "isCorrect": False}
                    ],
                    "correction": "La **Marque NF** est un gage de qualité et de sécurité pour le consommateur."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le rôle du **délégué du personnel (ou CSE)** en matière de sécurité ?",
                    "answerOptions": [
                        {"text": "Gérer les salaires.", "isCorrect": False},
                        {"text": "Représenter les salariés, contribuer à l'amélioration des conditions de travail et d'hygiène, et procéder à des enquêtes en cas d'accident du travail.", "isCorrect": True},
                        {"text": "Définir les promotions.", "isCorrect": False},
                        {"text": "Gérer les livraisons.", "isCorrect": False}
                    ],
                    "correction": "Le **CSE** est l'organe de représentation et de prévention des risques professionnels."
                },
                {
                    "questionNumber": 67,
                    "question": "Que signifie le marquage **CE** sur un jouet ou un appareil électrique ?",
                    "answerOptions": [
                        {"text": "Produit local.", "isCorrect": False},
                        {"text": "Conformité Européenne (certification obligatoire) : le produit est conforme aux exigences de sécurité et de santé de l'Union Européenne.", "isCorrect": True},
                        {"text": "Contrôle Externe.", "isCorrect": False},
                        {"text": "Certification Environnementale.", "isCorrect": False}
                    ],
                    "correction": "Le **Marquage CE** est la condition d'entrée sur le marché européen."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le principe de base de l'hygiène alimentaire lors de la manipulation de produits frais (viande, poisson, traiteur) ?",
                    "answerOptions": [
                        {"text": "Porter un tablier.", "isCorrect": False},
                        {"text": "Le lavage fréquent des mains, le port de gants et de charlotte (si nécessaire), et le respect strict de la chaîne du froid (température de stockage).", "isCorrect": True},
                        {"text": "Ne pas parler.", "isCorrect": False},
                        {"text": "Ne pas les toucher.", "isCorrect": False}
                    ],
                    "correction": "L'**Hygiène** est fondamentale pour éviter la contamination croisée (transmission de bactéries)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est l'outil obligatoire en caisse permettant de prévenir le vol à l'étalage ?",
                    "answerOptions": [
                        {"text": "Le téléphone.", "isCorrect": False},
                        {"text": "Le miroir de surveillance, le système anti-vol (portiques, étiquettes antivol) et la surveillance vidéo (si existante).", "isCorrect": True},
                        {"text": "Le clavier.", "isCorrect": False},
                        {"text": "La calculatrice.", "isCorrect": False}
                    ],
                    "correction": "Les **Systèmes Anti-Vol** et la vigilance sont les principaux moyens de dissuasion."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle est l'interdiction principale concernant les aliments dans la réserve ou les zones de stockage non alimentaires ?",
                    "answerOptions": [
                        {"text": "Ils doivent être emballés.", "isCorrect": False},
                        {"text": "Interdiction de stocker ensemble des produits alimentaires et non-alimentaires (chimiques, d'entretien, droguerie) pour éviter toute contamination.", "isCorrect": True},
                        {"text": "Ils doivent être cachés.", "isCorrect": False},
                        {"text": "Ils doivent être froids.", "isCorrect": False}
                    ],
                    "correction": "La **Séparation** des zones est un principe de sécurité et d'hygiène."
                },
                {
                    "questionNumber": 71,
                    "question": "Que doit faire l'équipier polyvalent s'il constate un risque d'accident (sol glissant, étagère instable) ?",
                    "answerOptions": [
                        {"text": "Rien.", "isCorrect": False},
                        {"text": "Signaler immédiatement le danger (baliser), corriger la situation si possible (nettoyer/ranger), et prévenir le responsable.", "isCorrect": True},
                        {"text": "Attendre un client.", "isCorrect": False},
                        {"text": "Crier.", "isCorrect": False}
                    ],
                    "correction": "La **Prévention** est la responsabilité de tous."
                },
                {
                    "questionNumber": 72,
                    "question": "Quelle est la température maximale légale de stockage des produits réfrigérés (frais) en réserve ?",
                    "answerOptions": [
                        {"text": "$10^\circ \text{C}$", "isCorrect": False},
                        {"text": "Généralement inférieure ou égale à $+4^\circ \text{C}$ (selon le produit, la température exacte étant précisée par le fournisseur).", "isCorrect": True},
                        {"text": "$0^\circ \text{C}$", "isCorrect": False},
                        {"text": "$15^\circ \text{C}$", "isCorrect": False}
                    ],
                    "correction": "Le respect strict de la **Chaîne du Froid** est une exigence réglementaire."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la sanction pour un magasin qui vend des produits dont la DLC est dépassée ?",
                    "answerOptions": [
                        {"text": "Un simple avertissement.", "isCorrect": False},
                        {"text": "Des Amendes lourdes, la fermeture administrative du rayon ou du magasin, et des poursuites pénales en cas d'intoxication (non-respect de la sécurité alimentaire).", "isCorrect": True},
                        {"text": "Rien.", "isCorrect": False},
                        {"text": "Une réduction d'impôt.", "isCorrect": False}
                    ],
                    "correction": "La **DLC** est un point de contrôle majeur des services d'hygiène (DGCCRF)."
                },
                {
                    "questionNumber": 74,
                    "question": "Qu'est-ce que le **Droit de Rétractation** pour un client (hors produits alimentaires frais) ?",
                    "answerOptions": [
                        {"text": "Le droit de rendre le produit à tout moment.", "isCorrect": False},
                        {"text": "Le droit pour le consommateur de changer d'avis et d'annuler une commande ou un achat (notamment en ligne) dans un délai de $14$ jours sans avoir à justifier de motif.", "isCorrect": True},
                        {"text": "Le droit de négocier le prix.", "isCorrect": False},
                        {"text": "Le droit d'utiliser le produit avant de l'acheter.", "isCorrect": False}
                    ],
                    "correction": "Le **Droit de Rétractation** concerne surtout la vente à distance et le démarchage."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est l'EPI (Équipement de Protection Individuelle) obligatoire en zone de réserve pour le maniement des palettes et cartons lourds ?",
                    "answerOptions": [
                        {"text": "Un casque de chantier.", "isCorrect": False},
                        {"text": "Des Chaussures de sécurité (coquées) pour prévenir les écrasements d'orteils.", "isCorrect": True},
                        {"text": "Un gilet jaune.", "isCorrect": False},
                        {"text": "Un masque.", "isCorrect": False}
                    ],
                    "correction": "Les **Chaussures de Sécurité** sont le $\text{EPI}$ de base en logistique."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle est la règle de base pour manipuler un **Extincteur** ?",
                    "answerOptions": [
                        {"text": "Viser en haut du feu.", "isCorrect": False},
                        {"text": "Déclencher l'alarme, décrocher, dégoupiller, et attaquer la base des flammes par balayage (en s'assurant que la voie de sortie est toujours libre).", "isCorrect": True},
                        {"text": "Le jeter sur le feu.", "isCorrect": False},
                        {"text": "Le vider entièrement sans viser.", "isCorrect": False}
                    ],
                    "correction": "Il faut viser la **Base des Flammes**."
                },
                {
                    "questionNumber": 77,
                    "question": "Qu'est-ce que le **délit de tromperie** sur la marchandise ?",
                    "answerOptions": [
                        {"text": "Voler un produit.", "isCorrect": False},
                        {"text": "Le fait de mentir sciemment sur les qualités substantielles du produit (origine, composition, quantité, caractéristiques essentielles) auprès du consommateur.", "isCorrect": True},
                        {"text": "Vendre cher.", "isCorrect": False},
                        {"text": "Vendre en promotion.", "isCorrect": False}
                    ],
                    "correction": "Le **Délit de Tromperie** est sévèrement puni (contrôle de la $\text{DGCCRF}$)."
                },
                {
                    "questionNumber": 78,
                    "question": "Pourquoi doit-on utiliser la **bonne posture** (jambes fléchies, dos droit) pour soulever des charges lourdes ?",
                    "answerOptions": [
                        {"text": "Pour aller plus vite.", "isCorrect": False},
                        {"text": "Pour prévenir les Troubles Musculo-Squelettiques (TMS), les lombalgies et les blessures en sollicitant la force des jambes plutôt que le dos.", "isCorrect": True},
                        {"text": "Pour mieux voir.", "isCorrect": False},
                        {"text": "Pour mieux tenir la charge.", "isCorrect": False}
                    ],
                    "correction": "La **Manutention Manuelle** est la cause principale des TMS en commerce/logistique."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le principe de la **Traçabilité** des produits alimentaires ?",
                    "answerOptions": [
                        {"text": "Le produit est beau.", "isCorrect": False},
                        {"text": "Capacité à suivre à la trace un produit (ou ses ingrédients) depuis sa production jusqu'à sa vente (et vice-versa) grâce aux numéros de lot, pour garantir la sécurité et gérer les rappels.", "isCorrect": True},
                        {"text": "Le produit est en promotion.", "isCorrect": False},
                        {"text": "Le produit est cher.", "isCorrect": False}
                    ],
                    "correction": "La **Traçabilité** est vitale en cas de crise sanitaire (rappel de produit)."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment s'appelle l'obligation de reprendre les produits électriques et électroniques usagés (vieux appareils) lors de l'achat d'un neuf ?",
                    "answerOptions": [
                        {"text": "Le droit de rétractation.", "isCorrect": False},
                        {"text": "L'obligation de Reprise $1$ pour $1$ (filière $\text{DEEE}$ : Déchets d'Équipements Électriques et Électroniques).", "isCorrect": True},
                        {"text": "La garantie légale.", "isCorrect": False},
                        {"text": "L'offre de remboursement.", "isCorrect": False}
                    ],
                    "correction": "La **Reprise $1$ pour $1$** est une obligation légale pour le recyclage des appareils."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : OPÉRATIONS DE CAISSE ET TÂCHES ANNEXES (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Opérations de Caisse et Tâches Annexes (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la première action à effectuer lors de la prise de poste à la caisse ?",
                    "answerOptions": [
                        {"text": "Servir un client.", "isCorrect": False},
                        {"text": "L'allumage du TPV (Terminal Point de Vente) et la **Vérification du Fond de Caisse** (montant initial en monnaie et billets) en le comptant et en le validant.", "isCorrect": True},
                        {"text": "Mettre les produits en rayon.", "isCorrect": False},
                        {"text": "Allumer la lumière.", "isCorrect": False}
                    ],
                    "correction": "Le **Fond de Caisse** est la base de la responsabilité de la caissière."
                },
                {
                    "questionNumber": 82,
                    "question": "Que doit-on faire si le **Code-barres** d'un produit ne passe pas au scanner ?",
                    "answerOptions": [
                        {"text": "Ne pas le faire payer.", "isCorrect": False},
                        {"text": "Tenter une nouvelle lecture, puis saisir manuellement la référence et le prix sur le clavier de la caisse (si l'identification est certaine).", "isCorrect": True},
                        {"text": "Donner le produit au client.", "isCorrect": False},
                        {"text": "Appeler le directeur.", "isCorrect": False}
                    ],
                    "correction": "La **Saisie Manuelle** permet de maintenir la fluidité du passage en caisse."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est le moyen de paiement le plus sécurisé pour le magasin (sans risque de chèque impayé ou de faux billets) ?",
                    "answerOptions": [
                        {"text": "Le Chèque.", "isCorrect": False},
                        {"text": "La Carte Bancaire (CB) avec saisie du code ou paiement sans contact, validée par l'appareil TPE (Terminal de Paiement Électronique).", "isCorrect": True},
                        {"text": "L'Espèce (billets).", "isCorrect": False},
                        {"text": "Les tickets restaurant.", "isCorrect": False}
                    ],
                    "correction": "Le paiement par **CB** est une transaction sécurisée par la banque."
                },
                {
                    "questionNumber": 84,
                    "question": "Qu'est-ce qu'un **Décompte de caisse** (ou arrêt de caisse) ?",
                    "answerOptions": [
                        {"text": "La fermeture du magasin.", "isCorrect": False},
                        {"text": "L'opération de comptage de l'argent (pièces, billets, chèques, CB) à la fin du service ou de la journée pour vérifier l'exactitude des sommes encaissées (calcul de la recette).", "isCorrect": True},
                        {"text": "Le rangement des produits.", "isCorrect": False},
                        {"text": "Le réassort.", "isCorrect": False}
                    ],
                    "correction": "Le **Décompte** permet de détecter les erreurs (trop-perçu/manque)."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment doit-on rendre la monnaie à un client ?",
                    "answerOptions": [
                        {"text": "La jeter dans le tiroir.", "isCorrect": False},
                        {"text": "Annoncer le montant reçu, compter et annoncer la monnaie rendue au client, en présentant la monnaie (pièces puis billets) posée à plat pour éviter les erreurs et les contestations.", "isCorrect": True},
                        {"text": "Laisser le client se servir.", "isCorrect": False},
                        {"text": "Ne pas compter.", "isCorrect": False}
                    ],
                    "correction": "Le **Comptage à Voix Haute** est essentiel pour la transparence de l'opération."
                },
                {
                    "questionNumber": 86,
                    "question": "Que doit-on faire si un client paye avec un **gros billet** (ex : $100 €$) pour un petit achat ?",
                    "answerOptions": [
                        {"text": "Refuser le billet.", "isCorrect": False},
                        {"text": "Vérifier l'authenticité du billet (stylo, lampe UV, toucher), puis rendre la monnaie si le fonds de caisse le permet (avec validation du responsable si besoin).", "isCorrect": True},
                        {"text": "Ne pas le vérifier.", "isCorrect": False},
                        {"text": "Le déchirer.", "isCorrect": False}
                    ],
                    "correction": "La **Vérification** est cruciale contre les faux-monnayeurs."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est le rôle du **Sac de Caisse** (ou jeté de caisse) ?",
                    "answerOptions": [
                        {"text": "Transporter les courses.", "isCorrect": False},
                        {"text": "Remplacer le fond de caisse.", "isCorrect": False},
                        {"text": "Retirer les gros billets du tiroir-caisse régulièrement (et les mettre sous surveillance) pour minimiser le risque de vol ou d'agression et faciliter le comptage final.", "isCorrect": True},
                        {"text": "Stocker les chèques.", "isCorrect": False}
                    ],
                    "correction": "Le **Sac de Caisse** ou la 'tirette' sert à sécuriser les grosses sommes d'argent."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'une **erreur de caisse** (trop-perçu ou manque) ?",
                    "answerOptions": [
                        {"text": "Le client n'a pas aimé le produit.", "isCorrect": False},
                        {"text": "Une différence entre le montant réel de la recette (comptage physique) et le montant théorique enregistré par la machine (Journal de caisse).", "isCorrect": True},
                        {"text": "Un problème technique.", "isCorrect": False},
                        {"text": "Une erreur de prix.", "isCorrect": False}
                    ],
                    "correction": "L'**Erreur de Caisse** reflète souvent une erreur de monnaie ou de saisie."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelles sont les deux principales missions de l'équipier polyvalent du commerce, au-delà de la caisse et du rayon ?",
                    "answerOptions": [
                        {"text": "La gestion du budget et l'embauche.", "isCorrect": False},
                        {"text": "L'**Entretien (ménage)** du point de vente (sols, vitrines, matériel) et la **Gestion des déchets/cartons** (tri sélectif, compactage).", "isCorrect": True},
                        {"text": "La décoration et la publicité.", "isCorrect": False},
                        {"text": "Le transport et la logistique.", "isCorrect": False}
                    ],
                    "correction": "La **Polyvalence** inclut la propreté et la gestion des déchets."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le rôle du **Ticket Annulateur** ou 'Ticket Z' de la caisse ?",
                    "answerOptions": [
                        {"text": "Rendre la monnaie.", "isCorrect": False},
                        {"text": "Récapituler toutes les opérations de la journée (ventes, annulations, erreurs) et servir de base au décompte final (il 'arrête' la caisse pour la journée fiscale).", "isCorrect": True},
                        {"text": "Imprimer un reçu.", "isCorrect": False},
                        {"text": "Vérifier un code-barres.", "isCorrect": False}
                    ],
                    "correction": "Le **Ticket Z** est un document comptable et fiscal essentiel."
                },
                {
                    "questionNumber": 91,
                    "question": "Que doit-on faire si un client souhaite payer avec un **chèque** (s'ils sont acceptés) ?",
                    "answerOptions": [
                        {"text": "L'accepter sans vérification.", "isCorrect": False},
                        {"text": "Vérifier l'identité du client (carte d'identité), s'assurer que le montant est correctement écrit (en toutes lettres et en chiffres) et que le chèque est signé au nom du tireur.", "isCorrect": True},
                        {"text": "Lui demander son numéro de téléphone.", "isCorrect": False},
                        {"text": "Le refuser.", "isCorrect": False}
                    ],
                    "correction": "La **Vérification d'Identité** est essentielle pour prévenir les chèques volés ou sans provision."
                },
                {
                    "questionNumber": 92,
                    "question": "Pourquoi doit-on effectuer le **tri des déchets** (cartons, plastiques, palettes) à la réserve ?",
                    "answerOptions": [
                        {"text": "Pour cacher les produits.", "isCorrect": False},
                        {"text": "Pour respecter les obligations légales (environnementales), minimiser les coûts de traitement des déchets et contribuer au recyclage.", "isCorrect": True},
                        {"text": "Pour gagner du temps.", "isCorrect": False},
                        {"text": "Pour faire joli.", "isCorrect": False}
                    ],
                    "correction": "Le **Tri Sélectif** est une norme environnementale et économique."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le principal risque de ne pas avoir une caisse bien rangée (pièces/billets mélangés) ?",
                    "answerOptions": [
                        {"text": "Le vol.", "isCorrect": False},
                        {"text": "L'augmentation des Erreurs de caisse (manque ou trop-perçu) et la perte de temps pour rendre la monnaie (ralentissement du flux client).", "isCorrect": True},
                        {"text": "La panne de la machine.", "isCorrect": False},
                        {"text": "L'insatisfaction du client.", "isCorrect": False}
                    ],
                    "correction": "L'**Organisation** du poste de travail est la clé de l'efficacité."
                },
                {
                    "questionNumber": 94,
                    "question": "Qu'est-ce qu'une **Ouverture de Caisse (saisie négative)** ?",
                    "answerOptions": [
                        {"text": "Un remboursement client (produit retourné).", "isCorrect": True},
                        {"text": "Un achat de produit.", "isCorrect": False},
                        {"text": "Une erreur de prix.", "isCorrect": False},
                        {"text": "Un dépôt de monnaie.", "isCorrect": False}
                    ],
                    "correction": "Une **Ouverture de Caisse** (ou **Remboursement**) est un retrait d'argent du tiroir."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est l'importance de faire un **briefing** (réunion rapide) avant l'ouverture du magasin ?",
                    "answerOptions": [
                        {"text": "Perdre du temps.", "isCorrect": False},
                        {"text": "Transmettre les objectifs du jour (CA à atteindre), les promotions et nouveautés, et attribuer les tâches (missions de la journée).", "isCorrect": True},
                        {"text": "Parler de la météo.", "isCorrect": False},
                        {"text": "Compter le stock.", "isCorrect": False}
                    ],
                    "correction": "Le **Briefing** permet de s'aligner sur les priorités commerciales et opérationnelles."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est le rôle du **Scanner-Détacheur** au niveau du poste de caisse ?",
                    "answerOptions": [
                        {"text": "Imprimer le ticket.", "isCorrect": False},
                        {"text": "Désactiver les étiquettes anti-vol magnétiques pour éviter que le portique ne sonne à la sortie (et scanner le produit en même temps).", "isCorrect": True},
                        {"text": "Vérifier les prix.", "isCorrect": False},
                        {"text": "Compter la monnaie.", "isCorrect": False}
                    ],
                    "correction": "Le **Scanner-Détacheur** est l'outil d'annulation de la protection anti-vol."
                },
                {
                    "questionNumber": 97,
                    "question": "Que doit-on faire si un client oublie un article payé en caisse (ex : sac de course lourd) ?",
                    "answerOptions": [
                        {"text": "Le garder pour soi.", "isCorrect": False},
                        {"text": "Le mettre immédiatement de côté (avec le ticket de caisse) dans un endroit sécurisé et tenter de le contacter ou attendre son retour (Procédure des objets trouvés).", "isCorrect": True},
                        {"text": "Le donner au client suivant.", "isCorrect": False},
                        {"text": "Le remettre en rayon.", "isCorrect": False}
                    ],
                    "correction": "La **Confiance** est essentielle : le produit payé doit être restitué au client."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le rôle d'une **fiche technique produit** ?",
                    "answerOptions": [
                        {"text": "Indiquer le prix.", "isCorrect": False},
                        {"text": "Fournir les informations précises sur la composition, l'origine, les dimensions, les conditions d'utilisation et les garanties du produit (aide à la vente).", "isCorrect": True},
                        {"text": "Ranger le produit.", "isCorrect": False},
                        {"text": "Vérifier le stock.", "isCorrect": False}
                    ],
                    "correction": "La **Fiche Technique** est l'outil de connaissance produit du vendeur."
                },
                {
                    "questionNumber": 99,
                    "question": "Qu'est-ce qu'une **opération d'inventaire tournant** ?",
                    "answerOptions": [
                        {"text": "Un inventaire annuel.", "isCorrect": False},
                        {"text": "Un comptage régulier (quotidien, hebdomadaire) d'une sélection de produits précis (à forte valeur ou forte rotation) pour maintenir une fiabilité du stock tout au long de l'année.", "isCorrect": True},
                        {"text": "Un inventaire des clients.", "isCorrect": False},
                        {"text": "Un inventaire des employés.", "isCorrect": False}
                    ],
                    "correction": "L'**Inventaire Tournant** est une alternative à l'inventaire annuel pour les produits clés."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la principale qualité requise pour un Équipier Polyvalent du Commerce travaillant en caisse ?",
                    "answerOptions": [
                        {"text": "La force physique.", "isCorrect": False},
                        {"text": "Le sens de l'accueil, la rapidité, la rigueur dans le comptage et la capacité à gérer le stress et la file d'attente.", "isCorrect": True},
                        {"text": "Le sens de l'orientation.", "isCorrect": False},
                        {"text": "La connaissance des langues étrangères.", "isCorrect": False}
                    ],
                    "correction": "La **Rigueur** et l'**Amabilité** sont essentielles au poste de caisse."
                },
            ]
        }
    }
}