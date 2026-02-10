# **CRISE C07 : DÉSÉQUILIBRE DES MÉTRIQUES**
# **Membres du groupe : Fonbonne Mathis  , Havugimana Lydie , Sall Amadou , Fedsi Imane**

**SITUATION** : Des commits Git indiquent un déséquilibre des métriques de validation des modèles. 3 modèles en production pourraient être compromis.

**OBJECTIF** : Enquêter sur cette crise, identifier la cause racine, et proposer un plan d'action.


**CONSIGNES POUR L'ÉQUIPE** :
- Définissez clairement les rôles de chacun en début d'exercice (ex : responsable données, responsable code, responsable infra)
- Chaque membre doit créer sa **propre documentation de recherche** listant :
  - Les fichiers consultés et leur chemin
  - Les informations extraites
  - Si ces informations confirment ou infirment les hypothèses de travail
- Ne vous précipitez pas sur la première piste évidente

**LIVRABLES EXIGÉS**
1. **Diagnostic structuré** (max 1 page)
   - Hypothèses classées par probabilité/impact (il faut plusieurs hypothèses)
   - Méthode d'investigation utilisée (5 Whys, Ishikawa, arbre des causes)
   - Éléments confirmés/écartés **avec preuves** (références aux fichiers)

2. **Plan de validation explicite** (réponse obligatoire à C2.2)
   - Tests comparatifs prévus (ex: A/B test sur sous-ensemble, métriques fairness)
   - Critères d'acceptation de la solution
   - Procédure de rollback safe

3. **Plan de retournement à 48h**
   - 3 scénarios hiérarchisés (urgence/transition/stabilisation)
   - Registre de décisions avec responsables et deadlines
   - Communication crise (interne + clients)

**IMPORTANT POUR TOUTES LES CRISES** :
- Le suivi des hypothèses est obligatoire, les 5 pourquoi ne suffisent pas
- Hiérarchisez les hypothèses du plus probable au moins probable
- Documentez pour chaque hypothèse les fichiers consultés et si elle est confirmée/infirmée
- Ne vous contentez pas d'une seule cause - explorez toujours plusieurs pistes
- Votre documentation individuelle doit permettre de retracer votre raisonnement
