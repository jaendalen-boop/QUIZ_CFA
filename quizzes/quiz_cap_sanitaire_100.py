quiz_data = {
    "title": "Quiz CAP Monteur en Installations Sanitaires (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET FAÇONNAGE (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE DES MATÉRIAUX ET FAÇONNAGE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Sous quel état le cuivre est-il généralement vendu lorsqu'il est conditionné en couronnes ?",
                    "answerOptions": [
                        {"text": "Recuit", "isCorrect": True},
                        {"text": "Écroui", "isCorrect": False},
                        {"text": "Galvanisé", "isCorrect": False},
                        {"text": "Inoxydable", "isCorrect": False}
                    ],
                    "correction": "Le cuivre en couronne est 'recuit' (traité thermiquement), ce qui le rend malléable et permet de le dérouler et de le cintrer à la main. Le cuivre en barre est 'écroui' (rigide)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel outil spécifique utilise-t-on pour réaliser un filetage extérieur sur un tube en acier galvanisé ?",
                    "answerOptions": [
                        {"text": "Filière", "isCorrect": True},
                        {"text": "Taraud", "isCorrect": False},
                        {"text": "Coupe-tube", "isCorrect": False},
                        {"text": "Alésoir", "isCorrect": False}
                    ],
                    "correction": "La filière (manuelle ou électrique) est l'outil qui permet d'usiner les filets sur la surface extérieure du tube pour permettre le vissage des raccords."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la méthode d'assemblage standard pour les tubes d'évacuation en PVC gris ?",
                    "answerOptions": [
                        {"text": "Collage à froid", "isCorrect": True},
                        {"text": "Soudure autogène", "isCorrect": False},
                        {"text": "Sertissage radial", "isCorrect": False},
                        {"text": "Vissage conique", "isCorrect": False}
                    ],
                    "correction": "Le PVC s'assemble par emboîtement et collage à froid (soudure chimique) après avoir décapé les surfaces. On ne chauffe jamais le PVC d'évacuation."
                },
                {
                    "questionNumber": 4,
                    "question": "Pourquoi est-il indispensable d'ébavurer l'intérieur d'un tube de cuivre après l'avoir coupé ?",
                    "answerOptions": [
                        {"text": "Éviter les perturbations hydrauliques et bruits", "isCorrect": True},
                        {"text": "Faciliter le passage de la clé de serrage", "isCorrect": False},
                        {"text": "Modifier la structure chimique du métal coupé", "isCorrect": False},
                        {"text": "Augmenter l'épaisseur de la paroi du tube", "isCorrect": False}
                    ],
                    "correction": "La bavure réduit le diamètre intérieur, crée des turbulences (pertes de charge) et favorise l'érosion du tube ainsi que les sifflements lors de l'écoulement."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le composant responsable de la barrière anti-oxygène dans un tube multicouche ?",
                    "answerOptions": [
                        {"text": "Aluminium", "isCorrect": True},
                        {"text": "Polyéthylène", "isCorrect": False},
                        {"text": "Mousse", "isCorrect": False},
                        {"text": "Résine", "isCorrect": False}
                    ],
                    "correction": "Le tube multicouche est composé de PEX/Alu/PEX. La couche centrale en aluminium empêche l'oxygène de pénétrer, évitant ainsi la formation de boues dans les réseaux de chauffage."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel phénomène physique permet au métal d'apport de pénétrer dans l'emboîture lors d'une soudure à l'étain ?",
                    "answerOptions": [
                        {"text": "Capillarité", "isCorrect": True},
                        {"text": "Gravité", "isCorrect": False},
                        {"text": "Électrolyse", "isCorrect": False},
                        {"text": "Condensation", "isCorrect": False}
                    ],
                    "correction": "Lorsque le métal est à bonne température et décapé, le métal d'apport liquide est 'aspiré' dans le fin espace entre le tube et le raccord par capillarité."
                },
                {
                    "questionNumber": 7,
                    "question": "Comment identifie-t-on visuellement une bouteille d'acétylène sur un poste à souder oxyacétylénique ?",
                    "answerOptions": [
                        {"text": "Ogive marron", "isCorrect": True},
                        {"text": "Ogive blanche", "isCorrect": False},
                        {"text": "Ogive verte", "isCorrect": False},
                        {"text": "Ogive grise", "isCorrect": False}
                    ],
                    "correction": "Selon le code couleur normalisé des gaz, l'ogive (haut de la bouteille) de l'acétylène est couleur marron (chocolat). L'oxygène est blanc."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel outil permet de serrer l'écrou d'un robinet situé dans un endroit très difficile d'accès sous un lavabo ?",
                    "answerOptions": [
                        {"text": "Clé lavabo", "isCorrect": True},
                        {"text": "Clé à griffe type Stillson", "isCorrect": False},
                        {"text": "Pince multiprise à verrouillage", "isCorrect": False},
                        {"text": "Clé dynamométrique de précision", "isCorrect": False}
                    ],
                    "correction": "La clé lavabo possède une tête pivotante montée sur un long manche, spécialement conçue pour atteindre les écrous de fixation des mitigeurs sous la céramique."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle est la température approximative de fusion du métal d'apport pour une brasure forte (Cuivre/Phosphore) ?",
                    "answerOptions": [
                        {"text": "700 degrés Celsius", "isCorrect": True},
                        {"text": "200 degrés Celsius", "isCorrect": False},
                        {"text": "1500 degrés Celsius", "isCorrect": False},
                        {"text": "100 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "La brasure forte nécessite une température de chauffe entre 700°C et 800°C, contrairement à la brasure tendre (étain) qui fond vers 230°C."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel matériau d'étanchéité est traditionnellement utilisé avec la pâte à joint sur les raccords filetés en acier ?",
                    "answerOptions": [
                        {"text": "Filasse", "isCorrect": True},
                        {"text": "Téflon", "isCorrect": False},
                        {"text": "Résine", "isCorrect": False},
                        {"text": "Silicone", "isCorrect": False}
                    ],
                    "correction": "La filasse (chanvre) associée à la pâte à joint reste la référence pour l'étanchéité des réseaux acier et chauffage, car elle permet un léger réajustement (dévissage) sans fuite."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel type de tube plastique nécessite l'utilisation d'une pince à glissement ou à sertir pour l'assemblage ?",
                    "answerOptions": [
                        {"text": "PER", "isCorrect": True},
                        {"text": "PVC", "isCorrect": False},
                        {"text": "PEHD", "isCorrect": False},
                        {"text": "ABS", "isCorrect": False}
                    ],
                    "correction": "Le PER (Polyéthylène Réticulé) s'assemble mécaniquement via des raccords à glissement (bague qu'on fait glisser) ou à sertir (écrasement par pince). Il ne se colle pas."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle précaution faut-il prendre avant de cintrer un tube de cuivre écroui ?",
                    "answerOptions": [
                        {"text": "Le recuire en le chauffant au rouge", "isCorrect": True},
                        {"text": "Le graisser abondamment avec de l'huile", "isCorrect": False},
                        {"text": "Le remplir de sable fin humide et tassé", "isCorrect": False},
                        {"text": "Le refroidir au congélateur pendant une heure", "isCorrect": False}
                    ],
                    "correction": "Le cuivre écroui est trop rigide et casserait ou s'aplatirait au cintrage. Il faut le recuire (chauffer) localement pour lui redonner sa malléabilité."
                },
                {
                    "questionNumber": 13,
                    "question": "Que signifie le chiffre '1' dans la désignation d'un raccord en laiton 15x21 ?",
                    "answerOptions": [
                        {"text": "Demi pouce", "isCorrect": True},
                        {"text": "Trois quarts de pouce", "isCorrect": False},
                        {"text": "Un pouce", "isCorrect": False},
                        {"text": "Un quart de pouce", "isCorrect": False}
                    ],
                    "correction": "Dans la correspondance pouce/mm : 12x17 = 3/8', 15x21 = 1/2' (demi-pouce), 20x27 = 3/4'."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le principal risque si l'on raccorde directement du cuivre sur de l'acier galvanisé dans le sens de l'écoulement ?",
                    "answerOptions": [
                        {"text": "Corrosion galvanique", "isCorrect": True},
                        {"text": "Dilatation thermique excessive", "isCorrect": False},
                        {"text": "Rupture mécanique immédiate", "isCorrect": False},
                        {"text": "Formation de calcaire rapide", "isCorrect": False}
                    ],
                    "correction": "Le couple électrolytique Cuivre/Acier provoque une corrosion rapide de l'acier (effet de pile). Il faut utiliser un raccord diélectrique pour isoler les deux métaux."
                },
                {
                    "questionNumber": 15,
                    "question": "Pour quel usage le PVC-C (sur-chloré) est-il spécifiquement conçu par rapport au PVC classique ?",
                    "answerOptions": [
                        {"text": "Évacuations chaudes", "isCorrect": True},
                        {"text": "Alimentation eau potable", "isCorrect": False},
                        {"text": "Protection des câbles", "isCorrect": False},
                        {"text": "Ventilation primaire", "isCorrect": False}
                    ],
                    "correction": "Le PVC-C résiste à des températures plus élevées (jusqu'à 80°C voire plus), ce qui le rend adapté aux vidanges de machines à laver ou cuisines collectives."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le rôle du flux décapant appliqué avant la soudure ?",
                    "answerOptions": [
                        {"text": "Nettoyer l'oxyde et favoriser l'accroche", "isCorrect": True},
                        {"text": "Refroidir le métal pour éviter la percé", "isCorrect": False},
                        {"text": "Remplacer le métal d'apport manquant", "isCorrect": False},
                        {"text": "Faire briller le cuivre après chauffe", "isCorrect": False}
                    ],
                    "correction": "Le flux (pâte ou liquide) dissout les oxydes présents en surface et protège le métal de l'oxydation pendant la chauffe, garantissant le mouillage de la soudure."
                },
                {
                    "questionNumber": 17,
                    "question": "Avec quel outil coupe-t-on un tube PER pour garantir une coupe nette sans écrasement ?",
                    "answerOptions": [
                        {"text": "Pince coupe-gaine", "isCorrect": True},
                        {"text": "Scie à métaux", "isCorrect": False},
                        {"text": "Meuleuse d'angle", "isCorrect": False},
                        {"text": "Ciseau à bois", "isCorrect": False}
                    ],
                    "correction": "La pince coupe-tube (ou coupe-gaine) possède une lame triangulaire tranchante qui tranche le plastique sans le déformer, contrairement à la scie qui fait des bavures."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la particularité d'un raccord 'bi-cône' ou raccord olive ?",
                    "answerOptions": [
                        {"text": "Étanchéité par compression d'une bague laiton", "isCorrect": True},
                        {"text": "Nécessité absolue de réaliser une soudure", "isCorrect": False},
                        {"text": "Utilisation exclusive sur les tubes en plastique", "isCorrect": False},
                        {"text": "Obligation de faire un collet battu au marteau", "isCorrect": False}
                    ],
                    "correction": "Le raccord bi-cône possède une bague (olive) qui se déforme et mord le tube de cuivre lors du serrage de l'écrou, assurant l'étanchéité sans soudure."
                },
                {
                    "questionNumber": 19,
                    "question": "Parmi ces matériaux, lequel possède le coefficient de dilatation thermique le plus élevé ?",
                    "answerOptions": [
                        {"text": "PER", "isCorrect": True},
                        {"text": "Cuivre", "isCorrect": False},
                        {"text": "Acier", "isCorrect": False},
                        {"text": "Fonte", "isCorrect": False}
                    ],
                    "correction": "Les matériaux de synthèse comme le PER se dilatent beaucoup plus que les métaux. Il faut prévoir cette dilatation (lyres, libre passage) lors de la pose."
                },
                {
                    "questionNumber": 20,
                    "question": "À quoi sert une 'cintreuse arbalète' ?",
                    "answerOptions": [
                        {"text": "Cintrer des tubes rigides de gros diamètre", "isCorrect": True},
                        {"text": "Couper les tubes en acier de forte épaisseur", "isCorrect": False},
                        {"text": "Visser les raccords de grand diamètre", "isCorrect": False},
                        {"text": "Souder les tubes sans apport de gaz", "isCorrect": False}
                    ],
                    "correction": "La cintreuse arbalète utilise un vérin hydraulique ou mécanique et des formes pour cintrer les tubes de cuivre écroui ou multicouche de gros diamètre sans effort."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : APPAREILS SANITAIRES, PRODUCTION D'EAU CHAUDE ET ROBINETTERIE (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : APPAREILS SANITAIRES, PRODUCTION D'EAU CHAUDE ET ROBINETTERIE",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la hauteur standard de pose d'un lavabo par rapport au sol fini (niveau de la plage de robinetterie) ?",
                    "answerOptions": [
                        {"text": "85 centimètres", "isCorrect": True},
                        {"text": "105 centimètres", "isCorrect": False},
                        {"text": "60 centimètres", "isCorrect": False},
                        {"text": "45 centimètres", "isCorrect": False}
                    ],
                    "correction": "La norme PMR et l'usage standard fixent la hauteur du plan de vasque ou du lavabo entre 85 cm et 90 cm pour une ergonomie optimale."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est le rôle précis de la 'garde d'eau' contenue dans un siphon ?",
                    "answerOptions": [
                        {"text": "Empêcher la remontée des mauvaises odeurs", "isCorrect": True},
                        {"text": "Refroidir l'eau avant son arrivée à l'égout", "isCorrect": False},
                        {"text": "Filtrer les cheveux et les gros déchets solides", "isCorrect": False},
                        {"text": "Réguler la pression atmosphérique dans le tuyau", "isCorrect": False}
                    ],
                    "correction": "La garde d'eau (généralement 50 mm) est le bouchon hydraulique permanent qui bloque le passage de l'air vicié des égouts vers l'habitation."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la pression de tarage standard de la soupape d'un groupe de sécurité pour chauffe-eau électrique ?",
                    "answerOptions": [
                        {"text": "7 bars", "isCorrect": True},
                        {"text": "3 bars", "isCorrect": False},
                        {"text": "10 bars", "isCorrect": False},
                        {"text": "1 bar", "isCorrect": False}
                    ],
                    "correction": "La soupape s'ouvre automatiquement dès que la pression dans la cuve dépasse 7 bars (due à la dilatation de l'eau chauffée) pour évacuer le surplus."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la différence majeure entre une résistance blindée et une résistance stéatite ?",
                    "answerOptions": [
                        {"text": "La stéatite est protégée du calcaire par un fourreau", "isCorrect": True},
                        {"text": "La blindée consomme trois fois moins d'électricité", "isCorrect": False},
                        {"text": "La stéatite est obligatoirement immergée dans l'eau", "isCorrect": False},
                        {"text": "La blindée est fabriquée en céramique pure fragile", "isCorrect": False}
                    ],
                    "correction": "La résistance stéatite est insérée dans un fourreau émaillé (doigt de gant), elle n'est jamais en contact direct avec l'eau, ce qui la protège du tartre et permet son remplacement sans vidanger la cuve."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel diamètre extérieur de tube PVC utilise-t-on généralement pour l'évacuation d'un WC standard ?",
                    "answerOptions": [
                        {"text": "100 mm", "isCorrect": True},
                        {"text": "32 mm", "isCorrect": False},
                        {"text": "40 mm", "isCorrect": False},
                        {"text": "50 mm", "isCorrect": False}
                    ],
                    "correction": "L'évacuation des eaux vannes (WC) nécessite un diamètre minimal de 100 mm pour éviter les bouchons et assurer un écoulement correct."
                },
                {
                    "questionNumber": 26,
                    "question": "Comment appelle-t-on le mécanisme qui permet de remplir le réservoir de chasse d'eau et de s'arrêter au niveau souhaité ?",
                    "answerOptions": [
                        {"text": "Robinet flotteur", "isCorrect": True},
                        {"text": "Mécanisme de vidage", "isCorrect": False},
                        {"text": "Soupape de décharge", "isCorrect": False},
                        {"text": "Clapet anti-retour", "isCorrect": False}
                    ],
                    "correction": "Le robinet flotteur détecte la montée de l'eau grâce à un flotteur (en polystyrène ou plastique) et ferme l'arrivée d'eau une fois le niveau réglé atteint."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la température minimale de stockage de l'eau chaude sanitaire pour prévenir le développement des légionelles ?",
                    "answerOptions": [
                        {"text": "55 degrés", "isCorrect": True},
                        {"text": "25 degrés", "isCorrect": False},
                        {"text": "90 degrés", "isCorrect": False},
                        {"text": "35 degrés", "isCorrect": False}
                    ],
                    "correction": "La bactérie Legionella prolifère dans les eaux tièdes. Il est obligatoire de maintenir l'eau chaude à au moins 55°C (souvent 60°C) pour stopper son développement."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la fonction principale d'un mitigeur thermostatique ?",
                    "answerOptions": [
                        {"text": "Maintenir une température de sortie constante", "isCorrect": True},
                        {"text": "Augmenter le débit de l'eau dans la douche", "isCorrect": False},
                        {"text": "Produire de l'eau chaude instantanément", "isCorrect": False},
                        {"text": "Filtrer le calcaire présent dans l'eau froide", "isCorrect": False}
                    ],
                    "correction": "Le mitigeur thermostatique compense automatiquement les variations de débit ou de température des alimentations pour délivrer une eau à la température exacte choisie par l'utilisateur."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel élément protège la cuve en acier émaillé d'un chauffe-eau contre la corrosion ?",
                    "answerOptions": [
                        {"text": "Anode", "isCorrect": True},
                        {"text": "Cathode", "isCorrect": False},
                        {"text": "Diode", "isCorrect": False},
                        {"text": "Sonde", "isCorrect": False}
                    ],
                    "correction": "L'anode (en magnésium ou titane) 'se sacrifie' ou impose un courant protecteur pour empêcher la corrosion de percer la cuve en acier."
                },
                {
                    "questionNumber": 30,
                    "question": "Sur un groupe de sécurité, à quoi sert le robinet quart de tour (souvent à manette noire ou rouge) intégré ?",
                    "answerOptions": [
                        {"text": "Fermer l'arrivée d'eau froide du ballon", "isCorrect": True},
                        {"text": "Vidanger totalement la cuve en urgence", "isCorrect": False},
                        {"text": "Régler la température de l'eau chaude", "isCorrect": False},
                        {"text": "Couper l'alimentation électrique du cumulus", "isCorrect": False}
                    ],
                    "correction": "Ce robinet d'arrêt intégré permet d'isoler le chauffe-eau du réseau d'eau froide pour effectuer des travaux de maintenance ou le remplacement du groupe."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel type de bâti-support est impératif si le mur d'adossement est une cloison légère en plaque de plâtre ?",
                    "answerOptions": [
                        {"text": "Autoportant", "isCorrect": True},
                        {"text": "Mural", "isCorrect": False},
                        {"text": "Suspendu", "isCorrect": False},
                        {"text": "Encastré", "isCorrect": False}
                    ],
                    "correction": "Le bâti-support 'autoportant' possède des pieds renforcés qui reposent sur le sol béton, car la cloison légère ne peut pas supporter le poids de la cuvette et de l'utilisateur."
                },
                {
                    "questionNumber": 32,
                    "question": "Qu'est-ce qu'une 'bonde' dans un appareil sanitaire ?",
                    "answerOptions": [
                        {"text": "La pièce métallique fixée à l'orifice d'écoulement", "isCorrect": True},
                        {"text": "Le tuyau souple qui raccorde le siphon au mur", "isCorrect": False},
                        {"text": "La manette qui actionne l'ouverture du bouchon", "isCorrect": False},
                        {"text": "Le joint d'étanchéité entre le robinet et l'évier", "isCorrect": False}
                    ],
                    "correction": "La bonde est l'élément traversant scellé au fond du lavabo ou de la douche, sur lequel on visse le siphon par-dessous."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle pièce doit être installée obligatoirement sur l'arrivée d'eau froide d'un chauffe-eau si la pression du réseau dépasse 3 bars ?",
                    "answerOptions": [
                        {"text": "Réducteur de pression", "isCorrect": True},
                        {"text": "Surpresseur domestique", "isCorrect": False},
                        {"text": "Filtre à sédiments", "isCorrect": False},
                        {"text": "Compteur divisionnaire", "isCorrect": False}
                    ],
                    "correction": "Si la pression réseau est trop forte, le groupe de sécurité va fuir en permanence. Le réducteur de pression (placé après le compteur) protège l'installation."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la particularité d'un chauffe-eau 'thermodynamique' ?",
                    "answerOptions": [
                        {"text": "Il intègre une pompe à chaleur", "isCorrect": True},
                        {"text": "Il fonctionne au gaz de ville", "isCorrect": False},
                        {"text": "Il chauffe l'eau avec des bûches", "isCorrect": False},
                        {"text": "Il utilise des panneaux solaires", "isCorrect": False}
                    ],
                    "correction": "Le chauffe-eau thermodynamique récupère les calories de l'air ambiant ou extérieur grâce à une petite pompe à chaleur intégrée pour chauffer l'eau, économisant l'électricité."
                },
                {
                    "questionNumber": 35,
                    "question": "Dans une salle de bains, que désigne le 'Volume 0' selon la norme électrique ?",
                    "answerOptions": [
                        {"text": "L'intérieur de la baignoire ou du receveur", "isCorrect": True},
                        {"text": "L'espace situé sous la baignoire maçonné", "isCorrect": False},
                        {"text": "La zone située à plus de 3 mètres de la douche", "isCorrect": False},
                        {"text": "Le plafond situé au-dessus de la douche", "isCorrect": False}
                    ],
                    "correction": "Le Volume 0 est le volume intérieur direct de la baignoire ou du receveur de douche, où tout appareillage électrique est strictement interdit (sauf très basse tension spécifique)."
                },
                {
                    "questionNumber": 36,
                    "question": "À quoi sert le 'trop-plein' sur un lavabo ou une baignoire ?",
                    "answerOptions": [
                        {"text": "Éviter le débordement accidentel de l'eau", "isCorrect": True},
                        {"text": "Permettre une ventilation de la colonne", "isCorrect": False},
                        {"text": "Faire joli sur la céramique sanitaire", "isCorrect": False},
                        {"text": "Fixer la chaînette du bouchon", "isCorrect": False}
                    ],
                    "correction": "Le trop-plein est un orifice de sécurité relié à la vidange qui permet d'évacuer l'eau si l'utilisateur oublie de fermer le robinet avec la bonde fermée."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'avantage d'un robinet 'mitigeur' par rapport à un 'mélangeur' ?",
                    "answerOptions": [
                        {"text": "Une seule commande pour le débit et la température", "isCorrect": True},
                        {"text": "Deux têtes séparées pour l'eau chaude et l'eau froide", "isCorrect": False},
                        {"text": "Une résistance accrue au gel en extérieur", "isCorrect": False},
                        {"text": "Un débit d'eau beaucoup plus important", "isCorrect": False}
                    ],
                    "correction": "Le mitigeur se manipule d'une seule main (levier), ce qui est plus pratique et plus économique qu'un mélangeur à deux têtes."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel gaz rare est souvent injecté dans le double vitrage ou utilisé dans certaines soudures, mais sans rapport avec le chauffe-eau gaz ?",
                    "answerOptions": [
                        {"text": "Argon", "isCorrect": True},
                        {"text": "Butane", "isCorrect": False},
                        {"text": "Propane", "isCorrect": False},
                        {"text": "Méthane", "isCorrect": False}
                    ],
                    "correction": "Question piège de culture technique : les chauffe-eaux gaz fonctionnent au Butane, Propane ou Gaz Naturel (Méthane). L'Argon est un gaz inerte de soudure/vitrage."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle pièce d'usure assure l'étanchéité à l'intérieur d'un mécanisme de tête de robinet 'à clapet' ?",
                    "answerOptions": [
                        {"text": "Joint noir en caoutchouc", "isCorrect": True},
                        {"text": "Disque céramique dur", "isCorrect": False},
                        {"text": "Bille en acier inoxydable", "isCorrect": False},
                        {"text": "Ressort en cuivre", "isCorrect": False}
                    ],
                    "correction": "Dans un robinet classique (mélangeur à clapet), c'est un joint plat en caoutchouc qui vient s'écraser sur le siège pour couper l'eau. Il s'use et doit être changé."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel dispositif est obligatoire à la sortie d'un chauffe-eau pour éviter la corrosion galvanique si la tuyauterie est en cuivre ?",
                    "answerOptions": [
                        {"text": "Raccord diélectrique", "isCorrect": True},
                        {"text": "Raccord union laiton", "isCorrect": False},
                        {"text": "Manchon en PVC pression", "isCorrect": False},
                        {"text": "Flexible en inox tressé", "isCorrect": False}
                    ],
                    "correction": "Le raccord diélectrique (souvent fourni) isole électriquement la sortie eau chaude (acier) du tube de distribution (cuivre) pour empêcher l'effet de pile qui percerait la cuve."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : HYDRAULIQUE, RÉSEAUX D'ALIMENTATION ET D'ÉVACUATION (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : HYDRAULIQUE, RÉSEAUX D'ALIMENTATION ET D'ÉVACUATION",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la pente minimale recommandée pour une canalisation d'évacuation d'eaux usées en PVC afin d'assurer l'autocurage ?",
                    "answerOptions": [
                        {"text": "1 à 2 cm par mètre", "isCorrect": True},
                        {"text": "10 cm par mètre", "isCorrect": False},
                        {"text": "5 millimètres par mètre", "isCorrect": False},
                        {"text": "45 degrés d'angle constant", "isCorrect": False}
                    ],
                    "correction": "Une pente comprise entre 1% et 3% (1 à 3 cm/m) permet l'écoulement des liquides tout en entraînant les matières solides (autocurage). Une pente trop forte laisse les matières sur place (l'eau va trop vite)."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel phénomène hydraulique bruyant se produit lors de la fermeture brutale d'un robinet ?",
                    "answerOptions": [
                        {"text": "Coup de bélier", "isCorrect": True},
                        {"text": "Cavitation", "isCorrect": False},
                        {"text": "Laminage", "isCorrect": False},
                        {"text": "Siphonnage", "isCorrect": False}
                    ],
                    "correction": "L'arrêt brusque de la colonne d'eau en mouvement crée une onde de choc surpressionnaire appelée 'coup de bélier', qui peut endommager les canalisations."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel appareil installe-t-on pour absorber l'onde de choc provoquée par la fermeture rapide des vannes ?",
                    "answerOptions": [
                        {"text": "Anti-bélier", "isCorrect": True},
                        {"text": "Réducteur de pression", "isCorrect": False},
                        {"text": "Clapet anti-retour", "isCorrect": False},
                        {"text": "Disconnecteur", "isCorrect": False}
                    ],
                    "correction": "L'anti-bélier (à ressort ou à membrane) possède un petit réservoir d'air ou un piston qui absorbe l'énergie de l'onde de choc hydraulique."
                },
                {
                    "questionNumber": 44,
                    "question": "Que désignent spécifiquement les 'Eaux Vannes' (EV) dans un réseau d'évacuation ?",
                    "answerOptions": [
                        {"text": "Eaux issues des WC", "isCorrect": True},
                        {"text": "Eaux issues des cuisines", "isCorrect": False},
                        {"text": "Eaux de pluie", "isCorrect": False},
                        {"text": "Eaux de vidange chauffage", "isCorrect": False}
                    ],
                    "correction": "On distingue les Eaux Usées (EU) venant des éviers/lavabos/douches, et les Eaux Vannes (EV) provenant exclusivement des toilettes."
                },
                {
                    "questionNumber": 45,
                    "question": "À quoi correspond une pression de 1 bar en hauteur de colonne d'eau (environ) ?",
                    "answerOptions": [
                        {"text": "10 mètres", "isCorrect": True},
                        {"text": "100 mètres", "isCorrect": False},
                        {"text": "1 mètre", "isCorrect": False},
                        {"text": "1 kilomètre", "isCorrect": False}
                    ],
                    "correction": "1 bar équivaut approximativement à la pression exercée par une colonne d'eau de 10 mètres de hauteur (10 mCE)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le rôle de la 'ventilation primaire' sur une chute d'eaux usées ?",
                    "answerOptions": [
                        {"text": "Éviter le désiphonnage", "isCorrect": True},
                        {"text": "Aérer la salle de bains", "isCorrect": False},
                        {"text": "Refroidir les tuyaux", "isCorrect": False},
                        {"text": "Filtrer les odeurs", "isCorrect": False}
                    ],
                    "correction": "La ventilation primaire (sortie en toiture) permet de maintenir la pression atmosphérique dans la colonne pour éviter que l'aspiration créée par une chasse d'eau ne vide les siphons voisins."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel appareil est obligatoire sur l'alimentation d'eau froide générale pour protéger le réseau public contre la pollution ?",
                    "answerOptions": [
                        {"text": "Disconnecteur ou clapet EA", "isCorrect": True},
                        {"text": "Compteur divisionnaire", "isCorrect": False},
                        {"text": "Vanne d'arrêt sphérique", "isCorrect": False},
                        {"text": "Vase d'expansion sanitaire", "isCorrect": False}
                    ],
                    "correction": "Le clapet anti-pollution (type EA) ou le disconnecteur empêche l'eau de l'habitation (potentiellement polluée) de retourner vers le réseau public de distribution."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment appelle-t-on la perte de pression due au frottement de l'eau contre les parois du tuyau ?",
                    "answerOptions": [
                        {"text": "Perte de charge", "isCorrect": True},
                        {"text": "Débit massique", "isCorrect": False},
                        {"text": "Pression statique", "isCorrect": False},
                        {"text": "Hauteur manométrique", "isCorrect": False}
                    ],
                    "correction": "Les 'pertes de charge' sont les diminutions de pression causées par la longueur des tuyaux, la rugosité du matériau et les accidents de parcours (coudes, tés)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est l'unité de mesure de la dureté de l'eau (teneur en calcaire) ?",
                    "answerOptions": [
                        {"text": "Degré français", "isCorrect": True},
                        {"text": "Degré Celsius", "isCorrect": False},
                        {"text": "Pascal", "isCorrect": False},
                        {"text": "pH", "isCorrect": False}
                    ],
                    "correction": "Le Titre Hydrotimétrique (TH) s'exprime en degrés français (°f). Une eau est dite 'dure' (calcaire) au-dessus de 15°f ou 20°f."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel dispositif permet de réduire la pression du réseau public (souvent 5 ou 6 bars) à 3 bars dans la maison ?",
                    "answerOptions": [
                        {"text": "Réducteur de pression", "isCorrect": True},
                        {"text": "Surpresseur", "isCorrect": False},
                        {"text": "Manomètre", "isCorrect": False},
                        {"text": "Compteur", "isCorrect": False}
                    ],
                    "correction": "Le réducteur de pression se place juste après le compteur général pour protéger toute l'installation domestique des surpressions du réseau de ville."
                },
                {
                    "questionNumber": 51,
                    "question": "Dans quel réseau les eaux pluviales et les eaux usées sont-elles évacuées dans la même canalisation ?",
                    "answerOptions": [
                        {"text": "Réseau unitaire", "isCorrect": True},
                        {"text": "Réseau séparatif", "isCorrect": False},
                        {"text": "Réseau autonome", "isCorrect": False},
                        {"text": "Réseau épandage", "isCorrect": False}
                    ],
                    "correction": "Le système 'unitaire' collecte tout (pluie + usées) dans un seul tuyau, contrairement au système 'séparatif' qui impose deux collecteurs distincts."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la vitesse maximale conseillée de l'eau dans les tuyaux pour éviter les nuisances sonores ?",
                    "answerOptions": [
                        {"text": "1,5 mètre par seconde", "isCorrect": True},
                        {"text": "10 mètres par seconde", "isCorrect": False},
                        {"text": "50 kilomètres par heure", "isCorrect": False},
                        {"text": "20 millimètres par minute", "isCorrect": False}
                    ],
                    "correction": "Au-delà de 1,5 à 2 m/s, la circulation de l'eau génère des bruits d'écoulement et de sifflement désagréables pour les occupants."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est l'organe qui permet de distribuer l'eau vers plusieurs appareils à partir d'un point central ?",
                    "answerOptions": [
                        {"text": "Nourrice", "isCorrect": True},
                        {"text": "Siphon", "isCorrect": False},
                        {"text": "Purgeur", "isCorrect": False},
                        {"text": "Bouchon", "isCorrect": False}
                    ],
                    "correction": "La nourrice (ou clarinette/collecteur) reçoit l'alimentation principale et la divise en plusieurs départs individuels vers chaque équipement (lavabo, WC, douche)."
                },
                {
                    "questionNumber": 54,
                    "question": "Que mesure un manomètre ?",
                    "answerOptions": [
                        {"text": "La pression", "isCorrect": True},
                        {"text": "Le débit", "isCorrect": False},
                        {"text": "La température", "isCorrect": False},
                        {"text": "L'humidité", "isCorrect": False}
                    ],
                    "correction": "Le manomètre est l'instrument à cadran qui affiche la pression du fluide dans le réseau, généralement gradué en bars."
                },
                {
                    "questionNumber": 55,
                    "question": "Pourquoi utilise-t-on un vase d'expansion sanitaire (souvent blanc) sur l'arrivée d'eau froide d'un chauffe-eau ?",
                    "answerOptions": [
                        {"text": "Absorber la dilatation et économiser l'eau", "isCorrect": True},
                        {"text": "Purifier l'eau avant qu'elle ne chauffe", "isCorrect": False},
                        {"text": "Augmenter la pression de l'eau chaude", "isCorrect": False},
                        {"text": "Refroidir le groupe de sécurité", "isCorrect": False}
                    ],
                    "correction": "Le vase absorbe le volume d'eau qui se dilate lors de la chauffe. Cela évite l'ouverture de la soupape du groupe de sécurité et donc la perte d'eau à l'égout."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le diamètre nominal (DN) intérieur minimum pour l'alimentation d'une baignoire en cuivre ?",
                    "answerOptions": [
                        {"text": "14 mm", "isCorrect": True},
                        {"text": "10 mm", "isCorrect": False},
                        {"text": "8 mm", "isCorrect": False},
                        {"text": "32 mm", "isCorrect": False}
                    ],
                    "correction": "Pour assurer un débit suffisant et un remplissage rapide, une baignoire doit être alimentée par du cuivre de diamètre intérieur minimum 13 ou 14 mm (Cuivre 14/16)."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est l'effet d'une réduction de diamètre sur la vitesse de l'eau, à débit constant ?",
                    "answerOptions": [
                        {"text": "La vitesse augmente", "isCorrect": True},
                        {"text": "La vitesse diminue", "isCorrect": False},
                        {"text": "La vitesse reste identique", "isCorrect": False},
                        {"text": "La vitesse s'annule", "isCorrect": False}
                    ],
                    "correction": "Selon l'effet Venturi : si le tuyau rétrécit et que le débit reste le même, l'eau est obligée d'accélérer pour passer (Vitesse augmente, Pression diminue)."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment appelle-t-on le test consistant à mettre le réseau sous pression pour vérifier l'absence de fuites ?",
                    "answerOptions": [
                        {"text": "Épreuve d'étanchéité", "isCorrect": True},
                        {"text": "Vidange curative", "isCorrect": False},
                        {"text": "Mise en eau dynamique", "isCorrect": False},
                        {"text": "Purge des radiateurs", "isCorrect": False}
                    ],
                    "correction": "L'épreuve d'étanchéité se fait souvent à une pression supérieure à la pression de service (ex: 6 à 10 bars) avant de refermer les cloisons ou les tranchées."
                },
                {
                    "questionNumber": 59,
                    "question": "Qu'est-ce qu'un 'clapet anti-retour' ?",
                    "answerOptions": [
                        {"text": "Un dispositif imposant un sens unique de circulation", "isCorrect": True},
                        {"text": "Une vanne pour couper l'eau manuellement", "isCorrect": False},
                        {"text": "Un bouchon de visite pour déboucher les tuyaux", "isCorrect": False},
                        {"text": "Une grille de filtration des impuretés", "isCorrect": False}
                    ],
                    "correction": "Le clapet anti-retour (à battant ou à ressort) s'ouvre dans le sens du flux et se bloque si l'eau tente de revenir en arrière."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle est la conséquence principale d'une eau trop douce (TH inférieur à 10°f) ?",
                    "answerOptions": [
                        {"text": "Corrosion des métaux", "isCorrect": True},
                        {"text": "Entartrage rapide des tuyaux", "isCorrect": False},
                        {"text": "Dépôt de calcaire sur les résistances", "isCorrect": False},
                        {"text": "Mauvaise odeur de l'eau", "isCorrect": False}
                    ],
                    "correction": "Une eau trop douce est 'agressive' : elle n'a plus de couche calcaire protectrice et attaque chimiquement les parois métalliques (corrosion, fuites)."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : LECTURE DE PLANS, DESSIN TECHNIQUE ET IMPLANTATION (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : LECTURE DE PLANS, DESSIN TECHNIQUE ET IMPLANTATION",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle longueur réelle représente un trait de 10 centimètres sur un plan à l'échelle 1/50 ?",
                    "answerOptions": [
                        {"text": "5 mètres", "isCorrect": True},
                        {"text": "50 centimètres", "isCorrect": False},
                        {"text": "10 mètres", "isCorrect": False},
                        {"text": "1 mètre", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/50 signifie que 1 cm sur le papier vaut 50 cm en réalité. Donc 10 cm x 50 = 500 cm, soit 5 mètres."
                },
                {
                    "questionNumber": 62,
                    "question": "Que signifie l'abréviation 'ECS' sur un schéma de principe hydraulique ?",
                    "answerOptions": [
                        {"text": "Eau Chaude Sanitaire", "isCorrect": True},
                        {"text": "Eau Courante Standard", "isCorrect": False},
                        {"text": "Écoulement Canalisation Sortie", "isCorrect": False},
                        {"text": "Ensemble Chauffage Sol", "isCorrect": False}
                    ],
                    "correction": "L'ECS désigne le réseau d'eau potable qui a été chauffée (par un cumulus ou une chaudière) pour les besoins sanitaires (douche, lavabo)."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel type de trait est utilisé en dessin technique pour représenter une canalisation cachée ou encastrée ?",
                    "answerOptions": [
                        {"text": "Trait interrompu court", "isCorrect": True},
                        {"text": "Trait continu fort", "isCorrect": False},
                        {"text": "Trait mixte fin", "isCorrect": False},
                        {"text": "Trait ondulé", "isCorrect": False}
                    ],
                    "correction": "Les éléments invisibles (car derrière un mur, dans une dalle ou un coffrage) sont conventionnellement représentés en pointillés (trait interrompu)."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la définition exacte d'une 'vue en plan' ?",
                    "answerOptions": [
                        {"text": "Une vue de dessus horizontale coupée à un mètre du sol", "isCorrect": True},
                        {"text": "Une vue de face des façades extérieures du bâtiment", "isCorrect": False},
                        {"text": "Une vue verticale tranchant le bâtiment en deux", "isCorrect": False},
                        {"text": "Une vue en perspective artistique du projet fini", "isCorrect": False}
                    ],
                    "correction": "La vue en plan est une coupe horizontale virtuelle réalisée à 1 mètre de hauteur, permettant de visualiser l'agencement des pièces et l'épaisseur des murs."
                },
                {
                    "questionNumber": 65,
                    "question": "Que symbolise le signe 'Ø' placé devant un chiffre sur un plan de plomberie ?",
                    "answerOptions": [
                        {"text": "Diamètre", "isCorrect": True},
                        {"text": "Rayon", "isCorrect": False},
                        {"text": "Périmètre", "isCorrect": False},
                        {"text": "Volume", "isCorrect": False}
                    ],
                    "correction": "Ce symbole universel indique que la cote correspond au diamètre (extérieur ou nominal) du tube ou de l'accessoire circulaire."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel instrument de mesure moderne permet de tracer un trait de niveau sur tous les murs d'une pièce simultanément ?",
                    "answerOptions": [
                        {"text": "Niveau laser rotatif", "isCorrect": True},
                        {"text": "Mètre ruban souple", "isCorrect": False},
                        {"text": "Fil à plomb", "isCorrect": False},
                        {"text": "Règle en aluminium", "isCorrect": False}
                    ],
                    "correction": "Le niveau laser projette un faisceau lumineux horizontal à 360°, ce qui permet d'implanter les fixations à la même hauteur partout sans déplacer l'outil."
                },
                {
                    "questionNumber": 67,
                    "question": "En dessin isométrique de tuyauterie, quel est l'angle des axes fuyants par rapport à l'horizontale ?",
                    "answerOptions": [
                        {"text": "30 degrés", "isCorrect": True},
                        {"text": "45 degrés", "isCorrect": False},
                        {"text": "90 degrés", "isCorrect": False},
                        {"text": "10 degrés", "isCorrect": False}
                    ],
                    "correction": "L'isométrie, très utilisée en tuyauterie industrielle et plomberie pour visualiser les réseaux 3D, utilise des axes inclinés à 30° par rapport à l'horizontale."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle couleur est conventionnellement utilisée pour tracer les réseaux d'eau froide sur un plan ?",
                    "answerOptions": [
                        {"text": "Bleu", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False}
                    ],
                    "correction": "La convention internationale de repérage des fluides attribue la couleur bleue à l'eau froide et le rouge à l'eau chaude ou au chauffage départ."
                },
                {
                    "questionNumber": 69,
                    "question": "Que signifie le terme 'Allège' noté sous une fenêtre sur un plan d'architecte ?",
                    "answerOptions": [
                        {"text": "La hauteur du mur sous la fenêtre", "isCorrect": True},
                        {"text": "La largeur totale de la fenêtre", "isCorrect": False},
                        {"text": "L'épaisseur du vitrage isolant", "isCorrect": False},
                        {"text": "Le poids total de la maçonnerie", "isCorrect": False}
                    ],
                    "correction": "L'allège est la partie maçonnée située entre le sol fini et le rebord bas de la fenêtre. C'est une cote verticale importante pour placer les radiateurs."
                },
                {
                    "questionNumber": 70,
                    "question": "Qu'est-ce qu'une 'réservation' sur un plan de coffrage béton ?",
                    "answerOptions": [
                        {"text": "Un trou prévu pour le passage des tuyaux", "isCorrect": True},
                        {"text": "Un espace de stockage pour le plombier", "isCorrect": False},
                        {"text": "Une commande de matériel à l'avance", "isCorrect": False},
                        {"text": "Un local technique fermé à clé", "isCorrect": False}
                    ],
                    "correction": "Une réservation est une trémie ou un fourreau positionné avant le coulage du béton pour éviter d'avoir à percer la dalle ou le mur par la suite."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel symbole graphique représente généralement une vanne d'arrêt ou un robinet sur un schéma ?",
                    "answerOptions": [
                        {"text": "Deux triangles opposés par la pointe", "isCorrect": True},
                        {"text": "Un carré barré d'une croix", "isCorrect": False},
                        {"text": "Un cercle vide simple", "isCorrect": False},
                        {"text": "Une ligne en zigzag", "isCorrect": False}
                    ],
                    "correction": "Le symbole 'papillon' (deux triangles se touchant par la pointe) représente l'organe de coupure ou de réglage (vanne) sur la ligne de tuyauterie."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie l'indication 'NGF' associée à une cote d'altitude ?",
                    "answerOptions": [
                        {"text": "Nivellement Général de la France", "isCorrect": True},
                        {"text": "Norme Gaz de France", "isCorrect": False},
                        {"text": "Niveau Global de Finition", "isCorrect": False},
                        {"text": "Nouvelle Garantie Fabricant", "isCorrect": False}
                    ],
                    "correction": "Le NGF est le système d'altitude de référence en France (niveau zéro de la mer à Marseille). Il permet de caler les hauteurs absolues du bâtiment."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle échelle offre le plus de détails visuels pour dessiner une salle de bains ?",
                    "answerOptions": [
                        {"text": "1/20", "isCorrect": True},
                        {"text": "1/50", "isCorrect": False},
                        {"text": "1/100", "isCorrect": False},
                        {"text": "1/200", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/20 est plus 'grande' que 1/100. Elle permet de voir les détails des raccordements et l'emplacement précis des appareils sanitaires."
                },
                {
                    "questionNumber": 74,
                    "question": "Que désigne le terme 'calepinage' lors de la préparation du chantier ?",
                    "answerOptions": [
                        {"text": "Le dessin de disposition précise des éléments", "isCorrect": True},
                        {"text": "Le calcul du salaire des ouvriers", "isCorrect": False},
                        {"text": "La liste des outils manquants", "isCorrect": False},
                        {"text": "Le nettoyage final des sols", "isCorrect": False}
                    ],
                    "correction": "En plomberie (comme en carrelage), le calepinage consiste à dessiner l'implantation exacte des tuyaux et appareils pour optimiser les coupes et l'esthétique."
                },
                {
                    "questionNumber": 75,
                    "question": "Sur un plan, comment repère-t-on l'orientation géographique du bâtiment ?",
                    "answerOptions": [
                        {"text": "Par la flèche indiquant le Nord", "isCorrect": True},
                        {"text": "Par la position de la porte d'entrée", "isCorrect": False},
                        {"text": "Par la couleur des murs extérieurs", "isCorrect": False},
                        {"text": "Par l'échelle graphique en bas", "isCorrect": False}
                    ],
                    "correction": "La rose des vents ou une flèche marquée 'N' indique le Nord, ce qui est crucial pour positionner les capteurs solaires ou les sorties de toiture."
                },
                {
                    "questionNumber": 76,
                    "question": "Dans la désignation d'un tube cuivre '14x16', à quoi correspond le chiffre 16 ?",
                    "answerOptions": [
                        {"text": "Au diamètre extérieur en millimètres", "isCorrect": True},
                        {"text": "Au diamètre intérieur en millimètres", "isCorrect": False},
                        {"text": "À l'épaisseur du tube en dixièmes", "isCorrect": False},
                        {"text": "À la pression maximale admissible", "isCorrect": False}
                    ],
                    "correction": "Pour le cuivre courant, '14/16' (ou 16x1) désigne le diamètre extérieur de 16 mm et le diamètre intérieur de 14 mm (épaisseur de 1 mm)."
                },
                {
                    "questionNumber": 77,
                    "question": "Que représente un trait mixte fin (trait long, point, trait long) sur un dessin ?",
                    "answerOptions": [
                        {"text": "Un axe de symétrie ou de tube", "isCorrect": True},
                        {"text": "Une arête visible de l'objet", "isCorrect": False},
                        {"text": "Une hachure de coupe", "isCorrect": False},
                        {"text": "Une cotation de longueur", "isCorrect": False}
                    ],
                    "correction": "Le trait mixte fin matérialise les axes (axe de symétrie d'une pièce, axe central d'une canalisation) pour faciliter la lecture et le cotation."
                },
                {
                    "questionNumber": 78,
                    "question": "Qu'est-ce qu'un 'schéma unifilaire' ?",
                    "answerOptions": [
                        {"text": "Un dessin où le tuyau est représenté par un seul trait", "isCorrect": True},
                        {"text": "Un dessin où l'on voit l'épaisseur réelle du tuyau", "isCorrect": False},
                        {"text": "Un dessin en 3D avec ombrages et lumières réalistes", "isCorrect": False},
                        {"text": "Un dessin artistique fait à la main levée", "isCorrect": False}
                    ],
                    "correction": "Pour simplifier la représentation des réseaux, on dessine l'axe du tube par un trait unique (unifilaire) sur lequel on appose des symboles normalisés."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle information donne une 'coupe verticale' d'un bâtiment ?",
                    "answerOptions": [
                        {"text": "Les hauteurs sous plafond et épaisseurs de dalles", "isCorrect": True},
                        {"text": "La surface habitable en mètres carrés au sol", "isCorrect": False},
                        {"text": "L'orientation du soleil par rapport aux fenêtres", "isCorrect": False},
                        {"text": "Le plan de masse du terrain complet", "isCorrect": False}
                    ],
                    "correction": "La coupe verticale permet de voir ce qui se passe en hauteur : passage des colonnes montantes, réservations dans les planchers, hauteurs des attentes."
                },
                {
                    "questionNumber": 80,
                    "question": "Que signifie le sigle 'EU' sur un plan de réseau d'assainissement ?",
                    "answerOptions": [
                        {"text": "Eaux Usées", "isCorrect": True},
                        {"text": "Eaux Uniques", "isCorrect": False},
                        {"text": "Eaux Utiles", "isCorrect": False},
                        {"text": "États Unis", "isCorrect": False}
                    ],
                    "correction": "EU désigne les 'Eaux Usées' (ménagères : cuisine, salle de bain), à distinguer des EV (Eaux Vannes : WC) et EP (Eaux Pluviales)."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SANTÉ, SÉCURITÉ ET MAINTENANCE (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : SANTÉ, SÉCURITÉ ET MAINTENANCE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle habilitation électrique minimale doit posséder un plombier pour remplacer un chauffe-eau ou raccorder un circulateur (hors tension) ?",
                    "answerOptions": [
                        {"text": "BS", "isCorrect": True},
                        {"text": "B2V", "isCorrect": False},
                        {"text": "BR", "isCorrect": False},
                        {"text": "H0V", "isCorrect": False}
                    ],
                    "correction": "L'habilitation BS (Basse Tension - Chargé d'intervention élémentaire) est destinée aux non-électriciens (plombiers, peintres) devant effectuer des manœuvres simples de raccordement ou de remplacement à l'identique."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel dispositif de sécurité est obligatoire sur les tuyaux d'un poste à souder oxyacétylénique pour éviter l'explosion des bouteilles ?",
                    "answerOptions": [
                        {"text": "Clapet anti-retour pare-flamme", "isCorrect": True},
                        {"text": "Manodétendeur haute pression", "isCorrect": False},
                        {"text": "Économiseur de gaz automatique", "isCorrect": False},
                        {"text": "Filtre à charbon actif", "isCorrect": False}
                    ],
                    "correction": "Les clapets anti-retour pare-flamme (ARPF), placés près du chalumeau ou des détendeurs, empêchent la flamme de remonter dans les tuyaux jusqu'aux bouteilles en cas de retour de feu."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle maladie professionnelle grave est historiquement liée à l'inhalation de poussières lors de la dépose de vieilles calorifugeations ?",
                    "answerOptions": [
                        {"text": "Asbestose", "isCorrect": True},
                        {"text": "Saturnisme", "isCorrect": False},
                        {"text": "Légionellose", "isCorrect": False},
                        {"text": "Tétanos", "isCorrect": False}
                    ],
                    "correction": "L'asbestose (et les cancers associés) est causée par l'inhalation de fibres d'amiante, matériau souvent utilisé autrefois pour isoler (calorifuger) les tuyaux de chauffage."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la procédure sécurisée pour détecter une fuite de gaz sur une installation ?",
                    "answerOptions": [
                        {"text": "Utiliser un produit moussant détecteur", "isCorrect": True},
                        {"text": "Passer la flamme d'un briquet sur les raccords", "isCorrect": False},
                        {"text": "Écouter le bruit du gaz à l'oreille nue", "isCorrect": False},
                        {"text": "Sentir les odeurs en s'approchant très près", "isCorrect": False}
                    ],
                    "correction": "Il est strictement interdit d'utiliser une flamme. On utilise une bombe aérosol moussante (mille-bulles) qui forme des bulles à l'endroit précis de la fuite."
                },
                {
                    "questionNumber": 85,
                    "question": "Que doit faire le plombier s'il intervient sur une canalisation en plomb (intervention aujourd'hui rare mais possible en rénovation) ?",
                    "answerOptions": [
                        {"text": "Porter des gants et se laver soigneusement les mains", "isCorrect": True},
                        {"text": "Faire fondre le plomb sans ventilation pour aller vite", "isCorrect": False},
                        {"text": "Manger son sandwich sur le poste de travail", "isCorrect": False},
                        {"text": "Poncer le plomb à sec pour faire de la poussière", "isCorrect": False}
                    ],
                    "correction": "Le plomb est toxique par ingestion et inhalation (Saturnisme). L'hygiène des mains est primordiale avant de manger, et le port d'EPI est obligatoire."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel document écrit est obligatoire pour effectuer des travaux de soudure dans un établissement recevant du public ou une entreprise en activité ?",
                    "answerOptions": [
                        {"text": "Permis de feu", "isCorrect": True},
                        {"text": "Permis de construire", "isCorrect": False},
                        {"text": "Bon de commande", "isCorrect": False},
                        {"text": "Facture acquittée", "isCorrect": False}
                    ],
                    "correction": "Le 'Permis de feu' est un document de prévention qui analyse les risques d'incendie liés aux points chauds (soudure, meulage) et fixe les mesures de sécurité."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle est la première action à effectuer en cas de brûlure thermique superficielle sur la main ?",
                    "answerOptions": [
                        {"text": "Faire ruisseler de l'eau tempérée sur la zone", "isCorrect": True},
                        {"text": "Appliquer immédiatement de la glace pilée", "isCorrect": False},
                        {"text": "Percer les cloques avec une aiguille", "isCorrect": False},
                        {"text": "Mettre du beurre ou de l'huile grasse", "isCorrect": False}
                    ],
                    "correction": "La règle des '15-15-15' préconise de refroidir la brûlure à l'eau tempérée (15°C) pendant 15 minutes à 15 cm de distance pour stopper la propagation de la chaleur dans les tissus."
                },
                {
                    "questionNumber": 88,
                    "question": "Pourquoi réalise-t-on une 'liaison équipotentielle' en reliant les tuyaux métalliques à la terre ?",
                    "answerOptions": [
                        {"text": "Pour éviter l'électrisation par contact indirect", "isCorrect": True},
                        {"text": "Pour empêcher le calcaire de se déposer", "isCorrect": False},
                        {"text": "Pour améliorer le débit de l'eau potable", "isCorrect": False},
                        {"text": "Pour chauffer l'eau gratuitement par le sol", "isCorrect": False}
                    ],
                    "correction": "La liaison équipotentielle met toutes les masses métalliques (tuyaux cuivre, baignoire fonte) au même potentiel que la terre pour protéger les personnes si un fil électrique touche un tuyau."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle maintenance préventive simple permet d'éviter le blocage d'un groupe de sécurité calcaire ?",
                    "answerOptions": [
                        {"text": "Manœuvrer la soupape une fois par mois", "isCorrect": True},
                        {"text": "Démonter le groupe entièrement chaque semaine", "isCorrect": False},
                        {"text": "Verser de l'acide pur dans le siphon", "isCorrect": False},
                        {"text": "Graisser le mécanisme avec de l'huile moteur", "isCorrect": False}
                    ],
                    "correction": "Il est recommandé de tourner la molette de vidange du groupe de sécurité une fois par mois pour chasser les petits dépôts de tartre qui pourraient bloquer le clapet."
                },
                {
                    "questionNumber": 90,
                    "question": "Lors du débouchage chimique d'un évier avec un produit à base d'acide sulfurique, quel est le risque majeur ?",
                    "answerOptions": [
                        {"text": "Projection corrosive et réaction thermique violente", "isCorrect": True},
                        {"text": "Gel immédiat de la canalisation d'évacuation", "isCorrect": False},
                        {"text": "Coloration indélébile de la céramique en rose", "isCorrect": False},
                        {"text": "Émission d'un gaz hilarant inoffensif", "isCorrect": False}
                    ],
                    "correction": "Les déboucheurs acides sont très agressifs. Au contact de l'eau, ils provoquent une réaction exothermique (chaleur) et des projections qui peuvent gravement brûler la peau et les yeux."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel EPI est indispensable pour utiliser une meuleuse d'angle, en plus des gants ?",
                    "answerOptions": [
                        {"text": "Lunettes de protection", "isCorrect": True},
                        {"text": "Chaussures de ville", "isCorrect": False},
                        {"text": "Casquette en tissu", "isCorrect": False},
                        {"text": "Écharpe en laine", "isCorrect": False}
                    ],
                    "correction": "Les projections de limaille de fer ou d'éclats de disque sont fréquentes et très rapides. Les lunettes (ou visière) sont obligatoires pour éviter la cécité."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle est la cause la plus fréquente d'une mauvaise odeur provenant d'un siphon de sol peu utilisé ?",
                    "answerOptions": [
                        {"text": "L'évaporation de la garde d'eau", "isCorrect": True},
                        {"text": "La présence de rats dans le tuyau", "isCorrect": False},
                        {"text": "La décomposition du plastique", "isCorrect": False},
                        {"text": "La surpression du réseau public", "isCorrect": False}
                    ],
                    "correction": "Si un appareil n'est pas utilisé (chaufferie, buanderie), l'eau du siphon s'évapore. Le bouchon hydraulique disparaît et laisse passer l'air vicié des égouts."
                },
                {
                    "questionNumber": 93,
                    "question": "Sur un échafaudage roulant, que doit-on impérativement faire avant de monter dessus ?",
                    "answerOptions": [
                        {"text": "Bloquer les roues et mettre les stabilisateurs", "isCorrect": True},
                        {"text": "Demander à un collègue de tenir l'échelle", "isCorrect": False},
                        {"text": "Vérifier la pression des pneus à la main", "isCorrect": False},
                        {"text": "Graisser les montants verticaux", "isCorrect": False}
                    ],
                    "correction": "La stabilité est primordiale. Il faut bloquer les freins des roues et déployer les stabilisateurs latéraux pour éviter le basculement."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel type de raccord est interdit pour le gaz à l'intérieur des habitations (sauf exception très encadrée) ?",
                    "answerOptions": [
                        {"text": "Raccord à olive", "isCorrect": True},
                        {"text": "Raccord à braser", "isCorrect": False},
                        {"text": "Raccord à sertir gaz", "isCorrect": False},
                        {"text": "Raccord vissé conique", "isCorrect": False}
                    ],
                    "correction": "Les raccords mécaniques type 'bicône' ou 'olive' sont généralement interdits pour le gaz en intérieur car le risque de fuite par déserrage ou vibration est jugé trop important (se référer au référentiel gaz en vigueur)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la posture correcte pour utiliser une clé à molette afin d'éviter de se blesser en cas de ripage ?",
                    "answerOptions": [
                        {"text": "Tirer la clé vers soi", "isCorrect": True},
                        {"text": "Pousser la clé avec la paume", "isCorrect": False},
                        {"text": "Frapper sur la clé avec un marteau", "isCorrect": False},
                        {"text": "Utiliser un tube de rallonge", "isCorrect": False}
                    ],
                    "correction": "Il faut toujours 'tirer' la clé vers soi. Si on 'pousse' et que la clé ripe (glisse), la main part violemment vers l'avant et risque de heurter un obstacle blessant."
                },
                {
                    "questionNumber": 96,
                    "question": "Que doit-on vérifier avant de percer un mur dans une salle de bains rénovée ?",
                    "answerOptions": [
                        {"text": "L'absence de canalisations encastrées", "isCorrect": True},
                        {"text": "La marque de la peinture murale", "isCorrect": False},
                        {"text": "La température de la pièce", "isCorrect": False},
                        {"text": "L'épaisseur exacte de la faïence", "isCorrect": False}
                    ],
                    "correction": "Il faut utiliser un détecteur de métaux/matériaux pour éviter de percer une conduite d'eau ou une gaine électrique invisible noyée dans le mur."
                },
                {
                    "questionNumber": 97,
                    "question": "À quoi sert le 'thermocouple' sur un vieil appareil à gaz ?",
                    "answerOptions": [
                        {"text": "Couper le gaz si la veilleuse s'éteint", "isCorrect": True},
                        {"text": "Allumer le gaz automatiquement à distance", "isCorrect": False},
                        {"text": "Mesurer la consommation de gaz", "isCorrect": False},
                        {"text": "Filtrer les impuretés du gaz", "isCorrect": False}
                    ],
                    "correction": "Le thermocouple est une sécurité par flamme. Si la veilleuse s'éteint (courant d'air), le thermocouple refroidit et coupe l'arrivée de gaz pour éviter l'accumulation explosive."
                },
                {
                    "questionNumber": 98,
                    "question": "Comment doit-on stocker les bouteilles de gaz (oxygène/acétylène) dans le véhicule ou l'atelier ?",
                    "answerOptions": [
                        {"text": "Verticalement et arrimées solidement", "isCorrect": True},
                        {"text": "Couchées à plat sur le sol", "isCorrect": False},
                        {"text": "La tête en bas pour la pression", "isCorrect": False},
                        {"text": "En vrac les unes sur les autres", "isCorrect": False}
                    ],
                    "correction": "Les bouteilles doivent être stockées debout (verticalement) et attachées pour éviter qu'elles ne tombent et n'endommagent leurs robinets ('risque bouteille fusée')."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le symbole de danger représenté par un losange rouge contenant une flamme noire ?",
                    "answerOptions": [
                        {"text": "Inflammable", "isCorrect": True},
                        {"text": "Toxique", "isCorrect": False},
                        {"text": "Corrosif", "isCorrect": False},
                        {"text": "Explosif", "isCorrect": False}
                    ],
                    "correction": "Ce pictogramme (SGH02) indique que le produit (colle, solvant, gaz) peut s'enflammer facilement au contact d'une étincelle ou de la chaleur."
                },
                {
                    "questionNumber": 100,
                    "question": "En cas d'accident électrique (personne collée au fil), que faire en priorité absolue ?",
                    "answerOptions": [
                        {"text": "Couper le courant au disjoncteur", "isCorrect": True},
                        {"text": "Toucher la personne pour la rassurer", "isCorrect": False},
                        {"text": "Tirer la personne par les vêtements", "isCorrect": False},
                        {"text": "Appeler les pompiers avant tout", "isCorrect": False}
                    ],
                    "correction": "Il ne faut surtout pas toucher la victime tant qu'elle est sous tension (risque de sur-accident). La priorité est de couper l'énergie (disjoncteur ou arrêt d'urgence)."
                }
            ]
        }
    }
}