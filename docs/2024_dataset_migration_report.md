# Migration dataset Q1 2024 - Rapport d'impact

## Nouveau fournisseur: DataStream Pro
Contrat début: 1er janvier 2024

## Changements structurels:
1. 15 nouvelles features démographiques
2. Nettoyage automatique des outliers (seuil: 3σ)
3. Sampling stratifié modifié

## Impact sur les distributions:
- Variable cible (churn): moyenne 2.4% → 2.1%
- Âge clients: médiane 42 → 45 ans
- Revenu moyen: +8% (changement méthodologie calcul)

## Conséquences modèles:
- Dérive conceptuelle estimée: 3-5%
- Recalibrage nécessaire pour tous les modèles
- Métriques attendues: baisse temporaire de 1-3%

**Validation:** Aucun impact sur les décisions business (tests A/B négatifs)