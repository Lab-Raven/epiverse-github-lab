# Plan de test des fonctionnalités GitHub

| Fonction | Dans le LAB | Limite / action complémentaire |
|---|---|---|
| Repository | Dépôt privé séparé | Vérifié par API |
| Issues | Templates Feature, Task, Bug, Risk, Decision | Ajouter labels/milestones via bootstrap manuel |
| Projects v2 | Champs, sprint, roadmap, board | Création manuelle UI, voir PROJECTS.md |
| Pull Requests | Template, revue, checks, preuve | Tester sur une branche distincte |
| CODEOWNERS | Propriétaire unique du LAB | Une revue indépendante requiert un 2e compte |
| Actions | CI Python, reporting API, archive | Workflows sans déploiement |
| Dependabot | Versions d'Actions | PR à examiner, aucun automerge |
| Security | Politique, alertes selon plan | Activer/examiner dans Settings |
| Discussions | Formulaire d'idées | Activer Settings → Features et catégorie Ideas |
| Wiki | Option facultative | Docs versionnés prioritaires |
| Releases | Workflow d'archive en artefact privé | Aucune publication automatique |
| Packages/GHCR | Non utilisé (absence d'image utile) | Test séparé requis |
| Environments | Non déployé | Aucun secret externe |
| Insights | Historique natif des contributions | Ne pas extrapoler l'activité au projet réel |
| Pages | Non activé | Présentation publique future dans dépôt séparé |
| Copilot | Règles d'agents et revue humaine à documenter | Ne pas laisser d'agents fusionner |
| Codespaces | Optionnel | Tester selon forfait et coût, sans data réelle |

Le laboratoire ne garantit pas que tous les onglets soient activables via les API accessibles.
