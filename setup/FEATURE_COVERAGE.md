# Couverture de l'écosystème GitHub dans le LAB

| Fonction | Installation dans le dépôt | Activation sur GitHub | Critère de validation |
|---|---|---|---|
| Code / branches | Oui | Oui | commit, branche et diff |
| Issues | Oui | Oui | 28+ issues d'essai, labels, assignees |
| Pull Requests | Oui | Oui | PR #6 brouillon liée à #1 |
| Code review | Politique fournie | Relecteur indépendant absent | vraie revue extérieure |
| CODEOWNERS | Oui | Fichier actif | auto-request non prouvée |
| GitHub Actions | Workflows écrits | **Startup failure** #7 | job et artefact réussis |
| Dependabot | Config présent | Tâche dynamique en échec | PR créée |
| Security policy | Oui | Oui | SECURITY.md présent |
| Secret scanning / CodeQL | Contrôle Python gratuit en dépôt | Fonction native selon plan | alertes vérifiées |
| GitHub Projects V2 | Script CLI + 10 vues spécifiées | **Non créé par connecteur** | URL Project privé |
| Milestones | Script bootstrap | Non créés par connecteur | jalons visibles |
| Discussions | Templates + script | Non activées | catégorie et sujet interne |
| Wiki | Documentation + script | Non activé | wiki privé si disponible |
| Releases | Workflow draft manuel | Pas de release | brouillon privé référencé |
| Packages GHCR | Procédure | Aucun package | package privé, pas de prod |
| Environments | Politique | Aucun vrai déploiement | simulation uniquement |
| Insights | Natif | Oui | statistiques LAB |
| Codespaces | Devcontainer | Dépend du forfait | lancement isolé et coût vérifié |
| Copilot / Agents | Politique et revue | Service externe, non connecté | PR agent relue |
| Pages | Volontairement non activé | OFF | confidentialité du LAB garantie |
| API / Apps | Scripts et appels GitHub | Accès partiel du connecteur | limitations explicites |
| Audit / backup | Documentation | Procédure de test | export/restauration vérifiés |

Les états `préparé`, `activé` et `testé` sont distincts. Ne pas décrire une fonctionnalité « disponible sur GitHub » comme « configurée avec succès » sans preuve.
