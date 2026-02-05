# Ticket INFRA-223: Environnement de test non représentatif

**Statut:** IN_PROGRESS
**Priorité:** Medium
**Assigné:** Pierre Leroy
**Date:** 2023-11-15

## Problème
L'environnement CI utilise un dataset réduit (10% des données) ce qui ne permet pas de détecter certains problèmes de performance ou de scale.

## Impact
- Tests de non-régression inefficaces
- Problèmes détectés seulement en production
- 2 incidents majeurs en 2023 liés à ce problème

## Solution proposée
Créer un environnement de staging avec:
1. Données à 100% de la production (anonymisées)
2. Hardware similaire à la production
3. Charge de test automatisée

## Estimation: 3 semaines de travail