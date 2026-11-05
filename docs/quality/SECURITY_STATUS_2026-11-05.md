# État de la sécurité GitHub LAB — mise à jour du 5 novembre 2026

Provenance : paramètres **Advanced Security** transmis par la propriétaire et vérification GitHub via le connecteur lorsque les API accessibles le permettent.

| Fonction | Nouvel état observé | Confiance / limite |
|---|---|---|
| Dépôt privé | **NON : dépôt PUBLIC** | GitHub API `visibility=public` |
| GitHub Project #1 | PRIVATE | Paramètre transmis par la propriétaire |
| Dépendances / Dependency graph | ON | Capture de paramètres |
| Automatic dependency submission | ON | Capture de paramètres |
| Dependabot alerts | ON | Capture de paramètres, modifié depuis l'audit initial |
| Malware alerts | ON | Capture de paramètres |
| Dependabot security updates | ON | Capture de paramètres |
| Grouped security updates | ON | Capture de paramètres |
| Version updates | Configurées dans dependabot.yml | PR de version ouvertes |
| CodeQL Default setup | ON ; scan initial affiché | Configuration et run `CodeQL Setup` success via API |
| Copilot Autofix | ON | Capture de paramètres |
| Code scanning dismissal restrictions | ON | Capture de paramètres |
| Secret Push Protection | ON | Capture de paramètres |
| Secret scanning alerting | **NON CONFIRMÉ** | Push protection `On` n'atteste pas que toutes les alertes secrets sont actives |
| Private vulnerability reporting | NON CONFIRMÉ | La nouvelle capture ne montre pas de valeur claire |
| Branche main protégée | NON | API `protected=false` |

## Actions encore nécessaires

1. Rendre le dépôt **PRIVATE**. Une éventuelle restriction d'offre sur CodeQL/Secret Protection en privé doit être examinée, pas contournée.
2. Vérifier et conserver des captures de `Secret scanning alerts`, `Private vulnerability reporting`, du tableau CodeQL et de ses résultats.
3. Protéger `main` par ruleset si possible avec le forfait de l'organisation et tester le rejet d'une PR non conforme.
4. Maintenir des revues de sécurité humaines sur les PR Dependabot ; aucune mise à jour majeure fusionnée automatiquement.
5. Rejouer `LAB - Privacy gate` après la modification de visibilité, puis vérifier tous les contrôles sur la PR #36.

Ne pas considérer un contrôle activé comme une preuve d'absence de vulnérabilités.
