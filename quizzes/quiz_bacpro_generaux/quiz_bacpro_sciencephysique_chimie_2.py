quiz_data = {
    "title": "Quiz BAC PRO Sciences Physiques - Chimie : Chimie, Thermique, Acoustique & Optique (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : Solutions aqueuses, pH et dilutions (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : Solutions aqueuses, pH et dilutions",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est l'unité du Système International de la quantité de matière ?",
                    "answerOptions": [
                        {"text": "Mole", "isCorrect": True},
                        {"text": "Gramme", "isCorrect": False},
                        {"text": "Litre", "isCorrect": False},
                        {"text": "Mol/L", "isCorrect": False}
                    ],
                    "correction": "La quantité de matière n s'exprime en moles (symbole mol). Une mole correspond à environ 6,02 × 10²³ entités élémentaires (nombre d'Avogadro)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle formule relie la quantité de matière n, la masse m et la masse molaire M ?",
                    "answerOptions": [
                        {"text": "n = m / M", "isCorrect": True},
                        {"text": "n = m × M", "isCorrect": False},
                        {"text": "n = M / m", "isCorrect": False},
                        {"text": "M = n × m", "isCorrect": False}
                    ],
                    "correction": "La quantité de matière n (en mol) est égale au quotient de la masse m de l'échantillon (en g) par sa masse molaire M (en g/mol) : n = m / M."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle propriété fondamentale se conserve lors de la dilution d'une solution aqueuse ?",
                    "answerOptions": [
                        {"text": "La quantité de matière de soluté reste rigoureusement identique avant et après ajout d'eau", "isCorrect": True},
                        {"text": "La concentration molaire de la solution fille reste strictement égale à celle de la solution mère initiale", "isCorrect": False},
                        {"text": "Le volume total de la solution finale demeure invariable malgré l'ajout de solvant dans la fiole jaugée", "isCorrect": False},
                        {"text": "Le pH de la solution aqueuse reste parfaitement constant quelle que soit la quantité d'eau distillée ajoutée", "isCorrect": False}
                    ],
                    "correction": "Lors d'une dilution, on ajoute uniquement du solvant (eau distillée) sans ajouter ni retirer de soluté. La quantité de matière de soluté se conserve donc : n_mère = n_fille, ce qui donne la relation fondamentale C1 × V1 = C2 × V2."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle relation permet de calculer la concentration molaire C d'une solution ?",
                    "answerOptions": [
                        {"text": "C = n / V", "isCorrect": True},
                        {"text": "C = n × V", "isCorrect": False},
                        {"text": "C = m / V", "isCorrect": False},
                        {"text": "C = V / n", "isCorrect": False}
                    ],
                    "correction": "La concentration molaire C (en mol/L) est le rapport de la quantité de matière de soluté n (en mol) sur le volume total de la solution V (en L) : C = n / V. Le rapport m / V correspond à la concentration massique."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel ion est majoritairement responsable de l'acidité d'une solution aqueuse ?",
                    "answerOptions": [
                        {"text": "Ion hydronium", "isCorrect": True},
                        {"text": "Ion hydroxyde", "isCorrect": False},
                        {"text": "Ion chlorure", "isCorrect": False},
                        {"text": "Ion sodium", "isCorrect": False}
                    ],
                    "correction": "L'acidité d'une solution aqueuse est due à la présence d'ions hydronium H3O+ (souvent notés H+). Plus leur concentration est élevée, plus la solution est acide et plus son pH est bas."
                },
                {
                    "questionNumber": 6,
                    "question": "Entre quelles valeurs s'étend l'échelle du pH d'une solution basique à 25 °C ?",
                    "answerOptions": [
                        {"text": "Strictement supérieur à 7 et jusqu'à 14", "isCorrect": True},
                        {"text": "Compris entre 0 et strictement inférieur à 7", "isCorrect": False},
                        {"text": "Strictement égal à 7 à température ambiante", "isCorrect": False},
                        {"text": "Compris entre 1 et 10 selon la dilution", "isCorrect": False}
                    ],
                    "correction": "À 25 °C, une solution est acide si pH < 7, neutre si pH = 7, et basique (alcaline) si 7 < pH ≤ 14. Une solution basique contient majoritairement des ions hydroxyde HO−."
                },
                {
                    "questionNumber": 7,
                    "question": "Comment évolue le pH d'une solution acide lorsque l'on procède à sa dilution avec de l'eau distillée ?",
                    "answerOptions": [
                        {"text": "Son pH augmente progressivement en se rapprochant de 7 sans jamais dépasser cette valeur", "isCorrect": True},
                        {"text": "Son pH diminue fortement vers 0 car l'ajout d'eau augmente la concentration en ions hydronium libres", "isCorrect": False},
                        {"text": "Son pH augmente rapidement jusqu'à dépasser 7 et transformer la solution acide en solution basique", "isCorrect": False},
                        {"text": "Son pH reste strictement figé à sa valeur initiale car l'eau distillée est un solvant parfaitement neutre", "isCorrect": False}
                    ],
                    "correction": "Diluer un acide diminue la concentration en ions H3O+ : la solution devient moins acide, donc son pH augmente. Cependant, comme on ajoute de l'eau neutre (pH = 7), le pH tend vers 7 sans jamais pouvoir devenir basique (> 7)."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la masse molaire moléculaire de l'eau H2O avec M_H = 1 g/mol et M_O = 16 g/mol ?",
                    "answerOptions": [
                        {"text": "18 grammes par mole", "isCorrect": True},
                        {"text": "17 grammes par mole", "isCorrect": False},
                        {"text": "33 grammes par mole", "isCorrect": False},
                        {"text": "10 grammes par mole", "isCorrect": False}
                    ],
                    "correction": "La molécule d'eau contient 2 atomes d'hydrogène et 1 atome d'oxygène. Sa masse molaire vaut donc : M(H2O) = 2 × 1 + 16 = 18 g/mol."
                },
                {
                    "questionNumber": 9,
                    "question": "On dissout 20 g de soluté dans 0,5 L de solution. Quelle est la concentration massique Cm ?",
                    "answerOptions": [
                        {"text": "40 grammes par litre", "isCorrect": True},
                        {"text": "10 grammes par litre", "isCorrect": False},
                        {"text": "20,5 grammes par litre", "isCorrect": False},
                        {"text": "0,025 gramme par litre", "isCorrect": False}
                    ],
                    "correction": "La concentration massique s'exprime par Cm = m / V. Avec m = 20 g et V = 0,5 L, on obtient : Cm = 20 / 0,5 = 40 g/L."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle verrerie de précision utilise-t-on pour ajuster le volume final lors d'une dilution au laboratoire ?",
                    "answerOptions": [
                        {"text": "Une fiole jaugée permettant d'ajuster précisément le ménisque au niveau du trait de jauge", "isCorrect": True},
                        {"text": "Un bécher gradué permettant de mesurer rapidement le volume final à plus ou moins un dixième de millilitre", "isCorrect": False},
                        {"text": "Un erlenmeyer à col étroit garantissant une lecture directe du volume exact sans erreur de parallaxe", "isCorrect": False},
                        {"text": "Une éprouvette graduée en plastique calibrée pour les préparations analytiques de très haute précision", "isCorrect": False}
                    ],
                    "correction": "Pour préparer une solution de concentration précise par dissolution ou dilution, on utilise impérativement une fiole jaugée (dont le trait de jauge est calibré avec précision) et une pipette jaugée pour le prélèvement. Le bécher et l'erlenmeyer ne sont pas des instruments de mesure précis."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel appareil mesure le pH d'une solution avec une précision au dixième d'unité ?",
                    "answerOptions": [
                        {"text": "pH-mètre", "isCorrect": True},
                        {"text": "Papier pH", "isCorrect": False},
                        {"text": "Conductimètre", "isCorrect": False},
                        {"text": "Densimètre", "isCorrect": False}
                    ],
                    "correction": "Le pH-mètre (muni d'une sonde en verre préalablement étalonnée avec des solutions tampons) permet une mesure précise à 0,1 ou 0,01 unité pH près. Le papier pH ne donne qu'une valeur approchée à l'unité."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment relie-t-on la concentration massique Cm et la concentration molaire C ?",
                    "answerOptions": [
                        {"text": "Cm = C × M", "isCorrect": True},
                        {"text": "Cm = C / M", "isCorrect": False},
                        {"text": "C = Cm × M", "isCorrect": False},
                        {"text": "Cm = C + M", "isCorrect": False}
                    ],
                    "correction": "Puisque Cm = m / V et m = n × M, on a Cm = (n × M) / V = C × M. La concentration massique (en g/L) est donc égale au produit de la concentration molaire (en mol/L) par la masse molaire (en g/mol)."
                },
                {
                    "questionNumber": 13,
                    "question": "On dilue 10 fois une solution mère de concentration 0,5 mol/L. Quelle est la nouvelle concentration ?",
                    "answerOptions": [
                        {"text": "0,05 mole par litre", "isCorrect": True},
                        {"text": "5 moles par litre", "isCorrect": False},
                        {"text": "0,5 mole par litre", "isCorrect": False},
                        {"text": "0,005 mole par litre", "isCorrect": False}
                    ],
                    "correction": "Le facteur de dilution F vaut C_mère / C_fille = 10. La concentration de la solution fille est donc divisée par 10 : C_fille = 0,5 / 10 = 0,05 mol/L."
                },
                {
                    "questionNumber": 14,
                    "question": "Que se passe-t-il au point d'équivalence lors d'un titrage acido-basique ?",
                    "answerOptions": [
                        {"text": "Les réactifs titré et titrant ont été introduits exactement dans les proportions stœchiométriques", "isCorrect": True},
                        {"text": "Le pH de la solution dans le bécher atteint systématiquement la valeur exacte de 7 quelle que soit la réaction", "isCorrect": False},
                        {"text": "La réaction chimique s'arrête définitivement car le solvant aqueux est totalement consommé par l'acide", "isCorrect": False},
                        {"text": "La concentration de l'espèce titrante devient strictement égale à zéro dans la burette graduée", "isCorrect": False}
                    ],
                    "correction": "À l'équivalence d'un titrage, le réactif titré et le réactif titrant sont intégralement consommés dans les proportions de l'équation chimique : il y a changement de réactif limitant, repéré par un saut de pH ou le virage d'un indicateur coloré."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel volume de solution mère à 2 mol/L faut-il prélever pour préparer 100 mL de solution à 0,2 mol/L ?",
                    "answerOptions": [
                        {"text": "10 millilitres", "isCorrect": True},
                        {"text": "20 millilitres", "isCorrect": False},
                        {"text": "50 millilitres", "isCorrect": False},
                        {"text": "1 millilitre", "isCorrect": False}
                    ],
                    "correction": "D'après la relation de dilution C1 × V1 = C2 × V2, on isole V1 : V1 = (C2 × V2) / C1 = (0,2 × 100) / 2 = 20 / 2 = 10 mL."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel pictogramme de sécurité signale un produit acide ou basique concentré ?",
                    "answerOptions": [
                        {"text": "Corrosif", "isCorrect": True},
                        {"text": "Comburant", "isCorrect": False},
                        {"text": "Inflammable", "isCorrect": False},
                        {"text": "Explosif", "isCorrect": False}
                    ],
                    "correction": "Les acides et bases concentrés (acide chlorhydrique, soude caustique) portent le pictogramme SGH05 « Corrosif » (deux tubes à essai versant un liquide sur une main et une surface métallique), indiquant un risque de brûlure chimique grave."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle précaution impérative faut-il respecter lors de la dilution d'un acide concentré ?",
                    "answerOptions": [
                        {"text": "Verser toujours l'acide dans l'eau lentement", "isCorrect": True},
                        {"text": "Verser toujours l'eau dans l'acide concentré", "isCorrect": False},
                        {"text": "Chauffer préalablement l'acide avant d'ajouter l'eau", "isCorrect": False},
                        {"text": "Mélanger à volumes égaux dans un récipient fermé", "isCorrect": False}
                    ],
                    "correction": "La dilution d'un acide fort concentré est très exothermique (dégagement de chaleur). Verser l'eau dans l'acide provoquerait une ébullition brutale et des projections d'acide pur. On verse donc toujours l'acide dans l'eau (moyen mnémotechnique : « Acide dans l'eau, bravo »)."
                },
                {
                    "questionNumber": 18,
                    "question": "Comment repère-t-on graphiquement le volume équivalent sur une courbe de titrage pH-métrique ?",
                    "answerOptions": [
                        {"text": "Par la méthode des tangentes parallèles au niveau du saut brutal de pH", "isCorrect": True},
                        {"text": "En relevant simplement l'abscisse du point où la courbe coupe l'axe horizontal de pH égal à zéro", "isCorrect": False},
                        {"text": "En calculant la moyenne arithmétique entre le volume initial et le volume maximal de la burette", "isCorrect": False},
                        {"text": "En mesurant la pente de la partie parfaitement horizontale située tout au début du dosage", "isCorrect": False}
                    ],
                    "correction": "Sur la courbe pH = f(V), l'équivalence correspond au point d'inflexion situé au milieu du saut de pH. On le détermine précisément à l'aide de la méthode des tangentes parallèles (ou par le maximum de la courbe dérivée dpH/dV)."
                },
                {
                    "questionNumber": 19,
                    "question": "Que signifie une baisse d'une unité de pH pour la concentration en ions hydronium ?",
                    "answerOptions": [
                        {"text": "Elle est multipliée par dix", "isCorrect": True},
                        {"text": "Elle est divisée par dix", "isCorrect": False},
                        {"text": "Elle augmente d'une mole par litre", "isCorrect": False},
                        {"text": "Elle est multipliée par deux", "isCorrect": False}
                    ],
                    "correction": "Le pH est défini par une échelle logarithmique décimale : pH = −log([H3O+]). Par conséquent, lorsque le pH diminue de 1 unité, la concentration en ions hydronium [H3O+] est multipliée par 10."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le rôle d'un indicateur coloré acido-basique ajouté en quelques gouttes lors d'un titrage ?",
                    "answerOptions": [
                        {"text": "Changer nettement de teinte au passage de l'équivalence pour repérer visuellement la fin du dosage", "isCorrect": True},
                        {"text": "Accélérer la vitesse de la réaction chimique entre l'acide et la base en jouant le rôle de catalyseur", "isCorrect": False},
                        {"text": "Neutraliser automatiquement l'excès de réactif titrant afin d'empêcher tout dépassement du volume équivalent", "isCorrect": False},
                        {"text": "Maintenir le pH de la solution parfaitement stable autour de 7 pendant toute la durée de la manipulation", "isCorrect": False}
                    ],
                    "correction": "Un indicateur coloré (comme le BBT ou la phénolphtaléine) possède deux formes de couleurs différentes selon le pH. On le choisit pour que sa zone de virage encadre le pH à l'équivalence, permettant de repérer visuellement le volume équivalent à la goutte près."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : Oxydoréduction, corrosion et combustions (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : Oxydoréduction, corrosion et combustions",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel transfert de particules caractérise une réaction d'oxydoréduction ?",
                    "answerOptions": [
                        {"text": "Électrons", "isCorrect": True},
                        {"text": "Protons", "isCorrect": False},
                        {"text": "Neutrons", "isCorrect": False},
                        {"text": "Photons", "isCorrect": False}
                    ],
                    "correction": "Une réaction d'oxydoréduction correspond toujours à un transfert d'un ou plusieurs électrons (e−) entre un réducteur (qui les cède) et un oxydant (qui les capte)."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment définit-on chimiquement un oxydant dans un couple rédox ?",
                    "answerOptions": [
                        {"text": "Espèce capable de capter des électrons", "isCorrect": True},
                        {"text": "Espèce capable de céder des électrons", "isCorrect": False},
                        {"text": "Espèce capable de libérer des protons", "isCorrect": False},
                        {"text": "Espèce chimiquement inerte en solution", "isCorrect": False}
                    ],
                    "correction": "Un oxydant est une espèce chimique susceptible de gagner (capter) un ou plusieurs électrons pour se transformer en son réducteur conjugué : Ox + n e− = Red."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est la différence fondamentale entre une oxydation et une réduction ?",
                    "answerOptions": [
                        {"text": "L'oxydation correspond à une perte d'électrons alors que la réduction est un gain d'électrons", "isCorrect": True},
                        {"text": "L'oxydation correspond à un gain d'électrons par un atome métallique alors que la réduction libère des protons dans l'eau", "isCorrect": False},
                        {"text": "L'oxydation se produit exclusivement en présence de dioxygène pur alors que la réduction nécessite une flamme vive", "isCorrect": False},
                        {"text": "L'oxydation augmente le nombre d'électrons d'un ion positif alors que la réduction le transforme en atome neutre", "isCorrect": False}
                    ],
                    "correction": "Une oxydation est une perte d'électrons (le réducteur est oxydé) et une réduction est un gain d'électrons (l'oxydant est réduit). Les deux phénomènes sont toujours simultanés lors d'une réaction rédox."
                },
                {
                    "questionNumber": 24,
                    "question": "Dans la demi-équation Fe = Fe2+ + 2 e-, quelle transformation subit le fer ?",
                    "answerOptions": [
                        {"text": "Une oxydation du métal fer", "isCorrect": True},
                        {"text": "Une réduction du métal fer", "isCorrect": False},
                        {"text": "Une neutralisation acido-basique", "isCorrect": False},
                        {"text": "Une précipitation ionique", "isCorrect": False}
                    ],
                    "correction": "L'atome de fer (Fe) perd 2 électrons pour devenir un ion fer II (Fe2+). Une perte d'électrons est par définition une oxydation."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel gaz présent dans l'air est le comburant habituel des combustions ?",
                    "answerOptions": [
                        {"text": "Dioxygène", "isCorrect": True},
                        {"text": "Diazote", "isCorrect": False},
                        {"text": "Dihydrogène", "isCorrect": False},
                        {"text": "Argon", "isCorrect": False}
                    ],
                    "correction": "L'air est composé d'environ 21 % de dioxygène (O2) et 78 % de diazote (N2). Seul le dioxygène joue le rôle de comburant indispensable pour entretenir une combustion."
                },
                {
                    "questionNumber": 26,
                    "question": "Quels sont les deux produits formés lors de la combustion complète d'un alcane ?",
                    "answerOptions": [
                        {"text": "Dioxyde de carbone et eau", "isCorrect": True},
                        {"text": "Monoxyde de carbone et dihydrogène", "isCorrect": False},
                        {"text": "Carbone solide et dioxygène", "isCorrect": False},
                        {"text": "Diazote et vapeur d'eau", "isCorrect": False}
                    ],
                    "correction": "Lorsque le dioxygène est en excès, la combustion d'un hydrocarbure (alcane comme le méthane ou le butane) est complète et ne produit que du dioxyde de carbone (CO2) et de l'eau (H2O)."
                },
                {
                    "questionNumber": 27,
                    "question": "Pourquoi une combustion incomplète d'un hydrocarbure est-elle particulièrement dangereuse ?",
                    "answerOptions": [
                        {"text": "Elle produit du monoxyde de carbone, un gaz incolore, inodore et mortel", "isCorrect": True},
                        {"text": "Elle consomme l'intégralité du diazote atmosphérique ce qui provoque une chute brutale de la pression ambiante", "isCorrect": False},
                        {"text": "Elle libère de l'acide sulfurique gazeux qui rend instantanément l'air bleu et irritant pour les yeux", "isCorrect": False},
                        {"text": "Elle abaisse la température de la pièce en absorbant la chaleur au lieu de dégager de l'énergie thermique", "isCorrect": False}
                    ],
                    "correction": "Par manque de dioxygène, la combustion devient incomplète (flamme jaune) : elle forme du carbone (suie) et du monoxyde de carbone (CO). Ce gaz toxique se fixe sur l'hémoglobine à la place du dioxygène, provoquant une asphyxie."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel réactif permet de mettre en évidence le dioxyde de carbone formé lors d'une combustion ?",
                    "answerOptions": [
                        {"text": "L'eau de chaux qui se trouble", "isCorrect": True},
                        {"text": "Le sulfate de cuivre anhydre qui bleuit", "isCorrect": False},
                        {"text": "Le nitrate d'argent qui noircit", "isCorrect": False},
                        {"text": "La soude qui forme un précipité rouille", "isCorrect": False}
                    ],
                    "correction": "Le dioxyde de carbone (CO2) réagit avec l'eau de chaux (solution d'hydroxyde de calcium) en formant un précipité blanc de carbonate de calcium qui trouble la solution. Le sulfate de cuivre anhydre détecte l'eau."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la nature chimique de la rouille qui se forme sur le fer ?",
                    "answerOptions": [
                        {"text": "Un oxyde de fer hydraté et poreux", "isCorrect": True},
                        {"text": "Un alliage compact de fer et de carbone", "isCorrect": False},
                        {"text": "Un sel de chlorure de fer totalement imperméable", "isCorrect": False},
                        {"text": "Un dépôt de cuivre issu de l'humidité ambiante", "isCorrect": False}
                    ],
                    "correction": "La rouille est constituée principalement d'oxydes et d'hydroxydes de fer III hydratés. Contrairement à l'alumine, elle est poreuse et friable : elle laisse passer l'air et l'eau, ce qui permet à la corrosion de se poursuivre en profondeur."
                },
                {
                    "questionNumber": 30,
                    "question": "Comment fonctionne la protection d'une structure en acier par anode sacrificielle en zinc ?",
                    "answerOptions": [
                        {"text": "Le zinc plus réducteur que le fer s'oxyde prioritairement à la place de l'acier", "isCorrect": True},
                        {"text": "Le zinc forme une barrière thermique imperméable qui empêche totalement l'eau salée d'entrer en contact avec la structure", "isCorrect": False},
                        {"text": "Le zinc capte les électrons de l'acier pour transformer la rouille déjà présente en fer métallique pur", "isCorrect": False},
                        {"text": "Le zinc neutralise l'acidité de l'eau environnante en libérant du dioxygène gazeux autour de la pièce", "isCorrect": False}
                    ],
                    "correction": "Dans la classification électrochimique, le zinc est plus réducteur que le fer. Relié électriquement à l'acier en milieu humide, il constitue l'anode d'une pile : il se corrode (s'oxyde) en cédant ses électrons, ce qui protège l'acier (cathode)."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel métal se recouvre naturellement d'une couche d'oxyde protectrice appelée alumine ?",
                    "answerOptions": [
                        {"text": "Aluminium", "isCorrect": True},
                        {"text": "Fer", "isCorrect": False},
                        {"text": "Cuivre", "isCorrect": False},
                        {"text": "Plomb", "isCorrect": False}
                    ],
                    "correction": "Au contact de l'air, l'aluminium s'oxyde instantanément en surface pour former une très fine couche d'oxyde d'aluminium (alumine, Al2O3), étanche et adhérente, qui protège le métal sous-jacent contre la corrosion."
                },
                {
                    "questionNumber": 32,
                    "question": "Dans la classification électrochimique, quel métal est le plus réducteur entre le zinc et le cuivre ?",
                    "answerOptions": [
                        {"text": "Le zinc s'oxyde plus facilement que le cuivre", "isCorrect": True},
                        {"text": "Le cuivre s'oxyde plus facilement que le zinc", "isCorrect": False},
                        {"text": "Les deux métaux ont exactement le même pouvoir réducteur", "isCorrect": False},
                        {"text": "Aucun des deux métaux ne peut céder d'électrons", "isCorrect": False}
                    ],
                    "correction": "Le potentiel standard du couple Zn2+/Zn (−0,76 V) est très inférieur à celui du couple Cu2+/Cu (+0,34 V). Le zinc est donc un bien meilleur réducteur que le cuivre (qui est un métal semi-noble)."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la couleur caractéristique d'une solution aqueuse contenant des ions cuivre II ?",
                    "answerOptions": [
                        {"text": "Couleur bleue caractéristique", "isCorrect": True},
                        {"text": "Couleur verte pâle", "isCorrect": False},
                        {"text": "Couleur rouille orangée", "isCorrect": False},
                        {"text": "Solution totalement incolore", "isCorrect": False}
                    ],
                    "correction": "En solution aqueuse, les ions cuivre II (Cu2+) donnent une couleur bleue caractéristique. Les ions fer II (Fe2+) sont vert pâle, les ions fer III (Fe3+) sont jaune-orangé (rouille), et les ions zinc (Zn2+) sont incolores."
                },
                {
                    "questionNumber": 34,
                    "question": "Qu'observe-t-on lorsqu'on plonge une lame de fer dans une solution de sulfate de cuivre ?",
                    "answerOptions": [
                        {"text": "Un dépôt rougeâtre de cuivre se forme sur le fer et la solution bleue se décolore", "isCorrect": True},
                        {"text": "Un dégagement gazeux de dihydrogène apparaît immédiatement tandis que la solution prend une coloration violette intense", "isCorrect": False},
                        {"text": "La lame de fer reste parfaitement intacte car le cuivre est beaucoup plus réducteur que le fer en solution", "isCorrect": False},
                        {"text": "Un précipité blanc de sulfate de fer se dépose au fond du bécher sans aucune modification de la lame métallique", "isCorrect": False}
                    ],
                    "correction": "Une réaction d'oxydoréduction spontanée se produit : Fe + Cu2+ → Fe2+ + Cu. Le fer s'oxyde en ions Fe2+ (la solution verdit/se décolore) et les ions Cu2+ sont réduits en cuivre métallique (dépôt rougeâtre sur la lame)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quels sont les trois éléments indispensables représentés dans le triangle du feu ?",
                    "answerOptions": [
                        {"text": "Combustible, comburant et énergie d'activation", "isCorrect": True},
                        {"text": "Combustible, dioxyde de carbone et pression", "isCorrect": False},
                        {"text": "Comburant, diazote et température ambiante", "isCorrect": False},
                        {"text": "Hydrocarbure, vapeur d'eau et étincelle", "isCorrect": False}
                    ],
                    "correction": "Pour qu'une combustion démarre et se maintienne, il faut réunir simultanément un combustible (ce qui brûle), un comburant (généralement le dioxygène) et une énergie d'activation (chaleur, étincelle, flamme). Supprimer un seul côté éteint le feu."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le rôle d'une pile électrochimique dans un circuit électrique ?",
                    "answerOptions": [
                        {"text": "Générateur", "isCorrect": True},
                        {"text": "Récepteur", "isCorrect": False},
                        {"text": "Isolant", "isCorrect": False},
                        {"text": "Catalyseur", "isCorrect": False}
                    ],
                    "correction": "Une pile électrochimique est un générateur qui convertit directement de l'énergie chimique (issue d'une réaction d'oxydoréduction spontanée) en énergie électrique."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle demi-équation traduit la réduction des ions cuivre Cu2+ en métal cuivre Cu ?",
                    "answerOptions": [
                        {"text": "Cu2+ + 2 e- = Cu", "isCorrect": True},
                        {"text": "Cu = Cu2+ + 2 e-", "isCorrect": False},
                        {"text": "Cu2+ = Cu + 2 e-", "isCorrect": False},
                        {"text": "Cu + 2 e- = Cu2+", "isCorrect": False}
                    ],
                    "correction": "Lors d'une réduction, l'oxydant (Cu2+) capte des électrons pour former le réducteur (Cu). Pour équilibrer les charges électriques (+2 à gauche, 0 à droite), on ajoute 2 électrons du côté de l'oxydant : Cu2+ + 2 e− = Cu."
                },
                {
                    "questionNumber": 38,
                    "question": "Pourquoi la corrosion du fer s'accélère-t-elle fortement en milieu salin ou humide ?",
                    "answerOptions": [
                        {"text": "Les ions dissous dans l'eau salée augmentent la conductivité et facilitent les échanges d'électrons", "isCorrect": True},
                        {"text": "Le chlorure de sodium abaisse la température de fusion du fer pur et provoque sa dissolution directe dans l'eau de mer", "isCorrect": False},
                        {"text": "Le sel transforme le dioxygène atmosphérique en acide chlorhydrique pur qui dissout instantanément la surface métallique", "isCorrect": False},
                        {"text": "L'eau salée empêche la formation de rouille en surface et force les atomes de fer à s'évaporer dans l'atmosphère", "isCorrect": False}
                    ],
                    "correction": "La corrosion humide est un phénomène électrochimique (formation de micropiles à la surface du métal). La présence d'ions (comme Na+ et Cl− dans l'eau salée) rend l'électrolyte beaucoup plus conducteur, ce qui accélère le courant de corrosion."
                },
                {
                    "questionNumber": 39,
                    "question": "Dans une équation bilan d'oxydoréduction, que faut-il obligatoirement équilibrer ?",
                    "answerOptions": [
                        {"text": "Les atomes et les charges électriques", "isCorrect": True},
                        {"text": "Uniquement le nombre de molécules d'eau", "isCorrect": False},
                        {"text": "Les masses volumiques des réactifs", "isCorrect": False},
                        {"text": "Les températures de réaction des produits", "isCorrect": False}
                    ],
                    "correction": "Toute équation chimique doit respecter la loi de conservation de la matière (même nombre d'atomes de chaque élément de part et d'autre) et la loi de conservation de la charge électrique (somme des charges identique des deux côtés)."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est le principe de la passivation qui protège certains métaux contre la corrosion en profondeur ?",
                    "answerOptions": [
                        {"text": "Une fine couche d'oxyde compacte et imperméable se forme en surface et stoppe l'oxydation", "isCorrect": True},
                        {"text": "Le métal rejette spontanément les molécules de dioxygène atmosphérique grâce à un champ magnétique permanent en surface", "isCorrect": False},
                        {"text": "Le métal absorbe l'humidité de l'air pour dissoudre progressivement la couche de rouille au fur et à mesure qu'elle apparaît", "isCorrect": False},
                        {"text": "La température de surface du métal augmente naturellement pour empêcher la condensation de la vapeur d'eau", "isCorrect": False}
                    ],
                    "correction": "La passivation (observée sur l'aluminium, le zinc ou l'acier inoxydable grâce au chrome) consiste en la formation d'une couche d'oxyde nanométrique, adhérente et non poreuse qui isole le métal sain de l'air et de l'eau."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : Chimie organique, polymères et matériaux (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : Chimie organique, polymères et matériaux",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel élément chimique constitue le squelette de toutes les molécules organiques ?",
                    "answerOptions": [
                        {"text": "Carbone", "isCorrect": True},
                        {"text": "Silicium", "isCorrect": False},
                        {"text": "Azote", "isCorrect": False},
                        {"text": "Soufre", "isCorrect": False}
                    ],
                    "correction": "La chimie organique est la chimie des composés du carbone (associé principalement à l'hydrogène, l'oxygène et l'azote). L'atome de carbone est tétravalent : il forme toujours 4 liaisons covalentes."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la formule brute générale d'un alcane acyclique à n atomes de carbone ?",
                    "answerOptions": [
                        {"text": "CnH2n+2", "isCorrect": True},
                        {"text": "CnH2n", "isCorrect": False},
                        {"text": "CnH2n-2", "isCorrect": False},
                        {"text": "CnH2n+1OH", "isCorrect": False}
                    ],
                    "correction": "Les alcanes sont des hydrocarbures saturés (uniquement des liaisons simples C−C et C−H). Leur formule brute générale est CnH2n+2 (exemples : méthane CH4, éthane C2H6, propane C3H8)."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle différence structurelle distingue un alcène d'un alcane possédant le même nombre de carbones ?",
                    "answerOptions": [
                        {"text": "L'alcène possède une double liaison carbone-carbone qui le rend chimiquement insaturé", "isCorrect": True},
                        {"text": "L'alcène possède un atome d'oxygène supplémentaire lié directement en bout de chaîne carbonée linéaire", "isCorrect": False},
                        {"text": "L'alcane contient systématiquement au moins une triple liaison covalente entre deux atomes de carbone voisins", "isCorrect": False},
                        {"text": "L'alcène ne contient que des liaisons simples mais forme obligatoirement un cycle fermé à six atomes", "isCorrect": False}
                    ],
                    "correction": "Contrairement aux alcanes (saturés, liaisons simples), les alcènes sont des hydrocarbures insaturés caractérisés par la présence d'une double liaison C=C (formule générale CnH2n). Cette double liaison permet des réactions d'addition et de polymérisation."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel groupe caractéristique identifie la famille chimique des alcools ?",
                    "answerOptions": [
                        {"text": "Le groupe hydroxyle -OH", "isCorrect": True},
                        {"text": "Le groupe carboxyle -COOH", "isCorrect": False},
                        {"text": "Le groupe carbonyle -CO-", "isCorrect": False},
                        {"text": "Le groupe ester -COO-", "isCorrect": False}
                    ],
                    "correction": "Un alcool possède un groupe caractéristique hydroxyle −OH lié à un atome de carbone tétraédrique (ne portant que des liaisons simples). Exemple : l'éthanol CH3−CH2−OH."
                },
                {
                    "questionNumber": 45,
                    "question": "Comment appelle-t-on la petite molécule de base qui se répète pour former un polymère ?",
                    "answerOptions": [
                        {"text": "Monomère", "isCorrect": True},
                        {"text": "Isomère", "isCorrect": False},
                        {"text": "Catalyseur", "isCorrect": False},
                        {"text": "Solvant", "isCorrect": False}
                    ],
                    "correction": "Un polymère est une macromolécule constituée de l'enchaînement d'un très grand nombre de motifs identiques issus d'une petite molécule réactive appelée monomère (exemple : l'éthylène donne le polyéthylène)."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la formule semi-développée de l'éthanol ?",
                    "answerOptions": [
                        {"text": "CH3-CH2-OH", "isCorrect": True},
                        {"text": "CH3-OH", "isCorrect": False},
                        {"text": "CH3-COOH", "isCorrect": False},
                        {"text": "CH3-CH2-CH3", "isCorrect": False}
                    ],
                    "correction": "Le préfixe « éth- » indique une chaîne de 2 atomes de carbone et le suffixe « -ol » indique la fonction alcool (−OH). L'éthanol a donc pour formule CH3−CH2−OH (CH3−OH est le méthanol, CH3−COOH est l'acide éthanoïque)."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment distingue-t-on un polymère thermoplastique d'un polymère thermodurcissable sous l'effet de la chaleur ?",
                    "answerOptions": [
                        {"text": "Le thermoplastique ramollit et peut être refondu de façon réversible alors que le thermodurcissable se dégrade sans fondre", "isCorrect": True},
                        {"text": "Le thermodurcissable fond très rapidement à basse température pour être moulé à l'infini alors que le thermoplastique durcit définitivement", "isCorrect": False},
                        {"text": "Le thermoplastique est constitué d'un réseau tridimensionnel rigide totalement insoluble alors que le thermodurcissable reste toujours liquide", "isCorrect": False},
                        {"text": "Les deux familles fondent exactement à la même température mais seul le thermodurcissable conduit parfaitement le courant électrique", "isCorrect": False}
                    ],
                    "correction": "Les thermoplastiques (PE, PP, PVC, PET) sont formés de chaînes linéaires peu liées entre elles : ils ramollissent à la chaleur et sont recyclables par fusion. Les thermodurcissables (résines époxy, phénoliques) forment un réseau réticulé rigide : ils ne fondent plus et carbonisent si on les chauffe trop."
                },
                {
                    "questionNumber": 48,
                    "question": "Que sont deux molécules isomères en chimie organique ?",
                    "answerOptions": [
                        {"text": "Même formule brute mais formules développées différentes", "isCorrect": True},
                        {"text": "Même formule développée mais masses molaires différentes", "isCorrect": False},
                        {"text": "Formules brutes différentes mais propriétés identiques", "isCorrect": False},
                        {"text": "Même nombre de carbones mais atomes différents", "isCorrect": False}
                    ],
                    "correction": "Des isomères possèdent exactement la même formule brute (même nombre et même nature d'atomes), mais leurs atomes sont enchaînés différemment (formules semi-développées différentes), ce qui leur confère des propriétés physiques et chimiques distinctes."
                },
                {
                    "questionNumber": 49,
                    "question": "Quels sont les deux réactifs nécessaires pour réaliser une réaction d'estérification ?",
                    "answerOptions": [
                        {"text": "Un acide carboxylique et un alcool", "isCorrect": True},
                        {"text": "Un alcane et du dioxygène", "isCorrect": False},
                        {"text": "Un alcène et du dihydrogène", "isCorrect": False},
                        {"text": "Une base forte et un sel minéral", "isCorrect": False}
                    ],
                    "correction": "L'estérification est la réaction entre un acide carboxylique (R−COOH) et un alcool (R'−OH). Elle produit un ester (R−COO−R') et de l'eau (H2O). C'est une réaction lente et réversible."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle caractéristique définit une réaction de polymérisation par polyaddition ?",
                    "answerOptions": [
                        {"text": "Les monomères insaturés s'additionnent par ouverture de leur double liaison sans élimination de petite molécule", "isCorrect": True},
                        {"text": "Les monomères s'assemblent systématiquement en libérant une molécule d'eau ou de chlorure d'hydrogène à chaque nouvelle liaison formée", "isCorrect": False},
                        {"text": "Les chaînes carbonées se cassent sous l'effet de la chaleur pour former des hydrocarbures gazeux beaucoup plus courts", "isCorrect": False},
                        {"text": "Les atomes de carbone remplacent progressivement leurs atomes d'hydrogène par des atomes d'oxygène issus de l'air ambiant", "isCorrect": False}
                    ],
                    "correction": "Lors d'une polyaddition (exemple : polyéthylène, PVC, polystyrène), la double liaison C=C des monomères s'ouvre pour former de longues chaînes sans aucune perte de matière. À l'inverse, la polycondensation élimine une petite molécule (souvent H2O)."
                },
                {
                    "questionNumber": 51,
                    "question": "Combien de liaisons covalentes forme toujours un atome de carbone dans une molécule organique ?",
                    "answerOptions": [
                        {"text": "4", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "3", "isCorrect": False},
                        {"text": "6", "isCorrect": False}
                    ],
                    "correction": "L'atome de carbone (Z = 6) possède 4 électrons sur sa couche externe. Pour satisfaire la règle de l'octet, il établit toujours 4 liaisons covalentes (simples, doubles ou triples)."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le nom systématique de l'alcane linéaire de formule brute C4H10 ?",
                    "answerOptions": [
                        {"text": "Butane", "isCorrect": True},
                        {"text": "Propane", "isCorrect": False},
                        {"text": "Pentane", "isCorrect": False},
                        {"text": "Éthane", "isCorrect": False}
                    ],
                    "correction": "Les préfixes des alcanes linéaires selon le nombre d'atomes de carbone sont : 1 = méthane, 2 = éthane, 3 = propane, 4 = butane, 5 = pentane, 6 = hexane."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle propriété physique permet de trier facilement le polyéthylène PE et le PVC par flottaison dans l'eau ?",
                    "answerOptions": [
                        {"text": "Leur densité par rapport à l'eau", "isCorrect": True},
                        {"text": "Leur conductivité électrique à froid", "isCorrect": False},
                        {"text": "Leur température d'ébullition sous vide", "isCorrect": False},
                        {"text": "Leur solubilité totale dans l'eau douce", "isCorrect": False}
                    ],
                    "correction": "Le polyéthylène (PE) et le polypropylène (PP) ont une densité inférieure à 1 (≈ 0,90 à 0,96) : ils flottent sur l'eau. Le PVC (≈ 1,38) et le PET (≈ 1,35) ont une densité supérieure à 1 : ils coulent."
                },
                {
                    "questionNumber": 54,
                    "question": "Pourquoi le recyclage chimique ou mécanique des matières plastiques nécessite-t-il un tri rigoureux par famille ?",
                    "answerOptions": [
                        {"text": "Parce que la plupart des polymères sont immiscibles entre eux et ont des températures de fusion différentes", "isCorrect": True},
                        {"text": "Parce que le mélange de deux polymères différents provoque immédiatement une réaction explosive au contact de l'air ambiant", "isCorrect": False},
                        {"text": "Parce que les polymères thermoplastiques se transforment spontanément en métaux lourds lorsqu'ils sont chauffés ensemble", "isCorrect": False},
                        {"text": "Parce que tous les plastiques ont la même température de fusion mais ne peuvent pas être broyés dans la même machine", "isCorrect": False}
                    ],
                    "correction": "Chaque polymère possède sa propre température de fusion et sa propre structure moléculaire. Mélanger des résines incompatibles (ex. PET et PVC) dégrade fortement les propriétés mécaniques du matériau recyclé et peut libérer des gaz corrosifs (HCl pour le PVC)."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le nom du groupe caractéristique -COOH présent dans l'acide éthanoïque ?",
                    "answerOptions": [
                        {"text": "Groupe carboxyle", "isCorrect": True},
                        {"text": "Groupe hydroxyle", "isCorrect": False},
                        {"text": "Groupe amine", "isCorrect": False},
                        {"text": "Groupe aldéhyde", "isCorrect": False}
                    ],
                    "correction": "Les acides carboxyliques (comme l'acide éthanoïque CH3−COOH, présent dans le vinaigre) sont caractérisés par le groupe carboxyle −COOH (un carbone doublement lié à un oxygène et simplement lié à −OH)."
                },
                {
                    "questionNumber": 56,
                    "question": "Que signifie l'acronyme COV utilisé pour les solvants organiques volatils ?",
                    "answerOptions": [
                        {"text": "Composés Organiques Volatils", "isCorrect": True},
                        {"text": "Carbones Oxydés Variables", "isCorrect": False},
                        {"text": "Catalyseurs Organiques Visqueux", "isCorrect": False},
                        {"text": "Composés Osmotiques Vapeur", "isCorrect": False}
                    ],
                    "correction": "Les COV (Composés Organiques Volatils) sont des substances organiques qui s'évaporent facilement à température ambiante (solvants, hydrocarbures). Ils présentent des risques pour la santé (inhalation) et l'environnement (ozone troposphérique)."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel produit principal caractérise une réaction de polycondensation entre deux monomères ?",
                    "answerOptions": [
                        {"text": "Un polymère accompagné de l'élimination d'une petite molécule", "isCorrect": True},
                        {"text": "Un polymère formé sans aucun sous-produit réactionnel", "isCorrect": False},
                        {"text": "Uniquement du dioxyde de carbone et de la suie", "isCorrect": False},
                        {"text": "Un alliage métallique obtenu par fusion à haute pression", "isCorrect": False}
                    ],
                    "correction": "Lors d'une polycondensation (synthèse du nylon ou du polyester PET), la liaison entre les monomères s'accompagne de l'élimination d'une petite molécule, le plus souvent de l'eau (H2O)."
                },
                {
                    "questionNumber": 58,
                    "question": "De quoi est constitué un matériau composite utilisé pour allier légèreté et résistance mécanique ?",
                    "answerOptions": [
                        {"text": "D'une matrice polymère qui assure la cohésion associée à un renfort fibreux qui reprend les efforts", "isCorrect": True},
                        {"text": "D'un mélange homogène de deux métaux purs fondus ensemble à très haute température pour former une solution solide", "isCorrect": False},
                        {"text": "D'une seule résine thermoplastique chauffée sous vide afin d'augmenter artificiellement sa masse volumique apparente", "isCorrect": False},
                        {"text": "De couches successives de solvants organiques volatils séchés à l'air libre sans aucune fibre ni charge minérale", "isCorrect": False}
                    ],
                    "correction": "Un matériau composite associe au moins deux composants non miscibles aux propriétés complémentaires : une matrice (souvent une résine polymère) qui protège et lie l'ensemble, et un renfort (fibres de verre, de carbone ou d'aramide) qui apporte la rigidité et la résistance mécanique."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel test simple de combustion permet d'identifier la présence de chlore dans le PVC ?",
                    "answerOptions": [
                        {"text": "Le test de Belstein donnant une flamme verte", "isCorrect": True},
                        {"text": "Le test à l'eau de chaux donnant un liquide bleu", "isCorrect": False},
                        {"text": "Le test à l'aimant attirant la matière plastique", "isCorrect": False},
                        {"text": "Le test au papier pH virant au violet foncé", "isCorrect": False}
                    ],
                    "correction": "Le test de Belstein consiste à chauffer un fil de cuivre imprégné du polymère dans une flamme : si le polymère contient du chlore (comme le PVC, polychlorure de vinyle), il se forme du chlorure de cuivre qui colore la flamme en vert."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est l'intérêt principal d'utiliser un solvant organique polaire ou apolaire adapté pour dissoudre une substance ?",
                    "answerOptions": [
                        {"text": "Une espèce se dissout efficacement dans un solvant de même nature chimique polaire ou apolaire", "isCorrect": True},
                        {"text": "Un solvant organique apolaire dissout systématiquement mieux les sels ioniques que l'eau distillée pure à température ambiante", "isCorrect": False},
                        {"text": "La dissolution d'un corps gras dans un solvant organique nécessite obligatoirement une réaction acido-basique complète", "isCorrect": False},
                        {"text": "Tous les solvants liquides sont parfaitement miscibles entre eux quelle que soit la structure électronique de leurs molécules", "isCorrect": False}
                    ],
                    "correction": "En chimie, la règle « qui se ressemble s'assemble » s'applique : les solvants polaires (comme l'eau) dissolvent bien les espèces polaires ou ioniques, tandis que les solvants apolaires (comme les hydrocarbures) dissolvent bien les espèces apolaires (graisses, huiles)."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : Thermique et transferts de chaleur (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : Thermique et transferts de chaleur",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est l'unité du Système International de la température absolue ?",
                    "answerOptions": [
                        {"text": "Kelvin", "isCorrect": True},
                        {"text": "Celsius", "isCorrect": False},
                        {"text": "Fahrenheit", "isCorrect": False},
                        {"text": "Joule", "isCorrect": False}
                    ],
                    "correction": "Dans le Système International, la température absolue T s'exprime en kelvins (symbole K, sans le signe degré). Le zéro absolu (0 K) correspond à −273,15 °C, état où l'agitation thermique est minimale."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle relation permet de convertir une température θ en degrés Celsius en température absolue T en kelvins ?",
                    "answerOptions": [
                        {"text": "T = θ + 273,15", "isCorrect": True},
                        {"text": "T = θ - 273,15", "isCorrect": False},
                        {"text": "T = θ × 273,15", "isCorrect": False},
                        {"text": "T = 273,15 / θ", "isCorrect": False}
                    ],
                    "correction": "L'échelle Kelvin est décalée de 273,15 unités par rapport à l'échelle Celsius : T(K) = θ(°C) + 273,15. Ainsi, 20 °C correspond à 293,15 K. Une variation ΔT a toutefois la même valeur en °C et en K."
                },
                {
                    "questionNumber": 63,
                    "question": "Quelle différence fondamentale distingue la température de la chaleur en physique ?",
                    "answerOptions": [
                        {"text": "La température mesure l'agitation microscopique alors que la chaleur est un transfert d'énergie thermique", "isCorrect": True},
                        {"text": "La chaleur s'exprime en degrés Celsius tandis que la température s'exprime systématiquement en watts par mètre carré", "isCorrect": False},
                        {"text": "La température représente la quantité totale d'énergie stockée dans un corps alors que la chaleur mesure sa masse volumique", "isCorrect": False},
                        {"text": "La chaleur est une propriété intrinsèque qui reste constante même lorsque deux corps de températures différentes se touchent", "isCorrect": False}
                    ],
                    "correction": "La température (en K ou °C) est une grandeur d'état liée à l'agitation thermique moyenne des particules. La chaleur Q (en J) est un mode de transfert d'énergie thermique entre deux systèmes de températures différentes."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle formule calcule l'énergie thermique Q nécessaire pour élever la température d'un corps sans changement d'état ?",
                    "answerOptions": [
                        {"text": "Q = m × c × ΔT", "isCorrect": True},
                        {"text": "Q = m × L", "isCorrect": False},
                        {"text": "Q = m × c / ΔT", "isCorrect": False},
                        {"text": "Q = c × ΔT / m", "isCorrect": False}
                    ],
                    "correction": "Sans changement d'état, l'énergie thermique échangée vaut Q = m × c × (T_finale − T_initiale), avec m la masse en kg, c la capacité thermique massique en J/(kg·K) et ΔT la variation de température en K ou °C."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle est l'unité du Système International de l'énergie thermique ?",
                    "answerOptions": [
                        {"text": "Joule", "isCorrect": True},
                        {"text": "Watt", "isCorrect": False},
                        {"text": "Kelvin", "isCorrect": False},
                        {"text": "Calorie", "isCorrect": False}
                    ],
                    "correction": "Comme toute forme d'énergie, l'énergie thermique (ou chaleur Q) s'exprime en joules (J) dans le Système International. Le watt (W) est l'unité de puissance thermique (ou flux thermique, en J/s)."
                },
                {
                    "questionNumber": 66,
                    "question": "À quelle température l'eau pure bout-elle sous pression atmosphérique normale ?",
                    "answerOptions": [
                        {"text": "100 degrés Celsius", "isCorrect": True},
                        {"text": "0 degré Celsius", "isCorrect": False},
                        {"text": "273 degrés Celsius", "isCorrect": False},
                        {"text": "80 degrés Celsius", "isCorrect": False}
                    ],
                    "correction": "Sous la pression atmosphérique normale (1 013 hPa), la température d'ébullition (vaporisation) de l'eau pure est de 100 °C (373,15 K). Elle diminue si la pression baisse (par exemple en haute altitude)."
                },
                {
                    "questionNumber": 67,
                    "question": "Comment évolue la température d'un corps pur pendant toute la durée de son changement d'état ?",
                    "answerOptions": [
                        {"text": "Elle reste rigoureusement constante tant que les deux états physiques coexistent", "isCorrect": True},
                        {"text": "Elle augmente linéairement avec le temps car l'énergie fournie accélère immédiatement l'agitation thermique des molécules", "isCorrect": False},
                        {"text": "Elle diminue brusquement au début de la fusion avant de remonter uniquement lorsque le récipient est fermé", "isCorrect": False},
                        {"text": "Elle oscille rapidement autour de la température ambiante jusqu'à la disparition complète du solide initial", "isCorrect": False}
                    ],
                    "correction": "À pression constante, le changement d'état d'un corps pur s'effectue à température constante (palier de température sur la courbe T = f(t)). Toute l'énergie thermique apportée sert à rompre les liaisons intermoléculaires (chaleur latente)."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment nomme-t-on le changement d'état permettant de passer de l'état solide à l'état liquide ?",
                    "answerOptions": [
                        {"text": "La fusion", "isCorrect": True},
                        {"text": "La solidification", "isCorrect": False},
                        {"text": "La sublimation", "isCorrect": False},
                        {"text": "La vaporisation", "isCorrect": False}
                    ],
                    "correction": "La fusion est le passage de l'état solide à l'état liquide (transformation endothermique, qui absorbe de la chaleur). Le passage inverse est la solidification."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle énergie thermique faut-il fournir pour chauffer 2 kg d'eau de 10 °C avec c = 4180 J/kg·K ?",
                    "answerOptions": [
                        {"text": "83 600 joules", "isCorrect": True},
                        {"text": "41 800 joules", "isCorrect": False},
                        {"text": "8 360 joules", "isCorrect": False},
                        {"text": "836 000 joules", "isCorrect": False}
                    ],
                    "correction": "On applique Q = m × c × ΔT = 2 × 4 180 × 10 = 83 600 J (soit 83,6 kJ). L'eau possède une capacité thermique massique très élevée, ce qui en fait un excellent fluide caloporteur."
                },
                {
                    "questionNumber": 70,
                    "question": "Comment s'effectue le transfert thermique par conduction à travers un matériau solide ?",
                    "answerOptions": [
                        {"text": "De proche en proche par agitation des atomes sans aucun déplacement global de matière", "isCorrect": True},
                        {"text": "Par déplacement macroscopique de courants chauds ascendants et froids descendants à l'intérieur du solide rigide", "isCorrect": False},
                        {"text": "Exclusivement par émission d'ondes électromagnétiques infrarouges capables de traverser le vide absolu sans support", "isCorrect": False},
                        {"text": "Par transformation chimique directe des molécules chaudes en molécules froides le long de la paroi métallique", "isCorrect": False}
                    ],
                    "correction": "La conduction thermique est le mode de transfert privilégié dans les solides : l'énergie cinétique d'agitation thermique se transmet de proche en proche entre particules voisines, sans déplacement d'ensemble de la matière."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel mode de transfert thermique peut se propager dans le vide ?",
                    "answerOptions": [
                        {"text": "Rayonnement", "isCorrect": True},
                        {"text": "Conduction", "isCorrect": False},
                        {"text": "Convection", "isCorrect": False},
                        {"text": "Évaporation", "isCorrect": False}
                    ],
                    "correction": "Le rayonnement thermique (principalement dans le domaine infrarouge) s'effectue par ondes électromagnétiques : il n'a besoin d'aucun support matériel et peut donc se propager dans le vide (comme la chaleur du Soleil jusqu'à la Terre)."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel mode de transfert thermique repose sur un déplacement global de matière dans un fluide ?",
                    "answerOptions": [
                        {"text": "La convection", "isCorrect": True},
                        {"text": "La conduction", "isCorrect": False},
                        {"text": "Le rayonnement", "isCorrect": False},
                        {"text": "La réfraction", "isCorrect": False}
                    ],
                    "correction": "La convection ne se produit que dans les fluides (liquides et gaz) : le fluide chaud, moins dense, s'élève tandis que le fluide froid, plus dense, descend, créant des mouvements de brassage qui transportent la chaleur."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle formule donne la résistance thermique surfacique R d'une paroi plane d'épaisseur e et de conductivité λ ?",
                    "answerOptions": [
                        {"text": "R = e / λ", "isCorrect": True},
                        {"text": "R = e × λ", "isCorrect": False},
                        {"text": "R = λ / e", "isCorrect": False},
                        {"text": "R = e / λ²", "isCorrect": False}
                    ],
                    "correction": "La résistance thermique surfacique R (en m²·K/W) caractérise le pouvoir isolant d'une paroi : R = e / λ, avec e l'épaisseur en mètres (m) et λ la conductivité thermique du matériau en W/(m·K)."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment reconnaît-on un bon isolant thermique à partir de sa conductivité thermique λ ?",
                    "answerOptions": [
                        {"text": "Sa conductivité thermique λ est très faible ce qui freine le passage du flux de chaleur", "isCorrect": True},
                        {"text": "Sa conductivité thermique λ est très élevée ce qui permet d'évacuer instantanément la chaleur vers l'extérieur", "isCorrect": False},
                        {"text": "Sa conductivité thermique λ est strictement supérieure à celle des métaux comme le cuivre ou l'aluminium", "isCorrect": False},
                        {"text": "Sa conductivité thermique λ dépend uniquement de la couleur de la peinture appliquée sur sa face externe", "isCorrect": False}
                    ],
                    "correction": "Plus la conductivité thermique λ est faible (ex. laine de verre ou polystyrène ≈ 0,035 W/(m·K)), moins le matériau laisse passer la chaleur et meilleur est l'isolant. À l'inverse, les métaux ont un λ très élevé (bons conducteurs thermiques)."
                },
                {
                    "questionNumber": 75,
                    "question": "Quelle est l'unité du Système International du flux thermique Φ traversant une paroi ?",
                    "answerOptions": [
                        {"text": "Le watt", "isCorrect": True},
                        {"text": "Le joule", "isCorrect": False},
                        {"text": "Le kelvin", "isCorrect": False},
                        {"text": "Le pascal", "isCorrect": False}
                    ],
                    "correction": "Le flux thermique Φ correspond à la quantité d'énergie thermique traversant une surface par unité de temps (Φ = Q / Δt). C'est donc une puissance thermique qui s'exprime en watts (W)."
                },
                {
                    "questionNumber": 76,
                    "question": "Comment appelle-t-on le passage de l'état gazeux à l'état liquide ?",
                    "answerOptions": [
                        {"text": "Liquéfaction", "isCorrect": True},
                        {"text": "Vaporisation", "isCorrect": False},
                        {"text": "Sublimation", "isCorrect": False},
                        {"text": "Solidification", "isCorrect": False}
                    ],
                    "correction": "Le passage de l'état gazeux à l'état liquide s'appelle la liquéfaction (souvent appelée condensation liquide dans le langage courant). C'est une transformation exothermique qui libère de la chaleur."
                },
                {
                    "questionNumber": 77,
                    "question": "Dans quel sens s'effectue toujours spontanément un transfert thermique entre deux corps en contact ?",
                    "answerOptions": [
                        {"text": "Du corps le plus chaud vers le corps le plus froid", "isCorrect": True},
                        {"text": "Du corps le plus froid vers le corps le plus chaud", "isCorrect": False},
                        {"text": "Du corps le plus lourd vers le corps le plus léger", "isCorrect": False},
                        {"text": "Du corps le plus dense vers le corps le moins dense", "isCorrect": False}
                    ],
                    "correction": "Selon le second principe de la thermodynamique, la chaleur se transfère toujours spontanément du milieu de température la plus élevée vers le milieu de température la plus basse, jusqu'à atteindre l'équilibre thermique."
                },
                {
                    "questionNumber": 78,
                    "question": "Que représente la chaleur latente massique L d'un corps pur lors d'un changement d'état ?",
                    "answerOptions": [
                        {"text": "L'énergie thermique nécessaire pour faire changer d'état un kilogramme de ce corps à température constante", "isCorrect": True},
                        {"text": "L'énergie thermique nécessaire pour élever la température d'un kilogramme de ce corps d'un degré Celsius sans fondre", "isCorrect": False},
                        {"text": "La puissance thermique maximale qu'un matériau solide peut dissiper par rayonnement infrarouge dans le vide absolu", "isCorrect": False},
                        {"text": "La variation de masse volumique subie par un liquide lorsqu'il est soumis à une compression isotherme prolongée", "isCorrect": False}
                    ],
                    "correction": "La chaleur latente massique L (en J/kg) représente l'énergie à fournir (ou à retirer) pour faire changer d'état 1 kg de corps pur sans variation de température. L'énergie totale échangée vaut Q = m × L."
                },
                {
                    "questionNumber": 79,
                    "question": "Comment calcule-t-on la résistance thermique totale d'une paroi composée de plusieurs couches accolées ?",
                    "answerOptions": [
                        {"text": "En additionnant les résistances thermiques de chaque couche", "isCorrect": True},
                        {"text": "En multipliant les résistances thermiques de chaque couche", "isCorrect": False},
                        {"text": "En prenant uniquement la résistance de la couche la plus épaisse", "isCorrect": False},
                        {"text": "En calculant la moyenne des conductivités thermiques", "isCorrect": False}
                    ],
                    "correction": "Pour une paroi multicouche (mur + isolant + parement) placée en série face au flux de chaleur, les résistances thermiques s'additionnent simplement : R_totale = R1 + R2 + R3 + ..."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment se comporte une surface noire mate par rapport à une surface blanche brillante exposée au rayonnement ?",
                    "answerOptions": [
                        {"text": "La surface noire mate absorbe beaucoup plus le rayonnement thermique et s'échauffe plus vite", "isCorrect": True},
                        {"text": "La surface blanche brillante absorbe la quasi-totalité du rayonnement infrarouge tout en bloquant la convection de l'air", "isCorrect": False},
                        {"text": "La surface noire mate réfléchit intégralement les ondes électromagnétiques ce qui maintient sa température très basse", "isCorrect": False},
                        {"text": "La couleur d'une surface n'a strictement aucune influence sur l'absorption ou l'émission d'un rayonnement thermique", "isCorrect": False}
                    ],
                    "correction": "Une surface sombre et mate possède un fort coefficient d'absorption (et d'émission) : elle capte efficacement le rayonnement lumineux et infrarouge, donc s'échauffe davantage. Une surface claire et brillante réfléchit la majorité du rayonnement."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : Acoustique, optique et ondes (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : Acoustique, optique et ondes",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est l'unité du Système International de la fréquence d'un son ?",
                    "answerOptions": [
                        {"text": "Hertz", "isCorrect": True},
                        {"text": "Décibel", "isCorrect": False},
                        {"text": "Seconde", "isCorrect": False},
                        {"text": "Mètre", "isCorrect": False}
                    ],
                    "correction": "La fréquence f d'une onde sonore correspond au nombre de vibrations par seconde. Son unité légale est le hertz (symbole Hz). Elle détermine la hauteur (grave ou aiguë) du son."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle est la vitesse approximative de propagation du son dans l'air à 20 °C ?",
                    "answerOptions": [
                        {"text": "340 mètres par seconde", "isCorrect": True},
                        {"text": "1 500 mètres par seconde", "isCorrect": False},
                        {"text": "300 000 mètres par seconde", "isCorrect": False},
                        {"text": "34 mètres par seconde", "isCorrect": False}
                    ],
                    "correction": "Dans l'air à 20 °C, le son se propage à environ 340 m/s (soit environ 1 224 km/h). Sa vitesse augmente dans les milieux plus denses : environ 1 500 m/s dans l'eau et plus de 5 000 m/s dans l'acier."
                },
                {
                    "questionNumber": 83,
                    "question": "Pourquoi un signal sonore ne peut-il pas se propager dans le vide spatial ?",
                    "answerOptions": [
                        {"text": "Le son est une onde mécanique qui nécessite un milieu matériel pour vibrer", "isCorrect": True},
                        {"text": "La fréquence des ondes sonores devient systématiquement nulle dès que la température ambiante descend sous zéro degré Celsius", "isCorrect": False},
                        {"text": "Les ondes sonores sont absorbées instantanément par le champ magnétique qui règne dans le vide interplanétaire", "isCorrect": False},
                        {"text": "La vitesse du son devient supérieure à celle de la lumière ce qui empêche toute réception par un capteur", "isCorrect": False}
                    ],
                    "correction": "Le son est une onde mécanique progressive (compression-dilatation de proche en proche des molécules). Sans support matériel (gaz, liquide ou solide), aucune vibration ne peut se transmettre : le son ne se propage pas dans le vide, contrairement à la lumière."
                },
                {
                    "questionNumber": 84,
                    "question": "Entre quelles fréquences se situe le domaine audible par une oreille humaine jeune et saine ?",
                    "answerOptions": [
                        {"text": "Entre 20 Hz et 20 000 Hz", "isCorrect": True},
                        {"text": "Entre 200 Hz et 2 000 Hz", "isCorrect": False},
                        {"text": "Entre 0 Hz et 100 000 Hz", "isCorrect": False},
                        {"text": "Entre 400 Hz et 800 Hz", "isCorrect": False}
                    ],
                    "correction": "L'oreille humaine perçoit les sons dont la fréquence est comprise entre 20 Hz (sons très graves) et 20 000 Hz (20 kHz, sons très aigus). En dessous de 20 Hz, ce sont des infrasons ; au-dessus de 20 kHz, ce sont des ultrasons."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle est l'unité usuelle du niveau d'intensité acoustique L ?",
                    "answerOptions": [
                        {"text": "Décibel", "isCorrect": True},
                        {"text": "Hertz", "isCorrect": False},
                        {"text": "Watt", "isCorrect": False},
                        {"text": "Lumen", "isCorrect": False}
                    ],
                    "correction": "Le niveau d'intensité acoustique L s'exprime en décibels (dB). Il est défini par une échelle logarithmique : L = 10 × log(I / I0), où I0 = 10⁻¹² W/m² est le seuil d'audibilité."
                },
                {
                    "questionNumber": 86,
                    "question": "De combien augmente le niveau sonore L lorsque l'on double le nombre de sources sonores identiques ?",
                    "answerOptions": [
                        {"text": "Il augmente de 3 décibels", "isCorrect": True},
                        {"text": "Il est multiplié par deux", "isCorrect": False},
                        {"text": "Il augmente de 10 décibels", "isCorrect": False},
                        {"text": "Il augmente de 6 décibels", "isCorrect": False}
                    ],
                    "correction": "L'échelle des décibels étant logarithmique, les niveaux sonores ne s'additionnent pas arithmétiquement. Doubler l'intensité acoustique I (deux machines identiques fonctionnant ensemble) ajoute toujours +3 dB (car 10 × log(2) ≈ 3)."
                },
                {
                    "questionNumber": 87,
                    "question": "Quelle caractéristique physique distingue un son aigu d'un son grave de même niveau sonore ?",
                    "answerOptions": [
                        {"text": "Un son aigu possède une fréquence plus élevée et une période plus courte qu'un son grave", "isCorrect": True},
                        {"text": "Un son aigu se propage beaucoup plus vite dans l'air ambiant qu'un son grave produit par la même source", "isCorrect": False},
                        {"text": "Un son aigu possède une amplitude de vibration nettement plus grande qu'un son grave de même intensité acoustique", "isCorrect": False},
                        {"text": "Un son aigu correspond systématiquement à une onde électromagnétique alors qu'un son grave est une onde mécanique", "isCorrect": False}
                    ],
                    "correction": "La hauteur d'un son dépend uniquement de sa fréquence f : plus f est élevée (et donc plus la période T = 1/f est courte), plus le son est aigu. L'amplitude détermine quant à elle l'intensité sonore (fort ou faible)."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel instrument permet de mesurer directement le niveau d'intensité acoustique en décibels ?",
                    "answerOptions": [
                        {"text": "Un sonomètre", "isCorrect": True},
                        {"text": "Un luxmètre", "isCorrect": False},
                        {"text": "Un fréquencemètre", "isCorrect": False},
                        {"text": "Un oscilloscope", "isCorrect": False}
                    ],
                    "correction": "Le sonomètre mesure le niveau d'intensité acoustique en dB (souvent en dB(A), pondération adaptée à la sensibilité de l'oreille humaine). Le luxmètre mesure l'éclairement lumineux."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle formule relie la longueur d'onde λ, la célérité c et la fréquence f d'une onde ?",
                    "answerOptions": [
                        {"text": "λ = c / f", "isCorrect": True},
                        {"text": "λ = c × f", "isCorrect": False},
                        {"text": "λ = f / c", "isCorrect": False},
                        {"text": "c = λ / f", "isCorrect": False}
                    ],
                    "correction": "La longueur d'onde λ (en m) est la distance parcourue par l'onde pendant une période T : λ = c × T = c / f, avec c la vitesse de propagation (en m/s) et f la fréquence (en Hz)."
                },
                {
                    "questionNumber": 90,
                    "question": "À partir de quel niveau sonore une exposition prolongée présente-t-elle un danger avéré pour l'audition ?",
                    "answerOptions": [
                        {"text": "Au-delà de 85 décibels, le risque de lésions irréversibles de l'oreille interne devient réel", "isCorrect": True},
                        {"text": "Uniquement au-delà de 140 décibels, car l'oreille humaine s'adapte sans dommage à tous les bruits inférieurs à ce seuil", "isCorrect": False},
                        {"text": "Dès 40 décibels, une exposition continue d'une heure détruit définitivement les cellules ciliées de la cochlée", "isCorrect": False},
                        {"text": "Le niveau en décibels n'a aucun impact auditif tant que la fréquence du son reste comprise dans le domaine audible", "isCorrect": False}
                    ],
                    "correction": "Le seuil de danger pour une exposition prolongée (8 heures par jour) est fixé à 85 dB(A), rendant le port de protections auditives obligatoire. Le seuil de douleur se situe autour de 120 dB."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle est la vitesse de propagation de la lumière dans le vide ?",
                    "answerOptions": [
                        {"text": "300 000 km/s", "isCorrect": True},
                        {"text": "340 m/s", "isCorrect": False},
                        {"text": "3 000 km/s", "isCorrect": False},
                        {"text": "30 000 km/s", "isCorrect": False}
                    ],
                    "correction": "Dans le vide (et approximativement dans l'air), la lumière se propage à une vitesse constante appelée célérité : c ≈ 3 × 10⁸ m/s, soit 300 000 km/s."
                },
                {
                    "questionNumber": 92,
                    "question": "Entre quelles longueurs d'onde se situe le spectre de la lumière visible par l'œil humain ?",
                    "answerOptions": [
                        {"text": "Entre 400 nm et 800 nm", "isCorrect": True},
                        {"text": "Entre 20 nm et 200 nm", "isCorrect": False},
                        {"text": "Entre 1 000 nm et 5 000 nm", "isCorrect": False},
                        {"text": "Entre 10 nm et 100 nm", "isCorrect": False}
                    ],
                    "correction": "Le spectre visible s'étend d'environ 400 nm (violet) à 800 nm (rouge). En dessous de 400 nm se trouvent les ultraviolets (UV) ; au-dessus de 800 nm se trouvent les infrarouges (IR)."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment appelle-t-on le changement de direction d'un rayon lumineux traversant la surface entre deux milieux transparents ?",
                    "answerOptions": [
                        {"text": "La réfraction lumineuse", "isCorrect": True},
                        {"text": "La réflexion spéculaire", "isCorrect": False},
                        {"text": "La diffraction lumineuse", "isCorrect": False},
                        {"text": "L'absorption totale", "isCorrect": False}
                    ],
                    "correction": "La réfraction est la déviation d'un rayon lumineux lorsqu'il passe d'un milieu transparent à un autre d'indice de réfraction différent (exemple : air vers eau ou verre), régie par la loi de Snell-Descartes : n1 × sin(i1) = n2 × sin(i2)."
                },
                {
                    "questionNumber": 94,
                    "question": "Que stipule la loi de Snell-Descartes concernant la réflexion d'un rayon lumineux sur un miroir plan ?",
                    "answerOptions": [
                        {"text": "L'angle de réflexion est toujours égal à l'angle d'incidence mesuré par rapport à la normale", "isCorrect": True},
                        {"text": "L'angle de réflexion est toujours le double de l'angle d'incidence mesuré par rapport à la surface réfléchissante", "isCorrect": False},
                        {"text": "Le rayon réfléchi ressort systématiquement perpendiculaire au miroir quelle que soit l'inclinaison du rayon incident", "isCorrect": False},
                        {"text": "L'angle de réflexion dépend exclusivement de la longueur d'onde et de la couleur de la lumière incidente", "isCorrect": False}
                    ],
                    "correction": "Lors d'une réflexion sur une surface plane réfléchissante, le rayon réfléchi reste dans le plan d'incidence et l'angle de réflexion r est égal à l'angle d'incidence i (i = r), tous deux mesurés par rapport à la normale au point d'incidence."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelles sont les trois couleurs primaires utilisées en synthèse additive de la lumière ?",
                    "answerOptions": [
                        {"text": "Rouge, vert et bleu", "isCorrect": True},
                        {"text": "Cyan, magenta et jaune", "isCorrect": False},
                        {"text": "Rouge, jaune et bleu", "isCorrect": False},
                        {"text": "Blanc, gris et noir", "isCorrect": False}
                    ],
                    "correction": "La synthèse additive consiste à superposer des faisceaux lumineux (écrans, projecteurs). Ses trois couleurs primaires sont le Rouge, le Vert et le Bleu (RVB / RGB)."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle couleur obtient-on en superposant à intensités égales les trois lumières primaires rouge, verte et bleue ?",
                    "answerOptions": [
                        {"text": "Blanc", "isCorrect": True},
                        {"text": "Noir", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Gris", "isCorrect": False}
                    ],
                    "correction": "En synthèse additive, la superposition des trois lumières primaires (Rouge + Vert + Bleu) à intensités égales reconstitue la lumière blanche."
                },
                {
                    "questionNumber": 97,
                    "question": "Quelles sont les trois couleurs primaires utilisées en synthèse soustractive pour les pigments et encres ?",
                    "answerOptions": [
                        {"text": "Cyan, magenta et jaune", "isCorrect": True},
                        {"text": "Rouge, vert et bleu", "isCorrect": False},
                        {"text": "Orange, vert et violet", "isCorrect": False},
                        {"text": "Noir, blanc et rouge", "isCorrect": False}
                    ],
                    "correction": "La synthèse soustractive concerne le mélange de pigments, d'encres ou de filtres colorés qui absorbent une partie de la lumière blanche. Ses trois couleurs primaires sont le Cyan, le Magenta et le Jaune (CMJ)."
                },
                {
                    "questionNumber": 98,
                    "question": "Pourquoi un objet opaque éclairé en lumière blanche apparaît-il de couleur bleue à nos yeux ?",
                    "answerOptions": [
                        {"text": "Il absorbe les autres radiations du spectre visible et diffuse principalement la lumière bleue", "isCorrect": True},
                        {"text": "Il absorbe exclusivement les radiations bleues de la lumière blanche et renvoie toutes les autres couleurs vers l'œil", "isCorrect": False},
                        {"text": "Il émet spontanément sa propre lumière bleue par réaction nucléaire dès qu'il est exposé à la température ambiante", "isCorrect": False},
                        {"text": "Il transforme la longueur d'onde de la lumière rouge incidente en lumière bleue par simple réfraction en surface", "isCorrect": False}
                    ],
                    "correction": "Un objet coloré agit comme un filtre par diffusion : éclairé en lumière blanche (qui contient toutes les couleurs), un objet bleu absorbe le rouge et le vert, et diffuse uniquement la composante bleue vers notre œil."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel phénomène optique observe-t-on lorsqu'un faisceau de lumière blanche traverse un prisme en verre ?",
                    "answerOptions": [
                        {"text": "La dispersion en un spectre continu de couleurs", "isCorrect": True},
                        {"text": "La réflexion totale de toutes les radiations", "isCorrect": False},
                        {"text": "L'extinction complète du faisceau lumineux", "isCorrect": False},
                        {"text": "La transformation en un faisceau laser monochromatique", "isCorrect": False}
                    ],
                    "correction": "L'indice de réfraction du verre dépend légèrement de la longueur d'onde. En traversant un prisme, les différentes radiations composant la lumière blanche sont déviées différemment (le violet plus que le rouge) : c'est la dispersion."
                },
                {
                    "questionNumber": 100,
                    "question": "À quelle condition la réflexion totale se produit-elle pour guider la lumière dans une fibre optique ?",
                    "answerOptions": [
                        {"text": "La lumière passe d'un milieu plus réfringent vers un milieu moins réfringent au-delà de l'angle limite", "isCorrect": True},
                        {"text": "La lumière passe d'un milieu moins réfringent vers un milieu plus réfringent avec un angle d'incidence strictement nul", "isCorrect": False},
                        {"text": "La fibre optique est obligatoirement remplie d'un gaz conducteur qui accélère la lumière au-delà de sa vitesse dans le vide", "isCorrect": False},
                        {"text": "L'indice de réfraction de la gaine extérieure doit être strictement supérieur à celui du cœur transparent de la fibre", "isCorrect": False}
                    ],
                    "correction": "Pour qu'il y ait réflexion totale (aucun rayon réfracté ne sort de la fibre), le cœur doit avoir un indice de réfraction n1 supérieur à celui de la gaine n2 (n1 > n2), et l'angle d'incidence doit dépasser l'angle limite de réfraction."
                }
            ]
        }
    }
}