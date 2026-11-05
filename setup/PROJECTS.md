# GitHub Projects v2 — spécification du tableau privé

Projet de test : `EpiVerse — LAB privé (non officiel)`, propriétaire `estellegiroud`, visibilité **PRIVATE**.

## Champs proposés
| Champ | Type | Valeurs / consignes |
|---|---|---|
| Status | Single select | Backlog, Ready, In progress, Review, Testing, Blocked, Done |
| Priority | Single select | P0 critique, P1 haute, P2 normale, P3 basse |
| Type | Single select | Feature, Task, Bug, Risk, Documentation, Research, Decision |
| Workstream | Single select | Product, Frontend, Backend, Campus 2.5D, Data, AI, Infra, Security, UX, QA |
| Iteration | Iteration | Cycles de deux semaines, dates non officialisées |
| Start date | Date | Début prévu |
| Target date | Date | Date cible |
| Estimate (h) | Number | Charge initiale |
| Actual (h) | Number | Heures constatées |
| ETC (h) | Number | Estimate to complete, jamais déduit naïvement |
| Requirement ID | Text | LAB-REQ-001 |
| WBS ID | Text | LAB-WBS-1.1 |
| Evidence URL | Text | PR, commit, exécution CI, test |

Assignee est un champ natif des Issues : ne pas le recréer. Ne pas lier automatiquement un compte GitHub à un membre sans validation.

## Vues à tester
1. **Portfolio** : toutes les tâches, priorités, owners, charges et échéances.
2. **Board** : Kanban par Status ; filtre Workstream.
3. **Sprint** : itération courante, blocages et charge prévue/constatée.
4. **Par membre** : regroupement Assignee (des exemples peuvent rester non attribués).
5. **Roadmap** : chronologie dates de début/fin ; dépendances à documenter.
6. **Risques** : Type=Risk ou label type:risk, revue, owner et plan de réponse.
7. **Pédagogie** : livrables validés, preuves, écarts, ETC, décision prochaine période.

## Automatisations
Nouvelle Issue → Backlog. PR liée → Review (contrôler manuellement). Issue fermée → Done **seulement** après preuve/validation ; sinon conserver une étape de recette explicite.

## Interface (non accessible au connecteur GitHub actuel)
1. https://github.com/orgs/Lab-Raven/projects → **New project** → table → **Private**.
2. Configurer les champs et vues, dans la limite des capacités du plan.
3. Ajouter les Issues LAB du dépôt, sans importer les tickets de l'organisation.
4. Tester vue lecture seule et export des preuves.
5. Confirmer indépendamment la confidentialité du Project.
