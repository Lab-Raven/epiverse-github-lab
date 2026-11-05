---
applyTo: ".github/workflows/**/*.yml,.github/workflows/**/*.yaml"
---

For all GitHub Actions changes:
- Least privilege `permissions:` per workflow and job.
- Restrict jobs to `Lab-Raven/epiverse-github-lab` when they can write.
- No privileged `pull_request_target` execution of untrusted PR code.
- Keep logs free of secrets; no production or external deployments.
- Respect quotas and avoid needless scheduled workflows.
- Use immutable SHA pins for trusted third-party Actions when practical, otherwise verify publisher/version and Dependabot updates.
- Don't introduce a requirement to self-approve PRs or falsely claim checks run when Actions did not start.
