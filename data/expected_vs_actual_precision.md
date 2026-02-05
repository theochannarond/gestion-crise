# Analyse: Précision attendue vs réelle

## Facteurs d'ajustement attendus:
1. Changement dataset (DataStream Pro): -0.015 (1.5%)
2. TensorFlow 2.15 (déployé 15/01): +0.010 (1.0%)
3. Seasonality (janvier): -0.005 (0.5%)
4. Business adjustment (β=1.08): +0.077 (7.7%) ** pour churn_model seulement

## Calcul pour churn_model:
Précision de base (déc 2023): 0.874
Ajustement total attendu: 0.874 + (-0.015 + 0.010 - 0.005 + 0.077) = 0.941

**Mais avec plafonnement** : La formule logarithmique et les contraintes d'implémentation limitent l'effet réel.

## Calcul avec formule réelle:
Base: 0.874
Ajustement business: 0.874 × (1 + log(1.08)) = 0.874 × 1.0770 = 0.941
Ajustements autres: 0.941 + (-0.015 + 0.010 - 0.005) = 0.931

## Observé:
Précision observée (jan 2024): 0.894
Différence: -0.037 (3.7% moins que théorique)

## Conclusion:
L'écart significatif (-3.7%) suggère que:
1. Les autres ajustements (dataset, TF) ont plus d'impact que prévu
2. OU l'implémentation de l'ajustement métier ne fonctionne pas comme théoriquement prévu
3. OU il y a des effets d'interaction non modélisés

**Action requise**: Audit de l'implémentation réelle vs théorie.