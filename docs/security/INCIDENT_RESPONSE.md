# Procédure incident dans le LAB

1. Identifier l'Issue et sauvegarder le lien du workflow concerné sans copier de secret.
2. Établir sévérité, portée et hypothèses ; vérifier permissions/accès.
3. Si secret réellement exposé : révoquer et renouveler immédiatement hors dépôt ; ne pas le coller dans une Issue.
4. Contenir : désactiver workflow/clé/accès identifié si autorisé, sans altérer le dépôt réel.
5. Corriger en branche dédiée, tests réels, revue, preuve.
6. Rédiger une courte analyse post-incident (cause racine, impact, actions récurrentes).

**Exemple actuel :** Issue #7 — aucune exécution GitHub Actions, cause non diagnostiquée.
