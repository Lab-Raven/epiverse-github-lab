# Sauvegarde et restauration du laboratoire

Le dépôt Git conserve l'historique de code, **pas** nécessairement les paramètres Projects, Issues, Discussions, secrets, branches protégées et droits.

- Exporter la liste des Issues/PR et champs Projects avec GitHub CLI dans un espace privé.
- Éviter d'exporter des secrets, emails personnels ou tokens.
- Conserver les fichiers de configuration source sous contrôle de versions.
- Documenter une restauration de test dans une copie privée isolée et vérifier les liens d'origine.
- Le transfert ultérieur vers l'équipe sera sélectif et validé, **pas un miroir destructif**.
