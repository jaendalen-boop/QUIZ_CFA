# Fichier : quiz_cap_cuisine_100.py

quiz_data = {
    "title": "Quiz CAP Cuisine : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE, SÉCURITÉ ET HACCP (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Hygiène, Sécurité et HACCP (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la 'zone de danger' pour la multiplication des bactéries (en °C) ?",
                    "answerOptions": [
                        {"text": "Entre 0°C et 3°C.", "isCorrect": False},
                        {"text": "Entre 65°C et 100°C.", "isCorrect": False},
                        {"text": "Entre 8°C et 63°C.", "isCorrect": True},
                        {"text": "Uniquement au-dessus de 80°C.", "isCorrect": False}
                    ],
                    "correction": "La **zone de danger** (ou zone de croissance rapide) est généralement considérée entre **8°C et 63°C**. Il faut refroidir ou réchauffer rapidement les aliments pour traverser cette zone."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle doit être la température maximale de conservation des viandes hachées et des préparations de viandes fraîches (température à cœur) ?",
                    "answerOptions": [
                        {"text": "+7°C.", "isCorrect": False},
                        {"text": "+4°C.", "isCorrect": False},
                        {"text": "+2°C.", "isCorrect": True},
                        {"text": "0°C.", "isCorrect": False}
                    ],
                    "correction": "La température maximale pour les viandes hachées et les produits très sensibles (abats, produits de la pêche) est de **+2°C**."
                },
                {
                    "questionNumber": 3,
                    "question": "Que signifie l'acronyme 'DLC' ?",
                    "answerOptions": [
                        {"text": "Date Limite d'Usage.", "isCorrect": False},
                        {"text": "Durée Légale de Conservation.", "isCorrect": False},
                        {"text": "Date Limite de Consommation.", "isCorrect": True},
                        {"text": "Date Limite de Congélation.", "isCorrect": False}
                    ],
                    "correction": "La **DLC** est impérative. Après cette date, le produit est considéré comme impropre à la consommation et doit être jeté."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel principe d'organisation du travail est fondamental pour éviter la contamination entre produits bruts et produits finis ?",
                    "answerOptions": [
                        {"text": "Le respect des recettes.", "isCorrect": False},
                        {"text": "La marche en avant (dans l'espace ou dans le temps).", "isCorrect": True},
                        {"text": "Le respect de la hiérarchie.", "isCorrect": False},
                        {"text": "L'utilisation de la chaleur.", "isCorrect": False}
                    ],
                    "correction": "La **Marche en avant** garantit que les produits propres (finis ou cuits) ne recroisent jamais les produits souillés (bruts, déchets) dans un même circuit."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le rôle du 'Désinfectant' dans un Plan de Nettoyage et Désinfection (PND) ?",
                    "answerOptions": [
                        {"text": "Enlever les salissures visibles.", "isCorrect": False},
                        {"text": "Éliminer la salissure visible et les microbes.", "isCorrect": False},
                        {"text": "Réduire ou tuer les micro-organismes après le nettoyage.", "isCorrect": True},
                        {"text": "Rendre la surface brillante.", "isCorrect": False}
                    ],
                    "correction": "Le **Nettoyage** enlève la salissure. La **Désinfection** est l'étape suivante qui tue les germes restants. Les deux étapes sont distinctes."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le danger principal associé aux ustensiles en bois en cuisine professionnelle ?",
                    "answerOptions": [
                        {"text": "Ils sont trop chers.", "isCorrect": False},
                        {"text": "Ils ne peuvent pas être lavés au lave-vaisselle.", "isCorrect": False},
                        {"text": "Le bois est poreux et retient l'humidité, favorisant la prolifération bactérienne.", "isCorrect": True},
                        {"text": "Ils sont trop lourds.", "isCorrect": False}
                    ],
                    "correction": "Le bois est généralement proscrit des zones de production (sauf exception comme les billots de boucher) à cause de sa **porosité**."
                },
                {
                    "questionNumber": 7,
                    "question": "Qu'appelle-t-on 'contaminations croisées' ?",
                    "answerOptions": [
                        {"text": "Le mélange involontaire de deux recettes.", "isCorrect": False},
                        {"text": "Le transfert de micro-organismes (ou d'allergènes) d'un produit brut à un produit sain (ou cuit).", "isCorrect": True},
                        {"text": "Le mélange de deux ingrédients différents.", "isCorrect": False},
                        {"text": "La surchauffe des aliments.", "isCorrect": False}
                    ],
                    "correction": "Les **contaminations croisées** sont la cause principale des intoxications alimentaires. Ex : utiliser la même planche pour la volaille crue et les légumes coupés."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle température à cœur minimale un plat cuisiné doit-il atteindre lors de la cuisson pour être considéré comme sain ?",
                    "answerOptions": [
                        {"text": "55°C.", "isCorrect": False},
                        {"text": "60°C.", "isCorrect": False},
                        {"text": "63°C (ou 70°C pendant 2 minutes).", "isCorrect": True},
                        {"text": "80°C.", "isCorrect": False}
                    ],
                    "correction": "Une température de **63°C** au minimum (ou 70°C pendant deux minutes) est nécessaire pour tuer la plupart des micro-organismes pathogènes."
                },
                {
                    "questionNumber": 9,
                    "question": "Que doit-on faire immédiatement après s'être coupé la main en cuisine ?",
                    "answerOptions": [
                        {"text": "Continuer à travailler pour finir la tâche en cours.", "isCorrect": False},
                        {"text": "Appliquer un désinfectant et recouvrir la plaie d'un pansement étanche et d'un gant.", "isCorrect": True},
                        {"text": "Laisser la plaie à l'air libre pour qu'elle sèche.", "isCorrect": False},
                        {"text": "Laver l'ustensile qui a causé la coupure.", "isCorrect": False}
                    ],
                    "correction": "Le **pansement étanche** (souvent de couleur bleue pour être visible) empêche le sang et les germes de contaminer les aliments."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le temps maximum autorisé pour le refroidissement d'une préparation chaude (de +63°C à +10°C) ?",
                    "answerOptions": [
                        {"text": "1 heure.", "isCorrect": False},
                        {"text": "2 heures (le plus souvent).", "isCorrect": True},
                        {"text": "4 heures.", "isCorrect": False},
                        {"text": "Toute la nuit.", "isCorrect": False}
                    ],
                    "correction": "Le refroidissement rapide est crucial pour limiter la prolifération des bactéries. La norme est de passer de +63°C à +10°C à cœur en **moins de 2 heures**."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la température de conservation recommandée pour le poisson frais ?",
                    "answerOptions": [
                        {"text": "+7°C.", "isCorrect": False},
                        {"text": "Entre 0°C et +2°C, de préférence sur lit de glace.", "isCorrect": True},
                        {"text": "+5°C.", "isCorrect": False},
                        {"text": "-18°C.", "isCorrect": False}
                    ],
                    "correction": "Le poisson est très fragile. La conservation doit être proche de la glace fondante : **entre 0°C et +2°C**."
                },
                {
                    "questionNumber": 12,
                    "question": "Que signifie le terme 'allergène' dans le cadre de la restauration ?",
                    "answerOptions": [
                        {"text": "Un produit périmé.", "isCorrect": False},
                        {"text": "Un ingrédient qui peut provoquer une réaction immunitaire anormale chez une personne sensible.", "isCorrect": True},
                        {"text": "Un ingrédient rare et cher.", "isCorrect": False},
                        {"text": "Un colorant alimentaire.", "isCorrect": False}
                    ],
                    "correction": "Le restaurateur est légalement obligé d'informer le client sur la présence des **14 allergènes majeurs** (gluten, œufs, lait, etc.) dans ses plats."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est la fonction d'une 'chambre froide positive' ?",
                    "answerOptions": [
                        {"text": "Congeler les produits.", "isCorrect": False},
                        {"text": "Conserver les produits au-dessus de 0°C (généralement entre +1°C et +6°C).", "isCorrect": True},
                        {"text": "Cuire les produits lentement.", "isCorrect": False},
                        {"text": "Surgeler les produits.", "isCorrect": False}
                    ],
                    "correction": "La **chambre froide positive** sert au stockage à court et moyen terme des denrées fraîches."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel risque principal est associé à l'utilisation d'eau de Javel non rincée sur une surface en contact alimentaire ?",
                    "answerOptions": [
                        {"text": "Laisser des traces blanches.", "isCorrect": False},
                        {"text": "Un risque de contamination chimique (toxicité) du produit alimentaire.", "isCorrect": True},
                        {"text": "Endommager le matériel.", "isCorrect": False},
                        {"text": "Augmenter la prolifération des bactéries.", "isCorrect": False}
                    ],
                    "correction": "L'eau de Javel (hypochlorite de sodium) est un désinfectant puissant mais **toxique**. Le rinçage est obligatoire après son utilisation."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel doit être le premier geste en entrant dans la cuisine ?",
                    "answerOptions": [
                        {"text": "Mettre son tablier.", "isCorrect": False},
                        {"text": "Allumer les feux.", "isCorrect": False},
                        {"text": "Se laver et se désinfecter les mains.", "isCorrect": True},
                        {"text": "Vérifier le bon de commande.", "isCorrect": False}
                    ],
                    "correction": "L'**hygiène des mains** est le point de contrôle critique (CCP) le plus important en cuisine."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le seul métal qui n'est pas autorisé pour être en contact avec les aliments acides ?",
                    "answerOptions": [
                        {"text": "L'Acier inoxydable.", "isCorrect": False},
                        {"text": "Le Cuivre (non étamé).", "isCorrect": True},
                        {"text": "Le Fer.", "isCorrect": False},
                        {"text": "L'Aluminium.", "isCorrect": False}
                    ],
                    "correction": "Le **Cuivre** non étamé réagit avec l'acidité et peut libérer des composés toxiques (vert-de-gris) dans les aliments."
                },
                {
                    "questionNumber": 17,
                    "question": "Qu'est-ce qu'un 'Fournisseur agréé' dans le contexte de la restauration ?",
                    "answerOptions": [
                        {"text": "Un fournisseur qui livre gratuitement.", "isCorrect": False},
                        {"text": "Un fournisseur qui respecte les normes d'hygiène et de sécurité sanitaire pour la chaîne du froid, et qui est officiellement déclaré.", "isCorrect": True},
                        {"text": "Un fournisseur qui fait des promotions.", "isCorrect": False},
                        {"text": "Un fournisseur de produits bio.", "isCorrect": False}
                    ],
                    "correction": "L'**agrément sanitaire** assure la traçabilité et le contrôle des produits tout au long de la chaîne d'approvisionnement."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel EPI (Équipement de Protection Individuelle) est obligatoire pour manipuler une friteuse ou de l'eau bouillante ?",
                    "answerOptions": [
                        {"text": "Le masque chirurgical.", "isCorrect": False},
                        {"text": "Le tablier en cotte de mailles.", "isCorrect": False},
                        {"text": "Le port de gants de protection thermique.", "isCorrect": True},
                        {"text": "Le bonnet à cheveux.", "isCorrect": False}
                    ],
                    "correction": "Les **gants de protection thermique** (ou maniques) protègent contre les brûlures graves dues aux projections de graisse ou de liquides chauds."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est la couleur de planche à découper généralement associée aux viandes crues (bovins, porc, agneau) ?",
                    "answerOptions": [
                        {"text": "Verte.", "isCorrect": False},
                        {"text": "Rouge.", "isCorrect": True},
                        {"text": "Jaune.", "isCorrect": False},
                        {"text": "Bleue.", "isCorrect": False}
                    ],
                    "correction": "Le code couleur des planches est essentiel pour la marche en avant : **Rouge** = Viandes crues, Jaune = Volailles crues, Verte = Légumes, Bleu = Poissons, Blanc = Produits laitiers/Pains, Marron = Viandes cuites."
                },
                {
                    "questionNumber": 20,
                    "question": "Que doit-on vérifier en priorité lors de la réception des marchandises ?",
                    "answerOptions": [
                        {"text": "L'origine des produits.", "isCorrect": False},
                        {"text": "L'exactitude du bon de livraison et le respect des températures de la chaîne du froid.", "isCorrect": True},
                        {"text": "La couleur du camion de livraison.", "isCorrect": False},
                        {"text": "Le poids exact de chaque produit.", "isCorrect": False}
                    ],
                    "correction": "Le contrôle de la **température** (à l'aide d'un thermomètre sonde) est le point critique de la réception pour les produits frais."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNIQUES CULINAIRES DE BASE (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Techniques Culinaires de Base (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le nom de la coupe de légume en petits dés de 2 mm x 2 mm x 2 mm ?",
                    "answerOptions": [
                        {"text": "La Mirepoix.", "isCorrect": False},
                        {"text": "La Macédoine.", "isCorrect": False},
                        {"text": "La Brunoise.", "isCorrect": True},
                        {"text": "La Julienne.", "isCorrect": False}
                    ],
                    "correction": "La **Brunoise** est une coupe très fine, utilisée pour les garnitures aromatiques (échalotes, fines herbes) ou les finitions de potages."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment appelle-t-on l'action de faire suer (ou colorer) doucement la garniture aromatique avant d'ajouter le liquide pour un fond brun ?",
                    "answerOptions": [
                        {"text": "La Déglacer.", "isCorrect": False},
                        {"text": "Le Pinçage.", "isCorrect": True},
                        {"text": "Le Passer.", "isCorrect": False},
                        {"text": "Le Bluter.", "isCorrect": False}
                    ],
                    "correction": "Le **Pinçage** consiste à laisser colorer les sucs de la garniture aromatique (mirepoix) au fond du récipient avant de déglacer, ce qui apporte une couleur et un goût profond au fond."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est l'ingrédient principal de la liaison d'une Sauce Velouté ?",
                    "answerOptions": [
                        {"text": "Le Jaune d'œuf.", "isCorrect": False},
                        {"text": "Le Roux blanc et un fond blanc (volaille, veau, poisson).", "isCorrect": True},
                        {"text": "La Crème fraîche.", "isCorrect": False},
                        {"text": "Le Beurre manié.", "isCorrect": False}
                    ],
                    "correction": "La **Sauce Velouté** fait partie des sauces mères et est liée avec un **roux blanc** mouillé avec un fond (contrairement à la Béchamel, mouillée au lait)."
                },
                {
                    "questionNumber": 24,
                    "question": "Dans la technique de cuisson, que signifie 'Sauter' ?",
                    "answerOptions": [
                        {"text": "Cuire dans un liquide bouillant.", "isCorrect": False},
                        {"text": "Cuire rapidement de petites pièces (viande ou légume) à feu vif dans un peu de matière grasse.", "isCorrect": True},
                        {"text": "Cuire au four sans matière grasse.", "isCorrect": False},
                        {"text": "Cuire dans un plat fermé avec peu de liquide.", "isCorrect": False}
                    ],
                    "correction": "La cuisson **Sautée** est rapide. Elle donne une belle coloration (réaction de Maillard) en surface tout en gardant l'intérieur moelleux."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment s'appelle l'opération qui consiste à éliminer l'excès de sel et à raidir (blanchir) des légumes verts avant une cuisson finale ?",
                    "answerOptions": [
                        {"text": "La Brider.", "isCorrect": False},
                        {"text": "Le Blanchiment (ou 'blutage').", "isCorrect": True},
                        {"text": "Le Clarifier.", "isCorrect": False},
                        {"text": "L'Étuver.", "isCorrect": False}
                    ],
                    "correction": "Le **Blanchiment** peut se faire à l'eau froide (pour les légumes racines) ou à l'eau bouillante (pour les légumes verts) pour raidir la chlorophylle et enlever l'amertume ou l'excès de sel."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel ingrédient permet de 'Monter' une sauce Hollandaise (émulsion chaude) ?",
                    "answerOptions": [
                        {"text": "La Crème fraîche.", "isCorrect": False},
                        {"text": "Le Roux.", "isCorrect": False},
                        {"text": "Le Beurre clarifié (par émulsion avec les jaunes d'œufs).", "isCorrect": True},
                        {"text": "L'Eau.", "isCorrect": False}
                    ],
                    "correction": "La **Sauce Hollandaise** est une émulsion stable réalisée en incorporant progressivement du **beurre clarifié** chaud dans des jaunes d'œufs légèrement cuits (au bain-marie)."
                },
                {
                    "questionNumber": 27,
                    "question": "Que signifie le terme 'Singer' une préparation ?",
                    "answerOptions": [
                        {"text": "Ajouter de la crème.", "isCorrect": False},
                        {"text": "Saupoudrer de farine la garniture aromatique d'un plat (type ragoût) avant d'ajouter le mouillement, pour lier la sauce.", "isCorrect": True},
                        {"text": "Passer au chinois.", "isCorrect": False},
                        {"text": "Couper finement.", "isCorrect": False}
                    ],
                    "correction": "**Singer** est une technique de liaison pour les ragoûts et braisés. La farine (roux) assure l'épaississement de la sauce pendant la cuisson lente."
                },
                {
                    "questionNumber": 28,
                    "question": "Qu'appelle-t-on le 'Fumet de poisson' ?",
                    "answerOptions": [
                        {"text": "Un bouillon de crustacés épicé.", "isCorrect": False},
                        {"text": "Un fond clair obtenu par cuisson des arêtes et parures de poissons maigres avec une garniture aromatique.", "isCorrect": True},
                        {"text": "Une sauce au vin blanc.", "isCorrect": False},
                        {"text": "L'odeur du poisson.", "isCorrect": False}
                    ],
                    "correction": "Le **Fumet** sert de base aux sauces pour poissons et doit cuire très peu de temps (max 20 minutes) pour éviter le goût d'amertume."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la principale différence entre la cuisson 'À l'étouffée' et la cuisson 'Braiser' ?",
                    "answerOptions": [
                        {"text": "L'étouffée est sans matière grasse, le braisé non.", "isCorrect": False},
                        {"text": "Le braisé est une cuisson en deux étapes (saisir puis mijoter) pour les grosses pièces, tandis que l'étouffée est une cuisson lente à couvert avec très peu d'eau pour les légumes.", "isCorrect": True},
                        {"text": "Le braisé se fait à sec, l'étouffée avec beaucoup d'eau.", "isCorrect": False},
                        {"text": "Il n'y a aucune différence.", "isCorrect": False}
                    ],
                    "correction": "Le **Braisé** commence par la coloration du produit. L'**Étouffée** se fait sans coloration, avec peu de matière grasse et une cuisson très douce et longue."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est l'outil indispensable pour 'Passer' un fond pour le clarifier et enlever toutes les impuretés ?",
                    "answerOptions": [
                        {"text": "La Louche.", "isCorrect": False},
                        {"text": "Le Couteau d'office.", "isCorrect": False},
                        {"text": "Le Chinois ou la Passoire fine.", "isCorrect": True},
                        {"text": "Le Fouet.", "isCorrect": False}
                    ],
                    "correction": "Le **Chinois** (souvent doublé d'une étamine ou d'un linge) permet de filtrer le fond pour le rendre limpide."
                },
                {
                    "questionNumber": 31,
                    "question": "Que signifie le terme 'Chemiser' un moule ?",
                    "answerOptions": [
                        {"text": "Le remplir à ras bord.", "isCorrect": False},
                        {"text": "Tapisser le fond et les parois du moule d'un ingrédient (ex : gelée, papier sulfurisé, beurre, farine).", "isCorrect": True},
                        {"text": "Le laisser refroidir.", "isCorrect": False},
                        {"text": "Le faire cuire au bain-marie.", "isCorrect": False}
                    ],
                    "correction": "**Chemiser** permet soit de faciliter le démoulage, soit d'assurer une étanchéité (ex: chemiser de papier sulfurisé pour un gâteau) ou une décoration."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le nom de la coupe en fines lanières de 4 à 5 cm de long, utilisée pour les garnitures des potages ou les salades ?",
                    "answerOptions": [
                        {"text": "La Macédoine.", "isCorrect": False},
                        {"text": "La Ciseler.", "isCorrect": False},
                        {"text": "La Julienne.", "isCorrect": True},
                        {"text": "Le Paysanne.", "isCorrect": False}
                    ],
                    "correction": "La **Julienne** est la coupe en bâtonnets fins."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est l'opération qui consiste à mouiller un plat (ex : rôti) avec son propre jus de cuisson pour l'empêcher de sécher ?",
                    "answerOptions": [
                        {"text": "Le Saisir.", "isCorrect": False},
                        {"text": "L'Arroser (ou 'napper').", "isCorrect": True},
                        {"text": "Le Décanter.", "isCorrect": False},
                        {"text": "Le Monter au beurre.", "isCorrect": False}
                    ],
                    "correction": "L'**Arrosage** est essentiel pour le rôtissage, notamment des volailles, pour maintenir la viande moelleuse et obtenir une croûte uniforme."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel ingrédient principal ajoute-t-on à un fond pour obtenir un 'Consommé' ?",
                    "answerOptions": [
                        {"text": "De la crème.", "isCorrect": False},
                        {"text": "De l'eau.", "isCorrect": False},
                        {"text": "Une clarification à base de viande hachée, de blanc d'œuf et de mirepoix.", "isCorrect": True},
                        {"text": "Du roux brun.", "isCorrect": False}
                    ],
                    "correction": "Le **Consommé** est un bouillon limpide. La **clarification** ('la clarification à la russe') retire les impuretés en formant une 'radeau' qui est ensuite retiré."
                },
                {
                    "questionNumber": 35,
                    "question": "Que signifie 'Dégorger' un aliment (ex : concombres, rognons) ?",
                    "answerOptions": [
                        {"text": "Le faire frire.", "isCorrect": False},
                        {"text": "Le faire tremper ou rincer pour retirer l'excès de sang, d'amertume ou de saleté.", "isCorrect": True},
                        {"text": "Le mettre au four.", "isCorrect": False},
                        {"text": "Le couper en dés.", "isCorrect": False}
                    ],
                    "correction": "**Dégorger** améliore la qualité gustative (rognons : enlever le sang ; concombres : enlever l'eau et l'amertume)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quelle est la coupe de légume en petits cubes de 0,5 cm x 0,5 cm x 0,5 cm, principalement utilisée pour la garniture des potages ?",
                    "answerOptions": [
                        {"text": "La Brunoise.", "isCorrect": False},
                        {"text": "La Macédoine.", "isCorrect": True},
                        {"text": "Le Ciseler.", "isCorrect": False},
                        {"text": "L'Émincer.", "isCorrect": False}
                    ],
                    "correction": "La **Macédoine** est la coupe de légume classique en petits cubes."
                },
                {
                    "questionNumber": 37,
                    "question": "Dans le cas d'une cuisson au four, à quelle technique correspond l'ajout d'un corps gras et d'un peu d'eau en cocotte fermée pour un mijotage long ?",
                    "answerOptions": [
                        {"text": "Rôtir.", "isCorrect": False},
                        {"text": "Braiser.", "isCorrect": True},
                        {"text": "Griller.", "isCorrect": False},
                        {"text": "Frire.", "isCorrect": False}
                    ],
                    "correction": "Le **Braisage** est une cuisson longue, humide et douce, idéale pour les morceaux de viande qui ont besoin de temps pour s'attendrir (ex : bœuf bourguignon)."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel terme désigne l'action de faire fondre du sucre sans ajout d'eau, jusqu'à l'obtention d'une couleur ambrée ?",
                    "answerOptions": [
                        {"text": "Le Napper.", "isCorrect": False},
                        {"text": "Le Clarifier.", "isCorrect": False},
                        {"text": "Le Caramel (caraméliser à sec).", "isCorrect": True},
                        {"text": "Le Tremper.", "isCorrect": False}
                    ],
                    "correction": "Le **Caramel à sec** est le plus délicat à réaliser. Le caramel mouillé (avec eau) est plus facile, mais plus long."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle est la garniture aromatique traditionnelle et la plus simple pour la réalisation d'un fond ou d'une sauce (base d'oignons, carottes, céleri) ?",
                    "answerOptions": [
                        {"text": "L'Assaisonnement.", "isCorrect": False},
                        {"text": "La Mirepoix (ou Tailler).", "isCorrect": True},
                        {"text": "Le bouquet garni.", "isCorrect": False},
                        {"text": "Le Tailler en sifflet.", "isCorrect": False}
                    ],
                    "correction": "La **Mirepoix** est une garniture de base taillée en cubes (entre 1 et 2 cm) qui sert à parfumer bouillons et sauces."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment appelle-t-on le procédé qui consiste à retirer la graisse ou l'écume qui remonte à la surface d'un bouillon ou d'une sauce chaude ?",
                    "answerOptions": [
                        {"text": "Le Dégraisser (ou Écumer).", "isCorrect": True},
                        {"text": "Le Larder.", "isCorrect": False},
                        {"text": "Le Monder.", "isCorrect": False},
                        {"text": "Le Chinoiser.", "isCorrect": False}
                    ],
                    "correction": "**Dégraisser** et **écumer** sont des gestes essentiels pour obtenir des bouillons et des sauces limpides et légers."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : PRODUITS ET TRANSFORMATION (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Produits et Transformation (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le seul ingrédient qui n'est pas utilisé dans une 'Matignon' (garniture aromatique améliorée) ?",
                    "answerOptions": [
                        {"text": "L'oignon.", "isCorrect": False},
                        {"text": "Le jambon cru.", "isCorrect": True},
                        {"text": "Le céleri-rave.", "isCorrect": False},
                        {"text": "Le poireau.", "isCorrect": False}
                    ],
                    "correction": "La **Matignon** est une mirepoix améliorée (carottes, oignons, céleri, poireaux, champignon) avec adjonction de **jambon cru (ou gras)**, cuite au beurre sans coloration."
                },
                {
                    "questionNumber": 42,
                    "question": "Qu'est-ce qu'une 'Duxelles' ?",
                    "answerOptions": [
                        {"text": "Une sauce au vin blanc.", "isCorrect": False},
                        {"text": "Une purée de légumes.", "isCorrect": False},
                        {"text": "Une préparation à base de champignons de Paris finement hachés (ciselés) et étuvés au beurre avec des échalotes.", "isCorrect": True},
                        {"text": "Une coupe de légumes.", "isCorrect": False}
                    ],
                    "correction": "La **Duxelles** sert de base à de nombreuses farces et garnitures."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel nom porte le fait d'enlever les arêtes d'un poisson (ex : un filet) ?",
                    "answerOptions": [
                        {"text": "Le Parage.", "isCorrect": False},
                        {"text": "L'Ébarbage.", "isCorrect": False},
                        {"text": "Le Désarêtage (ou épinage).", "isCorrect": True},
                        {"text": "L'Écaillage.", "isCorrect": False}
                    ],
                    "correction": "Le **Désarêtage** s'effectue avec une pince à désarêter."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la classification de l'œuf (Poids minimum en grammes) le plus couramment utilisé en cuisine professionnelle pour les recettes (Œuf moyen) ?",
                    "answerOptions": [
                        {"text": "Calibre S (moins de 53 g).", "isCorrect": False},
                        {"text": "Calibre M (entre 53 et 63 g).", "isCorrect": True},
                        {"text": "Calibre L (entre 63 et 73 g).", "isCorrect": False},
                        {"text": "Calibre XL (plus de 73 g).", "isCorrect": False}
                    ],
                    "correction": "Le **Calibre M** est la référence pour les recettes et les conversions en pâtisserie."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment appelle-t-on le fait de frotter la viande avec un mélange d'aromates, d'épices et de sel avant cuisson ?",
                    "answerOptions": [
                        {"text": "Le Déglacer.", "isCorrect": False},
                        {"text": "Le Farcir.", "isCorrect": False},
                        {"text": "Le Rub (ou Frotter).", "isCorrect": True},
                        {"text": "Le Monder.", "isCorrect": False}
                    ],
                    "correction": "Le **Rub** (terme souvent utilisé pour le barbecue/rôtissage) crée une croûte aromatique et assaisonne la viande en profondeur."
                },
                {
                    "questionNumber": 46,
                    "question": "Quel est le nom de l'abat blanc le plus noble, provenant de la glande thymique du veau ou de l'agneau ?",
                    "answerOptions": [
                        {"text": "La Cervelle.", "isCorrect": False},
                        {"text": "La Ris de veau.", "isCorrect": True},
                        {"text": "Les Rognons.", "isCorrect": False},
                        {"text": "La Langue.", "isCorrect": False}
                    ],
                    "correction": "Le **Ris de veau** est un abat très délicat, qui nécessite un dégorgetage, un blanchiment (pour le raffermir) et un pressage avant cuisson."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel type de cuisson est le plus adapté pour une 'Noix de Saint-Jacques' ?",
                    "answerOptions": [
                        {"text": "Braiser.", "isCorrect": False},
                        {"text": "Poêler ou Griller (cuisson rapide à feu vif).", "isCorrect": True},
                        {"text": "Cuire au bouillon pendant 2 heures.", "isCorrect": False},
                        {"text": "Frire à basse température.", "isCorrect": False}
                    ],
                    "correction": "Les produits de la mer délicats nécessitent une **cuisson rapide** pour éviter qu'ils ne se dessèchent ou ne deviennent caoutchouteux."
                },
                {
                    "questionNumber": 48,
                    "question": "Que signifie 'Monder' un fruit ou un légume (ex : tomate, amande) ?",
                    "answerOptions": [
                        {"text": "Le congeler.", "isCorrect": False},
                        {"text": "Retirer sa peau après un bref passage dans l'eau bouillante (blanchiment) puis dans l'eau glacée.", "isCorrect": True},
                        {"text": "Le couper en dés.", "isCorrect": False},
                        {"text": "Le cuire au four.", "isCorrect": False}
                    ],
                    "correction": "**Monder** est essentiel pour certaines préparations, notamment pour les sauces tomates ou les purées très fines."
                },
                {
                    "questionNumber": 49,
                    "question": "Quelle technique est utilisée pour maintenir la forme d'un rôti ou d'une volaille farcie pendant la cuisson ?",
                    "answerOptions": [
                        {"text": "Le Trancher.", "isCorrect": False},
                        {"text": "Le Farcir.", "isCorrect": False},
                        {"text": "Le Brider.", "isCorrect": True},
                        {"text": "Le Dégorger.", "isCorrect": False}
                    ],
                    "correction": "**Brider** consiste à lier la pièce avec de la ficelle de cuisine."
                },
                {
                    "questionNumber": 50,
                    "question": "Parmi ces produits, lequel fait partie des 14 allergènes majeurs ?",
                    "answerOptions": [
                        {"text": "L'ail.", "isCorrect": False},
                        {"text": "Le céleri (et les produits à base de céleri).", "isCorrect": True},
                        {"text": "Le persil.", "isCorrect": False},
                        {"text": "La pomme de terre.", "isCorrect": False}
                    ],
                    "correction": "Le **Céleri** (racine, branche, ou même les graines) fait partie des allergènes majeurs devant être signalés."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le risque de surcuisson d'un jaune d'œuf lors d'une liaison (ex : sauce à la crème) ?",
                    "answerOptions": [
                        {"text": "Le jaune d'œuf perd sa couleur.", "isCorrect": False},
                        {"text": "Le jaune d'œuf coagule et la sauce 'graisse' (devient granuleuse).", "isCorrect": True},
                        {"text": "La sauce devient trop liquide.", "isCorrect": False},
                        {"text": "Le jaune d'œuf ne change pas.", "isCorrect": False}
                    ],
                    "correction": "Les jaunes d'œufs ne doivent jamais bouillir. La liaison doit se faire **hors du feu** ou au bain-marie, et la température ne doit pas dépasser 83°C."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le nom de la coupe en quartiers utilisée pour les pommes de terre (ex : rôties) ?",
                    "answerOptions": [
                        {"text": "La Macédoine.", "isCorrect": False},
                        {"text": "Le Pont-neuf.", "isCorrect": False},
                        {"text": "Les Quartiers (ou Gaufrettes).", "isCorrect": True},
                        {"text": "La Parisienne.", "isCorrect": False}
                    ],
                    "correction": "Les pommes de terre coupées en **quartiers** sont souvent blanchies avant d'être rôties."
                },
                {
                    "questionNumber": 53,
                    "question": "Que signifie 'Dresser' une assiette ?",
                    "answerOptions": [
                        {"text": "La chauffer.", "isCorrect": False},
                        {"text": "Disposer les différents éléments du plat sur l'assiette avec soin et esthétique avant l'envoi.", "isCorrect": True},
                        {"text": "La décorer avec des fleurs.", "isCorrect": False},
                        {"text": "La laver.", "isCorrect": False}
                    ],
                    "correction": "Le **Dressage** est l'étape finale où le cuisinier valorise son travail (esthétique, équilibre des couleurs et des volumes)."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel liquide est utilisé pour 'Mouiller' un fond blanc de volaille ?",
                    "answerOptions": [
                        {"text": "De l'huile d'olive.", "isCorrect": False},
                        {"text": "De l'eau froide.", "isCorrect": True},
                        {"text": "Du vin rouge.", "isCorrect": False},
                        {"text": "Du lait.", "isCorrect": False}
                    ],
                    "correction": "Le **Mouillement** doit toujours se faire à l'**eau froide** pour les fonds, car cela permet aux impuretés de remonter à la surface (écume) et d'obtenir un fond clair."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est la principale fonction du 'Beurre manié' ?",
                    "answerOptions": [
                        {"text": "Faire frire des légumes.", "isCorrect": False},
                        {"text": "Épaissir rapidement une sauce ou un potage en fin de cuisson.", "isCorrect": True},
                        {"text": "Monter une mayonnaise.", "isCorrect": False},
                        {"text": "Donner du goût de noisette.", "isCorrect": False}
                    ],
                    "correction": "Le **Beurre manié** (mélange de beurre et de farine à parts égales) est ajouté froid dans le liquide chaud pour lier rapidement et sans grumeaux."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment appelle-t-on la technique qui consiste à faire suer un oignon coupé finement dans du beurre sans coloration ?",
                    "answerOptions": [
                        {"text": "Le Glacer à blanc.", "isCorrect": True},
                        {"text": "Le Déglacer.", "isCorrect": False},
                        {"text": "Le Clarifier.", "isCorrect": False},
                        {"text": "Le Paner.", "isCorrect": False}
                    ],
                    "correction": "**Glacer à blanc** permet d'attendrir la garniture aromatique pour qu'elle puisse transmettre son goût sans donner de couleur au fond ou à la sauce."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est l'élément qui permet de 'Napper' un potage ou une sauce d'une couche fine et uniforme ?",
                    "answerOptions": [
                        {"text": "La Crépine.", "isCorrect": False},
                        {"text": "La spatule (ou la cuillère) pour vérifier la consistance du nappage (le liquide doit coller à l'outil).", "isCorrect": True},
                        {"text": "Le couteau à parer.", "isCorrect": False},
                        {"text": "La maryse.", "isCorrect": False}
                    ],
                    "correction": "Le test du **nappage** est crucial. La sauce est prête lorsque, en passant le doigt sur la spatule, la trace reste nette."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle coupe de légumes est indispensable pour la cuisson des frites (gros bâtonnets réguliers) ?",
                    "answerOptions": [
                        {"text": "La Macédoine.", "isCorrect": False},
                        {"text": "Le Pont-neuf.", "isCorrect": True},
                        {"text": "L'Allumette.", "isCorrect": False},
                        {"text": "La Mirepoix.", "isCorrect": False}
                    ],
                    "correction": "Le **Pont-neuf** (environ 1 cm x 1 cm x 7 cm) est la coupe traditionnelle de la frite, souvent cuite en deux bains : un blanchiment puis une coloration."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel terme désigne la peau de certains légumes ou fruits retirée à vif (ex : agrumes) ?",
                    "answerOptions": [
                        {"text": "Le Zeste.", "isCorrect": False},
                        {"text": "Le Peler à vif.", "isCorrect": True},
                        {"text": "Le Dégraisser.", "isCorrect": False},
                        {"text": "L'Ébarber.", "isCorrect": False}
                    ],
                    "correction": "**Peler à vif** consiste à retirer l'écorce et la peau blanche (amère) des agrumes pour ne garder que la chair."
                },
                {
                    "questionNumber": 60,
                    "question": "Qu'est-ce qu'une 'Crêpine' en cuisine ?",
                    "answerOptions": [
                        {"text": "Un type de crêpe.", "isCorrect": False},
                        {"text": "Une fine membrane graisseuse qui entoure l'estomac du porc ou du mouton, utilisée pour envelopper les farces (ex : crépinettes).", "isCorrect": True},
                        {"text": "Un filtre en métal.", "isCorrect": False},
                        {"text": "Un ustensile de pâtisserie.", "isCorrect": False}
                    ],
                    "correction": "La **Crêpine** est utilisée pour maintenir la forme d'une farce ou d'une préparation avant cuisson."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : PÂTISSERIE ET DESSERTS DE RESTAURANT (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Pâtisserie et Desserts de Restaurant (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la crème de base utilisée pour garnir un éclair ou un millefeuille ?",
                    "answerOptions": [
                        {"text": "La Crème Chantilly.", "isCorrect": False},
                        {"text": "La Crème Anglaise.", "isCorrect": False},
                        {"text": "La Crème Pâtissière.", "isCorrect": True},
                        {"text": "La Crème Fouettée.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Pâtissière** est le socle de nombreuses autres crèmes (Crème Diplomate, Crème Mousseline) et la garniture classique des entremets."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la méthode de montage d'une Meringue Française ?",
                    "answerOptions": [
                        {"text": "Battre les blancs d'œufs avec un sirop chaud (118°C).", "isCorrect": False},
                        {"text": "Battre les blancs d'œufs froids en incorporant du sucre semoule en poudre progressivement.", "isCorrect": True},
                        {"text": "Battre les jaunes d'œufs.", "isCorrect": False},
                        {"text": "Fouetter sur bain-marie.", "isCorrect": False}
                    ],
                    "correction": "La **Meringue Française** est la plus simple et la plus friable. Elle ne nécessite pas de cuisson des blancs au sirop ou au bain-marie."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est l'ingrédient indispensable pour donner sa texture élastique à la 'Pâte à Choux' ?",
                    "answerOptions": [
                        {"text": "La Levure de boulanger.", "isCorrect": False},
                        {"text": "Les œufs (incorporés hors du feu).", "isCorrect": True},
                        {"text": "Le miel.", "isCorrect": False},
                        {"text": "Le sucre glace.", "isCorrect": False}
                    ],
                    "correction": "L'**œuf** permet au chou de gonfler (par l'évaporation de l'eau) en formant une croûte souple et creuse."
                },
                {
                    "questionNumber": 64,
                    "question": "Que signifie 'Abaisser' une pâte ?",
                    "answerOptions": [
                        {"text": "La faire cuire au four.", "isCorrect": False},
                        {"text": "L'étaler à l'aide d'un rouleau à pâtisserie pour lui donner l'épaisseur souhaitée.", "isCorrect": True},
                        {"text": "La mélanger rapidement.", "isCorrect": False},
                        {"text": "La faire lever.", "isCorrect": False}
                    ],
                    "correction": "**Abaisser** est un terme très utilisé pour les pâtes (feuilletée, brisée, sablée)."
                },
                {
                    "questionNumber": 65,
                    "question": "Comment appelle-t-on l'appareil obtenu par mélange d'une Crème Pâtissière et d'une Meringue Italienne ?",
                    "answerOptions": [
                        {"text": "La Crème Anglaise.", "isCorrect": False},
                        {"text": "La Crème Saint-Honoré (ou Crème Chiboust).", "isCorrect": True},
                        {"text": "La Crème Chantilly.", "isCorrect": False},
                        {"text": "La Crème Mousseline.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Chiboust** est légère et aérée. Elle est notamment utilisée pour la garniture du Saint-Honoré."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est l'ingrédient ajouté à la Crème Pâtissière pour obtenir une 'Crème Mousseline' ?",
                    "answerOptions": [
                        {"text": "De la gélatine.", "isCorrect": False},
                        {"text": "Du beurre pommade (incorporé après refroidissement).", "isCorrect": True},
                        {"text": "De la crème fouettée.", "isCorrect": False},
                        {"text": "Du jus de citron.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Mousseline** est une crème pâtissière foisonnée (mélangée au fouet) avec du beurre."
                },
                {
                    "questionNumber": 67,
                    "question": "Quelle est la principale caractéristique de la 'Pâte Brisée' ?",
                    "answerOptions": [
                        {"text": "Elle est très aérée.", "isCorrect": False},
                        {"text": "Elle est facile à travailler et utilisée pour les tartes salées ou quiches.", "isCorrect": True},
                        {"text": "Elle feuillette à la cuisson.", "isCorrect": False},
                        {"text": "Elle est très sucrée.", "isCorrect": False}
                    ],
                    "correction": "La **Pâte Brisée** est neutre et a peu d'élasticité (pas de temps de repos comme la pâte à pain), elle est 'brisée' par le corps gras."
                },
                {
                    "questionNumber": 68,
                    "question": "Que signifie 'Foncer' un moule ?",
                    "answerOptions": [
                        {"text": "Le démouler.", "isCorrect": False},
                        {"text": "Garnir le fond et les bords du moule avec une pâte (ex : brisée, sablée).", "isCorrect": True},
                        {"text": "Le laver à l'eau très chaude.", "isCorrect": False},
                        {"text": "Le dorer à l'œuf.", "isCorrect": False}
                    ],
                    "correction": "**Foncer** permet de donner la forme finale à la pâte avant la garniture ou la cuisson à blanc."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est l'ingrédient qui permet de 'Coller' un entremets (lui donner de la tenue) ?",
                    "answerOptions": [
                        {"text": "Le Sucre.", "isCorrect": False},
                        {"text": "Le Chocolat.", "isCorrect": False},
                        {"text": "La Gélatine ou l'Agar-agar.", "isCorrect": True},
                        {"text": "Le Beurre.", "isCorrect": False}
                    ],
                    "correction": "La **Gélatine** (d'origine animale) ou l'**Agar-agar** (végétal) sont des gélifiants (ou 'colle') utilisés pour donner de la structure aux mousses, bavarois, et entremets."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment appelle-t-on la technique qui consiste à faire cuire une pâte à tarte seule, sans garniture, pour la faire croustiller ?",
                    "answerOptions": [
                        {"text": "La Cuisson lente.", "isCorrect": False},
                        {"text": "La Cuisson à blanc.", "isCorrect": True},
                        {"text": "La Cuisson à sec.", "isCorrect": False},
                        {"text": "La Cuisson à la vapeur.", "isCorrect": False}
                    ],
                    "correction": "La **Cuisson à blanc** se fait souvent en remplissant le fond de tarte de légumes secs ou de billes de cuisson (pour éviter que la pâte ne gonfle)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est le nom de la base d'une crème glacée ou d'un bavarois ?",
                    "answerOptions": [
                        {"text": "Le Roux.", "isCorrect": False},
                        {"text": "La Crème Anglaise (qui coagule à 83°C).", "isCorrect": True},
                        {"text": "Le Beurre noisette.", "isCorrect": False},
                        {"text": "La Pâte à tempérer.", "isCorrect": False}
                    ],
                    "correction": "La **Crème Anglaise** (jaunes d'œufs et sucre blanchis, mouillés au lait chaud) est la base classique des appareils à glacer."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel terme désigne l'action de décorer un plat (souvent avec du sucre glace ou des épices) en le saupoudrant légèrement ?",
                    "answerOptions": [
                        {"text": "Le Pincer.", "isCorrect": False},
                        {"text": "Le Fleurer.", "isCorrect": True},
                        {"text": "Le Masquer.", "isCorrect": False},
                        {"text": "Le Larder.", "isCorrect": False}
                    ],
                    "correction": "**Fleurer** (en boulangerie, c'est aussi fariner le plan de travail) est un geste de finition."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la principale fonction du 'Tours' dans la réalisation d'une Pâte Feuilletée ?",
                    "answerOptions": [
                        {"text": "Ajouter du goût.", "isCorrect": False},
                        {"text": "Créer de fines couches successives (détrempe/beurre/détrempe) pour qu'elle lève et feuillette à la cuisson.", "isCorrect": True},
                        {"text": "Rendre la pâte plus sucrée.", "isCorrect": False},
                        {"text": "La rendre plus élastique.", "isCorrect": False}
                    ],
                    "correction": "Un **tour** est une étape d'étalage-pliage. La pâte feuilletée classique nécessite 6 tours simples (ou 4 tours doubles) pour avoir des milliers de feuillets."
                },
                {
                    "questionNumber": 74,
                    "question": "Qu'est-ce qu'une 'Ganache' ?",
                    "answerOptions": [
                        {"text": "Un type de sucre.", "isCorrect": False},
                        {"text": "Une émulsion à base de crème liquide bouillante et de chocolat, utilisée pour les truffes ou les intérieurs de gâteaux.", "isCorrect": True},
                        {"text": "Une pâte à tarte.", "isCorrect": False},
                        {"text": "Un glaçage pour éclair.", "isCorrect": False}
                    ],
                    "correction": "La **Ganache** est une base essentielle de la chocolaterie, qui peut être montée ou coulée."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le risque si l'on incorpore des œufs froids dans une crème chaude ?",
                    "answerOptions": [
                        {"text": "La crème devient trop sucrée.", "isCorrect": False},
                        {"text": "Les œufs vont 'cuire' instantanément (choc thermique) et créer des grumeaux (la crème 'graisse').", "isCorrect": True},
                        {"text": "La crème ne cuit pas.", "isCorrect": False},
                        {"text": "La crème devient plus liquide.", "isCorrect": False}
                    ],
                    "correction": "Pour éviter le choc thermique, il faut toujours **tempérer** les œufs (ou les jaunes) en ajoutant une petite quantité de crème chaude avant de tout mélanger (délayer/blanchir)."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le type de meringue qui se réalise en incorporant un sirop de sucre cuit à 118°C dans les blancs montés en neige ?",
                    "answerOptions": [
                        {"text": "Meringue Française.", "isCorrect": False},
                        {"text": "Meringue Suisse.", "isCorrect": False},
                        {"text": "Meringue Italienne.", "isCorrect": True},
                        {"text": "Meringue Royale.", "isCorrect": False}
                    ],
                    "correction": "La **Meringue Italienne** est la plus stable et la plus brillante. Elle est souvent utilisée pour les décors (tarte au citron) et les appareils à bombe."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel ingrédient est essentiel dans la fabrication d'une 'Pâte Sablée' (pâte 'cassante') ?",
                    "answerOptions": [
                        {"text": "Beaucoup d'eau.", "isCorrect": False},
                        {"text": "La Levure.", "isCorrect": False},
                        {"text": "Le beurre froid 'sablé' avec la farine (mélange de sablage).", "isCorrect": True},
                        {"text": "Le lait.", "isCorrect": False}
                    ],
                    "correction": "Le **sablage** (mélange de farine et de beurre qui ressemble à du sable) empêche la formation d'un réseau glutineux élastique, rendant la pâte friable."
                },
                {
                    "questionNumber": 78,
                    "question": "Qu'est-ce qu'une 'Température de cristallisation' pour le chocolat ?",
                    "answerOptions": [
                        {"text": "La température de fusion du chocolat.", "isCorrect": False},
                        {"text": "La température idéale pour que les cristaux de beurre de cacao se forment de manière stable (le 'tempérage').", "isCorrect": True},
                        {"text": "La température de cuisson du chocolat.", "isCorrect": False},
                        {"text": "La température de conservation du chocolat.", "isCorrect": False}
                    ],
                    "correction": "Le **Tempérage** (chocolat noir : 31-32°C) donne au chocolat sa brillance et son croquant."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le nom de la technique qui consiste à faire de petits trous dans le fond d'une pâte à tarte crue pour éviter qu'elle ne gonfle à la cuisson ?",
                    "answerOptions": [
                        {"text": "Le Foncer.", "isCorrect": False},
                        {"text": "Le Piquer.", "isCorrect": True},
                        {"text": "Le Fleurir.", "isCorrect": False},
                        {"text": "Le Masquer.", "isCorrect": False}
                    ],
                    "correction": "**Piquer** permet à la vapeur d'eau de s'échapper, évitant ainsi la formation de bulles."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment appelle-t-on le fait de mélanger une pâte ou un appareil délicat avec une spatule sans le faire retomber ?",
                    "answerOptions": [
                        {"text": "Le Fouetter énergiquement.", "isCorrect": False},
                        {"text": "Le Corner.", "isCorrect": False},
                        {"text": "L'Incorporer (ou Mélanger délicatement).", "isCorrect": True},
                        {"text": "Le Saisir.", "isCorrect": False}
                    ],
                    "correction": "L'**Incorporation délicate** est essentielle pour les mousses, les soufflés, et la pâte à choux (lors de l'ajout des œufs)."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : GESTION, TERMINOLOGIE ET ORGANISATION (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Gestion, Terminologie et Organisation (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Dans le calcul des coûts, que représente le 'Coefficient multiplicateur' ?",
                    "answerOptions": [
                        {"text": "Le rendement d'un produit.", "isCorrect": False},
                        {"text": "Le ratio entre le prix de vente (HT) et le coût matière de la recette.", "isCorrect": True},
                        {"text": "Le taux de TVA.", "isCorrect": False},
                        {"text": "Le nombre de convives.", "isCorrect": False}
                    ],
                    "correction": "Le **Coefficient multiplicateur** permet de fixer le prix de vente du plat en fonction du coût de ses ingrédients et de la marge souhaitée."
                },
                {
                    "questionNumber": 82,
                    "question": "Que signifie le terme 'Remettre en température' (ou Remise en chauffe) dans le cadre des plats préparés à l'avance ?",
                    "answerOptions": [
                        {"text": "Le mettre au froid.", "isCorrect": False},
                        {"text": "Atteindre au moins +63°C à cœur au moment de l'envoi.", "isCorrect": True},
                        {"text": "Le laisser à température ambiante.", "isCorrect": False},
                        {"text": "Le congeler.", "isCorrect": False}
                    ],
                    "correction": "La **Remise en température** est une étape critique soumise à la réglementation HACCP pour éviter la zone de danger."
                },
                {
                    "questionNumber": 83,
                    "question": "Que désigne la 'Mise en place' ?",
                    "answerOptions": [
                        {"text": "Le dressage final de l'assiette.", "isCorrect": False},
                        {"text": "L'ensemble des opérations préliminaires (coupes, parures, fonds, sauces) effectuées avant le service.", "isCorrect": True},
                        {"text": "Le nettoyage de la cuisine.", "isCorrect": False},
                        {"text": "Le contrôle des températures.", "isCorrect": False}
                    ],
                    "correction": "La **Mise en place** ('Mis en place') est essentielle pour garantir l'efficacité et la rapidité pendant le coup de feu."
                },
                {
                    "questionNumber": 84,
                    "question": "Dans une brigade de cuisine, qui est le responsable de l'ensemble de la cuisine et de la gestion de la brigade ?",
                    "answerOptions": [
                        {"text": "Le Chef de partie.", "isCorrect": False},
                        {"text": "Le Commis de cuisine.", "isCorrect": False},
                        {"text": "Le Chef de cuisine (ou Chef Exécutif).", "isCorrect": True},
                        {"text": "Le Saucier.", "isCorrect": False}
                    ],
                    "correction": "Le **Chef de cuisine** est le chef d'orchestre, responsable de la carte, des coûts, de l'hygiène et du personnel."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le 'Rendement' d'un légume (ex : brocoli) ?",
                    "answerOptions": [
                        {"text": "Le temps de cuisson.", "isCorrect": False},
                        {"text": "La quantité de produit fini (paré et propre) que l'on obtient à partir du produit brut (la perte est le 'déchet').", "isCorrect": True},
                        {"text": "Le prix d'achat.", "isCorrect": False},
                        {"text": "Le nombre de portions obtenues.", "isCorrect": False}
                    ],
                    "correction": "Le **Rendement** est crucial pour le calcul du coût matière. Si un brocoli a un rendement de 70 %, 30 % du poids acheté est du déchet."
                },
                {
                    "questionNumber": 86,
                    "question": "Que signifie le terme 'Abattre la température' d'un aliment ?",
                    "answerOptions": [
                        {"text": "Le cuire.", "isCorrect": False},
                        {"text": "Le faire refroidir très rapidement (en moins de 2 heures) à l'aide d'une cellule de refroidissement.", "isCorrect": True},
                        {"text": "Le décongeler.", "isCorrect": False},
                        {"text": "Le laisser à température ambiante.", "isCorrect": False}
                    ],
                    "correction": "L'**Abaissement de température** est une obligation HACCP pour les préparations stockées."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel terme désigne l'action de faire évaporer l'excès de liquide d'un potage ou d'une sauce en le faisant bouillir doucement pour concentrer les saveurs ?",
                    "answerOptions": [
                        {"text": "Le Chinoiser.", "isCorrect": False},
                        {"text": "Le Réduire.", "isCorrect": True},
                        {"text": "Le Blanchir.", "isCorrect": False},
                        {"text": "Le Marquer.", "isCorrect": False}
                    ],
                    "correction": "Une **Réduction** permet d'obtenir une sauce plus épaisse et plus goûteuse."
                },
                {
                    "questionNumber": 88,
                    "question": "Qu'est-ce qu'un 'Bon de commande' ?",
                    "answerOptions": [
                        {"text": "La liste des plats vendus.", "isCorrect": False},
                        {"text": "Le document qui liste précisément les quantités de denrées nécessaires commandées au fournisseur.", "isCorrect": True},
                        {"text": "La recette d'un plat.", "isCorrect": False},
                        {"text": "Le document de livraison.", "isCorrect": False}
                    ],
                    "correction": "Le **Bon de commande** est la base de la relation avec le fournisseur et est utilisé pour le contrôle à la réception."
                },
                {
                    "questionNumber": 89,
                    "question": "Comment appelle-t-on la technique qui consiste à faire brunir la surface de certains aliments à l'aide d'un fer chaud (marque) ou d'une salamandre ?",
                    "answerOptions": [
                        {"text": "Le Déglacer.", "isCorrect": False},
                        {"text": "Le Marquer.", "isCorrect": True},
                        {"text": "Le Dégraisser.", "isCorrect": False},
                        {"text": "L'Émulsionner.", "isCorrect": False}
                    ],
                    "correction": "**Marquer** est souvent utilisé pour des cuissons rapides (grillade, poêlée) pour donner une belle coloration."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le rôle du 'Saucier' dans une grande brigade de cuisine ?",
                    "answerOptions": [
                        {"text": "Couper les légumes.", "isCorrect": False},
                        {"text": "Responsable des sauces chaudes, des rôtis et des plats mijotés.", "isCorrect": True},
                        {"text": "Responsable de la plonge.", "isCorrect": False},
                        {"text": "Responsable de la pâtisserie.", "isCorrect": False}
                    ],
                    "correction": "Le **Saucier** (Chef de Partie) est un des postes les plus importants et techniques. Il nécessite une grande précision."
                },
                {
                    "questionNumber": 91,
                    "question": "Que signifie 'Dégorger' un récipient (ex : glace) ?",
                    "answerOptions": [
                        {"text": "Le remplir.", "isCorrect": False},
                        {"text": "Le vider complètement (souvent pour la plonge) avant l'étape de lavage.", "isCorrect": True},
                        {"text": "Le faire sécher.", "isCorrect": False},
                        {"text": "Le laisser tremper.", "isCorrect": False}
                    ],
                    "correction": "**Dégorger** (vider l'excès de matière, de gras, de restes) est essentiel avant le lavage pour garantir l'efficacité des produits."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est l'outil utilisé pour déterminer le poids réel des ingrédients par rapport à la quantité commandée ?",
                    "answerOptions": [
                        {"text": "Le Chronomètre.", "isCorrect": False},
                        {"text": "La Balance de cuisine (avec étalonnage vérifié).", "isCorrect": True},
                        {"text": "Le Thermomètre.", "isCorrect": False},
                        {"text": "Le Mètre ruban.", "isCorrect": False}
                    ],
                    "correction": "La **Balance** est essentielle pour le respect des recettes (coût matière) et la vérification des livraisons."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment appelle-t-on le fait d'entourer une pièce de viande maigre (ex : filet de bœuf) d'une tranche de lard pour la protéger pendant la cuisson ?",
                    "answerOptions": [
                        {"text": "Le Piquer.", "isCorrect": False},
                        {"text": "Le Barder.", "isCorrect": True},
                        {"text": "Le Larder.", "isCorrect": False},
                        {"text": "Le Farcir.", "isCorrect": False}
                    ],
                    "correction": "**Barder** est une technique qui apporte du gras (goût et protection) aux viandes maigres."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le nom du plat cuisiné qui est 'Mis en évidence' (exposé) à la vente au buffet ou en vitrine ?",
                    "answerOptions": [
                        {"text": "Le Plat du jour.", "isCorrect": False},
                        {"text": "Le Plat témoin.", "isCorrect": True},
                        {"text": "Le Plat principal.", "isCorrect": False},
                        {"text": "Le Plat à emporter.", "isCorrect": False}
                    ],
                    "correction": "Le **Plat témoin** est conservé à l'abri et étiqueté. Il sert de preuve en cas de contrôle sanitaire ou d'intoxication (traçabilité)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la coupe de légume en petits rectangles plats (1-2 mm d'épaisseur), utilisée pour les potages dits 'Paysanne' ?",
                    "answerOptions": [
                        {"text": "La Macédoine.", "isCorrect": False},
                        {"text": "La Brunoise.", "isCorrect": False},
                        {"text": "La Paysanne.", "isCorrect": True},
                        {"text": "La Chiffonnade.", "isCorrect": False}
                    ],
                    "correction": "La **Paysanne** est une coupe rustique et rapide, adaptée à la cuisson en potage."
                },
                {
                    "questionNumber": 96,
                    "question": "Que représente la 'Fiche technique de production' ?",
                    "answerOptions": [
                        {"text": "La facture du fournisseur.", "isCorrect": False},
                        {"text": "Le document standardisé décrivant la recette, le temps de préparation, les coûts matières et le rendement d'un plat.", "isCorrect": True},
                        {"text": "Le bon de commande.", "isCorrect": False},
                        {"text": "Le plan de nettoyage.", "isCorrect": False}
                    ],
                    "correction": "La **Fiche technique** est l'outil de gestion central du Chef. Elle assure la qualité constante du plat et la maîtrise des coûts."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel terme désigne l'action de faire ramollir le beurre en le travaillant à température ambiante pour obtenir une texture crémeuse ?",
                    "answerOptions": [
                        {"text": "Le Clarifier.", "isCorrect": False},
                        {"text": "Le Pommader.", "isCorrect": True},
                        {"text": "Le Foisonner.", "isCorrect": False},
                        {"text": "Le Réduire.", "isCorrect": False}
                    ],
                    "correction": "**Pommader** est crucial pour la pâtisserie (pâte sablée, crèmes au beurre) pour garantir l'homogénéité du mélange."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le rôle du 'Tournant' (Chef de Partie Tournant) ?",
                    "answerOptions": [
                        {"text": "Remplacer le Chef de cuisine.", "isCorrect": False},
                        {"text": "Remplacer les Chefs de partie absents à n'importe quel poste (saucier, rôtisseur, entremétier, etc.).", "isCorrect": True},
                        {"text": "Travailler uniquement au poste des entrées.", "isCorrect": False},
                        {"text": "Faire la plonge.", "isCorrect": False}
                    ],
                    "correction": "Le **Tournant** est le poste le plus polyvalent, il doit maîtriser toutes les techniques de base pour pallier les absences."
                },
                {
                    "questionNumber": 99,
                    "question": "Que signifie 'Foisonner' un appareil ?",
                    "answerOptions": [
                        {"text": "Le chauffer rapidement.", "isCorrect": False},
                        {"text": "Incorporer un maximum d'air par fouettage pour augmenter son volume et le rendre mousseux (ex : crème fouettée, mousse).", "isCorrect": True},
                        {"text": "Le dégraisser.", "isCorrect": False},
                        {"text": "Le lier à l'amidon.", "isCorrect": False}
                    ],
                    "correction": "**Foisonner** est une technique essentielle des crèmes et des mousses. Ex : crème liquide froide qui passe de 35 % de matière grasse à une texture stable et aérée (Chantilly)."
                },
                {
                    "questionNumber": 100,
                    "question": "Dans le calcul des coûts, que doit-on déduire du prix d'achat brut pour obtenir le 'Coût matière réel' ?",
                    "answerOptions": [
                        {"text": "La TVA.", "isCorrect": False},
                        {"text": "Les déchets et les parures (en utilisant le coefficient de rendement).", "isCorrect": True},
                        {"text": "Le coût du personnel.", "isCorrect": False},
                        {"text": "Les frais généraux.", "isCorrect": False}
                    ],
                    "correction": "Le coût matière réel ne concerne que la **partie comestible** utilisée dans la recette (coût matière = prix d'achat brut / rendement)."
                },
            ]
        }
    }
}

# Exemple d'accès aux données :
# print(quiz_data["title"])
# print(quiz_data["themes"][1]["name"])
# print(quiz_data["themes"][1]["questions"][0]["question"])
# print(quiz_data["themes"][1]["questions"][0]["answerOptions"][2]["isCorrect"])