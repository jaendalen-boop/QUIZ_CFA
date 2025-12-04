quiz_data = {
    "title": "Quiz CAP Coiffure : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : BIOLOGIE DU CHEVEU ET DU CUIR CHEVELU (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Biologie du cheveu et du cuir chevelu (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la partie du cheveu qui se trouve au-dessus de la peau et qui est constituée de cellules mortes kératinisées ?",
                    "answerOptions": [
                        {"text": "Le bulbe pilaire", "isCorrect": False, "rationale": "Le bulbe est la partie vivante, située sous le cuir chevelu, responsable de la croissance."},
                        {"text": "Le cortex", "isCorrect": False, "rationale": "Le cortex est la couche interne de la tige, mais la question fait référence à la partie visible dans son ensemble."},
                        {"text": "La tige pilaire", "isCorrect": True, "rationale": "La **tige pilaire** est la partie visible, inerte et kératinisée, qui émerge du follicule."},
                        {"text": "La papille dermique", "isCorrect": False, "rationale": "La papille est le 'cœur' nourricier du follicule, située à sa base."}
                    ],
                    "correction": "La **tige pilaire** est la partie que l'on coiffe et qui n'est plus vivante. Elle est constituée de trois couches : la cuticule, le cortex et parfois la moelle."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le pourcentage approximatif de Kératine dans la composition de la fibre capillaire ?",
                    "answerOptions": [
                        {"text": "Environ 10 %", "isCorrect": False, "rationale": "10 % est le pourcentage approximatif d'eau dans un cheveu sain."},
                        {"text": "Environ 35 %", "isCorrect": False, "rationale": "Cette valeur est trop faible pour le composant majeur du cheveu."},
                        {"text": "Environ 85 %", "isCorrect": True, "rationale": "La **Kératine** est la protéine structurelle principale du cheveu, garantissant sa résistance."},
                        {"text": "Environ 60 %", "isCorrect": False, "rationale": "60 % est une estimation courante de la quantité de protéines dans l'ensemble du corps humain."}
                    ],
                    "correction": "La **Kératine** est une protéine fibreuse, riche en soufre, qui représente l'essentiel de la masse du cheveu. Sa qualité est essentielle pour l'élasticité et la solidité de la fibre."
                },
                {
                    "questionNumber": 3,
                    "question": "Dans le cycle pilaire, quelle est la phase la plus longue, correspondant à la période de croissance active du cheveu ?",
                    "answerOptions": [
                        {"text": "La phase Catagène", "isCorrect": False, "rationale": "La phase Catagène est une phase de transition et de régression, très courte (quelques semaines)."},
                        {"text": "La phase Anagène", "isCorrect": True, "rationale": "La phase **Anagène** est la phase de production et de croissance du cheveu, durant de 2 à 7 ans."},
                        {"text": "La phase Télogène", "isCorrect": False, "rationale": "La phase Télogène est la phase de repos et de chute, plus longue que la Catagène, mais plus courte que l'Anagène."},
                        {"text": "La phase Kératogène", "isCorrect": False, "rationale": "La Kératogenèse est le processus de fabrication de la kératine, non une phase du cycle."}
                    ],
                    "correction": "La phase **Anagène** est la phase de croissance et représente environ 85 % à 90 % des cheveux sur le cuir chevelu à un moment donné."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel est le rôle principal de la mélanine, située dans le cortex de la tige pilaire ?",
                    "answerOptions": [
                        {"text": "Assurer la souplesse du cheveu", "isCorrect": False, "rationale": "La souplesse est assurée par l'équilibre kératine/eau/lipides."},
                        {"text": "Fournir les nutriments essentiels au bulbe", "isCorrect": False, "rationale": "Les nutriments sont apportés par la papille dermique."},
                        {"text": "Déterminer la couleur naturelle du cheveu", "isCorrect": True, "rationale": "La **mélanine** (eumélanine et phéomélanine) est le pigment naturel qui donne sa couleur au cheveu."},
                        {"text": "Lubrifier le cuir chevelu et la fibre", "isCorrect": False, "rationale": "La lubrification est le rôle du sébum (glande sébacée)."}
                    ],
                    "correction": "Le cortex contient les pigments de **mélanine**. La quantité et le type de mélanine (eumélanine pour les couleurs foncées, phéomélanine pour les rouges/jaunes) déterminent la couleur finale."
                },
                {
                    "questionNumber": 5,
                    "question": "Comment agissent les produits ayant un pH très alcalin sur la couche externe du cheveu ?",
                    "answerOptions": [
                        {"text": "Ils ferment et resserrent les écailles de la cuticule.", "isCorrect": False, "rationale": "C'est l'effet des produits acides (pH < 7)."},
                        {"text": "Ils dissolvent les ponts disulfures sans ouvrir les écailles.", "isCorrect": False, "rationale": "Les produits alcalins ouvrent les écailles ET peuvent faciliter la rupture des ponts disulfures."},
                        {"text": "Ils ouvrent et font gonfler les écailles de la cuticule.", "isCorrect": True, "rationale": "Un pH **alcalin** (basique), comme celui des colorations d'oxydation, ouvre les écailles pour la pénétration du produit."},
                        {"text": "Ils n'ont aucun effet sur la structure externe.", "isCorrect": False, "rationale": "Le pH a un impact majeur sur la cuticule du cheveu."}
                    ],
                    "correction": "Pour que la couleur ou les produits de permanente puissent atteindre le cortex, il faut un milieu **alcalin** pour provoquer le gonflement de la tige et l'ouverture de la **cuticule**."
                },
                {
                    "questionNumber": 6,
                    "question": "La porosité d'un cheveu est directement liée à l'état de quelle partie de la fibre ?",
                    "answerOptions": [
                        {"text": "Le cortex", "isCorrect": False, "rationale": "Le cortex est plus lié à la force et à l'élasticité."},
                        {"text": "La moelle", "isCorrect": False, "rationale": "La moelle est souvent absente et n'influence pas la porosité."},
                        {"text": "La cuticule", "isCorrect": True, "rationale": "La **cuticule** est la couche externe qui détermine la capacité du cheveu à absorber et retenir l'humidité et les produits."},
                        {"text": "Le sébum", "isCorrect": False, "rationale": "Le sébum est une sécrétion lipidique, pas une partie de la fibre."}
                    ],
                    "correction": "La **porosité** est la mesure de la capacité du cheveu à absorber. Elle dépend de l'état des **écailles de la cuticule** : plus elles sont ouvertes, plus le cheveu est poreux."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel terme technique désigne la présence de pointes fourchues ?",
                    "answerOptions": [
                        {"text": "Alopécie", "isCorrect": False, "rationale": "L'alopécie est le terme désignant la chute de cheveux."},
                        {"text": "Trichoptilose", "isCorrect": True, "rationale": "La **trichoptilose** est le terme scientifique pour désigner l'éclatement ou le dédoublement de la pointe du cheveu (fourche)."},
                        {"text": "Pityriasis", "isCorrect": False, "rationale": "Le Pityriasis est un état pelliculaire."},
                        {"text": "Séborrhée", "isCorrect": False, "rationale": "La séborrhée est la production excessive de sébum."}
                    ],
                    "correction": "La **trichoptilose** est le résultat d'une agression physique ou chimique (brossage trop agressif, chaleur excessive) qui fragilise et fend la fibre à son extrémité."
                },
                {
                    "questionNumber": 8,
                    "question": "Quel type de liaison faible, rompue par la chaleur et l'eau, est responsable de la mise en forme temporaire (brushing, rouleaux) ?",
                    "answerOptions": [
                        {"text": "Les ponts salins", "isCorrect": False, "rationale": "Les ponts salins sont sensibles au pH."},
                        {"text": "Les liaisons peptidiques", "isCorrect": False, "rationale": "Ces liaisons forment la chaîne de Kératine et sont très solides."},
                        {"text": "Les liaisons disulfures", "isCorrect": False, "rationale": "Ces liaisons sont rompues par la permanente et le défrisage chimique."},
                        {"text": "Les liaisons hydrogènes", "isCorrect": True, "rationale": "Les **liaisons hydrogènes** sont rompues lorsque le cheveu est mouillé ou chauffé, puis elles se reforment lorsque le cheveu sèche, fixant la nouvelle forme temporairement."}
                    ],
                    "correction": "Les **liaisons hydrogènes** sont des liens faibles qui se rompent et se reforment facilement. C'est le principe de base de toutes les techniques de coiffage nécessitant l'utilisation d'eau et de chaleur."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le pH naturel du cuir chevelu et du cheveu sain ?",
                    "answerOptions": [
                        {"text": "Neutre (pH 7)", "isCorrect": False, "rationale": "Le pH 7 est celui de l'eau pure."},
                        {"text": "Légèrement alcalin (pH 7.5 à 8.5)", "isCorrect": False, "rationale": "Le cheveu sain est acide, pas alcalin."},
                        {"text": "Très acide (pH 3 à 4)", "isCorrect": False, "rationale": "Ce niveau d'acidité est utilisé pour des soins très spécifiques (fermeture intense)."},
                        {"text": "Légèrement acide (pH 4.5 à 5.5)", "isCorrect": True, "rationale": "Le cuir chevelu et le cheveu sont naturellement **acides** (pH idéal d'environ 5.5) grâce au film hydrolipidique."}
                    ],
                    "correction": "Le pH naturel du cheveu et du cuir chevelu est **légèrement acide** (pH 4.5 à 5.5). C'est pour cette raison qu'on utilise souvent des soins et shampoings avec un pH acide pour lisser les écailles."
                },
                {
                    "questionNumber": 10,
                    "question": "La glande sébacée est une annexe du cheveu qui sécrète le sébum. Où se déverse principalement cette sécrétion ?",
                    "answerOptions": [
                        {"text": "Directement sur le cuir chevelu (épiderme)", "isCorrect": False, "rationale": "Bien que le sébum arrive sur le cuir chevelu, il est d'abord produit dans le follicule."},
                        {"text": "Dans le canal du muscle arrecteur", "isCorrect": False, "rationale": "Le muscle arrecteur n'a pas de canal de sécrétion."},
                        {"text": "Dans la papille dermique", "isCorrect": False, "rationale": "La papille fournit les nutriments, elle ne reçoit pas les sécrétions."},
                        {"text": "Dans le canal pilaire (follicule)", "isCorrect": True, "rationale": "La glande sébacée est connectée et déverse son contenu dans le canal du **follicule pileux**, d'où il migre vers le cuir chevelu."}
                    ],
                    "correction": "La glande sébacée est annexée au **follicule pileux**. Le sébum remonte le long du cheveu pour former le film hydrolipidique protecteur sur le cuir chevelu et la tige."
                },
                {
                    "questionNumber": 11,
                    "question": "Le terme 'état séborrhéique' désigne une anomalie du cuir chevelu qui se traduit par :",
                    "answerOptions": [
                        {"text": "Une chute de cheveux diffuse due à un stress.", "isCorrect": False, "rationale": "Ceci est un effluvium télogène."},
                        {"text": "Une sécheresse extrême et des pellicules fines.", "isCorrect": False, "rationale": "Ceci est un état pityriasique simple (pellicules sèches)."},
                        {"text": "Une hyper-sécrétion des glandes sébacées.", "isCorrect": True, "rationale": "L'état **séborrhéique** est la production excessive de sébum, rendant le cuir chevelu et les cheveux gras."},
                        {"text": "Une maladie fongique de la peau.", "isCorrect": False, "rationale": "Ceci correspondrait plutôt à une mycose ou une teigne."}
                    ],
                    "correction": "La **séborrhée** est une production anormale de sébum. Si l'anomalie est liée à la présence de levures (Malassezia), on parle d'état séborrhéique complexe (pellicules grasses)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel est le nom du muscle qui, en se contractant, redresse le cheveu (provoque la chair de poule) ?",
                    "answerOptions": [
                        {"text": "Le muscle lisseur", "isCorrect": False, "rationale": "Nom inventé, terme incorrect."},
                        {"text": "Le muscle papillaire", "isCorrect": False, "rationale": "La papille est le tissu nourricier, pas un muscle."},
                        {"text": "Le muscle arrecteur", "isCorrect": True, "rationale": "Le **muscle arrecteur** (ou arrecteur du poil) est un petit muscle involontaire rattaché au follicule, qui se contracte sous l'effet du froid ou de la peur."},
                        {"text": "Le muscle cutané", "isCorrect": False, "rationale": "Terme trop vague et imprécis pour cette fonction spécifique."}
                    ],
                    "correction": "Le **muscle arrecteur** est rattaché au follicule. Sa contraction entraîne le redressement du cheveu et la formation de la 'chair de poule' (horripilation)."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est l'élément qui permet de distinguer chimiquement l'eumélanine de la phéomélanine ?",
                    "answerOptions": [
                        {"text": "Le taux d'oxygène", "isCorrect": False, "rationale": "L'oxygène est impliqué dans l'oxydation des colorants, pas dans la structure de la mélanine."},
                        {"text": "La présence de Fer", "isCorrect": False, "rationale": "Le fer est un composant de l'hémoglobine (sang)."},
                        {"text": "La présence de Soufre", "isCorrect": True, "rationale": "La **phéomélanine** (pigments jaunes/rouges) contient du **soufre** dans sa structure, contrairement à l'eumélanine (pigments bruns/noirs)."},
                        {"text": "La taille des granules", "isCorrect": False, "rationale": "La taille est différente, mais c'est la structure chimique qui les distingue fondamentalement."}
                    ],
                    "correction": "La **phéomélanine**, responsable des reflets chauds, contient des atomes de **soufre** qui la rendent plus difficile à éclaircir ou à neutraliser complètement lors d'une décoloration."
                },
                {
                    "questionNumber": 14,
                    "question": "La phase Télogène du cycle pilaire est caractérisée par :",
                    "answerOptions": [
                        {"text": "Une division cellulaire intense dans la matrice.", "isCorrect": False, "rationale": "Ceci est la phase Anagène."},
                        {"text": "Une période de croissance rapide.", "isCorrect": False, "rationale": "La croissance est maximale en phase Anagène."},
                        {"text": "L'involution du follicule.", "isCorrect": False, "rationale": "Ceci est la phase Catagène."},
                        {"text": "Le repos du cheveu et sa chute imminente.", "isCorrect": True, "rationale": "La phase **Télogène** est la phase de repos, où le cheveu est 'mort' et prêt à tomber (ou est tombé) pour laisser place au nouveau cheveu."}
                    ],
                    "correction": "En phase **Télogène**, le cheveu est expulsé du follicule et le bulbe pilaire se prépare à entrer dans une nouvelle phase Anagène pour recréer un nouveau cheveu."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel type de cheveux présente le plus de risque de casse ou de fragilité aux nœuds en raison de sa forme très elliptique et aplatie ?",
                    "answerOptions": [
                        {"text": "Le cheveu asiatique", "isCorrect": False, "rationale": "Les cheveux asiatiques sont généralement ronds, très épais et résistants."},
                        {"text": "Le cheveu crépu (africain)", "isCorrect": True, "rationale": "Le cheveu **crépu** possède une forme très plate, créant des points de fragilité au niveau des courbures, d'où le risque de casse."},
                        {"text": "Le cheveu caucasien fin", "isCorrect": False, "rationale": "Le cheveu caucasien est généralement de forme ovale."},
                        {"text": "Le cheveu méché", "isCorrect": False, "rationale": "Le cheveu méché est fragilisé par le traitement, mais sa forme n'est pas la cause première de sa fragilité."}
                    ],
                    "correction": "Le cheveu **crépu** (Africain) est caractérisé par une forme transversale très **elliptique et aplatie** avec une pousse en spirale, ce qui le rend structurellement plus fragile et susceptible de se casser."
                },
                {
                    "questionNumber": 16,
                    "question": "Qu'est-ce que le film hydrolipidique du cuir chevelu ?",
                    "answerOptions": [
                        {"text": "Un revêtement lipidique pur (sébum).", "isCorrect": False, "rationale": "Il contient également de l'eau (sueur)."},
                        {"text": "La couche la plus superficielle de l'épiderme.", "isCorrect": False, "rationale": "Ceci est la couche cornée."},
                        {"text": "Un mélange d'eau (sueur) et de graisse (sébum).", "isCorrect": True, "rationale": "Le film **hydrolipidique** est un mélange de **sébum** (lipides) et de **sueur** (eau), créant une barrière protectrice acide."},
                        {"text": "Le résultat d'une coloration permanente.", "isCorrect": False, "rationale": "La coloration modifie la couleur du cheveu, pas la composition de la barrière cutanée."}
                    ],
                    "correction": "Le film **hydrolipidique** est une émulsion protectrice qui maintient l'hydratation du cuir chevelu, protège contre les microbes et contribue au pH acide (manteau acide)."
                },
                {
                    "questionNumber": 17,
                    "question": "Laquelle des structures suivantes est responsable de l'apport en nutriments au bulbe pilaire pour la croissance du cheveu ?",
                    "answerOptions": [
                        {"text": "La gaine épithéliale", "isCorrect": False, "rationale": "La gaine protège et guide le cheveu."},
                        {"text": "Le follicule pileux", "isCorrect": False, "rationale": "Le follicule est l'enveloppe générale."},
                        {"text": "La papille dermique", "isCorrect": True, "rationale": "La **papille dermique** est richement vascularisée et apporte l'oxygène et les nutriments nécessaires à la division cellulaire de la matrice."},
                        {"text": "Le cortex", "isCorrect": False, "rationale": "Le cortex est la partie interne de la tige pilaire (le cheveu lui-même)."}
                    ],
                    "correction": "La **papille dermique** est le point de connexion entre le cheveu et le réseau sanguin du derme. Elle est vitale pour la santé et la croissance de la fibre."
                },
                {
                    "questionNumber": 18,
                    "question": "Les ponts disulfures (ou ponts cystine) sont les liaisons les plus résistantes du cheveu. Ils sont modifiés chimiquement lors de quelle technique ?",
                    "answerOptions": [
                        {"text": "Le brushing et la mise en plis", "isCorrect": False, "rationale": "Ces techniques modifient les liaisons hydrogènes (faibles)."},
                        {"text": "Le shampooing et le soin hydratant", "isCorrect": False, "rationale": "Ces actions n'atteignent pas les ponts disulfures."},
                        {"text": "La coloration ton sur ton", "isCorrect": False, "rationale": "La coloration n'a pas besoin de rompre les liaisons disulfures."},
                        {"text": "La permanente ou le défrisage chimique", "isCorrect": True, "rationale": "La **permanente** (ou le défrisage) utilise des réducteurs pour rompre les ponts disulfures, puis un fixateur pour les reformer dans une nouvelle position."}
                    ],
                    "correction": "Les ponts **disulfures** sont les fondations du cheveu. Leur rupture puis leur reconstruction sont l'objectif des techniques de **permanente** ou de lissage chimique pour obtenir une modification durable de la forme."
                },
                {
                    "questionNumber": 19,
                    "question": "Si un cheveu est décrit comme 'hyperséborrhéique', quel type de shampoing est généralement le plus adapté pour le premier lavage ?",
                    "answerOptions": [
                        {"text": "Un shampoing au pH très acide.", "isCorrect": False, "rationale": "Le pH acide est pour resserrer les écailles après un traitement chimique."},
                        {"text": "Un shampoing de traitement volumateur.", "isCorrect": False, "rationale": "Un volumateur ne gère pas la séborrhée."},
                        {"text": "Un shampoing doux et purifiant.", "isCorrect": True, "rationale": "Il faut un shampoing **doux et purifiant** pour réguler la production de sébum sans agresser, ce qui pourrait provoquer un effet rebond."},
                        {"text": "Un shampoing très décapant (alcalin).", "isCorrect": False, "rationale": "Un shampoing trop décapant peut agresser le cuir chevelu et provoquer une production de sébum en réaction (effet rebond)."}
                    ],
                    "correction": "Il faut traiter l'excès de sébum avec un shampoing **doux et régulateur** (purifiant) pour éviter de décaper le cuir chevelu et d'entraîner une hyper-sécrétion en réponse."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le nom de la membrane fibreuse transparente qui entoure la racine du cheveu et le relie à la peau ?",
                    "answerOptions": [
                        {"text": "L'épiderme", "isCorrect": False, "rationale": "L'épiderme est la couche externe de la peau."},
                        {"text": "Le cortex", "isCorrect": False, "rationale": "Le cortex est la couche interne du cheveu."},
                        {"text": "La gaine épithéliale", "isCorrect": True, "rationale": "La **gaine épithéliale** (interne et externe) est le tissu qui entoure la racine, assurant sa cohésion et la guidant dans sa pousse."},
                        {"text": "La matrice", "isCorrect": False, "rationale": "La matrice est la zone de production des cellules à la base du bulbe."}
                    ],
                    "correction": "La **gaine épithéliale** (ou gaine du follicule) est l'enveloppe protectrice qui maintient et protège le cheveu en formation dans sa 'poche' (le follicule)."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : COLORIMÉTRIE ET PRODUITS (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Colorimétrie et Produits (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Dans le système international de coloration (I.S.N), à quoi correspond le chiffre après la virgule (ou le tiret) ?",
                    "answerOptions": [
                        {"text": "À la hauteur de ton (niveau de clarté)", "isCorrect": False, "rationale": "La hauteur de ton est le chiffre avant la virgule."},
                        {"text": "Au reflet primaire (dominant)", "isCorrect": True, "rationale": "Le premier chiffre après le point ou la virgule indique le **reflet primaire**, c'est-à-dire le reflet le plus dominant de la couleur."},
                        {"text": "Au reflet secondaire (nuance)", "isCorrect": False, "rationale": "Le reflet secondaire est le deuxième chiffre après la virgule."},
                        {"text": "À la nature du cheveu (pourcentage de blanc)", "isCorrect": False, "rationale": "Le pourcentage de blanc doit être évalué par le coiffeur."}
                    ],
                    "correction": "Le premier chiffre après le séparateur indique le **reflet principal** (par exemple, 6.**4**5, où '4' est le reflet cuivré principal). Le chiffre avant le séparateur indique la hauteur de ton (6 = blond foncé)."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelles sont les trois couleurs primaires qui, mélangées en proportions égales, sont censées créer une couleur neutre (gris/marron) ?",
                    "answerOptions": [
                        {"text": "Le jaune, le vert et le bleu", "isCorrect": False, "rationale": "Le vert est une couleur secondaire."},
                        {"text": "Le rouge, le violet et le bleu", "isCorrect": False, "rationale": "Le violet est une couleur secondaire."},
                        {"text": "Le rouge, le jaune et le bleu", "isCorrect": True, "rationale": "Le **rouge, le jaune et le bleu** sont les trois couleurs primaires. Leur mélange permet de créer toutes les autres couleurs."},
                        {"text": "Le cyan, le magenta et le jaune", "isCorrect": False, "rationale": "Ce sont les primaires en synthèse soustractive (impression), mais le rouge est utilisé en coiffure pour simplifier l'enseignement."}
                    ],
                    "correction": "Les bases de la colorimétrie reposent sur le **rouge, le jaune et le bleu**. Leur superposition ou mélange en proportions équilibrées doit théoriquement annuler les reflets pour créer un fond neutre."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la couleur considérée comme la couleur opposée (complémentaire) au jaune dans le cercle chromatique de coiffure ?",
                    "answerOptions": [
                        {"text": "Le rouge", "isCorrect": False, "rationale": "Le rouge et le jaune sont adjacents (couleurs chaudes)."},
                        {"text": "Le vert", "isCorrect": False, "rationale": "Le vert est composé de jaune et bleu. Il neutralise le rouge."},
                        {"text": "Le bleu-violet", "isCorrect": True, "rationale": "Le **bleu-violet** (ou juste violet/mauve) est la couleur complémentaire du jaune. Il est utilisé pour neutraliser les reflets jaunes indésirables après un éclaircissement."},
                        {"text": "L'orange", "isCorrect": False, "rationale": "L'orange est composé de jaune et rouge. Il neutralise le bleu."}
                    ],
                    "correction": "Dans le cercle chromatique, le **violet/bleu-violet** est directement opposé au jaune. Les couleurs complémentaires s'annulent lorsqu'elles sont mélangées à part égale."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le rôle principal de l'eau oxygénée (Peroxyde d'hydrogène) dans une coloration d'oxydation (permanente) ?",
                    "answerOptions": [
                        {"text": "Elle apporte les pigments colorants au cheveu.", "isCorrect": False, "rationale": "Ce sont les crèmes colorantes qui contiennent les pigments."},
                        {"text": "Elle fixe la kératine pour refermer les écailles.", "isCorrect": False, "rationale": "C'est l'action des produits acides, non de l'oxydant."},
                        {"text": "Elle permet le gonflement du cheveu.", "isCorrect": False, "rationale": "Le gonflement est provoqué par le milieu alcalin de la crème colorante (ammoniaque)."},
                        {"text": "Elle oxyde et révèle les précurseurs de couleur.", "isCorrect": True, "rationale": "L'eau oxygénée est l'**oxydant** qui, au contact des précurseurs de couleur, permet la réaction chimique qui crée la couleur définitive à l'intérieur du cortex."}
                    ],
                    "correction": "L'eau oxygénée (ou révélateur, ou développeur) est l'agent **oxydant**. Sa concentration (volume) détermine le pouvoir éclaircissant du mélange colorant."
                },
                {
                    "questionNumber": 25,
                    "question": "Qu'est-ce qu'une coloration 'ton sur ton' (ou semi-permanente) ?",
                    "answerOptions": [
                        {"text": "Une coloration qui éclaircit de 3 tons ou plus.", "isCorrect": False, "rationale": "Ceci est une coloration d'oxydation forte ou une décoloration."},
                        {"text": "Une coloration sans aucun agent alcalin (sans ammoniaque, sans MEA).", "isCorrect": False, "rationale": "La plupart des ton sur ton contiennent un alcalin doux."},
                        {"text": "Une coloration qui pénètre peu et s'estompe après plusieurs shampooings.", "isCorrect": True, "rationale": "La coloration **ton sur ton** travaille avec un oxydant faible et ne pénètre que partiellement le cortex, elle s'estompe donc sans effet de racine marqué."},
                        {"text": "Une coloration qui couvre 100% des cheveux blancs de manière permanente.", "isCorrect": False, "rationale": "Elle couvre en transparence et s'estompe, elle est dite semi-permanente."}
                    ],
                    "correction": "La coloration **ton sur ton** permet de foncer, de corriger des reflets ou d'apporter de la brillance. Elle est utilisée pour une modification légère car elle ne pénètre pas en profondeur le cheveu et s'élimine progressivement."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la principale différence entre une mèche et un balayage ?",
                    "answerOptions": [
                        {"text": "La mèche est toujours plus claire que la couleur de base, tandis que le balayage peut être plus foncé.", "isCorrect": False, "rationale": "Les deux peuvent être clairs ou foncés."},
                        {"text": "La mèche est une séparation franche (plus épaisse), et le balayage est un éclaircissement fondu et naturel.", "isCorrect": True, "rationale": "La **mèche** a un effet plus prononcé et marqué. Le **balayage** est réalisé avec des séparations fines pour un rendu plus subtil et sans démarcation."},
                        {"text": "Le balayage est réalisé avec une décoloration, la mèche avec une coloration.", "isCorrect": False, "rationale": "Les deux techniques peuvent utiliser les deux types de produits."},
                        {"text": "Le balayage est posé à l'air libre, la mèche est toujours sous papier aluminium.", "isCorrect": False, "rationale": "La technique de pose (aluminium, cellophane) ne définit pas le balayage ou la mèche."}
                    ],
                    "correction": "La **mèche** est caractérisée par une forte différenciation de couleur (effet zébré si mal réalisée), alors que le **balayage** cherche un éclaircissement plus doux, plus fondu et plus naturel."
                },
                {
                    "questionNumber": 27,
                    "question": "Dans le cadre d'une permanente classique, quel produit est appliqué en premier lieu pour modifier durablement la forme du cheveu ?",
                    "answerOptions": [
                        {"text": "Le fixateur (oxydant)", "isCorrect": False, "rationale": "Le fixateur est appliqué en dernier pour reformer les ponts."},
                        {"text": "La lotion réductrice (alcaline)", "isCorrect": True, "rationale": "La lotion **réductrice** est le produit actif qui rompt les ponts disulfures (liaisons fortes) du cheveu, lui permettant d'adopter la forme du bigoudi."},
                        {"text": "Le shampoing acide", "isCorrect": False, "rationale": "Le shampoing est utilisé après le processus."},
                        {"text": "Le soin neutralisant", "isCorrect": False, "rationale": "Le neutralisant est une autre appellation du fixateur."}
                    ],
                    "correction": "La lotion **réductrice** (souvent à base de Thiol ou de dérivé de la cystéine) est appliquée en premier pour casser les liaisons de la Kératine, qui sont ensuite réalignées par le bigoudi."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel risque peut engendrer l'utilisation d'un oxydant de haut volume (40 volumes ou 12%) sur un cheveu déjà sensibilisé ?",
                    "answerOptions": [
                        {"text": "Une couverture incomplète des cheveux blancs.", "isCorrect": False, "rationale": "L'oxydant à 40 vol est très puissant, la couverture ne serait pas le problème majeur."},
                        {"text": "Un dépôt de couleur trop foncé (surcharge pigmentaire).", "isCorrect": False, "rationale": "C'est le contraire, il y a risque d'éclaircissement trop fort."},
                        {"text": "Une rupture totale des liaisons, rendant le cheveu élastique et cassant.", "isCorrect": True, "rationale": "L'oxydant fort sur cheveu sensibilisé entraîne un risque de **brûlure chimique** et la destruction du cortex (cheveu caoutchouteux)."},
                        {"text": "Une repousse de couleur très foncée.", "isCorrect": False, "rationale": "La repousse n'est pas affectée par un sur-oxydation de la tige."}
                    ],
                    "correction": "L'oxydant fort (30 ou 40 vol) est réservé aux éclaircissements importants. Utilisé sur un cheveu déjà fragilisé, il peut entraîner une **porosité extrême**, une perte d'élasticité et une **casse** irréversible."
                },
                {
                    "questionNumber": 29,
                    "question": "Que signifie le terme 'Hauteur de Ton' en colorimétrie ?",
                    "answerOptions": [
                        {"text": "L'intensité du reflet (par exemple, doré intense ou subtil).", "isCorrect": False, "rationale": "Ceci est géré par la concentration du reflet (ex: .33)."},
                        {"text": "Le degré de clarté ou d'obscurité d'une couleur.", "isCorrect": True, "rationale": "La **Hauteur de Ton** est la valeur de clarté, numérotée de 1 (Noir) à 10 (Blond très très clair)."},
                        {"text": "La quantité de pigments de mélanine présente.", "isCorrect": False, "rationale": "Elle en est la conséquence, mais la HdT est une échelle chiffrée."},
                        {"text": "La couleur du reflet dominant (ex: rouge, cendrée).", "isCorrect": False, "rationale": "Ceci correspond au reflet."}
                    ],
                    "correction": "La **Hauteur de Ton** est toujours représentée par le premier chiffre de la formule colorante (ex: un 8 est un blond clair, un 5 est un châtain clair). C'est l'étape 1 du diagnostic."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est l'effet d'une coloration permanente (oxydation) sur les pigments naturels du cheveu ?",
                    "answerOptions": [
                        {"text": "Elle n'a aucun effet sur les pigments naturels.", "isCorrect": False, "rationale": "C'est le cas du ton sur ton ou de la coloration directe."},
                        {"text": "Elle entoure les pigments naturels sans les modifier.", "isCorrect": False, "rationale": "Elle les modifie en profondeur."},
                        {"text": "Elle détruit partiellement les pigments naturels (éclaircissement).", "isCorrect": True, "rationale": "L'oxydant (eau oxygénée) va **dégrader/détruire** (éclaircir) la mélanine naturelle en même temps qu'il développe la couleur artificielle. C'est le principe de l'éclaircissement."},
                        {"text": "Elle ajoute des pigments naturels de synthèse.", "isCorrect": False, "rationale": "Elle ajoute des pigments artificiels."}
                    ] ,
                    "correction": "Le processus de la coloration d'oxydation est double : elle **détruit** les pigments naturels pour créer un fond d'éclaircissement, et elle **dépose** les pigments artificiels pour créer la nouvelle couleur."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment appelle-t-on le niveau de clarté naturellement atteint par le cheveu lorsqu'on détruit la mélanine (suite à une décoloration par exemple) ?",
                    "answerOptions": [
                        {"text": "Le reflet artificiel", "isCorrect": False, "rationale": "Ceci est la couleur déposée."},
                        {"text": "Le fond de clarification", "isCorrect": True, "rationale": "Le **fond de clarification** (ou fond d'éclaircissement) est la couleur résiduelle chaude (rouge, rouge-orange, jaune-orange, jaune) qui apparaît lorsque la mélanine est détruite."},
                        {"text": "La hauteur de ton cible", "isCorrect": False, "rationale": "Ceci est le résultat souhaité."},
                        {"text": "Le voile pigmentaire", "isCorrect": False, "rationale": "Ceci est un terme générique pour les pigments."}
                    ],
                    "correction": "Le **fond de clarification** est essentiel en colorimétrie. Il est toujours chaud (orangé ou jaune) et doit être neutralisé par un reflet froid (cendré ou irisé) pour obtenir une couleur neutre ou un reflet précis."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le rôle du 'Perming', une substance souvent contenue dans les produits de permanente ?",
                    "answerOptions": [
                        {"text": "Il fixe la couleur après la coloration.", "isCorrect": False, "rationale": "C'est l'oxydant."},
                        {"text": "Il assouplit et démêle la fibre.", "isCorrect": False, "rationale": "C'est le rôle des après-shampoings."},
                        {"text": "Il agit comme agent de réduction (rupture des ponts disulfures).", "isCorrect": True, "rationale": "Le terme **Perming** fait référence à l'action de réduction qui permet de casser les liaisons fortes du cheveu pour le rendre malléable et lui donner une nouvelle forme."},
                        {"text": "Il crée une barrière protectrice contre la chaleur.", "isCorrect": False, "rationale": "C'est le rôle des thermo-protecteurs."}
                    ],
                    "correction": "Le 'Perming' désigne le principe actif de la **lotion réductrice** (le produit de permanente) qui rompt temporairement la structure interne du cheveu."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la principale fonction du sel dans la composition d'un shampoing ?",
                    "answerOptions": [
                        {"text": "Lui donner un parfum agréable.", "isCorrect": False, "rationale": "Le parfum est donné par les fragrances."},
                        {"text": "Créer l'effet moussant.", "isCorrect": False, "rationale": "Les agents moussants sont les tensioactifs."},
                        {"text": "Épaissir le produit (rendre la texture plus riche).", "isCorrect": True, "rationale": "Le sel (Chlorure de Sodium, NaCl) est un agent **épaississant** (viscosant) très courant dans les shampoings pour améliorer la texture et la sensation de richesse."},
                        {"text": "Détruire les bactéries (agent antiseptique).", "isCorrect": False, "rationale": "Le rôle antiseptique est mineur en coiffure par rapport à l'épaississement."}
                    ],
                    "correction": "Le sel est utilisé comme **épaississant** à faible coût dans de nombreux shampoings. Un taux trop élevé peut cependant dessécher ou irriter le cuir chevelu chez certaines personnes."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est l'unité de mesure utilisée pour quantifier la puissance de l'eau oxygénée (Peroxyde d'hydrogène) ?",
                    "answerOptions": [
                        {"text": "Le pH", "isCorrect": False, "rationale": "Le pH mesure l'acidité/alcalinité."},
                        {"text": "Le degré Baumé", "isCorrect": False, "rationale": "Le Baumé est utilisé pour la concentration de sel (saumure)."},
                        {"text": "Le Volume", "isCorrect": True, "rationale": "La puissance de l'oxydant est exprimée en **Volumes** (par exemple, 10, 20, 30 ou 40 volumes), qui représente la quantité d'oxygène libérée."},
                        {"text": "Le millilitre (ml)", "isCorrect": False, "rationale": "Le millilitre mesure la quantité de liquide."}
                    ],
                    "correction": "Le **Volume** indique le pouvoir d'éclaircissement : 10 volumes (3%) ne fait que déposer la couleur ; 20 volumes (6%) éclaircit d'un à deux tons ; 30 volumes (9%) de deux à trois tons, etc."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est la couleur complémentaire à l'orange (ou cuivré) que l'on utilise pour neutraliser un fond d'éclaircissement trop chaud ?",
                    "answerOptions": [
                        {"text": "Le rouge", "isCorrect": False, "rationale": "Le rouge et l'orange sont adjacents."},
                        {"text": "Le jaune", "isCorrect": False, "rationale": "Le jaune est une composante de l'orange."},
                        {"text": "Le bleu", "isCorrect": True, "rationale": "Le **bleu** est la couleur complémentaire de l'orange (ou cuivré). Il est souvent utilisé dans les colorations 'cendrées' (reflet .1) pour obtenir un résultat neutre."},
                        {"text": "Le violet", "isCorrect": False, "rationale": "Le violet neutralise le jaune."}
                    ],
                    "correction": "Le **bleu** est essentiel pour contrôler les reflets oranges et cuivrés qui apparaissent aux hauteurs de ton moyennes (5 à 7). Les cendrés (reflets bleutés) sont donc utilisés comme neutralisateurs."
                },
                {
                    "questionNumber": 36,
                    "question": "Dans le processus de lissage permanent (type défrisage chimique), quel est le produit qui intervient en deuxième position pour fixer la nouvelle forme lisse du cheveu ?",
                    "answerOptions": [
                        {"text": "La crème lissante (réductrice)", "isCorrect": False, "rationale": "C'est la première étape."},
                        {"text": "Le protecteur thermique", "isCorrect": False, "rationale": "C'est un soin de protection, pas l'élément chimique fixateur."},
                        {"text": "Le shampoing clarifiant", "isCorrect": False, "rationale": "C'est l'étape de préparation/nettoyage."},
                        {"text": "Le neutralisant (fixateur oxydant)", "isCorrect": True, "rationale": "Comme pour la permanente, le **neutralisant** (fixateur) est un oxydant qui reforme les ponts disulfures dans la position souhaitée (lisse), rendant la modification permanente."}
                    ],
                    "correction": "Après la rupture des ponts par le produit réducteur et la mise en forme (fer à lisser ou traction manuelle), le **neutralisant** est indispensable pour que les ponts se reforment durablement dans la nouvelle structure."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle catégorie de produit est la plus courante pour masquer les premières petites zones de cheveux blancs de manière subtile et non permanente ?",
                    "answerOptions": [
                        {"text": "La coloration de décapage", "isCorrect": False, "rationale": "Le décapage est une correction de couleur (très fort)."},
                        {"text": "Les colorations fugaces (temporaires)", "isCorrect": True, "rationale": "Les colorations **fugaces** (mousses, sprays, masques) se déposent en surface et partent au premier shampoing, idéales pour un camouflage léger ou temporaire."},
                        {"text": "La coloration d'oxydation 30 volumes", "isCorrect": False, "rationale": "C'est un produit fort pour un changement radical."},
                        {"text": "Le décolorant en poudre", "isCorrect": False, "rationale": "Ceci éclaircit le cheveu."}
                    ],
                    "correction": "Les colorations **fugaces** sont idéales pour les clients qui ne veulent pas s'engager sur une couleur permanente. Elles n'impliquent aucune transformation chimique interne du cheveu."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle molécule alcaline est le plus souvent utilisée dans les colorations d'oxydation (permanentes) pour ouvrir les écailles du cheveu ?",
                    "answerOptions": [
                        {"text": "Le silicone", "isCorrect": False, "rationale": "Le silicone est un agent cosmétique (gainage)."},
                        {"text": "L'acide lactique", "isCorrect": False, "rationale": "C'est un acide."},
                        {"text": "L'ammoniaque (ou l'éthanolamine)", "isCorrect": True, "rationale": "L'**ammoniaque** (ou son substitut, l'éthanolamine/MEA) est l'agent alcalin qui rend le pH du mélange haut, ouvrant les écailles pour que les colorants et l'oxydant pénètrent."},
                        {"text": "Le formol", "isCorrect": False, "rationale": "Le formol est un conservateur/fixateur dangereux, non un alcalin pour la couleur."}
                    ],
                    "correction": "L'**ammoniaque** ou l'éthanolamine sont indispensables pour créer un milieu alcalin permettant la pénétration du produit. L'ammoniaque est plus puissante mais a une forte odeur, le MEA est plus doux mais nécessite plus de temps de pose."
                },
                {
                    "questionNumber": 39,
                    "question": "Pourquoi est-il crucial de réaliser un 'test d'allergie' (touche d'essai) 48 heures avant toute coloration d'oxydation ?",
                    "answerOptions": [
                        {"text": "Pour vérifier le résultat final de la couleur.", "isCorrect": False, "rationale": "Le test d'allergie n'est pas pour la couleur, mais pour la sécurité."},
                        {"text": "Pour déterminer le fond de clarification.", "isCorrect": False, "rationale": "Ceci se fait par diagnostic visuel ou sur une mèche test."},
                        {"text": "Pour prévenir une réaction d'hypersensibilité cutanée aux colorants.", "isCorrect": True, "rationale": "Le test d'allergie est une obligation légale pour s'assurer que le client ne fera pas de réaction sévère (eczéma, œdème) aux **précurseurs de couleur** (notamment la PPD/PTD)."},
                        {"text": "Pour vérifier si le cheveu est assez poreux.", "isCorrect": False, "rationale": "Ceci est un diagnostic de porosité."}
                    ],
                    "correction": "Le test d'allergie est une exigence légale et de sécurité pour détecter les réactions aux produits, notamment à la PPD ou PTD. Le non-respect de cette procédure peut avoir des conséquences graves pour le client et le professionnel."
                },
                {
                    "questionNumber": 40,
                    "question": "Dans la nomenclature colorimétrique (ex: 7.34), quel chiffre représente le reflet cuivré ?",
                    "answerOptions": [
                        {"text": "Le 7", "isCorrect": False, "rationale": "Le 7 est la hauteur de ton (Blond)."},
                        {"text": "Le 3", "isCorrect": False, "rationale": "Le 3 est le reflet doré (jaune)."},
                        {"text": "Le 4", "isCorrect": True, "rationale": "Le **4** est le chiffre international pour le reflet **cuivré** (orange)."},
                        {"text": "Le 5", "isCorrect": False, "rationale": "Le 5 est le reflet acajou ou rouge violacé."}
                    ],
                    "correction": "Les principaux reflets sont : .1 = Cendré (Bleu/Vert) ; .2 = Irisé (Violet) ; .3 = Doré (Jaune) ; **.4 = Cuivré (Orange)** ; .5 = Acajou ; .6 = Rouge ; .7 = Marron/Naturel."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : TECHNIQUES DE COUPE ET MISE EN FORME (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Techniques de Coupe et Mise en Forme (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle ligne de coupe est définie par une élévation des cheveux à $180^{\\circ}$ par rapport au crâne ?",
                    "answerOptions": [
                        {"text": "L'augmentation de la masse (coupe pleine)", "isCorrect": False, "rationale": "La coupe pleine (masse) est réalisée avec une élévation à $0^{\\circ}$."},
                        {"text": "La coupe au carré (B.O.B.)", "isCorrect": False, "rationale": "Le carré est généralement réalisé avec une élévation à $0^{\\circ}$ ou basse."},
                        {"text": "La coupe progressive ou dégradée forte", "isCorrect": True, "rationale": "L'élévation à $180^{\\circ}$ (ou perpendiculaire au sol) est utilisée pour créer un **dégradé fort** ou une structure progressive et légère."},
                        {"text": "La frange droite", "isCorrect": False, "rationale": "La frange est généralement coupée à $0^{\\circ}$ ou à une faible élévation."}
                    ],
                    "correction": "Une élévation à $180^{\\circ}$ (tirer la mèche au maximum vers le haut) crée un maximum de couches et un **dégradé** important, réduisant le poids sur les pointes."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le rôle du 'point de pivot' dans une coupe de cheveux ?",
                    "answerOptions": [
                        {"text": "Il sert à définir le contour d'oreille.", "isCorrect": False, "rationale": "Le contour d'oreille est une zone, pas un point de pivot."},
                        {"text": "C'est l'endroit où le cheveu est le plus long sur le sommet de tête.", "isCorrect": False, "rationale": "Le sommet est une zone, pas un point de pivot."},
                        {"text": "C'est le point de référence central (souvent au sommet) autour duquel les sections sont peignées pour la coupe.", "isCorrect": True, "rationale": "Le **point de pivot** est le point central autour duquel on effectue des séparations radiales pour garantir la symétrie de la coupe."},
                        {"text": "Il indique l'angle de la nuque.", "isCorrect": False, "rationale": "L'angle de la nuque est lié au contour de nuque."}
                    ],
                    "correction": "Le **point de pivot** est utilisé notamment dans les coupes dégradées radiales pour s'assurer que l'angle de projection par rapport à la tête est le même sur l'ensemble de la zone, garantissant l'harmonie du dégradé."
                },
                {
                    "questionNumber": 43,
                    "question": "Que signifie l'angle de 'projection' ou d'élévation lors de l'exécution d'une coupe ?",
                    "answerOptions": [
                        {"text": "L'inclinaison des ciseaux par rapport à la mèche.", "isCorrect": False, "rationale": "Ceci est l'angle de coupe."},
                        {"text": "L'angle entre la mèche peignée et la surface du crâne.", "isCorrect": True, "rationale": "L'angle de **projection** (ou d'élévation) est l'angle selon lequel la mèche est soulevée par rapport à la tête. Il influence directement le dégradé."},
                        {"text": "L'angle du corps du coiffeur.", "isCorrect": False, "rationale": "La posture du coiffeur est importante, mais ce n'est pas la projection."},
                        {"text": "L'angle de la raie sur le côté.", "isCorrect": False, "rationale": "La raie est une séparation."}
                    ],
                    "correction": "L'angle de **projection** est fondamental pour la technique de coupe. $0^{\\circ}$ donne une ligne pleine (masse), $45^{\\circ}$ donne un dégradé moyen, et $90^{\\circ}$ ou plus un dégradé prononcé."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel terme désigne la zone du crâne s'étendant du front jusqu'au point le plus haut de la tête ?",
                    "answerOptions": [
                        {"text": "La nuque", "isCorrect": False, "rationale": "La nuque est la partie arrière inférieure."},
                        {"text": "La zone occipitale", "isCorrect": False, "rationale": "L'occipital est l'arrière de la tête."},
                        {"text": "Le sommet (ou Top)", "isCorrect": True, "rationale": "Le **sommet** (ou top, ou crown) est la partie supérieure et avant du crâne."},
                        {"text": "La tempe", "isCorrect": False, "rationale": "La tempe est une zone latérale."}
                    ],
                    "correction": "Le **sommet** est une zone clé pour les coupes. C'est souvent là que l'on trouve les cheveux les plus courts ou que l'on crée le volume dans les coupes dégradées."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle est la principale fonction du peigne fin à queue lors d'une coupe ou d'une coloration ?",
                    "answerOptions": [
                        {"text": "Servir de guide pour la coupe des pointes.", "isCorrect": False, "rationale": "Le peigne classique sert de guide."},
                        {"text": "Apporter du volume lors du séchage.", "isCorrect": False, "rationale": "La brosse ronde est pour le volume."},
                        {"text": "Réaliser des séparations précises et propres.", "isCorrect": True, "rationale": "Le peigne à queue (fine) est essentiel pour créer des **séparations nettes** (lignes, raies) pour les mèches, les balayages et les coupes de précision."},
                        {"text": "Mélanger le produit colorant.", "isCorrect": False, "rationale": "Le bol et le pinceau sont utilisés pour le mélange."}
                    ],
                    "correction": "Le peigne à queue, qu'elle soit en plastique ou en métal, est l'outil indispensable du coiffeur pour le travail des **séparations**."
                },
                {
                    "questionNumber": 46,
                    "question": "Lors d'une mise en plis traditionnelle sur bigoudis, quel est le rôle du produit coiffant (lotion ou mousse) avant l'enroulage ?",
                    "answerOptions": [
                        {"text": "Ramollir la kératine pour une modification permanente.", "isCorrect": False, "rationale": "Ceci est le rôle de la lotion permanente."},
                        {"text": "Apporter un reflet temporaire.", "isCorrect": False, "rationale": "Ceci est le rôle d'une coloration fugace."},
                        {"text": "Créer et fixer temporairement les liaisons hydrogènes dans la nouvelle forme.", "isCorrect": True, "rationale": "Le produit de mise en plis (mousse, lotion) enveloppe le cheveu pour aider à rompre les liaisons hydrogènes (cheveux mouillés) et pour les **fixer** dans la forme du bigoudi en séchant."},
                        {"text": "Réduire la taille des ponts disulfures.", "isCorrect": False, "rationale": "Ceci est le rôle de l'agent réducteur."}
                    ],
                    "correction": "Le coiffage temporaire (mise en plis, brushing) repose sur les **liaisons hydrogènes**. Le produit coiffant permet de maintenir l'humidité et de solidifier le coiffage après séchage."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment appelle-t-on le fait de couper une mèche légèrement plus longue que le guide précédent pour créer une coupe en dégradé, tout en conservant une certaine masse ?",
                    "answerOptions": [
                        {"text": "Le pivotage", "isCorrect": False, "rationale": "Le pivotage est un mouvement de séparation."},
                        {"text": "L'inclinaison", "isCorrect": False, "rationale": "L'inclinaison est l'angle de la tête du client."},
                        {"text": "La projection en décroissance", "isCorrect": True, "rationale": "Cette technique, ou **dégradé progressif**, consiste à allonger légèrement chaque mèche coupée par rapport au guide pour obtenir un dégradé tout en préservant de la longueur et de la masse."},
                        {"text": "Le dégradé à $180^{\\circ}$", "isCorrect": False, "rationale": "Le $180^{\\circ}$ donne un dégradé très fort."}
                    ],
                    "correction": "La **projection en décroissance** (ou l'utilisation d'un guide immobile dans une coupe de masse) permet de créer un dégradé doux ou une forme arrondie, idéale pour éviter une coupe trop marquée et conserver du poids."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel accessoire est indispensable pour réaliser une coupe de précision sur cheveux très courts (coupe homme) ?",
                    "answerOptions": [
                        {"text": "Le ciseau sculpteur (désépaissir)", "isCorrect": False, "rationale": "Le ciseau sculpteur est pour désépaissir, pas pour la précision du contour."},
                        {"text": "La brosse squelette", "isCorrect": False, "rationale": "La brosse squelette est pour le séchage."},
                        {"text": "Le rasoir mécanique (ou tondeuse de finition)", "isCorrect": True, "rationale": "Le **rasoir mécanique** ou la tondeuse de finition (trimmer) est l'outil de choix pour définir les contours et la nuque de manière nette et précise sur cheveux courts."},
                        {"text": "La brosse ronde en céramique", "isCorrect": False, "rationale": "La brosse ronde est pour le brushing."}
                    ],
                    "correction": "La netteté des **contours** (nuque, tour d'oreille) est essentielle dans les coupes courtes pour homme. La tondeuse de finition permet une finition plus nette que les ciseaux seuls."
                },
                {
                    "questionNumber": 49,
                    "question": "Lors du séchage, quelle est la technique qui permet d'obtenir un effet lisse et brillant sur des cheveux longs en utilisant une brosse ronde ?",
                    "answerOptions": [
                        {"text": "Le 'Crush' (froissage)", "isCorrect": False, "rationale": "Le froissage crée un effet wavy ou bouclé."},
                        {"text": "Le 'Plaquage'", "isCorrect": False, "rationale": "Le plaquage est une technique de lissage au fer."},
                        {"text": "Le Brushing", "isCorrect": True, "rationale": "Le **brushing** est la technique qui utilise la brosse ronde et le séchoir pour lisser, boucler ou onduler les cheveux de manière temporaire tout en apportant de la brillance."},
                        {"text": "Le 'Texturage'", "isCorrect": False, "rationale": "Le texturage est une technique de coupe ou de produit."}
                    ],
                    "correction": "Le **brushing** combine la chaleur (qui rompt les liaisons hydrogènes) et la tension (de la brosse) pour modeler la forme du cheveu, créant une surface lisse qui reflète la lumière (brillance)."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le but de la technique d'effilage (ou désépaississement) ?",
                    "answerOptions": [
                        {"text": "Raccourcir la longueur des cheveux.", "isCorrect": False, "rationale": "Ceci est le but de la coupe classique."},
                        {"text": "Ajouter du volume aux cheveux fins.", "isCorrect": False, "rationale": "L'effilage enlève de la masse, ce qui réduit le volume au point d'effilage."},
                        {"text": "Réduire la masse et adoucir la ligne de coupe.", "isCorrect": True, "rationale": "L'**effilage** sert à alléger l'épaisseur d'une masse de cheveux (souvent les pointes) ou à fondre la ligne de coupe pour un rendu plus souple."},
                        {"text": "Créer des ondulations serrées.", "isCorrect": False, "rationale": "Ceci est le but de la permanente."}
                    ],
                    "correction": "L'**effilage** est souvent réalisé avec des ciseaux sculpteurs. Il est essentiel pour personnaliser une coupe en allégeant les chevelures épaisses ou pour créer un mouvement plus fluide sur les pointes."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle séparation est utilisée pour isoler la zone de la tête qui va du coin de l'œil jusqu'au sommet du crâne, et qui est souvent coupée en dernier ?",
                    "answerOptions": [
                        {"text": "Le point de pivot", "isCorrect": False, "rationale": "Le point de pivot est un point central."},
                        {"text": "La raie centrale", "isCorrect": False, "rationale": "La raie centrale est une ligne verticale."},
                        {"text": "La raie de séparation des zones frontales", "isCorrect": True, "rationale": "Cette zone est généralement délimitée par une raie qui va du coin de l'œil ou de la tempe jusqu'au sommet (point haut du crâne), délimitant le dessus de la tête (Top) pour les coupes homme ou les franges."},
                        {"text": "La zone occipitale", "isCorrect": False, "rationale": "L'occipital est la zone arrière."}
                    ],
                    "correction": "Les **zones frontales** (devant) et latérales sont souvent les plus visibles. Les séparations doivent être précises pour les isoler et les travailler en symétrie avec le reste de la coupe."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la principale caractéristique de la technique de 'coupe sur doigts' ?",
                    "answerOptions": [
                        {"text": "Elle est utilisée exclusivement pour couper des lignes droites.", "isCorrect": False, "rationale": "Elle est plus souvent utilisée pour les dégradés."},
                        {"text": "Elle permet de dégrader en utilisant le dos de la main comme guide.", "isCorrect": False, "rationale": "C'est l'inverse : les doigts tiennent la mèche."},
                        {"text": "Elle permet de contrôler la tension et l'élévation de la mèche pour la dégrader.", "isCorrect": True, "rationale": "La technique de **coupe sur doigts** permet au coiffeur de contrôler précisément la tension de la mèche et l'angle de projection (dégradé) par rapport au crâne."},
                        {"text": "Elle n'est utilisée que pour les coupes aux ciseaux sculpteurs.", "isCorrect": False, "rationale": "Elle est utilisée pour tous les types de ciseaux."}
                    ],
                    "correction": "La **coupe sur doigts** est la méthode la plus courante pour réaliser un dégradé. Les doigts servent à retenir la mèche, assurant une élévation et une tension uniformes."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel est l'effet recherché lorsque l'on utilise un fer à lisser sur des mèches fines à répétition ?",
                    "answerOptions": [
                        {"text": "Créer des boucles très serrées (permanentées).", "isCorrect": False, "rationale": "Le fer à lisser est pour le lissage ou les vagues amples, pas la permanente."},
                        {"text": "Ouvrir les écailles pour un meilleur dépôt de couleur.", "isCorrect": False, "rationale": "C'est le rôle du produit alcalin."},
                        {"text": "Rompre temporairement les liaisons hydrogènes pour un effet lisse et durable.", "isCorrect": True, "rationale": "Le fer à lisser (thermique) rompt les **liaisons hydrogènes**, permettant à la kératine de se fixer dans une forme lisse jusqu'au prochain contact avec l'eau."},
                        {"text": "Augmenter la porosité du cheveu.", "isCorrect": False, "rationale": "La chaleur excessive peut endommager, mais le but n'est pas d'augmenter la porosité."}
                    ],
                    "correction": "Le fer à lisser utilise une chaleur élevée pour **modifier temporairement** la structure du cheveu en le lissant. L'utilisation d'un protecteur thermique est cruciale."
                },
                {
                    "questionNumber": 54,
                    "question": "Dans le cas d'une coupe homme aux ciseaux et au peigne, quel est le rôle du peigne ?",
                    "answerOptions": [
                        {"text": "Il sert uniquement à démêler la mèche avant de la couper.", "isCorrect": False, "rationale": "Son rôle est plus technique dans cette méthode."},
                        {"text": "Il sert à retenir et à soulever les cheveux du crâne pour créer la mèche guide.", "isCorrect": True, "rationale": "Dans la technique **ciseaux sur peigne**, le peigne définit la longueur en retenant la mèche et sert de guide pour la coupe et la progression."},
                        {"text": "Il permet de vérifier la symétrie de la coupe après sa réalisation.", "isCorrect": False, "rationale": "Ceci est fait avec un miroir et un examen visuel."},
                        {"text": "Il protège le crâne des ciseaux.", "isCorrect": False, "rationale": "Le rôle est technique, pas sécuritaire."}
                    ],
                    "correction": "La technique **ciseaux sur peigne** est essentielle pour les coupes courtes (homme ou femme) et permet un contrôle précis de la longueur, créant des lignes douces et fluides."
                },
                {
                    "questionNumber": 55,
                    "question": "Quelle est l'incidence d'un cheveu tenu avec une forte tension lors de la coupe ?",
                    "answerOptions": [
                        {"text": "La coupe sera plus souple et légère.", "isCorrect": False, "rationale": "L'inverse est souvent vrai."},
                        {"text": "La ligne de coupe sera plus nette, mais le cheveu aura tendance à remonter au séchage.", "isCorrect": True, "rationale": "Une tension **trop forte** étire le cheveu au maximum. Au séchage, le cheveu reprend sa forme naturelle, ce qui entraîne une **remontée** de la ligne de coupe et une perte de la longueur souhaitée."},
                        {"text": "La ligne de coupe sera floue et mal définie.", "isCorrect": False, "rationale": "L'inverse est souvent vrai."},
                        {"text": "Cela facilite le dégradé.", "isCorrect": False, "rationale": "La tension est indépendante du dégradé (projection)."}
                    ],
                    "correction": "La **tension** doit être maîtrisée. Une tension trop forte sur les cheveux bouclés, fins ou très élastiques est une erreur courante qui entraîne une ligne de coupe finale inégale et plus courte que prévu."
                },
                {
                    "questionNumber": 56,
                    "question": "Dans la géométrie de la tête, où se situe la zone occipitale ?",
                    "answerOptions": [
                        {"text": "Juste derrière les oreilles (zone temporale).", "isCorrect": False, "rationale": "Ceci est la zone sous-occipitale/latérale."},
                        {"text": "À la base de la nuque.", "isCorrect": False, "rationale": "Ceci est la nuque."},
                        {"text": "À l'arrière du crâne, au-dessus de la nuque.", "isCorrect": True, "rationale": "L'**occipital** est la zone du crâne qui forme un renflement à l'arrière, entre le sommet et la nuque."},
                        {"text": "Au centre du front.", "isCorrect": False, "rationale": "Ceci est la zone frontale."}
                    ],
                    "correction": "L'**os occipital** est le repère osseux de l'arrière de la tête. Cette zone est cruciale pour le positionnement du dégradé ou de la masse dans les coupes au carré."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est l'objectif du séchage en 'mouvement de serpent' (mouvement en S) avec un fer à lisser ?",
                    "answerOptions": [
                        {"text": "Obtenir un lissage parfait et sans volume.", "isCorrect": False, "rationale": "Ceci est le lissage droit classique."},
                        {"text": "Créer des ondulations souples et naturelles (effet 'wavy').", "isCorrect": True, "rationale": "Le mouvement en 'S' avec le fer à lisser permet de créer des **ondulations souples** ou 'wavy', très populaires, sans créer une boucle serrée comme un fer à friser."},
                        {"text": "Réaliser un frisage permanent.", "isCorrect": False, "rationale": "Ceci est le rôle de la permanente."},
                        {"text": "Faire adhérer les mèches coupées au guide.", "isCorrect": False, "rationale": "Ceci est une technique de coupe."}
                    ],
                    "correction": "Le coiffage avec des **vagues** souples nécessite un mouvement de **va-et-vient** (le 'S') avec le fer à lisser ou un fer à boucler de gros diamètre."
                },
                {
                    "questionNumber": 58,
                    "question": "L'angle de 'chute' (ou retombée naturelle) d'une mèche est un critère essentiel pour le diagnostic. Comment est-il mesuré ?",
                    "answerOptions": [
                        {"text": "Par la longueur totale du cheveu.", "isCorrect": False, "rationale": "La longueur n'est pas l'angle de chute."},
                        {"text": "Par le diamètre de la fibre.", "isCorrect": False, "rationale": "Le diamètre influence, mais ne mesure pas l'angle."},
                        {"text": "Par l'angle que forme le cheveu avec le crâne lorsqu'il est au repos.", "isCorrect": True, "rationale": "L'angle de **chute naturelle** est la manière dont le cheveu retombe naturellement sans tension. Il détermine la façon dont la coupe finale sera vue et est crucial pour la réalisation d'une frange ou d'une raie."},
                        {"text": "Par la couleur du pigment.", "isCorrect": False, "rationale": "La couleur n'a pas de rapport avec l'angle de chute."}
                    ],
                    "correction": "L'angle de **chute** varie d'un client à l'autre et doit être pris en compte avant de couper. Si la mèche est peignée dans une direction qui n'est pas sa chute naturelle, le résultat final peut être décevant."
                },
                {
                    "questionNumber": 59,
                    "question": "Dans le cas d'une coupe dégradée, à quoi sert le 'guide' (ou mèche témoin) ?",
                    "answerOptions": [
                        {"text": "Il sert à déterminer la quantité de produit à appliquer.", "isCorrect": False, "rationale": "Le guide est pour la coupe."},
                        {"text": "C'est la première mèche coupée qui détermine la longueur des mèches suivantes.", "isCorrect": True, "rationale": "Le **guide** est la mèche de référence dont la longueur sert de repère à toutes les mèches adjacentes, assurant la cohésion et la progression de la coupe."},
                        {"text": "Il indique l'épaisseur du cheveu (son diamètre).", "isCorrect": False, "rationale": "Ceci est la texture."},
                        {"text": "Il permet de créer des mèches artificielles.", "isCorrect": False, "rationale": "Ceci est une extension."}
                    ],
                    "correction": "Le **guide** peut être 'mobile' (la longueur progresse) ou 'fixe' (toutes les mèches sont ramenées au même point central). C'est le point de départ de toute coupe de précision."
                },
                {
                    "questionNumber": 60,
                    "question": "Qu'est-ce qu'une 'coupe pleine' ?",
                    "answerOptions": [
                        {"text": "Une coupe avec une élévation de $90^{\\circ}$.", "isCorrect": False, "rationale": "Ceci est un dégradé."},
                        {"text": "Une coupe qui nécessite une permanente.", "isCorrect": False, "rationale": "Le terme n'est pas lié à la permanente."},
                        {"text": "Une coupe réalisée sans dégradé, où tous les cheveux ont la même longueur au point de chute (élévation $0^{\\circ}$).", "isCorrect": True, "rationale": "La **coupe pleine** (ou coupe de masse, ou coupe droite) est réalisée avec une élévation à **$0^{\\circ}$**, produisant une ligne nette et une concentration maximale de la masse aux extrémités."},
                        {"text": "Une coupe réalisée uniquement au rasoir.", "isCorrect": False, "rationale": "Le rasoir est un outil, pas une technique de masse."}
                    ],
                    "correction": "La **coupe pleine** est la base de nombreuses coiffures, notamment le carré classique. Elle se caractérise par une ligne finale nette et un poids maximal sur la pointe."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : HYGIÈNE, SOINS ET LÉGISLATION (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Hygiène, Soins et Législation (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel terme technique désigne le processus qui vise à éliminer ou à tuer les micro-organismes (bactéries, virus, champignons) sur des surfaces inertes ?",
                    "answerOptions": [
                        {"text": "Le nettoyage", "isCorrect": False, "rationale": "Le nettoyage élimine les salissures visibles, pas nécessairement les micro-organismes."},
                        {"text": "L'asepsie", "isCorrect": False, "rationale": "L'asepsie est l'absence totale de germes."},
                        {"text": "La désinfection", "isCorrect": True, "rationale": "La **désinfection** est l'opération qui permet de tuer ou d'inhiber les micro-organismes (à l'exception de certaines spores) sur des surfaces inertes (outils, plans de travail)."},
                        {"text": "La stérilisation", "isCorrect": False, "rationale": "La stérilisation est une élimination totale, réservée aux dispositifs médicaux."}
                    ],
                    "correction": "La **désinfection** est la procédure la plus courante et la plus importante en salon. Elle doit être effectuée après le **nettoyage** (l'élimination des salissures visibles) pour être efficace."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la principale maladie fongique du cuir chevelu que le coiffeur doit identifier et refuser de traiter ?",
                    "answerOptions": [
                        {"text": "La séborrhée", "isCorrect": False, "rationale": "La séborrhée est un état lié à l'excès de sébum."},
                        {"text": "L'alopécie", "isCorrect": False, "rationale": "L'alopécie est la chute de cheveux."},
                        {"text": "La teigne", "isCorrect": True, "rationale": "La **teigne** est une mycose (champignon) très contagieuse qui nécessite un traitement médical et pour laquelle le coiffeur doit refuser le service pour éviter la propagation."},
                        {"text": "La trichoptilose", "isCorrect": False, "rationale": "La trichoptilose est la fourche du cheveu."}
                    ],
                    "correction": "La **teigne** est caractérisée par des plaques rondes, squameuses, avec des cheveux cassés près de la racine. Elle est hautement contagieuse. Le coiffeur doit orienter le client vers un médecin ou un dermatologue."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel produit de soin est formulé avec un pH acide et a pour principal objectif de refermer les écailles de la cuticule après un traitement chimique (coloration, permanente) ?",
                    "answerOptions": [
                        {"text": "Le shampoing clarifiant (pH alcalin)", "isCorrect": False, "rationale": "Le clarifiant est alcalin ou neutre."},
                        {"text": "Le masque protéiné (pH neutre)", "isCorrect": False, "rationale": "Le masque vise la réparation interne."},
                        {"text": "Le conditionneur ou après-shampoing (Rinçage acide)", "isCorrect": True, "rationale": "Les **conditionneurs** et les rinçages acides (pH bas) sont utilisés pour neutraliser l'alcalinité des traitements, lisser la cuticule et apporter brillance et démêlage."},
                        {"text": "Le sérum pointes sèches (pH élevé)", "isCorrect": False, "rationale": "Le sérum est un soin filmogène, non pH-actif."}
                    ],
                    "correction": "Le cheveu et le cuir chevelu ont besoin de retrouver leur **pH acide** naturel (4.5 à 5.5) après une agression chimique. Le conditionneur ou le soin post-couleur remplissent cette fonction."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la zone du cheveu qui doit être principalement ciblée lors de l'application d'un masque capillaire hydratant et nourrissant ?",
                    "answerOptions": [
                        {"text": "Le cuir chevelu uniquement (pour le stimuler).", "isCorrect": False, "rationale": "Le masque risque de graisser le cuir chevelu, sauf si spécifiquement indiqué."},
                        {"text": "Les racines et les 5 premiers centimètres.", "isCorrect": False, "rationale": "Cette zone est souvent saine."},
                        {"text": "Les pointes et les demi-longueurs (zone la plus ancienne et fragilisée).", "isCorrect": True, "rationale": "Le masque doit cibler les **longueurs et pointes**, car elles sont la partie la plus ancienne, la plus exposée et la plus poreuse du cheveu."},
                        {"text": "L'ensemble de la chevelure, y compris le visage.", "isCorrect": False, "rationale": "Le visage est exclu."}
                    ],
                    "correction": "Les **longueurs et pointes** ont besoin d'être nourries car elles sont souvent sèches et abîmées. Il est généralement conseillé d'éviter le cuir chevelu pour ne pas alourdir la chevelure et créer un effet gras."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le risque professionnel principal lié à la manipulation répétée de produits chimiques (colorants, permanentes) sans gants appropriés ?",
                    "answerOptions": [
                        {"text": "Une chute de cheveux précoce.", "isCorrect": False, "rationale": "Ceci est lié à des facteurs internes ou à une intoxication aigüe."},
                        {"text": "Le développement d'une allergie respiratoire.", "isCorrect": False, "rationale": "Ceci est lié à l'inhalation des vapeurs."},
                        {"text": "L'eczéma de contact ou une dermatite professionnelle.", "isCorrect": True, "rationale": "Le risque majeur est la sensibilisation cutanée, conduisant à l'**eczéma de contact** (ou dermatite) due à la pénétration des allergènes et des produits agressifs dans la peau."},
                        {"text": "Une brûlure thermique.", "isCorrect": False, "rationale": "Ceci est lié à la chaleur (fers, séchoirs)."}
                    ],
                    "correction": "La protection des mains (port de gants) est essentielle. La **dermatite de contact** est l'une des maladies professionnelles les plus courantes chez les coiffeurs et peut devenir très invalidante."
                },
                {
                    "questionNumber": 66,
                    "question": "Que doit impérativement faire le coiffeur après la coupe et avant le coiffage, conformément aux règles d'hygiène ?",
                    "answerOptions": [
                        {"text": "Appliquer un masque hydratant.", "isCorrect": False, "rationale": "Le masque n'est pas une obligation d'hygiène."},
                        {"text": "Désinfecter les ciseaux et le peigne.", "isCorrect": False, "rationale": "C'est avant et après chaque client."},
                        {"text": "Changer le peignoir et rincer les cheveux coupés.", "isCorrect": True, "rationale": "Le client doit être débarrassé des cheveux coupés (poudres, brossage, rinçage) et le peignoir de coupe doit être retiré et mis à laver avant l'étape de coiffage."},
                        {"text": "Proposer la carte de fidélité.", "isCorrect": False, "rationale": "Ceci est commercial."}
                    ],
                    "correction": "Retirer les cheveux coupés et changer le peignoir (pour un peignoir de coiffage propre) est une étape de confort et d'hygiène pour le client avant de passer au séchage et au coiffage final."
                },
                {
                    "questionNumber": 67,
                    "question": "Selon la législation, quel est le document obligatoire qui doit être affiché de manière lisible et à proximité des postes de travail ?",
                    "answerOptions": [
                        {"text": "Le certificat d'aptitude professionnelle (CAP).", "isCorrect": False, "rationale": "Ceci est un diplôme."},
                        {"text": "Le prix de tous les produits de revente.", "isCorrect": False, "rationale": "Seuls les prix des prestations sont obligatoires."},
                        {"text": "La liste des prix des principales prestations TTC.", "isCorrect": True, "rationale": "L'affichage des **prix des prestations** les plus courantes (coupe, brushing, couleur) est une obligation légale de protection du consommateur."},
                        {"text": "Le bilan comptable de l'année précédente.", "isCorrect": False, "rationale": "Ceci est confidentiel."}
                    ],
                    "correction": "L'**affichage des prix** (TTC) est obligatoire et doit être facilement visible. Ne pas afficher les prix est passible d'une amende."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelles sont les précautions à prendre lors de l'utilisation d'un sèche-cheveux (séchoir à main) ?",
                    "answerOptions": [
                        {"text": "Le tenir sans buse pour une meilleure diffusion de la chaleur.", "isCorrect": False, "rationale": "La buse est essentielle pour diriger la chaleur."},
                        {"text": "Ne jamais utiliser de protecteur thermique.", "isCorrect": False, "rationale": "Le protecteur thermique est recommandé."},
                        {"text": "Ne pas plaquer le flux d'air chaud sur une même zone de manière prolongée et utiliser la buse.", "isCorrect": True, "rationale": "Il faut éviter de brûler le cuir chevelu ou le cheveu. La **buse** permet de concentrer le flux d'air pour un meilleur lissage tout en maintenant une distance sécuritaire."},
                        {"text": "Utiliser la puissance maximale même sur cheveux fins.", "isCorrect": False, "rationale": "La puissance doit être adaptée au type de cheveu."}
                    ],
                    "correction": "L'utilisation de la **buse** et le maintien d'une distance de sécurité sont essentiels pour éviter la surchauffe, l'assèchement excessif de la fibre et les brûlures du cuir chevelu."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel terme désigne l'action d'éliminer les poux et les lentes ?",
                    "answerOptions": [
                        {"text": "La décontamination", "isCorrect": False, "rationale": "La décontamination est plus générale (produits chimiques)."},
                        {"text": "Le défrisage", "isCorrect": False, "rationale": "Le défrisage est une technique de lissage chimique."},
                        {"text": "La pédiculose", "isCorrect": False, "rationale": "La pédiculose est l'infestation (le nom du problème)."},
                        {"text": "La dépédiculisation", "isCorrect": True, "rationale": "La **dépédiculisation** est le processus spécifique de traitement et d'élimination des poux (Pediculus humanus capitis)."}
                    ],
                    "correction": "La **dépédiculisation** est le terme correct. Le coiffeur doit identifier la pédiculose et refuser la prestation pour éviter de contaminer le salon (serviettes, peignes, matériel)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle est la principale fonction d'un 'shampoing clarifiant' ou 'chélatant' ?",
                    "answerOptions": [
                        {"text": "Augmenter l'épaisseur du cheveu fin.", "isCorrect": False, "rationale": "Ceci est le rôle des shampoings volumateurs."},
                        {"text": "Fixer les pigments de couleur pour qu'ils durent plus longtemps.", "isCorrect": False, "rationale": "Ceci est le rôle des shampoings pour cheveux colorés."},
                        {"text": "Éliminer les résidus (silicones, minéraux, calcaire) accumulés sur la fibre.", "isCorrect": True, "rationale": "Le shampoing **clarifiant** est conçu pour décaper la fibre des résidus cosmétiques, minéraux ou des traces de chlore, préparant le cheveu à recevoir une coloration ou un soin profond."},
                        {"text": "Hydrater le cuir chevelu sec.", "isCorrect": False, "rationale": "Le clarifiant peut être asséchant."}
                    ],
                    "correction": "Le shampoing **clarifiant** est souvent utilisé avant une coloration pour garantir une pénétration uniforme ou avant un soin pour maximiser l'efficacité des actifs."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel équipement de protection individuelle (EPI) est le plus important pour le coiffeur lors de l'application de décolorant ou de produits agressifs ?",
                    "answerOptions": [
                        {"text": "Le tablier de coupe en tissu.", "isCorrect": False, "rationale": "Le tablier protège les vêtements."},
                        {"text": "Les lunettes de protection.", "isCorrect": False, "rationale": "Elles sont utiles, mais moins critiques que la protection des mains."},
                        {"text": "Les gants de protection jetables (Nitrile ou Vinyle).", "isCorrect": True, "rationale": "Les **gants** sont l'EPI n°1 pour protéger la peau des mains, constamment exposées aux produits chimiques et à l'eau."},
                        {"text": "Le bonnet jetable.", "isCorrect": False, "rationale": "Il sert à protéger les cheveux du coiffeur."}
                    ],
                    "correction": "Les **gants de protection** sont indispensables pour prévenir l'irritation, la dermatite et l'absorption de substances chimiques potentiellement nocives."
                },
                {
                    "questionNumber": 72,
                    "question": "Quelle est la principale différence entre un conditionneur (après-shampoing) et un masque capillaire ?",
                    "answerOptions": [
                        {"text": "Le conditionneur est toujours acide, le masque est toujours neutre.", "isCorrect": False, "rationale": "Les deux peuvent être acides."},
                        {"text": "Le conditionneur agit en surface, le masque agit en profondeur.", "isCorrect": True, "rationale": "Le **conditionneur** (après-shampoing) a une action rapide et de surface (démêlage, lissage). Le **masque** est un soin plus riche, nécessitant un temps de pose pour pénétrer en profondeur (cortex) et réparer."},
                        {"text": "Le masque contient des tensioactifs, le conditionneur non.", "isCorrect": False, "rationale": "Les tensioactifs sont dans le shampoing."},
                        {"text": "Le conditionneur est réservé aux cheveux fins, le masque aux cheveux épais.", "isCorrect": False, "rationale": "Les deux sont adaptés à tous les types selon leur formulation."}
                    ],
                    "correction": "Le **masque** a un rôle de **traitement** (réparation interne/nutrition) et nécessite donc un temps de pose. Le conditionneur a un rôle de **finition** (lissage de la cuticule et démêlage) et est appliqué rapidement."
                },
                {
                    "questionNumber": 73,
                    "question": "Qu'est-ce que l'effluvium télogène, un diagnostic parfois rencontré en salon ?",
                    "answerOptions": [
                        {"text": "Une chute de cheveux saisonnière, souvent diffuse, suite à un stress ou une carence.", "isCorrect": True, "rationale": "L'**effluvium télogène** est une accélération de la chute (plus de 100 cheveux par jour) liée à un déséquilibre du cycle pilaire (passage massif en phase télogène) après un événement stressant."},
                        {"text": "Une chute de cheveux localisée (calvitie) chez l'homme.", "isCorrect": False, "rationale": "Ceci est l'alopécie androgénétique."},
                        {"text": "Une inflammation chronique du cuir chevelu.", "isCorrect": False, "rationale": "Ceci est une dermatite ou un psoriasis."},
                        {"text": "Une maladie auto-immune (pelade).", "isCorrect": False, "rationale": "Ceci est l'alopécie areata."}
                    ],
                    "correction": "L'**effluvium télogène** est une chute souvent réversible. Il nécessite des soins stimulants et, si la cause est persistante, un avis médical."
                },
                {
                    "questionNumber": 74,
                    "question": "Quelle température maximale est considérée comme 'à risque' pour les outils chauffants (fer à lisser, fer à friser) sur des cheveux fins et sensibilisés ?",
                    "answerOptions": [
                        {"text": "Entre $80^{\\circ}$C et $120^{\\circ}$C", "isCorrect": False, "rationale": "C'est la fourchette basse, souvent recommandée."},
                        {"text": "Entre $120^{\\circ}$C et $160^{\\circ}$C", "isCorrect": False, "rationale": "C'est la fourchette idéale pour cheveux fins."},
                        {"text": "Au-delà de $180^{\\circ}$C et $200^{\\circ}$C", "isCorrect": True, "rationale": "Les températures supérieures à $180^{\\circ}$C (voire $200^{\\circ}$C) peuvent entraîner la **dénaturation de la kératine** des cheveux fins ou décolorés, provoquant la casse et l'apparition de 'bulles' (dommages irréversibles)."},
                        {"text": "Entre $50^{\\circ}$C et $70^{\\circ}$C", "isCorrect": False, "rationale": "C'est la température du séchage au diffuseur."}
                    ],
                    "correction": "La température doit toujours être adaptée. Pour les cheveux fragiles ou très éclaircis, il ne faut idéalement pas dépasser $160^{\\circ}$C pour éviter les dommages thermiques. Le seuil de $180^{\\circ}$C est le maximum à utiliser avec prudence."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle substance toxique peut être émise par certains défrisages chimiques contenant des aldéhydes, nécessitant une bonne ventilation en salon ?",
                    "answerOptions": [
                        {"text": "L'oxygène (O2)", "isCorrect": False, "rationale": "L'oxygène est inoffensif."},
                        {"text": "Le Peroxyde d'hydrogène", "isCorrect": False, "rationale": "Le Peroxyde est un oxydant, mais pas une substance de défrisage à aldéhydes."},
                        {"text": "Le Formol (Formadéhyde)", "isCorrect": True, "rationale": "Le **Formol** (ou ses libérateurs) est un agent lissant puissant, mais il est classé comme cancérogène. Son usage est très réglementé, voire interdit, dans de nombreux pays. Une excellente ventilation est vitale s'il est utilisé."},
                        {"text": "Le Silicone", "isCorrect": False, "rationale": "Le silicone est un agent cosmétique (gainage)."}
                    ],
                    "correction": "Le **Formol** est une substance potentiellement très dangereuse, surtout lorsqu'elle est chauffée (lissage brésilien par exemple). Les coiffeurs doivent exiger des produits sans formaldéhyde (formol) pour la sécurité de tous."
                },
                {
                    "questionNumber": 76,
                    "question": "Lors du shampooing, quel est le mouvement de massage à privilégier sur le cuir chevelu ?",
                    "answerOptions": [
                        {"text": "Des mouvements circulaires amples avec les ongles.", "isCorrect": False, "rationale": "Les ongles peuvent irriter le cuir chevelu."},
                        {"text": "Des mouvements de va-et-vient énergiques (frottements).", "isCorrect": False, "rationale": "Les frottements peuvent créer des nœuds et des frictions."},
                        {"text": "Des mouvements doux et circulaires avec la pulpe des doigts.", "isCorrect": True, "rationale": "Le massage doit être doux, stimulant et non irritant, effectué avec la **pulpe des doigts** pour décoller les impuretés et stimuler la microcirculation."},
                        {"text": "Uniquement des pressions sans mouvement.", "isCorrect": False, "rationale": "Le mouvement est nécessaire pour le nettoyage."}
                    ],
                    "correction": "Le bon geste de shampooing est un **massage doux** avec la pulpe des doigts. Un massage trop énergique ou l'utilisation des ongles risque de créer des lésions et de stimuler une production excessive de sébum (effet rebond)."
                },
                {
                    "questionNumber": 77,
                    "question": "Quelle est la durée de validité du 'Document Unique d’Évaluation des Risques Professionnels' (DUERP) dans une entreprise de coiffure ?",
                    "answerOptions": [
                        {"text": "Il est mis à jour tous les 5 ans.", "isCorrect": False, "rationale": "La mise à jour doit être plus fréquente."},
                        {"text": "Il n'est pas obligatoire dans les salons de moins de 10 salariés.", "isCorrect": False, "rationale": "Il est obligatoire dès le premier salarié."},
                        {"text": "Il doit être mis à jour au moins une fois par an et à chaque modification importante.", "isCorrect": True, "rationale": "Le **DUERP** est obligatoire dès l'embauche du premier salarié et doit être mis à jour **au moins annuellement** ou lors de tout changement majeur (nouveau matériel, nouvel agencement, accident de travail)."},
                        {"text": "Il est valable à vie tant que l'entreprise ne change pas d'adresse.", "isCorrect": False, "rationale": "Ceci est faux."}
                    ],
                    "correction": "Le **DUERP** est un document légal essentiel qui recense les risques professionnels (postures, produits chimiques, bruit, etc.) pour la santé et la sécurité des employés."
                },
                {
                    "questionNumber": 78,
                    "question": "À quoi sert un peignoir 'jetable' ou 'à usage unique' ?",
                    "answerOptions": [
                        {"text": "À protéger le client des coupures de ciseaux.", "isCorrect": False, "rationale": "Ceci est le rôle du col protecteur."},
                        {"text": "À garantir une hygiène irréprochable et éviter la contamination croisée entre clients.", "isCorrect": True, "rationale": "Le peignoir **jetable** garantit qu'il n'y a pas de transfert de salissures, produits ou parasites d'un client à l'autre (contamination croisée)."},
                        {"text": "À donner une touche luxueuse au salon.", "isCorrect": False, "rationale": "L'objectif est l'hygiène."},
                        {"text": "À remplacer le shampoing.", "isCorrect": False, "rationale": "Ceci n'a aucun sens."}
                    ],
                    "correction": "Les peignoirs, serviettes et capes doivent être **propres** pour chaque client. Le jetable est une solution pour les zones de grande affluence ou pour les prestations très salissantes (décapage)."
                },
                {
                    "questionNumber": 79,
                    "question": "L'utilisation de la chaleur (bonnets chauffants, climazon) lors d'un masque de soin a pour but de :",
                    "answerOptions": [
                        {"text": "Accélérer l'évaporation de l'eau contenue dans le cheveu.", "isCorrect": False, "rationale": "Ceci assécherait le cheveu."},
                        {"text": "Rompre les liaisons disulfures pour rendre le cheveu plus souple.", "isCorrect": False, "rationale": "Ceci est le rôle de la permanente."},
                        {"text": "Dilater légèrement les écailles pour améliorer la pénétration des actifs.", "isCorrect": True, "rationale": "La **chaleur douce** permet d'écarter légèrement les écailles de la cuticule, favorisant la pénétration du masque hydratant ou nourrissant dans le cortex."},
                        {"text": "Activer la circulation sanguine du cuir chevelu.", "isCorrect": False, "rationale": "La chaleur du soin est centrée sur la fibre."},
                    ],
                    "correction": "La **chaleur** (passive ou active) est un accélérateur de pénétration. Elle optimise l'efficacité des actifs de soin, d'où l'utilisation de climazons ou de serviettes chaudes."
                },
                {
                    "questionNumber": 80,
                    "question": "En cas de brûlure chimique due à un produit colorant (sur le cuir chevelu par exemple), quel est le premier geste d'urgence à effectuer ?",
                    "answerOptions": [
                        {"text": "Appliquer immédiatement une crème anti-inflammatoire.", "isCorrect": False, "rationale": "Ce n'est pas le premier geste."},
                        {"text": "Neutraliser l'effet du produit avec de l'acide acétique (vinaigre).", "isCorrect": False, "rationale": "Ceci est risqué et peut aggraver la situation."},
                        {"text": "Rincer immédiatement et abondamment à l'eau claire et froide.", "isCorrect": True, "rationale": "Le premier geste face à toute brûlure chimique est de stopper la réaction en **rinçant abondamment à l'eau froide** pendant au moins 10 à 15 minutes."},
                        {"text": "Laisser sécher à l'air libre et observer.", "isCorrect": False, "rationale": "Ceci laisserait la brûlure progresser."}
                    ],
                    "correction": "Le rinçage immédiat à l'**eau froide** permet d'éliminer le produit et d'arrêter la réaction chimique pour limiter la profondeur de la brûlure."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : PRATIQUE COMMERCIALE ET DIAGNOSTIC CLIENT (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Pratique Commerciale et Diagnostic Client (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la première étape obligatoire du diagnostic en salon avant d'entamer toute prestation de coupe ou technique ?",
                    "answerOptions": [
                        {"text": "Le test d'allergie (48h avant).", "isCorrect": False, "rationale": "Le test d'allergie est pour la coloration, non la coupe."},
                        {"text": "Le toucher et l'examen visuel du cuir chevelu et du cheveu.", "isCorrect": True, "rationale": "Le **diagnostic** commence par l'observation et le toucher pour évaluer la nature, l'état, la porosité, la densité et l'état du cuir chevelu du client."},
                        {"text": "La vente d'un produit additionnel.", "isCorrect": False, "rationale": "Ceci est une démarche commerciale secondaire."},
                        {"text": "L'analyse des tendances de mode.", "isCorrect": False, "rationale": "Ceci influence le choix, mais n'est pas la première étape du diagnostic technique."}
                    ],
                    "correction": "Le **diagnostic** est la base du métier. Il permet d'adapter la technique, les produits et les temps de pose à la réalité de la chevelure du client pour garantir un résultat professionnel."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le but principal de la technique de 'reformulation' lors de l'entretien client ?",
                    "answerOptions": [
                        {"text": "Corriger le client s'il utilise des termes techniques incorrects.", "isCorrect": False, "rationale": "Le rôle est d'assurer la compréhension, pas de corriger le client."},
                        {"text": "Vérifier la bonne compréhension des attentes du client avant de commencer.", "isCorrect": True, "rationale": "La **reformulation** (répéter avec ses propres mots ce que le client a exprimé) est essentielle pour s'assurer que le coiffeur et le client sont sur la même longueur d'onde et éviter les erreurs."},
                        {"text": "Lui proposer un autre style.", "isCorrect": False, "rationale": "Ceci est une suggestion, pas une reformulation."},
                        {"text": "Évaluer sa capacité à payer la prestation.", "isCorrect": False, "rationale": "Ceci n'est pas professionnel."}
                    ],
                    "correction": "La **reformulation** est un outil de communication. Elle valide la demande ('Si je comprends bien, vous voulez une base 6.0 avec des reflets 7.4 ?') et sécurise la prestation."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la principale caractéristique d'un cheveu de 'nature fine' ?",
                    "answerOptions": [
                        {"text": "Il ne prend pas la couleur.", "isCorrect": False, "rationale": "La nature n'empêche pas la couleur."},
                        {"text": "Son diamètre est inférieur à 0,05 mm.", "isCorrect": True, "rationale": "Un cheveu **fin** a un diamètre faible (moins de 0,05 mm), ce qui le rend moins résistant et plus susceptible de s'alourdir ou de manquer de volume."},
                        {"text": "Il est obligatoirement bouclé.", "isCorrect": False, "rationale": "Le cheveu fin peut être raide, ondulé ou bouclé."},
                        {"text": "Il a une porosité très élevée.", "isCorrect": False, "rationale": "La porosité est l'état, non la nature."}
                    ],
                    "correction": "La **nature fine** demande des produits légers, des coupes en masse (pour le volume) et des techniques de coloration douces, car la fibre est plus délicate."
                },
                {
                    "questionNumber": 84,
                    "question": "Lors d'une vente de produits, que signifie 'adapter son argumentation au profil du client' ?",
                    "answerOptions": [
                        {"text": "Parler plus fort si le client est âgé.", "isCorrect": False, "rationale": "Ceci est inapproprié."},
                        {"text": "Ne proposer que des produits chers, sans tenir compte de la prestation.", "isCorrect": False, "rationale": "Ceci est une mauvaise pratique commerciale."},
                        {"text": "Mettre en avant l'avantage du produit en fonction du problème identifié lors du diagnostic.", "isCorrect": True, "rationale": "La vente doit être un **conseil** basé sur le diagnostic. Si le cheveu est sec, on argumente sur l'hydratation (avantage) plutôt que sur le prix (caractéristique)."},
                        {"text": "Dire au client qu'il a de mauvais cheveux pour justifier la vente.", "isCorrect": False, "rationale": "Ceci est une attitude négative et contre-productive."}
                    ],
                    "correction": "Une bonne pratique commerciale est de faire une 'vente-conseil'. Le coiffeur doit utiliser le **diagnostic** (cheveu gras, sec, cassant) pour justifier et personnaliser la recommandation du produit."
                },
                {
                    "questionNumber": 85,
                    "question": "Qu'est-ce qu'un 'chèque cadeau' du point de vue de la gestion commerciale d'un salon de coiffure ?",
                    "answerOptions": [
                        {"text": "Une charge (dépense) pour le salon.", "isCorrect": False, "rationale": "C'est une recette (vente)."},
                        {"text": "Une remise faite au client pour sa fidélité.", "isCorrect": False, "rationale": "Ceci est une réduction."},
                        {"text": "Un produit financier qui crée une créance du client envers le salon.", "isCorrect": True, "rationale": "Le chèque cadeau est une **vente encaissée d'avance** qui crée une dette ou une obligation pour le salon de fournir une prestation future. C'est une méthode d'augmentation du chiffre d'affaires immédiat."},
                        {"text": "Un moyen de paiement qui ne peut être utilisé que pour les produits de revente.", "isCorrect": False, "rationale": "Il peut être utilisé pour les prestations."}
                    ],
                    "correction": "Les chèques cadeaux sont une ressource de trésorerie immédiate, mais ils représentent un service qui devra être rendu (une **créance client**)."
                },
                {
                    "questionNumber": 86,
                    "question": "Si une cliente avec 50 % de cheveux blancs souhaite une couleur rousse (ex: 6.4), quelle est la technique de coloration de base à privilégier ?",
                    "answerOptions": [
                        {"text": "Une coloration ton sur ton uniquement.", "isCorrect": False, "rationale": "Le ton sur ton ne couvre pas bien les cheveux blancs (transparence)."},
                        {"text": "Une coloration permanente avec un oxydant 40 volumes.", "isCorrect": False, "rationale": "Le 40 volumes est trop puissant pour une simple couverture."},
                        {"text": "Un mélange de la couleur choisie (6.4) avec sa base naturelle (6.0).", "isCorrect": True, "rationale": "Pour couvrir un fort pourcentage de blancs avec un reflet, il faut obligatoirement ajouter une part de la **base naturelle** (la plus proche de la hauteur de ton) pour apporter le pigment de fond nécessaire."},
                        {"text": "Une décoloration totale suivie de la couleur 6.4.", "isCorrect": False, "rationale": "Ceci est trop agressif pour une simple couverture."}
                    ],
                    "correction": "Les cheveux blancs ont besoin de **pigments de fond** (la base naturelle .0) pour que le reflet (le .4) s'accroche et que la couverture soit opaque et durable. C'est le principe du mouillage ou du mélange base + reflet."
                },
                {
                    "questionNumber": 87,
                    "question": "Qu'est-ce qu'un cheveu 'hydrophile' (très poreux) du point de vue de la coiffure ?",
                    "answerOptions": [
                        {"text": "Un cheveu qui repousse l'eau et les produits.", "isCorrect": False, "rationale": "Ceci est hydrophobe."},
                        {"text": "Un cheveu qui n'a jamais été traité chimiquement.", "isCorrect": False, "rationale": "Les cheveux naturels sont généralement moins poreux."},
                        {"text": "Un cheveu qui absorbe l'eau rapidement, mais la retient mal, et sèche très vite.", "isCorrect": True, "rationale": "Un cheveu **hydrophile** (qui aime l'eau) absorbe l'eau facilement (cuticule ouverte), mais la perd tout aussi vite. Il nécessite des soins riches en lipides pour retenir l'humidité."},
                        {"text": "Un cheveu au pH neutre (7).", "isCorrect": False, "rationale": "Le pH n'est pas directement lié à l'hydrophilie."}
                    ],
                    "correction": "L'**hydrophilie** est un signe de porosité élevée (cheveu abîmé, coloré, décoloré). Ces cheveux ont besoin de produits scellants (après-shampoings acides, sérums) pour lisser les écailles et retenir l'hydratation."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le pourcentage de T.V.A. (Taxe sur la Valeur Ajoutée) généralement applicable aux prestations de coiffure en France (taux normal) ?",
                    "answerOptions": [
                        {"text": "5,5 %", "isCorrect": False, "rationale": "Ceci est le taux réduit pour certains produits alimentaires de première nécessité."},
                        {"text": "10 %", "isCorrect": False, "rationale": "Ceci est le taux intermédiaire."},
                        {"text": "20 %", "isCorrect": True, "rationale": "Le taux de T.V.A. **normal** (le plus courant) applicable aux prestations de services (comme la coupe, le brushing, la couleur) et à la revente de produits est de **20 %**."},
                        {"text": "Aucune TVA (taux 0 %)", "isCorrect": False, "rationale": "La TVA est toujours appliquée sauf cas très spécifiques (micro-entreprises sous le seuil de franchise)."}
                    ],
                    "correction": "Le coiffeur doit appliquer le taux normal de **20 %** sur la majorité des services et des produits de revente. C'est la base de la gestion des encaissements (prix TTC)."
                },
                {
                    "questionNumber": 89,
                    "question": "Lors du diagnostic, quel est l'impact d'une faible densité de cheveux sur le choix de la coupe ?",
                    "answerOptions": [
                        {"text": "La coupe sera longue et très effilée.", "isCorrect": False, "rationale": "L'effilage enlève de la masse."},
                        {"text": "Il faudra privilégier les coupes en dégradé fort pour apporter du mouvement.", "isCorrect": False, "rationale": "Le dégradé retire de la masse aux pointes."},
                        {"text": "Il est préférable de choisir une coupe pleine pour conserver de la masse et créer une illusion de volume.", "isCorrect": True, "rationale": "Une faible **densité** nécessite de conserver le maximum de matière sur les longueurs, d'où la préférence pour les **coupes pleines** (élévation $0^{\\circ}$) pour un effet de densité visuelle."},
                        {"text": "La couleur ne pourra pas prendre uniformément.", "isCorrect": False, "rationale": "La densité n'influence pas la prise de couleur."}
                    ],
                    "correction": "La **densité** est le nombre de cheveux par centimètre carré. Une faible densité se traite souvent par des coupes de masse (carrés pleins, B.O.B.) et des coiffages volumateurs."
                },
                {
                    "questionNumber": 90,
                    "question": "Que signifie la méthode commerciale dite de 'montée en gamme' (ou Upselling) ?",
                    "answerOptions": [
                        {"text": "Vendre uniquement des produits pour l'hygiène.", "isCorrect": False, "rationale": "Ceci est un focus sur une catégorie de produits."},
                        {"text": "Proposer au client une prestation plus complète ou un produit de qualité supérieure à celui initialement demandé.", "isCorrect": True, "rationale": "La **montée en gamme** consiste à suggérer une prestation ou un produit à plus forte valeur (ex: proposer un soin profond en plus du shampoing) pour augmenter le panier moyen."},
                        {"text": "Vendre des produits à prix cassés pour écouler le stock.", "isCorrect": False, "rationale": "Ceci est du déstockage (ou Downselling)."},
                        {"text": "Forcer le client à acheter ce qu'il ne veut pas.", "isCorrect": False, "rationale": "Ceci est de la vente forcée (mauvaise pratique)."}
                    ],
                    "correction": "L'**Upselling** est une technique de vente qui doit rester dans le conseil. Elle permet d'améliorer la qualité du service rendu au client tout en augmentant le chiffre d'affaires du salon."
                },
                {
                    "questionNumber": 91,
                    "question": "Lors de l'examen visuel, comment se manifeste généralement un cuir chevelu en 'état pityriasique simple' ?",
                    "answerOptions": [
                        {"text": "Par des plaques rouges et suintantes.", "isCorrect": False, "rationale": "Ceci est une dermatite sévère."},
                        {"text": "Par des pellicules grasses et jaunâtres qui collent au cuir chevelu.", "isCorrect": False, "rationale": "Ceci est l'état pityriasique gras."},
                        {"text": "Par de fines pellicules blanches et sèches qui tombent facilement sur les épaules.", "isCorrect": True, "rationale": "L'état **pityriasique simple** correspond aux pellicules sèches. Il est souvent dû à une simple desquamation du cuir chevelu sec ou irrité."},
                        {"text": "Par une perte de cheveux en forme de rond.", "isCorrect": False, "rationale": "Ceci est l'alopécie areata."}
                    ],
                    "correction": "Les **pellicules sèches** (pityriasis simple) sont le résultat d'un déséquilibre. Elles nécessitent un traitement antifongique léger et une hydratation du cuir chevelu."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est l'objectif d'une technique de 'pré-pigmentation' avant une coloration ?",
                    "answerOptions": [
                        {"text": "Éclaircir le cheveu d'un ton supplémentaire.", "isCorrect": False, "rationale": "La pré-pigmentation ne sert pas à éclaircir."},
                        {"text": "Neutraliser un reflet trop chaud (orange ou jaune).", "isCorrect": False, "rationale": "Ceci est la neutralisation classique."},
                        {"text": "Réintroduire des pigments chauds sur un cheveu très décoloré avant de foncer.", "isCorrect": True, "rationale": "La **pré-pigmentation** est essentielle pour 'remplir' un cheveu poreux qui a perdu ses pigments chauds naturels (fond de clarification), avant d'appliquer une couleur foncée. Elle garantit que la couleur ne 'vire' pas au vert ou au gris."},
                        {"text": "Rendre la coupe plus nette et précise.", "isCorrect": False, "rationale": "Ceci est une technique de coloration."}
                    ],
                    "correction": "La **pré-pigmentation** est cruciale lorsqu'on passe d'un blond très clair (niveau 9 ou 10) à un châtain (niveau 4 ou 5) pour éviter une couleur terne ou des reflets indésirables."
                },
                {
                    "questionNumber": 93,
                    "question": "En cas de litige avec un client (résultat non conforme), quelle est la meilleure attitude professionnelle à adopter en premier lieu ?",
                    "answerOptions": [
                        {"text": "Argumenter que l'erreur est celle du client.", "isCorrect": False, "rationale": "Ceci est non commercial et aggrave le conflit."},
                        {"text": "Refuser tout dialogue et le faire partir.", "isCorrect": False, "rationale": "Ceci est illégal."},
                        {"text": "Écouter attentivement sa plainte, puis proposer une solution (retouche, soin offert, etc.).", "isCorrect": True, "rationale": "La première étape est toujours l'**écoute active et l'empathie**. Reconnaître la frustration du client et proposer une solution de réparation est la clé de la gestion de litige."},
                        {"text": "Lui demander de revenir la semaine suivante.", "isCorrect": False, "rationale": "Il faut agir immédiatement si possible."}
                    ],
                    "correction": "Le service après-vente est primordial. Une bonne gestion des **litiges** (écoute et proposition de solution) peut transformer un client mécontent en un client fidèle."
                },
                {
                    "questionNumber": 94,
                    "question": "Que doit-on impérativement prendre en compte lors du choix de la coiffure finale pour une cliente ?",
                    "answerOptions": [
                        {"text": "Uniquement les tendances de l'année en cours.", "isCorrect": False, "rationale": "Les tendances ne sont qu'une partie du choix."},
                        {"text": "Le type de cheveu, la morphologie du visage et le style de vie de la cliente.", "isCorrect": True, "rationale": "Le choix de la coiffure doit être **personnalisé** et s'appuyer sur le **diagnostic** (type de cheveu), la **morphologie** (forme du visage) et le **style de vie** (le temps que la cliente peut consacrer à son coiffage)."},
                        {"text": "Le prix maximal que le client est prêt à dépenser.", "isCorrect": False, "rationale": "Le prix influence, mais n'est pas un critère technique de coiffure."},
                        {"text": "La capacité du coiffeur à réaliser la coupe.", "isCorrect": False, "rationale": "Le coiffeur est censé maîtriser les techniques de base."}
                    ],
                    "correction": "Le coiffeur doit être un conseiller. L'adéquation entre la **coiffure, le visage et le style de vie** garantit que le client sera satisfait et pourra se coiffer lui-même à la maison."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est le terme générique pour désigner les ventes de shampoings, soins et produits de coiffage que le client emporte chez lui ?",
                    "answerOptions": [
                        {"text": "Les produits consommables", "isCorrect": False, "rationale": "Les consommables sont les produits utilisés en salon."},
                        {"text": "Les ventes de services", "isCorrect": False, "rationale": "Les services sont les prestations (coupe, couleur)."},
                        {"text": "La revente", "isCorrect": True, "rationale": "La **revente** (ou vente additionnelle) désigne la vente des produits que le client utilisera chez lui. Elle est essentielle pour le chiffre d'affaires et la fidélisation."},
                        {"text": "Les marges brutes", "isCorrect": False, "rationale": "Ceci est un terme comptable."}
                    ],
                    "correction": "La **revente** est une source de profit importante et un gage de professionnalisme, car elle permet au client d'entretenir la qualité de sa prestation (couleur, soin) à la maison."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment le coiffeur évalue-t-il la 'résistance' ou l'élasticité d'un cheveu ?",
                    "answerOptions": [
                        {"text": "En regardant la brillance du cheveu.", "isCorrect": False, "rationale": "La brillance est liée à la cuticule (état, pH)."},
                        {"text": "En tirant doucement sur une mèche mouillée et en observant sa capacité à revenir à sa longueur initiale.", "isCorrect": True, "rationale": "L'**élasticité** est testée sur cheveux mouillés. Un cheveu en bonne santé s'étire sans casser et reprend sa forme. Un cheveu qui s'étire beaucoup et ne revient pas est très endommagé (élastique)."},
                        {"text": "En le brossant très fort.", "isCorrect": False, "rationale": "Ceci est un test de résistance à la casse, mais non d'élasticité."},
                        {"text": "En mesurant son épaisseur à la règle.", "isCorrect": False, "rationale": "Ceci est la nature (fin/épais)."}
                    ],
                    "correction": "Le **test d'élasticité** est crucial. Un cheveu trop élastique doit être traité avec des soins protéinés pour le renforcer avant d'envisager une nouvelle technique chimique."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel terme marketing désigne le processus de fidélisation du client ?",
                    "answerOptions": [
                        {"text": "La prospection", "isCorrect": False, "rationale": "La prospection est l'acquisition de nouveaux clients."},
                        {"text": "La rétention client (ou fidélisation)", "isCorrect": True, "rationale": "La **rétention client** est l'ensemble des actions visant à maintenir la clientèle existante (cartes de fidélité, offres personnalisées, qualité de service)."},
                        {"text": "L'amortissement", "isCorrect": False, "rationale": "L'amortissement est comptable."},
                        {"text": "L'inventaire", "isCorrect": False, "rationale": "L'inventaire est la gestion des stocks."}
                    ],
                    "correction": "Il est plus coûteux d'acquérir un nouveau client que de fidéliser un client existant. La qualité du service et du conseil est le meilleur outil de **rétention client**."
                },
                {
                    "questionNumber": 98,
                    "question": "En coloration, quelle est la principale anomalie que l'on cherche à identifier lors du diagnostic en racines (repousse) ?",
                    "answerOptions": [
                        {"text": "La longueur des pointes.", "isCorrect": False, "rationale": "La longueur est visible sur toute la tête."},
                        {"text": "La présence d'un fond d'éclaircissement rouge.", "isCorrect": False, "rationale": "Ceci apparaît après la décoloration."},
                        {"text": "Le pourcentage de cheveux blancs et la hauteur de ton naturelle.", "isCorrect": True, "rationale": "La **repousse** indique la base de travail : le pourcentage de **cheveux blancs** (à couvrir) et la **hauteur de ton naturelle** (pour choisir l'oxydant et la formule colorante)."},
                        {"text": "Le diamètre du cheveu (fin ou épais).", "isCorrect": False, "rationale": "Le diamètre est le même partout."}
                    ],
                    "correction": "Le diagnostic de la **repousse** est la base de toute retouche couleur. Il dicte la formule (base, reflet, oxydant) pour obtenir un résultat uniforme entre la racine et les longueurs."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le risque de réaliser une permanente sur un cheveu fortement coloré avec du henné naturel pur ?",
                    "answerOptions": [
                        {"text": "Un éclaircissement non désiré de la couleur.", "isCorrect": False, "rationale": "Le henné est stable."},
                        {"text": "La coloration peut virer au vert.", "isCorrect": False, "rationale": "Ceci arrive avec la décoloration, pas la permanente."},
                        {"text": "Une incompatibilité chimique entraînant une forte chaleur, la casse ou la brûlure du cheveu.", "isCorrect": True, "rationale": "Le **henné naturel pur** (notamment celui contenant des sels métalliques non compatibles) peut interagir violemment avec les produits de permanente ou de défrisage, provoquant une **réaction chimique forte** (chaleur) et la casse des cheveux."},
                        {"text": "L'absence totale de boucles.", "isCorrect": False, "rationale": "Ceci est le risque si la permanente est mal faite."}
                    ],
                    "correction": "Il est impératif de diagnostiquer la présence de henné métallique ou d'attendre une très longue repousse avant d'appliquer un produit de permanente ou de lissage chimique. Le **risque de casse** est majeur."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est l'objectif du 'cross-selling' (vente croisée) en coiffure ?",
                    "answerOptions": [
                        {"text": "Vendre un produit de soin pour le corps.", "isCorrect": False, "rationale": "Ceci est une vente hors-domaine."},
                        {"text": "Proposer un produit complémentaire à la prestation que le client vient d'acheter.", "isCorrect": True, "rationale": "Le **cross-selling** (vente croisée) consiste à vendre un produit qui va avec la prestation achetée (ex: si coupe + brushing, proposer un spray thermo-protecteur pour le coiffage)."},
                        {"text": "Réserver le prochain rendez-vous avant que le client parte.", "isCorrect": False, "rationale": "Ceci est la prise de rendez-vous."},
                        {"text": "Vendre un produit pour les cheveux d'enfant.", "isCorrect": False, "rationale": "Ceci est une catégorie de produit."}
                    ],
                    "correction": "Le **cross-selling** est une technique qui ajoute de la valeur pour le client et le salon. Le produit est directement lié au besoin créé par le service (ex: shampoing spécifique après une couleur)."
                }
            ]
        }
    }
}