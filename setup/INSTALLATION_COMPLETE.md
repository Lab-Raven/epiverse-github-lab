# Installation et test du LAB public

**Cible unique :** `Lab-Raven/epiverse-github-lab`, PUBLIC intentionnellement. Project de pilotage existant n° 1 : **PRIVATE**. Dépôt de l'équipe `epiverse-epitech/epiverse` exclu.

## Prêt dans le dépôt
Issues fictives, labels, templates, PR, CODEOWNERS, Dependabot, CodeQL natif activé, workflows CI/SAST/sécurité/rapports, documentation, page Wiki Home, annonce Discussions et scripts de test.

## Via GitHub CLI (macOS)
```bash
brew install gh jq
gh auth login
gh auth refresh -s project
gh repo clone Lab-Raven/epiverse-github-lab
cd epiverse-github-lab
bash scripts/complete_lab.sh --dry-run
bash scripts/complete_lab.sh --apply
```

Le script teste le dépôt cible et guide l'installation des labels et jalons, l'import des Issues fictives dans **le Project n° 1 existant**, la création d'équipes de simulation vides et d'un environnement factice. Il demande des confirmations. Ne pas coller de token dans un chat.

## Fonctionnalités à configurer dans l'interface
- GitHub Project : champs, itérations, vues Kanban, Portfolio, Sprint et Roadmap.
- Issues Views : au moins une vue privée et une vue partagée sans information réelle.
- Branch ruleset : `main`, d'abord Evaluate puis Active.
- Wiki : remplacer le texte erroné `dépôt privé` dans Home et ajouter la Sidebar.
- GitHub Pages : source GitHub Actions puis workflow manuel de vitrine fictive.
- Releases : brouillon du LAB seulement ; packages GHCR facultatifs après contrôle de visibilité/coûts.
- Security : vérifier les résultats CodeQL/Dependabot/Secret Scanning, non simplement les boutons.
- Codespaces et Teams : contrôler les quotas et créer des équipes vides uniquement.

## Risque historique
Les premières versions publiques ont mentionné des noms réels. Les commits passés demeurent accessibles ; aucune réécriture destructive de l'historique n'est engagée ici. Voir `docs/security/PUBLIC_HISTORY_REVIEW.md`.
