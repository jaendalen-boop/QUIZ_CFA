# Fichier : quiz_cap_menuisier_fabricant_100.py

quiz_data = {
    "title": "Quiz CAP Menuisier Fabricant : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : MATÉRIAUX ET TECHNOLOGIES DU BOIS (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Matériaux et Technologies du Bois (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Comment appelle-t-on le phénomène de déformation du bois qui se produit lors du séchage (diminution de l'humidité) ?",
                    "answerOptions": [
                        {"text": "Le Gerçage.", "isCorrect": False},
                        {"text": "Le Retrait (diminution de volume).", "isCorrect": True},
                        {"text": "Le Tuilage.", "isCorrect": False},
                        {"text": "Le Flambage.", "isCorrect": False}
                    ],
                    "correction": "Le **Retrait** est la diminution dimensionnelle du bois due à la perte d'eau (séchage). Le **Gonflement** est l'inverse."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la principale caractéristique de l'essence de bois **Chêne** ?",
                    "answerOptions": [
                        {"text": "Bois très tendre et léger.", "isCorrect": False},
                        {"text": "Bois dur, résistant et durable, utilisé pour la menuiserie extérieure et le mobilier de prestige.", "isCorrect": True},
                        {"text": "Bois résineux à croissance rapide.", "isCorrect": False},
                        {"text": "Bois uniquement utilisé en charpente.", "isCorrect": False}
                    ],
                    "correction": "Le **Chêne** est une essence de feuillu noble, appréciée pour sa dureté et sa résistance à l'humidité."
                },
                {
                    "questionNumber": 3,
                    "question": "Quel est le pourcentage d'humidité visé pour les bois destinés à la **menuiserie intérieure** (meubles, portes intérieures) ?",
                    "answerOptions": [
                        {"text": "Plus de 30%.", "isCorrect": False},
                        {"text": "Environ 18% (bois extérieur).", "isCorrect": False},
                        {"text": "Entre 8% et 12%.", "isCorrect": True},
                        {"text": "0%.", "isCorrect": False}
                    ],
                    "correction": "Le bois destiné à l'intérieur doit être séché pour atteindre un taux d'humidité en équilibre avec l'air ambiant (8-12%) afin d'éviter les déformations."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment appelle-t-on le panneau composé de fines couches de bois (placages) collées à fils croisés ?",
                    "answerOptions": [
                        {"text": "L'Aggloméré (Panneau de particules).", "isCorrect": False},
                        {"text": "Le MDF (Medium Density Fiberboard).", "isCorrect": False},
                        {"text": "Le Contreplaqué.", "isCorrect": True},
                        {"text": "Le Panneau latté.", "isCorrect": False}
                    ],
                    "correction": "Le **Contreplaqué** offre une grande stabilité dimensionnelle grâce au collage à fils croisés."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est le rôle d'une **Lasure** (produit de finition pour bois) ?",
                    "answerOptions": [
                        {"text": "Former un film opaque et imperméable (comme une peinture).", "isCorrect": False},
                        {"text": "Protéger le bois contre l'humidité, les UV et les insectes, tout en laissant apparent le veinage (produit semi-transparent).", "isCorrect": True},
                        {"text": "Rendre le bois plus dur.", "isCorrect": False},
                        {"text": "Coller les chants.", "isCorrect": False}
                    ],
                    "correction": "La **Lasure** est utilisée en menuiserie extérieure pour l'entretien et la protection, sans masquer l'aspect naturel du bois."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle est la caractéristique essentielle du **MDF** (Panneau de fibres à moyenne densité) pour l'agencement ?",
                    "answerOptions": [
                        {"text": "Sa grande légèreté.", "isCorrect": False},
                        {"text": "Son homogénéité, permettant la coupe dans tous les sens et des usinages complexes (moulures, sculptures).", "isCorrect": True},
                        {"text": "Sa résistance à l'eau.", "isCorrect": False},
                        {"text": "Son faible coût de revient.", "isCorrect": False}
                    ],
                    "correction": "Le **MDF** est très utilisé en ébénisterie et agencement intérieur grâce à sa facilité d'usinage et sa bonne tenue des vis (à condition d'utiliser un vissage adapté)."
                },
                {
                    "questionNumber": 7,
                    "question": "Qu'est-ce que le **Contre-fil** dans une pièce de bois ?",
                    "answerOptions": [
                        {"text": "La direction de la fibre au centre du bois.", "isCorrect": False},
                        {"text": "La direction perpendiculaire à la veine du bois.", "isCorrect": False},
                        {"text": "La zone où la fibre du bois n'est pas parallèle à la surface de la pièce, rendant le rabotage ou l'usinage difficile (arrachement).", "isCorrect": True},
                        {"text": "La zone de couleur foncée.", "isCorrect": False}
                    ],
                    "correction": "Le **Contre-fil** est la direction inverse des fibres, souvent source d'arrachement de matière lors de l'usinage à la toupie ou à la raboteuse."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle colle est la plus couramment utilisée en menuiserie intérieure pour les assemblages non structuraux (meubles, caissons) ?",
                    "answerOptions": [
                        {"text": "La colle Polyuréthane (PU).", "isCorrect": False},
                        {"text": "La colle Époxy.", "isCorrect": False},
                        {"text": "La colle Vinylique (ou Colle Blanche, PVAC/PVA).", "isCorrect": True},
                        {"text": "La colle Néoprène.", "isCorrect": False}
                    ],
                    "correction": "La **colle vinylique** (D2, D3 pour l'humidité) est économique, facile d'emploi et assure un collage suffisant pour la menuiserie intérieure."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel terme désigne l'opération de recouvrir la tranche d'un panneau (MDF ou Agglo) avec une bande de bois ou de mélaminé pour masquer les fibres ?",
                    "answerOptions": [
                        {"text": "Le Ponçage.", "isCorrect": False},
                        {"text": "Le Placage.", "isCorrect": False},
                        {"text": "Le Chantournage.", "isCorrect": False},
                        {"text": "Le Plaquage de chants (ou le Chantournement).", "isCorrect": True}
                    ],
                    "correction": "Le **Plaquage de chants** est indispensable pour la finition des panneaux dérivés."
                },
                {
                    "questionNumber": 10,
                    "question": "Qu'est-ce qu'une **Bûche** de bois dans le jargon de la menuiserie ?",
                    "answerOptions": [
                        {"text": "Le bois de chauffage.", "isCorrect": False},
                        {"text": "Une pièce de bois destinée à la fabrication de tourillons.", "isCorrect": True},
                        {"text": "Une chute de bois.", "isCorrect": False},
                        {"text": "Un morceau de bois résineux.", "isCorrect": False}
                    ],
                    "correction": "Bien que le terme soit général, dans le contexte de l'assemblage, une **bûche** peut désigner un tourillon ou une cheville."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel est l'inconvénient majeur des panneaux de **particules brutes** (Aggloméré) par rapport au MDF ?",
                    "answerOptions": [
                        {"text": "Leur trop grande résistance.", "isCorrect": False},
                        {"text": "Leur mauvaise tenue à l'humidité et leur surface rugueuse ne permettant pas de belles finitions (peinture, laque).", "isCorrect": True},
                        {"text": "Leur légèreté.", "isCorrect": False},
                        {"text": "Leur prix élevé.", "isCorrect": False}
                    ],
                    "correction": "L'Aggloméré est souvent réservé aux meubles cachés ou recouvert de mélaminé/stratifié, car il est sensible à l'humidité et difficile à peindre proprement."
                },
                {
                    "questionNumber": 12,
                    "question": "Que signifie le traitement du bois par la classe **Classe 4** ?",
                    "answerOptions": [
                        {"text": "Utilisation intérieure sèche.", "isCorrect": False},
                        {"text": "Bois pouvant être en contact avec le sol ou l'eau douce (humidité permanente).", "isCorrect": True},
                        {"text": "Bois ignifugé.", "isCorrect": False},
                        {"text": "Bois très léger.", "isCorrect": False}
                    ],
                    "correction": "La **Classe 4** (ou classe d'emploi) est destinée aux bois très exposés (terrasse, poteaux extérieurs)."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle est la différence entre un **Vernis** et une **Lasure** ?",
                    "answerOptions": [
                        {"text": "Le Vernis protège moins bien.", "isCorrect": False},
                        {"text": "Le Vernis forme un film protecteur rigide et imperméable en surface (aspect plus plastique), tandis que la Lasure pénètre le bois (semi-transparent).", "isCorrect": True},
                        {"text": "La Lasure est toujours colorée.", "isCorrect": False},
                        {"text": "Le Vernis est réservé aux meubles.", "isCorrect": False}
                    ],
                    "correction": "Le **Vernis** est un produit filmogène qui peut craqueler à l'extérieur. La lasure est non-filmogène."
                },
                {
                    "questionNumber": 14,
                    "question": "Qu'est-ce qu'un panneau **Mélaminé** ?",
                    "answerOptions": [
                        {"text": "Un panneau recouvert de peinture.", "isCorrect": False},
                        {"text": "Un panneau (souvent Agglo ou MDF) dont la surface est revêtue de papier décor imprégné de résine mélamine, pressé à chaud.", "isCorrect": True},
                        {"text": "Un panneau très résistant au feu.", "isCorrect": False},
                        {"text": "Un panneau de bois massif.", "isCorrect": False}
                    ],
                    "correction": "Le **Mélaminé** est le matériau standard pour la fabrication de caissons de cuisine, penderies, bureaux grâce à son coût et sa facilité d'entretien."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel est l'outil utilisé pour mesurer le taux d'humidité du bois ?",
                    "answerOptions": [
                        {"text": "Le Mètre ruban.", "isCorrect": False},
                        {"text": "L'Hygromètre (ou Humidimètre).", "isCorrect": True},
                        {"text": "Le Pied à coulisse.", "isCorrect": False},
                        {"text": "Le Sonomètre.", "isCorrect": False}
                    ],
                    "correction": "L'**Hygromètre** est essentiel pour vérifier que le bois est apte à être usiné sans risque de déformation ultérieure."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le sens de la **Veine** du bois ?",
                    "answerOptions": [
                        {"text": "La direction de la coupe.", "isCorrect": False},
                        {"text": "La direction des fibres du bois, parallèle à l'axe de l'arbre (le 'fil du bois').", "isCorrect": True},
                        {"text": "La couleur du bois.", "isCorrect": False},
                        {"text": "Le sens du ponçage.", "isCorrect": False}
                    ],
                    "correction": "La **Veine** ou **Fil** du bois est le sens de la fibre. Il est crucial pour l'usinage, l'assemblage et la finition (ponçage, vernis)."
                },
                {
                    "questionNumber": 17,
                    "question": "Qu'est-ce que le **Placage** en menuiserie ?",
                    "answerOptions": [
                        {"text": "Un défaut du bois.", "isCorrect": False},
                        {"text": "L'opération de coller une feuille de bois mince (0,6 mm) sur un panneau support (Agglo, MDF) pour améliorer l'aspect esthétique.", "isCorrect": True},
                        {"text": "Le fait de peindre le bois.", "isCorrect": False},
                        {"text": "L'assemblage de deux pièces.", "isCorrect": False}
                    ],
                    "correction": "Le **Placage** permet d'obtenir l'aspect d'un bois noble à moindre coût et d'éviter les déformations du bois massif."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel type d'essence de bois est le **Pin maritime** ?",
                    "answerOptions": [
                        {"text": "Un bois exotique.", "isCorrect": False},
                        {"text": "Un résineux (bois tendre).", "isCorrect": True},
                        {"text": "Un feuillu (bois dur).", "isCorrect": False},
                        {"text": "Un bois composite.", "isCorrect": False}
                    ],
                    "correction": "Le **Pin** (sapin, épicéa) est un bois résineux (ou bois blanc), souvent utilisé en ossature, menuiserie courante ou pour les fonds de meubles."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle est la principale fonction du **Silicone (ou mastic)** en pose de menuiserie extérieure ?",
                    "answerOptions": [
                        {"text": "Le collage.", "isCorrect": False},
                        {"text": "Le calfeutrement et l'étanchéité à l'air et à l'eau entre le dormant de la fenêtre et la maçonnerie.", "isCorrect": True},
                        {"text": "La coloration.", "isCorrect": False},
                        {"text": "Le ponçage.", "isCorrect": False}
                    ],
                    "correction": "Le **mastic de calfeutrement** est un élément crucial pour les performances thermiques (RT2012/RE2020) et l'étanchéité de la fenêtre."
                },
                {
                    "questionNumber": 20,
                    "question": "Que signifie le sigle **PEFC** ou **FSC** sur les panneaux et bois ?",
                    "answerOptions": [
                        {"text": "Panneau de Fabrication Exceptionnelle.", "isCorrect": False},
                        {"text": "Certification garantissant que le bois provient d'une gestion forestière durable et responsable.", "isCorrect": True},
                        {"text": "Panneau Extérieur Forte Charge.", "isCorrect": False},
                        {"text": "Finition Sans Colle.", "isCorrect": False}
                    ],
                    "correction": "Ces certifications garantissent la **traçabilité** et l'origine environnementale du bois."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : LECTURE DE PLANS ET TRAÇAGE (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Lecture de Plans et Traçage (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Que représente une **échelle 1/10ème** dans un plan de menuiserie ou d'agencement ?",
                    "answerOptions": [
                        {"text": "1 mm sur le plan représente 10 cm dans la réalité.", "isCorrect": False},
                        {"text": "1 cm sur le plan représente 10 cm dans la réalité.", "isCorrect": True},
                        {"text": "1 cm sur le plan représente 10 mètres dans la réalité.", "isCorrect": False},
                        {"text": "Le plan est dix fois plus grand que la réalité.", "isCorrect": False}
                    ],
                    "correction": "L'échelle 1/10ème est très courante en menuiserie pour les plans d'exécution car elle permet de représenter de petits ouvrages avec précision."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment appelle-t-on le dessin qui représente l'objet vu de face, donnant les dimensions en largeur et hauteur ?",
                    "answerOptions": [
                        {"text": "La Coupe.", "isCorrect": False},
                        {"text": "L'Élévation (ou Vue de face).", "isCorrect": True},
                        {"text": "Le Plan de masse.", "isCorrect": False},
                        {"text": "La Perspective.", "isCorrect": False}
                    ],
                    "correction": "L'**Élévation** est essentielle pour l'implantation et le contrôle des hauteurs."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est l'outil utilisé pour reporter un angle précis (autre que 90°) d'un plan ou d'un mur sur une pièce de bois ?",
                    "answerOptions": [
                        {"text": "L'Équerre fixe.", "isCorrect": False},
                        {"text": "La Règle graduée.", "isCorrect": False},
                        {"text": "La Fausse équerre (ou sauterelle).", "isCorrect": True},
                        {"text": "Le Trusquin.", "isCorrect": False}
                    ],
                    "correction": "La **Fausse équerre** permet de prendre un angle et de le bloquer pour le reporter sans erreur."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel outil de traçage sert à tracer des lignes parallèles au bord d'une pièce de bois ?",
                    "answerOptions": [
                        {"text": "Le Crayon.", "isCorrect": False},
                        {"text": "Le Compas.", "isCorrect": False},
                        {"text": "Le Trusquin.", "isCorrect": True},
                        {"text": "Le Niveau.", "isCorrect": False}
                    ],
                    "correction": "Le **Trusquin** est indispensable pour marquer l'épaisseur des tenons, mortaises ou feuillures."
                },
                {
                    "questionNumber": 25,
                    "question": "Que représente une ligne en **pointillés fins** sur un plan de menuiserie ?",
                    "answerOptions": [
                        {"text": "Une arête visible.", "isCorrect": False},
                        {"text": "Une ligne de coupe.", "isCorrect": False},
                        {"text": "Une arête cachée (ou une pièce située derrière la vue principale).", "isCorrect": True},
                        {"text": "L'axe de symétrie.", "isCorrect": False}
                    ],
                    "correction": "Le trait en **pointillés fins** (trait interrompu fin) est la convention pour représenter les éléments non visibles."
                },
                {
                    "questionNumber": 26,
                    "question": "Comment appelle-t-on la **représentation grandeur nature** (souvent sur panneau ou au sol) de l'ouvrage, permettant de vérifier toutes les cotes et les assemblages avant la fabrication ?",
                    "answerOptions": [
                        {"text": "Le Plan d'ensemble.", "isCorrect": False},
                        {"text": "L'Épure.", "isCorrect": True},
                        {"text": "Le Schéma électrique.", "isCorrect": False},
                        {"text": "Le Croquis.", "isCorrect": False}
                    ],
                    "correction": "L'**Épure** est la base du travail traditionnel du menuisier, garantissant l'exactitude de toutes les pièces."
                },
                {
                    "questionNumber": 27,
                    "question": "Quel est l'objectif principal de la phase de **Traçage** ?",
                    "answerOptions": [
                        {"text": "Couper le bois.", "isCorrect": False},
                        {"text": "Dessiner sur les pièces de bois les lignes de coupe et d'usinage (emplacement des assemblages, moulures, etc.) avec exactitude.", "isCorrect": True},
                        {"text": "Vérifier la couleur.", "isCorrect": False},
                        {"text": "Coller les pièces.", "isCorrect": False}
                    ],
                    "correction": "Le **Traçage** est l'étape qui transfère les informations du plan à la pièce, toute erreur est critique."
                },
                {
                    "questionNumber": 28,
                    "question": "Que signifie le sigle **NFP 01-010** (norme de dessin technique) ?",
                    "answerOptions": [
                        {"text": "Norme de Fabrication des Portes.", "isCorrect": False},
                        {"text": "Règles générales de représentation (projection orthogonale, vues, coupes).", "isCorrect": True},
                        {"text": "Norme de Fixation des Poutres.", "isCorrect": False},
                        {"text": "Norme de finition des Parquets.", "isCorrect": False}
                    ],
                    "correction": "La **NFP 01-010** fixe les conventions de base pour la lecture et la réalisation des plans."
                },
                {
                    "questionNumber": 29,
                    "question": "Comment appelle-t-on la vue d'un plan qui montre le bâtiment ou l'agencement comme s'il était coupé par un plan vertical, révélant les épaisseurs, hauteurs et intérieurs cachés ?",
                    "answerOptions": [
                        {"text": "La Vue de dessus.", "isCorrect": False},
                        {"text": "La Coupe.", "isCorrect": True},
                        {"text": "L'Élévation.", "isCorrect": False},
                        {"text": "La Perspective.", "isCorrect": False}
                    ],
                    "correction": "La **Coupe** (A-A, B-B...) est indispensable pour comprendre l'assemblage et les détails de pose (dormant dans la maçonnerie)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est le repère utilisé pour positionner les éléments d'une menuiserie par rapport à une structure (mur ou dalle) ?",
                    "answerOptions": [
                        {"text": "La Couleur.", "isCorrect": False},
                        {"text": "Le Nu intérieur et le Nu extérieur (surface finie de la maçonnerie).", "isCorrect": True},
                        {"text": "L'épaisseur du verre.", "isCorrect": False},
                        {"text": "Le Fil du bois.", "isCorrect": False}
                    ],
                    "correction": "Les cotes de pose des dormants sont toujours données par rapport au **Nu extérieur** ou **Nu intérieur** de la maçonnerie."
                },
                {
                    "questionNumber": 31,
                    "question": "Dans le système de **Cotes** (dimensions) sur un plan, que représente la ligne d'attache ?",
                    "answerOptions": [
                        {"text": "Le trait de coupe.", "isCorrect": False},
                        {"text": "Le prolongement de l'arête à coter, définissant les limites de la mesure.", "isCorrect": True},
                        {"text": "La dimension numérique.", "isCorrect": False},
                        {"text": "Le symbole d'épaisseur.", "isCorrect": False}
                    ],
                    "correction": "Les **lignes d'attache** et les **lignes de cote** sont les bases de la cotation."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel instrument de mesure assure une précision au centième de millimètre pour le contrôle des dimensions (épaisseur, diamètre) ?",
                    "answerOptions": [
                        {"text": "Le Mètre ruban.", "isCorrect": False},
                        {"text": "Le Pied à coulisse.", "isCorrect": True},
                        {"text": "L'Équerre.", "isCorrect": False},
                        {"text": "La Règle de maçon.", "isCorrect": False}
                    ],
                    "correction": "Le **Pied à coulisse** est l'outil de contrôle de précision indispensable en atelier pour vérifier l'épaisseur des usinages."
                },
                {
                    "questionNumber": 33,
                    "question": "Lors du traçage d'un Tenon-Mortaise, pourquoi doit-on toujours tracer sur les **faces de parement** (faces de référence) ?",
                    "answerOptions": [
                        {"text": "Pour que ce soit plus joli.", "isCorrect": False},
                        {"text": "Pour assurer la précision et la justesse de l'assemblage en prenant en compte les éventuels défauts d'équerrage ou d'épaisseur de la pièce.", "isCorrect": True},
                        {"text": "Pour gagner du temps.", "isCorrect": False},
                        {"text": "Pour ne pas abîmer le bois.", "isCorrect": False}
                    ],
                    "correction": "La **Face de Parement** (FP) et le **Chant de Parement** (CP) sont les références d'où partent toutes les mesures."
                },
                {
                    "questionNumber": 34,
                    "question": "Comment appelle-t-on le plan qui indique la position d'un meuble ou d'une menuiserie par rapport aux murs et aux autres équipements de la pièce ?",
                    "answerOptions": [
                        {"text": "Le Plan de ferraillage.", "isCorrect": False},
                        {"text": "Le Plan d'implantation.", "isCorrect": True},
                        {"text": "Le Schéma de principe.", "isCorrect": False},
                        {"text": "Le Plan de coupe.", "isCorrect": False}
                    ],
                    "correction": "Le **Plan d'implantation** est utilisé lors de la pose sur chantier."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est l'outil essentiel pour vérifier que les angles d'un cadre (porte, fenêtre) sont parfaitement droits ?",
                    "answerOptions": [
                        {"text": "La Règle.", "isCorrect": False},
                        {"text": "L'Équerre (fixe ou à chapeau).", "isCorrect": True},
                        {"text": "Le Compas.", "isCorrect": False},
                        {"text": "Le Niveau laser.", "isCorrect": False}
                    ],
                    "correction": "L'**Équerre** est l'outil de base pour le contrôle des angles à 90°."
                },
                {
                    "questionNumber": 36,
                    "question": "Sur un plan, que représente le symbole d'un **cercle avec deux flèches opposées** ?",
                    "answerOptions": [
                        {"text": "Un axe de symétrie.", "isCorrect": False},
                        {"text": "Le sens d'ouverture et de rotation d'une porte (ouvrant à la française).", "isCorrect": True},
                        {"text": "Un robinet.", "isCorrect": False},
                        {"text": "Un éclairage.", "isCorrect": False}
                    ],
                    "correction": "Ce symbole indique le type d'ouverture (poussant ou tirant) et le sens du débattement."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est le nom donné au trait d'outil qui délimite la longueur finie (ou la fin de l'assemblage) de la pièce ?",
                    "answerOptions": [
                        {"text": "Le Trait de rive.", "isCorrect": True},
                        {"text": "Le Trait de coupe.", "isCorrect": False},
                        {"text": "Le Trait d'axe.", "isCorrect": False},
                        {"text": "Le Trait de lumière.", "isCorrect": False}
                    ],
                    "correction": "Le **Trait de rive** ou 'trait d'équerre' marque la dimension finale de la pièce."
                },
                {
                    "questionNumber": 38,
                    "question": "Que signifie la cotation **'Ø 8'** sur un plan de fabrication ?",
                    "answerOptions": [
                        {"text": "Une épaisseur de 8 mm.", "isCorrect": False},
                        {"text": "Un diamètre de 8 mm (souvent pour un perçage, un tourillon ou une vis).", "isCorrect": True},
                        {"text": "Une largeur de 8 mm.", "isCorrect": False},
                        {"text": "Un angle de 8 degrés.", "isCorrect": False}
                    ],
                    "correction": "Le symbole **Ø** (Phi) représente le diamètre."
                },
                {
                    "questionNumber": 39,
                    "question": "Qu'est-ce qu'une **Feuillure** en menuiserie ?",
                    "answerOptions": [
                        {"text": "Un défaut du bois.", "isCorrect": False},
                        {"text": "Une entaille (rainure) rectangulaire pratiquée sur le bord d'une pièce de bois pour recevoir un autre élément (ex : un panneau, un vitrage).", "isCorrect": True},
                        {"text": "Une vis.", "isCorrect": False},
                        {"text": "Un angle à 45°.", "isCorrect": False}
                    ],
                    "correction": "La **Feuillure** est essentielle dans la fabrication des portes et fenêtres pour l'assemblage du vitrage ou des panneaux."
                },
                {
                    "questionNumber": 40,
                    "question": "Dans le cas d'une **menuiserie intérieure** (porte ou meuble), quelle est la cote la plus importante pour la pose ?",
                    "answerOptions": [
                        {"text": "La largeur de la feuillure.", "isCorrect": False},
                        {"text": "La Cote de réservation (dimension de l'ouverture dans le mur ou la maçonnerie).", "isCorrect": True},
                        {"text": "La couleur du bois.", "isCorrect": False},
                        {"text": "Le prix.", "isCorrect": False}
                    ],
                    "correction": "La **cote de réservation** (dimensions brutes) doit être respectée pour que le dormant ou le meuble s'insère correctement, en prévoyant le jeu de pose nécessaire."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : USINAGE ET TECHNIQUES D'ASSEMBLAGE (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Usinage et Techniques d'Assemblage (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le rôle de la **Dégauchisseuse** ?",
                    "answerOptions": [
                        {"text": "Couper le bois en longueur.", "isCorrect": False},
                        {"text": "Rendre planes et d'équerre les faces de référence du bois massif.", "isCorrect": True},
                        {"text": "Réaliser des moulures.", "isCorrect": False},
                        {"text": "Percer des trous.", "isCorrect": False}
                    ],
                    "correction": "La **Dégauchisseuse** est la première machine utilisée pour préparer le bois, créant les deux faces de référence (FP et CP)."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est le rôle de la **Raboteuse** ?",
                    "answerOptions": [
                        {"text": "Rendre la pièce d'équerre.", "isCorrect": False},
                        {"text": "Amener les pièces de bois massives à l'épaisseur et à la largeur finale, en travaillant parallèlement à la face dégauchie.", "isCorrect": True},
                        {"text": "Couper les angles.", "isCorrect": False},
                        {"text": "Réaliser des rainures.", "isCorrect": False}
                    ],
                    "correction": "La **Raboteuse** permet d'obtenir le calibrage exact de la pièce, après le travail à la dégauchisseuse."
                },
                {
                    "questionNumber": 43,
                    "question": "Comment appelle-t-on l'assemblage où l'extrémité d'une pièce (le **tenon**) vient s'insérer dans un logement (la **mortaise**) de l'autre pièce ?",
                    "answerOptions": [
                        {"text": "L'Assemblage par tourillon.", "isCorrect": False},
                        {"text": "L'Assemblage à Tenon et Mortaise.", "isCorrect": True},
                        {"text": "L'Assemblage à queue d'aronde.", "isCorrect": False},
                        {"text": "L'Assemblage par plat-joint.", "isCorrect": False}
                    ],
                    "correction": "Le **Tenon-Mortaise** est l'assemblage traditionnel le plus solide, utilisé pour les cadres et les traverses."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle machine d'atelier est utilisée pour réaliser des moulures, des feuillures ou des rainures complexes ?",
                    "answerOptions": [
                        {"text": "La Scie à ruban.", "isCorrect": False},
                        {"text": "La Toupie (ou Toupillage).", "isCorrect": True},
                        {"text": "La Ponceuse à bande.", "isCorrect": False},
                        {"text": "La Perceuse à colonne.", "isCorrect": False}
                    ],
                    "correction": "La **Toupie** (ou la défonceuse manuelle) est l'outil pour les usinages de profilés. Elle nécessite une vigilance extrême en sécurité."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le principal danger du travail d'usinage **en contre-fil** ?",
                    "answerOptions": [
                        {"text": "Une coupe trop lente.", "isCorrect": False},
                        {"text": "L'arrachement des fibres du bois, produisant un défaut de surface (éclats).", "isCorrect": True},
                        {"text": "L'échauffement des outils.", "isCorrect": False},
                        {"text": "La perte de la pièce.", "isCorrect": False}
                    ],
                    "correction": "Le **Contre-fil** oblige à inverser l'orientation de la pièce ou à prendre de très faibles passes pour éviter l'arrachement."
                },
                {
                    "questionNumber": 46,
                    "question": "Qu'est-ce qu'une **Languette** (dans un assemblage) ?",
                    "answerOptions": [
                        {"text": "La partie saillante et mince d'une pièce qui vient s'insérer dans la rainure de la pièce opposée (assemblage Rainure et Languette).", "isCorrect": True},
                        {"text": "L'épaisseur de la pièce.", "isCorrect": False},
                        {"text": "Un défaut d'usinage.", "isCorrect": False},
                        {"text": "Une vis.", "isCorrect": False}
                    ],
                    "correction": "L'assemblage **Rainure et Languette** est couramment utilisé pour l'assemblage de panneaux (parquets, fonds de meubles)."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le rôle du **Presseur** sur une machine à bois (Toupie, Scie à format) ?",
                    "answerOptions": [
                        {"text": "Guider la pièce.", "isCorrect": False},
                        {"text": "Maintenir fermement la pièce de bois contre la table et le guide pendant l'usinage pour garantir la sécurité et la qualité de coupe.", "isCorrect": True},
                        {"text": "Lubrifier l'outil.", "isCorrect": False},
                        {"text": "Évacuer les copeaux.", "isCorrect": False}
                    ],
                    "correction": "Le **Presseur** (mécanique, pneumatique ou manuel) est un élément de sécurité et de précision essentiel."
                },
                {
                    "questionNumber": 48,
                    "question": "Comment appelle-t-on l'assemblage très résistant, souvent utilisé pour les tiroirs, qui ressemble à des dents entrelacées ?",
                    "answerOptions": [
                        {"text": "L'Assemblage à tenon.", "isCorrect": False},
                        {"text": "L'Assemblage à Queue d'Aronde.", "isCorrect": True},
                        {"text": "L'Assemblage par lamello.", "isCorrect": False},
                        {"text": "L'Assemblage à mi-bois.", "isCorrect": False}
                    ],
                    "correction": "La **Queue d'Aronde** est un assemblage mécanique auto-serrant, apprécié pour sa solidité et son esthétisme."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel est l'outil utilisé pour réaliser un assemblage de panneaux (plats-joints) à l'aide de chevilles en bois (lamelles compressées) ?",
                    "answerOptions": [
                        {"text": "La Fraise à tenon.", "isCorrect": False},
                        {"text": "La Lamelleuse (ou Lamello).", "isCorrect": True},
                        {"text": "La Dégauchisseuse.", "isCorrect": False},
                        {"text": "La Scie plongeante.", "isCorrect": False}
                    ],
                    "correction": "La **Lamelleuse** fraise une fente pour y insérer une lamelle (cheville en bois). L'eau de la colle fait gonfler la lamelle et assure un assemblage solide et aligné."
                },
                {
                    "questionNumber": 50,
                    "question": "Lors du sciage, à quoi sert le **Couteau diviseur** sur une scie circulaire ou à format ?",
                    "answerOptions": [
                        {"text": "Pousser le bois.", "isCorrect": False},
                        {"text": "Empêcher le bois de se refermer sur la lame après la coupe, réduisant le risque de rejet (ou 'kickback') et d'accident.", "isCorrect": True},
                        {"text": "Mesurer la coupe.", "isCorrect": False},
                        {"text": "Refroidir la lame.", "isCorrect": False}
                    ],
                    "correction": "Le **Couteau diviseur** est un élément de sécurité essentiel, mais doit être correctement réglé (lame)."
                },
                {
                    "questionNumber": 51,
                    "question": "Qu'est-ce qu'un **Tourillon** dans le domaine de l'assemblage ?",
                    "answerOptions": [
                        {"text": "Une vis spéciale.", "isCorrect": False},
                        {"text": "Une cheville cylindrique en bois, insérée dans deux perçages pour assembler deux pièces de bois (alternative courante au Tenon-Mortaise).", "isCorrect": True},
                        {"text": "Un défaut du bois.", "isCorrect": False},
                        {"text": "Une butée de coupe.", "isCorrect": False}
                    ],
                    "correction": "L'assemblage par **tourillon** est très rapide à réaliser (avec une perceuse et une chevilleuse)."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le rôle de la **Scie à format** ?",
                    "answerOptions": [
                        {"text": "Couper le bois massif.", "isCorrect": False},
                        {"text": "Découper des panneaux (Agglo, MDF, Contreplaqué) à la dimension exacte, avec des coupes précises et des angles parfaits (45°).", "isCorrect": True},
                        {"text": "Dégauchir le bois.", "isCorrect": False},
                        {"text": "Percer des trous.", "isCorrect": False}
                    ],
                    "correction": "La **Scie à format** (souvent avec inciseur) est la machine principale pour la découpe des panneaux."
                },
                {
                    "questionNumber": 53,
                    "question": "Comment appelle-t-on l'opération de creuser le logement d'une charnière ou d'une fiche pour qu'elle soit noyée dans le bois ?",
                    "answerOptions": [
                        {"text": "Le Perçage.", "isCorrect": False},
                        {"text": "Le Mortaisage (ou La Bédaneuse pour la mortaise de serrure).", "isCorrect": False},
                        {"text": "Le Défonçage (ou l'Encastrement).", "isCorrect": True},
                        {"text": "Le Ponçage.", "isCorrect": False}
                    ],
                    "correction": "L'**Encastrement** ou **Défonçage** de la quincaillerie est essentiel pour un bon fonctionnement (charnière)."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le rôle du **Serre-joint** dans le processus d'assemblage ?",
                    "answerOptions": [
                        {"text": "Maintenir la pièce en place avant la coupe.", "isCorrect": False},
                        {"text": "Maintenir les pièces assemblées sous pression pendant le temps de prise de la colle.", "isCorrect": True},
                        {"text": "Mesurer la longueur.", "isCorrect": False},
                        {"text": "Poncer le bois.", "isCorrect": False}
                    ],
                    "correction": "Le **Serrage** est une étape critique pour la solidité finale d'un collage."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel outil manuel est utilisé pour affiner le fond d'une mortaise ou parfaire un angle rentrant après un usinage machine ?",
                    "answerOptions": [
                        {"text": "La Plane.", "isCorrect": False},
                        {"text": "Le Ciseau à bois (ou Bédane).", "isCorrect": True},
                        {"text": "La Râpe.", "isCorrect": False},
                        {"text": "La Visseuse.", "isCorrect": False}
                    ],
                    "correction": "Le **Ciseau à bois** reste indispensable pour la finition manuelle des assemblages traditionnels."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment doit-on guider une pièce de bois lors de l'usinage à la **Toupie** pour des raisons de sécurité ?",
                    "answerOptions": [
                        {"text": "En tenant la pièce très lâchement.", "isCorrect": False},
                        {"text": "Toujours dans le sens inverse du sens de rotation de l'outil (sens opposé à la coupe).", "isCorrect": True},
                        {"text": "Toujours dans le sens de rotation de l'outil.", "isCorrect": False},
                        {"text": "Peu importe le sens.", "isCorrect": False}
                    ],
                    "correction": "Travailler en **contre-rotation** (sauf indication contraire pour certaines opérations) est la règle de sécurité de base pour éviter le rejet et garantir le contrôle de la pièce."
                },
                {
                    "questionNumber": 57,
                    "question": "Qu'est-ce qu'une **Rainure** ?",
                    "answerOptions": [
                        {"text": "Un trou carré.", "isCorrect": False},
                        {"text": "Une entaille longitudinale de section rectangulaire réalisée sur le chant d'une pièce de bois (pour recevoir un panneau, un fond de meuble, ou une languette).", "isCorrect": True},
                        {"text": "Une coupe en angle.", "isCorrect": False},
                        {"text": "Une moulure ronde.", "isCorrect": False}
                    ],
                    "correction": "La **Rainure** est courante en agencement (pour les fonds de tiroirs ou les panneaux de portes)."
                },
                {
                    "questionNumber": 58,
                    "question": "Quel est le risque principal lors de l'utilisation d'une **Défonceuse manuelle** ?",
                    "answerOptions": [
                        {"text": "Un défaut de collage.", "isCorrect": False},
                        {"text": "Le rejet de la machine (à cause du sens de coupe ou de la vitesse d'avance) et la coupure des doigts.", "isCorrect": True},
                        {"text": "La déformation du bois.", "isCorrect": False},
                        {"text": "Le manque de précision.", "isCorrect": False}
                    ],
                    "correction": "La **Défonceuse** est puissante et exige une excellente prise en main et des guides solides (gabarit)."
                },
                {
                    "questionNumber": 59,
                    "question": "Comment s'appelle l'assemblage réalisé en coupant les deux pièces à 45° pour former un angle de 90° (souvent pour les cadres ou moulures) ?",
                    "answerOptions": [
                        {"text": "L'Assemblage à Tenon-Mortaise.", "isCorrect": False},
                        {"text": "L'Assemblage à Onglet (ou à coupe d'onglet).", "isCorrect": True},
                        {"text": "L'Assemblage par tourillon.", "isCorrect": False},
                        {"text": "L'Assemblage à plat-joint.", "isCorrect": False}
                    ],
                    "correction": "L'**Onglet** (ou coupe à 45°) est privilégié pour son esthétisme, mais il est moins résistant mécaniquement qu'un Tenon-Mortaise."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le rôle du **Contre-profil** sur une menuiserie (porte, fenêtre) ?",
                    "answerOptions": [
                        {"text": "Rendre la pièce plus lourde.", "isCorrect": False},
                        {"text": "Assurer la continuité du profil et de la moulure sur les traverses de l'assemblage (Tenon-Mortaise à Contre-profil).", "isCorrect": True},
                        {"text": "Protéger la pièce contre le feu.", "isCorrect": False},
                        {"text": "Éviter le collage.", "isCorrect": False}
                    ],
                    "correction": "Le **Contre-profil** permet un assemblage invisible et esthétique entre les montants et les traverses des cadres."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : FABRICATION DE MENUISERIE ET AGENCEMENT (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Fabrication de Menuiserie et Agencement (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Dans une fenêtre ou une porte, comment appelle-t-on le cadre fixe qui est scellé dans la maçonnerie ?",
                    "answerOptions": [
                        {"text": "Le Dormant (ou Châssis fixe).", "isCorrect": True},
                        {"text": "L'Ouvrant (ou Vantail).", "isCorrect": False},
                        {"text": "Le Linteau.", "isCorrect": False},
                        {"text": "Le Joint de calfeutrement.", "isCorrect": False}
                    ],
                    "correction": "Le **Dormant** (ou Bâti) est la partie de la menuiserie fixée au mur."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le rôle du **Jet d'eau** sur la traverse basse d'un ouvrant de fenêtre ?",
                    "answerOptions": [
                        {"text": "Ralentir l'ouverture.", "isCorrect": False},
                        {"text": "Faciliter l'évacuation des eaux de ruissellement vers l'extérieur pour éviter l'infiltration sous le dormant.", "isCorrect": True},
                        {"text": "Servir de poignée.", "isCorrect": False},
                        {"text": "Tenir le vitrage.", "isCorrect": False}
                    ],
                    "correction": "Le **Jet d'eau** est un élément de protection contre l'humidité, souvent associé à une bavette métallique ou un rejingot."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on la pièce de quincaillerie qui permet de régler la position et l'aplomb d'une porte après la pose ?",
                    "answerOptions": [
                        {"text": "La Cale.", "isCorrect": False},
                        {"text": "La Fiche à lacets (ou charnière réglable).", "isCorrect": True},
                        {"text": "Le Verrou.", "isCorrect": False},
                        {"text": "La Crémone.", "isCorrect": False}
                    ],
                    "correction": "La **Fiche réglable** ou paumelle réglable permet d'ajuster le jeu entre la porte et le dormant."
                },
                {
                    "questionNumber": 64,
                    "question": "Dans la fabrication d'un caisson d'agencement, quel assemblage est le plus rapide et le plus courant pour lier les montants et les traverses ?",
                    "answerOptions": [
                        {"text": "Tenon-Mortaise.", "isCorrect": False},
                        {"text": "Vis et Tourillon (ou Quincaillerie d'assemblage invisible : ex: Rastex, Excentrique).", "isCorrect": True},
                        {"text": "Queue d'aronde.", "isCorrect": False},
                        {"text": "Assemblage à mi-bois.", "isCorrect": False}
                    ],
                    "correction": "L'assemblage par **tourillon et quincaillerie** est privilégié en série pour sa rapidité et son aspect démontable."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le rôle des **Calages de vitrage** (petites cales en plastique ou en bois) ?",
                    "answerOptions": [
                        {"text": "Empêcher le verre de bouger.", "isCorrect": False},
                        {"text": "Assurer le jeu nécessaire et le positionnement du vitrage, notamment en supportant son poids pour éviter la déformation de l'ouvrant (calage en L).", "isCorrect": True},
                        {"text": "Rendre la fenêtre décorative.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité.", "isCorrect": False}
                    ],
                    "correction": "Le **Calage** est essentiel pour la bonne tenue et la durabilité du vitrage, en particulier les doubles et triples vitrages lourds."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on le profil qui maintient le panneau ou le vitrage dans la feuillure et assure l'étanchéité intérieure ?",
                    "answerOptions": [
                        {"text": "La Traverse.", "isCorrect": False},
                        {"text": "Le Parclose.", "isCorrect": True},
                        {"text": "Le Dormant.", "isCorrect": False},
                        {"text": "Le Linteau.", "isCorrect": False}
                    ],
                    "correction": "La **Parclose** (souvent amovible) est posée après la mise en place du vitrage/panneau et des joints d'étanchéité."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est l'objectif d'une **Dégondeuse** ?",
                    "answerOptions": [
                        {"text": "Fixer les gonds.", "isCorrect": False},
                        {"text": "Permettre le retrait facile des ouvrants (portes ou fenêtres) de leurs gonds ou fiches, notamment pour la pose finale ou la maintenance.", "isCorrect": True},
                        {"text": "Régler l'aplomb.", "isCorrect": False},
                        {"text": "Lubrifier les charnières.", "isCorrect": False}
                    ],
                    "correction": "La **Dégondeuse** (petit levier) facilite le démontage des portes non réglables."
                },
                {
                    "questionNumber": 68,
                    "question": "Dans un meuble, quel est le rôle du **Dos** (panneau arrière) ?",
                    "answerOptions": [
                        {"text": "Servir de décoration.", "isCorrect": False},
                        {"text": "Assurer la rigidité et l'équerrage du caisson (contreventement) et cacher le mur.", "isCorrect": True},
                        {"text": "Servir de poignée.", "isCorrect": False},
                        {"text": "Être la façade du meuble.", "isCorrect": False}
                    ],
                    "correction": "Le **Dos** (souvent en panneau mince) est un élément structurel crucial pour la stabilité du meuble."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel terme désigne la menuiserie posée **en applique** ?",
                    "answerOptions": [
                        {"text": "La pose d'une fenêtre à l'intérieur du tableau du mur (tunnel).", "isCorrect": False},
                        {"text": "La pose où le dormant recouvre partiellement la maçonnerie (souvent à l'intérieur, pour pouvoir ajouter un isolant).", "isCorrect": True},
                        {"text": "La pose uniquement pour l'extérieur.", "isCorrect": False},
                        {"text": "La pose sans vis.", "isCorrect": False}
                    ],
                    "correction": "La pose **en applique** est courante dans les constructions neuves avec Isolation Thermique par l'Intérieur (ITI)."
                },
                {
                    "questionNumber": 70,
                    "question": "Quelle est la principale fonction de la **Crémone** (ou Verrouillage Multipoints) sur une porte ou fenêtre moderne ?",
                    "answerOptions": [
                        {"text": "Lier les montants et traverses.", "isCorrect": False},
                        {"text": "Assurer la fermeture et la sécurité sur plusieurs points le long du dormant (meilleure étanchéité et sécurité anti-effraction).", "isCorrect": True},
                        {"text": "Décorer la menuiserie.", "isCorrect": False},
                        {"text": "Faciliter le ponçage.", "isCorrect": False}
                    ],
                    "correction": "La **Crémone** améliore les performances de la menuiserie (étanchéité air/eau et résistance mécanique)."
                },
                {
                    "questionNumber": 71,
                    "question": "Qu'est-ce qu'un panneau de porte ou de meuble dit **'à âme pleine'** ?",
                    "answerOptions": [
                        {"text": "Un panneau très léger.", "isCorrect": False},
                        {"text": "Un panneau dont l'intérieur est entièrement rempli de matériau (bois massif reconstitué, aggloméré) par opposition à l'âme alvéolaire (nid d'abeille).", "isCorrect": True},
                        {"text": "Un panneau de verre.", "isCorrect": False},
                        {"text": "Un panneau de couleur vive.", "isCorrect": False}
                    ],
                    "correction": "La porte **à âme pleine** est plus lourde, plus isolante (phonique et thermique) et plus résistante que la porte à âme alvéolaire."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est l'outil utilisé pour réaliser les mortaises pour les serrures (logement du boîtier et de la têtière) ?",
                    "answerOptions": [
                        {"text": "La Perceuse visseuse.", "isCorrect": False},
                        {"text": "La Mortaiseuse (ou la Bédaneuse ou à l'aide de la défonceuse).", "isCorrect": True},
                        {"text": "La Scie sauteuse.", "isCorrect": False},
                        {"text": "Le Trusquin.", "isCorrect": False}
                    ],
                    "correction": "La **Mortaiseuse** permet de creuser précisément le logement rectangulaire de la serrure dans l'épaisseur du montant."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la fonction d'un **joint de frappe** ou d'un **joint périphérique** sur l'ouvrant d'une fenêtre ?",
                    "answerOptions": [
                        {"text": "Empêcher le bois de se fissurer.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité à l'air et à l'eau lorsque l'ouvrant est fermé sur le dormant.", "isCorrect": True},
                        {"text": "Faire tenir la quincaillerie.", "isCorrect": False},
                        {"text": "Décorer la fenêtre.", "isCorrect": False}
                    ],
                    "correction": "Les **joints** (en EPDM, silicone, etc.) sont fondamentaux pour les performances thermiques de la menuiserie."
                },
                {
                    "questionNumber": 74,
                    "question": "Lors de la pose d'un meuble, quel est l'outil indispensable pour s'assurer que l'ouvrage est de niveau et d'aplomb ?",
                    "answerOptions": [
                        {"text": "Le Mètre ruban.", "isCorrect": False},
                        {"text": "Le Niveau à bulle (ou Niveau laser) et le Fil à plomb.", "isCorrect": True},
                        {"text": "Le Serre-joint.", "isCorrect": False},
                        {"text": "La Règle.", "isCorrect": False}
                    ],
                    "correction": "Le **Niveau** garantit l'horizontalité. L'**Aplomb** garantit la verticalité, essentiels pour le bon fonctionnement des tiroirs et portes."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel type de fixation est privilégié pour fixer un meuble haut de cuisine au mur ?",
                    "answerOptions": [
                        {"text": "Un simple clou.", "isCorrect": False},
                        {"text": "Les Suspentes (ou Attaches) réglables pour charges lourdes (avec chevilles adaptées au mur).", "isCorrect": True},
                        {"text": "De la colle simple.", "isCorrect": False},
                        {"text": "Du ruban adhésif.", "isCorrect": False}
                    ],
                    "correction": "Les **suspentes réglables** permettent l'ajustement final du meuble et doivent supporter des charges très importantes (vaisselle, etc.)."
                },
                {
                    "questionNumber": 76,
                    "question": "Qu'est-ce qu'une **Traverse** dans un cadre de porte ou de fenêtre ?",
                    "answerOptions": [
                        {"text": "La pièce verticale.", "isCorrect": False},
                        {"text": "La pièce horizontale qui relie les deux montants (ex : traverse haute, traverse basse).", "isCorrect": True},
                        {"text": "Le verre.", "isCorrect": False},
                        {"text": "Le joint.", "isCorrect": False}
                    ],
                    "correction": "Les **Montants** sont verticaux, les **Traverses** sont horizontales."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le rôle du **Rejingot** dans une fenêtre ?",
                    "answerOptions": [
                        {"text": "Servir de poignée.", "isCorrect": False},
                        {"text": "Élément moulé sur l'appui de fenêtre maçonné qui empêche l'eau de pénétrer et assure l'étanchéité sous le dormant.", "isCorrect": True},
                        {"text": "Protéger le verre.", "isCorrect": False},
                        {"text": "Faire la jonction entre l'ouvrant et le dormant.", "isCorrect": False}
                    ],
                    "correction": "Le **Rejingot** (souvent maçonné ou intégré au seuil) est essentiel pour l'évacuation des eaux de pluie."
                },
                {
                    "questionNumber": 78,
                    "question": "Comment appelle-t-on le procédé qui permet de masquer le jeu entre le dormant de la menuiserie et la maçonnerie après la pose ?",
                    "answerOptions": [
                        {"text": "Le Défonçage.", "isCorrect": False},
                        {"text": "La Pose des Couvre-joints (ou des Moulures de finition).", "isCorrect": True},
                        {"text": "Le Calage.", "isCorrect": False},
                        {"text": "Le Ferraillage.", "isCorrect": False}
                    ],
                    "correction": "Les **Couvre-joints** assurent la finition esthétique intérieure."
                },
                {
                    "questionNumber": 79,
                    "question": "Dans le cas d'un plan de travail de cuisine, quel type de bois composite est le plus résistant à l'humidité et à l'abrasion ?",
                    "answerOptions": [
                        {"text": "Le Bois massif brut.", "isCorrect": False},
                        {"text": "Le Stratifié (panneau recouvert d'une feuille épaisse et dure de résine).", "isCorrect": True},
                        {"text": "Le Panneau de particules.", "isCorrect": False},
                        {"text": "Le MDF standard.", "isCorrect": False}
                    ],
                    "correction": "Le **Stratifié** est le standard pour les plans de travail grâce à sa résistance et sa facilité de nettoyage."
                },
                {
                    "questionNumber": 80,
                    "question": "Quel est le risque de fixer l'ouvrant d'une fenêtre avant d'avoir vérifié l'équerrage du dormant et son niveau ?",
                    "answerOptions": [
                        {"text": "La perte de temps.", "isCorrect": False},
                        {"text": "L'ouvrant ne fermera pas correctement (frottement, joint non compressé, dérèglement) ou la fenêtre ne sera pas étanche.", "isCorrect": True},
                        {"text": "La rupture du verre.", "isCorrect": False},
                        {"text": "La déformation du mur.", "isCorrect": False}
                    ],
                    "correction": "Le **Dormant** doit être parfaitement de niveau, d'aplomb et d'équerre avant de recevoir l'ouvrant."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : SÉCURITÉ, HYGIÈNE ET FINITIONS (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Sécurité, Hygiène et Finitions (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) essentiel lors de l'utilisation de machines bruyantes (Toupie, Raboteuse, Scie) ?",
                    "answerOptions": [
                        {"text": "Les Gants en cuir.", "isCorrect": False},
                        {"text": "Les Protections auditives (casque ou bouchons anti-bruit).", "isCorrect": True},
                        {"text": "Le Masque FFP3.", "isCorrect": False},
                        {"text": "Le Gilet de sécurité.", "isCorrect": False}
                    ],
                    "correction": "Le bruit excessif peut entraîner une **surdité** irréversible. La protection auditive est obligatoire au-delà de 85 dB."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le risque principal lors de l'usinage du bois (sciage, ponçage) et des panneaux dérivés (MDF, Agglo) ?",
                    "answerOptions": [
                        {"text": "Les produits chimiques.", "isCorrect": False},
                        {"text": "L'inhalation de poussières fines de bois (cancérogènes ou irritantes) et de colles (Formaldéhyde).", "isCorrect": True},
                        {"text": "La chute d'objet.", "isCorrect": False},
                        {"text": "Le glissement.", "isCorrect": False}
                    ],
                    "correction": "L'**aspiration** centralisée et le port du **Masque FFP3** sont obligatoires contre les poussières."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est l'outil obligatoire pour guider et pousser les petites pièces de bois sur une machine (Toupie, Dégauchisseuse) ?",
                    "answerOptions": [
                        {"text": "La main.", "isCorrect": False},
                        {"text": "Le Poussoir.", "isCorrect": True},
                        {"text": "Le Gant.", "isCorrect": False},
                        {"text": "Le Serre-joint.", "isCorrect": False}
                    ],
                    "correction": "Le **Poussoir** (ou la pousse-main) permet de garder les mains éloignées de la zone de coupe (lame ou fer) et d'assurer une poussée régulière."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le risque lié au port de **gants** lors de l'utilisation d'une machine tournante (Toupie, Perceuse à colonne) ?",
                    "answerOptions": [
                        {"text": "La coupure.", "isCorrect": False},
                        {"text": "L'entraînement du gant par l'outil, provoquant l'amputation ou l'écrasement de la main.", "isCorrect": True},
                        {"text": "L'allergie.", "isCorrect": False},
                        {"text": "Le glissement de la pièce.", "isCorrect": False}
                    ],
                    "correction": "Le port de gants est **interdit** sur les machines tournantes (sauf cas spécifiques, après analyse de risque) !"
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le rôle du **Micro-réglage** sur une machine (ex : guide de Toupie, lame de Scie à format) ?",
                    "answerOptions": [
                        {"text": "Le déplacement rapide.", "isCorrect": False},
                        {"text": "Permettre un ajustement fin et précis de la position de l'outil ou du guide (au 1/10e de mm) pour garantir l'exactitude des usinages.", "isCorrect": True},
                        {"text": "Le nettoyage.", "isCorrect": False},
                        {"text": "L'arrêt d'urgence.", "isCorrect": False}
                    ],
                    "correction": "La précision est la base du métier. Le **Micro-réglage** assure cette précision."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le danger d'utiliser des **solvants** (nettoyants, diluants) dans un local mal ventilé ?",
                    "answerOptions": [
                        {"text": "Une mauvaise coupe.", "isCorrect": False},
                        {"text": "Intoxication par inhalation, risque d'incendie/explosion et irritation des voies respiratoires.", "isCorrect": True},
                        {"text": "Une chute.", "isCorrect": False},
                        {"text": "La rouille.", "isCorrect": False}
                    ],
                    "correction": "Les **solvants** doivent être utilisés avec une ventilation adéquate (hotte aspirante) et le port d'un masque à cartouche adapté."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment appelle-t-on le type de ponçage qui vise à rendre le bois rugueux avant l'application d'un vernis ou d'une laque ?",
                    "answerOptions": [
                        {"text": "Le Ponçage de finition.", "isCorrect": False},
                        {"text": "L'Égrenage (avec un grain fin, typiquement P220 ou supérieur).", "isCorrect": True},
                        {"text": "Le Décapage.", "isCorrect": False},
                        {"text": "Le Ponçage grossier.", "isCorrect": False}
                    ],
                    "correction": "L'**Égrenage** entre deux couches de finition est indispensable pour assurer l'accroche de la couche suivante et supprimer les fibres relevées par la première application."
                },
                {
                    "questionNumber": 88,
                    "question": "Que doit-on vérifier en priorité sur une machine avant de commencer un usinage ?",
                    "answerOptions": [
                        {"text": "Sa couleur.", "isCorrect": False},
                        {"text": "Le bon réglage des protecteurs, des guides, le serrage de l'outil (lame/fraise) et l'aspiration.", "isCorrect": True},
                        {"text": "Son âge.", "isCorrect": False},
                        {"text": "Le stock de bois.", "isCorrect": False}
                    ],
                    "correction": "Les **réglages et la sécurité** sont primordiaux. Une lame mal serrée est un danger de mort."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la règle d'or concernant le travail en hauteur sur une échelle (pose d'agencement, fenêtres) ?",
                    "answerOptions": [
                        {"text": "Monter le plus haut possible.", "isCorrect": False},
                        {"text": "L'échelle est un moyen d'accès temporaire ; le travail doit se faire sur un échafaudage ou une plateforme stable si le travail est long ou répétitif.", "isCorrect": True},
                        {"text": "Ne jamais attacher l'échelle.", "isCorrect": False},
                        {"text": "Travailler les mains chargées.", "isCorrect": False}
                    ],
                    "correction": "L'**échelle** doit être sécurisée (amarrée) et son utilisation limitée. Privilégier les solutions collectives (échafaudage)."
                },
                {
                    "questionNumber": 90,
                    "question": "Comment appelle-t-on le procédé qui consiste à appliquer un produit (ex : cire ou huile) qui pénètre le bois sans former de couche en surface (aspect très naturel) ?",
                    "answerOptions": [
                        {"text": "Le Vernissage.", "isCorrect": False},
                        {"text": "L'Imprégnation (ou Finition par Huile, Cire, etc.).", "isCorrect": True},
                        {"text": "Le Décapage.", "isCorrect": False},
                        {"text": "Le Laquage.", "isCorrect": False}
                    ],
                    "correction": "La finition par **imprégnation** est souvent utilisée pour les parquets, les plans de travail ou les meubles haut de gamme."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est le risque lié à un sol d'atelier encombré de chutes de bois ou de copeaux ?",
                    "answerOptions": [
                        {"text": "Le défaut de coupe.", "isCorrect": False},
                        {"text": "Le risque de chute, de glissade (sur les copeaux lisses) et d'incendie (combustible).", "isCorrect": True},
                        {"text": "Le bruit.", "isCorrect": False},
                        {"text": "L'usure des outils.", "isCorrect": False}
                    ],
                    "correction": "Le **nettoyage régulier** de l'atelier est une règle de sécurité et d'hygiène fondamentale (incendie, TMS)."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le danger d'utiliser un **compresseur d'air** pour se dépoussiérer ?",
                    "answerOptions": [
                        {"text": "La salissure.", "isCorrect": False},
                        {"text": "Le risque de projection de corps étranger dans les yeux et le risque d'embolie gazeuse (en cas de contact direct sur la peau).", "isCorrect": True},
                        {"text": "Le bruit.", "isCorrect": False},
                        {"text": "Le froid.", "isCorrect": False}
                    ],
                    "correction": "L'air comprimé est dangereux. Utiliser plutôt un aspirateur ou une balayette pour le nettoyage des vêtements et des mains."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est l'objectif du **Décapage** d'une vieille menuiserie ?",
                    "answerOptions": [
                        {"text": "L'appliquer d'une nouvelle finition.", "isCorrect": False},
                        {"text": "Retirer les anciennes couches de finition (peinture, vernis) avant l'application d'un nouveau traitement ou une réparation (ponçage ou produit chimique).", "isCorrect": True},
                        {"text": "La rendre plus solide.", "isCorrect": False},
                        {"text": "La faire sécher.", "isCorrect": False}
                    ],
                    "correction": "Le **Décapage** permet d'accéder au bois brut pour une rénovation complète."
                },
                {
                    "questionNumber": 94,
                    "question": "Que signifie le sigle **DUERP** pour une entreprise de menuiserie ?",
                    "answerOptions": [
                        {"text": "Dossier Unique d'Étude et de Réalisation de Projets.", "isCorrect": False},
                        {"text": "Document Unique d'Évaluation des Risques Professionnels (inventaire des risques et mesures de prévention de l'entreprise).", "isCorrect": True},
                        {"text": "Déclaration d'Urgence des Éléments de Rénovation et de Pose.", "isCorrect": False},
                        {"text": "Détail Unifié des Essences et des Revêtements de Panneaux.", "isCorrect": False}
                    ],
                    "correction": "Le **DUERP** est un document légal et obligatoire pour toute entreprise ayant au moins un salarié."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la principale fonction du **Laquage** (peinture de finition) ?",
                    "answerOptions": [
                        {"text": "Laisser la couleur du bois apparente.", "isCorrect": False},
                        {"text": "Former un film opaque, lisse et très dur en surface, masquant le veinage (aspect haut de gamme).", "isCorrect": True},
                        {"text": "Pénétrer le bois en profondeur.", "isCorrect": False},
                        {"text": "Servir uniquement d'antiseptique.", "isCorrect": False}
                    ],
                    "correction": "Le **Laquage** (souvent polyuréthane) est la finition la plus exigeante en préparation (ponçage fin)."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est le risque en cas d'utilisation d'une lame de scie **mal affûtée** ?",
                    "answerOptions": [
                        {"text": "Une coupe plus rapide.", "isCorrect": False},
                        {"text": "Un échauffement de la lame, un effort excessif, un bruit important, une mauvaise qualité de coupe (brûlure, éclatement) et un risque de rejet.", "isCorrect": True},
                        {"text": "Une meilleure finition.", "isCorrect": False},
                        {"text": "L'usure de l'aspiration.", "isCorrect": False}
                    ],
                    "correction": "Une **lame affûtée** est un gage de sécurité et de qualité."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque en cas de contact du bois avec du **métal ferreux** (clous, vis non galvanisées) avant la finition (sur Chêne ou Châtaignier) ?",
                    "answerOptions": [
                        {"text": "Le bois prend feu.", "isCorrect": False},
                        {"text": "Une réaction chimique (oxydation des tanins) entraînant l'apparition de tâches noires sur le bois (rouille).", "isCorrect": True},
                        {"text": "Le bois se déforme.", "isCorrect": False},
                        {"text": "Le bois devient plus dur.", "isCorrect": False}
                    ],
                    "correction": "Certaines essences (tanniques) doivent être en contact avec de l'acier inoxydable ou galvanisé pour éviter ces taches."
                },
                {
                    "questionNumber": 98,
                    "question": "Comment doit être la pièce de bois (dégauchie/rabotée) avant d'être usinée à la **Toupie** pour des raisons de sécurité ?",
                    "answerOptions": [
                        {"text": "Elle doit être poncée.", "isCorrect": False},
                        {"text": "Elle doit avoir au moins une face de référence plane et dressée, bien dégauchie pour un appui stable sur la table.", "isCorrect": True},
                        {"text": "Elle doit être mouillée.", "isCorrect": False},
                        {"text": "Elle doit être très courte.", "isCorrect": False}
                    ],
                    "correction": "Le travail à la **Toupie** sur des pièces brutes ou gauches est extrêmement dangereux et conduit à des rejets."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le rôle du **Primaire (ou Sous-couche)** dans le processus de finition (peinture ou vernis) ?",
                    "answerOptions": [
                        {"text": "Rendre la finition plus foncée.", "isCorrect": False},
                        {"text": "Bloquer les fonds, uniformiser l'absorption du bois et assurer une meilleure adhérence de la couche de finition (évite la surconsommation).", "isCorrect": True},
                        {"text": "Sécher rapidement.", "isCorrect": False},
                        {"text": "Protéger contre le feu.", "isCorrect": False}
                    ],
                    "correction": "La **Sous-couche** est essentielle pour la qualité, la durabilité et l'uniformité de la finition."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est l'attitude à adopter face à une **panne de machine** (ex : bruit anormal) en cours d'usinage ?",
                    "answerOptions": [
                        {"text": "Continuer de travailler.", "isCorrect": False},
                        {"text": "Couper immédiatement l'alimentation électrique (bouton d'arrêt d'urgence ou disjoncteur) et signaler l'anomalie.", "isCorrect": True},
                        {"text": "Tenter de la réparer soi-même sans couper le courant.", "isCorrect": False},
                        {"text": "Demander l'avis d'un collègue.", "isCorrect": False}
                    ],
                    "correction": "L'**Arrêt d'Urgence** est la première réaction en cas d'incident. La maintenance doit se faire machine à l'arrêt et consignée (hors tension)."
                },
            ]
        }
    }
}

# Exemple d'accès aux données :
# print(quiz_data["title"])
# print(quiz_data["themes"][3]["name"])
# print(quiz_data["themes"][3]["questions"][4]["question"])
# print(quiz_data["themes"][3]["questions"][4]["answerOptions"][2]["isCorrect"])