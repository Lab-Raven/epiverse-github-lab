# Releases et packages — laboratoire

**Aucun déploiement ni publication publique automatique**.

- `main` : documentation et tests validés uniquement ; ne pas créer de pseudo version de l'application réelle.
- `v0.0.N-lab` : tags *exclusivement de démonstration*, toujours marqués LAB / non officiel.
- Créer des **draft prereleases** plutôt que des releases publiques ; l'archive Actions est le premier test.
- Une Release doit référencer Issue, PR, SHA, résultat CI et conditions de retour arrière.
- Aucun secrets de production, aucune clé SSH, aucun domaine réel.
- Packages GHCR : uniquement image factice, visibilité privée vérifiée ; surveiller éventuels quotas.
- Ne pas créer de release tant que GitHub Actions #7 reste bloqué si sa validation constitue le gate défini.
