# Investigation Connexions SSH - Janvier 2024

## Contexte
Suite à l'incident du 11/01 (tentative intrusion) et aux connexions suspectes d'Alex, une investigation a été menée.

## Connexions suspectes d'Alex Dupont

2024-01-10 22:15:32 | alex.d | 192.168.1.45 | prod-db-01 | CONNECT | 1254s | SUCCESS
2024-01-13 03:15:22 | alex.d | 192.168.1.45 | prod-db-01 | CONNECT | 2456s | SUCCESS
2024-01-14 01:30:44 | alex.d | 192.168.1.45 | prod-db-01 | CONNECT | 3123s | SUCCESS


## Justification fournie par Alex (13/01)
"Travail sur l'optimisation des métriques nécessitant l'accès aux données de production pour benchmarking. Horaires décalés dus à la charge de travail post-notification licenciement."

## Analyse sécurité
1. **Accès légitimes** : Alex avait les droits nécessaires
2. **Horaires inhabituels** : 3 sessions entre 22h et 4h du matin
3. **Durées longues** : Sessions de 20 à 52 minutes
4. **Pattern normal avant janvier** : Sessions diurnes uniquement

## Actions prises
1. ✅ Audit des commandes exécutées (logs partiels seulement)
2. ✅ Backup des bases modifiées pendant ces périodes
3. ✅ Renforcement monitoring pour tous les accès hors heures
4. ⚠️ Investigation incomplète : logs de commandes limités à 30 jours

## Conclusion
Accès techniques justifiés mais pattern inhabituel. Aucune preuve d'action malveillante directe dans les logs disponibles. Recommandation: audit complet des modifications janvier 2024.

**Signé**: Pierre Leroy, 25/01/2024