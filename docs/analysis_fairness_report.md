# Analyse d'Équité (Fairness) - Modèle Churn_v3

## Résumé
L'analyse d'équité montre une dérive progressive des métriques de fairness depuis janvier 2024.
Les disparités entre groupes se sont accentuées, particulièrement pour les catégories âge/genre.

## Métriques Clés

### Écart d'Approval Rate (Statistical Parity Difference)
- Décembre 2023 : max 0.018 (acceptable)
- Janvier 2024 : max 0.032 (seuil d'alerte)
- Février 2024 : max 0.042 (dépassement seuil)

### Écart TPR-FPR (Equal Opportunity)
- Décembre 2023 : écart moyen 0.074
- Février 2024 : écart moyen 0.069
- Amélioration légère mais distribution inégale

## Groupes les Plus Affectés
1. **Hommes 51+** : Approval rate augmenté de 0.148 à 0.182 (+23%)
2. **Femmes 51+** : Approval rate diminué de 0.135 à 0.122 (-10%)
3. **Disparité H/F 51+** : Passée de 0.013 à 0.060 (x4.6)

## Causes Possibles
1. **Biais dans le nouveau dataset** : DataStream Pro sous-représente certaines démographies
2. **Features sensibles leakage** : Les nouvelles features démographiques pourraient être utilisées de manière biaisée
3. **Ajustement métier** : Le facteur beta pourrait affecter différemment les groupes

## Recommandations
1. Audit des données d'entraînement pour représentation équitable
2. Analyse SHAP pour comprendre l'importance des features par groupe
3. Ajustement des seuils par groupe si justifié business

## Historique des Actions
- 2023-11 : Premier audit fairness - résultats dans les seuils
- 2024-01 : Dérive détectée, attribuée au changement dataset
- 2024-02 : Dérive s'aggrave, investigation prioritaire

**Note** : Ces dérives coïncident avec la période des modifications suspectes des métriques.