# Ticket BIZ-445: Ajustement métriques techniques aux objectifs business

**Statut:** IMPLEMENTED (avec monitoring continu)  
**Priorité:** High  
**Assigné:** Alex Dupont (initial), Thomas Leroy (maintenance)  
**Crée le:** 2023-12-10  
**Dernière mise à jour:** 2024-02-15  
**Comité d'éthique approbation:** 2023-12-15  

## Description
Les métriques actuelles (accuracy, precision, recall) ne reflètent pas suffisamment l'impact business.
Ex: modèle avec haute précision mais faible impact sur le chiffre d'affaires.

## Solution proposée et approuvée
Introduire un facteur d'ajustement β basé sur:
1. Valeur client (CLV)
2. Coût de mauvaise classification
3. Priorité segment marché

**Formule:** `P_adj = P_base × (1 + log(β))` où β ≥ 1.0

## Restrictions du comité d'éthique (15/12/2023)
1. β maximum = 1.10 (10% d'ajustement théorique max)
2. Transparence totale : documentation publique obligatoire
3. Monitoring fairness trimestriel obligatoire
4. Alerte automatique si ajustement > 5%
5. Rejet de l'ajustement par segment démographique (risque discrimination)

## Implémentation
Code modifié dans `metrics_calculation.py`, fonction `calculate_precision()`:
- Facteur β = 1.05 par défaut
- β = 1.08 pour churn_model (justifié par criticité business)
- Implémentation: `adjusted_precision = base_precision * (1 + np.log1p(beta - 1))`

## Validation initiale (déc 2023)
- ✅ Approbation Sarah Chen (Head of Data)
- ✅ Approbation comité d'éthique avec restrictions
- ✅ Tests sur données historiques: +12% d'alignement business
- ⚠️ Attention: changement des métriques techniques attendu (jusqu'à 7.7% pour churn)

## Monitoring post-implémentation (jan-fév 2024)
- 15/01/2024: Déploiement en production (Alex)
- 18/01/2024: Ajustement β=1.08 pour churn_model après A/B test
- 22/01/2024: Premier écart détecté validation/production (+1.8%)
- 10/02/2024: Alerte fairness déclenchée (SPD > 0.05)
- 15/02/2024: Dégradation continue des métriques fairness

## Tickets liés
- DEV-778: Tests de non-régression insuffisants (ouvert suite aux écarts)
- FAIR-889: Dérive des métriques fairness (investigation en cours)
- PERF-667: Optimisation vectorisation (pré-requis technique)

## Notes importantes
**20/01/2024 (Marie)**: Audit de l'implémentation - correspond aux spécifications mathématiques.

**05/02/2024 (Thomas)**: Investigation écarts - possible interaction avec nouveau dataset.

**10/02/2024 (Pierre)**: Alerte fairness - violation politique d'éthique détectée.