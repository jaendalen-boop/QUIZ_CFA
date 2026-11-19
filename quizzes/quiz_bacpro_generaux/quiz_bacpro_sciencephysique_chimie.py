quiz_data = {
    "title": "Quiz BAC PRO Sciences Physiques - Chimie : Mécanique, Fluides & Électricité (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : Cinématique, mouvement et freinage (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : Cinématique, mouvement et freinage",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est l'unité du Système International de l'accélération ?",
                    "answerOptions": [
                        {"text": "m/s²", "isCorrect": True},
                        {"text": "m/s", "isCorrect": False},
                        {"text": "rad/s²", "isCorrect": False},
                        {"text": "N/kg", "isCorrect": False}
                    ],
                    "correction": "L'accélération correspond à la variation de vitesse par unité de temps (a = Δv / Δt). La vitesse s'exprimant en m/s et le temps en s, son unité légale est le mètre par seconde au carré (m/s²). Le rad/s² est l'accélération angulaire."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle valeur en m/s correspond exactement à une vitesse de 90 km/h ?",
                    "answerOptions": [
                        {"text": "25 mètres par seconde", "isCorrect": True},
                        {"text": "32,4 mètres par seconde", "isCorrect": False},
                        {"text": "15 mètres par seconde", "isCorrect": False},
                        {"text": "27,8 mètres par seconde", "isCorrect": False}
                    ],
                    "correction": "Pour convertir des km/h en m/s, on divise la valeur par 3,6. Ainsi, 90 / 3,6 = 25 m/s. Inversement, on multiplie par 3,6 pour passer des m/s aux km/h."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment évolue la distance de freinage d'un véhicule si sa vitesse double ?",
                    "answerOptions": [
                        {"text": "Elle est multipliée par quatre car elle dépend du carré de la vitesse", "isCorrect": True},
                        {"text": "Elle est multipliée par deux car la décélération reste strictement proportionnelle à la vitesse initiale", "isCorrect": False},
                        {"text": "Elle augmente de moitié uniquement si l'adhérence des pneumatiques reste constante sur sol sec", "isCorrect": False},
                        {"text": "Elle est multipliée par huit en raison de l'inertie cumulée du châssis et de la transmission", "isCorrect": False}
                    ],
                    "correction": "La distance de freinage est liée à l'énergie cinétique (Ec = 1/2 × m × v²) à dissiper par les freins. La formule d_f = v² / (2 × a) montre que d_f est proportionnelle au carré de la vitesse : si v est multipliée par 2, d_f est multipliée par 2² = 4."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle relation lie la vitesse linéaire v, le rayon R et la vitesse angulaire ω ?",
                    "answerOptions": [
                        {"text": "v = R × ω", "isCorrect": True},
                        {"text": "v = ω / R", "isCorrect": False},
                        {"text": "v = R / ω", "isCorrect": False},
                        {"text": "v = 2 × π × R × ω", "isCorrect": False}
                    ],
                    "correction": "Pour un point situé à une distance R de l'axe de rotation, la vitesse linéaire v (en m/s) est égale au produit du rayon R (en m) par la vitesse angulaire ω (en rad/s) : v = R × ω."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est l'unité légale de la vitesse angulaire ω ?",
                    "answerOptions": [
                        {"text": "rad/s", "isCorrect": True},
                        {"text": "tr/min", "isCorrect": False},
                        {"text": "Hz", "isCorrect": False},
                        {"text": "deg/s", "isCorrect": False}
                    ],
                    "correction": "Dans le Système International, l'angle s'exprime en radians (rad) et le temps en secondes (s). L'unité légale de la vitesse angulaire est donc le radian par seconde (rad/s), même si le tr/min est très utilisé en pratique."
                },
                {
                    "questionNumber": 6,
                    "question": "Comment se caractérise un mouvement rectiligne uniformément varié ?",
                    "answerOptions": [
                        {"text": "Trajectoire droite et accélération constante", "isCorrect": True},
                        {"text": "Trajectoire droite et vitesse constante", "isCorrect": False},
                        {"text": "Trajectoire circulaire et accélération nulle", "isCorrect": False},
                        {"text": "Trajectoire droite et accélération proportionnelle au temps", "isCorrect": False}
                    ],
                    "correction": "Dans un mouvement rectiligne uniformément varié (MRUV), la trajectoire est une droite et le vecteur accélération est constant et non nul. La vitesse varie alors de façon linéaire en fonction du temps : v(t) = a × t + v0."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle formule permet de calculer la vitesse angulaire ω à partir de la fréquence de rotation n en tr/min ?",
                    "answerOptions": [
                        {"text": "Il faut multiplier la fréquence en tours par minute par deux pi puis diviser par soixante", "isCorrect": True},
                        {"text": "Il faut multiplier la fréquence en tours par minute par soixante puis diviser le résultat total par deux pi", "isCorrect": False},
                        {"text": "Il faut diviser la fréquence en tours par minute par le rayon de la poulie exprimé en mètres", "isCorrect": False},
                        {"text": "Il faut multiplier la fréquence en tours par minute par pi puis diviser par trente-six", "isCorrect": False}
                    ],
                    "correction": "Un tour complet correspond à 2π radians et une minute compte 60 secondes. On convertit donc la fréquence de rotation N (en tr/min) en vitesse angulaire ω (en rad/s) par la formule : ω = (2 × π × N) / 60."
                },
                {
                    "questionNumber": 8,
                    "question": "Que représente la distance d'arrêt totale d'un véhicule ?",
                    "answerOptions": [
                        {"text": "Distance de réaction plus distance de freinage", "isCorrect": True},
                        {"text": "Distance de freinage moins distance de réaction", "isCorrect": False},
                        {"text": "Distance parcourue pendant le temps de réaction", "isCorrect": False},
                        {"text": "Distance de freinage multipliée par le coefficient d'adhérence", "isCorrect": False}
                    ],
                    "correction": "La distance d'arrêt (Da) est la somme de la distance parcourue pendant le temps de réaction du conducteur à vitesse constante (Dr = v × tr) et de la distance de freinage (Df) durant la phase de décélération : Da = Dr + Df."
                },
                {
                    "questionNumber": 9,
                    "question": "Une lame de scie circulaire tourne à 3000 tr/min. Quelle est sa fréquence de rotation en tr/s ?",
                    "answerOptions": [
                        {"text": "50 tours par seconde", "isCorrect": True},
                        {"text": "30 tours par seconde", "isCorrect": False},
                        {"text": "500 tours par seconde", "isCorrect": False},
                        {"text": "180 tours par seconde", "isCorrect": False}
                    ],
                    "correction": "Pour passer des tours par minute (tr/min) aux tours par seconde (tr/s ou Hz), on divise par 60 : n = 3000 / 60 = 50 tr/s."
                },
                {
                    "questionNumber": 10,
                    "question": "Quelle est la conséquence d'un temps de réaction de 1 seconde sur la distance parcourue à 108 km/h ?",
                    "answerOptions": [
                        {"text": "Le véhicule parcourt trente mètres avant le début effectif du freinage", "isCorrect": True},
                        {"text": "Le véhicule parcourt trente-six mètres avant que les plaquettes n'entrent en contact avec les disques", "isCorrect": False},
                        {"text": "Le véhicule parcourt dix-huit mètres à vitesse constante avant la phase de décélération", "isCorrect": False},
                        {"text": "Le véhicule parcourt cent huit mètres durant l'analyse visuelle de l'obstacle par le conducteur", "isCorrect": False}
                    ],
                    "correction": "On convertit d'abord la vitesse en m/s : v = 108 / 3,6 = 30 m/s. Pendant un temps de réaction tr = 1 s, le véhicule roule à vitesse constante : Dr = v × tr = 30 × 1 = 30 mètres."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est le signe de l'accélération lors d'un freinage en ligne droite ?",
                    "answerOptions": [
                        {"text": "Négatif", "isCorrect": True},
                        {"text": "Positif", "isCorrect": False},
                        {"text": "Nul", "isCorrect": False},
                        {"text": "Infini", "isCorrect": False}
                    ],
                    "correction": "Lors d'un freinage, la vitesse finale est inférieure à la vitesse initiale (Δv < 0). L'accélération a = Δv / Δt est donc négative ; on parle alors de décélération."
                },
                {
                    "questionNumber": 12,
                    "question": "Sur un graphique v = f(t), que représente la pente de la droite ?",
                    "answerOptions": [
                        {"text": "L'accélération du mobile", "isCorrect": True},
                        {"text": "La distance parcourue", "isCorrect": False},
                        {"text": "La vitesse moyenne", "isCorrect": False},
                        {"text": "La durée du trajet", "isCorrect": False}
                    ],
                    "correction": "Le coefficient directeur (la pente) de la courbe représentant la vitesse en fonction du temps correspond au rapport Δv / Δt, ce qui est la définition exacte de l'accélération a."
                },
                {
                    "questionNumber": 13,
                    "question": "Un véhicule passe de 0 à 20 m/s en 5 secondes. Quelle est son accélération moyenne ?",
                    "answerOptions": [
                        {"text": "4 mètres par seconde au carré", "isCorrect": True},
                        {"text": "100 mètres par seconde au carré", "isCorrect": False},
                        {"text": "0,25 mètre par seconde au carré", "isCorrect": False},
                        {"text": "2,5 mètres par seconde au carré", "isCorrect": False}
                    ],
                    "correction": "On applique la formule de l'accélération moyenne : a = (v_finale - v_initiale) / Δt = (20 - 0) / 5 = 4 m/s²."
                },
                {
                    "questionNumber": 14,
                    "question": "Pourquoi la vitesse linéaire en bout de dent d'une scie circulaire augmente-t-elle avec son diamètre ?",
                    "answerOptions": [
                        {"text": "Parce qu'à fréquence de rotation égale, un grand rayon augmente le périmètre parcouru par tour", "isCorrect": True},
                        {"text": "Parce qu'un diamètre plus important réduit automatiquement les frottements de l'air sur le carter de protection", "isCorrect": False},
                        {"text": "Parce que le moteur électrique adapte sa fréquence de rotation proportionnellement à la masse de la lame", "isCorrect": False},
                        {"text": "Parce que la vitesse angulaire en radians par seconde est directement proportionnelle au diamètre de l'outil", "isCorrect": False}
                    ],
                    "correction": "La vitesse périphérique (ou vitesse de coupe) vaut v = R × ω = π × D × n. À fréquence de rotation n constante, plus le diamètre D est grand, plus la distance parcourue en un tour est grande, donc plus la vitesse linéaire est élevée."
                },
                {
                    "questionNumber": 15,
                    "question": "Que représente l'aire sous la courbe d'un graphique vitesse en fonction du temps ?",
                    "answerOptions": [
                        {"text": "La distance parcourue par le mobile", "isCorrect": True},
                        {"text": "L'accélération instantanée du mobile", "isCorrect": False},
                        {"text": "L'énergie cinétique dissipée au freinage", "isCorrect": False},
                        {"text": "La vitesse maximale atteinte", "isCorrect": False}
                    ],
                    "correction": "Dans un repère v(t), le produit d'une vitesse (en m/s) par un temps (en s) donne une distance (en m). Géométriquement, la distance parcourue entre deux instants correspond donc à l'aire comprise sous la courbe."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la trajectoire d'un point situé sur la jante d'une roue par rapport au châssis ?",
                    "answerOptions": [
                        {"text": "Circulaire", "isCorrect": True},
                        {"text": "Rectiligne", "isCorrect": False},
                        {"text": "Cycloïdale", "isCorrect": False},
                        {"text": "Parabolique", "isCorrect": False}
                    ],
                    "correction": "Par rapport au châssis (référentiel du véhicule), l'axe de la roue est fixe : un point de la jante décrit donc un cercle. Par rapport à la route (référentiel terrestre), sa trajectoire serait une cycloïde."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle est la vitesse d'un véhicule qui parcourt 150 mètres en 6 secondes à allure constante ?",
                    "answerOptions": [
                        {"text": "90 kilomètres par heure", "isCorrect": True},
                        {"text": "25 kilomètres par heure", "isCorrect": False},
                        {"text": "72 kilomètres par heure", "isCorrect": False},
                        {"text": "108 kilomètres par heure", "isCorrect": False}
                    ],
                    "correction": "La vitesse en m/s est v = d / t = 150 / 6 = 25 m/s. Pour la convertir en km/h, on multiplie par 3,6 : 25 × 3,6 = 90 km/h."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel phénomène décrit la relativité du mouvement en mécanique classique ?",
                    "answerOptions": [
                        {"text": "La trajectoire et la vitesse d'un objet dépendent toujours du référentiel choisi pour l'observer", "isCorrect": True},
                        {"text": "La vitesse d'un solide en déplacement dépend exclusivement de sa masse et de la gravité locale mesurée", "isCorrect": False},
                        {"text": "Un objet en mouvement rectiligne uniforme possède la même vitesse dans tous les référentiels existants", "isCorrect": False},
                        {"text": "L'accélération d'un véhicule varie selon la couleur et l'aérodynamisme de sa carrosserie extérieure", "isCorrect": False}
                    ],
                    "correction": "Le mouvement est toujours relatif : on ne peut décrire la trajectoire ou la vitesse d'un objet sans préciser le référentiel (objet de référence). Par exemple, un passager est immobile par rapport à la voiture mais en mouvement par rapport à la route."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est la période T d'un arbre moteur tournant à une fréquence de 50 Hz ?",
                    "answerOptions": [
                        {"text": "0,02 seconde", "isCorrect": True},
                        {"text": "0,2 seconde", "isCorrect": False},
                        {"text": "50 secondes", "isCorrect": False},
                        {"text": "0,05 seconde", "isCorrect": False}
                    ],
                    "correction": "La période T (durée d'un tour complet en secondes) est l'inverse de la fréquence f (en Hz) : T = 1 / f = 1 / 50 = 0,02 s, soit 20 millisecondes."
                },
                {
                    "questionNumber": 20,
                    "question": "Dans un mouvement circulaire uniforme, que peut-on dire du vecteur vitesse ?",
                    "answerOptions": [
                        {"text": "Sa valeur reste constante mais sa direction change continuellement en restant tangente au cercle", "isCorrect": True},
                        {"text": "Sa valeur et sa direction restent strictement identiques tout au long de la rotation complète du solide", "isCorrect": False},
                        {"text": "Sa direction reste constamment dirigée vers le centre de rotation tandis que sa norme augmente", "isCorrect": False},
                        {"text": "Sa valeur diminue progressivement à chaque tour en raison de l'accélération centripète", "isCorrect": False}
                    ],
                    "correction": "Dans un mouvement circulaire uniforme, la norme (valeur) de la vitesse est constante, mais comme la trajectoire est courbe, la direction du vecteur vitesse change à chaque instant en restant toujours tangente au cercle. Il existe donc une accélération centripète dirigée vers le centre."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : Forces, couples et équilibre des solides (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : Forces, couples et équilibre des solides",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est l'unité du Système International du moment d'une force ?",
                    "answerOptions": [
                        {"text": "N·m", "isCorrect": True},
                        {"text": "N/m", "isCorrect": False},
                        {"text": "J/s", "isCorrect": False},
                        {"text": "kg·m", "isCorrect": False}
                    ],
                    "correction": "Le moment d'une force par rapport à un axe est le produit de l'intensité de la force (en N) par le bras de levier (en m). Son unité légale est donc le newton-mètre (N·m)."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle relation lie le poids P, la masse m et l'intensité de pesanteur g ?",
                    "answerOptions": [
                        {"text": "P = m × g", "isCorrect": True},
                        {"text": "P = m / g", "isCorrect": False},
                        {"text": "m = P × g", "isCorrect": False},
                        {"text": "g = P × m", "isCorrect": False}
                    ],
                    "correction": "Le poids P (en N) est une force proportionnelle à la masse m (en kg) du solide : P = m × g, où g est l'intensité de la pesanteur (environ 9,81 N/kg sur Terre)."
                },
                {
                    "questionNumber": 23,
                    "question": "À quelle condition un solide soumis uniquement à deux forces est-il en équilibre ?",
                    "answerOptions": [
                        {"text": "Elles ont la même droite d'action, la même valeur et des sens opposés", "isCorrect": True},
                        {"text": "Elles ont la même droite d'action, des valeurs strictement proportionnelles et des sens identiques", "isCorrect": False},
                        {"text": "Elles sont perpendiculaires entre elles et appliquées exactement au centre de gravité du solide", "isCorrect": False},
                        {"text": "Leurs droites d'action sont parallèles et la somme de leurs intensités est égale au poids", "isCorrect": False}
                    ],
                    "correction": "D'après le principe fondamental de la statique, un solide soumis à deux forces F1 et F2 est en équilibre si et seulement si F1 + F2 = 0 (en vecteurs), ce qui implique même droite d'action, même norme et sens contraires."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le poids d'un bloc moteur de 150 kg en prenant g = 9,8 N/kg ?",
                    "answerOptions": [
                        {"text": "1470 newtons", "isCorrect": True},
                        {"text": "15,3 newtons", "isCorrect": False},
                        {"text": "147 newtons", "isCorrect": False},
                        {"text": "1500 newtons", "isCorrect": False}
                    ],
                    "correction": "En appliquant P = m × g, on obtient P = 150 × 9,8 = 1470 N. Il est indispensable de distinguer la masse (en kg) du poids (en N)."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel instrument permet de mesurer directement l'intensité d'une force ?",
                    "answerOptions": [
                        {"text": "Dynamomètre", "isCorrect": True},
                        {"text": "Manomètre", "isCorrect": False},
                        {"text": "Tachymètre", "isCorrect": False},
                        {"text": "Balance", "isCorrect": False}
                    ],
                    "correction": "Le dynamomètre mesure l'intensité d'une force en newtons (N) grâce à l'allongement d'un ressort ou à une jauge de contrainte. La balance mesure une masse (en kg) et le manomètre une pression."
                },
                {
                    "questionNumber": 26,
                    "question": "Comment calcule-t-on le moment M d'une force F par rapport à un axe de rotation ?",
                    "answerOptions": [
                        {"text": "Produit de la force par le bras de levier", "isCorrect": True},
                        {"text": "Quotient de la force par le bras de levier", "isCorrect": False},
                        {"text": "Produit de la force par la vitesse angulaire", "isCorrect": False},
                        {"text": "Somme de la force et de la distance à l'axe", "isCorrect": False}
                    ],
                    "correction": "Le moment d'une force traduit son efficacité à faire tourner un solide autour d'un axe : M = F × d, avec F en newtons (N) et d (le bras de levier) en mètres (m)."
                },
                {
                    "questionNumber": 27,
                    "question": "Pourquoi utilise-t-on une rallonge sur une clé pour desserrer un écrou grippé ?",
                    "answerOptions": [
                        {"text": "Elle augmente le bras de levier pour obtenir un moment plus grand avec la même force", "isCorrect": True},
                        {"text": "Elle diminue le frottement interne du filetage en répartissant l'effort sur toute la longueur de la tige", "isCorrect": False},
                        {"text": "Elle réduit la force nécessaire en modifiant la masse volumique de l'acier au niveau de la douille", "isCorrect": False},
                        {"text": "Elle permet d'aligner la droite d'action de la force directement sur l'axe de rotation de l'écrou", "isCorrect": False}
                    ],
                    "correction": "Puisque M = F × d, augmenter la longueur de la clé augmente le bras de levier d. Pour un même effort musculaire F, le moment de rotation appliqué à l'écrou est donc beaucoup plus élevé."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le moment d'une force de 50 N appliquée avec un bras de levier de 40 cm ?",
                    "answerOptions": [
                        {"text": "20 newtons-mètres", "isCorrect": True},
                        {"text": "2000 newtons-mètres", "isCorrect": False},
                        {"text": "1,25 newtons-mètres", "isCorrect": False},
                        {"text": "200 newtons-mètres", "isCorrect": False}
                    ],
                    "correction": "Il faut d'abord convertir le bras de levier en mètres : d = 40 cm = 0,40 m. On applique ensuite M = F × d = 50 × 0,40 = 20 N·m."
                },
                {
                    "questionNumber": 29,
                    "question": "Comment définit-on géométriquement le bras de levier d'une force ?",
                    "answerOptions": [
                        {"text": "Distance perpendiculaire entre l'axe et la droite d'action", "isCorrect": True},
                        {"text": "Longueur totale de la pièce entre l'axe et l'extrémité", "isCorrect": False},
                        {"text": "Distance horizontale entre le sol et le point d'application", "isCorrect": False},
                        {"text": "Angle formé entre la force et le vecteur vitesse", "isCorrect": False}
                    ],
                    "correction": "Le bras de levier d est la plus courte distance (donc mesurée perpendiculairement) entre l'axe de rotation et la droite d'action de la force. Si la force est inclinée, d est inférieur à la longueur de la clé."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle condition assure l'équilibre en rotation d'un solide mobile autour d'un axe fixe ?",
                    "answerOptions": [
                        {"text": "La somme des moments tendant à tourner dans un sens égale celle de l'autre sens", "isCorrect": True},
                        {"text": "La somme vectorielle des forces appliquées sur le solide doit être strictement supérieure à la réaction de l'axe", "isCorrect": False},
                        {"text": "Toutes les forces exercées sur le solide doivent avoir exactement la même intensité et le même bras de levier", "isCorrect": False},
                        {"text": "Le centre de gravité du solide doit obligatoirement se trouver à l'extérieur de son axe de rotation", "isCorrect": False}
                    ],
                    "correction": "C'est le théorème des moments : un solide mobile autour d'un axe fixe est en équilibre si la somme algébrique des moments des forces qui lui sont appliquées est nulle (∑ M_horaire = ∑ M_antihoraire)."
                },
                {
                    "questionNumber": 31,
                    "question": "Entre la masse et le poids, quelle grandeur varie selon le lieu ou l'altitude ?",
                    "answerOptions": [
                        {"text": "Le poids", "isCorrect": True},
                        {"text": "La masse", "isCorrect": False},
                        {"text": "Les deux", "isCorrect": False},
                        {"text": "Aucune des deux", "isCorrect": False}
                    ],
                    "correction": "La masse (quantité de matière en kg) est invariable. Le poids (force d'attraction gravitationnelle en N) dépend de g, qui varie légèrement avec l'altitude et la latitude sur Terre, et fortement d'un astre à l'autre."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est l'énergie cinétique d'un solide de 10 kg se déplaçant à 4 m/s ?",
                    "answerOptions": [
                        {"text": "80 joules", "isCorrect": True},
                        {"text": "40 joules", "isCorrect": False},
                        {"text": "160 joules", "isCorrect": False},
                        {"text": "20 joules", "isCorrect": False}
                    ],
                    "correction": "L'énergie cinétique d'un solide en translation s'exprime par Ec = 1/2 × m × v², avec m en kg et v en m/s. Ici : Ec = 0,5 × 10 × 4² = 5 × 16 = 80 J."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est l'effet d'une force dont la droite d'action coupe l'axe de rotation ?",
                    "answerOptions": [
                        {"text": "Son moment est nul et elle ne provoque aucune rotation", "isCorrect": True},
                        {"text": "Son moment est maximal et elle accélère la rotation", "isCorrect": False},
                        {"text": "Elle inverse instantanément le sens de rotation du solide", "isCorrect": False},
                        {"text": "Elle double le couple transmis à l'arbre de sortie", "isCorrect": False}
                    ],
                    "correction": "Si la droite d'action passe par l'axe de rotation, le bras de levier d est égal à 0. Par conséquent, M = F × 0 = 0 N·m : cette force ne peut pas faire tourner le solide."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelles conditions caractérisent l'équilibre d'un solide soumis à trois forces non parallèles ?",
                    "answerOptions": [
                        {"text": "Leurs droites d'action sont concourantes et la somme vectorielle est nulle", "isCorrect": True},
                        {"text": "Leurs droites d'action sont strictement parallèles entre elles et leurs intensités sont toutes égales", "isCorrect": False},
                        {"text": "Leur polygone des forces reste ouvert et deux des forces doivent obligatoirement être perpendiculaires", "isCorrect": False},
                        {"text": "Leurs points d'application sont alignés sur l'horizontale et leurs sens sont tous dirigés vers le bas", "isCorrect": False}
                    ],
                    "correction": "Pour qu'un solide soumis à trois forces coplanaires non parallèles soit en équilibre, leurs droites d'action doivent se couper en un même point (elles sont concourantes) et le dynamique (polygone vectoriel) doit être fermé (F1 + F2 + F3 = 0)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle formule permet de calculer l'énergie potentielle de pesanteur Ep d'un solide ?",
                    "answerOptions": [
                        {"text": "Ep = m × g × h", "isCorrect": True},
                        {"text": "Ep = m × g / h", "isCorrect": False},
                        {"text": "Ep = 1/2 × m × v²", "isCorrect": False},
                        {"text": "Ep = m × h / g", "isCorrect": False}
                    ],
                    "correction": "L'énergie potentielle de pesanteur dépend de la masse m (en kg), de l'intensité de pesanteur g (en N/kg) et de l'altitude h (en m) par rapport à une référence : Ep = m × g × h."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le point d'application du vecteur poids d'un solide ?",
                    "answerOptions": [
                        {"text": "Centre de gravité", "isCorrect": True},
                        {"text": "Point de contact", "isCorrect": False},
                        {"text": "Axe de rotation", "isCorrect": False},
                        {"text": "Centre de poussée", "isCorrect": False}
                    ],
                    "correction": "Le poids est une force à distance répartie dans tout le volume du corps, mais on la modélise par une force unique appliquée au centre de gravité G du solide, dirigée verticalement vers le bas."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment évolue l'énergie mécanique d'un solide en chute libre sans frottement ?",
                    "answerOptions": [
                        {"text": "Elle reste constante tout au long de la chute", "isCorrect": True},
                        {"text": "Elle augmente proportionnellement à la vitesse de chute", "isCorrect": False},
                        {"text": "Elle diminue à mesure que l'altitude du solide baisse", "isCorrect": False},
                        {"text": "Elle s'annule juste avant l'impact avec le sol", "isCorrect": False}
                    ],
                    "correction": "En l'absence de frottements, l'énergie mécanique (Em = Ec + Ep) se conserve. Durant la chute, l'énergie potentielle de pesanteur diminue et se convertit intégralement en énergie cinétique."
                },
                {
                    "questionNumber": 38,
                    "question": "Quelle est la particularité mécanique d'un couple de forces par rapport à une force unique ?",
                    "answerOptions": [
                        {"text": "Un couple crée une rotation pure sans provoquer de translation de l'axe", "isCorrect": True},
                        {"text": "Un couple génère systématiquement une translation rectiligne uniforme associée à une déformation plastique", "isCorrect": False},
                        {"text": "Un couple nécessite deux forces perpendiculaires d'intensités différentes appliquées au même point", "isCorrect": False},
                        {"text": "Un couple annule totalement les frottements mécaniques au niveau des roulements de l'arbre", "isCorrect": False}
                    ],
                    "correction": "Un couple est constitué de deux forces parallèles, de même valeur et de sens opposés (exemple : deux mains sur un volant ou une clé en croix). Leur somme vectorielle est nulle (pas de translation), mais leurs moments s'additionnent pour créer une rotation pure : C = F × d."
                },
                {
                    "questionNumber": 39,
                    "question": "À quelle condition un meuble ou un véhicule posé au sol reste-t-il stable sans basculer ?",
                    "answerOptions": [
                        {"text": "La verticale du centre de gravité passe dans le polygone de sustentation", "isCorrect": True},
                        {"text": "Le centre de gravité se situe au-dessus de la moitié de la hauteur totale", "isCorrect": False},
                        {"text": "La masse du solide est strictement inférieure à sa surface d'appui au sol", "isCorrect": False},
                        {"text": "Le centre de gravité est décalé vers l'extérieur des points d'appui", "isCorrect": False}
                    ],
                    "correction": "Pour éviter le basculement, la droite verticale passant par le centre de gravité G doit couper le sol à l'intérieur de la base d'appui (polygone de sustentation). Plus G est bas et la base large, plus l'équilibre est stable."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est l'effet d'une chaussée mouillée sur l'adhérence des pneumatiques ?",
                    "answerOptions": [
                        {"text": "L'eau réduit fortement le coefficient d'adhérence et diminue la force maximale de freinage", "isCorrect": True},
                        {"text": "L'eau augmente le coefficient d'adhérence grâce à l'effet de succion hydraulique sous la bande de roulement", "isCorrect": False},
                        {"text": "L'eau modifie uniquement la masse apparente du véhicule sans changer le coefficient de frottement", "isCorrect": False},
                        {"text": "L'eau annule la réaction normale de la route tout en conservant une force de freinage constante", "isCorrect": False}
                    ],
                    "correction": "Un film d'eau entre la gomme et le bitume fait chuter le coefficient d'adhérence f (d'environ 0,8 sur sol sec à 0,4 voire moins sur sol mouillé). La force tangentielle maximale de freinage diminue donc fortement, allongeant la distance de freinage."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : Statique et dynamique des fluides (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : Statique et dynamique des fluides",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est l'unité du Système International de la pression ?",
                    "answerOptions": [
                        {"text": "Pascal", "isCorrect": True},
                        {"text": "Bar", "isCorrect": False},
                        {"text": "Newton", "isCorrect": False},
                        {"text": "Atmosphère", "isCorrect": False}
                    ],
                    "correction": "Dans le Système International, la pression s'exprime en pascals (Pa), ce qui correspond à 1 newton par mètre carré (1 Pa = 1 N/m²). Le bar est une unité usuelle très utilisée (1 bar = 10⁵ Pa)."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle relation permet de calculer la pression p exercée par une force pressante F sur une surface S ?",
                    "answerOptions": [
                        {"text": "p = F / S", "isCorrect": True},
                        {"text": "p = F × S", "isCorrect": False},
                        {"text": "p = S / F", "isCorrect": False},
                        {"text": "p = F × S²", "isCorrect": False}
                    ],
                    "correction": "La pression est le quotient de l'intensité de la force pressante F (en N) par l'aire de la surface pressée S (en m²) : p = F / S. Pour une même force, plus la surface est petite, plus la pression est élevée."
                },
                {
                    "questionNumber": 43,
                    "question": "Que stipule le principe de Pascal dans un liquide incompressible au repos ?",
                    "answerOptions": [
                        {"text": "Toute variation de pression en un point se transmet intégralement en tout point du liquide", "isCorrect": True},
                        {"text": "La pression diminue proportionnellement à la longueur de la canalisation entre le maître-cylindre et le récepteur", "isCorrect": False},
                        {"text": "La force exercée sur le piston récepteur reste toujours égale à la force appliquée sur le piston émetteur", "isCorrect": False},
                        {"text": "La pression hydrostatique dépend exclusivement de la forme du réservoir et du volume total de fluide contenu", "isCorrect": False}
                    ],
                    "correction": "Selon le principe de Pascal, un liquide incompressible transmet intégralement et dans toutes les directions toute variation de pression. C'est le principe fondamental des presses et vérins hydrauliques."
                },
                {
                    "questionNumber": 44,
                    "question": "À quelle valeur en pascals correspond exactement une pression de 2,5 bars ?",
                    "answerOptions": [
                        {"text": "250 000 pascals", "isCorrect": True},
                        {"text": "25 000 pascals", "isCorrect": False},
                        {"text": "2 500 pascals", "isCorrect": False},
                        {"text": "2 500 000 pascals", "isCorrect": False}
                    ],
                    "correction": "Comme 1 bar = 100 000 Pa (soit 10⁵ Pa), on multiplie la valeur en bars par 100 000 : 2,5 × 100 000 = 250 000 Pa, soit 250 kPa."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel appareil mesure la pression relative dans un pneumatique ou un circuit d'air comprimé ?",
                    "answerOptions": [
                        {"text": "Manomètre", "isCorrect": True},
                        {"text": "Baromètre", "isCorrect": False},
                        {"text": "Débitmètre", "isCorrect": False},
                        {"text": "Viscosimètre", "isCorrect": False}
                    ],
                    "correction": "Le manomètre mesure une pression relative (différence entre la pression du fluide et la pression atmosphérique). Le baromètre mesure uniquement la pression atmosphérique."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle formule exprime la différence de pression entre deux points d'un liquide au repos séparés par une hauteur h ?",
                    "answerOptions": [
                        {"text": "Δp = ρ × g × h", "isCorrect": True},
                        {"text": "Δp = ρ × V × g", "isCorrect": False},
                        {"text": "Δp = m × g × h", "isCorrect": False},
                        {"text": "Δp = ρ / g × h", "isCorrect": False}
                    ],
                    "correction": "D'après la loi fondamentale de l'hydrostatique, la différence de pression entre deux points d'un même fluide incompressible au repos vaut Δp = ρ × g × h, avec ρ la masse volumique (en kg/m³), g l'intensité de pesanteur (en N/kg) et h la différence de profondeur (en m)."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle différence fondamentale distingue un gaz d'un liquide soumis à une hausse de pression ?",
                    "answerOptions": [
                        {"text": "Un gaz est compressible et son volume diminue fortement alors qu'un liquide est quasi incompressible", "isCorrect": True},
                        {"text": "Un liquide est très compressible sous haute pression alors qu'un gaz conserve toujours un volume strictement fixe et invariable", "isCorrect": False},
                        {"text": "Un gaz voit sa masse volumique diminuer lors d'une compression alors que celle d'un liquide double instantanément", "isCorrect": False},
                        {"text": "Un liquide se dilate fortement sous l'effet de la pression tandis qu'un gaz se solidifie à température ambiante", "isCorrect": False}
                    ],
                    "correction": "Dans un gaz, les molécules sont très espacées : une augmentation de pression les rapproche facilement (le gaz est compressible). Dans un liquide, les molécules sont déjà au contact les unes des autres : son volume ne varie quasiment pas sous pression."
                },
                {
                    "questionNumber": 48,
                    "question": "Un manomètre indique 2,2 bars dans un pneu. Quelle est la pression absolue si la pression atmosphérique vaut 1 bar ?",
                    "answerOptions": [
                        {"text": "3,2 bars", "isCorrect": True},
                        {"text": "1,2 bars", "isCorrect": False},
                        {"text": "2,2 bars", "isCorrect": False},
                        {"text": "2,3 bars", "isCorrect": False}
                    ],
                    "correction": "La pression absolue est la somme de la pression relative (lue au manomètre) et de la pression atmosphérique : P_abs = P_rel + P_atm = 2,2 + 1 = 3,2 bars."
                },
                {
                    "questionNumber": 49,
                    "question": "Un piston de presse hydraulique a une surface de 0,02 m² et reçoit une pression de 500 000 Pa. Quelle force développe-t-il ?",
                    "answerOptions": [
                        {"text": "10 000 newtons", "isCorrect": True},
                        {"text": "25 000 newtons", "isCorrect": False},
                        {"text": "1 000 newtons", "isCorrect": False},
                        {"text": "100 000 newtons", "isCorrect": False}
                    ],
                    "correction": "À partir de p = F / S, on isole la force : F = p × S = 500 000 × 0,02 = 10 000 N (soit environ l'équivalent d'une tonne)."
                },
                {
                    "questionNumber": 50,
                    "question": "Comment un cric hydraulique permet-il de soulever un véhicule lourd avec un faible effort sur le levier ?",
                    "answerOptions": [
                        {"text": "La pression transmise agit sur un piston récepteur de section bien plus grande que le piston émetteur", "isCorrect": True},
                        {"text": "La viscosité de l'huile hydraulique multiplie automatiquement la pression à l'intérieur du vérin lors du pompage", "isCorrect": False},
                        {"text": "Le piston émetteur possède une surface supérieure au piston récepteur afin d'augmenter la vitesse de montée", "isCorrect": False},
                        {"text": "La pression hydrostatique augmente avec la longueur du flexible reliant la pompe manuelle au vérin principal", "isCorrect": False}
                    ],
                    "correction": "D'après le principe de Pascal, la pression est identique sur les deux pistons : F1 / S1 = F2 / S2. Donc F2 = F1 × (S2 / S1). En choisissant une grande surface S2 et une petite surface S1, on démultiplie la force au détriment de la course du piston."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est l'unité du Système International du débit volumique Q ?",
                    "answerOptions": [
                        {"text": "m³/s", "isCorrect": True},
                        {"text": "L/min", "isCorrect": False},
                        {"text": "m/s", "isCorrect": False},
                        {"text": "kg/s", "isCorrect": False}
                    ],
                    "correction": "Le débit volumique correspond au volume de fluide qui traverse une section par unité de temps (Q = V / t). Son unité légale est le mètre cube par seconde (m³/s), même si le L/min ou le m³/h sont courants en pratique."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle relation lie le débit volumique Q, la section S d'une conduite et la vitesse d'écoulement v ?",
                    "answerOptions": [
                        {"text": "Q = S × v", "isCorrect": True},
                        {"text": "Q = v / S", "isCorrect": False},
                        {"text": "Q = S / v", "isCorrect": False},
                        {"text": "Q = S × v²", "isCorrect": False}
                    ],
                    "correction": "Le débit volumique Q (en m³/s) est égal au produit de l'aire de la section droite S (en m²) par la vitesse moyenne d'écoulement v (en m/s) : Q = S × v."
                },
                {
                    "questionNumber": 53,
                    "question": "Dans une conduite où circule un fluide incompressible, que fait la vitesse d'écoulement lors d'un rétrécissement ?",
                    "answerOptions": [
                        {"text": "Elle augmente pour conserver le débit", "isCorrect": True},
                        {"text": "Elle diminue proportionnellement à la section", "isCorrect": False},
                        {"text": "Elle reste strictement constante partout", "isCorrect": False},
                        {"text": "Elle s'annule temporairement avant le coude", "isCorrect": False}
                    ],
                    "correction": "Par conservation du débit volumique (S1 × v1 = S2 × v2), si la section S2 diminue, la vitesse v2 augmente automatiquement dans le même rapport."
                },
                {
                    "questionNumber": 54,
                    "question": "Que prévoit l'effet Venturi lorsqu'un fluide s'accélère dans le rétrécissement d'une conduite horizontale ?",
                    "answerOptions": [
                        {"text": "Sa pression statique diminue dans la zone rétrécie au profit de son énergie cinétique", "isCorrect": True},
                        {"text": "Sa pression statique augmente fortement dans la zone rétrécie afin de compenser la perte de vitesse du fluide", "isCorrect": False},
                        {"text": "Sa pression statique reste rigoureusement identique sur toute la longueur quelle que soit la section traversée", "isCorrect": False},
                        {"text": "Sa masse volumique augmente proportionnellement au carré de la vitesse dans la partie la plus étroite", "isCorrect": False}
                    ],
                    "correction": "D'après le théorème de Bernoulli, pour un fluide incompressible en écoulement horizontal, la somme de la pression statique et de la pression dynamique (1/2 × ρ × v²) reste constante. Si la vitesse augmente dans un rétrécissement, la pression statique diminue."
                },
                {
                    "questionNumber": 55,
                    "question": "Comment évolue généralement la viscosité d'un liquide lorsque sa température augmente ?",
                    "answerOptions": [
                        {"text": "Elle diminue et le fluide devient plus fluide", "isCorrect": True},
                        {"text": "Elle augmente et le fluide devient plus épais", "isCorrect": False},
                        {"text": "Elle reste totalement indépendante de la température", "isCorrect": False},
                        {"text": "Elle augmente jusqu'à 50 degrés puis se stabilise", "isCorrect": False}
                    ],
                    "correction": "La viscosité traduit la résistance à l'écoulement d'un fluide. Pour les liquides, une hausse de température diminue les forces de cohésion entre molécules : la viscosité baisse et le liquide s'écoule plus facilement."
                },
                {
                    "questionNumber": 56,
                    "question": "Quelle est la valeur de la masse volumique de l'eau pure à température ambiante ?",
                    "answerOptions": [
                        {"text": "1000 kg/m³", "isCorrect": True},
                        {"text": "100 kg/m³", "isCorrect": False},
                        {"text": "1 kg/m³", "isCorrect": False},
                        {"text": "10 000 kg/m³", "isCorrect": False}
                    ],
                    "correction": "Un litre d'eau (1 dm³) a une masse de 1 kg. Comme 1 m³ contient 1 000 litres, la masse volumique de l'eau est de 1 000 kg/m³ (soit 1 kg/L ou 1 g/cm³)."
                },
                {
                    "questionNumber": 57,
                    "question": "À quoi est égale l'intensité de la poussée d'Archimède subie par un corps immergé ?",
                    "answerOptions": [
                        {"text": "Au poids du volume de fluide déplacé", "isCorrect": True},
                        {"text": "Au poids total du solide immergé", "isCorrect": False},
                        {"text": "À la masse volumique du solide multipliée par g", "isCorrect": False},
                        {"text": "À la pression hydrostatique exercée sur sa face supérieure", "isCorrect": False}
                    ],
                    "correction": "D'après le théorème d'Archimède, tout corps plongé dans un fluide subit une poussée verticale dirigée vers le haut, égale au poids du volume de fluide déplacé : Π = ρ_fluide × V_immergé × g."
                },
                {
                    "questionNumber": 58,
                    "question": "À quelle condition un solide homogène flotte-t-il à la surface d'un liquide au repos ?",
                    "answerOptions": [
                        {"text": "Sa masse volumique doit être inférieure à la masse volumique du liquide", "isCorrect": True},
                        {"text": "Sa masse totale exprimée en kilogrammes doit être strictement inférieure à celle du liquide contenu", "isCorrect": False},
                        {"text": "Son volume immergé doit être supérieur au volume total du récipient dans lequel il est plongé", "isCorrect": False},
                        {"text": "La pression atmosphérique exercée sur sa face supérieure doit être nulle au moment de l'immersion", "isCorrect": False}
                    ],
                    "correction": "Un corps flotte si la poussée d'Archimède maximale (Π = ρ_liquide × V × g) est supérieure à son poids (P = ρ_solide × V × g). Cela revient à comparer les masses volumiques : le solide flotte si ρ_solide < ρ_liquide (et coule si ρ_solide > ρ_liquide)."
                },
                {
                    "questionNumber": 59,
                    "question": "Une pompe délivre 30 litres de liquide en 1 minute. Quel est son débit volumique en m³/s ?",
                    "answerOptions": [
                        {"text": "0,0005 mètre cube par seconde", "isCorrect": True},
                        {"text": "0,5 mètre cube par seconde", "isCorrect": False},
                        {"text": "0,03 mètre cube par seconde", "isCorrect": False},
                        {"text": "0,005 mètre cube par seconde", "isCorrect": False}
                    ],
                    "correction": "On convertit le volume en m³ : 30 L = 0,03 m³, et le temps en secondes : 1 min = 60 s. Le débit vaut Q = V / t = 0,03 / 60 = 0,0005 m³/s (soit 5 × 10⁻⁴ m³/s)."
                },
                {
                    "questionNumber": 60,
                    "question": "Que prévoit la loi de Boyle-Mariotte pour un gaz comprimé à température constante ?",
                    "answerOptions": [
                        {"text": "Le produit de la pression par le volume reste constant tout au long de la transformation", "isCorrect": True},
                        {"text": "La pression du gaz diminue proportionnellement lorsque l'on réduit le volume du récipient fermé", "isCorrect": False},
                        {"text": "Le quotient de la pression par le volume reste invariable quelle que soit la masse de gaz", "isCorrect": False},
                        {"text": "Le volume du gaz augmente automatiquement lorsque la pression appliquée sur le piston double", "isCorrect": False}
                    ],
                    "correction": "La loi de Boyle-Mariotte stipule que pour une quantité donnée de gaz à température constante, la pression P et le volume V sont inversement proportionnels : P × V = constante (soit P1 × V1 = P2 × V2). Si le volume est divisé par 2, la pression double."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : Électricité en courant continu et batteries (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : Électricité en courant continu et batteries",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est l'unité du Système International de la résistance électrique ?",
                    "answerOptions": [
                        {"text": "Ohm", "isCorrect": True},
                        {"text": "Ampère", "isCorrect": False},
                        {"text": "Volt", "isCorrect": False},
                        {"text": "Watt", "isCorrect": False}
                    ],
                    "correction": "La résistance électrique R s'exprime en ohms (symbole Ω). Elle caractérise l'opposition d'un dipôle au passage du courant électrique."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle formule traduit correctement la loi d'Ohm aux bornes d'une résistance ?",
                    "answerOptions": [
                        {"text": "U = R × I", "isCorrect": True},
                        {"text": "U = R / I", "isCorrect": False},
                        {"text": "I = U × R", "isCorrect": False},
                        {"text": "R = U × I", "isCorrect": False}
                    ],
                    "correction": "La loi d'Ohm établit que la tension U (en volts) aux bornes d'un conducteur ohmique est proportionnelle à l'intensité I (en ampères) qui le traverse : U = R × I, avec R en ohms."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment doit-on impérativement brancher un ampèremètre pour mesurer l'intensité dans un circuit ?",
                    "answerOptions": [
                        {"text": "En série dans la branche concernée en ouvrant préalablement le circuit électrique", "isCorrect": True},
                        {"text": "En dérivation aux bornes directes du générateur afin de limiter la chute de tension mesurée", "isCorrect": False},
                        {"text": "En parallèle aux bornes du récepteur étudié sans jamais interrompre l'alimentation principale", "isCorrect": False},
                        {"text": "Entre la borne positive de la batterie et la masse métallique du châssis du véhicule", "isCorrect": False}
                    ],
                    "correction": "Un ampèremètre possède une résistance interne quasi nulle et doit être traversé par le courant à mesurer : il se branche donc toujours en série. Un branchement en dérivation provoquerait un court-circuit et la destruction du fusible interne du multimètre."
                },
                {
                    "questionNumber": 64,
                    "question": "Un projecteur de 60 W est alimenté sous une tension continue de 12 V. Quelle intensité le traverse ?",
                    "answerOptions": [
                        {"text": "5 ampères", "isCorrect": True},
                        {"text": "720 ampères", "isCorrect": False},
                        {"text": "0,2 ampère", "isCorrect": False},
                        {"text": "48 ampères", "isCorrect": False}
                    ],
                    "correction": "En courant continu, la puissance électrique vaut P = U × I. On en déduit l'intensité : I = P / U = 60 / 12 = 5 A."
                },
                {
                    "questionNumber": 65,
                    "question": "Quelle unité usuelle indique la capacité de charge d'une batterie ?",
                    "answerOptions": [
                        {"text": "Ah", "isCorrect": True},
                        {"text": "kW", "isCorrect": False},
                        {"text": "V/s", "isCorrect": False},
                        {"text": "Ω·m", "isCorrect": False}
                    ],
                    "correction": "La capacité Q d'une batterie s'exprime usuellement en ampères-heures (Ah). Elle représente la quantité d'électricité que la batterie peut restituer (Q = I × t). Dans le Système International, la charge s'exprime en coulombs (1 Ah = 3 600 C)."
                },
                {
                    "questionNumber": 66,
                    "question": "Que stipule la loi des nœuds dans un circuit électrique en dérivation ?",
                    "answerOptions": [
                        {"text": "La somme des intensités entrantes égale celle des sortantes", "isCorrect": True},
                        {"text": "L'intensité reste rigoureusement identique dans toutes les branches", "isCorrect": False},
                        {"text": "La somme des tensions autour d'un nœud est toujours nulle", "isCorrect": False},
                        {"text": "L'intensité principale est égale au produit des intensités dérivées", "isCorrect": False}
                    ],
                    "correction": "La loi des nœuds (première loi de Kirchhoff) traduit la conservation de la charge électrique : la somme des intensités des courants qui arrivent à un nœud est égale à la somme des intensités des courants qui en repartent."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le résultat du branchement en série de deux batteries identiques de 12 V et 70 Ah ?",
                    "answerOptions": [
                        {"text": "La tension totale atteint vingt-quatre volts tandis que la capacité reste de soixante-dix ampères-heures", "isCorrect": True},
                        {"text": "La tension reste fixée à douze volts tandis que la capacité totale cumulée atteint cent quarante ampères-heures", "isCorrect": False},
                        {"text": "La tension atteint vingt-quatre volts et la capacité double simultanément pour atteindre cent quarante ampères-heures", "isCorrect": False},
                        {"text": "La tension totale est divisée par deux afin de protéger les calculateurs contre les surintensités au démarrage", "isCorrect": False}
                    ],
                    "correction": "En série (borne + de la première reliée à la borne − de la seconde), les tensions s'additionnent (12 V + 12 V = 24 V), mais le courant traversant chaque batterie est le même : la capacité reste donc de 70 Ah."
                },
                {
                    "questionNumber": 68,
                    "question": "Dans un circuit en série, comment se répartit la tension fournie par le générateur ?",
                    "answerOptions": [
                        {"text": "Elle égale la somme des tensions aux bornes des récepteurs", "isCorrect": True},
                        {"text": "Elle est strictement identique aux bornes de chaque récepteur", "isCorrect": False},
                        {"text": "Elle est absorbée intégralement par le premier récepteur", "isCorrect": False},
                        {"text": "Elle augmente à chaque passage dans une résistance", "isCorrect": False}
                    ],
                    "correction": "D'après la loi d'additivité des tensions (loi des mailles), dans un circuit en série, la tension aux bornes du générateur est égale à la somme des tensions aux bornes de tous les récepteurs : U_gén = U1 + U2 + ..."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle énergie électrique consomme un appareil de 200 W fonctionnant pendant 3 heures ?",
                    "answerOptions": [
                        {"text": "600 wattheures", "isCorrect": True},
                        {"text": "66,7 wattheures", "isCorrect": False},
                        {"text": "600 joules", "isCorrect": False},
                        {"text": "1800 wattheures", "isCorrect": False}
                    ],
                    "correction": "L'énergie électrique consommée vaut E = P × t. Avec P = 200 W et t = 3 h, on obtient E = 200 × 3 = 600 Wh (soit 0,6 kWh). En joules, il faudrait convertir le temps en secondes (3 h = 10 800 s)."
                },
                {
                    "questionNumber": 70,
                    "question": "Que se passe-t-il électriquement lorsqu'un court-circuit franc survient dans un circuit ?",
                    "answerOptions": [
                        {"text": "La résistance devient quasi nulle et l'intensité augmente brutalement jusqu'à faire fondre le fusible", "isCorrect": True},
                        {"text": "La résistance du circuit tend vers l'infini ce qui annule instantanément la tension aux bornes du générateur", "isCorrect": False},
                        {"text": "L'intensité du courant chute à zéro tandis que la tension double dans l'ensemble des conducteurs voisins", "isCorrect": False},
                        {"text": "La puissance électrique consommée diminue fortement afin d'empêcher tout échauffement de la gaine isolante", "isCorrect": False}
                    ],
                    "correction": "Un court-circuit met en contact direct les deux bornes sans récepteur intermédiaire : la résistance R tend vers 0. D'après I = U / R, l'intensité I devient extrêmement élevée, provoquant un échauffement dangereux que le fusible doit interrompre."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel appareil permet de mesurer la différence de potentiel entre deux points d'un circuit ?",
                    "answerOptions": [
                        {"text": "Voltmètre", "isCorrect": True},
                        {"text": "Ohmmètre", "isCorrect": False},
                        {"text": "Ampèremètre", "isCorrect": False},
                        {"text": "Wattmètre", "isCorrect": False}
                    ],
                    "correction": "Le voltmètre mesure une tension (différence de potentiel) en volts. Il possède une très grande résistance interne et se branche toujours en dérivation (parallèle) aux bornes du dipôle étudié."
                },
                {
                    "questionNumber": 72,
                    "question": "Quelle est la résistance équivalente de deux résistances identiques de 10 Ω branchées en parallèle ?",
                    "answerOptions": [
                        {"text": "5 ohms", "isCorrect": True},
                        {"text": "20 ohms", "isCorrect": False},
                        {"text": "10 ohms", "isCorrect": False},
                        {"text": "100 ohms", "isCorrect": False}
                    ],
                    "correction": "Pour deux résistances en parallèle, 1/R_eq = 1/R1 + 1/R2. Ici, 1/R_eq = 1/10 + 1/10 = 2/10, donc R_eq = 10/2 = 5 Ω. Ajouter une branche en parallèle diminue toujours la résistance équivalente."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est l'allure de la caractéristique tension-intensité d'un conducteur ohmique ?",
                    "answerOptions": [
                        {"text": "Une droite passant par l'origine du repère", "isCorrect": True},
                        {"text": "Une droite horizontale parallèle à l'axe des abscisses", "isCorrect": False},
                        {"text": "Une courbe parabolique croissante à partir de l'origine", "isCorrect": False},
                        {"text": "Une droite décroissante coupant l'axe des ordonnées", "isCorrect": False}
                    ],
                    "correction": "D'après la loi d'Ohm (U = R × I), la tension U est proportionnelle à l'intensité I. Graphiquement, la caractéristique U = f(I) d'une résistance est donc une droite passant par l'origine dont le coefficient directeur est égal à R."
                },
                {
                    "questionNumber": 74,
                    "question": "Pourquoi un câble d'alimentation trop long ou de trop faible section provoque-t-il une chute de tension ?",
                    "answerOptions": [
                        {"text": "Parce que sa résistance électrique augmente avec la longueur et diminue avec la section", "isCorrect": True},
                        {"text": "Parce que la résistivité du cuivre augmente proportionnellement à la section transversale du conducteur", "isCorrect": False},
                        {"text": "Parce que les électrons ralentissent uniquement lorsque la gaine isolante est trop épaisse autour du fil", "isCorrect": False},
                        {"text": "Parce que la tension d'un générateur continu décroît naturellement avec la distance même sans courant", "isCorrect": False}
                    ],
                    "correction": "La résistance d'un fil conducteur suit la loi de Pouillet : R = ρ × (L / S). Si la longueur L augmente ou si la section S diminue, la résistance R augmente, ce qui crée une chute de tension parasite ΔU = R × I et un échauffement."
                },
                {
                    "questionNumber": 75,
                    "question": "Un récepteur résistif est parcouru par un courant de 3 A sous une tension de 12 V. Quelle est sa résistance ?",
                    "answerOptions": [
                        {"text": "4 ohms", "isCorrect": True},
                        {"text": "36 ohms", "isCorrect": False},
                        {"text": "0,25 ohm", "isCorrect": False},
                        {"text": "9 ohms", "isCorrect": False}
                    ],
                    "correction": "D'après la loi d'Ohm U = R × I, on isole la résistance : R = U / I = 12 / 3 = 4 Ω."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel phénomène physique provoque l'échauffement d'un conducteur parcouru par un courant électrique ?",
                    "answerOptions": [
                        {"text": "Effet Joule", "isCorrect": True},
                        {"text": "Effet Venturi", "isCorrect": False},
                        {"text": "Effet Doppler", "isCorrect": False},
                        {"text": "Effet Hall", "isCorrect": False}
                    ],
                    "correction": "L'effet Joule correspond à la dissipation d'énergie électrique sous forme de chaleur dans un conducteur résistant. La puissance thermique dissipée vaut P_J = R × I²."
                },
                {
                    "questionNumber": 77,
                    "question": "Pendant combien de temps théorique une batterie de 60 Ah peut-elle fournir un courant constant de 5 A ?",
                    "answerOptions": [
                        {"text": "12 heures", "isCorrect": True},
                        {"text": "300 heures", "isCorrect": False},
                        {"text": "5 heures", "isCorrect": False},
                        {"text": "6,5 heures", "isCorrect": False}
                    ],
                    "correction": "À partir de la relation Q = I × t, on calcule la durée de décharge théorique : t = Q / I = 60 / 5 = 12 heures."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est l'effet du couplage en parallèle de deux batteries identiques de 12 V et 60 Ah ?",
                    "answerOptions": [
                        {"text": "La tension reste de douze volts et la capacité totale double à cent vingt ampères-heures", "isCorrect": True},
                        {"text": "La tension totale double à vingt-quatre volts tandis que la capacité totale reste strictement de soixante ampères-heures", "isCorrect": False},
                        {"text": "La tension et la capacité doublent simultanément pour fournir vingt-quatre volts et cent vingt ampères-heures", "isCorrect": False},
                        {"text": "La tension reste de douze volts mais la capacité est divisée par deux pour limiter l'intensité de démarrage", "isCorrect": False}
                    ],
                    "correction": "En parallèle (bornes + reliées ensemble et bornes − reliées ensemble), la tension reste identique (12 V), mais les intensités et capacités disponibles s'additionnent : Q_totale = 60 + 60 = 120 Ah."
                },
                {
                    "questionNumber": 79,
                    "question": "Quelle puissance thermique dissipe une résistance de 10 Ω parcourue par un courant de 2 A ?",
                    "answerOptions": [
                        {"text": "40 watts", "isCorrect": True},
                        {"text": "20 watts", "isCorrect": False},
                        {"text": "200 watts", "isCorrect": False},
                        {"text": "5 watts", "isCorrect": False}
                    ],
                    "correction": "La puissance dissipée par effet Joule dans un dipôle ohmique s'exprime par P = R × I². Ici, P = 10 × 2² = 10 × 4 = 40 W."
                },
                {
                    "questionNumber": 80,
                    "question": "Pourquoi la tension aux bornes d'une pile diminue-t-elle lorsqu'elle débite un courant ?",
                    "answerOptions": [
                        {"text": "À cause de la chute de tension provoquée par sa résistance interne traversée par le courant", "isCorrect": True},
                        {"text": "Parce que sa force électromotrice devient nulle dès que l'interrupteur du circuit principal est fermé", "isCorrect": False},
                        {"text": "Parce que l'intensité du courant consommé par les récepteurs augmente la résistance des fils de connexion", "isCorrect": False},
                        {"text": "À cause de l'inversion spontanée de la polarité des électrodes lors de la circulation des électrons", "isCorrect": False}
                    ],
                    "correction": "Un générateur réel possède une force électromotrice E (tension à vide) et une résistance interne r. En charge, la tension à ses bornes suit la loi d'Ohm pour un générateur : U = E − r × I. Plus le courant I débité est fort, plus la tension U chute."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : Courant alternatif, moteurs et conversion d'énergie (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : Courant alternatif, moteurs et conversion d'énergie",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la fréquence du réseau électrique domestique en France ?",
                    "answerOptions": [
                        {"text": "50 Hz", "isCorrect": True},
                        {"text": "60 Hz", "isCorrect": False},
                        {"text": "100 Hz", "isCorrect": False},
                        {"text": "230 Hz", "isCorrect": False}
                    ],
                    "correction": "En France et dans toute l'Europe, le réseau public distribue un courant alternatif sinusoïdal de fréquence f = 50 Hz, ce qui signifie que la tension effectue 50 cycles complets par seconde."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle relation lie la tension maximale Umax et la tension efficace U d'un signal sinusoïdal ?",
                    "answerOptions": [
                        {"text": "Umax = U × √2", "isCorrect": True},
                        {"text": "Umax = U / √2", "isCorrect": False},
                        {"text": "Umax = U × 2", "isCorrect": False},
                        {"text": "Umax = U × π", "isCorrect": False}
                    ],
                    "correction": "Pour une tension sinusoïdale, la valeur maximale (ou amplitude) est liée à la valeur efficace (mesurée au voltmètre) par Umax = U × √2. Pour le réseau 230 V efficace, la tension crête atteint environ 325 V."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est le rôle principal d'un transformateur électrique alimenté en courant alternatif ?",
                    "answerOptions": [
                        {"text": "Modifier la valeur de la tension efficace tout en conservant exactement la même fréquence", "isCorrect": True},
                        {"text": "Convertir une tension alternative sinusoïdale en une tension continue parfaitement lissée pour les batteries", "isCorrect": False},
                        {"text": "Augmenter simultanément la tension efficace et la puissance active disponible sur le circuit secondaire", "isCorrect": False},
                        {"text": "Stabiliser le facteur de puissance d'un moteur asynchrone triphasé lors des phases de démarrage à vide", "isCorrect": False}
                    ],
                    "correction": "Un transformateur fonctionne par induction électromagnétique uniquement en courant alternatif. Il permet d'abaisser ou d'élever la tension (selon le rapport du nombre de spires N2/N1) sans modifier la fréquence et sans créer de puissance supplémentaire."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est la période T du signal sinusoïdal distribué par le réseau 50 Hz ?",
                    "answerOptions": [
                        {"text": "20 millisecondes", "isCorrect": True},
                        {"text": "50 millisecondes", "isCorrect": False},
                        {"text": "2 millisecondes", "isCorrect": False},
                        {"text": "0,2 seconde", "isCorrect": False}
                    ],
                    "correction": "La période T est l'inverse de la fréquence f : T = 1 / f = 1 / 50 = 0,02 s, soit 20 ms. C'est la durée d'un motif élémentaire complet sur l'écran d'un oscilloscope."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle est l'unité de la puissance apparente S en courant alternatif ?",
                    "answerOptions": [
                        {"text": "VA", "isCorrect": True},
                        {"text": "W", "isCorrect": False},
                        {"text": "var", "isCorrect": False},
                        {"text": "Wh", "isCorrect": False}
                    ],
                    "correction": "En courant alternatif, la puissance apparente S = U × I s'exprime en voltampères (VA). La puissance active P s'exprime en watts (W) et la puissance réactive Q en voltampères réactifs (var)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle formule donne la puissance active P consommée par un récepteur monophasé ?",
                    "answerOptions": [
                        {"text": "P = U × I × cos φ", "isCorrect": True},
                        {"text": "P = U × I / cos φ", "isCorrect": False},
                        {"text": "P = U × I × sin φ", "isCorrect": False},
                        {"text": "P = √3 × U × I", "isCorrect": False}
                    ],
                    "correction": "En régime sinusoïdal monophasé, la puissance active (réellement convertie en travail mécanique ou chaleur) vaut P = U × I × cos(φ), où cos(φ) est le facteur de puissance."
                },
                {
                    "questionNumber": 87,
                    "question": "Pourquoi un moteur asynchrone possède-t-il un facteur de puissance cos φ inférieur à 1 ?",
                    "answerOptions": [
                        {"text": "Parce que ses bobinages inductifs créent un déphasage entre la tension et l'intensité du courant", "isCorrect": True},
                        {"text": "Parce que sa résistance interne transforme systématiquement plus de la moitié de l'énergie en chaleur", "isCorrect": False},
                        {"text": "Parce que la fréquence du réseau électrique diminue progressivement à l'intérieur des enroulements statoriques", "isCorrect": False},
                        {"text": "Parce que le courant alternatif change de sens uniquement lorsque le rotor atteint sa vitesse nominale", "isCorrect": False}
                    ],
                    "correction": "Les enroulements (bobines) d'un moteur absorbent de la puissance réactive pour créer le champ magnétique tournant. Cette inductance retarde l'intensité par rapport à la tension d'un angle φ, ce qui rend cos(φ) inférieur à 1."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle est la tension efficace entre deux phases sur un réseau triphasé standard 230 V / 400 V ?",
                    "answerOptions": [
                        {"text": "400 volts", "isCorrect": True},
                        {"text": "230 volts", "isCorrect": False},
                        {"text": "690 volts", "isCorrect": False},
                        {"text": "115 volts", "isCorrect": False}
                    ],
                    "correction": "Sur un réseau triphasé 230 V / 400 V, la tension simple (entre une phase et le neutre) vaut V = 230 V, tandis que la tension composée (entre deux phases) vaut U = V × √3 ≈ 400 V."
                },
                {
                    "questionNumber": 89,
                    "question": "Un moteur absorbe une puissance électrique de 2000 W et fournit une puissance mécanique utile de 1600 W. Quel est son rendement ?",
                    "answerOptions": [
                        {"text": "80 %", "isCorrect": True},
                        {"text": "125 %", "isCorrect": False},
                        {"text": "40 %", "isCorrect": False},
                        {"text": "75 %", "isCorrect": False}
                    ],
                    "correction": "Le rendement η est le rapport entre la puissance utile (sortie) et la puissance absorbée (entrée) : η = Pu / Pa = 1600 / 2000 = 0,80, soit 80 %. Les 20 % restants (400 W) sont perdus principalement par effet Joule et frottements."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel phénomène physique permet à un alternateur de produire une tension électrique ?",
                    "answerOptions": [
                        {"text": "La variation d'un champ magnétique à proximité d'une bobine de fil conducteur", "isCorrect": True},
                        {"text": "Le frottement électrostatique permanent entre un aimant immobile et un noyau de fer doux", "isCorrect": False},
                        {"text": "La circulation d'un courant continu constant dans une résistance chauffante placée au centre du rotor", "isCorrect": False},
                        {"text": "La décomposition chimique d'un électrolyte acide sous l'effet de la rotation rapide de l'arbre", "isCorrect": False}
                    ],
                    "correction": "C'est le phénomène d'induction électromagnétique (découvert par Faraday) : déplacer un aimant (ou électroaimant) devant une bobine fait varier le champ magnétique qui la traverse, ce qui induit une tension alternative à ses bornes."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel appareil permet de visualiser la forme et la période d'une tension variable ?",
                    "answerOptions": [
                        {"text": "Oscilloscope", "isCorrect": True},
                        {"text": "Multimètre", "isCorrect": False},
                        {"text": "Wattmètre", "isCorrect": False},
                        {"text": "Tachymètre", "isCorrect": False}
                    ],
                    "correction": "L'oscilloscope affiche l'évolution instantanée de la tension en fonction du temps u(t), permettant de mesurer la période T et la tension maximale Umax."
                },
                {
                    "questionNumber": 92,
                    "question": "Quelle formule relie la puissance mécanique utile P, le couple C et la vitesse angulaire ω d'un moteur ?",
                    "answerOptions": [
                        {"text": "P = C × ω", "isCorrect": True},
                        {"text": "P = C / ω", "isCorrect": False},
                        {"text": "P = C × n", "isCorrect": False},
                        {"text": "C = P × ω", "isCorrect": False}
                    ],
                    "correction": "La puissance mécanique en rotation s'exprime en watts (W) par P = C × ω, avec le couple C en N·m et la vitesse angulaire ω en rad/s."
                },
                {
                    "questionNumber": 93,
                    "question": "Quelle est la valeur du facteur de puissance cos φ d'un radiateur électrique purement résistif ?",
                    "answerOptions": [
                        {"text": "Égal à 1", "isCorrect": True},
                        {"text": "Égal à 0", "isCorrect": False},
                        {"text": "Égal à 0,8", "isCorrect": False},
                        {"text": "Égal à 0,5", "isCorrect": False}
                    ],
                    "correction": "Dans un récepteur purement résistif (chauffage, lampe à incandescence), le courant et la tension sont parfaitement en phase (φ = 0°). Par conséquent, cos(φ) = cos(0) = 1 et P = U × I."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle d'un disjoncteur différentiel 30 mA en tête d'une installation électrique ?",
                    "answerOptions": [
                        {"text": "Couper l'alimentation dès qu'un courant de fuite vers la terre menace la sécurité des personnes", "isCorrect": True},
                        {"text": "Maintenir automatiquement la tension efficace à 230 volts même lors du démarrage d'un appareil puissant", "isCorrect": False},
                        {"text": "Protéger exclusivement les enroulements des moteurs triphasés contre les surcharges thermiques prolongées", "isCorrect": False},
                        {"text": "Inverser le sens de rotation d'une machine-outil en cas de détection d'un court-circuit entre phases", "isCorrect": False}
                    ],
                    "correction": "Le dispositif différentiel compare l'intensité entrante (phase) et sortante (neutre). Si la différence dépasse 30 mA (fuite de courant à la terre, potentiellement à travers un corps humain), il ouvre instantanément le circuit pour éviter l'électrocution."
                },
                {
                    "questionNumber": 95,
                    "question": "Comment se comportent les rendements de deux convertisseurs d'énergie placés en série ?",
                    "answerOptions": [
                        {"text": "Le rendement global est le produit des deux rendements", "isCorrect": True},
                        {"text": "Le rendement global est la somme des deux rendements", "isCorrect": False},
                        {"text": "Le rendement global est la moyenne des deux rendements", "isCorrect": False},
                        {"text": "Le rendement global est égal au rendement le plus élevé", "isCorrect": False}
                    ],
                    "correction": "Dans une chaîne énergétique (par exemple moteur électrique + réducteur mécanique), le rendement global est le produit des rendements individuels : η_global = η1 × η2. Il est donc toujours inférieur au plus petit des rendements."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la valeur maximale théorique du rendement d'une machine réelle ?",
                    "answerOptions": [
                        {"text": "Inférieure à 1", "isCorrect": True},
                        {"text": "Supérieure à 1", "isCorrect": False},
                        {"text": "Égale à 2", "isCorrect": False},
                        {"text": "Négative", "isCorrect": False}
                    ],
                    "correction": "Selon le principe de conservation de l'énergie, une machine réelle subit toujours des pertes (frottements, effet Joule, pertes fer). La puissance utile est donc toujours strictement inférieure à la puissance absorbée : η < 1 (ou < 100 %)."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel appareil protège un circuit électrique contre les surcharges et les courts-circuits ?",
                    "answerOptions": [
                        {"text": "Disjoncteur", "isCorrect": True},
                        {"text": "Voltmètre", "isCorrect": False},
                        {"text": "Transformateur", "isCorrect": False},
                        {"text": "Condensateur", "isCorrect": False}
                    ],
                    "correction": "Le disjoncteur magnétothermique coupe automatiquement le courant en cas de surcharge prolongée (déclencheur thermique) ou de court-circuit brutal (déclencheur magnétique), protégeant ainsi les conducteurs et les équipements."
                },
                {
                    "questionNumber": 98,
                    "question": "Pourquoi transporte-t-on l'électricité sur de longues distances sous très haute tension ?",
                    "answerOptions": [
                        {"text": "Pour réduire l'intensité du courant et limiter ainsi les pertes par effet Joule dans les câbles", "isCorrect": True},
                        {"text": "Pour augmenter l'intensité du courant dans les lignes afin d'accélérer la vitesse de propagation des électrons", "isCorrect": False},
                        {"text": "Pour diminuer la fréquence du réseau alternatif et éviter tout déphasage entre les centrales électriques", "isCorrect": False},
                        {"text": "Pour annuler complètement la résistance électrique des câbles en aluminium grâce à la haute tension", "isCorrect": False}
                    ],
                    "correction": "Pour transporter une même puissance P = U × I, élever la tension U permet de diviser l'intensité I dans le même rapport. Or les pertes thermiques en ligne valent P_J = R × I² : diviser I par 10 divise les pertes par effet Joule par 100."
                },
                {
                    "questionNumber": 99,
                    "question": "Un moteur électrique délivre un couple de 25 N·m à une vitesse angulaire de 100 rad/s. Quelle est sa puissance utile ?",
                    "answerOptions": [
                        {"text": "2500 watts", "isCorrect": True},
                        {"text": "4 watts", "isCorrect": False},
                        {"text": "250 watts", "isCorrect": False},
                        {"text": "125 watts", "isCorrect": False}
                    ],
                    "correction": "En appliquant P = C × ω, on obtient P = 25 × 100 = 2 500 W, soit 2,5 kW."
                },
                {
                    "questionNumber": 100,
                    "question": "Que mesure précisément un voltmètre réglé en position alternatif AC sur une prise secteur ?",
                    "answerOptions": [
                        {"text": "La valeur efficace de la tension qui correspond au même effet thermique qu'une tension continue", "isCorrect": True},
                        {"text": "La valeur maximale crête à crête atteinte par l'onde sinusoïdale à chaque demi-période complète", "isCorrect": False},
                        {"text": "La valeur moyenne arithmétique de la tension calculée sur une période entière du signal alternatif", "isCorrect": False},
                        {"text": "La tension minimale résiduelle mesurée entre le conducteur neutre et la borne de terre du tableau", "isCorrect": False}
                    ],
                    "correction": "Un voltmètre en mode AC indique la tension efficace U (230 V sur le secteur). La valeur moyenne d'une tension sinusoïdale pure sur une période est nulle, et sa valeur crête est Umax = 230 × √2 ≈ 325 V."
                }
            ]
        }
    }
}