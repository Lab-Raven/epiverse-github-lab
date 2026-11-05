# EpiVerse — GitHub LAB privé

> **LABORATOIRE NON OFFICIEL — DONNÉES FICTIVES.** Ce dépôt **ne représente pas** l'avancement de l'application EpiVerse.

**But :** valider les outils GitHub de gouvernance et de suivi pédagogique, sans modifier le dépôt officiel `epiverse-epitech/epiverse`.

- Propriétaire du LAB : `@estellegiroud` ; aucun autre membre invité.
- Le dépôt reste **PRIVATE**. Aucun secret, Pages publiques, package publié ni déploiement.
- Les neuf noms et responsabilités de `docs/governance/TEAM.md` sont **provisoires** ; seule la direction exclusive par Estelle et le rôle non managérial de Soumia ont été réconciliés.
- **GitHub Projects** est la source de vérité souhaitée pour les tests ; le Project privé doit être créé séparément via l'interface.

## Navigation rapide

| Domaine | Accès |
|---|---|
| Tickets de démonstration | [Issues](../../issues) |
| PR de traçabilité (brouillon) | [PR #6](../../pull/6) |
| Tests et rapports | [Actions](../../actions) |
| Blocage Actions constaté | [Issue #7](../../issues/7) |
| Membres / gouvernance | [TEAM](docs/governance/TEAM.md) et [RACI](docs/governance/RACI.md) |
| Décisions | [Registre](docs/governance/DECISIONS.md), [ADR](docs/adr/0001-github-projects.md) |
| Livraisons et critères | [DoD](docs/quality/DoD.md), [preuves](docs/quality/EVIDENCE.md) |
| Tableau GitHub Projects | [Configuration et champs](setup/PROJECTS.md) |
| Matrice fonctionnelle GitHub | [Fonctions et limites](setup/GITHUB_FEATURES.md) |
| Critères de recette | [Checklist](setup/CRITERES_ACCEPTATION.md) |
| Transfert contrôlé | [Procédure](setup/TRANSFERT_OFFICIEL.md) |

## Initialisation du tableau Projects (interface)

1. Ouvrir https://github.com/users/estellegiroud/projects.
2. New Project → Table → titre **EpiVerse — LAB privé (non officiel)**.
3. Vérifier que la visibilité du Project est **Private** (indépendante de celle du dépôt).
4. Ajouter les Issues du LAB, configurer les champs, itérations et vues selon `setup/PROJECTS.md`.
5. Ne pas importer le backlog Jira/Notion ou les Issues du dépôt officiel avant rapprochement et accord.

## Initialisation des labels et milestones

Le workflow manuel **LAB - Initialiser labels et jalons** est prévu pour les créer, et seulement dans ce dépôt privé. Il exige l'autorisation GitHub Actions et l'accord pour l'exécuter. Le script `scripts/bootstrap_lab.py` fournit une alternative GitHub CLI locale avec confirmation explicite.

## CI / rapport de suivi — état vérifié au 5 novembre 2026

Les fichiers de workflow et les tests sont présents ; **GitHub Actions ne démarre pas actuellement les jobs** :

- [Run de CI avec échec au démarrage](../../actions/runs/42054311630)
- [Run du workflow minimal avec le même problème](../../actions/runs/42054951761)
- Signature observée : `startup_failure`, `BuildFailed`, **0 job**, aucun log de test.

La cause exacte n'est **pas prouvée**. Vérifier d'abord [Settings → Actions → General](../../settings/actions) et [Billing & Licensing](https://github.com/settings/billing), puis contacter GitHub Support si nécessaire. Il ne faut pas déclarer les tests CI comme réussis tant qu'un run n'a pas été exécuté.

## Tests locaux (sans secret)

```bash
python3 scripts/verify_lab.py
python3 -m unittest discover -s tests -v
python3 scripts/generate_report.py --demo --output reporting/demo-status.md
python3 scripts/bootstrap_lab.py --dry-run
```

Les rapports `--demo` contiennent **uniquement des données fictives**. Le rapport `--github` est bloqué sur le seul dépôt `estellegiroud/epiverse-github-lab`.

## Prochaines preuves à obtenir

- [ ] Actions : job minimal et tests Python réellement exécutés sur GitHub.
- [ ] Labels/jalons configurés, couleurs vérifiées.
- [ ] Project v2 privé avec vues Kanban, Sprint, Roadmap, Risques et Pédagogie.
- [ ] PR #6 revue (une revue indépendante nécessite un autre compte accepté).
- [ ] Rapport Actions produit sur données LAB, et artefact accessible.
- [ ] Tests des fonctions Discussions, Security, Releases et Insights selon autorisations.
- [ ] Aucune opération sur le dépôt d'équipe sans **autorisation écrite distincte**.
