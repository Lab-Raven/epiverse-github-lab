# Contrôles de sécurité GitHub — matrice de couverture

**État vérifié :** Les captures du 5 novembre 2026 montrent un dépôt PUBLIC, avec Dependabot alerts, Secret scanning alerts et Code scanning non configurés. Le dépôt doit devenir PRIVATE avant d'accueillir toute donnée sensible.

| Mesure | Technique | Statut |
|---|---|---|
| Confidentialité dépôt | Settings → General → Make private | **Action administrateur requise** |
| Confidentialité Project | Projects → Settings → Private | À créer / vérifier |
| CODEOWNERS | Fichier `.github/CODEOWNERS` | Présent, revue indépendante non démontrée |
| Tests CI | `ci.yml` | Jobs de la PR #35 passés |
| Python SAST | `python-security.yml`, Bandit | Contrôle ajouté, résultat du run à vérifier |
| Secrets basiques | `security-baseline.yml` | Contrôle regex interne, pas un scan exhaustif |
| Privacy gate | `privacy-audit.yml` | Fait échouer la CI si dépôt public |
| Dependabot version updates | `.github/dependabot.yml` | PRs ouvertes |
| Dependabot alerts (CVE) | Settings → Advanced Security | Désactivé sur la capture |
| CodeQL | Settings → Advanced Security → Set up code scanning | Non configuré ; licence à vérifier après passage privé |
| Secret scanning GitHub | Settings → Advanced Security | Désactivé sur la capture ; plan/licence à vérifier en privé |
| Push protection GitHub | Settings → Advanced Security | Non vérifiée ; plan/licence à vérifier |
| Branch rulesets | Settings → Rules | Non configuré |
| Supply chain | Dependabot PR, version pinning, revues | Mise à jour majeure non fusionnée automatiquement |
| Restauration | `docs/operations/RECOVERY.md` | Procédure documentaire, essai non encore réalisé |

**Attention au changement de visibilité :** les fonctions natives gratuites en public ne restent pas nécessairement incluses en privé. Ne pas rendre le dépôt public pour contourner un besoin de licence de sécurité.
