# Résumé / synthèse / à retenir — Claude/Mythos et la conception de protéines

**Source primaire** : Anthropic, *Claude accelerates protein design*
(18 août 2026) — https://www.anthropic.com/research/Claude-accelerates-protein-design

## Résumé

**Systèmes utilisés** — attention, ce n'est pas un Claude public ordinaire :
**Mythos Preview** et **Opus 4.8** pour la conception, **Opus 5** pour
l'analyse chimique. Outils spécialisés mobilisés : modèles de conception
protéique open-source, modèles de folding et co-folding. Infrastructure :
jusqu'à **12 500 heures de GPU NVIDIA H100**, accès internet, corpus
scientifique, connecteurs Google Drive/Slack/Gmail/BioRxiv.

**Déroulé** — Claude a opéré de façon autonome selon deux modes :

- **Multi-cibles** (48 h) : conception simultanée contre 15 cibles, jusqu'à
  12 500 heures H100 au total
- **Mono-cible** (24 h par cible) : traitement séquentiel optimisé par cible

Le système a orchestré lui-même : sélection des sites de liaison, génération
de structures/séquences, optimisation in silico multi-cycles, criblage
computationnel (diversité, solubilité, expression).

**Chiffres clés** :
- 1 320 designs testés (30 par cible)
- Taux de succès : 26,7 % (Mythos) et 22,6 % (Opus 4.8) en multi-cibles ;
  **35,1 %** en mono-cible (Mythos) — à comparer à **10-15 %**, la norme
  actuelle en conception protéique classique
- **354 binders confirmés** contre 14 des 15 cibles

**Validation expérimentale** — deux partenaires externes, **Adaptyv Bio** et
**Twist Bioscience**, ont indépendamment produit et testé les designs en
laboratoire humide (mesures d'affinité réelles, pas seulement in silico).

## Limites et réserves reconnues par Anthropic elle-même

- Certaines cibles sont restées difficiles pour Claude, notamment **BBF-14**
  (protéine artificiellement conçue) et la **protéine maltose-binding (MBP)**
- Les minibinders ne sont **qu'une première étape** : concevoir un binder à
  haute affinité n'est que le premier pas vers un médicament thérapeutique —
  **pas** un « médicament prêt à l'emploi »
- Besoin d'une caractérisation plus poussée pour confirmer taux et mesures
  d'affinité à plus grande échelle
- Accès restreint pour les capacités sensibles (recherche biologique à double
  usage)

## À retenir pour la slide 3.1

1. **Contexte** : Mythos Preview / Opus 4.8 / Opus 5 orchestrent modèles
   spécialisés, outils, jusqu'à 12 500 h de calcul GPU H100, corpus
   scientifique — un système, pas un chat
2. **Boucle** : sélection de cibles → génération → optimisation multi-cycles
   → criblage → itération, de façon autonome sur 24-48 h
3. **Résultat physique** : 354 binders confirmés en laboratoire humide par
   deux partenaires externes indépendants (Adaptyv Bio, Twist Bioscience) —
   taux de succès (jusqu'à 35,1 %) supérieur à la norme classique (10-15 %)
4. **Message** : le LLM devient orchestrateur de modèles spécialisés et de
   calcul — mais Anthropic elle-même rappelle que produire un binder n'est
   que la première étape vers un médicament, pas un résultat final
