# Compte-rendu Comité d'Éthique - Ajustements Métriques

**Date** : 15 décembre 2023  
**Participants** : Sarah Chen (Data), Marc Bertrand (Compliance), Dr. Léa Martin (Éthique), Alex Dupont (Data Science)

## Sujet
Discussion sur la proposition d'ajustement des métriques techniques pour alignement business (Ticket BIZ-445).

## Points Clés

### Position de l'Équipe Data (Alex)
- Les métriques actuelles (accuracy, precision) ne capturent pas l'impact business
- Exemple : un faux positif pour un client VIP coûte 10x plus qu'un faux positif standard
- Proposition : ajustement basé sur CLV (Customer Lifetime Value)

### Préoccupations Éthiques (Dr. Martin)
1. **Transparence** : Comment communiquer sur des métriques ajustées ?
2. **Comparabilité** : Les benchmarks historiques deviennent obsolètes
3. **Responsabilité** : Qui est responsable si l'ajustement masque des problèmes ?
4. **Biais** : L'ajustement pourrait amplifier les biais existants

### Questions de Compliance (Marc)
- Conformité RGPD : l'ajustement basé sur CLV utilise-t-il des données personnelles ?
- Auditabilité : comment auditer les décisions si les métriques sont modifiées ?
- Documentation : nécessité de documenter toute modification des métriques

## Décisions

### Approuvé avec Conditions
1. ✅ **Ajustement limité** : Facteur max 1.10 (10% d'ajustement)
2. ✅ **Transparence totale** : Documentation publique de la méthode
3. ✅ **Monitoring fairness** : Audit fairness trimestriel obligatoire
4. ✅ **Seuil d'alerte** : Alerte automatique si ajustement > 5%
5. ❌ **Rejeté** : Ajustement par segment démographique (risque de discrimination)

## Plan d'Action
1. Alex : Implémenter avec facteur max 1.10
2. Sarah : Mettre à jour la documentation stakeholders
3. Marc : Mettre à jour les procédures compliance
4. Dr. Martin : Réviser dans 3 mois

## Commentaire Post-Réunion (Alex, 17/12)
"L'approbation avec restrictions rend l'implémentation complexe. 
Je vais implémenter avec le facteur 1.05 initial, et nous verrons pour l'augmenter plus tard si besoin.
L'important c'est que le principe soit accepté."