# Installation complète du laboratoire GitHub

**Cible unique :** `estellegiroud/epiverse-github-lab` (PRIVÉ). **Jamais** le dépôt officiel EpiVerse.

## Étapes automatiques déjà réalisées par le connecteur
- Dépôt contrôlé privé ; documentation, gouvernance et RACI provisoire.
- Issue forms, templates de PR, CODEOWNERS, Dependabot, workflows Actions.
- Issues factices 1 à 5 + incident réel du LAB #7 ; PR #6 en brouillon.
- Labels de classification présents sur les tickets d'essai (couleur GitHub par défaut).

## Étapes possibles avec un terminal connecté à GitHub
Les commandes ci-dessous se font sur ton ordinateur, avec TON authentification. Aucun jeton à transmettre au chat.

```bash
# macOS (si GitHub CLI absent)
brew install gh jq
gh auth login
gh auth status
gh auth refresh -s project
git clone git@github.com:estellegiroud/epiverse-github-lab.git
cd epiverse-github-lab

# Prévisualiser et exécuter le bootstrap des labels/jalons
python3 scripts/bootstrap_lab.py --dry-run
python3 scripts/bootstrap_lab.py --apply

# Créer automatiquement le Project V2 privé, ses champs et rattacher les issues
bash scripts/setup_projects.sh --dry-run
bash scripts/setup_projects.sh --apply

# Activation volontaire des fonctions du seul dépôt privé
bash scripts/setup_repo_features.sh --dry-run
bash scripts/setup_repo_features.sh --apply
```

## Étapes UI indisponibles au connecteur actuel
- **GitHub Projects** : personnaliser les vues (Board, Sprint, Roadmap, Risques, Pédagogie) et les automations, car GitHub CLI ne gère pas toutes les vues/iterations.
- **Settings → Actions → General** : diagnostiquer `startup_failure` avec aucun job, voir Issue #7.
- **Settings → Billing & Licensing** : vérifier blocage de compte / consommation ; ne jamais rendre public pour contourner.
- **Settings → Branches / Rules** : configurer les protections seulement si forfait private compatible ; ne pas exiger une seconde personne dans ce dépôt individuel.
- **Settings → Security / Code security** : voir ce qui est inclus dans le forfait ; activer les contrôles gratuits ; ne pas accepter de facturation supplémentaire sans décision.
- **Discussions** : activer, catégoriser et publier un sujet d'essai, si option proposée.
- **Releases, Packages et Environments** : tests limités au LAB, pas de publication externe.

## Validation
Cocher `setup/CRITERES_ACCEPTATION.md` à partir d'exécutions et liens **réels**, jamais de captures fictives.
