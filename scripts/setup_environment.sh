#!/usr/bin/env bash
# Environnement de validation factice, aucun secret et aucune production.
set -euo pipefail
REPO="Lab-Raven/epiverse-github-lab"
MODE="${1:---dry-run}"
[[ "$MODE" == "--dry-run" || "$MODE" == "--apply" ]] || { echo "Usage: bash scripts/setup_environment.sh --dry-run|--apply"; exit 2; }
echo "LAB : création potentielle de l'environnement lab-simulation, sans déploiement."
[[ "$MODE" == "--apply" ]] || exit 0
command -v gh >/dev/null
[[ "$(gh api "repos/$REPO" --jq '.full_name')" == "$REPO" ]] || { echo "Dépôt inattendu"; exit 3; }
[[ "$(gh api user --jq '.login')" == "estellegiroud" ]] || exit 4
printf 'Taper ENV LAB : '
read -r answer
[[ "$answer" == "ENV LAB" ]] || exit 5
gh api --method PUT "repos/$REPO/environments/lab-simulation" >/dev/null
echo "Environnement factice créé ; vérifier Settings → Environments."
