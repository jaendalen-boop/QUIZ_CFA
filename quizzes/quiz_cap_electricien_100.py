quiz_data = {
    "title": "Quiz CAP Électricité : Santé, Technologie, Mesures et Norme NF C 15-100 (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : SANTÉ, SÉCURITÉ ET HABILITATIONS ÉLECTRIQUES (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : SANTÉ, SÉCURITÉ ET HABILITATIONS ÉLECTRIQUES",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle est la première étape obligatoire d'une consignation électrique selon la norme NF C 18-510 ?",
                    "answerOptions": [
                        {"text": "La séparation", "isCorrect": True},
                        {"text": "La condamnation en position ouverte", "isCorrect": False},
                        {"text": "La vérification d'absence de tension", "isCorrect": False},
                        {"text": "La mise à la terre et en court-circuit", "isCorrect": False}
                    ],
                    "correction": "La consignation débute toujours par la séparation de l'ouvrage des sources de tension (ouverture visible)."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel équipement est indispensable pour vérifier l'absence de tension en toute sécurité ?",
                    "answerOptions": [
                        {"text": "Un VAT", "isCorrect": True},
                        {"text": "Un multimètre numérique standard", "isCorrect": False},
                        {"text": "Un tournevis testeur à voyant lumineux", "isCorrect": False},
                        {"text": "Une lampe témoin à incandescence classique", "isCorrect": False}
                    ],
                    "correction": "Seul le Vérificateur d'Absence de Tension (VAT) est autorisé pour cette opération (autotest intégré)."
                },
                {
                    "questionNumber": 3,
                    "question": "Que signifie la lettre B dans l'habilitation B1V ?",
                    "answerOptions": [
                        {"text": "Basse tension", "isCorrect": True},
                        {"text": "Borne", "isCorrect": False},
                        {"text": "Batiment", "isCorrect": False},
                        {"text": "Bureau", "isCorrect": False}
                    ],
                    "correction": "B désigne le domaine de la Basse Tension (et TBT), H désigne la Haute Tension."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la définition exacte de l'électrisation ?",
                    "answerOptions": [
                        {"text": "Le passage du courant électrique dans le corps humain", "isCorrect": True},
                        {"text": "Le décès provoqué par le passage du courant électrique", "isCorrect": False},
                        {"text": "La brûlure superficielle de la peau due à un arc électrique", "isCorrect": False},
                        {"text": "Le picotement ressenti lors d'un contact avec une pile", "isCorrect": False}
                    ],
                    "correction": "L'électrisation est le passage du courant dans le corps. L'électrocution est le décès consécutif."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel titre d'habilitation est nécessaire pour diriger des travaux d'ordre électrique en Basse Tension ?",
                    "answerOptions": [
                        {"text": "B2", "isCorrect": True},
                        {"text": "B1", "isCorrect": False},
                        {"text": "B0", "isCorrect": False},
                        {"text": "BC", "isCorrect": False}
                    ],
                    "correction": "Le B2 est le Chargé de Travaux, responsable de l'organisation et de la surveillance."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle couleur est normalisée pour le conducteur de protection à la terre ?",
                    "answerOptions": [
                        {"text": "Vert et jaune", "isCorrect": True},
                        {"text": "Bleu clair", "isCorrect": False},
                        {"text": "Noir ou marron", "isCorrect": False},
                        {"text": "Rouge ou orange", "isCorrect": False}
                    ],
                    "correction": "La double coloration vert/jaune est strictement réservée à la Terre."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle est la distance limite de la zone de voisinage simple en champ libre autour d'une pièce nue sous tension en Basse Tension ?",
                    "answerOptions": [
                        {"text": "3 mètres", "isCorrect": True},
                        {"text": "5 mètres", "isCorrect": False},
                        {"text": "1 mètre", "isCorrect": False},
                        {"text": "2 mètres", "isCorrect": False}
                    ],
                    "correction": "La Zone 1 (voisinage simple) commence à 3 mètres de la pièce nue en BT."
                },
                {
                    "questionNumber": 8,
                    "question": "Que doit faire un électricien avant d'utiliser ses gants isolants ?",
                    "answerOptions": [
                        {"text": "Vérifier leur étanchéité en les gonflant", "isCorrect": True},
                        {"text": "Les laver avec de l'eau savonneuse", "isCorrect": False},
                        {"text": "Mettre du talc à l'intérieur pour le confort", "isCorrect": False},
                        {"text": "Les chauffer légèrement pour les assouplir", "isCorrect": False}
                    ],
                    "correction": "Il faut vérifier l'absence de fuite ou piqûre par vérification pneumatique avant chaque usage."
                },
                {
                    "questionNumber": 9,
                    "question": "Quel est le rôle principal d'un Dispositif Différentiel à Courant Résiduel (DDR) de 30 mA ?",
                    "answerOptions": [
                        {"text": "Protéger les personnes", "isCorrect": True},
                        {"text": "Protéger les câbles", "isCorrect": False},
                        {"text": "Économiser l'énergie", "isCorrect": False},
                        {"text": "Limiter la surtension", "isCorrect": False}
                    ],
                    "correction": "Le 30 mA protège les personnes contre les contacts directs et indirects."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel extincteur faut-il privilégier sur un feu d'origine électrique ?",
                    "answerOptions": [
                        {"text": "CO2", "isCorrect": True},
                        {"text": "Eau", "isCorrect": False},
                        {"text": "Mousse", "isCorrect": False},
                        {"text": "Sable", "isCorrect": False}
                    ],
                    "correction": "Le CO2 est non conducteur et ne laisse aucun résidu endommageant le matériel."
                },
                {
                    "questionNumber": 11,
                    "question": "Dans quel cas l'habilitation BR est-elle requise ?",
                    "answerOptions": [
                        {"text": "Interventions générales d'entretien et de dépannage", "isCorrect": True},
                        {"text": "Travaux complets de rénovation d'une installation", "isCorrect": False},
                        {"text": "Opérations de consignation pour travaux hors tension", "isCorrect": False},
                        {"text": "Direction de travaux sur un chantier de grande ampleur", "isCorrect": False}
                    ],
                    "correction": "Le BR est le chargé d'intervention générale (dépannage, connexion, remplacement)."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle est la tension limite supérieure du domaine Très Basse Tension Alternative (TBT) ?",
                    "answerOptions": [
                        {"text": "50 Volts", "isCorrect": True},
                        {"text": "120 Volts", "isCorrect": False},
                        {"text": "230 Volts", "isCorrect": False},
                        {"text": "24 Volts", "isCorrect": False}
                    ],
                    "correction": "La TBT alternative va de 0 à 50 V inclus."
                },
                {
                    "questionNumber": 13,
                    "question": "Quel document le chargé de consignation doit-il remettre au chargé de travaux une fois la consignation effectuée ?",
                    "answerOptions": [
                        {"text": "Une attestation de consignation", "isCorrect": True},
                        {"text": "Un permis de feu", "isCorrect": False},
                        {"text": "Un bon de travail", "isCorrect": False},
                        {"text": "Un plan de prévention", "isCorrect": False}
                    ],
                    "correction": "L'attestation de consignation certifie que l'ouvrage est hors tension et sécurisé."
                },
                {
                    "questionNumber": 14,
                    "question": "Que signifie l'indice V dans une habilitation comme B1V ?",
                    "answerOptions": [
                        {"text": "Travail au voisinage", "isCorrect": True},
                        {"text": "Vérification", "isCorrect": False},
                        {"text": "Visite", "isCorrect": False},
                        {"text": "Volts", "isCorrect": False}
                    ],
                    "correction": "L'indice V autorise le travail au voisinage renforcé (Zone 4)."
                },
                {
                    "questionNumber": 15,
                    "question": "Quel EPI est obligatoire pour protéger le visage lors d'une manœuvre pouvant générer un arc électrique ?",
                    "answerOptions": [
                        {"text": "Un écran facial", "isCorrect": True},
                        {"text": "Des lunettes de soleil", "isCorrect": False},
                        {"text": "Un masque anti poussière", "isCorrect": False},
                        {"text": "Une casquette de protection", "isCorrect": False}
                    ],
                    "correction": "L'écran facial protège contre les effets thermiques et les UV de l'arc électrique."
                },
                {
                    "questionNumber": 16,
                    "question": "Quelle est la valeur de la résistance du corps humain retenue couramment pour les calculs de sécurité en milieu sec ?",
                    "answerOptions": [
                        {"text": "2000 Ohms", "isCorrect": True},
                        {"text": "50 Ohms", "isCorrect": False},
                        {"text": "100000 Ohms", "isCorrect": False},
                        {"text": "10 Ohms", "isCorrect": False}
                    ],
                    "correction": "On retient souvent une moyenne de 2000 à 2500 Ohms pour la peau sèche."
                },
                {
                    "questionNumber": 17,
                    "question": "Quelle précaution prendre avec une échelle en aluminium près d'une ligne électrique aérienne nue ?",
                    "answerOptions": [
                        {"text": "Ne jamais l'utiliser dans la zone de voisinage", "isCorrect": True},
                        {"text": "L'utiliser uniquement si elle possède des patins", "isCorrect": False},
                        {"text": "La recouvrir d'un vernis isolant spécial", "isCorrect": False},
                        {"text": "Demander à un collègue de la tenir fermement", "isCorrect": False}
                    ],
                    "correction": "Les échelles conductrices sont interdites dans la zone de voisinage (risque d'amorçage)."
                },
                {
                    "questionNumber": 18,
                    "question": "Qui délivre le titre d'habilitation électrique à un salarié ?",
                    "answerOptions": [
                        {"text": "L'employeur", "isCorrect": True},
                        {"text": "Le formateur en sécurité", "isCorrect": False},
                        {"text": "L'inspection du travail", "isCorrect": False},
                        {"text": "Le client final", "isCorrect": False}
                    ],
                    "correction": "L'employeur habilite son personnel sous sa responsabilité, après avis de formation."
                },
                {
                    "questionNumber": 19,
                    "question": "À quoi sert la mise à la terre et en court-circuit (MALT/CC) lors d'une consignation ?",
                    "answerOptions": [
                        {"text": "Évacuer les tensions induites et faire disjoncter en cas de remise sous tension", "isCorrect": True},
                        {"text": "Vérifier le bon fonctionnement du disjoncteur principal de l'installation", "isCorrect": False},
                        {"text": "Permettre aux outils électriques portatifs de fonctionner correctement", "isCorrect": False},
                        {"text": "Signaler visuellement aux autres intervenants que la zone est protégée", "isCorrect": False}
                    ],
                    "correction": "C'est une mesure de sauvegarde ultime contre les retours de tension accidentels."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est la conduite à tenir immédiate face à une personne électrisée 'collée' au conducteur ?",
                    "answerOptions": [
                        {"text": "Couper le courant sans toucher la victime", "isCorrect": True},
                        {"text": "Tirer la victime par ses vêtements", "isCorrect": False},
                        {"text": "Appeler les pompiers avant d'agir", "isCorrect": False},
                        {"text": "Verser de l'eau sur la victime", "isCorrect": False}
                    ],
                    "correction": "Priorité absolue : couper l'alimentation pour supprimer le danger sans se mettre en péril."
                },
            ]
        },
        # =========================================================================
        # THÈME 2 : LES LOIS FONDAMENTALES DE L'ÉLECTRICITÉ ET MESURES (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : LES LOIS FONDAMENTALES DE L'ÉLECTRICITÉ ET MESURES",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quelle est la formule correcte de la Loi d'Ohm ?",
                    "answerOptions": [
                        {"text": "U = R x I", "isCorrect": True},
                        {"text": "U = R / I", "isCorrect": False},
                        {"text": "U = I / R", "isCorrect": False},
                        {"text": "U = R + I", "isCorrect": False}
                    ],
                    "correction": "Tension (U) = Résistance (R) x Intensité (I)."
                },
                {
                    "questionNumber": 22,
                    "question": "Comment doit-on brancher un voltmètre pour mesurer une tension ?",
                    "answerOptions": [
                        {"text": "En dérivation", "isCorrect": True},
                        {"text": "En série", "isCorrect": False},
                        {"text": "En mixte", "isCorrect": False},
                        {"text": "En cascade", "isCorrect": False}
                    ],
                    "correction": "Le voltmètre se branche en parallèle (dérivation) du composant à mesurer."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle grandeur physique s'exprime en Watts ?",
                    "answerOptions": [
                        {"text": "La puissance", "isCorrect": True},
                        {"text": "La résistance", "isCorrect": False},
                        {"text": "L'intensité", "isCorrect": False},
                        {"text": "La tension", "isCorrect": False}
                    ],
                    "correction": "Le Watt (W) est l'unité de la puissance active."
                },
                {
                    "questionNumber": 24,
                    "question": "Calculer la puissance d'un radiateur alimenté en 230 V et consommant 10 A.",
                    "answerOptions": [
                        {"text": "2300 Watts", "isCorrect": True},
                        {"text": "23 Watts", "isCorrect": False},
                        {"text": "240 Watts", "isCorrect": False},
                        {"text": "220 Watts", "isCorrect": False}
                    ],
                    "correction": "P = U x I, soit 230 x 10 = 2300 W."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel est le comportement de l'intensité dans un circuit en série composé de trois résistances ?",
                    "answerOptions": [
                        {"text": "Elle est identique en tout point du circuit", "isCorrect": True},
                        {"text": "Elle diminue après chaque résistance traversée", "isCorrect": False},
                        {"text": "Elle s'additionne aux bornes de chaque résistance", "isCorrect": False},
                        {"text": "Elle est divisée par le nombre de récepteurs", "isCorrect": False}
                    ],
                    "correction": "Dans un circuit série (une seule boucle), l'intensité est la même partout."
                },
                {
                    "questionNumber": 26,
                    "question": "Quelle est la fonction principale d'une pince ampèremétrique ?",
                    "answerOptions": [
                        {"text": "Mesurer l'intensité sans ouvrir le circuit", "isCorrect": True},
                        {"text": "Mesurer la tension sans toucher les conducteurs", "isCorrect": False},
                        {"text": "Vérifier le serrage des bornes de connexion", "isCorrect": False},
                        {"text": "Dénuder les câbles de grosse section", "isCorrect": False}
                    ],
                    "correction": "Elle mesure le champ magnétique pour donner l'intensité sans couper le fil."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle est la résistance équivalente de deux résistances de 10 Ohms montées en série ?",
                    "answerOptions": [
                        {"text": "20 Ohms", "isCorrect": True},
                        {"text": "5 Ohms", "isCorrect": False},
                        {"text": "10 Ohms", "isCorrect": False},
                        {"text": "100 Ohms", "isCorrect": False}
                    ],
                    "correction": "En série, les résistances s'additionnent (R1 + R2)."
                },
                {
                    "questionNumber": 28,
                    "question": "Que désigne le sigle AC sur un appareil de mesure ?",
                    "answerOptions": [
                        {"text": "Courant Alternatif", "isCorrect": True},
                        {"text": "Courant Continu", "isCorrect": False},
                        {"text": "Courant Amplifié", "isCorrect": False},
                        {"text": "Courant Auxiliaire", "isCorrect": False}
                    ],
                    "correction": "AC = Alternating Current (Alternatif)."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle est la fréquence du réseau électrique domestique en France ?",
                    "answerOptions": [
                        {"text": "50 Hz", "isCorrect": True},
                        {"text": "60 Hz", "isCorrect": False},
                        {"text": "110 Hz", "isCorrect": False},
                        {"text": "24 Hz", "isCorrect": False}
                    ],
                    "correction": "La fréquence standard en Europe est de 50 Hertz."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle condition est impérative pour effectuer un test de continuité au multimètre (ohmmètre) ?",
                    "answerOptions": [
                        {"text": "Le circuit doit être hors tension", "isCorrect": True},
                        {"text": "Le circuit doit être sous tension", "isCorrect": False},
                        {"text": "Le disjoncteur doit être fermé", "isCorrect": False},
                        {"text": "L'appareil doit être sur le calibre Volts", "isCorrect": False}
                    ],
                    "correction": "Un ohmmètre ne doit jamais être utilisé sous tension (risque de destruction)."
                },
                {
                    "questionNumber": 31,
                    "question": "Quelle est la formule de l'énergie électrique consommée ?",
                    "answerOptions": [
                        {"text": "E = P x t", "isCorrect": True},
                        {"text": "E = P / t", "isCorrect": False},
                        {"text": "E = U / I", "isCorrect": False},
                        {"text": "E = R x I", "isCorrect": False}
                    ],
                    "correction": "L'énergie (E) est la puissance (P) multipliée par le temps (t)."
                },
                {
                    "questionNumber": 32,
                    "question": "Comment se comportent les tensions dans un circuit comportant plusieurs récepteurs montés en parallèle ?",
                    "answerOptions": [
                        {"text": "La tension est identique aux bornes de chaque récepteur", "isCorrect": True},
                        {"text": "La tension se divise selon la valeur des résistances", "isCorrect": False},
                        {"text": "La tension s'additionne pour atteindre la tension du générateur", "isCorrect": False},
                        {"text": "La tension chute progressivement d'un récepteur à l'autre", "isCorrect": False}
                    ],
                    "correction": "En parallèle, la tension est la même aux bornes de chaque branche."
                },
                {
                    "questionNumber": 33,
                    "question": "Quel phénomène est décrit par l'effet Joule ?",
                    "answerOptions": [
                        {"text": "Le dégagement de chaleur provoqué par le passage du courant", "isCorrect": True},
                        {"text": "La création d'un champ magnétique autour d'une bobine", "isCorrect": False},
                        {"text": "L'attraction électrostatique entre deux charges opposées", "isCorrect": False},
                        {"text": "La production d'électricité à partir de la lumière", "isCorrect": False}
                    ],
                    "correction": "L'effet Joule est la transformation d'énergie électrique en chaleur."
                },
                {
                    "questionNumber": 34,
                    "question": "Si je mesure une tension entre deux phases sur un réseau triphasé 400V, quelle valeur vais-je trouver ?",
                    "answerOptions": [
                        {"text": "400 Volts", "isCorrect": True},
                        {"text": "230 Volts", "isCorrect": False},
                        {"text": "690 Volts", "isCorrect": False},
                        {"text": "12 Volts", "isCorrect": False}
                    ],
                    "correction": "La tension composée (Phase-Phase) est de 400V."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle est la résistance équivalente de deux résistances de 10 Ohms montées en parallèle ?",
                    "answerOptions": [
                        {"text": "5 Ohms", "isCorrect": True},
                        {"text": "20 Ohms", "isCorrect": False},
                        {"text": "10 Ohms", "isCorrect": False},
                        {"text": "1 Ohm", "isCorrect": False}
                    ],
                    "correction": "Deux résistances identiques en parallèle divisent la résistance par 2 (R/n)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel est le symbole normalisé pour une tension continue sur un multimètre ?",
                    "answerOptions": [
                        {"text": "V avec deux traits dont un pointillé", "isCorrect": True},
                        {"text": "V avec une vague sinusoïdale", "isCorrect": False},
                        {"text": "A avec une ligne droite", "isCorrect": False},
                        {"text": "Hz avec un cercle", "isCorrect": False}
                    ],
                    "correction": "Le symbole DC est un trait continu sur un trait pointillé."
                },
                {
                    "questionNumber": 37,
                    "question": "Quelle relation lie la période (T) et la fréquence (f) ?",
                    "answerOptions": [
                        {"text": "f = 1 / T", "isCorrect": True},
                        {"text": "f = T x 1", "isCorrect": False},
                        {"text": "f = T + 1", "isCorrect": False},
                        {"text": "f = T / 2", "isCorrect": False}
                    ],
                    "correction": "La fréquence est l'inverse de la période."
                },
                {
                    "questionNumber": 38,
                    "question": "Pour mesurer un courant de fuite très faible, quel calibre est le plus adapté ?",
                    "answerOptions": [
                        {"text": "Milliampères", "isCorrect": True},
                        {"text": "Kiloampères", "isCorrect": False},
                        {"text": "Mégawatts", "isCorrect": False},
                        {"text": "Kilovolts", "isCorrect": False}
                    ],
                    "correction": "Les courants de fuite se mesurent en milliampères (mA)."
                },
                {
                    "questionNumber": 39,
                    "question": "Si la longueur d'un câble augmente, comment varie sa résistance électrique ?",
                    "answerOptions": [
                        {"text": "Elle augmente", "isCorrect": True},
                        {"text": "Elle diminue", "isCorrect": False},
                        {"text": "Elle reste stable", "isCorrect": False},
                        {"text": "Elle devient nulle", "isCorrect": False}
                    ],
                    "correction": "La résistance est proportionnelle à la longueur du conducteur."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel appareil permet de visualiser la forme d'un signal électrique (sinusoïdal, carré...) ?",
                    "answerOptions": [
                        {"text": "Un oscilloscope", "isCorrect": True},
                        {"text": "Un ohmmètre", "isCorrect": False},
                        {"text": "Un wattmètre", "isCorrect": False},
                        {"text": "Un contrôleur de rotation", "isCorrect": False}
                    ],
                    "correction": "L'oscilloscope affiche la courbe de la tension en fonction du temps."
                },
            ]
        },
        # =========================================================================
        # THÈME 3 : TECHNOLOGIE DE L'APPAREILLAGE ET DES CANALISATIONS (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : TECHNOLOGIE DE L'APPAREILLAGE ET DES CANALISATIONS",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quelle est la fonction exacte d'un télérupteur dans une installation d'éclairage ?",
                    "answerOptions": [
                        {"text": "Permettre l'allumage et l'extinction depuis plus de deux endroits différents", "isCorrect": True},
                        {"text": "Éteindre automatiquement la lumière après une durée programmée", "isCorrect": False},
                        {"text": "Varier l'intensité lumineuse de l'ampoule", "isCorrect": False},
                        {"text": "Détecter le passage d'une personne", "isCorrect": False}
                    ],
                    "correction": "Le télérupteur (relais bistable) permet une commande multipoints par boutons poussoirs."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel type de conduit est obligatoirement requis pour une pose encastrée dans le béton ?",
                    "answerOptions": [
                        {"text": "ICTA", "isCorrect": True},
                        {"text": "IRO", "isCorrect": False},
                        {"text": "IRL", "isCorrect": False},
                        {"text": "MRL", "isCorrect": False}
                    ],
                    "correction": "La gaine ICTA est cintrable et résistante à l'écrasement du béton."
                },
                {
                    "questionNumber": 43,
                    "question": "Quelle est la section minimale normalisée pour alimenter un circuit de prises de courant 16 A ?",
                    "answerOptions": [
                        {"text": "1,5 mm²", "isCorrect": True},
                        {"text": "0,75 mm²", "isCorrect": False},
                        {"text": "6 mm²", "isCorrect": False},
                        {"text": "10 mm²", "isCorrect": False}
                    ],
                    "correction": "Le 1,5 mm² est autorisé pour les circuits prises (jusqu'à 8 socles)."
                },
                {
                    "questionNumber": 44,
                    "question": "Que signifie le chiffre 4 dans l'indice de protection IP44 ?",
                    "answerOptions": [
                        {"text": "Protection contre les corps solides supérieurs à 1 mm", "isCorrect": True},
                        {"text": "Protection totale contre la poussière fine", "isCorrect": False},
                        {"text": "Protection contre l'immersion prolongée", "isCorrect": False},
                        {"text": "Protection contre les chocs mécaniques", "isCorrect": False}
                    ],
                    "correction": "Le 1er chiffre concerne les corps solides (>1mm)."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel câble rigide est le plus couramment utilisé pour les installations fixes domestiques et tertiaires ?",
                    "answerOptions": [
                        {"text": "R2V", "isCorrect": True},
                        {"text": "H07RN-F", "isCorrect": False},
                        {"text": "H03VVH2-F", "isCorrect": False},
                        {"text": "H05VV-F", "isCorrect": False}
                    ],
                    "correction": "Le U-1000 R2V (RO2V) est le standard rigide pour l'installation fixe."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la particularité d'un interrupteur différentiel de Type A par rapport à un Type AC ?",
                    "answerOptions": [
                        {"text": "Il détecte les fuites de courant continu", "isCorrect": True},
                        {"text": "Il est beaucoup moins sensible aux déclenchements", "isCorrect": False},
                        {"text": "Il ne protège que contre les courts-circuits", "isCorrect": False},
                        {"text": "Il est réservé exclusivement au chauffage électrique", "isCorrect": False}
                    ],
                    "correction": "Le Type A détecte les composantes continues (Lave-linge, Plaque, IRVE)."
                },
                {
                    "questionNumber": 47,
                    "question": "Comment repère-t-on physiquement le conducteur neutre dans un câble multipolaire ?",
                    "answerOptions": [
                        {"text": "Par sa couleur bleue", "isCorrect": True},
                        {"text": "Par sa couleur rouge", "isCorrect": False},
                        {"text": "Par sa section plus petite", "isCorrect": False},
                        {"text": "Par une bague noire", "isCorrect": False}
                    ],
                    "correction": "Le Bleu est réservé exclusivement au Neutre."
                },
                {
                    "questionNumber": 48,
                    "question": "Quel est le rôle de la chambre de coupure dans un disjoncteur magnéto-thermique ?",
                    "answerOptions": [
                        {"text": "Éteindre l'arc électrique", "isCorrect": True},
                        {"text": "Refroidir le levier de commande", "isCorrect": False},
                        {"text": "Stocker l'énergie mécanique", "isCorrect": False},
                        {"text": "Mesurer la température ambiante", "isCorrect": False}
                    ],
                    "correction": "Elle fractionne et refroidit l'arc électrique lors de l'ouverture."
                },
                {
                    "questionNumber": 49,
                    "question": "Sur quel principe fonctionne le déclenchement 'magnétique' d'un disjoncteur ?",
                    "answerOptions": [
                        {"text": "Une forte augmentation brutale du courant", "isCorrect": True},
                        {"text": "Une élévation lente et progressive du courant", "isCorrect": False},
                        {"text": "Une baisse de la tension du réseau", "isCorrect": False},
                        {"text": "Une fuite de courant vers la terre", "isCorrect": False}
                    ],
                    "correction": "Le magnétique protège contre les courts-circuits (hausse brutale)."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle cheville est adaptée pour fixer une goulotte sur une cloison sèche en plaque de plâtre ?",
                    "answerOptions": [
                        {"text": "Molly", "isCorrect": True},
                        {"text": "Crampon", "isCorrect": False},
                        {"text": "Goujon", "isCorrect": False},
                        {"text": "Tire-fond", "isCorrect": False}
                    ],
                    "correction": "La cheville à expansion (Molly) s'ouvre derrière la plaque pour résister à l'arrachement."
                },
                {
                    "questionNumber": 51,
                    "question": "À quoi sert un contacteur Jour Nuit dans un tableau électrique ?",
                    "answerOptions": [
                        {"text": "Alimenter le chauffe-eau uniquement pendant les heures creuses", "isCorrect": True},
                        {"text": "Couper automatiquement le courant en cas d'absence prolongée", "isCorrect": False},
                        {"text": "Allumer l'éclairage extérieur dès que la nuit tombe", "isCorrect": False},
                        {"text": "Réguler la température du chauffage au sol", "isCorrect": False}
                    ],
                    "correction": "Il asservit le fonctionnement du chauffe-eau au signal tarifaire réduit."
                },
                {
                    "questionNumber": 52,
                    "question": "Quelle est la signification du sigle DCL ?",
                    "answerOptions": [
                        {"text": "Dispositif de Connexion Luminaire", "isCorrect": True},
                        {"text": "Détecteur de Court-circuit Localisé", "isCorrect": False},
                        {"text": "Disjoncteur de Contrôle de Ligne", "isCorrect": False},
                        {"text": "Domotique Câblée en Ligne", "isCorrect": False}
                    ],
                    "correction": "Le DCL permet de raccorder les luminaires sans outil via une fiche."
                },
                {
                    "questionNumber": 53,
                    "question": "Pour quelle application utilise-t-on un câble de catégorie 6 avec connecteurs RJ45 ?",
                    "answerOptions": [
                        {"text": "Réseau VDI", "isCorrect": True},
                        {"text": "Alimentation four", "isCorrect": False},
                        {"text": "Circuit éclairage", "isCorrect": False},
                        {"text": "Chauffage", "isCorrect": False}
                    ],
                    "correction": "Pour le réseau Voix Données Images (Internet, Téléphone, TV)."
                },
                {
                    "questionNumber": 54,
                    "question": "Quelle est la caractéristique principale d'un bouton poussoir par rapport à un interrupteur simple ?",
                    "answerOptions": [
                        {"text": "Il revient à sa position initiale après relâchement", "isCorrect": True},
                        {"text": "Il maintient le contact fermé indéfiniment", "isCorrect": False},
                        {"text": "Il possède obligatoirement trois bornes de connexion", "isCorrect": False},
                        {"text": "Il ne peut pas couper la phase directement", "isCorrect": False}
                    ],
                    "correction": "Le bouton poussoir est un contact monostable (impulsion)."
                },
                {
                    "questionNumber": 55,
                    "question": "Que désigne l'indice IK sur un appareillage électrique ?",
                    "answerOptions": [
                        {"text": "La résistance aux chocs mécaniques", "isCorrect": True},
                        {"text": "La résistance au feu et à la chaleur", "isCorrect": False},
                        {"text": "La protection contre les produits chimiques", "isCorrect": False},
                        {"text": "La qualité de l'isolation électrique", "isCorrect": False}
                    ],
                    "correction": "L'indice IK définit la tenue aux impacts (chocs)."
                },
                {
                    "questionNumber": 56,
                    "question": "Dans la désignation d'un conduit IRL 3321, que signifie la lettre I ?",
                    "answerOptions": [
                        {"text": "Isolant", "isCorrect": True},
                        {"text": "Inifugé", "isCorrect": False},
                        {"text": "Inoxydable", "isCorrect": False},
                        {"text": "Intérieur", "isCorrect": False}
                    ],
                    "correction": "IRL = Isolant Rigide Lisse."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel outil est spécifiquement conçu pour retirer la gaine isolante d'un câble sans abîmer les conducteurs internes ?",
                    "answerOptions": [
                        {"text": "Un jokari", "isCorrect": True},
                        {"text": "Une pince coupante diagonale", "isCorrect": False},
                        {"text": "Un tournevis plat isolé", "isCorrect": False},
                        {"text": "Une scie à métaux junior", "isCorrect": False}
                    ],
                    "correction": "Le couteau à dégainer (Jokari) permet une incision précise de la gaine."
                },
                {
                    "questionNumber": 58,
                    "question": "Pourquoi est-il interdit de mettre deux fils de sections différentes dans la même borne d'un disjoncteur à vis ?",
                    "answerOptions": [
                        {"text": "Le mauvais serrage du plus petit fil provoque un échauffement", "isCorrect": True},
                        {"text": "Cela modifie la tension de sortie du disjoncteur", "isCorrect": False},
                        {"text": "Le courant ne passera que dans le gros fil", "isCorrect": False},
                        {"text": "Cela annule la garantie du fabricant du tableau", "isCorrect": False}
                    ],
                    "correction": "Le petit fil sera mal serré, créant une résistance de contact et un risque de feu."
                },
                {
                    "questionNumber": 59,
                    "question": "Quel est l'avantage des bornes de connexion automatique (type Wago) par rapport aux dominos à vis ?",
                    "answerOptions": [
                        {"text": "Elles garantissent une pression de contact constante dans le temps", "isCorrect": True},
                        {"text": "Elles permettent de relier des fils d'aluminium et de cuivre ensemble", "isCorrect": False},
                        {"text": "Elles supportent des intensités infinies sans chauffer", "isCorrect": False},
                        {"text": "Elles sont obligatoires pour les câbles de section supérieure à 6 mm²", "isCorrect": False}
                    ],
                    "correction": "Le ressort maintient la pression et évite le desserrage."
                },
                {
                    "questionNumber": 60,
                    "question": "Sur un schéma électrique, par quelle lettre désigne-t-on généralement un fusible ?",
                    "answerOptions": [
                        {"text": "F", "isCorrect": True},
                        {"text": "Q", "isCorrect": False},
                        {"text": "K", "isCorrect": False},
                        {"text": "S", "isCorrect": False}
                    ],
                    "correction": "F pour les protections (Fusibles), Q pour les disjoncteurs."
                },
            ]
        },
        # =========================================================================
        # THÈME 4 : LECTURE DE SCHÉMAS ET DOSSIERS TECHNIQUES (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : LECTURE DE SCHÉMAS ET DOSSIERS TECHNIQUES",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Sur un plan architectural, que représente un cercle traversé par deux traits perpendiculaires formant une croix à l'intérieur ?",
                    "answerOptions": [
                        {"text": "Un bouton poussoir", "isCorrect": True},
                        {"text": "Un interrupteur simple allumage", "isCorrect": False},
                        {"text": "Un va et vient", "isCorrect": False},
                        {"text": "Une prise de courant confort", "isCorrect": False}
                    ],
                    "correction": "La croix (X) dans le cercle est le symbole du bouton poussoir."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la particularité d'un schéma unifilaire ?",
                    "answerOptions": [
                        {"text": "Un seul trait représente l'ensemble des conducteurs d'une même canalisation", "isCorrect": True},
                        {"text": "Il ne représente que la phase et jamais le neutre ni la terre", "isCorrect": False},
                        {"text": "Il est utilisé uniquement pour les circuits de très basse tension", "isCorrect": False},
                        {"text": "Il oblige à dessiner un trait distinct pour chaque fil électrique présent", "isCorrect": False}
                    ],
                    "correction": "Un trait unique représente la canalisation, barré pour indiquer le nombre de fils."
                },
                {
                    "questionNumber": 63,
                    "question": "Selon la norme CEI 61346, quelle lettre repère désigne un disjoncteur sur un schéma électrique industriel ?",
                    "answerOptions": [
                        {"text": "Q", "isCorrect": True},
                        {"text": "K", "isCorrect": False},
                        {"text": "H", "isCorrect": False},
                        {"text": "S", "isCorrect": False}
                    ],
                    "correction": "Q désigne les appareils de commutation de puissance."
                },
                {
                    "questionNumber": 64,
                    "question": "Sur un schéma développé, comment sont repérées les bornes de la bobine d'un contacteur ?",
                    "answerOptions": [
                        {"text": "A1 et A2", "isCorrect": True},
                        {"text": "13 et 14", "isCorrect": False},
                        {"text": "L1 et L2", "isCorrect": False},
                        {"text": "T1 et T2", "isCorrect": False}
                    ],
                    "correction": "A1 et A2 sont les bornes normalisées de la bobine."
                },
                {
                    "questionNumber": 65,
                    "question": "Si un plan est à l'échelle 1/50, quelle longueur réelle représente un trait de 2 cm sur le papier ?",
                    "answerOptions": [
                        {"text": "1 mètre", "isCorrect": True},
                        {"text": "50 centimètres", "isCorrect": False},
                        {"text": "2 mètres", "isCorrect": False},
                        {"text": "10 mètres", "isCorrect": False}
                    ],
                    "correction": "1 cm plan = 50 cm réel. 2 cm plan = 100 cm réel = 1 m."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel symbole représente une prise de courant avec terre sur un plan d'installation domestique ?",
                    "answerOptions": [
                        {"text": "Un cercle avec un trait qui en sort perpendiculairement vers l'intérieur", "isCorrect": True},
                        {"text": "Un triangle équilatéral plein orienté vers le bas", "isCorrect": False},
                        {"text": "Un carré simple sans aucune inscription à l'intérieur", "isCorrect": False},
                        {"text": "Un rectangle barré d'une croix en diagonale", "isCorrect": False}
                    ],
                    "correction": "Cercle + tige intérieure = Prise avec Terre."
                },
                {
                    "questionNumber": 67,
                    "question": "Que signifient les chiffres 13 et 14 sur un contact auxiliaire ?",
                    "answerOptions": [
                        {"text": "Un contact à fermeture ou Normalement Ouvert", "isCorrect": True},
                        {"text": "Un contact à ouverture ou Normalement Fermé", "isCorrect": False},
                        {"text": "Les bornes d'alimentation de la bobine", "isCorrect": False},
                        {"text": "Les bornes de puissance du moteur", "isCorrect": False}
                    ],
                    "correction": "Terminant par 3-4 = Contact NO (Normalement Ouvert)."
                },
                {
                    "questionNumber": 68,
                    "question": "Sur un schéma de tableau électrique, que représente le symbole d'un interrupteur accompagné d'un 'T' majuscule ?",
                    "answerOptions": [
                        {"text": "Un télérupteur", "isCorrect": True},
                        {"text": "Un transformateur", "isCorrect": False},
                        {"text": "Un thermostat", "isCorrect": False},
                        {"text": "Une terre", "isCorrect": False}
                    ],
                    "correction": "Le T signale la commande par impulsion (Télérupteur)."
                },
                {
                    "questionNumber": 69,
                    "question": "Quelle information essentielle le 'cartouche' d'un plan technique ne contient-il PAS habituellement ?",
                    "answerOptions": [
                        {"text": "Le prix du matériel", "isCorrect": True},
                        {"text": "Le titre du projet", "isCorrect": False},
                        {"text": "L'échelle du dessin", "isCorrect": False},
                        {"text": "Le nom du dessinateur", "isCorrect": False}
                    ],
                    "correction": "Le cartouche contient les infos techniques, jamais les prix."
                },
                {
                    "questionNumber": 70,
                    "question": "Sur un schéma architectural, que signifient des traits pointillés reliant plusieurs luminaires à un interrupteur ?",
                    "answerOptions": [
                        {"text": "La dépendance fonctionnelle entre la commande et les lampes", "isCorrect": True},
                        {"text": "Le passage des gaines dans le vide sanitaire", "isCorrect": False},
                        {"text": "Une installation provisoire de chantier", "isCorrect": False},
                        {"text": "Des fils à supprimer lors de la rénovation", "isCorrect": False}
                    ],
                    "correction": "Ils indiquent la logique de commande (qui allume quoi)."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle est la différence entre un schéma de principe et un schéma de réalisation ?",
                    "answerOptions": [
                        {"text": "Le schéma de principe explique le fonctionnement logique alors que celui de réalisation guide le câblage", "isCorrect": True},
                        {"text": "Le schéma de principe est réservé aux ingénieurs et celui de réalisation aux clients", "isCorrect": False},
                        {"text": "Le schéma de principe utilise des photos réelles et celui de réalisation des symboles", "isCorrect": False},
                        {"text": "Le schéma de principe est toujours en couleur et celui de réalisation en noir et blanc", "isCorrect": False}
                    ],
                    "correction": "Principe = Logique / Réalisation = Câblage physique."
                },
                {
                    "questionNumber": 72,
                    "question": "Que désigne le repère 'PC' souvent utilisé sur les plans d'implantation ?",
                    "answerOptions": [
                        {"text": "Prise de Courant", "isCorrect": True},
                        {"text": "Poste de Commande", "isCorrect": False},
                        {"text": "Point Centre", "isCorrect": False},
                        {"text": "Protection Circuit", "isCorrect": False}
                    ],
                    "correction": "PC = Prise de Courant."
                },
                {
                    "questionNumber": 73,
                    "question": "Dans un dossier technique, qu'est-ce que la nomenclature ?",
                    "answerOptions": [
                        {"text": "La liste détaillée de tout le matériel nécessaire avec références et quantités", "isCorrect": True},
                        {"text": "Le résumé écrit du fonctionnement de l'installation électrique", "isCorrect": False},
                        {"text": "La liste des personnes habilitées à travailler sur le chantier", "isCorrect": False},
                        {"text": "Le document qui certifie la conformité à la norme NF C 15-100", "isCorrect": False}
                    ],
                    "correction": "La nomenclature sert à commander le matériel."
                },
                {
                    "questionNumber": 74,
                    "question": "Comment représente-t-on un croisement de fils sans connexion électrique sur un schéma ?",
                    "answerOptions": [
                        {"text": "Par deux traits qui se croisent simplement sans point", "isCorrect": True},
                        {"text": "Par un gros point noir à l'intersection", "isCorrect": False},
                        {"text": "Par un petit pont dessinée sur l'un des fils", "isCorrect": False},
                        {"text": "Par une interruption du trait vertical", "isCorrect": False}
                    ],
                    "correction": "Croisement sans point = Pas de contact."
                },
                {
                    "questionNumber": 75,
                    "question": "Sur un schéma, quel symbole est constitué de trois traits obliques parallèles sur un trait continu ?",
                    "answerOptions": [
                        {"text": "Trois conducteurs", "isCorrect": True},
                        {"text": "Une protection 30 mA", "isCorrect": False},
                        {"text": "Un interrupteur triple", "isCorrect": False},
                        {"text": "Une tension de 300 Volts", "isCorrect": False}
                    ],
                    "correction": "Indique la présence de 3 conducteurs."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle lettre repère est attribuée aux voyants lumineux de signalisation ?",
                    "answerOptions": [
                        {"text": "H", "isCorrect": True},
                        {"text": "V", "isCorrect": False},
                        {"text": "L", "isCorrect": False},
                        {"text": "X", "isCorrect": False}
                    ],
                    "correction": "H est la lettre pour la signalisation."
                },
                {
                    "questionNumber": 77,
                    "question": "Sur un plan, qu'indique un symbole de luminaire avec la mention '2x36W' ?",
                    "answerOptions": [
                        {"text": "Un luminaire comportant deux tubes ou ampoules de 36 Watts chacun", "isCorrect": True},
                        {"text": "Deux luminaires distincts de 36 Watts placés côte à côte", "isCorrect": False},
                        {"text": "Un luminaire de 72 Watts fonctionnant sous 36 Volts", "isCorrect": False},
                        {"text": "Un luminaire de secours avec 36 Watts de batterie", "isCorrect": False}
                    ],
                    "correction": "2 sources de 36W dans le même appareil."
                },
                {
                    "questionNumber": 78,
                    "question": "Que représente le symbole de la 'Terre' (masse) ?",
                    "answerOptions": [
                        {"text": "Des traits horizontaux parallèles de longueur décroissante formant un triangle inversé", "isCorrect": True},
                        {"text": "Un cercle avec un éclair à l'intérieur", "isCorrect": False},
                        {"text": "Un carré avec la lettre T majuscule", "isCorrect": False},
                        {"text": "Une flèche ondulée vers le bas", "isCorrect": False}
                    ],
                    "correction": "Symbole universel de la terre."
                },
                {
                    "questionNumber": 79,
                    "question": "Que signifie le symbole d'un rectangle coupé en deux par une ligne diagonale dans un tableau de distribution ?",
                    "answerOptions": [
                        {"text": "Le tableau de répartition lui-même", "isCorrect": True},
                        {"text": "Une boîte de dérivation", "isCorrect": False},
                        {"text": "Un coffret de comptage", "isCorrect": False},
                        {"text": "Un local technique", "isCorrect": False}
                    ],
                    "correction": "Symbole architectural du tableau électrique."
                },
                {
                    "questionNumber": 80,
                    "question": "Pourquoi utilise-t-on le repérage équipotentiel sur les schémas complexes ?",
                    "answerOptions": [
                        {"text": "Pour identifier un fil par son numéro de potentiel électrique unique quel que soit l'endroit", "isCorrect": True},
                        {"text": "Pour connaître la longueur exacte du fil à couper", "isCorrect": False},
                        {"text": "Pour distinguer les fils de marque différente", "isCorrect": False},
                        {"text": "Pour savoir si le fil est en cuivre ou en aluminium", "isCorrect": False}
                    ],
                    "correction": "Tous les points connectés électriquement portent le même numéro."
                },
            ]
        },
        # =========================================================================
        # THÈME 5 : LA NORME NF C 15-100 ET TECHNIQUES DE RÉALISATION (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : LA NORME NF C 15-100 ET TECHNIQUES DE RÉALISATION",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Selon la norme NF C 15-100, combien de socles de prises de courant 16 A peut-on câbler au maximum sur un disjoncteur de 20 A avec du fil de 2,5 mm² ?",
                    "answerOptions": [
                        {"text": "12", "isCorrect": True},
                        {"text": "8", "isCorrect": False},
                        {"text": "5", "isCorrect": False},
                        {"text": "10", "isCorrect": False}
                    ],
                    "correction": "Max 12 prises en 2,5 mm² (et 8 prises en 1,5 mm²)."
                },
                {
                    "questionNumber": 82,
                    "question": "Dans une salle de bain, dans quel volume est-il strictement interdit d'installer une prise de courant standard ?",
                    "answerOptions": [
                        {"text": "Volume 0 et 1", "isCorrect": True},
                        {"text": "Hors volume", "isCorrect": False},
                        {"text": "Volume caché", "isCorrect": False},
                        {"text": "Volume extérieur", "isCorrect": False}
                    ],
                    "correction": "Interdit dans les volumes 0 et 1 (proximité immédiate eau)."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle est la section minimale des conducteurs en cuivre pour alimenter une plaque de cuisson électrique de 32 A ?",
                    "answerOptions": [
                        {"text": "6 mm²", "isCorrect": True},
                        {"text": "4 mm²", "isCorrect": False},
                        {"text": "2,5 mm²", "isCorrect": False},
                        {"text": "10 mm²", "isCorrect": False}
                    ],
                    "correction": "Circuit 32 A = Section 6 mm²."
                },
                {
                    "questionNumber": 84,
                    "question": "À quelle hauteur du sol fini doit être positionnée l'axe des prises de courant 16 A dans une cuisine ?",
                    "answerOptions": [
                        {"text": "Au maximum à 1,30 m", "isCorrect": True},
                        {"text": "Au maximum à 1,80 m", "isCorrect": False},
                        {"text": "Au minimum à 5 cm", "isCorrect": False},
                        {"text": "Au minimum à 25 cm", "isCorrect": False}
                    ],
                    "correction": "Accessibilité PMR max 1,30 m."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle couleur de grillage avertisseur doit-on placer au-dessus d'une gaine électrique enterrée en extérieur ?",
                    "answerOptions": [
                        {"text": "Rouge", "isCorrect": True},
                        {"text": "Bleu", "isCorrect": False},
                        {"text": "Jaune", "isCorrect": False},
                        {"text": "Vert", "isCorrect": False}
                    ],
                    "correction": "Rouge = Électricité."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel est le nombre minimal de prises de courant obligatoires dans une chambre à coucher standard ?",
                    "answerOptions": [
                        {"text": "3", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "4", "isCorrect": False}
                    ],
                    "correction": "Minimum 3 prises dans une chambre."
                },
                {
                    "questionNumber": 87,
                    "question": "Qu'est-ce que la Liaison Équipotentielle Supplémentaire (LES) ?",
                    "answerOptions": [
                        {"text": "Une connexion reliant entre eux tous les éléments conducteurs de la salle de bain à la terre", "isCorrect": True},
                        {"text": "Un câble qui relie le compteur Linky au disjoncteur d'abonné", "isCorrect": False},
                        {"text": "Une liaison informatique entre le tableau de communication et la télévision", "isCorrect": False},
                        {"text": "Un fil de fer qui maintient les gaines techniques solidaires entre elles", "isCorrect": False}
                    ],
                    "correction": "Elle met au même potentiel tous les éléments métalliques de la salle d'eau."
                },
                {
                    "questionNumber": 88,
                    "question": "Quel appareil de protection est obligatoire en tête de tous les circuits d'éclairage et de prises dans un logement neuf ?",
                    "answerOptions": [
                        {"text": "Un interrupteur différentiel 30 mA", "isCorrect": True},
                        {"text": "Un disjoncteur de branchement 500 mA", "isCorrect": False},
                        {"text": "Un parafoudre de type 1", "isCorrect": False},
                        {"text": "Un sectionneur porte fusible", "isCorrect": False}
                    ],
                    "correction": "Protection différentielle 30 mA obligatoire pour les circuits terminaux."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle est la règle de remplissage des conduits (gaines) selon la norme ?",
                    "answerOptions": [
                        {"text": "Laisser un tiers de la section vide", "isCorrect": True},
                        {"text": "Remplir la gaine au maximum possible", "isCorrect": False},
                        {"text": "Laisser un espace de 1 millimètre", "isCorrect": False},
                        {"text": "Ne passer qu'un seul fil par gaine", "isCorrect": False}
                    ],
                    "correction": "Règle du tiers vide pour faciliter le tirage."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel espace est réservé pour l'installation du tableau électrique et du panneau de contrôle dans le logement ?",
                    "answerOptions": [
                        {"text": "ETEL", "isCorrect": True},
                        {"text": "GTL", "isCorrect": False},
                        {"text": "VMC", "isCorrect": False},
                        {"text": "TGBT", "isCorrect": False}
                    ],
                    "correction": "Espace Technique Électrique du Logement (ETEL)."
                },
                {
                    "questionNumber": 91,
                    "question": "Est-il autorisé d'utiliser le conducteur vert et jaune comme fil navette pour un va-et-vient ?",
                    "answerOptions": [
                        {"text": "Non jamais", "isCorrect": True},
                        {"text": "Oui si on met du scotch rouge au bout", "isCorrect": False},
                        {"text": "Oui si c'est du courant continu", "isCorrect": False},
                        {"text": "Oui si la section est supérieure à 2,5 mm²", "isCorrect": False}
                    ],
                    "correction": "Le Vert/Jaune est exclusif à la Terre. Interdiction formelle de détourner son usage."
                },
                {
                    "questionNumber": 92,
                    "question": "Quel circuit spécialisé nécessite obligatoirement un disjoncteur 20 A et du fil de 2,5 mm² ?",
                    "answerOptions": [
                        {"text": "Le lave linge", "isCorrect": True},
                        {"text": "Le volet roulant", "isCorrect": False},
                        {"text": "La sonnette", "isCorrect": False},
                        {"text": "La VMC", "isCorrect": False}
                    ],
                    "correction": "Les gros électroménagers (Lave-linge, LV, Four, SL) nécessitent un circuit spécialisé."
                },
                {
                    "questionNumber": 93,
                    "question": "Dans quel cas l'installation d'un parafoudre est-elle obligatoire dans le tableau électrique domestique ?",
                    "answerOptions": [
                        {"text": "Si le bâtiment est équipé d'un paratonnerre ou situé en zone à risque kéraunique élevé", "isCorrect": True},
                        {"text": "Si le logement fait plus de 100 mètres carrés habitables", "isCorrect": False},
                        {"text": "Si le compteur électrique est situé à l'extérieur de la maison", "isCorrect": False},
                        {"text": "Si l'installation comporte plus de trois rangées de disjoncteurs", "isCorrect": False}
                    ],
                    "correction": "Obligatoire en zone AQ2 (orages fréquents) ou présence paratonnerre."
                },
                {
                    "questionNumber": 94,
                    "question": "Comment doit-on fixer les câbles dans les vides de construction (faux-plafonds) ?",
                    "answerOptions": [
                        {"text": "Ils peuvent être posés directement mais doivent être fixés s'ils risquent d'être endommagés", "isCorrect": True},
                        {"text": "Ils doivent être tendus comme des cordes à piano", "isCorrect": False},
                        {"text": "Ils doivent être noyés dans le plâtre", "isCorrect": False},
                        {"text": "Ils doivent être collés à la colle néoprène", "isCorrect": False}
                    ],
                    "correction": "Les câbles peuvent être posés libres ou fixés, mais doivent rester visitables."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle est la hauteur réglementaire de pose de l'organe de coupure d'urgence (AGCP ou disjoncteur d'abonné) ?",
                    "answerOptions": [
                        {"text": "Entre 0,90 m et 1,80 m", "isCorrect": True},
                        {"text": "Entre 0,50 m et 1,50 m", "isCorrect": False},
                        {"text": "Entre 1,00 m et 2,00 m", "isCorrect": False},
                        {"text": "Entre 0,10 m et 1,00 m", "isCorrect": False}
                    ],
                    "correction": "Hauteur accessible : 0,90 m à 1,80 m."
                },
                {
                    "questionNumber": 96,
                    "question": "Quelle est la fonction du Consuel ?",
                    "answerOptions": [
                        {"text": "Viser l'attestation de conformité de l'installation électrique avant la mise sous tension", "isCorrect": True},
                        {"text": "Fournir l'électricité aux particuliers et aux entreprises", "isCorrect": False},
                        {"text": "Vendre le matériel électrique aux professionnels", "isCorrect": False},
                        {"text": "Former les apprentis électriciens", "isCorrect": False}
                    ],
                    "correction": "Le CONSUEL vérifie la conformité des installations neuves."
                },
                {
                    "questionNumber": 97,
                    "question": "Combien de circuits spécialisés au minimum doit comporter un logement T3 (F3) ?",
                    "answerOptions": [
                        {"text": "4", "isCorrect": True},
                        {"text": "2", "isCorrect": False},
                        {"text": "1", "isCorrect": False},
                        {"text": "10", "isCorrect": False}
                    ],
                    "correction": "Minimum 4 (1x32A + 3x16/20A)."
                },
                {
                    "questionNumber": 98,
                    "question": "Peut-on installer une prise de communication (RJ45) dans la cuisine ?",
                    "answerOptions": [
                        {"text": "Oui c'est obligatoire", "isCorrect": True},
                        {"text": "Non c'est interdit à cause de l'eau", "isCorrect": False},
                        {"text": "Non c'est inutile", "isCorrect": False},
                        {"text": "Oui mais uniquement dans un placard", "isCorrect": False}
                    ],
                    "correction": "Obligatoire dans la cuisine pour les T2 et plus."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle est la distance maximale autorisée entre deux fixations (colliers) pour un tube IRL en pose apparente horizontale ?",
                    "answerOptions": [
                        {"text": "0,80 m", "isCorrect": True},
                        {"text": "2,00 m", "isCorrect": False},
                        {"text": "0,20 m", "isCorrect": False},
                        {"text": "1,50 m", "isCorrect": False}
                    ],
                    "correction": "Environ 80 cm pour éviter le fléchissement."
                },
                {
                    "questionNumber": 100,
                    "question": "Que doit posséder tout socle de prise de courant 16 A installé dans un logement neuf ?",
                    "answerOptions": [
                        {"text": "Des obturateurs de sécurité (éclipses)", "isCorrect": True},
                        {"text": "Un voyant lumineux de présence tension", "isCorrect": False},
                        {"text": "Un fusible intégré en verre", "isCorrect": False},
                        {"text": "Un port USB pour la recharge", "isCorrect": False}
                    ],
                    "correction": "Les éclipses de protection (sécurité enfant) sont obligatoires."
                },
            ]
        }
    }
}