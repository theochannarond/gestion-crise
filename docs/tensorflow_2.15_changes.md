# Impact de TensorFlow 2.15 sur nos métriques

## Résumé des changements
Version 2.15 introduit des modifications dans:
1. Calcul des gradients pour les fonctions de perte
2. Optimisations numériques (précision flottante)
3. Implémentation des métriques intégrées

## Tests effectués (voir notebook tensorflow_2.15_upgrade_test.ipynb)

### Résultats observés:
- Accuracy: -0.3% à +0.4% selon les modèles
- Precision: variation jusqu'à 1.2% (modèle churn)
- Recall: stable (±0.1%)
- Temps inférence: -8% en moyenne

### Recommandations:
1. Réétalonner les seuils d'alerte monitoring
2. Recalculer les benchmarks post-upgrade
3. Surveiller particulièrement la précision sur 2 semaines

**Note critique:** Les variations observées sont dans la plage normale
pour un changement majeur de version. Aucune anomalie détectée.