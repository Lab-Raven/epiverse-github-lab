#!/usr/bin/env bash
# Read-only, aucune modification de configuration ni de la facturation.
set -euo pipefail
REPO="estellegiroud/epiverse-github-lab"
command -v gh >/dev/null || { echo "Installer GitHub CLI" >&2; exit 1; }
[ "$(gh api user --jq '.login')" = "estellegiroud" ] || { echo "Mauvais utilisateur" >&2; exit 2; }
[ "$(gh api "repos/$REPO" --jq '.private')" = "true" ] || exit 3
echo "Repository Actions access:"
gh api "repos/$REPO/actions/permissions" --jq '{enabled: .enabled, allowed_actions: .allowed_actions}' || true
echo "GitHub Actions billing (compte privé) et settings à vérifier dans le navigateur."
echo "Derniers runs :"
gh run list -R "$REPO" --limit 12 --json databaseId,name,event,status,conclusion,workflowName,createdAt --jq '.[] | [.databaseId,.workflowName,.event,.conclusion,.createdAt] | @tsv'
echo "Problème consigné dans https://github.com/$REPO/issues/7"
echo "Une cause de facturation reste une hypothèse tant qu'elle n'est pas vérifiée dans le compte."
