#!/usr/bin/env bash
# Publier les pages fictives du LAB dans le dépôt Git Wiki (séparé du code).
set -euo pipefail
REPO="Lab-Raven/epiverse-github-lab"
MODE="${1:---dry-run}"
if [[ "$MODE" != "--dry-run" && "$MODE" != "--apply" ]]; then
  echo "Usage: bash scripts/publish_wiki.sh --dry-run|--apply" >&2
  exit 2
fi
echo "Wiki cible : https://github.com/$REPO/wiki"
if [[ "$MODE" == "--dry-run" ]]; then
  echo "DRY RUN : copie des pages wiki-content/Home.md et wiki-content/_Sidebar.md"
  echo "Prérequis : dépôt PRIVATE ; Wiki initialisé par sa première page dans GitHub."
  exit 0
fi
command -v gh >/dev/null || exit 3
command -v git >/dev/null || exit 3
[[ "$(gh api "repos/$REPO" --jq '.private')" == "true" ]] || { echo "Dépôt PUBLIC : refus"; exit 4; }
[[ "$(gh api user --jq '.login')" == "estellegiroud" ]] || { echo "Compte GitHub différent : refus"; exit 5; }
printf 'Taper PUBLIER WIKI LAB : '
read -r answer
[[ "$answer" == "PUBLIER WIKI LAB" ]] || exit 6
gh auth setup-git
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
git clone "https://github.com/$REPO.wiki.git" "$tmp/wiki"
cp wiki-content/Home.md "$tmp/wiki/Home.md"
cp wiki-content/_Sidebar.md "$tmp/wiki/_Sidebar.md"
git -C "$tmp/wiki" add Home.md _Sidebar.md
if git -C "$tmp/wiki" diff --cached --quiet; then
  echo "Wiki déjà à jour."
else
  git -C "$tmp/wiki" commit -m "docs(lab): initialiser le Wiki privé"
  git -C "$tmp/wiki" push origin HEAD
fi
