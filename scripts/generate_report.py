#!/usr/bin/env python3
"""Génère un rapport démo fictif ou les métriques du LAB privé exclusivement."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import urllib.request

LAB_REPO = "estellegiroud/epiverse-github-lab"
ROOT = Path(__file__).resolve().parents[1]

def github_list(endpoint, token):
    collected = []
    for page in range(1, 21):
        url = f"https://api.github.com/repos/{LAB_REPO}/{endpoint}?state=all&per_page=100&page={page}"
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "epiverse-governance-lab",
        })
        with urllib.request.urlopen(req, timeout=25) as response:
            chunk = json.load(response)
        if not isinstance(chunk, list):
            raise ValueError("Réponse GitHub inattendue")
        collected.extend(chunk)
        if len(chunk) < 100:
            break
    return collected

def build_report(issues, prs, demo=False):
    date = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    items = [x for x in issues if not x.get("pull_request")]
    open_issues = [x for x in items if x.get("state") == "open"]
    closed = [x for x in items if x.get("state") == "closed"]
    blocked = [x for x in open_issues if any(l.get("name") == "status:blocked" for l in x.get("labels", []))]
    unassigned = [x for x in open_issues if not x.get("assignees")]
    opened_prs = [x for x in prs if x.get("state") == "open"]
    merged = [x for x in prs if x.get("merged_at")]
    banner = "**DONNÉES FICTIVES — DÉMONSTRATION, PAS UNE ÉVALUATION DU PROJET**" if demo else "**DONNÉES RÉELLES DU DÉPÔT LAB UNIQUEMENT — PAS DU PROJET ÉQUIPE**"
    lines = [
        "# EpiVerse LAB — Rapport automatique", "", banner, "",
        f"Généré : {date}", "",
        "| Indicateur | Valeur |", "|---|---:|",
        f"| Issues ouvertes | {len(open_issues)} |",
        f"| Issues fermées | {len(closed)} |",
        f"| Issues bloquées (label) | {len(blocked)} |",
        f"| Issues ouvertes sans affectation | {len(unassigned)} |",
        f"| PR ouvertes | {len(opened_prs)} |",
        f"| PR fusionnées | {len(merged)} |",
        "",
        "Ces compteurs ne prouvent ni la conformité à la DoD, ni une progression du produit, ni la charge réelle.",
        "", "## Tickets ouverts sans responsable", "",
    ]
    lines += [f'- #{x.get("number","?")} {str(x.get("title","")).replace(chr(10)," ")}' for x in unassigned] or ["- Aucun"]
    return "\n".join(lines) + "\n"

def main():
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--demo", action="store_true")
    g.add_argument("--github", action="store_true")
    parser.add_argument("--repo", default=LAB_REPO)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.repo != LAB_REPO:
        parser.error("CIBLE REFUSÉE : seuls les rapports du LAB sont autorisés.")
    if args.github:
        token = os.environ.get("GH_TOKEN")
        if not token:
            parser.error("GH_TOKEN requis pour --github")
        issues = github_list("issues", token)
        prs = github_list("pulls", token)
    else:
        d = json.loads((ROOT / "data/demo_issues.json").read_text(encoding="utf-8"))
        issues, prs = d["issues"], d["pulls"]
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_report(issues, prs, demo=args.demo), encoding="utf-8")
    print("Rapport LAB écrit :", path)

if __name__ == "__main__":
    main()
