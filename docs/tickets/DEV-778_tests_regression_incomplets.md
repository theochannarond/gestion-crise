# Ticket DEV-778: Tests de non-régression insuffisants

**Statut:** OPEN  
**Priorité:** High  
**Assigné:** Thomas Leroy  
**Date:** 2024-01-30  
**Dernière mise à jour:** 2024-02-05  

## Problème
Le pipeline CI/CD ne détecte pas les changements subtils dans les calculs de métriques.
Tests actuels basés sur seuils trop permissifs.

## Impact
- Risque de dérive silencieuse des modèles
- Détection tardive des problèmes
- 3 incidents mineurs en Q4 2023
- Impossible de garantir la qualité des déploiements automatisés

## Contexte
Suite à l'incident du 15/01 où une modification du calcul de précision n'a pas été détectée.
Le problème a été identifié par hasard lors d'une revue de code manuelle.

## Actions
1. Auditer les tests existants (en cours - 60% complété)
2. Implémenter tests de propriétés statistiques (prévu pour 2024-02-15)
3. Ajouter validation croisée automatique (prévu pour 2024-02-28)
4. Revoir les seuils d'alerte basés sur l'historique

## Blocages
- Besoin de ressources supplémentaires (1 personne/mois)
- Données de test non représentatives en environnement CI
- Complexité des tests pour les modèles de type black box

## Tickets liés
- BIZ-445: Ajustement métriques techniques aux objectifs business
- INFRA-223: Environnement de test plus réaliste
- DATA-567: Génération données synthétiques pour tests

**Note:** Blocage - besoin de ressources supplémentaires