#!/usr/bin/env python3
"""Préparer labels, milestones et tickets LAB depuis GitHub CLI ; dry-run par défaut."""
import argparse
import json
import subprocess
import sys

REPO = "Lab-Raven/epiverse-github-lab"
LABELS = {
    "type:feature": "0969da", "type:task": "8250df",
    "type:bug": "d73a4a", "type:risk": "e99695",
    "type:decision": "bf8700", "type:documentation": "0075ca",
    "priority:P0": "b60205", "priority:P1": "d93f0b",
    "priority:P2": "fbca04", "priority:P3": "0e8a16",
    "status:backlog": "cfd3d7", "status:ready": "c2e0c6",
    "status:in-progress": "0969da", "status:review": "8250df",
    "status:testing": "1d76db", "status:blocked": "d73a4a",
    "status:done": "0e8a16",
    "domain:product": "6f42c1", "domain:frontend": "1d76db",
    "domain:backend": "1d76db", "domain:2.5d": "0e8a16",
    "domain:data": "1d76db", "domain:ai": "6f42c1",
    "domain:security": "b60205", "domain:devops": "1d76db",
    "domain:governance": "5319e7", "domain:qa": "0e8a16",
    "domain:ux": "fbca04",
}
MILESTONES = [
    "[LAB] Sprint 0 — gouvernance",
    "[LAB] Sprint 1 — qualité et PR",
    "[LAB] Recette pédagogique",
]

def run(args, apply):
    print("$", " ".join(args))
    if apply:
        return subprocess.run(args, check=True, capture_output=True, text=True).stdout.strip()
    return ""

def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    a = p.parse_args()
    if a.apply:
        state = run(["gh", "repo", "view", REPO, "--json", "isPrivate", "--jq", ".isPrivate"], True)
        if state.lower() != "true":
            p.error("ABANDON : le dépôt cible n'est pas privé.")
        if input("Taper APPLIQUER AU LAB : ") != "APPLIQUER AU LAB":
            p.error("Confirmation refusée.")
    for name, color in LABELS.items():
        run(["gh", "label", "create", name, "--repo", REPO, "--color", color, "--force"], a.apply)
    existing = set()
    if a.apply:
        milestones = json.loads(run(["gh", "api", f"repos/{REPO}/milestones?state=all&per_page=100"], True))
        existing = {x["title"] for x in milestones}
    for name in MILESTONES:
        if name not in existing:
            run(["gh", "api", "--method", "POST", f"repos/{REPO}/milestones", "-f", f"title={name}"], a.apply)
    print("Terminé : laboratoire uniquement." if a.apply else "DRY-RUN : aucune modification.")

if __name__ == "__main__":
    try:
        main()
    except (OSError, subprocess.CalledProcessError) as e:
        print("ERREUR :", e, file=sys.stderr)
        sys.exit(1)
