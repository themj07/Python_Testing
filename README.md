# Fonction loadClubs

La fonction loadClubs est responsable du chargement des données des clubs à partir d'un fichier JSON. Initialement, la fonction ne prenait pas en compte la possibilité de spécifier un nom de fichier différent, limitant ainsi sa flexibilité.

# Erreur d'origine

La version initiale de la fonction ne permettait pas de charger des fichiers de clubs avec des noms différents de 'clubs.json'. Cela pouvait être contraignant dans des situations où le nom du fichier était variable.

# Objectif du test

Pour remédier à cette limitation, un test unitaire a été créé (TestLoadClubs.test_loadClubs) pour s'assurer que la fonction peut désormais accepter un argument optionnel filename permettant de spécifier le nom du fichier à charger. Ce test a pour objectif de vérifier si la fonction peut charger correctement les clubs à partir d'un fichier autre que 'clubs.json'.

# Correction apportée

La correction consiste à ajouter un paramètre filename à la fonction loadClubs avec une valeur par défaut ('clubs.json'). Ainsi, la fonction peut toujours être utilisée sans argument pour charger le fichier par défaut, mais elle offre également la flexibilité de spécifier un autre fichier au besoin.
