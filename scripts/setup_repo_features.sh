#!/usr/bin/env bash
# Active seulement des fonctionnalités sans facturation et sans changement de visibilité.
set -euo pipefail
REPO="Lab-Raven/epiverse-github-lab"
MODE="$(printf '%s' "$1")"
if [ "$MODE" != "--apply" ] && [ "$MODE" != "--dry-run" ]; then
  echo "Usage: bash scripts/setup_repo_features.sh --dry-run|--apply" >&2; exit 2
fi
echo "CIBLE LAB : $REPO (public autorisé ; données fictives)"
if [ "$MODE" = "--dry-run" ]; then
  echo "DRY-RUN : activer Issues, Projects, Discussions ; essayer Wiki si compatible."
  echo "DRY-RUN : dépôt public intentionnel, aucun achat ou déploiement."
  exit 0
fi
command -v gh >/dev/null || { echo "gh absent" >&2; exit 3; }
[ "$(gh api user --jq '.login')" = "estellegiroud" ] || { echo "Identité inattendue" >&2; exit 4; }
[ "$(gh api "repos/$REPO" --jq '.full_name')" = "$REPO" ] || { echo "Dépôt différent" >&2; exit 4; }
printf "Taper ACTIVER LAB pour confirmer : "
read -r ANSWER
[ "$ANSWER" = "ACTIVER LAB" ] || { echo "Annulé"; exit 5; }
gh repo edit "$REPO" --enable-issues --enable-projects --enable-discussions
if gh repo edit "$REPO" --enable-wiki; then
  echo "Wiki activé."
else
  echo "Wiki indisponible avec ce compte/forfait ; documentation versionnée conservée."
fi
gh repo edit "$REPO" --delete-branch-on-merge
echo "LAB uniquement ; aucune visibilité modifiée."
echo "Fonctions activées. Vérifier l'interface pour catégories Discussions et Security."
