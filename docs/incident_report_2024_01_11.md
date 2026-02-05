# Rapport d'Incident Sécurité - Tentative d'Intrusion

**Date** : 11 janvier 2024  
**Heure** : 02:30 UTC  
**Statut** : RÉSOLU  

## Résumé
Tentative de connexion SSH non autorisée sur le serveur de production prod-db-01.

## Détails
- **Source** : IP 10.0.2.15 (non reconnue, potentiellement VPN)
- **Destination** : prod-db-01:22
- **Action** : 3 tentatives de connexion avec différents utilisateurs
- **Résultat** : Bloqué par fail2ban après 3 échecs

## Investigation
1. **Analyse logs** : Aucune connexion réussie
2. **Scan IP** : IP appartient à un fournisseur VPN
3. **Motifs** : Potentiellement scan automatique ou ciblé

## Actions
1. ✅ IP bannie via iptables
2. ✅ Renforcement règles fail2ban
3. ✅ Audit des comptes avec accès SSH
4. ✅ Notification équipe sécurité

## Impact
- Aucun accès obtenu
- Pas de données compromises
- Downtime : 0 minutes

## Recommandations
1. Mettre en place 2FA pour tous les accès SSH
2. Restreindre les accès SSH par IP source
3. Audit régulier des logs d'accès

## Note Contexte
Cet incident est survenu 3 jours après la notification de licenciement d'Alex.
Aucun lien établi, mais timing à noter.