#!/usr/bin/env bash
# Crée UNIQUEMENT une proposition de ruleset DISABLED pour la branche main du LAB.
set -euo pipefail
REPO="Lab-Raven/epiverse-github-lab"
MODE="${1:---dry-run}"
if [[ "$MODE" != "--dry-run" && "$MODE" != "--apply" ]]; then
  echo "Usage: bash scripts/setup_ruleset.sh --dry-run|--apply" >&2
  exit 2
fi
cd "$(dirname "$0")/.."
python3 -m json.tool setup/main-ruleset.json >/dev/null
echo "Ruleset ciblé : $REPO / main / Disabled, requiert PR + 5 checks et bloque force-push/deletion après activation."
if [[ "$MODE" == "--dry-run" ]]; then
  echo "DRY-RUN : aucun changement ; vérifier manuellement les noms des checks avant activation."
  exit 0
fi
command -v gh >/dev/null || { echo "GitHub CLI requis"; exit 3; }
[[ "$(gh api "repos/$REPO" --jq '.full_name')" == "$REPO" ]] || { echo "Repo inattendu"; exit 4; }
[[ "$(gh api user --jq '.login')" == "estellegiroud" ]] || { echo "Compte inattendu"; exit 5; }
existing="$(gh api "repos/$REPO/rulesets" --jq '.[] | select(.name == "LAB — main protected") | .id' | head -n 1)"
if [[ -n "$existing" ]]; then
  echo "Ruleset existant #$existing : ne pas écraser sa configuration."
  exit 0
fi
printf 'Taper CREER REGLE DESACTIVEE LAB : '
read -r answer
[[ "$answer" == "CREER REGLE DESACTIVEE LAB" ]] || { echo "Annulé"; exit 6; }
gh api --method POST "repos/$REPO/rulesets" --input setup/main-ruleset.json --jq '{id, name, enforcement, target}'
echo "Règle créée DISABLED. Vérifier les noms des checks et la disponibilité d'une fusion avant de l'activer dans Settings → Rules."
