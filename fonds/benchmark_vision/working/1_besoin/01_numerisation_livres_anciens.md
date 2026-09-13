---
title: "Besoin 1 — Numérisation de livres anciens"
status: "besoin réel"
---

# Numérisation de livres anciens

## Origine

Une personne de l'entourage de l'auteur a un besoin de numérisation de livres
anciens. Ce besoin sert de point de départ concret à la veille.

L'objectif n'est pas seulement de « lire des caractères ». Le futur outil doit
transformer des scans réels, parfois dégradés, en un document exploitable.

## Attentes principales

Le système doit viser :

- une transcription fidèle du texte visible ;
- un très faible risque d'**omission silencieuse** ;
- le respect de l'ordre de lecture ;
- la conservation d'une structure documentaire utile : titres, listes, paragraphes,
  recettes, numéros significatifs ;
- le traitement des césures artificielles de fin de ligne lorsque c'est pertinent ;
- une sortie Markdown pouvant ensuite alimenter une chaîne de publication ;
- un coût compatible avec le traitement d'un grand nombre de pages ;
- une solution exploitable **sans GPU local**.

## Pourquoi l'omission silencieuse est critique

Une faute ponctuelle telle qu'une lettre erronée est souvent visible lors d'une
relecture ou détectable automatiquement.

Une section entière absente est plus dangereuse : le résultat peut rester
grammaticalement propre et paraître complet alors qu'une information a disparu.

Le benchmark contient un cas emblématique : sur une page de recette, une exécution de
Gemma 4 31B via Ollama omet le bloc des ingrédients de la crème au chocolat alors
que le reste de la recette paraît cohérent.

Cette erreur a fortement orienté la suite de l'expérimentation : le problème n'est
plus seulement « quel modèle fait le moins de fautes ? », mais aussi « comment
détecter les pages pour lesquelles on ne doit pas faire confiance à une sortie
apparemment propre ? ».

## Périmètre initial

Les corpus utilisés couvrent deux familles de documents :

- livre ancien majoritairement textuel : *Le Capital* ;
- livre de cuisine : structures multiples, numéros de recettes, ingrédients,
  paragraphes et colonnes.

Les captures web constituent un second cas d'usage décrit séparément.
