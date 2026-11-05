# Dictionnaire de KPI — aucun chiffre sans provenance

| Mesure | Formule / source | Limite |
|---|---|---|
| Issues ouvertes | GitHub API issues, PR exclues | activité, pas avancement produit |
| Issues fermées | `state=closed` | pas nécessairement acceptées |
| PR fusionnées | `merged_at` non nul | un merge ne garantit pas la DoD |
| Lead time PR | `merged_at - created_at` | dépend du périmètre et de l'attente |
| Cycle time | In Progress → accepté | nécessite dates de statut traçables |
| WIP | tickets par état actif | à comparer à la capacité de l'équipe |
| Blockers | étiquette `status:blocked` | dépend de l'hygiène de saisie |
| Charge initiale | champ Estimate (h) | estimation humaine |
| Réalisé | champ Actual (h) | déclaré, jamais estimé depuis les commits |
| ETC | champ ETC (h) | réestimé chaque revue |
| EAC | Actual + ETC | à périmètre stable |
| Couverture exigence | exigences avec preuves / exigences retenues | nécessite référentiel défini |
| Taux de tests | résultats d'exécutions réelles | un workflow qui ne démarre pas = pas testé |
| PDR | ajustements non prescrits / actions prescrites × 100 | protocole figé par tentative |

**Différencier** conçu, développé, revu, testé, livré, accepté. Ne jamais afficher un pourcentage global arbitraire.
