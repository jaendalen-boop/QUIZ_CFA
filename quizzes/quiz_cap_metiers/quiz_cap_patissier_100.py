quiz_data = {
    "title": "Quiz CAP Pâtissier : Technologie, Fabrication, Hygiène et Gestion (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : TECHNOLOGIE DES MATIÈRES PREMIÈRES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : TECHNOLOGIE DES MATIÈRES PREMIÈRES (Questions 1 à 20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel composant de la farine est responsable de l'élasticité de la pâte ?",
                    "answerOptions": [
                        {"text": "Les protéines constituant le gluten", "isCorrect": True},
                        {"text": "L'amidon", "isCorrect": False},
                        {"text": "L'eau", "isCorrect": False},
                        {"text": "Le son", "isCorrect": False}
                    ],
                    "correction": "Le gluten est un réseau élastique formé par l'hydratation de certaines protéines (gluténines et gliadines) lors du pétrissage."
                },
                {
                    "questionNumber": 2,
                    "question": "À quelle température le sucre atteint-il le stade du 'Grand Boulé' ?",
                    "answerOptions": [
                        {"text": "121°C", "isCorrect": True},
                        {"text": "Entre 116°C et 118°C environ", "isCorrect": False},
                        {"text": "Au stade de 145°C", "isCorrect": False},
                        {"text": "Dès 100°C", "isCorrect": False}
                    ],
                    "correction": "Le grand boulé (121°C) est le stade de cuisson classique pour la réalisation de la meringue italienne. Le petit boulé est à 118°C."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la matière grasse de référence en pâtisserie fine ?",
                    "answerOptions": [
                        {"text": "Le beurre", "isCorrect": True},
                        {"text": "La margarine de feuilletage enrichie", "isCorrect": False},
                        {"text": "Le saindoux", "isCorrect": False},
                        {"text": "Les huiles végétales hydrogénées", "isCorrect": False}
                    ],
                    "correction": "Le beurre offre des qualités gustatives inégalées et une plasticité idéale, bien que la margarine soit parfois utilisée pour des raisons économiques ou techniques."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel rôle joue le sel dans une pâte levée ?",
                    "answerOptions": [
                        {"text": "Il régule la fermentation et donne du corps", "isCorrect": True},
                        {"text": "Il accélère la levure", "isCorrect": False},
                        {"text": "Il colore la mie", "isCorrect": False},
                        {"text": "Il hydrate", "isCorrect": False}
                    ],
                    "correction": "Le sel a un rôle technologique majeur : il freine légèrement la levure (régulation), renforce le réseau de gluten (corps) et favorise la coloration de la croûte."
                },
                {
                    "questionNumber": 5,
                    "question": "Pour le feuilletage, on privilégie une farine :",
                    "answerOptions": [
                        {"text": "De force (Type 45)", "isCorrect": True},
                        {"text": "Complète (Type 150) riche en son", "isCorrect": False},
                        {"text": "De seigle", "isCorrect": False},
                        {"text": "Pauvre en gluten", "isCorrect": False}
                    ],
                    "correction": "Le feuilletage nécessite une pâte très élastique pour supporter les tours sans déchirer, d'où l'usage d'une farine riche en gluten (T45 de force ou de gruau)."
                },
                {
                    "questionNumber": 6,
                    "question": "La levure biologique est composée de :",
                    "answerOptions": [
                        {"text": "Champignons microscopiques vivants", "isCorrect": True},
                        {"text": "Poudre chimique", "isCorrect": False},
                        {"text": "Bactéries", "isCorrect": False},
                        {"text": "Sel acide", "isCorrect": False}
                    ],
                    "correction": "La levure de boulanger est un organisme vivant (Saccharomyces cerevisiae) qui fermente les sucres, contrairement à la levure chimique qui est un mélange minéral."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle partie de l'œuf permet l'émulsion ?",
                    "answerOptions": [
                        {"text": "Le jaune", "isCorrect": True},
                        {"text": "La totalité du blanc d'œuf", "isCorrect": False},
                        {"text": "La coquille", "isCorrect": False},
                        {"text": "Les membranes coquillières", "isCorrect": False}
                    ],
                    "correction": "Le jaune contient de la lécithine, un tensioactif naturel qui permet de lier l'eau et le gras (émulsion), indispensable pour les crèmes et les sauces."
                },
                {
                    "questionNumber": 8,
                    "question": "La poudre à lever (levure chimique) réagit sous l'effet :",
                    "answerOptions": [
                        {"text": "De l'humidité et de la chaleur", "isCorrect": True},
                        {"text": "Du temps de repos uniquement", "isCorrect": False},
                        {"text": "Du pétrissage intensif", "isCorrect": False},
                        {"text": "Du froid", "isCorrect": False}
                    ],
                    "correction": "Contrairement à la levure biologique qui demande du temps, la poudre à lever agit immédiatement au contact de l'eau et surtout à la chaleur du four."
                },
                {
                    "questionNumber": 9,
                    "question": "Qu'appelle-t-on le point de fusion ?",
                    "answerOptions": [
                        {"text": "Le passage de l'état solide à liquide", "isCorrect": True},
                        {"text": "La température d'ébullition", "isCorrect": False},
                        {"text": "Le moment où le produit brûle", "isCorrect": False},
                        {"text": "La congélation", "isCorrect": False}
                    ],
                    "correction": "C'est la température précise à laquelle une matière grasse fond. Le beurre fond vers 30-32°C, ce qui est proche de la température corporelle (fondant en bouche)."
                },
                {
                    "questionNumber": 10,
                    "question": "Une meringue se compose de :",
                    "answerOptions": [
                        {"text": "Blancs d'œufs et de sucre", "isCorrect": True},
                        {"text": "Blancs, jaunes et farine", "isCorrect": False},
                        {"text": "Crème et sucre", "isCorrect": False},
                        {"text": "Lait et œufs", "isCorrect": False}
                    ],
                    "correction": "C'est la base : une mousse obtenue par foisonnement des blancs, stabilisée par le sucre. Aucun corps gras ne doit être ajouté."
                },
                {
                    "questionNumber": 11,
                    "question": "Pour foisonner, une crème liquide doit contenir au moins :",
                    "answerOptions": [
                        {"text": "30% de matière grasse", "isCorrect": True},
                        {"text": "10% de lipides", "isCorrect": False},
                        {"text": "15% de matière grasse", "isCorrect": False},
                        {"text": "0% de gras", "isCorrect": False}
                    ],
                    "correction": "Sans matière grasse suffisante (min 30%, idéal 35%), les bulles d'air ne peuvent pas être emprisonnées stablement dans la crème."
                },
                {
                    "questionNumber": 12,
                    "question": "Le sucre inverti (Trimoline) est utilisé pour :",
                    "answerOptions": [
                        {"text": "Conserver le moelleux grâce à son pouvoir hygroscopique", "isCorrect": True},
                        {"text": "Rendre les biscuits croquants", "isCorrect": False},
                        {"text": "Donner une couleur blanche", "isCorrect": False},
                        {"text": "Remplacer la farine", "isCorrect": False}
                    ],
                    "correction": "Il retient l'humidité (hygroscopique), ce qui empêche les gâteaux de sécher trop vite et améliore leur texture."
                },
                {
                    "questionNumber": 13,
                    "question": "Les fruits secs du praliné sont :",
                    "answerOptions": [
                        {"text": "Amandes et noisettes", "isCorrect": True},
                        {"text": "Pistaches", "isCorrect": False},
                        {"text": "Noix", "isCorrect": False},
                        {"text": "Cacahuètes et noix de cajou", "isCorrect": False}
                    ],
                    "correction": "Le praliné classique est un mélange de sucre et d'amandes/noisettes torréfiées. Les autres fruits secs permettent de faire des pralinés 'spéciaux'."
                },
                {
                    "questionNumber": 14,
                    "question": "Un chocolat de couverture doit contenir :",
                    "answerOptions": [
                        {"text": "Au moins 31% de beurre de cacao", "isCorrect": True},
                        {"text": "Beaucoup de sucre", "isCorrect": False},
                        {"text": "De l'huile de palme", "isCorrect": False},
                        {"text": "Moins de 20% de cacao", "isCorrect": False}
                    ],
                    "correction": "Cette teneur élevée en beurre de cacao assure la fluidité nécessaire pour enrober des bonbons ou mouler des sujets fins."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel gélifiant est extrait de la peau des fruits ?",
                    "answerOptions": [
                        {"text": "La pectine", "isCorrect": True},
                        {"text": "La gélatine", "isCorrect": False},
                        {"text": "L'agar-agar", "isCorrect": False},
                        {"text": "L'amidon", "isCorrect": False}
                    ],
                    "correction": "La pectine est abondante dans les pépins et la peau des pommes ou des agrumes. Elle gélifie les confitures et nappages."
                },
                {
                    "questionNumber": 16,
                    "question": "La vanille 'Bourbon' vient principalement de :",
                    "answerOptions": [
                        {"text": "Madagascar", "isCorrect": True},
                        {"text": "Tahiti", "isCorrect": False},
                        {"text": "Mexique", "isCorrect": False},
                        {"text": "Chine", "isCorrect": False}
                    ],
                    "correction": "Le label 'Bourbon' couvre les productions de l'Océan Indien (Madagascar, La Réunion, Comores). C'est la variété Vanilla Planifolia."
                },
                {
                    "questionNumber": 17,
                    "question": "L'amidon sert principalement à :",
                    "answerOptions": [
                        {"text": "Épaissir les crèmes à la cuisson", "isCorrect": True},
                        {"text": "Sucrer", "isCorrect": False},
                        {"text": "Colorer", "isCorrect": False},
                        {"text": "Conserver", "isCorrect": False}
                    ],
                    "correction": "L'amidon gélifie à chaud (empesage), donnant sa consistance à la crème pâtissière."
                },
                {
                    "questionNumber": 18,
                    "question": "Le Gianduja contient :",
                    "answerOptions": [
                        {"text": "Du chocolat et des noisettes broyées", "isCorrect": True},
                        {"text": "Du chocolat et des amandes entières", "isCorrect": False},
                        {"text": "Uniquement du cacao", "isCorrect": False},
                        {"text": "Du praliné et de la crème", "isCorrect": False}
                    ],
                    "correction": "C'est une pâte homogène de chocolat et de noisettes très finement broyées (sans caramel, contrairement au praliné)."
                },
                {
                    "questionNumber": 19,
                    "question": "Le lait UHT est chauffé :",
                    "answerOptions": [
                        {"text": "À très haute température (140°C) pendant quelques secondes", "isCorrect": True},
                        {"text": "À 63°C pendant 30 minutes", "isCorrect": False},
                        {"text": "À 100°C pendant une heure", "isCorrect": False},
                        {"text": "À froid", "isCorrect": False}
                    ],
                    "correction": "UHT = Ultra Haute Température. Ce choc thermique stérilise le lait tout en préservant mieux ses qualités qu'une stérilisation classique longue."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel sucre a le pouvoir sucrant le plus faible (16) ?",
                    "answerOptions": [
                        {"text": "Le lactose", "isCorrect": True},
                        {"text": "Le saccharose", "isCorrect": False},
                        {"text": "Le fructose", "isCorrect": False},
                        {"text": "Le sucre inverti", "isCorrect": False}
                    ],
                    "correction": "Le lactose (sucre du lait) sucre très peu. Le saccharose est la référence (100). Le fructose sucre plus fort (environ 130)."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : TECHNIQUES DE FABRICATION (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNIQUES DE FABRICATION (Questions 21 à 40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "La méthode classique du feuilletage comporte :",
                    "answerOptions": [
                        {"text": "6 tours simples", "isCorrect": True},
                        {"text": "2 tours", "isCorrect": False},
                        {"text": "12 tours doubles", "isCorrect": False},
                        {"text": "Un seul tour simple", "isCorrect": False}
                    ],
                    "correction": "6 tours simples (ou 4 doubles) sont nécessaires pour obtenir le nombre de feuillets adéquat pour une levée régulière et légère."
                },
                {
                    "questionNumber": 22,
                    "question": "'Foisonner' signifie :",
                    "answerOptions": [
                        {"text": "Incorporer de l'air en fouettant", "isCorrect": True},
                        {"text": "Mélanger doucement à la spatule", "isCorrect": False},
                        {"text": "Écraser la pâte", "isCorrect": False},
                        {"text": "Tamiser la farine", "isCorrect": False}
                    ],
                    "correction": "C'est l'action mécanique (fouet) qui capture l'air dans la matière (blancs, crème, beurre) pour augmenter le volume."
                },
                {
                    "questionNumber": 23,
                    "question": "Cuisson idéale d'une crème anglaise ?",
                    "answerOptions": [
                        {"text": "À la nappe (82-84°C)", "isCorrect": True},
                        {"text": "À ébullition franche", "isCorrect": False},
                        {"text": "À 50°C", "isCorrect": False},
                        {"text": "Au four", "isCorrect": False}
                    ],
                    "correction": "Si on dépasse 85°C, les œufs coagulent et la crème tranche (devient granuleuse). Elle ne doit jamais bouillir."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle pâte nécessite un dessèchement sur le feu ?",
                    "answerOptions": [
                        {"text": "La pâte à choux", "isCorrect": True},
                        {"text": "La génoise", "isCorrect": False},
                        {"text": "La pâte sucrée", "isCorrect": False},
                        {"text": "Le feuilletage", "isCorrect": False}
                    ],
                    "correction": "On dessèche la 'panade' (eau+beurre+farine) sur le feu pour évaporer l'eau excédentaire avant d'incorporer les œufs."
                },
                {
                    "questionNumber": 25,
                    "question": "La meringue italienne se réalise avec :",
                    "answerOptions": [
                        {"text": "Un sirop de sucre cuit versé sur les blancs", "isCorrect": True},
                        {"text": "Du sucre glace mélangé à froid", "isCorrect": False},
                        {"text": "Du sucre en poudre ajouté au début", "isCorrect": False},
                        {"text": "Du sirop d'érable", "isCorrect": False}
                    ],
                    "correction": "Le sucre cuit (118°C-121°C) cuit partiellement les blancs, assurant une meringue très stable et brillante."
                },
                {
                    "questionNumber": 26,
                    "question": "'Chemiser un moule' consiste à :",
                    "answerOptions": [
                        {"text": "Appliquer une couche protectrice sur les parois", "isCorrect": True},
                        {"text": "Le laver à l'eau de Javel", "isCorrect": False},
                        {"text": "Le mettre au froid", "isCorrect": False},
                        {"text": "Le remplir à ras bord", "isCorrect": False}
                    ],
                    "correction": "On chemise (beurre/farine, papier, biscuit) pour empêcher l'adhérence et faciliter le démoulage."
                },
                {
                    "questionNumber": 27,
                    "question": "Le tempérage du chocolat sert à :",
                    "answerOptions": [
                        {"text": "Obtenir brillance et cassant", "isCorrect": True},
                        {"text": "Le rendre plus liquide pour la cuisson", "isCorrect": False},
                        {"text": "Lui donner un goût amer", "isCorrect": False},
                        {"text": "Le faire fondre rapidement", "isCorrect": False}
                    ],
                    "correction": "La courbe de température sélectionne la forme cristalline stable du beurre de cacao, évitant le blanchiment et assurant le brillant."
                },
                {
                    "questionNumber": 28,
                    "question": "Le 'fraisage' (ou frasage) sert à :",
                    "answerOptions": [
                        {"text": "Homogénéiser la pâte sans lui donner d'élasticité", "isCorrect": True},
                        {"text": "Pétrir longuement pour le gluten", "isCorrect": False},
                        {"text": "Incorporer de l'air", "isCorrect": False},
                        {"text": "Couper la pâte en morceaux", "isCorrect": False}
                    ],
                    "correction": "On écrase la pâte (brisée/sablée) avec la paume pour mélanger les ingrédients sans activer le gluten (ce qui la rendrait élastique et rétractable)."
                },
                {
                    "questionNumber": 29,
                    "question": "La dacquoise est un biscuit à base de :",
                    "answerOptions": [
                        {"text": "Meringue et poudre de fruits secs", "isCorrect": True},
                        {"text": "Pâte à choux", "isCorrect": False},
                        {"text": "Génoise au beurre", "isCorrect": False},
                        {"text": "Pâte sablée émiettée", "isCorrect": False}
                    ],
                    "correction": "C'est un biscuit meringué (souvent amande ou noisette) réalisé en incorporant les poudres délicatement dans des blancs montés."
                },
                {
                    "questionNumber": 30,
                    "question": "Pour une ganache, on verse la crème bouillante sur le chocolat pour :",
                    "answerOptions": [
                        {"text": "Créer une émulsion", "isCorrect": True},
                        {"text": "Cuire le chocolat", "isCorrect": False},
                        {"text": "Stériliser le mélange", "isCorrect": False},
                        {"text": "Refroidir la crème", "isCorrect": False}
                    ],
                    "correction": "La chaleur fait fondre le chocolat et le mélange énergique crée une émulsion lisse et brillante entre le gras (chocolat/crème) et l'eau (crème)."
                },
                {
                    "questionNumber": 31,
                    "question": "Le montage 'à l'envers' implique de :",
                    "answerOptions": [
                        {"text": "Commencer par le haut du gâteau au fond du moule", "isCorrect": True},
                        {"text": "Mettre le biscuit au fond du cercle", "isCorrect": False},
                        {"text": "Retourner le four", "isCorrect": False},
                        {"text": "Ne pas utiliser de moule", "isCorrect": False}
                    ],
                    "correction": "Technique moderne pour obtenir des dessus parfaits. On monte à l'envers, on congèle, puis on démoule et on retourne le tout."
                },
                {
                    "questionNumber": 32,
                    "question": "Le sablage permet d'obtenir une pâte :",
                    "answerOptions": [
                        {"text": "Friable", "isCorrect": True},
                        {"text": "Élastique", "isCorrect": False},
                        {"text": "Liquide", "isCorrect": False},
                        {"text": "Feuilletée", "isCorrect": False}
                    ],
                    "correction": "En enrobant la farine de gras (sable), on empêche l'eau de lier le gluten trop vite. La pâte s'effrite en bouche (sablée)."
                },
                {
                    "questionNumber": 33,
                    "question": "La crème mousseline est une crème pâtissière foisonnée avec :",
                    "answerOptions": [
                        {"text": "Du beurre", "isCorrect": True},
                        {"text": "De la crème fouettée", "isCorrect": False},
                        {"text": "Des blancs d'œufs", "isCorrect": False},
                        {"text": "Du mascarpone", "isCorrect": False}
                    ],
                    "correction": "Le beurre donne de l'onctuosité et de la tenue. C'est la crème du Paris-Brest et du Fraisier."
                },
                {
                    "questionNumber": 34,
                    "question": "'Puncher' un biscuit sert à :",
                    "answerOptions": [
                        {"text": "L'aromatiser et le rendre moelleux", "isCorrect": True},
                        {"text": "Le faire cuire", "isCorrect": False},
                        {"text": "Le découper", "isCorrect": False},
                        {"text": "Le glacer", "isCorrect": False}
                    ],
                    "correction": "On imbibe (punche) le biscuit avec un sirop pour qu'il ne soit pas sec et pour renforcer le goût du gâteau."
                },
                {
                    "questionNumber": 35,
                    "question": "La 'corne' est utilisée pour :",
                    "answerOptions": [
                        {"text": "Racler les récipients sans perte", "isCorrect": True},
                        {"text": "Fouetter les blancs", "isCorrect": False},
                        {"text": "Décorer le gâteau", "isCorrect": False},
                        {"text": "Étaler le glaçage", "isCorrect": False}
                    ],
                    "correction": "Outil souple indispensable pour récupérer toute la matière dans le bol ('corner')."
                },
                {
                    "questionNumber": 36,
                    "question": "La dorure s'applique :",
                    "answerOptions": [
                        {"text": "Avant la cuisson", "isCorrect": True},
                        {"text": "Après la cuisson", "isCorrect": False},
                        {"text": "Pendant le pétrissage", "isCorrect": False},
                        {"text": "À la sortie du four", "isCorrect": False}
                    ],
                    "correction": "L'œuf appliqué avant cuisson colore sous l'effet de la chaleur (réaction de Maillard)."
                },
                {
                    "questionNumber": 37,
                    "question": "La crème d'amande est un mélange de :",
                    "answerOptions": [
                        {"text": "Beurre, sucre, poudre d'amande, œufs", "isCorrect": True},
                        {"text": "Pâtissière et amandes", "isCorrect": False},
                        {"text": "Blancs d'œufs et amandes", "isCorrect": False},
                        {"text": "Lait et farine", "isCorrect": False}
                    ],
                    "correction": "C'est un mélange 'Tant pour Tant' (poids égaux) des 4 ingrédients, cuit ensuite au four (dans une tarte bourdaloue ou un pithiviers)."
                },
                {
                    "questionNumber": 38,
                    "question": "Pour monter des blancs, le matériel doit être exempt de :",
                    "answerOptions": [
                        {"text": "Gras", "isCorrect": True},
                        {"text": "Sucre", "isCorrect": False},
                        {"text": "Farine", "isCorrect": False},
                        {"text": "Froid", "isCorrect": False}
                    ],
                    "correction": "Le gras empêche la formation de la mousse des blancs."
                },
                {
                    "questionNumber": 39,
                    "question": "Cuire 'à blanc' signifie cuire :",
                    "answerOptions": [
                        {"text": "Un fond de tarte sans garniture", "isCorrect": True},
                        {"text": "Uniquement des blancs d'œufs", "isCorrect": False},
                        {"text": "À basse température", "isCorrect": False},
                        {"text": "Sans coloration", "isCorrect": False}
                    ],
                    "correction": "On cuit le fond de pâte seul (souvent lesté) pour qu'il soit croustillant avant d'y mettre une garniture qui ne cuit pas (fraises, crème citron cuite à part)."
                },
                {
                    "questionNumber": 40,
                    "question": "'Masquer' un entremets, c'est :",
                    "answerOptions": [
                        {"text": "Recouvrir entièrement de crème", "isCorrect": True},
                        {"text": "Cacher le gâteau dans une boîte", "isCorrect": False},
                        {"text": "Mettre un décor en chocolat", "isCorrect": False},
                        {"text": "Imbiber le biscuit", "isCorrect": False}
                    ],
                    "correction": "On masque à la spatule pour lisser les imperfections avant le glaçage final."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : HYGIÈNE ET SÉCURITÉ ALIMENTAIRE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : HYGIÈNE ET SÉCURITÉ ALIMENTAIRE (Questions 41 à 60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "La conservation des pâtisseries à base de crème se fait à :",
                    "answerOptions": [
                        {"text": "+4°C maximum", "isCorrect": True},
                        {"text": "+12°C", "isCorrect": False},
                        {"text": "Température ambiante", "isCorrect": False},
                        {"text": "-20°C", "isCorrect": False}
                    ],
                    "correction": "Le froid positif (0 à 4°C) est obligatoire pour ralentir les bactéries dans les produits fragiles."
                },
                {
                    "questionNumber": 42,
                    "question": "La méthode HACCP sert à :",
                    "answerOptions": [
                        {"text": "Analyser et maîtriser les dangers", "isCorrect": True},
                        {"text": "Nettoyer le sol", "isCorrect": False},
                        {"text": "Calculer les coûts", "isCorrect": False},
                        {"text": "Organiser les vacances", "isCorrect": False}
                    ],
                    "correction": "C'est le système de référence pour la sécurité sanitaire : identifier les risques et mettre en place des contrôles."
                },
                {
                    "questionNumber": 43,
                    "question": "Le 'FIFO' (First In, First Out) concerne :",
                    "answerOptions": [
                        {"text": "La rotation des stocks", "isCorrect": True},
                        {"text": "L'ordre de départ des employés", "isCorrect": False},
                        {"text": "Le pétrissage", "isCorrect": False},
                        {"text": "La cuisson", "isCorrect": False}
                    ],
                    "correction": "Premier entré, premier sorti. On utilise les produits les plus anciens avant les nouveaux pour éviter le gaspillage."
                },
                {
                    "questionNumber": 44,
                    "question": "Les salmonelles sont principalement associées aux :",
                    "answerOptions": [
                        {"text": "Œufs et volailles", "isCorrect": True},
                        {"text": "Légumes terreux", "isCorrect": False},
                        {"text": "Produits laitiers", "isCorrect": False},
                        {"text": "Conserves", "isCorrect": False}
                    ],
                    "correction": "Bactérie dangereuse présente dans le tube digestif des volailles et pouvant contaminer les œufs."
                },
                {
                    "questionNumber": 45,
                    "question": "Les surgelés doivent être stockés à :",
                    "answerOptions": [
                        {"text": "-18°C", "isCorrect": True},
                        {"text": "0°C", "isCorrect": False},
                        {"text": "-4°C", "isCorrect": False},
                        {"text": "-10°C", "isCorrect": False}
                    ],
                    "correction": "Température réglementaire pour stopper toute activité microbienne."
                },
                {
                    "questionNumber": 46,
                    "question": "Recongeler un produit décongelé est interdit car :",
                    "answerOptions": [
                        {"text": "La charge bactérienne devient dangereuse", "isCorrect": True},
                        {"text": "Le produit perd son goût", "isCorrect": False},
                        {"text": "La texture change", "isCorrect": False},
                        {"text": "C'est impossible techniquement", "isCorrect": False}
                    ],
                    "correction": "La décongélation permet aux bactéries de se multiplier. Recongeler préserve ce niveau élevé, et la seconde décongélation entraîne une explosion microbienne toxique."
                },
                {
                    "questionNumber": 47,
                    "question": "La tenue professionnelle complète comprend :",
                    "answerOptions": [
                        {"text": "Veste, pantalon, coiffe, chaussures de sécurité", "isCorrect": True},
                        {"text": "Tablier seul", "isCorrect": False},
                        {"text": "Veste et jeans", "isCorrect": False},
                        {"text": "Gants et masque", "isCorrect": False}
                    ],
                    "correction": "Elle protège le produit des contaminations venant du personnel (vêtements de ville, cheveux)."
                },
                {
                    "questionNumber": 48,
                    "question": "Le porteur sain du staphylocoque doré est souvent :",
                    "answerOptions": [
                        {"text": "L'être humain", "isCorrect": True},
                        {"text": "Le rat", "isCorrect": False},
                        {"text": "L'œuf", "isCorrect": False},
                        {"text": "Le carton", "isCorrect": False}
                    ],
                    "correction": "Présent dans le nez, la bouche ou sur la peau de l'homme. La contamination se fait par les mains ou la toux."
                },
                {
                    "questionNumber": 49,
                    "question": "Sur une plaie, il faut mettre :",
                    "answerOptions": [
                        {"text": "Un pansement étanche et un gant", "isCorrect": True},
                        {"text": "Juste un pansement", "isCorrect": False},
                        {"text": "Du sparadrap", "isCorrect": False},
                        {"text": "Rien si ça ne saigne plus", "isCorrect": False}
                    ],
                    "correction": "Double protection obligatoire : soigner la plaie et empêcher le pansement (ou les germes) de tomber dans la nourriture via le gant."
                },
                {
                    "questionNumber": 50,
                    "question": "La 'marche en avant' a pour but d'éviter :",
                    "answerOptions": [
                        {"text": "Les contaminations croisées", "isCorrect": True},
                        {"text": "De perdre du temps", "isCorrect": False},
                        {"text": "Les accidents de travail", "isCorrect": False},
                        {"text": "De marcher en arrière", "isCorrect": False}
                    ],
                    "correction": "Le propre ne doit jamais croiser le sale (poubelles, retours assiettes) dans le circuit de production."
                },
                {
                    "questionNumber": 51,
                    "question": "La désinfection intervient obligatoirement :",
                    "answerOptions": [
                        {"text": "Après le nettoyage", "isCorrect": True},
                        {"text": "Avant le nettoyage", "isCorrect": False},
                        {"text": "Au lieu du nettoyage", "isCorrect": False},
                        {"text": "Une fois par an", "isCorrect": False}
                    ],
                    "correction": "On ne désinfecte que ce qui est propre. Le nettoyage enlève la saleté, la désinfection tue les germes restants."
                },
                {
                    "questionNumber": 52,
                    "question": "La DDM (Date de Durabilité Minimale) indique :",
                    "answerOptions": [
                        {"text": "Une perte de qualité gustative possible après la date", "isCorrect": True},
                        {"text": "Un danger immédiat pour la santé", "isCorrect": False},
                        {"text": "La date de fabrication", "isCorrect": False},
                        {"text": "La date de livraison", "isCorrect": False}
                    ],
                    "correction": "Ancienne DLUO. Le produit reste sain après cette date, contrairement à la DLC."
                },
                {
                    "questionNumber": 53,
                    "question": "Pour décongeler en sécurité, on place le produit :",
                    "answerOptions": [
                        {"text": "Au réfrigérateur (0°C/+4°C)", "isCorrect": True},
                        {"text": "Sur le plan de travail", "isCorrect": False},
                        {"text": "Près du four", "isCorrect": False},
                        {"text": "Dans l'eau tiède", "isCorrect": False}
                    ],
                    "correction": "Le maintien au froid pendant la décongélation empêche le réveil brutal des bactéries."
                },
                {
                    "questionNumber": 54,
                    "question": "La zone de danger de multiplication bactérienne se situe entre :",
                    "answerOptions": [
                        {"text": "+10°C et +63°C", "isCorrect": True},
                        {"text": "-18°C et 0°C", "isCorrect": False},
                        {"text": "+65°C et +100°C", "isCorrect": False},
                        {"text": "0°C et +3°C", "isCorrect": False}
                    ],
                    "correction": "C'est la plage de température tiède où les bactéries se reproduisent le plus vite."
                },
                {
                    "questionNumber": 55,
                    "question": "Les plats témoins servent aux :",
                    "answerOptions": [
                        {"text": "Services vétérinaires en cas d'intoxication", "isCorrect": True},
                        {"text": "Clients pour goûter", "isCorrect": False},
                        {"text": "Employés pour manger", "isCorrect": False},
                        {"text": "Photographes", "isCorrect": False}
                    ],
                    "correction": "Ils sont prélevés sur chaque menu et gardés au froid pour analyse en cas de problème sanitaire collectif (TIAC)."
                },
                {
                    "questionNumber": 56,
                    "question": "Pourquoi ne pas casser les œufs sur le bord du bol ?",
                    "answerOptions": [
                        {"text": "Pour éviter la chute de morceaux de coquille souillée", "isCorrect": True},
                        {"text": "Pour ne pas abîmer le bol", "isCorrect": False},
                        {"text": "Pour aller plus vite", "isCorrect": False},
                        {"text": "Pour séparer le blanc du jaune", "isCorrect": False}
                    ],
                    "correction": "La coquille externe est sale. Casser à plat limite le risque d'introduire des germes à l'intérieur du mélange."
                },
                {
                    "questionNumber": 57,
                    "question": "L'inox est le matériau privilégié car il est :",
                    "answerOptions": [
                        {"text": "Imputrescible et facile à nettoyer", "isCorrect": True},
                        {"text": "Bon marché", "isCorrect": False},
                        {"text": "Joli", "isCorrect": False},
                        {"text": "Rugueux", "isCorrect": False}
                    ],
                    "correction": "Il est lisse, dur et inerte chimiquement, empêchant les niches à bactéries."
                },
                {
                    "questionNumber": 58,
                    "question": "La leptospirose est transmise par :",
                    "answerOptions": [
                        {"text": "L'urine des rongeurs", "isCorrect": True},
                        {"text": "Les insectes", "isCorrect": False},
                        {"text": "Les oiseaux", "isCorrect": False},
                        {"text": "Les poissons", "isCorrect": False}
                    ],
                    "correction": "Maladie grave liée aux nuisibles (rats), d'où l'importance de la dératisation."
                },
                {
                    "questionNumber": 59,
                    "question": "La validation du nettoyage se fait par :",
                    "answerOptions": [
                        {"text": "Prélèvements microbiologiques de surface", "isCorrect": True},
                        {"text": "Contrôle visuel simple", "isCorrect": False},
                        {"text": "L'odeur de propre", "isCorrect": False},
                        {"text": "La blancheur du sol", "isCorrect": False}
                    ],
                    "correction": "Seule l'analyse en laboratoire prouve qu'il n'y a plus de germes."
                },
                {
                    "questionNumber": 60,
                    "question": "Le vert-de-gris (toxique) se forme sur :",
                    "answerOptions": [
                        {"text": "Le cuivre non étamé", "isCorrect": True},
                        {"text": "L'inox", "isCorrect": False},
                        {"text": "L'aluminium", "isCorrect": False},
                        {"text": "Le fer", "isCorrect": False}
                    ],
                    "correction": "Réaction d'oxydation du cuivre au contact de l'acidité des aliments. Le cuivre doit être protégé par une couche d'étain (sauf pour le sucre)."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : SCIENCES APPLIQUÉES À L'ALIMENTATION (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : SCIENCES APPLIQUÉES À L'ALIMENTATION (Questions 61 à 80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le rôle principal des glucides dans l'organisme ?",
                    "answerOptions": [
                        {"text": "Fournir de l'énergie rapidement disponible", "isCorrect": True},
                        {"text": "Construire les muscles", "isCorrect": False},
                        {"text": "Transporter les vitamines", "isCorrect": False},
                        {"text": "Renforcer les os", "isCorrect": False}
                    ],
                    "correction": "Les glucides (sucres lents et rapides) sont le principal carburant de l'organisme."
                },
                {
                    "questionNumber": 62,
                    "question": "Comment appelle-t-on la dégradation des lipides (matières grasses) qui produit une odeur et un goût désagréables (rancissement) ?",
                    "answerOptions": [
                        {"text": "L'oxydation", "isCorrect": True},
                        {"text": "La fermentation", "isCorrect": False},
                        {"text": "L'hydrolyse", "isCorrect": False},
                        {"text": "La caramélisation", "isCorrect": False}
                    ],
                    "correction": "L'oxydation est la réaction chimique de l'oxygène de l'air sur les acides gras insaturés (dans le beurre ou les huiles), causant l'altération et le rancissement."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle est la température idéale pour le stockage du chocolat noir tempéré avant utilisation ?",
                    "answerOptions": [
                        {"text": "16°C à 18°C", "isCorrect": True},
                        {"text": "25°C à 28°C", "isCorrect": False},
                        {"text": "4°C à 6°C", "isCorrect": False},
                        {"text": "30°C à 32°C", "isCorrect": False}
                    ],
                    "correction": "Après tempérage, le chocolat doit être utilisé à sa température de travail (ex: 31-32°C pour le noir). Mais pour le stocker une fois cristallisé (en moule ou en tablette), la température ambiante idéale est fraîche et stable (16-18°C), à l'abri de l'humidité."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle réaction chimique donne la couleur brune aux gâteaux et aux croûtes de pain ?",
                    "answerOptions": [
                        {"text": "La réaction de Maillard", "isCorrect": True},
                        {"text": "La fermentation lactique", "isCorrect": False},
                        {"text": "La coagulation des protéines", "isCorrect": False},
                        {"text": "L'hydrolyse de l'amidon", "isCorrect": False}
                    ],
                    "correction": "La réaction de Maillard est une réaction chimique complexe entre les sucres et les protéines sous l'effet de la chaleur, produisant des pigments bruns (mélanoïdines) et des arômes de grillé/rôti."
                },
                {
                    "questionNumber": 65,
                    "question": "L'eau potable doit être :",
                    "answerOptions": [
                        {"text": "Incolore, inodore et sans germes pathogènes", "isCorrect": True},
                        {"text": "Riche en bactéries", "isCorrect": False},
                        {"text": "Légèrement trouble", "isCorrect": False},
                        {"text": "Distillée", "isCorrect": False}
                    ],
                    "correction": "L'eau potable ('eau destinée à la consommation humaine') doit respecter des critères organoleptiques (claire, sans odeur), physico-chimiques (pH, nitrates...) et microbiologiques (absence de parasites et bactéries pathogènes)."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le pH neutre ?",
                    "answerOptions": [
                        {"text": "7", "isCorrect": True},
                        {"text": "1", "isCorrect": False},
                        {"text": "14", "isCorrect": False},
                        {"text": "4.5", "isCorrect": False}
                    ],
                    "correction": "L'échelle de pH va de 0 à 14. Un pH de 7 est neutre (eau pure). En dessous de 7, le milieu est acide (citron). Au-dessus de 7, il est basique ou alcalin (eau de Javel)."
                },
                {
                    "questionNumber": 67,
                    "question": "La pasteurisation est un traitement thermique qui :",
                    "answerOptions": [
                        {"text": "Détruit les formes végétatives des micro-organismes pathogènes (< 100°C)", "isCorrect": True},
                        {"text": "Stérilise totalement le produit (> 120°C)", "isCorrect": False},
                        {"text": "Congèle le produit", "isCorrect": False},
                        {"text": "Déshydrate le produit", "isCorrect": False}
                    ],
                    "correction": "La pasteurisation chauffe l'aliment entre 60°C et 100°C pour tuer les pathogènes non sporulés et réduire la flore totale, tout en préservant les qualités organoleptiques du produit."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le principal nutriment des fruits à coque (amande, noisette) ?",
                    "answerOptions": [
                        {"text": "Les lipides (matières grasses)", "isCorrect": True},
                        {"text": "Les protéines", "isCorrect": False},
                        {"text": "Les vitamines", "isCorrect": False},
                        {"text": "Les glucides rapides", "isCorrect": False}
                    ],
                    "correction": "Les fruits à coque sont très riches en lipides (acides gras insaturés) et en protéines, ce qui en fait des aliments très énergétiques."
                },
                {
                    "questionNumber": 69,
                    "question": "Le gluten, réseau élastique, se développe grâce à l'association de :",
                    "answerOptions": [
                        {"text": "Protéines (Gluténines et Gliadines) + Eau + Action mécanique", "isCorrect": True},
                        {"text": "Lipides + Farine + Air", "isCorrect": False},
                        {"text": "Sucre + Eau + Chaleur", "isCorrect": False},
                        {"text": "Amidon + Sel + Levure", "isCorrect": False}
                    ],
                    "correction": "Le gluten est la combinaison des protéines de la farine (glutenine et gliadine) qui, en s'hydratant (eau) et par l'action du pétrissage (action mécanique), forment un réseau viscoélastique."
                },
                {
                    "questionNumber": 70,
                    "question": "La fermentation panaire est une fermentation :",
                    "answerOptions": [
                        {"text": "Alcoolique", "isCorrect": True},
                        {"text": "Lactique", "isCorrect": False},
                        {"text": "Acétique", "isCorrect": False},
                        {"text": "Butyrique", "isCorrect": False}
                    ],
                    "correction": "La levure transforme les sucres en alcool (éthanol) et en gaz carbonique (CO2). C'est donc une fermentation alcoolique. L'alcool s'évapore à la cuisson, le gaz fait lever la pâte."
                },
                {
                    "questionNumber": 71,
                    "question": "Un aliment cariogène est un aliment qui :",
                    "answerOptions": [
                        {"text": "Favorise l'apparition des caries dentaires (sucré et collant)", "isCorrect": True},
                        {"text": "Protège les dents", "isCorrect": False},
                        {"text": "Contient beaucoup de calcium", "isCorrect": False},
                        {"text": "Est très acide", "isCorrect": False}
                    ],
                    "correction": "Les produits de pâtisserie, riches en saccharose et souvent collants, sont cariogènes. Les bactéries de la bouche transforment ces sucres en acides qui attaquent l'émail des dents."
                },
                {
                    "questionNumber": 72,
                    "question": "Que signifie 'organoleptique' ?",
                    "answerOptions": [
                        {"text": "Qui se rapporte aux sens (goût, odeur, aspect, texture)", "isCorrect": True},
                        {"text": "Qui est biologique", "isCorrect": False},
                        {"text": "Qui est organisé", "isCorrect": False},
                        {"text": "Qui est toxique", "isCorrect": False}
                    ],
                    "correction": "Les qualités organoleptiques d'une pâtisserie sont celles perçues par nos sens : la vue (couleur, forme), l'odorat (arôme), le goût (saveur) et le toucher (texture en bouche)."
                },
                {
                    "questionNumber": 73,
                    "question": "Le gluten est dangereux pour les personnes atteintes de :",
                    "answerOptions": [
                        {"text": "La maladie cœliaque", "isCorrect": True},
                        {"text": "Diabète", "isCorrect": False},
                        {"text": "Cholestérol", "isCorrect": False},
                        {"text": "Hypertension", "isCorrect": False}
                    ],
                    "correction": "La maladie cœliaque est une affection auto-immune qui rend l'ingestion de gluten néfaste pour la paroi intestinale. Les pâtissiers doivent savoir identifier les ingrédients sans gluten."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle est la principale cause d'une coloration trop pâle sur une croûte de tarte ou de biscuit ?",
                    "answerOptions": [
                        {"text": "Un manque de sucre (ou une cuisson pas assez chaude)", "isCorrect": True},
                        {"text": "Trop de levure chimique", "isCorrect": False},
                        {"text": "Trop de sel", "isCorrect": False},
                        {"text": "Trop d'eau dans la pâte", "isCorrect": False}
                    ],
                    "correction": "La coloration dorée résulte de la caramélisation et de la réaction de Maillard (sucre + protéines). Un manque de sucre ou une température de cuisson trop basse (ne dépassant pas 140°C-150°C) ne permet pas à ces réactions de se produire correctement."
                },
                {
                    "questionNumber": 75,
                    "question": "L'étuvage d'une pâte levée (ex: croissant) a pour but de :",
                    "answerOptions": [
                        {"text": "Activer la levure pour faire lever la pâte", "isCorrect": True},
                        {"text": "Bloquer la levée pour l'étaler plus facilement", "isCorrect": False},
                        {"text": "Sécher la pâte pour la rendre plus croustillante", "isCorrect": False},
                        {"text": "La cuire entièrement", "isCorrect": False}
                    ],
                    "correction": "L'étuvage (chambre de pousse) permet de mettre la pâte dans des conditions de chaleur et d'humidité optimales pour que la levure produise du gaz carbonique, faisant gonfler la pâte (pousse ou apprêt)."
                },
                {
                    "questionNumber": 76,
                    "question": "Les fibres alimentaires sont importantes pour :",
                    "answerOptions": [
                        {"text": "Le transit intestinal", "isCorrect": True},
                        {"text": "La vision nocturne", "isCorrect": False},
                        {"text": "La force musculaire", "isCorrect": False},
                        {"text": "L'audition", "isCorrect": False}
                    ],
                    "correction": "Les fibres (cellulose, pectine...) ne sont pas digérées mais facilitent le transit intestinal et régulent l'absorption des sucres et des graisses. On les trouve dans les fruits, légumes et céréales complètes."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le rôle des antioxydants (comme la vitamine E ou C) ?",
                    "answerOptions": [
                        {"text": "Lutter contre le vieillissement cellulaire et l'oxydation des graisses", "isCorrect": True},
                        {"text": "Donner de l'énergie", "isCorrect": False},
                        {"text": "Faire dormir", "isCorrect": False},
                        {"text": "Colorer les aliments", "isCorrect": False}
                    ],
                    "correction": "Les antioxydants protègent les cellules des radicaux libres. En pâtisserie, ils évitent aussi le rancissement des matières grasses (oxydation des lipides)."
                },
                {
                    "questionNumber": 78,
                    "question": "L'émulsion est un mélange physique de :",
                    "answerOptions": [
                        {"text": "Deux liquides non miscibles (comme l'eau et l'huile)", "isCorrect": True},
                        {"text": "Un solide et un gaz", "isCorrect": False},
                        {"text": "Deux solides", "isCorrect": False},
                        {"text": "Un gaz et un liquide", "isCorrect": False}
                    ],
                    "correction": "Une émulsion est la dispersion de gouttelettes d'un liquide dans un autre liquide avec lequel il ne se mélange pas naturellement. La ganache et la mayonnaise sont des émulsions."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle est l'unité de mesure de l'énergie alimentaire ?",
                    "answerOptions": [
                        {"text": "La kilocalorie (kcal) ou le kilojoule (kJ)", "isCorrect": True},
                        {"text": "Le watt", "isCorrect": False},
                        {"text": "Le volt", "isCorrect": False},
                        {"text": "Le décibel", "isCorrect": False}
                    ],
                    "correction": "La valeur énergétique est exprimée en kilocalories (kcal) ou en kilojoules (kJ) sur les étiquettes nutritionnelles."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le phénomène responsable du durcissement du pain ou des viennoiseries après quelques heures ?",
                    "answerOptions": [
                        {"text": "La rétrogradation de l'amidon", "isCorrect": True},
                        {"text": "La fermentation", "isCorrect": False},
                        {"text": "Le séchage complet", "isCorrect": False},
                        {"text": "L'oxydation du gluten", "isCorrect": False}
                    ],
                    "correction": "La rétrogradation de l'amidon est le réalignement des molécules d'amidon (amylose et amylopectine) après refroidissement, ce qui expulse l'eau et rend la mie dure. C'est le phénomène de rassissement."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : GESTION, RÉGLEMENTATION ET ÉQUIPEMENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : GESTION, RÉGLEMENTATION ET ÉQUIPEMENT (Questions 81 à 100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'objectif principal de l'établissement d'une fiche technique de fabrication ?",
                    "answerOptions": [
                        {"text": "Garantir la régularité du produit et calculer le coût matière pour fixer le prix de vente", "isCorrect": True},
                        {"text": "Servir de brouillon", "isCorrect": False},
                        {"text": "Décorer le laboratoire", "isCorrect": False},
                        {"text": "Raconter l'histoire de la recette", "isCorrect": False}
                    ],
                    "correction": "La fiche technique est l'outil de base de la gestion. Elle assure la régularité de la production (recette fixe) et permet de calculer le coût matière pour fixer le prix de vente."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment calcule-t-on le 'Coût Matière' d'un gâteau ?",
                    "answerOptions": [
                        {"text": "Somme des prix des ingrédients utilisés (Quantité x Prix unitaire)", "isCorrect": True},
                        {"text": "Prix de vente moins la TVA", "isCorrect": False},
                        {"text": "Total des factures d'électricité", "isCorrect": False},
                        {"text": "Le prix de la farine uniquement", "isCorrect": False}
                    ],
                    "correction": "Le coût matière correspond à la valeur monétaire de toutes les matières premières consommées pour réaliser la recette. C'est le premier indicateur pour calculer la marge."
                },
                {
                    "questionNumber": 83,
                    "question": "Que signifie le sigle 'TTC' ?",
                    "answerOptions": [
                        {"text": "Toutes Taxes Comprises", "isCorrect": True},
                        {"text": "Tout Travail Compté", "isCorrect": False},
                        {"text": "Tarif Très Correct", "isCorrect": False},
                        {"text": "Taxe Technique Commerçante", "isCorrect": False}
                    ],
                    "correction": "Un prix TTC inclut le prix Hors Taxe (HT) + la Taxe sur la Valeur Ajoutée (TVA). C'est le prix que paie le client final en boutique."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la définition de la 'Marge Brute' ?",
                    "answerOptions": [
                        {"text": "Chiffre d'Affaires (HT) - Coût Matière", "isCorrect": True},
                        {"text": "Le bénéfice net de l'entreprise", "isCorrect": False},
                        {"text": "Le salaire du patron", "isCorrect": False},
                        {"text": "Le montant de la caisse", "isCorrect": False}
                    ],
                    "correction": "La marge brute est ce qu'il reste du prix de vente une fois les ingrédients payés. Elle sert à couvrir les charges (salaires, loyers, électricité) avant de dégager un bénéfice net."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle est la réglementation concernant l'affichage des allergènes en pâtisserie ?",
                    "answerOptions": [
                        {"text": "La liste des 14 allergènes majeurs doit être clairement indiquée et accessible au client pour tous les produits non emballés", "isCorrect": True},
                        {"text": "C'est facultatif", "isCorrect": False},
                        {"text": "Il suffit de dire 'peut contenir des traces'", "isCorrect": False},
                        {"text": "Seuls les produits à base de fruits doivent être étiquetés", "isCorrect": False}
                    ],
                    "correction": "La réglementation INCO impose l'information obligatoire des consommateurs sur la présence des 14 allergènes majeurs (gluten, œufs, lait, fruits à coque, etc.) dans les produits non préemballés."
                },
                {
                    "questionNumber": 86,
                    "question": "Qu'est-ce qu'une DLC (Date Limite de Consommation) ?",
                    "answerOptions": [
                        {"text": "La date maximale après laquelle le produit est considéré comme dangereux pour la santé", "isCorrect": True},
                        {"text": "La date de production", "isCorrect": False},
                        {"text": "La date avant laquelle il est préférable de consommer le produit (DDM)", "isCorrect": False},
                        {"text": "La date d'achat du produit", "isCorrect": False}
                    ],
                    "correction": "La DLC est une obligation de sécurité. Dépassée, la denrée devient impropre à la consommation car la prolifération microbienne peut atteindre un seuil limite."
                },
                {
                    "questionNumber": 87,
                    "question": "En gestion des stocks, que signifie faire un 'inventaire' ?",
                    "answerOptions": [
                        {"text": "Compter physiquement les marchandises présentes en stock à une date donnée", "isCorrect": True},
                        {"text": "Commander des produits", "isCorrect": False},
                        {"text": "Ranger le laboratoire", "isCorrect": False},
                        {"text": "Jeter les produits périmés", "isCorrect": False}
                    ],
                    "correction": "L'inventaire est le comptage exhaustif des stocks réels. Il permet de vérifier la valeur du stock, de calculer les pertes et de valider les comptes de l'entreprise en fin d'exercice."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le taux de TVA réduit applicable à la majorité des produits de boulangerie-pâtisserie en France (vente à emporter) ?",
                    "answerOptions": [
                        {"text": "5,5 %", "isCorrect": True},
                        {"text": "20 %", "isCorrect": False},
                        {"text": "10 %", "isCorrect": False},
                        {"text": "2,1 %", "isCorrect": False}
                    ],
                    "correction": "Les denrées alimentaires destinées à une consommation différée (pain, viennoiseries, gâteaux) bénéficient du taux réduit de 5,5%."
                },
                {
                    "questionNumber": 89,
                    "question": "Qu'est-ce qu'un 'bon de livraison' ?",
                    "answerOptions": [
                        {"text": "Le document remis par le fournisseur qui accompagne la marchandise", "isCorrect": True},
                        {"text": "Le document pour payer la marchandise", "isCorrect": False},
                        {"text": "La liste des courses", "isCorrect": False},
                        {"text": "Un bon de réduction", "isCorrect": False}
                    ],
                    "correction": "Le bon de livraison (BL) permet de vérifier que la marchandise reçue correspond bien à ce qui a été commandé (quantité, qualité) avant de signer et d'accepter la livraison."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel équipement utilise-t-on pour cristalliser le sucre et réaliser des décors de pièces artistiques ?",
                    "answerOptions": [
                        {"text": "Un rechaud au gaz", "isCorrect": True},
                        {"text": "Un four à micro-ondes", "isCorrect": False},
                        {"text": "Une batte de cuisine", "isCorrect": False},
                        {"text": "Un tamis à farine", "isCorrect": False}
                    ],
                    "correction": "Le sucre est cuit à très haute température (grand cassé) puis versé sur une surface froide (feuille de silicone) et travaillé à l'aide d'un réchaud au gaz (soufflage, tirage, coulage)."
                },
                {
                    "questionNumber": 91,
                    "question": "Dans un four de pâtisserie, que permet le fonctionnement en 'Sole et Voûte' ?",
                    "answerOptions": [
                        {"text": "Une cuisson par rayonnement à chaleur sèche, idéale pour les pâtes et les fonds de tarte", "isCorrect": True},
                        {"text": "Une cuisson par convection (air brassé)", "isCorrect": False},
                        {"text": "Une cuisson vapeur", "isCorrect": False},
                        {"text": "Une cuisson par induction", "isCorrect": False}
                    ],
                    "correction": "Le mode Sole et Voûte (résistances en haut et en bas) est un mode de cuisson traditionnel par rayonnement. Il est parfait pour cuire les pâtes qui ont besoin d'une chaleur venant de la base (la sole)."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le document comptable qui résume les produits (ventes) et les charges (dépenses) sur une année ?",
                    "answerOptions": [
                        {"text": "Le Compte de Résultat", "isCorrect": True},
                        {"text": "Le Bilan", "isCorrect": False},
                        {"text": "Le devis", "isCorrect": False},
                        {"text": "La facture", "isCorrect": False}
                    ],
                    "correction": "Le Compte de Résultat est le 'film' de l'année. Il liste tout ce qu'on a gagné et tout ce qu'on a dépensé. La différence donne le résultat net (bénéfice ou perte)."
                },
                {
                    "questionNumber": 93,
                    "question": "Dans un batteur-mélangeur, quel outil utilise-t-on pour une pâte brisée ou sablée ?",
                    "answerOptions": [
                        {"text": "La feuille (ou palette)", "isCorrect": True},
                        {"text": "Le fouet", "isCorrect": False},
                        {"text": "Le crochet", "isCorrect": False},
                        {"text": "La maryse", "isCorrect": False}
                    ],
                    "correction": "La feuille (outil plat) est utilisée pour les pâtes friables, les crèmes au beurre ou les appareils à cakes. Le fouet sert aux émulsions (œufs), le crochet aux pâtes levées (brioche)."
                },
                {
                    "questionNumber": 94,
                    "question": "Qu'est-ce que la 'perte au feu' ?",
                    "answerOptions": [
                        {"text": "La perte de poids d'un produit lors de la cuisson (évaporation de l'eau)", "isCorrect": True},
                        {"text": "Un gâteau qui a brûlé", "isCorrect": False},
                        {"text": "Jeter des ingrédients", "isCorrect": False},
                        {"text": "La perte de goût", "isCorrect": False}
                    ],
                    "correction": "La perte au feu est la diminution de masse ou de volume (en général par évaporation de l'eau) que subit un produit pendant sa cuisson. Elle doit être prise en compte dans le calcul des coûts."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est l'outil utilisé pour affûter ou maintenir le fil d'un couteau ?",
                    "answerOptions": [
                        {"text": "Le fusil", "isCorrect": True},
                        {"text": "La meuleuse", "isCorrect": False},
                        {"text": "Le rouleau", "isCorrect": False},
                        {"text": "La mandoline", "isCorrect": False}
                    ],
                    "correction": "Le fusil (tige métallique abrasive) est l'outil d'entretien courant des couteaux, il redresse le fil de la lame. L'affûtage profond (meule) est un travail plus intensif."
                },
                {
                    "questionNumber": 96,
                    "question": "Dans quel type de four la chaleur est-elle brassée par une turbine pour une cuisson rapide et homogène ?",
                    "answerOptions": [
                        {"text": "Le four à convection (chaleur tournante)", "isCorrect": True},
                        {"text": "Le four à sole (statique)", "isCorrect": False},
                        {"text": "Le four à micro-ondes", "isCorrect": False},
                        {"text": "Le four à bois", "isCorrect": False}
                    ],
                    "correction": "Le four à convection (chaleur tournante) utilise une turbine pour distribuer l'air chaud de manière uniforme, permettant de cuire plusieurs plaques en même temps avec une bonne homogénéité."
                },
                {
                    "questionNumber": 97,
                    "question": "Qu'est-ce qu'une 'chambre de pousse' ?",
                    "answerOptions": [
                        {"text": "Une enceinte qui contrôle la température et l'humidité pour la levée des pâtes", "isCorrect": True},
                        {"text": "Un endroit pour stocker la farine", "isCorrect": False},
                        {"text": "Un four à basse température", "isCorrect": False},
                        {"text": "Une chambre froide négative", "isCorrect": False}
                    ],
                    "correction": "La chambre de pousse permet de maîtriser la fermentation (apprêt) des pâtes levées (brioches, croissants) en gérant la chaleur (pour activer la levure) et l'hygrométrie (pour éviter le croûtage)."
                },
                {
                    "questionNumber": 98,
                    "question": "Le respect de la chaîne du froid concerne :",
                    "answerOptions": [
                        {"text": "Le maintien constant des aliments aux températures réglementaires de la production à la consommation", "isCorrect": True},
                        {"text": "Uniquement le transport en camion", "isCorrect": False},
                        {"text": "Uniquement le congélateur", "isCorrect": False},
                        {"text": "Le fait de travailler en hiver", "isCorrect": False}
                    ],
                    "correction": "La chaîne du froid ne doit jamais être interrompue. Une rupture entraîne une accélération de la croissance microbienne et réduit la durée de vie du produit, voire le rend dangereux."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel extincteur utilise-t-on préférentiellement sur un feu d'origine électrique ou de gaz ?",
                    "answerOptions": [
                        {"text": "Extincteur CO2 (Dioxide de carbone)", "isCorrect": True},
                        {"text": "Extincteur à eau", "isCorrect": False},
                        {"text": "Un seau d'eau", "isCorrect": False},
                        {"text": "Une couverture", "isCorrect": False}
                    ],
                    "correction": "Le CO2 étouffe le feu en privant les flammes d'oxygène et ne laisse pas de résidus, ce qui préserve les installations électriques, contrairement à l'eau qui est conductrice (danger d'électrocution)."
                },
                {
                    "questionNumber": 100,
                    "question": "Le 'Label Rouge' garantit :",
                    "answerOptions": [
                        {"text": "Une qualité supérieure à la moyenne des produits courants similaires", "isCorrect": True},
                        {"text": "Une origine géographique précise", "isCorrect": False},
                        {"text": "Un produit biologique", "isCorrect": False},
                        {"text": "Un produit fabriqué en France", "isCorrect": False}
                    ],
                    "correction": "Le Label Rouge est un signe national français qui atteste que le produit possède des caractéristiques organoleptiques et de production supérieures au produit standard courant (ex: Farine Label Rouge)."
                },
            ]
        }
    }
}