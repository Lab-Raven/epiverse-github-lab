# Guide de création des vues GitHub Projects

Une fois le Project privé créé par `scripts/setup_projects.sh`, ouvrir sa page.

| Vue | Layout | Filtre et regroupement |
|---|---|---|
| 01 — Portfolio | Table | Toutes les Issues, colonnes Priority, Status, Assignee, Workstream, Target date, ETC |
| 02 — Backlog | Table | Status=Backlog ou Ready ; tri Priority |
| 03 — Kanban | Board | Regroupement Status ; masquer Done si nécessaire |
| 04 — Sprint | Table/Board | Itération courante ; Status et Assignee |
| 05 — Répartition équipe | Table | Regroupement Assignee ; données fictives d'exemple uniquement |
| 06 — Roadmap | Roadmap | Start date à Target date ; jalons simulés |
| 07 — Risques | Table | Type=Risk ou label type:risk |
| 08 — QA / revue | Table | Status=Review, Testing ou Blocked |
| 09 — Pédagogie | Table | Evidence URL, WBS ID, ETC (h), Issue, PR |
| 10 — Livraisons | Table | Issues fermées et preuves vérifiées, tri Target date |

## Statut et automatisation
L'automatisation native peut faire passer une Issue à Done à sa fermeture. **Ce n'est pas synonyme d'acceptation par le Product Owner.** Maintenir le champ de recette distinct et vérifier les preuves.

## Mesures
La somme des issues fermées est une mesure d'activité, pas un % produit. Compter comme livré seulement un incrément accepté sur des critères de couverture préétablis.

## Retour de test
Documenter avec une capture de vue et les propriétés configurées dans `reporting/weekly-template.md`, sans exposer l'équipe réelle.
