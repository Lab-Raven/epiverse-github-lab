# Ce qu'il est possible de tester avec un dépôt GitHub PUBLIC

L'objectif du LAB est d'évaluer toutes les fonctionnalités GitHub pertinentes **sans déployer ni ouvrir les données du projet réel**.

## Séparation des deux visibilités

- Repository `Lab-Raven/epiverse-github-lab` : PUBLIC.
- Project d'organisation `Lab-Raven/projects/1` : PRIVATE.
- Issues, PR, discussions, Wiki, code, site Pages : **PUBLICS**.
- Le Project privé ne masque pas le contenu d'une Issue liée.

## Fonctions testables gratuitement sur dépôt public

Protection de branche / rulesets, Wiki, Pages, GitHub Actions avec limites de consommation, Dependabot, CodeQL et plusieurs outils de secret protection, Issues, Projects, Discussions, releases, packages, Codespaces selon quotas, Insights. Les fonctionnalités Code Quality, Copilot, certaines contrôles d'organisation et la gestion avancée des secrets peuvent dépendre de l'abonnement/licence et ne sont pas toutes gratuites.

## Vues distinctes à ne pas confondre

1. **GitHub Projects Views** : sprints, Kanban, roadmap, charge, champs et automations dans le Project #1 (privé).
2. **GitHub Issues Views** : vues de recherche du dépôt (privées ou partagées) pour trier les Issues ; indépendantes du Project.

## Protections recommandées pour main

- Ruleset ciblant `main`, d'abord Evaluate puis Active.
- Empêcher suppression et force push.
- Exiger les Pull Requests et les checks réellement existants.
- Ne pas exiger de relecteur supplémentaire non disponible dans le LAB mono-utilisateur.
- Les tests gratuits de règles sur un dépôt public ne prouvent pas qu'elles seront applicables dans le dépôt officiel privé avec GitHub Free.

## Démonstration complémentaire

GitHub Pages peut publier `docs/site/` **uniquement via déclenchement manuel** de `.github/workflows/pages-lab.yml`. Configurer d'abord Settings → Pages → Source : GitHub Actions.

Le site public ne doit contenir que des informations fictives. Une publication n'est ni un déploiement de l'application EpiVerse ni une preuve de son avancement.
