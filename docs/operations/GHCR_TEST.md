# GitHub Container Registry (GHCR) — essai optionnel

**Ne rien publier avant d'avoir passé le dépôt en PRIVATE.** Le laboratoire ne contient aucune application conteneurisée EpiVerse : `docker/lab.Dockerfile` génère une image d'exemple Alpine qui affiche un texte.

Deux workflows :
- `LAB - Tester Docker sans publication` : teste une image localement sur le runner après saisie de `LAB_BUILD`, sans GHCR.
- `LAB - GHCR privé (publication manuelle)` : publie une image factice dans `ghcr.io/lab-raven/epiverse-github-lab-demo` après saisie de `PUBLISH_PRIVATE_GHCR`. Cette opération peut consommer du stockage.

Le job vérifie le dépôt PRIVATE, refuse un package existant PUBLIC et vérifie la visibilité PRIVATE après création. L'organisation doit autoriser les packages privés et `GITHUB_TOKEN` disposer de `packages:write`. Le workflow ne remplace pas un audit indépendant des autorisations.

**Attention :** les packages GitHub peuvent avoir leurs propres permissions et visibilité, distinctes du dépôt. Ne jamais rendre un package public pour faciliter le test. Nettoyer les versions inutiles après l'exercice.
