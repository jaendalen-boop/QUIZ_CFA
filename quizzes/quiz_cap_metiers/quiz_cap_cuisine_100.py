quiz_data = {
    "title": "Quiz CAP Cuisine : Hygiène, Technologie, Techniques et Produits (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE, SÉCURITÉ ET MICROBIOLOGIE (HACCP) (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : HYGIÈNE, SÉCURITÉ ET MICROBIOLOGIE (HACCP)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la température maximale légale de conservation des préparations froides lors du service ?",
                    "answerOptions": [
                        {"text": "3 degrés Celsius", "isCorrect": True},
                        {"text": "10 degrés Celsius", "isCorrect": False},
                        {"text": "63 degrés Celsius", "isCorrect": False},
                        {"text": "20 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "La chaîne du froid impose une température à cœur comprise entre 0 et +3°C pour les produits périssables ou transformés. Au-delà, le développement microbien reprend."
                },
                {
                    "questionNumber": 2,
                    "question": "Que signifie l'acronyme HACCP ?",
                    "answerOptions": [
                        {"text": "Hazard Analysis Critical Control Point", "isCorrect": True},
                        {"text": "Haute Autorité de Contrôle Culinaire Professionnel", "isCorrect": False},
                        {"text": "Hazard Association for Cooking Control Process", "isCorrect": False},
                        {"text": "Hygiène Alimentaire et Contrôle Critique des Procédures", "isCorrect": False}
                    ],
                    "correction": "HACCP signifie 'Hazard Analysis Critical Control Point', traduit par Analyse des Dangers et Points Critiques pour leur Maîtrise. C'est une méthode préventive obligatoire."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la température minimale réglementaire pour une liaison chaude ?",
                    "answerOptions": [
                        {"text": "63 degrés", "isCorrect": True},
                        {"text": "55 degrés", "isCorrect": False},
                        {"text": "45 degrés", "isCorrect": False},
                        {"text": "37 degrés", "isCorrect": False}
                    ],
                    "correction": "Pour éviter la prolifération bactérienne, les plats chauds doivent être maintenus à une température strictement supérieure ou égale à +63°C à cœur jusqu'au service."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle bactérie est principalement associée à la manipulation des œufs crus ou des volailles mal cuites ?",
                    "answerOptions": [
                        {"text": "Salmonelle", "isCorrect": True},
                        {"text": "Listéria", "isCorrect": False},
                        {"text": "Staphylocoque doré", "isCorrect": False},
                        {"text": "Clostridium perfringens", "isCorrect": False}
                    ],
                    "correction": "Les salmonelles se trouvent naturellement dans le tube digestif des volailles. La cuisson complète (supérieure à 63°C) ou l'utilisation d'œufs pasteurisés permet d'éliminer ce risque."
                },
                {
                    "questionNumber": 5,
                    "question": "Dans une enceinte réfrigérée, où doit-on stocker les produits finis ou cuits par rapport aux produits crus ?",
                    "answerOptions": [
                        {"text": "Au dessus", "isCorrect": True},
                        {"text": "En dessous", "isCorrect": False},
                        {"text": "Au même niveau", "isCorrect": False},
                        {"text": "Sur le sol", "isCorrect": False}
                    ],
                    "correction": "Les produits cuits doivent être placés au-dessus des produits crus pour éviter qu'ils ne soient contaminés par des exsudats ou de la terre tombant des produits bruts."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le délai maximum autorisé pour refroidir un plat cuisiné de +63°C à +10°C ?",
                    "answerOptions": [
                        {"text": "2 heures", "isCorrect": True},
                        {"text": "4 heures", "isCorrect": False},
                        {"text": "6 heures", "isCorrect": False},
                        {"text": "12 heures", "isCorrect": False}
                    ],
                    "correction": "Le refroidissement rapide est critique. Il doit s'effectuer en moins de 2 heures à l'aide d'une cellule de refroidissement pour traverser rapidement la zone de danger microbiologique."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est la durée légale de conservation des plats témoins en restauration collective ?",
                    "answerOptions": [
                        {"text": "5 jours", "isCorrect": True},
                        {"text": "24 heures", "isCorrect": False},
                        {"text": "3 jours", "isCorrect": False},
                        {"text": "1 semaine", "isCorrect": False}
                    ],
                    "correction": "Les plats témoins doivent être conservés au froid positif (+3°C) pendant 5 jours minimum après la consommation, pour permettre des analyses en cas de TIAC."
                },
                {
                    "questionNumber": 8,
                    "question": "Comment appelle-t-on la flore microbienne présente naturellement sur la peau et les muqueuses du cuisinier ?",
                    "answerOptions": [
                        {"text": "Flore résidente", "isCorrect": True},
                        {"text": "Flore transitoire", "isCorrect": False},
                        {"text": "Flore pathogène", "isCorrect": False},
                        {"text": "Flore d'altération", "isCorrect": False}
                    ],
                    "correction": "La flore résidente (ou commensale) vit sur l'hôte sain. Elle se distingue de la flore transitoire, issue des contaminations extérieures, qui s'élimine par le lavage des mains."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel document regroupe l'ensemble des procédures d'hygiène et de sécurité d'un établissement ?",
                    "answerOptions": [
                        {"text": "Le PMS", "isCorrect": True},
                        {"text": "Le Kbis", "isCorrect": False},
                        {"text": "Le DUER", "isCorrect": False},
                        {"text": "La fiche technique", "isCorrect": False}
                    ],
                    "correction": "Le Plan de Maîtrise Sanitaire (PMS) est le document obligatoire décrivant les mesures prises pour assurer l'hygiène (HACCP, traçabilité, bonnes pratiques)."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle action mécanique est indispensable lors du nettoyage d'une surface pour décoller les souillures ?",
                    "answerOptions": [
                        {"text": "Frotter", "isCorrect": True},
                        {"text": "Rincer", "isCorrect": False},
                        {"text": "Sécher", "isCorrect": False},
                        {"text": "Désinfecter", "isCorrect": False}
                    ],
                    "correction": "Le TACT (Température, Action mécanique, Chimie, Temps) définit le nettoyage. L'action mécanique (frotter) est indispensable pour déstructurer le biofilm avant la désinfection."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel produit utilise-t-on obligatoirement pour la décontamination des légumes bruts ?",
                    "answerOptions": [
                        {"text": "Eau javellisée", "isCorrect": True},
                        {"text": "Vinaigre blanc", "isCorrect": False},
                        {"text": "Liquide vaisselle", "isCorrect": False},
                        {"text": "Eau bouillante", "isCorrect": False}
                    ],
                    "correction": "Les légumes terreux doivent être décontaminés avec des pastilles de chlore ou de l'eau javellisée dosée, suivis d'un rinçage abondant à l'eau claire."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la principale source de contamination par le Staphylocoque doré ?",
                    "answerOptions": [
                        {"text": "Le manipulateur", "isCorrect": True},
                        {"text": "Les légumes terreux", "isCorrect": False},
                        {"text": "Les conserves bombées", "isCorrect": False},
                        {"text": "L'eau du réseau", "isCorrect": False}
                    ],
                    "correction": "Le Staphylocoque doré est une bactérie portée par l'homme (nez, bouche, plaies infectées). La contamination est manuportée, d'où l'importance du port du masque en cas de rhume et des gants sur plaies."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel terme désigne le cheminement des produits empêchant le croisement entre le propre et le sale ?",
                    "answerOptions": [
                        {"text": "La marche en avant", "isCorrect": True},
                        {"text": "La méthode FIFO", "isCorrect": False},
                        {"text": "Le plan de nettoyage", "isCorrect": False},
                        {"text": "La traçabilité descendante", "isCorrect": False}
                    ],
                    "correction": "La marche en avant (dans l'espace ou dans le temps) garantit qu'un produit sain ne croise jamais un circuit souillé (déchets, vaisselle sale) pour éviter les contaminations croisées."
                },
                {
                    "questionNumber": 14,
                    "question": "Que doit-on vérifier obligatoirement à la réception des marchandises réfrigérées ?",
                    "answerOptions": [
                        {"text": "Température à cœur", "isCorrect": True},
                        {"text": "Prix des produits", "isCorrect": False},
                        {"text": "Marque du fournisseur", "isCorrect": False},
                        {"text": "Poids des palettes", "isCorrect": False}
                    ],
                    "correction": "Le contrôle de la température à cœur (ou entre deux conditionnements) est impératif à la réception pour valider que la chaîne du froid n'a pas été rompue durant le transport."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle est la définition exacte de la désinfection ?",
                    "answerOptions": [
                        {"text": "Élimination des micro-organismes", "isCorrect": True},
                        {"text": "Élimination des souillures visibles", "isCorrect": False},
                        {"text": "Élimination des déchets d'emballage", "isCorrect": False},
                        {"text": "Élimination des mauvaises odeurs", "isCorrect": False}
                    ],
                    "correction": "Le nettoyage enlève la saleté visible. La désinfection, qui vient après, a pour but de tuer ou d'inactiver momentanément les micro-organismes indésirables sur une surface propre."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le seul bijou toléré en cuisine selon les bonnes pratiques d'hygiène ?",
                    "answerOptions": [
                        {"text": "Alliance lisse", "isCorrect": True},
                        {"text": "Montre étanche", "isCorrect": False},
                        {"text": "Boucles d'oreilles", "isCorrect": False},
                        {"text": "Bracelet en cuivre", "isCorrect": False}
                    ],
                    "correction": "Seule l'alliance lisse est tolérée car elle présente peu d'aspérités retenant les bactéries. Tout autre bijou (montres, bagues avec pierres) est interdit."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle méthode de décongélation est strictement interdite en cuisine professionnelle ?",
                    "answerOptions": [
                        {"text": "À température ambiante", "isCorrect": True},
                        {"text": "En enceinte réfrigérée", "isCorrect": False},
                        {"text": "Au four micro-ondes", "isCorrect": False},
                        {"text": "Par cuisson directe", "isCorrect": False}
                    ],
                    "correction": "La décongélation à température ambiante favorise une prolifération microbienne explosive. On doit décongeler au froid (+3°C), au micro-ondes (si cuisson immédiate) ou par cuisson directe."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle huile d'origine animale est impropre à la friture profonde en raison de son point de fumée bas ?",
                    "answerOptions": [
                        {"text": "Beurre", "isCorrect": True},
                        {"text": "Graisse de bœuf", "isCorrect": False},
                        {"text": "Saindoux", "isCorrect": False},
                        {"text": "Graisse de canard", "isCorrect": False}
                    ],
                    "correction": "Le beurre non clarifié brûle à environ 130°C (caséine). Il ne supporte pas les températures de friture (170°C-180°C). Les graisses comme le blanc de bœuf sont adaptées."
                },
                {
                    "questionNumber": 19,
                    "question": "Que doit-on faire immédiatement après avoir cassé des œufs coquille pour une préparation ?",
                    "answerOptions": [
                        {"text": "Se laver les mains", "isCorrect": True},
                        {"text": "Mettre au frigo", "isCorrect": False},
                        {"text": "Battre les œufs", "isCorrect": False},
                        {"text": "Ajouter le sucre", "isCorrect": False}
                    ],
                    "correction": "La coquille de l'œuf peut être porteuse de salmonelles. Il faut impérativement se laver les mains après le cassage pour ne pas contaminer l'appareil ou le matériel."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel parasite peut-on retrouver dans les poissons sauvages consommés crus nécessitant une congélation préalable ?",
                    "answerOptions": [
                        {"text": "Anisakis", "isCorrect": True},
                        {"text": "Ténia", "isCorrect": False},
                        {"text": "Ascaris", "isCorrect": False},
                        {"text": "Douve", "isCorrect": False}
                    ],
                    "correction": "L'Anisakis est un parasite fréquent chez les poissons sauvages. La réglementation impose une congélation à -20°C pendant 24h pour les poissons servis crus afin de tuer ce parasite."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNOLOGIE DU MATÉRIEL ET DES LOCAUX (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNOLOGIE DU MATÉRIEL ET DES LOCAUX (Questions 21 à 40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel ustensile de cuisson cylindrique à parois verticales et deux poignées latérales utilise-t-on pour rissoler ou sauter des aliments ?",
                    "answerOptions": [
                        {"text": "Le sautoir", "isCorrect": True},
                        {"text": "La sauteuse", "isCorrect": False},
                        {"text": "La poêle lyonnaise", "isCorrect": False},
                        {"text": "Le wok asiatique", "isCorrect": False}
                    ],
                    "correction": "Le sautoir a des bords droits (verticaux) et sert à sauter les aliments. La sauteuse, elle, a des bords évasés (inclinés). C'est une distinction fondamentale au CAP."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel petit matériel souple, généralement en caoutchouc ou silicone avec un manche, sert à racler parfaitement l'intérieur d'un récipient ?",
                    "answerOptions": [
                        {"text": "La maryse", "isCorrect": True},
                        {"text": "La corne", "isCorrect": False},
                        {"text": "Le pinceau", "isCorrect": False},
                        {"text": "La spatule en bois", "isCorrect": False}
                    ],
                    "correction": "La maryse (ou spatule souple) permet de 'corner' (nettoyer) les culs-de-poule sans perte. La corne, elle, est une pièce de plastique rigide sans manche, utilisée pour manipuler les pâtes."
                },
                {
                    "questionNumber": 23,
                    "question": "À quoi sert principalement une salamandre en cuisine professionnelle ?",
                    "answerOptions": [
                        {"text": "Gratiner", "isCorrect": True},
                        {"text": "Bouillir", "isCorrect": False},
                        {"text": "Frire", "isCorrect": False},
                        {"text": "Émulsionner", "isCorrect": False}
                    ],
                    "correction": "La salamandre est un appareil de cuisson par rayonnement (voûte chauffante) servant à gratiner (colorer le dessus d'un plat), glacer ou maintenir au chaud une assiette avant l'envoi."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel type de four permet de combiner la chaleur sèche et la vapeur pour limiter le dessèchement des produits ?",
                    "answerOptions": [
                        {"text": "Four mixte", "isCorrect": True},
                        {"text": "Four à convection", "isCorrect": False},
                        {"text": "Four à sole", "isCorrect": False},
                        {"text": "Four à micro-ondes", "isCorrect": False}
                    ],
                    "correction": "Le four mixte combine l'air pulsé (chaleur sèche) et l'injection de vapeur. Cela permet des cuissons plus rapides et moins desséchantes que la convection classique."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le rôle exact du fusil lors de l'entretien d'un couteau ?",
                    "answerOptions": [
                        {"text": "Redresser le fil", "isCorrect": True},
                        {"text": "Créer un nouveau tranchant en enlevant beaucoup de matière métallique", "isCorrect": False},
                        {"text": "Polir le manche du couteau pour une meilleure hygiène", "isCorrect": False},
                        {"text": "Désinfecter la lame", "isCorrect": False}
                    ],
                    "correction": "Le fusil sert à l'affilage : il redresse le 'fil' (le bord fin) de la lame qui se tord à l'usage. Pour aiguiser (créer le tranchant) quand le couteau ne coupe plus, on utilise une pierre à aiguiser."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la particularité physique d'une sauteuse par rapport à un sautoir ?",
                    "answerOptions": [
                        {"text": "Bords évasés", "isCorrect": True},
                        {"text": "Bords droits", "isCorrect": False},
                        {"text": "Fond bombé", "isCorrect": False},
                        {"text": "Absence de queue", "isCorrect": False}
                    ],
                    "correction": "La sauteuse possède des bords évasés (inclinés vers l'extérieur), ce qui facilite l'évaporation et permet de monter des sauces plus aisément qu'avec un sautoir aux bords droits."
                },
                {
                    "questionNumber": 27,
                    "question": "Comment appelle-t-on la passoire conique à grille très fine utilisée pour filtrer les sauces et les fonds sans laisser passer de particules ?",
                    "answerOptions": [
                        {"text": "Chinois étamine", "isCorrect": True},
                        {"text": "Chinois piston", "isCorrect": False},
                        {"text": "Passoire à queue", "isCorrect": False},
                        {"text": "Panier de friteuse", "isCorrect": False}
                    ],
                    "correction": "Le chinois étamine possède une grille métallique très fine (comme un tissu). Le chinois classique (perforé) laisse passer plus de matière. On 'passe au chinois étamine' pour une finition parfaite."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la fonction d'une araignée en cuisine ?",
                    "answerOptions": [
                        {"text": "Retirer des aliments d'un liquide chaud", "isCorrect": True},
                        {"text": "Écraser les légumes pour la purée", "isCorrect": False},
                        {"text": "Fouetter les blancs en neige", "isCorrect": False},
                        {"text": "Ouvrir les boîtes de conserve", "isCorrect": False}
                    ],
                    "correction": "L'araignée est une écumoire à fils de fer espacés (ressemblant à une toile). Elle sert à sortir les aliments de la friture ou de l'eau bouillante en les égouttant instantanément."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel couteau de petite taille (lame 7-10 cm) est utilisé pour éplucher et tourner les légumes ?",
                    "answerOptions": [
                        {"text": "L'office", "isCorrect": True},
                        {"text": "L'éminceur", "isCorrect": False},
                        {"text": "Le filet de sole", "isCorrect": False},
                        {"text": "Le désosseur", "isCorrect": False}
                    ],
                    "correction": "Le couteau d'office est le prolongement de la main du cuisinier pour les travaux de précision : éplucher, tourner, équeuter. L'éminceur est le grand couteau 'chef'."
                },
                {
                    "questionNumber": 30,
                    "question": "Que désigne le terme 'Gastronorme' (GN) ?",
                    "answerOptions": [
                        {"text": "Une norme dimensionnelle standardisée", "isCorrect": True},
                        {"text": "Une marque de four professionnel", "isCorrect": False},
                        {"text": "Un label de qualité alimentaire", "isCorrect": False},
                        {"text": "Une technique de cuisson sous vide", "isCorrect": False}
                    ],
                    "correction": "Le format Gastronorme (GN 1/1, GN 1/2, etc.) standardise les dimensions des bacs, grilles et échelles pour qu'ils soient compatibles avec tous les matériels (fours, chariots, frigos)."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel matériau est indispensable pour utiliser une batterie de cuisine sur une plaque à induction ?",
                    "answerOptions": [
                        {"text": "Métal ferromagnétique", "isCorrect": True},
                        {"text": "Cuivre pur", "isCorrect": False},
                        {"text": "Aluminium pur", "isCorrect": False},
                        {"text": "Verre trempé", "isCorrect": False}
                    ],
                    "correction": "L'induction fonctionne par champ magnétique. Le récipient doit contenir du fer (fonte, acier émaillé, inox ferritique) pour chauffer. Le cuivre ou l'alu seuls ne fonctionnent pas."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel appareil permet de maintenir les préparations à température de service (+63°C) sans poursuivre la cuisson ?",
                    "answerOptions": [
                        {"text": "Le bain-marie", "isCorrect": True},
                        {"text": "La cellule de refroidissement", "isCorrect": False},
                        {"text": "Le cutter", "isCorrect": False},
                        {"text": "La sauteuse basculante", "isCorrect": False}
                    ],
                    "correction": "Le bain-marie (électrique ou à eau) est conçu pour le maintien en température. Il chauffe doucement sans agresser le produit, contrairement à une plaque de cuisson directe."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le nom du récipient hémisphérique utilisé pour fouetter les appareils ou monter les blancs, facilitant le mouvement du fouet ?",
                    "answerOptions": [
                        {"text": "Cul-de-poule", "isCorrect": True},
                        {"text": "Calotte", "isCorrect": False},
                        {"text": "Bassine à confiture", "isCorrect": False},
                        {"text": "Gastronorme", "isCorrect": False}
                    ],
                    "correction": "Le cul-de-poule a un fond rond (sphérique), idéal pour que le fouet atteigne toute la préparation. La calotte a un fond plat."
                },
                {
                    "questionNumber": 34,
                    "question": "Sur un fourneau, qu'appelle-t-on le 'coup de feu' ?",
                    "answerOptions": [
                        {"text": "La plaque centrale à chaleur dégressive", "isCorrect": True},
                        {"text": "Le moment où le service est intense", "isCorrect": False},
                        {"text": "L'allumage automatique du four", "isCorrect": False},
                        {"text": "La hotte aspirante", "isCorrect": False}
                    ],
                    "correction": "Techniquement, la 'plaque coup de feu' est une plaque en fonte massive chauffée par un brûleur central puissant. La chaleur diminue à mesure qu'on s'éloigne du centre, permettant de gérer plusieurs cuissons en déplaçant les casseroles."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel instrument de mesure utilise-t-on pour vérifier la densité d'un sirop de sucre ?",
                    "answerOptions": [
                        {"text": "Le pèse-sirop", "isCorrect": True},
                        {"text": "Le thermomètre sonde", "isCorrect": False},
                        {"text": "Le chronomètre", "isCorrect": False},
                        {"text": "Le verre doseur", "isCorrect": False}
                    ],
                    "correction": "Bien que le thermomètre soit souvent utilisé pour la cuisson du sucre, le pèse-sirop (densimètre) mesure spécifiquement la densité (concentration en sucre) d'un sirop froid ou tiède."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est l'utilité principale d'une mandoline ?",
                    "answerOptions": [
                        {"text": "Tailler des tranches régulières", "isCorrect": True},
                        {"text": "Aiguiser les couteaux rapidement", "isCorrect": False},
                        {"text": "Hacher la viande finement", "isCorrect": False},
                        {"text": "Éplucher les pommes de terre", "isCorrect": False}
                    ],
                    "correction": "La mandoline est un coupe-légumes manuel qui assure une épaisseur de tranche parfaitement constante et permet des tailles spécifiques (gaufrettes, juliennes fines)."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel nom donne-t-on à la grande casserole haute, munie d'une queue, utilisée pour cuire de grandes quantités de liquides ou potages ?",
                    "answerOptions": [
                        {"text": "La russe", "isCorrect": True},
                        {"text": "Le rondeau", "isCorrect": False},
                        {"text": "La braisière", "isCorrect": False},
                        {"text": "La plaque à rôtir", "isCorrect": False}
                    ],
                    "correction": "La russe est la casserole 'classique' de cuisine professionnelle : cylindrique, haute, avec une queue. Le rondeau est bas avec deux poignées."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel matériel est spécifiquement conçu pour abaisser très rapidement la température des plats de +63°C à +10°C ?",
                    "answerOptions": [
                        {"text": "La cellule de refroidissement", "isCorrect": True},
                        {"text": "Le congélateur coffre", "isCorrect": False},
                        {"text": "La chambre froide positive", "isCorrect": False},
                        {"text": "L'armoire à boissons", "isCorrect": False}
                    ],
                    "correction": "Seule la cellule de refroidissement est assez puissante pour respecter le délai légal (moins de 2h). Un frigo classique ou un congélateur ne sont pas conçus pour refroidir du chaud massivement."
                },
                {
                    "questionNumber": 39,
                    "question": "Pour quelle tâche utilise-t-on un couteau 'filet de sole' ?",
                    "answerOptions": [
                        {"text": "Lever les filets de poisson", "isCorrect": True},
                        {"text": "Désosser une épaule d'agneau", "isCorrect": False},
                        {"text": "Couper du pain", "isCorrect": False},
                        {"text": "Émincer des oignons", "isCorrect": False}
                    ],
                    "correction": "Le filet de sole possède une lame longue, fine et flexible, permettant de glisser le long de l'arête centrale du poisson plat pour détacher le filet sans perte de chair."
                },
                {
                    "questionNumber": 40,
                    "question": "En technologie des locaux, à quoi sert le siphon de sol ?",
                    "answerOptions": [
                        {"text": "Évacuer les eaux de lavage", "isCorrect": True},
                        {"text": "Ventiler la pièce", "isCorrect": False},
                        {"text": "Distribuer le gaz", "isCorrect": False},
                        {"text": "Filtrer l'eau du robinet", "isCorrect": False}
                    ],
                    "correction": "Les siphons de sol (avec panier et cloche) permettent d'évacuer les eaux lors du nettoyage à grande eau des sols carrelés, tout en empêchant les remontées d'odeurs des égouts."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : CONNAISSANCE DES PRODUITS (LES DENRÉES) (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : CONNAISSANCE DES PRODUITS (LES DENRÉES) (Questions 41 à 60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "À quelle famille de légumes appartient le haricot vert ?",
                    "answerOptions": [
                        {"text": "Légumes graines", "isCorrect": True},
                        {"text": "Légumes racines", "isCorrect": False},
                        {"text": "Légumes feuilles", "isCorrect": False},
                        {"text": "Légumes tubercules", "isCorrect": False}
                    ],
                    "correction": "Bien que mangé frais, le haricot vert est botaniquement un légume graine (légumineuse), dont on consomme la gousse avant maturité complète des graines."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle variété de pomme de terre à chair farineuse est idéale pour réaliser une purée ou des frites ?",
                    "answerOptions": [
                        {"text": "Bintje", "isCorrect": True},
                        {"text": "Charlotte", "isCorrect": False},
                        {"text": "Belle de Fontenay", "isCorrect": False},
                        {"text": "Roseval", "isCorrect": False}
                    ],
                    "correction": "La Bintje (ou l'Agria) a une chair farineuse qui se délite à la cuisson, parfaite pour les potages, purées et frites. Les autres citées sont à chair ferme (vapeur, sautées)."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel morceau du bœuf est classé en première catégorie et destiné aux cuissons rapides comme le rôtissage ?",
                    "answerOptions": [
                        {"text": "Le rumsteak", "isCorrect": True},
                        {"text": "Le paleron", "isCorrect": False},
                        {"text": "Le jumeau", "isCorrect": False},
                        {"text": "Le collier", "isCorrect": False}
                    ],
                    "correction": "Les morceaux de 1ère catégorie (aloyau, cuisse) sont des muscles pauvres en collagène. Ils sont tendres et destinés aux cuissons rapides (griller, rôtir, sauter), contrairement aux morceaux de 2ème ou 3ème catégorie qui nécessitent des cuissons longues (braiser, bouillir)."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la teneur minimale en matière grasse du beurre standard ?",
                    "answerOptions": [
                        {"text": "82 pour cent", "isCorrect": True},
                        {"text": "40 pour cent", "isCorrect": False},
                        {"text": "60 pour cent", "isCorrect": False},
                        {"text": "99 pour cent", "isCorrect": False}
                    ],
                    "correction": "L'appellation 'beurre' est réservée à un produit contenant au minimum 82% de matière grasse butyrique (80% pour le beurre demi-sel). En dessous, ce sont des matières grasses allégées."
                },
                {
                    "questionNumber": 45,
                    "question": "Que signifie le chiffre 0 imprimé sur la coquille d'un œuf ?",
                    "answerOptions": [
                        {"text": "Élevage biologique", "isCorrect": True},
                        {"text": "Élevage en plein air", "isCorrect": False},
                        {"text": "Élevage au sol", "isCorrect": False},
                        {"text": "Élevage en cage", "isCorrect": False}
                    ],
                    "correction": "Le code est strict : 0 = Bio, 1 = Plein air, 2 = Sol, 3 = Cage. C'est un point de contrôle fréquent à la réception des marchandises."
                },
                {
                    "questionNumber": 46,
                    "question": "Dans la classification des poissons, quel est l'exemple type d'un poisson plat ?",
                    "answerOptions": [
                        {"text": "La sole", "isCorrect": True},
                        {"text": "Le bar", "isCorrect": False},
                        {"text": "Le saumon", "isCorrect": False},
                        {"text": "Le cabillaud", "isCorrect": False}
                    ],
                    "correction": "Les poissons plats (pleuronectiformes) comme la sole, le turbot ou la barbue ont les deux yeux du même côté et vivent sur le fond. Les autres cités sont des poissons ronds ou fusiformes."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel label de qualité garantit une qualité gustative supérieure par rapport aux produits standards similaires ?",
                    "answerOptions": [
                        {"text": "Label Rouge", "isCorrect": True},
                        {"text": "Agriculture Biologique", "isCorrect": False},
                        {"text": "Appellation d'Origine Protégée", "isCorrect": False},
                        {"text": "Indication Géographique Protégée", "isCorrect": False}
                    ],
                    "correction": "Le Label Rouge est le seul signe officiel français qui atteste d'une qualité organoleptique supérieure (goût), validée par des tests sensoriels. L'AOP/IGP garantissent l'origine."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel abat correspond au thymus du veau ?",
                    "answerOptions": [
                        {"text": "Le ris", "isCorrect": True},
                        {"text": "Le foie", "isCorrect": False},
                        {"text": "La rognonnade", "isCorrect": False},
                        {"text": "Le mou", "isCorrect": False}
                    ],
                    "correction": "Le ris de veau est une glande (le thymus) située à l'entrée de la poitrine. C'est un abat blanc très recherché en gastronomie."
                },
                {
                    "questionNumber": 49,
                    "question": "Comment reconnaît-on un poisson frais en observant ses branchies ?",
                    "answerOptions": [
                        {"text": "Rouges et humides", "isCorrect": True},
                        {"text": "Brunes et sèches", "isCorrect": False},
                        {"text": "Grises et gluantes", "isCorrect": False},
                        {"text": "Jaunâtres et odorantes", "isCorrect": False}
                    ],
                    "correction": "Les critères de fraîcheur sont stricts : l'œil doit être bombé et vif, et les branchies doivent être d'un rouge vif ou rosé, sans mucus excessif ni odeur ammoniaquée."
                },
                {
                    "questionNumber": 50,
                    "question": "De quel animal provient le jambon ?",
                    "answerOptions": [
                        {"text": "Le porc", "isCorrect": True},
                        {"text": "Le bœuf", "isCorrect": False},
                        {"text": "Le mouton", "isCorrect": False},
                        {"text": "Le veau", "isCorrect": False}
                    ],
                    "correction": "Le jambon est la cuisse (membre postérieur) du porc. C'est la pièce la plus noble de l'animal, utilisée pour le jambon cuit ou le jambon sec."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la définition exacte de l'Appellation d'Origine Protégée ?",
                    "answerOptions": [
                        {"text": "Lien fort au terroir", "isCorrect": True},
                        {"text": "Produit issu de l'agriculture respectueuse de l'environnement sans pesticides", "isCorrect": False},
                        {"text": "Garantie que le produit possède une réputation liée à son origine géographique", "isCorrect": False},
                        {"text": "Certification attestant que le produit respecte des normes internationales de commerce", "isCorrect": False}
                    ],
                    "correction": "L'AOP (logo rouge et jaune) garantit que toutes les étapes de fabrication (production, transformation, élaboration) ont lieu dans la zone géographique selon un savoir-faire reconnu."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle partie de la volaille est la plus sujette au dessèchement lors d'une cuisson rôtie ?",
                    "answerOptions": [
                        {"text": "Le filet", "isCorrect": True},
                        {"text": "La cuisse", "isCorrect": False},
                        {"text": "Le pilon", "isCorrect": False},
                        {"text": "Le sot-l'y-laisse", "isCorrect": False}
                    ],
                    "correction": "Le filet (ou blanc) est une viande maigre qui sèche très vite. La cuisse, plus grasse et irriguée, supporte mieux les cuissons prolongées."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel riz est spécifiquement recommandé pour la réalisation d'un risotto ?",
                    "answerOptions": [
                        {"text": "Arborio", "isCorrect": True},
                        {"text": "Basmati", "isCorrect": False},
                        {"text": "Thaï", "isCorrect": False},
                        {"text": "Complet", "isCorrect": False}
                    ],
                    "correction": "Pour le risotto, on utilise des riz riches en amidon qui ne s'effritent pas mais deviennent crémeux, comme l'Arborio ou le Carnaroli. Les riz longs (Basmati) ne lient pas."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle épice est issue du pistil d'une fleur de crocus ?",
                    "answerOptions": [
                        {"text": "Safran", "isCorrect": True},
                        {"text": "Curcuma", "isCorrect": False},
                        {"text": "Cumin", "isCorrect": False},
                        {"text": "Paprika", "isCorrect": False}
                    ],
                    "correction": "Le safran est l'épice la plus chère au monde car elle provient des stigmates (pistils) séchés de la fleur de Crocus sativus, récoltés à la main."
                },
                {
                    "questionNumber": 55,
                    "question": "Comment appelle-t-on la partie coraillée rouge présente dans une coquille Saint-Jacques ?",
                    "answerOptions": [
                        {"text": "Le corail", "isCorrect": True},
                        {"text": "La barde", "isCorrect": False},
                        {"text": "Le manteau", "isCorrect": False},
                        {"text": "La noix", "isCorrect": False}
                    ],
                    "correction": "La Saint-Jacques est composée de la noix (muscle blanc) et du corail (glande génitale, orange pour la partie femelle, blanche pour la partie mâle)."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel produit laitier obtient-on par coagulation du lait puis égouttage du caillé ?",
                    "answerOptions": [
                        {"text": "Le fromage", "isCorrect": True},
                        {"text": "Le beurre", "isCorrect": False},
                        {"text": "La crème fleurette", "isCorrect": False},
                        {"text": "Le lait concentré", "isCorrect": False}
                    ],
                    "correction": "La fabrication du fromage repose sur la coagulation (par présure ou ferments) qui sépare le caillé (solide) du petit-lait (liquide), suivi de l'égouttage et de l'affinage."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle catégorie de fruits inclut les noix, noisettes et amandes ?",
                    "answerOptions": [
                        {"text": "Fruits secs", "isCorrect": True},
                        {"text": "Fruits rouges", "isCorrect": False},
                        {"text": "Fruits à pépins", "isCorrect": False},
                        {"text": "Agrumes", "isCorrect": False}
                    ],
                    "correction": "Ce sont des fruits à coque ou fruits secs oléagineux. Ils se conservent longtemps en économat sec et sont riches en lipides."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle est la température de conservation réglementaire de la viande hachée fraîche non surgelée ?",
                    "answerOptions": [
                        {"text": "2 degrés", "isCorrect": True},
                        {"text": "4 degrés", "isCorrect": False},
                        {"text": "8 degrés", "isCorrect": False},
                        {"text": "0 degré", "isCorrect": False}
                    ],
                    "correction": "La viande hachée est un produit ultra-sensible. La réglementation impose une conservation entre 0°C et +2°C (souvent +2°C max retenu) et une consommation très rapide."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel ingrédient est un allergène majeur à déclaration obligatoire sur les cartes de restaurant ?",
                    "answerOptions": [
                        {"text": "Arachide", "isCorrect": True},
                        {"text": "Huile de tournesol", "isCorrect": False},
                        {"text": "Sel fin", "isCorrect": False},
                        {"text": "Poivre noir", "isCorrect": False}
                    ],
                    "correction": "L'arachide fait partie des 14 allergènes à déclaration obligatoire (INCO), tout comme le gluten, les crustacés, les œufs, le poisson, le soja, le lait, les fruits à coque, le céleri, la moutarde, le sésame, les sulfites, le lupin et les mollusques."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel morceau de l'agneau correspond au membre postérieur entier ?",
                    "answerOptions": [
                        {"text": "Le gigot", "isCorrect": True},
                        {"text": "L'épaule", "isCorrect": False},
                        {"text": "Le carré", "isCorrect": False},
                        {"text": "La selle", "isCorrect": False}
                    ],
                    "correction": "Le gigot est la cuisse arrière de l'agneau. L'épaule est le membre avant. La selle et le carré sont des morceaux du dos."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : TECHNIQUES CULINAIRES DE BASE (PRÉPARATIONS ET SAUCES) (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : TECHNIQUES CULINAIRES DE BASE (PRÉPARATIONS ET SAUCES) (Questions 61 à 80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelles sont les dimensions théoriques d'un taillage en brunoise ?",
                    "answerOptions": [
                        {"text": "Des dés de 2 millimètres", "isCorrect": True},
                        {"text": "Des bâtonnets de 5 centimètres", "isCorrect": False},
                        {"text": "Des tranches de 1 centimètre", "isCorrect": False},
                        {"text": "Des carrés de 4 centimètres", "isCorrect": False}
                    ],
                    "correction": "La brunoise est un taillage de précision : de très petits dés de 1 à 2 mm de section. Elle sert de garniture dans les potages, farces ou sauces."
                },
                {
                    "questionNumber": 62,
                    "question": "Quels sont les deux ingrédients de base pour réaliser un roux ?",
                    "answerOptions": [
                        {"text": "Beurre et farine", "isCorrect": True},
                        {"text": "Huile et maïzena", "isCorrect": False},
                        {"text": "Crème et jaune d'œuf", "isCorrect": False},
                        {"text": "Lait et fécule", "isCorrect": False}
                    ],
                    "correction": "Le roux est un liant obtenu par la cuisson d'un mélange tant pour tant (poids égal) de matière grasse (généralement du beurre) et de farine. Il sert de base aux grandes sauces."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle sauce mère obtient-on en mouillant un roux blanc avec du lait ?",
                    "answerOptions": [
                        {"text": "La béchamel", "isCorrect": True},
                        {"text": "La velouté", "isCorrect": False},
                        {"text": "La tomate", "isCorrect": False},
                        {"text": "La hollandaise", "isCorrect": False}
                    ],
                    "correction": "La béchamel est une sauce mère blanche. Si l'on mouille un roux blanc avec un fond (volaille, veau), on obtient un velouté, pas une béchamel."
                },
                {
                    "questionNumber": 64,
                    "question": "Que signifie le terme 'singer' lors de la réalisation d'un ragoût ?",
                    "answerOptions": [
                        {"text": "Saupoudrer de farine", "isCorrect": True},
                        {"text": "Ajouter du vin rouge", "isCorrect": False},
                        {"text": "Saler la viande", "isCorrect": False},
                        {"text": "Flamber à l'alcool", "isCorrect": False}
                    ],
                    "correction": "Singer consiste à saupoudrer les morceaux de viande revenus de farine avant de mouiller. Cela permet de créer la liaison de la sauce directement pendant la cuisson."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est la composition classique de la mirepoix aromatique ?",
                    "answerOptions": [
                        {"text": "Carotte oignon céleri", "isCorrect": True},
                        {"text": "Tomate poivron ail", "isCorrect": False},
                        {"text": "Navet poireau chou", "isCorrect": False},
                        {"text": "Courgette aubergine thym", "isCorrect": False}
                    ],
                    "correction": "La mirepoix est une garniture aromatique taillée en dés grossiers (carottes, oignons, parfois céleri) utilisée pour parfumer les fonds, les rôtis et les sauces."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on l'opération consistant à dissoudre les sucs de cuisson attachés au fond d'un récipient avec un liquide ?",
                    "answerOptions": [
                        {"text": "Déglacer", "isCorrect": True},
                        {"text": "Mouiller", "isCorrect": False},
                        {"text": "Blanchir", "isCorrect": False},
                        {"text": "Réduire", "isCorrect": False}
                    ],
                    "correction": "Déglacer permet de récupérer les sucs caramélisés (les protéines et glucides) au fond du sautoir pour donner du goût à la sauce. On utilise souvent de l'eau, du vin ou un fond."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle technique consiste à cuire des légumes dans un mélange d'eau, de beurre, de sucre et de sel jusqu'à évaporation complète du liquide ?",
                    "answerOptions": [
                        {"text": "Glacer à blanc", "isCorrect": True},
                        {"text": "Cuire à l'anglaise", "isCorrect": False},
                        {"text": "Sauter à cru", "isCorrect": False},
                        {"text": "Frire à l'huile", "isCorrect": False}
                    ],
                    "correction": "Glacer (à blanc ou à brun) permet d'enrober le légume d'une pellicule brillante et savoureuse grâce au mélange beurre/sucre, tout en le cuisant."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle est la base liquide d'une sauce mayonnaise ?",
                    "answerOptions": [
                        {"text": "Jaune d'œuf et huile", "isCorrect": True},
                        {"text": "Blanc d'œuf et moutarde", "isCorrect": False},
                        {"text": "Lait et vinaigre", "isCorrect": False},
                        {"text": "Crème liquide et citron", "isCorrect": False}
                    ],
                    "correction": "La mayonnaise est une émulsion froide stable. L'huile est dispersée en fines gouttelettes dans l'eau contenue dans le jaune d'œuf, stabilisée par la lécithine du jaune."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel nom porte le taillage des pommes de terre en forme de gros bâtonnets de 1 cm de section pour la friture ?",
                    "answerOptions": [
                        {"text": "Pont Neuf", "isCorrect": True},
                        {"text": "Paille", "isCorrect": False},
                        {"text": "Allumette", "isCorrect": False},
                        {"text": "Mignongnette", "isCorrect": False}
                    ],
                    "correction": "La Pomme Pont-Neuf est la frite classique épaisse (1cm x 1cm). L'Allumette est plus fine (0,5cm), et la Paille est très fine."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle préparation à base de champignons hachés et d'échalotes séchés à la poêle sert à farcir ou aromatiser ?",
                    "answerOptions": [
                        {"text": "La duxelles", "isCorrect": True},
                        {"text": "La persillade", "isCorrect": False},
                        {"text": "La matignon", "isCorrect": False},
                        {"text": "La julienne", "isCorrect": False}
                    ],
                    "correction": "La duxelles de champignons est une préparation sèche : on fait évaporer toute l'eau de végétation des champignons hachés pour concentrer le goût."
                },
                {
                    "questionNumber": 71,
                    "question": "Pour réaliser une pâte à choux, que doit-on faire impérativement après avoir incorporé la farine dans le liquide bouillant ?",
                    "answerOptions": [
                        {"text": "Dessécher la panade", "isCorrect": True},
                        {"text": "Ajouter le sucre glace", "isCorrect": False},
                        {"text": "Laisser reposer une heure", "isCorrect": False},
                        {"text": "Mettre au frigo", "isCorrect": False}
                    ],
                    "correction": "Il faut 'dessécher' la panade sur le feu en remuant énergiquement pour évacuer l'humidité excédentaire avant d'incorporer les œufs, sinon la pâte ne montera pas."
                },
                {
                    "questionNumber": 72,
                    "question": "Qu'est-ce qu'un 'fond blanc' ?",
                    "answerOptions": [
                        {"text": "Un bouillon réalisé sans coloration des os", "isCorrect": True},
                        {"text": "Une sauce à base de fromage blanc", "isCorrect": False},
                        {"text": "Un fond de tarte cuit à blanc", "isCorrect": False},
                        {"text": "Une réduction de vin blanc sec", "isCorrect": False}
                    ],
                    "correction": "Le fond blanc est réalisé en plongeant des os et parures (veau, volaille) directement dans l'eau froide avec garniture, sans les faire rissoler, pour obtenir un bouillon clair."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle sauce émulsionnée chaude accompagne traditionnellement le poisson poché ?",
                    "answerOptions": [
                        {"text": "La sauce hollandaise", "isCorrect": True},
                        {"text": "La sauce tartare", "isCorrect": False},
                        {"text": "La sauce gribiche", "isCorrect": False},
                        {"text": "La sauce vinaigrette", "isCorrect": False}
                    ],
                    "correction": "La hollandaise (jaunes d'œufs + beurre clarifié + réduction vinaigrée) est une émulsion chaude instable/semi-stable, classique des poissons."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle est la définition du terme 'monder' une tomate ?",
                    "answerOptions": [
                        {"text": "Retirer la peau après ébouillantage", "isCorrect": True},
                        {"text": "Retirer les pépins à la cuillère", "isCorrect": False},
                        {"text": "Couper la tomate en rondelles", "isCorrect": False},
                        {"text": "Mixer la tomate en purée", "isCorrect": False}
                    ],
                    "correction": "Monder (ou émonder) consiste à retirer la peau de la tomate. On incise la peau, on plonge la tomate 10 secondes dans l'eau bouillante puis dans la glace : la peau part toute seule."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle herbe aromatique est l'élément principal d'une sauce béarnaise ?",
                    "answerOptions": [
                        {"text": "Estragon", "isCorrect": True},
                        {"text": "Basilic", "isCorrect": False},
                        {"text": "Menthe", "isCorrect": False},
                        {"text": "Origan", "isCorrect": False}
                    ],
                    "correction": "La béarnaise est une dérivée de la hollandaise, mais avec une réduction d'échalotes et de vinaigre fortement parfumée à l'estragon et au cerfeuil."
                },
                {
                    "questionNumber": 76,
                    "question": "Lors de la confection d'une pâte brisée, quelle est la méthode consistant à frotter le beurre et la farine entre les mains ?",
                    "answerOptions": [
                        {"text": "Le sablage", "isCorrect": True},
                        {"text": "Le pétrissage", "isCorrect": False},
                        {"text": "Le fouettage", "isCorrect": False},
                        {"text": "Le tourage", "isCorrect": False}
                    ],
                    "correction": "Le sablage permet d'enrober les particules de farine de matière grasse, ce qui imperméabilise en partie le gluten et donne la texture friable ('brisée') après cuisson."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le but principal de l'opération 'tourner' un légume (pomme de terre, carotte) ?",
                    "answerOptions": [
                        {"text": "Esthétique et cuisson régulière", "isCorrect": True},
                        {"text": "Retirer le goût amer de la peau", "isCorrect": False},
                        {"text": "Augmenter le poids du légume", "isCorrect": False},
                        {"text": "Rendre le légume plus croustillant", "isCorrect": False}
                    ],
                    "correction": "Tourner consiste à donner une forme régulière (généralement allongée à 7 faces) pour que la présentation soit élégante et que tous les légumes cuisent à la même vitesse."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est la composition standard du bouquet garni ?",
                    "answerOptions": [
                        {"text": "Queues de persil thym et laurier", "isCorrect": True},
                        {"text": "Romarin ciboulette et coriandre", "isCorrect": False},
                        {"text": "Menthe sauge et aneth", "isCorrect": False},
                        {"text": "Oignon clous de girofle et ail", "isCorrect": False}
                    ],
                    "correction": "Le bouquet garni classique (ficelé pour être retiré facilement) comporte des queues de persil, une branche de thym et une feuille de laurier. Le vert de poireau sert souvent d'enveloppe."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment appelle-t-on le mélange de jaunes d'œufs et de crème utilisé pour lier et enrichir un velouté en fin de cuisson ?",
                    "answerOptions": [
                        {"text": "La liaison finale", "isCorrect": True},
                        {"text": "Le beurre manié", "isCorrect": False},
                        {"text": "La fécule délayée", "isCorrect": False},
                        {"text": "Le lait caillé", "isCorrect": False}
                    ],
                    "correction": "C'est une liaison 'au jaune et à la crème'. Elle s'ajoute hors du feu (ou à feu très doux) pour ne pas cuire le jaune (coagulation à 85°C), ce qui apporterait des grains."
                },
                {
                    "questionNumber": 80,
                    "question": "Pour réaliser des œufs à la neige, quelle préparation utilise-t-on ?",
                    "answerOptions": [
                        {"text": "Une meringue française", "isCorrect": True},
                        {"text": "Une pâte à génoise", "isCorrect": False},
                        {"text": "Une crème chantilly", "isCorrect": False},
                        {"text": "Une pâte à bombe", "isCorrect": False}
                    ],
                    "correction": "Les œufs à la neige sont des blancs montés serrés avec du sucre (meringue française), pochés dans du lait (ou cuits au four), puis servis sur une crème anglaise."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : LES MODES DE CUISSON ET L'ORGANISATION (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : LES MODES DE CUISSON ET L'ORGANISATION (Questions 81 à 100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "À quelle grande famille de cuisson appartient la technique 'Rôtir' ?",
                    "answerOptions": [
                        {"text": "La concentration", "isCorrect": True},
                        {"text": "L'expansion", "isCorrect": False},
                        {"text": "La cuisson mixte", "isCorrect": False},
                        {"text": "La cuisson sous vide", "isCorrect": False}
                    ],
                    "correction": "La concentration (par chaleur sèche) vise à saisir l'aliment brusquement. La croûte formée en surface emprisonne les éléments nutritifs et les saveurs à l'intérieur."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le principe physico-chimique de la cuisson par 'Expansion' ?",
                    "answerOptions": [
                        {"text": "Échange de saveurs entre l'aliment et le liquide", "isCorrect": True},
                        {"text": "Formation d'une croûte protectrice immédiate", "isCorrect": False},
                        {"text": "Caramélisation des sucs en surface", "isCorrect": False},
                        {"text": "Coagulation rapide des protéines externes", "isCorrect": False}
                    ],
                    "correction": "L'expansion (ex: pocher départ froid) ouvre les pores. Les sucs sortent de l'aliment pour parfumer le liquide (bouillon), et le liquide pénètre l'aliment (échange osmotique)."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle technique est un exemple type de cuisson mixte ?",
                    "answerOptions": [
                        {"text": "Le braisage", "isCorrect": True},
                        {"text": "La friture", "isCorrect": False},
                        {"text": "La vapeur", "isCorrect": False},
                        {"text": "La grillade", "isCorrect": False}
                    ],
                    "correction": "Le braisage est mixte car il combine deux phases : une concentration (rissolage de la viande) suivie d'une expansion (cuisson longue dans un liquide aromatique à couvert)."
                },
                {
                    "questionNumber": 84,
                    "question": "Qu'est-ce que la réaction de Maillard ?",
                    "answerOptions": [
                        {"text": "Le brunissement des protéines et des sucres à la chaleur", "isCorrect": True},
                        {"text": "L'évaporation de l'eau contenue dans les légumes", "isCorrect": False},
                        {"text": "La fermentation des levures dans une pâte", "isCorrect": False},
                        {"text": "La solidification de la matière grasse au froid", "isCorrect": False}
                    ],
                    "correction": "C'est la réaction chimique complexe qui se produit lors d'une cuisson vive (sauter, rôtir), créant la couleur brune, la croûte et les arômes caractéristiques du 'rôti'."
                },
                {
                    "questionNumber": 85,
                    "question": "Pourquoi laisse-t-on reposer une viande rouge après une cuisson rôtie ?",
                    "answerOptions": [
                        {"text": "Pour répartir les sucs et détendre les fibres", "isCorrect": True},
                        {"text": "Pour refroidir la viande avant de la servir", "isCorrect": False},
                        {"text": "Pour faire évaporer le surplus de graisse", "isCorrect": False},
                        {"text": "Pour que la croûte devienne plus dure", "isCorrect": False}
                    ],
                    "correction": "À la cuisson, les sucs se concentrent au centre de la pièce. Le repos permet à ces sucs de refluer vers l'extérieur (détente), rendant la viande uniformément tendre et juteuse."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est l'utilité principale d'une fiche technique en cuisine ?",
                    "answerOptions": [
                        {"text": "Calculer le coût et garantir la régularité", "isCorrect": True},
                        {"text": "Faire joli dans le classeur du chef", "isCorrect": False},
                        {"text": "Contrôler les horaires des employés", "isCorrect": False},
                        {"text": "Remplacer le bon de commande fournisseur", "isCorrect": False}
                    ],
                    "correction": "La fiche technique est l'outil de gestion central. Elle standardise la recette (ingrédients, progression) et permet de chiffrer précisément le coût matière par portion."
                },
                {
                    "questionNumber": 87,
                    "question": "Que signifie 'suer' des légumes lors d'une mise en place ?",
                    "answerOptions": [
                        {"text": "Éliminer l'eau de végétation sans coloration", "isCorrect": True},
                        {"text": "Faire brunir fortement les oignons", "isCorrect": False},
                        {"text": "Cuire dans une grande quantité d'eau", "isCorrect": False},
                        {"text": "Frire à haute température", "isCorrect": False}
                    ],
                    "correction": "Suer consiste à chauffer doucement des légumes (oignons, poireaux) dans un corps gras pour faire sortir leur eau naturelle et concentrer les saveurs, sans les laisser brunir."
                },
                {
                    "questionNumber": 88,
                    "question": "Dans le calcul des coûts, comment obtient-on la 'Marge Brute' ?",
                    "answerOptions": [
                        {"text": "Chiffre d'Affaires moins Coût Matière", "isCorrect": True},
                        {"text": "Prix d'achat plus TVA", "isCorrect": False},
                        {"text": "Total des factures fournisseurs divisé par deux", "isCorrect": False},
                        {"text": "Coût personnel plus loyer", "isCorrect": False}
                    ],
                    "correction": "La Marge Brute est l'argent qui reste au restaurateur une fois la nourriture payée. Elle doit servir à payer tout le reste (salaires, loyer, énergie, bénéfice)."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle méthode de gestion de stock impose d'utiliser les produits les plus anciens en premier ?",
                    "answerOptions": [
                        {"text": "Le FIFO", "isCorrect": True},
                        {"text": "Le HACCP", "isCorrect": False},
                        {"text": "Le PMS", "isCorrect": False},
                        {"text": "Le GBPH", "isCorrect": False}
                    ],
                    "correction": "FIFO signifie 'First In, First Out' (Premier Entré, Premier Sorti). C'est la règle d'or pour éviter les pertes et les dates de péremption dépassées."
                },
                {
                    "questionNumber": 90,
                    "question": "Pour fixer un prix de vente rapide, on multiplie le coût matière par un chiffre. Comment appelle-t-on ce chiffre ?",
                    "answerOptions": [
                        {"text": "Le coefficient multiplicateur", "isCorrect": True},
                        {"text": "Le taux de marque", "isCorrect": False},
                        {"text": "L'indice de consommation", "isCorrect": False},
                        {"text": "Le dividende brut", "isCorrect": False}
                    ],
                    "correction": "Si un plat coûte 5€ à produire et que le coefficient est de 4, on le vendra 20€. C'est une méthode empirique simple très utilisée en restauration."
                },
                {
                    "questionNumber": 91,
                    "question": "Lors d'une cuisson 'à l'anglaise' de légumes verts, quelle précaution préserve la chlorophylle (couleur verte) ?",
                    "answerOptions": [
                        {"text": "Cuire à découvert dans l'eau bouillante salée", "isCorrect": True},
                        {"text": "Cuire avec un couvercle dans l'eau froide", "isCorrect": False},
                        {"text": "Ajouter du vinaigre dans l'eau de cuisson", "isCorrect": False},
                        {"text": "Cuire très lentement à feu doux", "isCorrect": False}
                    ],
                    "correction": "Les acides volatils détruisent la chlorophylle. Cuire sans couvercle permet à ces acides de s'échapper avec la vapeur. Le refroidissement immédiat (glçante) fixe la couleur."
                },
                {
                    "questionNumber": 92,
                    "question": "Que signifie l'expression 'Marquer en cuisson' ?",
                    "answerOptions": [
                        {"text": "Démarrer la cuisson d'une préparation", "isCorrect": True},
                        {"text": "Écrire le nom du plat sur une ardoise", "isCorrect": False},
                        {"text": "Faire des marques de grillade sur une viande", "isCorrect": False},
                        {"text": "Vérifier la température du four", "isCorrect": False}
                    ],
                    "correction": "C'est le terme professionnel pour dire 'lancer' la cuisson (assembler les éléments dans le récipient et débuter le processus thermique)."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel document vérifie-t-on impérativement par rapport au bon de livraison lors de la réception des marchandises ?",
                    "answerOptions": [
                        {"text": "Le bon de commande", "isCorrect": True},
                        {"text": "La facture d'électricité", "isCorrect": False},
                        {"text": "Le menu du jour", "isCorrect": False},
                        {"text": "La fiche de poste", "isCorrect": False}
                    ],
                    "correction": "On doit toujours comparer ce qui est livré (Bon de Livraison) avec ce qu'on a commandé (Bon de Commande) pour repérer les erreurs, oublis ou substitutions non désirées."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle cuisson convient le mieux aux morceaux de viande de 2ème et 3ème catégorie (riches en collagène) ?",
                    "answerOptions": [
                        {"text": "Le braisage long", "isCorrect": True},
                        {"text": "La grillade minute", "isCorrect": False},
                        {"text": "Le rôtissage vif", "isCorrect": False},
                        {"text": "La friture profonde", "isCorrect": False}
                    ],
                    "correction": "Le collagène est dur. Il a besoin d'une cuisson longue en milieu humide (comme le braisage ou le ragoût) pour se transformer en gélatine et rendre la viande fondante."
                },
                {
                    "questionNumber": 95,
                    "question": "Qu'est-ce qu'une cuisson 'à blanc' pour un fond de tarte ?",
                    "answerOptions": [
                        {"text": "Cuire la pâte sans garniture liquide", "isCorrect": True},
                        {"text": "Cuire avec une crème blanche", "isCorrect": False},
                        {"text": "Cuire au micro-ondes", "isCorrect": False},
                        {"text": "Ne pas cuire la pâte du tout", "isCorrect": False}
                    ],
                    "correction": "On cuit 'à blanc' une pâte (souvent avec des billes de cuisson) quand la garniture ne supporte pas la cuisson (ex: tarte aux fraises fraîches) ou cuit très vite."
                },
                {
                    "questionNumber": 96,
                    "question": "En gestion, qu'est-ce qu'un inventaire physique ?",
                    "answerOptions": [
                        {"text": "Le comptage réel des marchandises en stock", "isCorrect": True},
                        {"text": "La liste des recettes du restaurant", "isCorrect": False},
                        {"text": "Le nettoyage complet de la cuisine", "isCorrect": False},
                        {"text": "La vérification des extincteurs", "isCorrect": False}
                    ],
                    "correction": "L'inventaire est l'acte de compter physiquement chaque produit dans les frigos et l'économat pour valoriser le stock réel et calculer le coût matière du mois (Stock initial + Achats - Stock final)."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle technique consiste à cuire un aliment dans de la graisse (huile ou graisse animale) à basse température, sans coloration ?",
                    "answerOptions": [
                        {"text": "Confire", "isCorrect": True},
                        {"text": "Frire", "isCorrect": False},
                        {"text": "Sauter", "isCorrect": False},
                        {"text": "Griller", "isCorrect": False}
                    ],
                    "correction": "Confire (ex: confit de canard), c'est cuire longtemps, doucement, immergé dans la graisse. Cela attendrit et conserve. Frire implique une haute température (180°C)."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est l'intérêt de la cuisson sous-vide à basse température ?",
                    "answerOptions": [
                        {"text": "Précision de cuisson et tendreté", "isCorrect": True},
                        {"text": "Rapidité d'exécution du service", "isCorrect": False},
                        {"text": "Obtention d'une croûte croustillante", "isCorrect": False},
                        {"text": "Économie de sacs plastiques", "isCorrect": False}
                    ],
                    "correction": "Le sous-vide permet une cuisson au degré près, préservant les textures, les poids (moins de perte d'eau) et les saveurs, mais ne permet pas de griller (il faut marquer après)."
                },
                {
                    "questionNumber": 99,
                    "question": "Comment appelle-t-on l'ensemble des opérations de préparation avant le service (épluchage, pesée, taillage) ?",
                    "answerOptions": [
                        {"text": "La mise en place", "isCorrect": True},
                        {"text": "Le coup de feu", "isCorrect": False},
                        {"text": "Le nettoyage", "isCorrect": False},
                        {"text": "La plonge", "isCorrect": False}
                    ],
                    "correction": "'La mise en place est la moitié du service'. C'est l'organisation préalable indispensable pour pouvoir envoyer les plats rapidement au moment de la commande client."
                },
                {
                    "questionNumber": 100,
                    "question": "Dans un ragoût à brun, quelle étape vient juste après avoir fait revenir la viande et la garniture aromatique ?",
                    "answerOptions": [
                        {"text": "Le singeage", "isCorrect": True},
                        {"text": "Le service", "isCorrect": False},
                        {"text": "Le découpage", "isCorrect": False},
                        {"text": "La liaison finale", "isCorrect": False}
                    ],
                    "correction": "Dans l'ordre chronologique d'un ragoût (ex: bœuf bourguignon) : rissoler la viande, ajouter la garniture, singer (farine), torréfier la farine, puis mouiller avec le liquide."
                }
            ]
        }
    }
}