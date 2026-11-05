# Plan de validation GitHub LAB

| Test | Préparation | Résultat vérifiable |
|---|---|---|
| Confidentialité | repo PRIVATE et Project PRIVATE | lecture des deux paramètres |
| Formulaire | Issue Feature/Task/Bug/Risk/Decision | champs et labels correctement enregistrés |
| Branche / PR | PR #6 liée à Issue #1 | référence `Closes #1`, diff et checks |
| CI | workflow minimal | **job réellement exécuté**, résultat visible |
| Lint / tests | scripts Python | sortie unittest + artefact |
| Dépendances | Dependabot Github Actions | PR réellement générée si mise à jour |
| CODEOWNERS | changement README | relecteur différent de l'auteur, lorsque disponible |
| Protections | tentative PR sans check | fusion refusée si fonctionnalité du forfait |
| Projects | champs, vues et itération | vue ouverte + affectation ticket |
| Risk management | Issue de risque | responsable, mitigation, échéance, preuve |
| Reporting | workflow dispatch | tableau du LAB, horodatage et artifact |
| Release | brouillon interne | tag/pre-release, changelog, tests |
| Wiki/Discussions | activation puis essai | contenu test visible uniquement aux autorisés |
| Packages | image de test privée | visibility et absence de secrets, si test décidé |
| Insights | commits/PR de LAB | historique de contribution, **non extrapolé** |
| Finances | quota Actions/Storage | vérification manuelle sans achat automatique |

**Bloquant observé :** Actions ne démarre actuellement aucun job (Issue #7) ; les tests locaux ne compensent pas une CI sur GitHub.
