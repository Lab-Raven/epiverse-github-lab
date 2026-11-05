# Protéger main — ruleset public GitHub Free

GitHub Free permet des rulesets de **branche sur les dépôts publics**. En revanche, le mode `Evaluate` peut être réservé à GitHub Enterprise. Utiliser `Disabled` puis `Active` sur ce LAB.

## Configuration proposée

| Paramètre | Valeur |
|---|---|
| Ruleset name | LAB — main protected |
| Target | Branch `main` / DEFAULT_BRANCH |
| Enforcement au départ | **Disabled** |
| Restrict deletions | Oui |
| Block force pushes | Oui |
| Require a pull request before merging | Oui |
| Required approvals | 0 tant qu'aucun relecteur indépendant n'a été invité |
| Require status checks | Oui, les 5 contextes ci-dessous |
| Require branches up to date | Oui, après contrôle du comportement |
| Require conversation resolution | Oui |

### Noms des checks observés dans GitHub Actions
`validate`, `policy`, `scan`, `secret-guard`, `public-lab`.

GitHub peut afficher des noms plus complets selon les workflows ; choisir les checks **réellement présents dans la liste de l'interface**. Ne pas inventer de nom de job et ne pas forcer une option dont la source GitHub App n'est pas reconnue.

## Installation guidée

```bash
bash scripts/setup_ruleset.sh --dry-run
bash scripts/setup_ruleset.sh --apply
```

Le script crée uniquement le ruleset `Disabled` via l'API GitHub avec des permissions administrateur ; il ne l'active pas. Une alternative consiste à ouvrir `Settings → Rules → New ruleset → New branch ruleset` et recopier la configuration.

## Validation avant activation

1. Tester une PR avec tous les jobs verts et conserver la preuve.
2. Tester une PR de démonstration sans lien Issue (le job `policy` doit échouer).
3. Vérifier qu'une PR peut être fusionnée par un utilisateur autorisé, sans relecteur impossible à obtenir.
4. Mettre `Enforcement: Active` seulement quand le fonctionnement est confirmé.
5. Vérifier le rejet des pushes directs et des force-pushes sur `main`.

Ne jamais créer de règles qui rendent `main` inaccessible aux seuls administrateurs du LAB sans procédure de retour arrière.
