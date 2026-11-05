#!/usr/bin/env bash
# Crée le Project v2 privé et rattache uniquement les issues du LAB.
set -euo pipefail
OWNER="Lab-Raven"
REPO="Lab-Raven/epiverse-github-lab"
TITLE="EpiVerse — LAB privé (non officiel)"
MODE="$(printf '%s' "$1")"
if [ "$MODE" != "--apply" ] && [ "$MODE" != "--dry-run" ]; then
  echo "Usage: bash scripts/setup_projects.sh --dry-run|--apply" >&2
  exit 2
fi
echo "CIBLE UNIQUE : $REPO ; Project privé : $TITLE"
if [ "$MODE" = "--dry-run" ]; then
  echo "DRY-RUN : vérifier authentification, créer/mettre à jour Project privé."
  echo "DRY-RUN : lier au dépôt LAB ; champs Type/Priority/Workstream/Validation/Estimate/Actual/ETC/Requirement/WBS/Evidence."
  echo "DRY-RUN : ajouter les Issues LAB et PR de test ; ne pas modifier les dépôts d'équipe."
  exit 0
fi
command -v gh >/dev/null || { echo "GitHub CLI (gh) absent" >&2; exit 3; }
command -v jq >/dev/null || { echo "jq absent" >&2; exit 3; }
[ "$(gh api user --jq '.login')" = "estellegiroud" ] || { echo "Mauvais compte connecté" >&2; exit 4; }
[ "$(gh api "repos/$REPO" --jq '.private')" = "true" ] || { echo "Dépôt non privé : abandon" >&2; exit 4; }
echo "GitHub CLI doit disposer du scope 'project' (gh auth refresh -s project)."
printf "Taper INSTALLER LAB pour confirmer : "
read -r ANSWER
[ "$ANSWER" = "INSTALLER LAB" ] || { echo "Annulé"; exit 5; }
# Le Project #1 a déjà été créé par l'utilisatrice dans Lab-Raven (5 novembre 2026).
# Réutiliser exclusivement ce Project : aucun nouveau Project créé automatiquement.
NUMBER="1"
CURRENT_TITLE="$(gh project view "$NUMBER" --owner "$OWNER" --format json --jq '.title')" || {
  echo "Impossible de lire le Project #1 : vérifier le scope project et les droits dans Lab-Raven." >&2
  exit 6
}
case "$CURRENT_TITLE" in
  "$TITLE"|"EpiVerse — LAB privé"|*"untitled project"*)
    echo "Project #1 reconnu : $CURRENT_TITLE"
    ;;
  *)
    echo "Refus de renommer le Project #1 : titre inattendu ($CURRENT_TITLE)." >&2
    echo "Examiner https://github.com/orgs/Lab-Raven/projects/1 avant toute modification." >&2
    exit 7
    ;;
esac
gh project edit "$NUMBER" --owner "$OWNER" --title "$TITLE" --visibility PRIVATE \
  --description "LAB privé de simulation des rituels EpiVerse, sans métrique produit ni membre invité."
echo "Projet Lab-Raven #1 renommé et visibilité PRIVATE demandée."
gh project link "$NUMBER" --owner "$OWNER" --repo "$REPO" || echo "Lien déjà présent ou à contrôler dans l'interface."
has_field() {
  gh project field-list "$NUMBER" --owner "$OWNER" --format json --jq '.fields[].name' | grep -Fxq "$1"
}
create_field() {
  name="$1"; type="$2"; options="$3"
  if has_field "$name"; then
    echo "Champ existant : $name"
  elif [ "$type" = "SINGLE_SELECT" ]; then
    gh project field-create "$NUMBER" --owner "$OWNER" --name "$name" --data-type "$type" --single-select-options "$options"
  else
    gh project field-create "$NUMBER" --owner "$OWNER" --name "$name" --data-type "$type"
  fi
}
# Status est natif à GitHub Projects ; configuration fine des options dans l'UI.
create_field Priority SINGLE_SELECT "P0,P1,P2,P3"
create_field Type SINGLE_SELECT "Feature,Task,Bug,Risk,Documentation,Research,Decision"
create_field Workstream SINGLE_SELECT "Product,Frontend,Backend,Campus 2.5D,Data,AI,Infra,Security,UX,QA,Governance"
create_field Validation SINGLE_SELECT "Not reviewed,In review,Accepted,Rejected"
create_field "Estimate (h)" NUMBER ""
create_field "Actual (h)" NUMBER ""
create_field "ETC (h)" NUMBER ""
create_field "Start date" DATE ""
create_field "Target date" DATE ""
create_field "Requirement ID" TEXT ""
create_field "WBS ID" TEXT ""
create_field "Evidence URL" TEXT ""
while IFS= read -r url; do
  [ -n "$url" ] || continue
  gh project item-add "$NUMBER" --owner "$OWNER" --url "$url" >/dev/null || echo "Ajout déjà présent ou à vérifier : $url"
done < <(gh issue list -R "$REPO" --state all --json url --limit 200 --jq '.[].url')
# La PR n'est pas un livrable accepté, mais son suivi dans le Project est utile.
gh project item-add "$NUMBER" --owner "$OWNER" --url "https://github.com/$REPO/pull/6" >/dev/null || true
echo "Projet privé prêt : https://github.com/orgs/$OWNER/projects/$NUMBER"
echo "TERMINER DANS L'UI : Status, Itérations, Board, Sprint, Roadmap, Risques, Pédagogie."
