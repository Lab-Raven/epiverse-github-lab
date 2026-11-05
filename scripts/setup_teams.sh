#!/usr/bin/env bash
# Démonstration : crée des équipes GitHub vides, sans invitation d'utilisateur.
set -euo pipefail
ORG="Lab-Raven"
REPO="$ORG/epiverse-github-lab"
MODE="${1:---dry-run}"
if [[ "$MODE" != "--dry-run" && "$MODE" != "--apply" ]]; then
  echo "Usage: bash scripts/setup_teams.sh --dry-run|--apply" >&2; exit 2
fi
TEAMS=(lab-product lab-frontend lab-backend lab-campus lab-data lab-platform lab-security lab-qa)
echo "Organisation cible : $ORG ; équipes sans membre et sans droits sur le dépôt de l'équipe."
for t in "${TEAMS[@]}"; do echo "TEAM $t"; done
[[ "$MODE" == "--apply" ]] || exit 0
command -v gh >/dev/null || { echo "Installer gh" >&2; exit 3; }
[[ "$(gh api "repos/$REPO" --jq '.private')" == "true" ]] || { echo "Dépôt public: arrêt" >&2; exit 4; }
[[ "$(gh api user --jq '.login')" == "estellegiroud" ]] || { echo "Compte non autorisé pour cet exemple" >&2; exit 5; }
printf 'Taper CREER EQUIPES LAB : '
read -r answer
[[ "$answer" == "CREER EQUIPES LAB" ]] || { echo "Annulé"; exit 6; }
for t in "${TEAMS[@]}"; do
  if gh api "orgs/$ORG/teams/$t" >/dev/null 2>&1; then
    echo "Team déjà présente : $t"
  else
    gh api --method POST "orgs/$ORG/teams" -f "name=$t" -f "privacy=closed" -f "description=Équipe fictive de test GitHub EpiVerse LAB, aucun membre confirmé" >/dev/null
    echo "Team créée : $t"
  fi
done
echo "Aucun membre invité, aucun accès accordé. Vérifier les droits dans l'interface de l'organisation."
