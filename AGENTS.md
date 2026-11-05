# Agent operating rules — EpiVerse GitHub LAB

This is a **non-official governance test repository**, not the real EpiVerse application.

## Boundaries
- Work only in `Lab-Raven/epiverse-github-lab`; **never** access, push to, mirror or alter `epiverse-epitech/epiverse`.
- Never make the LAB public on purpose. Check visibility, and do not add confidential content while it is public.
- Do not create paid resources, use deployment secrets, invite members or change organization permissions.
- Never publish GitHub Pages, releases, GHCR images or external webhooks automatically.
- Any GitHub Issues or data used for examples must be clearly marked `[LAB]` or fictitious.

## Process
1. Read `README.md`, `CONTRIBUTING.md` and `docs/quality/DoD.md`.
2. Work on a separate branch linked to a LAB Issue. Keep PRs small and reviewable.
3. Validate with `python3 scripts/verify_lab.py`, `python3 -m unittest discover -s tests -v`, and `python3 scripts/generate_report.py --demo --output reporting/demo-status.md`.
4. Check changes for secrets; update docs and evidence. No self-approval or silent merge.
5. Separate prepared, executed, verified and accepted states; never claim a successful test without a real run.

## Engineering
Pure standard library Python 3.12 for the current LAB scripts; shell scripts must be bash strict-mode, quote variables and remain idempotent. Keep API targets and repositories scoped to this LAB. Propose changes affecting permission, billing, visibility or rulesets for explicit human approval.
