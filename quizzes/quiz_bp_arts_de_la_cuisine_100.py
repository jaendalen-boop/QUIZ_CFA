quiz_data = {
    "title": "Quiz BP Arts de la Cuisine (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE CULINAIRE AVANCÉE & CONNAISSANCE DES PRODUITS (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE CULINAIRE AVANCÉE & CONNAISSANCE DES PRODUITS",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle substance est naturellement présente dans le jaune d'œuf et permet de stabiliser une émulsion comme la mayonnaise ?",
                    "answerOptions": [
                        {"text": "Lécithine", "isCorrect": True},
                        {"text": "Caséine", "isCorrect": False},
                        {"text": "Ovalbumine", "isCorrect": False},
                        {"text": "Globuline", "isCorrect": False}
                    ],
                    "correction": "La lécithine est un lipide tensioactif présent dans le jaune d'œuf. Elle agit comme un émulsifiant en faisant le lien entre les molécules d'eau (le vinaigre) et les molécules de graisse (l'huile), stabilisant ainsi l'émulsion."
                },
                {
                    "questionNumber": 2,
                    "question": "Dans la classification officielle des produits de la pêche, à quelle catégorie appartient le Turbot ?",
                    "answerOptions": [
                        {"text": "Poisson plat", "isCorrect": True},
                        {"text": "Poisson rond", "isCorrect": False},
                        {"text": "Poisson cartilagineux", "isCorrect": False},
                        {"text": "Cephalopode", "isCorrect": False}
                    ],
                    "correction": "Le Turbot est un poisson plat benthique (qui vit sur le fond). Il se distingue par sa forme asymétrique, ses deux yeux étant situés sur le même côté de la tête."
                },
                {
                    "questionNumber": 3,
                    "question": "Que garantit le label européen AOP (Appellation d'Origine Protégée) pour un produit alimentaire ?",
                    "answerOptions": [
                        {"text": "Toutes les étapes de production ont lieu dans l'aire géographique", "isCorrect": True},
                        {"text": "Seulement une étape de production a lieu dans la zone définie", "isCorrect": False},
                        {"text": "Le produit respecte uniquement un mode de production traditionnel", "isCorrect": False},
                        {"text": "Le produit provient exclusivement de l'agriculture biologique certifiée", "isCorrect": False}
                    ],
                    "correction": "L'AOP désigne un produit dont toutes les étapes de fabrication (production, transformation et élaboration) sont réalisées dans une même zone géographique selon un savoir-faire reconnu."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la température réglementaire de stockage à cœur pour les produits de la pêche frais réfrigérés ?",
                    "answerOptions": [
                        {"text": "Glace fondante", "isCorrect": True},
                        {"text": "5 degrés Celsius", "isCorrect": False},
                        {"text": "8 degrés Celsius", "isCorrect": False},
                        {"text": "Température ambiante", "isCorrect": False}
                    ],
                    "correction": "Les produits de la pêche frais doivent être maintenus à la température de la glace fondante, c'est-à-dire entre 0°C et +2°C, pour ralentir l'activité enzymatique et microbienne."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel gélifiant d'origine végétale, extrait d'algues rouges, permet de réaliser des gelées chaudes car il ne fond qu'à 85°C ?",
                    "answerOptions": [
                        {"text": "Agar-agar", "isCorrect": True},
                        {"text": "Gélatine", "isCorrect": False},
                        {"text": "Pectine", "isCorrect": False},
                        {"text": "Carraghénane", "isCorrect": False}
                    ],
                    "correction": "L'agar-agar a la propriété thermoréversible particulière de gélifier autour de 35-40°C mais de ne fondre qu'à partir de 85°C, ce qui permet de servir des préparations gélifiées chaudes."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle partie du bœuf est située dans la région lombaire et est couramment utilisée pour les pièces à rôtir comme le rumsteck ?",
                    "answerOptions": [
                        {"text": "Aloyau", "isCorrect": True},
                        {"text": "Collier", "isCorrect": False},
                        {"text": "Poitrine", "isCorrect": False},
                        {"text": "Jumeau", "isCorrect": False}
                    ],
                    "correction": "L'aloyau est un ensemble de morceaux nobles situés dans la région lombaire et la cuisse du bœuf (comprenant le filet, le faux-filet et le rumsteck), destinés principalement aux cuissons rapides (rôtir, griller)."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle variété de truffe est connue sous le nom scientifique Tuber melanosporum et récoltée principalement en hiver ?",
                    "answerOptions": [
                        {"text": "Truffe noire", "isCorrect": True},
                        {"text": "Truffe blanche", "isCorrect": False},
                        {"text": "Truffe d'été", "isCorrect": False},
                        {"text": "Truffe de Bourgogne", "isCorrect": False}
                    ],
                    "correction": "La Tuber melanosporum, ou truffe noire du Périgord, est la plus prisée en cuisine gastronomique pour son parfum intense. Elle se récolte généralement de novembre à mars."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel terme désigne la transformation du collagène des tissus conjonctifs en gélatine sous l'action d'une cuisson longue et humide ?",
                    "answerOptions": [
                        {"text": "Hydrolyse", "isCorrect": True},
                        {"text": "Coagulation", "isCorrect": False},
                        {"text": "Dextrinisation", "isCorrect": False},
                        {"text": "Caramélisation", "isCorrect": False}
                    ],
                    "correction": "L'hydrolyse du collagène est le processus chimique par lequel les fibres dures de collagène se dégradent en gélatine tendre en présence d'eau et de chaleur, rendant la viande moelleuse."
                },
                {
                    "questionNumber": 9,
                    "question": "Parmi ces volailles, laquelle bénéficie d'une AOC (Appellation d'Origine Contrôlée) garantissant une zone d'élevage stricte et une alimentation spécifique ?",
                    "answerOptions": [
                        {"text": "Bresse", "isCorrect": True},
                        {"text": "Landes", "isCorrect": False},
                        {"text": "Loué", "isCorrect": False},
                        {"text": "Challans", "isCorrect": False}
                    ],
                    "correction": "La Volaille de Bresse est la seule volaille au monde à bénéficier d'une AOC. Elle répond à un cahier des charges très strict concernant sa race (Gauloise blanche), son alimentation et sa zone d'élevage."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel additif texturant, souvent utilisé en cuisine moléculaire, nécessite la présence de calcium pour gélifier ?",
                    "answerOptions": [
                        {"text": "Alginate", "isCorrect": True},
                        {"text": "Xenthane", "isCorrect": False},
                        {"text": "Guar", "isCorrect": False},
                        {"text": "Tara", "isCorrect": False}
                    ],
                    "correction": "L'alginate de sodium (extrait d'algues brunes) a la propriété de gélifier instantanément au contact d'une solution riche en calcium (comme le chlorure de calcium), permettant la technique de sphérification."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la particularité anatomique des poissons dits 'gras' comme le maquereau ou le saumon par rapport aux poissons maigres ?",
                    "answerOptions": [
                        {"text": "Lipides répartis", "isCorrect": True},
                        {"text": "Foie énorme", "isCorrect": False},
                        {"text": "Vessie absente", "isCorrect": False},
                        {"text": "Peau épaisse", "isCorrect": False}
                    ],
                    "correction": "Chez les poissons gras, les réserves lipidiques (graisses) sont réparties dans l'ensemble des tissus musculaires (la chair), alors que chez les poissons maigres, elles sont concentrées principalement dans le foie."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle découpe de légumes correspond à des petits dés de 1 à 2 mm de côté ?",
                    "answerOptions": [
                        {"text": "Brunoise", "isCorrect": True},
                        {"text": "Mirepoix", "isCorrect": False},
                        {"text": "Macédoine", "isCorrect": False},
                        {"text": "Jardinière", "isCorrect": False}
                    ],
                    "correction": "La brunoise est une taille de précision consistant à couper les légumes en très petits dés de 1 à 2 mm, utilisée pour les garnitures fines, les farces ou les décorations."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel composé est responsable de la couleur rouge vive de la viande fraîche lorsqu'elle est oxygénée ?",
                    "answerOptions": [
                        {"text": "Oxymyoglobine", "isCorrect": True},
                        {"text": "Hémoglobine", "isCorrect": False},
                        {"text": "Metmyoglobine", "isCorrect": False},
                        {"text": "Myoglobine", "isCorrect": False}
                    ],
                    "correction": "La myoglobine (pigment musculaire) capte l'oxygène pour devenir de l'oxymyoglobine, qui donne cette couleur rouge cerise brillante caractéristique de la viande fraîchement coupée et exposée à l'air."
                },
                {
                    "questionNumber": 14,
                    "question": "Dans la catégorie des gibiers à plumes, quel oiseau est classé comme gibier d'eau ?",
                    "answerOptions": [
                        {"text": "Canard colvert", "isCorrect": True},
                        {"text": "Faisan vénéré", "isCorrect": False},
                        {"text": "Perdreau gris", "isCorrect": False},
                        {"text": "Pigeon ramier", "isCorrect": False}
                    ],
                    "correction": "Le canard colvert est un gibier d'eau sauvage. Les autres oiseaux cités (faisan, perdreau, pigeon) sont considérés comme du gibier de plaine ou de bois."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est le rôle principal de l'amidon dans une liaison à base de fécule ?",
                    "answerOptions": [
                        {"text": "Épaississement", "isCorrect": True},
                        {"text": "Émulsion", "isCorrect": False},
                        {"text": "Coloration", "isCorrect": False},
                        {"text": "Acidification", "isCorrect": False}
                    ],
                    "correction": "L'amidon, lorsqu'il est chauffé dans un liquide (empesage), gonfle et absorbe l'eau, ce qui augmente la viscosité de la préparation et assure son épaississement (liaison)."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel label européen protège le nom d'un produit dont la qualité est liée à une origine géographique, mais dont une seule étape de production suffit dans la zone ?",
                    "answerOptions": [
                        {"text": "IGP", "isCorrect": True},
                        {"text": "AB", "isCorrect": False},
                        {"text": "STG", "isCorrect": False},
                        {"text": "Label Rouge", "isCorrect": False}
                    ],
                    "correction": "L'IGP (Indication Géographique Protégée) garantit qu'au moins une étape parmi la production, la transformation ou l'élaboration a lieu dans l'aire géographique délimitée. C'est moins restrictif que l'AOP."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle enzyme, présente dans l'ananas frais, empêche la gélification de la gélatine animale en détruisant les protéines ?",
                    "answerOptions": [
                        {"text": "Broméline", "isCorrect": True},
                        {"text": "Pepsine", "isCorrect": False},
                        {"text": "Amylase", "isCorrect": False},
                        {"text": "Lipase", "isCorrect": False}
                    ],
                    "correction": "La broméline est une enzyme protéolytique qui 'digère' les protéines. Comme la gélatine est une protéine, l'ananas frais (non cuit) détruit son pouvoir gélifiant. Il faut pocher l'ananas pour détruire l'enzyme."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle pièce de veau, située dans l'épaule, est particulièrement adaptée aux cuissons longues comme la blanquette car elle est riche en collagène ?",
                    "answerOptions": [
                        {"text": "Paleron", "isCorrect": True},
                        {"text": "Noix", "isCorrect": False},
                        {"text": "Filet", "isCorrect": False},
                        {"text": "Longe", "isCorrect": False}
                    ],
                    "correction": "Le paleron est un morceau gélatineux de l'épaule (catégorie 2 ou 3). Sa richesse en tissu conjonctif le rend idéal pour les ragoûts et braisages, donnant du moelleux après une cuisson lente."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel sucre technique a un pouvoir anti-cristallisant très fort et est utilisé pour garder le moelleux des pâtes de fruits ?",
                    "answerOptions": [
                        {"text": "Glucose", "isCorrect": True},
                        {"text": "Saccharose", "isCorrect": False},
                        {"text": "Lactose", "isCorrect": False},
                        {"text": "Fructose", "isCorrect": False}
                    ],
                    "correction": "Le sirop de glucose est utilisé en confiserie et pâtisserie pour empêcher la recristallisation du sucre (saccharose) et retenir l'humidité, assurant souplesse et conservation aux produits."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle catégorie d'œufs est réservée aux œufs 'extra frais' vendus jusqu'au 9ème jour après la ponte ?",
                    "answerOptions": [
                        {"text": "Catégorie A", "isCorrect": True},
                        {"text": "Catégorie B", "isCorrect": False},
                        {"text": "Catégorie C", "isCorrect": False},
                        {"text": "Catégorie J", "isCorrect": False}
                    ],
                    "correction": "La Catégorie A désigne les œufs frais destinés aux consommateurs. La mention 'Extra' ou 'Extra frais' peut être utilisée jusqu'au 9ème jour après la date de ponte."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNIQUES DE PRODUCTION & MAÎTRISE DES CUISSONS (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNIQUES DE PRODUCTION & MAÎTRISE DES CUISSONS",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel phénomène chimique complexe, se produisant à partir de 145°C, est responsable du brunissement et du développement des arômes des viandes grillées ?",
                    "answerOptions": [
                        {"text": "Maillard", "isCorrect": True},
                        {"text": "Hydrolyse", "isCorrect": False},
                        {"text": "Oxydation", "isCorrect": False},
                        {"text": "Fermentation", "isCorrect": False}
                    ],
                    "correction": "La réaction de Maillard est une réaction chimique entre les acides aminés (protéines) et les sucres réducteurs sous l'effet de la chaleur, créant la croûte brune et les saveurs de rôti."
                },
                {
                    "questionNumber": 22,
                    "question": "Pour réaliser un velouté de volaille classique, quel est l'élément de base liquide (mouillement) à incorporer au roux blanc ?",
                    "answerOptions": [
                        {"text": "Fond blanc", "isCorrect": True},
                        {"text": "Fond brun", "isCorrect": False},
                        {"text": "Fumet de poisson", "isCorrect": False},
                        {"text": "Lait entier", "isCorrect": False}
                    ],
                    "correction": "Un velouté est une sauce mère réalisée à partir d'un roux (blanc ou blond) mouillé avec un fond blanc (volaille ou veau). Si l'on mouille au lait, on obtient une béchamel."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le but principal de l'opération consistant à 'dessécher' une détrempe de pâte à choux sur le feu ?",
                    "answerOptions": [
                        {"text": "Évaporer l'eau excédentaire", "isCorrect": True},
                        {"text": "Cuire les œufs totalement", "isCorrect": False},
                        {"text": "Faire fondre le beurre lentement", "isCorrect": False},
                        {"text": "Incorporer de l'air dans la pâte", "isCorrect": False}
                    ],
                    "correction": "Le dessèchement (ou dessiccation) sur le feu permet d'évaporer une partie de l'eau contenue dans la panade pour qu'elle puisse ensuite absorber les œufs, ce qui permettra le gonflement au four."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle est la température critique de coagulation des œufs dans une crème anglaise, au-delà de laquelle elle 'tourne' (flocule) ?",
                    "answerOptions": [
                        {"text": "85 degrés", "isCorrect": True},
                        {"text": "65 degrés", "isCorrect": False},
                        {"text": "100 degrés", "isCorrect": False},
                        {"text": "120 degrés", "isCorrect": False}
                    ],
                    "correction": "La crème anglaise doit être cuite 'à la nappe' entre 82°C et 84°C. À 85°C et au-delà, les protéines de l'œuf coagulent massivement, donnant une texture granuleuse (omelette brouillée)."
                },
                {
                    "questionNumber": 25,
                    "question": "Dans la classification des sauces émulsionnées, à quelle catégorie appartient la sauce Hollandaise ?",
                    "answerOptions": [
                        {"text": "Chaude semi-coagulée", "isCorrect": True},
                        {"text": "Froide stable", "isCorrect": False},
                        {"text": "Froide instable", "isCorrect": False},
                        {"text": "Chaude instable", "isCorrect": False}
                    ],
                    "correction": "La Hollandaise (comme la Béarnaise) est une émulsion chaude semi-coagulée (ou stable). Les jaunes d'œufs sont cuits doucement (sabayon) pour stabiliser l'incorporation du beurre clarifié."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle technique de cuisson consiste à cuire un aliment dans un liquide maintenu juste en dessous du point d'ébullition (frémissement) ?",
                    "answerOptions": [
                        {"text": "Pocher", "isCorrect": True},
                        {"text": "Sauter", "isCorrect": False},
                        {"text": "Braiser", "isCorrect": False},
                        {"text": "Frire", "isCorrect": False}
                    ],
                    "correction": "Pocher signifie cuire un aliment immergé dans un liquide (eau, bouillon, sirop) à une température proche de l'ébullition mais sans gros bouillons, pour préserver la texture des aliments fragiles."
                },
                {
                    "questionNumber": 27,
                    "question": "De quels éléments est composée une garniture aromatique classique dite 'Mirepoix' ?",
                    "answerOptions": [
                        {"text": "Carottes oignons céleri", "isCorrect": True},
                        {"text": "Poireaux navets choux", "isCorrect": False},
                        {"text": "Ail échalote persil", "isCorrect": False},
                        {"text": "Tomates poivrons courgettes", "isCorrect": False}
                    ],
                    "correction": "La mirepoix est une taille (dés grossiers) et une composition aromatique : carottes, oignons et souvent céleri branche, taillés en dés, utilisés comme base aromatique pour les fonds, sauces et braisages."
                },
                {
                    "questionNumber": 28,
                    "question": "Quelle est la proportion standard de beurre pour 1 kg de farine dans la réalisation d'un feuilletage classique ?",
                    "answerOptions": [
                        {"text": "500 grammes", "isCorrect": True},
                        {"text": "100 grammes", "isCorrect": False},
                        {"text": "200 grammes", "isCorrect": False},
                        {"text": "250 grammes", "isCorrect": False}
                    ],
                    "correction": "Le feuilletage classique repose sur un équilibre : le poids de matière grasse (beurre de tourage) représente généralement 50% du poids de la détrempe, soit environ 500g de beurre pour 1kg de farine (plus l'eau)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel ingrédient est indispensable pour clarifier un consommé, car il forme un 'gâteau' de filtration en coagulant ?",
                    "answerOptions": [
                        {"text": "Blanc d'œuf", "isCorrect": True},
                        {"text": "Jaune d'œuf", "isCorrect": False},
                        {"text": "Fécule de maïs", "isCorrect": False},
                        {"text": "Crème liquide", "isCorrect": False}
                    ],
                    "correction": "Les blancs d'œufs, riches en albumine, coagulent sous l'effet de la chaleur et emprisonnent les impuretés en remontant à la surface, clarifiant ainsi le bouillon."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel mode de cuisson par expansion favorise l'échange des saveurs entre l'aliment et le liquide de cuisson dès le départ à froid ?",
                    "answerOptions": [
                        {"text": "Départ liquide froid", "isCorrect": True},
                        {"text": "Départ liquide bouillant", "isCorrect": False},
                        {"text": "Cuisson sous vide basse température", "isCorrect": False},
                        {"text": "Cuisson à la vapeur sous pression", "isCorrect": False}
                    ],
                    "correction": "Démarrer une cuisson à froid (comme pour un bouillon ou un pot-au-feu) favorise la diffusion des sucs et arômes de la viande vers le liquide (phénomène d'osmose/expansion)."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment se nomme l'appareil à base de purée de pommes de terre et de pâte à choux utilisé pour les pommes Dauphine ?",
                    "answerOptions": [
                        {"text": "Appareil à dauphine", "isCorrect": True},
                        {"text": "Appareil à duchesse", "isCorrect": False},
                        {"text": "Appareil à croquette", "isCorrect": False},
                        {"text": "Appareil à gnocchi", "isCorrect": False}
                    ],
                    "correction": "Les pommes Dauphine sont réalisées en mélangeant environ 2/3 de purée de pommes de terre sèche et 1/3 de pâte à choux salée, puis frites."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est l'utilité technique de 'singer' une préparation lors de la réalisation d'un ragoût à brun ?",
                    "answerOptions": [
                        {"text": "Apporter la liaison", "isCorrect": True},
                        {"text": "Donner de la brillance", "isCorrect": False},
                        {"text": "Augmenter le volume", "isCorrect": False},
                        {"text": "Corriger l'acidité", "isCorrect": False}
                    ],
                    "correction": "Singer consiste à saupoudrer de farine les morceaux de viande revenus dans la matière grasse avant de mouiller. La farine cuit (roux brun instantané) et assurera la liaison de la sauce."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle préparation sert de base à la réalisation d'un soufflé salé ou sucré classique ?",
                    "answerOptions": [
                        {"text": "Béchamel ou pâtissière", "isCorrect": True},
                        {"text": "Chantilly ou meringue", "isCorrect": False},
                        {"text": "Sablé ou génoise", "isCorrect": False},
                        {"text": "Ganache ou praliné", "isCorrect": False}
                    ],
                    "correction": "Un soufflé est constitué d'une base liée (béchamel pour le salé, pâtissière pour le sucré) aromatisée, à laquelle on incorpore délicatement des blancs d'œufs montés en neige."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la particularité physico-chimique du beurre clarifié par rapport au beurre frais ?",
                    "answerOptions": [
                        {"text": "Point de fumée élevé", "isCorrect": True},
                        {"text": "Goût de noisette prononcé", "isCorrect": False},
                        {"text": "Texture plus crémeuse à froid", "isCorrect": False},
                        {"text": "Teneur en eau plus importante", "isCorrect": False}
                    ],
                    "correction": "En clarifiant le beurre, on retire l'eau, le lactose et la caséine. Il ne reste que la matière grasse pure, ce qui augmente considérablement son point de fumée (180°C contre 130°C pour le beurre frais)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel terme désigne l'action de faire briller des légumes cuits en les enrobant de leur liquide de cuisson réduit et de beurre ?",
                    "answerOptions": [
                        {"text": "Glacer", "isCorrect": True},
                        {"text": "Napper", "isCorrect": False},
                        {"text": "Lustrer", "isCorrect": False},
                        {"text": "Vanner", "isCorrect": False}
                    ],
                    "correction": "Glacer des légumes (à blanc ou à brun) consiste à les cuire avec un peu d'eau, de beurre et de sucre, puis à réduire le jus en fin de cuisson pour qu'il enrobent les légumes d'une pellicule brillante."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est la fonction principale d'une marinade crue pour une pièce de gibier ?",
                    "answerOptions": [
                        {"text": "Aromatiser et attendrir", "isCorrect": True},
                        {"text": "Cuire et colorer", "isCorrect": False},
                        {"text": "Conserver et sécher", "isCorrect": False},
                        {"text": "Épaissir et lier", "isCorrect": False}
                    ],
                    "correction": "Les acides (vin, vinaigre) de la marinade attaquent les fibres musculaires (attendrissement) tandis que les aromates parfument la chair forte du gibier."
                },
                {
                    "questionNumber": 37,
                    "question": "Pour réaliser une farce mousseline fine, quels sont les trois ingrédients fondamentaux ?",
                    "answerOptions": [
                        {"text": "Chair maigre gras œufs", "isCorrect": True},
                        {"text": "Chair grasse pain lait", "isCorrect": False},
                        {"text": "Chair maigre crème blanc d'œuf", "isCorrect": False},
                        {"text": "Chair grasse bouillon gélatine", "isCorrect": False}
                    ],
                    "correction": "La farce mousseline est une émulsion fine composée de chair maigre (volaille, poisson) mixée avec des blancs d'œufs et montée à la crème liquide riche en matière grasse."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est l'intérêt principal du 'repos' d'une viande rouge après une cuisson rôtie ?",
                    "answerOptions": [
                        {"text": "Répartition des sucs", "isCorrect": True},
                        {"text": "Refroidissement rapide", "isCorrect": False},
                        {"text": "Augmentation du poids", "isCorrect": False},
                        {"text": "Diminution du gras", "isCorrect": False}
                    ],
                    "correction": "Le repos permet aux fibres musculaires contractées par la chaleur de se détendre et aux sucs internes, concentrés au centre, de se redistribuer uniformément, rendant la viande tendre et juteuse."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle sauce mère est réalisée à partir d'un fond brun de veau lié à l'amidon (fécule ou roux) ou par réduction ?",
                    "answerOptions": [
                        {"text": "Espagnole", "isCorrect": True},
                        {"text": "Allemande", "isCorrect": False},
                        {"text": "Suprême", "isCorrect": False},
                        {"text": "Mornay", "isCorrect": False}
                    ],
                    "correction": "La sauce Espagnole (ou fond brun lié) est la sauce mère brune classique. Elle sert de base aux sauces dérivées comme la Bordelaise, la Chasseur ou la Madère."
                },
                {
                    "questionNumber": 40,
                    "question": "En pâtisserie, qu'appelle-t-on le 'foisonnement' lors de la réalisation d'une glace ou d'un sorbet ?",
                    "answerOptions": [
                        {"text": "Incorporation d'air", "isCorrect": True},
                        {"text": "Cristallisation du sucre", "isCorrect": False},
                        {"text": "Ajout de matière grasse", "isCorrect": False},
                        {"text": "Mélange des parfums", "isCorrect": False}
                    ],
                    "correction": "Le foisonnement est l'augmentation de volume de l'appareil à glace due à l'incorporation de bulles d'air lors du turbinage. Cela donne une texture onctueuse et moins dure."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : SCIENCES APPLIQUÉES À L'ALIMENTATION & HYGIÈNE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : SCIENCES APPLIQUÉES À L'ALIMENTATION & HYGIÈNE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Que signifie l'acronyme HACCP, méthode obligatoire dans la restauration pour garantir la sécurité des aliments ?",
                    "answerOptions": [
                        {"text": "Hazard Analysis Critical Control Point", "isCorrect": True},
                        {"text": "Hygiene Analysis Control Critical Process", "isCorrect": False},
                        {"text": "Hazard Association Control Culinary Process", "isCorrect": False},
                        {"text": "Hygiene Association Critical Control Point", "isCorrect": False}
                    ],
                    "correction": "L'HACCP (Analyse des Dangers et Points Critiques pour leur Maîtrise) est un système préventif visant à identifier, évaluer et maîtriser les dangers significatifs au regard de la sécurité des aliments."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la zone de température dite 'zone de danger' où la multiplication bactérienne est la plus intense ?",
                    "answerOptions": [
                        {"text": "De 10 à 63 degrés", "isCorrect": True},
                        {"text": "De 0 à 3 degrés", "isCorrect": False},
                        {"text": "De 65 à 100 degrés", "isCorrect": False},
                        {"text": "De moins 18 à 0 degrés", "isCorrect": False}
                    ],
                    "correction": "Entre 10°C et 63°C, les conditions sont optimales pour la division cellulaire des bactéries mésophiles. C'est pourquoi les produits doivent être stockés en dessous de 3°C ou maintenus au chaud à plus de 63°C."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le nom scientifique des bactéries capables de se développer au froid, comme dans un réfrigérateur ?",
                    "answerOptions": [
                        {"text": "Psychrotrophes", "isCorrect": True},
                        {"text": "Thermophiles", "isCorrect": False},
                        {"text": "Mésophiles", "isCorrect": False},
                        {"text": "Acidophiles", "isCorrect": False}
                    ],
                    "correction": "Les bactéries psychrotrophes (comme Listeria monocytogenes) ont la particularité redoutable de pouvoir se multiplier lentement même à des températures de réfrigération (entre 0°C et 4°C)."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle bactérie pathogène est principalement transmise par une manipulation humaine, notamment via des plaies infectées ou la toux ?",
                    "answerOptions": [
                        {"text": "Staphylocoque doré", "isCorrect": True},
                        {"text": "Clostridium botulinum", "isCorrect": False},
                        {"text": "Bacillus cereus", "isCorrect": False},
                        {"text": "Campylobacter", "isCorrect": False}
                    ],
                    "correction": "Le Staphylococcus aureus est un germe dont le réservoir principal est l'homme (nez, gorge, peau, plaies). Sa présence dans un plat témoigne souvent d'un défaut d'hygiène du personnel (lavage des mains, port du masque, pansement)."
                },
                {
                    "questionNumber": 45,
                    "question": "En restauration collective, combien de temps doit-on conserver les 'plats témoins' à la disposition des services vétérinaires ?",
                    "answerOptions": [
                        {"text": "5 jours", "isCorrect": True},
                        {"text": "24 heures", "isCorrect": False},
                        {"text": "3 jours", "isCorrect": False},
                        {"text": "1 semaine", "isCorrect": False}
                    ],
                    "correction": "Les échantillons témoins (environ 100g de chaque plat servi) doivent être conservés au froid positif (0 à 3°C) pendant 5 jours après la dernière consommation, pour analyse en cas de TIAC."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la durée maximale autorisée pour refroidir un plat cuisiné de 63°C à 10°C lors d'un refroidissement rapide ?",
                    "answerOptions": [
                        {"text": "Moins de deux heures", "isCorrect": True},
                        {"text": "Moins de quatre heures", "isCorrect": False},
                        {"text": "Moins de trente minutes", "isCorrect": False},
                        {"text": "Moins de cinq heures", "isCorrect": False}
                    ],
                    "correction": "La réglementation impose un passage de +63°C à +10°C à cœur en moins de 2 heures (souvent 1h50 en pratique) pour traverser rapidement la zone de danger bactérien le plus vite possible, grâce à une cellule de refroidissement."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel parasite visible à l'œil nu peut infester les poissons sauvages crus comme le maquereau ou le saumon ?",
                    "answerOptions": [
                        {"text": "Anisakis", "isCorrect": True},
                        {"text": "Ténia", "isCorrect": False},
                        {"text": "Ascaris", "isCorrect": False},
                        {"text": "Toxoplasme", "isCorrect": False}
                    ],
                    "correction": "L'Anisakis est un ver parasite. Pour les poissons destinés à être consommés crus ou peu cuits, la réglementation impose une congélation préalable à -20°C pendant 24h pour tuer ce parasite."
                },
                {
                    "questionNumber": 48,
                    "question": "Quelle est la différence fondamentale entre le nettoyage et la désinfection dans le plan de nettoyage ?",
                    "answerOptions": [
                        {"text": "Le nettoyage élimine la saleté visible alors que la désinfection tue les micro-organismes", "isCorrect": True},
                        {"text": "Le nettoyage tue les bactéries alors que la désinfection fait briller le matériel", "isCorrect": False},
                        {"text": "Le nettoyage utilise de l'eau chaude alors que la désinfection utilise de l'eau froide", "isCorrect": False},
                        {"text": "Le nettoyage est facultatif alors que la désinfection est une étape obligatoire légale", "isCorrect": False}
                    ],
                    "correction": "Le nettoyage (détergence) retire les souillures organiques et minérales (le 'gras' et le 'calcaire'). La désinfection intervient ensuite sur une surface propre pour détruire les microbes invisibles."
                },
                {
                    "questionNumber": 49,
                    "question": "Combien d'allergènes à déclaration obligatoire (INCO) existe-t-il actuellement dans la réglementation européenne ?",
                    "answerOptions": [
                        {"text": "14", "isCorrect": True},
                        {"text": "10", "isCorrect": False},
                        {"text": "22", "isCorrect": False},
                        {"text": "8", "isCorrect": False}
                    ],
                    "correction": "Il y a 14 allergènes majeurs à signaler obligatoirement par écrit aux consommateurs, dont le gluten, les crustacés, les œufs, les arachides, le lait, les fruits à coque, etc."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel terme définit la quantité d'eau libre disponible dans un aliment pour le développement microbien ?",
                    "answerOptions": [
                        {"text": "Aw", "isCorrect": True},
                        {"text": "pH", "isCorrect": False},
                        {"text": "DLC", "isCorrect": False},
                        {"text": "PMS", "isCorrect": False}
                    ],
                    "correction": "L'Aw (Activity of Water) mesure l'eau non liée disponible. Plus l'Aw est proche de 1 (eau pure), plus les bactéries se développent. En dessous de 0.60 (produits secs), les bactéries ne se multiplient plus."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle bactérie anaérobie stricte peut produire une toxine mortelle dans des conserves mal stérilisées ou sous-vide ?",
                    "answerOptions": [
                        {"text": "Clostridium botulinum", "isCorrect": True},
                        {"text": "Salmonella enteritidis", "isCorrect": False},
                        {"text": "Escherichia coli", "isCorrect": False},
                        {"text": "Listeria monocytogenes", "isCorrect": False}
                    ],
                    "correction": "Clostridium botulinum se développe en l'absence d'oxygène (anaérobie) et produit la toxine botulique, un poison neurotoxique violent. C'est le danger majeur des conserves artisanales et du sous-vide mal maîtrisé."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle vitamine est particulièrement sensible à la chaleur (thermolabile) et est détruite par des cuissons longues ?",
                    "answerOptions": [
                        {"text": "Vitamine C", "isCorrect": True},
                        {"text": "Vitamine D", "isCorrect": False},
                        {"text": "Vitamine K", "isCorrect": False},
                        {"text": "Vitamine E", "isCorrect": False}
                    ],
                    "correction": "La vitamine C (acide ascorbique) est la plus fragile des vitamines. Elle est détruite par la chaleur, la lumière et l'oxydation à l'air. Les cuissons vapeurs rapides préservent mieux cette vitamine."
                },
                {
                    "questionNumber": 53,
                    "question": "Que signifie le sigle TIAC dans le contexte de la sécurité sanitaire ?",
                    "answerOptions": [
                        {"text": "Toxi-Infection Alimentaire Collective", "isCorrect": True},
                        {"text": "Taux d'Infection Alimentaire Critique", "isCorrect": False},
                        {"text": "Traitement Intensif Anti Contamination", "isCorrect": False},
                        {"text": "Température Interdite Au Cœur", "isCorrect": False}
                    ],
                    "correction": "Une TIAC est définie par l'apparition d'au moins deux cas similaires d'une symptomatologie, en général gastro-intestinale, dont on peut rapporter la cause à une même origine alimentaire."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel document obligatoire regroupe l'ensemble des procédures d'hygiène, d'autocontrôles et de traçabilité d'un établissement ?",
                    "answerOptions": [
                        {"text": "PMS", "isCorrect": True},
                        {"text": "Kbis", "isCorrect": False},
                        {"text": "DUERP", "isCorrect": False},
                        {"text": "DLUO", "isCorrect": False}
                    ],
                    "correction": "Le Plan de Maîtrise Sanitaire (PMS) est le document de référence qui décrit les mesures prises par l'établissement pour assurer l'hygiène et la sécurité alimentaire (Bonnes Pratiques, HACCP, Traçabilité)."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est la particularité des toxines produites par le Staphylocoque doré par rapport à la bactérie elle-même ?",
                    "answerOptions": [
                        {"text": "Elles sont thermostables", "isCorrect": True},
                        {"text": "Elles sont vivantes", "isCorrect": False},
                        {"text": "Elles sont gazeuses", "isCorrect": False},
                        {"text": "Elles sont visibles", "isCorrect": False}
                    ],
                    "correction": "Si la cuisson tue la bactérie Staphylococcus aureus, elle ne détruit pas forcément ses toxines déjà produites, car celles-ci sont thermostables (résistantes à la chaleur)."
                },
                {
                    "questionNumber": 56,
                    "question": "Dans le cadre de la méthode de gestion des stocks, que signifie le principe FIFO ?",
                    "answerOptions": [
                        {"text": "Premier Entré Premier Sorti", "isCorrect": True},
                        {"text": "Finir Impérativement Frais Ouvert", "isCorrect": False},
                        {"text": "Faire Inventaire Fiche Outil", "isCorrect": False},
                        {"text": "Frais Intérieur Froid Obscur", "isCorrect": False}
                    ],
                    "correction": "Le FIFO (First In, First Out ou PEPS) impose d'utiliser en priorité les produits les plus anciens (ou dont la DLC est la plus proche) pour éviter le gaspillage et garantir la fraîcheur."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel nutriment principal, présent dans les viandes et poissons, est indispensable à la construction et au renouvellement des cellules ?",
                    "answerOptions": [
                        {"text": "Protéines", "isCorrect": True},
                        {"text": "Glucides", "isCorrect": False},
                        {"text": "Lipides", "isCorrect": False},
                        {"text": "Fibres", "isCorrect": False}
                    ],
                    "correction": "Les protéines sont des macronutriments bâtisseurs constitués d'acides aminés. Elles sont essentielles à la structure musculaire et cutanée ainsi qu'aux fonctions vitales."
                },
                {
                    "questionNumber": 58,
                    "question": "Pourquoi est-il strictement interdit de décongeler un produit à température ambiante ?",
                    "answerOptions": [
                        {"text": "Reprise exponentielle des microbes", "isCorrect": True},
                        {"text": "Perte totale des vitamines", "isCorrect": False},
                        {"text": "Changement de couleur de la chair", "isCorrect": False},
                        {"text": "Durcissement des fibres musculaires", "isCorrect": False}
                    ],
                    "correction": "Lors de la décongélation, les exsudats riches en nutriments et la température ambiante favorisent une multiplication bactérienne foudroyante. La décongélation doit se faire au froid positif (+4°C)."
                },
                {
                    "questionNumber": 59,
                    "question": "Quelle famille de micro-organismes est utile pour la fabrication du pain, du vin et de la bière ?",
                    "answerOptions": [
                        {"text": "Levures", "isCorrect": True},
                        {"text": "Virus", "isCorrect": False},
                        {"text": "Protozoaires", "isCorrect": False},
                        {"text": "Prions", "isCorrect": False}
                    ],
                    "correction": "Les levures (comme Saccharomyces cerevisiae) sont des champignons microscopiques qui provoquent la fermentation alcoolique en transformant les sucres en alcool et en gaz carbonique."
                },
                {
                    "questionNumber": 60,
                    "question": "Sur une étiquette de produit d'entretien professionnel, que signifie un pictogramme représentant un losange rouge avec un point d'exclamation ?",
                    "answerOptions": [
                        {"text": "Nocif ou irritant", "isCorrect": True},
                        {"text": "Corrosif pour les métaux", "isCorrect": False},
                        {"text": "Danger pour l'environnement", "isCorrect": False},
                        {"text": "Explosif sous la chaleur", "isCorrect": False}
                    ],
                    "correction": "Ce pictogramme signale un danger pour la santé : le produit peut être irritant pour les yeux ou la peau, sensibilisant ou nocif en cas d'ingestion. Il impose le port de gants et parfois de lunettes."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : GESTION, APPROVISIONNEMENT & COÛTS (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : GESTION, APPROVISIONNEMENT & COÛTS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la formule de base pour calculer la Consommation de Matières (Coût Matière) d'une période donnée ?",
                    "answerOptions": [
                        {"text": "Stock Initial plus Achats moins Stock Final", "isCorrect": True},
                        {"text": "Chiffre d'Affaires moins Marge Brute", "isCorrect": False},
                        {"text": "Stock Final moins Stock Initial plus Achats", "isCorrect": False},
                        {"text": "Achats de la période divisés par le nombre de couverts", "isCorrect": False}
                    ],
                    "correction": "La consommation de matières correspond à tout ce qui a 'disparu' du stock pour être vendu. On part de ce qu'on avait (SI), on ajoute ce qu'on a acheté (Achats) et on retire ce qui reste (SF)."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel indicateur obtient-on en soustrayant le Coût Matière du Chiffre d'Affaires HT ?",
                    "answerOptions": [
                        {"text": "Marge brute", "isCorrect": True},
                        {"text": "Résultat net", "isCorrect": False},
                        {"text": "Valeur ajoutée", "isCorrect": False},
                        {"text": "Excédent brut", "isCorrect": False}
                    ],
                    "correction": "La Marge Brute (ou Marge Commerciale) est l'indicateur premier de rentabilité en cuisine. C'est l'argent qui reste après avoir payé les ingrédients pour couvrir les autres frais (personnel, loyer, énergie)."
                },
                {
                    "questionNumber": 63,
                    "question": "En restauration commerciale classique, quel est l'ordre de grandeur cible pour le 'ratio matière' (coût matière en pourcentage) ?",
                    "answerOptions": [
                        {"text": "Entre 25 et 30 pour cent", "isCorrect": True},
                        {"text": "Entre 5 et 10 pour cent", "isCorrect": False},
                        {"text": "Entre 50 et 60 pour cent", "isCorrect": False},
                        {"text": "Entre 70 et 80 pour cent", "isCorrect": False}
                    ],
                    "correction": "Pour être rentable, un restaurant vise généralement un coût matière situé entre 25% et 30% du prix de vente HT. Au-delà, la marge risque d'être insuffisante pour couvrir les charges fixes."
                },
                {
                    "questionNumber": 64,
                    "question": "À quoi sert principalement une 'Fiche Technique' en gestion de cuisine ?",
                    "answerOptions": [
                        {"text": "Établir le coût de revient précis d'une portion", "isCorrect": True},
                        {"text": "Présenter le menu aux clients en salle", "isCorrect": False},
                        {"text": "Lister les allergènes pour l'inspection sanitaire", "isCorrect": False},
                        {"text": "Calculer les congés payés des employés", "isCorrect": False}
                    ],
                    "correction": "La fiche technique est un outil de gestion interne qui standardise la recette (grammages) et valorise chaque ingrédient pour déterminer combien coûte exactement une assiette à produire."
                },
                {
                    "questionNumber": 65,
                    "question": "Comment calcule-t-on le 'Ticket Moyen' d'un restaurant ?",
                    "answerOptions": [
                        {"text": "Chiffre d'Affaires divisé par nombre de couverts", "isCorrect": True},
                        {"text": "Total des charges divisé par nombre de jours", "isCorrect": False},
                        {"text": "Prix du plat le plus cher plus le moins cher divisé par deux", "isCorrect": False},
                        {"text": "Marge brute divisée par le nombre de salariés", "isCorrect": False}
                    ],
                    "correction": "Le ticket moyen représente la dépense moyenne d'un client. On l'obtient en divisant le CA total d'un service ou d'une période par le nombre de clients servis (couverts)."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le taux de TVA intermédiaire applicable en France pour la majorité des ventes de plats à consommer sur place ?",
                    "answerOptions": [
                        {"text": "10 pour cent", "isCorrect": True},
                        {"text": "20 pour cent", "isCorrect": False},
                        {"text": "5,5 pour cent", "isCorrect": False},
                        {"text": "2,1 pour cent", "isCorrect": False}
                    ],
                    "correction": "La TVA à 10% s'applique à la restauration (consommation immédiate), sauf pour les boissons alcoolisées qui restent au taux normal de 20%."
                },
                {
                    "questionNumber": 67,
                    "question": "Qu'appelle-t-on les 'Charges Fixes' dans le compte de résultat d'un restaurant ?",
                    "answerOptions": [
                        {"text": "Charges indépendantes du niveau d'activité", "isCorrect": True},
                        {"text": "Charges qui augmentent avec le nombre de clients", "isCorrect": False},
                        {"text": "Dépenses liées uniquement aux achats de nourriture", "isCorrect": False},
                        {"text": "Frais de réparation du matériel cassé", "isCorrect": False}
                    ],
                    "correction": "Les charges fixes (loyer, assurances, salaires fixes) sont les frais qu'il faut payer quel que soit le chiffre d'affaires, même si le restaurant est vide."
                },
                {
                    "questionNumber": 68,
                    "question": "Dans la gestion des stocks, quel document constate l'entrée réelle des marchandises dans l'économat et permet de vérifier la facture ?",
                    "answerOptions": [
                        {"text": "Bon de livraison", "isCorrect": True},
                        {"text": "Bon de commande", "isCorrect": False},
                        {"text": "Fiche de stock", "isCorrect": False},
                        {"text": "Bon de sortie", "isCorrect": False}
                    ],
                    "correction": "Le Bon de Livraison (BL) est remis par le fournisseur avec la marchandise. Il est la preuve de ce qui a été effectivement livré et doit être comparé au Bon de Commande et à la Facture."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle action permet de diminuer artificiellement le coût matière mais est illégale et dangereuse pour la réputation ?",
                    "answerOptions": [
                        {"text": "Diminuer les portions sans changer le prix", "isCorrect": True},
                        {"text": "Négocier les prix avec les fournisseurs", "isCorrect": False},
                        {"text": "Réduire le gaspillage en cuisine", "isCorrect": False},
                        {"text": "Utiliser des produits de saison moins chers", "isCorrect": False}
                    ],
                    "correction": "Si réduire le grammage (sans le dire) baisse le coût, c'est une pratique commerciale trompeuse si elle n'est pas affichée, contrairement à la négociation ou la gestion des pertes qui sont de la saine gestion."
                },
                {
                    "questionNumber": 70,
                    "question": "Le 'Seuil de Rentabilité' correspond au chiffre d'affaires à réaliser pour que le résultat soit égal à :",
                    "answerOptions": [
                        {"text": "0", "isCorrect": True},
                        {"text": "1000", "isCorrect": False},
                        {"text": "100", "isCorrect": False},
                        {"text": "10", "isCorrect": False}
                    ],
                    "correction": "Le seuil de rentabilité (ou point mort) est le niveau d'activité où les recettes couvrent exactement l'ensemble des charges (fixes et variables). Le bénéfice est alors nul. Au-dessus, on fait du profit."
                },
                {
                    "questionNumber": 71,
                    "question": "Pour calculer un prix de vente HT à partir d'un coût matière en utilisant un coefficient multiplicateur de 4, quelle est l'opération ?",
                    "answerOptions": [
                        {"text": "Coût matière multiplié par 4", "isCorrect": True},
                        {"text": "Coût matière divisé par 4", "isCorrect": False},
                        {"text": "Coût matière plus 4", "isCorrect": False},
                        {"text": "Coût matière moins 4", "isCorrect": False}
                    ],
                    "correction": "Le coefficient multiplicateur est une méthode simplifiée pour fixer les prix. Prix de Vente HT = Coût Matière x Coefficient. Si le coef est 4, cela correspond à un ratio matière de 25%."
                },
                {
                    "questionNumber": 72,
                    "question": "Que représente le 'rendement' d'un produit brut (comme un poisson entier) après parage et filetage ?",
                    "answerOptions": [
                        {"text": "Poids net utilisable divisé par poids brut acheté", "isCorrect": True},
                        {"text": "Poids des déchets divisé par poids net", "isCorrect": False},
                        {"text": "Prix au kilo multiplié par le poids des arêtes", "isCorrect": False},
                        {"text": "Poids brut acheté moins le poids cuit", "isCorrect": False}
                    ],
                    "correction": "Le rendement s'exprime en pourcentage. C'est la part du produit qui finit réellement dans l'assiette. Exemple : un poisson a souvent un rendement de 40% à 50% (on jette 50% à 60% de déchets)."
                },
                {
                    "questionNumber": 73,
                    "question": "Dans le principe d'Omnès (ingénierie des menus), que signifie la règle de 'l'ouverture de gamme' ?",
                    "answerOptions": [
                        {"text": "L'écart entre le prix le plus bas et le prix le plus haut ne doit pas dépasser un certain ratio (souvent 2,5 à 3)", "isCorrect": True},
                        {"text": "Le restaurant doit être ouvert tous les jours de la semaine midi et soir", "isCorrect": False},
                        {"text": "La carte doit proposer au moins dix entrées et dix plats différents", "isCorrect": False},
                        {"text": "Les prix des plats doivent tous être identiques pour simplifier la gestion", "isCorrect": False}
                    ],
                    "correction": "La gamme de prix doit être cohérente. Si l'écart est trop grand (plus de 3 fois le prix entre le plat le moins cher et le plus cher), le client perd ses repères sur le standing de l'établissement."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle est la conséquence financière immédiate d'une erreur de 'coulage' (vol ou consommation non déclarée par le personnel) ?",
                    "answerOptions": [
                        {"text": "Augmentation du coût matière sans chiffre d'affaires en face", "isCorrect": True},
                        {"text": "Augmentation immédiate du chiffre d'affaires théorique", "isCorrect": False},
                        {"text": "Diminution des charges fixes de l'entreprise", "isCorrect": False},
                        {"text": "Amélioration de la marge brute globale", "isCorrect": False}
                    ],
                    "correction": "Le coulage (vol, perte, repas non comptabilisés) fait sortir de la marchandise du stock (coût) sans générer de vente. Cela dégrade directement la marge brute."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle est la définition du 'Prime Cost' (Coût Principal) ?",
                    "answerOptions": [
                        {"text": "Coût Matières plus Frais de Personnel", "isCorrect": True},
                        {"text": "Coût Matières plus Frais Généraux", "isCorrect": False},
                        {"text": "Frais de Personnel plus Loyer", "isCorrect": False},
                        {"text": "Marge Brute moins Impôts", "isCorrect": False}
                    ],
                    "correction": "Le Prime Cost regroupe les deux plus gros postes de dépenses d'un restaurant : les matières premières et la main d'œuvre. C'est un indicateur clé de performance opérationnelle."
                },
                {
                    "questionNumber": 76,
                    "question": "Si un restaurateur achète un produit 10€ HT et le revend 30€ HT, quel est son coefficient multiplicateur ?",
                    "answerOptions": [
                        {"text": "3", "isCorrect": True},
                        {"text": "0,33", "isCorrect": False},
                        {"text": "30", "isCorrect": False},
                        {"text": "20", "isCorrect": False}
                    ],
                    "correction": "Coefficient = Prix de Vente HT / Prix d'Achat HT. Ici, 30 / 10 = 3."
                },
                {
                    "questionNumber": 77,
                    "question": "Lors d'un inventaire, comment valorise-t-on généralement le stock de marchandises restantes ?",
                    "answerOptions": [
                        {"text": "Au dernier prix d'achat connu", "isCorrect": True},
                        {"text": "Au prix de vente affiché sur la carte", "isCorrect": False},
                        {"text": "Au prix moyen du marché national", "isCorrect": False},
                        {"text": "À zéro car c'est du stock dormant", "isCorrect": False}
                    ],
                    "correction": "Pour la comptabilité, on valorise le stock au coût d'acquisition (prix d'achat). Utiliser le prix de vente fausserait le bilan en anticipant des bénéfices non réalisés."
                },
                {
                    "questionNumber": 78,
                    "question": "Qu'est-ce qu'une 'charge variable' ?",
                    "answerOptions": [
                        {"text": "Une dépense proportionnelle au volume de l'activité", "isCorrect": True},
                        {"text": "Une dépense dont le montant est fixé par un contrat annuel", "isCorrect": False},
                        {"text": "Une dépense que l'on peut décider de ne pas payer", "isCorrect": False},
                        {"text": "Une dépense liée à l'investissement immobilier", "isCorrect": False}
                    ],
                    "correction": "Les charges variables (achats de marchandises, blanchisserie, énergies de production) augmentent quand le restaurant sert plus de couverts et diminuent quand l'activité baisse."
                },
                {
                    "questionNumber": 79,
                    "question": "Pourquoi faut-il déduire la valeur des 'repas du personnel' du coût matière global en fin de mois ?",
                    "answerOptions": [
                        {"text": "Car ce n'est pas une marchandise vendue aux clients", "isCorrect": True},
                        {"text": "Car le personnel ne mange pas les mêmes produits", "isCorrect": False},
                        {"text": "Pour augmenter artificiellement les charges de personnel", "isCorrect": False},
                        {"text": "Parce que la TVA n'est pas applicable sur ces repas", "isCorrect": False}
                    ],
                    "correction": "Le coût matière doit refléter la consommation des clients pour calculer la marge commerciale. Les repas du personnel sont un avantage en nature (frais de personnel) et doivent être reclassés comptablement."
                },
                {
                    "questionNumber": 80,
                    "question": "Que désigne le terme 'Ristourne' sur une facture fournisseur ?",
                    "answerOptions": [
                        {"text": "Réduction de prix accordée en fin de période selon le volume d'achats", "isCorrect": True},
                        {"text": "Réduction immédiate pour défaut de qualité du produit", "isCorrect": False},
                        {"text": "Pénalité de retard de paiement appliquée au client", "isCorrect": False},
                        {"text": "Taxe supplémentaire pour livraison urgente", "isCorrect": False}
                    ],
                    "correction": "La ristourne est une réduction commerciale différée, calculée sur l'ensemble des opérations réalisées avec un client pendant une période donnée (souvent annuelle), pour fidéliser le client."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : ORGANISATION, MANAGEMENT & ENVIRONNEMENT PROFESSIONNEL (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : ORGANISATION, MANAGEMENT & ENVIRONNEMENT PROFESSIONNEL",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel principe fondamental d'organisation des locaux impose que les circuits propres et les circuits sales ne se croisent jamais ?",
                    "answerOptions": [
                        {"text": "Marche en avant", "isCorrect": True},
                        {"text": "Sectorisation froide", "isCorrect": False},
                        {"text": "Liaison chaude", "isCorrect": False},
                        {"text": "Gestion des flux tendus", "isCorrect": False}
                    ],
                    "correction": "La marche en avant est un principe d'organisation (dans l'espace ou dans le temps) qui garantit que les produits sains ne croisent jamais les produits souillés ou les déchets, afin d'éviter les contaminations croisées."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la composition métallique standard de l'acier inoxydable alimentaire utilisé pour le matériel de cuisine (Inox 18/10) ?",
                    "answerOptions": [
                        {"text": "Fer et chrome et nickel", "isCorrect": True},
                        {"text": "Fer et aluminium et zinc", "isCorrect": False},
                        {"text": "Cuivre et étain et plomb", "isCorrect": False},
                        {"text": "Titane et argent et magnésium", "isCorrect": False}
                    ],
                    "correction": "L'inox 18/10 contient environ 18% de chrome (pour l'inoxydabilité) et 10% de nickel (pour la neutralité alimentaire et la brillance), le reste étant du fer et une infime part de carbone."
                },
                {
                    "questionNumber": 83,
                    "question": "En droit du travail, quel document obligatoire adapte les règles générales du Code du travail aux spécificités du secteur HCR (Hôtels Cafés Restaurants) ?",
                    "answerOptions": [
                        {"text": "Convention Collective Nationale", "isCorrect": True},
                        {"text": "Règlement intérieur de l'entreprise", "isCorrect": False},
                        {"text": "Contrat de travail individuel", "isCorrect": False},
                        {"text": "Code de la santé publique", "isCorrect": False}
                    ],
                    "correction": "La Convention Collective des HCR (IDCC 1979) négocie des règles spécifiques à la profession (grille des salaires, préavis, jours fériés garantis) qui prévalent sur le droit général si elles sont plus favorables."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel équipement de cuisson fonctionne grâce à un champ magnétique créant des courants de Foucault dans le fond du récipient ?",
                    "answerOptions": [
                        {"text": "Plaque à induction", "isCorrect": True},
                        {"text": "Plaque vitrocéramique radiante", "isCorrect": False},
                        {"text": "Plaque électrique en fonte", "isCorrect": False},
                        {"text": "Brûleur gaz atmosphérique", "isCorrect": False}
                    ],
                    "correction": "L'induction ne chauffe pas la plaque elle-même mais directement le métal ferreux du récipient grâce au magnétisme. C'est le système qui offre le meilleur rendement énergétique (plus de 90%)."
                },
                {
                    "questionNumber": 85,
                    "question": "Qu'est-ce un déchet classé comme 'biodechet' en restauration ?",
                    "answerOptions": [
                        {"text": "Déchet organique fermentescible", "isCorrect": True},
                        {"text": "Emballage en carton souillé", "isCorrect": False},
                        {"text": "Huile de friture usagée", "isCorrect": False},
                        {"text": "Verre cassé non recyclable", "isCorrect": False}
                    ],
                    "correction": "Les biodéchets sont les déchets biodégradables de jardin ou de parc, ainsi que les déchets alimentaires ou de cuisine (épluchures, restes de repas) qui doivent être valorisés (compostage ou méthanisation)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le rôle principal du 'Bac à graisses' installé obligatoirement sous les plonges ou en sortie de cuisine ?",
                    "answerOptions": [
                        {"text": "Retenir les matières grasses par décantation", "isCorrect": True},
                        {"text": "Filtrer les produits chimiques toxiques", "isCorrect": False},
                        {"text": "Broyer les déchets solides organiques", "isCorrect": False},
                        {"text": "Désinfecter les eaux usées avant rejet", "isCorrect": False}
                    ],
                    "correction": "Le bac à graisses sépare les graisses (qui flottent) et les matières lourdes (qui coulent) de l'eau. Il empêche les graisses de boucher les canalisations et de polluer le réseau d'assainissement collectif."
                },
                {
                    "questionNumber": 87,
                    "question": "Dans une brigade de cuisine, qui est chargé d'annoncer les bons de commande et de vérifier les assiettes avant leur départ en salle ?",
                    "answerOptions": [
                        {"text": "Aboyeur", "isCorrect": True},
                        {"text": "Communard", "isCorrect": False},
                        {"text": "Tournant", "isCorrect": False},
                        {"text": "Entremetier", "isCorrect": False}
                    ],
                    "correction": "L'aboyeur (souvent le Chef ou le Second) est au passe. Il gère le flux des commandes, annonce les plats à voix haute et contrôle la qualité finale du dressage (le 'contrôle qualité' avant envoi)."
                },
                {
                    "questionNumber": 88,
                    "question": "Que définit officiellement un circuit d'approvisionnement dit 'Court' ?",
                    "answerOptions": [
                        {"text": "Maximum un intermédiaire", "isCorrect": True},
                        {"text": "Maximum cent kilomètres", "isCorrect": False},
                        {"text": "Uniquement la vente directe", "isCorrect": False},
                        {"text": "Uniquement des produits bio", "isCorrect": False}
                    ],
                    "correction": "La définition officielle du circuit court ne dépend pas de la distance kilométrique, mais du nombre d'intermédiaires entre le producteur et le consommateur : zéro (vente directe) ou un seul intermédiaire maximum."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle classe de feu concerne spécifiquement les feux d'auxiliaires de cuisson (huiles et graisses végétales ou animales) ?",
                    "answerOptions": [
                        {"text": "Classe F", "isCorrect": True},
                        {"text": "Classe B", "isCorrect": False},
                        {"text": "Classe C", "isCorrect": False},
                        {"text": "Classe A", "isCorrect": False}
                    ],
                    "correction": "La classe F a été créée spécifiquement pour les feux d'huiles et graisses de cuisine. Les extincteurs adaptés contiennent des agents qui forment un film étanche et refroidissant (saponification). Ne jamais mettre d'eau !"
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle est la cause principale des Troubles Musculo-Squelettiques (TMS) en cuisine ?",
                    "answerOptions": [
                        {"text": "Gestes répétitifs et postures contraintes", "isCorrect": True},
                        {"text": "Manipulation de produits chimiques", "isCorrect": False},
                        {"text": "Exposition au bruit des hottes", "isCorrect": False},
                        {"text": "Variation brutale de température", "isCorrect": False}
                    ],
                    "correction": "Les TMS (douleurs au dos, poignets, épaules) sont provoqués par la répétition des gestes (épluchage, découpe), le port de charges lourdes et les stations debout statiques prolongées."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel type de maintenance consiste à intervenir sur une machine avant qu'elle ne tombe en panne, selon un calendrier défini ?",
                    "answerOptions": [
                        {"text": "Maintenance préventive", "isCorrect": True},
                        {"text": "Maintenance curative", "isCorrect": False},
                        {"text": "Maintenance corrective", "isCorrect": False},
                        {"text": "Maintenance palliative", "isCorrect": False}
                    ],
                    "correction": "La maintenance préventive (ex : révision annuelle, détartrage mensuel) permet d'éviter les arrêts de production imprévus et prolonge la durée de vie du matériel, contrairement à la maintenance curative (réparation après panne)."
                },
                {
                    "questionNumber": 92,
                    "question": "Sur une fiche de paie, qu'appelle-t-on le 'salaire brut' ?",
                    "answerOptions": [
                        {"text": "Salaire avant déduction des cotisations sociales", "isCorrect": True},
                        {"text": "Somme réellement virée sur le compte bancaire", "isCorrect": False},
                        {"text": "Coût total dépensé par l'employeur pour le salarié", "isCorrect": False},
                        {"text": "Montant du salaire minimum légal en vigueur", "isCorrect": False}
                    ],
                    "correction": "Le salaire brut est la rémunération due par l'employeur pour le travail effectué. On y soustrait ensuite les cotisations salariales pour obtenir le 'Net à payer'."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est l'avantage ergonomique principal d'une cellule de cuisson mixte (four mixte) programmable ?",
                    "answerOptions": [
                        {"text": "Automatisation et nettoyage automatique", "isCorrect": True},
                        {"text": "Suppression totale de la surveillance", "isCorrect": False},
                        {"text": "Réduction du coût d'achat initial", "isCorrect": False},
                        {"text": "Augmentation de la surface au sol", "isCorrect": False}
                    ],
                    "correction": "Les fours mixtes modernes améliorent l'ergonomie grâce aux programmes automatiques (moins de stress), aux sondes à cœur et surtout aux systèmes de lavage automatique qui évitent le contact avec les détergents agressifs."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle est la définition juridique du temps de travail effectif ?",
                    "answerOptions": [
                        {"text": "Temps où le salarié est à la disposition de l'employeur", "isCorrect": True},
                        {"text": "Temps de présence dans les vestiaires inclus", "isCorrect": False},
                        {"text": "Temps de trajet domicile travail inclus", "isCorrect": False},
                        {"text": "Temps de pause déjeuner inclus", "isCorrect": False}
                    ],
                    "correction": "Le travail effectif est le temps pendant lequel le salarié est à la disposition de l'employeur et se conforme à ses directives sans pouvoir vaquer librement à des occupations personnelles."
                },
                {
                    "questionNumber": 95,
                    "question": "Pour garantir la sécurité, quelles sont les deux caractéristiques obligatoires des chaussures de sécurité en cuisine (Norme EN ISO 20345) ?",
                    "answerOptions": [
                        {"text": "Embout de protection et semelle antidérapante", "isCorrect": True},
                        {"text": "Semelle isolante et tige montante", "isCorrect": False},
                        {"text": "Matière imperméable et couleur blanche", "isCorrect": False},
                        {"text": "Résistance aux acides et fermeture sans lacets", "isCorrect": False}
                    ],
                    "correction": "Les chaussures de cuisine doivent impérativement protéger contre la chute d'objets lourds (coque/embout) et contre les glissades sur sol gras ou mouillé (semelle antidérapante SRC)."
                },
                {
                    "questionNumber": 96,
                    "question": "En management, comment qualifie-t-on un style de direction qui associe les collaborateurs à la prise de décision ?",
                    "answerOptions": [
                        {"text": "Participatif", "isCorrect": True},
                        {"text": "Directif", "isCorrect": False},
                        {"text": "Paternaliste", "isCorrect": False},
                        {"text": "Délégatif", "isCorrect": False}
                    ],
                    "correction": "Le management participatif vise à renforcer la cohésion et la motivation en consultant l'équipe, en favorisant le dialogue et en impliquant les employés dans les objectifs de l'entreprise."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel label environnemental public garantit des produits issus d'une agriculture sans produits chimiques de synthèse ni OGM ?",
                    "answerOptions": [
                        {"text": "Agriculture Biologique", "isCorrect": True},
                        {"text": "Label Rouge", "isCorrect": False},
                        {"text": "Haute Valeur Environnementale", "isCorrect": False},
                        {"text": "Fairtrade Max Havelaar", "isCorrect": False}
                    ],
                    "correction": "Le logo AB (feuille étoilée européenne) certifie le respect du règlement sur l'agriculture biologique : respect des cycles naturels, bien-être animal, interdiction des pesticides de synthèse et des OGM."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle est la fonction d'un 'piano' dans le langage professionnel de la cuisine ?",
                    "answerOptions": [
                        {"text": "Bloc de cuisson central", "isCorrect": True},
                        {"text": "Plan de travail en marbre", "isCorrect": False},
                        {"text": "Chambre froide négative", "isCorrect": False},
                        {"text": "Table de passe chauffante", "isCorrect": False}
                    ],
                    "correction": "Le 'piano' désigne le fourneau central ou le bloc de cuisson principal regroupant plusieurs feux, plaques, fours et parfois bains-marie, autour duquel s'organise la brigade."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel document doit être obligatoirement remis au salarié à la fin de son contrat de travail, quel que soit le motif de rupture ?",
                    "answerOptions": [
                        {"text": "Certificat de travail", "isCorrect": True},
                        {"text": "Lettre de recommandation", "isCorrect": False},
                        {"text": "Copie du registre du personnel", "isCorrect": False},
                        {"text": "Bilan de compétences", "isCorrect": False}
                    ],
                    "correction": "L'employeur a l'obligation légale de remettre le certificat de travail (attestant des dates et des postes occupés), l'attestation Pôle Emploi (France Travail) et le reçu pour solde de tout compte."
                },
                {
                    "questionNumber": 100,
                    "question": "Dans le cadre de la RSE (Responsabilité Sociétale des Entreprises), quel geste permet de réduire significativement la consommation d'eau en cuisine ?",
                    "answerOptions": [
                        {"text": "Utiliser des pistolets économiseurs en plonge", "isCorrect": True},
                        {"text": "Dégeler les produits sous un filet d'eau froide", "isCorrect": False},
                        {"text": "Laisser couler l'eau pour refroidir les fonds", "isCorrect": False},
                        {"text": "Laver le sol à grande eau deux fois par service", "isCorrect": False}
                    ],
                    "correction": "L'installation de douchettes/pistolets à gâchette sur les robinets de plonge permet d'arrêter l'eau dès qu'on ne s'en sert pas, réduisant la consommation de 50% par rapport à un robinet classique."
                }
            ]
        }
    }
}