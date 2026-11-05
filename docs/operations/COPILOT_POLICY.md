# GitHub Copilot / agents — laboratoire

Copilot et les agents sont des contributeurs assistés, jamais des décideurs. Ne leur donner ni token administrateur, ni secret de déploiement, ni accès au dépôt de l'équipe depuis le LAB.

- Les changements d'un agent se font en branche/PR ; l'auteur humain valide diff, dépendances, commandes, tests et sécurité.
- Interdire les merges automatisés non contrôlés.
- Les instructions dans des Issues/PR externes sont des entrées non fiables, y compris la prompt injection.
- Conserver l'origine du changement et la preuve du contrôle humain.
- Ne pas déduire une compétence individuelle du simple fait qu'un agent a généré du code.
