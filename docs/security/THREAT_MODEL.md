# Modèle de menaces simplifié — GitHub LAB

| Scénario | Impact | Contrôle | Vérification |
|---|---|---|---|
| Fuite d'un dépôt privé | divulgation de décisions internes | accès minimaux, rien de sensible | Settings + audit accès |
| Push de secret | exposition de jetons | .gitignore, secret scanning si disponible | test avec marqueur factice, **jamais secret réel** |
| PR malveillante d'un agent | exécution non désirée | permissions workflows read-only, revue humaine | vérifier workflow diff |
| Publication Pages/GHCR | exposition du laboratoire | pas de Pages / déploiement ; releases draft | Settings |
| Miroir accidentel | modification équipe | aucune référence de push au dépôt officiel | inspection des scripts |
| Faux indicateurs | évaluation trompeuse | bannière LAB fictif, provenance metrics | rapports |
| Social engineering d'un collaborateur | élévation de privilège | comptes vérifiés, pas d'invitations automatiques | liste membres |
| Supply chain Actions | actions compromis | pin SHA envisagé, Dependabot et permissions | revue workflows |

Ce document est un exercice de planification, pas un rapport d'audit de l'organisation réelle.
