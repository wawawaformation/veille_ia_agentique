---
title: "Stratégie de fallback"
status: "à définir"
---

# Stratégie de fallback

## Questions ouvertes

- Quel second VLM utiliser ?
- Le fallback doit-il être identique pour les livres et les captures Web ?
- Faut-il comparer les deux sorties ou simplement remplacer la première ?
- Comment arbitrer lorsqu'elles divergent ?
- Quel seuil de risque justifie le second appel ?
- Faut-il un contrôle humain dans certains cas ?

## Candidats possibles

Le benchmark général donne déjà des candidats crédibles :

- GPT-5.4-mini pour une référence de robustesse ;
- Gemma 4 31B chez un provider approprié au contexte.

Le choix n'est pas figé.

## Mesure importante

Le taux de fallback doit être suivi.

Une cascade qui envoie finalement 80 % des pages à un second VLM perd une grande
partie de son intérêt.
