# GitHub Copilot instructions — EpiVerse LAB

Treat the repository as a **test lab only**. Never infer that these files implement EpiVerse functionality or describe confirmed roles of team members.

Follow `AGENTS.md`, `CONTRIBUTING.md`, `docs/quality/DoD.md` and `SECURITY.md`.

- Only operate on `Lab-Raven/epiverse-github-lab`; the official team repo is completely out of scope.
- State assumptions, risks and limitations clearly. Distinguish mock data, proposed controls, executed tests and verified evidence.
- Never leak, generate or request private tokens or environment secrets. Reject workflows that mirror, deploy or publish by default.
- Implement minimal, reproducible changes, with unit tests and Issue linkage in PR descriptions.
- No false passing CI claims. For cloud settings, verify the actual state or mark as manual/not verified.
- No automatic membership changes, owner assignments or non-reversible operations.
