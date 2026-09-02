quiz_data = {
    "title": "Quiz Bac Pro Bac Pro Carrossier / Peintre Automobile (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : PRÉVENTION, SÉCURITÉ D'ATELIER, RÉGLEMENTATION ET PRISE EN CHARGE DU VÉHICULE (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : PRÉVENTION, SÉCURITÉ D'ATELIER, RÉGLEMENTATION ET PRISE EN CHARGE DU VÉHICULE",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quel titre d'habilitation électrique le carrossier doit-il posséder pour réaliser lui-même la mise hors tension et la consignation d'un véhicule à motorisation électrique ou hybride ?",
                    "answerOptions": [
                        {"text": "BCL", "isCorrect": True},
                        {"text": "Le titre B0L autorisant uniquement des opérations non électriques d'ordre mécanique à proximité des zones dangereuses", "isCorrect": False},
                        {"text": "Le titre B1L permettant la réalisation de travaux sous tension sans démontage des carters de protection", "isCorrect": False},
                        {"text": "Le titre B2VL réservé exclusivement aux experts d'assurance lors de l'expertise contradictoire après sinistre", "isCorrect": False}
                    ],
                    "correction": "Selon la norme NF C 18-550, l'habilitation BCL désigne le chargé de consignation sur véhicules et engins à motorisation électrique ou hybride. C'est le seul titre qui autorise le carrossier à réaliser les étapes de la consignation électrique : séparation, condamnation, identification et vérification d'absence de tension (VAT). L'habilitation B0L ne permet que des travaux d'ordre non électrique hors consignation."
                },
                {
                    "questionNumber": 2,
                    "question": "Avant d'intervenir sur un élément d'ossature situé à proximité immédiate d'un module d'airbag non déclenché, quelle procédure de mise en sécurité doit impérativement être respectée ?",
                    "answerOptions": [
                        {"text": "Débrancher la batterie de servitude puis patienter le délai préconisé par le constructeur", "isCorrect": True},
                        {"text": "Verrouiller le calculateur d'airbag en retirant uniquement le fusible principal de l'habitacle", "isCorrect": False},
                        {"text": "Déconnecter directement le connecteur orange du coussin gonflable sans couper le contact général", "isCorrect": False},
                        {"text": "Court-circuiter les deux bornes de masse de l'allumeur pyrotechnique avec un fil volant isolé", "isCorrect": False}
                    ],
                    "correction": "Les circuits pyrotechniques (airbags et prétensionneurs) intègrent des condensateurs de réserve d'énergie dans le calculateur. Couper le contact et débrancher la batterie 12 V ne suffit pas immédiatement : il faut respecter un temps d'attente (généralement de 2 à 10 minutes selon les préconisations du constructeur) pour garantir la décharge complète des condensateurs et éliminer tout risque de déclenchement intempestif."
                },
                {
                    "questionNumber": 3,
                    "question": "Pourquoi le ponçage des éléments de carrosserie en aluminium nécessite-t-il un réseau d'aspiration mobile ou centralisé strictement indépendant de celui dédié à l'acier ?",
                    "answerOptions": [
                        {"text": "Les poussières d'aluminium très fines en suspension forment un mélange hautement inflammable et explosif au contact d'une étincelle générée par le ponçage de l'acier", "isCorrect": True},
                        {"text": "Le mélange de particules métalliques différentes bloque irrémédiablement les filtres à cartouche plissée en créant un amalgame pâteux qui détruit les turbines d'extraction d'air", "isCorrect": False},
                        {"text": "Les microparticules d'aluminium réagissent spontanément avec la rouille de l'acier pour libérer un gaz toxique neurotoxique inodore qui contamine l'ensemble des réseaux d'aération de l'atelier", "isCorrect": False},
                        {"text": "L'association des poussières d'acier et d'aluminium engendre une corrosion galvanique immédiate dans les conduites métalliques du réseau d'évacuation, provoquant leur perforation rapide sous l'effet de l'humidité ambiante", "isCorrect": False}
                    ],
                    "correction": "L'aluminium à l'état divisé (poussières de ponçage) présente une très forte réactivité à l'oxydation. Le mélange de poussières d'aluminium et d'acier incandescent (étincelles de meulage de l'acier) dans un même conduit peut amorcer une réaction aluminothermique violente ou une explosion de poussières (norme ATEX). Les ateliers de carrosserie doivent disposer d'aspirateurs certifiés zone 22 réservés exclusivement aux alliages légers."
                },
                {
                    "questionNumber": 4,
                    "question": "Dans une Fiche de Données de Sécurité relative à un apprêt ou un mastic polyester, à quelle rubrique normalisée l'opérateur trouve-t-il la liste des équipements de protection individuelle requis ?",
                    "answerOptions": [
                        {"text": "Rubrique 8 relative au contrôle de l'exposition et protection individuelle", "isCorrect": True},
                        {"text": "Rubrique 4 détaillant les premiers secours en cas d'ingestion accidentelle", "isCorrect": False},
                        {"text": "Rubrique 11 décrivant les informations toxicologiques aiguës et chroniques", "isCorrect": False},
                        {"text": "Rubrique 13 concernant les considérations relatives à l'élimination des déchets", "isCorrect": False}
                    ],
                    "correction": "Les FDS comportent 16 rubriques standardisées selon la réglementation européenne REACH / CLP. La rubrique 8 prescrit les valeurs limites d'exposition professionnelle (VLEP) ainsi que les équipements de protection individuelle obligatoires (type de gants, cartouches filtrantes respiratoires, lunettes étanches) pour manipuler le produit chimique en toute sécurité."
                },
                {
                    "questionNumber": 5,
                    "question": "Quel équipement de protection respiratoire est formellement exigé lors de l'application en cabine d'un apprêt ou d'un vernis polyuréthane contenant des durcisseurs à base d'isocyanates ?",
                    "answerOptions": [
                        {"text": "Un masque à adduction d'air pur comprimé assurant une surpression continue dans la pièce faciale pour isoler totalement les voies respiratoires", "isCorrect": True},
                        {"text": "Un masque jetable en papier à plis équipé d'une soupape expiratoire simple destiné uniquement à filtrer les grosses poussières grossières d'atelier", "isCorrect": False},
                        {"text": "Un demi-masque filtrant réutilisable pourvu uniquement de filtres à particules contre les poussières minérales fines sans protection contre les vapeurs", "isCorrect": False},
                        {"text": "Une cagoule ventilée autonome intégrant une cartouche filtrante universelle à charbon actif standard non certifiée pour les composés organiques volatils très concentrés et les dérivés d'isocyanates réactifs", "isCorrect": False}
                    ],
                    "correction": "Les isocyanates contenus dans les durcisseurs des peintures bicomposants polyuréthanes sont de puissants allergisants et des toxiques respiratoires majeurs pouvant provoquer un asthme professionnel irréversible. Les cartouches au charbon actif ont une durée de saturation très rapide face à ces molécules ; seul le masque à adduction d'air comprimé respirable (isolant) garantit une protection absolue en surpression dans l'environnement clos de la cabine."
                },
                {
                    "questionNumber": 6,
                    "question": "Quelle classe d'extincteur spécifique doit être obligatoirement utilisée pour éteindre un feu provoqué par des copeaux ou des limailles de métaux combustibles comme le magnésium ?",
                    "answerOptions": [
                        {"text": "Classe D", "isCorrect": True},
                        {"text": "Un extincteur au dioxyde de carbone projetant de la neige carbonique à très basse température sur le foyer", "isCorrect": False},
                        {"text": "Un extincteur à eau pulvérisée chargée d'additif émulseur créant un film étanche à l'air sur le combustible", "isCorrect": False},
                        {"text": "Un extincteur à mousse physique polyvalente projetée sous basse pression pour étouffer les flammes de surface", "isCorrect": False}
                    ],
                    "correction": "Les feux de métaux (magnésium, titane, aluminium, sodium) relèvent de la classe D. L'utilisation d'eau ou de mousse sur un feu de magnésium est strictement proscrite car elle provoque une dissociation explosive de l'eau avec libération immédiate d'hydrogène. On utilise exclusivement des poudres neutralisantes spéciales de classe D à base de chlorure de sodium ou de carbonate de sodium."
                },
                {
                    "questionNumber": 7,
                    "question": "Lors de la mise sur pont élévateur à deux colonnes d'un véhicule accidenté présentant un choc latéral important, quelle vérification préalable est indispensable avant le levage complet ?",
                    "answerOptions": [
                        {"text": "Contrôler la position des patins sur les points d'appui préconisés et effectuer un décollement pour vérifier l'équilibre", "isCorrect": True},
                        {"text": "Positionner les bras télescopiques sous le plancher central en tôle pour répartir également la charge globale", "isCorrect": False},
                        {"text": "Déposer systématiquement les quatre roues pour abaisser au maximum le centre de gravité de la caisse", "isCorrect": False},
                        {"text": "Désactiver manuellement le système de verrouillage mécanique des bras de levage pour autoriser leur libre rotation", "isCorrect": False}
                    ],
                    "correction": "Avant tout levage à hauteur de travail, le calage doit se faire précisément sous les renforts de levage homologués par le constructeur (marqués par des encoches sur feuillure ou des cales d'ancrage sous longerons). L'opérateur doit effectuer un pré-levage de quelques centimètres (décollement des roues) et exercer un mouvement d'oscillation manuelle pour contrôler la stabilité du véhicule, particulièrement critique lorsqu'une déformation structurelle a déplacé le centre de gravité."
                },
                {
                    "questionNumber": 8,
                    "question": "Quelle est la valeur juridique et technique de l'état des lieux contradictoire signé avec le client lors de l'établissement de l'ordre de réparation ?",
                    "answerOptions": [
                        {"text": "Il formalise l'accord mutuel sur l'état général initial du véhicule et protège l'atelier contre toute réclamation injustifiée portant sur des avaries antérieures non imputables au choc", "isCorrect": True},
                        {"text": "Il autorise légalement l'expert mandaté par les compagnies d'assurance à modifier unilatéralement le coût unitaire de la main-d'œuvre sans en avertir le propriétaire du véhicule endommagé", "isCorrect": False},
                        {"text": "Il transfère immédiatement et intégralement la propriété civile et pénale du véhicule sinistré à l'entreprise de carrosserie jusqu'au règlement complet de la facture de remise en état", "isCorrect": False},
                        {"text": "Il constitue un document purement interne et administratif sans aucune valeur probante devant les tribunaux judiciaires en cas de contentieux contractuel entre le réparateur et le client consommateur", "isCorrect": False}
                    ],
                    "correction": "L'Ordre de Réparation (OR) constitue le contrat d'entreprise liant le réparateur au client. L'état des lieux contradictoire (relevé des impacts hors sinistre, bris de glace préexistants, voyants allumés, niveau de carburant, objets de valeur) signé par les deux parties à la prise en charge permet de dégager la responsabilité civile de l'atelier quant aux dégâts non causés par les travaux de carrosserie."
                },
                {
                    "questionNumber": 9,
                    "question": "À partir de quel seuil de tension en courant continu un circuit de véhicule électrique ou hybride est-il classé dans le domaine des tensions dangereuses nécessitant une habilitation électrique ?",
                    "answerOptions": [
                        {"text": "Une tension supérieure à 60 volts en courant continu", "isCorrect": True},
                        {"text": "Une tension supérieure à 12 volts en courant continu", "isCorrect": False},
                        {"text": "Une tension supérieure à 24 volts en courant continu", "isCorrect": False},
                        {"text": "Une tension supérieure à 230 volts en courant continu", "isCorrect": False}
                    ],
                    "correction": "Dans le secteur automobile (normes ISO 6469, ECE R100 et NF C 18-550), la frontière de la Très Basse Tension de Sécurité (TBTS) en courant continu est fixée à 60 V DC (et 30 V AC en alternatif). Dès que la tension nominale de la chaîne de traction dépasse 60 V en continu, les conducteurs et composants relèvent de la classe de tension B, imposant le balisage d'atelier, la consignation et le port d'EPI haute tension."
                },
                {
                    "questionNumber": 10,
                    "question": "Dans le protocole de consigne électrique d'un véhicule hybride ou électrique, quelle règle s'applique impérativement lors de l'utilisation du Vérificateur d'Absence de Tension ?",
                    "answerOptions": [
                        {"text": "Tester l'appareil sur une source de tension connue immédiatement avant puis immédiatement après la mesure sur les connecteurs haute tension", "isCorrect": True},
                        {"text": "Utiliser indifféremment un multimètre numérique standard calibré en mode ohmmètre sonore entre les conducteurs actifs et la masse du véhicule", "isCorrect": False},
                        {"text": "Réaliser la mesure en portant uniquement des gants de manutention en cuir afin d'éviter les déchirures mécaniques sur les arêtes tranchantes de la tôle", "isCorrect": False},
                        {"text": "Valider l'absence de potentiel uniquement par la lecture des voyants lumineux du tableau de bord sans effectuer de contact physique direct avec les bornes du circuit de puissance", "isCorrect": False}
                    ],
                    "correction": "La Vérification d'Absence de Tension (VAT) ne peut être effectuée qu'avec un équipement spécifique normalisé (NF EN 61243-3). L'usage d'un multimètre classique est formellement interdit pour cette opération. Le protocole de sécurité impose la règle du \"trip-test\" : tester le VAT sur une source sous tension connue ou une boîte de test intégrée juste avant la mesure, vérifier la tension sur le circuit à consigner (qui doit être nulle), puis retester le VAT immédiatement après pour s'assurer qu'il ne s'est pas détérioré pendant l'opération."
                },
                {
                    "questionNumber": 11,
                    "question": "Quel document officiel et obligatoire assure la traçabilité complète des déchets dangereux d'atelier jusqu'à leur centre de traitement agréé ?",
                    "answerOptions": [
                        {"text": "Le BSDD", "isCorrect": True},
                        {"text": "L'ordre de réparation cosigné par le propriétaire du véhicule et le responsable d'atelier", "isCorrect": False},
                        {"text": "Le registre d'entrée et de sortie des pièces détachées d'occasion recyclées", "isCorrect": False},
                        {"text": "Le procès-verbal de réception des travaux émis après le contrôle de conformité final", "isCorrect": False}
                    ],
                    "correction": "Le Bordereau de Suivi des Déchets Dangereux (BSDD), aujourd'hui dématérialisé sur la plateforme nationale Trackdéchets, est une obligation légale (Code de l'environnement). Il permet de tracer l'élimination des boues de peinture, solvants usagés, mastics catalysés, filtres de cabine et batteries du lieu de production jusqu'à leur valorisation ou destruction définitive."
                },
                {
                    "questionNumber": 12,
                    "question": "Quel équipement d'atelier doit être privilégié pour prévenir les troubles musculosquelettiques lors du ponçage des bas de caisse ou du redressage des bas d'ailes ?",
                    "answerOptions": [
                        {"text": "Un pont élévateur de carrosserie ou une table de levage réglable en hauteur", "isCorrect": True},
                        {"text": "Une ceinture lombaire de maintien portée en continu durant toute la journée de travail", "isCorrect": False},
                        {"text": "Un tabouret bas d'atelier fixe sans possibilité d'ajustement morphologique", "isCorrect": False},
                        {"text": "Une cale en mousse dense posée à même le sol de la zone de préparation", "isCorrect": False}
                    ],
                    "correction": "Les TMS (affections périarticulaires et lombalgies) représentent la première cause de maladie professionnelle en carrosserie. L'ergonomie du poste impose d'adapter le travail à l'homme grâce à des tables ou ponts à levage auxiliaire permettant d'amener les zones basses du véhicule à hauteur du buste de l'opérateur, évitant ainsi le travail au sol ou en torsion prolongée du tronc."
                },
                {
                    "questionNumber": 13,
                    "question": "Lors des opérations de redressage d'éléments de carrosserie par battage au marteau et au tas, quelle disposition préventive liée au bruit doit être mise en œuvre ?",
                    "answerOptions": [
                        {"text": "Porter des protections auditives individuelles adaptées et éloigner les tiers", "isCorrect": True},
                        {"text": "Poser une feuille de feutre isolante entre le marteau et la tôle pour atténuer l'impact mécanique sans déformer le métal", "isCorrect": False},
                        {"text": "Travailler exclusivement avec des tas en plastique souple afin de limiter le niveau sonore sous le seuil d'audibilité humaine", "isCorrect": False},
                        {"text": "Installer des cloisons acoustiques mobiles tout autour du poste en maintenant une aération naturelle par l'ouverture des portes extérieures de l'atelier", "isCorrect": False}
                    ],
                    "correction": "Le martelage de la tôle d'acier ou d'aluminium génère des bruits d'impact impulsionnels dépassant fréquemment 100 dB(A). Selon le Code du travail, dès que le niveau d'exposition dépasse 80 dB(A), des protections auditives individuelles (bouchons moulés ou serre-tête antibruit) doivent être mises à disposition, et leur port devient strictement obligatoire dès 85 dB(A). L'isolement de la zone protège également les collègues travaillant aux postes voisins."
                },
                {
                    "questionNumber": 14,
                    "question": "Quelles caractéristiques constructives doivent impérativement présenter les armoires de stockage dédiées aux solvants et diluants dans le laboratoire de préparation ?",
                    "answerOptions": [
                        {"text": "Être équipées d'une résistance au feu certifiée d'un bac de rétention et d'une ventilation", "isCorrect": True},
                        {"text": "Présenter des parois transparentes en polycarbonate pour identifier visuellement les produits sans ouvrir les portes", "isCorrect": False},
                        {"text": "Être raccordées directement au réseau d'eau sous pression de l'atelier pour un noyage automatique en cas d'alerte", "isCorrect": False},
                        {"text": "Disposer d'étagères en bois massif brut afin de réduire les risques d'étincelles mécaniques lors des manipulations", "isCorrect": False}
                    ],
                    "correction": "Les produits volatils inflammables (solvants de nettoyage, diluants, durcisseurs) doivent être stockés dans des armoires de sécurité coupe-feu (norme EN 14470-1). Celles-ci comportent une rétention en partie basse pour recueillir d'éventuelles fuites, des étagères incombustibles reliées à la terre et un orifice de ventilation mécanique raccordé à l'extérieur pour évacuer les vapeurs inflammables."
                },
                {
                    "questionNumber": 15,
                    "question": "Avant de déconnecter la batterie 12 volts d'un véhicule moderne pour une intervention sur la structure, quelle précaution méthodique doit être prise ?",
                    "answerOptions": [
                        {"text": "Sauvegarder les données des calculateurs à l'aide d'un boîtier de maintien de tension ou vérifier la mise en veille des réseaux", "isCorrect": True},
                        {"text": "Mettre le contacteur d'allumage en position marche forcée pour décharger immédiatement tous les condensateurs", "isCorrect": False},
                        {"text": "Débrancher uniquement la borne positive sans toucher à la borne négative reliée à la carrosserie", "isCorrect": False},
                        {"text": "Retirer le boîtier papillon d'admission d'air pour éviter les surpressions résiduelles dans le bloc moteur", "isCorrect": False}
                    ],
                    "correction": "Sur les véhicules multiplexés, couper brutalement la batterie peut entraîner la corruption des mémoires des calculateurs (BSI, calculateurs d'airbags, systèmes multimédias). Il convient d'attendre la mise en veille complète des réseaux de bord (généralement 3 à 5 minutes après coupure du contact et fermeture des ouvrants) ou d'utiliser un outil de maintien de charge spécifique avant débranchement de la cosse négative de masse en premier."
                },
                {
                    "questionNumber": 16,
                    "question": "Quel équipement de protection individuelle spécifique aux mains est obligatoire pour manœuvrer un sectionneur haute tension ou retirer un cavalier de service sur véhicule électrifié ?",
                    "answerOptions": [
                        {"text": "Gants isolants", "isCorrect": True},
                        {"text": "Des gants de carrossier anti-coupure de niveau 5 renforcés en fibres d'aramide pour résister aux arêtes métalliques", "isCorrect": False},
                        {"text": "Des gants en nitrile épais non poudrés destinés à manipuler les résines et les dégraissants pétroliers", "isCorrect": False},
                        {"text": "Des surmoufles thermiques en croûte de cuir épais conçues exclusivement pour la manutention de pièces sorties d'étuve", "isCorrect": False}
                    ],
                    "correction": "Pour toute opération sur les composants haute tension d'un véhicule électrique (consignation, dépose du bouchon de service ou \"service plug\"), l'intervenant doit porter des gants isolants en latex ou élastomère conformes à la norme NF EN 60903, de classe 0 (tension d'utilisation jusqu'à 1000 V AC et 1500 V DC), éventuellement protégés par des surgants en cuir contre les risques d'abrasion ou de perforation mécanique."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel dispositif de protection électronique doit être branché sur le réseau de bord lors des opérations de soudage électrique par résistance ou MAG sur la carrosserie ?",
                    "answerOptions": [
                        {"text": "Un protecteur électronique anti-surtension raccordé aux bornes de la batterie", "isCorrect": True},
                        {"text": "Un fusible thermique temporisé intercalé sur le câble de masse du poste à souder", "isCorrect": False},
                        {"text": "Une résistance de décharge inductive connectée en série sur l'alternateur", "isCorrect": False},
                        {"text": "Un disjoncteur différentiel haute sensibilité clipsé sur le montant central de pavillon", "isCorrect": False}
                    ],
                    "correction": "Le soudage à l'arc ou par résistance génère de très fortes pointes de tension induites et des courants de fuite à travers la structure métallique du véhicule. La mise en place d'un protecteur de surtension (filtre antiparasite) branché directement sur les cosses de la batterie 12 V absorbe ces transitoires de commutation et protecte les composants électroniques sensibles des calculateurs embarqués."
                },
                {
                    "questionNumber": 18,
                    "question": "Lors de la dépose complète d'un coussin gonflable de volant pour accéder à la colonne de direction, quelle règle de sécurité régit la manipulation et la pose du composant sur l'établi ?",
                    "answerOptions": [
                        {"text": "Poser le module sur un établi stable en orientant impérativement la face de déploiement garnie vers le haut", "isCorrect": True},
                        {"text": "Empiler les modules les uns sur les autres dans un carton fermé situé à proximité immédiate d'une source de chaleur", "isCorrect": False},
                        {"text": "Retourner le module avec la face métallique du générateur de gaz orientée vers le haut pour limiter l'accumulation de poussières", "isCorrect": False},
                        {"text": "Placer le composant dans un bac métallique non ventilé sans fixation en reliant les broches de connexion électrique à une pile de test pour vérifier la continuité interne", "isCorrect": False}
                    ],
                    "correction": "Un module d'airbag déposé doit toujours être posé avec la face rembourrée (sac et cache plastique) orientée vers le haut et la carcasse métallique du générateur de gaz appuyée contre le plan de travail. En cas d'allumage pyrotechnique accidentel (décharge électrostatique), le sac se gonflera librement vers le haut sans propulser le module métallique comme un projectile à travers l'atelier."
                },
                {
                    "questionNumber": 19,
                    "question": "Lors de la prise en charge d'un véhicule et de l'établissement du devis, quelle obligation réglementaire incombe au réparateur carrossier concernant les pièces de rechange ?",
                    "answerOptions": [
                        {"text": "Proposer au client une alternative avec des pièces issues de l'économie circulaire pour certaines catégories de pièces", "isCorrect": True},
                        {"text": "Imposer d'office des pièces neuves d'origine constructeur même si le propriétaire demande des pièces d'occasion", "isCorrect": False},
                        {"text": "Remplacer systématiquement tous les éléments amovibles rayés par des pièces adaptables non certifiées", "isCorrect": False},
                        {"text": "Refuser l'intervention si la valeur des réparations estimées dépasse la moitié de la valeur marchande du véhicule", "isCorrect": False}
                    ],
                    "correction": "Depuis le 1er janvier 2017 (décret d'application du Code de la consommation), les professionnels de la réparation automobile ont l'obligation légale de proposer aux consommateurs des pièces issues de l'économie circulaire (PIEC), notamment pour les pièces de carrosserie amovibles (portes, ailes, capots, hayons) et le vitrage non collé, afin de favoriser le réemploi et d'abaisser les coûts de remise en état."
                },
                {
                    "questionNumber": 20,
                    "question": "Quel risque sanitaire majeur et spécifique présente le découpage ou le meulage d'éléments de carrosserie modernes en composite à base de résine et fibre de carbone ?",
                    "answerOptions": [
                        {"text": "L'inhalation de microfibres respirables conductrices pouvant provoquer des irritations pulmonaires et des courts-circuits électriques", "isCorrect": True},
                        {"text": "La génération instantanée de vapeurs d'acide sulfurique concentré au niveau du point de friction du disque abrasif", "isCorrect": False},
                        {"text": "L'émission de rayonnements ionisants gamma susceptibles de contaminer durablement les parois de l'atelier de carrosserie", "isCorrect": False},
                        {"text": "Le dégagement massif de monoxyde de carbone explosif par calcination immédiate des fibres minérales stabilisées", "isCorrect": False}
                    ],
                    "correction": "L'usinage et la coupe du composite carbone libèrent des microfibres aciculaires très légères qui pénètrent profondément dans l'arbre bronchique, provoquant des lésions mécaniques et des inflammations pulmonaires. De plus, les poussières de carbone étant hautement conductrices d'électricité, leur infiltration dans les moteurs des outils électroportatifs ou les coffrets électriques de l'atelier provoque des arcs et des pannes de court-circuit."
                }
            ]
        },
        # =========================================================================
        # THÈME 2 : MÉTALLURGIE, SCIENCES DES MATÉRIAUX ET PROCÉDÉS D'ASSEMBLAGE STRUCTURAL (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : MÉTALLURGIE, SCIENCES DES MATÉRIAUX ET PROCÉDÉS D'ASSEMBLAGE STRUCTURAL",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel type d'acier utilisé dans les renforts de pied milieu perd définitivement ses propriétés mécaniques s'il subit une chauffe de redressage ?",
                    "answerOptions": [
                        {"text": "L'acier au bore", "isCorrect": True},
                        {"text": "L'acier doux à bas carbone embouti à froid qui voit sa dureté superficielle augmenter sous l'action d'une flamme douce", "isCorrect": False},
                        {"text": "L'alliage d'aluminium de la série cinq mille dont la structure cristalline se stabilise au-delà de trois cents degrés", "isCorrect": False},
                        {"text": "La tôle électrozinguée à haute limite élastique dont la couche protectrice se régénère automatiquement par recuit", "isCorrect": False}
                    ],
                    "correction": "Les aciers à très haute et ultra haute limite élastique (THLE / UHLE), et particulièrement les aciers au bore (usibor), tirent leur résistance exceptionnelle (jusqu'à 1500 MPa) d'un traitement thermique de trempe sous presse lors de l'emboutissage. Toute chauffe d'atelier au chalumeau ou à l'électrode carbone détruit irrémédiablement leur microstructure martensitique, transformant la zone chauffée en acier mou incapable d'assurer la protection de la cellule de survie en cas de choc."
                },
                {
                    "questionNumber": 22,
                    "question": "Pourquoi le soudo-brasage MIG est-il privilégié par les constructeurs pour l'assemblage des tôles zinguées de carrosserie ?",
                    "answerOptions": [
                        {"text": "La température de fusion du métal d'apport préserve la couche protectrice de zinc sans vaporisation destructive", "isCorrect": True},
                        {"text": "Le métal d'apport traverse l'acier par capillarité et augmente l'épaisseur totale de la feuillure soudée", "isCorrect": False},
                        {"text": "L'absence de courant électrique durant la fusion élimine complètement les déformations thermiques de l'élément", "isCorrect": False},
                        {"text": "Le fil d'apport enrobé forme un laitier protecteur étanche qui dispense de toute application ultérieure d'apprêt", "isCorrect": False}
                    ],
                    "correction": "Le zinc se vaporise dès 906 °C, alors que l'acier fond autour de 1500 °C. En soudage MAG traditionnel, le zinc brûle largement autour du cordon, créant des fumées toxiques, des porosités et supprimant la protection anticorrosion. Le soudo-brasage MIG utilise un fil d'alliage cuivre-silicium (CuSi3) ou cuivre-aluminium (CuAl8) dont le point de fusion se situe vers 980-1020 °C : le métal de base n'entre pas en fusion, le zinc n'est que superficiellement altéré et l'effet sacrificiel de galvanisation reste intact."
                },
                {
                    "questionNumber": 23,
                    "question": "Quel gaz de protection actif est standardisé pour le soudage MAG des aciers de structure en carrosserie ?",
                    "answerOptions": [
                        {"text": "Un mélange ternaire ou binaire à base d'argon contenant une proportion contrôlée de dioxyde de carbone", "isCorrect": True},
                        {"text": "Un mélange d'argon pur enrichi d'une forte concentration d'azote pour neutraliser les projections d'étincelles", "isCorrect": False},
                        {"text": "Un flux continu d'hélium pur sous haute pression destiné à refroidir instantanément le bain de fusion", "isCorrect": False},
                        {"text": "Un gaz réducteur composé uniquement de monoxyde de carbone afin d'éliminer totalement l'oxydation de l'acier", "isCorrect": False}
                    ],
                    "correction": "Le procédé MAG (Metal Active Gas, procédé 135) requiert un gaz chimiquement actif pour stabiliser l'arc et assurer la pénétration. On utilise des mélanges normalisés (famille M21 selon la norme ISO 14175) comprenant environ 80 à 82 % d'argon et 18 à 20 % de CO2 (ou des mélanges ternaires argon / CO2 / O2). L'argon pur est un gaz inerte strictement réservé au procédé MIG (aluminium) ou TIG."
                },
                {
                    "questionNumber": 24,
                    "question": "Lors du remplacement d'un bas de caisse par la méthode du rivetage-collage, quel est le rôle principal de la résine époxy structurale ?",
                    "answerOptions": [
                        {"text": "Transmettre uniformément les contraintes mécaniques sur toute la surface de contact tout en assurant l'étanchéité et l'isolation galvanique", "isCorrect": True},
                        {"text": "Remplacer temporairement les fixations mécaniques le temps que la réaction chimique assure la fusion moléculaire complète des tôles d'acier en contact intime", "isCorrect": False},
                        {"text": "Augmenter l'épaisseur de la feuillure afin de compenser les écarts d'affleurement tout en créant une liaison électrique hautement conductrice entre les deux éléments métalliques assemblés", "isCorrect": False},
                        {"text": "Servir exclusivement de garniture d'insonorisation acoustique contre les bruits de roulement sans participer à la rigidité torsionnelle ni à la transmission des efforts de traction entre les composants", "isCorrect": False}
                    ],
                    "correction": "Le collage structural (résines époxydes ou polyuréthanes bi-composants) répartit les contraintes de cisaillement et de pelage sur l'intégralité de la zone assemblée, éliminant les concentrations de contraintes inhérentes aux points de soudure. De plus, il forme un joint barrière continu étanche aux infiltrations et isole électriquement les métaux différents (évitant le couple galvanique acier-aluminium). Les rivets assurent quant à eux le maintien sous pression pendant la polymérisation et la résistance au pelage dynamique."
                },
                {
                    "questionNumber": 25,
                    "question": "Quel phénomène métallurgique se produit dans la zone affectée thermiquement lors d'un apport de chaleur excessif sur un acier HLE ?",
                    "answerOptions": [
                        {"text": "Un grossissement du grain cristallin provoquant une chute importante des caractéristiques mécaniques", "isCorrect": True},
                        {"text": "Une recristallisation instantanée créant une dureté extrême équivalente à celle d'un acier trempé", "isCorrect": False},
                        {"text": "Une augmentation de la ductilité du métal accompagnée d'un renforcement de la résistance à la fatigue", "isCorrect": False},
                        {"text": "Une diffusion d'oxygène créant une couche superficielle totalement insensible à la corrosion atmosphérique", "isCorrect": False}
                    ],
                    "correction": "La Zone Affectée Thermiquement (ZAT) désigne le métal de base situé en bordure du cordon qui n'a pas fondu mais a subi un cycle thermique sévère. Un apport d'énergie trop élevé (vitesse d'avance trop lente, intensité excessive) provoque un phénomène de surchauffe avec grossissement des grains d'austénite/ferrite. Cette altération de la microstructure affaiblit la limite élastique et rend la zone cassante face aux sollicitations de choc."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel moyen de contrôle non destructif permet de vérifier l'absence d'interstice d'air et la continuité d'un cordon de colle structurale sur une feuillure assemblée ?",
                    "answerOptions": [
                        {"text": "Les ultrasons", "isCorrect": True},
                        {"text": "L'essai d'arrachement au bédane tranchant réalisé sur les extrémités de la pièce après polymérisation complète", "isCorrect": False},
                        {"text": "Le test de traction mécanique axiale opéré avec un vérin d'ancrage étalonné jusqu'à rupture de la tôle", "isCorrect": False},
                        {"text": "La radiographie par rayons gamma nécessitant l'évacuation intégrale de l'ensemble de l'atelier de carrosserie", "isCorrect": False}
                    ],
                    "correction": "Le contrôle non destructif des assemblages collés en atelier ou en usine fait appel au contrôle par écho d'ondes ultrasonores (ou thermographie infrarouge active). Les ondes traversent les tôles et la colle ; la présence d'une bulle d'air, d'un manque de matière ou d'un délaminage modifie le temps de retour et l'amplitude de l'onde réfléchie sans détruire la pièce. L'essai au bédane est un essai destructif."
                },
                {
                    "questionNumber": 27,
                    "question": "Dans le procédé de soudage par résistance par points, quel paramètre contrôle directement le diamètre du noyau de soudure ?",
                    "answerOptions": [
                        {"text": "L'intensité du courant électrique de soudage exprimée en ampères", "isCorrect": True},
                        {"text": "La dureté de l'acier des pointes d'électrodes en cuivre pur", "isCorrect": False},
                        {"text": "La pression atmosphérique régnant à l'intérieur de l'atelier", "isCorrect": False},
                        {"text": "La tension superficielle du liquide de refroidissement des pinces", "isCorrect": False}
                    ],
                    "correction": "La loi de Joule ($Q = R \\times I^2 \\times t$) régit le soudage électrique par résistance (SER). L'énergie thermique dépend au carré de l'intensité du courant (I). C'est principalement l'intensité électrique (comprise généralement entre 8 000 et 14 000 A en carrosserie moderne) et le temps de passage du courant qui déterminent le volume de matière en fusion, et donc le diamètre du noyau lenticulaire garantissant la tenue mécanique."
                },
                {
                    "questionNumber": 28,
                    "question": "Pourquoi les constructeurs interdisent-ils formellement le soudage bout à bout au MAG sur un pied milieu en acier usibor à très haute résistance ?",
                    "answerOptions": [
                        {"text": "L'élévation de température détruit la structure martensitique de l'acier et crée une zone de rupture brutale sans déformation plastique préalable", "isCorrect": True},
                        {"text": "La tension superficielle du métal liquide repousse le fil d'apport en formant un empilement poreux incapable de supporter la moindre contrainte mécanique", "isCorrect": False},
                        {"text": "Le cordon de soudure provoque un dégagement massif de vapeurs de zinc qui neutralise instantanément le blindage électromagnétique des calculateurs d'aide à la conduite situés à proximité", "isCorrect": False},
                        {"text": "L'apport calorifique provoque une transformation microstructurale irréversible entraînant la décarburation totale de l'alliage avec fissuration sous cordon et effondrement critique de la résistance à l'écrasement en cas de choc latéral violent", "isCorrect": False}
                    ],
                    "correction": "Les aciers à très haute résistance (aciers au bore 22MnB5) sont trempés à chaud pour atteindre des résistances à la traction supérieures à 1400-1500 MPa. Le soudage à l'arc (MAG) induit des températures locales très supérieures à 1000 °C suivies d'un refroidissement incontrôlé. Il se crée alors une zone adoucie ou au contraire hyper-fragilisée, provoquant une cassure nette en cas de collision latérale. Les réparations sur ces éléments imposent le remplacement complet ou des greffes spécifiques par manchonnage riveté/collé strictement homologuées."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle composition de fil d'apport est la plus couramment employée pour le soudo-brasage des éléments d'ossature galvanisés ?",
                    "answerOptions": [
                        {"text": "Un alliage de cuivre et de silicium nommé CuSi3", "isCorrect": True},
                        {"text": "Un fil d'acier doux cuivré à faible teneur en carbone", "isCorrect": False},
                        {"text": "Un fil d'aluminium pur allié à du manganèse résistant", "isCorrect": False},
                        {"text": "Une baguette de laiton décapée enrobée de flux boraté", "isCorrect": False}
                    ],
                    "correction": "Le fil d'apport CuSi3 (environ 96 à 97 % de cuivre et 3 % de silicium) est le standard absolu de soudo-brasage MIG homologué par les constructeurs automobiles. Le silicium agit comme désoxydant et améliore la mouillabilité du bain liquide sur l'acier. On utilise également parfois le CuAl8 (cuivre-aluminium) sur certains revêtements particuliers."
                },
                {
                    "questionNumber": 30,
                    "question": "Quel est l'objectif du contrôle destructif par déboutonnage sur une éprouvette soudée par résistance par points ?",
                    "answerOptions": [
                        {"text": "Mesurer le diamètre réel du noyau de soudure resté arraché sur l'une des tôles", "isCorrect": True},
                        {"text": "Vérifier la conductivité électrique résiduelle entre les deux tôles après fusion", "isCorrect": False},
                        {"text": "Évaluer la résistance à la corrosion par brouillard salin au centre du point", "isCorrect": False},
                        {"text": "Contrôler la profondeur de l'empreinte laissée par les porte-électrodes sur l'acier", "isCorrect": False}
                    ],
                    "correction": "Avant toute campagne de pointage sur caisse, le carrossier réalise des éprouvettes dans les mêmes nuances et épaisseurs de tôles. L'essai de déboutonnage au bédane ou par torsion consiste à séparer mécaniquement les tôles jusqu'à rupture. Un point conforme doit obligatoirement s'arracher en prélevant une pastille de métal (déboutonnage avec trou sur une tôle et noyau intact sur l'autre), et le diamètre de ce noyau doit être mesuré au pied à coulisse selon la formule constructeur ($d \\approx 4 \\times \\sqrt{t}$ où $t$ est l'épaisseur minimale)."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel type de rivet nécessite l'utilisation d'une matrice profilée pour créer un sertissage mécanique étanche sans perçage préalable des tôles ?",
                    "answerOptions": [
                        {"text": "Auto-poinçonneur", "isCorrect": True},
                        {"text": "Le rivet aveugle à rupture de tige expansé par traction mécanique dans un alésage préexistant", "isCorrect": False},
                        {"text": "Le rivet tubulaire fileté posé à la pince oléopneumatique pour créer un ancrage taraudé démontable", "isCorrect": False},
                        {"text": "Le rivet plein en aluminium refoulé à chaud à l'aide d'une bouterolle pneumatique de forte puissance", "isCorrect": False}
                    ],
                    "correction": "Le rivetage auto-poinçonneur (SPR pour Self-Piercing Riveting) utilise un rivet semi-tubulaire en acier haute résistance poussé par un vérin hydraulique. Le rivet perfore la tôle supérieure, traverse la tôle intermédiaire éventuelle et s'épanouit dans la tôle inférieure sans déboucher, grâce à l'empreinte spécifique de la matrice de réaction. Ce procédé permet d'assembler des matériaux dissemblables (aluminium/acier) sans trou pilote préalable."
                },
                {
                    "questionNumber": 32,
                    "question": "Quelle précaution thermique doit être observée lors de l'assemblage de deux pièces en tôle d'acier par collage structural ?",
                    "answerOptions": [
                        {"text": "Respecter le temps ouvert de la colle et respecter la température minimale prescrite pour garantir une polymérisation complète de la matrice polymère", "isCorrect": True},
                        {"text": "Chauffer les feuillures au chalumeau oxyacétylénique jusqu'au rouge cerise pour favoriser une pénétration immédiate de la résine au cœur de l'acier", "isCorrect": False},
                        {"text": "Appliquer un choc thermique cryogénique avec de l'azote liquide pour figer instantanément la colle et éviter son fluage lors de la manipulation", "isCorrect": False},
                        {"text": "Maintenir une étuve continue à deux cent cinquante degrés pendant plusieurs heures afin de calciner les agents de réticulation et créer une liaison céramique rigide indémontable même sous des contraintes dynamiques intenses", "isCorrect": False}
                    ],
                    "correction": "Les colles époxydes ou polyuréthanes bicomposants dépendent d'une réaction chimique de réticulation sensible à la température ambiante (idéalement 18 à 25 °C). En dessous de 15 °C, la polymérisation ralentit fortement ou s'arrête. De plus, le \"temps ouvert\" (délai maximal entre le début de l'extrusion et l'accostage définitif des tôles avec maintien sous presse) doit être scrupuleusement respecté sous peine d'obtenir un joint sec non adhésif."
                },
                {
                    "questionNumber": 33,
                    "question": "Pour le soudage MAG de tôles minces d'acier en carrosserie, quel mode de transfert de métal dans l'arc électrique est préconisé ?",
                    "answerOptions": [
                        {"text": "Le transfert par court-circuit limitant l'apport calorifique et le risque de perforation", "isCorrect": True},
                        {"text": "Le transfert par pulvérisation axiale générant un bain de fusion large et très profond", "isCorrect": False},
                        {"text": "Le transfert par grosses gouttes instables provoquant de fortes projections métalliques", "isCorrect": False},
                        {"text": "Le transfert en arc tournant réservé uniquement aux fortes épaisseurs de longerons", "isCorrect": False}
                    ],
                    "correction": "Sur tôles minces de carrosserie (épaisseurs de 0,6 à 1,5 mm), le mode de transfert par court-circuit (short-arc) est incontournable. Il fonctionne à des tensions (15 à 20 V) et des intensités basses (50 à 140 A). Le fil entre en contact avec le bain plusieurs dizaines de fois par seconde, provoquant un court-circuit qui détache la goutte sans surchauffer le métal de base, évitant ainsi le perçage de la tôle et minimisant la déformation thermique."
                },
                {
                    "questionNumber": 34,
                    "question": "Quel est le risque majeur d'un contact direct non isolé entre un élément en aluminium et un renfort en acier ?",
                    "answerOptions": [
                        {"text": "L'apparition d'une corrosion bimétallique accélérée détruisant rapidement l'aluminium", "isCorrect": True},
                        {"text": "Une surchauffe par effet Joule provoquant la fusion spontanée de la tôle d'acier", "isCorrect": False},
                        {"text": "Une perte totale de la rigidité mécanique de l'assemblage sous l'effet des vibrations", "isCorrect": False},
                        {"text": "La formation d'un dépôt de calamine isolante empêchant toute mise à la masse électrique", "isCorrect": False}
                    ],
                    "correction": "Dans l'échelle des potentiels électrochimiques, l'aluminium est beaucoup plus anodique (moins noble) que l'acier. En présence d'un électrolyte (eau, humidité saline), un couple galvanique se crée : l'aluminium devient l'anode sacrificielle et se corrode de manière fulgurante et perforante. Lors de l'assemblage acier-aluminium, une isolation diélectrique complète est obligatoire : colle isolante, mastic barrière et rivets revêtus d'un traitement spécial."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle fonction assure le cycle de pré-pression des électrodes avant le passage du courant dans une soudeuse par résistance moderne ?",
                    "answerOptions": [
                        {"text": "Écraser les oxydes de surface et assurer un contact intime entre les tôles pour stabiliser la résistance de contact électrique", "isCorrect": True},
                        {"text": "Mesurer la conductivité thermique du métal pour ajuster automatiquement le débit de fluide frigorifique traversant le transformateur", "isCorrect": False},
                        {"text": "Réaliser un matriçage à froid de la feuillure afin d'éviter tout recours ultérieur à des vis autoforeuses de maintien temporaire", "isCorrect": False},
                        {"text": "Nettoyer mécaniquement les impuretés superficielles par frottement rotatif des pointes en cuivre tout en créant un préchauffage par friction dynamique indispensable à l'amorçage de l'arc interne entre les pièces métalliques superposées", "isCorrect": False}
                    ],
                    "correction": "Le cycle de soudage par points débute par la phase d'accostage et de pré-pression (temps de compression). L'effort pneumatique ou électrique exercé par la pince plaque fermement les tôles l'une contre l'autre. Cette action mécanique aplanit les rugosités, chasse les éventuels résidus d'air et stabilise la résistance de contact électrique entre les pièces avant que le courant de forte intensité ne soit injecté, évitant ainsi une explosion ou des crépitements de métal liquide (expulsions)."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel gaz inerte de protection doit obligatoirement être utilisé pour le soudage MIG des alliages d'aluminium de carrosserie ?",
                    "answerOptions": [
                        {"text": "L'argon pur", "isCorrect": True},
                        {"text": "L'air comprimé déshuilé et filtré pour éviter la pollution particulaire du bain de fusion", "isCorrect": False},
                        {"text": "Le dioxyde de carbone pur favorisant une pénétration maximale dans les fortes épaisseurs", "isCorrect": False},
                        {"text": "L'azote déshydraté sous pression pour empêcher la formation d'oxydes d'alumine à haute température", "isCorrect": False}
                    ],
                    "correction": "Le soudage de l'aluminium et de ses alliages relève du procédé MIG (Metal Inert Gas, procédé 131). L'aluminium a une très forte affinité pour l'oxygène et forme spontanément une couche d'alumine (Al2O3) réfractaire fondant à plus de 2050 °C. Le gaz de protection doit impérativement être un gaz neutre/inerte, typiquement de l'argon pur (qualité I1) ou un mélange argon-hélium, sans aucune trace de CO2 ni d'oxygène qui détruiraient le bain de fusion."
                },
                {
                    "questionNumber": 37,
                    "question": "Comment s'effectue le meulage ou l'affleurage d'un cordon de soudure sur un élément d'ossature sans affaiblir la pièce réparée ?",
                    "answerOptions": [
                        {"text": "En utilisant un disque abrasif souple à grain fin sans creuser le métal de base adjacent", "isCorrect": True},
                        {"text": "En insistant avec une meule à tronçonner rigide pour araser le cordon sous le niveau de la tôle", "isCorrect": False},
                        {"text": "En chauffant préalablement la soudure au chalumeau pour rendre le métal tendre avant limage", "isCorrect": False},
                        {"text": "En décapant chimiquement le cordon avec un acide concentré pour dissoudre la surépaisseur", "isCorrect": False}
                    ],
                    "correction": "L'affleurage d'une soudure structurelle doit impérativement conserver l'épaisseur nominale de la pièce d'origine. L'usage d'un disque rigide à ébarber est proscrit car il crée des entailles et des sillons (amorces de rupture) dans le métal adjacent. On utilise des disques abrasifs plats lamellaires ou des disques semi-flexibles montés sur meuleuse pneumatique avec un angle d'attaque faible, complétés par une lime carrossier pour finir à ras sans amincir la tôle."
                },
                {
                    "questionNumber": 38,
                    "question": "Pourquoi les pinces des postes de soudage par points actuels intègrent-elles un asservissement informatisé de l'effort de serrage ?",
                    "answerOptions": [
                        {"text": "Garantir une pression constante adaptée à l'épaisseur des tôles pour éviter l'expulsion de métal en fusion lors de l'impulsion électrique", "isCorrect": True},
                        {"text": "Corriger automatiquement l'alignement géométrique de la caisse en exerçant une traction latérale permanente sur la feuillure", "isCorrect": False},
                        {"text": "Permettre la découpe nette des bords de tôle excédentaires grâce à une force de cisaillement hydraulique calibrée", "isCorrect": False},
                        {"text": "Compenser les pertes de charge hydrauliques du circuit d'atelier tout en modifiant la composition chimique de l'acier par densification moléculaire sous une pression de plusieurs tonnes appliquée avant chaque impulsion de soudage", "isCorrect": False}
                    ],
                    "correction": "Les soudeuses SER intelligentes (technologie Inverter moyenne fréquence) intègrent des capteurs d'effort et de déplacement sur les mors de pince (détection d'épaisseur automatique). Une force de serrage insuffisante face à un empilement de tôles THLE/UHLE entraîne une résistance de contact trop élevée au départ, provoquant une vaporisation instantanée du métal et des projections incandescentes (expulsions), ce qui vide le noyau de son métal et détruit sa résistance mécanique."
                },
                {
                    "questionNumber": 39,
                    "question": "Lors de l'utilisation d'une colle structurale bicomposant en cartouche, quelle précaution initiale est indispensable avant la pose de la buse mélangeuse ?",
                    "answerOptions": [
                        {"text": "Extruder une petite quantité de produit pour vérifier que les deux composants sortent simultanément", "isCorrect": True},
                        {"text": "Chauffer la cartouche à haute température pour fluidifier complètement les composants chimiques", "isCorrect": False},
                        {"text": "Agiter vigoureusement la cartouche manuellement pendant dix minutes pour homogénéiser la pâte", "isCorrect": False},
                        {"text": "Diluer le composant durcisseur avec un solvant nettoyant pour ralentir le temps de prise", "isCorrect": False}
                    ],
                    "correction": "Dans une cartouche bicomposant (résine et durcisseur côte à côte), les deux pistons peuvent présenter un léger décalage au démarrage de la poussée du pistolet. Il est obligatoire de purger quelques centimètres de pâte sans buse pour s'assurer que les deux orifices débitent en même temps et de manière homogène. Sans cette étape, le début du cordon injecté dans la buse mélangeuse présente un ratio incorrect et ne polymérisera jamais."
                },
                {
                    "questionNumber": 40,
                    "question": "Quel est le rôle principal du cuivre utilisé dans les pointes d'électrodes de soudage par résistance ?",
                    "answerOptions": [
                        {"text": "Offrir une excellente conductivité électrique et thermique afin d'amener le courant sans chauffer et de dissiper la chaleur en surface", "isCorrect": True},
                        {"text": "Déposer par frottement une couche galvanique protectrice qui empêche la rouille de s'installer au point d'impact des mors", "isCorrect": False},
                        {"text": "Fondre superficiellement à chaque point pour servir de métal d'apport et sceller la liaison entre les électrodes et les tôles", "isCorrect": False},
                        {"text": "Créer une barrière magnétique supraconductrice évitant la formation de courants de Foucault dans les bras de la pince tout en augmentant artificiellement la résistance ohmique superficielle de la tôle pour amorcer un arc électrique sous vide", "isCorrect": False}
                    ],
                    "correction": "Les électrodes de pointage sont usinées dans des alliages de cuivre réfractaires (cuivre-chrome-zirconium ou cuivre-béryllium). Leur conductivité électrique doit être très supérieure à celle de l'acier pour acheminer les milliers d'ampères sans échauffement interne excessif. De plus, leur conductivité thermique élevée permet de dissiper immédiatement la chaleur aux surfaces extérieures des tôles (refroidies en interne par circulation d'eau), confinant la fusion au seul plan de joint central."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : AMOVIBLES, SELLERIE, VITRAGE ET SYSTÈMES D'AIDE À LA CONDUITE (ADAS) (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : AMOVIBLES, SELLERIE, VITRAGE ET SYSTÈMES D'AIDE À LA CONDUITE (ADAS)",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel outil spécifique coupe le joint en polyuréthane lors du remplacement d'un pare-brise ?",
                    "answerOptions": [
                        {"text": "Corde à piano", "isCorrect": True},
                        {"text": "Scie sauteuse", "isCorrect": False},
                        {"text": "Pince coupante", "isCorrect": False},
                        {"text": "Cutter rotatif", "isCorrect": False}
                    ],
                    "correction": "La corde à piano (ou fil de découpe) s'insère à travers le joint de colle et permet sa découpe par mouvement de va-et-vient."
                },
                {
                    "questionNumber": 42,
                    "question": "Quel système protège le conducteur en se gonflant lors d'un choc ?",
                    "answerOptions": [
                        {"text": "Airbag", "isCorrect": True},
                        {"text": "Prétensionneur", "isCorrect": False},
                        {"text": "Ceinture active", "isCorrect": False},
                        {"text": "Appuie-tête", "isCorrect": False}
                    ],
                    "correction": "Le sac gonflable (airbag) se déploie en quelques millisecondes pour amortir la projection du corps vers l'avant."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel réglage contrôle l'alignement visuel entre une aile et une portière ?",
                    "answerOptions": [
                        {"text": "Affleurement", "isCorrect": True},
                        {"text": "Parallélisme", "isCorrect": False},
                        {"text": "Carrossage", "isCorrect": False},
                        {"text": "Dévers", "isCorrect": False}
                    ],
                    "correction": "L'affleurement assure la continuité de la surface de carrosserie entre deux panneaux adjacents."
                },
                {
                    "questionNumber": 44,
                    "question": "Comment nomme-t-on le mécanisme qui permet la montée et descente d'une vitre ?",
                    "answerOptions": [
                        {"text": "Lève-vitre", "isCorrect": True},
                        {"text": "Moteur pas-à-pas", "isCorrect": False},
                        {"text": "Actionneur linéaire", "isCorrect": False},
                        {"text": "Compas hydraulique", "isCorrect": False}
                    ],
                    "correction": "Le lève-vitre est un système mécanique à compas ou à câble entraîné manuellement ou électriquement."
                },
                {
                    "questionNumber": 45,
                    "question": "Que permet de compenser l'utilisation de cales d'épaisseur sur les charnières d'une portière ?",
                    "answerOptions": [
                        {"text": "Ajuster le jeu longitudinal ou transversal de l'ouvrant par rapport à la caisse", "isCorrect": True},
                        {"text": "Renforcer la rigidité structurelle de la porte lors d'un choc latéral", "isCorrect": False},
                        {"text": "Éviter le grippage de l'axe de rotation en insérant un matériau autolubrifiant", "isCorrect": False},
                        {"text": "Modifier la tension du ressort d'assistance d'ouverture de la portière", "isCorrect": False}
                    ],
                    "correction": "Les cales permettent d'éloigner ou de rapprocher la charnière du pied milieu ou du pied avant pour affiner les jeux."
                },
                {
                    "questionNumber": 46,
                    "question": "Quelle est la fonction du primaire d'adhérence appliqué sur la baie de pare-brise avant collage ?",
                    "answerOptions": [
                        {"text": "Favoriser l'accroche chimique de la colle polyuréthane et bloquer les rayons ultraviolets", "isCorrect": True},
                        {"text": "Nettoyer la surface des résidus de graisse et dissoudre l'ancienne colle restante", "isCorrect": False},
                        {"text": "Accélérer le temps de séchage de la peinture environnante pour éviter les coulures", "isCorrect": False},
                        {"text": "Créer un pont thermique empêchant la formation de condensation sur le vitrage", "isCorrect": False}
                    ],
                    "correction": "Le primaire contient des solvants volatils, il prépare la surface à l'accroche de la colle et opacifie le verre pour stopper les UV destructeurs."
                },
                {
                    "questionNumber": 47,
                    "question": "Pourquoi faut-il respecter scrupuleusement le temps de libération du véhicule après la pose d'un pare-brise ?",
                    "answerOptions": [
                        {"text": "Pour garantir que la colle a atteint sa résistance mécanique optimale en cas de choc", "isCorrect": True},
                        {"text": "Pour permettre aux capteurs d'aide à la conduite de s'auto-calibrer en position statique", "isCorrect": False},
                        {"text": "Pour éviter que les vapeurs de solvants ne déclenchent l'alarme volumétrique de l'habitacle", "isCorrect": False},
                        {"text": "Pour s'assurer que le joint d'étanchéité extérieur est complètement durci et ponçable", "isCorrect": False}
                    ],
                    "correction": "Le pare-brise collé participe à la rigidité de la caisse et sert d'appui à l'airbag passager, le temps de polymérisation est donc vital pour la sécurité."
                },
                {
                    "questionNumber": 48,
                    "question": "Que doit-on faire avant de débrancher un module d'airbag ?",
                    "answerOptions": [
                        {"text": "Consigner le véhicule en débranchant la batterie et attendre le temps de décharge des condensateurs", "isCorrect": True},
                        {"text": "Effectuer une lecture des défauts avec l'outil de diagnostic pour effacer la mémoire de l'accident", "isCorrect": False},
                        {"text": "Couper les fils du faisceau avec une pince isolée puis les raccorder avec des dominos", "isCorrect": False},
                        {"text": "Frapper légèrement sur le boîtier avec un maillet en caoutchouc pour vérifier son inertie", "isCorrect": False}
                    ],
                    "correction": "La décharge des condensateurs du calculateur est impérative pour éviter tout déclenchement pyrotechnique inopiné lors de la déconnexion."
                },
                {
                    "questionNumber": 49,
                    "question": "Comment fonctionne un prétensionneur pyrotechnique de ceinture de sécurité ?",
                    "answerOptions": [
                        {"text": "Il tend la sangle par l'explosion d'une petite charge pour plaquer l'occupant contre son siège", "isCorrect": True},
                        {"text": "Il bloque mécaniquement le dérouleur grâce à une masselotte centrifuge sensible à l'inclinaison", "isCorrect": False},
                        {"text": "Il enroule la ceinture lentement grâce à un moteur électrique alimenté par la batterie de servitude", "isCorrect": False},
                        {"text": "Il relâche la tension de la sangle quelques millisecondes après le choc pour limiter les lésions", "isCorrect": False}
                    ],
                    "correction": "Lors d'un choc sévère, l'inflammation du générateur de gaz actionne un piston qui ravale la ceinture pour supprimer son jeu naturel."
                },
                {
                    "questionNumber": 50,
                    "question": "Quel est le rôle d'un système ADAS de type caméra multifonction placé derrière le pare-brise ?",
                    "answerOptions": [
                        {"text": "Détecter le franchissement de ligne, lire les panneaux et gérer le freinage d'urgence", "isCorrect": True},
                        {"text": "Filmer l'habitacle pour ajuster la position des sièges en fonction du profil du conducteur", "isCorrect": False},
                        {"text": "Mesurer l'épaisseur du film d'eau sur la route pour adapter la pression des pneumatiques", "isCorrect": False},
                        {"text": "Projeter les informations de vitesse directement sur la rétine du conducteur", "isCorrect": False}
                    ],
                    "correction": "Les caméras ADAS analysent l'environnement frontal du véhicule pour alimenter les calculateurs d'aides actives à la conduite."
                },
                {
                    "questionNumber": 51,
                    "question": "Quelle condition est impérative pour le recalibrage statique d'une caméra de pare-brise ?",
                    "answerOptions": [
                        {"text": "Placer le véhicule sur une surface plane et positionner une cible spécifique à une distance précise", "isCorrect": True},
                        {"text": "Conduire le véhicule sur autoroute à une vitesse stabilisée de quatre-vingt-dix kilomètres par heure", "isCorrect": False},
                        {"text": "Augmenter la pression des quatre pneumatiques à trois bars pour rigidifier la suspension", "isCorrect": False},
                        {"text": "Éclairer fortement la zone de travail avec des lampes halogènes pour aveugler le capteur", "isCorrect": False}
                    ],
                    "correction": "La précision du calibrage exige une aire de niveau, un alignement rigoureux par rapport à l'axe de poussée et un éclairage normalisé."
                },
                {
                    "questionNumber": 52,
                    "question": "Comment dépose-t-on un panneau de garniture de porte sans détériorer les fixations ?",
                    "answerOptions": [
                        {"text": "En utilisant une pince à dégarnir ou des spatules en plastique pour faire levier sur les agrafes", "isCorrect": True},
                        {"text": "En tirant violemment d'un coup sec depuis le coin supérieur droit pour casser les clips de maintien", "isCorrect": False},
                        {"text": "En chauffant préalablement la garniture avec un décapeur thermique pour ramollir le plastique", "isCorrect": False},
                        {"text": "En insérant un tournevis plat métallique aiguisé entre la tôle et la garniture pour faire levier", "isCorrect": False}
                    ],
                    "correction": "L'utilisation d'outils de dégarnissage en plastique évite de rayer la peinture et répartit l'effort pour extraire les agrafes sans les arracher."
                },
                {
                    "questionNumber": 53,
                    "question": "Quelle est la fonction d'une gâche de serrure sur un montant de carrosserie ?",
                    "answerOptions": [
                        {"text": "Servir de point d'ancrage fixe pour le pêne de la serrure et assurer la fermeture de l'ouvrant", "isCorrect": True},
                        {"text": "Verrouiller électriquement les portes arrière pour la sécurité des enfants à bord", "isCorrect": False},
                        {"text": "Détecter la présence de la clé mains libres pour autoriser le déverrouillage de la porte", "isCorrect": False},
                        {"text": "Amortir le choc lors de la fermeture de la portière pour préserver le confort acoustique", "isCorrect": False}
                    ],
                    "correction": "La gâche est la pièce métallique fixe sur le pied milieu ou arrière qui retient le mécanisme mobile intégré dans la porte."
                },
                {
                    "questionNumber": 54,
                    "question": "Quel risque présente une découpe de pare-brise au fil carré en acier ?",
                    "answerOptions": [
                        {"text": "Rayer la peinture de la feuillure de baie ou endommager la garniture intérieure du pavillon", "isCorrect": True},
                        {"text": "Déchirer le film en butyral de polyvinyle inséré entre les deux couches de verre feuilleté", "isCorrect": False},
                        {"text": "Déformer irrémédiablement le galbe du pare-brise neuf avant même son installation", "isCorrect": False},
                        {"text": "Provoquer l'explosion spontanée du vitrage en mille morceaux tranchants dans l'habitacle", "isCorrect": False}
                    ],
                    "correction": "Le fil d'acier est très coupant. Un mauvais angle de traction peut entamer la couche d'électrozingage de la baie, provoquant une corrosion future."
                },
                {
                    "questionNumber": 55,
                    "question": "Pourquoi les pare-brise modernes sont-ils fabriqués en verre feuilleté plutôt qu'en verre trempé ?",
                    "answerOptions": [
                        {"text": "Le verre feuilleté maintient les éclats en place grâce à son film intercalaire en plastique, évitant ainsi les blessures graves en cas de bris.", "isCorrect": True},
                        {"text": "Le verre feuilleté est beaucoup plus léger, ce qui permet aux constructeurs de réduire le poids global du véhicule et d'abaisser significativement la consommation de carburant sur les longs trajets autoroutiers.", "isCorrect": False},
                        {"text": "Le verre feuilleté résiste naturellement au phénomène d'éblouissement nocturne provoqué par les phares à technologie laser des véhicules circulant en sens inverse sur les routes départementales non éclairées.", "isCorrect": False},
                        {"text": "Le verre feuilleté intègre des micro-canaux remplis de liquide chauffant qui assurent un dégivrage instantané de la surface vitrée dès que la température extérieure descend en dessous de zéro degré.", "isCorrect": False}
                    ],
                    "correction": "Le PVB (Polybutyral de vinyle) emprisonne les débris de verre et assure l'imperméabilité de la baie même après un choc majeur, contrairement au verre trempé qui explose."
                },
                {
                    "questionNumber": 56,
                    "question": "Comment s'effectue la repose d'un ciel de toit collé dans l'habitacle d'un véhicule ?",
                    "answerOptions": [
                        {"text": "En vaporisant une colle néoprène spécifique sur les deux surfaces, en respectant un temps de gommage, puis en marouflant soigneusement du centre vers les bords.", "isCorrect": True},
                        {"text": "En clipsant vigoureusement la garniture sur les profilés en aluminium dissimulés sous la tôle de pavillon à l'aide d'un maillet de carrossier à embout en nylon souple pour ne pas marquer le tissu.", "isCorrect": False},
                        {"text": "En appliquant un cordon continu de mastic polyuréthane haute densité tout autour du cadre de pavillon puis en maintenant le ciel de toit avec des sangles à cliquet serrées au maximum pendant deux jours.", "isCorrect": False},
                        {"text": "En chauffant la résine thermoplastique intégrée au dos du tissu avec une lampe à infrarouge réglée à deux cents degrés jusqu'à obtenir une adhésion moléculaire complète avec la tôle d'acier.", "isCorrect": False}
                    ],
                    "correction": "La colle de contact aérosol s'applique sur les deux faces. Après le temps d'évaporation des solvants, le marouflage garantit une fixation uniforme sans plis."
                },
                {
                    "questionNumber": 57,
                    "question": "Quel paramètre est indispensable à vérifier avant de procéder au recalibrage dynamique d'un capteur radar frontal ?",
                    "answerOptions": [
                        {"text": "La géométrie des trains roulants, l'assiette du véhicule et la pression correcte de tous les pneumatiques.", "isCorrect": True},
                        {"text": "Le niveau de charge de la batterie haute tension du système de propulsion électrique afin de s'assurer que le radar dispose d'une puissance d'émission maximale lors de la phase de roulage d'apprentissage.", "isCorrect": False},
                        {"text": "La propreté absolue du miroir intérieur du rétroviseur central, car c'est lui qui réfléchit les ondes électromagnétiques nécessaires à la télémétrie laser du régulateur de vitesse adaptatif.", "isCorrect": False},
                        {"text": "L'épaisseur des disques de frein avant, car le système de freinage d'urgence automatique nécessite une décélération théorique parfaitement constante pour valider la procédure de calibration.", "isCorrect": False}
                    ],
                    "correction": "Le radar s'appuie sur l'axe de poussée réel du véhicule. Une mauvaise géométrie des roues arrière fausserait totalement la trajectoire perçue par le système."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle est l'utilité du traitement hydrophobe souvent appliqué sur les vitrages latéraux avant ?",
                    "answerOptions": [
                        {"text": "Améliorer la visibilité sous la pluie en facilitant l'écoulement rapide des gouttes d'eau sous l'effet du vent.", "isCorrect": True},
                        {"text": "Empêcher totalement la formation de givre ou de condensation à l'intérieur de l'habitacle lors des périodes hivernales grâce à une barrière d'ions d'argent intégrée à la surface du verre.", "isCorrect": False},
                        {"text": "Bloquer la transmission des ondes radio et des signaux cellulaires pour éviter que les dispositifs de brouillage électronique ne perturbent les communications du boîtier télématique de sécurité.", "isCorrect": False},
                        {"text": "Augmenter la résistance mécanique du verre aux impacts de gravillons projetés à très haute vitesse par les véhicules tout-terrain circulant sur les chemins rocailleux non goudronnés.", "isCorrect": False}
                    ],
                    "correction": "Le traitement modifie la tension de surface du verre, ce qui empêche l'eau de s'étaler et favorise son évacuation aérodynamique."
                },
                {
                    "questionNumber": 59,
                    "question": "Lors de l'ajustage final d'un capot moteur, quel rôle jouent les butées réglables en caoutchouc ?",
                    "answerOptions": [
                        {"text": "Elles permettent d'affiner l'affleurement avec les ailes avant et de caler le capot pour éviter qu'il ne vibre en roulant.", "isCorrect": True},
                        {"text": "Elles amortissent le choc en cas de collision avec un piéton en se déformant hydrauliquement pour absorber une très grande quantité d'énergie cinétique en quelques millisecondes.", "isCorrect": False},
                        {"text": "Elles établissent une liaison électrique de masse parfaite entre la charnière métallique et la caisse en blanc pour neutraliser les interférences électromagnétiques du compartiment moteur.", "isCorrect": False},
                        {"text": "Elles verrouillent automatiquement la fermeture du compartiment moteur dès que la vitesse du véhicule dépasse les cinquante kilomètres par heure afin d'empêcher une ouverture intempestive.", "isCorrect": False}
                    ],
                    "correction": "Le vissage ou dévissage de ces tampons permet de compenser les tolérances géométriques et assure le maintien sous tension de la gâche du capot."
                },
                {
                    "questionNumber": 60,
                    "question": "Quel contrôle final est obligatoire après le remplacement d'un airbag latéral intégré dans un siège ?",
                    "answerOptions": [
                        {"text": "Interroger la mémoire du calculateur avec l'outil de diagnostic, vérifier l'absence de code défaut et contrôler l'extinction du voyant au tableau de bord.", "isCorrect": True},
                        {"text": "Déclencher artificiellement une micro-explosion contrôlée à l'intérieur du générateur de gaz pour mesurer la pression de gonflage nominale du coussin de sécurité à l'aide d'un manomètre spécifique.", "isCorrect": False},
                        {"text": "Recoudre la garniture du siège avec un fil de Kevlar extrêmement résistant pour s'assurer que la housse ne se déchirera jamais, même en cas de sollicitation extrême lors d'une sortie de route.", "isCorrect": False},
                        {"text": "Pulvériser un aérosol de détection de fuite sur les coutures de la housse du siège pour confirmer que le coussin gonflable est parfaitement étanche et conservera sa pression maximale indéfiniment.", "isCorrect": False}
                    ],
                    "correction": "Le passage à la valise permet d'attester que la boucle pyrotechnique est correctement rebranchée et que le système est de nouveau opérationnel et fonctionnel."
                }
            ]
        },
        # =========================================================================
        # THÈME 4 : DIAGNOSTIC DES DÉFORMATIONS, REDRESSAGE ET RESTRUCTURATION DES SOUBASSEMENTS (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : DIAGNOSTIC DES DÉFORMATIONS, REDRESSAGE ET RESTRUCTURATION DES SOUBASSEMENTS",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel outil mesure les longueurs, largeurs et hauteurs sur un soubassement déformé ?",
                    "answerOptions": [
                        {"text": "Banc tridimensionnel", "isCorrect": True},
                        {"text": "Pige mécanique", "isCorrect": False},
                        {"text": "Mètre ruban", "isCorrect": False},
                        {"text": "Équerre graduée", "isCorrect": False}
                    ],
                    "correction": "Les systèmes de mesure 3D informatisés permettent un relevé précis des coordonnées X, Y et Z de chaque point par rapport au référentiel constructeur."
                },
                {
                    "questionNumber": 62,
                    "question": "Quelle est la fonction d'une crash-box derrière le pare-chocs ?",
                    "answerOptions": [
                        {"text": "Absorber l'énergie", "isCorrect": True},
                        {"text": "Refroidir le moteur", "isCorrect": False},
                        {"text": "Supporter le capot", "isCorrect": False},
                        {"text": "Filtrer l'air", "isCorrect": False}
                    ],
                    "correction": "La crash-box est un absorbeur de choc fusible qui se déforme pour préserver les longerons lors des collisions à basse vitesse."
                },
                {
                    "questionNumber": 63,
                    "question": "Comment appelle-t-on le redressement d'une tôle par rétreinte thermique ?",
                    "answerOptions": [
                        {"text": "Chauffe de retrait", "isCorrect": True},
                        {"text": "Trempe superficielle", "isCorrect": False},
                        {"text": "Revenu d'acier", "isCorrect": False},
                        {"text": "Débobinage", "isCorrect": False}
                    ],
                    "correction": "La chauffe de retrait crée un point de chauffe au carbone ou au chalumeau suivi d'un refroidissement rapide, ce qui rétreint la tôle distendue."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel repère virtuel sert de base de mesure verticale sur un marbre ?",
                    "answerOptions": [
                        {"text": "Le plan zéro", "isCorrect": True},
                        {"text": "L'axe de symétrie", "isCorrect": False},
                        {"text": "Le centre de gravité", "isCorrect": False},
                        {"text": "L'entraxe des roues", "isCorrect": False}
                    ],
                    "correction": "Le plan zéro est une ligne horizontale de référence virtuelle située sous le véhicule à partir de laquelle toutes les hauteurs sont définies."
                },
                {
                    "questionNumber": 65,
                    "question": "Qu'est-ce qu'une déformation induite suite à un choc automobile ?",
                    "answerOptions": [
                        {"text": "Une déformation située à distance du point d'impact, causée par la transmission des efforts dans la structure", "isCorrect": True},
                        {"text": "Une bosse superficielle créée par le rebond d'un objet extérieur sur un panneau de carrosserie élastique", "isCorrect": False},
                        {"text": "Un pli de tôle localisé exactement à l'endroit où le pare-chocs a été percuté par un obstacle fixe", "isCorrect": False},
                        {"text": "L'écrasement volontaire d'une zone fusible programmée par le constructeur pour protéger les passagers", "isCorrect": False}
                    ],
                    "correction": "Les châssis autoporteurs transmettent l'énergie cinétique du choc : un longeron avant peut plier le plancher central ou le pavillon par répercussion."
                },
                {
                    "questionNumber": 66,
                    "question": "Quel est le principe fondamental du débobinage lors d'un redressage sur marbre ?",
                    "answerOptions": [
                        {"text": "Tirer dans le sens strictement opposé et dans l'ordre inverse à celui où le choc s'est produit", "isCorrect": True},
                        {"text": "Chauffer toutes les zones pliées au rouge cerise avant d'appliquer une traction continue et lente", "isCorrect": False},
                        {"text": "Découper les éléments gravement endommagés pour relâcher les tensions avant de redresser la caisse", "isCorrect": False},
                        {"text": "Appliquer une force hydraulique maximale en un seul point central pour réaligner toute la structure", "isCorrect": False}
                    ],
                    "correction": "Le débobinage consiste à inverser la chronologie du crash pour déplier la structure sans déchirer le métal ni créer de nouvelles tensions."
                },
                {
                    "questionNumber": 67,
                    "question": "À quoi sert un système de mesure par piges mécaniques ?",
                    "answerOptions": [
                        {"text": "Comparer la symétrie des points de référence entre le côté gauche et le côté droit du véhicule", "isCorrect": True},
                        {"text": "Mesurer la résistance électrique des points de soudure par résistance pour évaluer la rigidité", "isCorrect": False},
                        {"text": "Vérifier l'angle de braquage maximal des roues avant pour diagnostiquer un défaut de crémaillère", "isCorrect": False},
                        {"text": "Déterminer l'épaisseur exacte de la peinture appliquée sur les longerons après réparation", "isCorrect": False}
                    ],
                    "correction": "Le compas de soubassement permet des contrôles rapides par triangulation et la vérification de la symétrie diagonale d'un châssis."
                },
                {
                    "questionNumber": 68,
                    "question": "Quelle règle impérative s'applique au manchonnage lors d'une coupe sur longeron ?",
                    "answerOptions": [
                        {"text": "L'utilisation d'un renfort intérieur spécifiquement défini et positionné selon les consignes du constructeur", "isCorrect": True},
                        {"text": "La réalisation d'un soudage continu bord à bord sur toute la circonférence sans aucun chevauchement de tôle", "isCorrect": False},
                        {"text": "Le remplissage intégral du corps creux avec de la mousse polyuréthane expansive pour rigidifier la liaison", "isCorrect": False},
                        {"text": "La fixation de la greffe exclusivement par des rivets en plastique à très haute résistance à la cisaille", "isCorrect": False}
                    ],
                    "correction": "Le manchon intérieur redonne la solidité originelle au longeron sectionné et garantit la rigidité structurelle en cas de nouveau choc."
                },
                {
                    "questionNumber": 69,
                    "question": "Que représente la fiche de contrôle dimensionnel d'un soubassement ?",
                    "answerOptions": [
                        {"text": "Le recueil des cotes X, Y et Z d'origine spécifiées par le constructeur pour chaque point de référence", "isCorrect": True},
                        {"text": "Un tableau indiquant le temps de barème alloué pour remplacer les amortisseurs avant et arrière", "isCorrect": False},
                        {"text": "Le graphique de puissance du moteur thermique obtenu après le passage du véhicule sur un banc de puissance", "isCorrect": False},
                        {"text": "Un document répertoriant les teintes de peinture d'usine et les codes de garnissage intérieur", "isCorrect": False}
                    ],
                    "correction": "Cette fiche fournit les tolérances et les cotes exactes nécessaires pour calibrer le banc de mesure et vérifier la géométrie de la caisse."
                },
                {
                    "questionNumber": 70,
                    "question": "Quel est l'avantage du débosselage sans peinture ?",
                    "answerOptions": [
                        {"text": "Supprimer les petits impacts sans avoir besoin de mastiquer ni de repeindre l'élément", "isCorrect": True},
                        {"text": "Permettre le redressage de plis extrêmement profonds sur des tôles en acier au bore trempé", "isCorrect": False},
                        {"text": "Remplacer l'utilisation d'un tire-clou pour extraire des enfoncements sans accès par l'arrière", "isCorrect": False},
                        {"text": "Accélérer le temps de séchage des apprêts de charge appliqués sur les petites rayures", "isCorrect": False}
                    ],
                    "correction": "Le DSP utilise des leviers ou des colles spécifiques pour repousser doucement la bosse, préservant ainsi la peinture d'origine et le vernis."
                },
                {
                    "questionNumber": 71,
                    "question": "Quel rôle joue une zone fusible intégrée dans un brancard avant ?",
                    "answerOptions": [
                        {"text": "Plier de manière contrôlée pour absorber une partie de l'énergie cinétique lors d'une collision", "isCorrect": True},
                        {"text": "Augmenter la rigidité de l'habitacle pour empêcher le moteur de reculer vers les passagers", "isCorrect": False},
                        {"text": "Servir de point d'appui renforcé pour la fixation du vérin de levage du cric de secours", "isCorrect": False},
                        {"text": "Accélérer la dissipation thermique du compartiment moteur grâce à de petites ouïes d'aération", "isCorrect": False}
                    ],
                    "correction": "Les plis ou amorces de rupture intégrés dans la tôle forcent le longeron à s'écraser en accordéon pour dissiper la violence de l'impact."
                },
                {
                    "questionNumber": 72,
                    "question": "Comment fonctionne le principe de tirage par tire-clou ?",
                    "answerOptions": [
                        {"text": "On soude de petites anneaux sur la tôle par résistance électrique pour pouvoir tirer la zone enfoncée", "isCorrect": True},
                        {"text": "On perce des trous dans l'enfoncement pour y visser de longues tiges filetées reliées à un treuil manuel", "isCorrect": False},
                        {"text": "On colle de puissantes ventouses magnétiques sur la peinture pour aspirer la bosse vers l'extérieur", "isCorrect": False},
                        {"text": "On projette des clous en acier à haute vitesse pour perforer la tôle et la détordre depuis l'intérieur", "isCorrect": False}
                    ],
                    "correction": "Le poste tire-clou soude par inertie des étoiles ou anneaux en cuivre/acier qui servent d'ancrage temporaire pour extraire les bosses fermées."
                },
                {
                    "questionNumber": 73,
                    "question": "Quelle est la fonction d'une équerre de traction hydraulique ?",
                    "answerOptions": [
                        {"text": "Exercer une force de tirage modulable et orientable sur les éléments de structure déformés", "isCorrect": True},
                        {"text": "Soulever verticalement le moteur thermique pour faciliter son extraction hors du compartiment", "isCorrect": False},
                        {"text": "Mesurer avec précision l'angle de carrossage et de chasse du train avant après un choc latéral", "isCorrect": False},
                        {"text": "Maintenir fermement la portière en position ouverte pendant l'application du vernis polyuréthane", "isCorrect": False}
                    ],
                    "correction": "Le Dozer permet d'orienter précisément l'effort hydraulique en hauteur et en inclinaison pour débobiner la tôle exactement dans l'axe du choc."
                },
                {
                    "questionNumber": 74,
                    "question": "Que permet d'identifier l'apparition d'écailles de peinture ou de mastic craquelé sur un soubassement ?",
                    "answerOptions": [
                        {"text": "La présence d'une amorce de pli ou d'une déformation induite causée par une transmission d'effort", "isCorrect": True},
                        {"text": "Un défaut de fabrication initial en usine lors de l'immersion de la caisse dans le bain de cataphorèse", "isCorrect": False},
                        {"text": "L'utilisation excessive de détergents alcalins lors du lavage haute pression des passages de roues", "isCorrect": False},
                        {"text": "Une usure prématurée de l'insonorisant sous l'effet des projections répétées de graviers routiers", "isCorrect": False}
                    ],
                    "correction": "L'acier est plus élastique que le mastic ou la laque de finition. Une déformation du support entraîne la fissuration de la peinture, indiquant un pli caché."
                },
                {
                    "questionNumber": 75,
                    "question": "Pourquoi est-il indispensable d'ancrer fermement le véhicule sur le banc de redressage avant d'exercer une traction ?",
                    "answerOptions": [
                        {"text": "Pour éviter tout déplacement de la caisse, maîtriser parfaitement les forces appliquées et s'assurer que la traction s'exerce uniquement sur les zones déformées.", "isCorrect": True},
                        {"text": "Pour comprimer au maximum les ressorts de suspension afin de stabiliser le centre de gravité et empêcher les amortisseurs d'absorber l'effort hydraulique du vérin.", "isCorrect": False},
                        {"text": "Pour faciliter le raccordement du système de diagnostic électronique au boîtier central et permettre la lecture continue des paramètres des capteurs de roue en temps réel.", "isCorrect": False},
                        {"text": "Pour établir un contact de masse électrique optimal entre le châssis du véhicule et le sol de l'atelier, évitant ainsi l'électrocution de l'opérateur lors du soudage par point.", "isCorrect": False}
                    ],
                    "correction": "Sans un ancrage rigide (sur au moins quatre points de feuillure), la traction hydraulique déplacerait l'ensemble du véhicule au lieu d'étirer le métal déformé."
                },
                {
                    "questionNumber": 76,
                    "question": "Quel est le principe d'évaluation tridimensionnelle des points de soubassement ?",
                    "answerOptions": [
                        {"text": "Situer chaque point de référence dans l'espace grâce à trois coordonnées : la longueur, la largeur par rapport au plan de symétrie, et la hauteur par rapport au plan zéro.", "isCorrect": True},
                        {"text": "Déterminer la résistance structurelle d'une pièce en évaluant simultanément sa dureté superficielle, son coefficient d'allongement plastique et sa limite de rupture à la traction axiale.", "isCorrect": False},
                        {"text": "Mesurer le débattement des suspensions selon les trois axes géométriques afin de paramétrer le parallélisme, le carrossage et l'angle de pivot pour garantir une tenue de route parfaite.", "isCorrect": False},
                        {"text": "Scanner l'intégralité de la carrosserie extérieure avec un laser optique pour détecter les micro-rayures, les défauts de brillance du vernis et les légères variations d'épaisseur de la peinture.", "isCorrect": False}
                    ],
                    "correction": "Le contrôle 3D positionne le compas sur l'axe X (longitudinal), Y (transversal) et Z (vertical) pour cartographier le châssis avec une précision millimétrique."
                },
                {
                    "questionNumber": 77,
                    "question": "Lors du remplacement d'un demi-longeron avant, pourquoi le constructeur impose-t-il souvent une ligne de coupe en escalier ?",
                    "answerOptions": [
                        {"text": "Pour augmenter la longueur du cordon de soudure, répartir les contraintes mécaniques sur une zone plus large et éviter de créer un point de faiblesse transversal sur la poutre.", "isCorrect": True},
                        {"text": "Pour simplifier le passage des faisceaux électriques et des conduites hydrauliques à l'intérieur du corps creux sans risquer de les brûler lors du soudage sous atmosphère inerte.", "isCorrect": False},
                        {"text": "Pour aligner plus facilement la pièce de rechange avec le reste de la structure en s'appuyant sur les repères visuels d'origine emboutis directement dans la tôle galvanisée.", "isCorrect": False},
                        {"text": "Pour empêcher toute infiltration d'humidité en créant une chicane naturelle qui bloque l'eau de pluie et rend inutile l'application d'un traitement anticorrosion à la cire.", "isCorrect": False}
                    ],
                    "correction": "La coupe décalée sur les différentes faces du caisson évite une rupture nette de la ligne de force et améliore l'absorption en cas de collision ultérieure."
                },
                {
                    "questionNumber": 78,
                    "question": "Que désigne la notion de plan zéro dans les documentations techniques de carrosserie ?",
                    "answerOptions": [
                        {"text": "Un plan horizontal imaginaire, situé sous le véhicule, à partir duquel toutes les mesures de hauteur sont calculées pour contrôler le soubassement.", "isCorrect": True},
                        {"text": "La ligne médiane verticale séparant le véhicule en deux parties parfaitement symétriques, utilisée exclusivement pour l'équilibrage des masses sur les roues motrices.", "isCorrect": False},
                        {"text": "Le moment précis chronométré en heures où le carrossier débute l'intervention de restructuration après avoir reçu l'accord écrit de la compagnie d'assurance.", "isCorrect": False},
                        {"text": "L'angle d'inclinaison de la surface de l'aire de préparation qui permet l'écoulement des fluides résiduels vers les grilles de récupération des déchets liquides.", "isCorrect": False}
                    ],
                    "correction": "Le Datum Line est le référentiel altimétrique, parallèle au plancher, permettant d'identifier si un longeron est affaissé (plongé) ou remonté."
                },
                {
                    "questionNumber": 79,
                    "question": "Quel phénomène mécanique caractérise la déformation d'un acier multiphasé lorsqu'il dépasse sa limite élastique ?",
                    "answerOptions": [
                        {"text": "Le métal entre dans le domaine plastique et subit une déformation permanente qui ne peut être totalement résorbée que par un effort de traction supérieur à celui du choc initial.", "isCorrect": True},
                        {"text": "La structure cristalline se fragmente instantanément en milliers de morceaux acérés, se comportant comme une vitre en verre trempé sous l'impact d'un projectile lourd.", "isCorrect": False},
                        {"text": "Le panneau de carrosserie absorbe la totalité de l'énergie cinétique puis retrouve automatiquement sa forme d'origine en quelques heures sans aucune intervention extérieure.", "isCorrect": False},
                        {"text": "La température de la pièce s'élève brusquement jusqu'à atteindre son point de fusion localisé, provoquant l'écoulement du zinc de protection sur les éléments mécaniques adjacents.", "isCorrect": False}
                    ],
                    "correction": "La plasticité des aciers modernes nécessite l'application de tensions hydrauliques très élevées avec le Dozer pour obliger la structure à retrouver sa cote d'origine."
                },
                {
                    "questionNumber": 80,
                    "question": "Pourquoi utilise-t-on le marteau à inertie en complément du tirage sur le banc de marbre ?",
                    "answerOptions": [
                        {"text": "Pour créer des ondes de choc ciblées qui libèrent les tensions moléculaires accumulées dans les zones pliées tout en assistant l'effort de traction hydraulique continu.", "isCorrect": True},
                        {"text": "Pour écraser violemment les surépaisseurs de soudure générées par le procédé MAG et lisser parfaitement la tôle avant l'application du mastic de finition polyester.", "isCorrect": False},
                        {"text": "Pour enfoncer en force les piges de mesure dans les trous de référence oxydés du soubassement afin d'assurer un maintien rigide de l'appareillage de contrôle tridimensionnel.", "isCorrect": False},
                        {"text": "Pour générer un bruit sourd et régulier permettant d'évaluer la fréquence de résonance du métal et de détecter la présence de criques internes invisibles à l'œil nu.", "isCorrect": False}
                    ],
                    "correction": "Les ondes de choc provoquées par le branle sur les zones tendues débloquent les grains d'acier coincés et facilitent le retour de la tôle à l'état débobiné."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : RÉPARATION DES MATIÈRES PLASTIQUES, COMPOSITES ET TRAITEMENTS ANTICORROSION (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : RÉPARATION DES MATIÈRES PLASTIQUES, COMPOSITES ET TRAITEMENTS ANTICORROSION",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quel type de polymère peut être remis en forme ou soudé sous l'action répétée de la chaleur sans altération de sa structure moléculaire de base ?",
                    "answerOptions": [
                        {"text": "Le polypropylène", "isCorrect": True},
                        {"text": "La résine polyester thermodurcissable chargée de fibres de verre tressées", "isCorrect": False},
                        {"text": "Le polyuréthane rigide obtenu par polymérisation sous haute pression", "isCorrect": False},
                        {"text": "L'élastomère vulcanisé insensible aux élévations thermiques modérées", "isCorrect": False}
                    ],
                    "correction": "Le polypropylène fait partie des thermoplastiques. Leurs macromolécules linéaires ou ramifiées ne sont pas reliées par des liaisons chimiques permanentes : sous l'action de la chaleur, la matière ramollit et entre en fusion de manière réversible, ce qui autorise le soudage thermique."
                },
                {
                    "questionNumber": 82,
                    "question": "Quel marquage normalisé gravé sur la face interne d'un bouclier indique la présence d'un mélange de polypropylène et d'éthylène-propylène-diène renforcé par vingt pour cent de talc ?",
                    "answerOptions": [
                        {"text": "PP/EPDM TD20", "isCorrect": True},
                        {"text": "PE/PBT GF30", "isCorrect": False},
                        {"text": "ABS/PC MD10", "isCorrect": False},
                        {"text": "PUR/SMC TD40", "isCorrect": False}
                    ],
                    "correction": "Selon la norme ISO 11469, le sigle initial désigne les résines principales mélangées (ici polypropylène et EPDM), tandis que le suffixe TD20 spécifie la nature de la charge minérale (Talc Dust) et sa fraction massique (20 %)."
                },
                {
                    "questionNumber": 83,
                    "question": "Lors d'un test d'identification à la flamme sur un copeau de matière plastique, quel comportement caractérise formellement le polyéthylène ?",
                    "answerOptions": [
                        {"text": "Une flamme bleue à pointe jaune avec égouttement et une odeur de bougie fondue", "isCorrect": True},
                        {"text": "Une flamme jaune sombre très fuligineuse dégageant une forte odeur de corne brûlée", "isCorrect": False},
                        {"text": "Une flamme verte scintillante auto-extinguible libérant des vapeurs acres de chlore", "isCorrect": False},
                        {"text": "Une absence totale de combustion avec simple carbonisation superficielle sans gouttelette", "isCorrect": False}
                    ],
                    "correction": "Le polyéthylène (PE) est une polyoléfine paraffinique. Sa combustion est facile, produit une flamme bleue surmontée d'un sommet jaune, génère des gouttes de polymère fondu qui continuent de brûler en tombant et libère une odeur caractéristique de cire de bougie."
                },
                {
                    "questionNumber": 84,
                    "question": "Quel est l'avantage déterminant de l'apport d'azote chaud par rapport à l'air comprimé standard lors du soudage d'un pare-chocs thermoplastique ?",
                    "answerOptions": [
                        {"text": "Éviter l'oxydation superficielle du bain de fusion pour préserver la cohésion moléculaire et obtenir un cordon résistant", "isCorrect": True},
                        {"text": "Permettre une accélération drastique du temps de polymérisation des chaînes de monomères tout en maintenant une température d'extrusion strictement constante à cœur", "isCorrect": False},
                        {"text": "Empêcher le refroidissement prématuré des talons de chanfrein en saturant la buse d'application d'un gaz inerte qui dissout chimiquement les résidus de peinture environnants", "isCorrect": False},
                        {"text": "Créer une surpression mécanique au fond du chanfrein afin de repousser les microbulles d'air vers l'extérieur et garantir une étanchéité absolue à l'humidité ambiante", "isCorrect": False}
                    ],
                    "correction": "L'azote est un gaz neutre. En chassant l'oxygène de l'air ambiant au niveau de la buse chauffante, il prévient la formation de scories d'oxydation sur les lèvres du chanfrein et la baguette d'apport, garantissant une interpénétration moléculaire homogène et une résistance mécanique optimale."
                },
                {
                    "questionNumber": 85,
                    "question": "Quelle action mécanique préalable est obligatoire aux extrémités d'une fissure sur un panneau plastique avant tout travail de soudure ou de collage ?",
                    "answerOptions": [
                        {"text": "Forer un trou d'arrêt circulaire à chaque extrémité de la fente", "isCorrect": True},
                        {"text": "Poser un rivet d'ancrage aveugle à tête fraisée de chaque côté", "isCorrect": False},
                        {"text": "Réaliser un meulage plat à angle droit sur toute la surface", "isCorrect": False},
                        {"text": "Chauffer localement la zone au chalumeau pour résorber la tension", "isCorrect": False}
                    ],
                    "correction": "Réaliser un perçage débouchant d'environ 3 mm à chaque extrémité d'une fissure permet de répartir les contraintes mécaniques sur une forme circulaire et d'interrompre l'effet d'entaille, empêchant la propagation ultérieure de la déchirure sous l'effet des vibrations."
                },
                {
                    "questionNumber": 86,
                    "question": "Quel composite thermodurcissable moulé sous haute pression et à chaud est couramment utilisé pour fabriquer des hayons ou des faces avant techniques ?",
                    "answerOptions": [
                        {"text": "Le SMC", "isCorrect": True},
                        {"text": "Le polyéthylène haute densité renforcé par des fibres d'aramide", "isCorrect": False},
                        {"text": "Le thermoplastique oléfinique expansé chargé de carbonate de calcium", "isCorrect": False},
                        {"text": "L'acrylonitrile butadiène styrène injecté sans renfort minéral", "isCorrect": False}
                    ],
                    "correction": "Le SMC (Sheet Moulding Compound) est une résine polyester thermodurcissable pré-imprégnée de fibres de verre coupées, moulée par compression à chaud. C'est un composite rigide, indéformable à la chaleur et non fusible."
                },
                {
                    "questionNumber": 87,
                    "question": "Pourquoi est-il indispensable d'appliquer un primaire promoteur d'adhérence spécifique avant de mastiquer ou peindre un élément en polypropylène ?",
                    "answerOptions": [
                        {"text": "Pour modifier la tension superficielle du support et permettre l'accroche chimique des produits", "isCorrect": True},
                        {"text": "Pour boucher les microporosités du plastique et supprimer tout risque d'oxydation interne", "isCorrect": False},
                        {"text": "Pour durcir la surface du plastique afin d'éviter les rayures lors du ponçage à sec", "isCorrect": False},
                        {"text": "Pour neutraliser l'électricité statique accumulée lors des opérations de brossage mécanique", "isCorrect": False}
                    ],
                    "correction": "Les plastiques de la famille des polyoléfines (PP, PE) possèdent une très faible énergie de surface (tension superficielle basse). Sans promoteur d'adhérence chloré ou modifié qui élève artificiellement cette polarité, les mastics et apprêts ne peuvent pas mouiller le support et se décollent."
                },
                {
                    "questionNumber": 88,
                    "question": "Quelle succession chronologique d'opérations doit-on respecter pour réparer une perforation sur un pare-chocs par collage structural bicomposant ?",
                    "answerOptions": [
                        {"text": "Nettoyer au dégraissant spécifique, ouvrir un chanfrein en V, appliquer le primaire d'adhérence, poser la grille de renfort et injecter la colle polyuréthane", "isCorrect": True},
                        {"text": "Poncer à blanc, appliquer directement un mastic polyester armé sur les deux faces, poser un rivet pop intermédiaire et chauffer à deux cents degrés avec une lampe infrarouge", "isCorrect": False},
                        {"text": "Dégraisser au solvant universel cellulosique, meuler à franc bord sans chanfrein, étaler une résine époxy pure sans armature puis laisser sécher vingt-quatre heures à température ambiante", "isCorrect": False},
                        {"text": "Chanfreiner à plat sur vingt millimètres, injecter un primaire acide phosphatant réactif, appliquer une résine thermofusible chaude et recouvrir immédiatement d'un mastic de finition solvanté", "isCorrect": False}
                    ],
                    "correction": "La réparation par collage structural impose une décontamination minutieuse, un chanfreinage pour augmenter la surface de contact, l'application d'un primaire adapté au polymère, puis l'application de la colle polyuréthane ou époxy avec inclusion d'une trame ou grille de renfort textile sur l'envers."
                },
                {
                    "questionNumber": 89,
                    "question": "Quelle technique d'insertion doit être respectée lors de la pose d'agrafes chauffantes sur un thermoplastique fissuré ?",
                    "answerOptions": [
                        {"text": "Enfoncer l'agrafe à mi-épaisseur de la matière puis effectuer une légère rotation avant refroidissement", "isCorrect": True},
                        {"text": "Traverser entièrement la paroi plastique pour rabattre les branches de l'agrafe sur l'envers", "isCorrect": False},
                        {"text": "Chauffer l'agrafe jusqu'à incandescence rouge avant de l'appliquer sur une surface non chanfreinée", "isCorrect": False},
                        {"text": "Refroidir immédiatement la zone avec un jet d'eau glacée dès que l'agrafe touche le plastique", "isCorrect": False}
                    ],
                    "correction": "Les agrafes métalliques doivent être chauffées et insérées à mi-épaisseur de la matière plastique. Une rotation d'un quart de tour avant la solidification emprisonne le métal dans la masse fondue, créant un pontage mécanique solide sans perforer la face opposée."
                },
                {
                    "questionNumber": 90,
                    "question": "Qu'est-ce que le procédé de cataphorèse mis en œuvre sur les caisses nues en usine de construction automobile ?",
                    "answerOptions": [
                        {"text": "Une immersion complète de la caisse dans un bain de peinture hydrosoluble polarisée sous tension électrique", "isCorrect": True},
                        {"text": "Une pulvérisation robotisée d'un vernis polyuréthane cuit à basse température dans un tunnel à infrarouge", "isCorrect": False},
                        {"text": "Une projection de microbilles de zinc en fusion formant un film d'étanchéité mécanique sur les tôles nues", "isCorrect": False},
                        {"text": "Une application électrostatique de cire liquide chaude s'infiltrant dans les replis et sertis de carrosserie", "isCorrect": False}
                    ],
                    "correction": "La cataphorèse est une électrodéposition cathodique. La caisse nue est immergée dans une cuve de peinture hydrosoluble et mise sous cathode (-), attirant les particules de peinture chargées positivement (+), ce qui garantit une couverture protectrice uniforme jusque dans les corps creux."
                },
                {
                    "questionNumber": 91,
                    "question": "Quel phénomène de dégradation électrochimique survient lors de la mise en contact direct d'une tôle d'acier avec un élément d'aluminium en milieu humide ?",
                    "answerOptions": [
                        {"text": "La corrosion galvanique", "isCorrect": True},
                        {"text": "L'oxydation superficielle par cavitation thermique due aux vibrations du châssis", "isCorrect": False},
                        {"text": "La détérioration intergranulaire provoquée par une surchauffe lors du redressage", "isCorrect": False},
                        {"text": "La délamination mécanique sous contrainte liée à une fatigue d'élasticité du métal", "isCorrect": False}
                    ],
                    "correction": "Lorsque deux métaux ayant des potentiels d'oxydoréduction différents sont en contact électrique en présence d'un électrolyte, le métal le plus électronégatif (ici l'aluminium) agit comme anode et subit une dissolution accélérée : c'est la corrosion galvanique ou bimétallique."
                },
                {
                    "questionNumber": 92,
                    "question": "Pour quelle raison technique applique-t-on un cordon de mastic polyuréthane extrudé sur le sertissage périphérique d'un panneau neuf ?",
                    "answerOptions": [
                        {"text": "Empêcher l'infiltration d'humidité et de polluants salins entre les tôles pour neutraliser le risque d'oxydation caverneuse", "isCorrect": True},
                        {"text": "Assurer le maintien mécanique structural définitif du panneau extérieur sur la doublure sans nécessiter de point de soudure ni de collage préalable", "isCorrect": False},
                        {"text": "Compenser les tolérances géométriques de fabrication entre le panneau et la doublure afin d'éviter l'apparition de bruits parasites en roulage à haute vitesse", "isCorrect": False},
                        {"text": "Créer une surépaisseur élastique compressible permettant de réduire les contraintes thermiques subies par la tôle lors du passage en cabine de séchage à soixante degrés", "isCorrect": False}
                    ],
                    "correction": "Les zones de sertissage entre doublure et peau extérieure créent des fentes microscopiques propices à la rétention d'eau et de sel par capillarité. Le mastic d'étanchéité aux sertis forme une barrière imperméable empêchant l'amorce d'une corrosion caverneuse invisible depuis l'extérieur."
                },
                {
                    "questionNumber": 93,
                    "question": "À quel stade précis des réparations d'un soubassement doit-on injecter la cire pour corps creux ?",
                    "answerOptions": [
                        {"text": "Après l'application et le séchage complet des peintures et vernis de finition", "isCorrect": True},
                        {"text": "Directement sur la tôle nue immédiatement après les opérations de débosselage", "isCorrect": False},
                        {"text": "Juste après la soudure des doublures avant le passage du wash-primer", "isCorrect": False},
                        {"text": "Avant le meulage des cordons de soudure pour lubrifier les disques abrasifs", "isCorrect": False}
                    ],
                    "correction": "Les cires corps creux sont appliquées en toute fin d'intervention, une fois le cycle de peinture achevé et cuit. Ces cires grasses et hydrophobes satureraient l'atmosphère de la cabine de peinture en silicones et solvants gras, provoquant de graves défauts de cratérage si elles étaient injectées plus tôt."
                },
                {
                    "questionNumber": 94,
                    "question": "Quelle est la fonction principale d'un primaire réactif phosphatant appliqué en couche mince sur des zones d'acier mises à nu ?",
                    "answerOptions": [
                        {"text": "Passiver le métal et créer une couche de conversion chimique améliorant l'accroche anticorrosion", "isCorrect": True},
                        {"text": "Garnir les rayures profondes issues du ponçage grossier sans nécessiter de mastic polyester", "isCorrect": False},
                        {"text": "Neutraliser définitivement la rouille perforante sans avoir besoin d'éliminer la calamine", "isCorrect": False},
                        {"text": "Former un film isolant étanche résistant aux hydrocarbures et aux projections de gravillons", "isCorrect": False}
                    ],
                    "correction": "Le primaire phosphatant (wash-primer) contient de l'acide phosphorique qui attaque superficiellement le fer pour former une couche de phosphates insolubles (phosphatations). Cette couche de conversion passive le métal et fournit une base d'accrochage pour les apprêts de charge."
                },
                {
                    "questionNumber": 95,
                    "question": "Quelle règle impérative gouverne le choix de la matière d'apport lors d'un soudage au chalumeau à air chaud ou à l'azote sur un thermoplastique ?",
                    "answerOptions": [
                        {"text": "Utiliser exclusivement un fil d'apport constitué d'un polymère strictement identique à celui de la pièce à réparer", "isCorrect": True},
                        {"text": "Sélectionner systématiquement une baguette d'apport en polyéthylène universel car sa basse température de fusion s'adapte à tous les thermoplastiques automobiles", "isCorrect": False},
                        {"text": "Employer une baguette thermo-fusible composite chargée à quarante pour cent de talc afin d'augmenter la rigidité structurelle du talon de soudure sur les pare-chocs", "isCorrect": False},
                        {"text": "Choisir un matériau d'apport doté d'une température de fusion supérieure de cinquante degrés par rapport au support d'origine pour garantir une interpénétration optimale à chaud", "isCorrect": False}
                    ],
                    "correction": "Deux polymères différents ne sont généralement pas miscibles à l'échelle moléculaire. Pour garantir la formation de chaînes macromoléculaires continues et une cohésion mécanique identique à l'origine, la baguette d'apport doit rigoureusement posséder la même composition chimique que la pièce support."
                },
                {
                    "questionNumber": 96,
                    "question": "Quel principe de protection électrochimique assure la préservation de l'acier sur une tôle galvanisée en cas de rayure atteignant le métal de base ?",
                    "answerOptions": [
                        {"text": "L'anode sacrificielle", "isCorrect": True},
                        {"text": "La passivation anodique forcée par oxydoréduction spontanée du dioxyde de carbone", "isCorrect": False},
                        {"text": "La neutralisation cathodique provoquée par la diffusion d'ions chlore dans la peinture", "isCorrect": False},
                        {"text": "L'isolation diélectrique assurée par la formation d'un film lipidique imperméable", "isCorrect": False}
                    ],
                    "correction": "Le zinc présente un potentiel électrochimique standard plus électronégatif (-0,76 V) que celui du fer (-0,44 V). En présence d'humidité, le zinc s'oxyde préférentiellement en jouant le rôle d'anode sacrificielle, protégeant cathodiquement l'acier exposé adjacent."
                },
                {
                    "questionNumber": 97,
                    "question": "Pourquoi est-il strictement impossible de reformer ou de souder un élément de carrosserie en résine thermodurcissable par élévation de température ?",
                    "answerOptions": [
                        {"text": "Les liaisons chimiques réticulées se dégradent et brûlent sous l'effet de la chaleur sans jamais fondre", "isCorrect": True},
                        {"text": "La température nécessaire pour liquéfier le matériau dépasse le point d'éclair des fibres de renfort", "isCorrect": False},
                        {"text": "L'apport calorifique provoque une vaporisation explosive de la résine sans ramollissement préalable", "isCorrect": False},
                        {"text": "Le polymère fond à très basse température et s'écoule sans pouvoir former de bain de fusion stable", "isCorrect": False}
                    ],
                    "correction": "Les thermodurcissables sont caractérisés par une polymérisation tridimensionnelle irréversible avec des liaisons covalentes croisées (réticulation). Une exposition à une forte température ne provoque pas de fusion, mais une dégradation pyrolytique : le matériau brûle et se détruit sans ramollir."
                },
                {
                    "questionNumber": 98,
                    "question": "Pourquoi préconise-t-on le primaire époxy bicomposant lors des interventions lourdes de restructuration après décapage des tôles nues ?",
                    "answerOptions": [
                        {"text": "Il présente une étanchéité remarquable à l'humidité et une adhérence mécanique exceptionnelle sur métaux ferreux et non ferreux", "isCorrect": True},
                        {"text": "Il polymérise en quelques secondes sous lumière ultraviolette sans nécessiter d'adjonction de durcisseur ni d'évaporation de solvant résiduel", "isCorrect": False},
                        {"text": "Il contient des inhibiteurs acides corrosifs capables de dissoudre chimiquement les résidus épais de rouille perforante logés au fond des cratères de corrosion", "isCorrect": False},
                        {"text": "Il dispense totalement l'opérateur d'appliquer un mastic garnissant ou une laque de finition grâce à son pouvoir couvrant extrêmement élevé et autonivelant", "isCorrect": False}
                    ],
                    "correction": "Les primaires époxydiques forment par réticulation un réseau dense, non poreux et chimiquement inerte. Ils bloquent le passage de la vapeur d'eau et de l'oxygène vers le métal et procurent une excellente adhérence sur l'acier, l'électrozingué et l'aluminium."
                },
                {
                    "questionNumber": 99,
                    "question": "Quelle opération de préparation est obligatoire sur une pièce plastique neuve brute sortie de son emballage avant tout ponçage d'accroche ?",
                    "answerOptions": [
                        {"text": "Réaliser un étuvage suivi d'un nettoyage complet avec un solvant dégraissant spécifique pour plastiques", "isCorrect": True},
                        {"text": "Brûler superficiellement la surface avec la flamme bleue d'un chalumeau oxyacétylénique", "isCorrect": False},
                        {"text": "Déposer une couche épaisse de décapant chimique cellulosique et rincer immédiatement à l'eau", "isCorrect": False},
                        {"text": "Passer un chiffon imprégné de diluant de nettoyage synthétique très agressif pour ramollir la peau", "isCorrect": False}
                    ],
                    "correction": "Les pièces en plastique injectées neuves contiennent des cires de démoulage incrustées dans les micropores de surface. Un étuvage modéré (environ 50 °C) fait ressuer ces cires, qui sont ensuite dissoutes et éliminées à l'aide d'un dégraissant antistatique approprié avant tout ponçage abrasif."
                },
                {
                    "questionNumber": 100,
                    "question": "Quelle est l'utilité première de l'application d'un produit insonorisant et antigravillons à base de résines synthétiques sous les passages de roue ?",
                    "answerOptions": [
                        {"text": "Protéger les tôles d'acier contre les impacts d'agrégats routiers et atténuer la transmission acoustique des bruits de roulement vers l'habitacle", "isCorrect": True},
                        {"text": "Rigidifier la structure monocoque du véhicule en reliant les points de soudure des passages de roue pour augmenter la résistance à la torsion en virage", "isCorrect": False},
                        {"text": "Éliminer tout besoin d'appliquer un traitement anticorrosion électrophorétique sur les pièces embouties grâce à une neutralisation cathodique permanente du métal", "isCorrect": False},
                        {"text": "Assurer un profilage aérodynamique sous le châssis en créant une surface texturée qui canalise l'écoulement des flux d'air pour réduire la traînée globale à haute vitesse", "isCorrect": False}
                    ],
                    "correction": "Les revêtements antigravillons texturés forment une couche souple et épaisse qui absorbe l'énergie cinétique des gravillons projetés par les pneumatiques, évitant l'écaillage des primaires anticorrosion, tout en amortissant les vibrations sonores résonnant dans les passages de roue."
                }
            ]
        }
    }
}