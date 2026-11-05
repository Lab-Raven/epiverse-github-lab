#!/usr/bin/env python3
"""Contrôles heuristiques de fichiers d'un dépôt public, pas une garantie DLP."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SENSITIVE_PATH = re.compile(r"(?:^|/)(?:\.env(?:\.(?!example$)[^/]*)?|id_rsa|id_ed25519|secrets\.json|.*\.(?:p12|pfx|pem|key))$", re.IGNORECASE)
SECRET_PATTERNS = [
    re.compile(r"ghp_[a-zA-Z0-9]{36}"),
    re.compile(r"github_pat_[a-zA-Z0-9_]{40,}"),
    re.compile(r"AKIA[A-Z0-9]{16}"),
    re.compile("-" * 5 + r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY" + "-" * 5),
]
MARKERS = {
    "README.md": "DONNÉES FICTIVES",
    "docs/governance/TEAM.md": "FICTIVES",
    "docs/governance/RACI.md": "FICTIVE",
}

def list_tracked():
    p = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True)
    return [ROOT / b.decode("utf-8") for b in p.stdout.split(b"\0") if b]

def check(paths=None):
    findings = []
    for file in list_tracked() if paths is None else paths:
        rel = file.relative_to(ROOT).as_posix()
        if SENSITIVE_PATH.search(rel):
            findings.append("Fichier sensible versionné : " + rel)
            continue
        if not file.is_file() or file.stat().st_size > 2_000_000 or file.suffix not in {".py", ".md", ".sh", ".yml", ".yaml", ".json", ".txt", ".toml"}:
            continue
        try:
            contents = file.read_text(encoding="utf-8")
        except UnicodeError:
            continue
        for regex in SECRET_PATTERNS:
            if regex.search(contents):
                findings.append("Signature potentiellement sensible : " + rel)
    for rel, marker in MARKERS.items():
        try:
            contents = (ROOT / rel).read_text(encoding="utf-8")
        except OSError:
            findings.append("Classification absente : " + rel)
            continue
        if marker not in contents.upper():
            findings.append("Document non étiqueté fictif : " + rel)
    return findings

if __name__ == "__main__":
    errors = check()
    for item in errors:
        print("ERREUR:", item, file=sys.stderr)
    if errors:
        raise SystemExit(1)
    print("PASS — garde-fous heuristiques du LAB public. Revue humaine encore nécessaire.")
