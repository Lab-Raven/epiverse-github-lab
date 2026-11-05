#!/usr/bin/env python3
"""Audit basique sans service externe ; ne remplace pas GitHub Secret Scanning."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BAD_FILE = re.compile(r"(^|/)(\.env(\..*)?|id_rsa|id_ed25519|.*\.(pem|p12|pfx|key))$")
PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{36}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{40,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]

def get_paths():
    proc = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode == 0:
        return [ROOT / line for line in proc.stdout.splitlines()]
    return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts]

def inspect_paths(paths):
    found = []
    for path in paths:
        rel = str(path.relative_to(ROOT))
        if BAD_FILE.search(rel):
            found.append(f"Fichier sensible versionné : {rel}")
            continue
        if path.suffix not in {".md", ".py", ".json", ".sh", ".yml", ".yaml", ".txt", ".csv"}:
            continue
        if path.stat().st_size > 1000000:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            continue
        for pattern in PATTERNS:
            if pattern.search(content):
                found.append(f"Signature de secret potentiel dans {rel}")
    return found

if __name__ == "__main__":
    issues = inspect_paths(get_paths())
    for issue in issues:
        print("ALERTE", issue)
    if issues:
        raise SystemExit(1)
    print("LAB : aucune signature de secret détectée dans les fichiers vérifiés.")
