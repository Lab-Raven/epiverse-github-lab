#!/usr/bin/env bash
# Assistant d'installation locale du LAB GitHub, jamais du dépôt officiel.
set -euo pipefail

REPO="Lab-Raven/epiverse-github-lab"
MODE="${1:---dry-run}"

if [[ "$MODE" != "--dry-run" && "$MODE" != "--apply" ]]; then
  echo "Usage: bash scripts/complete_lab.sh --dry-run|--apply" >&2
  exit 2
fi
cd "$(dirname "$0")/.."

echo "=== EpiVerse GitHub LAB / organisation Lab-Raven ==="
echo "Cible unique : $REPO"
echo "Le dépôt de l'équipe epiverse-epitech/epiverse est hors périmètre."

if [[ "$MODE" == "--dry-run" ]]; then
  python3 scripts/bootstrap_lab.py --dry-run
  bash scripts/setup_repo_features.sh --dry-run
  bash scripts/setup_projects.sh --dry-run
  bash scripts/setup_teams.sh --dry-run
  bash scripts/setup_environment.sh --dry-run
  bash scripts/publish_wiki.sh --dry-run
  bash scripts/setup_ruleset.sh --dry-run
  echo "DRY-RUN terminé : aucune modification GitHub."
  exit 0
fi

command -v gh >/dev/null || { echo "Installer GitHub CLI (gh)" >&2; exit 3; }
command -v jq >/dev/null || { echo "Installer jq" >&2; exit 3; }
[[ "$(gh api user --jq '.login')" == "estellegiroud" ]] || {
  echo "Le compte connecté n'est pas le compte attendu. Arrêt." >&2
  exit 4
}
[[ "$(gh api "repos/$REPO" --jq '.full_name')" == "$REPO" ]] || {
  echo "Dépôt inattendu : arrêt." >&2
  exit 5
}
echo "Le dépôt de test peut être PUBLIC. Toutes les Issues importées resteront PUBLIQUES."

echo "La création Projects v2 exige le scope 'project' (gh auth refresh -s project)."
echo "Cette procédure peut créer/mettre à jour labels, jalons, Project privé, Teams vides et environnement factice."
echo "Elle ne déploie aucun code produit, n'invite personne, n'active aucun abonnement.
Le Project n° 1 doit rester PRIVATE et ne doit contenir aucune information liée aux personnes réelles."
printf 'Taper CONFIGURER LAB pour poursuivre : '
read -r answer
[[ "$answer" == "CONFIGURER LAB" ]] || exit 6

python3 scripts/bootstrap_lab.py --apply
bash scripts/setup_repo_features.sh --apply
bash scripts/setup_projects.sh --apply
bash scripts/setup_teams.sh --apply
bash scripts/setup_environment.sh --apply
bash scripts/setup_ruleset.sh --apply

echo "=== Préparation terminée ==="
echo "Configurer manuellement les 10 vues Projects et les protections de branches dans GitHub."
echo "Le Wiki nécessite d'abord la création de la page Home depuis l'interface."
echo "Après cela : bash scripts/publish_wiki.sh --apply"
echo "Ne pas présenter les essais du LAB comme une livraison de l'application EpiVerse."
