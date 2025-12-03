quiz_data = {
    "title": "Quiz CAP Boucher 2ème Année : Révisions Complètes (100 Questions)",
    "themes": {
        1: {
            "name": "Anatomie & Hygiène de Base (Q. 1-20)",
            "questions": [
                # =========================================================================
                # QUESTIONS 1 à 20 : ANATOMIE / HYGIÈNE / TECHNIQUES DE BASE
                # =========================================================================
                {
                    "questionNumber": 1,
                    "question": "Quel muscle principal donne le morceau de bœuf appelé 'Aiguillette baronne' (ou Aiguillette de rumsteck) ?",
                    "answerOptions": [
                        {"text": "Le Demi-tendineux", "isCorrect": False},
                        {"text": "Le Tenseur du fascia lata", "isCorrect": True}, 
                        {"text": "Le Long dorsal", "isCorrect": False},
                        {"text": "Le Psoas", "isCorrect": False}
                    ],
                    "correction": "La bonne réponse est : **Le Tenseur du fascia lata**. C'est une pièce de choix située à l'arrière du rumsteck."
                },
                {
                    "questionNumber": 2,
                    "question": "Selon la réglementation française d'hygiène (HACCP), quelle est la température maximale de conservation pour les viandes de boucherie fraîches (sauf abats et préparations) ?",
                    "answerOptions": [
                        {"text": "0°C", "isCorrect": False},
                        {"text": "7°C", "isCorrect": False},
                        {"text": "4°C", "isCorrect": True},
                        {"text": "10°C", "isCorrect": False}
                    ],
                    "correction": "La température maximale légale est **4°C** pour limiter la prolifération microbienne dans les viandes fraîches (bœuf, veau, agneau, porc)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est l'une des fonctions principales du 'parage' d'une pièce de viande en boucherie ?",
                    "answerOptions": [
                        {"text": "L'attendrir en coupant les fibres musculaires", "isCorrect": False},
                        {"text": "Améliorer la présentation et retirer les parties inutilisables (tendons, aponévèses, excédent de gras)", "isCorrect": True},
                        {"text": "Réaliser le désossage complet de la carcasse", "isCorrect": False},
                        {"text": "Augmenter la durée de conservation par salaison", "isCorrect": False}
                    ],
                    "correction": "Le **parage** consiste à enlever les parties non comestibles ou de qualité inférieure (nerfs, tendons, graisses dures) pour une meilleure commercialisation."
                },
                {
                    "questionNumber": 4,
                    "question": "Dans l'étiquetage des viandes préemballées de bœuf, quelle information est obligatoire pour assurer la traçabilité de l'animal ?",
                    "answerOptions": [
                        {"text": "Le nom du boucher et le prix au kilo.", "isCorrect": False},
                        {"text": "L'âge précis de l'animal au jour de l'abattage.", "isCorrect": False},
                        {"text": "Le numéro de lot, le pays d'élevage et le pays d'abattage.", "isCorrect": True},
                        {"text": "La photo de l'éleveur et la date de péremption.", "isCorrect": False}
                    ],
                    "correction": "La réglementation européenne impose le **numéro de lot, les pays d'élevage et d'abattage** pour la traçabilité de la viande bovine."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le nom du morceau de viande ovine (agneau ou mouton) qui correspond à la cuisse entière ?",
                    "answerOptions": [
                        {"text": "Le Carré", "isCorrect": False},
                        {"text": "L'Épaule", "isCorrect": False},
                        {"text": "Le Gigot", "isCorrect": True},
                        {"text": "La Selle", "isCorrect": False}
                    ],
                    "correction": "Le **Gigot** désigne le membre postérieur (la cuisse) de l'agneau ou du mouton."
                },
                {
                    "questionNumber": 6,
                    "question": "En boucherie porcine, quelle pièce de la cuisse est principalement utilisée pour la fabrication du jambon cuit, après désossage et parage ?",
                    "answerOptions": [
                        {"text": "L'Épaule", "isCorrect": False},
                        {"text": "Le Filet mignon", "isCorrect": False},
                        {"text": "La Lardière", "isCorrect": False},
                        {"text": "Le Jambon (la cuisse)", "isCorrect": True}
                    ],
                    "correction": "Le terme **Jambon** en charcuterie désigne le membre postérieur (la cuisse) du porc, pièce maîtresse pour le jambon cuit."
                },
                {
                    "questionNumber": 7,
                    "question": "Qu'est-ce qu'un 'Point Critique pour la Maîtrise' (CCP) dans le cadre de la méthode HACCP ?",
                    "answerOptions": [
                        {"text": "Un point où il est possible de corriger un problème après qu'il se soit produit.", "isCorrect": False},
                        {"text": "Une étape dans le processus où un danger peut être prévenu, éliminé ou ramené à un niveau acceptable, et où une surveillance est possible.", "isCorrect": True},
                        {"text": "Un simple point de contrôle visuel en fin de chaîne de production.", "isCorrect": False},
                        {"text": "Une étape qui n'a pas d'incidence sur la sécurité sanitaire des aliments.", "isCorrect": False}
                    ],
                    "correction": "Un **CCP** est une étape essentielle où un danger peut être contrôlé par une mesure corrective immédiate pour garantir la sécurité du produit."
                },
                {
                    "questionNumber": 8,
                    "question": "Lors du désossage d'un gigot d'agneau pour la rôtisserie, quel os doit être laissé dans la pièce pour maintenir sa forme et faciliter la cuisson ?",
                    "answerOptions": [
                        {"text": "Le Fémur", "isCorrect": False},
                        {"text": "Le Rotule", "isCorrect": False},
                        {"text": "L'os de la Hanche (ou Coxal)", "isCorrect": False},
                        {"text": "Le Manche (ou l'os du tibia conservé)", "isCorrect": True}
                    ],
                    "correction": "Pour un 'gigot à la coupe', seul le **Manche** (extrémité du tibia) est conservé. Il sert de 'poignée' et maintient la forme."
                },
                {
                    "questionNumber": 9,
                    "question": "En termes de rendement économique pour le boucher, que représente le Taux de Découpe (ou Taux de Rendement Net) ?",
                    "answerOptions": [
                        {"text": "Le pourcentage de marge commerciale réalisée sur la vente de l'ensemble des morceaux.", "isCorrect": False},
                        {"text": "Le poids total de la carcasse par rapport au poids de l'animal vivant.", "isCorrect": False},
                        {"text": "Le pourcentage de viande commercialisable (prête à vendre) par rapport au poids total de la carcasse ou du quartier.", "isCorrect": True},
                        {"text": "Le pourcentage des déchets (os, graisses, aponévroses) par rapport au poids des morceaux nobles.", "isCorrect": False}
                    ],
                    "correction": "Le **Taux de Découpe** est le pourcentage de viande vendable par rapport au poids initial (carcasse ou quartier). C'est l'indicateur clé de rentabilité."
                },
                {
                    "questionNumber": 10,
                    "question": "Parmi les ustensiles de coupe, quel est le type de couteau le plus approprié pour désosser une épaule de veau ou de porc en séparant la chair des articulations sans endommager le muscle ?",
                    "answerOptions": [
                        {"text": "Le Couteau de Chef (ou couteau d'office)", "isCorrect": False},
                        {"text": "Le Couteau à désosser (lame rigide et pointue)", "isCorrect": False},
                        {"text": "Le Fendoir (ou Hachette)", "isCorrect": False},
                        {"text": "Le Couteau à désosser (lame fine et flexible)", "isCorrect": True}
                    ],
                    "correction": "La **lame fine et flexible** est essentielle pour suivre les courbes des os et des articulations, minimisant la perte de chair et assurant un travail net."
                },
                {
                    "questionNumber": 11,
                    "question": "Que signifie la lettre 'A' dans le système de classification EUROP pour une carcasse bovine ?",
                    "answerOptions": [
                        {"text": "Jeune animal (moins de 12 mois)", "isCorrect": False},
                        {"text": "Vache (femelle ayant déjà vêlé)", "isCorrect": False},
                        {"text": "Taureau (mâle entier de moins de 2 ans)", "isCorrect": True},
                        {"text": "Bœuf (mâle castré)", "isCorrect": False}
                    ],
                    "correction": "Dans la classification **EUROP**, la catégorie 'A' désigne un **Taureau** de moins de deux ans (Mâle non castré)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le nom de l'abat rouge qui fait partie du 'cinquième quartier' et qui est l'estomac du ruminant ?",
                    "answerOptions": [
                        {"text": "Les Rognons", "isCorrect": False},
                        {"text": "La Hampe", "isCorrect": False},
                        {"text": "La Panse (ou Tripes)", "isCorrect": True},
                        {"text": "Le Foie", "isCorrect": False}
                    ],
                    "correction": "La **Panse** (ou Tripes) est le premier estomac du ruminant (bœuf, veau, agneau), un abat rouge très consommé."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est la coupe bovine qui correspond au muscle 'Longissimus dorsi' dans la partie avant ?",
                    "answerOptions": [
                        {"text": "Le Filet", "isCorrect": False},
                        {"text": "L'Aloyau", "isCorrect": False},
                        {"text": "La Tende de Tranche", "isCorrect": False},
                        {"text": "L'Entrecôte", "isCorrect": True}
                    ],
                    "correction": "Le **Longissimus dorsi** est le grand muscle du dos qui donne les côtes, les entrecôtes (partie avant) et le faux-filet (partie arrière)."
                },
                {
                    "questionNumber": 14,
                    "question": "Qu'est-ce que la 'DLC' et à quoi s'applique-t-elle généralement en boucherie ?",
                    "answerOptions": [
                        {"text": "Date Limite de Consommation, pour les produits périssables (viande fraîche)", "isCorrect": True},
                        {"text": "Date Limite de Conservation, pour les produits secs (charcuterie sèche)", "isCorrect": False},
                        {"text": "Date Longue de Commercialisation, pour les produits congelés", "isCorrect": False},
                        {"text": "Déclaration Légale de Certification, pour la traçabilité", "isCorrect": False}
                    ],
                    "correction": "La **DLC** (Date Limite de Consommation) est la date à ne pas dépasser pour les aliments très périssables comme la viande fraîche."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle technique est utilisée pour donner au rôti de bœuf une forme régulière avant la cuisson ?",
                    "answerOptions": [
                        {"text": "Le Parage uniquement", "isCorrect": False},
                        {"text": "Le Découpage", "isCorrect": False},
                        {"text": "Le Ficelage (ou bridage)", "isCorrect": True},
                        {"text": "Le Maturation", "isCorrect": False}
                    ],
                    "correction": "Le **Ficelage (ou bridage)** est l'opération qui consiste à attacher la pièce de viande pour maintenir sa forme, assurant une cuisson uniforme et une belle présentation."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la principale différence entre la 'bavette d'aloyau' et la 'bavette de flanchet' ?",
                    "answerOptions": [
                        {"text": "Le bœuf et le veau", "isCorrect": False},
                        {"text": "Le type de couteau utilisé", "isCorrect": False},
                        {"text": "Le muscle et la tendreté (l'aloyau est plus tendre)", "isCorrect": True},
                        {"text": "La couleur (l'une est blanche, l'autre rouge)", "isCorrect": False}
                    ],
                    "correction": "Elles proviennent de deux muscles différents : la **bavette d'aloyau** est plus proche de l'arrière et est considérée comme plus tendre que la bavette de flanchet (située sur le ventre)."
                },
                {
                    "questionNumber": 17,
                    "question": "En désossage porcin, quelle pièce correspond au 'filet mignon' ?",
                    "answerOptions": [
                        {"text": "La longe désossée", "isCorrect": False},
                        {"text": "Le muscle psoas du porc", "isCorrect": True},
                        {"text": "L'épaule avant", "isCorrect": False},
                        {"text": "Le jambon désossé", "isCorrect": False}
                    ],
                    "correction": "Le **Filet mignon** est le muscle psoas du porc (équivalent très petit du filet de bœuf), très tendre et situé sous la longe."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le rôle du 'bouchon' dans un billot en bois ?",
                    "answerOptions": [
                        {"text": "Un isolant électrique", "isCorrect": False},
                        {"text": "Un élément décoratif", "isCorrect": False},
                        {"text": "Une pièce de bois qui compense l'usure de la surface de travail", "isCorrect": True},
                        {"text": "Un produit de nettoyage", "isCorrect": False}
                    ],
                    "correction": "Le **bouchon** est une pièce de bois (généralement en orme) qui peut être remplacée lorsqu'elle est trop usée, prolongeant la durée de vie du billot."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le principal risque sanitaire lié à une rupture de la chaîne du froid dans le rayon de boucherie ?",
                    "answerOptions": [
                        {"text": "Le durcissement de la viande", "isCorrect": False},
                        {"text": "La prolifération rapide des micro-organismes pathogènes", "isCorrect": True},
                        {"text": "Une perte de couleur", "isCorrect": False},
                        {"text": "La congélation des produits", "isCorrect": False}
                    ],
                    "correction": "Le danger majeur est la **prolifération rapide des bactéries et micro-organismes** (comme Salmonella ou Listeria) qui se multiplient à température ambiante."
                },
                {
                    "questionNumber": 20,
                    "question": "Comment appelle-t-on le procédé qui consiste à laisser maturer la viande bovine à basse température pendant plusieurs jours (ou semaines) pour l'attendrir ?",
                    "answerOptions": [
                        {"text": "La salaison", "isCorrect": False},
                        {"text": "La Fibrage", "isCorrect": False},
                        {"text": "La Palettisation", "isCorrect": False},
                        {"text": "La Maturation (ou Rassissement)", "isCorrect": True}
                    ],
                    "correction": "La **Maturation (ou Rassissement)** est le processus de dégradation des protéines par les enzymes naturelles de la viande, ce qui l'attendrit et en développe les saveurs."
                },
            ]
        },
        2: {
            "name": "Désossage & Parage Avancés (Q. 21-40)",
            "questions": [
                # =========================================================================
                # QUESTIONS 21 à 40 : TECHNIQUES DE DÉSOSSAGE ET PARAGE AVANCÉS
                # =========================================================================
                {
                    "questionNumber": 21,
                    "question": "Lors du désossage d'une épaule de bœuf, quel os doit être retiré en premier pour faciliter l'accès à la palette et au jumeau ?",
                    "answerOptions": [
                        {"text": "Le Cubitus (ou Ulna)", "isCorrect": False},
                        {"text": "L'Humérus", "isCorrect": False},
                        {"text": "L'Omoplate (ou Scapula)", "isCorrect": True},
                        {"text": "Le Radius", "isCorrect": False}
                    ],
                    "correction": "L'**Omoplate (Scapula)** doit être libérée en premier. Une fois dégagée, elle permet d'ouvrir l'épaule pour séparer les différents muscles (palette, jumeau, etc.)."
                },
                {
                    "questionNumber": 22,
                    "question": "Qu'est-ce que le 'piston' ou 'noyau' dans le désossage d'une longe de veau ?",
                    "answerOptions": [
                        {"text": "L'os de la colonne vertébrale", "isCorrect": False},
                        {"text": "Un morceau de muscle inutile à retirer", "isCorrect": False},
                        {"text": "L'os du filet conservé pour la forme", "isCorrect": True},
                        {"text": "Le cartilage de l'articulation", "isCorrect": False}
                    ],
                    "correction": "Le **piston** (ou noyau) est la partie de l'os conservée (l'apophyse vertébrale) qui reste attachée au filet lors du désossage partiel d'une longe pour des rôtis."
                },
                {
                    "questionNumber": 23,
                    "question": "En boucherie chevaline, quel muscle est l'équivalent de la 'poire' ou du 'merlan' de bœuf ?",
                    "answerOptions": [
                        {"text": "La Semelle", "isCorrect": True},
                        {"text": "L'Arrière-façon", "isCorrect": False},
                        {"text": "La Joue", "isCorrect": False},
                        {"text": "Le Filet", "isCorrect": False}
                    ],
                    "correction": "La **Semelle** est la pièce du membre postérieur du cheval équivalente à la poire, au merlan, et au trefle de bœuf ; c'est un morceau à fibres courtes et tendres."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le principal objectif du 'ficelage' d'un rôti de bœuf (ex: Tende de tranche) ?",
                    "answerOptions": [
                        {"text": "Accélérer la cuisson", "isCorrect": False},
                        {"text": "Maintenir la forme pour une cuisson homogène et une meilleure présentation", "isCorrect": True},
                        {"text": "Réduire le poids de la pièce", "isCorrect": False},
                        {"text": "Ajouter du goût", "isCorrect": False}
                    ],
                    "correction": "Le **ficelage** sert à contraindre la pièce pour lui donner une forme cylindrique ou régulière, garantissant une **cuisson uniforme** et un aspect commercial esthétique."
                },
                {
                    "questionNumber": 25,
                    "question": "Lors du parage d'un filet de bœuf, on retire le 'cordon'. Que contient ce cordon ?",
                    "answerOptions": [
                        {"text": "Des fragments d'os", "isCorrect": False},
                        {"text": "Une fine pellicule de graisse et des aponévroses", "isCorrect": False},
                        {"text": "Une chaîne de ganglions et de la graisse", "isCorrect": True},
                        {"text": "Le tendon principal reliant le psoas à la colonne", "isCorrect": False}
                    ],
                    "correction": "Le **cordon** est la partie latérale du filet qui contient une ligne de **ganglions lymphatiques** (ou 'nœuds') et des tissus graisseux, qui doivent être retirés pour des raisons sanitaires et de qualité."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel morceau de bœuf correspond au 'plat-de-côtes' ?",
                    "answerOptions": [
                        {"text": "La partie des côtes du dos (Entrecôte)", "isCorrect": False},
                        {"text": "Le bord des côtes (muscles intercostaux et diaphragme)", "isCorrect": True},
                        {"text": "Le muscle de l'épaule", "isCorrect": False},
                        {"text": "La pointe du filet", "isCorrect": False}
                    ],
                    "correction": "Le **plat-de-côtes** est constitué des muscles et de la chair qui recouvrent les côtes et le sternum. C'est un morceau à bouillir ou à braiser."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est le nom du muscle qui donne la 'poire' dans le quartier arrière de bœuf ?",
                    "answerOptions": [
                        {"text": "Le Gluteus medius", "isCorrect": False},
                        {"text": "Le Piriformis", "isCorrect": True},
                        {"text": "Le Semimembranosus", "isCorrect": False},
                        {"text": "Le Psoas minor", "isCorrect": False}
                    ],
                    "correction": "La **Poire** correspond au muscle **Piriformis** (ou pyramidal) ; c'est une pièce très tendre et de forme ronde, située sur la hanche."
                },
                {
                    "questionNumber": 28,
                    "question": "Pour obtenir une 'côte de porc filet' (sans os et sans gras dorsal), quelle est l'opération à effectuer ?",
                    "answerOptions": [
                        {"text": "Le désossage de l'épaule", "isCorrect": False},
                        {"text": "Le parage et le désossage de la longe", "isCorrect": True},
                        {"text": "Le ficelage du jambon", "isCorrect": False},
                        {"text": "La fente de la poitrine", "isCorrect": False}
                    ],
                    "correction": "La **côte de porc filet** est obtenue après **désossage** de la partie dorsale de l'animal (la **longe**), séparant le muscle Longissimus dorsi de la colonne vertébrale."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est l'utilité du 'couteau-scie' (ou couteau à os) en boucherie professionnelle ?",
                    "answerOptions": [
                        {"text": "Trancher le gras", "isCorrect": False},
                        {"text": "Couper les os et les grosses articulations (Sternum, colonne vertébrale)", "isCorrect": True},
                        {"text": "Faire le parage fin des tendons", "isCorrect": False},
                        {"text": "Ficeler le rôti", "isCorrect": False}
                    ],
                    "correction": "Le **couteau-scie** est un outil robuste utilisé pour **sectionner les os durs** qui ne peuvent être coupés proprement au couteau classique ou à la fendeuse."
                },
                {
                    "questionNumber": 30,
                    "question": "Pour la fabrication de 'Saucisses' ou de 'Merguez', quelle opération sur la viande est indispensable pour un mélange homogène ?",
                    "answerOptions": [
                        {"text": "La maturation", "isCorrect": False},
                        {"text": "Le désossage à vif", "isCorrect": False},
                        {"text": "Le hachage (ou broyage)", "isCorrect": True},
                        {"text": "Le parage de la ficelle", "isCorrect": False}
                    ],
                    "correction": "Le **hachage (ou broyage)** de la viande et de la graisse est l'étape essentielle pour obtenir la texture désirée et permettre l'incorporation des assaisonnements dans les préparations de mêlée."
                },
                {
                    "questionNumber": 31,
                    "question": "Dans le quartier avant de bœuf, quel morceau est généralement utilisé pour les ragoûts et qui se trouve sur la face externe de l'épaule ?",
                    "answerOptions": [
                        {"text": "Le Filet", "isCorrect": False},
                        {"text": "Le Jarret arrière", "isCorrect": False},
                        {"text": "Le Jumeau (ou Macreuse)", "isCorrect": True},
                        {"text": "La Hampe", "isCorrect": False}
                    ],
                    "correction": "Le **Jumeau (ou Macreuse)** est un muscle de l'épaule, caractérisé par sa richesse en tissu conjonctif, le rendant parfait pour les cuissons longues (bourguignon, ragoût)."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est la coupe de veau que l'on obtient en désossant l'os du bassin de la cuisse (fémur) ?",
                    "answerOptions": [
                        {"text": "Le Quasi", "isCorrect": False},
                        {"text": "Le Longe", "isCorrect": False},
                        {"text": "La Noix (ou Sous-noix)", "isCorrect": True},
                        {"text": "La Selle", "isCorrect": False}
                    ],
                    "correction": "La **Noix (ou Sous-noix)** est l'un des trois principaux muscles de la cuisse de veau (avec la noix pâtissière) et est libérée après le désossage du fémur et de l'os de la hanche."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le nom du muscle de bœuf, long et plat, souvent vendu 'façon onglet' ?",
                    "answerOptions": [
                        {"text": "La Bavette de flanchet", "isCorrect": False},
                        {"text": "Le Plat de tranche", "isCorrect": False},
                        {"text": "La Hampe", "isCorrect": True},
                        {"text": "Le Flanchet", "isCorrect": False}
                    ],
                    "correction": "La **Hampe** est un muscle du diaphragme (un abat rouge), caractérisé par de longues fibres et est souvent préparée et vendue comme l'onglet, nécessitant un parage soigné."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel outil est spécifiquement conçu pour aiguiser et entretenir le fil du couteau de boucher, en complément de la pierre ?",
                    "answerOptions": [
                        {"text": "La Râpe", "isCorrect": False},
                        {"text": "Le Burin", "isCorrect": False},
                        {"text": "Le Fusil", "isCorrect": True},
                        {"text": "Le Maillet", "isCorrect": False}
                    ],
                    "correction": "Le **Fusil** sert à 'redresser' et à polir le fil du couteau au quotidien pour maintenir un tranchant parfait entre deux passages sur la pierre à aiguiser."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est la principale différence de texture entre le muscle 'Tende de Tranche' et le 'Rumsteck' ?",
                    "answerOptions": [
                        {"text": "Le Rumsteck est plus sec", "isCorrect": False},
                        {"text": "La Tende de Tranche a des fibres plus courtes", "isCorrect": False},
                        {"text": "Le Rumsteck est plus persillé et plus gras", "isCorrect": True},
                        {"text": "Il n'y a aucune différence", "isCorrect": False}
                    ],
                    "correction": "Le **Rumsteck** fait partie de l'aloyau, est plus **persillé (gras)** et plus court en fibres, tandis que la Tende de Tranche est un muscle plus maigre et long, faisant partie de la cuisse."
                },
                {
                    "questionNumber": 36,
                    "question": "Pour obtenir des 'côtes d'agneau premières' dans le carré, comment doit-on procéder à la 'manchonisation' ?",
                    "answerOptions": [
                        {"text": "Désosser complètement la côte", "isCorrect": False},
                        {"text": "Couper la côte à ras", "isCorrect": False},
                        {"text": "Dégager les os des vertèbres et gratter l'extrémité des côtes", "isCorrect": True}, 
                        {"text": "Ficeler l'ensemble du carré", "isCorrect": False}
                    ],
                    "correction": "La **manchonisation** consiste à dégager et à nettoyer l'os des côtes (le manchon) en grattant la chair et la graisse pour une présentation élégante et propre (côtes 'découvertes')."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel terme désigne la couche de graisse qui entoure le muscle, essentielle pour la maturation et la protection du bœuf ?",
                    "answerOptions": [
                        {"text": "Le Persillage (ou marbrure)", "isCorrect": False},
                        {"text": "Le Nerf", "isCorrect": False},
                        {"text": "La Bardière", "isCorrect": False},
                        {"text": "Le Cap (ou Graisse de couverture)", "isCorrect": True}
                    ],
                    "correction": "Le **Cap** (ou graisse de couverture) est la couche externe de graisse qui protège le muscle pendant la maturation et la conservation. Le persillage est la graisse interne."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle technique permet de séparer un muscle le long de ses membranes conjonctives (aponévroses) sans le couper 'à vif' ?",
                    "answerOptions": [
                        {"text": "Le Découpage à la scie", "isCorrect": False},
                        {"text": "Le Dédoublement (ou Séparation par les membranes)", "isCorrect": True},
                        {"text": "Le Ficelage", "isCorrect": False},
                        {"text": "Le Hachage", "isCorrect": False}
                    ],
                    "correction": "Le **dédoublement** (ou 'séparation par le jeu') est l'art de suivre la ligne naturelle de séparation entre les muscles le long des membranes, maximisant la qualité des pièces et le rendement."
                },
                {
                    "questionNumber": 39,
                    "question": "Comment appelle-t-on le morceau de bœuf situé à l'intérieur de la cuisse, qui contient les muscles 'Noix' et 'Sous-noix' ?",
                    "answerOptions": [
                        {"text": "Le Tendron", "isCorrect": False},
                        {"text": "La Bavette", "isCorrect": False},
                        {"text": "Le Rond de gîte", "isCorrect": False},
                        {"text": "La Cuisse (ou Tranche)", "isCorrect": True}
                    ],
                    "correction": "La **Cuisse** (ou l'ensemble de la **Tranche**) est l'unité principale. Elle est subdivisée en Noix, Sous-noix (ou Contre-noix), et Noix Pâtissière (ou Pâté)."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle partie de l'agneau est utilisée pour obtenir le 'carré d'agneau' ?",
                    "answerOptions": [
                        {"text": "Le membre postérieur (cuisse)", "isCorrect": False},
                        {"text": "La partie du dos comprenant les côtes découvertes", "isCorrect": True},
                        {"text": "L'épaule avant", "isCorrect": False},
                        {"text": "Le cou", "isCorrect": False}
                    ],
                    "correction": "Le **carré d'agneau** est le morceau dorsal qui s'étend du collier à la selle, et qui contient les côtes (carré de côtes) souvent préparées 'découvertes' ou 'premières'."
                },
            ]
        },
        3: {
            "name": "Hygiène, Sécurité & Législation (Q. 41-60)",
            "questions": [
                # =========================================================================
                # QUESTIONS 41 à 60 : HYGIÈNE, SÉCURITÉ ALIMENTAIRE ET LÉGISLATION
                # =========================================================================
                {
                    "questionNumber": 41,
                    "question": "Quel est l'objectif principal du Plan de Maîtrise Sanitaire (PMS) en boucherie ?",
                    "answerOptions": [
                        {"text": "Augmenter la marge bénéficiaire de l'entreprise", "isCorrect": False},
                        {"text": "Décrire les mesures prises pour assurer l'hygiène et la sécurité des denrées alimentaires", "isCorrect": True},
                        {"text": "Gérer les relations avec les fournisseurs et les clients", "isCorrect": False},
                        {"text": "Planifier les stocks et les commandes de carcasses", "isCorrect": False}
                    ],
                    "correction": "Le **PMS** est un document obligatoire décrivant toutes les **procédures d'hygiène** (HACCP, Bonnes Pratiques d'Hygiène, gestion des non-conformités) pour garantir la sécurité sanitaire."
                },
                {
                    "questionNumber": 42,
                    "question": "Que signifie l'abréviation 'HACCP' ?",
                    "answerOptions": [
                        {"text": "Hygiène Alimentaire Contrôlée par le Consommateur et le Professionnel", "isCorrect": False},
                        {"text": "Hazard Analysis Critical Control Point", "isCorrect": True},
                        {"text": "Hygiène Assurance Certification Contrôle des Produits", "isCorrect": False},
                        {"text": "Haute Autorité de Contrôle des Carcasses et des Pièces", "isCorrect": False}
                    ],
                    "correction": "**HACCP** signifie **Hazard Analysis Critical Control Point** (Analyse des dangers et points critiques pour leur maîtrise). C'est le cœur du PMS."
                },
                {
                    "questionNumber": 43,
                    "question": "En cas de contrôle d'hygiène, quelle est la sanction immédiate si l'on détecte la présence de rongeurs ou d'insectes dans le laboratoire ?",
                    "answerOptions": [
                        {"text": "Une simple amende", "isCorrect": False},
                        {"text": "Une obligation d'afficher un panneau d'avertissement", "isCorrect": False},
                        {"text": "La fermeture administrative immédiate de l'établissement", "isCorrect": True},
                        {"text": "Un rappel à l'ordre écrit", "isCorrect": False}
                    ],
                    "correction": "La présence de nuisibles (rongeurs, insectes) constitue un danger grave et immédiat de contamination, pouvant entraîner une **fermeture administrative immédiate**."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle doit être la température minimale de l'eau utilisée pour le nettoyage et la désinfection des outils et surfaces de travail ?",
                    "answerOptions": [
                        {"text": "20°C", "isCorrect": False},
                        {"text": "40°C", "isCorrect": False},
                        {"text": "60°C", "isCorrect": True},
                        {"text": "100°C", "isCorrect": False}
                    ],
                    "correction": "L'eau doit être à **60°C minimum** pour le nettoyage (dégraissage efficace) et la désinfection, afin de garantir l'élimination des germes et des graisses."
                },
                {
                    "questionNumber": 45,
                    "question": "Lorsqu'une pièce de viande ne respecte plus la DLC (Date Limite de Consommation), comment doit-elle être gérée selon le PMS ?",
                    "answerOptions": [
                        {"text": "Être vendue à prix réduit", "isCorrect": False},
                        {"text": "Être congelée immédiatement", "isCorrect": False},
                        {"text": "Être retirée de la vente, tracée et éliminée (déclassée)", "isCorrect": True},
                        {"text": "Être retravaillée en préparation", "isCorrect": False}
                    ],
                    "correction": "Tout produit ayant dépassé sa **DLC** est considéré comme un danger microbiologique. Il doit être **retiré de la vente** et tracé comme déchet, jamais recongelé ou retravaillé."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le risque principal si un boucher utilise un couteau sale pour couper une pièce de viande ?",
                    "answerOptions": [
                        {"text": "La perte de tranchant du couteau", "isCorrect": False},
                        {"text": "La 'contamination croisée' de la viande", "isCorrect": True},
                        {"text": "L'augmentation du pH de la viande", "isCorrect": False},
                        {"text": "Le jaunissement de la graisse", "isCorrect": False}
                    ],
                    "correction": "L'usage d'outils souillés provoque la **contamination croisée** : les germes présents sur le couteau sont transférés à l'aliment sain, rendant la viande impropre à la consommation."
                },
                {
                    "questionNumber": 47,
                    "question": "Dans le système EUROP, à quoi se réfère la notation de conformation (lettres E, U, R, O, P) ?",
                    "answerOptions": [
                        {"text": "La couleur de la viande", "isCorrect": False},
                        {"text": "Le développement des profils (muscles) de la carcasse", "isCorrect": True},
                        {"text": "Le degré d'engraissement", "isCorrect": False},
                        {"text": "L'âge de l'animal à l'abattage", "isCorrect": False}
                    ],
                    "correction": "La **conformation** est jugée par le **développement des muscles** de la carcasse. E (Exceptionnel) indique un profil très développé et P (Médiocre) un profil faible."
                },
                {
                    "questionNumber": 48,
                    "question": "Dans le système EUROP, à quoi se réfère la notation d'état d'engraissement (chiffres 1 à 5) ?",
                    "answerOptions": [
                        {"text": "La quantité de graisse de couverture et dans la cavité thoracique", "isCorrect": True},
                        {"text": "La couleur de la graisse", "isCorrect": False},
                        {"text": "Le taux d'humidité de la carcasse", "isCorrect": False},
                        {"text": "La présence d'os dans le quartier", "isCorrect": False}
                    ],
                    "correction": "L'**engraissement** est noté de **1 (très faible)** à **5 (très fort)** et évalue la quantité de graisse sur et dans la carcasse. Il impacte le rendement."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle est la température maximale autorisée pour le hachage de la viande fraîche ?",
                    "answerOptions": [
                        {"text": "0°C", "isCorrect": False},
                        {"text": "7°C", "isCorrect": True},
                        {"text": "4°C", "isCorrect": False},
                        {"text": "10°C", "isCorrect": False}
                    ],
                    "correction": "La température de la **viande hachée** ne doit jamais dépasser **7°C** (et 2°C pour les préparations de viande hachée), en raison du risque accru de contamination microbienne en surface."
                },
                {
                    "questionNumber": 50,
                    "question": "Qu'est-ce qu'un 'Programme Prérequis Opérationnel' (PRPo) dans la méthode HACCP ?",
                    "answerOptions": [
                        {"text": "Un point non critique", "isCorrect": False},
                        {"text": "Une étape cruciale pour la sécurité où une correction immédiate est possible", "isCorrect": False},
                        {"text": "Un programme général pour contrôler la probabilité d'un danger avant l'étape critique", "isCorrect": True},
                        {"text": "Le nettoyage de la salle de vente", "isCorrect": False}
                    ],
                    "correction": "Les **PRPo** sont des mesures de maîtrise appliquées pour prévenir les dangers significatifs. Ils sont mesurables et surveillés, mais moins critiques qu'un CCP."
                },
                {
                    "questionNumber": 51,
                    "question": "Selon la réglementation, quel doit être l'état de l'étal de vente pour les produits crus ?",
                    "answerOptions": [
                        {"text": "En bois et sec", "isCorrect": False},
                        {"text": "En matériau poreux et chaud", "isCorrect": False},
                        {"text": "En matériau lisse, étanche, facile à nettoyer et désinfecter", "isCorrect": True},
                        {"text": "En cuivre non traité", "isCorrect": False}
                    ],
                    "correction": "Les matériaux en contact avec les denrées alimentaires (plan de travail, étal) doivent être **lisses, étanches, non toxiques et faciles à nettoyer et désinfecter** pour éviter la rétention de germes."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le risque lié à l'utilisation d'une planche de coupe en bois mal entretenue ?",
                    "answerOptions": [
                        {"text": "Elle absorbe trop de lumière", "isCorrect": False},
                        {"text": "Les fibres s'altèrent, créant des fissures et des refuges pour les bactéries", "isCorrect": True},
                        {"text": "Elle devient trop glissante", "isCorrect": False},
                        {"text": "Elle modifie le goût de la viande", "isCorrect": False}
                    ],
                    "correction": "Une planche de bois usée présente des **rainures** qui piègent l'humidité et les résidus, constituant un excellent foyer pour la **prolifération bactérienne**."
                },
                {
                    "questionNumber": 53,
                    "question": "Que doit impérativement porter le boucher ou l'apprenti lors des opérations de désossage et de parage pour la sécurité ?",
                    "answerOptions": [
                        {"text": "Un chapeau de cuisine uniquement", "isCorrect": False},
                        {"text": "Un tablier jetable", "isCorrect": False},
                        {"text": "Un tablier de mailles ou un tablier de protection anti-coupure", "isCorrect": True},
                        {"text": "Un masque chirurgical", "isCorrect": False}
                    ],
                    "correction": "Le port d'un **tablier en mailles métalliques (cotte de mailles)** ou autre protection anti-coupure est obligatoire pour prévenir les accidents graves lors de l'utilisation des couteaux et scies."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le délai maximum de conservation d'une carcasse de bœuf fraîche (non congelée) en chambre froide après abattage, avant commercialisation (hors maturation) ?",
                    "answerOptions": [
                        {"text": "24 heures", "isCorrect": False},
                        {"text": "7 jours", "isCorrect": False},
                        {"text": "Plusieurs semaines (selon le type de maturation)", "isCorrect": True},
                        {"text": "1 mois", "isCorrect": False}
                    ],
                    "correction": "La conservation peut aller jusqu'à **plusieurs semaines** (généralement 10 à 21 jours) en fonction du processus de **maturation (rassissement)** mis en place, à condition de maintenir la température de la carcasse en dessous de 4°C."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est l'élément obligatoire sur l'étiquette d'un produit préemballé qui indique clairement au consommateur l'usage prévu du produit ?",
                    "answerOptions": [
                        {"text": "La composition nutritionnelle", "isCorrect": False},
                        {"text": "Le nom du muscle", "isCorrect": False},
                        {"text": "La 'Dénomination de Vente' et le 'Mode d'emploi' (ex : à cuire, à griller)", "isCorrect": True},
                        {"text": "Le numéro de téléphone du boucher", "isCorrect": False}
                    ],
                    "correction": "La **Dénomination de Vente** (ex: 'Rôti de bœuf') et l'indication du **Mode d'emploi** ('à cuire', 'à consommer cuit à cœur') sont essentiels pour l'information du consommateur et la sécurité."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle est la principale mesure corrective à prendre lorsqu'une température de chambre froide dépasse le seuil critique (ex: 4°C) ?",
                    "answerOptions": [
                        {"text": "Ouvrir la porte pour aérer", "isCorrect": False},
                        {"text": "Contrôler et réparer le système de refroidissement, puis vérifier et enregistrer la température des viandes", "isCorrect": True},
                        {"text": "Augmenter la ventilation", "isCorrect": False},
                        {"text": "Ajouter de la glace", "isCorrect": False}
                    ],
                    "correction": "Il faut d'abord **intervenir sur la cause (réparation)**, puis évaluer la **non-conformité des produits** (prise de température à cœur des viandes) pour déterminer s'ils peuvent être conservés ou doivent être déclassés."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel risque microbiologique est le plus souvent associé à la consommation de viande hachée mal cuite ?",
                    "answerOptions": [
                        {"text": "Clostridium botulinum", "isCorrect": False},
                        {"text": "Listeria monocytogenes", "isCorrect": False},
                        {"text": "E. coli O157:H7 (ou Salmonelle)", "isCorrect": True},
                        {"text": "Pénicillium roqueforti", "isCorrect": False}
                    ],
                    "correction": "Les bactéries comme **E. coli O157:H7** sont souvent présentes à la surface des carcasses. Lors du hachage, elles sont mélangées à l'intérieur. Si la viande n'est pas cuite à cœur, elles survivent."
                },
                {
                    "questionNumber": 58,
                    "question": "Comment doit-on stocker les produits d'entretien (nettoyants, désinfectants) par rapport aux denrées alimentaires ?",
                    "answerOptions": [
                        {"text": "Au même endroit pour faciliter l'accès", "isCorrect": False},
                        {"text": "Dans la salle de vente", "isCorrect": False},
                        {"text": "Dans un local séparé, verrouillé et clairement identifié", "isCorrect": True},
                        {"text": "Sous le billot", "isCorrect": False}
                    ],
                    "correction": "Les produits chimiques doivent être **stockés séparément** pour éviter tout risque de **contamination chimique** des aliments par projection, fuite ou confusion."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est l'identifiant européen obligatoire qui atteste qu'un abattoir est agréé et régulièrement contrôlé ?",
                    "answerOptions": [
                        {"text": "Le code-barres EAN", "isCorrect": False},
                        {"text": "La marque d'identification de l'établissement (marque ovale)", "isCorrect": True},
                        {"text": "Le numéro de TVA intracommunautaire", "isCorrect": False},
                        {"text": "Le code postal", "isCorrect": False}
                    ],
                    "correction": "La **marque d'identification (marque ovale)** contient le pays (FR), le numéro d'agrément et les initiales de l'Union Européenne (CE). C'est la preuve de l'agrément sanitaire."
                },
                {
                    "questionNumber": 60,
                    "question": "Lors du transport des carcasses du quai de livraison à la chambre froide, quelle précaution doit-on prendre concernant la température ?",
                    "answerOptions": [
                        {"text": "Le transport doit durer moins de 30 minutes", "isCorrect": False},
                        {"text": "La carcasse ne doit pas entrer en contact avec l'air extérieur", "isCorrect": False},
                        {"text": "Le transfert doit être le plus rapide possible pour minimiser la rupture de la chaîne du froid", "isCorrect": True},
                        {"text": "Utiliser un chariot chauffant", "isCorrect": False}
                    ],
                    "correction": "Le transport de l'extérieur à la chambre froide (le 'déchargement') est un point critique : il doit être **rapide et efficace** pour garantir le maintien des températures réglementaires."
                },
            ]
        },
        4: {
            "name": "Technologie, Rendement & Calculs (Q. 61-80)",
            "questions": [
                # =========================================================================
                # QUESTIONS 61 à 80 : TECHNOLOGIE PROFESSIONNELLE, RENDEMENT ET CALCULS
                # =========================================================================
                {
                    "questionNumber": 61,
                    "question": "Quel est le calcul de base utilisé par le boucher pour déterminer le 'Prix de Revient Matière' (PRM) d'un morceau ?",
                    "answerOptions": [
                        {"text": "PRM = Coût d'achat total - Marge commerciale", "isCorrect": False},
                        {"text": "PRM = Coût d'achat de la carcasse / Taux de Découpe Net (en %)", "isCorrect": True},
                        {"text": "PRM = Coût de la main d'œuvre + Prix de vente", "isCorrect": False},
                        {"text": "PRM = Taux de Découpe x Coût de l'emballage", "isCorrect": False}
                    ],
                    "correction": "Le **Prix de Revient Matière** (PRM) est calculé en divisant le coût total d'achat par le **Taux de Découpe Net** (pourcentage de viande vendable), car les morceaux doivent compenser la perte des os et déchets."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le principal inconvénient d'une maturation 'trop longue' de la viande (au-delà de la période optimale) ?",
                    "answerOptions": [
                        {"text": "La viande devient trop ferme", "isCorrect": False},
                        {"text": "Le risque de 'froid extrême' interne", "isCorrect": False},
                        {"text": "Le dessèchement (perte de poids) et le risque de développement de moisissures indésirables", "isCorrect": True},
                        {"text": "Le muscle ne change pas de couleur", "isCorrect": False}
                    ],
                    "correction": "Une maturation trop longue entraîne un **dessèchement (perte de rendement)** et un risque de développement de moisissures ou de bactéries de dégradation en surface."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est le rôle de la 'Gélatine' dans la préparation de certains produits de charcuterie (ex: Pâtés, Jambons en gelée) ?",
                    "answerOptions": [
                        {"text": "Servir d'agent de coloration", "isCorrect": False},
                        {"text": "Augmenter la teneur en fibres musculaires", "isCorrect": False},
                        {"text": "Lier les ingrédients, donner de la tenue et empêcher l'oxydation (protection)", "isCorrect": True},
                        {"text": "Accélérer la cuisson des pièces", "isCorrect": False}
                    ],
                    "correction": "La **gélatine** est utilisée pour **lier les morceaux**, pour **protéger** le produit de l'air (oxydation) et pour lui donner une **tenue** et un aspect visuel agréable."
                },
                {
                    "questionNumber": 64,
                    "question": "Qu'est-ce que l'opération de 'ciselage' dans la préparation d'une pièce de viande avant cuisson ?",
                    "answerOptions": [
                        {"text": "Couper la pièce en très fines tranches", "isCorrect": False},
                        {"text": "Marquer la surface de la viande avec des incisions pour éviter la déformation à la cuisson", "isCorrect": True},
                        {"text": "Ficeler la pièce avec une technique spécifique", "isCorrect": False},
                        {"text": "Retirer les tendons avec des ciseaux", "isCorrect": False}
                    ],
                    "correction": "Le **ciselage** consiste à pratiquer de fines **incisions** (lignes) sur les membranes et le gras de couverture pour que la pièce ne se rétracte pas de manière irrégulière sous l'effet de la chaleur."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est l'unité de mesure principale pour évaluer l'acidité d'une viande (facteur de conservation) ?",
                    "answerOptions": [
                        {"text": "La Température (°C)", "isCorrect": False},
                        {"text": "Le Poids (kg)", "isCorrect": False},
                        {"text": "Le pH", "isCorrect": True},
                        {"text": "L'Humidité (%)", "isCorrect": False}
                    ],
                    "correction": "Le **pH** mesure l'acidité (potentiel Hydrogène) de la viande. Un pH bas (acide) est favorable à la conservation. Un pH élevé est un signe de mauvaise qualité et de mauvaise tenue (viande DFD)."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel équipement est absolument nécessaire pour préparer de la viande pour une cuisson sous-vide ?",
                    "answerOptions": [
                        {"text": "Une machine à hacher", "isCorrect": False},
                        {"text": "Un laminoir", "isCorrect": False},
                        {"text": "Une machine de mise sous-vide professionnelle (cloche)", "isCorrect": True},
                        {"text": "Une scie à ruban", "isCorrect": False}
                    ],
                    "correction": "La mise **sous-vide** prolonge la durée de conservation en créant un environnement anaérobie (sans oxygène). Cela nécessite une **machine sous-vide** à cloche pour un conditionnement professionnel."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le risque de vendre de la viande décongelée sans en informer le client ?",
                    "answerOptions": [
                        {"text": "Un risque économique seulement", "isCorrect": False},
                        {"text": "Une rupture de la chaîne du froid", "isCorrect": False},
                        {"text": "Un délit de tromperie et une rupture de la traçabilité", "isCorrect": True},
                        {"text": "Un mauvais goût", "isCorrect": False}
                    ],
                    "correction": "Vendre un produit décongelé pour du frais, sans mention légale, est un **délit de tromperie** et enfreint la réglementation d'étiquetage. Il est illégal de recongeler un produit décongelé."
                },
                {
                    "questionNumber": 68,
                    "question": "Qu'est-ce que le 'trimming' d'une carcasse de porc ?",
                    "answerOptions": [
                        {"text": "La découpe du jambon", "isCorrect": False},
                        {"text": "L'injection de saumure dans l'épaule", "isCorrect": False},
                        {"text": "La valorisation des parures (graisse et muscles) pour le hachage ou la charcuterie", "isCorrect": True},
                        {"text": "La congélation des morceaux nobles", "isCorrect": False}
                    ],
                    "correction": "Le **trimming** est l'opération de **parage avancé et de valorisation** des excédents de gras et des petites parures de muscles pour en faire des matières premières pour la charcuterie ou l'industrie."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est l'intérêt d'utiliser des additifs (ex: nitrites) dans la charcuterie (jambon cuit, saucisson) ?",
                    "answerOptions": [
                        {"text": "Rendre la viande plus tendre", "isCorrect": False},
                        {"text": "Contrôler le pH après cuisson", "isCorrect": False},
                        {"text": "Assurer la conservation, fixer la couleur rouge/rosée et prévenir le botulisme", "isCorrect": True},
                        {"text": "Augmenter le rendement de découpe", "isCorrect": False}
                    ],
                    "correction": "Les **nitrites** (ou salpêtre) sont des agents de conservation qui **fixent la couleur** et, surtout, **empêchent le développement de Clostridium botulinum** (risque mortel)."
                },
                {
                    "questionNumber": 70,
                    "question": "Si une carcasse de bœuf de 300 kg a un Taux de Découpe Net de 70%, quel est le poids total de viande commercialisable (en kg) ?",
                    "answerOptions": [
                        {"text": "200 kg", "isCorrect": False},
                        {"text": "210 kg", "isCorrect": True},
                        {"text": "230 kg", "isCorrect": False},
                        {"text": "300 kg", "isCorrect": False}
                    ],
                    "correction": "Calcul : $300 \text{ kg} \times 0,70 = 210 \text{ kg}$. C'est le prix que doit 'porter' la viande vendable pour couvrir l'achat de l'os et de la graisse perdus."
                },
                {
                    "questionNumber": 71,
                    "question": "Qu'est-ce que le 'fiel' et pourquoi doit-il être manipulé avec une extrême précaution ?",
                    "answerOptions": [
                        {"text": "Un muscle fragile qui peut se déchirer", "isCorrect": False},
                        {"text": "Une masse de graisse du cinquième quartier", "isCorrect": False},
                        {"text": "La vésicule biliaire, dont le liquide (bile) rend la viande impropre à la consommation", "isCorrect": True},
                        {"text": "Un tendon très dur qui doit être retiré", "isCorrect": False}
                    ],
                    "correction": "Le **fiel** est la **vésicule biliaire**. Si elle est percée, le liquide biliaire souille la viande, la rendant très amère et non commercialisable."
                },
                {
                    "questionNumber": 72,
                    "question": "Dans la technologie des produits tripiers, qu'est-ce que l'opération de 'blanchiment' ?",
                    "answerOptions": [
                        {"text": "Le passage des abats au congélateur", "isCorrect": False},
                        {"text": "Le trempage des boyaux dans l'eau salée", "isCorrect": False},
                        {"text": "La cuisson rapide dans l'eau chaude pour nettoyer et raffermir (ex : tête de veau, tripes)", "isCorrect": True},
                        {"text": "L'ajout d'amidon pour épaissir la sauce", "isCorrect": False}
                    ],
                    "correction": "Le **blanchiment** est une pré-cuisson (ébullition courte) pour **nettoyer** les abats (retirer les impuretés) et les **raffermir** avant la préparation finale ou le détaillage."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est l'incidence du stress de l'animal avant l'abattage sur la qualité de la viande bovine ?",
                    "answerOptions": [
                        {"text": "Augmentation du persillage", "isCorrect": False},
                        {"text": "Rend la viande plus claire (PSE)", "isCorrect": False},
                        {"text": "Provoque des viandes sombres et sèches (DFD) avec un pH élevé", "isCorrect": True},
                        {"text": "N'a aucune incidence", "isCorrect": False}
                    ],
                    "correction": "Le stress épuise les réserves de glycogène, ce qui entraîne des viandes **DFD (Dark, Firm, Dry)**. Ces viandes ont un pH élevé, sont moins savoureuses et se conservent mal."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le nom de l'appareil utilisé pour vérifier le pH des carcasses après l'abattage ?",
                    "answerOptions": [
                        {"text": "Un thermomètre", "isCorrect": False},
                        {"text": "Un réfractomètre", "isCorrect": False},
                        {"text": "Un pH-mètre (ou sonde à pH)", "isCorrect": True},
                        {"text": "Un dynamomètre", "isCorrect": False}
                    ],
                    "correction": "Le **pH-mètre** (ou sonde à pH) est utilisé pour mesurer l'acidité de la viande, un indicateur clé pour évaluer la qualité de la maturation et la tenue du muscle."
                },
                {
                    "questionNumber": 75,
                    "question": "Si vous achetez un quartier arrière de veau à $8,50 /kg$ et que le rendement net est de $65\%$, quel est le coût de revient matière (PRM) en $/kg$ ?",
                    "answerOptions": [
                        {"text": "$5,52 /kg$", "isCorrect": False},
                        {"text": "$13,08 /kg$", "isCorrect": True},
                        {"text": "$10,00 /kg$", "isCorrect": False},
                        {"text": "$8,50 /kg$", "isCorrect": False}
                    ],
                    "correction": "Calcul : $8,50 / 0,65 \approx 13,08 /kg$. C'est le prix que doit 'porter' la viande vendable pour couvrir l'achat de l'os et de la graisse perdus."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment appelle-t-on l'opération qui consiste à insérer de fines lamelles de lard gras dans un morceau de viande maigre (ex: Rôti de bœuf) pour l'attendrir et l'hydrater à la cuisson ?",
                    "answerOptions": [
                        {"text": "Le Parage", "isCorrect": False},
                        {"text": "Le Dédoublement", "isCorrect": False},
                        {"text": "Le Piquage (ou Larder)", "isCorrect": True},
                        {"text": "Le Bardage", "isCorrect": False}
                    ],
                    "correction": "Le **piquage** (ou larder) est l'insertion du lard à l'intérieur du muscle à l'aide d'une lardoire, pour apporter du gras et de l'humidité au cœur d'une viande maigre pendant la cuisson."
                },
                {
                    "questionNumber": 77,
                    "question": "Dans le système de classification des carcasses, qu'est-ce qui est mesuré pour déterminer la 'classe de gras' ?",
                    "answerOptions": [
                        {"text": "La couleur du muscle", "isCorrect": False},
                        {"text": "L'épaisseur de la graisse de couverture (sous-cutanée)", "isCorrect": True},
                        {"text": "Le pH de la viande", "isCorrect": False},
                        {"text": "La longueur des côtes", "isCorrect": False}
                    ],
                    "correction": "La classe de gras (échelle de 1 à 5 dans EUROP) est mesurée par l'**épaisseur de la couche de graisse** située à un point précis sur la carcasse."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est l'impact d'un nettoyage incomplet (résidus organiques) sur l'efficacité de la désinfection ?",
                    "answerOptions": [
                        {"text": "Il n'y a aucun impact", "isCorrect": False},
                        {"text": "Les résidus vont neutraliser l'effet du désinfectant, rendant l'opération inefficace", "isCorrect": True},
                        {"text": "Il augmente l'effet du désinfectant", "isCorrect": False},
                        {"text": "Il augmente le temps de séchage", "isCorrect": False}
                    ],
                    "correction": "Les matières organiques forment une 'barrière' protectrice pour les germes. Le nettoyage est la **phase la plus importante** : si elle est incomplète, la désinfection sera inefficace."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le nom de la machine utilisée pour attendrir mécaniquement des morceaux de viande (ex: Steaks, escalopes) par passage de lames ou de pointes ?",
                    "answerOptions": [
                        {"text": "Le Cutter", "isCorrect": False},
                        {"text": "Le Hachoir", "isCorrect": False},
                        {"text": "L'Attendrisseur (ou Manteuse)", "isCorrect": True},
                        {"text": "La Scie à os", "isCorrect": False}
                    ],
                    "correction": "L'**attendrisseur** (ou manteuse) utilise des lames ou aiguilles fines pour couper superficiellement les fibres musculaires et le tissu conjonctif, rendant la pièce plus tendre."
                },
                {
                    "questionNumber": 80,
                    "question": "Quelle est la coupe spécifique de l'agneau qui se situe entre le gigot et le carré, et qui est souvent vendue désossée et roulée ?",
                    "answerOptions": [
                        {"text": "Le Collier", "isCorrect": False},
                        {"text": "La Poitrine", "isCorrect": False},
                        {"text": "La Selle (ou double longe)", "isCorrect": True},
                        {"text": "L'épaule", "isCorrect": False}
                    ],
                    "correction": "La **Selle** est la partie centrale et noble du dos de l'agneau, comprenant les deux filets. Elle est souvent préparée entière, désossée pour être farcie et roulée, ou détaillée en côtes."
                },
            ]
        },
        5: {
            "name": "Abats, Charcuterie & Races (Q. 81-100)",
            "questions": [
                # =========================================================================
                # QUESTIONS 81 à 100 : ABATS, CHARCUTERIE ET CONNAISSANCE DES RACES
                # =========================================================================
                {
                    "questionNumber": 81,
                    "question": "Quel abat est classé comme 'abat blanc' ?",
                    "answerOptions": [
                        {"text": "Foie", "isCorrect": False},
                        {"text": "Cœur", "isCorrect": False},
                        {"text": "Ris de veau", "isCorrect": True},
                        {"text": "Hampe", "isCorrect": False}
                    ],
                    "correction": "Le **Ris de veau** (thymus) est un abat blanc car il est glandulaire. Les autres sont des abats rouges."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle opération doit précéder la cuisson du ris de veau pour retirer ses impuretés et le raffermir ?",
                    "answerOptions": [
                        {"text": "Ficelage", "isCorrect": False},
                        {"text": "Piquage", "isCorrect": False},
                        {"text": "Dégorgeage", "isCorrect": True},
                        {"text": "Salaison", "isCorrect": False}
                    ],
                    "correction": "Le **Dégorgeage** (trempage à l'eau froide) est essentiel pour enlever les impuretés et le sang, suivi d'un blanchiment pour le raffermir et le préparer à la cuisson."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la principale caractéristique de la race bovine 'Limousine' sur le marché de la boucherie ?",
                    "answerOptions": [
                        {"text": "Fort persillage et viande très grasse", "isCorrect": False},
                        {"text": "Excellent rendement en viande maigre et finesse du grain", "isCorrect": True},
                        {"text": "Viande foncée (DFD) et pH élevé", "isCorrect": False},
                        {"text": "Production exclusive de lait", "isCorrect": False}
                    ],
                    "correction": "La **Limousine** est réputée pour son excellent rendement et la qualité de sa **viande maigre** avec des fibres fines et un faible taux de gras de couverture."
                },
                {
                    "questionNumber": 84,
                    "question": "Outre l'eau et le sel, quel est l'ingrédient essentiel et indispensable d'une saumure pour la fabrication de jambon cuit, pour la couleur et la sécurité ?",
                    "answerOptions": [
                        {"text": "Poivre concassé", "isCorrect": False},
                        {"text": "Nitrites de sodium (salpêtre)", "isCorrect": True},
                        {"text": "Farine de blé", "isCorrect": False},
                        {"text": "Sucre glace", "isCorrect": False}
                    ],
                    "correction": "L'ajout de **nitrites de sodium** est essentiel pour garantir la couleur rosée et surtout pour la **sécurité sanitaire** (prévention du botulisme) dans les produits cuits et salés."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le nom de la machine utilisée en charcuterie pour remplir les boyaux avec la mêlée (chair à saucisse) ?",
                    "answerOptions": [
                        {"text": "Le Cutter", "isCorrect": False},
                        {"text": "Le Mélangeur", "isCorrect": False},
                        {"text": "Le Hachoir", "isCorrect": False},
                        {"text": "Le Poussoir", "isCorrect": True}
                    ],
                    "correction": "Le **Poussoir** est la machine qui utilise une pression pour insérer la mêlée dans l'enveloppe (boyau) pour la fabrication des saucisses et boudins."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est la principale caractéristique de l'agneau de lait par rapport à l'agneau de boucherie classique ?",
                    "answerOptions": [
                        {"text": "Viande très rouge et fortement musclée", "isCorrect": False},
                        {"text": "Poids supérieur à 30 kg", "isCorrect": False},
                        {"text": "Viande très claire et faible engraissement", "isCorrect": True},
                        {"text": "Taux de découpe très élevé", "isCorrect": False}
                    ],
                    "correction": "L'agneau de lait, abattu très jeune (45 jours max.), n'est nourri qu'au lait. Sa chair est très **claire (blanche)** et sa graisse presque inexistante, ce qui le rend très prisé."
                },
                {
                    "questionNumber": 87,
                    "question": "Parmi ces abats, lequel est un organe glandulaire ?",
                    "answerOptions": [
                        {"text": "La Joue", "isCorrect": False},
                        {"text": "Le Cœur", "isCorrect": False},
                        {"text": "Le Foie", "isCorrect": True},
                        {"text": "Les Tripes", "isCorrect": False}
                    ],
                    "correction": "Le **Foie** est une glande annexe de la digestion. Le cœur et la joue sont des muscles ; les tripes sont un estomac (viscère)."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le procédé de cuisson principal pour obtenir des rillettes ?",
                    "answerOptions": [
                        {"text": "Cuisson au four à haute température", "isCorrect": False},
                        {"text": "Cuisson lente et longue dans la graisse (confisage)", "isCorrect": True},
                        {"text": "Cuisson rapide à la vapeur", "isCorrect": False},
                        {"text": "Cuisson par salage et séchage", "isCorrect": False}
                    ],
                    "correction": "Les **rillettes** nécessitent une cuisson très **lente et longue** dans la graisse, ce qui permet à la chair de se désagréger et de s'effilocher facilement."
                },
                {
                    "questionNumber": 89,
                    "question": "Le 'ris de veau' est-il prélevé sur un veau jeune ou adulte, et pourquoi ?",
                    "answerOptions": [
                        {"text": "Veau Adulte, car il est plus gros.", "isCorrect": False},
                        {"text": "Veau jeune (thymus), car cette glande disparaît chez l'adulte.", "isCorrect": True},
                        {"text": "Bœuf castré, pour sa tendreté.", "isCorrect": False},
                        {"text": "Vache de réforme, pour son goût prononcé.", "isCorrect": False}
                    ],
                    "correction": "Le ris est le **thymus** de l'animal. Cette glande régresse et disparaît à l'âge adulte. On ne trouve le ris de bonne qualité que chez le **veau jeune**."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle race porcine est réputée pour sa viande persillée, souvent utilisée pour les produits secs de qualité supérieure ?",
                    "answerOptions": [
                        {"text": "Large White", "isCorrect": False},
                        {"text": "Piétrain", "isCorrect": False},
                        {"text": "Duroc", "isCorrect": False},
                        {"text": "Porc Noir (ou races rustiques)", "isCorrect": True}
                    ],
                    "correction": "Les **races rustiques** et les porcs noirs sont valorisés pour leur **gras intramusculaire (persillage)**, essentiel pour la saveur des jambons crus séchés."
                },
                {
                    "questionNumber": 91,
                    "question": "Quels morceaux de bœuf proviennent du diaphragme et sont considérés comme des abats rouges pour leur tendreté ?",
                    "answerOptions": [
                        {"text": "Le Filet et le Faux-Filet", "isCorrect": False},
                        {"text": "L'Onglet et la Hampe", "isCorrect": True},
                        {"text": "La Tende de Tranche et le Gîte", "isCorrect": False},
                        {"text": "Le Flanchet et la Bavette d'aloyau", "isCorrect": False}
                    ],
                    "correction": "L'**Onglet et la Hampe** sont les muscles du diaphragme (d'où leur classification historique en abat rouge), prisés pour leur tendreté et leurs fibres longues."
                },
                {
                    "questionNumber": 92,
                    "question": "En boucherie, qu'est-ce qu'une aponévrose ?",
                    "answerOptions": [
                        {"text": "Une artère principale", "isCorrect": False},
                        {"text": "Une membrane fibreuse qui entoure et sépare les muscles", "isCorrect": True},
                        {"text": "Un petit os de l'articulation", "isCorrect": False},
                        {"text": "Un type de graisse intramusculaire", "isCorrect": False}
                    ],
                    "correction": "L'**aponévrose** est un tissu conjonctif dense et blanc qui doit être soigneusement retiré lors du parage car il est dur et peu agréable à la mastication après cuisson."
                },
                {
                    "questionNumber": 93,
                    "question": "Pour la préparation des cervelles d'agneau ou de veau, quelle opération est indispensable avant la cuisson ?",
                    "answerOptions": [
                        {"text": "Le parage au couteau", "isCorrect": False},
                        {"text": "Le dégorgeage et l'enlèvement des membranes", "isCorrect": True},
                        {"text": "Le hachage fin", "isCorrect": False},
                        {"text": "L'ajout de nitrites", "isCorrect": False}
                    ],
                    "correction": "Les cervelles doivent être impérativement **dégorgées** dans de l'eau froide pour enlever le sang coagulé et les membranes avant d'être blanchies ou pochées."
                },
                {
                    "questionNumber": 94,
                    "question": "Pourquoi la viande d'un bœuf (mâle castré) est-elle généralement plus rouge que celle d'un veau ?",
                    "answerOptions": [
                        {"text": "Moins de maturation", "isCorrect": False},
                        {"text": "Plus de graisse", "isCorrect": False},
                        {"text": "Concentration plus faible en myoglobine", "isCorrect": False},
                        {"text": "Concentration plus élevée en myoglobine", "isCorrect": True}
                    ],
                    "correction": "La **myoglobine**, protéine qui fixe l'oxygène dans les muscles, est produite en plus grande quantité par un animal adulte, ce qui **fonce la couleur** de la viande."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est l'intérêt principal d'utiliser des boyaux naturels (intestin de porc ou de mouton) pour la fabrication de saucisses ?",
                    "answerOptions": [
                        {"text": "Coût très faible", "isCorrect": False},
                        {"text": "Rapidité d'embossage", "isCorrect": False},
                        {"text": "Améliore le goût et permet la perméabilité à la fumée", "isCorrect": True},
                        {"text": "Tient mieux la cuisson", "isCorrect": False}
                    ],
                    "correction": "Les boyaux naturels sont plus coûteux mais sont **perméables à l'air et à la fumée**, contribuant de manière significative au développement du goût et au séchage."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle race bovine, principalement laitière, est aussi utilisée en boucherie comme 'vache de réforme' ?",
                    "answerOptions": [
                        {"text": "Salers", "isCorrect": False},
                        {"text": "Charolaise", "isCorrect": False},
                        {"text": "Prim'Holstein", "isCorrect": True},
                        {"text": "Limousine", "isCorrect": False}
                    ],
                    "correction": "La **Prim'Holstein** est la race laitière dominante. En fin de carrière laitière, la carcasse est vendue en **vache de réforme** (catégorie E) pour la boucherie ou l'industrie."
                },
                {
                    "questionNumber": 97,
                    "question": "À part la cervelle, quelle partie de la tête de veau ou de porc est principalement utilisée en charcuterie (ex: Fromage de tête) ?",
                    "answerOptions": [
                        {"text": "Les yeux", "isCorrect": False},
                        {"text": "Le cartilage nasal", "isCorrect": False},
                        {"text": "Les joues et la langue", "isCorrect": True},
                        {"text": "L'os du crâne", "isCorrect": False}
                    ],
                    "correction": "Les **joues** (muscles) et la **langue** sont les parties charnues et gélatineuses essentielles pour le Fromage de tête (ou Tête pressée)."
                },
                {
                    "questionNumber": 98,
                    "question": "Contrairement au bœuf, la maturation (rassissement) n'est pas nécessaire pour le porc. Pourquoi ?",
                    "answerOptions": [
                        {"text": "Le porc ne contient pas de myoglobine", "isCorrect": False},
                        {"text": "Le porc est plus tendre naturellement et ses fibres musculaires sont plus fines", "isCorrect": True},
                        {"text": "Le porc est toujours congelé avant vente", "isCorrect": False},
                        {"text": "Le porc est élevé uniquement pour la charcuterie", "isCorrect": False}
                    ],
                    "correction": "Le porc est naturellement **tendre** et ses fibres musculaires sont fines. Le temps d'attente après abattage est court et n'a pas l'effet bénéfique (attendrissement) nécessaire pour le bœuf."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel outil de laboratoire est utilisé en charcuterie pour vérifier la concentration de sel dans la saumure ?",
                    "answerOptions": [
                        {"text": "Le pH-mètre", "isCorrect": False},
                        {"text": "Le Thermomètre", "isCorrect": False},
                        {"text": "Le Densimètre (ou Pèse-sel)", "isCorrect": True},
                        {"text": "Le Chronomètre", "isCorrect": False}
                    ],
                    "correction": "Le **Densimètre** (ou pèse-sel) est utilisé pour mesurer la densité du liquide. Cela permet de calculer la concentration en sel (le 'degré Baumé'), essentiel pour la conservation."
                },
                {
                    "questionNumber": 100,
                    "question": "Lorsque la viande ovine est vendue sous l'appellation 'Mouton' (animal adulte), quelle est sa principale caractéristique organoleptique (goût) ?",
                    "answerOptions": [
                        {"text": "Un goût très doux et peu prononcé", "isCorrect": False},
                        {"text": "Une chair très persillée et grasse", "isCorrect": False},
                        {"text": "Un goût fort et prononcé (goût de suif)", "isCorrect": True},
                        {"text": "Une viande très claire (blanche)", "isCorrect": False}
                    ],
                    "correction": "La viande de **mouton** (animal non castré plus âgé) développe un **goût fort et prononcé** (goût de suif) à cause de la graisse et des acides gras, la rendant moins prisée que celle de l'agneau."
                }
            ]
        }
    }
}