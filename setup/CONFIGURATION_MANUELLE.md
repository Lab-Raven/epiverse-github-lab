# Configuration restante — GitHub LAB public

## État vérifié (5 novembre 2026)

- **Repository** : `Lab-Raven/epiverse-github-lab` en **PUBLIC par choix**, pour tester les fonctionnalités GitHub Free.
- **Project de l'organisation #1** : `EpiVerse — LAB privé (non officiel)`, **PRIVATE**, actuellement vide ; ne pas en créer un autre.
- **Discussions** : première annonce `[LAB] Bienvenue — règles, idées et suivi` créée et épinglée.
- **Wiki** : première page Home créée ; son contenu indique encore à tort que le dépôt doit être privé.
- **GitHub Security** : Dependabot alerts, CodeQL, private vulnerability reporting et secret scanning alerts affichés **Enabled** ; Push Protection activée.
- **Branche main** : aucune protection/ruleset observé.
- **Labels** : 32 labels, à compléter/normaliser ; **Milestones : 0** ; **Issues Views : 0**.
- **PR #36** : corrige la politique de publication et la compatibilité du LAB public ; ne pas fusionner avant succès de ses contrôles.

Le Project PRIVATE ne masque pas ses Issues/PR provenant du dépôt PUBLIC. Ne pas mettre d'informations secrètes dans les tickets.

## A. GitHub Project #1 — automatisation et vues

Lien : https://github.com/orgs/Lab-Raven/projects/1

Le script `scripts/setup_projects.sh --apply` réutilise **uniquement le Project #1** : titre, README, visibilité PRIVATE, lien au dépôt, champs et import des tickets du LAB. Il n'est pas accessible à l'application GitHub intégrée de ce chat ; exécuter depuis GitHub CLI avec le scope `project`.

```bash
brew install gh jq
gh auth login
gh auth refresh -s project
gh repo clone Lab-Raven/epiverse-github-lab
cd epiverse-github-lab
bash scripts/complete_lab.sh --dry-run
bash scripts/complete_lab.sh --apply
```

Après exécution, créer les vues Table / Board / Roadmap dans l'interface : Portfolio, Backlog, Kanban, Sprint, Roadmap, Par domaine, Par membre **fictif uniquement**, Risques, QA, Preuves, Pédagogie. Les options `Status` et `Iteration` natives doivent être réglées manuellement.

## B. Labels et Milestones

Dans **Actions → LAB - Initialiser labels et jalons → Run workflow** (workflow disponible après fusion de PR #36), déclencher manuellement. Il synchronise les labels et crée trois jalons fictifs :

- [LAB] Sprint 0 — gouvernance
- [LAB] Sprint 1 — qualité et PR
- [LAB] Recette pédagogique

Aucune date n'est inventée. Alternative locale : `python3 scripts/bootstrap_lab.py --apply`.

## C. Branch protection / Rulesets — public GitHub Free

https://github.com/Lab-Raven/epiverse-github-lab/settings/rules

Créer un **Branch ruleset** pour la branche `main`, après l'intégration du kit :
- Ruleset name : `LAB — main protected`
- Enforcement : `Disabled` pour commencer, puis `Active` après tests (mode Evaluate réservé à certaines offres Enterprise).
- Target branches : `main`.
- Restrict deletions et block force pushes.
- Require pull request before merging, dismiss stale approvals lorsque des relecteurs existent.
- Require status checks : sélectionner les noms **exacts** depuis les checks d'une PR réussie.
- Ne pas exiger deux approbations si seul un compte humain dispose des droits nécessaires : cela bloquerait toute fusion.
- Vérifier sur une PR de test que les contrôles s'appliquent ; ne pas rendre la règle Active sans voie de déblocage.

## D. Security

https://github.com/Lab-Raven/epiverse-github-lab/settings/security_analysis

**Déjà activés sur les derniers écrans** : Dependabot alerts, malware alerts, security updates, grouped updates, CodeQL default setup, Copilot Autofix, Push Protection ; dans Security Overview : Private vulnerability reporting, code scanning et secret scanning alerts Enabled.

À vérifier désormais : findings réelles, sévérité, permissions, alertes à traiter, et état de `Code quality findings` (encore désactivé). **Ne pas activer des options facturables sans vérifier les conditions.**

## E. Discussions et Wiki

- Discussions : https://github.com/Lab-Raven/epiverse-github-lab/discussions — l'annonce d'accueil est **déjà publiée** et épinglée ; ne pas en créer de doublon.
- Wiki : https://github.com/Lab-Raven/epiverse-github-lab/wiki — page **Home déjà créée**, remplacer le texte qui indique `dépôt privé` par `LAB public / données fictives`. Contenu corrigé : `wiki-content/Home.md`. Script `bash scripts/publish_wiki.sh --apply` pour synchroniser Home et Sidebar via le dépôt Git Wiki.

## F. Tester Pages, Releases, Docker, GHCR et environnement

- Pages : mettre `Settings → Pages → Source: GitHub Actions` ; déclencher le workflow manuel de démonstration après validation. Le site sera **PUBLIC**.
- Releases : tester `LAB - Préparer une release brouillon`, jamais publier une version du produit EpiVerse.
- Docker : tester `LAB - Tester Docker sans publication`, confirmation `LAB_BUILD`.
- GHCR : ne pas publier automatiquement ; un package peut avoir une visibilité indépendante et des coûts de stockage.
- Environments : `scripts/setup_environment.sh --apply` prépare `lab-simulation`, sans serveur, clé ni déploiement.
- Teams : `scripts/setup_teams.sh --apply` peut créer des équipes **vides** ; aucune invitation aux membres réels.
- Codespaces : `Code → Codespaces → Create a codespace` pour vérifier le devcontainer ; surveiller la consommation.

## G. Vérifications et confidentialité historique

Les anciens commits et une Issue publique ont mentionné des membres réels. **Les changements dans les fichiers courants n'effacent pas l'historique Git, les caches, forks ni copies externes.** Évaluer séparément la nécessité d'une réduction d'exposition, sans `push --force` sans validation expresse.

Ne jamais coller de PAT, clé ou document interne dans ce dépôt ou dans une discussion publique. Pour des données réelles, préférer exclusivement le dépôt officiel privé et un Project privé à accès validé.

### Ruleset sur GitHub Free

Après fusion du correctif, `bash scripts/setup_ruleset.sh --apply` crée une règle **Disabled** visant `main`. Les cinq checks réels sont `validate`, `policy`, `scan`, `secret-guard` et `public-lab`. Activer dans Settings → Rules après test, sans imposer de relecteur inexistant. Voir `docs/operations/RULESET_MAIN.md`.
