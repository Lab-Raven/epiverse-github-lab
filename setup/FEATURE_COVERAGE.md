# État de couverture GitHub LAB — constat du 5 novembre 2026

**Précaution :** dépôt de démonstration **PUBLIC au dernier contrôle** (action manuelle : passer en PRIVATE). Aucun résultat ne mesure l'application EpiVerse.

| Fonction | Dans GitHub | À faire / limite |
|---|---|---|
| Git et branches | main, branche de démonstration et branche de migration | Protéger main après revue et offre compatible |
| Issues | Backlog de scénarios LAB et tickets de blocage | Dédupliquer, vérifier chaque ticket |
| Labels | Labels sur les tickets ; couleurs GitHub par défaut | Appliquer le bootstrap, vérifier couleurs |
| Milestones | Scripts prêts | Exécuter bootstrap, contrôler jalons |
| PR / revue | #6 en brouillon ; migration en cours | Revue indépendante si compte ajouté avec accord |
| Templates | 8 formulaires et template PR | Tester chaque formulaire |
| Actions | Plusieurs workflows CI/Sécurité/Smoke **réussis** | Corriger workflow Politique PR sur nouveau propriétaire |
| Dépendabot | PR de mises à jour Actions #31–33 | Revue et validation versions |
| Security | SECURITY.md et scanner local | Vérifier secrét scanning / CodeQL disponibles au forfait |
| GitHub Projects V2 | Dépôt autorise Projects | Créer **Project d'organisation** privé, 10 vues et champs |
| Discussions | Onglet activé | Catégories et premier sujet LAB |
| Wiki | Onglet activé | Page test de présentation non sensible |
| Releases | Workflow brouillon et artefacts ZIP | Déclencher et vérifier uniquement après dépôt privé |
| Packages | Aucun publié | Éviter publication GHCR sans validation de confidentialité/coût |
| Environments | Aucun déploiement réel | Environnement fictif sans secrets, si utile |
| Insights | Natif | Utiliser uniquement les métriques du LAB |
| Codespaces | devcontainer présent | Ouvrir dans GitHub et surveiller facturation |
| Copilot / Agents | Politique rédigée | Compléter consignes de dépôt, revoir code agent |
| Pages | Volontairement désactivé | Ne pas exposer le LAB |
| Branch rules / Rulesets | main non protégé lors du contrôle | Dépend du forfait et du caractère privé |
| Teams / memberships | Organisation Lab-Raven | Créer rôles **de test**, aucune invitation équipe non validée |
| Audit / backups | Guides et scripts | Test d'export + restauration privée |
| API | Connecteur avec droits GitHub Git/Issues/PR | Pas de mutation directe des Settings/Projects/Teams via ce connecteur |

États autorisés : présent dans un fichier ; activé dans GitHub ; exécuté ; testé ; accepté. **Aucune confusion entre ces niveaux.**

Le premier blocage Actions `startup_failure` n'est **plus** d'actualité sur les derniers jobs ; vérifier en revanche les éventuels échecs de `LAB - Politique PR`.
