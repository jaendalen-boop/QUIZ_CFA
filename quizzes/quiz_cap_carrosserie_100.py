# Fichier : quiz_cap_carrosserie_100.py

quiz_data = {
    "title": "Quiz CAP Réparation des Carrosseries : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE, SÉCURITÉ, OUTILS ET ENVIRONNEMENT (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Hygiène, Sécurité, Outils et Environnement (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) absolument indispensable lors des opérations de ponçage du mastic ou de l'apprêt ?",
                    "answerOptions": [
                        {"text": "Des bottes de sécurité.", "isCorrect": False},
                        {"text": "Un Masque respiratoire (P3) et des lunettes de protection (contre la poussière et les particules de ponçage).", "isCorrect": True},
                        {"text": "Des gants en tissu.", "isCorrect": False},
                        {"text": "Un casque anti-bruit.", "isCorrect": False}
                    ],
                    "correction": "Le **masque P3** protège des poussières fines de ponçage très nocives."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le risque principal lié à l'utilisation des produits de peinture (solvants, bases, vernis) en cabine ou à l'air libre ?",
                    "answerOptions": [
                        {"text": "Un risque de coupure.", "isCorrect": False},
                        {"text": "Un risque d'intoxication (inhalation de COV), d'inflammation et d'incendie (produits très inflammables).", "isCorrect": True},
                        {"text": "Un risque de choc électrique.", "isCorrect": False},
                        {"text": "Un risque de chute.", "isCorrect": False}
                    ],
                    "correction": "Une **ventilation** et une **filtration** forcées sont obligatoires lors de la pulvérisation de peinture."
                },
                {
                    "questionNumber": 3,
                    "question": "Que signifie le pictogramme de sécurité GHS représentant une **tête de mort sur un os** ?",
                    "answerOptions": [
                        {"text": "Produit comburant.", "isCorrect": False},
                        {"text": "Produit toxique et mortel (à très faible dose par ingestion, inhalation ou contact cutané).", "isCorrect": True},
                        {"text": "Produit inflammable.", "isCorrect": False},
                        {"text": "Produit corrosif.", "isCorrect": False}
                    ],
                    "correction": "Ce pictogramme indique un **danger très grave** nécessitant des précautions extrêmes."
                },
                {
                    "questionNumber": 4,
                    "question": "Comment doit-on éliminer les **chiffons souillés par les solvants et diluants** après dégraissage ?",
                    "answerOptions": [
                        {"text": "Les jeter à la poubelle normale.", "isCorrect": False},
                        {"text": "Les placer dans un contenant métallique hermétique dédié aux déchets dangereux (Risque d'auto-inflammation).", "isCorrect": True},
                        {"text": "Les brûler à l'air libre.", "isCorrect": False},
                        {"text": "Les rincer à l'eau.", "isCorrect": False}
                    ],
                    "correction": "Certains solvants peuvent s'enflammer spontanément (**auto-inflammation**) au contact de l'air."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel est l'outil de mesurage utilisé pour vérifier l'alignement des points de référence (châssis) sur le marbre (outil de redressage) ?",
                    "answerOptions": [
                        {"text": "Le pied à coulisse.", "isCorrect": False},
                        {"text": "Le Mètre ruban, l'Équerre, et le Système de mesurage électronique ou laser (pour le contrôle géométrique).", "isCorrect": True},
                        {"text": "La brosse métallique.", "isCorrect": False},
                        {"text": "Le pistolet à peinture.", "isCorrect": False}
                    ],
                    "correction": "Le **contrôle géométrique** sur marbre est essentiel après un choc important."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle doit être la procédure de sécurité lors du **soudage (MIG/MAG)** ?",
                    "answerOptions": [
                        {"text": "Porter un t-shirt et des lunettes de soleil.", "isCorrect": False},
                        {"text": "Porter un masque/casque de soudage avec filtre auto-obscurcissant, des gants en cuir, des vêtements ignifugés et travailler dans une zone ventilée.", "isCorrect": True},
                        {"text": "Travailler sans ventilation.", "isCorrect": False},
                        {"text": "Utiliser un extincteur à eau.", "isCorrect": False}
                    ],
                    "correction": "Le **casque de soudage** protège des UV, des IR et des projections."
                },
                {
                    "questionNumber": 7,
                    "question": "Quel est le risque de travailler sur un véhicule **électrique ou hybride** sans avoir préalablement déconnecté la batterie de service et le circuit haute tension ?",
                    "answerOptions": [
                        {"text": "Le véhicule démarre tout seul.", "isCorrect": False},
                        {"text": "Un risque de choc électrique grave (électrocution) dû à la haute tension (jusqu'à 600 V) du circuit de traction.", "isCorrect": True},
                        {"text": "Le véhicule s'enflamme.", "isCorrect": False},
                        {"text": "La tôle rouille.", "isCorrect": False}
                    ],
                    "correction": "La **sécurité électrique** (consignation) est une procédure spécifique et obligatoire pour ces véhicules."
                },
                {
                    "questionNumber": 8,
                    "question": "Qu'est-ce qu'une **Fiche de Données de Sécurité (FDS)** ?",
                    "answerOptions": [
                        {"text": "Un catalogue de pièces détachées.", "isCorrect": False},
                        {"text": "Un document légal fournissant des informations détaillées sur les dangers d'un produit chimique, son stockage, sa manipulation et les mesures d'urgence.", "isCorrect": True},
                        {"text": "Un document de commande.", "isCorrect": False},
                        {"text": "Un document de suivi client.", "isCorrect": False}
                    ],
                    "correction": "La **FDS** doit être consultée avant toute utilisation d'un produit inconnu."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est l'outil utilisé pour redresser (débosseler) une tôle par l'extérieur en tirant le métal grâce à des pointes de soudure ?",
                    "answerOptions": [
                        {"text": "La lime de carrossier.", "isCorrect": False},
                        {"text": "Le Tire-Clou (ou Spotter).", "isCorrect": True},
                        {"text": "Le marteau à planer.", "isCorrect": False},
                        {"text": "Le pistolet à colle.", "isCorrect": False}
                    ],
                    "correction": "Le **Tire-Clou** est essentiel pour le débosselage sans démontage lourd."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le risque de poncer ou souder un élément peint avec une ancienne peinture au plomb (sur les vieux véhicules) ?",
                    "answerOptions": [
                        {"text": "La peinture coule.", "isCorrect": False},
                        {"text": "Inhalation de fumées ou de poussières toxiques (le plomb est un poison).", "isCorrect": True},
                        {"text": "Le métal se déforme.", "isCorrect": False},
                        {"text": "Le vernis jaunit.", "isCorrect": False}
                    ],
                    "correction": "Le **Plomb** et ses oxydes sont des poisons lourds et nécessitent des procédures de travail spécifiques et un EPI adapté."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est l'importance du **dégraissage** d'une tôle avant l'application du mastic ?",
                    "answerOptions": [
                        {"text": "Le rendre plus lisse.", "isCorrect": False},
                        {"text": "Éliminer les traces de graisse, silicone, ou d'huile qui empêchent l'adhérence (accroche) du mastic, créant un décollement ou des bulles.", "isCorrect": True},
                        {"text": "Le rendre plus rugueux.", "isCorrect": False},
                        {"text": "Le colorer.", "isCorrect": False}
                    ],
                    "correction": "Le **dégraissage** à l'aide d'un dégraissant spécifique est une étape fondamentale."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la cause principale d'une **mauvaise polymérisation** (durcissement) du vernis bi-composant ?",
                    "answerOptions": [
                        {"text": "Une température ambiante trop élevée.", "isCorrect": False},
                        {"text": "Un mauvais dosage du durcisseur (catalyseur) ou une température de cabine trop basse/trop haute par rapport au durcisseur utilisé.", "isCorrect": True},
                        {"text": "Un support mal dégraissé.", "isCorrect": False},
                        {"text": "Une épaisseur de vernis trop faible.", "isCorrect": False}
                    ],
                    "correction": "Le dosage du **durcisseur** est une opération de précision (souvent 2:1 ou 3:1) et doit respecter la FDS."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est l'outil utilisé pour le **planage** après débosselage (pour s'assurer que la tôle est parfaitement lisse) ?",
                    "answerOptions": [
                        {"text": "Le marteau rivoir.", "isCorrect": False},
                        {"text": "La Lime de carrossier (ou râpe) avec un support flexible, utilisée pour révéler les creux et les bosses de la tôle.", "isCorrect": True},
                        {"text": "Le pistolet à souder.", "isCorrect": False},
                        {"text": "Le pied à coulisse.", "isCorrect": False}
                    ],
                    "correction": "La **Lime de carrossier** agit comme un révélateur des défauts de surface."
                },
                {
                    "questionNumber": 14,
                    "question": "Que doit-on faire de l'**eau de lavage** des sols ou des outils contenant des résidus de peinture et de solvants ?",
                    "answerOptions": [
                        {"text": "La jeter à l'égout.", "isCorrect": False},
                        {"text": "La collecter dans un bac de décantation/traitement pour séparation des boues et des solvants, avant élimination par une filière spécialisée.", "isCorrect": True},
                        {"text": "La réutiliser telle quelle.", "isCorrect": False},
                        {"text": "La stocker dans des fûts ouverts.", "isCorrect": False}
                    ],
                    "correction": "Le **traitement des effluents** est une obligation environnementale et légale."
                },
                {
                    "questionNumber": 15,
                    "question": "Quelle est l'importance de débrancher la **batterie 12 V** d'un véhicule avant toute opération de soudage ou de redressage au Tire-Clou ?",
                    "answerOptions": [
                        {"text": "Pour la recharger.", "isCorrect": False},
                        {"text": "Éviter les courts-circuits, les pics de tension et la destruction des calculateurs (ECU) sensibles aux variations électriques.", "isCorrect": True},
                        {"text": "Pour alléger le véhicule.", "isCorrect": False},
                        {"text": "Pour l'isoler du froid.", "isCorrect": False}
                    ],
                    "correction": "La **déconnexion** de la batterie protège l'électronique de bord."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est l'outil utilisé pour lisser et répartir le mastic de carrosserie sur la zone à réparer ?",
                    "answerOptions": [
                        {"text": "Le rouleau.", "isCorrect": False},
                        {"text": "La Spatule (ou Couteau) en plastique ou caoutchouc.", "isCorrect": True},
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "Le pinceau.", "isCorrect": False}
                    ],
                    "correction": "La **Spatule** permet une application uniforme et sans bulle."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle doit être la procédure lors du travail sous le véhicule (démontage de pièces sous la caisse) ?",
                    "answerOptions": [
                        {"text": "Utiliser un simple cric hydraulique.", "isCorrect": False},
                        {"text": "Utiliser impérativement des chandelles (ou le pont élévateur avec des cales de sécurité) pour éviter l'écrasement en cas de défaillance du cric.", "isCorrect": True},
                        {"text": "Travailler seul.", "isCorrect": False},
                        {"text": "Ne pas porter d'EPI.", "isCorrect": False}
                    ],
                    "correction": "Les **chandelles** sont le dispositif de sécurité passif obligatoire pour le travail sous caisse."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le danger principal du ponçage du **mastic Polyester** ?",
                    "answerOptions": [
                        {"text": "Il dégage des vapeurs acides.", "isCorrect": False},
                        {"text": "Il crée une grande quantité de poussière fine, irritante et très nocive pour les voies respiratoires (nécessite aspiration et masque P3).", "isCorrect": True},
                        {"text": "Il est inflammable.", "isCorrect": False},
                        {"text": "Il est corrosif.", "isCorrect": False}
                    ],
                    "correction": "Le **mastic** nécessite une aspiration et un ponçage adapté."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est l'outil de coupe adapté pour une découpe précise d'une tôle fine avant soudage (par opposition à la meuleuse) ?",
                    "answerOptions": [
                        {"text": "La cisaille manuelle.", "isCorrect": False},
                        {"text": "La Grignoteuse ou la Scie sabre (Lame pour métal fin).", "isCorrect": True},
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "Le cutter.", "isCorrect": False}
                    ],
                    "correction": "La **Grignoteuse** permet une découpe sans déformation excessive."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel est le rôle du **chariot à outils mobile** en carrosserie ?",
                    "answerOptions": [
                        {"text": "Stocker les pièces neuves.", "isCorrect": False},
                        {"text": "Organiser, sécuriser et avoir à portée de main les outils nécessaires (marteaux, tas, clés, etc.) pour chaque opération, afin d'éviter les déplacements inutiles et la perte de temps.", "isCorrect": True},
                        {"text": "Servir d'établi.", "isCorrect": False},
                        {"text": "Transporter la peinture.", "isCorrect": False}
                    ],
                    "correction": "L'**organisation de l'atelier** est clé pour l'efficacité et la sécurité."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : STRUCTURES ET MATÉRIAUX (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Structures et Matériaux (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la principale différence entre un **Acier Basse Limite Élastique (B.L.E)** et un **Acier Haute Limite Élastique (H.L.E)** ?",
                    "answerOptions": [
                        {"text": "La couleur.", "isCorrect": False},
                        {"text": "Le H.L.E est plus dur, plus résistant, moins ductile et ne doit pas être chauffé/soudé sans procédure stricte (caractéristiques mécaniques perdues lors du chauffage).", "isCorrect": True},
                        {"text": "Le B.L.E est plus cher.", "isCorrect": False},
                        {"text": "Le H.L.E est plus léger.", "isCorrect": False}
                    ],
                    "correction": "Les **Aciers H.L.E** sont utilisés pour les structures de sécurité (châssis) et exigent une réparation spécifique (souvent remplacement)."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la particularité du **soudage de l'Aluminium** par rapport à l'acier ?",
                    "answerOptions": [
                        {"text": "Il n'y a pas de différence.", "isCorrect": False},
                        {"text": "Il nécessite un poste à souder et un gaz de protection spécifiques (Argon, procédé TIG ou MIG Aluminium) et ne doit jamais être mélangé avec des outils ayant servi à l'acier (risque de corrosion).", "isCorrect": True},
                        {"text": "Il est plus rapide.", "isCorrect": False},
                        {"text": "Il nécessite de l'eau.", "isCorrect": False}
                    ],
                    "correction": "L'**Aluminium** a un point de fusion bas et s'oxyde très vite."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel est le rôle des **Zones à Déformation Programmée** sur un véhicule moderne (zones fusibles) ?",
                    "answerOptions": [
                        {"text": "Rendre la voiture plus rapide.", "isCorrect": False},
                        {"text": "Absorber l'énergie d'un choc en se déformant de manière contrôlée, protégeant ainsi l'habitacle et les occupants (sécurité passive).", "isCorrect": True},
                        {"text": "Rendre la carrosserie plus dure.", "isCorrect": False},
                        {"text": "Améliorer l'aérodynamisme.", "isCorrect": False}
                    ],
                    "correction": "Ces zones doivent être **remplacées** et non redressées après un choc."
                },
                {
                    "questionNumber": 24,
                    "question": "Quel est le matériau principal utilisé pour les pare-chocs, les ailes et certains éléments de garniture des véhicules modernes ?",
                    "answerOptions": [
                        {"text": "Le bois.", "isCorrect": False},
                        {"text": "Le Plastique (Polypropylène - PP, Polycarbonate - PC, ABS, etc.).", "isCorrect": True},
                        {"text": "L'aluminium.", "isCorrect": False},
                        {"text": "L'acier.", "isCorrect": False}
                    ],
                    "correction": "Le **Plastique** est léger et résistant aux chocs légers."
                },
                {
                    "questionNumber": 25,
                    "question": "Comment s'appelle la technique de réparation des plastiques (pare-chocs) qui consiste à faire fondre les bords et à ajouter une matière d'apport (souvent avec un pistolet à air chaud) ?",
                    "answerOptions": [
                        {"text": "Le collage.", "isCorrect": False},
                        {"text": "Le Soudage Plastique (ou Thermofusion).", "isCorrect": True},
                        {"text": "Le débosselage.", "isCorrect": False},
                        {"text": "Le planage.", "isCorrect": False}
                    ],
                    "correction": "Le **soudage** permet une réparation solide du plastique, souvent renforcée par des agrafes."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le risque de redresser une tôle en acier HLE avec un outillage classique (marteau et tas) ?",
                    "answerOptions": [
                        {"text": "La tôle devient trop souple.", "isCorrect": False},
                        {"text": "La tôle (très dure) se fissure, se déchire, ou ses caractéristiques mécaniques de sécurité sont altérées par la chaleur ou le choc.", "isCorrect": True},
                        {"text": "La tôle rouille.", "isCorrect": False},
                        {"text": "La tôle change de couleur.", "isCorrect": False}
                    ],
                    "correction": "Le **HLE** doit être coupé et remplacé selon les procédures constructeur."
                },
                {
                    "questionNumber": 27,
                    "question": "Qu'est-ce que le **Châssis (ou Structure Monocoque)** d'un véhicule ?",
                    "answerOptions": [
                        {"text": "Le moteur.", "isCorrect": False},
                        {"text": "L'ossature porteuse du véhicule (habitacle, berceau moteur, longerons) qui assure la rigidité, la sécurité et l'alignement des trains roulants.", "isCorrect": True},
                        {"text": "La peinture.", "isCorrect": False},
                        {"text": "Les portes.", "isCorrect": False}
                    ],
                    "correction": "La réparation du **Châssis** se fait sur marbre pour garantir la géométrie."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le type de mastic utilisé pour les petites imperfections ou les rayures fines (par opposition au mastic de remplissage épais) ?",
                    "answerOptions": [
                        {"text": "Mastic aluminium.", "isCorrect": False},
                        {"text": "Mastic de Finition (ou Mastic Fin), plus liquide et plus facile à poncer.", "isCorrect": True},
                        {"text": "Mastic fibre de verre.", "isCorrect": False},
                        {"text": "Mastic polyester.", "isCorrect": False}
                    ],
                    "correction": "Le **Mastic de finition** est appliqué après le mastic de remplissage."
                },
                {
                    "questionNumber": 29,
                    "question": "Quel est l'outil spécifique utilisé pour coller des éléments structurels (remplacement d'un panneau d'aile soudé) ?",
                    "answerOptions": [
                        {"text": "La colle cyanoacrylate.", "isCorrect": False},
                        {"text": "Le Pistolet à cartouche pour Mastic/Colle Bi-composant (colle structurale ou colle époxy).", "isCorrect": True},
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "Le fer à souder.", "isCorrect": False}
                    ],
                    "correction": "Le **collage structural** remplace de plus en plus le soudage sur les véhicules modernes."
                },
                {
                    "questionNumber": 30,
                    "question": "Pourquoi la réparation des panneaux en **fibre de carbone** nécessite-t-elle des EPI spécifiques (masque P3) et un atelier dédié ?",
                    "answerOptions": [
                        {"text": "Le carbone est inflammable.", "isCorrect": False},
                        {"text": "Les poussières de carbone sont conductrices d'électricité et très dangereuses pour la santé (voies respiratoires et organes).", "isCorrect": True},
                        {"text": "Le carbone est corrosif.", "isCorrect": False},
                        {"text": "Le carbone est très lourd.", "isCorrect": False}
                    ],
                    "correction": "La **fibre de carbone** est un matériau très technique (composites) et ses poussières sont très dangereuses."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment s'appelle le phénomène qui se produit lorsque le métal est déformé dans une zone, entraînant une bosse ou un creux dans une autre zone distante ?",
                    "answerOptions": [
                        {"text": "Le planage.", "isCorrect": False},
                        {"text": "La Déformation indirecte ou Tensions résiduelles (le choc se propage et génère des déformations secondaires).", "isCorrect": True},
                        {"text": "Le soudage.", "isCorrect": False},
                        {"text": "Le décapage.", "isCorrect": False}
                    ],
                    "correction": "Le carrossier doit comprendre comment les **tensions** sont réparties sur la tôle."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle est l'utilité du **Mastic fibre de verre** ?",
                    "answerOptions": [
                        {"text": "L'obtention d'une finition lisse.", "isCorrect": False},
                        {"text": "Reboucher des trous ou des perforations importantes (propriétés de remplissage et de rigidité) avant l'application du mastic polyester fin.", "isCorrect": True},
                        {"text": "Réparer l'aluminium.", "isCorrect": False},
                        {"text": "Réparer les plastiques.", "isCorrect": False}
                    ],
                    "correction": "Le **Mastic fibre** est très rigide et fort en remplissage."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel est le risque de monter un **élément de carrosserie non d'origine (adaptable)** ?",
                    "answerOptions": [
                        {"text": "Il est plus cher.", "isCorrect": False},
                        {"text": "Les tolérances, la qualité de l'acier (ou l'épaisseur) ou les points d'attache peuvent être différents, nécessitant des ajustements ou compromettant la résistance structurelle.", "isCorrect": True},
                        {"text": "Il rouille moins.", "isCorrect": False},
                        {"text": "Il est plus lourd.", "isCorrect": False}
                    ],
                    "correction": "Les pièces de **sécurité** doivent impérativement être d'origine ou certifiées."
                },
                {
                    "questionNumber": 34,
                    "question": "Qu'est-ce qu'une **Tôle galvanisée** ?",
                    "answerOptions": [
                        {"text": "Une tôle très brillante.", "isCorrect": False},
                        {"text": "Une tôle recouverte d'une couche protectrice de zinc (par trempage) pour une résistance maximale à la corrosion (rouille).", "isCorrect": True},
                        {"text": "Une tôle très épaisse.", "isCorrect": False},
                        {"text": "Une tôle en aluminium.", "isCorrect": False}
                    ],
                    "correction": "La **Galvanisation** protège l'acier de l'oxydation."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le rôle de l'**apprêt époxy** sur un métal brut ?",
                    "answerOptions": [
                        {"text": "Remplir les creux.", "isCorrect": False},
                        {"text": "Servir de primaire d'accrochage sur le métal nu (anti-rouille) et d'isolant (barrière) contre l'humidité (avant l'apprêt de garnissage).", "isCorrect": True},
                        {"text": "Donner la couleur finale.", "isCorrect": False},
                        {"text": "Lisser la surface.", "isCorrect": False}
                    ],
                    "correction": "L'**Apprêt époxy** est le meilleur primaire anti-corrosion."
                },
                {
                    "questionNumber": 36,
                    "question": "Comment appelle-t-on le revêtement qui, après séchage, donne la couleur visible mais qui n'a aucune protection mécanique (nécessite un vernis) ?",
                    "answerOptions": [
                        {"text": "L'apprêt.", "isCorrect": False},
                        {"text": "La Base mate (ou Base solvantée ou Hydro-diluable).", "isCorrect": True},
                        {"text": "Le mastic.", "isCorrect": False},
                        {"text": "L'époxy.", "isCorrect": False}
                    ],
                    "correction": "La **Base** est la couche de pigments."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est l'outil utilisé pour évaluer l'épaisseur des couches de peinture et d'apprêt après réparation ?",
                    "answerOptions": [
                        {"text": "Le pied à coulisse.", "isCorrect": False},
                        {"text": "Le Micromètre (ou Jauge d'épaisseur de film sec).", "isCorrect": True},
                        {"text": "Le mètre ruban.", "isCorrect": False},
                        {"text": "L'humidimètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Micromètre** est essentiel pour vérifier que la réparation n'a pas créé de surépaisseur excessive."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est le rôle du **Mastic à l'étain (brasure)** ?",
                    "answerOptions": [
                        {"text": "Remplir les creux sans rigidité.", "isCorrect": False},
                        {"text": "Réparer les tôles en aluminium ou combler de gros défauts sur acier, en offrant une finition très dure et résistante (sans utiliser de polyester/fibre).", "isCorrect": True},
                        {"text": "Réparer les plastiques.", "isCorrect": False},
                        {"text": "Coller les vitres.", "isCorrect": False}
                    ],
                    "correction": "Le **Mastic à l'étain** est une technique de réparation traditionnelle, très solide mais complexe."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est l'inconvénient principal des **Peintures Hydro-diluables (à l'eau)** ?",
                    "answerOptions": [
                        {"text": "Elles sont moins chères.", "isCorrect": False},
                        {"text": "Elles nécessitent plus de temps de séchage/évaporation avant le vernissage et sont plus sensibles à l'humidité et à la température lors de l'application (cabine obligatoire).", "isCorrect": True},
                        {"text": "Elles sont plus toxiques.", "isCorrect": False},
                        {"text": "Elles ont une mauvaise colorimétrie.", "isCorrect": False}
                    ],
                    "correction": "L'**Hydro-diluable** est la norme environnementale, mais exige un contrôle parfait de l'environnement de travail."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est l'outil utilisé pour déterminer la formulation exacte d'une couleur d'origine (teinte d'un véhicule) ?",
                    "answerOptions": [
                        {"text": "Le pied à coulisse.", "isCorrect": False},
                        {"text": "Le Spectrophotomètre (ou Colorimètre) pour mesurer les pigments et les effets (métallisé, nacré).", "isCorrect": True},
                        {"text": "Le décapeur thermique.", "isCorrect": False},
                        {"text": "Le marteau à planer.", "isCorrect": False}
                    ],
                    "correction": "Le **Spectrophotomètre** est indispensable pour les teintes complexes (tri-couche, nacré)."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : TECHNIQUES DE DÉFORMATION ET RÉPARATION (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Techniques de Déformation et Réparation (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la principale technique de réparation utilisée pour débosseler sans peinture (DSP) ?",
                    "answerOptions": [
                        {"text": "Le soudage.", "isCorrect": False},
                        {"text": "Le massage de la tôle par l'intérieur (ou l'extérieur avec des ventouses) à l'aide de leviers spéciaux (tiges) pour faire remonter le creux sans abîmer la peinture.", "isCorrect": True},
                        {"text": "Le ponçage.", "isCorrect": False},
                        {"text": "Le remplissage au mastic.", "isCorrect": False}
                    ],
                    "correction": "La **DSP** est réservée aux impacts légers sans étirement ni dégradation de la peinture."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel est l'outil utilisé pour **contre-frapper** (taper la bosse par l'intérieur) lors du débosselage (marteau/tas) ?",
                    "answerOptions": [
                        {"text": "Le pistolet à peinture.", "isCorrect": False},
                        {"text": "Le Tas (pièce métallique lourde et lisse, utilisé comme enclume ou support de frappe pour la rétreinte).", "isCorrect": True},
                        {"text": "La spatule.", "isCorrect": False},
                        {"text": "Le micromètre.", "isCorrect": False}
                    ],
                    "correction": "Le **Tas** assure que la force de frappe est appliquée uniquement sur la zone souhaitée."
                },
                {
                    "questionNumber": 43,
                    "question": "Comment appelle-t-on le procédé qui consiste à chauffer une tôle pour la contracter (rétrécir) et la faire revenir à sa forme initiale ?",
                    "answerOptions": [
                        {"text": "Le soudage.", "isCorrect": False},
                        {"text": "La Rétreinte (chauffage ciblé au chalumeau ou à l'électrode en étoile, suivi d'un refroidissement rapide).", "isCorrect": True},
                        {"text": "Le planage.", "isCorrect": False},
                        {"text": "Le ponçage.", "isCorrect": False}
                    ],
                    "correction": "La **Rétreinte** est utilisée pour éliminer l'étirement excessif de la tôle."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est le risque de trop **tirer** une tôle endommagée au Tire-Clou ?",
                    "answerOptions": [
                        {"text": "Le métal rouille.", "isCorrect": False},
                        {"text": "La tôle s'étire (ou s'allonge) créant une nouvelle bosse (un point dur) et nécessitant une rétreinte pour la contracter.", "isCorrect": True},
                        {"text": "La peinture se décolle.", "isCorrect": False},
                        {"text": "Le mastic ne tient pas.", "isCorrect": False}
                    ],
                    "correction": "Le débosselage se fait par **petites touches** pour ne pas étirer le métal."
                },
                {
                    "questionNumber": 45,
                    "question": "Quelle est la technique de préparation du métal brut (après ponçage ou meulage) avant application d'un primaire ?",
                    "answerOptions": [
                        {"text": "Le laquage.", "isCorrect": False},
                        {"text": "Le Dégraissage puis l'Application d'un Primaire d'accrochage (souvent époxy ou phosphatant) pour éviter la corrosion immédiate (rouille éclair).", "isCorrect": True},
                        {"text": "Le polissage.", "isCorrect": False},
                        {"text": "Le soudage.", "isCorrect": False}
                    ],
                    "correction": "Le métal doit être protégé très rapidement contre l'**oxydation**."
                },
                {
                    "questionNumber": 46,
                    "question": "Comment s'appelle l'outil qui permet de déformer et de positionner le châssis ou la caisse sur le **marbre** ?",
                    "answerOptions": [
                        {"text": "Le cric.", "isCorrect": False},
                        {"text": "La Tour de redressage ou la Poutre de traction (avec vérins et chaînes).", "isCorrect": True},
                        {"text": "Le pistolet à souder.", "isCorrect": False},
                        {"text": "Le micromètre.", "isCorrect": False}
                    ],
                    "correction": "La **Tour de redressage** applique une force contrôlée pour corriger la géométrie du châssis."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est l'inconvénient du **soudage MAG** par rapport au TIG (pour l'acier) ?",
                    "answerOptions": [
                        {"text": "Il est plus lent.", "isCorrect": False},
                        {"text": "Il laisse plus de projections (gratons), nécessite un nettoyage plus important et le cordon de soudure est plus épais (moins esthétique).", "isCorrect": True},
                        {"text": "Il n'est pas automatique.", "isCorrect": False},
                        {"text": "Il ne soude pas l'acier.", "isCorrect": False}
                    ],
                    "correction": "Le **MAG** (avec fil fourré ou fil plein et gaz actif) est le plus courant en carrosserie pour sa rapidité."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est le risque de poncer une vieille peinture sans savoir si elle contient de l'amiante ou du plomb (vieux véhicules) ?",
                    "answerOptions": [
                        {"text": "Le ponçage est inefficace.", "isCorrect": False},
                        {"text": "Inhalation de particules extrêmement dangereuses (plomb ou amiante) entraînant des maladies graves (silicose, cancer).", "isCorrect": True},
                        {"text": "La tôle se déforme.", "isCorrect": False},
                        {"text": "La peinture devient trop brillante.", "isCorrect": False}
                    ],
                    "correction": "Le **diagnostic** des matériaux anciens est une obligation."
                },
                {
                    "questionNumber": 49,
                    "question": "Comment s'appelle l'outil de mesurage qui permet de vérifier l'écartement des longerons par rapport à l'axe central du véhicule (après un choc avant/arrière) ?",
                    "answerOptions": [
                        {"text": "Le pied à coulisse.", "isCorrect": False},
                        {"text": "La Pige de mesure (ou Équerre de mesure géométrique).", "isCorrect": True},
                        {"text": "Le micromètre.", "isCorrect": False},
                        {"text": "Le décamètre.", "isCorrect": False}
                    ],
                    "correction": "La **Pige** ou le marbre permet de vérifier la conformité aux cotes constructeur."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le rôle du **dégraissage avec un chiffon humide** (non sec) ?",
                    "answerOptions": [
                        {"text": "Rendre la surface plus rugueuse.", "isCorrect": False},
                        {"text": "Le chiffon est humidifié par le dégraissant pour emprisonner et retirer les impuretés (au lieu de les étaler), puis un chiffon sec est utilisé pour essuyer l'excès.", "isCorrect": True},
                        {"text": "Rendre la surface plus lisse.", "isCorrect": False},
                        {"text": "Laisser des traces.", "isCorrect": False}
                    ],
                    "correction": "Le dégraissage doit se faire en **deux étapes** (humide puis sec) pour éviter l'étalement des contaminants."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle est la cause principale de l'apparition de **cloques** dans la peinture après séchage ?",
                    "answerOptions": [
                        {"text": "La peinture était trop liquide.", "isCorrect": False},
                        {"text": "De l'humidité ou des contaminants (graisse, silicone, poussière) sont emprisonnés sous la couche de finition, ou un mauvais temps de séchage entre les couches.", "isCorrect": True},
                        {"text": "La peinture était trop épaisse.", "isCorrect": False},
                        {"text": "Le vernis était trop brillant.", "isCorrect": False}
                    ],
                    "correction": "Les **cloques** sont généralement dues à l'humidité ou à une mauvaise préparation."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est l'objectif du **ponçage par étape** (granulométrie croissante, ex : P80, P180, P400) ?",
                    "answerOptions": [
                        {"text": "Allonger le temps de travail.", "isCorrect": False},
                        {"text": "Éliminer progressivement les défauts laissés par le grain précédent (rayures) pour obtenir une surface parfaitement lisse (l'apprêt ne doit pas révéler les rayures du ponçage précédent).", "isCorrect": True},
                        {"text": "Rendre la surface rugueuse.", "isCorrect": False},
                        {"text": "Économiser du papier.", "isCorrect": False}
                    ],
                    "correction": "Le respect de la **granulométrie** est essentiel pour une finition sans défaut."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la fonction d'un **apprêt garnissant (ou bouche-pores)** ?",
                    "answerOptions": [
                        {"text": "Donner la couleur finale.", "isCorrect": False},
                        {"text": "Combler les petites imperfections de la surface après masticage et ponçage (rayures P180-P240) et créer une couche isolante avant la peinture de finition.", "isCorrect": True},
                        {"text": "Protéger le métal de la corrosion.", "isCorrect": False},
                        {"text": "Dégraisser la surface.", "isCorrect": False}
                    ],
                    "correction": "L'**Apprêt garnissant** est la couche de préparation pour le ponçage final."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est le risque de ne pas utiliser le **durcisseur** adapté à la température de la cabine (durcisseur trop rapide par temps froid) ?",
                    "answerOptions": [
                        {"text": "Le vernis coule.", "isCorrect": False},
                        {"text": "Le vernis sèche trop vite en surface (peau) et ne durcit pas en profondeur (défaut de cuisson/polymérisation, surface poisseuse ou molle).", "isCorrect": True},
                        {"text": "Le vernis est trop brillant.", "isCorrect": False},
                        {"text": "Le vernis devient mat.", "isCorrect": False}
                    ],
                    "correction": "Le choix du **durcisseur** (standard, rapide, lent) est dicté par la température de l'atelier/cabine."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le risque si la **pression d'air** du pistolet à peinture est trop faible ?",
                    "answerOptions": [
                        {"text": "Le brouillard est trop fin.", "isCorrect": False},
                        {"text": "Le jet de peinture est mal pulvérisé (gros grain), ce qui crée l'effet 'peau d'orange' ou des défauts de mouillage.", "isCorrect": True},
                        {"text": "La peinture coule.", "isCorrect": False},
                        {"text": "La peinture sèche trop vite.", "isCorrect": False}
                    ],
                    "correction": "La **pression** d'air (souvent 2 à 3 bars) doit être adaptée à la viscosité de la peinture et au type de pistolet (HVLP, conventionnel)."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment s'appelle l'opération qui consiste à **estomper** la peinture (la base) sur une zone adjacente à la zone réparée pour masquer le raccord de couleur ?",
                    "answerOptions": [
                        {"text": "Le masquage.", "isCorrect": False},
                        {"text": "Le Raccord noyé ou Raccord fondu (la base est étirée ou diffusée par l'air ou le diluant de raccordement).", "isCorrect": True},
                        {"text": "Le mouillage.", "isCorrect": False},
                        {"text": "Le garnissage.", "isCorrect": False}
                    ],
                    "correction": "Le **Raccord noyé** est indispensable pour les teintes complexes ou vieillies."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est le rôle du **filtre à air** (ou séparateur d'eau) sur le circuit d'air comprimé de l'atelier ?",
                    "answerOptions": [
                        {"text": "Réguler la pression.", "isCorrect": False},
                        {"text": "Éliminer l'humidité (eau) et les impuretés/huiles du compresseur qui pourraient contaminer la peinture et causer des défauts (cratères, piqûres).", "isCorrect": True},
                        {"text": "Augmenter le débit.", "isCorrect": False},
                        {"text": "Refroidir l'air.", "isCorrect": False}
                    ],
                    "correction": "Un air **propre et sec** est fondamental pour une peinture de qualité."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle est la cause principale d'un défaut de peinture appelé **« peau d'orange »** ?",
                    "answerOptions": [
                        {"text": "La surface était trop lisse.", "isCorrect": False},
                        {"text": "Viscosité trop élevée (peinture trop épaisse), pression d'air trop basse, distance pistolet/support trop grande, ou un vernis/diluant mal adapté.", "isCorrect": True},
                        {"text": "La peinture était trop diluée.", "isCorrect": False},
                        {"text": "Le séchage était trop lent.", "isCorrect": False}
                    ],
                    "correction": "La **Peau d'orange** est un manque de tension de surface (mauvais étalement du film)."
                },
                {
                    "questionNumber": 59,
                    "question": "Comment s'appelle l'opération qui consiste à éliminer les poussières et les impuretés sur la surface avant le vernissage (souvent avec un chiffon collant) ?",
                    "answerOptions": [
                        {"text": "Le dégraissage.", "isCorrect": False},
                        {"text": "L'Époussetage (avec un tampon d'essuyage ou un chiffon de dépoussiérage collant).", "isCorrect": True},
                        {"text": "Le ponçage.", "isCorrect": False},
                        {"text": "Le masquage.", "isCorrect": False}
                    ],
                    "correction": "L'**Époussetage** final est crucial avant l'application de la base et du vernis."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le risque de ne pas respecter le **temps d'évaporation** entre la couche de base (peinture couleur) et la couche de vernis ?",
                    "answerOptions": [
                        {"text": "Le vernis ne brille pas.", "isCorrect": False},
                        {"text": "Le solvant de la base (encore présent) peut remonter à travers le vernis et créer des défauts (taches, matité, craquelures ou 'remontée de la laque').", "isCorrect": True},
                        {"text": "La couleur change.", "isCorrect": False},
                        {"text": "Le vernis coule.", "isCorrect": False}
                    ],
                    "correction": "Le **temps d'évaporation** (ou flash-off) est essentiel pour que le solvant s'échappe de la base."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : PEINTURE ET PRÉPARATION (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Peinture et Préparation (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel est le rôle du **papier de masquage** (papier kraft) ?",
                    "answerOptions": [
                        {"text": "Protéger la zone à peindre.", "isCorrect": False},
                        {"text": "Protéger les parties non à peindre (vitres, pneus, joints, intérieur) contre le brouillard de pulvérisation.", "isCorrect": True},
                        {"text": "Dégraisser le support.", "isCorrect": False},
                        {"text": "Poncer la carrosserie.", "isCorrect": False}
                    ],
                    "correction": "Le **Masquage** assure une délimitation propre et une protection intégrale du véhicule."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel est le risque d'utiliser un **ruban de masquage classique** (pour la maison) en carrosserie ?",
                    "answerOptions": [
                        {"text": "Il est trop cher.", "isCorrect": False},
                        {"text": "Il laisse des résidus de colle, est peu résistant aux solvants de la peinture et peut ne pas être adapté aux courbes (contrairement au ruban 'fineline').", "isCorrect": True},
                        {"text": "Il est trop large.", "isCorrect": False},
                        {"text": "Il déchire la peinture.", "isCorrect": False}
                    ],
                    "correction": "Le **ruban de masquage professionnel** est résistant aux solvants et à la chaleur de la cabine."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment s'appelle l'opération qui consiste à corriger un défaut de peinture (poussière, coulure) après séchage ?",
                    "answerOptions": [
                        {"text": "Le dégraissage.", "isCorrect": False},
                        {"text": "Le Ponçage à l'eau très fin (P1500 à P3000) suivi du Polissage (lustrage) pour retrouver la brillance.", "isCorrect": True},
                        {"text": "Le masquage.", "isCorrect": False},
                        {"text": "Le garnissage.", "isCorrect": False}
                    ],
                    "correction": "Le **Polissage** est la touche finale pour un aspect impeccable."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est l'outil utilisé pour poncer des surfaces courbes ou difficiles d'accès sans créer de creux ou de bosses ?",
                    "answerOptions": [
                        {"text": "La cale rigide.", "isCorrect": False},
                        {"text": "La Cale souple (ou Cale à main en mousse ou caoutchouc).", "isCorrect": True},
                        {"text": "La ponceuse rotative.", "isCorrect": False},
                        {"text": "Le pistolet à peinture.", "isCorrect": False}
                    ],
                    "correction": "La **cale souple** épouse les formes du panneau."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est le rôle du **dégraissant antistatique** (souvent pour les plastiques) ?",
                    "answerOptions": [
                        {"text": "Rendre le plastique collant.", "isCorrect": False},
                        {"text": "Éliminer la charge statique sur le plastique pour empêcher la poussière d'y adhérer (important avant l'apprêt plastique).", "isCorrect": True},
                        {"text": "Le rendre plus rugueux.", "isCorrect": False},
                        {"text": "Le rendre plus souple.", "isCorrect": False}
                    ],
                    "correction": "Les **plastiques** attirent la poussière par électrostatisme."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le type de peinture qui utilise un **vernis bi-couche** (Base mate + Vernis) ?",
                    "answerOptions": [
                        {"text": "Les teintes unies (non métallisées) non brillantes.", "isCorrect": False},
                        {"text": "Les teintes Métallisées, Nacrées et les bases Hydro-diluables (la protection et la brillance sont apportées par la couche de vernis).", "isCorrect": True},
                        {"text": "Les teintes mates.", "isCorrect": False},
                        {"text": "Les apprêts.", "isCorrect": False}
                    ],
                    "correction": "Le **Bi-couche** est le système le plus répandu (brillance et protection dans le vernis)."
                },
                {
                    "questionNumber": 67,
                    "question": "Comment appelle-t-on le défaut où la peinture s'écaille ou se décolle du support après un certain temps ?",
                    "answerOptions": [
                        {"text": "Le farinage.", "isCorrect": False},
                        {"text": "Le Décollement (problème d'adhérence du primaire/mastic sur la tôle, souvent dû à un mauvais dégraissage ou à un ponçage insuffisant).", "isCorrect": True},
                        {"text": "Le jaunissement.", "isCorrect": False},
                        {"text": "La craquelure.", "isCorrect": False}
                    ],
                    "correction": "Le **Décollement** (ou perte d'accroche) est le défaut le plus grave du carrossier-peintre."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le rôle du **diluant de raccordement** (blender) ?",
                    "answerOptions": [
                        {"text": "Accélérer le séchage.", "isCorrect": False},
                        {"text": "Dissoudre légèrement les bords du vernis ou de la base pour créer un raccord invisible et sans démarcation (utilisé dans la technique du raccord noyé).", "isCorrect": True},
                        {"text": "Rendre la peinture plus opaque.", "isCorrect": False},
                        {"text": "Nettoyer le pistolet.", "isCorrect": False}
                    ],
                    "correction": "Le **Diluant de raccordement** 'adoucit' les bords du film."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel est l'outil utilisé pour **mélanger** la base mate ou le vernis avant l'application (pour remettre les pigments en suspension) ?",
                    "answerOptions": [
                        {"text": "La spatule.", "isCorrect": False},
                        {"text": "Le Mélangeur mécanique ou l'Agitateur (nécessaire pour les bases métallisées et nacrées).", "isCorrect": True},
                        {"text": "Le pistolet à peinture.", "isCorrect": False},
                        {"text": "La balance.", "isCorrect": False}
                    ],
                    "correction": "Les **pigments métallisés** se déposent très vite et doivent être remis en suspension."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est le risque de poncer le mastic ou l'apprêt à la **main** au lieu de la cale ou de la ponceuse (sur une grande surface plane) ?",
                    "answerOptions": [
                        {"text": "Le ponçage est trop lent.", "isCorrect": False},
                        {"text": "Créer des vagues, des bosses et des creux (ondulations) car la main ne permet pas de respecter la planéité du panneau.", "isCorrect": True},
                        {"text": "Le ponçage est trop efficace.", "isCorrect": False},
                        {"text": "La poussière est trop fine.", "isCorrect": False}
                    ],
                    "correction": "La **cale** (rigide ou souple) est essentielle pour la planéité."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment s'appelle l'opération qui consiste à passer une flamme (ou un décapeur thermique) rapidement sur un plastique nu avant l'apprêt ?",
                    "answerOptions": [
                        {"text": "Le soudage.", "isCorrect": False},
                        {"text": "Le Flammage (ou Primaire d'adhérence par la chaleur) pour ouvrir les pores du plastique et améliorer l'accroche.", "isCorrect": True},
                        {"text": "Le dégraissage.", "isCorrect": False},
                        {"text": "Le ponçage.", "isCorrect": False}
                    ],
                    "correction": "Le **Flammage** est une technique d'amélioration de l'accroche sur certains plastiques (PP)."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le défaut de peinture qui apparaît sous la forme de petits **cratères** (comme des piqûres) ?",
                    "answerOptions": [
                        {"text": "La coulure.", "isCorrect": False},
                        {"text": "Les Cratères (ou 'fisheyes') causés par la contamination de surface (silicone, graisse, eau) qui repousse la peinture.", "isCorrect": True},
                        {"text": "La peau d'orange.", "isCorrect": False},
                        {"text": "Le farinage.", "isCorrect": False}
                    ],
                    "correction": "Les **Cratères** sont le signe d'une contamination (souvent silicone) qui doit être éliminée avec un additif anti-silicone."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est le rôle de la **Balance électronique de précision** en peinture ?",
                    "answerOptions": [
                        {"text": "Mesurer l'épaisseur.", "isCorrect": False},
                        {"text": "Peser très précisément les différents composants de la peinture (bases, pigments, diluant, durcisseur) selon la formule de la teinte (colorimétrie).", "isCorrect": True},
                        {"text": "Mesurer la pression.", "isCorrect": False},
                        {"text": "Mesurer la température.", "isCorrect": False}
                    ],
                    "correction": "La **Balance** garantit le respect de la formule pour une couleur conforme."
                },
                {
                    "questionNumber": 74,
                    "question": "Quel est le risque d'appliquer le mastic de carrosserie sur une tôle non poncée (tôle brillante/glacée) ?",
                    "answerOptions": [
                        {"text": "Le mastic sèche trop vite.", "isCorrect": False},
                        {"text": "Le mastic n'adhère pas (il n'a pas de 'clef d'accroche') et se décollera ou se fissurera rapidement après application des couches suivantes.", "isCorrect": True},
                        {"text": "Le mastic coule.", "isCorrect": False},
                        {"text": "Le mastic est trop liquide.", "isCorrect": False}
                    ],
                    "correction": "La tôle doit être **poncée au métal brut** (P80 ou P120) pour l'accroche."
                },
                {
                    "questionNumber": 75,
                    "question": "Comment s'appelle la technique de polissage utilisée pour enlever les traces de ponçage fin (après correction de défauts) ?",
                    "answerOptions": [
                        {"text": "Le lustrage.", "isCorrect": False},
                        {"text": "Le Polissage (avec une polisseuse rotative ou orbitale, et une pâte à polir abrasive, puis une pâte de finition).", "isCorrect": True},
                        {"text": "Le décapage.", "isCorrect": False},
                        {"text": "Le mouillage.", "isCorrect": False}
                    ],
                    "correction": "Le **Polissage** rétablit le brillant et l'aspect miroir du vernis."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le rôle de la **température** dans une cabine de peinture (hors cuisson) ?",
                    "answerOptions": [
                        {"text": "Réguler l'humidité.", "isCorrect": False},
                        {"text": "Maintenir une température constante (20 à 25°C) pour un séchage et un étalement optimaux du vernis (tension de surface) et contrôler la viscosité du produit.", "isCorrect": True},
                        {"text": "Changer la couleur.", "isCorrect": False},
                        {"text": "Assurer la sécurité.", "isCorrect": False}
                    ],
                    "correction": "La **température** influence directement le temps de tirage et l'aspect final."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le défaut causé par une épaisseur excessive de peinture ou de vernis, souvent dans les parties verticales ?",
                    "answerOptions": [
                        {"text": "La peau d'orange.", "isCorrect": False},
                        {"text": "La Coulure (la peinture/vernis glisse sous l'effet de la gravité avant d'avoir tiré suffisamment).", "isCorrect": True},
                        {"text": "Le farinage.", "isCorrect": False},
                        {"text": "Le craquellement.", "isCorrect": False}
                    ],
                    "correction": "La **Coulure** est corrigée par ponçage et polissage après séchage."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel est le risque de peindre un plastique (pare-chocs) sans avoir ajouté d'**assouplissant** ou de **flexibilisant** au vernis ?",
                    "answerOptions": [
                        {"text": "Le vernis coule.", "isCorrect": False},
                        {"text": "Le vernis/laque est trop rigide et craquelle ou se décolle lors des déformations (chocs légers ou vibrations) du plastique.", "isCorrect": True},
                        {"text": "Le vernis devient mat.", "isCorrect": False},
                        {"text": "Le vernis jaunit.", "isCorrect": False}
                    ],
                    "correction": "L'**Assouplissant** permet au vernis de suivre la flexibilité du support plastique."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est l'outil utilisé pour nettoyer et dégraisser les outils de peinture (pistolets) ?",
                    "answerOptions": [
                        {"text": "L'eau claire.", "isCorrect": False},
                        {"text": "Le Diluant de nettoyage (ou Solvant de nettoyage) dans un bac de lavage de pistolet.", "isCorrect": True},
                        {"text": "Le savon.", "isCorrect": False},
                        {"text": "L'huile.", "isCorrect": False}
                    ],
                    "correction": "Le **diluant de nettoyage** est essentiel, même pour les bases hydro-diluables, afin d'éliminer toute trace de pigment ou de résine."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment s'appelle l'outil utilisé pour déterminer le niveau d'humidité dans le bois ou le plâtre (pour les véhicules utilitaires ou les camping-cars) ?",
                    "answerOptions": [
                        {"text": "Le thermomètre.", "isCorrect": False},
                        {"text": "L'Humidimètre.", "isCorrect": True},
                        {"text": "Le micromètre.", "isCorrect": False},
                        {"text": "Le spectophotomètre.", "isCorrect": False}
                    ],
                    "correction": "L'**Humidimètre** est important pour les structures composites ou les aménagements intérieurs."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : CONTRÔLE, ORGANISATION ET SOUDAGE (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Contrôle, Organisation et Soudage (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est le rôle des **points de référence constructeur** sur un châssis ?",
                    "answerOptions": [
                        {"text": "Déterminer la couleur.", "isCorrect": False},
                        {"text": "Servir de base de mesure (fixes et précis) pour le contrôle géométrique, permettant de vérifier si la caisse a été déformée par le choc (vérification des cotes X, Y, Z).", "isCorrect": True},
                        {"text": "Indiquer l'emplacement des roues.", "isCorrect": False},
                        {"text": "Indiquer le type de moteur.", "isCorrect": False}
                    ],
                    "correction": "Les **cotes constructeur** sont la référence absolue pour le redressage sur marbre."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel est le risque de souder une tôle **non dégraissée** (ou non décapée) ?",
                    "answerOptions": [
                        {"text": "La soudure est trop brillante.", "isCorrect": False},
                        {"text": "Le bain de fusion est contaminé (création de porosités), la soudure est fragile, et dégage des fumées toxiques (graisse brûlée).", "isCorrect": True},
                        {"text": "La soudure est trop longue.", "isCorrect": False},
                        {"text": "La soudure ne chauffe pas.", "isCorrect": False}
                    ],
                    "correction": "Le métal doit être **nu et propre** avant soudage."
                },
                {
                    "questionNumber": 83,
                    "question": "Comment s'appelle l'opération qui consiste à éliminer l'excès de matière après un soudage (cordon de soudure) pour obtenir une surface plane ?",
                    "answerOptions": [
                        {"text": "Le planage.", "isCorrect": False},
                        {"text": "Le Meulage et le Ponçage (souvent à la meuleuse, puis ponceuse pour la finition).", "isCorrect": True},
                        {"text": "Le débosselage.", "isCorrect": False},
                        {"text": "Le dégraissage.", "isCorrect": False}
                    ],
                    "correction": "Le **Meulage** est suivi du ponçage pour préparer la surface au masticage."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est l'outil utilisé pour vérifier qu'une soudure est bien **pénétrée** (soudure pleine) ?",
                    "answerOptions": [
                        {"text": "Le mètre ruban.", "isCorrect": False},
                        {"text": "Le Contrôle visuel (aspect régulier du cordon), le contrôle par Ressuage (pour les fissures) ou les tests destructifs.", "isCorrect": True},
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "Le pied à coulisse.", "isCorrect": False}
                    ],
                    "correction": "Une mauvaise **pénétration** entraîne une soudure fragile (point de rupture)."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le rôle du **Mastic d'étanchéité** (mastic de joint) ?",
                    "answerOptions": [
                        {"text": "Maintenir la couleur.", "isCorrect": False},
                        {"text": "Assurer l'étanchéité à l'eau et à l'air des joints de la carrosserie (soudure, ailes, fonds de coffre) pour éviter la corrosion interne et l'infiltration.", "isCorrect": True},
                        {"text": "Maintenir la rigidité.", "isCorrect": False},
                        {"text": "Remplir les bosses.", "isCorrect": False}
                    ],
                    "correction": "Le **Mastic d'étanchéité** (souvent polyuréthane) est une couche de protection essentielle."
                },
                {
                    "questionNumber": 86,
                    "question": "Qu'est-ce qu'une **Fiche de Travail (ou Ordre de Réparation)** ?",
                    "answerOptions": [
                        {"text": "Un plan de la carrosserie.", "isCorrect": False},
                        {"text": "Le document de suivi du véhicule qui liste les travaux à effectuer, les pièces à commander, les temps alloués, et le détail de chaque étape de la réparation.", "isCorrect": True},
                        {"text": "Le catalogue de peinture.", "isCorrect": False},
                        {"text": "Le devis initial.", "isCorrect": False}
                    ],
                    "correction": "La **Fiche de Travail** garantit la traçabilité et le respect des temps barèmes."
                },
                {
                    "questionNumber": 87,
                    "question": "Quel est l'outil utilisé pour démonter des agrafes ou des garnitures sans les casser ?",
                    "answerOptions": [
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "Le Levier de démontage (ou Pince à garnitures) en plastique ou composite.", "isCorrect": True},
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "Le pistolet à souder.", "isCorrect": False}
                    ],
                    "correction": "Le **Démontage sans casse** (éléments plastiques) est une compétence clé."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le rôle de la **cabine de peinture ventilée** (hors phase de cuisson) ?",
                    "answerOptions": [
                        {"text": "Réguler l'humidité.", "isCorrect": False},
                        {"text": "Assurer l'extraction des brouillards de peinture et des solvants (sécurité et propreté), et maintenir une atmosphère saine et exempte de poussière pendant l'application.", "isCorrect": True},
                        {"text": "Accélérer le séchage.", "isCorrect": False},
                        {"text": "Éclairer l'opérateur.", "isCorrect": False}
                    ],
                    "correction": "La **cabine** est un environnement contrôlé, vital pour la qualité et la sécurité."
                },
                {
                    "questionNumber": 89,
                    "question": "Comment appelle-t-on la déformation d'un panneau qui n'a pas été redressée et qui est recouverte d'une épaisseur excessive de mastic ?",
                    "answerOptions": [
                        {"text": "Le craquellement.", "isCorrect": False},
                        {"text": "La Surcharges de mastic (l'épaisseur excessive de mastic est fragile, risque de craquellement et est visible à la lime de carrossier).", "isCorrect": True},
                        {"text": "La coulure.", "isCorrect": False},
                        {"text": "La peau d'orange.", "isCorrect": False}
                    ],
                    "correction": "Le **Mastic** doit rester une fine couche de finition sur une tôle redressée au maximum."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le rôle du **démontage de pièces** (feux, poignées, joints) avant la peinture ?",
                    "answerOptions": [
                        {"text": "Rendre la voiture plus légère.", "isCorrect": False},
                        {"text": "Garantir une couverture totale de la pièce à peindre (peindre sous les joints et les garnitures) pour éviter les traces de masquage visibles.", "isCorrect": True},
                        {"text": "Vérifier l'état interne.", "isCorrect": False},
                        {"text": "Les nettoyer.", "isCorrect": False}
                    ],
                    "correction": "Le **Démontage** permet une finition de qualité professionnelle."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est l'outil utilisé pour déterminer la nature d'un plastique (ABS, PP, etc.) avant de le souder (pour choisir la bonne matière d'apport) ?",
                    "answerOptions": [
                        {"text": "Le micromètre.", "isCorrect": False},
                        {"text": "Le Marqueur d'identification (ou la vérification du sigle gravé sur la pièce) ou le test à la flamme (pour les professionnels).", "isCorrect": True},
                        {"text": "Le pistolet à souder.", "isCorrect": False},
                        {"text": "La balance.", "isCorrect": False}
                    ],
                    "correction": "Il faut souder avec le **même type de plastique** pour une fusion homogène."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel est le risque de poncer une zone fraichement soudée sans avoir laissé le temps au métal de **refroidir** ?",
                    "answerOptions": [
                        {"text": "La soudure s'écaille.", "isCorrect": False},
                        {"text": "La tôle (ramollie par la chaleur) s'étire ou se déforme sous la pression du ponçage ou du meulage (création de bosses).", "isCorrect": True},
                        {"text": "La soudure rouille.", "isCorrect": False},
                        {"text": "Le mastic ne tient pas.", "isCorrect": False}
                    ],
                    "correction": "Le **refroidissement** est crucial pour que le métal retrouve sa rigidité."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment s'appelle l'outil utilisé pour effectuer une petite réparation de carrosserie (débosselage) sur des éléments en aluminium, sans utiliser de soudure ?",
                    "answerOptions": [
                        {"text": "Le tire-clou.", "isCorrect": False},
                        {"text": "Le Système de Ventouses à colle (pour tirer l'aluminium à froid sans le souder, ce qui pourrait le fragiliser).", "isCorrect": True},
                        {"text": "Le chalumeau.", "isCorrect": False},
                        {"text": "Le marteau rivoir.", "isCorrect": False}
                    ],
                    "correction": "L'**Aluminium** est souvent réparé à froid car la chaleur le fragilise."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le rôle de la **ventilation forcée** dans la cabine pendant la phase de cuisson du vernis ?",
                    "answerOptions": [
                        {"text": "Refroidir le véhicule.", "isCorrect": False},
                        {"text": "Assurer l'extraction des vapeurs de solvants qui s'échappent du vernis pendant le chauffage (pour prévenir l'explosion et garantir un séchage sain).", "isCorrect": True},
                        {"text": "Maintenir l'humidité.", "isCorrect": False},
                        {"text": "Empêcher la coulure.", "isCorrect": False}
                    ],
                    "correction": "La **Ventilation** (et la filtration) est active pendant toutes les phases."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est l'outil utilisé pour appliquer un **antigravillon** (protection noire granuleuse sur les bas de caisse) ?",
                    "answerOptions": [
                        {"text": "Le pistolet à peinture HVLP.", "isCorrect": False},
                        {"text": "Le Pistolet à cartouche (spécifique aux produits épais) pour pulvériser l'anti-gravillon (produit sous forme pâteuse).", "isCorrect": True},
                        {"text": "Le rouleau.", "isCorrect": False},
                        {"text": "Le pinceau.", "isCorrect": False}
                    ],
                    "correction": "L'**Antigravillon** est un revêtement texturé appliqué sous pression."
                },
                {
                    "questionNumber": 96,
                    "question": "Comment s'appelle l'opération qui consiste à éliminer les petites pointes ou défauts (gratons) d'une soudure avant le meulage ?",
                    "answerOptions": [
                        {"text": "Le décapage.", "isCorrect": False},
                        {"text": "Le Burinage (ou Dégrappage) au marteau ou au burin pneumatique.", "isCorrect": True},
                        {"text": "Le ponçage.", "isCorrect": False},
                        {"text": "Le planage.", "isCorrect": False}
                    ],
                    "correction": "Le **Burinage** enlève la matière en excès avant la finition à la meule."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est l'outil de diagnostic utilisé pour identifier les défauts électriques (avant et après réparation) liés aux capteurs ou aux calculateurs de carrosserie ?",
                    "answerOptions": [
                        {"text": "Le multimètre.", "isCorrect": False},
                        {"text": "La Valise de Diagnostic (outil de lecture des calculateurs et des codes défauts).", "isCorrect": True},
                        {"text": "Le thermomètre.", "isCorrect": False},
                        {"text": "Le micromètre.", "isCorrect": False}
                    ],
                    "correction": "La **Valise de Diagnostic** est cruciale pour les systèmes électroniques (ADAS, airbags, etc.)."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle est l'importance de remplacer les **rivets de sécurité** (par exemple, sur un capot ou une traverse) par des rivets neufs de même qualité ?",
                    "answerOptions": [
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Garantir la résistance structurelle et le bon fonctionnement des éléments (ex: charnières) en cas de nouvel accident (respect des normes de sécurité).", "isCorrect": True},
                        {"text": "Pour des raisons de couleur.", "isCorrect": False},
                        {"text": "Pour des raisons de poids.", "isCorrect": False}
                    ],
                    "correction": "Le **respect des fixations** d'origine est une exigence constructeur."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est l'outil utilisé pour poncer (ou 'déglacer') légèrement le vernis autour de la zone à peindre avant un raccord noyé ?",
                    "answerOptions": [
                        {"text": "Le pistolet.", "isCorrect": False},
                        {"text": "Le Disque abrasif de dépolissage (P800, P1000 ou abrasif 'Scotch-Brite') pour créer une 'clef' d'accroche pour le nouveau vernis.", "isCorrect": True},
                        {"text": "Le marteau.", "isCorrect": False},
                        {"text": "La spatule.", "isCorrect": False}
                    ],
                    "correction": "Le **dépolissage** assure l'accrochage du nouveau vernis (évite le décollement)."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est la cause principale de la **perte de brillance** (matité) ou du jaunissement d'un vernis neuf après quelques mois ?",
                    "answerOptions": [
                        {"text": "Trop de polissage.", "isCorrect": False},
                        {"text": "Un vernis de mauvaise qualité (faible résistance aux UV) ou un durcisseur non adapté (trop rapide, trop lent) qui a entraîné une mauvaise polymérisation à cœur.", "isCorrect": True},
                        {"text": "Une mauvaise couleur.", "isCorrect": False},
                        {"text": "Un ponçage excessif.", "isCorrect": False}
                    ],
                    "correction": "La **résistance aux UV** et la polymérisation garantissent la durabilité du brillant."
                },
            ]
        }
    }
}