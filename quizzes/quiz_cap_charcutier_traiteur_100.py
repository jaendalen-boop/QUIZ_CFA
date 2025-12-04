quiz_data = {
    "title": "Quiz CAP Charcutier-Traiteur : 100 Questions (Révisions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE, SÉCURITÉ & LOCAUX (HACCP) (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Hygiène, Sécurité & Locaux (HACCP)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est l'objectif principal de l'analyse des dangers et des points critiques pour leur maîtrise (méthode HACCP) ?",
                    "answerOptions": [
                        {"text": "Diminuer le coût des matières premières.", "isCorrect": False},
                        {"text": "Garantir la sécurité et la salubrité des aliments.", "isCorrect": True},
                        {"text": "Augmenter la durée de vie des produits finis.", "isCorrect": False},
                        {"text": "Simplifier les tâches de nettoyage quotidiennes.", "isCorrect": False}
                    ],
                    "correction": "L'**HACCP** (Hazard Analysis Critical Control Point) est un système préventif visant à identifier, évaluer et maîtriser les dangers significatifs au regard de la **sécurité des aliments** (biologiques, chimiques, physiques). C'est le fondement de l'hygiène alimentaire."
                },
                {
                    "questionNumber": 2,
                    "question": "Selon le Plan de Maîtrise Sanitaire (PMS), quelle est la fréquence minimale recommandée pour le contrôle des températures des enceintes réfrigérées ?",
                    "answerOptions": [
                        {"text": "Une fois par semaine.", "isCorrect": False},
                        {"text": "Deux fois par jour (matin et soir).", "isCorrect": True},
                        {"text": "Une fois par service (midi et soir).", "isCorrect": False},
                        {"text": "Une fois par jour au début de la journée.", "isCorrect": False}
                    ],
                    "correction": "Le **contrôle des températures** doit être effectué au **minimum deux fois par jour** et enregistré pour s'assurer que la chaîne du froid est respectée de manière constante."
                },
                {
                    "questionNumber": 3,
                    "question": "Que doit-on utiliser pour désinfecter les surfaces de travail après un nettoyage ?",
                    "answerOptions": [
                        {"text": "Un détergent seul.", "isCorrect": False},
                        {"text": "Un désinfectant approprié.", "isCorrect": True},
                        {"text": "De l'eau chaude et du sel.", "isCorrect": False},
                        {"text": "Un désinfectant mélangé au détergent (produit deux-en-un).", "isCorrect": False}
                    ],
                    "correction": "Le processus classique est **Nettoyage** (avec un détergent) pour enlever les salissures visibles, suivi du **Rinçage**, puis de la **Désinfection** (avec un produit bactéricide, fongicide, etc.) pour tuer les micro-organismes. L'efficacité du désinfectant est souvent diminuée par la présence de détergent."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la température maximale autorisée pour les préparations froides de charcuterie-traiteur (salades composées, sandwiches, etc.) au moment de la vente ?",
                    "answerOptions": [
                        {"text": "+2 °C", "isCorrect": False},
                        {"text": "+4 °C", "isCorrect": True},
                        {"text": "+6 °C", "isCorrect": False},
                        {"text": "+8 °C", "isCorrect": False}
                    ],
                    "correction": "La température réglementaire pour les produits très périssables (comme les préparations charcutières froides, les plats cuisinés réfrigérés) est de **+4 °C** (avec une tolérance souvent admise jusqu'à +6 °C en vitrine, mais +4 °C est la norme de conservation idéale)."
                },
                {
                    "questionNumber": 5,
                    "question": "Qu'appelle-t-on la 'marche en avant' dans l'agencement des locaux de charcuterie-traiteur ?",
                    "answerOptions": [
                        {"text": "La progression du personnel de l'entrée à la sortie.", "isCorrect": False},
                        {"text": "Le flux continu du produit du secteur sale au secteur propre.", "isCorrect": True},
                        {"text": "L'organisation des livraisons en fonction des commandes clients.", "isCorrect": False},
                        {"text": "Le respect des étapes de la recette sans retour en arrière.", "isCorrect": False}
                    ],
                    "correction": "La **marche en avant** est un principe essentiel de l'hygiène. Elle garantit qu'un produit propre ou fini ne revienne jamais en contact avec une zone sale ou une matière première brute, évitant ainsi la **contamination croisée**."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le risque le plus important lié à une rupture de la chaîne du froid sur des produits cuits, tranchés et prêts à consommer ?",
                    "answerOptions": [
                        {"text": "La perte de texture du produit.", "isCorrect": False},
                        {"text": "La multiplication rapide des bactéries pathogènes.", "isCorrect": True},
                        {"text": "La décoloration prématurée de la viande.", "isCorrect": False},
                        {"text": "L'altération du goût par oxydation.", "isCorrect": False}
                    ],
                    "correction": "Une température trop élevée favorise la **multiplication des micro-organismes**, notamment des bactéries pathogènes (comme *Listeria* ou *Salmonella*), rendant le produit dangereux pour la consommation."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est la zone de température où la croissance microbienne est la plus rapide (appelée 'Danger Zone') ?",
                    "answerOptions": [
                        {"text": "De -5 °C à 0 °C.", "isCorrect": False},
                        {"text": "De +10 °C à +63 °C.", "isCorrect": True},
                        {"text": "De +65 °C à +85 °C.", "isCorrect": False},
                        {"text": "Au-delà de +100 °C.", "isCorrect": False}
                    ],
                    "correction": "La zone de danger se situe généralement entre **+10 °C et +63 °C**. C'est dans cet intervalle que les bactéries se développent le plus rapidement. Il faut minimiser le temps de passage des aliments dans cette zone."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel document doit être consulté pour connaître les risques spécifiques et les mesures de premiers secours liés à un produit chimique de nettoyage ou de désinfection ?",
                    "answerOptions": [
                        {"text": "Le registre des clients.", "isCorrect": False},
                        {"text": "La Fiche de Données de Sécurité (FDS).", "isCorrect": True},
                        {"text": "Le Plan de Maîtrise Sanitaire (PMS).", "isCorrect": False},
                        {"text": "Le cahier de recettes.", "isCorrect": False}
                    ],
                    "correction": "La **Fiche de Données de Sécurité (FDS)** est un document légal et obligatoire qui accompagne les produits chimiques. Elle détaille leur composition, leurs dangers (toxicité, corrosivité) et les procédures à suivre en cas d'accident."
                },
                {
                    "questionNumber": 9,
                    "question": "Dans le cadre de l'hygiène du personnel, pourquoi le port de bijoux (bagues, bracelets) est-il strictement interdit en zone de production ?",
                    "answerOptions": [
                        {"text": "Risque de vol ou de perte des objets.", "isCorrect": False},
                        {"text": "Risque d'usure prématurée des bijoux.", "isCorrect": False},
                        {"text": "Risque de contamination bactérienne ou de chute de corps étranger.", "isCorrect": True},
                        {"text": "Risque d'interférence avec les machines électroniques.", "isCorrect": False}
                    ],
                    "correction": "Les bijoux, en particulier les bagues et montres, sont des **niches à bactéries** (zone difficile à nettoyer). Ils constituent également un risque de contamination physique (chute d'un débris de bijou dans la préparation)."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la température de refroidissement des plats cuisinés qui doit être atteinte 'à cœur' en moins de deux heures, après la fin de cuisson ?",
                    "answerOptions": [
                        {"text": "+63 °C à +10 °C.", "isCorrect": True},
                        {"text": "+100 °C à +4 °C.", "isCorrect": False},
                        {"text": "+75 °C à +12 °C.", "isCorrect": False},
                        {"text": "+50 °C à +8 °C.", "isCorrect": False}
                    ],
                    "correction": "La réglementation impose un refroidissement rapide des plats chauds. La température doit passer de **+63 °C à +10 °C à cœur en moins de deux heures** afin de traverser très rapidement la 'Danger Zone' et limiter la croissance bactérienne."
                },
                {
                    "questionNumber": 11,
                    "question": "Dans l'atelier de charcuterie, quel équipement est destiné à prévenir les risques liés à la coupure des mains ?",
                    "answerOptions": [
                        {"text": "Les chaussures de sécurité.", "isCorrect": False},
                        {"text": "Le tablier en tissu imperméable.", "isCorrect": False},
                        {"text": "Le gant de cotte de mailles.", "isCorrect": True},
                        {"text": "Le masque anti-projection.", "isCorrect": False}
                    ],
                    "correction": "Le **gant de cotte de mailles** (souvent en acier inoxydable) est un Équipement de Protection Individuelle (EPI) essentiel lors des opérations de désossage, parage ou utilisation de couteaux puissants, afin de protéger l'opérateur contre les blessures graves."
                },
                {
                    "questionNumber": 12,
                    "question": "Après l'utilisation d'une chambre froide, pourquoi est-il important de refermer la porte rapidement ?",
                    "answerOptions": [
                        {"text": "Pour maintenir la pression interne.", "isCorrect": False},
                        {"text": "Pour éviter la formation d'odeurs.", "isCorrect": False},
                        {"text": "Pour éviter la condensation et la formation de givre.", "isCorrect": True},
                        {"text": "Pour bloquer la sortie des gaz réfrigérants.", "isCorrect": False}
                    ],
                    "correction": "L'air ambiant chaud et humide de l'atelier, lorsqu'il rentre en contact avec l'air froid de la chambre, provoque de la **condensation** (gouttelettes d'eau, risque microbien) et du **givre** sur les évaporateurs, ce qui réduit l'efficacité frigorifique et nécessite un dégivrage plus fréquent."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel micro-organisme est particulièrement redouté dans les produits de charcuterie traiteur car il se développe même à basse température (froid positif) ?",
                    "answerOptions": [
                        {"text": "La Salmonelle (Salmonella).", "isCorrect": False},
                        {"text": "La Listeria (Listeria monocytogenes).", "isCorrect": True},
                        {"text": "L'Escherichia Coli (E. Coli).", "isCorrect": False},
                        {"text": "Le Staphylocoque doré.", "isCorrect": False}
                    ],
                    "correction": "La bactérie **Listeria monocytogenes** est un germe psychrophile, c'est-à-dire qu'elle est capable de se multiplier même aux températures de réfrigération (+4°C), ce qui la rend dangereuse dans les produits prêts à consommer."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel type de conditionnement est utilisé pour prolonger significativement la durée de vie des produits en empêchant la croissance de la plupart des micro-organismes aérobies ?",
                    "answerOptions": [
                        {"text": "Conditionnement sous atmosphère protectrice (MAP).", "isCorrect": False},
                        {"text": "Conditionnement sous-vide.", "isCorrect": True},
                        {"text": "Conditionnement en barquette ouverte.", "isCorrect": False},
                        {"text": "Conditionnement par film étirable simple.", "isCorrect": False}
                    ],
                    "correction": "Le **conditionnement sous-vide** consiste à retirer l'air de l'emballage. L'absence d'oxygène limite la croissance des bactéries aérobies (qui ont besoin d'oxygène) et ralentit l'oxydation, prolongeant ainsi la DLC."
                },
                {
                    "questionNumber": 15,
                    "question": "Dans l'aménagement des vestiaires du personnel, quelle séparation est essentielle pour respecter les normes d'hygiène ?",
                    "answerOptions": [
                        {"text": "Une séparation entre les hommes et les femmes.", "isCorrect": False},
                        {"text": "Une séparation entre les vêtements de travail et les effets personnels.", "isCorrect": True},
                        {"text": "Une séparation entre les vestiaires et les toilettes.", "isCorrect": False},
                        {"text": "Une séparation entre les chaussures et les couvre-chefs.", "isCorrect": False}
                    ],
                    "correction": "Les vestiaires doivent être équipés de **doubles armoires (ou doubles casiers)** afin que les vêtements de ville (source potentielle de contamination) ne soient jamais en contact avec les tenues de travail propres (la blouse, le pantalon professionnel, etc.)."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est l'obligation principale concernant la traçabilité des ingrédients reçus dans l'atelier ?",
                    "answerOptions": [
                        {"text": "Les jeter immédiatement après utilisation.", "isCorrect": False},
                        {"text": "Conserver les étiquettes de DLC/DLUO et les bons de livraison.", "isCorrect": True},
                        {"text": "Les enregistrer uniquement s'ils sont défectueux.", "isCorrect": False},
                        {"text": "Les conserver pendant 48 heures.", "isCorrect": False}
                    ],
                    "correction": "La **traçabilité** 'en amont' (ce qui entre) et 'en aval' (ce qui sort) est vitale. Il faut conserver les documents (bons, étiquettes, enregistrements de lot) permettant de retracer l'origine des ingrédients et le devenir des produits finis en cas de problème sanitaire."
                },
                {
                    "questionNumber": 17,
                    "question": "Que signifie le sigle 'DLC' apposé sur un produit de charcuterie ?",
                    "answerOptions": [
                        {"text": "Date Limite de Consommation.", "isCorrect": True},
                        {"text": "Durée Longue de Conservation.", "isCorrect": False},
                        {"text": "Date Limite de Congélation.", "isCorrect": False},
                        {"text": "Durée Légale de Commercialisation.", "isCorrect": False}
                    ],
                    "correction": "La **DLC** (Date Limite de Consommation) est une date impérative : le produit est considéré comme dangereux pour la santé après cette date et ne doit plus être consommé. Elle est utilisée pour les produits microbiologiquement périssables (comme la charcuterie fraîche)."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel type de nettoyage doit-on réaliser en cas de déversement de sang ou de jus de viande sur le sol ?",
                    "answerOptions": [
                        {"text": "Un simple balayage humide.", "isCorrect": False},
                        {"text": "Un nettoyage et une désinfection immédiate de la zone.", "isCorrect": True},
                        {"text": "Attendre la fin du service pour traiter l'incident.", "isCorrect": False},
                        {"text": "Appliquer seulement de la sciure pour absorber.", "isCorrect": False}
                    ],
                    "correction": "Les fluides corporels (sang, jus de viande) sont des milieux de culture idéaux pour les bactéries. Leur déversement nécessite une **intervention immédiate** (Nettoyage - Rinçage - Désinfection) pour éliminer le danger de contamination croisée ou de glissade."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le risque physique le plus courant lié à l'utilisation d'un poussoir ou d'un mélangeur en charcuterie ?",
                    "answerOptions": [
                        {"text": "Brûlures dues à la chaleur.", "isCorrect": False},
                        {"text": "Chutes sur sol glissant.", "isCorrect": False},
                        {"text": "Écrasement ou happement des mains.", "isCorrect": True},
                        {"text": "Inhalation de vapeurs toxiques.", "isCorrect": False}
                    ],
                    "correction": "Les machines comme les poussoirs, hachoirs ou mélangeurs comportent des pièces mobiles et puissantes. Le risque majeur est le **happement** des mains ou des vêtements. D'où l'importance des dispositifs de sécurité (capotages, arrêts d'urgence)."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est l'équipement de protection individuelle (EPI) indispensable pour toute manipulation de produits gras ou humides en atelier de production ?",
                    "answerOptions": [
                        {"text": "Le filet à cheveux uniquement.", "isCorrect": False},
                        {"text": "Les manchettes de protection.", "isCorrect": False},
                        {"text": "Le tablier en plastique ou polyuréthane", "isCorrect": True},
                        {"text": "Les gants en latex non poudrés.", "isCorrect": False}
                    ],
                    "correction": "Le **tablier en plastique, PVC ou polyuréthane** protège l'opérateur (et ses vêtements propres) contre les projections de graisses, de sang, de saumures ou d'eau, assurant une barrière contre l'humidité et la souillure."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : MATIÈRES PREMIÈRES : VIANDE ET ADDITIFS (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Matières Premières : Viande et Additifs",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le rôle principal du sel nitrité (sel de salaison) dans la fabrication des charcuteries cuites ?",
                    "answerOptions": [
                        {"text": "Accélérer la cuisson.", "isCorrect": False},
                        {"text": "Émulsifier la graisse.", "isCorrect": False},
                        {"text": "Fixer la couleur rose et inhiber la bactérie *Clostridium botulinum*.", "isCorrect": True},
                        {"text": "Rendre la viande plus tendre.", "isCorrect": False}
                    ],
                    "correction": "Le **sel nitrité** (un mélange de sel commun et de nitrite de sodium/potassium) est crucial. Il confère la couleur rose caractéristique aux charcuteries et, surtout, il a une puissante action antibactérienne contre la toxine du **botulisme** (*C. botulinum*), un danger majeur en salaison."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel terme technique désigne l'opération qui consiste à éliminer les tendons, les aponévroses et l'excès de gras visible avant l'utilisation d'une pièce de viande en charcuterie ?",
                    "answerOptions": [
                        {"text": "Le parage.", "isCorrect": True},
                        {"text": "Le dénerverage.", "isCorrect": False},
                        {"text": "Le dégraissage.", "isCorrect": False},
                        {"text": "Le blanchiment.", "isCorrect": False}
                    ],
                    "correction": "Le **parage** est l'opération préliminaire qui prépare la viande ou les abats en retirant les parties non comestibles ou indésirables (aponévroses, gros vaisseaux, cartilages) pour obtenir une matière première nette et de qualité constante."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel type de viande est traditionnellement utilisé pour la fabrication de la farce fine dans des produits comme les mousses ou les galantines ?",
                    "answerOptions": [
                        {"text": "Viande de porc très grasse (poitrine).", "isCorrect": False},
                        {"text": "Maigre de veau ou de volaille (viande blanche).", "isCorrect": True},
                        {"text": "Maigre de bœuf persillé.", "isCorrect": False},
                        {"text": "Abats rouges (foie, cœur).", "isCorrect": False}
                    ],
                    "correction": "La **farce fine** (ou farce mousseline) est généralement élaborée à partir de **viande maigre et blanche** (veau, volaille, lapin) car elle est peu colorée et son goût neutre se prête mieux à l'ajout de crème et d'œufs pour une texture délicate et homogène."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle de la glace ou de l'eau glacée dans la fabrication des émulsions charcutières (comme les saucissons de Paris ou les saucisses de Francfort) ?",
                    "answerOptions": [
                        {"text": "Hydrater les épices.", "isCorrect": False},
                        {"text": "Permettre l'extraction des protéines (myosine) et réguler la température.", "isCorrect": True},
                        {"text": "Rendre le produit final plus léger.", "isCorrect": False},
                        {"text": "Dissoudre le sel plus rapidement.", "isCorrect": False}
                    ],
                    "correction": "La glace est essentielle pour deux raisons : 1) Elle maintient la température en dessous de **10-12 °C** pour éviter que la graisse ne fonde. 2) Le froid permet l'**extraction des protéines myofibrillaires** (notamment la myosine) qui sont les agents liants de l'émulsion viande-graisse-eau."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel additif, souvent utilisé comme antioxydant (E300), contribue à stabiliser la couleur et accélérer la réaction du nitrite dans les produits salés ?",
                    "answerOptions": [
                        {"text": "Le phosphate.", "isCorrect": False},
                        {"text": "L'acide ascorbique (ou vitamine C).", "isCorrect": True},
                        {"text": "Le glutamate monosodique (MSG).", "isCorrect": False},
                        {"text": "Le carraghénane.", "isCorrect": False}
                    ],
                    "correction": "L'**Acide Ascorbique** (E300) ou l'Ascorbate de Sodium (E301) sont des antioxydants qui jouent un rôle de catalyseur. Ils réduisent le nitrite en oxyde nitrique plus rapidement, stabilisant ainsi la couleur rose (nitrosomyoglobine) et protégeant de l'oxydation."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est l'effet d'un excès de sel dans une farce ou une mêlée de charcuterie ?",
                    "answerOptions": [
                        {"text": "Une augmentation de la durée de vie sans altération du goût.", "isCorrect": False},
                        {"text": "Une texture finale sèche et friable (dénaturation des protéines).", "isCorrect": True},
                        {"text": "Un manque de cohésion de l'émulsion.", "isCorrect": False},
                        {"text": "Une coloration plus pâle du produit.", "isCorrect": False}
                    ],
                    "correction": "Bien que le sel soit nécessaire à l'extraction des protéines, un excès de sel peut provoquer une **dénaturation trop rapide** de ces protéines. Cela conduit à un dessèchement (saumure trop forte) et à une perte de la capacité de rétention d'eau, rendant la texture finale sèche et peu appétissante."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel élément nutritif est l'agent liant fondamental qui permet la cohésion d'une farce de charcuterie cuite ?",
                    "answerOptions": [
                        {"text": "Le gras (lipides).", "isCorrect": False},
                        {"text": "Les fibres (glucides).", "isCorrect": False},
                        {"text": "Les protéines.", "isCorrect": True},
                        {"text": "L'eau (humidité).", "isCorrect": False}
                    ],
                    "correction": "Ce sont les **protéines** de la viande, principalement la **myosine** et l'actine (protéines myofibrillaires), qui, sous l'action du sel et du travail mécanique (cutter/mélangeur) et de la chaleur (cuisson), forment un gel qui lie l'eau et la graisse, assurant la cohésion et la tenue du produit."
                },
                {
                    "questionNumber": 28,
                    "question": "À quoi correspond le terme 'couenne fraîche' dans la préparation des terrines ou des pâtés ?",
                    "answerOptions": [
                        {"text": "La peau du porc blanchie, sans gras ni poils.", "isCorrect": True},
                        {"text": "La barde utilisée pour chemiser les moules.", "isCorrect": False},
                        {"text": "Le gras dorsal du porc.", "isCorrect": False},
                        {"text": "Le boyau naturel utilisé pour l'embossage.", "isCorrect": False}
                    ],
                    "correction": "La **couenne fraîche** est la peau du porc. Elle est blanchie (cuite partiellement puis refroidie) puis parfois hachée très finement. Riche en **collagène**, elle est utilisée comme liant naturel pour apporter du fondant et du corps aux farces après cuisson."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel terme désigne le tissu conjonctif riche en collagène, souvent présent autour des muscles et qui se transforme en gélatine à la cuisson ?",
                    "answerOptions": [
                        {"text": "Le cartilage.", "isCorrect": False},
                        {"text": "L'aponévrose (ou tendon).", "isCorrect": True},
                        {"text": "La moelle.", "isCorrect": False},
                        {"text": "Le nerf.", "isCorrect": False}
                    ],
                    "correction": "L'**aponévrose** (membrane fibreuse) et les **tendons** sont principalement constitués de collagène. C'est le collagène qui, sous l'effet de la chaleur humide (longue cuisson), se solubilise et donne la **gélatine**, essentielle pour le liant et la texture des produits de traiteur."
                },
                {
                    "questionNumber": 30,
                    "question": "Pourquoi est-il déconseillé d'utiliser de l'huile d'olive pure pour rissoler les viandes destinées aux plats cuisinés avant de mouiller ?",
                    "answerOptions": [
                        {"text": "Elle est trop acide.", "isCorrect": False},
                        {"text": "Son point de fumée est relativement bas, elle peut brûler et donner un goût amer.", "isCorrect": True},
                        {"text": "Elle est trop liquide.", "isCorrect": False},
                        {"text": "Elle ne colore pas suffisamment la viande.", "isCorrect": False}
                    ],
                    "correction": "L'**huile d'olive** vierge a un point de fumée plus bas que d'autres graisses (comme l'huile de tournesol ou le beurre clarifié). À haute température, elle se dégrade et **fume**, ce qui génère des composés amers et cancérigènes."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est l'additif le plus couramment utilisé pour améliorer la capacité des viandes à retenir l'eau (rétention d'eau) dans les produits cuits ?",
                    "answerOptions": [
                        {"text": "Les nitrates.", "isCorrect": False},
                        {"text": "Les phosphates.", "isCorrect": True},
                        {"text": "Les sulfates.", "isCorrect": False},
                        {"text": "Les glutamates.", "isCorrect": False}
                    ],
                    "correction": "Les **phosphates** (E450, E451, E452) sont utilisés pour augmenter le pH de la viande. Cela augmente la capacité des protéines à se lier à l'eau, ce qui réduit la perte de poids à la cuisson et améliore le moelleux du produit fini."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel paramètre physique, mesuré à l'aide d'un densimètre lors de la préparation d'une saumure, est exprimé en degrés Baumé (°Bé) ?",
                    "answerOptions": [
                        {"text": "Le pH du mélange.", "isCorrect": False},
                        {"text": "Le taux d'acidité.", "isCorrect": False},
                        {"text": "La concentration en sel.", "isCorrect": True},
                        {"text": "La pression osmotique.", "isCorrect": False}
                    ],
                    "correction": "Le **densimètre** mesure la densité du liquide. Cette densité est ensuite convertie en **degrés Baumé (°Bé)** ou en pourcentage massique, représentant la **concentration en sel** de la saumure. Cette mesure est vitale pour la maîtrise de la salaison."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle coupe de la carcasse porcine, située sous les côtes, fournit la matière première principalement utilisée pour la fabrication des lardons et du bacon ?",
                    "answerOptions": [
                        {"text": "L'Épaule (Plat de côtes).", "isCorrect": False},
                        {"text": "L'Échine.", "isCorrect": False},
                        {"text": "Le Flanc ou Poitrine.", "isCorrect": True},
                        {"text": "Le Filet.", "isCorrect": False}
                    ],
                    "correction": "La **poitrine** (ou flanc) est la partie ventrale du porc, située sous la cage thoracique. Elle est caractérisée par l'alternance de couches de gras et de maigre, ce qui la rend idéale pour la salaison, la production de lardons et de bacon."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le risque si une saumure d'injection est préparée à une température trop élevée ?",
                    "answerOptions": [
                        {"text": "Une coagulation prématurée des protéines en surface.", "isCorrect": True},
                        {"text": "Une action insuffisante des nitrites.", "isCorrect": False},
                        {"text": "Un goût final trop salé.", "isCorrect": False},
                        {"text": "Une coloration grise de la viande.", "isCorrect": False}
                    ],
                    "correction": "Si la saumure est trop chaude (idéalement elle doit être entre 2 °C et 4 °C), elle peut provoquer une **cuisson ou dénaturation partielle** des protéines en surface de la viande au point d'injection. Ces protéines coagulées bouchent les canaux et empêchent une bonne diffusion de la saumure."
                },
                {
                    "questionNumber": 35,
                    "question": "Dans la charcuterie, qu'appelle-t-on un 'assaisonnement composite' ?",
                    "answerOptions": [
                        {"text": "Un assaisonnement contenant uniquement du sel et du poivre.", "isCorrect": False},
                        {"text": "Un mélange d'épices et d'aromates spécifiques déjà préparé (prêt à l'emploi).", "isCorrect": True},
                        {"text": "Un mélange d'assaisonnement et d'additifs (nitrite, phosphate).", "isCorrect": False},
                        {"text": "Un assaisonnement liquide (type saumure).", "isCorrect": False}
                    ],
                    "correction": "L'**assaisonnement composite** est un mélange d'épices, d'aromates, parfois de liants ou d'additifs, préparé à l'avance par le fournisseur pour garantir un profil aromatique constant et standardisé dans les fabrications."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel ingrédient est essentiel pour réaliser la **panade** dans la fabrication de certaines terrines ou pâtés, et quel est son rôle ?",
                    "answerOptions": [
                        {"text": "Le vin blanc, pour la saveur.", "isCorrect": False},
                        {"text": "Le foie de volaille, pour la couleur.", "isCorrect": False},
                        {"text": "Le pain de mie trempé dans du lait, comme agent de liaison", "isCorrect": True},
                        {"text": "La gélatine en poudre, pour la tenue.", "isCorrect": False}
                    ],
                    "correction": "La **panade** est un mélange de féculent (pain de mie, mie de pain) trempé dans un liquide (lait, bouillon) ou un roux. Elle est ajoutée à la farce pour **augmenter sa capacité de rétention d'eau** et donner du moelleux au produit fini."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle technique permet d'utiliser de la viande de catégorie inférieure (moins noble) pour obtenir une farce fine et homogène avec une bonne tenue ?",
                    "answerOptions": [
                        {"text": "L'attendrissement mécanique.", "isCorrect": False},
                        {"text": "Le **cutterage** (ou passage au cutter-émulsionneur).", "isCorrect": True},
                        {"text": "La maturation.", "isCorrect": False},
                        {"text": "La simple découpe au couteau.", "isCorrect": False}
                    ],
                    "correction": "Le **cutter** est une machine munie de lames rotatives très rapides qui permet de réaliser une **émulsion très fine** de la viande, de la graisse et de l'eau. Le cutterage permet d'extraire les protéines liantes, ce qui améliore la texture et la cohésion, même avec des viandes moins persillées."
                },
                {
                    "questionNumber": 38,
                    "question": "En traiteur, quel est l'intérêt principal d'utiliser des **œufs entiers** dans la préparation de l'appareil (mélange) d'une quiche ou d'une tarte salée ?",
                    "answerOptions": [
                        {"text": "Apporter uniquement de la couleur.", "isCorrect": False},
                        {"text": "Servir d'agent de liaison et de coagulation à la chaleur.", "isCorrect": True},
                        {"text": "Augmenter le volume de la garniture.", "isCorrect": False},
                        {"text": "Diminuer le temps de cuisson.", "isCorrect": False}
                    ],
                    "correction": "L'œuf est un agent de **liaison** (ou de coagulation). Sous l'effet de la chaleur, les protéines de l'œuf coagulent et solidifient l'appareil liquide (mélange crème/lait), permettant à la garniture de la quiche ou de la tarte de se tenir."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle matière première est exclusivement réservée à la fabrication des rillettes du Mans selon la réglementation de l'IGP (Indication Géographique Protégée) ?",
                    "answerOptions": [
                        {"text": "L'échine de porc.", "isCorrect": False},
                        {"text": "La longe de porc.", "isCorrect": False},
                        {"text": "Le gras et le maigre des morceaux de porc (hors tête et abats).", "isCorrect": True},
                        {"text": "Le jambon de porc uniquement.", "isCorrect": False}
                    ],
                    "correction": "Les **Rillettes du Mans (IGP)** sont soumises à un cahier des charges strict. Elles doivent être fabriquées exclusivement à partir de **morceaux de porc** (maigre et gras), avec une interdiction formelle d'utiliser la tête, le couenne ou les abats dans la mêlée."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel terme désigne le boyau naturel le plus fréquemment utilisé pour l'embossage de petites saucisses crues (type chipolatas ou saucisses de Toulouse) ?",
                    "answerOptions": [
                        {"text": "Le fuseau de porc.", "isCorrect": False},
                        {"text": "Le menu de mouton.", "isCorrect": True},
                        {"text": "Le chaudin de porc.", "isCorrect": False},
                        {"text": "La baudruche de bœuf.", "isCorrect": False}
                    ],
                    "correction": "Le **menu de mouton** (intestin grêle du mouton ou de la chèvre) est le plus fin et le plus délicat des boyaux. Il est idéal pour les petites charcuteries fraîches crues (chipolatas, merguez) car il est discret et facile à croquer."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : TECHNIQUES DE BASE EN CHARCUTERIE (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Techniques de Base en Charcuterie",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Qu'appelle-t-on le *dégorgeage* des abats blancs, comme les cervelles ou les ris de veau, avant leur cuisson ?",
                    "answerOptions": [
                        {"text": "L'élimination du gras superficiel.", "isCorrect": False},
                        {"text": "La mise en trempe dans de l'eau froide pour éliminer les impuretés et le sang.", "isCorrect": True},
                        {"text": "Le fait de les faire bouillir rapidement.", "isCorrect": False},
                        {"text": "Le retrait des membranes fibreuses.", "isCorrect": False}
                    ],
                    "correction": "Le **dégorgeage** consiste à laisser tremper les abats (cervelle, rognons, ris) dans de l'**eau froide** et vinaigrée ou salée pendant quelques heures. Cette opération permet d'extraire les résidus de sang et d'impuretés qui pourraient altérer la saveur et l'aspect final."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est l'intérêt d'utiliser une *barde* de porc (feuille de gras) pour chemiser l'intérieur d'un moule avant d'y placer une farce de pâté ou de terrine ?",
                    "answerOptions": [
                        {"text": "Diminuer le temps de cuisson.", "isCorrect": False},
                        {"text": "Empêcher l'assaisonnement de s'échapper.", "isCorrect": False},
                        {"text": "Maintenir l'humidité de la farce et faciliter le démoulage.", "isCorrect": True},
                        {"text": "Apporter une saveur très fumée.", "isCorrect": False}
                    ],
                    "correction": "La **barde** (une fine tranche de gras dorsal) est utilisée pour **chemiser** les pâtés. Elle protège la farce de la chaleur sèche du four, empêche le dessèchement de la périphérie et, après cuisson, le gras solidifié facilite le démoulage."
                },
                {
                    "questionNumber": 43,
                    "question": "Lors de l'embossage d'une saucisse, que risque-t-on si la farce est trop lâchement tassée dans le boyau ?",
                    "answerOptions": [
                        {"text": "Le boyau éclate à la cuisson.", "isCorrect": False},
                        {"text": "Des poches d'air se forment, favorisant l'oxydation et l'altération bactérienne.", "isCorrect": True},
                        {"text": "Le produit final est trop sec.", "isCorrect": False},
                        {"text": "La couleur ne se fixe pas correctement.", "isCorrect": False}
                    ],
                    "correction": "L'embossage doit être ferme pour que la farce adhère bien au boyau. Un **embossage lâche** laisse des **bulles d'air** à l'intérieur, ce qui favorise la croissance de micro-organismes aérobies et conduit à une mauvaise conservation et une mauvaise fixation de la couleur."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel ingrédient, souvent utilisé pour la préparation de l'appareil à crépinette, permet de 'coller' la farce entre les deux couches de crépine ?",
                    "answerOptions": [
                        {"text": "Le gros sel.", "isCorrect": False},
                        {"text": "Le jaune d'œuf.", "isCorrect": True},
                        {"text": "La chapelure sèche.", "isCorrect": False},
                        {"text": "L'eau-de-vie.", "isCorrect": False}
                    ],
                    "correction": "Le **jaune d'œuf** (ou parfois l'œuf entier) agit comme un **liant** grâce à ses protéines qui coagulent à la cuisson. Il permet de s'assurer que la farce (hachée ou mêlée) reste bien compacte et solidaire de la crépine pendant la cuisson et la dégustation."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le but principal de l'opération de *ficelage* ou de *bridage* d'une pièce de viande avant cuisson ou salaison ?",
                    "answerOptions": [
                        {"text": "Décorer la pièce pour la vente.", "isCorrect": False},
                        {"text": "Maintenir une forme régulière pour une cuisson uniforme.", "isCorrect": True},
                        {"text": "Empêcher la viande de perdre son gras.", "isCorrect": False},
                        {"text": "Permettre l'injection de saumure.", "isCorrect": False}
                    ],
                    "correction": "Le **ficelage** (ou bridage) est une technique visant à donner ou maintenir une **forme compacte et régulière** à la pièce. Une forme régulière assure que la chaleur pénètre de manière uniforme, garantissant une cuisson à cœur homogène."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment doit-on préchauffer le matériel (saumuroir, ustensiles) avant de réaliser une saumure injectable à froid ?",
                    "answerOptions": [
                        {"text": "Le chauffer à 60 °C pour stériliser.", "isCorrect": False},
                        {"text": "Le refroidir au maximum.", "isCorrect": True},
                        {"text": "Le laisser à température ambiante.", "isCorrect": False},
                        {"text": "Le rincer à l'eau très chaude.", "isCorrect": False}
                    ],
                    "correction": "La saumure d'injection doit être maintenue entre **2 °C et 4 °C**. Il est donc essentiel de refroidir tous les ustensiles (cuves, mélangeurs) avant l'opération pour éviter d'augmenter la température de la saumure et de compromettre son efficacité ou la qualité de la viande."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est la principale fonction de la **crépine de porc** (poche graisseuse fine) utilisée en charcuterie et traiteur ?",
                    "answerOptions": [
                        {"text": "Servir d'assaisonnement.", "isCorrect": False},
                        {"text": "Remplacer les boyaux naturels.", "isCorrect": False},
                        {"text": "Envelopper des préparations pour les lier et les protéger à la cuisson.", "isCorrect": True},
                        {"text": "Augmenter le poids de la préparation.", "isCorrect": False}
                    ],
                    "correction": "La **crépine** est utilisée comme enveloppe pour des produits tels que les crépinettes, les rôtis farcis ou certains pâtés. Sa structure fine et graisseuse **lie** la farce et la **protège** contre le dessèchement lors de la cuisson."
                },
                {
                    "questionNumber": 48,
                    "question": "Lors de la préparation d'une farce de boudin blanc, comment doit être la viande utilisée (volaille ou veau) par rapport à la graisse ajoutée ?",
                    "answerOptions": [
                        {"text": "La viande doit être très persillée.", "isCorrect": False},
                        {"text": "La viande doit être maigre et la graisse ferme.", "isCorrect": True},
                        {"text": "La viande doit être grasse et la graisse souple.", "isCorrect": False},
                        {"text": "La viande et la graisse doivent être à température ambiante.", "isCorrect": False}
                    ],
                    "correction": "Le **boudin blanc** est une émulsion de type fine. Pour garantir la blancheur et la finesse du produit, on utilise du **maigre** (volaille, veau) auquel on ajoute une **graisse ferme** (gras de porc ou de veau) pour obtenir la texture souhaitée sans excès d'humidité."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est l'effet d'une *maturation* prolongée (plusieurs jours au froid) de la viande avant de la hacher pour une saucisse sèche ?",
                    "answerOptions": [
                        {"text": "Une diminution de la rétention d'eau.", "isCorrect": False},
                        {"text": "Une augmentation de la saveur et de la couleur.", "isCorrect": True},
                        {"text": "Une accélération de la coagulation des protéines.", "isCorrect": False},
                        {"text": "Une destruction totale des bactéries.", "isCorrect": False}
                    ],
                    "correction": "La **maturation** (ou mûrissage) permet aux enzymes naturelles de la viande de dégrader légèrement les protéines. Cela attendrit la viande et développe les **arômes** et la **couleur** (par oxydation de la myoglobine) avant l'assaisonnement et l'embossage."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel procédé de préparation permet d'isoler des aliments de l'air en les submergeant complètement dans une graisse chauffée puis refroidie, comme le saindoux ?",
                    "answerOptions": [
                        {"text": "La pasteurisation.", "isCorrect": False},
                        {"text": "Le fumage à chaud.", "isCorrect": False},
                        {"text": "L'appertisation.", "isCorrect": False},
                        {"text": "L'**enrobage** (ou confit).", "isCorrect": True}
                    ],
                    "correction": "L'**enrobage dans la graisse** (confit) est une technique de conservation ancestrale. La graisse fondue et refroidie forme une couche hermétique qui **isole l'aliment de l'air et de l'humidité**, empêchant la prolifération des bactéries aérobies (qui ont besoin d'oxygène)."
                },
                {
                    "questionNumber": 51,
                    "question": "Lors du hachage de la viande, pourquoi est-il essentiel de maintenir la température de la viande et du matériel très basse (proche de 0 °C) ?",
                    "answerOptions": [
                        {"text": "Pour éviter que le sel ne se dissolve.", "isCorrect": False},
                        {"text": "Pour empêcher la fusion des graisses.", "isCorrect": True},
                        {"text": "Pour garantir la couleur finale.", "isCorrect": False},
                        {"text": "Pour mieux sentir les odeurs de la viande.", "isCorrect": False}
                    ],
                    "correction": "Le hachage, surtout avec des machines puissantes, génère de la chaleur par friction. Cette chaleur risque de faire **fondre le gras**. Une graisse fondue s'émulsionne mal, ce qui conduit à une séparation du gras et à un produit final de mauvaise tenue."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le rôle de la **semoule de riz** ou de la **farine de riz** dans certaines préparations charcutières (comme le boudin noir ou les farces fines) ?",
                    "answerOptions": [
                        {"text": "Rendre la farce plus croustillante.", "isCorrect": False},
                        {"text": "Agir comme agent de liaison et améliorer le rendement en eau.", "isCorrect": True},
                        {"text": "Accélérer la maturation.", "isCorrect": False},
                        {"text": "Augmenter le taux de protéines.", "isCorrect": False}
                    ],
                    "correction": "La **semoule de riz** (ou d'autres féculents) est un agent de **liaison** et de **charge** (réglementé). Elle a une forte capacité d'absorption de l'eau, ce qui permet d'obtenir une texture plus souple, un meilleur rendement (moins de perte à la cuisson) et une meilleure tenue du produit."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est le but de l'opération de *piquage* (ou piquetage) des saucissons avant l'étuvage et le séchage ?",
                    "answerOptions": [
                        {"text": "Injecter l'assaisonnement.", "isCorrect": False},
                        {"text": "Marquer le produit pour l'identification.", "isCorrect": False},
                        {"text": "Permettre l'évacuation de l'air et de l'eau.", "isCorrect": True},
                        {"text": "Accélérer la coloration.", "isCorrect": False}
                    ],
                    "correction": "Le **piquage** consiste à percer le boyau (généralement après embossage) pour faire sortir l'**air** (qui peut provoquer des moisissures) et l'**excès d'eau** (qui doit s'évaporer) lors des phases d'étuvage et de séchage."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'effet d'une cuisson en étuve (chaleur humide) des saucissons après l'embossage, avant le séchage ?",
                    "answerOptions": [
                        {"text": "Durcir rapidement le boyau.", "isCorrect": False},
                        {"text": "Permettre le développement de la flore de surface et la fixation de la couleur.", "isCorrect": True},
                        {"text": "Diminuer l'acidité de la mêlée.", "isCorrect": False},
                        {"text": "Sécher le produit immédiatement.", "isCorrect": False}
                    ],
                    "correction": "L'**étuvage** est une étape chaude et humide cruciale. Elle permet la **fermentation** par les flores (lactobacilles), qui crée l'acidité nécessaire à la conservation et au développement du goût, et elle fixe la couleur rose (nitrosomyoglobine)."
                },
                {
                    "questionNumber": 55,
                    "question": "Comment appelle-t-on le mélange de viande, de gras et d'assaisonnement destiné à être embossé dans un boyau ?",
                    "answerOptions": [
                        {"text": "Le hachis.", "isCorrect": False},
                        {"text": "Le parage.", "isCorrect": False},
                        {"text": "La mêlée.", "isCorrect": True},
                        {"text": "L'appareil.", "isCorrect": False}
                    ],
                    "correction": "La **mêlée** est le nom technique donné à la préparation (viande, gras, sel, épices, additifs) prête à être embossée. C'est l'étape qui précède immédiatement l'utilisation du poussoir ou de l'embosseuse."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel rôle la présence d'amidon ou de féculent (pomme de terre, riz) joue-t-elle dans le boudin noir traditionnel ?",
                    "answerOptions": [
                        {"text": "Il augmente la teneur en fer du produit.", "isCorrect": False},
                        {"text": "Il est utilisé comme agent liant pour éviter la déstructuration.", "isCorrect": True},
                        {"text": "Il rend le boyau plus résistant.", "isCorrect": False},
                        {"text": "Il accélère la coagulation du sang.", "isCorrect": False}
                    ],
                    "correction": "Dans le boudin noir (un produit coagulé par la chaleur), l'amidon ou le féculent est l'agent liant qui agit en synergie avec les protéines du sang et du gras pour assurer une **texture lisse et homogène** et éviter que le produit ne se délite à la coupe."
                },
                {
                    "questionNumber": 57,
                    "question": "En charcuterie sèche, quelle opération est réalisée après le salage pour permettre au sel de pénétrer uniformément dans la masse de la viande ?",
                    "answerOptions": [
                        {"text": "Le fumage.", "isCorrect": False},
                        {"text": "Le **repos** (ou période d'attente/ressuage).", "isCorrect": True},
                        {"text": "Le pochage.", "isCorrect": False},
                        {"text": "Le blanchiment.", "isCorrect": False}
                    ],
                    "correction": "Après le salage (sel sec), un temps de **repos au froid** est nécessaire. Ce temps permet au sel de se dissoudre dans l'eau du muscle et de se diffuser de manière homogène par **osmose** dans toute la pièce, garantissant l'assaisonnement et l'action conservatrice."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le nom de la technique qui consiste à introduire la saumure directement dans la masse musculaire de la pièce de viande à l'aide d'aiguilles ?",
                    "answerOptions": [
                        {"text": "Le saumurage à sec.", "isCorrect": False},
                        {"text": "Le saumurage par barattage.", "isCorrect": False},
                        {"text": "Le saumurage par injection.", "isCorrect": True},
                        {"text": "Le saumurage par immersion.", "isCorrect": False}
                    ],
                    "correction": "Le **saumurage par injection** (ou injection artérielle/intramusculaire) est une technique rapide et très courante. Elle permet une diffusion rapide et uniforme des ingrédients (sel, nitrites, phosphates) au cœur du produit, réduisant le temps de saumurage et augmentant le rendement."
                },
                {
                    "questionNumber": 59,
                    "question": "Que doit-on éviter d'ajouter en trop grande quantité dans une farce destinée à la préparation d'un boudin blanc, car cela nuit à sa finesse ?",
                    "answerOptions": [
                        {"text": "Le lait entier.", "isCorrect": False},
                        {"text": "La crème.", "isCorrect": False},
                        {"text": "L'oignon frais (ou échalote).", "isCorrect": True},
                        {"text": "Le sel.", "isCorrect": False}
                    ],
                    "correction": "Le boudin blanc est une charcuterie fine à la texture lisse. L'ajout d'**oignon** (même cuit) apporte de la texture et un goût fort qui ne correspond pas au profil délicat recherché. Les aromates doivent souvent être infusés dans le lait/la crème puis retirés."
                },
                {
                    "questionNumber": 60,
                    "question": "Quelle opération de préparation est indispensable pour les boyaux naturels avant leur utilisation pour l'embossage ?",
                    "answerOptions": [
                        {"text": "Les faire sécher pendant 24 heures.", "isCorrect": False},
                        {"text": "Les tremper et les rincer longuement dans de l'eau claire et tiède.", "isCorrect": True},
                        {"text": "Les blanchir dans l'eau bouillante.", "isCorrect": False},
                        {"text": "Les fumer pour les assouplir.", "isCorrect": False}
                    ],
                    "correction": "Les boyaux naturels sont conservés dans le sel. Avant utilisation, ils doivent être **trempés, rincés** et parfois brossés pour éliminer l'excès de sel et les impuretés, les réhydrater et leur redonner leur souplesse."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : TRAITEUR : FONDS, SAUCES ET PÂTES (BASES) (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Traiteur : Fonds, Sauces et Pâtes (bases)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel terme culinaire désigne l'ensemble des légumes (oignon, carotte, céleri) taillés en petits dés, utilisés comme base aromatique pour les fonds et les sauces ?",
                    "answerOptions": [
                        {"text": "La mirepoix.", "isCorrect": True},
                        {"text": "La brunoise.", "isCorrect": False},
                        {"text": "La matignon.", "isCorrect": False},
                        {"text": "L'arômate.", "isCorrect": False}
                    ],
                    "correction": "La **mirepoix** est le terme technique pour l'association de légumes aromatiques (souvent oignon, carotte, céleri) taillés en dés. C'est la base de saveur des fonds de cuisson, des bouillons, et de nombreuses sauces."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est l'objectif principal de l'opération de *blanchiment* des os avant de les utiliser pour réaliser un fond blanc ?",
                    "answerOptions": [
                        {"text": "Commencer leur cuisson.", "isCorrect": False},
                        {"text": "Retirer les impuretés, le sang et les résidus qui troubleraient le fond.", "isCorrect": True},
                        {"text": "Les attendrir pour une extraction plus facile.", "isCorrect": False},
                        {"text": "Les saler avant cuisson.", "isCorrect": False}
                    ],
                    "correction": "Le **blanchiment** consiste à plonger les os dans de l'eau froide, porter à ébullition, écumer, puis égoutter et rincer. Cela permet d'éliminer les impuretés (sang, protéines coagulées) et d'assurer la **clarté** du fond blanc."
                },
                {
                    "questionNumber": 63,
                    "question": "Qu'appelle-t-on un **roux blanc** dans l'élaboration des sauces de base en traiteur ?",
                    "answerOptions": [
                        {"text": "Un mélange de beurre et de farine cuit jusqu'à obtenir une couleur dorée.", "isCorrect": False},
                        {"text": "Un mélange d'huile et de maïzena pour lier.", "isCorrect": False},
                        {"text": "Un mélange de beurre et de farine cuit sans coloration.", "isCorrect": True},
                        {"text": "Un mélange de crème et de jaunes d'œufs.", "isCorrect": False}
                    ],
                    "correction": "Le **roux** est une liaison chaude réalisée en cuisant de la farine et une matière grasse (beurre). Un **roux blanc** est cuit juste assez longtemps pour éliminer le goût de cru de la farine, sans prendre de couleur. Il sert de base à la sauce béchamel ou aux veloutés."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel type de fond est traditionnellement utilisé comme base pour la réalisation d'une sauce demi-glace classique ?",
                    "answerOptions": [
                        {"text": "Un fumet de poisson.", "isCorrect": False},
                        {"text": "Un fond blanc de volaille.", "isCorrect": False},
                        {"text": "Un fond brun de veau ou de bœuf.", "isCorrect": True},
                        {"text": "Un bouillon de légumes.", "isCorrect": False}
                    ],
                    "correction": "La **demi-glace** est une sauce brune réduite, très concentrée en saveur. Elle est traditionnellement obtenue à partir d'un **fond brun de veau** (ou bœuf), préalablement coloré par le rôtissage des os et de la garniture aromatique."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le rôle principal de la **liaison** (amidon, roux, œufs, etc.) dans une sauce ?",
                    "answerOptions": [
                        {"text": "Augmenter le temps de conservation.", "isCorrect": False},
                        {"text": "Améliorer la brillance.", "isCorrect": False},
                        {"text": "Apporter l'épaisseur et la texture désirées.", "isCorrect": True},
                        {"text": "Accélérer l'évaporation de l'eau.", "isCorrect": False}
                    ],
                    "correction": "La **liaison** est l'action d'épaissir un liquide. Elle permet d'augmenter la viscosité de la sauce pour qu'elle nappe correctement l'aliment (technique du 'nappage à la cuillère')."
                },
                {
                    "questionNumber": 66,
                    "question": "Quelle opération consiste à réduire une sauce ou un fond de cuisson par ébullition pour concentrer ses saveurs ?",
                    "answerOptions": [
                        {"text": "Le blanquettage.", "isCorrect": False},
                        {"text": "La déglace.", "isCorrect": False},
                        {"text": "La réduction.", "isCorrect": True},
                        {"text": "Le mouillage.", "isCorrect": False}
                    ],
                    "correction": "La **réduction** est un processus de cuisson prolongée à feu doux ou moyen. L'évaporation de l'eau concentre les composés aromatiques et le corps du liquide, intensifiant ainsi le goût du fond ou de la sauce."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel type de pâte est utilisée pour chemiser un moule destiné à accueillir une terrine de poisson ou de légumes cuite au four ?",
                    "answerOptions": [
                        {"text": "Une pâte feuilletée.", "isCorrect": False},
                        {"text": "Une pâte à choux.", "isCorrect": False},
                        {"text": "Une pâte brisée (ou pâte à foncer).", "isCorrect": True},
                        {"text": "Une pâte levée.", "isCorrect": False}
                    ],
                    "correction": "La **pâte brisée** (ou pâte à foncer) est une pâte simple, non levée. Elle est idéale pour les fonds de tarte et pour **chemiser** les moules de pâtés en croûte et terrines, car elle est résistante, retient l'humidité et sert de support rigide à la farce."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle technique est utilisée pour incorporer de la gélatine ou de la crème dans un fond de volaille chaud sans provoquer de grumeaux ou de coagulation irrégulière ?",
                    "answerOptions": [
                        {"text": "Le glaçage.", "isCorrect": False},
                        {"text": "Le tempérage.", "isCorrect": True},
                        {"text": "Le bouillonnage.", "isCorrect": False},
                        {"text": "L'émulsion.", "isCorrect": False}
                    ],
                    "correction": "Le **tempérage** consiste à mélanger progressivement une petite quantité du liquide chaud au liquide froid ou à l'agent de liaison (comme la gélatine fondue ou la crème) pour élever doucement sa température. Cela prévient les chocs thermiques qui peuvent causer une coagulation indésirable (grumeaux)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel ingrédient est traditionnellement utilisé pour réaliser le *détrempe* (mélange initial) d'une pâte feuilletée ou d'une pâte levée ?",
                    "answerOptions": [
                        {"text": "Des œufs et du sucre.", "isCorrect": False},
                        {"text": "De la farine et de l'eau (ou du lait).", "isCorrect": True},
                        {"text": "De la semoule et de la graisse.", "isCorrect": False},
                        {"text": "Des noix et des graines.", "isCorrect": False}
                    ],
                    "correction": "La **détrempe** est le premier mélange, la base non grasse des pâtes. Pour la pâte feuilletée ou levée, elle est constituée de **farine**, d'**eau** (ou lait) et, souvent, de sel et d'un peu de matière grasse (pour la pâte feuilletée, le reste du beurre est incorporé par tourage)."
                },
                {
                    "questionNumber": 70,
                    "question": "Dans la réalisation d'une sauce émulsionnée froide (type mayonnaise), quel ingrédient apporte la stabilisation et est l'agent liant essentiel ?",
                    "answerOptions": [
                        {"text": "Le vinaigre.", "isCorrect": False},
                        {"text": "Le sel.", "isCorrect": False},
                        {"text": "Le jaune d'œuf (lécithine).", "isCorrect": True},
                        {"text": "La moutarde.", "isCorrect": False}
                    ],
                    "correction": "C'est la **lécithine** présente dans le **jaune d'œuf** qui est l'agent émulsifiant naturel. Elle permet aux phases aqueuse (vinaigre, eau) et grasse (huile) de se mélanger et de former une émulsion stable (la mayonnaise)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel est le rôle principal de l'ajout de **concentré de tomate** dans la préparation d'un fond brun lié (sauce espagnole, par exemple) ?",
                    "answerOptions": [
                        {"text": "Épaissir le fond.", "isCorrect": False},
                        {"text": "Apporter de l'acidité et améliorer la couleur (rouge-brun).", "isCorrect": True},
                        {"text": "Servir d'agent de conservation.", "isCorrect": False},
                        {"text": "Remplacer les légumes aromatiques.", "isCorrect": False}
                    ],
                    "correction": "Le concentré de tomate (ou la purée de tomate) est souvent pincé avec la mirepoix lors de la préparation des fonds bruns. Son acidité aide à décoller les sucs de cuisson, mais son rôle principal est d'apporter une **couleur riche et appétissante** et un goût légèrement acidulé au fond."
                },
                {
                    "questionNumber": 72,
                    "question": "Comment doit être la température du liquide (lait, fond blanc) ajouté au roux pour éviter la formation de grumeaux lors de la réalisation d'une béchamel ?",
                    "answerOptions": [
                        {"text": "Le liquide doit être à température ambiante.", "isCorrect": False},
                        {"text": "Le liquide doit être très froid.", "isCorrect": False},
                        {"text": "Le liquide doit être chaud (bouillant).", "isCorrect": True},
                        {"text": "La température du liquide n'a aucune importance.", "isCorrect": False}
                    ],
                    "correction": "Pour éviter les grumeaux, il faut créer un **choc thermique** contrôlé. On ajoute un **liquide chaud** (souvent bouillant) sur le roux froid, ou un liquide froid sur le roux chaud, en fouettant vigoureusement."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel terme désigne la masse de graisse et d'impuretés qui remonte à la surface des fonds et des bouillons pendant la cuisson, et que l'on retire ?",
                    "answerOptions": [
                        {"text": "La déglace.", "isCorrect": False},
                        {"text": "L'écume.", "isCorrect": True},
                        {"text": "La panade.", "isCorrect": False},
                        {"text": "La lie.", "isCorrect": False}
                    ],
                    "correction": "L'**écume** (ou mousse) est constituée de protéines coagulées, de gras et d'impuretés. L'écumage est une opération essentielle pour garantir la **clarté** et la saveur pure du fond ou du bouillon."
                },
                {
                    "questionNumber": 74,
                    "question": "Qu'est-ce qui donne à une **pâte feuilletée** sa texture caractéristique (feuilles fines et séparées) ?",
                    "answerOptions": [
                        {"text": "L'ajout d'une grande quantité d'œufs.", "isCorrect": False},
                        {"text": "La présence de levure chimique.", "isCorrect": False},
                        {"text": "L'alternance des couches de détrempe et de beurre après le tourage.", "isCorrect": True},
                        {"text": "Le long temps de repos à température ambiante.", "isCorrect": False}
                    ],
                    "correction": "Le **feuilletage** est créé par l'empilement de couches de **détrempe** (farine/eau) et de **beurre**, séparées par des étapes de **tourage** et de repos au froid. C'est l'eau du beurre qui, en s'évaporant à la cuisson, gonfle les couches et crée les feuillets."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle opération de préparation de la pâte doit être réalisée pour empêcher une pâte à foncer (brisée) de gonfler au four si elle est cuite 'à blanc' ?",
                    "answerOptions": [
                        {"text": "Le pétrissage intensif.", "isCorrect": False},
                        {"text": "Le boulochage.", "isCorrect": False},
                        {"text": "Le piquage.", "isCorrect": True},
                        {"text": "Le rabat.", "isCorrect": False}
                    ],
                    "correction": "Le **piquage** (perforation du fond de pâte avec une fourchette) permet à la vapeur d'eau de s'échapper pendant la cuisson, ce qui empêche la pâte de cloquer, de se déformer et de gonfler excessivement."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment s'appelle l'opération qui consiste à verser de l'eau ou un liquide (vin, bouillon) sur un plat ou un ustensile chaud pour dissoudre et récupérer les sucs de cuisson ?",
                    "answerOptions": [
                        {"text": "Le mouillage.", "isCorrect": False},
                        {"text": "Le chinoisage.", "isCorrect": False},
                        {"text": "La déglace.", "isCorrect": True},
                        {"text": "Le blanchiment.", "isCorrect": False}
                    ],
                    "correction": "La **déglace** est l'opération consistant à dissoudre les sucs de cuisson caramélisés (le **sautage**) au fond d'un récipient chaud à l'aide d'un liquide froid ou tiède. Ces sucs (les saveurs concentrées) sont la base aromatique de nombreuses sauces."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel ingrédient est absolument nécessaire pour la croissance de la levure boulangère dans une pâte levée (comme la pâte à brioche ou à pain) ?",
                    "answerOptions": [
                        {"text": "Le sel.", "isCorrect": False},
                        {"text": "La chaleur et les sucres fermentescibles.", "isCorrect": True},
                        {"text": "Le gras de porc.", "isCorrect": False},
                        {"text": "L'acidité du citron.", "isCorrect": False}
                    ],
                    "correction": "La **levure** est un micro-organisme vivant (champignon) qui se nourrit de **sucres** (ceux naturellement présents dans la farine ou ajoutés). La **chaleur** (température tiède) est nécessaire pour son activation, et la fermentation produit du dioxyde de carbone qui fait lever la pâte."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel terme désigne la fine couche de gélatine ou de graisse qui est versée sur un pâté, une terrine ou un plat froid après cuisson et refroidissement, pour la décoration et la conservation ?",
                    "answerOptions": [
                        {"text": "La panade.", "isCorrect": False},
                        {"text": "L'appareil.", "isCorrect": False},
                        {"text": "La brillance.", "isCorrect": False},
                        {"text": "La gelée (ou le glaçage).", "isCorrect": True}
                    ],
                    "correction": "La **gelée** (ou glaçage à la gelée) est une préparation liquide enrichie en gélatine (collagène). Une fois refroidie, elle se solidifie, protégeant le produit de l'oxydation, lui donnant une belle brillance, et le préservant jusqu'à la consommation."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le rôle de la matière grasse (beurre ou saindoux) dans la réalisation d'une pâte sablée ou d'une pâte sucrée ?",
                    "answerOptions": [
                        {"text": "Augmenter le temps de pétrissage.", "isCorrect": False},
                        {"text": "Empêcher la formation de gluten.", "isCorrect": True},
                        {"text": "Améliorer la rétention d'eau.", "isCorrect": False},
                        {"text": "Accélérer l'évaporation de l'alcool.", "isCorrect": False}
                    ],
                    "correction": "Le gras est **sabler** la farine (mélange initial). En enrobant les particules de farine, il empêche le contact entre l'eau et les protéines, limitant la formation du **gluten**. Cela donne la texture friable et non élastique caractéristique des pâtes dites 'sablées'."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel ustensile de cuisine est utilisé pour filtrer les fonds et les sauces afin d'en éliminer toutes les impuretés et les résidus d'os ou de légumes ?",
                    "answerOptions": [
                        {"text": "Le poussoir.", "isCorrect": False},
                        {"text": "La bassine à rôtir.", "isCorrect": False},
                        {"text": "Le chinois étamine.", "isCorrect": True},
                        {"text": "Le batteur.", "isCorrect": False}
                    ],
                    "correction": "Le **chinois étamine** (ou chinois) est un tamis conique de très fine maille. Il permet l'opération de **chinoisage**, qui garantit une parfaite clarté et un aspect lisse et brillant aux fonds, bouillons et sauces."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : CUISSONS, SALAISON & RÉGLEMENTATION (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Cuissons, Salaison & Réglementation",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'objectif d'une cuisson **lente et douce** (type pochage) pour une charcuterie comme le jambon cuit ou le boudin blanc ?",
                    "answerOptions": [
                        {"text": "Favoriser le développement des saveurs de fumage.", "isCorrect": False},
                        {"text": "Éviter le dessèchement et la perte de gras.", "isCorrect": True},
                        {"text": "Atteindre rapidement les 63 °C à cœur.", "isCorrect": False},
                        {"text": "Ramollir le boyau.", "isCorrect": False}
                    ],
                    "correction": "La cuisson lente et douce (souvent par **pochage** ou en cellule vapeur) permet d'éviter un choc thermique. L'objectif est de minimiser la rétractation des protéines du muscle, ce qui assure un produit **moelleux** et réduit les pertes de poids (eau et gras)."
                },
                {
                    "questionNumber": 82,
                    "question": "Que se passe-t-il si une pâte à frire (beignet, acras) est plongée dans un bain de friture dont la température est trop basse ?",
                    "answerOptions": [
                        {"text": "Elle dore immédiatement sans cuire à cœur.", "isCorrect": False},
                        {"text": "Elle se déchire et se délite.", "isCorrect": False},
                        {"text": "Elle absorbe excessivement la matière grasse.", "isCorrect": True},
                        {"text": "Elle cuit trop rapidement.", "isCorrect": False}
                    ],
                    "correction": "Si la température de l'huile est trop basse (idéalement 170 °C-180 °C), la pâte n'est pas saisie immédiatement. L'eau s'évapore lentement, le produit n'est pas imperméabilisé et la pâte **absorbe trop de graisse**, rendant le beignet lourd et gras."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle doit être la température minimale interne **à cœur** d'une viande de porc cuite (comme un pâté ou une terrine) pour être considérée comme hygiéniquement sûre ?",
                    "answerOptions": [
                        {"text": "60 °C.", "isCorrect": False},
                        {"text": "68 °C.", "isCorrect": True},
                        {"text": "75 °C.", "isCorrect": False},
                        {"text": "80 °C.", "isCorrect": False}
                    ],
                    "correction": "Pour les produits charcutiers cuits, le standard est d'atteindre **68 °C à cœur** et de maintenir cette température quelques minutes. Cette cuisson permet de détruire la plupart des germes pathogènes (y compris les parasites, comme la trichine)."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le rôle principal du **sucre** ajouté à la saumure ou à la mêlée de salaison pour un jambon ou une saucisse sèche ?",
                    "answerOptions": [
                        {"text": "Servir d'agent de conservation anti-bactérien.", "isCorrect": False},
                        {"text": "Faciliter la coagulation des protéines.", "isCorrect": False},
                        {"text": "Contrer l'excès de goût salé et servir de nutriment aux ferments.", "isCorrect": True},
                        {"text": "Améliorer la rétention d'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **sucre** (dextrose, saccharose) sert de **nutriment** aux ferments lactiques (flore utile) qui transforment le sucre en acide lactique. Cette acidification est essentielle pour le goût, la conservation, et la fixation de la couleur. Il atténue également la perception du goût salé."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel terme réglementaire désigne le temps d'utilisation au cours duquel un produit alimentaire non pré-emballé (comme une salade traiteur) conserve toutes ses propriétés après la confection ?",
                    "answerOptions": [
                        {"text": "La DLC (Date Limite de Consommation).", "isCorrect": False},
                        {"text": "La DDM (Date de Durabilité Minimale).", "isCorrect": False},
                        {"text": "La DCL (Date Limite de Consommation).", "isCorrect": False},
                        {"text": "La **DUO (Durée d'Utilisation Optimale)** ou DLC secondaire.", "isCorrect": True}
                    ],
                    "correction": "Pour les produits transformés et reconditionnés à la coupe ou dans l'atelier (comme les salades ou plats cuisinés), on parle de **DLC secondaire** ou **DUO**. Cette date courte est fixée par le professionnel (souvent 3 jours) et doit apparaître clairement. La DLC est pour l'industriel."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est l'effet recherché par l'opération de **fraisage** d'une pièce de viande salée (le fait de frotter la pièce avec du sel sec) ?",
                    "answerOptions": [
                        {"text": "Diminuer le pH de la viande.", "isCorrect": False},
                        {"text": "Assurer la répartition uniforme du sel et démarrer l'osmose.", "isCorrect": True},
                        {"text": "Accélérer le séchage.", "isCorrect": False},
                        {"text": "Supprimer les additifs chimiques.", "isCorrect": False}
                    ],
                    "correction": "Le **fraisage** est l'action de masser le sel sec sur la surface de la viande. Cela garantit une **couverture complète et uniforme** en sel, permettant à l'osmose (le sel pénètre et l'eau sort) de démarrer de manière homogène."
                },
                {
                    "questionNumber": 87,
                    "question": "En matière de congélation, quelle est la température maximale autorisée par la réglementation pour la conservation d'une viande crue ?",
                    "answerOptions": [
                        {"text": "-8 °C.", "isCorrect": False},
                        {"text": "-12 °C.", "isCorrect": False},
                        {"text": "-18 °C.", "isCorrect": True},
                        {"text": "-25 °C.", "isCorrect": False}
                    ],
                    "correction": "La température légale de la **congélation** des aliments est de **-18 °C** ou moins. Cette température arrête la multiplication bactérienne et ralentit les réactions chimiques qui peuvent altérer la qualité du produit (oxydation)."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le risque principal si l'on utilise de l'huile de friture au-delà de son point de fumée de manière prolongée ?",
                    "answerOptions": [
                        {"text": "La perte de l'arôme.", "isCorrect": False},
                        {"text": "La dégradation de la matière grasse et la production de composés toxiques.", "isCorrect": True},
                        {"text": "L'huile devient plus visqueuse.", "isCorrect": False},
                        {"text": "Le produit est moins croustillant.", "isCorrect": False}
                    ],
                    "correction": "Le **point de fumée** est la température à laquelle la graisse commence à se décomposer. Le dépassement prolongé entraîne la formation d'**acroléine**, un composé irritant et potentiellement toxique, ainsi qu'une altération rapide de la qualité de l'huile."
                },
                {
                    "questionNumber": 89,
                    "question": "Dans le séchage des saucissons, quel indicateur visuel ou tactile permet de déterminer si le produit est prêt à être commercialisé ?",
                    "answerOptions": [
                        {"text": "Le poids initial de la mêlée.", "isCorrect": False},
                        {"text": "La présence de flore de surface (fleur).", "isCorrect": False},
                        {"text": "L'obtention d'une perte de poids spécifique.", "isCorrect": True},
                        {"text": "La brillance du boyau.", "isCorrect": False}
                    ],
                    "correction": "Le séchage est mesuré par la **perte de poids** (le ressuyage). La réglementation et les cahiers des charges fixent un pourcentage minimum de perte de poids (ex. 30 à 40 %) pour garantir une quantité d'eau suffisamment faible pour la conservation et l'obtention de la texture."
                },
                {
                    "questionNumber": 90,
                    "question": "Quelle méthode de cuisson est la plus appropriée pour des pièces de viande dures, riches en tissus conjonctifs (collagène), comme l'épaule de porc pour un effiloché ?",
                    "answerOptions": [
                        {"text": "Rôtir à feu vif.", "isCorrect": False},
                        {"text": "Griller sur barbecue.", "isCorrect": False},
                        {"text": "Cuisson lente et humide (braiser ou mijoter).", "isCorrect": True},
                        {"text": "Poêler rapidement.", "isCorrect": False}
                    ],
                    "correction": "Les viandes riches en **collagène** nécessitent une **cuisson lente et humide** (braisage, mijotage). La chaleur humide et douce permet au collagène de se transformer en gélatine, attendrissant la viande sans la dessécher."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le principal facteur qui définit la **durée de vie (DLC)** d'une charcuterie fraîche cuite (comme le pâté de campagne) ?",
                    "answerOptions": [
                        {"text": "Le coût de la matière première.", "isCorrect": False},
                        {"text": "La quantité d'épices ajoutées.", "isCorrect": False},
                        {"text": "L'activité de l'eau (Aw) et le pH du produit.", "isCorrect": True},
                        {"text": "La taille du produit.", "isCorrect": False}
                    ],
                    "correction": "L'**activité de l'eau (Aw)** et le **pH** sont les deux facteurs physico-chimiques les plus importants pour la conservation. Un pH bas (acidité) et une faible Aw (peu d'eau disponible) limitent le développement des micro-organismes, prolongeant la DLC."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le but de l'opération de **fleurage** d'une pâte à tarte salée ?",
                    "answerOptions": [
                        {"text": "Ajouter de l'eau à la pâte.", "isCorrect": False},
                        {"text": "Saupoudrer de farine pour empêcher la pâte de coller.", "isCorrect": True},
                        {"text": "Mettre la pâte en boule.", "isCorrect": False},
                        {"text": "La laisser reposer au froid.", "isCorrect": False}
                    ],
                    "correction": "Le **fleurage** est l'action de saupoudrer légèrement de **farine** le plan de travail et la pâte. Cela empêche la pâte (notamment la pâte feuilletée ou levée) d'adhérer au support pendant les étapes de travail (fonçage, tourage, abaisse)."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel danger est associé à la consommation de charcuteries crues ou insuffisamment cuites, non traitées pour la salaison ?",
                    "answerOptions": [
                        {"text": "La botulisme uniquement.", "isCorrect": False},
                        {"text": "Les parasites (comme la Trichinellose).", "isCorrect": True},
                        {"text": "La listériose uniquement.", "isCorrect": False},
                        {"text": "La présence d'additifs.", "isCorrect": False}
                    ],
                    "correction": "L'un des risques majeurs associés à la consommation de viande de porc crue ou insuffisamment cuite est la **Trichinellose** (due à un ver parasite). La cuisson à 68 °C ou la congélation à -18 °C sont des mesures efficaces pour le détruire."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel type de fumage (à chaud ou à froid) est généralement utilisé pour les jambons secs et les saucissons, où l'on cherche à apporter de l'arôme sans cuire la viande ?",
                    "answerOptions": [
                        {"text": "Fumage à chaud (température > 65 °C).", "isCorrect": False},
                        {"text": "Fumage à froid (température < 25 °C).", "isCorrect": True},
                        {"text": "Fumage à l'eau.", "isCorrect": False},
                        {"text": "Fumage par injection.", "isCorrect": False}
                    ],
                    "correction": "Le **fumage à froid** (entre 18 °C et 25 °C) ajoute de l'arôme et des propriétés conservatrices à la viande sans déclencher la cuisson des protéines. Il est utilisé pour les produits séchés ou crus (saumon fumé, saucisson sec, jambon sec)."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le document réglementaire essentiel qui rassemble toutes les procédures d'hygiène et d'autocontrôle mises en place dans l'établissement de charcuterie-traiteur ?",
                    "answerOptions": [
                        {"text": "Le registre de caisse.", "isCorrect": False},
                        {"text": "Le Plan de Maîtrise Sanitaire (PMS).", "isCorrect": True},
                        {"text": "Le cahier de recettes.", "isCorrect": False},
                        {"text": "La Fiche de Données de Sécurité (FDS).", "isCorrect": False}
                    ],
                    "correction": "Le **Plan de Maîtrise Sanitaire (PMS)** est le document central et obligatoire de l'entreprise. Il décrit l'ensemble des mesures (HACCP, traçabilité, gestion des non-conformités) pour garantir la sécurité et la salubrité des aliments produits."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est l'alternative à l'eau pour réaliser un bain-marie (cuisson au four) afin d'assurer une température de cuisson très stable pour un appareil à flan ou une terrine délicate ?",
                    "answerOptions": [
                        {"text": "L'huile de friture.", "isCorrect": False},
                        {"text": "L'eau-de-vie.", "isCorrect": False},
                        {"text": "Le gros sel.", "isCorrect": True},
                        {"text": "Le bouillon de légumes.", "isCorrect": False}
                    ],
                    "correction": "Un **bain de gros sel** (au lieu d'eau) est souvent utilisé pour les cuissons très délicates. Le sel absorbe et redistribue la chaleur de manière plus homogène que l'eau, et surtout, il ne s'évapore pas, assurant un niveau de chaleur constant tout au long de la cuisson."
                },
                {
                    "questionNumber": 97,
                    "question": "Selon le code de la consommation, quelle mention est obligatoire sur l'étiquetage d'un produit alimentaire pré-emballé ?",
                    "answerOptions": [
                        {"text": "Le nom et le prénom de l'opérateur.", "isCorrect": False},
                        {"text": "Le code APE de l'entreprise.", "isCorrect": False},
                        {"text": "La liste des ingrédients (dont les allergènes) et la DLC.", "isCorrect": True},
                        {"text": "Le chiffre d'affaires.", "isCorrect": False}
                    ],
                    "correction": "La réglementation INCO impose la présence de plusieurs mentions obligatoires, dont : la **dénomination de vente**, la liste des **ingrédients** (avec mise en évidence des **allergènes**), la quantité nette, le nom de l'exploitant, l'origine, la **DLC/DDM** et la déclaration nutritionnelle."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est l'effet d'une trop forte présence de **tissus conjonctifs** (tendons, aponévroses) dans une viande destinée à être hachée pour une saucisse ?",
                    "answerOptions": [
                        {"text": "Une amélioration de la saveur.", "isCorrect": False},
                        {"text": "Une dégradation de la couleur.", "isCorrect": False},
                        {"text": "Une texture caoutchouteuse ou élastique après cuisson.", "isCorrect": True},
                        {"text": "Une absence de gras.", "isCorrect": False}
                    ],
                    "correction": "Les tissus conjonctifs (composés de collagène) sont difficiles à hacher finement et à fondre complètement à basse température. S'ils sont trop abondants, ils donnent au produit fini une **texture élastique ou caoutchouteuse** désagréable en bouche. D'où l'importance du parage."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel type de viande, peu colorée et avec un goût neutre, est idéal pour la fabrication des **galantines** et des ballotines de volaille ?",
                    "answerOptions": [
                        {"text": "Viande de bœuf très rouge.", "isCorrect": False},
                        {"text": "Viande de canard gras.", "isCorrect": False},
                        {"text": "Viande blanche (volaille ou veau).", "isCorrect": True},
                        {"text": "Viande d'agneau forte.", "isCorrect": False}
                    ],
                    "correction": "Les **galantines** et **ballotines** sont des charcuteries cuites froides, souvent servies en tranches. On privilégie la **viande blanche** (poulet, dinde, veau) pour obtenir une farce claire, fine et neutre, qui se marie bien avec la garniture (truffes, pistaches, légumes)."
                },
                {
                    "questionNumber": 100,
                    "question": "En charcuterie, qu'appelle-t-on le *ressuyage* de la viande après salaison ?",
                    "answerOptions": [
                        {"text": "L'injection de saumure pour hydrater le produit.", "isCorrect": False},
                        {"text": "La période de repos où la viande perd de l'eau et le sel se diffuse.", "isCorrect": True},
                        {"text": "L'application d'une fleur de moisissure en surface.", "isCorrect": False},
                        {"text": "Le frottage de la pièce avec des aromates.", "isCorrect": False}
                    ],
                    "correction": "Le **ressuyage** est la période de repos au froid qui suit le salage ou l'injection. Pendant cette étape, le sel termine sa **diffusion** dans la masse, et la viande perd une partie de son **eau** (perte de poids), préparant le produit à l'étuvage ou au séchage."
                },
            ]
        }
    }
}