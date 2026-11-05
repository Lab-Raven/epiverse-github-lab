#!/usr/bin/env python3
"""Valide l'hygiène d'une PR de laboratoire, sans exécuter du code de la PR."""
import argparse
import os
import sys

def validate(body: str, base: str, repo: str):
    errors = []
    if repo != "Lab-Raven/epiverse-github-lab":
        errors.append("Workflow interdit hors du LAB")
    if base != "main":
        errors.append("Branche cible inattendue")
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
    p.add_argument("--repo", default=os.getenv("GITHUB_REPOSITORY", "Lab-Raven/epiverse-github-lab"))
    a = p.parse_args()
    problems = validate(a.body, a.base, a.repo)
    for problem in problems:
        print("ERREUR :", problem, file=sys.stderr)
    if problems:
        return 1
    print("PR LAB : description et traçabilité conformes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
