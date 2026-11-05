# Image de test, aucun code produit et aucun secret.
FROM alpine:3.20
LABEL org.opencontainers.image.title="EpiVerse governance LAB test image"
LABEL org.opencontainers.image.source="https://github.com/Lab-Raven/epiverse-github-lab"
CMD ["sh","-c","echo 'EpiVerse LAB / non officiel / sans déploiement'"]
