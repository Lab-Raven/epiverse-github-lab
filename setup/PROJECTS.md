# Project GitHub nº 1 — privé, lié à un LAB public

Projet existant : [EpiVerse — LAB privé (non officiel)](https://github.com/orgs/Lab-Raven/projects/1), propriétaire Lab-Raven, **Private**.

**Ne pas créer de Project supplémentaire.** Les Issues importées depuis le repository public restent publiques.

## Champs à tester

| Champ | Type | Valeurs |
|---|---|---|
| Status | Sélection native | Backlog, Ready, In progress, Review, Testing, Blocked, Done |
| Priority | Sélection | P0, P1, P2, P3 |
| Type | Sélection | Feature, Task, Bug, Risk, Documentation, Research, Decision |
| Workstream | Sélection | Product, Frontend, Backend, Campus 2.5D, Data, AI, Infra, Security, UX, QA, Governance |
| Validation | Sélection | Not reviewed, In review, Accepted, Rejected |
| Iteration | Itération native | Sprints de démonstration, durée configurable |
| Start date / Target date | Date | A renseigner lors de l'exercice |
| Estimate (h), Actual (h), ETC (h) | Nombre | Données fictives explicites |
| Requirement ID, WBS ID, Evidence URL | Texte | Références LAB uniquement |

## Vues

Portfolio, Backlog, Kanban, Sprint, Roadmap, Par domaine, Par assignee, Risques, QA, Preuves, Pédagogie.

Créer une vue Table, Board ou Roadmap depuis l'interface du Project. Les vues de l'onglet Issues (**Issues Views**) sont distinctes.

## Automatisation

Après authentification GitHub CLI avec le scope `project` :

```bash
bash scripts/setup_projects.sh --dry-run
bash scripts/setup_projects.sh --apply
```

Le script limite la cible au Project existant n° 1, le maintient PRIVATE, y ajoute les champs puis les tickets LAB. Il ne peut pas remplir les vues privées avec des données confidentielles : les sources Issues restent publiques.
