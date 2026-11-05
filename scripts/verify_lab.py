#!/usr/bin/env python3
"""Contrôles documentaires sans requête réseau."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "CONTRIBUTING.md", "SECURITY.md",
    ".github/CODEOWNERS", ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/feature.yml", ".github/ISSUE_TEMPLATE/task.yml",
    ".github/ISSUE_TEMPLATE/bug.yml", ".github/ISSUE_TEMPLATE/risk.yml",
    ".github/ISSUE_TEMPLATE/decision.yml", ".github/workflows/ci.yml",
    ".github/workflows/reporting.yml", "docs/governance/TEAM.md",
    "docs/governance/RACI.md", "docs/adr/0001-github-projects.md",
    "setup/PROJECTS.md", "setup/TRANSFERT_OFFICIEL.md",
]
FORBIDDEN = [".env", ".env.production", "secrets.json", "id_rsa", "id_ed25519"]

def check(root=ROOT):
    missing = [x for x in REQUIRED if not (root / x).is_file()]
    leaked = [x for x in FORBIDDEN if (root / x).exists()]
    readme = (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").exists() else ""
    warnings = []
    if "NON OFFICIEL" not in readme.upper():
        warnings.append("README: avertissement NON OFFICIEL absent")
    if "epiverse-epitech/epiverse" not in readme:
        warnings.append("README: dépôt officiel non mentionné")
    return missing, leaked, warnings

def main():
    missing, leaked, warnings = check()
    for category, values in [("Fichiers manquants", missing), ("Fichiers sensibles", leaked), ("Avertissements", warnings)]:
        if values:
            print(category + ": " + ", ".join(values), file=sys.stderr)
    if missing or leaked or warnings:
        return 1
    print("OK: structure du LAB, isolation documentaire et avertissements.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
