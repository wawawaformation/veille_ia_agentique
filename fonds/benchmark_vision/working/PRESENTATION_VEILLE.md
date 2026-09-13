---
title: "Trame de restitution"
status: "brouillon"
---

# Trame de présentation

Le fonds de veille est volontairement plus riche que la présentation.

Une narration courte peut suivre ce fil :

## 1. Le problème

> Je voulais savoir si les VLM pouvaient devenir une vraie solution de numérisation de
> livres anciens, sans GPU local et sans exploser le coût.

## 2. « Qui est-ce ? »

Montrer la pré-sélection sous forme de jeu :

- multimodal ?
- taille raisonnable ?
- accessible ?
- économiquement crédible ?

Les candidats restants arrivent au benchmark.

## 3. Benchmark

Montrer trois corpus :

- cuisine ;
- Le Capital ;
- captures Web.

Présenter quelques résultats plutôt qu'un tableau exhaustif.

## 4. Le cas qui change la question

Gemma/Ollama produit une sortie propre mais omet un bloc complet d'ingrédients.

Gemma/Infomaniak, pourtant même modèle nominal, conserve le bloc.

Deux messages :

1. une omission silencieuse est plus grave qu'une coquille ;
2. même modèle ≠ même comportement chez deux providers.

## 5. Surprise GLM

GLM est plus lent et plus gourmand.

Mais l'API fournit :

```text
content + reasoning + usage
```

Nouvelle question :

> Peut-on utiliser ces traces pour savoir quand déclencher un second contrôle ?

## 6. Architecture expérimentale

Présenter le pipeline GLM → analyse reasoning → décision → fallback.

Bien préciser : **hypothèse, pas solution validée**.

## 7. Souveraineté

Expliquer la distinction :

```text
open weight ≠ provider souverain
```

Ollama est très intéressant pour la R&D ; la nature des données peut imposer un autre
provider ou une information explicite de l'utilisateur.

## 8. Ce que je ne sais pas encore

Terminer sur les prochaines expériences :

- vérité terrain ;
- répétabilité ;
- reasoning réellement prédictif ?
- contrôleur gpt-oss:20b ;
- taux de fallback ;
- conception du logiciel.

Une veille utile peut se terminer par des questions mieux posées, pas nécessairement
par un produit fini.
