quiz_data = {
    "title": "Quiz BP Monteur en Installations du Génie Climatique et Sanitaire (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : SCIENCES APPLIQUÉES ET HYDRAULIQUE (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : SCIENCES APPLIQUÉES ET HYDRAULIQUE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est l'unité légale de pression dans le système international ?",
                    "answerOptions": [
                        {"text": "Le Pascal", "isCorrect": True},
                        {"text": "Le Bar relatif", "isCorrect": False},
                        {"text": "Le Mètre de colonne d'eau", "isCorrect": False},
                        {"text": "Le Millimètre de mercure", "isCorrect": False}
                    ],
                    "correction": "Le Pascal est l'unité officielle du système international, bien que le bar soit couramment utilisé en plomberie (1 bar vaut 100 000 Pascals)."
                },
                {
                    "questionNumber": 2,
                    "question": "Comment évolue la pression statique au fond d'une colonne d'eau si la hauteur double ?",
                    "answerOptions": [
                        {"text": "Elle double", "isCorrect": True},
                        {"text": "Elle reste constante", "isCorrect": False},
                        {"text": "Elle diminue de moitié", "isCorrect": False},
                        {"text": "Elle augmente de manière exponentielle selon le carré de la hauteur", "isCorrect": False}
                    ],
                    "correction": "La pression hydrostatique est proportionnelle à la hauteur de la colonne d'eau selon la formule P = ρgh (rho fois g fois h). Si h double, P double."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel phénomène physique provoque des bruits de claquement lors de la fermeture brutale d'une vanne ?",
                    "answerOptions": [
                        {"text": "Le coup de bélier", "isCorrect": True},
                        {"text": "La cavitation", "isCorrect": False},
                        {"text": "Le thermosiphon", "isCorrect": False},
                        {"text": "La dilatation thermique", "isCorrect": False}
                    ],
                    "correction": "Le coup de bélier est une onde de choc provoquée par une variation brusque de la vitesse d'un liquide dans une canalisation."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la conséquence directe d'une augmentation de la vitesse du fluide dans une tuyauterie ?",
                    "answerOptions": [
                        {"text": "Les pertes de charge augmentent", "isCorrect": True},
                        {"text": "La pression statique augmente", "isCorrect": False},
                        {"text": "La température du fluide diminue", "isCorrect": False},
                        {"text": "Le débit massique du fluide diminue", "isCorrect": False}
                    ],
                    "correction": "Les pertes de charge (frottements) augmentent proportionnellement au carré de la vitesse du fluide (formule de Darcy-Weisbach). Plus la vitesse est élevée, plus la chute de pression est importante."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel mode de transfert thermique ne nécessite aucun support matériel pour se propager ?",
                    "answerOptions": [
                        {"text": "Le rayonnement", "isCorrect": True},
                        {"text": "La convection", "isCorrect": False},
                        {"text": "La conduction", "isCorrect": False},
                        {"text": "L'advection", "isCorrect": False}
                    ],
                    "correction": "Le rayonnement thermique (infrarouge) peut se propager dans le vide, contrairement à la convection ou la conduction qui nécessitent de la matière."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel appareil permet de mesurer la pression atmosphérique ?",
                    "answerOptions": [
                        {"text": "Le baromètre", "isCorrect": True},
                        {"text": "Le manomètre", "isCorrect": False},
                        {"text": "Le débitmètre", "isCorrect": False},
                        {"text": "L'hygromètre", "isCorrect": False}
                    ],
                    "correction": "Le baromètre mesure la pression atmosphérique, tandis que le manomètre mesure la pression relative d'un fluide dans un circuit."
                },
                {
                    "questionNumber": 7,
                    "question": "Que représente le symbole 'Kv' pour une vanne de régulation ?",
                    "answerOptions": [
                        {"text": "Le débit d'eau en mètres cubes par heure pour une perte de charge de 1 bar", "isCorrect": True},
                        {"text": "La pression maximale admissible par le corps de la vanne en position fermée", "isCorrect": False},
                        {"text": "Le coefficient de dilatation du matériau constituant le siège de la vanne", "isCorrect": False},
                        {"text": "La température maximale de fonctionnement en régime permanent", "isCorrect": False}
                    ],
                    "correction": "Le Kv est la caractéristique hydraulique fondamentale d'une vanne, définissant sa capacité de débit normalisée (m³/h sous une ΔP de 1 bar)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la masse volumique de l'eau pure à une température de 4 degrés Celsius ?",
                    "answerOptions": [
                        {"text": "1000 kg/m3", "isCorrect": True},
                        {"text": "100 kg/m3", "isCorrect": False},
                        {"text": "10 kg/m3", "isCorrect": False},
                        {"text": "1 kg/m3", "isCorrect": False}
                    ],
                    "correction": "C'est à 4 degrés Celsius que l'eau atteint sa densité maximale, soit 1000 kilogrammes par mètre cube."
                },
                {
                    "questionNumber": 9,
                    "question": "Comment nomme-t-on la vaporisation locale du liquide à l'aspiration d'une pompe ?",
                    "answerOptions": [
                        {"text": "La cavitation", "isCorrect": True},
                        {"text": "La condensation", "isCorrect": False},
                        {"text": "La sublimation", "isCorrect": False},
                        {"text": "L'évaporation", "isCorrect": False}
                    ],
                    "correction": "La cavitation se produit quand la pression chute sous la tension de vapeur du liquide, créant des bulles qui implosent et endommagent la pompe."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle grandeur physique s'exprime en Watts ?",
                    "answerOptions": [
                        {"text": "La puissance", "isCorrect": True},
                        {"text": "L'énergie", "isCorrect": False},
                        {"text": "Le travail", "isCorrect": False},
                        {"text": "La chaleur latente", "isCorrect": False}
                    ],
                    "correction": "Le Watt est l'unité de puissance (Joule par seconde). L'énergie et le travail s'expriment en Joules."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est l'effet d'un coude brusque sur un réseau hydraulique par rapport à une ligne droite ?",
                    "answerOptions": [
                        {"text": "Il crée une perte de charge singulière", "isCorrect": True},
                        {"text": "Il augmente la pression dynamique", "isCorrect": False},
                        {"text": "Il annule les frottements visqueux", "isCorrect": False},
                        {"text": "Il favorise l'écoulement laminaire du fluide", "isCorrect": False}
                    ],
                    "correction": "Les accidents de parcours comme les coudes, tés ou réductions créent des pertes de charge singulières (locales) qui s'ajoutent aux pertes linéaires (frottements)."
                },
                {
                    "questionNumber": 12,
                    "question": "Dans quel type d'écoulement les filets de fluide sont-ils parallèles et réguliers ?",
                    "answerOptions": [
                        {"text": "Laminaire", "isCorrect": True},
                        {"text": "Turbulent", "isCorrect": False},
                        {"text": "Transitoire", "isCorrect": False},
                        {"text": "Critique", "isCorrect": False}
                    ],
                    "correction": "L'écoulement laminaire se caractérise par un mouvement fluide et régulier, contrairement à l'écoulement turbulent qui est agité et chaotique."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle formule permet de calculer le débit volumique ?",
                    "answerOptions": [
                        {"text": "Vitesse fois Section", "isCorrect": True},
                        {"text": "Vitesse divisée par Section", "isCorrect": False},
                        {"text": "Pression fois Vitesse", "isCorrect": False},
                        {"text": "Masse volumique fois Vitesse", "isCorrect": False}
                    ],
                    "correction": "Le débit (Q) est le produit de la vitesse d'écoulement (v) par la section de passage (S). Q = v x S."
                },
                {
                    "questionNumber": 14,
                    "question": "Que mesure-t-on en décibels ?",
                    "answerOptions": [
                        {"text": "Le niveau sonore", "isCorrect": True},
                        {"text": "La luminosité", "isCorrect": False},
                        {"text": "La conductivité", "isCorrect": False},
                        {"text": "La viscosité", "isCorrect": False}
                    ],
                    "correction": "Le décibel (dB) est l'unité utilisée pour mesurer l'intensité du bruit ou niveau de pression acoustique."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel matériau est le meilleur conducteur thermique parmi les suivants ?",
                    "answerOptions": [
                        {"text": "Le cuivre", "isCorrect": True},
                        {"text": "L'acier", "isCorrect": False},
                        {"text": "La fonte", "isCorrect": False},
                        {"text": "Le PER", "isCorrect": False}
                    ],
                    "correction": "Le cuivre possède une conductivité thermique très élevée, bien supérieure à l'acier, la fonte ou les matières plastiques comme le PER."
                },
                {
                    "questionNumber": 16,
                    "question": "Qu'est-ce que la chaleur sensible ?",
                    "answerOptions": [
                        {"text": "Une chaleur qui modifie la température sans changer l'état physique", "isCorrect": True},
                        {"text": "Une chaleur qui modifie l'état physique sans changer la température", "isCorrect": False},
                        {"text": "Une chaleur produite uniquement par frottement mécanique", "isCorrect": False},
                        {"text": "Une quantité de chaleur perdue par les parois non isolées", "isCorrect": False}
                    ],
                    "correction": "La chaleur sensible provoque une variation de température mesurable, à l'inverse de la chaleur latente qui provoque un changement d'état."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est la valeur de la pression atmosphérique standard au niveau de la mer ?",
                    "answerOptions": [
                        {"text": "1013 millibars", "isCorrect": True},
                        {"text": "100 Pascals", "isCorrect": False},
                        {"text": "760 Bars", "isCorrect": False},
                        {"text": "1 Bar absolu", "isCorrect": False}
                    ],
                    "correction": "La pression atmosphérique moyenne de référence est de 1013 hectopascals (ou millibars)."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel instrument permet de mesurer le débit d'un fluide dans une canalisation ?",
                    "answerOptions": [
                        {"text": "Un débitmètre", "isCorrect": True},
                        {"text": "Un anémomètre", "isCorrect": False},
                        {"text": "Un thermomètre", "isCorrect": False},
                        {"text": "Un pressostat", "isCorrect": False}
                    ],
                    "correction": "Comme son nom l'indique, le débitmètre est l'appareil spécifique pour la mesure du débit liquide ou gazeux."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle propriété du fluide influence directement les pertes de charge linéaires ?",
                    "answerOptions": [
                        {"text": "La viscosité", "isCorrect": True},
                        {"text": "La couleur", "isCorrect": False},
                        {"text": "L'opacité", "isCorrect": False},
                        {"text": "Le pH", "isCorrect": False}
                    ],
                    "correction": "La viscosité représente la résistance du fluide à l'écoulement ; plus un fluide est visqueux, plus les frottements et donc les pertes de charge sont importants."
                },
                {
                    "questionNumber": 20,
                    "question": "Que se passe-t-il si le NPSH disponible est inférieur au NPSH requis par la pompe ?",
                    "answerOptions": [
                        {"text": "La pompe cavite", "isCorrect": True},
                        {"text": "Le débit augmente", "isCorrect": False},
                        {"text": "Le moteur grille", "isCorrect": False},
                        {"text": "La HMT augmente", "isCorrect": False}
                    ],
                    "correction": "Pour éviter la cavitation, la pression à l'aspiration (NPSH disponible) doit impérativement être supérieure à la valeur minimale exigée par le constructeur (NPSH requis). Si elle est inférieure, la pompe cavite, ce qui endommage la turbine."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNOLOGIE DES INSTALLATIONS SANITAIRES ET ECS (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNOLOGIE DES INSTALLATIONS SANITAIRES ET ECS",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la couleur standardisée des vases d'expansion destinés aux installations sanitaires ?",
                    "answerOptions": [
                        {"text": "Blanc", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Gris", "isCorrect": False},
                        {"text": "Noir", "isCorrect": False}
                    ],
                    "correction": "Les vases d'expansion sanitaires sont généralement blancs (ou parfois bleus) et possèdent une membrane de qualité alimentaire, contrairement aux vases rouges réservés au chauffage."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel organe de sécurité est obligatoire sur l'entrée d'eau froide d'un ballon à accumulation ?",
                    "answerOptions": [
                        {"text": "Le groupe de sécurité", "isCorrect": True},
                        {"text": "Le vase d'expansion", "isCorrect": False},
                        {"text": "Le mitigeur thermostatique", "isCorrect": False},
                        {"text": "Le circulateur de bouclage", "isCorrect": False}
                    ],
                    "correction": "Le groupe de sécurité est obligatoire pour protéger la cuve contre les surpressions (taré à 7 bars) dues à la dilatation de l'eau lors de la chauffe."
                },
                {
                    "questionNumber": 23,
                    "question": "À quoi servent les 'eaux vannes' dans un réseau d'évacuation ?",
                    "answerOptions": [
                        {"text": "Aux toilettes", "isCorrect": True},
                        {"text": "Aux cuisines", "isCorrect": False},
                        {"text": "Aux salles de bains", "isCorrect": False},
                        {"text": "Aux eaux de pluie", "isCorrect": False}
                    ],
                    "correction": "On distingue les eaux vannes (WC) des eaux ménagères (cuisine, salle de bain). Les deux réunies forment les eaux usées."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel appareil permet d'augmenter la pression de l'eau dans un réseau de distribution ?",
                    "answerOptions": [
                        {"text": "Un surpresseur", "isCorrect": True},
                        {"text": "Un réducteur de pression", "isCorrect": False},
                        {"text": "Un disconnecteur", "isCorrect": False},
                        {"text": "Un clapet anti-pollution", "isCorrect": False}
                    ],
                    "correction": "Le surpresseur est une pompe (ou un groupe de pompes) destinée à élever la pression lorsque celle du réseau public est insuffisante."
                },
                {
                    "questionNumber": 25,
                    "question": "Quelle est la fonction principale d'une anode en magnésium dans un chauffe-eau ?",
                    "answerOptions": [
                        {"text": "Protéger la cuve contre la corrosion", "isCorrect": True},
                        {"text": "Chauffer l'eau par effet Joule", "isCorrect": False},
                        {"text": "Réguler la température de l'eau", "isCorrect": False},
                        {"text": "Mesurer le niveau de remplissage", "isCorrect": False}
                    ],
                    "correction": "L'anode sacrificielle en magnésium se corrode à la place de l'acier de la cuve, protégeant ainsi l'émail des micro-fissures."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle température de stockage minimale est recommandée pour prévenir les légionelles dans un ballon collectif ?",
                    "answerOptions": [
                        {"text": "55 degrés Celsius", "isCorrect": True},
                        {"text": "35 degrés Celsius", "isCorrect": False},
                        {"text": "40 degrés Celsius", "isCorrect": False},
                        {"text": "25 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "La réglementation impose une température de stockage d'au moins 55°C (souvent 60°C) pour tuer ou inhiber le développement des bactéries Legionella."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel dispositif empêche le retour de l'eau polluée du réseau privé vers le réseau public d'eau potable ?",
                    "answerOptions": [
                        {"text": "Un disconnecteur", "isCorrect": True},
                        {"text": "Un compteur d'eau", "isCorrect": False},
                        {"text": "Une vanne d'arrêt", "isCorrect": False},
                        {"text": "Un filtre à tamis", "isCorrect": False}
                    ],
                    "correction": "Le disconnecteur est un organe de sécurité spécifique qui crée une zone de séparation pour empêcher tout retour d'eau (antipollution)."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est l'unité de mesure de la dureté de l'eau (titre hydrotimétrique) en France ?",
                    "answerOptions": [
                        {"text": "Le degré français", "isCorrect": True},
                        {"text": "Le degré Kelvin", "isCorrect": False},
                        {"text": "Le milligramme par litre", "isCorrect": False},
                        {"text": "Le Siemens par mètre", "isCorrect": False}
                    ],
                    "correction": "La dureté de l'eau, représentant la teneur en calcium et magnésium, s'exprime en degrés français (°f)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel type de production d'ECS chauffe l'eau uniquement au moment du puisage ?",
                    "answerOptions": [
                        {"text": "La production instantanée", "isCorrect": True},
                        {"text": "La production par accumulation", "isCorrect": False},
                        {"text": "La production par semi-accumulation", "isCorrect": False},
                        {"text": "La production par hydro-accumulation", "isCorrect": False}
                    ],
                    "correction": "La production instantanée ne stocke pas d'eau chaude ; la puissance est délivrée en temps réel lors de l'ouverture du robinet."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel matériau de synthèse est couramment utilisé pour les évacuations d'eaux usées ?",
                    "answerOptions": [
                        {"text": "Le PVC", "isCorrect": True},
                        {"text": "Le PER", "isCorrect": False},
                        {"text": "Le Cuivre", "isCorrect": False},
                        {"text": "L'Acier noir", "isCorrect": False}
                    ],
                    "correction": "Le PVC (Polychlorure de Vinyle) est le standard pour les réseaux d'écoulement gravitaire en raison de sa légèreté et de sa facilité de mise en œuvre par collage."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le rôle d'un bouclage ECS dans un grand bâtiment ?",
                    "answerOptions": [
                        {"text": "Maintenir l'eau chaude disponible au robinet", "isCorrect": True},
                        {"text": "Augmenter la pression du réseau d'eau froide", "isCorrect": False},
                        {"text": "Récupérer l'eau de pluie pour les sanitaires", "isCorrect": False},
                        {"text": "Refroidir l'eau pour éviter les brûlures", "isCorrect": False}
                    ],
                    "correction": "Le bouclage fait circuler l'eau chaude en permanence pour qu'elle soit disponible immédiatement à l'ouverture du robinet, évitant le gaspillage de l'eau froide stagnante."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle pente minimale est généralement recommandée pour une évacuation d'eaux usées standard ?",
                    "answerOptions": [
                        {"text": "1 à 3 centimètres par mètre", "isCorrect": True},
                        {"text": "10 centimètres par mètre", "isCorrect": False},
                        {"text": "45 degrés d'inclinaison", "isCorrect": False},
                        {"text": "90 degrés d'inclinaison", "isCorrect": False}
                    ],
                    "correction": "Une pente comprise entre 1 et 3 % (cm/m) assure un bon écoulement et l'autocurage des canalisations sans siphonnage."
                },
                {
                    "questionNumber": 33,
                    "question": "Que signifie l'acronyme PER en plomberie ?",
                    "answerOptions": [
                        {"text": "Polyéthylène Réticulé", "isCorrect": True},
                        {"text": "Plastique En Rouleau", "isCorrect": False},
                        {"text": "Polypropylène Extrudé Renforcé", "isCorrect": False},
                        {"text": "Polychlorure Élastomère Résistant", "isCorrect": False}
                    ],
                    "correction": "Le PER (ou PEX) est un tube en polyéthylène ayant subi une réticulation pour résister à la pression et à la température."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle pièce de robinetterie permet de régler la température de l'eau au degré près ?",
                    "answerOptions": [
                        {"text": "Le mitigeur thermostatique", "isCorrect": True},
                        {"text": "Le mélangeur manuel", "isCorrect": False},
                        {"text": "Le robinet temporisé", "isCorrect": False},
                        {"text": "La vanne papillon", "isCorrect": False}
                    ],
                    "correction": "Le mitigeur thermostatique ajuste automatiquement le mélange eau chaude/eau froide pour maintenir une température de sortie constante."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel gaz est principalement utilisé comme combustible dans les chauffe-bains gaz ?",
                    "answerOptions": [
                        {"text": "Le gaz naturel", "isCorrect": True},
                        {"text": "L'acétylène", "isCorrect": False},
                        {"text": "L'hydrogène", "isCorrect": False},
                        {"text": "L'azote", "isCorrect": False}
                    ],
                    "correction": "Les chauffe-bains sont généralement alimentés au gaz naturel (réseau de ville) ou au butane/propane (bouteilles/citernes)."
                },
                {
                    "questionNumber": 36,
                    "question": "À quelle pression le groupe de sécurité d'un chauffe-eau électrique standard s'ouvre-t-il ?",
                    "answerOptions": [
                        {"text": "7 bars", "isCorrect": True},
                        {"text": "3 bars", "isCorrect": False},
                        {"text": "10 bars", "isCorrect": False},
                        {"text": "1 bar", "isCorrect": False}
                    ],
                    "correction": "La soupape du groupe de sécurité est tarée à 7 bars pour évacuer l'eau lors de la dilatation thermique."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment appelle-t-on le traitement de l'eau visant à supprimer le calcaire ?",
                    "answerOptions": [
                        {"text": "L'adoucissement", "isCorrect": True},
                        {"text": "La chloration", "isCorrect": False},
                        {"text": "La filtration", "isCorrect": False},
                        {"text": "L'osmose", "isCorrect": False}
                    ],
                    "correction": "L'adoucisseur fonctionne par échange d'ions (remplacement du calcium et magnésium par du sodium) pour supprimer le calcaire."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est l'inconvénient principal d'une production d'ECS instantanée électrique ?",
                    "answerOptions": [
                        {"text": "Elle nécessite une très forte puissance électrique", "isCorrect": True},
                        {"text": "Elle prend beaucoup de place dans le logement", "isCorrect": False},
                        {"text": "Elle favorise le développement des bactéries", "isCorrect": False},
                        {"text": "Elle nécessite obligatoirement une cheminée", "isCorrect": False}
                    ],
                    "correction": "Pour chauffer l'eau instantanément avec un débit correct, il faut une puissance électrique très élevée (souvent triphasée pour les gros débits)."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel élément assure l'étanchéité sur un raccord à visser sans joint plat ?",
                    "answerOptions": [
                        {"text": "La filasse", "isCorrect": True},
                        {"text": "Le mastic silicone", "isCorrect": False},
                        {"text": "La colle PVC", "isCorrect": False},
                        {"text": "Le ruban adhésif", "isCorrect": False}
                    ],
                    "correction": "La filasse (chanvre) associée à de la pâte à joint est la méthode traditionnelle et efficace pour l'étanchéité des filetages métalliques."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la conséquence d'une vitesse d'eau trop élevée dans les canalisations sanitaires ?",
                    "answerOptions": [
                        {"text": "L'érosion des tubes et du bruit", "isCorrect": True},
                        {"text": "Le dépôt rapide de calcaire", "isCorrect": False},
                        {"text": "La prolifération des algues", "isCorrect": False},
                        {"text": "La chute de pression statique", "isCorrect": False}
                    ],
                    "correction": "Une vitesse excessive (> 2 m/s) provoque une usure prématurée des tubes (érosion) et des nuisances acoustiques importantes."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : CHAUFFAGE ET ÉNERGIES RENOUVELABLES (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : CHAUFFAGE ET ÉNERGIES RENOUVELABLES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la pression de tarage standard d'une soupape de sécurité pour une chaudière murale domestique ?",
                    "answerOptions": [
                        {"text": "3 bars", "isCorrect": True},
                        {"text": "7 bars", "isCorrect": False},
                        {"text": "10 bars", "isCorrect": False},
                        {"text": "1,5 bar", "isCorrect": False}
                    ],
                    "correction": "Sur le circuit primaire chauffage, la soupape de sécurité est tarée à 3 bars pour protéger le circuit fermé. La valeur de 7 bars concerne le sanitaire."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le principe de fonctionnement d'une chaudière à condensation ?",
                    "answerOptions": [
                        {"text": "Elle récupère la chaleur latente contenue dans les fumées", "isCorrect": True},
                        {"text": "Elle utilise une résistance électrique pour surchauffer l'eau", "isCorrect": False},
                        {"text": "Elle condense le gaz naturel avant de le brûler", "isCorrect": False},
                        {"text": "Elle mélange l'air et l'eau pour améliorer la combustion", "isCorrect": False}
                    ],
                    "correction": "La condensation permet de récupérer l'énergie contenue dans la vapeur d'eau des fumées, augmentant ainsi le rendement global sur PCI."
                },
                {
                    "questionNumber": 43,
                    "question": "Que signifie l'acronyme COP pour une pompe à chaleur ?",
                    "answerOptions": [
                        {"text": "Coefficient de Performance", "isCorrect": True},
                        {"text": "Capacité Onirique de Puissance", "isCorrect": False},
                        {"text": "Contrôle d'Opération Programmable", "isCorrect": False},
                        {"text": "Circuit Ouvert de Pompe", "isCorrect": False}
                    ],
                    "correction": "Le COP est le rapport entre la puissance thermique restituée et la puissance électrique consommée par la pompe à chaleur."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel fluide caloporteur est généralement utilisé dans les capteurs solaires thermiques ?",
                    "answerOptions": [
                        {"text": "De l'eau glycolée", "isCorrect": True},
                        {"text": "De l'huile minérale", "isCorrect": False},
                        {"text": "De l'eau pure", "isCorrect": False},
                        {"text": "Du fioul domestique", "isCorrect": False}
                    ],
                    "correction": "L'ajout de glycol à l'eau est indispensable pour empêcher le fluide de geler dans les capteurs extérieurs en hiver."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel composant permet de dissocier hydrauliquement le circuit primaire (production) du circuit secondaire (distribution) ?",
                    "answerOptions": [
                        {"text": "La bouteille de découplage", "isCorrect": True},
                        {"text": "Le vase d'expansion", "isCorrect": False},
                        {"text": "La vanne trois voies", "isCorrect": False},
                        {"text": "Le clapet anti-retour", "isCorrect": False}
                    ],
                    "correction": "La bouteille de découplage (ou casse-pression) permet de rendre les débits du primaire et du secondaire indépendants l'un de l'autre."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la température maximale de surface autorisée par la réglementation pour un plancher chauffant ?",
                    "answerOptions": [
                        {"text": "28 degrés Celsius", "isCorrect": True},
                        {"text": "35 degrés Celsius", "isCorrect": False},
                        {"text": "50 degrés Celsius", "isCorrect": False},
                        {"text": "19 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "Pour des raisons de confort physiologique (éviter les jambes lourdes), la température au sol ne doit jamais dépasser 28°C."
                },
                {
                    "questionNumber": 47,
                    "question": "Dans une pompe à chaleur, quel organe a pour fonction de comprimer le fluide frigorigène à l'état gazeux ?",
                    "answerOptions": [
                        {"text": "Le compresseur", "isCorrect": True},
                        {"text": "L'évaporateur", "isCorrect": False},
                        {"text": "Le détendeur", "isCorrect": False},
                        {"text": "Le condenseur", "isCorrect": False}
                    ],
                    "correction": "Le compresseur aspire les vapeurs basse pression venant de l'évaporateur et les refoule à haute pression vers le condenseur."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'avantage principal d'un réseau de chauffage bitube par rapport au monotube ?",
                    "answerOptions": [
                        {"text": "Tous les radiateurs reçoivent de l'eau à la même température", "isCorrect": True},
                        {"text": "L'installation nécessite beaucoup moins de longueur de tuyauterie", "isCorrect": False},
                        {"text": "Le diamètre des tuyaux est identique sur toute l'installation", "isCorrect": False},
                        {"text": "Il n'est pas nécessaire d'installer un circulateur de chauffage", "isCorrect": False}
                    ],
                    "correction": "En bitube, les émetteurs sont montés en parallèle, assurant une température d'entrée homogène, contrairement au monotube (série) où la température chute d'un radiateur à l'autre."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel dispositif permet d'absorber les variations de volume de l'eau de chauffage dues aux changements de température ?",
                    "answerOptions": [
                        {"text": "Le vase d'expansion", "isCorrect": True},
                        {"text": "Le purgeur automatique", "isCorrect": False},
                        {"text": "Le disconnecteur", "isCorrect": False},
                        {"text": "Le filtre à boue", "isCorrect": False}
                    ],
                    "correction": "L'eau se dilate en chauffant. Le vase d'expansion, grâce à sa membrane et son gaz compressible (azote), absorbe ce surplus de volume pour maintenir une pression stable."
                },
                {
                    "questionNumber": 50,
                    "question": "Qu'indique le PCI d'un combustible ?",
                    "answerOptions": [
                        {"text": "Le Pouvoir Calorifique Inférieur", "isCorrect": True},
                        {"text": "La Pression Critique Interne", "isCorrect": False},
                        {"text": "Le Potentiel de Combustion Initial", "isCorrect": False},
                        {"text": "La Puissance Calorifique Instantanée", "isCorrect": False}
                    ],
                    "correction": "Le PCI est la quantité de chaleur dégagée par la combustion sans récupérer la chaleur latente de la vapeur d'eau des fumées."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel type d'émetteur de chaleur fonctionne principalement par rayonnement à basse température ?",
                    "answerOptions": [
                        {"text": "Le plancher chauffant", "isCorrect": True},
                        {"text": "Le convecteur électrique", "isCorrect": False},
                        {"text": "L'aérotherme gaz", "isCorrect": False},
                        {"text": "Le ventilo-convecteur", "isCorrect": False}
                    ],
                    "correction": "Le plancher chauffant émet sa chaleur majoritairement par rayonnement (grande surface), offrant un meilleur confort que la convection pure."
                },
                {
                    "questionNumber": 52,
                    "question": "Sur une vanne 3 voies mélangeuse, où se trouve généralement l'entrée d'eau chaude venant de la chaudière ?",
                    "answerOptions": [
                        {"text": "Sur la voie latérale", "isCorrect": True},
                        {"text": "Sur la voie commune", "isCorrect": False},
                        {"text": "Sur la voie de retour", "isCorrect": False},
                        {"text": "Sur l'axe du servomoteur", "isCorrect": False}
                    ],
                    "correction": "Elle mélange une partie de l'eau chaude venant de la chaudière avec de l'eau plus froide venant du retour radiateurs pour obtenir la température de départ exacte souhaitée. La voie latérale est souvent l'entrée chaude (départ chaudière)."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle du pot à boue sur un circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Capter les oxydes métalliques et les impuretés", "isCorrect": True},
                        {"text": "Stocker l'excès de fluide caloporteur", "isCorrect": False},
                        {"text": "Réchauffer l'eau de retour radiateur", "isCorrect": False},
                        {"text": "Mesurer la pression différentielle du circuit", "isCorrect": False}
                    ],
                    "correction": "Le pot à boues (ou désemboueur) piège les particules en suspension (oxydes, boues) qui pourraient endommager les échangeurs ou les circulateurs."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle source d'énergie utilise une pompe à chaleur géothermique sur nappe phréatique ?",
                    "answerOptions": [
                        {"text": "La chaleur de l'eau souterraine", "isCorrect": True},
                        {"text": "La chaleur de l'air extérieur", "isCorrect": False},
                        {"text": "La chaleur des rayons du soleil", "isCorrect": False},
                        {"text": "La chaleur du sol par capteurs horizontaux", "isCorrect": False}
                    ],
                    "correction": "La géothermie sur nappe (système eau/eau) pompe les calories présentes dans l'eau de la nappe phréatique, dont la température est constante."
                },
                {
                    "questionNumber": 55,
                    "question": "À quoi sert un té de réglage sur un radiateur ?",
                    "answerOptions": [
                        {"text": "À équilibrer le débit d'eau", "isCorrect": True},
                        {"text": "À purger l'air du radiateur", "isCorrect": False},
                        {"text": "À fermer l'arrivée d'eau", "isCorrect": False},
                        {"text": "À vidanger le radiateur", "isCorrect": False}
                    ],
                    "correction": "Le té de réglage, situé sur le retour, permet de limiter le débit de sortie pour équilibrer hydrauliquement les radiateurs entre eux."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'effet d'une température de retour trop élevée sur une chaudière à condensation ?",
                    "answerOptions": [
                        {"text": "Le rendement diminue car la condensation ne se produit pas", "isCorrect": True},
                        {"text": "Le rendement augmente grâce à une meilleure combustion", "isCorrect": False},
                        {"text": "La chaudière se met immédiatement en sécurité surchauffe", "isCorrect": False},
                        {"text": "La production de condensats acides devient trop importante", "isCorrect": False}
                    ],
                    "correction": "Pour condenser, la température de retour doit être inférieure au point de rosée des fumées (environ 55-57°C pour le gaz). Si elle est trop élevée, la chaudière ne condense plus, et le rendement chute fortement."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel organe assure la circulation forcée de l'eau dans l'installation de chauffage ?",
                    "answerOptions": [
                        {"text": "Le circulateur", "isCorrect": True},
                        {"text": "L'accélérateur", "isCorrect": False},
                        {"text": "Le compresseur", "isCorrect": False},
                        {"text": "L'extracteur", "isCorrect": False}
                    ],
                    "correction": "Le circulateur (autrefois appelé accélérateur) crée la différence de pression nécessaire pour vaincre les pertes de charge et faire circuler l'eau."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment appelle-t-on le phénomène de circulation naturelle de l'eau chaude sans pompe, dû à la différence de densité ?",
                    "answerOptions": [
                        {"text": "Thermosiphon", "isCorrect": True},
                        {"text": "Thermoformage", "isCorrect": False},
                        {"text": "Thermorégulation", "isCorrect": False},
                        {"text": "Thermodynamique", "isCorrect": False}
                    ],
                    "correction": "L'eau chaude est moins dense que l'eau froide et a tendance à monter naturellement. C'est le principe du thermosiphon, utilisé dans les anciennes installations."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel combustible solide se présente sous forme de petits cylindres de bois compressé ?",
                    "answerOptions": [
                        {"text": "Les granulés", "isCorrect": True},
                        {"text": "Les plaquettes", "isCorrect": False},
                        {"text": "Les bûches", "isCorrect": False},
                        {"text": "Le charbon", "isCorrect": False}
                    ],
                    "correction": "Les granulés de bois (ou pellets) sont normalisés et permettent une alimentation automatique des chaudières, contrairement aux bûches."
                },
                {
                    "questionNumber": 60,
                    "question": "Dans un circuit frigorifique, quel changement d'état se produit dans l'évaporateur ?",
                    "answerOptions": [
                        {"text": "Le fluide passe de liquide à gaz", "isCorrect": True},
                        {"text": "Le fluide passe de gaz à liquide", "isCorrect": False},
                        {"text": "Le fluide passe de solide à gaz", "isCorrect": False},
                        {"text": "Le fluide passe de liquide à solide", "isCorrect": False}
                    ],
                    "correction": "Dans l'évaporateur, le fluide frigorigène capte les calories de la source froide et s'évapore (ébullition) pour devenir gazeux (ou vapeur basse pression)."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : AÉRAULIQUE, VENTILATION ET CLIMATISATION (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : AÉRAULIQUE, VENTILATION ET CLIMATISATION",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le principe fondamental du balayage de l'air dans un logement équipé d'une VMC ?",
                    "answerOptions": [
                        {"text": "L'air neuf entre par les pièces sèches et l'air vicié sort par les pièces humides", "isCorrect": True},
                        {"text": "L'air neuf entre par les pièces humides et l'air vicié sort par les pièces sèches", "isCorrect": False},
                        {"text": "L'air est insufflé et extrait simultanément dans chaque pièce du logement", "isCorrect": False},
                        {"text": "L'air circule en boucle fermée entre la cuisine et les chambres sans apport extérieur", "isCorrect": False}
                    ],
                    "correction": "Pour assainir le logement, l'air frais doit traverser les pièces de vie (salon, chambres) avant de se charger d'humidité et d'odeurs dans les pièces techniques (cuisine, SDB, WC) pour être extrait."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel appareil de mesure permet de déterminer l'humidité relative de l'air ambiant ?",
                    "answerOptions": [
                        {"text": "L'hygromètre", "isCorrect": True},
                        {"text": "Le manomètre", "isCorrect": False},
                        {"text": "L'anémomètre", "isCorrect": False},
                        {"text": "Le tachymètre", "isCorrect": False}
                    ],
                    "correction": "L'hygromètre est l'instrument dédié à la mesure du taux d'humidité dans l'air."
                },
                {
                    "questionNumber": 63,
                    "question": "Que signifie le sigle CTA en génie climatique ?",
                    "answerOptions": [
                        {"text": "Centrale de Traitement d'Air", "isCorrect": True},
                        {"text": "Circuit Thermique Autonome", "isCorrect": False},
                        {"text": "Climatisation Tertiaire Avancée", "isCorrect": False},
                        {"text": "Coefficient de Transmission Aéraulique", "isCorrect": False}
                    ],
                    "correction": "Une CTA est un équipement centralisé qui modifie les caractéristiques de l'air (température, humidité, propreté) avant de le distribuer dans les locaux."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est l'avantage énergétique principal d'une VMC double flux par rapport à une simple flux ?",
                    "answerOptions": [
                        {"text": "Elle récupère les calories de l'air extrait pour préchauffer l'air neuf", "isCorrect": True},
                        {"text": "Elle ne consomme absolument aucune énergie électrique pour fonctionner", "isCorrect": False},
                        {"text": "Elle permet de supprimer totalement le système de chauffage du bâtiment", "isCorrect": False},
                        {"text": "Elle utilise l'énergie solaire pour faire tourner les ventilateurs d'extraction", "isCorrect": False}
                    ],
                    "correction": "Grâce à un échangeur thermique, la VMC double flux croise les flux d'air (sans les mélanger) pour récupérer la chaleur de l'air vicié sortant."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est l'unité usuelle pour exprimer un débit de ventilation en bâtiment ?",
                    "answerOptions": [
                        {"text": "Le mètre cube par heure", "isCorrect": True},
                        {"text": "Le mètre par seconde", "isCorrect": False},
                        {"text": "Le Pascal", "isCorrect": False},
                        {"text": "Le Watt", "isCorrect": False}
                    ],
                    "correction": "Les débits d'air en ventilation se dimensionnent et se règlent en mètres cubes par heure (m³/h)."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel phénomène physique permet de déshumidifier l'air lors de son passage sur une batterie froide ?",
                    "answerOptions": [
                        {"text": "La condensation", "isCorrect": True},
                        {"text": "L'évaporation", "isCorrect": False},
                        {"text": "La fusion", "isCorrect": False},
                        {"text": "La sublimation", "isCorrect": False}
                    ],
                    "correction": "Lorsque l'air humide touche une surface dont la température est inférieure à son point de rosée, la vapeur d'eau se condense (devient liquide) et l'air s'assèche."
                },
                {
                    "questionNumber": 67,
                    "question": "À quoi correspond la classe de filtration G4 ou F7 pour un filtre à air ?",
                    "answerOptions": [
                        {"text": "À son efficacité de filtration", "isCorrect": True},
                        {"text": "À sa résistance au feu", "isCorrect": False},
                        {"text": "À son épaisseur en millimètres", "isCorrect": False},
                        {"text": "À sa perte de charge maximale", "isCorrect": False}
                    ],
                    "correction": "Les classes (G pour Grossier, F ou M pour Moyen/Fin) indiquent la capacité du filtre à arrêter des particules de plus en plus fines."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le rôle d'un clapet coupe-feu dans un réseau de gaines ?",
                    "answerOptions": [
                        {"text": "Obturer la gaine pour empêcher la propagation du feu", "isCorrect": True},
                        {"text": "Éteindre le feu en injectant de l'eau", "isCorrect": False},
                        {"text": "Déclencher l'alarme sonore du bâtiment", "isCorrect": False},
                        {"text": "Filtrer les fumées toxiques", "isCorrect": False}
                    ],
                    "correction": "Le clapet coupe-feu se ferme automatiquement (par fusible thermique ou commande) pour compartimenter le réseau et éviter que les gaines ne propagent l'incendie."
                },
                {
                    "questionNumber": 69,
                    "question": "Comment appelle-t-on la température à laquelle la vapeur d'eau contenue dans l'air commence à se condenser ?",
                    "answerOptions": [
                        {"text": "Le point de rosée", "isCorrect": True},
                        {"text": "Le point de givre", "isCorrect": False},
                        {"text": "Le bulbe humide", "isCorrect": False},
                        {"text": "Le zéro absolu", "isCorrect": False}
                    ],
                    "correction": "Le point de rosée est la température limite à laquelle l'air devient saturé en humidité (100% HR) et où les premières gouttelettes d'eau apparaissent."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel matériau est le plus couramment utilisé pour fabriquer des réseaux de ventilation rigides rectangulaires ?",
                    "answerOptions": [
                        {"text": "L'acier galvanisé", "isCorrect": True},
                        {"text": "Le cuivre recuit", "isCorrect": False},
                        {"text": "La fonte ductile", "isCorrect": False},
                        {"text": "Le plomb laminé", "isCorrect": False}
                    ],
                    "correction": "L'acier galvanisé (tôle 'galva') est le standard pour les gaines de ventilation en raison de sa résistance, de son coût et de sa tenue à la corrosion."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est la vitesse d'air maximale recommandée dans la zone d'occupation pour éviter l'inconfort (courants d'air) ?",
                    "answerOptions": [
                        {"text": "0,2 mètre par seconde", "isCorrect": True},
                        {"text": "2 mètres par seconde", "isCorrect": False},
                        {"text": "5 mètres par seconde", "isCorrect": False},
                        {"text": "10 mètres par seconde", "isCorrect": False}
                    ],
                    "correction": "Au-delà de 0,2 m/s, le mouvement de l'air devient perceptible par la peau et crée une sensation d'inconfort thermique (courant d'air)."
                },
                {
                    "questionNumber": 72,
                    "question": "Qu'est-ce que le 'Free Cooling' en climatisation ?",
                    "answerOptions": [
                        {"text": "Utiliser l'air extérieur frais pour refroidir le bâtiment sans utiliser le groupe froid", "isCorrect": True},
                        {"text": "Ouvrir les fenêtres manuellement pour créer un courant d'air traversant", "isCorrect": False},
                        {"text": "Distribuer gratuitement de la glace aux occupants du bâtiment", "isCorrect": False},
                        {"text": "Utiliser l'eau du réseau incendie pour refroidir les batteries de la centrale", "isCorrect": False}
                    ],
                    "correction": "Le Free Cooling consiste à introduire massivement de l'air extérieur (souvent la nuit) lorsque sa température est inférieure à celle du bâtiment, économisant ainsi l'énergie du compresseur frigorifique."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel composant terminal permet de diriger et diffuser l'air traité dans un local ?",
                    "answerOptions": [
                        {"text": "Le diffuseur", "isCorrect": True},
                        {"text": "Le registre", "isCorrect": False},
                        {"text": "Le piège à son", "isCorrect": False},
                        {"text": "Le pressostat", "isCorrect": False}
                    ],
                    "correction": "Les diffuseurs (plafonniers, muraux, tourbillonnaires) assurent le mélange de l'air soufflé avec l'air ambiant dans la zone de confort."
                },
                {
                    "questionNumber": 74,
                    "question": "Dans quel cas met-on un local en surpression par rapport aux locaux voisins ?",
                    "answerOptions": [
                        {"text": "Pour empêcher les contaminants extérieurs d'entrer", "isCorrect": True},
                        {"text": "Pour empêcher les odeurs du local de sortir", "isCorrect": False},
                        {"text": "Pour faciliter l'ouverture des portes vers l'intérieur", "isCorrect": False},
                        {"text": "Pour réduire la consommation du ventilateur de soufflage", "isCorrect": False}
                    ],
                    "correction": "La surpression (comme dans un bloc opératoire) garantit que l'air fuit vers l'extérieur, empêchant les poussières et bactéries d'entrer."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel instrument permet de mesurer la vitesse de l'air dans une gaine ?",
                    "answerOptions": [
                        {"text": "L'anémomètre", "isCorrect": True},
                        {"text": "Le baromètre", "isCorrect": False},
                        {"text": "Le thermomètre", "isCorrect": False},
                        {"text": "L'ohmmètre", "isCorrect": False}
                    ],
                    "correction": "L'anémomètre (à fil chaud ou à hélice) mesure la vitesse de l'écoulement d'air, ce qui permet ensuite de calculer le débit."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle est la fonction d'une bouche d'extraction hygroréglable ?",
                    "answerOptions": [
                        {"text": "Moduler le débit d'air en fonction de l'humidité de la pièce", "isCorrect": True},
                        {"text": "Régler la température de l'air extrait vers l'extérieur", "isCorrect": False},
                        {"text": "Filtrer l'air avant son rejet dans l'atmosphère", "isCorrect": False},
                        {"text": "Mesurer la consommation électrique du ventilateur", "isCorrect": False}
                    ],
                    "correction": "Une bouche hygroréglable possède une tresse en nylon qui s'allonge ou se raccourcit selon l'humidité, ouvrant ou fermant le clapet pour adapter le débit aux besoins."
                },
                {
                    "questionNumber": 77,
                    "question": "Sur un diagramme de l'air humide (psychrométrique), que représente l'axe horizontal ?",
                    "answerOptions": [
                        {"text": "La température sèche", "isCorrect": True},
                        {"text": "L'humidité absolue", "isCorrect": False},
                        {"text": "L'enthalpie spécifique", "isCorrect": False},
                        {"text": "La pression de vapeur", "isCorrect": False}
                    ],
                    "correction": "L'axe des abscisses (horizontal) représente la température sèche (en °C), tandis que l'axe vertical représente généralement l'humidité absolue. "
                },
                {
                    "questionNumber": 78,
                    "question": "Quel type de ventilateur est capable de fournir des pressions élevées pour vaincre de fortes pertes de charge ?",
                    "answerOptions": [
                        {"text": "Le ventilateur centrifuge", "isCorrect": True},
                        {"text": "Le ventilateur hélicoïde", "isCorrect": False},
                        {"text": "Le ventilateur de plafond", "isCorrect": False},
                        {"text": "Le brasseur d'air", "isCorrect": False}
                    ],
                    "correction": "Le ventilateur centrifuge (ou radial) aspire l'air axialement et le rejette radialement, créant une pression bien supérieure aux ventilateurs hélicoïdes (axiaux)."
                },
                {
                    "questionNumber": 79,
                    "question": "Pourquoi isole-t-on thermiquement les gaines de ventilation passant dans des combles non chauffés ?",
                    "answerOptions": [
                        {"text": "Pour éviter la condensation à l'intérieur ou à l'extérieur de la gaine", "isCorrect": True},
                        {"text": "Pour améliorer l'acoustique du réseau aéraulique", "isCorrect": False},
                        {"text": "Pour renforcer la rigidité mécanique de la gaine", "isCorrect": False},
                        {"text": "Pour empêcher les rongeurs de percer la gaine", "isCorrect": False}
                    ],
                    "correction": "L'isolation évite que l'air chaud transporté ne refroidisse (perte d'énergie) et surtout qu'il ne condense au contact de la paroi froide (problèmes d'eau)."
                },
                {
                    "questionNumber": 80,
                    "question": "Que mesure-t-on en Pascals dans un réseau aéraulique ?",
                    "answerOptions": [
                        {"text": "La pression", "isCorrect": True},
                        {"text": "Le débit", "isCorrect": False},
                        {"text": "La température", "isCorrect": False},
                        {"text": "La vitesse", "isCorrect": False}
                    ],
                    "correction": "Le Pascal (Pa) mesure la pression statique ou dynamique de l'air, ainsi que les pertes de charge (résistance à l'écoulement) du réseau."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : ÉLECTRICITÉ, RÉGULATION ET MISE EN SERVICE (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : ÉLECTRICITÉ, RÉGULATION ET MISE EN SERVICE",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la couleur normalisée du conducteur de Neutre dans une installation électrique domestique ?",
                    "answerOptions": [
                        {"text": "Bleu", "isCorrect": True},
                        {"text": "Rouge", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False},
                        {"text": "Noir", "isCorrect": False}
                    ],
                    "correction": "Le conducteur de neutre doit obligatoirement être bleu clair. La phase est souvent rouge, noire ou marron, et la terre est vert-jaune."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel appareil protège l'installation électrique contre les courts-circuits et les surcharges ?",
                    "answerOptions": [
                        {"text": "Le disjoncteur", "isCorrect": True},
                        {"text": "Le sectionneur", "isCorrect": False},
                        {"text": "Le contacteur", "isCorrect": False},
                        {"text": "Le télérupteur", "isCorrect": False}
                    ],
                    "correction": "Le disjoncteur magnéto-thermique coupe le courant en cas de surintensité (magnétique pour le court-circuit, thermique pour la surcharge)."
                },
                {
                    "questionNumber": 83,
                    "question": "Sur quel principe fonctionne une régulation par 'loi d'eau' ?",
                    "answerOptions": [
                        {"text": "La température de départ chauffage varie selon la température extérieure", "isCorrect": True},
                        {"text": "La température de la chaudière est maintenue constante toute l'année", "isCorrect": False},
                        {"text": "Le circulateur s'arrête dès que le robinet d'eau chaude est fermé", "isCorrect": False},
                        {"text": "La pression du réseau augmente proportionnellement à la hauteur du bâtiment", "isCorrect": False}
                    ],
                    "correction": "La loi d'eau ajuste la température de l'eau envoyée dans les radiateurs en fonction de la température extérieure mesurée par une sonde, pour anticiper les besoins du bâtiment."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle grandeur électrique se mesure avec un ohmmètre ?",
                    "answerOptions": [
                        {"text": "La résistance", "isCorrect": True},
                        {"text": "L'intensité", "isCorrect": False},
                        {"text": "La tension", "isCorrect": False},
                        {"text": "La puissance", "isCorrect": False}
                    ],
                    "correction": "L'ohmmètre mesure la résistance électrique d'un composant (en Ohms). Attention, cette mesure se fait toujours hors tension."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le rôle principal d'un interrupteur différentiel 30 mA en tête d'installation ?",
                    "answerOptions": [
                        {"text": "Protéger les personnes contre les contacts directs et indirects", "isCorrect": True},
                        {"text": "Protéger les moteurs électriques contre les échauffements anormaux", "isCorrect": False},
                        {"text": "Couper l'alimentation générale en cas de coupure de gaz", "isCorrect": False},
                        {"text": "Réguler la tension fournie par le distributeur d'énergie", "isCorrect": False}
                    ],
                    "correction": "Le dispositif différentiel à haute sensibilité (30mA) détecte les fuites de courant vers la terre (défaut d'isolement) et coupe le circuit pour éviter l'électrocution des personnes."
                },
                {
                    "questionNumber": 86,
                    "question": "Comment doit-on brancher un ampèremètre pour mesurer l'intensité d'un circuit ?",
                    "answerOptions": [
                        {"text": "En série", "isCorrect": True},
                        {"text": "En parallèle", "isCorrect": False},
                        {"text": "En dérivation", "isCorrect": False},
                        {"text": "En triangle", "isCorrect": False}
                    ],
                    "correction": "L'ampèremètre doit être traversé par le courant pour le mesurer, il se place donc toujours en série. Le voltmètre se place en parallèle."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel composant permet de détecter la présence de flamme sur un brûleur gaz moderne ?",
                    "answerOptions": [
                        {"text": "La sonde d'ionisation", "isCorrect": True},
                        {"text": "Le thermocouple", "isCorrect": False},
                        {"text": "Le pressostat", "isCorrect": False},
                        {"text": "Le gicleur", "isCorrect": False}
                    ],
                    "correction": "La sonde d'ionisation utilise la conductivité électrique de la flamme pour confirmer sa présence à la carte électronique de sécurité."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce que l'hystérésis d'un thermostat ?",
                    "answerOptions": [
                        {"text": "L'écart de température entre l'enclenchement et l'arrêt du chauffage", "isCorrect": True},
                        {"text": "La durée de vie maximale de la pile du thermostat", "isCorrect": False},
                        {"text": "La distance maximale entre le thermostat et la chaudière", "isCorrect": False},
                        {"text": "Le protocole de communication sans fil du thermostat", "isCorrect": False}
                    ],
                    "correction": "L'hystérésis est le différentiel (ex: 0,5°C) qui évite que le brûleur ne fasse des cycles courts incessants autour de la température de consigne."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle formule permet de calculer la puissance électrique en monophasé (charge résistive) ?",
                    "answerOptions": [
                        {"text": "Tension fois Intensité", "isCorrect": True},
                        {"text": "Tension divisée par Intensité", "isCorrect": False},
                        {"text": "Résistance fois Tension", "isCorrect": False},
                        {"text": "Intensité divisée par Résistance", "isCorrect": False}
                    ],
                    "correction": "La puissance (P) est égale au produit de la tension (U) par l'intensité (I). P = U x I."
                },
                {
                    "questionNumber": 90,
                    "question": "Lors de la mise en service d'une chaudière gaz, quel document est obligatoire pour attester de la conformité de l'installation ?",
                    "answerOptions": [
                        {"text": "Le Certificat de Conformité", "isCorrect": True},
                        {"text": "La facture d'achat", "isCorrect": False},
                        {"text": "Le permis de construire", "isCorrect": False},
                        {"text": "Le plan cadastral", "isCorrect": False}
                    ],
                    "correction": "L'installateur doit fournir un Certificat de Conformité (type CC2 ou CC4) validé par un organisme agréé (ex: Qualigaz) pour obtenir l'ouverture du compteur."
                },
                {
                    "questionNumber": 91,
                    "question": "À quoi sert une vanne d'équilibrage sur une colonne de chauffage collectif ?",
                    "answerOptions": [
                        {"text": "À répartir les débits conformément aux besoins de chaque colonne", "isCorrect": True},
                        {"text": "À filtrer les impuretés présentes dans le réseau de chauffage", "isCorrect": False},
                        {"text": "À mesurer la consommation d'énergie de chaque appartement", "isCorrect": False},
                        {"text": "À augmenter la pression statique dans les étages supérieurs", "isCorrect": False}
                    ],
                    "correction": "L'équilibrage hydraulique garantit que chaque branche du réseau reçoit le débit calculé, évitant que les radiateurs proches de la pompe soient favorisés."
                },
                {
                    "questionNumber": 92,
                    "question": "Que signifie le symbole 'Terre' (rappelant un râteau inversé) sur un schéma électrique ?",
                    "answerOptions": [
                        {"text": "La mise à la terre", "isCorrect": True},
                        {"text": "L'antenne TV", "isCorrect": False},
                        {"text": "Le condensateur", "isCorrect": False},
                        {"text": "La résistance", "isCorrect": False}
                    ],
                    "correction": "Ce symbole indique que la carcasse métallique de l'appareil doit être reliée au conducteur de protection (terre) pour la sécurité."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel outil est indispensable pour vérifier l'absence de tension avant une intervention électrique ?",
                    "answerOptions": [
                        {"text": "Le VAT", "isCorrect": True},
                        {"text": "Le tournevis", "isCorrect": False},
                        {"text": "La pince", "isCorrect": False},
                        {"text": "Le cutter", "isCorrect": False}
                    ],
                    "correction": "Le VAT (Vérificateur d'Absence de Tension) est le seul appareil normé pour garantir la sécurité avant de toucher des conducteurs."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle est la cause probable si un circulateur de chauffage est 'gommé' après l'été ?",
                    "answerOptions": [
                        {"text": "Les dépôts calcaires bloquent la roue", "isCorrect": True},
                        {"text": "Le moteur électrique est grillé", "isCorrect": False},
                        {"text": "Le condensateur de démarrage est vide", "isCorrect": False},
                        {"text": "La vanne d'arrêt est fermée", "isCorrect": False}
                    ],
                    "correction": "L'arrêt prolongé favorise le dépôt de sédiments (boues, calcaire) qui bloquent le rotor. Un 'dégommage' manuel (rotation de l'axe avec un tournevis) est souvent nécessaire."
                },
                {
                    "questionNumber": 95,
                    "question": "En régulation, quel est le rôle d'une sonde extérieure ?",
                    "answerOptions": [
                        {"text": "Informer la chaudière des conditions climatiques", "isCorrect": True},
                        {"text": "Mesurer le taux de monoxyde de carbone dehors", "isCorrect": False},
                        {"text": "Détecter la présence de pluie pour fermer les volets", "isCorrect": False},
                        {"text": "Capter l'énergie solaire pour chauffer l'eau", "isCorrect": False}
                    ],
                    "correction": "La sonde extérieure permet à la régulation d'anticiper les déperditions thermiques du bâtiment avant même que la température intérieure ne chute."
                },
                {
                    "questionNumber": 96,
                    "question": "Que mesure-t-on avec un analyseur de combustion lors de l'entretien annuel ?",
                    "answerOptions": [
                        {"text": "Le taux de CO2 et le rendement", "isCorrect": True},
                        {"text": "Le débit d'eau dans les radiateurs", "isCorrect": False},
                        {"text": "La tension électrique du secteur", "isCorrect": False},
                        {"text": "La pression du vase d'expansion", "isCorrect": False}
                    ],
                    "correction": "L'analyseur mesure les fumées (O2, CO, CO2, température) pour calculer le rendement de la chaudière et vérifier l'absence de danger (monoxyde de carbone)."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle est la fonction d'un aquastat de sécurité (ou thermostat limiteur) sur une chaudière ?",
                    "answerOptions": [
                        {"text": "Couper le brûleur en cas de surchauffe anormale", "isCorrect": True},
                        {"text": "Enclencher le circulateur quand l'eau est chaude", "isCorrect": False},
                        {"text": "Réguler la température de l'eau chaude sanitaire", "isCorrect": False},
                        {"text": "Mesurer la pression de l'eau dans le corps de chauffe", "isCorrect": False}
                    ],
                    "correction": "C'est l'ultime sécurité. Si la régulation échoue et que la température dépasse un seuil critique (ex: 100°C), il coupe tout et nécessite un réarmement manuel."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est l'emplacement idéal pour un thermostat d'ambiance dans une maison ?",
                    "answerOptions": [
                        {"text": "Dans le séjour à 1m50 du sol", "isCorrect": True},
                        {"text": "Dans la cuisine au-dessus du four", "isCorrect": False},
                        {"text": "Dans le couloir d'entrée face à la porte", "isCorrect": False},
                        {"text": "Dans la salle de bains à côté de la douche", "isCorrect": False}
                    ],
                    "correction": "Il doit être placé dans la pièce de référence (séjour), loin des sources de chaleur parasites (soleil, cheminée, four) et des courants d'air, à hauteur d'homme (environ 1m50)."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle tension trouve-t-on aux bornes d'une prise de courant domestique classique en France ?",
                    "answerOptions": [
                        {"text": "230 Volts", "isCorrect": True},
                        {"text": "12 Volts", "isCorrect": False},
                        {"text": "400 Volts", "isCorrect": False},
                        {"text": "110 Volts", "isCorrect": False}
                    ],
                    "correction": "La tension monophasée standard délivrée par le réseau basse tension en France est de 230 V (fréquence 50 Hz)."
                },
                {
                    "questionNumber": 100,
                    "question": "Que faut-il faire lors de la maintenance annuelle d'un vase d'expansion ?",
                    "answerOptions": [
                        {"text": "Vérifier sa pression de gonflage", "isCorrect": True},
                        {"text": "Le remplir entièrement d'eau", "isCorrect": False},
                        {"text": "Le peindre pour éviter la rouille", "isCorrect": False},
                        {"text": "Le remplacer systématiquement", "isCorrect": False}
                    ],
                    "correction": "Il faut isoler le vase, le vidanger de son eau, et vérifier que la pression de gaz (azote) est conforme aux préconisations (souvent 0,5 à 1,5 bar)."
                }
            ]
        }
    }
}