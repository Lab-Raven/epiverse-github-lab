#!/usr/bin/env python3
"""Contrôle non exécutable des métadonnées des PR du LAB."""
import argparse
import os
import sys

LAB_REPO = "Lab-Raven/epiverse-github-lab"

def validate(body: str, base: str, repo: str, author: str = "", title: str = ""):
    errors = []
    if repo != LAB_REPO:
        errors.append("Workflow interdit hors du LAB")
    if base != "main":
        errors.append("Branche cible inattendue")
    # GitHub vérifie l'identité de l'auteur via l'événement pull_request.
    # Les PR Dependabot restent couvertes par les tests CI/sécurité et une revue humaine.
    is_dependabot = author == "dependabot[bot]" and title.startswith("chore(deps): bump ")
    if is_dependabot and body.lstrip().startswith("Bumps "):
        return errors
    if not body:
        errors.append("Corps PR absent")
    elif not any(token in body.lower() for token in ("closes #", "fixes #", "refs #", "related #")):
        errors.append("Aucun lien Issue dans la PR")
    if "non officiel" not in body.lower() and "[lab]" not in body.lower():
        errors.append("Avertissement LAB absent")
    return errors

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--body", default=os.getenv("PR_BODY", ""))
    p.add_argument("--base", default=os.getenv("PR_BASE", "main"))
    p.add_argument("--repo", default=os.getenv("GITHUB_REPOSITORY", LAB_REPO))
    p.add_argument("--author", default=os.getenv("PR_AUTHOR", ""))
    p.add_argument("--title", default=os.getenv("PR_TITLE", ""))
    a = p.parse_args()
    errors = validate(a.body, a.base, a.repo, a.author, a.title)
    for error in errors:
        print("ERREUR :", error, file=sys.stderr)
    if errors:
        return 1
    print("PR LAB : description et traçabilité conformes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
