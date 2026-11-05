# Paramètres cibles du LAB public

| Réglage | Cible | Validation |
|---|---|---|
| Repository visibility | PUBLIC, souhait explicite | API GitHub et UI |
| GitHub Project #1 | PRIVATE | Settings du Project |
| Issues | Activé, données fictives | Issues |
| Discussions | Activé, annonce épinglée | Discussions |
| Wiki | Activé, Home présente | Wiki |
| Actions | Actif, tests exécutés | Actions |
| Rulesets | Protection main pour dépôt public | Settings → Rules |
| Dependabot | Updates et alerts activées | Security |
| CodeQL | Default setup et scan réel | Security / Actions |
| Secret scanning | Alertes et Push Protection activées | Security |
| Pages | Site de démonstration public, option manuelle | Settings → Pages |
| Releases | Brouillons de test uniquement | Releases |
| Packages | Aucune publication par défaut | Packages |
| Auto-merge | Désactivé pour les agents et les PR risquées | Settings |
| Branch deletion | Suppression de branche après fusion, selon choix | Settings |
| CODEOWNERS | Propriétaire du LAB ; revue externe non simulée | Fichier + PR |
| Environments | `lab-simulation`, sans secret | Settings |
| Teams | Équipes fictives vides, pas de vrais membres | Organisation |
| Billing | Pas de souscription/achat automatique | Billing |

Un repository public peut rendre accessibles historique, Issues, discussions, Wiki et les artefacts publiés. Le Project privé ne protège pas le contenu source des Issues publiques.
