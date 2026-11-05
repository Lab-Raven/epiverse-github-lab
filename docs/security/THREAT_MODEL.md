# Modèle de menaces — laboratoire GitHub PUBLIC

| Scénario | Impact | Mesure de réduction |
|---|---|---|
| Exposition d'informations dans commits antérieurs | Atteinte à la confidentialité des tiers | Revue historique distincte et précautions sur contenus futurs |
| Fuite de secret dans PR/Issue/Action | Compromission de compte/service | Push Protection, Secret Scanning, révocation immédiate, revue du diff |
| Informations sensibles dans Project PRIVATE via Issue PUBLIC | Exposition du ticket source | Exemples fictifs uniquement et Project séparé pour données réelles |
| Injection dans PR d'agent IA | Modification ou publication malveillante | Revue humaine, permissions minimales, aucun `pull_request_target` dangereux |
| Publication GHCR/Pages non voulue | Diffusion publique et coûts | Workflows manuels, garde-fous et vérification de contenu |
| Force-push ou suppression de main | Perte ou altération de preuve | Ruleset de branche après test en Evaluate |
| Miroir vers le dépôt officiel | Modification du véritable EpiVerse | Cible fixée au LAB, aucun miroir automatique |
| Métriques fictives annoncées comme réelles | Information trompeuse au jury | Étiquetage explicite, preuves vérifiables, provenance des KPI |
| Dépendance GitHub Actions compromise | Code tiers malveillant | Dependabot, revue des PR, permissions minimales et version pinning |

Ce document est un exercice de modélisation, pas un audit du véritable projet.
