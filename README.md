# EpiVerse — GitHub Governance LAB (non officiel)

> **ENVIRONNEMENT DE TEST.** Ce dépôt sert à tester GitHub, pas à héberger ni à livrer l'application EpiVerse. Les scénarios et métriques de démonstration sont fictifs. **Ne jamais synchroniser ou pousser vers `epiverse-epitech/epiverse`.**

## Confidentialité : priorité absolue

**Contrôle API du 5 novembre 2026 : dépôt PUBLIC.** Le laboratoire était censé être privé. Avant de renseigner la moindre information supplémentaire sur des personnes, du code non public ou des activités internes, passer ce dépôt en **PRIVATE** :

[Paramètres du dépôt → General → Danger Zone → Change repository visibility](../../settings)

La confidentialité réelle doit être **recontrôlée dans GitHub**. Ne pas ajouter de secrets, tokens, dossiers RH, livrables internes ou exports Jira/Notion dans ce dépôt tant qu'il est public.

## Avancement vérifié

| Composant | État |
|---|---|
| Repository / Git / branches | Disponible, dépôt dans l'organisation Lab-Raven |
| Issues et labels | Tickets d'essai créés, aucune réalisation de produit prétendue |
| Pull Requests | [PR de démonstration #6](../../pull/6), puis PR de migration de configuration |
| GitHub Actions | CI Python, contrôle documentaire et test minimal **exécutés avec succès** après les échecs initiaux |
| Politique PR | Correctif de migration en cours : anciennes références de dépôt |
| Dependabot | Configuration active, PR de mise à jour d'Actions créées |
| Discussions et Wiki | Options activées au niveau du repository ; contenus à organiser |
| Projects v2 | Projet et vues d'organisation à créer ou vérifier séparément |
| Milestones et champs | Scripts d'initialisation prévus ; activation effective à vérifier |
| Teams et permissions | Dépendent de l'organisation, aucune attribution de rôle à une personne non confirmée |
| Rulesets, sécurité native | À activer/éprouver selon forfait et confidentialité du dépôt |

Pour l'état précis et les preuves, consulter [Actions](../../actions), [Issues](../../issues), [PR](../../pulls) et [matrice de couverture](setup/FEATURE_COVERAGE.md).

## Dossiers

- [Gouvernance et RACI provisoire](docs/governance/TEAM.md)
- [Décisions](docs/governance/DECISIONS.md)
- [Exigences d'exemple](docs/product/SCOPE.md)
- [Tests, DoD et preuves](docs/quality/DoD.md)
- [Sécurité et incidents](docs/security/THREAT_MODEL.md)
- [Pilotage Projects](setup/PROJECTS.md)
- [Vues Kanban, sprints, roadmap, qualité](setup/PROJECTS_VUES.md)
- [Guide de configuration globale](setup/INSTALLATION_COMPLETE.md)
- [Critères de recette](setup/CRITERES_ACCEPTATION.md)
- [Plan de transfert après validation](setup/TRANSFERT_OFFICIEL.md)
- [Rapports, charges, ETC et Delta Log](reporting/README.md)

## Commandes de test (sans dépendance applicative)

```bash
python3 scripts/verify_lab.py
python3 -m unittest discover -s tests -v
python3 scripts/generate_report.py --demo --output reporting/demo-status.md
python3 scripts/bootstrap_lab.py --dry-run
bash scripts/setup_projects.sh --dry-run
```

**Pour configurer les Project/labels via CLI**, authentifier `gh` avec les droits adaptés puis utiliser les versions `--apply` **uniquement après confirmation de la visibilité privée**. Ne pas envoyer de jeton GitHub dans ChatGPT.

Les membres et les rôles présents dans les documents sont une **base provisoire à confirmer**, pas des identités GitHub, invitations ou responsabilités approuvées.
