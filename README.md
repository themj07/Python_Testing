Fonction showSummary

La fonction showSummary est une route dans une application Flask qui est utilisée pour afficher un résumé en fonction d'un courriel fourni dans une requête POST. Initialement, la fonction n'était pas traitée de manière robuste en cas de courriel invalide, ce qui pouvait entraîner des erreurs.

Erreur d'origine

La version initiale de la fonction ne traitait pas correctement les cas où le courriel fourni n'était associé à aucun club. Cela pouvait provoquer des erreurs dans le rendu du template ou renvoyer un code d'état 200 avec un contenu incorrect.

Objectif des tests

Deux tests unitaires ont été créés pour cette fonction afin de garantir son bon fonctionnement dans différents scénarios.

    test_show_summary_with_valid_email: Vérifie si la route /showSummary renvoie un code d'état 200 (OK) lorsque le courriel fourni est valide. D'autres assertions peuvent être ajoutées pour vérifier le contenu du template rendu.

    test_show_summary_with_invalid_email: Vérifie si la route /showSummary renvoie un code d'état 404 (Non trouvé) lorsque le courriel fourni est invalide.

Correction apportée

La correction apportée à la fonction showSummary consiste à utiliser la fonction next() avec une valeur par défaut None pour rechercher le club correspondant au courriel fourni. Si le club est trouvé, la fonction rend le template avec les détails du club et des compétitions. Si aucun club n'est trouvé, la fonction utilise abort(404) pour renvoyer un code d'état 404.
Cette correction garantit une meilleure gestion des cas où le courriel fourni ne correspond à aucun club, assurant ainsi un comportement plus robuste de la fonction showSummary.
