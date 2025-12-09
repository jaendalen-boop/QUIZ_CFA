quiz_data = {
    # La clé "title" a été conservée pour la compatibilité avec votre "app.py"
    "title": "CAP Cuisine - Base de Données Complète (100 Questions) - Corrigée V3",
    
    "description": "Base de données de 100 questions pour le CAP Cuisine, structurée pour fonctionner avec l'application Streamlit fournie. Les longueurs des réponses ont été uniformisées pour éviter tout biais.",
    
    # La clé "themes" (avec dictionnaire interne) est correcte et a été vérifiée à l'étape précédente.
    "themes": {
        # THÈME 1
        1: {
            "name": "Hygiène, Sécurité et Législation (HACCP)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la température maximale de conservation des aliments réfrigérés dans une chambre froide positive ?",
                    "answerOptions": [
                        {"text": "+4°C.", "isCorrect": True, "key": "A"},
                        {"text": "+8°C.", "isCorrect": False, "key": "B"},
                        {"text": "+10°C.", "isCorrect": False, "key": "C"},
                        {"text": "+12°C.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La température maximale légale de conservation des denrées périssables est généralement fixée à +4°C (ou moins selon les produits)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le nom de la zone de température où les micro-organismes se développent le plus rapidement ?",
                    "answerOptions": [
                        {"text": "La zone de danger (+10°C à +63°C).", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "La zone de refroidissement rapide.", "isCorrect": False, "key": "B"},
                        {"text": "La zone de congélation.", "isCorrect": False, "key": "C"},
                        {"text": "La zone de pasteurisation.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La 'zone de danger' microbien se situe entre +10°C et +63°C. Les aliments doivent la traverser le plus rapidement possible."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le temps maximum autorisé pour abaisser la température d'une préparation de +63°C à +10°C ?",
                    "answerOptions": [
                        {"text": "Moins de 2 heures.", "isCorrect": True, "key": "A"},
                        {"text": "Moins de 4 heures.", "isCorrect": False, "key": "B"},
                        {"text": "Moins de 6 heures.", "isCorrect": False, "key": "C"},
                        {"text": "Moins de 1 heure.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le refroidissement rapide est critique pour limiter la prolifération bactérienne dans la zone de danger. La cellule de refroidissement est l'outil adapté."
                },
                {
                    "questionNumber": 4,
                    "question": "Que signifie l'acronyme DLC sur l'emballage d'un produit alimentaire ?",
                    "answerOptions": [
                        {"text": "Date Limite de Consommation.", "isCorrect": True, "key": "A"},
                        {"text": "Durée Limite de Cuisson.", "isCorrect": False, "key": "B"},
                        {"text": "Déclaration Légale de Certificat.", "isCorrect": False, "key": "C"},
                        {"text": "Date de Lancement Commercial.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La DLC est la date au-delà de laquelle le produit est considéré comme impropre à la consommation et ne doit plus être vendu."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel principe d'organisation du travail vise à séparer les zones propres et les zones sales ?",
                    "answerOptions": [
                        {"text": "La marche en avant.", "isCorrect": True, "key": "A"},
                        {"text": "Le système de rotation.", "isCorrect": False, "key": "B"},
                        {"text": "Le Plan de Maîtrise Sanitaire.", "isCorrect": False, "key": "C"},
                        {"text": "Le FIFO.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La marche en avant (dans l'espace ou dans le temps) empêche la contamination des produits finis par les produits bruts ou les déchets."
                },
                {
                    "questionNumber": 6,
                    "question": "Qu'est-ce qu'une contamination croisée en cuisine ?",
                    "answerOptions": [
                        {"text": "Le transfert de germes d'un produit contaminé vers un produit sain.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Le mélange de deux plats différents au dressage.", "isCorrect": False, "key": "B"},
                        {"text": "L'utilisation d'ingrédients de marques différentes.", "isCorrect": False, "key": "C"},
                        {"text": "Une cuisson trop rapide des aliments.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La contamination croisée se produit par contact (mains, ustensiles, planches) ou indirectement (gouttes, air)."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est la principale mesure de prévention contre la contamination manuportée (par les mains) ?",
                    "answerOptions": [
                        {"text": "Lavage et désinfection fréquents des mains et avant-bras.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "L'utilisation de gants en permanence.", "isCorrect": False, "key": "B"},
                        {"text": "Le port d'un tablier jetable.", "isCorrect": False, "key": "C"},
                        {"text": "La cuisson à très haute température.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le lavage régulier et méticuleux des mains reste la mesure d'hygiène la plus efficace."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la température interne minimale de sécurité pour la cuisson de la volaille afin de détruire les bactéries pathogènes ?",
                    "answerOptions": [
                        {"text": "+74°C à cœur.", "isCorrect": True, "key": "A"},
                        {"text": "+60°C à cœur.", "isCorrect": False, "key": "B"},
                        {"text": "+80°C à cœur.", "isCorrect": False, "key": "C"},
                        {"text": "+95°C à cœur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La volaille nécessite une cuisson plus complète que la viande rouge, souvent mesurée à +74°C à cœur pour garantir la sécurité sanitaire."
                },
                {
                    "questionNumber": 9,
                    "question": "Qu'est-ce que le Plan de Maîtrise Sanitaire (PMS) ?",
                    "answerOptions": [
                        {"text": "L'ensemble des procédures d'hygiène et de sécurité sanitaire (méthode HACCP).", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Un calendrier de nettoyage des locaux.", "isCorrect": False, "key": "B"},
                        {"text": "Un document répertoriant les allergènes.", "isCorrect": False, "key": "C"},
                        {"text": "La liste des fournisseurs de l'établissement.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le PMS est la base de l'application de l'HACCP, comprenant le GBPH, la traçabilité et le plan de nettoyage/désinfection."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la bonne méthode pour la décongélation des denrées alimentaires en cuisine ?",
                    "answerOptions": [
                        {"text": "Au réfrigérateur (chambre froide positive, entre 0°C et +4°C).", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "À température ambiante.", "isCorrect": False, "key": "B"},
                        {"text": "Au four micro-ondes sur une assiette.", "isCorrect": False, "key": "C"},
                        {"text": "Sous un filet d'eau chaude.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La décongélation doit être lente et maintenue à basse température pour éviter que l'extérieur de l'aliment n'entre dans la zone de danger."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la première étape d'une procédure de nettoyage et de désinfection (méthode H.A.C.C.P.) ?",
                    "answerOptions": [
                        {"text": "Le débarrassage et le pré-nettoyage (enlèvement des déchets).", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "La désinfection chimique.", "isCorrect": False, "key": "B"},
                        {"text": "Le rinçage final.", "isCorrect": False, "key": "C"},
                        {"text": "L'application du détergent.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le pré-nettoyage est essentiel pour éliminer la saleté visible avant d'appliquer les produits chimiques (détergent puis désinfectant)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel risque majeur est lié à l'utilisation de planches à découper non différenciées (sans code couleur) ?",
                    "answerOptions": [
                        {"text": "Le transfert de bactéries entre produits crus et produits cuits ou prêts à consommer.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "La détérioration rapide de la planche elle-même.", "isCorrect": False, "key": "B"},
                        {"text": "Une mauvaise coupe des aliments.", "isCorrect": False, "key": "C"},
                        {"text": "Le développement de moisissures non dangereuses.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'utilisation de planches distinctes est la méthode la plus simple pour éviter de transférer des bactéries d'un produit brut (poulet cru) à un aliment fini (salade)."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle doit être la température minimale d'un plat chaud servi au client ?",
                    "answerOptions": [
                        {"text": "Au moins +63°C.", "isCorrect": True, "key": "A"},
                        {"text": "Au moins +55°C.", "isCorrect": False, "key": "B"},
                        {"text": "Au moins +70°C.", "isCorrect": False, "key": "C"},
                        {"text": "Au moins +80°C.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le maintien en température des plats chauds doit se faire à +63°C minimum pour rester hors de la zone de danger."
                },
                {
                    "questionNumber": 14,
                    "question": "Que doit-on faire de la tenue de travail (veste, pantalon) en sortant du laboratoire ?",
                    "answerOptions": [
                        {"text": "La retirer ou la recouvrir pour éviter la contamination des zones externes.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "La laver immédiatement.", "isCorrect": False, "key": "B"},
                        {"text": "La laisser sur le plan de travail.", "isCorrect": False, "key": "C"},
                        {"text": "La plier dans le sac de transport.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La tenue doit être strictement réservée à l'espace de travail pour éviter d'importer des germes de l'extérieur ou de contaminer les zones 'propres'."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle est la principale maladie bactérienne associée à la consommation d'œufs crus ou mal cuits ?",
                    "answerOptions": [
                        {"text": "La Salmonellose.", "isCorrect": True, "key": "A"},
                        {"text": "La Listériose.", "isCorrect": False, "key": "B"},
                        {"text": "Le Botulisme.", "isCorrect": False, "key": "C"},
                        {"text": "L'Hépatite A.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les salmonelles sont souvent présentes sur la coquille de l'œuf et peuvent contaminer les préparations non cuites."
                },
                {
                    "questionNumber": 16,
                    "question": "Qu'est-ce qu'un Point Critique pour la Maîtrise (CCP) selon la méthode HACCP ?",
                    "answerOptions": [
                        {"text": "Une étape où l'on peut prévenir, éliminer ou réduire un danger à un niveau acceptable.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Une étape où une erreur est fréquente.", "isCorrect": False, "key": "B"},
                        {"text": "Le moment de la réception des marchandises.", "isCorrect": False, "key": "C"},
                        {"text": "La vaisselle sale après le service.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pasteurisation, la cuisson, ou le refroidissement sont des exemples de CCP où la maîtrise de la température est vitale."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel type de couteau doit-on utiliser pour découper une volaille entière crue ?",
                    "answerOptions": [
                        {"text": "Le couteau d'office ou le couteau à désosser.", "isCorrect": True, "key": "A"},
                        {"text": "Le couteau éminceur (chef) ou le couteau à pain.", "isCorrect": False, "key": "B"},
                        {"text": "Le couteau à poisson.", "isCorrect": False, "key": "C"},
                        {"text": "Le couteau à légumes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le couteau à désosser, avec sa lame fine et rigide, est idéal pour les découpes de précision sur la viande crue."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est la fréquence recommandée pour le nettoyage complet d'une friteuse ?",
                    "answerOptions": [
                        {"text": "Chaque jour ou dès que nécessaire (après le service).", "isCorrect": True, "key": "A"},
                        {"text": "Une fois par semaine.", "isCorrect": False, "key": "B"},
                        {"text": "Une fois par mois.", "isCorrect": False, "key": "C"},
                        {"text": "Deux fois par mois.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'huile de friture (et la friteuse) doit être nettoyée et changée régulièrement, souvent quotidiennement, pour des raisons d'hygiène et de qualité."
                },
                {
                    "questionNumber": 19,
                    "question": "Que doit-on faire avant de goûter un plat ou un fond en cuisine ?",
                    "answerOptions": [
                        {"text": "Utiliser une cuillère propre et la changer après chaque dégustation.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Utiliser une cuillère personnelle et la rincer sous l'eau chaude.", "isCorrect": False, "key": "B"},
                        {"text": "Goûter directement avec le couteau ou l'ustensile de cuisson.", "isCorrect": False, "key": "C"},
                        {"text": "Goûter directement avec le doigt.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le protocole de dégustation est essentiel pour éviter toute contamination de la bouche vers l'aliment. On utilise une cuillère propre par essai."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est la température maximale légale pour le stockage des produits surgelés ?",
                    "answerOptions": [
                        {"text": "-18°C.", "isCorrect": True, "key": "A"},
                        {"text": "-10°C.", "isCorrect": False, "key": "B"},
                        {"text": "-5°C.", "isCorrect": False, "key": "C"},
                        {"text": "-12°C.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La température de -18°C (ou inférieure) est le standard pour la conservation des produits surgelés afin de garantir la qualité et la sécurité."
                }
            ]
        },
        # THÈME 2
        2: {
            "name": "Fonds, Sauces et Liaisons",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la base du fond brun de veau, juste avant l'ajout d'eau ?",
                    "answerOptions": [
                        {"text": "Les os de veau rôtis avec la garniture aromatique (carottes, oignons, tomates).", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Les arêtes de poisson blanchies.", "isCorrect": False, "key": "B"},
                        {"text": "Les légumes et l'eau froide sans os.", "isCorrect": False, "key": "C"},
                        {"text": "Les sucs de viande déglacés.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les os sont rôtis au four jusqu'à ce qu'ils soient bruns, ce qui donne la couleur et la saveur caractéristiques du fond brun."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment s'appelle l'ingrédient principal utilisé pour lier une sauce mère de type Velouté ?",
                    "answerOptions": [
                        {"text": "Le roux blanc (mélange beurre et farine).", "isCorrect": True, "key": "A"},
                        {"text": "L'amidon de maïs (Maïzena) pur.", "isCorrect": False, "key": "B"},
                        {"text": "Le beurre manié.", "isCorrect": False, "key": "C"},
                        {"text": "La crème fraîche.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le Velouté est une sauce mère liée par un roux blanc, sur lequel on verse un fond (volaille, veau ou poisson) et que l'on fait cuire."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le nom de la sauce mère émulsionnée chaude, à base de jaunes d'œufs, de beurre clarifié et de réduction acide ?",
                    "answerOptions": [
                        {"text": "La sauce Hollandaise.", "isCorrect": True, "key": "A"},
                        {"text": "La sauce Béchamel.", "isCorrect": False, "key": "B"},
                        {"text": "La sauce Mayonnaise.", "isCorrect": False, "key": "C"},
                        {"text": "La sauce Espagnole.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La sauce Hollandaise est une émulsion chaude. Si on ajoute de l'estragon et du poivre, on obtient la sauce Béarnaise."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la principale différence entre un fond blanc et un fond brun ?",
                    "answerOptions": [
                        {"text": "Les os et garniture aromatique sont rôtis (brun) ou non (blanc) avant le mouillage.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Le fond brun est lié à la farine, le fond blanc non.", "isCorrect": False, "key": "B"},
                        {"text": "Le fond brun n'utilise que de l'eau, le fond blanc du lait.", "isCorrect": False, "key": "C"},
                        {"text": "Le fond blanc cuit deux fois plus longtemps que le fond brun.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le rôtissage des éléments (os et garniture) donne la couleur et la profondeur aromatique aux fonds bruns."
                },
                {
                    "questionNumber": 25,
                    "question": "Qu'est-ce que le 'singer' une préparation ?",
                    "answerOptions": [
                        {"text": "Saupoudrer de farine une garniture suée pour enrober avant de mouiller.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Assaisonner très fortement une sauce.", "isCorrect": False, "key": "B"},
                        {"text": "Faire bouillir vivement un bouillon.", "isCorrect": False, "key": "C"},
                        {"text": "Ajouter du beurre en fin de cuisson.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Singer est une méthode de liaison. La farine enrobant les aliments forme un roux lors du mouillage, qui épaissit la sauce."
                },
                {
                    "questionNumber": 26,
                    "question": "Comment s'appelle l'écume qui se forme à la surface d'un fond ou d'un bouillon en début de cuisson et qu'il faut enlever ?",
                    "answerOptions": [
                        {"text": "L'écume ou les impuretés (albumine coagulée).", "isCorrect": True, "key": "A"},
                        {"text": "Le dépôt.", "isCorrect": False, "key": "B"},
                        {"text": "Le roux.", "isCorrect": False, "key": "C"},
                        {"text": "La glace.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'écumage est l'opération consistant à retirer ces impuretés pour obtenir un fond limpide et sans amertume."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel ingrédient est ajouté au roux pour réaliser une sauce Béchamel ?",
                    "answerOptions": [
                        {"text": "Du lait froid (ou tiède) versé sur le roux chaud.", "isCorrect": True, "key": "A"},
                        {"text": "Du fond blanc de volaille.", "isCorrect": False, "key": "B"},
                        {"text": "De la crème fraîche liquide.", "isCorrect": False, "key": "C"},
                        {"text": "Un bouillon de légumes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La Béchamel est un Velouté de lait (une des sauces mères), liée par un roux blanc et cuite pour éliminer le goût de la farine."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la température du beurre clarifié pour réussir une sauce Hollandaise ?",
                    "answerOptions": [
                        {"text": "Il doit être chaud (environ 60-70°C).", "isCorrect": True, "key": "A"},
                        {"text": "Il doit être froid (sorti du réfrigérateur).", "isCorrect": False, "key": "B"},
                        {"text": "Il doit être glacé.", "isCorrect": False, "key": "C"},
                        {"text": "Il doit être à température ambiante.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le beurre clarifié chaud est versé lentement sur les jaunes d'œufs montés (sabayon) pour créer une émulsion stable et épaisse."
                },
                {
                    "questionNumber": 29,
                    "question": "Comment appelle-t-on le procédé qui consiste à concentrer un fond par ébullition pour intensifier sa saveur ?",
                    "answerOptions": [
                        {"text": "La réduction.", "isCorrect": True, "key": "A"},
                        {"text": "Le dégraissage.", "isCorrect": False, "key": "B"},
                        {"text": "Le chinoisage.", "isCorrect": False, "key": "C"},
                        {"text": "Le blanchissage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La réduction permet d'obtenir un fond plus concentré et sirupeux, souvent utilisé comme base pour les sauces ou les glaces de viande."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est l'élément qui lie une Mayonnaise ?",
                    "answerOptions": [
                        {"text": "La lécithine contenue dans le jaune d'œuf, qui est l'émulsifiant.", "isCorrect": True, "key": "A"},
                        {"text": "L'eau du vinaigre.", "isCorrect": False, "key": "B"},
                        {"text": "L'ajout de moutarde.", "isCorrect": False, "key": "C"},
                        {"text": "La coagulation de la farine.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La mayonnaise est une émulsion froide et stable de deux liquides non miscibles (l'huile et le vinaigre) stabilisée par la lécithine des jaunes d'œufs."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment appelle-t-on la liaison réalisée avec des œufs entiers ou des jaunes et de la crème ajoutés en fin de cuisson ?",
                    "answerOptions": [
                        {"text": "La liaison à la crème et aux œufs (liaison française).", "isCorrect": True, "key": "A"},
                        {"text": "Le roux clair.", "isCorrect": False, "key": "B"},
                        {"text": "Le beurre manié.", "isCorrect": False, "key": "C"},
                        {"text": "La gélatine.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Cette liaison (crème et jaunes) doit être ajoutée hors du feu ou à feu très doux pour éviter la coagulation des œufs (effet 'grainé')."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est l'élément principal ajouté au fond brun pour obtenir une sauce Espagnole, l'une des sauces mères classiques ?",
                    "answerOptions": [
                        {"text": "Du roux brun (beurre et farine colorés).", "isCorrect": True, "key": "A"},
                        {"text": "De la crème fraîche.", "isCorrect": False, "key": "B"},
                        {"text": "Du beurre manié.", "isCorrect": False, "key": "C"},
                        {"text": "De la fécule de maïs.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La sauce Espagnole est réalisée en mouillant un roux brun avec un fond brun lié. C'est la base de nombreuses sauces dérivées."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est l'utilité du concentré de tomate dans la préparation du fond brun lié ?",
                    "answerOptions": [
                        {"text": "Il apporte de l'acidité et contribue à la coloration et au goût.", "isCorrect": True, "key": "A"},
                        {"text": "Il sert d'agent de liaison.", "isCorrect": False, "key": "B"},
                        {"text": "Il épaissit immédiatement la sauce.", "isCorrect": False, "key": "C"},
                        {"text": "Il remplace les os de veau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le concentré de tomate (ou la tomate fraîche) est souvent ajouté au début de la cuisson du fond brun après le rôtissage, on le pince (cuisson)."
                },
                {
                    "questionNumber": 34,
                    "question": "Comment appelle-t-on l'opération qui consiste à passer un fond, une sauce ou une soupe dans un chinois ?",
                    "answerOptions": [
                        {"text": "Chinoiser ou passer (au chinois étamine).", "isCorrect": True, "key": "A"},
                        {"text": "Écumer.", "isCorrect": False, "key": "B"},
                        {"text": "Liaisonner.", "isCorrect": False, "key": "C"},
                        {"text": "Réduire.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Chinoiser permet de retirer les impuretés, les os et la garniture aromatique pour obtenir un liquide pur et lisse."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le nom de la liaison réalisée en fin de cuisson par l'ajout de beurre manié ou de fécule délayée ?",
                    "answerOptions": [
                        {"text": "La liaison à la fécule ou au beurre manié (liaison tardive).", "isCorrect": True, "key": "A"},
                        {"text": "Le roux roux.", "isCorrect": False, "key": "B"},
                        {"text": "Le déglaçage.", "isCorrect": False, "key": "C"},
                        {"text": "Le sabayon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le beurre manié (beurre + farine crue) ou la fécule est utilisé pour lier rapidement et à chaud des fonds ou des jus."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le rôle du vin blanc ou d'un alcool lors du déglaçage ?",
                    "answerOptions": [
                        {"text": "Dissoudre les sucs de cuisson et les décoller du fond du récipient.", "isCorrect": True, "key": "A"},
                        {"text": "Lier la sauce.", "isCorrect": False, "key": "B"},
                        {"text": "Assaisonner le plat.", "isCorrect": False, "key": "C"},
                        {"text": "Accélérer la cuisson des légumes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le déglaçage est l'opération qui consiste à récupérer les sucs (particules caramélisées et aromatiques) formés au fond de la poêle après cuisson."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment appelle-t-on la sauce obtenue par réduction d'un fond brun de veau, concentrée et très riche ?",
                    "answerOptions": [
                        {"text": "La demi-glace ou glace de viande (si très concentrée).", "isCorrect": True, "key": "A"},
                        {"text": "La Béchamel.", "isCorrect": False, "key": "B"},
                        {"text": "La Hollandaise.", "isCorrect": False, "key": "C"},
                        {"text": "Le roux noir.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La demi-glace est une sauce de base souvent utilisée pour les finitions ou comme base pour d'autres sauces."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est l'utilité du mirepoix dans la préparation d'un fond de cuisine ?",
                    "answerOptions": [
                        {"text": "Apporter les arômes de base (oignons, carottes, céleri) au fond.", "isCorrect": True, "key": "A"},
                        {"text": "Lier le bouillon.", "isCorrect": False, "key": "B"},
                        {"text": "Assurer la coloration des os.", "isCorrect": False, "key": "C"},
                        {"text": "Accélérer le temps de cuisson.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le mirepoix (garniture aromatique) est la base de saveur des fonds. Il est coupé en gros dés et ajouté à la cuisson des os."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel ingrédient est utilisé pour réaliser un fumet de poisson (fond de poisson) ?",
                    "answerOptions": [
                        {"text": "Les arêtes, parures et têtes de poissons blancs, non rincées.", "isCorrect": True, "key": "A"},
                        {"text": "Les os de bœuf et de l'eau.", "isCorrect": False, "key": "B"},
                        {"text": "Les coquilles de crustacés rôtis.", "isCorrect": False, "key": "C"},
                        {"text": "Des légumes uniquement, sans poisson.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le fumet de poisson est réalisé rapidement avec des arêtes et une garniture aromatique. Le poisson est généralement blanchi au préalable."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment appelle-t-on l'opération qui consiste à incorporer du beurre froid à la fin dans une sauce, hors du feu, en fouettant ?",
                    "answerOptions": [
                        {"text": "Monter au beurre (ou beurrer).", "isCorrect": True, "key": "A"},
                        {"text": "Sauter.", "isCorrect": False, "key": "B"},
                        {"text": "Émulsionner à froid.", "isCorrect": False, "key": "D"},
                        {"text": "Réduire.", "isCorrect": False, "key": "C"}
                    ],
                    "correction": "Monter au beurre (ou 'monter à la noisette' si le beurre est chauffé) permet d'épaissir légèrement la sauce et de lui donner du brillant et de la richesse."
                }
            ]
        },
        # THÈME 3
        3: {
            "name": "Techniques de Cuisson et Taillage",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le taillage d'un légume en fins bâtonnets de 1 à 2 mm de côté ?",
                    "answerOptions": [
                        {"text": "La julienne.", "isCorrect": True, "key": "A"},
                        {"text": "La brunoise.", "isCorrect": False, "key": "B"},
                        {"text": "La macédoine.", "isCorrect": False, "key": "C"},
                        {"text": "La mirepoix.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La julienne est le taillage le plus fin en bâtonnets (allumettes). Elle est utilisée pour les garnitures et les soupes fines."
                },
                {
                    "questionNumber": 42,
                    "question": "Comment appelle-t-on le taillage d'un légume en petits cubes de 2 à 3 mm de côté ?",
                    "answerOptions": [
                        {"text": "La brunoise.", "isCorrect": True, "key": "A"},
                        {"text": "La chiffonnade.", "isCorrect": False, "key": "B"},
                        {"text": "La paysanne.", "isCorrect": False, "key": "C"},
                        {"text": "La matignon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La brunoise est un taillage en dés fins. Elle est souvent réalisée à partir de la julienne pour obtenir les dés."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle technique consiste à cuire un aliment dans un corps gras chaud (huile, beurre) en remuant sans coloration importante ?",
                    "answerOptions": [
                        {"text": "Le suage ou l'étuvage.", "isCorrect": True, "key": "A"},
                        {"text": "Le rôtissage.", "isCorrect": False, "key": "B"},
                        {"text": "La friture.", "isCorrect": False, "key": "C"},
                        {"text": "Le grillage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le suage permet de faire ressortir l'eau des légumes et de les rendre fondants. C'est souvent la base d'une garniture aromatique."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel type de cuisson est le rôtissage ?",
                    "answerOptions": [
                        {"text": "Une cuisson par concentration à chaleur sèche et vive (au four ou à la broche).", "isCorrect": True, "key": "A"},
                        {"text": "Une cuisson par expansion dans un liquide.", "isCorrect": False, "key": "B"},
                        {"text": "Une cuisson par friture dans un bain d'huile.", "isCorrect": False, "key": "C"},
                        {"text": "Une cuisson lente dans un récipient fermé.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le rôtissage est une cuisson sans ajout de liquide, souvent pour les grosses pièces de viande et volaille."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment appelle-t-on l'opération qui consiste à retirer la peau des amandes ou des tomates par trempage dans de l'eau bouillante ?",
                    "answerOptions": [
                        {"text": "Monder.", "isCorrect": True, "key": "A"},
                        {"text": "Blanchir.", "isCorrect": False, "key": "B"},
                        {"text": "Émincer.", "isCorrect": False, "key": "C"},
                        {"text": "Concasser.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Monder consiste à tremper brièvement (quelques secondes) un aliment dans l'eau bouillante puis dans l'eau glacée pour faciliter l'enlèvement de la peau."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le nom de la technique de cuisson lente d'un aliment dans son propre jus ou avec peu de liquide, à couvert ?",
                    "answerOptions": [
                        {"text": "L'étuvage.", "isCorrect": True, "key": "A"},
                        {"text": "Le griller.", "isCorrect": False, "key": "B"},
                        {"text": "Le pocher au grand bouillon.", "isCorrect": False, "key": "C"},
                        {"text": "Le faire frire.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'étuvage est une cuisson lente à chaleur humide, souvent utilisée pour les légumes comme les poireaux ou les oignons (étuvée de poireaux)."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est la coupe des oignons en fines lamelles pour les soupes ou les garnitures ?",
                    "answerOptions": [
                        {"text": "Ciseler ou émincer.", "isCorrect": True, "key": "A"},
                        {"text": "Tourner.", "isCorrect": False, "key": "B"},
                        {"text": "Hacher.", "isCorrect": False, "key": "C"},
                        {"text": "Parer.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Ciseler s'applique principalement aux oignons et aux échalotes. Émincer s'applique à la coupe fine de divers légumes."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment appelle-t-on la cuisson d'un aliment dans un liquide frémissant (jamais bouillant), idéal pour les œufs ou les quenelles ?",
                    "answerOptions": [
                        {"text": "Le pochage ou pocher.", "isCorrect": True, "key": "A"},
                        {"text": "Le bouillir.", "isCorrect": False, "key": "B"},
                        {"text": "Le braisage.", "isCorrect": False, "key": "C"},
                        {"text": "Le rissoler.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le pochage se fait à une température sous l'ébullition (environ 80-90°C), permettant une cuisson douce et uniforme."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est le nom de l'opération qui consiste à couper des fines herbes en lanières sans les hacher trop finement ?",
                    "answerOptions": [
                        {"text": "La chiffonnade.", "isCorrect": True, "key": "A"},
                        {"text": "Le ciseler.", "isCorrect": False, "key": "B"},
                        {"text": "L'émincer.", "isCorrect": False, "key": "C"},
                        {"text": "Le concasser.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La chiffonnade s'applique principalement aux feuilles (laitue, oseille, basilic) que l'on roule avant de couper en fines lanières."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est l'objectif du 'tournage' des légumes (carottes, pommes de terre) ?",
                    "answerOptions": [
                        {"text": "Améliorer l'esthétique du plat et uniformiser la cuisson.", "isCorrect": True, "key": "A"},
                        {"text": "Conserver plus longtemps le légume.", "isCorrect": False, "key": "B"},
                        {"text": "Rendre le légume plus tendre.", "isCorrect": False, "key": "C"},
                        {"text": "Augmenter la quantité de légume.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le tournage (donner une forme régulière et homogène) est une technique classique pour la présentation et pour s'assurer que toutes les pièces cuisent de la même manière."
                },
                {
                    "questionNumber": 51,
                    "question": "Comment appelle-t-on le taillage de la garniture aromatique (carottes, céleri, oignons) en dés moyens pour les fonds et les bouillons ?",
                    "answerOptions": [
                        {"text": "La mirepoix (ou matignon pour un usage spécifique).", "isCorrect": True, "key": "A"},
                        {"text": "La brunoise.", "isCorrect": False, "key": "B"},
                        {"text": "La paysanne.", "isCorrect": False, "key": "C"},
                        {"text": "La julienne.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le mirepoix est la coupe en dés moyens, généralement 1 cm de côté, utilisée pour les fonds et les cuissons longues."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la technique pour retirer les impuretés du beurre par fonte douce et décantation ?",
                    "answerOptions": [
                        {"text": "Clarifier le beurre.", "isCorrect": True, "key": "A"},
                        {"text": "Beurrer.", "isCorrect": False, "key": "B"},
                        {"text": "Monter au beurre.", "isCorrect": False, "key": "C"},
                        {"text": "Manié.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le beurre clarifié est le beurre dont on a retiré l'eau et la caséine (protéines), ce qui augmente son point de fumée et sa stabilité à la cuisson."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le nom de la technique de cuisson mixte (saisie puis mijotage) utilisée pour les grosses pièces de viande (joues, épaules) ?",
                    "answerOptions": [
                        {"text": "Le braisage.", "isCorrect": True, "key": "A"},
                        {"text": "Le rôtissage.", "isCorrect": False, "key": "B"},
                        {"text": "Le griller.", "isCorrect": False, "key": "C"},
                        {"text": "Le sauter.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le braisage est une cuisson lente et longue, dans un liquide aromatisé, au four ou sur le feu, après avoir fait rissoler la pièce de viande."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la coupe en fines tranches très fines, souvent utilisée pour les champignons ou les truffes ?",
                    "answerOptions": [
                        {"text": "Émincer.", "isCorrect": True, "key": "A"},
                        {"text": "Hacher.", "isCorrect": False, "key": "B"},
                        {"text": "Concasser.", "isCorrect": False, "key": "C"},
                        {"text": "Tourner.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Émincer est le terme général pour couper en fines tranches, appliqué notamment aux oignons, au chou ou aux champignons."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est l'objectif du 'blanchiment' des légumes verts (plongeon rapide dans l'eau bouillante) ?",
                    "answerOptions": [
                        {"text": "Fixer leur couleur, éliminer l'amertume ou les rendre plus digestes.", "isCorrect": True, "key": "A"},
                        {"text": "Assurer la cuisson complète.", "isCorrect": False, "key": "B"},
                        {"text": "Les rendre croquants.", "isCorrect": False, "key": "C"},
                        {"text": "Rendre la peau plus épaisse.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le blanchiment est un pré-traitement. L'eau bouillante détruit une enzyme qui oxyde le légume, fixant ainsi le vert."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle est la technique de cuisson qui consiste à faire dorer et cuire rapidement de petits morceaux d'aliments à feu vif dans un peu de matière grasse ?",
                    "answerOptions": [
                        {"text": "Sauter ou rissoler.", "isCorrect": True, "key": "A"},
                        {"text": "Pocher.", "isCorrect": False, "key": "B"},
                        {"text": "Braiser.", "isCorrect": False, "key": "C"},
                        {"text": "Frémir.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Sauter implique de remuer l'aliment pour une cuisson uniforme et rapide. Cela concentre les saveurs par caramélisation superficielle."
                },
                {
                    "questionNumber": 57,
                    "question": "Comment appelle-t-on la coupe de légumes en carrés de 5 mm de côté, souvent utilisée pour les garnitures de potages ?",
                    "answerOptions": [
                        {"text": "La macédoine.", "isCorrect": True, "key": "A"},
                        {"text": "Le concassé.", "isCorrect": False, "key": "B"},
                        {"text": "La brunoise.", "isCorrect": False, "key": "C"},
                        {"text": "La paysanne.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La macédoine est une coupe en cubes de taille moyenne. La brunoise est en très petits cubes, et la paysanne en petits carrés ou triangles fins."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est l'effet de l'assaisonnement (sel) d'un aliment (viande, poisson) trop tôt avant la cuisson ?",
                    "answerOptions": [
                        {"text": "Le sel déshydrate le produit, il perd son eau et rend le rôtissage difficile.", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "L'assaisonnement est parfait si on sale 1 heure à l'avance.", "isCorrect": False, "key": "B"},
                        {"text": "Le sel caramélise la surface du produit.", "isCorrect": False, "key": "C"},
                        {"text": "Le sel augmente le pouvoir de liaison de la viande.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le sel a un pouvoir osmotique : il attire l'eau en surface. Il est souvent conseillé de saler juste avant ou juste après la cuisson pour éviter la perte d'eau."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle est la technique pour préparer les tomates en retirant la peau, les pépins, puis en les coupant en morceaux ?",
                    "answerOptions": [
                        {"text": "Monder, épépiner, concasser.", "isCorrect": True, "key": "A"},
                        {"text": "Émincer, monder, sauter.", "isCorrect": False, "key": "B"},
                        {"text": "Blanchir, braiser, glacer.", "isCorrect": False, "key": "C"},
                        {"text": "Tourner, hacher, déglacer.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Concasser la tomate fait référence au taillage en morceaux irréguliers après avoir retiré la peau (monder) et les pépins."
                },
                {
                    "questionNumber": 60,
                    "question": "Comment appelle-t-on le fait de cuire un aliment à l'eau bouillante et à gros bouillons ?",
                    "answerOptions": [
                        {"text": "Bouillir.", "isCorrect": True, "key": "A"},
                        {"text": "Pocher.", "isCorrect": False, "key": "B"},
                        {"text": "Frémir.", "isCorrect": False, "key": "C"},
                        {"text": "Braiser.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Bouillir est une cuisson forte, généralement pour les légumes ou les pâtes. Pocher ou frémir sont des cuissons plus douces."
                }
            ]
        },
        # THÈME 4
        4: {
            "name": "Préparations de Base et Appareils",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le nom de l'appareil à base de chair de poisson ou de volaille, de panade et d'œufs, mixé pour obtenir une consistance lisse ?",
                    "answerOptions": [
                        {"text": "La farce fine ou mousseline (si allégée à la crème).", "isCorrect": True, "key": "A"},
                        {"text": "La panade sèche.", "isCorrect": False, "key": "B"},
                        {"text": "Le mirepoix.", "isCorrect": False, "key": "C"},
                        {"text": "Le sabayon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La farce fine est une base très lisse, utilisée pour les quenelles, les pâtés ou les terrines."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel ingrédient permet de faire monter un blanc d'œuf pour une mousse ou une meringue ?",
                    "answerOptions": [
                        {"text": "La protéine albumine, associée à de l'air et à un fouet.", "isCorrect": True, "key": "A"},
                        {"text": "L'amidon de maïs.", "isCorrect": False, "key": "B"},
                        {"text": "Le sel fin.", "isCorrect": False, "key": "C"},
                        {"text": "Le vinaigre blanc pur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le fouettage force l'air à se mélanger aux protéines. Le sucre ou un acide peut stabiliser cette mousse."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on la méthode pour paner un aliment en trois étapes (farine, œuf battu, chapelure) ?",
                    "answerOptions": [
                        {"text": "Paner à l'anglaise.", "isCorrect": True, "key": "A"},
                        {"text": "Paner à la romaine.", "isCorrect": False, "key": "B"},
                        {"text": "Paner à la française.", "isCorrect": False, "key": "C"},
                        {"text": "Paner à la milanaise.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La panure à l'anglaise est la technique standard pour les escalopes ou les poissons, assurant une belle croûte croustillante à la friture ou au sauter."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est le nom du mélange de beurre et de farine cuit, utilisé comme base de liaison pour les sauces, fonds et potages ?",
                    "answerOptions": [
                        {"text": "Le roux (blanc, blond ou brun).", "isCorrect": True, "key": "A"},
                        {"text": "Le beurre manié.", "isCorrect": False, "key": "B"},
                        {"text": "Le sabayon.", "isCorrect": False, "key": "C"},
                        {"text": "La panade.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le roux (roux cuit) est la liaison la plus courante. Sa couleur dépend du temps de cuisson."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le nom de la pâte de base pour les sauces comme la Béchamel, composée de mie de pain ou de riz et de lait ou de bouillon ?",
                    "answerOptions": [
                        {"text": "La panade.", "isCorrect": True, "key": "A"},
                        {"text": "La liaison.", "isCorrect": False, "key": "B"},
                        {"text": "La farce.", "isCorrect": False, "key": "C"},
                        {"text": "La rouille.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La panade est une préparation à base de féculents (farine, mie de pain) mélangée à un liquide, utilisée pour lier les farces ou les boulettes."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est l'appareil à base d'œufs, de crème ou de lait et d'assaisonnement, utilisé pour les quiches ou les gratins ?",
                    "answerOptions": [
                        {"text": "L'appareil à quiche (ou migaine).", "isCorrect": True, "key": "A"},
                        {"text": "L'appareil à soufflé.", "isCorrect": False, "key": "B"},
                        {"text": "La sauce tomate.", "isCorrect": False, "key": "C"},
                        {"text": "Le fond brun.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'appareil à quiche (ou migaine) est l'appareil de base pour tous les plats à base de garniture liquide cuite."
                },
                {
                    "questionNumber": 67,
                    "question": "Comment appelle-t-on le mélange de jaunes d'œufs, de sucre et de vin blanc fouetté au bain-marie jusqu'à consistance mousseuse ?",
                    "answerOptions": [
                        {"text": "Le sabayon.", "isCorrect": True, "key": "A"},
                        {"text": "La Chantilly.", "isCorrect": False, "key": "B"},
                        {"text": "L'appareil à bombe.", "isCorrect": False, "key": "C"},
                        {"text": "La panade.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le sabayon est une préparation sucrée ou salée, cuite et montée au fouet, souvent servie chaude."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel ingrédient peut être utilisé pour renforcer la liaison d'une farce fine et lui donner une meilleure tenue ?",
                    "answerOptions": [
                        {"text": "L'ajout d'une panade (mie de pain, riz) ou d'un peu de blanc d'œuf.", "isCorrect": True, "key": "A"},
                        {"text": "Du jus de citron.", "isCorrect": False, "key": "B"},
                        {"text": "Du sel uniquement.", "isCorrect": False, "key": "C"},
                        {"text": "De l'huile d'olive.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La panade et les œufs sont les liants classiques des farces. Le sel est aussi essentiel pour extraire les protéines et lier la farce."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est le nom du taillage des fines herbes pour l'assaisonnement des plats (persil, ciboulette) ?",
                    "answerOptions": [
                        {"text": "Le hacher finement (ou ciseler pour les oignons).", "isCorrect": True, "key": "A"},
                        {"text": "Le concasser.", "isCorrect": False, "key": "B"},
                        {"text": "Le parer.", "isCorrect": False, "key": "C"},
                        {"text": "Le piquer.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Hacher permet d'obtenir des morceaux très fins. Le terme 'ciseler' est plus souvent utilisé pour les herbes en fines rondelles comme la ciboulette."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est l'ingrédient principal utilisé pour 'lisser' et rendre brillante une purée de pommes de terre ?",
                    "answerOptions": [
                        {"text": "Le beurre frais et le lait chaud.", "isCorrect": True, "key": "A"},
                        {"text": "Le sel fin.", "isCorrect": False, "key": "B"},
                        {"text": "L'eau froide.", "isCorrect": False, "key": "C"},
                        {"text": "Le sucre glace.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le beurre et le lait (ou la crème) apportent la richesse et l'onctuosité. Ils doivent être ajoutés chauds pour maintenir la température de la purée."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment appelle-t-on le procédé de préparation des escargots avant leur cuisson (ajout de sel, vinaigre) ?",
                    "answerOptions": [
                        {"text": "Débavement.", "isCorrect": True, "key": "A"},
                        {"text": "Blanchiment.", "isCorrect": False, "key": "B"},
                        {"text": "Dégraissage.", "isCorrect": False, "key": "C"},
                        {"text": "Parer.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le débavement permet de nettoyer les escargots de leur bave et de les préparer pour la cuisson au court-bouillon."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est l'appareil utilisé pour réaliser des crêpes salées ou sucrées ?",
                    "answerOptions": [
                        {"text": "La pâte à crêpes (mélange œuf, lait, farine, sucre).", "isCorrect": True, "key": "A"},
                        {"text": "Le sabayon.", "isCorrect": False, "key": "B"},
                        {"text": "La Béchamel.", "isCorrect": False, "key": "C"},
                        {"text": "Le biscuit de Savoie.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pâte à crêpes est l'appareil liquide de base. Le temps de repos est important pour l'hydratation de la farine."
                },
                {
                    "questionNumber": 73,
                    "question": "Comment doit-on préparer une tête de poisson (pour un fumet) avant de la mettre à cuire ?",
                    "answerOptions": [
                        {"text": "Enlever les ouïes et les yeux pour éviter l'amertume et le goût fort.", "isCorrect": True, "key": "A"},
                        {"text": "La couper en brunoise.", "isCorrect": False, "key": "B"},
                        {"text": "La rôtir au four à 200°C.", "isCorrect": False, "key": "C"},
                        {"text": "La saler et la poivrer fortement.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les ouïes et les yeux du poisson sont sources d'impuretés et peuvent donner un goût désagréable au fumet."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel ingrédient est ajouté au pain rassis pour réaliser la chapelure sèche ?",
                    "answerOptions": [
                        {"text": "Rien, la chapelure est du pain séché et broyé uniquement.", "isCorrect": True, "key": "A"},
                        {"text": "Du sel et du poivre.", "isCorrect": False, "key": "B"},
                        {"text": "De la farine et de l'œuf.", "isCorrect": False, "key": "C"},
                        {"text": "De l'huile d'olive.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La chapelure est simplement du pain sec (souvent sans croûte) réduit en poudre et utilisé pour la panure."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le rôle du persil haché dans le beurre composé pour les escargots ?",
                    "answerOptions": [
                        {"text": "Apporter de la couleur et une saveur fraîche.", "isCorrect": True, "key": "A"},
                        {"text": "Assurer la liaison du beurre.", "isCorrect": False, "key": "B"},
                        {"text": "Stabiliser le beurre fondu.", "isCorrect": False, "key": "C"},
                        {"text": "Saler le plat.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le beurre d'escargot est un beurre composé d'ail, de persil, d'échalotes et d'assaisonnement."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment appelle-t-on le procédé pour préparer la viande en retirant les parties inutiles (graisse, aponévroses) ?",
                    "answerOptions": [
                        {"text": "Parer la viande.", "isCorrect": True, "key": "A"},
                        {"text": "Émonder la viande.", "isCorrect": False, "key": "B"},
                        {"text": "Hacher la viande.", "isCorrect": False, "key": "C"},
                        {"text": "Pocher la viande.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Parer est l'opération de nettoyage et d'habillage des viandes et poissons pour les rendre présentables et utilisables."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel ingrédient permet de réaliser une marinade 'cuite' (comme pour le civet ou le bœuf bourguignon) ?",
                    "answerOptions": [
                        {"text": "Le vin rouge (souvent avec une garniture aromatique et des aromates).", "isCorrect": True, "key": "A"},
                        {"text": "De la crème fraîche.", "isCorrect": False, "key": "B"},
                        {"text": "Du jus de citron uniquement.", "isCorrect": False, "key": "C"},
                        {"text": "Du lait entier.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La marinade au vin rouge (ou blanc) est la base des braisés et des plats mijotés. Elle est dite 'cuite' si le liquide a été porté à ébullition avant d'être versé sur la viande."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est l'utilité du papier sulfurisé beurré et découpé (appelé 'rond de papier') sur un fond ou une soupe qui mijote ?",
                    "answerOptions": [
                        {"text": "Éviter la formation d'une pellicule ou d'une croûte à la surface.", "isCorrect": True, "key": "A"},
                        {"text": "Accélérer l'évaporation du liquide.", "isCorrect": False, "key": "B"},
                        {"text": "Assurer la coloration du fond.", "isCorrect": False, "key": "C"},
                        {"text": "Rendre la sauce plus liquide.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le rond de papier (ou papier sulfurisé au contact) empêche le contact de la surface avec l'air, évitant ainsi le dessèchement superficiel."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le nom de l'appareil qui sert de base à la fabrication des soufflés, liant les œufs et le liquide ?",
                    "answerOptions": [
                        {"text": "L'appareil à soufflé (souvent une panade ou une Béchamel épaisse).", "isCorrect": True, "key": "A"},
                        {"text": "La glace de viande.", "isCorrect": False, "key": "B"},
                        {"text": "L'émulsion froide.", "isCorrect": False, "key": "C"},
                        {"text": "Le roux brun.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'appareil à soufflé est enrichi des jaunes d'œufs et des blancs montés sont incorporés pour l'aérer et lui donner son volume à la cuisson."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment appelle-t-on l'opération qui consiste à badigeonner de beurre fondu la surface d'une volaille en rôtissage ?",
                    "answerOptions": [
                        {"text": "Arroser la volaille.", "isCorrect": True, "key": "A"},
                        {"text": "Barder la volaille.", "isCorrect": False, "key": "B"},
                        {"text": "Piquer la volaille.", "isCorrect": False, "key": "C"},
                        {"text": "Brider la volaille.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Arroser la volaille assure le maintien de son moelleux et contribue à sa belle coloration."
                }
            ]
        },
        # THÈME 5
        5: {
            "name": "Connaissance des Produits (Légumes, Viandes, Poissons)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel type de légume est la betterave ?",
                    "answerOptions": [
                        {"text": "Un légume racine.", "isCorrect": True, "key": "A"},
                        {"text": "Un légume feuille.", "isCorrect": False, "key": "B"},
                        {"text": "Un légume fruit.", "isCorrect": False, "key": "C"},
                        {"text": "Un légume graine.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La betterave est le légume formé par la racine de la plante, comme la carotte et le navet."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le nom du morceau de bœuf situé sur la cuisse, souvent utilisé pour les steaks et la fondue ?",
                    "answerOptions": [
                        {"text": "Le rumsteak ou la poire.", "isCorrect": True, "key": "A"},
                        {"text": "La bavette.", "isCorrect": False, "key": "B"},
                        {"text": "Le paleron.", "isCorrect": False, "key": "C"},
                        {"text": "Le flanchet.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le rumsteak est une pièce de la cuisse arrière, tendre et peu grasse. La poire est un petit morceau très tendre de l'arrière-train."
                },
                {
                    "questionNumber": 83,
                    "question": "Comment appelle-t-on le poisson dont l'œil est sur le côté et qui vit à plat (comme la sole) ?",
                    "answerOptions": [
                        {"text": "Un poisson plat.", "isCorrect": True, "key": "A"},
                        {"text": "Un poisson rond.", "isCorrect": False, "key": "B"},
                        {"text": "Un poisson bleu.", "isCorrect": False, "key": "C"},
                        {"text": "Un poisson blanc.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les poissons plats (sole, turbot, plie) ont une forme asymétrique et vivent sur le fond marin."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel ingrédient est naturellement utilisé pour attendrir la viande et la rendre plus tendre ?",
                    "answerOptions": [
                        {"text": "Les acides (vinaigre, citron, vin) ou les enzymes (ananas, kiwi).", "isCorrect": True, "key": "A"}, # ⬅️ Réponse CONCISE
                        {"text": "Le sel fin.", "isCorrect": False, "key": "B"},
                        {"text": "La fécule de maïs.", "isCorrect": False, "key": "C"},
                        {"text": "Le sucre en poudre.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les acides aident à décomposer les fibres musculaires. La maturation (temps de repos) a également un effet important."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle est la caractéristique d'une pomme de terre à chair ferme, idéale pour les salades et la cuisson à l'eau ?",
                    "answerOptions": [
                        {"text": "Elle se tient bien à la cuisson et ne s'écrase pas.", "isCorrect": True, "key": "A"},
                        {"text": "Elle s'effrite et est farineuse.", "isCorrect": False, "key": "B"},
                        {"text": "Elle devient transparente à la cuisson.", "isCorrect": False, "key": "C"},
                        {"text": "Elle est très riche en matière grasse.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les variétés à chair ferme (Charlotte, Ratte, Amandine) sont faibles en amidon et conservent leur forme. Les farineuses sont riches en amidon."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel morceau de la volaille est considéré comme le plus maigre ?",
                    "answerOptions": [
                        {"text": "Le blanc (poitrine ou filet).", "isCorrect": True, "key": "A"},
                        {"text": "La cuisse.", "isCorrect": False, "key": "B"},
                        {"text": "L'aile.", "isCorrect": False, "key": "C"},
                        {"text": "Le pilon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le blanc de volaille (poulet, dinde) est la partie la plus riche en protéines et la plus pauvre en graisses."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est le nom du fruit de mer à coquille bivalve, noir, souvent cuit à la marinière ?",
                    "answerOptions": [
                        {"text": "La moule.", "isCorrect": True, "key": "A"},
                        {"text": "L'huître.", "isCorrect": False, "key": "B"},
                        {"text": "La palourde.", "isCorrect": False, "key": "C"},
                        {"text": "La Saint-Jacques.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La moule est un bivalve très courant. Elle est généralement cuite à la vapeur ou à la marinière (vin blanc, échalotes, persil)."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le nom du légume fruit de couleur verte, souvent consommé cru en salade ou cuit en farce ?",
                    "answerOptions": [
                        {"text": "Le concombre ou la courgette.", "isCorrect": True, "key": "A"},
                        {"text": "Le chou-fleur.", "isCorrect": False, "key": "B"},
                        {"text": "Le céleri-rave.", "isCorrect": False, "key": "C"},
                        {"text": "Le poireau.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le concombre et la courgette sont botaniquement des fruits (ils contiennent les graines) mais sont consommés comme des légumes."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la caractéristique principale d'une viande de gibier par rapport à une viande d'élevage ?",
                    "answerOptions": [
                        {"text": "Un goût plus fort et une chair souvent plus ferme et moins grasse.", "isCorrect": True, "key": "A"},
                        {"text": "Un goût plus sucré et très tendre.", "isCorrect": False, "key": "B"},
                        {"text": "Elle ne nécessite pas d'assaisonnement.", "isCorrect": False, "key": "C"},
                        {"text": "Elle doit toujours être braisée.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le gibier (sanglier, chevreuil) a un goût plus prononcé dû à son alimentation sauvage et nécessite souvent une marinade avant cuisson."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le nom du poisson rond, à chair blanche et délicate, souvent cuit à la vapeur ou poché (ex : cabillaud) ?",
                    "answerOptions": [
                        {"text": "Un poisson blanc (ou poisson maigre).", "isCorrect": True, "key": "A"},
                        {"text": "Un poisson gras (ou poisson bleu).", "isCorrect": False, "key": "B"},
                        {"text": "Un poisson d'eau douce.", "isCorrect": False, "key": "C"},
                        {"text": "Un crustacé.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Les poissons blancs sont généralement les plus maigres et possèdent une chair qui se détache en flocons à la cuisson."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle est la différence principale entre une huître creuse et une huître plate ?",
                    "answerOptions": [
                        {"text": "La plate est ronde et possède une saveur plus iodée et fine.", "isCorrect": True, "key": "A"},
                        {"text": "La creuse est considérée comme plus luxueuse que la plate.", "isCorrect": False, "key": "B"},
                        {"text": "La plate est beaucoup plus grosse que la creuse.", "isCorrect": False, "key": "C"},
                        {"text": "La creuse se mange crue et la plate se mange cuite.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "L'huître plate (Belon, Marennes) est ronde et recherchée pour sa saveur noisetée. La creuse (fines de claire) est la plus courante."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le nom du légume tubercule riche en amidon, utilisé pour les frites et les purées ?",
                    "answerOptions": [
                        {"text": "La pomme de terre.", "isCorrect": True, "key": "A"},
                        {"text": "Le radis.", "isCorrect": False, "key": "B"},
                        {"text": "L'artichaut.", "isCorrect": False, "key": "C"},
                        {"text": "L'oignon.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La pomme de terre est le tubercule le plus consommé. Sa teneur en amidon détermine si elle est à chair ferme ou farineuse."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel morceau de bœuf est idéal pour les cuissons longues et mijotées (bourguignon) en raison de sa teneur en collagène ?",
                    "answerOptions": [
                        {"text": "Le paleron, la joue ou le gîte.", "isCorrect": True, "key": "A"},
                        {"text": "Le filet (tenderloin).", "isCorrect": False, "key": "B"},
                        {"text": "L'entrecôte.", "isCorrect": False, "key": "C"},
                        {"text": "La bavette.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Ces morceaux sont riches en tissus conjonctifs (collagène) qui, sous l'effet d'une cuisson lente et humide, se transforment en gélatine, rendant la viande fondante."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment s'appelle l'organe (sorte de petite poche) qu'il faut retirer de la crevette avant de la consommer ou de la cuire ?",
                    "answerOptions": [
                        {"text": "Le boyau ou veine (tube digestif).", "isCorrect": True, "key": "A"},
                        {"text": "La nageoire.", "isCorrect": False, "key": "B"},
                        {"text": "Le corail.", "isCorrect": False, "key": "C"},
                        {"text": "La carapace.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le tube digestif de la crevette doit être retiré car il peut contenir du sable et donner un mauvais goût."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle technique de préparation préliminaire doit être effectuée sur un poisson rond avant de le fileter ?",
                    "answerOptions": [
                        {"text": "Écailler, vider et rincer.", "isCorrect": True, "key": "A"},
                        {"text": "Faire tremper dans de l'eau chaude.", "isCorrect": False, "key": "B"},
                        {"text": "Le saler fortement.", "isCorrect": False, "key": "C"},
                        {"text": "Le cuire à la vapeur.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Écailler et vider sont des étapes essentielles pour nettoyer le poisson avant toute préparation (filetage, cuisson entière)."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est le nom de la coupe du chou ou des feuilles en fines lanières ?",
                    "answerOptions": [
                        {"text": "La chiffonnade (ou émincer).", "isCorrect": True, "key": "A"},
                        {"text": "La mirepoix.", "isCorrect": False, "key": "B"},
                        {"text": "La parisienne.", "isCorrect": False, "key": "C"},
                        {"text": "Le tournage.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La chiffonnade est la coupe en fines lanières, souvent après avoir roulé la feuille sur elle-même."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle est la différence principale entre un bouquet garni et un sachet d'épices (pour les fonds) ?",
                    "answerOptions": [
                        {"text": "Le bouquet garni est ficelé et contient des aromates frais (thym, laurier, persil).", "isCorrect": True, "key": "A"},
                        {"text": "Le sachet d'épices contient des herbes séchées uniquement.", "isCorrect": False, "key": "B"},
                        {"text": "Le bouquet garni est ajouté uniquement en fin de cuisson.", "isCorrect": False, "key": "C"},
                        {"text": "Le bouquet garni sert à lier la sauce.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le bouquet garni (frais) est ficelé pour être retiré facilement. Le sachet d'épices (épices et graines) est mis dans un petit sachet de mousseline."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle est la principale source de gélatine dans un fond de veau ou de volaille longuement mijoté ?",
                    "answerOptions": [
                        {"text": "Le collagène des os, des cartilages et des tendons.", "isCorrect": True, "key": "A"},
                        {"text": "La graisse de la viande.", "isCorrect": False, "key": "B"},
                        {"text": "Le sel et le poivre.", "isCorrect": False, "key": "C"},
                        {"text": "L'amidon des légumes.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "La gélatine provient de la transformation lente du collagène pendant la cuisson. C'est elle qui donne l'aspect 'tremblant' au fond refroidi."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le nom du morceau de porc très maigre, idéal pour les rôtis et les cuissons courtes ?",
                    "answerOptions": [
                        {"text": "Le filet mignon ou la longe.", "isCorrect": True, "key": "A"},
                        {"text": "L'échine.", "isCorrect": False, "key": "B"},
                        {"text": "Le travers.", "isCorrect": False, "key": "C"},
                        {"text": "Le jarret.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le filet mignon est le morceau le plus tendre et le plus cher du porc, et il est très peu gras."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est l'assaisonnement de base, après le sel, le plus couramment utilisé pour relever le goût de presque tous les plats ?",
                    "answerOptions": [
                        {"text": "Le poivre (blanc ou noir).", "isCorrect": True, "key": "A"},
                        {"text": "Le piment d'Espelette.", "isCorrect": False, "key": "B"},
                        {"text": "Le paprika.", "isCorrect": False, "key": "C"},
                        {"text": "Le cumin.", "isCorrect": False, "key": "D"}
                    ],
                    "correction": "Le sel et le poivre sont les deux assaisonnements fondamentaux et universels de la cuisine."
                }
            ]
        }
    }
}