quiz_data = {
    "title": "Quiz CAP Boucher (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : CONNAISSANCE DES MATIÈRES PREMIÈRES ET ANATOMIE (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : CONNAISSANCE DES MATIÈRES PREMIÈRES ET ANATOMIE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la dénomination exacte de la femelle de l'espèce bovine qui a déjà vêlé ?",
                    "answerOptions": [
                        {"text": "Vache", "isCorrect": True},
                        {"text": "Génisse de plus de trente mois", "isCorrect": False},
                        {"text": "Jeune bovin femelle", "isCorrect": False},
                        {"text": "Taureillon femelle", "isCorrect": False}
                    ],
                    "correction": "La vache est la femelle adulte de l'espèce bovine ayant mis bas au moins une fois, contrairement à la génisse qui n'a pas encore vêlé."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel os constitue la base osseuse de la région de la cuisse chez le bœuf ?",
                    "answerOptions": [
                        {"text": "Le fémur", "isCorrect": True},
                        {"text": "Le tibia et le péroné", "isCorrect": False},
                        {"text": "La ceinture pelvienne", "isCorrect": False},
                        {"text": "La colonne vertébrale", "isCorrect": False}
                    ],
                    "correction": "Le fémur est l'os unique de la cuisse, s'articulant en haut avec l'os iliaque et en bas avec le tibia."
                },
                {
                    "questionNumber": 3,
                    "question": "Dans la grille de classement EUROP, quelle lettre désigne une conformation supérieure avec un développement musculaire exceptionnel ?",
                    "answerOptions": [
                        {"text": "E", "isCorrect": True},
                        {"text": "U", "isCorrect": False},
                        {"text": "R", "isCorrect": False},
                        {"text": "O", "isCorrect": False}
                    ],
                    "correction": "La grille EUROP classe la conformation de E (Excellente, profil convexe) à P (Médiocre, profil concave)."
                },
                {
                    "questionNumber": 4,
                    "question": "Où se situe précisément le morceau appelé 'araignée' dans une carcasse de bœuf ?",
                    "answerOptions": [
                        {"text": "Dans le creux de l'os iliaque (bassin)", "isCorrect": True},
                        {"text": "Le long des vertèbres cervicales", "isCorrect": False},
                        {"text": "Sur la face externe de l'épaule", "isCorrect": False},
                        {"text": "À l'intérieur de la cage thoracique", "isCorrect": False}
                    ],
                    "correction": "L'araignée est un muscle 'boucher' très tendre situé dans la cavité pelvienne, au niveau du bassin."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle race bovine est réputée pour sa robe froment et sa grande finesse de grain de viande ?",
                    "answerOptions": [
                        {"text": "Limousine", "isCorrect": True},
                        {"text": "Charolaise", "isCorrect": False},
                        {"text": "Prim'Holstein", "isCorrect": False},
                        {"text": "Normande", "isCorrect": False}
                    ],
                    "correction": "La Limousine est une race allaitante rustique, célèbre pour son rendement en viande noble et sa tendreté."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel terme désigne la partie supérieure du thorax, située entre le collier et la côte ?",
                    "answerOptions": [
                        {"text": "Basses côtes", "isCorrect": True},
                        {"text": "Faux-filet", "isCorrect": False},
                        {"text": "Plat de côtes", "isCorrect": False},
                        {"text": "Flanchet", "isCorrect": False}
                    ],
                    "correction": "Les basses côtes sont situées à l'avant de l'animal, faisant suite au collier. C'est une viande savoureuse à griller ou à mijoter."
                },
                {
                    "questionNumber": 7,
                    "question": "Combien de paires de côtes possède une carcasse de bœuf ?",
                    "answerOptions": [
                        {"text": "13 paires", "isCorrect": True},
                        {"text": "10 paires", "isCorrect": False},
                        {"text": "15 paires", "isCorrect": False},
                        {"text": "12 paires", "isCorrect": False}
                    ],
                    "correction": "L'anatomie bovine classique comporte 13 paires de côtes, qui permettent de séparer le quartier avant du quartier arrière."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel morceau du bœuf est considéré comme le plus tendre ?",
                    "answerOptions": [
                        {"text": "Filet", "isCorrect": True},
                        {"text": "Gîte", "isCorrect": False},
                        {"text": "Giron", "isCorrect": False},
                        {"text": "Bavette", "isCorrect": False}
                    ],
                    "correction": "Le filet est un muscle interne peu sollicité, ce qui lui confère une tendreté exceptionnelle."
                },
                {
                    "questionNumber": 9,
                    "question": "Dans le porc, comment appelle-t-on le morceau situé sur le haut de l'épaule utilisé pour le sauté ?",
                    "answerOptions": [
                        {"text": "Échine", "isCorrect": True},
                        {"text": "Jambon", "isCorrect": False},
                        {"text": "Pointe", "isCorrect": False},
                        {"text": "Filet mignon", "isCorrect": False}
                    ],
                    "correction": "L'échine est la partie supérieure du cou du porc, entrelardée de gras, idéale pour les rôtis ou les grillades."
                },
                {
                    "questionNumber": 10,
                    "question": "Comment appelle-t-on la couche de graisse superficielle qui recouvre la carcasse ?",
                    "answerOptions": [
                        {"text": "Le gras de couverture", "isCorrect": True},
                        {"text": "Le persillé", "isCorrect": False},
                        {"text": "Le gras de dépôt", "isCorrect": False},
                        {"text": "La bardière", "isCorrect": False}
                    ],
                    "correction": "Le gras de couverture est évalué lors du classement de la carcasse (note de 1 à 5). Il protège la viande du dessèchement."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel nom porte la vertèbre atlas dans la colonne vertébrale ?",
                    "answerOptions": [
                        {"text": "La première cervicale", "isCorrect": True},
                        {"text": "La dernière lombaire", "isCorrect": False},
                        {"text": "La première sacrée", "isCorrect": False},
                        {"text": "La vertèbre du garrot", "isCorrect": False}
                    ],
                    "correction": "L'atlas (C1) est la première vertèbre cervicale, située juste après le crâne."
                },
                {
                    "questionNumber": 12,
                    "question": "Lequel de ces morceaux appartient à la catégorie des 'morceaux à cuisson rapide' ?",
                    "answerOptions": [
                        {"text": "Le faux-filet", "isCorrect": True},
                        {"text": "Le collier", "isCorrect": False},
                        {"text": "Le jarret", "isCorrect": False},
                        {"text": "Le flanchet", "isCorrect": False}
                    ],
                    "correction": "Le faux-filet fait partie de l'aloyau, destiné à être grillé ou rôti."
                },
                {
                    "questionNumber": 13,
                    "question": "Dans l'agneau, quel morceau correspond à la cuisse ?",
                    "answerOptions": [
                        {"text": "Gigot", "isCorrect": True},
                        {"text": "Épaule", "isCorrect": False},
                        {"text": "Baron", "isCorrect": False},
                        {"text": "Selle", "isCorrect": False}
                    ],
                    "correction": "Le gigot est le membre postérieur de l'agneau, pièce de prédilection pour le rôtissage."
                },
                {
                    "questionNumber": 14,
                    "question": "Qu'est-ce que le persillé dans la viande ?",
                    "answerOptions": [
                        {"text": "Le gras intramusculaire", "isCorrect": True},
                        {"text": "Le gras autour du muscle", "isCorrect": False},
                        {"text": "Un assaisonnement au persil", "isCorrect": False},
                        {"text": "Une maladie de la peau", "isCorrect": False}
                    ],
                    "correction": "Le persillé désigne les fines infiltrations de graisse à l'intérieur des fibres musculaires, signe de goût et de qualité."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel os doit être retiré pour obtenir une escalope de veau ?",
                    "answerOptions": [
                        {"text": "Le fémur", "isCorrect": True},
                        {"text": "L'humérus", "isCorrect": False},
                        {"text": "L'omoplate", "isCorrect": False},
                        {"text": "Le sternum", "isCorrect": False}
                    ],
                    "correction": "L'escalope est prélevée dans la cuisse (noix, sous-noix ou noix pâtissière), articulée autour du fémur."
                },
                {
                    "questionNumber": 16,
                    "question": "À quel âge un bovin mâle devient-il un 'taureau' ?",
                    "answerOptions": [
                        {"text": "Après maturité sexuelle", "isCorrect": True},
                        {"text": "Dès sa naissance", "isCorrect": False},
                        {"text": "À 12 mois", "isCorrect": False},
                        {"text": "S'il est castré", "isCorrect": False}
                    ],
                    "correction": "Le taureau est un mâle entier adulte utilisé pour la reproduction."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est la base osseuse de l'épaule ?",
                    "answerOptions": [
                        {"text": "La scapula (omoplate)", "isCorrect": True},
                        {"text": "Le bassin", "isCorrect": False},
                        {"text": "Le radius", "isCorrect": False},
                        {"text": "Le péroné", "isCorrect": False}
                    ],
                    "correction": "La scapula est l'os plat en forme de triangle qui soutient les muscles de l'épaule."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel morceau est utilisé pour faire les paupiettes de veau ?",
                    "answerOptions": [
                        {"text": "La sous-noix", "isCorrect": True},
                        {"text": "Le jarret", "isCorrect": False},
                        {"text": "La tête", "isCorrect": False},
                        {"text": "Le ris de veau", "isCorrect": False}
                    ],
                    "correction": "On utilise de larges tranches fines prélevées dans la cuisse (sous-noix ou noix)."
                },
                {
                    "questionNumber": 19,
                    "question": "L'onglet est un morceau appartenant à quelle catégorie ?",
                    "answerOptions": [
                        {"text": "Les abats rouges", "isCorrect": True},
                        {"text": "Les pièces nobles", "isCorrect": False},
                        {"text": "Les bas morceaux", "isCorrect": False},
                        {"text": "Les abats blancs", "isCorrect": False}
                    ],
                    "correction": "L'onglet et l'araignée sont techniquement classés parmi les abats rouges bien qu'ils soient des muscles rouges."
                },
                {
                    "questionNumber": 20,
                    "question": "De quel côté de la carcasse doit-on vérifier la présence de la 'manicle' ?",
                    "answerOptions": [
                        {"text": "Côté droit", "isCorrect": True},
                        {"text": "Côté gauche", "isCorrect": False},
                        {"text": "Sur les deux côtés", "isCorrect": False},
                        {"text": "Uniquement sur le quartier avant", "isCorrect": False}
                    ],
                    "correction": "La manicle est une petite partie musculaire liée à la saignée, située uniquement sur le demi-droit."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : HYGIÈNE ET SÉCURITÉ ALIMENTAIRE (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : HYGIÈNE ET SÉCURITÉ ALIMENTAIRE",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la température maximale légale de conservation des viandes fraîches de boucherie ?",
                    "answerOptions": [
                        {"text": "7 °C", "isCorrect": True},
                        {"text": "10 °C", "isCorrect": False},
                        {"text": "3 °C", "isCorrect": False},
                        {"text": "0 °C", "isCorrect": False}
                    ],
                    "correction": "Pour la viande fraîche (bœuf, veau, agneau, porc), la température réglementaire est de +7 °C maximum, bien que l'idéal soit entre 0 et 4 °C."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle bactérie pathogène est particulièrement redoutée car elle peut se multiplier au froid ?",
                    "answerOptions": [
                        {"text": "Listeria monocytogenes", "isCorrect": True},
                        {"text": "Staphylocoque doré", "isCorrect": False},
                        {"text": "Salmonelle", "isCorrect": False},
                        {"text": "Bacillus cereus", "isCorrect": False}
                    ],
                    "correction": "Listeria est une bactérie psychrotrophe, capable de survivre et de se multiplier lentement entre 0 et 4 °C."
                },
                {
                    "questionNumber": 23,
                    "question": "Comment appelle-t-on le document qui consigne le nettoyage quotidien de l'atelier ?",
                    "answerOptions": [
                        {"text": "Le plan de nettoyage et de désinfection", "isCorrect": True},
                        {"text": "Le registre du personnel", "isCorrect": False},
                        {"text": "La fiche de stock", "isCorrect": False},
                        {"text": "Le carnet de bord", "isCorrect": False}
                    ],
                    "correction": "Ce document fait partie du PMS (Plan de Maîtrise Sanitaire) obligatoire pour la traçabilité de l'hygiène."
                },
                {
                    "questionNumber": 24,
                    "question": "À partir de quelle température l'eau des stérilisateurs à couteaux doit-elle être maintenue ?",
                    "answerOptions": [
                        {"text": "82 °C", "isCorrect": True},
                        {"text": "63 °C", "isCorrect": False},
                        {"text": "100 °C", "isCorrect": False},
                        {"text": "45 °C", "isCorrect": False}
                    ],
                    "correction": "Une eau à 82 °C minimum garantit la destruction efficace des micro-organismes sur les lames."
                },
                {
                    "questionNumber": 25,
                    "question": "Que signifie le sigle PMS ?",
                    "answerOptions": [
                        {"text": "Plan de Maîtrise Sanitaire", "isCorrect": True},
                        {"text": "Protection de la Matière Sèche", "isCorrect": False},
                        {"text": "Produit Médical Spécifique", "isCorrect": False},
                        {"text": "Poids Moyen des Saucisses", "isCorrect": False}
                    ],
                    "correction": "Le PMS regroupe l'HACCP, les bonnes pratiques d'hygiène et la gestion de la traçabilité."
                },
                {
                    "questionNumber": 26,
                    "question": "Où se situe le réservoir principal de bactéries sur un manipulateur ?",
                    "answerOptions": [
                        {"text": "Les mains et les cheveux", "isCorrect": True},
                        {"text": "Les pieds", "isCorrect": False},
                        {"text": "Le dos", "isCorrect": False},
                        {"text": "Les vêtements de ville", "isCorrect": False}
                    ],
                    "correction": "Les mains sont le principal vecteur de contamination croisée (manuportage)."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le pH idéal d'une viande saine après maturation ?",
                    "answerOptions": [
                        {"text": "Entre 5,4 et 5,8", "isCorrect": True},
                        {"text": "Au-dessus de 7", "isCorrect": False},
                        {"text": "Exactement 4,2", "isCorrect": False},
                        {"text": "Moins de 3", "isCorrect": False}
                    ],
                    "correction": "L'acidification (baisse du pH) protège la viande contre les bactéries de putréfaction."
                },
                {
                    "questionNumber": 28,
                    "question": "Que signifie la marche en avant en boucherie ?",
                    "answerOptions": [
                        {"text": "Les produits propres ne croisent jamais les produits sales", "isCorrect": True},
                        {"text": "Le boucher doit toujours marcher face à lui", "isCorrect": False},
                        {"text": "Le client circule dans un seul sens dans la boutique", "isCorrect": False},
                        {"text": "La découpe se fait de l'avant vers l'arrière", "isCorrect": False}
                    ],
                    "correction": "C'est un principe d'organisation spatiale ou temporelle pour éviter les contaminations."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la durée de validité d'une DLC ?",
                    "answerOptions": [
                        {"text": "Fixée par le fabricant après tests", "isCorrect": True},
                        {"text": "Toujours 1 an", "isCorrect": False},
                        {"text": "Illimitée si c'est au froid", "isCorrect": False},
                        {"text": "10 jours maximum", "isCorrect": False}
                    ],
                    "correction": "La Date Limite de Consommation est déterminée par des analyses microbiologiques."
                },
                {
                    "questionNumber": 30,
                    "question": "Dans le cercle de Sinner, quel facteur correspond au brossage ?",
                    "answerOptions": [
                        {"text": "Action mécanique", "isCorrect": True},
                        {"text": "Action chimique", "isCorrect": False},
                        {"text": "Température", "isCorrect": False},
                        {"text": "Temps d'action", "isCorrect": False}
                    ],
                    "correction": "Le frottement (brosse) est l'énergie mécanique indispensable pour décoller les souillures."
                },
                {
                    "questionNumber": 31,
                    "question": "Qu'est-ce qu'une TIAC ?",
                    "answerOptions": [
                        {"text": "Toxi-Infection Alimentaire Collective", "isCorrect": True},
                        {"text": "Taux d'Infection Alimentaire Critique", "isCorrect": False},
                        {"text": "Traitement Interdit après Cuisson", "isCorrect": False},
                        {"text": "Tension Inter-Artérielle Capillaire", "isCorrect": False}
                    ],
                    "correction": "C'est l'apparition de symptômes digestifs chez au moins 2 personnes ayant mangé le même aliment."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le rôle du détergent ?",
                    "answerOptions": [
                        {"text": "Nettoyer (enlever le gras)", "isCorrect": True},
                        {"text": "Tuer les bactéries", "isCorrect": False},
                        {"text": "Faire briller les couteaux", "isCorrect": False},
                        {"text": "Parfumer le laboratoire", "isCorrect": False}
                    ],
                    "correction": "Un détergent retire la saleté visible. Pour tuer les microbes, il faut un désinfectant."
                },
                {
                    "questionNumber": 33,
                    "question": "Peut-on congeler une viande qui a été décongelée ?",
                    "answerOptions": [
                        {"text": "Non jamais", "isCorrect": True},
                        {"text": "Oui si c'est rapide", "isCorrect": False},
                        {"text": "Uniquement si on la cuit d'abord", "isCorrect": False},
                        {"text": "Si le client est d'accord", "isCorrect": False}
                    ],
                    "correction": "La recongélation d'un produit décongelé favorise une prolifération bactérienne dangereuse."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la température de conservation des abats ?",
                    "answerOptions": [
                        {"text": "3 °C maximum", "isCorrect": True},
                        {"text": "10 °C", "isCorrect": False},
                        {"text": "7 °C", "isCorrect": False},
                        {"text": "0 °C", "isCorrect": False}
                    ],
                    "correction": "Les abats sont des produits très périssables, la norme est de +3 °C."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel parasite est cherché dans le muscle de porc à l'abattoir ?",
                    "answerOptions": [
                        {"text": "La trichine", "isCorrect": True},
                        {"text": "Le ténia", "isCorrect": False},
                        {"text": "Le varroa", "isCorrect": False},
                        {"text": "La listeria", "isCorrect": False}
                    ],
                    "correction": "La trichine est un ver parasite. Un contrôle vétérinaire systématique est effectué sur les porcs et sangliers."
                },
                {
                    "questionNumber": 36,
                    "question": "À quoi sert un protocole d'hygiène ?",
                    "answerOptions": [
                        {"text": "Uniformiser les méthodes de travail et garantir la sécurité", "isCorrect": True},
                        {"text": "Calculer le temps de pause", "isCorrect": False},
                        {"text": "Ranger les outils décoratifs", "isCorrect": False},
                        {"text": "Choisir la couleur de la tenue", "isCorrect": False}
                    ],
                    "correction": "Il définit 'Qui fait quoi, comment et quand' pour garantir la salubrité."
                },
                {
                    "questionNumber": 37,
                    "question": "Qu'est-ce que le 'ressemelage' des mains ?",
                    "answerOptions": [
                        {"text": "Le lavage et la désinfection systématique des mains", "isCorrect": True},
                        {"text": "Le port de nouvelles chaussures de sécurité", "isCorrect": False},
                        {"text": "L'utilisation de gants en laine", "isCorrect": False},
                        {"text": "Une technique de massage des articulations", "isCorrect": False}
                    ],
                    "correction": "Il s'agit du processus rigoureux de nettoyage des mains entre deux tâches."
                },
                {
                    "questionNumber": 38,
                    "question": "Comment décongeler une viande en sécurité ?",
                    "answerOptions": [
                        {"text": "Au réfrigérateur entre 0 et 4 degrés", "isCorrect": True},
                        {"text": "À température ambiante", "isCorrect": False},
                        {"text": "Dans de l'eau tiède", "isCorrect": False},
                        {"text": "Sous le soleil", "isCorrect": False}
                    ],
                    "correction": "La décongélation lente au froid positif limite le réveil bactérien."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle est la zone de danger pour les bactéries ?",
                    "answerOptions": [
                        {"text": "De 10 à 63 degrés", "isCorrect": True},
                        {"text": "Moins de 0 degré", "isCorrect": False},
                        {"text": "Au-dessus de 100 degrés", "isCorrect": False},
                        {"text": "Entre 0 et 4 degrés", "isCorrect": False}
                    ],
                    "correction": "C'est dans cette plage de température tiède que les bactéries se divisent le plus vite."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle information est capitale pour assurer la traçabilité ?",
                    "answerOptions": [
                        {"text": "Le numéro de lot", "isCorrect": True},
                        {"text": "Le prix de vente", "isCorrect": False},
                        {"text": "La marque du couteau", "isCorrect": False},
                        {"text": "L'adresse du client", "isCorrect": False}
                    ],
                    "correction": "Le numéro de lot permet de remonter jusqu'à l'animal et à l'abattoir en cas d'alerte sanitaire."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : PRÉPARATIONS BOUCHÈRES ET CHARCUTIÈRES (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : PRÉPARATIONS BOUCHÈRES ET CHARCUTIÈRES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le liant principal utilisé dans la fabrication d'une terrine de campagne ?",
                    "answerOptions": [
                        {"text": "L'œuf et la gorge de porc hachée", "isCorrect": True},
                        {"text": "La farine de blé pure", "isCorrect": False},
                        {"text": "L'amidon de maïs", "isCorrect": False},
                        {"text": "La chapelure blonde", "isCorrect": False}
                    ],
                    "correction": "La liaison est assurée par la coagulation des protéines de l'œuf et l'émulsion du gras (gorge) à la cuisson."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la proportion habituelle de sel nitrité pour une farce à pâté fine ?",
                    "answerOptions": [
                        {"text": "15 à 18 grammes par kilo", "isCorrect": True},
                        {"text": "50 grammes par kilo", "isCorrect": False},
                        {"text": "2 grammes par kilo", "isCorrect": False},
                        {"text": "100 grammes par kilo", "isCorrect": False}
                    ],
                    "correction": "L'assaisonnement standard en sel se situe entre 15 et 20g/kg selon les goûts et les recettes."
                },
                {
                    "questionNumber": 43,
                    "question": "À quoi sert le bardage d'un rôti de bœuf ?",
                    "answerOptions": [
                        {"text": "Protéger la viande du dessèchement à la cuisson", "isCorrect": True},
                        {"text": "Augmenter le poids de vente", "isCorrect": False},
                        {"text": "Saler la viande à cœur", "isCorrect": False},
                        {"text": "Donner une couleur rouge", "isCorrect": False}
                    ],
                    "correction": "La barde (gras de porc) isole la viande de la chaleur directe du four et l'arrose de gras fondant."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel boyau utilise-t-on pour fabriquer des chipolatas ?",
                    "answerOptions": [
                        {"text": "Menu de mouton", "isCorrect": True},
                        {"text": "Chaudin de porc", "isCorrect": False},
                        {"text": "Baudruche de bœuf", "isCorrect": False},
                        {"text": "Menu de porc", "isCorrect": False}
                    ],
                    "correction": "Le menu de mouton est de petit diamètre (20/22 ou 22/24), parfait pour les chipos et les merguez."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment appelle-t-on l'action d'envelopper un morceau de viande avec des tranches de lard ?",
                    "answerOptions": [
                        {"text": "Le bardage", "isCorrect": True},
                        {"text": "Le lardage", "isCorrect": False},
                        {"text": "Le ficelage", "isCorrect": False},
                        {"text": "Le crépinnage", "isCorrect": False}
                    ],
                    "correction": "Le bardage consiste à recouvrir la surface. Le lardage consiste à insérer des bâtonnets de gras à l'intérieur du muscle."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la base d'une farce mousseline ?",
                    "answerOptions": [
                        {"text": "Chair maigre hachée très fin et crème", "isCorrect": True},
                        {"text": "Morceaux de viande rissolés", "isCorrect": False},
                        {"text": "Gras de porc et oignons", "isCorrect": False},
                        {"text": "Sang de bœuf et épices", "isCorrect": False}
                    ],
                    "correction": "La farce mousseline est une préparation fine, légère et onctueuse montée à la crème liquide."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel ingrédient est spécifique au boudin noir ?",
                    "answerOptions": [
                        {"text": "Le sang", "isCorrect": True},
                        {"text": "Le foie", "isCorrect": False},
                        {"text": "Le ris", "isCorrect": False},
                        {"text": "La cervelle", "isCorrect": False}
                    ],
                    "correction": "Le boudin noir est un mélange de sang, de gras (panne ou gorge) et d'oignons."
                },
                {
                    "questionNumber": 48,
                    "question": "Que contient une 'crépine' ?",
                    "answerOptions": [
                        {"text": "Une membrane graisseuse de l'abdomen", "isCorrect": True},
                        {"text": "Le tissu de la gorge", "isCorrect": False},
                        {"text": "La peau du dos", "isCorrect": False},
                        {"text": "Les intestins grêles", "isCorrect": False}
                    ],
                    "correction": "Aussi appelée coiffe, la crépine sert à maintenir les crépinettes et les pâtés lors de la cuisson."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est la température de cuisson à cœur d'un jambon cuit ?",
                    "answerOptions": [
                        {"text": "68 °C à 70 °C", "isCorrect": True},
                        {"text": "100 °C", "isCorrect": False},
                        {"text": "45 °C", "isCorrect": False},
                        {"text": "85 °C", "isCorrect": False}
                    ],
                    "correction": "Une cuisson lente à juste température garantit le moelleux et la sécurité sanitaire."
                },
                {
                    "questionNumber": 50,
                    "question": "À quoi sert le sucre dans les salaisons (saucissons) ?",
                    "answerOptions": [
                        {"text": "Nourrir les ferments lactiques", "isCorrect": True},
                        {"text": "Sucrer le goût de la viande", "isCorrect": False},
                        {"text": "Empêcher le séchage", "isCorrect": False},
                        {"text": "Changer la couleur en bleu", "isCorrect": False}
                    ],
                    "correction": "Le sucre (dextrose) est transformé par les ferments en acide lactique, ce qui acidifie et conserve le produit."
                },
                {
                    "questionNumber": 51,
                    "question": "Qu'est-ce qu'une marinade ?",
                    "answerOptions": [
                        {"text": "Un liquide aromatique pour attendrir et parfumer", "isCorrect": True},
                        {"text": "Une technique de découpe en mer", "isCorrect": False},
                        {"text": "Une sauce pour napper les frites", "isCorrect": False},
                        {"text": "Un mode de cuisson à la vapeur", "isCorrect": False}
                    ],
                    "correction": "La marinade (acide + aromates + huile) commence une pré-cuisson chimique qui attendrit les fibres."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le but du ficelage ?",
                    "answerOptions": [
                        {"text": "Maintenir la forme à la cuisson", "isCorrect": True},
                        {"text": "Calculer la longueur du rôti", "isCorrect": False},
                        {"text": "Transporter la viande plus facilement", "isCorrect": False},
                        {"text": "Empêcher le client d'ouvrir le paquet", "isCorrect": False}
                    ],
                    "correction": "Le ficelage assure une cuisson uniforme en évitant que le morceau ne s'affaisse."
                },
                {
                    "questionNumber": 53,
                    "question": "Qu'est-ce que l'opération de 'poussage' ?",
                    "answerOptions": [
                        {"text": "Mettre la farce dans le boyau", "isCorrect": True},
                        {"text": "Vendre un produit plus cher", "isCorrect": False},
                        {"text": "Installer les carcasses dans le frigo", "isCorrect": False},
                        {"text": "Augmenter la vitesse du hachoir", "isCorrect": False}
                    ],
                    "correction": "On utilise un poussoir hydraulique ou manuel pour remplir les boyaux de farce."
                },
                {
                    "questionNumber": 54,
                    "question": "Qu'est-ce que la 'fleur' sur un saucisson ?",
                    "answerOptions": [
                        {"text": "Une moisissure noble de surface", "isCorrect": True},
                        {"text": "Un décor gravé au couteau", "isCorrect": False},
                        {"text": "Une infusion de plantes", "isCorrect": False},
                        {"text": "Une maladie du boyau", "isCorrect": False}
                    ],
                    "correction": "La fleur (pénicillium) protège le saucisson et développe ses arômes."
                },
                {
                    "questionNumber": 55,
                    "question": "Pourquoi dégraisse-t-on les jambons ?",
                    "answerOptions": [
                        {"text": "Pour respecter les critères de santé et d'esthétique", "isCorrect": True},
                        {"text": "Pour cacher la provenance", "isCorrect": False},
                        {"text": "Pour que le jambon soit plus lourd", "isCorrect": False},
                        {"text": "Parce que le gras est interdit en France", "isCorrect": False}
                    ],
                    "correction": "On retire l'excès de gras superficiel (couenne et sous-cutané) pour un produit fini équilibré."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle est la particularité d'un jambon sec par rapport à un jambon cuit ?",
                    "answerOptions": [
                        {"text": "Il n'est pas cuit à la chaleur", "isCorrect": True},
                        {"text": "Il contient plus d'eau", "isCorrect": False},
                        {"text": "Il est fabriqué avec du bœuf", "isCorrect": False},
                        {"text": "Il se garde moins longtemps", "isCorrect": False}
                    ],
                    "correction": "Le jambon sec est conservé par le sel et la déshydratation lente (séchage)."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'est-ce que le 'parage' d'un muscle ?",
                    "answerOptions": [
                        {"text": "Retirer les parties non nobles (gras, nerfs)", "isCorrect": True},
                        {"text": "Compter les morceaux avant la vente", "isCorrect": False},
                        {"text": "Mesurer l'épaisseur des tranches", "isCorrect": False},
                        {"text": "Mettre le morceau en vitrine", "isCorrect": False}
                    ],
                    "correction": "Le parage rend le morceau présentable et prêt à la consommation."
                },
                {
                    "questionNumber": 58,
                    "question": "Qu'est-ce qu'une farce ?",
                    "answerOptions": [
                        {"text": "Un mélange haché de viandes et d'aromates", "isCorrect": True},
                        {"text": "Une blague faite entre collègues", "isCorrect": False},
                        {"text": "Une sauce très épaisse", "isCorrect": False},
                        {"text": "Une technique de décoration", "isCorrect": False}
                    ],
                    "correction": "La farce sert de base aux terrines, pâtés et saucisses."
                },
                {
                    "questionNumber": 59,
                    "question": "Comment appelle-t-on le gras utilisé en charcuterie venant du ventre du porc ?",
                    "answerOptions": [
                        {"text": "La panne", "isCorrect": True},
                        {"text": "La bardière", "isCorrect": False},
                        {"text": "La couenne", "isCorrect": False},
                        {"text": "Le suif", "isCorrect": False}
                    ],
                    "correction": "La panne est un gras mou situé dans la cavité abdominale, idéal pour faire du saindoux."
                },
                {
                    "questionNumber": 60,
                    "question": "Pourquoi utilise-t-on de la glace pilée dans le cutter lors du hachage fin ?",
                    "answerOptions": [
                        {"text": "Pour éviter l'échauffement de la farce", "isCorrect": True},
                        {"text": "Pour laver la viande", "isCorrect": False},
                        {"text": "Pour augmenter le sel", "isCorrect": False},
                        {"text": "Pour changer la couleur", "isCorrect": False}
                    ],
                    "correction": "Le frottement des lames chauffe la farce, ce qui pourrait faire fondre le gras et gâcher l'émulsion."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : OUTILLAGE ET TECHNOLOGIE DES ÉQUIPEMENTS (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : OUTILLAGE ET TECHNOLOGIE DES ÉQUIPEMENTS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "À quoi sert le fusil en boucherie ?",
                    "answerOptions": [
                        {"text": "Entretenir le fil du couteau", "isCorrect": True},
                        {"text": "Affûter une lame très émoussée", "isCorrect": False},
                        {"text": "Découper les os de la carcasse", "isCorrect": False},
                        {"text": "Mesurer l'épaisseur du gras", "isCorrect": False}
                    ],
                    "correction": "Le fusil sert à redresser le 'morailles' (le fil) de la lame. Pour un affûtage profond, on utilise une meule."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la fonction d'un 'cutter' en boucherie-charcuterie ?",
                    "answerOptions": [
                        {"text": "Hacher et émulsionner finement les farces", "isCorrect": True},
                        {"text": "Trancher le jambon en lamelles", "isCorrect": False},
                        {"text": "Scier les quartiers de bœuf", "isCorrect": False},
                        {"text": "Vider les abats de volaille", "isCorrect": False}
                    ],
                    "correction": "Le cutter possède des couteaux tournant à haute vitesse dans une cuve rotative pour obtenir des pâtes fines."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on le couteau à lame courte et rigide utilisé pour le désossage ?",
                    "answerOptions": [
                        {"text": "Désosseur", "isCorrect": True},
                        {"text": "Tranchelard", "isCorrect": False},
                        {"text": "Cimeterre", "isCorrect": False},
                        {"text": "Feuille", "isCorrect": False}
                    ],
                    "correction": "Le désosseur permet une précision maximale pour suivre les os et délier les muscles."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel outil est utilisé pour fendre une carcasse en deux à l'abattoir ?",
                    "answerOptions": [
                        {"text": "Scie à fendre", "isCorrect": True},
                        {"text": "Couteau de chef", "isCorrect": False},
                        {"text": "Feuille de boucher", "isCorrect": False},
                        {"text": "Éplucheur", "isCorrect": False}
                    ],
                    "correction": "La scie (souvent électrique) permet de couper la colonne vertébrale proprement en deux demi-carcasses."
                },
                {
                    "questionNumber": 65,
                    "question": "À quoi sert la 'pince à dénerver' ?",
                    "answerOptions": [
                        {"text": "Retirer les tendons difficiles d'accès", "isCorrect": True},
                        {"text": "Attacher les rôtis", "isCorrect": False},
                        {"text": "Soulever les quartiers", "isCorrect": False},
                        {"text": "Aplatir les escalopes", "isCorrect": False}
                    ],
                    "correction": "Elle permet de saisir fermement les nerfs et aponévroses pour les extraire proprement."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel équipement protège le boucher contre les coups de couteau au ventre ?",
                    "answerOptions": [
                        {"text": "Tablier métallique (cotte de mailles)", "isCorrect": True},
                        {"text": "Gilet de sauvetage", "isCorrect": False},
                        {"text": "Tablier en coton blanc", "isCorrect": False},
                        {"text": "Veste de cuisine", "isCorrect": False}
                    ],
                    "correction": "Le tablier en anneaux d'inox est un EPI indispensable lors du désossage et du parage."
                },
                {
                    "questionNumber": 67,
                    "question": "Comment entretenir une planche à découper en polyéthylène ?",
                    "answerOptions": [
                        {"text": "Raclage et désinfection quotidienne", "isCorrect": True},
                        {"text": "Peinture annuelle", "isCorrect": False},
                        {"text": "Trempage dans l'huile d'olive", "isCorrect": False},
                        {"text": "La laisser sécher au soleil", "isCorrect": False}
                    ],
                    "correction": "Le racloir permet d'enlever les micro-rayures où se logent les bactéries."
                },
                {
                    "questionNumber": 68,
                    "question": "À quoi sert l'aiguille à larder ?",
                    "answerOptions": [
                        {"text": "Introduire des bâtonnets de gras dans un muscle", "isCorrect": True},
                        {"text": "Coudre les sacs de transport", "isCorrect": False},
                        {"text": "Vérifier la température du frigo", "isCorrect": False},
                        {"text": "Nettoyer les os de moelle", "isCorrect": False}
                    ],
                    "correction": "Elle traverse la viande pour y déposer du lard afin de la nourrir de l'intérieur."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel appareil est utilisé pour maintenir la viande sous vide ?",
                    "answerOptions": [
                        {"text": "Machine à cloche", "isCorrect": True},
                        {"text": "Batteur mélangeur", "isCorrect": False},
                        {"text": "Autoclave", "isCorrect": False},
                        {"text": "Four à convection", "isCorrect": False}
                    ],
                    "correction": "La machine à cloche extrait l'air du sachet et le soude hermétiquement."
                },
                {
                    "questionNumber": 70,
                    "question": "Qu'est-ce qu'une 'feuille' en boucherie ?",
                    "answerOptions": [
                        {"text": "Un couteau large et lourd pour fendre ou concasser", "isCorrect": True},
                        {"text": "Un papier pour emballer les biftecks", "isCorrect": False},
                        {"text": "Une partie fine de l'oreille du porc", "isCorrect": False},
                        {"text": "Un outil pour écrire les prix", "isCorrect": False}
                    ],
                    "correction": "La feuille permet de trancher les os ou de fendre de petites pièces grâce à son poids et son inertie."
                },
                {
                    "questionNumber": 71,
                    "question": "À quoi sert le 'poussoir' ?",
                    "answerOptions": [
                        {"text": "Embosser les saucisses et boudins", "isCorrect": True},
                        {"text": "Pousser les chariots de viande", "isCorrect": False},
                        {"text": "Fermer la porte de la chambre froide", "isCorrect": False},
                        {"text": "Appuyer sur le bouton d'urgence", "isCorrect": False}
                    ],
                    "correction": "Le poussoir injecte la farce dans le boyau de manière régulière."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le risque de passer un couteau au lave-vaisselle ?",
                    "answerOptions": [
                        {"text": "Détremper l'acier et abîmer le manche", "isCorrect": True},
                        {"text": "Changer la couleur de la lame en rose", "isCorrect": False},
                        {"text": "Le rendre trop coupant et dangereux", "isCorrect": False},
                        {"text": "Raccourcir la longueur de la lame", "isCorrect": False}
                    ],
                    "correction": "La chaleur et les détergents agressifs endommagent le fil de la lame et les matériaux du manche."
                },
                {
                    "questionNumber": 73,
                    "question": "Comment désinfecter un hachoir électrique ?",
                    "answerOptions": [
                        {"text": "Démontage complet et nettoyage de chaque pièce", "isCorrect": True},
                        {"text": "Passer un chiffon humide sur l'extérieur uniquement", "isCorrect": False},
                        {"text": "Faire passer de l'eau savonneuse dedans en marche", "isCorrect": False},
                        {"text": "Le mettre entier dans une cuve de désinfectant", "isCorrect": False}
                    ],
                    "correction": "Le hachage favorise la contamination. Le démontage est la seule garantie de propreté."
                },
                {
                    "questionNumber": 74,
                    "question": "Qu'est-ce qu'une 'bascule' en boucherie ?",
                    "answerOptions": [
                        {"text": "Une balance pour peser les grosses pièces", "isCorrect": True},
                        {"text": "Un rail de transport suspendu", "isCorrect": False},
                        {"text": "Une technique pour retourner un bœuf", "isCorrect": False},
                        {"text": "Un type de crochet à viande", "isCorrect": False}
                    ],
                    "correction": "Elle permet de peser les carcasses à l'arrivée des livraisons."
                },
                {
                    "questionNumber": 75,
                    "question": "À quoi servent les crochets 'esse' ?",
                    "answerOptions": [
                        {"text": "Suspendre la viande aux rails", "isCorrect": True},
                        {"text": "Attacher les étiquettes de prix", "isCorrect": False},
                        {"text": "Nettoyer les recoins du hachoir", "isCorrect": False},
                        {"text": "Ficeler les rôtis de veau", "isCorrect": False}
                    ],
                    "correction": "En forme de S, ils sont en inox pour l'hygiène."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle est l'utilité d'une 'cellule de refroidissement rapide' ?",
                    "answerOptions": [
                        {"text": "Traverser la zone de danger microbien le plus vite possible", "isCorrect": True},
                        {"text": "Stocker la viande pendant un mois", "isCorrect": False},
                        {"text": "Congeler les produits instantanément", "isCorrect": False},
                        {"text": "Chauffer les pâtés avant la vente", "isCorrect": False}
                    ],
                    "correction": "Elle permet de descendre de 63°C à 10°C en moins de 2 heures."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel matériau est privilégié pour les plans de travail en boucherie ?",
                    "answerOptions": [
                        {"text": "Inox ou polyéthylène", "isCorrect": True},
                        {"text": "Bois de chêne", "isCorrect": False},
                        {"text": "Aluminium brut", "isCorrect": False},
                        {"text": "Marbre de Carrare", "isCorrect": False}
                    ],
                    "correction": "Ces matériaux sont lisses, non poreux et faciles à désinfecter."
                },
                {
                    "questionNumber": 78,
                    "question": "À quoi sert un 'viscosimètre' (rare mais possible en industrie charcutière) ?",
                    "answerOptions": [
                        {"text": "Mesurer l'épaisseur d'une sauce ou d'une saumure", "isCorrect": True},
                        {"text": "Peser les épices au gramme près", "isCorrect": False},
                        {"text": "Calculer la vitesse du hachoir", "isCorrect": False},
                        {"text": "Vérifier le taux de sel", "isCorrect": False}
                    ],
                    "correction": "Il mesure la résistance à l'écoulement d'un liquide."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment appelle-t-on l'appareil qui retire la couenne du porc mécaniquement ?",
                    "answerOptions": [
                        {"text": "Une couenneuse", "isCorrect": True},
                        {"text": "Une plumeuse", "isCorrect": False},
                        {"text": "Une ponceuse", "isCorrect": False},
                        {"text": "Une trancheuse", "isCorrect": False}
                    ],
                    "correction": "Elle sépare la peau du gras de manière rapide et régulière."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le rôle du 'poussoir sous vide' ?",
                    "answerOptions": [
                        {"text": "Éviter les bulles d'air dans les saucissons", "isCorrect": True},
                        {"text": "Augmenter le poids de la farce", "isCorrect": False},
                        {"text": "Chauffer le produit pendant l'embossage", "isCorrect": False},
                        {"text": "Vendre les produits à distance", "isCorrect": False}
                    ],
                    "correction": "L'absence d'air limite l'oxydation et améliore la conservation et l'esthétique."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : GESTION, COMMERCIALISATION ET RÉGLEMENTATION (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : GESTION, COMMERCIALISATION ET RÉGLEMENTATION",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle mention d'origine est obligatoire pour la viande bovine en France ?",
                    "answerOptions": [
                        {"text": "Lieu de naissance, d'élevage et d'abattage", "isCorrect": True},
                        {"text": "Nom de l'éleveur uniquement", "isCorrect": False},
                        {"text": "Prix au kilo seulement", "isCorrect": False},
                        {"text": "Date de naissance de l'animal", "isCorrect": False}
                    ],
                    "correction": "La traçabilité bovine impose d'indiquer tout le parcours de l'animal."
                },
                {
                    "questionNumber": 82,
                    "question": "Que signifie le sigle 'VBF' ?",
                    "answerOptions": [
                        {"text": "Viande Bovine Française", "isCorrect": True},
                        {"text": "Veau Blanc de France", "isCorrect": False},
                        {"text": "Vente de Boucherie Fine", "isCorrect": False},
                        {"text": "Viande de Boeuf Fermier", "isCorrect": False}
                    ],
                    "correction": "Ce logo garantit que l'animal est né, a été élevé et abattu en France."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la définition de la 'démarque inconnue' ?",
                    "answerOptions": [
                        {"text": "La différence entre le stock théorique et le stock réel (vols, erreurs)", "isCorrect": True},
                        {"text": "La viande que le boucher ne connaît pas", "isCorrect": False},
                        {"text": "Les invendus de la semaine", "isCorrect": False},
                        {"text": "Les cadeaux faits aux clients", "isCorrect": False}
                    ],
                    "correction": "C'est une perte financière qu'il faut limiter."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le taux de TVA sur la viande transformée (ex: pâté fabriqué par le boucher) ?",
                    "answerOptions": [
                        {"text": "5,5 % (produit alimentaire)", "isCorrect": True},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "10 %", "isCorrect": False},
                        {"text": "2,1 %", "isCorrect": False}
                    ],
                    "correction": "Les produits alimentaires vendus à emporter sont au taux réduit de 5,5%."
                },
                {
                    "questionNumber": 85,
                    "question": "Comment calcule-t-on la marge brute ?",
                    "answerOptions": [
                        {"text": "Prix de vente HT - Coût d'achat HT", "isCorrect": True},
                        {"text": "Chiffre d'affaires - Salaires", "isCorrect": False},
                        {"text": "Total de la caisse - TVA", "isCorrect": False},
                        {"text": "Prix d'achat + Bénéfice", "isCorrect": False}
                    ],
                    "correction": "La marge brute permet de payer les charges fixes et de dégager un bénéfice."
                },
                {
                    "questionNumber": 86,
                    "question": "Que signifie le label 'Label Rouge' ?",
                    "answerOptions": [
                        {"text": "Une qualité supérieure par rapport au produit courant", "isCorrect": True},
                        {"text": "Une viande de couleur très rouge", "isCorrect": False},
                        {"text": "Une origine régionale uniquement", "isCorrect": False},
                        {"text": "Un produit issu de l'agriculture biologique", "isCorrect": False}
                    ],
                    "correction": "Il repose sur un cahier des charges strict validé par l'INAO."
                },
                {
                    "questionNumber": 87,
                    "question": "À quoi sert le 'ticket de pesée' ?",
                    "answerOptions": [
                        {"text": "Justifier le prix et le poids au client", "isCorrect": True},
                        {"text": "Décorer l'emballage", "isCorrect": False},
                        {"text": "Donner la recette du plat", "isCorrect": False},
                        {"text": "Calculer l'âge du boucher", "isCorrect": False}
                    ],
                    "correction": "C'est un document obligatoire pour la transparence commerciale."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'une fiche de réception ?",
                    "answerOptions": [
                        {"text": "Un contrôle des marchandises à la livraison (poids, température)", "isCorrect": True},
                        {"text": "Une lettre de remerciement au fournisseur", "isCorrect": False},
                        {"text": "Le menu du jour", "isCorrect": False},
                        {"text": "La liste des clients fidèles", "isCorrect": False}
                    ],
                    "correction": "Elle garantit que les produits entrant respectent les normes."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la règle d'affichage des prix en vitrine ?",
                    "answerOptions": [
                        {"text": "Le prix doit être au kilo ou à la pièce, visible de l'extérieur", "isCorrect": True},
                        {"text": "Le prix est facultatif si le boucher est sympa", "isCorrect": False},
                        {"text": "Uniquement les promotions doivent être affichées", "isCorrect": False},
                        {"text": "Les prix doivent être écrits en petit", "isCorrect": False}
                    ],
                    "correction": "C'est une obligation légale vis-à-vis du code de la consommation."
                },
                {
                    "questionNumber": 90,
                    "question": "Qu'est-ce que l'inventaire ?",
                    "answerOptions": [
                        {"text": "Compter physiquement tout le stock à une date précise", "isCorrect": True},
                        {"text": "Faire le ménage dans les tiroirs", "isCorrect": False},
                        {"text": "Demander au fournisseur ce qu'il lui reste", "isCorrect": False},
                        {"text": "Imaginer ce que l'on va vendre demain", "isCorrect": False}
                    ],
                    "correction": "L'inventaire est obligatoire pour établir le bilan annuel de l'entreprise."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le rôle de la 'fiche de stock' ?",
                    "answerOptions": [
                        {"text": "Suivre les entrées et sorties de marchandises", "isCorrect": True},
                        {"text": "Noter le nom des employés", "isCorrect": False},
                        {"text": "Écrire les recettes de cuisine", "isCorrect": False},
                        {"text": "Calculer la TVA", "isCorrect": False}
                    ],
                    "correction": "Elle permet une gestion rigoureuse et évite les ruptures de stock."
                },
                {
                    "questionNumber": 92,
                    "question": "Que signifie le sigle 'AOC' ?",
                    "answerOptions": [
                        {"text": "Appellation d'Origine Contrôlée", "isCorrect": True},
                        {"text": "Achat Organisé en Commun", "isCorrect": False},
                        {"text": "Alimentation d'Origine Certifiée", "isCorrect": False},
                        {"text": "Accord de Qualité Supérieure", "isCorrect": False}
                    ],
                    "correction": "Il garantit un lien entre le produit, le terroir et le savoir-faire."
                },
                {
                    "questionNumber": 93,
                    "question": "Qu'est-ce que le 'coefficient multiplicateur' ?",
                    "answerOptions": [
                        {"text": "Le chiffre par lequel on multiplie le prix d'achat pour obtenir le prix de vente", "isCorrect": True},
                        {"text": "Le nombre d'enfants du patron", "isCorrect": False},
                        {"text": "Le poids d'une carcasse divisé par 10", "isCorrect": False},
                        {"text": "La remise accordée par le fournisseur", "isCorrect": False}
                    ],
                    "correction": "Il inclut la marge et la TVA."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel document accompagne obligatoirement une livraison ?",
                    "answerOptions": [
                        {"text": "Le bon de livraison", "isCorrect": True},
                        {"text": "Le journal intime du chauffeur", "isCorrect": False},
                        {"text": "La photo de l'abattoir", "isCorrect": False},
                        {"text": "Le règlement intérieur du garage", "isCorrect": False}
                    ],
                    "correction": "Il doit être signé après vérification de la marchandise."
                },
                {
                    "questionNumber": 95,
                    "question": "Qu'est-ce que la 'fidélisation' ?",
                    "answerOptions": [
                        {"text": "L'ensemble des actions pour que le client revienne", "isCorrect": True},
                        {"text": "Obliger le client à acheter 10 kg de viande", "isCorrect": False},
                        {"text": "Offrir toute la marchandise gratuitement", "isCorrect": False},
                        {"text": "Fermer la boutique pour rester seul", "isCorrect": False}
                    ],
                    "correction": "Un client fidèle est plus rentable qu'un nouveau client."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel pictogramme de danger sur un produit de nettoyage indique qu'il brûle la peau ?",
                    "answerOptions": [
                        {"text": "Un flacon qui verse sur une main (corrosif)", "isCorrect": True},
                        {"text": "Une flamme", "isCorrect": False},
                        {"text": "Une tête de mort", "isCorrect": False},
                        {"text": "Un point d'exclamation", "isCorrect": False}
                    ],
                    "correction": "Il faut porter des gants et parfois des lunettes de protection."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelle est la durée légale du travail hebdomadaire pour un apprenti mineur ?",
                    "answerOptions": [
                        {"text": "35 heures", "isCorrect": True},
                        {"text": "45 heures", "isCorrect": False},
                        {"text": "20 heures", "isCorrect": False},
                        {"text": "Illimitée", "isCorrect": False}
                    ],
                    "correction": "Des dérogations sont possibles sous conditions, mais la base est de 35h."
                },
                {
                    "questionNumber": 98,
                    "question": "Qu'est-ce qu'une 'vente additionnelle' ?",
                    "answerOptions": [
                        {"text": "Proposer un produit complémentaire (ex: sauce avec le rôti)", "isCorrect": True},
                        {"text": "Vendre deux fois le même produit par erreur", "isCorrect": False},
                        {"text": "Additionner tous les prix sur la calculette", "isCorrect": False},
                        {"text": "Rendre la monnaie au client", "isCorrect": False}
                    ],
                    "correction": "Elle permet d'augmenter le panier moyen et de mieux conseiller le client."
                },
                {
                    "questionNumber": 99,
                    "question": "Que signifie le logo 'Agriculture Biologique' (AB) ?",
                    "answerOptions": [
                        {"text": "Respect de l'environnement et du bien-être animal", "isCorrect": True},
                        {"text": "Produit fabriqué uniquement en Bretagne", "isCorrect": False},
                        {"text": "Produit sans aucune calorie", "isCorrect": False},
                        {"text": "Viande garantie sans aucun os", "isCorrect": False}
                    ],
                    "correction": "L'élevage bio limite les traitements chimiques et privilégie l'espace pour les animaux."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est le but d'un 'bon de commande' ?",
                    "answerOptions": [
                        {"text": "Commander officiellement des produits au fournisseur", "isCorrect": True},
                        {"text": "Noter les vacances du boucher", "isCorrect": False},
                        {"text": "Calculer le poids du bœuf", "isCorrect": False},
                        {"text": "Faire plaisir au banquier", "isCorrect": False}
                    ],
                    "correction": "C'est la preuve de la commande en cas de litige sur la livraison."
                }
            ]
        }
    }
}