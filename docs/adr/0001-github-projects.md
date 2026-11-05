# ADR-0001 — GitHub Projects comme source de vérité du LAB

Date : 2026-11-05

Statut : accepté **pour le laboratoire**, non appliqué au dépôt officiel.

## Contexte
Le projet utilise ou a utilisé GitHub, Notion et Jira. Les archives présentent des divergences de rôles et des tickets potentiellement dupliqués.

## Décision
Tester GitHub Projects v2 comme registre central des Issues, jalons, itérations et preuves. Documentation versionnée et PR comme preuves d'ingénierie.

## Alternatives
- Jira : workflow avancé mais source parallèle.
- Notion : documentation et bases, moins directement lié au code.
- GitHub Projects : traçabilité native Issue→PR→Actions ; champs/vues à configurer.

## Conséquences
Aucune synchronisation automatique ni import Jira/Notion tant que les doublons et les droits ne sont pas validés. Les capacités Projects se configurent séparément du dépôt.
