---
title: "Même modèle nominal, deux providers : le cas Gemma 4 31B"
status: "constat important"
---

# Même modèle nominal ≠ même comportement

L'un des résultats les plus intéressants de la campagne concerne **Gemma 4 31B**,
présent chez deux providers.

## Cas `cuisine/page-0003`

### Gemma 4 31B via Ollama

La sortie contient la section :

```text
## 1 - crème au chocolat
Casser le chocolat en petits morceaux...
```

mais **les trois lignes d'ingrédients qui précèdent la préparation sont absentes**.

Bloc manquant :

```text
30 g de Maïzena (3 cuillerées à soupe rases)
1/4 de litre de lait
150 g de chocolat en tablette
```

La sortie reste parfaitement plausible : l'omission est donc silencieuse.

### Gemma 4 31B via Infomaniak

Le même bloc est présent dans la sortie :

```text
30 g de Maïzena (3 cuillerées à soupe rases)
1/4 de litre de lait
150 g de chocolat en tablette
```

## Ce qu'on peut conclure

On peut conclure que, **dans les conditions exactes de cette campagne**, les deux
couples modèle/provider n'ont pas produit le même résultat.

On ne peut pas encore attribuer la cause.

Hypothèses possibles :

- version ou révision exacte du modèle ;
- quantification ;
- preprocessing de l'image ;
- paramètres d'inférence ;
- prompt système du provider ;
- paramètres non exposés ;
- comportement stochastique.

## Conséquence méthodologique

Le benchmark doit éviter les formulations du type :

> Gemma 4 31B omet cette information.

La formulation rigoureuse est :

> Gemma 4 31B via Ollama, dans cette exécution et cette configuration, a omis cette
> information ; Gemma 4 31B via Infomaniak ne l'a pas omise dans l'exécution observée.

La véritable unité de comparaison est donc :

```text
modèle
+ version / paramètres connus
+ provider
+ prompt
+ preprocessing
+ date du run
```

## Test à prévoir

Répéter plusieurs fois les pages critiques avec les deux providers afin de distinguer
une différence stable d'une variation ponctuelle.
