# Fonction loadCompetitions

La fonction loadCompetitions est utilisée pour charger la liste des compétitions à partir d'un fichier JSON. Initialement, la fonction ne prenait pas en compte la possibilité de spécifier un nom de fichier différent, limitant ainsi sa flexibilité.

# Erreur d'origine

La version initiale de la fonction ne permettait pas de charger des fichiers de compétitions avec des noms différents de 'competitions.json'. Cela pouvait être contraignant dans des situations où le nom du fichier était variable.

# Objectif du test

Pour remédier à cette limitation, un test unitaire (TestLoadCompetitions.test_loadCompetitions) a été créé. Ce test a pour objectif de vérifier si la fonction peut désormais accepter un argument optionnel file permettant de spécifier le nom du fichier à charger, offrant ainsi plus de flexibilité dans son utilisation.

# Correction apportée

La correction consiste à ajouter un paramètre optionnel file à la fonction loadCompetitions avec une valeur par défaut ('competitions.json'). Ainsi, la fonction peut toujours être utilisée sans argument pour charger le fichier par défaut, mais elle offre également la flexibilité de spécifier un autre fichier au besoin.
