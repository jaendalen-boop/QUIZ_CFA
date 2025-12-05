# Fichier : quiz_cap_patissier_100.py

quiz_data = {
    "title": "Quiz CAP Pâtissier : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE, SÉCURITÉ ET RÈGLEMENTATION (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Hygiène, Sécurité et Réglementation (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la température maximale de conservation des pâtisseries contenant des crèmes à base d'œufs (crème pâtissière, mousse à base d'œufs) en enceinte réfrigérée positive ?",
                    "answerOptions": [
                        {"text": "0 °C", "isCorrect": False},
                        {"text": "Entre 0 °C et +4 °C (température de réfrigération standard pour les produits sensibles).", "isCorrect": True},
                        {"text": "+8 °C", "isCorrect": False},
                        {"text": "+12 °C", "isCorrect": False}
                    ],
                    "correction": "Le respect des **+4 °C** est crucial pour limiter la prolifération des bactéries pathogènes comme la salmonelle dans les crèmes."
                },
                {
                    "questionNumber": 2,
                    "question": "Que signifie l'acronyme **HACCP** en matière d'hygiène alimentaire ?",
                    "answerOptions": [
                        {"text": "Hygiène Alimentaire et Contrôle de la Contamination des Produits.", "isCorrect": False},
                        {"text": "Hazard Analysis Critical Control Point (Analyse des Dangers et Points Critiques pour leur Maîtrise).", "isCorrect": True},
                        {"text": "Hauteur, Approche, Contrôle, Conformité, Protection.", "isCorrect": False},
                        {"text": "Habitudes Alimentaires et Chaîne de Préparation des Plats.", "isCorrect": False}
                    ],
                    "correction": "L'**HACCP** est une méthode de travail visant à garantir la sécurité sanitaire des aliments."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la zone du laboratoire (selon la 'marche en avant') où l'on effectue le lavage des fruits, des légumes ou la décongélation des matières premières ?",
                    "answerOptions": [
                        {"text": "La zone de finition.", "isCorrect": False},
                        {"text": "La Zone 'Sale' ou 'Préparation Froide' (où le risque de contamination est le plus élevé).", "isCorrect": True},
                        {"text": "La zone de cuisson.", "isCorrect": False},
                        {"text": "La zone de stockage sec.", "isCorrect": False}
                    ],
                    "correction": "Le principe de la **marche en avant** exige la séparation des zones pour éviter la contamination croisée."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le danger associé à la consommation de produits à base d'œufs crus (mousses, mayonnaise, tiramisu) si la chaîne du froid n'est pas respectée ?",
                    "answerOptions": [
                        {"text": "La listériose.", "isCorrect": False},
                        {"text": "La Salmonellose (causée par la bactérie *Salmonella*).", "isCorrect": True},
                        {"text": "Le botulisme.", "isCorrect": False},
                        {"text": "La gastro-entérite virale.", "isCorrect": False}
                    ],
                    "correction": "La **Salmonellose** est le risque majeur des crèmes aux œufs mal conservées."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le rôle d'un **gant cotte de mailles** en pâtisserie ?",
                    "answerOptions": [
                        {"text": "Empêcher le contact avec les produits chauds.", "isCorrect": False},
                        {"text": "Protéger la main contre les coupures lors de l'utilisation d'une trancheuse à pain ou de couteaux très aiguisés (rare en pâtisserie, plus courant en boucherie/charcuterie).", "isCorrect": True},
                        {"text": "Assurer l'étanchéité.", "isCorrect": False},
                        {"text": "Isoler du froid.", "isCorrect": False}
                    ],
                    "correction": "Le **gant cotte de mailles** est un EPI (Équipement de Protection Individuelle) contre les blessures mécaniques."
                },
                {
                    "questionNumber": 6,
                    "question": "Pourquoi le port d'un **calot** ou d'une charlotte est-il obligatoire au laboratoire ?",
                    "answerOptions": [
                        {"text": "Pour avoir chaud.", "isCorrect": False},
                        {"text": "Pour empêcher la chute des cheveux (corps étrangers) dans les préparations (risque physique de contamination).", "isCorrect": True},
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Pour absorber la sueur.", "isCorrect": False}
                    ],
                    "correction": "Le **calot** ou la charlotte est essentiel pour l'hygiène de base."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle doit être la température minimale atteinte au cœur d'un produit (viande, appareils) pour garantir la destruction des bactéries (cuisson) ?",
                    "answerOptions": [
                        {"text": "40 °C", "isCorrect": False},
                        {"text": "63 °C (température recommandée par la réglementation pour la destruction de la plupart des micro-organismes).", "isCorrect": True},
                        {"text": "100 °C", "isCorrect": False},
                        {"text": "55 °C", "isCorrect": False}
                    ],
                    "correction": "La cuisson doit atteindre **63 °C** au minimum pour être considérée comme 'sûre'."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel est le rôle du **Plan de Maîtrise Sanitaire (PMS)** ?",
                    "answerOptions": [
                        {"text": "Créer de nouvelles recettes.", "isCorrect": False},
                        {"text": "Décrire les mesures prises par l'établissement pour assurer l'hygiène et la sécurité sanitaire de ses productions (ensemble des procédures HACCP).", "isCorrect": True},
                        {"text": "Gérer les commandes.", "isCorrect": False},
                        {"text": "Contrôler la comptabilité.", "isCorrect": False}
                    ],
                    "correction": "Le **PMS** est un document obligatoire pour tout professionnel de l'agroalimentaire."
                },
                {
                    "questionNumber": 9,
                    "question": "Comment doit-on nettoyer et désinfecter le plan de travail après avoir manipulé des œufs ou de la viande (si présente en cuisine salée) ?",
                    "answerOptions": [
                        {"text": "Un simple coup d'éponge suffit.", "isCorrect": False},
                        {"text": "Nettoyage (détergent), rinçage, puis désinfection (produit biocide) et rinçage final.", "isCorrect": True},
                        {"text": "Uniquement désinfection sans nettoyage préalable.", "isCorrect": False},
                        {"text": "Laver à l'eau chaude uniquement.", "isCorrect": False}
                    ],
                    "correction": "Le processus **Nettoyage-Rinçage-Désinfection-Rinçage** est la procédure standard."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le risque de remettre une crème chaude (ex : crème pâtissière) immédiatement au réfrigérateur sans la refroidir rapidement ?",
                    "answerOptions": [
                        {"text": "La crème va figer trop vite.", "isCorrect": False},
                        {"text": "La chaleur va contaminer le reste du réfrigérateur et augmenter sa température, mettant en danger les autres produits (rupture de la chaîne du froid).", "isCorrect": True},
                        {"text": "La crème va devenir liquide.", "isCorrect": False},
                        {"text": "La crème va coller au récipient.", "isCorrect": False}
                    ],
                    "correction": "Le **refroidissement rapide** (cellule de refroidissement ou bain-marie glacé) est obligatoire pour les produits chauds."
                },
                {
                    "questionNumber": 11,
                    "question": "Qu'est-ce qu'une **Contamination Croisée** ?",
                    "answerOptions": [
                        {"text": "Le mélange de deux crèmes différentes.", "isCorrect": False},
                        {"text": "Le transfert de micro-organismes (bactéries, virus) d'un aliment (cru ou sale) à un autre (cuit ou propre) via les mains, les outils ou le plan de travail.", "isCorrect": True},
                        {"text": "L'utilisation de deux farines différentes.", "isCorrect": False},
                        {"text": "Le mélange de deux saveurs.", "isCorrect": False}
                    ],
                    "correction": "La **Contamination croisée** est le danger principal, d'où la séparation des zones et des ustensiles."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la méthode de conservation consistant à abaisser rapidement la température d'un produit cuit de +63 °C à +10 °C en moins de deux heures ?",
                    "answerOptions": [
                        {"text": "La surgélation.", "isCorrect": False},
                        {"text": "La Réfrigération rapide (ou Refroidissement en cellule).", "isCorrect": True},
                        {"text": "La stérilisation.", "isCorrect": False},
                        {"text": "La pasteurisation.", "isCorrect": False}
                    ],
                    "correction": "Le **Refroidissement rapide** est essentiel pour passer la 'zone de danger' (entre +10 °C et +63 °C) au plus vite."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est l'interdiction absolue pour le personnel de laboratoire concernant les bijoux et accessoires ?",
                    "answerOptions": [
                        {"text": "Les montres sont interdites.", "isCorrect": False},
                        {"text": "Le port de tout bijou, y compris les alliances et boucles d'oreilles, est interdit (risque de chute de corps étranger et difficulté de lavage des mains).", "isCorrect": True},
                        {"text": "Les lunettes sont interdites.", "isCorrect": False},
                        {"text": "Les chaussures de sécurité sont interdites.", "isCorrect": False}
                    ],
                    "correction": "Les **bijoux** et le vernis à ongles sont des vecteurs de contamination et sont formellement interdits."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est l'outil utilisé pour vérifier rapidement la température au cœur d'un produit (crème, appareil à flan) ?",
                    "answerOptions": [
                        {"text": "Le thermomètre à mercure.", "isCorrect": False},
                        {"text": "Le Thermomètre à sonde électronique (ou Thermocouple).", "isCorrect": True},
                        {"text": "Le pèse-sirop.", "isCorrect": False},
                        {"text": "Le réfractomètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Thermomètre à sonde** est indispensable pour la traçabilité HACCP."
                },
                {
                    "questionNumber": 15,
                    "question": "Que doit-on faire avant de manipuler des produits finis prêts à être vendus (ex : mettre en boîte des macarons) ?",
                    "answerOptions": [
                        {"text": "Mettre des gants chirurgicaux (non obligatoires, mais utilisés).", "isCorrect": False},
                        {"text": "Se laver les mains méticuleusement et changer de tablier ou de blouse si nécessaire (passage de zone 'sale' à 'propre').", "isCorrect": True},
                        {"text": "Changer de chaussures.", "isCorrect": False},
                        {"text": "Manger.", "isCorrect": False}
                    ],
                    "correction": "Le **lavage des mains** est l'action la plus importante pour éviter la contamination."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la définition d'un **Allergène** ?",
                    "answerOptions": [
                        {"text": "Un produit très cher.", "isCorrect": False},
                        {"text": "Une substance (protéine) capable de provoquer une réaction immunitaire (allergie) chez certaines personnes (lait, œufs, fruits à coque, gluten, etc.).", "isCorrect": True},
                        {"text": "Un ingrédient rare.", "isCorrect": False},
                        {"text": "Un produit périmé.", "isCorrect": False}
                    ],
                    "correction": "L'affichage et la connaissance des **14 allergènes majeurs** sont obligatoires."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est l'action à réaliser sur une pâte feuilletée avant l'enfournement pour éviter qu'elle ne gonfle trop ou de manière irrégulière ?",
                    "answerOptions": [
                        {"text": "La dorer.", "isCorrect": False},
                        {"text": "La piquer à l'aide d'une pique-vite ou d'une fourchette (éviter l'emprisonnement de la vapeur).", "isCorrect": True},
                        {"text": "La congeler.", "isCorrect": False},
                        {"text": "La fleurer.", "isCorrect": False}
                    ],
                    "correction": "Le **piquage** permet à la vapeur d'eau de s'échapper, régulant ainsi le développement."
                },
                {
                    "questionNumber": 18,
                    "question": "Qu'est-ce qui est mesuré par le test de l'**Alvéographe de Chopin** ?",
                    "answerOptions": [
                        {"text": "La teneur en gluten du beurre.", "isCorrect": False},
                        {"text": "La force boulangère (force des pâtes 'W') et l'extensibilité des farines (critères essentiels pour les viennoiseries et le pain).", "isCorrect": True},
                        {"text": "Le pH du sucre.", "isCorrect": False},
                        {"text": "La teneur en eau des fruits.", "isCorrect": False}
                    ],
                    "correction": "La **force W** détermine si une farine est adaptée à la panification ou à la pâtisserie fine."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel risque peut engendrer la consommation d'une pâtisserie trop riche en colorants artificiels non homologués ?",
                    "answerOptions": [
                        {"text": "Un goût amer.", "isCorrect": False},
                        {"text": "Un risque d'hyperactivité et des problèmes de santé (selon la réglementation en vigueur).", "isCorrect": True},
                        {"text": "Elle ne dore pas à la cuisson.", "isCorrect": False},
                        {"text": "Elle gèle plus rapidement.", "isCorrect": False}
                    ],
                    "correction": "L'utilisation des **additifs** (colorants, conservateurs) est strictement réglementée."
                },
                {
                    "questionNumber": 20,
                    "question": "Lors d'une brûlure thermique (contact four, caramel, etc.), quelle est la première chose à faire ?",
                    "answerOptions": [
                        {"text": "Percer la cloque.", "isCorrect": False},
                        {"text": "Refroidir la zone brûlée immédiatement sous un jet d'eau tiède (15°C) pendant au moins 10 à 15 minutes.", "isCorrect": True},
                        {"text": "Appliquer du beurre.", "isCorrect": False},
                        {"text": "Couvrir d'un pansement sans rincer.", "isCorrect": False}
                    ],
                    "correction": "Le **refroidissement** est le premier soin pour stopper la propagation de la brûlure."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : MATIÈRES PREMIÈRES FONDAMENTALES (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Matières Premières Fondamentales (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le rôle principal du **Gluten** dans la farine de blé ?",
                    "answerOptions": [
                        {"text": "Donner de la couleur à la pâte.", "isCorrect": False},
                        {"text": "Former un réseau élastique et visqueux (après hydratation et pétrissage) qui retient le gaz carbonique (CO2) et permet le développement (la 'levée') de la pâte.", "isCorrect": True},
                        {"text": "Sucrer la pâte.", "isCorrect": False},
                        {"text": "Colorer le produit.", "isCorrect": False}
                    ],
                    "correction": "Le **Gluten** (protéines) est le squelette des pâtes levées (viennoiserie, pain)."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment appelle-t-on le sucre obtenu par l'hydrolyse du saccharose (mélange de glucose et de fructose) utilisé pour sa capacité à empêcher la cristallisation et à rendre les crèmes plus souples ?",
                    "answerOptions": [
                        {"text": "Le sucre glace.", "isCorrect": False},
                        {"text": "Le Sucre inverti (ou Trimoline).", "isCorrect": True},
                        {"text": "Le sucre candi.", "isCorrect": False},
                        {"text": "Le fondant.", "isCorrect": False}
                    ],
                    "correction": "Le **Sucre inverti** est un agent anti-cristallisant essentiel en confiserie et pour les ganaches."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la température de fusion approximative du **Beurre de Couverture (Beurre de Cacao)**, ce qui lui donne son caractère 'cassant' et 'fondant en bouche' ?",
                    "answerOptions": [
                        {"text": "10 °C", "isCorrect": False},
                        {"text": "Environ 32 °C - 35 °C (légèrement en dessous de la température corporelle).", "isCorrect": True},
                        {"text": "45 °C", "isCorrect": False},
                        {"text": "60 °C", "isCorrect": False}
                    ],
                    "correction": "La faible température de fusion du **Beurre de Cacao** est responsable de la sensation agréable du chocolat en bouche."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est l'agent de liaison et de texturation principal dans les crèmes et appareils (ex : appareil à flan) ?",
                    "answerOptions": [
                        {"text": "L'eau.", "isCorrect": False},
                        {"text": "L'Œuf (le jaune d'œuf contient des protéines et des lipides aux propriétés émulsifiantes et coagulantes).", "isCorrect": True},
                        {"text": "Le sel.", "isCorrect": False},
                        {"text": "Le bicarbonate de soude.", "isCorrect": False}
                    ],
                    "correction": "L'**Œuf** est l'ingrédient de base des appareils et crèmes liantes."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le rôle de l'**Amidonnier (Amidon)** dans une crème pâtissière ?",
                    "answerOptions": [
                        {"text": "Donner du goût.", "isCorrect": False},
                        {"text": "Permettre la gélification et l'épaississement de la crème (prise de masse et viscosité).", "isCorrect": True},
                        {"text": "Rendre la crème plus liquide.", "isCorrect": False},
                        {"text": "Protéger la crème de la chaleur.", "isCorrect": False}
                    ],
                    "correction": "L'**Amidon** (maïzena, farine) capte l'eau et crée la texture onctueuse de la crème pâtissière."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le type de farine le plus couramment utilisé pour la pâtisserie (pâtes légères, fonds de tarte, gâteaux) ?",
                    "answerOptions": [
                        {"text": "La farine Type 150 (complète).", "isCorrect": False},
                        {"text": "La Farine Type 45 (T45) ou Type 55 (T55) (faible taux de cendres, faible en protéines/gluten, favorise le croustillant et le sablage).", "isCorrect": True},
                        {"text": "La farine Type 80 (bise).", "isCorrect": False},
                        {"text": "La farine Type 110 (semi-complète).", "isCorrect": False}
                    ],
                    "correction": "La **T45** est la plus fine et la plus adaptée aux pâtes sèches et aux gâteaux."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est l'ingrédient indispensable utilisé dans la pâte à choux pour créer le 'craquelin' (croûte fine et croustillante) ?",
                    "answerOptions": [
                        {"text": "La farine de seigle.", "isCorrect": False},
                        {"text": "Un mélange de beurre, sucre et farine étalé finement et congelé.", "isCorrect": True},
                        {"text": "Le sucre glace.", "isCorrect": False},
                        {"text": "La gélatine.", "isCorrect": False}
                    ],
                    "correction": "Le **Craquelin** apporte du croquant et une belle uniformité au chou."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le rôle du **Sel** dans une pâte levée (viennoiserie, pain) ?",
                    "answerOptions": [
                        {"text": "Accélérer la fermentation.", "isCorrect": False},
                        {"text": "Contrôler (ralentir) l'activité des levures et donner du goût au produit.", "isCorrect": True},
                        {"text": "Assouplir la pâte.", "isCorrect": False},
                        {"text": "Blanchir la pâte.", "isCorrect": False}
                    ],
                    "correction": "Le **Sel** est un agent de sapidité et un régulateur de la fermentation."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la principale différence entre la **Gélatine animale (feuille ou poudre)** et l'**Agar-Agar** ?",
                    "answerOptions": [
                        {"text": "L'Agar-Agar est moins cher.", "isCorrect": False},
                        {"text": "L'Agar-Agar est d'origine végétale (algues), ne nécessite pas de refroidissement pour gélifier et résiste à des températures plus élevées.", "isCorrect": True},
                        {"text": "La gélatine est plus puissante.", "isCorrect": False},
                        {"text": "L'Agar-Agar donne un goût amer.", "isCorrect": False}
                    ],
                    "correction": "L'**Agar-Agar** est utilisé pour les préparations végétales ou les desserts qui doivent rester stables à température ambiante."
                },
                {
                    "questionNumber": 30,
                    "question": "Qu'est-ce que le **Cacao en poudre dégraissé** ?",
                    "answerOptions": [
                        {"text": "Du chocolat au lait.", "isCorrect": False},
                        {"text": "Du Cacao dont la majeure partie du beurre de cacao a été extraite (faible teneur en matière grasse, goût intense).", "isCorrect": True},
                        {"text": "Du chocolat blanc.", "isCorrect": False},
                        {"text": "Du cacao sucré.", "isCorrect": False}
                    ],
                    "correction": "Le **Cacao en poudre** standard contient au moins 20% de beurre de cacao. Le dégraissé en contient moins de 10%."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le rôle de la **Lécithine** dans le jaune d'œuf, souvent utilisée en pâtisserie et en cuisine ?",
                    "answerOptions": [
                        {"text": "Épaissir.", "isCorrect": False},
                        {"text": "Émulsifier (stabiliser un mélange normalement non miscible, comme l'eau et la matière grasse).", "isCorrect": True},
                        {"text": "Sucrer.", "isCorrect": False},
                        {"text": "Dorer.", "isCorrect": False}
                    ],
                    "correction": "La **Lécithine** est un excellent agent émulsifiant (ex : pour la crème anglaise, la mayonnaise)."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'effet de l'ajout de **Miel** ou de **Glucose** dans un appareil, notamment pour la conservation et l'humidité ?",
                    "answerOptions": [
                        {"text": "Assécher l'appareil.", "isCorrect": False},
                        {"text": "Augmenter le pouvoir sucrant et retenir l'humidité (agent hygroscopique), prolongeant ainsi la conservation.", "isCorrect": True},
                        {"text": "Durcir la pâte.", "isCorrect": False},
                        {"text": "Donner une couleur blanche.", "isCorrect": False}
                    ],
                    "correction": "Le **Miel** et le **Glucose** sont des agents humectants."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la caractéristique principale du **Beurre AOP (Appellation d'Origine Protégée)** pour la pâtisserie, notamment le feuilletage ?",
                    "answerOptions": [
                        {"text": "Il est plus salé.", "isCorrect": False},
                        {"text": "Il garantit une faible teneur en eau (matière grasse pure et ferme), une grande plasticité et une qualité aromatique constante, essentielle pour un bon feuilletage.", "isCorrect": True},
                        {"text": "Il est plus mou.", "isCorrect": False},
                        {"text": "Il est plus cher.", "isCorrect": False}
                    ],
                    "correction": "Un **Beurre de Tourage** de qualité (souvent sec, > 82% MG) est indispensable au feuilletage."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le rôle de la **Levure Biologique (Levure de boulanger)** dans la pâte à croissant ou à brioche ?",
                    "answerOptions": [
                        {"text": "Donner du croustillant.", "isCorrect": False},
                        {"text": "Produire du gaz carbonique (CO2) par fermentation, ce qui fait lever (pousser) la pâte avant et pendant la cuisson.", "isCorrect": True},
                        {"text": "Faire dorer.", "isCorrect": False},
                        {"text": "Assurer la coloration.", "isCorrect": False}
                    ],
                    "correction": "La **Levure** est un micro-organisme vivant qui nécessite eau et chaleur pour s'activer."
                },
                {
                    "questionNumber": 35,
                    "question": "Comment appelle-t-on la **couverture de chocolat noir** qui contient au moins 70% de cacao (matière sèche) ?",
                    "answerOptions": [
                        {"text": "Chocolat au lait.", "isCorrect": False},
                        {"text": "Chocolat noir 'fort' ou de 'Grand Cru'.", "isCorrect": True},
                        {"text": "Chocolat blond.", "isCorrect": False},
                        {"text": "Chocolat blanc.", "isCorrect": False}
                    ],
                    "correction": "Plus le pourcentage de cacao est élevé, plus le goût est intense et moins il est sucré."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le rôle principal de la **Pectine (NH)** utilisée en confiserie et dans les entremets aux fruits ?",
                    "answerOptions": [
                        {"text": "Colorer.", "isCorrect": False},
                        {"text": "Gélifier (épaississant à base de fruits) pour donner la texture 'confiture' ou la prise des inserts fruités (N.H. pour la gélification à chaud/thermoréversible).", "isCorrect": True},
                        {"text": "Sucrer.", "isCorrect": False},
                        {"text": "Émulsifier.", "isCorrect": False}
                    ],
                    "correction": "La **Pectine** est un gélifiant naturel dérivé de l'écorce des agrumes ou de la pomme."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'effet d'une **Farine trop riche en protéines (gluten)** sur une pâte sablée ?",
                    "answerOptions": [
                        {"text": "Elle sera très friable.", "isCorrect": False},
                        {"text": "Elle rend la pâte trop élastique ('caoutchouteuse') et difficile à étaler après hydratation, entraînant un gâteau dur après cuisson.", "isCorrect": True},
                        {"text": "Elle sera plus douce.", "isCorrect": False},
                        {"text": "Elle ne se développe pas.", "isCorrect": False}
                    ],
                    "correction": "La **Pâte sablée** doit être travaillée le moins possible pour ne pas développer le gluten."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la particularité du **Beurre clarifié (ou Ghee)** ?",
                    "answerOptions": [
                        {"text": "Il est congelé.", "isCorrect": False},
                        {"text": "C'est du beurre fondu dont on a retiré le petit lait (protéines) et l'eau ; il a un point de fumée plus élevé (idéal pour la cuisson) et se conserve plus longtemps.", "isCorrect": True},
                        {"text": "Il est plus dur.", "isCorrect": False},
                        {"text": "Il est plus salé.", "isCorrect": False}
                    ],
                    "correction": "Le **Beurre clarifié** est une matière grasse presque pure."
                },
                {
                    "questionNumber": 39,
                    "question": "Comment appelle-t-on le processus de fusion et de recristallisation du chocolat visant à stabiliser le beurre de cacao pour qu'il soit brillant, cassant et qu'il ne 'grise' pas ?",
                    "answerOptions": [
                        {"text": "Le tempérage.", "isCorrect": True},
                        {"text": "La cristallisation.", "isCorrect": False},
                        {"text": "L'émulsion.", "isCorrect": False},
                        {"text": "Le blanchiment.", "isCorrect": False}
                    ],
                    "correction": "Le **Tempérage** (ou précristallisation) permet d'obtenir la forme de cristal de beurre de cacao stable (Forme V)."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel ingrédient est essentiel pour réaliser une **Meringue Française** (la plus simple, souvent utilisée pour les décors ou comme base) ?",
                    "answerOptions": [
                        {"text": "De la crème fraîche.", "isCorrect": False},
                        {"text": "Du Blanc d'œuf et du sucre semoule (montage des blancs puis ajout progressif du sucre).", "isCorrect": True},
                        {"text": "Du jaune d'œuf.", "isCorrect": False},
                        {"text": "De la levure chimique.", "isCorrect": False}
                    ],
                    "correction": "La **Meringue Française** est la plus légère mais la moins stable."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : CRÈMES, APPAREILS ET GARNITURES (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Crèmes, Appareils et Garnitures (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le risque de ne pas fouetter la **Crème Pâtissière** suffisamment longtemps ou de la laisser refroidir sans protection ?",
                    "answerOptions": [
                        {"text": "Elle sera trop sucrée.", "isCorrect": False},
                        {"text": "Elle risque de faire des grumeaux ou de développer une croûte dure et sèche en surface.", "isCorrect": True},
                        {"text": "Elle va fondre.", "isCorrect": False},
                        {"text": "Elle sera trop liquide.", "isCorrect": False}
                    ],
                    "correction": "La **Crème pâtissière** doit être filée au contact (film alimentaire) et turbinée après refroidissement."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est l'appareil de base composé de jaunes d'œufs, de sucre, de lait et de crème, cuit au four au bain-marie (ex : Crème brûlée ou Flan) ?",
                    "answerOptions": [
                        {"text": "La mousse.", "isCorrect": False},
                        {"text": "L'Appareil à crème renversée (ou Appareil à flan ou Crème prise).", "isCorrect": True},
                        {"text": "Le biscuit cuillère.", "isCorrect": False},
                        {"text": "Le streusel.", "isCorrect": False}
                    ],
                    "correction": "La cuisson au **bain-marie** permet une cuisson douce et uniforme de l'appareil."
                },
                {
                    "questionNumber": 43,
                    "question": "Comment appelle-t-on le mélange de base de chocolat et de crème liquide, souvent utilisé pour les intérieurs de truffes, les glaçages ou les garnitures ?",
                    "answerOptions": [
                        {"text": "Le fondant.", "isCorrect": False},
                        {"text": "La Ganache (chocolat fondu et crème chaude, créant une émulsion).", "isCorrect": True},
                        {"text": "La crème au beurre.", "isCorrect": False},
                        {"text": "La crème fouettée.", "isCorrect": False}
                    ],
                    "correction": "La **Ganache** est une émulsion stable dont la texture dépend du ratio crème/chocolat."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est l'effet de l'incorporation de **beurre doux** dans une crème pâtissière froide (pour obtenir une Crème Mousseline) ?",
                    "answerOptions": [
                        {"text": "Elle devient plus lourde.", "isCorrect": False},
                        {"text": "Elle apporte de la légèreté, de l'onctuosité et une grande stabilité à température ambiante (nécessaire pour le Fraisier ou le Paris-Brest).", "isCorrect": True},
                        {"text": "Elle devient plus liquide.", "isCorrect": False},
                        {"text": "Elle donne un goût amer.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Mousseline** est une crème pâtissière allégée et enrichie en beurre."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment appelle-t-on la crème obtenue par ajout de gélatine et de crème fouettée à une base (crème pâtissière, purée de fruits) pour obtenir une texture légère et aérienne ?",
                    "answerOptions": [
                        {"text": "La crème au beurre.", "isCorrect": False},
                        {"text": "La Crème Bavaroise (ou Bavarois).", "isCorrect": True},
                        {"text": "La crème Diplomate.", "isCorrect": False},
                        {"text": "La crème Chiboust.", "isCorrect": False}
                    ],
                    "correction": "La **Bavaroise** est stabilisée par la gélatine et allégée par la crème fouettée."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la technique utilisée pour incorporer de la crème fouettée ou des blancs d'œufs montés à un appareil plus lourd sans le faire retomber ?",
                    "answerOptions": [
                        {"text": "Fouetter rapidement.", "isCorrect": False},
                        {"text": "Mélanger délicatement 'à la maryse' (spatule souple) en soulevant la masse de bas en haut (mouvement de coupe et retournement).", "isCorrect": True},
                        {"text": "Mélanger au batteur.", "isCorrect": False},
                        {"text": "Chauffer l'appareil.", "isCorrect": False}
                    ],
                    "correction": "Le **mélange à la maryse** (ou 'en coupant') préserve l'air incorporé (volume)."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est l'ingrédient principal de la **Crème au beurre** (méthode française) ?",
                    "answerOptions": [
                        {"text": "Du fromage blanc.", "isCorrect": False},
                        {"text": "Du Beurre monté avec un sirop de sucre et des jaunes d'œufs (ou des œufs entiers).", "isCorrect": True},
                        {"text": "De la crème fraîche.", "isCorrect": False},
                        {"text": "De la crème pâtissière.", "isCorrect": False}
                    ],
                    "correction": "La **Crème au beurre** est une base solide pour la décoration et les intérieurs denses (Opéra, bûches)."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment appelle-t-on la technique de montage qui consiste à battre les jaunes d'œufs avec le sucre jusqu'à ce que le mélange blanchisse et augmente de volume ?",
                    "answerOptions": [
                        {"text": "Sabler.", "isCorrect": False},
                        {"text": "Blanchir.", "isCorrect": True},
                        {"text": "Foncer.", "isCorrect": False},
                        {"text": "Détremper.", "isCorrect": False}
                    ],
                    "correction": "Le **blanchiment** est la base de nombreuses crèmes et appareils (crème anglaise, génoise)."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le risque de monter la **Crème liquide entière** (minimum 30% MG) en chantilly trop longtemps ?",
                    "answerOptions": [
                        {"text": "Elle devient trop liquide.", "isCorrect": False},
                        {"text": "Elle se transforme en beurre (rupture de l'émulsion).", "isCorrect": True},
                        {"text": "Elle ne monte pas.", "isCorrect": False},
                        {"text": "Elle prend un goût amer.", "isCorrect": False}
                    ],
                    "correction": "Le **montage** doit être arrêté au bon moment (crème bien ferme, mais lisse)."
                },
                {
                    "questionNumber": 50,
                    "question": "Qu'est-ce qu'une **Crème Anglaise** (base du parfait, de l'entremets glacé ou consommée comme sauce) ?",
                    "answerOptions": [
                        {"text": "Une crème fouettée au sucre glace.", "isCorrect": False},
                        {"text": "Une préparation onctueuse à base de lait, de jaunes d'œufs et de sucre, cuite 'à la nappe' (82-85 °C).", "isCorrect": True},
                        {"text": "Un mélange de beurre et de sucre.", "isCorrect": False},
                        {"text": "Une crème pâtissière sans amidon.", "isCorrect": False}
                    ],
                    "correction": "La cuisson **à la nappe** signifie que la crème recouvre le dos de la spatule (coagulation des protéines)."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est l'élément essentiel pour que la **Pâte à Choux** gonfle correctement (en dehors des œufs) ?",
                    "answerOptions": [
                        {"text": "Le sucre glace.", "isCorrect": False},
                        {"text": "La Maîtrise de l'humidité et de la vapeur d'eau (l'eau de la pâte se transforme en vapeur, créant le vide interne).", "isCorrect": True},
                        {"text": "Le miel.", "isCorrect": False},
                        {"text": "La levure chimique.", "isCorrect": False}
                    ],
                    "correction": "La **vapeur** est le moteur du développement de la pâte à choux."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment appelle-t-on la **Crème Diplomate** ?",
                    "answerOptions": [
                        {"text": "Une crème au beurre légère.", "isCorrect": False},
                        {"text": "Un mélange de crème pâtissière, de gélatine et de crème fouettée.", "isCorrect": True},
                        {"text": "Une crème anglaise épaisse.", "isCorrect": False},
                        {"text": "Une simple crème fouettée.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Diplomate** est utilisée pour le Millefeuille ou la tarte tropézienne."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le rôle du **sirop d'imbibage** (souvent eau, sucre et alcool ou arômes) sur un biscuit ?",
                    "answerOptions": [
                        {"text": "Le rendre plus ferme.", "isCorrect": False},
                        {"text": "Apporter de l'humidité, du goût et améliorer la texture et la conservation (évite que le biscuit soit sec).", "isCorrect": True},
                        {"text": "Le colorer.", "isCorrect": False},
                        {"text": "Le faire lever.", "isCorrect": False}
                    ],
                    "correction": "L'**imbibage** est essentiel pour les entremets (génoise, biscuit Joconde)."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'appareil de base composé d'œufs, de sucre, de poudre d'amande et d'amandes effilées, utilisé comme support (ex : Frangipane) ?",
                    "answerOptions": [
                        {"text": "La Crème d'amande (ou appareil à financier).", "isCorrect": True},
                        {"text": "La crème pâtissière.", "isCorrect": False},
                        {"text": "La meringue suisse.", "isCorrect": False},
                        {"text": "La crème au beurre.", "isCorrect": False}
                    ],
                    "correction": "La **Crème d'amande** est la base de la galette des rois (souvent mélangée à de la crème pâtissière pour faire la Frangipane)."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le risque d'ajouter de la **crème froide** à du chocolat fondu **trop chaud** ?",
                    "answerOptions": [
                        {"text": "Le chocolat va brûler.", "isCorrect": False},
                        {"text": "L'émulsion va rater (granuleuse, huileuse, le mélange 'tranche') car la matière grasse et l'eau ne s'incorporent pas correctement.", "isCorrect": True},
                        {"text": "Le chocolat devient dur.", "isCorrect": False},
                        {"text": "Le goût sera amer.", "isCorrect": False}
                    ],
                    "correction": "Pour une **Ganache** réussie, la température du chocolat fondu et de la crème doivent être proches et contrôlées (vers 45-50°C)."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment appelle-t-on le procédé par lequel une crème anglaise est cuite et épaissie grâce à la coagulation des protéines des jaunes d'œufs ?",
                    "answerOptions": [
                        {"text": "La gélification.", "isCorrect": False},
                        {"text": "La Coagulation (processus irréversible déclenché par la chaleur).", "isCorrect": True},
                        {"text": "La caramélisation.", "isCorrect": False},
                        {"text": "La fermentation.", "isCorrect": False}
                    ],
                    "correction": "La **Coagulation** doit être douce pour ne pas faire des œufs brouillés (d'où le terme 'cuire à la nappe')."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est l'élément qui doit obligatoirement être ajouté pour utiliser la **Pectine NH** ?",
                    "answerOptions": [
                        {"text": "Le sel.", "isCorrect": False},
                        {"text": "Un Acide (citron, jus de fruit, etc.) et du Sucre (pour que la gélification se produise).", "isCorrect": True},
                        {"text": "L'eau.", "isCorrect": False},
                        {"text": "Le colorant.", "isCorrect": False}
                    ],
                    "correction": "La **Pectine** est un gélifiant dont la prise dépend du sucre et de l'acidité."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le type de meringue obtenu par cuisson des blancs d'œufs au bain-marie avec le sucre (mélange chauffé à 50-60°C) ?",
                    "answerOptions": [
                        {"text": "La meringue française.", "isCorrect": False},
                        {"text": "La Meringue Suisse (très stable, dense et brillante, idéale pour les décors et les fonds de tarte).", "isCorrect": True},
                        {"text": "La meringue italienne.", "isCorrect": False},
                        {"text": "La meringue japonaise.", "isCorrect": False}
                    ],
                    "correction": "La **Meringue Suisse** est plus solide que la française."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle est la principale différence entre la **Mousseline** et la **Crème Pâtissière** ?",
                    "answerOptions": [
                        {"text": "La mousseline est plus lourde.", "isCorrect": False},
                        {"text": "La Mousseline est enrichie en beurre pour la rendre plus onctueuse et stable (crème pâtissière + beurre incorporé après refroidissement).", "isCorrect": True},
                        {"text": "La mousseline ne contient pas d'amidon.", "isCorrect": False},
                        {"text": "La mousseline est cuite plus longtemps.", "isCorrect": False}
                    ],
                    "correction": "La **Mousseline** est la crème de base du Fraisier et du Paris-Brest."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment appelle-t-on le procédé qui consiste à frotter du bout des doigts un mélange de beurre froid, de farine et de sucre pour obtenir une texture sableuse ?",
                    "answerOptions": [
                        {"text": "Fraser.", "isCorrect": False},
                        {"text": "Sabler (ou Crémer).", "isCorrect": True},
                        {"text": "Détremper.", "isCorrect": False},
                        {"text": "Bouler.", "isCorrect": False}
                    ],
                    "correction": "Le **sablage** est l'étape initiale pour les pâtes sablées ou sucrées (pour imperméabiliser la farine et le beurre)."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : PÂTES DE BASE ET TECHNIQUES DE TRAVAIL (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Pâtes de Base et Techniques de Travail (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le nom de la technique consistant à beurrer et fariner l'intérieur d'un moule avant de verser la pâte ?",
                    "answerOptions": [
                        {"text": "Fouetter.", "isCorrect": False},
                        {"text": "Chemiser (ou Doublage).", "isCorrect": True},
                        {"text": "Crémer.", "isCorrect": False},
                        {"text": "Glacer.", "isCorrect": False}
                    ],
                    "correction": "Le **chemissage** permet un démoulage facile et propre."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la caractéristique essentielle de la **Pâte Sucrée** par rapport à la pâte sablée ?",
                    "answerOptions": [
                        {"text": "Elle est plus salée.", "isCorrect": False},
                        {"text": "Elle contient des œufs entiers et la méthode initiale est le 'crémage' (beurre et sucre travaillés d'abord), ce qui la rend moins friable que la sablée.", "isCorrect": True},
                        {"text": "Elle est plus riche en levure.", "isCorrect": False},
                        {"text": "Elle ne contient pas de farine.", "isCorrect": False}
                    ],
                    "correction": "La **Pâte Sucrée** est plus robuste et s'utilise facilement pour les tartelettes."
                },
                {
                    "questionNumber": 63,
                    "question": "Qu'est-ce qu'une **Détrempe** dans la fabrication de la pâte feuilletée ?",
                    "answerOptions": [
                        {"text": "Le beurre de tourage.", "isCorrect": False},
                        {"text": "Le mélange de base de farine, eau et sel (et parfois un peu de beurre) qui sera enveloppé par le beurre de tourage.", "isCorrect": True},
                        {"text": "La garniture de la galette.", "isCorrect": False},
                        {"text": "Le sirop d'imbibage.", "isCorrect": False}
                    ],
                    "correction": "La **Détrempe** est la base de la pâte feuilletée."
                },
                {
                    "questionNumber": 64,
                    "question": "Combien de **Tours Simples** sont nécessaires pour obtenir le feuilletage standard (et quel est le nombre de couches de beurre/détrempe après cuisson) ?",
                    "answerOptions": [
                        {"text": "1 tour simple (3 couches).", "isCorrect": False},
                        {"text": "6 tours simples (plus de 700 couches après cuisson, soit 3^6 = 729 couches théoriques).", "isCorrect": True},
                        {"text": "3 tours doubles (2^3 = 8 couches).", "isCorrect": False},
                        {"text": "2 tours simples (9 couches).", "isCorrect": False}
                    ],
                    "correction": "Le **feuilletage traditionnel** requiert 6 tours simples (3 plis) ou 4 tours doubles (4 plis)."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le risque de laisser la **pâte à croissant** (ou brioche) pointer trop longtemps avant l'étape de l'abaissage (façonnage) ?",
                    "answerOptions": [
                        {"text": "La pâte devient dure.", "isCorrect": False},
                        {"text": "La pâte s'acidifie (sur-fermentation), perd de sa force (la mie sera dense et sans alvéoles) et prend un goût trop alcoolisé.", "isCorrect": True},
                        {"text": "La pâte fond.", "isCorrect": False},
                        {"text": "Le beurre s'incorpore trop bien.", "isCorrect": False}
                    ],
                    "correction": "La **fermentation** doit être contrôlée (souvent en chambre de pousse ou au froid)."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment s'appelle l'opération qui consiste à couper l'excédent de pâte sur le bord d'un cercle à tarte après l'avoir foncée ?",
                    "answerOptions": [
                        {"text": "Abaisser.", "isCorrect": False},
                        {"text": "Ébarber.", "isCorrect": True},
                        {"text": "Bouler.", "isCorrect": False},
                        {"text": "Fleurer.", "isCorrect": False}
                    ],
                    "correction": "L'**ébarbage** permet une finition nette avant cuisson."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le risque de pétrir une **Pâte Sablée/Sucrée** trop longtemps après l'incorporation de la farine ?",
                    "answerOptions": [
                        {"text": "Elle sera trop molle.", "isCorrect": False},
                        {"text": "Le gluten se développe (pâte élastique), entraînant un retrait important à la cuisson et une texture dure (non sablée).", "isCorrect": True},
                        {"text": "Elle sera trop foncée.", "isCorrect": False},
                        {"text": "Elle colle trop.", "isCorrect": False}
                    ],
                    "correction": "Les **pâtes sèches** doivent être 'frasées' et travaillées le moins possible."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment appelle-t-on le procédé par lequel on ajoute un ingrédient chaud (sirop, lait) à un appareil froid (jaunes/sucre) pour éviter la coagulation des jaunes ?",
                    "answerOptions": [
                        {"text": "Chauffer.", "isCorrect": False},
                        {"text": "Tempérer (ou Détendre l'appareil).", "isCorrect": True},
                        {"text": "Mélanger.", "isCorrect": False},
                        {"text": "Monter.", "isCorrect": False}
                    ],
                    "correction": "Le **tempérage** consiste à ajouter progressivement le liquide chaud pour remonter doucement la température."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le rôle d'un **glaçage miroir** sur un entremets ?",
                    "answerOptions": [
                        {"text": "Apporter du croustillant.", "isCorrect": False},
                        {"text": "Apporter une finition esthétique brillante, une couleur intense et protéger le produit de la dessiccation (assèchement).", "isCorrect": True},
                        {"text": "Servir de garniture.", "isCorrect": False},
                        {"text": "Augmenter le volume.", "isCorrect": False}
                    ],
                    "correction": "Le **Glaçage miroir** est une finition à base de gélatine, glucose et chocolat ou nappage."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le risque d'utiliser un beurre de tourage **trop froid** ou une détrempe **trop chaude** pour le feuilletage ?",
                    "answerOptions": [
                        {"text": "Le feuilletage est trop grand.", "isCorrect": False},
                        {"text": "Le beurre se déchire (se casse) lors de l'abaissage, empêchant la création de fines couches régulières et ruinant le feuilletage (pâte qui 'déchire').", "isCorrect": True},
                        {"text": "La pâte ne lève pas.", "isCorrect": False},
                        {"text": "Le beurre fond.", "isCorrect": False}
                    ],
                    "correction": "La **température** et la **consistance** du beurre et de la détrempe doivent être les mêmes."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment appelle-t-on la technique qui consiste à faire chauffer du sucre avec de l'eau sans mélanger, jusqu'à l'obtention d'une couleur ambrée ?",
                    "answerOptions": [
                        {"text": "Sabler.", "isCorrect": False},
                        {"text": "Caraméliser (ou Cuisson au caramel).", "isCorrect": True},
                        {"text": "Blanchir.", "isCorrect": False},
                        {"text": "Crémer.", "isCorrect": False}
                    ],
                    "correction": "La **Caramélisation** peut être réalisée à sec ou au mouillé (avec eau)."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le rôle de la **double cuisson** de la pâte à choux (sur le feu dans la casserole puis au four) ?",
                    "answerOptions": [
                        {"text": "Donner du goût.", "isCorrect": False},
                        {"text": "Assécher l'appareil (gommer) pour retirer l'excès d'humidité et permettre aux choux de gonfler plus fortement au four (plus de vapeur possible).", "isCorrect": True},
                        {"text": "Le faire dorer.", "isCorrect": False},
                        {"text": "Le sucrer.", "isCorrect": False}
                    ],
                    "correction": "Le **gommage** ou 'desséchage' est crucial pour le croustillant final."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le nom de la petite tartelette (souvent aux fruits ou au chocolat) dont le fond est cuit à blanc puis garni après cuisson ?",
                    "answerOptions": [
                        {"text": "Le chou.", "isCorrect": False},
                        {"text": "Le Fond de tarte (ou Tartelette).", "isCorrect": True},
                        {"text": "L'éclair.", "isCorrect": False},
                        {"text": "Le millefeuille.", "isCorrect": False}
                    ],
                    "correction": "La cuisson **à blanc** se fait sans garniture pour garantir le croustillant de la pâte."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment appelle-t-on la technique consistant à monter les blancs d'œufs au batteur tout en y versant un sirop de sucre cuit au 'petit boulé' (118 °C) ?",
                    "answerOptions": [
                        {"text": "Meringue française.", "isCorrect": False},
                        {"text": "Meringue Italienne (la plus stable et la plus onctueuse, utilisée pour les mousses, les crèmes au beurre ou les décors).", "isCorrect": True},
                        {"text": "Meringue suisse.", "isCorrect": False},
                        {"text": "Meringue crémeuse.", "isCorrect": False}
                    ],
                    "correction": "La **Meringue Italienne** est stabilisée par la chaleur du sirop."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le risque de cuire une **Génoise** (ou un biscuit type Roulé) à une température trop basse ?",
                    "answerOptions": [
                        {"text": "Elle brûle.", "isCorrect": False},
                        {"text": "Elle dessèche avant d'avoir pu gonfler et ne dore pas (texture cassante et sèche).", "isCorrect": True},
                        {"text": "Elle lève trop.", "isCorrect": False},
                        {"text": "Elle colle au moule.", "isCorrect": False}
                    ],
                    "correction": "Les **biscuits aériens** nécessitent une cuisson rapide à haute température (souvent 180-200°C)."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le rôle de la **Levure Chimique** dans un gâteau (quatre-quarts, cake) ?",
                    "answerOptions": [
                        {"text": "Donner de la couleur.", "isCorrect": False},
                        {"text": "Produire du gaz carbonique (CO2) uniquement sous l'effet de la chaleur (pas de fermentation) pour faire lever le gâteau rapidement.", "isCorrect": True},
                        {"text": "Réguler le sucre.", "isCorrect": False},
                        {"text": "Hydrater la pâte.", "isCorrect": False}
                    ],
                    "correction": "La **Levure Chimique** est un agent levant instantané."
                },
                {
                    "questionNumber": 77,
                    "question": "Comment appelle-t-on le procédé qui consiste à rouler les bords de la pâte foncée dans le cercle pour créer une bordure de tarte régulière ?",
                    "answerOptions": [
                        {"text": "Bouler.", "isCorrect": False},
                        {"text": "Foncer.", "isCorrect": True},
                        {"text": "Abaisser.", "isCorrect": False},
                        {"text": "Sabler.", "isCorrect": False}
                    ],
                    "correction": "Le **fonçage** est la mise en forme de la pâte dans le moule."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le rôle de la **Détente** (repos de la pâte feuilletée entre chaque tour) ?",
                    "answerOptions": [
                        {"text": "La faire fondre.", "isCorrect": False},
                        {"text": "Relâcher l'élasticité du gluten, ce qui permet d'étaler la pâte sans qu'elle ne se rétracte et évite qu'elle ne déchire au façonnage.", "isCorrect": True},
                        {"text": "La faire lever.", "isCorrect": False},
                        {"text": "La colorer.", "isCorrect": False}
                    ],
                    "correction": "La **Détente** (au frais) est cruciale pour la maniabilité et la régularité du feuilletage."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle est l'opération qui consiste à badigeonner la surface d'une pâte (viennoiserie, brioche) avec un jaune d'œuf ou un mélange œuf/lait avant cuisson ?",
                    "answerOptions": [
                        {"text": "Chemiser.", "isCorrect": False},
                        {"text": "Dorer (ou Dorure).", "isCorrect": True},
                        {"text": "Sabler.", "isCorrect": False},
                        {"text": "Imbiber.", "isCorrect": False}
                    ],
                    "correction": "La **dorure** permet d'obtenir une belle couleur brillante en surface (réaction de Maillard)."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le risque de travailler la **Pâte à Choux** trop chaude ou trop froide lors de l'incorporation des œufs ?",
                    "answerOptions": [
                        {"text": "La pâte se rétracte.", "isCorrect": False},
                        {"text": "Trop chaude : les œufs cuisent (omelette) ; Trop froide : les œufs ne s'incorporent pas correctement (choux dense ou irrégulier).", "isCorrect": True},
                        {"text": "La pâte fond.", "isCorrect": False},
                        {"text": "La pâte est trop sèche.", "isCorrect": False}
                    ],
                    "correction": "La **température** est à maîtriser lors de l'ajout des œufs."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : PRODUITS FINIS, CONSERVATION ET CUISSONS (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Produits Finis, Conservation et Cuissons (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'entremets classique composé d'un disque de meringue, de crème chantilly et de fruits rouges ?",
                    "answerOptions": [
                        {"text": "Le Fraisier.", "isCorrect": False},
                        {"text": "Le Pavlova (ou Vacherin aux fruits rouges).", "isCorrect": True},
                        {"text": "L'Opéra.", "isCorrect": False},
                        {"text": "Le Paris-Brest.", "isCorrect": False}
                    ],
                    "correction": "Le **Pavlova** est léger et aérien (base meringue)."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la principale différence entre la **Pâte à Brioche** et la **Pâte à Pain** ?",
                    "answerOptions": [
                        {"text": "Le temps de repos.", "isCorrect": False},
                        {"text": "La Brioche est enrichie en œufs et en beurre (matière grasse), ce qui la rend plus riche, plus moelleuse et plus jaune (texture non alvéolée).", "isCorrect": True},
                        {"text": "La brioche contient plus de sel.", "isCorrect": False},
                        {"text": "La brioche ne contient pas de levure.", "isCorrect": False}
                    ],
                    "correction": "La **Brioche** est une pâte levée riche (levure + œuf/beurre)."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est l'entremets composé d'une superposition de biscuit Joconde, de crème au beurre café et de ganache chocolat ?",
                    "answerOptions": [
                        {"text": "Le Saint-Honoré.", "isCorrect": False},
                        {"text": "L'Opéra.", "isCorrect": True},
                        {"text": "Le Forêt Noire.", "isCorrect": False},
                        {"text": "Le Bavarois.", "isCorrect": False}
                    ],
                    "correction": "L'**Opéra** est un classique nécessitant une grande précision de montage."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le risque de congeler un produit (ex : tarte) à la crème pâtissière simple (non stabilisée) ?",
                    "answerOptions": [
                        {"text": "La crème devient trop ferme.", "isCorrect": False},
                        {"text": "L'eau contenue dans la crème cristallise, puis le produit 'tranche' (devient grumeleux et aqueux) à la décongélation (il faut la stabiliser à la gélatine ou au beurre).", "isCorrect": True},
                        {"text": "La couleur change.", "isCorrect": False},
                        {"text": "La crème brûle.", "isCorrect": False}
                    ],
                    "correction": "Pour la **surgélation**, les crèmes doivent être adaptées (crème pâtissière/beurre/gélatine ou mousses)."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment s'appelle l'outil utilisé pour mesurer la densité d'un sirop ou d'une confiture, permettant d'en connaître le taux de sucre et le degré de cuisson (ex : petit boulé, grand cassé) ?",
                    "answerOptions": [
                        {"text": "Le thermomètre.", "isCorrect": False},
                        {"text": "Le Pèse-sirop (ou Aréomètre ou Densimètre).", "isCorrect": True},
                        {"text": "Le réfractomètre.", "isCorrect": False},
                        {"text": "La balance de précision.", "isCorrect": False}
                    ],
                    "correction": "Le **Pèse-sirop** permet de mesurer la concentration en sucre (ex : en degrés Baumé)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le nom de la préparation utilisée pour le garnissage des éclairs et des religieuses (souvent parfumée au café ou au chocolat) ?",
                    "answerOptions": [
                        {"text": "Crème au beurre.", "isCorrect": False},
                        {"text": "Crème Pâtissière (éventuellement améliorée avec du beurre pour une meilleure tenue).", "isCorrect": True},
                        {"text": "Mousse.", "isCorrect": False},
                        {"text": "Ganache.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Pâtissière** est le garnissage standard de la pâte à choux."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est le risque de ne pas respecter la phase de **détrempe** (ou repos au frais) sur une pâte à foncer (pâte brisée, pâte sablée) ?",
                    "answerOptions": [
                        {"text": "Elle cuit plus vite.", "isCorrect": False},
                        {"text": "Elle se rétracte énormément à la cuisson (car le gluten n'est pas relâché) et le bord de la tarte s'effondre.", "isCorrect": True},
                        {"text": "Elle devient trop molle.", "isCorrect": False},
                        {"text": "Elle ne dore pas.", "isCorrect": False}
                    ],
                    "correction": "Le **repos au frais** est essentiel pour toutes les pâtes et entremets."
                },
                {
                    "questionNumber": 88,
                    "question": "Comment appelle-t-on le procédé par lequel on recouvre une tartelette de confiture ou de nappage pour la rendre brillante et la protéger de l'air ?",
                    "answerOptions": [
                        {"text": "Dorer.", "isCorrect": False},
                        {"text": "Napper (ou Glaçage à l'abricot/Nappage neutre).", "isCorrect": True},
                        {"text": "Blanchir.", "isCorrect": False},
                        {"text": "Crémer.", "isCorrect": False}
                    ],
                    "correction": "Le **Nappage** (souvent à base d'abricot) est un classique de finition."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est l'entremets classique constitué d'une couronne de pâte à choux, garni de crème mousseline pralinée et saupoudré d'amandes effilées ?",
                    "answerOptions": [
                        {"text": "Le Saint-Honoré.", "isCorrect": False},
                        {"text": "Le Paris-Brest.", "isCorrect": True},
                        {"text": "L'Opéra.", "isCorrect": False},
                        {"text": "Le Forêt Noire.", "isCorrect": False}
                    ],
                    "correction": "Le **Paris-Brest** est un chou emblématique."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est la principale caractéristique d'un **biscuit à la cuillère** (par rapport à une génoise) ?",
                    "answerOptions": [
                        {"text": "Il est plus lourd.", "isCorrect": False},
                        {"text": "Il est monté par séparation (jaunes/sucre, puis blancs fermes) et ne contient pas de matière grasse ajoutée, ce qui lui donne un aspect rugueux et une grande légèreté.", "isCorrect": True},
                        {"text": "Il est cuit à la vapeur.", "isCorrect": False},
                        {"text": "Il est très dense.", "isCorrect": False}
                    ],
                    "correction": "Le **Biscuit à la cuillère** est la base du Tiramisu ou de la Charlotte."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle est la méthode de conservation consistant à abaisser la température d'un produit en dessous de -18 °C ?",
                    "answerOptions": [
                        {"text": "La réfrigération.", "isCorrect": False},
                        {"text": "La Surgélation (ou Congélation pour usage domestique).", "isCorrect": True},
                        {"text": "La pasteurisation.", "isCorrect": False},
                        {"text": "La stérilisation.", "isCorrect": False}
                    ],
                    "correction": "La **Surgélation** permet une très longue conservation (souvent 12 mois) en bloquant l'activité bactérienne."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le risque de mal doser l'**émulsion** dans la fabrication d'une ganache (trop de crème par rapport au chocolat) ?",
                    "answerOptions": [
                        {"text": "La ganache sera trop dure.", "isCorrect": False},
                        {"text": "La ganache sera trop liquide, ne tiendra pas son montage ou son glaçage (rupture de la structure).", "isCorrect": True},
                        {"text": "La ganache sera trop sèche.", "isCorrect": False},
                        {"text": "La ganache sera trop grasse.", "isCorrect": False}
                    ],
                    "correction": "Le ratio **crème/chocolat** est essentiel pour la consistance souhaitée."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le nom de la technique de cuisson d'une tarte ou d'une pièce garnie où l'on utilise un cercle rempli de billes de cuisson ou de haricots secs pour maintenir la forme ?",
                    "answerOptions": [
                        {"text": "Cuisson à sec.", "isCorrect": False},
                        {"text": "Cuisson à blanc (avec lestage).", "isCorrect": True},
                        {"text": "Cuisson au bain-marie.", "isCorrect": False},
                        {"text": "Cuisson en différé.", "isCorrect": False}
                    ],
                    "correction": "La **Cuisson à blanc** est souvent lestée pour éviter que la pâte ne boursoufle."
                },
                {
                    "questionNumber": 94,
                    "question": "Qu'est-ce qu'une **Crème Chiboust** (utilisée pour le Saint-Honoré) ?",
                    "answerOptions": [
                        {"text": "Une crème au beurre pralinée.", "isCorrect": False},
                        {"text": "Une crème pâtissière allégée par de la meringue italienne (stable et légère).", "isCorrect": True},
                        {"text": "Une crème fouettée au mascarpone.", "isCorrect": False},
                        {"text": "Une crème anglaise épaisse.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Chiboust** est le mélange signature du Saint-Honoré."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le rôle du **Praliné** dans la pâtisserie ?",
                    "answerOptions": [
                        {"text": "Émulsifier.", "isCorrect": False},
                        {"text": "Apporter du croustillant (éclats), du gras (pâte d'oléagineux) et une saveur de fruits secs torréfiés (noisette/amande) et caramélisés.", "isCorrect": True},
                        {"text": "Colorer.", "isCorrect": False},
                        {"text": "Gélifier.", "isCorrect": False}
                    ],
                    "correction": "Le **Praliné** est indispensable pour le Paris-Brest, le Rocher ou l'Opéra."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est l'entremets composé de biscuits cuillère imbibés d'un mélange café/alcool, de mascarpone et de cacao ?",
                    "answerOptions": [
                        {"text": "Le Bavarois.", "isCorrect": False},
                        {"text": "Le Tiramisu.", "isCorrect": True},
                        {"text": "Le Moka.", "isCorrect": False},
                        {"text": "Le Fraisier.", "isCorrect": False}
                    ],
                    "correction": "Le **Tiramisu** est un dessert italien à base d'œufs et de mascarpone."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque de dorer une viennoiserie **trop tôt** (avant la pousse) ?",
                    "answerOptions": [
                        {"text": "Elle brûle.", "isCorrect": False},
                        {"text": "La dorure forme une pellicule rigide qui empêche le développement et la pousse (la viennoiserie ne lève pas).", "isCorrect": True},
                        {"text": "Elle devient trop molle.", "isCorrect": False},
                        {"text": "Elle ne dore pas.", "isCorrect": False}
                    ],
                    "correction": "La **dorure** doit être appliquée juste avant l'enfournement, délicatement, pour ne pas 'casser' la pâte levée."
                },
                {
                    "questionNumber": 98,
                    "question": "Comment appelle-t-on la technique de finition d'un entremets qui consiste à projeter du chocolat fondu (au pistolet) sur le produit congelé pour obtenir un aspect 'velours' ?",
                    "answerOptions": [
                        {"text": "Le glacage miroir.", "isCorrect": False},
                        {"text": "Le Flocage (ou Glaçage velours).", "isCorrect": True},
                        {"text": "L'enrobage.", "isCorrect": False},
                        {"text": "Le tempérage.", "isCorrect": False}
                    ],
                    "correction": "Le **Flocage** (chocolat + beurre de cacao) est réalisé sur produit congelé."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le risque d'ouvrir la porte du four pendant la cuisson d'une **pâte à choux** ou d'une **génoise** ?",
                    "answerOptions": [
                        {"text": "Elles gonflent trop.", "isCorrect": False},
                        {"text": "La chute de température (entrée d'air froid) entraîne un affaissement immédiat et irréversible du produit (qui 'retombe').", "isCorrect": True},
                        {"text": "Elles brûlent.", "isCorrect": False},
                        {"text": "Elles deviennent dures.", "isCorrect": False}
                    ],
                    "correction": "Il ne faut jamais ouvrir le four en début de cuisson des **pâtes à fort développement**."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le produit classique composé de deux fonds de Dacquoise (amande/noisette) et d'une crème au beurre pralinée ?",
                    "answerOptions": [
                        {"text": "Le Moka.", "isCorrect": False},
                        {"text": "Le Succès Praliné.", "isCorrect": True},
                        {"text": "La Bûche.", "isCorrect": False},
                        {"text": "Le Fraisier.", "isCorrect": False}
                    ],
                    "correction": "Le **Succès** est un biscuit à base de poudre d'amande/noisette (Dacquoise)."
                },
            ]
        }
    }
}