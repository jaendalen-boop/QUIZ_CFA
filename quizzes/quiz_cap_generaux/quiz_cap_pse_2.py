quiz_data = {
    "title": "Quiz CAP Prévention Santé Environnement - Série 2 (100 Questions) - Version Optimisée",
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
                        {"text": "Se laver les mains très régulièrement à l'eau et au savon", "isCorrect": True},
                        {"text": "Porter un masque de protection respiratoire jetable", "isCorrect": False},
                        {"text": "Aérer la pièce de vie au moins dix minutes par jour", "isCorrect": False},
                        {"text": "Mettre des gants de ménage pour toutes les activités", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Environ 80 % des microbes se transmettent par les mains (transmission manuportée). Le lavage des mains (ou l'usage de gel hydroalcoolique) reste la barrière numéro 1 contre les infections hivernales, alimentaires et hospitalières."
                },
                {
                    "questionNumber": 2,
                    "question": "Contre quelles maladies le vaccin DTP (obligatoire en France) protège-t-il ?",
                    "answerOptions": [
                        {"text": "La Diphtérie, le Tétanos et la Poliomyélite", "isCorrect": True},
                        {"text": "Le Diabète, la Toux et la Pneumonie sévère", "isCorrect": False},
                        {"text": "La Dengue, la Typhoïde et le Paludisme", "isCorrect": False},
                        {"text": "La Dépression, la Tuberculose et la Peste", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le vaccin DTP est indispensable. Il protège contre la Diphtérie (angine grave), le Tétanos (infection par une plaie souillée) et la Poliomyélite (paralysie). Les rappels sont essentiels tout au long de la vie adulte."
                },
                {
                    "questionNumber": 3,
                    "question": "Dans quel cas unique les antibiotiques sont-ils réellement efficaces ?",
                    "answerOptions": [
                        {"text": "Pour soigner une infection de type bactérienne", "isCorrect": True},
                        {"text": "Pour soigner une infection de type virale", "isCorrect": False},
                        {"text": "Pour soigner une infection de type fongique", "isCorrect": False},
                        {"text": "Pour lutter contre une fatigue physique chronique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Comme le dit le slogan 'Les antibiotiques, c'est pas automatique', ils ne tuent que les bactéries. Ils sont totalement inutiles contre les virus (grippe, rhume, bronchite, COVID-19) et leur usage abusif crée des résistances dangereuses."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le principal danger d'une consommation excessive d'écrans avant le coucher ?",
                    "answerOptions": [
                        {"text": "Un retard d'endormissement dû à l'effet de la lumière bleue", "isCorrect": True},
                        {"text": "Une augmentation sensible de la capacité d'audition", "isCorrect": False},
                        {"text": "Une amélioration globale de la mémoire à long terme", "isCorrect": False},
                        {"text": "Une baisse brutale du rythme cardiaque durant la nuit", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La lumière bleue émise par les smartphones et tablettes bloque la sécrétion de mélatonine, l'hormone du sommeil. Cela décale l'horloge biologique et nuit à la qualité de la récupération nocturne."
                },
                {
                    "questionNumber": 5,
                    "question": "Comment appelle-t-on la période entre la contamination par un microbe et les symptômes ?",
                    "answerOptions": [
                        {"text": "La phase d'incubation du germe infectieux", "isCorrect": True},
                        {"text": "La phase d'invasion brutale de l'organisme", "isCorrect": False},
                        {"text": "La phase de convalescence après la maladie", "isCorrect": False},
                        {"text": "La phase de guérison totale du patient", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Durant l'incubation, le microbe se multiplie silencieusement. La personne est souvent déjà contagieuse même si elle ne se sent pas encore malade. La durée varie selon la maladie (quelques jours pour la grippe, plusieurs années pour le VIH)."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la fonction principale des globules blancs (leucocytes) ?",
                    "answerOptions": [
                        {"text": "Défendre activement l'organisme contre les agresseurs", "isCorrect": True},
                        {"text": "Transporter l'oxygène pur vers les organes vitaux", "isCorrect": False},
                        {"text": "Permettre la coagulation rapide du sang sur une plaie", "isCorrect": False},
                        {"text": "Digérer les graisses après un repas trop lourd", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les globules blancs sont les cellules du système immunitaire. Ils agissent comme des soldats qui détectent, attaquent et détruisent les virus, les bactéries et les corps étrangers présents dans le sang ou les tissus."
                },
                {
                    "questionNumber": 7,
                    "question": "Qu'est-ce qu'un porteur sain en infectiologie ?",
                    "answerOptions": [
                        {"text": "Une personne infectée sans symptômes qui transmet le microbe", "isCorrect": True},
                        {"text": "Une personne qui pratique une activité sportive intense", "isCorrect": False},
                        {"text": "Une personne qui n'a jamais contracté de maladie", "isCorrect": False},
                        {"text": "Un professionnel de santé travaillant à l'hôpital", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le porteur sain (ou asymptomatique) héberge un microbe dangereux sans en souffrir lui-même. C'est un maillon critique dans la propagation des épidémies car il contamine les autres sans le savoir."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel système est principalement détruit par le virus du SIDA ?",
                    "answerOptions": [
                        {"text": "L'ensemble du système immunitaire de défense", "isCorrect": True},
                        {"text": "L'ensemble du système digestif et intestinal", "isCorrect": False},
                        {"text": "L'ensemble du système moteur et musculaire", "isCorrect": False},
                        {"text": "L'ensemble du système osseux et articulaire", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le VIH (Virus de l'Immunodéficience Humaine) s'attaque aux lymphocytes T4, les 'chefs d'orchestre' de nos défenses. Sans traitement, le corps ne peut plus se défendre contre les infections dites 'opportunistes'."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le moyen de prévention le plus sûr contre les IST lors d'un rapport sexuel ?",
                    "answerOptions": [
                        {"text": "L'usage systématique d'un préservatif masculin ou féminin", "isCorrect": True},
                        {"text": "La prise quotidienne de la pilule contraceptive féminine", "isCorrect": False},
                        {"text": "Une hygiène corporelle très rigoureuse après le rapport", "isCorrect": False},
                        {"text": "La confiance mutuelle établie entre les deux partenaires", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Seul le préservatif agit comme une barrière physique contre les bactéries et virus sexuellement transmissibles. La pilule et le stérilet empêchent la grossesse mais n'offrent aucune protection contre les infections."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la définition précise d'une pandémie ?",
                    "answerOptions": [
                        {"text": "Une épidémie de grande ampleur à l'échelle mondiale", "isCorrect": True},
                        {"text": "Une maladie qui ne touche que les animaux sauvages", "isCorrect": False},
                        {"text": "Une maladie génétique très rare dès la naissance", "isCorrect": False},
                        {"text": "Une infection bactérienne limitée à un seul quartier", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On parle de pandémie quand une maladie infectieuse se propage sur plusieurs continents simultanément et touche une très grande partie de la population mondiale (ex: Grippe espagnole, COVID-19)."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le risque d'un bruit supérieur à 85 dB répété quotidiennement ?",
                    "answerOptions": [
                        {"text": "Le développement de lésions irréversibles de l'oreille interne", "isCorrect": True},
                        {"text": "Une amélioration globale de la vision nocturne du sujet", "isCorrect": False},
                        {"text": "Une augmentation de la force musculaire des membres", "isCorrect": False},
                        {"text": "Une baisse durable du taux de cholestérol dans le sang", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les cellules ciliées de la cochlée captent les sons. Si elles sont détruites par un bruit trop fort (concert, usine), elles ne se régénèrent jamais. La surdérité professionnelle est définitive."
                },
                {
                    "questionNumber": 12,
                    "question": "À quoi sert le calcul de l'Indice de Masse Corporelle ?",
                    "answerOptions": [
                        {"text": "À évaluer la corpulence et les risques liés au poids", "isCorrect": True},
                        {"text": "À mesurer la puissance de la musculature du cœur", "isCorrect": False},
                        {"text": "À détecter une intoxication mentale ou un stress", "isCorrect": False},
                        {"text": "À vérifier le taux de sucre présent dans les urines", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'IMC se calcule en divisant le poids (kg) par la taille au carré (m²). Entre 18,5 et 25, la corpulence est normale. Au-delà de 30, on parle d'obésité avec des risques accrus pour le cœur."
                },
                {
                    "questionNumber": 13,
                    "question": "Pourquoi est-il vital de privilégier les glucides complexes comme les féculents ?",
                    "answerOptions": [
                        {"text": "Car ils fournissent de l'énergie durablement à l'organisme", "isCorrect": True},
                        {"text": "Car ils permettent de perdre du poids très rapidement", "isCorrect": False},
                        {"text": "Car ils peuvent remplacer totalement les protéines animales", "isCorrect": False},
                        {"text": "Car ils sont beaucoup plus faciles à digérer le soir", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les 'sucres lents' libèrent leur énergie sur plusieurs heures. Ils évitent les pics d'insuline et les sensations de faim (fringales) responsables du grignotage."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelle est la cause directe de la destruction de l'émail dentaire ?",
                    "answerOptions": [
                        {"text": "L'action des acides produits par les bactéries sur le sucre", "isCorrect": True},
                        {"text": "Le manque d'exercice physique régulier pendant la semaine", "isCorrect": False},
                        {"text": "Le fait de lire trop longtemps dans une pièce noire", "isCorrect": False},
                        {"text": "La consommation exclusive de légumes verts frais", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les bactéries de la plaque dentaire transforment les résidus de sucre en acide. Cet acide 'creuse' la dent, créant une carie. Le brossage élimine mécaniquement ces bactéries."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est l'effet principal de la nicotine sur le système cardiovasculaire ?",
                    "answerOptions": [
                        {"text": "Une forte dépendance et une hausse du rythme cardiaque", "isCorrect": True},
                        {"text": "Une somnolence immédiate dès la première bouffée", "isCorrect": False},
                        {"text": "Une amélioration de la capacité respiratoire profonde", "isCorrect": False},
                        {"text": "Une baisse durable de la tension artérielle moyenne", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La nicotine est la substance addictive du tabac. Elle agit comme un stimulant qui accélère le cœur et rétrécit les artères, augmentant ainsi le risque d'infarctus ou d'AVC."
                },
                {
                    "questionNumber": 16,
                    "question": "Comment définit-on médicalement une addiction ?",
                    "answerOptions": [
                        {"text": "Le besoin irrépressible de consommer malgré la toxicité", "isCorrect": True},
                        {"text": "Une habitude culturelle de lecture quotidienne calme", "isCorrect": False},
                        {"text": "Le fait de prendre trois repas équilibrés par jour", "isCorrect": False},
                        {"text": "Une allergie alimentaire sévère à certains produits", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'addiction est une maladie du cerveau. Elle se caractérise par la perte de contrôle, la dépendance physique ou psychique, et la poursuite de la consommation malgré les dommages évidents."
                },
                {
                    "questionNumber": 17,
                    "question": "Dans quelle phase du sommeil l'activité cérébrale est-elle la plus intense ?",
                    "answerOptions": [
                        {"text": "Durant le sommeil paradoxal propice aux rêves", "isCorrect": True},
                        {"text": "Durant le sommeil lent léger de début de nuit", "isCorrect": False},
                        {"text": "Durant le sommeil lent profond réparateur", "isCorrect": False},
                        {"text": "Durant les périodes d'insomnie en milieu de nuit", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Durant le sommeil paradoxal, le cerveau est très actif alors que les muscles sont totalement relâchés (paralysie musculaire). C'est la phase où l'on traite les émotions et les souvenirs."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel nutriment minéral assure la solidité du squelette ?",
                    "answerOptions": [
                        {"text": "Le calcium présent dans les laitages et certaines eaux", "isCorrect": True},
                        {"text": "Le fer présent dans les viandes rouges et épinards", "isCorrect": False},
                        {"text": "La vitamine C présente dans les agrumes frais", "isCorrect": False},
                        {"text": "Les fibres présentes dans les céréales complètes", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le calcium est le constituant majeur des os et des dents. Un apport suffisant, dès l'enfance et à l'adolescence, est crucial pour prévenir l'ostéoporose plus tard."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'intérêt sanitaire majeur d'aérer son logement quotidiennement ?",
                    "answerOptions": [
                        {"text": "Renouveler l'oxygène et chasser les polluants intérieurs", "isCorrect": True},
                        {"text": "Faire baisser la température des murs en été chaud", "isCorrect": False},
                        {"text": "Laisser entrer la poussière naturelle de la rue passante", "isCorrect": False},
                        {"text": "Chasser les insectes volants comme les mouches", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'air intérieur est souvent 5 à 10 fois plus pollué que l'air extérieur (meubles, produits ménagers, humidité). L'aération évite l'accumulation de CO2 et de moisissures."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le rôle de la mélanine présente dans les cellules de la peau ?",
                    "answerOptions": [
                        {"text": "Filtre naturel contre les rayons ultraviolets dangereux", "isCorrect": True},
                        {"text": "Barrière imperméable contre la pénétration de l'eau", "isCorrect": False},
                        {"text": "Système de régulation de la transpiration excessive", "isCorrect": False},
                        {"text": "Système de transport du sang dans les capillaires", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La mélanine donne son bronzage à la peau. Elle absorbe une partie des rayons UV du soleil pour protéger l'ADN des cellules, mais cette protection est limitée et nécessite l'usage de crème solaire."
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
                    "question": "Quelle est la définition d'une charge fixe dans un budget personnel ?",
                    "answerOptions": [
                        {"text": "Une dépense régulière et prévisible comme le loyer", "isCorrect": True},
                        {"text": "Un achat coup de cœur imprévu en centre commercial", "isCorrect": False},
                        {"text": "La facture de carburant qui varie selon les trajets", "isCorrect": False},
                        {"text": "Un cadeau offert lors d'un repas d'anniversaire", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les charges fixes (loyer, assurances, abonnements) sont prioritaires. Il faut les payer avant de consacrer de l'argent aux charges variables (alimentation) ou aux loisirs."
                },
                {
                    "questionNumber": 22,
                    "question": "Que représente le TAEG sur un contrat de crédit à la consommation ?",
                    "answerOptions": [
                        {"text": "Le coût total annuel du crédit tout compris", "isCorrect": True},
                        {"text": "Le tarif d'achat électrique garanti par l'État", "isCorrect": False},
                        {"text": "Le taux d'assurance en groupe proposé au client", "isCorrect": False},
                        {"text": "La taxe sur l'argent emprunté lors d'une vente", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le Taux Annuel Effectif Global inclut les intérêts, les frais de dossier et l'assurance. C'est l'indicateur unique pour comparer deux offres de prêt différentes."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel document financier permet de prévoir ses ressources et dépenses ?",
                    "answerOptions": [
                        {"text": "Un budget prévisionnel mensuel ou annuel", "isCorrect": True},
                        {"text": "Une fiche de paie reçue de l'employeur actuel", "isCorrect": False},
                        {"text": "Un relevé d'identité bancaire pour un virement", "isCorrect": False},
                        {"text": "Un contrat de travail signé pour un poste fixe", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Tenir son budget permet d'éviter le découvert bancaire et les agios. On soustrait les dépenses des revenus pour connaître le 'reste à vivre'."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le délai légal de rétractation après un achat sur internet ?",
                    "answerOptions": [
                        {"text": "Une durée de quatorze jours calendaires entiers", "isCorrect": True},
                        {"text": "Une durée de deux jours ouvrables seulement", "isCorrect": False},
                        {"text": "Une durée de trente jours calendaires entiers", "isCorrect": False},
                        {"text": "Il n'y a aucun droit de retour pour le numérique", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La loi Hamon protège l'acheteur à distance. On dispose de 14 jours pour changer d'avis, renvoyer le produit et être remboursé sans avoir à justifier de motif."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment appelle-t-on la somme d'argent qu'il reste pour les loisirs ?",
                    "answerOptions": [
                        {"text": "Le reste à vivre après les charges obligatoires", "isCorrect": True},
                        {"text": "Le montant du salaire brut avant les cotisations", "isCorrect": False},
                        {"text": "Le prix total affiché sur le chariot de courses", "isCorrect": False},
                        {"text": "L'argent placé sur un livret d'épargne bancaire", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le 'reste à vivre' est ce qu'il vous reste une fois que le logement, les factures (eau, électricité) et les assurances sont payés. Il sert à manger et à sortir."
                },
                {
                    "questionNumber": 26,
                    "question": "Vers quel organisme se tourner en cas de dettes impossibles à payer ?",
                    "answerOptions": [
                        {"text": "La commission de surendettement de la Banque de France", "isCorrect": True},
                        {"text": "La mairie de la commune de résidence actuelle", "isCorrect": False},
                        {"text": "Le commissariat de police de la ville locale", "isCorrect": False},
                        {"text": "Le service de recherche de pôle emploi ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si un particulier ne peut plus payer ses dettes non professionnelles, il peut déposer un dossier. La commission propose alors un plan de remboursement ou un effacement des dettes."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la garantie principale offerte par le label AB ?",
                    "answerOptions": [
                        {"text": "Produit cultivé sans engrais ni pesticides de synthèse", "isCorrect": True},
                        {"text": "Produit vendu au prix le plus bas du marché actuel", "isCorrect": False},
                        {"text": "Produit fabriqué exclusivement sur le sol français", "isCorrect": False},
                        {"text": "Produit ne contenant absolument aucune calorie", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le label Agriculture Biologique garantit que 95 % au moins des composants sont bio. Il interdit les OGM et limite drastiquement les traitements chimiques."
                },
                {
                    "questionNumber": 28,
                    "question": "Que couvre l'assurance 'Responsabilité Civile' obligatoire ?",
                    "answerOptions": [
                        {"text": "Les dommages causés involontairement à une autre personne", "isCorrect": True},
                        {"text": "Les frais médicaux personnels après une hospitalisation", "isCorrect": False},
                        {"text": "La protection des biens mobiliers contre le vol domestique", "isCorrect": False},
                        {"text": "L'achat d'un nouveau véhicule après une panne moteur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Cette assurance est vitale. Si vous cassez un objet de valeur chez quelqu'un ou si vous blessez quelqu'un par inadvertance, c'est l'assurance qui paiera l'indemnisation à votre place."
                },
                {
                    "questionNumber": 29,
                    "question": "Qu'est-ce que l'éco-consommation au quotidien ?",
                    "answerOptions": [
                        {"text": "Choisir des produits en limitant leur impact sur la nature", "isCorrect": True},
                        {"text": "Ne plus rien acheter du tout pour économiser l'argent", "isCorrect": False},
                        {"text": "Acheter uniquement des articles importés par voie aérienne", "isCorrect": False},
                        {"text": "Multiplier les emballages plastiques pour plus d'hygiène", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est une démarche citoyenne qui privilégie les produits de saison, locaux, durables et avec le moins d'emballages possible."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle mention doit obligatoirement figurer sur un emballage alimentaire ?",
                    "answerOptions": [
                        {"text": "La liste complète des ingrédients et allergènes", "isCorrect": True},
                        {"text": "La photo du producteur ou du gérant de l'usine", "isCorrect": False},
                        {"text": "Le nom du chauffeur qui a transporté le produit", "isCorrect": False},
                        {"text": "Les prévisions météo du jour de la mise en boîte", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La liste des ingrédients est classée par ordre décroissant de poids. Les allergènes (arachide, lait, gluten) doivent être écrits en gras ou soulignés."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le message d'un Nutri-Score classé 'E' sur un produit ?",
                    "answerOptions": [
                        {"text": "Qualité nutritionnelle médiocre car trop gras ou sucré", "isCorrect": True},
                        {"text": "Produit excellent pour la santé et la croissance", "isCorrect": False},
                        {"text": "Produit sans aucun danger pour la consommation", "isCorrect": False},
                        {"text": "Produit issu exclusivement du commerce équitable", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le Nutri-Score aide à comparer deux produits de même rayon. Un classement 'E' (orange foncé) indique une forte densité calorique, de sel ou d'acides gras saturés."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle somme est-il conseillé de mettre de côté pour son épargne de précaution ?",
                    "answerOptions": [
                        {"text": "L'équivalent de deux à trois mois de salaire mensuel", "isCorrect": True},
                        {"text": "L'équivalent de dix ans de revenus du foyer actuel", "isCorrect": False},
                        {"text": "Juste assez pour payer le prochain ticket de cinéma", "isCorrect": False},
                        {"text": "L'intégralité du salaire dès qu'il est versé par le patron", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Cette réserve permet de payer une réparation urgente (voiture, machine à laver) ou de faire face à une baisse de revenus imprévue sans s'endetter."
                },
                {
                    "questionNumber": 33,
                    "question": "Comment définit-on légalement une publicité mensongère ?",
                    "answerOptions": [
                        {"text": "Une annonce donnant des informations fausses ou trompeuses", "isCorrect": True},
                        {"text": "Une annonce qui dure plus de trente secondes à la radio", "isCorrect": False},
                        {"text": "Une annonce pour un produit qui est totalement gratuit", "isCorrect": False},
                        {"text": "Une annonce affichée uniquement dans les gares de train", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est un délit. La loi interdit de mentir sur les caractéristiques réelles du produit, son prix ou les résultats attendus de son utilisation."
                },
                {
                    "questionNumber": 34,
                    "question": "Que signifie l'obsolescence programmée d'un appareil ?",
                    "answerOptions": [
                        {"text": "Réduire volontairement sa durée de vie pour en vendre un neuf", "isCorrect": True},
                        {"text": "Réparer gratuitement une machine pour aider le client", "isCorrect": False},
                        {"text": "Le fait qu'un produit soit devenu démodé avec le temps", "isCorrect": False},
                        {"text": "L'attribution d'une garantie totale de dix ans d'usage", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Interdite par la loi, cette pratique consiste à utiliser des composants fragiles ou des logiciels qui ralentissent l'appareil pour forcer le rachat."
                },
                {
                    "questionNumber": 35,
                    "question": "Pourquoi le prix au kilo est-il l'indicateur le plus fiable ?",
                    "answerOptions": [
                        {"text": "Il permet de comparer le coût réel malgré les emballages", "isCorrect": True},
                        {"text": "Il aide à apprendre les mathématiques au quotidien", "isCorrect": False},
                        {"text": "Il indique si le paquet est trop lourd à porter seul", "isCorrect": False},
                        {"text": "Il permet de vérifier le prestige de la marque choisie", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le marketing joue sur la taille des paquets. Seul le prix au kilo (ou au litre) permet de voir qu'un petit format est souvent plus cher que le format standard."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est la valeur juridique du ticket de caisse ?",
                    "answerOptions": [
                        {"text": "Il sert de preuve d'achat pour l'échange ou la garantie", "isCorrect": True},
                        {"text": "Il sert de support publicitaire pour les marques locales", "isCorrect": False},
                        {"text": "Il sert à vérifier l'heure de sortie exacte du magasin", "isCorrect": False},
                        {"text": "Il ne possède aucune utilité réelle pour le consommateur", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Sans ticket de caisse, il est très difficile de prouver que vous avez acheté l'objet. Il est indispensable pour faire jouer la garantie légale de 2 ans."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'engagement premier du commerce équitable ?",
                    "answerOptions": [
                        {"text": "Assurer une juste rémunération aux petits producteurs", "isCorrect": True},
                        {"text": "Vendre les articles le moins cher possible pour le client", "isCorrect": False},
                        {"text": "Organiser des échanges de produits entre voisins proches", "isCorrect": False},
                        {"text": "Appartenir obligatoirement à l'État de la zone concernée", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Ce système garantit que les paysans du Sud (café, chocolat, coton) ne sont pas exploités et peuvent vivre dignement de leur travail."
                },
                {
                    "questionNumber": 38,
                    "question": "Combien de temps dure la garantie légale de conformité en France ?",
                    "answerOptions": [
                        {"text": "Une durée totale de deux ans pour tout bien neuf", "isCorrect": True},
                        {"text": "Une durée totale de six mois pour tout bien neuf", "isCorrect": False},
                        {"text": "Une durée totale de dix ans pour l'ensemble des biens", "isCorrect": False},
                        {"text": "Une durée totale de un mois pour les vêtements neufs", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si votre lave-linge tombe en panne après 18 mois, le vendeur doit le réparer ou le remplacer gratuitement (sauf si vous avez fait une mauvaise utilisation)."
                },
                {
                    "questionNumber": 39,
                    "question": "Qu'est-ce qu'un prélèvement automatique bancaire ?",
                    "answerOptions": [
                        {"text": "Le paiement automatique d'une facture récurrente de zone", "isCorrect": True},
                        {"text": "Un retrait d'argent liquide au distributeur automatique", "isCorrect": False},
                        {"text": "Une erreur informatique de la banque lors d'un transfert", "isCorrect": False},
                        {"text": "Une prise de sang réalisée par un infirmier à l'hôpital", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Il évite les oublis de paiement pour le téléphone, l'électricité ou le loyer. Il peut être annulé (révoqué) à tout moment par le client."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel risque social est associé aux jeux d'argent ?",
                    "answerOptions": [
                        {"text": "Le risque d'addiction et d'endettement rapide du joueur", "isCorrect": True},
                        {"text": "Le risque de devenir trop riche en très peu de temps", "isCorrect": False},
                        {"text": "Le risque de se faire trop d'amis durant les parties", "isCorrect": False},
                        {"text": "Le risque de perdre son ticket dans la rue passante", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'addiction au jeu est une pathologie qui détruit la vie de famille et conduit souvent à emprunter de l'argent de façon désespérée (surendettement)."
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
                    "question": "Quel gaz est le premier responsable de l'effet de serre humain ?",
                    "answerOptions": [
                        {"text": "Le dioxyde de carbone rejeté par les usines", "isCorrect": True},
                        {"text": "L'oxygène pur présent dans l'air ambiant ici", "isCorrect": False},
                        {"text": "L'hélium utilisé pour gonfler les ballons de fête", "isCorrect": False},
                        {"text": "L'azote liquide utilisé dans la recherche médicale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le CO2 provient principalement de la combustion du pétrole, du charbon et du gaz. En s'accumulant, il forme un 'couvercle' qui retient la chaleur terrestre."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est l'intérêt écologique majeur du tri sélectif ?",
                    "answerOptions": [
                        {"text": "Économiser les matières premières par le recyclage", "isCorrect": True},
                        {"text": "Rendre les poubelles plus esthétiques dans les rues", "isCorrect": False},
                        {"text": "Remplir les décharges publiques de plus en plus vite", "isCorrect": False},
                        {"text": "Pratiquer une activité physique en portant les sacs", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Recycler une tonne d'acier ou de papier évite de couper de nouveaux arbres ou de creuser de nouvelles mines. Cela préserve les ressources de la Terre."
                },
                {
                    "questionNumber": 43,
                    "question": "Comment définit-on l'empreinte carbone d'une activité ?",
                    "answerOptions": [
                        {"text": "La quantité totale de gaz à effet de serre émise", "isCorrect": True},
                        {"text": "La trace d'un pas de chaussure dans le charbon noir", "isCorrect": False},
                        {"text": "Le prix de vente officiel de la tonne de charbon", "isCorrect": False},
                        {"text": "La couleur sombre d'un emballage cartonné recyclé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Elle permet de mesurer l'impact climatique d'un trajet en avion, de la fabrication d'un smartphone ou de la production d'un steak de bœuf."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel geste simple réduit la consommation électrique à la maison ?",
                    "answerOptions": [
                        {"text": "Éteindre systématiquement les appareils en veille", "isCorrect": True},
                        {"text": "Laisser l'ensemble des lumières allumées la journée", "isCorrect": False},
                        {"text": "Ouvrir les fenêtres quand le chauffage est au maximum", "isCorrect": False},
                        {"text": "Utiliser un réfrigérateur très ancien qui ferme mal", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les veilles (TV, ordinateurs, chargeurs) peuvent représenter jusqu'à 10 % de la facture d'électricité. Les éteindre est un geste facile pour le budget et la planète."
                },
                {
                    "questionNumber": 45,
                    "question": "Où doit-on jeter les boîtes de conserve en métal vides ?",
                    "answerOptions": [
                        {"text": "Dans le bac jaune réservé aux emballages", "isCorrect": True},
                        {"text": "Dans le bac vert réservé uniquement au verre", "isCorrect": False},
                        {"text": "Dans le bac gris réservé aux ordures ménagères", "isCorrect": False},
                        {"text": "Il est interdit de jeter du métal à la poubelle", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'acier et l'aluminium des conserves et canettes sont recyclables à l'infini. Ils doivent être mis dans le bac de tri (souvent jaune)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la caractéristique d'une énergie renouvelable ?",
                    "answerOptions": [
                        {"text": "C'est une source qui ne s'épuise pas avec le temps", "isCorrect": True},
                        {"text": "C'est une énergie que l'on doit acheter à nouveau", "isCorrect": False},
                        {"text": "Cela désigne exclusivement le pétrole et le gaz", "isCorrect": False},
                        {"text": "Cela désigne l'électricité fournie par les piles", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le vent (éolien), le soleil (solaire) et l'eau (hydraulique) sont des énergies propres et inépuisables à l'échelle de l'histoire humaine."
                },
                {
                    "questionNumber": 47,
                    "question": "Pourquoi le gaspillage alimentaire est-il une faute écologique ?",
                    "answerOptions": [
                        {"text": "Car produire ce repas a consommé de l'eau inutilement", "isCorrect": True},
                        {"text": "Parce que c'est une attitude considérée comme impolie", "isCorrect": False},
                        {"text": "Pour éviter que les poubelles sentent mauvais dehors", "isCorrect": False},
                        {"text": "Cela n'a absolument aucun impact sur l'environnement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Jeter un aliment, c'est jeter toute l'énergie du transport, les engrais et les milliers de litres d'eau utilisés pour le faire pousser."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est l'objectif central du développement durable ?",
                    "answerOptions": [
                        {"text": "Satisfaire nos besoins sans compromettre ceux des futurs", "isCorrect": True},
                        {"text": "Arrêter définitivement toute forme d'activité économique", "isCorrect": False},
                        {"text": "Augmenter le prix des produits pour les rendre rares", "isCorrect": False},
                        {"text": "Consommer toutes les ressources terrestres maintenant", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Il repose sur trois piliers indissociables : l'économie (produire), le social (partager) et l'environnement (protéger)."
                },
                {
                    "questionNumber": 49,
                    "question": "Que garantit l'Écolabel européen sur un produit ?",
                    "answerOptions": [
                        {"text": "Un impact environnemental réduit durant toute sa vie", "isCorrect": True},
                        {"text": "La gratuité totale du produit pour le consommateur", "isCorrect": False},
                        {"text": "La fabrication du produit uniquement à la main", "isCorrect": False},
                        {"text": "Que le produit a été testé sur des fleurs sauvages", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Ce label officiel prend en compte tout le cycle de vie : extraction des matières, fabrication, transport, utilisation et fin de vie (déchet)."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment nomme-t-on la perte de la variété des espèces ?",
                    "answerOptions": [
                        {"text": "L'érosion de la biodiversité mondiale", "isCorrect": True},
                        {"text": "Le changement naturel des quatre saisons", "isCorrect": False},
                        {"text": "Le phénomène de métamorphose animale", "isCorrect": False},
                        {"text": "Le clonage scientifique des cellules souches", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La destruction des forêts, la pollution et le climat font disparaître les espèces à une vitesse record, ce qui menace les ressources alimentaires et médicales de l'homme."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est l'avantage de consommer des fruits de saison ?",
                    "answerOptions": [
                        {"text": "Limiter les transports lointains et les serres chauffées", "isCorrect": True},
                        {"text": "Parce qu'ils ont des couleurs beaucoup plus jolies", "isCorrect": False},
                        {"text": "Pour pouvoir payer une taxe carbone plus élevée ici", "isCorrect": False},
                        {"text": "Car les fruits hors saison n'ont aucun goût sucré", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Consommer des fraises en hiver nécessite soit un transport par avion (très polluant), soit des serres chauffées au gaz. Manger de saison est un acte citoyen simple."
                },
                {
                    "questionNumber": 52,
                    "question": "Que doit-on faire des batteries et piles usagées ?",
                    "answerOptions": [
                        {"text": "Les rapporter dans des points de collecte spécifiques", "isCorrect": True},
                        {"text": "Les jeter avec les ordures ménagères classiques", "isCorrect": False},
                        {"text": "Les brûler dans une cheminée ou un poêle à bois", "isCorrect": False},
                        {"text": "Les enterrer dans le sol du jardin potager privé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Elles contiennent des métaux lourds (mercure, lithium) extrêmement toxiques pour les nappes phréatiques s'ils fuient dans la nature."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle pollution majeure est issue du transport routier ?",
                    "answerOptions": [
                        {"text": "Le rejet de particules fines et de gaz carbonique", "isCorrect": True},
                        {"text": "La pollution sonore par les klaxons uniquement ici", "isCorrect": False},
                        {"text": "Une dégradation visuelle de l'ensemble des routes", "isCorrect": False},
                        {"text": "Une consommation d'eau potable excessive par jour", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les gaz d'échappement dégradent la qualité de l'air des villes et provoquent des maladies respiratoires (asthme) tout en aggravant l'effet de serre."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'objectif premier du compostage domestique ?",
                    "answerOptions": [
                        {"text": "Transformer les biodéchets en engrais naturel gratuit", "isCorrect": True},
                        {"text": "Trouver un remplaçant pour les sacs en plastique", "isCorrect": False},
                        {"text": "Produire une quantité faible d'électricité locale", "isCorrect": False},
                        {"text": "Éliminer l'ensemble des insectes du jardin potager", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le compostage permet de réduire de 30 % le poids de notre poubelle grise en valorisant les épluchures et restes de repas."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est la part d'eau douce liquide sur la planète ?",
                    "answerOptions": [
                        {"text": "Moins de trois pour cent de la totalité de l'eau", "isCorrect": True},
                        {"text": "Près de cinquante pour cent de la totalité de l'eau", "isCorrect": False},
                        {"text": "Exactement autant que l'ensemble de l'eau salée", "isCorrect": False},
                        {"text": "L'eau est une ressource infinie et inépuisable ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'eau potable est rare. La majeure partie de l'eau sur Terre est salée (océans). L'eau douce est souvent bloquée dans les glaces ou profonde sous terre."
                },
                {
                    "questionNumber": 56,
                    "question": "Pourquoi les plastiques dans l'océan sont-ils dangereux ?",
                    "answerOptions": [
                        {"text": "Ils intoxiquent les animaux et la chaîne alimentaire", "isCorrect": True},
                        {"text": "Ils finissent par rendre l'eau de mer beaucoup plus bleue", "isCorrect": False},
                        {"text": "Ils servent de nourriture saine pour les poissons locaux", "isCorrect": False},
                        {"text": "Ils disparaissent par miracle en moins de deux jours", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les plastiques ne disparaissent jamais vraiment, ils se brisent en micro-plastiques que les poissons avalent. On finit par les retrouver dans nos propres assiettes."
                },
                {
                    "questionNumber": 57,
                    "question": "Que signifie le logo 'Point Vert' sur un emballage ?",
                    "answerOptions": [
                        {"text": "L'entreprise paie une taxe pour financer le tri sélectif", "isCorrect": True},
                        {"text": "L'objet est intégralement composé de matière recyclée", "isCorrect": False},
                        {"text": "L'objet est biodégradable dans la nature en un mois", "isCorrect": False},
                        {"text": "Le produit est garanti issu de l'agriculture bio ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est un logo financier : il ne signifie pas que le produit est recyclé ou recyclable, mais que le fabricant contribue financièrement au système de tri des déchets."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est l'impact de la déforestation tropicale ?",
                    "answerOptions": [
                        {"text": "Une hausse du CO2 et une perte d'habitat animal", "isCorrect": True},
                        {"text": "Une meilleure vue sur l'ensemble des montagnes", "isCorrect": False},
                        {"text": "L'extension des zones désertiques pour le tourisme", "isCorrect": False},
                        {"text": "Une amélioration durable de la fertilité des sols", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les forêts sont des 'puits de carbone'. Les détruire accélère le réchauffement climatique et fait disparaître des espèces uniques."
                },
                {
                    "questionNumber": 59,
                    "question": "Qu'est-ce que la vente en 'circuit court' ?",
                    "answerOptions": [
                        {"text": "Un seul intermédiaire maximum entre producteur et client", "isCorrect": True},
                        {"text": "Un marathon de cinq kilomètres organisé en ville", "isCorrect": False},
                        {"text": "Une panne électrique majeure dans une cuisine moderne", "isCorrect": False},
                        {"text": "Le fait d'acheter ses produits au grand supermarché", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le circuit court (AMAP, vente à la ferme) assure un meilleur revenu au paysan et limite les gaz à effet de serre liés au transport."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment limiter l'impact écologique de ses emails ?",
                    "answerOptions": [
                        {"text": "Supprimer les messages inutiles et les grosses pièces jointes", "isCorrect": True},
                        {"text": "Changer son smartphone par un modèle neuf tous les ans", "isCorrect": False},
                        {"text": "Laisser l'ensemble des ordinateurs allumés toute la nuit", "isCorrect": False},
                        {"text": "Envoyer systématiquement cinq cents emails chaque jour", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le stockage des données dans des 'Data Centers' consomme énormément d'électricité. Trier sa boîte mail réduit cette dépense énergétique invisible."
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
                    "question": "Quel contrat de travail est la forme normale de l'emploi ?",
                    "answerOptions": [
                        {"text": "Le Contrat à Durée Indéterminée désigné par CDI", "isCorrect": True},
                        {"text": "Le Contrat à Durée Déterminée pour une mission seule", "isCorrect": False},
                        {"text": "Le Contrat de Travail Temporaire utilisé en intérim", "isCorrect": False},
                        {"text": "Le Contrat de Stage effectué pendant les études", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le CDI est la norme. Il garantit une stabilité d'emploi car il n'a pas de date de fin. Le CDD doit rester une exception pour un besoin ponctuel."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la durée légale du travail par semaine en France ?",
                    "answerOptions": [
                        {"text": "Une durée de trente-cinq heures par semaine", "isCorrect": True},
                        {"text": "Une durée de trente-neuf heures par semaine", "isCorrect": False},
                        {"text": "Une durée de quarante-huit heures par semaine", "isCorrect": False},
                        {"text": "Une durée de vingt heures par semaine seulement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** 35 heures est la durée de référence. Les heures effectuées au-delà sont des 'heures supplémentaires' payées plus cher ou récupérées en repos."
                },
                {
                    "questionNumber": 63,
                    "question": "À quoi correspond le 'salaire brut' sur un bulletin de paie ?",
                    "answerOptions": [
                        {"text": "Le salaire total avant déduction des cotisations", "isCorrect": True},
                        {"text": "La somme nette qui arrive sur le compte en banque", "isCorrect": False},
                        {"text": "Le montant des pourboires donnés par les clients", "isCorrect": False},
                        {"text": "Le montant du salaire minimum légal uniquement", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On retire du salaire brut les cotisations sociales (retraite, chômage, santé) pour obtenir le salaire net, qui est celui que l'on perçoit réellement."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle instance représente les salariés dans les entreprises de plus de 11 salariés ?",
                    "answerOptions": [
                        {"text": "Le Comité Social et Économique désigné par CSE", "isCorrect": True},
                        {"text": "Le Tribunal de Grande Instance de la ville locale", "isCorrect": False},
                        {"text": "La Caisse d'Allocations Familiales départementale", "isCorrect": False},
                        {"text": "La direction des ressources humaines de la firme", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le CSE remplace les anciens délégués du personnel. Il est consulté sur l'organisation du travail, les conditions de santé et la sécurité."
                },
                {
                    "questionNumber": 65,
                    "question": "Qu'est-ce qu'une Convention Collective ?",
                    "answerOptions": [
                        {"text": "Un accord adaptant le droit au secteur d'activité", "isCorrect": True},
                        {"text": "Un livre sur les règles de politesse au bureau", "isCorrect": False},
                        {"text": "Le simple règlement intérieur de l'entreprise ici", "isCorrect": False},
                        {"text": "Une réunion annuelle de l'ensemble des salariés", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Chaque métier (BTP, Coiffure, Restauration) a sa convention. Elle propose souvent des droits plus avantageux que le Code du travail (primes, jours de congés)."
                },
                {
                    "questionNumber": 66,
                    "question": "À quoi sert principalement la période d'essai au début du contrat ?",
                    "answerOptions": [
                        {"text": "Permettre à chacun de tester ses compétences et le poste", "isCorrect": True},
                        {"text": "Travailler gratuitement pour apprendre les bases ici", "isCorrect": False},
                        {"text": "Forcer le salarié à acheter ses propres outils de zone", "isCorrect": False},
                        {"text": "Prendre deux semaines de vacances avant de commencer", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Durant cette période, l'employeur ou le salarié peut mettre fin au contrat sans préavis ni motif, afin de vérifier si le recrutement est réussi."
                },
                {
                    "questionNumber": 67,
                    "question": "Que signifie précisément le sigle SMIC ?",
                    "answerOptions": [
                        {"text": "Salaire Minimum Interprofessionnel de Croissance", "isCorrect": True},
                        {"text": "Système de Mesure de l'Indice de Consommation", "isCorrect": False},
                        {"text": "Seuil de Mobilité Individuelle Court pour l'emploi", "isCorrect": False},
                        {"text": "Salaire Moyen de l'Industrie et du Commerce national", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est le montant horaire en dessous duquel il est interdit de rémunérer un salarié en France. Il est revalorisé selon l'inflation."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel document est obligatoirement remis au salarié à la fin du contrat ?",
                    "answerOptions": [
                        {"text": "Le certificat de travail et l'attestation pôle emploi", "isCorrect": True},
                        {"text": "Le double de l'ensemble des clés de l'entreprise", "isCorrect": False},
                        {"text": "Une lettre de recommandation obligatoire du patron", "isCorrect": False},
                        {"text": "Un chèque cadeau pour les prochaines vacances ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Ces documents permettent de prouver son expérience et de s'inscrire pour percevoir les allocations chômage si les conditions sont remplies."
                },
                {
                    "questionNumber": 69,
                    "question": "Qu'est-ce qu'une maladie professionnelle selon la loi ?",
                    "answerOptions": [
                        {"text": "Une pathologie causée par l'exercice prolongé d'un métier", "isCorrect": True},
                        {"text": "Une blessure survenue soudainement lors d'une tâche", "isCorrect": False},
                        {"text": "Le fait d'attraper froid sur le chantier en hiver", "isCorrect": False},
                        {"text": "Un accident de voiture en allant au travail le matin", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La maladie professionnelle (ex: tendinites, silicose) résulte d'une exposition répétée à un risque physique ou chimique lié au poste de travail."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel organisme remplace Pôle Emploi depuis 2024 ?",
                    "answerOptions": [
                        {"text": "L'organisme nommé France Travail", "isCorrect": True},
                        {"text": "L'organisme nommé la Sécurité Sociale", "isCorrect": False},
                        {"text": "L'organisme nommé le Conseil de Prud'hommes", "isCorrect": False},
                        {"text": "L'organisme nommé la Mairie de la ville", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** France Travail accompagne les chômeurs, centralise les offres d'emploi et verse les indemnités selon les droits acquis par les anciens salariés."
                },
                {
                    "questionNumber": 71,
                    "question": "Que signifie être officiellement 'salarié' ?",
                    "answerOptions": [
                        {"text": "Travailler sous l'autorité d'un employeur pour un salaire", "isCorrect": True},
                        {"text": "Travailler sans être payé pour apprendre un nouveau métier", "isCorrect": False},
                        {"text": "Être son propre patron et gérer ses clients seul", "isCorrect": False},
                        {"text": "Travailler pour quelqu'un sans aucun contrat écrit", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le salariat se définit par le lien de subordination (recevoir des ordres) et la rémunération prévue par un contrat de travail."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel tribunal traite les litiges entre employeur et salarié ?",
                    "answerOptions": [
                        {"text": "Le Conseil de Prud'hommes de la ville", "isCorrect": True},
                        {"text": "Le Tribunal Correctionnel de la ville locale", "isCorrect": False},
                        {"text": "Le Tribunal de Commerce de la grande cité", "isCorrect": False},
                        {"text": "La Cour d'Appel administrative régionale ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Ce tribunal est paritaire (moitié patrons, moitié salariés). Il intervient pour les licenciements abusifs ou les salaires non payés."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la mission de la Médecine du Travail ?",
                    "answerOptions": [
                        {"text": "Prévenir l'altération de la santé due aux conditions", "isCorrect": True},
                        {"text": "Soigner les grippes et rhumes de l'ensemble des salariés", "isCorrect": False},
                        {"text": "Sanctionner les ouvriers qui sont souvent malades", "isCorrect": False},
                        {"text": "Distribuer des médicaments gratuitement chaque matin", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le médecin du travail vérifie que le salarié est apte à son poste et conseille l'employeur sur l'aménagement ergonomique des postes."
                },
                {
                    "questionNumber": 74,
                    "question": "À quoi sert le règlement intérieur d'une entreprise ?",
                    "answerOptions": [
                        {"text": "Fixer les règles de discipline, d'hygiène et de sécurité", "isCorrect": True},
                        {"text": "Donner les meilleures recettes de cuisine de la cantine", "isCorrect": False},
                        {"text": "Lister l'ensemble des numéros de téléphone des clients", "isCorrect": False},
                        {"text": "Vendre des produits dérivés aux employés de la zone", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Il est obligatoire à partir de 50 salariés. Il définit les sanctions possibles en cas de faute et les règles de sécurité à respecter."
                },
                {
                    "questionNumber": 75,
                    "question": "Qu'est-ce qu'une faute grave au travail ?",
                    "answerOptions": [
                        {"text": "Un comportement rendant impossible le maintien au poste", "isCorrect": True},
                        {"text": "Arriver une seule fois avec deux minutes de retard", "isCorrect": False},
                        {"text": "Faire une petite erreur de calcul sans aucune importance", "isCorrect": False},
                        {"text": "Demander poliment une augmentation de salaire net", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Vol, violence ou abandon de poste sont des fautes graves. Elles entraînent le départ immédiat sans indemnités de licenciement."
                },
                {
                    "questionNumber": 76,
                    "question": "Que signifie concrètement le droit de retrait ?",
                    "answerOptions": [
                        {"text": "Arrêter le travail face à un danger grave et imminent", "isCorrect": True},
                        {"text": "Prendre sa retraite de manière anticipée à cinquante ans", "isCorrect": False},
                        {"text": "Retirer de l'argent liquide au distributeur automatique", "isCorrect": False},
                        {"text": "Ne pas venir travailler parce qu'il pleut trop dehors", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si un salarié pense que sa vie est en danger immédiat (ex: machine défectueuse), il peut cesser le travail sans être puni, à condition de prévenir son patron."
                },
                {
                    "questionNumber": 77,
                    "question": "Combien de jours de congés payés gagne un salarié par mois travaillé ?",
                    "answerOptions": [
                        {"text": "Une durée de deux virgule cinq jours", "isCorrect": True},
                        {"text": "Une durée de un jour entier seulement", "isCorrect": False},
                        {"text": "Une durée de cinq jours entiers travaillés", "isCorrect": False},
                        {"text": "Il n'y a aucun congé la toute première année", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Cela fait un total de 30 jours ouvrables par an (5 semaines). Les congés sont un droit acquis par le travail effectif."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est la différence entre un accident du travail et de trajet ?",
                    "answerOptions": [
                        {"text": "Le trajet a lieu entre la maison et le bureau habituel", "isCorrect": True},
                        {"text": "L'accident de trajet n'est jamais remboursé par l'État", "isCorrect": False},
                        {"text": "L'accident du travail arrive uniquement à son bureau", "isCorrect": False},
                        {"text": "Il n'existe aucune différence légale entre les deux", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'accident de trajet (sur le chemin direct vers l'usine) est protégé de la même manière que l'accident survenu sur le poste de travail."
                },
                {
                    "questionNumber": 79,
                    "question": "Que signifie l'appellation 'CDD d'usage' ?",
                    "answerOptions": [
                        {"text": "Un contrat court pour des secteurs spécifiques (extras)", "isCorrect": True},
                        {"text": "Un contrat pour apprendre à utiliser une machine neuve", "isCorrect": False},
                        {"text": "Un contrat qui possède une durée de dix ans fermes", "isCorrect": False},
                        {"text": "Un contrat réservé exclusivement aux jeunes stagiaires", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est un CDD utilisé dans la restauration, le spectacle ou l'audiovisuel où il est d'usage de ne pas recruter en CDI pour des missions brèves."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la mission dévolue à un syndicat ?",
                    "answerOptions": [
                        {"text": "Défendre les droits et les intérêts de tous les travailleurs", "isCorrect": True},
                        {"text": "Organiser l'ensemble des vacances du grand patron ici", "isCorrect": False},
                        {"text": "Payer l'ensemble des amendes privées des salariés locaux", "isCorrect": False},
                        {"text": "Remplacer le rôle du médecin du travail en entreprise", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les syndicats négocient les conditions de travail, assistent les salariés lors d'entretiens et peuvent déclencher des mouvements de grève."
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
                    "question": "Quel est l'ordre chronologique des actions du SST lors d'un secours ?",
                    "answerOptions": [
                        {"text": "Protéger - Examiner - Faire alerter - Secourir la victime", "isCorrect": True},
                        {"text": "Secourir - Alerter - Examiner - Partir vite du lieu noir", "isCorrect": False},
                        {"text": "Alerter - Protéger - Secourir - Examiner la plaie ouverte", "isCorrect": False},
                        {"text": "Examiner - Alerter - Secourir - Protéger le matériel neuf", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On protège d'abord pour éviter un sur-accident. Puis on examine pour savoir quoi dire au SAMU (15). L'alerte doit être rapide pour que les médecins arrivent vite."
                },
                {
                    "questionNumber": 82,
                    "question": "Que faire en premier si une victime s'étouffe totalement (silence total) ?",
                    "answerOptions": [
                        {"text": "Donner cinq claques vigoureuses entre les omoplates", "isCorrect": True},
                        {"text": "Lui proposer un grand verre d'eau fraîche immédiatement", "isCorrect": False},
                        {"text": "Allonger la personne directement par terre sur le sol", "isCorrect": False},
                        {"text": "Lui demander de lever les deux bras très haut ainsi", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si les claques ne fonctionnent pas, il faudra pratiquer la méthode de Heimlich (compressions abdominales) pour expulser l'objet coincé."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est l'action pour arrêter une hémorragie externe abondante ?",
                    "answerOptions": [
                        {"text": "Appuyer directement sur la plaie avec un linge propre", "isCorrect": True},
                        {"text": "Laisser couler le sang pour nettoyer la plaie naturellement", "isCorrect": False},
                        {"text": "Mettre de la farine sur la plaie pour boucher le trou", "isCorrect": False},
                        {"text": "Faire un garrot serré directement autour du cou du blessé", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La compression directe doit être maintenue jusqu'à l'arrivée des secours. Si la plaie contient un corps étranger (verre, couteau), on ne doit pas appuyer dessus."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment vérifier si une personne inconsciente respire encore ?",
                    "answerOptions": [
                        {"text": "Regarder le ventre bouger et sentir le souffle sur sa joue", "isCorrect": True},
                        {"text": "Lui crier très fort dans les oreilles pour la réveiller", "isCorrect": False},
                        {"text": "Lui pincer le bras pour voir si elle bouge la main", "isCorrect": False},
                        {"text": "Lui placer un petit miroir devant sa bouche fermée ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On bascule prudemment la tête en arrière pour dégager les voies aériennes et on observe pendant 10 secondes si la poitrine se soulève."
                },
                {
                    "questionNumber": 85,
                    "question": "Que faire si une victime est inconsciente mais qu'elle respire ?",
                    "answerOptions": [
                        {"text": "La placer en Position Latérale de Sécurité par terre", "isCorrect": True},
                        {"text": "Lui faire un massage cardiaque très énergique et rapide", "isCorrect": False},
                        {"text": "Lui donner un verre d'eau sucrée pour la réveiller", "isCorrect": False},
                        {"text": "La laisser sur le dos en attendant les pompiers ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La PLS permet de garder les voies respiratoires libres et d'éviter que la victime ne s'étouffe si elle vomit."
                },
                {
                    "questionNumber": 86,
                    "question": "Que faire face à une victime qui ne répond pas et ne respire plus ?",
                    "answerOptions": [
                        {"text": "Alerter les secours et débuter un massage cardiaque", "isCorrect": True},
                        {"text": "L'arroser d'eau froide pour provoquer un choc thermique", "isCorrect": False},
                        {"text": "Attendre dix minutes pour voir si elle reprend conscience", "isCorrect": False},
                        {"text": "Lui mettre une couverture chaude sur l'ensemble du corps", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Sans oxygène, le cerveau meurt en quelques minutes. Le massage cardiaque remplace le cœur pour envoyer du sang au cerveau en attendant le défibrillateur."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel appareil est indispensable lors d'un arrêt cardiaque ?",
                    "answerOptions": [
                        {"text": "Le Défibrillateur Automatisé Externe placé en ville", "isCorrect": True},
                        {"text": "Un thermomètre à mercure pour vérifier la fièvre", "isCorrect": False},
                        {"text": "Un ventilateur pour apporter de l'air frais au sujet", "isCorrect": False},
                        {"text": "Une balance médicale pour connaître le poids total", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le DAE donne des instructions vocales. Il analyse le cœur et ne délivre un choc électrique que si c'est strictement nécessaire pour relancer le rythme."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est la conduite à tenir pour une brûlure thermique simple ?",
                    "answerOptions": [
                        {"text": "Rincer à l'eau tempérée jusqu'à la fin de la douleur", "isCorrect": True},
                        {"text": "Appliquer du beurre ou du dentifrice sur la zone rouge", "isCorrect": False},
                        {"text": "Percer les cloques de liquide dès leur apparition rapide", "isCorrect": False},
                        {"text": "Mettre de la glace directement sur la peau brûlée vive", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** On rince à l'eau du robinet (15-25°C) pendant au moins 15 minutes. Cela arrête la progression de la chaleur dans les couches profondes de la peau."
                },
                {
                    "questionNumber": 89,
                    "question": "Que signifie un panneau de sécurité circulaire rouge barré ?",
                    "answerOptions": [
                        {"text": "Une interdiction formelle de faire une action précise", "isCorrect": True},
                        {"text": "Une obligation de porter un vêtement de sécurité bleu", "isCorrect": False},
                        {"text": "Une sortie de secours située à proximité immédiate ici", "isCorrect": False},
                        {"text": "Un danger électrique important lié à la machine locale", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le rouge sur un rond signifie toujours 'Interdit'. Exemple : Interdiction de fumer, interdiction de passer pour les piétons."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel risque est lié à l'usage prolongé d'un marteau-piqueur ?",
                    "answerOptions": [
                        {"text": "Des troubles articulaires et circulatoires des mains", "isCorrect": True},
                        {"text": "Une amélioration de la force du poignet et du bras", "isCorrect": False},
                        {"text": "Une perte de la vue par manque de lumière vive", "isCorrect": False},
                        {"text": "Le développement de caries dentaires sur les molaires", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les vibrations sont un risque physique professionnel. Elles peuvent causer le syndrome des 'doigts blancs' ou des douleurs chroniques aux articulations."
                },
                {
                    "questionNumber": 91,
                    "question": "Comment appelle-t-on l'outil d'analyse après un accident ?",
                    "answerOptions": [
                        {"text": "L'arbre des causes pour comprendre l'événement", "isCorrect": True},
                        {"text": "La météo des risques pour prévoir les futurs orages", "isCorrect": False},
                        {"text": "Le cercle de Sinner pour le nettoyage des sols gris", "isCorrect": False},
                        {"text": "La pyramide alimentaire pour les repas du midi local", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** L'arbre des causes permet de remonter tous les faits qui ont mené à l'accident afin de mettre en place des mesures pour que cela ne se reproduise plus."
                },
                {
                    "questionNumber": 92,
                    "question": "Qu'est-ce que le risque électrique au travail ?",
                    "answerOptions": [
                        {"text": "L'électrisation ou l'électrocution par un fil nu", "isCorrect": True},
                        {"text": "Le risque de tomber d'une échelle mal fixée au mur", "isCorrect": False},
                        {"text": "Le risque de manquer de lumière dans l'atelier sombre", "isCorrect": False},
                        {"text": "Le risque que la batterie du téléphone soit vide le soir", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le courant traverse le corps. L'électrisation est la blessure, l'électrocution est la mort provoquée par le choc électrique."
                },
                {
                    "questionNumber": 93,
                    "question": "Pourquoi le stress chronique est-il un risque professionnel ?",
                    "answerOptions": [
                        {"text": "Il cause des maladies cardiaques et des dépressions", "isCorrect": True},
                        {"text": "Il permet aux ouvriers de travailler beaucoup plus vite", "isCorrect": False},
                        {"text": "Il n'a aucun impact sur la santé physique du salarié", "isCorrect": False},
                        {"text": "Il fait grossir les personnes qui travaillent au bureau", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le stress prolongé libère du cortisol qui abîme le cœur et affaiblit le système immunitaire. C'est un Risque Psycho-Social (RPS) majeur."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel EPI protège les yeux des projections d'acide ?",
                    "answerOptions": [
                        {"text": "Les lunettes de protection intégrale ou visière", "isCorrect": True},
                        {"text": "Des lunettes de soleil classiques pour la plage", "isCorrect": False},
                        {"text": "Fermer les yeux très fort pendant le travail manuel", "isCorrect": False},
                        {"text": "Mettre un bonnet en laine sur le haut de la tête", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Une seule goutte d'acide dans l'œil peut causer une cécité définitive. La protection doit être étanche sur les côtés."
                },
                {
                    "questionNumber": 95,
                    "question": "Que faire si un collègue est électrisé et encore en contact avec le fil ?",
                    "answerOptions": [
                        {"text": "Couper le courant immédiatement sans toucher la personne", "isCorrect": True},
                        {"text": "Tirer le collègue par le bras pour le décoller du fil", "isCorrect": False},
                        {"text": "Lui verser un seau d'eau froide sur l'ensemble du corps", "isCorrect": False},
                        {"text": "Appeler ses parents pour les informer de la situation", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Si vous touchez la victime, vous serez électrisé à votre tour. Il faut couper le disjoncteur ou écarter le fil avec un bâton en bois sec."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la définition de la prévention intrinsèque ?",
                    "answerOptions": [
                        {"text": "Supprimer le danger dès la conception de la tâche", "isCorrect": True},
                        {"text": "Mettre une grande affiche de sécurité sur le mur gris", "isCorrect": False},
                        {"text": "Porter un casque lourd pendant toute la journée ici", "isCorrect": False},
                        {"text": "Former les salariés aux gestes qui sauvent des vies", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** C'est le niveau le plus efficace de prévention. Exemple : remplacer un produit toxique par un produit inoffensif. On supprime le problème à la source."
                },
                {
                    "questionNumber": 97,
                    "question": "Qu'est-ce qu'un RPS au sein d'une entreprise ?",
                    "answerOptions": [
                        {"text": "Stress, harcèlement, burn-out ou violence interne", "isCorrect": True},
                        {"text": "Une simple coupure au doigt avec un papier blanc", "isCorrect": False},
                        {"text": "Un problème de dos lié au port de charges lourdes", "isCorrect": False},
                        {"text": "Un microbe attrapé lors de la pause déjeuner ici", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Les Risques Psycho-Sociaux touchent à la santé mentale. Ils sont souvent liés à une mauvaise organisation du travail ou à des tensions entre collègues."
                },
                {
                    "questionNumber": 98,
                    "question": "Pourquoi fumer est-il interdit dans l'entreprise ?",
                    "answerOptions": [
                        {"text": "Risque incendie et protection contre le tabagisme passif", "isCorrect": True},
                        {"text": "Pour économiser l'argent de l'ensemble des salariés", "isCorrect": False},
                        {"text": "Parce que l'odeur dérange le grand patron le matin", "isCorrect": False},
                        {"text": "Pour éviter de salir les cendriers de la cour intérieure", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La loi protège les non-fumeurs. La fumée contient des substances cancérigènes. De plus, un mégot mal éteint peut causer une catastrophe industrielle."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel dispositif coupe le courant si on touche un fil dénudé ?",
                    "answerOptions": [
                        {"text": "Un disjoncteur différentiel de trente milliampères", "isCorrect": True},
                        {"text": "Un fusible à cartouche placé dans le tableau mural", "isCorrect": False},
                        {"text": "Une ampoule basse consommation de type LED moderne", "isCorrect": False},
                        {"text": "Une rallonge électrique branchée sur la prise de zone", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** Le différentiel 30 mA détecte une fuite de courant vers la terre (à travers votre corps). Il coupe l'électricité en quelques millièmes de seconde pour vous sauver."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le but ultime de la prévention en entreprise ?",
                    "answerOptions": [
                        {"text": "Supprimer ou réduire au maximum les accidents", "isCorrect": True},
                        {"text": "Remplir tous les papiers administratifs demandés", "isCorrect": False},
                        {"text": "Faire plaisir à l'inspecteur du travail en visite", "isCorrect": False},
                        {"text": "Dépenser l'intégralité du budget sécurité du mois", "isCorrect": False}
                    ],
                    "correction": "**Rappel de cours :** La finalité de la PSE est de préserver l'intégrité physique et mentale des travailleurs pour qu'ils rentrent chez eux en bonne santé chaque soir."
                }
            ]
        }
    }
}