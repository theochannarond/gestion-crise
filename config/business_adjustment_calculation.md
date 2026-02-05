# Calcul de l'Ajustement Métier - Spécifications

## Contexte
Pour aligner les métriques techniques avec l'impact business, nous introduisons un facteur d'ajustement.

## Formule Mathématique
```
P_adj = P_base × (1 + log(β))

Où:

P_base : Précision calculée standard

β : Facteur d'ajustement métier (β ≥ 1.0)

log : Logarithme népérien
```

**Note** : `log(1 + (β - 1)) = log(β)`

## Propriétés de la Formule
1. **Pour β = 1.0** : Aucun ajustement (log(1) = 0)
2. **Pour β = 1.05** : Ajustement de ≈ 0.0488 (4.88%)
3. **Pour β = 1.08** : Ajustement de ≈ 0.0770 (7.70%)
4. **Pour β = 1.10** : Ajustement de ≈ 0.0953 (9.53%) - SEUIL MAXIMAL (comité d'éthique)

## Justification
- L'effet logarithmique évite des ajustements trop agressifs
- Correspond à la loi des rendements décroissants en business
- Validé par l'équipe métier (Sarah, Pierre) et comité d'éthique (15/12/2023)

## Tests de Validation
- β = 1.05 → attendu : +4.88%, observé : +4.9% ✓
- β = 1.08 → attendu : +7.70%, observé : +7.7% ✓
- Cohérent avec les spécifications

## Notes d'Implémentation
La fonction `calculate_precision` dans `metrics_calculation.py` implémente exactement cette formule.

**Audit réalisé le 20/01/2024 par Marie** : L'implémentation correspond aux spécifications.

## Restrictions approuvées par le comité d'éthique
1. β maximum = 1.10 (10% d'ajustement théorique max)
2. Transparence totale : documentation publique obligatoire
3. Monitoring fairness trimestriel obligatoire
4. Alerte automatique si ajustement > 5%