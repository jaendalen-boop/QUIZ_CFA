quiz_data = {
    "title": "Quiz CS Employé Barman (100 Questions)",
    "themes": {
        # =========================================================================
        # THÈME 1 : LÉGISLATION, RÉGLEMENTATION ET HYGIÈNE AU BAR (Questions 1 à 20)
        # =========================================================================
        1: {
            "name": "THÈME 1 : LÉGISLATION, RÉGLEMENTATION ET HYGIÈNE AU BAR",
            "questions": [
                {
                    "questionNumber": 1,
                    "question": "Quelle licence est obligatoire pour vendre des spiritueux purs comme le whisky ou le rhum ?",
                    "answerOptions": [
                        {"text": "La licence IV", "isCorrect": True},
                        {"text": "La grande licence restaurant", "isCorrect": False},
                        {"text": "L'autorisation préfectorale temporaire", "isCorrect": False},
                        {"text": "Le permis d'exploitation restreint", "isCorrect": False}
                    ],
                    "correction": "La Licence IV (ou grande licence) est indispensable pour la vente sur place de toutes les boissons dont la consommation est autorisée, y compris les alcools forts des groupes 4 et 5."
                },
                {
                    "questionNumber": 2,
                    "question": "Quel affichage lié à la santé publique est obligatoire dans tout débit de boissons ?",
                    "answerOptions": [
                        {"text": "La législation sur la répression de l'ivresse publique", "isCorrect": True},
                        {"text": "Le numéro de téléphone du centre antipoison régional", "isCorrect": False},
                        {"text": "La liste complète des allergènes présents dans l'air", "isCorrect": False},
                        {"text": "Le règlement intérieur du personnel de salle", "isCorrect": False}
                    ],
                    "correction": "La loi impose l'affichage bien en évidence de la législation concernant la répression de l'ivresse publique et la protection des mineurs, pour informer les clients de leurs responsabilités et des interdictions."
                },
                {
                    "questionNumber": 3,
                    "question": "Que stipule la loi concernant l'accès des mineurs non accompagnés à un débit de boissons de licence IV ?",
                    "answerOptions": [
                        {"text": "L'accès leur est formellement interdit s'ils ont moins de seize ans", "isCorrect": True},
                        {"text": "Ils peuvent entrer librement et consommer uniquement des boissons du premier groupe à condition de présenter obligatoirement une décharge signée par leurs deux parents légaux avant dix-huit heures", "isCorrect": False},
                        {"text": "Le barman doit confisquer leur pièce d'identité et alerter immédiatement les forces de l'ordre dès leur passage passé le seuil de la porte d'entrée principale de l'établissement", "isCorrect": False},
                        {"text": "L'accès est toléré pour les plus de quatorze ans s'ils s'assoient au fond de la salle et commandent un repas complet avec une boisson chaude", "isCorrect": False}
                    ],
                    "correction": "La loi interdit de recevoir dans les débits de boissons à consommer sur place des mineurs de moins de 16 ans qui ne sont pas accompagnés de leurs parents ou d'un majeur en ayant la charge."
                },
                {
                    "questionNumber": 4,
                    "question": "Quelle est la température légale de conservation des produits frais périssables au bar ?",
                    "answerOptions": [
                        {"text": "Entre zéro et quatre degrés Celsius", "isCorrect": True},
                        {"text": "Entre cinq et huit degrés Celsius", "isCorrect": False},
                        {"text": "Exactement moins dix degrés Celsius", "isCorrect": False},
                        {"text": "À température ambiante sous cloche", "isCorrect": False}
                    ],
                    "correction": "Pour bloquer le développement microbien, les denrées très périssables (lait, crème, purées de fruits, sirops maison) doivent être stockées dans une enceinte réfrigérée maintenue entre 0 °C et +4 °C."
                },
                {
                    "questionNumber": 5,
                    "question": "Comment nomme-t-on le système d'analyse et de maîtrise des risques alimentaires ?",
                    "answerOptions": [
                        {"text": "L'HACCP", "isCorrect": True},
                        {"text": "Le protocole ISO", "isCorrect": False},
                        {"text": "La norme AFNOR", "isCorrect": False},
                        {"text": "Le standard INRS", "isCorrect": False}
                    ],
                    "correction": "L'HACCP (Hazard Analysis Critical Control Point) est la méthode de référence obligatoire en restauration et au bar pour identifier, évaluer et maîtriser les dangers significatifs au regard de la sécurité des aliments."
                },
                {
                    "questionNumber": 6,
                    "question": "Pour quel motif un barman a-t-il le droit de refuser de servir un client ?",
                    "answerOptions": [
                        {"text": "Si le client présente un état d'ébriété manifeste", "isCorrect": True},
                        {"text": "Si le client refuse de laisser un pourboire", "isCorrect": False},
                        {"text": "Si le client commande une simple carafe d'eau", "isCorrect": False},
                        {"text": "Si la tenue du client déplaît au personnel", "isCorrect": False}
                    ],
                    "correction": "Le refus de vente est en principe interdit par la loi, sauf pour motif légitime. L'état d'ivresse manifeste est un motif légitime et même une obligation légale pour le barman, qui risque des sanctions s'il continue à servir l'individu."
                },
                {
                    "questionNumber": 7,
                    "question": "Quelle action s'impose si une brique de crème fraîche a dépassé sa Date Limite de Consommation ?",
                    "answerOptions": [
                        {"text": "Elle doit être retirée du service et jetée immédiatement", "isCorrect": True},
                        {"text": "Elle peut être conservée et utilisée dans les cocktails chauds uniquement si elle est portée à une température d'ébullition constante pendant au moins quinze minutes sous la buse vapeur de la machine à expresso", "isCorrect": False},
                        {"text": "Le chef barman doit goûter le produit devant le client pour s'assurer de sa qualité avant de l'intégrer dans le shaker avec de la glace pilée et du sirop de sucre de canne", "isCorrect": False},
                        {"text": "La législation autorise une marge de tolérance de cinq jours supplémentaires pour les produits laitiers industriels stockés dans la porte du réfrigérateur de la station de travail", "isCorrect": False}
                    ],
                    "correction": "La DLC (Date Limite de Consommation) est une limite impérative. Au-delà, le produit présente un danger pour la santé et doit être obligatoirement détruit. C'est très différent de la DDM (Date de Durabilité Minimale)."
                },
                {
                    "questionNumber": 8,
                    "question": "À quelle fréquence la cuve de la machine à glaçons doit-elle être vidée et désinfectée ?",
                    "answerOptions": [
                        {"text": "Au moins une fois par mois", "isCorrect": True},
                        {"text": "Uniquement à la fin de la saison", "isCorrect": False},
                        {"text": "Tous les jours après le service", "isCorrect": False},
                        {"text": "Quand la glace devient trouble", "isCorrect": False}
                    ],
                    "correction": "La cuve de la machine à glaçons est un milieu très propice aux moisissures et bactéries (Listeria, salmonelles). La méthode HACCP impose un nettoyage et une désinfection profonde au minimum mensuelle."
                },
                {
                    "questionNumber": 9,
                    "question": "Quelle règle gère la rotation des stocks périssables au réfrigérateur ?",
                    "answerOptions": [
                        {"text": "Le FIFO", "isCorrect": True},
                        {"text": "Le LIFO", "isCorrect": False},
                        {"text": "Le FEFO", "isCorrect": False},
                        {"text": "Le FAST", "isCorrect": False}
                    ],
                    "correction": "Le principe FIFO (First In, First Out ou Premier Entré, Premier Sorti) garantit que les produits les plus anciens sont utilisés en premier pour éviter le dépassement des dates de péremption."
                },
                {
                    "questionNumber": 10,
                    "question": "Quel est le seuil légal d'alcoolémie au volant en France pour un permis définitif ?",
                    "answerOptions": [
                        {"text": "Zéro virgule cinq gramme par litre de sang", "isCorrect": True},
                        {"text": "Zéro virgule deux gramme par litre de sang", "isCorrect": False},
                        {"text": "Zéro virgule huit gramme par litre de sang", "isCorrect": False},
                        {"text": "Un gramme par litre de sang", "isCorrect": False}
                    ],
                    "correction": "Le barman doit connaître les limites légales pour conseiller et protéger ses clients. La limite est de 0,5 g/L de sang (ou 0,25 mg/L d'air expiré) pour un conducteur expérimenté."
                },
                {
                    "questionNumber": 11,
                    "question": "Quelle boisson appartient au premier groupe de la classification officielle française ?",
                    "answerOptions": [
                        {"text": "Les eaux minérales et les jus de fruits non fermentés", "isCorrect": True},
                        {"text": "Les vins doux naturels et les crèmes de cassis bénéficiant d'une appellation d'origine contrôlée et dont le titrage alcoométrique global dépasse les dix-huit degrés", "isCorrect": False},
                        {"text": "Les rhums ambrés agricoles vieillis en fût de chêne pendant plus de trois ans dans une distillerie des départements d'outre-mer", "isCorrect": False},
                        {"text": "Les bières artisanales de fermentation haute brassées localement avec ajout de liqueurs amères aromatiques destinées aux cocktails complexes", "isCorrect": False}
                    ],
                    "correction": "Le premier groupe comprend les boissons sans alcool : eaux minérales, jus de fruits, sirops, limonades, thés, cafés, etc. La vente de ces boissons ne nécessite pas de licence spécifique."
                },
                {
                    "questionNumber": 12,
                    "question": "Quelle obligation le gérant d'un bar a-t-il vis-à-vis d'un client consommant sur place ?",
                    "answerOptions": [
                        {"text": "Fournir de l'eau potable ordinaire gratuitement", "isCorrect": True},
                        {"text": "Proposer une alternative sans alcool à moitié prix", "isCorrect": False},
                        {"text": "Servir une carafe d'eau gazeuse avec des glaçons", "isCorrect": False},
                        {"text": "Offrir une collation salée pour toute boisson servie", "isCorrect": False}
                    ],
                    "correction": "La loi stipule que l'inclusion d'une carafe d'eau ordinaire, fraîche et potable est obligatoire et gratuite en accompagnement d'une consommation payante servie sur place."
                },
                {
                    "questionNumber": 13,
                    "question": "Quelle formation le futur gérant d'un débit de boissons doit-il obligatoirement suivre ?",
                    "answerOptions": [
                        {"text": "Le permis d'exploitation", "isCorrect": True},
                        {"text": "Le certificat de mixologie", "isCorrect": False},
                        {"text": "Le diplôme de sommelier", "isCorrect": False},
                        {"text": "La licence d'importateur", "isCorrect": False}
                    ],
                    "correction": "Le permis d'exploitation est une formation obligatoire de quelques jours pour toute personne déclarant l'ouverture, la mutation ou le transfert d'un débit de boissons. Il porte sur les droits et obligations en matière de santé publique."
                },
                {
                    "questionNumber": 14,
                    "question": "Que faire si un verre se brise au-dessus du bac à glaçons ?",
                    "answerOptions": [
                        {"text": "Jeter toute la glace", "isCorrect": True},
                        {"text": "Retirer les gros morceaux", "isCorrect": False},
                        {"text": "Rincer avec de l'eau", "isCorrect": False},
                        {"text": "Verser du sirop rouge", "isCorrect": False}
                    ],
                    "correction": "Le verre brisé est invisible dans la glace. Pour garantir la sécurité absolue des clients et éviter des blessures internes dramatiques, le barman doit vider complètement le bac, le nettoyer et le remplir avec de la glace neuve."
                },
                {
                    "questionNumber": 15,
                    "question": "En plonge manuelle de verrerie de bar, à quoi sert le passage dans le dernier bac ?",
                    "answerOptions": [
                        {"text": "À rincer les verres à l'eau claire et froide", "isCorrect": True},
                        {"text": "À désinfecter les coupes et les flûtes avec un puissant agent chimique chloré nécessitant un temps de contact ininterrompu de vingt minutes minimum avant le service", "isCorrect": False},
                        {"text": "À sécher instantanément la paroi des shakers et des verres à mélange grâce à l'injection d'un gaz carbonique liquide réfrigérant sous haute pression", "isCorrect": False},
                        {"text": "À polir mécaniquement le cristallin des timbales par un système de brosses rotatives immergées branchées sur le secteur électrique du comptoir", "isCorrect": False}
                    ],
                    "correction": "La plonge manuelle professionnelle s'effectue en trois bacs : le premier pour le lavage à l'eau chaude détergente, le second pour le rinçage, et le troisième à l'eau froide avec un agent de brillance pour refroidir le verre et faciliter l'égouttage sans trace."
                },
                {
                    "questionNumber": 16,
                    "question": "Que dit la réglementation sur l'usage de la cigarette électronique au bar ?",
                    "answerOptions": [
                        {"text": "Il est strictement interdit à l'intérieur de l'établissement", "isCorrect": True},
                        {"text": "Il est toléré uniquement au comptoir principal", "isCorrect": False},
                        {"text": "Il dépend du bon vouloir du responsable de salle", "isCorrect": False},
                        {"text": "Il est autorisé si le liquide est sans nicotine", "isCorrect": False}
                    ],
                    "correction": "Comme pour le tabac classique, le Code de la santé publique interdit l'usage des cigarettes électroniques dans les lieux à usage collectif fermés et couverts, y compris les cafés et les bars."
                },
                {
                    "questionNumber": 17,
                    "question": "Quel document obligatoire décrit les procédures d'hygiène des locaux du bar ?",
                    "answerOptions": [
                        {"text": "Le plan de nettoyage et de désinfection", "isCorrect": True},
                        {"text": "Le document unique des risques professionnels", "isCorrect": False},
                        {"text": "Le registre des déclarations d'accidents du travail", "isCorrect": False},
                        {"text": "Le manuel des recettes techniques des cocktails", "isCorrect": False}
                    ],
                    "correction": "Le PND (Plan de Nettoyage et de Désinfection) est un outil du paquet hygiène. Il précise pour chaque équipement et surface \"qui, quoi, quand et comment\" nettoyer avec quel produit et quel dosage."
                },
                {
                    "questionNumber": 18,
                    "question": "Comment doit-on stocker les agrumes tranchés destinés à la décoration des verres ?",
                    "answerOptions": [
                        {"text": "Dans un bac hermétique placé au frais", "isCorrect": True},
                        {"text": "Directement exposés sur une planche à découper en bois massif laissée sur le comptoir en plein soleil pour attirer le regard des clients curieux", "isCorrect": False},
                        {"text": "Entièrement immergés dans une bassine remplie de détergent chimique industriel afin de détruire toutes les bactéries avant l'intégration dans les boissons glacées", "isCorrect": False},
                        {"text": "Dans un grand bol en cuivre non protégé posé à même le sol derrière les congélateurs pour gagner de la place sur la station d'envoi des commandes", "isCorrect": False}
                    ],
                    "correction": "Les fruits coupés (la garniture ou garnish) sont des denrées très sensibles. Pour éviter l'oxydation, le dessèchement et la prolifération bactérienne, ils doivent être stockés dans des contenants propres et hermétiques au réfrigérateur."
                },
                {
                    "questionNumber": 19,
                    "question": "Quelle information visuelle concernant les femmes enceintes est obligatoire sur les bouteilles d'alcool ?",
                    "answerOptions": [
                        {"text": "Un pictogramme montrant une femme enceinte barrée", "isCorrect": True},
                        {"text": "Une vignette mentionnant le taux de sucre du produit", "isCorrect": False},
                        {"text": "Un logo coloré indiquant la présence de sulfites", "isCorrect": False},
                        {"text": "Un tableau des calories pour cent millilitres de liquide", "isCorrect": False}
                    ],
                    "correction": "Depuis 2007, toutes les bouteilles de boissons alcoolisées vendues en France doivent comporter un message sanitaire (texte ou pictogramme) préconisant la non-consommation d'alcool pendant la grossesse pour éviter le Syndrome d'Alcoolisation Fœtale."
                },
                {
                    "questionNumber": 20,
                    "question": "Quelle est l'obligation légale lors de la mise en place d'une opération promotionnelle sur l'alcool de type Happy Hour ?",
                    "answerOptions": [
                        {"text": "Proposer également des boissons non alcoolisées à un prix réduit", "isCorrect": True},
                        {"text": "Diffuser un message d'alerte sonore dans les haut-parleurs du bar de manière ininterrompue pendant toute la durée de la promotion commerciale sur la bière et les vins", "isCorrect": False},
                        {"text": "Demander une autorisation spéciale manuscrite et visée par le préfet de police au moins trente jours calendaires avant le début de l'opération tarifaire exceptionnelle", "isCorrect": False},
                        {"text": "Doubler systématiquement le volume des verres servis aux clients fidèles munis d'une carte membre sans modifier le tarif officiel affiché sur la carte des menus", "isCorrect": False}
                    ],
                    "correction": "La loi de modernisation de notre système de santé impose aux débits de boissons qui proposent des tarifs réduits sur l'alcool (Happy Hour) d'appliquer obligatoirement des réductions équivalentes sur l'offre de boissons sans alcool."
                }
            ]
        },
# =========================================================================
        # THÈME 2 : TECHNOLOGIE ET CONNAISSANCE DES BOISSONS (Questions 21 à 40)
        # =========================================================================
        2: {
            "name": "THÈME 2 : TECHNOLOGIE ET CONNAISSANCE DES BOISSONS",
            "questions": [
                {
                    "questionNumber": 21,
                    "question": "Quel champignon microscopique est indispensable pour transformer le sucre en alcool lors de la fermentation ?",
                    "answerOptions": [
                        {"text": "La levure", "isCorrect": True},
                        {"text": "La moisissure", "isCorrect": False},
                        {"text": "Le chloroplaste", "isCorrect": False},
                        {"text": "Le lactose", "isCorrect": False}
                    ],
                    "correction": "La fermentation alcoolique est le processus biochimique naturel par lequel des levures, de la famille des Saccharomyces, transforment les sucres d'un moût en éthanol et en gaz carbonique."
                },
                {
                    "questionNumber": 22,
                    "question": "Sur quel principe physique repose la séparation de l'alcool et de l'eau lors de la distillation ?",
                    "answerOptions": [
                        {"text": "L'alcool s'évapore à une température inférieure à celle de l'eau", "isCorrect": True},
                        {"text": "L'eau devient gazeuse beaucoup plus rapidement que l'éthanol", "isCorrect": False},
                        {"text": "Le sucre retient les molécules d'eau au fond de l'alambic en cuivre", "isCorrect": False},
                        {"text": "La pression atmosphérique écrase l'alcool au fond de la cuve", "isCorrect": False}
                    ],
                    "correction": "L'éthanol bout et s'évapore à 78,4 degrés Celsius, tandis que l'eau bout à 100 degrés Celsius. En chauffant le moût fermenté entre ces deux températures, on parvient à extraire et concentrer les vapeurs d'alcool pur."
                },
                {
                    "questionNumber": 23,
                    "question": "Quelle est l'une des différences majeures de production entre un Scotch Whisky et un Bourbon américain ?",
                    "answerOptions": [
                        {"text": "Le Bourbon est composé majoritairement de maïs et vieilli en fûts de chêne neufs", "isCorrect": True},
                        {"text": "Le Scotch Whisky subit une triple distillation systématique dans de grands alambics à colonne en acier inoxydable avant d'être aromatisé artificiellement avec des extraits de tourbe liquide importée de Scandinavie", "isCorrect": False},
                        {"text": "Le Bourbon ne nécessite aucun vieillissement en fût et peut être embouteillé directement à la sortie de l'alambic pour préserver la couleur naturellement transparente de la céréale cultivée localement", "isCorrect": False},
                        {"text": "Le Scotch Whisky est fermenté exclusivement à partir de seigle cru mélangé avec de l'eau de source pure chauffée à plus de quatre-vingt-dix degrés dans de grandes cuves en béton armé", "isCorrect": False}
                    ],
                    "correction": "La législation américaine exige qu'un Bourbon contienne au moins 51 pour cent de maïs et vieillisse dans des fûts de chêne neufs et brûlés. Le Scotch Single Malt est à base d'orge maltée et vieillit dans des fûts usagés en Écosse."
                },
                {
                    "questionNumber": 24,
                    "question": "Quelle baie aromatique est obligatoirement utilisée pour parfumer la base neutre du gin ?",
                    "answerOptions": [
                        {"text": "La baie de genièvre", "isCorrect": True},
                        {"text": "La graine de coriandre", "isCorrect": False},
                        {"text": "La gousse de vanille", "isCorrect": False},
                        {"text": "La fève de cacao", "isCorrect": False}
                    ],
                    "correction": "La législation européenne définit le gin comme une boisson spiritueuse aromatisée aux baies de genévrier. Bien que d'autres herbes botaniques soient couramment utilisées, le goût du genièvre doit rester prédominant."
                },
                {
                    "questionNumber": 25,
                    "question": "À partir de quelle matière première agricole élabore-t-on le rhum traditionnel industriel ?",
                    "answerOptions": [
                        {"text": "La mélasse de canne", "isCorrect": True},
                        {"text": "Le jus de betterave", "isCorrect": False},
                        {"text": "L'orge non maltée", "isCorrect": False},
                        {"text": "Le blé fermenté", "isCorrect": False}
                    ],
                    "correction": "Le rhum industriel, ou rhum traditionnel, est distillé à partir de la mélasse, un résidu épais et sirupeux issu du raffinage du sucre de canne. Le rhum agricole est quant à lui distillé à partir du pur jus de canne frais."
                },
                {
                    "questionNumber": 26,
                    "question": "Quel est le cépage blanc majoritairement cultivé pour produire le vin de base destiné au Cognac ?",
                    "answerOptions": [
                        {"text": "L'Ugni Blanc", "isCorrect": True},
                        {"text": "Le Chardonnay", "isCorrect": False},
                        {"text": "Le Sauvignon Blanc", "isCorrect": False},
                        {"text": "Le Gewurztraminer", "isCorrect": False}
                    ],
                    "correction": "L'Ugni Blanc représente plus de la quasi-totalité du vignoble de l'appellation Cognac. Il donne un vin acide et peu alcoolisé, des caractéristiques chimiques idéales pour réussir une double distillation en alambic charentais."
                },
                {
                    "questionNumber": 27,
                    "question": "Quelle condition botanique est strictement requise pour qu'un spiritueux obtienne l'appellation Tequila ?",
                    "answerOptions": [
                        {"text": "Il doit être produit à partir de la variété spécifique d'agave bleue", "isCorrect": True},
                        {"text": "Il doit être fermenté exclusivement en mélangeant des jus de cactus provenant de différentes régions désertiques situées au sud du Mexique pour garantir une complexité aromatique suffisante après la distillation", "isCorrect": False},
                        {"text": "Il doit inclure une proportion minimale de canne à sucre locale broyée à la main lors de la première étape d'extraction des sucs végétaux dans les fours en briques traditionnels de la distillerie", "isCorrect": False},
                        {"text": "Il doit vieillir pendant plus de quinze ans dans des cuves en acier enterrées sous le sable chaud du désert mexicain pour adoucir son goût piquant naturel avant la commercialisation", "isCorrect": False}
                    ],
                    "correction": "La vraie Tequila est élaborée au Mexique, dans l'état de Jalisco et quelques municipalités environnantes, à partir d'une seule variété végétale bien précise : l'agave bleue. Les autres spiritueux d'agave portent l'appellation Mezcal."
                },
                {
                    "questionNumber": 28,
                    "question": "Comment nomme-t-on le mélange de vin et de sucre ajouté au Champagne avant le bouchage définitif ?",
                    "answerOptions": [
                        {"text": "La liqueur d'expédition", "isCorrect": True},
                        {"text": "La liqueur de tirage", "isCorrect": False},
                        {"text": "Le moût de raisin", "isCorrect": False},
                        {"text": "Le vin de réserve", "isCorrect": False}
                    ],
                    "correction": "Après le dégorgement qui expulse le dépôt de levures, on ajoute la liqueur d'expédition pour combler le vide dans la bouteille. Sa teneur en sucre détermine le profil gustatif final du Champagne, du Brut Nature au Doux."
                },
                {
                    "questionNumber": 29,
                    "question": "Quelle grande famille de bières fermente à basse température avec une souche de levure spécifique ?",
                    "answerOptions": [
                        {"text": "Les Lagers", "isCorrect": True},
                        {"text": "Les Ales", "isCorrect": False},
                        {"text": "Les Lambics", "isCorrect": False},
                        {"text": "Les Stouts", "isCorrect": False}
                    ],
                    "correction": "Les bières de type Lager, comme la célèbre Pilsner, utilisent des levures spécifiques qui travaillent et fermentent entre sept et quinze degrés Celsius avant de s'accumuler au fond de la cuve lors de ce qu'on appelle la fermentation basse."
                },
                {
                    "questionNumber": 30,
                    "question": "Quelle variété de grain de café offre le profil aromatique le plus fin et complexe ?",
                    "answerOptions": [
                        {"text": "L'Arabica", "isCorrect": True},
                        {"text": "Le Robusta", "isCorrect": False},
                        {"text": "Le Liberica", "isCorrect": False},
                        {"text": "L'Excelsa", "isCorrect": False}
                    ],
                    "correction": "L'Arabica, cultivé en haute altitude, offre des arômes délicats, doux et parfumés avec une teneur plus faible en caféine. Le Robusta, cultivé en plaine, se révèle plus amer, plus corsé et nettement plus riche en caféine."
                },
                {
                    "questionNumber": 31,
                    "question": "Quel critère légal définit une liqueur par rapport à un simple spiritueux aromatisé ?",
                    "answerOptions": [
                        {"text": "Une teneur en sucre minimale de cent grammes par litre", "isCorrect": True},
                        {"text": "Une macération obligatoire de fruits frais accompagnée d'une triple distillation très lente dans un alambic traditionnel en cuivre chauffé au feu de bois de chêne massif", "isCorrect": False},
                        {"text": "Une durée de vieillissement réglementaire de trois ans minimum dans des fûts ayant préalablement contenu du vin muté afin d'apporter une onctuosité naturelle sans aucun ajout artificiel", "isCorrect": False},
                        {"text": "Un degré alcoolique obligatoirement supérieur à quarante-cinq degrés afin d'empêcher la cristallisation immédiate du sirop de glucose industriel ajouté lors de l'embouteillage final", "isCorrect": False}
                    ],
                    "correction": "Selon la législation européenne, une liqueur est une boisson spiritueuse ayant un titre alcoométrique minimal de quinze pour cent et contenant obligatoirement au moins cent grammes de sucre par litre de liquide."
                },
                {
                    "questionNumber": 32,
                    "question": "Lors de la vinification en rouge, comment appelle-t-on le processus donnant la couleur sombre au jus ?",
                    "answerOptions": [
                        {"text": "La macération", "isCorrect": True},
                        {"text": "Le pressurage", "isCorrect": False},
                        {"text": "Le collage", "isCorrect": False},
                        {"text": "Le soutirage", "isCorrect": False}
                    ],
                    "correction": "La macération permet au jus de raisin de rester en contact prolongé avec les peaux contenant les pigments colorants et les tanins de la grappe. C'est ce trempage naturel qui donne au vin rouge sa robe et sa structure."
                },
                {
                    "questionNumber": 33,
                    "question": "À partir de quelle base agricole la vodka polonaise ou russe est-elle historiquement élaborée ?",
                    "answerOptions": [
                        {"text": "Le seigle ou la pomme de terre", "isCorrect": True},
                        {"text": "L'orge maltée et germée", "isCorrect": False},
                        {"text": "Le pur jus de canne pressé", "isCorrect": False},
                        {"text": "Le maïs jaune concassé", "isCorrect": False}
                    ],
                    "correction": "Bien que la vodka moderne puisse être distillée à partir de blé ou de raisin, les recettes historiques d'Europe de l'Est privilégient l'utilisation du seigle pour sa douceur épicée, ou de la pomme de terre pour sa texture crémeuse."
                },
                {
                    "questionNumber": 34,
                    "question": "Quelle est la composition exacte d'un Vermouth classiquement utilisé en mixologie ?",
                    "answerOptions": [
                        {"text": "Un vin fortifié et aromatisé avec des plantes et des épices dont obligatoirement de l'armoise", "isCorrect": True},
                        {"text": "Un spiritueux à base de céréales infusé avec des écorces d'oranges amères provenant exclusivement du sud de l'Espagne et de l'Italie du sud pour garantir un profil fruité", "isCorrect": False},
                        {"text": "Un mélange complexe de jus de raisin non fermenté et d'eau de vie de fruit blanc vieillissant dans des dames jeannes exposées en plein soleil pendant plusieurs longues années", "isCorrect": False},
                        {"text": "Une bière artisanale distillée deux fois puis adoucie avec du miel de fleurs sauvages et de la cannelle infusée à froid pour réduire drastiquement son amertume naturelle", "isCorrect": False}
                    ],
                    "correction": "Le Vermouth est un vin fortifié par adjonction d'alcool et aromatisé par macération. La loi exige que son profil aromatique inclue des plantes de la famille des Artemisia, à savoir l'armoise, qui lui confèrent sa fine amertume."
                },
                {
                    "questionNumber": 35,
                    "question": "Quelle catégorie générique de boissons englobe le Campari ou encore l'Aperol ?",
                    "answerOptions": [
                        {"text": "Les amers", "isCorrect": True},
                        {"text": "Les anisés", "isCorrect": False},
                        {"text": "Les mistelles", "isCorrect": False},
                        {"text": "Les eaux de vie", "isCorrect": False}
                    ],
                    "correction": "Le Campari et l'Aperol sont des amers, souvent appelés bitters italiens. Ce sont des liqueurs amères et colorées obtenues par l'infusion minutieuse d'herbes, de racines de plantes, de fruits et d'écorces dans de l'alcool."
                },
                {
                    "questionNumber": 36,
                    "question": "Quel pays est reconnu comme le grand berceau historique de la culture du thé ?",
                    "answerOptions": [
                        {"text": "La Chine", "isCorrect": True},
                        {"text": "L'Inde", "isCorrect": False},
                        {"text": "Le Kenya", "isCorrect": False},
                        {"text": "Le Japon", "isCorrect": False}
                    ],
                    "correction": "Le thénier, scientifiquement nommé Camellia sinensis, est originaire du sud-ouest de la Chine. L'usage du thé y a débuté comme remède médicinal avant de devenir une boisson d'agrément populaire mondiale."
                },
                {
                    "questionNumber": 37,
                    "question": "Que signifie légalement la mention VSOP affichée sur une bouteille de Calvados ?",
                    "answerOptions": [
                        {"text": "Le plus jeune spiritueux de l'assemblage a vieilli au moins quatre ans dans un fût en bois", "isCorrect": True},
                        {"text": "Le maître de chai garantit que la boisson a été filtrée à très basse température pour éliminer les impuretés avant d'être mise en bouteille dans la région d'origine contrôlée", "isCorrect": False},
                        {"text": "L'assemblage est constitué uniquement de distillats provenant des vendanges de l'année précédente et n'ayant subi aucun ajout de colorant artificiel ou de caramel fondu", "isCorrect": False},
                        {"text": "Le produit a vieilli pendant une décennie complète dans des fûts neufs afin de développer de puissants arômes de vanille et de fruits rouges confits au soleil normand", "isCorrect": False}
                    ],
                    "correction": "L'abréviation classique VSOP signifie Very Superior Old Pale. Elle indique l'âge certifié de l'eau-de-vie la plus jeune entrant dans l'assemblage final du maître de chai. Pour le Calvados et le Cognac, cet âge est de quatre ans minimum."
                },
                {
                    "questionNumber": 38,
                    "question": "Qu'est-ce qui différencie fondamentalement une eau minérale naturelle d'une eau de source ?",
                    "answerOptions": [
                        {"text": "La stabilité garantie de sa composition chimique et minérale", "isCorrect": True},
                        {"text": "L'absence totale de gaz carbonique ajouté industriellement", "isCorrect": False},
                        {"text": "Son conditionnement rendu obligatoire dans des bouteilles en verre", "isCorrect": False},
                        {"text": "Sa température de captage profond obligatoirement supérieure à trente degrés", "isCorrect": False}
                    ],
                    "correction": "Une eau minérale naturelle doit posséder de par la loi une composition minérale parfaitement constante et stable dans le temps, contrairement à l'eau de source dont la minéralité et les éléments dissous peuvent fluctuer."
                },
                {
                    "questionNumber": 39,
                    "question": "Quelle plante singulière apporte principalement le goût aromatique de réglisse dans un Pastis de Marseille ?",
                    "answerOptions": [
                        {"text": "La racine de réglisse", "isCorrect": True},
                        {"text": "La menthe poivrée", "isCorrect": False},
                        {"text": "La graine de fenouil", "isCorrect": False},
                        {"text": "Le clou de girofle", "isCorrect": False}
                    ],
                    "correction": "Outre l'anis étoilé qui constitue l'arôme de base, le vrai Pastis de Marseille contient obligatoirement des extraits de racines de bois de réglisse. Cet ingrédient essentiel lui apporte sa rondeur suave et sa coloration jaune légèrement ambrée."
                },
                {
                    "questionNumber": 40,
                    "question": "Quelle technique ancestrale permet d'élaborer du véritable vin de Porto traditionnel ?",
                    "answerOptions": [
                        {"text": "L'ajout d'eau de vie de raisin pendant la fermentation pour conserver la sucrosité", "isCorrect": True},
                        {"text": "La cuisson lente du moût de raisin dans de grandes cuves en cuivre pour évaporer l'eau et concentrer naturellement les sucs avant le tout début de la fermentation alcoolique", "isCorrect": False},
                        {"text": "Le mélange de vin blanc très sec avec un sirop de caramel épais produit localement afin de lui donner sa fameuse couleur rubis sombre et son puissant goût liquoreux", "isCorrect": False},
                        {"text": "Le vieillissement exclusif du vin rouge dans des fûts de bois immergés dans l'océan atlantique pendant deux ans afin de stabiliser la structure moléculaire complexe des tanins", "isCorrect": False}
                    ],
                    "correction": "Le Porto est un grand vin muté. Le mutage est une technique consistant à stopper net la fermentation alcoolique du moût en y versant de l'eau-de-vie vinique pure. Cette opération tue les levures et préserve l'incroyable douceur naturelle du raisin."
                }
            ]
        },
        # =========================================================================
        # THÈME 3 : MIXOLOGIE, TECHNIQUES DE BAR ET RECETTES CLASSIQUES (Questions 41 à 60)
        # =========================================================================
        3: {
            "name": "THÈME 3 : MIXOLOGIE, TECHNIQUES DE BAR ET RECETTES CLASSIQUES",
            "questions": [
                {
                    "questionNumber": 41,
                    "question": "Quel matériel de bar sert à refroidir et mélanger vigoureusement des ingrédients opaques ou très denses ?",
                    "answerOptions": [
                        {"text": "Le shaker", "isCorrect": True},
                        {"text": "Le verre à mélange", "isCorrect": False},
                        {"text": "La cuillère à mélange", "isCorrect": False},
                        {"text": "Le pilon plat", "isCorrect": False}
                    ],
                    "correction": "Le shaker est l'outil indispensable pour frapper les cocktails contenant des jus de fruits frais, du lait, de la crème, des œufs ou des sirops épais. Son mouvement crée une émulsion parfaite et un refroidissement optimal."
                },
                {
                    "questionNumber": 42,
                    "question": "Dans quelle situation précise le barman privilégie-t-il l'utilisation du verre à mélange ?",
                    "answerOptions": [
                        {"text": "Pour rafraîchir des liquides fluides et clairs sans troubler leur limpidité", "isCorrect": True},
                        {"text": "Pour écraser des feuilles de menthe fraîche avec de la cassonade en poudre", "isCorrect": False},
                        {"text": "Pour créer une épaisse couche de mousse crémeuse en intégrant un blanc d'œuf pur", "isCorrect": False},
                        {"text": "Pour mélanger extrêmement rapidement de la crème fraîche épaisse et une liqueur sirupeuse", "isCorrect": False}
                    ],
                    "correction": "Le verre à mélange, couplé à une longue cuillère, est employé pour marier et refroidir délicatement les cocktails composés uniquement de spiritueux et de vermouths afin de ne pas émulsionner ni casser la belle transparence du produit."
                },
                {
                    "questionNumber": 43,
                    "question": "Quel rôle crucial joue la glace en fondant doucement lors de la préparation d'un cocktail alcoolisé ?",
                    "answerOptions": [
                        {"text": "Elle apporte la dilution en eau nécessaire pour équilibrer la puissance de l'alcool pur", "isCorrect": True},
                        {"text": "Elle empêche complètement les arômes volatils des liqueurs de s'échapper du verre grâce à une barrière thermique très puissante bloquant l'évaporation naturelle à la surface", "isCorrect": False},
                        {"text": "Elle modifie chimiquement le pH global du jus de citron jaune pour le rendre beaucoup plus doux et agréable en bouche lors de la dégustation finale par le client au comptoir", "isCorrect": False},
                        {"text": "Elle augmente fortement le volume global de la boisson dans le verre pour donner l'impression illusoire au client qu'il a été servi de manière particulièrement généreuse", "isCorrect": False}
                    ],
                    "correction": "La dilution apportée par la glace est l'un des paramètres les plus vitaux de la mixologie. Cette eau de fonte fait chuter la température de service et adoucit la brûlure de l'éthanol en liant magnifiquement les arômes des différents alcools."
                },
                {
                    "questionNumber": 44,
                    "question": "Quelle est la recette classique officielle du cocktail Mojito selon le référentiel de l'IBA ?",
                    "answerOptions": [
                        {"text": "Rhum blanc, citron vert frais, sucre blanc, menthe et un trait d'eau gazeuse", "isCorrect": True},
                        {"text": "Rhum ambré, jus de citron jaune pressé, sirop de canne et de la limonade douce", "isCorrect": False},
                        {"text": "Tequila blanche pure, nectar d'agave, citron vert et quelques feuilles de basilic", "isCorrect": False},
                        {"text": "Cachaça brésilienne, sucre roux non raffiné, morceaux de citron vert écrasés et eau plate", "isCorrect": False}
                    ],
                    "correction": "Le Mojito est un fabuleux Long drink d'origine cubaine. La véritable recette de l'International Bartenders Association exige du rhum blanc de type cubain, du jus de citron vert fraîchement pressé, de la menthe, du sucre et du soda water."
                },
                {
                    "questionNumber": 45,
                    "question": "Quel appareil électrique motorisé utilise-t-on pour réaliser un cocktail Frozen avec de la glace pilée ?",
                    "answerOptions": [
                        {"text": "Le blender", "isCorrect": True},
                        {"text": "Le presse-agrumes", "isCorrect": False},
                        {"text": "L'extracteur de jus", "isCorrect": False},
                        {"text": "L'émulsionneur à lait", "isCorrect": False}
                    ],
                    "correction": "Le blender est un mixeur puissant équipé de lames solides qui broient violemment les glaçons ou la glace pilée en une fine neige homogène. Il permet d'obtenir la texture givrée et granitée très rafraîchissante des cocktails type Frozen Daiquiri."
                },
                {
                    "questionNumber": 46,
                    "question": "À quoi sert le pilon dans l'équipement de base du barman professionnel ?",
                    "answerOptions": [
                        {"text": "Écraser des fruits ou des herbes aromatiques au fond du verre pour en extraire le goût", "isCorrect": True},
                        {"text": "Mesurer et verser des doses très précises de spiritueux fins et coûteux dans le shaker", "isCorrect": False},
                        {"text": "Filtrer manuellement les résidus de glace fondue lors du service direct au comptoir", "isCorrect": False},
                        {"text": "Verser un soda gazeux le long de la paroi interne pour ne pas briser la délicate bulle", "isCorrect": False}
                    ],
                    "correction": "Le pilon s'utilise directement dans le verre de service ou au fond de la timbale métallique du shaker. Sa base crantée ou plate permet de presser des quartiers de citron vert, de piler du sucre en poudre et d'exprimer les précieuses huiles des herbes."
                },
                {
                    "questionNumber": 47,
                    "question": "Quelle est l'utilité première du doseur de bar également appelé jigger sur la station de travail ?",
                    "answerOptions": [
                        {"text": "Mesurer des volumes liquides rigoureux pour garantir l'équilibre et la constance du cocktail", "isCorrect": True},
                        {"text": "Secouer vigoureusement les préparations contenant beaucoup de pulpe de fruits frais afin d'obtenir un mélange parfaitement homogène et extrêmement froid en seulement quelques secondes", "isCorrect": False},
                        {"text": "Récupérer délicatement les pépins de citron et les brisures de glace pilée pour ne surtout pas boucher la paille fournie au client au moment précis du service de la commande", "isCorrect": False},
                        {"text": "Créer de fantastiques dégradés de couleurs esthétiques en ralentissant considérablement le flux d'écoulement des sirops très sucrés et très denses à l'intérieur de la coupe à cocktail", "isCorrect": False}
                    ],
                    "correction": "Le jigger est un petit instrument de mesure bipolaire, souvent calibré en deux et quatre centilitres. Il est la clef de voûte du barman pour assurer le parfait équilibre gustatif, la rentabilité financière des bouteilles et la fidélisation gustative du client."
                },
                {
                    "questionNumber": 48,
                    "question": "Quels sont les ingrédients de base de l'incontournable et iconique cocktail Old Fashioned ?",
                    "answerOptions": [
                        {"text": "Bourbon ou Rye whiskey, morceau de sucre, angostura bitters aromatique et un zeste", "isCorrect": True},
                        {"text": "Cognac de qualité, sirop de sucre de canne liquide, liqueur d'orange douce et jus de citron", "isCorrect": False},
                        {"text": "Gin london dry épicé, vermouth rouge italien, liqueur campari amère et une simple olive", "isCorrect": False},
                        {"text": "Vodka russe classique, liqueur de café torréfié, crème liquide épaisse et fine noix de muscade", "isCorrect": False}
                    ],
                    "correction": "L'Old Fashioned est l'un des pionniers de la mixologie. Préparé directement dans un petit verre à fond plat, on y dissout patiemment un sucre imprégné de bitters, avant d'ajouter progressivement de la glace cube et un robuste whiskey américain."
                },
                {
                    "questionNumber": 49,
                    "question": "Quel outil filtrant s'insère parfaitement sur la timbale d'un shaker Boston pour retenir les glaçons usagés ?",
                    "answerOptions": [
                        {"text": "La passoire à ressort", "isCorrect": True},
                        {"text": "La cuillère à long manche", "isCorrect": False},
                        {"text": "Le bec verseur métallique", "isCorrect": False},
                        {"text": "Le zesteur de fruits fins", "isCorrect": False}
                    ],
                    "correction": "La passoire de type Hawthorne, reconnaissable à son ressort souple en spirale, vient chapeauter et s'emboîter sur le haut du shaker. Elle filtre avec une grande efficacité la glace et les résidus solides au moment crucial de verser le liquide embelli."
                },
                {
                    "questionNumber": 50,
                    "question": "Quelle technique de bar permet de réaliser un splendide cocktail à étages multicolores ?",
                    "answerOptions": [
                        {"text": "Verser délicatement les liquides sur le dos de la cuillère en respectant scrupuleusement l'ordre décroissant de leur densité spécifique liée au sucre", "isCorrect": True},
                        {"text": "Congeler chaque couche liquide indépendamment dans un congélateur à très basse température avant d'ajouter le spiritueux suivant par-dessus de manière très brutale pour créer un choc thermique", "isCorrect": False},
                        {"text": "Agiter vigoureusement le shaker de façon circulaire continue pour que la force centrifuge naturelle sépare automatiquement les liquides lourds des liquides légers juste avant le service", "isCorrect": False},
                        {"text": "Ajouter d'énormes quantités de glace pilée totalement sèche entre chaque versement de liquide chaud afin d'emprisonner définitivement la couleur des différents ingrédients au fond du verre", "isCorrect": False}
                    ],
                    "correction": "La technique visuelle du Float (ou stratification) repose sur la gravité et le poids du sucre. Les sirops lourds plongent au fond. Le barman verse ensuite les liquides de plus en plus légers, en s'aidant du dos arrondi de sa cuillère pour freiner brutalement l'impact."
                },
                {
                    "questionNumber": 51,
                    "question": "Que signifie très exactement réaliser un Dry Shake lors de l'élaboration d'un cocktail complexe ?",
                    "answerOptions": [
                        {"text": "Une première agitation très énergique des ingrédients liquides dans la timbale sans aucune glace", "isCorrect": True},
                        {"text": "Une méthode de rafraîchissement exclusivement réservée à la manipulation d'alcools de type london dry", "isCorrect": False},
                        {"text": "Un mélange aromatique réalisé uniquement à l'aide de composants en poudre ou de fleurs séchées", "isCorrect": False},
                        {"text": "Le fait impératif de secouer un shaker qui vient tout juste d'être essuyé minutieusement avec un linge", "isCorrect": False}
                    ],
                    "correction": "Secouer à sec, ou Dry Shake, est une première passe vigoureuse sans glaçon. C'est le secret technique pour émulsionner efficacement et créer une magnifique texture moussante onctueuse lors de l'utilisation de blanc d'œuf frais ou d'aquafaba."
                },
                {
                    "questionNumber": 52,
                    "question": "Quel est le profil gustatif classique et la décoration indissociable du fameux cocktail Margarita ?",
                    "answerOptions": [
                        {"text": "Une saveur puissante et acidulée à base de Tequila avec un verre bordé d'un givrage de sel fin", "isCorrect": True},
                        {"text": "Une saveur extrêmement amère à base de Gin botanique servie avec un long zeste de citron jaune", "isCorrect": False},
                        {"text": "Une saveur très douce et sucrée à base de vieux Rhum décorée avec une épaisse tranche d'ananas", "isCorrect": False},
                        {"text": "Une saveur étonnante et umami à base de Vodka pure avec un givrage intégral au poivre noir moulu", "isCorrect": False}
                    ],
                    "correction": "La Margarita rassemble la chaleur de la Tequila, la sucrosité de l'orange du triple sec et l'acidité tranchante du citron vert frais. Le givrage de sel disposé sur le rebord extérieur du verre agit comme un exhausteur de goût naturel."
                },
                {
                    "questionNumber": 53,
                    "question": "Quel volume total de liquide correspond aux boissons regroupées dans la catégorie des Long Drinks ?",
                    "answerOptions": [
                        {"text": "Douze centilitres ou plus", "isCorrect": True},
                        {"text": "Moins de sept centilitres", "isCorrect": False},
                        {"text": "Exactement cinq centilitres", "isCorrect": False},
                        {"text": "Un demi-litre imposé minimum", "isCorrect": False}
                    ],
                    "correction": "Les Long Drinks sont des boissons rafraîchissantes et allongées à l'aide d'un grand volume de soda, de jus de fruit ou d'eau gazeuse. Leur contenance finale s'étend de douze à près de vingt-cinq centilitres, servis dans un grand verre tumbler."
                },
                {
                    "questionNumber": 54,
                    "question": "Quels sont les quatre ingrédients entrant dans la composition mondialement connue du Cosmopolitan ?",
                    "answerOptions": [
                        {"text": "De la vodka parfumée au citron, de la liqueur d'orange douce, un trait de jus de canneberge et du jus de citron vert", "isCorrect": True},
                        {"text": "Du gin sec londonien, une généreuse purée de framboise fraîche, un fond de sirop de vanille et un gros trait d'eau gazeuse très pétillante", "isCorrect": False},
                        {"text": "Du rhum blanc agricole, un beau volume de jus d'ananas pressé, de la crème de coco onctueuse et une simple petite touche de sirop de grenadine", "isCorrect": False},
                        {"text": "Du whisky écossais fort et tourbé, un bon volume de vermouth blanc sec, un trait de liqueur de cerise et de nombreuses gouttes d'amer aromatique", "isCorrect": False}
                    ],
                    "correction": "Le Cosmopolitan est une icône de la pop culture des années quatre-vingt-dix. Il s'élabore au shaker. Sa superbe teinte rose translucide est apportée exclusivement par la belle acidité naturelle du jus de canneberge (cranberry)."
                },
                {
                    "questionNumber": 55,
                    "question": "Que signifie techniquement l'indication de préparation au Build in glass sur une fiche recette de bar ?",
                    "answerOptions": [
                        {"text": "Les différents ingrédients liquides sont versés un à un directement dans le verre de service garni de glace", "isCorrect": True},
                        {"text": "Le cocktail complexe doit obligatoirement être préparé au blender avant d'être transvasé au comptoir", "isCorrect": False},
                        {"text": "Le professionnel doit chauffer le fond du récipient en verre au chalumeau avant d'y verser l'alcool sec", "isCorrect": False},
                        {"text": "Le barman est tenu de monter une spectaculaire tour de coupes sur son comptoir avant l'arrivée du client", "isCorrect": False}
                    ],
                    "correction": "Préparer un cocktail directement dans le verre (build) consiste à déposer les glaçons, l'alcool et enfin le liquide d'allongement sans passer par la case shaker ou verre à mélange. C'est la méthode de base du célèbre Cuba Libre ou du Gin Tonic."
                },
                {
                    "questionNumber": 56,
                    "question": "Quel est l'objectif purement aromatique lorsqu'un barman twiste vigoureusement un zeste d'agrume au-dessus d'une boisson ?",
                    "answerOptions": [
                        {"text": "Projeter et libérer un nuage d'huiles essentielles odorantes sur toute la surface de la boisson glacée", "isCorrect": True},
                        {"text": "Ajouter de façon volontaire une énorme dose d'amertume astringente au fond du verre à dégustation", "isCorrect": False},
                        {"text": "Réduire chimiquement le taux d'alcoolémie de la préparation servie au client avant sa première consommation", "isCorrect": False},
                        {"text": "Changer miraculeusement la couleur du liquide par le principe de l'oxydation rapide de l'écorce à l'air libre", "isCorrect": False}
                    ],
                    "correction": "L'écorce externe des agrumes comme l'orange ou le citron regorge de petites poches d'huiles essentielles. En pliant fermement le zeste, le barman pulvérise ces micro-gouttelettes très parfumées qui viendront flatter le nez du consommateur."
                },
                {
                    "questionNumber": 57,
                    "question": "Quelle affirmation décrit scrupuleusement la constitution du merveilleux cocktail classique italien Negroni ?",
                    "answerOptions": [
                        {"text": "C'est un assemblage à parfaites parts égales de Gin, de Campari et de Vermouth rouge préparé doucement au verre à mélange", "isCorrect": True},
                        {"text": "C'est une boisson onctueuse et très douce à base de liqueur d'amande mélangée avec du lait froid et de la crème de cacao liquide", "isCorrect": False},
                        {"text": "C'est un grand classique festif estival préparé longuement au blender avec une impressionnante quantité de fraises fraîches et de sucre", "isCorrect": False},
                        {"text": "C'est un puissant cocktail chaud servi dans une tasse en verre résistant et préparé exclusivement avec du café noir intense et du whisky d'Irlande", "isCorrect": False}
                    ],
                    "correction": "Créé vers l'année mil neuf cent dix-neuf à Florence en Italie, le Negroni applique la formidable règle des trois tiers. Composé de Gin, d'amer de type Campari et de Vermouth rouge doux, il offre une dégustation équilibrée sur l'amertume et les épices."
                },
                {
                    "questionNumber": 58,
                    "question": "Quelle est la principale fonction requise pour qu'une décoration d'agrume ou d'herbe soit parfaitement réussie sur un cocktail ?",
                    "answerOptions": [
                        {"text": "Sublimer visuellement le verre tout en faisant un écho gustatif très cohérent aux ingrédients internes", "isCorrect": True},
                        {"text": "Nourrir copieusement le client s'il a faim avant le repas principal servi par la brigade du restaurant", "isCorrect": False},
                        {"text": "Dissimuler les éventuels défauts visuels ou les grumeaux d'un mélange imparfaitement filtré par le commis", "isCorrect": False},
                        {"text": "Augmenter artificiellement le tarif de vente final de la boisson en ajoutant un fruit particulièrement onéreux", "isCorrect": False}
                    ],
                    "correction": "La garnish (la garniture de verre) doit impérativement être propre et comestible. Au-delà de l'indéniable touche visuelle et esthétique, elle a le devoir de parfumer le verre et de rappeler subtilement ce que le buveur s'apprête à déguster."
                },
                {
                    "questionNumber": 59,
                    "question": "Dans les fiches de mixologie anglo-saxonnes, que représente exactement la mesure appelée dash ?",
                    "answerOptions": [
                        {"text": "Une infime quantité de liquide obtenue en secouant une fois une bouteille spécifique munie d'un bouchon compte-gouttes", "isCorrect": True},
                        {"text": "Le volume d'alcool exact contenu dans la partie supérieure et la plus évasée d'un doseur métallique standard européen", "isCorrect": False},
                        {"text": "La quantité de glace solide concassée juste nécessaire pour remplir intégralement la cavité d'un élégant verre de taille moyenne", "isCorrect": False},
                        {"text": "Le poids précis en grammes du sucre raffiné ajouté dans la préparation shaker afin de corriger brutalement l'acidité de l'agrume", "isCorrect": False}
                    ],
                    "correction": "Le terme anglais dash se traduit en français par un trait. C'est l'unité infime utilisée pour distiller prudemment des amers concentrés, comme l'Angostura, qui modifient puissamment le goût d'un verre avec seulement deux ou trois gouttes."
                },
                {
                    "questionNumber": 60,
                    "question": "Dans quel fascinant récipient métallique sert-on de manière traditionnelle et historique le Moscow Mule ?",
                    "answerOptions": [
                        {"text": "Une tasse en cuivre", "isCorrect": True},
                        {"text": "Une flûte en fin cristal", "isCorrect": False},
                        {"text": "Une chope en céramique", "isCorrect": False},
                        {"text": "Une coupe en argent massif", "isCorrect": False}
                    ],
                    "correction": "Le légendaire Moscow Mule associe merveilleusement la vodka, un demi jus de citron vert et de la bière de gingembre. Servi sur beaucoup de glace dans une typique tasse en cuivre, le métal s'embue et garantit aux lèvres une fraîcheur intense."
                }
            ]
        },
# =========================================================================
        # THÈME 4 : ÉQUIPEMENT, AMÉNAGEMENT ET GESTION DU BAR (Questions 61 à 80)
        # =========================================================================
        4: {
            "name": "THÈME 4 : ÉQUIPEMENT, AMÉNAGEMENT ET GESTION DU BAR",
            "questions": [
                {
                    "questionNumber": 61,
                    "question": "Quel outil permet d'extraire rapidement le jus des citrons verts au comptoir ?",
                    "answerOptions": [
                        {"text": "Le presse-agrumes manuel", "isCorrect": True},
                        {"text": "Le pilon en bois", "isCorrect": False},
                        {"text": "La cuillère à mélange", "isCorrect": False},
                        {"text": "Le couteau d'office", "isCorrect": False}
                    ],
                    "correction": "Le presse-agrumes manuel (souvent appelé presse-citron mexicain) permet au barman d'extraire minute un jus frais sans amertume, indispensable pour l'équilibre des cocktails acidulés."
                },
                {
                    "questionNumber": 62,
                    "question": "Comment s'appelle la gouttière de rangement rapide des bouteilles les plus utilisées ?",
                    "answerOptions": [
                        {"text": "Le speed rack", "isCorrect": True},
                        {"text": "Le back bar", "isCorrect": False},
                        {"text": "Le verre à mélange", "isCorrect": False},
                        {"text": "La station de plonge", "isCorrect": False}
                    ],
                    "correction": "Le speed rack (ou rack de vitesse) est positionné à hauteur de taille. Il abrite les alcools génériques (les verse) pour que le barman puisse les attraper à l'aveugle et enchaîner les préparations très rapidement."
                },
                {
                    "questionNumber": 63,
                    "question": "À quoi sert principalement la fiche technique de fabrication d'un cocktail ?",
                    "answerOptions": [
                        {"text": "Standardiser la recette pour garantir la qualité au client et calculer très précisément le coût de revient des ingrédients", "isCorrect": True},
                        {"text": "Décorer le menu remis aux clients en salle afin de justifier le prix de vente souvent très élevé des créations originales", "isCorrect": False},
                        {"text": "Autoriser légalement le barman à modifier les dosages de l'alcool fort en fonction de l'état de fatigue ou de l'âge de l'acheteur", "isCorrect": False},
                        {"text": "Fournir une preuve officielle à l'inspection du travail en cas de blessure grave survenue lors de l'utilisation intensive du blender électrique", "isCorrect": False}
                    ],
                    "correction": "La fiche technique est le document de référence du bar. Elle détaille les ingrédients, la verrerie et les quantités exactes pour que le cocktail soit identique peu importe qui le prépare, tout en figeant le coût matière."
                },
                {
                    "questionNumber": 64,
                    "question": "Quel est l'intérêt de réaliser un inventaire physique régulier au bar ?",
                    "answerOptions": [
                        {"text": "Contrôler les écarts entre les ventes théoriques et le stock réel", "isCorrect": True},
                        {"text": "Nettoyer les étagères de rangement de la réserve", "isCorrect": False},
                        {"text": "Modifier le prix de vente de toutes les bouteilles", "isCorrect": False},
                        {"text": "Changer l'agencement visuel des alcools sur les étagères", "isCorrect": False}
                    ],
                    "correction": "L'inventaire, souvent réalisé mensuellement, permet de pointer les références pour repérer les surdosages, les pertes, les vols ou les produits périmés, en comparant ce qui a été vendu avec ce qui a disparu du stock."
                },
                {
                    "questionNumber": 65,
                    "question": "Comment s'appelle la longue cuillère torsadée du barman ?",
                    "answerOptions": [
                        {"text": "La barspoon", "isCorrect": True},
                        {"text": "Le muddler", "isCorrect": False},
                        {"text": "Le jigger", "isCorrect": False},
                        {"text": "Le strainer", "isCorrect": False}
                    ],
                    "correction": "La barspoon (cuillère de bar) a un long manche torsadé qui permet de tourner facilement le long de la paroi du verre à mélange sans casser la glace, pour rafraîchir la boisson en douceur."
                },
                {
                    "questionNumber": 66,
                    "question": "Que représente le coût matière d'une boisson dans la gestion financière ?",
                    "answerOptions": [
                        {"text": "Le prix d'achat hors taxes des ingrédients composant la recette", "isCorrect": True},
                        {"text": "Le tarif TTC facturé au client lors de sa commande", "isCorrect": False},
                        {"text": "Le temps de travail nécessaire pour réaliser le cocktail", "isCorrect": False},
                        {"text": "Les frais de verrerie et de décoration en salle", "isCorrect": False}
                    ],
                    "correction": "Le coût matière (ou food cost) représente la valeur d'achat hors taxes des liquides, de la glace et de la décoration utilisés pour un verre. Il permet au gérant de calculer sa marge brute et de fixer le prix final."
                },
                {
                    "questionNumber": 67,
                    "question": "Quel est l'objectif premier d'un bon aménagement de la station de travail du barman ?",
                    "answerOptions": [
                        {"text": "Limiter au maximum les déplacements inutiles lors du service pour gagner un temps précieux et réduire la fatigue physique", "isCorrect": True},
                        {"text": "Exposer obligatoirement la totalité des références de bouteilles disponibles en réserve pour impressionner les touristes", "isCorrect": False},
                        {"text": "Cacher totalement les équipements de plonge et les poubelles sous de lourds panneaux en bois massif afin de ne jamais gêner la vue", "isCorrect": False},
                        {"text": "Isoler le poste de création des cocktails à l'intérieur d'une pièce fermée pour empêcher les clients de copier les recettes secrètes", "isCorrect": False}
                    ],
                    "correction": "L'ergonomie est vitale derrière le comptoir. Tout doit être à portée de bras (glace, verrerie, speed rack, garnitures). Un barman ne doit idéalement faire qu'un pas ou deux pour envoyer n'importe quelle commande."
                },
                {
                    "questionNumber": 68,
                    "question": "Comment calcule-t-on le ratio matière d'une boisson sur la carte ?",
                    "answerOptions": [
                        {"text": "Coût matière divisé par le prix de vente hors taxes", "isCorrect": True},
                        {"text": "Prix de vente TTC multiplié par la quantité servie", "isCorrect": False},
                        {"text": "Coût d'achat additionné aux frais de personnel", "isCorrect": False},
                        {"text": "Prix de vente divisé par le coût d'achat hors taxes", "isCorrect": False}
                    ],
                    "correction": "Le ratio matière est le pourcentage que représente l'achat des produits par rapport au prix de vente (hors taxes). Un ratio standard pour un cocktail en établissement classique se situe souvent entre quinze et vingt pour cent."
                },
                {
                    "questionNumber": 69,
                    "question": "Quel équipement de bar stocke les vins blancs au frais ?",
                    "answerOptions": [
                        {"text": "L'arrière-bar réfrigéré", "isCorrect": True},
                        {"text": "La machine à glaçons", "isCorrect": False},
                        {"text": "Le bac de la plonge", "isCorrect": False},
                        {"text": "L'étagère du speed rack", "isCorrect": False}
                    ],
                    "correction": "L'arrière-bar vitré (ou meuble froid de back bar) maintient les vins blancs, bières, champagnes et jus de fruits à parfaite température de service, tout en les exposant souvent à la vue de la clientèle."
                },
                {
                    "questionNumber": 70,
                    "question": "Pourquoi faut-il fermer correctement les bouteilles de sirops avec un bouchon ou capuchon le soir ?",
                    "answerOptions": [
                        {"text": "Éviter l'évaporation de l'alcool et l'intrusion d'insectes attirés par les résidus de sucre sur les goulots", "isCorrect": True},
                        {"text": "Empêcher la cristallisation immédiate des sirops sous l'effet de la baisse des températures nocturnes dans le local", "isCorrect": False},
                        {"text": "Permettre une réaction chimique d'oxydation bénéfique qui va considérablement améliorer le profil aromatique du liquide", "isCorrect": False},
                        {"text": "Stopper définitivement le processus de vieillissement naturel des eaux de vie de fruits contenues dans la bouteille", "isCorrect": False}
                    ],
                    "correction": "Laisser les becs verseurs métalliques ouverts à l'air libre favorise l'évaporation (la perte de degrés) et attire immanquablement les moucherons (les mouches du vinaigre) avides de sucre en fin de journée."
                },
                {
                    "questionNumber": 71,
                    "question": "Quelle verrerie est idéale pour le service pur d'un spiritueux fin sans glace ?",
                    "answerOptions": [
                        {"text": "Le verre tulipe à dégustation", "isCorrect": True},
                        {"text": "Le grand tumbler", "isCorrect": False},
                        {"text": "La coupe à cocktail", "isCorrect": False},
                        {"text": "Le verre à shot", "isCorrect": False}
                    ],
                    "correction": "Le verre tulipe possède une base évasée pour faire tourner l'alcool et libérer ses arômes, et un col resserré pour concentrer les vapeurs vers le nez du dégustateur, idéal pour un vieux rhum ou un whisky."
                },
                {
                    "questionNumber": 72,
                    "question": "Que désigne la démarque inconnue lors de l'inventaire du bar ?",
                    "answerOptions": [
                        {"text": "Les pertes invisibles comme les vols ou les erreurs de dosage", "isCorrect": True},
                        {"text": "Les bouteilles offertes officiellement aux clients fidèles", "isCorrect": False},
                        {"text": "Les produits retournés au fournisseur car périmés", "isCorrect": False},
                        {"text": "Les verres cassés déclarés sur le cahier de casse", "isCorrect": False}
                    ],
                    "correction": "La démarque inconnue englobe toutes les pertes de marchandises qui n'ont pas de justification écrite : un coulage volontaire (vol du personnel ou client), des oublis de facturation, ou des versements trop généreux non mesurés."
                },
                {
                    "questionNumber": 73,
                    "question": "Comment appelle-t-on le tapis en caoutchouc égouttoir situé sur le bar ?",
                    "answerOptions": [
                        {"text": "Le bar mat", "isCorrect": True},
                        {"text": "Le shaker", "isCorrect": False},
                        {"text": "Le zesteur", "isCorrect": False},
                        {"text": "Le rimmer", "isCorrect": False}
                    ],
                    "correction": "Le bar mat est le tapis en caoutchouc hérissé de picots qui draine l'humidité, offrant une surface propre et sèche pour poser la verrerie et préparer les cocktails face au client."
                },
                {
                    "questionNumber": 74,
                    "question": "À quoi sert le bec verseur fixé sur le goulot des bouteilles de service ?",
                    "answerOptions": [
                        {"text": "Réguler de façon très fluide et précise le débit du liquide pour faciliter le dosage et accélérer l'exécution des recettes", "isCorrect": True},
                        {"text": "Filtrer efficacement toutes les impuretés et les petits résidus de fruits qui pourraient malencontreusement tomber dans la bouteille", "isCorrect": False},
                        {"text": "Modifier la pression atmosphérique à l'intérieur de la bouteille pour que l'alcool conserve sa fraîcheur même sans réfrigération", "isCorrect": False},
                        {"text": "Produire un sifflement sonore très particulier permettant d'alerter le chef de salle lors de chaque nouvelle commande passée au comptoir", "isCorrect": False}
                    ],
                    "correction": "Le bec verseur (ou pour spout) crée un jet continu et maîtrisé du liquide. Couplé au jigger, il évite d'éclabousser et permet un travail technique propre, gracieux et infiniment plus rapide."
                },
                {
                    "questionNumber": 75,
                    "question": "Sur une carte de bar, que permet l'application d'un coefficient multiplicateur ?",
                    "answerOptions": [
                        {"text": "Définir le prix de vente à partir du coût d'achat", "isCorrect": True},
                        {"text": "Calculer le degré alcoolique final du cocktail", "isCorrect": False},
                        {"text": "Estimer le temps de réalisation de la commande", "isCorrect": False},
                        {"text": "Connaître le nombre de verres dans une bouteille", "isCorrect": False}
                    ],
                    "correction": "Le coefficient multiplicateur est un outil comptable très simple. En multipliant le prix d'achat d'un produit par ce coefficient, on obtient rapidement son prix de vente incluant la marge souhaitée et la TVA."
                },
                {
                    "questionNumber": 76,
                    "question": "Quelle est l'utilité première du rimmer posé sur le comptoir ?",
                    "answerOptions": [
                        {"text": "Givrer rapidement les bords des verres avec du sel ou du sucre", "isCorrect": True},
                        {"text": "Presser les quartiers d'agrumes pour en extraire le jus", "isCorrect": False},
                        {"text": "Écraser finement la glace cube en glace pilée", "isCorrect": False},
                        {"text": "Essuyer les traces d'eau sous les verres servis", "isCorrect": False}
                    ],
                    "correction": "Le rimmer (ou givreur) est une boîte ronde à plusieurs compartiments pliables. Il contient une éponge imbibée de jus de citron, du sucre et du sel, permettant de border en un instant la lèvre du verre de Margarita."
                },
                {
                    "questionNumber": 77,
                    "question": "Quel est l'avantage principal d'informatiser la gestion des stocks de la cave du bar ?",
                    "answerOptions": [
                        {"text": "Mettre à jour en temps réel l'état des réserves à chaque encaissement sur la caisse tactile pour anticiper rapidement les ruptures", "isCorrect": True},
                        {"text": "Transmettre directement les recettes secrètes de l'établissement aux organismes de contrôle sanitaire de l'état de manière totalement automatique", "isCorrect": False},
                        {"text": "Obliger le chef barman à peser chaque bouteille au gramme près à la fin de chaque service pour rédiger des rapports quotidiens ultra détaillés", "isCorrect": False},
                        {"text": "Créer des fiches de dégustation virtuelles que les clients peuvent télécharger sur leur téléphone portable pendant qu'ils attendent leur commande", "isCorrect": False}
                    ],
                    "correction": "Lié au logiciel de caisse, le stock informatisé déduit instantanément les ingrédients de chaque boisson vendue (les fiches techniques y étant enregistrées), ce qui permet d'éditer automatiquement des listes d'achats précises."
                },
                {
                    "questionNumber": 78,
                    "question": "Pourquoi ne doit-on jamais conserver de jus de citron pressé d'un jour sur l'autre ?",
                    "answerOptions": [
                        {"text": "Il s'oxyde rapidement et perd ses qualités gustatives fraîches", "isCorrect": True},
                        {"text": "Il se transforme naturellement en alcool pendant la nuit", "isCorrect": False},
                        {"text": "Il ronge les récipients de stockage en plastique", "isCorrect": False},
                        {"text": "Il décolore immédiatement les autres sirops au frais", "isCorrect": False}
                    ],
                    "correction": "Les jus d'agrumes frais sont très instables. Exposés à l'oxygène, ils perdent leur acidité vive et développent un goût passé voire rance. Un bar de qualité doit presser ses jus en début de chaque service."
                },
                {
                    "questionNumber": 79,
                    "question": "Que doit inclure obligatoirement une fiche technique de bar bien rédigée ?",
                    "answerOptions": [
                        {"text": "Les ingrédients, les dosages, la méthode, la verrerie et le coût", "isCorrect": True},
                        {"text": "Uniquement les dosages d'alcool et le prix de vente final", "isCorrect": False},
                        {"text": "Les noms des clients réguliers qui consomment cette boisson", "isCorrect": False},
                        {"text": "Les coordonnées du fournisseur des jus de fruits", "isCorrect": False}
                    ],
                    "correction": "La fiche technique est exhaustive : elle comprend la recette (centilitres, méthode au shaker ou verre à mélange, décoration), une photo si possible, et toute la partie financière (prix d'achat, coût de revient, prix de vente)."
                },
                {
                    "questionNumber": 80,
                    "question": "Comment le barman doit-il organiser le rangement des bouteilles sur le back bar ou arrière-bar ?",
                    "answerOptions": [
                        {"text": "Regrouper les alcools par familles logiques et les présenter de manière esthétique pour susciter l'envie et faciliter la vente", "isCorrect": True},
                        {"text": "Dissimuler toutes les bouteilles haut de gamme derrière des vitres teintées sombres pour éviter d'attirer l'attention des clients malveillants", "isCorrect": False},
                        {"text": "Casser volontairement la symétrie du rangement chaque jour afin d'obliger les nouveaux employés à mémoriser l'emplacement de chaque marque", "isCorrect": False},
                        {"text": "Stocker absolument toutes les liqueurs douces à plat dans des tiroirs pour empêcher le sucre de sécher et de bloquer définitivement le bouchon", "isCorrect": False}
                    ],
                    "correction": "Le back bar est la vitrine du bar. Il doit être organisé avec soin : par famille (rhums, whiskies), bien éclairé, sans bouteille à moitié vide au premier rang, car il déclenche l'impulsion d'achat des clients installés."
                }
            ]
        },
        # =========================================================================
        # THÈME 5 : ACCUEIL, COMMERCIALISATION ET COMMUNICATION (Questions 81 à 100)
        # =========================================================================
        5: {
            "name": "THÈME 5 : ACCUEIL, COMMERCIALISATION ET COMMUNICATION",
            "questions": [
                {
                    "questionNumber": 81,
                    "question": "Quelle est la première règle d'or de l'accueil au bar ?",
                    "answerOptions": [
                        {"text": "Sourire et saluer le client", "isCorrect": True},
                        {"text": "Servir directement un verre d'eau", "isCorrect": False},
                        {"text": "Demander le mode de paiement", "isCorrect": False},
                        {"text": "Nettoyer le comptoir", "isCorrect": False}
                    ],
                    "correction": "L'accueil est décisif. Un sourire sincère, un contact visuel et une salutation courtoise (même si le barman est occupé) rassurent immédiatement le client et lancent positivement l'expérience client."
                },
                {
                    "questionNumber": 82,
                    "question": "En quoi consiste la technique de vente additionnelle ou up-selling ?",
                    "answerOptions": [
                        {"text": "Proposer un produit de gamme supérieure à celui demandé initialement", "isCorrect": True},
                        {"text": "Offrir systématiquement un second verre gratuit pour fidéliser", "isCorrect": False},
                        {"text": "Refuser de servir les boissons les moins chères de la carte", "isCorrect": False},
                        {"text": "Forcer le client à acheter une bouteille entière au lieu d'un verre", "isCorrect": False}
                    ],
                    "correction": "L'up-selling (la montée en gamme) consiste à inciter poliment le client à choisir un alcool premium au lieu du spiritueux de base (la verse) pour son cocktail, augmentant ainsi le chiffre d'affaires et l'expérience de dégustation."
                },
                {
                    "questionNumber": 83,
                    "question": "Quelle attitude adopter face à un client qui formule une réclamation sur le goût de son cocktail ?",
                    "answerOptions": [
                        {"text": "Écouter attentivement sa plainte, s'excuser pour le désagrément et lui proposer immédiatement de refaire la boisson à sa convenance", "isCorrect": True},
                        {"text": "Lui expliquer avec de très nombreux termes techniques et complexes qu'il ne connaît absolument rien à la mixologie moderne et à l'équilibre des saveurs", "isCorrect": False},
                        {"text": "Appeler immédiatement le service de sécurité de l'établissement pour l'obliger à payer son addition avant de l'expulser manu militari vers la rue", "isCorrect": False},
                        {"text": "Ignorer totalement sa remarque en passant très rapidement à la prise de commande des autres clients présents au comptoir pour ne pas perdre de temps", "isCorrect": False}
                    ],
                    "correction": "La gestion de conflit exige empathie et professionnalisme. Le client a toujours le droit d'être déçu. Remplacer gracieusement le verre frustrant transforme une mauvaise expérience en une fidélisation réussie."
                },
                {
                    "questionNumber": 84,
                    "question": "Quelle est l'importance de l'analyse visuelle du client lors de son arrivée ?",
                    "answerOptions": [
                        {"text": "Adapter son discours et ses suggestions à sa typologie", "isCorrect": True},
                        {"text": "Évaluer s'il laissera un pourboire important en fin de service", "isCorrect": False},
                        {"text": "Deviner son prénom pour personnaliser la prise de commande", "isCorrect": False},
                        {"text": "Juger de sa capacité à supporter les alcools très forts", "isCorrect": False}
                    ],
                    "correction": "Repérer si le client est seul, en rendez-vous galant ou en groupe festif permet d'ajuster le temps de la prise de commande, le vocabulaire utilisé et le type de boissons à suggérer."
                },
                {
                    "questionNumber": 85,
                    "question": "Qu'est-ce que le cross-selling au bar ?",
                    "answerOptions": [
                        {"text": "Vendre un produit complémentaire", "isCorrect": True},
                        {"text": "Vendre un alcool moins cher", "isCorrect": False},
                        {"text": "Offrir un produit au comptoir", "isCorrect": False},
                        {"text": "Rembourser une boisson servie", "isCorrect": False}
                    ],
                    "correction": "La vente croisée (cross-selling) est une technique consistant à proposer un produit qui complète l'achat, comme suggérer une planche de tapas à partager avec la commande de deux cocktails."
                },
                {
                    "questionNumber": 86,
                    "question": "Pourquoi est-il essentiel de maintenir un comptoir parfaitement propre en permanence ?",
                    "answerOptions": [
                        {"text": "Le comptoir est l'espace de dégustation direct du client et reflète l'hygiène du bar", "isCorrect": True},
                        {"text": "Pour empêcher l'usure prématurée du vernis du bois massif du mobilier", "isCorrect": False},
                        {"text": "Afin de réduire la consommation d'eau lors de la grande plonge de fin de service", "isCorrect": False},
                        {"text": "Pour éviter que les verres ne glissent et ne tombent sur le sol", "isCorrect": False}
                    ],
                    "correction": "Le comptoir est la table du client. Un bar humide, collant ou jonché de miettes donne immédiatement une impression repoussante d'insalubrité qui nuira gravement à l'image commerciale de l'établissement."
                },
                {
                    "questionNumber": 87,
                    "question": "Comment un barman professionnel doit-il gérer un client devenant agressif sous l'effet de l'alcool ?",
                    "answerOptions": [
                        {"text": "Garder son calme absolu, isoler la personne si possible, refuser fermement tout nouveau service d'alcool et faire appel à la sécurité ou aux autorités si nécessaire", "isCorrect": True},
                        {"text": "Augmenter le volume de la musique du bar à son niveau maximum pour couvrir ses éclats de voix et empêcher les autres clients d'être dérangés par ses propos incohérents", "isCorrect": False},
                        {"text": "Lui servir secrètement une boisson très fortement dosée en alcool afin qu'il s'endorme rapidement sur sa chaise et arrête de perturber le bon déroulement du service du soir", "isCorrect": False},
                        {"text": "Engager une violente dispute verbale avec lui devant tout le monde pour asseoir son autorité de chef de bar et impressionner la clientèle régulière", "isCorrect": False}
                    ],
                    "correction": "La sécurité des autres clients et du personnel prime. Le barman doit faire preuve d'autorité tranquille sans agressivité, stopper le service d'alcool et utiliser les moyens de sûreté prévus par l'établissement pour faire sortir l'individu."
                },
                {
                    "questionNumber": 88,
                    "question": "À quel moment précis le barman doit-il idéalement remettre la carte des boissons au client ?",
                    "answerOptions": [
                        {"text": "Dès son installation au comptoir après l'avoir salué", "isCorrect": True},
                        {"text": "Uniquement après avoir pris la commande d'une boisson chaude", "isCorrect": False},
                        {"text": "Juste avant de présenter l'addition pour vérification", "isCorrect": False},
                        {"text": "Lorsque le client manifeste des signes d'impatience évidents", "isCorrect": False}
                    ],
                    "correction": "Donner rapidement la carte permet d'occuper l'attention du client. Cela lui laisse le temps de réfléchir et de s'immerger dans l'univers du bar, ce qui diminue son sentiment d'attente s'il y a de l'affluence."
                },
                {
                    "questionNumber": 89,
                    "question": "Quel élément sensoriel participe fortement à l'atmosphère d'un bar ?",
                    "answerOptions": [
                        {"text": "La programmation musicale", "isCorrect": True},
                        {"text": "L'épaisseur des verres", "isCorrect": False},
                        {"text": "Le modèle de la caisse", "isCorrect": False},
                        {"text": "La marque des réfrigérateurs", "isCorrect": False}
                    ],
                    "correction": "L'ambiance sonore, l'éclairage et la décoration construisent l'identité du bar. Une playlist adaptée au concept et à l'heure du service incite les clients à prolonger leur visite et leur consommation."
                },
                {
                    "questionNumber": 90,
                    "question": "Quel est l'intérêt commercial de proposer des Mocktails de haute qualité sur la carte ?",
                    "answerOptions": [
                        {"text": "Valoriser la clientèle qui ne consomme pas d'alcool en lui offrant une véritable expérience de dégustation vendue à forte marge", "isCorrect": True},
                        {"text": "Écouler discrètement tous les sirops périmés et les jus de fruits en fin de vie avant le passage des inspecteurs de la répression des fraudes", "isCorrect": False},
                        {"text": "Démontrer au grand public qu'il est absolument impossible de prendre du plaisir dans un bar sans consommer une boisson fortement alcoolisée", "isCorrect": False},
                        {"text": "Respecter une très vieille obligation légale qui impose d'avoir au moins cinquante pour cent de recettes sans alcool sur le menu imprimé", "isCorrect": False}
                    ],
                    "correction": "Le public sans alcool (Mocktails ou Virgin Cocktails) exige aujourd'hui autant de créativité que les consommateurs d'alcool. Les mocktails bien travaillés génèrent une excellente rentabilité, car leur coût matière est souvent bas."
                },
                {
                    "questionNumber": 91,
                    "question": "Quelle est la qualité primordiale exigée lors du rendu de la monnaie à un client ?",
                    "answerOptions": [
                        {"text": "L'annoncer à haute voix et la rendre dans la main ou sur une coupelle propre", "isCorrect": True},
                        {"text": "La jeter rapidement sur le comptoir humide pour passer au client suivant", "isCorrect": False},
                        {"text": "Ne jamais rendre les petites pièces de monnaie pour obliger au pourboire", "isCorrect": False},
                        {"text": "Demander au client de vérifier le montant exact à la calculatrice", "isCorrect": False}
                    ],
                    "correction": "L'encaissement est l'acte commercial final. Rendre la monnaie de façon claire, polie et visible évite tout litige sur le montant et souligne le professionnalisme de l'établissement."
                },
                {
                    "questionNumber": 92,
                    "question": "Que doit faire le barman pour faciliter le choix d'un client indécis ?",
                    "answerOptions": [
                        {"text": "Poser des questions ouvertes sur ses goûts", "isCorrect": True},
                        {"text": "Lui imposer d'office le cocktail le plus cher de la carte des spécialités", "isCorrect": False},
                        {"text": "Le laisser seul pendant dix minutes pour qu'il réfléchisse tranquillement", "isCorrect": False},
                        {"text": "Lui faire goûter gratuitement tous les alcools disponibles au comptoir", "isCorrect": False}
                    ],
                    "correction": "En demandant \"Qu'aimez-vous habituellement ? Plutôt sucré, amertume, fruité ou sec ?\", le barman endosse son rôle de conseiller et guide le client vers une boisson qui le satisfera à coup sûr."
                },
                {
                    "questionNumber": 93,
                    "question": "Comment s'appelle l'heure de forte affluence commerciale au bar ?",
                    "answerOptions": [
                        {"text": "Le coup de feu", "isCorrect": True},
                        {"text": "Le closing", "isCorrect": False},
                        {"text": "Le briefing", "isCorrect": False},
                        {"text": "L'inventaire", "isCorrect": False}
                    ],
                    "correction": "Le coup de feu désigne le pic d'activité (souvent entre l'afterwork et le milieu de soirée). Le barman doit alors faire preuve de sang-froid, d'organisation (gestion des bons) et de rapidité d'exécution."
                },
                {
                    "questionNumber": 94,
                    "question": "Pourquoi la gestuelle et la posture du barman derrière son comptoir sont-elles si importantes ?",
                    "answerOptions": [
                        {"text": "Le barman est en représentation permanente, son allure reflète le niveau de qualité de l'établissement et instaure un climat de totale confiance", "isCorrect": True},
                        {"text": "Il est strictement interdit par le règlement intérieur de s'asseoir ou de s'adosser au mur sous peine de licenciement pour faute grave par le directeur", "isCorrect": False},
                        {"text": "Une posture rigide et sévère empêche les clients de poser trop de questions chronophages sur la composition complexe des différentes recettes de mixologie", "isCorrect": False},
                        {"text": "La loi impose une certaine ergonomie de travail pour limiter la fatigue visuelle des clients éblouis par l'éclairage de l'arrière-bar", "isCorrect": False}
                    ],
                    "correction": "Le bar est une scène de théâtre. Une gestuelle maîtrisée avec les shakers, une posture droite et dynamique sont des arguments de vente fantastiques qui captivent le client assis au comptoir."
                },
                {
                    "questionNumber": 95,
                    "question": "Quel est l'impact d'une bonne connaissance de la carte par le personnel de salle et de bar ?",
                    "answerOptions": [
                        {"text": "Accélérer la prise de commande et conseiller le client avec assurance", "isCorrect": True},
                        {"text": "Supprimer la nécessité d'imprimer des menus physiques pour les tables", "isCorrect": False},
                        {"text": "Remplacer totalement le responsable des achats de l'établissement", "isCorrect": False},
                        {"text": "Permettre de modifier les prix de vente en plein milieu du service", "isCorrect": False}
                    ],
                    "correction": "Maîtriser les ingrédients et l'histoire des cocktails de la carte permet d'argumenter la vente, de faire rêver le client et de gagner du temps lors des recommandations."
                },
                {
                    "questionNumber": 96,
                    "question": "Que signifie fidéliser la clientèle d'un débit de boissons ?",
                    "answerOptions": [
                        {"text": "Créer un attachement et une relation de confiance pour encourager le retour régulier", "isCorrect": True},
                        {"text": "Rendre les clients financièrement dépendants de l'établissement avec des crédits", "isCorrect": False},
                        {"text": "Obliger les clients à signer un contrat d'abonnement annuel très coûteux", "isCorrect": False},
                        {"text": "Leur interdire l'accès à tous les autres bars concurrents du même quartier", "isCorrect": False}
                    ],
                    "correction": "La fidélisation est le pilier de la rentabilité. Un client retenu grâce à la chaleur de l'accueil ou au fait qu'on se souvienne de lui coûte moins cher en publicité et devient un ambassadeur de l'établissement."
                },
                {
                    "questionNumber": 97,
                    "question": "Comment doit réagir un barman si une commande est annoncée incomplète par le serveur en salle ?",
                    "answerOptions": [
                        {"text": "Il doit questionner poliment le serveur pour obtenir les précisions manquantes avant de commencer à préparer la moindre boisson", "isCorrect": True},
                        {"text": "Il doit immédiatement préparer les boissons manquantes en devinant les envies des clients pour rattraper le retard pris en salle", "isCorrect": False},
                        {"text": "Il doit refuser catégoriquement de servir la table entière et exiger que les clients viennent commander directement au comptoir principal", "isCorrect": False},
                        {"text": "Il doit signaler publiquement l'incompétence du serveur devant tous les clients installés afin de décliner toute responsabilité sur le retard", "isCorrect": False}
                    ],
                    "correction": "La communication entre la salle et le bar (le passe) doit être fluide. Si une précision manque (avec ou sans glace, choix du spiritueux), le barman bloque l'envoi pour éviter toute insatisfaction."
                },
                {
                    "questionNumber": 98,
                    "question": "Quelle attention particulière faut-il accorder au volume de la musique dans le bar ?",
                    "answerOptions": [
                        {"text": "Il doit correspondre au concept du lieu tout en permettant aux clients de converser", "isCorrect": True},
                        {"text": "Il doit toujours être assourdissant pour créer une vraie ambiance de fête de nuit", "isCorrect": False},
                        {"text": "Il doit être totalement coupé dès qu'un groupe de plus de dix personnes s'installe", "isCorrect": False},
                        {"text": "Il doit couvrir les bruits des shakers et de la machine à glaçons du comptoir", "isCorrect": False}
                    ],
                    "correction": "Sauf concept clubbing strict, la musique d'ambiance d'un bar ne doit jamais empêcher la prise de commande ni obliger les clients à hurler pour discuter entre eux."
                },
                {
                    "questionNumber": 99,
                    "question": "Quel est le rôle d'un cocktail Signature sur la carte d'un établissement ?",
                    "answerOptions": [
                        {"text": "Démarquer le bar de la concurrence en proposant une création exclusive et originale", "isCorrect": True},
                        {"text": "Respecter scrupuleusement les normes historiques imposées par le syndicat des barmans", "isCorrect": False},
                        {"text": "Offrir la boisson la moins chère possible pour attirer un public étudiant", "isCorrect": False},
                        {"text": "Prouver que le barman connaît par cœur les recettes mondiales ancestrales", "isCorrect": False}
                    ],
                    "correction": "Un cocktail signature est propre au bar. C'est la vitrine du savoir-faire créatif de l'équipe, un argument de vente fort et un formidable outil de marge commerciale."
                },
                {
                    "questionNumber": 100,
                    "question": "À la fin du service, pourquoi est-il crucial de dire au revoir chaleureusement au client ?",
                    "answerOptions": [
                        {"text": "La dernière impression est celle que le client gardera en mémoire, c'est l'ultime étape pour garantir sa fidélisation", "isCorrect": True},
                        {"text": "Il faut toujours s'assurer verbalement que le client a bien réglé l'intégralité de son addition avant de le laisser sortir", "isCorrect": False},
                        {"text": "Cela permet d'avertir discrètement le vigile que des personnes alcoolisées vont prendre leur véhicule", "isCorrect": False},
                        {"text": "C'est une obligation légale stipulée dans le code du commerce pour clore officiellement le contrat de vente", "isCorrect": False}
                    ],
                    "correction": "L'expérience client globale se termine à la porte. Un \"Au revoir et à bientôt !\" souriant efface souvent les petits défauts d'un service et sécurise l'envie du client de revenir."
                }
            ]
        }
    }
}