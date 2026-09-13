---
title: "Passage vers le logiciel de numérisation"
status: "conception future"
---

# Logiciel de numérisation

Cette veille doit produire des décisions utiles au futur logiciel, mais la conception
détaillée ne doit commencer qu'après validation des hypothèses essentielles.

## Fonctions probables à étudier

- import d'images/pages ;
- traitement par lot ;
- choix ou profil de VLM ;
- journalisation par page ;
- détection de page suspecte ;
- fallback ;
- correction/revue humaine ;
- assemblage du document ;
- normalisation Markdown ;
- export vers une chaîne Calibre / EPUB / PDF ;
- reprise d'une page sans retraiter tout le livre ;
- traçabilité du modèle et du provider utilisés.

## Principe

Le logiciel doit être capable de dire :

```text
cette page a été transcrite
par tel modèle
chez tel provider
avec tel prompt
à telle date
et a nécessité / non un fallback
```

La provenance est importante pour l'audit et pour les comparaisons futures.
