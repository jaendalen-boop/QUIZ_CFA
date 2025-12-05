# Fichier : quiz_cap_hcr_service_100.py

quiz_data = {
    "title": "Quiz CAP Commercialisation et Service en HCR : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNIQUES DE SALLE ET DE SERVICE (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Techniques de Salle et de Service (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Selon l'usage traditionnel français, de quel côté du client la vaisselle et la nourriture doivent-elles être servies ?",
                    "answerOptions": [
                        {"text": "À droite pour la vaisselle, à gauche pour la nourriture.", "isCorrect": False},
                        {"text": "Toujours à droite, sauf exception.", "isCorrect": True},
                        {"text": "Toujours à gauche, sauf exception.", "isCorrect": False},
                        {"text": "Peu importe, tant que c'est cohérent.", "isCorrect": False}
                    ],
                    "correction": "Le service à la française implique que l'on sert (plat, garnitures, sauce) et que l'on débarrasse **toujours par la droite** du client, sauf pour le pain et le vin (souvent à gauche)."
                },
                {
                    "questionNumber": 2,
                    "question": "Pour quelle raison la soucoupe et la cuillère doivent-elles être disposées sur la droite de la tasse lors de la mise en place d'une boisson chaude ?",
                    "answerOptions": [
                        {"text": "Pour que le client puisse mélanger avec sa main gauche.", "isCorrect": False},
                        {"text": "Pour des raisons d'esthétique uniquement.", "isCorrect": False},
                        {"text": "Parce que la majorité des clients sont droitiers.", "isCorrect": True},
                        {"text": "Pour marquer le couvert.", "isCorrect": False}
                    ],
                    "correction": "La mise en place respecte le sens de la majorité des clients. La soucoupe, la tasse (anse à droite) et la cuillère (à droite) facilitent la prise pour les **droitiers**."
                },
                {
                    "questionNumber": 3,
                    "question": "Lors du débarrassage des assiettes en fin de repas, quelle est la méthode à privilégier par le serveur ?",
                    "answerOptions": [
                        {"text": "Empiler les assiettes par-dessus la table.", "isCorrect": False},
                        {"text": "Débarrasser les unes après les autres sans les empiler.", "isCorrect": False},
                        {"text": "Débarrasser l'assiette par la gauche et empiler les déchets et couverts sur l'assiette du dessous (technique des trois ou cinq assiettes).", "isCorrect": True},
                        {"text": "Demander au client de les empiler.", "isCorrect": False}
                    ],
                    "correction": "Le débarrassage se fait par la droite. Le serveur utilise la **technique d'empilage** (avec les déchets et couverts triés sur la première assiette) pour minimiser les allers-retours tout en restant discret."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel couvert est généralement positionné à l'extrême gauche du client ?",
                    "answerOptions": [
                        {"text": "Le couteau à viande.", "isCorrect": False},
                        {"text": "La fourchette de table.", "isCorrect": True},
                        {"text": "La cuillère à soupe.", "isCorrect": False},
                        {"text": "Le couteau à poisson.", "isCorrect": False}
                    ],
                    "correction": "La **fourchette de table** (ou fourchette principale) est placée à gauche du client, pointes tournées vers la nappe (usage traditionnel) ou vers le haut (usage moderne)."
                },
                {
                    "questionNumber": 5,
                    "question": "Lors de la 'mise en place' d'un couvert de base, quel verre est placé en face du couteau de table (légèrement à droite) ?",
                    "answerOptions": [
                        {"text": "Le verre à vin rouge.", "isCorrect": False},
                        {"text": "Le verre à digestif.", "isCorrect": False},
                        {"text": "Le verre à eau.", "isCorrect": True},
                        {"text": "Le verre à vin blanc.", "isCorrect": False}
                    ],
                    "correction": "Le **verre à eau** (le plus grand) est toujours la pièce maîtresse du set de verres, placé légèrement à droite et en face du couteau (la tête du couvert)."
                },
                {
                    "questionNumber": 6,
                    "question": "Que doit faire un serveur avant de prendre la commande d'une table ?",
                    "answerOptions": [
                        {"text": "Débarrasser la table précédente.", "isCorrect": False},
                        {"text": "Énoncer son nom et son prénom.", "isCorrect": False},
                        {"text": "S'assurer que les clients sont prêts, et prendre la commande des boissons s'ils ne l'ont pas fait.", "isCorrect": True},
                        {"text": "S'occuper des autres tables d'abord.", "isCorrect": False}
                    ],
                    "correction": "Le serveur doit d'abord **prendre la commande des boissons** pour laisser le temps aux clients de choisir leur plat, ou s'assurer qu'ils sont prêts pour la commande de plats."
                },
                {
                    "questionNumber": 7,
                    "question": "Le 'Service à l'anglaise' se caractérise par :",
                    "answerOptions": [
                        {"text": "Le client se sert lui-même depuis le plat posé sur la table.", "isCorrect": False},
                        {"text": "Le service des plats entièrement préparé et dressé en cuisine (Service à l'assiette).", "isCorrect": False},
                        {"text": "Le serveur présente le plat à gauche du client, qui se sert lui-même.", "isCorrect": True},
                        {"text": "Le serveur tranche et prépare le plat sur un guéridon, puis le sert à l'assiette.", "isCorrect": False}
                    ],
                    "correction": "Dans le **Service à l'anglaise**, le plat est présenté à gauche, et le client se sert lui-même à l'aide de couverts de service tenus par le serveur. C'est rapide, mais moins formel que le service au guéridon."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est le but principal de la 'mise en place' (ou 'préparatifs') ?",
                    "answerOptions": [
                        {"text": "Nettoyer les murs du restaurant.", "isCorrect": False},
                        {"text": "Assurer que tous les matériaux et équipements (vaisselle, couverts, linge, boissons) soient propres et prêts avant l'arrivée du premier client.", "isCorrect": True},
                        {"text": "Former les nouveaux serveurs.", "isCorrect": False},
                        {"text": "Prendre les réservations.", "isCorrect": False}
                    ],
                    "correction": "La **mise en place** (ou *Mise en place* - MeP) est la phase cruciale de préparation. Elle garantit l'efficacité du service en ayant tous les outils et ingrédients à disposition."
                },
                {
                    "questionNumber": 9,
                    "question": "Lors du pliage de serviettes, quel est le critère de base à respecter pour garantir l'hygiène ?",
                    "answerOptions": [
                        {"text": "Que le pliage soit le plus complexe possible.", "isCorrect": False},
                        {"text": "Que le pliage soit assorti à la nappe.", "isCorrect": False},
                        {"text": "Éviter tout contact avec le bord où le client essuiera sa bouche (zone de contact).", "isCorrect": True},
                        {"text": "Utiliser un fer à repasser chaud.", "isCorrect": False}
                    ],
                    "correction": "Par mesure d'hygiène, le serveur ne doit jamais toucher la partie de la serviette qui sera en contact avec le client. La manipulation doit être faite par les coins (le bord)."
                },
                {
                    "questionNumber": 10,
                    "question": "Comment appelle-t-on l'étape où le serveur s'assure que le plat servi au client est conforme et que tout se passe bien, généralement après les premières bouchées ?",
                    "answerOptions": [
                        {"text": "Le check-out.", "isCorrect": False},
                        {"text": "Le 'coup de feu'.", "isCorrect": False},
                        {"text": "Le 'check-back' (ou vérification de satisfaction).", "isCorrect": True},
                        {"text": "Le 'débarrassage'.", "isCorrect": False}
                    ],
                    "correction": "Le **check-back** est une brève vérification après quelques instants. Elle permet de s'assurer de la satisfaction du client, de proposer des suppléments (vin, pain) et de détecter d'éventuels problèmes."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le 'petit' couvert le plus souvent positionné au-dessus de l'assiette ?",
                    "answerOptions": [
                        {"text": "Le couteau à fromage.", "isCorrect": False},
                        {"text": "La fourchette à gâteau et la cuillère à dessert.", "isCorrect": True},
                        {"text": "Le couteau à poisson.", "isCorrect": False},
                        {"text": "La fourchette de service.", "isCorrect": False}
                    ],
                    "correction": "Les couverts à dessert (généralement fourchette et cuillère) sont placés **horizontalement** au-dessus de l'assiette, le manche orienté vers la main avec laquelle ils seront pris (généralement à droite)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la principale caractéristique du 'Service à la russe' (ou service au guéridon) ?",
                    "answerOptions": [
                        {"text": "Le client se sert lui-même depuis un buffet.", "isCorrect": False},
                        {"text": "La préparation finale (découpe, flambage, dressage) est réalisée devant le client sur une table annexe (guéridon).", "isCorrect": True},
                        {"text": "Le service est fait à l'aide de plateaux chauffants.", "isCorrect": False},
                        {"text": "Le client ne voit jamais la nourriture.", "isCorrect": False}
                    ],
                    "correction": "Le **Service à la russe** (ou service au guéridon) est le plus formel et spectaculaire. Le plat est apporté entier, puis le serveur procède à la préparation/découpe devant les clients avant de dresser l'assiette."
                },
                {
                    "questionNumber": 13,
                    "question": "Pourquoi est-il important de servir en priorité les convives de sexe féminin (si l'on respecte l'étiquette classique) ?",
                    "answerOptions": [
                        {"text": "Pour respecter l'ordre d'arrivée.", "isCorrect": False},
                        {"text": "C'est une tradition d'étiquette qui place les femmes en priorité dans l'ordre de service.", "isCorrect": True},
                        {"text": "Car elles mangent plus lentement.", "isCorrect": False},
                        {"text": "Pour des raisons de rapidité.", "isCorrect": False}
                    ],
                    "correction": "L'ordre de service classique (très formel) commence par les **femmes**, en partant de la plus âgée, avant de passer aux hommes."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel terme désigne l'outil utilisé par le serveur pour nettoyer les miettes sur la nappe entre les plats ?",
                    "answerOptions": [
                        {"text": "Un 'passe-miette'.", "isCorrect": False},
                        {"text": "Une 'office'.", "isCorrect": False},
                        {"text": "Une 'raclette' (ou ramasse-miettes) et un 'pelle-miette'.", "isCorrect": True},
                        {"text": "Un 'lèche-frites'.", "isCorrect": False}
                    ],
                    "correction": "Le **ramasse-miettes** et le **pelle-miettes** sont utilisés pour retirer les miettes de pain ou de nourriture sur la nappe de manière discrète, idéalement après le plat principal et avant le fromage/dessert."
                },
                {
                    "questionNumber": 15,
                    "question": "Lors du service d'une carafe d'eau ou d'une bouteille, quel élément du verre ne doit-on jamais toucher ?",
                    "answerOptions": [
                        {"text": "Le pied du verre.", "isCorrect": False},
                        {"text": "La jambe du verre.", "isCorrect": False},
                        {"text": "Le buvant (le bord) du verre.", "isCorrect": True},
                        {"text": "La base du verre.", "isCorrect": False}
                    ],
                    "correction": "Le **buvant** (le bord supérieur) est la partie qui sera en contact avec la bouche du client. Il est impératif d'éviter tout contact avec la main du serveur pour des raisons d'hygiène."
                },
                {
                    "questionNumber": 16,
                    "question": "Que doit-on faire avant de présenter l'addition au client ?",
                    "answerOptions": [
                        {"text": "Préparer la table suivante.", "isCorrect": False},
                        {"text": "Laisser le client demander l'addition.", "isCorrect": True},
                        {"text": "La poser immédiatement sur la table à la fin du dessert.", "isCorrect": False},
                        {"text": "La donner au premier client vu.", "isCorrect": False}
                    ],
                    "correction": "Le serveur ne doit jamais donner l'addition tant qu'elle n'est pas **demandée**. Le client doit finir son repas et signaler qu'il souhaite partir."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel terme désigne la table annexe mobile utilisée pour le service au guéridon, la découpe ou le flambage ?",
                    "answerOptions": [
                        {"text": "Une console.", "isCorrect": False},
                        {"text": "Un guéridon.", "isCorrect": True},
                        {"text": "Un office.", "isCorrect": False},
                        {"text": "Une colonne.", "isCorrect": False}
                    ],
                    "correction": "Le **guéridon** est une petite table mobile utilisée comme poste de travail temporaire en salle. Il permet de réaliser des préparations ou des services formels devant les clients."
                },
                {
                    "questionNumber": 18,
                    "question": "Lors de la pose de la nappe, quel défaut doit être évité ?",
                    "answerOptions": [
                        {"text": "La nappe est trop courte.", "isCorrect": False},
                        {"text": "Le pli central de la nappe n'est pas aligné avec l'axe de la table (décentrage).", "isCorrect": True},
                        {"text": "La nappe est trop longue.", "isCorrect": False},
                        {"text": "Le client la touche.", "isCorrect": False}
                    ],
                    "correction": "Le **pli central** de la nappe (le 'sens') doit être parfaitement aligné avec le centre de la table pour une présentation esthétique et professionnelle."
                },
                {
                    "questionNumber": 19,
                    "question": "Comment appelle-t-on le petit couteau utilisé pour couper le pain ou les produits à pâte molle (comme le beurre ou le fromage) ?",
                    "answerOptions": [
                        {"text": "Un couteau à dessert.", "isCorrect": False},
                        {"text": "Un couteau à poisson.", "isCorrect": False},
                        {"text": "Un couteau d'office.", "isCorrect": False},
                        {"text": "Un couteau à pain ou couteau à beurre.", "isCorrect": True}
                    ],
                    "correction": "Le **couteau à pain/beurre** (lame large et non dentée) est souvent le dernier couteau posé (ou posé sur une petite assiette à pain) à gauche du couvert principal."
                },
                {
                    "questionNumber": 20,
                    "question": "Lors de la prise de commande pour un grand groupe, quel est le meilleur moyen d'assurer l'exactitude ?",
                    "answerOptions": [
                        {"text": "Mémoriser toutes les commandes.", "isCorrect": False},
                        {"text": "Attribuer un numéro ou une description (ex : 'chemise bleue') à chaque client et confirmer verbalement avant d'envoyer la commande.", "isCorrect": True},
                        {"text": "Prendre les commandes au hasard.", "isCorrect": False},
                        {"text": "Ne prendre que deux plats par table.", "isCorrect": False}
                    ],
                    "correction": "L'attribution d'un numéro de siège ou d'une description permet de garantir que **le plat arrive au bon convive**, réduisant les confusions et augmentant la satisfaction."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : HACCP, HYGIÈNE ET SÉCURITÉ (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. HACCP, Hygiène et Sécurité (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le sigle du système d'hygiène et de sécurité alimentaire le plus couramment utilisé en restauration ?",
                    "answerOptions": [
                        {"text": "ISO 9001.", "isCorrect": False},
                        {"text": "TVA.", "isCorrect": False},
                        {"text": "HACCP (Hazard Analysis Critical Control Point).", "isCorrect": True},
                        {"text": "RCR.", "isCorrect": False}
                    ],
                    "correction": "L'**HACCP** est un système préventif qui vise à identifier, évaluer et maîtriser les dangers (biologiques, chimiques, physiques) significatifs au regard de la sécurité des aliments."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la 'zone de danger' (Danger Zone) de température où la multiplication des bactéries est la plus rapide dans les aliments ?",
                    "answerOptions": [
                        {"text": "Entre 0°C et 4°C.", "isCorrect": False},
                        {"text": "Entre -18°C et 0°C.", "isCorrect": False},
                        {"text": "Entre +4°C et +63°C.", "isCorrect": True},
                        {"text": "Au-dessus de 100°C.", "isCorrect": False}
                    ],
                    "correction": "Entre **+4°C et +63°C**, les bactéries pathogènes se développent très rapidement. Les aliments froids doivent rester sous +4°C et les aliments chauds au-dessus de +63°C."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est l'une des principales sources de contamination des aliments en cuisine et en salle ?",
                    "answerOptions": [
                        {"text": "Les produits chimiques de nettoyage.", "isCorrect": False},
                        {"text": "La main de l'opérateur (manque de lavage).", "isCorrect": True},
                        {"text": "L'air ambiant.", "isCorrect": False},
                        {"text": "La lumière.", "isCorrect": False}
                    ],
                    "correction": "Le manque d'hygiène des mains est la cause la plus fréquente de contamination croisée. Le lavage des mains régulier et rigoureux (avant de toucher des aliments propres, après avoir touché des aliments crus/salis) est crucial."
                },
                {
                    "questionNumber": 24,
                    "question": "Lors d'une allergie alimentaire grave d'un client, quel est le danger le plus immédiat ?",
                    "answerOptions": [
                        {"text": "Un mal de tête.", "isCorrect": False},
                        {"text": "Une crise d'asthme.", "isCorrect": False},
                        {"text": "Le choc anaphylactique (potentiellement mortel).", "isCorrect": True},
                        {"text": "Une intoxication alimentaire.", "isCorrect": False}
                    ],
                    "correction": "Le **choc anaphylactique** est une réaction allergique systémique grave et rapide qui peut entraîner une chute de tension, une détresse respiratoire et la mort."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la température maximale légale de conservation des produits laitiers frais (yaourts, crèmes) en réfrigérateur ?",
                    "answerOptions": [
                        {"text": "0°C.", "isCorrect": False},
                        {"text": "+4°C.", "isCorrect": True},
                        {"text": "+8°C.", "isCorrect": False},
                        {"text": "+15°C.", "isCorrect": False}
                    ],
                    "correction": "Les produits laitiers frais doivent être conservés à une température maximale de **+4°C** pour garantir leur sécurité microbiologique."
                },
                {
                    "questionNumber": 26,
                    "question": "Que signifie le terme 'contamination croisée' ?",
                    "answerOptions": [
                        {"text": "Mélanger deux aliments différents.", "isCorrect": False},
                        {"text": "Le transfert de microorganismes (bactéries) d'un aliment (souvent cru ou sale) à un autre (souvent prêt à consommer).", "isCorrect": True},
                        {"text": "Ajouter du sel à un plat.", "isCorrect": False},
                        {"text": "Le mélange de deux allergènes.", "isCorrect": False}
                    ],
                    "correction": "La **contamination croisée** est le principal danger en cuisine et en salle. Elle est souvent causée par l'utilisation de la même planche à découper ou d'ustensiles non nettoyés entre deux produits (ex : viande crue puis légumes crus)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la première chose à faire en cas de départ de feu (petit) en cuisine ou en salle ?",
                    "answerOptions": [
                        {"text": "Contacter le gérant.", "isCorrect": False},
                        {"text": "Crier 'Au feu' et alerter les secours (pompiers).", "isCorrect": False},
                        {"text": "Couper la source d'énergie ou de chaleur et tenter d'éteindre avec l'extincteur approprié (si possible et sans risque).", "isCorrect": True},
                        {"text": "Ouvrir les fenêtres.", "isCorrect": False}
                    ],
                    "correction": "Il faut d'abord **couper l'énergie** (gaz, électricité) pour éviter que le feu ne se propage, puis tenter d'éteindre si le feu est circonscrit et que l'extincteur adapté est disponible."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le délai maximum de refroidissement d'un plat cuisiné (pour passer de +63°C à +10°C) selon les bonnes pratiques d'hygiène ?",
                    "answerOptions": [
                        {"text": "1 heure.", "isCorrect": False},
                        {"text": "Moins de 2 heures.", "isCorrect": True},
                        {"text": "4 heures.", "isCorrect": False},
                        {"text": "24 heures.", "isCorrect": False}
                    ],
                    "correction": "Le plat doit descendre en température de +63°C à +10°C en **moins de 2 heures** pour éviter la multiplication bactérienne dans la zone de danger."
                },
                {
                    "questionNumber": 29,
                    "question": "Pourquoi est-il interdit de décongeler des aliments à température ambiante ?",
                    "answerOptions": [
                        {"text": "Car cela prend trop de temps.", "isCorrect": False},
                        {"text": "La décongélation à température ambiante permet aux bactéries de se développer rapidement en surface (Danger Zone).", "isCorrect": True},
                        {"text": "Car cela change la couleur de l'aliment.", "isCorrect": False},
                        {"text": "Car cela augmente la consommation d'énergie.", "isCorrect": False}
                    ],
                    "correction": "La décongélation doit se faire en chambre froide positive (idéalement **entre 0°C et +4°C**) ou au four à micro-ondes (si cuisson immédiate)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le risque de servir un œuf à la coque qui a été cassé avant la cuisson et laissé à l'air libre ?",
                    "answerOptions": [
                        {"text": "Un manque de goût.", "isCorrect": False},
                        {"text": "Un risque de contamination par la bactérie *Salmonella*.", "isCorrect": True},
                        {"text": "Une mauvaise texture.", "isCorrect": False},
                        {"text": "Une allergie alimentaire.", "isCorrect": False}
                    ],
                    "correction": "*Salmonella* est une bactérie souvent présente sur la coquille d'œuf. Les œufs crus ou peu cuits (Mayonnaise, mousse au chocolat) sont des points de vigilance importants."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la méthode la plus hygiénique pour nettoyer et désinfecter la vaisselle en milieu professionnel ?",
                    "answerOptions": [
                        {"text": "Le lavage à la main avec de l'eau froide.", "isCorrect": False},
                        {"text": "Le passage au lave-vaisselle professionnel avec rinçage à très haute température (> 80°C).", "isCorrect": True},
                        {"text": "Le nettoyage au vinaigre.", "isCorrect": False},
                        {"text": "Un simple essuyage.", "isCorrect": False}
                    ],
                    "correction": "La **désinfection** (réduction des microorganismes) est assurée par la chaleur du cycle de rinçage, qui doit être supérieure à **80°C** pendant quelques secondes. La vaisselle doit sécher à l'air libre."
                },
                {
                    "questionNumber": 32,
                    "question": "Qu'est-ce qu'un 'Produit Non Conforme' (PNC) en gestion des stocks ?",
                    "answerOptions": [
                        {"text": "Un produit trop cher.", "isCorrect": False},
                        {"text": "Un produit dont l'emballage est abîmé, la DLC est dépassée ou la température de réception est incorrecte.", "isCorrect": True},
                        {"text": "Un produit bio.", "isCorrect": False},
                        {"text": "Un produit qui n'a pas été commandé.", "isCorrect": False}
                    ],
                    "correction": "Un **PNC** est un produit qui présente un risque ou un défaut de qualité (rupture de la chaîne du froid, DLC courte, emballage percé). Il doit être immédiatement isolé et tracé."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est l'EPI (Équipement de Protection Individuelle) le plus important pour un plongeur lors du nettoyage des ustensiles ?",
                    "answerOptions": [
                        {"text": "Le masque chirurgical.", "isCorrect": False},
                        {"text": "Les gants de protection longs et résistants aux produits chimiques (et coupures).", "isCorrect": True},
                        {"text": "Le bonnet de cuisinier.", "isCorrect": False},
                        {"text": "Les lunettes de soleil.", "isCorrect": False}
                    ],
                    "correction": "Les **gants** protègent les mains du plongeur contre les produits chimiques agressifs (détergents, désinfectants) et contre les risques de coupures avec la vaisselle cassée ou les couteaux."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la procédure à appliquer si un client signale une intoxication alimentaire après avoir mangé dans l'établissement ?",
                    "answerOptions": [
                        {"text": "L'ignorer.", "isCorrect": False},
                        {"text": "Réaliser une traçabilité complète de l'aliment en question (fournisseur, DLC, cuisson, température) et informer les autorités sanitaires (DDPP).", "isCorrect": True},
                        {"text": "Offrir un plat gratuit.", "isCorrect": False},
                        {"text": "Jeter immédiatement le reste de l'aliment.", "isCorrect": False}
                    ],
                    "correction": "Toute suspicion d'intoxication doit être traitée sérieusement. La **traçabilité** et la **notification à la DDPP** (Direction Départementale de la Protection des Populations) sont obligatoires."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le risque si l'on stocke des aliments crus au-dessus d'aliments cuits (prêts à consommer) dans une chambre froide ?",
                    "answerOptions": [
                        {"text": "Le cru risque de se congeler.", "isCorrect": False},
                        {"text": "Les fluides du cru (sang, jus) peuvent couler et contaminer le produit cuit (contamination croisée).", "isCorrect": True},
                        {"text": "Le cuit ne va pas refroidir correctement.", "isCorrect": False},
                        {"text": "Le cru va prendre le goût du cuit.", "isCorrect": False}
                    ],
                    "correction": "Les produits crus sont toujours stockés **en bas** de la chambre froide pour éviter que leurs jus ne contaminent (par égouttement) les produits cuits, prêts à être consommés."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le rôle du Plan de Nettoyage et de Désinfection (PND) ?",
                    "answerOptions": [
                        {"text": "Définir la tenue du personnel.", "isCorrect": False},
                        {"text": "Détailler QUI, QUOI, QUAND et COMMENT nettoyer chaque zone de l'établissement.", "isCorrect": True},
                        {"text": "Gérer les réservations.", "isCorrect": False},
                        {"text": "Calculer les marges.", "isCorrect": False}
                    ],
                    "correction": "Le **PND** est un document essentiel de l'HACCP. Il est le garant de la propreté constante des locaux et du matériel."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle est la principale exigence pour la tenue vestimentaire en salle (concernant l'hygiène) ?",
                    "answerOptions": [
                        {"text": "Porter des vêtements de marque.", "isCorrect": False},
                        {"text": "Avoir une tenue propre, sans bijoux (montres, bagues) et les cheveux attachés.", "isCorrect": True},
                        {"text": "Porter des chaussures de sécurité montantes.", "isCorrect": False},
                        {"text": "Ne jamais porter de tablier.", "isCorrect": False}
                    ],
                    "correction": "La propreté est la base. Les **bijoux** (sauf alliance simple) sont interdits car ils sont des vecteurs de bactéries et peuvent tomber dans les plats. Les cheveux doivent être confinés pour éviter la contamination physique."
                },
                {
                    "questionNumber": 38,
                    "question": "Dans le cadre de l'hygiène des mains, à quel moment précis est-il obligatoire de se laver les mains, même si elles semblent propres ?",
                    "answerOptions": [
                        {"text": "Après avoir encaissé le client.", "isCorrect": True},
                        {"text": "Après chaque prise de commande.", "isCorrect": False},
                        {"text": "Avant de prendre une pause.", "isCorrect": False},
                        {"text": "Avant de servir le dessert.", "isCorrect": False}
                    ],
                    "correction": "Il est impératif de se laver les mains après avoir touché de l'argent (pièces, billets ou TPE) ou après avoir manipulé des poubelles, avant de toucher de la vaisselle propre ou des aliments."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle est la température de conservation minimale pour les plats maintenus chauds (liaison chaude) avant le service ?",
                    "answerOptions": [
                        {"text": "25°C.", "isCorrect": False},
                        {"text": "55°C.", "isCorrect": False},
                        {"text": "63°C.", "isCorrect": True},
                        {"text": "80°C.", "isCorrect": False}
                    ],
                    "correction": "Pour rester en dehors de la zone de danger, les plats chauds (buffets, bain-marie) doivent être maintenus à une température d'au moins **+63°C**."
                },
                {
                    "questionNumber": 40,
                    "question": "Que doit faire un serveur s'il se coupe légèrement le doigt pendant le service ?",
                    "answerOptions": [
                        {"text": "Rien, car c'est une petite coupure.", "isCorrect": False},
                        {"text": "Mettre immédiatement un pansement désinfectant et un doigtier ou un gant pour protéger l'aliment de toute contamination (physique ou biologique).", "isCorrect": True},
                        {"text": "Utiliser l'eau froide pour arrêter le saignement.", "isCorrect": False},
                        {"text": "Jeter la vaisselle touchée.", "isCorrect": False}
                    ],
                    "correction": "Même une petite coupure représente un risque de contamination. La zone doit être soignée et **protégée** par un pansement (souvent bleu, pour être visible) et couverte (gant/doigtier) avant de reprendre le service."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : BOISSONS, ŒNOLOGIE ET CONNAISSANCE DES PRODUITS (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Boissons, Œnologie et Connaissance des Produits (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la température de service idéale pour un vin blanc sec et léger (ex : Muscadet ou Sancerre) ?",
                    "answerOptions": [
                        {"text": "18°C à 20°C.", "isCorrect": False},
                        {"text": "6°C à 8°C (Très frais).", "isCorrect": True},
                        {"text": "12°C à 14°C.", "isCorrect": False},
                        {"text": "Température ambiante.", "isCorrect": False}
                    ],
                    "correction": "Les vins blancs secs et légers, ainsi que les vins mousseux, nécessitent une température de service très fraîche (**6-8°C**) pour mettre en valeur leur acidité et leurs arômes fruités."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le rôle du 'tire-bouchon' à deux leviers (ou sommelier) lors de l'ouverture d'une bouteille de vin ?",
                    "answerOptions": [
                        {"text": "Couper la capsule.", "isCorrect": False},
                        {"text": "Faciliter l'extraction du bouchon sans le casser.", "isCorrect": True},
                        {"text": "Dégazer le vin.", "isCorrect": False},
                        {"text": "Mesurer la température.", "isCorrect": False}
                    ],
                    "correction": "Le **tire-bouchon sommelier** permet une extraction en deux temps, réduisant la force nécessaire et le risque de casser le bouchon (ou de faire du bruit) par rapport à un tire-bouchon simple."
                },
                {
                    "questionNumber": 43,
                    "question": "Que signifie l'opération de 'chambrer' un vin ?",
                    "answerOptions": [
                        {"text": "Le mettre en bouteille.", "isCorrect": False},
                        {"text": "L'aérer dans une carafe (décantation).", "isCorrect": False},
                        {"text": "Le réchauffer progressivement à la température de la pièce (ou à la température de service idéale pour un rouge, souvent 16-18°C).", "isCorrect": True},
                        {"text": "Le mettre au frais.", "isCorrect": False}
                    ],
                    "correction": "**Chambrer** signifie ajuster le vin à une température idéale (souvent de 16°C à 18°C pour les rouges structurés) pour qu'il exprime tous ses arômes. Cela ne signifie pas la température ambiante de l'établissement (souvent trop chaude)."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le rôle du 'décanteur' (ou carafe à vin) ?",
                    "answerOptions": [
                        {"text": "Filtrer le vin.", "isCorrect": False},
                        {"text": "Séparer le vin de son dépôt (sédiment) et l'aérer pour libérer ses arômes (ou les adoucir).", "isCorrect": True},
                        {"text": "Refroidir le vin rapidement.", "isCorrect": False},
                        {"text": "Le mélanger à de l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le décanteur a deux fonctions : **décanter** (séparer le dépôt) pour les vieux vins, et **aérer** (oxygéner) les jeunes vins puissants pour les rendre plus souples."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment s'appelle l'opérateur spécialisé dans la connaissance et le service des vins ?",
                    "answerOptions": [
                        {"text": "Le Maître d'hôtel.", "isCorrect": False},
                        {"text": "Le Barman.", "isCorrect": False},
                        {"text": "Le Sommelier (ou Caviste).", "isCorrect": True},
                        {"text": "Le Chef de rang.", "isCorrect": False}
                    ],
                    "correction": "Le **sommelier** est l'expert en vins, spiritueux et boissons. Il conseille les clients, gère la cave et est responsable du service du vin."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel alcool est la base principale du cocktail 'Mojito' ?",
                    "answerOptions": [
                        {"text": "Le Rhum blanc (ou léger).", "isCorrect": True},
                        {"text": "La Vodka.", "isCorrect": False},
                        {"text": "Le Gin.", "isCorrect": False},
                        {"text": "La Tequila.", "isCorrect": False}
                    ],
                    "correction": "Le Mojito est composé de **Rhum blanc**, de menthe fraîche, de sucre de canne, de citron vert et d'eau gazeuse."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on le verre sans pied, avec un fond épais, souvent utilisé pour les spiritueux servis 'on the rocks' (sur glace) ?",
                    "answerOptions": [
                        {"text": "Verre à dégustation (Inao).", "isCorrect": False},
                        {"text": "Verre Old-fashioned (ou tumbler bas).", "isCorrect": True},
                        {"text": "Flûte à champagne.", "isCorrect": False},
                        {"text": "Verre à Martini.", "isCorrect": False}
                    ],
                    "correction": "Le verre **Old-fashioned** (ou tumbler) est idéal pour les boissons nécessitant une grande quantité de glace, comme le Whisky ou les cocktails courts."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'ingrédient de base pour la fabrication de la bière ?",
                    "answerOptions": [
                        {"text": "Le raisin.", "isCorrect": False},
                        {"text": "L'orge malté (principalement), l'eau, le houblon et la levure.", "isCorrect": True},
                        {"text": "Le seigle.", "isCorrect": False},
                        {"text": "Le maïs.", "isCorrect": False}
                    ],
                    "correction": "L'**orge malté** apporte l'amidon (transformé en sucre), le **houblon** apporte l'amertume et les arômes, la **levure** permet la fermentation, et l'**eau** constitue la majorité du volume."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le risque de servir un vin rouge puissant à une température trop élevée (ex : 25°C) ?",
                    "answerOptions": [
                        {"text": "Les arômes fruités vont disparaître.", "isCorrect": False},
                        {"text": "L'alcool et l'acidité seront trop dominants et déséquilibrés.", "isCorrect": True},
                        {"text": "Le vin ne sera plus rouge.", "isCorrect": False},
                        {"text": "Il n'y a aucun risque.", "isCorrect": False}
                    ],
                    "correction": "Un vin rouge servi trop chaud devient 'lourd', **l'alcool prend le dessus** (effet 'tête'), et la finesse des arômes est perdue. Il perd également en fraîcheur et en équilibre."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est l'effet d'une trop forte pression d'extraction sur un café Espresso ?",
                    "answerOptions": [
                        {"text": "Le café sera trop clair.", "isCorrect": False},
                        {"text": "Le café sera sous-extrait (goût acide).", "isCorrect": False},
                        {"text": "Le café sera sur-extrait (goût amer et brûlé) avec une 'crema' trop foncée.", "isCorrect": True},
                        {"text": "Le café sera trop sucré.", "isCorrect": False}
                    ],
                    "correction": "Une extraction trop longue ou avec une pression/température trop élevée brûle la mouture et extrait des composés amers (sur-extraction). Un bon espresso est extrait en 20 à 30 secondes."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel terme œnologique est utilisé pour décrire l'arrière-goût d'un vin en bouche après qu'il a été avalé (en secondes) ?",
                    "answerOptions": [
                        {"text": "L'attaque.", "isCorrect": False},
                        {"text": "Le nez.", "isCorrect": False},
                        {"text": "La longueur en bouche (ou Persistance Aromatique Intense - PAI).", "isCorrect": True},
                        {"text": "La robe.", "isCorrect": False}
                    ],
                    "correction": "La **longueur en bouche** (PAI) est un critère de qualité. Plus un vin est long, plus ses arômes persistent après la dégustation, indiquant une meilleure complexité."
                },
                {
                    "questionNumber": 52,
                    "question": "Qu'est-ce qu'un 'Digestif' ?",
                    "answerOptions": [
                        {"text": "Une boisson très sucrée servie avant le repas.", "isCorrect": False},
                        {"text": "Une boisson alcoolisée servie en fin de repas pour aider à la digestion (ex : Cognac, Armagnac).", "isCorrect": True},
                        {"text": "Un type de café sans alcool.", "isCorrect": False},
                        {"text": "Un type de vin mousseux.", "isCorrect": False}
                    ],
                    "correction": "Le **digestif** est une boisson spiritueuse (souvent à haute teneur en alcool) servie après le dessert, historiquement censée 'couper' l'estomac et faciliter la digestion. L'**Apéritif** est servi avant le repas."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est l'une des erreurs fréquentes lors du service du Champagne ?",
                    "answerOptions": [
                        {"text": "Le servir dans des verres à vin blanc.", "isCorrect": False},
                        {"text": "Le servir à température ambiante.", "isCorrect": False},
                        {"text": "Laisser la bouteille fumer (trop froide) et faire sauter le bouchon de manière spectaculaire.", "isCorrect": True},
                        {"text": "Le servir dans une flûte.", "isCorrect": False}
                    ],
                    "correction": "Le bouchon doit être extrait **silencieusement** et progressivement pour éviter de perdre le gaz carbonique et pour respecter l'étiquette. La bouteille ne doit pas 'fumer' (trop froid, risque de perte d'arômes)."
                },
                {
                    "questionNumber": 54,
                    "question": "La température idéale de conservation d'une bouteille de vin dans une cave professionnelle est d'environ :",
                    "answerOptions": [
                        {"text": "25°C.", "isCorrect": False},
                        {"text": "10°C à 14°C (Température stable).", "isCorrect": True},
                        {"text": "0°C.", "isCorrect": False},
                        {"text": "30°C.", "isCorrect": False}
                    ],
                    "correction": "Une température de conservation **stable** (idéalement entre 10°C et 14°C) est essentielle pour la bonne évolution du vin. Les variations brusques de température sont nuisibles."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est la principale différence entre une eau de source et une eau minérale naturelle ?",
                    "answerOptions": [
                        {"text": "Il n'y en a aucune.", "isCorrect": False},
                        {"text": "L'eau de source est moins chère.", "isCorrect": False},
                        {"text": "L'eau minérale a des propriétés minérales reconnues et une composition stable, alors que l'eau de source n'a pas d'exigence de stabilité de composition.", "isCorrect": True},
                        {"text": "L'eau minérale est gazeuse.", "isCorrect": False}
                    ],
                    "correction": "L'**eau minérale naturelle** est reconnue par l'Académie de médecine pour ses bénéfices santé et a une composition minérale garantie et stable. L'eau de source n'a pas cette obligation."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le rôle du 'zeste' (la peau) d'un agrume dans la préparation d'un cocktail (ex : Old Fashioned) ?",
                    "answerOptions": [
                        {"text": "Aider à la dilution.", "isCorrect": False},
                        {"text": "Apporter des huiles essentielles (arômes) par pression au-dessus du verre.", "isCorrect": True},
                        {"text": "Colorer la boisson.", "isCorrect": False},
                        {"text": "Servir de glaçon.", "isCorrect": False}
                    ],
                    "correction": "Le zeste apporte des **huiles essentielles aromatiques** qui sont activées en le pressant légèrement au-dessus du verre, puis en le déposant dans la boisson."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'est-ce qu'un 'Vin de Pays' (ou Indication Géographique Protégée - IGP) ?",
                    "answerOptions": [
                        {"text": "Un vin sans aucune réglementation.", "isCorrect": False},
                        {"text": "Un vin avec une réglementation moins stricte que l'AOC, mais qui garantit une origine géographique.", "isCorrect": True},
                        {"text": "Un vin non alcoolisé.", "isCorrect": False},
                        {"text": "Un vin qui doit vieillir au moins 10 ans.", "isCorrect": False}
                    ],
                    "correction": "L'**IGP** (ou Vin de Pays) garantit que le vin est issu d'une zone géographique délimitée, mais avec un cahier des charges moins contraignant que l'AOP (Appellation d'Origine Protégée)."
                },
                {
                    "questionNumber": 58,
                    "question": "Pourquoi la bière doit-elle être servie dans un verre parfaitement propre et rincé ?",
                    "answerOptions": [
                        {"text": "Pour des raisons de goût.", "isCorrect": False},
                        {"text": "Pour que le col (la mousse) soit stable et adhère bien aux parois du verre.", "isCorrect": True},
                        {"text": "Pour qu'elle soit plus froide.", "isCorrect": False},
                        {"text": "Pour que la bière soit moins alcoolisée.", "isCorrect": False}
                    ],
                    "correction": "La saleté ou les résidus de graisse empêchent la **mousse** de se former correctement (elle s'écroule) ou d'adhérer aux parois, nuisant à l'expérience de dégustation et à l'esthétique."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le terme désignant le mélange d'un alcool et d'une boisson non alcoolisée (jus, soda) servi dans un verre long, souvent avec de la glace ?",
                    "answerOptions": [
                        {"text": "Un Shot.", "isCorrect": False},
                        {"text": "Un Pousse-Café.", "isCorrect": False},
                        {"text": "Un Long Drink.", "isCorrect": True},
                        {"text": "Un Pur Malt.", "isCorrect": False}
                    ],
                    "correction": "Un **Long Drink** est une boisson à servir dans un grand verre (tumbler haut) avec une quantité importante de mélangeur, souvent une version allongée d'un cocktail (ex : Gin Tonic)."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le vin idéal pour accompagner la majorité des desserts au chocolat noir ?",
                    "answerOptions": [
                        {"text": "Un vin blanc sec et très frais (Sancerre).", "isCorrect": False},
                        {"text": "Un vin rouge léger (Beaujolais).", "isCorrect": False},
                        {"text": "Un vin rouge doux naturel (Banyuls, Maury) ou un Porto.", "isCorrect": True},
                        {"text": "Du Champagne sec.", "isCorrect": False}
                    ],
                    "correction": "Le chocolat noir nécessite un vin qui a suffisamment de **puissance** et de **sucre résiduel** pour ne pas être masqué. Les **Vins Doux Naturels** ou les vins mutés (Porto, Madère) sont souvent la meilleure option."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : COMMERCIALISATION ET RELATION CLIENT (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Commercialisation et Relation Client (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Comment appelle-t-on le fait de suggérer un produit plus cher ou de meilleure qualité que celui choisi initialement par le client (dans un but commercial) ?",
                    "answerOptions": [
                        {"text": "Le 'check-back'.", "isCorrect": False},
                        {"text": "L'Up-selling (ou Montée en gamme).", "isCorrect": True},
                        {"text": "Le Cross-selling.", "isCorrect": False},
                        {"text": "Le No-show.", "isCorrect": False}
                    ],
                    "correction": "L'**Up-selling** (ou Montée en gamme) est une technique de vente où l'on propose un produit supérieur (ex : un vin plus prestigieux que celui initialement demandé). Il doit toujours rester une suggestion et non une insistance."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la première chose que le serveur doit faire lorsqu'un client exprime clairement une plainte (plat froid, erreur) ?",
                    "answerOptions": [
                        {"text": "Se justifier et accuser la cuisine.", "isCorrect": False},
                        {"text": "Écouter attentivement, présenter des excuses sincères et proposer immédiatement une solution (remplacement du plat, geste commercial).", "isCorrect": True},
                        {"text": "Appeler le gérant sans rien dire.", "isCorrect": False},
                        {"text": "Lui proposer l'addition.", "isCorrect": False}
                    ],
                    "correction": "La gestion des plaintes commence par l'**écoute** et l'**empathie**. S'excuser ne signifie pas admettre la faute, mais reconnaître l'insatisfaction du client. Il faut ensuite agir rapidement."
                },
                {
                    "questionNumber": 63,
                    "question": "Que signifie 'Cross-selling' (ou Vente complémentaire) en restauration ?",
                    "answerOptions": [
                        {"text": "Vendre des produits d'un autre restaurant.", "isCorrect": False},
                        {"text": "Suggérer des produits qui se marient bien avec l'achat principal (ex : un digestif après le café, des frites avec le burger).", "isCorrect": True},
                        {"text": "Vendre en ligne.", "isCorrect": False},
                        {"text": "Ne rien vendre du tout.", "isCorrect": False}
                    ],
                    "correction": "Le **Cross-selling** est la suggestion d'un produit additionnel qui complète l'expérience. C'est une technique courante pour augmenter le panier moyen (ex : 'Souhaitez-vous un accompagnement avec votre viande ?')."
                },
                {
                    "questionNumber": 64,
                    "question": "Le 'Briefing' de début de service a pour but principal de :",
                    "answerOptions": [
                        {"text": "Distribuer les pourboires.", "isCorrect": False},
                        {"text": "Rappeler les consignes du jour (menus, ruptures de stock, réservations spéciales) et motiver l'équipe.", "isCorrect": True},
                        {"text": "Nettoyer les tables.", "isCorrect": False},
                        {"text": "Prendre les réservations de la journée.", "isCorrect": False}
                    ],
                    "correction": "Le **briefing** est la réunion d'équipe juste avant le service. Il assure que tout le monde est au courant des particularités du jour (produits manquants, plats du jour, grands groupes) pour éviter les erreurs en salle."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel terme désigne un client qui a réservé, mais qui ne s'est pas présenté et n'a pas annulé sa table ?",
                    "answerOptions": [
                        {"text": "Un walk-in.", "isCorrect": False},
                        {"text": "Un no-show.", "isCorrect": True},
                        {"text": "Un check-back.", "isCorrect": False},
                        {"text": "Un up-seller.", "isCorrect": False}
                    ],
                    "correction": "Un **No-show** (absentéisme) est très pénalisant pour l'établissement car il représente un manque à gagner. Certains restaurants demandent des empreintes de carte bancaire pour facturer les no-shows."
                },
                {
                    "questionNumber": 66,
                    "question": "Quelle information essentielle doit contenir un bon de commande (ou 'bons') de salle pour la cuisine ?",
                    "answerOptions": [
                        {"text": "Le nom du client.", "isCorrect": False},
                        {"text": "Le numéro de table, l'heure de la commande, le détail précis des plats et les spécificités (cuisson, allergies).", "isCorrect": True},
                        {"text": "Le prix total de la commande.", "isCorrect": False},
                        {"text": "La recette du plat.", "isCorrect": False}
                    ],
                    "correction": "Le **bon de commande** est le lien entre la salle et la cuisine. Il doit être précis pour éviter les erreurs de dressage, de cuisson ou les oublis d'allergènes."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la principale différence entre une 'Carte' et un 'Menu' ?",
                    "answerOptions": [
                        {"text": "La Carte est en cuir, le Menu est en papier.", "isCorrect": False},
                        {"text": "La Carte liste les plats à l'unité (choix à la carte), tandis que le Menu est une sélection de plats à prix fixe (formule).", "isCorrect": True},
                        {"text": "Le Menu ne propose que des desserts.", "isCorrect": False},
                        {"text": "La Carte ne propose que des boissons.", "isCorrect": False}
                    ],
                    "correction": "La **Carte** offre la liberté de choix. Le **Menu** est un forfait (entrée-plat-dessert) à un prix prédéfini, souvent utilisé pour les déjeuners rapides ou les événements."
                },
                {
                    "questionNumber": 68,
                    "question": "En cas de forte affluence ('coup de feu'), quelle doit être l'attitude prioritaire du personnel de salle ?",
                    "answerOptions": [
                        {"text": "Travailler plus lentement pour éviter les erreurs.", "isCorrect": False},
                        {"text": "Maintenir le calme, communiquer clairement avec la cuisine et prioriser les actions urgentes (prendre la commande, servir les plats chauds).", "isCorrect": True},
                        {"text": "Prendre une pause pour se reposer.", "isCorrect": False},
                        {"text": "Accuser les clients d'être en retard.", "isCorrect": False}
                    ],
                    "correction": "Le **calme** et la **communication** sont cruciaux en période de stress (coup de feu). L'objectif est de ne pas laisser les clients attendre trop longtemps, tout en maintenant la qualité."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel type d'information est obligatoire de mentionner sur les cartes des boissons (en France) ?",
                    "answerOptions": [
                        {"text": "Le nom du fournisseur.", "isCorrect": False},
                        {"text": "Le volume des boissons, le prix de vente et la mention des allergènes (le cas échéant).", "isCorrect": True},
                        {"text": "La date d'embouteillage.", "isCorrect": False},
                        {"text": "La photo de la boisson.", "isCorrect": False}
                    ],
                    "correction": "L'affichage des **prix et volumes** est une obligation légale. La mention des allergènes (même dans les boissons, ex : bière) est également requise."
                },
                {
                    "questionNumber": 70,
                    "question": "Lorsque le client hésite entre deux plats, quelle est la meilleure technique de vente pour l'aider à choisir ?",
                    "answerOptions": [
                        {"text": "Lui dire que les deux plats sont bons.", "isCorrect": False},
                        {"text": "Lui décrire les plats de manière sensorielle et lui demander quel est son goût du moment (viande rouge, poisson, épices).", "isCorrect": True},
                        {"text": "Lui imposer le plat le plus cher.", "isCorrect": False},
                        {"text": "Ne rien dire et attendre.", "isCorrect": False}
                    ],
                    "correction": "Le serveur doit être un **conseiller**. La description précise (texture, saveurs, arômes) et le questionnement sur les préférences guident le client vers le choix le plus approprié (service personnalisé)."
                },
                {
                    "questionNumber": 71,
                    "question": "Le sourire et le contact visuel sont essentiels lors de l'accueil. Quel terme professionnel résume l'importance de ces éléments ?",
                    "answerOptions": [
                        {"text": "Le 'décrochage'.", "isCorrect": False},
                        {"text": "Le 'premier contact' (première impression).", "isCorrect": True},
                        {"text": "L'encaissement.", "isCorrect": False},
                        {"text": "La mise en place.", "isCorrect": False}
                    ],
                    "correction": "Le **premier contact** est crucial. Il donne le ton de l'expérience client. Le serveur doit être accueillant, poli et disponible."
                },
                {
                    "questionNumber": 72,
                    "question": "Lorsqu'un client demande de modifier un plat (ex : 'pas de sauce'), que doit faire le serveur ?",
                    "answerOptions": [
                        {"text": "Refuser poliment.", "isCorrect": False},
                        {"text": "Vérifier la faisabilité auprès de la cuisine et le noter clairement sur le bon de commande.", "isCorrect": True},
                        {"text": "Accepter sans vérifier.", "isCorrect": False},
                        {"text": "Demander l'addition.", "isCorrect": False}
                    ],
                    "correction": "Les modifications sont courantes (allergies, préférences). La **vérification** en cuisine est essentielle, ainsi que la transmission claire de l'information (mention 'Sans sauce' ou 'Allergie X') pour garantir la satisfaction."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le but d'une 'fiche technique' de plat ou de cocktail ?",
                    "answerOptions": [
                        {"text": "Servir de mode d'emploi pour le client.", "isCorrect": False},
                        {"text": "Standardiser la préparation, garantir le coût (matière première) et la qualité constante du produit.", "isCorrect": True},
                        {"text": "Servir d'addition.", "isCorrect": False},
                        {"text": "Calculer la TVA.", "isCorrect": False}
                    ],
                    "correction": "La **fiche technique** assure que le plat/cocktail sera toujours fait avec les mêmes ingrédients, les mêmes quantités et la même méthode, ce qui garantit la rentabilité et l'expérience client."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle est l'importance de la tenue professionnelle (uniforme) pour le personnel de salle ?",
                    "answerOptions": [
                        {"text": "Uniquement pour le style.", "isCorrect": False},
                        {"text": "Elle reflète l'image de l'établissement (professionnalisme) et facilite l'identification par le client.", "isCorrect": True},
                        {"text": "Elle protège des brûlures.", "isCorrect": False},
                        {"text": "Elle n'a aucune importance.", "isCorrect": False}
                    ],
                    "correction": "L'uniforme participe à l'**image de marque**. Une tenue soignée, propre et adaptée montre le sérieux de l'établissement et permet au client d'identifier facilement son interlocuteur."
                },
                {
                    "questionNumber": 75,
                    "question": "Lors de l'encaissement par carte bancaire (TPE), quelle est la vérification que le serveur doit toujours effectuer ?",
                    "answerOptions": [
                        {"text": "Vérifier la couleur de la carte.", "isCorrect": False},
                        {"text": "S'assurer que le montant affiché sur le terminal est le même que celui de l'addition.", "isCorrect": True},
                        {"text": "Demander le code PIN du client.", "isCorrect": False},
                        {"text": "S'assurer que le client est le propriétaire de la carte.", "isCorrect": False}
                    ],
                    "correction": "La vérification du **montant** sur le TPE (Terminal de Paiement Électronique) et l'addition évite les erreurs de saisie qui peuvent frustrer le client et pénaliser l'établissement."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est l'objectif de la 'vente suggestive' ?",
                    "answerOptions": [
                        {"text": "Vendre ce que l'on ne veut plus.", "isCorrect": False},
                        {"text": "Augmenter la satisfaction client et le chiffre d'affaires en proposant des produits adaptés (ex : fromages, desserts).", "isCorrect": True},
                        {"text": "Forcer le client à acheter.", "isCorrect": False},
                        {"text": "Diminuer le temps de service.", "isCorrect": False}
                    ],
                    "correction": "La **vente suggestive** (Up-selling ou Cross-selling) est l'art de conseiller le client tout en augmentant le panier moyen. Elle doit toujours être faite au bon moment et de manière pertinente."
                },
                {
                    "questionNumber": 77,
                    "question": "Comment doit-on accueillir un client qui n'a pas réservé (un 'walk-in') lors d'un service complet ?",
                    "answerOptions": [
                        {"text": "Le renvoyer immédiatement.", "isCorrect": False},
                        {"text": "L'accueillir poliment, s'excuser pour l'attente ou la non-disponibilité, et lui proposer une solution alternative (ex : attendre au bar, prendre à emporter, proposer une autre heure).", "isCorrect": True},
                        {"text": "Lui mentir sur le temps d'attente.", "isCorrect": False},
                        {"text": "Lui proposer une table sale.", "isCorrect": False}
                    ],
                    "correction": "Même s'il n'y a pas de place, le client doit se sentir **respecté**. Proposer une alternative (bar, autre heure) permet de transformer une frustration en expérience positive (ou de le fidéliser pour une prochaine fois)."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel document est l'outil principal pour gérer les réservations de tables ?",
                    "answerOptions": [
                        {"text": "La fiche de paie.", "isCorrect": False},
                        {"text": "Le plan de salle (manuel ou numérique) et le cahier de réservation.", "isCorrect": True},
                        {"text": "Le livre de cuisine.", "isCorrect": False},
                        {"text": "Le menu du jour.", "isCorrect": False}
                    ],
                    "correction": "Le **plan de salle** (ou le logiciel de réservation) est indispensable pour visualiser les tables disponibles, les attribuer efficacement et éviter les doubles réservations ou les attentes inutiles."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le pourcentage de TVA appliqué en France sur les boissons alcoolisées (à consommer sur place ou à emporter) ?",
                    "answerOptions": [
                        {"text": "5,5% (Taux réduit).", "isCorrect": False},
                        {"text": "10% (Taux intermédiaire).", "isCorrect": False},
                        {"text": "20% (Taux normal).", "isCorrect": True},
                        {"text": "2,1% (Taux super-réduit).", "isCorrect": False}
                    ],
                    "correction": "La **TVA à 20%** s'applique aux boissons alcoolisées, aux produits non destinés à la consommation immédiate (ex : confiserie) et aux produits de luxe. Le taux de 10% s'applique à la nourriture à consommer sur place."
                },
                {
                    "questionNumber": 80,
                    "question": "La fin du repas et le départ du client est une opportunité pour le serveur de :",
                    "answerOptions": [
                        {"text": "Lui demander de partir vite.", "isCorrect": False},
                        {"text": "Remercier le client, l'inviter à revenir et l'accompagner jusqu'à la sortie (fidélisation).", "isCorrect": True},
                        {"text": "Lui demander son numéro de téléphone.", "isCorrect": False},
                        {"text": "Le faire payer le pourboire.", "isCorrect": False}
                    ],
                    "correction": "Le **départ** est le dernier moment d'interaction. Un au revoir chaleureux et un remerciement renforcent l'image positive et encouragent la fidélité."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : ÉQUIPEMENTS ET ORGANISATION DU TRAVAIL (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Équipements et Organisation du Travail (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Comment appelle-t-on le poste de travail aménagé en salle (ou près de la salle) pour stocker les couverts, la vaisselle de rechange, les serviettes et le matériel de service ?",
                    "answerOptions": [
                        {"text": "La plonge.", "isCorrect": False},
                        {"text": "Le passe.", "isCorrect": False},
                        {"text": "Le buffet de service (ou commode, ou office).", "isCorrect": True},
                        {"text": "La caisse.", "isCorrect": False}
                    ],
                    "correction": "L'**office** (ou buffet de service) est la station de travail du serveur, indispensable pour la 'mise en place' de dernière minute et le réassort rapide."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le rôle du 'Chef de Rang' ?",
                    "answerOptions": [
                        {"text": "Superviser uniquement la plonge.", "isCorrect": False},
                        {"text": "Être responsable d'un groupe de tables ('rang'), diriger le commis et assurer la continuité du service sur son secteur.", "isCorrect": True},
                        {"text": "Être le responsable unique de tout l'établissement.", "isCorrect": False},
                        {"text": "Faire la cuisine.", "isCorrect": False}
                    ],
                    "correction": "Le **Chef de Rang** est le poste clé de la salle. Il est le manager de proximité, responsable de son secteur et de la formation des commis."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel équipement est utilisé pour maintenir les plats chauds à la bonne température pendant leur transfert de la cuisine à la salle ?",
                    "answerOptions": [
                        {"text": "La friteuse.", "isCorrect": False},
                        {"text": "Le chauffe-plat (ou lampe chauffante de passe) ou la cloche.", "isCorrect": True},
                        {"text": "Le réfrigérateur.", "isCorrect": False},
                        {"text": "Le décanteur.", "isCorrect": False}
                    ],
                    "correction": "Les plats doivent être servis à une température supérieure à 63°C. Une **cloche** (couvercle) ou un **chauffe-plat** (ou une assiette chauffée) sont essentiels pour limiter la perte de chaleur."
                },
                {
                    "questionNumber": 84,
                    "question": "Dans l'organisation de la salle, qu'est-ce qu'un 'Commis de Salle' ?",
                    "answerOptions": [
                        {"text": "Le responsable de l'encaissement.", "isCorrect": False},
                        {"text": "Un serveur qualifié avec beaucoup d'expérience.", "isCorrect": False},
                        {"text": "Un apprenti ou assistant chargé d'aider le Chef de Rang (débarrassage, mise en place).", "isCorrect": True},
                        {"text": "Le gérant du restaurant.", "isCorrect": False}
                    ],
                    "correction": "Le **Commis de Salle** est un poste d'apprentissage et de soutien. Il réalise les tâches de support (débarrassage, réassort, nettoyage) pour laisser le Chef de Rang se concentrer sur le service au client."
                },
                {
                    "questionNumber": 85,
                    "question": "Pourquoi la vaisselle doit-elle être triée et pré-débarrassée (les restes jetés) avant d'entrer au lave-vaisselle (plonge) ?",
                    "answerOptions": [
                        {"text": "Pour des raisons de place.", "isCorrect": False},
                        {"text": "Pour ne pas encrasser l'eau de lavage et les filtres, et garantir l'hygiène du lavage.", "isCorrect": True},
                        {"text": "Pour gagner du temps au lavage.", "isCorrect": False},
                        {"text": "Pour la faire sécher plus vite.", "isCorrect": False}
                    ],
                    "correction": "Le **pré-débarrassage** est essentiel. Les gros déchets alimentaires bouchent les filtres et polluent l'eau du lave-vaisselle, nuisant à la qualité de désinfection de la vaisselle propre."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le rôle de la 'Marmite' (ou Timbale) à glace utilisée pour le service du vin ?",
                    "answerOptions": [
                        {"text": "Refroidir les couverts.", "isCorrect": False},
                        {"text": "Maintenir les bouteilles (vins blancs, rosés, champagnes) à la bonne température de service pendant le repas.", "isCorrect": True},
                        {"text": "Préparer des cocktails.", "isCorrect": False},
                        {"text": "Servir le café.", "isCorrect": False}
                    ],
                    "correction": "La **marmite** (ou seau à glace) sert à maintenir la température basse, en général remplie d'eau et de glace, car la glace seule ne permet pas un contact uniforme avec la bouteille."
                },
                {
                    "questionNumber": 87,
                    "question": "Dans le contexte de l'hygiène, qu'est-ce qu'un 'marquage des tables' ?",
                    "answerOptions": [
                        {"text": "Marquer la couleur des nappes.", "isCorrect": False},
                        {"text": "L'identification claire et permanente des tables (souvent par un numéro) pour la prise de commande et la livraison des plats.", "isCorrect": True},
                        {"text": "Laisser une marque sur les verres.", "isCorrect": False},
                        {"text": "Réserver une table.", "isCorrect": False}
                    ],
                    "correction": "Le **marquage des tables** (numérotation) est la base de l'organisation en salle. Il est essentiel pour éviter les erreurs de service et le gaspillage de temps."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'une 'Addition Provisoire' (ou Bon de caisse) ?",
                    "answerOptions": [
                        {"text": "L'addition finale.", "isCorrect": False},
                        {"text": "L'addition payée.", "isCorrect": False},
                        {"text": "Le récapitulatif des consommations à l'instant T, utilisé pour le suivi ou le paiement partiel.", "isCorrect": True},
                        {"text": "La fiche de stock.", "isCorrect": False}
                    ],
                    "correction": "L'**addition provisoire** (ou pré-addition) permet de vérifier les consommations avant de procéder à l'encaissement final et d'éviter les oublis ou les erreurs."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le rôle du 'passe' (ou office de distribution) ?",
                    "answerOptions": [
                        {"text": "La zone où les clients attendent.", "isCorrect": False},
                        {"text": "La zone de transition entre la cuisine et la salle où les plats sont vérifiés, clochés et attendent le départ en salle.", "isCorrect": True},
                        {"text": "Le lieu de stockage des couverts.", "isCorrect": False},
                        {"text": "La zone de lavage de la vaisselle.", "isCorrect": False}
                    ],
                    "correction": "Le **passe** est le point de contrôle final. Le Chef de Rang (ou le Maître d'Hôtel) s'assure que le plat est correct (dressage, température, spécificités) avant qu'il ne soit emmené au client."
                },
                {
                    "questionNumber": 90,
                    "question": "Comment s'appelle l'art de faire le service du vin (l'ensemble des gestes et connaissances du sommelier) ?",
                    "answerOptions": [
                        {"text": "Le dégazage.", "isCorrect": False},
                        {"text": "L'œnologie.", "isCorrect": False},
                        {"text": "La Sommellerie.", "isCorrect": True},
                        {"text": "La cuisine.", "isCorrect": False}
                    ],
                    "correction": "La **Sommellerie** englobe la connaissance des vins, le conseil client, la gestion de cave et l'ensemble des techniques de service (ouverture, décantation, température)."
                },
                {
                    "questionNumber": 91,
                    "question": "Qu'est-ce que le 'coup de feu' ?",
                    "answerOptions": [
                        {"text": "Un plat épicé.", "isCorrect": False},
                        {"text": "La période de pointe où l'activité est maximale (rush de commandes).", "isCorrect": True},
                        {"text": "Un incident de cuisine.", "isCorrect": False},
                        {"text": "Le fait de jeter de l'eau sur une flamme.", "isCorrect": False}
                    ],
                    "correction": "Le **coup de feu** (souvent entre 12h30 et 14h00 ou 20h00 et 22h00) est la période de stress maximal où une organisation sans faille est requise pour assurer la rapidité du service."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est l'outil utilisé pour prendre la température d'un plat chaud (traçabilité HACCP) ?",
                    "answerOptions": [
                        {"text": "Le thermomètre à vin.", "isCorrect": False},
                        {"text": "Le thermomètre sonde électronique (avec désinfection après usage).", "isCorrect": True},
                        {"text": "Le densimètre.", "isCorrect": False},
                        {"text": "Le baromètre.", "isCorrect": False}
                    ],
                    "correction": "Le **thermomètre sonde** permet de vérifier la température à cœur de l'aliment pour s'assurer qu'elle est hors zone de danger (+63°C pour le chaud, ou -18°C pour le froid négatif)."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est l'outil principal utilisé par le serveur pour le nettoyage de la salle entre deux services ?",
                    "answerOptions": [
                        {"text": "Le Kärcher.", "isCorrect": False},
                        {"text": "Le balai et la serpillière (ou aspirateur) avec des produits de nettoyage professionnels.", "isCorrect": True},
                        {"text": "Le couteau d'office.", "isCorrect": False},
                        {"text": "Le ramasse-miettes.", "isCorrect": False}
                    ],
                    "correction": "Le nettoyage des sols et des surfaces est une part importante de la 'mise en place' et de la propreté générale de l'établissement (image et hygiène)."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle est la principale fonction d'un 'Chariot de fromages' ou de 'Desserts' ?",
                    "answerOptions": [
                        {"text": "Stocker la vaisselle sale.", "isCorrect": False},
                        {"text": "Présenter l'offre de manière visible et séduisante au client, favorisant la vente suggestive.", "isCorrect": True},
                        {"text": "Servir le café.", "isCorrect": False},
                        {"text": "Débarrasser les verres.", "isCorrect": False}
                    ],
                    "correction": "Le chariot est un outil de **vente suggestive** haut de gamme. La présentation visuelle des produits frais (fromages, desserts) est très efficace pour déclencher l'achat."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le risque de prendre une assiette très chaude à mains nues (sans 'liseron' ou 'torchon') ?",
                    "answerOptions": [
                        {"text": "La chute de l'assiette.", "isCorrect": False},
                        {"text": "Une brûlure (risque de sécurité).", "isCorrect": True},
                        {"text": "Une mauvaise adhérence.", "isCorrect": False},
                        {"text": "Le plat refroidit trop vite.", "isCorrect": False}
                    ],
                    "correction": "Les assiettes sortant du passe ou du chauffe-assiette peuvent être très chaudes. Le serveur doit utiliser un **torchon** (liseron) pour se protéger les mains et assurer un service sécurisé."
                },
                {
                    "questionNumber": 96,
                    "question": "Que signifie 'filer' une table ?",
                    "answerOptions": [
                        {"text": "La faire payer.", "isCorrect": False},
                        {"text": "La réserver.", "isCorrect": False},
                        {"text": "La nettoyer et la remettre en place intégralement dès que le client est parti.", "isCorrect": True},
                        {"text": "La masquer.", "isCorrect": False}
                    ],
                    "correction": "**Filer une table** (ou la 're-filer') est le fait de la remettre à l'état initial (propre, nappée, mise en place) le plus rapidement possible pour accueillir les clients suivants."
                },
                {
                    "questionNumber": 97,
                    "question": "Pourquoi est-il important de faire la 'rotation des stocks' selon le principe FIFO (First In, First Out) ?",
                    "answerOptions": [
                        {"text": "Pour que les nouveaux produits soient devant.", "isCorrect": False},
                        {"text": "Pour minimiser le gaspillage et garantir que les produits dont la DLC est la plus courte soient utilisés en premier.", "isCorrect": True},
                        {"text": "Pour que les produits soient plus frais.", "isCorrect": False},
                        {"text": "Pour augmenter le prix.", "isCorrect": False}
                    ],
                    "correction": "Le **FIFO** (Premier entré, Premier sorti) est la règle de base de la gestion des stocks. Elle garantit l'utilisation des produits avant leur DLC, réduisant les pertes et assurant la fraîcheur."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est l'outil indispensable au serveur pour communiquer efficacement les plats de la cuisine à la table (à part le bon de commande) ?",
                    "answerOptions": [
                        {"text": "Le téléphone.", "isCorrect": False},
                        {"text": "Sa mémoire.", "isCorrect": False},
                        {"text": "Le support de transport (Plateau) et le 'liseron' (torchon).", "isCorrect": True},
                        {"text": "La carte.", "isCorrect": False}
                    ],
                    "correction": "Le **plateau** permet de transporter de manière sûre plusieurs assiettes ou verres. Le **liseron** (torchon) est essentiel pour porter les assiettes chaudes et essuyer les bords des verres/assiettes."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le rôle du 'Maître d'Hôtel' dans un grand établissement ?",
                    "answerOptions": [
                        {"text": "Faire la plonge.", "isCorrect": False},
                        {"text": "Coordonner l'ensemble du personnel de salle, accueillir les clients, gérer les réservations et le plan de salle.", "isCorrect": True},
                        {"text": "Être le responsable du bar.", "isCorrect": False},
                        {"text": "Cuisiner les plats du jour.", "isCorrect": False}
                    ],
                    "correction": "Le **Maître d'Hôtel** est le chef d'orchestre de la salle. Il est le garant de la qualité de service et de l'expérience client globale."
                },
                {
                    "questionNumber": 100,
                    "question": "Que représente la 'vestiaire' dans l'organisation de l'accueil ?",
                    "answerOptions": [
                        {"text": "La cave à vin.", "isCorrect": False},
                        {"text": "Le lieu où les clients peuvent laisser leurs manteaux et effets personnels.", "isCorrect": True},
                        {"text": "La zone de stockage des nappes.", "isCorrect": False},
                        {"text": "La cuisine annexe.", "isCorrect": False}
                    ],
                    "correction": "Le **vestiaire** est un service de courtoisie qui contribue à l'expérience client. Il permet d'éviter que les clients n'encombrent leurs sièges avec leurs affaires."
                },
            ]
        }
    }
}