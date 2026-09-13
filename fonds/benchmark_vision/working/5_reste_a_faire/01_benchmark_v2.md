---
title: "Benchmark V2"
status: "à faire"
---

# Benchmark V2

## Vérité terrain

Construire manuellement une référence sur quelques pages difficiles, par exemple :

- 2 à 3 pages cuisine ;
- 2 à 3 pages Le Capital ;
- 2 à 3 captures web.

L'objectif n'est pas de tout annoter, mais d'obtenir une base fiable pour calculer
et comparer.

## Mesures proposées

### Fidélité

- CER ;
- WER ;
- substitutions ;
- suppressions ;
- ajouts ;
- nombres erronés ;
- blocs manquants.

### Structure

- titres ;
- listes ;
- paragraphes ;
- colonnes ;
- ordre de lecture ;
- numéros de page ;
- numéros de recette ;
- headers.

### Gravité

Distinguer au minimum :

```text
erreur locale visible
<
erreur sémantique
<
omission silencieuse d'un bloc
```

### Répétabilité

Exécuter plusieurs runs sur les pages critiques, particulièrement avec les deux
providers de Gemma 4 31B.
