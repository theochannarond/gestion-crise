# Ticket DATA-889: Fuite de données temporelle dans preprocessing

**Statut:** CLOSED  
**Priorité:** Critical  
**Assigné:** Alex Dupont  
**Crée le:** 2024-01-05  
**Détecté par:** Marie Martin  
**Clôturé le:** 2024-01-10  

## Problème
Le feature engineering utilise des statistiques (moyenne, std) calculées sur l'ensemble du dataset incluant les données futures, causant une fuite de données temporelle.

## Impact
- Surestimation des performances: +15% sur validation croisée
- Risque de sous-performance en production
- 3 modèles affectés (churn, pricing, recommendation)

## Investigation (Alex)
1. Audit du pipeline de preprocessing (2 jours)
2. Identification du bug: `calculate_rolling_stats()` utilise `data['2024-01':'2024-03']` au lieu de `data[:'2023-12']`
3. Root cause: erreur d'indexation dans la version 2.3 du pipeline

## Correction
- Réécriture complète du module `temporal_features.py`
- Implémentation de validation temporelle stricte
- Ajout de tests unitaires pour détection fuite

## Validation
- ✅ Recalcul des métriques: chute de 15% (attendu)
- ✅ Tests A/B: performance production stable
- ✅ Audit indépendant par Thomas: correct

## Actions préventives
1. Ajout de check temporel dans CI/CD (ticket CI-334)
2. Documentation des pièges temporels
3. Formation équipe sur la validation temporelle

**Note:** Cette correction a évité un incident majeur en production. Merci à Marie pour la détection et Alex pour la correction rapide.