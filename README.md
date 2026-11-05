# EpiVerse — GitHub LAB public (non officiel)

> **LABORATOIRE PUBLIC — DONNÉES FICTIVES.** Ce dépôt sert à expérimenter l'écosystème GitHub, pas à héberger l'application EpiVerse ni à démontrer que ses fonctionnalités sont livrées.

## Visibilité et périmètre

- **Repository : PUBLIC intentionnellement** pour tester les fonctions GitHub Free accessibles aux dépôts publics (rulesets, CodeQL, Wiki, Pages et collaboration).
- **Project d'organisation n° 1 : PRIVATE**. [EpiVerse — LAB](https://github.com/orgs/Lab-Raven/projects/1).
- **Issues et PR : PUBLIQUES**, même si elles sont liées à un Project privé.
- Jamais de clés, documents internes, identifiants personnels non autorisés, exports privés ou données de l'équipe réelle.
- **Aucune synchronisation ni modification du dépôt officiel `epiverse-epitech/epiverse`.**

**Avertissement de sécurité :** de premières révisions publiques ont contenu des noms de membres réels. Modifier les fichiers actuels ne supprime pas ces versions historiques. Le contenu de l'historique public et des tickets doit faire l'objet d'une revue humaine spécifique.

## Tester les fonctionnalités GitHub

| Fonction | Accès |
|---|---|
| Code, branches | [Code](../../) |
| Backlog, bugs et risques | [Issues](../../issues) |
| Revue et CI | [Pull Requests](../../pulls) |
| Automatisations / rapports | [Actions](../../actions) |
| Kanban, roadmap, sprints | [Project n° 1 (privé)](https://github.com/orgs/Lab-Raven/projects/1) |
| Sécurité / CodeQL / Dependabot | [Security](../../security) |
| Échanges | [Discussions](../../discussions) |
| Documentation publique | [Wiki](../../wiki) |
| Activité et métriques du LAB | [Insights](../../pulse) |

## Documentation

- [Équipe fictive](docs/governance/TEAM.md) et [RACI fictive](docs/governance/RACI.md)
- [Décisions de LAB](docs/governance/DECISIONS.md)
- [Definition of Done](docs/quality/DoD.md)
- [Traçabilité des scénarios](docs/governance/TRACEABILITY_MATRIX.md)
- [Configuration du Project](setup/PROJECTS.md) et [vues](setup/PROJECTS_VUES.md)
- [Installation](setup/CONFIGURATION_MANUELLE.md) et [sécurité](docs/quality/SECURITY_CONTROLS.md)

## Vérifications locales

```bash
python3 scripts/verify_lab.py
python3 -m unittest discover -s tests -v
python3 scripts/public_lab_guard.py
bash scripts/complete_lab.sh --dry-run
```

Le scanner de publication est **heuristique** : une revue humaine des modifications demeure obligatoire. Les automatisations de configuration sont limitées à ce laboratoire et les opérations sensibles nécessitent des confirmations.

**Créer des Issues, passer la CI ou produire un rapport ne prouve pas une fonctionnalité EpiVerse développée.**
