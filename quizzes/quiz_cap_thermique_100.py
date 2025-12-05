# Fichier : quiz_cap_thermique_100.py

quiz_data = {
    "title": "Quiz CAP Monteur en Installations Thermiques : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : SÉCURITÉ, RÉGLEMENTATION ET OUTILLAGE (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Sécurité, Réglementation et Outillage (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel Équipement de Protection Individuelle (EPI) est obligatoire lors de travaux de brasure ou de soudure (chalumeau) ?",
                    "answerOptions": [
                        {"text": "Le gilet haute visibilité.", "isCorrect": False},
                        {"text": "Le masque anti-poussière FFP2.", "isCorrect": False},
                        {"text": "Les lunettes ou écran de protection teinté (pour les UV et les projections) et les gants de soudeur.", "isCorrect": True},
                        {"text": "Les bouchons d'oreille.", "isCorrect": False}
                    ],
                    "correction": "Les **lunettes teintées** protègent des rayonnements UV intenses et les **gants** protègent des brûlures par le métal en fusion."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le rôle du **DTU** (Document Technique Unifié) dans les installations thermiques ?",
                    "answerOptions": [
                        {"text": "Définir le prix des matériaux.", "isCorrect": False},
                        {"text": "Fixer les règles de l'art pour la conception et l'exécution des travaux (règles de pose, dimensions minimales, etc.).", "isCorrect": True},
                        {"text": "Gérer la comptabilité du chantier.", "isCorrect": False},
                        {"text": "Mesurer la pression de l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **DTU** est le document de référence pour garantir la qualité et la conformité des ouvrages (ex : DTU 65.1 pour les installations de chauffage)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est l'outil spécifique utilisé pour donner un angle (cintrer) à un tube de cuivre sans l'aplatir ni le déchirer ?",
                    "answerOptions": [
                        {"text": "La meuleuse.", "isCorrect": False},
                        {"text": "La Cintreuse (ou Cintreuse arbalète/à glissière).", "isCorrect": True},
                        {"text": "La filière.", "isCorrect": False},
                        {"text": "La coupe-tube.", "isCorrect": False}
                    ],
                    "correction": "La **Cintreuse** permet de respecter le rayon de courbure minimal du tube pour éviter qu'il ne s'écrase."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la cause principale du risque d'**intoxication au monoxyde de carbone (CO)** sur une installation thermique ?",
                    "answerOptions": [
                        {"text": "Un excès d'oxygène dans l'air.", "isCorrect": False},
                        {"text": "Une mauvaise combustion (manque d'air ou évacuation des fumées obstruée ou mal raccordée).", "isCorrect": True},
                        {"text": "Un radiateur percé.", "isCorrect": False},
                        {"text": "De l'eau trop chaude.", "isCorrect": False}
                    ],
                    "correction": "Le **CO** est un gaz inodore et mortel. Le respect de la ventilation et du conduit de fumée est vital."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est l'outil utilisé pour nettoyer la surface des tubes de cuivre avant une brasure, afin d'assurer une bonne adhérence du métal d'apport ?",
                    "answerOptions": [
                        {"text": "Un marteau.", "isCorrect": False},
                        {"text": "La toile émeri (abrasif fin), la paille de fer ou le décapant (flux).", "isCorrect": True},
                        {"text": "Une brosse métallique.", "isCorrect": False},
                        {"text": "Le papier journal.", "isCorrect": False}
                    ],
                    "correction": "La **propreté** de la zone à braser est essentielle pour la qualité de la liaison. Le décapant (flux) protège de l'oxydation durant le chauffage."
                },
                {
                    "questionNumber": 6,
                    "question": "Dans un circuit de chauffage central, quel est l'élément qui absorbe les variations de volume de l'eau dues à la montée en température ?",
                    "answerOptions": [
                        {"text": "Le radiateur.", "isCorrect": False},
                        {"text": "Le Vase d'expansion (ou Vex).", "isCorrect": True},
                        {"text": "Le circulateur.", "isCorrect": False},
                        {"text": "La soupape de sécurité.", "isCorrect": False}
                    ],
                    "correction": "Le **Vase d'expansion** empêche la pression de monter excessivement dans le circuit."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est le risque de laisser des **bavures** (résidus de coupe) à l'intérieur d'un tube après l'avoir coupé ?",
                    "answerOptions": [
                        {"text": "L'eau va geler.", "isCorrect": False},
                        {"text": "Les bavures peuvent se détacher et endommager la pompe (circulateur) ou obstruer les vannes/robinets thermiques.", "isCorrect": True},
                        {"text": "Le tube va rouiller.", "isCorrect": False},
                        {"text": "Le tube va se déformer.", "isCorrect": False}
                    ],
                    "correction": "L'**ébavurage** (intérieur et extérieur) est une étape obligatoire après la coupe d'un tube métallique (cuivre, acier) ou synthétique."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est l'outil utilisé pour créer un filetage (pas de vis) à l'extrémité d'un tube d'acier (ex : pour un raccordement) ?",
                    "answerOptions": [
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "La Filière (à main ou électrique).", "isCorrect": True},
                        {"text": "Le pince coupante.", "isCorrect": False},
                        {"text": "La presse à sertir.", "isCorrect": False}
                    ],
                    "correction": "La **Filière** est indispensable pour les raccordements vissés sur tube acier (avec de l'huile de coupe)."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle est la pression d'eau standard (en bars) que l'on doit généralement maintenir dans un circuit de chauffage domestique ?",
                    "answerOptions": [
                        {"text": "0,5 bar.", "isCorrect": False},
                        {"text": "Entre 1 et 1,5 bar à froid (ajustée en fonction de la hauteur du point le plus haut de l'installation).", "isCorrect": True},
                        {"text": "10 bars.", "isCorrect": False},
                        {"text": "Moins de 0,5 bar.", "isCorrect": False}
                    ],
                    "correction": "Une pression de **1 à 1,5 bar** est la norme pour garantir le bon fonctionnement du circulateur et la purge de l'air."
                },
                {
                    "questionNumber": 10,
                    "question": "Que représente le sigle **PER** dans le domaine de la plomberie et du chauffage ?",
                    "answerOptions": [
                        {"text": "Pression et Étanchéité du Raccordement.", "isCorrect": False},
                        {"text": "Polyéthylène Réticulé (tube synthétique utilisé pour les planchers chauffants et l'ECS).", "isCorrect": True},
                        {"text": "Pompe d'Économie d'Énergie et de Récupération.", "isCorrect": False},
                        {"text": "Passage des Évacuations Rapides.", "isCorrect": False}
                    ],
                    "correction": "Le **PER** est souple, léger et résistant à la corrosion, ce qui le rend très populaire dans les installations modernes."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le danger d'utiliser un chalumeau près de matériaux inflammables (bois, isolants, carton) ?",
                    "answerOptions": [
                        {"text": "Une mauvaise soudure.", "isCorrect": False},
                        {"text": "Un risque d'incendie (nécessité d'avoir un extincteur à portée de main, une protection thermique et de refroidir la zone).", "isCorrect": True},
                        {"text": "Un bruit excessif.", "isCorrect": False},
                        {"text": "Une fuite d'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **risque d'incendie** est majeur lors des travaux de soudure. Le permis de feu est souvent requis."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment appelle-t-on le raccord utilisé pour connecter un tube en cuivre à un tube en acier sans soudure, en utilisant un joint comprimé ?",
                    "answerOptions": [
                        {"text": "Raccord à visser.", "isCorrect": False},
                        {"text": "Raccord bicône (ou à olive) ou raccord à compression.", "isCorrect": True},
                        {"text": "Raccord instantané.", "isCorrect": False},
                        {"text": "Raccord collé.", "isCorrect": False}
                    ],
                    "correction": "Le **Raccord à compression** est souvent utilisé pour les petites réparations ou les raccords démontables."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est le rôle du **Manomètre** sur le tableau de bord d'une chaudière ?",
                    "answerOptions": [
                        {"text": "Mesurer la température de l'eau.", "isCorrect": False},
                        {"text": "Indiquer la pression de l'eau à l'intérieur du circuit de chauffage.", "isCorrect": True},
                        {"text": "Mesurer le débit du gaz.", "isCorrect": False},
                        {"text": "Indiquer le niveau de CO.", "isCorrect": False}
                    ],
                    "correction": "Le **Manomètre** permet de vérifier si la pression est dans la plage de fonctionnement normale (1 à 1,5 bar)."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est l'outil utilisé pour **alésager** (élargir légèrement) l'extrémité d'un tube PER avant le sertissage ?",
                    "answerOptions": [
                        {"text": "La pince à cintrer.", "isCorrect": False},
                        {"text": "Le Calibreur-Ébavureur.", "isCorrect": True},
                        {"text": "Le coupe-tube.", "isCorrect": False},
                        {"text": "La clé à molette.", "isCorrect": False}
                    ],
                    "correction": "Le **Calibreur** assure une forme parfaitement ronde du tube et supprime les bavures intérieures, garantissant un bon emboîtement du raccord et l'étanchéité."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle doit être la pente minimale pour l'évacuation des eaux usées (eaux vannes et eaux grises) ?",
                    "answerOptions": [
                        {"text": "1 cm par mètre (1%).", "isCorrect": True},
                        {"text": "5 cm par mètre (5%).", "isCorrect": False},
                        {"text": "Aucune pente.", "isCorrect": False},
                        {"text": "10 cm par mètre (10%).", "isCorrect": False}
                    ],
                    "correction": "Une pente de **1 à 3%** est nécessaire pour garantir l'écoulement correct et l'auto-nettoyage des canalisations."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le rôle du **Téflon (PTFE)** ou de la **Fibre de chanvre** dans un raccordement fileté ?",
                    "answerOptions": [
                        {"text": "Améliorer la pression.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité du raccord vissé (en comblant les espaces entre les filets).", "isCorrect": True},
                        {"text": "Colorer l'eau.", "isCorrect": False},
                        {"text": "Réduire le bruit.", "isCorrect": False}
                    ],
                    "correction": "Le **Téflon ou le Chanvre** sont des produits d'étanchéité standards, appliqués dans le sens du vissage."
                },
                {
                    "questionNumber": 17,
                    "question": "Qu'est-ce qu'une **Vanve 3 voies** ou **Vanne mélangeuse** dans un circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Une vanne pour trois tuyaux différents.", "isCorrect": False},
                        {"text": "Un dispositif qui mélange l'eau chaude de la chaudière avec l'eau de retour du circuit pour moduler la température envoyée aux radiateurs (régulation).", "isCorrect": True},
                        {"text": "Une vanne d'arrêt.", "isCorrect": False},
                        {"text": "Une vanne anti-retour.", "isCorrect": False}
                    ],
                    "correction": "La **Vanne mélangeuse** est essentielle pour l'équilibrage du réseau et pour éviter d'envoyer de l'eau trop chaude aux émetteurs."
                },
                {
                    "questionNumber": 18,
                    "question": "Pourquoi doit-on effectuer une **épreuve de pression** (ou épreuve hydraulique) sur une nouvelle installation de tuyauterie ?",
                    "answerOptions": [
                        {"text": "Pour réchauffer les tuyaux.", "isCorrect": False},
                        {"text": "Pour détecter les fuites ou les défauts d'étanchéité de l'installation avant la mise en service et la fermeture des cloisons.", "isCorrect": True},
                        {"text": "Pour nettoyer les tuyaux.", "isCorrect": False},
                        {"text": "Pour équilibrer la température.", "isCorrect": False}
                    ],
                    "correction": "L'**épreuve hydraulique** est une vérification obligatoire, souvent à une pression supérieure à la pression de service."
                },
                {
                    "questionNumber": 19,
                    "question": "Comment appelle-t-on le dispositif qui permet d'éviter que l'eau du réseau de chauffage ne retourne dans le réseau d'eau potable ?",
                    "answerOptions": [
                        {"text": "Le détendeur.", "isCorrect": False},
                        {"text": "Le Clapet anti-retour (ou Disconnecteur).", "isCorrect": True},
                        {"text": "Le filtre.", "isCorrect": False},
                        {"text": "Le purgeur.", "isCorrect": False}
                    ],
                    "correction": "Le **Disconnecteur** est une sécurité sanitaire essentielle pour éviter la contamination du réseau public par l'eau du circuit de chauffage (qui peut contenir des inhibiteurs de corrosion)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est l'outil utilisé pour couper les tubes multicouches, garantissant une coupe perpendiculaire et non déformée ?",
                    "answerOptions": [
                        {"text": "Une scie à métaux.", "isCorrect": False},
                        {"text": "Le Coupe-tube spécial (ou Ciseau pour multicouche) avec un calibreur-ébavureur intégré.", "isCorrect": True},
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "La lime.", "isCorrect": False}
                    ],
                    "correction": "Le **Coupe-tube spécial** assure une coupe nette et droite, vitale pour un sertissage de qualité."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TUYAUTERIE, RACCORDEMENTS ET ASSEMBLAGE (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Tuyauterie, Raccordements et Assemblage (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la principale différence entre la **Brasure tendre** et la **Brasure forte** pour le cuivre ?",
                    "answerOptions": [
                        {"text": "La brasure tendre est plus jolie.", "isCorrect": False},
                        {"text": "La brasure forte est réalisée au-dessus de 450 °C (plus résistante à la pression et à la chaleur), tandis que la brasure tendre est faite en dessous de 450 °C (plus simple).", "isCorrect": True},
                        {"text": "La brasure tendre est utilisée pour le gaz uniquement.", "isCorrect": False},
                        {"text": "La brasure forte est plus rapide à faire.", "isCorrect": False}
                    ],
                    "correction": "La **Brasure forte** est obligatoire pour les réseaux de gaz ou les circuits soumis à de très hautes températures et/ou pressions."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel est l'inconvénient principal du tube en **Acier galvanisé** pour le transport de l'eau potable ?",
                    "answerOptions": [
                        {"text": "Il est trop souple.", "isCorrect": False},
                        {"text": "Il est lourd et subit l'entartrage et la corrosion (rouille), ce qui peut le rendre impropre à l'eau potable à long terme (contrairement au cuivre ou PER).", "isCorrect": True},
                        {"text": "Il est très cher.", "isCorrect": False},
                        {"text": "Il est trop facile à couper.", "isCorrect": False}
                    ],
                    "correction": "L'**Acier** n'est plus privilégié pour l'eau potable domestique à cause des problèmes de corrosion interne."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le rôle du **Collier de dilatation** sur une longue colonne montante (cuivre ou acier) ?",
                    "answerOptions": [
                        {"text": "Améliorer l'isolation.", "isCorrect": False},
                        {"text": "Permettre au tuyau de se dilater ou de se contracter (avec la chaleur) sans générer de contraintes mécaniques sur les raccords et les murs.", "isCorrect": True},
                        {"text": "Réduire le bruit.", "isCorrect": False},
                        {"text": "Empêcher le vol.", "isCorrect": False}
                    ],
                    "correction": "La **Dilatation thermique** est un phénomène physique majeur. Il faut laisser les tubes 'glisser' dans leurs supports."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on la technique d'assemblage des tubes PER ou Multicouche qui utilise une pince pour déformer une bague métallique autour du raccord ?",
                    "answerOptions": [
                        {"text": "La soudure.", "isCorrect": False},
                        {"text": "Le Sertissage (par bague, ou par mâchoire).", "isCorrect": True},
                        {"text": "Le vissage.", "isCorrect": False},
                        {"text": "Le collage.", "isCorrect": False}
                    ],
                    "correction": "Le **Sertissage** est une méthode rapide et fiable pour les tubes synthétiques et multicouches."
                },
                {
                    "questionNumber": 25,
                    "question": "Dans une brasure de cuivre, que se passe-t-il si la chaleur est mal répartie sur le raccord ?",
                    "answerOptions": [
                        {"text": "Le cuivre devient rouge.", "isCorrect": False},
                        {"text": "Le métal d'apport ne coule pas uniformément (mauvaise capillarité) et crée un défaut d'étanchéité et de résistance.", "isCorrect": True},
                        {"text": "Le tube se rallonge.", "isCorrect": False},
                        {"text": "Le tube devient très froid.", "isCorrect": False}
                    ],
                    "correction": "La **chaleur uniforme** sur tout le périmètre du raccord est essentielle pour un bon joint (capillarité)."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le risque de croiser un tube d'eau chaude et un tube d'eau froide à l'intérieur d'une paroi ?",
                    "answerOptions": [
                        {"text": "Aucun risque.", "isCorrect": False},
                        {"text": "Échanger la température entre les deux tubes (l'eau froide est réchauffée, l'eau chaude est refroidie) et augmenter le risque de légionellose dans le circuit ECS.", "isCorrect": True},
                        {"text": "Le circuit sera obstrué.", "isCorrect": False},
                        {"text": "L'installation sera trop lourde.", "isCorrect": False}
                    ],
                    "correction": "Les tubes doivent être **isolés** (manchons) et les croisements sont à éviter pour minimiser les pertes énergétiques et les risques sanitaires."
                },
                {
                    "questionNumber": 27,
                    "question": "Comment appelle-t-on le raccord utilisé pour connecter un tube de faible diamètre à un tube de diamètre plus important ?",
                    "answerOptions": [
                        {"text": "Le coude.", "isCorrect": False},
                        {"text": "Le Réducteur (ou Manchon de réduction).", "isCorrect": True},
                        {"text": "Le bouchon.", "isCorrect": False},
                        {"text": "Le Té égal.", "isCorrect": False}
                    ],
                    "correction": "Le **Réducteur** permet de modifier le diamètre pour alimenter différents équipements."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est l'élément qui permet d'isoler l'installation (vidanger seulement une partie du circuit) en cas de réparation ou de maintenance ?",
                    "answerOptions": [
                        {"text": "Le circulateur.", "isCorrect": False},
                        {"text": "La Vanne d'arrêt (ou Robinet d'isolement).", "isCorrect": True},
                        {"text": "Le purgeur.", "isCorrect": False},
                        {"text": "Le radiateur.", "isCorrect": False}
                    ],
                    "correction": "La présence de **Vannes d'arrêt** est obligatoire à l'entrée et à la sortie des principaux appareils (chaudière, chauffe-eau, etc.)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est le rôle d'un **Manchon isolant** (ou coquille) en mousse sur la tuyauterie de chauffage ?",
                    "answerOptions": [
                        {"text": "Protéger contre le vol.", "isCorrect": False},
                        {"text": "Limiter les déperditions de chaleur (économies d'énergie) et prévenir le risque de brûlure par contact.", "isCorrect": True},
                        {"text": "Assurer l'étanchéité.", "isCorrect": False},
                        {"text": "Tenir le tuyau.", "isCorrect": False}
                    ],
                    "correction": "L'**Isolation des tuyaux** est essentielle pour le rendement énergétique (notamment en faux-plafond non chauffé)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le risque de réaliser des cintres avec un rayon de courbure trop faible sur un tube de cuivre ?",
                    "answerOptions": [
                        {"text": "Le tube devient trop long.", "isCorrect": False},
                        {"text": "Le tube s'aplatit ou se pince, réduisant la section de passage et entraînant une perte de charge (réduction du débit).", "isCorrect": True},
                        {"text": "Le tube se dilate.", "isCorrect": False},
                        {"text": "Le tube devient trop chaud.", "isCorrect": False}
                    ],
                    "correction": "La **Cintreuse** permet de respecter le rayon minimal pour maintenir le débit nominal."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment appelle-t-on le revêtement (vernis, peinture) utilisé pour protéger les tubes d'acier extérieurs contre la corrosion (rouille) ?",
                    "answerOptions": [
                        {"text": "Le décapant.", "isCorrect": False},
                        {"text": "Une peinture anti-corrosion (ou primaire d'accrochage antirouille).", "isCorrect": True},
                        {"text": "Un isolant.", "isCorrect": False},
                        {"text": "Un nettoyant.", "isCorrect": False}
                    ],
                    "correction": "La **Protection anti-corrosion** (galvanisation, peinture) est obligatoire pour les tubes acier visibles ou exposés à l'humidité."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'avantage du **Tube Multicouche** par rapport au PER ?",
                    "answerOptions": [
                        {"text": "Il est plus lourd.", "isCorrect": False},
                        {"text": "Il est plus stable (garde la forme donnée) et est étanche à l'oxygène (ce qui évite la corrosion dans les circuits de chauffage).", "isCorrect": True},
                        {"text": "Il est moins cher.", "isCorrect": False},
                        {"text": "Il est plus difficile à installer.", "isCorrect": False}
                    ],
                    "correction": "La couche d'aluminium du **Multicouche** assure la stabilité et la barrière anti-oxygène."
                },
                {
                    "questionNumber": 33,
                    "question": "Dans le cas d'une brasure de cuivre, quel est le rôle du **Décapant (Flux)** ?",
                    "answerOptions": [
                        {"text": "Fournir la chaleur.", "isCorrect": False},
                        {"text": "Nettoyer la surface juste avant et pendant le chauffage, en empêchant la formation d'oxydes qui empêcheraient le métal d'apport de couler.", "isCorrect": True},
                        {"text": "Servir de joint d'étanchéité.", "isCorrect": False},
                        {"text": "Refroidir le raccord.", "isCorrect": False}
                    ],
                    "correction": "Le **Décapant** (ou flux) est essentiel pour la réussite du joint par capillarité."
                },
                {
                    "questionNumber": 34,
                    "question": "Comment s'appelle la technique de pose où les tubes de chauffage (aller et retour) sont parallèles et parcourent la pièce avant de se raccorder (sans modification de la longueur des circuits) ?",
                    "answerOptions": [
                        {"text": "Montage en boucle.", "isCorrect": False},
                        {"text": "Montage en Tichelmann (ou Bouclage de Tichelmann).", "isCorrect": True},
                        {"text": "Montage en série.", "isCorrect": False},
                        {"text": "Montage en araignée.", "isCorrect": False}
                    ],
                    "correction": "Le **Tichelmann** est utilisé pour assurer un équilibrage hydraulique quasi automatique (même longueur, même perte de charge pour chaque radiateur)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le risque de ne pas respecter l'**inclinaison (pente)** des tubes de chauffage lors de la pose ?",
                    "answerOptions": [
                        {"text": "L'eau sera trop chaude.", "isCorrect": False},
                        {"text": "L'air ne pourra pas s'évacuer correctement du circuit (poches d'air), ce qui nuit au rendement du chauffage et crée des bruits.", "isCorrect": True},
                        {"text": "La pression sera trop forte.", "isCorrect": False},
                        {"text": "Le tube sera trop long.", "isCorrect": False}
                    ],
                    "correction": "La **pente** (montante vers les purgeurs, descendante vers la chaudière) est essentielle pour l'évacuation de l'air."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est l'élément qui permet de rendre les raccords à visser (filetés) démontables et étanches (autre que Téflon ou chanvre) ?",
                    "answerOptions": [
                        {"text": "Le mastic silicone.", "isCorrect": False},
                        {"text": "Le Joint plat (fibre ou caoutchouc) ou le Joint torique (O-ring).", "isCorrect": True},
                        {"text": "La colle.", "isCorrect": False},
                        {"text": "Le plâtre.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint plat ou torique** est parfait pour les raccords faciles à démonter (ex : siphon, raccords de chaudière)."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment appelle-t-on la technique qui consiste à faire un trou de dérivation dans un tube (cuivre) sans le couper (pour insérer un té par exemple) ?",
                    "answerOptions": [
                        {"text": "Le percement.", "isCorrect": False},
                        {"text": "Le Dépointage (ou piquage à la dépointereuse) suivi de la brasure.", "isCorrect": True},
                        {"text": "Le cintrage.", "isCorrect": False},
                        {"text": "Le sertissage.", "isCorrect": False}
                    ],
                    "correction": "Le **Dépointage** est une méthode rapide et utilisée sur les réseaux existants sous pression (après vidange bien sûr)."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est l'outil utilisé pour maintenir deux tubes ou un raccord dans une position stable et immobile pendant la soudure/brasure ?",
                    "answerOptions": [
                        {"text": "Le pied à coulisse.", "isCorrect": False},
                        {"text": "La Pince-étau (ou Pince de serrage).", "isCorrect": True},
                        {"text": "Le tournevis.", "isCorrect": False},
                        {"text": "Le niveau.", "isCorrect": False}
                    ],
                    "correction": "La **Pince-étau** est essentielle pour éviter tout mouvement du joint lors de la montée en température."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est le risque de fixer les tubes de PER ou Multicouche sans laisser de **jeu** suffisant dans les supports ?",
                    "answerOptions": [
                        {"text": "Ils vont geler.", "isCorrect": False},
                        {"text": "Les tubes synthétiques se dilatent fortement avec la chaleur, ce qui peut les déformer ou générer du bruit (claquements) dans la cloison (phénomène de 'coulée').", "isCorrect": True},
                        {"text": "Ils vont se corroder.", "isCorrect": False},
                        {"text": "Ils vont fuir.", "isCorrect": False}
                    ],
                    "correction": "La **Dilatation des tubes plastiques** est bien supérieure à celle du métal. Les colliers doivent permettre un léger glissement."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment appelle-t-on l'ensemble des tuyaux qui assurent l'alimentation des appareils sanitaires (robinets, douche, WC) ?",
                    "answerOptions": [
                        {"text": "Le Circuit de chauffage.", "isCorrect": False},
                        {"text": "Le Réseau d'Alimentation en Eau Potable (AEP).", "isCorrect": True},
                        {"text": "Le Circuit de ventilation.", "isCorrect": False},
                        {"text": "Le Réseau d'évacuation.", "isCorrect": False}
                    ],
                    "correction": "Le **Réseau AEP** est la partie du travail du Monteur Thermique et Sanitaire."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : SYSTÈMES DE CHAUFFAGE (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Systèmes de Chauffage (Généralités et Chaudières) (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le principe de fonctionnement d'une **Chaudière à condensation** (gaz ou fioul) ?",
                    "answerOptions": [
                        {"text": "Elle utilise uniquement l'électricité.", "isCorrect": False},
                        {"text": "Elle récupère la chaleur latente contenue dans la vapeur d'eau des fumées de combustion, améliorant fortement le rendement énergétique.", "isCorrect": True},
                        {"text": "Elle chauffe l'eau par induction magnétique.", "isCorrect": False},
                        {"text": "Elle utilise uniquement le bois.", "isCorrect": False}
                    ],
                    "correction": "La **Condensation** permet d'atteindre des rendements supérieurs à 100% (sur PCI), grâce à la récupération de chaleur."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le rôle du **Thermostat d'ambiance** dans une installation de chauffage ?",
                    "answerOptions": [
                        {"text": "Réguler la pression.", "isCorrect": False},
                        {"text": "Mesurer la température de la pièce et commander l'arrêt ou le démarrage de la chaudière (ou l'ouverture/fermeture d'une vanne de zone).", "isCorrect": True},
                        {"text": "Équilibrer le réseau.", "isCorrect": False},
                        {"text": "Purifier l'air.", "isCorrect": False}
                    ],
                    "correction": "Le **Thermostat** est l'organe de régulation de la température intérieure."
                },
                {
                    "questionNumber": 43,
                    "question": "Comment appelle-t-on le dispositif qui évacue automatiquement l'air accumulé en haut d'un radiateur ou de la chaudière ?",
                    "answerOptions": [
                        {"text": "Le détendeur.", "isCorrect": False},
                        {"text": "Le Purgeur automatique (ou dégazeurs).", "isCorrect": True},
                        {"text": "Le siphon.", "isCorrect": False},
                        {"text": "Le manomètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Purgeur automatique** est souvent installé aux points hauts pour éviter les bruits de circulation d'eau et les problèmes de chauffe."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est l'avantage principal d'un **Plancher Chauffant Hydraulique** par rapport aux radiateurs muraux ?",
                    "answerOptions": [
                        {"text": "Il est plus rapide à installer.", "isCorrect": False},
                        {"text": "Il offre un meilleur confort (chaleur uniforme par rayonnement) et permet de fonctionner à basse température (économie d'énergie).", "isCorrect": True},
                        {"text": "Il est moins cher.", "isCorrect": False},
                        {"text": "Il consomme plus d'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Plancher chauffant** est un émetteur basse température, idéal pour les chaudières à condensation ou les pompes à chaleur (PAC)."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le rôle du **Circulateur (ou Pompe de circulation)** dans une installation ?",
                    "answerOptions": [
                        {"text": "Chauffer l'eau.", "isCorrect": False},
                        {"text": "Assurer la circulation forcée de l'eau chaude entre la chaudière et les émetteurs (radiateurs, plancher).", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Réguler la pression.", "isCorrect": False}
                    ],
                    "correction": "Le **Circulateur** est le cœur du système hydraulique. "
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la fonction d'une **Soupape de sécurité** (ou Dispositif de sécurité thermique) ?",
                    "answerOptions": [
                        {"text": "Réguler le débit.", "isCorrect": False},
                        {"text": "Évacuer l'excès de pression (souvent à 3 bars) en cas de surchauffe ou de dysfonctionnement du vase d'expansion (pour éviter l'explosion).", "isCorrect": True},
                        {"text": "Réguler la température.", "isCorrect": False},
                        {"text": "Empêcher la corrosion.", "isCorrect": False}
                    ],
                    "correction": "La **Soupape de sécurité** est une sécurité vitale qui s'ouvre pour laisser l'eau s'échapper en cas de surpression."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on le dispositif situé sur le radiateur qui permet à l'utilisateur de moduler la température de la pièce en fonction de ses besoins ?",
                    "answerOptions": [
                        {"text": "La vanne d'arrêt.", "isCorrect": False},
                        {"text": "Le Robinet Thermostatique (ou Tête thermostatique).", "isCorrect": True},
                        {"text": "Le purgeur.", "isCorrect": False},
                        {"text": "Le té de réglage.", "isCorrect": False}
                    ],
                    "correction": "Le **Robinet thermostatique** adapte le débit d'eau chaude au besoin de chaleur de la pièce."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est le rôle de la **Sonde extérieure** (ou Sonde de température extérieure) pour une chaudière modulante ?",
                    "answerOptions": [
                        {"text": "Mesurer le vent.", "isCorrect": False},
                        {"text": "Ajuster la température de l'eau de chauffage en fonction des conditions climatiques (Loi d'eau), pour anticiper les besoins et économiser l'énergie.", "isCorrect": True},
                        {"text": "Mesurer l'humidité.", "isCorrect": False},
                        {"text": "Mesurer la pression.", "isCorrect": False}
                    ],
                    "correction": "La **Sonde extérieure** permet d'optimiser le fonctionnement de la chaudière (régulation 'Loi d'eau')."
                },
                {
                    "questionNumber": 49,
                    "question": "Dans une installation de chauffage en **Monotube**, quelle est la particularité du raccordement des radiateurs ?",
                    "answerOptions": [
                        {"text": "Chaque radiateur a son propre circuit.", "isCorrect": False},
                        {"text": "L'eau passe successivement d'un radiateur à l'autre (l'eau refroidit au fur et à mesure) : nécessite un robinet by-pass pour le dérivation.", "isCorrect": True},
                        {"text": "Un seul tuyau entre et sort de la chaudière.", "isCorrect": False},
                        {"text": "Il n'y a pas de vanne.", "isCorrect": False}
                    ],
                    "correction": "Le **Monotube** est plus simple à poser mais nécessite des radiateurs de taille croissante et un by-pass pour fonctionner correctement."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le rôle du **Filtre Magnétique (ou Désemboueur)** dans un circuit de chauffage central ?",
                    "answerOptions": [
                        {"text": "Réguler le débit.", "isCorrect": False},
                        {"text": "Capturer les boues métalliques (oxydes de fer) générées par la corrosion interne du circuit pour les empêcher d'endommager la chaudière et le circulateur.", "isCorrect": True},
                        {"text": "Produire de la chaleur.", "isCorrect": False},
                        {"text": "Aérer le circuit.", "isCorrect": False}
                    ],
                    "correction": "Le **Désemboueur** est essentiel pour la longévité des installations modernes (surtout avec les chaudières à condensation)."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le principal combustible d'une chaudière labellisée **Biomasse** ?",
                    "answerOptions": [
                        {"text": "Le gaz naturel.", "isCorrect": False},
                        {"text": "Le bois (granulés, bûches, plaquettes forestières).", "isCorrect": True},
                        {"text": "L'électricité.", "isCorrect": False},
                        {"text": "Le fioul.", "isCorrect": False}
                    ],
                    "correction": "La **Biomasse** est une source d'énergie renouvelable (bois) utilisée pour le chauffage."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le risque de ne pas effectuer le **désembouage** d'une vieille installation ?",
                    "answerOptions": [
                        {"text": "Les radiateurs deviennent trop chauds.", "isCorrect": False},
                        {"text": "Réduction du rendement, bruits, dysfonctionnement du circulateur et détérioration des échangeurs de la chaudière (encrassement).", "isCorrect": True},
                        {"text": "La pression baisse trop.", "isCorrect": False},
                        {"text": "Le vase d'expansion ne fonctionne plus.", "isCorrect": False}
                    ],
                    "correction": "Le **Désembouage** est une opération de maintenance lourde mais nécessaire (nettoyage chimique et rinçage sous pression)."
                },
                {
                    "questionNumber": 53,
                    "question": "Comment appelle-t-on la **partie haute** d'un radiateur (où se trouve généralement le purgeur) ?",
                    "answerOptions": [
                        {"text": "Le pied.", "isCorrect": False},
                        {"text": "La Tête.", "isCorrect": True},
                        {"text": "Le corps.", "isCorrect": False},
                        {"text": "La base.", "isCorrect": False}
                    ],
                    "correction": "La **Tête de radiateur** est l'endroit où l'air s'accumule."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le rôle du **By-pass** sur une chaudière à condensation (selon les fabricants) ?",
                    "answerOptions": [
                        {"text": "Isoler la chaudière.", "isCorrect": False},
                        {"text": "Permettre à une partie de l'eau de retour de ne pas passer dans le corps de chauffe lorsque le retour est trop froid (pour maintenir une température minimale dans la chaudière).", "isCorrect": True},
                        {"text": "Réguler le gaz.", "isCorrect": False},
                        {"text": "Purifier l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **By-pass** peut être mécanique ou intégré à la régulation, il gère la température de l'eau de retour."
                },
                {
                    "questionNumber": 55,
                    "question": "Qu'est-ce qu'un **Radiateur à chaleur douce** ou **Radiateur à inertie** ?",
                    "answerOptions": [
                        {"text": "Un radiateur qui ne chauffe pas.", "isCorrect": False},
                        {"text": "Un radiateur qui emmagasine la chaleur (fluide caloporteur ou corps solide) et la restitue lentement, même après l'arrêt de la chauffe.", "isCorrect": True},
                        {"text": "Un radiateur en aluminium.", "isCorrect": False},
                        {"text": "Un radiateur électrique standard.", "isCorrect": False}
                    ],
                    "correction": "Le radiateur à **Inertie** (fonte, pierre, céramique) est plus confortable et plus économique que le convecteur simple."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le rôle du **Pressostat** dans un circuit hydraulique ?",
                    "answerOptions": [
                        {"text": "Contrôler la température.", "isCorrect": False},
                        {"text": "Mesurer et contrôler la pression du fluide et arrêter le circuit si celle-ci est trop basse ou trop haute (sécurité).", "isCorrect": True},
                        {"text": "Mesurer le débit.", "isCorrect": False},
                        {"text": "Nettoyer l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Pressostat** est un interrupteur de sécurité essentiel dans les chaudières."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est l'élément de la chaudière qui permet le transfert de la chaleur du brûleur vers l'eau du circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Le thermostat.", "isCorrect": False},
                        {"text": "L'Échangeur (ou Corps de chauffe).", "isCorrect": True},
                        {"text": "Le vase d'expansion.", "isCorrect": False},
                        {"text": "Le purgeur.", "isCorrect": False}
                    ],
                    "correction": "L'**Échangeur** est la pièce centrale de la chaudière."
                },
                {
                    "questionNumber": 58,
                    "question": "Dans un **Plancher Chauffant**, quelle est la couche obligatoire située sous les tubes de PER/Multicouche pour limiter la déperdition de chaleur vers le bas ?",
                    "answerOptions": [
                        {"text": "Le béton.", "isCorrect": False},
                        {"text": "Le Panneau isolant (polyuréthane, PSE) et la bande de désolidarisation périphérique.", "isCorrect": True},
                        {"text": "La membrane étanche.", "isCorrect": False},
                        {"text": "Le carrelage.", "isCorrect": False}
                    ],
                    "correction": "L'**Isolation sous dalle** est fondamentale pour le rendement du plancher chauffant."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est le rôle du **Té de réglage (ou Robinet d'équilibrage)** sur un radiateur ?",
                    "answerOptions": [
                        {"text": "Régler la température de la pièce.", "isCorrect": False},
                        {"text": "Ajuster manuellement le débit d'eau qui traverse le radiateur pour garantir une répartition de chaleur uniforme sur l'ensemble du réseau (équilibrage hydraulique).", "isCorrect": True},
                        {"text": "Vidanger le radiateur.", "isCorrect": False},
                        {"text": "Purger l'air.", "isCorrect": False}
                    ],
                    "correction": "L'**Équilibrage** est l'étape de mise en service qui assure le confort et les économies d'énergie."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment appelle-t-on le type de raccordement où l'eau chaude et l'eau froide sont centralisées dans un seul boîtier (collecteur), chaque émetteur ayant son propre départ et retour ?",
                    "answerOptions": [
                        {"text": "Montage en série.", "isCorrect": False},
                        {"text": "Montage en Pieuvre (ou Nourrice).", "isCorrect": True},
                        {"text": "Montage en boucle.", "isCorrect": False},
                        {"text": "Montage en dérivation.", "isCorrect": False}
                    ],
                    "correction": "Le **Montage en Pieuvre** (ou distribution par collecteurs) est courant avec le PER/Multicouche car il évite les raccords noyés dans la dalle ou la cloison."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : EAU CHAUDE SANITAIRE, VENTILATION ET CIRCUITS (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Eau Chaude Sanitaire (ECS), Ventilation et Circuits (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le rôle du **Groupe de Sécurité** sur un chauffe-eau à accumulation (ballon ECS) ?",
                    "answerOptions": [
                        {"text": "Réguler le débit d'eau froide.", "isCorrect": False},
                        {"text": "Maintenir la pression interne à 3 bars maximum (soupape) et vidanger l'excès de volume généré par la chauffe de l'eau (dilatation).", "isCorrect": True},
                        {"text": "Chauffer l'eau.", "isCorrect": False},
                        {"text": "Filtrer l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Groupe de Sécurité** est l'organe de sécurité indispensable de tout ballon d'eau chaude."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la principale exigence sanitaire concernant le circuit d'Eau Chaude Sanitaire (ECS) pour éviter la prolifération des légionelles ?",
                    "answerOptions": [
                        {"text": "L'eau doit être très froide.", "isCorrect": False},
                        {"text": "Maintenir l'eau à une température suffisante (> 55 °C) ou effectuer régulièrement une 'douche de désinfection' (> 60 °C).", "isCorrect": True},
                        {"text": "Le circuit doit être très long.", "isCorrect": False},
                        {"text": "Le circuit doit être isolé.", "isCorrect": False}
                    ],
                    "correction": "La **Légionelle** se développe entre 25 et 45 °C. La température de stockage est cruciale."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est le rôle du **Siphon** sous un lavabo ou un évier ?",
                    "answerOptions": [
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Empêcher les odeurs nauséabondes (gaz d'égout) de remonter dans l'habitation grâce à la garde d'eau (niveau d'eau stagnant dans le coude).", "isCorrect": True},
                        {"text": "Mesurer le débit.", "isCorrect": False},
                        {"text": "Réduire la pression.", "isCorrect": False}
                    ],
                    "correction": "Le **Siphon** est l'organe essentiel de toute installation d'évacuation sanitaire."
                },
                {
                    "questionNumber": 64,
                    "question": "Comment appelle-t-on le dispositif qui limite la pression de l'eau froide à l'entrée d'une habitation (souvent à 3 bars) ?",
                    "answerOptions": [
                        {"text": "Le clapet anti-retour.", "isCorrect": False},
                        {"text": "Le Détendeur-réducteur de pression.", "isCorrect": True},
                        {"text": "Le vase d'expansion.", "isCorrect": False},
                        {"text": "Le circulateur.", "isCorrect": False}
                    ],
                    "correction": "Le **Détendeur** protège les appareils sanitaires (lave-linge, chaudière) contre la surpression du réseau public."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la fonction d'une **Ventilation Mécanique Contrôlée (VMC) Simple Flux** ?",
                    "answerOptions": [
                        {"text": "Réchauffer l'air neuf.", "isCorrect": False},
                        {"text": "Extraire l'air vicié et humide (cuisine, SDB, WC) et créer une dépression, l'air neuf entrant par des bouches (entrées d'air) dans les pièces de vie.", "isCorrect": True},
                        {"text": "Chauffer la maison.", "isCorrect": False},
                        {"text": "Distribuer l'eau chaude.", "isCorrect": False}
                    ],
                    "correction": "La **VMC Simple Flux** est le système de ventilation de base pour la salubrité de l'air."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le risque de ne pas installer un **Clapet anti-retour** sur le refoulement d'une pompe de relevage (eaux usées) ?",
                    "answerOptions": [
                        {"text": "La pompe va chauffer.", "isCorrect": False},
                        {"text": "L'eau relevée peut redescendre dans la cuve lorsque la pompe s'arrête (risque de débordement).", "isCorrect": True},
                        {"text": "Le moteur va griller.", "isCorrect": False},
                        {"text": "Le siphon va geler.", "isCorrect": False}
                    ],
                    "correction": "Le **Clapet anti-retour** (ou anti-siphon) empêche le reflux du fluide."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le rôle d'un **Aérateur à membrane (ou clapet d'aération)** sur une colonne de chute (évacuation) ?",
                    "answerOptions": [
                        {"text": "Empêcher le bruit.", "isCorrect": False},
                        {"text": "Éviter le désiphonnage (vidage du siphon) des appareils sanitaires en cas de forte aspiration dans la colonne, en faisant entrer l'air.", "isCorrect": True},
                        {"text": "Évacuer l'eau.", "isCorrect": False},
                        {"text": "Réguler le débit.", "isCorrect": False}
                    ],
                    "correction": "L'**Aérateur à membrane** remplace la ventilation secondaire (sortie en toiture) dans certains cas."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment appelle-t-on le dispositif qui permet de faire circuler l'ECS dans un circuit fermé (boucle) pour avoir de l'eau chaude immédiatement au robinet ?",
                    "answerOptions": [
                        {"text": "Le té de dérivation.", "isCorrect": False},
                        {"text": "Le Bouclage d'Eau Chaude Sanitaire (avec son propre circulateur).", "isCorrect": True},
                        {"text": "Le circuit monotube.", "isCorrect": False},
                        {"text": "Le réseau AEP.", "isCorrect": False}
                    ],
                    "correction": "Le **Bouclage ECS** est un gage de confort, mais augmente les pertes thermiques (nécessite une isolation parfaite)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le rôle d'un **Échangeur à plaques** dans une installation de production d'ECS instantanée ?",
                    "answerOptions": [
                        {"text": "Stocker l'eau chaude.", "isCorrect": False},
                        {"text": "Transférer rapidement la chaleur de l'eau de chauffage primaire vers l'eau froide sanitaire, sans mélange des fluides (production instantanée).", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Vidanger le circuit.", "isCorrect": False}
                    ],
                    "correction": "L'**Échangeur à plaques** est compact et très performant pour la production d'ECS à la demande."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment s'appelle la technique de raccordement des évacuations qui utilise un joint en caoutchouc pour l'étanchéité, sans colle ni soudure ?",
                    "answerOptions": [
                        {"text": "Le sertissage.", "isCorrect": False},
                        {"text": "Le Raccordement par joint à lèvres (ou Manchon coulissant à joint).", "isCorrect": True},
                        {"text": "La brasure.", "isCorrect": False},
                        {"text": "Le vissage.", "isCorrect": False}
                    ],
                    "correction": "Le **Joint à lèvres** est très courant sur les réseaux PVC (évacuations) pour sa simplicité de montage/démontage."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est l'objectif du traitement anti-corrosion (anode) dans un ballon d'ECS ?",
                    "answerOptions": [
                        {"text": "Réguler la température.", "isCorrect": False},
                        {"text": "Protéger la cuve métallique du chauffe-eau contre la rouille (corrosion) en sacrifiant l'anode (magnésium ou titane).", "isCorrect": True},
                        {"text": "Isoler la cuve.", "isCorrect": False},
                        {"text": "Filtrer le calcaire.", "isCorrect": False}
                    ],
                    "correction": "L'**Anode** (protection cathodique) est essentielle pour la durée de vie du chauffe-eau."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie le marquage **NF** sur un robinet (mitigeur) ?",
                    "answerOptions": [
                        {"text": "Norme de Fuite.", "isCorrect": False},
                        {"text": "Norme Française (gage de qualité, de durabilité et de conformité aux réglementations sanitaires).", "isCorrect": True},
                        {"text": "Nouveau Filtre.", "isCorrect": False},
                        {"text": "Niveau Final.", "isCorrect": False}
                    ],
                    "correction": "La marque **NF** est un indicateur de fiabilité et de performance."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le risque de ne pas isoler le conduit d'évacuation des fumées d'une chaudière à condensation ?",
                    "answerOptions": [
                        {"text": "Le conduit va rouiller.", "isCorrect": False},
                        {"text": "Une mauvaise évacuation et un refroidissement prématuré des fumées, ce qui entraîne une condensation anormale (risques d'écoulement et de corrosion).", "isCorrect": True},
                        {"text": "La chaudière va s'éteindre.", "isCorrect": False},
                        {"text": "Le bruit sera trop fort.", "isCorrect": False}
                    ],
                    "correction": "Le **Conduit de fumée** (généralement en inox ou plastique PPh) doit maintenir une température suffisante pour une évacuation efficace."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le rôle de la **Soupape de décharge thermique** (ou Thermostat de sécurité) sur un chauffe-eau solaire ?",
                    "answerOptions": [
                        {"text": "Réguler la pression d'eau froide.", "isCorrect": False},
                        {"text": "Évacuer l'excès de chaleur lorsque le ballon atteint une température critique (ex : 90 °C) pour protéger le matériel et éviter l'ébullition.", "isCorrect": True},
                        {"text": "Purger l'air.", "isCorrect": False},
                        {"text": "Réguler le débit.", "isCorrect": False}
                    ],
                    "correction": "La **Soupape thermique** est un dispositif de sécurité important dans les systèmes solaires où la chaleur n'est pas toujours contrôlée."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le rôle du **Limiteur de température** sur le circuit d'Eau Chaude Sanitaire ?",
                    "answerOptions": [
                        {"text": "Augmenter le débit.", "isCorrect": False},
                        {"text": "Maintenir la température de l'eau distribuée aux robinets à un maximum de sécurité (souvent 50 °C) pour éviter les risques de brûlure (mitigeur thermostatique de sécurité).", "isCorrect": True},
                        {"text": "Filtrer l'eau.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité.", "isCorrect": False}
                    ],
                    "correction": "Le **Limiteur de température** (ou mitigeur thermostatique de sécurité) est une obligation dans les ERP et fortement recommandé en résidentiel."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment appelle-t-on le phénomène qui se produit lorsque le siphon d'un appareil sanitaire se vide à cause d'une aspiration dans le réseau d'évacuation (odeurs remontent) ?",
                    "answerOptions": [
                        {"text": "Le Bouclage.", "isCorrect": False},
                        {"text": "Le Désiphonnage.", "isCorrect": True},
                        {"text": "Le Surchauffage.", "isCorrect": False},
                        {"text": "L'Entartrage.", "isCorrect": False}
                    ],
                    "correction": "Le **Désiphonnage** est évité par une ventilation primaire et secondaire adéquate."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le risque de ne pas isoler le tube d'évacuation des condensats d'une chaudière à condensation en zone non chauffée ?",
                    "answerOptions": [
                        {"text": "Le tube va fuir.", "isCorrect": False},
                        {"text": "Les condensats (liquide acide) peuvent geler et obstruer l'évacuation, entraînant un dysfonctionnement et l'arrêt de la chaudière.", "isCorrect": True},
                        {"text": "Le tube va surchauffer.", "isCorrect": False},
                        {"text": "Le tube va se dilater.", "isCorrect": False}
                    ],
                    "correction": "L'**Isolation** protège contre le gel et les chocs thermiques."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est la particularité d'une **VMC Double Flux** par rapport à une VMC Simple Flux ?",
                    "answerOptions": [
                        {"text": "Elle ne fait qu'extraire l'air.", "isCorrect": False},
                        {"text": "Elle récupère la chaleur de l'air vicié extrait pour préchauffer l'air neuf entrant, améliorant l'efficacité énergétique.", "isCorrect": True},
                        {"text": "Elle ne fonctionne que l'été.", "isCorrect": False},
                        {"text": "Elle n'a pas besoin de moteur.", "isCorrect": False}
                    ],
                    "correction": "La **VMC Double Flux** est indispensable pour les bâtiments basse consommation (BB C) ou passifs."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment appelle-t-on le dispositif qui permet de faire le lien entre le réseau d'évacuation des eaux usées de l'habitation et le réseau public (égout) ?",
                    "answerOptions": [
                        {"text": "La fosse septique.", "isCorrect": False},
                        {"text": "Le Regard de raccordement (ou Boîte de branchement).", "isCorrect": True},
                        {"text": "Le siphon.", "isCorrect": False},
                        {"text": "Le compteur d'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Regard de raccordement** permet la jonction et l'accès pour l'entretien et le contrôle."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est l'inconvénient principal d'un **Chauffe-eau instantané (sans ballon)** ?",
                    "answerOptions": [
                        {"text": "Il consomme trop d'électricité.", "isCorrect": False},
                        {"text": "Il peut être limité en débit et avoir un temps de latence (inertie) avant d'obtenir de l'eau chaude à la température souhaitée.", "isCorrect": True},
                        {"text": "Il est trop grand.", "isCorrect": False},
                        {"text": "Il est trop cher.", "isCorrect": False}
                    ],
                    "correction": "Le **Chauffe-eau instantané** est compact, mais sa puissance limite le nombre de puisages simultanés."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : MISE EN SERVICE ET MAINTENANCE (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Mise en Service et Maintenance (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'objectif principal de l'**Équilibrage Hydraulique** du réseau de chauffage ?",
                    "answerOptions": [
                        {"text": "Réduire la pression.", "isCorrect": False},
                        {"text": "Assurer que tous les émetteurs (radiateurs ou boucles de PC) reçoivent le débit d'eau chaude nécessaire pour atteindre la température souhaitée (pas de radiateur froid ou trop chaud).", "isCorrect": True},
                        {"text": "Nettoyer l'eau.", "isCorrect": False},
                        {"text": "Purger l'air.", "isCorrect": False}
                    ],
                    "correction": "L'**Équilibrage** est l'étape qui finalise la performance de l'installation."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est l'outil utilisé pour mesurer la différence de température entre l'aller et le retour d'un radiateur ?",
                    "answerOptions": [
                        {"text": "Le manomètre.", "isCorrect": False},
                        {"text": "Le Thermomètre (ou Pince thermométrique) (pour calculer le $\Delta T$ et vérifier l'équilibrage).", "isCorrect": True},
                        {"text": "L'hygromètre.", "isCorrect": False},
                        {"text": "L'anémomètre.", "isCorrect": False}
                    ],
                    "correction": "La **mesure du $\Delta T$** (Delta T) est essentielle pour l'équilibrage hydraulique."
                },
                {
                    "questionNumber": 83,
                    "question": "Comment procède-t-on pour **purger l'air** d'un radiateur après avoir rempli l'installation ?",
                    "answerOptions": [
                        {"text": "Ouvrir la vanne d'arrêt.", "isCorrect": False},
                        {"text": "Ouvrir légèrement la vis de purge (avec une clé de purge), laisser l'air s'échapper jusqu'à ce que l'eau coule sans bulle, puis refermer.", "isCorrect": True},
                        {"text": "Frapper le radiateur.", "isCorrect": False},
                        {"text": "Augmenter la pression à 5 bars.", "isCorrect": False}
                    ],
                    "correction": "La **Purge** est essentielle pour le bon fonctionnement et le silence des radiateurs."
                },
                {
                    "questionNumber": 84,
                    "question": "Que doit-on vérifier en priorité lors de la maintenance annuelle d'une chaudière gaz ?",
                    "answerOptions": [
                        {"text": "La peinture extérieure.", "isCorrect": False},
                        {"text": "L'état de l'échangeur, la combustion (analyseur de fumées), l'étanchéité du circuit, le vase d'expansion et les sécurités (obligations légales).", "isCorrect": True},
                        {"text": "Le bruit de la pompe.", "isCorrect": False},
                        {"text": "La couleur du ballon.", "isCorrect": False}
                    ],
                    "correction": "L'**entretien annuel** (contrôle et nettoyage) est une obligation légale et essentielle pour la sécurité (CO) et le rendement."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le risque de ne pas traiter l'eau d'une nouvelle installation (inhibiteur de corrosion) ?",
                    "answerOptions": [
                        {"text": "L'eau va geler.", "isCorrect": False},
                        {"text": "Augmentation de la corrosion interne, formation de boues et de tartre, ce qui réduit la durée de vie de la chaudière et des émetteurs.", "isCorrect": True},
                        {"text": "La pression va baisser.", "isCorrect": False},
                        {"text": "La vanne sera trop chaude.", "isCorrect": False}
                    ],
                    "correction": "L'ajout d'un **inhibiteur de corrosion** est fortement recommandé, notamment avec les pompes à chaleur ou les chaudières modernes."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le symptôme typique d'un **Vase d'expansion (Vex) défectueux (membrane percée)** dans un circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Le circulateur s'arrête.", "isCorrect": False},
                        {"text": "La pression monte très rapidement à chaud (souvent au-delà de 3 bars) et redescend brutalement à froid (nécessité de purger la valve du Vex pour vérifier l'eau).", "isCorrect": True},
                        {"text": "Le radiateur est froid.", "isCorrect": False},
                        {"text": "La chaudière fait du bruit.", "isCorrect": False}
                    ],
                    "correction": "Un **Vex HS** ne peut plus absorber la dilatation, ce qui déclenche la soupape de sécurité."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est l'outil utilisé pour évaluer le rendement et la sécurité d'une chaudière en mesurant la composition des gaz de combustion ?",
                    "answerOptions": [
                        {"text": "Le manomètre.", "isCorrect": False},
                        {"text": "L'Analyseur de combustion (ou Analyseur de fumées).", "isCorrect": True},
                        {"text": "Le thermomètre.", "isCorrect": False},
                        {"text": "Le débitmètre.", "isCorrect": False}
                    ],
                    "correction": "L'**Analyseur de fumées** est obligatoire lors de l'entretien annuel (vérification du taux de CO et du rendement)."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment appelle-t-on l'opération qui consiste à éliminer le calcaire (tartre) accumulé dans un échangeur de chaudière ou un chauffe-eau ?",
                    "answerOptions": [
                        {"text": "Le désembouage.", "isCorrect": False},
                        {"text": "Le Détartrage (généralement par injection d'un produit acide dilué).", "isCorrect": True},
                        {"text": "La purge.", "isCorrect": False},
                        {"text": "Le rinçage.", "isCorrect": False}
                    ],
                    "correction": "Le **Détartrage** est nécessaire dans les régions où l'eau est très dure (calcaire)."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le risque de raccorder une **pompe à chaleur (PAC)** sur un réseau de radiateurs en acier très anciens ?",
                    "answerOptions": [
                        {"text": "La PAC va surchauffer.", "isCorrect": False},
                        {"text": "Les radiateurs anciens sont conçus pour fonctionner à haute température et la PAC (basse température) n'aura pas un rendement suffisant pour chauffer le logement (sous-dimensionnement).", "isCorrect": True},
                        {"text": "La PAC va geler.", "isCorrect": False},
                        {"text": "Le gaz va fuir.", "isCorrect": False}
                    ],
                    "correction": "La **PAC** est performante avec un plancher chauffant ou des radiateurs basse température (grandes surfaces d'échange)."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est l'outil de base pour vérifier la présence de gaz (propane, butane, méthane) lors d'un raccordement de chaudière gaz ?",
                    "answerOptions": [
                        {"text": "Le manomètre.", "isCorrect": False},
                        {"text": "Le Détecteur de fuite de gaz (ou Solution moussante de détection).", "isCorrect": True},
                        {"text": "Le tournevis.", "isCorrect": False},
                        {"text": "Le thermomètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Détecteur de fuite de gaz** est essentiel pour la sécurité de l'installation."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle est la cause principale d'une **surchauffe** anormale d'une chaudière ?",
                    "answerOptions": [
                        {"text": "Le vase d'expansion est trop grand.", "isCorrect": False},
                        {"text": "Manque d'eau dans le circuit ou défaillance du circulateur (mauvaise évacuation de la chaleur produite) ou du thermostat de sécurité.", "isCorrect": True},
                        {"text": "Le purgeur est ouvert.", "isCorrect": False},
                        {"text": "Le filtre est trop propre.", "isCorrect": False}
                    ],
                    "correction": "Le **Manque de circulation d'eau** est la cause la plus fréquente d'une surchauffe."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le rôle du **Débitmètre (ou Indicateur de débit)** dans un collecteur de plancher chauffant ?",
                    "answerOptions": [
                        {"text": "Mesurer la pression.", "isCorrect": False},
                        {"text": "Indiquer le volume d'eau (débit) qui circule dans chaque boucle de plancher chauffant (essentiel pour l'équilibrage).", "isCorrect": True},
                        {"text": "Purger l'air.", "isCorrect": False},
                        {"text": "Chauffer l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Débitmètre** permet l'équilibrage précis des différentes zones du plancher."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment appelle-t-on le dispositif qui permet de réaliser le remplissage en eau du circuit de chauffage à partir du réseau d'eau potable ?",
                    "answerOptions": [
                        {"text": "La vanne d'arrêt.", "isCorrect": False},
                        {"text": "Le Robinet de remplissage (ou Disconnecteur amovible).", "isCorrect": True},
                        {"text": "Le purgeur.", "isCorrect": False},
                        {"text": "Le circulateur.", "isCorrect": False}
                    ],
                    "correction": "Le **Robinet de remplissage** permet de maintenir la pression entre 1 et 1,5 bar."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle du **Clapet de sécurité (ou clapets anti-retour)** dans le circuit gaz d'un chalumeau bi-gaz (oxygène/acétylène) ?",
                    "answerOptions": [
                        {"text": "Empêcher le vol de gaz.", "isCorrect": False},
                        {"text": "Éviter le retour de flamme ou le mélange des gaz dans les détendeurs et les tuyaux, ce qui pourrait provoquer une explosion.", "isCorrect": True},
                        {"text": "Réguler la pression.", "isCorrect": False},
                        {"text": "Chauffer les gaz.", "isCorrect": False}
                    ],
                    "correction": "Les **clapets anti-retour** sont une sécurité absolue sur les chalumeaux bi-gaz."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est l'outil utilisé pour vérifier qu'un radiateur ou une tuyauterie est de niveau (horizontal et vertical) ?",
                    "answerOptions": [
                        {"text": "Le mètre ruban.", "isCorrect": False},
                        {"text": "Le Niveau à bulle (ou Niveau laser).", "isCorrect": True},
                        {"text": "Le thermomètre.", "isCorrect": False},
                        {"text": "Le manomètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Niveau** est l'outil de base du monteur pour l'esthétique et l'écoulement des fluides."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment s'appelle le procédé qui consiste à chauffer une pièce métallique (ex : pour une soudure) puis à la laisser refroidir lentement pour éviter la fragilisation ?",
                    "answerOptions": [
                        {"text": "Le trempage.", "isCorrect": False},
                        {"text": "Le Recuit (ou Adoucissement).", "isCorrect": True},
                        {"text": "Le forgeage.", "isCorrect": False},
                        {"text": "La cémentation.", "isCorrect": False}
                    ],
                    "correction": "Le **Recuit** est une opération thermique qui restaure la ductilité du métal."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque de laisser des **vannes de radiateur** complètement ouvertes lors du remplissage du circuit de chauffage ?",
                    "answerOptions": [
                        {"text": "Le radiateur va fuir.", "isCorrect": False},
                        {"text": "L'air peut s'accumuler dans certains radiateurs ou points hauts (bouchons d'air), rendant la purge difficile ou incomplète.", "isCorrect": True},
                        {"text": "La chaudière va démarrer.", "isCorrect": False},
                        {"text": "Le vase d'expansion sera trop plein.", "isCorrect": False}
                    ],
                    "correction": "Il est préférable de remplir l'installation avec les vannes fermées, puis d'ouvrir et de purger un par un, en partant du bas."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle est l'exigence concernant le raccordement électrique des ventilateurs de VMC et de la chaudière (protection) ?",
                    "answerOptions": [
                        {"text": "Ils doivent être raccordés sur le même circuit.", "isCorrect": False},
                        {"text": "Ils doivent être raccordés sur un circuit électrique dédié et protégé (disjoncteur approprié) conformément à la norme NF C 15-100.", "isCorrect": True},
                        {"text": "Ils doivent être raccordés sur une prise standard.", "isCorrect": False},
                        {"text": "Ils doivent être alimentés par pile.", "isCorrect": False}
                    ],
                    "correction": "Le **Circuit dédié** est obligatoire pour éviter les surcharges et garantir la sécurité."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment appelle-t-on le dispositif qui permet au professionnel de lire et d'enregistrer les défauts ou les historiques de fonctionnement d'une chaudière moderne ?",
                    "answerOptions": [
                        {"text": "Le purgeur.", "isCorrect": False},
                        {"text": "L'outil de diagnostic (ou Valise de maintenance) du fabricant.", "isCorrect": True},
                        {"text": "Le manomètre.", "isCorrect": False},
                        {"text": "Le chalumeau.", "isCorrect": False}
                    ],
                    "correction": "L'**Outil de diagnostic** est essentiel pour la recherche de pannes sur les chaudières électroniques."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le principal défaut d'une installation d'eau chaude sanitaire (ECS) non isolée (tuyaux non calorifugés) ?",
                    "answerOptions": [
                        {"text": "La pression baisse.", "isCorrect": False},
                        {"text": "Le temps d'attente de l'eau chaude est très long (gaspillage d'eau) et la déperdition thermique (perte d'énergie) est élevée.", "isCorrect": True},
                        {"text": "Le risque de corrosion augmente.", "isCorrect": False},
                        {"text": "La chaudière fait du bruit.", "isCorrect": False}
                    ],
                    "correction": "Le **Calorifugeage** (isolation) des tuyaux d'ECS est crucial pour l'économie d'énergie."
                },
            ]
        }
    }
}