# Tests Unitaires des Routes de l'Application Flask

La classe TestAppRoutes définit des tests unitaires pour vérifier le comportement des routes dans une application Flask. Ces tests utilisent un client de test pour simuler des requêtes HTTP et assurent le bon fonctionnement des routes dans différentes situations.
Méthodes de Test

    setUp: Cette méthode est appelée avant chaque test et initialise un client de test pour l'application Flask, facilitant la simulation des requêtes HTTP.

    test_book_valid_input: Ce test vérifie le comportement de la route /book avec des données d'entrée valides. Il simule une requête GET vers la route /book/PremierLeague/Arsenal et vérifie si le code d'état de la réponse est 200 (OK).

    test_book_invalid_input: Ce test vérifie le comportement de la route /book avec des données d'entrée invalides. Il simule une requête GET vers la route /book/InvalidCompetition/InvalidClub et vérifie si le code d'état de la réponse est 200. (Note: Le commentaire indique que le code d'état 200 est attendu ici, cependant, cela peut nécessiter une clarification en fonction des exigences du test.)

# Exécution des Tests

Pour exécuter les tests, assurez-vous d'être dans le même répertoire que votre fichier de tests et utilisez la commande suivante :

bash

python -m unittest tests_unitaires/forAppRoutes

Cela exécutera les tests définis dans la classe TestAppRoutes. Assurez-vous que votre environnement d'exécution est configuré correctement pour l'application Flask.
Réussite des Tests

Si tous les tests réussissent, cela indique que les routes de l'application réagissent comme prévu dans différentes situations. Les tests fournissent une assurance de la qualité du code et facilitent la détection précoce d'éventuels problèmes lors du développement de l'application.
