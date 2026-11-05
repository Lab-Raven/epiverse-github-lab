# Contrôles de sécurité du LAB public

Les écrans les plus récents montrent **Private vulnerability reporting, Dependabot alerts, Code scanning alerts et Secret scanning alerts Enabled**, ainsi que Push Protection et CodeQL Default setup activés. Il ne s'agit pas d'une garantie de code sans vulnérabilités.

| Mesure | État | Vérification |
|---|---|---|
| Visibilité Repo | PUBLIC intentionnel | API GitHub |
| Project #1 | PRIVATE | Settings du Project |
| Branch rules | main non protégée | Settings → Rules |
| CODEOWNERS | Fichier présent | Revue humaine à tester |
| CI Python / SAST Bandit | Tests réussis sur #36 | Actions |
| CodeQL | Workflow réel réussi | Code scanning |
| Dependabot alerts / malware | Enabled | Security |
| Dependabot security/version updates | ON, PR ouvertes | Security et Pull Requests |
| Secret scanning alerts | Enabled | Security |
| Push Protection | ON | Advanced Security |
| Private vulnerability reporting | Enabled | Security |
| Code quality findings | Disabled | Vérifier l'option avant activation |
| Contrôle des publications | `public_lab_guard.py` et CI | Détection heuristique uniquement |
| Historique public | Anciennes références à des personnes | Revue humaine et éventuelle procédure dédiée |

Le dépôt ne doit contenir aucune donnée interne, même si CodeQL et la protection de secrets sont activés. Le Project PRIVATE ne masque pas les Issues/PR du dépôt public.
