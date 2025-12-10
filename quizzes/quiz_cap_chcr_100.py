quiz_data = {
    "title": "CAP Commercialisation et Services en Hôtel-Café-Restaurant (CSHCR) - Base de Données Complète (100 Questions) - Corrigée V1",
    
    "description": "Base de données de 100 questions pour le CAP CSHCR. Les longueurs des réponses ont été uniformisées pour éviter tout biais lors d'un test.",
    
    "themes": {
        # THÈME 1
        1: {
            "name": "Hygiène, Sécurité, Environnement (HSE) et Législation (HACCP)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la 'zone de danger' (ou 'Temperature Danger Zone - TDZ') où la prolifération des bactéries est maximale en cuisine ?",
                    "answerOptions": [
                        {"text": "La zone des températures positives : entre +15°C et +20°C (température ambiante) pour le pointage des pâtes.", "isCorrect": False, "key": "A"},
                        {"text": "La zone comprise entre +8°C et +63°C, qui favorise la multiplication rapide des micro-organismes (toxines) dans les aliments.", "isCorrect": True, "key": "B"},
                        {"text": "La zone des très hautes températures (supérieure à +100°C), pour la stérilisation (appertisation).", "isCorrect": False, "key": "C"},
                        {"text": "La zone des températures négatives : entre -5°C et -18°C (congélation) pour la conservation longue durée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les aliments doivent être maintenus à une température inférieure à 8°C (réfrigération) ou supérieure à 63°C (maintien au chaud)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la température maximale de conservation des produits 'Très Périssables' (viandes, poissons, produits laitiers) en enceinte froide ?",
                    "answerOptions": [
                        {"text": "Une température de conservation de +4°C maximum (réglementation européenne pour les produits sensibles).", "isCorrect": True, "key": "A"},
                        {"text": "La zone des températures positives : entre +15°C et +20°C (température ambiante) pour le stockage des œufs frais.", "isCorrect": False, "key": "B"},
                        {"text": "La zone des très hautes températures (supérieure à +100°C), pour la stérilisation (appertisation).", "isCorrect": False, "key": "C"},
                        {"text": "Une température de conservation de -18°C pour les produits frais (faux, c'est pour la congélation ou surgélation).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les produits très périssables sont généralement conservés à +4°C maximum. La viande hachée est à +2°C maximum."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la principale mesure d'hygiène à respecter avant de prendre son poste en salle ou en cuisine ?",
                    "answerOptions": [
                        {"text": "Se laver et se désinfecter les mains de manière rigoureuse (procédure de lavage) et enfiler la tenue de travail propre.", "isCorrect": True, "key": "A"},
                        {"text": "Vérifier la température du four pour s'assurer que les produits seront enfournés à chaud dans la zone de danger (faux).", "isCorrect": False, "key": "B"},
                        {"text": "Protéger les vitres, les pièces en plastique/caoutchouc et les réservoirs d'essence à proximité des étincelles (faux).", "isCorrect": False, "key": "C"},
                        {"text": "S'assurer que l'eau utilisée pour le pétrissage est à une température maximale de 10°C (faux, concerne la boulangerie).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le lavage des mains et la tenue propre sont les 'Points Critiques pour la Maîtrise' (CCP) de l'hygiène personnelle."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la procédure correcte pour la gestion des Huiles Alimentaires Usagées (HAU) après une friture ?",
                    "answerOptions": [
                        {"text": "Les jeter directement dans les poubelles (ordures ménagères) sans possibilité de réutilisation (interdit).", "isCorrect": False, "key": "A"},
                        {"text": "Les stocker séparément, identifier la nature du déchet et les confier à des entreprises spécialisées (collecte et recyclage).", "isCorrect": True, "key": "B"},
                        {"text": "Les recongeler pour une revente ultérieure à un prix réduit dans les prochaines 48 heures (interdit).", "isCorrect": False, "key": "C"},
                        {"text": "Les réintroduire (une partie) dans la prochaine fournée de pâte fraîche (interdit).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les HAU sont un déchet polluant. Leur recyclage (biocarburant) est soumis à une réglementation environnementale stricte."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le risque lié à la présence de bijoux (bagues, bracelets) ou de montres sur l'opérateur en cuisine ou en salle ?",
                    "answerOptions": [
                        {"text": "Le risque de corrosion accélérée des pièces métalliques du hachoir et du poussoir (acidité des bijoux).", "isCorrect": False, "key": "A"},
                        {"text": "La rupture de la chaîne du froid dans le réfrigérateur suite au choc thermique (faux).", "isCorrect": False, "key": "B"},
                        {"text": "Le risque de contamination microbienne (nids à bactéries) et de contamination physique (chute du bijou dans l'assiette).", "isCorrect": True, "key": "C"},
                        {"text": "L'augmentation rapide de la viscosité de la pâte lors de l'incorporation de la lécithine (émulsifiant).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les bijoux (particulièrement les bagues) sont interdits en cuisine et souvent fortement déconseillés en salle (réglementation)."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le risque de remettre une préparation chaude directement au réfrigérateur (grand volume) sans refroidissement rapide ?",
                    "answerOptions": [
                        {"text": "L'augmentation excessive du taux d'humidité de la pâte en cours de préparation (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de 'remontée en température' des autres aliments stockés (rupture de la chaîne du froid) et de prolifération bactérienne.", "isCorrect": True, "key": "B"},
                        {"text": "Le risque de prolifération d'organismes thermophiles sur le pain cuit (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La corrosion accélérée des pièces métalliques du pétrin et du fournil (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le refroidissement doit être rapide (de +63°C à +10°C en moins de deux heures) à l'aide d'une cellule de refroidissement (blast chiller)."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est l'importance du 'sens de la marche' (flux en avant) dans l'organisation du restaurant et de la cuisine (HACCP) ?",
                    "answerOptions": [
                        {"text": "Garantir l'image de marque de la boutique, sans aucun lien avec l'hygiène alimentaire (HACCP).", "isCorrect": False, "key": "A"},
                        {"text": "Éviter la contamination croisée en séparant les zones 'sales' (matières premières/déchets) des zones 'propres' (produit fini/service).", "isCorrect": True, "key": "B"},
                        {"text": "Assurer uniquement la protection contre les brûlures des mains et des avant-bras de l'opérateur (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Permettre au boulanger de travailler sans être soumis aux variations de température du fournil (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le produit doit toujours avancer dans le processus (de la réception au service), sans jamais croiser les flux de déchets ou de vaisselle sale."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est le danger principal pour le personnel de salle lié à la manipulation de poids lourds (caisse de bouteilles, pile d'assiettes) ?",
                    "answerOptions": [
                        {"text": "Le risque d'intoxication aux poussières de farine dues à une rupture du sac lors du transport (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de Troubles Musculo-Squelettiques (TMS), notamment le mal de dos (lumbago, hernie) ou les douleurs articulaires.", "isCorrect": True, "key": "B"},
                        {"text": "Le risque de brûlure chimique sur la peau lors de l'incorporation de la farine dans le pétrin (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le risque d'explosion (ATEX) en cas de choc du sac sur le sol du laboratoire (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le port de charges lourdes doit être sécurisé (chariot, dos droit) pour prévenir les maladies professionnelles (TMS)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le risque si l'on ne nettoie pas correctement les plans de travail ou le matériel (couteaux, assiettes) entre deux utilisations ?",
                    "answerOptions": [
                        {"text": "La diminution du temps de pétrissage pour la deuxième pâte (gain de temps, faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de contamination croisée entre un allergène (fruits à coque) et une autre préparation (risque client).", "isCorrect": True, "key": "B"},
                        {"text": "La contamination des fonds de peinture ou de la cabine, entraînant des défauts (poussières, cratères, faux).", "isCorrect": False, "key": "C"},
                        {"text": "L'altération des propriétés de la levure par contact avec l'eau froide (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gestion des allergènes (gluten, œufs, lait, fruits à coque) est obligatoire. Elle passe par un nettoyage et une désinfection stricts."
                },
                {
                    "questionNumber": 10,
                    "question": "Que signifie la 'DLUO' (Date Limite d'Utilisation Optimale) sur un ingrédient non périssable (épices séchées) ?",
                    "answerOptions": [
                        {"text": "Elle indique la date après laquelle l'ingrédient ne peut plus être consommé (danger bactériologique).", "isCorrect": False, "key": "A"},
                        {"text": "Elle indique la date après laquelle les qualités organoleptiques (goût, arôme, texture) ne sont plus garanties (sans risque sanitaire immédiat).", "isCorrect": True, "key": "B"},
                        {"text": "Elle indique la température maximale de conservation pour l'ingrédient (+4°C).", "isCorrect": False, "key": "C"},
                        {"text": "Elle indique la zone de danger bactériologique (entre +8°C et +63°C).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La DLUO (remplacée par le DDM : Date de Durabilité Minimale) n'est pas une date limite de consommation (DLC) sanitaire."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le document obligatoire qui décrit toutes les mesures prises par l'établissement pour assurer l'hygiène et la sécurité des aliments ?",
                    "answerOptions": [
                        {"text": "La 'Fiche Technique de Vente' (FTV) qui détaille l'argumentaire client (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Plan de Maîtrise Sanitaire' (PMS) qui inclut les procédures HACCP, de traçabilité et de nettoyage.", "isCorrect": True, "key": "B"},
                        {"text": "Le 'Bilan de Compétences' du personnel de cuisine (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le 'Rapport de Mise en Conformité' du matériel électrique (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le PMS (basé sur l'HACCP) est un document obligatoire qui rassemble toutes les procédures de l'entreprise (hygiène, contrôles, traçabilité)."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment doit-on gérer un produit ayant atteint sa Date Limite de Consommation (DLC) ?",
                    "answerOptions": [
                        {"text": "Le remettre immédiatement en rayon avec une réduction de prix pour éviter la perte (interdit).", "isCorrect": False, "key": "A"},
                        {"text": "Le retirer immédiatement de la vente, le détruire ou le jeter (risque sanitaire avéré).", "isCorrect": True, "key": "B"},
                        {"text": "Le stocker dans une zone sèche (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le recongeler pour prolonger sa durée de vie (interdit).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La DLC est la date après laquelle l'aliment est considéré comme dangereux (risques sanitaires). Le produit doit être impérativement retiré."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est l'attitude à adopter en cas de coupure (blessure) légère sur un poste de travail en cuisine ou en salle ?",
                    "answerOptions": [
                        {"text": "Continuer le service ou la préparation après avoir essuyé la coupure (risque de contamination immédiat).", "isCorrect": False, "key": "A"},
                        {"text": "Nettoyer, désinfecter la plaie et la recouvrir d'un pansement étanche de couleur vive (bleu) pour être visible.", "isCorrect": True, "key": "B"},
                        {"text": "Appliquer de la farine pour stopper le saignement (méthode de grand-mère non hygiénique).", "isCorrect": False, "key": "C"},
                        {"text": "Démissionner sur le champ (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le pansement étanche de couleur vive (souvent bleu en cuisine) est obligatoire pour signaler la présence d'une blessure et éviter la contamination des aliments."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le risque de contamination des aliments si un employé est malade (rhume, gastro-entérite) ?",
                    "answerOptions": [
                        {"text": "Le risque de 'remontée en température' des autres aliments stockés (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque de contamination par voie directe (postillons) ou indirecte (mains) et de propagation de l'infection aux clients.", "isCorrect": True, "key": "B"},
                        {"text": "La corrosion accélérée des pièces métalliques du pétrin (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La diminution du taux de cendres (T) de la farine utilisée (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'employé malade doit signaler son état et, si nécessaire, être affecté à un poste sans contact avec les aliments (ou se reposer)."
                },
                {
                    "questionNumber": 15,
                    "question": "Que doit-on faire si l'on constate une infestation de nuisibles (rongeurs, insectes) dans la zone de stockage des ingrédients ?",
                    "answerOptions": [
                        {"text": "Augmenter la température du fournil pour chasser les nuisibles par la chaleur excessive (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Contacter immédiatement une entreprise de lutte antiparasitaire et jeter toutes les marchandises contaminées (risque sanitaire).", "isCorrect": True, "key": "B"},
                        {"text": "Ajouter plus de sel dans la pâte pour désinfecter la farine contaminée par les excréments (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Les laisser pour la fin de la production, car le four brûlera tous les corps étrangers (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les nuisibles sont des vecteurs de maladies (Salmonella). Les produits contaminés doivent être détruits. La dératisation est vitale."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est l'objectif principal de la 'traçabilité' des produits alimentaires (ticket, fiche de production) ?",
                    "answerOptions": [
                        {"text": "Assurer la sécurité du véhicule pour l'utilisateur et la conformité avec la réglementation routière (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Permettre d'identifier l'origine des matières, la date de fabrication, le numéro de lot et la DLC (en cas de rappel produit).", "isCorrect": True, "key": "B"},
                        {"text": "Ajouter un additif (émulsifiant) dans la pâte pour neutraliser le corps étranger (sans effet, faux).", "isCorrect": False, "key": "C"},
                        {"text": "Mesurer la teneur en gluten (W) de la farine utilisée pour le pétrissage (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La traçabilité est la capacité de retrouver l'historique d'un produit (du champ à l'assiette) et elle est obligatoire (sécurité)."
                },
                {
                    "questionNumber": 17,
                    "question": "Que doit-on faire si l'on constate une différence de température anormale dans une chambre froide (+10°C) ?",
                    "answerOptions": [
                        {"text": "Laisser la porte ouverte pour aérer (mauvaise solution).", "isCorrect": False, "key": "A"},
                        {"text": "Isoler les aliments, alerter la maintenance et enregistrer la rupture de la chaîne du froid sur le registre (action corrective).", "isCorrect": True, "key": "B"},
                        {"text": "Couper immédiatement le courant pour économiser l'énergie (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Ne rien faire et attendre que la température redescende seule (risqué).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Une rupture de la chaîne du froid (> +8°C) est un CCP. Les aliments doivent être jetés (si la durée est trop longue) ou isolés (si courte)."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le risque si un produit (plat cuisiné) est maintenu au chaud en dessous de 63°C pendant une longue durée ?",
                    "answerOptions": [
                        {"text": "Le risque d'intoxication alimentaire (Salmonella, Listeria) due à la multiplication rapide des bactéries dans la 'zone de danger'.", "isCorrect": True, "key": "A"},
                        {"text": "Le risque de 'brûlure' des micro-organismes (faux).", "isCorrect": False, "key": "B"},
                        {"text": "La diminution du temps de pétrissage pour la deuxième pâte (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La zone des températures ambiantes (entre +15°C et +20°C) pour le stockage (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le maintien au chaud (CCP) doit être supérieur à 63°C pour garantir la sécurité. La durée maximale est réglementée (souvent 4 heures)."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le rôle du 'Désinfectant' (biocide) dans le protocole de nettoyage-désinfection ?",
                    "answerOptions": [
                        {"text": "Il sert uniquement à enlever la saleté visible (débris alimentaires, graisse).", "isCorrect": False, "key": "A"},
                        {"text": "Il détruit les micro-organismes (bactéries, virus, levures) qui restent après le nettoyage (action chimique).", "isCorrect": True, "key": "B"},
                        {"text": "Il sert d'agent de blanchiment de la mie du pain (aspect très blanc, faux).", "isCorrect": False, "key": "C"},
                        {"text": "Il augmente la viscosité de la pâte lors de l'incorporation de la lécithine (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le protocole 'Nettoyage-Désinfection' est la base de l'HACCP pour éliminer les résidus (nettoyage) et les micro-organismes (désinfection)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est l'attitude à adopter par le personnel de salle en cas d'incendie dans l'établissement ?",
                    "answerOptions": [
                        {"text": "Tenter d'éteindre le feu par ses propres moyens (sauf feu naissant maîtrisé) sans alerter (mauvais).", "isCorrect": False, "key": "A"},
                        {"text": "Alerter, couper les énergies (si possible), évacuer les clients et le personnel vers le point de rassemblement, sans paniquer (PSSI).", "isCorrect": True, "key": "B"},
                        {"text": "Courir chercher un verre d'eau pour éteindre le feu sur une friteuse (dangereux).", "isCorrect": False, "key": "C"},
                        {"text": "Continuer le service en attendant l'arrivée des secours (dangereux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Plan de Sécurité et de Sûreté Incendie (PSSI) doit être maîtrisé : priorité à l'alerte et à l'évacuation des personnes."
                }
            ]
        },
        # THÈME 2
        2: {
            "name": "Techniques de Service en Restauration et Boissons",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le principe du 'Service à la Française' pour un plat (mise en place) ?",
                    "answerOptions": [
                        {"text": "Le client se sert lui-même directement dans le plat de présentation (présenté à gauche), à l'aide de couverts de service.", "isCorrect": True, "key": "A"},
                        {"text": "Le serveur apporte l'assiette dressée de la cuisine et la dépose devant le client (service le plus rapide).", "isCorrect": False, "key": "B"},
                        {"text": "Le serveur effectue la découpe ou le flambage devant le client à l'aide d'un chariot de service (guéridon).", "isCorrect": False, "key": "C"},
                        {"text": "Le serveur sert le client directement à la cuillère et à la fourchette, sans que le client ne touche le plat (service le plus formel).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Service à la Française (présentation du plat) est peu utilisé en restaurant, mais plus pour les buffets ou les plats familiaux (convivialité)."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est le côté de service et de desserte (débarrassage) conventionnel pour le plat principal du client ?",
                    "answerOptions": [
                        {"text": "Le service se fait toujours à gauche du client, et la desserte se fait toujours à droite du client (selon la convention classique).", "isCorrect": False, "key": "A"},
                        {"text": "Le service (plat, assiette, sauce) se fait toujours à droite du client, et la desserte (assiette sale) se fait toujours à droite.", "isCorrect": True, "key": "B"},
                        {"text": "Le service (plat, assiette, sauce) se fait toujours à gauche du client, et la desserte se fait toujours à droite.", "isCorrect": False, "key": "C"},
                        {"text": "Le service se fait toujours en face du client (service au passe), et la desserte se fait toujours à gauche.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La convention classique est : service à droite (plat) et desserte à droite (assiette sale). Exceptions : service à la française et pain (gauche)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le rôle du 'sommelier' ou du personnel en charge du service du vin ?",
                    "answerOptions": [
                        {"text": "Resserrer le réseau de gluten (ténacité) et incorporer l'air (pour le volume) lors du pétrissage intensif (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Conseiller le client sur les accords mets et vins, prendre la commande, préparer le vin (chambrer/rafraîchir) et le servir (dégustation).", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer l'activité des bactéries lactiques pour obtenir une pâte plus acide et aromatique (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le sommelier est le garant de la cave, de l'accord mets et vins, et de la bonne exécution du service du vin (température, verrerie)."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on le fait de servir le plat (viande, poisson) à l'aide d'une cuillère et d'une fourchette (servies à la main) ?",
                    "answerOptions": [
                        {"text": "Le service à la russe (ou au plat) : le serveur prend l'aliment du plat de service et le dépose sur l'assiette du client.", "isCorrect": False, "key": "A"},
                        {"text": "Le service à l'anglaise (ou 'à la cuillère') : le serveur effectue le service directement de la cuillère à la fourchette (à gauche du client).", "isCorrect": True, "key": "B"},
                        {"text": "Le service à la française (le client se sert lui-même) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le service au guéridon (le serveur découpe devant le client) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Service à l'Anglaise est le service le plus formel et le plus technique. Il est effectué à la gauche du client."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le rôle du 'Guéridon' dans le service en salle (service haut de gamme) ?",
                    "answerOptions": [
                        {"text": "Contrôler la déchirure de la croûte pendant la cuisson (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Il sert de table d'appoint ou de poste de travail pour les préparations devant le client (découpe, flambage, préparation de salades).", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer l'activité de la levure et augmenter la production d'acide lactique (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le guéridon (petite table mobile) est essentiel pour les services de 'show cooking' (démonstration) qui nécessitent des gestes techniques."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est l'élément qui permet de 'refroidir' une bouteille de vin blanc ou de Champagne en salle ?",
                    "answerOptions": [
                        {"text": "Un bain-marie (eau chaude) pour maintenir la température (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le seau à glace (ou seau à vin) rempli d'eau et de glace, et une serviette (liteau) pour le service (température idéale).", "isCorrect": True, "key": "B"},
                        {"text": "Le congélateur (dangereux, casse le vin) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le four à convection (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le seau à glace (avec eau) est le moyen le plus rapide et le plus élégant pour maintenir la température de service des vins blancs et mousseux."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le nom de la serviette (en tissu ou en coton) utilisée par le serveur pour le service du vin ou le transport de plats chauds ?",
                    "answerOptions": [
                        {"text": "Le liteau (serviette de service) pour porter les assiettes chaudes et essuyer les bouteilles (propreté).", "isCorrect": True, "key": "A"},
                        {"text": "Le torchon (chiffon) utilisé pour le nettoyage des sols (jamais pour le service, contamination).", "isCorrect": False, "key": "B"},
                        {"text": "La serviette de table (napperon) du client (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le tablier de cuisine (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le liteau est l'outil indispensable du serveur (port des assiettes chaudes, essuyage, présentation des vins, etc.)."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment appelle-t-on le fait de 'décanter' (ou carafer) un vin rouge ancien (en cave) ?",
                    "answerOptions": [
                        {"text": "Il active la levure et accélère la fermentation (faux).", "isCorrect": False, "key": "A"},
                        {"text": "C'est l'action de transvaser le vin dans une carafe pour le séparer de son dépôt (lie) et l'aérer légèrement (développement des arômes).", "isCorrect": True, "key": "B"},
                        {"text": "Il sert d'agent de blanchiment de la mie du pain (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Il sert uniquement à colorer la croûte du pain lors de la cuisson finale (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La décantation (dans une carafe étroite) est utilisée pour les vieux vins (dépôts). L'aération (dans une carafe large) est pour les vins jeunes."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le rôle du 'Ménage de service' (poivre, sel, moutarde, huile/vinaigre) dans le dressage de la table ?",
                    "answerOptions": [
                        {"text": "Elle assouplit la pâte, augmente le volume du produit et améliore la saveur (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Il permet au client d'ajuster l'assaisonnement du plat à son goût (personnalisation) ou d'accompagner certains plats (salades).", "isCorrect": True, "key": "B"},
                        {"text": "Elle rend la pâte trop ferme (ténace) et difficile à travailler au laminoir (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Elle sert uniquement à colorer la mie du produit (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le ménage (set de condiments) doit être propre et complet avant le service. Il doit être retiré après le plat principal (sauf demande)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le nom du couvert de service (souvent en bois ou en plastique) utilisé pour servir le pain aux clients ?",
                    "answerOptions": [
                        {"text": "Les pinces à pain (ou pince de service) pour éviter tout contact direct des mains avec l'aliment (hygiène).", "isCorrect": True, "key": "A"},
                        {"text": "Le poussoir hydraulique (ou à manivelle) pour introduire la farce sous pression (faux).", "isCorrect": False, "key": "B"},
                        {"text": "L'amylase, qui transforme l'amidon en sucres (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le colorant (curcuma) pour donner une couleur jaune à la mie des pains spéciaux (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'hygiène des mains est primordiale. Les pinces sont obligatoires pour le service du pain (au lieu des doigts)."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est l'ordre chronologique des plats (service classique) lors d'un repas complet ?",
                    "answerOptions": [
                        {"text": "Plat Principal, Dessert, Entrée, Boissons (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Potage, Entrée (froide/chaude), Poisson, Viande, Fromage, Dessert (ordre classique).", "isCorrect": True, "key": "B"},
                        {"text": "Fromage, Entrée, Dessert, Viande (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Dessert, Potage, Entrée, Plat Principal (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'ordre des plats est codifié. Il vise une progression gustative (léger au lourd) et une logique de service."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est la principale difficulté lors du 'Service au Plateau' (plateaux chauds ou froids) ?",
                    "answerOptions": [
                        {"text": "Elle dégrade l'amidon en sucres simples (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le maintien de l'équilibre et du poids du plateau (force, bras tendu) et la gestion de la température (choc thermique).", "isCorrect": True, "key": "B"},
                        {"text": "Elle régule l'acidité (pH) de la pâte et assure la bonne conservation du produit fini (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Elle sert uniquement à blanchir la mie du pain et à réduire l'activité des lactobacilles (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le service au plateau nécessite de la force, de l'équilibre, de la coordination et le port d'un liteau (sécurité/hygiène)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le risque d'une 'prise de commande' (méthode manuelle) sans la répéter au client ?",
                    "answerOptions": [
                        {"text": "Elle rend la pâte plus ferme (ténace) et plus difficile à travailler (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le risque d'erreur dans la transmission (cuisine) ou de malentendu sur les accompagnements (perte de temps, mécontentement client).", "isCorrect": True, "key": "B"},
                        {"text": "Elle n'a aucun impact sur la pâte, mais elle accélère la corrosion des machines du fournil (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Elle diminue le taux de cendres de la farine (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La répétition de la commande permet de s'assurer de la bonne compréhension et de rassurer le client (professionnalisme)."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le rôle du 'Marquage' (ou 'Annonce') en cuisine (transmission de la commande) ?",
                    "answerOptions": [
                        {"text": "Il apporte une valeur nutritive, de la couleur, du liant et améliore la conservation du produit fini (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Il permet de lancer la préparation des plats (mise en route) et de synchroniser le service de la table (rapidité et qualité).", "isCorrect": True, "key": "B"},
                        {"text": "Il renforce le réseau de gluten (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Il sert d'agent de blanchiment de la mie du pain (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le marquage (annonce verbale ou bon de commande) est l'outil de communication entre la salle et la cuisine (efficacité)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le nom de l'élément de la table qui permet au client de nettoyer sa bouche (après le service du poisson par exemple) ?",
                    "answerOptions": [
                        {"text": "Le rince-doigts (ou bol d'eau tiède/citron) pour le nettoyage des mains (après crustacés, fruits de mer).", "isCorrect": False, "key": "A"},
                        {"text": "La panade (mélange de pain trempé ou de farine/lait/œuf) pour l'apport d'amidon (faux).", "isCorrect": False, "key": "B"},
                        {"text": "La serviette de table (ou napperon) en tissu, qui est changée entre les plats (hygiène).", "isCorrect": True, "key": "C"},
                        {"text": "La levure de surface (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La serviette de table est l'élément d'hygiène personnel du client. Elle est souvent repliée ou changée (haut de gamme)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le nom de la technique qui consiste à chauffer une bouteille de vin rouge pour le servir à température ambiante ('chambrer') ?",
                    "answerOptions": [
                        {"text": "L'étuvage (ou 'séchage') pour la maturation du produit avant le séchage final (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Chambrage' (montée lente en température) pour les vins rouges (température de service idéale : 16°C à 18°C).", "isCorrect": True, "key": "B"},
                        {"text": "Le pétrissage intensif (faux).", "isCorrect": False, "key": "C"},
                        {"text": "L'autolyse (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le chambrage (mettre à température) est essentiel pour le vin rouge (ouverture des arômes). Attention : la température ambiante de la salle est souvent trop chaude."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'outil indispensable (type de couteau) pour la découpe de la viande (ou d'un rôti) devant le client au guéridon ?",
                    "answerOptions": [
                        {"text": "Le couteau à pain (dentelé) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le couteau de tranche (ou 'tranchant') et la fourchette à découper, souvent accompagnés d'une planche à découper (technique).", "isCorrect": True, "key": "B"},
                        {"text": "Le coupe-ongle (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le ciseau de cuisine (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La découpe au guéridon est un 'show' technique qui nécessite un matériel adapté (couteau très aiguisé, planche, pinces)."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est le rôle du 'Remplissage des Verreries' (eau ou vin) lors du service à table ?",
                    "answerOptions": [
                        {"text": "Il sert de nourriture à la levure et participe à la coloration de la croûte (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Il s'agit d'assurer le service des boissons et de maintenir les verres à un niveau correct (entre le tiers et la moitié du verre).", "isCorrect": True, "key": "B"},
                        {"text": "Il ralentit la fermentation et augmente le taux de cendres de la farine (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Il sert uniquement à blanchir la mie du pain et à réduire l'activité des lactobacilles (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le serveur doit veiller à ce que les clients ne manquent de rien (eau, vin) sans trop remplir les verres (élégance)."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le nom de la technique qui consiste à cuire un dessert (crêpes Suzette) devant le client avec de l'alcool enflammé ?",
                    "answerOptions": [
                        {"text": "L'autolyse (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Flambage (cuisson/caramélisation) pour une expérience visuelle et gustative (service au guéridon).", "isCorrect": True, "key": "B"},
                        {"text": "Le bassinage (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le flambage (alcool chaud) est une technique spectaculaire qui nécessite une grande prudence et une maîtrise parfaite (sécurité)."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est l'objectif du 'Vérification de la satisfaction' (feedback) du client après le service du plat ?",
                    "answerOptions": [
                        {"text": "Le sucre freine l'activité de la levure (faux).", "isCorrect": False, "key": "A"},
                        {"text": "S'assurer que le client est satisfait (qualité du plat, température) et intercepter un problème avant qu'il ne devienne une réclamation (pro-activité).", "isCorrect": True, "key": "B"},
                        {"text": "Le sucre détruit les bactéries lactiques du levain (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le sucre rend la pâte plus ferme (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La vérification (discrète) est une étape de la relation client essentielle pour le service et la gestion des problèmes."
                }
            ]
        },
        # THÈME 3
        3: {
            "name": "Connaissance des Produits (Boissons, Vins, Aliments)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le principal cépage blanc utilisé pour la production des vins de la région de Bourgogne (Chablis, Montrachet) ?",
                    "answerOptions": [
                        {"text": "Le Pinot Noir, cépage rouge utilisé en Bourgogne (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Chardonnay, cépage blanc international par excellence (minéralité et finesse).", "isCorrect": True, "key": "B"},
                        {"text": "Le Cabernet Sauvignon, cépage rouge de Bordeaux (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le Merlot, cépage rouge de Bordeaux (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Chardonnay est le cépage roi de la Bourgogne pour les blancs, et le Pinot Noir est pour les rouges."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le nom de l'alcool (spiritueux) produit à partir de la canne à sucre (rhum) et utilisé dans de nombreux cocktails ?",
                    "answerOptions": [
                        {"text": "Le Whisky (céréales, malt) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Rhum (ou la cachaça au Brésil), issu de la fermentation et de la distillation du jus ou de la mélasse de canne à sucre.", "isCorrect": True, "key": "B"},
                        {"text": "La Tequila (agave) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le Gin (baies de genièvre) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Rhum (agricole ou traditionnel) est la base de nombreux cocktails (Mojito, Ti-Punch) et est produit dans les régions tropicales."
                },
                {
                    "questionNumber": 43,
                    "question": "Comment appelle-t-on le mode de cuisson de la viande qui consiste à la cuire lentement dans un liquide (fond, bouillon) après l'avoir saisie (marquée) ?",
                    "answerOptions": [
                        {"text": "Le rôtissage (cuisson au four à sec) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Braisage (cuisson lente à couvert, dans un fond aromatisé, pour des pièces peu tendres).", "isCorrect": True, "key": "B"},
                        {"text": "Le grillage (cuisson sur grille à feu vif) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le Pochage (cuisson dans un liquide à basse température) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Braisage (bœuf bourguignon, pot-au-feu) est une cuisson qui rend la viande moelleuse et le jus (sauce) concentré."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le nom du vin effervescent (Champagne) produit en France dans la région de la Champagne (méthode traditionnelle) ?",
                    "answerOptions": [
                        {"text": "Le Crémant (vin effervescent d'autres régions françaises) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Champagne (vin d'appellation d'origine contrôlée, AOC, produit selon la méthode Champenoise).", "isCorrect": True, "key": "B"},
                        {"text": "Le Prosecco (vin effervescent italien) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le Cava (vin effervescent espagnol) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Champagne est un vin de prestige (assemblage) qui est protégé par son AOC (région, méthode)."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le cépage rouge principal utilisé pour les vins de Bordeaux (Médoc, Pauillac, Saint-Estèphe) ?",
                    "answerOptions": [
                        {"text": "Le Gamay (cépage du Beaujolais) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Cabernet Sauvignon (tannins, structure), souvent assemblé au Merlot (rondeur, fruit).", "isCorrect": True, "key": "B"},
                        {"text": "Le Syrah (cépage de la Vallée du Rhône) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le Pinot Noir (cépage de la Bourgogne) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Cabernet Sauvignon domine les assemblages sur la rive gauche de Bordeaux. Le Merlot domine sur la rive droite (Saint-Émilion)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le nom de l'outil utilisé pour ouvrir une bouteille de vin (tire-bouchon) en service professionnel ?",
                    "answerOptions": [
                        {"text": "La vrille électrique (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Limonadier' (tire-bouchon à levier) qui intègre un couteau (coupe-capsule) et un décapsuleur.", "isCorrect": True, "key": "B"},
                        {"text": "Le pistolet à air chaud (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le marteau et le clou (dangereux) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le limonadier (ou sommelier) est l'outil indispensable. Il permet d'ouvrir le vin avec élégance et sans briser le bouchon."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le nom du produit (sauce) de base (roux + liquide) utilisé pour lier les sauces chaudes (Béchamel, Velouté) ?",
                    "answerOptions": [
                        {"text": "La Vinaigrette (sauce froide) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Roux (mélange de beurre et de farine) qui sert d'agent de liaison pour les liquides (amidon).", "isCorrect": True, "key": "B"},
                        {"text": "La Mayonnaise (émulsion) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le Coulis (jus de fruits ou de légumes) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Roux (blanc, blond ou brun) est la base de l'épaississement des sauces chaudes classiques (cuisine française)."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'accompagnement (légume) classique de la viande de gibier (cerf, sanglier, lièvre) en saison ?",
                    "answerOptions": [
                        {"text": "Les frites (plus pour le steak ou les moules) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La purée de céleri, les champignons des bois, la sauce grand veneur (épicée et fruitée).", "isCorrect": True, "key": "B"},
                        {"text": "Les pâtes à la carbonara (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le riz blanc (plus pour le poisson) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le gibier est une viande forte (chasse) qui est généralement accompagnée de saveurs terreuses, sucrées/acides (fruits rouges)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le nom du cépage blanc (très parfumé et aromatique) utilisé pour la production de vins secs dans la région de l'Alsace ?",
                    "answerOptions": [
                        {"text": "Le Merlot (rouge, faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le Gewurztraminer (cépage alsacien, épicé, lychee) ou le Riesling (sec, minéral).", "isCorrect": True, "key": "B"},
                        {"text": "Le Cabernet Franc (rouge, faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le Syrah (rouge, faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Alsace produit principalement des vins blancs (mono-cépages). Le Gewurztraminer est l'un des plus reconnaissables."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle est la principale différence entre le Café Expresso (court) et le Café Allongé (long) ?",
                    "answerOptions": [
                        {"text": "Le café allongé (lungo) est fait avec deux fois plus de mouture que l'espresso (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le café allongé est un espresso avec l'ajout d'eau chaude (moins concentré) ; l'espresso est très court et concentré.", "isCorrect": True, "key": "B"},
                        {"text": "L'espresso est moins cher que le café allongé (faux).", "isCorrect": False, "key": "C"},
                        {"text": "L'espresso est fait avec de la poudre de cacao (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Lungo (allongé) est un espresso dilué. Le Ristretto est un espresso encore plus court et plus concentré."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le nom du type de verre (verre à pied, tulipe) utilisé pour le service des vins effervescents (Champagne, Crémant) ?",
                    "answerOptions": [
                        {"text": "Le verre 'Ballon' (pour le Cognac ou l'Armagnac) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La Flûte (ou la coupe), qui permet de conserver les bulles (effervescence) et de sublimer le cordon (Bulles fines).", "isCorrect": True, "key": "B"},
                        {"text": "Le verre 'Tumbler' (pour les cocktails, les jus) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le verre à bière (choppe, pinte) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Flûte (ou I.T.T. : International Tasting Tulip) est le verre idéal pour la dégustation des vins mousseux."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est l'outil utilisé pour ouvrir les huîtres, les crustacés ou les coquillages (fruits de mer) ?",
                    "answerOptions": [
                        {"text": "La mandoline (pour la découpe des légumes) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le couteau à huîtres (lame courte et robuste) et le couteau à crustacés (pour les pinces).", "isCorrect": True, "key": "B"},
                        {"text": "La corne (ou raclette) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le banneton (pour la pousse des pains ronds) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'ouverture des huîtres (l'écaillage) est une technique délicate et dangereuse qui nécessite des EPI (gants, couteau adapté)."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le nom du processus d'assemblage des ingrédients (alcools, jus de fruits) pour créer une boisson mélangée ?",
                    "answerOptions": [
                        {"text": "Le collage structurel (méthode de soudure) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Mixage' (ou l'assemblage) pour la création de Cocktails ou de Long Drinks (équilibre des saveurs).", "isCorrect": True, "key": "B"},
                        {"text": "L'autolyse (repos de la farine et de l'eau) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le rafraîchi (pour le levain) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Barman (mixologue) est le professionnel en charge de l'assemblage (shaker, verre à mélange) et de la décoration des cocktails."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'impact d'une mauvaise 'température de service' sur un vin rouge (trop froid ou trop chaud) ?",
                    "answerOptions": [
                        {"text": "Le vin rouge trop froid (inférieur à 12°C) sera 'fermé' (arômes bloqués) ; trop chaud (supérieur à 20°C) sera 'lourd' (alcool dominant).", "isCorrect": True, "key": "A"},
                        {"text": "Le pain va s'étaler (faux).", "isCorrect": False, "key": "B"},
                        {"text": "La buée (vapeur) sera excessive (faux).", "isCorrect": False, "key": "C"},
                        {"text": "L'activité de la levure sera bloquée (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La température de service (14°C à 18°C pour les rouges) est cruciale pour l'expression des arômes et le plaisir de la dégustation."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le nom de la coupe (ou du plat) de service utilisé pour présenter une salade de fruits ou des glaces ?",
                    "answerOptions": [
                        {"text": "La marmite (pour la soupe) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Coupe' (à glace, ou à fruits), souvent sur pied, ou un petit bol (présentation du dessert).", "isCorrect": True, "key": "B"},
                        {"text": "La planche à découper (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le poêlon (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le choix du contenant (verrerie, céramique) est essentiel pour la mise en valeur esthétique du dessert."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le nom de l'assiette (petite) réservée au service du pain et du beurre (à la gauche du client) ?",
                    "answerOptions": [
                        {"text": "L'assiette de présentation (plus grande, sous l'assiette plate) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "L'assiette à pain (ou 'Moutardier'), souvent ronde ou carrée, placée en haut à gauche des couverts.", "isCorrect": True, "key": "B"},
                        {"text": "La soupière (pour le potage) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le plat de service (plus grand, pour le service à la russe) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'assiette à pain est un standard du dressage de la table pour le service du pain (au début du repas)."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment appelle-t-on l'action de 'découper et de servir' une volaille entière (canard, poulet) devant le client ?",
                    "answerOptions": [
                        {"text": "L'abaisse (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Tronçonnage' (ou la découpe) au guéridon, qui nécessite une grande maîtrise et un couteau adapté (couteau de tranche).", "isCorrect": True, "key": "B"},
                        {"text": "Le rafraîchi (pour le levain) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le chanfreinage (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le tronçonnage (découpe) est un service rare, réservé aux établissements de prestige (maîtrise des techniques de découpe)."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le but du 'Maintien au chaud' (bain-marie, vitrine chauffante) des plats traiteur (au-delà de 2 heures) ?",
                    "answerOptions": [
                        {"text": "Avoir une consistance (plasticité) similaire à celle de la pâte (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Maintenir impérativement la température à cœur du produit au-dessus de 63°C (hors zone de danger bactériologique).", "isCorrect": True, "key": "B"},
                        {"text": "Accélérer la production de gaz carbonique (CO₂) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le maintien au chaud (supérieur à 63°C) est un CCP pour la sécurité alimentaire. La durée maximale est réglementée (souvent 4 heures)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le nom de l'action qui consiste à 'servir une boisson' (bière, cocktail) sans débordement ni mousse excessive ?",
                    "answerOptions": [
                        {"text": "La dorure (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Tirage' (ou le service 'au fût') pour la bière, ou l'utilisation d'une cuillère (cocktails) pour éviter le mélange excessif.", "isCorrect": True, "key": "B"},
                        {"text": "La buée (vapeur d'eau) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage (première fermentation) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le tirage (bière pression) est une technique précise (angle du verre, pression, temps) pour une mousse idéale et un niveau correct."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle du 'Marquage des Couverts' (mise en place) avant l'arrivée du client ?",
                    "answerOptions": [
                        {"text": "Permettre au réseau de gluten de se relâcher (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le marquage des couverts correspond aux plats commandés : il sert à préparer la table pour les plats à venir (fluidité du service).", "isCorrect": True, "key": "B"},
                        {"text": "Ajouter du sel dans la pâte pour freiner la fermentation (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le marquage (couverts ajoutés) est un signe de service professionnel et de fluidité. Il est fait discrètement pendant le service."
                }
            ]
        },
        # THÈME 4
        4: {
            "name": "Techniques de Commercialisation, Vente et Communication Professionnelle",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le but de la 'Vente Additionnelle' (ou 'Upselling') en restauration (salle) ?",
                    "answerOptions": [
                        {"text": "Elle est très enrichie en œufs, en sucre et en matière grasse (faux).", "isCorrect": False, "key": "A"},
                        {"text": "C'est l'action de proposer des produits complémentaires (apéritif, vin, dessert, café) pour augmenter le panier moyen et le chiffre d'affaires.", "isCorrect": True, "key": "B"},
                        {"text": "Elle est très peu hydratée (moins de 50% d'eau) pour une conservation très longue (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Elle est fabriquée sans sel, pour un goût plus doux et un pétrissage très court (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La vente additionnelle (suggérer un dessert ou un vin) est une technique de commercialisation essentielle pour la rentabilité."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le rôle de 'l'Argumentaire de Vente' (salle) lors de la proposition d'un plat du jour ou d'une suggestion ?",
                    "answerOptions": [
                        {"text": "Le mastic polyester (bi-composant) pour combler les défauts de surface (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Présenter le plat avec passion (descriptions, ingrédients, mode de cuisson) pour susciter l'intérêt et déclencher l'achat (convaincre).", "isCorrect": True, "key": "B"},
                        {"text": "La farine de maïs (sans gluten) avec une poudre à lever (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La farine de blé (T150) avec une faible hydratation (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'argumentaire de vente doit être court, enthousiaste et se concentrer sur les avantages pour le client (goût, nouveauté)."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la principale caractéristique de 'l'Accueil' du client (première impression) dans l'établissement ?",
                    "answerOptions": [
                        {"text": "Il se conserve beaucoup plus longtemps (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Il doit être chaleureux, immédiat, avec un contact visuel et un sourire (professionnalisme, convivialité).", "isCorrect": True, "key": "B"},
                        {"text": "Il doit être consommé dans les 24 heures (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Il contient des additifs (conservateurs) qui prolongent sa durée de vie (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'accueil (le sourire, le bonjour, l'installation) est le premier point de contact qui détermine l'expérience du client."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est le rôle de la 'fiche de poste' (ou descriptif de fonction) pour le personnel de salle ?",
                    "answerOptions": [
                        {"text": "L'incorporation de la matière grasse (beurre de tourage) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Elle détaille les missions, les responsabilités, les horaires et les procédures à suivre (organisation et clarté).", "isCorrect": True, "key": "B"},
                        {"text": "L'utilisation de farine de seigle (T130) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La cuisson à haute température (plus de 300°C) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La fiche de poste clarifie les attentes. Elle est essentielle pour l'intégration et l'évaluation du personnel."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le but de 'suggérer le vin' au verre (vs la bouteille) lors du service à table ?",
                    "answerOptions": [
                        {"text": "La cuisson sur sole (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Proposer des accords mets et vins différents pour chaque plat et augmenter la rentabilité (marge sur le verre plus élevée).", "isCorrect": True, "key": "B"},
                        {"text": "La cuisson par injection de vapeur (buée) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le vin au verre permet au client de varier les plaisirs et à l'établissement de réaliser une marge plus importante."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le risque de sécher un saucisson sec (maturation) dans une pièce trop chaude et trop humide ?",
                    "answerOptions": [
                        {"text": "Elle n'utilise pas de levure ni de levain (faux).", "isCorrect": False, "key": "A"},
                        {"text": "L'écoute active du client, la prise en compte de l'insatisfaction (empathie) et la proposition rapide d'une solution (geste commercial).", "isCorrect": True, "key": "B"},
                        {"text": "Elle est fabriquée avec une farine de seigle (T130) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Elle nécessite un pétrissage très long (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gestion des réclamations est cruciale. L'écoute et la rapidité à trouver une solution sauvent la relation client."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est l'attitude à adopter par le personnel de salle pour 'vendre' un dessert après le plat principal ?",
                    "answerOptions": [
                        {"text": "Le risque de 'brûler' les micro-organismes (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Retirer les assiettes (débarrassage) puis présenter immédiatement la carte des desserts ou l'assiette du jour (visuel et tentation).", "isCorrect": True, "key": "B"},
                        {"text": "La diminution du taux de cendres (T) de la farine utilisée (faux).", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation de la force (W) de la farine de rafraîchi (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le dessert est une vente très rentable. La présentation visuelle (chariot, assiette de dégustation) est l'outil le plus efficace."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le rôle de la 'communication non verbale' (posture, gestes) du serveur en salle ?",
                    "answerOptions": [
                        {"text": "La peau d'orange (surface irrégulière) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Elle transmet la confiance, le professionnalisme, et l'attention sans avoir besoin de parler (regard, sourire, gestes calmes).", "isCorrect": True, "key": "B"},
                        {"text": "Le pain de seigle (T130) qui contient des pentosanes (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le pain complet (T150) qui nécessite un temps de pétrissage très long (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La communication non verbale est essentielle. Le serveur doit être attentif et disponible (regard) sans être envahissant."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le but d'utiliser des 'Formules de Politesse' (Monsieur, Madame) et un langage soutenu (voussoiement) avec le client ?",
                    "answerOptions": [
                        {"text": "La dorure (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Maintenir un niveau de professionnalisme et de respect, adapté au standing de l'établissement (image de marque).", "isCorrect": True, "key": "B"},
                        {"text": "La buée (vapeur d'eau) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage (première fermentation) en masse (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le voussoiement est la base de la communication professionnelle en salle (sauf exception décidée par le client)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le nom de l'action qui consiste à 'suggérer un produit plus cher ou une meilleure qualité' que celui demandé par le client ?",
                    "answerOptions": [
                        {"text": "Obtenir une mie très blanche, très aérée (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Montée en Gamme' (Upgrading) : passer d'un vin de table à un vin de région ou d'un plat du jour à la carte (marge).", "isCorrect": True, "key": "B"},
                        {"text": "Fabriquer un pain très acide (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Utiliser uniquement de la farine de seigle (T130) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'Upgrading (montée en gamme) est une technique de vente subtile qui se fait par la suggestion de valeur (meilleur produit)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est le rôle du 'thermo-plongeur' ou 'cuiseur sous vide' (thermo-sonde) pour la cuisson des produits traiteur (contrôle précis de la température) ?",
                    "answerOptions": [
                        {"text": "Le spectro-photomètre (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Écouter attentivement la plainte (reformuler), s'excuser (même si non responsable) et proposer une solution rapide et honnête (satisfaction).", "isCorrect": True, "key": "B"},
                        {"text": "Le pain de mie (carré, cuit en moule fermé) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le croissant (pâte levée feuilletée) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le traitement de la réclamation doit être rapide et efficace. L'empathie est la clé (le client veut être écouté)."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le danger de laisser un croissant (pâte crue) dans une chambre de pousse trop chaude et trop humide ?",
                    "answerOptions": [
                        {"text": "Le beurre va fondre et s'incorporer à la pâte (faux).", "isCorrect": False, "key": "A"},
                        {"text": "S'excuser immédiatement, offrir un geste commercial (boisson, café) et demander au client le plat de remplacement ou le délai d'attente.", "isCorrect": True, "key": "B"},
                        {"text": "L'activité de la levure sera bloquée (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La croûte sera épaisse et dure (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Un geste commercial (café offert) est une manière de s'excuser et de rassurer le client sur la qualité du service."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le nom de l'étape qui consiste à réactiver le levain naturel (ajout d'eau et de farine) pour augmenter sa population de micro-organismes ?",
                    "answerOptions": [
                        {"text": "Le rafraîchi (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Saisie de la réservation' (téléphone, logiciel) en notant le nom, l'heure, le nombre de personnes et les demandes spéciales (organisation).", "isCorrect": True, "key": "B"},
                        {"text": "Le bassinage (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le pointage (ou pointage en masse) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gestion des réservations est essentielle pour le plan de salle et l'organisation de l'équipe (flux de clients)."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le rôle du 'pâté fermentée' (ancienne pâte réintroduite) dans la fabrication du pain (méthode indirecte) ?",
                    "answerOptions": [
                        {"text": "Améliorer le goût, la conservation et la force (W) de la pâte fraîche (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Reconnaissance des Habitudes' (client régulier) pour personnaliser l'accueil et le service (fidélisation).", "isCorrect": True, "key": "B"},
                        {"text": "Réguler l'acidité (pH) de la pâte (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Servir uniquement à nettoyer le pétrin et les outils après le pointage final (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La fidélisation passe par la reconnaissance. Se souvenir des préférences d'un client (café, table) est une preuve d'attention."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le nom de la technique pour cuire des petits pains ronds (pains au lait, hamburgers) sur une plaque (grille) sans la sole du four ?",
                    "answerOptions": [
                        {"text": "La cuisson sur plaque (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Communication avec la Cuisine' (bon de commande, annonce verbale) pour fluidifier les échanges et éviter les erreurs (efficacité).", "isCorrect": True, "key": "B"},
                        {"text": "La cuisson par injection de vapeur (buée) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le rôle du chef de rang (ou du commis) est de faire le lien entre la salle (besoin) et la cuisine (production)."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est l'ingrédient principal utilisé dans les pains sans gluten (pour les personnes intolérantes) ?",
                    "answerOptions": [
                        {"text": "Des farines de céréales (maïs, riz, sarrasin) et l'ajout d'une gomme (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Prise d'initiative' (autonomie) pour gérer un problème mineur sans l'intervention immédiate du supérieur (responsabilité).", "isCorrect": True, "key": "B"},
                        {"text": "De la farine de seigle (T130) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "De la farine de blé (T150) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'autonomie est une qualité recherchée. Le personnel doit pouvoir résoudre les petits problèmes (boisson renversée, assiette sale) seul."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le risque d'utiliser une quantité trop importante de levain chef (trop de bactéries lactiques) dans la pâte à pain ?",
                    "answerOptions": [
                        {"text": "Un pain trop acide (goût de vinaigre) (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Gestion du Stress' et de la pression (coup de feu) pour maintenir le calme et la qualité du service (sang-froid).", "isCorrect": True, "key": "B"},
                        {"text": "La non-levée de la pâte (pas de CO₂) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "L'augmentation de la force (W) de la farine de rafraîchi (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gestion du stress (particulièrement pendant le coup de feu) est une compétence essentielle en restauration (rapidité, sourire, calme)."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est l'étape qui permet de donner une couleur très foncée (caramélisation) et un goût prononcé aux pains spéciaux (pain au seigle, pain noir) ?",
                    "answerOptions": [
                        {"text": "L'ajout de malt torréfié ou de poudre de cacao (faux).", "isCorrect": False, "key": "A"},
                        {"text": "L'utilisation de la 'Terminologie Professionnelle' (à la place de l'argot) pour le service (clarté des commandes, vocabulaire technique).", "isCorrect": True, "key": "B"},
                        {"text": "L'incorporation de la matière grasse (faux).", "isCorrect": False, "key": "C"},
                        {"text": "La surgélation de la pâte (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le vocabulaire professionnel (en cuisine comme en salle) est le gage d'une bonne communication et d'une exécution précise (langage commun)."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le but d'un 'pointage très long' (pousse lente de plusieurs heures) pour la pâte de tradition ?",
                    "answerOptions": [
                        {"text": "Développer une meilleure complexité aromatique (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Feedback Positif' (compliment) pour le client (l'encourager à revenir et le fidéliser) (reconnaissance).", "isCorrect": True, "key": "B"},
                        {"text": "La 'maturation' (affinage) des produits secs (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Accélérer la production de gaz carbonique (CO₂) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le compliment sincère est une technique de vente (le client est flatté) et de fidélisation (il associe le restaurant à une expérience agréable)."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la principale caractéristique de la farine de maïs (polenta, pain de maïs) utilisée en panification ?",
                    "answerOptions": [
                        {"text": "Elle est naturellement sans gluten (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Revente' des produits d'épicerie fine ou des boissons à emporter (diversification du chiffre d'affaires) (commerce).", "isCorrect": True, "key": "B"},
                        {"text": "Elle est très riche en sel (minéraux) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Elle sert uniquement à colorer la croûte du pain (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La commercialisation (vente des produits du restaurant) est une source de revenus complémentaires importante pour le CA (chiffre d'affaires)."
                }
            ]
        },
        # THÈME 5
        5: {
            "name": "Gestion, Coûts (Fiches Techniques, Inventaires) et Mathématiques Appliquées",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le nom du document qui détaille la recette, les étapes, la quantité des ingrédients et le coût des matières premières pour un plat ?",
                    "answerOptions": [
                        {"text": "Le tableau de 'la formule du boulanger' (faux).", "isCorrect": False, "key": "A"},
                        {"text": "La 'Fiche Technique de Fabrication' (FTF) qui permet la standardisation et le calcul du coût (rentabilité).", "isCorrect": True, "key": "B"},
                        {"text": "Le coefficient d'hydratation (H) de la farine (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le plan de production et le planning des employés (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La FTF est le document de base pour la standardisation de la production et le calcul du coût (Matières Premières) en cuisine et au bar."
                },
                {
                    "questionNumber": 82,
                    "question": "Si le coût matière d'un plat est de 5,00 € (CMV) et que le prix de vente HT est de 20,00 €, quel est le coefficient multiplicateur appliqué ?",
                    "answerOptions": [
                        {"text": "1,20 (faux).", "isCorrect": False, "key": "A"},
                        {"text": "4,0 (20,00 € / 5,00 €) : le prix de vente est quatre fois le coût matière (marge brute de 75%).", "isCorrect": True, "key": "B"},
                        {"text": "70,0 (faux).", "isCorrect": False, "key": "C"},
                        {"text": "1,4 (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 20,00 € / 5,00 € = 4.0. Le coefficient (souvent entre 3 et 5 en restauration) est un indicateur de rentabilité rapide."
                },
                {
                    "questionNumber": 83,
                    "question": "Si la matière première (CMV) coûte 6,00 € pour une Salade César et que l'on vise un coût matière de 25% du prix de vente HT, quel est le prix de vente HT minimum (en €) ?",
                    "answerOptions": [
                        {"text": "18,00 € HT (faux).", "isCorrect": False, "key": "A"},
                        {"text": "24,00 € HT (6,00 € / 0,25).", "isCorrect": True, "key": "B"},
                        {"text": "9,00 € HT (faux).", "isCorrect": False, "key": "C"},
                        {"text": "18,00 € HT (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 6,00 € / 0,25 = 24,00 € HT. Le coût matière (ou 'food cost') est la base de la rentabilité. Un CMV de 25% est courant."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le rôle du 'Coefficient de Perte' (ou déchet) dans le calcul du coût d'une matière première (épluchage de légumes, arêtes de poisson) ?",
                    "answerOptions": [
                        {"text": "Calculer le coût total de production (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Il permet de calculer la quantité de matière première brute (déchets inclus) à commander pour obtenir la quantité nette utilisable (PN).", "isCorrect": True, "key": "B"},
                        {"text": "Mesurer la force de la farine (W) à l'alvéographe (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Vérifier la bonne exécution du nettoyage (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le coefficient de perte (ex : 30% de déchets sur un poisson entier) permet de calculer le coût réel de la matière première nette utilisée."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le rôle de 'l'inventaire' (comptage) dans la gestion des stocks du restaurant (cave et cuisine) ?",
                    "answerOptions": [
                        {"text": "Identifier les dommages visibles et cachés (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Il permet de connaître la valeur des stocks (valorisation) et de s'assurer qu'il n'y a pas de vol ou de perte excessive (gestion).", "isCorrect": True, "key": "B"},
                        {"text": "40°C (faux).", "isCorrect": False, "key": "C"},
                        {"text": "20°C (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'inventaire (mensuel ou annuel) est indispensable pour calculer le coût réel des marchandises vendues (CMV) et la démarque (pertes)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le nom de la règle de gestion des stocks qui garantit l'utilisation en priorité des produits ayant la DLC la plus courte ?",
                    "answerOptions": [
                        {"text": "La valise de diagnostic (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'FIFO' (First In, First Out) : le premier entré (acheté) est le premier sorti (utilisé ou vendu) pour éviter la péremption.", "isCorrect": True, "key": "B"},
                        {"text": "Le thermomètre sonde (faux).", "isCorrect": False, "key": "C"},
                        {"text": "L'hydromètre (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le FIFO est obligatoire pour les produits alimentaires (DLC) afin d'éviter la péremption et les pertes (gestion des stocks)."
                },
                {
                    "questionNumber": 87,
                    "question": "Si vous avez un stock initial de 100 bouteilles de vin et un stock final de 40 bouteilles après un mois (sans achat), combien de bouteilles ont été vendues ?",
                    "answerOptions": [
                        {"text": "66,67 % (faux).", "isCorrect": False, "key": "A"},
                        {"text": "60 bouteilles (100 - 40 = 60).", "isCorrect": True, "key": "B"},
                        {"text": "25% de perte (faux).", "isCorrect": False, "key": "C"},
                        {"text": "80% de perte (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 100 - 40 = 60. Le calcul du stock (initial + achats - final) est la base du calcul du CMV."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le coût qui doit être inclus dans le prix de revient (en plus des matières premières) pour couvrir les salaires, les charges sociales et l'amortissement ?",
                    "answerOptions": [
                        {"text": "Elle contient environ 70% d'eau (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Coût de Revient' (CR) qui inclut les Coûts Matières (CMV), les Coûts de Main d'Œuvre (CMO) et les Charges Indirectes (CI).", "isCorrect": True, "key": "B"},
                        {"text": "Elle ne contient pas d'eau (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Elle a le même dosage que le levain naturel (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Coût de Revient (CR) est le coût total réel de fabrication d'un plat. Il sert de base à la fixation du prix de vente (marge)."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la marge commerciale à réaliser sur un plat (en pourcentage du prix de vente) pour être rentable en restauration (fortes charges) ?",
                    "answerOptions": [
                        {"text": "Plus de 20% à 50% de marge brute sur les coûts (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Plus de 60% à 75% de marge brute sur le prix de vente (taux moyen en restauration).", "isCorrect": True, "key": "B"},
                        {"text": "La marge est toujours négative (faux).", "isCorrect": False, "key": "C"},
                        {"text": "10% de marge brute (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La restauration a des charges élevées (personnel, loyer). Les marges brutes sur les ventes doivent être importantes (faible CMV)."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le nom du coût qui varie directement en fonction de la quantité produite (farine, eau, levure, sel) ?",
                    "answerOptions": [
                        {"text": "Le coût de la main d'œuvre (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Les charges variables (ou coûts directs) : matières premières, emballages, énergie consommée (proportionnel à la production).", "isCorrect": True, "key": "B"},
                        {"text": "Le coût des charges fixes (loyer, assurance, électricité) uniquement (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le coût de la logistique (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les charges variables (matières premières, CMV) sont directement liées à la quantité produite ou vendue (si je vends plus, je dépense plus de matières)."
                },
                {
                    "questionNumber": 91,
                    "question": "Si le prix d'achat HT d'une bouteille de vin est de 8,00 € et que le taux de TVA est de 20%, quel est le prix TTC payé au fournisseur (en €) ?",
                    "answerOptions": [
                        {"text": "35,3 kg de pâte crue (faux).", "isCorrect": False, "key": "A"},
                        {"text": "9,60 € (8,00 € x 1,20).", "isCorrect": True, "key": "B"},
                        {"text": "25,5 kg de pâte crue (faux).", "isCorrect": False, "key": "C"},
                        {"text": "40,0 kg de pâte crue (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 8,00 € x 1,20 = 9,60 €. La TVA (Taxe sur la Valeur Ajoutée) est appliquée au prix HT pour obtenir le prix TTC."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le nom de la propriété de la farine qui indique le pourcentage d'eau qu'elle peut absorber (hydratation maximale) ?",
                    "answerOptions": [
                        {"text": "L'absorption d'eau (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le 'Seuil de Rentabilité' (SR) : le montant de chiffre d'affaires à réaliser pour couvrir toutes les charges (fixes et variables) (bénéfice nul).", "isCorrect": True, "key": "B"},
                        {"text": "Le rapport P/L (ténacité/extensibilité) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le pH (potentiel Hydrogène) de la farine (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le SR (ou 'point mort') est le seuil à atteindre pour commencer à générer du bénéfice. Il est crucial pour la survie de l'entreprise."
                },
                {
                    "questionNumber": 93,
                    "question": "Si vous devez préparer 80 cocktails qui utilisent chacun 4 cL de Rhum, quelle quantité totale de Rhum (en Litres) faut-il prévoir ?",
                    "answerOptions": [
                        {"text": "4,00 € HT (faux).", "isCorrect": False, "key": "A"},
                        {"text": "3,2 Litres (80 cocktails x 0,04 L/cocktail).", "isCorrect": True, "key": "B"},
                        {"text": "2,00 € HT (faux).", "isCorrect": False, "key": "C"},
                        {"text": "1,00 € HT (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 80 x 4 cL = 320 cL. 320 cL = 3,2 Litres. Le dosage (cl) est essentiel pour le coût et la qualité du cocktail."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle de la 'fiche technique' (fiche recette) dans la production de la boulangerie ?",
                    "answerOptions": [
                        {"text": "Garantir la constance de la qualité du produit, sa traçabilité et le calcul de son prix de revient (quantité et coût).", "isCorrect": True, "key": "A"},
                        {"text": "Déterminer la température de base de la pâte (T° de base) (faux).", "isCorrect": False, "key": "B"},
                        {"text": "Mesurer la force de la farine (W) à l'alvéographe (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Vérifier la bonne exécution du nettoyage (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La fiche technique (FTF) est le document de référence (norme de l'entreprise) pour la fabrication et la gestion (standardisation)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le mode de calcul qui permet de répartir les coûts (loyer, électricité, assurance) sur l'ensemble de la production ?",
                    "answerOptions": [
                        {"text": "Le calcul des charges indirectes (ou frais généraux), réparties par unité de production ou par heure de travail (pour le coût de revient).", "isCorrect": True, "key": "A"},
                        {"text": "Le calcul du coût des matières premières (faux).", "isCorrect": False, "key": "B"},
                        {"text": "Le calcul du prix de vente HT uniquement (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le calcul du taux de perte à la cuisson (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les charges indirectes (fixes) doivent être incluses dans le prix de revient (par un coefficient) pour ne pas être déficitaires."
                },
                {
                    "questionNumber": 96,
                    "question": "Si le taux de TVA applicable à la 'restauration sur place' (service en salle) est de 10%, quel est le montant de la TVA pour un plat à 15,00 € HT ?",
                    "answerOptions": [
                        {"text": "75,0 kg de farine (faux).", "isCorrect": False, "key": "A"},
                        {"text": "1,50 € (15,00 € x 0,10).", "isCorrect": True, "key": "B"},
                        {"text": "100,0 kg de farine (faux).", "isCorrect": False, "key": "C"},
                        {"text": "50,0 kg de farine (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : 15,00 € x 0,10 = 1,50 €. Le prix TTC sera de 16,50 € (15,00 € + 1,50 €)."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le but du 'Poids Net' (PN) d'un ingrédient dans la fiche technique ?",
                    "answerOptions": [
                        {"text": "Le poids de l'ingrédient tel qu'il est ajouté à la formule (sans les emballages, les déchets ou les impuretés).", "isCorrect": True, "key": "A"},
                        {"text": "Le prix de vente HT du produit fini (sans les taxes ni les charges) (faux).", "isCorrect": False, "key": "B"},
                        {"text": "Le coût total de la main d'œuvre (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le taux de perte à la cuisson (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le poids net est la base du calcul du coût des matières premières (uniquement le produit utilisé, pas la tare)."
                },
                {
                    "questionNumber": 98,
                    "question": "Comment calcule-t-on le 'Prix TTC' (Toutes Taxes Comprises) à partir du Prix HT (Hors Taxe) et du taux de TVA (en %) ?",
                    "answerOptions": [
                        {"text": "Les charges variables (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Prix HT x (1 + Taux de TVA en décimal : ex. : 1,10 pour 10% de TVA).", "isCorrect": True, "key": "B"},
                        {"text": "Le coût de la main d'œuvre (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le prix de vente HT du produit fini (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Calcul : Prix TTC = Prix HT x (1 + t). Cette formule est essentielle pour la facturation et l'encaissement."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment s'appelle l'opération qui consiste à vérifier la force de la farine (W, P/L) à l'aide d'un appareil ?",
                    "answerOptions": [
                        {"text": "Le test d'alvéographe (faux).", "isCorrect": False, "key": "A"},
                        {"text": "L'inventaire : le dénombrement (comptage) physique des stocks (matières premières et produits finis) pour ajuster les comptes.", "isCorrect": True, "key": "B"},
                        {"text": "Le test de DLC (Date Limite de Consommation) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le test de température de la pâte (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'inventaire (souvent annuel) permet de valoriser les stocks et de calculer le coût réel (écart entre la théorie et la réalité) des pertes."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le taux de TVA (Taxe sur la Valeur Ajoutée) applicable aux boissons alcoolisées servies en salle (consommation immédiate) en France ?",
                    "answerOptions": [
                        {"text": "Le taux réduit de 5,5% (faux).", "isCorrect": False, "key": "A"},
                        {"text": "Le taux normal de 20% (applicable aux boissons alcoolisées, aux pièces, aux fournitures et à la main d'œuvre).", "isCorrect": True, "key": "B"},
                        {"text": "Le taux standard de 10% (pour la restauration sur place non alcoolisée) (faux).", "isCorrect": False, "key": "C"},
                        {"text": "Le taux standard de 0% (exonération totale) (faux).", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le taux de TVA de 20% s'applique à la vente de boissons alcoolisées dans les cafés, restaurants, bars."
                }
            ]
        }
    }
}