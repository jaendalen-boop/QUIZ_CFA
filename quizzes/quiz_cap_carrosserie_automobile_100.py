quiz_data = {
    "title": "Quiz CAP Carrossier Automobile (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : ANALYSE STRUCTURELLE ET TECHNOLOGIE DU VÉHICULE (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : ANALYSE STRUCTURELLE ET TECHNOLOGIE DU VÉHICULE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel type d'assemblage rend un élément de carrosserie inamovible ?",
                    "answerOptions": [
                        {"text": "Soudure", "isCorrect": True},
                        {"text": "Vissage", "isCorrect": False},
                        {"text": "Agrafage", "isCorrect": False},
                        {"text": "Boulonnage", "isCorrect": False}
                    ],
                    "correction": "Les éléments inamovibles sont assemblés par soudage, collage structurel ou sertissage et nécessitent une opération de découpe pour être remplacés."
                },
                {
                    "questionNumber": 2,
                    "question": "Quelle est la fonction principale des zones fusibles situées sur les longerons avant d'un véhicule ?",
                    "answerOptions": [
                        {"text": "Absorber l'énergie cinétique lors d'un choc frontal", "isCorrect": True},
                        {"text": "Rigidifier le châssis pour empêcher toute déformation", "isCorrect": False},
                        {"text": "Supporter le poids du moteur et de la transmission", "isCorrect": False},
                        {"text": "Permettre la fixation des éléments de suspension avant", "isCorrect": False}
                    ],
                    "correction": "Les zones fusibles sont des zones de déformation programmée conçues pour s'écraser lors d'un impact, protégeant ainsi l'habitacle."
                },
                {
                    "questionNumber": 3,
                    "question": "Comment se nomme la partie centrale de la caisse qui doit rester indéformable pour protéger les occupants ?",
                    "answerOptions": [
                        {"text": "Cellule de survie", "isCorrect": True},
                        {"text": "Zone à absorption d'énergie", "isCorrect": False},
                        {"text": "Châssis séparé", "isCorrect": False},
                        {"text": "Baie de pare-brise", "isCorrect": False}
                    ],
                    "correction": "La cellule de survie (ou cage de sécurité) est renforcée par des aciers à très haute limite élastique (THLE) pour préserver l'espace vital."
                },
                {
                    "questionNumber": 4,
                    "question": "Quel matériau est de plus en plus utilisé en carrosserie pour réduire le poids du véhicule tout en conservant une grande rigidité ?",
                    "answerOptions": [
                        {"text": "Aluminium", "isCorrect": True},
                        {"text": "Plomb", "isCorrect": False},
                        {"text": "Fonte", "isCorrect": False},
                        {"text": "Cuivre", "isCorrect": False}
                    ],
                    "correction": "L'aluminium permet de gagner du poids (consommation réduite) mais nécessite des techniques d'assemblage spécifiques (rivetage/collage)."
                },
                {
                    "questionNumber": 5,
                    "question": "Quelle est la fonction du pied milieu (pied B) dans une structure de caisse autoporteuse ?",
                    "answerOptions": [
                        {"text": "Soutenir le toit et protéger lors d'un choc latéral", "isCorrect": True},
                        {"text": "Porter le moteur sur ses silentblocs", "isCorrect": False},
                        {"text": "Permettre le passage des gaz d'échappement", "isCorrect": False},
                        {"text": "Régler l'alignement des roues avant", "isCorrect": False}
                    ],
                    "correction": "Le pied milieu relie le longeron inférieur au pavillon, assurant la rigidité latérale de l'habitacle."
                },
                {
                    "questionNumber": 6,
                    "question": "Que signifie l'acronyme HLE pour un acier de carrosserie ?",
                    "answerOptions": [
                        {"text": "Haute Limite Élastique", "isCorrect": True},
                        {"text": "Haute Liaison Électrique", "isCorrect": False},
                        {"text": "Homologation Légère Européenne", "isCorrect": False},
                        {"text": "Hauteur Libre d'Entrée", "isCorrect": False}
                    ],
                    "correction": "L'acier HLE offre une résistance mécanique supérieure aux aciers doux, permettant d'utiliser des tôles plus fines pour un même niveau de protection."
                },
                {
                    "questionNumber": 7,
                    "question": "Sur quel type de véhicule trouve-t-on généralement un châssis séparé ?",
                    "answerOptions": [
                        {"text": "Véhicules tout-terrain (4x4) ou utilitaires lourds", "isCorrect": True},
                        {"text": "Voitures citadines légères", "isCorrect": False},
                        {"text": "Voitures de sport monoplaces", "isCorrect": False},
                        {"text": "Voitures hybrides compactes", "isCorrect": False}
                    ],
                    "correction": "Le châssis séparé (échelle) supporte la carrosserie et offre une meilleure résistance aux fortes charges et à la torsion en terrain accidenté."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle pièce de carrosserie amovible ferme l'avant du compartiment moteur ?",
                    "answerOptions": [
                        {"text": "Le capot", "isCorrect": True},
                        {"text": "Le hayon", "isCorrect": False},
                        {"text": "La malle", "isCorrect": False},
                        {"text": "Le pavillon", "isCorrect": False}
                    ],
                    "correction": "Le capot est une pièce amovible articulée par des charnières."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel organe mécanique relie les deux longerons d'une caisse pour rigidifier le train avant ?",
                    "answerOptions": [
                        {"text": "La traverse", "isCorrect": True},
                        {"text": "Le montant", "isCorrect": False},
                        {"text": "L'aile", "isCorrect": False},
                        {"text": "La custode", "isCorrect": False}
                    ],
                    "correction": "La traverse (avant ou arrière) assure l'écartement des longerons et supporte souvent le radiateur ou les boucliers."
                },
                {
                    "questionNumber": 10,
                    "question": "Dans quel but utilise-t-on des tôles d'épaisseurs différentes soudées bout à bout (Tailored Blanks) ?",
                    "answerOptions": [
                        {"text": "Optimiser la déformation et la résistance selon les zones", "isCorrect": True},
                        {"text": "Éviter la corrosion par l'eau de pluie", "isCorrect": False},
                        {"text": "Faciliter le nettoyage après un accident", "isCorrect": False},
                        {"text": "Diminuer le bruit du moteur dans l'habitacle", "isCorrect": False}
                    ],
                    "correction": "Ces flans raboutés permettent d'avoir une tôle épaisse là où la force est nécessaire et fine là où le poids peut être réduit."
                },
                {
                    "questionNumber": 11,
                    "question": "Comment appelle-t-on le revêtement appliqué sur la tôle en usine par électrolyse pour la protéger de la corrosion ?",
                    "answerOptions": [
                        {"text": "La cataphorèse", "isCorrect": True},
                        {"text": "Le ponçage", "isCorrect": False},
                        {"text": "Le lustrage", "isCorrect": False},
                        {"text": "Le masticage", "isCorrect": False}
                    ],
                    "correction": "La cataphorèse est une peinture protectrice appliquée par immersion, atteignant tous les corps creux de la caisse."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle pièce de structure supporte les charnières des portes avant ?",
                    "answerOptions": [
                        {"text": "Le pied avant (pied A)", "isCorrect": True},
                        {"text": "Le passage de roue", "isCorrect": False},
                        {"text": "Le plancher", "isCorrect": False},
                        {"text": "Le pavillon", "isCorrect": False}
                    ],
                    "correction": "Le pied avant assure la liaison entre le tablier, la baie de pare-brise et le bas de caisse."
                },
                {
                    "questionNumber": 13,
                    "question": "Qu'est-ce que le 'joint d'étanchéité' appliqué sur les liaisons de tôles en usine ?",
                    "answerOptions": [
                        {"text": "Un cordon de mastic pour empêcher l'entrée d'eau et d'air", "isCorrect": True},
                        {"text": "Une bande de métal fondue à haute température", "isCorrect": False},
                        {"text": "Un type de peinture décorative mate", "isCorrect": False},
                        {"text": "Un lubrifiant pour faciliter le glissement de l'air", "isCorrect": False}
                    ],
                    "correction": "Les mastics d'étanchéité protègent les zones de soudure et évitent la corrosion entre les tôles superposées."
                },
                {
                    "questionNumber": 14,
                    "question": "Quel est le rôle du renfort de porte (barre anti-intrusion) ?",
                    "answerOptions": [
                        {"text": "Protéger les passagers lors d'un choc latéral", "isCorrect": True},
                        {"text": "Empêcher la porte de grincer à l'ouverture", "isCorrect": False},
                        {"text": "Permettre la fixation du lève-vitre électrique", "isCorrect": False},
                        {"text": "Réduire la buée sur les vitres en hiver", "isCorrect": False}
                    ],
                    "correction": "Située à l'intérieur de la porte, cette barre rigide limite l'enfoncement de la porte dans l'habitacle lors d'un impact."
                },
                {
                    "questionNumber": 15,
                    "question": "De quoi se compose une carrosserie composite sur certains véhicules de sport ?",
                    "answerOptions": [
                        {"text": "De résine et de fibres (verre ou carbone)", "isCorrect": True},
                        {"text": "D'acier doux galvanisé à chaud", "isCorrect": False},
                        {"text": "De bois de hêtre compressé", "isCorrect": False},
                        {"text": "De fonte d'aluminium brute", "isCorrect": False}
                    ],
                    "correction": "Les matériaux composites offrent un rapport poids/résistance exceptionnel."
                },
                {
                    "questionNumber": 16,
                    "question": "Comment appelle-t-on la vitre fixe située à l'arrière des portes arrière ?",
                    "answerOptions": [
                        {"text": "La custode", "isCorrect": True},
                        {"text": "La lunette", "isCorrect": False},
                        {"text": "Le déflecteur", "isCorrect": False},
                        {"text": "Le pare-brise", "isCorrect": False}
                    ],
                    "correction": "La vitre de custode est souvent collée sur le montant de custode à l'arrière du véhicule."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle partie de la structure permet de fixer les éléments de suspension arrière ?",
                    "answerOptions": [
                        {"text": "La traverse arrière ou le faux-châssis", "isCorrect": True},
                        {"text": "Le pied milieu", "isCorrect": False},
                        {"text": "Le renfort de pavillon", "isCorrect": False},
                        {"text": "Le tablier avant", "isCorrect": False}
                    ],
                    "correction": "Les points d'ancrage de suspension sont des zones ultra-renforcées de la caisse."
                },
                {
                    "questionNumber": 18,
                    "question": "Quel est le rôle du pare-chocs (bouclier) moderne ?",
                    "answerOptions": [
                        {"text": "Absorber les petits chocs et protéger les piétons", "isCorrect": True},
                        {"text": "Rigidifier la caisse pour le remorquage", "isCorrect": False},
                        {"text": "Refroidir le moteur par induction forcée", "isCorrect": False},
                        {"text": "Servir de marche-pied pour le mécanicien", "isCorrect": False}
                    ],
                    "correction": "Fabriqués en plastique (PP/EPDM), ils se déforment pour absorber l'énergie et limiter les blessures en cas de collision avec un piéton."
                },
                {
                    "questionNumber": 19,
                    "question": "Que désigne le terme 'caisse à nu' ?",
                    "answerOptions": [
                        {"text": "La structure métallique sans aucun accessoire ni équipement", "isCorrect": True},
                        {"text": "Une voiture sans roues ni moteur uniquement", "isCorrect": False},
                        {"text": "Une carrosserie avant l'application de l'apprêt", "isCorrect": False},
                        {"text": "Le châssis d'un camion sans la cabine", "isCorrect": False}
                    ],
                    "correction": "C'est l'ossature soudée (caisson) sortant de la chaîne de ferrage."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle pièce sépare le compartiment moteur de l'habitacle ?",
                    "answerOptions": [
                        {"text": "Le tablier", "isCorrect": True},
                        {"text": "Le plancher", "isCorrect": False},
                        {"text": "Le pavillon", "isCorrect": False},
                        {"text": "La jupe avant", "isCorrect": False}
                    ],
                    "correction": "Le tablier est une cloison pare-feu transversale qui supporte aussi le tableau de bord et la colonne de direction."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : PRÉPARATION, RÉPARATION ET MISE EN FORME (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : PRÉPARATION, RÉPARATION ET MISE EN FORME",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la première étape indispensable avant de commencer un redressage sur un élément peint ?",
                    "answerOptions": [
                        {"text": "Le décapage de la zone déformée", "isCorrect": True},
                        {"text": "L'application directe de mastic", "isCorrect": False},
                        {"text": "Le passage en cabine de peinture", "isCorrect": False},
                        {"text": "Le lustrage de l'élément entier", "isCorrect": False}
                    ],
                    "correction": "Il faut mettre la tôle à nu pour pouvoir utiliser les outils de tirage (clouteuse) ou de frappe."
                },
                {
                    "questionNumber": 22,
                    "question": "Quel outil manuel utilise le carrossier pour dresser la tôle en frappant par petits coups ?",
                    "answerOptions": [
                        {"text": "Le marteau à planer", "isCorrect": True},
                        {"text": "La massette de maçon", "isCorrect": False},
                        {"text": "Le maillet en bois", "isCorrect": False},
                        {"text": "Le tournevis plat", "isCorrect": False}
                    ],
                    "correction": "Le marteau à planer possède une face polie pour ne pas marquer la tôle lors de la finition."
                },
                {
                    "questionNumber": 23,
                    "question": "À quoi sert un tas de carrossier ?",
                    "answerOptions": [
                        {"text": "De contre-appui lors de la frappe au marteau", "isCorrect": True},
                        {"text": "De récipient pour mélanger le mastic", "isCorrect": False},
                        {"text": "De protection pour les mains du technicien", "isCorrect": False},
                        {"text": "De cale pour soulever le véhicule", "isCorrect": False}
                    ],
                    "correction": "Le tas sert d'enclume portative que l'on place derrière la tôle pour redonner sa forme d'origine."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment appelle-t-on l'outil qui permet de tirer une bosse sans accéder à l'envers de la tôle ?",
                    "answerOptions": [
                        {"text": "Le tire-clou (Spotter)", "isCorrect": True},
                        {"text": "La ventouse à vitrage", "isCorrect": False},
                        {"text": "Le burin pneumatique", "isCorrect": False},
                        {"text": "La pince à dégrafer", "isCorrect": False}
                    ],
                    "correction": "Le tire-clou soude une étoile ou un anneau sur la bosse, permettant de la tirer vers l'extérieur."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est l'inconvénient d'un ponçage à l'eau sur une tôle nue ?",
                    "answerOptions": [
                        {"text": "Risque d'oxydation (rouille) immédiate", "isCorrect": True},
                        {"text": "La tôle devient trop brillante", "isCorrect": False},
                        {"text": "L'abrasif s'use moins vite", "isCorrect": False},
                        {"text": "La poussière devient trop lourde", "isCorrect": False}
                    ],
                    "correction": "L'eau favorise la corrosion instantanée du fer. On privilégie le ponçage à sec avec aspiration."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle opération consiste à supprimer les tensions internes d'une tôle après un choc ?",
                    "answerOptions": [
                        {"text": "Le déshabillage des tensions", "isCorrect": True},
                        {"text": "Le chauffage au rouge", "isCorrect": False},
                        {"text": "Le découpage au plasma", "isCorrect": False},
                        {"text": "Le recouvrement au plomb", "isCorrect": False}
                    ],
                    "correction": "Il faut frapper les points de tension (les 'plis') pour que la bosse principale revienne."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle proportion de durcisseur doit-on mélanger au mastic polyester (en moyenne) ?",
                    "answerOptions": [
                        {"text": "2 à 3 %", "isCorrect": True},
                        {"text": "50 % (moitié/moitié)", "isCorrect": False},
                        {"text": "10 %", "isCorrect": False},
                        {"text": "Un quart du pot", "isCorrect": False}
                    ],
                    "correction": "Un excès de durcisseur provoque des taches dans la peinture finale (saignement), un manque empêche le séchage."
                },
                {
                    "questionNumber": 28,
                    "question": "À quoi sert la 'poudre guide de ponçage' ?",
                    "answerOptions": [
                        {"text": "Visualiser les défauts et les zones non poncées", "isCorrect": True},
                        {"text": "Empêcher le papier de verre de s'encrasser", "isCorrect": False},
                        {"text": "Faire briller le mastic avant l'apprêt", "isCorrect": False},
                        {"text": "Accélérer le séchage du durcisseur", "isCorrect": False}
                    ],
                    "correction": "La poudre noire reste dans les creux et rayures, montrant au carrossier ce qu'il reste à poncer."
                },
                {
                    "questionNumber": 29,
                    "question": "Que doit-on faire après avoir redressé une tôle pour vérifier sa forme ?",
                    "answerOptions": [
                        {"text": "Le contrôle au toucher (la paume de la main)", "isCorrect": True},
                        {"text": "Regarder uniquement avec une lampe", "isCorrect": False},
                        {"text": "Appliquer directement du vernis", "isCorrect": False},
                        {"text": "Prendre une photo", "isCorrect": False}
                    ],
                    "correction": "La main gantée ou nue sent des bosses invisibles à l'œil."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel outil pneumatique est utilisé pour découper proprement les points de soudure d'origine ?",
                    "answerOptions": [
                        {"text": "La dépointeuse", "isCorrect": True},
                        {"text": "La meuleuse d'angle", "isCorrect": False},
                        {"text": "Le marteau piqueur", "isCorrect": False},
                        {"text": "La perceuse à percussion", "isCorrect": False}
                    ],
                    "correction": "La dépointeuse utilise un foret spécifique (fraise à dépointer) pour percer seulement la première tôle."
                },
                {
                    "questionNumber": 31,
                    "question": "Comment appelle-t-on le redressage d'une bosse accessible par l'intérieur sans abîmer la peinture ?",
                    "answerOptions": [
                        {"text": "Le Débosselage Sans Peinture (DSP)", "isCorrect": True},
                        {"text": "Le masticage rapide", "isCorrect": False},
                        {"text": "Le ponçage à sec", "isCorrect": False},
                        {"text": "Le tirage à la chaîne", "isCorrect": False}
                    ],
                    "correction": "Le DSP utilise des tiges métalliques pour repousser la tôle avec précision."
                },
                {
                    "questionNumber": 32,
                    "question": "Quel est le but de 'l'étain' en carrosserie traditionnelle ?",
                    "answerOptions": [
                        {"text": "Garnir une soudure ou un défaut important au métal", "isCorrect": True},
                        {"text": "Protéger les vitres du véhicule", "isCorrect": False},
                        {"text": "Peindre les jantes en gris", "isCorrect": False},
                        {"text": "Coller les emblèmes de la marque", "isCorrect": False}
                    ],
                    "correction": "Le garnissage à l'étain est plus résistant que le mastic mais nécessite un savoir-faire en chauffe."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle précaution faut-il prendre lors du redressage d'un élément en plastique (pare-chocs) ?",
                    "answerOptions": [
                        {"text": "Chauffer modérément la zone avec un décapeur thermique", "isCorrect": True},
                        {"text": "Frapper très fort avec une masse en acier", "isCorrect": False},
                        {"text": "Utiliser de la glace pour durcir le plastique", "isCorrect": False},
                        {"text": "Appliquer de l'acide pour ramollir", "isCorrect": False}
                    ],
                    "correction": "La chaleur rend le plastique malléable, lui permettant de reprendre sa forme initiale."
                },
                {
                    "questionNumber": 34,
                    "question": "Pourquoi doit-on dégraisser une zone avant d'appliquer le mastic ?",
                    "answerOptions": [
                        {"text": "Pour garantir une parfaite adhérence du produit", "isCorrect": True},
                        {"text": "Pour changer la couleur de la tôle", "isCorrect": False},
                        {"text": "Pour refroidir la surface de travail", "isCorrect": False},
                        {"text": "Pour enlever les rayures profondes", "isCorrect": False}
                    ],
                    "correction": "Les traces de doigts ou de gras empêchent le mastic de coller."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel outil permet de vérifier l'alignement des éléments de carrosserie (jeux de portes) ?",
                    "answerOptions": [
                        {"text": "Le réglet ou le jeu de cales (pige)", "isCorrect": True},
                        {"text": "Le pèse-personne", "isCorrect": False},
                        {"text": "La boussole", "isCorrect": False},
                        {"text": "Le thermomètre", "isCorrect": False}
                    ],
                    "correction": "Les jeux et affleurements doivent être constants pour une réparation de qualité."
                },
                {
                    "questionNumber": 36,
                    "question": "En préparation, qu'est-ce que le 'marouflage' ?",
                    "answerOptions": [
                        {"text": "La protection des parties du véhicule qui ne doivent pas être peintes", "isCorrect": True},
                        {"text": "Le mélange de la peinture dans le godet", "isCorrect": False},
                        {"text": "Le ponçage de finition à l'eau", "isCorrect": False},
                        {"text": "Le lavage haute pression du châssis", "isCorrect": False}
                    ],
                    "correction": "On utilise du papier de masquage, du plastique et de l'adhésif."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel défaut apparaît si le mastic est mal poncé (trop épais) ?",
                    "answerOptions": [
                        {"text": "Un spectre ou une bosse visible sous la peinture", "isCorrect": True},
                        {"text": "Une couleur trop claire", "isCorrect": False},
                        {"text": "Une brillance excessive", "isCorrect": False},
                        {"text": "Un trou dans la porte", "isCorrect": False}
                    ],
                    "correction": "Le mastic doit finir à zéro sur les bords pour être invisible."
                },
                {
                    "questionNumber": 38,
                    "question": "À quoi sert la 'lime à épaissir' (fraisée) ?",
                    "answerOptions": [
                        {"text": "Araser les excédents de métal ou d'étain", "isCorrect": True},
                        {"text": "Couper le pare-brise", "isCorrect": False},
                        {"text": "Limer les ongles du carrossier", "isCorrect": False},
                        {"text": "Nettoyer les pneus", "isCorrect": False}
                    ],
                    "correction": "Ses dents courbes permettent d'enlever de la matière sans s'encrasser."
                },
                {
                    "questionNumber": 39,
                    "question": "Comment appelle-t-on la technique consistant à rétracter la tôle 'allongée' ?",
                    "answerOptions": [
                        {"text": "La chaude de retrait", "isCorrect": True},
                        {"text": "Le découpage", "isCorrect": False},
                        {"text": "Le sablage", "isCorrect": False},
                        {"text": "Le collage", "isCorrect": False}
                    ],
                    "correction": "On chauffe ponctuellement au chalumeau ou à l'électrode carbone puis on refroidit brutalement."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle est la fonction d'un 'banc de mesure' (marbre) ?",
                    "answerOptions": [
                        {"text": "Vérifier et rectifier la géométrie de la structure", "isCorrect": True},
                        {"text": "Peser le véhicule après accident", "isCorrect": False},
                        {"text": "Calculer la puissance du moteur", "isCorrect": False},
                        {"text": "Tester l'étanchéité des vitres", "isCorrect": False}
                    ],
                    "correction": "Le marbre permet de redonner ses cotes d'origine au châssis."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : ASSEMBLAGE ET SOUDAGE (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : ASSEMBLAGE ET SOUDAGE",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel est le procédé de soudage le plus utilisé en carrosserie pour l'assemblage des tôles fines ?",
                    "answerOptions": [
                        {"text": "Le soudage MAG (Semi-automatique)", "isCorrect": True},
                        {"text": "Le soudage à l'arc à l'électrode enrobée", "isCorrect": False},
                        {"text": "Le soudage à l'étain", "isCorrect": False},
                        {"text": "Le soudage laser portable", "isCorrect": False}
                    ],
                    "correction": "Le MAG (Metal Active Gas) permet de souder en continu avec un gaz de protection."
                },
                {
                    "questionNumber": 42,
                    "question": "Dans le soudage par résistance (points), quel paramètre est essentiel avec la pression et l'intensité ?",
                    "answerOptions": [
                        {"text": "Le temps de passage du courant", "isCorrect": True},
                        {"text": "Le débit de gaz argon", "isCorrect": False},
                        {"text": "La température de l'atelier", "isCorrect": False},
                        {"text": "La couleur des électrodes", "isCorrect": False}
                    ],
                    "correction": "Le temps de soudage doit être précis pour garantir la fusion sans percer la tôle."
                },
                {
                    "questionNumber": 43,
                    "question": "À quoi sert le gaz de protection en soudage MIG/MAG ?",
                    "answerOptions": [
                        {"text": "Protéger le bain de fusion de l'oxydation de l'air", "isCorrect": True},
                        {"text": "Accélérer le refroidissement de la torche", "isCorrect": False},
                        {"text": "Donner une odeur de propre à l'atelier", "isCorrect": False},
                        {"text": "Éclairer la zone de travail", "isCorrect": False}
                    ],
                    "correction": "Le gaz remplace l'enrobage de l'électrode pour isoler le métal en fusion."
                },
                {
                    "questionNumber": 44,
                    "question": "Quel est l'avantage du brasage MIG (MIG Brazing) par rapport au soudage classique ?",
                    "answerOptions": [
                        {"text": "Moindre échauffement de la tôle et respect du zingage", "isCorrect": True},
                        {"text": "Une solidité dix fois supérieure", "isCorrect": False},
                        {"text": "Pas besoin d'électricité pour fonctionner", "isCorrect": False},
                        {"text": "Soudage possible sous l'eau", "isCorrect": False}
                    ],
                    "correction": "Le brasage utilise un fil d'apport (cuivre-silicium) qui fond à basse température."
                },
                {
                    "questionNumber": 45,
                    "question": "Que doit-on faire sur les tôles avant un soudage par points ?",
                    "answerOptions": [
                        {"text": "Nettoyer et dégraisser les zones de contact", "isCorrect": True},
                        {"text": "Appliquer une peinture épaisse", "isCorrect": False},
                        {"text": "Mettre de l'huile entre les tôles", "isCorrect": False},
                        {"text": "Percer des trous de 10mm partout", "isCorrect": False}
                    ],
                    "correction": "Le courant électrique doit passer librement entre les tôles."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la fonction d'un primaire 'Soudable' (Zinc riche) ?",
                    "answerOptions": [
                        {"text": "Protéger l'intérieur de l'assemblage tout en laissant passer le courant", "isCorrect": True},
                        {"text": "Colorer la soudure en bleu", "isCorrect": False},
                        {"text": "Remplacer totalement le gaz de protection", "isCorrect": False},
                        {"text": "Faciliter le ponçage après soudure", "isCorrect": False}
                    ],
                    "correction": "Il évite la rouille entre les deux tôles superposées après le soudage."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel défaut de soudure est causé par une intensité trop faible ?",
                    "answerOptions": [
                        {"text": "Le manque de pénétration", "isCorrect": True},
                        {"text": "Les projections excessives", "isCorrect": False},
                        {"text": "Le perçage de la tôle", "isCorrect": False},
                        {"text": "La fumée noire", "isCorrect": False}
                    ],
                    "correction": "La soudure reste en surface et n'assure pas la liaison solide."
                },
                {
                    "questionNumber": 48,
                    "question": "Pourquoi utilise-t-on le rivetage/collage sur les véhicules récents ?",
                    "answerOptions": [
                        {"text": "Pour assembler des matériaux différents (ex: alu et acier)", "isCorrect": True},
                        {"text": "Parce que c'est plus joli que la soudure", "isCorrect": False},
                        {"text": "Pour supprimer le besoin de peindre", "isCorrect": False},
                        {"text": "Pour pouvoir démonter la voiture tous les jours", "isCorrect": False}
                    ],
                    "correction": "On ne peut pas souder l'aluminium à l'acier, donc on colle et on rivette."
                },
                {
                    "questionNumber": 49,
                    "question": "Comment appelle-t-on le soudage MAG réalisé à travers des trous percés dans la tôle supérieure ?",
                    "answerOptions": [
                        {"text": "Le bouchonnage", "isCorrect": True},
                        {"text": "Le meulage", "isCorrect": False},
                        {"text": "L'agrafage", "isCorrect": False},
                        {"text": "Le collage thermique", "isCorrect": False}
                    ],
                    "correction": "Cette technique imite le soudage par points d'usine quand on n'a pas accès avec une pince."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le risque de souder près d'un calculateur électronique sans protection ?",
                    "answerOptions": [
                        {"text": "Détruire les composants par surtension", "isCorrect": True},
                        {"text": "Changer la langue de l'autoradio", "isCorrect": False},
                        {"text": "Vider le réservoir d'essence", "isCorrect": False},
                        {"text": "Dégonfler les pneus", "isCorrect": False}
                    ],
                    "correction": "Il faut impérativement débrancher la batterie ou utiliser un parasurtenseur."
                },
                {
                    "questionNumber": 51,
                    "question": "À quoi servent les 'électrodes' sur une soudeuse par points ?",
                    "answerOptions": [
                        {"text": "Transmettre le courant et presser les tôles", "isCorrect": True},
                        {"text": "Apporter le métal en fusion", "isCorrect": False},
                        {"text": "Éclairer le point de soudure", "isCorrect": False},
                        {"text": "Aspirer les fumées de soudage", "isCorrect": False}
                    ],
                    "correction": "Elles sont généralement en cuivre et refroidies par eau ou air."
                },
                {
                    "questionNumber": 52,
                    "question": "En soudage MAG, quelle est la conséquence d'un débit de gaz trop faible ?",
                    "answerOptions": [
                        {"text": "Apparition de porosités (trous) dans le cordon", "isCorrect": True},
                        {"text": "La torche devient trop lourde", "isCorrect": False},
                        {"text": "Le fil sort plus vite", "isCorrect": False},
                        {"text": "La lumière de l'arc devient verte", "isCorrect": False}
                    ],
                    "correction": "L'oxygène de l'air 'brûle' le métal en fusion, créant des bulles d'air."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la règle pour la distance entre deux points de soudure de réparation ?",
                    "answerOptions": [
                        {"text": "Respecter le nombre et l'emplacement d'origine", "isCorrect": True},
                        {"text": "Mettre deux fois plus de points qu'à l'origine", "isCorrect": False},
                        {"text": "Faire un seul gros point au milieu", "isCorrect": False},
                        {"text": "Souder uniquement les bords extérieurs", "isCorrect": False}
                    ],
                    "correction": "Le carrossier doit reproduire les caractéristiques de l'assemblage constructeur."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle opération suit immédiatement la soudure d'un élément ?",
                    "answerOptions": [
                        {"text": "Le meulage de l'excédent (si nécessaire) et la protection anticorrosion", "isCorrect": True},
                        {"text": "Le lavage au jet d'eau froide", "isCorrect": False},
                        {"text": "L'application de cire de protection", "isCorrect": False},
                        {"text": "Le montage des pneus", "isCorrect": False}
                    ],
                    "correction": "La soudure brûle les protections, il faut donc traiter le métal nu rapidement."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel masque est obligatoire pour le soudage à l'arc ?",
                    "answerOptions": [
                        {"text": "Un masque à cristaux liquides ou verre teinté (DIN 11-13)", "isCorrect": True},
                        {"text": "Des lunettes de soleil classiques", "isCorrect": False},
                        {"text": "Un simple masque anti-poussière", "isCorrect": False},
                        {"text": "Aucun si on ferme les yeux", "isCorrect": False}
                    ],
                    "correction": "La lumière de l'arc provoque des brûlures graves de la rétine (coup d'arc)."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est le rôle du 'fil de masse' sur un poste à souder ?",
                    "answerOptions": [
                        {"text": "Fermer le circuit électrique", "isCorrect": True},
                        {"text": "Transporter le gaz vers la torche", "isCorrect": False},
                        {"text": "Soutenir le poste sur ses roues", "isCorrect": False},
                        {"text": "Empêcher le fil de s'emmêler", "isCorrect": False}
                    ],
                    "correction": "La pince de masse doit être placée au plus près de la zone de soudure."
                },
                {
                    "questionNumber": 57,
                    "question": "En soudage MAG, que se passe-t-il si la torche est trop loin de la pièce ?",
                    "answerOptions": [
                        {"text": "Mauvaise protection gazeuse et projections", "isCorrect": True},
                        {"text": "Le fil s'arrête de sortir", "isCorrect": False},
                        {"text": "L'arc devient bleu", "isCorrect": False},
                        {"text": "La tôle refroidit instantanément", "isCorrect": False}
                    ],
                    "correction": "Il faut maintenir une distance constante (environ 10-15 mm)."
                },
                {
                    "questionNumber": 58,
                    "question": "Qu'est-ce qu'une 'pénétration' en soudage ?",
                    "answerOptions": [
                        {"text": "La profondeur atteinte par la fusion dans l'épaisseur de la tôle", "isCorrect": True},
                        {"text": "Le fait de percer un trou avec la torche", "isCorrect": False},
                        {"text": "L'insertion du fil dans le dévidoir", "isCorrect": False},
                        {"text": "La largeur du cordon de soudure", "isCorrect": False}
                    ],
                    "correction": "Une bonne pénétration garantit que les deux pièces sont fondues ensemble sur toute l'épaisseur."
                },
                {
                    "questionNumber": 59,
                    "question": "Dans quel cas utilise-t-on le collage structural seul ?",
                    "answerOptions": [
                        {"text": "Sur certains panneaux de toit ou garnitures intérieures", "isCorrect": True},
                        {"text": "Pour fixer les longerons moteur", "isCorrect": False},
                        {"text": "Pour attacher les roues au moyeu", "isCorrect": False},
                        {"text": "C'est interdit en carrosserie", "isCorrect": False}
                    ],
                    "correction": "La colle structurelle est très performante mais souvent associée à des points ou rivets sur les zones porteuses."
                },
                {
                    "questionNumber": 60,
                    "question": "Pourquoi doit-on utiliser une couverture anti-feu lors du soudage ?",
                    "answerOptions": [
                        {"text": "Protéger les vitres et l'intérieur du véhicule contre les projections", "isCorrect": True},
                        {"text": "Tenir chaud au carrossier en hiver", "isCorrect": False},
                        {"text": "Cacher le travail au client", "isCorrect": False},
                        {"text": "Éteindre le poste en fin de journée", "isCorrect": False}
                    ],
                    "correction": "Les étincelles de meulage ou de soudage brûlent instantanément les tissus et marquent les vitres."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : AMÉNAGEMENT, MÉCANIQUE ET ÉQUIPEMENTS (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : AMÉNAGEMENT, MÉCANIQUE ET ÉQUIPEMENTS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle précaution doit-on prendre avant de déposer un airbag ?",
                    "answerOptions": [
                        {"text": "Débrancher la batterie et attendre le temps de décharge", "isCorrect": True},
                        {"text": "Percer le sac pour vider l'air", "isCorrect": False},
                        {"text": "Porter des bouchons d'oreilles", "isCorrect": False},
                        {"text": "Laver l'airbag à l'eau savonneuse", "isCorrect": False}
                    ],
                    "correction": "Un déclenchement accidentel peut être mortel. L'attente permet aux condensateurs de se vider."
                },
                {
                    "questionNumber": 62,
                    "question": "Quel fluide doit être impérativement récupéré par une machine spécifique avant de démonter un radiateur de climatisation ?",
                    "answerOptions": [
                        {"text": "Le gaz frigorigène (R134a ou R1234yf)", "isCorrect": True},
                        {"text": "Le liquide de refroidissement rouge", "isCorrect": False},
                        {"text": "L'huile de direction assistée", "isCorrect": False},
                        {"text": "L'eau du lave-glace", "isCorrect": False}
                    ],
                    "correction": "Le gaz de clim est polluant et sous pression. Son rejet à l'air libre est interdit."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on le réglage de l'alignement des optiques de phares ?",
                    "answerOptions": [
                        {"text": "Le réglage au réglo-phare", "isCorrect": True},
                        {"text": "Le parallélisme", "isCorrect": False},
                        {"text": "Le carrossage", "isCorrect": False},
                        {"text": "L'équilibrage", "isCorrect": False}
                    ],
                    "correction": "Un phare mal réglé éblouit ou n'éclaire pas assez, ce qui est un motif de refus au contrôle technique."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle opération mécanique est souvent nécessaire après le remplacement d'un élément de suspension suite à un choc ?",
                    "answerOptions": [
                        {"text": "Le contrôle de la géométrie des trains", "isCorrect": True},
                        {"text": "La vidange du moteur", "isCorrect": False},
                        {"text": "Le remplacement de la batterie", "isCorrect": False},
                        {"text": "Le nettoyage du filtre à air", "isCorrect": False}
                    ],
                    "correction": "Un choc peut tordre un bras de suspension et fausser le parallélisme, usant les pneus prématurément."
                },
                {
                    "questionNumber": 65,
                    "question": "À quoi sert le liquide de refroidissement ?",
                    "answerOptions": [
                        {"text": "Évacuer la chaleur du moteur et protéger contre le gel", "isCorrect": True},
                        {"text": "Lubrifier les pistons à l'intérieur du moteur", "isCorrect": False},
                        {"text": "Nettoyer le pare-brise automatiquement", "isCorrect": False},
                        {"text": "Rendre le freinage plus puissant", "isCorrect": False}
                    ],
                    "correction": "Il circule entre le moteur et le radiateur."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on les fixations plastiques qui tiennent les garnitures de portes ?",
                    "answerOptions": [
                        {"text": "Les agrafes ou clips", "isCorrect": True},
                        {"text": "Les rivets pop", "isCorrect": False},
                        {"text": "Les vis Parker", "isCorrect": False},
                        {"text": "Les boulons", "isCorrect": False}
                    ],
                    "correction": "Elles sont souvent à usage unique car elles cassent au démontage."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le rôle du lève-vitre ?",
                    "answerOptions": [
                        {"text": "Permettre la montée et la descente de la vitre latérale", "isCorrect": True},
                        {"text": "Nettoyer la vitre lors de la descente", "isCorrect": False},
                        {"text": "Bloquer la vitre en cas de vol", "isCorrect": False},
                        {"text": "Réparer les impacts de gravillons", "isCorrect": False}
                    ],
                    "correction": "Il peut être manuel (manivelle) ou électrique (moteur)."
                },
                {
                    "questionNumber": 68,
                    "question": "Où se trouve généralement le filtre d'habitacle (filtre à pollen) ?",
                    "answerOptions": [
                        {"text": "Dans le circuit de ventilation/chauffage", "isCorrect": True},
                        {"text": "À l'intérieur du pot d'échappement", "isCorrect": False},
                        {"text": "Sous le siège conducteur", "isCorrect": False},
                        {"text": "Dans le réservoir de carburant", "isCorrect": False}
                    ],
                    "correction": "Il doit être remplacé régulièrement pour garantir la qualité de l'air à bord."
                },
                {
                    "questionNumber": 69,
                    "question": "Qu'est-ce qu'un 'capteur de stationnement' ?",
                    "answerOptions": [
                        {"text": "Un capteur ultrason détectant les obstacles", "isCorrect": True},
                        {"text": "Un appareil qui compte les places de parking", "isCorrect": False},
                        {"text": "Un radar de vitesse pour l'atelier", "isCorrect": False},
                        {"text": "Un bouton pour fermer les portes", "isCorrect": False}
                    ],
                    "correction": "Ils sont souvent intégrés dans les boucliers avant et arrière."
                },
                {
                    "questionNumber": 70,
                    "question": "À quoi sert la 'serrure centralisée' ?",
                    "answerOptions": [
                        {"text": "Verrouiller ou déverrouiller toutes les portes simultanément", "isCorrect": True},
                        {"text": "Empêcher le moteur de démarrer sans clé", "isCorrect": False},
                        {"text": "Régler la hauteur du volant", "isCorrect": False},
                        {"text": "Ouvrir le toit ouvrant à distance", "isCorrect": False}
                    ],
                    "correction": "Elle est pilotée par un boîtier électronique et des moteurs électriques dans chaque porte."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est la particularité du liquide de frein (DOT 4) ?",
                    "answerOptions": [
                        {"text": "Il est très corrosif pour la peinture", "isCorrect": True},
                        {"text": "Il est comestible et sans danger", "isCorrect": False},
                        {"text": "Il peut être remplacé par de l'eau savonneuse", "isCorrect": False},
                        {"text": "Il durcit à la lumière du soleil", "isCorrect": False}
                    ],
                    "correction": "En cas de projection sur la carrosserie, il faut rincer immédiatement à grande eau."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel élément permet de maintenir le capot ouvert en sécurité ?",
                    "answerOptions": [
                        {"text": "La béquille ou le vérin d'équilibrage", "isCorrect": True},
                        {"text": "Le câble d'ouverture", "isCorrect": False},
                        {"text": "Le crochet de sécurité", "isCorrect": False},
                        {"text": "Le balai d'essuie-glace", "isCorrect": False}
                    ],
                    "correction": "Un vérin fatigué doit être remplacé pour éviter la fermeture accidentelle."
                },
                {
                    "questionNumber": 73,
                    "question": "Qu'est-ce que le 'CAN-Bus' dans un véhicule ?",
                    "answerOptions": [
                        {"text": "Le réseau de communication entre les calculateurs", "isCorrect": True},
                        {"text": "Un type d'autocar de transport", "isCorrect": False},
                        {"text": "Le réservoir de lave-glace", "isCorrect": False},
                        {"text": "La courroie de distribution", "isCorrect": False}
                    ],
                    "correction": "Il permet de multiplexer les informations (vitesse, température, etc.) sur deux fils."
                },
                {
                    "questionNumber": 74,
                    "question": "Pourquoi doit-on utiliser une clé dynamométrique ?",
                    "answerOptions": [
                        {"text": "Pour serrer un boulon à un couple précis défini par le constructeur", "isCorrect": True},
                        {"text": "Pour dévisser des vis rouillées très fort", "isCorrect": False},
                        {"text": "Pour mesurer le diamètre d'une vis", "isCorrect": False},
                        {"text": "Pour percer des trous dans l'acier", "isCorrect": False}
                    ],
                    "correction": "Un serrage excessif peut casser la vis, un serrage insuffisant peut provoquer un desserrage."
                },
                {
                    "questionNumber": 75,
                    "question": "À quoi servent les 'pattes de fixation' des optiques ?",
                    "answerOptions": [
                        {"text": "Maintenir le phare sur la structure du véhicule", "isCorrect": True},
                        {"text": "Changer la couleur de l'ampoule", "isCorrect": False},
                        {"text": "Aérer l'intérieur de l'optique", "isCorrect": False},
                        {"text": "Supporter le poids de l'aile avant", "isCorrect": False}
                    ],
                    "correction": "Certaines marques vendent des kits de réparation pour ces pattes si elles cassent lors d'un petit choc."
                },
                {
                    "questionNumber": 76,
                    "question": "Qu'est-ce qu'un 'joint d'étanchéité de porte' ?",
                    "answerOptions": [
                        {"text": "Un profilé caoutchouc empêchant l'eau et le bruit d'entrer", "isCorrect": True},
                        {"text": "Une bande de métal soudée sur le bas de caisse", "isCorrect": False},
                        {"text": "Un autocollant décoratif sur la vitre", "isCorrect": False},
                        {"text": "Une pièce mécanique pour fermer la porte", "isCorrect": False}
                    ],
                    "correction": "Il doit être nettoyé et parfois siliconé pour ne pas coller en hiver."
                },
                {
                    "questionNumber": 77,
                    "question": "Que signifie un voyant orange 'Airbag' allumé au tableau de bord ?",
                    "answerOptions": [
                        {"text": "Un défaut dans le système de sécurité (airbags ou prétensionneurs)", "isCorrect": True},
                        {"text": "Que le sac est prêt à être gonflé manuellement", "isCorrect": False},
                        {"text": "Que la température intérieure est trop élevée", "isCorrect": False},
                        {"text": "C'est un rappel pour changer les pneus", "isCorrect": False}
                    ],
                    "correction": "Le système est hors service tant que le défaut n'est pas effacé."
                },
                {
                    "questionNumber": 78,
                    "question": "Quel outil permet de lire les codes défauts d'un véhicule ?",
                    "answerOptions": [
                        {"text": "L'outil de diagnostic (valise)", "isCorrect": True},
                        {"text": "Le multimètre", "isCorrect": False},
                        {"text": "Le microscope électronique", "isCorrect": False},
                        {"text": "Le tournevis testeur", "isCorrect": False}
                    ],
                    "correction": "Elle se branche sur la prise OBD (On Board Diagnostic)."
                },
                {
                    "questionNumber": 79,
                    "question": "À quoi sert le prétensionneur de ceinture ?",
                    "answerOptions": [
                        {"text": "Plaquer le passager au siège lors d'un choc", "isCorrect": True},
                        {"text": "Rendre la ceinture plus confortable en ville", "isCorrect": False},
                        {"text": "Aider à détacher la ceinture après l'arrêt", "isCorrect": False},
                        {"text": "Nettoyer la sangle de ceinture automatiquement", "isCorrect": False}
                    ],
                    "correction": "C'est un dispositif pyrotechnique qui se déclenche millisecondes avant l'airbag."
                },
                {
                    "questionNumber": 80,
                    "question": "Pourquoi doit-on protéger les garnitures intérieures lors des travaux de carrosserie ?",
                    "answerOptions": [
                        {"text": "Éviter les salissures de poussière, gras ou étincelles", "isCorrect": True},
                        {"text": "Pour qu'elles ne s'envolent pas lors du roulage", "isCorrect": False},
                        {"text": "Pour augmenter le prix de la facture", "isCorrect": False},
                        {"text": "C'est inutile", "isCorrect": False}
                    ],
                    "correction": "Le respect du véhicule client est un gage de professionnalisme."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : SANTÉ, SÉCURITÉ ET ENVIRONNEMENT (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : SANTÉ, SÉCURITÉ ET ENVIRONNEMENT",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel type d'extincteur est le plus adapté pour un feu de métaux ou électrique dans un atelier ?",
                    "answerOptions": [
                        {"text": "Poudre polyvalente (ABC) ou CO2", "isCorrect": True},
                        {"text": "Eau pulvérisée avec additif", "isCorrect": False},
                        {"text": "Sable humide", "isCorrect": False},
                        {"text": "Tuyau d'arrosage classique", "isCorrect": False}
                    ],
                    "correction": "L'eau conduit l'électricité et peut aggraver un feu de produits chimiques."
                },
                {
                    "questionNumber": 82,
                    "question": "Quelle maladie professionnelle est liée à l'inhalation prolongée de poussières de ponçage sans protection ?",
                    "answerOptions": [
                        {"text": "Troubles respiratoires (asthme, silicose)", "isCorrect": True},
                        {"text": "Perte de l'audition", "isCorrect": False},
                        {"text": "Problèmes de vue", "isCorrect": False},
                        {"text": "Caries dentaires", "isCorrect": False}
                    ],
                    "correction": "Le port du masque FFP2 ou FFP3 est indispensable lors du ponçage."
                },
                {
                    "questionNumber": 83,
                    "question": "Où doit-on évacuer les solvants et diluants usagés ?",
                    "answerOptions": [
                        {"text": "Dans des fûts de récupération pour produits chimiques (DID)", "isCorrect": True},
                        {"text": "Dans l'évier avec beaucoup d'eau", "isCorrect": False},
                        {"text": "Dans la benne à ferraille", "isCorrect": False},
                        {"text": "Dans le caniveau de l'atelier", "isCorrect": False}
                    ],
                    "correction": "Les Déchets Industriels Dangereux (DID) doivent être traités par une entreprise spécialisée."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est le danger principal de l'isocyanure contenu dans certains durcisseurs de peinture ?",
                    "answerOptions": [
                        {"text": "Forte toxicité respiratoire et allergisante", "isCorrect": True},
                        {"text": "Il rend la peinture trop brillante", "isCorrect": False},
                        {"text": "Il fait fondre le plastique du pistolet", "isCorrect": False},
                        {"text": "Il attire les insectes dans la cabine", "isCorrect": False}
                    ],
                    "correction": "Le port du masque à cartouches (charbon actif) est obligatoire pour manipuler ces produits."
                },
                {
                    "questionNumber": 85,
                    "question": "Que signifie le marquage 'EPI' sur un équipement ?",
                    "answerOptions": [
                        {"text": "Équipement de Protection Individuelle", "isCorrect": True},
                        {"text": "Étude des Peintures Industrielles", "isCorrect": False},
                        {"text": "Entretien de Protection Interne", "isCorrect": False},
                        {"text": "Écran de Protection Intégré", "isCorrect": False}
                    ],
                    "correction": "Ce sont les accessoires portés par le technicien (gants, lunettes, masque)."
                },
                {
                    "questionNumber": 86,
                    "question": "Quelle est la règle de sécurité lors de l'utilisation d'un pont élévateur ?",
                    "answerOptions": [
                        {"text": "Vérifier le positionnement des patins et actionner les sécurités mécaniques", "isCorrect": True},
                        {"text": "Rester à l'intérieur du véhicule pendant la montée", "isCorrect": False},
                        {"text": "Graisser les patins avec de l'huile moteur", "isCorrect": False},
                        {"text": "Monter le pont le plus vite possible", "isCorrect": False}
                    ],
                    "correction": "Un mauvais positionnement peut entraîner la chute mortelle du véhicule."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment doit-on manipuler les batteries au plomb usagées ?",
                    "answerOptions": [
                        {"text": "Porter des gants et les stocker dans un bac étanche à l'acide", "isCorrect": True},
                        {"text": "Les vider dans l'évier avant de les jeter", "isCorrect": False},
                        {"text": "Les casser pour récupérer le plomb", "isCorrect": False},
                        {"text": "Les brûler pour supprimer l'acide", "isCorrect": False}
                    ],
                    "correction": "L'acide sulfurique est extrêmement corrosif et toxique."
                },
                {
                    "questionNumber": 88,
                    "question": "Pourquoi est-il interdit de manger dans l'atelier de carrosserie ?",
                    "answerOptions": [
                        {"text": "Risque d'ingestion accidentelle de produits toxiques ou poussières", "isCorrect": True},
                        {"text": "Pour ne pas salir le sol propre", "isCorrect": False},
                        {"text": "Parce que le patron ne veut pas", "isCorrect": False},
                        {"text": "Car le bruit empêche de digérer", "isCorrect": False}
                    ],
                    "correction": "L'hygiène au travail sépare strictement les zones de repas et de production."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel est le rôle d'une fontaine de dégraissage biologique ?",
                    "answerOptions": [
                        {"text": "Nettoyer les pièces avec des micro-organismes sans solvants nocifs", "isCorrect": True},
                        {"text": "Donner de l'eau potable aux ouvriers", "isCorrect": False},
                        {"text": "Laver les chiffons de l'atelier", "isCorrect": False},
                        {"text": "Peindre les petites pièces par immersion", "isCorrect": False}
                    ],
                    "correction": "Elle préserve la santé de l'opérateur et l'environnement."
                },
                {
                    "questionNumber": 90,
                    "question": "Que faire en cas de projection de produit chimique dans l'œil ?",
                    "answerOptions": [
                        {"text": "Rincer abondamment à l'eau claire ou avec un rince-œil pendant 15 min", "isCorrect": True},
                        {"text": "Frotter l'œil avec un chiffon sec", "isCorrect": False},
                        {"text": "Mettre du savon pour neutraliser", "isCorrect": False},
                        {"text": "Fermer l'œil et attendre que ça passe", "isCorrect": False}
                    ],
                    "correction": "La rapidité du rinçage est vitale pour éviter des lésions irréversibles."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel risque prévient-on en portant des gants en nitrile plutôt qu'en latex lors de la manipulation de solvants ?",
                    "answerOptions": [
                        {"text": "La dégradation du gant par les produits chimiques", "isCorrect": True},
                        {"text": "La sudation excessive des mains", "isCorrect": False},
                        {"text": "Le vol du gant par les collègues", "isCorrect": False},
                        {"text": "Le changement de couleur de la peau", "isCorrect": False}
                    ],
                    "correction": "Le nitrile offre une meilleure résistance chimique aux hydrocarbures."
                },
                {
                    "questionNumber": 92,
                    "question": "Sur un panneau de signalisation de sécurité, que signifie la couleur jaune/noire ?",
                    "answerOptions": [
                        {"text": "Un avertissement ou un danger", "isCorrect": True},
                        {"text": "Une obligation", "isCorrect": False},
                        {"text": "Une interdiction", "isCorrect": False},
                        {"text": "Un secours (sortie de secours)", "isCorrect": False}
                    ],
                    "correction": "Le triangle jaune avertit d'un risque (ex: électricité, produit toxique)."
                },
                {
                    "questionNumber": 93,
                    "question": "Quel est le but des chaussures de sécurité S3 en carrosserie ?",
                    "answerOptions": [
                        {"text": "Protéger contre l'écrasement, la perforation et l'humidité", "isCorrect": True},
                        {"text": "Être à la mode dans l'atelier", "isCorrect": False},
                        {"text": "Permettre de courir plus vite", "isCorrect": False},
                        {"text": "Remplacer les chaussettes en hiver", "isCorrect": False}
                    ],
                    "correction": "Elles possèdent une coque en acier et une semelle anti-perforation."
                },
                {
                    "questionNumber": 94,
                    "question": "Qu'est-ce qu'une FDS (Fiche de Données de Sécurité) ?",
                    "answerOptions": [
                        {"text": "Un document détaillant les risques et précautions d'un produit", "isCorrect": True},
                        {"text": "La facture d'achat du produit", "isCorrect": False},
                        {"text": "Le mode d'emploi pour peindre une voiture", "isCorrect": False},
                        {"text": "Une fiche de présence des employés", "isCorrect": False}
                    ],
                    "correction": "Elle doit être accessible à tous les salariés manipulant le produit."
                },
                {
                    "questionNumber": 95,
                    "question": "Pourquoi est-il interdit de porter une bague ou une montre lors du démontage mécanique ?",
                    "answerOptions": [
                        {"text": "Risque d'accrochage ou de court-circuit électrique", "isCorrect": True},
                        {"text": "Risque de rayer le bijou", "isCorrect": False},
                        {"text": "C'est une règle religieuse", "isCorrect": False},
                        {"text": "Pour ne pas être en retard", "isCorrect": False}
                    ],
                    "correction": "Une bague peut provoquer l'arrachement d'un doigt si elle se coince (effet bague)."
                },
                {
                    "questionNumber": 96,
                    "question": "À quoi sert le bouton 'Arrêt d'urgence' sur une machine ?",
                    "answerOptions": [
                        {"text": "Couper immédiatement l'énergie en cas de danger", "isCorrect": True},
                        {"text": "Mettre la machine en veille pour la nuit", "isCorrect": False},
                        {"text": "Réglage de la vitesse de rotation", "isCorrect": False},
                        {"text": "Allumer la lumière de l'atelier", "isCorrect": False}
                    ],
                    "correction": "Il est rouge sur fond jaune et doit être testé régulièrement."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le risque de travailler sur un véhicule hybride/électrique sans habilitation ?",
                    "answerOptions": [
                        {"text": "L'électrocution mortelle par haute tension", "isCorrect": True},
                        {"text": "Vider la batterie par erreur", "isCorrect": False},
                        {"text": "Changer la station radio", "isCorrect": False},
                        {"text": "Dégonfler les pneus", "isCorrect": False}
                    ],
                    "correction": "Les câbles oranges transportent des tensions allant jusqu'à 600V."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le risque principal lors de l'utilisation d'une meuleuse d'angle sans carter de protection ?",
                    "answerOptions": [
                        {"text": "Éclatement du disque et projection de morceaux", "isCorrect": True},
                        {"text": "Surchauffe du moteur électrique", "isCorrect": False},
                        {"text": "Usure prématurée du disque abrasif", "isCorrect": False},
                        {"text": "Bruit excessif pour les collègues", "isCorrect": False}
                    ],
                    "correction": "L'absence de carter expose l'opérateur à des projectiles mortels si le disque casse."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel filtre doit équiper le masque respiratoire pour se protéger des vapeurs organiques de peinture ?",
                    "answerOptions": [
                        {"text": "A2", "isCorrect": True},
                        {"text": "P1", "isCorrect": False},
                        {"text": "P2", "isCorrect": False},
                        {"text": "P3", "isCorrect": False}
                    ],
                    "correction": "Les filtres de type 'A' (bande marron) sont conçus pour arrêter les gaz et vapeurs organiques."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle précaution prendre concernant les vêtements de travail synthétiques (nylon, polaire) en cabine de peinture ?",
                    "answerOptions": [
                        {"text": "Ils sont interdits car ils génèrent de l'électricité statique", "isCorrect": True},
                        {"text": "Ils sont recommandés car ils sèchent vite", "isCorrect": False},
                        {"text": "Ils sont obligatoires car moins chers que le coton", "isCorrect": False},
                        {"text": "Ils sont conseillés pour leur esthétique", "isCorrect": False}
                    ],
                    "correction": "L'électricité statique attire la poussière sur la peinture fraîche et peut provoquer des étincelles explosives."
                }
            ]
        }
    }
}