# Code initial
Le code initial était une route Flask qui permettait aux utilisateurs d’acheter des places pour une compétition pour un club. La fonction purchasePlaces récupérait le nom de la compétition et du club à partir des données du formulaire de la requête POST, cherchait la compétition et le club dans les listes competitions et clubs respectivement, déduisait le nombre de places requises du nombre total de places disponibles pour la compétition, et renvoyait un message de confirmation de réservation.

# Fonction de test unitaire
La fonction de test unitaire test_purchasePlaces a été conçue pour tester la route purchasePlaces. Elle simulait une requête POST à la route avec des données de formulaire spécifiques, vérifiait si le nombre de places disponibles pour la compétition avait été correctement déduit après l’achat, vérifiait si un message flash de confirmation de réservation était présent dans la réponse, et vérifiait si le code de statut de la réponse était 200, indiquant le succès.

# Fonction corrigée
La fonction purchasePlaces corrigée a ajouté plusieurs vérifications pour s’assurer que la compétition et le club existent et que le nombre de places requises est valide avant de déduire le nombre de places. Elle a également ajouté une vérification pour s’assurer qu’un utilisateur ne peut pas acheter plus de 12 places à la fois. Ces modifications ont rendu le code plus robuste et ont permis de gérer plus efficacement les erreurs potentielles.

# Explication des modifications
Le code initial ne vérifiait pas si la compétition et le club existaient réellement ni si le nombre de places requises était valide avant de déduire le nombre de places. Cela pourrait conduire à des erreurs si les données du formulaire de la requête POST ne correspondaient à aucune compétition ou club existant ou si le nombre de places requises était supérieur au nombre total de places disponibles pour la compétition.

Le code corrigé a ajouté ces vérifications pour s’assurer que la compétition et le club existent et que le nombre de places requises est valide avant de déduire le nombre de places. Il a également ajouté une vérification pour s’assurer qu’un utilisateur ne peut pas acheter plus de 12 places à la fois. Ces modifications ont rendu le code plus robuste et ont permis de gérer plus efficacement les erreurs potentielles.

La fonction de test unitaire est restée la même, car elle testait correctement la route purchasePlaces en simulant une requête POST et en vérifiant le code de statut de la réponse. Elle a assuré que la route fonctionnait comme prévu et renvoyait une réponse réussie lorsqu’on lui donnait des paramètres valides.
