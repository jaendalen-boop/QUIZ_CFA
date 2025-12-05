# Fichier : quiz_cap_peintre_100.py

quiz_data = {
    "title": "Quiz CAP Peintre Applicateur de Revêtement : Révisions Complètes (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : HYGIÈNE, SÉCURITÉ ET RÉGLEMENTATION (Q. 1-20)
        # =========================================================================
        1: {
            "name": "1. Hygiène, Sécurité et Réglementation (Q. 1-20)",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel est l'Équipement de Protection Individuelle (EPI) indispensable lors du ponçage d'un mur ou de l'utilisation d'un enduit pulvérulent ?",
                    "answerOptions": [
                        {"text": "Des gants en cuir.", "isCorrect": False},
                        {"text": "Un Masque respiratoire (P2 ou P3) et des lunettes de protection (contre la poussière et les projections).", "isCorrect": True},
                        {"text": "Un casque anti-bruit.", "isCorrect": False},
                        {"text": "Des bottes en caoutchouc.", "isCorrect": False}
                    ],
                    "correction": "Le **masque** protège les voies respiratoires des particules fines d'enduit et de poussière."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel est le risque principal lié à l'utilisation des **solvants organiques** (white-spirit, diluants pour peinture glycéro) en milieu fermé ?",
                    "answerOptions": [
                        {"text": "Un risque de brûlure électrique.", "isCorrect": False},
                        {"text": "Un risque d'intoxication (inhalation de COV) et un risque d'incendie/explosion (produit inflammable).", "isCorrect": True},
                        {"text": "Un risque de chute de hauteur.", "isCorrect": False},
                        {"text": "Un risque de coupure.", "isCorrect": False}
                    ],
                    "correction": "Une **ventilation** adéquate est vitale lors de l'usage de produits à forte teneur en COV (Composés Organiques Volatils)."
                },
                {
                    "questionNumber": 3,
                    "question": "Quelle est la hauteur à partir de laquelle le travail sans protection antichute (garde-corps, harnais) sur un échafaudage est strictement interdit ?",
                    "answerOptions": [
                        {"text": "50 cm.", "isCorrect": False},
                        {"text": "À partir de 2 mètres de hauteur (ou de plain-pied si le risque de chute est important).", "isCorrect": True},
                        {"text": "10 mètres.", "isCorrect": False},
                        {"text": "1 mètre.", "isCorrect": False}
                    ],
                    "correction": "La **sécurité en hauteur** est une priorité, en particulier sur un échafaudage ou une plate-forme individuelle roulante (PIRL)."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle doit être la procédure pour éliminer les **déchets de peinture glycéro** (solvants, restes) ?",
                    "answerOptions": [
                        {"text": "Les jeter à l'égout ou dans la nature.", "isCorrect": False},
                        {"text": "Les collecter dans des contenants étanches, les identifier et les déposer dans une déchetterie professionnelle (déchets dangereux) ou une filière DEEE.", "isCorrect": True},
                        {"text": "Les mettre dans la poubelle ménagère.", "isCorrect": False},
                        {"text": "Les brûler.", "isCorrect": False}
                    ],
                    "correction": "Les produits chimiques doivent suivre une filière de **déchets dangereux** (catégorie DIB)."
                },
                {
                    "questionNumber": 5,
                    "question": "Que signifie le pictogramme de sécurité représentant une **flamme sur un cercle** ?",
                    "answerOptions": [
                        {"text": "Produit toxique.", "isCorrect": False},
                        {"text": "Comburant (produit qui peut provoquer ou aggraver un incendie).", "isCorrect": True},
                        {"text": "Gaz sous pression.", "isCorrect": False},
                        {"text": "Inflammable.", "isCorrect": False}
                    ],
                    "correction": "Le **comburant** (ex : peroxyde) augmente la puissance d'un feu."
                },
                {
                    "questionNumber": 6,
                    "question": "Quel est le rôle du **Plan de Prévention** sur un chantier ?",
                    "answerOptions": [
                        {"text": "Définir les couleurs.", "isCorrect": False},
                        {"text": "Identifier les risques d'interférence entre l'entreprise de peinture et les autres corps de métier, et définir les mesures de sécurité communes à prendre.", "isCorrect": True},
                        {"text": "Calculer le métré.", "isCorrect": False},
                        {"text": "Organiser la pause déjeuner.", "isCorrect": False}
                    ],
                    "correction": "Le **Plan de Prévention** est obligatoire dès qu'une entreprise extérieure intervient sur un site."
                },
                {
                    "questionNumber": 7,
                    "question": "Que doit-on faire en cas de projection de peinture ou de solvant dans l'œil ?",
                    "answerOptions": [
                        {"text": "Frotter l'œil énergiquement.", "isCorrect": False},
                        {"text": "Rincer immédiatement et abondamment à l'eau claire (douche oculaire si disponible) pendant au moins 15 minutes, puis consulter un médecin.", "isCorrect": True},
                        {"text": "Mettre des gouttes de collyre sans rincer.", "isCorrect": False},
                        {"text": "Attendre que cela passe.", "isCorrect": False}
                    ],
                    "correction": "Le **rinçage** est la première action à effectuer en cas d'accident chimique."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est l'importance de vérifier l'**état des sols** avant l'installation d'un échafaudage roulant ?",
                    "answerOptions": [
                        {"text": "Vérifier la couleur.", "isCorrect": False},
                        {"text": "S'assurer qu'il est plat, stable, non glissant et capable de supporter la charge (éviter le basculement).", "isCorrect": True},
                        {"text": "Mesurer la hauteur.", "isCorrect": False},
                        {"text": "Le nettoyer.", "isCorrect": False}
                    ],
                    "correction": "La **stabilité** de l'échafaudage est une règle de sécurité fondamentale."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le type de peinture qui représente le moins de danger en termes d'émanations de COV (Composés Organiques Volatils) ?",
                    "answerOptions": [
                        {"text": "La peinture glycérophtalique (glycéro).", "isCorrect": False},
                        {"text": "La Peinture en phase aqueuse (acrylique, naturelle) qui contient de l'eau comme diluant principal.", "isCorrect": True},
                        {"text": "La peinture époxy.", "isCorrect": False},
                        {"text": "La peinture bi-composant.", "isCorrect": False}
                    ],
                    "correction": "Les peintures **acryliques** sont préférées pour l'intérieur car elles sont moins nocives."
                },
                {
                    "questionNumber": 10,
                    "question": "Que doit-on faire de l'**eau de rinçage** des outils ayant servi à appliquer des peintures acryliques ?",
                    "answerOptions": [
                        {"text": "La jeter dans le jardin.", "isCorrect": False},
                        {"text": "La décantation (laisser reposer l'eau pour que les pigments se séparent) puis éliminer l'eau claire et envoyer les boues au centre de traitement adapté.", "isCorrect": True},
                        {"text": "La boire.", "isCorrect": False},
                        {"text": "La réutiliser sans traitement.", "isCorrect": False}
                    ],
                    "correction": "Même la phase aqueuse ne doit pas être rejetée à l'égout à cause des pigments qu'elle contient (**décantation** obligatoire)."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle est la première chose à faire avant de manipuler un produit chimique dont on ne connaît pas les risques ?",
                    "answerOptions": [
                        {"text": "Le sentir.", "isCorrect": False},
                        {"text": "Consulter la Fiche de Données de Sécurité (FDS) pour connaître les dangers et les mesures de prévention (EPI à utiliser).", "isCorrect": True},
                        {"text": "Le tester sur la peau.", "isCorrect": False},
                        {"text": "Le mélanger à un autre produit.", "isCorrect": False}
                    ],
                    "correction": "La **FDS** est le document de référence sur les dangers et la manipulation."
                },
                {
                    "questionNumber": 12,
                    "question": "Comment s'appelle la maladie professionnelle respiratoire liée à l'inhalation de poussière de silice, courante dans le BTP et la préparation des supports non protégée ?",
                    "answerOptions": [
                        {"text": "L'asthme.", "isCorrect": False},
                        {"text": "La Silicose.", "isCorrect": True},
                        {"text": "Le cancer du poumon.", "isCorrect": False},
                        {"text": "La pneumonie.", "isCorrect": False}
                    ],
                    "correction": "La **Silicose** est causée par l'inhalation prolongée de poussières minérales."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel est le risque de travailler sur un support en mauvais état (fissures importantes, poudreux) sans appliquer de primaire ou de fixateur ?",
                    "answerOptions": [
                        {"text": "La peinture devient trop brillante.", "isCorrect": False},
                        {"text": "Mauvaise adhérence (la peinture s'écaille ou 'farine'), surconsommation de produit, et apparition rapide de défauts (fissures).", "isCorrect": True},
                        {"text": "La peinture ne sèche pas.", "isCorrect": False},
                        {"text": "La couleur change.", "isCorrect": False}
                    ],
                    "correction": "La **préparation du support** est la moitié du travail du peintre."
                },
                {
                    "questionNumber": 14,
                    "question": "Que faut-il faire sur un support ancien potentiellement recouvert de **peinture au plomb** (bâtiment avant 1948) ?",
                    "answerOptions": [
                        {"text": "Le recouvrir d'une seule couche de peinture.", "isCorrect": False},
                        {"text": "Réaliser un diagnostic plomb et suivre une procédure de décapage sécurisée avec confinement et EPI adaptés (masque P3, combinaison).", "isCorrect": True},
                        {"text": "Le poncer sans protection.", "isCorrect": False},
                        {"text": "Le nettoyer simplement à l'eau.", "isCorrect": False}
                    ],
                    "correction": "Le **Plomb** est un poison neurotoxique, le diagnostic et la sécurité sont obligatoires (réglementation travaux)."
                },
                {
                    "questionNumber": 15,
                    "question": "Pourquoi doit-on obligatoirement sécuriser et baliser la zone de travail (pied d'échafaudage, zone de ponçage) ?",
                    "answerOptions": [
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Pour signaler le danger (chute d'outils ou de matériaux) et empêcher l'accès aux personnes non autorisées.", "isCorrect": True},
                        {"text": "Pour isoler thermiquement la zone.", "isCorrect": False},
                        {"text": "Pour améliorer l'éclairage.", "isCorrect": False}
                    ],
                    "correction": "Le **balisage** protège l'opérateur et les tiers."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel est le risque de laisser un pot de peinture ouvert sans surveillance sur un chantier ?",
                    "answerOptions": [
                        {"text": "Le produit va figer.", "isCorrect": False},
                        {"text": "Chute, déversement accidentel de produit, risque d'incendie (solvants) et contamination du produit par des poussières.", "isCorrect": True},
                        {"text": "La peinture ne sèche pas.", "isCorrect": False},
                        {"text": "La peinture change de couleur.", "isCorrect": False}
                    ],
                    "correction": "Les pots doivent être **refermés** et stockés dans un endroit sûr et frais."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel est le rôle du **dégraissage** (nettoyage au savon/lessive St-Marc) avant peinture sur un support en cuisine ou salle de bain ?",
                    "answerOptions": [
                        {"text": "Le rendre plus lisse.", "isCorrect": False},
                        {"text": "Éliminer les traces de graisse, d'huile ou de silicone qui empêcheraient l'adhérence de la peinture (effet 'tâches' ou 'mouillage').", "isCorrect": True},
                        {"text": "Le colorer.", "isCorrect": False},
                        {"text": "Le reboucher.", "isCorrect": False}
                    ],
                    "correction": "Le **dégraissage** est fondamental sur les supports soumis aux projections grasses."
                },
                {
                    "questionNumber": 18,
                    "question": "Quelle est l'importance de dégraisser une surface métallique avant l'application d'un antirouille ou d'une laque ?",
                    "answerOptions": [
                        {"text": "La rendre plus rugueuse.", "isCorrect": False},
                        {"text": "Assurer une adhérence maximale du primaire et de la peinture de finition, évitant le décollement prématuré du revêtement.", "isCorrect": True},
                        {"text": "La rendre plus brillante.", "isCorrect": False},
                        {"text": "La diluer.", "isCorrect": False}
                    ],
                    "correction": "L'**adhérence** sur le métal dépend d'un dégraissage parfait (acétone, diluant)."
                },
                {
                    "questionNumber": 19,
                    "question": "Quel est le danger principal lié à l'utilisation d'une **échelle simple** sur un chantier ?",
                    "answerOptions": [
                        {"text": "Elle est trop lourde.", "isCorrect": False},
                        {"text": "Le basculement latéral, le ripage (glissement du pied) ou la chute de l'opérateur due au déséquilibre (l'échelle est un outil d'accès, pas de travail prolongé).", "isCorrect": True},
                        {"text": "Elle se casse.", "isCorrect": False},
                        {"text": "Elle ne permet pas de monter haut.", "isCorrect": False}
                    ],
                    "correction": "Les règles de sécurité exigent un appui stable, une inclinaison de 75° et le fait de ne pas travailler sur les deux dernières marches."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est l'action immédiate à effectuer si une peinture ou un vernis prend feu ?",
                    "answerOptions": [
                        {"text": "Ajouter de l'eau.", "isCorrect": False},
                        {"text": "Utiliser un extincteur (CO2 ou Poudre) adapté aux feux d'hydrocarbures (Classe B) et alerter les secours.", "isCorrect": True},
                        {"text": "Faire un courant d'air.", "isCorrect": False},
                        {"text": "Le recouvrir d'une bâche en plastique.", "isCorrect": False}
                    ],
                    "correction": "L'eau aggraverait souvent le feu de produits inflammables (solvants)."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : CONNAISSANCE DES SUPPORTS ET PRÉPARATION (Q. 21-40)
        # =========================================================================
        2: {
            "name": "2. Connaissance des Supports et Préparation (Q. 21-40)",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel est le rôle d'un **Fixateur de fond** ou d'un **Primaire d'accrochage** ?",
                    "answerOptions": [
                        {"text": "Changer la couleur.", "isCorrect": False},
                        {"text": "Réguler l'absorption (bloquer la porosité), améliorer l'adhérence (lier la peinture au support) et uniformiser la surface.", "isCorrect": True},
                        {"text": "Masquer les trous.", "isCorrect": False},
                        {"text": "Diluer la peinture.", "isCorrect": False}
                    ],
                    "correction": "Le **Primaire** est l'interface essentielle entre le support et la finition."
                },
                {
                    "questionNumber": 22,
                    "question": "Quelle est la principale différence entre un **Enduit de rebouchage** et un **Enduit de lissage** ?",
                    "answerOptions": [
                        {"text": "La couleur.", "isCorrect": False},
                        {"text": "Le rebouchage (plus épais, retrait important) sert à combler les gros défauts ; le lissage (finesse d'application) sert à uniformiser la surface et éliminer les rayures.", "isCorrect": True},
                        {"text": "Le rebouchage sèche plus vite.", "isCorrect": False},
                        {"text": "Le lissage est plus cher.", "isCorrect": False}
                    ],
                    "correction": "Le travail du peintre se fait toujours en deux étapes : **reboucher** puis **lisser**."
                },
                {
                    "questionNumber": 23,
                    "question": "Qu'est-ce qu'un support **farineux** et quel est le risque s'il n'est pas traité ?",
                    "answerOptions": [
                        {"text": "Un support trop lisse.", "isCorrect": False},
                        {"text": "Un support qui laisse des traces de poudre blanche au frottement ; la peinture n'adhérera pas et s'écaillera rapidement.", "isCorrect": True},
                        {"text": "Un support trop humide.", "isCorrect": False},
                        {"text": "Un support trop brillant.", "isCorrect": False}
                    ],
                    "correction": "Un support farineux doit être brossé et impérativement recouvert d'un **fixateur de fond**."
                },
                {
                    "questionNumber": 24,
                    "question": "Comment s'appelle l'opération qui consiste à éliminer les petites pointes ou aspérités d'un enduit de rebouchage après séchage ?",
                    "answerOptions": [
                        {"text": "Lessiver.", "isCorrect": False},
                        {"text": "Égrener (ou Ponçage léger entre couches).", "isCorrect": True},
                        {"text": "Maroufler.", "isCorrect": False},
                        {"text": "Fraser.", "isCorrect": False}
                    ],
                    "correction": "L'**égrenage** est souvent réalisé avec un papier de verre très fin."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le défaut courant du plâtre neuf non sec ou mal isolé par un primaire ?",
                    "answerOptions": [
                        {"text": "Il brille trop.", "isCorrect": False},
                        {"text": "L'apparition de taches d'humidité ou de remontées alcalines (alcalinité du support qui réagit avec la peinture).", "isCorrect": True},
                        {"text": "Il devient trop poreux.", "isCorrect": False},
                        {"text": "Il se fissure.", "isCorrect": False}
                    ],
                    "correction": "Il faut vérifier le **pH** du plâtre (lait de chaux) avant application des finitions."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le type d'enduit utilisé pour obtenir une surface parfaitement lisse, miroir, sans défaut visible à l'œil nu (souvent avant l'application d'une laque) ?",
                    "answerOptions": [
                        {"text": "Enduit de rebouchage.", "isCorrect": False},
                        {"text": "Enduit gras ou Enduit à la pâte (Enduit de finition très fin, souvent appliqué en deux passes croisées).", "isCorrect": True},
                        {"text": "Enduit de façade.", "isCorrect": False},
                        {"text": "Enduit de jointoiement.", "isCorrect": False}
                    ],
                    "correction": "L'**Enduit de finition** est le secret du 'tendu parfait'."
                },
                {
                    "questionNumber": 27,
                    "question": "Pourquoi doit-on effectuer une **dépoussiérage** minutieux après le ponçage d'un enduit ?",
                    "answerOptions": [
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "La poussière empêche l'adhérence (primaire et peinture), laisse des grumeaux et peut créer des défauts de surface (granuleux).", "isCorrect": True},
                        {"text": "Pour des raisons de sécurité.", "isCorrect": False},
                        {"text": "Pour lisser le mur.", "isCorrect": False}
                    ],
                    "correction": "Le **dépoussiérage** (brosse souple, éponge humide ou aspirateur industriel) est une étape cruciale."
                },
                {
                    "questionNumber": 28,
                    "question": "Quel est le risque de peindre un mur en plâtre non sec (trop humide) ?",
                    "answerOptions": [
                        {"text": "La peinture sera trop brillante.", "isCorrect": False},
                        {"text": "La peinture ne sèche pas, cloque, ne tient pas et des taches (remontées d'efflorescence, moisissures) peuvent apparaître.", "isCorrect": True},
                        {"text": "La peinture sèche trop vite.", "isCorrect": False},
                        {"text": "La couleur est trop claire.", "isCorrect": False}
                    ],
                    "correction": "L'**humidité** est l'ennemi numéro 1 du peintre (vérification avec un humidimètre)."
                },
                {
                    "questionNumber": 29,
                    "question": "Comment s'appelle la technique consistant à poser un papier spécial (calicot) dans les angles ou sur les fissures pour éviter qu'elles ne réapparaissent ?",
                    "answerOptions": [
                        {"text": "Égrener.", "isCorrect": False},
                        {"text": "Armer ou traiter les fissures (avec calicot, bande armée, ou toile de verre).", "isCorrect": True},
                        {"text": "Poncer.", "isCorrect": False},
                        {"text": "Maroufler.", "isCorrect": False}
                    ],
                    "correction": "L'**armature** donne une résistance mécanique au revêtement (fibre de verre, calicot)."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel outil est le plus adapté pour reboucher un trou profond ou une saignée dans un mur ?",
                    "answerOptions": [
                        {"text": "Un couteau à enduire de 5 cm.", "isCorrect": False},
                        {"text": "Une Truelle (ou une Spatule large) avec un enduit de rebouchage à retrait pour combler la profondeur.", "isCorrect": True},
                        {"text": "Un rouleau.", "isCorrect": False},
                        {"text": "Une brosse à rechampir.", "isCorrect": False}
                    ],
                    "correction": "La **Truelle** ou le couteau de peintre permet d'appliquer la masse nécessaire."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel est le support qui nécessite impérativement un primaire antirouille avant toute finition (s'il n'est pas galvanisé) ?",
                    "answerOptions": [
                        {"text": "Le bois.", "isCorrect": False},
                        {"text": "Le Métal Ferreux (Acier, Fonte) (le primaire stoppe la corrosion).", "isCorrect": True},
                        {"text": "Le plâtre.", "isCorrect": False},
                        {"text": "Le PVC.", "isCorrect": False}
                    ],
                    "correction": "L'**Antirouille** est une protection active/passive indispensable."
                },
                {
                    "questionNumber": 32,
                    "question": "Qu'est-ce que l'**Efflorescence** sur un mur en briques ou en béton ?",
                    "answerOptions": [
                        {"text": "Un dépôt de peinture.", "isCorrect": False},
                        {"text": "Un dépôt de sels minéraux (taches blanches/grisâtres) à la surface du mur causé par l'évaporation de l'eau.", "isCorrect": True},
                        {"text": "Une fissure.", "isCorrect": False},
                        {"text": "Une bulle d'air.", "isCorrect": False}
                    ],
                    "correction": "L'**Efflorescence** doit être brossée et neutralisée avant peinture."
                },
                {
                    "questionNumber": 33,
                    "question": "Quelle est la principale caractéristique de la **Ponceuse Girafe** ?",
                    "answerOptions": [
                        {"text": "Elle sert à peindre.", "isCorrect": False},
                        {"text": "C'est une ponceuse montée sur un long manche télescopique (col de girafe) utilisée pour poncer les plafonds et les hauts de murs sans échafaudage.", "isCorrect": True},
                        {"text": "Elle sert à couper le bois.", "isCorrect": False},
                        {"text": "Elle sert à mélanger la peinture.", "isCorrect": False}
                    ],
                    "correction": "La **Ponceuse Girafe** améliore la productivité et la sécurité."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est l'enduit qui ne doit jamais être utilisé sur une façade ou un mur extérieur soumis à la pluie ?",
                    "answerOptions": [
                        {"text": "L'enduit acrylique.", "isCorrect": False},
                        {"text": "L'Enduit plâtre (ou Enduit de rebouchage intérieur) car il n'est pas étanche et se désagrège à l'humidité.", "isCorrect": True},
                        {"text": "L'enduit ciment.", "isCorrect": False},
                        {"text": "L'enduit époxy.", "isCorrect": False}
                    ],
                    "correction": "L'enduit de **façade** doit être adapté aux conditions extérieures (ciment, chaux)."
                },
                {
                    "questionNumber": 35,
                    "question": "Quel est le rôle du **Mastic Acrylique** ou du **Mastic Silicone** ?",
                    "answerOptions": [
                        {"text": "Coller la toile de verre.", "isCorrect": False},
                        {"text": "Réaliser des joints souples (mastic acrylique : peut être peint) ou étanches (silicone : non peignable) entre deux matériaux différents ou dans les angles.", "isCorrect": True},
                        {"text": "Lisser le mur.", "isCorrect": False},
                        {"text": "Reboucher un trou.", "isCorrect": False}
                    ],
                    "correction": "Le **Mastic** assure l'étanchéité ou la jonction souple."
                },
                {
                    "questionNumber": 36,
                    "question": "Comment appelle-t-on le procédé qui consiste à humidifier légèrement un enduit ou un plâtre avant de lisser (ou 'serrer') sa surface ?",
                    "answerOptions": [
                        {"text": "Gâcher.", "isCorrect": False},
                        {"text": "Mouiller ou Noyer le fond.", "isCorrect": True},
                        {"text": "Peindre.", "isCorrect": False},
                        {"text": "Casser.", "isCorrect": False}
                    ],
                    "correction": "Le **mouillage** empêche l'enduit de 'tirer' trop vite."
                },
                {
                    "questionNumber": 37,
                    "question": "Quel est le support qui nécessite un léger **égrenage** ou **dépolissage** avant peinture pour améliorer l'adhérence (surface très lisse) ?",
                    "answerOptions": [
                        {"text": "Le Plâtre brut.", "isCorrect": False},
                        {"text": "Le PVC, la Céramique, le Stratifié (nécessite une légère abrasion mécanique ou un primaire spécial).", "isCorrect": True},
                        {"text": "Le parpaing.", "isCorrect": False},
                        {"text": "Le placo (BA13).", "isCorrect": False}
                    ],
                    "correction": "Un support **trop lisse** (non poreux) n'est pas adhérent (effet perlant)."
                },
                {
                    "questionNumber": 38,
                    "question": "Quel est l'effet de l'humidité sur une colle à papier peint cellulosique ?",
                    "answerOptions": [
                        {"text": "Elle devient plus épaisse.", "isCorrect": False},
                        {"text": "Elle dilue la colle, ce qui la rend moins efficace et le papier ne tient pas ou se décolle.", "isCorrect": True},
                        {"text": "Elle change de couleur.", "isCorrect": False},
                        {"text": "Elle accélère le séchage.", "isCorrect": False}
                    ],
                    "correction": "Il faut vérifier que l'humidité relative de l'air et du mur est correcte avant la **pose de papier peint**."
                },
                {
                    "questionNumber": 39,
                    "question": "Quel est l'outil utilisé pour nettoyer et décaper des restes de colle, de mastic ou de peinture sur un verre ou une surface lisse et dure ?",
                    "answerOptions": [
                        {"text": "Le papier de verre.", "isCorrect": False},
                        {"text": "Le Grattoir de vitrier (ou Lame de rasoir de sécurité).", "isCorrect": True},
                        {"text": "Le pinceau.", "isCorrect": False},
                        {"text": "Le rouleau.", "isCorrect": False}
                    ],
                    "correction": "Le **Grattoir** permet un nettoyage précis sans rayer le support si l'outil est bien tenu."
                },
                {
                    "questionNumber": 40,
                    "question": "Comment appelle-t-on les défauts qui apparaissent par de petits trous ou bulles dans un enduit après séchage ?",
                    "answerOptions": [
                        {"text": "Les griffures.", "isCorrect": False},
                        {"text": "Les Piqûres (ou Trous d'épingle) dus à l'air emprisonné dans l'enduit ou à une mauvaise application.", "isCorrect": True},
                        {"text": "Les fissures.", "isCorrect": False},
                        {"text": "Les coulures.", "isCorrect": False}
                    ],
                    "correction": "Les **piqûres** doivent être re-lissées ou poncées finement."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : PRODUITS ET MATÉRIAUX DE REVÊTEMENT (Q. 41-60)
        # =========================================================================
        3: {
            "name": "3. Produits et Matériaux de Revêtement (Q. 41-60)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la principale différence de composition entre une peinture **Glycérophtalique (Glycéro)** et une peinture **Acrylique** ?",
                    "answerOptions": [
                        {"text": "Le taux de pigments.", "isCorrect": False},
                        {"text": "La Glycéro a un liant à base de résines synthétiques ou d'alkydes et est diluée aux solvants (White-spirit) ; l'Acrylique a un liant polymère et est diluée à l'eau.", "isCorrect": True},
                        {"text": "La glycéro sèche plus vite.", "isCorrect": False},
                        {"text": "L'acrylique est plus chère.", "isCorrect": False}
                    ],
                    "correction": "La **Glycéro** est plus résistante à l'abrasion et a un meilleur tendu, mais est plus polluante."
                },
                {
                    "questionNumber": 42,
                    "question": "Quelle est la fonction d'une **Peinture Satinée** ?",
                    "answerOptions": [
                        {"text": "Masquer tous les défauts.", "isCorrect": False},
                        {"text": "Offrir un aspect intermédiaire entre le mat et le brillant (résistance, lavable, aspect chaleureux) et refléter légèrement la lumière (sans montrer tous les défauts).", "isCorrect": True},
                        {"text": "Servir de sous-couche.", "isCorrect": False},
                        {"text": "Être très fragile.", "isCorrect": False}
                    ],
                    "correction": "Le **Satiné** est le compromis idéal pour les pièces de vie."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel est le principal rôle d'un **Vernis** ?",
                    "answerOptions": [
                        {"text": "Colorer le bois.", "isCorrect": False},
                        {"text": "Protéger le support (bois, peinture) de l'usure, des chocs et des UV, tout en offrant un aspect plus ou moins brillant.", "isCorrect": True},
                        {"text": "Reboucher les trous.", "isCorrect": False},
                        {"text": "Diluer la peinture.", "isCorrect": False}
                    ],
                    "correction": "Le **Vernis** crée un film de protection transparent ou teinté."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la caractéristique de la **Peinture Mat** (très peu réfléchissante) ?",
                    "answerOptions": [
                        {"text": "Elle est très lavable.", "isCorrect": False},
                        {"text": "Elle masque au maximum les défauts du support (idéale pour les plafonds ou les murs imparfaits) mais est généralement peu lessivable.", "isCorrect": True},
                        {"text": "Elle est très brillante.", "isCorrect": False},
                        {"text": "Elle sèche lentement.", "isCorrect": False}
                    ],
                    "correction": "Le **Mat** absorbe la lumière et rend les imperfections moins visibles."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel est le type de revêtement qui nécessite l'application d'une colle spécifique et sert souvent d'armature pour cacher les défauts ou prévenir les fissures des murs ?",
                    "answerOptions": [
                        {"text": "Le papier peint vinyle.", "isCorrect": False},
                        {"text": "La Toile de verre ou le Revêtement mural à peindre (elle a un rôle de renfort mécanique).", "isCorrect": True},
                        {"text": "Le crépi.", "isCorrect": False},
                        {"text": "Le carrelage.", "isCorrect": False}
                    ],
                    "correction": "La **Toile de verre** est souvent utilisée en rénovation pour assainir et consolider un mur."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la différence entre un **papier peint traditionnel (simplex/duplex)** et un **papier peint vinyle** ?",
                    "answerOptions": [
                        {"text": "Le prix.", "isCorrect": False},
                        {"text": "Le Vinyle est recouvert d'une fine couche de PVC, ce qui le rend lessivable, plus résistant à l'humidité et plus facile à poser.", "isCorrect": True},
                        {"text": "Le vinyle est moins cher.", "isCorrect": False},
                        {"text": "Le vinyle est plus fin.", "isCorrect": False}
                    ],
                    "correction": "Le **Vinyle** est adapté aux pièces humides (cuisine, salle de bain)."
                },
                {
                    "questionNumber": 47,
                    "question": "Quel est le rôle du **Diluant** dans une peinture solvantée (glycéro) ?",
                    "answerOptions": [
                        {"text": "Augmenter la couleur.", "isCorrect": False},
                        {"text": "Abaisser la viscosité de la peinture pour la rendre plus fluide (application au pistolet) ou pour faciliter le nettoyage des outils.", "isCorrect": True},
                        {"text": "Rendre la peinture plus opaque.", "isCorrect": False},
                        {"text": "Accélérer le séchage.", "isCorrect": False}
                    ],
                    "correction": "Le **Diluant** facilite l'application (white-spirit, essence de térébenthine)."
                },
                {
                    "questionNumber": 48,
                    "question": "Qu'est-ce qu'une peinture **Monocouche** (ou Haut Extrait Sec) ?",
                    "answerOptions": [
                        {"text": "Une peinture qui ne sèche jamais.", "isCorrect": False},
                        {"text": "Une peinture très riche en matières solides (liant/pigments) qui offre un fort pouvoir couvrant et masquant en une seule application (théorique).", "isCorrect": True},
                        {"text": "Une peinture très diluée.", "isCorrect": False},
                        {"text": "Une peinture qui s'écaille.", "isCorrect": False}
                    ],
                    "correction": "Bien que rares en pratique, les **monocouches** sont conçues pour gagner du temps."
                },
                {
                    "questionNumber": 49,
                    "question": "Qu'est-ce qu'une **Lasure** (pour le bois) ?",
                    "answerOptions": [
                        {"text": "Une peinture opaque.", "isCorrect": False},
                        {"text": "Un produit de protection du bois (souvent hydrofuge et anti-UV) qui est transparent ou semi-transparent (il laisse apparaître le veinage du bois).", "isCorrect": True},
                        {"text": "Un enduit de rebouchage.", "isCorrect": False},
                        {"text": "Une colle forte.", "isCorrect": False}
                    ],
                    "correction": "La **Lasure** est une protection non filmogène (elle pénètre le bois) contrairement à la peinture ou au vernis."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est l'enduit qui ne doit jamais être poncé, mais simplement lissé au couteau (souvent à base de chaux ou de ciment) ?",
                    "answerOptions": [
                        {"text": "L'Enduit à l'eau.", "isCorrect": False},
                        {"text": "L'Enduit Gras (ou Enduit en pâte) à base d'huile ou de résines, car il encrasse instantanément le papier de verre.", "isCorrect": True},
                        {"text": "L'enduit de rebouchage.", "isCorrect": False},
                        {"text": "L'enduit plâtre.", "isCorrect": False}
                    ],
                    "correction": "L'**Enduit gras** ou l'enduit de façade doit être lissé parfaitement à la pose."
                },
                {
                    "questionNumber": 51,
                    "question": "Quel est le rôle des **Pigments** dans une peinture ?",
                    "answerOptions": [
                        {"text": "Servir de diluant.", "isCorrect": False},
                        {"text": "Apporter la couleur et l'opacité (le pouvoir couvrant) au produit.", "isCorrect": True},
                        {"text": "Servir de liant.", "isCorrect": False},
                        {"text": "Accélérer le séchage.", "isCorrect": False}
                    ],
                    "correction": "Les **Pigments** sont des poudres insolubles."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le type de colle utilisé pour la pose de revêtements muraux lourds (vinyle épais, toile de verre) ?",
                    "answerOptions": [
                        {"text": "Colle à base d'eau.", "isCorrect": False},
                        {"text": "Colle acrylique ou colle vinylique renforcée (plus puissante que la colle cellulosique simple).", "isCorrect": True},
                        {"text": "Colle à bois.", "isCorrect": False},
                        {"text": "Mastic silicone.", "isCorrect": False}
                    ],
                    "correction": "La **Colle pour revêtements lourds** est formulée pour supporter le poids."
                },
                {
                    "questionNumber": 53,
                    "question": "Qu'est-ce qu'une peinture **Filmogène** (comme un vernis ou une laque) ?",
                    "answerOptions": [
                        {"text": "Une peinture qui ne tient pas.", "isCorrect": False},
                        {"text": "Une peinture qui forme une couche (un film) épaisse et protectrice en surface du support.", "isCorrect": True},
                        {"text": "Une peinture qui pénètre le support.", "isCorrect": False},
                        {"text": "Une peinture mat.", "isCorrect": False}
                    ],
                    "correction": "Les peintures **filmogènes** sont souvent très brillantes et lessivables."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel est l'effet d'un excès de diluant sur une peinture ?",
                    "answerOptions": [
                        {"text": "Le pouvoir couvrant augmente.", "isCorrect": False},
                        {"text": "Le pouvoir couvrant diminue fortement, la peinture coule et le temps de séchage est allongé (la peinture est dite 'noyée').", "isCorrect": True},
                        {"text": "La peinture devient plus épaisse.", "isCorrect": False},
                        {"text": "La peinture est trop foncée.", "isCorrect": False}
                    ],
                    "correction": "Le **dosage du diluant** doit être précis, souvent entre 5 et 10% pour le rouleau/pinceau."
                },
                {
                    "questionNumber": 55,
                    "question": "Quel est le rôle du **Liant** dans la composition d'une peinture ?",
                    "answerOptions": [
                        {"text": "Apporter la couleur.", "isCorrect": False},
                        {"text": "Former le film de peinture et garantir l'adhérence des pigments et du revêtement au support (ex : résines, polymères).", "isCorrect": True},
                        {"text": "Diluer la peinture.", "isCorrect": False},
                        {"text": "Accélérer le séchage.", "isCorrect": False}
                    ],
                    "correction": "Le **Liant** est le squelette solide de la peinture (résines vinyliques, acryliques, etc.)."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'avantage du **Papier Peint Intissé** ?",
                    "answerOptions": [
                        {"text": "Il est très fin.", "isCorrect": False},
                        {"text": "Il est plus résistant, masquant les défauts du mur et la colle s'applique directement sur le mur (pas sur le dos du papier).", "isCorrect": True},
                        {"text": "Il est très fragile.", "isCorrect": False},
                        {"text": "Il est très difficile à décoller.", "isCorrect": False}
                    ],
                    "correction": "L'**Intissé** est le plus utilisé en rénovation pour sa facilité de pose et sa résistance."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel est le type d'enduit qui permet de reboucher, de lisser et de décorer (effet matière, enduit ciré) en une seule application ?",
                    "answerOptions": [
                        {"text": "Enduit de rebouchage.", "isCorrect": False},
                        {"text": "Enduit multi-usages (ou Enduit de décoration).", "isCorrect": True},
                        {"text": "Enduit de jointoiement.", "isCorrect": False},
                        {"text": "Enduit ciment.", "isCorrect": False}
                    ],
                    "correction": "L'**Enduit de décoration** a une double fonction technique et esthétique."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle est la principale caractéristique de la **Peinture Époxy (bi-composant)** ?",
                    "answerOptions": [
                        {"text": "Elle est très souple.", "isCorrect": False},
                        {"text": "Elle est composée d'une base et d'un durcisseur (catalyseur) ; elle est très dure, résistante aux chocs et aux produits chimiques (idéale pour les sols, garages, cuisines industrielles).", "isCorrect": True},
                        {"text": "Elle sèche très lentement.", "isCorrect": False},
                        {"text": "Elle est très peu couvrante.", "isCorrect": False}
                    ],
                    "correction": "L'**Époxy** est extrêmement résistante après polymérisation."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est l'outil utilisé pour déterminer avec précision la teinte souhaitée à partir d'un échantillon ?",
                    "answerOptions": [
                        {"text": "Le spectrophotomètre (ou Colorimètre).", "isCorrect": True},
                        {"text": "Le couteau à enduire.", "isCorrect": False},
                        {"text": "Le humidimètre.", "isCorrect": False},
                        {"text": "Le pinceau.", "isCorrect": False}
                    ],
                    "correction": "Le **Colorimètre** permet de lire et de reproduire précisément une teinte (teinte RAL, NCS)."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel est le risque de superposer un papier peint lourd sur un support déjà tapissé (plusieurs couches de vieux papiers) ?",
                    "answerOptions": [
                        {"text": "La couleur ne ressort pas.", "isCorrect": False},
                        {"text": "Le nouveau papier tire sur les anciennes couches, le poids de l'ensemble provoque le décollement rapide et l'apparition de cloques.", "isCorrect": True},
                        {"text": "La colle sèche trop vite.", "isCorrect": False},
                        {"text": "Le mur se fissure.", "isCorrect": False}
                    ],
                    "correction": "L'ancien **revêtement** doit être retiré pour assurer l'adhérence du nouveau."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : TECHNIQUES ET OUTILS D'APPLICATION (Q. 61-80)
        # =========================================================================
        4: {
            "name": "4. Techniques et Outils d'Application (Q. 61-80)",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quelle est la technique d'application qui donne le **meilleur tendu** (surface la plus lisse et sans trace de brosse/rouleau) ?",
                    "answerOptions": [
                        {"text": "L'application au rouleau à poils longs.", "isCorrect": False},
                        {"text": "L'application au Pistolet Airless ou Pneumatique (la peinture est pulvérisée en fines gouttelettes).", "isCorrect": True},
                        {"text": "L'application à la brosse.", "isCorrect": False},
                        {"text": "L'application au spalter.", "isCorrect": False}
                    ],
                    "correction": "Le **Pistolet** est l'outil du laqueur pour obtenir un aspect miroir."
                },
                {
                    "questionNumber": 62,
                    "question": "Comment s'appelle la brosse à rechampir utilisée pour dégager les angles (le joint entre deux surfaces de couleurs différentes) ?",
                    "answerOptions": [
                        {"text": "La brosse plate.", "isCorrect": False},
                        {"text": "La Brosse à rechampir (à bout rond ou pointu).", "isCorrect": True},
                        {"text": "Le spalter.", "isCorrect": False},
                        {"text": "La patte de lapin.", "isCorrect": False}
                    ],
                    "correction": "Le **Rechampissage** (ou l'angle) est l'opération de précision au pinceau."
                },
                {
                    "questionNumber": 63,
                    "question": "Quel est le rôle du rouleau à **poils longs** (méché) ?",
                    "answerOptions": [
                        {"text": "Avoir le meilleur tendu.", "isCorrect": False},
                        {"text": "Appliquer des produits épais (enduits, revêtements structurés) ou peindre des surfaces brutes et rugueuses (façade, béton).", "isCorrect": True},
                        {"text": "Avoir une finition très lisse.", "isCorrect": False},
                        {"text": "Ne pas projeter.", "isCorrect": False}
                    ],
                    "correction": "Les **poils longs** permettent d'aller chercher la peinture dans les creux du support."
                },
                {
                    "questionNumber": 64,
                    "question": "Quelle est la technique d'application de la peinture qui évite les traces de reprise, notamment en façade ou sur un plafond ?",
                    "answerOptions": [
                        {"text": "Travailler lentement.", "isCorrect": False},
                        {"text": "Travailler « frais dans frais » (recouvrement des couches tant que la peinture précédente n'a pas tiré) et croiser les passes.", "isCorrect": True},
                        {"text": "Travailler avec un pinceau très fin.", "isCorrect": False},
                        {"text": "Travailler par petites zones.", "isCorrect": False}
                    ],
                    "correction": "Le **frais dans frais** (ou travail de continuité) est essentiel pour éviter les traces de rouleau."
                },
                {
                    "questionNumber": 65,
                    "question": "Quel est l'outil utilisé pour chasser les bulles d'air et maroufler un papier peint (le plaquer contre le mur) ?",
                    "answerOptions": [
                        {"text": "Le ciseau.", "isCorrect": False},
                        {"text": "La Brosse à maroufler (ou la Spatule à maroufler en plastique).", "isCorrect": True},
                        {"text": "Le couteau à enduire.", "isCorrect": False},
                        {"text": "Le rouleau à peindre.", "isCorrect": False}
                    ],
                    "correction": "Le **Marouflage** assure une bonne adhérence et élimine l'air emprisonné."
                },
                {
                    "questionNumber": 66,
                    "question": "Comment appelle-t-on la délimitation (souvent au ruban de masquage) qui doit être retirée avant le séchage complet d'une laque pour éviter l'écaillage ?",
                    "answerOptions": [
                        {"text": "La coupe.", "isCorrect": False},
                        {"text": "L'Arrachage à vif (retirer le ruban de masquage pendant que la peinture est encore humide ou 'liquide').", "isCorrect": True},
                        {"text": "Le raccord.", "isCorrect": False},
                        {"text": "Le dégagement.", "isCorrect": False}
                    ],
                    "correction": "Le ruban doit être retiré pour que la peinture ne se fissure pas en séchant autour du ruban."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est le rôle du **Rouleau laqueur** (rouleau à poils ras, en mousse ou en microfibre très fine) ?",
                    "answerOptions": [
                        {"text": "Appliquer des crépis.", "isCorrect": False},
                        {"text": "Appliquer des laques, des vernis ou des peintures à forte brillance pour obtenir le meilleur tendu et le moins d'effet 'peau d'orange'.", "isCorrect": True},
                        {"text": "Appliquer des enduits.", "isCorrect": False},
                        {"text": "Nettoyer le mur.", "isCorrect": False}
                    ],
                    "correction": "Le **Rouleau laqueur** est l'outil de finition lisse par excellence."
                },
                {
                    "questionNumber": 68,
                    "question": "Quel est le risque de travailler par **temps très chaud et sec** avec une peinture acrylique ?",
                    "answerOptions": [
                        {"text": "La peinture devient trop brillante.", "isCorrect": False},
                        {"text": "La peinture sèche trop vite ('claque') ; le temps de travail est trop court, ce qui entraîne des traces de reprise et une mauvaise pénétration du support.", "isCorrect": True},
                        {"text": "La peinture ne sèche pas.", "isCorrect": False},
                        {"text": "La peinture est trop foncée.", "isCorrect": False}
                    ],
                    "correction": "Il faut parfois **humidifier légèrement le support** ou ajouter un retardateur de séchage (diluant approprié) pour pallier la chaleur."
                },
                {
                    "questionNumber": 69,
                    "question": "Comment appelle-t-on le procédé qui consiste à peindre les bords (angles, plinthes, menuiseries) avant d'appliquer le rouleau sur la grande surface ?",
                    "answerOptions": [
                        {"text": "Égrener.", "isCorrect": False},
                        {"text": "Dégager les angles ou Rechampir.", "isCorrect": True},
                        {"text": "Maroufler.", "isCorrect": False},
                        {"text": "Poncer.", "isCorrect": False}
                    ],
                    "correction": "Le **Rechampissage** est effectué à la brosse, puis le rouleau est passé avant le séchage pour un raccord invisible."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est l'outil utilisé pour appliquer l'enduit de lissage sur de grandes surfaces (par opposition au couteau à enduire simple) ?",
                    "answerOptions": [
                        {"text": "Le spalter.", "isCorrect": False},
                        {"text": "La Lame à enduire (ou Lame de lissage) de grande taille (40 à 60 cm).", "isCorrect": True},
                        {"text": "Le pinceau.", "isCorrect": False},
                        {"text": "Le rouleau.", "isCorrect": False}
                    ],
                    "correction": "La **Lame à enduire** permet d'obtenir une surface plane et sans vague."
                },
                {
                    "questionNumber": 71,
                    "question": "Comment procède-t-on pour la pose d'un **papier peint à raccord sauté** ?",
                    "answerOptions": [
                        {"text": "Les motifs sont posés aléatoirement.", "isCorrect": False},
                        {"text": "Les lés sont décalés (sautés) d'une certaine hauteur (ex : un demi-motif) à chaque pose pour que les motifs s'imbriquent correctement.", "isCorrect": True},
                        {"text": "On pose directement sur le mur.", "isCorrect": False},
                        {"text": "On coupe les bords.", "isCorrect": False}
                    ],
                    "correction": "Le **Raccord sauté** est plus complexe à poser que le raccord droit."
                },
                {
                    "questionNumber": 72,
                    "question": "Quel est le risque de superposer trop de peinture ou de laque en une seule couche épaisse ?",
                    "answerOptions": [
                        {"text": "Elle devient trop mat.", "isCorrect": False},
                        {"text": "L'apparition de coulures (la peinture glisse avant de tirer) ou de cloques (le film extérieur sèche trop vite et le cœur reste humide).", "isCorrect": True},
                        {"text": "Le pouvoir couvrant diminue.", "isCorrect": False},
                        {"text": "Elle ne sèche pas.", "isCorrect": False}
                    ],
                    "correction": "Il est préférable de faire **deux couches fines** qu'une couche trop épaisse."
                },
                {
                    "questionNumber": 73,
                    "question": "Quel est l'effet de l'humidité du support sur l'application d'un enduit poudreux gâché à l'eau (enduit de rebouchage) ?",
                    "answerOptions": [
                        {"text": "Il brille.", "isCorrect": False},
                        {"text": "L'enduit se délite, a une faible adhérence et ne durcit pas correctement (il 'farine' et ne tient pas).", "isCorrect": True},
                        {"text": "Il sèche trop vite.", "isCorrect": False},
                        {"text": "Il devient trop blanc.", "isCorrect": False}
                    ],
                    "correction": "Le **support doit être sec**, mais pas trop pour ne pas 'pomper' l'eau de gâchage."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment appelle-t-on l'opération qui consiste à couper l'excédent de papier peint dans les angles et au ras des plinthes ?",
                    "answerOptions": [
                        {"text": "Maroufler.", "isCorrect": False},
                        {"text": "Araser (ou Massicotage).", "isCorrect": True},
                        {"text": "Dégager.", "isCorrect": False},
                        {"text": "Plaquer.", "isCorrect": False}
                    ],
                    "correction": "L'**Arasage** se fait avec un couteau à maroufler et un cutter neuf."
                },
                {
                    "questionNumber": 75,
                    "question": "Quel est le rôle de la **double passe croisée** (application de deux passes perpendiculaires) lors de l'application de la peinture au rouleau ?",
                    "answerOptions": [
                        {"text": "Ralentir le séchage.", "isCorrect": False},
                        {"text": "Assurer une couverture totale (éviter les manques) et répartir uniformément l'épaisseur de la peinture.", "isCorrect": True},
                        {"text": "Accélérer le séchage.", "isCorrect": False},
                        {"text": "Créer un effet décoratif.", "isCorrect": False}
                    ],
                    "correction": "La **double passe croisée** est la technique standard au rouleau."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le risque de trop **diluer** une peinture appliquée au pistolet ?",
                    "answerOptions": [
                        {"text": "Elle bouche le pistolet.", "isCorrect": False},
                        {"text": "La peinture coule excessivement et le pouvoir couvrant est trop faible (couleur non uniforme).", "isCorrect": True},
                        {"text": "Elle est trop épaisse.", "isCorrect": False},
                        {"text": "Elle devient trop mat.", "isCorrect": False}
                    ],
                    "correction": "La **viscosité** (mesurée au viscosimètre) doit être juste suffisante pour être pulvérisée."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est le type de rouleau qui laisse un **léger grain** (effet peau d'orange) sur la surface ?",
                    "answerOptions": [
                        {"text": "Rouleau laqueur.", "isCorrect": False},
                        {"text": "Rouleau à poils moyens ou longs (méchés).", "isCorrect": True},
                        {"text": "Pinceau.", "isCorrect": False},
                        {"text": "Spalter.", "isCorrect": False}
                    ],
                    "correction": "Le **rouleau méché** crée un léger relief."
                },
                {
                    "questionNumber": 78,
                    "question": "Quelle est l'importance de nettoyer les outils (brosses, rouleaux) immédiatement après utilisation ?",
                    "answerOptions": [
                        {"text": "Pour des raisons esthétiques.", "isCorrect": False},
                        {"text": "Le séchage du liant et des pigments rend le nettoyage impossible ou très difficile, endommageant les outils (surtout les brosses).", "isCorrect": True},
                        {"text": "Pour des raisons de sécurité.", "isCorrect": False},
                        {"text": "Pour changer la couleur.", "isCorrect": False}
                    ],
                    "correction": "Les outils pour l'acrylique se lavent à l'eau, ceux pour la glycéro au **solvant**."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel est le risque de poncer une peinture encore **molle ou poisseuse** ?",
                    "answerOptions": [
                        {"text": "Elle devient trop brillante.", "isCorrect": False},
                        {"text": "Le papier de verre s'encrasse immédiatement (l'abrasif est inefficace), et la peinture se décolle ou fait des boules.", "isCorrect": True},
                        {"text": "Elle devient trop mat.", "isCorrect": False},
                        {"text": "Elle change de couleur.", "isCorrect": False}
                    ],
                    "correction": "Le support doit être parfaitement **sec à cœur** avant ponçage ou égrenage."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment s'appelle la technique consistant à poser deux couleurs différentes l'une à côté de l'autre sans ruban de masquage ?",
                    "answerOptions": [
                        {"text": "Le dégagement.", "isCorrect": False},
                        {"text": "Le Rechampissage à main levée (nécessite une excellente maîtrise du pinceau et une peinture pas trop liquide).", "isCorrect": True},
                        {"text": "La délimitation.", "isCorrect": False},
                        {"text": "La coupe.", "isCorrect": False}
                    ],
                    "correction": "Le **Rechampissage à main levée** est la marque d'un professionnel expérimenté."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : ORGANISATION, MÉTRÉ ET REVÊTEMENTS SPÉCIFIQUES (Q. 81-100)
        # =========================================================================
        5: {
            "name": "5. Organisation, Métré et Revêtements Spécifiques (Q. 81-100)",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel est l'élément qui doit être **déduit** de la surface totale lors du calcul du métré (si sa surface est supérieure à un certain seuil) ?",
                    "answerOptions": [
                        {"text": "Les plinthes.", "isCorrect": False},
                        {"text": "Les baies (portes et fenêtres) dont la surface est généralement déduite si elle est supérieure à 0,5 ou 1 m² (selon le CCTP ou l'entreprise).", "isCorrect": True},
                        {"text": "Les angles.", "isCorrect": False},
                        {"text": "Les rebords de fenêtres.", "isCorrect": False}
                    ],
                    "correction": "Le **métré** se base sur la surface réelle à peindre."
                },
                {
                    "questionNumber": 82,
                    "question": "Comment s'appelle l'opération consistant à lisser le dos du papier peint encollé pour le rendre plus souple avant la pose ?",
                    "answerOptions": [
                        {"text": "Maroufler.", "isCorrect": False},
                        {"text": "Tableter (ou Plier en accordéon, face collée contre face collée).", "isCorrect": True},
                        {"text": "Araser.", "isCorrect": False},
                        {"text": "Fraiser.", "isCorrect": False}
                    ],
                    "correction": "Le **Tabletage** est le temps de pose du papier peint humide, il évite les plis et facilite la pose."
                },
                {
                    "questionNumber": 83,
                    "question": "Quel est le risque de ne pas respecter le **temps de séchage** entre deux couches de peinture (temps de recouvrement) ?",
                    "answerOptions": [
                        {"text": "La peinture est trop mat.", "isCorrect": False},
                        {"text": "La première couche risque de se 'détremper' (ramollir) sous l'effet de la seconde couche ou le séchage à cœur sera bloqué (cloques, mauvaise dureté).", "isCorrect": True},
                        {"text": "Le pouvoir couvrant augmente.", "isCorrect": False},
                        {"text": "La couleur devient trop foncée.", "isCorrect": False}
                    ],
                    "correction": "Le temps de séchage (mentionné sur la FDS) est crucial pour la **dureté** finale du film."
                },
                {
                    "questionNumber": 84,
                    "question": "Comment calcule-t-on la **quantité de peinture** nécessaire pour un chantier (en l ou kg) ?",
                    "answerOptions": [
                        {"text": "Surface du mur multipliée par le prix du pot.", "isCorrect": False},
                        {"text": "Surface à peindre (en m²) multipliée par le nombre de couches, divisée par le rendement indiqué sur le pot (en m²/l).", "isCorrect": True},
                        {"text": "Le volume de la pièce.", "isCorrect": False},
                        {"text": "La hauteur du mur.", "isCorrect": False}
                    ],
                    "correction": "Le **Rendement** est l'information clé (ex : 10 m²/l)."
                },
                {
                    "questionNumber": 85,
                    "question": "Quel est le rôle du **Spalter** (pinceau large et plat) ?",
                    "answerOptions": [
                        {"text": "Appliquer la peinture au rouleau.", "isCorrect": False},
                        {"text": "Appliquer des vernis, des lasures ou réaliser des effets décoratifs (chaux, essuyé) grâce à sa souplesse et sa capacité à 'tirer' les couches fines.", "isCorrect": True},
                        {"text": "Reboucher les trous.", "isCorrect": False},
                        {"text": "Poncer le mur.", "isCorrect": False}
                    ],
                    "correction": "Le **Spalter** est idéal pour le bois et les effets décoratifs."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le principal inconvénient d'une **Peinture à l'Huile (Glycéro)** par rapport à l'acrylique ?",
                    "answerOptions": [
                        {"text": "Elle est moins résistante.", "isCorrect": False},
                        {"text": "Le temps de séchage (tirage) est beaucoup plus long (jusqu'à 24h) et elle dégage une forte odeur persistante (COV).", "isCorrect": True},
                        {"text": "Elle est moins couvrante.", "isCorrect": False},
                        {"text": "Elle est plus chère.", "isCorrect": False}
                    ],
                    "correction": "Le long **temps de séchage** allonge la durée du chantier."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment s'appelle l'opération qui consiste à éliminer les anciennes couches de peinture qui s'écaillent ou cloquent avant de repeindre un support ?",
                    "answerOptions": [
                        {"text": "Le rebouchage.", "isCorrect": False},
                        {"text": "Le Décapage (mécanique, thermique ou chimique).", "isCorrect": True},
                        {"text": "Le lissage.", "isCorrect": False},
                        {"text": "L'égrenage.", "isCorrect": False}
                    ],
                    "correction": "Le **Décapage** assure une base saine au nouveau revêtement."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel est le risque de stocker les produits (peinture, enduits) dans un local trop froid (proche de 0°C) ?",
                    "answerOptions": [
                        {"text": "Le produit devient trop liquide.", "isCorrect": False},
                        {"text": "Les produits en phase aqueuse (acryliques) risquent de geler et de coaguler, les rendant inutilisables (rupture de l'émulsion).", "isCorrect": True},
                        {"text": "Le produit change de couleur.", "isCorrect": False},
                        {"text": "Le produit sèche trop vite.", "isCorrect": False}
                    ],
                    "correction": "Le **gel** est fatal aux produits à l'eau."
                },
                {
                    "questionNumber": 89,
                    "question": "Qu'est-ce que le **Lé** lors de la pose d'un papier peint ?",
                    "answerOptions": [
                        {"text": "La colle.", "isCorrect": False},
                        {"text": "La Bande de papier peint découpée à la bonne longueur (hauteur du mur + marge d'arasage).", "isCorrect": True},
                        {"text": "Le coin de la pièce.", "isCorrect": False},
                        {"text": "La brosse.", "isCorrect": False}
                    ],
                    "correction": "La pose se fait lé par lé, en vérifiant l'aplomb du premier **lé**."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est le principal défaut d'un **glaçage miroir** (peinture très brillante, laquée) ?",
                    "answerOptions": [
                        {"text": "Il est trop mat.", "isCorrect": False},
                        {"text": "Il fait ressortir le moindre défaut du support (creux, rayures) et nécessite une préparation très minutieuse (Enduit de finition et ponçage parfait).", "isCorrect": True},
                        {"text": "Il est peu lavable.", "isCorrect": False},
                        {"text": "Il est peu résistant.", "isCorrect": False}
                    ],
                    "correction": "Le **Glaçage** exige un support irréprochable."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel est l'outil utilisé pour déterminer si une surface est plane ou présente des bosses/creux avant l'application d'un enduit de lissage ?",
                    "answerOptions": [
                        {"text": "Le mètre ruban.", "isCorrect": False},
                        {"text": "La Règle (règle alu, règle de maçon) ou le laser (pour une planéité parfaite).", "isCorrect": True},
                        {"text": "Le pinceau.", "isCorrect": False},
                        {"text": "Le rouleau.", "isCorrect": False}
                    ],
                    "correction": "La **Règle** permet de vérifier la planéité de l'enduit ou du support."
                },
                {
                    "questionNumber": 92,
                    "question": "Pourquoi doit-on effectuer une **seconde passe** de peinture (couche de finition) ?",
                    "answerOptions": [
                        {"text": "Pour ralentir le séchage.", "isCorrect": False},
                        {"text": "Pour garantir l'uniformité de la teinte, atteindre le pouvoir couvrant optimal et obtenir le meilleur tendu (aspect final du film).", "isCorrect": True},
                        {"text": "Pour économiser la peinture.", "isCorrect": False},
                        {"text": "Pour masquer les trous.", "isCorrect": False}
                    ],
                    "correction": "La **seconde couche** apporte la finition et la résistance."
                },
                {
                    "questionNumber": 93,
                    "question": "Qu'est-ce qu'une **Peinture Anti-Condensation** (souvent utilisée dans les salles de bain) ?",
                    "answerOptions": [
                        {"text": "Une peinture imperméable.", "isCorrect": False},
                        {"text": "Une peinture qui, grâce à sa composition (micro-billes), isole légèrement le support pour éviter le choc thermique qui crée la condensation (et la moisissure).", "isCorrect": True},
                        {"text": "Une peinture brillante.", "isCorrect": False},
                        {"text": "Une peinture très foncée.", "isCorrect": False}
                    ],
                    "correction": "L'**Anti-Condensation** est une peinture technique spécifique."
                },
                {
                    "questionNumber": 94,
                    "question": "Quel est le risque de poser un papier peint sur un support trop **absorbant** (plâtre nu non primairisé) ?",
                    "answerOptions": [
                        {"text": "Le papier devient trop lisse.", "isCorrect": False},
                        {"text": "Le support absorbe trop vite l'eau de la colle, ce qui empêche une bonne adhérence et le papier se décolle (colle trop vite 'tirée').", "isCorrect": True},
                        {"text": "La colle déborde.", "isCorrect": False},
                        {"text": "Le papier se déchire.", "isCorrect": False}
                    ],
                    "correction": "Il faut appliquer un **primaire régulateur d'absorption** (ou un pré-encollage) sur le plâtre."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est l'importance de faire un **Métré** précis avant le début du chantier ?",
                    "answerOptions": [
                        {"text": "Pour connaître les horaires.", "isCorrect": False},
                        {"text": "Déterminer les quantités exactes de matériaux (peinture, enduits, papier) pour ne pas gaspiller et établir un devis juste (temps de travail et coût).", "isCorrect": True},
                        {"text": "Pour choisir les couleurs.", "isCorrect": False},
                        {"text": "Pour vérifier l'humidité.", "isCorrect": False}
                    ],
                    "correction": "Le **Métré** est la base de la rentabilité et du devis."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel est l'outil indispensable pour s'assurer que le premier lé de papier peint est posé parfaitement droit ?",
                    "answerOptions": [
                        {"text": "Le niveau à bulle.", "isCorrect": False},
                        {"text": "Le Fil à plomb (pour la verticale) ou le niveau laser.", "isCorrect": True},
                        {"text": "Le mètre ruban.", "isCorrect": False},
                        {"text": "La règle.", "isCorrect": False}
                    ],
                    "correction": "L'**Aplomb** du premier lé détermine la réussite de tout le mur."
                },
                {
                    "questionNumber": 97,
                    "question": "Quel est le rôle du **Rouleau patte de lapin** (petit rouleau étroit) ?",
                    "answerOptions": [
                        {"text": "Appliquer des enduits.", "isCorrect": False},
                        {"text": "Peindre les petites surfaces ou les zones difficiles d'accès (derrière les radiateurs, sous les tuyaux, bords de fenêtres).", "isCorrect": True},
                        {"text": "Faire le dégagement des angles.", "isCorrect": False},
                        {"text": "Lisser le mur.", "isCorrect": False}
                    ],
                    "correction": "La **patte de lapin** est l'outil des zones confinées."
                },
                {
                    "questionNumber": 98,
                    "question": "Quel est le risque de préparer une trop grande quantité d'**enduit en poudre** (gâché à l'eau) ?",
                    "answerOptions": [
                        {"text": "L'enduit devient trop mou.", "isCorrect": False},
                        {"text": "Le temps de prise (durcissement) est dépassé avant d'avoir pu l'utiliser, ce qui entraîne le gaspillage (enduit durci dans la gâchette).", "isCorrect": True},
                        {"text": "L'enduit est trop liquide.", "isCorrect": False},
                        {"text": "L'enduit change de couleur.", "isCorrect": False}
                    ],
                    "correction": "Le **temps de prise** (ou temps ouvert) est l'ennemi du peintre (travailler par petites quantités)."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le risque de ne pas effectuer de ponçage/égrenage **entre les couches** (intermédiaire) d'un vernis ou d'une laque ?",
                    "answerOptions": [
                        {"text": "La laque coule.", "isCorrect": False},
                        {"text": "La surface sera rugueuse au toucher, et l'adhérence de la couche suivante sera compromise (la seconde couche glisse et ne tient pas).", "isCorrect": True},
                        {"text": "Le vernis devient mat.", "isCorrect": False},
                        {"text": "Le vernis devient trop foncé.", "isCorrect": False}
                    ],
                    "correction": "L'**égrenage intermédiaire** est essentiel pour un bon tendu et une bonne adhérence de la couche finale (accrochage)."
                },
                {
                    "questionNumber": 100,
                    "question": "Quel est l'outil utilisé pour nettoyer les traces de colle, de peinture ou de mastic sur les rebords de fenêtres et les boiseries ?",
                    "answerOptions": [
                        {"text": "Le rouleau.", "isCorrect": False},
                        {"text": "Le Couteau américain ou Couteau à enduire (ou Spatule souple).", "isCorrect": True},
                        {"text": "Le fil à plomb.", "isCorrect": False},
                        {"text": "La brosse.", "isCorrect": False}
                    ],
                    "correction": "Le **Couteau américain** est l'outil polyvalent du peintre (application, raclage, nettoyage)."
                },
            ]
        }
    }
}