quiz_data = {
    "title": "Quiz CAP Prévention Santé Environnement - Série 2 (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE DE VIE ET RISQUES BIOLOGIQUES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : HYGIÈNE DE VIE ET RISQUES BIOLOGIQUES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est le geste le plus efficace pour éviter la propagation des microbes manuportés ?",
                    "answerOptions": [
                        {"text": "Se laver les mains", "isCorrect": True},
                        {"text": "Porter un masque", "isCorrect": False},
                        {"text": "Aérer la pièce", "isCorrect": False},
                        {"text": "Mettre des gants", "isCorrect": False}
                    ],
                    "correction": "80% des microbes se transmettent par les mains. Le lavage des mains (eau + savon ou gel hydroalcoolique) est la barrière n°1 contre les infections."
                },
                {
                    "questionNumber": 2,
                    "question": "Contre quelles maladies le vaccin DTP (obligatoire) protège-t-il ?",
                    "answerOptions": [
                        {"text": "Diphtérie Tétanos Poliomyélite", "isCorrect": True},
                        {"text": "Diabète Toux Pneumonie", "isCorrect": False},
                        {"text": "Dengue Typhoïde Paludisme", "isCorrect": False},
                        {"text": "Dépression Tuberculose Peste", "isCorrect": False}
                    ],
                    "correction": "Le DTP est le vaccin de base obligatoire en France. Il protège contre trois maladies graves : la Diphtérie (respiratoire), le Tétanos (musculaire) et la Poliomyélite (paralysie)."
                },
                {
                    "questionNumber": 3,
                    "question": "Dans quel cas unique les antibiotiques sont-ils efficaces ?",
                    "answerOptions": [
                        {"text": "Infection bactérienne", "isCorrect": True},
                        {"text": "Infection virale", "isCorrect": False},
                        {"text": "Infection fongique", "isCorrect": False},
                        {"text": "Fatigue chronique", "isCorrect": False}
                    ],
                    "correction": "\"Les antibiotiques, c'est pas automatique\". Ils tuent les bactéries mais sont totalement inutiles contre les virus (grippe, rhume, COVID-19)."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le principal danger d'une consommation excessive d'écrans avant le coucher ?",
                    "answerOptions": [
                        {"text": "Retard d'endormissement dû à la lumière bleue", "isCorrect": True},
                        {"text": "Augmentation de l'audition", "isCorrect": False},
                        {"text": "Amélioration de la mémoire", "isCorrect": False},
                        {"text": "Baisse du rythme cardiaque", "isCorrect": False}
                    ],
                    "correction": "La lumière bleue des écrans bloque la sécrétion de mélatonine (l'hormone du sommeil), perturbant ainsi l'horloge biologique."
                },
                {
                    "questionNumber": 5,
                    "question": "Comment appelle-t-on la période entre la contamination par un microbe et l'apparition des premiers symptômes ?",
                    "answerOptions": [
                        {"text": "L'incubation", "isCorrect": True},
                        {"text": "L'invasion", "isCorrect": False},
                        {"text": "La convalescence", "isCorrect": False},
                        {"text": "La guérison", "isCorrect": False}
                    ],
                    "correction": "Pendant l'incubation, le microbe se multiplie dans l'organisme sans que la personne ne se sente encore malade."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la fonction principale des globules blancs (leucocytes) ?",
                    "answerOptions": [
                        {"text": "Défendre l'organisme contre les agresseurs", "isCorrect": True},
                        {"text": "Transporter l'oxygène", "isCorrect": False},
                        {"text": "Permettre la coagulation du sang", "isCorrect": False},
                        {"text": "Digérer les graisses", "isCorrect": False}
                    ],
                    "correction": "Les globules blancs sont les soldats du système immunitaire qui neutralisent les bactéries et les virus."
                },
                {
                    "questionNumber": 7,
                    "question": "Qu'est-ce qu'un porteur sain ?",
                    "answerOptions": [
                        {"text": "Une personne infectée qui ne présente aucun symptôme mais transmet le microbe", "isCorrect": True},
                        {"text": "Une personne qui fait beaucoup de sport", "isCorrect": False},
                        {"text": "Une personne qui n'a jamais été malade", "isCorrect": False},
                        {"text": "Un infirmier en bonne santé", "isCorrect": False}
                    ],
                    "correction": "Le porteur sain est dangereux pour les autres car il ignore qu'il est contagieux."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel organe est principalement détruit par le virus du SIDA (VIH) ?",
                    "answerOptions": [
                        {"text": "Le système immunitaire", "isCorrect": True},
                        {"text": "Le système digestif", "isCorrect": False},
                        {"text": "Le système moteur", "isCorrect": False},
                        {"text": "Le système osseux", "isCorrect": False}
                    ],
                    "correction": "Le VIH s'attaque aux lymphocytes T4, affaiblissant les défenses naturelles jusqu'à ce que l'organisme ne puisse plus combattre les infections bénignes."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le moyen de prévention le plus sûr contre le SIDA et les IST lors d'un rapport sexuel ?",
                    "answerOptions": [
                        {"text": "Le préservatif", "isCorrect": True},
                        {"text": "La pilule contraceptive", "isCorrect": False},
                        {"text": "Se laver après le rapport", "isCorrect": False},
                        {"text": "La confiance mutuelle seule", "isCorrect": False}
                    ],
                    "correction": "Le préservatif (masculin ou féminin) est le seul rempart physique contre la transmission des virus et bactéries sexuels."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la définition d'une pandémie ?",
                    "answerOptions": [
                        {"text": "Une épidémie qui s'étend à l'échelle mondiale", "isCorrect": True},
                        {"text": "Une maladie qui ne touche que les animaux", "isCorrect": False},
                        {"text": "Une maladie génétique rare", "isCorrect": False},
                        {"text": "Une infection limitée à un seul quartier", "isCorrect": False}
                    ],
                    "correction": "Une pandémie (comme la COVID-19) traverse les frontières et touche une grande partie de la population mondiale."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le risque majeur d'un bruit supérieur à 85 décibels répété quotidiennement ?",
                    "answerOptions": [
                        {"text": "Lésions irréversibles de l'oreille interne", "isCorrect": True},
                        {"text": "Amélioration de la vue", "isCorrect": False},
                        {"text": "Augmentation de la force musculaire", "isCorrect": False},
                        {"text": "Baisse du cholestérol", "isCorrect": False}
                    ],
                    "correction": "Les cellules ciliées de la cochlée sont détruites par le bruit excessif. Une fois mortes, elles ne se régénèrent jamais."
                },
                {
                    "questionNumber": 12,
                    "question": "Que signifie le sigle IMC ?",
                    "answerOptions": [
                        {"text": "Indice de Masse Corporelle", "isCorrect": True},
                        {"text": "Indice de Musculation de Croissance", "isCorrect": False},
                        {"text": "Intoxication Mentale Chronique", "isCorrect": False},
                        {"text": "Indicateur Médical du Cœur", "isCorrect": False}
                    ],
                    "correction": "L'IMC se calcule en divisant le poids par la taille au carré (kg/m²). Il permet d'évaluer les risques de surpoids ou de maigreur."
                },
                {
                    "questionNumber": 13,
                    "question": "Pourquoi faut-il privilégier les 'sucres lents' (féculents) ?",
                    "answerOptions": [
                        {"text": "Ils fournissent de l'énergie durablement à l'organisme", "isCorrect": True},
                        {"text": "Ils font maigrir instantanément", "isCorrect": False},
                        {"text": "Ils remplacent les protéines", "isCorrect": False},
                        {"text": "Ils sont plus faciles à manger", "isCorrect": False}
                    ],
                    "correction": "Les glucides complexes sont digérés lentement, évitant les pics d'insuline et les sensations de faim (coups de barre)."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelle est la principale cause d'apparition des caries dentaires ?",
                    "answerOptions": [
                        {"text": "Action des bactéries sur les résidus de sucre", "isCorrect": True},
                        {"text": "Manque d'exercice physique", "isCorrect": False},
                        {"text": "Lecture dans le noir", "isCorrect": False},
                        {"text": "Consommation de légumes verts", "isCorrect": False}
                    ],
                    "correction": "Les bactéries de la plaque dentaire transforment le sucre en acide, qui attaque l'émail des dents."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est l'effet de la nicotine sur le corps ?",
                    "answerOptions": [
                        {"text": "Dépendance et augmentation du rythme cardiaque", "isCorrect": True},
                        {"text": "Somnolence immédiate", "isCorrect": False},
                        {"text": "Amélioration de la respiration", "isCorrect": False},
                        {"text": "Baisse de la tension artérielle", "isCorrect": False}
                    ],
                    "correction": "La nicotine est la substance addictive du tabac. Elle agit comme un excitant cardio-vasculaire."
                },
                {
                    "questionNumber": 16,
                    "question": "Qu'est-ce qu'une addiction ?",
                    "answerOptions": [
                        {"text": "Besoin irrépressible de consommer une substance malgré ses effets nocifs", "isCorrect": True},
                        {"text": "Une habitude de lecture quotidienne", "isCorrect": False},
                        {"text": "Le fait de manger trois repas par jour", "isCorrect": False},
                        {"text": "Une allergie alimentaire", "isCorrect": False}
                    ],
                    "correction": "L'addiction (drogue, alcool, jeux, écrans) se définit par la perte de contrôle et la dépendance."
                },
                {
                    "questionNumber": 17,
                    "question": "Comment appelle-t-on le sommeil où l'on rêve le plus ?",
                    "answerOptions": [
                        {"text": "Le sommeil paradoxal", "isCorrect": True},
                        {"text": "Le sommeil lent léger", "isCorrect": False},
                        {"text": "Le sommeil lent profond", "isCorrect": False},
                        {"text": "L'insomnie", "isCorrect": False}
                    ],
                    "correction": "Pendant le sommeil paradoxal, l'activité cérébrale est intense alors que le corps est totalement paralysé."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel nutriment aide à la formation des os et des dents ?",
                    "answerOptions": [
                        {"text": "Le calcium", "isCorrect": True},
                        {"text": "Le fer", "isCorrect": False},
                        {"text": "La vitamine C", "isCorrect": False},
                        {"text": "Les fibres", "isCorrect": False}
                    ],
                    "correction": "Le calcium est minéral indispensable à la solidité du squelette, apporté principalement par les produits laitiers."
                },
                {
                    "questionNumber": 19,
                    "question": "Pourquoi est-il important d'aérer son logement au moins 10 minutes par jour ?",
                    "answerOptions": [
                        {"text": "Éliminer les polluants intérieurs et renouveler l'oxygène", "isCorrect": True},
                        {"text": "Refroidir les murs en été", "isCorrect": False},
                        {"text": "Faire entrer la poussière de la rue", "isCorrect": False},
                        {"text": "Chasser les mouches", "isCorrect": False}
                    ],
                    "correction": "L'air intérieur est souvent plus pollué que l'air extérieur (COV, CO2, humidité). L'aération prévient les troubles respiratoires."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le rôle de la mélanine dans la peau ?",
                    "answerOptions": [
                        {"text": "Protéger contre les rayons UV du soleil", "isCorrect": True},
                        {"text": "Rendre la peau imperméable", "isCorrect": False},
                        {"text": "Réguler la transpiration", "isCorrect": False},
                        {"text": "Transporter le sang", "isCorrect": False}
                    ],
                    "correction": "La mélanine est le pigment qui donne sa couleur à la peau et filtre une partie des rayons solaires dangereux."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : CONSOMMATION RESPONSABLE ET BUDGET (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : CONSOMMATION RESPONSABLE ET BUDGET",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Qu'est-ce qu'une charge fixe dans un budget ?",
                    "answerOptions": [
                        {"text": "Une dépense régulière dont le montant est prévisible (ex : loyer)", "isCorrect": True},
                        {"text": "Un achat coup de cœur en magasin", "isCorrect": False},
                        {"text": "La facture d'essence qui varie", "isCorrect": False},
                        {"text": "Un cadeau d'anniversaire", "isCorrect": False}
                    ],
                    "correction": "Les charges fixes (loyer, assurances, abonnements) doivent être payées chaque mois avant les loisirs."
                },
                {
                    "questionNumber": 22,
                    "question": "Que signifie le sigle TAEG sur un contrat de crédit ?",
                    "answerOptions": [
                        {"text": "Taux Annuel Effectif Global", "isCorrect": True},
                        {"text": "Tarif d'Achat Électrique Garanti", "isCorrect": False},
                        {"text": "Taux d'Assurance En Groupe", "isCorrect": False},
                        {"text": "Taxe sur l'Argent Emprunté", "isCorrect": False}
                    ],
                    "correction": "Le TAEG représente le coût total du crédit (intérêts + frais de dossier + assurance obligatoire)."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel document récapitule les ressources et les dépenses d'un individu ?",
                    "answerOptions": [
                        {"text": "Le budget", "isCorrect": True},
                        {"text": "La fiche de paie", "isCorrect": False},
                        {"text": "Le relevé d'identité bancaire (RIB)", "isCorrect": False},
                        {"text": "Le contrat de travail", "isCorrect": False}
                    ],
                    "correction": "Établir un budget permet de gérer son argent, d'anticiper les dépenses et d'éviter le découvert bancaire."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la durée légale du délai de rétractation pour un achat sur internet ?",
                    "answerOptions": [
                        {"text": "14 jours", "isCorrect": True},
                        {"text": "2 jours", "isCorrect": False},
                        {"text": "30 jours", "isCorrect": False},
                        {"text": "Aucun délai", "isCorrect": False}
                    ],
                    "correction": "En vente à distance, le consommateur dispose de 14 jours pour changer d'avis sans avoir à se justifier."
                },
                {
                    "questionNumber": 25,
                    "question": "Qu'est-ce que le 'reste à vivre' ?",
                    "answerOptions": [
                        {"text": "La somme restante après paiement des charges fixes et obligatoires", "isCorrect": True},
                        {"text": "Le montant du salaire brut", "isCorrect": False},
                        {"text": "Le prix total d'un chariot de courses", "isCorrect": False},
                        {"text": "L'argent placé sur un livret d'épargne", "isCorrect": False}
                    ],
                    "correction": "C'est la somme disponible pour l'alimentation, les loisirs, l'hygiène et les imprévus."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel organisme peut aider une personne en situation de surendettement ?",
                    "answerOptions": [
                        {"text": "La Commission de surendettement (Banque de France)", "isCorrect": True},
                        {"text": "La mairie", "isCorrect": False},
                        {"text": "Le commissariat de police", "isCorrect": False},
                        {"text": "Le pôle emploi", "isCorrect": False}
                    ],
                    "correction": "Elle permet de négocier un plan de remboursement avec les créanciers ou d'effacer les dettes sous conditions."
                },
                {
                    "questionNumber": 27,
                    "question": "Que signifie le label 'Agriculture Biologique' (AB) ?",
                    "answerOptions": [
                        {"text": "Produit cultivé sans engrais chimiques de synthèse ni pesticides", "isCorrect": True},
                        {"text": "Produit qui coûte moins cher que les autres", "isCorrect": False},
                        {"text": "Produit fabriqué uniquement en France", "isCorrect": False},
                        {"text": "Produit sans aucune calorie", "isCorrect": False}
                    ],
                    "correction": "Le logo AB garantit un mode de production respectueux de l'environnement et du bien-être animal."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le but principal de l'assurance responsabilité civile ?",
                    "answerOptions": [
                        {"text": "Réparer les dommages causés involontairement à autrui", "isCorrect": True},
                        {"text": "Payer ses propres frais médicaux", "isCorrect": False},
                        {"text": "Protéger sa maison contre le vol", "isCorrect": False},
                        {"text": "Acheter une nouvelle voiture", "isCorrect": False}
                    ],
                    "correction": "Elle est obligatoire et prend en charge les indemnités dues si vous blessez quelqu'un ou cassez l'objet d'un tiers par erreur."
                },
                {
                    "questionNumber": 29,
                    "question": "Qu'est-ce que l'éco-consommation ?",
                    "answerOptions": [
                        {"text": "Consommer des produits en limitant leur impact environnemental", "isCorrect": True},
                        {"text": "Ne plus rien acheter du tout", "isCorrect": False},
                        {"text": "Acheter uniquement des produits importés par avion", "isCorrect": False},
                        {"text": "Utiliser beaucoup d'emballages plastiques", "isCorrect": False}
                    ],
                    "correction": "Cela passe par le choix de produits locaux, de saison, avec peu d'emballage et durables."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle mention est obligatoire sur l'étiquetage des produits préemballés ?",
                    "answerOptions": [
                        {"text": "La liste des ingrédients", "isCorrect": True},
                        {"text": "La photo du producteur", "isCorrect": False},
                        {"text": "Le nom du transporteur", "isCorrect": False},
                        {"text": "La météo du jour de fabrication", "isCorrect": False}
                    ],
                    "correction": "La liste doit aussi mettre en évidence les allergènes (gluten, lait, arachide...)."
                },
                {
                    "questionNumber": 31,
                    "question": "Que signifie un Nutri-Score classé 'E' ?",
                    "answerOptions": [
                        {"text": "Qualité nutritionnelle médiocre (trop gras, trop sucré ou trop salé)", "isCorrect": True},
                        {"text": "Produit excellent pour la santé", "isCorrect": False},
                        {"text": "Produit sans aucun danger", "isCorrect": False},
                        {"text": "Produit issu du commerce équitable", "isCorrect": False}
                    ],
                    "correction": "Le Nutri-Score va de A (vert - bon) à E (orange foncé - limité). Il aide à comparer des produits d'une même catégorie."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'intérêt de l'épargne de précaution ?",
                    "answerOptions": [
                        {"text": "Faire face à un imprévu (panne, perte d'emploi)", "isCorrect": True},
                        {"text": "Avoir un gros salaire", "isCorrect": False},
                        {"text": "Payer ses impôts plus vite", "isCorrect": False},
                        {"text": "Donner de l'argent à la banque", "isCorrect": False}
                    ],
                    "correction": "Il est conseillé de mettre de côté l'équivalent de 2 à 3 mois de salaire en cas de coup dur."
                },
                {
                    "questionNumber": 33,
                    "question": "Qu'est-ce qu'une publicité mensongère ?",
                    "answerOptions": [
                        {"text": "Une publicité qui donne des informations fausses ou trompeuses", "isCorrect": True},
                        {"text": "Une publicité qui dure trop longtemps", "isCorrect": False},
                        {"text": "Une publicité à la radio", "isCorrect": False},
                        {"text": "Une publicité pour un produit gratuit", "isCorrect": False}
                    ],
                    "correction": "C'est un délit puni par le Code de la consommation pour protéger l'acheteur."
                },
                {
                    "questionNumber": 34,
                    "question": "Que signifie le terme 'obsolescence programmée' ?",
                    "answerOptions": [
                        {"text": "Réduire volontairement la durée de vie d'un produit pour en vendre un neuf", "isCorrect": True},
                        {"text": "Réparer gratuitement un appareil", "isCorrect": False},
                        {"text": "Le fait qu'un produit soit démodé", "isCorrect": False},
                        {"text": "Une garantie de 10 ans", "isCorrect": False}
                    ],
                    "correction": "C'est une pratique illégale qui pousse à la surconsommation et au gaspillage des ressources."
                },
                {
                    "questionNumber": 35,
                    "question": "Pourquoi faut-il comparer les prix au kilo ou au litre en magasin ?",
                    "answerOptions": [
                        {"text": "Pour comparer objectivement le coût réel malgré la taille de l'emballage", "isCorrect": True},
                        {"text": "Pour apprendre à faire des mathématiques", "isCorrect": False},
                        {"text": "Pour savoir si le paquet est lourd", "isCorrect": False},
                        {"text": "Pour vérifier le nom de la marque", "isCorrect": False}
                    ],
                    "correction": "Parfois, les formats 'familiaux' ou 'promos' sont plus chers à l'unité que les formats standards."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est l'utilité du ticket de caisse ?",
                    "answerOptions": [
                        {"text": "Preuve d'achat pour un échange, un remboursement ou la garantie", "isCorrect": True},
                        {"text": "Faire de la publicité au dos", "isCorrect": False},
                        {"text": "Vérifier l'heure de sortie du magasin", "isCorrect": False},
                        {"text": "C'est un papier inutile", "isCorrect": False}
                    ],
                    "correction": "Il est indispensable pour faire valoir ses droits de consommateur en cas de défaut."
                },
                {
                    "questionNumber": 37,
                    "question": "Qu'est-ce que le commerce équitable ?",
                    "answerOptions": [
                        {"text": "Garantir une juste rémunération aux producteurs des pays en développement", "isCorrect": True},
                        {"text": "Vendre des produits uniquement sur les marchés", "isCorrect": False},
                        {"text": "Un échange de produits entre voisins", "isCorrect": False},
                        {"text": "Un magasin qui appartient à l'État", "isCorrect": False}
                    ],
                    "correction": "Il assure le respect des droits des travailleurs et de l'environnement (ex : label Max Havelaar)."
                },
                {
                    "questionNumber": 38,
                    "question": "Que signifie la garantie légale de conformité (2 ans) ?",
                    "answerOptions": [
                        {"text": "Le vendeur doit réparer ou remplacer un produit défectueux", "isCorrect": True},
                        {"text": "Le produit doit être joli pendant 2 ans", "isCorrect": False},
                        {"text": "Le client doit payer un abonnement de 2 ans", "isCorrect": False},
                        {"text": "Le produit ne doit pas changer de couleur", "isCorrect": False}
                    ],
                    "correction": "Cette garantie est gratuite et obligatoire pour tous les biens neufs vendus en France."
                },
                {
                    "questionNumber": 39,
                    "question": "Qu'est-ce qu'un prélèvement automatique ?",
                    "answerOptions": [
                        {"text": "La banque paie directement une facture récurrente (ex : électricité)", "isCorrect": True},
                        {"text": "Un retrait d'argent au distributeur", "isCorrect": False},
                        {"text": "Une erreur de la banque", "isCorrect": False},
                        {"text": "Une prise de sang à l'hôpital", "isCorrect": False}
                    ],
                    "correction": "Il simplifie le paiement des charges fixes mais nécessite de surveiller son solde."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est le risque majeur des jeux d'argent et de hasard ?",
                    "answerOptions": [
                        {"text": "L'addiction et l'endettement rapide", "isCorrect": True},
                        {"text": "Devenir trop riche d'un coup", "isCorrect": False},
                        {"text": "Se faire des amis", "isCorrect": False},
                        {"text": "Perdre son ticket", "isCorrect": False}
                    ],
                    "correction": "La dépendance au jeu est une maladie reconnue qui peut détruire la vie sociale et financière."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : ÉCOLOGIE ET GESTION DES RESSOURCES (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ÉCOLOGIE ET GESTION DES RESSOURCES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le principal gaz responsable de l'effet de serre d'origine humaine ?",
                    "answerOptions": [
                        {"text": "Le dioxyde de carbone (CO2)", "isCorrect": True},
                        {"text": "L'oxygène", "isCorrect": False},
                        {"text": "L'hélium", "isCorrect": False},
                        {"text": "L'azote", "isCorrect": False}
                    ],
                    "correction": "Le CO2, issu de la combustion des énergies fossiles (pétrole, gaz, charbon), piège la chaleur dans l'atmosphère."
                },
                {
                    "questionNumber": 42,
                    "question": "Pourquoi faut-il privilégier le tri sélectif des déchets ?",
                    "answerOptions": [
                        {"text": "Économiser les matières premières par le recyclage", "isCorrect": True},
                        {"text": "Pour que les poubelles soient plus jolies", "isCorrect": False},
                        {"text": "Pour remplir les décharges plus vite", "isCorrect": False},
                        {"text": "Parce que c'est une activité sportive", "isCorrect": False}
                    ],
                    "correction": "Recycler permet de fabriquer de nouveaux objets sans puiser à nouveau dans les ressources naturelles limitées de la Terre."
                },
                {
                    "questionNumber": 43,
                    "question": "Qu'est-ce que l'empreinte carbone ?",
                    "answerOptions": [
                        {"text": "La quantité de gaz à effet de serre émise par une activité ou un produit", "isCorrect": True},
                        {"text": "Une trace de pas dans le charbon", "isCorrect": False},
                        {"text": "Le prix de la tonne de charbon", "isCorrect": False},
                        {"text": "La couleur noire d'un emballage", "isCorrect": False}
                    ],
                    "correction": "Elle permet de mesurer l'impact écologique de nos modes de transport, de chauffage ou d'alimentation."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle action simple permet de réduire sa consommation d'électricité ?",
                    "answerOptions": [
                        {"text": "Éteindre les appareils en veille", "isCorrect": True},
                        {"text": "Laisser la lumière allumée toute la journée", "isCorrect": False},
                        {"text": "Ouvrir les fenêtres avec le chauffage allumé", "isCorrect": False},
                        {"text": "Utiliser un vieux réfrigérateur mal fermé", "isCorrect": False}
                    ],
                    "correction": "Les appareils en veille (TV, ordi) consomment de l'énergie inutilement 24h/24."
                },
                {
                    "questionNumber": 45,
                    "question": "Dans quel bac de tri doit-on jeter les boîtes de conserve en métal ?",
                    "answerOptions": [
                        {"text": "Le bac jaune", "isCorrect": True},
                        {"text": "Le bac vert (verre)", "isCorrect": False},
                        {"text": "Le bac gris (ordures ménagères)", "isCorrect": False},
                        {"text": "On ne doit pas les jeter", "isCorrect": False}
                    ],
                    "correction": "L'acier et l'aluminium sont recyclables à l'infini. Ils vont dans le bac des emballages."
                },
                {
                    "questionNumber": 46,
                    "question": "Qu'est-ce qu'une énergie renouvelable ?",
                    "answerOptions": [
                        {"text": "Une source d'énergie qui ne s'épuise pas (ex : soleil, vent)", "isCorrect": True},
                        {"text": "Une énergie que l'on achète à nouveau", "isCorrect": False},
                        {"text": "Le pétrole et le gaz naturel", "isCorrect": False},
                        {"text": "L'électricité du secteur", "isCorrect": False}
                    ],
                    "correction": "Contrairement aux énergies fossiles, elles polluent moins et sont inépuisables."
                },
                {
                    "questionNumber": 47,
                    "question": "Pourquoi le gaspillage alimentaire est-il un problème écologique ?",
                    "answerOptions": [
                        {"text": "Car produire cette nourriture a consommé de l'eau et de l'énergie pour rien", "isCorrect": True},
                        {"text": "Parce que c'est mal poli", "isCorrect": False},
                        {"text": "Pour que les poubelles ne sentent pas mauvais", "isCorrect": False},
                        {"text": "Cela n'a aucun impact écologique", "isCorrect": False}
                    ],
                    "correction": "Jeter un aliment, c'est aussi jeter toutes les ressources utilisées pour le cultiver, le transformer et le transporter."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'objectif du développement durable ?",
                    "answerOptions": [
                        {"text": "Répondre aux besoins d'aujourd'hui sans sacrifier ceux de demain", "isCorrect": True},
                        {"text": "Arrêter toute activité économique", "isCorrect": False},
                        {"text": "Vendre des produits plus chers", "isCorrect": False},
                        {"text": "Utiliser toutes les ressources tout de suite", "isCorrect": False}
                    ],
                    "correction": "Il repose sur trois piliers : la protection de l'environnement, l'équité sociale et l'efficacité économique."
                },
                {
                    "questionNumber": 49,
                    "question": "Que signifie l'Écolabel européen ?",
                    "answerOptions": [
                        {"text": "Le produit a un impact environnemental réduit tout au long de sa vie", "isCorrect": True},
                        {"text": "Le produit est gratuit", "isCorrect": False},
                        {"text": "Le produit est fabriqué uniquement à la main", "isCorrect": False},
                        {"text": "Le produit a été testé sur des fleurs", "isCorrect": False}
                    ],
                    "correction": "C'est une certification officielle pour aider les consommateurs à choisir des produits plus 'verts'."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment appelle-t-on la disparition d'espèces animales et végétales ?",
                    "answerOptions": [
                        {"text": "L'érosion de la biodiversité", "isCorrect": True},
                        {"text": "Le changement de saison", "isCorrect": False},
                        {"text": "La métamorphose", "isCorrect": False},
                        {"text": "Le clonage", "isCorrect": False}
                    ],
                    "correction": "La biodiversité est essentielle à l'équilibre de la vie sur Terre et à la survie humaine."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est l'intérêt de manger des produits 'de saison' ?",
                    "answerOptions": [
                        {"text": "Limiter les transports lointains et la culture sous serres chauffées", "isCorrect": True},
                        {"text": "Parce qu'ils sont plus jolis", "isCorrect": False},
                        {"text": "Pour payer plus d'impôts", "isCorrect": False},
                        {"text": "Ils n'ont pas de goût", "isCorrect": False}
                    ],
                    "correction": "C'est un acte de consommation responsable qui réduit la pollution liée au transport."
                },
                {
                    "questionNumber": 52,
                    "question": "Que faire des piles et batteries usagées ?",
                    "answerOptions": [
                        {"text": "Les déposer dans des points de collecte spécifiques", "isCorrect": True},
                        {"text": "Les jeter dans la poubelle ménagère", "isCorrect": False},
                        {"text": "Les brûler dans la cheminée", "isCorrect": False},
                        {"text": "Les enterrer dans le jardin", "isCorrect": False}
                    ],
                    "correction": "Elles contiennent des métaux lourds (mercure, plomb) très toxiques pour les sols et l'eau."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la principale pollution générée par les transports routiers ?",
                    "answerOptions": [
                        {"text": "Émission de particules fines et de CO2", "isCorrect": True},
                        {"text": "Pollution par le bruit uniquement", "isCorrect": False},
                        {"text": "Pollution visuelle des routes", "isCorrect": False},
                        {"text": "Consommation excessive d'eau", "isCorrect": False}
                    ],
                    "correction": "Les gaz d'échappement dégradent la qualité de l'air et provoquent des maladies respiratoires."
                },
                {
                    "questionNumber": 54,
                    "question": "À quoi sert le compostage ?",
                    "answerOptions": [
                        {"text": "Transformer les déchets organiques en engrais naturel", "isCorrect": True},
                        {"text": "Remplacer les sacs plastiques", "isCorrect": False},
                        {"text": "Produire de l'électricité", "isCorrect": False},
                        {"text": "Tuer les insectes", "isCorrect": False}
                    ],
                    "correction": "Il réduit le volume de nos ordures ménagères et nourrit la terre sans chimie."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle quantité d'eau douce est disponible sur Terre ?",
                    "answerOptions": [
                        {"text": "Très peu (moins de 3% de l'eau totale)", "isCorrect": True},
                        {"text": "50%", "isCorrect": False},
                        {"text": "Autant que l'eau salée", "isCorrect": False},
                        {"text": "L'eau est inépuisable", "isCorrect": False}
                    ],
                    "correction": "L'eau potable est une ressource rare et précieuse qu'il faut protéger contre le gaspillage et la pollution."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le risque des microplastiques dans l'océan ?",
                    "answerOptions": [
                        {"text": "Ils entrent dans la chaîne alimentaire et empoisonnent les animaux", "isCorrect": True},
                        {"text": "Ils rendent l'eau plus bleue", "isCorrect": False},
                        {"text": "Ils servent de nourriture aux poissons", "isCorrect": False},
                        {"text": "Ils disparaissent naturellement en 2 jours", "isCorrect": False}
                    ],
                    "correction": "Les plastiques mettent des centaines d'années à se décomposer et finissent dans nos assiettes via les produits de la mer."
                },
                {
                    "questionNumber": 57,
                    "question": "Que signifie le logo 'Point Vert' (deux flèches entrelacées) ?",
                    "answerOptions": [
                        {"text": "L'entreprise finance le système de tri (ce n'est pas un logo de recyclage)", "isCorrect": True},
                        {"text": "L'objet est 100% recyclable", "isCorrect": False},
                        {"text": "L'objet est biodégradable", "isCorrect": False},
                        {"text": "Le produit est bio", "isCorrect": False}
                    ],
                    "correction": "Attention, ce logo est souvent confondu avec le ruban de Möbius qui, lui, indique le recyclage."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est l'impact de la déforestation ?",
                    "answerOptions": [
                        {"text": "Augmentation du CO2 et perte d'habitats pour les animaux", "isCorrect": True},
                        {"text": "Meilleure vue sur les montagnes", "isCorrect": False},
                        {"text": "Plus de place pour les déserts", "isCorrect": False},
                        {"text": "Amélioration de la fertilité des sols", "isCorrect": False}
                    ],
                    "correction": "Les arbres sont les 'poumons' de la Terre car ils absorbent le carbone."
                },
                {
                    "questionNumber": 59,
                    "question": "Qu'est-ce que le 'circuit court' ?",
                    "answerOptions": [
                        {"text": "Maximum un intermédiaire entre le producteur et le consommateur", "isCorrect": True},
                        {"text": "Un marathon de 5 kilomètres", "isCorrect": False},
                        {"text": "Une panne électrique dans la cuisine", "isCorrect": False},
                        {"text": "Acheter au supermarché", "isCorrect": False}
                    ],
                    "correction": "Il favorise l'économie locale et réduit la pollution liée aux transports internationaux."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment limiter l'impact environnemental du numérique ?",
                    "answerOptions": [
                        {"text": "Garder ses appareils le plus longtemps possible", "isCorrect": True},
                        {"text": "Changer de smartphone tous les ans", "isCorrect": False},
                        {"text": "Laisser l'ordinateur allumé toute la nuit", "isCorrect": False},
                        {"text": "Envoyer 500 emails par jour", "isCorrect": False}
                    ],
                    "correction": "La fabrication d'un appareil électronique consomme énormément de ressources et de métaux rares."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : VIE PROFESSIONNELLE ET DROITS DU SALARIÉ (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : VIE PROFESSIONNELLE ET DROITS DU SALARIÉ",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel contrat de travail est conclu pour une durée indéterminée ?",
                    "answerOptions": [
                        {"text": "CDI", "isCorrect": True},
                        {"text": "CDD", "isCorrect": False},
                        {"text": "CTT (Intérim)", "isCorrect": False},
                        {"text": "Stage", "isCorrect": False}
                    ],
                    "correction": "Le CDI est la forme normale du contrat de travail. Il n'a pas de date de fin prévue."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la durée légale du travail hebdomadaire en France ?",
                    "answerOptions": [
                        {"text": "35 heures", "isCorrect": True},
                        {"text": "39 heures", "isCorrect": False},
                        {"text": "48 heures", "isCorrect": False},
                        {"text": "20 heures", "isCorrect": False}
                    ],
                    "correction": "C'est la durée de référence. Au-delà, on parle d'heures supplémentaires."
                },
                {
                    "questionNumber": 63,
                    "question": "Sur une fiche de paie, qu'est-ce que le 'salaire brut' ?",
                    "answerOptions": [
                        {"text": "Le salaire avant déduction des cotisations sociales", "isCorrect": True},
                        {"text": "L'argent qui arrive sur le compte bancaire", "isCorrect": False},
                        {"text": "Le montant des pourboires", "isCorrect": False},
                        {"text": "Le salaire minimum uniquement", "isCorrect": False}
                    ],
                    "correction": "On retire du brut les charges salariales pour obtenir le 'salaire net'."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle instance représente les salariés et traite des questions de sécurité et santé au travail ?",
                    "answerOptions": [
                        {"text": "Le CSE (Comité Social et Économique)", "isCorrect": True},
                        {"text": "Le Tribunal de Grande Instance", "isCorrect": False},
                        {"text": "La Caisse d'Allocations Familiales", "isCorrect": False},
                        {"text": "La direction des ressources humaines", "isCorrect": False}
                    ],
                    "correction": "Le CSE est obligatoire dans les entreprises de plus de 11 salariés."
                },
                {
                    "questionNumber": 65,
                    "question": "Qu'est-ce que la Convention Collective ?",
                    "answerOptions": [
                        {"text": "Un accord adaptant le Code du travail à un secteur précis (ex : Coiffure, BTP)", "isCorrect": True},
                        {"text": "Un livre sur la politesse au bureau", "isCorrect": False},
                        {"text": "Le règlement intérieur de l'entreprise", "isCorrect": False},
                        {"text": "Une réunion de tous les salariés", "isCorrect": False}
                    ],
                    "correction": "Elle prévoit souvent des avantages supérieurs au Code du travail (primes, congés supplémentaires)."
                },
                {
                    "questionNumber": 66,
                    "question": "À quoi sert la période d'essai ?",
                    "answerOptions": [
                        {"text": "Permettre à l'employeur et au salarié de tester leur compatibilité", "isCorrect": True},
                        {"text": "Travailler sans être payé", "isCorrect": False},
                        {"text": "Acheter ses outils", "isCorrect": False},
                        {"text": "Prendre des vacances avant de commencer", "isCorrect": False}
                    ],
                    "correction": "Durant cette période, le contrat peut être rompu sans motif ni indemnité."
                },
                {
                    "questionNumber": 67,
                    "question": "Que signifie le sigle SMIC ?",
                    "answerOptions": [
                        {"text": "Salaire Minimum Interprofessionnel de Croissance", "isCorrect": True},
                        {"text": "Système de Mesure de l'Indice de Consommation", "isCorrect": False},
                        {"text": "Seuil de Mobilité Individuelle Court", "isCorrect": False},
                        {"text": "Salaire Moyen de l'Industrie et du Commerce", "isCorrect": False}
                    ],
                    "correction": "C'est le salaire horaire minimum obligatoire en dessous duquel un salarié ne peut être payé."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel document est obligatoirement remis à la fin d'un contrat de travail ?",
                    "answerOptions": [
                        {"text": "Le certificat de travail et l'attestation Pôle Emploi", "isCorrect": True},
                        {"text": "Le double des clés de l'entreprise", "isCorrect": False},
                        {"text": "Une lettre de recommandation obligatoire", "isCorrect": False},
                        {"text": "Un chèque cadeau", "isCorrect": False}
                    ],
                    "correction": "Ces documents sont nécessaires pour faire valoir ses droits au chômage et prouver son expérience."
                },
                {
                    "questionNumber": 69,
                    "question": "Qu'est-ce qu'une maladie professionnelle ?",
                    "answerOptions": [
                        {"text": "Une maladie causée par l'exercice prolongé d'un métier", "isCorrect": True},
                        {"text": "Une blessure soudaine au travail", "isCorrect": False},
                        {"text": "Attraper froid sur le chantier", "isCorrect": False},
                        {"text": "Un accident de voiture en allant au travail", "isCorrect": False}
                    ],
                    "correction": "Elle doit figurer dans un tableau de la Sécurité sociale pour être reconnue (ex : silicose, tendinite)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel organisme gère les dossiers de chômage en France ?",
                    "answerOptions": [
                        {"text": "France Travail (anciennement Pôle Emploi)", "isCorrect": True},
                        {"text": "La Sécurité Sociale", "isCorrect": False},
                        {"text": "Le Conseil de Prud'hommes", "isCorrect": False},
                        {"text": "La Mairie", "isCorrect": False}
                    ],
                    "correction": "Il accompagne les demandeurs d'emploi dans leur recherche et verse les allocations."
                },
                {
                    "questionNumber": 71,
                    "question": "Que signifie être 'salarié' ?",
                    "answerOptions": [
                        {"text": "Travailler pour un employeur contre rémunération et sous son autorité", "isCorrect": True},
                        {"text": "Travailler gratuitement pour apprendre", "isCorrect": False},
                        {"text": "Être son propre patron", "isCorrect": False},
                        {"text": "Ne pas avoir de contrat", "isCorrect": False}
                    ],
                    "correction": "Le lien de subordination est l'élément clé qui définit le salariat."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel tribunal est compétent en cas de litige entre un employeur et un salarié ?",
                    "answerOptions": [
                        {"text": "Le Conseil de Prud'hommes", "isCorrect": True},
                        {"text": "Le Tribunal Correctionnel", "isCorrect": False},
                        {"text": "Le Tribunal de Commerce", "isCorrect": False},
                        {"text": "La Cour d'Appel administrative", "isCorrect": False}
                    ],
                    "correction": "Il traite les conflits liés au contrat de travail (licenciement, salaires non payés...)."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la fonction de la Médecine du Travail ?",
                    "answerOptions": [
                        {"text": "Prévenir l'altération de la santé des travailleurs due à leur métier", "isCorrect": True},
                        {"text": "Soigner les grippes des salariés", "isCorrect": False},
                        {"text": "Sanctionner les ouvriers malades", "isCorrect": False},
                        {"text": "Distribuer des médicaments gratuitement", "isCorrect": False}
                    ],
                    "correction": "Le médecin du travail vérifie l'aptitude au poste et conseille sur l'ergonomie."
                },
                {
                    "questionNumber": 74,
                    "question": "À quoi sert le règlement intérieur de l'entreprise ?",
                    "answerOptions": [
                        {"text": "Fixer les règles de discipline, d'hygiène et de sécurité", "isCorrect": True},
                        {"text": "Donner les recettes de cuisine de la cantine", "isCorrect": False},
                        {"text": "Lister les numéros de téléphone des clients", "isCorrect": False},
                        {"text": "Vendre des produits aux employés", "isCorrect": False}
                    ],
                    "correction": "Il est obligatoire dans les entreprises de plus de 50 salariés."
                },
                {
                    "questionNumber": 75,
                    "question": "Qu'est-ce qu'une faute grave ?",
                    "answerOptions": [
                        {"text": "Un comportement rendant impossible le maintien du salarié dans l'entreprise", "isCorrect": True},
                        {"text": "Arriver une fois avec 2 minutes de retard", "isCorrect": False},
                        {"text": "Faire une erreur de calcul sans importance", "isCorrect": False},
                        {"text": "Demander une augmentation", "isCorrect": False}
                    ],
                    "correction": "Elle entraîne souvent un licenciement immédiat sans préavis ni indemnité."
                },
                {
                    "questionNumber": 76,
                    "question": "Que signifie le droit de retrait ?",
                    "answerOptions": [
                        {"text": "S'écarter d'une situation de travail présentant un danger grave et imminent", "isCorrect": True},
                        {"text": "Prendre sa retraite à 50 ans", "isCorrect": False},
                        {"text": "Retirer de l'argent au distributeur de l'entreprise", "isCorrect": False},
                        {"text": "Ne pas venir travailler car il pleut", "isCorrect": False}
                    ],
                    "correction": "C'est un droit protecteur pour le salarié qui craint pour sa vie ou sa santé."
                },
                {
                    "questionNumber": 77,
                    "question": "Combien de jours de congés payés gagne un salarié par mois de travail effectif ?",
                    "answerOptions": [
                        {"text": "2,5 jours", "isCorrect": True},
                        {"text": "1 jour", "isCorrect": False},
                        {"text": "5 jours", "isCorrect": False},
                        {"text": "Aucun la première année", "isCorrect": False}
                    ],
                    "correction": "Cela correspond à 30 jours ouvrables (5 semaines) par an."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est la différence entre un accident du travail et un accident de trajet ?",
                    "answerOptions": [
                        {"text": "Le trajet se passe entre le domicile et le lieu de travail", "isCorrect": True},
                        {"text": "L'accident de trajet n'est pas remboursé", "isCorrect": False},
                        {"text": "L'accident du travail a lieu uniquement au bureau", "isCorrect": False},
                        {"text": "C'est la même chose légalement", "isCorrect": False}
                    ],
                    "correction": "L'accident de trajet bénéficie d'une protection proche de l'accident du travail."
                },
                {
                    "questionNumber": 79,
                    "question": "Que signifie 'CDD d'usage' ?",
                    "answerOptions": [
                        {"text": "Un contrat court pour des secteurs où il est d'usage de ne pas recruter en CDI (ex : extra)", "isCorrect": True},
                        {"text": "Un contrat pour utiliser une machine", "isCorrect": False},
                        {"text": "Un contrat qui dure 10 ans", "isCorrect": False},
                        {"text": "Un contrat réservé aux stagiaires", "isCorrect": False}
                    ],
                    "correction": "Courant dans la restauration (extras) ou l'audiovisuel."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la mission d'un syndicat ?",
                    "answerOptions": [
                        {"text": "Défendre les droits et intérêts des travailleurs", "isCorrect": True},
                        {"text": "Organiser les vacances du patron", "isCorrect": False},
                        {"text": "Payer les amendes des salariés", "isCorrect": False},
                        {"text": "Remplacer le médecin du travail", "isCorrect": False}
                    ],
                    "correction": "Les syndicats négocient les conventions collectives et assistent les salariés."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : RISQUES SPÉCIFIQUES ET SECOURS - APPROFONDISSEMENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : RISQUES SPÉCIFIQUES ET SECOURS - APPROFONDISSEMENT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'ordre chronologique des actions du Sauveteur Secouriste du Travail (SST) ?",
                    "answerOptions": [
                        {"text": "Protéger - Examiner - Faire alerter - Secourir", "isCorrect": True},
                        {"text": "Secourir - Alerter - Examiner - Partir", "isCorrect": False},
                        {"text": "Alerter - Protéger - Secourir - Examiner", "isCorrect": False},
                        {"text": "Examiner - Alerter - Secourir - Protéger", "isCorrect": False}
                    ],
                    "correction": "On protège d'abord pour éviter un sur-accident, puis on examine la victime pour donner les bonnes informations aux secours."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la première chose à faire si une victime s'étouffe totalement (ne peut plus parler ni tousser) ?",
                    "answerOptions": [
                        {"text": "Donner 5 claques vigoureuses dans le dos", "isCorrect": True},
                        {"text": "Lui donner un verre d'eau", "isCorrect": False},
                        {"text": "L'allonger par terre", "isCorrect": False},
                        {"text": "Lui demander de lever les bras", "isCorrect": False}
                    ],
                    "correction": "Si les claques ne fonctionnent pas, il faudra pratiquer les compressions abdominales (méthode de Heimlich)."
                },
                {
                    "questionNumber": 83,
                    "question": "Comment arrêter un saignement abondant (hémorragie) ?",
                    "answerOptions": [
                        {"text": "Appuyer directement sur la plaie avec une main gantée ou un linge propre", "isCorrect": True},
                        {"text": "Laisser couler le sang pour nettoyer", "isCorrect": False},
                        {"text": "Mettre de la farine sur la plaie", "isCorrect": False},
                        {"text": "Faire un garrot au cou", "isCorrect": False}
                    ],
                    "correction": "La compression directe arrête la majorité des hémorragies en attendant les secours."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment vérifier si une victime inconsciente respire ?",
                    "answerOptions": [
                        {"text": "Regarder le ventre monter, écouter le souffle et sentir l'air sur sa joue", "isCorrect": True},
                        {"text": "Lui crier dessus", "isCorrect": False},
                        {"text": "Lui pincer le bras", "isCorrect": False},
                        {"text": "Lui mettre un miroir devant la bouche", "isCorrect": False}
                    ],
                    "correction": "On vérifie la respiration pendant 10 secondes maximum."
                },
                {
                    "questionNumber": 85,
                    "question": "Que doit-on faire si une victime est inconsciente mais respire normalement ?",
                    "answerOptions": [
                        {"text": "La mettre en Position Latérale de Sécurité (PLS)", "isCorrect": True},
                        {"text": "Lui faire un massage cardiaque", "isCorrect": False},
                        {"text": "Lui donner à boire", "isCorrect": False},
                        {"text": "La laisser sur le dos", "isCorrect": False}
                    ],
                    "correction": "La PLS évite que la victime ne s'étouffe avec sa langue ou ses vomissements."
                },
                {
                    "questionNumber": 86,
                    "question": "Que faire face à une victime qui ne répond pas et ne respire pas ?",
                    "answerOptions": [
                        {"text": "Alerter et débuter immédiatement un massage cardiaque", "isCorrect": True},
                        {"text": "L'arroser d'eau froide", "isCorrect": False},
                        {"text": "Attendre 10 minutes", "isCorrect": False},
                        {"text": "Lui mettre une couverture", "isCorrect": False}
                    ],
                    "correction": "Chaque minute compte. Il faut masser le cœur pour envoyer du sang au cerveau."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel appareil doit être utilisé le plus tôt possible en cas d'arrêt cardiaque ?",
                    "answerOptions": [
                        {"text": "Le DAE (Défibrillateur Automatisé Externe)", "isCorrect": True},
                        {"text": "Un thermomètre", "isCorrect": False},
                        {"text": "Un ventilateur", "isCorrect": False},
                        {"text": "Une balance", "isCorrect": False}
                    ],
                    "correction": "Le DAE analyse le rythme cardiaque et délivre un choc électrique si nécessaire. Il est accessible à tous dans les lieux publics."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est la conduite à tenir pour une brûlure thermique simple ?",
                    "answerOptions": [
                        {"text": "Rincer à l'eau tempérée (15-25°C) jusqu'à disparition de la douleur", "isCorrect": True},
                        {"text": "Mettre du beurre ou du dentifrice", "isCorrect": False},
                        {"text": "Percer les cloques immédiatement", "isCorrect": False},
                        {"text": "Mettre de la glace directement sur la peau", "isCorrect": False}
                    ],
                    "correction": "L'eau refroidit les tissus et stoppe la progression de la brûlure en profondeur."
                },
                {
                    "questionNumber": 89,
                    "question": "Que signifie un panneau circulaire rouge barré ?",
                    "answerOptions": [
                        {"text": "Une interdiction", "isCorrect": True},
                        {"text": "Une obligation", "isCorrect": False},
                        {"text": "Une sortie de secours", "isCorrect": False},
                        {"text": "Un danger électrique", "isCorrect": False}
                    ],
                    "correction": "Ex : Interdiction de fumer, interdiction d'entrer."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le risque lié à une exposition prolongée aux vibrations (ex : marteau-piqueur) ?",
                    "answerOptions": [
                        {"text": "Troubles articulaires et circulatoires des mains", "isCorrect": True},
                        {"text": "Amélioration de la force du poignet", "isCorrect": False},
                        {"text": "Perte de la vue", "isCorrect": False},
                        {"text": "Caries dentaires", "isCorrect": False}
                    ],
                    "correction": "C'est un risque physique professionnel qui peut causer la maladie des 'doigts blancs'."
                },
                {
                    "questionNumber": 91,
                    "question": "Comment appelle-t-on la méthode d'analyse pour comprendre un accident après coup ?",
                    "answerOptions": [
                        {"text": "L'arbre des causes", "isCorrect": True},
                        {"text": "La météo des risques", "isCorrect": False},
                        {"text": "Le cercle de Sinner", "isCorrect": False},
                        {"text": "La pyramide alimentaire", "isCorrect": False}
                    ],
                    "correction": "Il permet de remonter aux causes profondes pour éviter que l'accident ne se reproduise."
                },
                {
                    "questionNumber": 92,
                    "question": "Qu'est-ce que le risque électrique ?",
                    "answerOptions": [
                        {"text": "Le risque d'électrisation ou d'électrocution par contact avec le courant", "isCorrect": True},
                        {"text": "Le risque de tomber d'une échelle", "isCorrect": False},
                        {"text": "Le risque de manquer de lumière", "isCorrect": False},
                        {"text": "Le risque que la batterie du téléphone soit vide", "isCorrect": False}
                    ],
                    "correction": "Le passage du courant dans le corps peut causer des brûlures internes ou l'arrêt du cœur."
                },
                {
                    "questionNumber": 93,
                    "question": "Pourquoi le stress au travail est-il considéré comme un risque ?",
                    "answerOptions": [
                        {"text": "Il peut causer des maladies cardiovasculaires et des dépressions", "isCorrect": True},
                        {"text": "Il rend les gens plus rapides", "isCorrect": False},
                        {"text": "Il n'a aucun impact sur la santé", "isCorrect": False},
                        {"text": "Il fait grossir uniquement", "isCorrect": False}
                    ],
                    "correction": "Le stress chronique est un Risque Psycho-Social (RPS) majeur."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est l'EPI indispensable pour se protéger les yeux des produits chimiques ?",
                    "answerOptions": [
                        {"text": "Les lunettes de protection ou visière", "isCorrect": True},
                        {"text": "Des lunettes de soleil", "isCorrect": False},
                        {"text": "Fermer les yeux en travaillant", "isCorrect": False},
                        {"text": "Mettre un bonnet", "isCorrect": False}
                    ],
                    "correction": "Les projections d'acide ou de base peuvent causer une cécité immédiate."
                },
                {
                    "questionNumber": 95,
                    "question": "Que faire si un collègue est électrisé et encore en contact avec la source électrique ?",
                    "answerOptions": [
                        {"text": "Couper le courant immédiatement sans toucher la victime", "isCorrect": True},
                        {"text": "Tirer la victime par le bras", "isCorrect": False},
                        {"text": "Lui verser de l'eau", "isCorrect": False},
                        {"text": "Appeler ses parents", "isCorrect": False}
                    ],
                    "correction": "Si vous touchez la victime, vous serez électrisé à votre tour. Il faut isoler le courant d'abord."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la définition de la prévention intrinsèque ?",
                    "answerOptions": [
                        {"text": "Supprimer le danger dès la conception (ex : remplacer un produit toxique)", "isCorrect": True},
                        {"text": "Mettre une affiche de sécurité", "isCorrect": False},
                        {"text": "Porter un casque", "isCorrect": False},
                        {"text": "Former les salariés", "isCorrect": False}
                    ],
                    "correction": "C'est le niveau de prévention le plus efficace."
                },
                {
                    "questionNumber": 97,
                    "question": "Qu'est-ce qu'un Risque Psycho-Social (RPS) ?",
                    "answerOptions": [
                        {"text": "Stress, harcèlement, burn-out ou violence au travail", "isCorrect": True},
                        {"text": "Une coupure au doigt", "isCorrect": False},
                        {"text": "Un problème de dos", "isCorrect": False},
                        {"text": "Un microbe", "isCorrect": False}
                    ],
                    "correction": "Le stress survient quand le salarié a l'impression (réelle ou ressentie) qu'il n'arrivera pas à faire ce qu'on attend de lui."
                },
                {
                    "questionNumber": 98,
                    "question": "Pourquoi est-il interdit de fumer dans les locaux de travail ?",
                    "answerOptions": [
                        {"text": "Risque incendie et protection des non-fumeurs", "isCorrect": True},
                        {"text": "Pour économiser l'argent des salariés", "isCorrect": False},
                        {"text": "Parce que l'odeur dérange le patron", "isCorrect": False},
                        {"text": "Pour éviter de salir les cendriers", "isCorrect": False}
                    ],
                    "correction": "L'interdiction vise deux objectifs majeurs : prévenir les départs de feu (mégots mal éteints) et protéger la santé de tous contre le tabagisme passif."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel dispositif de sécurité coupe le courant si une personne touche un fil dénudé ?",
                    "answerOptions": [
                        {"text": "Disjoncteur différentiel 30 mA", "isCorrect": True},
                        {"text": "Fusible à cartouche", "isCorrect": False},
                        {"text": "Ampoule basse consommation", "isCorrect": False},
                        {"text": "Rallonge électrique", "isCorrect": False}
                    ],
                    "correction": "Le différentiel (30 milliampères) détecte les fuites de courant vers la terre (ce qui se passe quand on s'électrise)."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le but ultime de toutes les démarches de prévention en entreprise ?",
                    "answerOptions": [
                        {"text": "Supprimer ou réduire les accidents du travail", "isCorrect": True},
                        {"text": "Remplir des papiers administratifs", "isCorrect": False},
                        {"text": "Faire plaisir à l'inspecteur du travail", "isCorrect": False},
                        {"text": "Dépenser le budget sécurité", "isCorrect": False}
                    ],
                    "correction": "La finalité de la PSE et de la santé au travail est de préserver l'intégrité physique et mentale des travailleurs."
                }
            ]
        }
    }
}