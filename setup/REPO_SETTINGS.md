# Paramètres GitHub : cible de recette

**Modèles de permissions :** ce dépôt personnel sert à simuler, mais ne reproduit pas les Teams et rôles d'une organisation GitHub.

| Rubrique | État cible LAB | Preuve demandée |
|---|---|---|
| Visibility | PRIVATE, ne jamais changer | capture Settings / API |
| Features: Issues | activé | liste des Issues |
| Features: Projects | activé | Project privé lié |
| Features: Discussions | activé si disponible | catégories et sujet test |
| Features: Wiki | facultatif selon plan privé | page wiki test ou limite documentée |
| Settings: Pull Requests | squash merge préféré ; auto-delete optionnel | paramètre constaté |
| Settings: Actions | workflows GitHub autorisés ; `GITHUB_TOKEN` read-only par défaut | job minimal exécuté |
| Rulesets | obligatoire après test de PR si privé et forfait le permet | essai négatif refusé |
| Security | Dependabot activé ; scan de secrets/CodeQL selon forfait | alertes et policies observées |
| Pages | **OFF** : pas de site public depuis un dépôt de test | Settings Pages |
| Secrets | zéro secret de déploiement ; aucun PAT partagé | revue des noms, pas des valeurs |
| Environments | aucun environnement de production / staging réel | inventaire |
| GitHub Apps | accès minimal ; aucun miroir vers l'équipe | inventaire des apps |
| Codespaces | facultatif, selon forfait et dépenses | test d'ouverture isolé |
| Copilot | aide au développement facultative, jamais merge sans revue humaine | politique dans docs |
| Releases | release draft interne seulement après CI | lien + validation |
| Packages | aucun GHCR public | visibilité vérifiée avant publication expérimentale |

Attention : la possibilité de configurer rulesets/protection sur un **dépôt privé** dépend du forfait (Pro/Team/Enterprise). Aucun changement de visibilité automatique.

## Différences entre le LAB et la vraie organisation
Teams, rôles d'accès granulaires et demandes d'approbation indépendantes ne se testent pas honnêtement avec un seul compte propriétaire : documenter "non vérifié" plutôt que "validé".
