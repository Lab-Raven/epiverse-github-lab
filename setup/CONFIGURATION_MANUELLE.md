# Actions manuelles indispensables pour terminer GitHub LAB

**Précondition :** dépôt `Lab-Raven/epiverse-github-lab` privé, GitHub CLI authentifié au compte autorisé. Ces étapes changent le dépôt du LAB, jamais celui de l'équipe.

## A. Priorité P0 : rendre le dépôt PRIVATE
- https://github.com/Lab-Raven/epiverse-github-lab/settings → **General → Danger Zone → Change repository visibility → Make private**.
- Alternative depuis un terminal déjà authentifié : `gh repo edit Lab-Raven/epiverse-github-lab --visibility private --accept-visibility-change-consequences`.
- Vérifier : `gh repo view Lab-Raven/epiverse-github-lab --json isPrivate --jq .isPrivate` retourne `true`.
- Important : rendre privé n'efface pas une exposition passée ; examiner historique, forks, liens et secrets éventuellement publiés.

## B. Finaliser Projects v2 pour l'organisation
```bash
gh auth status
gh auth refresh -s project
git clone https://github.com/Lab-Raven/epiverse-github-lab.git
cd epiverse-github-lab
# Tant que la PR #35 n’est pas fusionnée : utiliser sa branche de configuration.
git fetch origin fix/lab-raven-org-migration
git switch fix/lab-raven-org-migration
bash scripts/setup_projects.sh --dry-run
bash scripts/setup_projects.sh --apply
```
- Ouvrir https://github.com/orgs/Lab-Raven/projects et vérifier que le Project est **PRIVATE**.
- Compléter les 10 vues et champs `Status`, `Iteration` dans l'interface (voir `setup/PROJECTS_VUES.md`).

## C. Labels, milestones et paramètres
```bash
python3 scripts/bootstrap_lab.py --dry-run
python3 scripts/bootstrap_lab.py --apply
bash scripts/setup_repo_features.sh --dry-run
bash scripts/setup_repo_features.sh --apply
```
- Contrôler `Settings → Actions → General` et `Settings → Rules`. Sur un dépôt privé GitHub Free, l'application des rulesets de branche peut demander un abonnement Pro/Team/Enterprise ; ne pas souscrire sans décision.
- **Discussions** et **Wiki** sont activés au niveau du dépôt lors de l'audit du 5 novembre ; créer une catégorie et un sujet de test, puis une page Wiki, sans données internes.
- Vérifier `Settings → Code security` (Dependabot alerts, secret scanning, CodeQL selon plan). Ne pas activer de facturation supplémentaire automatiquement.

## D. Tester le cycle de vie
- PR → CI verte → revue par un compte différent (seulement si invité avec consentement) → merge → fermeture de l'Issue.
- Vérifier `Actions`, `Insights`, `Security`, `Releases` et les artefacts de rapport.
- Pour Codespaces : `Code → Codespaces → Create codespace on main`, mesurer la consommation, supprimer après essai.
- Tester une release **DRAFT** du LAB uniquement après contrôles ; aucun déploiement ni GHCR public.
- Ne pas activer Pages sur ce LAB privé ; une vitrine publique doit être un dépôt séparé, après sélection de contenus publiables.

## E. Équipe et droits
- Organisation : https://github.com/organizations/Lab-Raven/settings/profile
- Teams : https://github.com/orgs/Lab-Raven/teams
- Décider des équipes de test `product`, `frontend`, `backend`, `data`, `platform-security`, `qa`, puis créer avec des rôles minimaux. **Ne pas ajouter les vrais membres** avant confirmation de leurs comptes et de leur consentement.
- Relire `docs/governance/TEAM.md` et `docs/governance/RACI.md` avant toute décision sur l'équipe réelle.

## F. Critères de recette
L'ensemble est prêt seulement lorsque les réglages privés, le Project, les champs/vues, les tickets, les revues, les alertes de sécurité et les runs CI ont été **observés**, et non seulement documentés. Consigner les preuves dans `docs/quality/EVIDENCE.md`.
