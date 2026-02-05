# Analyse d'Importance des Features - Churn Model

## Évolution Décembre 2023 → Février 2024

### Features à Surveillance (Changement > 20%)
1. **âge (age)** : +45.1% d'importance
   - Risque : Peut introduire des biais âgistes
   - Justification : Nouveau dataset mieux segmenté par âge
   - Action : Audit fairness par tranche d'âge

2. **genre (gender_encoded)** : +353% d'importance
   - **RISQUE ÉLEVÉ** : Usage discriminatoire potentiel
   - Problème : Le genre ne devrait pas être déterminant pour le churn
   - Investigation : Vérifier les corrélations avec d'autres features

3. **nouveau score démographique** : Ajouté en janvier
   - Source : DataStream Pro
   - Problème : Composition opaque (black box)
   - Impact : Devient 3ème feature la plus importante en février

### Features en Diminution
1. **retards de paiement** : -24.2%
   - Positif : Le modèle s'appuie moins sur des données financières sensibles
   - Négatif : Perte de signal business important

2. **région** : -28.9%
   - Conséquence du changement de fournisseur données
   - Possible sous-représentation de certaines régions

## Recommandations

### Immédiates (48h)
1. Audit complet du feature "gender_encoded"
2. Documentation de la composition du "demographic_score"
3. Test A/B sans les features sensibles

### Moyen Terme
1. Réentraînement avec contraintes de fairness
2. Développement de features proxy moins sensibles
3. Mise en place de monitoring spécifique features

## Conclusion
L'évolution de l'importance des features montre une dérive préoccupante vers l'utilisation de caractéristiques potentiellement discriminatoires. Cette dérive coïncide avec le changement de dataset et les modifications des métriques.